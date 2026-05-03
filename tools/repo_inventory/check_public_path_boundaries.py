#!/usr/bin/env python3
import subprocess,re,sys
pat=r'data/(raw|work|quarantine|internal)'
scan=['apps','packages','docs']
out=[]
for s in scan:
    r=subprocess.run(['rg','-n',pat,s],capture_output=True,text=True)
    if r.returncode==0: out.append(r.stdout)
text=''.join(out)
if text: print(text[:5000]); sys.exit(1)
print('no direct forbidden lifecycle refs found in bounded scan')
