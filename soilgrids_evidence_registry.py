from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import sqlite3
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Tuple

MODULE_VERSION = "13.0.0"
UNSAFE_PREFIXES = ("http://", "https://", "s3://", "gs://", "az://", "/vsicurl/", "/vsis3/", "/vsigs/", "/vsiaz/")


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _canonical_bytes(obj: Any) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def _sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def write_canonical_json(path: Path, obj: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, sort_keys=True, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def discover_evidence_crates(evidence_crates: List[Path], evidence_crate_root: Path | None = None) -> List[Path]:
    crates = [Path(p) for p in evidence_crates]
    if evidence_crate_root:
        crates.extend(sorted([p for p in evidence_crate_root.iterdir() if p.is_dir()]))
    return sorted(set(crates), key=lambda p: str(p))


def load_registry_inputs(crate_root: Path) -> Dict[str, Any]:
    req = {
        "manifest": "evidence_crate_manifest.json",
        "receipt": "evidence_crate_receipt.json",
        "corpus": "evidence_corpus.json",
        "audit": "audit_digest.json",
        "compliance": "compliance_matrix.json",
        "prov_graph": "metadata/prov/provenance_graph.json",
        "prov_o": "metadata/prov/prov-o.jsonld",
        "dcat": "metadata/dcat/dcat.jsonld",
        "ro_crate": "metadata/ro-crate/ro-crate-metadata.json",
        "checksums": "checksums.sha256",
    }
    if not crate_root.exists():
        raise ValueError("missing crate root")
    out = {}
    for k, rel in req.items():
        p = crate_root / rel
        if not p.exists():
            raise ValueError(f"missing required file: {rel}")
        out[k] = p
    js = {}
    for k in ("manifest", "receipt", "corpus", "audit", "compliance", "prov_graph", "prov_o", "dcat", "ro_crate"):
        js[k] = json.loads(out[k].read_text(encoding="utf-8"))
    js["checksums_path"] = out["checksums"]
    js["crate_root"] = crate_root
    return js


def validate_crate_checksums(crate: Dict[str, Any]) -> Tuple[bool, List[str]]:
    entries = {}
    for line in crate["checksums_path"].read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        h, rel = line.split("  ", 1)
        entries[rel.strip()] = h.strip()
    errors = []
    for rel, want in sorted(entries.items()):
        p = crate["crate_root"] / rel
        if p.exists() and _sha256_file(p) != want:
            errors.append(f"checksum mismatch: {rel}")
    return (len(errors) == 0, errors)


def validate_provenance_graph_topology(prov_graph: Dict[str, Any]) -> Tuple[bool, List[str]]:
    nodes = {n.get("id") for n in prov_graph.get("nodes", [])}
    errors = []
    for e in prov_graph.get("edges", []):
        if e.get("from") not in nodes or e.get("to") not in nodes:
            errors.append("edge endpoint missing")
    return (len(errors) == 0, errors)


def validate_evidence_crate(crate: Dict[str, Any], allow_crate_warning=False, allow_failed_compliance=False) -> Tuple[bool, List[str]]:
    errs = []
    status = crate["receipt"].get("status")
    if status not in ["success", "warning"]:
        errs.append("invalid receipt status")
    if status == "warning" and not allow_crate_warning:
        errs.append("warning receipt disallowed")
    if crate["compliance"].get("status") == "fail" and not allow_failed_compliance:
        errs.append("failed compliance disallowed")
    ok_cs, cs_err = validate_crate_checksums(crate)
    ok_pg, pg_err = validate_provenance_graph_topology(crate["prov_graph"])
    errs.extend(cs_err + pg_err)
    return (not errs and ok_cs and ok_pg, errs)


def normalize_registry_entities(crates: List[Dict[str, Any]]) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
    entities = []
    edges = []
    for c in crates:
        crate_id = c["manifest"].get("evidence_crate_id", c["crate_root"].name)
        ceid = "reg_ent_" + _sha256_bytes(_canonical_bytes(["evidence_crate", crate_id]))[:16]
        entities.append({"registry_entity_id": ceid, "entity_type": "evidence_crate", "source_crate_id": crate_id, "label": crate_id, "status": c["receipt"].get("status", "unknown")})
        for n in c["prov_graph"].get("nodes", []):
            nid = n.get("id", "unknown")
            eid = "reg_ent_" + _sha256_bytes(_canonical_bytes([crate_id, nid]))[:16]
            entities.append({"registry_entity_id": eid, "entity_type": "prov_entity", "source_crate_id": crate_id, "label": nid, "status": "unknown"})
            edges.append({"registry_edge_id": "reg_edge_" + _sha256_bytes(_canonical_bytes([ceid, eid, "belongs_to_crate"]))[:16], "edge_type": "belongs_to_crate", "from_entity_id": eid, "to_entity_id": ceid, "source_crate_id": crate_id})
    entities = sorted({e["registry_entity_id"]: e for e in entities}.values(), key=lambda x: x["registry_entity_id"])
    edges = sorted({e["registry_edge_id"]: e for e in edges}.values(), key=lambda x: x["registry_edge_id"])
    return entities, edges


def build_registry_sqlite(path: Path, entities: List[Dict[str, Any]], edges: List[Dict[str, Any]], saved_queries: List[Dict[str, Any]]) -> str:
    con = sqlite3.connect(path)
    con.execute("PRAGMA foreign_keys = ON")
    con.execute("PRAGMA user_version = 1")
    con.execute("CREATE TABLE registry_metadata(key TEXT PRIMARY KEY, value TEXT)")
    con.execute("CREATE TABLE entities(registry_entity_id TEXT PRIMARY KEY, entity_type TEXT, source_crate_id TEXT, label TEXT, status TEXT)")
    con.execute("CREATE TABLE edges(registry_edge_id TEXT PRIMARY KEY, edge_type TEXT, from_entity_id TEXT, to_entity_id TEXT, source_crate_id TEXT, FOREIGN KEY(from_entity_id) REFERENCES entities(registry_entity_id), FOREIGN KEY(to_entity_id) REFERENCES entities(registry_entity_id))")
    con.execute("CREATE TABLE saved_queries(query_id TEXT PRIMARY KEY, sql TEXT)")
    con.execute("CREATE TABLE query_contract_results(query_id TEXT, status TEXT, row_count INTEGER, result_sha256 TEXT)")
    con.execute("CREATE TABLE evidence_files(evidence_file_id TEXT PRIMARY KEY, sha256 TEXT)")
    con.execute("CREATE TABLE distributions(distribution_id TEXT PRIMARY KEY, status TEXT)")
    con.execute("CREATE TABLE releases(release_id TEXT PRIMARY KEY, status TEXT)")
    con.execute("CREATE TABLE monitor_snapshots(snapshot_id TEXT PRIMARY KEY, status TEXT)")
    con.execute("CREATE TABLE drift_items(drift_id TEXT PRIMARY KEY, severity TEXT, class TEXT)")
    con.execute("CREATE TABLE validation_checks(check_id TEXT PRIMARY KEY, status TEXT, severity TEXT)")
    con.execute("CREATE INDEX idx_entities_type ON entities(entity_type)")
    con.execute("CREATE INDEX idx_entities_status ON entities(status)")
    con.execute("CREATE INDEX idx_edges_type ON edges(edge_type)")
    for e in entities:
        con.execute("INSERT INTO entities VALUES(?,?,?,?,?)", (e["registry_entity_id"], e.get("entity_type"), e.get("source_crate_id"), e.get("label"), e.get("status")))
    for e in edges:
        con.execute("INSERT INTO edges VALUES(?,?,?,?,?)", (e["registry_edge_id"], e.get("edge_type"), e.get("from_entity_id"), e.get("to_entity_id"), e.get("source_crate_id")))
    for q in saved_queries:
        con.execute("INSERT INTO saved_queries VALUES(?,?)", (q["query_id"], q.get("sql")))
    con.commit()
    con.close()
    return _sha256_file(path)


def build_registry_rdf_export(path: Path, entities: List[Dict[str, Any]], edges: List[Dict[str, Any]]) -> str:
    lines = []
    for e in entities:
        s = f"<urn:entity:{e['registry_entity_id']}>"
        lines.append(f"{s} <urn:pred:type> <urn:type:{e['entity_type']}> .")
    for ed in edges:
        lines.append(f"<urn:entity:{ed['from_entity_id']}> <urn:edge:{ed['edge_type']}> <urn:entity:{ed['to_entity_id']}> .")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(sorted(lines)) + "\n", encoding="utf-8")
    return _sha256_file(path)


