#!/usr/bin/env python

# Template File:  /bisos/apps/defaults/begin/templates/purposed/pyModule/python/setup.py
# Blee Panel: /bisos/git/auth/bxRepos/blee-binders/bisos-core/bisos-pip/bisos.pycs/pipPackaging/_nodeBase_/fullUsagePanel-en.org

# b:py3:pypi:setup/pkgName Arguments  :pkgName "somePkg" :pkgNameSpace "bisos"
####+BEGIN: b:py3:pypi:setup/pkgName :comment "Auto Detected"

import setuptools
import re
import inspect
import pathlib

def pkgName():
    ''' From this eg., filepath=.../bisos-pip/PkgName/py3/setup.py, extract PkgName. '''
    filename = inspect.getframeinfo(inspect.currentframe()).filename
    grandMother = pathlib.Path(filename).resolve().parent.parent.name
    return f'bisos.{grandMother}'

def description():
    ''' Extract title from ./_description.org which is expected to have a #+title: line. '''
    try:
        with open('./_description.org') as file:
            while line := file.readline():
                if match := re.search(r'^#\+title: (.*)',  line.rstrip()):
                    return match.group(1)
            return 'MISSING TITLE in ./_description.org'
    except IOError:
        return  'ERROR: Could not read ./_description.org file.'

def longDescription():
    ''' Read README.rst as a string. '''
    fileName = './README.rst'
    try:
        with open(fileName) as file:
           result = file.read()
        return result
    except IOError:
        return  f'ERROR: Could not read {fileName} file.'

####+END:

# b:py3:pypi:setup/version Arguments  :forSys t :forPyPi t :constant "666"
####+BEGIN: b:py3:pypi:setup/version :comment "Auto Detected"

# ./pypiUploadVer DID NOT exist -- forPypiVersion=0.11 -- forLocalVersion=0.1 -- constant=NA
def pkgVersion():
        return '0.1'

####+END:

# b:py3:pypi:setup/requires :extras ; :requirements "requirements.txt" (bring here requirements.txt)
####+BEGIN: b:py3:pypi:setup/requires :extras ()

requires = [
"bisos",
"bisos.b",
"bisos.basics",
"bisos.capability",
"bisos.common",
"bisos.csPlayer",
"bisos.debian",
"bisos.sbom",
"bisos.tocsModules",
"bisos.uploadAsCs",
"setuptools==75.8.0",
"wheel==0.38.4",
]
####+END:

# b:py3:pypi:setup/scripts :comment
####+BEGIN: b:py3:pypi:setup/scripts :comment ""

scripts = [
'bin/cbs-is-np-sysd_gunicorn-csPlayerPerf.pcs',
'bin/csLineInvoker-react-nginx.pcs',
'bin/csPlayerPerf-gunicorn-nginx.pcs',
'bin/csPlayerUi-gatsby-nginx.pcs',
'bin/djangoAdmin.cs',
'bin/djangoProc-seed.cs',
'bin/djangoProc.spcs',
'bin/django-sbom.pcs',
'bin/facterModule.cs',
'bin/gunicornAdmin.cs',
'bin/gunicorn-csPlayerPerf-sysd.pcs',
'bin/gunicorn-sbom.pcs',
'bin/gunicorn-socket-sysd.pcs',
'bin/nginx-sbom.pcs',
'bin/nginx-seed.cs',
'bin/nginx-sysd.pcs',
'bin/planted-facterModule.cs',
'bin/postgresql-sbom.pcs',
'bin/starterSidebar-gatsby-nginx.pcs',
'bin/webCap-csPlayers-assemble.cs',
]
####+END:

# b:py3:pypi:setup/dataFiles :comment
####+BEGIN: b:py3:pypi:setup/dataFiles :comment "Instead of ./MANIFEST.in or in pyproject.toml"

data_files = [
('',  ['lh-agpl3-LICENSE.txt', '_description.org', 'README.rst']),
]
####+END:

# :pkgName "--auto--"  --- results in use of name=pkgName(),
####+BEGIN: b:py3:pypi:setup/funcArgs :comment "defaults to --auto--"

setuptools.setup(
    name=pkgName(),  # 'bisos.webCap'
    version=pkgVersion(),
    packages=setuptools.find_packages(),
    scripts=scripts,
    data_files=data_files,
    include_package_data=True,
    zip_safe=False,
    author='Mohsen Banan',
    author_email='libre@mohsen.1.banan.byname.net',
    maintainer='Mohsen Banan',
    maintainer_email='libre@mohsen.1.banan.byname.net',
    license='AGPL',
    description=description(),
    long_description=longDescription(),
    install_requires=requires,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ]
    )

####+END:
