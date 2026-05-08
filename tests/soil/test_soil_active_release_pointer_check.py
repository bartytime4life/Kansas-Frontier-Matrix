from tests.soil.test_soil_active_release_pointer_builder import test_builder, run, ROOT
import sys

def test_check(tmp_path):
 test_builder(tmp_path)
 s=ROOT/'tools/validators/soil/active_release_pointer_check.py'
 assert run([s,'--active-root',tmp_path/'a']).returncode==0
