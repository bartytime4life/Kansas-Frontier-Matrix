#!/usr/bin/env python3
"""Replay synthetic EvidenceTemporalPostureAssessment compatibility and recovery.

Common envelopes keep their own chronology. This is a fixture rehearsal, with
no common/evidence translation or production-store interface.
"""
from __future__ import annotations

import argparse
import json
import sys
import tempfile
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.local_data.file_io import read_regular
from tools.release import rollback_apply as rollback
from tools.validators import validate_temporal_authority_envelope as common
from tools.validators.evidence import validate_evidence_temporal_posture_assessment as evidence
from tools.validators.evidence import validate_temporal_authority_envelope as legacy
from tools.validators.governance.temporal_authority_split_support import (
    CANONICAL_SCHEMA, CANONICAL_SCHEMA_ID, COMMON_SCHEMA, COMMON_SCHEMA_ID,
    LEGACY_PREFIX, LEGACY_SCHEMA, LEGACY_SCHEMA_ID,
)

FIXTURES = ROOT / "fixtures/release/temporal_replay"
MAX_INPUT_BYTES = 256 * 1024
PROFILE = "kfm.synthetic-temporal-replay/v1"
PREDECESSOR = "release:synthetic:temporal-v1"
SUCCESSOR = "release:synthetic:temporal-v2"
FILES = ("case.json", "legacy.json", "successor.json", "withdrawn.json",
         "common-v1.json", "common-v2.json", "successor-receipt.json")
CLOCKS = ("observed_at", "valid_from", "valid_to", "source_updated_at",
          "retrieved_at", "released_at", "corrected_at")
CONSUMERS = (
    "tools/validators/evidence/validate_temporal_authority_envelope.py",
    "tools/validators/evidence/validate_evidence_temporal_posture_assessment.py",
    "tools/validators/validate_temporal_authority_envelope.py",
    "tools/release/rollback_apply.py",
    "tests/release/test_temporal_replay.py",
    ".github/workflows/rollback-drill.yml",
)
EXTERNAL_SCOPES = ("databases", "object_storage", "deployed_clients",
                   "downstream_repositories", "generated_ci_artifacts")


class ReplayError(ValueError):
    """Finite failure without record values, private paths or stack traces."""


def require(condition: bool, code: str) -> None:
    if not condition:
        raise ReplayError(code)


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ReplayError("DUPLICATE_JSON_KEY")
        result[key] = value
    return result


def reject_constant(_value):
    raise ReplayError("NONFINITE_JSON")


def load_fixture(root: Path):
    raw, objects = {}, {}
    for name in FILES:
        raw[name] = read_regular(root / name, MAX_INPUT_BYTES)
        objects[name] = json.loads(raw[name], object_pairs_hook=unique_object, parse_constant=reject_constant)
        require(isinstance(objects[name], dict), "FIXTURE_OBJECT_REQUIRED")
    return raw, objects


