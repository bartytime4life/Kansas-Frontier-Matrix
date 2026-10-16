// Private startup diagnostic: no model load, allocation test, file scan or public route.
const positive = read => {
 try { const value=read(); return Number.isSafeInteger(value)&&value>0?value:null; }
 catch { return null; }
};
export function readHostedResourceSnapshot({runtime=process,now=()=>new Date().toISOString()}={}) {
 return {
  profile:'kfm.hosted-ai-resources/20261016/v1',observedAt:now(),
  node:runtime.versions?.node??null,platform:runtime.platform??null,arch:runtime.arch??null,
  constrainedMemoryBytes:positive(()=>runtime.constrainedMemory()),
  availableMemoryBytes:positive(()=>runtime.availableMemory()),
  processRssBytes:positive(()=>runtime.memoryUsage().rss),
  interpretation:'OS observations only. Null is unknown, never unlimited. Shared, ancestor and provider limits need confirmation; do not allocate all reported free memory.',
 };
}
export function reportHostedResources(enabled=process.env.KFM_HOSTED_AI_RESOURCE_PROBE==='1',read=readHostedResourceSnapshot,write=value=>console.info(value)) {
 if(!enabled)return {status:'DISABLED'};
 try { write('KFM_HOSTED_RESOURCE_REPORT '+JSON.stringify(read()));return {status:'REPORTED'}; }
 catch { write('KFM_HOSTED_RESOURCE_REPORT_UNAVAILABLE');return {status:'UNAVAILABLE'}; }
}
