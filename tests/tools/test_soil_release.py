"""USCRN soil release (ADR-0046): admitted package -> owner decision; gate denials; family isolation; depth bundles."""
from datetime import datetime, timedelta, timezone
import json

import pytest

from connectors_core.captured_json import canonical_bytes, digest_bytes
from hashing import compute_spec_hash
from pipelines.domains.soil import uscrn_daily_admission
from policy_runtime.core import (
    SELF_RELEASE_LICENSES, SOIL_DECISION_PROFILE, SOIL_SELF_RELEASE_LICENSES, WEATHER_DECISION_PROFILE,
    WEATHER_SELF_RELEASE_LICENSES, serving_gate,
)
from release.core import SOIL, WATER, WEATHER, validate_snapshot
from tests.domains.soil.uscrn_daily_fixtures import acquired
from tools.local_data import uscrn_daily_pilot
from tools.local_data.manage import init_store
from tools.release import soil_release

OWNER = "@bartytime4life"
NOW = datetime(2026, 10, 11, 13, 0, tzinfo=timezone.utc)
SOIL_GATE = {"decision_profile": SOIL_DECISION_PROFILE, "licenses": SOIL_SELF_RELEASE_LICENSES}


def prepared(tmp_path, *, admitted):
    root = tmp_path / "store"
    init_store(root)
    candidate_id = uscrn_daily_pilot.stage(root, acquired())["candidate_id"]
    return root, soil_release.prepare(root, candidate_id, admitted_source=admitted)


def snapshot_path(root, package_id):
    return root / "release/candidates/soil" / package_id.split(":")[1] / "snapshot.json"


def gate(root, package_id, decision, **profile):
    manifest, values = soil_release._snapshot(root, package_id)
    return serving_gate(manifest, values["evidence.json"], decision, now=decision["released_at"], **profile)


def reseal(snapshot, evidence):
    """Rewrite evidence.json and every outer digest, as a forger would."""
    text = canonical_bytes(evidence).decode()
    manifest = snapshot["manifest"]
    manifest["artifacts"]["evidence.json"] = digest_bytes(text.encode())
    snapshot["artifacts"]["evidence.json"] = text
    manifest["package_id"] = compute_spec_hash({k: v for k, v in manifest.items() if k != "package_id"})
    return canonical_bytes(snapshot)


def test_owner_releases_an_admitted_soil_package(tmp_path, capsys):
    root, preparation = prepared(tmp_path, admitted=True)
    assert (preparation["reason_code"], preparation["admitted_source"]) == ("RELEASE_DECISION_REQUIRED", "kfm://source/noaa-uscrn")
    code = soil_release.main(["decide", "--root", str(root), "--package-id", preparation["package_id"],
                              "--reviewer", OWNER, "--releaser", OWNER])
    decided = json.loads(capsys.readouterr().out)
    assert (code, decided["outcome"], decided["activated"]) == (0, "DECIDED", False)
    decision = json.loads((root / decided["decision_path"]).read_text())
    assert (decision["profile"], decision["policy_ref"], decision["package_id"]) == (
        SOIL_DECISION_PROFILE, "kfm://adr/0046", preparation["package_id"])
    assert decided["decision_path"].startswith("release/decisions/soil/")
    assert not (root / "release/active").exists()


def test_evidence_is_one_bundle_per_station_and_depth(tmp_path):
    root, preparation = prepared(tmp_path, admitted=True)
    manifest, values = soil_release._snapshot(root, preparation["package_id"])
    entries = values["evidence.json"]["entries"]
    assert [(e["station_id"], e["series"]) for e in entries] == SOIL.evidence_keys()
    assert len(entries) == 10
    candidate = values["candidate.json"]
    for entry in entries:
        members = entry["bundle"]["evidence_refs"]
        assert members[0]["ref"] == f"kfm://soil/station/{entry['station_id']}/depth-{entry['series']}cm/" + manifest["candidate_id"].split(":")[1]
        records = [r for r in candidate["observations"] if r["station_id"] == entry["station_id"] and r["depth_cm"] == entry["series"]]
        assert [m["ref"] for m in members[1:]] == [r["evidence_ref"] for r in records]
        assert len(members) == 61
    # Every observation is in exactly one bundle.
    refs = [m["ref"] for e in entries for m in e["bundle"]["evidence_refs"][1:]]
    assert sorted(refs) == sorted(r["evidence_ref"] for r in candidate["observations"])


@pytest.mark.parametrize("forge", ["drop", "duplicate", "missing_series", "string_series", "move"])
def test_a_resealed_package_with_wrong_depth_bundles_is_refused(tmp_path, forge):
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
    elif forge == "missing_series":
        del entries[0]["series"]
        expected = "SERIES_EVIDENCE_MISMATCH"
    elif forge == "string_series":
        entries[0]["series"] = "5"
        expected = "SERIES_EVIDENCE_MISMATCH"
    else:
        # Swap two depths' labels: each bundle now claims the other depth's values.
        entries[0]["series"], entries[1]["series"] = entries[1]["series"], entries[0]["series"]
        expected = "DATASET_EVIDENCE_MISMATCH"
    with pytest.raises(ValueError, match=expected):
        validate_snapshot(reseal(snapshot, evidence), profile=SOIL)


def test_an_unadmitted_package_cannot_be_released(tmp_path):
    root, preparation = prepared(tmp_path, admitted=False)
    assert preparation["reason_code"] == "REVIEW_REQUIRED"
    with pytest.raises(ValueError, match="INDEPENDENT_REVIEW_REQUIRED"):
        soil_release.decide(root, preparation["package_id"], reviewer=OWNER, releaser=OWNER, valid_days=7, now=NOW)
    # A second reviewer does not clear the rights and sensitivity hold either.
    with pytest.raises(ValueError, match="RIGHTS_OR_SENSITIVITY_HOLD"):
        soil_release.decide(root, preparation["package_id"], reviewer="@reviewer", releaser=OWNER, valid_days=7, now=NOW)
    assert not (root / "release/decisions").exists()


