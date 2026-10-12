"""Core validation rules for fixture-first governed model-card envelopes.

PASS proves bounded contract conformance only. It authenticates no model,
evidence, rights, review, signature, attestation, release, publication,
deployment, or public-use authority.
"""
from __future__ import annotations

import copy
import json
import re
import sys
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
for path in (REPO_ROOT, REPO_ROOT / "packages/hashing/src"):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))
from hashing import CanonicalizationFailure, JsonInputError, compute_spec_hash, load_json_file  # noqa: E402

SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/governance/model_card_envelope.schema.json"
SCOPE = "governance.model_card_envelope"
EXIT_CODES = {"PASS": 0, "FAIL": 1, "ERROR": 2, "HOLD": 3, "DENY": 4}
SCHEMA = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
VALIDATOR = Draft202012Validator(SCHEMA, format_checker=FormatChecker())

BASELINE_TRANSFORMS = {
    "deanonymize", "expose-sensitive-coordinates", "fabricate-provenance",
    "override-governance", "publish-without-human-review",
}
KIND_TRANSFORMS = {
    "ENVIRONMENTAL_RECONSTRUCTION": {"fabricate-results", "invent-dataset-ids", "invent-license-rights"},
    "GOVERNED_NARRATIVE": {"fabricate-facts", "genealogical-inference", "invent-citations", "sacred-site-inference"},
    "SPATIAL_ALIGNMENT": set(), "DOMAIN_MODEL": set(), "OTHER": set(),
}
KIND_USES = {
    "ENVIRONMENTAL_RECONSTRUCTION": {"emergency-alerting", "forward-climate-projection", "uncited-narrative-use"},
    "GOVERNED_NARRATIVE": {"autonomous-publishing", "culturally-sensitive-reconstruction", "sensitive-heritage-narrative", "unreviewed-historical-claims"},
    "SPATIAL_ALIGNMENT": {"archaeological-precision-mapping", "cadastral-boundary-correction", "sensitive-cultural-alignment"},
    "DOMAIN_MODEL": set(), "OTHER": set(),
}
REQUIRED_ROLES = {
    "TRAINING_DATA", "TRAINING_RUN", "MODEL_RUN_RECEIPT", "UNCERTAINTY",
    "MODEL_CARD", "EVIDENCE_BUNDLE", "PROVENANCE", "OUTPUT_ARTIFACT",
    "EVALUATION_REPORT", "DRIFT_REPORT", "EXPLAINABILITY_REPORT",
    "SIGNATURE", "ATTESTATION", "SBOM", "MANIFEST", "RELEASE_MANIFEST",
    "TELEMETRY", "TELEMETRY_SCHEMA", "GOVERNANCE_POLICY", "POLICY_DECISION", "ETHICS_POLICY",
    "SOVEREIGNTY_POLICY",
}
SORTED_ARRAYS = (
    "classification.care_labels", "allowed_uses", "prohibited_uses",
    "ai_transform_permissions", "ai_transform_prohibited", "limitations",
    "governance.reason_codes",
)

@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str

@dataclass(frozen=True)
class ValidationResult:
    outcome: str
    findings: tuple[Finding, ...]
    model_card_id: str | None = None
    declared_decision: str | None = None
    declared_release_state: str | None = None


def _path(parts: Iterable[object]) -> str:
    value = "$"
    for part in parts:
        value += f"[{part}]" if isinstance(part, int) else f".{part}"
    return value


def _get(doc: Mapping[str, Any], dotted: str) -> Any:
    value: Any = doc
    for part in dotted.split("."):
        value = value[part]
    return value


def _schema_findings(doc: object) -> set[Finding]:
    errors = list(islice(VALIDATOR.iter_errors(doc), 101))
    findings = {
        Finding("SCHEMA_INVALID", _path(error.absolute_path))
        for error in errors[:100]
    }
    if len(errors) > 100:
        findings.add(Finding("SCHEMA_FINDINGS_TRUNCATED", "$"))
    return findings


def _hash_subject(doc: Mapping[str, Any]) -> dict[str, Any]:
    subject = copy.deepcopy(dict(doc)); subject.pop("spec_hash", None); return subject


def expected_spec_hash(doc: Mapping[str, Any]) -> str:
    return compute_spec_hash(_hash_subject(doc))


def _identity_findings(doc: Mapping[str, Any]) -> set[Finding]:
    model_id = str(doc["model"]["model_id"])
    version = str(doc["model"]["model_version"])
    slug = model_id.removeprefix("kfm:model:")
    expected = {
        "model_card_id": f"kfm:model-card:{slug}:v{version}",
        "document.semantic_document_id": f"kfm-modelcard-{slug.replace('.', '-')}",
        "document.doc_uuid": f"urn:kfm:modelcard:{slug}:v{version}",
        "document.event_source_id": f"urn:kfm:modelcard:{slug}",
    }
    codes = {
        "model_card_id": "MODEL_CARD_ID_MISMATCH",
        "document.semantic_document_id": "SEMANTIC_DOCUMENT_ID_MISMATCH",
        "document.doc_uuid": "DOC_UUID_MISMATCH",
        "document.event_source_id": "EVENT_SOURCE_ID_MISMATCH",
    }
    return {
        Finding(codes[path], f"$.{path}")
        for path, wanted in expected.items()
        if (doc[path] if "." not in path else _get(doc, path)) != wanted
    }


