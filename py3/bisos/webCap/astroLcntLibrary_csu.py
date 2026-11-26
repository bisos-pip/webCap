# -*- coding: utf-8 -*-
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars |]]* :: The Library and the LCNT access pages of an astro site, generated from what lcnt landed
** This File: /bisos/git/bxRepos/bisos-pip/webCap/py3/bisos/webCap/astroLcntLibrary_csu.py
** Authors: Mohsen BANAN, http://mohsen.banan.1.byname.net/contact
#+end_org """

####+BEGIN: b:py3:cs:file/dblockControls :classification "cs-u"
""" #+begin_org
* [[elisp:(org-cycle)][| /Control Parameters Of This File/ |]] :: dblk ctrls classifications=cs-u
#+BEGIN_SRC emacs-lisp
(setq-local b:dblockControls t) ; (setq-local b:dblockControls nil)
(put 'b:dblockControls 'py3:cs:Classification "cs-u") ; one of cs-mu, cs-u, cs-lib, bpf-lib, pyLibPure
#+END_SRC
#+RESULTS:
: cs-u
#+end_org """
####+END:

####+BEGIN: b:py3:file/particulars-csInfo :status "inUse"
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars-csInfo |]]*
#+end_org """
if 'csInfo' not in globals(): import typing ; csInfo: typing.Dict[str, typing.Any] = { 'moduleName': ['loadAs'], }
csInfo['version'] = '202611143854'
csInfo['status']  = 'inUse'
csInfo['panel'] = 'astroLcntLibrary_csu-Panel.org'
csInfo['groupingType'] = 'IcmGroupingType-pkged'
csInfo['cmndParts'] = 'IcmCmndParts[common] IcmCmndParts[param]'
####+END:

""" #+begin_org
* [[elisp:(org-cycle)][| ~Description~ |]] :: Pages for the LCNT documents a site declares in its lcntSpecs/
A site declares the LCNT releases it publishes in =<siteBase>/lcntSpecs/*.pyl=, kept in the site's git: one Python
literal per release (read with ast.literal_eval, never eval), written by the lcnt =localWeb= export (bisos.lcnt). Each
points at the release: its canonical path (=/de/sys/lcnt/...=), else its BXO and the path in it. =landAll= rebuilds
=<siteBase>/var/lcnt/= wholly from those specs (var/ is a cache, outside git): =<class>/<number>/<release>/= with the
release's files and =meta.pyl=. =libraryGenerate= turns what is landed into
*content-tree nodes*, which the site renders like any other page (no JavaScript of its own, no per-site wrapper pages):
=content/tree/lcnt/<class>/<number>/<release>/accessPage/=, the latest-release alias =.../<number>/accessPage/=, and
=content/tree/library/index_html/=. They are generated whole on every run (built aside, renamed in), and a site keeps
them out of git. The access pages' look is =/bisos/asc/web/astro/lcntLibrary/lcntLibrary.css=, copied into each page.
The site needs the page parameter =layoutBare= (no footer, no tree heading) in its layout. Standard library only.
=build= (landAll, then generate) is what the site's =contentBuild= runs when the site has =lcntSpecs/=.
** Status: In use with BISOS
** /[[elisp:(org-cycle)][| Planned Improvements |]]/ :
*** TODO Embed the document only when it is a plain HeVeA article; a presentation shows its formats only.
#+end_org """

####+BEGIN: b:py3:cs:framework/imports :basedOn "classification"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CsFrmWrk   [[elisp:(outline-show-subtree+toggle)][||]] *Imports* =Based on Classification=cs-u=
#+end_org """
from bisos import b  # noqa: E402
from bisos.b import cs
from bisos.b import b_io
from bisos.common import csParam

import collections
####+END:

import ast
import datetime
import html
import os
import pathlib
import pprint
import re
import shutil
import subprocess

from bisos.webCap import astroSite_csu

styleSheetPath = pathlib.Path("/bisos/asc/web/astro/lcntLibrary/lcntLibrary.css")

