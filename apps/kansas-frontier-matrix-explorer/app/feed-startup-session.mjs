import { resolveFeedStartup } from './feed-startup.ts';

const freeze = (value) => {
  if (value && typeof value === 'object' && !Object.isFrozen(value)) {
    for (const child of Object.values(value)) freeze(child);
    Object.freeze(value);
  }
  return value;
};
const copy = (value) => freeze(structuredClone(value));

/** App-local request coordinator, not a provider parser or publication authority.
 * The reader must supply already validated, rights-cleared Artifact metadata.
 * No network, persistent cache or polling is started by construction/import.
 * @param {import('./feed-startup.ts').StartupInput} initial
 * @param {{now?: () => string, onChange?: (snapshot: object) => void}} options
 */
export function createFeedStartupSession(initial, { now = () => new Date().toISOString(), onChange = () => {} } = {}) {
  let input = copy(initial), generation = 0, disposed = false, active = null, workState = 'idle';
  const snapshot = () => freeze({ generation, workState,
    decision: resolveFeedStartup({ ...input, now: now() }) });
  const emit = () => { if (!disposed) onChange(snapshot()); };
  const invalidate = () => {
    generation++;
    const previous = active;
    active = null;
    previous?.controller.abort();
  };
  const select = (patch) => {
    if (disposed) return false;
    invalidate();
    input = copy({ ...input, ...patch, phase: 'idle', live: undefined, history: undefined,
      failureCode: undefined, rendererState: 'unverified', renderedArtifactId: undefined, renderedScopeKey: undefined });
    workState = 'idle'; emit(); return true;
  };
  const cancel = () => {
    if (disposed) return;
    invalidate();
    input = copy({ ...input, phase: 'idle', live: undefined, history: undefined,
      failureCode: undefined, rendererState: 'unverified', renderedArtifactId: undefined, renderedScopeKey: undefined });
    workState = 'cancelled'; emit();
  };
  /** @param {(context: {signal: AbortSignal, generation: number, sourceId: string, scopeKey: string, direction: string}) => Promise<any>} reader */
  async function load(reader, { timeoutMs = 45_000 } = {}) {
    if (disposed) return { outcome: 'DISPOSED' };
    if (typeof reader !== 'function' || !Number.isInteger(timeoutMs) || timeoutMs < 10 || timeoutMs > 60_000) {
      throw new TypeError('Invalid reader or request deadline.');
    }
    invalidate();
    // Never invoke an adapter for an inaccessible, disabled or demonstration-only request.
    if (input.access !== 'allowed' || !input.enabled || !input.timeSupported || !input.zoomSupported
      || !['auto', 'live', 'history'].includes(input.direction)) {
      workState = 'idle'; emit(); return { outcome: 'NOT_REQUESTED' };
    }
    const ownGeneration = generation, controller = new AbortController();
    active = { controller, generation: ownGeneration };
    input = copy({ ...input, phase: 'loading', failureCode: undefined, live: undefined, history: undefined,
      rendererState: 'unverified', renderedArtifactId: undefined, renderedScopeKey: undefined });
    const request = Object.freeze({ signal: controller.signal, generation: ownGeneration,
      sourceId: input.sourceId, scopeKey: input.scopeKey, direction: input.direction });
    workState = 'loading'; emit();
    let timer, timeout = false, result;
    const interrupted = new Promise((resolve) => controller.signal.addEventListener('abort',
      () => resolve({ phase: 'error', failureCode: timeout ? 'TIMEOUT' : 'CANCELLED' }), { once: true }));
    timer = setTimeout(() => { timeout = true; controller.abort(); }, timeoutMs);
    try {
      result = await Promise.race([Promise.resolve().then(() => controller.signal.aborted
        ? { phase: 'error', failureCode: 'CANCELLED' } : reader(request)), interrupted]);
    } catch {
      result = { phase: 'error', failureCode: 'NETWORK_ERROR' };
    } finally { clearTimeout(timer); }
    if (disposed || ownGeneration !== generation) return { outcome: 'SUPERSEDED' };
    active = null;
    controller.abort();
    const phase = ['ready', 'empty', 'partial', 'error'].includes(result?.phase) ? result.phase : 'error';
    try {
      input = copy({ ...input, phase, failureCode: result?.failureCode ?? 'INVALID_RESPONSE',
        live: input.direction !== 'history' ? result?.artifact : undefined,
        history: input.direction === 'history' ? result?.artifact : undefined });
    } catch {
      input = copy({ ...input, phase: 'error', failureCode: 'INVALID_RESPONSE', live: undefined, history: undefined });
    }
    workState = 'settled'; emit();
    return { outcome: 'SETTLED', snapshot: snapshot() };
  }
  return Object.freeze({ snapshot, select, cancel, load,
    dispose() { if (!disposed) {
      invalidate(); disposed = true; workState = 'disposed';
      input = copy({ ...input, enabled: false, phase: 'idle', live: undefined, history: undefined,
        snapshots: [], demo: undefined, rendererState: 'unverified', renderedArtifactId: undefined, renderedScopeKey: undefined });
    } } });
}
