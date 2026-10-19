import { get } from 'node:http';
import { BUILD_PROFILE, BUILD_APPLICATION } from '../scripts/build-identity.mjs';

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
    let request, settled = false;
    const finish = result => {
      if (settled) return;
      settled = true;
      clearTimeout(timer);
      request?.destroy();
      resolve({ ...base, ...result });
    };
    const timer = setTimeout(() => finish({ outcome: 'TIMEOUT', httpStatus: null }), timeoutMs);
    try {
      request = get({
        hostname: address.family === 'IPv6' ? '::1' : '127.0.0.1',
        port: address.port, path: '/api/build', agent: false, maxHeaderSize: 16384,
        headers: { Accept: 'application/json' },
      }, response => {
        const httpStatus = response.statusCode;
        if (httpStatus !== 200) { finish({ outcome: 'HTTP_ERROR', httpStatus }); return; }
        if (!/^application\/json(?:;|$)/i.test(response.headers['content-type'] ?? '')) {
          finish({ outcome: 'INVALID_IDENTITY', httpStatus }); return;
        }
        let bytes = 0;
        const chunks = [];
        response.on('error', () => finish({ outcome: 'READ_ERROR', httpStatus }));
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
      request.on('error', () => finish({ outcome: 'UNREACHABLE', httpStatus: null }));
    } catch { finish({ outcome: 'UNREACHABLE', httpStatus: null }); }
  });
}

export async function reportNodeStartup(server, write = console.info) {
  const result = await probeNodeStartup(server);
  write('KFM_NODE_STARTUP ' + JSON.stringify(result));
  return result;
}
