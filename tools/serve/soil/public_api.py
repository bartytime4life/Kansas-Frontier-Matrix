#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, signal, hashlib
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlparse
from tools.audit.soil._published_common import load_json, sanitize_id, is_retracted
from tools.serve.soil._service_common import validate_service_release, public_safe_payload, scan_payload_for_forbidden_terms, sha256_bytes

class H(BaseHTTPRequestHandler):
    def _write(self, status:int, payload:object, ctype='application/json'):
        data = payload if isinstance(payload,bytes) else json.dumps(payload,sort_keys=True).encode()
        self.send_response(status); self.send_header('Content-Type',ctype)
        self.send_header('X-KFM-Domain','soil'); self.send_header('X-KFM-State','PUBLISHED')
        self.send_header('X-KFM-Release-ID',self.server.release_id); self.send_header('X-KFM-Audit-Passed','true')
        self.send_header('ETag',sha256_bytes(data)); self.end_headers(); self.wfile.write(data)
        if getattr(self.server,'access_log',None):
            path=urlparse(self.path).path
            rt=path
            if path.startswith('/soil/records/'): rt='/soil/records/{id}'
            if path.startswith('/soil/focus-cards/'): rt='/soil/focus-cards/{safe_bundle_id}'
            if path.startswith('/soil/triplets/'): rt='/soil/triplets/{safe_bundle_id}.nt'
            e={'schema_version':'kfm.v1','object_type':'SoilPublicApiAccessLogEntry','created':'','method':'GET','route_template':rt,'status':status,'release_id':self.server.release_id,'response_bytes':len(data),'request_id':hashlib.sha256((self.path+str(status)).encode()).hexdigest()[:16]}
            lp=Path(self.server.access_log); lp.parent.mkdir(parents=True,exist_ok=True)
            with lp.open('a',encoding='utf-8') as f: f.write(json.dumps(e,sort_keys=True)+'\n')
    def _err(self,status,reason): self._write(status,{"error":True,"status":status,"reason":reason})
    def do_GET(self):
        rel=self.server.release_root; rid=self.server.release_id
        u=urlparse(self.path); path=u.path; q=parse_qs(u.query)
        if '..' in path: return self._err(400,'malformed path')
        if path=='/health': return self._write(200,{"status":"ok","domain":"soil","state":"PUBLISHED","release_id":rid,"audit_passed":True})
        if path=='/openapi.json':
            p=Path('schemas/openapi/soil_public_api.openapi.json'); return self._write(200,load_json(p) if p.exists() else {"openapi":"3.0.3","info":{"title":"KFM Soil Public API","version":"v1"},"paths":{}})
        if path=='/soil/current':
            c=public_safe_payload(load_json(self.server.published_root/'published/soil/current.json')); c['publication_status']='PUBLISHED'; return self._write(200,c)
        if path=='/soil/releases':
            ids=sorted([p.name for p in (self.server.published_root/'published/soil/releases').iterdir() if p.is_dir()]); ids=[x for x in ids if not is_retracted(self.server.published_root,x)]; return self._write(200,{"release_ids":ids})
        if path.startswith('/soil/releases/') and path.endswith('/manifest'):
            x=unquote(path.split('/')[3]);
            if sanitize_id(x)!=x: return self._err(400,'malformed release_id')
            if is_retracted(self.server.published_root,x): return self._err(410,'release retracted')
            return self._write(200, public_safe_payload(load_json(self.server.published_root/f'published/soil/releases/{x}/manifest.json')))
        if path.startswith('/soil/releases/') and path.endswith('/publication-receipt'):
            x=unquote(path.split('/')[3]);
            if sanitize_id(x)!=x: return self._err(400,'malformed release_id')
            return self._write(200, public_safe_payload(load_json(self.server.published_root/f'published/soil/releases/{x}/publication_receipt.json')))
        idx=load_json(rel/'index.json'); records=idx.get('records',[])
        if path=='/soil/records':
            try:
                limit=int(q.get('limit',[str(len(records))])[0]); offset=int(q.get('offset',['0'])[0]);
                if limit<0 or offset<0: raise ValueError
            except Exception: return self._err(400,'invalid limit/offset')
            rows=sorted(records,key=lambda r:r.get('bundle_id',''))
            if 'source' in q: rows=[r for r in rows if r.get('source')==q['source'][0]]
            if 'aggregation' in q: rows=[r for r in rows if r.get('aggregation')==q['aggregation'][0]]
            return self._write(200,{"object_type":"SoilPublicReadModel","records":rows[offset:offset+limit]})
        if path.startswith('/soil/records/'):
            x=unquote(path.split('/')[3]);
            if not x or '..' in x: return self._err(400,'malformed id')
            for r in records:
                if r.get('bundle_id')==x or sanitize_id(r.get('bundle_id',''))==x: return self._write(200,r)
            return self._err(404,'record not found')
        if path.startswith('/soil/focus-cards/'):
            sid=unquote(path.split('/')[3]);
            if sid!=sanitize_id(sid): return self._err(400,'malformed id')
            p=rel/'focus_cards'/f'{sid}.json'
            if not p.exists(): return self._err(404,'focus card not found')
            c=load_json(p)
            if c.get('provisional') is not False or c.get('status')!='PUBLISHED': return self._err(503,'focus card not publishable')
            return self._write(200,c)
        if path.startswith('/soil/triplets/') and path.endswith('.nt'):
            sid=path.split('/')[3][:-3]
            if sid!=sanitize_id(sid): return self._err(400,'malformed id')
            p=rel/'triplets'/f'{sid}.nt'
            if not p.exists(): return self._err(404,'triplets not found')
            return self._write(200,p.read_bytes(),'application/n-triples')
        if path=='/soil/governance/retractions':
            rdir=self.server.published_root/'published/soil/retractions'; items=[]
            if rdir.exists():
                for p in sorted(rdir.glob('*.retraction_notice.json')): items.append(public_safe_payload(load_json(p)))
            return self._write(200,{"retractions":items})
        if path=='/soil/discovery' and getattr(self.server,'discovery_root',None):
            from tools.validators.soil.discovery_check import main as dchk
            if dchk(['--discovery-root',self.server.discovery_root])!=0: return self._err(503,'discovery invalid')
            d=Path(self.server.discovery_root)/'discovery/soil';ptr=load_json(d/'current_discovery.json');rid=ptr['active_discovery_id'];return self._write(200,load_json(d/f'releases/{rid}/discovery_manifest.json'))
        if path in ['/soil/discovery/schema.org','/soil/discovery/dcat','/soil/discovery/stac-collection','/soil/discovery/feed.json','/soil/discovery/sitemap.xml','/soil/discovery/robots.txt'] and getattr(self.server,'discovery_root',None):
            d=Path(self.server.discovery_root)/'discovery/soil';ptr=load_json(d/'current_discovery.json');did=ptr['active_discovery_id'];m={'/soil/discovery/schema.org':'landing.schemaorg.jsonld','/soil/discovery/dcat':'dcat.dataset.jsonld','/soil/discovery/stac-collection':'stac_collection.json','/soil/discovery/feed.json':'feeds/soil.json','/soil/discovery/sitemap.xml':'sitemap.xml','/soil/discovery/robots.txt':'robots.txt'}
            fp=d/f'releases/{did}/{m[path]}'
            ct='application/json' if path.endswith('json') or 'schema.org' in path or 'dcat' in path else ('application/xml' if path.endswith('.xml') else 'text/plain')
            return self._write(200, fp.read_text(), ct)
        
        if path.startswith('/soil/certification') and getattr(self.server,'certification_root',None):
            croot=Path(self.server.certification_root)/'certification/soil'
            ptr=load_json(croot/'current_certification.json'); cid=ptr['active_certification_id']; cdir=croot/'certifications'/cid
            mapping={'/soil/certification':'public_trust_report.json','/soil/certification/manifest':'certification_manifest.json','/soil/certification/control-matrix':'control_matrix.json','/soil/certification/audit-dossier':'audit_dossier.json','/soil/certification/receipt-chain':'receipt_chain.json','/soil/certification/provenance-lineage':'provenance_lineage.jsonld','/soil/certification/dataset-bom':'dataset_bill_of_materials.json','/soil/certification/risk-register':'risk_register.json','/soil/certification/exception-ledger':'exception_ledger.json','/soil/certification/public-trust-report':'public_trust_report.json','/soil/certification/receipt':'certification_receipt.json'}
            if path in mapping:
                payload=load_json(cdir/mapping[path])
                self.send_header('X-KFM-State','TRUST_CERTIFIED')
                return self._write(200,payload)

        if path=='/soil/governance/status':
            st={"release_id":rid,"audit_passed":True,"retracted":False,"public_access_allowed":True,"policy_checks":load_json(rel/'publication_receipt.json').get('policy_checks',{})}
            if getattr(self.server,'ops_root',None):
                sp=Path(self.server.ops_root)/'ops/soil/status/current_status.json'
                if sp.exists():
                    cs=load_json(sp); st.update({'operational_status_ref':str(sp),'service_state':cs.get('service_state'),'latest_probe_id':cs.get('latest_probe_id'),'active_incident_count':len(cs.get('active_incidents',[])),'scheduled_maintenance_count':len(cs.get('scheduled_maintenance',[])),'public_access_allowed':cs.get('public_access_allowed',True)})
            return self._write(200,st)
        
        if getattr(self.server,'access_log',None):
            rt=path
            if path.startswith('/soil/records/'): rt='/soil/records/{id}'
            if path.startswith('/soil/focus-cards/'): rt='/soil/focus-cards/{safe_bundle_id}'
            if path.startswith('/soil/triplets/'): rt='/soil/triplets/{safe_bundle_id}.nt'
        return self._err(404,'not found')

