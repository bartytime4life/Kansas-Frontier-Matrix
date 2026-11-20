"""Synthetic TIGER ingestion with explicit integrity, hold and no-side-effect proof."""
import base64
import copy
import importlib
import io
import json
import os
from pathlib import Path
import socket
import stat
import struct
import subprocess
import sys
import zipfile

import pytest

m = importlib.import_module("pipelines.domains.roads-rail-trade.ingest_tiger_roads")
STEM = "tl_2025_20001_roads"


def packet(case="clean"):
    return json.loads((m.FIXTURE_ROOT / (case + ".json")).read_text())


def source(case="clean"):
    return base64.b64decode(packet(case)["package_base64"])


def prepare(raw=None, **kw):
    return m.prepare_package(source() if raw is None else raw,
                             file_name=kw.pop("file_name", STEM + ".zip"),
                             retrieved_at=kw.pop("retrieved_at", "2026-11-19T00:00:00Z"), **kw)


def repack(changes=None, *, extra=None, compression=zipfile.ZIP_STORED):
    with zipfile.ZipFile(io.BytesIO(source())) as z:
        members = {i.filename: z.read(i) for i in z.infolist()}
    members.update(changes or {})
    members.update(extra or {})
    out = io.BytesIO()
    with zipfile.ZipFile(out, "w", compression) as z:
        for name, body in members.items():
            z.writestr(name, body)
    return out.getvalue()


@pytest.mark.parametrize("case,route,reasons", [
    ("clean", "RAW_CANDIDATE", []),
    ("duplicate-identity", "QUARANTINE_CANDIDATE", ["IDENTITY_DUPLICATE"]),
])
def test_sealed_golden(case, route, reasons):
    result = m.replay_packet((m.FIXTURE_ROOT / (case + ".json")).read_bytes())
    assert result.candidate == packet(case)["expected"]
    assert result.candidate["inspection"]["provisional_route"] == route
    assert result.candidate["inspection"]["reason_codes"] == reasons
    assert result.candidate["inspection"]["feature_count"] == 2
    assert result.candidate["inspection"]["kansas_feature_count"] is None
    assert result.summary()["outcome"] == "HOLD"
    assert result.summary()["reference_bytes_match"] is False
    assert not any(result.candidate["authority"].values())
    assert "LINEARID" not in repr(result)


def test_exact_reference_comparison_is_independent_of_supplied_capture():
    c = prepare().candidate
    real = m.tiger.manifest_entry(m.tiger.load_manifest(), STEM + ".zip")
    assert c["reference"]["expected_sha256"] == "sha256:" + real["sha256"]
    assert c["reference"]["expected_byte_length"] == real["byte_length"]
    assert c["reference"]["sha256"] == m.digest_bytes((m.ROOT / m.MANIFEST).read_bytes())
    assert c["artifact"]["sha256"] != c["reference"]["expected_sha256"]
    assert "REFERENCE_BYTES_NOT_MATCHED" in c["reason_codes"]


def test_equivalent_capture_times_keep_identity_and_complete_candidate():
    assert prepare(retrieved_at="2026-11-18T18:00:00-06:00") == prepare()
    later = prepare(retrieved_at="2026-11-20T00:00:00Z").candidate
    c = prepare().candidate
    assert later["candidate_id"] == c["candidate_id"]
    assert later["spec_hash"] != c["spec_hash"]


def test_recompression_changes_exact_artifact_identity():
    other = prepare(repack()).candidate
    c = prepare().candidate
    assert c["inspection"] == other["inspection"]
    assert c["artifact"] != other["artifact"]
    assert c["candidate_id"] != other["candidate_id"]


@pytest.mark.parametrize("name", ["tl_2025_us_primaryroads.zip", "tl_2024_20001_roads.zip",
    "tl_2025_40001_roads.zip", "tl_2025_20999_roads.zip", "tl_2025_20_tract.zip", "../x.zip"])
def test_wrong_product_vintage_or_county_refused(name):
    with pytest.raises(ValueError):
        prepare(file_name=name)


@pytest.mark.parametrize("when", ["2024-12-31T00:00:00Z", "2026-11-19", "2026-02-30T00:00:00Z", None])
def test_invalid_capture_time_refused(when):
    with pytest.raises(ValueError):
        prepare(retrieved_at=when)


@pytest.mark.parametrize("bad", [b"", b"a" * (m.MAX_SOURCE + 1), "not bytes", b"not zip"])
def test_source_bounds(bad):
    with pytest.raises(ValueError):
        prepare(bad)


def test_zip_crc_checked_for_unparsed_geometry():
    raw = bytearray(repack())
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        i = z.getinfo(STEM + ".shp")
    name_len, extra_len = struct.unpack_from("<HH", raw, i.header_offset + 26)
    offset = i.header_offset + 30 + name_len + extra_len
    raw[offset + 120] ^= 1
    with pytest.raises(ValueError, match="TIGER_ZIP_INVALID"):
        prepare(bytes(raw))


def test_zip_expansion_count_and_path_bounds():
    cases = [repack(extra={"../escape": b"x"}),
             repack(extra={f"extra-{n}": b"x" for n in range(20)}),
             repack(extra={"bomb": b"x" * (m.MAX_MEMBER + 1)}, compression=zipfile.ZIP_DEFLATED)]
    for raw in cases:
        with pytest.raises(ValueError):
            prepare(raw)


def test_zip_symlink_and_unsupported_compression_refused():
    for compression, mode in [(zipfile.ZIP_BZIP2, 0), (zipfile.ZIP_STORED, stat.S_IFLNK)]:
        buf = io.BytesIO()
        with zipfile.ZipFile(buf, "w") as z:
            i = zipfile.ZipInfo("extra"); i.compress_type = compression; i.external_attr = mode << 16
            z.writestr(i, b"x")
        with pytest.raises(ValueError):
            prepare(buf.getvalue())


