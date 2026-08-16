#!/usr/bin/env python3
"""Assess the unresolved TemporalAuthorityEnvelope authority collision.

The assessment is local, deterministic, read-only, and non-authoritative. It
requires the two currently confirmed same-named families, inventories bounded
UTF-8 tracked text, and returns HOLD_UNRESOLVED (exit 3) while the conflict
remains unchanged. It never accepts ADR-0014, chooses a canonical family,
migrates consumers, or creates evidence, policy, review, release, publication,
deployment, or access authority.

Exit codes: 1 FAIL_INVARIANT, 2 ERROR_VALIDATOR, 3 HOLD_UNRESOLVED.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import sys
from collections import Counter
from pathlib import Path, PurePosixPath
from typing import Iterable, Mapping, Sequence

REPORT_VERSION = "kfm.temporal-authority-envelope-conflict-assessment.v1"
MAX_TEXT_BYTES = 64 * 1024 * 1024
MAX_REFERENCES = 20_000
EXIT_FAIL, EXIT_ERROR, EXIT_HOLD = 1, 2, 3

ADR_0014 = "docs/adr/ADR-0014-temporal-vocabulary--six-time-kinds-tracked.md"
ADR_0029 = "docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md"
COMMON_CONTRACT = "contracts/common/temporal_authority_envelope.md"
COMMON_SCHEMA = "schemas/contracts/v1/common/temporal_authority_envelope.schema.json"
COMMON_VALIDATOR = "tools/validators/validate_temporal_authority_envelope.py"
COMMON_TEST = "tests/validators/test_validate_temporal_authority_envelope.py"
COMMON_WORKFLOW = ".github/workflows/briefing-integration.yml"
COMMON_FIXTURES = "fixtures/contracts/v1/common/temporal_authority_envelope"
EVIDENCE_CONTRACT = "contracts/evidence/temporal_authority_envelope.md"
EVIDENCE_SCHEMA = "schemas/contracts/v1/evidence/temporal_authority_envelope.schema.json"
EVIDENCE_VALIDATOR = "tools/validators/evidence/validate_temporal_authority_envelope.py"
EVIDENCE_TEST = "tests/evidence/test_temporal_authority_envelope.py"
EVIDENCE_WORKFLOW = ".github/workflows/temporal-authority-envelope.yml"
EVIDENCE_FIXTURES = "fixtures/contracts/v1/evidence/temporal_authority_envelope"
ASSESSMENT_PATHS = frozenset(
    {
        "tools/validators/governance/assess_temporal_authority_envelope_conflict.py",
        "tests/validators/governance/test_assess_temporal_authority_envelope_conflict.py",
        ".github/workflows/temporal-authority-envelope-conflict-assessment.yml",
        "tools/validators/governance/README.md",
    }
)
REQUIRED_FILES = {
    "common": (COMMON_CONTRACT, COMMON_SCHEMA, COMMON_VALIDATOR, COMMON_TEST, COMMON_WORKFLOW),
    "evidence": (EVIDENCE_CONTRACT, EVIDENCE_SCHEMA, EVIDENCE_VALIDATOR, EVIDENCE_TEST, EVIDENCE_WORKFLOW),
}
REQUIRED_FIXTURE_DIRS = {
    "common": (f"{COMMON_FIXTURES}/valid", f"{COMMON_FIXTURES}/invalid"),
    "evidence": (f"{EVIDENCE_FIXTURES}/valid", f"{EVIDENCE_FIXTURES}/invalid"),
}
TOKENS = {
    "object_name": "TemporalAuthorityEnvelope",
    "snake_name": "temporal_authority_envelope",
    "common_contract": COMMON_CONTRACT,
    "common_schema": COMMON_SCHEMA,
    "common_validator": COMMON_VALIDATOR,
    "evidence_contract": EVIDENCE_CONTRACT,
    "evidence_schema": EVIDENCE_SCHEMA,
    "evidence_validator": EVIDENCE_VALIDATOR,
}
COMMON_TOKEN_IDS = frozenset({"common_contract", "common_schema", "common_validator"})
EVIDENCE_TOKEN_IDS = frozenset({"evidence_contract", "evidence_schema", "evidence_validator"})
TEXT_SUFFIXES = frozenset(
    ".cfg .csv .graphql .html .ini .js .json .jsonl .jsx .md .mjs .ndjson .py .rego .rst .sh .sql .toml .ts .tsx .txt .xml .yaml .yml".split()
)
TEXT_FILENAMES = frozenset({"Dockerfile", "Makefile", "NOTICE", "README"})
EXCLUDED_DIRS = frozenset(
    {".git", ".mypy_cache", ".pytest_cache", ".ruff_cache", ".tox", ".venv", "__pycache__", "dist", "node_modules", "vendor", "venv"}
)


def _sha(payload: bytes) -> str:
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def _canonical(value: object) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()


def _finding(code: str, path: str, detail: str) -> dict[str, str]:
    return {"code": code, "detail": detail, "path": path}


def _authority() -> dict[str, bool]:
    return {
        "accepts_adr": False,
        "authorizes_migration": False,
        "authorizes_repository_write": False,
        "creates_evidence": False,
        "creates_policy_or_review_decision": False,
        "creates_release_or_publication_authority": False,
        "selects_canonical_family": False,
    }


def _report_hash(report: Mapping[str, object]) -> str:
    payload = dict(report)
    payload.pop("report_sha256", None)
    return _sha(_canonical(payload))


def _relative(root: Path, path: Path) -> str:
    return path.relative_to(root).as_posix()


def _text_files(root: Path) -> Iterable[Path]:
    for current, dirs, files in os.walk(root):
        dirs[:] = sorted(name for name in dirs if name not in EXCLUDED_DIRS)
        current_path = Path(current)
        for name in sorted(files):
            path = current_path / name
            if path.is_symlink():
                continue
            if path.suffix.lower() in TEXT_SUFFIXES or path.name in TEXT_FILENAMES:
                yield path


def _classify(path: str) -> str:
    parts = PurePosixPath(path).parts
    if path in ASSESSMENT_PATHS:
        return "assessment_surface"
    if path.startswith((COMMON_FIXTURES + "/", EVIDENCE_FIXTURES + "/")):
        return "family_fixture"
    if path in set(REQUIRED_FILES["common"]) | set(REQUIRED_FILES["evidence"]):
        return "family_surface"
    if parts[:2] == ("docs", "adr"):
        return "decision_record"
    if parts[:2] == ("docs", "intake"):
        return "source_map_or_intake_doc"
    if parts and parts[0] == "docs":
        return "documentation"
    if parts and parts[0] == "contracts":
        return "semantic_consumer"
    if parts and parts[0] == "schemas":
        return "schema_consumer"
    if parts[:2] == ("data", "receipts"):
        return "receipt_binding"
    if parts and parts[0] == "fixtures":
        return "fixture"
    if parts and parts[0] == "tests":
        return "test"
    if parts[:2] == (".github", "workflows"):
        return "workflow"
    if parts and parts[0] == "tools":
        return "validator_or_tool"
    if parts and parts[0] in {"apps", "packages", "runtime", "connectors", "pipelines", "pipeline_specs"}:
        return "runtime_or_implementation_consumer"
    if parts and parts[0] == "release":
        return "release_consumer"
    if len(parts) >= 2 and parts[0] == "data" and parts[1] in {
        "raw", "work", "quarantine", "processed", "catalog", "triplet", "triplets", "published", "proofs", "registry", "rollback"
    }:
        return "persisted_or_lifecycle_consumer"
    return "other"


def _families(path: str, token_ids: set[str]) -> list[str]:
    values: set[str] = set()
    if token_ids & COMMON_TOKEN_IDS or path.startswith(COMMON_FIXTURES + "/") or path in REQUIRED_FILES["common"]:
        values.add("common")
    if token_ids & EVIDENCE_TOKEN_IDS or path.startswith(EVIDENCE_FIXTURES + "/") or path in REQUIRED_FILES["evidence"]:
        values.add("evidence")
    return sorted(values or {"ambiguous"})


def _read_text(path: Path) -> tuple[str | None, dict[str, str] | None]:
    try:
        size = path.stat().st_size
    except OSError as exc:
        return None, _finding("KFM-TAE-SCAN-001", path.as_posix(), f"stat_failed:{type(exc).__name__}")
    if size > MAX_TEXT_BYTES:
        return None, _finding("KFM-TAE-SCAN-002", path.as_posix(), f"text_candidate_exceeds_{MAX_TEXT_BYTES}_bytes")
    try:
        payload = path.read_bytes()
    except OSError as exc:
        return None, _finding("KFM-TAE-SCAN-003", path.as_posix(), f"read_failed:{type(exc).__name__}")
    if b"\x00" in payload:
        return None, _finding("KFM-TAE-SCAN-004", path.as_posix(), "text_candidate_contains_nul")
    try:
        return payload.decode("utf-8"), None
    except UnicodeDecodeError:
        return None, _finding("KFM-TAE-SCAN-005", path.as_posix(), "text_candidate_is_not_utf8")


def _inventory(root: Path) -> tuple[list[dict[str, object]], list[dict[str, str]], int]:
    references: list[dict[str, object]] = []
    gaps: list[dict[str, str]] = []
    scanned = 0
    for absolute in _text_files(root):
        relative = _relative(root, absolute)
        text, gap = _read_text(absolute)
        if gap:
            gap["path"] = relative
            gaps.append(gap)
            continue
        assert text is not None
        scanned += 1
        token_ids: set[str] = set()
        line_numbers: set[int] = set()
        for number, line in enumerate(text.splitlines(), 1):
            matched = {key for key, token in TOKENS.items() if token in line}
            if matched:
                token_ids.update(matched)
                line_numbers.add(number)
        if not token_ids:
            continue
        if len(references) >= MAX_REFERENCES:
            gaps.append(_finding("KFM-TAE-SCAN-006", relative, f"reference_limit_exceeded:{MAX_REFERENCES}"))
            break
        payload = text.encode()
        references.append(
            {
                "classification": _classify(relative),
                "content_sha256": _sha(payload),
                "families": _families(relative, token_ids),
                "line_numbers": sorted(line_numbers),
                "path": relative,
                "reference_mode": "exact_path" if token_ids & (COMMON_TOKEN_IDS | EVIDENCE_TOKEN_IDS) else "name_only",
                "token_ids": sorted(token_ids),
            }
        )
    return sorted(references, key=lambda item: str(item["path"])), sorted(gaps, key=lambda item: (item["path"], item["code"])), scanned


def _required_state(root: Path, findings: list[dict[str, str]]) -> dict[str, object]:
    state: dict[str, object] = {}
    for family in ("common", "evidence"):
        files: list[dict[str, str]] = []
        directories: list[dict[str, object]] = []
        for relative in REQUIRED_FILES[family]:
            path = root / relative
            if not path.is_file() or path.is_symlink():
                findings.append(_finding("KFM-TAE-FAMILY-001", relative, f"missing_or_nonregular_{family}_family_file"))
                continue
            try:
                files.append({"path": relative, "sha256": _sha(path.read_bytes())})
            except OSError as exc:
                findings.append(_finding("KFM-TAE-FAMILY-004", relative, f"family_file_read_failed:{type(exc).__name__}"))
        for relative in REQUIRED_FIXTURE_DIRS[family]:
            path = root / relative
            fixtures = sorted(_relative(root, item) for item in path.rglob("*.json") if item.is_file() and not item.is_symlink()) if path.is_dir() else []
            if not path.is_dir():
                findings.append(_finding("KFM-TAE-FAMILY-002", relative, f"missing_{family}_fixture_directory"))
            elif not fixtures:
                findings.append(_finding("KFM-TAE-FAMILY-003", relative, f"empty_{family}_fixture_directory"))
            else:
                directories.append({"directory": relative, "fixture_count": len(fixtures), "path_set_sha256": _sha("\n".join(fixtures).encode())})
        state[family] = {"files": sorted(files, key=lambda item: item["path"]), "fixture_directories": directories}
    return state


def _discover(root: Path) -> dict[str, list[str]]:
    def paths(base: str, name: str) -> list[str]:
        directory = root / base
        return sorted(_relative(root, path) for path in directory.rglob(name) if path.is_file() and not path.is_symlink()) if directory.is_dir() else []

    return {
        "contracts": paths("contracts", "temporal_authority_envelope.md"),
        "schemas": paths("schemas/contracts/v1", "temporal_authority_envelope.schema.json"),
        "validators": paths("tools/validators", "validate_temporal_authority_envelope.py"),
    }


def _governance(root: Path, findings: list[dict[str, str]]) -> dict[str, object]:
    state: dict[str, object] = {}
    for key, relative in (("adr_0014", ADR_0014), ("adr_0029", ADR_0029)):
        path = root / relative
        if not path.is_file() or path.is_symlink():
            findings.append(_finding("KFM-TAE-GOV-001", relative, "required_governance_record_missing"))
            continue
        try:
            payload = path.read_bytes()
            text = payload.decode("utf-8")
        except OSError as exc:
            findings.append(_finding("KFM-TAE-GOV-005", relative, f"governance_record_read_failed:{type(exc).__name__}"))
            continue
        except UnicodeDecodeError:
            findings.append(_finding("KFM-TAE-GOV-006", relative, "governance_record_is_not_utf8"))
            continue
        state[key] = {"path": relative, "sha256": _sha(payload)}
        lowered = text.casefold()
        if key == "adr_0014":
            if "status: proposed" not in lowered and 'status: "proposed"' not in lowered:
                findings.append(_finding("KFM-TAE-GOV-002", relative, "adr_0014_not_explicitly_proposed"))
            if "parallel" not in lowered or "conflict" not in lowered:
                findings.append(_finding("KFM-TAE-GOV-003", relative, "adr_0014_conflict_boundary_not_found"))
        elif "accepted" not in lowered:
            findings.append(_finding("KFM-TAE-GOV-004", relative, "adr_0029_acceptance_marker_not_found"))
    return state


def assess(root: Path, *, revision: str = "UNKNOWN") -> tuple[int, dict[str, object]]:
    root = root.resolve()
    if not root.is_dir():
        report = {"report_version": REPORT_VERSION, "outcome": "ERROR_VALIDATOR", "disposition": "HOLD", "revision": revision, "scan_complete": False, "findings": [_finding("KFM-TAE-ROOT-001", ".", "repository_root_missing")], "authority": _authority()}
        report["report_sha256"] = _report_hash(report)
        return EXIT_ERROR, report

    findings: list[dict[str, str]] = []
    family_state = _required_state(root, findings)
    discovered = _discover(root)
    expected = {
        "contracts": sorted([COMMON_CONTRACT, EVIDENCE_CONTRACT]),
        "schemas": sorted([COMMON_SCHEMA, EVIDENCE_SCHEMA]),
        "validators": sorted([COMMON_VALIDATOR, EVIDENCE_VALIDATOR]),
    }
    for kind in expected:
        if discovered[kind] != expected[kind]:
            findings.append(_finding("KFM-TAE-FAMILY-005", kind, "same_name_family_set_differs_from_confirmed_two_family_conflict"))
    governance = _governance(root, findings)
    references, scan_gaps, scanned_count = _inventory(root)
    critical_classes = {"persisted_or_lifecycle_consumer", "release_consumer", "runtime_or_implementation_consumer"}
    critical_paths = sorted({str(item["path"]) for item in references if item["classification"] in critical_classes})
    ambiguous_paths = sorted({str(item["path"]) for item in references if item["families"] == ["ambiguous"]})

    if scan_gaps:
        code, outcome, reasons = EXIT_ERROR, "ERROR_VALIDATOR", ["KFM-TAE-SCAN-INCOMPLETE"]
    elif findings:
        code, outcome, reasons = EXIT_FAIL, "FAIL_INVARIANT", ["KFM-TAE-CONFLICT-SHAPE-DRIFT"]
    else:
        code, outcome = EXIT_HOLD, "HOLD_UNRESOLVED"
        reasons = ["KFM-TAE-MIGRATION-NOT-AUTHORIZED", "KFM-TAE-PARALLEL-AUTHORITY-CONFIRMED", "KFM-TAE-TRACKED-TEXT-INVENTORY-COMPLETE"]
        if critical_paths:
            reasons.append("KFM-TAE-CRITICAL-CONSUMER-PRESENT")
        if ambiguous_paths:
            reasons.append("KFM-TAE-AMBIGUOUS-NAME-REFERENCES-PRESENT")

    classes = Counter(str(item["classification"]) for item in references)
    families = Counter(family for item in references for family in item["families"])
    report: dict[str, object] = {
        "report_version": REPORT_VERSION,
        "outcome": outcome,
        "disposition": "HOLD",
        "reason_codes": sorted(reasons),
        "revision": revision,
        "scan_complete": not scan_gaps,
        "scanned_text_file_count": scanned_count,
        "family_state": family_state,
        "same_name_family_discovery": discovered,
        "governance_state": governance,
        "reference_counts": {"by_classification": dict(sorted(classes.items())), "by_family": dict(sorted(families.items())), "critical_consumer_count": len(critical_paths), "reference_file_count": len(references)},
        "critical_consumer_paths": critical_paths,
        "ambiguous_reference_paths": ambiguous_paths,
        "inventory_scope": {"tracked_repository_text": True, "runtime_observation": False, "external_object_storage": False, "database_records": False, "generated_ci_artifacts": False},
        "reference_inventory": references,
        "findings": sorted(findings, key=lambda item: (item["path"], item["code"], item["detail"])),
        "scan_gaps": scan_gaps,
        "authority": _authority(),
        "non_effects": [
            "does_not_accept_adr_0014",
            "does_not_select_a_canonical_family",
            "does_not_migrate_or_delete_consumers",
            "does_not_prove_complete_runtime_or_persisted_consumer_graph",
            "does_not_create_evidence_or_policy_authority",
            "does_not_release_publish_deploy_or_widen_access",
        ],
    }
    report["report_sha256"] = _report_hash(report)
    return code, report


def _render_text(report: Mapping[str, object]) -> str:
    counts = report.get("reference_counts", {})
    return "\n".join(
        [
            f"outcome={report.get('outcome')}",
            f"disposition={report.get('disposition')}",
            f"revision={report.get('revision')}",
            f"scan_complete={str(report.get('scan_complete')).lower()}",
            f"reference_file_count={counts.get('reference_file_count', 0) if isinstance(counts, Mapping) else 0}",
            f"critical_consumer_count={counts.get('critical_consumer_count', 0) if isinstance(counts, Mapping) else 0}",
            f"finding_count={len(report.get('findings', []))}",
            f"scan_gap_count={len(report.get('scan_gaps', []))}",
            f"report_sha256={report.get('report_sha256')}",
            "authority_created=false",
            "canonical_family_selected=false",
            "",
        ]
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument("--revision", default="UNKNOWN")
    parser.add_argument("--format", choices=("json", "text"), default="text")
    args = parser.parse_args(argv)
    try:
        code, report = assess(args.root, revision=args.revision)
    except (OSError, UnicodeError, ValueError) as exc:
        report = {"report_version": REPORT_VERSION, "outcome": "ERROR_VALIDATOR", "disposition": "HOLD", "revision": args.revision, "scan_complete": False, "findings": [_finding("KFM-TAE-UNEXPECTED-001", ".", type(exc).__name__)], "authority": _authority()}
        report["report_sha256"] = _report_hash(report)
        code = EXIT_ERROR
    if args.format == "json":
        print(json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2))
    else:
        sys.stdout.write(_render_text(report))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
