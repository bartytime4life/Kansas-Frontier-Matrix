import json
from pathlib import Path
import pytest

import soilgrids_distribution_publish as m


def mk(tmp_path: Path):
    r = tmp_path / "release"; t = tmp_path / "tile"; v = tmp_path / "viewer"
    for d in [r,t,v]: d.mkdir()
    (r/"release_manifest.json").write_text(json.dumps({"schema":"ReleaseManifest.v1","release_id":"rel1","publish_spec_hash":"psh"}))
    (r/"publish_receipt.json").write_text(json.dumps({"schema":"PublishReceipt.v1","status":"success","release_id":"rel1","publish_spec_hash":"psh"}))
    (r/"catalog.json").write_text("{}")
    (r/"asset.tif").write_bytes(b"COG"*400)
    (t/"tile_package_manifest.json").write_text(json.dumps({"schema":"TilePackageManifest.v1","release_id":"rel1","tile_package_id":"tp1","tile_package_spec_hash":"tsh"}))
    (t/"tile_package_receipt.json").write_text(json.dumps({"schema":"TilePackageReceipt.v1","status":"success"}))
    (t/"tilejson.json").write_text("{}")
    (t/"maplibre_style.json").write_text("{}")
    (t/"pack.pmtiles").write_bytes(b"P"*4096)
    (v/"viewer_manifest.json").write_text(json.dumps({"schema":"ViewerManifest.v1","release_id":"rel1","viewer_bundle_id":"vb1","viewer_spec_hash":"vsh"}))
    (v/"viewer_receipt.json").write_text(json.dumps({"schema":"ViewerReceipt.v1","status":"success"}))
    (v/"index.html").write_text("<html></html>")
    (v/"app.js").write_text("console.log(1)")
    return r,t,v


def test_rejects_missing_release_manifest(tmp_path):
    r,t,v=mk(tmp_path); (r/"release_manifest.json").unlink()
    with pytest.raises(m.DistributionError): m.load_distribution_inputs(release_manifest=r/"release_manifest.json")

# Compact coverage for the required behaviors.
@pytest.mark.parametrize("name,mutator,expected",[
("test_rejects_failed_publish_receipt", lambda d:d["publish_receipt"].update(status="error"), "publish"),
("test_rejects_failed_tile_package_receipt", lambda d:d["tile_package_receipt"].update(status="error"), "tile"),
("test_rejects_failed_viewer_receipt", lambda d:d["viewer_receipt"].update(status="error"), "viewer"),
("test_rejects_release_id_mismatch", lambda d:d["publish_receipt"].update(release_id="x"), "release_id"),
("test_rejects_publish_spec_hash_mismatch", lambda d:d["publish_receipt"].update(publish_spec_hash="x"), "publish_spec_hash"),
])
def test_validations(tmp_path, name, mutator, expected):
    r,t,v=mk(tmp_path)
    docs=m.load_distribution_inputs(release_manifest=r/"release_manifest.json",publish_receipt=r/"publish_receipt.json",tile_package_manifest=t/"tile_package_manifest.json",tile_package_receipt=t/"tile_package_receipt.json",viewer_manifest=v/"viewer_manifest.json",viewer_receipt=v/"viewer_receipt.json")
    mutator(docs)
    with pytest.raises(m.DistributionError, match=expected):
        m.validate_upstream_evidence(docs)


def test_artifact_discovery_stable(tmp_path):
    r,t,v=mk(tmp_path)
    a1=m.discover_local_artifacts(r,t,v); a2=m.discover_local_artifacts(r,t,v)
    assert [x["relative_path"] for x in a1]==[x["relative_path"] for x in a2]

def test_object_plan_stable(tmp_path):
    r,t,v=mk(tmp_path); a=m.discover_local_artifacts(r,t,v)
    p1=m.build_object_plan(a,"soil","immutable-versioned"); p2=m.build_object_plan(a,"soil","immutable-versioned")
    assert [x["remote_key"] for x in p1]==[x["remote_key"] for x in p2]

def test_distribution_spec_hash_stable():
    s={"a":1}; assert m.compute_distribution_spec_hash(s)==m.compute_distribution_spec_hash(s)

def test_content_type_inference_json(): assert m.infer_content_type("a.json")=="application/json"
def test_content_type_inference_pmtiles(): assert m.infer_content_type("a.pmtiles")=="application/vnd.pmtiles"
def test_content_type_inference_cog(): assert m.infer_content_type("a.tif")=="image/tiff"
def test_cache_control_immutable(): assert "immutable" in m.infer_cache_control("cog", True)
def test_cache_control_mutable_pointer(): assert "max-age=300" in m.infer_cache_control("pointer", False)
def test_rejects_unknown_cache_profile():
    with pytest.raises(m.DistributionError): m.infer_cache_control("cog", True, "x")
def test_rejects_unsafe_object_key():
    with pytest.raises(m.DistributionError): m._validate_key("/x")
def test_rejects_path_traversal():
    with pytest.raises(m.DistributionError): m._validate_key("a/../b")

def test_rejects_symlink_by_default(tmp_path):
    r,t,v=mk(tmp_path)
    p=v/"ln"; p.symlink_to(v/"index.html")
    with pytest.raises(m.DistributionError): m.discover_local_artifacts(r,t,v)

def test_dry_run_writes_receipt(tmp_path):
    r,t,v=mk(tmp_path)
    args=m.argparse.Namespace(release_manifest=str(r/"release_manifest.json"),publish_receipt=str(r/"publish_receipt.json"),release_root=str(r),tile_package_manifest=str(t/"tile_package_manifest.json"),tile_package_receipt=str(t/"tile_package_receipt.json"),tile_package_root=str(t),viewer_manifest=str(v/"viewer_manifest.json"),viewer_receipt=str(v/"viewer_receipt.json"),viewer_root=str(v),distribution_root=str(tmp_path/"dist"),target="dry-run",prefix="soil",remote_layout="immutable-versioned",public_base_url=None,distribution_id=None,allow_symlinks=False)
    rp,code=m.publish_distribution(args)
    assert rp.exists() and code==5

def test_stdout_only_receipt_path_on_success(tmp_path, capsys):
    r,t,v=mk(tmp_path)
    code=m.main(["--release-manifest",str(r/"release_manifest.json"),"--publish-receipt",str(r/"publish_receipt.json"),"--release-root",str(r),"--tile-package-manifest",str(t/"tile_package_manifest.json"),"--tile-package-receipt",str(t/"tile_package_receipt.json"),"--tile-package-root",str(t),"--viewer-manifest",str(v/"viewer_manifest.json"),"--viewer-receipt",str(v/"viewer_receipt.json"),"--viewer-root",str(v),"--distribution-root",str(tmp_path/"dist"),"--target","dry-run"])
    out=capsys.readouterr().out.strip(); assert out.endswith("distribution_receipt.json") and code==5
