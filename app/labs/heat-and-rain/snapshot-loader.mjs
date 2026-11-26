import { validateSnapshot } from './climate-model.mjs';

const LIMIT = 1024 * 1024;
export async function loadClimateSnapshot(descriptor, { signal, fetchImpl = globalThis.fetch, cryptoImpl = globalThis.crypto, timeoutMs = 12000 } = {}) {
  if (!descriptor || !/^\/science-data\/daily-climate\/usw\d{8}-[a-f0-9]{16}\.json$/.test(descriptor.url) ||
      !/^[a-f0-9]{64}$/.test(descriptor.sha256) || !Number.isInteger(descriptor.bytes) || descriptor.bytes < 1 || descriptor.bytes > LIMIT ||
      descriptor.url !== `/science-data/daily-climate/${descriptor.id.toLowerCase()}-${descriptor.sha256.slice(0, 16)}.json`) throw new Error('Invalid climate snapshot manifest.');
  if (signal?.aborted) throw signal.reason ?? new DOMException('Aborted', 'AbortError');
  const controller = new AbortController();
  let reader;
  let abortReject;
  const aborted = new Promise((_, reject) => { abortReject = reject; });
  const onAbort = () => { const error = controller.signal.reason ?? new DOMException('Aborted', 'AbortError'); void reader?.cancel(error).catch(() => {}); abortReject(error); };
  controller.signal.addEventListener('abort', onAbort, { once: true });
  const cancel = () => controller.abort(signal.reason ?? new DOMException('Aborted', 'AbortError'));
  if (signal?.aborted) cancel(); else signal?.addEventListener('abort', cancel, { once: true });
  const timer = setTimeout(() => controller.abort(new Error('The snapshot read timed out. Retry the station.')), timeoutMs);
  try {
    return await Promise.race([aborted, (async () => {
      const response = await fetchImpl(descriptor.url, { signal: controller.signal, credentials: 'same-origin', redirect: 'error' });
      if (controller.signal.aborted) throw controller.signal.reason;
      if (!response.ok) throw new Error('The station snapshot could not be read. Retry the station.');
      const size = response.headers.get('content-length');
      if (size !== null && (!/^\d+$/.test(size) || Number(size) > LIMIT)) throw new Error('Oversized station snapshot.');
      if (!response.body) throw new Error('The station snapshot has no body.');
      reader = response.body.getReader();
      const chunks = [];
      let length = 0;
      while (true) {
        const { done, value } = await reader.read();
        if (controller.signal.aborted) throw controller.signal.reason;
        if (done) break;
        length += value.byteLength;
        if (length > LIMIT || length > descriptor.bytes) throw new Error('The station snapshot exceeded its recorded size.');
        chunks.push(value);
      }
      if (length !== descriptor.bytes) throw new Error('The station snapshot is incomplete.');
      const bytes = new Uint8Array(length);
      let offset = 0;
      for (const chunk of chunks) { bytes.set(chunk, offset); offset += chunk.length; }
      if (!cryptoImpl?.subtle) throw new Error('Source integrity verification requires a secure browser context.');
      const hash = Array.from(new Uint8Array(await cryptoImpl.subtle.digest('SHA-256', bytes)), byte => byte.toString(16).padStart(2, '0')).join('');
      if (hash !== descriptor.sha256) throw new Error('The station snapshot failed its integrity check.');
      if (controller.signal.aborted) throw controller.signal.reason;
      return validateSnapshot(JSON.parse(new TextDecoder('utf-8', { fatal: true }).decode(bytes)), descriptor);
    })()]);
  } finally {
    clearTimeout(timer);
    signal?.removeEventListener('abort', cancel);
    controller.signal.removeEventListener('abort', onAbort);
    if (reader) { void reader.cancel().catch(() => {}); }
  }
}
