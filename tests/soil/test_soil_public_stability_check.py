from tests.soil.test_soil_public_stability_builder import test_build,ROOT
import subprocess,sys

def test_check(tmp_path):
 test_build(tmp_path)
 p=subprocess.run([sys.executable,ROOT/'tools/validators/soil/public_stability_check.py','--stability-root',tmp_path],capture_output=True,text=True)
 assert p.returncode==0
