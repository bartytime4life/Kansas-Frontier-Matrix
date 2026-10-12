"""Support primitives for the compatibility-first TemporalAuthorityEnvelope split."""
from __future__ import annotations

import copy
import hashlib
import json
import os
from pathlib import Path
from typing import Iterable, Mapping

REPORT_VERSION = "kfm.temporal-authority-envelope-split-assessment.v1"
EXIT_FAIL, EXIT_ERROR, EXIT_HOLD = 1, 2, 3
MAX_TEXT_BYTES = 64 * 1024 * 1024
MAX_REFERENCES = 20_000

ADR_0014 = "docs/adr/ADR-0014-temporal-vocabulary--six-time-kinds-tracked.md"
ADR_0029 = "docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md"
COMMON_CONTRACT = "contracts/common/temporal_authority_envelope.md"
COMMON_SCHEMA = "schemas/contracts/v1/common/temporal_authority_envelope.schema.json"
COMMON_SCHEMA_ID = "https://schemas.kfm.local/contracts/v1/common/temporal_authority_envelope.schema.json"
CANONICAL_CONTRACT = "contracts/evidence/evidence_temporal_posture_assessment.md"
CANONICAL_SCHEMA = "schemas/contracts/v1/evidence/evidence_temporal_posture_assessment.schema.json"
CANONICAL_SCHEMA_ID = "https://kfm.invalid/schemas/contracts/v1/evidence/evidence_temporal_posture_assessment.schema.json"
CANONICAL_VALIDATOR = "tools/validators/evidence/validate_evidence_temporal_posture_assessment.py"
CANONICAL_TEST = "tests/evidence/test_evidence_temporal_posture_assessment.py"
CANONICAL_WORKFLOW = ".github/workflows/evidence-temporal-posture-assessment.yml"
CANONICAL_FIXTURES = "fixtures/contracts/v1/evidence/evidence_temporal_posture_assessment"
LEGACY_CONTRACT = "contracts/evidence/temporal_authority_envelope.md"
LEGACY_SCHEMA = "schemas/contracts/v1/evidence/temporal_authority_envelope.schema.json"
LEGACY_SCHEMA_ID = "https://kfm.invalid/schemas/contracts/v1/evidence/temporal_authority_envelope.schema.json"
LEGACY_VALIDATOR = "tools/validators/evidence/validate_temporal_authority_envelope.py"
LEGACY_TEST = "tests/evidence/test_temporal_authority_envelope.py"
LEGACY_WORKFLOW = ".github/workflows/temporal-authority-envelope.yml"
LEGACY_FIXTURES = "fixtures/contracts/v1/evidence/temporal_authority_envelope"
ADVISORY_SCHEMA = "schemas/contracts/v1/common/advisory_event_envelope.schema.json"
PROGRAM_CONTRACT = "contracts/governance/program_outcome_chain.md"
PROGRAM_MODEL = "tools/validators/governance/program_outcome_chain_model.py"
PROGRAM_LEGACY_REFERENCE = "kfm:temporal-authority:synthetic-program-v1"
LEGACY_PREFIX = "kfm:temporal-authority:"

REQUIRED_FILES = (
    ADR_0014, ADR_0029, COMMON_CONTRACT, COMMON_SCHEMA,
    CANONICAL_CONTRACT, CANONICAL_SCHEMA, CANONICAL_VALIDATOR, CANONICAL_TEST, CANONICAL_WORKFLOW,
    LEGACY_CONTRACT, LEGACY_SCHEMA, LEGACY_VALIDATOR, LEGACY_TEST, LEGACY_WORKFLOW,
    ADVISORY_SCHEMA, PROGRAM_CONTRACT, PROGRAM_MODEL,
)
REQUIRED_FIXTURE_DIRS = (
    f"{CANONICAL_FIXTURES}/valid", f"{CANONICAL_FIXTURES}/invalid",
    f"{LEGACY_FIXTURES}/valid", f"{LEGACY_FIXTURES}/invalid",
)
TEXT_SUFFIXES = frozenset(
    ".cfg .csv .graphql .html .ini .js .json .jsonl .jsx .md .mjs .ndjson .py .rego .rst .sh .sql .toml .ts .tsx .txt .xml .yaml .yml".split()
)
TEXT_FILENAMES = frozenset({"Dockerfile", "Makefile", "NOTICE", "README"})
EXCLUDED_DIRS = frozenset({".git", ".mypy_cache", ".pytest_cache", ".ruff_cache", ".tox", ".venv", "__pycache__", "dist", "node_modules", "vendor", "venv"})
KNOWN_COMMON_REFERENCE_PATHS = frozenset({
    PROGRAM_CONTRACT,
    "schemas/contracts/v1/governance/program_outcome_chain.schema.json",
    "contracts/common/modeled_surface.md",
    "schemas/contracts/v1/common/modeled_surface.schema.json",
    "contracts/common/forecast_product.md",
    "schemas/contracts/v1/common/forecast_product.schema.json",
    "contracts/common/classification_release.md",
    "schemas/contracts/v1/common/classification_release.schema.json",
    "contracts/common/aggregate_statistic.md",
    "schemas/contracts/v1/common/aggregate_statistic.schema.json",
})


