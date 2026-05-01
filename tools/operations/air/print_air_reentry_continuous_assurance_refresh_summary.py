#!/usr/bin/env python
import argparse,json
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument("--assurance-refresh-dir",required=True);p.add_argument("--format",choices=["text","json"],default="text");a=p.parse_args();d=Path(a.assurance_refresh_dir);f=d/"reentry_continuous_assurance_refresh_summary.json";o=json.loads(f.read_text());
print(json.dumps(o,indent=2) if a.format=="json" else f"status={o.get("status")}")
