"""Synthetic-only land capture, privacy, financial-role and replay regression tests."""
from pathlib import Path
import csv
import importlib.util
import io
import json
import sys

import pytest

ROOT = Path(__file__).resolve().parents[3]
sys.path[:0] = [str(ROOT / "packages/domains/people-dna-land/src"), str(ROOT / "packages/hashing/src"), str(ROOT)]
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


def raw_request(app, path, *, query="", auth=None, host="127.0.0.1:5271", origin=None, method="GET"):
    env = {"PATH_INFO": path, "QUERY_STRING": query, "REQUEST_METHOD": method, "HTTP_HOST": host}
    if auth: env["HTTP_AUTHORIZATION"] = auth
    if origin: env["HTTP_ORIGIN"] = origin
    result = []
    body = b"".join(app(env, lambda status, headers: result.append((status, dict(headers)))))
    return result[0][0], body, result[0][1]


def request(app, path, **options):
    status_code, body, headers = raw_request(app, path, **options)
    return status_code, json.loads(body), headers


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


@pytest.mark.parametrize("token", ["", "x" * 39, None, b"x" * 43])
def test_runtime_refuses_weak_review_token(tmp_path, token):
    with pytest.raises(ValueError, match="STRONG_REVIEW_TOKEN_REQUIRED"):
        load_runtime().application(tmp_path, token, 5271)


@pytest.mark.parametrize("method", ["POST", "PUT", "PATCH", "DELETE", "HEAD"])
def test_runtime_is_read_only(tmp_path, method):
    import_csv(tmp_path, [ROW]); token = "x" * 43; app = load_runtime().application(tmp_path, token, 5271)
    before = status(tmp_path)
    status_code, data, _ = request(app, "/review/v1/records", auth="Bearer " + token, method=method)
    assert status_code.startswith("405") and data["reason_code"] == "READ_ONLY_RUNTIME"
    assert status(tmp_path) == before


@pytest.mark.parametrize("path,query", [
    # 128 decoded characters pass the per-value cap; 1,159 encoded bytes exceed the query budget.
    ("/review/v1/records", "county=" + "%E2%82%AC" * 128),
    ("/review/v1/records", "source=unknown-source"),
    ("/review/v1/records", "kind=sale"),
    ("/review/v1/status", "verbose=1"),
    ("/review/v1/evidence", ""),
    ("/review/v1/evidence", "digest=a&extra=b"),
    ("/review/v1/unknown", ""),
])
def test_runtime_query_budget_and_routes_fail_closed(tmp_path, path, query):
    import_csv(tmp_path, [ROW]); token = "x" * 43; app = load_runtime().application(tmp_path, token, 5271)
    status_code, data, _ = request(app, path, query=query, auth="Bearer " + token)
    assert status_code.startswith("400") and data == {"outcome": "ABSTAIN", "reason_code": "INVALID_QUERY"}


def test_runtime_public_routes_expose_no_records(tmp_path):
    import_csv(tmp_path, [ROW]); app = load_runtime().application(tmp_path, "x" * 43, 5271)
    status_code, data, _ = request(app, "/healthz")
    assert status_code.startswith("200") and data["public_records"] == 0 and data["scope"] == "OWNER_REVIEW_ONLY"
    status_code, data, _ = request(app, "/v1/land/other")
    assert status_code.startswith("404") and data["reason_code"] == "ROUTE_NOT_FOUND"
    for path, media in (("/review", "text/html"), ("/review.js", "text/javascript"), ("/review.css", "text/css")):
        status_code, body, headers = raw_request(app, path)
        assert status_code.startswith("200") and headers["Content-Type"].startswith(media) and body
        assert "default-src 'none'" in headers["Content-Security-Policy"] and headers["Cache-Control"] == "private, no-store"
        assert b"SYNTHETIC GRANTOR" not in body


def test_runtime_status_and_evidence_require_review_key(tmp_path):
    import_csv(tmp_path, [ROW]); token = "x" * 43; app = load_runtime().application(tmp_path, token, 5271)
    for path in ("/review/v1/status", "/review/v1/evidence"):
        assert request(app, path, auth="Bearer " + "y" * 43)[0].startswith("401")
    status_code, data, _ = request(app, "/review/v1/status", auth="Bearer " + token)
    assert status_code.startswith("200") and data == status(tmp_path)
    record = request(app, "/review/v1/records", auth="Bearer " + token)[1]["records"][0]
    status_code, data, _ = request(app, "/review/v1/evidence", query="digest=" + record["record_digest"], auth="Bearer " + token)
    assert status_code.startswith("200") and data["scope"] == "OWNER_REVIEW_ONLY"
    assert data["bundles"] == evidence_for(tmp_path, record["record_digest"]) and data["bundles"]


