from pathlib import Path
import json,subprocess,tempfile

def test_static_deployment_chain():
    with tempfile.TemporaryDirectory() as d:
        base=Path(d);pub=base/'published/flora/usda_plants/2026-01-01'
        for f in ['release_manifest.json','dataset_index.json','evidence_drawer_index.json','county_presence.json','map_descriptor.json','map/county_presence.geojson','map/map_style.json','hosting/static_host_handoff.json','hosting/cache_integrity_manifest.json']:
            p=pub/f;p.parent.mkdir(parents=True,exist_ok=True);p.write_text('{}')
        req=base/'req.json';ap=base/'ap.json';plan=base/'plan.json'
        subprocess.check_call(['python','tools/deploy/flora/usda_plants_static_deployment_request_builder.py','--published-root',str(pub),'--snapshot-date','2026-01-01','--generated-at','2026-01-01T00:00:00Z','--requested-by','tester','--out',str(req)])
        subprocess.check_call(['python','tools/deploy/flora/usda_plants_static_deployment_approval_builder.py','--deployment-request',str(req),'--generated-at','2026-01-01T00:00:00Z','--approved-by','reviewer','--out',str(ap)])
        subprocess.check_call(['python','tools/deploy/flora/usda_plants_static_site_build_plan_builder.py','--deployment-request',str(req),'--deployment-approval',str(ap),'--site-root','site/flora/usda_plants/2026-01-01','--generated-at','2026-01-01T00:00:00Z','--out',str(plan)])
        subprocess.check_call(['python','tools/deploy/flora/usda_plants_static_site_builder.py','--published-root',str(pub),'--snapshot-date','2026-01-01','--generated-at','2026-01-01T00:00:00Z','--out-root',str(base)])
        bundle=base/'site/flora/usda_plants/2026-01-01/static_site_bundle_manifest.json'
        execp=base/'exec.json';rec=base/'rec.json';ver=base/'ver.json'
        subprocess.check_call(['python','tools/deploy/flora/usda_plants_deployment_execution_plan_builder.py','--snapshot-date','2026-01-01','--generated-at','2026-01-01T00:00:00Z','--site-bundle-manifest',str(bundle),'--out',str(execp)])
        subprocess.check_call(['python','tools/deploy/flora/usda_plants_deployment_receipt_builder.py','--execution-plan',str(execp),'--generated-at','2026-01-01T00:00:00Z','--out',str(rec)])
        subprocess.check_call(['python','tools/deploy/flora/usda_plants_deployment_verifier.py','--site-bundle-manifest',str(bundle),'--mode','local_artifact','--generated-at','2026-01-01T00:00:00Z','--out',str(ver)])
        assert json.loads(rec.read_text())['deployed'] is False
        assert json.loads(ver.read_text())['mode']=='local_artifact'