specsDirName = "lcntSpecs"
specVersion = 1
# Where an activated BXO is on any BISOS host: a BRO by its <org>/<repo>, a BPO by its id.
bxoRoots = {"bro": pathlib.Path("/bisos/git/bxRepos"), "bpo": pathlib.Path("/bxo")}
htmlSuffixes = frozenset(['.html', '.htm', '.css', '.png', '.jpg', '.jpeg', '.gif', '.svg'])

####+BEGIN: b:py3:cs:orgItem/section :title "Common Parameters Specification" :comment "based on cs.param.CmndParamDict -- As expected from CSU-s"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  /Section/    [[elisp:(outline-show-subtree+toggle)][||]] *Common Parameters Specification* based on cs.param.CmndParamDict -- As expected from CSU-s  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: b:py3:cs:func/typing :funcName "commonParamsSpecify" :comment "~CSU Specification~" :funcType "ParSpc" :deco ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-ParSpc [[elisp:(outline-show-subtree+toggle)][||]] /commonParamsSpecify/  ~CSU Specification~  [[elisp:(org-cycle)][| ]]
#+end_org """
def commonParamsSpecify(
####+END:
        csParams: cs.param.CmndParamDict,
) -> None:
    pass

####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "Library" :anchor ""  :extraInfo "Generating the pages"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _Library_: |]]  Generating the pages  [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:

def styleSheet() -> str:
    """ The access pages' stylesheet, shared by all sites (empty, with a note on stderr, when it is missing). """
    try:
        return styleSheetPath.read_text()
    except OSError as err:
        b_io.eh.problem_usageError(f"No stylesheet for the access pages: {err}")
        return ""


LABELS = {"html": "HTML", "pdf": "PDF", "bib": "BibTeX"}
NOTES = {
    "html": "Displays the document as a web page.",
    "pdf": "For reading and printing.",
    "bib": "The citation entry.",
}
LIBRARY_TITLE = "Library"


def esc(text):
    return html.escape(str(text), quote=True)


def size_of(nbytes):
    """301453 -> '294 KB'; 754 -> '754 bytes'; over a megabyte -> '1.2 MB'."""
    if nbytes < 1024:
        return f"{nbytes} bytes"
    if nbytes < 1024 * 1024:
        return f"{int(nbytes / 1024 + 0.5)} KB"
    return f"{nbytes / 1024 / 1024:.1f} MB"


def natural_key(tag):
    """Release tags in numeric order: 0.10 after 0.9."""
    return [int(part) if part.isdigit() else part for part in re.split(r"(\d+)", tag)]


def read_meta(path):
    """The release's meta, or None when it cannot be read as a literal (code in the file is refused, not run)."""
    try:
        meta = ast.literal_eval(path.read_text())
    except (OSError, ValueError, SyntaxError, MemoryError, RecursionError):
        return None
    return meta if isinstance(meta, dict) else None


def releases_of(var_lcnt):
    """{class: {lcntNu: [meta, ...newest first]}}; each meta gains lcntClass, lcntNu and relTag from its directory."""
    found = {}
    if not var_lcnt.is_dir():
        return found
    for cls in sorted(var_lcnt.iterdir()):
        for nu in sorted(cls.iterdir()) if cls.is_dir() and not cls.name.startswith(".") else []:
            if not nu.is_dir() or nu.name.startswith("."):
                continue
            for rel in nu.iterdir():
                if not rel.is_dir() or rel.name.startswith("."):
                    continue
                meta = read_meta(rel / "meta.pyl")
                if meta is None:
                    continue
                meta.update(lcntClass=cls.name, lcntNu=nu.name, relTag=rel.name)
                found.setdefault(cls.name, {}).setdefault(nu.name, []).append(meta)
    for nus in found.values():
        for rels in nus.values():
            rels.sort(key=lambda m: natural_key(m["relTag"]), reverse=True)
    return found


def file_base(meta):
    return f"/lcnt/{meta['lcntClass']}/{meta['lcntNu']}/{meta['relTag']}"


def release_path(meta):
    return f"{file_base(meta)}/accessPage/"


def latest_path(meta):
    return f"/lcnt/{meta['lcntClass']}/{meta['lcntNu']}/accessPage/"


