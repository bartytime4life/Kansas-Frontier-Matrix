import { PUBLIC_LAB_SNAPSHOTS } from './public-snapshots.mjs';
import { boundedStoryText, validStoryBundle } from '../living-welcome/stories/story-bundle.mjs';

/** A closed list of versioned public files; never falls through to private PC data. */
export async function loadPublicLabSnapshot(id, { signal, fetcher = fetch, digest = globalThis.crypto.subtle } = {}) {
  const snapshot = Object.hasOwn(PUBLIC_LAB_SNAPSHOTS, id) ? PUBLIC_LAB_SNAPSHOTS[id] : null;
  if (!snapshot) return { state: 'waiting', bundle: null };
  const response = await fetcher(snapshot.path, { signal, headers: { Accept: 'application/json' } });
  if (!response.ok) return { state: 'offline', bundle: null };
  const text = await boundedStoryText(response);
  const bytes = new TextEncoder().encode(text);
  if (bytes.byteLength !== snapshot.bytes) throw new Error('Lab snapshot size mismatch');
  const hash = Array.from(new Uint8Array(await digest.digest('SHA-256', bytes)), byte => byte.toString(16).padStart(2, '0')).join('');
  if (hash !== snapshot.sha256) throw new Error('Lab snapshot integrity mismatch');
  const bundle = JSON.parse(text);
  if (!validStoryBundle(bundle, id)) throw new Error('Lab snapshot contract mismatch');
  return { state: 'ready', bundle };
}