def validate_fixture(root: Path, raw: dict, objects: dict) -> datetime:
    case = objects["case.json"]
    require(set(case) == {"profile", "synthetic", "evaluated_at", "predecessor_release_id", "successor_release_id"},
            "FIXTURE_PROFILE_INVALID")
    require(case["profile"] == PROFILE and case["synthetic"] is True, "SYNTHETIC_FIXTURE_REQUIRED")
    require((case["predecessor_release_id"], case["successor_release_id"]) == (PREDECESSOR, SUCCESSOR),
            "FIXTURE_RELEASE_ID_INVALID")
    require(isinstance(case["evaluated_at"], str), "EXPLICIT_TIME_REQUIRED")
    try:
        now = datetime.fromisoformat(case["evaluated_at"].upper().replace("Z", "+00:00"))
    except ValueError:
        raise ReplayError("EXPLICIT_TIME_REQUIRED") from None
    require(now.tzinfo is not None and now.utcoffset() is not None, "EXPLICIT_TIME_REQUIRED")
    for name in ("legacy.json", "successor.json", "withdrawn.json"):
        record = objects[name]
        require(not legacy.validate_doc(record, now=now) and not evidence.validate_doc(record, now=now),
                "EVIDENCE_REPLAY_INVALID")
        require(record["source_role"] == "SYNTHETIC" and record["envelope_id"].startswith(LEGACY_PREFIX + "synthetic-"),
                "SYNTHETIC_RECORD_REQUIRED")
        require(not common.validate_envelope(root / name).ok, "CROSS_FAMILY_FALSE_ACCEPTANCE")
        require(all(datetime.fromisoformat(record["times"][clock].upper().replace("Z", "+00:00")) <= now
                    for clock in ("observed_at", "source_updated_at", "retrieved_at", "released_at", "corrected_at")
                    if record["times"][clock] is not None), "REPLAY_EVENT_AFTER_AS_OF")
    for name in ("common-v1.json", "common-v2.json"):
        require(common.validate_envelope(root / name).ok, "COMMON_REPLAY_INVALID")
        require(bool(evidence.validate_doc(objects[name], now=now)), "CROSS_FAMILY_FALSE_ACCEPTANCE")

    old, new, withdrawn = (objects[name] for name in ("legacy.json", "successor.json", "withdrawn.json"))
    require(len({old["envelope_id"], new["envelope_id"], withdrawn["envelope_id"]}) == 3, "REVISION_ID_COLLAPSE")
    require(old["subject_ref"] == new["subject_ref"] == withdrawn["subject_ref"], "SUBJECT_BINDING_MISMATCH")
    require(old["temporal_posture"] == new["temporal_posture"] == "CURRENT", "CURRENT_REPLAY_REQUIRED")
    require(new.get("supersedes_ref") == old["envelope_id"] and old["envelope_id"] in new["lineage_refs"],
            "SUCCESSOR_LINEAGE_MISMATCH")
    require(withdrawn["temporal_posture"] == "WITHDRAWN"
            and withdrawn.get("supersedes_ref") == new["envelope_id"]
            and new["envelope_id"] in withdrawn["lineage_refs"]
            and withdrawn.get("withdrawal_ref") == "correction:synthetic:temporal-withdrawal", "WITHDRAWAL_BINDING_MISMATCH")
    require(all(new["times"][clock] is not None for clock in CLOCKS)
            and len(set(new["times"].values())) == len(CLOCKS), "CLOCK_COVERAGE_INCOMPLETE")
    require(all(old["times"][clock] == new["times"][clock] for clock in ("observed_at", "valid_from", "valid_to")),
            "OBSERVATION_CLOCKS_CHANGED")
    first, second = objects["common-v1.json"], objects["common-v2.json"]
    require(first["identity"]["object_id"] == second["identity"]["object_id"]
            and first["identity"]["revision_id"] != second["identity"]["revision_id"]
            and second["lineage"]["supersedes"] == [first["identity"]["revision_id"]], "COMMON_LINEAGE_MISMATCH")
    require(second["time"]["corrected_at"] is not None
            and second["time"]["corrected_at"] != new["times"]["corrected_at"], "CORRECTION_CLOCKS_COLLAPSED")

    expected_receipt = {
        "profile": "kfm.synthetic-temporal-successor-receipt/v1", "synthetic": True,
        "source_schema_id": LEGACY_SCHEMA_ID, "target_schema_id": CANONICAL_SCHEMA_ID,
        "compatibility": "EVIDENCE_DUAL_READ_ONLY", "common_translation": False,
        "predecessor": {"record_ref": old["envelope_id"], "sha256": rollback.digest_bytes(raw["legacy.json"])},
        "successor": {"record_ref": new["envelope_id"], "sha256": rollback.digest_bytes(raw["successor.json"])},
        "common_context": {"schema_id": COMMON_SCHEMA_ID,
            "predecessor_revision_ref": first["identity"]["revision_id"],
            "predecessor_sha256": rollback.digest_bytes(raw["common-v1.json"]),
            "successor_revision_ref": second["identity"]["revision_id"],
            "successor_sha256": rollback.digest_bytes(raw["common-v2.json"])},
    }
    require(rollback.canonical(objects["successor-receipt.json"]) == rollback.canonical(expected_receipt),
            "SUCCESSOR_RECEIPT_BINDING_MISMATCH")
    return now


