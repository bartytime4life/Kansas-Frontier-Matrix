// Bounded UI input validation, not source admission or release approval.
export const STORY_BUNDLE_BYTES = 3_000_000;
const object = value => value !== null && typeof value === 'object' && !Array.isArray(value);
const text = value => typeof value === 'string' && value.length <= 4000;
const finite = value => typeof value === 'number' && Number.isFinite(value);
const numeric = value => value === null || finite(value);
const list = (value, max = 10000) => Array.isArray(value) && value.length > 0 && value.length <= max;
const years = value => list(value, 2000) && value.every((v, i) => finite(v) && (!i || v > value[i - 1]));
const https = value => { try { return new URL(value).protocol === 'https:'; } catch { return false; } };
const coordinate = value => Array.isArray(value) && value.length === 2 && value.every(finite) && Math.abs(value[0]) <= 180 && Math.abs(value[1]) <= 90;
function geometry(value) {
  if (!object(value)) return false;
  const points = (line, minimum) => Array.isArray(line) && line.length >= minimum && line.every(coordinate);
  const ring = line => points(line, 4) && line[0][0] === line.at(-1)[0] && line[0][1] === line.at(-1)[1];
  const polygon = rings => list(rings) && rings.every(ring);
  switch (value.type) {
    case 'Point': return coordinate(value.coordinates);
    case 'LineString': return points(value.coordinates, 2);
    case 'MultiLineString': return list(value.coordinates) && value.coordinates.every(line => points(line, 2));
    case 'Polygon': return polygon(value.coordinates);
    case 'MultiPolygon': return list(value.coordinates) && value.coordinates.every(polygon);
    default: return false;
  }
}

export function validStoryBundle(bundle, id) {
  if (!object(bundle) || bundle.format !== 'kfm-story-bundle-v1' || bundle.story !== id || bundle.version !== 1 ||
      !object(bundle.data) || !object(bundle.observed) || !list(bundle.sources, 30) ||
      !bundle.sources.every(source => object(source) && text(source.name) && https(source.url) && text(source.license) && text(source.citation))) return false;
  const d = bundle.data;
  if (!list(d.limits, 50) || !d.limits.every(text)) return false;
  if (d.kind === 'records' && !['climate-stripes', 'iron-horse'].includes(id)) {
    if (!list(d.columns, 60) || !Array.isArray(d.records) || d.records.length > 10000 || !text(d.coverage)) return false;
    const keys = new Set();
    for (const column of d.columns) {
      if (!object(column) || !/^[a-zA-Z][a-zA-Z0-9_]*$/.test(column.key) || keys.has(column.key) ||
          !text(column.label) || !['string', 'number', 'year'].includes(column.type)) return false;
      keys.add(column.key);
    }
    if ([d.yearField, d.valueField, d.categoryField].filter(Boolean).some(key => !keys.has(key))) return false;
    const ids = new Set();
    for (const row of d.records) {
      if (!object(row) || !['string', 'number'].includes(typeof row.id) || ids.has(String(row.id))) return false;
      ids.add(String(row.id));
      if (row.longitude != null && (!finite(row.longitude) || Math.abs(row.longitude) > 180)) return false;
      if (row.latitude != null && (!finite(row.latitude) || Math.abs(row.latitude) > 90)) return false;
      if (row.geometry != null && !geometry(row.geometry)) return false;
      for (const column of d.columns) {
        const value = row[column.key];
        if (value == null) continue;
        if (column.type === 'number' || column.type === 'year') { if (!finite(value)) return false; }
        else if (!text(value)) return false;
      }
    }
    return true;
  }
  if (id === 'climate-stripes') {
    if (!years(d.years) || !list(d.areas, 110) || !list(d.baselines, 10) || !object(d.values) || !object(d.normals) || !object(d.elements)) return false;
    if (!object(d.latest) || !d.years.includes(d.latest.year) || !Number.isInteger(d.latest.month) || d.latest.month < 1 || d.latest.month > 12 ||
        !d.areas.some(area => area.id === '20') || !d.baselines.includes('1901-2000') || new Set(d.areas.map(area => area.id)).size !== d.areas.length) return false;
    return ['tmpc', 'pcpn', 'pdsi'].every(element => object(d.elements[element]) && text(d.elements[element].label) && text(d.elements[element].unit) &&
      d.elements[element].annual === (element === 'pcpn' ? 'sum' : 'mean') && finite(d.elements[element].scale) && d.elements[element].scale > 0 &&
      object(d.values[element]) && d.areas.every(area => text(area.id) && text(area.name) && Array.isArray(d.values[element][area.id]) &&
        d.values[element][area.id].length === d.years.length * 12 && d.values[element][area.id].every(numeric))) &&
      d.baselines.every(baseline => text(baseline) && object(d.normals[baseline]) && ['tmpc', 'pcpn'].every(element =>
        object(d.normals[baseline][element]) && d.areas.every(area => Array.isArray(d.normals[baseline][element][area.id]) &&
          d.normals[baseline][element][area.id].length === 12 && d.normals[baseline][element][area.id].every(finite))));
  }
  if (id === 'iron-horse') {
    if (!years(d.years) || !list(d.states, 60) || !list(d.names, 10000) || !list(d.gauges, 100) || !d.gauges.every(finite) ||
        !object(d.grid) || !Array.isArray(d.grid.origin) || d.grid.origin.length !== 2 || !d.grid.origin.every(finite) ||
        !finite(d.grid.unit) || d.grid.unit <= 0 || !list(d.lines, 10000) || !list(d.milesByYear, 2000) || !object(d.counts)) return false;
    return d.lines.every(row => Array.isArray(row) && row.length === 6 && [d.years,d.states,d.names,d.gauges].every((items, i) => Number.isInteger(row[i]) && row[i] >= 0 && row[i] < items.length) &&
      finite(row[4]) && row[4] >= 0 && list(row[5], 40000) && row[5].length % 2 === 0 && row[5].every(finite));
  }
  return false;
}

/** Stop oversized transfers before JSON parsing, including chunked responses. */
export async function boundedStoryText(response) {
  if (Number(response.headers?.get('content-length')) > STORY_BUNDLE_BYTES) throw new Error('Story snapshot exceeds the preview limit');
  if (!response.body?.getReader) {
    const value = await response.text();
    if (new TextEncoder().encode(value).byteLength > STORY_BUNDLE_BYTES) throw new Error('Story snapshot exceeds the preview limit');
    return value;
  }
  const reader = response.body.getReader(), chunks = [];
  let size = 0;
  try {
    for (;;) {
      const { done, value } = await reader.read();
      if (done) break;
      size += value.byteLength;
      if (size > STORY_BUNDLE_BYTES) { await reader.cancel(); throw new Error('Story snapshot exceeds the preview limit'); }
      chunks.push(value);
    }
  } finally { reader.releaseLock(); }
  const bytes = new Uint8Array(size);
  let offset = 0;
  for (const chunk of chunks) { bytes.set(chunk, offset); offset += chunk.byteLength; }
  return new TextDecoder().decode(bytes);
}
