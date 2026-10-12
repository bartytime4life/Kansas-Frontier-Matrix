"""USGS ComCat earthquake pilot: monthly capture, window ownership, withholding and tamper denial."""
from copy import deepcopy
import json

import pytest
from jsonschema import Draft202012Validator, FormatChecker

from connectors_core.captured_json import canonical_bytes, digest_bytes
from connectors.usgs.src.usgs.earthquake_capture import EMPTY, capture, month_keys, object_url, window
from pipelines.domains.hazards import earthquake_admission
from pipelines.domains.hazards.earthquake_normalize import number, normalize_capture
from pipelines.domains.hazards.earthquake_validate import SCHEMA, validate_candidate
from tests.domains.hazards.earthquake_fixtures import CAPTURED_AT, YEAR, acquired, fetcher


def candidate(mutate=None, **kwargs):
    source = acquired(mutate, **kwargs)
    return normalize_capture(source.manifest, source.objects)


def reseal(value, key="candidate_id"):
    value[key] = digest_bytes(canonical_bytes({k: v for k, v in value.items() if k != key}))
    return value


def event(result, event_id):
    [record] = [r for r in result["observations"] if r["event_id"] == event_id]
    return record


def in_month(month, change):
    """Apply ``change`` to the document of one month only."""
    return lambda key, document: change(document) if key == month else document


def test_capture_queries_every_calendar_month_once_with_a_fixed_plan():
    fetch = fetcher()
    source = capture(YEAR, fetcher=fetch, clock=lambda: CAPTURED_AT)
    assert [key for key, _ in fetch.calls] == month_keys(YEAR)
    manifest = source.manifest
    assert [p["status"] for p in manifest["pages"]] == [200, 200, 204, 204, 200] + [204] * 7
    assert all(p["sha256"] == EMPTY and p["bytes"] == 0 for p in manifest["pages"] if p["status"] == 204)
    assert set(source.objects) == {p["sha256"] for p in manifest["pages"] if p["status"] == 200}
    assert manifest["capture_id"] == digest_bytes(canonical_bytes({k: v for k, v in manifest.items() if k != "capture_id"}))
    may = window("2025-05")
    assert (may.start, may.end_exclusive, may.limit) == ("2025-05-01T00:00:00.000Z", "2025-06-01T00:00:00.000Z", 5000)
    assert window("2025-12").end_exclusive == "2026-01-01T00:00:00.000Z"
    assert "minlongitude=-102.1" in object_url("2025-05") and "eventtype=earthquake" in object_url("2025-05")


def test_keys_are_an_allowlist():
    for bad in ("2025-13", "2025-5", "1972-01", "../2025-01", "https://elsewhere.example/2025-01", None):
        with pytest.raises(ValueError):
            object_url(bad)


def test_capture_refuses_failures_wrong_urls_bodies_and_bad_years():
    def failing(key, limit):
        raise OSError("connection reset")
    with pytest.raises(ValueError, match="SOURCE_FETCH_FAILED"):
        capture(YEAR, fetcher=failing, clock=lambda: CAPTURED_AT)

    def redirected(key, limit):
        return b"{}", {"source_url": "https://elsewhere.example/" + key, "status": 200, "retrieved_at": CAPTURED_AT}
    with pytest.raises(ValueError, match="SOURCE_RESPONSE_INVALID"):
        capture(YEAR, fetcher=redirected, clock=lambda: CAPTURED_AT)

    def oversized(key, limit):
        return b"x" * (limit + 1), {"source_url": object_url(key), "status": 200, "retrieved_at": CAPTURED_AT}
    with pytest.raises(ValueError, match="SOURCE_SIZE_LIMIT"):
        capture(YEAR, fetcher=oversized, clock=lambda: CAPTURED_AT)

    def empty_ok(key, limit):
        return b"", {"source_url": object_url(key), "status": 200, "retrieved_at": CAPTURED_AT}
    with pytest.raises(ValueError, match="SOURCE_SIZE_LIMIT"):
        capture(YEAR, fetcher=empty_ok, clock=lambda: CAPTURED_AT)
    with pytest.raises(ValueError, match="DATA_YEAR_IN_FUTURE"):
        capture(2026, fetcher=fetcher(), clock=lambda: CAPTURED_AT)
    for bad in (1972, "2025", 2025.0, True, None):
        with pytest.raises(ValueError, match="DATA_YEAR_INVALID"):
            capture(bad, fetcher=fetcher(), clock=lambda: CAPTURED_AT)


