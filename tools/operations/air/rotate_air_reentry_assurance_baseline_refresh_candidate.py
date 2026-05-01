#!/usr/bin/env python
from pathlib import Path
import runpy
runpy.run_path(str(Path(__file__).resolve().parent/'rotate_air_assurance_baseline_candidate.py'),run_name='__main__')