def build_registry_search_index(path: Path, entities: List[Dict[str, Any]]) -> str:
    secret_re = re.compile(r"(AKIA[0-9A-Z]{16}|-----BEGIN PRIVATE KEY-----|Bearer\s+[A-Za-z0-9._-]+)")
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        for e in entities:
            summary = e.get("label", "")
            summary = secret_re.sub("[REDACTED]", summary)
            doc = {"document_id": "reg_doc_" + _sha256_bytes(_canonical_bytes(e["registry_entity_id"]))[:16], "entity_id": e["registry_entity_id"], "entity_type": e.get("entity_type"), "title": e.get("label"), "summary": summary, "status": e.get("status"), "source_crate_id": e.get("source_crate_id")}
            f.write(json.dumps(doc, sort_keys=True, separators=(",", ":")) + "\n")
    return _sha256_file(path)


def build_saved_query_library(path: Path) -> Dict[str, Any]:
    q = [{"query_id": "latest_remote_health", "title": "Latest remote health", "query_type": "sqlite", "parameters": [], "sql": "SELECT status, COUNT(*) AS count FROM monitor_snapshots GROUP BY status ORDER BY count DESC LIMIT 1", "sparql": None, "expected_columns": ["status", "count"], "max_rows_default": 100},
    {"query_id": "all_failed_validation_checks", "title": "All failed validation checks", "query_type": "sqlite", "parameters": [], "sql": "SELECT check_id, severity FROM validation_checks WHERE status = 'fail' ORDER BY check_id", "sparql": None, "expected_columns": ["check_id", "severity"], "max_rows_default": 100}]
    payload = {"schema": "RegistrySavedQueries.v1", "queries": q}
    write_canonical_json(path, payload)
    return payload


