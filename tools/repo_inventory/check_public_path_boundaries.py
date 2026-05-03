#!/usr/bin/env python3
import subprocess,re
scan=['apps','packages','docs']
pat=re.compile(r'data/(raw|work|quarantine)/')
text=subprocess.check_output(['rg','-n','data/(raw|work|quarantine)/']+scan,text=True)
lines=[l for l in text.splitlines() if l]
print('\n'.join(lines[:80]))
raise SystemExit(1 if lines else 0)
