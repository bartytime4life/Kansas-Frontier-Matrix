"""Synthetic conformance and approval-boundary tests; no real source admission."""
from copy import deepcopy
from datetime import datetime, timezone
import json
import sqlite3

import pytest
from jsonschema import Draft202012Validator, FormatChecker
from connectors_core.captured_json import canonical_bytes, digest_bytes
from hashing import compute_spec_hash
from pipelines.domains.hydrology.normalize import normalize_capture
from pipelines.domains.hydrology.package import prepare_water_package
from release.core import validate_snapshot
from release.local_store import LocalReleaseStore
from release.water_projection import project
from tests.domains.hydrology.test_usgs_water_normalizer import acquired, ROOT
from tools.validators._common.local_resolver import build_registry

NOW = "2026-09-30T19:00:00Z"


def synthetic_snapshot(*, cleared=False, mutate=lambda records: records):
    raw = acquired(mutate)
    snapshot = prepare_water_package(normalize_capture(raw.manifest, raw.objects))
    if cleared:
        # Explicitly synthetic clearance. Never applied to captured real bytes.
        evidence = json.loads(snapshot["artifacts"]["evidence.json"])
        for entry in evidence["entries"]:
            bundle = entry["bundle"]
            bundle["sensitivity"] = {"level": "public", "reason": "SYNTHETIC TEST ONLY", "applied_at": NOW}
            bundle["rights"] = {"license": "SYNTHETIC TEST ONLY - no real rights grant"}
            bundle["spec_hash"] = {"value": compute_spec_hash({k: v for k, v in bundle.items() if k != "spec_hash"})}
        snapshot["artifacts"]["evidence.json"] = canonical_bytes(evidence).decode()
        snapshot["manifest"]["artifacts"]["evidence.json"] = digest_bytes(snapshot["artifacts"]["evidence.json"].encode())
        snapshot["manifest"]["package_id"] = compute_spec_hash({k: v for k, v in snapshot["manifest"].items() if k != "package_id"})
    return snapshot


def synthetic_decision(snapshot):
    result = {"profile": "kfm.water-release-decision/v1", "package_id": snapshot["manifest"]["package_id"],
              "decision": "APPROVED", "reviewed_at": "2026-09-30T18:30:00Z", "released_at": "2026-09-30T18:45:00Z",
              "expires_at": "2026-10-01T00:00:00Z", "correction_state": "ACTIVE", "correction_ref": None,
              "reviewer": "synthetic-reviewer", "releaser": "synthetic-releaser"}
    for name in ("source_admission", "rights", "sensitivity", "policy", "review", "release"):
        result[name + "_ref"] = "kfm://synthetic/" + name
    return result


def test_real_preparation_never_self_approves():
    snapshot = synthetic_snapshot()
    for decision in [None, synthetic_decision(snapshot)]:
        response = project(canonical_bytes(snapshot), decision, view="layers", now=NOW)
        assert response["envelope"]["outcome"] == "ABSTAIN"
        assert "data" not in response


@pytest.mark.parametrize("view", ["bootstrap", "layers", "evidence"])
def test_synthetic_released_projection_satisfies_closed_envelope(view):
    snapshot = synthetic_snapshot(cleared=True)
    response = project(canonical_bytes(snapshot), synthetic_decision(snapshot), view=view, now=NOW)
    assert response["envelope"]["outcome"] == "ANSWER"
    assert "data" in response and "data" not in response["envelope"]
    schema = json.loads((ROOT / "schemas/contracts/v1/runtime/runtime_response_envelope.schema.json").read_text())
    Draft202012Validator(schema, registry=build_registry(ROOT), format_checker=FormatChecker()).validate(response["envelope"])


