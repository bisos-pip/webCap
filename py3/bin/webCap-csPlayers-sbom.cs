#!/usr/bin/env python

from bisos.sbom import pkgsSeed  # pkgsSeed.plantWithWhich("seedSbom.cs")
ap = pkgsSeed.aptPkg
pp = pkgsSeed.pipPkg

aptPkgsList = [
    # ap("facter"),
]

pipPkgsList = [
    pp("Django"),
    pp("djangorestframework"),
    pp("python-dotenv"),
]

pipxPkgsList = [
    # pp("bisos.marmee"),
]

pkgsSeed.setup(
    aptPkgsList=aptPkgsList,
    pipPkgsList=pipPkgsList,
    pipxPkgsList=[],

)
