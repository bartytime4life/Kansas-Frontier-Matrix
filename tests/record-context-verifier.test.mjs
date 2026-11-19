import test from 'node:test';
import assert from 'node:assert/strict';
import {mkdtemp,mkdir,readFile,rm,symlink,writeFile,access} from 'node:fs/promises';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
import {ARCHIVE_ORIGIN,verifierOptions,archiveRequest,archivePage,expectedExportNames,exportsReady,prepareVerifierOutput} from '../scripts/verify-record-context-live.mjs';

test('live verification accepts loopback candidates and keeps output outside source',()=>{
 const options=verifierOptions(['--candidate=http://127.0.0.1:8797','--output=/tmp/kfm-verify','--chrome=/usr/bin/chromium'],'/source','/source');
 assert.deepEqual(options,{candidate:'http://127.0.0.1:8797',output:'/tmp/kfm-verify',chrome:'/usr/bin/chromium'});
 assert.equal(ARCHIVE_ORIGIN,'https://kansasfrontiermatrix.com');
 assert.equal(verifierOptions(['--output=/tmp/kfm-verify'],'/source').candidate,'http://127.0.0.1:8797');
 assert.equal(verifierOptions(['--candidate=http://[::1]:8797/','--output=/tmp/kfm-verify'],'/source').candidate,'http://[::1]:8797');
});

test('live verifier refuses remote/credential candidates, ambiguous flags and in-source artifacts',()=>{
 for(const candidate of ['https://kansasfrontiermatrix.com','http://10.0.0.1','http://user:password@127.0.0.1','http://127.0.0.1/app','http://127.0.0.1/?token=x','http://127.0.0.1/#fragment']){
  assert.throws(()=>verifierOptions(['--candidate='+candidate,'--output=/tmp/kfm-verify'],'/source'),/loopback/);
 }
 for(const args of [[],['--output=/source'],['--output=/source/public/verification'],['--output=/tmp/a','--output=/tmp/b'],['--output=/tmp/a','--archive=https://other.example']]){
  assert.throws(()=>verifierOptions(args,'/source','/source'));
 }
});

test('archive bridge accepts only validated pages from the five public water collections',()=>{
 const origin='http://127.0.0.1:8797';
 for(const name of ['daily-values','field-measurements','peaks','sites','series']){
  const query=new URLSearchParams({collection:'observations-usgs-'+name,limit:'50',after:JSON.stringify(['capture',50])});
  const value=archiveRequest(origin+'/api/local-data/recovered-observations?'+query,origin);
  assert.equal(value.collection,'observations-usgs-'+name);assert.equal(value.limit,50);
  assert.ok(value.path.startsWith('/api/local-data/recovered-observations?'));
 }
});

test('archive bridge rejects host, route, collection, parameter and cursor broadening',()=>{
 const origin='http://127.0.0.1:8797',base=origin+'/api/local-data/recovered-observations?collection=observations-usgs-sites';
 for(const url of [
  base.replace(origin,'https://other.example'),base.replace('recovered-observations','recovered-bulk'),base.replace('usgs-sites','faa-obstacles'),
  base+'&collection=observations-usgs-series',base+'&limit=1&limit=50',base+'&table=usgs_sites',base+'&sql=select',
  base+'&field=name&record=%5B1,1%5D',base+'&limit=51',base+'&after=%5B1%5D',base+'&after=not-json',base+'#fragment',
  base.replace(origin,'http://user:password@127.0.0.1:8797'),
 ])assert.throws(()=>archiveRequest(url,origin),url);
});

test('verified public pages retain explicit live, fresh and stale cache claims',()=>{
 const query={collection:'observations-usgs-sites',limit:1};
 for(const state of ['live','fresh','stale']){
  const page={format:'kfm-local-data-v1',dataset:'recovered-observations',collection:query.collection,total:null,count:1,
   rows:[{id:'synthetic',values:{}}],cache:{state,at:'2026-11-18T12:00:00Z'}};
  assert.deepEqual(archivePage({status:200,contentType:'application/json; charset=utf-8',text:JSON.stringify(page)},query),page);
 }
});

test('missing cache claims, unrelated data, oversized pages and failed responses cannot pass live verification',()=>{
 const query={collection:'observations-usgs-sites',limit:1};
 const page={format:'kfm-local-data-v1',dataset:'recovered-observations',collection:query.collection,total:null,count:1,rows:[{id:'synthetic',values:{}}],cache:{state:'live',at:'2026-11-18T12:00:00Z'}};
 const reply={status:200,contentType:'application/json',text:JSON.stringify(page)};
 for(const patch of [{cache:undefined},{cache:{state:'unknown',at:page.cache.at}},{cache:{state:'fresh'}},{collection:'observations-usgs-series'},{count:2},{rows:[{},{}],count:2},{total:1}]){
  assert.throws(()=>archivePage({...reply,text:JSON.stringify({...page,...patch})},query));
 }
 assert.throws(()=>archivePage({...reply,status:503},query));
 assert.throws(()=>archivePage({...reply,contentType:'application/jsonp'},query));
});

test('verification output preserves earlier evidence and rejects symlinks into the checkout before writing',async()=>{
 const root=await mkdtemp(join(tmpdir(),'kfm-verifier-output-'));
 try{
  const repo=join(root,'source');await mkdir(repo);
  const output=join(root,'evidence');await prepareVerifierOutput(output,repo);
  await writeFile(join(output,'retained.json'),'original evidence');
  await assert.rejects(prepareVerifierOutput(output,repo),/not be overwritten/);
  assert.equal(await readFile(join(output,'retained.json'),'utf8'),'original evidence');
  const link=join(root,'alias');await symlink(repo,link);
  await assert.rejects(prepareVerifierOutput(join(link,'reports','new'),repo),/symlinks/);
  await assert.rejects(access(join(repo,'reports')),{code:'ENOENT'});
 }finally{await rm(root,{recursive:true,force:true});}
});

test('only the named JSON and story exports count as download evidence',()=>{
 const names=expectedExportNames('observations-usgs-daily-values');
 const unrelated=['downloads.html','observations-usgs-daily-values-lab.json'];
 assert.equal(exportsReady(unrelated,'observations-usgs-daily-values'),false);
 assert.equal(exportsReady([...unrelated,'observations-usgs-daily-values-research-brief.md'],'observations-usgs-daily-values'),true);
 assert.equal(exportsReady(['other-lab.json','other-research-brief.md'],'observations-usgs-daily-values'),false);
 assert.deepEqual(names,['observations-usgs-daily-values-lab.json','observations-usgs-daily-values-research-brief.md']);
 assert.throws(()=>expectedExportNames('../other'));
});