def _sha(payload: bytes) -> str:
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def _canonical(value: object) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()


def _finding(code: str, path: str, detail: str) -> dict[str, str]:
    return {"code": code, "path": path, "detail": detail}


def _authority() -> dict[str, bool]:
    return {
        "accepts_adr": False,
        "authorizes_legacy_removal": False,
        "authorizes_repository_write": False,
        "creates_evidence": False,
        "creates_policy_or_review_decision": False,
        "creates_release_or_publication_authority": False,
        "translates_common_and_evidence_records": False,
    }


def _report_hash(report: Mapping[str, object]) -> str:
    payload = dict(report)
    payload.pop("report_sha256", None)
    return _sha(_canonical(payload))


def _read_text(path: Path, root: Path) -> tuple[str | None, dict[str, str] | None]:
    relative = path.relative_to(root).as_posix()
    try:
        if path.stat().st_size > MAX_TEXT_BYTES:
            return None, _finding("KFM-TAE-SCAN-002", relative, f"text_candidate_exceeds_{MAX_TEXT_BYTES}_bytes")
        payload = path.read_bytes()
    except OSError as exc:
        return None, _finding("KFM-TAE-SCAN-003", relative, f"read_failed:{type(exc).__name__}")
    if b"\x00" in payload:
        return None, _finding("KFM-TAE-SCAN-004", relative, "text_candidate_contains_nul")
    try:
        return payload.decode("utf-8"), None
    except UnicodeDecodeError:
        return None, _finding("KFM-TAE-SCAN-005", relative, "text_candidate_is_not_utf8")


def _text_files(root: Path) -> Iterable[Path]:
    for current, dirs, files in os.walk(root):
        dirs[:] = sorted(name for name in dirs if name not in EXCLUDED_DIRS)
        base = Path(current)
        for name in sorted(files):
            path = base / name
            if not path.is_symlink() and (path.suffix.lower() in TEXT_SUFFIXES or path.name in TEXT_FILENAMES):
                yield path


def _load_json(root: Path, relative: str, findings: list[dict[str, str]]) -> dict[str, object] | None:
    try:
        value = json.loads((root / relative).read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError) as exc:
        findings.append(_finding("KFM-TAE-SHAPE-001", relative, f"json_unavailable:{type(exc).__name__}"))
        return None
    if not isinstance(value, dict):
        findings.append(_finding("KFM-TAE-SHAPE-002", relative, "json_root_not_object"))
        return None
    return value


def _schema_shape(schema: Mapping[str, object]) -> dict[str, object]:
    result = copy.deepcopy(dict(schema))
    for key in ("$id", "title", "description", "$comment", "x-kfm"):
        result.pop(key, None)
    return result


def _fixture_map(root: Path, base: str) -> dict[str, str]:
    directory = root / base
    return {
        path.relative_to(directory).as_posix(): _sha(path.read_bytes())
        for path in sorted(directory.rglob("*.json"))
        if path.is_file() and not path.is_symlink()
    }


