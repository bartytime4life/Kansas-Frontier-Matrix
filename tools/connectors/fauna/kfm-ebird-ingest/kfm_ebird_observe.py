#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, sys
from datetime import datetime, timezone
from pathlib import Path

DENIED_FIELDS={"decimalLatitude","decimalLongitude","latitude","longitude","lat","lon","raw_latitude","raw_longitude","point","geom","geometry"}
SECRET_KEYS={"token","api_key","apikey","key","secret","password","credential","access_token","refresh_token","auth","signature","sig"}


def now(): return datetime.now(timezone.utc).isoformat()
def cjson(o): return json.dumps(o,sort_keys=True,separators=(",",":"),ensure_ascii=False)
def sha256_text(t:str): return "sha256:"+hashlib.sha256(t.encode()).hexdigest()
def sha256_file(p:Path): return sha256_text(p.read_text())

def fail(m):
    print(f"ERROR: {m}", file=sys.stderr)
    raise SystemExit(2)

def redact_uri(uri:str|None):
    if not uri: return uri
    if "?" not in uri: return uri
    b,q=uri.split("?",1)
    out=[]
    for part in q.split("&"):
        if "=" not in part: out.append(part); continue
        k,v=part.split("=",1)
        out.append(f"{k}=REDACTED" if k.lower() in SECRET_KEYS else f"{k}={v}")
    return b+"?"+"&".join(out)

def load_json(p:Path): return json.loads(p.read_text())

def scan_obj(x, issues, public_safe=False):
    if isinstance(x, dict):
        for k,v in x.items():
            lk=k.lower()
            if public_safe and lk in {f.lower() for f in DENIED_FIELDS}:
                issues.append(f"denied_field:{k}")
            if lk in SECRET_KEYS and isinstance(v,str) and v:
                issues.append(f"secret_key:{k}")
            if isinstance(v,str):
                lv=v.lower()
                if any(s+"=" in lv for s in SECRET_KEYS): issues.append("secret_query_param")
                if public_safe and ("restricted" in lv and "path" in lk): issues.append(f"restricted_path:{k}")
            scan_obj(v,issues,public_safe)
    elif isinstance(x,list):
        for i in x: scan_obj(i,issues,public_safe)

def parse(argv):
    ap=argparse.ArgumentParser(prog='kfm-ebird-observe')
    ap.add_argument('--mode',default='scan',choices=['scan','trend','attest','evidence-pack','incident-open','incident-update','incident-close','report'])
    ap.add_argument('--aggregate',default='huc12',choices=['huc12','county','both'])
    ap.add_argument('--release-index',default='data/catalog/fauna/ebird/releases/index.json')
    ap.add_argument('--release-receipt')
    ap.add_argument('--published-root',default='data/published/fauna/ebird')
    ap.add_argument('--catalog-root',default='data/catalog/fauna/ebird')
    ap.add_argument('--layer-registry-dir',default='data/published/fauna/layers')
    ap.add_argument('--history-dir',default='data/catalog/fauna/ebird/observability')
    ap.add_argument('--out-dir')
    ap.add_argument('--thresholds',default='configs/fauna/ebird/observability_thresholds.json')
    ap.add_argument('--emit-prometheus')
    ap.add_argument('--incident-id')
    ap.add_argument('--severity',choices=['info','low','medium','high','critical'])
    ap.add_argument('--summary')
    ap.add_argument('--linked-artifact',action='append',default=[])
    ap.add_argument('--dry-run',action='store_true')
    ap.add_argument('--force',action='store_true')
    return ap.parse_args(argv)

def resolve_receipt(a):
    if a.release_receipt: return Path(a.release_receipt)
    idx=Path(a.release_index)
    if not idx.exists(): fail('release-index or release-receipt must exist')
    j=load_json(idx)
    p=j.get('latest_release_receipt_path') or j.get('release_receipt_path')
    if not p: fail('release index missing release receipt path')
    return Path(p)

