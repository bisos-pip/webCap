# -*- coding: utf-8 -*-

""" #+begin_org
* ~[Summary]~ :: A =CS-Unit= for static sites built with Astro: content, build, verify; for a planted astroProc.spcs.
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

####+BEGIN: b:prog:file/proclamations :outLevel 1
""" #+begin_org
* *[[elisp:(org-cycle)][| Proclamations |]]* :: Libre-Halaal Software --- Part Of BISOS ---  Poly-COMEEGA Format.
** This is Libre-Halaal Software. © Neda Communications, Inc. Subject to AGPL.
** It is part of BISOS (ByStar Internet Services OS)
** Best read and edited  with Blee in Poly-COMEEGA (Polymode Colaborative Org-Mode Enhance Emacs Generalized Authorship)
#+end_org """
####+END:

####+BEGIN: b:prog:file/particulars :authors ("./inserts/authors-mb.org")
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars |]]* :: Authors, version
** This File: /bisos/git/bxRepos/bisos-pip/webCap/py3/bisos/webCap/astroProc_csu.py
** Authors: Mohsen BANAN, http://mohsen.banan.1.byname.net/contact
#+end_org """
####+END:

####+BEGIN: b:py3:file/particulars-csInfo :status "inUse"
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars-csInfo |]]*
#+end_org """
import typing
csInfo: typing.Dict[str, typing.Any] = { 'moduleName': ['astroProc_csu'], }
csInfo['version'] = '202403270908'
csInfo['status']  = 'inUse'
csInfo['panel'] = 'astroProc_csu-Panel.org'
csInfo['groupingType'] = 'IcmGroupingType-pkged'
csInfo['cmndParts'] = 'IcmCmndParts[common] IcmCmndParts[param]'
####+END:

""" #+begin_org
* [[elisp:(org-cycle)][| ~Description~ |]] :: [[file:/bisos/git/auth/bxRepos/blee-binders/bisos-core/COMEEGA/_nodeBase_/fullUsagePanel-en.org][BISOS COMEEGA Panel]]
A BISOS static site keeps its capability, content and site apart, under one directory (=<siteBase>=):
| =astroProc.spcs= | planted on astroProc-seed.cs; declares the fqdn and dev port         |
| =cbm/=           | the capability: CBS, assemble (siteBuild, hereDns, webVirtDom), vhost, dns |
| =content/tree/=  | the content tree (contentTree_csu), engine-neutral                  |
| =content/bin/=   | site-specific content scripts; each writes into =content/data/=     |
| =site/=          | the Astro site; built into =site/dist/=, which nginx serves         |
This module is the Astro-specific processing: contentBuild (pageLcnt bodies, files nodes, then every
executable in content/bin/), siteBuild (contentBuild, then npm ci and astro build in site/), and
siteVerify (the site's pages over HTTP). It works from siteBase, never from the current directory.
Node and npm come from the reactPlus capability; Astro itself is pinned by site/package-lock.json.
** Relevant Panels:
** Status: In use with BISOS
** /[[elisp:(org-cycle)][| Planned Improvements |]]/ :
#+end_org """

####+BEGIN: b:prog:file/orgTopControls :outLevel 1
""" #+begin_org
* [[elisp:(org-cycle)][| Controls |]] :: [[elisp:(delete-other-windows)][(1)]] | [[elisp:(show-all)][Show-All]]  [[elisp:(org-shifttab)][Overview]]  [[elisp:(progn (org-shifttab) (org-content))][Content]] | [[file:Panel.org][Panel]] | [[elisp:(blee:ppmm:org-mode-toggle)][Nat]] | [[elisp:(bx:org:run-me)][Run]] | [[elisp:(bx:org:run-me-eml)][RunEml]] | [[elisp:(progn (save-buffer) (kill-buffer))][S&Q]]  [[elisp:(save-buffer)][Save]]  [[elisp:(kill-buffer)][Quit]] [[elisp:(org-cycle)][| ]]
** /Version Control/ ::  [[elisp:(call-interactively (quote cvs-update))][cvs-update]]  [[elisp:(vc-update)][vc-update]] | [[elisp:(bx:org:agenda:this-file-otherWin)][Agenda-List]]  [[elisp:(bx:org:todo:this-file-otherWin)][ToDo-List]]

#+end_org """
####+END:

