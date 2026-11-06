#!/usr/bin/env python3
"""Bounded offline daily Sky candidate preparation. Never writes public/ or activates collection.
Default: inspect the fixed provider release and print transfer/storage requirements.
--download: verify every daily production asset, stream its tar, retain regional raw
members and every regional segment, and atomically finish a private candidate day.
--tar: local diagnostic input; always partial-input coverage, never a complete day.
"""
import argparse, contextlib, datetime as dt, gzip, hashlib, importlib.util, io, json, os
import pathlib, re, shutil, tarfile, tempfile, time, urllib.request

SPEC = importlib.util.spec_from_file_location('sky_replay', pathlib.Path(__file__).with_name('prepare-kansas-sky-replay.py'))
REPLAY = importlib.util.module_from_spec(SPEC); SPEC.loader.exec_module(REPLAY)
MAX_DOWNLOAD = 6 * 1024**3
MAX_CANDIDATE = 2 * 1024**3
MAX_MEMBERS = 500000
MAX_FILES = 10000
MAX_PAYLOAD = 4 * 1024**2
ALLOWED_HOSTS = {'api.github.com', 'github.com', 'release-assets.githubusercontent.com', 'objects.githubusercontent.com'}

def encoded(value): return (json.dumps(value, separators=(',', ':'), allow_nan=False)+'\n').encode()
def sha(data): return hashlib.sha256(data).hexdigest()
def now(): return dt.datetime.now(dt.timezone.utc).isoformat().replace('+00:00','Z')
def day_value(value):
    if value == 'yesterday': return (dt.datetime.now(dt.timezone.utc).date()-dt.timedelta(days=1)).isoformat()
    if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', value) or dt.date.fromisoformat(value).isoformat()!=value: raise ValueError('INVALID_DAY')
    if dt.date.fromisoformat(value)>=dt.datetime.now(dt.timezone.utc).date(): raise ValueError('DAY_NOT_FINISHED')
    return value

def release_url(day):
    return f"https://api.github.com/repos/adsblol/globe_history_{day[:4]}/releases/tags/v{day.replace('-','.')}-planes-readsb-prod-0"

class SafeRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        check_url(newurl)
        return super().redirect_request(req, fp, code, msg, headers, newurl)

def check_url(url):
    from urllib.parse import urlsplit
    parsed=urlsplit(url)
    if parsed.scheme!='https' or parsed.hostname not in ALLOWED_HOSTS or parsed.username or parsed.password or parsed.port not in (None,443): raise ValueError('SOURCE_URL_REJECTED')

def open_url(url, timeout=60):
    check_url(url)
    return urllib.request.build_opener(SafeRedirect()).open(urllib.request.Request(url,headers={'User-Agent':'KFM-Kansas-Sky-Daily/1','Accept':'application/vnd.github+json' if url.startswith('https://api.github.com/') else 'application/octet-stream'}),timeout=timeout)

