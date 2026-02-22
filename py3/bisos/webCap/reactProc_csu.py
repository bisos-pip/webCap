# -*- coding: utf-8 -*-

""" #+begin_org
* ~[Summary]~ :: A =CS-Unit= as equivalent of facter in py and remotely with rpyc.
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
** This File: /bisos/git/bxRepos/bisos-pip/facter/py3/bisos/facter/facter_csu.py
** Authors: Mohsen BANAN, http://mohsen.banan.1.byname.net/contact
#+end_org """
####+END:

####+BEGIN: b:py3:file/particulars-csInfo :status "inUse"
""" #+begin_org
* *[[elisp:(org-cycle)][| Particulars-csInfo |]]*
#+end_org """
import typing
csInfo: typing.Dict[str, typing.Any] = { 'moduleName': ['facter_csu'], }
csInfo['version'] = '202403270908'
csInfo['status']  = 'inUse'
csInfo['panel'] = 'facter_csu-Panel.org'
csInfo['groupingType'] = 'IcmGroupingType-pkged'
csInfo['cmndParts'] = 'IcmCmndParts[common] IcmCmndParts[param]'
####+END:

""" #+begin_org
* [[elisp:(org-cycle)][| ~Description~ |]] :: [[file:/bisos/git/auth/bxRepos/blee-binders/bisos-core/COMEEGA/_nodeBase_/fullUsagePanel-en.org][BISOS COMEEGA Panel]]
This a =Cs-Unit= for running the equivalent of facter in py and remotely with rpyc.
With BISOS, it is used in CMDB remotely.

** Relevant Panels:
** Status: In use with BISOS
** /[[elisp:(org-cycle)][| Planned Improvements |]]/ :
*** TODO complete fileName in particulars.
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
import enum

from bisos.webCap import reactProc_seedInfo

import logging
log = logging.getLogger(__name__)

####+BEGIN: b:py3:cs:orgItem/basic :type "=Executes=  "  :title "CSU-Lib Executions" :comment "-- cs.invOutcomeReportControl"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  =Executes=   [[elisp:(outline-show-subtree+toggle)][||]] CSU-Lib Executions -- cs.invOutcomeReportControl  [[elisp:(org-cycle)][| ]]
#+end_org """
####+END:

# g_svcName = "svcFacter"
# g_rosmu = cs.G.icmMyName()

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

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "examples_csu" :comment "" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv "pyKwArgs"
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
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  Basic example command.
        #+end_org """)

        self.captureRunStr(""" #+begin_org
*** Run Results
#+begin_src sh :results output :session shared
facterModule.cs -i examples 
  #+end_src
#+RESULTS:
#+begin_example
#+end_example

        #+end_org """)

        od = collections.OrderedDict
        cmnd = cs.examples.cmndEnter
        literal = cs.examples.execInsert

        #  -v 1 --callTrackings monitor+ --callTrackings invoke+
        pars_debug_verbosity = od([('verbosity', "1"),])
        pars_debug_monitor = od([('callTrackings', "monitor+"),])
        pars_debug_invoke = od([('callTrackings', "invoke+"),])
        pars_debug_full = (pars_debug_verbosity | pars_debug_monitor | pars_debug_invoke)

        pars_cluster_default = od([('cluster', "default"),])

        cs.examples.menuChapter('=Determine Which React Framework is Being Used=')
        cmnd('whichReactFramework', comment=f"""# DEBUG Small Batch""",)

        cs.examples.menuChapter('=MONITOR Nginx and related services=')
        literal("nginx-sysd.pcs")
        literal("nginx-sysd.pcs -i sysdSysUnit  status")
        literal("journalctl -u nginx 200  # Traffic in and out of nginx")

        cs.examples.menuChapter('=RESTART Nginx and related services=')
        literal("nginx-sysd.pcs -i sysdSysUnit  restart")

        cs.examples.menuChapter('=React/Gatsby NPM Development=')

        reactFramework = whichReactFramework_()
        if reactFramework == ReactFramework.React:
            literal("npm run watch")
        elif reactFramework == ReactFramework.Gatsby:
            literal("gatsby develop")
        elif  reactFramework== ReactFramework.NoneFound:
            log.info("No React framework detected; skipping Nginx restart.")

        cs.examples.menuChapter('=React/Gatsby NPM Production Build=')

        reactFramework = whichReactFramework_()
        if reactFramework == ReactFramework.React:
            literal("npm run build")
            literal("npm run build && nginx-sysd.pcs -i sysdSysUnit  restart") 
            literal("npm run clean && npm install && npm run build && nginx-sysd.pcs -i sysdSysUnit  restart")
        elif reactFramework == ReactFramework.Gatsby:
            literal("gatsby build")
            literal("gatsby build && nginx-sysd.pcs -i sysdSysUnit  restart")
            literal("gatsby clean && npm install && gatsby build && nginx-sysd.pcs -i sysdSysUnit  restart")
        elif  reactFramework== ReactFramework.NoneFound:
            log.info("No React framework detected; skipping Nginx restart.")

        cs.examples.menuChapter('=React/Gatsby NPM Clean=')

        reactFramework = whichReactFramework_()
        if reactFramework == ReactFramework.React:
            literal("npm run clean")
            literal("npm run clean && nginx-sysd.pcs -i sysdSysUnit  restart")
        elif reactFramework == ReactFramework.Gatsby:
            literal("gatsby clean")
            literal("gatsby clean && nginx-sysd.pcs -i sysdSysUnit  restart")
        elif  reactFramework== ReactFramework.NoneFound:
            log.info("No React framework detected; skipping Nginx restart.")

        return(cmndOutcome)



####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "examples_seed" :comment "" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv "pyKwArgs"
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
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]  pyKwArgs 'upload' is mandatory
        #+end_org """)

        self.captureRunStr(""" #+begin_org
*** Run Results
#+begin_src sh :results output :session shared
facterModule.cs -i examples
  #+end_src
#+RESULTS:
#+begin_example
#+end_example

        #+end_org """)

        examples_csu().pyCmnd()

        cs.examples.menuChapter('=Planted CS Info=')

        assert reactProc_seedInfo.reactProcSeedInfo.reactFramework == whichReactFramework_()

        cwd = pathlib.Path.cwd()

        print(f"{cwd}")
        print(f"http://{reactProc_seedInfo.reactProcSeedInfo.webVirtualDomain}")
        print(f"http://localhost:{reactProc_seedInfo.reactProcSeedInfo.dev_webPortNu}")

        return(cmndOutcome)

####+BEGIN: bx:dblock:python:enum :enumName "ReactFramework" :comment ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  Enum       [[elisp:(outline-show-subtree+toggle)][||]] /ReactFramework/  [[elisp:(org-cycle)][| ]]
#+end_org """
@enum.unique
class ReactFramework(enum.Enum):
####+END:
        React = "react"
        Gatsby = "gatsby"
        NoneFound = "noneFound"

