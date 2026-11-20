"""Supplied plant-query capture integrity, minimization, drift and denied authority."""
import copy
import json
import os
import socket
import subprocess
import sys

import pytest
from pipelines.domains.flora import inaturalist_ingest as m


def packet(case="complete"):
    return json.loads((m.FIXTURE_ROOT / (case + ".json")).read_text())


def envelope(case="complete"):
    return json.loads(packet(case)["capture"])


def prepare(e=None):
    return m.prepare_capture(m.canonical_bytes(envelope() if e is None else e))


def change_body(e, index, mutate):
    b = json.loads(e["pages"][index]["body"])
    mutate(b)
    e["pages"][index]["body"] = m.canonical_bytes(b).decode()


@pytest.mark.parametrize("case,kind,count", [("complete", "CAPTURE_CANDIDATE", 3),
    ("count-drift", "INCOMPLETE_CAPTURE", 3), ("empty", "CAPTURE_CANDIDATE", 0)])
def test_complete_goldens_and_finite_denials(case, kind, count):
    result = m.replay_packet((m.FIXTURE_ROOT / (case + ".json")).read_bytes())
    assert result.candidate == packet(case)["expected"]
    assert result.summary()["capture_outcome"] == kind
    assert result.summary()["record_count"] == count
    assert result.summary()["outcome"] == "HOLD"
    assert not any(result.candidate["authority"].values())
    assert result.candidate["capture"]["coverage"] == "NOT_ESTABLISHED"
    assert "synthetic_observer" not in repr(result)


def test_users_minimized_before_any_snapshot_is_returned():
    c = prepare().candidate
    text = m.canonical_bytes(c).decode()
    for marker in ("DO_NOT_RETURN_PROFILE", "DO_NOT_RETURN_NESTED_PROFILE", "DO_NOT_RETURN_TOP_LEVEL", "invented@example.invalid"):
        assert marker not in text
    a = c["capture"]["records"][0]
    r = json.loads(a["raw_record_json"])
    assert r["user"] == {"id": 900000002, "login": "synthetic_observer"}
    assert r["identifications"][0]["user"] == {"id": 900000003, "login": "synthetic_identifier"}
    assert r["unknown_synthetic_field"] == {"retained": True}
    assert set(json.loads(c["pages"][0]["minimized_body"])) == {"results", "per_page", "total_results"}


def test_source_privacy_rights_and_plant_lineage_stay_separate():
    c = prepare().candidate
    a, b, z = c["capture"]["records"]
    assert a["route"] == "RAW_CANDIDATE" and (a["latitude"], a["longitude"]) == (38.5, -98.5)
    assert b["route"] == "QUARANTINE_CANDIDATE" and b["precision_class"] == "obscured_randomized"
    assert "NONCOMMERCIAL_TERMS" in b["reasons"] and b["geoprivacy_status"] == "obscured"
    assert z["latitude"] is None and z["precision_class"] == "withheld"
    assert {"LICENSE_UNRESOLVED", "GEOPRIVACY_PRIVATE"} <= set(z["reasons"])
    assert c["flora_checks"][0]["flora_scope"] == "SOURCE_PLANT_LINEAGE"
    assert c["flora_checks"][2]["flora_scope"] == "UNVERIFIED"
    assert c["flora_checks"][2]["reason_codes"] == ["FLORA_LINEAGE_UNVERIFIED"]
    assert c["source_descriptor_ref"] == "data/registry/fauna/sources/inaturalist.yaml"
    assert "CROSS_DOMAIN_USE_UNREVIEWED" in c["reason_codes"]
    assert prepare().summary()["quarantined"] == 2


def test_root_taxon_matches_but_unidentified_or_foreign_lineage_quarantines():
    for taxon, expected in [(None, "UNVERIFIED"), ({"id": 123, "ancestor_ids": [1]}, "UNVERIFIED"),
                            ({"id": m.PLANT_TAXON}, "SOURCE_PLANT_LINEAGE")]:
        e = envelope()
        change_body(e, 0, lambda b: b["results"][0].update(taxon=taxon))
        c = prepare(e).candidate
        assert c["flora_checks"][0]["flora_scope"] == expected
        if expected == "UNVERIFIED":
            assert c["flora_checks"][0]["route"] == "QUARANTINE_CANDIDATE"