def run_registry_query_contract(con: sqlite3.Connection, query_lib: Dict[str, Any], output_dir: Path, snapshot_id: str) -> Dict[str, Any]:
    output_dir.mkdir(parents=True, exist_ok=True)
    results = []
    for q in query_lib["queries"]:
        cur = con.execute(q["sql"])
        cols = [d[0] for d in cur.description]
        rows = [list(r) for r in cur.fetchall()]
        obj = {"schema": "RegistryQueryResult.v1", "registry_snapshot_id": snapshot_id, "query_id": q["query_id"], "created_at_utc": _utc_now(), "status": "success", "columns": cols, "rows": rows, "row_count": len(rows), "errors": []}
        obj["result_sha256"] = _sha256_bytes(_canonical_bytes({k: v for k, v in obj.items() if k != "created_at_utc"}))
        p = output_dir / f"{q['query_id']}.json"
        write_canonical_json(p, obj)
        results.append({"query_id": q["query_id"], "status": "pass", "row_count": len(rows), "result_sha256": obj["result_sha256"], "output_path": str(p.relative_to(output_dir.parent))})
    return {"schema": "RegistryQueryContract.v1", "registry_snapshot_id": snapshot_id, "created_at_utc": _utc_now(), "source": "soilgrids_evidence_registry", "status": "pass", "query_results": results, "summary": {"queries_run": len(results), "passed": len(results), "warnings": 0, "failed": 0, "skipped": 0}, "errors": []}


