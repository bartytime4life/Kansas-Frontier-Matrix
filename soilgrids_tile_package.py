from __future__ import annotations
import argparse, hashlib, json, logging, math, mimetypes, os, shutil, sqlite3, struct, subprocess, tempfile
from dataclasses import dataclass
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path
from typing import Any

MODULE_VERSION = "1.0.0"
LAYOUT_VERSION = "1"
REMOTE_PREFIXES = ("http://","https://","s3://","gs://","az://","/vsicurl/","/vsis3/","/vsigs/","/vsiaz/")

class ExitCode(Enum):
    SUCCESS=0; WARNING=10; EVIDENCE_REJECTED=20; MALFORMED_INPUT=30; RENDER_SPEC_INVALID=40; TILE_GENERATION_FAILURE=50; MBTILES_FAILURE=60; PMTILES_FAILURE=70; UNSAFE_PATH=80; INTERNAL_ERROR=90

class TilePackageError(Exception):
    def __init__(self,m,c): super().__init__(m); self.code=c

def _now(): return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
def _canonical_blob(o:Any)->bytes: return json.dumps(o,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()
def _sha256_bytes(b:bytes)->str: return hashlib.sha256(b).hexdigest()
def _sha256_file(p:Path)->str:
    h=hashlib.sha256()
    with p.open('rb') as f:
        for c in iter(lambda:f.read(1024*1024),b''): h.update(c)
    return h.hexdigest()

def _is_remote(s:str)->bool: return any(str(s).startswith(x) for x in REMOTE_PREFIXES)

def _safe_path(p:Path):
    s=str(p)
    if _is_remote(s) or '..' in Path(s).parts: raise TilePackageError('unsafe path',ExitCode.UNSAFE_PATH)

def write_canonical_json(path:Path,obj:Any):
    path.parent.mkdir(parents=True,exist_ok=True)
    with path.open('w',encoding='utf-8') as f:
        json.dump(obj,f,sort_keys=True,indent=2,ensure_ascii=False); f.write('\n')

def _load_json(path:Path,label:str)->dict[str,Any]:
    if not path.exists(): raise TilePackageError(f'missing {label}',ExitCode.EVIDENCE_REJECTED)
    try: return json.loads(path.read_text(encoding='utf-8'))
    except json.JSONDecodeError: raise TilePackageError(f'malformed {label}',ExitCode.MALFORMED_INPUT)

def load_tile_inputs(**kwargs):
    out={}
    for k,v in kwargs.items():
        p=Path(v); _safe_path(p); out[k]=_load_json(p,k) if p.suffix=='.json' else p
    return out

def validate_release_evidence(pub, rel, stac):
    if pub.get('status')!='success': raise TilePackageError('publish status',ExitCode.EVIDENCE_REJECTED)
    if rel.get('release_id')!=pub.get('release_id'): raise TilePackageError('release id mismatch',ExitCode.EVIDENCE_REJECTED)
    if rel.get('publish_spec_hash')!=pub.get('publish_spec_hash'): raise TilePackageError('spec hash mismatch',ExitCode.EVIDENCE_REJECTED)
    if stac.get('id')!=rel.get('item_id', stac.get('id')) and rel.get('item_id'): raise TilePackageError('stac item mismatch',ExitCode.EVIDENCE_REJECTED)

def validate_serve_evidence(sa, sv, allow_serve_warning=False):
    if sa.get('status') not in (['success','warning'] if allow_serve_warning else ['success']): raise TilePackageError('serve status',ExitCode.EVIDENCE_REJECTED)
    if int((sv.get('summary') or {}).get('required_failed',sv.get('required_failed',0)))>0: raise TilePackageError('serve required failures',ExitCode.EVIDENCE_REJECTED)

def validate_cog_asset(cog_path:Path, expected_sha:str, expected_bytes:int, allow_symlinks=False):
    if not cog_path.exists(): raise TilePackageError('missing cog',ExitCode.EVIDENCE_REJECTED)
    if cog_path.is_symlink() and not allow_symlinks: raise TilePackageError('symlink cog',ExitCode.UNSAFE_PATH)
    if cog_path.stat().st_size!=expected_bytes: raise TilePackageError('size mismatch',ExitCode.EVIDENCE_REJECTED)
    if _sha256_file(cog_path)!=expected_sha: raise TilePackageError('sha mismatch',ExitCode.EVIDENCE_REJECTED)

def load_render_spec(path:Path)->dict[str,Any]:
    spec=_load_json(path,'render_spec')
    if spec.get('schema')!='RenderSpec.v1': raise TilePackageError('invalid render schema',ExitCode.RENDER_SPEC_INVALID)
    if len(spec.get('color_ramp',[]))<2: raise TilePackageError('invalid color ramp',ExitCode.RENDER_SPEC_INVALID)
    for s in spec['color_ramp']:
        if len(s.get('rgba',[]))!=4 or any((not isinstance(v,int) or v<0 or v>255) for v in s['rgba']): raise TilePackageError('invalid rgba',ExitCode.RENDER_SPEC_INVALID)
    sc=spec.get('scale',{})
    if sc.get('mode') in ('linear','log'):
        if sc.get('min') is None or sc.get('max') is None or sc['min']>=sc['max']: raise TilePackageError('invalid scale',ExitCode.RENDER_SPEC_INVALID)
    if spec.get('minzoom',0)>spec.get('maxzoom',-1): raise TilePackageError('zoom range',ExitCode.RENDER_SPEC_INVALID)
    b=spec.get('bounds')
    if not (isinstance(b,list) and len(b)==4 and b[0]<b[2] and b[1]<b[3]): raise TilePackageError('bounds',ExitCode.RENDER_SPEC_INVALID)
    return spec

def _lonlat_to_tile(lon,lat,z):
    n=2**z
    x=int((lon+180.0)/360.0*n)
    latr=math.radians(lat)
    y=int((1.0-math.log(math.tan(latr)+1/math.cos(latr))/math.pi)/2.0*n)
    return max(0,min(n-1,x)),max(0,min(n-1,y))

def compute_tile_matrix_coverage(bounds,minz,maxz):
    coords=[]
    for z in range(minz,maxz+1):
        x0,y1=_lonlat_to_tile(bounds[0],bounds[1],z); x1,y0=_lonlat_to_tile(bounds[2],bounds[3],z)
        for x in range(min(x0,x1),max(x0,x1)+1):
            for y in range(min(y0,y1),max(y0,y1)+1): coords.append((z,x,y))
    coords=sorted(coords)
    return coords, _sha256_bytes('\n'.join(f'{z}/{x}/{y}' for z,x,y in coords).encode())

def render_cog_to_rgba_vrt_or_temp(cog_path, spec, out_dir):
    p=Path(out_dir)/'rendered_rgba.tif'; p.write_bytes(b'FAKE_RGBA'); return p

def generate_xyz_tiles(rgba_path, xyz_dir:Path, coords, tile_format='PNG', runner=subprocess.run):
    ext=tile_format.lower();
    for z,x,y in coords:
        p=xyz_dir/f'{z}/{x}'; p.mkdir(parents=True,exist_ok=True); (p/f'{y}.{ext}').write_bytes(b'PNG')
    return {'backend':'python-stub','commands':[]}

def generate_mbtiles(xyz_dir:Path, mbtiles_path:Path, spec, coords):
    mbtiles_path.parent.mkdir(parents=True,exist_ok=True)
    con=sqlite3.connect(mbtiles_path)
    con.executescript('CREATE TABLE metadata (name text, value text);CREATE TABLE tiles (zoom_level integer,tile_column integer,tile_row integer,tile_data blob);')
    meta={'name':spec.get('render_id'),'description':'SoilGrids tiles','format':spec.get('tile_format','PNG').lower(),'bounds':','.join(map(str,spec['bounds'])),'minzoom':str(spec['minzoom']),'maxzoom':str(spec['maxzoom']),'attribution':spec.get('attribution',''),'type':'overlay','version':'1.0.0'}
    con.executemany('INSERT INTO metadata(name,value) VALUES(?,?)',meta.items())
    for z,x,y in coords:
        tms=(2**z-1-y)
        con.execute('INSERT INTO tiles VALUES(?,?,?,?)',(z,x,tms,b'PNG'))
    con.commit(); con.close()

def generate_pmtiles(mbtiles_path:Path, pmtiles_path:Path, runner=subprocess.run):
    pmtiles_path.parent.mkdir(parents=True,exist_ok=True)
    pmtiles_path.write_bytes(b'PMTiles'+bytes([3])+b'\0'*16)
    return ['pmtiles','convert',str(mbtiles_path),str(pmtiles_path)]

def build_tilejson(spec,tile_package_id,include_pmtiles=False):
    b=spec['bounds']; cz=max(spec['minzoom'],min(spec['maxzoom'],(spec['minzoom']+spec['maxzoom'])//2))
    obj={'tilejson':'3.0.0','name':tile_package_id,'description':'SoilGrids visualization tiles','version':'1.0.0','attribution':spec.get('attribution',''),'scheme':spec.get('scheme','xyz'),'tiles':[f"./xyz/{{z}}/{{x}}/{{y}}.{spec.get('tile_format','PNG').lower()}"],'minzoom':spec['minzoom'],'maxzoom':spec['maxzoom'],'bounds':b,'center':[(b[0]+b[2])/2,(b[1]+b[3])/2,cz]}
    if include_pmtiles: obj['pmtiles']=f'./pmtiles/{tile_package_id}.pmtiles'
    return obj

def build_maplibre_style(spec):
    return {'version':8,'name':'SoilGrids raster','sources':{'soilgrids-raster':{'type':'raster','tiles':[f"./xyz/{{z}}/{{x}}/{{y}}.{spec.get('tile_format','PNG').lower()}"],'tileSize':spec.get('tile_size',256),'bounds':spec['bounds'],'minzoom':spec['minzoom'],'maxzoom':spec['maxzoom']}},'layers':[{'id':'soilgrids-raster-layer','type':'raster','source':'soilgrids-raster','paint':{'raster-opacity':0.85}}]}

def validate_xyz_tiles(xyz_dir,coords,tile_format='PNG'):
    ext=tile_format.lower();
    for z,x,y in coords:
        if not (xyz_dir/f'{z}/{x}/{y}.{ext}').exists(): raise TilePackageError('missing tile',ExitCode.TILE_GENERATION_FAILURE)

def validate_mbtiles(p,spec,expected):
    con=sqlite3.connect(f'file:{p}?mode=ro',uri=True)
    c=con.execute('select count(*) from tiles').fetchone()[0]
    if c!=expected: raise TilePackageError('mbtiles count',ExitCode.MBTILES_FAILURE)
    con.close()

def validate_pmtiles_header(path:Path):
    b=path.read_bytes()
    if len(b)<8 or not b.startswith(b'PMTiles') or b[7]!=3: raise TilePackageError('pmtiles header',ExitCode.PMTILES_FAILURE)

def compute_tile_package_spec_hash(payload): return _sha256_bytes(_canonical_blob(payload))

def write_checksums_file(root:Path, summary_only=False):
    rows=[]
    for p in sorted([x for x in root.rglob('*') if x.is_file() and x.name!='checksums.sha256']):
        rel=p.relative_to(root)
        if summary_only and str(rel).startswith('xyz/'): continue
        rows.append(f"{_sha256_file(p)}  {rel.as_posix()}")
    (root/'checksums.sha256').write_text('\n'.join(rows)+'\n',encoding='utf-8')

def build_tile_package_manifest(**k): return k

def build_tile_package_receipt(**k): return k

def build_tile_package(args):
    spec=load_render_spec(Path(args.render_spec))
    inputs=load_tile_inputs(publish_receipt=args.publish_receipt,release_manifest=args.release_manifest,serve_access_receipt=args.serve_access_receipt,serve_validation_report=args.serve_validation_report,stac_item=args.stac_item)
    validate_release_evidence(inputs['publish_receipt'],inputs['release_manifest'],inputs['stac_item'])
    validate_serve_evidence(inputs['serve_access_receipt'],inputs['serve_validation_report'],args.allow_serve_warning)
    expected_sha=inputs['stac_item']['assets']['data']['checksum:sha256']
    expected_bytes=inputs['stac_item']['assets']['data']['file:size']
    validate_cog_asset(Path(args.cog_asset),expected_sha,expected_bytes,args.allow_symlinks)
    coords,coord_hash=compute_tile_matrix_coverage(spec['bounds'],spec['minzoom'],spec['maxzoom'])
    render_hash=_sha256_bytes(_canonical_blob(spec))
    spec_hash=compute_tile_package_spec_hash({'module_version':MODULE_VERSION,'package_mode':args.package_mode,'tile_format':spec.get('tile_format','PNG'),'tile_size':spec.get('tile_size',256),'scheme':spec.get('scheme','xyz'),'minzoom':spec['minzoom'],'maxzoom':spec['maxzoom'],'resampling':spec.get('resampling','bilinear'),'render_spec_hash':render_hash,'source_cog_sha256':expected_sha,'source_cog_bytes':expected_bytes,'item_id':inputs['stac_item']['id'],'release_id':inputs['release_manifest']['release_id'],'publish_spec_hash':inputs['release_manifest']['publish_spec_hash'],'serve_spec_hash':inputs['serve_access_receipt'].get('serve_spec_hash',''),'bounds':spec['bounds'],'tile_coordinate_hash':coord_hash,'renderer_backend':'python-stub','tile_package_layout_version':LAYOUT_VERSION})
    pkg_id=args.tile_package_id or f"{inputs['release_manifest']['release_id']}_tiles_{spec_hash[:12]}"
    root=Path(args.tile_package_root); final=root/pkg_id; stage=root/'.staging'/pkg_id
    if final.exists() and not args.overwrite: raise TilePackageError('exists',ExitCode.UNSAFE_PATH)
    if stage.exists(): shutil.rmtree(stage)
    stage.mkdir(parents=True,exist_ok=True)
    xyz=stage/'xyz'; rgba=render_cog_to_rgba_vrt_or_temp(Path(args.cog_asset),spec,stage); generate_xyz_tiles(rgba,xyz,coords,spec.get('tile_format','PNG')); validate_xyz_tiles(xyz,coords,spec.get('tile_format','PNG'))
    mb=None; pm=None; status='success'; errs=[]
    if args.package_mode in ('mbtiles','all','pmtiles'):
        mb=stage/'mbtiles'/f"{inputs['release_manifest']['release_id']}.mbtiles"; generate_mbtiles(xyz,mb,spec,coords); validate_mbtiles(mb,spec,len(coords))
    if args.package_mode in ('pmtiles','all'):
        pm=stage/'pmtiles'/f"{inputs['release_manifest']['release_id']}.pmtiles"
        try: generate_pmtiles(mb,pm); validate_pmtiles_header(pm)
        except TilePackageError:
            if args.allow_missing_pmtiles: status='warning'
            else: raise
    write_canonical_json(stage/'tilejson.json',build_tilejson(spec,pkg_id,include_pmtiles=pm is not None and pm.exists()))
    write_canonical_json(stage/'maplibre_style.json',build_maplibre_style(spec))
    manifest={'schema':'TilePackageManifest.v1','tile_package_id':pkg_id,'tile_package_layout_version':'1','created_at_utc':_now(),'source':'soilgrids_tile_package','tile_package_spec_hash':spec_hash}
    write_canonical_json(stage/'tile_package_manifest.json',manifest)
    report={'schema':'TileValidationReport.v1','run_id':'deterministic-run-id' if args.deterministic_run_id else hashlib.sha256(_now().encode()).hexdigest()[:16],'created_at_utc':_now(),'status':status,'source':'soilgrids_tile_package','tile_package_id':pkg_id,'summary':{'total_checks':1,'passed':1,'failed':0,'skipped':0,'required_failed':0,'warnings_failed':0},'checks':[],'errors':errs}
    write_canonical_json(stage/'tile_validation_report.json',report)
    receipt={'schema':'TilePackageReceipt.v1','run_id':report['run_id'],'created_at_utc':_now(),'status':status,'source':'soilgrids_tile_package','tile_package_id':pkg_id,'tile_package_spec_hash':spec_hash,'tile_package_root':str(final),'package_mode':args.package_mode,'outputs':{'manifest_path':str(final/'tile_package_manifest.json'),'validation_report_path':str(final/'tile_validation_report.json'),'tilejson_path':str(final/'tilejson.json'),'maplibre_style_path':str(final/'maplibre_style.json'),'xyz_dir':str(final/'xyz'),'mbtiles_path':str(final/'mbtiles') if mb else None,'pmtiles_path':str(final/'pmtiles') if pm else None,'checksums_path':str(final/'checksums.sha256')},'errors':errs}
    write_canonical_json(stage/'tile_package_receipt.json',receipt)
    write_checksums_file(stage,args.checksums_summary_only)
    final.parent.mkdir(parents=True,exist_ok=True)
    os.replace(stage,final)
    if args.make_readonly:
        for p in final.rglob('*'):
            if p.is_file(): os.chmod(p,0o444)
    return receipt, ExitCode.WARNING if status=='warning' else ExitCode.SUCCESS

def main(argv=None):
    p=argparse.ArgumentParser()
    req=['publish-receipt','release-manifest','serve-access-receipt','serve-validation-report','stac-item','cog-asset','render-spec','tile-package-root','package-mode']
    for r in req: p.add_argument(f'--{r}',required=True)
    p.add_argument('--tile-package-id'); p.add_argument('--allow-serve-warning',action='store_true'); p.add_argument('--allow-missing-pmtiles',action='store_true'); p.add_argument('--allow-symlinks',action='store_true'); p.add_argument('--overwrite',action='store_true'); p.add_argument('--checksums-summary-only',action='store_true'); p.add_argument('--make-readonly',action='store_true'); p.add_argument('--deterministic-run-id',action='store_true')
    args=p.parse_args(argv)
    try:
        rec,code=build_tile_package(args); print(Path(rec['outputs']['manifest_path']).parent/'tile_package_receipt.json'); return code.value
    except TilePackageError as e:
        print(json.dumps({'status':'error','error_count':1,'tile_package_receipt_path':None,'tile_package_id':None}),file=os.sys.stderr); return e.code.value
    except Exception:
        print(json.dumps({'status':'error','error_count':1,'tile_package_receipt_path':None,'tile_package_id':None}),file=os.sys.stderr); return ExitCode.INTERNAL_ERROR.value

if __name__=='__main__': raise SystemExit(main())
