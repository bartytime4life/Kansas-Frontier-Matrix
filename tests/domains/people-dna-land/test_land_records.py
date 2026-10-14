"""Synthetic-only land capture, privacy, financial-role and replay regression tests."""
from pathlib import Path
import csv
import importlib.util
import io
import json
import sys

import pytest

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / "packages/domains/people-dna-land/src"), str(ROOT)]
from connectors.blm.src.blm.land_records import capture
from people_dna_land.land_records import canonical, digest, make_record, normalize, public_projection
from people_dna_land.land_store import audit, connection, evidence_for, initialize, list_records, stage, status

NOW = "2026-10-13T20:00:00Z"
URL = "https://glorecords.blm.gov/s/advanced-search?searchTerm=%2Fsearch%3Fq%3DKansas%26page%3D1%26pageSize%3D25"
CARD = """View Details
Control Document Index (CDI) Details:
Name(s):
SYNTHETIC REVIEW PERSON (Patentee)
Date:
04-17-1884
State:
Kansas
County:
Reno
Document#:
TEST-ONLY-001
Document Type:
Patent
Land Descriptions (3):
Meridian\tTownship\tRange\tSection(s)\tSubdivision
6th PM\t0220S\t0100W\t001\tNE
6th PM\t0220S\t0100W\t001\tNW

Show More
"""
GLO = ("General Land Office > Search Results\n1-1 of 999 results\n" + CARD + "1-1 of 999 results\n").encode()
ROW = {"source_record_id": "SYNTHETIC-TEST-DEED-01", "instrument_type": "warranty_deed", "event_date": "2001-05-20", "state": "KS", "transaction_status": "RECORDED", "county": "Sedgwick", "grantor": "SYNTHETIC GRANTOR", "grantee": "SYNTHETIC GRANTEE", "legal_description": "SYNTHETIC LEGAL DESCRIPTION", "amount": "1.00", "amount_kind": "nominal_consideration", "currency": "USD"}


def bundle(raw=GLO):
    m, objects = capture("blm-glo", raw, url=URL, retrieved_at=NOW, format="glo-text")
    return m, objects, normalize(raw, m)


def csv_input(rows):
    handle = io.StringIO(newline="")
    writer = csv.DictWriter(handle, fieldnames=sorted(rows[0]))
    writer.writeheader(); writer.writerows(rows)
    return handle.getvalue().encode(), {k: k for k in rows[0]}


def import_csv(tmp_path, rows, source="sedgwick-deeds", documents=()):
    raw, mapping = csv_input(rows)
    from people_dna_land.land_capture import capture_export
    url = {"sedgwick-deeds": "https://www.sedgwickcounty.org/register-of-deeds/online-land-record-search/", "blm-mlrs": "https://reports.blm.gov/reports/MLRS", "kshs-land-sales": "https://www.kansashistory.gov/p/land-records-at-the-state-archives/11083"}[source]
    m, objects = capture_export(source, raw, url=url, retrieved_at=NOW, format="mapped-csv", documents=documents)
    c = normalize(raw, m, mapping=mapping, max_records=1000)
    return stage(tmp_path, m, objects, c)


def load_runtime():
    spec = importlib.util.spec_from_file_location("land_review_runtime", ROOT / "apps/land-records/server.py")
    module = importlib.util.module_from_spec(spec); spec.loader.exec_module(module)
    return module


def test_glo_index_does_not_claim_sale_title_or_geometry():
    _, _, c = bundle()
    r = c["records"][0]
    assert r["amount"] is None and r["geometry"] is None
    assert r["title_claim"] == r["sale_completion"] == "NOT_ESTABLISHED"
    assert r["parties"][0]["living_status"] == "UNKNOWN"
    assert "LEGAL_DESCRIPTION_PARTIAL" in r["flags"]
    assert "COMPOSITE_IDENTITY" in r["flags"]
    assert c["coverage"]["complete"] is False


@pytest.mark.parametrize("old,new", [(b"Patent", b"Unknown financial instrument"), (b"1884", b"188x"), (b"Kansas", b"Nebraska"), (b"1-1 of 999", b"1-2 of 999"), (b"Meridian\tTownship", b"Latitude\tTownship")])
def test_source_schema_drift_refuses_whole_capture(old, new):
    with pytest.raises(ValueError): bundle(GLO.replace(old, new))


