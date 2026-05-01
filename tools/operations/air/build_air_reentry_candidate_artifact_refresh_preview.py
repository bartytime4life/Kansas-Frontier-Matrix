#!/usr/bin/env python
from pathlib import Path
import runpy
runpy.run_path(str(Path(__file__).resolve().parent/'build_air_candidate_artifact_refresh.py'),run_name='__main__')