def main(argv=None):
    ap=argparse.ArgumentParser(); ap.add_argument('--published-root',required=True); ap.add_argument('--release-id'); ap.add_argument('--host',default='127.0.0.1'); ap.add_argument('--port',type=int,default=8765); ap.add_argument('--access-log'); ap.add_argument('--ops-root'); ap.add_argument('--discovery-root'); ap.add_argument('--certification-root')
    a=ap.parse_args(argv); root=Path(a.published_root)
    v=validate_service_release(root,a.release_id)
    if not v['valid']:
        print(json.dumps({"service_started":False,"reasons":v['reasons']},sort_keys=True)); return 1
    rel=root/'published/soil/releases'/v['release_id']
    for p in [load_json(rel/'manifest.json'),load_json(rel/'index.json'),load_json(rel/'publication_receipt.json')]:
        if scan_payload_for_forbidden_terms(p): print(json.dumps({"service_started":False,"reasons":["forbidden terms in public payload"]},sort_keys=True)); return 1
    httpd=ThreadingHTTPServer((a.host,a.port),H); httpd.release_id=v['release_id']; httpd.release_root=rel; httpd.published_root=root; httpd.access_log=a.access_log; httpd.ops_root=a.ops_root; httpd.discovery_root=a.discovery_root; httpd.certification_root=a.certification_root
    print(json.dumps({"service_started":True,"host":a.host,"port":httpd.server_port,"release_id":v['release_id'],"audit_passed":True},sort_keys=True),flush=True)
    signal.signal(signal.SIGTERM, lambda *_: httpd.shutdown())
    try: httpd.serve_forever()
    except KeyboardInterrupt: pass
    return 0
if __name__=='__main__': raise SystemExit(main())