def release_plan(day, metadata=None):
    if metadata is None:
        with open_url(release_url(day),20) as response: body=response.read(MAX_PAYLOAD+1)
        if len(body)>MAX_PAYLOAD: raise ValueError('RELEASE_METADATA_BOUND')
        metadata=json.loads(body)
    tag=f"v{day.replace('-','.')}-planes-readsb-prod-0"
    if metadata.get('tag_name')!=tag or metadata.get('draft') or metadata.get('prerelease') or not metadata.get('published_at'): raise ValueError('RELEASE_IDENTITY_MISMATCH')
    assets=[]
    for asset in metadata.get('assets',[]):
        name=asset.get('name','')
        if not re.fullmatch(re.escape(tag)+r'\.tar\.[a-z]{2}',name): raise ValueError('UNEXPECTED_RELEASE_ASSET')
        url=f'https://github.com/adsblol/globe_history_{day[:4]}/releases/download/{tag}/{name}'
        digest=asset.get('digest','')
        size=asset.get('size')
        if asset.get('browser_download_url')!=url or not re.fullmatch(r'sha256:[a-f0-9]{64}',digest) or type(size)!=int or size<=0: raise ValueError('ASSET_INTEGRITY_METADATA_REQUIRED')
        assets.append({'name':name,'url':url,'sha256':digest[7:],'bytes':size})
    assets.sort(key=lambda a:a['name'])
    suffixes=[a['name'][-2:] for a in assets]
    expected=[chr(97+i//26)+chr(97+i%26) for i in range(len(assets))]
    if not assets or len(assets)>26 or suffixes!=expected: raise ValueError('ARCHIVE_PARTS_INCOMPLETE')
    size=sum(a['bytes'] for a in assets)
    if size>MAX_DOWNLOAD: raise ValueError('DAILY_DOWNLOAD_BOUND')
    return {'day':day,'releaseUrl':release_url(day),'sourcePublishedAt':metadata['published_at'],'assets':assets,'downloadBytes':size,'maxCandidateBytes':MAX_CANDIDATE,'provider':'adsb.lol','license':'ODbL-1.0','licenseUrl':'https://opendatacommons.org/licenses/odbl/1-0/','region':{'west':-103.2,'east':-93.6,'south':36.2,'north':40.9}}

class Parts(io.RawIOBase):
    def __init__(self, paths): self.paths=iter(paths); self.current=None
    def readable(self): return True
    def read(self, size=-1):
        if size<0: raise ValueError('UNBOUNDED_READ_REFUSED')
        out=bytearray()
        while len(out)<size:
            if self.current is None:
                path=next(self.paths,None)
                if path is None: break
                self.current=open(path,'rb')
            piece=self.current.read(size-len(out))
            if piece: out.extend(piece)
            else: self.current.close(); self.current=None
        return bytes(out)
    def close(self):
        if self.current: self.current.close()
        super().close()

class CandidateWriter:
    def __init__(self,root): self.root=root; self.used=0; self.artifacts=[]
    def put(self,relative,data):
        self.used+=len(data)
        if self.used>MAX_CANDIDATE: raise ValueError('CANDIDATE_CAPACITY_BOUND')
        path=self.root/relative;path.parent.mkdir(parents=True,exist_ok=True)
        with path.open('xb') as stream: stream.write(data);stream.flush();os.fsync(stream.fileno())
        self.artifacts.append({'path':relative,'sha256':sha(data),'bytes':len(data)})

# No whole global day is held in memory and no tar paths are extracted.
def prepare_tar(paths, plan, root, verified=False):
    writer=CandidateWriter(root);flights=[];aircraft=set();seen=set();scanned=0;point_count=0
    started=time.monotonic(); day=plan['day'];source_url=plan['assets'][0]['url']
    with Parts(paths) as stream, tarfile.open(fileobj=stream,mode='r|') as archive:
        for member in archive:
            scanned+=1
            if scanned>MAX_MEMBERS or time.monotonic()-started>3*3600: raise ValueError('ARCHIVE_PROCESSING_BOUND')
            if len(member.name)>512 or member.name.startswith('/') or '..' in pathlib.PurePosixPath(member.name).parts: raise ValueError('ARCHIVE_PATH_REJECTED')
            if member.issym() or member.islnk(): raise ValueError('ARCHIVE_LINK_REJECTED')
            if not member.isfile(): continue
            if not re.search(r'(?:^|/)traces/[a-f0-9]{2}/trace_full_~?[a-f0-9]{6}\.json(?:\.gz)?$',member.name): continue
            if member.size>4*1024**2: raise ValueError('TRACE_MEMBER_BOUND')
            handle=archive.extractfile(member)
            with handle: raw=handle.read(4*1024**2+1)
            if len(raw)!=member.size: raise ValueError('TRACE_MEMBER_TRUNCATED')
            try: result=REPLAY.prepare(raw,source_url,member.name,all_segments=True,utc_day=day)
            except ValueError as error:
                if str(error)=='NO_REGIONAL_OBSERVATIONS': continue
                raise
            hex_id=result['points'][0]['hex']
            if not re.search(r'trace_full_'+re.escape(hex_id)+r'\.json(?:\.gz)?$',member.name): raise ValueError('TRACE_IDENTITY_MISMATCH')
            if hex_id in seen: raise ValueError('DUPLICATE_AIRCRAFT_MEMBER')
            seen.add(hex_id);aircraft.add(hex_id);point_count+=len(result['points'])
            writer.put(f'raw/{hex_id}.json.gz',raw)
            # At most 2,500 original points per browser chunk, further reduced by byte bound.
            parts=[];points=result['points'];offset=0
            while offset<len(points):
                count=min(2500,len(points)-offset);part=len(parts)+1
                while True:
                    identifier=f"{day}-{hex_id.replace('~','nonicao-')}-p{part:04d}"
                    output={**result,'id':identifier,'day':day,'points':points[offset:offset+count]}
                    payload=encoded(output)
                    if len(payload)<=MAX_PAYLOAD: break
                    count//=2
                    if not count: raise ValueError('POINT_PAYLOAD_BOUND')
                parts.append((output,payload));offset+=count
            for part,(output,payload) in enumerate(parts,1):
                identifier=output['id'];file=f'{identifier}.json';writer.put(f'replays/{file}',payload)
                pts=output['points'];flights.append({'id':identifier,'title':f"{pts[-1].get('callsign') or hex_id.upper()} · {day} · part {part}/{len(parts)}",'hex':hex_id,'day':day,'part':part,'partCount':len(parts),'pointCount':len(pts),'segmentCount':sum(bool(p.get('breakBefore')) for p in pts),'coverage':'provider-day-processed' if verified else 'partial-input','start':REPLAY.iso(pts[0]['observedAt']),'end':REPLAY.iso(pts[-1]['observedAt']),'url':f'/data/aviation/replays/days/{day}/{file}','sha256':sha(payload),'provider':'adsb.lol','license':'ODbL-1.0','sourceUrl':source_url})
                if len(flights)>MAX_FILES: raise ValueError('DAY_CATALOG_ENTRY_BOUND')
    flights.sort(key=lambda f:(f['hex'],f['start'],f['id']))
    catalog=encoded({'schemaVersion':1,'flights':flights})
    if len(catalog)>MAX_PAYLOAD: raise ValueError('DAY_CATALOG_BYTE_BOUND')
    writer.put('replays/index.json',catalog)
    receipt={'schemaVersion':1,'profile':'kfm-sky-day-candidate/v1','day':day,'preparedAt':now(),'coverage':'provider-day-processed' if verified else 'partial-input','lifecycle':'WORK/QUARANTINE','releaseState':'unreleased','evidenceRole':'EXTERNAL_CONTEXT_ONLY','source':plan,'membersScanned':scanned,'aircraftCount':len(aircraft),'pointCount':point_count,'fileCount':len(flights),'artifacts':writer.artifacts,'limitations':['Coverage is observations from the chosen provider instance, not every real aircraft.','All regional segments are retained; gaps are not filled.','Prepared output is not published or proof of an active schedule.','Raw members preserve original source bytes; replay files are bounded derivatives.']}
    writer.put('receipt.json',encoded(receipt));return receipt

def bytes_under(root):
    total=0
    for path in root.rglob('*'):
        if path.is_symlink(): raise ValueError('ARCHIVE_SYMLINK_REJECTED')
        if path.is_file(): total+=path.stat().st_size
    return total

def verify_day(root):
    receipt_path=root/'receipt.json'
    if receipt_path.is_symlink() or receipt_path.stat().st_size>MAX_PAYLOAD: raise ValueError('RETAINED_DAY_INTEGRITY_FAILED')
    receipt=json.loads(receipt_path.read_bytes())
    if receipt.get('profile')!='kfm-sky-day-candidate/v1' or not isinstance(receipt.get('artifacts'),list) or len(receipt['artifacts'])>MAX_FILES*2+1: raise ValueError('RETAINED_DAY_INTEGRITY_FAILED')
    for artifact in receipt['artifacts']:
        if not isinstance(artifact.get('path'),str) or not re.fullmatch(r'(?:raw/[~a-f0-9]+\.json\.gz|replays/[a-z0-9-]+\.json)',artifact['path']) or type(artifact.get('bytes'))!=int or not 0<artifact['bytes']<=MAX_PAYLOAD: raise ValueError('RETAINED_DAY_INTEGRITY_FAILED')
        path=root/artifact['path']
        if path.is_symlink() or not path.resolve().is_relative_to(root.resolve()) or not path.is_file() or path.stat().st_size!=artifact['bytes'] or sha(path.read_bytes())!=artifact['sha256']: raise ValueError('RETAINED_DAY_INTEGRITY_FAILED')
    return receipt

def main():
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--day',default='yesterday');parser.add_argument('--output',type=pathlib.Path)
    mode=parser.add_mutually_exclusive_group();mode.add_argument('--download',action='store_true');mode.add_argument('--tar',type=pathlib.Path)
    parser.add_argument('--capacity-bytes',type=int,default=80_000_000_000)
    args=parser.parse_args();day=day_value(args.day)
    plan=release_plan(day)
    if not(args.download or args.tar): print(json.dumps({'state':'plan-only','collectionActive':False,**plan},indent=2));return
    if args.output is None: raise ValueError('EXPLICIT_OUTPUT_REQUIRED')
    root=args.output.resolve();repo=pathlib.Path(__file__).resolve().parents[1]
    if root.is_relative_to(repo) or 'sources' in root.parts: raise ValueError('PRIVATE_OUTPUT_OUTSIDE_REPOSITORY_REQUIRED')
    root.mkdir(parents=True,exist_ok=True,mode=0o700)
    lock=root/'.sky-day.lock';fd=os.open(lock,os.O_WRONLY|os.O_CREAT|os.O_EXCL|os.O_NOFOLLOW,0o600)
    try:
        os.write(fd,encoded({'pid':os.getpid(),'at':now(),'day':day}));os.close(fd)
        final=root/day
        if final.exists(): print(json.dumps({'state':'already-prepared','receipt':verify_day(final)}));return
        reserve=(plan['downloadBytes'] if args.download else 0)+MAX_CANDIDATE
        if not 0<args.capacity_bytes<=80_000_000_000 or bytes_under(root)+reserve>args.capacity_bytes or shutil.disk_usage(root).free<reserve: raise ValueError('ARCHIVE_CAPACITY_HELD')
        stage=pathlib.Path(tempfile.mkdtemp(prefix=f'.{day}-preparing-',dir=root))
        try:
            if args.download:
                downloads=stage/'downloads';downloads.mkdir();paths=[]
                for asset in plan['assets']:
                    path=downloads/asset['name'];digest=hashlib.sha256();count=0
                    with open_url(asset['url']) as response,path.open('xb') as target:
                        while block:=response.read(1024**2):
                            count+=len(block)
                            if count>asset['bytes']: raise ValueError('ASSET_SIZE_MISMATCH')
                            digest.update(block);target.write(block)
                    if count!=asset['bytes'] or digest.hexdigest()!=asset['sha256']: raise ValueError('ASSET_DIGEST_MISMATCH')
                    paths.append(path);print(json.dumps({'state':'asset-verified','asset':asset['name'],'bytes':count}),flush=True)
            else: paths=[args.tar.resolve()]
            receipt=prepare_tar(paths,plan,stage,verified=args.download)
            if args.download: shutil.rmtree(downloads) # Only verified temporary global transfer files; retained regional bytes remain.
            os.rename(stage,final)
            print(json.dumps({'state':'candidate-prepared','collectionActive':False,'path':str(final),'coverage':receipt['coverage'],'aircraftCount':receipt['aircraftCount'],'pointCount':receipt['pointCount'],'releaseState':'unreleased'}))
        except Exception as error:
            (stage/'failure.json').write_bytes(encoded({'state':'failed','day':day,'at':now(),'reason':str(error),'releaseState':'unreleased'}))
            raise
    finally: lock.unlink(missing_ok=True)

if __name__=='__main__':
    try: main()
    except Exception as error:
        print(json.dumps({'state':'held','reason':str(error),'collectionActive':False}));raise SystemExit(1)
