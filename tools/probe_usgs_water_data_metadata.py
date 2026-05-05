import argparse,os

def main():
 p=argparse.ArgumentParser();p.add_argument('--dry-run',action='store_true');p.add_argument('--source-id',default='SRC-HYD-USGS-WATERDATA-CANDIDATE');a=p.parse_args()
 if a.dry_run or os.getenv('KFM_ALLOW_NETWORK')!='1' or os.getenv('KFM_SOURCE_METADATA_PROBE')!='SRC-HYD-USGS-WATERDATA-CANDIDATE' or os.getenv('KFM_METADATA_PROBE_KIND')!='OFFICIAL_METADATA_ONLY':
  print('ABSTAIN metadata probe not run (network/env disabled)'); return 0
 print('PASS env gates satisfied (live metadata not executed)'); return 0
if __name__=='__main__': raise SystemExit(main())
