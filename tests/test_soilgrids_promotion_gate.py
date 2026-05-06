import hashlib
import json
import subprocess
import sys
from pathlib import Path

import pytest
from tools.soilgrids import soilgrids_promotion_gate as g


def mk_bundle(tmp: Path):
    cog = tmp / "a.tif"
    payload = b"cog-bytes"
    cog.write_bytes(payload)
    h = hashlib.sha256(payload).hexdigest()
    n = len(payload)
    (tmp / "run.json").write_text(json.dumps({"status": "success", "source": "soilgrids_wcs", "spec_hash": "run1", "bbox": [0, 0, 1, 1]}))
    (tmp / "cogr.json").write_text(json.dumps({"status": "success", "source": "soilgrids_cog_normalize", "spec_hash": "cog1", "source_receipt": {"spec_hash": "run1"}, "output_path": str(cog), "output_sha256": h, "output_bytes": n, "raster": {"crs": "EPSG:4326"}}))
    (tmp / "stacr.json").write_text(json.dumps({"status": "success", "source": "soilgrids_stac_register", "spec_hash": "stac1", "source_receipts": {"run_spec_hash": "run1", "cog_spec_hash": "cog1"}, "asset_sha256": h, "asset_bytes": n, "bbox": [0, 0, 1, 1]}))
    (tmp / "item.json").write_text(json.dumps({"id": "i1", "stac_version": "1.1.0", "collection": "c1", "bbox": [0, 0, 1, 1], "assets": {"data": {"href": "a.tif", "file:size": n, "file:checksum": "1220" + h}}, "links": [{"rel": "self"}, {"rel": "root"}, {"rel": "collection"}], "properties": {"proj:code": "EPSG:4326", "proj:shape": [1, 1], "proj:transform": [1, 0, 0, 0, 1, 0]}}))
    (tmp / "col.json").write_text(json.dumps({"id": "c1", "stac_version": "1.1.0", "license": "CC-BY-4.0", "links": [{"rel": "item", "href": "item.json"}]}))
    (tmp / "cat.json").write_text(json.dumps({"id": "cat1", "stac_version": "1.1.0", "links": [{"rel": "child", "href": "col.json"}, {"rel": "self", "href": "cat.json"}]}))


def args(tmp):
    return dict(run_receipt=str(tmp / "run.json"), cog_receipt=str(tmp / "cogr.json"), stac_receipt=str(tmp / "stacr.json"), stac_item=str(tmp / "item.json"), stac_collection=str(tmp / "col.json"), stac_catalog=str(tmp / "cat.json"), policy_profile=None, output_dir=str(tmp / "out"), decision_mode="strict", overwrite=True)


def test_promotes_valid_bundle(tmp_path):
    mk_bundle(tmp_path)
    de, _, _ = g.evaluate_promotion_gate(**args(tmp_path))
    assert de["decision"] == "promote"


def test_rejects_cog_sha256_mismatch(tmp_path):
    mk_bundle(tmp_path)
    c = json.loads((tmp_path / "cogr.json").read_text())
    c["output_sha256"] = "x"
    (tmp_path / "cogr.json").write_text(json.dumps(c))
    de, _, _ = g.evaluate_promotion_gate(**args(tmp_path))
    assert de["decision"] == "reject"


def test_quarantines_warning_failure_in_strict_mode(tmp_path):
    mk_bundle(tmp_path)
    (tmp_path / "cat.json").write_text(json.dumps({"id": "cat1", "stac_version": "1.1.0", "links": []}))
    de, _, _ = g.evaluate_promotion_gate(**args(tmp_path))
    assert de["decision"] == "quarantine"


def test_promotes_warning_failure_in_permissive_mode(tmp_path):
    mk_bundle(tmp_path)
    (tmp_path / "cat.json").write_text(json.dumps({"id": "cat1", "stac_version": "1.1.0", "links": []}))
    a = args(tmp_path)
    a["decision_mode"] = "permissive"
    de, _, _ = g.evaluate_promotion_gate(**a)
    assert de["decision"] == "promote"


def test_exit_code_promote(tmp_path):
    mk_bundle(tmp_path)
    a = args(tmp_path)
    r = subprocess.run([sys.executable, "soilgrids_promotion_gate.py", "--run-receipt", a["run_receipt"], "--cog-receipt", a["cog_receipt"], "--stac-receipt", a["stac_receipt"], "--stac-item", a["stac_item"], "--stac-collection", a["stac_collection"], "--stac-catalog", a["stac_catalog"], "--output-dir", a["output_dir"]], capture_output=True, text=True)
    assert r.returncode == 0
