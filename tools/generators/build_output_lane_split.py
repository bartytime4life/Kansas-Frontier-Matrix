#!/usr/bin/env python3
"""Validate and deterministically index a proposed output-lane manifest.

The tool never reads, moves, or copies referenced payload bytes. Its default mode
writes nothing. ``--write`` is limited to deterministic reviewer indexes in an
explicit empty directory.
"""
from __future__ import annotations

import argparse
import copy
import json
import math
import sys
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[2]
HASH_SRC = ROOT / "packages/hashing/src"
if str(HASH_SRC) not in sys.path:
    sys.path.insert(0, str(HASH_SRC))
try:
    from hashing import CanonicalizationFailure, compute_spec_hash
except ImportError as exc:  # fail closed when the repository hashing package is unavailable
    raise RuntimeError("repository hashing package is required") from exc

SCHEMA = ROOT / "schemas/contracts/v1/data/output_lane_split_manifest.schema.json"
FIXTURES = ROOT / "fixtures/contracts/v1/data/output_lane_split_manifest/cases.json"
MAX_BYTES = 2 * 1024 * 1024
MAX_SCHEMA_FINDINGS = 100
SCOPE = "pass32-output-lane-splitter-fixture-only"
LANES = ("FEATURE_VECTOR", "SCORECARD", "POLICY_REPORT", "RECEIPT", "PREFILTER")
ROLES = {
    "FEATURE_VECTOR": "ANALYSIS_DERIVATIVE",
    "SCORECARD": "REVIEW_SCORECARD",
    "POLICY_REPORT": "POLICY_REVIEW_CANDIDATE",
    "RECEIPT": "PROCESS_MEMORY_RECEIPT",
    "PREFILTER": "PREFILTER_DECISION_CANDIDATE",
}


class DuplicateKeyError(ValueError):
    """Input JSON repeated an object key."""


class NonFiniteNumberError(ValueError):
    """Input JSON contained a non-standard or non-finite number."""


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


@dataclass(frozen=True)
class Result:
    outcome: str
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return self.outcome == "PASS"


def _unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError
        value[key] = item
    return value


def _reject_constant(_value: str) -> None:
    raise NonFiniteNumberError