def main():
    a=parse(sys.argv[1:])
    if a.mode in {'scan','trend','attest','evidence-pack','report'} and not (Path(a.release_index).exists() or (a.release_receipt and Path(a.release_receipt).exists())):
        fail('release-index or release-receipt must exist')
    if a.mode=='incident-open' and (not a.severity or not a.summary): fail('incident-open requires severity and summary')
    if a.mode in {'incident-update','incident-close'} and not a.incident_id: fail('incident-id required')
    rrp=resolve_receipt(a) if a.mode in {'scan','trend','attest','evidence-pack','report','incident-open'} else None
    rr=load_json(rrp) if rrp and rrp.exists() else {}
    run_id=rr.get('run_id','unknown-run'); release_id=rr.get('release_id','unknown-release')
    out=Path(a.out_dir) if a.out_dir else Path(a.catalog_root)/'observability'/release_id
    if 'data/published' in out.as_posix() and not a.emit_prometheus: fail('out-dir must not be under data/published')
    if out.exists() and any(out.iterdir()) and not a.force and not a.dry_run: fail('out-dir exists; use --force')

    if a.dry_run:
        print(json.dumps({'status':'dry-run','mode':a.mode,'out_dir':str(out)},indent=2)); return
    out.mkdir(parents=True,exist_ok=True)

    if a.mode=='scan':
        public=Path(a.published_root)/f"ebird_agg_{'huc12' if a.aggregate=='both' else a.aggregate}.json"
        issues=[]; missing=[]; hm=[]
        if public.exists():
            pobj=load_json(public); scan_obj(pobj,issues,True)
            if rr.get('kfm:spec_hash') and pobj.get('kfm:spec_hash') and rr['kfm:spec_hash']!=pobj['kfm:spec_hash']: hm.append(str(public))
        else: missing.append(str(public))
        snap={'schema_version':'v1','object_type':'ObservabilitySnapshot','domain':'fauna','source':'ebird','release_id':release_id,'run_id':run_id,'aggregate_targets':['huc12','county'] if a.aggregate=='both' else [a.aggregate],'kfm:spec_hash':rr.get('kfm:spec_hash'),'public_safe':False,'generated_at':now()}
        integ={'schema_version':'v1','object_type':'IntegrityScanReport','release_id':release_id,'run_id':run_id,'hash_mismatches':hm,'missing_artifacts':missing,'failures':len(hm)+len(missing),'status':'pass' if not hm and not missing else 'fail'}
        ps={'schema_version':'v1','object_type':'PublicSafetyScanReport','release_id':release_id,'run_id':run_id,'issues':sorted(set(issues)),'failures':len(set(issues)),'status':'pass' if not issues else 'fail'}
        slo={'schema_version':'v1','object_type':'OperationalSLOReport','release_id':release_id,'run_id':run_id,'status':'pass' if integ['status']=='pass' and ps['status']=='pass' else 'fail','integrity_failures':integ['failures'],'public_safety_failures':ps['failures']}
        for fn,obj in [('observability_snapshot.json',snap),('integrity_scan_report.json',integ),('public_safety_scan_report.json',ps),('operational_slo_report.json',slo)]:
            (out/fn).write_text(json.dumps(obj,indent=2,sort_keys=True)+'\n')

    elif a.mode=='attest':
        sub=[]
        for p in [rrp]:
            sub.append({'path_or_uri':str(p),'sha256':sha256_file(p),'artifact_type':'release_receipt','policy_label':'public_aggregate','public_safe':True})
        att={'schema_version':'v1','object_type':'ProvenanceAttestation','domain':'fauna','source':'ebird','policy_label':'operational_attestation','public_safe':True,'exact_points':'restricted','release_id':release_id,'run_id':run_id,'aggregate_targets':['huc12','county'] if a.aggregate=='both' else [a.aggregate],'kfm:spec_hash':rr.get('kfm:spec_hash'),'suppression_min_n':rr.get('suppression_min_n'),'subject_artifacts':sub,'evidence_bundle_uri':rr.get('evidencebundle_path'),'redacted_source_uri':redact_uri(rr.get('source_uri')),'query_predicate':rr.get('query_predicate'),'validators_run':['validate_observability'],'policy_checks_run':['policy/fauna/ebird.rego'],'release_receipt_sha256':sha256_file(rrp),'generated_by':'kfm-ebird-observe','generated_at':now()}
        core=dict(att); core.pop('generated_at'); att['attestation_hash']=sha256_text(cjson(core))
        inv={'schema_version':'v1','object_type':'ArtifactHashInventory','domain':'fauna','source':'ebird','release_id':release_id,'run_id':run_id,'aggregate_targets':att['aggregate_targets'],'artifacts':[{'path_or_uri':s['path_or_uri'],'sha256':s['sha256'],'size_bytes':Path(s['path_or_uri']).stat().st_size,'artifact_type':s['artifact_type'],'policy_label':s['policy_label'],'public_safe':s['public_safe']} for s in sub],'generated_at':now()}
        (out/'provenance_attestation.json').write_text(json.dumps(att,indent=2,sort_keys=True)+'\n')
        (out/'artifact_hash_inventory.json').write_text(json.dumps(inv,indent=2,sort_keys=True)+'\n')

    if a.emit_prometheus:
        mpath=Path(a.emit_prometheus); mpath.parent.mkdir(parents=True,exist_ok=True)
        content='\n'.join([
            '# TYPE kfm_ebird_public_safety_failures_total gauge','kfm_ebird_public_safety_failures_total 0',
            '# TYPE kfm_ebird_integrity_failures_total gauge','kfm_ebird_integrity_failures_total 0'])+'\n'
        if any(x in content.lower() for x in ['source_uri','query_predicate','token=']): fail('unsafe metrics content')
        mpath.write_text(content)

if __name__=='__main__': main()
