import { buildCountyModel } from './county-model.mjs';
import { validKansasFips } from './county-csv.mjs';
import { HISTORY_METRICS } from './county-investigations.mjs';
import { PUBLIC_LAB_SNAPSHOTS } from './public-snapshots.mjs';

const SOURCE_IDS = { county: ['census-mosaic', 'county-conditions', 'built-kansas', 'air-and-health'], signal: ['climate-stripes', 'energy-shift', 'river-memory', 'tornado-tracks', 'shaking-ground'] };
const countyMetrics = new Set(buildCountyModel().metrics.map(item => item.key));
const energy = 'BMTCB CLTCB CLPRB TECCB PAPRB TEEIB GETCB HYTCB HYPRB TEICB NGMPB NGTCB NUETB NUPRB PATCB RETCB REPRB TERCB SOTCB SOPRB TETCB TEPRB TEACB WYTCB WYPRB WWPRB'.split(' ');
export const SUPPORTED_SIGNAL_IDS = Object.freeze([
  ...['20', ...Array.from({ length: 9 }, (_, index) => String(1401 + index))].flatMap(area => ['pcpn', 'pdsi', 'tmpc'].map(element => `climate:${area}:${element}`)),
  ...energy.map(series => `energy:SEDS.${series}.KS.A`), ...['06887000', '06892350', '07144300'].map(site => `river:${site}`),
  ...['count', 'fatalities', 'injuries', 'maxLength'].map(key => `tornado:${key}`), ...['count', 'count3', 'maxMagnitude'].map(key => `quake:${key}`),
]);
const signals = new Set(SUPPORTED_SIGNAL_IDS);
export function currentSourceBindings(workspace) {
  if (!SOURCE_IDS[workspace]) throw new Error('Unknown investigation workspace.');
  return Object.fromEntries(SOURCE_IDS[workspace].map(id => [id, PUBLIC_LAB_SNAPSHOTS[id].sha256]));
}
const integer = (value, min, max) => Number.isInteger(value) && value >= min && value <= max;
export function validateInvestigationState(workspace, state, { privateData } = {}) {
  if (!SOURCE_IDS[workspace] || !state || typeof state !== 'object' || Array.isArray(state) || Object.getPrototypeOf(state) !== Object.prototype || Object.keys(state).length > 40) throw new Error('Invalid investigation settings.');
  if (workspace === 'signal' && privateData) throw new Error('Signal investigations cannot contain private county attachments.');
  const privateKeys = new Set(privateData?.columns?.map(item => item.key) || []);
  const metric = value => typeof value === 'string' && (countyMetrics.has(value) || privateKeys.has(value));
  const county = {
    countyA: validKansasFips, countyB: validKansasFips, mapMetric: metric, xMetric: metric, yMetric: metric,
    populationYear: value => integer(value, 2020, 2025), acsYear: value => [2014, 2019, 2024].includes(value),
    aqiYear: value => integer(value, 2000, 2025), inventoryYear: value => value === 2026,
    rankOrder: value => ['asc', 'desc'].includes(value), query: value => typeof value === 'string' && value.length <= 300,
    historyMetric: value => HISTORY_METRICS.includes(value),
    peerKeys: value => typeof value === 'string' && value.length <= 300 && (() => { const keys = value.split(','); return keys.length >= 2 && keys.length <= 5 && new Set(keys).size === keys.length && keys.every(metric); })(),
  };
  const signal = { x: value => signals.has(value), y: value => signals.has(value), from: value => integer(value, 1800, 2100), to: value => integer(value, 1800, 2100), lag: value => integer(value, -5, 5), transform: value => ['raw', 'difference', 'detrended'].includes(value), selectedYear: value => value === null || integer(value, 1800, 2100) };
  const checks = workspace === 'county' ? county : signal;
  for (const [key, value] of Object.entries(state)) if (!Object.hasOwn(checks, key) || !checks[key](value)) throw new Error(`Unsupported ${workspace} investigation setting: ${key}.`);
  if (workspace === 'signal' && state.from !== undefined && state.to !== undefined && state.from > state.to) throw new Error('Investigation start year must be no later than end year.');
  return { ...state };
}