def embedded(meta, var_lcnt):
    """The release's HeVeA html as (<style> blocks, body) with relative src and href made absolute; None without html."""
    entry = meta.get("html")
    if not entry:
        return None
    try:
        text = (var_lcnt / meta["lcntClass"] / meta["lcntNu"] / meta["relTag"] / entry).read_text()
    except OSError:
        return None
    body = re.search(r"<body[^>]*>([\s\S]*)</body>", text, re.I)
    if not body:
        return None
    css = "\n".join(re.findall(r"<style[^>]*>([\s\S]*?)</style>", text, re.I))
    base = f"{file_base(meta)}/{os.path.dirname(entry)}/"
    fixed = re.sub(
        r'(\s(?:src|href))="(?![a-z][a-z0-9+.-]*:|/|#)([^"]*)"',
        lambda m: f'{m.group(1)}="{base}{m.group(2)}"',
        body.group(1),
        flags=re.I,
    )
    return css, fixed


SEP = ' <span aria-hidden="true">›</span>'


def access_body(meta, rels, alias, var_lcnt):
    """The body of an access page: crumbs, heading, vitals, formats, description, then the document."""
    title = [meta.get(k) for k in ("title", "subTitle", "subSubTitle")]
    title = [t for t in title if t]
    out = ['<nav class="crumbs" aria-label="Breadcrumb">']
    out.append(f'  <a href="/library/">lcnt</a>{SEP}')
    out.append(f'  <a href="/library/">{esc(meta["lcntClass"])}</a>{SEP}')
    out.append(f'  <a href="{latest_path(meta)}">{esc(meta["lcntNu"])}</a>{SEP}')
    if not alias:
        out.append(f'  <a href="{release_path(meta)}">{esc(meta["relTag"])}</a>{SEP}')
    out.append("  <span>accessPage</span>")
    out.append("</nav>")
    out.append(f"<h1>{esc(meta.get('title', meta['lcntNu']))}</h1>")
    for line in title[1:]:
        out.append(f'<p class="accessSubtitle">{esc(line)}</p>')
    if alias:
        out.append(
            f'<p class="description">This is the latest release, {esc(meta["relTag"])}. To cite this version, use '
            f'<a href="{release_path(meta)}">{release_path(meta)}</a>.</p>'
        )

    versions = " · ".join(
        f'<a href="{release_path(r)}"'
        + (' class="thisRelease"' if r["relTag"] == meta["relTag"] else "")
        + f'>{esc(r.get("version") or r["relTag"])}</a>'
        for r in rels
    )
    facts = [
        ("Document Number", esc(meta.get("docNumber") or meta["lcntNu"])),
        ("Version", versions),
        ("Dated", esc(meta["date"]) if meta.get("date") else None),
        ("Group", esc(meta["group"]) if meta.get("group") else None),
        ("Author(s)", esc(", ".join(meta.get("authors") or []))),
        ("Organization", esc(meta["organization"]) if meta.get("organization") else None),
        ("See Also", esc(meta["seeAlso"]) if meta.get("seeAlso") else None),
        ("Primary URL", f'<a href="{esc(meta["url"])}">{esc(meta["url"])}</a>' if meta.get("url") else None),
    ]
    out.append('<table class="perf accessFacts">')
    out.append("  <tbody>")
    for name, value in facts:
        if value:
            out.append(f'    <tr><th scope="row">{name}</th><td>{value}</td></tr>')
    out.append("  </tbody>")
    out.append("</table>")

    if meta.get("formats"):
        out.append('<h2 class="accessLabel">Available formats</h2>')
        out.append('<ul class="accessFormats">')
        several = sum(1 for f in meta["formats"] if f["kind"] == "pdf") > 1
        for f in meta["formats"]:
            kind = f["kind"]
            label = LABELS.get(kind, kind)
            if several and kind == "pdf" and f.get("build"):
                build = f["build"]
                prefix = f'{meta.get("title", "")}-'
                label += f' ({build[len(prefix):] if prefix != "-" and build.startswith(prefix) else build})'
            out.append(
                f'  <li><a href="{file_base(meta)}/{esc(f["path"])}"><strong>{esc(label)}</strong></a>'
                f'<span class="description"> — {size_of(f["bytes"])} — {esc(NOTES.get(kind, ""))}</span></li>'
            )
        out.append("</ul>")

    if meta.get("description"):
        out.append('<h2 class="accessLabel">Short description</h2>')
        out.append(f'<p class="accessDescription">{esc(meta["description"])}</p>')

    doc = embedded(meta, var_lcnt)
    # the shared look is wanted with or without an embedded document; the site's reader moves it into the <head>
    out.append(f"<style>{styleSheet()}\n{doc[0] if doc else ''}</style>")
    if doc:
        css, body = doc
        out.append('<h2 class="accessLabel libdocHeading">The document</h2>')
        out.append('<hr class="libdocRule" />')
        out.append(f'<article class="libdoc">{body}</article>')
    return "\n".join(out) + "\n"


