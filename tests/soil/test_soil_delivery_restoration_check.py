from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def test_check_exists(): assert (ROOT/'tools/validators/soil/delivery_restoration_check.py').exists()
