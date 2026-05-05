#!/usr/bin/env python
from pathlib import Path
import runpy
runpy.run_path(str(Path(__file__).resolve().parent/'plan_air_remediation_rollforward.py'),run_name='__main__')
