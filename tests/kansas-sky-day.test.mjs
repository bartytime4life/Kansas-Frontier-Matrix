import test from 'node:test';
import {execFileSync} from 'node:child_process';
const prelude=String.raw`import importlib.util,json,gzip,tarfile,io,tempfile,pathlib,hashlib
spec=importlib.util.spec_from_file_location('day','scripts/prepare-kansas-sky-day.py');day=importlib.util.module_from_spec(spec);spec.loader.exec_module(day)
D='2026-11-03';tag='v2026.11.03-planes-readsb-prod-0';name=tag+'.tar.aa';url='https://github.com/adsblol/globe_history_2026/releases/download/'+tag+'/'+name
metadata={'tag_name':tag,'published_at':'2026-11-04T03:00:00Z','assets':[{'name':name,'size':100,'digest':'sha256:'+'a'*64,'browser_download_url':url}]}
plan=day.release_plan(D,metadata)
def trace(hexid='abc123', rows=None):
 return gzip.compress(json.dumps({'icao':hexid,'timestamp':1793664000,'trace':rows or [[0,38,-98,10000,400,90,0,0,{},'adsb_icao'],[10,38.01,-98,11000,400,90,0,0,{},'adsb_icao']]}).encode())
def tar(path, members):
 with tarfile.open(path,'w') as archive:
  for name,raw in members:
   info=tarfile.TarInfo(name);info.size=len(raw);archive.addfile(info,io.BytesIO(raw))
`;
const check=source=>execFileSync('python3',['-c',prelude+source],{stdio:'pipe'});
test('daily extraction retains every regional segment and original bytes, including single observations',()=>check(String.raw`
rows=[[0,38,-98,10000,400,90,0,0,{},'adsb_icao'],[10,38.01,-98,11000,400,90,0,0,{},'adsb_icao'],[100,38.1,-98,20000,400,90,0,0,{},'adsb_icao'],[110,38.11,-98,21000,400,90,0,0,{},'adsb_icao'],[120,50,-98,21000,400,90,0,0,{},'adsb_icao'],[130,38.2,-98,22000,400,90,0,0,{},'adsb_icao']]
raw=trace(rows=rows)
with tempfile.TemporaryDirectory() as temp:
 root=pathlib.Path(temp);archive=root/'input.tar';tar(archive,[('./traces/23/trace_full_abc123.json',raw)])
 output=root/'day';output.mkdir();receipt=day.prepare_tar([archive],plan,output)
 assert receipt['coverage']=='partial-input' and receipt['releaseState']=='unreleased'
 assert receipt['aircraftCount']==1 and receipt['pointCount']==5
 assert (output/'raw/abc123.json.gz').read_bytes()==raw
 catalog=json.loads((output/'replays/index.json').read_bytes());entry=catalog['flights'][0]
 part=json.loads((output/'replays'/pathlib.Path(entry['url']).name).read_bytes())
 assert [p['observedAt'] for p in part['points']]==[1793664000000+t*1000 for t in [0,10,100,110,130]]
 assert sum(p['breakBefore'] for p in part['points'])==3
 assert day.verify_day(output)['pointCount']==5
 one=root/'one.tar';tar(one,[('./traces/23/trace_full_abc123.json',trace(rows=[rows[0]]))]);single=root/'single';single.mkdir()
 assert day.prepare_tar([one],plan,single)['pointCount']==1
`));
test('daily payloads split without deleting observations and preserve hashes',()=>check(String.raw`
rows=[[i,38,-98,10000,400,90,0,0,{},'adsb_icao'] for i in range(3000)]
with tempfile.TemporaryDirectory() as temp:
 root=pathlib.Path(temp);archive=root/'input.tar';tar(archive,[('./traces/23/trace_full_abc123.json',trace(rows=rows))]);output=root/'day';output.mkdir()
 receipt=day.prepare_tar([archive],plan,output);catalog=json.loads((output/'replays/index.json').read_bytes())
 assert len(catalog['flights'])==2 and sum(f['pointCount'] for f in catalog['flights'])==3000
 assert all(f['partCount']==2 for f in catalog['flights'])
 day.verify_day(output)
 (output/'raw/abc123.json.gz').write_bytes(b'tampered')
 try: day.verify_day(output)
 except ValueError as error: assert str(error)=='RETAINED_DAY_INTEGRITY_FAILED'
 else: raise AssertionError('tampered bytes accepted')
`));
test('archive source, capacity, member paths and identity fail closed',()=>check(String.raw`
for mutate in [lambda m:m['assets'][0].update(digest=None),lambda m:m['assets'][0].update(browser_download_url='https://example.invalid/x'),lambda m:m['assets'][0].update(name=tag+'.tar.ab')]:
 m=json.loads(json.dumps(metadata));mutate(m)
 try: day.release_plan(D,m)
 except (ValueError,TypeError): pass
 else: raise AssertionError('unverified release accepted')
with tempfile.TemporaryDirectory() as temp:
 root=pathlib.Path(temp)
 for i,(member,hexid,expected) in enumerate([('../traces/23/trace_full_abc123.json','abc123','ARCHIVE_PATH_REJECTED'),('./traces/23/trace_full_abc123.json','def456','TRACE_IDENTITY_MISMATCH')]):
  archive=root/f'{i}.tar';tar(archive,[(member,trace(hexid))]);output=root/str(i);output.mkdir()
  try: day.prepare_tar([archive],plan,output)
  except ValueError as error: assert str(error)==expected
  else: raise AssertionError('invalid member accepted')
 archive=root/'cap.tar';tar(archive,[('./traces/23/trace_full_abc123.json',trace())]);output=root/'cap';output.mkdir();day.MAX_CANDIDATE=10
 try: day.prepare_tar([archive],plan,output)
 except ValueError as error: assert str(error)=='CANDIDATE_CAPACITY_BOUND'
 else: raise AssertionError('capacity bypassed')
`));
test('shipped full-journey files reproduce from the retained original members without silently dropping segments',()=>check(String.raw`
with tempfile.TemporaryDirectory() as temp:
 root=pathlib.Path(temp);archive=root/'source.tar';members=[]
 original=json.loads(pathlib.Path('public/data/aviation/replays/index.json').read_bytes())
 for entry in original['flights']:
  artifact=json.loads(pathlib.Path('public'+entry['url']).read_bytes())
  raw=(pathlib.Path('tests/fixtures/kansas-sky')/(pathlib.Path(artifact['sourceMember']).name+'.gz')).read_bytes()
  assert hashlib.sha256(raw).hexdigest()==artifact['sourceSha256']
  members.append((artifact['sourceMember'],raw))
 tar(archive,members);output=root/'day';output.mkdir();receipt=day.prepare_tar([archive],plan,output)
 staged=pathlib.Path('public/data/aviation/replays/days/2026-11-03')
 index=json.loads((staged/'index.json').read_bytes())
 assert receipt['pointCount']==1115 and len(index['flights'])==2
 for entry in index['flights']:
  file=pathlib.Path(entry['url']).name;actual=(staged/file).read_bytes()
  assert actual==(output/'replays'/file).read_bytes()
  assert hashlib.sha256(actual).hexdigest()==entry['sha256']
  assert entry['coverage']=='selected-recordings'
`));
