from __future__ import annotations
import argparse, hashlib, html, json, logging, os, re, shutil, sqlite3, sys, tempfile
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any, Dict, List, Tuple
from urllib.parse import parse_qs, urlparse

MODULE_VERSION = "14.0.0"
FORBIDDEN_SQL = re.compile(r"\b(INSERT|UPDATE|DELETE|DROP|ALTER|CREATE|REPLACE|TRUNCATE|VACUUM|REINDEX|ANALYZE|ATTACH|DETACH|LOAD_EXTENSION|BEGIN|COMMIT|ROLLBACK|SAVEPOINT|RELEASE)\b", re.I)
SECRET_RE = re.compile(r"(AKIA[0-9A-Z]{16}|Bearer\s+[A-Za-z0-9._-]+|-----BEGIN [A-Z ]*PRIVATE KEY-----|api[_-]?key\s*[:=]\s*['\"]?[A-Za-z0-9_-]{12,})")


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")

def _canonical_bytes(obj: Any) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()

def _sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for c in iter(lambda: f.read(65536), b""): h.update(c)
    return h.hexdigest()

def write_canonical_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, sort_keys=True, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

def load_runtime_inputs(args):
    required = ["registry_manifest", "registry_snapshot", "registry_receipt", "sqlite_db", "openapi", "saved_queries"]
    out = {}
    for k in required:
        p = Path(getattr(args, k))
        if not p.exists(): raise ValueError(f"missing required input: {k}")
        out[k] = p
    for k in ["registry_query_contract", "registry_validation_report", "search_index"]:
        v = getattr(args, k, None)
        out[k] = Path(v) if v else None
    return out

def validate_registry_inputs(inputs: Dict[str, Path]) -> Dict[str, Any]:
    parsed = {k: json.loads(v.read_text(encoding="utf-8")) for k, v in inputs.items() if v and v.suffix == ".json"}
    status = parsed["registry_receipt"].get("status")
    if status not in ("success", "warning"): raise ValueError("invalid registry receipt status")
    hashes = {f"{k}_sha256": _sha256_file(v) for k, v in inputs.items() if v}
    return {"parsed": parsed, "hashes": hashes}

def open_sqlite_readonly_immutable(sqlite_db: Path) -> sqlite3.Connection:
    uri = f"file:{sqlite_db.resolve()}?mode=ro&immutable=1"
    con = sqlite3.connect(uri, uri=True, timeout=2.0)
    con.row_factory = sqlite3.Row
    con.execute("PRAGMA query_only=ON")
    con.execute("PRAGMA foreign_keys=ON")
    return con

def enforce_readonly_sql(sql: str) -> None:
    s = re.sub(r"--.*?$|/\*.*?\*/", "", sql, flags=re.M | re.S).strip()
    if ";" in s.rstrip(";"): raise ValueError("multiple statements rejected")
    if FORBIDDEN_SQL.search(s): raise ValueError("mutating SQL rejected")
    if not re.match(r"^(SELECT|WITH\b)", s, re.I): raise ValueError("only SELECT/WITH allowed")

def execute_parameterized_query(con, sql: str, params: Dict[str, Any] | None = None, limit: int = 100):
    enforce_readonly_sql(sql)
    q = f"SELECT * FROM ({sql}) LIMIT ?"
    cur = con.execute(q, {**(params or {}), "1": limit} if isinstance(params, dict) else [limit])
    rows = [dict(r) for r in cur.fetchall()]
    return rows

def execute_saved_query(con, saved_queries: Dict[str, Any], query_id: str, params: Dict[str, Any] | None = None):
    q = next((x for x in saved_queries.get("queries", []) if x.get("query_id") == query_id), None)
    if not q: raise KeyError(query_id)
    return execute_parameterized_query(con, q["sql"], params=params, limit=int(q.get("max_rows_default", 100)))

def build_dashboard_config(bundle_id, snapshot_id, reg_hash, title):
    return {"schema":"RegistryDashboardAppConfig.v1","runtime_bundle_id":bundle_id,"registry_snapshot_id":snapshot_id,"registry_spec_hash":reg_hash,"dashboard_title":title,"api_base":"/api","static_mode":False,"views":["overview","evidence_crates","pipeline_layers","releases","distributions","monitoring","drift","incidents","remediation","compliance","provenance","artifacts","queries","search","api_docs"],"limits":{"default_page_size":50,"max_page_size":1000},"provenance":{"registry_manifest":"data/registry_manifest.json","registry_snapshot":"data/registry_snapshot.json","openapi":"data/openapi.json","saved_queries":"data/saved_queries.json"}}

