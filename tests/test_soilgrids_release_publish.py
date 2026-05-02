import json
from pathlib import Path
import pytest

from soilgrids_release_publish import load_publish_inputs, publish_approved_bundle, compute_release_id, compute_publish_spec_hash, PublishError


def _write(p: Path, obj):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(obj), encoding="utf-8")


@pytest.fixture
def bundle(tmp_path):
    cog = tmp_path / "src" / "a.tif"
    cog.parent.mkdir(parents=True)
    cog.write_bytes(b"fake-cog")
    import hashlib
    sha = hashlib.sha256(b"fake-cog").hexdigest()
    run = {"status": "success", "spec_hash": "run1"}
    cre = {"status": "success", "spec_hash": "cog1", "source_receipt": {"spec_hash": "run1"}, "output_bytes": 8, "output_sha256": sha}
    sre = {"status": "success", "spec_hash": "st1", "source_receipts": {"run_spec_hash": "run1", "cog_spec_hash": "cog1"}, "asset_sha256": sha, "asset_bytes": 8, "asset_path": str(cog), "bbox": [0,0,1,1]}
    val = {"status": "success", "summary": {"required_failed": 0}, "cross_layer": {"provenance_chain_valid": True}}
    dec = {"schema": "DecisionEnvelope.v1", "decision": "promote", "spec_hash": "dec1", "promotion": {"eligible": True, "item_id": "item1", "collection_id": "soilgrids-v2", "catalog_id": "cat1"}}
    item = {"id": "item1", "collection": "soilgrids-v2", "bbox": [0,0,1,1], "properties": {"datetime": "2020-01-01T00:00:00Z", "license": "CC-BY-4.0"}, "assets": {"data": {"href": str(cog), "file:size": 8, "file:checksum": f"1220{sha}"}}, "links": [{"rel": "self", "href": "x"}, {"rel": "root", "href": "x"}, {"rel": "collection", "href": "x"}]}
    coll = {"id": "soilgrids-v2", "links": [{"rel": "self", "href": "x"}, {"rel": "root", "href": "x"}]}
    cat = {"id": "cat1", "links": [{"rel": "self", "href": "x"}, {"rel": "child", "href": "x"}]}
    files = {
        "decision_envelope": tmp_path / "decision.json", "validation_report": tmp_path / "validation.json", "run_receipt": tmp_path / "run.json", "cog_receipt": tmp_path / "cog.json", "stac_receipt": tmp_path / "stac_receipt.json", "stac_item": tmp_path / "item.json", "stac_collection": tmp_path / "collection.json", "stac_catalog": tmp_path / "catalog.json"
    }
    for k, obj in [("decision_envelope", dec), ("validation_report", val), ("run_receipt", run), ("cog_receipt", cre), ("stac_receipt", sre), ("stac_item", item), ("stac_collection", coll), ("stac_catalog", cat)]: _write(files[k], obj)
    return tmp_path, cog, files


def test_rejects_missing_decision_envelope(bundle):
    tmp, cog, files = bundle
    files["decision_envelope"].unlink()
    with pytest.raises(PublishError):
        load_publish_inputs(**{**{k: str(v) for k, v in files.items()}, "cog_asset": str(cog)})


@pytest.mark.parametrize("decision", ["quarantine", "reject"])
def test_rejects_quarantine_or_reject(bundle, decision):
    tmp, cog, files = bundle
    d = json.loads(files["decision_envelope"].read_text()); d["decision"] = decision; _write(files["decision_envelope"], d)
    inp = load_publish_inputs(**{**{k: str(v) for k, v in files.items()}, "cog_asset": str(cog)})
    with pytest.raises(PublishError):
        publish_approved_bundle(inp, tmp / "published")


def test_release_id_is_stable(bundle):
    tmp, cog, files = bundle
    inp = load_publish_inputs(**{**{k: str(v) for k, v in files.items()}, "cog_asset": str(cog)})
    h = compute_publish_spec_hash(inp, "immutable-release", "latest-release", "relative")
    assert compute_release_id("soilgrids-v2", "2020-01-01T00:00:00Z", h) == compute_release_id("soilgrids-v2", "2020-01-01T00:00:00Z", h)


def test_dry_run_writes_receipt(bundle):
    tmp, cog, files = bundle
    inp = load_publish_inputs(**{**{k: str(v) for k, v in files.items()}, "cog_asset": str(cog)})
    _, code, path = publish_approved_bundle(inp, tmp / "published", mode="dry-run")
    assert code == 5
    assert path.exists()


def test_publish_success(bundle):
    tmp, cog, files = bundle
    inp = load_publish_inputs(**{**{k: str(v) for k, v in files.items()}, "cog_asset": str(cog)})
    receipt, code, path = publish_approved_bundle(inp, tmp / "published", mode="immutable-release")
    assert code == 0
    assert path.exists()
    assert receipt["status"] == "success"
    assert (tmp / "published" / "latest.json").exists()
