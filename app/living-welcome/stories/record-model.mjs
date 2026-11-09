// Pure, null-preserving research operations. Views and downloads share this path.
export const numeric = value => typeof value === 'number' && Number.isFinite(value) ? value : null;
const missing = value => value === null || value === undefined || value === '';
const cache = new WeakMap();

export function recordModel(bundle) {
  if (cache.has(bundle)) return cache.get(bundle);
  const data = bundle?.data || {}, records = Array.isArray(data.records) ? data.records : [];
  const columns = (data.columns || []).filter(column => typeof column.key === 'string');
  const yearField = data.yearField || 'year', categoryField = data.categoryField || 'category';
  const metrics = columns.filter(column => column.type === 'number' && !['latitude', 'longitude', yearField].includes(column.key));
  const valueField = metrics.some(column => column.key === data.valueField) ? data.valueField : metrics[0]?.key || null;
  const years = records.map(row => numeric(row[yearField])).filter(value => value !== null);
  const endYears = data.temporalMode === 'interval' ? records.map(row => numeric(row[data.endYearField || 'endYear'])).filter(value => value !== null) : [];
  const categories = [...new Set(records.map(row => row[categoryField]).filter(value => !missing(value)).map(String))].sort((a, b) => a.localeCompare(b));
  const model = { data, records, columns, metrics, yearField, categoryField, valueField, categories,
    first: years.length ? Math.min(...years) : null, last: years.length ? Math.max(...years, ...endYears) : null };
  cache.set(bundle, model);
  return model;
}

export function recordRange(bundle) {
  const model = recordModel(bundle);
  return model.first !== null && model.last > model.first
    ? { min: model.first, max: model.last, step: model.data.timeStep || 1,
      label: model.data.timeLabel || (model.data.temporalMode === 'snapshot' ? 'Observation year' : model.data.temporalMode === 'interval' ? 'Boundaries at year end' : 'Records through year'),
      format: value => timeText(model, value), rate: Math.max(.1, (model.last - model.first) / 35) } : null;
}

export function timeText(model, value) {
  if (numeric(value) === null) return 'Undated';
  return model.data.timeUnit === 'Ma' ? `${Number(Math.abs(value).toPrecision(5))} Ma` : String(value);
}

export function metricOf(model, controls = {}) {
  return model.metrics.find(column => column.key === controls.metric) || model.metrics.find(column => column.key === model.valueField) || null;
}

export function filterRecords(model, { controls = {}, time = null } = {}) {
  const query = String(controls.query || '').trim().toLocaleLowerCase();
  const numberControl = value => value === '' || value === null || value === undefined ? null : Number.isFinite(Number(value)) ? Number(value) : null;
  const from = numberControl(controls.from), to = numberControl(controls.to);
  const temporal = model.data.temporalMode, exact = temporal === 'snapshot' || temporal === 'interval';
  const ceiling = numeric(time) ?? (exact ? model.last : null), metric = metricOf(model, controls)?.key;
  const minValue = numberControl(controls.minValue), maxValue = numberControl(controls.maxValue);
  // The final playback frame includes undated rows; a constrained temporal selection cannot assign them a year.
  const datedOnly = from !== null || to !== null || (ceiling !== null && ceiling < model.last);
  const selected = model.records.filter(row => {
    const year = numeric(row[model.yearField]), value = numeric(row[metric]);
    if (controls.category && String(row[model.categoryField] ?? '') !== controls.category) return false;
    if (query && !model.columns.some(column => String(row[column.key] ?? '').toLocaleLowerCase().includes(query))) return false;
    if (datedOnly && year === null) return false;
    if (year !== null && ((from !== null && year < from) || (to !== null && year > to) || (ceiling !== null && year > ceiling))) return false;
    if (temporal === 'snapshot' && year !== ceiling) return false;
    if (temporal === 'interval' && ceiling !== null) {
      const at = `${Math.floor(ceiling)}-12-31`, start = row[model.data.dateField || 'startDate'], end = row[model.data.endDateField || 'endDate'];
      if (typeof start === 'string' && typeof end === 'string') { if (start.slice(0, 10) > at || end.slice(0, 10) < at) return false; }
      else { const endYear = numeric(row[model.data.endYearField || 'endYear']); if (year === null || endYear === null || year > ceiling || endYear < ceiling) return false; }
    }
    if ((minValue !== null || maxValue !== null) && value === null) return false;
    if (value !== null && ((minValue !== null && value < minValue) || (maxValue !== null && value > maxValue))) return false;
    return true;
  });
  if (!controls.sort || !model.columns.some(column => column.key === controls.sort)) return selected;
  const key = controls.sort, direction = controls.direction === 'desc' ? -1 : 1;
  return selected.toSorted((a, b) => {
    if (missing(a[key]) && missing(b[key])) return 0;
    if (missing(a[key])) return 1;
    if (missing(b[key])) return -1;
    return (typeof a[key] === 'number' && typeof b[key] === 'number' ? a[key] - b[key] : String(a[key]).localeCompare(String(b[key]))) * direction;
  });
}