def _verify_state(root: Path, findings: list[dict[str, str]]) -> dict[str, object]:
    for relative in REQUIRED_FILES:
        if not (root / relative).is_file() or (root / relative).is_symlink():
            findings.append(_finding("KFM-TAE-FAMILY-001", relative, "required_file_missing_or_nonregular"))
    for relative in REQUIRED_FIXTURE_DIRS:
        directory = root / relative
        if not directory.is_dir() or not any(directory.glob("*.json")):
            findings.append(_finding("KFM-TAE-FAMILY-002", relative, "required_fixture_lane_missing_or_empty"))

    common = _load_json(root, COMMON_SCHEMA, findings)
    canonical = _load_json(root, CANONICAL_SCHEMA, findings)
    legacy = _load_json(root, LEGACY_SCHEMA, findings)
    advisory = _load_json(root, ADVISORY_SCHEMA, findings)
    if common is not None and (common.get("$id") != COMMON_SCHEMA_ID or common.get("title") not in {"TemporalAuthorityEnvelope", "temporal_authority_envelope"}):
        findings.append(_finding("KFM-TAE-COMMON-001", COMMON_SCHEMA, "common_schema_identity_changed"))
    if canonical is not None and (canonical.get("$id") != CANONICAL_SCHEMA_ID or canonical.get("title") != "EvidenceTemporalPostureAssessment"):
        findings.append(_finding("KFM-TAE-SPLIT-001", CANONICAL_SCHEMA, "canonical_evidence_assessment_identity_invalid"))
    if legacy is not None and (legacy.get("$id") != LEGACY_SCHEMA_ID or legacy.get("title") != "TemporalAuthorityEnvelope"):
        findings.append(_finding("KFM-TAE-COMPAT-001", LEGACY_SCHEMA, "legacy_schema_identity_changed"))
    if canonical is not None and legacy is not None and _schema_shape(canonical) != _schema_shape(legacy):
        findings.append(_finding("KFM-TAE-COMPAT-002", CANONICAL_SCHEMA, "canonical_and_legacy_machine_shapes_diverge"))

    canonical_fixtures = _fixture_map(root, CANONICAL_FIXTURES) if (root / CANONICAL_FIXTURES).is_dir() else {}
    legacy_fixtures = _fixture_map(root, LEGACY_FIXTURES) if (root / LEGACY_FIXTURES).is_dir() else {}
    if canonical_fixtures != legacy_fixtures:
        findings.append(_finding("KFM-TAE-COMPAT-003", CANONICAL_FIXTURES, "canonical_and_legacy_fixture_bytes_diverge"))

    try:
        wrapper = (root / LEGACY_VALIDATOR).read_text(encoding="utf-8")
        legacy_contract = (root / LEGACY_CONTRACT).read_text(encoding="utf-8")
        canonical_contract = (root / CANONICAL_CONTRACT).read_text(encoding="utf-8")
        adr14 = (root / ADR_0014).read_text(encoding="utf-8").casefold()
        adr29 = (root / ADR_0029).read_text(encoding="utf-8").casefold()
        program_contract = (root / PROGRAM_CONTRACT).read_text(encoding="utf-8")
        program_model = (root / PROGRAM_MODEL).read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        findings.append(_finding("KFM-TAE-SHAPE-003", ".", f"required_text_unavailable:{type(exc).__name__}"))
        wrapper = legacy_contract = canonical_contract = adr14 = adr29 = program_contract = program_model = ""

    if "validate_evidence_temporal_posture_assessment" not in wrapper or "LEGACY_SCHEMA" not in wrapper:
        findings.append(_finding("KFM-TAE-COMPAT-004", LEGACY_VALIDATOR, "legacy_validator_is_not_explicit_wrapper"))
    if "compatibility" not in legacy_contract.casefold() or "EvidenceTemporalPostureAssessment" not in canonical_contract:
        findings.append(_finding("KFM-TAE-SPLIT-002", CANONICAL_CONTRACT, "responsibility_split_not_documented"))
    if "status: proposed" not in adr14 and 'status: "proposed"' not in adr14:
        findings.append(_finding("KFM-TAE-GOV-001", ADR_0014, "adr_0014_not_proposed"))
    if "accepted" not in adr29:
        findings.append(_finding("KFM-TAE-GOV-002", ADR_0029, "adr_0029_acceptance_marker_missing"))
    if COMMON_CONTRACT not in program_contract and "../common/temporal_authority_envelope.md" not in program_contract:
        findings.append(_finding("KFM-TAE-REF-001", PROGRAM_CONTRACT, "program_outcome_chain_common_binding_missing"))
    if PROGRAM_LEGACY_REFERENCE not in program_model:
        findings.append(_finding("KFM-TAE-REF-002", PROGRAM_MODEL, "fenced_historical_program_reference_changed"))
    if advisory is not None:
        properties = advisory.get("properties")
        ref = (((properties or {}).get("temporal_authority") or {}).get("$ref") if isinstance(properties, dict) else None)
        if ref != COMMON_SCHEMA_ID:
            findings.append(_finding("KFM-TAE-ADVISORY-001", ADVISORY_SCHEMA, "advisory_common_schema_ref_changed"))

    return {
        "common": {"contract": COMMON_CONTRACT, "schema": COMMON_SCHEMA, "schema_id": COMMON_SCHEMA_ID},
        "evidence_assessment": {"contract": CANONICAL_CONTRACT, "schema": CANONICAL_SCHEMA, "schema_id": CANONICAL_SCHEMA_ID, "fixture_count": len(canonical_fixtures)},
        "legacy_compatibility": {"contract": LEGACY_CONTRACT, "schema": LEGACY_SCHEMA, "schema_id": LEGACY_SCHEMA_ID, "fixture_count": len(legacy_fixtures)},
        "program_outcome_chain_reference": {"classification": "legacy_compatibility", "path": PROGRAM_MODEL, "value_sha256": _sha(PROGRAM_LEGACY_REFERENCE.encode()), "conformance_inferred": False},
    }


