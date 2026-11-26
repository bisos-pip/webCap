# -*- coding: utf-8 -*-
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars |]]* :: The astro sites served on this system, found through nginx
** This File: /bisos/git/bxRepos/bisos-pip/webCap/py3/bisos/webCap/astroSite_csu.py
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
csInfo['version'] = '202611143853'
csInfo['status']  = 'inUse'
csInfo['panel'] = 'astroSite_csu-Panel.org'
csInfo['groupingType'] = 'IcmGroupingType-pkged'
csInfo['cmndParts'] = 'IcmCmndParts[common] IcmCmndParts[param]'
####+END:

""" #+begin_org
* [[elisp:(org-cycle)][| ~Description~ |]] :: Where an astro site lives, given its FQDN.
A BISOS astro site is served by nginx from =<siteBase>/site/dist= (see astroProc_csu). The enabled
vhost whose =server_name= lists the FQDN therefore names the site's base directory in its =root=.
This module deduces the base from that, and nothing else: it is the one way tools such as the
lcnt export find a site from its name. The =root= is used as configured and never resolved, since
=site/dist= may be a link into a release directory.
** Status: In use with BISOS
** /[[elisp:(org-cycle)][| Planned Improvements |]]/ :
*** TODO A vhost with the root inside a =location= block is not understood.
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

import pathlib
import re

nginxEnabledDir = pathlib.Path("/etc/nginx/sites-enabled")

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

####+BEGIN: blee:bxPanel:foldingSection :outLevel 0 :sep nil :title "Library" :anchor ""  :extraInfo "Finding a site from its FQDN"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*     [[elisp:(outline-show-subtree+toggle)][| _Library_: |]]  Finding a site from its FQDN  [[elisp:(org-shifttab)][<)]] E|
#+end_org """
####+END:

_commentRe = re.compile(r'(?m)#.*$')
_serverRe = re.compile(r'(?m)^\s*server\s*\{')
_nameRe = re.compile(r'(?m)^\s*server_name\s+([^;]*);')
_rootRe = re.compile(r'(?m)^\s*root\s+([^;\s]+)\s*;')


def siteBaseOf(
        fqdn: str,
        vhostDir: pathlib.Path = nginxEnabledDir,
) -> typing.Tuple[typing.Optional[pathlib.Path], str]:
    """ Returns (base, "") for the astro site served as fqdn, or (None, reason).

    The base is the =root= of the enabled vhost naming fqdn with "/site/dist" removed; the
    base must hold content/tree. Several server blocks in one file are told apart.
    """
    if not vhostDir.is_dir():
        return None, f"{fqdn}: no vhost directory {vhostDir}"
    for vhost in sorted(vhostDir.iterdir()):
        if not vhost.is_file():
            continue
        try:
            text = _commentRe.sub('', vhost.read_text())
        except OSError as err:
            return None, f"{fqdn}: cannot read {vhost}: {err}"
        for block in _serverRe.split(text):
            names = [name for found in _nameRe.finditer(block) for name in found.group(1).split()]
            if fqdn not in names:
                continue
            found = _rootRe.search(block)
            if not found:
                return None, f"{fqdn}: {vhost} has no root (a proxy vhost?)"
            root = found.group(1)
            if not root.endswith('/site/dist'):
                return None, f"{fqdn}: root {root} does not end in /site/dist"
            base = pathlib.Path(root[:-len('/site/dist')])
            if not (base / 'content' / 'tree').is_dir():
                return None, f"{fqdn}: {base}/content/tree is missing"
            return base, ""
    return None, f"{fqdn}: no enabled vhost in {vhostDir}"


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
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Examples of finding an astro site's base directory from its FQDN.
        #+end_org """)

        cmnd = cs.examples.cmndEnter
        cs.examples.menuChapter('=siteBase= -- the base directory of an astro site, from nginx')
        cmnd('siteBase', args="astroStarter.internal", comment=" # prints: <fqdn> <base>")
        cmnd('siteBase', args="astroStarter.internal platform.internal", comment=" # several; exit 1 if any fails")
        return(cmndOutcome)


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "siteBase" :comment "" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 1 :argsMax 9999 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<siteBase>>  =verify= argsMin=1 argsMax=9999 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class siteBase(cs.Cmnd):
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
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Print "<fqdn> <base>" for each FQDN, the base directory of the astro site nginx serves as that name; a reason and a failed outcome for each that is not one.
        #+end_org """)

        fqdns = self.cmndArgsGet("0&-1", cmndArgsSpecDict, argsList)
        if not fqdns:
            b_io.eh.problem_usageError("No FQDN: give one or more as arguments")
            return failed(cmndOutcome)

        allFound = True
        for fqdn in fqdns:
            base, reason = siteBaseOf(fqdn)
            if base is None:
                b_io.eh.problem_usageError(reason)
                allFound = False
                continue
            print(f"{fqdn} {base}")
        if not allFound:
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
            argName="fqdns",
            argDefault='',
            argChoices=[],
            argDescription="One or more FQDNs of astro sites, e.g. astroStarter.internal"
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
