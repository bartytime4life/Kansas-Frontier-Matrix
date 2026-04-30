import subprocess, json
from pathlib import Path

ST='tools/connectors/fauna/kfm-ebird-ingest/kfm-ebird-storage'
CT='tools/connectors/fauna/kfm-ebird-ingest/kfm-ebird-cost'

def test_storage_help(): assert subprocess.run([ST,'--help'],check=False).returncode==0

def test_storage_version(): assert subprocess.run([ST,'--version'],check=False).returncode==0

def test_cost_help(): assert subprocess.run([CT,'--help'],check=False).returncode==0

def test_cost_version(): assert subprocess.run([CT,'--version'],check=False).returncode==0

def test_storage_inventory_and_deterministic(tmp_path:Path):
 out=tmp_path/'s1'; out2=tmp_path/'s2'
 subprocess.run([ST,'--mode','inventory','--work-root','tools/tests/fixtures/ebird','--catalog-root','tools/tests/fixtures/ebird','--published-root','tools/tests/fixtures/ebird','--fixture-root','tools/tests/fixtures/ebird','--out-dir',str(out)],check=True)
 subprocess.run([ST,'--mode','inventory','--work-root','tools/tests/fixtures/ebird','--catalog-root','tools/tests/fixtures/ebird','--published-root','tools/tests/fixtures/ebird','--fixture-root','tools/tests/fixtures/ebird','--out-dir',str(out2)],check=True)
 a=json.loads((out/'storage_inventory.json').read_text())['storage_run_id']; b=json.loads((out2/'storage_inventory.json').read_text())['storage_run_id']
 assert a==b

def test_cost_estimate(tmp_path:Path):
 sout=tmp_path/'s'; cout=tmp_path/'c'
 subprocess.run([ST,'--mode','inventory','--work-root','tools/tests/fixtures/ebird','--catalog-root','tools/tests/fixtures/ebird','--published-root','tools/tests/fixtures/ebird','--fixture-root','tools/tests/fixtures/ebird','--out-dir',str(sout)],check=True)
 r=subprocess.run([CT,'--mode','estimate','--storage-inventory',str(sout/'storage_inventory.json'),'--out-dir',str(cout)],check=False)
 assert r.returncode==0
 assert (cout/'local_cost_estimate.json').exists()
