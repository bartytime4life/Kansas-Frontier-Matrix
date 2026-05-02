from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def test_probe_script_exists(): assert (ROOT/'tools/restoration/soil/probe_restored_delivery.py').exists()
