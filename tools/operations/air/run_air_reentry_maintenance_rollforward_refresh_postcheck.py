#!/usr/bin/env python
from pathlib import Path
import runpy
runpy.run_path(str(Path(__file__).resolve().parent/'run_air_rollforward_postcheck.py'),run_name='__main__')
