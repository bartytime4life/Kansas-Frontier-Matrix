#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
FORBIDDEN=["confirmed present","verified present"]

def has_coords(obj):
    t=json.dumps(obj).lower(); return 'decimallatitude' in t or 'decimallongitude' in t

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--catalog');ap.add_argument('--claims');ap.add_argument('--answer');a=ap.parse_args();errs=[]
    if a.catalog:
        for e in json.loads(Path(a.catalog).read_text()):
            if not e.get('source_evidence_bundle_id'): errs.append('catalog missing source_evidence_bundle_id')
            if not e.get('download_key'): errs.append('catalog missing download_key')
            if not e.get('geoprivacy_receipt_refs'): errs.append('catalog missing geoprivacy_receipt_refs')
            if e.get('release_posture') in {'public_candidate','published'} and e.get('rights_posture')!='public_allowed': errs.append('catalog rights invalid')
            if e.get('release_posture') in {'public_candidate','published'} and e.get('sensitivity_posture')=='restricted': errs.append('catalog sensitivity invalid')
    if a.claims:
        for c in json.loads(Path(a.claims).read_text()):
            if not c.get('evidence'): errs.append('missing evidence block')
            if not c.get('kfm:spec_hash'): errs.append('missing kfm:spec_hash')
            text=(c.get('claim_text','')+' '+json.dumps(c)).lower()
            if any(w in text for w in FORBIDDEN): errs.append('forbidden confirmed presence language')
    if a.answer:
        an=json.loads(Path(a.answer).read_text())
        if an.get('claims') and any(not c.get('citations') for c in an.get('claims',[])): errs.append('claims without citations')
        if has_coords(an): errs.append('exact coordinates exposed')
        if an.get('query',{}).get('exact_coordinates_requested') and an.get('answer_posture')!='abstain': errs.append('must abstain exact coordinates')
    if errs:
        print('\n'.join(errs)); raise SystemExit(1)

if __name__=='__main__':main()
