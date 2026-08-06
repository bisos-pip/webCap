# -*- coding: utf-8 -*-

""" #+begin_org
* ~[Summary]~ :: CS-Unit for NGINX virtual-host capability (capWebVd).
#+end_org """

####+BEGIN: b:py3:cs:file/dblockControls :classification "cs-u"
""" #+begin_org
* [[elisp:(org-cycle)][| /Control Parameters Of This File/ |]] :: dblk ctrls classifications=cs-u
#+end_org """
####+END:

import collections
import typing
import subprocess
import pathlib
import __main__

####+BEGIN: b:py3:cs:framework/imports :basedOn "classification"
""" #+begin_org
*  Imports =Based on Classification=cs-u=
#+end_org """
from bisos import b  # noqa: E402
from bisos.b import cs
from bisos.b import b_io
from bisos.common import csParam
####+END:

from bisos.debian import configFile
from bisos.basics import pyRunAs

from bisos.webCap import capWebVd_seedInfo

import logging
log = logging.getLogger(__name__)


def commonParamsSpecify(
        csParams: cs.param.CmndParamDict,
) -> None:
    pass


####+BEGIN: b:py3:class/decl :className "ConfigFile_nginxVd" :superClass "configFile.ConfigFile" :comment "" :classType "basic"
""" #+begin_org
*  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]]  Cls-basic  [[elisp:(outline-show-subtree+toggle)][||]] /ConfigFile_nginxVd/  superClass=configFile.ConfigFile  [[elisp:(org-cycle)][| ]]
#+end_org """
class ConfigFile_nginxVd(configFile.ConfigFile):
####+END:
    """ #+begin_org
** [[elisp:(org-cycle)][| DocStr| ]]  ConfigFile subclass for NGINX virtual-host in sites-available/.
    #+end_org """

####+BEGIN: b:py3:cs:method/typing :methodName "configFilePath" :deco "default"
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]]  Mtd-T-  [[elisp:(outline-show-subtree+toggle)][||]] /configFilePath/  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def configFilePath(
####+END:
            self,
    ) -> pathlib.Path:
        """ #+begin_org
*** [[elisp:(org-cycle)][| DocStr| ]]  Return path to /etc/nginx/sites-available/<serverName>.
        #+end_org """
        ci = capWebVd_seedInfo.cmndsControlInfo
        return pathlib.Path(f'/etc/nginx/sites-available/{ci.serverName}')

####+BEGIN: b:py3:cs:method/typing :methodName "configFileStr" :methodType "" :deco "default"
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]]  Mtd-T-  [[elisp:(outline-show-subtree+toggle)][||]] /configFileStr/  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def configFileStr(
####+END:
            self,
    ) -> str | None:
        """ #+begin_org
*** [[elisp:(org-cycle)][| DocStr| ]]  Return NGINX config as string via wvdConfigFunc from seedInfo.
        #+end_org """
        ci = capWebVd_seedInfo.cmndsControlInfo
        if ci.wvdConfigFunc is None:
            print(f"EH_problem Missing capWebVd_seedInfo.cmndsControlInfo.wvdConfigFunc")
            return None
        return ci.wvdConfigFunc()

####+BEGIN: b:py3:cs:method/typing :methodName "configFileUpdate" :methodType "eType" :retType "" :deco "default" :argsList ""
    """ #+begin_org
**  _[[elisp:(blee:menu-sel:outline:popupMenu)][±]]_ _[[elisp:(blee:menu-sel:navigation:popupMenu)][Ξ]]_ [[elisp:(outline-show-branches+toggle)][|=]]  Mtd-T-eType  [[elisp:(outline-show-subtree+toggle)][||]] /configFileUpdate/  deco=default  [[elisp:(org-cycle)][| ]]
    #+end_org """
    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def configFileUpdate(
####+END:
            self,
    ):
        """ #+begin_org
*** [[elisp:(org-cycle)][| DocStr| ]]  Write config string to sites-available/ as root.
        #+end_org """
        contentStr = self.configFileStr()
        destPath = self.configFilePath()
        pyRunAs.as_root_writeToFile(destPath, contentStr)


configFile_nginxVd = ConfigFile_nginxVd()


