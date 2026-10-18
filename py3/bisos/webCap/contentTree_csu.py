# -*- coding: utf-8 -*-

""" #+begin_org
* ~[Summary]~ :: A =CS-Unit= for content trees: a static site's pages as a file-system tree (the ByStar Plone 3 ContentTree model).
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
** This File: /bisos/git/bxRepos/bisos-pip/webCap/py3/bisos/webCap/contentTree_csu.py
** Authors: Mohsen BANAN, http://mohsen.banan.1.byname.net/contact
#+end_org """
####+END:

####+BEGIN: b:py3:file/particulars-csInfo :status "inUse"
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars-csInfo |]]*
#+end_org """
import typing
csInfo: typing.Dict[str, typing.Any] = { 'moduleName': ['contentTree_csu'], }
csInfo['version'] = '202403270908'
csInfo['status']  = 'inUse'
csInfo['panel'] = 'contentTree_csu-Panel.org'
csInfo['groupingType'] = 'IcmGroupingType-pkged'
csInfo['cmndParts'] = 'IcmCmndParts[common] IcmCmndParts[param]'
####+END:

""" #+begin_org
* [[elisp:(org-cycle)][| ~Description~ |]] :: [[file:/bisos/git/auth/bxRepos/blee-binders/bisos-core/COMEEGA/_nodeBase_/fullUsagePanel-en.org][BISOS COMEEGA Panel]]
A content tree (=<siteBase>/content/tree/=) holds a static site's pages as a file-system tree, in the
model of the ByStar Plone 3 ContentTree. It is engine-neutral: astroProc_csu renders one with Astro,
and another engine would read the same tree. This module holds what is not engine-specific: the
parameter rules, validation, the bodies of =pageLcnt= nodes (LaTeX through HeVeA), the placing of
=files= nodes, and importing a Plone 3 ContentTree.

A node is a directory; its parameters are one file each, named as in the Plone 3 ContentTree:
| =objectType=      | folder, page, pageLcnt, files, custom, app (auxNode, auxLeaf, rawFiles: the old slider) |
| (app)             | the tree gives the tab, title and place; the site's fixed page renders it (an island) |
| (link)            | a tab that leads out to =linkUrl= (e.g. another .here site)                  |
| =folderTitle=     | a folder's label in the navigation                                 |
| =pageTitle=       | a page's heading and title; =pageDescription= its summary          |
| =pubState=        | publish: built; anything else: left out                            |
| =excludeFromNav=  | true: built, but not in the navigation                             |
| =contentBody.html= | a page's body (HeVeA output); else =content.html=, =contentPreface.html= |
| =filesList=, =siteFolder= | a files node's files and their place in the site           |
and, new with the Plone migration:
| =nodesOrdered=    | a folder's children in navigation order, one per line (the rest by name) |
| =contentLang=     | en, fa, fr, ...; inherited; fa/ar/he/ur pages are right-to-left    |
| =defaultPage=, =siteTitle= | at the tree's root                                        |
A folder's own page is its =index_html/= leaf.
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
import re
import shutil
import subprocess
import tempfile
import typing
from dataclasses import dataclass, field

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

####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "Content Tree Model" :anchor ""  :extraInfo "Parameters, nodes, walk"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _Content Tree Model_: |]]  Parameters, nodes, walk  [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:


RTL_LANGS = {"fa", "ar", "he", "ur"}
OBJECT_TYPES = {"folder", "page", "pageLcnt", "files", "custom", "app", "link"}
SLIDER_TYPES = {"auxNode", "auxLeaf", "rawFiles"}   # the Plone 3 sites' slider; Reveal replaces it
PAGE_TYPES = {"page", "pageLcnt"}
# A page's body: the first of these that exists (the Plone 3 trees used all three).
BODY_FILES = ("contentBody.html", "content.html", "contentPreface.html")

# The bxtex HeVeA macros (bxlcnt) that LCNT documents expect.
BXTEX_HEVEA_MACROS = pathlib.Path("/bisos/git/bxRepos/bxlcnt/bxtex/hevea/macros")

####+BEGIN: b:py3:cs:func/typing :funcName "param" :funcType "extTyped" :deco "default"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /param/  deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
def param(
####+END:
        nodeDir: pathlib.Path,
        name: str,
) -> str | None:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] One parameter of a node: its file's content, stripped; None when absent.
    #+end_org """
    path = pathlib.Path(nodeDir) / name
    return path.read_text(encoding="utf-8").strip() if path.is_file() else None


