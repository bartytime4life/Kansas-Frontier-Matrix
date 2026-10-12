"""NOAA Storm Events pilot: listing-chosen capture, deterministic Kansas candidate, withholding and tamper denial."""
from copy import deepcopy
import json

import pytest
from jsonschema import Draft202012Validator, FormatChecker

from connectors_core.captured_json import canonical_bytes, digest_bytes
from connectors.noaa.src.noaa import storm_events_capture
from connectors.noaa.src.noaa.storm_events_capture import LISTING_KEY, LISTING_URL, capture, latest_details, object_url
from pipelines.domains.hazards import storm_events_admission
from pipelines.domains.hazards.storm_events_normalize import normalize_capture
from pipelines.domains.hazards.storm_events_validate import SCHEMA, validate_candidate
from tests.domains.hazards.storm_events_fixtures import CAPTURED_AT, DETAILS, YEAR, acquired, fetcher, fixture_bytes

LISTING = fixture_bytes(LISTING_KEY)


def candidate(mutate=None):
    source = acquired(mutate)
    return normalize_capture(source.manifest, source.objects)


def reseal(value, key="candidate_id"):
    value[key] = digest_bytes(canonical_bytes({k: v for k, v in value.items() if k != key}))
    return value


def event(result, event_id):
    [record] = [r for r in result["observations"] if r["event_id"] == event_id]
    return record


def details_only(transform):
    return lambda key, text: text if key == LISTING_KEY else transform(text)


def test_capture_reads_the_listing_then_only_the_newest_details_file_for_the_year():
    fetch = fetcher()
    source = capture(YEAR, fetcher=fetch, clock=lambda: CAPTURED_AT)
    assert [key for key, _ in fetch.calls] == [LISTING_KEY, DETAILS]
    assert all(limit == storm_events_capture.object_limit(key) for key, limit in fetch.calls)
    manifest = source.manifest
    assert [p["url"] for p in manifest["pages"]] == [LISTING_URL, LISTING_URL + DETAILS]
    assert (manifest["data_year"], manifest["state_fips"], manifest["complete"]) == (YEAR, 20, True)
    assert manifest["capture_id"] == digest_bytes(canonical_bytes({k: v for k, v in manifest.items() if k != "capture_id"}))
    assert set(source.objects) == {p["sha256"] for p in manifest["pages"]}


def test_the_listing_names_the_file_and_the_fatalities_and_locations_files_are_never_chosen():
    assert latest_details(LISTING, 2025) == DETAILS
    assert latest_details(LISTING, 2024) == "StormEvents_details-ftp_v1.0_d2024_c20250401.csv.gz"
    with pytest.raises(ValueError, match="DATA_YEAR_NOT_LISTED"):
        latest_details(LISTING, 2023)
    # Only the fatalities file names a 2026 vintage: it is not a details file, so the year is unlisted.
    with pytest.raises(ValueError, match="DATA_YEAR_NOT_LISTED"):
        latest_details(LISTING.replace(b"fatalities-ftp_v1.0_d2025", b"fatalities-ftp_v1.0_d2026"), 2026)
    with pytest.raises(ValueError, match="LISTING_CREATION_DATE_INVALID"):
        latest_details(LISTING.replace(b"d2025_c20251020", b"d2025_c20251399"), 2025)
    with pytest.raises(ValueError, match="LISTING_CREATION_DATE_INVALID"):
        latest_details(LISTING.replace(b"d2025_c20250916", b"d2025_c20240916"), 2025)
    with pytest.raises(ValueError, match="LISTING_ENCODING"):
        latest_details(b"\xff\xfe", 2025)


def test_urls_are_an_allowlist():
    assert object_url(LISTING_KEY) == LISTING_URL
    for bad in ("StormEvents_fatalities-ftp_v1.0_d2025_c20251020.csv.gz", "../../x.csv.gz",
                "StormEvents_details-ftp_v1.0_d2025_c20251020.csv", "https://elsewhere.example/" + DETAILS, None):
        with pytest.raises(ValueError, match="SOURCE_KEY_NOT_ALLOWED"):
            object_url(bad)


def test_capture_refuses_failures_wrong_urls_and_bad_years():
    def failing(key, limit):
        raise OSError("connection reset")
    with pytest.raises(ValueError, match="SOURCE_FETCH_FAILED"):
        capture(YEAR, fetcher=failing, clock=lambda: CAPTURED_AT)

    def redirected(key, limit):
        return b"x", {"source_url": "https://elsewhere.example/" + key, "retrieved_at": CAPTURED_AT}
    with pytest.raises(ValueError, match="SOURCE_RESPONSE_INVALID"):
        capture(YEAR, fetcher=redirected, clock=lambda: CAPTURED_AT)

    def oversized(key, limit):
        return b"x" * (limit + 1), {"source_url": object_url(key), "retrieved_at": CAPTURED_AT}
    with pytest.raises(ValueError, match="SOURCE_SIZE_LIMIT"):
        capture(YEAR, fetcher=oversized, clock=lambda: CAPTURED_AT)
    with pytest.raises(ValueError, match="DATA_YEAR_IN_FUTURE"):
        capture(2026, fetcher=fetcher(), clock=lambda: CAPTURED_AT)
    for bad in (1995, "2025", 2025.0, True, None):
        with pytest.raises(ValueError, match="DATA_YEAR_INVALID"):
            capture(bad, fetcher=fetcher(), clock=lambda: CAPTURED_AT)


