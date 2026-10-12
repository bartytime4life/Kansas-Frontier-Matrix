"""NOAA Storm Events release (ADR-0047): admitted package -> owner decision; gate denials; family isolation; month bundles."""
from datetime import datetime, timedelta, timezone
import json

import pytest

from connectors_core.captured_json import canonical_bytes, digest_bytes
from hashing import compute_spec_hash
from pipelines.domains.hazards import storm_events_admission, storm_events_package
from pipelines.domains.hazards.storm_events_normalize import normalize_capture
from policy_runtime.core import (
    SELF_RELEASE_LICENSES, SOIL_DECISION_PROFILE, SOIL_SELF_RELEASE_LICENSES, STORM_EVENTS_DECISION_PROFILE,
    STORM_EVENTS_SELF_RELEASE_LICENSES, WEATHER_SELF_RELEASE_LICENSES, serving_gate,
)
from release.core import MONTH_PART_SIZE, SOIL, STORM_EVENTS, WATER, WEATHER, validate_snapshot
from tests.domains.hazards.storm_events_fixtures import acquired
from tools.local_data import storm_events_pilot
from tools.local_data.manage import init_store
from tools.release import storm_events_release

OWNER = "@bartytime4life"
NOW = datetime(2026, 10, 12, 13, 0, tzinfo=timezone.utc)
STORM_GATE = {"decision_profile": STORM_EVENTS_DECISION_PROFILE, "licenses": STORM_EVENTS_SELF_RELEASE_LICENSES}


def many_in_may(count):
    """Add ``count`` synthetic May events (copies of the tornado row) to the details file."""
    def mutate(key, text):
        if key == "listing":
            return text
        lines = text.splitlines()
        row = lines[1]
        extra = [row.replace("202504,28,1712,202504,28,1726,900001,9000101",
                             f"202505,28,1712,202505,28,1726,{910000 + i},{9200000 + i}")
                    .replace("28-04-25 17:12:00", "28-05-25 17:12:00") for i in range(count)]
        return "\n".join(lines + extra) + "\n"
    return mutate


def prepared(tmp_path, *, admitted, mutate=None):
    root = tmp_path / "store"
    init_store(root)
    candidate_id = storm_events_pilot.stage(root, acquired(mutate))["candidate_id"]
    return root, storm_events_release.prepare(root, candidate_id, admitted_source=admitted)


def snapshot_path(root, package_id):
    return root / "release/candidates/storm-events" / package_id.split(":")[1] / "snapshot.json"


def gate(root, package_id, decision, **profile):
    manifest, values = storm_events_release._snapshot(root, package_id)
    return serving_gate(manifest, values["evidence.json"], decision, now=decision["released_at"], **profile)


def reseal(snapshot, evidence):
    """Rewrite evidence.json and every outer digest, as a forger would."""
    text = canonical_bytes(evidence).decode()
    manifest = snapshot["manifest"]
    manifest["artifacts"]["evidence.json"] = digest_bytes(text.encode())
    snapshot["artifacts"]["evidence.json"] = text
    manifest["package_id"] = compute_spec_hash({k: v for k, v in manifest.items() if k != "package_id"})
    return canonical_bytes(snapshot)


def test_owner_releases_an_admitted_storm_events_package(tmp_path, capsys):
    root, preparation = prepared(tmp_path, admitted=True)
    assert (preparation["reason_code"], preparation["admitted_source"]) == ("RELEASE_DECISION_REQUIRED", "kfm://source/noaa-storm-events")
    code = storm_events_release.main(["decide", "--root", str(root), "--package-id", preparation["package_id"],
                                      "--reviewer", OWNER, "--releaser", OWNER])
    decided = json.loads(capsys.readouterr().out)
    assert (code, decided["outcome"], decided["activated"]) == (0, "DECIDED", False)
    decision = json.loads((root / decided["decision_path"]).read_text())
    assert (decision["profile"], decision["policy_ref"], decision["package_id"]) == (
        STORM_EVENTS_DECISION_PROFILE, "kfm://adr/0047", preparation["package_id"])
    assert decided["decision_path"].startswith("release/decisions/storm-events/")
    assert not (root / "release/active").exists()


