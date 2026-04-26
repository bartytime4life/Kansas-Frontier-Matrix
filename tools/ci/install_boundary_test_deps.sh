#!/bin/sh
set -eu

if python3 -m pip install --disable-pip-version-check --quiet \
  fastapi \
  jsonschema \
  httpx
then
  echo "install_boundary_test_deps: installed fastapi/jsonschema/httpx"
else
  echo "install_boundary_test_deps: warning: unable to install optional deps; boundary tests may skip" >&2
fi