def _reference_findings(doc: Mapping[str, Any]) -> set[Finding]:
    located: list[tuple[str, Mapping[str, Any], str | None]] = [
        (f"$.bindings[{index}]", item, None)
        for index, item in enumerate(doc["bindings"])
    ]
    located.extend(
        [
            ("$.document.model_card_ref", doc["document"]["model_card_ref"], "MODEL_CARD"),
            (
                "$.reality_boundary.reality_boundary_note_ref",
                doc["reality_boundary"]["reality_boundary_note_ref"],
                "REALITY_BOUNDARY_NOTE",
            ),
        ]
    )
    for key, role in (
        ("review_record_ref", "REVIEW_RECORD"),
        ("correction_ref", "CORRECTION"),
        ("rollback_ref", "ROLLBACK"),
    ):
        value = doc["governance"][key]
        if isinstance(value, dict):
            located.append((f"$.governance.{key}", value, role))

    findings: set[Finding] = set()
    keys = [(str(item["role"]), str(item["ref"])) for item in doc["bindings"]]
    if keys != sorted(keys): findings.add(Finding("BINDINGS_NOT_SORTED", "$.bindings"))
    if len(keys) != len(set(keys)): findings.add(Finding("BINDING_DUPLICATE", "$.bindings"))
    roles = {role for role, _ in keys}
    if not REQUIRED_ROLES.issubset(roles): findings.add(Finding("REQUIRED_BINDING_ROLE_MISSING", "$.bindings"))
    if doc["governance"]["citation_required"] and "CITATION" not in roles:
        findings.add(Finding("CITATION_BINDING_REQUIRED", "$.bindings"))

    for path, item, expected_role in located:
        ref = str(item["ref"]); digest = str(item["digest"])
        if expected_role is not None and item["role"] != expected_role:
            findings.add(Finding("BINDING_ROLE_MISMATCH", f"{path}.role"))
        tail = ref.split(":", 1)[1] if ":" in ref else ref
        if "\\" in ref or "../" in ref or "/.." in ref or any(part in {".", ".."} for part in re.split(r"[/@#]", tail) if part):
            findings.add(Finding("REF_PATH_ESCAPE", f"{path}.ref"))
        upper = ref.upper()
        if any(token in upper for token in ("<", ">", "TODO", "PLACEHOLDER", "LATEST-COMMIT")):
            findings.add(Finding("REF_PLACEHOLDER_DENIED", f"{path}.ref"))
        if set(digest.removeprefix("sha256:")) == {"0"}:
            findings.add(Finding("BINDING_DIGEST_PLACEHOLDER_DENIED", f"{path}.digest"))
    return findings


def _boundary_findings(doc: Mapping[str, Any]) -> set[Finding]:
    findings: set[Finding] = set()
    for path in SORTED_ARRAYS:
        values = _get(doc, path)
        if values != sorted(values): findings.add(Finding("ARRAY_NOT_SORTED", f"$.{path}"))
    allowed, prohibited = set(doc["allowed_uses"]), set(doc["prohibited_uses"])
    permissions, blocked = set(doc["ai_transform_permissions"]), set(doc["ai_transform_prohibited"])
    if allowed & prohibited: findings.add(Finding("USE_BOUNDARY_CONFLICT", "$.allowed_uses"))
    if permissions & blocked: findings.add(Finding("TRANSFORM_PERMISSION_CONFLICT", "$.ai_transform_permissions"))
    if not BASELINE_TRANSFORMS.issubset(blocked): findings.add(Finding("BASELINE_TRANSFORM_PROHIBITION_MISSING", "$.ai_transform_prohibited"))
    kind = str(doc["model"]["model_kind"])
    if not KIND_TRANSFORMS[kind].issubset(blocked):
        findings.add(Finding("NARRATIVE_CITATION_CONTROL_MISSING" if kind == "GOVERNED_NARRATIVE" else "MODEL_KIND_TRANSFORM_BOUNDARY_MISSING", "$.ai_transform_prohibited"))
    if not KIND_USES[kind].issubset(prohibited):
        findings.add(Finding("ENVIRONMENTAL_USE_BOUNDARY_MISSING" if kind == "ENVIRONMENTAL_RECONSTRUCTION" else "MODEL_KIND_USE_BOUNDARY_MISSING", "$.prohibited_uses"))
    expected_role = "INTERPRETIVE" if kind == "GOVERNED_NARRATIVE" else "MODELED"
    if doc["reality_boundary"]["output_source_role"] != expected_role:
        findings.add(Finding("REALITY_SOURCE_ROLE_MISMATCH", "$.reality_boundary.output_source_role"))
    if kind == "GOVERNED_NARRATIVE" and not doc["governance"]["citation_required"]:
        findings.add(Finding("NARRATIVE_CITATION_CONTROL_MISSING", "$.governance.citation_required"))
    return findings


