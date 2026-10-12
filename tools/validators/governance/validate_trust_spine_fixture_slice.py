#!/usr/bin/env python3
"""Validate the bounded MRTS-05 synthetic trust-spine fixture slice.

The validator reads only repository-local fixture bytes, reuses declared KFM
schemas and validators, checks cross-family references and SHA-256 bindings,
and executes the existing offline promotion-verification and publication-deny
dry runs.  PASS means the fixture is internally reproducible and ready for
review.  It never activates a source, writes lifecycle state, approves a
policy or review, releases, deploys, promotes, publishes, or creates public
authority.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
import os
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators._common.local_resolver import build_registry
from tools.validators.policy.validate_policy_decision_semantics_v1 import (
    validate_payload as validate_policy_payload,
)

FIXTURE_ROOT = (
    REPO_ROOT
    / "fixtures/contracts/v1/governance/trust_spine_fixture_slice"
)
FLOW_PATH = FIXTURE_ROOT / "flow.json"
CASES_PATH = FIXTURE_ROOT / "cases.json"
SCHEMA_PATH = (
    REPO_ROOT
    / "schemas/contracts/v1/governance/trust_spine_fixture_slice.schema.json"
)
OBJECT_REGISTER = REPO_ROOT / "control_plane/object_family_register.yaml"
MAX_JSON_BYTES = 4 * 1024 * 1024
MAX_GIT_BLOB_BYTES = 8 * 1024 * 1024
SUBPROCESS_TIMEOUT_SECONDS = 45
ALLOWED_WRITER = "tools/validators/governance/validate_trust_spine_fixture_slice.py"

FAMILIES = (
    "evidence_bundle",
    "evidence_ref",
    "policy_decision",
    "promotion_receipt",
    "proof_pack",
    "release_manifest",
    "rollback_card",
    "run_receipt",
    "source_activation_decision",
    "source_descriptor",
    "validation_report",
)
LINK_REQUIREMENTS = (
    "activation_descriptor_digest",
    "activation_descriptor_identity",
    "activation_policy_decision",
    "bundle_source_descriptor",
    "evidence_ref_bundle",
    "proof_pack_component_digests",
    "proof_pack_release",
    "promotion_evidence_bundle",
    "promotion_policy_decision",
    "release_evidence_bundle",
    "release_policy_decision",
    "release_promotion_receipt",
    "release_proof_pack",
    "release_rollback_card",
    "release_run_receipt",
    "release_source_descriptor",
    "rollback_release_and_target",
    "run_source_descriptor",
    "run_validation_report",
)
CASE_EXPECTATIONS: dict[str, tuple[str, tuple[str, ...]]] = {
    "direct_public_path_attempt": ("DENY", ("DIRECT_PUBLIC_PATH_ATTEMPT",)),
    "duplicate_id": ("FAIL", ("DUPLICATE_OBJECT_ID",)),
    "incomplete_promotion_gates": ("FAIL", ("PROMOTION_GATES_INCOMPLETE",)),
    "invalid_lifecycle_placement": ("FAIL", ("LIFECYCLE_PLACEMENT_INVALID",)),
    "missing_receipt": ("FAIL", ("MISSING_RECEIPT",)),
    "missing_release_manifest": ("FAIL", ("MISSING_RELEASE_MANIFEST",)),
    "missing_rollback_target": ("FAIL", ("ROLLBACK_TARGET_MISSING",)),
    "missing_source_identity": ("FAIL", ("SOURCE_IDENTITY_MISSING",)),
    "policy_deny": ("DENY", ("POLICY_DENIED",)),
    "schema_mismatch": ("FAIL", ("SCHEMA_MISMATCH",)),
    "unauthorized_parallel_writer": ("DENY", ("UNAUTHORIZED_PARALLEL_WRITER",)),
    "unknown_rights_or_sensitivity": (
        "DENY",
        ("RIGHTS_OR_SENSITIVITY_UNKNOWN",),
    ),
    "unresolved_evidence_ref": ("FAIL", ("EVIDENCE_REF_UNRESOLVED",)),
}
DENY_CODES = frozenset(
    {
        "DIRECT_PUBLIC_PATH_ATTEMPT",
        "POLICY_DENIED",
        "RIGHTS_OR_SENSITIVITY_UNKNOWN",
        "UNAUTHORIZED_PARALLEL_WRITER",
    }
)


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str
    detail: str


@dataclass(frozen=True)
class LoadedFlow:
    packet: dict[str, Any]
    artifact_entries: dict[str, dict[str, Any]]
    objects: dict[str, dict[str, Any]]


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


def _read_json(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink() or not path.is_file():
            return None, [Finding("INPUT_NOT_REGULAR", "/", "regular file required")]
        raw = path.read_bytes()
        if len(raw) > MAX_JSON_BYTES:
            return None, [Finding("INPUT_TOO_LARGE", "/", "input exceeds 4 MiB")]
        value = json.loads(
            raw.decode("utf-8"),
            object_pairs_hook=_pairs,
            parse_constant=_nonfinite,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/", "duplicate key denied")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE", "/", "finite JSON required")]
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError, ValueError):
        return None, [Finding("JSON_INVALID", "/", "safe JSON object required")]
    if not isinstance(value, dict):
        return None, [Finding("JSON_ROOT_INVALID", "/", "object root required")]
    return value, []


def _sha256_bytes(raw: bytes) -> str:
    return "sha256:" + hashlib.sha256(raw).hexdigest()


def _sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return "sha256:" + digest.hexdigest()


def _canonical_repo_file(value: object) -> Path | None:
    if not isinstance(value, str) or not value or "\\" in value or value.startswith("/"):
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
        if not candidate.is_file():
            return None
        candidate.resolve(strict=True).relative_to(REPO_ROOT.resolve(strict=True))
    except (OSError, ValueError):
        return None
    return candidate


def _pointer(parts: Sequence[object]) -> str:
    if not parts:
        return "/"
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded)


def _schema_errors(instance: Mapping[str, Any], schema_path: Path) -> list[Finding]:
    try:
        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(
            schema,
            registry=build_registry(REPO_ROOT),
            format_checker=FormatChecker(),
        )
        errors = sorted(
            validator.iter_errors(instance),
            key=lambda error: (_pointer(tuple(error.absolute_path)), str(error.validator)),
        )
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/", "schema could not be evaluated")]
    return [
        Finding("SCHEMA_MISMATCH", _pointer(tuple(error.absolute_path)), "schema mismatch")
        for error in errors[:100]
    ]


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


def _derived_id(family: str, value: Mapping[str, Any]) -> str | None:
    field_by_family = {
        "evidence_bundle": "bundle_id",
        "evidence_ref": "ref",
        "policy_decision": "decision_id",
        "promotion_receipt": "promotion_id",
        "proof_pack": "proof_pack_id",
        "release_manifest": "release_id",
        "rollback_card": "id",
        "run_receipt": "run_id",
        "source_activation_decision": "activation_decision_id",
        "validation_report": "id",
    }
    if family == "source_descriptor":
        source_id = value.get("source_id")
        version = value.get("descriptor_version")
        if isinstance(source_id, str) and isinstance(version, str):
            return f"source-descriptor:{source_id}:{version}"
        return None
    field = field_by_family.get(family)
    raw = value.get(field) if field else None
    return raw if isinstance(raw, str) else None


def _load_flow() -> tuple[LoadedFlow | None, tuple[Finding, ...]]:
    packet, findings = _read_json(FLOW_PATH)
    if packet is None:
        return None, tuple(findings)
    findings.extend(_schema_errors(packet, SCHEMA_PATH))
    if findings:
        return None, tuple(sorted(set(findings)))

    artifacts = packet.get("artifacts")
    if not isinstance(artifacts, list):
        return None, (Finding("ARTIFACT_SET_INVALID", "/artifacts", "artifact set invalid"),)
    family_order = [item.get("family_id") for item in artifacts if isinstance(item, dict)]
    if tuple(family_order) != FAMILIES:
        findings.append(Finding("ARTIFACT_SET_INVALID", "/artifacts", "family set or order invalid"))
    if tuple(packet.get("link_requirements", ())) != LINK_REQUIREMENTS:
        findings.append(Finding("LINK_PROFILE_INVALID", "/link_requirements", "link profile invalid"))
    if tuple(packet.get("required_negative_cases", ())) != tuple(CASE_EXPECTATIONS):
        findings.append(Finding("CASE_PROFILE_INVALID", "/required_negative_cases", "case profile invalid"))

    entries: dict[str, dict[str, Any]] = {}
    objects: dict[str, dict[str, Any]] = {}
    for item in artifacts:
        if not isinstance(item, dict) or not isinstance(item.get("family_id"), str):
            continue
        family = item["family_id"]
        path = _canonical_repo_file(item.get("path"))
        schema = _canonical_repo_file(item.get("schema_path"))
        if path is None or schema is None:
            findings.append(Finding("ARTIFACT_PATH_INVALID", f"/artifacts/{family}", "safe file required"))
            continue
        expected_digest = item.get("sha256")
        if _sha256_file(path) != expected_digest:
            findings.append(Finding("ARTIFACT_DIGEST_MISMATCH", f"/artifacts/{family}", "artifact digest mismatch"))
            continue
        value, read_findings = _read_json(path)
        if value is None:
            findings.extend(read_findings)
            continue
        derived = _derived_id(family, value)
        if derived != item.get("object_id"):
            findings.append(Finding("OBJECT_ID_MISMATCH", f"/artifacts/{family}", "declared identity mismatch"))
        entries[family] = item
        objects[family] = value

    for section in (packet.get("governing_refs"),):
        if not isinstance(section, list):
            continue
        for index, item in enumerate(section):
            if not isinstance(item, dict):
                continue
            path = item.get("path")
            digest = item.get("sha256")
            if not isinstance(path, str) or not isinstance(digest, str):
                continue
            raw = _git_blob(str(packet.get("base_ref")), path)
            if raw is None:
                findings.append(Finding("PINNED_REF_UNRESOLVED", f"/governing_refs/{index}", "pinned blob unavailable"))
            elif _sha256_bytes(raw) != digest:
                findings.append(Finding("PINNED_REF_DIGEST_MISMATCH", f"/governing_refs/{index}", "pinned blob digest mismatch"))

    dry_run = packet.get("dry_run")
    if isinstance(dry_run, dict):
        for name in ("promotion_verification_plan", "publication_deny_tool"):
            item = dry_run.get(name)
            if not isinstance(item, dict):
                continue
            path = _canonical_repo_file(item.get("path"))
            if path is None or _sha256_file(path) != item.get("sha256"):
                findings.append(Finding("DRY_RUN_REF_MISMATCH", f"/dry_run/{name}", "dry-run reference mismatch"))

    register, register_findings = _read_json(OBJECT_REGISTER)
    if register is None:
        findings.extend(register_findings)
    else:
        registered = {
            item.get("family_id"): item
            for item in register.get("entries", [])
            if isinstance(item, dict) and isinstance(item.get("family_id"), str)
        }
        for family, entry in entries.items():
            registered_entry = registered.get(family)
            identity = registered_entry.get("identity") if isinstance(registered_entry, dict) else None
            expected_status = identity.get("status") if isinstance(identity, dict) else None
            if entry.get("registry_identity_status") != expected_status:
                findings.append(Finding("REGISTRY_IDENTITY_STATUS_MISMATCH", f"/artifacts/{family}", "registry identity status mismatch"))
            expected_binding = (
                "CONFLICTED_CANDIDATE_PIN"
                if expected_status == "CONFLICTED"
                else "SINGLE_SURFACE_FIXTURE_PIN"
            )
            if entry.get("candidate_binding") != expected_binding:
                findings.append(Finding("CANDIDATE_BINDING_MISMATCH", f"/artifacts/{family}", "fixture candidate binding mismatch"))

    loaded = LoadedFlow(packet, entries, objects)
    return (loaded if not findings else None), tuple(sorted(set(findings)))


def _outcome(codes: Sequence[str]) -> str:
    if not codes:
        return "PASS"
    return "DENY" if any(code in DENY_CODES for code in codes) else "FAIL"


def _evaluate_objects(
    loaded: LoadedFlow,
    objects: Mapping[str, dict[str, Any]],
    controls: Mapping[str, Any],
) -> tuple[str, tuple[str, ...]]:
    descriptor = objects.get("source_descriptor")
    if not isinstance(descriptor, dict) or _derived_id("source_descriptor", descriptor) is None:
        return "FAIL", ("SOURCE_IDENTITY_MISSING",)
    if "run_receipt" not in objects or "promotion_receipt" not in objects:
        return "FAIL", ("MISSING_RECEIPT",)
    if "release_manifest" not in objects:
        return "FAIL", ("MISSING_RELEASE_MANIFEST",)
    rollback = objects.get("rollback_card")
    target = rollback.get("target") if isinstance(rollback, dict) else None
    if not isinstance(target, dict) or not isinstance(target.get("release_ref"), str):
        return "FAIL", ("ROLLBACK_TARGET_MISSING",)

    promotion = objects["promotion_receipt"]
    gates = promotion.get("gates")
    gate_ids = [item.get("gate") for item in gates if isinstance(item, dict)] if isinstance(gates, list) else []
    gate_statuses = [item.get("status") for item in gates if isinstance(item, dict)] if isinstance(gates, list) else []
    if gate_ids != list("ABCDEFG") or gate_statuses != ["PASS"] * 7:
        return "FAIL", ("PROMOTION_GATES_INCOMPLETE",)

    release = objects["release_manifest"]
    if (
        release.get("execution_mode") != "FIXTURE_ONLY"
        or release.get("lifecycle_state") != "CANDIDATE"
        or release.get("release_state") != "CANDIDATE"
    ):
        return "FAIL", ("LIFECYCLE_PLACEMENT_INVALID",)

    release_governance = release.get("governance")
    public_attempt = (
        controls.get("publication_attempted") is not False
        or controls.get("publication_created") is not False
        or controls.get("public_route") is not None
        or promotion.get("transition", {}).get("applied") is not False
        or (
            isinstance(release_governance, dict)
            and any(value is not False for value in release_governance.values())
        )
    )
    if public_attempt:
        return "DENY", ("DIRECT_PUBLIC_PATH_ATTEMPT",)
    if controls.get("writer_path") != ALLOWED_WRITER:
        return "DENY", ("UNAUTHORIZED_PARALLEL_WRITER",)

    bundle = objects.get("evidence_bundle")
    sensitivity = bundle.get("sensitivity") if isinstance(bundle, dict) else None
    rights = descriptor.get("rights")
    if (
        not isinstance(rights, dict)
        or rights.get("rights_status") != "verified_open"
        or descriptor.get("sensitivity_default") != "public"
        or not isinstance(sensitivity, dict)
        or sensitivity.get("level") != "public"
    ):
        return "DENY", ("RIGHTS_OR_SENSITIVITY_UNKNOWN",)

    policy = objects.get("policy_decision")
    if isinstance(policy, dict) and policy.get("outcome") == "DENY":
        return "DENY", ("POLICY_DENIED",)

    identities = [
        identity
        for family, value in objects.items()
        if (identity := _derived_id(family, value)) is not None
    ]
    if len(identities) != len(set(identities)):
        return "FAIL", ("DUPLICATE_OBJECT_ID",)

    evidence_ref = objects.get("evidence_ref")
    if (
        not isinstance(evidence_ref, dict)
        or not isinstance(bundle, dict)
        or evidence_ref.get("bundle_ref") != bundle.get("bundle_id")
        or not isinstance(bundle.get("evidence_refs"), list)
        or evidence_ref not in bundle["evidence_refs"]
    ):
        return "FAIL", ("EVIDENCE_REF_UNRESOLVED",)

    schema_findings: list[Finding] = []
    for family, value in objects.items():
        entry = loaded.artifact_entries.get(family)
        schema_path = _canonical_repo_file(entry.get("schema_path")) if entry else None
        if schema_path is None:
            schema_findings.append(Finding("SCHEMA_UNAVAILABLE", "/", "schema unavailable"))
        else:
            schema_findings.extend(_schema_errors(value, schema_path))
    if schema_findings:
        return "FAIL", ("SCHEMA_MISMATCH",)

    if not isinstance(policy, dict) or policy.get("outcome") != "ANSWER":
        return "FAIL", ("POLICY_ALLOW_MISSING",)
    policy_result = validate_policy_payload(policy)
    if not policy_result.ok:
        return "FAIL", ("POLICY_SEMANTICS_INVALID",)

    activation = objects["source_activation_decision"]
    descriptor_ref = _derived_id("source_descriptor", descriptor)
    descriptor_entry = loaded.artifact_entries["source_descriptor"]
    if (
        activation.get("source_id") != descriptor.get("source_id")
        or activation.get("descriptor_version") != descriptor.get("descriptor_version")
        or activation.get("source_descriptor_ref") != descriptor_ref
        or activation.get("source_descriptor_digest") != descriptor_entry.get("sha256")
    ):
        return "FAIL", ("ACTIVATION_DESCRIPTOR_BINDING_INVALID",)
    activation_decision = activation.get("decision")
    if (
        not isinstance(activation_decision, dict)
        or policy.get("decision_id") not in activation_decision.get("policy_decision_refs", [])
    ):
        return "FAIL", ("ACTIVATION_POLICY_BINDING_INVALID",)
    if descriptor_ref not in bundle.get("source_records", []):
        return "FAIL", ("BUNDLE_SOURCE_BINDING_INVALID",)

    run = objects["run_receipt"]
    validation = objects["validation_report"]
    if descriptor_ref not in run.get("source_descriptor_refs", []):
        return "FAIL", ("RUN_SOURCE_BINDING_INVALID",)
    if validation.get("id") not in run.get("validation_refs", []):
        return "FAIL", ("RUN_VALIDATION_BINDING_INVALID",)
    if bundle.get("bundle_id") not in promotion.get("evidence_refs", []):
        return "FAIL", ("PROMOTION_EVIDENCE_BINDING_INVALID",)
    if policy.get("decision_id") not in promotion.get("policy_refs", []):
        return "FAIL", ("PROMOTION_POLICY_BINDING_INVALID",)

    proof = objects["proof_pack"]
    release_id = release.get("release_id")
    rollback_id = rollback.get("id") if isinstance(rollback, dict) else None
    required_release_bindings = (
        descriptor_ref in release.get("source_descriptor_refs", [])
        and bundle.get("bundle_id") in release.get("evidence_bundle_refs", [])
        and policy.get("decision_id") in release.get("policy_decision_refs", [])
        and run.get("run_id") in release.get("receipt_refs", [])
        and promotion.get("promotion_id") in release.get("receipt_refs", [])
        and proof.get("proof_pack_id") in release.get("proof_refs", [])
        and isinstance(release.get("lineage"), dict)
        and release["lineage"].get("rollback_ref") == rollback_id
    )
    if not required_release_bindings:
        return "FAIL", ("RELEASE_REFERENCE_CLOSURE_INVALID",)
    if proof.get("release_id") != release_id:
        return "FAIL", ("PROOF_RELEASE_BINDING_INVALID",)
    if (
        not isinstance(rollback, dict)
        or rollback.get("affected_release_ref") != release_id
        or target.get("release_ref") == release_id
    ):
        return "FAIL", ("ROLLBACK_RELEASE_BINDING_INVALID",)

    if any(
        controls.get(name) is not expected
        for name, expected in {
            "fixture_only": True,
            "network_used": False,
            "source_activated": False,
            "lifecycle_write": False,
            "release_authorized": False,
            "promotion_authorized": False,
        }.items()
    ):
        return "FAIL", ("CONTROL_BOUNDARY_VIOLATION",)
    return "PASS", ()


def _mutate(
    case_id: str,
    objects: dict[str, dict[str, Any]],
    controls: dict[str, Any],
) -> None:
    if case_id == "direct_public_path_attempt":
        controls["publication_attempted"] = True
    elif case_id == "duplicate_id":
        objects["validation_report"]["id"] = objects["run_receipt"]["run_id"]
    elif case_id == "incomplete_promotion_gates":
        objects["promotion_receipt"]["gates"] = objects["promotion_receipt"]["gates"][:-1]
    elif case_id == "invalid_lifecycle_placement":
        objects["release_manifest"]["lifecycle_state"] = "RELEASED"
        objects["release_manifest"]["release_state"] = "RELEASED"
    elif case_id == "missing_receipt":
        del objects["run_receipt"]
    elif case_id == "missing_release_manifest":
        del objects["release_manifest"]
    elif case_id == "missing_rollback_target":
        objects["rollback_card"]["target"] = {}
    elif case_id == "missing_source_identity":
        del objects["source_descriptor"]["source_id"]
    elif case_id == "policy_deny":
        policy = objects["policy_decision"]
        policy["outcome"] = "DENY"
        policy["reasons"] = ["RIGHTS_UNKNOWN"]
        policy["obligations"] = []
    elif case_id == "schema_mismatch":
        objects["validation_report"]["version"] = 7
    elif case_id == "unauthorized_parallel_writer":
        controls["writer_path"] = "runtime/publication/parallel_writer.py"
    elif case_id == "unknown_rights_or_sensitivity":
        objects["source_descriptor"]["rights"]["rights_status"] = "unknown"
    elif case_id == "unresolved_evidence_ref":
        objects["evidence_ref"]["bundle_ref"] = "evidence-bundle:fixture:missing"
    else:
        raise ValueError("unknown bounded fixture case")


def _load_cases() -> tuple[dict[str, tuple[str, tuple[str, ...]]] | None, tuple[Finding, ...]]:
    value, findings = _read_json(CASES_PATH)
    if value is None:
        return None, tuple(findings)
    cases = value.get("cases")
    parsed: dict[str, tuple[str, tuple[str, ...]]] = {}
    if value.get("schema_version") != "kfm.trust-spine-fixture-slice-cases.v1" or not isinstance(cases, list):
        return None, (Finding("CASE_MANIFEST_INVALID", "/", "case manifest invalid"),)
    for item in cases:
        if not isinstance(item, dict):
            return None, (Finding("CASE_MANIFEST_INVALID", "/cases", "case entry invalid"),)
        case_id = item.get("case_id")
        outcome = item.get("expected_outcome")
        codes = item.get("expected_codes")
        if not isinstance(case_id, str) or not isinstance(outcome, str) or not isinstance(codes, list):
            return None, (Finding("CASE_MANIFEST_INVALID", "/cases", "case entry invalid"),)
        parsed[case_id] = (outcome, tuple(code for code in codes if isinstance(code, str)))
    if parsed != CASE_EXPECTATIONS or tuple(parsed) != tuple(CASE_EXPECTATIONS):
        return None, (Finding("CASE_MANIFEST_INVALID", "/cases", "exact case contract mismatch"),)
    return parsed, ()


def _run_command(command: Sequence[str]) -> tuple[int | None, str]:
    env = os.environ.copy()
    env.update(
        {
            "KFM_NO_NETWORK": "1",
            "PYTHONHASHSEED": "0",
            "PYTHONDONTWRITEBYTECODE": "1",
            "PYTHONUNBUFFERED": "1",
            "TZ": "UTC",
        }
    )
    try:
        completed = subprocess.run(
            list(command),
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
            env=env,
            timeout=SUBPROCESS_TIMEOUT_SECONDS,
        )
    except (OSError, subprocess.TimeoutExpired):
        return None, ""
    return completed.returncode, completed.stdout


def _canonical_lanes() -> tuple[dict[str, str], tuple[Finding, ...]]:
    artifact = "fixtures/contracts/v1/governance/trust_spine_fixture_slice/artifacts"
    commands: tuple[tuple[str, tuple[str, ...]], ...] = (
        ("source_descriptor", (sys.executable, "tools/validators/validate_source_descriptor.py", f"{artifact}/source_descriptor.json")),
        ("source_activation_decision", (sys.executable, "tools/validators/validate_source_activation_decision.py", f"{artifact}/source_activation_decision.json")),
        ("evidence_ref", (sys.executable, "tools/validators/validate_evidence_ref.py", f"{artifact}/evidence_ref.json")),
        ("evidence_bundle", (sys.executable, "tools/validators/validate_evidence_bundle.py", f"{artifact}/evidence_bundle.json")),
        ("policy_decision", (sys.executable, "tools/validators/policy/validate_policy_decision_semantics_v1.py", f"{artifact}/policy_decision_allow.json")),
        ("run_receipt", (sys.executable, "tools/validators/validate_run_receipt.py", f"{artifact}/run_receipt.json")),
        ("promotion_receipt", (sys.executable, "tools/validators/release/validate_promotion_receipt.py", f"{artifact}/promotion_receipt.json")),
        ("release_manifest", (sys.executable, "tools/validators/release/validate_release_manifest.py", f"{artifact}/release_manifest.json")),
        ("proof_pack", (sys.executable, "tools/proof_pack/proof_pack_check.py", f"{artifact}/proof_pack.json", "--repo-root", ".")),
        ("rollback_card", (sys.executable, "tools/validators/release/validate_rollback_card.py", f"{artifact}/rollback_card.json")),
    )
    outcomes: dict[str, str] = {}
    findings: list[Finding] = []
    for lane, command in commands:
        returncode, _stdout = _run_command(command)
        outcomes[lane] = "PASS" if returncode == 0 else ("NOT_RUN" if returncode is None else "FAIL")
        if returncode is None:
            findings.append(Finding("CANONICAL_LANE_NOT_RUN", f"/lanes/{lane}", "canonical lane did not run"))
        elif returncode != 0:
            findings.append(Finding("CANONICAL_LANE_FAILED", f"/lanes/{lane}", "canonical lane failed"))
    return outcomes, tuple(sorted(findings))


def _dry_runs() -> tuple[dict[str, Any], tuple[Finding, ...]]:
    fixture = "fixtures/release/promotion_verification_execution"
    command = (
        sys.executable,
        "tools/validators/promotion_gate/execute_promotion_verification.py",
        f"{fixture}/valid/pass.json",
        "--repo-root",
        ".",
        "--cosign-bin",
        f"{fixture}/bin/fake_cosign.py",
        "--conftest-bin",
        f"{fixture}/bin/fake_conftest.py",
        "--promotion-validator",
        f"{fixture}/bin/fake_promotion_validator.py",
        "--cosign-plan-validator",
        f"{fixture}/bin/fake_cosign_plan_validator.py",
    )
    findings: list[Finding] = []
    code, stdout = _run_command(command)
    try:
        promotion = json.loads(stdout) if code == 0 else None
    except json.JSONDecodeError:
        promotion = None
    expected_authority = {
        "deployment_authorized": False,
        "lifecycle_write": False,
        "promotion_authorized": False,
        "publication_authorized": False,
        "release_authorized": False,
    }
    if (
        not isinstance(promotion, dict)
        or promotion.get("status") != "PASS"
        or promotion.get("readiness") != "APPROVE_READY"
        or promotion.get("authority") != expected_authority
    ):
        findings.append(Finding("PROMOTION_DRY_RUN_FAILED", "/dry_run/promotion", "promotion dry run failed"))

    deny_code, deny_stdout = _run_command((sys.executable, "tools/release/release_dry_run.py"))
    try:
        denial = json.loads(deny_stdout) if deny_code == 0 else None
    except json.JSONDecodeError:
        denial = None
    if (
        not isinstance(denial, dict)
        or denial.get("dry_run_status") != "PASS"
        or denial.get("publication_created") is not False
        or denial.get("network_used") is not False
        or denial.get("case_count") != 5
    ):
        findings.append(Finding("PUBLICATION_DENY_DRY_RUN_FAILED", "/dry_run/publication", "publication-deny dry run failed"))

    return (
        {
            "promotion_verification": "PASS" if not any(item.code == "PROMOTION_DRY_RUN_FAILED" for item in findings) else "FAIL",
            "readiness": "APPROVE_READY" if isinstance(promotion, dict) and promotion.get("readiness") == "APPROVE_READY" else "BLOCKED",
            "publication_deny": "PASS" if not any(item.code == "PUBLICATION_DENY_DRY_RUN_FAILED" for item in findings) else "FAIL",
            "publication_created": False,
        },
        tuple(sorted(findings)),
    )


def validate_current() -> tuple[dict[str, Any], LoadedFlow | None]:
    loaded, load_findings = _load_flow()
    findings = list(load_findings)
    lanes: dict[str, str] = {}
    dry_run: dict[str, Any] = {
        "promotion_verification": "NOT_RUN",
        "readiness": "BLOCKED",
        "publication_deny": "NOT_RUN",
        "publication_created": False,
    }
    object_outcome = "FAIL"
    object_codes: tuple[str, ...] = ()
    if loaded is not None:
        controls = loaded.packet.get("controls")
        assert isinstance(controls, dict)
        object_outcome, object_codes = _evaluate_objects(loaded, loaded.objects, controls)
        findings.extend(Finding(code, "/flow", "cross-family flow invalid") for code in object_codes)
        lanes, lane_findings = _canonical_lanes()
        findings.extend(lane_findings)
        dry_run, dry_findings = _dry_runs()
        findings.extend(dry_findings)

    ordered = tuple(sorted(set(findings)))
    report = {
        "artifact_count": len(loaded.objects) if loaded is not None else 0,
        "artifact_set_digest": (
            _sha256_bytes(
                json.dumps(
                    {family: loaded.artifact_entries[family]["sha256"] for family in FAMILIES},
                    sort_keys=True,
                    separators=(",", ":"),
                ).encode("utf-8")
            )
            if loaded is not None
            else None
        ),
        "authority": {
            "lifecycle_write": False,
            "promotion_authorized": False,
            "publication_authorized": False,
            "release_authorized": False,
            "source_activated": False,
        },
        "canonical_lanes": lanes,
        "case_count": len(CASE_EXPECTATIONS),
        "dry_run": dry_run,
        "findings": [
            {"code": item.code, "field": item.field, "detail": item.detail}
            for item in ordered
        ],
        "flow_digest": _sha256_file(FLOW_PATH) if loaded is not None else None,
        "network_used": False,
        "outcome": "PASS" if not ordered and object_outcome == "PASS" else "FAIL",
        "publication_outcome": "NOT_ATTEMPTED",
        "readiness": "READY_FOR_REVIEW" if not ordered and object_outcome == "PASS" else "BLOCKED",
        "scope": "synthetic-cross-family-fixture-only-no-network",
    }
    return report, loaded


def run_fixtures() -> int:
    report, loaded = validate_current()
    cases, case_findings = _load_cases()
    if report["outcome"] != "PASS" or loaded is None or cases is None or case_findings:
        print(json.dumps({"outcome": "ERROR", "reason_code": "BASE_OR_CASE_PROFILE_INVALID"}, sort_keys=True, separators=(",", ":")))
        return 2
    controls = loaded.packet.get("controls")
    assert isinstance(controls, dict)
    failed = False
    for case_id, expected in cases.items():
        objects = copy.deepcopy(loaded.objects)
        mutated_controls = copy.deepcopy(controls)
        _mutate(case_id, objects, mutated_controls)
        observed_outcome, observed_codes = _evaluate_objects(loaded, objects, mutated_controls)
        suite_match = (observed_outcome, observed_codes) == expected
        failed = failed or not suite_match
        print(
            json.dumps(
                {
                    "case_id": case_id,
                    "finding_codes": list(observed_codes),
                    "outcome": observed_outcome,
                    "suite_match": suite_match,
                },
                sort_keys=True,
                separators=(",", ":"),
            )
        )
    return 1 if failed else 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixtures", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    if args.fixtures:
        return run_fixtures()
    report, _loaded = validate_current()
    print(json.dumps(report, sort_keys=True, separators=(",", ":")))
    return 0 if report["outcome"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
