"""Synthetic pilot captures exercise transformation and private-store replay."""
from copy import deepcopy
from datetime import datetime, timezone
import json
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import pytest
from jsonschema import Draft202012Validator, FormatChecker

from connectors_core.captured_json import canonical_bytes, digest_bytes
from connectors_core.transport import TransportResponse
from connectors.usgs.water_data.pilot_capture import Capture, MAX_PAGE_BYTES, STATIONS, capture
from pipelines.domains.hydrology.normalize import normalize_capture
from pipelines.domains.hydrology.validate import validate_candidate
from tools.local_data.manage import init_store
from tools.local_data.water_pilot import replay, stage
from tools.validators.source.validate_source_health_assessment import validate_payload

START, END = "2026-09-29T18:00:00Z", "2026-09-30T18:00:00Z"
ROOT = Path(__file__).resolve().parents[3]


class Clock:
    def now(self):
        return datetime(2026, 9, 30, 18, 1, tzinfo=timezone.utc)

    def monotonic(self):
        return 0

    def sleep(self, _seconds):
        pass


def observation(station, *, value="12.5", revised="2026-09-30T18:00:01.123456Z"):
    return {"type": "Feature", "id": "synthetic-" + station, "geometry": None,
            "properties": {"monitoring_location_id": station, "time_series_id": "synthetic-series-" + station,
                           "parameter_code": "00060", "statistic_id": "00011", "method_category": None,
                           "time": END, "last_modified": revised, "value": value, "unit_of_measure": "ft^3/s",
                           "approval_status": "Provisional", "qualifier": None}}


class FixtureTransport:
    def __init__(self, mutate=lambda value: value):
        self.mutate = mutate

    def send(self, request, **_options):
        query = parse_qs(urlsplit(request.url).query)
        if "/monitoring-locations/" in request.url:
            station = "USGS-" + query["monitoring_location_number"][0]
            features = [{"type": "Feature", "id": station,
                         "geometry": {"type": "Point", "coordinates": [-98, 38]},
                         "properties": {"agency_code": "USGS", "monitoring_location_number": station[5:],
                                        "monitoring_location_name": "SYNTHETIC TEST STATION", "state_code": "20"}}]
        else:
            station = query["monitoring_location_id"][0]
            features = self.mutate([observation(station)])
        return TransportResponse(200, {"content-type": "application/geo+json"},
                                 (canonical_bytes({"type": "FeatureCollection", "features": features, "links": []}),))


def acquired(mutate=lambda value: value):
    return capture(START, END, transport=FixtureTransport(mutate), clock=Clock())


def reseal(manifest):
    manifest["capture_id"] = digest_bytes(canonical_bytes({k: v for k, v in manifest.items() if k != "capture_id"}))


def test_candidate_replay_preserves_times_identity_and_no_authority():
    source = acquired()
    first = normalize_capture(source.manifest, source.objects)
    assert first == normalize_capture(deepcopy(source.manifest), dict(source.objects))
    assert first["coverage"] == "COMPLETE"
    assert first["source_admission"] == first["review_state"] == "PENDING"
    assert first["release_state"] == "UNRELEASED"
    assert first["observations"][0]["provider_revision_at"].endswith(".123456Z")
    assert first["observations"][0]["provisional"] is True
    schema = json.loads((ROOT / "schemas/contracts/v1/domains/hydrology/flow_observation.schema.json").read_text())
    for record in first["observations"]:
        Draft202012Validator(schema, format_checker=FormatChecker()).validate(record)


def _with_station_revision(source: Capture, revision: str) -> Capture:
    page = next(item for item in source.manifest["pages"]
                if item["collection"] == "monitoring-locations")
    old_digest = page["sha256"]
    payload = json.loads(source.objects[old_digest])
    payload["features"][0]["properties"]["revision_modified"] = revision
    raw = canonical_bytes(payload)
    page["sha256"] = digest_bytes(raw)
    page["bytes"] = len(raw)
    source.objects.pop(old_digest)
    source.objects[page["sha256"]] = raw
    reseal(source.manifest)
    return source


@pytest.mark.parametrize("revision", ["2099-01-01T00:00:00Z", "not-a-time"])
def test_station_revision_must_be_valid_and_no_later_than_retrieval(revision, tmp_path):
    source = _with_station_revision(acquired(), revision)
    with pytest.raises(ValueError, match="STATION_PROVENANCE_INVALID"):
        normalize_capture(source.manifest, source.objects)
    root = tmp_path / "private-store"
    init_store(root)
    assert stage(root, source)["outcome"] == "QUARANTINED"
    assert not list(root.glob("data/work/hydrology/usgs-nwis/*/candidate.json"))

    source = acquired()
    candidate = normalize_capture(source.manifest, source.objects)
    candidate["stations"][0]["provider_revision_at"] = revision
    candidate["candidate_id"] = digest_bytes(canonical_bytes({
        key: value for key, value in candidate.items() if key != "candidate_id"
    }))
    with pytest.raises(ValueError, match="STATION_PROVENANCE_INVALID"):
        validate_candidate(candidate)


