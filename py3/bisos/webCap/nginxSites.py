# -*- coding: utf-8 -*-

""" #+begin_org
* Overview: the web sites this host's nginx serves, from nginx -T.

nginx has no command that lists its server names. nginx -T tests the configuration and prints all of
it, every included file preceded by "# configuration file <path>:". That is what nginx loaded, so it is
the source here, not the names of the files in sites-enabled/.

sitesEnabled() parses it into Site records: the server names, the listen lines, the file, and what
location / does (root/alias: a base directory; proxy_pass: a proxied target). Used by
webSitesEnabled.cs (list, verify, browse, report, baseFind).
#+end_org """

import dataclasses
import os
import pathlib
import re
import shutil
import subprocess
import urllib.error
import urllib.request


@dataclasses.dataclass
class Site:
    serverNames: list[str]
    file: str
    listens: list[list[str]] = dataclasses.field(default_factory=list)
    root: str | None = None          # root or alias of location / (else of the server)
    proxyPass: str | None = None     # proxy_pass of location /

    def fqdns(self) -> list[str]:
        """The server names a browser can open: not "_", not wildcards, not regex (~...)."""
        return [n for n in self.serverNames
                if n not in ("_", '""', "") and "*" not in n and not n.startswith("~")]

    def isSsl(self) -> bool:
        return any("ssl" in each[1:] for each in self.listens)

    def port(self) -> int | None:
        """The port of the first listen line of the scheme in use; None for the scheme's default."""
        ssl = self.isSsl()
        for each in self.listens:
            if ("ssl" in each[1:]) != ssl:
                continue
            m = re.search(r"(\d+)$", each[0])
            portNu = int(m.group(1)) if m else (443 if ssl else 80)
            return None if portNu == (443 if ssl else 80) else portNu
        return None

    def url(self, fqdn: str) -> str:
        portNu = self.port()
        return f"{'https' if self.isSsl() else 'http'}://{fqdn}{f':{portNu}' if portNu else ''}/"


def nginxDumpConfig() -> str:
    """The output of nginx -T, run as root (sudo -n when not root). Raises RuntimeError on failure."""
    nginx = shutil.which("nginx") or "/usr/sbin/nginx"
    cmd = [nginx, "-T"] if os.geteuid() == 0 else ["sudo", "-n", nginx, "-T"]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(f"{' '.join(cmd)} failed: {proc.stderr.strip()}")
    return proc.stdout


_tokenRe = re.compile(r'"(?:[^"\\]|\\.)*"|\'(?:[^\'\\]|\\.)*\'|[{};]|[^\s{};]+')


def parseSites(dump: str) -> list[Site]:
    """Site records of every http server block in an nginx -T dump.

    nginx -T prints each file in a section of its own, an included file after the one including it, so
    a sites-enabled/ file's server block is at the top of its section, not inside http {}. A server
    block counts when it is at the top of a section or directly inside http (not stream, not mail).
    """
    sites: list[Site] = []
    stack: list[tuple[str, list[str]]] = []   # (block name, its arguments), within the current file
    words: list[str] = []
    curFile = ""
    site: Site | None = None
    for line in dump.splitlines():
        m = re.match(r"# configuration file (.+):$", line)
        if m:
            curFile, stack, words, site = m.group(1), [], [], None
            continue
        line = re.sub(r"(^|\s)#.*$", "", line)
        for tok in _tokenRe.findall(line):
            if tok == "{":
                name, args = (words[0], words[1:]) if words else ("", [])
                stack.append((name, args))
                if name == "server" and [s for s, _ in stack[:-1]] in ([], ["http"]):
                    site = Site(serverNames=[], file=curFile)
                words = []
            elif tok == "}":
                if stack:
                    name, _ = stack.pop()
                    if name == "server" and site is not None and [s for s, _ in stack] in ([], ["http"]):
                        sites.append(site)
                        site = None
                words = []
            elif tok == ";":
                if site is not None and words:
                    _statement(site, stack, words)
                words = []
            else:
                words.append(tok.strip("\"'") if tok[0] in "\"'" else tok)
    return sites


def _statement(site: Site, stack: list[tuple[str, list[str]]], words: list[str]) -> None:
    inner = stack[[s for s, _ in stack].index("server") + 1:]
    directive, args = words[0], words[1:]
    if not inner:
        if directive == "server_name":
            site.serverNames += args
        elif directive == "listen" and args:
            site.listens.append(args)
        elif directive == "root" and args and site.root is None:
            site.root = args[0]
    elif len(inner) == 1 and inner[0][0] == "location" and inner[0][1] in (["/"], ["=", "/"]):
        if directive in ("root", "alias") and args:
            site.root = args[0]
        elif directive == "proxy_pass" and args:
            site.proxyPass = args[0]


def sitesEnabled(dump: str | None = None) -> list[Site]:
    """The Site records of this host's nginx (nginx -T when dump is None)."""
    return parseSites(nginxDumpConfig() if dump is None else dump)


def fqdnUrls(sites: list[Site]) -> list[tuple[str, str, Site]]:
    """(fqdn, url, site) of every browsable server name, sorted by fqdn, each fqdn once."""
    seen: dict[str, tuple[str, str, Site]] = {}
    for site in sites:
        for fqdn in site.fqdns():
            seen.setdefault(fqdn, (fqdn, site.url(fqdn), site))
    return [seen[k] for k in sorted(seen, key=str.lower)]


def siteOf(fqdn: str, sites: list[Site]) -> Site | None:
    for site in sites:
        if fqdn in site.serverNames:
            return site
    return None


def baseDir(site: Site) -> pathlib.Path | None:
    """The directory location / is served from (root/alias), resolved; None for a proxied site."""
    return pathlib.Path(site.root).resolve() if site.root else None


class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):  # noqa: D102
        return None


def httpStatus(url: str, timeout: float = 5.0) -> str:
    """The HTTP status of url, without following redirects or proxies; else the error, briefly."""
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}), _NoRedirect())
    try:
        with opener.open(url, timeout=timeout) as resp:
            return str(resp.status)
    except urllib.error.HTTPError as e:
        return str(e.code)
    except urllib.error.URLError as e:
        return f"error: {e.reason}"
    except Exception as e:  # timeouts, resets
        return f"error: {e}"


def browserCommand(urls: list[str]) -> list[list[str]]:
    """Commands that open urls as tabs: one firefox call; else xdg-open per url."""
    if shutil.which("firefox"):
        cmd = ["firefox"]
        for url in urls:
            cmd += ["--new-tab", url]
        return [cmd]
    return [["xdg-open", url] for url in urls]


def browse(urls: list[str]) -> list[list[str]]:
    """Open urls in the browser of this display, detached. Returns the commands run."""
    cmds = browserCommand(urls)
    for cmd in cmds:
        subprocess.Popen(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                         start_new_session=True)
    return cmds
