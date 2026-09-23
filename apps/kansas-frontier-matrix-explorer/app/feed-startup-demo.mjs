// Binds only the shipped synthetic fixture. A matching hash is not source admission.
export const STARTUP_DEMO_SHA256 = '98dabad1b43de7218aebbb0ee279073f5b06aabf32a65e6c67bfbe3aff06ecde';
const freeze = (value) => {
  if (value && typeof value === 'object') { Object.values(value).forEach(freeze); Object.freeze(value); }
  return value;
};
/** Verify exact bundled UTF-8 bytes before accepting this invented demonstration.
 * No URL/file input, user-location lookup, measurement or observation generation.
 * @param {string} text
 */
export async function readBundledStartupDemo(text) {
  if (typeof text !== 'string' || text.length > 16_384) throw new Error('DEMO_INVALID');
  const bytes = new TextEncoder().encode(text);
  const digest = Array.from(new Uint8Array(await crypto.subtle.digest('SHA-256', bytes)),
    (b) => b.toString(16).padStart(2, '0')).join('');
  if (digest !== STARTUP_DEMO_SHA256) throw new Error('DEMO_INTEGRITY');
  const data = JSON.parse(text), p = data.properties;
  if (data.type !== 'FeatureCollection' || data.features.length !== 2 || p.synthetic !== true
    || p.sourceId !== 'synthetic:starter' || p.retrievedAt !== null
    || data.features.some((f) => f.properties.synthetic !== true)) throw new Error('DEMO_INVALID');
  return freeze({ data, artifact: { id: p.artifactId, sourceId: p.sourceId, scopeKey: p.scopeKey,
    kind: 'synthetic', dataRole: 'synthetic', sha256: digest, validation: 'passed', displayAllowed: true,
    dataTime: p.dataTime, retrievedAt: null, freshnessAnchor: null, validUntil: null, featureCount: data.features.length } });
}
