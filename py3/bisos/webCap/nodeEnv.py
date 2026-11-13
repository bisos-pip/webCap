# -*- coding: utf-8 -*-

""" #+begin_org
* Overview: Node and npm for non-interactive shells.

Builds (astro, gatsby) and sboms run node, npm and npx in shells that never read ~/.bashrc, so the
user's nvm is not loaded and the system /bin/node is used. nvmLoadPrelude loads nvm the way
nvm-sbom.pcs installs it (NVM_DIR, else $XDG_CONFIG_HOME/nvm, else ~/.nvm) with its default Node;
without nvm it does nothing and the system node stays. The same prelude is in bisos.sbom's sbom_csu
(for npmPkgs_update).
#+end_org """

import typing

nvmLoadPrelude = """
if [ -z "${NVM_DIR}" ]; then
    if [ -n "${XDG_CONFIG_HOME}" ]; then NVM_DIR="${XDG_CONFIG_HOME}/nvm"
    else NVM_DIR="${HOME}/.nvm"; fi
fi
export NVM_DIR
if [ -s "$NVM_DIR/nvm.sh" ]; then . "$NVM_DIR/nvm.sh"; nvm use default >/dev/null 2>&1; fi
"""


def withNvm(
        cmd: list[str],
) -> list[str]:
    """argv that runs cmd in bash after nvmLoadPrelude (for subprocess.run)."""
    return ["bash", "-c", nvmLoadPrelude + 'exec "$@"', "bash", *cmd]


def withNvmBash(
        script: str,
) -> str:
    """A bash script string preceded by nvmLoadPrelude (for b.subProc ... .bash())."""
    return nvmLoadPrelude + script
