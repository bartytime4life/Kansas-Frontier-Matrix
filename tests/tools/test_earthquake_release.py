"""USGS ComCat earthquake release (ADR-0049): admitted package -> owner decision; gate denials; family isolation; month bundles."""
from copy import deepcopy
from datetime import datetime, timedelta, timezone
import json
import shutil

import pytest

from connectors_core.captured_json import canonical_bytes, digest_bytes
from hashing import compute_spec_hash
from pipelines.domains.hazards import earthquake_admission, earthquake_package
from pipelines.domains.hazards.earthquake_normalize import normalize_capture
from policy_runtime.core import (
    EARTHQUAKE_DECISION_PROFILE, EARTHQUAKE_SELF_RELEASE_LICENSES, SELF_RELEASE_LICENSES, SOIL_SELF_RELEASE_LICENSES,
    STORM_EVENTS_DECISION_PROFILE, STORM_EVENTS_SELF_RELEASE_LICENSES, WEATHER_SELF_RELEASE_LICENSES, serving_gate,
)
from release.core import EARTHQUAKES, MAX_PACKAGE_BYTES, MONTH_PART_SIZE, SOIL, STORM_EVENTS, WATER, WEATHER, validate_snapshot
from tests.domains.hazards.earthquake_fixtures import acquired
from tools.local_data import earthquake_pilot
from tools.local_data.manage import init_store
from tools.release import earthquake_release

OWNER = "@bartytime4life"
NOW = datetime(2026, 10, 12, 15, 0, tzinfo=timezone.utc)
QUAKE_GATE = {"decision_profile": EARTHQUAKE_DECISION_PROFILE, "licenses": EARTHQUAKE_SELF_RELEASE_LICENSES}


def many_in_may(count, place="synthetic: 9 km SW of Wellington, Kansas"):
    """Add ``count`` synthetic May events, one minute apart, to the May page."""
    def mutate(key, document):
        if key != "2025-05":
            return document
        template = document["features"][0]
        for i in range(count):
            feature = deepcopy(template)
            feature["id"] = f"us7000m{i:04d}"
            feature["properties"].update(ids=f",us7000m{i:04d},", time=1746662400000 + i * 60000, place=place, status="reviewed")
            feature["geometry"]["coordinates"] = [-97.4, 37.25, 4.5]
            document["features"].append(feature)
        document["features"].sort(key=lambda f: f["properties"]["time"])
        document["metadata"]["count"] = len(document["features"])
        return document
    return mutate


