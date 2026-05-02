#!/usr/bin/env python3
from __future__ import annotations
import datetime, hashlib, json, os, re, shutil
from pathlib import Path
from typing import Any, Dict, List, Optional

SOURCE="soilgrids_data_use_accountability"
DEFAULT_MODE="full"
ALLOWED_MODES={"plan-only","inventory-usage","meter-usage","evaluate-obligations","quota-check","anomaly-scan","consumer-statement","full","local-api","dry-run"}
EXIT={"success":0,"planned":0,"dry":5,"warning":10,"compliance":20,"malformed":30,"ledger":40,"meter":50,"obligation":60,"quota":70,"anomaly":80,"api":90,"unsafe":100,"secret":110,"internal":120}
SECRET_PATTERNS=[re.compile(r"AKIA[0-9A-Z]{16}"),re.compile(r"-----BEGIN (?:RSA|EC|OPENSSH) PRIVATE KEY-----")]
KNOWN_PROFILES={"strict","standard","relaxed"}


def _utc_now()->str:return datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
def _canon_obj(obj:Any)->bytes:return json.dumps(obj,sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()
def _sha_obj(obj:Any)->str:return hashlib.sha256(_canon_obj(obj)).hexdigest()
def _read_json(p:str|Path)->Dict[str,Any]:return json.loads(Path(p).read_text(encoding='utf-8'))
def write_canonical_json(path:Path,obj:Any)->None:path.parent.mkdir(parents=True,exist_ok=True);path.write_text(json.dumps(obj,sort_keys=True,indent=2)+"\n",encoding='utf-8')

def _scan_secret(v:Any)->bool:
    s=json.dumps(v,sort_keys=True) if not isinstance(v,str) else v
    return any(p.search(s) for p in SECRET_PATTERNS)

def validate_data_use_spec(spec:Dict[str,Any],allow_plaintext_subjects=False,allow_unvalidated_ledger=False)->List[str]:
    e=[]
    if spec.get('schema')!='DataUseSpec.v1': e.append('schema')
    for k in ('data_use_id','dataset_id'):
        if not spec.get(k): e.append(k)
    if spec.get('accountability_profile') and spec['accountability_profile'] not in KNOWN_PROFILES: e.append('accountability_profile')
    if spec.get('usage_sources',{}).get('require_usage_audit_ledger_valid') is False and not allow_unvalidated_ledger: e.append('require_usage_audit_ledger_valid')
    allowed=set(spec.get('obligations',{}).get('allowed_purposes',[])); denied=set(spec.get('obligations',{}).get('denied_purposes',[]))
    if allowed & denied: e.append('purpose_policy_conflict')
    for sec,keys in ((spec.get('quotas',{}),('default_subject_daily_events','default_subject_daily_bytes','default_resource_daily_events')),(spec.get('anomaly_detection',{}),('burst_event_threshold','burst_window_minutes','denial_rate_warning_percent','blocked_access_critical_threshold'))):
        for k in keys:
            if k in sec and (not isinstance(sec[k],int) or sec[k]<0): e.append(k)
    if spec.get('privacy',{}).get('forbid_plaintext_subjects') is not True and not allow_plaintext_subjects: e.append('forbid_plaintext_subjects')
    return e

def validate_usage_audit_event(event:Dict[str,Any],allow_unknown_action=False,allow_plaintext_subjects=False,require_redaction=True)->List[str]:
    e=[]
    if event.get('schema')!='UsageAuditEvent.v1': e.append('schema')
    for k in ('event_id','event_hash','enforcement_action','action'):
        if not event.get(k): e.append(k)
    subj=event.get('subject',{})
    if require_redaction and subj and subj.get('redacted') is not True: e.append('subject.redacted')
    if subj.get('subject_id') and not allow_plaintext_subjects: e.append('subject_id')
    if _scan_secret(event): e.append('secret')
    if event.get('action') and event['action'] not in {'read','download','view','embed','cite','analyze','audit'} and not allow_unknown_action: e.append('unknown_action')
    body={k:v for k,v in event.items() if k!='event_hash'}
    if event.get('event_hash') and _sha_obj(body)!=event['event_hash']: e.append('event_hash')
    return e

def validate_usage_audit_ledger(ledger:Dict[str,Any],events:List[Dict[str,Any]],allow_broken=False,allow_plaintext_subjects=False)->List[str]:
    e=[]
    if ledger.get('schema')!='UsageAuditLedger.v1': e.append('schema')
    ids=set(); eids=set(); prev=None
    for en in ledger.get('entries',[]):
        if en.get('entry_id') in ids: e.append('duplicate_entry_id')
        ids.add(en.get('entry_id'))
        if en.get('event_id') in eids: e.append('duplicate_event_id')
        eids.add(en.get('event_id'))
        calc=_sha_obj({'entry_id':en.get('entry_id'),'event_id':en.get('event_id'),'previous_chain_hash':prev})
        if en.get('chain_hash')!=calc: e.append('chain_hash')
        prev=en.get('chain_hash')
    for ev in events: e.extend(validate_usage_audit_event(ev,allow_plaintext_subjects=allow_plaintext_subjects))
    if e and not allow_broken: e.append('broken')
    return sorted(set(e))

def classify_usage_event(event:Dict[str,Any])->Dict[str,Any]: return {'event_id':event['event_id'],'event_hash':event['event_hash'],'subject_hash':event.get('subject',{}).get('subject_hash'),'action':event.get('action'),'enforcement_action':event.get('enforcement_action'),'purpose':event.get('purpose'),'bytes_served':int(event.get('bytes_served') or 0),'resource_sha256':event.get('resource_sha256'),'event_time_utc':event.get('event_time_utc')}

def build_usage_event_inventory(spec,events):
    rows=sorted([classify_usage_event(e) for e in events],key=lambda r:((r.get('event_time_utc') or ''),r['event_id']))
    inv={'schema':'UsageEventInventory.v1','data_use_id':spec['data_use_id'],'events':rows,'summary':{'events_total':len(rows),'grants':sum(1 for r in rows if str(r['enforcement_action']).startswith('grant')),'denials':sum(1 for r in rows if r['enforcement_action']=='deny'),'reviews':sum(1 for r in rows if r['enforcement_action']=='review_required'),'unique_subjects':len({r.get('subject_hash') for r in rows if r.get('subject_hash')})},'created_at_utc':_utc_now()}
    inv['inventory_hash']=_sha_obj({k:v for k,v in inv.items() if k not in {'created_at_utc','inventory_hash'}});return inv

def build_usage_metering_snapshot(spec,inv):
    events=inv['events']
    snap={'schema':'UsageMeteringSnapshot.v1','data_use_id':spec['data_use_id'],'time_window':{'start_utc':events[0]['event_time_utc'] if events else None,'end_utc':events[-1]['event_time_utc'] if events else None},'counters':{'events_total':len(events),'grant_events':sum(1 for e in events if str(e['enforcement_action']).startswith('grant')),'denial_events':sum(1 for e in events if e['enforcement_action']=='deny'),'review_events':sum(1 for e in events if e['enforcement_action']=='review_required'),'bytes_served_total':sum(e['bytes_served'] for e in events)},'by_subject':sorted(list({e.get('subject_hash') for e in events})),'by_action':sorted(list({e.get('action') for e in events})),'by_resource':sorted(list({e.get('resource_sha256') for e in events})),'created_at_utc':_utc_now()}
    snap['metering_snapshot_hash']=_sha_obj({k:v for k,v in snap.items() if k not in {'created_at_utc','metering_snapshot_hash'}});return snap

def main(argv:Optional[List[str]]=None)->int:
    import argparse
    ap=argparse.ArgumentParser()
    ap.add_argument('--data-use-spec'); ap.add_argument('--output-root'); ap.add_argument('--mode',required=True)
    ap.add_argument('--usage-audit-ledger',action='append',default=[]); ap.add_argument('--usage-audit-event',action='append',default=[])
    ap.add_argument('--data-use-policy'); ap.add_argument('--allow-broken-usage-ledger',action='store_true'); ap.add_argument('--allow-unvalidated-ledger',action='store_true'); ap.add_argument('--allow-unknown-action',action='store_true'); ap.add_argument('--allow-plaintext-subjects',action='store_true'); ap.add_argument('--allow-public-bind',action='store_true'); ap.add_argument('--host',default='127.0.0.1'); ap.add_argument('--serve-forever',action='store_true'); ap.add_argument('--deterministic-run-id',action='store_true')
    a=ap.parse_args(argv)
    try:
        spec=_read_json(a.data_use_spec) if a.data_use_spec else None
        if not spec:
            os.sys.stderr.write(json.dumps({'status':'error','error_count':1,'data_use_receipt_path':None,'data_use_run_id':None})+'\n'); return EXIT['malformed']
        se=validate_data_use_spec(spec,a.allow_plaintext_subjects,a.allow_unvalidated_ledger)
        if se:
            os.sys.stderr.write(json.dumps({'status':'error','error_count':len(se),'data_use_receipt_path':None,'data_use_run_id':None})+'\n'); return EXIT['malformed']
        if a.host=='0.0.0.0' and not a.allow_public_bind: return EXIT['unsafe']
        out=Path(a.output_root); out.mkdir(parents=True,exist_ok=True); rid='deterministic' if a.deterministic_run_id else _sha_obj(spec)[:12]; run=out/rid; run.mkdir(parents=True,exist_ok=True)
        receipt=run/'data_use_receipt.json'; write_canonical_json(receipt,{'schema':'DataUseReceipt.v1','data_use_run_id':rid})
        os.sys.stdout.write(str(receipt)+'\n')
        return EXIT['dry'] if a.mode=='dry-run' else EXIT['success']
    except Exception:
        os.sys.stderr.write(json.dumps({'status':'error','error_count':1,'data_use_receipt_path':None,'data_use_run_id':None})+'\n'); return EXIT['internal']

if __name__=='__main__': raise SystemExit(main())
