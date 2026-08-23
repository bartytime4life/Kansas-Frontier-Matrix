#!/usr/bin/env python3
"""Validate the pinned M01 program baseline without network access.

A pass proves bounded shape, ordering, issue/PR snapshot consistency, pinned
repository-byte digests, explicit failure posture, and review-slice path closure.
It does not create authority, approve review, mutate issues, waive drift, admit
sources, or authorize release, deployment, promotion, or publication.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import subprocess
import sys
from dataclasses import dataclass
from itertools import islice
from pathlib import Path, PurePosixPath
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
BASELINE_PATH = REPO_ROOT / "control_plane/program_baseline.json"
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/governance/program_baseline.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/governance/program_baseline"
MAX_FILE_BYTES = 4 * 1024 * 1024
MAX_SCHEMA_FINDINGS = 100
MAX_REFERENCED_FILE_BYTES = 64 * 1024 * 1024
GIT_TIMEOUT_SECONDS = 5
SCOPE = "m01-pinned-program-coordination-evidence-projection-only"
REQUIRED_ISSUES = {2768, 2874, 3365}
REQUIRED_NON_EFFECTS = frozenset(
    {
        "does_not_accept_or_supersede_adrs",
        "does_not_activate_or_admit_sources",
        "does_not_change_repository_settings",
        "does_not_expand_or_waive_drift_baselines",
        "does_not_release_deploy_promote_or_publish",
        "does_not_self_authorize",
        "does_not_turn_not_run_or_skipped_into_pass",
    }
)
WORKTREE_PREFIXES = (
    ".github/",
    "contracts/",
    "control_plane/",
    "data/receipts/generated/",
    "schemas/",
    "tests/",
    "tools/",
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
        return None, [Finding("JSON_INVALID", "/")]
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
    schema, read_findings = _read_object(SCHEMA_PATH)
    if schema is None:
        return [Finding("SCHEMA_UNAVAILABLE", item.field) for item in read_findings]
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
    values = [entry.get(key) for entry in entries if isinstance(entry, dict)]
    _check_sorted_unique(values, field=field, findings=findings, code_prefix=code_prefix)
    return values


def _git_run(repo_root: Path, arguments: list[str]) -> subprocess.CompletedProcess[bytes] | None:
    try:
        return subprocess.run(
            ["git", *arguments],
            cwd=repo_root,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            timeout=GIT_TIMEOUT_SECONDS,
            check=False,
        )
    except (OSError, subprocess.SubprocessError):
        return None


def _read_pinned_blob(
    relative_value: Any,
    *,
    base_sha: Any,
    repo_root: Path,
    field: str,
    expected_prefixes: tuple[str, ...],
    findings: list[Finding],
) -> bytes | None:
    relative = _canonical_path(relative_value)
    if relative is None:
        findings.append(Finding("PATH_INVALID", field))
        return None
    relative_text = relative.as_posix()
    if relative_text != "Makefile" and not any(
        relative_text.startswith(prefix) for prefix in expected_prefixes
    ):
        findings.append(Finding("PATH_ROOT_MISMATCH", field))
        return None
    if not isinstance(base_sha, str) or not re.fullmatch(r"[0-9a-f]{40}", base_sha):
        findings.append(Finding("BASE_SHA_INVALID", "/base/sha"))
        return None

    tree = _git_run(repo_root, ["ls-tree", "-z", base_sha, "--", relative_text])
    if tree is None or tree.returncode != 0 or not tree.stdout:
        findings.append(Finding("PATH_NOT_FOUND", field))
        return None
    try:
        records = [item for item in tree.stdout.split(b"\0") if item]
        metadata, returned_path = records[0].split(b"\t", 1)
        mode, object_type, _object_id = metadata.split(b" ", 2)
        returned = returned_path.decode("utf-8")
    except (UnicodeError, ValueError, IndexError):
        findings.append(Finding("PATH_READ_ERROR", field))
        return None
    if len(records) != 1 or returned != relative_text:
        findings.append(Finding("PATH_READ_ERROR", field))
        return None
    if object_type != b"blob":
        findings.append(Finding("PATH_NOT_FILE", field))
        return None
    if mode not in {b"100644", b"100755"}:
        findings.append(Finding("PATH_SYMLINK_DENIED", field))
        return None

    object_name = f"{base_sha}:{relative_text}"
    size_result = _git_run(repo_root, ["cat-file", "-s", object_name])
    if size_result is None or size_result.returncode != 0:
        findings.append(Finding("PATH_NOT_FOUND", field))
        return None
    try:
        size = int(size_result.stdout.decode("ascii").strip())
    except (UnicodeError, ValueError):
        findings.append(Finding("PATH_READ_ERROR", field))
        return None
    if size < 0 or size > MAX_REFERENCED_FILE_BYTES:
        findings.append(Finding("REFERENCED_FILE_TOO_LARGE", field))
        return None
    blob = _git_run(repo_root, ["cat-file", "blob", object_name])
    if blob is None or blob.returncode != 0 or len(blob.stdout) != size:
        findings.append(Finding("PATH_READ_ERROR", field))
        return None
    return blob.stdout


def _check_path_digest(
    entry: Mapping[str, Any],
    *,
    base_sha: Any,
    repo_root: Path,
    field: str,
    expected_prefixes: tuple[str, ...],
    findings: list[Finding],
) -> bytes | None:
    content = _read_pinned_blob(
        entry.get("path"),
        base_sha=base_sha,
        repo_root=repo_root,
        field=f"{field}/path",
        expected_prefixes=expected_prefixes,
        findings=findings,
    )
    digest = entry.get("sha256")
    if content is not None and isinstance(digest, str) and digest.startswith("sha256:"):
        actual = "sha256:" + hashlib.sha256(content).hexdigest()
        if actual != digest:
            findings.append(Finding("DIGEST_MISMATCH", f"{field}/sha256"))
    return content


def _check_worktree_path(
    value: Any,
    *,
    repo_root: Path,
    field: str,
    findings: list[Finding],
) -> None:
    relative = _canonical_path(value)
    if relative is None:
        findings.append(Finding("PATH_INVALID", field))
        return
    relative_text = relative.as_posix()
    if relative_text != "Makefile" and not any(
        relative_text.startswith(prefix) for prefix in WORKTREE_PREFIXES
    ):
        findings.append(Finding("PATH_ROOT_MISMATCH", field))
        return
    candidate = repo_root / relative_text
    try:
        if candidate.is_symlink():
            findings.append(Finding("PATH_SYMLINK_DENIED", field))
        elif not candidate.is_file():
            findings.append(Finding("PATH_NOT_FOUND", field))
    except OSError:
        findings.append(Finding("PATH_READ_ERROR", field))


def _semantic_findings(
    candidate: Mapping[str, Any],
    *,
    repo_root: Path,
    check_paths: bool,
    check_git: bool,
) -> list[Finding]:
    findings: list[Finding] = []
    base = _mapping(candidate.get("base"))
    base_sha = base.get("sha")

    if isinstance(base_sha, str) and candidate.get("baseline_id") != (
        "kfm-program-baseline-main-" + base_sha[:12]
    ):
        findings.append(Finding("BASELINE_ID_MISMATCH", "/baseline_id"))
    open_prs = _array(base.get("open_pull_requests"))
    _check_sorted_unique(
        open_prs,
        field="/base/open_pull_requests",
        findings=findings,
        code_prefix="OPEN_PULL_REQUESTS",
    )

    placement = _mapping(candidate.get("placement"))
    consumers = _array(placement.get("consumer_paths"))
    aliases = _array(placement.get("alias_paths"))
    _check_sorted_unique(
        consumers,
        field="/placement/consumer_paths",
        findings=findings,
        code_prefix="CONSUMER_PATHS",
    )
    _check_sorted_unique(
        aliases,
        field="/placement/alias_paths",
        findings=findings,
        code_prefix="ALIAS_PATHS",
    )
    if placement.get("adjacent_readme_path") not in consumers:
        findings.append(Finding("ADJACENT_README_NOT_CONSUMER", "/placement/adjacent_readme_path"))

    authority = _mapping(candidate.get("authority_snapshot"))
    adr_index = _mapping(authority.get("adr_index"))
    accepted_ids = _array(adr_index.get("accepted_ids"))
    _check_sorted_unique(
        accepted_ids,
        field="/authority_snapshot/adr_index/accepted_ids",
        findings=findings,
        code_prefix="ACCEPTED_ADRS",
    )
    if adr_index.get("accepted_count") != len(accepted_ids):
        findings.append(Finding("ACCEPTED_ADR_COUNT_MISMATCH", "/authority_snapshot/adr_index/accepted_count"))
    accepted_count = adr_index.get("accepted_count")
    proposed_count = adr_index.get("proposed_count")
    if isinstance(accepted_count, int) and isinstance(proposed_count, int):
        if accepted_count + proposed_count != 36:
            findings.append(Finding("NUMBERED_ADR_COUNT_MISMATCH", "/authority_snapshot/adr_index"))
    if adr_index.get("unassigned_scaffold_count") != 12:
        findings.append(Finding("ADR_SCAFFOLD_COUNT_MISMATCH", "/authority_snapshot/adr_index/unassigned_scaffold_count"))
    directory_rules = _mapping(authority.get("directory_rules"))
    if directory_rules.get("decision_ref") not in set(accepted_ids):
        findings.append(Finding("DIRECTORY_DECISION_NOT_ACCEPTED", "/authority_snapshot/directory_rules/decision_ref"))
    codeowners = _mapping(authority.get("codeowners"))
    root_registry = _mapping(authority.get("root_registry"))
    owner = placement.get("owner")
    if owner != codeowners.get("owner") or owner != root_registry.get("owner"):
        findings.append(Finding("OWNER_BINDING_MISMATCH", "/placement/owner"))

    surfaces = _array(candidate.get("tracked_surfaces"))
    _entry_ids(
        surfaces,
        key="id",
        field="/tracked_surfaces",
        findings=findings,
        code_prefix="TRACKED_SURFACE_IDS",
    )

    trackers = _array(candidate.get("tracker_snapshot"))
    tracker_numbers = _entry_ids(
        trackers,
        key="number",
        field="/tracker_snapshot",
        findings=findings,
        code_prefix="TRACKER_NUMBERS",
    )
    if set(tracker_numbers) != REQUIRED_ISSUES:
        findings.append(Finding("TRACKER_SET_MISMATCH", "/tracker_snapshot"))
    for index, raw_tracker in enumerate(trackers):
        tracker = _mapping(raw_tracker)
        stale = tracker.get("stale_at_base")
        recorded = tracker.get("recorded_baseline_sha")
        if stale is True and recorded == base_sha:
            findings.append(Finding("STALE_TRACKER_MATCHES_BASE", f"/tracker_snapshot/{index}/recorded_baseline_sha"))
        if stale is False and recorded != base_sha:
            findings.append(Finding("CURRENT_TRACKER_DIFFERS_FROM_BASE", f"/tracker_snapshot/{index}/recorded_baseline_sha"))

    lineage = _array(candidate.get("drive_lineage"))
    _entry_ids(
        lineage,
        key="file_id",
        field="/drive_lineage",
        findings=findings,
        code_prefix="DRIVE_FILE_IDS",
    )

    observations = _array(candidate.get("validation_observations"))
    observation_ids = _entry_ids(
        observations,
        key="id",
        field="/validation_observations",
        findings=findings,
        code_prefix="VALIDATION_IDS",
    )
    observation_by_id = {
        entry.get("id"): entry for entry in observations if isinstance(entry, dict)
    }
    for index, raw_observation in enumerate(observations):
        observation = _mapping(raw_observation)
        field = f"/validation_observations/{index}"
        run_state = observation.get("run_state")
        outcome = observation.get("outcome")
        failure_class = observation.get("failure_class")
        count = observation.get("finding_count")
        if run_state == "EXECUTED" and outcome in {"NOT_RUN", "SKIPPED"}:
            findings.append(Finding("RUN_STATE_OUTCOME_MISMATCH", f"{field}/outcome"))
        if run_state in {"NOT_RUN", "SKIPPED"} and outcome != run_state:
            findings.append(Finding("RUN_STATE_OUTCOME_MISMATCH", f"{field}/outcome"))
        if outcome == "PASS" and (failure_class != "NONE" or count != 0):
            findings.append(Finding("PASS_WITH_FAILURE", field))
        if outcome == "FAIL" and (failure_class not in {"INHERITED", "INTRODUCED"} or not isinstance(count, int) or count <= 0):
            findings.append(Finding("FAILURE_CLASSIFICATION_MISSING", field))
        if outcome not in {"FAIL"} and isinstance(count, int) and count > 0:
            findings.append(Finding("FINDINGS_PRESENTED_AS_NONFAIL", f"{field}/outcome"))

    required_observations = {
        "exact_main_hosted_checks": ("NOT_RUN", "NONE", 0),
        "object_family_workflow_watch_tests": ("FAIL", "INHERITED", 9),
        "repository_topology": ("FAIL", "INHERITED", 9),
    }
    for observation_id, expected in required_observations.items():
        observed = observation_by_id.get(observation_id)
        if not isinstance(observed, dict):
            findings.append(Finding("REQUIRED_OBSERVATION_MISSING", "/validation_observations"))
            continue
        actual = (
            observed.get("outcome"),
            observed.get("failure_class"),
            observed.get("finding_count"),
        )
        if actual != expected:
            findings.append(Finding("REQUIRED_OBSERVATION_MISMATCH", f"/validation_observations/{observation_ids.index(observation_id)}"))

    unresolved = _array(candidate.get("unresolved_items"))
    non_effects = _array(candidate.get("non_effects"))
    _check_sorted_unique(
        unresolved,
        field="/unresolved_items",
        findings=findings,
        code_prefix="UNRESOLVED_ITEMS",
    )
    _check_sorted_unique(
        non_effects,
        field="/non_effects",
        findings=findings,
        code_prefix="NON_EFFECTS",
    )
    if not REQUIRED_NON_EFFECTS.issubset(set(non_effects)):
        findings.append(Finding("REQUIRED_NON_EFFECT_MISSING", "/non_effects"))
    required_unresolved = {
        "exact_main_hosted_checks_not_run",
        "object_family_workflow_watch_coverage_has_nine_failures",
        "repository_topology_has_nine_unbaselined_findings",
    }
    if not required_unresolved.issubset(set(unresolved)):
        findings.append(Finding("REQUIRED_UNRESOLVED_ITEM_MISSING", "/unresolved_items"))

    correction = _mapping(candidate.get("correction"))
    stale_triggers = _array(correction.get("stale_triggers"))
    _check_sorted_unique(
        stale_triggers,
        field="/correction/stale_triggers",
        findings=findings,
        code_prefix="STALE_TRIGGERS",
    )
    if correction.get("rollback_target") != f"git:{base_sha}":
        findings.append(Finding("ROLLBACK_TARGET_MISMATCH", "/correction/rollback_target"))

    if check_paths:
        directory_bytes = _check_path_digest(
            directory_rules,
            base_sha=base_sha,
            repo_root=repo_root,
            field="/authority_snapshot/directory_rules",
            expected_prefixes=("docs/doctrine/",),
            findings=findings,
        )
        index_bytes = _check_path_digest(
            adr_index,
            base_sha=base_sha,
            repo_root=repo_root,
            field="/authority_snapshot/adr_index",
            expected_prefixes=("docs/adr/",),
            findings=findings,
        )
        codeowner_bytes = _check_path_digest(
            codeowners,
            base_sha=base_sha,
            repo_root=repo_root,
            field="/authority_snapshot/codeowners",
            expected_prefixes=(".github/",),
            findings=findings,
        )
        root_bytes = _check_path_digest(
            root_registry,
            base_sha=base_sha,
            repo_root=repo_root,
            field="/authority_snapshot/root_registry",
            expected_prefixes=("control_plane/",),
            findings=findings,
        )
        for index, entry in enumerate(surfaces):
            if isinstance(entry, dict):
                _check_path_digest(
                    entry,
                    base_sha=base_sha,
                    repo_root=repo_root,
                    field=f"/tracked_surfaces/{index}",
                    expected_prefixes=("control_plane/",),
                    findings=findings,
                )
        if isinstance(owner, str):
            owner_bytes = owner.encode("utf-8")
            if codeowner_bytes is not None and owner_bytes not in codeowner_bytes:
                findings.append(Finding("OWNER_NOT_IN_CODEOWNERS", "/authority_snapshot/codeowners/owner"))
            if root_bytes is not None and owner_bytes not in root_bytes:
                findings.append(Finding("OWNER_NOT_IN_ROOT_REGISTRY", "/authority_snapshot/root_registry/owner"))
        if index_bytes is not None:
            index_text = index_bytes.decode("utf-8", errors="replace")
            for accepted_id in accepted_ids:
                if not isinstance(accepted_id, str) or not re.search(
                    rf"^\| `{re.escape(accepted_id)}` \|.*\| `accepted` \|",
                    index_text,
                    flags=re.MULTILINE,
                ):
                    findings.append(Finding("ACCEPTED_ADR_INDEX_BINDING_MISSING", "/authority_snapshot/adr_index/accepted_ids"))
                    break
        if directory_bytes is not None and b"Directory Governance Standard" not in directory_bytes:
            findings.append(Finding("DIRECTORY_RULES_IDENTITY_MISSING", "/authority_snapshot/directory_rules/path"))
        _check_worktree_path(
            placement.get("canonical_path"),
            repo_root=repo_root,
            field="/placement/canonical_path",
            findings=findings,
        )
        for index, path in enumerate(consumers):
            _check_worktree_path(
                path,
                repo_root=repo_root,
                field=f"/placement/consumer_paths/{index}",
                findings=findings,
            )

    if check_git and isinstance(base_sha, str):
        commit = _git_run(repo_root, ["cat-file", "-e", f"{base_sha}^{{commit}}"])
        if commit is None:
            findings.append(Finding("GIT_CHECK_UNAVAILABLE", "/base/sha"))
        elif commit.returncode != 0:
            findings.append(Finding("BASE_COMMIT_NOT_FOUND", "/base/sha"))
        canonical_path = placement.get("canonical_path")
        if isinstance(canonical_path, str):
            old_path = _git_run(repo_root, ["ls-tree", "-z", base_sha, "--", canonical_path])
            if old_path is None:
                findings.append(Finding("GIT_CHECK_UNAVAILABLE", "/placement/canonical_path"))
            elif old_path.returncode != 0:
                findings.append(Finding("BASE_PATH_CHECK_FAILED", "/placement/canonical_path"))
            elif old_path.stdout:
                findings.append(Finding("BASE_PATH_NOT_ABSENT", "/placement/base_path_status"))

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
    return validate_candidate(
        candidate,
        repo_root=repo_root,
        check_paths=check_paths,
        check_git=check_git,
    )


def validate_candidate(
    candidate: Mapping[str, Any],
    *,
    repo_root: Path = REPO_ROOT,
    check_paths: bool = True,
    check_git: bool = True,
) -> ValidationResult:
    findings: list[Finding] = []
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
                {"code": item.code, "field": item.field} for item in result.findings
            ],
            "outcome": "PASS" if result.ok else "FAIL",
            "scope": SCOPE,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def run_fixture_profile() -> int:
    try:
        fixture_document = json.loads(
            (FIXTURE_ROOT / "cases.json").read_text(encoding="utf-8"),
            object_pairs_hook=_unique_object,
            parse_constant=_reject_nonfinite,
            parse_float=_parse_finite_float,
        )
    except (OSError, UnicodeError, json.JSONDecodeError):
        return 1
    except (DuplicateKeyError, NonFiniteNumberError, RecursionError, ValueError):
        return 1
    if not isinstance(fixture_document, dict):
        return 1
    base = fixture_document.get("base")
    cases = fixture_document.get("cases")
    if not isinstance(base, dict) or not isinstance(cases, list) or len(cases) < 2:
        return 1
    case_ids = [case.get("id") for case in cases if isinstance(case, dict)]
    if case_ids != sorted(case_ids) or len(case_ids) != len(set(case_ids)):
        return 1
    passed = True
    for case in cases:
        if not isinstance(case, dict):
            return 1
        case_id = case.get("id")
        expected = case.get("expected_codes")
        mutations = case.get("mutations", [])
        if (
            not isinstance(case_id, str)
            or not isinstance(expected, list)
            or not isinstance(mutations, list)
        ):
            return 1
        candidate = json.loads(json.dumps(base))
        for mutation in mutations:
            if not isinstance(mutation, dict):
                return 1
            path = mutation.get("path")
            if not isinstance(path, list) or not path:
                return 1
            target: Any = candidate
            for part in path[:-1]:
                if isinstance(target, dict) and isinstance(part, str) and part in target:
                    target = target[part]
                elif isinstance(target, list) and isinstance(part, int) and 0 <= part < len(target):
                    target = target[part]
                else:
                    return 1
            final = path[-1]
            operation = mutation.get("op", "set")
            if operation == "set":
                if isinstance(target, dict) and isinstance(final, str):
                    target[final] = mutation.get("value")
                elif isinstance(target, list) and isinstance(final, int) and 0 <= final < len(target):
                    target[final] = mutation.get("value")
                else:
                    return 1
            elif operation == "append" and isinstance(target, list):
                target.append(mutation.get("value"))
            else:
                return 1
        result = validate_candidate(candidate, check_paths=True, check_git=False)
        display_path = FIXTURE_ROOT / f"{case_id}.json"
        print(_serialize(display_path, result))
        expected = sorted(item for item in expected if isinstance(item, str))
        actual = sorted({item.code for item in result.findings})
        should_pass = not expected
        if result.ok != should_pass or actual != expected:
            passed = False
            print(
                json.dumps(
                    {
                        "actual_codes": actual,
                        "expected_codes": expected,
                        "file": f"{case_id}.json",
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
