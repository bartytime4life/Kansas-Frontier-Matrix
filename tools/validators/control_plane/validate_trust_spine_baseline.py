#!/usr/bin/env python3
"""Validate the KFM trust-spine authority baseline without network access.

The baseline is an evidence projection. A PASS proves bounded shape, canonical
ordering, count reconciliation, repository-path containment, referenced-byte
digests, and execution-state consistency only. It does not create authority,
accept an ADR, waive drift, activate a source, approve review, or authorize a
release, deployment, promotion, or publication.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import subprocess
import sys
from dataclasses import dataclass
from itertools import islice
from pathlib import Path, PurePosixPath
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
BASELINE_PATH = REPO_ROOT / "control_plane/trust_spine_baseline.yaml"
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/governance/trust_spine_baseline.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/governance/trust_spine_baseline"
MAX_FILE_BYTES = 4 * 1024 * 1024
MAX_SCHEMA_FINDINGS = 100
MAX_REFERENCED_FILE_BYTES = 64 * 1024 * 1024
SCOPE = "pinned-authority-and-implementation-evidence-projection-only"
REQUIRED_NON_EFFECTS = frozenset(
    {
        "does_not_create_authority",
        "does_not_activate_sources",
        "does_not_expand_the_topology_drift_baseline",
        "does_not_release_deploy_promote_or_publish",
    }
)


class DuplicateKeyError(ValueError):
    """Raised when a JSON object repeats a key."""


class NonFiniteNumberError(ValueError):
    """Raised when JSON uses a non-standard non-finite number."""


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


@dataclass(frozen=True)
class ValidationResult:
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return not self.findings


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError
        result[key] = value
    return result


def _reject_nonfinite(_value: str) -> None:
    raise NonFiniteNumberError


def _parse_finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _read_object(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("FILE_NOT_FOUND", "/")]
        if path.stat().st_size > MAX_FILE_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        with path.open("r", encoding="utf-8") as stream:
            value = json.load(
                stream,
                object_pairs_hook=_unique_object,
                parse_constant=_reject_nonfinite,
                parse_float=_parse_finite_float,
            )
    except UnicodeDecodeError:
        return None, [Finding("JSON_NOT_UTF8", "/")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_COMPATIBLE_YAML_REQUIRED", "/")]
    except OSError:
        return None, [Finding("FILE_READ_ERROR", "/")]
    except (RecursionError, ValueError):
        return None, [Finding("JSON_COMPLEXITY_LIMIT", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def _pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _schema_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    schema, schema_read_findings = _read_object(SCHEMA_PATH)
    if schema is None:
        return [Finding("SCHEMA_UNAVAILABLE", finding.field) for finding in schema_read_findings]
    try:
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        errors = list(islice(validator.iter_errors(candidate), MAX_SCHEMA_FINDINGS + 1))
    except (RecursionError, ValueError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    truncated = len(errors) > MAX_SCHEMA_FINDINGS
    findings = [
        Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in sorted(
            errors[:MAX_SCHEMA_FINDINGS],
            key=lambda item: (_pointer(item.absolute_path), str(item.validator)),
        )
    ]
    if truncated:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def _array(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _mapping(value: Any) -> Mapping[str, Any]:
    return value if isinstance(value, dict) else {}


def _canonical_path(value: Any) -> PurePosixPath | None:
    if not isinstance(value, str) or not value or "\\" in value or value.startswith("/"):
        return None
    path = PurePosixPath(value)
    if str(path) != value or any(part in {"", ".", ".."} for part in path.parts):
        return None
    return path


def _check_sorted_unique(
    values: Sequence[Any],
    *,
    field: str,
    findings: list[Finding],
    code_prefix: str,
) -> None:
    try:
        sorted_values = sorted(values)
        unique_count = len(set(values))
    except TypeError:
        return
    if len(values) != unique_count:
        findings.append(Finding(f"{code_prefix}_DUPLICATE", field))
    if list(values) != sorted_values:
        findings.append(Finding(f"{code_prefix}_NOT_CANONICAL", field))


def _entry_ids(
    entries: Sequence[Any],
    *,
    key: str,
    field: str,
    findings: list[Finding],
    code_prefix: str,
) -> list[Any]:
    ids = [entry.get(key) for entry in entries if isinstance(entry, dict)]
    _check_sorted_unique(ids, field=field, findings=findings, code_prefix=code_prefix)
    return ids


def _resolve_path(
    relative_value: Any,
    *,
    repo_root: Path,
    field: str,
    expected_prefixes: tuple[str, ...],
    findings: list[Finding],
) -> Path | None:
    relative = _canonical_path(relative_value)
    if relative is None:
        findings.append(Finding("PATH_INVALID", field))
        return None
    if not any(str(relative).startswith(prefix) for prefix in expected_prefixes):
        findings.append(Finding("PATH_ROOT_MISMATCH", field))
        return None
    try:
        resolved_root = repo_root.resolve(strict=True)
        unresolved = resolved_root.joinpath(*relative.parts)
        if unresolved.is_symlink():
            findings.append(Finding("PATH_SYMLINK_DENIED", field))
            return None
        resolved = unresolved.resolve(strict=True)
        resolved.relative_to(resolved_root)
    except (OSError, ValueError):
        findings.append(Finding("PATH_NOT_FOUND", field))
        return None
    if not resolved.is_file():
        findings.append(Finding("PATH_NOT_FILE", field))
        return None
    return resolved


def _check_path_digest(
    entry: Mapping[str, Any],
    *,
    path_key: str,
    repo_root: Path,
    field: str,
    expected_prefixes: tuple[str, ...],
    findings: list[Finding],
) -> None:
    resolved = _resolve_path(
        entry.get(path_key),
        repo_root=repo_root,
        field=f"{field}/{path_key}",
        expected_prefixes=expected_prefixes,
        findings=findings,
    )
    digest = entry.get("sha256")
    if resolved is None or not isinstance(digest, str) or not digest.startswith("sha256:"):
        return
    try:
        if resolved.stat().st_size > MAX_REFERENCED_FILE_BYTES:
            findings.append(Finding("REFERENCED_FILE_TOO_LARGE", f"{field}/{path_key}"))
            return
        actual = "sha256:" + hashlib.sha256(resolved.read_bytes()).hexdigest()
    except OSError:
        findings.append(Finding("PATH_READ_ERROR", f"{field}/{path_key}"))
        return
    if actual != digest:
        findings.append(Finding("DIGEST_MISMATCH", f"{field}/sha256"))


def _semantic_findings(
    candidate: Mapping[str, Any],
    *,
    repo_root: Path,
    check_paths: bool,
    check_git: bool,
) -> list[Finding]:
    findings: list[Finding] = []

    authority = _mapping(candidate.get("authority_snapshot"))
    accepted = _array(authority.get("accepted_adrs"))
    candidates = _array(authority.get("unresolved_authority_candidates"))
    accepted_ids = _entry_ids(
        accepted,
        key="id",
        field="/authority_snapshot/accepted_adrs",
        findings=findings,
        code_prefix="ACCEPTED_ADRS",
    )
    candidate_ids = _entry_ids(
        candidates,
        key="id",
        field="/authority_snapshot/unresolved_authority_candidates",
        findings=findings,
        code_prefix="AUTHORITY_CANDIDATES",
    )
    if set(accepted_ids) & set(candidate_ids):
        findings.append(Finding("AUTHORITY_STATUS_OVERLAP", "/authority_snapshot"))
    if authority.get("accepted_adr_count") != len(accepted):
        findings.append(Finding("ACCEPTED_ADR_COUNT_MISMATCH", "/authority_snapshot/accepted_adr_count"))
    relevant_count = sum(
        1 for entry in accepted if isinstance(entry, dict) and entry.get("relevant_to_milestone") is True
    )
    if authority.get("accepted_relevant_adr_count") != relevant_count:
        findings.append(
            Finding(
                "RELEVANT_ADR_COUNT_MISMATCH",
                "/authority_snapshot/accepted_relevant_adr_count",
            )
        )
    directory_rules = _mapping(authority.get("directory_rules"))
    decision_ref = directory_rules.get("decision_ref")
    relevant_ids = {
        entry.get("id")
        for entry in accepted
        if isinstance(entry, dict) and entry.get("relevant_to_milestone") is True
    }
    if decision_ref not in relevant_ids:
        findings.append(
            Finding(
                "DIRECTORY_DECISION_NOT_ACCEPTED_RELEVANT",
                "/authority_snapshot/directory_rules/decision_ref",
            )
        )

    roots = _mapping(candidate.get("repository_roots"))
    classes = _mapping(roots.get("classes"))
    if all(isinstance(value, int) and not isinstance(value, bool) for value in classes.values()):
        if roots.get("declared_count") != sum(classes.values()):
            findings.append(Finding("ROOT_CLASS_COUNT_MISMATCH", "/repository_roots/classes"))
    declared_count = roots.get("declared_count")
    present_count = roots.get("observed_present_count")
    if isinstance(declared_count, int) and isinstance(present_count, int) and present_count > declared_count:
        findings.append(Finding("ROOT_PRESENT_COUNT_EXCEEDS_DECLARED", "/repository_roots/observed_present_count"))
    root_unresolved = _array(roots.get("unresolved_items"))
    _check_sorted_unique(
        root_unresolved,
        field="/repository_roots/unresolved_items",
        findings=findings,
        code_prefix="ROOT_UNRESOLVED_ITEMS",
    )

    projections = _array(candidate.get("control_plane_projections"))
    _entry_ids(
        projections,
        key="id",
        field="/control_plane_projections",
        findings=findings,
        code_prefix="PROJECTION_IDS",
    )
    projection_by_id = {
        entry.get("id"): entry for entry in projections if isinstance(entry, dict)
    }

    catalog = _mapping(candidate.get("trust_object_catalog"))
    registered = _array(catalog.get("registered_required_families"))
    unregistered = _array(catalog.get("unregistered_required_families"))
    other = _array(catalog.get("other_registered_families"))
    for field_name, values in (
        ("registered_required_families", registered),
        ("unregistered_required_families", unregistered),
        ("other_registered_families", other),
    ):
        _check_sorted_unique(
            values,
            field=f"/trust_object_catalog/{field_name}",
            findings=findings,
            code_prefix="TRUST_OBJECT_FAMILIES",
        )
    if (
        set(registered) & set(unregistered)
        or set(registered) & set(other)
        or set(unregistered) & set(other)
    ):
        findings.append(Finding("TRUST_OBJECT_FAMILY_OVERLAP", "/trust_object_catalog"))
    if catalog.get("required_family_count") != len(registered) + len(unregistered):
        findings.append(Finding("REQUIRED_FAMILY_COUNT_MISMATCH", "/trust_object_catalog/required_family_count"))
    if catalog.get("registered_required_count") != len(registered):
        findings.append(
            Finding(
                "REGISTERED_REQUIRED_COUNT_MISMATCH",
                "/trust_object_catalog/registered_required_count",
            )
        )
    if catalog.get("other_registered_count") != len(other):
        findings.append(Finding("OTHER_REGISTERED_COUNT_MISMATCH", "/trust_object_catalog/other_registered_count"))
    object_projection = projection_by_id.get("object_family_register")
    if isinstance(object_projection, dict):
        if (
            object_projection.get("path") != catalog.get("registry_path")
            or object_projection.get("sha256") != catalog.get("sha256")
        ):
            findings.append(Finding("OBJECT_FAMILY_PROJECTION_MISMATCH", "/trust_object_catalog"))
    root_projection = projection_by_id.get("root_registry")
    if isinstance(root_projection, dict):
        if (
            root_projection.get("path") != roots.get("registry_path")
            or root_projection.get("sha256") != roots.get("sha256")
        ):
            findings.append(Finding("ROOT_PROJECTION_MISMATCH", "/repository_roots"))

    observations = _array(candidate.get("validation_observations"))
    _entry_ids(
        observations,
        key="id",
        field="/validation_observations",
        findings=findings,
        code_prefix="VALIDATION_IDS",
    )
    for index, raw_observation in enumerate(observations):
        if not isinstance(raw_observation, dict):
            continue
        field = f"/validation_observations/{index}"
        run_state = raw_observation.get("run_state")
        outcome = raw_observation.get("outcome")
        if run_state != "EXECUTED" and outcome in {"PASS", "FAIL"}:
            findings.append(Finding("RUN_STATE_OUTCOME_MISMATCH", f"{field}/outcome"))
        if run_state == "EXECUTED" and outcome in {"NOT_RUN", "SKIPPED"}:
            findings.append(Finding("RUN_STATE_OUTCOME_MISMATCH", f"{field}/outcome"))
        counts = _mapping(raw_observation.get("finding_counts"))
        if counts:
            drift_failures = sum(
                value
                for key, value in counts.items()
                if key in {"fail_invariant", "fail_new_drift"}
                and isinstance(value, int)
                and not isinstance(value, bool)
            )
            if drift_failures > 0 and outcome != "FAIL":
                findings.append(Finding("DRIFT_FAILURE_PRESENTED_AS_NONFAIL", f"{field}/outcome"))
            count_values = [counts.get(key) for key in ("baselined_warning", "fail_invariant", "fail_new_drift")]
            if all(isinstance(value, int) and not isinstance(value, bool) for value in count_values):
                if counts.get("finding") != sum(count_values):
                    findings.append(Finding("FINDING_COUNT_MISMATCH", f"{field}/finding_counts/finding"))

    overlap = _mapping(candidate.get("overlap"))
    base = _mapping(candidate.get("base"))
    for field, values in (
        ("/base/open_pull_requests", _array(base.get("open_pull_requests"))),
        ("/overlap/open_pull_requests", _array(overlap.get("open_pull_requests"))),
        ("/overlap/milestone_issue_numbers", _array(overlap.get("milestone_issue_numbers"))),
        ("/overlap/related_issue_numbers", _array(overlap.get("related_issue_numbers"))),
    ):
        _check_sorted_unique(values, field=field, findings=findings, code_prefix="ISSUE_NUMBERS")
    if base.get("open_pull_requests") != overlap.get("open_pull_requests"):
        findings.append(Finding("OPEN_PULL_REQUEST_SNAPSHOT_MISMATCH", "/overlap/open_pull_requests"))

    unresolved = _array(candidate.get("unresolved_items"))
    non_effects = _array(candidate.get("non_effects"))
    _check_sorted_unique(unresolved, field="/unresolved_items", findings=findings, code_prefix="UNRESOLVED_ITEMS")
    _check_sorted_unique(non_effects, field="/non_effects", findings=findings, code_prefix="NON_EFFECTS")
    if not REQUIRED_NON_EFFECTS.issubset(set(non_effects)):
        findings.append(Finding("REQUIRED_NON_EFFECT_MISSING", "/non_effects"))
    correction = _mapping(candidate.get("correction"))
    if correction.get("rollback_target") != f"git:{base.get('sha')}":
        findings.append(Finding("ROLLBACK_TARGET_MISMATCH", "/correction/rollback_target"))

    if check_paths:
        _check_path_digest(
            directory_rules,
            path_key="path",
            repo_root=repo_root,
            field="/authority_snapshot/directory_rules",
            expected_prefixes=("docs/doctrine/",),
            findings=findings,
        )
        for index, entry in enumerate(accepted):
            if isinstance(entry, dict):
                _check_path_digest(
                    entry,
                    path_key="path",
                    repo_root=repo_root,
                    field=f"/authority_snapshot/accepted_adrs/{index}",
                    expected_prefixes=("docs/adr/",),
                    findings=findings,
                )
        for index, entry in enumerate(candidates):
            if isinstance(entry, dict):
                _resolve_path(
                    entry.get("path"),
                    repo_root=repo_root,
                    field=f"/authority_snapshot/unresolved_authority_candidates/{index}/path",
                    expected_prefixes=("docs/adr/",),
                    findings=findings,
                )
        _check_path_digest(
            roots,
            path_key="registry_path",
            repo_root=repo_root,
            field="/repository_roots",
            expected_prefixes=("control_plane/",),
            findings=findings,
        )
        for index, entry in enumerate(projections):
            if isinstance(entry, dict):
                _check_path_digest(
                    entry,
                    path_key="path",
                    repo_root=repo_root,
                    field=f"/control_plane_projections/{index}",
                    expected_prefixes=("control_plane/",),
                    findings=findings,
                )
        _check_path_digest(
            catalog,
            path_key="registry_path",
            repo_root=repo_root,
            field="/trust_object_catalog",
            expected_prefixes=("control_plane/",),
            findings=findings,
        )

    if check_git:
        sha = base.get("sha")
        if isinstance(sha, str):
            try:
                completed = subprocess.run(
                    ["git", "cat-file", "-e", f"{sha}^{{commit}}"],
                    cwd=repo_root,
                    stdin=subprocess.DEVNULL,
                    stdout=subprocess.DEVNULL,
                    stderr=subprocess.DEVNULL,
                    timeout=5,
                    check=False,
                )
            except (OSError, subprocess.SubprocessError):
                findings.append(Finding("GIT_CHECK_UNAVAILABLE", "/base/sha"))
            else:
                if completed.returncode != 0:
                    findings.append(Finding("BASE_COMMIT_NOT_FOUND", "/base/sha"))

    return findings


def validate_baseline(
    path: Path,
    *,
    repo_root: Path = REPO_ROOT,
    check_paths: bool = True,
    check_git: bool = True,
) -> ValidationResult:
    candidate, findings = _read_object(path)
    if candidate is None:
        return ValidationResult(tuple(sorted(set(findings))))
    findings.extend(_schema_findings(candidate))
    findings.extend(
        _semantic_findings(
            candidate,
            repo_root=repo_root,
            check_paths=check_paths,
            check_git=check_git,
        )
    )
    return ValidationResult(tuple(sorted(set(findings))))


def _display(path: Path) -> str:
    try:
        return path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()
    except (OSError, ValueError):
        return path.name


def _serialize(path: Path, result: ValidationResult) -> str:
    return json.dumps(
        {
            "file": _display(path),
            "findings": [
                {"code": finding.code, "field": finding.field}
                for finding in result.findings
            ],
            "outcome": "PASS" if result.ok else "FAIL",
            "scope": SCOPE,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def run_fixture_profile() -> int:
    try:
        manifest = json.loads(
            (FIXTURE_ROOT / "expected_findings_manifest.json").read_text(encoding="utf-8")
        )
    except (OSError, UnicodeError, json.JSONDecodeError):
        return 1
    valid = sorted((FIXTURE_ROOT / "valid").glob("*.yaml"))
    invalid = sorted((FIXTURE_ROOT / "invalid").glob("*.yaml"))
    if not valid or not invalid or not isinstance(manifest, dict):
        return 1
    passed = True
    for path in valid:
        result = validate_baseline(path, check_paths=True, check_git=False)
        print(_serialize(path, result))
        passed = result.ok and passed
    for path in invalid:
        result = validate_baseline(path, check_paths=True, check_git=False)
        print(_serialize(path, result))
        expected = sorted(manifest.get(path.name, []))
        actual = sorted({finding.code for finding in result.findings})
        if result.ok or not expected or actual != expected:
            passed = False
            print(
                json.dumps(
                    {
                        "actual_codes": actual,
                        "expected_codes": expected,
                        "file": path.name,
                        "outcome": "FIXTURE_EXPECTATION_MISMATCH",
                    },
                    sort_keys=True,
                    separators=(",", ":"),
                ),
                file=sys.stderr,
            )
    return 0 if passed else 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", default=str(BASELINE_PATH))
    parser.add_argument("--repo-root", default=str(REPO_ROOT))
    parser.add_argument("--skip-path-existence", action="store_true")
    parser.add_argument("--skip-git-commit", action="store_true")
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        return run_fixture_profile()
    path = Path(args.path)
    result = validate_baseline(
        path,
        repo_root=Path(args.repo_root),
        check_paths=not args.skip_path_existence,
        check_git=not args.skip_git_commit,
    )
    print(_serialize(path, result))
    return 0 if result.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
