"""GHCN-Daily release (ADR-0045): admitted package -> owner decision; gate denials; water/weather isolation."""
from datetime import datetime, timedelta, timezone
import json

import pytest

from connectors_core.captured_json import canonical_bytes
from pipelines.domains.atmosphere import ghcnd_daily_admission
from policy_runtime.core import (
    SELF_RELEASE_LICENSES, WATER_DECISION_PROFILE, WEATHER_DECISION_PROFILE, WEATHER_SELF_RELEASE_LICENSES, serving_gate,
)
from release.core import WATER, WEATHER, validate_snapshot
from tests.domains.atmosphere.ghcnd_daily_fixtures import acquired
from tools.local_data import ghcnd_daily_pilot
from tools.local_data.manage import init_store
from tools.release import weather_release

OWNER = "@bartytime4life"
NOW = datetime(2026, 10, 11, 13, 0, tzinfo=timezone.utc)


def prepared(tmp_path, *, admitted):
    root = tmp_path / "store"
    init_store(root)
    candidate_id = ghcnd_daily_pilot.stage(root, acquired())["candidate_id"]
    return root, weather_release.prepare(root, candidate_id, admitted_source=admitted)


def gate(root, package_id, decision, **profile):
    manifest, values = weather_release._snapshot(root, package_id)
    return serving_gate(manifest, values["evidence.json"], decision, now=decision["released_at"], **profile)


def test_owner_releases_an_admitted_weather_package(tmp_path, capsys):
    root, preparation = prepared(tmp_path, admitted=True)
    assert (preparation["reason_code"], preparation["admitted_source"]) == ("RELEASE_DECISION_REQUIRED", "kfm://source/noaa-ghcnd")
    code = weather_release.main(["decide", "--root", str(root), "--package-id", preparation["package_id"],
                                 "--reviewer", OWNER, "--releaser", OWNER])
    decided = json.loads(capsys.readouterr().out)
    assert (code, decided["outcome"], decided["activated"]) == (0, "DECIDED", False)
    decision = json.loads((root / decided["decision_path"]).read_text())
    assert (decision["profile"], decision["policy_ref"], decision["package_id"]) == (
        WEATHER_DECISION_PROFILE, "kfm://adr/0045", preparation["package_id"])
    assert decided["decision_path"].startswith("release/decisions/atmosphere/")
    assert not (root / "release/active").exists()


def test_an_unadmitted_package_cannot_be_released(tmp_path):
    root, preparation = prepared(tmp_path, admitted=False)
    assert preparation["reason_code"] == "REVIEW_REQUIRED"
    with pytest.raises(ValueError, match="INDEPENDENT_REVIEW_REQUIRED"):
        weather_release.decide(root, preparation["package_id"], reviewer=OWNER, releaser=OWNER, valid_days=7, now=NOW)
    # A second reviewer does not clear the rights and sensitivity hold either.
    with pytest.raises(ValueError, match="RIGHTS_OR_SENSITIVITY_HOLD"):
        weather_release.decide(root, preparation["package_id"], reviewer="@reviewer", releaser=OWNER, valid_days=7, now=NOW)
    assert not (root / "release/decisions").exists()


def test_water_and_weather_gates_never_accept_each_others_decisions(tmp_path):
    root, preparation = prepared(tmp_path, admitted=True)
    weather_decision = weather_release.build_decision(preparation["package_id"], reviewer=OWNER, releaser=OWNER, now=NOW, valid_days=7)
    weather = {"decision_profile": WEATHER_DECISION_PROFILE, "licenses": WEATHER_SELF_RELEASE_LICENSES}
    assert gate(root, preparation["package_id"], weather_decision, **weather) == "ELIGIBLE"
    # The water gate (defaults) refuses a weather decision outright.
    assert gate(root, preparation["package_id"], weather_decision) == "RELEASE_BINDING_MISMATCH"
    # A water-profiled decision is refused by the weather gate.
    water_profiled = {**weather_decision, "profile": WATER_DECISION_PROFILE}
    assert gate(root, preparation["package_id"], water_profiled, **weather) == "RELEASE_BINDING_MISMATCH"
    # The water license list does not admit the NOAA license for self-release.
    assert gate(root, preparation["package_id"], water_profiled) == "INDEPENDENT_REVIEW_REQUIRED"


def test_snapshot_profiles_do_not_cross(tmp_path):
    root, preparation = prepared(tmp_path, admitted=True)
    raw = (root / "release/candidates/atmosphere" / preparation["package_id"].split(":")[1] / "snapshot.json").read_bytes()
    assert validate_snapshot(raw, profile=WEATHER)[0]["profile"] == "kfm.weather-snapshot/v1"
    with pytest.raises(ValueError, match="MANIFEST_PROFILE_INVALID"):
        validate_snapshot(raw)
    with pytest.raises(ValueError, match="MANIFEST_PROFILE_INVALID"):
        validate_snapshot(raw, profile=WATER)