def test_manifest_covers_the_data_year_and_the_catalog_carries_no_narrative(tmp_path):
    root, preparation = prepared(tmp_path, admitted=True)
    manifest, values = storm_events_release._snapshot(root, preparation["package_id"])
    assert (manifest["start"], manifest["end"], manifest["profile"]) == ("2025-01-01", "2025-12-31", "kfm.storm-events-snapshot/v1")
    dataset = values["catalog.json"]["dataset"]
    assert (dataset["observation_count"], dataset["withheld_rows"], dataset["narratives"]) == (6, 2, "excluded")
    assert dataset["event_types"]["Tornado"] == 1
    assert "Synthetic narrative" not in snapshot_path(root, preparation["package_id"]).read_text()


def test_evidence_is_one_bundle_per_month_with_events(tmp_path):
    root, preparation = prepared(tmp_path, admitted=True)
    manifest, values = storm_events_release._snapshot(root, preparation["package_id"])
    entries = values["evidence.json"]["entries"]
    # The six included fixture events begin in January, April, May, June, July and August.
    assert [(e["month"], e["part"]) for e in entries] == [(1, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1)]
    candidate = values["candidate.json"]
    may = entries[2]["bundle"]["evidence_refs"]
    assert may[0]["ref"] == "kfm://hazards/storm-events/2025-05/part-1/" + manifest["candidate_id"].split(":")[1]
    assert [m["ref"] for m in may[1:]] == [r["evidence_ref"] for r in candidate["observations"] if r["begin_local"][5:7] == "05"]
    assert {m["kind"] for e in entries for m in e["bundle"]["evidence_refs"][1:]} == {"record"}
    refs = [m["ref"] for e in entries for m in e["bundle"]["evidence_refs"][1:]]
    assert sorted(refs) == sorted(r["evidence_ref"] for r in candidate["observations"])


def test_a_busy_month_splits_into_numbered_parts(tmp_path):
    root, preparation = prepared(tmp_path, admitted=True, mutate=many_in_may(2 * MONTH_PART_SIZE))
    _, values = storm_events_release._snapshot(root, preparation["package_id"])
    entries = values["evidence.json"]["entries"]
    may = [e for e in entries if e["month"] == 5]
    # 1 fixture May event + 254 added = 255 records: 127 + 127 + 1.
    assert [(e["part"], len(e["bundle"]["evidence_refs"]) - 1) for e in may] == [(1, 127), (2, 127), (3, 1)]
    assert all(len(e["bundle"]["evidence_refs"]) <= 128 for e in entries)
    assert "part 3 of 3" in may[2]["bundle"]["claim_scope"]
    assert sum(len(e["bundle"]["evidence_refs"]) - 1 for e in entries) == len(values["candidate.json"]["observations"])


@pytest.mark.parametrize("forge", ["drop", "duplicate", "missing_part", "string_month", "swap"])
def test_a_resealed_package_with_wrong_month_bundles_is_refused(tmp_path, forge):
    root, preparation = prepared(tmp_path, admitted=True)
    snapshot = json.loads(snapshot_path(root, preparation["package_id"]).read_text())
    evidence = json.loads(snapshot["artifacts"]["evidence.json"])
    entries = evidence["entries"]
    if forge == "drop":
        entries.pop()
        expected = "EVIDENCE_CLOSURE_INVALID"
    elif forge == "duplicate":
        entries[1] = entries[0]
        expected = "SERIES_EVIDENCE_MISMATCH"
    elif forge == "missing_part":
        del entries[0]["part"]
        expected = "SERIES_EVIDENCE_MISMATCH"
    elif forge == "string_month":
        entries[0]["month"] = "1"
        expected = "SERIES_EVIDENCE_MISMATCH"
    else:
        # Swap two months' labels: each bundle now claims the other month's events.
        entries[0]["month"], entries[1]["month"] = entries[1]["month"], entries[0]["month"]
        entries[0], entries[1] = entries[1], entries[0]
        expected = "DATASET_EVIDENCE_MISMATCH"
    with pytest.raises(ValueError, match=expected):
        validate_snapshot(reseal(snapshot, evidence), profile=STORM_EVENTS)


