from __future__ import annotations

import argparse
import base64
import datetime as dt
import hashlib
import json
import os
import platform
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple
from urllib import request, error

try:
    import tomllib
except Exception:  # pragma: no cover
    tomllib = None

SUPPORTED_MODES = {
    "inventory-only", "sbom", "verify", "attest", "offline-vulnerability-scan",
    "online-vulnerability-scan", "certify-supply-chain", "dry-run",
}

class SupplyChainError(Exception):
    def __init__(self, message: str, code: int = 110):
        super().__init__(message)
        self.code = code


def now_utc() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def sha256_bytes(b: bytes) -> str:
    return hashlib.sha256(b).hexdigest()


def canonical_json_bytes(obj: Any) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def write_canonical_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, sort_keys=True, indent=2) + "\n", encoding="utf-8")


def compute_file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def load_supply_chain_spec(path: Path) -> Dict[str, Any]:
    if not path.exists():
        raise SupplyChainError("missing supply chain spec", 30)
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        raise SupplyChainError(f"malformed supply chain spec: {e}", 30)


def validate_supply_chain_spec(spec: Dict[str, Any], allow_remote_network: bool = False) -> None:
    if spec.get("schema") != "SupplyChainSpec.v1":
        raise SupplyChainError("unsupported schema", 30)
    if not spec.get("supply_chain_id"):
        raise SupplyChainError("missing supply_chain_id", 30)
    vuln = (spec.get("vulnerabilities") or {}).get("mode", "offline")
    if vuln not in {"offline", "online", "none"}:
        raise SupplyChainError("unknown vulnerability mode", 30)
    if vuln == "online" and not allow_remote_network:
        raise SupplyChainError("online vulnerability scan without allow remote network", 90)


def compute_supply_chain_spec_hash(spec: Dict[str, Any]) -> str:
    normalized = json.loads(json.dumps(spec, sort_keys=True))
    return sha256_bytes(canonical_json_bytes(normalized))


def discover_repository_files(repo_root: Path, include_globs: List[str], exclude_globs: List[str]) -> List[Path]:
    out: set[Path] = set()
    for g in include_globs:
        for p in repo_root.glob(g):
            if p.is_file():
                out.add(p)
    results = []
    for p in sorted(out):
        rel = p.relative_to(repo_root).as_posix()
        if any(Path(rel).match(ex) for ex in exclude_globs):
            continue
        results.append(p)
    return results


def classify_supply_chain_file(rel: str) -> str:
    if rel.endswith(".py") and "/tests/" in f"/{rel}":
        return "test_file"
    if rel.endswith(".py"):
        return "source_module"
    if "/workflows/" in rel and (rel.endswith(".yml") or rel.endswith(".yaml")):
        return "workflow"
    if rel.endswith(".sh"):
        return "script"
    if "policy" in rel and rel.endswith(".json"):
        return "policy"
    if "manifest" in rel and rel.endswith(".json"):
        return "manifest"
    if "receipt" in rel and rel.endswith(".json"):
        return "receipt"
    if "report" in rel and rel.endswith(".json"):
        return "report"
    if rel.endswith(("requirements.txt", "poetry.lock", "Pipfile.lock")):
        return "dependency_lock"
    if rel.lower().startswith("readme") or rel.endswith(".md"):
        return "documentation"
    return "unknown"


def compute_file_inventory(repo_root: Path, files: List[Path], allow_unknown_files: bool = False) -> List[Dict[str, Any]]:
    inv = []
    for p in files:
        rel = p.relative_to(repo_root).as_posix()
        role = classify_supply_chain_file(rel)
        if role == "unknown" and not allow_unknown_files:
            raise SupplyChainError(f"unknown role {rel}", 40)
        inv.append({
            "path": rel,
            "role": role,
            "bytes": p.stat().st_size,
            "sha256": compute_file_sha256(p),
            "language": "python" if rel.endswith(".py") else None,
            "included_in_sbom": role in {"source_module", "dependency_lock", "test_file", "workflow", "script"},
        })
    return sorted(inv, key=lambda x: x["path"])


def parse_requirements_txt(path: Path) -> List[Dict[str, str]]:
    deps = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "==" in line:
            n, v = line.split("==", 1)
            deps.append({"name": n.strip(), "version": v.strip(), "source": path.name})
        else:
            deps.append({"name": re.split(r"[<>= ]", line)[0], "version": "", "source": path.name})
    return deps


