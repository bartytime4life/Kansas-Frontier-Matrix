#!/usr/bin/env python3
"""Validate HabitatPatch candidates against the current (scaffold) schema,
plus reference-hygiene checks for two PROPOSED connectivity fields.

``schemas/contracts/v1/domains/habitat/habitat_patch.schema.json`` is a
PROPOSED scaffold with empty ``properties`` and ``additionalProperties:
true`` (see ``contracts/domains/habitat/habitat_patch.md``, "Schema posture"
and "Recommended semantics" -- the field list there is explicitly not yet
enforced, and open questions such as the canonical source-role spelling and
which sibling contract document is canonical remain NEEDS VERIFICATION
pending a domain-steward decision).

This entrypoint therefore still checks only what the shared JSON Schema
runner would check against the scaffold as it stands: valid JSON, a JSON
object at the root, no duplicate object keys, no non-finite numbers, and
conformance with whatever the schema currently declares (nothing, field-
wise). It additionally checks reference-string HYGIENE on two of
HabitatPatch's own PROPOSED fields: ``connectivity_edge_refs`` and
``corridor_refs``, which point at ``ConnectivityEdge`` and ``Corridor`` --
two other Habitat object families that are themselves still empty PROPOSED
scaffolds
(``schemas/contracts/v1/domains/habitat/connectivity_edge.schema.json``,
``corridor.schema.json``). There is nothing real to resolve these
references against yet, so this validator does not attempt that. If a
candidate declares either field, it checks only that the array is sorted,
unique, made of strings matching a bounded reference grammar, and free of
internal-lifecycle prefixes (``raw:``, ``work:``, ``quarantine:``,
``internal:``, ``canonical:``, ``model:``) -- reusing, unchanged, the same
rule the shared CatalogMatrix closure validator already applies elsewhere
(``tools/validators/validate_catalog_matrix_closure.py``). Neither field is
required, and this asserts no other HabitatPatch identity, source-role,
geometry, evidence, sensitivity, policy, or release semantics.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any, Sequence


REPO_ROOT = Path(__file__).resolve().parents[4]
HASHING_SRC = REPO_ROOT / "packages/hashing/src"
for _import_root in (REPO_ROOT, HASHING_SRC):
    if str(_import_root) not in sys.path:
        sys.path.insert(0, str(_import_root))

from tools.validators._common.jsonschema_runner import load_validator  # noqa: E402
from hashing import JsonInputError, load_json_file  # noqa: E402


SCHEMA_PATH = (
    REPO_ROOT / "schemas/contracts/v1/domains/habitat/habitat_patch.schema.json"
)
FIXTURES_DIR = REPO_ROOT / "fixtures/domains/habitat/patch"

_VALIDATOR = load_validator(SCHEMA_PATH)

_REF_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._~:/#?=&%+@-]{0,319}$")
_DENIED_PREFIXES = (
    "raw:",
    "work:",
    "quarantine:",
    "internal:",
    "canonical:",
    "model:",
)
_CONNECTIVITY_REF_FIELDS = ("connectivity_edge_refs", "corridor_refs")


def _reference_hygiene_finding(candidate: dict[str, Any], field: str) -> str | None:
    """Return a failure message, or None if this optional ref array (or its absence) is fine."""

    value = candidate.get(field)
    if value is None:
        return None
    if (
        not isinstance(value, list)
        or not value
        or any(not isinstance(item, str) for item in value)
    ):
        return f"{field} must be a non-empty array of strings"

    if value != sorted(set(value)):
        return f"{field} must be sorted and unique: {value!r}"
    if any(not _REF_RE.fullmatch(item) for item in value):
        return f"{field} contains a reference that violates the bounded grammar: {value!r}"
    if any(item.casefold().startswith(_DENIED_PREFIXES) for item in value):
        return f"{field} contains a lifecycle-private reference, which is denied: {value!r}"
    return None


def _connectivity_finding(candidate: dict[str, Any]) -> str | None:
    for field in _CONNECTIVITY_REF_FIELDS:
        message = _reference_hygiene_finding(candidate, field)
        if message is not None:
            return message
    return None


def validate_candidate_file(path: Path) -> str | None:
    """Return a failure message, or None if the candidate passes."""

    try:
        candidate = load_json_file(path)
    except JsonInputError as exc:
        return str(exc)

    errors = sorted(
        _VALIDATOR.iter_errors(candidate),
        key=lambda error: (list(error.absolute_path), str(error.validator)),
    )
    if errors:
        return errors[0].message
    if not isinstance(candidate, dict):
        return "candidate document must be a JSON object"

    return _connectivity_finding(candidate)


def _validate_paths(paths: list[Path]) -> bool:
    ok = True
    for path in paths:
        message = validate_candidate_file(path)
        if message is None:
            print(f"OK {path}")
        else:
            print(f"FAIL {path}: {message}")
            ok = False
    return ok


def _run_fixtures() -> int:
    valid_dir = FIXTURES_DIR / "valid"
    invalid_dir = FIXTURES_DIR / "invalid"
    valid_files = sorted(valid_dir.glob("*.json"))
    invalid_files = sorted(invalid_dir.glob("*.json"))

    ok = True
    if not valid_files:
        print(f"FAIL {valid_dir}: no JSON fixtures found")
        ok = False
    for path in valid_files:
        message = validate_candidate_file(path)
        if message is None:
            print(f"OK {path}")
        else:
            print(f"FAIL {path}: {message}")
            ok = False

    if not invalid_files:
        print(f"FAIL {invalid_dir}: no JSON fixtures found")
        ok = False
    for path in invalid_files:
        message = validate_candidate_file(path)
        if message is not None:
            print(f"EXPECTED_FAIL {path}: {message}")
        else:
            print(f"FAIL {path}: expected rejection")
            ok = False

    return 0 if ok else 1


def main(argv: Sequence[str] | None = None) -> int:
    """Run shared shape validation, plus connectivity ref hygiene, for explicit files or --fixtures."""

    arguments = list(sys.argv[1:] if argv is None else argv)
    if "--fixtures" in arguments and any(
        argument != "--fixtures" for argument in arguments
    ):
        print("Cannot combine --fixtures with explicit files", file=sys.stderr)
        return 2
    if "--fixtures" in arguments:
        return _run_fixtures()
    if not arguments:
        print("No files provided", file=sys.stderr)
        return 2
    return 0 if _validate_paths([Path(argument) for argument in arguments]) else 1


if __name__ == "__main__":
    raise SystemExit(main())
