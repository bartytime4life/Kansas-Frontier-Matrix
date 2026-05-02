import json
from pathlib import Path
import pytest

import soilgrids_evidence_crate as mod


def _write(p: Path, obj):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj), encoding='utf-8')


def _base(tmp_path: Path):
    run = tmp_path/'run.json'; _write(run,{"schema":"RunReceipt.v1","spec_hash":"runhash"})
    cog = tmp_path/'cog.json'; _write(cog,{"schema":"CogReceipt.v1","spec_hash":"coghash","source_receipt":{"spec_hash":"runhash"}})
    stac = tmp_path/'stac.json'; _write(stac,{"schema":"StacRegistrationReceipt.v1","spec_hash":"stachash","source_receipts":{"cog_spec_hash":"coghash"}})
    rel = tmp_path/'release.json'; _write(rel,{"schema":"ReleaseManifest.v1","spec_hash":"relhash"})
    pub = tmp_path/'publish.json'; _write(pub,{"schema":"PublishReceipt.v1","spec_hash":"pubhash"})
    view = tmp_path/'viewer.json'; _write(view,{"schema":"ViewerManifest.v1","spec_hash":"viewhash"})
    dist = tmp_path/'dist.json'; _write(dist,{"schema":"DistributionReceipt.v1","spec_hash":"disthash","viewer_spec_hash":"viewhash"})
    return run,cog,stac,rel,pub,view,dist


def test_rejects_missing_required_crate_root():
    with pytest.raises(SystemExit):
        mod.parse_args([])


def test_rejects_missing_explicit_evidence_file(tmp_path):
    with pytest.raises(mod.EvidenceError):
        mod.validate_evidence_file(tmp_path/'missing.json')


def test_rejects_malformed_json(tmp_path):
    p = tmp_path/'bad.json'; p.write_text('{', encoding='utf-8')
    with pytest.raises(mod.EvidenceError):
        mod.validate_evidence_file(p)


def test_classifies_evidence_by_schema(tmp_path):
    p = tmp_path/'x.json'; _write(p,{"schema":"RunReceipt.v1"})
    ev = mod.validate_evidence_file(p)
    assert ev.role == 'source_receipt'


def test_rejects_unknown_schema_by_default(tmp_path):
    p = tmp_path/'x.json'; _write(p,{"schema":"Unknown.v1"})
    with pytest.raises(mod.EvidenceError): mod.validate_evidence_file(p)


def test_allows_unknown_schema_when_flag_set(tmp_path):
    p = tmp_path/'x.json'; _write(p,{"schema":"Unknown.v1"})
    ev = mod.validate_evidence_file(p, allow_unknown_evidence=True)
    assert ev.role == 'unknown'


def test_cross_layer_chain_valid(tmp_path):
    run,cog,stac,_,_,view,dist = _base(tmp_path)
    evs = [mod.validate_evidence_file(p) for p in [run,cog,stac,view,dist]]
    ok, errs = mod.validate_cross_layer_chain({e.role:e for e in evs})
    assert ok and not errs


def test_rejects_broken_cog_to_run_chain(tmp_path):
    run,cog,*rest = _base(tmp_path)
    _write(cog,{"schema":"CogReceipt.v1","spec_hash":"coghash","source_receipt":{"spec_hash":"bad"}})
    evs=[mod.validate_evidence_file(p) for p in [run,cog,rest[0]]]
    ok,_=mod.validate_cross_layer_chain({e.role:e for e in evs})
    assert not ok


def test_receipt_written_on_success(tmp_path):
    run,cog,stac,rel,pub,view,dist = _base(tmp_path)
    args = mod.parse_args(["--crate-root",str(tmp_path/'crates'),"--crate-mode","metadata-only","--dataset-id","soilgrids-v2","--crate-title","t","--run-receipt",str(run),"--cog-receipt",str(cog),"--stac-receipt",str(stac),"--release-manifest",str(rel),"--publish-receipt",str(pub),"--viewer-manifest",str(view),"--distribution-receipt",str(dist)])
    receipt, code = mod.build_evidence_crate(args)
    assert code == 0
    assert receipt.exists()


def test_exit_code_chain_failure(tmp_path):
    run,cog,stac,rel,pub,view,dist = _base(tmp_path)
    _write(dist,{"schema":"DistributionReceipt.v1","viewer_spec_hash":"bad"})
    rc = mod.main(["--crate-root",str(tmp_path/'crates'),"--crate-mode","metadata-only","--dataset-id","soilgrids-v2","--crate-title","t","--run-receipt",str(run),"--cog-receipt",str(cog),"--stac-receipt",str(stac),"--release-manifest",str(rel),"--publish-receipt",str(pub),"--viewer-manifest",str(view),"--distribution-receipt",str(dist)])
    assert rc == 20