def test_station_revision_before_retrieval_is_normalized_to_utc():
    source = _with_station_revision(acquired(), "2026-09-30T13:00:30-05:00")
    candidate = normalize_capture(source.manifest, source.objects)
    assert candidate["stations"][0]["provider_revision_at"] == "2026-09-30T18:00:30Z"
    assert validate_candidate(candidate)["outcome"] == "PASS"


def test_duplicates_and_new_revisions():
    def mutate(records):
        revised = deepcopy(records[0])
        revised["properties"]["value"] = "13.5"
        revised["properties"]["last_modified"] = "2026-09-30T18:00:01.234567Z"
        return [revised, records[0], deepcopy(records[0])]
    result = acquired(mutate)
    candidate = normalize_capture(result.manifest, result.objects)
    assert len(candidate["observations"]) == 2
    assert len(candidate["revision_history"]) == 4
    assert all(record["value"] == 13.5 for record in candidate["observations"])
    assert candidate["observations"][0]["id"] == normalize_capture(acquired().manifest, acquired().objects)["observations"][0]["id"]


def test_same_revision_with_conflicting_value_quarantines():
    def mutate(records):
        other = deepcopy(records[0])
        other["properties"]["value"] = "99"
        return [*records, other]
    result = acquired(mutate)
    with pytest.raises(ValueError, match="CONFLICTING_OBSERVATION_REVISION"):
        normalize_capture(result.manifest, result.objects)


@pytest.mark.parametrize("property,value", [
    ("time", "2004-10-01T00:00:00Z"), ("value", "NaN"), ("value", True),
    ("unit_of_measure", "unknown"), ("parameter_code", "00065"),
    ("approval_status", "unknown"), ("time_series_id", ""),
])
def test_invalid_observation_rejected(property, value):
    def mutate(records):
        records[0]["properties"][property] = value
        return records
    result = acquired(mutate)
    with pytest.raises(ValueError):
        normalize_capture(result.manifest, result.objects)


def test_empty_and_null_are_not_no_flow():
    empty = acquired(lambda _: [])
    result = normalize_capture(empty.manifest, empty.objects)
    assert result["coverage"] == "EMPTY" and set(result["freshness_at_capture"].values()) == {"EMPTY"}
    def missing(records):
        records[0]["properties"]["value"] = None
        return records
    source = acquired(missing)
    candidate = normalize_capture(source.manifest, source.objects)
    assert candidate["observations"][0]["value"] is None
    assert candidate["coverage"] == "EMPTY"
    assert set(candidate["freshness_at_capture"].values()) == {"EMPTY"}


def test_null_value_does_not_make_station_recent():
    def one_missing(records):
        if records[0]["properties"]["monitoring_location_id"] == STATIONS[0]:
            records[0]["properties"]["value"] = None
        return records

    source = acquired(one_missing)
    candidate = normalize_capture(source.manifest, source.objects)
    assert candidate["coverage"] == "PARTIAL"
    assert candidate["freshness_at_capture"] == {STATIONS[0]: "EMPTY", STATIONS[1]: "RECENT"}
    assert validate_candidate(candidate)["outcome"] == "PASS"

    misleading = deepcopy(candidate)
    misleading["freshness_at_capture"][STATIONS[0]] = "RECENT"
    misleading["coverage"] = "COMPLETE"
    misleading["candidate_id"] = digest_bytes(canonical_bytes({k: v for k, v in misleading.items() if k != "candidate_id"}))
    with pytest.raises(ValueError, match="COVERAGE_OR_FRESHNESS_MISMATCH"):
        validate_candidate(misleading)


def test_old_observations_are_explicitly_stale():
    source = acquired()
    source.manifest["captured_at"] = "2026-10-01T12:00:00Z"
    reseal(source.manifest)
    candidate = normalize_capture(source.manifest, source.objects)
    assert set(candidate["freshness_at_capture"].values()) == {"STALE"}


def test_manifest_and_raw_tampering_rejected():
    source = acquired()
    source.manifest["complete"] = False
    with pytest.raises(ValueError, match="DIGEST"):
        normalize_capture(source.manifest, source.objects)
    source = acquired()
    source.objects[source.manifest["pages"][0]["sha256"]] = b"{}"
    with pytest.raises(ValueError, match="PAGE_DIGEST"):
        normalize_capture(source.manifest, source.objects)


