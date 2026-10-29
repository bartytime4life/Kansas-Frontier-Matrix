import { captureRequest } from './ingestion-sources.mjs';
import { canonical, sha, parse, fail, timestamp } from './pipeline-contract.mjs';

const text = (value, max = 512) => typeof value === 'string' && value.length <= max && !/[\u0000-\u0008\u000b\u000c\u000e-\u001f]/.test(value) ? value : null;
export function providerTime(value) {
  const m = typeof value === 'string' && /^(\d{4})-(\d\d)-(\d\d)T(\d\d):(\d\d):(\d\d)(?:\.\d{1,9})?(Z|[+-]\d\d:\d\d)$/.exec(value);
  if (!m || Number(m[1]) < 1 || Number(m[2]) < 1 || Number(m[2]) > 12 || Number(m[3]) < 1 || Number(m[3]) > new Date(Date.UTC(Number(m[1]), Number(m[2]), 0)).getUTCDate()
    || Number(m[4]) > 23 || Number(m[5]) > 59 || Number(m[6]) > 59 || (m[7] !== 'Z' && (Number(m[7].slice(1, 3)) > 14 || Number(m[7].slice(4)) > 59)) || !Number.isFinite(Date.parse(value))) fail('SOURCE_TIME_INVALID');
  return new Date(value).toISOString();
}
function geometry(value) {
  if (value === null) return null;
  if (!value || !['Point', 'Polygon', 'MultiPolygon'].includes(value.type)) fail('GEOMETRY_INVALID');
  let points = 0;
  function walk(v, depth) {
    if (!Array.isArray(v) || depth > 4) fail('GEOMETRY_INVALID');
    if (typeof v[0] === 'number') {
      if (v.length !== 2 || !v.every(Number.isFinite) || Math.abs(v[0]) > 180 || Math.abs(v[1]) > 90 || ++points > 50000) fail('GEOMETRY_INVALID');
    } else { if (!v.length) fail('GEOMETRY_INVALID'); for (const child of v) walk(child, depth + 1); }
  }
  walk(value.coordinates, 0);
  const point = p => Array.isArray(p) && p.length === 2 && p.every(Number.isFinite);
  const ring = r => Array.isArray(r) && r.length >= 4 && r.every(point) && r[0][0] === r.at(-1)[0] && r[0][1] === r.at(-1)[1];
  const polygon = p => Array.isArray(p) && p.length > 0 && p.every(ring);
  if (value.type === 'Point' ? !point(value.coordinates) : value.type === 'Polygon' ? !polygon(value.coordinates) : !value.coordinates.every(polygon)) fail('GEOMETRY_INVALID');
  return { type: value.type, coordinates: value.coordinates };
}
// The capture window both point sources are requested with (ingestion-sources.mjs).
const outsideWindow = shape => shape.type !== 'Point' || shape.coordinates[0] < -102.1 || shape.coordinates[0] > -94.5 || shape.coordinates[1] < 36.9 || shape.coordinates[1] > 40.1;
function sourceGeometry(sourceId, value) {
  const shape = geometry(value);
  if (sourceId === 'usgs-streamflow' && shape !== null && outsideWindow(shape)) fail('GEOGRAPHIC_SCOPE_INVALID');
  if (sourceId === 'usgs-earthquakes' && (shape === null || outsideWindow(shape))) fail('GEOGRAPHIC_SCOPE_INVALID');
  return shape;
}
const EARTHQUAKE_ID = /^[a-z0-9]{2,40}$/;
const EARTHQUAKE_PAGE = 'https://earthquake.usgs.gov/earthquakes/eventpage/';
const EARTHQUAKE_WINDOW_MS = 30 * 86400000;
/** A finite number inside [min, max], or null for a source null; anything else is a schema change. */
function bounded(value, min, max) {
  if (value === null || value === undefined) return null;
  if (typeof value !== 'number' || !Number.isFinite(value) || value < min || value > max) fail('EARTHQUAKE_SCHEMA_CHANGED');
  return value;
}
const epoch = value => { if (typeof value !== 'number' || !Number.isInteger(value) || !Number.isFinite(new Date(value).getTime())) fail('SOURCE_TIME_INVALID'); return new Date(value).toISOString(); };
function amount(value) {
  if (value === null) return null;
  if (!((typeof value === 'number' || typeof value === 'string' && value.length <= 64 && /^[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?$/.test(value)) && Number.isFinite(Number(value)) && Math.abs(Number(value)) <= 1e9)) fail('STREAMFLOW_VALUE_INVALID');
  return Number(value);
}
// Public context is deliberately allowlisted; raw provider properties remain private.
export function normalizeCapture(request, capture) {
  const r = capture.receipt; const value = parse(capture.bytes);
  const fixed = captureRequest(request.sourceId, request.slot);
  if (!['usgs-streamflow', 'nws-alerts', 'usgs-earthquakes'].includes(request.sourceId) || fixed.id !== request.id || r.captureId !== request.id || r.sourceId !== request.sourceId
    || r.sha256 !== sha(capture.bytes) || r.byteLength !== capture.bytes.length || r.sourceUrl !== fixed.url
    || r.validation !== 'structure-valid' || value.type !== 'FeatureCollection' || !Array.isArray(value.features) || value.features.length > 1000) fail('CAPTURE_INVALID');
  timestamp(r.retrievedAt);
  const ids = new Set();
  const features = value.features.flatMap(feature => {
    const p = feature.properties;
    const id = text(String(feature.id ?? p.id ?? ''), 512);
    if (!id || ids.has(id)) fail('FEATURE_ID_INVALID'); ids.add(id);
    let properties, shape = feature.geometry;
    if (request.sourceId === 'usgs-earthquakes') {
      if (p.type !== 'earthquake' || !['automatic', 'reviewed', 'deleted'].includes(p.status) || !EARTHQUAKE_ID.test(id)) fail('EARTHQUAKE_SCHEMA_CHANGED');
      // USGS marks a retracted event deleted; it is not an earthquake to show.
      if (p.status === 'deleted') return [];
      const c = feature.geometry?.coordinates;
      if (feature.geometry?.type !== 'Point' || !Array.isArray(c) || c.length !== 3) fail('GEOMETRY_INVALID');
      const observedAt = epoch(p.time);
      if (timestamp(observedAt) > request.slot || timestamp(observedAt) < request.slot - EARTHQUAKE_WINDOW_MS) fail('OBSERVATION_OUTSIDE_WINDOW');
      // Depth leaves the coordinates (published points are two-dimensional) and keeps its kilometres.
      shape = { type: 'Point', coordinates: [c[0], c[1]] };
      properties = { magnitude: bounded(p.mag, -2, 10), magnitudeType: p.magType === null || p.magType === undefined ? null : text(p.magType, 16),
        place: p.place === null || p.place === undefined ? null : text(p.place, 256), depthKm: bounded(c[2], -10, 800), observedAt,
        updatedAt: p.updated === null || p.updated === undefined ? null : epoch(p.updated), status: p.status,
        // Built from the checked id, never taken from the provider's url field.
        eventUrl: EARTHQUAKE_PAGE + id, sourceFeatureId: id };
      if ((p.magType != null && properties.magnitudeType === null) || (p.place != null && properties.place === null)) fail('EARTHQUAKE_SCHEMA_CHANGED');
    } else if (request.sourceId === 'nws-alerts') {
      const times = Object.fromEntries(['sent', 'effective', 'expires', 'onset', 'ends'].map(k => [k, p[k] === null || p[k] === undefined ? null : providerTime(p[k])]));
      for (const field of ['sent', 'effective', 'expires']) timestamp(times[field]);
      if (timestamp(times.expires) < timestamp(times.effective) || timestamp(times.sent) > timestamp(r.retrievedAt) + 60000) fail('ALERT_TIME_INVALID');
      properties = Object.fromEntries(['event', 'headline', 'severity', 'certainty', 'urgency', 'areaDesc', 'status', 'messageType', 'sent', 'effective', 'onset', 'ends', 'expires', 'description', 'instruction'].map(key => [key, text(p[key], ['description', 'instruction'].includes(key) ? 12000 : 1000)]));
      Object.assign(properties, times); properties.observedAt = times.sent;
    } else {
      if (String(p.parameter_code) !== '00060' || typeof p.monitoring_location_id !== 'string' || !p.monitoring_location_id.startsWith('USGS-')) fail('STREAMFLOW_SCHEMA_CHANGED');
      const observedAt = providerTime(p.time);
      if (timestamp(observedAt) > request.slot || timestamp(observedAt) < request.slot - 86400000) fail('OBSERVATION_OUTSIDE_WINDOW');
      // Preserve source units and missingness. Do not guess missing unit metadata.
      const value = amount(p.value);
      if (!text(p.unit_of_measure, 32) || !['Provisional','Approved','P','A'].includes(p.approval_status)) fail('STREAMFLOW_SCHEMA_CHANGED');
      properties = { stationId: text(p.monitoring_location_id), parameterCode: '00060', value, originalValue: p.value,
        unit: text(p.unit_of_measure), observedAt, originalTime: p.time, sourceFeatureId: id,
        qualifiers: p.qualifier === null || p.qualifier === undefined ? [] : [text(p.qualifier, 128)],
        provisional: ['Provisional','P'].includes(p.approval_status) };
    }
    return [{ type: 'Feature', id, geometry: sourceGeometry(request.sourceId, shape), properties }];
  });
  features.sort((a, b) => a.id < b.id ? -1 : a.id > b.id ? 1 : 0);
  const product = { format: 'kfm-curated-context-v1', sourceId: request.sourceId, captureId: request.id, captureSha256: r.sha256,
    sourceUrl: fixed.url, retrievedAt: r.retrievedAt, bucketAt: new Date(request.slot).toISOString(),
    partial: r.partial === true, evidenceRole: 'EXTERNAL_CONTEXT_ONLY', evidenceEligible: false,
    rightsUrl: fixed.rightsUrl, limitation: fixed.limitation, data: { type: 'FeatureCollection', features } };
  return { product, bytes: Buffer.from(canonical(product)) };
}
export function validateContext(product) {
  const keys = ['format','sourceId','captureId','captureSha256','sourceUrl','retrievedAt','bucketAt','partial','evidenceRole','evidenceEligible','rightsUrl','limitation','data'];
  if (product?.format !== 'kfm-curated-context-v1' || Object.keys(product).sort().join(',') !== keys.sort().join(',') || product.evidenceRole !== 'EXTERNAL_CONTEXT_ONLY' || product.evidenceEligible !== false) fail('CONTEXT_INVALID');
  const req = captureRequest(product.sourceId, timestamp(product.bucketAt));
  if (!['usgs-streamflow', 'nws-alerts', 'usgs-earthquakes'].includes(product.sourceId) || product.captureId !== req.id || product.sourceUrl !== req.url || product.rightsUrl !== req.rightsUrl || product.limitation !== req.limitation
    || !/^[a-f0-9]{64}$/.test(product.captureSha256) || typeof product.partial !== 'boolean' || product.data?.type !== 'FeatureCollection' || !Array.isArray(product.data.features) || product.data.features.length > 1000) fail('CONTEXT_INVALID');
  timestamp(product.retrievedAt);
  const ids = new Set();
  for (const f of product.data.features) {
    if (f?.type !== 'Feature' || Object.keys(f).sort().join(',') !== 'geometry,id,properties,type' || !text(f.id) || ids.has(f.id) || !f.properties || typeof f.properties !== 'object') fail('CONTEXT_INVALID');
    ids.add(f.id); sourceGeometry(product.sourceId, f.geometry); const p = f.properties;
    if (product.sourceId === 'usgs-earthquakes') {
      const allowed = ['magnitude','magnitudeType','place','depthKm','observedAt','updatedAt','status','eventUrl','sourceFeatureId'];
      if (Object.keys(p).sort().join(',') !== allowed.sort().join(',') || p.sourceFeatureId !== f.id || !EARTHQUAKE_ID.test(f.id) || p.eventUrl !== EARTHQUAKE_PAGE + f.id
        || !['automatic', 'reviewed'].includes(p.status) || (p.magnitudeType !== null && text(p.magnitudeType, 16) === null) || (p.place !== null && text(p.place, 256) === null)) fail('CONTEXT_INVALID');
      try { bounded(p.magnitude, -2, 10); bounded(p.depthKm, -10, 800); } catch { fail('CONTEXT_INVALID'); }
      if (timestamp(p.observedAt) > req.slot || timestamp(p.observedAt) < req.slot - EARTHQUAKE_WINDOW_MS) fail('CONTEXT_INVALID');
      if (p.updatedAt !== null) timestamp(p.updatedAt);
    } else if (product.sourceId === 'nws-alerts') {
      const allowed = ['event','headline','severity','certainty','urgency','areaDesc','status','messageType','sent','effective','onset','ends','expires','description','instruction','observedAt'];
      if (Object.keys(p).sort().join(',') !== allowed.sort().join(',') || allowed.some(k => p[k] !== null && text(p[k], ['description','instruction'].includes(k) ? 12000 : 1000) === null)
        || p.observedAt !== p.sent || timestamp(p.expires) < timestamp(p.effective)) fail('CONTEXT_INVALID');
      for (const k of ['sent','effective','expires','observedAt']) timestamp(p[k]);
      for (const k of ['onset','ends']) if (p[k] !== null) timestamp(p[k]);
    } else {
      const allowed = ['stationId','parameterCode','value','originalValue','unit','observedAt','originalTime','sourceFeatureId','qualifiers','provisional'];
      if (Object.keys(p).sort().join(',') !== allowed.sort().join(',') || !text(p.stationId)?.startsWith('USGS-') || p.parameterCode !== '00060' || !text(p.unit, 32)
        || !text(p.sourceFeatureId) || providerTime(p.originalTime) !== p.observedAt || typeof p.provisional !== 'boolean' || !Array.isArray(p.qualifiers) || p.qualifiers.length > 1 || p.qualifiers.some(q => text(q, 128) === null)
        || p.value !== amount(p.originalValue)) fail('CONTEXT_INVALID');
      if (timestamp(p.observedAt) < req.slot - 86400000 || timestamp(p.observedAt) > req.slot) fail('CONTEXT_INVALID');
    }
  }
  return product;
}
