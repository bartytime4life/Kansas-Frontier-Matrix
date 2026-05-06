import json,subprocess,sys

def test_builder(tmp_path):
 d=tmp_path/'d';d.mkdir();obs=d/'scheduled_observation.json'
 payload={"schema_version":"1.0.0","object_type":"usda_plants_scheduled_observation","observation_id":"x","domain":"flora","source_id":"usda_plants","source_uri":"https://plants.sc.egov.usda.gov/downloads","generated_at":"2026-04-30T00:00:00Z","mode":"scheduled_mock","network_mode":"disabled","ci":False,"publishes":False,"promotes":False,"creates_pr":False,"downloads_raw":False,"resources":[],"change_summary":{"changed":False,"added":0,"removed":0,"changed_resources":0,"failed_resources":0},"status":"pass","reason_codes":[],"observation_hash":"sha256:"+"0"*64}
 obs.write_text(json.dumps(payload))
 out=d/'watch.json';subprocess.check_call([sys.executable,'tools/watchers/flora/usda_plants_watch_state_builder.py','--observation',str(obs),'--generated-at','2026-04-30T00:00:00Z','--out',str(out)])
 assert json.loads(out.read_text())['state_hash'].startswith('sha256:')