def test_license_lists_match_the_admitted_descriptors():
    descriptor = json.loads(ghcnd_daily_admission.DESCRIPTOR.read_text())
    assert descriptor["review_state"] == "approved" and descriptor["public_release"]["allowed"] is True
    assert WEATHER_SELF_RELEASE_LICENSES == {descriptor["rights"]["license_or_terms"]}
    assert ghcnd_daily_admission.load_admission()["license"] in WEATHER_SELF_RELEASE_LICENSES
    assert not WEATHER_SELF_RELEASE_LICENSES & SELF_RELEASE_LICENSES


def test_decisions_are_bounded_and_ids_checked(tmp_path):
    root, preparation = prepared(tmp_path, admitted=True)
    for days in (0, 31):
        with pytest.raises(ValueError, match="VALID_DAYS_OUT_OF_RANGE"):
            weather_release.decide(root, preparation["package_id"], reviewer=OWNER, releaser=OWNER, valid_days=days, now=NOW)
    with pytest.raises(ValueError, match="PACKAGE_ID_INVALID"):
        weather_release.decide(root, "../../x", reviewer=OWNER, releaser=OWNER, valid_days=7, now=NOW)
    with pytest.raises(ValueError, match="INVALID_CANDIDATE_ID"):
        weather_release.prepare(root, "sha256:../x")


def test_an_expired_decision_is_not_eligible(tmp_path):
    root, preparation = prepared(tmp_path, admitted=True)
    decision = weather_release.build_decision(preparation["package_id"], reviewer=OWNER, releaser=OWNER, now=NOW, valid_days=1)
    manifest, values = weather_release._snapshot(root, preparation["package_id"])
    later = (NOW + timedelta(days=2)).strftime("%Y-%m-%dT%H:%M:%SZ")
    assert serving_gate(manifest, values["evidence.json"], decision, now=later, decision_profile=WEATHER_DECISION_PROFILE,
                        licenses=WEATHER_SELF_RELEASE_LICENSES) == "RELEASE_TIME_INVALID"


def test_preparation_is_deterministic(tmp_path):
    root, first = prepared(tmp_path, admitted=True)
    again = weather_release.prepare(root, first["candidate_id"], admitted_source=True)
    assert again == first
    path = root / "release/candidates/atmosphere" / first["package_id"].split(":")[1] / "snapshot.json"
    assert canonical_bytes(json.loads(path.read_text())) == path.read_bytes()


def test_decide_replays_evidence_and_refuses_a_rehashed_package_with_stale_bundles(tmp_path):
    # Outer artifact and package hashes are regenerated, but one bundle's spec_hash is stale.
    from connectors_core.captured_json import digest_bytes
    from hashing import compute_spec_hash
    root, preparation = prepared(tmp_path, admitted=True)
    path = root / "release/candidates/atmosphere" / preparation["package_id"].split(":")[1] / "snapshot.json"
    snapshot = json.loads(path.read_text())
    evidence = json.loads(snapshot["artifacts"]["evidence.json"])
    evidence["entries"][0]["bundle"]["spec_hash"]["value"] = "sha256:" + "0" * 64
    text = canonical_bytes(evidence).decode()
    manifest = snapshot["manifest"]
    manifest["artifacts"]["evidence.json"] = digest_bytes(text.encode())
    snapshot["artifacts"]["evidence.json"] = text
    manifest["package_id"] = compute_spec_hash({k: v for k, v in manifest.items() if k != "package_id"})
    forged = root / "release/candidates/atmosphere" / manifest["package_id"].split(":")[1] / "snapshot.json"
    forged.parent.mkdir(parents=True)
    forged.write_bytes(canonical_bytes(snapshot))
    with pytest.raises(ValueError, match="EVIDENCE_DIGEST_MISMATCH"):
        weather_release.decide(root, manifest["package_id"], reviewer=OWNER, releaser=OWNER, valid_days=7, now=NOW)
    assert not (root / "release/decisions").exists()


def test_decide_revalidates_the_candidate_and_refuses_a_resealed_semantic_change(tmp_path, monkeypatch):
    from connectors_core.captured_json import digest_bytes
    from pipelines.domains.atmosphere import ghcnd_daily_package
    root, preparation = prepared(tmp_path, admitted=True)
    _, values = weather_release._snapshot(root, preparation["package_id"])
    candidate = values["candidate.json"]
    candidate["coverage"] = "EMPTY"
    candidate["candidate_id"] = digest_bytes(canonical_bytes({k: v for k, v in candidate.items() if k != "candidate_id"}))

    def lenient(value):
        report = {**values["validation.json"], "candidate_id": value["candidate_id"]}
        report.pop("receipt_digest")
        report["receipt_digest"] = digest_bytes(canonical_bytes(report))
        return report
    monkeypatch.setattr(ghcnd_daily_package, "validate_candidate", lenient)
    snapshot = ghcnd_daily_package.prepare_weather_package(candidate, admission=ghcnd_daily_admission.load_admission())
    package_id = snapshot["manifest"]["package_id"]
    path = root / "release/candidates/atmosphere" / package_id.split(":")[1] / "snapshot.json"
    path.parent.mkdir(parents=True)
    path.write_bytes(canonical_bytes(snapshot))
    with pytest.raises(ValueError, match="COVERAGE_OR_FRESHNESS_MISMATCH"):
        weather_release.decide(root, package_id, reviewer=OWNER, releaser=OWNER, valid_days=7, now=NOW)
    assert not (root / "release/decisions").exists()
