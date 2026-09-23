/** Read-only, explicit-run transport diagnostics. Importing this module does not fetch.
 * Paths are from the historical v40 mirror, NOT asserted current Site configuration. */

export const REFERENCE_MIRROR = 'c4e5ebe54cba9d7ca9bbee108b442bdf68763f58';
const siteHost = 'kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site';
const json = (id, path) => Object.freeze({ id, path, kind: 'json' });
const raster = (id) => Object.freeze({ id, path: null, kind: 'renderer' });
export const CONNECTIONS = Object.freeze([
  json('census-counties', '/api/live-context?feed=census-counties'),
  json('usgs-streamflow', '/api/hydrology/streamflow?mode=network&range=24h'),
  json('noaa-nwps-gauges', '/api/hydrology/noaa?mode=network'),
  raster('usgs-3dhp-hydrography'),
  raster('usgs-wbd-watersheds'),
  raster('noaa-nwm-analysis'),
  raster('noaa-nwm-short-range'),
  json('usgs-earthquakes', '/api/live-context?feed=usgs-earthquakes'),
  json('noaa-hms-smoke', '/api/live-context?feed=noaa-hms-smoke'),
  raster('nasa-firms-active-fire'),
  json('raspberry-shake-stations', '/api/live-context?feed=raspberry-shake-stations'),
  Object.freeze({ id: 'usgs-3dep-hillshade', kind: 'png', path: '/api/terrain-tile?kind=hillshade&z=8&x=58&y=98' }),
  Object.freeze({ id: 'usgs-3dep-slope', kind: 'png', path: '/api/terrain-tile?kind=slope&z=8&x=58&y=98' }),
  json('nws-alerts', '/api/live-context?feed=nws-alerts'),
  json('nws-radar', '/api/noaa-radar/frames'),
]);
export function validateOrigin(value) {
  const url = new URL(value);
  const local = ['localhost', '127.0.0.1', '[::1]'].includes(url.hostname);
  const browserPreview = typeof globalThis.location !== 'undefined'
    && url.origin === globalThis.location.origin && url.protocol === 'https:';
  const hosted = url.hostname === siteHost && url.protocol === 'https:' && !url.port;
  if (url.username || url.password || url.pathname !== '/' || url.search || url.hash
    || (!hosted && !browserPreview && !(local && ['http:', 'https:'].includes(url.protocol)))) {
    throw new Error('Use only the existing HTTPS Explorer origin or an explicit loopback preview origin.');
  }
  return url.origin;
}
const MAX_BYTES = 4 * 1024 * 1024;
async function readBounded(response, signal) {
  const declared = response.headers.get('content-length');
  if (declared && /^\d+$/.test(declared) && Number(declared) > MAX_BYTES) throw new Error('BODY_LIMIT');
  if (!response.body) return new Uint8Array();
  const reader = response.body.getReader(), chunks = [];
  let length = 0;
  const cancel = () => { void reader.cancel().catch(() => {}); };
  signal.addEventListener('abort', cancel, { once: true });
  try {
    while (true) {
      if (signal.aborted) throw new Error('REQUEST_ABORTED');
      const { done, value } = await reader.read();
      if (signal.aborted) throw new Error('REQUEST_ABORTED');
      if (done) break;
      length += value.byteLength;
      if (length > MAX_BYTES) throw new Error('BODY_LIMIT');
      chunks.push(value);
    }
    const bytes = new Uint8Array(length);
    let offset = 0;
    for (const chunk of chunks) { bytes.set(chunk, offset); offset += chunk.byteLength; }
    return bytes;
  } finally {
    signal.removeEventListener('abort', cancel);
    void reader.cancel().catch(() => {});
    reader.releaseLock();
  }
}
function pngHeader(bytes) {
  const signature = [137, 80, 78, 71, 13, 10, 26, 10];
  if (bytes.length < 33 || signature.some((b, i) => bytes[i] !== b)) return false;
  const view = new DataView(bytes.buffer, bytes.byteOffset, bytes.byteLength);
  return view.getUint32(8) === 13 && view.getUint32(12) === 0x49484452
    && view.getUint32(16) === 256 && view.getUint32(20) === 256;
}
async function probeOne(connection, origin, fetchImpl, timeoutMs, signal) {
  const started = Date.now();
  const base = { id: connection.id, path: connection.path, httpStatus: null,
    payloadValidated: false, freshnessVerified: false, rendered: false };
  if (!connection.path) return { ...base, status: 'NOT_PROBED_RENDERER', durationMs: 0 };
  if (signal?.aborted) return { ...base, status: 'CANCELLED', durationMs: 0 };
  const controller = new AbortController();
  let rejectCancellation;
  const cancellation = new Promise((_, reject) => { rejectCancellation = reject; });
  const cancel = () => { controller.abort(); rejectCancellation(new Error('CANCELLED')); };
  signal?.addEventListener('abort', cancel, { once: true });
  let timer, timedOut = false, response;
  const execute = async () => {
    response = await fetchImpl(`${origin}${connection.path}`, { method: 'GET',
      credentials: 'same-origin', redirect: 'manual', cache: 'no-store', signal: controller.signal });
    base.httpStatus = response.status;
    if (response.type === 'opaqueredirect' || (response.status >= 300 && response.status < 400)) return 'REDIRECT_OR_AUTH_UNVERIFIED';
    if ([401, 403].includes(response.status)) return 'AUTH_REQUIRED';
    if (response.status === 404) return 'ROUTE_MISSING';
    if (response.status === 429) return 'RATE_LIMITED';
    if (response.status === 503 && (response.headers.get('content-type') ?? '').split(';')[0].trim().toLowerCase() === 'application/json') {
      const bytes = await readBounded(response, controller.signal);
      try {
        const body = JSON.parse(new TextDecoder('utf-8', { fatal: true }).decode(bytes));
        if (body?.code === 'KFM_API_NOT_CONFIGURED') return 'API_NOT_CONFIGURED';
      } catch { /* Still a failed adapter response; never a healthy feed. */ }
    }
    if (response.status >= 500) return 'UPSTREAM_OR_ADAPTER_ERROR';
    if (response.status === 204) return 'EMPTY_HTTP_RESPONSE_UNVALIDATED';
    if (response.status !== 200) return 'HTTP_ERROR';
    const media = (response.headers.get('content-type') ?? '').split(';')[0].trim().toLowerCase();
    if (connection.kind === 'json' && !['application/json', 'application/geo+json'].includes(media)) return 'UNEXPECTED_MEDIA_TYPE';
    if (connection.kind === 'png' && media !== 'image/png') return 'UNEXPECTED_MEDIA_TYPE';
    const bytes = await readBounded(response, controller.signal);
    if (connection.kind === 'png') return pngHeader(bytes) ? 'PNG_HEADER_ONLY_RENDER_UNPROVED' : 'INVALID_PNG_HEADER';
    try {
      JSON.parse(new TextDecoder('utf-8', { fatal: true }).decode(bytes));
      return 'JSON_RECEIVED_SCHEMA_UNVERIFIED';
    } catch { return 'INVALID_JSON_OR_UTF8'; }
  };
  try {
    const status = await Promise.race([execute(), cancellation, new Promise((_, reject) => {
      timer = setTimeout(() => { timedOut = true; controller.abort(); reject(new Error('TIMEOUT')); }, timeoutMs);
    })]);
    return { ...base, status, durationMs: Date.now() - started };
  } catch (error) {
    return { ...base, status: signal?.aborted ? 'CANCELLED' : timedOut ? 'TIMEOUT' : error?.message === 'BODY_LIMIT' ? 'BODY_LIMIT' : 'NETWORK_OR_STREAM_ERROR',
      durationMs: Date.now() - started };
  } finally {
    clearTimeout(timer);
    signal?.removeEventListener('abort', cancel);
    controller.abort();
    if (response?.body && !response.body.locked) void response.body.cancel().catch(() => {});
  }
}
/** No cookies/tokens are accepted as arguments and no response bodies are logged.
 * Node has no browser session: redirects/auth failures are not provider failures. */
export async function probeContextConnections({ origin, fetchImpl = globalThis.fetch, timeoutMs = 8000, signal = undefined } = {}) {
  const target = validateOrigin(origin);
  if (signal !== undefined && !(signal instanceof AbortSignal)) throw new Error('Invalid cancellation signal.');
  if (typeof fetchImpl !== 'function' || !Number.isInteger(timeoutMs) || timeoutMs < 10 || timeoutMs > 15000) {
    throw new Error('Invalid probe options.');
  }
  const results = new Array(CONNECTIONS.length);
  let cursor = 0;
  async function worker() {
    while (cursor < CONNECTIONS.length) {
      const index = cursor++;
      results[index] = await probeOne(CONNECTIONS[index], target, fetchImpl, timeoutMs, signal);
    }
  }
  await Promise.all([worker(), worker()]);
  return { schema: 'kfm-context-transport-probe/v1', observedAt: new Date().toISOString(), origin: target,
    referenceMirror: REFERENCE_MIRROR, activeSiteParity: 'UNVERIFIED',
    limits: { concurrentRequests: 2, timeoutMs, maxResponseBytes: MAX_BYTES },
    operationalAcceptance: 'NOT_ESTABLISHED', results };
}
