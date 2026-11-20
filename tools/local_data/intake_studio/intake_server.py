#!/usr/bin/python3
"""Account-protected public entrypoint for the local KFM Studio.

The legacy implementation lives in intake_backend.py. Its
storage/extraction primitives are implementation details, not a second supported
HTTP entrypoint. Both the normal launcher and this historical CLI require login.
"""
from pathlib import Path
import sys

if __package__ in (None, ''):
    sys.path.insert(0, str(Path(__file__).resolve().parents[3]))

from tools.local_data.intake_studio import intake_backend as _backend
from tools.local_data.intake_studio.intake_backend import *  # noqa: F403
from tools.local_data.intake_studio.studio_access import AccessMixin, secure_server_class

Server = secure_server_class(_backend.Server, _backend.Handler)


class Handler(AccessMixin, _backend.Handler):
    """The supported handler has the same mandatory account gate as Server."""


def main():
    original = _backend.Server
    _backend.Server = Server
    try:
        _backend.main()
    finally:
        _backend.Server = original


if __name__ == '__main__':
    main()
