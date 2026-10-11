"""USCRN daily soil pilot: bounded capture, header profile, deterministic candidate, withholding and tamper denial."""
from copy import deepcopy
import json

import pytest
from jsonschema import Draft202012Validator, FormatChecker

from connectors_core.captured_json import canonical_bytes, digest_bytes
from connectors.noaa.src.noaa import uscrn_daily
from connectors.noaa.src.noaa.uscrn_daily_capture import STATIONS, capture, capture_keys, window
from pipelines.domains.soil import uscrn_daily_admission
from pipelines.domains.soil.uscrn_daily_normalize import normalize_capture
from pipelines.domains.soil.uscrn_daily_validate import SCHEMA, validate_candidate
from tests.domains.soil.uscrn_daily_fixtures import CAPTURED_AT, END, acquired, fetcher

MANHATTAN = "2026/CRND0103-2026-KS_Manhattan_6_SSW.txt"


def candidate(mutate=None):
    source = acquired(mutate)
    return normalize_capture(source.manifest, source.objects)


def reseal(value, key="candidate_id"):
    value[key] = digest_bytes(canonical_bytes({k: v for k, v in value.items() if k != key}))
    return value


def find(result, station, variable, depth, day):
    [record] = [r for r in result["observations"]
                if (r["station_id"], r["variable"], r["depth_cm"], r["observation_date"]) == (station, variable, depth, day)]
    return record


def test_capture_fetches_the_headers_and_each_station_year_within_limits():
    fetch = fetcher()
    source = capture(END, fetcher=fetch, clock=lambda: CAPTURED_AT)
    assert [key for key, _ in fetch.calls] == capture_keys(END) == [
        "headers.txt", MANHATTAN, "2026/CRND0103-2026-KS_Oakley_19_SSW.txt"]
    assert all(limit == uscrn_daily.object_limit(key) for key, limit in fetch.calls)
    manifest = source.manifest
    assert (manifest["start"], manifest["end"], manifest["complete"]) == ("2026-09-11", END, True)
    assert manifest["capture_id"] == digest_bytes(canonical_bytes({k: v for k, v in manifest.items() if k != "capture_id"}))
    # A window that crosses New Year needs both years' files for each station.
    assert capture_keys("2027-01-10") == ["headers.txt",
                                          "2026/CRND0103-2026-KS_Manhattan_6_SSW.txt", "2027/CRND0103-2027-KS_Manhattan_6_SSW.txt",
                                          "2026/CRND0103-2026-KS_Oakley_19_SSW.txt", "2027/CRND0103-2027-KS_Oakley_19_SSW.txt"]


def test_urls_are_an_allowlist():
    assert uscrn_daily.object_url(MANHATTAN) == uscrn_daily.BASE + MANHATTAN
    for bad in ("2026/CRND0103-2025-KS_Manhattan_6_SSW.txt", "2026/CRND0103-2026-KS_Elsewhere.txt",
                "../hourly02/x.txt", "2026/CRNH0203-2026-KS_Manhattan_6_SSW.txt"):
        with pytest.raises(ValueError, match="SOURCE_KEY_NOT_ALLOWED"):
            uscrn_daily.object_url(bad)


def test_a_changed_upstream_layout_fails_closed():
    # NOAA reorders two columns: the capture is refused instead of mislabeling values.
    swapped = lambda key, text: text.replace("SOIL_TEMP_5_DAILY SOIL_TEMP_10_DAILY", "SOIL_TEMP_10_DAILY SOIL_TEMP_5_DAILY") if key == "headers.txt" else text
    with pytest.raises(ValueError, match="HEADER_PROFILE_MISMATCH"):
        acquired(swapped)
    with pytest.raises(ValueError, match="HEADER_PROFILE_MISMATCH"):
        acquired(lambda key, text: text.replace("SOIL_TEMP_100_DAILY", "SOIL_TEMP_100_DAILY WIND_DAILY") if key == "headers.txt" else text)


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
    assert [s["name"] for s in first["stations"]] == ["Manhattan 6 SSW", "Oakley 19 SSW"]
    assert first["stations"][0]["geometry"] == {"type": "Point", "coordinates": [-96.61, 39.1]}
    # 2 stations x 30 days x 2 variables x 5 depths, from 40-day year files.
    assert len(first["observations"]) == 600
    assert min(r["observation_date"] for r in first["observations"]) == "2026-09-11"
    schema = Draft202012Validator(json.loads(SCHEMA.read_text()), format_checker=FormatChecker())
    for record in first["observations"]:
        schema.validate(record)
    report = validate_candidate(first)
    assert (report["outcome"], report["release_authorized"], report["withheld"]) == ("PASS", False, 28)