def test_record_ids_survive_retrieval_and_page_change():
    m, objects, c = bundle()
    m2, _ = capture("blm-glo", GLO, url=URL, retrieved_at="2026-10-14T20:00:00Z", format="glo-text")
    assert normalize(GLO, m2)["records"] == c["records"]
    changed = GLO.replace(b"1-1 of 999", b"26-26 of 999")
    m3, _ = capture("blm-glo", changed, url=URL.replace("page%3D1", "page%3D2"), retrieved_at=NOW, format="glo-text")
    assert normalize(changed, m3)["records"] == c["records"]


def test_raw_byte_tampering_is_rejected():
    m, _, _ = bundle()
    with pytest.raises(ValueError, match="CAPTURE_INTEGRITY_FAILED"):
        normalize(GLO + b"injected", m)


@pytest.mark.parametrize("url", ["http://glorecords.blm.gov/", "https://glorecords.blm.gov.evil.test/", "https://secret@glorecords.blm.gov/", "https://glorecords.blm.gov/?access_token=secret", "https://127.0.0.1/"])
def test_source_identity_and_credential_url_guards(url):
    with pytest.raises(ValueError): capture("blm-glo", GLO, url=url, retrieved_at=NOW, format="glo-text")


def test_explicit_csv_mapping_nominal_value_is_not_sale_price(tmp_path):
    import_csv(tmp_path, [ROW])
    r = list_records(tmp_path)["records"][0]
    assert r["amount"] == {"value": "1.00", "kind": "nominal_consideration", "currency": "USD"}
    assert r["sale_completion"] == "NOT_ESTABLISHED"


@pytest.mark.parametrize("field,value", [("amount", "1e99"), ("amount", "$100"), ("amount", "NaN"), ("currency", ""), ("amount_kind", "tax_value"), ("state", "MO"), ("county", "Johnson"), ("instrument_type", "patent"), ("event_date", "2001-02-31")])
def test_mapped_csv_roles_and_types_fail_closed(tmp_path, field, value):
    row = {**ROW, field: value}
    with pytest.raises(ValueError): import_csv(tmp_path, [row])
    assert not (tmp_path / ".kfm-land-store.json").exists()


def test_mlrs_case_is_not_a_completed_sale(tmp_path):
    row = {**ROW, "instrument_type": "land_tenure_case", "transaction_status": "RECORDED"}
    with pytest.raises(ValueError, match="CASE_OR_NOTICE_NOT_COMPLETED_SALE"): import_csv(tmp_path, [row], source="blm-mlrs")
    row = {k: v for k, v in row.items() if k not in {"amount", "amount_kind", "currency"}}
    row["transaction_status"] = "CASE_ACTION"
    import_csv(tmp_path, [row], source="blm-mlrs")
    assert list_records(tmp_path)["records"][0]["instrument_type"] == "land_tenure_case"


def test_replay_no_duplicates_and_correction_retains_versions(tmp_path):
    a = import_csv(tmp_path, [ROW]); b = import_csv(tmp_path, [ROW]); assert a == b
    import_csv(tmp_path, [{**ROW, "amount": "2.00"}])
    assert status(tmp_path)["counts"] == {"captures": 2, "versions": 2, "runs": 2, "withdrawn_captures": 0}
    rows = list_records(tmp_path)["records"]
    assert rows[0]["id"] == rows[1]["id"] and rows[0]["record_digest"] != rows[1]["record_digest"]
    assert audit(tmp_path)["record_versions"] == 2


def test_same_identity_conflict_within_batch_refuses_import(tmp_path):
    with pytest.raises(ValueError, match="DUPLICATE_IDENTITY_CONFLICT"):
        import_csv(tmp_path, [ROW, {**ROW, "amount": "2.00"}])