def test_runtime_store_failure_is_opaque(tmp_path, monkeypatch, caplog):
    import_csv(tmp_path, [ROW]); token = "x" * 43; runtime = load_runtime(); app = runtime.application(tmp_path, token, 5271)
    secret = f"SYNTHETIC GRANTOR at {tmp_path}/private"
    def failing_store(*args, **kwargs):
        raise RuntimeError(secret)
    monkeypatch.setattr(runtime, "list_records", failing_store)
    with caplog.at_level("ERROR", logger="kfm.land-runtime"):
        status_code, body, _ = raw_request(app, "/review/v1/records", auth="Bearer " + token)
    assert status_code.startswith("503")
    assert json.loads(body) == {"outcome": "ABSTAIN", "reason_code": "STORE_UNAVAILABLE"}
    assert secret.encode() not in body and secret not in caplog.text
    assert "LAND_STORE_UNAVAILABLE RuntimeError" in caplog.text


class FakeServer:
    def __init__(self, calls, host, port, app, handler_class):
        calls.append((host, port, handler_class)); self.app = app
    def __enter__(self): return self
    def __exit__(self, *exc): return False
    def serve_forever(self): pass


def test_runtime_main_binds_loopback_with_private_key(tmp_path, monkeypatch, capsys):
    import_csv(tmp_path, [ROW]); runtime = load_runtime(); calls = []
    monkeypatch.setattr(runtime, "make_server", lambda *a, **k: FakeServer(calls, *a, **k))
    monkeypatch.setattr(sys, "argv", ["server.py", "--root", str(tmp_path), "--port", "5271"])
    runtime.main()
    key = tmp_path / ".review-token"
    assert key.stat().st_mode & 0o777 == 0o600 and len(key.read_text()) >= 40
    assert calls == [("127.0.0.1", 5271, runtime.PrivateLog)]
    assert key.read_text() not in capsys.readouterr().out
    key.chmod(0o644)
    with pytest.raises(ValueError, match="TOKEN_FILE_MUST_BE_PRIVATE"):
        runtime.main()
    assert len(calls) == 1


@pytest.mark.parametrize("port", ["80", "70000"])
def test_runtime_main_refuses_privileged_or_invalid_port(tmp_path, monkeypatch, port):
    runtime = load_runtime()
    monkeypatch.setattr(sys, "argv", ["server.py", "--root", str(tmp_path), "--port", port])
    with pytest.raises(SystemExit):
        runtime.main()
    assert not (tmp_path / ".review-token").exists()


def test_runtime_request_log_is_silent(capsys):
    handler = object.__new__(load_runtime().PrivateLog)
    handler.log_message("%s", "/review/v1/records?county=SYNTHETIC")
    assert capsys.readouterr() == ("", "")


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
    from people_dna_land.land_records import SOURCES
    for source in SOURCES:
        descriptor = json.loads((ROOT / "data/registry/sources/people-dna-land" / (source + ".source.json")).read_text())
        assert not list(validator.iter_errors(descriptor))
        assert descriptor["spec_hash"] == compute_spec_hash({k: v for k, v in descriptor.items() if k != "spec_hash"})
        assert descriptor["lifecycle"]["registry_state"] == "proposed"
        assert descriptor["public_release"]["allowed"] is False


def test_expanded_glo_page_scope_and_survey_exclusion_remain_explicit():
    survey = """View Details
Survey Details:
Name(s):
SYNTHETIC SURVEY
Document Type:
Original Survey
Survey Title:
SYNTHETIC ONLY
Approved/Accepted Date:
01-01-1884
State:
Kansas
Survey Number:
TEST
Field Note:

County:
Reno
Land Description:
Meridian\tTownship\tRange\tBoundary
6th PM\t0220S\t0100W\tNorth
"""
    raw = ("1-2 of 999 results\n" + CARD + survey + "1-2 of 999 results\n").encode()
    m, _ = capture("blm-glo", raw, url="https://glo-entry-prod.blm.gov/ui/search?q=Kansas&page=1&pageSize=100", retrieved_at=NOW, format="glo-text")
    c = normalize(raw, m)
    assert len(c["records"]) == 1
    assert c["coverage"]["excluded"] == [{"locator": "result-card:2", "reason": "SURVEY_NOT_LAND_INSTRUMENT"}]
    assert c["coverage"]["complete"] is False
    with pytest.raises(ValueError, match="GLO_SURVEY_FORMAT_DRIFT"):
        bad = raw.replace(b"Original Survey", b"Unknown instrument")
        m, _ = capture("blm-glo", bad, url=m["source_url"], retrieved_at=NOW, format="glo-text")
        normalize(bad, m)