def install_workspace(root: Path, raw: dict) -> dict:
    """Materialize verified fixture bytes in a new TemporaryDirectory only."""
    require(root.is_dir() and not root.is_symlink() and not any(root.iterdir()), "ISOLATED_EMPTY_WORKSPACE_REQUIRED")
    (root / rollback.MARKER).write_text("synthetic-only\n")
    manifests = {}
    for rid, evidence_name, common_name in ((PREDECESSOR, "legacy.json", "common-v1.json"),
                                          (SUCCESSOR, "successor.json", "common-v2.json")):
        files = {"evidence.json": raw[evidence_name], "common.json": raw[common_name]}
        if rid == SUCCESSOR:
            files["successor-receipt.json"] = raw["successor-receipt.json"]
        directory = root / "releases" / rid
        directory.mkdir(parents=True)
        for name, payload in files.items():
            (directory / name).write_bytes(payload)
        manifest = {"release_id": rid, "previous_release_id": None if rid == PREDECESSOR else PREDECESSOR,
                    "artifacts": [{"path": name, "digest": rollback.digest_bytes(payload)}
                                  for name, payload in sorted(files.items())]}
        rollback.write_json(directory / "manifest.json", manifest)
        manifests[rid] = manifest
    rollback.write_json(root / "published/current.json", {"status": "ACTIVE", "release_id": SUCCESSOR})
    return manifests


def tree_bytes(root: Path) -> dict:
    return {path.relative_to(root).as_posix(): path.read_bytes() for path in root.rglob("*") if path.is_file()}


def replay_branch(raw: dict, objects: dict, operation: str, now: datetime) -> dict:
    case = objects["case.json"]
    with tempfile.TemporaryDirectory(prefix="kfm-temporal-replay-") as directory:
        root = Path(directory)
        manifests = install_workspace(root, raw)
        target = PREDECESSOR if operation == "ROLLBACK" else None
        scenario = {"scenario_id": "rehearsal:synthetic:temporal-" + operation.lower(), "synthetic": True,
                    "operation": operation, "affected_release_id": SUCCESSOR, "target_release_id": target,
                    "correction": {"correction_id": "correction:synthetic:temporal-" + operation.lower(),
                                   "reason_code": "SYNTHETIC_TEMPORAL_CORRECTION",
                                   "decided_at": objects["withdrawn.json"]["times"]["corrected_at"] if operation == "WITHDRAWAL" else case["evaluated_at"]},
                    "invalidations": list(rollback.INVALIDATIONS),
                    "expected": {"current_alias_digest": rollback.digest_bytes(rollback.canonical({"status": "ACTIVE", "release_id": SUCCESSOR})),
                                 "affected_manifest_digest": rollback.digest_bytes(rollback.canonical(manifests[SUCCESSOR])),
                                 "target_manifest_digest": rollback.digest_bytes(rollback.canonical(manifests[PREDECESSOR])) if target else None}}
        before = tree_bytes(root)
        plan = rollback.rehearse(root, scenario)
        require(plan["mode"] == "PLAN" and tree_bytes(root) == before, "PLAN_WROTE_STATE")
        report = rollback.rehearse(root, scenario, apply=True)
        after = tree_bytes(root)
        require(all(after.get(name) == data for name, data in before.items() if name.startswith("releases/")), "HISTORY_MUTATED")
        alias = rollback.read_object(root / "published/current.json")
        invalidation = rollback.read_object(root / "invalidations" / (scenario["scenario_id"] + ".json"))
        require(invalidation == {"scenario_id": scenario["scenario_id"], "affected_release_id": SUCCESSOR,
                                 "invalidations": list(rollback.INVALIDATIONS), "synthetic": True}, "INVALIDATION_READBACK_MISMATCH")
        correction = rollback.read_object(root / "corrections" / (scenario["correction"]["correction_id"] + ".json"))
        require(correction == {**scenario["correction"], "affected_release_id": SUCCESSOR, "operation": operation,
                               "target_release_id": target, "synthetic": True}
                and alias == report["after"]["current_alias"], "RECOVERY_READBACK_MISMATCH")
        if target:
            restored = root / "releases" / target / "evidence.json"
            require(alias["release_id"] == PREDECESSOR and restored.read_bytes() == raw["legacy.json"], "LEGACY_ROLLBACK_MISMATCH")
            require(not legacy.validate_file(restored, now=now) and not evidence.validate_file(restored, now=now), "LEGACY_ROLLBACK_INVALID")
        else:
            require(alias["status"] == "WITHDRAWN" and alias["release_id"] is None, "WITHDRAWAL_STILL_CURRENT")
        return {"outcome": report["outcome"], "alias": alias, "history_byte_identical": True,
                "plan_read_only": True, "invalidations": invalidation["invalidations"]}


