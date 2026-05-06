"""Compatibility shim exposing soilgrids_registry_runtime at repository root."""

from tools.soilgrids import soilgrids_registry_runtime as _impl
from tools.soilgrids.soilgrids_registry_runtime import *  # noqa: F401,F403


def main(argv=None):
    return _impl.main(argv)


if __name__ == "__main__":
    raise SystemExit(main())
