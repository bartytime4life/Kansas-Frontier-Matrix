import { validBorehole, intervalIssues, type Borehole } from '../subsurface-model';
import { materialFor, materialInfo } from '../subsurface-materials';

/** Existing published tile, pinned in public/data/subsurface/manifest.json.
 * Welcome reads one fixed record; this is not a probe, admission or new carrier. */
export const WELCOME_GEOLOGY_SOURCE = Object.freeze({
 url: '/data/subsurface/tile-164-257311.json.gz',
 sha256: '1d120cea755356d06bc6995d78a4fea7aff9f177847bce2715eb98f32c8d18e8',
 decodedSha256: 'ea306c13f6df8e64fe706d578873b3585b65e1c72b06b4aa50f8add0493dd502',
 maxBytes: 5681, maxDecodedBytes: 60440,
 recordId: 'wwc5-1054515520', recordDate: '2024-04-09',
 sourceUrl: 'https://chasm.kgs.ku.edu/ords/wwc5.wwc5d2.well_details?well_id=1054515520',
});
const cancelled = () => new DOMException('Source request cancelled', 'AbortError');
async function bytesFrom(stream: ReadableStream<Uint8Array> | null, limit: number, signal: AbortSignal): Promise<Uint8Array<ArrayBuffer>> {
 if (signal.aborted) throw cancelled();
 if (!stream) throw new Error('Source body unavailable');
 const reader = stream.getReader(), chunks: Uint8Array[] = []; let size = 0;
 const abort = () => { void reader.cancel().catch(() => {}); };
 signal.addEventListener('abort', abort, { once: true });
 try {
  while (true) {
   const { done, value } = await reader.read();
   if (signal.aborted) throw cancelled();
   if (done) break;
   size += value.byteLength;
   if (size > limit) { await reader.cancel(); throw new Error('Source exceeds welcome display limit'); }
   chunks.push(value);
  }
 } finally { signal.removeEventListener('abort', abort); reader.releaseLock(); }
 const bytes = new Uint8Array(size); let offset = 0;
 for (const chunk of chunks) { bytes.set(chunk, offset); offset += chunk.byteLength; }
 return bytes;
}
const digest = async (bytes: Uint8Array<ArrayBuffer>) => Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256', bytes)), n => n.toString(16).padStart(2, '0')).join('');
export function geologyRecord(raw: unknown): Borehole {
 if (!Array.isArray(raw) || raw.length !== 85 || !raw.every(validBorehole)) throw new Error('Source schema unavailable');
 const matches = raw.filter(row => row.id === WELCOME_GEOLOGY_SOURCE.recordId);
 if (matches.length !== 1) throw new Error('Recorded well unavailable');
 const record = matches[0];
 if (record.sourceId !== 'kgs-wwc5' || record.kind !== 'well' || record.sourceTime !== WELCOME_GEOLOGY_SOURCE.recordDate || record.sourceUrl !== WELCOME_GEOLOGY_SOURCE.sourceUrl || record.depthUnit !== 'ft' || record.depthReference !== 'land-surface' || record.totalDepth !== 60 || record.intervals.length !== 8) throw new Error('Recorded well contract differs');
 const issues = intervalIssues(record.intervals);
 if (issues.gaps.length || issues.overlaps.length || record.intervals[0].top !== 0 || record.intervals.at(-1)?.bottom !== 60 || record.intervals.some((row, i) => i > 0 && row.top !== record.intervals[i - 1].bottom)) throw new Error('Recorded depth order differs');
 return record;
}
export async function readWelcomeGeology(signal: AbortSignal): Promise<Borehole> {
 const pin = WELCOME_GEOLOGY_SOURCE;
 const response = await fetch(pin.url + '?sha256=' + pin.sha256, { signal, cache: 'force-cache', redirect: 'error' });
 if (!response.ok || response.redirected) { await response.body?.cancel().catch(() => {}); throw new Error('Recorded well source unavailable'); }
 const length = Number(response.headers.get('content-length'));
 if (length > pin.maxDecodedBytes) { await response.body?.cancel().catch(() => {}); throw new Error('Source exceeds welcome display limit'); }
 const bytes = await bytesFrom(response.body, pin.maxDecodedBytes, signal);
 const gzip = bytes[0] === 0x1f && bytes[1] === 0x8b;
 if (gzip && bytes.byteLength > pin.maxBytes) throw new Error('Compressed source exceeds welcome display limit');
 const hash = await digest(bytes);
 // Like subsurface-worker, accept transparent HTTP decompression only when its
 // separately pinned exact decoded bytes match. Parseable JSON never suffices.
 if (hash !== (gzip ? pin.sha256 : pin.decodedSha256)) throw new Error('Source integrity mismatch');
 const decoded = gzip ? await bytesFrom(new Blob([bytes]).stream().pipeThrough(new DecompressionStream('gzip')), pin.maxDecodedBytes, signal) : bytes;
 if (await digest(decoded) !== pin.decodedSha256) throw new Error('Decoded source integrity mismatch');
 if (signal.aborted) throw cancelled();
 return geologyRecord(JSON.parse(new TextDecoder('utf-8', { fatal: true }).decode(decoded)));
}
/** Exact per-record depth geometry. Width and display palette are illustrative. */
export function geologyIntervals(record: Borehole) {
 return record.intervals.map((interval, index) => ({ ...interval, index,
  y: interval.top / 60 * 204, height: (interval.bottom - interval.top) / 60 * 204,
  material: materialInfo(materialFor(interval, record.kind)),
 }));
}