def library_body(found):
    """The Library page's body: one row per document, highest number first."""
    docs = []
    for cls, nus in found.items():
        for nu, rels in nus.items():
            docs.append((nu, rels))
    if not docs:
        return "<p>No document has been exported to this site yet.</p>\n"
    docs.sort(key=lambda d: d[0], reverse=True)
    out = ['<table class="perf library">', "  <thead>",
           "    <tr><th>Number</th><th>Title</th><th>Version</th><th>Date</th><th>Read</th></tr>",
           "  </thead>", "  <tbody>"]
    for nu, rels in docs:
        latest = rels[0]
        sub = f'<br /><span class="description">{esc(latest["subTitle"])}</span>' if latest.get("subTitle") else ""
        versions = " · ".join(
            f'<a href="{release_path(r)}">{esc(r.get("version") or r["relTag"])}</a>' for r in rels
        )
        read = []
        if latest.get("html"):
            read.append(f'<a href="{file_base(latest)}/{esc(latest["html"])}">HTML</a>')
        read += [f'<a href="{file_base(latest)}/{esc(p)}">PDF</a>' for p in latest.get("pdfs") or []]
        out.append(
            f'    <tr><td>{esc(nu)}</td><td><a href="{latest_path(latest)}">{esc(latest.get("title", nu))}</a>{sub}</td>'
            f'<td>{versions}</td><td>{esc(latest.get("date", ""))}</td><td>{" · ".join(read)}</td></tr>'
        )
    out += ["  </tbody>", "</table>"]
    return "\n".join(out) + "\n"


def write_node(directory, params, body=None):
    """A content-tree node: one file per parameter, and contentBody.html when there is a body."""
    directory.mkdir(parents=True, exist_ok=True)
    for name, value in {"_tree_": "node", "pubState": "publish", **params}.items():
        (directory / name).write_text(f"{value}\n")
    if body is not None:
        (directory / "contentBody.html").write_text(body)


def replace_dir(new, final):
    """Rename `new` over `final`, keeping the old one aside until the new one is in."""
    old = final.with_name(f".{final.name}.old")
    if old.exists():
        shutil.rmtree(old)
    if final.exists():
        os.rename(final, old)
    os.rename(new, final)
    if old.exists():
        shutil.rmtree(old)