export function describe(records, key) {
  const values = records.map(row => numeric(row[key])).filter(value => value !== null).sort((a, b) => a - b), n = values.length;
  return { total: records.length, count: n, missing: records.length - n,
    min: n ? values[0] : null, max: n ? values[n - 1] : null,
    mean: n ? values.reduce((sum, value) => sum + value, 0) / n : null,
    median: n ? (values[Math.floor((n - 1) / 2)] + values[Math.floor(n / 2)]) / 2 : null };
}

export function distribution(records, key, count = 16) {
  const summary = describe(records, key);
  if (!summary.count) return [];
  if (summary.min === summary.max) return [{ from: summary.min, to: summary.max, count: summary.count }];
  const width = (summary.max - summary.min) / count;
  const bins = Array.from({ length: count }, (_, index) => ({ from: summary.min + index * width, to: index === count - 1 ? summary.max : summary.min + (index + 1) * width, count: 0 }));
  for (const row of records) { const value = numeric(row[key]); if (value !== null) bins[Math.min(count - 1, Math.floor((value - summary.min) / width))].count++; }
  return bins;
}

export function yearCounts(records, yearField) {
  const years = new Map();
  for (const row of records) { const year = numeric(row[yearField]); if (year !== null) years.set(year, (years.get(year) || 0) + 1); }
  return [...years].sort(([a], [b]) => a - b).map(([year, count]) => ({ year, count }));
}

export function monthlySeries(records, dateField, valueField, categoryField) {
  if (!dateField) return [];
  const groups = new Map();
  for (const row of records) {
    const date = typeof row[dateField] === 'string' ? row[dateField].slice(0, 7) : '';
    if (!/^\d{4}-\d{2}$/.test(date) || !Number.isFinite(Date.parse(`${date}-01`))) continue;
    const category = String(row[categoryField] ?? 'Unclassified'), key = `${category}\u0000${date}`;
    if (!groups.has(key)) groups.set(key, { date, timestamp: Date.parse(`${date}-01`), category, values: [], missing: 0 });
    const group = groups.get(key), value = numeric(row[valueField]);
    if (value === null) group.missing++; else group.values.push(value);
  }
  return [...groups.values()].sort((a, b) => a.timestamp - b.timestamp).map(({ values, ...group }) => ({ ...group, count: values.length, mean: values.length ? values.reduce((sum, value) => sum + value, 0) / values.length : null }));
}

export function comparisonModes(model) {
  const modes = [];
  if (model.categories.length > 1) modes.push('category');
  // Start dates of versions and years of repeated snapshots are not period cohorts.
  if (model.first !== null && model.last > model.first && !['snapshot', 'interval'].includes(model.data.temporalMode)) modes.push('period');
  return modes;
}

export function comparisonMode(model, controls = {}) {
  const modes = comparisonModes(model);
  return modes.includes(controls.compareMode) ? controls.compareMode : modes[0] || null;
}

