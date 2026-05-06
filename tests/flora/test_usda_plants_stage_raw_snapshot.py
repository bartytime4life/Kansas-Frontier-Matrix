import csv,json,subprocess

def test_stage(tmp_path):
 raw=tmp_path/'raw/flora/usda_plants/2026-04-30';work=tmp_path/'work/flora/usda_plants'
 subprocess.run(['python','tools/intake/flora/usda_plants_snapshot_intake.py','--raw-dir','tests/fixtures/flora/usda_plants/operator_snapshot/good','--snapshot-date','2026-04-30','--generated-at','2026-04-30T00:00:00Z','--out-dir',str(raw)],check=True)
 cc=work/'column_contract.json';subprocess.run(['python','tools/quality/flora/usda_plants_column_contract_builder.py','--generated-at','2026-04-30T00:00:00Z','--out',str(cc)],check=True)
 dr=work/'2026-04-30/source_drift_report.json';subprocess.run(['python','tools/quality/flora/usda_plants_source_drift_detector.py','--raw-dir',str(raw),'--column-contract',str(cc),'--snapshot-date','2026-04-30','--generated-at','2026-04-30T00:00:00Z','--out',str(dr)],check=True)
 st=work/'2026-04-30/staged';subprocess.run(['python','tools/normalize/flora/usda_plants_stage_raw_snapshot.py','--raw-dir',str(raw),'--raw-snapshot-manifest',str(raw/'raw_snapshot_manifest.json'),'--drift-report',str(dr),'--snapshot-date','2026-04-30','--generated-at','2026-04-30T00:00:00Z','--out-dir',str(st)],check=True)
 rows=list(csv.DictReader((st/'county_distribution.csv').open())); assert {r['fips'] for r in rows}=={'00001','00173'}