def test_candidate_owns_boundary_events_once_withholds_deleted_and_validates():
    result = candidate()
    assert [r["event_id"] for r in result["observations"]] == [
        "us7000p001", "ok2025b002", "us7000p004", "ok2025p005", "us7000p006"]
    # ok2025b002 is at 2025-02-01T00:00:00.000Z: both inclusive queries return it, February owns it.
    assert event(result, "ok2025b002")["origin_utc"] == "2025-02-01T00:00:00.000Z"
    assert [(m["month"], m["query_status"], m["events"]) for m in result["months"][:5]] == [
        (1, 200, 1), (2, 200, 1), (3, 204, 0), (4, 204, 0), (5, 200, 3)]
    assert result["withheld_counts"] == {"STATUS_DELETED": 1}
    assert (result["latest_event_date"], result["year_state"], result["coverage"], result["review_state"],
            result["source_admission"], result["release_state"]) == (
        "2025-05-27", "OPEN", "NOT_ESTABLISHED", "PENDING", "PENDING", "UNRELEASED")
    validator = Draft202012Validator(json.loads(SCHEMA.read_text()), format_checker=FormatChecker())
    assert all(validator.is_valid(r) for r in result["observations"])
    receipt = validate_candidate(result)
    assert (receipt["outcome"], receipt["observations"], receipt["withheld"]) == ("PASS", 5, 1)
    assert (receipt["review_required"], receipt["promotion_authorized"], receipt["release_authorized"],
            receipt["publication_authorized"]) == (True, False, False, False)


def test_flags_numbers_and_source_text():
    result = candidate()
    first = event(result, "us7000p001")
    assert (first["aliases"], first["depth_km"], first["magnitude"], first["magnitude_type"], first["flags"]) == (
        ["us7000p001", "ok2025a001"], 5, 2.6, "ml", [])
    assert (first["place"], first["net"], first["updated_utc"]) == (
        "synthetic: 8 km NNW of Caldwell, Kansas", "us", "2025-01-20T16:02:11.000Z")
    assert event(result, "us7000p004")["flags"] == ["DEPTH_ABSENT", "REVIEW_AUTOMATIC"]
    # North of Medford, Oklahoma: inside the context envelope, outside the Kansas rectangle.
    assert event(result, "ok2025p005")["flags"] == ["CONTEXT_MARGIN"]
    sixth = event(result, "us7000p006")
    assert (sixth["flags"], sixth["magnitude_type"], sixth["place"], sixth["longitude"]) == (
        ["MAGNITUDE_ABSENT"], None, None, -100.2568)
    assert (number(5.0), number(-0.00004), number(2.65), number(None)) == (5, 0, 2.65, None)
    assert type(number(-0.00004)) is int
    unknown = candidate(in_month("2025-01", lambda d: (d["features"][0]["properties"].update(status=None), d)[1]))
    assert event(unknown, "us7000p001")["flags"] == ["REVIEW_STATUS_UNKNOWN"]
    assert validate_candidate(unknown)["outcome"] == "PASS"


def test_raw_features_are_not_copied():
    text = canonical_bytes(candidate()).decode()
    for field in ("eventpage", "phase-data", "tsunami", "\"sig\"", "deleted solution"):
        assert field not in text


def test_normalization_is_deterministic_and_identity_follows_the_preferred_id():
    first, second = candidate(), candidate()
    assert canonical_bytes(first) == canonical_bytes(second)
    revised = candidate(in_month("2025-05", lambda d: (d["features"][0]["properties"].update(mag=2.2), d)[1]))
    assert revised["candidate_id"] != first["candidate_id"]
    assert [r["id"] for r in revised["observations"]] == [r["id"] for r in first["observations"]]
    assert event(revised, "us7000p004")["record_digest"] != event(first, "us7000p004")["record_digest"]


def test_a_capture_after_the_year_is_closed():
    later = candidate(clock="2026-01-15T00:00:00Z")
    assert later["year_state"] == "CLOSED"
    assert validate_candidate(later)["outcome"] == "PASS"


