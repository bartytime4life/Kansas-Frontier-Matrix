// Fixed same-origin, content-hashed provider-context assets only. No live API.
export async function loadVerifiedSnapshot(descriptor, validate, { prefix, limit, signal, fetchImpl = globalThis.fetch,
  cryptoImpl = globalThis.crypto, timeoutMs = 12000 } = {}) {
  if (!descriptor || !/^[a-z0-9-]+$/.test(descriptor.id) || !/^[a-f0-9]{64}$/.test(descriptor.sha256) ||
      !Number.isInteger(descriptor.bytes) || descriptor.bytes < 1 || descriptor.bytes > limit ||
      descriptor.url !== `/science-data/${prefix}/${descriptor.id}-${descriptor.sha256.slice(0, 16)}.json`) {
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
      const response = await fetchImpl(descriptor.url, { signal: controller.signal, credentials: 'same-origin', redirect: 'error' });
      if (controller.signal.aborted) throw controller.signal.reason;
      if (!response.ok) throw new Error('The science snapshot could not be read. Please retry.');
      const declared = response.headers.get('content-length');
      if (declared !== null && (!/^\d+$/.test(declared) || Number(declared) > limit || Number(declared) !== descriptor.bytes)) {
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
        if (length > limit || length > descriptor.bytes) throw new Error('The science snapshot exceeded its recorded size.');
        chunks.push(value);
      }
      if (length !== descriptor.bytes) throw new Error('The science snapshot is incomplete.');
      const bytes = new Uint8Array(length);
      let offset = 0;
      for (const chunk of chunks) { bytes.set(chunk, offset); offset += chunk.byteLength; }
      if (!cryptoImpl?.subtle) throw new Error('Source integrity verification requires a secure browser context.');
      const digest = new Uint8Array(await cryptoImpl.subtle.digest('SHA-256', bytes));
      const hash = Array.from(digest, byte => byte.toString(16).padStart(2, '0')).join('');
      if (hash !== descriptor.sha256) throw new Error('The science snapshot failed its integrity check.');
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
