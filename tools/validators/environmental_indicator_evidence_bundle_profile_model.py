"""Shared value types and bounded helpers for the environmental profile."""

from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


def _mapping(value: object) -> Mapping[str, object]:
    return value if isinstance(value, Mapping) else {}


def _list(value: object) -> list[object]:
    return value if isinstance(value, list) else []


def _string_list(value: object) -> list[str]:
    return [item for item in _list(value) if isinstance(item, str)]


def _parse_aware_datetime(value: object) -> datetime | None:
    if not isinstance(value, str):
        return None
    normalized = value[:-1] + "+00:00" if value.endswith(("Z", "z")) else value
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return None
    if parsed.tzinfo is None or parsed.utcoffset() is None:
        return None
    return parsed


def _hash_projection(value: Mapping[str, object]) -> dict[str, object]:
    return {key: item for key, item in value.items() if key != "spec_hash"}


def _stored_hash(value: object) -> str | None:
    candidate = _mapping(value).get("value")
    return candidate if isinstance(candidate, str) else None


def _is_placeholder_hash(value: object) -> bool:
    return (
        isinstance(value, str)
        and value.startswith("sha256:")
        and len(value) == 71
        and set(value[7:]) == {"0"}
    )


def _reference_ids(bundle: Mapping[str, object]) -> tuple[list[str], set[str], bool]:
    refs = _list(bundle.get("evidence_refs"))
    ordered: list[str] = []
    valid = True
    for item in refs:
        ref = _mapping(item).get("ref")
        if not isinstance(ref, str):
            valid = False
            continue
        ordered.append(ref)
    return ordered, set(ordered), valid