@pytest.mark.parametrize("tamper", ["missing", "wrong_station", "future", "bad_status", "duplicate"])
def test_rehashed_complete_capture_requires_page_success_attempts(tamper, tmp_path):
    source = acquired()
    attempts = source.manifest["attempts"]
    if tamper == "missing":
        attempts.clear()
    elif tamper == "wrong_station":
        attempts[0]["station_id"] = "USGS-07156900"
    elif tamper == "future":
        attempts[0]["observed_at"] = "2026-09-30T18:02:00Z"
    elif tamper == "bad_status":
        attempts[0]["status"] = 503
        attempts[1]["observed_at"] = "2026-09-30T18:00:59Z"
    else:
        attempts.append(deepcopy(attempts[0]))
    reseal(source.manifest)

    with pytest.raises(ValueError, match="CAPTURE_ATTEMPT_CHAIN_MISMATCH"):
        normalize_capture(source.manifest, source.objects)

    root = tmp_path / "store"
    init_store(root)
    assert stage(root, source)["outcome"] == "QUARANTINED"
    assert not list((root / "data/work").rglob("candidate.json"))
    health = [json.loads(path.read_text()) for path in root.glob(
        "data/receipts/ingest/usgs-nwis/*/health/*.json")]
    assert len(health) == 2
    assert all(validate_payload(item).ok for item in health)
    assert all(item["health_outcome"] == "UNAVAILABLE" for item in health)
    if tamper in {"future", "bad_status"}:
        first = next(item for item in health if item["source_id"] == "usgs-nwis:USGS-06892518")
        assert first["last_success_at"] == source.manifest["attempts"][1]["observed_at"]


def test_retry_before_success_does_not_break_page_binding():
    source = acquired()
    prior = deepcopy(source.manifest["attempts"][0])
    prior.update(number=1, outcome="TIMEOUT", code="RETRY_TIMEOUT", status=None)
    source.manifest["attempts"][0]["number"] = 2
    source.manifest["attempts"].insert(0, prior)
    reseal(source.manifest)

    assert normalize_capture(source.manifest, source.objects)["coverage"] == "COMPLETE"


def test_private_store_replay_and_failed_capture_preserves_candidate(tmp_path):
    root = tmp_path / "store"
    init_store(root)
    source = acquired()
    first = stage(root, source)
    assert replay(root, source.manifest["capture_id"]) == first
    before = {p.relative_to(root): p.read_bytes() for p in (root / "data/work").rglob("*.json")}
    bad = acquired()
    bad.manifest["complete"] = False
    reseal(bad.manifest)
    assert stage(root, bad)["outcome"] == "QUARANTINED"
    assert before == {p.relative_to(root): p.read_bytes() for p in (root / "data/work").rglob("*.json")}
    assert not list((root / "data/published").rglob("*"))
    assert not list((root / "data/processed").rglob("*"))


def test_replay_binds_requested_capture_to_stored_manifest(tmp_path):
    root = tmp_path / "store"
    init_store(root)
    source = acquired()
    actual_id = source.manifest["capture_id"]
    first = stage(root, source)
    wrong_id = "sha256:" + "0" * 64
    original = root / "data/quarantine/usgs-nwis/runs" / actual_id.split(":")[1] / "manifest.json"
    misplaced = root / "data/quarantine/usgs-nwis/runs" / wrong_id.split(":")[1] / "manifest.json"
    misplaced.parent.mkdir(parents=True)
    misplaced.write_bytes(original.read_bytes())

    with pytest.raises(ValueError, match="CAPTURE_PATH_ID_MISMATCH"):
        replay(root, wrong_id)

    assert not (root / "data/receipts/ingest/usgs-nwis" / wrong_id.split(":")[1]).exists()
    assert replay(root, actual_id) == first


def test_stage_rejects_excess_objects_before_writing(tmp_path):
    root = tmp_path / "store"
    init_store(root)
    source = acquired()
    source.manifest["complete"] = False
    reseal(source.manifest)
    for number in range(9):
        raw = f"extra page {number}".encode()
        source.objects[digest_bytes(raw)] = raw

    with pytest.raises(ValueError, match="CAPTURE_OBJECT_BUDGET_EXCEEDED"):
        stage(root, source)

    assert not list((root / "data/quarantine/usgs-nwis").rglob("payload"))
    assert not list((root / "data/quarantine/usgs-nwis").rglob("manifest.json"))
    assert not list((root / "data/receipts/ingest/usgs-nwis").rglob("*.json"))


