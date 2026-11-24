#!/usr/bin/env python3
"""Decode the provider F32 GeoTIFF, retaining its mask and exact float32 values."""
import hashlib,json,math,os,sys
import numpy as np
from rasterio.io import MemoryFile

def read_private(path,maximum):
    if os.path.realpath(os.path.dirname(path))!=os.path.dirname(path): raise ValueError('UNSAFE_DIRECTORY')
    fd=os.open(path,os.O_RDONLY|os.O_NOFOLLOW|os.O_NONBLOCK)
    try:
        s=os.fstat(fd)
        if not __import__('stat').S_ISREG(s.st_mode) or s.st_uid!=os.getuid() or s.st_mode&0o777!=0o600 or s.st_nlink!=1 or not 0<s.st_size<=maximum: raise ValueError('UNSAFE_FILE')
        with os.fdopen(fd,'rb',closefd=False) as f: b=f.read(maximum+1)
        t=os.fstat(fd)
        if len(b)!=s.st_size or (s.st_size,s.st_mtime_ns,s.st_ctime_ns)!=(t.st_size,t.st_mtime_ns,t.st_ctime_ns): raise ValueError('CHANGED_FILE')
        return b
    finally: os.close(fd)

def decode(data,expected):
    with MemoryFile(data) as mem:
        with mem.open() as ds:
            if ds.driver!='GTiff' or ds.count!=1 or ds.width!=96 or ds.height!=96 or str(ds.crs)!='EPSG:3857' or ds.dtypes!=('float32',): raise ValueError('RASTER_SCHEMA')
            tr=ds.transform
            if tr.b!=0 or tr.d!=0 or tr.a<=0 or tr.e>=0 or any(abs(a-b)>1e-5 for a,b in zip(ds.bounds,expected)): raise ValueError('RASTER_GEOMETRY')
            a=ds.read(1); mask=ds.read_masks(1)>0
            valid=np.isfinite(a)&(a>=-12000)&(a<=9000)
            excluded=int(np.count_nonzero(mask&~valid)); mask &= valid
            return {'bounds3857':list(ds.bounds),'cellSize3857':[tr.a,-tr.e],'ground':[float(x) if ok else None for x,ok in zip(a.ravel(),mask.ravel())],'excludedValues':excluded}

def main():
    job=json.loads(read_private(sys.argv[1],16384));data=read_private(job['path'],2000000)
    if 'sha256:'+hashlib.sha256(data).hexdigest()!=job['sha256']: raise ValueError('RASTER_HASH')
    value=decode(data,job['bounds3857']);target=job['output']
    encoded=(json.dumps(value,allow_nan=False,separators=(',',':'))+'\n').encode()
    fd=os.open(target,os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW,0o600)
    with os.fdopen(fd,'wb') as f: f.write(encoded)
    print(json.dumps({'valid':sum(v is not None for v in value['ground']),'excludedValues':value['excludedValues']}))
if __name__=='__main__': main()