def test_upstream_drift_truncation_and_conflicts_fail_closed():
    def full(document):
        document["features"] = [deepcopy(document["features"][0]) for _ in range(5000)]
        for index, feature in enumerate(document["features"]):
            feature["id"] = f"us7000x{index:04d}"
            feature["properties"]["ids"] = f",us7000x{index:04d},"
        document["metadata"]["count"] = 5000
        return document
    with pytest.raises(ValueError, match="WINDOW_LIMIT_REACHED"):
        candidate(in_month("2025-01", full))
    with pytest.raises(ValueError, match="QUERY_PAGE_COUNT_MISMATCH"):
        candidate(in_month("2025-01", lambda d: (d["metadata"].update(count=7), d)[1]))
    # An event outside the month, other than the next month's boundary event, is drift.
    with pytest.raises(ValueError, match="WINDOW_SCOPE_MISMATCH"):
        candidate(in_month("2025-05", lambda d: (d["features"][0]["properties"].update(time=1735689600000), d)[1]))
    with pytest.raises(ValueError, match="WINDOW_SCOPE_MISMATCH"):
        candidate(in_month("2025-05", lambda d: (d["features"][0]["properties"].update(type="quarry blast"), d)[1]))
    with pytest.raises(ValueError, match="WINDOW_SCOPE_MISMATCH"):
        candidate(in_month("2025-05", lambda d: (d["features"][0]["geometry"].update(coordinates=[-93.0, 39.0, 5]), d)[1]))
    # A boundary event is exempt only inside the envelope.
    with pytest.raises(ValueError, match="WINDOW_SCOPE_MISMATCH"):
        candidate(in_month("2025-01", lambda d: (d["features"][1]["geometry"].update(coordinates=[-93.0, 37.05, 6.2]), d)[1]))
    # One alias naming events in two months.
    with pytest.raises(ValueError, match="IDENTITY_CONFLICT"):
        candidate(in_month("2025-05", lambda d: (d["features"][0]["properties"].update(ids=",us7000p004,ok2025a001,"), d)[1]))
    with pytest.raises(ValueError, match="FEATURE_TEXT_INVALID"):
        candidate(in_month("2025-05", lambda d: (d["features"][0]["properties"].update(place="x" * 257), d)[1]))


def test_capture_tampering_is_refused():
    source = acquired()
    with pytest.raises(ValueError, match="CAPTURE_DIGEST_MISMATCH"):
        normalize_capture({**source.manifest, "data_year": 2024}, source.objects)
    with pytest.raises(ValueError, match="CAPTURE_SCOPE_MISMATCH"):
        normalize_capture(reseal({**deepcopy(source.manifest), "bounds": [-103.0, 36.9, -94.5, 40.1]}, "capture_id"), source.objects)
    with pytest.raises(ValueError, match="CAPTURE_SCOPE_MISMATCH"):
        normalize_capture(reseal({**deepcopy(source.manifest), "query_limit": 20000}, "capture_id"), source.objects)
    dropped = deepcopy(source.manifest)
    dropped["pages"].pop()
    with pytest.raises(ValueError, match="CAPTURE_PAGE_CHAIN_MISMATCH"):
        normalize_capture(reseal(dropped, "capture_id"), source.objects)
    may = source.manifest["pages"][4]["sha256"]
    # A 200 page's body must be present, and a 204 page cannot claim one.
    with pytest.raises(ValueError, match="PAGE_DIGEST_MISMATCH"):
        normalize_capture(source.manifest, {k: v for k, v in source.objects.items() if k != may})
    claimed = deepcopy(source.manifest)
    claimed["pages"][2].update(sha256=may, bytes=source.manifest["pages"][4]["bytes"])
    with pytest.raises(ValueError, match="PAGE_DIGEST_MISMATCH"):
        normalize_capture(reseal(claimed, "capture_id"), source.objects)
    objects = dict(source.objects)
    objects[may] = objects[may][:-2] + b"}\n"
    with pytest.raises(ValueError, match="PAGE_DIGEST_MISMATCH"):
        normalize_capture(source.manifest, objects)


