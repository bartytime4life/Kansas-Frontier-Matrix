#!/usr/bin/env python3
import argparse, subprocess
from pathlib import Path

FAMILIES=["app_api","app_web","app_worker","package","connector","schema_contract","api_contract","policy","test","fixture","tool_validator","pipeline","migration","data_lifecycle_raw","data_lifecycle_work","data_lifecycle_quarantine","data_lifecycle_processed","data_lifecycle_catalog","data_lifecycle_triplet","data_lifecycle_receipt","data_lifecycle_proof","data_lifecycle_published","data_registry","release","doc_adr","doc_architecture","doc_domain","doc_register","doc_runbook","doc_source","doc_tracking","style","config","infra","root_meta","generated_or_cache","unknown"]

def classify(p:str)->str:
    if p in {"README.md",".gitignore","pytest.ini","pyproject.toml","Makefile"}: return "root_meta"
    if p.startswith("apps/governed_api/"): return "app_api"
    if p.startswith(("apps/web/","apps/ui/","apps/review-console/","web/","ui/")): return "app_web"
    if p.startswith("apps/"): return "app_worker"
    if p.startswith("packages/"): return "package"
    if p.startswith("connectors/"): return "connector"
    if p.startswith(("contracts/","schemas/","jsonschema/")): return "schema_contract"
    if p.startswith("policy/") or p.startswith("policies/"): return "policy"
    if p.startswith("tests/"): return "test"
    if p.startswith("fixtures/") or "/fixtures/" in p: return "fixture"
    if p.startswith("tools/"): return "tool_validator" if "validator" in p else "pipeline"
    if p.startswith(("pipeline_specs/","pipelines/")): return "pipeline"
    if p.startswith("migrations/"): return "migration"
    if p.startswith("data/raw/"): return "data_lifecycle_raw"
    if p.startswith("data/work/"): return "data_lifecycle_work"
    if p.startswith("data/quarantine/"): return "data_lifecycle_quarantine"
    if p.startswith("data/processed/"): return "data_lifecycle_processed"
    if p.startswith("data/catalog/"): return "data_lifecycle_catalog"
    if p.startswith("data/triplets/"): return "data_lifecycle_triplet"
    if p.startswith("data/receipts/"): return "data_lifecycle_receipt"
    if p.startswith("data/proofs/"): return "data_lifecycle_proof"
    if p.startswith("data/published/"): return "data_lifecycle_published"
    if p.startswith("data/registry/"): return "data_registry"
    if p.startswith("release/"): return "release"
    if p.startswith("docs/adr/"): return "doc_adr"
    if p.startswith("docs/architecture/") or p.startswith("docs/control-plane/"): return "doc_architecture"
    if p.startswith("docs/domains/"): return "doc_domain"
    if p.startswith("docs/registers/"): return "doc_register"
    if p.startswith("docs/runbooks/"): return "doc_runbook"
    if p.startswith("docs/sources/"): return "doc_source"
    if p.startswith("docs/tracking/"): return "doc_tracking"
    if p.startswith("docs/"): return "doc_source"
    if p.startswith("styles/"): return "style"
    if p.startswith("configs/"): return "config"
    if p.startswith("infra/"): return "infra"
    if "__pycache__" in p or p.endswith((".pyc",".pyo")): return "generated_or_cache"
    return "unknown"

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--out", default="docs/registers/reorg/path_inventory.tsv")
    args=ap.parse_args()
    files=subprocess.check_output(["git","ls-files",":!:apps/web/node_modules/**",":!:.git/**"], text=True).splitlines()
    files=sorted(files)
    out=Path(args.out)
    out.parent.mkdir(parents=True,exist_ok=True)
    with out.open("w",encoding="utf-8") as f:
        f.write("path\tfamily\n")
        for p in files:
            f.write(f"{p}\t{classify(p)}\n")

if __name__=="__main__":
    main()
