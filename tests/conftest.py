"""Repository-wide pytest configuration for tests/.

Bounded-input tests parametrize multi-megabyte strings and byte strings. By
default pytest embeds such a value in the test ID, which produced collected IDs
of up to 4 MB. Printing them stalled the hosted runner's log processing, so the
`collect full Python suite` job never finished. Long values now get a short,
stable ID built from their type, length and SHA-256 prefix.
"""
from __future__ import annotations

import hashlib

MAX_PARAMETER_ID_CHARACTERS = 64


def short_parameter_id(value: object) -> str | None:
    """Return a bounded ID for a long str/bytes parameter, else None (pytest default)."""
    if isinstance(value, str):
        raw = value.encode("utf-8", "surrogatepass")
    elif isinstance(value, (bytes, bytearray)):
        raw = bytes(value)
    else:
        return None
    if len(value) <= MAX_PARAMETER_ID_CHARACTERS:
        return None
    return f"{type(value).__name__}{len(value)}-{hashlib.sha256(raw).hexdigest()[:12]}"


def pytest_make_parametrize_id(config, val, argname):  # noqa: ARG001 - pytest hook signature
    return short_parameter_id(val)
