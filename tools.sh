#!/bin/bash
set -o errexit -o nounset -o pipefail
#script_abspath="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cmd-deploy() {
    python3 setup.py sdist bdist_wheel
    python3 -m twine upload dist/*
}

"cmd-$1" "${@:2}"
