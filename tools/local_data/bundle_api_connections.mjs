/** Build a deterministic deployment mirror; canonical acquisition remains connectors/. */
import {readFile,writeFile,mkdir} from "node:fs/promises";
import {resolve,join} from "node:path";
import {createHash} from "node:crypto";
export const sources=["connectors/nass/quick-stats-api.mjs","connectors/drought-monitor/statistics-api.mjs","connectors/kansas/dasc-imagery-api.mjs","connectors/usgs/nldi-transect-api.mjs","connectors/microsoft/planetary-computer-api.mjs","connectors/nrcs/soil-data-access-api.mjs","connectors/openstreetmap/overpass-api.mjs","connectors/census/acs-http-api.mjs","connectors/eia/open-data-api.mjs","connectors/noaa/ncei-hosted-api.mjs","connectors/usgs/wqp-api.mjs","connectors/nrcs/scan-http-api.mjs","connectors/epa/air-quality-api.mjs","connectors/loc/maps-api.mjs","connectors/iem/asos-api.mjs","connectors/kansas/kanplan-api.mjs"];
export async function bundle(destination) {
 const root=resolve(import.meta.dirname,"../.."); const target=resolve(destination,"app/api-connections-runtime");
 await mkdir(target,{recursive:true});const manifest=[];
 const entries=[["packages/connectors-core/src/http-runtime.mjs","http-runtime.mjs"],...sources.map((p,i)=>[p,"provider-"+i+".mjs"]),["pipelines/ingest/shared/api-connections.mjs","connections.mjs"]];
 for(const [path,name] of entries) {
  const original=await readFile(join(root,path),"utf8");
  let text=original.replaceAll(/"\.\.\/\.\.\/(?:\.\.\/)?packages\/connectors-core\/src\/http-runtime\.mjs"/g,'"./http-runtime.mjs"');
  for(let i=0;i<sources.length;i++)text=text.replace('"../../../'+sources[i]+'"','"./provider-'+i+'.mjs"');
  await writeFile(join(target,name),text);
  manifest.push({sourcePath:path,sourceSha256:createHash("sha256").update(original).digest("hex"),deploymentPath:"app/api-connections-runtime/"+name,deploymentSha256:createHash("sha256").update(text).digest("hex")});
 }
 await writeFile(join(target,"manifest.json"),JSON.stringify({format:"kfm-api-mirror-v1",authority:"Deployment mirror only; connectors/ and pipelines/ own implementation. No source admission, rights, review or release.",files:manifest},null,2)+"\n");
 return manifest;
}
if(process.argv[1]===import.meta.filename){if(process.argv.length!==3)throw new Error("Pass one existing application checkout.");console.log(JSON.stringify({mirrored:(await bundle(process.argv[2])).length}));}
