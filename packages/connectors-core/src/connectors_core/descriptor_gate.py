"""Fail-closed reading of a connector-local ``descriptor.yaml`` for candidate routing.

Connector packages carry a flat descriptor (``name``, ``role``, ``rights``,
``sensitivity_floor``). Role and rights are steward decisions; while either is
unresolved, a connector must hold every candidate route. This module only reads the
file strictly and reports blockers. It resolves nothing, activates nothing, and is not
a SourceDescriptor registry or rights decision.
"""
from __future__ import annotations

from pathlib import Path
import re

KEYS = frozenset({"name", "role", "rights", "sensitivity_floor"})
UNRESOLVED = frozenset({"", "TBD", "UNKNOWN", "NEEDS_VERIFICATION", "PROPOSED", "OWNER_TBD"})
# Non-public values of the SourceDescriptor sensitivity_floor enum
# (schemas/contracts/v1/source/source_descriptor.schema.json).
REVIEWED_SENSITIVITY_FLOORS = frozenset({"GENERALIZED", "RESTRICTED", "QUARANTINE"})
MAX_BYTES = 16 * 1024


def load_descriptor(path: Path) -> dict[str, str]:
    """Return ``key: value`` pairs, or ``{}`` for anything unreadable or structured."""
    try:
        data = Path(path).read_bytes()
    except OSError:
        return {}
    if len(data) > MAX_BYTES:
        return {}
    try:
        lines = data.decode("utf-8").splitlines()
    except UnicodeError:
        return {}
    result: dict[str, str] = {}
    for line in lines:
        text = line.strip()
        if not text or text.startswith("#"):
            continue
        key, sep, value = text.partition(":")
        key, value = key.strip(), value.strip()
        if not sep or key not in KEYS or key in result or line[:1].isspace():
            return {}
        result[key] = value
    return result


def normalized(value: str) -> str:
    """Fold case, whitespace, hyphens, underscores and quotes for status comparison."""
    return re.sub(r"[\s_-]+", "_", value.strip().strip("'\"").upper()).strip("_")


def descriptor_blockers(descriptor: dict[str, str], *, name: str) -> tuple[str, ...]:
    """Blocker codes that keep a connector's routes at HOLD; empty means none found."""
    if not isinstance(descriptor, dict) or descriptor.get("name") != name:
        return ("DESCRIPTOR_INVALID",)
    return tuple(f"DESCRIPTOR_{key.upper()}_UNRESOLVED" for key in ("role", "rights")
                 if normalized(str(descriptor.get(key, ""))) in UNRESOLVED)


def sensitivity_floor_blockers(descriptor: dict[str, str]) -> tuple[str, ...]:
    """For sources whose records may be sensitive: only a reviewed non-public floor passes.

    Public, unresolved, unknown, or misspelled floors all block, so a connector-local
    ``public`` placeholder can never authorize a candidate route.
    """
    floor = normalized(str(descriptor.get("sensitivity_floor", ""))) if isinstance(
        descriptor, dict) else ""
    if floor in REVIEWED_SENSITIVITY_FLOORS:
        return ()
    return ("DESCRIPTOR_SENSITIVITY_FLOOR_UNREVIEWED",)