####+BEGIN: b:py3:file/workbench :outLevel 1
""" #+begin_org
* [[elisp:(org-cycle)][| Workbench |]] :: [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pyclbr %s" (bx:buf-fname))))][pyclbr]] || [[elisp:(python-check (format "/bisos/venv/py3/bisos3/bin/python -m pydoc ./%s" (bx:buf-fname))))][pydoc]] || [[elisp:(python-check (format "/bisos/pipx/bin/pyflakes %s" (bx:buf-fname)))][pyflakes]] | [[elisp:(python-check (format "/bisos/pipx/bin/pychecker %s" (bx:buf-fname))))][pychecker (executes)]] | [[elisp:(python-check (format "/bisos/pipx/bin/pycodestyle %s" (bx:buf-fname))))][pycodestyle]] | [[elisp:(python-check (format "/bisos/pipx/bin/flake8 %s" (bx:buf-fname))))][flake8]] | [[elisp:(python-check (format "/bisos/pipx/bin/pylint %s" (bx:buf-fname))))][pylint]]  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

####+BEGIN: b:py3:cs:orgItem/basic :type "=PyImports= "  :title "*Py Library IMPORTS*" :comment "-- Framework and External Packages Imports"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  =PyImports=  [[elisp:(outline-show-subtree+toggle)][||]] *Py Library IMPORTS* -- Framework and External Packages Imports  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

# import os
import collections
# import pathlib
# import invoke

####+BEGIN: b:py3:cs:framework/imports :basedOn "classification"
""" #+begin_org
** Imports Based On Classification=cs-u
#+end_org """
from bisos import b
from bisos.b import cs
from bisos.b import b_io
from bisos.common import csParam

import collections
####+END:

import pathlib
import subprocess
import typing
import urllib.error
import urllib.request

from bisos.csSeed import seedsLib
from bisos.webCap import astroProc_seedInfo
from bisos.webCap import contentTree_csu

####+BEGIN: b:py3:cs:orgItem/basic :type "=Executes=  "  :title "CSU-Lib Executions" :comment "-- cs.invOutcomeReportControl"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  =Executes=   [[elisp:(outline-show-subtree+toggle)][||]] CSU-Lib Executions -- cs.invOutcomeReportControl  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

# cs.invOutcomeReportControl(cmnd=True, ro=True)

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

####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "Direct Command Services" :anchor ""  :extraInfo "Examples and CSs"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _Direct Command Services_: |]]  Examples and CSs  [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:

####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "Site Directories" :anchor ""  :extraInfo "siteBase and what is under it"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _Site Directories_: |]]  siteBase and what is under it  [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:


####+BEGIN: b:py3:cs:func/typing :funcName "siteBase" :funcType "extTyped" :deco "default"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /siteBase/  deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
def siteBase(
####+END:
) -> pathlib.Path:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] The site's top directory: as declared, else the planted astroProc.spcs's directory,
else the current directory (when run without a plant).
    #+end_org """
    declared = astroProc_seedInfo.astroProcSeedInfo.siteBase
    if declared:
        return pathlib.Path(declared).resolve()
    plant = seedsLib.seededCsxuInfo.plantOfThisSeed
    if plant:
        return pathlib.Path(plant).resolve().parent
    return pathlib.Path.cwd()


####+BEGIN: b:py3:cs:func/typing :funcName "siteDirs" :funcType "extTyped" :deco "default"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /siteDirs/  deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
def siteDirs(
####+END:
        base: pathlib.Path | None = None,
) -> dict[str, pathlib.Path]:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] The directories of the common structure, under base.
    #+end_org """
    base = base or siteBase()
    return {
        "base": base,
        "cbm": base / "cbm",
        "content": base / "content",
        "tree": base / "content" / "tree",
        "bin": base / "content" / "bin",
        "data": base / "content" / "data",
        "site": base / "site",
        "public": base / "site" / "public",
        "dist": base / "site" / "dist",
    }


####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "Build" :anchor ""  :extraInfo "content, then the Astro build"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _Build_: |]]  content, then the Astro build  [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:


