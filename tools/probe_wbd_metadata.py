import argparse, hashlib, json, os
from pathlib import Path

DENY_TOKENS = ['/query','/export','/identify','/tile','/FeatureServer/query','f=geojson','returnGeometry=true','outFields=*','objectIds','geometry=','where=']

def decision_for_env():
    if os.getenv('KFM_ALLOW_NETWORK') != '1' or os.getenv('KFM_SOURCE_PROBE') != 'SRC-HYD-WBD-CANDIDATE' or os.getenv('KFM_PROBE_KIND') != 'METADATA_ONLY':
        return 'ABSTAIN', 'network/env gate disabled'
    return 'PASS', 'env gates satisfied (real probe not executed in this baseline)'

def main():
    parser=argparse.ArgumentParser(); parser.add_argument('--dry-run',action='store_true'); parser.add_argument('--source-id',default='SRC-HYD-WBD-CANDIDATE'); args=parser.parse_args()
    outcome,reason=decision_for_env()
    if args.dry_run: outcome='ABSTAIN'; reason='dry-run mode'
    receipt={'receipt_id':'SPR-WBD-DRYRUN-001','source_id':args.source_id,'probe_kind':'METADATA_ONLY','validation_result':outcome,'response_summary':reason,'response_body_stored':False,'no_ingestion_assertion':True}
    print(outcome, reason)
    print(json.dumps(receipt, sort_keys=True))
    return 0
if __name__=='__main__': raise SystemExit(main())
