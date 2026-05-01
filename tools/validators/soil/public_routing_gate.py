import argparse,subprocess,sys,json

def main(argv=None):
 p=argparse.ArgumentParser()
 for n in ['routing','active','lineage','outcome','remediation','corrective','resolution','accountability','assurance','registry','certification','archive','preservation','reconciliation','federation','discovery','published','ops']:
  p.add_argument(f'--{n}-root',required=True)
 a=p.parse_args(argv)
 r=subprocess.run([sys.executable,'tools/validators/soil/public_routing_check.py','--routing-root',a.routing_root],capture_output=True,text=True)
 if r.returncode!=0: print(r.stdout.strip()); return 1
 d=json.loads(r.stdout)
 print(json.dumps({'public_routing_advertising_allowed':True,'prior_release_id':d.get('prior_release_id'),'active_release_id':d.get('active_release_id'),'routing_id':d.get('routing_id'),'routing_state':d.get('routing_state'),'decision':'pass'})); return 0
if __name__=='__main__': raise SystemExit(main())
