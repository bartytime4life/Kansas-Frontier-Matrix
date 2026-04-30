from pathlib import Path
from subprocess import run

def test_cdn_rollback_plan_builder(tmp_path: Path):
 out=tmp_path/'o.json'
 cmd=['python','tools/deploy/flora/usda_plants_cdn_rollback_plan_builder.py','--snapshot-date','2026-01-01','--generated-at','2026-01-01T00:00:00Z','--out',str(out)]
 if 'cdn_rollback_plan_builder'=='external_deployment_request_builder':
  reg=tmp_path/'r.json';run(['python','tools/deploy/flora/usda_plants_external_host_registry_builder.py','--snapshot-date','2026-01-01','--generated-at','2026-01-01T00:00:00Z','--out',str(reg)],check=True);cmd+=['--registry',str(reg),'--target-host-id','github_pages','--requester','alice']
 if 'cdn_rollback_plan_builder'=='cdn_deployment_execution_plan_builder':
  sb=tmp_path/'s.json';sb.write_text('{}');reg=tmp_path/'r.json';req=tmp_path/'req.json';ap=tmp_path/'ap.json'
  run(['python','tools/deploy/flora/usda_plants_external_host_registry_builder.py','--snapshot-date','2026-01-01','--generated-at','2026-01-01T00:00:00Z','--allow-cloudflare','--out',str(reg)],check=True)
  run(['python','tools/deploy/flora/usda_plants_external_deployment_request_builder.py','--snapshot-date','2026-01-01','--generated-at','2026-01-01T00:00:00Z','--registry',str(reg),'--target-host-id','cloudflare_pages_guarded','--requester','alice','--out',str(req)],check=True)
  run(['python','tools/deploy/flora/usda_plants_external_deployment_approval_builder.py','--snapshot-date','2026-01-01','--generated-at','2026-01-01T00:00:00Z','--approver','bob','--out',str(ap)],check=True)
  cmd+=['--site-bundle-manifest',str(sb),'--request',str(req),'--approval',str(ap),'--protected-environment']
 if 'cdn_rollback_plan_builder'=='cloudflare_pages_manifest_builder': cmd+=['--protected-environment']
 if 'cdn_rollback_plan_builder'=='custom_domain_readiness_builder': pass
 if 'cdn_rollback_plan_builder'=='external_deployment_verifier': sb=tmp_path/'s.json';pm=tmp_path/'p.json';sb.write_text('{}');pm.write_text('{}');cmd+=['--site-bundle-manifest',str(sb),'--provider-manifest',str(pm)]
 if 'cdn_rollback_plan_builder'=='external_deployment_approval_builder': cmd+=['--approver','bob']
 run(cmd,check=True);assert out.exists()
