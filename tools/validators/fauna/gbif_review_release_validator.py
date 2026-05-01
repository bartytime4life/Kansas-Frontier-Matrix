#!/usr/bin/env python3
from __future__ import annotations
import json, hashlib
from copy import deepcopy
FORBIDDEN_FIELDS={"decimalLatitude","decimalLongitude","occurrenceLatitude","occurrenceLongitude","exact_coordinate","exactCoordinates","raw_occurrence_point","rawGbifCoordinate","site_level_location","precise_location"}
FORBIDDEN_PHRASES=["confirmed present","verified present","known population","exact location","site-level record","precise coordinates","occurrence point","raw gbif location"]

def canonicalize(v):
    if isinstance(v, dict): return {k:canonicalize(v[k]) for k in sorted(v)}
    if isinstance(v, list):
        c=[canonicalize(x) for x in v]
        if all(isinstance(x,(str,int,float,bool,type(None))) for x in c):
            return sorted(c,key=lambda x: json.dumps(x,sort_keys=True))
        return c
    return v

def stable_hash(doc,exclude=()):
    c=deepcopy(doc)
    for k in exclude: c.pop(k,None)
    b=json.dumps(canonicalize(c),sort_keys=True,separators=(",",":"))
    return 'sha256:'+hashlib.sha256(b.encode()).hexdigest()

def scan_forbidden(obj,path='$',errs=None):
    errs=errs or []
    if isinstance(obj,dict):
        for k,v in obj.items():
            if k in FORBIDDEN_FIELDS: errs.append(f'forbidden field at {path}.{k}')
            scan_forbidden(v,f'{path}.{k}',errs)
    elif isinstance(obj,list):
        for i,v in enumerate(obj): scan_forbidden(v,f'{path}[{i}]',errs)
    elif isinstance(obj,str):
        low=obj.lower()
        for p in FORBIDDEN_PHRASES:
            if p in low: errs.append(f"forbidden language '{p}' at {path}")
    return errs

import argparse
from pathlib import Path

def validate(kind,doc):
    e=scan_forbidden(doc)
    if not doc.get('kfm:spec_hash'): e.append('missing kfm:spec_hash')
    if kind in {'review_queue_item','release_registry_entry'}:
        for r in ['source_evidence_bundle_ids','download_keys']:
            if not doc.get(r): e.append(f'missing {r}')
    if kind=='release_registry_entry':
        for r in ['query_predicate_hashes','geoprivacy_receipt_refs','answer_receipt_refs']:
            if not doc.get(r): e.append(f'missing {r}')
    if kind=='review_decision_receipt' and doc.get('decision')=='approve_publish':
        rv=doc.get('reviewer',{})
        if not rv.get('actor_id'): e.append('approved decision without reviewer')
        if 'fauna_steward' not in rv.get('roles',[]): e.append('approved decision without required reviewer role')
        for c in doc.get('review_checks',[]):
            if not c.get('passed'): e.append(f"approved decision failed check {c.get('check_name')}")
    if kind=='release_registry_entry' and doc.get('release_state')=='published':
        if not doc.get('review_decision_receipt_id'): e.append('release registry entry without review_decision_receipt_id')
        if doc.get('rights_posture')!='public_allowed': e.append('rights_posture not public_allowed for public release')
        if doc.get('sensitivity_posture')=='restricted': e.append('restricted sensitivity for public release')
        if doc.get('presence_posture')!='reported_occurrence_not_confirmed_presence': e.append('invalid presence_posture')
    if kind=='public_manifest':
        if not doc.get('citation_index'): e.append('public manifest without citation_index')
    if kind=='release_gate_result' and doc.get('gate_posture')=='passed':
        if any(not c.get('passed') for c in doc.get('checks',[])): e.append('release gate marked passed while check failed')
    return e

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--kind',required=True,choices=['review_queue_item','review_decision_receipt','exception_receipt','release_registry_entry','public_manifest','release_gate_result'])
    ap.add_argument('--input',required=True)
    a=ap.parse_args()
    doc=json.loads(Path(a.input).read_text())
    errs=validate(a.kind,doc)
    if errs: print('\n'.join(errs)); raise SystemExit(1)
    print('ok')

if __name__=='__main__': main()