@dataclass
class ContentNode:
    """A node of a content tree, as a site sees it."""
    dir: pathlib.Path
    urlPath: str                      # "/" or "/projects/wapTrap/"
    objectType: str
    title: str
    lang: str
    published: bool
    inNav: bool
    hasPage: bool
    children: list["ContentNode"] = field(default_factory=list)

    @property
    def textDir(self) -> str:
        return "rtl" if self.lang in RTL_LANGS else "ltr"


####+BEGIN: b:py3:cs:func/typing :funcName "bodyFile" :funcType "extTyped" :deco "default"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /bodyFile/  deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
def bodyFile(
####+END:
        pageDir: pathlib.Path,
) -> pathlib.Path | None:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] A page's body file: the first of BODY_FILES that exists; None when there is none.
    #+end_org """
    return next((pathlib.Path(pageDir) / n for n in BODY_FILES if (pathlib.Path(pageDir) / n).is_file()), None)


####+BEGIN: b:py3:cs:func/typing :funcName "childNames" :funcType "extTyped" :deco "default"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /childNames/  deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
def childNames(
####+END:
        nodeDir: pathlib.Path,
) -> list[str]:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] A node's child nodes, in navigation order: nodesOrdered first, then the rest by name.
    #+end_org """
    nodeDir = pathlib.Path(nodeDir)
    names = sorted(d.name for d in nodeDir.iterdir()
                   if d.is_dir() and d.name != "index_html" and (d / "objectType").is_file())
    ordered = [n for n in (param(nodeDir, "nodesOrdered") or "").split() if n in names]
    return ordered + [n for n in names if n not in ordered]


####+BEGIN: b:py3:cs:func/typing :funcName "readTree" :funcType "extTyped" :deco "default"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /readTree/  deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
def readTree(
####+END:
        treeDir: pathlib.Path,
        urlPath: str = "/",
        parentLang: str = "en",
) -> ContentNode:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] Read a content tree (or a subtree) into ContentNodes, unpublished nodes included and marked.
The same rules as an engine's reader (astro-starter-bystar site/src/lib/contentTree.mjs).
    #+end_org """
    treeDir = pathlib.Path(treeDir)
    objectType = param(treeDir, "objectType") or "folder"
    lang = param(treeDir, "contentLang") or parentLang
    pageDir = treeDir / "index_html" if objectType == "folder" else treeDir
    hasPage = (objectType in ("folder", "app") + tuple(PAGE_TYPES)) and (pageDir / "objectType").is_file() \
        and param(pageDir, "pubState") == "publish"
    title = param(treeDir, "folderTitle") or (param(pageDir, "pageTitle") if hasPage else None)         or (param(treeDir, "siteTitle") if urlPath == "/" else None) or treeDir.name
    node = ContentNode(
        dir=treeDir, urlPath=urlPath, objectType=objectType, title=title, lang=lang,
        published=(urlPath == "/" or param(treeDir, "pubState") == "publish"),
        inNav=param(treeDir, "excludeFromNav") != "true", hasPage=hasPage,
    )
    for name in childNames(treeDir):
        node.children.append(readTree(treeDir / name, f"{urlPath}{name}/", lang))
    return node


####+BEGIN: b:py3:cs:func/typing :funcName "walkNodes" :funcType "extTyped" :deco "default"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /walkNodes/  deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
def walkNodes(
####+END:
        node: ContentNode,
        depth: int = 0,
) -> typing.Iterator[tuple[int, ContentNode]]:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] Every node, depth first, with its depth.
    #+end_org """
    yield depth, node
    for child in node.children:
        yield from walkNodes(child, depth + 1)


