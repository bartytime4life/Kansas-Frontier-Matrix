import { mkdir, writeFile, rename } from 'node:fs/promises';
import { join } from 'node:path';
import { DEMO_IDS } from './scenarios.mjs';

export const CAPTURE_DIRECTORY = '/tmp/kfm-welcome-demo-recordings';
export const MAX_CAPTURE_BYTES = 32 * 1024 * 1024;
const ids = new Set(DEMO_IDS);
export function captureRequestTarget(rawUrl) {
  const frame = /^\/__welcome-demo-capture\/(weather|science|government|rivers|underground|history|transport|farming)-([12])\.frame-(\d{3})\.jpg$/.exec(rawUrl ?? '');
  if (frame) return Number(frame[3]) < 120 && ids.has(`${frame[1]}-${frame[2]}`) ? { file: `${frame[1]}-${frame[2]}.frame-${frame[3]}.jpg`, extension: 'jpg' } : null;
  const match = /^\/__welcome-demo-capture\/(weather|science|government|rivers|underground|history|transport|farming)-([12])(\.(?:rejected|preview))?\.(webm|json|jpg|png)$/.exec(rawUrl ?? '');
  if (!match || !ids.has(`${match[1]}-${match[2]}`)) return null;
  return { file: `${match[1]}-${match[2]}${match[3] ?? ""}.${match[4]}`, extension: match[4] };
}
export function captureOriginAllowed(origin, host, remoteAddress) {
  if (!['127.0.0.1', '::1', '::ffff:127.0.0.1'].includes(remoteAddress)) return false;
  try {
    const url = new URL(origin);
    return url.protocol === 'http:' && url.hostname === '127.0.0.1' && url.host === host;
  } catch { return false; }
}
/** Deliberately registered only by Vite serve with an explicit local environment flag. */
export function welcomeDemoCapturePlugin() {
  return {
    name: 'kfm-local-welcome-demo-capture', apply: 'serve',
    configureServer(server) {
      server.middlewares.use(async (request, response, next) => {
        if (!request.url?.startsWith('/__welcome-demo-capture/')) return next();
        response.setHeader('Cache-Control', 'no-store');
        const target = captureRequestTarget(request.url);
        if (!target || request.method !== 'POST') { response.statusCode = 404; response.end('Unknown capture'); return; }
        if (!captureOriginAllowed(request.headers.origin, request.headers.host, request.socket.remoteAddress)) { response.statusCode = 403; response.end('Local recording origin required'); return; }
        const expected = target.extension === 'webm' ? 'video/webm' : target.extension === 'jpg' ? 'image/jpeg' : target.extension === 'png' ? 'image/png' : 'application/json';
        if ((request.headers['content-type'] ?? '').split(';')[0] !== expected) { response.statusCode = 415; response.end('Unexpected capture type'); return; }
        const limit = target.extension === 'json' ? 32_768 : ['jpg', 'png'].includes(target.extension) ? 2_000_000 : MAX_CAPTURE_BYTES;
        const declared = Number(request.headers['content-length']);
        if (Number.isFinite(declared) && declared > limit) { response.statusCode = 413; response.end('Capture exceeds limit'); return; }
        let size = 0;
        const chunks = [];
        try {
          for await (const chunk of request) {
            size += chunk.length;
            if (size > limit) { response.statusCode = 413; response.end('Capture exceeds limit'); return; }
            chunks.push(chunk);
          }
          if (!size) { response.statusCode = 400; response.end('Empty capture'); return; }
          const body = Buffer.concat(chunks);
          if (target.extension === 'json') {
            const metadata = JSON.parse(body.toString('utf8'));
            if (metadata.id !== target.file.replace(/(?:\.(?:rejected|preview))?\.json$/, '') || !['recorded-software-demo', 'rendered-software-tour'].includes(metadata.kind)) throw new Error('Invalid metadata');
          } else if (target.extension === 'webm' && body.subarray(0, 4).toString('hex') !== '1a45dfa3') throw new Error('Invalid WebM');
          else if (target.extension === 'jpg' && body.subarray(0, 2).toString('hex') !== 'ffd8') throw new Error('Invalid JPEG');
          else if (target.extension === 'png' && body.subarray(0, 8).toString('hex') !== '89504e470d0a1a0a') throw new Error('Invalid PNG');
          await mkdir(CAPTURE_DIRECTORY, { recursive: true, mode: 0o700 });
          const temporary = join(CAPTURE_DIRECTORY, `${target.file}.partial`);
          await writeFile(temporary, body, { mode: 0o600 });
          await rename(temporary, join(CAPTURE_DIRECTORY, target.file));
          response.statusCode = 201; response.end('Saved local capture');
        } catch { response.statusCode = 400; response.end('Invalid or interrupted capture'); }
      });
    },
  };
}
