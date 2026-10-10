#!/usr/bin/env node
import { realpathSync } from "node:fs";
/** Sequential, restart-safe daily runner. Hosted access stays in memory/stdin. */
import { pathToFileURL } from "node:url";
const feeds = ["census-counties","usgs-streamflow","usgs-earthquakes","nws-alerts","noaa-hms-smoke","nasa-gibs-fire-points","nifc-fire-reports","raspberry-shake-stations","fema-disaster-declarations"];
const hostedOrigin = "https://kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site";
export async function captureDaily(origin = "http://127.0.0.1:4173", token = null, request = fetch) {
  if (origin !== hostedOrigin && !/^http:\/\/127\.0\.0\.1:(?:[1-9][0-9]{3,4})$/.test(origin)) throw new Error("UNSUPPORTED_ARCHIVE_ORIGIN");
  if (origin === hostedOrigin && !token) throw new Error("HOSTED_SERVICE_ACCESS_REQUIRED");
  if (origin !== hostedOrigin && token) throw new Error("DO_NOT_SEND_HOSTED_ACCESS_TO_LOCAL_RUNTIME");
  const headers = { "X-KFM-Archive-Writer": "daily-v1", ...(token ? { "OAI-Sites-Authorization": `Bearer ${token}` } : {}) };
  const results = [];
  // Read pause/budget first; failure cannot be mistaken for an empty archive.
  const read = await request(`${origin}/api/daily-archive`, {headers,redirect:"error",signal:AbortSignal.timeout(30000)});
  if(!read.ok) throw new Error(`ARCHIVE_UNAVAILABLE_HTTP_${read.status}`);
  const before = await read.json();
  if(before.storage.paused) return {outcome:"paused",results};
  for (const feed of feeds) {
    try {
      const response = await request(`${origin}/api/daily-archive?action=capture&feed=${feed}`, {method:"POST",headers,redirect:"error",signal:AbortSignal.timeout(180000)});
      const value = await response.json();
      results.push({ feed, ok:response.ok, status:response.status, ...(response.ok?{outcome:value.outcome,id:value.id,day:value.day,captureStatus:value.status}:{error:value.error}) });
    } catch { results.push({feed,ok:false,error:"CAPTURE_REQUEST_FAILED_OR_TIMED_OUT"}); }
  }
  const after = await request(`${origin}/api/daily-archive`, {headers,redirect:"error",signal:AbortSignal.timeout(30000)});
  if(!after.ok) throw new Error(`ARCHIVE_READBACK_HTTP_${after.status}`);
  const catalog = await after.json();
  const rows=new Map(catalog.entries.filter(row=>["ready","empty","partial"].includes(row.status)).map(row=>[row.id,row]));
  // A slow run may span midnight. Verify every actual capture day independently.
  for(const day of new Set(results.filter(result=>result.ok&&result.day!==catalog.day).map(result=>result.day))) {
    if(!/^\d{4}-\d{2}-\d{2}$/.test(day??""))throw new Error("INVALID_CAPTURE_DAY");
    const response=await request(`${origin}/api/daily-archive?day=${day}`,{headers,redirect:"error",signal:AbortSignal.timeout(30000)});
    if(!response.ok)throw new Error("ARCHIVE_DAY_READBACK_FAILED");
    for(const row of (await response.json()).entries)if(["ready","empty","partial"].includes(row.status))rows.set(row.id,row);
  }
  for(const result of results) if(result.ok) { if(!rows.has(result.id)) {result.ok=false;result.error="CAPTURE_NOT_IN_CURRENT_DAY_READBACK";} else result.captureStatus=rows.get(result.id).status; }
  return {outcome:results.every(result=>result.ok&&result.captureStatus!=="partial")?"complete":"incomplete",day:catalog.day,storage:catalog.storage,results};
}
if (process.argv[1] && import.meta.url === pathToFileURL(realpathSync(process.argv[1])).href) {
  try {
    const args=process.argv.slice(2);let origin="http://127.0.0.1:4173";let token=null;
    if(args.length===2&&args[0]==="--origin") origin=args[1];
    else if(args.length===1&&args[0]==="--hosted-stdin") {
      origin=hostedOrigin;let input="";for await(const chunk of process.stdin){input+=chunk;if(input.length>4096)throw new Error("INPUT_LIMIT");}token=JSON.parse(input).token;
      if(typeof token!=="string"||!token||/[\r\n]/.test(token))throw new Error("INVALID_SERVICE_ACCESS");
    } else if(args.length) throw new Error("USAGE: --origin http://127.0.0.1:PORT or --hosted-stdin");
    const result=await captureDaily(origin,token);console.log(JSON.stringify(result));if(result.outcome==="incomplete")process.exitCode=result.results.every(item=>item.ok)?2:1;
  } catch(error) { console.error(JSON.stringify({outcome:"failed",reason:/^[A-Z0-9_: ./-]+$/.test(error.message)?error.message:"DAILY_CAPTURE_FAILED"}));process.exitCode=1; }
}