####+BEGIN: b:py3:cs:func/typing :funcName "validate" :funcType "extTyped" :deco "default"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /validate/  deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
def validate(
####+END:
        treeDir: pathlib.Path,
) -> list[str]:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] The problems of a content tree, one line each; empty when there are none.
    #+end_org """
    problems = []
    treeDir = pathlib.Path(treeDir)
    if not treeDir.is_dir():
        return [f"{treeDir}: not a directory"]
    for objectTypeFile in sorted(treeDir.rglob("objectType")):
        nodeDir = objectTypeFile.parent
        rel = nodeDir.relative_to(treeDir)
        objectType = objectTypeFile.read_text().strip()
        if objectType in SLIDER_TYPES:
            continue
        if objectType not in OBJECT_TYPES:
            problems.append(f"{rel}: unknown objectType {objectType}")
            continue
        if param(nodeDir, "pubState") is None and objectType not in ("files", "custom"):
            problems.append(f"{rel}: no pubState (the node is left out)")
        if objectType == "page" and bodyFile(nodeDir) is None:
            problems.append(f"{rel}: page without a body ({', '.join(BODY_FILES)})")
        if objectType == "pageLcnt" and not (nodeDir / "webPageLcnt" / "bodyWebPage.tex").is_file() \
                and bodyFile(nodeDir) is None:
            problems.append(f"{rel}: pageLcnt without webPageLcnt/bodyWebPage.tex or contentBody.html")
        if objectType == "link" and not param(nodeDir, "linkUrl"):
            problems.append(f"{rel}: link without linkUrl")
        if objectType == "files":
            for name in (param(nodeDir, "filesList") or "").split():
                if not (nodeDir / name).is_file():
                    problems.append(f"{rel}: filesList names a missing file, {name}")
            if not param(nodeDir, "siteFolder"):
                problems.append(f"{rel}: files node without siteFolder")
        for name in (param(nodeDir, "nodesOrdered") or "").split():
            if not (nodeDir / name / "objectType").is_file():
                problems.append(f"{rel}: nodesOrdered names a missing node, {name}")
    return problems


####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "LCNT Bodies and Files" :anchor ""  :extraInfo "pageLcnt through HeVeA; files nodes into the site"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _LCNT Bodies and Files_: |]]  pageLcnt through HeVeA; files nodes into the site  [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:


# Persian runs marked for the browser's bidi; given to hevea before the document so the document's own
# XeTeX-only definitions of fa / faPar are not used; and no HeVeA footer, since the page sits in a site's
# layout. Candidate for bxtex/hevea/macros.
BX_RTL_HVA = r"""\newenvironment{fa}{\@open{span}{lang="fa" dir="rtl"}}{\@close{span}}
\newenvironment{faPar}{\@open{div}{lang="fa" dir="rtl"}}{\@close{div}}
\newcommand{\beginR}{}
\newcommand{\endR}{}
\newcommand{\persian}{}
\footerfalse
"""

# Only the body: a Plone 3 site's webpage.ttytex also carries the old slider's raw HTML.
LCNT_WRAPPER = r"""\documentclass{article}
\usepackage{hevea}
\usepackage[utf8]{inputenc}
\usepackage{hyperref}
\begin{document}
\input{bodyWebPage.tex}
\end{document}
"""

####+BEGIN: b:py3:cs:func/typing :funcName "lcntBody" :funcType "extTyped" :deco "default"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /lcntBody/  deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
def lcntBody(
####+END:
        nodeDir: pathlib.Path,
        macrosDir: pathlib.Path = BXTEX_HEVEA_MACROS,
) -> str:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] Build a pageLcnt node's contentBody.html from webPageLcnt/bodyWebPage.tex with HeVeA.
Returns "" on success, else the problem.
    #+end_org """
    nodeDir = pathlib.Path(nodeDir)
    src = nodeDir / "webPageLcnt" / "bodyWebPage.tex"
    if not src.is_file():
        return f"{nodeDir}: no webPageLcnt/bodyWebPage.tex"
    if shutil.which("hevea") is None:
        if (nodeDir / "contentBody.html").is_file():
            print(f"{nodeDir}: hevea is not installed; the existing contentBody.html is kept")
            return ""
        return "hevea is not installed (apt: hevea)"
    with tempfile.TemporaryDirectory() as tmp:
        tmpDir = pathlib.Path(tmp)
        shutil.copy(src, tmpDir / "bodyWebPage.tex")
        (tmpDir / "page.tex").write_text(LCNT_WRAPPER)
        (tmpDir / "bx-rtl.hva").write_text(BX_RTL_HVA)
        cmd = ["hevea", "-fix", "-I", str(macrosDir), "bx-rtl.hva", "page.tex", "-o", "page.html"]
        run = subprocess.run(cmd, cwd=tmpDir, capture_output=True, text=True)
        if run.returncode != 0 or not (tmpDir / "page.html").is_file():
            return f"{nodeDir}: hevea failed: {run.stderr.strip()[-300:]}"
        shutil.copy(tmpDir / "page.html", nodeDir / "contentBody.html")
    return ""


