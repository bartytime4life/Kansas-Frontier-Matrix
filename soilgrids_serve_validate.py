"""Compatibility shim exposing soilgrids_serve_validate at repository root."""

from tools.soilgrids import soilgrids_serve_validate as _impl
from tools.soilgrids.soilgrids_serve_validate import *  # noqa: F401,F403


def main(argv=None):
    return _impl.main(argv)


if __name__ == "__main__":
    raise SystemExit(main())
