#!/usr/bin/env python3
"""Validate SuitabilityModel candidates against the current (scaffold) schema,
plus one optional, well-grounded semantic check: ModelCardEnvelope linkage.

``schemas/contracts/v1/domains/habitat/suitability_model.schema.json`` is a
PROPOSED scaffold with empty ``properties`` and ``additionalProperties:
true`` (see ``contracts/domains/habitat/suitability_model.md``, "Schema
posture", "Recommended semantics", and "Model-card burden" -- the field
list there, including ``model_card_ref`` itself, is explicitly not yet
enforced, and open questions such as the accepted model-card field set
remain NEEDS VERIFICATION pending a domain-steward decision).

This entrypoint therefore still checks only what the shared JSON Schema
runner would check against the scaffold as it stands: valid JSON, a JSON
object at the root, no duplicate keys, no non-finite numbers, and
conformance with whatever the schema currently declares (nothing, field-
wise). It additionally checks exactly one thing that IS well-grounded: if a
candidate declares a ``model_card_ref``, the referenced document must
independently pass the real, already-implemented governance
ModelCardEnvelope validator
(``tools/validators/governance/validate_model_card_envelope.py``). This does
not make ``model_card_ref`` required -- it remains a PROPOSED field -- and
it asserts no other SuitabilityModel identity, model-versus-observed source
role, uncertainty, evidence, or release semantics.

``model_card_ref`` is resolved here as a plain repository-root-relative (or
absolute) filesystem path to a JSON document. No KFM URI resolver contract
exists yet for cross-object references, so this is a deliberately minimal,
locally-scoped convention for this validator only; it is not a claim that
``kfm://`` or other ref schemes resolve this way anywhere else in the repo.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, Sequence


REPO_ROOT = Path(__file__).resolve().parents[4]
GOVERNANCE_DIR = REPO_ROOT / "tools/validators/governance"
HASHING_SRC = REPO_ROOT / "packages/hashing/src"
for _import_root in (REPO_ROOT, GOVERNANCE_DIR, HASHING_SRC):
    if str(_import_root) not in sys.path:
        sys.path.insert(0, str(_import_root))

from tools.validators._common.jsonschema_runner import load_validator  # noqa: E402
from hashing import JsonInputError, load_json_file  # noqa: E402
from model_card_envelope_core import (  # noqa: E402
    validate_file as validate_model_card_envelope_file,
)


SCHEMA_PATH = (
    REPO_ROOT / "schemas/contracts/v1/domains/habitat/suitability_model.schema.json"
)
FIXTURES_DIR = REPO_ROOT / "fixtures/domains/habitat/suitability_model"

_VALIDATOR = load_validator(SCHEMA_PATH)


def _check_model_card_linkage(candidate: dict[str, Any]) -> str | None:
    """Return a failure message, or None if the (optional) link is fine."""

    ref = candidate.get("model_card_ref")
    if ref is None:
        return None
    if not isinstance(ref, str) or not ref:
        return "model_card_ref must be a non-empty string path"

    resolved = Path(ref)
    if not resolved.is_absolute():
        resolved = REPO_ROOT / ref
    if resolved.is_symlink() or not resolved.is_file():
        return f"model_card_ref does not resolve to a regular file: {ref}"

    result = validate_model_card_envelope_file(resolved)
    if result.outcome != "PASS":
        codes = ", ".join(finding.code for finding in result.findings) or "no findings"
        return (
            "model_card_ref target failed ModelCardEnvelope validation: "
            f"outcome={result.outcome} findings=[{codes}]"
        )
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

    return _check_model_card_linkage(candidate)


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
    """Run shared shape validation, plus model-card linkage, for explicit files or --fixtures."""

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