def test_order_normalization_and_byte_identity_are_distinct():
    e = envelope(); e["pages"].reverse()
    assert prepare(e) == prepare()
    c = prepare().candidate
    e = envelope(); e["pages"][0]["retrieved_at"] = "2026-09-27T07:00:00.123456-05:00"
    assert prepare(e).candidate == c
    e["pages"][1]["retrieved_at"] = "2026-09-27T12:00:02.123456Z"
    later = prepare(e).candidate
    assert later["candidate_id"] == c["candidate_id"] and later["spec_hash"] != c["spec_hash"]
    assert c["pages"][0]["retrieved_at"] == "2026-09-27T12:00:00.123456Z"
    e = envelope(); e["pages"][0]["body"] = json.dumps(json.loads(e["pages"][0]["body"]), indent=2)
    formatted = prepare(e).candidate
    assert formatted["candidate_id"] != c["candidate_id"]
    assert formatted["capture"]["records"] == c["capture"]["records"]
    assert formatted["pages"][0]["minimized_body_sha256"] == c["pages"][0]["minimized_body_sha256"]


def test_original_and_minimized_preimages_are_never_conflated():
    c = prepare().candidate; p = c["pages"][0]
    assert p["source_body_sha256"] != p["minimized_body_sha256"]
    assert p["source_byte_length"] > p["minimized_byte_length"]
    m.validate_candidate(c, original_capture=m.canonical_bytes(envelope()))
    # A coherent changed original digest is only an asserted lineage annotation
    # without original bytes. Strong verification must and does reject it.
    c = copy.deepcopy(c); c["pages"][0]["source_body_sha256"] = "sha256:" + "f"*64
    c["capture"]["page_sha256"][0] = c["pages"][0]["source_body_sha256"]
    identity = [{k: p[k] for k in ("source_url", "source_body_sha256", "source_byte_length")} for p in c["pages"]]
    c["candidate_id"] = "inaturalist-ingest:" + m.digest_bytes(m.canonical_bytes(identity))
    c["spec_hash"] = m.spec_hash(c)
    m.validate_candidate(c)
    with pytest.raises(ValueError, match="ORIGINAL_CAPTURE_MISMATCH"):
        m.validate_candidate(c, original_capture=m.canonical_bytes(envelope()))


def test_exact_multiple_requires_empty_terminal_and_partial_stays_partial():
    e = envelope(); e["pages"] = e["pages"][:1]
    change_body(e, 0, lambda b: b.update(total_results=2))
    assert "END_NOT_REACHED" in prepare(e).candidate["capture"]["reasons"]
    terminal = envelope("empty")["pages"][0]
    terminal["source_url"] = m.obs.page_url(m.QUERY, id_above=900000102, per_page=2)
    terminal["retrieved_at"] = e["pages"][0]["retrieved_at"]
    e["pages"].append(terminal)
    assert prepare(e).candidate["capture"]["outcome"] == "CAPTURE_CANDIDATE"
    e = envelope(); e["pages"] = e["pages"][1:]
    assert "CURSOR_NOT_FROM_START" in prepare(e).candidate["capture"]["reasons"]
    e = envelope(); e["pages"][1]["source_url"] = m.obs.page_url(m.QUERY, id_above=900000101, per_page=2)
    assert "CURSOR_GAP_OR_OVERLAP" in prepare(e).candidate["capture"]["reasons"]


@pytest.mark.parametrize("status", [304, 429, 503, True, "200"])
def test_status_must_be_actual_http_200(status):
    e = envelope(); e["pages"][0]["status"] = status
    with pytest.raises(ValueError): prepare(e)


@pytest.mark.parametrize("bad", [b"", b"[]", b'{"pages":[],"pages":[]}', b'{"pages":NaN}',
    b'{"pages":1e999}', b"x"*(m.MAX_ENVELOPE+1)])
def test_envelope_json_is_strict_and_bounded(bad):
    with pytest.raises(ValueError): m.prepare_capture(bad)


@pytest.mark.parametrize("query", [m.obs.ObservationQuery(), m.obs.ObservationQuery(taxon_id=1),
    m.obs.ObservationQuery(bounds=None, place_id=1, taxon_id=m.PLANT_TAXON),
    m.obs.ObservationQuery(taxon_id=m.PLANT_TAXON, quality_grade="research")])
def test_only_fixed_plant_context_query_is_in_profile(query):
    e = envelope(); e["pages"][0]["source_url"] = m.obs.page_url(query, per_page=2)
    with pytest.raises(ValueError, match="QUERY_PROFILE_BOUND"): prepare(e)


