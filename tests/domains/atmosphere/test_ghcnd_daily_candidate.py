"""GHCN-Daily pilot: bounded capture, deterministic candidate, flag handling and tamper denial."""
from copy import deepcopy
import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator, FormatChecker

from connectors_core.captured_json import canonical_bytes, digest_bytes
from connectors.noaa.src.noaa import ghcnd
from connectors.noaa.src.noaa.ghcnd_daily_capture import STATIONS, capture, capture_keys, window
from pipelines.domains.atmosphere import ghcnd_daily_admission
from pipelines.domains.atmosphere.ghcnd_daily_normalize import normalize_capture
from pipelines.domains.atmosphere.ghcnd_daily_validate import SCHEMA, validate_candidate
from tests.domains.atmosphere.ghcnd_daily_fixtures import CAPTURED_AT, END, acquired, fetcher

ROOT = Path(__file__).resolve().parents[3]


def candidate(mutate=None):
    source = acquired(mutate)
    return normalize_capture(source.manifest, source.objects)


def reseal(value, key="candidate_id"):
    value[key] = digest_bytes(canonical_bytes({k: v for k, v in value.items() if k != key}))
    return value


def find(result, station, element, day):
    [record] = [r for r in result["observations"]
                if (r["station_id"], r["element"], r["observation_date"]) == (station, element, day)]
    return record


def test_capture_fetches_only_the_planned_objects_within_their_limits():
    fetch = fetcher()
    source = capture(END, fetcher=fetch, clock=lambda: CAPTURED_AT)
    assert [key for key, _ in fetch.calls] == capture_keys() == [
        "ghcnd-stations.txt", *[f"by_station/{s}.csv.gz" for s in STATIONS]]
    assert all(limit == ghcnd.METADATA["ghcnd-stations.txt"] if key == "ghcnd-stations.txt" else limit == ghcnd.STATION_BYTES
               for key, limit in fetch.calls)
    manifest = source.manifest
    assert (manifest["start"], manifest["end"], manifest["complete"]) == ("2026-09-11", END, True)
    assert manifest["capture_id"] == digest_bytes(canonical_bytes({k: v for k, v in manifest.items() if k != "capture_id"}))
    assert set(source.objects) == {page["sha256"] for page in manifest["pages"]}


def test_capture_refuses_failures_wrong_urls_and_future_windows():
    def failing(key, limit):
        raise OSError("connection reset")
    with pytest.raises(ValueError, match="SOURCE_FETCH_FAILED"):
        capture(END, fetcher=failing, clock=lambda: CAPTURED_AT)

    def redirected(key, limit):
        return b"x", {"source_url": "https://elsewhere.example/" + key, "retrieved_at": CAPTURED_AT}
    with pytest.raises(ValueError, match="SOURCE_RESPONSE_INVALID"):
        capture(END, fetcher=redirected, clock=lambda: CAPTURED_AT)
    with pytest.raises(ValueError, match="WINDOW_END_IN_FUTURE"):
        capture("2026-10-12", fetcher=fetcher(), clock=lambda: CAPTURED_AT)
    for bad in ("2026-13-01", "20261010", None):
        with pytest.raises(ValueError, match="WINDOW_END_INVALID"):
            window(bad)


def test_candidate_is_deterministic_bounded_and_schema_valid():
    first = candidate()
    assert first == candidate()
    assert (first["start"], first["end"], first["coverage"]) == ("2026-09-11", END, "COMPLETE")
    assert [s["id"] for s in first["stations"]] == list(STATIONS)
    assert first["stations"][0]["geometry"] == {"type": "Point", "coordinates": [-97.4331, 37.6497]}
    # 30 days x 3 elements, except Goodland, which stops after 2026-10-05.
    assert len(first["observations"]) == 3 * 90 + 3 * 25
    assert {r["element"] for r in first["observations"]} == {"PRCP", "TMAX", "TMIN"}
    assert min(r["observation_date"] for r in first["observations"]) == "2026-09-11"
    schema = Draft202012Validator(json.loads(SCHEMA.read_text()), format_checker=FormatChecker())
    for record in first["observations"]:
        schema.validate(record)
    report = validate_candidate(first)
    assert (report["outcome"], report["release_authorized"], report["withheld"]) == ("PASS", False, 3)


def test_flags_units_and_missing_values():
    result = candidate()
    trace = find(result, "USW00003928", "PRCP", "2026-09-20")
    assert (trace["value"], trace["trace"], trace["withheld"], trace["measurement_flag"]) == (0.0, True, None, "T")
    flagged = find(result, "USW00003928", "TMAX", "2026-09-21")
    assert (flagged["raw_value"], flagged["value"], flagged["withheld"], flagged["quality_flag"]) == (412, None, "QUALITY_FLAG", "I")
    missing = find(result, "USW00003928", "TMIN", "2026-09-22")
    assert (missing["raw_value"], missing["value"], missing["withheld"]) == (-9999, None, "MISSING")
    presumed_zero = find(result, "USW00013996", "PRCP", "2026-09-25")
    assert (presumed_zero["value"], presumed_zero["withheld"], presumed_zero["measurement_flag"]) == (None, "MISSING", "P")
    tmax = find(result, "USW00013985", "TMAX", "2026-09-11")
    assert (tmax["raw_value"], tmax["value"], tmax["unit"]) == (247, 24.7, "degC")
    assert find(result, "USW00013985", "PRCP", "2026-09-12")["unit"] == "mm"
    assert result["withheld_counts"]["USW00003928"] == {"MISSING": 1, "QUALITY_FLAG": 1}
    assert result["withheld_counts"]["USW00013996"] == {"MISSING": 1, "QUALITY_FLAG": 0}