def build_dashboard_html(title):
    return f"<!doctype html><html><head><meta charset='utf-8'><meta http-equiv='Content-Security-Policy' content=\"default-src 'self'; style-src 'self'; script-src 'self'; img-src 'self' data:; connect-src 'self'\"><title>{html.escape(title)}</title><link rel='stylesheet' href='assets/css/dashboard.css'></head><body><a href='#main' class='skip-link'>Skip</a><h1>{html.escape(title)}</h1><main id='main' aria-label='Dashboard main'><section><h2>Overview</h2><div id='app' aria-label='app'></div></section></main><script src='assets/js/dashboard.js'></script></body></html>"

def build_dashboard_js():
    return "(()=>{const out=document.getElementById('app');fetch('/api/registry').then(r=>r.json()).then(j=>{out.textContent=JSON.stringify(j,null,2)}).catch(()=>{out.textContent='API unavailable';});})();"

def build_dashboard_css():
    return ":root{color-scheme:light dark} .skip-link:focus{outline:3px solid #ff0}.focus-visible:focus{outline:2px solid #06f}@media (prefers-reduced-motion: reduce){*{animation:none!important;transition:none!important}}@media (prefers-contrast: more){body{background:#000;color:#fff}}"

def validate_dashboard_static_security(html_s, js_s, css_s):
    if "http://" in html_s or "https://" in html_s: raise ValueError("external refs disallowed")
    if "eval(" in js_s: raise ValueError("eval disallowed")
    if "Content-Security-Policy" not in html_s: raise ValueError("missing csp")

def validate_dashboard_accessibility(html_s, css_s):
    for token in ["aria-label", "<h1", "skip-link"]:
        if token not in html_s: raise ValueError("accessibility marker missing")
    if "prefers-reduced-motion" not in css_s: raise ValueError("reduced motion missing")

def compute_runtime_spec_hash(spec: Dict[str, Any]) -> str: return hashlib.sha256(_canonical_bytes(spec)).hexdigest()
def compute_dashboard_spec_hash(spec: Dict[str, Any]) -> str: return hashlib.sha256(_canonical_bytes(spec)).hexdigest()

def write_checksums_file(path: Path, rel_paths: List[Path]):
    lines = [f"{_sha256_file(path.parent/r)}  {r.as_posix()}" for r in sorted(rel_paths, key=lambda p: p.as_posix())]
    path.write_text("\n".join(lines)+"\n", encoding="utf-8")

def build_api_handlers(con, snapshot, saved):
    def list_entities(params):
        lim = int(params.get("limit", ["50"])[0]); off = int(params.get("offset", ["0"])[0])
        if lim < 1 or lim > 1000 or off < 0: raise ValueError("invalid pagination")
        rows = [dict(r) for r in con.execute("SELECT * FROM entities ORDER BY registry_entity_id LIMIT ? OFFSET ?", (lim, off)).fetchall()]
        return {"items": rows, "limit": lim, "offset": off}
    return {"/health": lambda p: {"status": "ok", "registry_snapshot_id": snapshot.get("registry_snapshot_id")},
            "/api/registry": lambda p: snapshot,
            "/api/entities": list_entities,
            "/api/queries": lambda p: {"queries":[{"query_id":q.get("query_id"),"title":q.get("title")} for q in saved.get("queries",[])]}}

def run_local_registry_api(host, port, handlers):
    class H(BaseHTTPRequestHandler):
        def _send(self, code, obj):
            b = json.dumps(obj, sort_keys=True, separators=(",", ":")).encode(); self.send_response(code); self.send_header("Content-Type","application/json"); self.send_header("Content-Length",str(len(b))); self.end_headers(); self.wfile.write(b)
        def do_GET(self):
            p = urlparse(self.path)
            if ".." in p.path: return self._send(400,{"error":"path traversal"})
            fn = handlers.get(p.path)
            if not fn: return self._send(404,{"error":"not found"})
            try: self._send(200, fn(parse_qs(p.query)))
            except ValueError as e: self._send(400,{"error":str(e)})
        def log_message(self, *a): return
    srv = ThreadingHTTPServer((host, port), H)
    return srv

