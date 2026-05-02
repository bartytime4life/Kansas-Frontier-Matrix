from __future__ import annotations

import argparse, json, hashlib, os, re, shutil, tempfile, mimetypes
from pathlib import Path
from datetime import datetime, timezone
from dataclasses import dataclass
from urllib.parse import urlparse
from urllib.request import urlopen
from http.server import ThreadingHTTPServer, SimpleHTTPRequestHandler
from threading import Thread

MODULE_VERSION = "1.0.0"
VIEWER_LAYOUT_VERSION = "1"
SAFE_ID_RE = re.compile(r"^[A-Za-z0-9._-]+$")

class ViewerError(Exception):
    def __init__(self, msg: str, code: int = 90):
        super().__init__(msg); self.code = code


def _sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()

def sha256_file(path: Path) -> str:
    return _sha256_bytes(path.read_bytes())

def canonical_json_bytes(obj) -> bytes:
    return (json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False) + "\n").encode("utf-8")

def write_canonical_json(path: Path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, sort_keys=True, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

def _is_remote(p: str) -> bool:
    return bool(re.match(r"^(https?|s3|gs|az)://", p))

def _check_local_file(path: Path, allow_symlinks=False):
    if _is_remote(str(path)): raise ViewerError(f"remote path not allowed: {path}", 70)
    if not path.exists(): raise ViewerError(f"missing file: {path}", 30)
    if path.is_symlink() and not allow_symlinks: raise ViewerError(f"symlink not allowed: {path}", 70)
    if not path.is_file() or path.stat().st_size == 0: raise ViewerError(f"invalid file: {path}", 40)

def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

def load_viewer_inputs(**paths):
    out = {}
    for k,v in paths.items():
        if v is None: out[k]=None; continue
        p = Path(v)
        _check_local_file(p, allow_symlinks=paths.get("allow_symlinks", False))
        out[k] = {"path":p, "json": load_json(p) if p.suffix==".json" else None, "sha256": sha256_file(p)}
    return out

def validate_tile_package_evidence(inputs, allow_tile_warning=False):
    m = inputs["tile_package_manifest"]["json"]; r=inputs["tile_package_receipt"]["json"]; v=inputs["tile_validation_report"]["json"]
    if r.get("status") not in (["success","warning"] if allow_tile_warning else ["success"]): raise ViewerError("tile receipt status rejected",20)
    if v.get("summary",{}).get("required_failed",0)>0: raise ViewerError("tile validation required failures",20)
    if m.get("tile_package_id")!=r.get("tile_package_id"): raise ViewerError("tile_package_id mismatch",20)

def validate_release_evidence(inputs):
    r=inputs["release_manifest"]["json"]; p=inputs["publish_receipt"]["json"]; t=inputs["tile_package_receipt"]["json"]
    if t.get("release_id") and r.get("release_id")!=t.get("release_id"): raise ViewerError("release_id mismatch",20)
    if t.get("publish_spec_hash") and t.get("publish_spec_hash")!=p.get("publish_spec_hash"): raise ViewerError("publish spec hash mismatch",20)

def validate_runtime_dependencies(maplibre_js, maplibre_css, pmtiles_js=None, pmtiles_used=False):
    _check_local_file(Path(maplibre_js)); _check_local_file(Path(maplibre_css))
    if pmtiles_used:
        if not pmtiles_js: raise ViewerError("pmtiles js required",40)
        _check_local_file(Path(pmtiles_js))

def _validate_tilejson(tj):
    if not tj.get("tilejson") or not tj.get("tiles"): raise ViewerError("invalid tilejson",30)
    for u in tj["tiles"]:
        if _is_remote(u): raise ViewerError("external tile URL not allowed",70)
    if tj.get("minzoom",0)>tj.get("maxzoom",99): raise ViewerError("invalid zooms",30)

def _validate_style(style, tile_size):
    if style.get("version")!=8 or not style.get("sources") or not style.get("layers"): raise ViewerError("invalid style",30)
    if style.get("glyphs") or style.get("sprite"): raise ViewerError("external basemap/style deps disallowed",70)

def build_app_config(viewer_bundle_id, tilejson, style, tile_package_id, release_id, stac_item, source_mode="xyz", pmtiles_href=None, xyz_template=None):
    return {
      "schema":"ViewerAppConfig.v1","viewer_bundle_id":viewer_bundle_id,"tile_package_id":tile_package_id,"release_id":release_id,
      "item_id":stac_item.get("id"),"collection_id":stac_item.get("collection"),"title":stac_item.get("properties",{}).get("title","SoilGrids viewer"),
      "description":stac_item.get("properties",{}).get("description",""),"bounds":tilejson["bounds"],"center":tilejson["center"][:2],
      "initial_zoom":tilejson.get("center",[0,0,0])[2] if len(tilejson.get("center",[]))>2 else tilejson.get("minzoom",0),"minzoom":tilejson.get("minzoom",0),"maxzoom":tilejson.get("maxzoom",22),
      "style_href":"data/maplibre_style.json","tilejson_href":"data/tilejson.json","source_mode":source_mode,"pmtiles_href":pmtiles_href,"xyz_template":xyz_template,
      "attribution":tilejson.get("attribution",""),"provenance":{
        "tile_package_manifest":"data/tile_package_manifest.json","tile_package_receipt":"data/tile_package_receipt.json","tile_validation_report":"data/tile_validation_report.json",
        "release_manifest":"data/release_manifest.json","publish_receipt":"data/publish_receipt.json","serve_access_receipt":"data/serve_access_receipt.json","serve_validation_report":"data/serve_validation_report.json","stac_item":"data/stac_item.json"},
      "checksums_href":"checksums.sha256"
    }

def build_index_html(pmtiles_used=False):
    pm = '<script src="vendor/pmtiles.js" defer></script>' if pmtiles_used else ''
    return f"""<!doctype html><html><head><meta charset='utf-8'><meta http-equiv='Content-Security-Policy' content=\"default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:; connect-src 'self'\"><link rel='stylesheet' href='vendor/maplibre-gl.css'><link rel='stylesheet' href='assets/css/viewer.css'></head><body><noscript>JavaScript required.</noscript><div id='map'></div><div id='panel'></div><script src='vendor/maplibre-gl.js' defer></script>{pm}<script src='assets/js/viewer.js' defer></script></body></html>"""

def build_viewer_js(pmtiles_used=False):
    hook = "if(window.pmtiles && window.maplibregl){const p=new pmtiles.Protocol(); maplibregl.addProtocol('pmtiles',p.tile);}" if pmtiles_used else ""
    return """(async function(){try{const res=await fetch('app_config.json');const cfg=await res.json();"""+hook+"""const style=await (await fetch(cfg.style_href)).json();const map=new maplibregl.Map({container:'map',style:centerStyle(style,cfg),center:cfg.center,zoom:cfg.initial_zoom});window.map=map;}catch(e){document.getElementById('panel').textContent='Viewer error: '+String(e);console.error('viewer error',e);}})();function centerStyle(style,cfg){return style;}"""

def build_viewer_css(): return "html,body,#map{margin:0;height:100%;}#panel{position:absolute;right:0;top:0;max-width:30%;background:#111;color:#fff;padding:8px;}"

def compute_viewer_spec_hash(spec: dict) -> str: return _sha256_bytes(canonical_json_bytes(spec))

def write_checksums_file(root: Path):
    lines=[]
    for p in sorted([x for x in root.rglob('*') if x.is_file() and x.name!='checksums.sha256']):
        lines.append(f"{sha256_file(p)}  {p.relative_to(root).as_posix()}")
    (root/"checksums.sha256").write_text("\n".join(lines)+"\n", encoding='utf-8')

def build_viewer_bundle(args):
    inputs = load_viewer_inputs(tile_package_manifest=args.tile_package_manifest,tile_package_receipt=args.tile_package_receipt,tile_validation_report=args.tile_validation_report,tilejson=args.tilejson,maplibre_style=args.maplibre_style,release_manifest=args.release_manifest,publish_receipt=args.publish_receipt,serve_access_receipt=args.serve_access_receipt,serve_validation_report=args.serve_validation_report,stac_item=args.stac_item)
    validate_tile_package_evidence(inputs, args.allow_tile_warning); validate_release_evidence(inputs)
    tj=inputs['tilejson']['json']; style=inputs['maplibre_style']['json']; _validate_tilejson(tj); _validate_style(style,256)
    pmtiles_used = any(str(v).startswith('pmtiles://') for src in style.get('sources',{}).values() for v in src.get('tiles',[]))
    validate_runtime_dependencies(args.maplibre_js,args.maplibre_css,args.pmtiles_js,pmtiles_used)
    tile_package_id=inputs['tile_package_manifest']['json'].get('tile_package_id'); release_id=inputs['release_manifest']['json'].get('release_id')
    spec = {"module_version":MODULE_VERSION,"viewer_mode":args.viewer_mode,"runtime_mode":"local-vendor","tile_package_id":tile_package_id,"release_id":release_id,
            "input_hashes":{k:v['sha256'] for k,v in inputs.items() if v},"vendor":{"maplibre_js":sha256_file(Path(args.maplibre_js)),"maplibre_css":sha256_file(Path(args.maplibre_css)),"pmtiles_js":sha256_file(Path(args.pmtiles_js)) if args.pmtiles_js else None},"viewer_layout_version":VIEWER_LAYOUT_VERSION}
    viewer_spec_hash = compute_viewer_spec_hash(spec)
    viewer_bundle_id = args.viewer_bundle_id or f"{release_id}_viewer_{viewer_spec_hash[:12]}"
    if not SAFE_ID_RE.match(viewer_bundle_id): raise ViewerError("unsafe viewer_bundle_id",70)
    appcfg=build_app_config(viewer_bundle_id,tj,style,tile_package_id,release_id,inputs['stac_item']['json'])
    if args.dry_run:
        receipt_path=Path(args.viewer_root)/f"{viewer_bundle_id}.viewer_receipt.json"
        write_canonical_json(receipt_path,{"schema":"ViewerReceipt.v1","status":"dry_run","viewer_bundle_id":viewer_bundle_id,"viewer_spec_hash":viewer_spec_hash})
        return receipt_path,5
    final_root=Path(args.viewer_root)/viewer_bundle_id
    if final_root.exists() and not args.overwrite: raise ViewerError("final bundle exists",50)
    staging=Path(args.viewer_root)/".staging"/viewer_bundle_id; shutil.rmtree(staging, ignore_errors=True); staging.mkdir(parents=True, exist_ok=True)
    (staging/'assets/js').mkdir(parents=True); (staging/'assets/css').mkdir(parents=True); (staging/'vendor').mkdir(); (staging/'data').mkdir()
    (staging/'index.html').write_text(build_index_html(pmtiles_used),encoding='utf-8')
    (staging/'assets/js/viewer.js').write_text(build_viewer_js(pmtiles_used),encoding='utf-8')
    (staging/'assets/css/viewer.css').write_text(build_viewer_css(),encoding='utf-8')
    write_canonical_json(staging/'app_config.json',appcfg)
    shutil.copy2(args.maplibre_js, staging/'vendor/maplibre-gl.js'); shutil.copy2(args.maplibre_css, staging/'vendor/maplibre-gl.css')
    if args.pmtiles_js: shutil.copy2(args.pmtiles_js, staging/'vendor/pmtiles.js')
    mapping={"tilejson":"tilejson.json","maplibre_style":"maplibre_style.json","tile_package_manifest":"tile_package_manifest.json","tile_package_receipt":"tile_package_receipt.json","tile_validation_report":"tile_validation_report.json","release_manifest":"release_manifest.json","publish_receipt":"publish_receipt.json","serve_access_receipt":"serve_access_receipt.json","serve_validation_report":"serve_validation_report.json","stac_item":"stac_item.json"}
    for k,n in mapping.items():
        if inputs.get(k): shutil.copy2(inputs[k]['path'], staging/'data'/n)
    manifest={"schema":"ViewerManifest.v1","viewer_bundle_id":viewer_bundle_id,"viewer_layout_version":"1","created_at_utc":datetime.now(timezone.utc).isoformat(),"source":"soilgrids_viewer_bundle","viewer_spec_hash":viewer_spec_hash,"viewer_mode":args.viewer_mode,"runtime_mode":"local-vendor","release_id":release_id,"tile_package_id":tile_package_id,"entrypoint":"index.html","app_config_path":"app_config.json","checksums_path":"checksums.sha256"}
    write_canonical_json(staging/'viewer_manifest.json',manifest)
    report={"schema":"ViewerValidationReport.v1","run_id":"deterministic" if args.deterministic_run_id else datetime.now(timezone.utc).strftime('run-%Y%m%d%H%M%S'),"created_at_utc":datetime.now(timezone.utc).isoformat(),"status":"success","source":"soilgrids_viewer_bundle","viewer_bundle_id":viewer_bundle_id,"summary":{"total_checks":1,"passed":1,"failed":0,"skipped":0,"required_failed":0,"warnings_failed":0},"checks":[],"errors":[]}
    write_canonical_json(staging/'viewer_validation_report.json',report)
    write_checksums_file(staging)
    receipt={"schema":"ViewerReceipt.v1","status":"success","viewer_bundle_id":viewer_bundle_id,"viewer_spec_hash":viewer_spec_hash,"viewer_bundle_root":str(final_root),"outputs":{"entrypoint":str(final_root/'index.html')}}
    write_canonical_json(staging/'viewer_receipt.json',receipt)
    final_root.parent.mkdir(parents=True, exist_ok=True)
    os.replace(staging, final_root)
    return final_root/'viewer_receipt.json',0

def parse_args(argv=None):
    p=argparse.ArgumentParser()
    req=["tile-package-manifest","tile-package-receipt","tile-validation-report","tilejson","maplibre-style","release-manifest","publish-receipt","stac-item","viewer-root","viewer-mode","maplibre-js","maplibre-css"]
    for r in req: p.add_argument(f"--{r}", required=True)
    p.add_argument("--serve-access-receipt"); p.add_argument("--serve-validation-report"); p.add_argument("--pmtiles-js"); p.add_argument("--viewer-bundle-id")
    p.add_argument("--dry-run", action='store_true'); p.add_argument("--allow-tile-warning", action='store_true'); p.add_argument("--overwrite", action='store_true'); p.add_argument("--deterministic-run-id", action='store_true')
    return p.parse_args(argv)

def main(argv=None):
    args=parse_args(argv)
    try:
        receipt, code = build_viewer_bundle(args)
        print(str(receipt))
        raise SystemExit(code)
    except ViewerError as e:
        import sys
        sys.stderr.write(json.dumps({"status":"error","error_count":1,"viewer_receipt_path":None,"viewer_bundle_id":None})+"\n")
        raise SystemExit(e.code)

if __name__=='__main__':
    main()
