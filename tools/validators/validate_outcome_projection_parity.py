#!/usr/bin/env python3
"""Validate fixture-only cross-layer outcome projection parity candidates."""
from __future__ import annotations

import argparse
import copy
import hmac
import json
import math
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[2]
HASHING_SRC = REPO_ROOT / "packages/hashing/src"
sys.path.insert(0, str(HASHING_SRC))

from hashing import compute_spec_hash

SCHEMA = (
    REPO_ROOT
    / "schemas/contracts/v1/common/outcome_projection_parity.schema.json"
)
FIXTURES = (
    REPO_ROOT
    / "fixtures/contracts/v1/common/outcome_projection_parity/cases.json"
)
LAYER_ORDER = ("POLICY", "RELEASE", "RUNTIME", "API", "UI", "EXPORT", "CACHE")
SAFE_OUTCOME_PAIRS = (
    "ABSTAIN->ABSTAIN",
    "ABSTAIN->DENY",
    "ABSTAIN->ERROR",
    "ANSWER->ABSTAIN",
    "ANSWER->ANSWER",
    "ANSWER->DENY",
    "ANSWER->ERROR",
    "DENY->DENY",
    "ERROR->ERROR",
)
SAFE_VISIBILITY_PAIRS = (
    "FULL->FULL",
    "FULL->REDACTED",
    "FULL->STALE",
    "FULL->UNAVAILABLE",
    "REDACTED->REDACTED",
    "REDACTED->STALE",
    "REDACTED->UNAVAILABLE",
    "STALE->STALE",
    "STALE->UNAVAILABLE",
    "UNAVAILABLE->UNAVAILABLE",
)
MAX_JSON_BYTES = 1024 * 1024


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


class InputSymlinkError(ValueError):
    pass


class InputTooLargeError(ValueError):
    pass


@dataclass(frozen=True)
class Finding:
    code: str
    path: str
    step_index: int | None = None


@dataclass(frozen=True)
class ValidationResult:
    status: str
    parity_status: str | None
    findings: tuple[Finding, ...]


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError(key)
        value[key] = item
    return value


def _reject_constant(_value: str) -> None:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _json_pointer(parts: Iterable[object]) -> str:
    encoded = [
        str(part).replace("~", "~0").replace("/", "~1") for part in parts
    ]
    return "/" + "/".join(encoded) if encoded else "/"


def _hash_subject(document: Mapping[str, Any]) -> dict[str, Any]:
    subject = copy.deepcopy(dict(document))
    subject.pop("assessment_id", None)
    subject.pop("spec_hash", None)
    return subject


def expected_spec_hash(document: Mapping[str, Any]) -> str:
    return compute_spec_hash(_hash_subject(document))


def expected_assessment_id(spec_hash: str) -> str:
    digest = spec_hash.removeprefix("sha256:")
    return f"kfm:outcome-projection-parity:{digest[:24]}"


def _schema_validator() -> Draft202012Validator:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    return Draft202012Validator(schema, format_checker=FormatChecker())


def _is_canonical(values: Sequence[str]) -> bool:
    return list(values) == sorted(set(values))


def _profile_is_exact(document: Mapping[str, Any]) -> bool:
    profile = document["projection_profile"]
    return (
        tuple(profile["layer_order"]) == LAYER_ORDER
        and tuple(profile["allowed_outcome_pairs"]) == SAFE_OUTCOME_PAIRS
        and tuple(profile["allowed_visibility_pairs"]) == SAFE_VISIBILITY_PAIRS
    )


def _finding(code: str, path: str, step_index: int | None = None) -> Finding:
    return Finding(code, path, step_index)