def test_null_discharge_does_not_refresh_served_measurements():
    def old_value_then_recent_null(records):
        old = deepcopy(records[0])
        old["properties"]["time"] = "2026-09-29T18:00:00Z"
        old["properties"]["last_modified"] = "2026-09-29T18:00:01Z"
        records[0]["properties"]["value"] = None
        return [old, records[0]]

    snapshot = synthetic_snapshot(cleared=True, mutate=old_value_then_recent_null)
    response = project(canonical_bytes(snapshot), synthetic_decision(snapshot), view="layers", now=NOW)
    assert response["envelope"]["outcome"] == "ANSWER"
    assert response["envelope"]["freshness"] == "stale-accepted"
    assert response["envelope"]["precision_actually_used"]["temporal"]["freshness_class"] == "stale-accepted"
    assert any(record["value"] is None for record in response["data"]["observations"])

    def only_null(records):
        records[0]["properties"]["value"] = None
        return records

    empty = synthetic_snapshot(cleared=True, mutate=only_null)
    response = project(canonical_bytes(empty), synthetic_decision(empty), view="layers", now=NOW)
    assert response["envelope"]["outcome"] == "ANSWER"
    assert response["envelope"]["freshness"] == "unknown"
    assert response["data"]["coverage"] == "EMPTY"


@pytest.mark.parametrize("change,reason", [
    ({"rights_ref": None}, "REVIEW_REFERENCE_MISSING"),
    ({"reviewer": "synthetic-releaser"}, "INDEPENDENT_REVIEW_REQUIRED"),
    ({"package_id": "sha256:" + "a"*64}, "RELEASE_BINDING_MISMATCH"),
    ({"correction_state": "WITHDRAWN"}, "CORRECTION_HOLD"),
    ({"correction_state": "SUPERSEDED"}, "CORRECTION_HOLD"),
    ({"expires_at": "2026-09-30T18:59:59Z"}, "RELEASE_TIME_INVALID"),
    ({"expires_at": "2026-09-31T00:00:00Z"}, "RELEASE_TIME_INVALID"),
    ({"released_at": "2026-10-01T00:00:00Z"}, "RELEASE_TIME_INVALID"),
])
def test_missing_review_tampered_binding_correction_and_expiry_withhold_data(change, reason):
    snapshot = synthetic_snapshot(cleared=True)
    decision = {**synthetic_decision(snapshot), **change}
    response = project(canonical_bytes(snapshot), decision, view="layers", now=NOW)
    assert response["envelope"]["reason_code"] == reason
    assert "data" not in response


def test_artifact_tampering_and_extra_paths_fail():
    snapshot = synthetic_snapshot()
    snapshot["artifacts"]["candidate.json"] += " "
    with pytest.raises(ValueError, match="ARTIFACT_DIGEST"):
        validate_snapshot(canonical_bytes(snapshot))
    snapshot = synthetic_snapshot()
    snapshot["artifacts"]["../../private"] = "{}"
    with pytest.raises(ValueError, match="ARTIFACT_CLOSURE"):
        validate_snapshot(canonical_bytes(snapshot))


def test_local_store_only_reads_trusted_activation_and_immutable_object(tmp_path):
    root = tmp_path / "serving"
    root.mkdir(mode=0o700)
    (root / "objects").mkdir()
    snapshot = synthetic_snapshot(cleared=True)
    decision = synthetic_decision(snapshot)
    package_id = snapshot["manifest"]["package_id"]
    path = root / "objects" / (package_id.split(":")[1] + ".json")
    path.write_bytes(canonical_bytes(snapshot))
    with sqlite3.connect(root / "activation.sqlite") as db:
        db.execute("CREATE TABLE water_packages(package_id TEXT, state TEXT)")
        db.execute("INSERT INTO water_packages VALUES(?,?)", (package_id, "STAGED"))
        db.execute("CREATE TABLE water_active(singleton INTEGER PRIMARY KEY, package_id TEXT, decision_json TEXT)")
        db.execute("INSERT INTO water_active VALUES(1,?,?)", (package_id, json.dumps(decision)))
    assert project(*LocalReleaseStore(str(root)).active(), view="layers", now=NOW)["envelope"]["outcome"] == "ANSWER"
    path.unlink()
    path.symlink_to(root / "activation.sqlite")
    with pytest.raises(ValueError, match="SYMLINK"):
        LocalReleaseStore(str(root)).active()


