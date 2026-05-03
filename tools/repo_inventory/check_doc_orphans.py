#!/usr/bin/env python3
import subprocess,sys
allowed=('docs/','README.md','.github/')
orph=[]
for p in subprocess.check_output(['git','ls-files','*.md'],text=True).splitlines():
    if not p.startswith(allowed): orph.append(p)
print(f'orphan_markdown_outside_allowed={len(orph)}')
for p in orph[:50]: print(p)
sys.exit(0)