def test_pagination_filters_and_evidence(tmp_path):
    rows = [{**ROW, "source_record_id": str(i), "event_date": "2001-05-" + str(i + 1).zfill(2)} for i in range(8)]
    import_csv(tmp_path, rows)
    first = list_records(tmp_path, limit=3); second = list_records(tmp_path, limit=3, after=first["next_cursor"])
    assert len(first["records"]) == len(second["records"]) == 3
    assert not {r["id"] for r in first["records"]} & {r["id"] for r in second["records"]}
    assert len(list_records(tmp_path, start="2001-05-07")["records"]) == 2
    assert list_records(tmp_path, county="nonexistent")["records"] == []
    bundles = evidence_for(tmp_path, first["records"][0]["record_digest"])
    assert bundles[0]["locators"][0].startswith("csv-row:")
    assert bundles[0]["release_state"] == "UNRELEASED"


def test_budget_never_silently_truncates():
    raw, mapping = csv_input([ROW, {**ROW, "source_record_id": "2"}])
    m, _ = capture("blm-glo", raw, url="https://glorecords.blm.gov/s/", retrieved_at=NOW, format="mapped-csv")
    with pytest.raises(ValueError, match="RECORD_LIMIT"): normalize(raw, m, mapping=mapping, max_records=1)


def test_self_hashed_approval_cannot_bypass_replay(tmp_path):
    m, objects, c = bundle(); c["records"][0]["release_state"] = "RELEASED"
    c["candidate_id"] = digest(canonical({k: v for k, v in c.items() if k != "candidate_id"}))
    with pytest.raises(ValueError, match="NORMALIZATION_REPLAY_MISMATCH"): stage(tmp_path, m, objects, c)


def test_audit_detects_raw_corruption_and_unattested_index(tmp_path):
    m, objects, c = bundle(); stage(tmp_path, m, objects, c)
    assert audit(tmp_path)["outcome"] == "PASS"
    path = tmp_path / "data/quarantine/land-records/objects" / m["payload_sha256"][7:]
    path.write_bytes(b"tampered")
    with pytest.raises(ValueError): audit(tmp_path)


def test_store_and_input_symlinks_refused(tmp_path):
    from people_dna_land.land_store import read_file
    target = tmp_path / "regular"; target.write_bytes(b"record")
    link = tmp_path / "link"; link.symlink_to(target)
    with pytest.raises(OSError): read_file(link)
    store = tmp_path / "store"; store.symlink_to(tmp_path, target_is_directory=True)
    with pytest.raises(ValueError): initialize(store)


def request(app, path, *, query="", auth=None, host="127.0.0.1:5271", origin=None, method="GET"):
    env = {"PATH_INFO": path, "QUERY_STRING": query, "REQUEST_METHOD": method, "HTTP_HOST": host}
    if auth: env["HTTP_AUTHORIZATION"] = auth
    if origin: env["HTTP_ORIGIN"] = origin
    result = []
    body = b"".join(app(env, lambda status, headers: result.append((status, dict(headers)))))
    return result[0][0], json.loads(body), result[0][1]


def test_runtime_auth_public_denial_and_dns_rebinding(tmp_path):
    import_csv(tmp_path, [ROW]); token = "x" * 43; app = load_runtime().application(tmp_path, token, 5271)
    status_code, data, headers = request(app, "/review/v1/records")
    assert status_code.startswith("401") and "records" not in data
    status_code, data, _ = request(app, "/review/v1/records", auth="Bearer " + token)
    assert status_code.startswith("200") and len(data["records"]) == 1
    assert "no-store" in headers["Cache-Control"]
    for options in ({"host": "evil.test:5271"}, {"origin": "https://evil.test"}):
        assert request(app, "/review/v1/records", auth="Bearer " + token, **options)[0].startswith("403")
    status_code, data, _ = request(app, "/v1/land/records", auth="Bearer " + token)
    assert status_code.startswith("403") and data["records"] == []
    assert public_projection(ROW)["records"] == []


@pytest.mark.parametrize("query", ["source=blm-glo&source=sedgwick-deeds", "unknown=x", "limit=101", "limit=01", "after=../../secret", "start=2000-02-31", "start=2002-01-01&end=2001-01-01"])
def test_runtime_queries_fail_closed(tmp_path, query):
    import_csv(tmp_path, [ROW]); app = load_runtime().application(tmp_path, "x" * 43, 5271)
    assert request(app, "/review/v1/records", query=query, auth="Bearer " + "x" * 43)[0].startswith("400")