def test_freshness_marks_a_station_that_stopped_reporting():
    result = candidate()
    assert result["freshness_at_capture"] == {"USW00003928": "RECENT", "USW00013985": "RECENT",
                                              "USW00013996": "RECENT", "USW00023065": "STALE"}


def test_identity_is_stable_across_value_revisions():
    def revise(key, text):
        return text.replace("USW00013985,20260915,PRCP,35,", "USW00013985,20260915,PRCP,30,")
    before, after = find(candidate(), "USW00013985", "PRCP", "2026-09-15"), find(candidate(revise), "USW00013985", "PRCP", "2026-09-15")
    assert before["id"] == after["id"] and before["record_digest"] != after["record_digest"]
    assert after["value"] == 3.0


@pytest.mark.parametrize("mutate, reason", [
    (lambda key, text: text.replace("USW00013996,", "USW00099999,", 1) if key.endswith("USW00013996.csv.gz") else text, "STATION_ROW_ID_OR_SHAPE"),
    (lambda key, text: text + text.splitlines()[5] + "\n" if key.endswith("USW00013985.csv.gz") else text, "DUPLICATE_STATION_DAY_ELEMENT"),
    (lambda key, text: text.replace(",TMAX,250,", ",TMAX,25x,", 1) if key.endswith("USW00003928.csv.gz") else text, "STATION_ROW_FORMAT"),
    (lambda key, text: "\n".join(l for l in text.splitlines() if not l.startswith("USW00023065")) if key == "ghcnd-stations.txt" else text, "STATION_LIST_MISMATCH"),
    (lambda key, text: text.replace("USW00013996  39.0725  -95.6261  270.4 KS", "USW00013996  39.0725  -95.6261  270.4 MO") if key == "ghcnd-stations.txt" else text, "STATION_LIST_MISMATCH"),
])
def test_invalid_source_rows_are_refused(mutate, reason):
    with pytest.raises(ValueError, match=reason):
        candidate(mutate)


def test_capture_closure_is_checked():
    source = acquired()
    manifest, objects = deepcopy(source.manifest), dict(source.objects)
    with pytest.raises(ValueError, match="CAPTURE_DIGEST_MISMATCH"):
        normalize_capture({**manifest, "end": "2026-10-09"}, objects)
    dropped = {k: v for k, v in objects.items() if k != manifest["pages"][2]["sha256"]}
    with pytest.raises(ValueError, match="PAGE_DIGEST_MISMATCH"):
        normalize_capture(manifest, dropped)
    reordered = deepcopy(manifest)
    reordered["pages"] = reordered["pages"][::-1]
    with pytest.raises(ValueError, match="CAPTURE_PAGE_CHAIN_MISMATCH"):
        normalize_capture(reseal(reordered, "capture_id"), objects)
    widened = reseal({**deepcopy(manifest), "station_ids": [*STATIONS, "USC00140010"]}, "capture_id")
    with pytest.raises(ValueError, match="CAPTURE_SCOPE_MISMATCH"):
        normalize_capture(widened, objects)


@pytest.mark.parametrize("tamper, reason", [
    (lambda c: c["observations"][0].update(value=99.9), "OBSERVATION_DIGEST_MISMATCH"),
    (lambda c: c.update(review_state="APPROVED"), "CANDIDATE_AUTHORITY_OR_PROFILE_INVALID"),
    (lambda c: c.update(coverage="PARTIAL"), "COVERAGE_OR_FRESHNESS_MISMATCH"),
    (lambda c: c["stations"].pop(), "STATION_SCOPE_INVALID"),
    (lambda c: c["observations"].reverse(), "OBSERVATION_ORDER_INVALID"),
])
def test_tampered_candidates_are_refused(tamper, reason):
    value = candidate()
    tamper(value)
    with pytest.raises(ValueError, match=reason):
        validate_candidate(reseal(value))


def test_a_reported_value_that_disagrees_with_its_flags_is_refused():
    value = candidate()
    record = next(r for r in value["observations"] if r["withheld"] == "QUALITY_FLAG")
    record["value"], record["withheld"] = 41.2, None
    record["record_digest"] = digest_bytes(canonical_bytes({k: v for k, v in record.items() if k != "record_digest"}))
    with pytest.raises(ValueError, match="OBSERVATION_VALUE_MISMATCH"):
        validate_candidate(reseal(value))


def test_descriptor_is_schema_valid_and_not_admitted_until_the_owner_approves(tmp_path):
    with pytest.raises(ValueError, match="SOURCE_NOT_ADMITTED"):
        ghcnd_daily_admission.load_admission()
    descriptor = json.loads(ghcnd_daily_admission.DESCRIPTOR.read_text())
    assert descriptor["review_state"] == "needs_review" and descriptor["public_release"]["allowed"] is False
    approved = deepcopy(descriptor)
    approved["review_state"], approved["public_release"]["allowed"] = "approved", True
    approved["lifecycle"]["registry_state"] = "active"
    path = tmp_path / "noaa_ghcnd.yaml"
    path.write_text(json.dumps(approved))
    admission = ghcnd_daily_admission.load_admission(path)
    assert admission["source_ref"] == "kfm://source/noaa-ghcnd"
    assert admission["license"].startswith("U.S. Public Domain")


def test_two_captures_of_the_same_bytes_have_the_same_identity():
    # Receipts and quarantine paths are keyed by these digests; the fixtures gzip with mtime=0.
    assert acquired().manifest == acquired().manifest