def test_duplicates_mixed_windows_and_noncanonical_urls_rejected():
    e = envelope(); e["pages"].append(copy.deepcopy(e["pages"][0]))
    with pytest.raises(ValueError, match="DUPLICATE_PAGE"): prepare(e)
    e = envelope(); e["pages"][1]["source_url"] = m.obs.page_url(m.QUERY, id_above=900000102, per_page=3)
    change_body(e, 1, lambda b: b.update(per_page=3))
    with pytest.raises(ValueError, match="MIXED_QUERY"): prepare(e)
    e = envelope(); e["pages"][0]["source_url"] += "&api_key=private-marker"
    with pytest.raises(ValueError): prepare(e)
    e = envelope(); e["pages"][0]["source_url"] = e["pages"][0]["source_url"].replace("id_above=0", "id_above=00")
    with pytest.raises(ValueError, match="QUERY_PROFILE_BOUND"): prepare(e)
    e = envelope(); e["pages"][1]["source_url"] = m.obs.page_url(m.QUERY, id_above=0, per_page=2)
    # Distinct request with a shared observation identity cannot be silently merged.
    e["pages"][1]["source_url"] = m.obs.page_url(m.QUERY, id_above=1, per_page=2)
    change_body(e, 1, lambda b: b["results"][0].update(id=900000101))
    with pytest.raises(ValueError, match="DUPLICATE_OBSERVATION"): prepare(e)


@pytest.mark.parametrize("ancestry", [{}, "47126", [True], [1.0], [-1], [1]*65])
def test_malformed_ancestry_fails_whole_capture(ancestry):
    e = envelope(); change_body(e, 0, lambda b: b["results"][0]["taxon"].update(ancestor_ids=ancestry))
    with pytest.raises(ValueError, match="ANCESTRY_SHAPE"): prepare(e)


@pytest.mark.parametrize("user", [[], "private-marker", {"id": {"email": "private-marker"}}, {"login": []}])
def test_nested_user_values_cannot_smuggle_profiles(user):
    e = envelope(); change_body(e, 0, lambda b: b["results"][0].update(comments=[{"user": user}]))
    with pytest.raises(ValueError, match="MINIMIZED_USER_SHAPE"): prepare(e)


@pytest.mark.parametrize("field,value", [("observed_on", "2020-02-30"), ("observed_on", "2020"),
    ("observed_on", "2027-01-01"), ("updated_at", "2027-01-01T00:00:00Z"), ("updated_at", "bad")])
def test_dates_never_silently_change_or_exceed_capture(field, value):
    e = envelope(); change_body(e, 0, lambda b: b["results"][0].update({field: value}))
    with pytest.raises(ValueError): prepare(e)


def test_capture_time_order_and_shape_rejected():
    for value in ("2026-09-27T11:59:59Z", "2026-09-27", None):
        e = envelope(); e["pages"][1]["retrieved_at"] = value
        with pytest.raises(ValueError): prepare(e)


def test_byte_page_row_and_reported_count_budgets():
    for e in ({"pages": []}, {"pages": envelope()["pages"]*(m.MAX_PAGES+1)}):
        with pytest.raises(ValueError): prepare(e)
    e = envelope(); e["pages"][0]["body"] = "x"*(m.MAX_PAGE+1)
    with pytest.raises(ValueError): prepare(e)
    e = envelope(); change_body(e, 0, lambda b: b.update(total_results=m.MAX_REPORTED+1))
    with pytest.raises(ValueError, match="QUERY_PROFILE_BOUND"): prepare(e)
    e = envelope("empty"); e["pages"][0]["source_url"] = m.obs.page_url(m.QUERY, per_page=65)
    change_body(e, 0, lambda b: b.update(per_page=65))
    with pytest.raises(ValueError, match="QUERY_PROFILE_BOUND"): prepare(e)
    pages = []
    for i in range(6):
        p = copy.deepcopy(envelope("empty")["pages"][0])
        p["source_url"] = m.obs.page_url(m.QUERY, id_above=i, per_page=2)
        b = json.loads(p["body"]); b["padding"] = "x"*200000; p["body"] = m.canonical_bytes(b).decode(); pages.append(p)
    with pytest.raises(ValueError, match="CAPTURE_BYTE_BOUND"): prepare({"pages": pages})
    template = json.loads(envelope()["pages"][0]["body"])["results"][0]
    pages = []
    for start, size in ((1,64),(65,64),(129,64),(193,64),(257,1)):
        p = copy.deepcopy(envelope("empty")["pages"][0]); rows = []
        for i in range(start, start+size):
            r = copy.deepcopy(template); r["id"] = i; rows.append(r)
        p["source_url"] = m.obs.page_url(m.QUERY, id_above=start-1, per_page=64)
        p["body"] = m.canonical_bytes({"results": rows, "total_results": 258-start, "per_page": 64}).decode()
        pages.append(p)
    with pytest.raises(ValueError, match="RECORD_COUNT_BOUND"): prepare({"pages": pages})