def generate(base):
    """ Write the access pages and the Library page of the site at base from its var/lcnt; returns (releases, documents). """
    var_lcnt = base / "var" / "lcnt"
    tree = base / "content" / "tree"
    found = releases_of(var_lcnt)

    # The access pages: lcnt/<class>/<nu>/{<rel>/,}accessPage
    new = tree / ".lcnt.new"
    if new.exists():
        shutil.rmtree(new)
    hidden = {"objectType": "folder", "excludeFromNav": "true"}
    write_node(new, {**hidden, "folderTitle": "lcnt"})
    count = 0
    for cls, nus in found.items():
        write_node(new / cls, {**hidden, "folderTitle": cls})
        for nu, rels in nus.items():
            write_node(new / cls / nu, {**hidden, "folderTitle": nu})
            for rel in rels:
                write_node(new / cls / nu / rel["relTag"], {**hidden, "folderTitle": rel["relTag"]})
                page = {"objectType": "page", "excludeFromNav": "true", "layoutBare": "true",
                        "layoutLeftPortlets": "none", "pageTitle": rel.get("title", nu),
                        "pageDescription": rel.get("description", "")}
                write_node(new / cls / nu / rel["relTag"] / "accessPage", page,
                           access_body(rel, rels, False, var_lcnt))
                count += 1
            write_node(new / cls / nu / "accessPage",
                       {**page, "pageTitle": rels[0].get("title", nu), "pageDescription": rels[0].get("description", "")},
                       access_body(rels[0], rels, True, var_lcnt))
    replace_dir(new, tree / "lcnt")

    # The Library tab: the folder node is the site's own (kept in git); its page is generated.
    lib = tree / "library"
    if not (lib / "objectType").is_file():
        write_node(lib, {"objectType": "folder", "folderTitle": LIBRARY_TITLE, "excludeFromNav": "false"})
    description = (lib / "pageDescription").read_text().strip() if (lib / "pageDescription").is_file() else ""
    newPage = lib / ".index_html.new"
    if newPage.exists():
        shutil.rmtree(newPage)
    write_node(newPage, {"objectType": "page", "pageTitle": LIBRARY_TITLE, "pageDescription": description,
                         "excludeFromNav": "false"}, library_body(found))
    replace_dir(newPage, lib / "index_html")
    return count, sum(len(n) for n in found.values())


####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "Landing" :anchor ""  :extraInfo "var/lcnt from lcntSpecs/"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _Landing_: |]]  var/lcnt from lcntSpecs/  [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:

def read_spec(path):
    """(spec, "") or (None, reason): one lcntSpecs/*.pyl, a literal dictionary of a known specVersion."""
    spec = read_meta(path)
    if spec is None:
        return None, f"{path.name}: not a Python literal dictionary"
    if spec.get("specVersion") != specVersion:
        return None, f"{path.name}: specVersion {spec.get('specVersion')!r}, expected {specVersion}"
    for key in ("lcntClass", "lcntNu", "relTag", "release"):
        if not spec.get(key):
            return None, f"{path.name}: {key} is missing"
    for key in ("lcntClass", "lcntNu", "relTag"):
        if "/" in str(spec[key]) or str(spec[key]).startswith("."):
            return None, f"{path.name}: {key} {spec[key]!r} cannot be a directory name"
    return spec, ""


def release_dir_of(spec):
    """(directory, "") or (None, reason): the release on this host, by its canonical path, else by its BXO.

    The BXO and the path in it are the authority; the canonical path (/de/sys/lcnt/...) is the quick way in.
    """
    canonical = spec.get("releaseDir")
    if canonical and pathlib.Path(canonical).is_dir():
        return pathlib.Path(canonical), ""
    kind, bxo, inBxo = spec.get("bxoKind"), spec.get("bxo"), spec.get("bxoPath")
    if kind in bxoRoots and bxo and inBxo:
        repo = bxoRoots[kind] / bxo
        if (repo / inBxo).is_dir():
            return repo / inBxo, ""
        if repo.is_dir():
            return None, f"the {kind.upper()} {bxo} is at {repo} but has no {inBxo} (pull it?)"
        return None, f"the {kind.upper()} {bxo} is not activated on this host (expected at {repo})"
    return None, f"no {canonical} and no BXO to find it in"


def commit_of(directory):
    """The last commit that touched directory, or None (not in git, or never committed)."""
    try:
        out = subprocess.run(["git", "-C", str(directory), "log", "-1", "--format=%H", "--", "."],
                             capture_output=True, text=True, timeout=30)
    except (OSError, subprocess.TimeoutExpired):
        return None
    return out.stdout.strip() or None


def meta_text(meta):
    """meta.pyl's text: one Python literal, formatted by black when it is importable."""
    text = pprint.pformat(dict(sorted(meta.items()))) + "\n"
    try:
        import black
        return black.format_str(text, mode=black.Mode())
    except Exception:                                      # not importable, or black refused: still a valid literal
        return text


