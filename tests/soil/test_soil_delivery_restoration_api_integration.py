from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
def test_api_exists(): assert (ROOT/'tools/serve/soil/public_api.py').exists()