def test_missing_and_impossible_values_are_withheld_never_zero():
    result = candidate()
    missing = find(result, "53974", "SOIL_MOISTURE", 5, "2026-10-03")
    assert (missing["source_token"], missing["value"], missing["withheld"]) == ("-99.000", None, "MISSING")
    cold = find(result, "53974", "SOIL_TEMP", 100, "2026-10-07")
    assert (cold["source_token"], cold["value"], cold["withheld"]) == ("-9999.0", None, "MISSING")
    impossible = find(result, "53974", "SOIL_MOISTURE", 20, "2026-09-20")
    assert (impossible["source_token"], impossible["value"], impossible["withheld"]) == ("1.234", None, "OUT_OF_RANGE")
    reading = find(result, "53974", "SOIL_MOISTURE", 10, "2026-09-11")
    assert (reading["source_token"], reading["value"], reading["unit"], reading["withheld"]) == ("0.280", 0.28, "m3/m3", None)
    assert find(result, "53974", "SOIL_TEMP", 5, "2026-09-11")["unit"] == "degC"
    assert result["withheld_counts"] == {"53974": {"MISSING": 2, "OUT_OF_RANGE": 1}, "03067": {"MISSING": 25, "OUT_OF_RANGE": 0}}


def test_freshness_marks_a_station_whose_soil_sensors_stopped_reporting():
    assert candidate()["freshness_at_capture"] == {"53974": "RECENT", "03067": "STALE"}


def test_a_station_with_no_rows_in_the_window_is_empty_not_a_failed_capture():
    oakley = "2026/CRND0103-2026-KS_Oakley_19_SSW.txt"
    outage = lambda key, text: "\n".join(l for l in text.splitlines() if l.split()[1] < "20260911") + "\n" if key == oakley else text
    result = candidate(outage)
    assert (result["freshness_at_capture"], result["coverage"]) == ({"53974": "RECENT", "03067": "EMPTY"}, "PARTIAL")
    assert result["stations"][1]["geometry"] == {"type": "Point", "coordinates": [-100.96, 38.87]}
    assert {r["station_id"] for r in result["observations"]} == {"53974"}
    assert validate_candidate(result)["outcome"] == "PASS"


def test_identity_is_stable_across_value_revisions():
    revise = lambda key, text: text.replace("20260915 2.622", "20260915 2.623") if key == MANHATTAN else text
    before, after = find(candidate(), "53974", "SOIL_MOISTURE", 5, "2026-09-15"), find(candidate(revise), "53974", "SOIL_MOISTURE", 5, "2026-09-15")
    assert before["id"] == after["id"] and before["record_digest"] != after["record_digest"]
    assert after["datalogger_version"] == "2.623"


@pytest.mark.parametrize("mutate, reason", [
    (lambda key, text: text.replace("53974 ", "53975 ", 1) if key == MANHATTAN else text, "STATION_ROW_ID_OR_SHAPE"),
    (lambda key, text: text + text.splitlines()[15] + "\n" if key == MANHATTAN else text, "DUPLICATE_STATION_DAY"),
    (lambda key, text: text.replace(" 0.280 ", " 0.28x ", 1) if key == MANHATTAN else text, "STATION_ROW_FORMAT"),
    # The station moves within the window.
    (lambda key, text: text.replace("20260920 2.622 -96.61", "20260920 2.622 -96.70") if key == MANHATTAN else text, "STATION_LOCATION_INVALID"),
    (lambda key, text: text.replace(" -96.61 39.10 ", " -96.61 41.50 ") if key == MANHATTAN else text, "STATION_LOCATION_INVALID"),
    (lambda key, text: "" if key == MANHATTAN else text, "SOURCE_SIZE_LIMIT"),
])
def test_invalid_source_rows_are_refused(mutate, reason):
    with pytest.raises(ValueError, match=reason):
        candidate(mutate)


