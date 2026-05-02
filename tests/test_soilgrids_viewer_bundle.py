import json, subprocess, sys
from pathlib import Path
import pytest
from soilgrids_viewer_bundle import parse_args, build_viewer_bundle, ViewerError, compute_viewer_spec_hash


def wj(p,o): p.parent.mkdir(parents=True, exist_ok=True); p.write_text(json.dumps(o), encoding='utf-8')

@pytest.fixture
def fx(tmp_path):
    d=tmp_path
    wj(d/'tile_package_manifest.json',{"tile_package_id":"tp1"})
    wj(d/'tile_package_receipt.json',{"status":"success","tile_package_id":"tp1","release_id":"r1","publish_spec_hash":"ph1"})
    wj(d/'tile_validation_report.json',{"summary":{"required_failed":0}})
    wj(d/'tilejson.json',{"tilejson":"3.0.0","tiles":["../tiles/{z}/{x}/{y}.png"],"bounds":[-1,-1,1,1],"center":[0,0,1],"minzoom":0,"maxzoom":1,"attribution":"a"})
    wj(d/'maplibre_style.json',{"version":8,"sources":{"s":{"type":"raster","tiles":["../tiles/{z}/{x}/{y}.png"],"tileSize":256}},"layers":[{"id":"l","type":"raster","source":"s"}]})
    wj(d/'release_manifest.json',{"release_id":"r1"}); wj(d/'publish_receipt.json',{"publish_spec_hash":"ph1"})
    wj(d/'serve_access_receipt.json',{}); wj(d/'serve_validation_report.json',{})
    wj(d/'stac_item.json',{"id":"i1","collection":"c1","properties":{"title":"t","description":"d"}})
    (d/'maplibre-gl.js').write_text('x'); (d/'maplibre-gl.css').write_text('x'); (d/'pmtiles.js').write_text('x')
    return d

def mkargs(fx, **kw):
    base=["--tile-package-manifest",str(fx/'tile_package_manifest.json'),"--tile-package-receipt",str(fx/'tile_package_receipt.json'),"--tile-validation-report",str(fx/'tile_validation_report.json'),"--tilejson",str(fx/'tilejson.json'),"--maplibre-style",str(fx/'maplibre_style.json'),"--release-manifest",str(fx/'release_manifest.json'),"--publish-receipt",str(fx/'publish_receipt.json'),"--stac-item",str(fx/'stac_item.json'),"--viewer-root",str(fx/'viewer_bundles'),"--viewer-mode","link-existing-tile-package","--maplibre-js",str(fx/'maplibre-gl.js'),"--maplibre-css",str(fx/'maplibre-gl.css'),"--serve-access-receipt",str(fx/'serve_access_receipt.json'),"--serve-validation-report",str(fx/'serve_validation_report.json')]
    for k,v in kw.items():
        base += [f"--{k}"] if v is True else [f"--{k}",str(v)]
    return parse_args(base)

# representative required tests

def test_rejects_missing_tile_package_manifest(fx):
    with pytest.raises(ViewerError):
        build_viewer_bundle(mkargs(fx, **{"tile-package-manifest":fx/'none.json'}))

def test_rejects_failed_tile_package_receipt(fx):
    wj(fx/'tile_package_receipt.json',{"status":"error","tile_package_id":"tp1"})
    with pytest.raises(ViewerError): build_viewer_bundle(mkargs(fx))

def test_viewer_manifest_written_on_success(fx):
    receipt,_=build_viewer_bundle(mkargs(fx))
    assert receipt.exists()
    root=receipt.parent
    assert (root/'viewer_manifest.json').exists()

def test_viewer_receipt_written_on_success(fx):
    receipt,_=build_viewer_bundle(mkargs(fx)); assert json.loads(receipt.read_text())["schema"]=="ViewerReceipt.v1"

def test_viewer_validation_report_written_on_success(fx):
    receipt,_=build_viewer_bundle(mkargs(fx)); assert (receipt.parent/'viewer_validation_report.json').exists()

def test_dry_run_writes_receipt(fx):
    receipt,code=build_viewer_bundle(mkargs(fx, **{"dry-run":True})); assert code==5 and receipt.exists()

def test_dry_run_writes_no_bundle(fx):
    receipt,code=build_viewer_bundle(mkargs(fx, **{"dry-run":True})); assert not (fx/'viewer_bundles'/'r1_viewer').exists()

def test_viewer_spec_hash_stable():
    s={"a":1}; assert compute_viewer_spec_hash(s)==compute_viewer_spec_hash(s)