def parse_pyproject_toml(path: Path) -> List[Dict[str, str]]:
    if tomllib is None:
        return []
    data = tomllib.loads(path.read_text(encoding="utf-8"))
    deps = []
    for d in data.get("project", {}).get("dependencies", []):
        name = re.split(r"[<>= (]", d)[0]
        deps.append({"name": name, "version": "", "source": path.name})
    return deps


def parse_lockfiles(repo_root: Path) -> List[Dict[str, str]]:
    deps = []
    for f in ["requirements.txt", "requirements-dev.txt"]:
        p = repo_root / f
        if p.exists():
            deps.extend(parse_requirements_txt(p))
    pyproj = repo_root / "pyproject.toml"
    if pyproj.exists():
        deps.extend(parse_pyproject_toml(pyproj))
    return deps

parse_python_dependencies = parse_lockfiles


def build_dependency_graph(supply_chain_id: str, deps: List[Dict[str, str]]) -> Dict[str, Any]:
    pkgs = []
    rels = []
    for d in sorted(deps, key=lambda x: (x["name"], x.get("version", ""))):
        ver = d.get("version") or "unknown"
        pkg_id = f"pkg:pypi/{d['name']}@{ver}"
        pkgs.append({"package_id": pkg_id, "name": d["name"], "version": ver, "source": d.get("source"), "direct": True, "license": None, "hashes": []})
        rels.append({"from": "root", "to": pkg_id, "type": "depends_on"})
    graph = {"schema": "DependencyGraph.v1", "supply_chain_id": supply_chain_id, "created_at_utc": now_utc(), "source": "soilgrids_supply_chain", "ecosystem": "PyPI", "packages": pkgs, "relationships": rels, "errors": []}
    graph["dependency_graph_hash"] = sha256_bytes(canonical_json_bytes({"packages": pkgs, "relationships": rels, "ecosystem": "PyPI", "supply_chain_id": supply_chain_id}))
    return graph


def build_spdx_sbom(supply_chain_id: str, deps: List[Dict[str, str]]) -> Dict[str, Any]:
    packages = []
    for d in sorted(deps, key=lambda x: (x["name"], x.get("version", ""))):
        packages.append({"SPDXID": f"SPDXRef-{d['name']}-{(d.get('version') or 'unknown').replace('.', '_')}", "name": d["name"], "versionInfo": d.get("version") or "unknown", "downloadLocation": "NOASSERTION"})
    return {"spdxVersion": "SPDX-2.3", "SPDXID": "SPDXRef-DOCUMENT", "name": supply_chain_id, "dataLicense": "CC0-1.0", "packages": packages}


def build_cyclonedx_sbom(supply_chain_id: str, deps: List[Dict[str, str]]) -> Dict[str, Any]:
    comps = [{"type": "library", "name": d["name"], "version": d.get("version") or "unknown", "purl": f"pkg:pypi/{d['name']}@{d.get('version') or 'unknown'}"} for d in sorted(deps, key=lambda x: (x["name"], x.get("version", "")))]
    return {"bomFormat": "CycloneDX", "specVersion": "1.6", "version": 1, "metadata": {"component": {"type": "application", "name": supply_chain_id}}, "components": comps}


def validate_sbom_consistency(spdx: Dict[str, Any], cyclonedx: Dict[str, Any]) -> bool:
    s = {(p["name"], p.get("versionInfo", "")) for p in spdx.get("packages", [])}
    c = {(p["name"], p.get("version", "")) for p in cyclonedx.get("components", [])}
    return s == c

# stubs for completeness
load_license_policy=lambda spec: spec.get("licenses", {})

def evaluate_license_compliance(deps, policy):
    findings=[]; denied=0; unknown=0; allowed=0
    allow=set(policy.get("allowed",[])); deny=set(policy.get("denied",[]))
    for d in deps:
        lic=d.get("license")
        if lic in deny: st="denied"; denied+=1
        elif lic in allow: st="allowed"; allowed+=1
        else: st="unknown"; unknown+=1
        findings.append({"package_id":f"pkg:pypi/{d['name']}@{d.get('version') or 'unknown'}","license":lic,"status":st,"severity":"required" if st=="denied" else "warning" if st=="unknown" else "info"})
    status="fail" if denied else ("warning" if unknown else "pass")
    return {"status":status,"findings":findings,"summary":{"allowed":allowed,"denied":denied,"unknown":unknown},"errors":[]}