####+BEGIN: b:py3:cs:func/typing :funcName "lcntBodies" :funcType "extTyped" :deco "default"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /lcntBodies/  deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
def lcntBodies(
####+END:
        treeDir: pathlib.Path,
        macrosDir: pathlib.Path = BXTEX_HEVEA_MACROS,
) -> tuple[list[str], list[str]]:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] Build every pageLcnt node's body. Returns (built nodes, problems).
    #+end_org """
    built, problems = [], []
    for objectTypeFile in sorted(pathlib.Path(treeDir).rglob("objectType")):
        if objectTypeFile.read_text().strip() != "pageLcnt":
            continue
        problem = lcntBody(objectTypeFile.parent, macrosDir)
        (problems if problem else built).append(problem or str(objectTypeFile.parent))
    return built, problems


####+BEGIN: b:py3:cs:func/typing :funcName "filesPlace" :funcType "extTyped" :deco "default"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /filesPlace/  deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
def filesPlace(
####+END:
        treeDir: pathlib.Path,
        publicDir: pathlib.Path,
) -> list[str]:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] Copy every files node's filesList into publicDir/<siteFolder>/. Returns the files placed.
    #+end_org """
    placed = []
    for objectTypeFile in sorted(pathlib.Path(treeDir).rglob("objectType")):
        nodeDir = objectTypeFile.parent
        if objectTypeFile.read_text().strip() != "files":
            continue
        dest = pathlib.Path(publicDir) / (param(nodeDir, "siteFolder") or "").strip("/")
        dest.mkdir(parents=True, exist_ok=True)
        for name in (param(nodeDir, "filesList") or "").split():
            shutil.copy(nodeDir / name, dest / name)
            placed.append(str(dest / name))
    return placed


####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "Plone 3 Import" :anchor ""  :extraInfo "A ByStar Plone 3 ContentTree into a content tree"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _Plone 3 Import_: |]]  A ByStar Plone 3 ContentTree into a content tree  [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:


# Per-node processors of the Plone 3 trees; the content tree needs none (_tree_ stays).
PLONE_DROPPED = ("plone3Proc.sh", "plone3Proc.sh.gened", "ploneProc.sh", "lcntProc.sh", "_treeProc_")

####+BEGIN: b:py3:cs:func/typing :funcName "ploneImport" :funcType "extTyped" :deco "default"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /ploneImport/  deco=default  [[elisp:(org-cycle)][| ]]
#+end_org """
def ploneImport(
####+END:
        srcTree: pathlib.Path,
        destTree: pathlib.Path,
) -> list[str]:
    """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] Copy a Plone 3 ContentTree into destTree (which must not exist): the parameter files and
bodies as they are, without the per-node processors; each folder's nodesOrdered= from its plone3Proc.sh
becomes a nodesOrdered file. Returns notes, one line each.
    #+end_org """
    srcTree, destTree = pathlib.Path(srcTree), pathlib.Path(destTree)
    if destTree.exists():
        return [f"{destTree} exists; not imported"]
    shutil.copytree(srcTree, destTree, symlinks=True, ignore=shutil.ignore_patterns(*PLONE_DROPPED))
    notes = [f"copied {srcTree} -> {destTree}"]
    for proc in sorted(srcTree.rglob("plone3Proc.sh")):
        m = re.search(r'^nodesOrdered="([^"]*)"', proc.read_text(errors="replace"), re.M)
        order = m.group(1).split() if m else []
        if order:
            target = destTree / proc.parent.relative_to(srcTree) / "nodesOrdered"
            target.write_text("\n".join(order) + "\n")
            notes.append(f"{target}: {' '.join(order)}")
    sliders = sorted({p.parent.relative_to(destTree).parts[0] for p in destTree.rglob("objectType")
                     if p.read_text().strip() in SLIDER_TYPES})
    if sliders:
        notes.append(f"slider nodes kept but not rendered (Reveal replaces them): {' '.join(sliders)}")
    notes.append("order the top level with a nodesOrdered file at the root (the tabs)")
    return notes


