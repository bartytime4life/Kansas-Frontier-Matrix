from __future__ import annotations
import json, subprocess, sys
from pathlib import Path

SDK="tools/connectors/fauna/kfm-ebird-ingest/kfm_ebird_sdk.py"
EX="tools/connectors/fauna/kfm-ebird-ingest/kfm_ebird_examples.py"

def run(script:str,*args:str):
 return subprocess.run([sys.executable,script,*args],check=False,text=True,capture_output=True)

def test_sdk_help_and_version()->None:
 assert run(SDK,"--help").returncode==0
 assert run(SDK,"--version").returncode==0

def test_examples_help_and_version()->None:
 assert run(EX,"--help").returncode==0
 assert run(EX,"--version").returncode==0

def test_sdk_id_deterministic(tmp_path:Path)->None:
 r1=run(SDK,"--mode","build","--dry-run","--out-dir",str(tmp_path))
 r2=run(SDK,"--mode","build","--dry-run","--out-dir",str(tmp_path))
 assert json.loads(r1.stdout)["sdk_id"]==json.loads(r2.stdout)["sdk_id"]

def test_examples_id_deterministic(tmp_path:Path)->None:
 r1=run(EX,"--mode","build","--dry-run","--out-dir",str(tmp_path))
 r2=run(EX,"--mode","build","--dry-run","--out-dir",str(tmp_path))
 assert json.loads(r1.stdout)["examples_id"]==json.loads(r2.stdout)["examples_id"]
