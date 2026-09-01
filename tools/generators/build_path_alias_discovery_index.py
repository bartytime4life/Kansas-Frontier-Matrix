#!/usr/bin/env python3
"""Build deterministic discovery metadata from the governed KFM path-alias register.

The source register remains the machine projection of accepted Directory Rules
alias state. This generator derives lookup metadata for downstream discovery
clients without creating path, identity, migration, policy, release, or
publication authority.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path
from typing import Any

PROFILE = "kfm.path-alias-discovery-index.v1"
SOURCE_REGISTRY = "path_alias_register"
SOURCE_AUTHORITY = "machine_projection_only"
OUTPUT_AUTHORITY = "derived_discovery_only"
PASSTHROUGH_FIELDS = (
    "alias_id",
    "class",
    "status",
    "old_path",
    "canonical_target",
    "object_family",
    "read_rule",
    "write_rule",
    "authority_mode",
    "verification_state",
)


class DiscoveryIndexError(ValueError):
    """Raised when the canonical source cannot safely produce a discovery index."""


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key, value in pairs:
        if key in out:
            raise DiscoveryIndexError(f"duplicate JSON key: {key}")
        out[key] = value
    return out


def _reject_nonfinite(value: str) -> None:
    raise DiscoveryIndexError(f"non-finite JSON number: {value}")


def _parse_finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise DiscoveryIndexError(f"non-finite JSON number: {value}")
    return parsed


def load_register(path: Path) -> dict[str, Any]:
    try:
        with path.open("r", encoding="utf-8") as stream:
            value = json.load(
                stream,
                object_pairs_hook=_unique_object,
                parse_constant=_reject_nonfinite,
                parse_float=_parse_finite_float,
            )
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise DiscoveryIndexError(f"unable to read JSON-compatible register: {exc}") from exc
    if not isinstance(value, dict):
        raise DiscoveryIndexError("path-alias register root must be an object")
    return value


def _required_string(entry: dict[str, Any], field: str, alias_id: str) -> str:
    value = entry.get(field)
    if not isinstance(value, str) or not value:
        raise DiscoveryIndexError(f"{alias_id}.{field} must be a non-empty string")
    return value


def _identity_mapping(entry: dict[str, Any], alias_id: str) -> tuple[str, list[str], str]:
    raw = entry.get("identity_mapping")
    if not isinstance(raw, dict):
        raise DiscoveryIndexError(f"{alias_id}.identity_mapping must be an object")
    canonical_id = raw.get("canonical_id")
    identity_rule = raw.get("identity_rule")
    aliases = raw.get("aliases")
    if not isinstance(canonical_id, str) or not canonical_id:
        raise DiscoveryIndexError(
            f"{alias_id}.identity_mapping.canonical_id must be a non-empty string"
        )
    if not isinstance(identity_rule, str) or not identity_rule:
        raise DiscoveryIndexError(
            f"{alias_id}.identity_mapping.identity_rule must be a non-empty string"
        )
    if not isinstance(aliases, list) or any(
        not isinstance(value, str) or not value for value in aliases
    ):
        raise DiscoveryIndexError(
            f"{alias_id}.identity_mapping.aliases must be an array of non-empty strings"
        )
    if len(aliases) != len(set(aliases)):
        raise DiscoveryIndexError(
            f"{alias_id}.identity_mapping.aliases contains duplicate values"
        )
    if canonical_id in aliases:
        raise DiscoveryIndexError(
            f"{alias_id}.identity_mapping aliases canonical_id to itself"
        )
    return canonical_id, sorted(aliases), identity_rule


def build_discovery_index(
    register: dict[str, Any], *, source_path: str
) -> dict[str, Any]:
    if register.get("registry") != SOURCE_REGISTRY:
        raise DiscoveryIndexError("unexpected source registry")
    if register.get("authority") != SOURCE_AUTHORITY:
        raise DiscoveryIndexError(
            "source registry authority must remain machine_projection_only"
        )

    raw_aliases = register.get("aliases")
    if not isinstance(raw_aliases, list):
        raise DiscoveryIndexError("aliases must be an array")

    normalized: list[dict[str, Any]] = []
    alias_ids: list[str] = []
    old_paths: list[str] = []
    identity_seen: dict[str, str] = {}

    for index, raw_entry in enumerate(raw_aliases):
        if not isinstance(raw_entry, dict):
            raise DiscoveryIndexError(f"aliases[{index}] must be an object")
        raw_id = raw_entry.get("alias_id")
        if not isinstance(raw_id, str) or not raw_id:
            raise DiscoveryIndexError(
                f"aliases[{index}].alias_id must be a non-empty string"
            )
        alias_id = raw_id
        item = {
            field: _required_string(raw_entry, field, alias_id)
            for field in PASSTHROUGH_FIELDS
        }
        canonical_id, identity_aliases, identity_rule = _identity_mapping(
            raw_entry, alias_id
        )
        item["identity"] = {
            "canonical_id": canonical_id,
            "aliases": identity_aliases,
            "identity_rule": identity_rule,
        }
        alias_ids.append(alias_id)
        old_paths.append(item["old_path"])
        normalized.append(item)

        for identity_alias in identity_aliases:
            previous = identity_seen.get(identity_alias)
            if previous is not None:
                raise DiscoveryIndexError(
                    f"identity alias {identity_alias} is declared by both {previous} and {alias_id}"
                )
            identity_seen[identity_alias] = alias_id

    if len(alias_ids) != len(set(alias_ids)):
        raise DiscoveryIndexError("alias_id values must be unique")
    if len(old_paths) != len(set(old_paths)):
        raise DiscoveryIndexError("old_path values must be unique")

    old_path_set = set(old_paths)
    for item in normalized:
        if item["old_path"] == item["canonical_target"]:
            raise DiscoveryIndexError(f"{item['alias_id']} aliases a path to itself")
        if item["canonical_target"] in old_path_set:
            raise DiscoveryIndexError(
                f"{item['alias_id']} canonical_target points to another alias path"
            )

    aliases = sorted(normalized, key=lambda item: item["alias_id"])
    path_index = sorted(
        (
            {
                "old_path": item["old_path"],
                "canonical_target": item["canonical_target"],
                "alias_id": item["alias_id"],
            }
            for item in aliases
        ),
        key=lambda item: item["old_path"],
    )
    identity_index = sorted(
        (
            {
                "alias": identity_alias,
                "canonical_id": item["identity"]["canonical_id"],
                "path_alias_id": item["alias_id"],
            }
            for item in aliases
            for identity_alias in item["identity"]["aliases"]
        ),
        key=lambda item: item["alias"],
    )

    return {
        "profile": PROFILE,
        "authority": OUTPUT_AUTHORITY,
        "authority_created": False,
        "scope": "path-alias-discovery-metadata-only",
        "source": {
            "path": source_path,
            "registry": register.get("registry"),
            "version": register.get("version"),
            "status": register.get("status"),
            "authority": register.get("authority"),
            "coverage_scope": register.get("coverage_scope"),
            "base_ref": register.get("base_ref"),
        },
        "alias_count": len(aliases),
        "identity_alias_count": len(identity_index),
        "aliases": aliases,
        "path_index": path_index,
        "identity_alias_index": identity_index,
    }


def render_index(index: dict[str, Any]) -> str:
    return json.dumps(index, sort_keys=True, separators=(",", ":")) + "\n"


def _parser() -> argparse.ArgumentParser:
    repo_root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser(
        description=(
            "Build deterministic discovery metadata from the KFM path-alias register."
        )
    )
    parser.add_argument(
        "--register",
        type=Path,
        default=repo_root / "control_plane" / "path_alias_register.yaml",
    )
    parser.add_argument("--output", type=Path, default=None)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    try:
        register = load_register(args.register)
        repo_root = Path(__file__).resolve().parents[2]
        try:
            source_path = args.register.resolve().relative_to(repo_root).as_posix()
        except ValueError:
            source_path = args.register.as_posix()
        output = render_index(
            build_discovery_index(register, source_path=source_path)
        )
        if args.output is None:
            sys.stdout.write(output)
        else:
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(output, encoding="utf-8")
    except (DiscoveryIndexError, OSError) as exc:
        print(
            json.dumps(
                {
                    "profile": PROFILE,
                    "outcome": "ERROR",
                    "authority_created": False,
                    "error": str(exc),
                },
                sort_keys=True,
                separators=(",", ":"),
            )
        )
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
