import subprocess,sys

def test_importable():
    cp=subprocess.run([sys.executable,'tools/archive/soil/mock_archive_ack.py','--help'],capture_output=True,text=True)
    assert cp.returncode==0
