#!/bin/env python
# -*- coding: utf-8 -*-

import typing ; csInfo: typing.Dict[str, typing.Any] = {'category': 'csxu', 'name': 'capWebVd_seed.cs', 'features': ['direct', 'uploader', 'seeded']}

csInfo['summary'] = """ #+begin_org
* ~[Summary]~ :: A =CmndSvc= seed for BISOS NGINX virtual-host capability (capWebVd).
#+end_org """

csInfo['description'] = """ #+begin_org
* [[elisp:(org-cycle)][| ~csInfoDescription~ |]] :: The capWebVd seed. Plants (e.g. =airflow-wvd.pcs=) extend it
to manage NGINX virtual host entries.
#+end_org """

####+BEGIN: b:py3:cs:file/dblockControls :classification "cs-mu"
""" #+begin_org
* [[elisp:(org-cycle)][| /Control Parameters Of This File/ |]] :: dblk ctrls classifications=cs-mu
#+end_org """
####+END:

####+BEGIN: b:py3:cs:framework/imports :basedOn "classification"
from bisos import b
from bisos.b import cs
from bisos.b import b_io
from bisos.common import csParam

import collections
####+END:

from bisos.b import enhancedExceptions

import pathlib
import typing
import sys
import os

####+BEGIN: b:py3:cs:framework/csxuSeeded
from bisos.csSeed import seedsLib
if seedsLib.seededCsxuInfo.plantOfThisSeed is not None:
    b.importFileAs('plantedCsu', seedsLib.seededCsxuInfo.plantOfThisSeed, __file__, __name__)
####+END:

####+BEGIN: b:py3:cs:framework/csuListImportPlus
from bisos.csPlayer import csxuFps_csu
from bisos.webCap import capWebVd_csu
from bisos.debian import configFile
from bisos.b import clsMethod_csu
from bisos.csSeed import csCmndsList_csu

csuList = [ 'bisos.csPlayer.csxuFps_csu', 'bisos.webCap.capWebVd_csu', 'bisos.debian.configFile', 'bisos.b.clsMethod_csu', 'bisos.csSeed.csCmndsList_csu', 'plantedCsu', ]

if seedsLib.seededCsxuInfo.plantOfThisSeed is None:
    csuList.remove('plantedCsu')

g_importedCmndsModules = cs.csuList_importedModules(csuList)

def g_extraParams():
    csParams = cs.param.CmndParamDict()
    cs.csuList_commonParamsSpecify(csuList, csParams)
    cs.argsparseBasedOnCsParams(csParams)

####+END:

# Expose configFile_nginxVd to __main__ so configFile commands can resolve --cls=configFile_nginxVd
configFile_nginxVd = capWebVd_csu.configFile_nginxVd

####+BEGIN: b:py3:cs:cmnd/classHead :cmndName "examples" :extent "verify" :ro "noCli"
class examples(cs.Cmnd):
    cmndParamsMandatory = []
    cmndParamsOptional  = []
    cmndArgsLen = {'Min': 0, 'Max': 0,}
    rtInvConstraints = cs.rtInvoker.RtInvoker.new_noRo()

    @cs.track(fnLoc=True, fnEntry=True, fnExit=True)
    def cmnd(self,
             rtInv: cs.RtInvoker,
             cmndOutcome: b.op.Outcome,
    ) -> b.op.Outcome:
        """FrameWrk: CS-Main-Examples"""
        failed = b_io.eh.badOutcome
        callParamsDict = {}
        if self.invocationValidate(rtInv, cmndOutcome, callParamsDict, None).isProblematic():
            return failed(cmndOutcome)
####+END:
        cs.examples.myName(cs.G.icmMyName(), cs.G.icmMyFullName())
        cs.examples.commonBrief()
        csxuFps_csu.playerMenuExamples().pyCmnd()

        if seedsLib.seededCsxuInfo.seedOfThisPlant is None:
            csCmndsList_csu.examples_csu().pyCmnd()
        else:
            csCmndsList_csu.examples_seed().pyCmnd()
            seedsLib.plantedCsuExamplesRun()

        return cmndOutcome


if __name__ == '__main__':
    cs.main.g_csMain(
        csInfo=csInfo,
        noCmndEntry=examples,
        extraParamsHook=g_extraParams,
        ignoreUnknownParams=True,
        importedCmndsModules=g_importedCmndsModules,
    )