def test_an_unadmitted_package_cannot_be_released(tmp_path):
    root, preparation = prepared(tmp_path, admitted=False)
    assert preparation["reason_code"] == "REVIEW_REQUIRED"
    with pytest.raises(ValueError, match="INDEPENDENT_REVIEW_REQUIRED"):
        storm_events_release.decide(root, preparation["package_id"], reviewer=OWNER, releaser=OWNER, valid_days=7, now=NOW)
    # A second reviewer does not clear the rights and sensitivity hold either.
    with pytest.raises(ValueError, match="RIGHTS_OR_SENSITIVITY_HOLD"):
        storm_events_release.decide(root, preparation["package_id"], reviewer="@reviewer", releaser=OWNER, valid_days=7, now=NOW)
    assert not (root / "release/decisions").exists()


def test_storm_events_and_other_gates_never_accept_each_others_decisions(tmp_path):
    root, preparation = prepared(tmp_path, admitted=True)
    decision = storm_events_release.build_decision(preparation["package_id"], reviewer=OWNER, releaser=OWNER, now=NOW, valid_days=7)
    assert gate(root, preparation["package_id"], decision, **STORM_GATE) == "ELIGIBLE"
    soil = {"decision_profile": SOIL_DECISION_PROFILE, "licenses": SOIL_SELF_RELEASE_LICENSES}
    assert gate(root, preparation["package_id"], decision) == "RELEASE_BINDING_MISMATCH"
    assert gate(root, preparation["package_id"], decision, **soil) == "RELEASE_BINDING_MISMATCH"
    # No other family's license list admits the Storm Events license for self-release.
    assert gate(root, preparation["package_id"], {**decision, "profile": SOIL_DECISION_PROFILE}, **soil) == "INDEPENDENT_REVIEW_REQUIRED"
    assert gate(root, preparation["package_id"], {**decision, "profile": "kfm.water-release-decision/v1"}) == "INDEPENDENT_REVIEW_REQUIRED"


def test_snapshot_profiles_do_not_cross(tmp_path):
    root, preparation = prepared(tmp_path, admitted=True)
    raw = snapshot_path(root, preparation["package_id"]).read_bytes()
    assert validate_snapshot(raw, profile=STORM_EVENTS)[0]["profile"] == "kfm.storm-events-snapshot/v1"
    for profile in (WATER, WEATHER, SOIL):
        with pytest.raises(ValueError, match="MANIFEST_PROFILE_INVALID"):
            validate_snapshot(raw, profile=profile)


def test_license_lists_match_the_admitted_descriptor_and_are_disjoint():
    descriptor = json.loads(storm_events_admission.DESCRIPTOR.read_text())
    assert descriptor["review_state"] == "approved" and descriptor["public_release"]["allowed"] is True
    assert STORM_EVENTS_SELF_RELEASE_LICENSES == {descriptor["rights"]["license_or_terms"]}
    assert storm_events_admission.load_admission()["license"] in STORM_EVENTS_SELF_RELEASE_LICENSES
    assert not STORM_EVENTS_SELF_RELEASE_LICENSES & (SELF_RELEASE_LICENSES | WEATHER_SELF_RELEASE_LICENSES | SOIL_SELF_RELEASE_LICENSES)


def test_decisions_are_bounded_and_ids_checked(tmp_path):
    root, preparation = prepared(tmp_path, admitted=True)
    for days in (0, 31):
        with pytest.raises(ValueError, match="VALID_DAYS_OUT_OF_RANGE"):
            storm_events_release.decide(root, preparation["package_id"], reviewer=OWNER, releaser=OWNER, valid_days=days, now=NOW)
    with pytest.raises(ValueError, match="PACKAGE_ID_INVALID"):
        storm_events_release.decide(root, "../../x", reviewer=OWNER, releaser=OWNER, valid_days=7, now=NOW)
    with pytest.raises(ValueError, match="INVALID_CANDIDATE_ID"):
        storm_events_release.prepare(root, "sha256:../x")


def test_an_expired_decision_is_not_eligible(tmp_path):
    root, preparation = prepared(tmp_path, admitted=True)
    decision = storm_events_release.build_decision(preparation["package_id"], reviewer=OWNER, releaser=OWNER, now=NOW, valid_days=1)
    manifest, values = storm_events_release._snapshot(root, preparation["package_id"])
    later = (NOW + timedelta(days=2)).strftime("%Y-%m-%dT%H:%M:%SZ")
    assert serving_gate(manifest, values["evidence.json"], decision, now=later, **STORM_GATE) == "RELEASE_TIME_INVALID"


