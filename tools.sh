#!/bin/bash
set -o errexit -o nounset -o pipefail
script_abspath="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

cmd-deploy() {
    python3 setup.py sdist bdist_wheel
    python3 -m twine upload dist/*
}

cmd-test() {
    pushd "$script_abspath/grpc-stubs" > /dev/null
        mypy -- *.pyi
    popd > /dev/null

    # This test setup is based on the instructions here:
    # https://sobolevn.me/2019/08/testing-mypy-types
    pytest --mypy-ini-file=setup.cfg
}

"cmd-$1" "${@:2}"
