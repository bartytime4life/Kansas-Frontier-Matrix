#!/usr/bin/env python
import argparse,sys
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('dirs',nargs='+');a=p.parse_args();need=['reentry_maintenance_refresh_closure_record.json'];ok=True
for n in need: ok = ok and any((Path(d)/n).exists() for d in a.dirs)
print('PASS' if ok else 'DENY');sys.exit(0 if ok else 1)