####+BEGIN: b:py3:cs:func/typing :funcName "contentBuild_" :funcType "extTyped" :deco "default"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /contentBuild_/  deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
def contentBuild_(
####+END:
        base: pathlib.Path | None = None,
) -> list[str]:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] Build the content: the tree's pageLcnt bodies (HeVeA) and files nodes (into
site/public/), then every executable in content/bin/, in name order, from base. Returns the problems;
the first failing script stops it.
    #+end_org """
    d = siteDirs(base)
    problems = []
    if d["tree"].is_dir():
        for warning in contentTree_csu.validate(d["tree"]):
            print(f"content/tree: {warning}")
        built, lcntProblems = contentTree_csu.lcntBodies(d["tree"])
        for each in built:
            print(f"built: {each}/contentBody.html")
        problems += lcntProblems
        for each in contentTree_csu.filesPlace(d["tree"], d["public"]):
            print(f"placed: {each}")
    if d["bin"].is_dir():
        d["data"].mkdir(parents=True, exist_ok=True)
        for script in sorted(p for p in d["bin"].iterdir() if p.is_file() and p.stat().st_mode & 0o111):
            print(f"running: content/bin/{script.name}")
            if subprocess.run([str(script)], cwd=d["base"]).returncode != 0:
                problems.append(f"content/bin/{script.name} failed")
                break
    return problems


####+BEGIN: b:py3:cs:func/typing :funcName "siteBuild_" :funcType "extTyped" :deco "default"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /siteBuild_/  deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
def siteBuild_(
####+END:
        base: pathlib.Path | None = None,
) -> list[str]:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] contentBuild_, then npm ci (exactly site/package-lock.json) and astro build into site/dist/.
    #+end_org """
    problems = contentBuild_(base)
    if problems:
        return problems
    site = siteDirs(base)["site"]
    if not (site / "package-lock.json").is_file():
        return [f"{site}/package-lock.json is missing: run npm install there once (and keep the lock file under git)"]
    for cmd in (["npm", "ci", "--no-audit", "--no-fund"], ["npx", "astro", "build"]):
        print(f"running: {' '.join(cmd)}  (in {site})")
        if subprocess.run(cmd, cwd=site).returncode != 0:
            return [f"{' '.join(cmd)} failed in {site}"]
    return []


####+BEGIN: b:py3:cs:func/typing :funcName "siteVerify_" :funcType "extTyped" :deco "default"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /siteVerify_/  deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
def siteVerify_(
####+END:
        fqdn: str,
        paths: list[str],
) -> list[str]:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] GET each path of http://fqdn (expects 200) and a path that does not exist (expects
the site's 404). Returns the problems.
    #+end_org """
    problems = []
    checks = [(p, 200) for p in (paths or ["/"])] + [("/astroProc-verify-missing/", 404)]
    for path, expected in checks:
        url = f"http://{fqdn}{path}"
        try:
            with urllib.request.urlopen(url, timeout=5) as resp:
                status = resp.status
        except urllib.error.HTTPError as e:
            status = e.code
        except (urllib.error.URLError, OSError) as e:
            status = f"no answer ({e})"
        print(f"{status}  {url}")
        if status != expected:
            problems.append(f"{url}: {status}, expected {expected}")
    return problems


####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "Examples" :anchor ""  :extraInfo "examples_csu (no plant), examples_seed (a planted astroProc.spcs)"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _Examples_: |]]  examples_csu (no plant), examples_seed (a planted astroProc.spcs)  [[elisp:(org-shifttab)][<)]] E|
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
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Usage of astroProc without a planted file: plant an astroProc.spcs at a site's top.
        #+end_org """)

        literal = cs.examples.execInsert
        cs.examples.menuChapter('=astroProc -- plant astroProc.spcs at the top of a static site=')
        literal("cp <astro-starter-bystar>/astroProc.spcs <siteBase>/   # then set its fqdn and dev port")
        literal("<siteBase>/astroProc.spcs                              # its menu: content, build, verify")
        return(cmndOutcome)


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "examples_seed" :comment "" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv "pyKwArgs"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<examples_seed>>  =verify= ro=cli pyInv=pyKwArgs   [[elisp:(org-cycle)][| ]]
#+end_org """
class examples_seed(cs.Cmnd):
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
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  The site's process, as run from its planted astroProc.spcs.
        #+end_org """)

        cmnd = cs.examples.cmndEnter
        literal = cs.examples.execInsert
        info = astroProc_seedInfo.astroProcSeedInfo
        d = siteDirs()
        port = info.devPortNu or 4321

        cs.examples.menuChapter(f'*Site Process --- {d["base"]}*')

        cs.examples.menuSection('/The site/')
        cmnd('siteInfo', comment=" # directories, fqdn, dev port, Astro version, content tree summary")

        cs.examples.menuSection('/Content -- content/tree (contentTree_csu) and content/bin/*/')
        cmnd('contentTreeList', args="content/tree", comment=" # the tree: types, titles, languages, flags")
        cmnd('contentTreeValidate', args="content/tree", comment=" # unknown types, missing bodies or files")
        cmnd('contentBuild', comment=" # pageLcnt bodies (HeVeA), files nodes, then content/bin/*")

        cs.examples.menuSection('/Build -- npm ci and astro build into site/dist/')
        cmnd('siteBuild', comment=" # contentBuild, npm ci, astro build")

        cs.examples.menuSection('/Develop and Preview -- run in site/')
        literal(f"(cd site && npx astro dev --host 127.0.0.1 --port {port})       # http://localhost:{port}")
        literal(f"(cd site && npx astro preview --host 127.0.0.1 --port {port})   # serve site/dist/")

        cs.examples.menuSection('/Serve -- the capability (cbm/)/')
        for assemble in sorted(d["cbm"].glob("*-assemble.cs")):
            literal(f"./cbm/{assemble.name} -i fullUpdate   # siteBuild + dns entry + nginx vhost")
        if info.fqdn:
            cmnd('siteVerify', args="/", comment=f" # GET http://{info.fqdn}/ (200) and a missing page (404)")
            literal(f"bx-browse-url.sh http://{info.fqdn}")

        cs.examples.menuSection('/Plone 3 migration -- a ContentTree into content/tree/')
        cmnd('contentTreePloneImport', args="<plone3Site>/ContentTree content/tree", comment=" # content/tree must not exist")
        return(cmndOutcome)