def replay(fixture_root: Path = FIXTURES) -> dict:
    raw, objects = load_fixture(fixture_root)
    now = validate_fixture(fixture_root, raw, objects)
    branches = {name.lower(): replay_branch(raw, objects, name, now) for name in ("ROLLBACK", "WITHDRAWAL")}
    require(all(read_regular(fixture_root / name, MAX_INPUT_BYTES) == data for name, data in raw.items()), "FIXTURE_BYTES_CHANGED")
    report = {"profile": PROFILE, "outcome": "PASS", "scope": "SYNTHETIC_REPLAY_ONLY",
              "evaluated_at": objects["case.json"]["evaluated_at"],
              "input_sha256": {name: rollback.digest_bytes(data) for name, data in sorted(raw.items())},
              "clock_fields_preserved": list(CLOCKS), "common_and_evidence_chronology_distinct": True,
              "legacy_identifier": objects["legacy.json"]["envelope_id"], "legacy_dual_read": "PASS",
              "cross_family_false_acceptance": False, "branches": branches,
              "consumer_inventory": {
                  "scope": "declared first-party rehearsal consumers only; not a repository-wide census",
                  "first_party": [{"path": path, "sha256": rollback.digest_bytes(read_regular(ROOT / path, 1024 * 1024))}
                                  for path in CONSUMERS],
                  "external": [{"scope": scope, "status": "NOT_INSPECTED", "record_count": None, "sha256": None}
                               for scope in EXTERNAL_SCOPES],
                  "legacy_removal": "HOLD_EXTERNAL_INVENTORY_REQUIRED"},
              "schema_sha256": {path: rollback.digest_bytes(read_regular(ROOT / path, 1024 * 1024))
                                for path in (LEGACY_SCHEMA, CANONICAL_SCHEMA, COMMON_SCHEMA)},
              "authority": {"translation": False, "legacy_removal": False, "source_admission": False,
                            "review": False, "production_write": False, "release": False, "publication": False}}
    report["report_sha256"] = rollback.digest_bytes(rollback.canonical(report))
    return report


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fixtures", action="store_true", required=True, help="replay repository synthetic fixtures in temporary roots")
    parser.parse_args(argv)
    try:
        report = replay()
    except ReplayError as exc:
        report = {"profile": PROFILE, "outcome": "FAIL", "reason_code": str(exc)}
    except rollback.RehearsalError as exc:
        report = {"profile": PROFILE, "outcome": "FAIL", "reason_code": exc.code}
    except (OSError, ValueError, TypeError, KeyError, RecursionError):
        report = {"profile": PROFILE, "outcome": "ERROR", "reason_code": "FIXTURE_REPLAY_UNAVAILABLE"}
    print(json.dumps(report, sort_keys=True))
    return 0 if report["outcome"] == "PASS" else 1 if report["outcome"] == "FAIL" else 2


if __name__ == "__main__":
    raise SystemExit(main())