####+BEGIN: b:py3:cs:func/typing :funcName "whichReactFramework_" :funcType "extTyped" :deco "track"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  F-T-extTyped [[elisp:(outline-show-subtree+toggle)][||]] /reactFramework/  deco=track  [[elisp:(org-cycle)][| ]]
#+end_org """
@cs.track(fnLoc=True, fnEntry=True, fnExit=True)
def whichReactFramework_(
####+END:
) -> ReactFramework:
        """ #+begin_org
** [[elisp:(org-cycle)][| *DocStr | ] Look in the current directory for files that indicate which React framework is being used.
        #+end_org """
        # Check for Gatsby-specific configuration files
        current_dir = pathlib.Path('.')
        
        # Gatsby indicators
        gatsby_config_files = [
            'gatsby-config.js',
            'gatsby-config.ts',
            'gatsby-config.mjs',
        ]
        
        for gatsby_file in gatsby_config_files:
            if (current_dir / gatsby_file).exists():
                return ReactFramework.Gatsby
        
        # Check for .gatsby-files marker directory
        if (current_dir / '.gatsby-files').exists():
            return ReactFramework.Gatsby
        
        # Check for pure React config files (CRA or similar)
        react_config_files = [
            'package.json',  # All React projects have this
            'react-scripts',  # CRA dependency (in node_modules, but check package.json)
        ]
        
        # Check if package.json exists and contains react/react-scripts
        package_json_path = current_dir / 'package.json'
        if package_json_path.exists():
            try:
                import json
                with open(package_json_path, 'r') as f:
                    package_data = json.load(f)
                    # Check if react or react-scripts is in dependencies
                    deps = package_data.get('dependencies', {})
                    devDeps = package_data.get('devDependencies', {})
                    if 'react' in deps or 'react' in devDeps or 'react-scripts' in devDeps:
                        return ReactFramework.React
            except (json.JSONDecodeError, IOError):
                pass
        
        # If neither Gatsby nor React found, return NoneFound
        return ReactFramework.NoneFound



####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "whichReactFramework" :comment "" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 0 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<whichReactFramework>>  =verify= argsMax=0 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class whichReactFramework(cs.Cmnd):
    cmndParamsMandatory = [ ]
    cmndParamsOptional = [ ]
    cmndArgsLen = {'Min': 0, 'Max': 0,}

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
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]
Detect which React framework is being used in the current directory.
        #+end_org """)

        result: ReactFramework = whichReactFramework_()
        
        #print(f"{result.value}")

        return cmndOutcome.set(
                opError=b.OpError.Success,
                opResults=result,
        )


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "placeHolder" :comment "" :extent "verify" :ro "cli" :parsMand "" :parsOpt "" :argsMin 0 :argsMax 9999 :pyInv ""
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]] [[elisp:(bx:orgm:indirectBufOther)][|>]] *[[elisp:(blee:ppmm:org-mode-toggle)][|N]]*  CmndSvc-   [[elisp:(outline-show-subtree+toggle)][||]] <<placeHolder>>  =verify= argsMax=9999 ro=cli   [[elisp:(org-cycle)][| ]]
#+end_org """
class placeHolder(cs.Cmnd):
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
** [[elisp:(org-cycle)][| *CmndDesc:* | ]]
        #+end_org """)

        self.captureRunStr(""" #+begin_org
*** Run Results
#+begin_src sh :results output :session shared
echo 127.0.0.1 | facterModule.cs --upload=../../bin/facterModuleSample.py  -i clusterRun localhost otherHost
  #+end_src
#+RESULTS:
: ['localhost', 'otherHost', '127.0.0.1']
: ** cmnd= env CHECKPOINT_DISABLE=1 echo  localhost
: localhost
: ** cmnd= env CHECKPOINT_DISABLE=1 echo  otherHost
: otherHost
: ** cmnd= env CHECKPOINT_DISABLE=1 echo  127.0.0.1
: 127.0.0.1
: ReRun this as subprocs

        #+end_org """)

        cmndArgs = self.cmndArgsGet("0&9999", cmndArgsSpecDict, argsList)
        effectiveClustersList = []

        def processArgsAndStdin(cmndArgs, process):
            for each in cmndArgs:
                process(each)
            stdinArgs = b_io.stdin.readAsList()
            for each in stdinArgs:
                process(each)

        def process(item):
            effectiveClustersList.append(item)
            if rtInv.outs:
                # print(f"target: {target}")
                pass

        processArgsAndStdin(cmndArgs, process)

        print(f"{effectiveClustersList}")

        return cmndOutcome.set(
            opError=b.OpError.Success,
            opResults=None,
        )


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
            argName="cmndArgs",
            argDefault='',
            argChoices=[],
            argDescription="Targets"
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