def test_unknown_crs_and_deleted_rows_remain_explicit_quarantine():
    with zipfile.ZipFile(io.BytesIO(source())) as z:
        dbf = bytearray(z.read(STEM + ".dbf"))
    header_len = struct.unpack_from("<H", dbf, 8)[0]
    dbf[header_len] = ord("*")
    for raw, code in [(repack({STEM + ".prj": b"unrecognized"}), "CRS_UNRECOGNIZED"),
                      (repack({STEM + ".dbf": bytes(dbf)}), "DELETED_RECORDS_PRESENT")]:
        c = prepare(raw).candidate
        assert code in c["reason_codes"]
        assert c["inspection"]["provisional_route"] == "QUARANTINE_CANDIDATE"
        assert c["route"] == "HOLD"


@pytest.mark.parametrize("key,value", [("package_sha256", "sha256:" + "0" * 64),
    ("package_base64", "!"), ("fixture_kind", "PROVIDER_CAPTURE"), ("extra", True),
    ("expected", {})])
def test_packet_tamper_refused(key, value):
    p = packet(); p[key] = value
    with pytest.raises(ValueError):
        m.replay_packet(m.canonical_bytes(p))


def test_malformed_and_oversized_json_refused():
    for raw in [b'{"a":1,"a":2}', b'{"a":NaN}', b'[]', b'a' * (m.MAX_PACKET + 1)]:
        with pytest.raises(ValueError):
            m.replay_packet(raw)


def test_candidate_hash_semantics_and_authority():
    for path, value in [(('authority', 'public_use_allowed'), True),
        (('reference', 'exact_bytes_match'), True), (('route',), 'RAW'),
        (('county_fips',), '20209'), (('spec_hash',), 'sha256:' + '0' * 64),
        (('inspection', 'deleted_count'), 3), (('extra',), True)]:
        c = copy.deepcopy(prepare().candidate)
        target = c
        for key in path[:-1]: target = target[key]
        target[path[-1]] = value
        if path != ('spec_hash',): c['spec_hash'] = m.spec_hash(c)
        with pytest.raises(ValueError): m.validate_candidate(c)


def test_no_socket_side_effects(monkeypatch):
    def denied(*a, **kw): raise AssertionError("NETWORK_FORBIDDEN")
    monkeypatch.setattr(socket, 'socket', denied)
    monkeypatch.setattr(socket, 'create_connection', denied)
    prepare()


@pytest.mark.parametrize("case", ["clean", "duplicate-identity"])
def test_cli_is_aggregate_only_and_writes_no_files(case, tmp_path):
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', KFM_NO_NETWORK='1')
    env['PYTHONPATH'] = os.pathsep.join([str(m.ROOT/'tools/ci/kfm_no_network'), str(m.ROOT),
        str(m.ROOT/'packages/connectors-core/src'), env.get('PYTHONPATH', '')])
    p = subprocess.run([sys.executable, '-B', '-m', m.__name__, case], cwd=tmp_path,
                       env=env, text=True, capture_output=True, check=True)
    summary = json.loads(p.stdout)
    assert summary['outcome'] == 'HOLD'
    assert not summary['source_admitted'] and not summary['lifecycle_write']
    assert all(token not in p.stdout for token in ['SYNTHETIC ROAD', 'LINEARID', '-99.', '20001', 'package_base64'])
    assert list(tmp_path.iterdir()) == []
    assert p.stderr == ''


def test_reference_and_capture_cannot_be_rewritten_even_with_new_spec_hash():
    for mutate in [lambda c: c['reference'].update(expected_sha256=c['artifact']['sha256']),
                   lambda c: c['reference'].update(sha256='sha256:' + '0' * 64),
                   lambda c: c.update(created_at='2024-01-01T00:00:00Z')]:
        c = copy.deepcopy(prepare().candidate)
        mutate(c)
        c['spec_hash'] = m.spec_hash(c)
        with pytest.raises(ValueError): m.validate_candidate(c)


def test_reference_byte_match_never_changes_admission_or_hold(monkeypatch):
    # An injected reference exercises the match branch without downloading or
    # relabeling the committed provider bytes. The disk manifest stays untouched.
    manifest = m.tiger.load_manifest()
    entry = m.tiger.manifest_entry(manifest, STEM + '.zip')
    entry.update(sha256=m.digest_bytes(source()).removeprefix('sha256:'), byte_length=len(source()))
    original = m.read_regular
    def read(path, limit):
        return m.canonical_bytes(manifest) if path == m.ROOT/m.MANIFEST else original(path, limit)
    monkeypatch.setattr(m, 'read_regular', read)
    c = prepare().candidate
    assert c['reference']['exact_bytes_match'] is True
    assert 'REFERENCE_BYTES_NOT_MATCHED' not in c['reason_codes']
    assert c['route'] == 'HOLD' and not any(c['authority'].values())


def test_summary_refuses_mutated_authority():
    result = prepare()
    result.candidate['authority']['public_use_allowed'] = True
    with pytest.raises(ValueError): result.summary()


def test_missing_required_member_refused():
    with zipfile.ZipFile(io.BytesIO(source())) as z:
        members = {i.filename: z.read(i) for i in z.infolist() if not i.filename.endswith('.dbf')}
    out = io.BytesIO()
    with zipfile.ZipFile(out, 'w') as z:
        for name, body in members.items(): z.writestr(name, body)
    with pytest.raises(ValueError, match='MEMBER_MISSING'): prepare(out.getvalue())