def test_preparation_is_deterministic(tmp_path):
    root, first = prepared(tmp_path, admitted=True)
    assert storm_events_release.prepare(root, first["candidate_id"], admitted_source=True) == first
    path = snapshot_path(root, first["package_id"])
    assert canonical_bytes(json.loads(path.read_text())) == path.read_bytes()


def test_a_year_without_kansas_events_has_nothing_to_package():
    source = acquired(lambda key, text: text if key == "listing" else text.replace(",KANSAS,20,", ",NEBRASKA,31,"))
    candidate = normalize_capture(source.manifest, source.objects)
    assert candidate["observations"] == []
    with pytest.raises(ValueError, match="NO_EVENTS_TO_PACKAGE"):
        storm_events_package.prepare_storm_events_package(candidate, admission=storm_events_admission.load_admission())


def test_decide_refuses_a_rehashed_package_with_stale_bundles(tmp_path):
    root, preparation = prepared(tmp_path, admitted=True)
    snapshot = json.loads(snapshot_path(root, preparation["package_id"]).read_text())
    evidence = json.loads(snapshot["artifacts"]["evidence.json"])
    evidence["entries"][0]["bundle"]["spec_hash"]["value"] = "sha256:" + "0" * 64
    raw = reseal(snapshot, evidence)
    package_id = snapshot["manifest"]["package_id"]
    forged = snapshot_path(root, package_id)
    forged.parent.mkdir(parents=True)
    forged.write_bytes(raw)
    with pytest.raises(ValueError, match="PACKAGE_NOT_REPRODUCIBLE"):
        storm_events_release.decide(root, package_id, reviewer=OWNER, releaser=OWNER, valid_days=7, now=NOW)
    assert not (root / "release/decisions").exists()


def test_cli_reports_a_reason_code_on_refusal(tmp_path, capsys):
    root, preparation = prepared(tmp_path, admitted=False)
    code = storm_events_release.main(["decide", "--root", str(root), "--package-id", preparation["package_id"],
                                      "--reviewer", OWNER, "--releaser", OWNER])
    assert (code, json.loads(capsys.readouterr().out)) == (1, {"outcome": "ERROR", "reason_code": "INDEPENDENT_REVIEW_REQUIRED"})


def test_decide_refuses_a_package_whose_receipt_differs_from_revalidation(tmp_path, monkeypatch):
    # The candidate is genuine, but the packaged (and bundle-bound) receipt is not the one it produces.
    root, preparation = prepared(tmp_path, admitted=True)
    _, values = storm_events_release._snapshot(root, preparation["package_id"])

    def miscounting(value):
        report = {k: v for k, v in values["validation.json"].items() if k != "receipt_digest"}
        report["withheld"] += 1
        report["receipt_digest"] = digest_bytes(canonical_bytes(report))
        return report
    monkeypatch.setattr(storm_events_package, "validate_candidate", miscounting)
    snapshot = storm_events_package.prepare_storm_events_package(values["candidate.json"], admission=storm_events_admission.load_admission())
    package_id = snapshot["manifest"]["package_id"]
    path = snapshot_path(root, package_id)
    path.parent.mkdir(parents=True)
    path.write_bytes(canonical_bytes(snapshot))
    with pytest.raises(ValueError, match="VALIDATION_RECEIPT_MISMATCH"):
        storm_events_release.decide(root, package_id, reviewer=OWNER, releaser=OWNER, valid_days=7, now=NOW)


