import { createServer } from "node:http";
import assert from "node:assert/strict";
import { mkdtempSync, mkdirSync, writeFileSync, readFileSync, rmSync, symlinkSync } from "node:fs";
import { tmpdir } from "node:os";
import path from "node:path";
import { spawnSync } from "node:child_process";
import { gzipSync } from "node:zlib";
import test from "node:test";
import { HOLD_MANIFEST, validateSubsurfacePublic } from "../scripts/validate-subsurface-public.mjs";

function temporary(t) { const root = mkdtempSync(path.join(tmpdir(), "kfm-static-test-")); t.after(() => rmSync(root, { recursive: true, force: true })); return root; }
function held(root) { mkdirSync(path.join(root,"data/subsurface"),{recursive:true}); writeFileSync(path.join(root,"data/subsurface/manifest.json"),JSON.stringify(HOLD_MANIFEST)); }
test("real public tree contains only an empty hold and the unchanged separate survey asset",()=>{
 assert.deepEqual(validateSubsurfacePublic(path.resolve("public")),[]);
 assert.deepEqual(JSON.parse(readFileSync("public/data/subsurface/manifest.json","utf8")),HOLD_MANIFEST);
});
test("guard rejects locator, undeclared tiles, nested carriers and false approval metadata",t=>{
 const root=temporary(t);held(root);const carrier=path.join(root,"data/subsurface/locator.json.gz");
 writeFileSync(carrier,gzipSync("[]"));assert.ok(validateSubsurfacePublic(root).length);rmSync(carrier);
 const nested=path.join(root,"data/subsurface/archive");mkdirSync(nested);writeFileSync(path.join(nested,"tile.bin"),"restricted");assert.ok(validateSubsurfacePublic(root).length);rmSync(nested,{recursive:true});
 writeFileSync(path.join(root,"data/subsurface/manifest.json"),JSON.stringify({...HOLD_MANIFEST,release:{approved:true}}));assert.ok(validateSubsurfacePublic(root).length);
});
test("renamed plain and gzip carriers and symlink aliases are held; unrelated JSON remains usable",t=>{
 const root=temporary(t), file=path.join(root,"renamed.json");
 writeFileSync(file,JSON.stringify({details:{locator:".historical-entry"},coordinates:[0,0],kind:"event"}));assert.deepEqual(validateSubsurfacePublic(root),[]);
 const feature={type:"Feature",geometry:{type:"Point",coordinates:[0,0]},properties:{id:"wwc5-000",sourceId:"kgs-wwc5"}};
 writeFileSync(file,JSON.stringify({type:"FeatureCollection",features:[feature]}));assert.ok(validateSubsurfacePublic(root).length);rmSync(file);
 const rows=[{kind:"well",sourceId:"kgs-wwc5",coordinates:[0,0],intervals:[]}];writeFileSync(file,JSON.stringify(rows));assert.ok(validateSubsurfacePublic(root).length);rmSync(file);
 writeFileSync(path.join(root,"renamed.gz"),gzipSync(JSON.stringify([["wwc5-000", "", [0,0],"tile"]])));assert.ok(validateSubsurfacePublic(root).length);rmSync(path.join(root,"renamed.gz"));
 for(const name of ["renamed.txt","renamed.dat"]) { const alias=path.join(root,name);writeFileSync(alias,name.endsWith("txt")?JSON.stringify(rows):gzipSync(JSON.stringify(rows)));assert.ok(validateSubsurfacePublic(root).length);rmSync(alias); }
 symlinkSync(path.resolve("public/data/subsurface/geophysics.json"),file);assert.ok(validateSubsurfacePublic(root).length);
});
test("direct generator calls deny deployed, repository, traversal and symlink paths before IO",t=>{
 const root=temporary(t);const code=`import importlib.util, pathlib, sys
s=importlib.util.spec_from_file_location('subsurface','scripts/prepare-subsurface.py')
m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
root=pathlib.Path(sys.argv[1]);site=pathlib.Path.cwd()
inputs=root/'cache'; safe=root/'review'
m.validate_storage(inputs,safe)
assert m.interval('0','10','original shale')['description']=='original shale'
assert m.interval('10','5','bad') is None
assert m.kansas_coordinates('',38) is None
assert m.record_date('10-Jul-1978')=='1978-07-10'
for output in [site/'public/data/subsurface',site/'public/../candidate',root/'public'/'alias',root/'dist',root/'published']:
 try: m.build(inputs,output)
 except ValueError: pass
 else: raise AssertionError('unsafe output accepted')
assert not inputs.exists()
assert not safe.exists()
(root/'alias').symlink_to(site/'public',target_is_directory=True)
try: m.build(inputs,root/'alias/data/subsurface')
except ValueError: pass
else: raise AssertionError('symlink output accepted')
try: m.build(site/'cache',safe)
except ValueError: pass
else: raise AssertionError('tracked input accepted')
`;
 const result=spawnSync("python3",["-c",code,root],{encoding:"utf8"});assert.equal(result.status,0,result.stderr);
 const cli=spawnSync("python3",["scripts/prepare-subsurface.py","--input-dir",path.join(root,"cache")],{encoding:"utf8"});assert.equal(cli.status,2);assert.match(cli.stderr,/--output-dir/);
});
test("direct Vite/build/start and both local serving branches include the asset denial gate",()=>{
 assert.match(readFileSync("vite.config.ts","utf8"),/execFileSync[\s\S]*validate-subsurface-public/);
 assert.match(readFileSync("scripts/build-verified.sh","utf8"),/validate-subsurface-public[\s\S]*vinext[\s\S]*validate-subsurface-public/);
 assert.match(readFileSync("scripts/serve-local-worker.mjs","utf8"),/validateSubsurfacePublic\(client\)/);
 const repositoryRoot=process.env.KFM_WEATHER_REPOSITORY_ROOT;
 if(repositoryRoot&&!path.isAbsolute(repositoryRoot))throw new Error("KFM_WEATHER_REPOSITORY_ROOT must be absolute");
 const shell=readFileSync(repositoryRoot?path.join(repositoryRoot,"apps/site/serve-local.sh"):"../serve-local.sh","utf8");assert.ok(shell.indexOf("validate-subsurface-public.mjs dist/client")<shell.indexOf('exec node scripts/serve-local-worker'));
 assert.match(JSON.parse(readFileSync("package.json","utf8")).scripts.prestart,/validate:subsurface-public.*dist\/client/);
});