def reseal_evidence(snapshot, evidence):
    snapshot["artifacts"]["evidence.json"] = canonical_bytes(evidence).decode()
    snapshot["manifest"]["artifacts"]["evidence.json"] = digest_bytes(snapshot["artifacts"]["evidence.json"].encode())
    snapshot["manifest"]["package_id"] = compute_spec_hash({k: v for k, v in snapshot["manifest"].items() if k != "package_id"})


def reseal_validation(snapshot, validation):
    validation["receipt_digest"] = digest_bytes(canonical_bytes({k: v for k, v in validation.items() if k != "receipt_digest"}))
    evidence = json.loads(snapshot["artifacts"]["evidence.json"])
    for entry in evidence["entries"]:
        bundle = entry["bundle"]
        bundle["checksums"]["validation"] = validation["receipt_digest"]
        bundle["spec_hash"] = {"value": compute_spec_hash({k: v for k, v in bundle.items() if k != "spec_hash"})}
    snapshot["artifacts"]["validation.json"] = canonical_bytes(validation).decode()
    snapshot["manifest"]["artifacts"]["validation.json"] = digest_bytes(snapshot["artifacts"]["validation.json"].encode())
    reseal_evidence(snapshot, evidence)


def test_staging_replays_validation_receipt_before_writing(tmp_path):
    from release.local_admin import stage

    snapshot = synthetic_snapshot(cleared=True)
    validation = json.loads(snapshot["artifacts"]["validation.json"])
    validation["release_authorized"] = True
    reseal_validation(snapshot, validation)
    raw = canonical_bytes(snapshot)
    # All carrier hashes and references are consistent; only replay exposes the lie.
    validate_snapshot(raw)
    root = tmp_path / "uncreated-release-store"
    with pytest.raises(ValueError, match="VALIDATION_RECEIPT_MISMATCH"):
        stage(root, raw, actor="synthetic-owner", now=NOW)
    assert not root.exists()


def test_staging_revalidates_fully_resealed_candidate(tmp_path):
    from evidence_resolver.verification_history import canonical_spec_hash
    from release.local_admin import stage

    snapshot = synthetic_snapshot(cleared=True)
    candidate = json.loads(snapshot["artifacts"]["candidate.json"])
    old_id = candidate["candidate_id"]
    candidate["stale_after_seconds"] = 3600
    candidate["candidate_id"] = digest_bytes(canonical_bytes({k: v for k, v in candidate.items() if k != "candidate_id"}))
    new_id = candidate["candidate_id"]
    snapshot["artifacts"]["candidate.json"] = canonical_bytes(candidate).decode()
    snapshot["manifest"]["artifacts"]["candidate.json"] = digest_bytes(snapshot["artifacts"]["candidate.json"].encode())
    snapshot["manifest"]["candidate_id"] = new_id

    validation = json.loads(snapshot["artifacts"]["validation.json"])
    validation["candidate_id"] = new_id
    validation["receipt_digest"] = digest_bytes(canonical_bytes({k: v for k, v in validation.items() if k != "receipt_digest"}))
    catalog = json.loads(snapshot["artifacts"]["catalog.json"])
    catalog["candidate_id"] = new_id
    for entry in catalog["entries"]:
        entry["evidence_ref"] = entry["evidence_ref"].replace(old_id.split(":")[1], new_id.split(":")[1])
        entry["validation_ref"] = validation["receipt_digest"]
    snapshot["artifacts"]["catalog.json"] = canonical_bytes(catalog).decode()
    snapshot["manifest"]["artifacts"]["catalog.json"] = digest_bytes(snapshot["artifacts"]["catalog.json"].encode())

    evidence = json.loads(snapshot["artifacts"]["evidence.json"])
    evidence["candidate_id"] = new_id
    for entry in evidence["entries"]:
        bundle = entry["bundle"]
        bundle["bundle_id"] = bundle["bundle_id"].replace(old_id.split(":")[1], new_id.split(":")[1])
        entry["evidence_ref"]["ref"] = entry["evidence_ref"]["ref"].replace(old_id.split(":")[1], new_id.split(":")[1])
        entry["evidence_ref"]["bundle_ref"] = bundle["bundle_id"]
        for ref in bundle["evidence_refs"]:
            ref["bundle_ref"] = bundle["bundle_id"]
        bundle["evidence_refs"][0] = entry["evidence_ref"]
        bundle["checksums"] = {"candidate": new_id, "validation": validation["receipt_digest"]}
        bundle["spec_hash"] = {"value": compute_spec_hash({k: v for k, v in bundle.items() if k != "spec_hash"})}
        history = entry["verification_history"]
        history["subject_ref"] = entry["evidence_ref"]["ref"]
        history["events"][0]["basis_refs"] = ["kfm://receipt/validation/" + validation["receipt_digest"].split(":")[1]]
        history["spec_hash"] = canonical_spec_hash(history)
    snapshot["artifacts"]["validation.json"] = canonical_bytes(validation).decode()
    snapshot["manifest"]["artifacts"]["validation.json"] = digest_bytes(snapshot["artifacts"]["validation.json"].encode())
    reseal_evidence(snapshot, evidence)
    raw = canonical_bytes(snapshot)
    validate_snapshot(raw)
    root = tmp_path / "invalid-candidate-store"
    with pytest.raises(ValueError, match="CANDIDATE_VALIDATION_FAILED"):
        stage(root, raw, actor="synthetic-owner", now=NOW)
    assert not root.exists()


