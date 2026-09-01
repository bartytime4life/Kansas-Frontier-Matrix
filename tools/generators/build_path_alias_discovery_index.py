#!/usr/bin/env python3
"""Build deterministic discovery metadata from the governed path-alias register.

The source register remains a machine projection of accepted directory-governance
state. This generator exposes stable alias, identity, consumer, and facet lookups
without authorizing aliases, writes, migrations, retirement, or publication.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any

PROFILE = "kfm.path-alias-discovery-index.v1"
SOURCE_REGISTRY = "path_alias_register"
SOURCE_AUTHORITY = "machine_projection_only"
OUTPUT_AUTHORITY = "derived_discovery_only"
FACET_FIELDS = (
    "class",
    "status",
    "object_family",
    "consumer_closure",
    "verification_state",
)
ALIAS_FIELDS = (
    "alias_id",
    "class",
    "status",
    "old_path",
    "canonical_target",
    "object_family",
    "consumer_closure",
    "read_rule",
    "write_rule",
    "authority_mode",
    "body_mode",
    "verification_state",
)


class DiscoveryIndexError(ValueError):
    """Raised when the canonical register cannot safely produce an index."""


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DiscoveryIndexError(f"duplicate JSON key: {key}")
        result[key] = value
    return result


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
        raise DiscoveryIndexError(
            f"unable to read JSON-compatible register: {exc}"
        ) from exc
    if not isinstance(value, dict):
        raise DiscoveryIndexError("path-alias register root must be an object")
    return value


def _string(value: Any, field: str) -> str:
    if not isinstance(value, str) or not value:
        raise DiscoveryIndexError(f"{field} must be a non-empty string")
    return value


def _identity_mapping(value: Any, alias_id: str) -> tuple[str, list[str], str]:
    if not isinstance(value, dict):
        raise DiscoveryIndexError(f"{alias_id}.identity_mapping must be an object")
    canonical_id = _string(value.get("canonical_id"), f"{alias_id}.canonical_id")
    identity_rule = _string(value.get("identity_rule"), f"{alias_id}.identity_rule")
    raw_aliases = value.get("aliases")
    if not isinstance(raw_aliases, list) or not raw_aliases:
        raise DiscoveryIndexError(f"{alias_id}.identity aliases must be a non-empty array")
    aliases = [
        _string(item, f"{alias_id}.identity aliases[{index}]")
        for index, item in enumerate(raw_aliases)
    ]
    if len(aliases) != len(set(aliases)):
        raise DiscoveryIndexError(f"{alias_id}.identity aliases contain duplicates")
    if canonical_id in aliases:
        raise DiscoveryIndexError(f"{alias_id}.canonical identity is also an alias")
    return canonical_id, sorted(aliases), identity_rule


def _consumers(value: Any, alias_id: str) -> list[dict[str, str]]:
    if not isinstance(value, list):
        raise DiscoveryIndexError(f"{alias_id}.consumers must be an array")
    consumers: list[dict[str, str]] = []
    for index, raw_consumer in enumerate(value):
        if not isinstance(raw_consumer, dict):
            raise DiscoveryIndexError(
                f"{alias_id}.consumers[{index}] must be an object"
            )
        consumers.append(
            {
                "consumer_id": _string(
                    raw_consumer.get("consumer_id"),
                    f"{alias_id}.consumers[{index}].consumer_id",
                ),
                "kind": _string(
                    raw_consumer.get("kind"),
                    f"{alias_id}.consumers[{index}].kind",
                ),
                "state": _string(
                    raw_consumer.get("state"),
                    f"{alias_id}.consumers[{index}].state",
                ),
            }
        )
    ids = [item["consumer_id"] for item in consumers]
    if len(ids) != len(set(ids)):
        raise DiscoveryIndexError(f"{alias_id}.consumers contain duplicate consumer_id values")
    return sorted(consumers, key=lambda item: item["consumer_id"])


def _reverse_index(
    grouped: dict[str, set[str]], *, key_name: str
) -> list[dict[str, Any]]:
    return [
        {key_name: key, "alias_ids": sorted(alias_ids)}
        for key, alias_ids in sorted(grouped.items())
    ]


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

    aliases: list[dict[str, Any]] = []
    alias_ids: list[str] = []
    old_paths: list[str] = []
    canonical_ids: list[str] = []
    identity_aliases: list[str] = []
    identity_index: dict[str, set[str]] = defaultdict(set)
    consumer_index: dict[str, set[str]] = defaultdict(set)
    facet_indexes: dict[str, dict[str, set[str]]] = {
        field: defaultdict(set) for field in FACET_FIELDS
    }

    for index, raw_alias in enumerate(raw_aliases):
        if not isinstance(raw_alias, dict):
            raise DiscoveryIndexError(f"aliases[{index}] must be an object")
        alias_id = _string(raw_alias.get("alias_id"), f"aliases[{index}].alias_id")
        item: dict[str, Any] = {}
        for field in ALIAS_FIELDS:
            item[field] = _string(raw_alias.get(field), f"{alias_id}.{field}")
        if item["old_path"] == item["canonical_target"]:
            raise DiscoveryIndexError(f"{alias_id} aliases its own canonical target")

        canonical_id, mapped_aliases, identity_rule = _identity_mapping(
            raw_alias.get("identity_mapping"), alias_id
        )
        consumers = _consumers(raw_alias.get("consumers"), alias_id)
        item["identity"] = {
            "canonical_id": canonical_id,
            "aliases": mapped_aliases,
            "identity_rule": identity_rule,
        }
        item["consumers"] = consumers
        aliases.append(item)
        alias_ids.append(alias_id)
        old_paths.append(item["old_path"])
        canonical_ids.append(canonical_id)
        identity_aliases.extend(mapped_aliases)
        identity_index[canonical_id].add(alias_id)
        for identity_alias in mapped_aliases:
            identity_index[identity_alias].add(alias_id)
        for consumer in consumers:
            consumer_index[consumer["consumer_id"]].add(alias_id)
        for field in FACET_FIELDS:
            facet_indexes[field][item[field]].add(alias_id)

    if len(alias_ids) != len(set(alias_ids)):
        raise DiscoveryIndexError("alias_id values must be unique")
    if len(old_paths) != len(set(old_paths)):
        raise DiscoveryIndexError("old_path values must be unique")
    if len(canonical_ids) != len(set(canonical_ids)):
        raise DiscoveryIndexError("canonical identity values must be unique")
    if len(identity_aliases) != len(set(identity_aliases)):
        raise DiscoveryIndexError("identity alias values must be globally unique")
    if set(canonical_ids).intersection(identity_aliases):
        raise DiscoveryIndexError("canonical identities and identity aliases must not overlap")

    aliases.sort(key=lambda item: item["alias_id"])
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
            "base_ref": register.get("base_ref"),
        },
        "alias_count": len(aliases),
        "aliases": aliases,
        "identity_index": _reverse_index(identity_index, key_name="identity"),
        "consumer_index": _reverse_index(consumer_index, key_name="consumer_id"),
        "facets": {
            field: _reverse_index(values, key_name="value")
            for field, values in sorted(facet_indexes.items())
        },
        "non_effects": {
            "aliases_authorized": False,
            "consumer_closure_decided": False,
            "paths_migrated_or_deleted": False,
            "publication_inferred": False,
        },
    }


def render_index(index: dict[str, Any]) -> str:
    return json.dumps(index, sort_keys=True, separators=(",", ":")) + "\n"


def _parser() -> argparse.ArgumentParser:
    repo_root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser(
        description="Build deterministic discovery metadata from the KFM path-alias register."
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
        output = render_index(build_discovery_index(register, source_path=source_path))
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