def test_candidate_selects_kansas_withholds_quarantined_events_and_validates():
    result = candidate()
    assert [r["event_id"] for r in result["observations"]] == [9000101, 9000102, 9000103, 9000104, 9000105, 9000106]
    assert result["withheld_counts"] == {"CASUALTY_UNPARSEABLE": 0, "DAMAGE_UNPARSEABLE": 1, "END_BEFORE_BEGIN": 1}
    assert (result["source_file"], result["vintage_created"], result["latest_event_date"]) == (DETAILS, "2025-10-20", "2025-08-03")
    assert (result["freshness_at_capture"], result["coverage"], result["review_state"],
            result["source_admission"], result["release_state"]) == ("CURRENT", "NOT_ESTABLISHED", "PENDING", "PENDING", "UNRELEASED")
    validator = Draft202012Validator(json.loads(SCHEMA.read_text()), format_checker=FormatChecker())
    assert all(validator.is_valid(r) for r in result["observations"])
    receipt = validate_candidate(result)
    assert (receipt["outcome"], receipt["observations"], receipt["withheld"]) == ("PASS", 6, 2)
    assert (receipt["review_required"], receipt["promotion_authorized"], receipt["release_authorized"],
            receipt["publication_authorized"]) == (True, False, False, False)


def test_source_strings_parsed_values_and_flags_stay_side_by_side():
    result = candidate()
    tornado = event(result, 9000101)
    assert (tornado["damage_property_source"], tornado["damage_property_usd"], tornado["damage_crops_usd"]) == ("250.00K", 250000, 0)
    assert (tornado["begin_utc"], tornado["tor_f_scale"], tornado["injuries_direct"], tornado["flags"]) == (
        "2025-04-28T23:12Z", "EF1", 1, [])
    hail = event(result, 9000102)
    # Blank damage is unreported, never zero.
    assert (hail["damage_property_source"], hail["damage_property_usd"], hail["magnitude_source"]) == ("", None, "1.75")
    winter = event(result, 9000103)
    assert (winter["cz_type"], winter["begin_utc"], winter["flags"]) == ("Z", "2025-01-05T13:00Z", ["ZONE_OR_COUNTY_SUPPORT_ONLY"])
    assert event(result, 9000104)["flags"] == ["EPISODE_ID_ABSENT"]
    flood = event(result, 9000105)
    assert (flood["damage_property_usd"], flood["damage_crops_usd"], flood["begin_utc"], flood["flags"]) == (
        2000000, 10000, None, ["UTC_OFFSET_UNKNOWN"])
    assert event(result, 9000106)["flags"] == ["EVENT_TYPE_OUTSIDE_DIRECTIVE"]


def test_no_narrative_text_reaches_the_candidate():
    result = candidate()
    text = canonical_bytes(result).decode()
    assert "narrative" not in text.lower().replace("has_narrative", "")
    assert "Synthetic episode" not in text
    assert [r["has_narrative"] for r in result["observations"]][:2] == [True, False]


def test_normalization_is_deterministic_and_identity_is_vintage_independent():
    first, second = candidate(), candidate()
    assert canonical_bytes(first) == canonical_bytes(second)
    reissued = acquired(lambda key, text: text.replace("d2025_c20251020", "d2025_c20251030") if key == LISTING_KEY else text)
    later = normalize_capture(reissued.manifest, reissued.objects)
    assert later["source_file"] == "StormEvents_details-ftp_v1.0_d2025_c20251030.csv.gz"
    assert later["candidate_id"] != first["candidate_id"]
    assert [r["id"] for r in later["observations"]] == [r["id"] for r in first["observations"]]


def test_a_stale_vintage_is_marked_stale():
    old = acquired(lambda key, text: text.replace("d2025_c20251020", "d2025_c20250901") if key == LISTING_KEY else text)
    result = normalize_capture(old.manifest, old.objects)
    assert result["freshness_at_capture"] == "STALE"
    assert validate_candidate(result)["outcome"] == "PASS"


def test_upstream_drift_and_bad_rows_fail_closed():
    with pytest.raises(ValueError, match="DETAILS_FILE_"):
        candidate(details_only(lambda text: text.replace("DAMAGE_PROPERTY,", "DAMAGE_PROP,", 1)))
    with pytest.raises(ValueError, match="DETAILS_FILE_"):
        candidate(details_only(lambda text: text.replace(",9000102,", ",9000101,", 1)))
    # A row outside the file's data year rejects the whole file.
    with pytest.raises(ValueError, match="DETAILS_FILE_"):
        candidate(details_only(lambda text: text.replace("202505,19,1840,202505,19,1840", "202405,19,1840,202405,19,1840", 1)))