def test_activation_replays_previously_staged_validation_receipt(tmp_path):
    from release.local_admin import activate, initialize

    snapshot = synthetic_snapshot(cleared=True)
    validation = json.loads(snapshot["artifacts"]["validation.json"])
    validation["release_authorized"] = True
    reseal_validation(snapshot, validation)
    raw = canonical_bytes(snapshot)
    validate_snapshot(raw)
    root = tmp_path / "legacy-release-store"
    initialize(root)
    package_id = snapshot["manifest"]["package_id"]
    name = package_id.split(":")[1] + ".json"
    (root / "objects" / name).write_bytes(raw)
    with sqlite3.connect(root / "activation.sqlite") as db:
        db.execute("INSERT INTO water_packages VALUES(?,?,?,?,?)", (package_id, name, NOW, "synthetic-owner", "STAGED"))
    with pytest.raises(ValueError, match="VALIDATION_RECEIPT_MISMATCH"):
        activate(root, package_id, synthetic_decision(snapshot), expected_active=None, now=NOW)
    assert LocalReleaseStore(str(root)).active() is None


def test_revoked_second_station_cannot_leak_through_filtered_layers():
    from evidence_resolver.verification_history import canonical_spec_hash
    snapshot = synthetic_snapshot(cleared=True)
    evidence = json.loads(snapshot["artifacts"]["evidence.json"])
    history = evidence["entries"][1]["verification_history"]
    history["events"].append({"event_id": "evt:002", "event_type": "REVOKED", "state": "REVOKED",
        "effective_at": "2026-09-30T18:50:00Z", "recorded_at": "2026-09-30T18:50:00Z", "reason_code": "SYNTHETIC_WITHDRAWAL",
        "basis_refs": ["kfm://synthetic/correction"], "relates_to_event_id": "evt:001", "revocation_ref": "kfm://synthetic/revocation"})
    history["spec_hash"] = canonical_spec_hash(history)
    reseal_evidence(snapshot, evidence)
    decision = synthetic_decision(snapshot)
    response = project(canonical_bytes(snapshot), decision, view="layers", now=NOW, station_id="USGS-06892518")
    assert response["envelope"]["outcome"] == "ANSWER"
    assert [s["id"] for s in response["data"]["stations"]] == ["USGS-06892518"]
    assert "USGS-07156900" not in json.dumps(response)
    assert "data" not in project(canonical_bytes(snapshot), decision, view="layers", now=NOW)


