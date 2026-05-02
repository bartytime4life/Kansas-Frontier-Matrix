from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def test_gate_exists(): assert (ROOT/'tools/validators/soil/delivery_restoration_gate.py').exists()