def test_capture_tampering_is_refused():
    source = acquired()
    manifest = deepcopy(source.manifest)
    manifest["data_year"] = 2024
    with pytest.raises(ValueError, match="CAPTURE_DIGEST_MISMATCH"):
        normalize_capture(manifest, source.objects)
    with pytest.raises(ValueError, match="CAPTURE_SCOPE_MISMATCH"):
        normalize_capture(reseal(deepcopy({**source.manifest, "state_fips": 31}), "capture_id"), source.objects)
    # An older vintage the listing does not name as newest is not accepted.
    older = deepcopy(source.manifest)
    older["pages"][1]["key"] = "StormEvents_details-ftp_v1.0_d2025_c20250916.csv.gz"
    older["pages"][1]["url"] = object_url(older["pages"][1]["key"])
    with pytest.raises(ValueError, match="CAPTURE_PAGE_CHAIN_MISMATCH"):
        normalize_capture(reseal(older, "capture_id"), source.objects)
    swapped = deepcopy(source.manifest)
    swapped["pages"].reverse()
    with pytest.raises(ValueError, match="CAPTURE_PAGE_CHAIN_MISMATCH"):
        normalize_capture(reseal(swapped, "capture_id"), source.objects)
    objects = dict(source.objects)
    details = source.manifest["pages"][1]["sha256"]
    objects[details] = objects[details][:-1] + bytes([objects[details][-1] ^ 1])
    with pytest.raises(ValueError, match="PAGE_DIGEST_MISMATCH"):
        normalize_capture(source.manifest, objects)


def test_validation_refuses_forged_records_and_authority():
    base = candidate()
    for change, reason in [
        (lambda c: c.update(release_state="RELEASED"), "CANDIDATE_AUTHORITY_OR_PROFILE_INVALID"),
        (lambda c: c.update(source_admission="ADMITTED"), "CANDIDATE_AUTHORITY_OR_PROFILE_INVALID"),
        (lambda c: c.update(coverage="COMPLETE"), "CANDIDATE_AUTHORITY_OR_PROFILE_INVALID"),
        (lambda c: c.update(source_file="StormEvents_details-ftp_v1.0_d2024_c20251020.csv.gz"), "CANDIDATE_SOURCE_FILE_INVALID"),
        (lambda c: c.update(vintage_created="2025-10-21"), "CANDIDATE_SOURCE_FILE_INVALID"),
        (lambda c: c.update(withheld_counts={"DAMAGE_UNPARSEABLE": 0}), "WITHHELD_COUNTS_INVALID"),
        (lambda c: c.update(latest_event_date="2025-12-31"), "LATEST_EVENT_DATE_MISMATCH"),
        (lambda c: c.update(freshness_at_capture="STALE"), "FRESHNESS_MISMATCH"),
        (lambda c: c["observations"].reverse(), "RECORD_ORDER_OR_DUPLICATE"),
        (lambda c: c["observations"][0].update(narrative="x"), "STORM_EVENT_SCHEMA_INVALID"),
    ]:
        forged = deepcopy(base)
        change(forged)
        with pytest.raises(ValueError, match=reason):
            validate_candidate(reseal(forged))
    for field, value, reason in [
        ("damage_property_usd", 2500000, "RECORD_DAMAGE_MISMATCH"),
        ("begin_utc", "2025-04-28T22:12Z", "RECORD_UTC_MISMATCH"),
        ("flags", [], "RECORD_FLAGS_MISMATCH"),
        ("event_id", 9000201, "RECORD_IDENTITY_MISMATCH"),
        ("begin_local", "2024-04-28T17:12", "RECORD_TIME_INVALID"),
        ("end_lat", None, "RECORD_COORDINATE_INVALID"),
    ]:
        forged = deepcopy(base)
        index = 4 if field == "flags" else 0
        forged["observations"][index][field] = value
        reseal(forged["observations"][index], "record_digest")
        with pytest.raises(ValueError, match=reason):
            validate_candidate(reseal(forged))
    unsealed = deepcopy(base)
    unsealed["observations"][0]["deaths_direct"] = 3
    with pytest.raises(ValueError, match="RECORD_DIGEST_MISMATCH"):
        validate_candidate(reseal(unsealed))
    with pytest.raises(ValueError, match="CANDIDATE_DIGEST_MISMATCH"):
        validate_candidate({**base, "data_year": 2024})


def test_the_proposed_descriptor_is_not_admitted():
    with pytest.raises(ValueError, match="SOURCE_NOT_ADMITTED"):
        storm_events_admission.load_admission()