####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "Content Tree Cmnds" :anchor ""  :extraInfo "list, validate, lcntBodies, filesPlace, ploneImport"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _Content Tree Cmnds_: |]]  list, validate, lcntBodies, filesPlace, ploneImport  [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "contentTreeList" :comment "" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 1 :argsMax 1 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<contentTreeList>>  =verify= argsMin=1 argsMax=1 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class contentTreeList(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 1, 'Max': 1,}

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
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Print a content tree: each node's path, type, title, language, and whether it is published and in the navigation.
        #+end_org """)

        treeDir = pathlib.Path(self.cmndArgsGet("0", cmndArgsSpecDict, argsList))
        root = readTree(treeDir)
        for depth, node in walkNodes(root):
            flags = ("" if node.published else " UNPUBLISHED") + ("" if node.inNav else " notInNav") \
                + ("" if node.hasPage else " noPage")
            print(f"{'  ' * depth}{node.urlPath}  [{node.objectType}] {node.title}  ({node.lang}){flags}")
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
            argPosition="0",
            argName="treeDir",
            argDefault='',
            argChoices=[],
            argDescription="the content tree, e.g. content/tree"
        )

        return cmndArgsSpecDict


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "contentTreeValidate" :comment "" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 1 :argsMax 1 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<contentTreeValidate>>  =verify= argsMin=1 argsMax=1 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class contentTreeValidate(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 1, 'Max': 1,}

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
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Report the problems of a content tree: unknown types, pages without bodies, missing files, wrong nodesOrdered.
        #+end_org """)

        problems = validate(pathlib.Path(self.cmndArgsGet("0", cmndArgsSpecDict, argsList)))
        for problem in problems:
            print(problem)
        if not problems:
            print("no problems")
            return cmndOutcome.set(opError=b.OpError.Success, opResults=None)
        return failed(cmndOutcome)

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
            argPosition="0",
            argName="treeDir",
            argDefault='',
            argChoices=[],
            argDescription="the content tree, e.g. content/tree"
        )

        return cmndArgsSpecDict


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "contentTreeLcntBodies" :comment "" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 1 :argsMax 1 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<contentTreeLcntBodies>>  =verify= argsMin=1 argsMax=1 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class contentTreeLcntBodies(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 1, 'Max': 1,}

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
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Build every pageLcnt node's contentBody.html with HeVeA (bxtex macros; Persian runs marked rtl).
        #+end_org """)

        built, problems = lcntBodies(pathlib.Path(self.cmndArgsGet("0", cmndArgsSpecDict, argsList)))
        for each in built:
            print(f"built: {each}/contentBody.html")
        for problem in problems:
            print(problem)
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
            argPosition="0",
            argName="treeDir",
            argDefault='',
            argChoices=[],
            argDescription="the content tree, e.g. content/tree"
        )

        return cmndArgsSpecDict


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "contentTreeFilesPlace" :comment "" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 2 :argsMax 2 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<contentTreeFilesPlace>>  =verify= argsMin=2 argsMax=2 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class contentTreeFilesPlace(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 2, 'Max': 2,}

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
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Copy every files node's files into the site's public directory, at its siteFolder.
        #+end_org """)

        treeDir = pathlib.Path(self.cmndArgsGet("0", cmndArgsSpecDict, argsList))
        publicDir = pathlib.Path(self.cmndArgsGet("1", cmndArgsSpecDict, argsList))
        for each in filesPlace(treeDir, publicDir):
            print(f"placed: {each}")
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
            argPosition="0",
            argName="treeDir",
            argDefault='',
            argChoices=[],
            argDescription="the content tree, e.g. content/tree"
        )
        cmndArgsSpecDict.argsDictAdd(
            argPosition="1",
            argName="publicDir",
            argDefault='',
            argChoices=[],
            argDescription="the site's public directory, e.g. site/public"
        )

        return cmndArgsSpecDict


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "contentTreePloneImport" :comment "" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 2 :argsMax 2 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<contentTreePloneImport>>  =verify= argsMin=2 argsMax=2 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class contentTreePloneImport(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 2, 'Max': 2,}

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
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Import a ByStar Plone 3 ContentTree as a content tree (destTree must not exist).
        #+end_org """)

        srcTree = pathlib.Path(self.cmndArgsGet("0", cmndArgsSpecDict, argsList))
        destTree = pathlib.Path(self.cmndArgsGet("1", cmndArgsSpecDict, argsList))
        for note in ploneImport(srcTree, destTree):
            print(note)
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
            argPosition="0",
            argName="srcTree",
            argDefault='',
            argChoices=[],
            argDescription="a Plone 3 ContentTree directory"
        )
        cmndArgsSpecDict.argsDictAdd(
            argPosition="1",
            argName="destTree",
            argDefault='',
            argChoices=[],
            argDescription="the new content tree, e.g. content/tree"
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
