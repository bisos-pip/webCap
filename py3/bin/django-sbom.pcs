#!/usr/bin/env python

from bisos.sbom import pkgsSeed  # pkgsSeed.plantWithWhich("seedSbom.cs")
ap = pkgsSeed.aptPkg
pp = pkgsSeed.pipPkg

aptPkgsList = [
    # ap("aptPkgName"),
]

pipPkgsList = [
    pp("django"),
    pp("djangorestframework"),
    pp("python-dotenv"),
]

pipxPkgsList = [
    # pp("pipPkgName"),
]

pkgsSeed.setup(
    aptPkgsList=aptPkgsList,
    pipPkgsList=pipPkgsList,
    pipxPkgsList=pipxPkgsList,

)
