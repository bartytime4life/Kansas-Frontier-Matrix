import { SCIENCE_TOOLS, scienceToolPath } from './science-handoff.mjs';

const period = ({ from, to }) => `${from.slice(0, 4)}–${to.slice(0, 4)}`;
const count = new Intl.NumberFormat('en-US');

/** Build the directory from the same manifests the labs actually use. */
export function nativeScienceDirectory({ climate, drought, soil, air, sunlight }) {
  const metadata = {
    weather: { topic: 'Weather & climate', question: 'When did it get hot, freeze, or get wet?',
      coverage: `${climate.stations.length} stations · daily · ${period(climate.period)}`,
      source: 'NOAA GHCN-Daily', keywords: 'weather temperature frost rain snowfall heat precipitation station' },
    drought: { topic: 'Water & land', question: 'How much of my county was in drought?',
      coverage: `${drought.counties.length} counties · ${count.format(drought.snapshot.weeks)} weekly assessments · ${period(drought.period)}`,
      source: 'U.S. Drought Monitor', keywords: 'water soil agriculture dry severe coverage county' },
    soil: { topic: 'Water & land', question: 'What changed below the surface?',
      coverage: `${soil.stations.length} stations · ${soil.depthsCm.length} depths · ${period(soil.period)}`,
      source: 'NOAA USCRN', keywords: 'soil irrigation moisture water sensors subsurface temperature agriculture' },
    air: { topic: 'Air & sunlight', question: 'When did reported air quality change?',
      coverage: `${air.counties.length} reporting counties · daily AQI · ${period(air.period)}`,
      source: 'EPA AirData', keywords: 'air aqi pollution smoke ozone monitor county' },
    sunlight: { topic: 'Air & sunlight', question: 'How did modeled sunlight change?',
      coverage: `${sunlight.points.length} query points · daily estimates · ${period(sunlight.period)}`,
      source: 'NASA POWER', keywords: 'sunlight solar energy radiation sky clear cloud weather' },
    comparison: { topic: 'Reports & workspaces', question: 'What differed between two years?',
      coverage: `Topeka, Wichita and Dodge City areas · monthly and annual · ${period(climate.period)}`,
      source: 'NOAA, USDM, EPA and NASA POWER', keywords: 'weather drought air sunlight precipitation report csv json print compare' },
  };
  return SCIENCE_TOOLS.map(tool => ({ ...tool, ...metadata[tool.id], href: tool.path, native: true,
    kind: tool.id === 'comparison' ? 'Report' : 'Lab' }));
}

const words = text => text.toLocaleLowerCase('en-US').match(/[\p{L}\p{N}]+/gu) ?? [];

export function filterScienceDirectory(entries, query, topic) {
  const terms = words(query);
  return entries.filter(entry => {
    if (topic && entry.topic !== topic) return false;
    const searchable = words([entry.label, entry.question, entry.topic, entry.source, entry.coverage, entry.keywords].join(' '));
    return terms.every(term => searchable.some(word => word.includes(term)));
  });
}

export function directoryEntryPath(entry, selectedYear) {
  return entry.native && selectedYear !== null ? scienceToolPath(entry.id, selectedYear) : entry.href;
}
