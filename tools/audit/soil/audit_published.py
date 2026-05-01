#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
import argparse, datetime as dt, json, os, tempfile
from pathlib import Path
from tools.audit.soil._published_common import load_json, sanitize_id, validate_published_release

def atomic_write(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=".tmp_", dir=str(path.parent))
    with os.fdopen(fd, "w", encoding="utf-8") as f:
        f.write(json.dumps(payload, sort_keys=True, indent=2) + "\n")
    os.replace(tmp, path)

def main(argv=None):
    ap=argparse.ArgumentParser();ap.add_argument("--published-root",required=True);ap.add_argument("--release-id");ap.add_argument("--out-root")
    a=ap.parse_args(argv)
    root=Path(a.published_root)
    try:
        rid=a.release_id or load_json(root/"published/soil/current.json").get("current_release_id")
        if not rid: raise ValueError("missing release id")
        v=validate_published_release(root,rid)
        if not v["valid"]:
            print(json.dumps({"audit_passed":False,"release_id":rid,"reasons":v["reasons"]},sort_keys=True));return 1
        outputs={}
        if a.out_root:
            out=Path(a.out_root)/"audits/soil"
            rpt={"schema_version":"kfm.v1","object_type":"PublishedReleaseAuditReport","domain":"soil","release_id":rid,"audit_passed":True,"checks":v["checks"],"created":dt.datetime.now(dt.timezone.utc).isoformat()}
            rct={"schema_version":"kfm.v1","receipt_type":"PublishedReleaseAuditReceipt","release_id":rid,"decision":"pass","report_ref":f"audits/soil/{sanitize_id(rid)}.audit_report.json","created":dt.datetime.now(dt.timezone.utc).isoformat()}
            rp=out/f"{sanitize_id(rid)}.audit_report.json";rc=out/f"{sanitize_id(rid)}.audit_receipt.json"
            atomic_write(rp,rpt);atomic_write(rc,rct)
            outputs={"audit_report":str(rp),"audit_receipt":str(rc)}
        print(json.dumps({"audit_passed":True,"release_id":rid,"checks":v["checks"],"outputs":outputs},sort_keys=True));return 0
    except Exception as e:
        rid=a.release_id or "unknown"
        print(json.dumps({"audit_passed":False,"release_id":rid,"reasons":[str(e)]},sort_keys=True));return 1
if __name__=='__main__': raise SystemExit(main())