export function compareGroups(model, records, controls = {}) {
  const metric = metricOf(model, controls), mode = comparisonMode(model, controls);
  if (!mode) return [];
  let groups;
  if (mode === 'category') {
    groups = [controls.compareA ?? model.categories[0], controls.compareB ?? model.categories[1]].map(category => ({ label: category || 'No category', records: records.filter(row => String(row[model.categoryField]) === category) }));
  } else {
    const middle = model.first !== null && model.last !== null ? Math.floor((model.first + model.last) / 2) : null;
    const bounds = [[controls.compareAFrom ?? model.first, controls.compareATo ?? middle], [controls.compareBFrom ?? (middle !== null ? middle + (model.data.timeStep || 1) : null), controls.compareBTo ?? model.last]];
    groups = bounds.map(([from, to]) => ({ label: from === null || to === null ? 'No dated period' : `${timeText(model, Number(from))}–${timeText(model, Number(to))}`, records: records.filter(row => { const year = numeric(row[model.yearField]); return year !== null && from !== null && to !== null && year >= Number(from) && year <= Number(to); }) }));
  }
  return groups.map(group => ({ label: group.label, ...describe(group.records, metric?.key) }));
}

export function recordGeometry(record) {
  if (record.geometry?.type && record.geometry.coordinates) return record.geometry;
  const lon = numeric(record.longitude), lat = numeric(record.latitude);
  return lon !== null && lat !== null && lon >= -180 && lon <= 180 && lat >= -90 && lat <= 90 ? { type: 'Point', coordinates: [lon, lat] } : null;
}

/** True only when a located record's whole geometry extent is outside the frame. */
export function recordOutsideBounds(record, bounds) {
  const geometry = recordGeometry(record);
  if (!geometry) return false;
  let west = Infinity, east = -Infinity, south = Infinity, north = -Infinity;
  const visit = coordinates => {
    if (!Array.isArray(coordinates)) return;
    if (numeric(coordinates[0]) !== null && numeric(coordinates[1]) !== null) {
      west = Math.min(west, coordinates[0]); east = Math.max(east, coordinates[0]);
      south = Math.min(south, coordinates[1]); north = Math.max(north, coordinates[1]);
    } else coordinates.forEach(visit);
  };
  visit(geometry.coordinates);
  return west !== Infinity && (east < bounds.west || west > bounds.east || north < bounds.south || south > bounds.north);
}

export function safeCell(value) {
  if (value === null || value === undefined) return '';
  // Spreadsheet-safe text: retain numeric negatives, but prevent formulas in source text.
  if (typeof value === 'string' && /^[\s]*[=+@-]/.test(value)) return `'${value}`;
  return typeof value === 'object' ? JSON.stringify(value) : value;
}

export function recordsCSV(bundle, options = {}) {
  const model = recordModel(bundle), records = filterRecords(model, options);
  const columns = model.columns, hasGeometry = records.some(row => row.geometry);
  const keys = columns.map(column => column.key);
  const extras = ['id', 'longitude', 'latitude'].filter(key => !keys.includes(key) && records.some(row => !missing(row[key])));
  if (hasGeometry && !keys.includes('geometry')) extras.push('geometry');
  const allKeys = [...keys, ...extras];
  const snapshots = model.data.sourceSnapshots || (model.data.sourceSnapshot ? [model.data.sourceSnapshot] : []);
  return { filename: `kfm-${String(bundle.story || bundle.id || 'records').replace(/[^a-zA-Z0-9_-]/g, '-')}-selection.csv`,
    rows: [[...allKeys, 'source_urls', 'snapshot_retrieved_at', 'snapshot_sha256'], ...records.map(row => [...allKeys.map(key => safeCell(row[key])), (bundle.sources || []).map(source => source.url).filter(Boolean).join(' | '), snapshots.map(snapshot => snapshot.retrievedAt || '').join(' | '), snapshots.map(snapshot => snapshot.rawSha256 || '').join(' | ')])] };
}
