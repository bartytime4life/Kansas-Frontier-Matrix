import json, subprocess, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]

def test_files_exist():
    assert (ROOT/'tools/restoration/soil/record_restoration_approval.py').exists()
