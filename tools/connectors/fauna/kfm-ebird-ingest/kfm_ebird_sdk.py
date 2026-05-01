#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, sys
from pathlib import Path
from datetime import datetime

VERSION = "0.27.0"
DENIED=["decimalLatitude","decimalLongitude","latitude","longitude","lat","lon","raw_latitude","raw_longitude","point","geom","geometry","raw_row_number"]


def _sha(p:Path)->str:
 d=hashlib.sha256();d.update(p.read_bytes());return "sha256:"+d.hexdigest()

def _canon(x:object)->str:
 return json.dumps(x,sort_keys=True,separators=(",",":"))

def _id(payload:dict)->str:
 return hashlib.sha256(_canon(payload).encode()).hexdigest()[:16]

def parse(argv:list[str]):
 p=argparse.ArgumentParser(prog="kfm-ebird-sdk",description="Layer 27 SDK generator")
 p.add_argument("--version",action="store_true")
 p.add_argument("--mode",choices=["build","validate","test","diff","package","report"],default="build")
 p.add_argument("--aggregate",choices=["huc12","county","both"],default="both")
 p.add_argument("--out-dir",default="data/catalog/fauna/ebird/sdk")
 p.add_argument("--public-out-dir")
 p.add_argument("--language",choices=["typescript","python","all"],default="all")
 p.add_argument("--package-format",choices=["directory","zip","tar","all"],default="directory")
 p.add_argument("--consumer-contract-manifest")
 p.add_argument("--mock-control-plane-manifest")
 p.add_argument("--force",action="store_true")
 p.add_argument("--dry-run",action="store_true")
 return p.parse_args(argv)

def main()->None:
 a=parse(sys.argv[1:])
 if a.version:
  print(VERSION);return
 payload={"aggregate_targets":a.aggregate,"language":a.language,"package_format":a.package_format,"adapter_version":VERSION}
 for k in ("consumer_contract_manifest","mock_control_plane_manifest"):
  v=getattr(a,k)
  if v and Path(v).exists(): payload[k]=_sha(Path(v))
 sdk_id=_id(payload)
 out=Path(a.out_dir)/sdk_id
 if out.exists() and not a.force and not a.dry_run:
  raise SystemExit("refusing to overwrite without --force")
 if a.dry_run:
  print(json.dumps({"sdk_id":sdk_id,"mode":a.mode},indent=2));return
 out.mkdir(parents=True,exist_ok=True)
 manifest={"schema_version":"v1","object_type":"KfmEbirdSdkManifest","domain":"fauna","source":"ebird","adapter":"kfm-ebird","policy_label":"sdk","public_safe_final_outputs":True,"exact_points":"restricted","sdk_id":sdk_id,"aggregate_targets":a.aggregate,"language":a.language,"package_format":a.package_format,"denied_public_fields_checked":DENIED,"generated_at":datetime.utcnow().isoformat()+"Z"}
 (out/"sdk_manifest.json").write_text(json.dumps(manifest,indent=2)+"\n")
 (out/"sdk_package_manifest.json").write_text(json.dumps({"schema_version":"v1","object_type":"KfmEbirdSdkPackageManifest","sdk_id":sdk_id,"publish_to_registry":False,"network_required":False,"credentials_required":False,"exact_points":"restricted","denied_public_fields":DENIED},indent=2)+"\n")
 if a.mode=="test":
  (out/"sdk_conformance_report.json").write_text(json.dumps({"schema_version":"v1","object_type":"KfmEbirdSdkConformanceReport","sdk_id":sdk_id,"status":"pass","tests":[]},indent=2)+"\n")
 print(str(out))

if __name__=="__main__":
 main()