@pytest.mark.parametrize("mutate", [
    lambda b: b["evidence_refs"].pop(),
    lambda b: b["checksums"].update(candidate="sha256:" + "0"*64),
    lambda b: b["source_records"].clear(),
])
def test_resealed_inconsistent_evidence_cannot_be_served(mutate):
    snapshot = synthetic_snapshot(cleared=True)
    evidence = json.loads(snapshot["artifacts"]["evidence.json"])
    mutate(evidence["entries"][0]["bundle"])
    reseal_evidence(snapshot, evidence)
    with pytest.raises(ValueError):
        project(canonical_bytes(snapshot), synthetic_decision(snapshot), view="layers", now=NOW)


def test_staging_cannot_activate_and_atomic_rollback_rehearsal(tmp_path):
    from release.local_admin import stage, activate
    root = tmp_path / "release-only"
    held = synthetic_snapshot()
    held_id = stage(root, canonical_bytes(held), actor="synthetic-owner", now=NOW)
    assert LocalReleaseStore(str(root)).active() is None
    with pytest.raises(ValueError, match="HOLD"):
        activate(root, held_id, synthetic_decision(held), expected_active=None, now=NOW)
    first = synthetic_snapshot(cleared=True)
    first_id = stage(root, canonical_bytes(first), actor="synthetic-owner", now=NOW)
    activate(root, first_id, synthetic_decision(first), expected_active=None, now=NOW)
    second = deepcopy(first)
    second["manifest"]["rollback_target"] = first_id
    second["manifest"]["package_id"] = compute_spec_hash({k: v for k, v in second["manifest"].items() if k != "package_id"})
    second_id = stage(root, canonical_bytes(second), actor="synthetic-owner", now=NOW)
    with pytest.raises(ValueError, match="CONFLICT"):
        activate(root, second_id, synthetic_decision(second), expected_active=None, now=NOW)
    assert json.loads(LocalReleaseStore(str(root)).active()[0])["manifest"]["package_id"] == first_id
    activate(root, second_id, synthetic_decision(second), expected_active=first_id, now=NOW)
    activate(root, first_id, synthetic_decision(first), expected_active=second_id, now=NOW, rollback=True)
    restored = project(*LocalReleaseStore(str(root)).active(), view="evidence", now=NOW)
    assert restored == project(canonical_bytes(first), synthetic_decision(first), view="evidence", now=NOW)
    with sqlite3.connect(root / "activation.sqlite") as db:
        assert db.execute("SELECT COUNT(*) FROM water_activation_events").fetchone()[0] == 3


def test_withdrawn_package_state_immediately_withholds_active_data(tmp_path):
    from release.local_admin import stage, activate
    root = tmp_path / "withdrawal"
    snapshot = synthetic_snapshot(cleared=True)
    package_id = stage(root, canonical_bytes(snapshot), actor="synthetic-owner", now=NOW)
    activate(root, package_id, synthetic_decision(snapshot), expected_active=None, now=NOW)
    with sqlite3.connect(root / "activation.sqlite") as db:
        db.execute("UPDATE water_packages SET state='WITHDRAWN' WHERE package_id=?", (package_id,))
    assert LocalReleaseStore(str(root)).active() is None
    with pytest.raises(ValueError, match="PACKAGE_NOT_STAGED|ROLLBACK_BINDING_MISMATCH"):
        activate(root, package_id, synthetic_decision(snapshot), expected_active=package_id, now=NOW)


def test_package_and_trusted_decision_have_canonical_closed_schemas():
    snapshot = synthetic_snapshot(cleared=True)
    for name, value in [("water_snapshot", snapshot), ("water_release_decision", synthetic_decision(snapshot))]:
        schema = json.loads((ROOT / f"schemas/contracts/v1/release/{name}.schema.json").read_text())
        validator = Draft202012Validator(schema, registry=build_registry(ROOT), format_checker=FormatChecker())
        validator.validate(value)
        assert list(validator.iter_errors({**value, "client_approval": True}))