def _governance_findings(doc: Mapping[str, Any]) -> set[Finding]:
    g, c = doc["governance"], doc["classification"]
    findings: set[Finding] = set()
    if any(bool(value) for value in doc["authority_limits"].values()): findings.add(Finding("AUTHORITY_OVERCLAIM", "$.authority_limits"))
    if g["decision"] == "ALLOW" and (g["review_state"] != "APPROVED" or not g["human_review_completed"]): findings.add(Finding("ALLOW_REVIEW_INCOMPLETE", "$.governance.review_state"))
    if (g["review_state"] == "APPROVED") != bool(g["human_review_completed"]): findings.add(Finding("REVIEW_STATE_COMPLETION_MISMATCH", "$.governance.review_state"))
    if g["human_review_completed"] and g["review_record_ref"] is None: findings.add(Finding("REVIEW_RECORD_REQUIRED", "$.governance.review_record_ref"))
    if g["human_review_completed"] and g["reviewed_at"] is None: findings.add(Finding("REVIEW_TIMESTAMP_REQUIRED", "$.governance.reviewed_at"))
    sensitive = c["sensitivity"] in {"HIGH", "RESTRICTED"} or c["sovereignty_scope"] in {"APPLIES", "POSSIBLE"}
    if sensitive and not g["sovereignty_review_required"]: findings.add(Finding("SOVEREIGNTY_REVIEW_FLAG_REQUIRED", "$.governance.sovereignty_review_required"))
    if g["decision"] == "ALLOW" and sensitive and not g["sovereignty_review_completed"]: findings.add(Finding("ALLOW_SOVEREIGNTY_REVIEW_INCOMPLETE", "$.governance.sovereignty_review_completed"))
    if g["decision"] == "ALLOW" and c["rights_status"] != "VERIFIED": findings.add(Finding("ALLOW_RIGHTS_UNVERIFIED", "$.classification.rights_status"))
    if g["release_state"] == "RELEASED":
        if g["decision"] != "ALLOW": findings.add(Finding("RELEASE_DECISION_INVALID", "$.governance.decision"))
        if g["review_state"] != "APPROVED" or not g["human_review_completed"]: findings.add(Finding("RELEASE_REVIEW_REQUIRED", "$.governance.review_state"))
        if g["review_record_ref"] is None: findings.add(Finding("RELEASE_REVIEW_RECORD_REQUIRED", "$.governance.review_record_ref"))
        if g["correction_ref"] is None: findings.add(Finding("RELEASE_CORRECTION_REQUIRED", "$.governance.correction_ref"))
        if g["rollback_ref"] is None: findings.add(Finding("RELEASE_ROLLBACK_REQUIRED", "$.governance.rollback_ref"))
        if c["rights_status"] != "VERIFIED": findings.add(Finding("RELEASE_RIGHTS_UNVERIFIED", "$.classification.rights_status"))
    return findings


def _declared_outcome(doc: Mapping[str, Any]) -> str:
    g = doc["governance"]
    if g["decision"] == "DENY" or g["review_state"] == "REJECTED" or g["release_state"] == "WITHDRAWN": return "DENY"
    if g["decision"] == "HOLD" or g["review_state"] != "APPROVED" or g["release_state"] != "RELEASED" or not g["human_review_completed"]: return "HOLD"
    return "PASS"


def validate_document(doc: object) -> ValidationResult:
    schema_findings = _schema_findings(doc)
    if schema_findings or not isinstance(doc, dict): return ValidationResult("FAIL", tuple(sorted(schema_findings)))
    findings = _identity_findings(doc) | _reference_findings(doc) | _boundary_findings(doc) | _governance_findings(doc)
    try:
        if doc["spec_hash"] != expected_spec_hash(doc): findings.add(Finding("SPEC_HASH_MISMATCH", "$.spec_hash"))
    except CanonicalizationFailure:
        findings.add(Finding("SPEC_HASH_CANONICALIZATION_ERROR", "$.spec_hash"))
    g = doc["governance"]
    return ValidationResult("FAIL" if findings else _declared_outcome(doc), tuple(sorted(findings)), str(doc.get("model_card_id")), str(g.get("decision")), str(g.get("release_state")))


def validate_file(path: Path) -> ValidationResult:
    try: return validate_document(load_json_file(path))
    except JsonInputError: return ValidationResult("ERROR", (Finding("INPUT_JSON_INVALID", "$"),))


def serialize_result(result: ValidationResult) -> str:
    return json.dumps({"authority":"NONE","execution_mode":"FIXTURE_ONLY_NO_EXTERNAL_EFFECT","scope":SCOPE,"outcome":result.outcome,"model_card_id":result.model_card_id,"declared_decision":result.declared_decision,"declared_release_state":result.declared_release_state,"findings":[{"code":f.code,"path":f.path} for f in result.findings]}, sort_keys=True, separators=(",", ":"))