def _finite(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def canonical_hash(value: Mapping[str, Any]) -> str:
    """Return the repository-owned RFC 8785 JCS + SHA-256 spec hash."""

    return compute_spec_hash(value)


def _read(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("INPUT_NOT_FILE", "/")]
        if path.stat().st_size > MAX_BYTES:
            return None, [Finding("INPUT_TOO_LARGE", "/")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject_constant,
            parse_float=_finite,
        )
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except (UnicodeError, json.JSONDecodeError):
        return None, [Finding("JSON_INVALID", "/")]
    except OSError:
        return None, [Finding("INPUT_READ_ERROR", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def _schema_findings(value: Mapping[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = list(
            islice(
                Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(value),
                MAX_SCHEMA_FINDINGS + 1,
            )
        )
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    errors.sort(key=lambda error: (_pointer(error.absolute_path), str(error.validator)))
    findings = [
        Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in errors[:MAX_SCHEMA_FINDINGS]
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def _semantic_findings(value: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    candidate = {key: item for key, item in value.items() if key != "spec_hash"}
    try:
        actual_spec_hash = canonical_hash(candidate)
    except CanonicalizationFailure:
        findings.append(Finding("OUTPUT_LANE_CANONICALIZATION_ERROR", "/"))
    else:
        if value.get("spec_hash") != actual_spec_hash:
            findings.append(Finding("OUTPUT_LANE_SPEC_HASH_MISMATCH", "/spec_hash"))
    if value.get("required_lanes") != list(LANES):
        findings.append(Finding("OUTPUT_LANE_REQUIRED_LANES_INVALID", "/required_lanes"))

    outputs = value.get("outputs")
    if not isinstance(outputs, list):
        return findings
    represented: set[str] = set()
    seen_refs: set[str] = set()
    order: list[tuple[int, str]] = []
    for index, output in enumerate(outputs):
        if not isinstance(output, dict):
            continue
        lane = output.get("lane")
        if isinstance(lane, str) and lane in LANES:
            represented.add(lane)
            order.append((LANES.index(lane), str(output.get("output_id"))))
            if output.get("logical_role") != ROLES[lane]:
                findings.append(
                    Finding(
                        "OUTPUT_LANE_LOGICAL_ROLE_MISMATCH",
                        f"/outputs/{index}/logical_role",
                    )
                )
        ref = output.get("artifact_ref")
        if isinstance(ref, str):
            if ref in seen_refs:
                findings.append(
                    Finding("OUTPUT_LANE_DUPLICATE_ARTIFACT_REF", f"/outputs/{index}/artifact_ref")
                )
            seen_refs.add(ref)
    if represented != set(LANES):
        findings.append(Finding("OUTPUT_LANE_REQUIRED_LANE_UNREPRESENTED", "/outputs"))
    if order != sorted(order):
        findings.append(Finding("OUTPUT_LANE_ORDER_NONCANONICAL", "/outputs"))
    governance = value.get("governance")
    if isinstance(governance, dict) and any(item is not False for item in governance.values()):
        findings.append(Finding("OUTPUT_LANE_AUTHORITY_OVERREACH", "/governance"))
    return findings


def validate_payload(value: Mapping[str, Any]) -> Result:
    findings = _schema_findings(value)
    if not findings:
        findings = _semantic_findings(value)
    return Result("DENY", tuple(sorted(set(findings)))) if findings else Result("PASS", ())


def split_payload(value: Mapping[str, Any]) -> dict[str, Any]:
    if not validate_payload(value).ok:
        raise ValueError("manifest does not pass validation")
    lanes: dict[str, list[dict[str, Any]]] = {lane: [] for lane in LANES}
    for output in value["outputs"]:
        lanes[output["lane"]].append(
            {
                key: output[key]
                for key in (
                    "artifact_ref",
                    "artifact_sha256",
                    "logical_role",
                    "media_type",
                    "output_id",
                )
            }
        )
    return {
        "object_type": "OutputLaneSplitResult",
        "schema_version": "1.0.0",
        "source_manifest_id": value["manifest_id"],
        "source_spec_hash": value["spec_hash"],
        "status": "REVIEW_REQUIRED",
        "lane_order": list(LANES),
        "counts": {lane: len(lanes[lane]) for lane in LANES},
        "lanes": lanes,
        "writes_performed": False,
        "payloads_moved_or_copied": False,
        "promotion_authorized": False,
        "release_authorized": False,
        "publication_authorized": False,
    }


def write_indexes(result: Mapping[str, Any], output_dir: Path) -> list[Path]:
    if output_dir.exists():
        if output_dir.is_symlink() or not output_dir.is_dir():
            raise ValueError("output directory must be a real directory")
        if any(output_dir.iterdir()):
            raise ValueError("output directory must be empty")
    else:
        output_dir.mkdir(parents=True, exist_ok=False)
    written: list[Path] = []
    for lane in LANES:
        path = output_dir / f"{lane.lower()}.json"
        payload = {
            "object_type": "OutputLaneIndex",
            "schema_version": "1.0.0",
            "lane": lane,
            "source_manifest_id": result["source_manifest_id"],
            "source_spec_hash": result["source_spec_hash"],
            "outputs": result["lanes"][lane],
            "review_required": True,
            "writes_authorized": False,
        }
        path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        written.append(path)
    summary = dict(result)
    summary["writes_performed"] = True
    summary_path = output_dir / "split-summary.json"
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return [*written, summary_path]


def load_fixture_manifest() -> dict[str, Any]:
    value = json.loads(FIXTURES.read_text(encoding="utf-8"))
    if not isinstance(value, dict) or not isinstance(value.get("bases"), dict) or not isinstance(value.get("cases"), list):
        raise ValueError("fixture manifest is invalid")
    return value


def _replace_pointer(payload: dict[str, Any], path: str, value: Any) -> None:
    if not path.startswith("/"):
        raise ValueError("mutation path must be a JSON pointer")
    parts = [part.replace("~1", "/").replace("~0", "~") for part in path.split("/")[1:]]
    if not parts:
        raise ValueError("root replacement is denied")
    cursor: Any = payload
    for part in parts[:-1]:
        cursor = cursor[int(part)] if isinstance(cursor, list) else cursor[part]
    final = parts[-1]
    if isinstance(cursor, list):
        cursor[int(final)] = copy.deepcopy(value)
    elif isinstance(cursor, dict) and final in cursor:
        cursor[final] = copy.deepcopy(value)
    else:
        raise ValueError("mutation path is invalid")


def materialize_case(manifest: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    bases = manifest.get("bases")
    base_id = case.get("base")
    if not isinstance(bases, dict) or not isinstance(base_id, str) or not isinstance(bases.get(base_id), dict):
        raise ValueError("fixture base is invalid")
    payload = copy.deepcopy(bases[base_id])
    mutations = case.get("mutations", [])
    if not isinstance(mutations, list):
        raise ValueError("fixture mutations must be an array")
    for mutation in mutations:
        if not isinstance(mutation, dict) or mutation.get("op") != "replace" or not isinstance(mutation.get("path"), str):
            raise ValueError("only deterministic replace mutations are supported")
        _replace_pointer(payload, mutation["path"], mutation.get("value"))
    override = case.get("spec_hash_override")
    if override is not None and not isinstance(override, str):
        raise ValueError("spec_hash_override must be a string")
    payload["spec_hash"] = override or canonical_hash(
        {key: item for key, item in payload.items() if key != "spec_hash"}
    )
    return payload


def run_fixtures() -> int:
    try:
        manifest = load_fixture_manifest()
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError):
        return 2
    passed = True
    for case in manifest["cases"]:
        try:
            result = validate_payload(materialize_case(manifest, case))
        except (KeyError, TypeError, ValueError):
            result = Result("ERROR", (Finding("FIXTURE_PAYLOAD_INVALID", "/payload"),))
        actual = [{"code": item.code, "field": item.field} for item in result.findings]
        match = result.outcome == case["expected_outcome"] and actual == case["expected_findings"]
        print(_json({"case_id": case["case_id"], "outcome": result.outcome, "findings": actual, "suite_match": match}))
        passed = passed and match
    return 0 if passed else 1


def _validation_output(path: Path, result: Result) -> str:
    return _json(
        {
            "file": path.as_posix(),
            "outcome": result.outcome,
            "findings": [{"code": item.code, "field": item.field} for item in result.findings],
            "scope": SCOPE,
        }
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--output-dir", type=Path)
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.input or args.write or args.output_dir:
            parser.error("--fixtures cannot be combined with other arguments")
        return run_fixtures()
    if args.input is None:
        parser.error("input is required unless --fixtures is used")
    if args.write != (args.output_dir is not None):
        parser.error("--write and --output-dir must be supplied together")

    value, operational = _read(args.input)
    if value is None:
        result = Result("ERROR", tuple(sorted(set(operational))))
        print(_validation_output(args.input, result))
        return 2
    validation = validate_payload(value)
    if not validation.ok:
        print(_validation_output(args.input, validation))
        return 1
    result = split_payload(value)
    if args.write:
        written = write_indexes(result, args.output_dir)
        result = {**result, "writes_performed": True, "written_files": [path.as_posix() for path in written]}
    print(_json(result))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
