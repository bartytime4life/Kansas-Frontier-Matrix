import json,subprocess,sys,os

def test_plan_only(tmp_path):
 out=tmp_path/'raw';subprocess.run([sys.executable,'tools/sources/flora/usda_plants_live_fetcher.py','--source-uri','https://plants.sc.egov.usda.gov/downloads','--snapshot-date','2026-04-30','--generated-at','2026-04-30T00:00:00Z','--plan-only','--out-dir',str(out)],check=True)
 assert (out/'live_fetch_plan.json').exists()
