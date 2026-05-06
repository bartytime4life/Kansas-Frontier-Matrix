from pathlib import Path
from tools.resolvers.hydrology.resolve_huc12_comid_timeslice import resolve
R=Path('tests/fixtures/hydrology/huc12_comid_release')

def test_resolves_manifest_and_timeslice():
    r=resolve(R/'valid/catalog.jsonl','031300010101','2026-03-01')
    assert r['ok'] and r['selected']['manifest_id'].startswith('031300010101@') and r['selected']['timeslice_id'].startswith('huc12::')

def test_rejects_no_match(): assert not resolve(R/'valid/catalog.jsonl','031300010101','2027-01-01')['ok']
def test_rejects_unpublished_default(): assert not resolve(R/'invalid/catalog_unpublished.jsonl','031300010101','2026-03-01')['ok']
def test_rejects_lifecycle_leakage(): assert not resolve(R/'invalid/catalog_raw_uri.jsonl','031300010101','2026-03-01')['ok']
def test_rejects_overlap_conflict(): assert not resolve(R/'invalid/catalog_overlapping_conflict.jsonl','031300010101','2026-03-01')['ok']
def test_supports_snapshot_filter(): assert resolve(R/'valid/catalog.jsonl','031300010101','2026-03-01',snapshot_id='wbd-2026-01')['ok']
def test_deterministic_keys():
    import json
    out=json.dumps(resolve(R/'valid/catalog.jsonl','031300010101','2026-03-01'),sort_keys=True,separators=(',',':'))
    assert out==json.dumps(json.loads(out),sort_keys=True,separators=(',',':'))
