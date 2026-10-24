"""Synthetic FAA failure and replay coverage; no provider calls or release grants."""
import csv
from copy import deepcopy
from datetime import date
import hashlib
import importlib.util
import io
import json
from pathlib import Path
from types import SimpleNamespace
import zipfile

import pytest

ROOT = Path(__file__).resolve().parents[2]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


faa = load("faa_airports", "pipelines/domains/roads-rail-trade/faa_airports.py")
capture = load("faa_capture", "connectors/faa/capture.py")
rehearsal = load("faa_rehearsal", "tools/local_data/faa_airport_rehearsal.py")
HEADERS = json.loads((ROOT / "fixtures/connectors/faa/apt-headers.json").read_text())


def row(**changes):
    value = dict.fromkeys(HEADERS, "")
    value.update(EFF_DATE="2026/10/01", SITE_NO="99999.01", SITE_TYPE_CODE="A", STATE_CODE="KS", ARPT_ID="ZZZZ",
                 ARPT_NAME="SYNTHETIC TEST AIRPORT", CITY="TEST", COUNTY_NAME="ELLSWORTH", COUNTY_ASSOC_STATE="KS",
                 FACILITY_USE_CODE="PU", OWNERSHIP_TYPE_CODE="PU", ARPT_STATUS="O", LAT_DECIMAL="38.7", LONG_DECIMAL="-98.2", ELEV="1500")
    return {**value, **changes}


def payload(rows=None, headers=HEADERS, extra=None):
    text = io.StringIO(newline="")
    writer = csv.DictWriter(text, fieldnames=headers)
    writer.writeheader()
    writer.writerows(rows or [row()])
    output = io.BytesIO()
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("APT_BASE.csv", text.getvalue())
        if extra:
            z.writestr(*extra)
    data = output.getvalue()
    return data, {"edition": "2026-10-01", "source_id": "faa-nasr-apt", "url": capture.PRODUCTS["2026-10-01"],
                  "retrieved_at": "2026-10-21T19:00:00Z", "sha256": hashlib.sha256(data).hexdigest()}


def test_deterministic_identity_altitude_and_no_contacts():
    a = faa.prepare(*payload())
    assert a == faa.prepare(*payload())
    r = a["records"][0]
    assert r["entity_id"] == "faa:site:99999.01:a"
    assert (r["elevation"], r["elevation_unit"], r["vertical_reference"]) == (1500, "ft", "MSL")
    assert r["horizontal_datum"] == "UNVERIFIED_SOURCE_DATUM"
    assert "PHONE_NO" not in r["original"] and r["bundle"]["sensitivity"]["level"] == "quarantine"
    assert r["evidence_ref"] in r["bundle"]["evidence_refs"]
    assert a["release_time"] is None and a["release_state"] == "HELD"


@pytest.mark.parametrize("changes,reason", [({"LAT_DECIMAL": "NaN"}, "COORDINATES_INVALID"), ({"LONG_DECIMAL": "181"}, "COORDINATES_INVALID"),
    ({"ELEV": "inf"}, "ELEVATION_INVALID"), ({"EFF_DATE": "2026/10/29"}, "EDITION_MISMATCH"), ({"SITE_NO": "ZZ"}, "IDENTITY_INVALID")])
def test_bad_records_quarantined(changes, reason):
    c = faa.prepare(*payload([row(**changes)]))
    assert not c["records"] and c["coverage"] == "PARTIAL"
    assert c["rejects"][0]["reason"] == reason and c["rejects"][0]["original"]


def test_duplicate_does_not_hide_incomplete_coverage():
    c = faa.prepare(*payload([row(), row()]))
    assert len(c["records"]) == 1 and c["rejects"][0]["reason"] == "DUPLICATE_ENTITY"


def test_revision_separate_from_entity_and_identifiers():
    first, second = [faa.prepare(*payload([row(ARPT_ID=identifier)]))["records"][0] for identifier in ("AAAA", "BBBB")]
    assert first["entity_id"] == second["entity_id"] and first["revision_id"] != second["revision_id"]


@pytest.mark.parametrize("site", ["99999.", "99999.1", "99999.01", "99999.101"])
def test_source_site_numbers_preserve_variable_fraction(site):
    c = faa.prepare(*payload([row(SITE_NO=site, SITE_TYPE_CODE="C")]))
    assert not c["rejects"] and c["records"][0]["entity_id"] == "faa:site:" + site + ":c"