def analyze_steps(document: Mapping[str, Any]) -> tuple[Finding, ...]:
    findings: list[Finding] = []
    steps = document["steps"]
    expected_indexes = list(range(1, len(LAYER_ORDER)))
    if [step["step_index"] for step in steps] != expected_indexes:
        findings.append(
            _finding("OUTCOME_PARITY_STEP_ORDER_INVALID", "/steps")
        )

    prior_state = document["initial_state"]
    for offset, step in enumerate(steps):
        index = step["step_index"]
        input_state = step["input_state"]
        output_state = step["output_state"]
        expected_input_layer = LAYER_ORDER[offset]
        expected_output_layer = LAYER_ORDER[offset + 1]
        expected_transition = f"{expected_input_layer}->{expected_output_layer}"
        step_path = f"/steps/{offset}"

        if (
            input_state["layer"] != expected_input_layer
            or output_state["layer"] != expected_output_layer
            or step["transition_id"] != expected_transition
        ):
            findings.append(
                _finding(
                    "OUTCOME_PARITY_LAYER_ORDER_INVALID",
                    step_path,
                    index,
                )
            )
        if input_state != prior_state:
            findings.append(
                _finding(
                    "OUTCOME_PARITY_STEP_CONTINUITY_INVALID",
                    f"{step_path}/input_state",
                    index,
                )
            )

        outcome_pair = (
            f"{input_state['semantic_outcome']}->"
            f"{output_state['semantic_outcome']}"
        )
        if outcome_pair not in SAFE_OUTCOME_PAIRS:
            findings.append(
                _finding(
                    "OUTCOME_PARITY_PROHIBITED_UPGRADE",
                    f"{step_path}/output_state/semantic_outcome",
                    index,
                )
            )

        visibility_pair = (
            f"{input_state['visibility']}->{output_state['visibility']}"
        )
        if visibility_pair not in SAFE_VISIBILITY_PAIRS:
            findings.append(
                _finding(
                    "OUTCOME_PARITY_VISIBILITY_UPGRADE",
                    f"{step_path}/output_state/visibility",
                    index,
                )
            )

        for state_name, state in (
            ("input_state", input_state),
            ("output_state", output_state),
        ):
            if not _is_canonical(state["reason_codes"]):
                findings.append(
                    _finding(
                        "OUTCOME_PARITY_REASON_ORDER_INVALID",
                        f"{step_path}/{state_name}/reason_codes",
                        index,
                    )
                )
            if not _is_canonical(state["support_refs"]):
                findings.append(
                    _finding(
                        "OUTCOME_PARITY_SUPPORT_ORDER_INVALID",
                        f"{step_path}/{state_name}/support_refs",
                        index,
                    )
                )

        mappings = step["reason_mappings"]
        mapped_inputs = [item["input_code"] for item in mappings]
        mapping_outputs = [item["output_code"] for item in mappings]
        mapping_shape_valid = (
            sorted(mapped_inputs) == sorted(input_state["reason_codes"])
            and len(mapped_inputs) == len(set(mapped_inputs))
            and all(
                item["mapping"] != "PRESERVED"
                or item["input_code"] == item["output_code"]
                for item in mappings
            )
        )
        if not mapping_shape_valid:
            findings.append(
                _finding(
                    "OUTCOME_PARITY_REASON_MAPPING_INVALID",
                    f"{step_path}/reason_mappings",
                    index,
                )
            )
        expected_output_reasons = sorted(
            set(mapping_outputs) | set(step["added_reason_codes"])
        )
        if output_state["reason_codes"] != expected_output_reasons:
            findings.append(
                _finding(
                    "OUTCOME_PARITY_REASON_LINEAGE_LOST",
                    f"{step_path}/output_state/reason_codes",
                    index,
                )
            )

        if not set(input_state["support_refs"]).issubset(
            set(output_state["support_refs"])
        ):
            findings.append(
                _finding(
                    "OUTCOME_PARITY_SUPPORT_LINEAGE_LOST",
                    f"{step_path}/output_state/support_refs",
                    index,
                )
            )
        if (
            output_state["semantic_outcome"] == "ANSWER"
            and not output_state["support_refs"]
        ):
            findings.append(
                _finding(
                    "OUTCOME_PARITY_EMPTY_SUCCESS",
                    f"{step_path}/output_state/support_refs",
                    index,
                )
            )
        if (
            output_state["semantic_outcome"] == "ANSWER"
            and output_state["visibility"] in {"STALE", "UNAVAILABLE"}
        ):
            findings.append(
                _finding(
                    "OUTCOME_PARITY_STALE_OR_UNAVAILABLE_SUCCESS",
                    f"{step_path}/output_state",
                    index,
                )
            )

        degraded = (
            input_state["semantic_outcome"] != output_state["semantic_outcome"]
            or input_state["visibility"] != output_state["visibility"]
        )
        if degraded and (
            step["degradation_rule_ref"] is None
            or not step["added_reason_codes"]
        ):
            findings.append(
                _finding(
                    "OUTCOME_PARITY_DEGRADATION_UNBOUND",
                    step_path,
                    index,
                )
            )

        prior_state = output_state

    unique = {
        (item.code, item.path, item.step_index): item for item in findings
    }
    return tuple(
        sorted(
            unique.values(),
            key=lambda item: (
                item.step_index if item.step_index is not None else 0,
                item.code,
                item.path,
            ),
        )
    )


