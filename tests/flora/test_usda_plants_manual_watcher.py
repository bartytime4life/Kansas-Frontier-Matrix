import subprocess,sys

def test_offline_mock(tmp_path):
 out=tmp_path/'out'
 subprocess.run([sys.executable,'tools/watchers/flora/usda_plants_manual_watcher.py','--mode','offline_mock','--downloads-html','tests/fixtures/flora/usda_plants/source_discovery/downloads_page_fixture.html','--operator-raw-dir','tests/fixtures/flora/usda_plants/operator_snapshot/good','--snapshot-date','2026-04-30','--generated-at','2026-04-30T00:00:00Z','--out-dir',str(out)],check=False)
 assert (out/'receipts/flora/usda_plants/watcher_run_receipt.json').exists()