def test_private_and_military_never_public_candidates():
    for changes in ({"FACILITY_USE_CODE": "PR"}, *({"OWNERSHIP_TYPE_CODE": code} for code in ["MA", "MN", "MR", "CG", "XX"]), {"ARPT_STATUS": "CI"}, {"SITE_TYPE_CODE": "H"}):
        assert not faa.prepare(*payload([row(**changes)]))["records"][0]["public_candidate"]


def test_schema_drift_and_unsafe_archive_and_integrity():
    with pytest.raises(ValueError, match="SCHEMA_DRIFT"):
        faa.prepare(*payload([row()], headers=list(reversed(HEADERS))))
    with pytest.raises(ValueError, match="ARCHIVE_MEMBER_UNSAFE"):
        faa.prepare(*payload(extra=("../contact.csv", "sensitive test")))
    data, receipt = payload()
    with pytest.raises(ValueError, match="CAPTURE_INTEGRITY_FAILED"):
        faa.prepare(data + b"x", receipt)


def test_future_edition_and_observation_rights_holds():
    data, receipt = payload()
    c = faa.prepare(data, {**receipt, "retrieved_at": "2026-09-30T12:00:00Z"})
    assert c["future_at_capture"] and c["release_state"] == "HELD"
    assert capture.surveillance_decision("opensky")["outcome"] == "DENY"
    assert not capture.surveillance_decision("opensky")["public_display_enabled"]
    for provider in ("adsb-lol", "adsb-fi"):
        decision = capture.surveillance_decision(provider)
        assert decision["outcome"] == "ALLOW_DISPLAY_ONLY" and decision["attribution_required"]
        assert decision["public_display_enabled"] and not decision["ingestion_enabled"] and decision["evidence_refs"] == []
    with pytest.raises(ValueError, match="SOURCE_NOT_ALLOWED"):
        capture.surveillance_decision("unknown-feed")


class Response(io.BytesIO):
    status = 200

    def __init__(self, body, length=None):
        super().__init__(body)
        self.headers = {"Content-Length": str(len(body) if length is None else length)}

    def geturl(self):
        return capture.PRODUCTS["2026-10-01"]


def test_atomic_capture_retry_and_incomplete_download(tmp_path):
    data, _ = payload()
    def open_response(request, timeout):
        assert timeout == 20
        return Response(data)
    saved = capture.capture(tmp_path, "2026-10-01", opener=SimpleNamespace(open=open_response))
    assert capture.capture(tmp_path, "2026-10-01") == saved
    (saved / "archive.zip").write_bytes(b"corrupt")
    with pytest.raises(ValueError, match="CAPTURE_INTEGRITY_FAILED"):
        capture.capture(tmp_path, "2026-10-01")
    other = tmp_path / "other"
    other.mkdir()
    with pytest.raises(ValueError, match="INCOMPLETE_CAPTURE"):
        capture.capture(other, "2026-10-01", opener=SimpleNamespace(open=lambda *a, **kw: Response(data, len(data) + 1)))
    assert not list(other.iterdir())


def test_disk_full_and_outage_leave_no_capture(tmp_path, monkeypatch):
    monkeypatch.setattr(capture.shutil, "disk_usage", lambda p: SimpleNamespace(free=0))
    with pytest.raises(OSError, match="DISK_RESERVE_REQUIRED"):
        capture.capture(tmp_path, "2026-10-01")
    assert not list(tmp_path.iterdir())
    with pytest.raises(ValueError, match="EDITION_NOT_ALLOWED"):
        capture.capture(tmp_path, "2026-10-01", today=date(2026, 9, 30))


def test_candidate_reuses_existing_evidence_schemas():
    from tools.validators._common.jsonschema_runner import load_validator
    validator = load_validator(ROOT / "schemas/contracts/v1/domains/roads-rail-trade/faa_airport_candidate.schema.json", check_formats=True)
    candidate = faa.prepare(*payload())
    assert not list(validator.iter_errors(candidate))
    candidate["release_state"] = "RELEASED"
    assert list(validator.iter_errors(candidate))


