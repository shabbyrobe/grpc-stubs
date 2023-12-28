#!/bin/bash
set -o errexit -o nounset -o pipefail
script_abspath="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Don't forget to update the version in setup.py, commit, tag and
# push tags.
cmd-deploy() {
  # Clean out dist to avoid "file already exists" errors:
  rm ./dist/*
  source venv/bin/activate
  python3 setup.py sdist bdist_wheel
  python3 -m twine upload dist/*
}

cmd-dev-setup() {
  python3 -m venv venv
  source venv/bin/activate
  pip install -r requirements-dev.txt
}

cmd-test() {
  source venv/bin/activate

  dirs=(
    "grpc-stubs"
    "grpc_channelz-stubs"
    "grpc_health-stubs"
    "grpc_reflection-stubs"
    "grpc_status-stubs"
  )

  for dir in "${dirs[@]}"; do
    pushd "$script_abspath/$dir" > /dev/null
      echo "$dir"
      mypy -- .
    popd > /dev/null
  done

  # This test setup is based on the instructions here:
  # https://sobolevn.me/2019/08/testing-mypy-types
  pytest --mypy-ini-file=setup.cfg
}

"cmd-$1" "${@:2}"
