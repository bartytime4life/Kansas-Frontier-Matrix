#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, sys
from pathlib import Path
from datetime import datetime
VERSION="0.27.0"

def _sha(p:Path)->str:
 import hashlib
 d=hashlib.sha256();d.update(p.read_bytes());return "sha256:"+d.hexdigest()

def _id(payload:dict)->str:
 return hashlib.sha256(json.dumps(payload,sort_keys=True,separators=(",",":")).encode()).hexdigest()[:16]

def parse(argv:list[str]):
 p=argparse.ArgumentParser(prog="kfm-ebird-examples",description="Layer 27 examples generator")
 p.add_argument("--version",action="store_true")
 p.add_argument("--mode",choices=["build","validate","run","diff","report"],default="build")
 p.add_argument("--aggregate",choices=["huc12","county","both"],default="both")
 p.add_argument("--language",choices=["typescript","python","all"],default="all")
 p.add_argument("--out-dir",default="data/catalog/fauna/ebird/examples")
 p.add_argument("--sdk-manifest")
 p.add_argument("--force",action="store_true")
 p.add_argument("--dry-run",action="store_true")
 return p.parse_args(argv)

def main()->None:
 a=parse(sys.argv[1:])
 if a.version: print(VERSION);return
 payload={"aggregate_targets":a.aggregate,"language":a.language,"adapter_version":VERSION}
 if a.sdk_manifest and Path(a.sdk_manifest).exists(): payload["sdk_manifest_sha256"]=_sha(Path(a.sdk_manifest))
 ex_id=_id(payload); out=Path(a.out_dir)/ex_id
 if out.exists() and not a.force and not a.dry_run: raise SystemExit("refusing to overwrite without --force")
 if a.dry_run: print(json.dumps({"examples_id":ex_id,"mode":a.mode},indent=2));return
 out.mkdir(parents=True,exist_ok=True)
 man={"schema_version":"v1","object_type":"KfmEbirdExamplesManifest","domain":"fauna","source":"ebird","adapter":"kfm-ebird","policy_label":"examples","public_safe_final_outputs":True,"exact_points":"restricted","examples_id":ex_id,"aggregate_targets":a.aggregate,"language":a.language,"generated_at":datetime.utcnow().isoformat()+"Z"}
 (out/"examples_manifest.json").write_text(json.dumps(man,indent=2)+"\n")
 print(str(out))
if __name__=="__main__": main()
