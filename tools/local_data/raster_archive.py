"""Bounded, in-memory inspection of a retained PRISM BIL tar.gz archive.

No member is extracted to disk. Header/byte-count/CRC checks describe the saved
grid; statistics do not independently validate a provider's climate model.
"""
import hashlib
import io
import math
from pathlib import PurePosixPath
import re
import struct
import tarfile
import zlib

from tools.local_data.file_io import read_regular

VERSION = 'prism-bil-archive-v2'
COMPRESSED_LIMIT = 16 * 1024**2
EXPANDED_LIMIT = 64 * 1024**2
MEMBER_LIMIT = 24
HEADER_LIMIT = 16384
CELL_LIMIT = 8_000_000
VARIABLES = {
    'ppt':('modeled total precipitation','mm'),
    'tmax':('modeled maximum temperature','degrees C'),
    'tmin':('modeled minimum temperature','degrees C'),
    'tmean':('modeled mean temperature','degrees C'),
    'tdmean':('modeled mean dew point temperature','degrees C'),
    'vpdmin':('modeled minimum vapor pressure deficit','hPa'),
    'vpdmax':('modeled maximum vapor pressure deficit','hPa'),
    'soltotal':('modeled total daily global shortwave solar radiation','MJ/m2/day'),
    'solslope':('modeled daily solar radiation on a sloped surface','MJ/m2/day'),
}
VARIABLE_REFERENCES = ['https://prism.oregonstate.edu/documents/PRISM_datasets.pdf',
    'https://prism.oregonstate.edu/faq/',
    'https://developers.google.com/earth-engine/datasets/catalog/OREGONSTATE_PRISM_ANd']


