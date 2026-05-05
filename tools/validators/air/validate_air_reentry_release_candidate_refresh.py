#!/usr/bin/env python
import argparse,json
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('dirs',nargs='+');a=p.parse_args();need=['reentry_release_candidate_refresh_package.json','reentry_qa_revalidation_refresh_report.json'];seen=[]
for d in a.dirs:
 pth=Path(d)
 for n in need:
  if (pth/n).exists(): seen.append(n)
if len(set(seen))<2: raise SystemExit('DENY: missing required artifacts')
print('PASS')
