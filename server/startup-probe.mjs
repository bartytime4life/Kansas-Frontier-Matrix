import { get } from 'node:http';
import { BUILD_PROFILE, BUILD_APPLICATION } from '../scripts/build-identity.mjs';

const transportCodes = new Set([
  'ECONNREFUSED', 'ECONNRESET', 'ETIMEDOUT', 'EACCES', 'EPERM',
  'ENETUNREACH', 'EHOSTUNREACH', 'EADDRNOTAVAIL', 'EPIPE',
  'ERR_ACCESS_DENIED', 'ERR_NETWORK_ACCESS_DENIED', 'ERR_SOCKET_CLOSED',
  'HPE_HEADER_OVERFLOW', 'HPE_INVALID_CONSTANT',
]);
const transportCode = error => transportCodes.has(error?.code) ? error.code : 'OTHER_ERROR';

// One local read of an already-public route. No provider calls, model load,
// private-store inspection, secrets, request headers or response text are logged.
export function probeNodeStartup(server, { timeoutMs = 5000 } = {}) {
  const address = server.address();
  const base = {
    profile: 'kfm.node-startup/v1', node: process.versions.node,
    production: process.env.NODE_ENV === 'production',
    listenPort: typeof address === 'object' && address ? address.port : null,
  };
  if (!address || typeof address === 'string') return Promise.resolve({ ...base, outcome: 'NOT_LISTENING', httpStatus: null });
  return new Promise(resolve => {
    let request, settled = false, transportStage = 'REQUEST_SETUP';
    const finish = result => {
      if (settled) return;
      settled = true;
      clearTimeout(timer);
      request?.destroy();
      resolve({ ...base, transportStage, ...result });
    };
    const timer = setTimeout(() => finish({ outcome: 'TIMEOUT', httpStatus: null }), timeoutMs);
    try {
      request = get({
        hostname: address.family === 'IPv6' ? '::1' : '127.0.0.1',
        port: address.port, path: '/api/build', agent: false, maxHeaderSize: 16384,
        headers: { Accept: 'application/json', 'X-KFM-Startup-Probe': '1' },
      }, response => {
        transportStage = 'RESPONSE_RECEIVED';
        const httpStatus = response.statusCode;
        if (httpStatus !== 200) { finish({ outcome: 'HTTP_ERROR', httpStatus }); return; }
        if (!/^application\/json(?:;|$)/i.test(response.headers['content-type'] ?? '')) {
          finish({ outcome: 'INVALID_IDENTITY', httpStatus }); return;
        }
        let bytes = 0;
        const chunks = [];
        response.on('error', error => finish({ outcome: 'READ_ERROR', httpStatus, errorCode: transportCode(error) }));
        response.on('data', chunk => {
          if (settled) return;
          bytes += chunk.length;
          if (bytes > 4096) { finish({ outcome: 'RESPONSE_TOO_LARGE', httpStatus }); return; }
          chunks.push(chunk);
        });
        response.on('end', () => {
          if (settled) return;
          let identity;
          try { identity = JSON.parse(Buffer.concat(chunks).toString('utf8')); } catch { /* Reject below. */ }
          if (identity?.profile !== BUILD_PROFILE || identity.application !== BUILD_APPLICATION ||
              !/^sha256:[a-f0-9]{64}$/.test(identity.sourceDigest) ||
              !Number.isSafeInteger(identity.sourceFileCount) || identity.sourceFileCount < 1) {
            finish({ outcome: 'INVALID_IDENTITY', httpStatus }); return;
          }
          finish({ outcome: 'LOOPBACK_BUILD_READY', httpStatus,
            sourceDigest: identity.sourceDigest, sourceFileCount: identity.sourceFileCount });
        });
      });
      transportStage = 'CONNECTING';
      request.on('socket', socket => {
        if (!socket.connecting) transportStage = 'CONNECTED';
        else socket.once('connect', () => { transportStage = 'CONNECTED'; });
      });
      request.on('error', error => finish({ outcome: 'UNREACHABLE', httpStatus: null, errorCode: transportCode(error) }));
    } catch (error) { finish({ outcome: 'UNREACHABLE', httpStatus: null, errorCode: transportCode(error) }); }
  });
}

export async function reportNodeStartup(server, write = console.info) {
  const result = await probeNodeStartup(server);
  write('KFM_NODE_STARTUP ' + JSON.stringify(result));
  return result;
}

// Observe only the first existing public root/build read for at most one minute.
// This adds no endpoint and grants no authority. It logs fixed route categories
// and an HTTP status, never URLs, query text, headers, bodies or client identity.
export function reportPublicDelivery(server, { timeoutMs = 60000, write = console.info } = {}) {
  return new Promise(resolve => {
    const base = { profile: 'kfm.node-delivery/v1' };
    let settled = false, route = null, trackedResponse;
    const finish = (outcome, httpStatus = null) => {
      if (settled) return;
      settled = true;
      clearTimeout(timer);
      server.removeListener('request', onRequest);
      server.removeListener('close', onServerClose);
      trackedResponse?.removeListener('finish', onFinished);
      trackedResponse?.removeListener('close', onResponseClose);
      const result = { ...base, outcome, route, httpStatus };
      write('KFM_NODE_DELIVERY ' + JSON.stringify(result));
      resolve(result);
    };
    const onFinished = () => finish('RESPONSE_FINISHED', trackedResponse.statusCode);
    const onResponseClose = () => finish('RESPONSE_CLOSED', trackedResponse.headersSent ? trackedResponse.statusCode : null);
    const onServerClose = () => finish('SERVER_CLOSED');
    const onRequest = (request, response) => {
      if (route || !['GET', 'HEAD'].includes(request.method) ||
          !['/', '/api/build'].includes(request.url) ||
          request.headers['x-kfm-startup-probe'] === '1') return;
      route = request.url === '/' ? 'ROOT' : 'BUILD';
      trackedResponse = response;
      server.removeListener('request', onRequest);
      response.once('finish', onFinished);
      response.once('close', onResponseClose);
      write('KFM_NODE_DELIVERY ' + JSON.stringify({ ...base, outcome: 'REQUEST_RECEIVED', route, httpStatus: null }));
    };
    const timer = setTimeout(() => finish(route ? 'RESPONSE_TIMEOUT' : 'NO_PUBLIC_REQUEST_OBSERVED'), timeoutMs);
    timer.unref?.();
    if (!server.listening) { finish('NOT_LISTENING'); return; }
    server.prependListener('request', onRequest);
    server.once('close', onServerClose);
  });
}
