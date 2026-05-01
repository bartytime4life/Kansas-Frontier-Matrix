#!/usr/bin/env python3
import argparse, base64, copy, hashlib, json, re, sys
from datetime import datetime, timezone
from pathlib import Path
from jsonschema import Draft202012Validator

DIGEST_RE=re.compile(r'^sha256:[a-f0-9]{64}$')
FORBIDDEN_RE=re.compile(r'(/RAW/|/WORK/|/QUARANTINE/|raw://|work://|quarantine://)',re.IGNORECASE)


def cj(obj): return json.dumps(obj,sort_keys=True,separators=(',',':'),ensure_ascii=False)
def sha(b): return 'sha256:'+hashlib.sha256(b).hexdigest()
def hash_manifest(m): return sha(cj(m).encode())
def fail(msg): print(f'FAIL: {msg}'); return False

def load_json(p): return json.loads(Path(p).read_text(encoding='utf-8'))

def validate_manifest_schema(manifest):
    schema=load_json('contracts/kfm/delta_manifest.v1.json')
    errs=[]
    for e in Draft202012Validator(schema).iter_errors(manifest):
        errs.append(f"schema {'.'.join(map(str,e.path)) or '<root>'}: {e.message}")
    return errs

def tile_key(t): return f"{t['z']}/{t['x']}/{t['y']}"

def verify(manifest, base, delta, ledger, refs):
    checks=[]; rejected=[]
    def chk(name, ok, msg=''):
        checks.append({'name':name,'result':'PASS' if ok else 'FAIL', **({'message':msg} if msg else {})})
        if not ok: rejected.append(name)
        return ok

    errs=validate_manifest_schema(manifest)
    chk('manifest_schema', not errs, '; '.join(errs))
    mhash=hash_manifest(manifest)
    chk('manifest_hash_present', bool(mhash and DIGEST_RE.match(mhash)))
    chk('base_spec_hash_present', bool(manifest.get('base_pmtiles',{}).get('spec_hash')))

    def _strings(x):
        if isinstance(x,str):
            yield x
        elif isinstance(x,dict):
            for v in x.values():
                yield from _strings(v)
        elif isinstance(x,list):
            for v in x:
                yield from _strings(v)
    all_refs=list(_strings(manifest))+list(_strings(refs))
    chk('no_forbidden_refs', not any(FORBIDDEN_RE.search(r) for r in all_refs), 'forbidden RAW/WORK/QUARANTINE ref')

    tiles=manifest.get('tiles',[])
    chk('produced_tile_count', manifest.get('produced_tile_count')==len(tiles))
    uniq=len({tile_key(t) for t in tiles})==len(tiles)
    chk('unique_tile_keys',uniq)
    chk('tile_fields_present', all(all(k in t for k in ('tile_id','z','x','y','quadkey','run_receipt_url')) and str(t.get('run_receipt_url','')).strip() for t in tiles))
    rt=manifest.get('qc',{}).get('masked_pct_review_threshold')
    chk('masked_pct_threshold', all(float(t.get('masked_pct',0))<=float(rt) for t in tiles if rt is not None))

    base_spec=base.get('metadata',{}).get('kfm:spec_hash')
    chk('base_spec_hash_match', base_spec==manifest.get('base_pmtiles',{}).get('spec_hash'))

    entries=ledger.get('applied_deltas',[])
    byid={e.get('delta_id'):e for e in entries}
    prior=byid.get(manifest.get('delta_id'))
    chk('replay_mismatch', not(prior and prior.get('manifest_hash')!=mhash))
    if entries:
        latest=max(e.get('time_end','') for e in entries)
        chk('time_order', manifest.get('time_end','')>=latest)

    base_tiles=base.get('tiles',{})
    delta_tiles=delta.get('tiles',{})
    for t in tiles:
        k=tile_key(t); c=t['change_type']
        if c=='added':
            ok=t.get('prior_digest') is None and k not in base_tiles and k in delta_tiles and sha(base64.b64decode(delta_tiles[k]['content_b64']))==t['digest']
            chk(f'added_{k}',ok)
        elif c=='modified':
            ok=t.get('prior_digest') is not None and k in base_tiles and base_tiles[k].get('digest')==t['prior_digest'] and k in delta_tiles and sha(base64.b64decode(delta_tiles[k]['content_b64']))==t['digest']
            chk(f'modified_{k}',ok)
        elif c=='removed':
            tid=int(t['tile_id']) if str(t.get('tile_id','')).isdigit() else t['tile_id']; tomb={"change_type":"removed","tile_id":tid,"x":t['x'],"y":t['y'],"z":t['z']}
            ok=t.get('prior_digest') is not None and k in base_tiles and base_tiles[k].get('digest')==t['prior_digest'] and sha(cj(tomb).encode())==t['digest']
            chk(f'removed_{k}',ok)
        else:
            chk(f'change_type_{k}',False)

    ok=all(c['result']=='PASS' for c in checks)
    return ok,mhash,checks,rejected