@pytest.mark.parametrize("kind", ["State Volume", "Serial Patent"])
def test_glo_accession_is_identity_and_patent_remains_index_only(kind):
    raw = GLO.replace(b"Control Document Index (CDI)", b"Patent").replace(b"Document Type:\nPatent\n", ("Document Type:\n" + kind + "\nAccession #:\nSYNTHETIC-ACCESSION-1\nPage Count:\n1\n").encode())
    r = bundle(raw)[2]["records"][0]
    assert r["source_record_id"] == "glo-accession:SYNTHETIC-ACCESSION-1"
    assert r["instrument_type"] == "patent" and r["amount"] is None
    assert "COMPOSITE_IDENTITY" not in r["flags"]
    assert r["sale_completion"] == "NOT_ESTABLISHED"


def test_county_auction_requires_original_and_does_not_establish_title(tmp_path):
    from connectors.kansas_county_deeds.land_records import capture as county_capture
    row = {**ROW, "county": "Shawnee", "instrument_type": "tax_foreclosure_sale", "transaction_status": "AUCTION_REPORTED", "amount_kind": "auction_purchase_price"}
    raw, mapping = csv_input([row])
    url = "https://cdn.snco.gov/counselor/document/SYNTHETIC.pdf"
    with pytest.raises(ValueError, match="AUCTION_ORIGINAL_DOCUMENT_REQUIRED"):
        county_capture("shawnee-tax-sales", raw, url=url, retrieved_at=NOW)
    m, objects = county_capture("shawnee-tax-sales", raw, url=url, retrieved_at=NOW, documents=[(url, b"%PDF-SYNTHETIC")])
    c = normalize(raw, m, mapping=mapping)
    stage(tmp_path, m, objects, c)
    assert c["records"][0]["sale_completion"] == "NOT_ESTABLISHED"
    for change in ({"county": "Sedgwick"}, {"transaction_status": "RECORDED"}, {"amount_kind": "sale_price"}):
        with pytest.raises(ValueError): make_record({**row, **change}, "shawnee-tax-sales", NOW)


def test_transfer_retains_originals_and_excludes_withdrawn_captures(tmp_path):
    import base64
    from people_dna_land.land_transfer import export_review
    from people_dna_land.land_store import withdraw_capture
    root = tmp_path / "store"
    m, objects, c = bundle(); stage(root, m, objects, c)
    destination = tmp_path / "review.json"
    result = export_review(root, destination)
    value = json.loads(destination.read_bytes())
    from tools.validators._common.jsonschema_runner import load_validator
    load_validator(ROOT / "schemas/contracts/v1/domains/people-dna-land/land_review_transfer.schema.json").validate(value)
    assert result["authority"] == "PRIVATE_REVIEW_ONLY" and result["records"] == 1
    assert base64.b64decode(value["objects"][m["payload_sha256"]]) == GLO
    assert value["transfer_digest"] == digest(canonical({k: v for k, v in value.items() if k != "transfer_digest"}))
    assert destination.stat().st_mode & 0o077 == 0
    with pytest.raises(ValueError, match="ACTIVE_CAPTURE_REQUIRED"):
        export_review(root, tmp_path / "bad.json", capture_ids=["sha256:" + "0" * 64])
    withdraw_capture(root, m["capture_id"], "Synthetic intake withdrawn")
    with pytest.raises(ValueError, match="ACTIVE_CAPTURE_REQUIRED"):
        export_review(root, tmp_path / "withdrawn.json")
    assert audit(root)["outcome"] == "PASS"


def test_transfer_cannot_commit_person_bearing_bytes_under_git(tmp_path):
    from people_dna_land.land_transfer import export_review
    root = tmp_path / "store"
    m, objects, c = bundle(); stage(root, m, objects, c)
    target = tmp_path / "checkout"; (target / ".git").mkdir(parents=True); (target / ".git/HEAD").write_text("ref: refs/heads/main")
    with pytest.raises(ValueError, match="TRANSFER_MUST_BE_OUTSIDE_GIT"):
        export_review(root, target / "review.json")


