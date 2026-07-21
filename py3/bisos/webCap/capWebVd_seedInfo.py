# -*- coding: utf-8 -*-

""" #+begin_org
* ~[Summary]~ :: SeedInfo for capWebVd NGINX virtual-host capability.
#+end_org """

from bisos.b import cs
import typing
import enum
from dataclasses import dataclass


@enum.unique
class WebVdSpecMethod(enum.Enum):
    nginxProxy = "nginxProxy"
    apache     = "apache"      # placeholder


@dataclass
class CmndsControlInfo(object):
    """Control parameters for NGINX virtual-host capability commands."""

    webVdSpecMethod: WebVdSpecMethod | None = None
    serverName: str | None = None
    proxyPort: int | None = None
    wvdConfigFunc: typing.Callable | None = None

    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


# Singleton instantiation
cmndsControlInfo = CmndsControlInfo()


@cs.track(fnLoc=True, fnEntry=True, fnExit=True)
def setup(
        serverName: str | None = None,
        proxyPort: int | None = None,
        wvdConfigFunc: typing.Callable | None = None,
        webVdSpecMethod: WebVdSpecMethod = WebVdSpecMethod.nginxProxy,
) -> None:
    """Populate cmndsControlInfo from a .pcs file."""
    ci = cmndsControlInfo
    if serverName is not None:
        ci.serverName = serverName
    if proxyPort is not None:
        ci.proxyPort = proxyPort
    if wvdConfigFunc is not None:
        ci.wvdConfigFunc = wvdConfigFunc
    ci.webVdSpecMethod = webVdSpecMethod