def build_receipt(result,manifest,mhash,base_spec,refs,out,checks,rejected):
    tiles=manifest['tiles'];
    return {
      'receipt_version':'v1','result':'PASS' if result else 'FAIL','delta_id':manifest['delta_id'],'manifest_hash':mhash,
      'base_spec_hash':base_spec,'time_start':manifest['time_start'],'time_end':manifest['time_end'],'applied_at':datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z'),
      'changed_tile_count':len(tiles),'added_count':sum(1 for t in tiles if t['change_type']=='added'),'modified_count':sum(1 for t in tiles if t['change_type']=='modified'),'removed_count':sum(1 for t in tiles if t['change_type']=='removed'),
      'input_refs':refs,'output_refs':{'out_store':out},'checks':checks,'rejected_checks':rejected,'tool':{'name':'kfm_delta_apply','version':'v1'}
    }

def cmd_verify(a):
    refs={'manifest':a.manifest,'base_store':a.base_store,'delta_store':a.delta_store,'ledger':a.ledger}
    m,b,d,l=map(load_json,[a.manifest,a.base_store,a.delta_store,a.ledger])
    ok,mh,checks,rej=verify(m,b,d,l,refs)
    print('PASS: verification passed' if ok else 'FAIL: verification failed')
    return 0 if ok else 1

def cmd_apply(a):
    refs={'manifest':a.manifest,'base_store':a.base_store,'delta_store':a.delta_store,'ledger':a.ledger}
    m,b,d,l=map(load_json,[a.manifest,a.base_store,a.delta_store,a.ledger])
    ok,mh,checks,rej=verify(m,b,d,l,refs)
    receipt=build_receipt(ok,m,mh,b.get('metadata',{}).get('kfm:spec_hash'),refs,a.out_store,checks,rej)
    Path(a.receipt).write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
    if not ok:
        print('FAIL: apply aborted')
        return 1
    out=copy.deepcopy(b)
    for t in m['tiles']:
        k=tile_key(t)
        if t['change_type']=='removed': out.get('tiles',{}).pop(k,None)
        else:
            payload=d['tiles'][k]
            out['tiles'][k]={'tile_id':t['tile_id'],'digest':t['digest'],'content_b64':payload['content_b64']}
    out.setdefault('metadata',{})['kfm:spec_hash']=m['base_pmtiles']['spec_hash']
    out['metadata']['last_delta_id']=m['delta_id']; out['metadata']['last_manifest_hash']=mh; out['metadata']['time_end']=m['time_end']
    out.setdefault('applied_deltas',[])
    if not any(e.get('delta_id')==m['delta_id'] and e.get('manifest_hash')==mh for e in out['applied_deltas']):
      out['applied_deltas'].append({'delta_id':m['delta_id'],'manifest_hash':mh,'time_end':m['time_end']})
    Path(a.out_store).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print('PASS: apply succeeded')
    return 0

def main():
    p=argparse.ArgumentParser(); sp=p.add_subparsers(dest='cmd',required=True)
    for n in ('verify','apply'):
      s=sp.add_parser(n); s.add_argument('--manifest',required=True); s.add_argument('--base-store',required=True); s.add_argument('--delta-store',required=True); s.add_argument('--ledger',required=True)
      if n=='apply': s.add_argument('--out-store',required=True); s.add_argument('--receipt',required=True)
    h=sp.add_parser('hash'); h.add_argument('--manifest',required=True)
    a=p.parse_args()
    if a.cmd=='verify': return cmd_verify(a)
    if a.cmd=='apply': return cmd_apply(a)
    print(hash_manifest(load_json(a.manifest))); return 0

if __name__=='__main__': sys.exit(main())
