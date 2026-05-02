from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def test_builder_exists(): assert (ROOT/'tools/restoration/soil/build_delivery_restoration.py').exists()