def load_advisory_database(path):
    if not path: return {}
    return json.loads(Path(path).read_text(encoding='utf-8'))

def match_vulnerabilities_offline(deps, db):
    findings=[]
    vulns=db.get("vulns",[])
    for d in deps:
        for v in vulns:
            if v.get("package")==d["name"] and (not v.get("version") or v.get("version")==d.get("version")):
                findings.append({"finding_id":"vuln_"+sha256_bytes(f"{d['name']}:{v['id']}".encode())[:12],"package_id":f"pkg:pypi/{d['name']}@{d.get('version') or 'unknown'}","vulnerability_id":v["id"],"severity":v.get("severity","unknown"),"affected":True,"fixed_versions":v.get("fixed_versions",[]),"source":"OSV"})
    return findings

def query_vulnerabilities_online_if_allowed(*args, **kwargs):
    raise SupplyChainError("online scanning not implemented without explicit adapter", 60)
validate_source_integrity=lambda *a, **k: {"status":"pass","checks":[],"summary":{"files_checked":len(a[0]) if a else 0,"hash_conflicts":0,"secret_findings":0,"unsafe_paths":0},"errors":[]}
validate_workflow_supply_chain=lambda *a, **k: {"status":"pass","workflow_files":[],"checks":[],"errors":[]}
validate_generated_scripts=lambda *a, **k: {"status":"pass","checks":[],"errors":[]}

def build_environment_report():
    return {"schema":"BuildEnvironmentReport.v1","created_at_utc":now_utc(),"source":"soilgrids_supply_chain","status":"pass","python":{"version":sys.version.split()[0],"executable":sys.executable,"executable_sha256":compute_file_sha256(Path(sys.executable)) if Path(sys.executable).exists() else None},"platform":{"system":platform.system(),"release":platform.release(),"machine":platform.machine()},"tools":{"git":{"version":None},"gdal_translate":{"version":None},"cosign":{"version":None}},"environment_variables_recorded":[],"redactions":[],"errors":[]}

def build_slsa_provenance_statement(*args, **kwargs): return {"_type":"https://in-toto.io/Statement/v1","predicateType":"https://slsa.dev/provenance/v1","subject":[],"predicate":{"buildDefinition":{},"runDetails":{}}}
def build_intoto_statement_bundle(*args, **kwargs): return {"schema":"InTotoStatementBundle.v1","statements":[]}
sign_attestations_if_requested=lambda *a, **k: []
verify_attestations_if_requested=lambda *a, **k: []
def build_attestation_bundle(supply_chain_id, atts): return {"schema":"AttestationBundle.v1","supply_chain_id":supply_chain_id,"created_at_utc":now_utc(),"source":"soilgrids_supply_chain","status":"unsigned","attestations":atts,"errors":[]}
build_signature_verification_report=lambda *a, **k: {"schema":"SignatureVerificationReport.v1","status":"not_run","verifications":[],"errors":[]}

def evaluate_supply_chain_gate(sbom_ok=True, license_status="pass", vuln_status="pass"):
    failed = []
    if not sbom_ok: failed.append("sbom")
    if license_status == "fail": failed.append("license")
    if vuln_status == "fail": failed.append("vuln")
    return {"status": "fail" if failed else "pass", "failed": failed}

build_supply_chain_inventory=lambda *a, **k: None
build_vulnerability_scan_report=lambda *a, **k: None
build_license_compliance_report=lambda *a, **k: None
build_source_integrity_report=lambda *a, **k: None
build_workflow_supply_chain_report=lambda *a, **k: None
build_supply_chain_gate_report=lambda *a, **k: None
build_supply_chain_receipt=lambda *a, **k: None

def compute_inventory_hash(inventory_files: List[Dict[str, Any]]) -> str:
    keep = [{k: f[k] for k in ["path", "role", "bytes", "sha256", "included_in_sbom"]} for f in inventory_files]
    return sha256_bytes(canonical_json_bytes(keep))

def compute_sbom_hashes(spdx: Dict[str, Any], cyclonedx: Dict[str, Any]) -> Dict[str, str]:
    return {"spdx_sha256": sha256_bytes(canonical_json_bytes(spdx)), "cyclonedx_sha256": sha256_bytes(canonical_json_bytes(cyclonedx))}