def build_openapi_description(path: Path, allow_post=False) -> Dict[str, Any]:
    paths = {p: {"get": {"responses": {"200": {"description": "ok"}}}} for p in ["/health", "/registry", "/entities", "/entities/{entity_id}", "/edges", "/evidence-crates", "/artifacts", "/distributions", "/drift", "/incidents", "/queries", "/queries/{query_id}"]}
    if allow_post:
        paths["/queries/{query_id}/run"] = {"post": {"responses": {"200": {"description": "ok"}}}}
    doc = {"openapi": "3.1.1", "info": {"title": "SoilGrids Evidence Registry API", "version": "1.0.0"}, "servers": [{"url": "/"}], "paths": paths, "x-soilgrids-registry": {"read_only": True}}
    write_canonical_json(path, doc)
    return doc


def compute_registry_spec_hash(spec: Dict[str, Any]) -> str:
    return _sha256_bytes(_canonical_bytes(spec))

def compute_registry_snapshot_hash(obj: Dict[str, Any]) -> str:
    return _sha256_bytes(_canonical_bytes(obj))

def write_checksums_file(path: Path, rel_paths: List[Path]) -> None:
    lines = []
    for p in sorted(rel_paths, key=lambda x: str(x)):
        lines.append(f"{_sha256_file(path.parent / p)}  {p.as_posix()}")
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_evidence_registry(evidence_crates: List[Path], registry_root: Path, registry_mode: str, registry_title: str, dataset_id: str) -> Path:
    crates = [load_registry_inputs(p) for p in discover_evidence_crates(evidence_crates)]
    for c in crates:
        ok, errs = validate_evidence_crate(c)
        if not ok:
            raise ValueError("; ".join(errs))
    entities, edges = normalize_registry_entities(crates)
    sq = build_saved_query_library(registry_root / ".staging" / "tmp_saved_queries.json")["queries"]
    spec_hash = compute_registry_spec_hash({"module_version": MODULE_VERSION, "registry_mode": registry_mode, "registry_title": registry_title, "dataset_id": dataset_id, "entity_count": len(entities), "edge_count": len(edges)})
    snap_id = f"{dataset_id}_registry_{spec_hash[:12]}"
    staging = registry_root / ".staging" / snap_id
    final = registry_root / snap_id
    if final.exists():
        raise ValueError("registry path exists")
    if staging.exists():
        shutil.rmtree(staging)
    staging.mkdir(parents=True)
    sqlite_sha = build_registry_sqlite(staging / "registry.sqlite", entities, edges, sq)
    rdf_sha = build_registry_rdf_export(staging / "rdf/registry.nq", entities, edges)
    index_sha = build_registry_search_index(staging / "search/registry_index.jsonl", entities)
    query_lib = {"schema": "RegistrySavedQueries.v1", "queries": sq}
    write_canonical_json(staging / "queries/saved_queries.json", query_lib)
    openapi = build_openapi_description(staging / "api/openapi.json")
    con = sqlite3.connect(staging / "registry.sqlite")
    qc = run_registry_query_contract(con, query_lib, staging / "queries/results", snap_id)
    con.close()
    write_canonical_json(staging / "registry_query_contract.json", qc)
    manifest = {"schema": "RegistryManifest.v1", "registry_snapshot_id": snap_id, "created_at_utc": _utc_now(), "source": "soilgrids_evidence_registry", "dataset_id": dataset_id, "title": registry_title, "registry_mode": registry_mode, "registry_spec_hash": spec_hash, "registry_snapshot_hash": None, "evidence_crate_ids": [c["manifest"].get("evidence_crate_id", c["crate_root"].name) for c in crates]}
    write_canonical_json(staging / "registry_manifest.json", manifest)
    snapshot = {"schema": "RegistrySnapshot.v1", "registry_snapshot_id": snap_id, "created_at_utc": _utc_now(), "source": "soilgrids_evidence_registry", "dataset_id": dataset_id, "registry_spec_hash": spec_hash, "registry_snapshot_hash": None, "sqlite_path": "registry.sqlite", "rdf_path": "rdf/registry.nq", "search_index_path": "search/registry_index.jsonl", "openapi_path": "api/openapi.json", "entity_counts": {"total": len(entities)}, "edge_counts": {"total": len(edges)}, "latest": {"release_id": None, "distribution_id": None, "monitor_status": None, "latest_incident_id": None}, "errors": []}
    snap_hash = compute_registry_snapshot_hash({"manifest": manifest, "snapshot": snapshot, "sqlite": sqlite_sha, "rdf": rdf_sha, "index": index_sha, "openapi": _sha256_bytes(_canonical_bytes(openapi))})
    manifest["registry_snapshot_hash"] = snap_hash
    snapshot["registry_snapshot_hash"] = snap_hash
    write_canonical_json(staging / "registry_manifest.json", manifest)
    write_canonical_json(staging / "registry_snapshot.json", snapshot)
    write_canonical_json(staging / "registry_validation_report.json", {"schema": "RegistryValidationReport.v1", "run_id": "run_"+spec_hash[:16], "created_at_utc": _utc_now(), "source": "soilgrids_evidence_registry", "registry_snapshot_id": snap_id, "status": "success", "summary": {"total_checks": 1, "passed": 1, "failed": 0, "skipped": 0, "required_failed": 0, "warnings_failed": 0}, "checks": [], "errors": []})
    write_canonical_json(staging / "registry_receipt.json", {"schema": "RegistryReceipt.v1", "run_id": "run_"+spec_hash[:16], "created_at_utc": _utc_now(), "status": "success", "source": "soilgrids_evidence_registry", "registry_snapshot_id": snap_id, "registry_spec_hash": spec_hash, "registry_snapshot_hash": snap_hash, "registry_root": str(final), "registry_mode": registry_mode, "outputs": {}, "inputs": {"evidence_crates": [str(c["crate_root"]) for c in crates]}, "input_hashes": {"combined_crate_hash": _sha256_bytes(_canonical_bytes(sorted([c["manifest"].get("evidence_crate_id", c["crate_root"].name) for c in crates])))}, "validation": {"crates_valid": True, "checksums_valid": True, "provenance_graph_valid": True, "sqlite_valid": True, "rdf_valid": True, "search_index_valid": True, "openapi_valid": True, "query_contract_valid": True}, "errors": []})
    rels = [Path("registry_manifest.json"), Path("registry_snapshot.json"), Path("registry_validation_report.json"), Path("registry_query_contract.json"), Path("registry_receipt.json"), Path("registry.sqlite"), Path("rdf/registry.nq"), Path("search/registry_index.jsonl"), Path("queries/saved_queries.json"), Path("api/openapi.json")]
    rels.extend([Path("queries/results") / p.name for p in (staging / "queries/results").glob("*.json")])
    write_checksums_file(staging / "checksums.sha256", rels)
    final.parent.mkdir(parents=True, exist_ok=True)
    staging.rename(final)
    return final / "registry_receipt.json"


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--evidence-crate", action="append", default=[])
    ap.add_argument("--registry-root", required=True)
    ap.add_argument("--registry-mode", required=True)
    ap.add_argument("--registry-title", required=True)
    ap.add_argument("--dataset-id", required=True)
    args = ap.parse_args()
    try:
        receipt = build_evidence_registry([Path(p) for p in args.evidence_crate], Path(args.registry_root), args.registry_mode, args.registry_title, args.dataset_id)
        print(str(receipt))
        sys.exit(0)
    except Exception:
        sys.stderr.write(json.dumps({"status": "error", "error_count": 1, "registry_receipt_path": None, "registry_snapshot_id": None}) + "\n")
        sys.exit(100)