def test_changed_mapped_csv_header_is_not_guessed():
    raw, mapping = csv_input([ROW]); raw = raw.replace(b"source_record_id", b"new_id")
    m, _ = capture("blm-glo", raw, url="https://glorecords.blm.gov/s/", retrieved_at=NOW, format="mapped-csv")
    with pytest.raises(ValueError, match="CSV_HEADER_DRIFT"): normalize(raw, m, mapping=mapping)


def test_withdrawal_keeps_audit_bytes_and_is_not_undone_by_replay(tmp_path):
    from people_dna_land.land_store import withdraw_capture
    m, objects, c = bundle(); stage(tmp_path, m, objects, c)
    withdrawal = withdraw_capture(tmp_path, m["capture_id"], "Synthetic correction test")
    assert withdrawal["state"] == "WITHDRAWN"
    assert list_records(tmp_path)["records"] == []
    assert evidence_for(tmp_path, c["records"][0]["record_digest"]) == []
    stage(tmp_path, m, objects, c)
    assert list_records(tmp_path)["records"] == []
    assert audit(tmp_path)["outcome"] == "PASS"
    assert status(tmp_path)["counts"]["versions"] == 1


def test_self_hashed_capture_cannot_admit_source(tmp_path):
    m, objects, c = bundle(); m["source_admission"] = "APPROVED"
    m["capture_id"] = digest(canonical({k: v for k, v in m.items() if k != "capture_id"}))
    with pytest.raises(ValueError, match="CAPTURE_AUTHORITY_OR_SHAPE_INVALID"): stage(tmp_path, m, objects, c)


def test_encoded_credentials_are_not_preserved():
    with pytest.raises(ValueError, match="SOURCE_URL_CREDENTIAL_QUERY"):
        capture("blm-glo", GLO, url="https://glorecords.blm.gov/?%74oken=secret", retrieved_at=NOW, format="glo-text")


def test_index_tampering_is_detected(tmp_path):
    import_csv(tmp_path, [ROW])
    with connection(tmp_path) as db:
        db.execute("UPDATE versions SET record='{}'")
    with pytest.raises(ValueError, match="RECORD_INDEX_MISMATCH"): audit(tmp_path)
    with pytest.raises(ValueError, match="RECORD_INDEX_MISMATCH"): import_csv(tmp_path, [ROW])


def test_archival_connector_requires_original_document():
    from connectors.kshs.land_records import capture as archive_capture
    with pytest.raises(ValueError, match="ARCHIVAL_ORIGINAL_REQUIRED"):
        archive_capture(b"csv", url="https://www.kansashistory.gov/p/land-records-at-the-state-archives/11083", retrieved_at=NOW, documents=[])


def test_real_git_root_is_rejected(tmp_path):
    (tmp_path / ".git").mkdir(); (tmp_path / ".git/HEAD").write_text("ref: refs/heads/main")
    with pytest.raises(ValueError, match="STORE_MUST_BE_OUTSIDE_GIT"): initialize(tmp_path / "records")


def test_closed_instrument_schema_and_no_ownership_projection():
    from jsonschema import Draft202012Validator, FormatChecker
    schema = json.loads((ROOT / "schemas/contracts/v1/domains/people-dna-land/land_instrument_candidate.schema.json").read_text())
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    record = bundle()[2]["records"][0]
    validator.validate(record)
    for field, value in [("release_state", "RELEASED"), ("geometry", {"type": "Point", "coordinates": [0, 0]}), ("sale_completion", "CONFIRMED")]:
        assert list(validator.iter_errors({**record, field: value}))


def test_source_descriptors_are_inactive_and_validate():
    from tools.validators._common.jsonschema_runner import load_validator
    from hashing import compute_spec_hash
    validator = load_validator(ROOT / "schemas/contracts/v1/source/source_descriptor.schema.json")
    for source in ("blm-glo", "blm-mlrs", "kshs-land-sales", "sedgwick-deeds", "johnson-deeds"):
        descriptor = json.loads((ROOT / "data/registry/sources/people-dna-land" / (source + ".source.json")).read_text())
        assert not list(validator.iter_errors(descriptor))
        assert descriptor["spec_hash"] == compute_spec_hash({k: v for k, v in descriptor.items() if k != "spec_hash"})
        assert descriptor["lifecycle"]["registry_state"] == "proposed"
        assert descriptor["public_release"]["allowed"] is False
