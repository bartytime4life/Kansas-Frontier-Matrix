from pathlib import Path
from subprocess import run

def test_chain(tmp_path: Path):
 snap='2026-01-01';gen='2026-01-01T00:00:00Z'
 reg=tmp_path/'reg.json';run(['python','tools/deploy/flora/usda_plants_external_host_registry_builder.py','--snapshot-date',snap,'--generated-at',gen,'--allow-cloudflare','--out',str(reg)],check=True)
 assert reg.exists()