####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "Site Cmnds" :anchor ""  :extraInfo "siteInfo, contentBuild, siteBuild, siteVerify"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _Site Cmnds_: |]]  siteInfo, contentBuild, siteBuild, siteVerify  [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "siteInfo" :comment "" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<siteInfo>>  =verify= ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class siteInfo(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Print the site's directories, fqdn, dev port, Astro version and a content tree summary.
        #+end_org """)

        info = astroProc_seedInfo.astroProcSeedInfo
        d = siteDirs()
        for name, path in d.items():
            print(f"{name:8} {path}{'' if path.exists() else '  (absent)'}")
        print(f"fqdn     {info.fqdn}")
        print(f"devPort  {info.devPortNu}")
        lock = d["site"] / "package-lock.json"
        if lock.is_file():
            import json
            astro = json.loads(lock.read_text()).get("packages", {}).get("node_modules/astro", {})
            print(f"astro    {astro.get('version', '?')}  (site/package-lock.json)")
        if d["tree"].is_dir():
            nodes = list(contentTree_csu.walkNodes(contentTree_csu.readTree(d["tree"])))
            print(f"tree     {len(nodes)} nodes, {sum(n.hasPage for _, n in nodes)} with a page")
        return cmndOutcome.set(opError=b.OpError.Success, opResults=None)


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "contentBuild" :comment "" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<contentBuild>>  =verify= ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class contentBuild(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Build the content: pageLcnt bodies (HeVeA), files nodes, then every content/bin/ executable.
        #+end_org """)

        problems = contentBuild_()
        for problem in problems:
            print(problem)
        return failed(cmndOutcome) if problems else cmndOutcome.set(opError=b.OpError.Success, opResults=None)


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "siteBuild" :comment "" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<siteBuild>>  =verify= ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class siteBuild(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
####+END:
        self.cmndDocStr(f""" #+begin_org
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  contentBuild, then npm ci and astro build into site/dist/.
        #+end_org """)

        problems = siteBuild_()
        for problem in problems:
            print(problem)
        return failed(cmndOutcome) if problems else cmndOutcome.set(opError=b.OpError.Success, opResults=None)


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "siteVerify" :comment "" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 9999 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<siteVerify>>  =verify= argsMin=0 argsMax=9999 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class siteVerify(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 9999,}

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
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  GET the given paths of http://<fqdn> (200 expected) and a missing one (404).
        #+end_org """)

        fqdn = astroProc_seedInfo.astroProcSeedInfo.fqdn
        if not fqdn:
            print("no fqdn declared (astroProc_seedInfo.setup(fqdn=...))")
            return failed(cmndOutcome)
        paths = self.cmndArgsGet("0&9999", cmndArgsSpecDict, argsList) or ["/"]
        problems = siteVerify_(fqdn, list(paths))
        return failed(cmndOutcome) if problems else cmndOutcome.set(opError=b.OpError.Success, opResults=None)

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
            argPosition="0&9999",
            argName="paths",
            argDefault='',
            argChoices=[],
            argDescription="site paths to GET, e.g. / /sitemap/"
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