def expected_report(document: Mapping[str, Any]) -> dict[str, Any]:
    findings = analyze_steps(document)
    terminal = document["steps"][-1]["output_state"]
    degraded = any(
        step["input_state"]["semantic_outcome"]
        != step["output_state"]["semantic_outcome"]
        or step["input_state"]["visibility"]
        != step["output_state"]["visibility"]
        for step in document["steps"]
    )
    if findings:
        parity_status = "PARITY_FAILURE"
    elif degraded:
        parity_status = "AUTHORIZED_DEGRADATION"
    else:
        parity_status = "PARITY_CONFIRMED"
    return {
        "terminal_layer": terminal["layer"],
        "terminal_outcome": terminal["semantic_outcome"],
        "terminal_visibility": terminal["visibility"],
        "parity_status": parity_status,
        "failing_step_indexes": sorted(
            {
                item.step_index
                for item in findings
                if item.step_index is not None
            }
        ),
        "finding_codes": sorted({item.code for item in findings}),
        "trusted_surface_allowed": False,
        "separate_policy_review_required": True,
    }


def validate_payload(document: Mapping[str, Any]) -> ValidationResult:
    errors = sorted(
        _schema_validator().iter_errors(document),
        key=lambda error: (
            _json_pointer(error.absolute_path),
            str(error.validator),
        ),
    )
    if errors:
        return ValidationResult(
            "DENY",
            None,
            (
                _finding(
                    "OUTCOME_PARITY_SCHEMA_INVALID",
                    _json_pointer(errors[0].absolute_path),
                ),
            ),
        )

    if not _profile_is_exact(document):
        return ValidationResult(
            "DENY",
            None,
            (
                _finding(
                    "OUTCOME_PARITY_PROFILE_MATRIX_INVALID",
                    "/projection_profile",
                ),
            ),
        )
    if not _is_canonical(document["initial_state"]["reason_codes"]):
        return ValidationResult(
            "DENY",
            None,
            (
                _finding(
                    "OUTCOME_PARITY_REASON_ORDER_INVALID",
                    "/initial_state/reason_codes",
                ),
            ),
        )
    if not _is_canonical(document["initial_state"]["support_refs"]):
        return ValidationResult(
            "DENY",
            None,
            (
                _finding(
                    "OUTCOME_PARITY_SUPPORT_ORDER_INVALID",
                    "/initial_state/support_refs",
                ),
            ),
        )

    expected = expected_report(document)
    if document["report"] != expected:
        return ValidationResult(
            "DENY",
            None,
            (
                _finding(
                    "OUTCOME_PARITY_REPORT_MISMATCH",
                    "/report",
                ),
            ),
        )

    semantic_findings = analyze_steps(document)
    if semantic_findings:
        return ValidationResult(
            "DENY",
            expected["parity_status"],
            semantic_findings,
        )

    actual_hash = expected_spec_hash(document)
    if not hmac.compare_digest(document["spec_hash"], actual_hash):
        return ValidationResult(
            "DENY",
            None,
            (
                _finding(
                    "OUTCOME_PARITY_SPEC_HASH_MISMATCH",
                    "/spec_hash",
                ),
            ),
        )
    actual_id = expected_assessment_id(actual_hash)
    if not hmac.compare_digest(document["assessment_id"], actual_id):
        return ValidationResult(
            "DENY",
            None,
            (
                _finding(
                    "OUTCOME_PARITY_ID_MISMATCH",
                    "/assessment_id",
                ),
            ),
        )
    return ValidationResult("PASS", expected["parity_status"], ())


def _set_pointer(document: dict[str, Any], pointer: str, value: Any) -> None:
    if not pointer.startswith("/"):
        raise ValueError("fixture mutation path must be an absolute JSON pointer")
    parts = [
        part.replace("~1", "/").replace("~0", "~")
        for part in pointer[1:].split("/")
    ]
    cursor: Any = document
    for part in parts[:-1]:
        cursor = cursor[int(part)] if isinstance(cursor, list) else cursor[part]
    final = parts[-1]
    if isinstance(cursor, list):
        cursor[int(final)] = value
    else:
        cursor[final] = value


