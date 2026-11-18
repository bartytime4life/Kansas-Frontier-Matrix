export function recordedEvents(record, year) {
  const events = [];
  if (record.established === year) events.push('Established');
  if (record.discontinued === year) events.push('Discontinued');
  return events;
}

export function postalTimeline(records) {
  const byYear = new Map();
  for (const record of records) {
    for (const field of ['established', 'discontinued']) {
      const year = record[field];
      if (!Number.isInteger(year)) continue;
      const entry = byYear.get(year) ?? { year, established: 0, discontinued: 0 };
      entry[field]++;
      byYear.set(year, entry);
    }
  }
  const min = Math.min(...byYear.keys());
  const max = Math.max(...byYear.keys());
  const years = Array.from({ length: max - min + 1 }, (_, index) => {
    const year = min + index;
    return byYear.get(year) ?? { year, established: 0, discontinued: 0 };
  });
  const busiest = [...byYear.values()].sort((a, b) =>
    (b.established + b.discontinued) - (a.established + a.discontinued) || a.year - b.year,
  )[0].year;
  return { min, max, busiest, years };
}

export function officesInView(records, year, view) {
  return view === 'all'
    ? records
    : records.filter(record => recordedEvents(record, year).length);
}

export function readPostalView(params, timeline, records) {
  const value = typeof params?.year === 'string' && /^\d{4}$/.test(params.year) ? Number(params.year) : null;
  const year = value >= timeline.min && value <= timeline.max ? value : timeline.busiest;
  const view = params?.view === 'all' ? 'all' : 'events';
  const selected = officesInView(records, year, view).find(record => record.id === params?.office);
  return { year, view, office: selected?.id ?? null };
}

export function locationText(record) {
  return record.location ? 'Approximate GNIS match' : 'No matched coordinates';
}

export function continuityText(record) {
  if (record.continuous === false) return 'Marked noncontinuous. Exact interruption dates unavailable.';
  if (!Number.isInteger(record.established) || !Number.isInteger(record.discontinued)) return 'A start or end year is unrecorded.';
  return record.continuous === true ? 'Recorded as continuous between the listed years.' : 'Continuity unrecorded.';
}

export function postalMap(ring, records) {
  const coordinates = [...ring, ...records.flatMap(({ location }) => location ? [[location.longitude, location.latitude]] : [])];
  const longitudes = coordinates.map(point => point[0]);
  const latitudes = coordinates.map(point => point[1]);
  const west = Math.min(...longitudes);
  const east = Math.max(...longitudes);
  const south = Math.min(...latitudes);
  const north = Math.max(...latitudes);
  const middleLat = (north + south) / 2;
  const middleLon = (east + west) / 2;
  const lonScale = Math.cos(middleLat * Math.PI / 180);
  const aspect = 1.6;
  const scale = 82 / Math.max((east - west) * lonScale / aspect, north - south);
  const project = (lon, lat) => ({
    x: 50 + (lon - middleLon) * lonScale * scale / aspect,
    y: 50 - (lat - middleLat) * scale,
  });
  const clip = ring.map(([lon, lat]) => {
    const { x, y } = project(lon, lat);
    return `${x.toFixed(3)}% ${y.toFixed(3)}%`;
  });
  return { project, boundaryClip: `polygon(${clip.join(', ')})` };
}

export function mapOfficeGroups(records, project) {
  const points = new Map();
  for (const record of records) {
    if (!record.location) continue;
    const { longitude, latitude } = record.location;
    const key = `${longitude},${latitude}`;
    const group = points.get(key) ?? { key, ...project(longitude, latitude), records: [] };
    group.records.push(record);
    points.set(key, group);
  }
  return [...points.values()];
}

export function postalCSV(records, year, view, source) {
  return [
    ['Source ID', 'Name', 'Source counties', 'Established year', 'Discontinued year', 'Continuous flag',
      'Location status', 'Longitude', 'Latitude', 'GNIS ID', 'View', 'Selected year', 'Recorded events in selected year', 'Source URL', 'Source SHA-256'],
    ...records.map(record => [
      record.id, record.name, record.counties.join(' / '), record.established, record.discontinued, record.continuous,
      locationText(record), record.location?.longitude, record.location?.latitude, record.location?.gnisId,
      view, year, recordedEvents(record, year).join(' and '), source.url, source.sha256,
    ]),
  ];
}
