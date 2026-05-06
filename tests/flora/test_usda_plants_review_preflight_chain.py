import json, subprocess, sys

def test_chain(tmp_path):
    out=tmp_path/'out'; d='2026-04-30'; g='2026-04-30T00:00:00Z'
    rc=out/f'releases/flora/usda_plants/release_candidate_{d}.json'; rc.parent.mkdir(parents=True,exist_ok=True); rc.write_text(json.dumps({'source_id':'usda_plants'}))
    ca=out/f'work/flora/usda_plants/scheduled/{d}/change_alert.json'; ca.parent.mkdir(parents=True,exist_ok=True); ca.write_text('{}')
    rq=out/f'work/flora/usda_plants/scheduled/{d}/reviewer_queue.json'; rq.write_text('{}')
    ph=out/f'releases/flora/usda_plants/pr_handoff_{d}.json'; ph.write_text('{}')
    mc=out/'maps/flora/usda_plants/county_presence.layer_contract.json'; mc.parent.mkdir(parents=True,exist_ok=True); mc.write_text('{}')
    ev=out/'ui/flora/usda_plants/evidence_drawer'; ev.mkdir(parents=True,exist_ok=True); (ev/'ok.json').write_text('{"fips":"12345"}')
    rd=out/f'review/flora/usda_plants/{d}/review_decision.json'; sr=out/f'review/flora/usda_plants/{d}/sensitivity_review.json'; ra=out/f'review/flora/usda_plants/{d}/rights_attestation.json'; al=out/f'review/flora/usda_plants/{d}/review_audit_ledger.json'; pf=out/f'preflight/flora/usda_plants/{d}/promotion_preflight.json'
    subprocess.run([sys.executable,'tools/review/flora/usda_plants_review_decision_builder.py','--release-candidate',str(rc),'--change-alert',str(ca),'--reviewer-queue',str(rq),'--pr-handoff',str(ph),'--reviewer-id','flora-data-steward','--decision','approved_for_preflight','--snapshot-date',d,'--generated-at',g,'--out',str(rd)],check=True)
    subprocess.run([sys.executable,'tools/review/flora/usda_plants_sensitivity_review_builder.py','--release-candidate',str(rc),'--map-contract',str(mc),'--evidence-drawer-dir',str(ev),'--snapshot-date',d,'--generated-at',g,'--out',str(sr)],check=True)
    subprocess.run([sys.executable,'tools/review/flora/usda_plants_rights_attestation_builder.py','--release-candidate',str(rc),'--snapshot-date',d,'--generated-at',g,'--out',str(ra)],check=True)
    subprocess.run([sys.executable,'tools/review/flora/usda_plants_review_audit_ledger_builder.py','--release-candidate',str(rc),'--review-decision',str(rd),'--sensitivity-review',str(sr),'--rights-attestation',str(ra),'--snapshot-date',d,'--generated-at',g,'--out',str(al)],check=True)
    subprocess.run([sys.executable,'tools/promotion/flora/usda_plants_promotion_preflight_builder.py','--release-candidate',str(rc),'--review-decision',str(rd),'--sensitivity-review',str(sr),'--rights-attestation',str(ra),'--audit-ledger',str(al),'--snapshot-date',d,'--generated-at',g,'--out',str(pf)],check=True)
    o=json.loads(pf.read_text()); assert o['status']=='pass' and o['eligibility']['eligible_for_publication'] is False and o['gates']['publication']=='blocked'
