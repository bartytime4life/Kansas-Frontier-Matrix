import argparse, json
from pathlib import Path

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--manifest',required=True); ap.add_argument('--decisions',required=True); a=ap.parse_args()
    m=json.loads(Path(a.manifest).read_text()); d={json.loads(p.read_text())['decision_id']:json.loads(p.read_text()) for p in Path(a.decisions).glob('*.json')}
    reasons=[]
    for art in m.get('artifacts',[]):
        if art.get('release_channel') in {'public','export'}:
            ok=False
            for i in m.get('decision_envelope_ids',[]):
                dec=d.get(i)
                if dec and dec.get('subject_artifact_id')==art.get('artifact_id') and dec.get('decision')=='allow': ok=True
            if not ok: reasons.append(f"artifact {art.get('artifact_id')} missing allow decision")
    print(json.dumps({'ok': not reasons, 'reasons': reasons}))
if __name__=='__main__': main()