def test_stage_rejects_excess_bytes_before_writing(tmp_path):
    root = tmp_path / "store"
    init_store(root)
    source = acquired()
    source.manifest["complete"] = False
    reseal(source.manifest)
    source.objects = {}
    for number in range(6):
        raw = bytes([number]) * MAX_PAGE_BYTES
        source.objects[digest_bytes(raw)] = raw

    with pytest.raises(ValueError, match="CAPTURE_OBJECT_BUDGET_EXCEEDED"):
        stage(root, source)

    assert not list((root / "data/quarantine/usgs-nwis").rglob("payload"))


def test_stage_rejects_bad_later_digest_before_writing(tmp_path):
    root = tmp_path / "store"
    init_store(root)
    source = acquired()
    source.objects["sha256:" + "0" * 64] = b"wrong digest"

    with pytest.raises(ValueError, match="PAGE_DIGEST_MISMATCH"):
        stage(root, source)

    assert not list((root / "data/quarantine/usgs-nwis").rglob("payload"))


def test_replay_rejects_excess_page_refs_before_loading_objects(tmp_path):
    root = tmp_path / "store"
    init_store(root)
    source = acquired()
    source.manifest["pages"] *= 4
    reseal(source.manifest)
    capture_id = source.manifest["capture_id"]
    path = root / "data/quarantine/usgs-nwis/runs" / capture_id.split(":")[1] / "manifest.json"
    path.parent.mkdir(parents=True)
    path.write_bytes(canonical_bytes(source.manifest))

    with pytest.raises(ValueError, match="CAPTURE_PAGE_LIMIT"):
        replay(root, capture_id)


def test_stage_rejects_excess_page_refs_before_writing(tmp_path):
    root = tmp_path / "store"
    init_store(root)
    source = acquired()
    source.manifest["pages"] *= 4
    reseal(source.manifest)

    with pytest.raises(ValueError, match="CAPTURE_PAGE_LIMIT"):
        stage(root, source)

    assert not list((root / "data/quarantine/usgs-nwis").rglob("payload"))


def test_candidate_storage_conflict_is_not_reported_as_invalid_source(tmp_path):
    root = tmp_path / "store"
    init_store(root)
    source = acquired()
    candidate = normalize_capture(source.manifest, source.objects)
    path = root / "data/work/hydrology/usgs-nwis" / candidate["candidate_id"].split(":")[1] / "candidate.json"
    path.parent.mkdir(parents=True)
    path.write_bytes(b"conflicting local bytes")

    with pytest.raises(ValueError, match="IMMUTABLE_OBJECT_CONFLICT"):
        stage(root, source)

    assert path.read_bytes() == b"conflicting local bytes"
    assert not list((root / "data/receipts/ingest/usgs-nwis").rglob("quarantined.json"))


def test_symlink_object_rejected(tmp_path):
    root = tmp_path / "store"
    init_store(root)
    (root / "data/quarantine/usgs-nwis").symlink_to(tmp_path, target_is_directory=True)
    with pytest.raises(ValueError, match="SYMLINK"):
        stage(root, acquired())


@pytest.mark.parametrize("amount", ["1e1000000", "-1e1000000"])
def test_decimal_overflow_is_quarantined_with_receipt(tmp_path, amount):
    result = acquired(lambda records: [observation(records[0]["properties"]["monitoring_location_id"], value=amount)])
    with pytest.raises(ValueError, match="INVALID_DISCHARGE"):
        normalize_capture(result.manifest, result.objects)
    root = tmp_path / "private-store"
    init_store(root)
    receipt = stage(root, result)
    assert receipt["outcome"] == "QUARANTINED"
    assert list(root.glob("data/receipts/ingest/usgs-nwis/*/quarantined.json"))
    assert len(list(root.glob("data/quarantine/usgs-nwis/objects/sha256/*/payload"))) == 4


@pytest.mark.parametrize("mutate", [
    lambda value: value["features"][0]["properties"].update(time="0001-01-01T00:00:00+23:59") if "time" in value["features"][0]["properties"] else None,
    lambda value: value["features"][0]["geometry"].update(coordinates=[10**400, 38]) if value["features"][0]["geometry"] else None,
])
def test_scalar_conversion_overflow_has_quarantine_receipt(tmp_path, mutate):
    result = acquired()
    for page in result.manifest["pages"]:
        body = json.loads(result.objects[page["sha256"]])
        mutate(body)
        raw = canonical_bytes(body)
        digest = digest_bytes(raw)
        result.objects[digest] = raw
        page.update(sha256=digest, bytes=len(raw))
    reseal(result.manifest)
    root = tmp_path / "private-store"
    init_store(root)
    assert stage(root, result)["outcome"] == "QUARANTINED"
    assert list(root.glob("data/receipts/ingest/usgs-nwis/*/quarantined.json"))