def _rewrite_chain(document: dict[str, Any], outcome: str) -> None:
    support_refs = list(document["initial_state"]["support_refs"])

    def state(layer: str) -> dict[str, Any]:
        return {
            "layer": layer,
            "native_outcome": f"{layer}_{outcome}",
            "semantic_outcome": outcome,
            "visibility": "FULL",
            "reason_codes": [f"{layer}_{outcome}"],
            "support_refs": support_refs,
        }

    document["initial_state"] = state(LAYER_ORDER[0])
    steps: list[dict[str, Any]] = []
    prior = document["initial_state"]
    for offset, output_layer in enumerate(LAYER_ORDER[1:]):
        output = state(output_layer)
        steps.append(
            {
                "step_index": offset + 1,
                "transition_id": f"{prior['layer']}->{output_layer}",
                "input_state": copy.deepcopy(prior),
                "output_state": output,
                "reason_mappings": [
                    {
                        "input_code": prior["reason_codes"][0],
                        "output_code": output["reason_codes"][0],
                        "mapping": "TRANSLATED",
                    }
                ],
                "added_reason_codes": [],
                "omitted_fields": [],
                "degradation_rule_ref": None,
            }
        )
        prior = output
    document["steps"] = steps


def load_fixtures() -> dict[str, Any]:
    value = json.loads(FIXTURES.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("fixture manifest root must be an object")
    return value


def materialize_case(
    manifest: Mapping[str, Any], case: Mapping[str, Any]
) -> dict[str, Any]:
    document = copy.deepcopy(manifest["base"])
    if "chain_outcome" in case:
        _rewrite_chain(document, case["chain_outcome"])
    for mutation in case.get("mutations", []):
        _set_pointer(document, mutation["path"], mutation["value"])
    if case.get("recompute_report") or "chain_outcome" in case:
        document["report"] = expected_report(document)
    document["spec_hash"] = expected_spec_hash(document)
    document["assessment_id"] = expected_assessment_id(document["spec_hash"])
    if "spec_hash_override" in case:
        document["spec_hash"] = case["spec_hash_override"]
    if "assessment_id_override" in case:
        document["assessment_id"] = case["assessment_id_override"]
    return document


def _load_document(path: Path) -> Mapping[str, Any]:
    if path.is_symlink():
        raise InputSymlinkError
    if not path.is_file():
        raise OSError
    if path.stat().st_size > MAX_JSON_BYTES:
        raise InputTooLargeError
    with path.open("r", encoding="utf-8") as stream:
        value = json.load(
            stream,
            object_pairs_hook=_unique_object,
            parse_constant=_reject_constant,
            parse_float=_finite_float,
        )
    if not isinstance(value, dict):
        raise ValueError("candidate root must be an object")
    return value


def _run_fixtures() -> int:
    manifest = load_fixtures()
    failures: list[dict[str, Any]] = []
    for case in manifest["cases"]:
        result = validate_payload(materialize_case(manifest, case))
        actual_findings = [
            {"code": item.code, "path": item.path}
            for item in result.findings
        ]
        if (
            result.status != case["expected_status"]
            or result.parity_status != case["expected_parity_status"]
            or actual_findings != case["expected_findings"]
        ):
            failures.append(
                {
                    "case_id": case["case_id"],
                    "expected_status": case["expected_status"],
                    "actual_status": result.status,
                    "expected_parity_status": case[
                        "expected_parity_status"
                    ],
                    "actual_parity_status": result.parity_status,
                    "expected_findings": case["expected_findings"],
                    "actual_findings": actual_findings,
                }
            )
    print(
        json.dumps(
            {
                "cases": len(manifest["cases"]),
                "failures": failures,
                "suite_match": not failures,
            },
            sort_keys=True,
            separators=(",", ":"),
        )
    )
    return 0 if not failures else 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.fixtures:
        return _run_fixtures()
    if args.path is None:
        raise SystemExit("path is required unless --fixtures is used")
    try:
        result = validate_payload(_load_document(args.path))
    except DuplicateKeyError:
        result = ValidationResult(
            "ERROR", None, (_finding("JSON_DUPLICATE_KEY", "/"),)
        )
    except NonFiniteNumberError:
        result = ValidationResult(
            "ERROR", None, (_finding("JSON_NONFINITE_NUMBER", "/"),)
        )
    except InputSymlinkError:
        result = ValidationResult(
            "ERROR", None, (_finding("JSON_INPUT_SYMLINK_DENIED", "/"),)
        )
    except InputTooLargeError:
        result = ValidationResult(
            "ERROR", None, (_finding("JSON_INPUT_TOO_LARGE", "/"),)
        )
    except (
        OSError,
        UnicodeError,
        json.JSONDecodeError,
        ValueError,
        RecursionError,
    ):
        result = ValidationResult(
            "ERROR", None, (_finding("JSON_INPUT_INVALID", "/"),)
        )
    print(
        json.dumps(
            {
                "status": result.status,
                "parity_status": result.parity_status,
                "findings": [
                    {"code": item.code, "path": item.path}
                    for item in result.findings
                ],
            },
            sort_keys=True,
            separators=(",", ":"),
        )
    )
    return 0 if result.status == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