def land_release(spec, specName, releaseDir, varLcnt):
    """Copy what spec names from releaseDir into varLcnt/<class>/<nu>/<rel>/ with its meta.pyl; returns the problems."""
    rel = spec["release"]
    final = varLcnt / spec["lcntClass"] / spec["lcntNu"] / spec["relTag"]
    final.mkdir(parents=True)
    problems, files, formats = [], [], []
    for pdf in rel.get("pdfs") or []:
        source = releaseDir / pdf["name"]
        if not source.is_file():
            problems.append(f"{specName}: {source} is missing")
            continue
        shutil.copyfile(source, final / pdf["name"])
        files.append(pdf["name"])
        formats.append({"kind": "pdf", "path": pdf["name"], "bytes": source.stat().st_size, "build": pdf.get("build")})
    htmlEntry = None
    if rel.get("html"):
        source = releaseDir / rel["html"]
        if not source.is_dir():
            problems.append(f"{specName}: {source}/ is missing")
        else:
            out = final / "html"
            out.mkdir()
            for each in sorted(source.iterdir()):
                if each.is_symlink() or not each.is_file() or each.suffix not in htmlSuffixes:
                    continue
                shutil.copyfile(each, out / each.name)
                files.append(f"html/{each.name}")
            nbytes = sum(f.stat().st_size for f in out.iterdir())
            entry = rel.get("htmlEntry")
            if entry and (out / entry).is_file():
                if entry != "index.html":
                    shutil.copyfile(out / entry, out / "index.html")   # a copy: not counted in the size
                    files.append("html/index.html")
                htmlEntry = "html/index.html"
                formats.append({"kind": "html", "path": htmlEntry, "bytes": nbytes})
    for bib in rel.get("bibs") or []:
        source = releaseDir / bib
        if source.is_file():
            shutil.copyfile(source, final / bib)
            files.append(bib)
            formats.append({"kind": "bib", "path": bib, "bytes": source.stat().st_size})
    meta = dict(spec.get("meta") or {})
    meta.update(lcntClass=spec["lcntClass"], lcntNu=spec["lcntNu"], relTag=spec["relTag"], html=htmlEntry,
                pdfs=[p["name"] for p in rel.get("pdfs") or [] if (final / p["name"]).is_file()],
                formats=formats, files=sorted(files), lcntSpec=specName,
                landedAt=datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"))
    if spec.get("docNumber"):
        meta["docNumber"] = spec["docNumber"]
    (final / "meta.pyl").write_text(meta_text(meta))
    for root, dirs, names in os.walk(final):
        os.chmod(root, 0o755)
        for name in names:
            os.chmod(os.path.join(root, name), 0o644)
    return problems


def land_all(base):
    """Rebuild base/var/lcnt from base/lcntSpecs/*.pyl, whole; returns (landed, problems).

    A release that cannot be found is a problem, and the others are still landed. A release whose last commit is
    not the one recorded at export is landed, with a note (it was changed, or rebuilt, since).
    """
    specs = base / specsDirName
    var = base / "var"
    var.mkdir(exist_ok=True)
    new = var / ".lcnt.new"
    if new.exists():
        shutil.rmtree(new)
    new.mkdir()
    landed, problems, seen = [], [], set()
    for path in sorted(specs.glob("*.pyl")) if specs.is_dir() else []:
        spec, reason = read_spec(path)
        if spec is None:
            problems.append(reason)
            continue
        key = (spec["lcntClass"], spec["lcntNu"], spec["relTag"])
        if key in seen:
            problems.append(f"{path.name}: {'/'.join(key)} is declared twice")
            continue
        seen.add(key)
        releaseDir, reason = release_dir_of(spec)
        if releaseDir is None:
            problems.append(f"{path.name}: {reason}")
            continue
        commit = commit_of(releaseDir)
        if spec.get("bxoCommit") and commit and commit != spec["bxoCommit"]:
            print(f"note: {path.name}: {releaseDir} was committed again since the export "
                  f"({spec['bxoCommit'][:10]} then, {commit[:10]} now)")
        try:
            problems += land_release(spec, path.name, releaseDir, new)
        except OSError as err:
            problems.append(f"{path.name}: cannot land: {err}")
            continue
        landed.append("/".join(key))
    replace_dir(new, var / "lcnt")
    return landed, problems


def build(base):
    """The site's Library from its lcntSpecs/: land_all, then generate. Returns the problems."""
    landed, problems = land_all(base)
    for each in landed:
        print(f"landed: var/lcnt/{each}")
    releases, documents = generate(base)
    print(f"library: {documents} documents, {releases} releases")
    return problems


####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "Direct Command Services" :anchor ""  :extraInfo "Examples and CSs"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _Direct Command Services_: |]]  Examples and CSs  [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "examples_csu" :comment "" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv "pyKwArgs"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<examples_csu>>  =verify= ro=cli pyInv=pyKwArgs   [[elisp:(org-cycle)][| ]]
#+end_org """
class examples_csu(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             pyKwArgs: typing.Any=None,   # pyInv Argument
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Examples of generating the Library and the LCNT access pages of an astro site.
        #+end_org """)

        cmnd = cs.examples.cmndEnter
        cs.examples.menuChapter('=libraryGenerate= -- var/lcnt from lcntSpecs/, then the Library and the access pages')
        cmnd('libraryGenerate', args="astroStarter.internal", comment=" # by FQDN (found through nginx)")
        cmnd('libraryGenerate', args="/bisos/git/bxRepos/bisos-web/astro-starter-bystar", comment=" # or by the site's base directory")
        return(cmndOutcome)


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "libraryGenerate" :comment "" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 1 :argsMax 9999 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<libraryGenerate>>  =verify= argsMin=1 argsMax=9999 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class libraryGenerate(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 1, 'Max': 9999,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             argsList: typing.Optional[list[str]]=None,  # CsArgs
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  For each site (an FQDN, or a base directory when it holds a slash), rebuild its var/lcnt from its lcntSpecs/, then write the Library page and the LCNT access pages as content-tree nodes, and print what was landed and "library: N documents, M releases". The site's contentBuild does the same.
        #+end_org """)

        sites = self.cmndArgsGet("0&-1", cmndArgsSpecDict, argsList)
        if not sites:
            b_io.eh.problem_usageError("No site: give one or more FQDNs or base directories")
            return failed(cmndOutcome)

        allDone = True
        for site in sites:
            if '/' in site:
                base, reason = pathlib.Path(site), ""
                if not (base / 'content' / 'tree').is_dir():
                    base, reason = None, f"{site}: {site}/content/tree is missing"
            else:
                base, reason = astroSite_csu.siteBaseOf(site)
            if base is None:
                b_io.eh.problem_usageError(reason)
                allDone = False
                continue
            try:
                problems = build(base)
            except OSError as err:
                b_io.eh.problem_usageError(f"{base}: {err}")
                allDone = False
                continue
            for problem in problems:
                b_io.eh.problem_usageError(f"{base}: {problem}")
                allDone = False
        if not allDone:
            return failed(cmndOutcome)
        return cmndOutcome.set(opError=b.OpError.Success, opResults=None)

####+BEGIN: b:py3:cs:method/args :methodName "cmndArgsSpec" :methodType "anyOrNone" :retType "bool" :deco "default" :argsList "self"
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Mtd-T-anyOrNone [[elisp:(outline-show-subtree+toggle)][||]] /cmndArgsSpec/ deco=default  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self, ):
####+END:
        """
***** Cmnd Args Specification
"""
        cmndArgsSpecDict = cs.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&-1",
            argName="sites",
            argDefault='',
            argChoices=[],
            argDescription="One or more FQDNs of astro sites, or their base directories"
        )

        return cmndArgsSpecDict

####+BEGIN: b:py3:cs:framework/endOfFile :basedOn "classification"
""" #+begin_org
* [[elisp:(org-cycle)][| *End-Of-Editable-Text* |]] :: emacs and org variables and control parameters
#+end_org """

#+STARTUP: showall

### local variables:
### no-byte-compile: t
### end:
####+END:
