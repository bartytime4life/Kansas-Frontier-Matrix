#!/usr/bin/env python
from pathlib import Path
import runpy
runpy.run_path(str(Path(__file__).resolve().parent/'accept_air_rollforward_candidate.py'),run_name='__main__')