####+BEGIN: b:py3:cs:func/typing :funcName "examples_csu"
@cs.track(fnLoc=True, fnEntry=True, fnExit=True)
def examples_csu(
####+END:
        sectionTitle: typing.AnyStr = '',
) -> None:
    """Examples of capWebVd commands."""

    od = collections.OrderedDict
    cmnd = cs.examples.cmndEnter

    if sectionTitle == 'default':
        cs.examples.menuChapter('*BISOS NGINX Virtual-Host Capability Commands*')

    concreteConfigFilePars     = od([('cls', 'configFile_nginxVd'),])
    concreteConfigFileRootPars = od([('cls', 'configFile_nginxVd'), ('runAs', 'root'),])

    ci = capWebVd_seedInfo.cmndsControlInfo
    filePath = configFile_nginxVd.configFilePath()

    cs.examples.menuSection(f'*Config Content {filePath}*')
    cmnd('configFileStdout', pars=concreteConfigFilePars,     comment="# That which will be stored in configFile")
    cmnd('configFilePath',   pars=concreteConfigFilePars,     comment=f"# ls -l {filePath}")
    cmnd('configFilePath',   pars=concreteConfigFileRootPars, comment=f"# sudo ls -l {filePath}")
    cmnd('configFileUpdate', pars=concreteConfigFilePars,     comment=f"# write stdout to {filePath}")
    cmnd('configFileUpdate', pars=concreteConfigFileRootPars, comment=f"# sudo write stdout to {filePath}")
    cmnd('configFileCat',    pars=concreteConfigFilePars,     comment=f"# cat {filePath}")
    cmnd('configFileCat',    pars=concreteConfigFileRootPars, comment=f"# sudo cat {filePath}")
    cmnd('configFileVerify', pars=concreteConfigFilePars,     comment=f"# are stdout and {filePath} the same")
    cmnd('configFileDelete', pars=concreteConfigFilePars,     comment=f"# delete {filePath}")
    cmnd('configFileDelete', pars=concreteConfigFileRootPars, comment=f"# sudo delete {filePath}")

    cs.examples.menuSection('/WebVd Enable/Disable/Verify Commands/')
    cmnd('webVd_enable',   comment="# Symlink into sites-enabled/ + nginx reload")
    cmnd('webVd_disable',  comment="# Remove symlink from sites-enabled/ + nginx reload")
    cmnd('webVd_verify',   comment="# Verify symlink present + nginx -t")
    cmnd('webVd_resolve',  comment="# curl HTTP check against serverName")
    cmnd('webVd_fqdnPing', comment="# Ping serverName once")


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "webVd_enable"
class webVd_enable(cs.Cmnd):
    cmndParamsMandatory = []
    cmndParamsOptional  = []
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:
####+END:
        """Create symlink in sites-enabled/ and reload nginx. Idempotent."""

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)

        ci = capWebVd_seedInfo.cmndsControlInfo
        if ci.serverName is None:
            b_io.ann.note("ERROR: serverName is not set in cmndsControlInfo")
            return failed(cmndOutcome)

        sitesAvailable = pathlib.Path(f'/etc/nginx/sites-available/{ci.serverName}')
        sitesEnabled   = pathlib.Path(f'/etc/nginx/sites-enabled/{ci.serverName}')

        if not sitesAvailable.exists():
            b_io.ann.note(f"ERROR: {sitesAvailable} does not exist — run configFileUpdate first")
            return failed(cmndOutcome)

        if sitesEnabled.is_symlink():
            b_io.ann.note(f"webVd_enable: symlink already present at {sitesEnabled} (idempotent)")
        else:
            result = subprocess.run(
                ['sudo', 'ln', '-s', str(sitesAvailable), str(sitesEnabled)],
                capture_output=True, text=True,
            )
            if result.returncode != 0:
                b_io.ann.note(f"ERROR: failed to create symlink: {result.stderr}")
                return failed(cmndOutcome)
            b_io.ann.note(f"webVd_enable: created symlink {sitesEnabled} -> {sitesAvailable}")

        testResult = subprocess.run(
            ['sudo', 'nginx', '-t'],
            capture_output=True, text=True,
        )
        if testResult.returncode != 0:
            b_io.ann.note(f"ERROR: nginx -t failed:\n{testResult.stderr}")
            return failed(cmndOutcome)

        # Always reload via the systemd-managed unit so a just-written config
        # is guaranteed to be picked up (nginx -s reload can leave stale workers
        # if the reload raced the config write).
        reloadResult = subprocess.run(
            ['sudo', 'systemctl', 'reload', 'nginx'],
            capture_output=True, text=True,
        )
        if reloadResult.returncode != 0:
            b_io.ann.note(f"ERROR: nginx reload failed: {reloadResult.stderr}")
            return failed(cmndOutcome)

        b_io.ann.note(f"webVd_enable: nginx reloaded (systemctl) for {ci.serverName}")
        return cmndOutcome.set(opError=b.OpError.Success)


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "webVd_disable"
class webVd_disable(cs.Cmnd):
    cmndParamsMandatory = []
    cmndParamsOptional  = []
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:
####+END:
        """Remove symlink from sites-enabled/ and reload nginx. sites-available/ is untouched."""

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)

        ci = capWebVd_seedInfo.cmndsControlInfo
        if ci.serverName is None:
            b_io.ann.note("ERROR: serverName is not set in cmndsControlInfo")
            return failed(cmndOutcome)

        sitesEnabled = pathlib.Path(f'/etc/nginx/sites-enabled/{ci.serverName}')

        if not sitesEnabled.is_symlink():
            b_io.ann.note(f"webVd_disable: symlink not present at {sitesEnabled} (already disabled)")
        else:
            result = subprocess.run(
                ['sudo', 'rm', str(sitesEnabled)],
                capture_output=True, text=True,
            )
            if result.returncode != 0:
                b_io.ann.note(f"ERROR: failed to remove symlink: {result.stderr}")
                return failed(cmndOutcome)
            b_io.ann.note(f"webVd_disable: removed symlink {sitesEnabled}")

        reloadResult = subprocess.run(
            ['sudo', 'nginx', '-s', 'reload'],
            capture_output=True, text=True,
        )
        if reloadResult.returncode != 0:
            b_io.ann.note(f"ERROR: nginx reload failed: {reloadResult.stderr}")
            return failed(cmndOutcome)

        b_io.ann.note(f"webVd_disable: nginx reloaded, {ci.serverName} disabled")
        return cmndOutcome.set(opError=b.OpError.Success)


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "webVd_verify"
class webVd_verify(cs.Cmnd):
    cmndParamsMandatory = []
    cmndParamsOptional  = []
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:
####+END:
        """Check symlink in sites-enabled/ is present and nginx -t passes."""

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)

        ci = capWebVd_seedInfo.cmndsControlInfo
        if ci.serverName is None:
            b_io.ann.note("ERROR: serverName is not set in cmndsControlInfo")
            return failed(cmndOutcome)

        sitesAvailable = pathlib.Path(f'/etc/nginx/sites-available/{ci.serverName}')
        sitesEnabled   = pathlib.Path(f'/etc/nginx/sites-enabled/{ci.serverName}')

        issues = []
        if not sitesAvailable.exists():
            issues.append(f"MISSING: {sitesAvailable}")
        if not sitesEnabled.is_symlink():
            issues.append(f"MISSING symlink: {sitesEnabled}")

        if issues:
            for issue in issues:
                b_io.ann.note(f"webVd_verify: {issue}")
            return failed(cmndOutcome)

        testResult = subprocess.run(
            ['sudo', 'nginx', '-t'],
            capture_output=True, text=True,
        )
        if testResult.returncode != 0:
            b_io.ann.note(f"webVd_verify: nginx -t FAILED:\n{testResult.stderr}")
            return failed(cmndOutcome)

        b_io.ann.note(f"webVd_verify: OK — {ci.serverName} present in sites-available + sites-enabled, nginx -t passes")
        return cmndOutcome.set(opError=b.OpError.Success)


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "webVd_resolve"
class webVd_resolve(cs.Cmnd):
    cmndParamsMandatory = []
    cmndParamsOptional  = []
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:
####+END:
        """HTTP check: curl -s -o /dev/null -w '%{http_code}' http://<serverName>."""

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)

        ci = capWebVd_seedInfo.cmndsControlInfo
        if ci.serverName is None:
            b_io.ann.note("ERROR: serverName is not set in cmndsControlInfo")
            return failed(cmndOutcome)

        result = subprocess.run(
            ['curl', '-s', '-o', '/dev/null', '-w', '%{http_code}',
             f'http://{ci.serverName}'],
            capture_output=True, text=True,
        )
        httpCode = result.stdout.strip()
        b_io.ann.note(f"webVd_resolve: http://{ci.serverName} -> HTTP {httpCode}")
        return cmndOutcome.set(opError=b.OpError.Success, opResults=httpCode)


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "webVd_fqdnPing"
class webVd_fqdnPing(cs.Cmnd):
    cmndParamsMandatory = []
    cmndParamsOptional  = []
    cmndArgsLen = {'Min': 0, 'Max': 1,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
             argsList: typing.Optional[list[str]] = None,
    ) -> b.op.Outcome:
####+END:
        """Ping serverName (or arg) once."""

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, argsList).isProblematic():
            return failed(cmndOutcome)
        cmndArgsSpecDict = self.cmndArgsSpec()

        ci = capWebVd_seedInfo.cmndsControlInfo
        cmndArgs = self.cmndArgsGet("0&1", cmndArgsSpecDict, argsList)
        fqdn = cmndArgs[0] if cmndArgs else ci.serverName

        result = subprocess.run(
            ['ping', '-c', '1', fqdn],
            capture_output=True, text=True,
        )
        b_io.ann.note(result.stdout.strip() if result.returncode == 0 else f"ping failed: {fqdn}")
        return cmndOutcome.set(
            opError=b.OpError.Success if result.returncode == 0 else b.OpError.Failed,
            opResults=result.stdout.strip(),
        )

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmndArgsSpec(self):
        cmndArgsSpecDict = cs.CmndArgsSpecDict()
        cmndArgsSpecDict.argsDictAdd(
            argPosition="0&1",
            argName="cmndArgs",
            argDefault='',
            argChoices=[],
            argDescription="fqdn to ping (overrides cntrlInfo.serverName)"
        )
        return cmndArgsSpecDict
