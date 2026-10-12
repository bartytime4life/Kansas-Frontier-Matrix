from __future__ import annotations

import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
CANONICAL_JOIN_SCHEMA = (
    REPO_ROOT / "schemas/contracts/v1/joins/habitat-fauna-join.schema.json"
)
HABITAT_JOIN_MIRROR = (
    REPO_ROOT
    / "schemas/contracts/v1/domains/habitat/habitat-fauna-join.schema.json"
)
LOCAL_SCHEMA_AUTHORITY_KEYS = frozenset(
    {"type", "properties", "required", "additionalProperties", "allOf", "anyOf", "oneOf"}
)


def _load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _local_schema_authority_keys(schema: dict) -> set[str]:
    return set(schema) & LOCAL_SCHEMA_AUTHORITY_KEYS


def test_habitat_fauna_domain_schema_is_one_way_compatibility_mirror() -> None:
    canonical = _load_json(CANONICAL_JOIN_SCHEMA)
    mirror = _load_json(HABITAT_JOIN_MIRROR)

    assert canonical["x-kfm"]["status"] == "PROPOSED"
    assert canonical["properties"] == {}
    assert canonical["additionalProperties"] is True

    assert mirror["x-kfm"]["status"] == "MIRROR"
    assert (
        mirror["x-kfm"]["canonical_schema"]
        == "schemas/contracts/v1/joins/habitat-fauna-join.schema.json"
    )
    assert "contract_doc" not in mirror["x-kfm"]
    assert mirror["$ref"] == "../../joins/habitat-fauna-join.schema.json"
    assert _local_schema_authority_keys(mirror) == set()
    assert (
        HABITAT_JOIN_MIRROR.parent.joinpath(mirror["$ref"]).resolve()
        == CANONICAL_JOIN_SCHEMA.resolve()
    )


def test_parallel_habitat_fauna_schema_shape_is_rejected_by_regression_guard() -> None:
    mirror = _load_json(HABITAT_JOIN_MIRROR)
    previous_parallel_scaffold = {
        **mirror,
        "type": "object",
        "properties": {},
        "additionalProperties": True,
    }

    assert _local_schema_authority_keys(mirror) == set()
    assert _local_schema_authority_keys(previous_parallel_scaffold) == {
        "type",
        "properties",
        "additionalProperties",
    }
