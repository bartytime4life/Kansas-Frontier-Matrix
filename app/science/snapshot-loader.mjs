// Register new content-addressed files alongside their manifests. The request
// uses a literal from this list, while the descriptor supplies verification data.
const publicSnapshots = [
  '/science-data/county-drought/kansas-4ca3a97c9d597afe.json',
  '/science-data/daily-air-quality/kansas-b571e1266c363d9d.json',
  '/science-data/daily-climate/usw00003928-b945aa52a206ad3f.json',
  '/science-data/daily-climate/usw00013985-d69ba63bc5223929.json',
  '/science-data/daily-climate/usw00013996-46bce3b93367f4a5.json',
  '/science-data/soil-profile/03067-38078772371cbf34.json',
  '/science-data/soil-profile/53974-d7476f6fba73aa93.json',
  '/science-data/sunlight/dodge-city-34cb2b0a4c18b671.json',
  '/science-data/sunlight/topeka-e813440e4ae96182.json',
  '/science-data/sunlight/wichita-46c54872d6dd5c10.json',
];

export async function loadVerifiedSnapshot(descriptor, validate, { prefix, limit, signal, fetchImpl = globalThis.fetch,
  cryptoImpl = globalThis.crypto, timeoutMs = 12000 } = {}) {
  const { url: recordedUrl, sha256, bytes: expectedBytes } = descriptor ?? {};
  const url = publicSnapshots.find(path => path === recordedUrl);
  const id = prefix === 'daily-climate' && typeof descriptor?.id === 'string' ? descriptor.id.toLowerCase() : descriptor?.id;
  if (!url || typeof id !== 'string' || !/^[a-z0-9-]+$/.test(id) ||
      typeof sha256 !== 'string' || sha256.length !== 64 || !/^[a-f0-9]+$/.test(sha256) ||
      !Number.isInteger(expectedBytes) || expectedBytes < 1 || expectedBytes > limit ||
      url !== `/science-data/${prefix}/${id}-${sha256.slice(0, 16)}.json`) {
    throw new Error('Invalid science snapshot manifest.');
  }
  if (signal?.aborted) throw signal.reason ?? new DOMException('Aborted', 'AbortError');
  const controller = new AbortController();
  let reader;
  let abortReject;
  const aborted = new Promise((_, reject) => { abortReject = reject; });
  const onAbort = () => {
    const error = controller.signal.reason ?? new DOMException('Aborted', 'AbortError');
    void reader?.cancel(error).catch(() => {});
    abortReject(error);
  };
  controller.signal.addEventListener('abort', onAbort, { once: true });
  const cancel = () => controller.abort(signal.reason ?? new DOMException('Aborted', 'AbortError'));
  signal?.addEventListener('abort', cancel, { once: true });
  const timer = setTimeout(() => controller.abort(new Error('The science snapshot read timed out. Please retry.')), timeoutMs);
  try {
    return await Promise.race([aborted, (async () => {
      const response = await fetchImpl(url, { method: 'GET', mode: 'same-origin', signal: controller.signal,
        credentials: 'same-origin', redirect: 'error' });
      if (controller.signal.aborted) throw controller.signal.reason;
      if (!response.ok) throw new Error('The science snapshot could not be read. Please retry.');
      const declared = response.headers.get('content-length');
      const encoding = response.headers.get('content-encoding')?.trim().toLowerCase();
      // Fetch exposes decoded bytes; Content-Length describes the transferred
      // representation when a host applies gzip or Brotli compression.
      const identity = !encoding || encoding === 'identity';
      if (declared !== null && (!/^\d+$/.test(declared) || Number(declared) > limit || (identity && Number(declared) !== expectedBytes))) {
        throw new Error('The science snapshot size did not match its manifest.');
      }
      if (!response.body) throw new Error('The science snapshot has no body.');
      reader = response.body.getReader();
      const chunks = [];
      let length = 0;
      while (true) {
        const { done, value } = await reader.read();
        if (controller.signal.aborted) throw controller.signal.reason;
        if (done) break;
        length += value.byteLength;
        if (length > limit || length > expectedBytes) throw new Error('The science snapshot exceeded its recorded size.');
        chunks.push(value);
      }
      if (length !== expectedBytes) throw new Error('The science snapshot is incomplete.');
      const bytes = new Uint8Array(length);
      let offset = 0;
      for (const chunk of chunks) { bytes.set(chunk, offset); offset += chunk.byteLength; }
      if (!cryptoImpl?.subtle) throw new Error('Source integrity verification requires a secure browser context.');
      const digest = new Uint8Array(await cryptoImpl.subtle.digest('SHA-256', bytes));
      const hash = Array.from(digest, byte => byte.toString(16).padStart(2, '0')).join('');
      if (hash !== sha256) throw new Error('The science snapshot failed its integrity check.');
      if (controller.signal.aborted) throw controller.signal.reason;
      return validate(JSON.parse(new TextDecoder('utf-8', { fatal: true }).decode(bytes)));
    })()]);
  } finally {
    clearTimeout(timer);
    signal?.removeEventListener('abort', cancel);
    controller.signal.removeEventListener('abort', onAbort);
    if (reader) void reader.cancel().catch(() => {});
  }
}