def _classify_reference(path: str, text: str) -> list[str]:
    roles: set[str] = set()
    if COMMON_CONTRACT in text or COMMON_SCHEMA in text or COMMON_SCHEMA_ID in text or path in KNOWN_COMMON_REFERENCE_PATHS:
        roles.add("common")
    if CANONICAL_CONTRACT in text or CANONICAL_SCHEMA in text or CANONICAL_SCHEMA_ID in text or "EvidenceTemporalPostureAssessment" in text or path.startswith(CANONICAL_FIXTURES + "/"):
        roles.add("evidence_assessment")
    if LEGACY_CONTRACT in text or LEGACY_SCHEMA in text or LEGACY_SCHEMA_ID in text or path.startswith(LEGACY_FIXTURES + "/"):
        roles.add("legacy_compatibility")
    if LEGACY_PREFIX in text:
        allowed = (
            path == PROGRAM_MODEL
            or path.startswith("data/receipts/generated/")
            or path.startswith(CANONICAL_FIXTURES + "/")
            or path.startswith(LEGACY_FIXTURES + "/")
            or path in {CANONICAL_SCHEMA, LEGACY_SCHEMA, CANONICAL_VALIDATOR, LEGACY_VALIDATOR, CANONICAL_CONTRACT, LEGACY_CONTRACT, CANONICAL_TEST, LEGACY_TEST, CANONICAL_WORKFLOW, LEGACY_WORKFLOW}
        )
        if allowed:
            roles.add("legacy_compatibility")
        elif not roles:
            roles.add("unresolved")
    if ("temporal_authority_ref" in text or "TemporalAuthorityEnvelope" in text or "temporal_authority_envelope" in text) and not roles:
        roles.add("unresolved")
    return sorted(roles)


def _inventory(root: Path) -> tuple[list[dict[str, object]], list[dict[str, str]], int]:
    references: list[dict[str, object]] = []
    gaps: list[dict[str, str]] = []
    scanned = 0
    tokens = (
        "TemporalAuthorityEnvelope", "temporal_authority_envelope",
        "EvidenceTemporalPostureAssessment", "evidence_temporal_posture_assessment",
        "temporal_authority_ref", LEGACY_PREFIX,
    )
    for path in _text_files(root):
        text, gap = _read_text(path, root)
        if gap is not None:
            gaps.append(gap)
            continue
        assert text is not None
        scanned += 1
        relative = path.relative_to(root).as_posix()
        roles = _classify_reference(relative, text)
        if not roles:
            continue
        if len(references) >= MAX_REFERENCES:
            gaps.append(_finding("KFM-TAE-SCAN-006", ".", f"reference_limit_exceeded:{MAX_REFERENCES}"))
            break
        line_numbers = [
            number for number, line in enumerate(text.splitlines(), 1)
            if any(token in line for token in tokens)
        ]
        references.append({
            "path": relative,
            "classification": roles,
            "line_numbers": line_numbers,
            "content_sha256": _sha(text.encode()),
        })
    return (
        sorted(references, key=lambda item: str(item["path"])),
        sorted(gaps, key=lambda item: (item["path"], item["code"])),
        scanned,
    )
