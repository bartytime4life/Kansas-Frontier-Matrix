from pathlib import Path
import json
import soilgrids_cog_normalize as m


def _fake_translate(inp: Path, outp: Path, opts: dict[str, str]):
    outp.write_bytes(inp.read_bytes() or b'x')


def _patch_open(monkeypatch):
    class Band:
        DataType = 1
        def __init__(self): self.nodata=None
        def GetNoDataValue(self): return self.nodata
        def Checksum(self): return 7
        def GetOverviewCount(self): return 1
        def GetBlockSize(self): return (512, 512)
    class Driver: ShortName = 'COG'
    class DS:
        RasterXSize=10; RasterYSize=10; RasterCount=1
        def GetGeoTransform(self): return (0,1,0,0,0,-1)
        def GetProjectionRef(self): return 'EPSG:4326'
        def GetRasterBand(self, i): return Band()
        def GetMetadata(self, domain=None): return {'LAYOUT':'COG'}
        def GetDriver(self): return Driver()
    monkeypatch.setattr(m, '_open_ds', lambda p: DS())


def test_rejects_missing_input(tmp_path):
    r = m.normalize_to_cog(tmp_path/'x.tif', tmp_path)
    assert r['status'] == 'error'

def test_rejects_remote_paths(tmp_path):
    r = m.normalize_to_cog('https://x.tif', tmp_path)
    assert r['status'] == 'error'

def test_rejects_empty_input(tmp_path):
    inp = tmp_path/'e.tif'; inp.write_bytes(b'')
    r = m.normalize_to_cog(inp, tmp_path)
    assert r['status'] == 'error'

def test_canonical_creation_options_stable():
    a = m.canonical_creation_options('deflate',2,512,'if_safer',1)
    b = m.canonical_creation_options('DEFLATE','2','512','IF_SAFER','1')
    assert a == b

def test_spec_hash_stable(tmp_path):
    inp = tmp_path/'a.tif'; inp.write_bytes(b'abc')
    opts = m.canonical_creation_options('DEFLATE',2,512,'IF_SAFER',1)
    h1 = m.compute_spec_hash(inp, m.sha256_file(inp), opts, None)
    h2 = m.compute_spec_hash(inp, m.sha256_file(inp), opts, None)
    assert h1 == h2

def test_output_filename_contains_spec_hash(tmp_path, monkeypatch):
    _patch_open(monkeypatch)
    inp = tmp_path/'a.tif'; inp.write_bytes(b'abc')
    r = m.normalize_to_cog(inp, tmp_path, translate_runner=_fake_translate)
    assert r['status']=='success'
    assert r['spec_hash'][:12] in Path(r['output_path']).name

def test_receipt_written_on_success(tmp_path, monkeypatch):
    _patch_open(monkeypatch)
    inp = tmp_path/'a.tif'; inp.write_bytes(b'abc')
    r = m.normalize_to_cog(inp, tmp_path, translate_runner=_fake_translate)
    rp = tmp_path / f"cog_receipt_{r['run_id']}.json"
    assert rp.exists()

def test_receipt_written_on_failure(tmp_path):
    r = m.normalize_to_cog(tmp_path/'none.tif', tmp_path)
    rp = tmp_path / f"cog_receipt_{r['run_id']}.json"
    assert rp.exists()

def test_no_overwrite_without_flag(tmp_path, monkeypatch):
    _patch_open(monkeypatch)
    inp = tmp_path/'a.tif'; inp.write_bytes(b'abc')
    r1 = m.normalize_to_cog(inp, tmp_path, translate_runner=_fake_translate)
    r2 = m.normalize_to_cog(inp, tmp_path, translate_runner=_fake_translate)
    assert r1['status']=='success'
    assert r2['status']=='error'

def test_atomic_write_no_partial_final_on_failure(tmp_path, monkeypatch):
    _patch_open(monkeypatch)
    inp = tmp_path/'a.tif'; inp.write_bytes(b'abc')
    def bad(i,o,opts):
        o.write_bytes(b'partial')
        raise RuntimeError('fail')
    r = m.normalize_to_cog(inp, tmp_path, translate_runner=bad)
    assert r['status']=='error'
    assert not list(tmp_path.glob('*_cog_*.tif'))

def test_mock_gdal_runner_called_with_expected_options(tmp_path, monkeypatch):
    _patch_open(monkeypatch)
    inp = tmp_path/'a.tif'; inp.write_bytes(b'abc')
    seen = {}
    def runner(i,o,opts):
        seen.update(opts)
        o.write_bytes(b'abc')
    m.normalize_to_cog(inp, tmp_path, translate_runner=runner)
    assert seen['NUM_THREADS'] == '1'
    assert seen['COMPRESS'] == 'DEFLATE'

def test_semantic_raster_hash_stable_for_fixture(tmp_path, monkeypatch):
    _patch_open(monkeypatch)
    sem = m._raster_semantics(m._open_ds(tmp_path/'x'))
    assert m.compute_semantic_raster_hash(sem) == m.compute_semantic_raster_hash(sem)
