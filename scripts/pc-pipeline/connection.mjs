// One public health request; never reads PC credentials, datasets or SQL config.
import { ORIGIN, parse, timestamp } from '../../server/pipeline-contract.mjs';

export const CONNECTION_ENDPOINT = ORIGIN + '/api/database-connection';
const LIMIT = 8192;
const REASONS = ['configuration-missing', 'private-provider-network-required', 'verified-tls-unavailable', 'authentication-failed', 'connection-unavailable'];
const TLS_FAILURES = ['server-does-not-support-tls', 'provider-ca-required', 'certificate-hostname-mismatch', 'provider-tls-configuration-required'];
const TRANSPORTS = ['verified-tls', 'host-loopback', 'provider-private-network'];

function validate(value, status) {
  const keys = ['format', 'mode', 'checkedAt', 'cacheSeconds', 'uploadsEnabled', 'sqlWritesEnabled', 'connected', 'state', 'transport', 'reason', 'tlsFailure'];
  if (!value || Array.isArray(value) || Object.keys(value).some(key => !keys.includes(key))
    || value.format !== 'kfm-database-connection-v1' || value.mode !== 'connection-only'
    || value.cacheSeconds !== 60 || value.uploadsEnabled !== false || value.sqlWritesEnabled !== false) throw new Error('invalid-response');
  timestamp(value.checkedAt);
  if (status === 200 && value.connected === true && value.state === 'connected' && TRANSPORTS.includes(value.transport)
    && value.reason === undefined && value.tlsFailure === undefined) {
    return { connected: true, state: value.transport === 'verified-tls' ? 'connected' : 'held', transport: value.transport,
      ...(value.transport !== 'verified-tls' ? { reason: 'verified-tls-required' } : {}) };
  }
  if (status === 503 && value.connected === false && value.state === 'unavailable' && REASONS.includes(value.reason)
    && value.transport === undefined && (value.reason === 'verified-tls-unavailable'
      ? TLS_FAILURES.includes(value.tlsFailure) : value.tlsFailure === undefined)) {
    return { connected: false, state: 'unavailable', reason: value.reason,
      ...(value.tlsFailure ? { tlsFailure: value.tlsFailure } : {}) };
  }
  throw new Error('invalid-response');
}

export async function connectionCheck({ fetcher = fetch, timeoutMs = 10000, environment = process.env } = {}) {
  // Dependency injection is for synthetic tests only; no CLI URL/timeout override.
  if (!Number.isInteger(timeoutMs) || timeoutMs < 1 || timeoutMs > 10000) throw new Error('CONNECTION_BUDGET_INVALID');
  const requestedAt = new Date().toISOString();
  const controller = new AbortController();
  let reader, body, timer, httpStatus = null, received = false, timedOut = false;
  const deadline = new Promise((_, reject) => {
    timer = setTimeout(() => { timedOut = true; controller.abort(); reject(new Error('request-timeout')); }, timeoutMs);
  });
  let outcome;
  try {
    const operation = (async () => {
      if (environment.NODE_TLS_REJECT_UNAUTHORIZED === '0') return { connected: false, state: 'held', reason: 'tls-verification-disabled' };
      const response = await fetcher(CONNECTION_ENDPOINT, { method: 'GET', redirect: 'manual', credentials: 'omit',
        cache: 'no-store', headers: { Accept: 'application/json' }, signal: controller.signal });
      received = true;
      body = response.body;
      httpStatus = response.status;
      if (response.redirected || (response.url && response.url !== CONNECTION_ENDPOINT)
        || ![200, 503].includes(httpStatus) || !/^application\/json(?:\s*;|$)/i.test(response.headers.get('content-type') ?? '')) throw new Error('invalid-response');
      const length = response.headers.get('content-length');
      const encoding = response.headers.get('content-encoding')?.trim().toLowerCase() || 'identity';
      if (length !== null && (!/^\d+$/.test(length) || Number(length) > LIMIT)) throw new Error('invalid-response');
      if (!response.body) throw new Error('invalid-response');
      reader = response.body.getReader();
      let count = 0;
      const chunks = [];
      while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        count += value.byteLength;
        if (count > LIMIT) throw new Error('invalid-response');
        chunks.push(Buffer.from(value));
      }
      // Native fetch decodes compression but retains the encoded Content-Length.
      // The decoded stream always has its own cap; fetch enforces wire framing.
      if (encoding === 'identity' && length !== null && Number(length) !== count) throw new Error('invalid-response');
      const value = parse(Buffer.concat(chunks, count), LIMIT);
      return { ...validate(value, httpStatus), serverCheckedAt: value.checkedAt, serverCacheSeconds: value.cacheSeconds };
    })();
    outcome = await Promise.race([operation, deadline]);
  } catch {
    // Never copy driver text, URLs, headers, response bodies or arbitrary errors.
    outcome = { connected: false, state: 'unavailable', reason: timedOut ? 'request-timeout' : received ? 'invalid-response' : 'hosting-unreachable' };
  } finally {
    clearTimeout(timer);
    controller.abort();
    if (reader) void reader.cancel().catch(() => {});
    else if (body) void body.cancel().catch(() => {});
  }
  return { format: 'kfm-pc-database-connection-receipt-v1', mode: 'connection-only', endpoint: CONNECTION_ENDPOINT,
    requestedAt, completedAt: new Date().toISOString(), httpStatus, uploadsEnabled: false, sqlWritesEnabled: false,
    ...outcome };
}