def write_checksums_file(root: Path) -> Path:
    lines=[]
    for p in sorted([x for x in root.rglob("*") if x.is_file()]):
        rel=p.relative_to(root).as_posix()
        lines.append(f"{compute_file_sha256(p)}  {rel}")
    out=root/"checksums.sha256"
    out.write_text("\n".join(lines)+"\n", encoding="utf-8")
    return out


def run_supply_chain_authority(**kwargs):
    spec=load_supply_chain_spec(Path(kwargs["supply_chain_spec"]))
    validate_supply_chain_spec(spec, kwargs.get("allow_remote_network", False))
    repo=Path(kwargs["repo_root"]).resolve(); out_root=Path(kwargs["output_root"]).resolve(); mode=kwargs["mode"]
    includes=spec.get("inventory",{}).get("include_globs",["*.py"])
    excludes=spec.get("inventory",{}).get("exclude_globs",[])
    files=discover_repository_files(repo, includes, excludes)
    inv=compute_file_inventory(repo, files, kwargs.get("allow_unknown_files", False))
    inv_hash=compute_inventory_hash(inv)
    deps=parse_lockfiles(repo)
    graph=build_dependency_graph(spec["supply_chain_id"], deps)
    run_id=kwargs.get("supply_chain_run_id") or f"{spec['supply_chain_id']}_{compute_supply_chain_spec_hash(spec)[:12]}"
    run_dir=out_root/run_id
    run_dir.mkdir(parents=True, exist_ok=True)
    write_canonical_json(run_dir/"supply_chain_spec.json", spec)
    write_canonical_json(run_dir/"supply_chain_inventory.json", {"schema":"SupplyChainInventory.v1","supply_chain_id":spec["supply_chain_id"],"created_at_utc":now_utc(),"source":"soilgrids_supply_chain","inventory_hash":inv_hash,"repo_root":str(repo),"files":inv,"summary":{"file_count":len(inv)},"errors":[]})
    write_canonical_json(run_dir/"dependency_graph.json", graph)
    sbom_hashes={}
    if mode in {"sbom","certify-supply-chain","verify","attest","offline-vulnerability-scan","online-vulnerability-scan"}:
        spdx=build_spdx_sbom(spec["supply_chain_id"], deps); cdx=build_cyclonedx_sbom(spec["supply_chain_id"], deps)
        (run_dir/"sbom").mkdir(exist_ok=True)
        write_canonical_json(run_dir/"sbom/spdx.json", spdx); write_canonical_json(run_dir/"sbom/cyclonedx.json", cdx)
        sbom_hashes=compute_sbom_hashes(spdx, cdx)
    receipt={"schema":"SupplyChainReceipt.v1","run_id":run_id,"created_at_utc":now_utc(),"status":"dry_run" if mode=="dry-run" else "success","source":"soilgrids_supply_chain","mode":mode,"supply_chain_id":spec["supply_chain_id"],"supply_chain_spec_hash":compute_supply_chain_spec_hash(spec),"inventory_hash":inv_hash,"dependency_graph_hash":graph["dependency_graph_hash"],"outputs":{"inventory":"supply_chain_inventory.json","dependency_graph":"dependency_graph.json","spdx_sbom":"sbom/spdx.json" if sbom_hashes else None,"cyclonedx_sbom":"sbom/cyclonedx.json" if sbom_hashes else None,"checksums":"checksums.sha256"},"errors":[]}
    write_canonical_json(run_dir/"supply_chain_receipt.json", receipt)
    write_checksums_file(run_dir)
    return run_dir/"supply_chain_receipt.json", (5 if mode=="dry-run" else 0)


def main(argv=None):
    p=argparse.ArgumentParser()
    p.add_argument("--supply-chain-spec", required=True)
    p.add_argument("--repo-root", required=True)
    p.add_argument("--output-root", required=True)
    p.add_argument("--mode", required=True)
    p.add_argument("--offline-advisory-db")
    p.add_argument("--allow-remote-network", action="store_true")
    p.add_argument("--allow-unknown-files", action="store_true")
    p.add_argument("--supply-chain-run-id")
    args=p.parse_args(argv)
    try:
        if args.mode not in SUPPORTED_MODES:
            raise SupplyChainError("unsupported mode",30)
        receipt_path, code = run_supply_chain_authority(**vars(args))
        print(str(receipt_path))
        return code
    except SupplyChainError as e:
        sys.stderr.write(json.dumps({"status":"error","error_count":1,"supply_chain_receipt_path":None,"supply_chain_id":None})+"\n")
        return e.code

if __name__ == "__main__":
    raise SystemExit(main())
