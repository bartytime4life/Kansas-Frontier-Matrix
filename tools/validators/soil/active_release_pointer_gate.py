import argparse,subprocess,sys,json

def main():
 p=argparse.ArgumentParser();
 for n in ['active','lineage','outcome','remediation','corrective','resolution','accountability','assurance','registry','certification','archive','preservation','reconciliation','federation','discovery','published','ops']:
  p.add_argument(f'--{n}-root',required=True)
 a=p.parse_args()
 r=subprocess.run([sys.executable,'tools/validators/soil/active_release_pointer_check.py','--active-root',a.active_root],capture_output=True,text=True)
 if r.returncode!=0: print(r.stdout.strip() or json.dumps({'active_release_pointer_advertising_allowed':False})); sys.exit(1)
 d=json.loads(r.stdout)
 print(json.dumps({"active_release_pointer_advertising_allowed":True,"prior_release_id":d.get('prior_release_id'),"active_release_id":d.get('active_release_id'),"pointer_transition_id":d.get('pointer_transition_id'),"pointer_state":d.get('pointer_state'),"decision":"pass"}))
if __name__=='__main__': main()
