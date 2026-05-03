#!/usr/bin/env python3
import subprocess,re,sys
pat=re.compile(r'data/(raw|work|quarantine)/')
scan=['apps','packages','docs']
cmd=['rg','-n','data/(raw|work|quarantine)/']+scan
r=subprocess.run(cmd,text=True,capture_output=True)
hits=[ln for ln in r.stdout.splitlines() if ln.strip()]
print('scan=raw/work/quarantine public-boundary references')
print(f'boundary_refs={len(hits)}')
for h in hits[:80]: print(h)
sys.exit(0)
