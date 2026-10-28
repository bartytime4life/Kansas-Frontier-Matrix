import { createHash } from 'node:crypto';

export function weatherRequest(url) {
  let u;
  try { u = new URL(url); } catch { return null; }
  const params = new URLSearchParams([...u.searchParams].map(([key, value]) => [key.toLowerCase(), value]));
  let group;
  if (u.hostname === 'nowcoast.noaa.gov' && params.get('request')?.toLowerCase() === 'getmap' && params.get('layers') === 'conus_base_reflectivity_mosaic') group = 'radar-tile';
  else if (u.pathname === '/api/noaa-radar/frames') group = 'radar-manifest';
  else if (u.pathname === '/api/noaa-satellite/frames') group = 'satellite-manifest';
  else if (/satellit|geocolor/i.test(u.pathname)) group = 'satellite';
  else if (/lightning/i.test(u.pathname)) group = 'lightning';
  else if (/wind|open-meteo/i.test(u.pathname + u.hostname)) group = 'wind';
  else if (/streamflow|hydrology/i.test(u.pathname)) group = 'gauges';
  else if (u.pathname === '/api/live-context' && ['nws-alerts', 'noaa-hms-smoke', 'usgs-streamflow'].includes(params.get('feed'))) group = params.get('feed');
  else return null;
  u.hash = ''; u.searchParams.sort();
  return {group, key: createHash('sha256').update(u.href).digest('hex'),
    endpoint: u.origin + u.pathname, observedAt: params.get('time')};
}

// CDP encodedDataLength is the browser-observed encoded HTTP transfer, not
// upstream server egress or radio-link bytes. Cache hits are retained as zero.
export class StormDeskNetwork {
  constructor(limit = 20000) {
    this.limit = limit; this.phase = 'startup'; this.active = new Map(); this.records = [];
    this.seen = new Set(); this.dropped = 0;
  }
  event(method, p, session = '') {
    const id = session + ':' + p.requestId;
    if (method === 'Network.requestWillBeSent') {
      const prior = this.active.get(id);
      if (prior && p.redirectResponse) {
        this.finish(id, {timestamp: p.timestamp, encodedDataLength: p.redirectResponse.encodedDataLength ?? 0}, 'redirect');
      }
      const info = weatherRequest(p.request.url);
      if (!info) return;
      if (this.records.length + this.active.size >= this.limit) { this.dropped++; return; }
      const duplicate = this.seen.has(info.key);
      const concurrentDuplicate = [...this.active.values()].some(r => r.key === info.key);
      this.seen.add(info.key);
      this.active.set(id, {...info, phase: this.phase, started: p.timestamp, duplicate, concurrentDuplicate,
        partialEncodedBytes: 0, cache: false});
      return;
    }
    const r = this.active.get(id);
    if (!r) return;
    if (method === 'Network.responseReceived') Object.assign(r, {status: p.response.status,
      responseMs: (p.timestamp - r.started) * 1000,
      cache: r.cache || p.response.fromDiskCache === true || p.response.fromServiceWorker === true,
      serviceWorker: p.response.fromServiceWorker === true});
    if (method === 'Network.requestServedFromCache') r.cache = true;
    if (method === 'Network.dataReceived') r.partialEncodedBytes += p.encodedDataLength;
    if (method === 'Network.loadingFinished') this.finish(id, p, 'finished');
    if (method === 'Network.loadingFailed') this.finish(id, p, 'failed');
  }
  finish(id, p, outcome) {
    const r = this.active.get(id);
    if (!r) return;
    this.active.delete(id);
    this.records.push({...r, completedPhase: this.phase, outcome,
      encodedBytes: p.encodedDataLength ?? r.partialEncodedBytes,
      bytesArePartial: outcome === 'failed', error: p.errorText,
      durationMs: (p.timestamp - r.started) * 1000});
  }
  snapshot() {
    return {records: this.records, inFlight: [...this.active.values()], dropped: this.dropped,
      completeCapture: this.dropped === 0,
      boundary: 'Failed-transfer bytes are partial lower bounds. Repeated URL requests include legitimate replay/cache hits; concurrent duplicates need investigation. Requests are attributed to their starting phase, completions also retain their finishing phase. Browser traffic excludes server-to-provider traffic.'};
  }
}

export function summarizeStormDeskNetwork(snapshot) {
  const groups = new Map();
  for (const r of [...snapshot.records, ...snapshot.inFlight]) {
    const key = r.phase + '/' + r.group;
    const row = groups.get(key) ?? {phase:r.phase, group:r.group, requests:0, inFlight:0, failed:0, repeatedUrls:0,
      concurrentDuplicates:0, cacheResponses:0, completedEncodedBytes:0, partialEncodedBytes:0, responseMs:[], durationMs:[]};
    row.requests++; row.inFlight += Number(!r.outcome); row.failed += Number(r.outcome === 'failed'); row.repeatedUrls += Number(r.duplicate);
    row.concurrentDuplicates += Number(r.concurrentDuplicate); row.cacheResponses += Number(r.cache);
    if (!r.outcome) row.partialEncodedBytes += r.partialEncodedBytes;
    else if (r.bytesArePartial) row.partialEncodedBytes += r.encodedBytes; else row.completedEncodedBytes += r.encodedBytes;
    if (Number.isFinite(r.responseMs)) row.responseMs.push(r.responseMs);
    if (Number.isFinite(r.durationMs)) row.durationMs.push(r.durationMs);
    groups.set(key, row);
  }
  return [...groups.values()];
}
