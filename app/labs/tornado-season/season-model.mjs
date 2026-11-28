export const MONTHS = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'];
export const PERIODS = [
  { id: 'recent', label: '2008–2025', from: 2008, to: 2025 },
  { id: 'historical', label: '1950–2006', from: 1950, to: 2006 },
  { id: 'all', label: '1950–2025', from: 1950, to: 2025 },
];

// A display envelope includes the Kansas border area and the reported ends of
// its mapped paths. It also keeps three discrepant historical starts off the map.
export const MAP_BOUNDS = { west: -102.3, south: 36.75, east: -93.5, north: 40.65 };

export function seasonSettings(query = {}) {
  return {
    period: PERIODS.some(period => period.id === query.period) ? query.period : 'recent',
    month: typeof query.month === 'string' && /^(?:[1-9]|1[0-2])$/.test(query.month) ? Number(query.month) : 0,
    layer: query.layer === 'lines' ? 'lines' : 'starts',
  };
}

export function summarizeSeason(records, period) {
  const months = MONTHS.map((name, index) => ({ name, month: index + 1, rows: [], dates: new Map() }));
  for (const row of records) {
    if (!(row.year >= period.from && row.year <= period.to)) continue;
    const month = months[Number(row.date.slice(5, 7)) - 1];
    if (!month) continue;
    month.rows.push(row);
    month.dates.set(row.date, (month.dates.get(row.date) ?? 0) + 1);
  }
  const tracks = months.reduce((count, month) => count + month.rows.length, 0);
  const days = months.reduce((count, month) => count + month.dates.size, 0);
  const aprilJune = months.slice(3, 6);
  return {
    months,
    tracks,
    days,
    aprilJuneTracks: aprilJune.reduce((count, month) => count + month.rows.length, 0),
    aprilJuneDays: aprilJune.reduce((count, month) => count + month.dates.size, 0),
  };
}

export function inMap(lon, lat) {
  const { west, south, east, north } = MAP_BOUNDS;
  return Number.isFinite(lon) && Number.isFinite(lat) && lon >= west && lon <= east && lat >= south && lat <= north;
}

export function mapCoverage(records) {
  const starts = [];
  const paths = [];
  for (const row of records) {
    if (!inMap(row.longitude, row.latitude)) continue;
    starts.push(row);
    const points = row.geometry?.coordinates;
    if (row.geometry?.type === 'LineString' && points?.length === 2 && points.every(([lon, lat]) => inMap(lon, lat))) {
      paths.push(row);
    }
  }
  return { starts, paths };
}

export function busiestDate(months) {
  let busiest = null;
  for (const { dates } of months) {
    for (const [date, tracks] of dates) {
      if (!busiest || tracks > busiest.tracks || tracks === busiest.tracks && date < busiest.date) busiest = { date, tracks };
    }
  }
  return busiest;
}

export function displayRating(row) {
  if (!Number.isInteger(row.magnitude) || row.magnitude < 0 || row.magnitude > 5) return 'Unknown';
  return (row.date < '2007-02-01' ? 'F' : 'EF') + row.magnitude;
}

export function seasonCsv(records) {
  return [
    ['record_id', 'spc_id', 'date_as_reported', 'time_as_reported', 'damage_rating', 'path_length_miles', 'path_width_yards', 'injuries', 'fatalities', 'start_latitude', 'start_longitude', 'end_latitude', 'end_longitude'],
    ...records.map(row => {
      const [lon, lat] = row.geometry?.coordinates?.[1] ?? [];
      return [row.id, row.sourceId, row.date, row.sourceTime, displayRating(row), row.length, row.width,
        row.injuries, row.fatalities, row.latitude, row.longitude, lat, lon];
    }),
  ];
}
