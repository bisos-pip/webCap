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
import os

####+BEGIN: b:py3:cs:framework/imports :basedOn "classification"
""" #+begin_org
*  Imports =Based on Classification=cs-u=
#+end_org """
from bisos import b  # noqa: E402
from bisos.b import cs
from bisos.b import b_io
from bisos.common import csParam
####+END:

from bisos.webCap import capWebVd_seedInfo

import logging
log = logging.getLogger(__name__)


def commonParamsSpecify(
        csParams: cs.param.CmndParamDict,
) -> None:
    pass


####+BEGIN: b:py3:cs:func/typing :funcName "examples_csu"
@cs.track(fnLoc=True, fnEntry=True, fnExit=True)
def examples_csu(
####+END:
        sectionTitle: typing.AnyStr = '',
) -> None:
    """Examples of capWebVd commands."""

    cmnd = cs.examples.cmndEnter

    if sectionTitle == 'default':
        cs.examples.menuChapter('*BISOS NGINX Virtual-Host Capability Commands*')

    cs.examples.menuSection('/WebVd Capability Commands/')
    cmnd('webVd_update',   comment="# Write NGINX config to sites-available/")
    cmnd('webVd_enable',   comment="# Symlink into sites-enabled/ + nginx reload")
    cmnd('webVd_disable',  comment="# Remove symlink from sites-enabled/ + nginx reload")
    cmnd('webVd_verify',   comment="# Verify config + symlink present + nginx -t")
    cmnd('webVd_resolve',  comment="# curl HTTP check against serverName")
    cmnd('webVd_fqdnPing', comment="# Ping serverName once")


####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "webVd_update"
class webVd_update(cs.Cmnd):
    cmndParamsMandatory = []
    cmndParamsOptional  = []
    cmndArgsLen = {'Min': 0, 'Max': 0,}

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:
####+END:
        """Write NGINX config to /etc/nginx/sites-available/<serverName>. Does NOT enable."""

        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)

        ci = capWebVd_seedInfo.cmndsControlInfo
        if ci.serverName is None:
            b_io.ann.note("ERROR: serverName is not set in cmndsControlInfo")
            return failed(cmndOutcome)
        if ci.wvdConfigFunc is None:
            b_io.ann.note("ERROR: wvdConfigFunc is not set in cmndsControlInfo")
            return failed(cmndOutcome)

        configStr = ci.wvdConfigFunc()
        sitesAvailable = pathlib.Path(f'/etc/nginx/sites-available/{ci.serverName}')

        import tempfile
        with tempfile.NamedTemporaryFile(mode='w', suffix='.nginx.conf', delete=False) as tmp:
            tmp.write(configStr)
            tmpPath = tmp.name

        result = subprocess.run(
            ['sudo', 'cp', tmpPath, str(sitesAvailable)],
            capture_output=True, text=True,
        )
        os.unlink(tmpPath)

        if result.returncode != 0:
            b_io.ann.note(f"ERROR: failed to write {sitesAvailable}: {result.stderr}")
            return failed(cmndOutcome)

        b_io.ann.note(f"webVd_update: wrote config to {sitesAvailable}")
        return cmndOutcome.set(opError=b.OpError.Success)


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
            b_io.ann.note(f"ERROR: {sitesAvailable} does not exist — run webVd_update first")
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

        reloadResult = subprocess.run(
            ['sudo', 'nginx', '-s', 'reload'],
            capture_output=True, text=True,
        )
        if reloadResult.returncode != 0:
            b_io.ann.note(f"ERROR: nginx reload failed: {reloadResult.stderr}")
            return failed(cmndOutcome)

        b_io.ann.note(f"webVd_enable: nginx reloaded for {ci.serverName}")
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
        """Check sites-available/ exists, symlink in sites-enabled/ present, nginx -t passes."""

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