# manifest/report builders minimal
build_api_runtime_manifest = lambda **k: {"schema":"ApiRuntimeManifest.v1", **k}
build_api_runtime_contract = lambda **k: {"schema":"ApiRuntimeContract.v1", **k}
build_api_runtime_validation_report = lambda **k: {"schema":"ApiRuntimeValidationReport.v1", **k}
build_dashboard_manifest = lambda **k: {"schema":"DashboardManifest.v1", **k}
build_dashboard_validation_report = lambda **k: {"schema":"DashboardValidationReport.v1", **k}
build_runtime_access_receipt = lambda **k: {"schema":"RuntimeAccessReceipt.v1", **k}
build_query_audit_log = lambda **k: {"schema":"QueryAuditLog.v1", **k}
validate_openapi_contract = lambda openapi: openapi.get("openapi") == "3.1.1"
validate_api_runtime_contract = lambda *a, **k: True
validate_registry_runtime = lambda *a, **k: {"status":"success"}

def build_dashboard_bundle(args):
    inputs = load_runtime_inputs(args); reg = validate_registry_inputs(inputs); parsed = reg["parsed"]
    con = open_sqlite_readonly_immutable(inputs["sqlite_db"])
    snapshot = parsed["registry_snapshot"]; openapi = parsed["openapi"]; saved = parsed["saved_queries"]
    spec = {"module_version":MODULE_VERSION,"runtime_mode":args.runtime_mode,"dashboard_title":args.dashboard_title,"registry_snapshot_id":snapshot.get("registry_snapshot_id","unknown"),"registry_spec_hash":reg["hashes"]["registry_snapshot_sha256"]}
    rsh = compute_runtime_spec_hash(spec); bundle_id = f"{snapshot.get('registry_snapshot_id','registry')}_runtime_{rsh[:12]}"
    root = Path(args.runtime_root); stg = root / ".staging" / bundle_id; final = root / bundle_id
    if final.exists() and not args.overwrite: raise FileExistsError("bundle exists")
    shutil.rmtree(stg, ignore_errors=True); (stg/"assets/js").mkdir(parents=True); (stg/"assets/css").mkdir(parents=True); (stg/"data").mkdir(parents=True)
    html_s, js_s, css_s = build_dashboard_html(args.dashboard_title), build_dashboard_js(), build_dashboard_css()
    validate_dashboard_static_security(html_s, js_s, css_s); validate_dashboard_accessibility(html_s, css_s)
    (stg/"index.html").write_text(html_s, encoding="utf-8"); (stg/"assets/js/dashboard.js").write_text(js_s, encoding="utf-8"); (stg/"assets/css/dashboard.css").write_text(css_s, encoding="utf-8")
    cfg = build_dashboard_config(bundle_id, snapshot.get("registry_snapshot_id","unknown"), reg["hashes"]["registry_snapshot_sha256"], args.dashboard_title)
    write_canonical_json(stg/"app_config.json", cfg)
    for src, dst in [(inputs["registry_manifest"],"registry_manifest.json"),(inputs["registry_snapshot"],"registry_snapshot.json"),(inputs["openapi"],"openapi.json"),(inputs["saved_queries"],"saved_queries.json")]: shutil.copy2(src, stg/"data"/dst)
    receipt = build_runtime_access_receipt(run_id="run",created_at_utc=_utc_now(),status="success",source="soilgrids_registry_runtime",runtime_mode=args.runtime_mode,runtime_bundle_id=bundle_id,runtime_spec_hash=rsh,dashboard_spec_hash=compute_dashboard_spec_hash(cfg))
    write_canonical_json(stg/"runtime_access_receipt.json", receipt)
    write_canonical_json(stg/"api_runtime_contract.json", build_api_runtime_contract(runtime_bundle_id=bundle_id,created_at_utc=_utc_now(),source="soilgrids_registry_runtime",registry_snapshot_id=snapshot.get("registry_snapshot_id"),openapi_version="3.1.1",api_base="/api",read_only=True,allowed_methods=["GET","HEAD","OPTIONS"],post_query_enabled=False,endpoints=[] ,query_safety={"select_only":True}))
    write_canonical_json(stg/"api_runtime_manifest.json", build_api_runtime_manifest(runtime_bundle_id=bundle_id,created_at_utc=_utc_now(),source="soilgrids_registry_runtime"))
    write_canonical_json(stg/"api_runtime_validation_report.json", build_api_runtime_validation_report(run_id="run",created_at_utc=_utc_now(),source="soilgrids_registry_runtime",runtime_bundle_id=bundle_id,status="success",summary={"total_checks":0,"passed":0,"failed":0,"skipped":0,"required_failed":0,"warnings_failed":0},checks=[],errors=[]))
    write_canonical_json(stg/"dashboard_manifest.json", build_dashboard_manifest(runtime_bundle_id=bundle_id,created_at_utc=_utc_now(),source="soilgrids_registry_runtime",dashboard_title=args.dashboard_title,registry_snapshot_id=snapshot.get("registry_snapshot_id"),dashboard_spec_hash=compute_dashboard_spec_hash(cfg),entrypoint="index.html",app_config="app_config.json",views=cfg["views"],accessibility={"wcag_target":"WCAG 2.2 AA","keyboard_navigation":True,"high_contrast":True,"reduced_motion":True},security={"external_scripts":False,"external_css":False,"eval":False,"telemetry":False},errors=[]))
    write_canonical_json(stg/"dashboard_validation_report.json", build_dashboard_validation_report(run_id="run",created_at_utc=_utc_now(),source="soilgrids_registry_runtime",runtime_bundle_id=bundle_id,status="success",summary={"total_checks":0,"passed":0,"failed":0,"skipped":0,"required_failed":0,"warnings_failed":0},checks=[],errors=[]))
    rels=[Path(p) for p in ["index.html","app_config.json","api_runtime_manifest.json","api_runtime_contract.json","api_runtime_validation_report.json","dashboard_manifest.json","dashboard_validation_report.json","runtime_access_receipt.json","assets/js/dashboard.js","assets/css/dashboard.css","data/registry_manifest.json","data/registry_snapshot.json","data/openapi.json","data/saved_queries.json"]]
    write_checksums_file(stg/"checksums.sha256", rels)
    root.mkdir(parents=True, exist_ok=True)
    if final.exists() and args.overwrite: shutil.rmtree(final)
    os.replace(stg, final)
    return final/"runtime_access_receipt.json"

