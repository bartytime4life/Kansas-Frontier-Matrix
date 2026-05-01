import argparse, json
from pathlib import Path
ap=argparse.ArgumentParser(); ap.add_argument('--decision',required=True); ap.add_argument('--out_dir',required=True); a=ap.parse_args()
d=json.loads(Path(a.decision).read_text()); o=Path(a.out_dir); o.mkdir(parents=True,exist_ok=True); p=o/f"{d['decision_id']}.json"; p.write_text(json.dumps(d,indent=2,sort_keys=True)); print(p)