def spread(count, place):
    """``count`` synthetic events over June to December (months with no fixture page)."""
    months = [f"2025-{m:02d}" for m in range(6, 13)]
    share = {key: count // len(months) + (i < count % len(months)) for i, key in enumerate(months)}

    def mutate(key, document):
        if key not in share:
            return document
        first = int(datetime.fromisoformat(key + "-02T00:00:00+00:00").timestamp() * 1000)
        features = [{"type": "Feature", "id": f"us7000{key[5:]}{i:04d}",
                     "geometry": {"type": "Point", "coordinates": [-97.4123, 37.2512, 4.512]},
                     "properties": {"time": first + i * 60000, "updated": first + i * 60000 + 5000, "mag": 2.35,
                                    "magType": "ml", "type": "earthquake", "status": "reviewed", "net": "us",
                                    "place": place, "ids": f",us7000{key[5:]}{i:04d},ok2025{key[5:]}{i:04d},"}}
                    for i in range(share[key])]
        return {"type": "FeatureCollection", "metadata": {"status": 200, "count": len(features), "generated": first},
                "features": features}
    return mutate


def prepared(tmp_path, *, admitted, mutate=None):
    root = tmp_path / "store"
    init_store(root)
    candidate_id = earthquake_pilot.stage(root, acquired(mutate))["candidate_id"]
    return root, earthquake_release.prepare(root, candidate_id, admitted_source=admitted)


def snapshot_path(root, package_id):
    return root / "release/candidates/earthquakes" / package_id.split(":")[1] / "snapshot.json"


def gate(root, package_id, decision, **profile):
    manifest, values = earthquake_release._snapshot(root, package_id)
    return serving_gate(manifest, values["evidence.json"], decision, now=decision["released_at"], **profile)


def reseal(snapshot, evidence):
    """Rewrite evidence.json and every outer digest, as a forger would."""
    text = canonical_bytes(evidence).decode()
    manifest = snapshot["manifest"]
    manifest["artifacts"]["evidence.json"] = digest_bytes(text.encode())
    snapshot["artifacts"]["evidence.json"] = text
    manifest["package_id"] = compute_spec_hash({k: v for k, v in manifest.items() if k != "package_id"})
    return canonical_bytes(snapshot)


def plant(root, snapshot_or_raw):
    raw = snapshot_or_raw if isinstance(snapshot_or_raw, bytes) else canonical_bytes(snapshot_or_raw)
    package_id = json.loads(raw)["manifest"]["package_id"]
    path = snapshot_path(root, package_id)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(raw)
    return package_id


def test_owner_releases_an_admitted_earthquake_package(tmp_path, capsys):
    root, preparation = prepared(tmp_path, admitted=True)
    assert (preparation["reason_code"], preparation["admitted_source"]) == ("RELEASE_DECISION_REQUIRED", "kfm://source/usgs-earthquakes")
    code = earthquake_release.main(["decide", "--root", str(root), "--package-id", preparation["package_id"],
                                    "--reviewer", OWNER, "--releaser", OWNER])
    decided = json.loads(capsys.readouterr().out)
    assert (code, decided["outcome"], decided["activated"]) == (0, "DECIDED", False)
    decision = json.loads((root / decided["decision_path"]).read_text())
    assert (decision["profile"], decision["policy_ref"], decision["package_id"]) == (
        EARTHQUAKE_DECISION_PROFILE, "kfm://adr/0049", preparation["package_id"])
    assert decided["decision_path"].startswith("release/decisions/earthquakes/")
    assert not (root / "release/active").exists()


def test_manifest_covers_the_data_year_and_the_catalog_summarizes_it(tmp_path):
    root, preparation = prepared(tmp_path, admitted=True)
    manifest, values = earthquake_release._snapshot(root, preparation["package_id"])
    assert (manifest["start"], manifest["end"], manifest["profile"]) == ("2025-01-01", "2025-12-31", "kfm.earthquake-snapshot/v1")
    dataset = values["catalog.json"]["dataset"]
    assert (dataset["observation_count"], dataset["withheld_counts"], dataset["context_margin_count"]) == (5, {"STATUS_DELETED": 1}, 1)
    assert (dataset["review_status"], dataset["magnitude_range"]) == ({"automatic": 1, "reviewed": 4}, [1.9, 2.8])
    assert (dataset["year_state"], dataset["coverage"], dataset["interval"]["basis"]) == ("OPEN", "NOT_ESTABLISHED", "origin time, UTC")
    bundle = values["evidence.json"]["entries"][0]["bundle"]
    assert bundle["citations"][0].startswith("https://earthquake.usgs.gov/fdsnws/event/1/query?")
    assert "not the state boundary" in bundle["claim_scope"]


def test_evidence_is_one_bundle_per_utc_month_with_events(tmp_path):
    root, preparation = prepared(tmp_path, admitted=True)
    manifest, values = earthquake_release._snapshot(root, preparation["package_id"])
    entries = values["evidence.json"]["entries"]
    # The midnight boundary event belongs to February, its UTC origin month.
    assert [(e["month"], e["part"]) for e in entries] == [(1, 1), (2, 1), (5, 1)]
    candidate = values["candidate.json"]
    may = entries[2]["bundle"]["evidence_refs"]
    assert may[0]["ref"] == "kfm://hazards/earthquakes/2025-05/part-1/" + manifest["candidate_id"].split(":")[1]
    assert [m["ref"] for m in may[1:]] == [r["evidence_ref"] for r in candidate["observations"] if r["origin_utc"][5:7] == "05"]
    assert {m["kind"] for e in entries for m in e["bundle"]["evidence_refs"][1:]} == {"record"}
    refs = [m["ref"] for e in entries for m in e["bundle"]["evidence_refs"][1:]]
    assert sorted(refs) == sorted(r["evidence_ref"] for r in candidate["observations"])


def test_a_busy_month_splits_into_numbered_parts(tmp_path):
    root, preparation = prepared(tmp_path, admitted=True, mutate=many_in_may(2 * MONTH_PART_SIZE))
    _, values = earthquake_release._snapshot(root, preparation["package_id"])
    may = [e for e in values["evidence.json"]["entries"] if e["month"] == 5]
    # 3 fixture May events + 254 added = 257 records: 127 + 127 + 3.
    assert [(e["part"], len(e["bundle"]["evidence_refs"]) - 1) for e in may] == [(1, 127), (2, 127), (3, 3)]
    assert "part 3 of 3" in may[2]["bundle"]["claim_scope"]


def test_the_event_cap_keeps_a_full_package_inside_the_byte_limit():
    # A long place text and an alias on every event: the cap, not the byte limit, must refuse first.
    place = "synthetic: " + "x" * 120
    source = acquired(spread(EARTHQUAKES.max_observations - 5, place))
    candidate = normalize_capture(source.manifest, source.objects)
    assert len(candidate["observations"]) == EARTHQUAKES.max_observations
    snapshot = earthquake_package.prepare_earthquake_package(candidate, admission=earthquake_admission.load_admission())
    assert len(canonical_bytes(snapshot)) < MAX_PACKAGE_BYTES
    over = acquired(spread(EARTHQUAKES.max_observations - 4, place))
    with pytest.raises(ValueError, match="OBSERVATION_LIMIT"):
        earthquake_package.prepare_earthquake_package(normalize_capture(over.manifest, over.objects))


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
        entries[0]["month"], entries[1]["month"] = entries[1]["month"], entries[0]["month"]
        entries[0], entries[1] = entries[1], entries[0]
        expected = "DATASET_EVIDENCE_MISMATCH"
    with pytest.raises(ValueError, match=expected):
        validate_snapshot(reseal(snapshot, evidence), profile=EARTHQUAKES)


def test_an_unadmitted_package_cannot_be_released(tmp_path):
    root, preparation = prepared(tmp_path, admitted=False)
    assert preparation["reason_code"] == "REVIEW_REQUIRED"
    with pytest.raises(ValueError, match="INDEPENDENT_REVIEW_REQUIRED"):
        earthquake_release.decide(root, preparation["package_id"], reviewer=OWNER, releaser=OWNER, valid_days=7, now=NOW)
    with pytest.raises(ValueError, match="RIGHTS_OR_SENSITIVITY_HOLD"):
        earthquake_release.decide(root, preparation["package_id"], reviewer="@reviewer", releaser=OWNER, valid_days=7, now=NOW)
    assert not (root / "release/decisions").exists()


def test_earthquake_and_other_gates_never_accept_each_others_decisions(tmp_path):
    root, preparation = prepared(tmp_path, admitted=True)
    decision = earthquake_release.build_decision(preparation["package_id"], reviewer=OWNER, releaser=OWNER, now=NOW, valid_days=7)
    assert gate(root, preparation["package_id"], decision, **QUAKE_GATE) == "ELIGIBLE"
    storm = {"decision_profile": STORM_EVENTS_DECISION_PROFILE, "licenses": STORM_EVENTS_SELF_RELEASE_LICENSES}
    assert gate(root, preparation["package_id"], decision) == "RELEASE_BINDING_MISMATCH"
    assert gate(root, preparation["package_id"], decision, **storm) == "RELEASE_BINDING_MISMATCH"
    # No other family's license list admits the earthquake license for self-release.
    assert gate(root, preparation["package_id"], {**decision, "profile": STORM_EVENTS_DECISION_PROFILE}, **storm) == "INDEPENDENT_REVIEW_REQUIRED"
    assert gate(root, preparation["package_id"], {**decision, "profile": "kfm.water-release-decision/v1"}) == "INDEPENDENT_REVIEW_REQUIRED"


def test_snapshot_profiles_do_not_cross(tmp_path):
    root, preparation = prepared(tmp_path, admitted=True)
    raw = snapshot_path(root, preparation["package_id"]).read_bytes()
    assert validate_snapshot(raw, profile=EARTHQUAKES)[0]["profile"] == "kfm.earthquake-snapshot/v1"
    for profile in (WATER, WEATHER, SOIL, STORM_EVENTS):
        with pytest.raises(ValueError, match="MANIFEST_PROFILE_INVALID"):
            validate_snapshot(raw, profile=profile)


def test_license_lists_match_the_admitted_descriptor_and_are_disjoint():
    descriptor = json.loads(earthquake_admission.DESCRIPTOR.read_text())
    assert descriptor["review_state"] == "approved" and descriptor["public_release"]["allowed"] is True
    assert EARTHQUAKE_SELF_RELEASE_LICENSES == {descriptor["rights"]["license_or_terms"]}
    assert earthquake_admission.load_admission()["license"] in EARTHQUAKE_SELF_RELEASE_LICENSES
    others = SELF_RELEASE_LICENSES | WEATHER_SELF_RELEASE_LICENSES | SOIL_SELF_RELEASE_LICENSES | STORM_EVENTS_SELF_RELEASE_LICENSES
    assert not EARTHQUAKE_SELF_RELEASE_LICENSES & others


def test_decisions_are_bounded_and_ids_checked(tmp_path):
    root, preparation = prepared(tmp_path, admitted=True)
    for days in (0, 31):
        with pytest.raises(ValueError, match="VALID_DAYS_OUT_OF_RANGE"):
            earthquake_release.decide(root, preparation["package_id"], reviewer=OWNER, releaser=OWNER, valid_days=days, now=NOW)
    with pytest.raises(ValueError, match="PACKAGE_ID_INVALID"):
        earthquake_release.decide(root, "../../x", reviewer=OWNER, releaser=OWNER, valid_days=7, now=NOW)
    with pytest.raises(ValueError, match="INVALID_CANDIDATE_ID"):
        earthquake_release.prepare(root, "sha256:../x")


def test_an_expired_decision_is_not_eligible(tmp_path):
    root, preparation = prepared(tmp_path, admitted=True)
    decision = earthquake_release.build_decision(preparation["package_id"], reviewer=OWNER, releaser=OWNER, now=NOW, valid_days=1)
    manifest, values = earthquake_release._snapshot(root, preparation["package_id"])
    later = (NOW + timedelta(days=2)).strftime("%Y-%m-%dT%H:%M:%SZ")
    assert serving_gate(manifest, values["evidence.json"], decision, now=later, **QUAKE_GATE) == "RELEASE_TIME_INVALID"


def test_preparation_is_deterministic(tmp_path):
    root, first = prepared(tmp_path, admitted=True)
    assert earthquake_release.prepare(root, first["candidate_id"], admitted_source=True) == first
    path = snapshot_path(root, first["package_id"])
    assert canonical_bytes(json.loads(path.read_text())) == path.read_bytes()


def test_a_year_without_events_has_nothing_to_package():
    source = acquired(lambda key, document: None)
    candidate = normalize_capture(source.manifest, source.objects)
    assert candidate["observations"] == [] and [m["query_status"] for m in candidate["months"]] == [204] * 12
    with pytest.raises(ValueError, match="NO_EVENTS_TO_PACKAGE"):
        earthquake_package.prepare_earthquake_package(candidate, admission=earthquake_admission.load_admission())


def test_decide_refuses_a_rehashed_package_with_stale_bundles(tmp_path):
    root, preparation = prepared(tmp_path, admitted=True)
    snapshot = json.loads(snapshot_path(root, preparation["package_id"]).read_text())
    evidence = json.loads(snapshot["artifacts"]["evidence.json"])
    evidence["entries"][0]["bundle"]["spec_hash"]["value"] = "sha256:" + "0" * 64
    package_id = plant(root, reseal(snapshot, evidence))
    with pytest.raises(ValueError, match="PACKAGE_NOT_REPRODUCIBLE"):
        earthquake_release.decide(root, package_id, reviewer=OWNER, releaser=OWNER, valid_days=7, now=NOW)
    assert not (root / "release/decisions").exists()


def test_cli_reports_a_reason_code_on_refusal(tmp_path, capsys):
    root, preparation = prepared(tmp_path, admitted=False)
    code = earthquake_release.main(["decide", "--root", str(root), "--package-id", preparation["package_id"],
                                    "--reviewer", OWNER, "--releaser", OWNER])
    assert (code, json.loads(capsys.readouterr().out)) == (1, {"outcome": "ERROR", "reason_code": "INDEPENDENT_REVIEW_REQUIRED"})


def test_decide_refuses_a_package_whose_receipt_differs_from_revalidation(tmp_path, monkeypatch):
    root, preparation = prepared(tmp_path, admitted=True)
    _, values = earthquake_release._snapshot(root, preparation["package_id"])

    def miscounting(value):
        report = {k: v for k, v in values["validation.json"].items() if k != "receipt_digest"}
        report["withheld"] += 1
        report["receipt_digest"] = digest_bytes(canonical_bytes(report))
        return report
    monkeypatch.setattr(earthquake_package, "validate_candidate", miscounting)
    package_id = plant(root, earthquake_package.prepare_earthquake_package(values["candidate.json"], admission=earthquake_admission.load_admission()))
    with pytest.raises(ValueError, match="VALIDATION_RECEIPT_MISMATCH"):
        earthquake_release.decide(root, package_id, reviewer=OWNER, releaser=OWNER, valid_days=7, now=NOW)


def test_decide_requires_the_candidate_to_match_its_stored_capture(tmp_path):
    # A magnitude is changed and every identity, receipt, bundle and outer hash is rebuilt by the
    # normal package builder; only the stored capture disagrees.
    root, preparation = prepared(tmp_path, admitted=True)
    _, values = earthquake_release._snapshot(root, preparation["package_id"])
    candidate = values["candidate.json"]
    record = candidate["observations"][0]
    record["magnitude"] = 4.6
    record["record_digest"] = digest_bytes(canonical_bytes({k: v for k, v in record.items() if k != "record_digest"}))
    candidate["candidate_id"] = digest_bytes(canonical_bytes({k: v for k, v in candidate.items() if k != "candidate_id"}))
    package_id = plant(root, earthquake_package.prepare_earthquake_package(candidate, admission=earthquake_admission.load_admission()))
    with pytest.raises(ValueError, match="CANDIDATE_CAPTURE_MISMATCH"):
        earthquake_release.decide(root, package_id, reviewer=OWNER, releaser=OWNER, valid_days=7, now=NOW)
    assert not (root / "release/decisions").exists()


def test_decide_refuses_a_package_whose_capture_is_not_in_the_store(tmp_path):
    root, preparation = prepared(tmp_path, admitted=True)
    runs = root / "data/quarantine" / earthquake_pilot.LANE / "runs"
    for manifest in runs.glob("*/manifest.json"):
        manifest.unlink()
    with pytest.raises(ValueError, match="CAPTURE_NOT_IN_STORE"):
        earthquake_release.decide(root, preparation["package_id"], reviewer=OWNER, releaser=OWNER, valid_days=7, now=NOW)
    shutil.rmtree(runs)
    with pytest.raises(ValueError, match="CAPTURE_NOT_IN_STORE"):
        earthquake_release.decide(root, preparation["package_id"], reviewer=OWNER, releaser=OWNER, valid_days=7, now=NOW)


def test_a_held_package_resealed_as_admitted_cannot_be_self_released(tmp_path):
    root, preparation = prepared(tmp_path, admitted=False)
    snapshot = json.loads(snapshot_path(root, preparation["package_id"]).read_text())
    evidence = json.loads(snapshot["artifacts"]["evidence.json"])
    license_text = earthquake_admission.load_admission()["license"]
    for entry in evidence["entries"]:
        bundle = entry["bundle"]
        bundle["rights"] = {"license": license_text}
        bundle["sensitivity"] = {**bundle["sensitivity"], "level": "public", "reason": "forged"}
        bundle["spec_hash"] = {"value": compute_spec_hash({k: v for k, v in bundle.items() if k != "spec_hash"})}
    raw = reseal(snapshot, evidence)
    manifest, values = validate_snapshot(raw, profile=EARTHQUAKES)  # the carrier checks alone accept it
    decision = earthquake_release.build_decision(manifest["package_id"], reviewer=OWNER, releaser=OWNER, now=NOW, valid_days=7)
    assert serving_gate(manifest, values["evidence.json"], decision, now=decision["released_at"], **QUAKE_GATE) == "ELIGIBLE"
    package_id = plant(root, raw)
    with pytest.raises(ValueError, match="PACKAGE_NOT_REPRODUCIBLE"):
        earthquake_release.decide(root, package_id, reviewer=OWNER, releaser=OWNER, valid_days=7, now=NOW)
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
        validate_snapshot(canonical_bytes(snapshot), profile=EARTHQUAKES)
