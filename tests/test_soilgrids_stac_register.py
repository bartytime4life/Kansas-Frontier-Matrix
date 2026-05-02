import json
from pathlib import Path

import pytest

import soilgrids_stac_register as m


def _cog_bytes() -> bytes:
    return b"fake-cog-bytes"


def _mk_receipt(tmp_path: Path, **overrides):
    cog = tmp_path / "asset.tif"
    cog.write_bytes(_cog_bytes())
    sha = m._sha256_file(cog)
    receipt = {
        "schema": "CogReceipt.v1",
        "status": "success",
        "output_path": str(cog),
        "output_sha256": sha,
        "output_bytes": cog.stat().st_size,
        "spec_hash": "a" * 64,
        "raster": {
            "bbox": [-98.0, 37.0, -94.0, 41.0],
            "crs": "EPSG:4326",
            "height": 20,
            "width": 30,
            "geotransform": [1, 2, 3, 4, 5, 6],
        },
    }
    receipt.update(overrides)
    p = tmp_path / "cog_receipt.json"
    p.write_text(json.dumps(receipt))
    return p, cog


def _kwargs(tmp_path: Path, receipt_path: Path):
    return dict(cog_receipt_path=str(receipt_path), catalog_dir=str(tmp_path / "stac"), catalog_id="soilgrids-local", catalog_title="Local", collection_id="soilgrids-v2", collection_title="V2", dataset_datetime="2020-01-01T00:00:00Z", license="CC-BY-4.0", property="soc", depth="0-5cm", statistic="mean", unit="g/kg", asset_href_mode="relative", stac_version="1.1.0")


def test_rejects_missing_cog_receipt(tmp_path: Path):
    with pytest.raises(FileNotFoundError):
        m.register_cog_to_stac(**_kwargs(tmp_path, tmp_path / "missing.json"))


def test_rejects_failed_cog_receipt(tmp_path: Path):
    rp, _ = _mk_receipt(tmp_path, status="error")
    with pytest.raises(ValueError):
        m.register_cog_to_stac(**_kwargs(tmp_path, rp))


def test_item_id_is_stable(tmp_path: Path):
    rp, _ = _mk_receipt(tmp_path)
    r1 = m.register_cog_to_stac(**_kwargs(tmp_path, rp))
    r2 = m.register_cog_to_stac(**_kwargs(tmp_path, rp))
    assert r1["item_id"] == r2["item_id"]


def test_spec_hash_is_stable(tmp_path: Path):
    rp, _ = _mk_receipt(tmp_path)
    r1 = m.register_cog_to_stac(**_kwargs(tmp_path, rp))
    r2 = m.register_cog_to_stac(**_kwargs(tmp_path, rp))
    assert r1["spec_hash"] == r2["spec_hash"]


def test_stac_1_1_uses_bands(tmp_path: Path):
    rp, _ = _mk_receipt(tmp_path)
    kwargs = _kwargs(tmp_path, rp)
    kwargs["stac_version"] = "1.1.0"
    rec = m.register_cog_to_stac(**kwargs)
    item = json.loads(Path(rec["item_path"]).read_text())
    assert "bands" in item["assets"]["data"]


def test_stac_1_0_uses_raster_bands(tmp_path: Path):
    rp, _ = _mk_receipt(tmp_path)
    kwargs = _kwargs(tmp_path, rp)
    kwargs["stac_version"] = "1.0.0"
    rec = m.register_cog_to_stac(**kwargs)
    item = json.loads(Path(rec["item_path"]).read_text())
    assert "raster:bands" in item["assets"]["data"]