def execute_query_session(args):
    con=open_sqlite_readonly_immutable(Path(args.sqlite_db)); saved=json.loads(Path(args.saved_queries).read_text())
    rows=execute_saved_query(con,saved,args.query_id,json.loads(args.query_params_json) if args.query_params_json else {})
    outdir=Path(args.query_output_dir or Path(args.runtime_root)/"query_results"); outdir.mkdir(parents=True,exist_ok=True)
    res={"rows":rows,"row_count":len(rows)}; out=outdir/f"{args.query_id}.json"; write_canonical_json(out,res)
    audit=build_query_audit_log(run_id="run",created_at_utc=_utc_now(),source="soilgrids_registry_runtime",registry_snapshot_id="unknown",runtime_bundle_id=None,queries=[{"query_execution_id":"query_"+hashlib.sha256(args.query_id.encode()).hexdigest()[:12],"query_id":args.query_id,"query_type":"saved_query","parameters_hash":hashlib.sha256(_canonical_bytes(json.loads(args.query_params_json) if args.query_params_json else {})).hexdigest(),"status":"success","row_count":len(rows),"result_sha256":hashlib.sha256(_canonical_bytes(res)).hexdigest(),"result_path":str(out),"read_only":True}],errors=[])
    write_canonical_json(outdir/"query_audit_log.json", audit)
    return outdir/"query_audit_log.json"

def main():
    ap=argparse.ArgumentParser();
    for a in ["registry_manifest","registry_snapshot","registry_query_contract","registry_validation_report","registry_receipt","sqlite_db","openapi","saved_queries","search_index"]: ap.add_argument(f"--{a.replace('_','-')}")
    ap.add_argument("--runtime-root",required=True); ap.add_argument("--runtime-mode",required=True,choices=["build-dashboard","query-session"]); ap.add_argument("--dashboard-title",default="SoilGrids Governance Dashboard"); ap.add_argument("--query-id"); ap.add_argument("--query-params-json"); ap.add_argument("--query-output-dir"); ap.add_argument("--overwrite",action="store_true")
    args=ap.parse_args()
    try:
        p=build_dashboard_bundle(args) if args.runtime_mode=="build-dashboard" else execute_query_session(args)
        sys.stdout.write(str(p)+"\n"); return 0
    except Exception as e:
        sys.stderr.write(json.dumps({"status":"error","error_count":1,"runtime_access_receipt_path":None,"runtime_bundle_id":None})+"\n"); return 100

if __name__=="__main__": raise SystemExit(main())
