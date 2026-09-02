"""CLI and reviewed-fixture replay for governed ModelCardEnvelope validation."""
from __future__ import annotations

import argparse
import copy
import json
import sys
from pathlib import Path
from typing import Any, Mapping, Sequence

MODULE_DIR = Path(__file__).resolve().parent
if str(MODULE_DIR) not in sys.path:
    sys.path.insert(0, str(MODULE_DIR))

from model_card_envelope_core import (  # noqa: E402
    CanonicalizationFailure,
    EXIT_CODES,
    JsonInputError,
    REPO_ROOT,
    SCOPE,
    ValidationResult,
    expected_spec_hash,
    load_json_file,
    serialize_result,
    validate_document,
    validate_file,
)

FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/governance/model_card_envelope"
FIXTURE_BASE = FIXTURE_ROOT / "base.json"
FIXTURE_CASES = FIXTURE_ROOT / "cases"
FIXTURE_PROFILE = "kfm.governance.model-card-envelope.fixture-suite.v1"


def _parts(path: object) -> tuple[str, ...]:
    if not isinstance(path, str) or not path.startswith("/") or len(path) > 256: raise ValueError
    result = tuple(part.replace("~1", "/").replace("~0", "~") for part in path[1:].split("/"))
    if not result or any(not part for part in result): raise ValueError
    return result


def _mutate(doc: dict[str, Any], mutation: Mapping[str, Any]) -> None:
    parts = _parts(mutation.get("path")); target: Any = doc
    for part in parts[:-1]: target = target[part]
    key, op, value = parts[-1], mutation.get("op"), copy.deepcopy(mutation.get("value"))
    if op == "set": target[key] = value; return
    current = target[key]
    if not isinstance(current, list): raise ValueError
    if op == "add": current.append(value); current.sort(); return
    if op == "remove": current.remove(value); return
    raise ValueError


def build_fixture_case(case: Mapping[str, Any], base: Mapping[str, Any]) -> dict[str, Any]:
    doc = copy.deepcopy(dict(base)); mutations = case.get("mutations")
    if not isinstance(mutations, list) or len(mutations) > 40: raise ValueError
    for mutation in mutations:
        if not isinstance(mutation, dict): raise ValueError
        _mutate(doc, mutation)
    if case.get("rehash") is True: doc["spec_hash"] = expected_spec_hash(doc)
    elif case.get("rehash") is not False: raise ValueError
    return doc


def load_fixture_suite() -> tuple[dict[str, Any], list[dict[str, Any]], list[Path]]:
    base = load_json_file(FIXTURE_BASE)
    if not isinstance(base, dict):
        raise ValueError("fixture base must be an object")
    if FIXTURE_CASES.is_symlink() or not FIXTURE_CASES.is_dir():
        raise ValueError("fixture case directory is invalid")
    paths = sorted(FIXTURE_CASES.glob("*.json"), key=lambda item: item.name)
    if not paths or len(paths) > 100:
        raise ValueError("fixture case count is outside the bounded profile")
    cases: list[dict[str, Any]] = []
    for path in paths:
        if path.is_symlink() or not path.is_file():
            raise ValueError("fixture case must be a regular file")
        case = load_json_file(path)
        if not isinstance(case, dict):
            raise ValueError("fixture case must be an object")
        cases.append(case)
    return base, cases, paths


def run_fixture_suite() -> tuple[bool, dict[str, object]]:
    try:
        base, entries, paths = load_fixture_suite()
    except (JsonInputError, OSError, ValueError):
        return False, {"scope": SCOPE, "ok": False, "cases": []}
    ids = [case.get("case_id") for case in entries]
    filenames = [path.stem for path in paths]
    ok = (
        all(isinstance(item, str) for item in ids)
        and ids == sorted(ids)
        and ids == filenames
        and len(ids) == len(set(ids))
    )
    report = []
    for case in entries:
        try:
            expected = case["expected"]
            result = validate_document(build_fixture_case(case, base))
            codes = sorted({finding.code for finding in result.findings})
            case_ok = (
                isinstance(expected, dict)
                and expected.get("finding_codes")
                == sorted(expected.get("finding_codes", []))
                and result.outcome == expected.get("outcome")
                and codes == expected.get("finding_codes")
            )
        except (KeyError, TypeError, ValueError, CanonicalizationFailure):
            case_ok = False
            result = ValidationResult("ERROR", ())
            codes = []
            expected = {}
        ok = ok and case_ok
        report.append(
            {
                "case_id": case.get("case_id"),
                "actual_outcome": result.outcome,
                "expected_outcome": expected.get("outcome"),
                "actual_findings": codes,
                "expected_findings": expected.get("finding_codes"),
                "ok": case_ok,
            }
        )
    counts = {
        outcome: sum(item["actual_outcome"] == outcome for item in report)
        for outcome in EXIT_CODES
    }
    return ok, {
        "scope": SCOPE,
        "fixture_profile": FIXTURE_PROFILE,
        "counts": counts,
        "cases": report,
        "ok": ok,
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser=argparse.ArgumentParser(description="Validate fixture-first governed model-card envelopes.")
    parser.add_argument("--candidate", type=Path); parser.add_argument("--fixtures", action="store_true"); args=parser.parse_args(argv)
    if args.fixtures:
        if args.candidate is not None: parser.error("--fixtures cannot be combined with --candidate")
        ok, report=run_fixture_suite(); print(json.dumps(report,sort_keys=True,separators=(",",":"))); return 0 if ok else 1
    if args.candidate is None: parser.error("--candidate is required unless --fixtures is used")
    result=validate_file(args.candidate); print(serialize_result(result)); return EXIT_CODES[result.outcome]

if __name__ == "__main__": raise SystemExit(main())
