#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from tools.validators.soil.accountability_check import main as chk

def main(argv=None):
 a=argparse.ArgumentParser();
 for n in ['accountability-root','assurance-root','registry-root','certification-root','archive-root','preservation-root','reconciliation-root','federation-root','discovery-root','published-root','ops-root']: a.add_argument('--'+n,required=True)
 x=a.parse_args(argv)
 rc=chk(['--accountability-root',x.accountability_root])
 if rc!=0: print(json.dumps({'accountability_advertising_allowed':False,'decision':'fail'})); return 1
 print(json.dumps({'accountability_advertising_allowed':True,'certificate_status':'active','decision':'pass'})); return 0
if __name__=='__main__': raise SystemExit(main())
