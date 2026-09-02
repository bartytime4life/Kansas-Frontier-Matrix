#!/usr/bin/env python3
"""Validate the deterministic MRTS-06 CI conformance inspection report.

The report is process evidence only.  Validation checks schema shape, finite
outcomes, exact local/base-tree digests, canonical serialization, closure
preconditions, and the no-self-authority boundary without using the network.
A green validator result does not approve review, merge, release, deployment,
promotion, publication, a public route, issue closure, or milestone closure.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators._common.local_resolver import build_registry

REPORT_PATH = (
    REPO_ROOT
    / "artifacts/qa/validation/milestone-1/ci_conformance_report.json"
)
SCHEMA_PATH = (
    REPO_ROOT
    / "schemas/contracts/v1/governance/ci_conformance_report.schema.json"
)
CASES_PATH = (
    REPO_ROOT
    / "fixtures/contracts/v1/governance/ci_conformance_report/cases.json"
)
MAX_JSON_BYTES = 4 * 1024 * 1024
MAX_GIT_BLOB_BYTES = 16 * 1024 * 1024
SUBPROCESS_TIMEOUT_SECONDS = 30
REF_SECTIONS = (
    "authority_refs",
    "registries",
    "schemas",
    "policies",
    "validators",
    "generated_artifacts",
)


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str
    detail: str


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


def _pairs(items: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in items:
        if key in result:
            raise DuplicateKeyError
        result[key] = value
    return result


def _nonfinite(_value: str) -> object:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _read_json(path: Path) -> tuple[dict[str, Any] | None, list[Finding], bytes | None]:
    try:
        if path.is_symlink() or not path.is_file():
            return None, [Finding("INPUT_NOT_REGULAR", "/", "regular file required")], None
        raw = path.read_bytes()
        if len(raw) > MAX_JSON_BYTES:
            return None, [Finding("INPUT_TOO_LARGE", "/", "input exceeds 4 MiB")], None
        value = json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=_pairs,
            parse_constant=_nonfinite,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/", "duplicate key denied")], None
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE", "/", "finite JSON required")], None
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError, ValueError):
        return None, [Finding("JSON_INVALID", "/", "safe JSON object required")], None
    if not isinstance(value, dict):
        return None, [Finding("JSON_ROOT_INVALID", "/", "object root required")], raw
    return value, [], raw


def canonical_bytes(value: Mapping[str, Any]) -> bytes:
    return (
        json.dumps(
            value,
            ensure_ascii=False,
            allow_nan=False,
            indent=2,
            sort_keys=True,
        )
        + "\n"
    ).encode("utf-8")


def report_digest(value: Mapping[str, Any]) -> str:
    payload = copy.deepcopy(dict(value))
    payload.pop("report_digest", None)
    payload.pop("sha256", None)
    raw = json.dumps(
        payload,
        ensure_ascii=False,
        allow_nan=False,
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def _sha256(raw: bytes) -> str:
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def _pointer(parts: Iterable[object]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _schema_findings(value: Mapping[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(
            schema,
            registry=build_registry(REPO_ROOT),
            format_checker=FormatChecker(),
        )
        errors = sorted(
            validator.iter_errors(value),
            key=lambda item: (_pointer(item.absolute_path), str(item.validator)),
        )
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/", "schema evaluation unavailable")]
    return [
        Finding("SCHEMA_MISMATCH", _pointer(item.absolute_path), "schema constraint failed")
        for item in errors[:100]
    ]


def _canonical_repo_path(value: object) -> Path | None:
    if not isinstance(value, str) or not value or value.startswith("/") or "\\" in value:
        return None
    pure = PurePosixPath(value)
    if str(pure) != value or any(part in {"", ".", ".."} for part in pure.parts):
        return None
    candidate = REPO_ROOT.joinpath(*pure.parts)
    current = REPO_ROOT
    try:
        for part in pure.parts:
            current /= part
            if current.is_symlink():
                return None
        candidate.resolve(strict=True).relative_to(REPO_ROOT.resolve(strict=True))
    except (OSError, ValueError):
        return None
    return candidate if candidate.is_file() else None


def _git_blob(ref: str, path: str) -> bytes | None:
    try:
        result = subprocess.run(
            ["git", "cat-file", "blob", f"{ref}:{path}"],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            timeout=SUBPROCESS_TIMEOUT_SECONDS,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None
    if result.returncode != 0 or len(result.stdout) > MAX_GIT_BLOB_BYTES:
        return None
    return result.stdout


def _git_commit_exists(ref: object) -> bool:
    if not isinstance(ref, str):
        return False
    try:
        result = subprocess.run(
            ["git", "cat-file", "-e", f"{ref}^{{commit}}"],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            timeout=SUBPROCESS_TIMEOUT_SECONDS,
        )
    except (OSError, subprocess.TimeoutExpired):
        return False
    return result.returncode == 0


def _id_order_findings(value: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    paths: list[tuple[str, object]] = [(name, value.get(name)) for name in REF_SECTIONS]
    paths.extend(
        [
            ("checks", value.get("checks")),
            ("unresolved_items", value.get("unresolved_items")),
        ]
    )
    failures = value.get("failures")
    if isinstance(failures, dict):
        paths.extend(
            [
                ("failures/inherited", failures.get("inherited")),
                ("failures/introduced", failures.get("introduced")),
            ]
        )
    closure = value.get("closure")
    if isinstance(closure, dict):
        paths.append(("closure/exit_criteria", closure.get("exit_criteria")))

    for name, items in paths:
        if not isinstance(items, list):
            continue
        key = "code" if name.startswith("failures/") else "id"
        ids = [item.get(key) for item in items if isinstance(item, dict)]
        if len(ids) != len(set(ids)):
            findings.append(Finding("IDS_NOT_UNIQUE", f"/{name}", "identifiers must be unique"))
        if ids != sorted(ids):
            findings.append(Finding("IDS_NOT_SORTED", f"/{name}", "identifiers must be sorted"))
    return findings


def _ref_findings(value: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    repository = value.get("repository")
    base_sha = repository.get("base_sha") if isinstance(repository, dict) else None
    if not _git_commit_exists(base_sha):
        findings.append(Finding("BASE_SHA_UNRESOLVED", "/repository/base_sha", "base commit unavailable"))

    refs: list[tuple[str, int, Mapping[str, Any]]] = []
    for section in REF_SECTIONS:
        entries = value.get(section)
        if isinstance(entries, list):
            refs.extend(
                (section, index, item)
                for index, item in enumerate(entries)
                if isinstance(item, dict)
            )
    fixture = value.get("fixture")
    if isinstance(fixture, dict):
        refs.append(("fixture", 0, fixture))

    seen_paths: set[tuple[str, str]] = set()
    for section, index, item in refs:
        path = item.get("path")
        scope = item.get("scope")
        field = f"/{section}/{index}" if section != "fixture" else "/fixture"
        if not isinstance(path, str) or not isinstance(scope, str):
            continue
        identity = (scope, path)
        if identity in seen_paths:
            findings.append(Finding("REF_PATH_DUPLICATE", field, "scoped path must be unique"))
        seen_paths.add(identity)
        if path == "artifacts/qa/validation/milestone-1/ci_conformance_report.json":
            findings.append(Finding("SELF_REFERENCE_DENIED", field, "report cannot hash itself as a ref"))
            continue
        if scope == "BASE_TREE":
            raw = _git_blob(str(base_sha), path) if isinstance(base_sha, str) else None
        elif scope == "CANDIDATE_TREE":
            candidate = _canonical_repo_path(path)
            raw = candidate.read_bytes() if candidate is not None else None
        else:
            continue
        if raw is None:
            findings.append(Finding("REF_UNAVAILABLE", field, "referenced bytes unavailable"))
        elif _sha256(raw) != item.get("sha256"):
            findings.append(Finding("REF_DIGEST_MISMATCH", field, "referenced digest mismatch"))
    return findings


def _check_findings(value: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    checks = value.get("checks")
    if not isinstance(checks, list):
        return findings
    allowed = {
        "EXECUTED_LOCAL": {"PASS", "FAIL", "HOLD_INHERITED"},
        "EXECUTED_HOSTED": {"PASS", "FAIL", "HOLD_INHERITED"},
        "CHECK_NOT_RUN": {"CHECK_NOT_RUN"},
        "SKIPPED": {"SKIPPED"},
    }
    for index, check in enumerate(checks):
        if not isinstance(check, dict):
            continue
        state = check.get("execution_state")
        outcome = check.get("outcome")
        command = check.get("command")
        if state in allowed and outcome not in allowed[state]:
            findings.append(
                Finding(
                    "CHECK_OUTCOME_INVALID",
                    f"/checks/{index}/outcome",
                    "outcome cannot exceed execution state",
                )
            )
        if state in {"EXECUTED_LOCAL", "EXECUTED_HOSTED"} and not isinstance(command, str):
            findings.append(
                Finding("CHECK_COMMAND_MISSING", f"/checks/{index}/command", "executed check needs command")
            )
        if state in {"CHECK_NOT_RUN", "SKIPPED"} and command is not None:
            findings.append(
                Finding("CHECK_COMMAND_UNEXECUTED", f"/checks/{index}/command", "unexecuted check command must be null")
            )
    return findings


def _closure_findings(value: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    closure = value.get("closure")
    repository = value.get("repository")
    unresolved = value.get("unresolved_items")
    checks = value.get("checks")
    milestone = value.get("milestone")
    if not isinstance(closure, dict):
        return findings

    blocking = (
        sum(1 for item in unresolved if isinstance(item, dict) and item.get("blocking") is True)
        if isinstance(unresolved, list)
        else 0
    )
    if closure.get("unresolved_count") != blocking:
        findings.append(
            Finding("UNRESOLVED_COUNT_MISMATCH", "/closure/unresolved_count", "blocking count mismatch")
        )

    state = closure.get("state")
    final_sha = repository.get("final_sha") if isinstance(repository, dict) else None
    target_sha = closure.get("target_sha")
    if final_sha != target_sha:
        findings.append(Finding("CLOSURE_SHA_MISMATCH", "/closure/target_sha", "closure and repository SHA differ"))

    if state == "BLOCKED":
        if closure.get("closer") is not None or closure.get("closed_at") is not None:
            findings.append(Finding("BLOCKED_CLOSURE_METADATA", "/closure", "blocked closure cannot name closer or time"))
        return findings

    if not isinstance(target_sha, str):
        findings.append(Finding("CLOSURE_FINAL_SHA_MISSING", "/closure/target_sha", "exact final SHA required"))
    criteria = closure.get("exit_criteria")
    if not isinstance(criteria, list) or any(
        not isinstance(item, dict) or item.get("satisfied") is not True for item in criteria
    ):
        findings.append(Finding("CLOSURE_CRITERIA_INCOMPLETE", "/closure/exit_criteria", "all criteria must be true"))
    runs = closure.get("hosted_runs")
    if not isinstance(runs, list) or not runs or any(
        not isinstance(run, dict)
        or run.get("conclusion") != "SUCCESS"
        or run.get("head_sha") != target_sha
        for run in runs
    ):
        findings.append(Finding("CLOSURE_HOSTED_EVIDENCE_MISSING", "/closure/hosted_runs", "exact-head hosted success required"))
    review = closure.get("human_review")
    if (
        not isinstance(review, dict)
        or review.get("state") != "APPROVED"
        or not review.get("reviewer_ids")
        or review.get("timestamp") is None
    ):
        findings.append(Finding("CLOSURE_REVIEW_MISSING", "/closure/human_review", "approved review evidence required"))
    if blocking or closure.get("unresolved_count") != 0:
        findings.append(Finding("CLOSURE_UNRESOLVED", "/unresolved_items", "blocking items must be zero"))
    if isinstance(checks, list) and any(
        isinstance(check, dict)
        and check.get("required_for_closure") is True
        and check.get("outcome") != "PASS"
        for check in checks
    ):
        findings.append(Finding("CLOSURE_REQUIRED_CHECKS", "/checks", "all required checks must pass"))
    if state == "READY" and (closure.get("closer") is not None or closure.get("closed_at") is not None):
        findings.append(Finding("READY_CLOSURE_METADATA", "/closure", "ready record is not closed"))
    if state == "CLOSED":
        if closure.get("closer") is None or closure.get("closed_at") is None:
            findings.append(Finding("CLOSED_METADATA_MISSING", "/closure", "closed record needs closer and time"))
        if not isinstance(milestone, dict) or milestone.get("state") != "CLOSED":
            findings.append(Finding("MILESTONE_STATE_MISMATCH", "/milestone/state", "closed record needs closed milestone"))
    return findings


def _status_finding(value: Mapping[str, Any]) -> list[Finding]:
    checks = value.get("checks")
    failures = value.get("failures")
    unresolved = value.get("unresolved_items")
    closure = value.get("closure")
    check_values = [item for item in checks if isinstance(item, dict)] if isinstance(checks, list) else []
    introduced = failures.get("introduced") if isinstance(failures, dict) else []
    has_introduced = isinstance(introduced, list) and any(
        isinstance(item, dict) and item.get("count", 0) > 0 for item in introduced
    )
    if has_introduced or any(item.get("outcome") == "FAIL" for item in check_values):
        expected = "NONCONFORMANT"
    elif (
        any(item.get("required_for_closure") is True and item.get("outcome") != "PASS" for item in check_values)
        or (isinstance(unresolved, list) and any(isinstance(item, dict) and item.get("blocking") is True for item in unresolved))
        or not isinstance(closure, dict)
        or closure.get("state") == "BLOCKED"
    ):
        expected = "BLOCKED"
    else:
        expected = "CONFORMANT"
    return (
        [Finding("STATUS_MISMATCH", "/status", "status does not match bounded evidence")]
        if value.get("status") != expected
        else []
    )


def _authority_findings(value: Mapping[str, Any]) -> list[Finding]:
    controls = value.get("controls")
    if not isinstance(controls, dict):
        return []
    return [
        Finding("AUTHORITY_EFFECT_DENIED", f"/controls/{name}", "report cannot create authority")
        for name, enabled in controls.items()
        if enabled is not False
    ]


def validate_report(
    value: Mapping[str, Any],
    *,
    raw: bytes | None = None,
    check_canonical: bool = True,
) -> tuple[Finding, ...]:
    findings: list[Finding] = []
    findings.extend(_schema_findings(value))
    findings.extend(_id_order_findings(value))
    findings.extend(_ref_findings(value))
    findings.extend(_check_findings(value))
    findings.extend(_closure_findings(value))
    findings.extend(_status_finding(value))
    findings.extend(_authority_findings(value))
    expected_digest = report_digest(value)
    if value.get("report_digest") != expected_digest:
        findings.append(Finding("REPORT_DIGEST_MISMATCH", "/report_digest", "report digest mismatch"))
    if value.get("sha256") != expected_digest:
        findings.append(Finding("PROVENANCE_DIGEST_MISMATCH", "/sha256", "provenance digest mismatch"))
    if check_canonical and raw is not None and raw != canonical_bytes(value):
        findings.append(Finding("SERIALIZATION_NOT_CANONICAL", "/", "canonical pretty JSON required"))
    return tuple(sorted(set(findings)))


def _resolve_pointer(value: Any, pointer: str) -> tuple[Any, str | int]:
    parts = pointer.lstrip("/").split("/") if pointer != "/" else []
    if not parts:
        raise ValueError("root mutation denied")
    current = value
    for raw in parts[:-1]:
        part = raw.replace("~1", "/").replace("~0", "~")
        current = current[int(part)] if isinstance(current, list) else current[part]
    last_raw = parts[-1].replace("~1", "/").replace("~0", "~")
    return current, int(last_raw) if isinstance(current, list) else last_raw


def apply_mutations(value: dict[str, Any], mutations: Sequence[Mapping[str, Any]]) -> None:
    for mutation in mutations:
        parent, key = _resolve_pointer(value, str(mutation.get("path")))
        op = mutation.get("op")
        if op == "set":
            parent[key] = copy.deepcopy(mutation.get("value"))
        elif op == "delete":
            del parent[key]
        elif op == "append":
            target = parent[key]
            if not isinstance(target, list):
                raise ValueError("append target must be list")
            target.append(copy.deepcopy(mutation.get("value")))
        else:
            raise ValueError("unknown mutation")


def validate_fixtures(base: Mapping[str, Any]) -> tuple[Finding, ...]:
    packet, read_findings, _raw = _read_json(CASES_PATH)
    if read_findings or packet is None:
        return tuple(read_findings or [Finding("FIXTURES_INVALID", "/", "case packet unavailable")])
    cases = packet.get("cases")
    if not isinstance(cases, list):
        return (Finding("FIXTURES_INVALID", "/cases", "cases array required"),)
    findings: list[Finding] = []
    for index, case in enumerate(cases):
        if not isinstance(case, dict):
            findings.append(Finding("FIXTURE_CASE_INVALID", f"/cases/{index}", "object required"))
            continue
        candidate = copy.deepcopy(dict(base))
        try:
            apply_mutations(candidate, case.get("mutations", []))
            if case.get("refresh_digest", True):
                digest = report_digest(candidate)
                candidate["report_digest"] = digest
                candidate["sha256"] = digest
        except (KeyError, IndexError, TypeError, ValueError):
            findings.append(Finding("FIXTURE_MUTATION_INVALID", f"/cases/{index}", "mutation failed"))
            continue
        actual = sorted({finding.code for finding in validate_report(candidate, check_canonical=False)})
        expected = case.get("expected_codes")
        if actual != expected:
            findings.append(Finding("FIXTURE_POLARITY_MISMATCH", f"/cases/{index}", "exact codes differ"))
    return tuple(sorted(findings))


def _emit_text(findings: Sequence[Finding], value: Mapping[str, Any] | None) -> None:
    if findings:
        print(f"CI_CONFORMANCE_REPORT validation=FAIL findings={len(findings)}")
        for finding in findings:
            print(f"{finding.code} {finding.field} {finding.detail}")
        return
    closure = value.get("closure") if isinstance(value, dict) else {}
    checks = value.get("checks") if isinstance(value, dict) else []
    unresolved = value.get("unresolved_items") if isinstance(value, dict) else []
    print(
        "CI_CONFORMANCE_REPORT validation=PASS "
        f"status={value.get('status')} closure={closure.get('state')} "
        f"checks={len(checks)} unresolved={len(unresolved)} authority=false"
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("report", nargs="?", type=Path, default=REPORT_PATH)
    parser.add_argument("--fixtures", action="store_true")
    parser.add_argument("--render", action="store_true", help="write canonical report bytes to stdout")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    args = parser.parse_args(argv)

    value, findings, raw = _read_json(args.report)
    if value is not None and not findings:
        findings = list(validate_report(value, raw=raw))
        if args.fixtures and not findings:
            findings.extend(validate_fixtures(value))

    if args.render and value is not None and not findings:
        sys.stdout.buffer.write(canonical_bytes(value))
        return 0
    if args.format == "json":
        print(
            json.dumps(
                {
                    "validation": "PASS" if not findings else "FAIL",
                    "status": value.get("status") if value else None,
                    "closure": value.get("closure", {}).get("state") if value else None,
                    "authority_created": False,
                    "findings": [finding.__dict__ for finding in sorted(findings)],
                },
                separators=(",", ":"),
                sort_keys=True,
            )
        )
    else:
        _emit_text(sorted(findings), value)
    return 0 if not findings else 1


if __name__ == "__main__":
    raise SystemExit(main())
