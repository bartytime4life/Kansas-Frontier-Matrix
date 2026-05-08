import pytest
pytest.importorskip("jsonschema", reason="jsonschema dependency unavailable in this environment")

from pathlib import Path
from tools.validators.hydrology import validate_huc12_comid_catalog_record as v
R=Path('tests/fixtures/hydrology/huc12_comid_release')
CS=Path('schemas/hydrology/huc12_comid_catalog_record.schema.json')
ES=Path('schemas/hydrology/huc12_comid_evidence_bundle.schema.json')

def test_valid_catalog_record_passes():
    r=v.validate(R/'valid/catalog_record.json',CS,R/'valid/evidence_bundle.json',ES)
    assert r['ok']

def test_bad_lifecycle_uri_fails():
    p=R/'invalid/tmp.json'; p.write_text((R/'valid/catalog_record.json').read_text().replace('/published/','/raw/'))
    assert not v.validate(p,CS)['ok']

def test_evidence_drawer_mismatch_fails():
    p=R/'invalid/tmp2.json'; p.write_text((R/'valid/catalog_record.json').read_text().replace('"published"','"revoked"',1))
    assert any('evidence_drawer:mismatch' in e for e in v.validate(p,CS)['errors'])

def test_invalid_stable_id_fails():
    p=R/'invalid/tmp3.json'; p.write_text((R/'valid/catalog_record.json').read_text().replace('031300010101@','bad@'))
    assert any('ids:invalid manifest_id'==e for e in v.validate(p,CS)['errors'])

def test_evidence_bundle_mismatch_fails():
    r=v.validate(R/'valid/catalog_record.json',CS,R/'invalid/evidence_mismatched_timeslice.json',ES)
    assert any('evidence_bundle:mismatch timeslice_id'==e for e in r['errors'])
