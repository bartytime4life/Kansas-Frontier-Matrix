#!/usr/bin/env python3
"""Build a deterministic discovery-only projection from the KFM object-family register.

The source register remains authoritative only as the repository's navigational
object-family index. This generator derives producer, consumer, and dependency
lookups for discovery clients without adding object-family meaning, policy,
evidence, release, or publication authority.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from collections import defaultdict
from pathlib import Path
from typing import Any, Iterable

PROFILE = "kfm.object-family-discovery-index.v2"
SOURCE_REGISTRY = "object_family_register"
SOURCE_AUTHORITY = "navigational_index_only"
OUTPUT_AUTHORITY = "derived_discovery_only"
RELATION_FIELDS = (
    "dependency_family_ids",
    "evidence_family_ids",
    "release_family_ids",
    "correction_family_ids",
    "rollback_family_ids",
)
RELATION_KIND_BY_FIELD = {
    "dependency_family_ids": "dependency",
    "evidence_family_ids": "evidence",
    "release_family_ids": "release",
    "correction_family_ids": "correction",
    "rollback_family_ids": "rollback",
}
PASSTHROUGH_FIELDS = (
    "family_id",
    "display_name",
    "family_kind",
    "maturity",
    "implementation_status",
    "lifecycle_stage",
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
        raise DiscoveryIndexError("object-family register root must be an object")
    return value


def _string_list(entry: dict[str, Any], field: str, family_id: str) -> list[str]:
    value = entry.get(field, [])
    if not isinstance(value, list) or any(
        not isinstance(item, str) or not item for item in value
    ):
        raise DiscoveryIndexError(
            f"{family_id}.{field} must be an array of non-empty strings"
        )
    if len(value) != len(set(value)):
        raise DiscoveryIndexError(f"{family_id}.{field} contains duplicate values")
    return sorted(value)


def _family_id(entry: dict[str, Any], index: int) -> str:
    value = entry.get("family_id")
    if not isinstance(value, str) or not value:
        raise DiscoveryIndexError(
            f"entries[{index}].family_id must be a non-empty string"
        )
    return value


def _class_index(
    entries: Iterable[dict[str, Any]], field: str, key: str
) -> list[dict[str, Any]]:
    grouped: dict[str, set[str]] = defaultdict(set)
    for entry in entries:
        family_id = entry["family_id"]
        for class_name in entry[field]:
            grouped[class_name].add(family_id)
    return [
        {key: class_name, "family_ids": sorted(family_ids)}
        for class_name, family_ids in sorted(grouped.items())
    ]


def build_discovery_index(
    register: dict[str, Any], *, source_path: str
) -> dict[str, Any]:
    if register.get("registry") != SOURCE_REGISTRY:
        raise DiscoveryIndexError("unexpected source registry")
    if register.get("authority") != SOURCE_AUTHORITY:
        raise DiscoveryIndexError(
            "source registry authority must remain navigational_index_only"
        )

    raw_entries = register.get("entries")
    if not isinstance(raw_entries, list):
        raise DiscoveryIndexError("entries must be an array")

    ids: list[str] = []
    normalized: list[dict[str, Any]] = []
    for index, raw_entry in enumerate(raw_entries):
        if not isinstance(raw_entry, dict):
            raise DiscoveryIndexError(f"entries[{index}] must be an object")
        family_id = _family_id(raw_entry, index)
        ids.append(family_id)
        item: dict[str, Any] = {}
        for field in PASSTHROUGH_FIELDS:
            value = raw_entry.get(field)
            if not isinstance(value, str) or not value:
                raise DiscoveryIndexError(
                    f"{family_id}.{field} must be a non-empty string"
                )
            item[field] = value
        item["producer_classes"] = _string_list(
            raw_entry, "producer_classes", family_id
        )
        item["consumer_classes"] = _string_list(
            raw_entry, "consumer_classes", family_id
        )
        for field in RELATION_FIELDS:
            item[field] = _string_list(raw_entry, field, family_id)
        normalized.append(item)

    if len(ids) != len(set(ids)):
        raise DiscoveryIndexError("family_id values must be unique")

    known_ids = set(ids)
    relation_edges: list[dict[str, str]] = []
    incoming_relations: dict[tuple[str, str], set[str]] = defaultdict(set)
    for item in normalized:
        family_id = item["family_id"]
        for field in RELATION_FIELDS:
            for related_id in item[field]:
                if related_id not in known_ids:
                    raise DiscoveryIndexError(
                        f"unknown family in {field}: {family_id} -> {related_id}"
                    )
                relation = RELATION_KIND_BY_FIELD[field]
                relation_edges.append(
                    {
                        "relation": relation,
                        "from_family_id": family_id,
                        "to_family_id": related_id,
                    }
                )
                incoming_relations[(relation, related_id)].add(family_id)

    families = sorted(normalized, key=lambda item: item["family_id"])
    relation_edges.sort(
        key=lambda edge: (
            edge["relation"],
            edge["from_family_id"],
            edge["to_family_id"],
        )
    )
    dependency_edges = [
        {
            "from_family_id": edge["from_family_id"],
            "to_family_id": edge["to_family_id"],
        }
        for edge in relation_edges
        if edge["relation"] == "dependency"
    ]
    relation_index = [
        {
            "relation": relation,
            "to_family_id": to_family_id,
            "from_family_ids": sorted(from_family_ids),
        }
        for (relation, to_family_id), from_family_ids in sorted(
            incoming_relations.items()
        )
    ]
    relation_counts = {
        relation: sum(
            1 for edge in relation_edges if edge["relation"] == relation
        )
        for relation in sorted(RELATION_KIND_BY_FIELD.values())
    }

    return {
        "profile": PROFILE,
        "authority": OUTPUT_AUTHORITY,
        "authority_created": False,
        "scope": "object-family-discovery-metadata-only",
        "source": {
            "path": source_path,
            "registry": register.get("registry"),
            "version": register.get("version"),
            "status": register.get("status"),
            "authority": register.get("authority"),
            "base_ref": register.get("base_ref"),
        },
        "family_count": len(families),
        "families": families,
        "producer_index": _class_index(
            families, "producer_classes", "producer_class"
        ),
        "consumer_index": _class_index(
            families, "consumer_classes", "consumer_class"
        ),
        "dependency_edges": dependency_edges,
        "relation_edges": relation_edges,
        "relation_index": relation_index,
        "relation_counts": relation_counts,
    }


def render_index(index: dict[str, Any]) -> str:
    return json.dumps(index, sort_keys=True, separators=(",", ":")) + "\n"


def _parser() -> argparse.ArgumentParser:
    repo_root = Path(__file__).resolve().parents[2]
    parser = argparse.ArgumentParser(
        description=(
            "Build deterministic discovery metadata from the KFM object-family register."
        )
    )
    parser.add_argument(
        "--register",
        type=Path,
        default=repo_root / "control_plane" / "object_family_register.yaml",
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