def test_validation_refuses_forged_records_and_authority():
    base = candidate()
    for change, reason in [
        (lambda c: c.update(release_state="RELEASED"), "CANDIDATE_AUTHORITY_OR_PROFILE_INVALID"),
        (lambda c: c.update(source_admission="ADMITTED"), "CANDIDATE_AUTHORITY_OR_PROFILE_INVALID"),
        (lambda c: c.update(coverage="COMPLETE"), "CANDIDATE_AUTHORITY_OR_PROFILE_INVALID"),
        (lambda c: c.update(bounds=[-102.0, 37.0, -94.6, 40.0]), "CANDIDATE_AUTHORITY_OR_PROFILE_INVALID"),
        (lambda c: c.update(year_state="CLOSED"), "CANDIDATE_TIME_INVALID"),
        (lambda c: c.update(retrieved_at="2025-12-31"), "CANDIDATE_TIME_INVALID"),
        (lambda c: c.update(retrieved_at="2025-11-01T12:00:00"), "CANDIDATE_TIME_INVALID"),
        (lambda c: c.update(retrieved_at="2025-11-01T06:00:00-06:00"), "CANDIDATE_TIME_INVALID"),
        (lambda c: c.update(withheld_counts={}), "WITHHELD_COUNTS_INVALID"),
        (lambda c: c.update(withheld_counts={"STATUS_DELETED": -1}), "WITHHELD_COUNTS_INVALID"),
        (lambda c: c.update(latest_event_date="2025-12-31"), "LATEST_EVENT_DATE_MISMATCH"),
        (lambda c: c["months"][4].update(events=2), "MONTH_SUMMARY_MISMATCH"),
        (lambda c: c["months"][0].update(query_status=204), "MONTH_SUMMARY_MISMATCH"),
        (lambda c: c["observations"].reverse(), "RECORD_ORDER_OR_DUPLICATE"),
        (lambda c: c["observations"][0].update(raw_feature_json="{}"), "EARTHQUAKE_SCHEMA_INVALID"),
        (lambda c: c["observations"][0].update(longitude=-93.0), "EARTHQUAKE_SCHEMA_INVALID"),
    ]:
        forged = deepcopy(base)
        change(forged)
        with pytest.raises(ValueError, match=reason):
            validate_candidate(reseal(forged))
    for index, field, value, reason in [
        (0, "flags", ["CONTEXT_MARGIN"], "RECORD_FLAGS_MISMATCH"),
        (3, "flags", [], "RECORD_FLAGS_MISMATCH"),
        (0, "event_id", "us7000p999", "RECORD_IDENTITY_MISMATCH"),
        (0, "aliases", ["ok2025a001", "us7000p001"], "RECORD_ORDER_OR_DUPLICATE"),
        (1, "aliases", ["ok2025b002", "ok2025a001"], "RECORD_ORDER_OR_DUPLICATE"),
        (0, "origin_utc", "2024-01-14T08:23:45.120Z", "RECORD_TIME_INVALID"),
        (0, "origin_utc", "2025-02-30T08:23:45.120Z", "RECORD_TIME_INVALID"),
        (0, "depth_km", 5.0, "RECORD_NUMBER_NOT_CANONICAL"),
        (0, "latitude", 37.27412, "RECORD_NUMBER_NOT_CANONICAL"),
        (0, "review_status", "deleted", "RECORD_STATUS_WITHHELD"),
        (0, "retrieved_at", "2025-11-01T06:00:00-06:00", "RECORD_TIME_INVALID"),
    ]:
        forged = deepcopy(base)
        forged["observations"][index][field] = value
        reseal(forged["observations"][index], "record_digest")
        with pytest.raises(ValueError, match=reason):
            validate_candidate(reseal(forged))
    unsealed = deepcopy(base)
    unsealed["observations"][0]["magnitude"] = 4.1
    with pytest.raises(ValueError, match="RECORD_DIGEST_MISMATCH"):
        validate_candidate(reseal(unsealed))
    with pytest.raises(ValueError, match="CANDIDATE_DIGEST_MISMATCH"):
        validate_candidate({**base, "data_year": 2024})


def test_the_admitted_descriptor_supplies_only_rights_and_sensitivity(tmp_path):
    admission = earthquake_admission.load_admission()
    assert admission["source_ref"] == "kfm://source/usgs-earthquakes"
    assert admission["license"].startswith("U.S. Public Domain")
    # A descriptor that is not approved, active and releasable is refused.
    descriptor = json.loads(earthquake_admission.DESCRIPTOR.read_text())
    for change in ({"review_state": "needs_review"}, {"lifecycle": {**descriptor["lifecycle"], "registry_state": "proposed"}},
                   {"public_release": {**descriptor["public_release"], "allowed": False}}):
        path = tmp_path / "descriptor.json"
        path.write_text(json.dumps({**descriptor, **change}))
        with pytest.raises(ValueError, match="SOURCE_NOT_ADMITTED"):
            earthquake_admission.load_admission(path)
