"""Keep Geology schema metadata linked to existing semantic contracts."""

from __future__ import annotations

import json
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[4]
SCHEMA_ROOT = REPO_ROOT / "schemas" / "contracts" / "v1" / "domains" / "geology"
CONTRACT_ROOT = REPO_ROOT / "contracts" / "domains" / "geology"


def _pascal_case(stem: str) -> str:
    return "".join(part[:1].upper() + part[1:] for part in stem.split("_"))


def test_existing_object_family_contract_links_resolve_exactly() -> None:
    """A schema must not point at a missing alias when its contract exists."""

    checked: list[str] = []
    mismatches: list[str] = []

    for schema_path in sorted(SCHEMA_ROOT.glob("*.schema.json")):
        stem = schema_path.name.removesuffix(".schema.json")
        contract_path = CONTRACT_ROOT / f"{_pascal_case(stem)}.md"
        if not contract_path.is_file():
            continue

        checked.append(schema_path.name)
        document = json.loads(schema_path.read_text(encoding="utf-8"))
        declared = document.get("x-kfm", {}).get("contract_doc")
        expected = contract_path.relative_to(REPO_ROOT).as_posix()
        if declared != expected:
            mismatches.append(
                f"{schema_path.relative_to(REPO_ROOT).as_posix()}: "
                f"expected {expected!r}, got {declared!r}"
            )

    assert checked, "no Geology schema/contract pairs were discovered"
    assert not mismatches, "\n".join(mismatches)