def test_decide_requires_the_candidate_to_match_its_stored_capture(tmp_path):
    # Damage is changed consistently (source string and parsed value) and every identity, receipt,
    # bundle and outer hash is rebuilt by the normal package builder; only the stored capture disagrees.
    root, preparation = prepared(tmp_path, admitted=True)
    _, values = storm_events_release._snapshot(root, preparation["package_id"])
    candidate = values["candidate.json"]
    record = candidate["observations"][0]
    record["damage_property_source"], record["damage_property_usd"] = "2.50M", 2500000
    record["record_digest"] = digest_bytes(canonical_bytes({k: v for k, v in record.items() if k != "record_digest"}))
    candidate["candidate_id"] = digest_bytes(canonical_bytes({k: v for k, v in candidate.items() if k != "candidate_id"}))
    snapshot = storm_events_package.prepare_storm_events_package(candidate, admission=storm_events_admission.load_admission())
    package_id = snapshot["manifest"]["package_id"]
    path = snapshot_path(root, package_id)
    path.parent.mkdir(parents=True)
    path.write_bytes(canonical_bytes(snapshot))
    with pytest.raises(ValueError, match="CANDIDATE_CAPTURE_MISMATCH"):
        storm_events_release.decide(root, package_id, reviewer=OWNER, releaser=OWNER, valid_days=7, now=NOW)
    assert not (root / "release/decisions").exists()


def test_decide_refuses_a_package_whose_capture_is_not_in_the_store(tmp_path):
    import shutil
    root, preparation = prepared(tmp_path, admitted=True)
    runs = root / "data/quarantine" / storm_events_pilot.LANE / "runs"
    for manifest in runs.glob("*/manifest.json"):
        manifest.unlink()  # the run directory remains
    with pytest.raises(ValueError, match="CAPTURE_NOT_IN_STORE"):
        storm_events_release.decide(root, preparation["package_id"], reviewer=OWNER, releaser=OWNER, valid_days=7, now=NOW)
    shutil.rmtree(runs)  # a store that never held the capture
    with pytest.raises(ValueError, match="CAPTURE_NOT_IN_STORE"):
        storm_events_release.decide(root, preparation["package_id"], reviewer=OWNER, releaser=OWNER, valid_days=7, now=NOW)


def test_a_held_package_resealed_as_admitted_cannot_be_self_released(tmp_path):
    # Genuine candidate and receipt; only the bundles' rights and sensitivity are rewritten and rehashed.
    root, preparation = prepared(tmp_path, admitted=False)
    snapshot = json.loads(snapshot_path(root, preparation["package_id"]).read_text())
    evidence = json.loads(snapshot["artifacts"]["evidence.json"])
    license_text = storm_events_admission.load_admission()["license"]
    for entry in evidence["entries"]:
        bundle = entry["bundle"]
        bundle["rights"] = {"license": license_text}
        bundle["sensitivity"] = {**bundle["sensitivity"], "level": "public", "reason": "forged"}
        bundle["spec_hash"] = {"value": compute_spec_hash({k: v for k, v in bundle.items() if k != "spec_hash"})}
    raw = reseal(snapshot, evidence)
    package_id = snapshot["manifest"]["package_id"]
    manifest, values = validate_snapshot(raw, profile=STORM_EVENTS)  # the carrier checks alone accept it
    decision = storm_events_release.build_decision(package_id, reviewer=OWNER, releaser=OWNER, now=NOW, valid_days=7)
    assert serving_gate(manifest, values["evidence.json"], decision, now=decision["released_at"], **STORM_GATE) == "ELIGIBLE"
    path = snapshot_path(root, package_id)
    path.parent.mkdir(parents=True)
    path.write_bytes(raw)
    with pytest.raises(ValueError, match="PACKAGE_NOT_REPRODUCIBLE"):
        storm_events_release.decide(root, package_id, reviewer=OWNER, releaser=OWNER, valid_days=7, now=NOW)
    assert not (root / "release/decisions").exists()


@pytest.mark.parametrize("start,end,expected", [
    ("2025-02-01", "2025-12-31", "SNAPSHOT_INTERVAL_INVALID"),
    ("2025-01-01", "2026-12-31", "SNAPSHOT_INTERVAL_INVALID"),
    ("2024-01-01", "2024-12-31", "CANDIDATE_IDENTITY_MISMATCH"),
])
def test_the_manifest_window_must_be_the_candidates_data_year(tmp_path, start, end, expected):
    root, preparation = prepared(tmp_path, admitted=True)
    snapshot = json.loads(snapshot_path(root, preparation["package_id"]).read_text())
    manifest = snapshot["manifest"]
    manifest["start"], manifest["end"] = start, end
    manifest["package_id"] = compute_spec_hash({k: v for k, v in manifest.items() if k != "package_id"})
    with pytest.raises(ValueError, match=expected):
        validate_snapshot(canonical_bytes(snapshot), profile=STORM_EVENTS)
