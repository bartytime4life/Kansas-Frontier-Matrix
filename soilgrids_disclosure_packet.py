"""Compatibility shim exposing soilgrids_disclosure_packet at repository root."""

from tools.soilgrids import soilgrids_disclosure_packet as _impl
from tools.soilgrids.soilgrids_disclosure_packet import *  # noqa: F401,F403


def main(argv=None):
    return _impl.main(argv)


if __name__ == "__main__":
    raise SystemExit(main())
