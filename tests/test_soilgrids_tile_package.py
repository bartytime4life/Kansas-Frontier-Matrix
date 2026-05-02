import json, hashlib
from pathlib import Path
import pytest
import soilgrids_tile_package as m


def _w(p,obj): p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(obj),encoding='utf-8')

@pytest.fixture
def fx(tmp_path):
    cog=tmp_path/'a.tif'; cog.write_bytes(b'abc')
    sha=hashlib.sha256(b'abc').hexdigest()
    pub={'schema':'PublishReceipt.v1','status':'success','release_id':'r1','publish_spec_hash':'p1'}
    rel={'schema':'ReleaseManifest.v1','release_id':'r1','publish_spec_hash':'p1'}
    sa={'schema':'ServeAccessReceipt.v1','status':'success','serve_spec_hash':'s1'}
    sv={'schema':'ServeValidationReport.v1','required_failed':0}
    st={'id':'item1','assets':{'data':{'checksum:sha256':sha,'file:size':3}}}
    rs={'schema':'RenderSpec.v1','render_id':'x','scale':{'mode':'linear','min':0,'max':1},'color_ramp':[{'value':0,'rgba':[0,0,0,255]},{'value':1,'rgba':[255,255,255,255]}],'minzoom':6,'maxzoom':6,'bounds':[-98,37,-97.9,37.1],'tile_format':'PNG','tile_size':256,'scheme':'xyz'}
    for n,o in [('publish_receipt.json',pub),('release_manifest.json',rel),('serve_access_receipt.json',sa),('serve_validation_report.json',sv),('stac_item.json',st),('render_spec.json',rs)]: _w(tmp_path/n,o)
    return tmp_path, cog

def _args(base,cog):
    class A: pass
    a=A(); a.publish_receipt=str(base/'publish_receipt.json'); a.release_manifest=str(base/'release_manifest.json'); a.serve_access_receipt=str(base/'serve_access_receipt.json'); a.serve_validation_report=str(base/'serve_validation_report.json'); a.stac_item=str(base/'stac_item.json'); a.cog_asset=str(cog); a.render_spec=str(base/'render_spec.json'); a.tile_package_root=str(base/'tiles'); a.package_mode='all'; a.tile_package_id=None; a.allow_serve_warning=False; a.allow_missing_pmtiles=False; a.allow_symlinks=False; a.overwrite=False; a.checksums_summary_only=False; a.make_readonly=False; a.deterministic_run_id=True
    return a

def test_receipt_written_on_success(fx):
    base,cog=fx; rec,code=m.build_tile_package(_args(base,cog)); assert code==m.ExitCode.SUCCESS; assert Path(rec['outputs']['manifest_path']).parent.joinpath('tile_package_receipt.json').exists()

def test_rejects_failed_publish_receipt(fx):
    base,cog=fx; d=json.loads((base/'publish_receipt.json').read_text()); d['status']='error'; _w(base/'publish_receipt.json',d)
    with pytest.raises(m.TilePackageError): m.build_tile_package(_args(base,cog))

def test_rejects_cog_checksum_mismatch(fx):
    base,cog=fx; d=json.loads((base/'stac_item.json').read_text()); d['assets']['data']['checksum:sha256']='0'*64; _w(base/'stac_item.json',d)
    with pytest.raises(m.TilePackageError): m.build_tile_package(_args(base,cog))

def test_tile_package_spec_hash_stable():
    p={'a':1,'b':2}; assert m.compute_tile_package_spec_hash(p)==m.compute_tile_package_spec_hash({'b':2,'a':1})

def test_pmtiles_header_magic_valid(tmp_path):
    p=tmp_path/'a.pmtiles'; p.write_bytes(b'PMTiles'+bytes([3])+b'0'*10); m.validate_pmtiles_header(p)

def test_pmtiles_version_is_3(tmp_path):
    p=tmp_path/'a.pmtiles'; p.write_bytes(b'PMTiles'+bytes([2])+b'0'*10)
    with pytest.raises(m.TilePackageError): m.validate_pmtiles_header(p)