test("private candidate generation preserves deterministic intervals and relative references with synthetic inputs",t=>{
 const root=temporary(t);const code=`import importlib.util, pathlib, sys, types, json, gzip
s=importlib.util.spec_from_file_location('subsurface','scripts/prepare-subsurface.py')
m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
root=pathlib.Path(sys.argv[1]); output=root/'quarantine'/'candidate'
sys.modules['pyproj']=types.SimpleNamespace(__version__='3.7.1',proj_version_str='synthetic',Transformer=types.SimpleNamespace(from_pipeline=lambda _:None))
m.pinned_download=lambda *args:None
m.rows=lambda _,name,stats: iter({'wwc5_wells':[{'WELL_ID':'000','NAD83_LONGITUDE':'-99','NAD83_LATITUDE':'38','WELL_DEPTH':'10','LONG_LAT_TYPE':'GPS','COMPLE_DATE':'10-Jul-1978','COUNTY':'Synthetic'}],'wwc5_lith_log':[{'WELL_ID':'000','TOP':'0','BOTTOM':'10','LOG':'synthetic shale'}],'interpreted_logs':[],'coreLib':[]}[name])
m.build(root/'cache',output)
manifest=json.loads((output/'manifest.json').read_text())
assert manifest['status']=='RESTRICTED_REVIEW_REQUIRED'
assert manifest['totals']['wellCount']==1
assert manifest['locator']['url']=='locator.json.gz'
tile=manifest['tiles'][0]
assert not tile['url'].startswith('/')
record=json.loads(gzip.decompress((output/tile['url']).read_bytes()))[0]
assert record['intervals']==[{'top':0.0,'bottom':10.0,'description':'synthetic shale'}]
`;
 const result=spawnSync("python3",["-c",code,root],{encoding:"utf8"});assert.equal(result.status,0,result.stderr);
});

test("unauthenticated static retrieval returns only the hold notice; original locator and tile paths are absent",async t=>{
 const root=path.resolve("public");
 const server=createServer((request,response)=>{
  const file=path.join(root,new URL(request.url,"http://localhost").pathname);
  try { response.end(readFileSync(file)); } catch { response.writeHead(404);response.end("Unavailable"); }
 });
 await new Promise(resolve=>server.listen(0,"127.0.0.1",resolve));t.after(()=>new Promise(resolve=>server.close(resolve)));
 const base=`http://127.0.0.1:${server.address().port}`;
 const manifest=await fetch(base+"/data/subsurface/manifest.json");assert.equal(manifest.status,200);assert.deepEqual(await manifest.json(),HOLD_MANIFEST);
 for(const name of ["locator.json.gz","tile-155-253.json.gz"])assert.equal((await fetch(base+"/data/subsurface/"+name)).status,404);
});
