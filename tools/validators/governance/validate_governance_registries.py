#!/usr/bin/env python3
"""Validate KFM stewardship and authority registries."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[3]
REGISTRIES = {
    "stewardship": (
        ROOT / "control_plane" / "stewardship" / "assignments.json",
        ROOT
        / "schemas"
        / "contracts"
        / "v1"
        / "governance"
        / "stewardship_assignments.schema.json",
    ),
    "authority": (
        ROOT / "docs" / "evidence" / "authority-index.json",
        ROOT
        / "schemas"
        / "contracts"
        / "v1"
        / "governance"
        / "authority_index.schema.json",
    ),
}


class RegistryError(ValueError):
    pass


def read_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise RegistryError(f"{path}: {exc}") from exc


def validate_schema(document: Any, schema: Any) -> None:
    errors = sorted(
        Draft202012Validator(
            schema, format_checker=FormatChecker()
        ).iter_errors(document),
        key=lambda error: tuple(str(part) for part in error.absolute_path),
    )
    if errors:
        raise RegistryError(
            "; ".join(
                f"{'/'.join(str(part) for part in error.absolute_path) or '<root>'}: "
                f"{error.message}"
                for error in errors
            )
        )


def validate_stewardship(document: dict[str, Any]) -> None:
    seen: set[str] = set()
    for assignment in document["assignments"]:
        identifier = assignment["assignment_id"]
        if identifier in seen:
            raise RegistryError(f"duplicate assignment_id: {identifier}")
        seen.add(identifier)
        status = assignment["status"]
        assignee = assignment["assignee"]
        effective = assignment["effective_at"]
        if status == "ASSIGNED" and (not assignee or not effective):
            raise RegistryError(
                f"{identifier}: ASSIGNED requires assignee and effective_at"
            )
        if status != "ASSIGNED" and assignee is not None:
            raise RegistryError(f"{identifier}: {status} cannot name an assignee")
        overlap = set(assignment["granted_authorities"]) & set(
            assignment["denied_authorities"]
        )
        if overlap:
            raise RegistryError(
                f"{identifier}: authority both granted and denied: {sorted(overlap)}"
            )


def validate_authority(document: dict[str, Any]) -> None:
    implementation = [
        record
        for record in document["records"]
        if record["implementation_authority"]
    ]
    if len(implementation) != 1:
        raise RegistryError(
            "authority index must name exactly one implementation authority"
        )
    record = implementation[0]
    if record["location"] != "github" or record["role"] != "implementation":
        raise RegistryError(
            "implementation authority must be the GitHub implementation record"
        )
    for candidate in document["records"]:
        if (
            candidate["status"] == "CURRENT"
            and candidate["record_id"] != "github-main"
            and candidate["currentness_pointer"] != "github-main"
        ):
            raise RegistryError(
                f"{candidate['record_id']}: current external record must point to github-main"
            )


def validate(kind: str) -> None:
    document_path, schema_path = REGISTRIES[kind]
    document = read_json(document_path)
    validate_schema(document, read_json(schema_path))
    if kind == "stewardship":
        validate_stewardship(document)
    else:
        validate_authority(document)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "kind",
        choices=["stewardship", "authority", "all"],
        default="all",
        nargs="?",
    )
    args = parser.parse_args()
    try:
        kinds = REGISTRIES if args.kind == "all" else [args.kind]
        for kind in kinds:
            validate(kind)
    except RegistryError as exc:
        print(f"GOVERNANCE_REGISTRY_INVALID: {exc}")
        return 2
    print("GOVERNANCE_REGISTRY_VALID")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
