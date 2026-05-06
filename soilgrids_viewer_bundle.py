"""Compatibility shim exposing soilgrids_viewer_bundle at repository root."""

from tools.soilgrids import soilgrids_viewer_bundle as _impl
from tools.soilgrids.soilgrids_viewer_bundle import *  # noqa: F401,F403


def main(argv=None):
    return _impl.main(argv)


if __name__ == "__main__":
    raise SystemExit(main())
