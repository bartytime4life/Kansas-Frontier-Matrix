"""Compatibility shim exposing soilgrids_release_publish at repository root."""

from tools.soilgrids import soilgrids_release_publish as _impl
from tools.soilgrids.soilgrids_release_publish import *  # noqa: F401,F403


def main(argv=None):
    return _impl.main(argv)


if __name__ == "__main__":
    raise SystemExit(main())