def test_sql_replay_index_and_transaction_rollback(tmp_path):
    c = faa.prepare(*payload())
    path = tmp_path / "rehearsal.sqlite"
    assert rehearsal.rehearse(c, path)["inserted"] == 1
    result = rehearsal.rehearse(c, path)
    assert result["inserted"] == 0 and result["rows"] == 1 and result["integrity"] == "ok"
    assert "INDEX faa_county" in str(result["query_plan"])
    import sqlite3
    with sqlite3.connect(path) as db:
        db.execute("DELETE FROM faa_candidate")
        db.rollback()
        assert db.execute("SELECT COUNT(*) FROM faa_candidate").fetchone()[0] == 1


def test_selection_evidence_report_and_correction_preserve_prior_revision():
    first = faa.prepare(*payload())
    selected = first["records"][0]
    result = rehearsal.inspect_selection(first, selected["revision_id"])
    assert result["evidence_ref"]["ref"] in result["report"] and "PRIVATE REVIEW DRAFT - HELD" in result["report"]
    corrected = faa.prepare(*payload([row(ARPT_NAME="SYNTHETIC CORRECTED NAME")]))
    assert corrected["records"][0]["entity_id"] == selected["entity_id"]
    assert corrected["records"][0]["revision_id"] != selected["revision_id"]
    assert rehearsal.inspect_selection(first, selected["revision_id"]) == result
    selected["bundle"]["citations"] = ["https://invalid.test/"]
    with pytest.raises(ValueError, match="CANDIDATE_DIGEST_MISMATCH"):
        rehearsal.inspect_selection(first, selected["revision_id"])


# Rehashing the outer container must not let a changed projection reuse a revision.
TAMPERS = [
    (("records", 0, "name"), "SYNTHETIC MODIFIED NAME"),
    (("records", 0, "county_name"), "UNBOUND COUNTY"),
    (("records", 0, "state"), "MO"),
    (("archive_sha256",), "0" * 64),
    (("records", 0, "edition"), "2026-10-29"),
    (("edition",), "2026-10-29"),
    (("records", 0, "entity_id"), "faa:site:88888.01:a"),
    (("records", 0, "revision_id"), "faa:revision:" + "0" * 64),
    (("records", 0, "faa_id"), "FORGED"),
    (("records", 0, "icao_id"), "KZZZ"),
    (("records", 0, "original", "ARPT_NAME"), "SYNTHETIC MODIFIED ORIGINAL"),
    (("records", 0, "original", "SITE_NO"), "88888.01"),
    (("records", 0, "evidence_ref", "ref"), "kfm://aviation/airport/unbound"),
    (("records", 0, "evidence_ref", "bundle_ref"), "faa:bundle:unbound"),
    (("records", 0, "bundle", "citations"), ["https://invalid.test/"]),
    (("records", 0, "bundle", "evidence_refs"), []),
    (("records", 0, "bundle", "source_records"), ["sha256:" + "0" * 64]),
    (("records", 0, "bundle", "checksums", "record"), "sha256:" + "0" * 64),
]


@pytest.mark.parametrize("path,value", TAMPERS)
@pytest.mark.parametrize("reseal", [False, True], ids=["original-seal", "rehashed-container"])
def test_tampered_candidate_rejected_before_report_or_sql(path, value, reseal, tmp_path, monkeypatch):
    candidate = faa.prepare(*payload())
    target = candidate
    for part in path[:-1]:
        target = target[part]
    target[path[-1]] = value
    if reseal:
        bundle = candidate["records"][0]["bundle"]
        bundle["spec_hash"]["value"] = faa.sha(faa.canonical({k: v for k, v in bundle.items() if k != "spec_hash"}))
        candidate["candidate_id"] = faa.sha(faa.canonical({k: v for k, v in candidate.items() if k != "candidate_id"}))
    before = deepcopy(candidate)
    def forbidden_connect(*args, **kwargs):
        pytest.fail("invalid candidate reached SQLite")
    monkeypatch.setattr(rehearsal.sqlite3, "connect", forbidden_connect)
    error = "RECORD_BINDING_MISMATCH" if reseal else "CANDIDATE_DIGEST_MISMATCH"
    with pytest.raises(ValueError, match=error):
        rehearsal.inspect_selection(candidate, candidate["records"][0]["revision_id"])
    database = tmp_path / "rejected.sqlite"
    with pytest.raises(ValueError, match=error):
        rehearsal.rehearse(candidate, database)
    assert not database.exists() and candidate == before


