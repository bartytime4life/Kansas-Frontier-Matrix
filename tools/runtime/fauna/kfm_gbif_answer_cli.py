#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT))
from tools.runtime.fauna.kfm_gbif_answer_service import build_answer,with_spec_hash,now_iso

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--claims',required=True); ap.add_argument('--query'); ap.add_argument('--query-type'); ap.add_argument('--query-id',default='query_cli_001'); ap.add_argument('--taxon-key'); ap.add_argument('--scientific-name',default='Testus exampleus'); ap.add_argument('--geography-id'); ap.add_argument('--aggregation-unit',default='county'); ap.add_argument('--include-ui-cards',action='store_true'); ap.add_argument('--include-geometry',action='store_true'); ap.add_argument('--output',required=True); ap.add_argument('--receipt-output',required=True)
    a=ap.parse_args()
    claims=json.loads(Path(a.claims).read_text())
    if a.query: query=json.loads(Path(a.query).read_text())
    else:
        if not a.query_type: return 2
        query=with_spec_hash({"query_id":a.query_id,"query_type":a.query_type,"taxon_key":a.taxon_key,"scientific_name":a.scientific_name,"geography_id":a.geography_id,"aggregation_unit":a.aggregation_unit,"request_public":True,"include_geometry":a.include_geometry,"include_ui_cards":a.include_ui_cards,"created_at":now_iso()},{"query_id"})
    answer,receipt=build_answer(claims,query)
    Path(a.output).write_text(json.dumps(answer,indent=2)); Path(a.receipt_output).write_text(json.dumps(receipt,indent=2))
    print(f"{answer['answer_posture']}:{answer.get('abstain_reason')}")
    return 0
if __name__=='__main__': raise SystemExit(main())