def shawnee_transcript():
    return {"case_number": "SN-2020-CV-000001", "event_date": "2020-01-02", "expected_tracts": 3,
            "totals": {"total_lien": "20.00", "court_costs": "4.00", "taxes": "16.00", "purchase_price": "12.00"},
            "units": [{"unit_id": "GROUP1-2TRACTS", "purchaser": "SYNTHETIC BIDDER", "deed_name": "SYNTHETIC DEED NAME",
                       "purchase_price": "12.00", "result": "PURCHASE_REPORTED", "pages": [1, 2],
                       "parcels": [{"tract": str(i), "parcel_id": [str(i).zfill(16)], "total_lien": "10.00", "court_costs": "2.00", "taxes": "8.00"} for i in (1, 2)]},
                      {"unit_id": "3", "purchaser": "Invalidated Sale", "deed_name": None, "purchase_price": None, "result": "INVALIDATED_SALE", "pages": [2],
                       "parcels": [{"tract": "3", "parcel_id": ["0000000000000003"], "total_lien": None, "court_costs": None, "taxes": None}]}]}


def test_complete_county_transcript_retains_all_columns_without_title_or_release(tmp_path):
    from connectors.kansas_county_deeds.land_records import transcribe_shawnee, capture as county_capture
    raw, mapping, summary = transcribe_shawnee(shawnee_transcript())
    manifest, objects = county_capture("shawnee-tax-sales", raw, url="https://cdn.snco.gov/counselor/synthetic-results.pdf", retrieved_at=NOW,
                                       documents=[("https://cdn.snco.gov/counselor/synthetic-results.pdf", b"SYNTHETIC ORIGINAL PDF")])
    candidate = normalize(raw, manifest, mapping=mapping)
    stage(tmp_path, manifest, objects, candidate)
    assert summary["units"] == 2 and summary["tracts"] == 3
    group, invalid = candidate["records"]
    assert group["amount"]["value"] == "12.00" and len(group["parties"]) == 1
    assert group["parties"][0]["label"] == "SYNTHETIC DEED NAME"
    assert "Printed purchaser(s): SYNTHETIC BIDDER" in group["notes"]
    assert "lien 10.00; costs 2.00; taxes 8.00 USD" in group["notes"]
    assert "Tract 2: 0000000000000002" in group["legal_description"]
    assert "no allocation" in group["notes"] and "source pages 1,2" in group["notes"]
    assert invalid["amount"] is None and "INVALIDATED_SALE" in invalid["notes"]
    assert all(r["title_claim"] == r["sale_completion"] == "NOT_ESTABLISHED" for r in candidate["records"])
    assert public_projection(candidate)["records"] == []
    assert audit(tmp_path)["outcome"] == "PASS"


@pytest.mark.parametrize("mutation", ["total", "lien", "duplicate_tract", "duplicate_unit", "missing_parcel", "unknown_field", "invalidated_price", "boolean_page", "unbounded_notes"])
def test_county_transcript_fails_closed_on_incomplete_or_conflicting_source_values(mutation):
    from connectors.kansas_county_deeds.land_records import transcribe_shawnee
    table = shawnee_transcript()
    if mutation == "total": table["totals"]["purchase_price"] = "13.00"
    elif mutation == "lien": table["units"][0]["parcels"][0]["taxes"] = "9.00"
    elif mutation == "duplicate_tract": table["units"][0]["parcels"][1]["tract"] = "1"
    elif mutation == "duplicate_unit": table["units"][1]["unit_id"] = table["units"][0]["unit_id"]
    elif mutation == "missing_parcel": table["units"][0]["parcels"][0]["parcel_id"] = []
    elif mutation == "unknown_field": table["units"][0]["approved"] = True
    elif mutation == "invalidated_price": table["units"][1]["purchase_price"] = "0.00"
    elif mutation == "boolean_page": table["units"][0]["pages"] = [True]
    else: table["units"][0]["purchaser"] = "X" * 257
    with pytest.raises(ValueError): transcribe_shawnee(table)


def test_transcript_cli_is_immutable_work_before_explicit_ingestion(tmp_path, capsys):
    spec = importlib.util.spec_from_file_location("land_cli", ROOT / "tools/local_data/land_records.py")
    cli = importlib.util.module_from_spec(spec); spec.loader.exec_module(cli)
    input_path = tmp_path / "transcript.json"; input_path.write_bytes(canonical(shawnee_transcript()))
    root = tmp_path / "store"
    argv = ["--root", str(root), "transcribe-shawnee", "--file", str(input_path)]
    assert cli.main(argv) == 0
    first = json.loads(capsys.readouterr().out)
    assert first["outcome"] == "TRANSCRIBED_NOT_IMPORTED" and status(root)["counts"]["versions"] == 0
    assert Path(first["paths"]["transcript"]).read_bytes() == input_path.read_bytes()
    assert cli.main(argv) == 0
    assert json.loads(capsys.readouterr().out) == first
    input_path.write_text('{"case_number":"A","case_number":"B"}')
    assert cli.main(argv) == 1
    assert json.loads(capsys.readouterr().out)["reason_code"] == "SHAWNEE_DUPLICATE_JSON_KEY"