def test_selection_missing_ambiguous_and_unselected_tampering(tmp_path):
    candidate = faa.prepare(*payload([row(), row(SITE_NO="88888.01")]))
    with pytest.raises(ValueError, match="SELECTION_NOT_FOUND"):
        rehearsal.inspect_selection(candidate, "faa:revision:" + "0" * 64)
    selected = candidate["records"][0]["revision_id"]
    candidate["records"][1]["name"] = "SYNTHETIC MODIFIED UNSELECTED"
    with pytest.raises(ValueError, match="CANDIDATE_DIGEST_MISMATCH"):
        rehearsal.inspect_selection(candidate, selected)
    candidate = faa.prepare(*payload())
    candidate["records"].append(deepcopy(candidate["records"][0]))
    candidate["candidate_id"] = faa.sha(faa.canonical({k: v for k, v in candidate.items() if k != "candidate_id"}))
    with pytest.raises(ValueError, match="RECORD_BINDING_MISMATCH"):
        rehearsal.inspect_selection(candidate, candidate["records"][0]["revision_id"])
    with pytest.raises(ValueError, match="RECORD_BINDING_MISMATCH"):
        rehearsal.rehearse(candidate, tmp_path / "duplicate.sqlite")


def test_verified_selection_does_not_alias_candidate():
    candidate = faa.prepare(*payload())
    before = deepcopy(candidate)
    result = rehearsal.inspect_selection(candidate, candidate["records"][0]["revision_id"])
    result["bundle"]["citations"].append("https://invalid.test/")
    result["evidence_ref"]["ref"] = "kfm://aviation/airport/unbound"
    assert candidate == before


@pytest.mark.parametrize("changes", [
    {}, {"ELEV": "", "ICAO_ID": ""}, {"SITE_TYPE_CODE": "H", "FACILITY_USE_CODE": "PR"},
    {"OWNERSHIP_TYPE_CODE": "MA"}, {"SITE_NO": "99999."}, {"LAT_DECIMAL": "NaN"},
])
def test_verified_candidates_preserve_schema_json_replay_and_holds(changes, tmp_path):
    candidate = faa.prepare(*payload([row(**changes)]))
    candidate = json.loads(faa.canonical(candidate))
    before = deepcopy(candidate)
    assert faa.verify_candidate(candidate) == candidate
    assert rehearsal.rehearse(candidate, tmp_path / "valid.sqlite")["rows"] == len(candidate["records"])
    if candidate["records"]:
        result = rehearsal.inspect_selection(candidate, candidate["records"][0]["revision_id"])
        assert result["release_state"] == "HELD" and candidate["records"][0]["name"] in result["report"]
    assert candidate == before and candidate["release_state"] == "HELD" and candidate["release_time"] is None


@pytest.mark.parametrize("field,value", [
    ("profile", "unsupported"), ("parser_version", "unsupported"),
    ("release_state", "RELEASED"), ("rights_state", "APPROVED"), ("release_time", "2026-10-21T19:00:00Z"),
])
def test_resealed_authority_changes_rejected(field, value, tmp_path):
    candidate = faa.prepare(*payload())
    candidate[field] = value
    candidate["candidate_id"] = faa.sha(faa.canonical({k: v for k, v in candidate.items() if k != "candidate_id"}))
    with pytest.raises(ValueError, match="CANDIDATE_STATE_INVALID"):
        rehearsal.inspect_selection(candidate, candidate["records"][0]["revision_id"])
    path = tmp_path / "held.sqlite"
    with pytest.raises(ValueError, match="CANDIDATE_STATE_INVALID"):
        rehearsal.rehearse(candidate, path)
    assert not path.exists()


def test_invalid_candidate_leaves_existing_database_unchanged(tmp_path):
    candidate = faa.prepare(*payload())
    path = tmp_path / "existing.sqlite"
    rehearsal.rehearse(candidate, path)
    before = path.read_bytes()
    candidate["records"][0]["name"] = "SYNTHETIC MODIFIED NAME"
    with pytest.raises(ValueError, match="CANDIDATE_DIGEST_MISMATCH"):
        rehearsal.rehearse(candidate, path)
    assert path.read_bytes() == before
