/** Public projections contain no job rows, private paths, provider payloads or error messages. */
const time = value => typeof value === 'string' && /^\d{4}-\d\d-\d\dT/.test(value) && Number.isFinite(Date.parse(value)) ? new Date(value).toISOString() : null;
const allowed = new Set(['available', 'partial', 'empty', 'stale', 'held', 'unavailable', 'not-checked', 'candidate']);
export function publicSourceHealth(sourceId, product) {
  const empty = { sourceId, state: 'held', retrievedAt: null, observedFrom: null, observedThrough: null, releaseId: null, approvalExpiresAt: null };
  if (!product || !['available', 'partial', 'empty'].includes(product.state) || !/^[a-f0-9]{64}$/.test(product.releaseId ?? '')) return empty;
  const times = (product.data?.features ?? []).flatMap(feature => [feature.properties?.observedAt, feature.properties?.sent].map(time).filter(Boolean)).sort();
  return { ...empty, state: product.freshness === 'stale' ? 'stale' : product.state,
    retrievedAt: time(product.retrievedAt), observedFrom: times[0] ?? null, observedThrough: times.at(-1) ?? null,
    releaseId: product.releaseId, approvalExpiresAt: time(product.approvalExpiresAt) };
}
export function cardHealth(card, health) {
  if (card.demo) return 'demo';
  const states = card.required.map(id => health.get(id)?.state ?? 'not-checked');
  const usable = states.filter(state => ['available', 'empty', 'partial', 'stale'].includes(state));
  if (states.includes('partial') || usable.length && usable.length < states.length) return 'partial';
  if (states.includes('unavailable')) return 'unavailable';
  if (states.includes('held')) return 'held';
  if (states.includes('not-checked')) return 'not-checked';
  if (states.includes('stale')) return 'stale';
  if (states.length) return states.every(state => state === 'empty') ? 'empty' : 'available';
  // Optional context never turns an unqualified topic into a complete pipeline.
  return card.gaps.length ? 'coverage-gap' : 'not-checked';
}
export function cardSnapshot(cards, pipelines, sourceHealth = [], { now = Date.now(), state = 'setup-pending' } = {}) {
  const known = new Set(pipelines.map(pipeline => pipeline.id));
  const health = new Map(sourceHealth.filter(item => known.has(item.sourceId) && allowed.has(item.state)).map(item => [item.sourceId, {
    sourceId: item.sourceId, state: item.state, retrievedAt: time(item.retrievedAt), observedFrom: time(item.observedFrom),
    observedThrough: time(item.observedThrough), approvalExpiresAt: time(item.approvalExpiresAt),
    releaseId: /^[a-f0-9]{64}$/.test(item.releaseId ?? '') ? item.releaseId : null,
  }]));
  const sources = pipelines.map(pipeline => ({ ...pipeline, health: health.get(pipeline.id) ?? {
    sourceId: pipeline.id, state: pipeline.mode === 'candidate' ? 'candidate' : 'not-checked',
    retrievedAt: null, observedFrom: null, observedThrough: null, releaseId: null, approvalExpiresAt: null,
  } }));
  return { format: 'kfm-card-pipelines-v1', checkedAt: new Date(now).toISOString(), state,
    authority: 'COVERAGE_METADATA_ONLY', sources,
    cards: cards.map(card => ({ ...card, state: cardHealth(card, health),
      coverage: card.demo ? 'demo' : card.required.length ? 'context-recipe' : card.optional.length ? 'optional-context' : 'unbundled',
      expansion: card.gaps.length ? 'review-required' : 'none' })),
  };
}