@pytest.mark.parametrize("body", ['{"results":[],"results":[],"total_results":0,"per_page":2}',
    '{"results":[],"total_results":0,"per_page":2,"x":NaN}',
    '{"results":[],"total_results":0,"per_page":2,"x":1e999}'])
def test_page_json_duplicate_and_nonfinite_rejected(body):
    e = envelope("empty"); e["pages"][0]["body"] = body
    with pytest.raises(ValueError): prepare(e)


def test_deep_pages_and_malformed_record_reject_whole_capture():
    e = envelope(); change_body(e, 0, lambda b: b["results"][1].update(obscured=1))
    with pytest.raises(ValueError): prepare(e)
    nested = {}; root = nested
    for _ in range(40): root["x"] = {}; root = root["x"]
    e = envelope(); change_body(e, 0, lambda b: b["results"][0].update(nested=nested))
    with pytest.raises(ValueError, match="NESTING_BOUND"): prepare(e)


@pytest.mark.parametrize("tamper", ["authority", "record", "lineage", "minimized", "time", "source_hash"])
def test_recomputed_hash_does_not_bypass_replay(tamper):
    c = copy.deepcopy(prepare().candidate)
    if tamper == "authority": c["authority"]["public_use_allowed"] = True
    elif tamper == "record": c["capture"]["records"][1]["precision_class"] = "source_point"
    elif tamper == "lineage": c["flora_checks"][2]["flora_scope"] = "SOURCE_PLANT_LINEAGE"
    elif tamper == "minimized": c["pages"][0]["minimized_body"] += " "
    elif tamper == "time": c["pages"][0]["retrieved_at"] = "2026-09-27T07:00:00.123456-05:00"
    elif tamper == "source_hash": c["pages"][0]["source_body_sha256"] = "sha256:" + "f"*64
    c["spec_hash"] = m.spec_hash(c)
    with pytest.raises(ValueError): m.validate_candidate(c)


def test_packet_seal_and_golden_projection_are_both_checked():
    p = packet(); p["capture"] += " "
    with pytest.raises(ValueError, match="PACKET_HASH"): m.replay_packet(m.canonical_bytes(p))
    p = packet(); p["expected"]["flora_checks"][0]["route"] = "QUARANTINE_CANDIDATE"
    with pytest.raises(ValueError, match="GOLDEN_MISMATCH"): m.replay_packet(m.canonical_bytes(p))


def test_library_has_no_network_dependency(monkeypatch):
    def deny(*args, **kwargs): raise AssertionError("network attempted")
    monkeypatch.setattr(socket, "create_connection", deny)
    monkeypatch.setattr(socket, "getaddrinfo", deny)
    assert prepare().summary()["outcome"] == "HOLD"


@pytest.mark.parametrize("case", ["complete", "count-drift", "empty"])
def test_cli_is_aggregate_only_and_writes_no_files(case, tmp_path):
    env = dict(os.environ, KFM_NO_NETWORK="1", PYTHONDONTWRITEBYTECODE="1",
        PYTHONPATH=str(m.ROOT / "tools/ci/kfm_no_network") + os.pathsep + str(m.ROOT))
    result = subprocess.run([sys.executable, "-B", "-m", "pipelines.domains.flora.inaturalist_ingest", case],
        cwd=tmp_path, env=env, capture_output=True, text=True, check=True)
    summary = json.loads(result.stdout)
    assert summary["outcome"] == "HOLD" and result.stderr == ""
    for marker in ("synthetic", "900000", "38.5", "-98.5", "https:", "DO_NOT_RETURN", "Plantae"):
        assert marker not in result.stdout
    assert list(tmp_path.iterdir()) == []