def test_capture_closure_is_checked():
    source = acquired()
    manifest, objects = deepcopy(source.manifest), dict(source.objects)
    with pytest.raises(ValueError, match="CAPTURE_DIGEST_MISMATCH"):
        normalize_capture({**manifest, "end": "2026-10-09"}, objects)
    dropped = {k: v for k, v in objects.items() if k != manifest["pages"][1]["sha256"]}
    with pytest.raises(ValueError, match="PAGE_DIGEST_MISMATCH"):
        normalize_capture(manifest, dropped)
    reordered = deepcopy(manifest)
    reordered["pages"] = reordered["pages"][::-1]
    with pytest.raises(ValueError, match="CAPTURE_PAGE_CHAIN_MISMATCH"):
        normalize_capture(reseal(reordered, "capture_id"), objects)
    widened = reseal({**deepcopy(manifest), "depths_cm": [5, 10, 20, 50, 100, 150]}, "capture_id")
    with pytest.raises(ValueError, match="CAPTURE_SCOPE_MISMATCH"):
        normalize_capture(widened, objects)


@pytest.mark.parametrize("tamper, reason", [
    (lambda c: c["observations"][0].update(value=0.5), "OBSERVATION_DIGEST_MISMATCH"),
    (lambda c: c.update(review_state="APPROVED"), "CANDIDATE_AUTHORITY_OR_PROFILE_INVALID"),
    (lambda c: c.update(coverage="PARTIAL"), "COVERAGE_OR_FRESHNESS_MISMATCH"),
    (lambda c: c["stations"].pop(), "STATION_SCOPE_INVALID"),
    (lambda c: c["stations"][0].update(name="Manhattan"), "STATION_SHAPE_INVALID"),
    (lambda c: c["observations"].reverse(), "OBSERVATION_ORDER_INVALID"),
])
def test_tampered_candidates_are_refused(tamper, reason):
    value = candidate()
    tamper(value)
    with pytest.raises(ValueError, match=reason):
        validate_candidate(reseal(value))


def reseal_record(record):
    record["record_digest"] = digest_bytes(canonical_bytes({k: v for k, v in record.items() if k != "record_digest"}))
    return record


@pytest.mark.parametrize("variable, token, reason", [
    ("SOIL_MOISTURE", "0.28", "OBSERVATION_TOKEN_INVALID"),
    ("SOIL_TEMP", "21.50", "OBSERVATION_TOKEN_INVALID"),
])
def test_tokens_keep_the_daily01_form_for_their_variable(variable, token, reason):
    value = candidate()
    record = next(r for r in value["observations"] if r["variable"] == variable and r["withheld"] is None)
    record["source_token"], record["value"] = token, float(token)
    reseal_record(record)
    with pytest.raises(ValueError, match=reason):
        validate_candidate(reseal(value))


def test_a_partial_station_day_is_refused():
    # Dropping one of a day's ten values, even with counts and digests recomputed, is refused.
    value = candidate()
    dropped = next(i for i, r in enumerate(value["observations"]) if r["station_id"] == "53974" and r["withheld"] is None)
    del value["observations"][dropped]
    with pytest.raises(ValueError, match="STATION_DAY_INCOMPLETE"):
        validate_candidate(reseal(value))


def test_a_reported_value_that_disagrees_with_its_token_is_refused():
    value = candidate()
    record = next(r for r in value["observations"] if r["withheld"] == "OUT_OF_RANGE")
    record["value"], record["withheld"] = 0.234, None
    record["record_digest"] = digest_bytes(canonical_bytes({k: v for k, v in record.items() if k != "record_digest"}))
    with pytest.raises(ValueError, match="OBSERVATION_VALUE_MISMATCH"):
        validate_candidate(reseal(value))


def test_descriptor_is_schema_valid_and_not_admitted_until_the_owner_approves(tmp_path):
    with pytest.raises(ValueError, match="SOURCE_NOT_ADMITTED"):
        uscrn_daily_admission.load_admission()
    descriptor = json.loads(uscrn_daily_admission.DESCRIPTOR.read_text())
    assert descriptor["review_state"] == "needs_review" and descriptor["public_release"]["allowed"] is False
    approved = deepcopy(descriptor)
    approved["review_state"], approved["public_release"]["allowed"] = "approved", True
    approved["lifecycle"]["registry_state"] = "active"
    path = tmp_path / "noaa-uscrn.yaml"
    path.write_text(json.dumps(approved))
    admission = uscrn_daily_admission.load_admission(path)
    assert admission["source_ref"] == "kfm://source/noaa-uscrn"
    assert admission["license"].startswith("U.S. Public Domain")


def test_two_captures_of_the_same_bytes_have_the_same_identity():
    assert acquired().manifest == acquired().manifest