def inspect(path):
    info = {'version':VERSION,'format':'prism-bil-tar','issues':[],
        'compressed_limit':COMPRESSED_LIMIT,'expanded_limit':EXPANDED_LIMIT,
        'member_limit':MEMBER_LIMIT,'header_limit':HEADER_LIMIT,'cell_limit':CELL_LIMIT,
        'crc_validated':False,'structure_validated':False,'members':[],
        'scope':'Saved archive and grid structure only; no independent climate, date, units or factual validation.'}
    try:
        raw = read_regular(path,COMPRESSED_LIMIT)
        info['compressed_bytes_read']=len(raw)
        decoder = zlib.decompressobj(16+zlib.MAX_WBITS)
        expanded = decoder.decompress(raw,EXPANDED_LIMIT+1)
        info['expanded_bytes']=len(expanded)
        if len(expanded)>EXPANDED_LIMIT:raise ValueError('RASTER_ARCHIVE_EXPANSION_LIMIT')
        if not decoder.eof:raise ValueError('RASTER_ARCHIVE_INCOMPLETE_GZIP')
        if decoder.unused_data:raise ValueError('RASTER_ARCHIVE_TRAILING_OR_MULTIPLE_MEMBERS')
        info['crc_validated']=True
        files={}
        with tarfile.open(fileobj=io.BytesIO(expanded),mode='r:') as archive:
            for member in archive:
                if len(info['members'])>=MEMBER_LIMIT:raise ValueError('RASTER_ARCHIVE_MEMBER_LIMIT')
                name=PurePosixPath(member.name)
                if (len(member.name)>240 or name.is_absolute() or '..' in name.parts or '\\' in member.name
                        or ':' in member.name or str(name)!=member.name
                        or any(ord(c)<32 or ord(c)==127 for c in member.name)
                        or not member.isfile() or member.name in files):
                    raise ValueError('RASTER_ARCHIVE_UNSAFE_MEMBER')
                if not member.name.lower().endswith(('.bil','.hdr','.prj','.info.txt')):
                    raise ValueError('RASTER_ARCHIVE_UNSUPPORTED_MEMBER')
                if member.size<0 or member.size>EXPANDED_LIMIT:raise ValueError('RASTER_ARCHIVE_MEMBER_SIZE')
                if not member.name.lower().endswith('.bil') and member.size>HEADER_LIMIT:
                    raise ValueError('RASTER_ARCHIVE_HEADER_LIMIT')
                stream=archive.extractfile(member)
                if stream is None:raise ValueError('RASTER_ARCHIVE_MEMBER_MISSING')
                body=stream.read(member.size+1)
                if len(body)!=member.size:raise ValueError('RASTER_ARCHIVE_MEMBER_TRUNCATED')
                files[member.name]=body
                info['members'].append({'name':member.name,'bytes':member.size,
                    'sha256':hashlib.sha256(body).hexdigest()})
        bils=[name for name in files if name.lower().endswith('.bil')]
        if len(bils)!=1:raise ValueError('RASTER_ARCHIVE_ONE_BIL_REQUIRED')
        bil=bils[0];header_name=bil[:-4]+'.hdr'
        if header_name not in files:raise ValueError('RASTER_ARCHIVE_MATCHING_HEADER_REQUIRED')
        headers={}
        for line in files[header_name].decode('ascii').splitlines():
            if not line.strip():continue
            key,value=line.split(None,1);key=key.upper()
            if key in headers:raise ValueError('RASTER_ARCHIVE_DUPLICATE_HEADER_KEY')
            headers[key]=value.strip()
        if (headers.get('LAYOUT')!='BIL' or headers.get('PIXELTYPE')!='FLOAT'
                or headers.get('NBANDS')!='1' or headers.get('NBITS')!='32'
                or headers.get('BYTEORDER') not in {'I','M'}):
            raise ValueError('RASTER_ARCHIVE_UNSUPPORTED_GRID')
        rows,cols=int(headers['NROWS']),int(headers['NCOLS'])
        if rows<=0 or cols<=0 or rows*cols>CELL_LIMIT:raise ValueError('RASTER_ARCHIVE_CELL_LIMIT')
        if len(files[bil])!=rows*cols*4:raise ValueError('RASTER_ARCHIVE_GRID_BYTE_COUNT')
        x,y,dx,dy=(float(headers[k]) for k in ('ULXMAP','ULYMAP','XDIM','YDIM'))
        nodata=float(headers['NODATA'])
        if not all(math.isfinite(v) for v in (x,y,dx,dy,nodata)) or dx<=0 or dy<=0:
            raise ValueError('RASTER_ARCHIVE_INVALID_GEOREFERENCE')
        count,missing,nonfinite,low,high=0,0,0,None,None
        order='<' if headers['BYTEORDER']=='I' else '>'
        for (value,) in struct.iter_unpack(order+'f',files[bil]):
            if value==nodata:missing+=1
            elif not math.isfinite(value):nonfinite+=1
            else:
                count+=1;low=value if low is None else min(low,value);high=value if high is None else max(high,value)
        projection=files.get(bil[:-4]+'.prj')
        # PRISM's upstream projection sidecar can retain its original US stem.
        if projection is None:
            projections=[body for name,body in files.items() if name.lower().endswith('.prj')]
            if len(projections)!=1:raise ValueError('RASTER_ARCHIVE_ONE_PROJECTION_REQUIRED')
            projection=projections[0]
        info['grid']={'rows':rows,'columns':cols,'bands':1,'dtype':'float32','byte_order':headers['BYTEORDER'],
            'upper_left_cell_center':[x,y],'cell_spacing':[dx,dy],
            'header_coordinate_bounds':[x-dx/2,y-(rows-.5)*dy,x+(cols-.5)*dx,y+dy/2],
            'projection_wkt':projection.decode('utf-8'),'nodata':nodata,
            'valid_cells':count,'nodata_cells':missing,'nonfinite_cells':nonfinite,
            'stored_minimum':low,'stored_maximum':high,
            'units':'Not embedded in the BIL header; documented provider units are recorded separately when identified.'}
        if nonfinite:raise ValueError('RASTER_ARCHIVE_NONFINITE_CELLS')
        if not count:raise ValueError('RASTER_ARCHIVE_NO_VALID_CELLS')
        text=[]
        for name,body in files.items():
            if name==bil:continue
            value=body.decode('utf-8')
            if '\0' in value:raise ValueError('RASTER_ARCHIVE_BINARY_SIDECAR')
            text.append('Archive member '+name+':\n'+value)
            if name.endswith('.info.txt'):
                fields=dict(line.split(':',1) for line in value.splitlines() if ':' in line)
                dataset=fields.get('PRISM_DATASET_FILENAME','').strip()
                match=re.fullmatch(r'prism_([a-z]+)_us_[A-Za-z0-9]+_([0-9]{4,8})\.bil',dataset)
                if match and match[1] in VARIABLES:
                    meaning,units=VARIABLES[match[1]]
                    info['provider_variable']={'code':match[1],'meaning':meaning,'documented_units':units,
                        'provider_date_code':match[2],'dataset_filename':dataset,
                        'interpretation_basis':'Saved provider filename code interpreted using the published PRISM variable dictionary; source identity and climate values remain unverified.',
                        'documentation':VARIABLE_REFERENCES}
        info['structure_validated']=True
        combined='\n\n'.join(text)
        info['metadata_text_characters']=min(len(combined),6000)
        info['metadata_text_truncated']=len(combined)>6000
        return {'inspection':info,'text':combined[:6000]}
    except (ValueError,KeyError,UnicodeError,struct.error,zlib.error,tarfile.TarError,OSError) as error:
        code=str(error)
        info['issues'].append(code if code.startswith('RASTER_ARCHIVE_') else 'RASTER_ARCHIVE_INVALID_OR_UNSUPPORTED')
        return {'inspection':info,'text':''}