def test_soil_water_and_weather_gates_never_accept_each_others_decisions(tmp_path):
    root, preparation = prepared(tmp_path, admitted=True)
    decision = soil_release.build_decision(preparation["package_id"], reviewer=OWNER, releaser=OWNER, now=NOW, valid_days=7)
    assert gate(root, preparation["package_id"], decision, **SOIL_GATE) == "ELIGIBLE"
    weather = {"decision_profile": WEATHER_DECISION_PROFILE, "licenses": WEATHER_SELF_RELEASE_LICENSES}
    assert gate(root, preparation["package_id"], decision) == "RELEASE_BINDING_MISMATCH"
    assert gate(root, preparation["package_id"], decision, **weather) == "RELEASE_BINDING_MISMATCH"
    # Neither the water nor the weather license list admits the USCRN license for self-release.
    assert gate(root, preparation["package_id"], {**decision, "profile": WEATHER_DECISION_PROFILE}, **weather) == "INDEPENDENT_REVIEW_REQUIRED"
    assert gate(root, preparation["package_id"], {**decision, "profile": "kfm.water-release-decision/v1"}) == "INDEPENDENT_REVIEW_REQUIRED"


def test_snapshot_profiles_do_not_cross(tmp_path):
    root, preparation = prepared(tmp_path, admitted=True)
    raw = snapshot_path(root, preparation["package_id"]).read_bytes()
    assert validate_snapshot(raw, profile=SOIL)[0]["profile"] == "kfm.soil-snapshot/v1"
    for profile in (WATER, WEATHER):
        with pytest.raises(ValueError, match="MANIFEST_PROFILE_INVALID"):
            validate_snapshot(raw, profile=profile)


def test_license_lists_match_the_admitted_descriptor_and_are_disjoint():
    descriptor = json.loads(uscrn_daily_admission.DESCRIPTOR.read_text())
    assert descriptor["review_state"] == "approved" and descriptor["public_release"]["allowed"] is True
    assert SOIL_SELF_RELEASE_LICENSES == {descriptor["rights"]["license_or_terms"]}
    assert uscrn_daily_admission.load_admission()["license"] in SOIL_SELF_RELEASE_LICENSES
    assert not SOIL_SELF_RELEASE_LICENSES & (SELF_RELEASE_LICENSES | WEATHER_SELF_RELEASE_LICENSES)


def test_decisions_are_bounded_and_ids_checked(tmp_path):
    root, preparation = prepared(tmp_path, admitted=True)
    for days in (0, 31):
        with pytest.raises(ValueError, match="VALID_DAYS_OUT_OF_RANGE"):
            soil_release.decide(root, preparation["package_id"], reviewer=OWNER, releaser=OWNER, valid_days=days, now=NOW)
    with pytest.raises(ValueError, match="PACKAGE_ID_INVALID"):
        soil_release.decide(root, "../../x", reviewer=OWNER, releaser=OWNER, valid_days=7, now=NOW)
    with pytest.raises(ValueError, match="INVALID_CANDIDATE_ID"):
        soil_release.prepare(root, "sha256:../x")


def test_an_expired_decision_is_not_eligible(tmp_path):
    root, preparation = prepared(tmp_path, admitted=True)
    decision = soil_release.build_decision(preparation["package_id"], reviewer=OWNER, releaser=OWNER, now=NOW, valid_days=1)
    manifest, values = soil_release._snapshot(root, preparation["package_id"])
    later = (NOW + timedelta(days=2)).strftime("%Y-%m-%dT%H:%M:%SZ")
    assert serving_gate(manifest, values["evidence.json"], decision, now=later, **SOIL_GATE) == "RELEASE_TIME_INVALID"


def test_preparation_is_deterministic(tmp_path):
    root, first = prepared(tmp_path, admitted=True)
    assert soil_release.prepare(root, first["candidate_id"], admitted_source=True) == first
    path = snapshot_path(root, first["package_id"])
    assert canonical_bytes(json.loads(path.read_text())) == path.read_bytes()


def test_decide_replays_evidence_and_refuses_a_rehashed_package_with_stale_bundles(tmp_path):
    root, preparation = prepared(tmp_path, admitted=True)
    snapshot = json.loads(snapshot_path(root, preparation["package_id"]).read_text())
    evidence = json.loads(snapshot["artifacts"]["evidence.json"])
    evidence["entries"][0]["bundle"]["spec_hash"]["value"] = "sha256:" + "0" * 64
    raw = reseal(snapshot, evidence)
    package_id = snapshot["manifest"]["package_id"]
    forged = snapshot_path(root, package_id)
    forged.parent.mkdir(parents=True)
    forged.write_bytes(raw)
    with pytest.raises(ValueError, match="EVIDENCE_DIGEST_MISMATCH"):
        soil_release.decide(root, package_id, reviewer=OWNER, releaser=OWNER, valid_days=7, now=NOW)
    assert not (root / "release/decisions").exists()


def test_cli_reports_a_reason_code_on_refusal(tmp_path, capsys):
    root, preparation = prepared(tmp_path, admitted=False)
    code = soil_release.main(["decide", "--root", str(root), "--package-id", preparation["package_id"],
                              "--reviewer", OWNER, "--releaser", OWNER])
    assert (code, json.loads(capsys.readouterr().out)) == (1, {"outcome": "ERROR", "reason_code": "INDEPENDENT_REVIEW_REQUIRED"})
