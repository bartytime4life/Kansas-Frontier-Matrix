// Builds the table the Kansas records page reads (app/kansas-records.generated.json) from four bundles the labs
// already ship. Every entry is the largest or smallest value in one named dataset, never a claim beyond it.
// No network. Run after a bundle changes: node scripts/prepare-kansas-records.mjs
import { readFile, writeFile } from 'node:fs/promises';
import { createHash } from 'node:crypto';
import { resolve } from 'node:path';
import { pathToFileURL } from 'node:url';
import { COUNTY_LAB_SNAPSHOTS } from '../app/labs/county-snapshots.mjs';
import { BASE_LAB_SNAPSHOTS } from '../app/labs/base-snapshots.mjs';
import { BRIDGE_LAB_SNAPSHOTS } from '../app/labs/bridge-snapshots.mjs';
import { countySlug } from './prepare-county-pages.mjs';

const SNAPSHOTS = Object.freeze({
  population: BASE_LAB_SNAPSHOTS['census-mosaic'],
  conditions: COUNTY_LAB_SNAPSHOTS['county-conditions'],
  bridges: BRIDGE_LAB_SNAPSHOTS['built-kansas'],
  tornadoes: BASE_LAB_SNAPSHOTS['tornado-tracks'],
});
const snapshotReference = ({ path, bytes, sha256 }) => ({ path, bytes, sha256 });

const whole = new Intl.NumberFormat('en-US', { maximumFractionDigits: 0 });
const one = value => (Math.round(value * 10) / 10).toFixed(1);
const longDate = iso => new Date(`${iso.slice(0, 10)}T12:00:00Z`).toLocaleDateString('en-US', { year: 'numeric', month: 'long', day: 'numeric', timeZone: 'UTC' });
const titleCase = text => String(text).toLowerCase().replace(/\b[a-z]/g, letter => letter.toUpperCase());
// Every record that shares the extreme value, so a tie is reported as a tie.
function extreme(records, value, direction) {
  let best = null, found = [];
  for (const record of records) {
    const v = value(record);
    if (typeof v !== 'number' || !Number.isFinite(v)) continue;
    if (best === null || (direction === 'max' ? v > best : v < best)) { best = v; found = [record]; } else if (v === best) found.push(record);
  }
  if (best === null) throw new Error('KANSAS_RECORDS_EMPTY');
  return { value: best, records: found };
}
const county = record => ({ where: `${record.name}, Kansas`, href: `/counties/${countySlug(record.name)}` });
const shared = found => found.records.length > 1 ? `Shared by ${found.records.length} counties; the first alphabetically is shown.` : undefined;
const first = found => [...found.records].sort((a, b) => String(a.name).localeCompare(String(b.name)))[0];

export function buildKansasRecords({ population, conditions, bridges, tornadoes }) {
  // People: July 1 population estimates for the newest year and the first year of the vintage.
  const years = [...new Set(population.data.records.map(r => r.year))].sort((a, b) => a - b), year = years.at(-1), baseYear = years[0];
  const base = new Map(population.data.records.filter(r => r.year === baseYear).map(r => [r.fips, r.population]));
  const now = population.data.records.filter(r => r.year === year).map(r => ({ ...r, change: r.population - base.get(r.fips), changePct: (r.population - base.get(r.fips)) / base.get(r.fips) * 100 }));
  if (now.length !== 105 || now.some(r => !Number.isFinite(r.change))) throw new Error('KANSAS_RECORDS_POPULATION_INCOMPLETE');
  const person = (label, found, text) => ({ label, value: text(found.value), ...county(first(found)), note: shared(found) });
  const people = [
    person('Most people', extreme(now, r => r.population, 'max'), v => whole.format(v)),
    person('Fewest people', extreme(now, r => r.population, 'min'), v => whole.format(v)),
    person(`Largest gain since ${baseYear}`, extreme(now, r => r.change, 'max'), v => `${whole.format(v)} more people`),
    person(`Largest loss since ${baseYear}`, extreme(now, r => r.change, 'min'), v => `${whole.format(Math.abs(v))} fewer people`),
    person(`Fastest growth since ${baseYear}`, extreme(now, r => r.changePct, 'max'), v => `up ${one(v)}%`),
    person(`Steepest decline since ${baseYear}`, extreme(now, r => r.changePct, 'min'), v => `down ${one(Math.abs(v))}%`),
  ];

  // Survey estimates for the newest five-year period, each with its 90% margin of error.
  const latestYear = Math.max(...conditions.data.records.map(r => r.year)), survey = conditions.data.records.filter(r => r.year === latestYear);
  if (survey.length !== 105) throw new Error('KANSAS_RECORDS_SURVEY_INCOMPLETE');
  const estimate = (label, key, direction, text) => {
    const found = extreme(survey, r => r[key], direction), record = first(found);
    return { label, value: `${text(found.value)} (±${text(record[`${key}Moe`]).replace(/^\$/, '$')})`, ...county(record), note: shared(found) };
  };
  const dollars = v => `$${whole.format(v)}`, ageText = v => `${one(v)} years`, pct = v => `${one(v)}%`;
  const surveyItems = [
    estimate('Highest median household income', 'medianIncome', 'max', dollars), estimate('Lowest median household income', 'medianIncome', 'min', dollars),
    estimate('Oldest median age', 'medianAge', 'max', ageText), estimate('Youngest median age', 'medianAge', 'min', ageText),
    estimate('Largest share of adults with a bachelor’s degree or higher', 'educationPct', 'max', pct),
    estimate('Highest median home value', 'medianHomeValue', 'max', dollars),
  ];

  // Bridges: the KDOT inventory, where a record is not always one physical bridge.
  const inventory = bridges.data.records, perCounty = new Map();
  for (const record of inventory) { const name = `${titleCase(String(record.county).trim())} County`; perCounty.set(name, (perCounty.get(name) ?? 0) + 1); }
  if (perCounty.size !== 105) throw new Error('KANSAS_RECORDS_BRIDGE_COUNTIES');
  const counts = [...perCounty].map(([name, records]) => ({ name, records }));
  // The inventory's own wording, unchanged: it abbreviates, and tidying it would be guessing.
  const bridgeLine = record => `Recorded as “${String(record.name).trim()}” over “${String(record.crossing).trim()}”, ${titleCase(String(record.county).trim())} County`;
  const bridgeMap = record => `/?ctx=kdot-bridges-state,kdot-bridges-local&c=${record.longitude},${record.latitude}&z=14`;
  const oldest = extreme(inventory, r => Number.isInteger(r.year) ? r.year : null, 'min'), longest = extreme(inventory, r => r.length, 'max');
  const most = extreme(counts, r => r.records, 'max'), fewest = extreme(counts, r => r.records, 'min');
  const bridgeItems = [
    { label: 'Oldest recorded built year', value: String(oldest.value), where: oldest.records.length === 1 ? bridgeLine(oldest.records[0]) : `${oldest.records.length} inventory records share this year`, href: oldest.records.length === 1 && Number.isFinite(oldest.records[0].longitude) ? bridgeMap(oldest.records[0]) : undefined },
    { label: 'Longest structure', value: `${whole.format(longest.value)} feet`, where: bridgeLine(longest.records[0]), href: Number.isFinite(longest.records[0].longitude) ? bridgeMap(longest.records[0]) : undefined, note: longest.records.length > 1 ? `${longest.records.length} inventory records share this length; one is shown.` : undefined },
    { label: 'Most bridge records in a county', value: whole.format(most.value), ...county(first(most)), note: shared(most) },
    { label: 'Fewest bridge records in a county', value: whole.format(fewest.value), ...county(first(fewest)), note: shared(fewest) },
  ];

  // Tornadoes that started in Kansas. A whole track is counted once and can cross the state line.
  const tracks = tornadoes.data.records, byYear = new Map();
  for (const track of tracks) byYear.set(track.year, (byYear.get(track.year) ?? 0) + 1);
  const busiest = extreme([...byYear].map(([y, n]) => ({ year: y, n })), r => r.n, 'max');
  const when = track => `${longDate(track.date)} · rated ${track.rating === 'Unknown' ? 'unknown' : track.rating}`;
  const tornado = (label, key, text, extra) => { const found = extreme(tracks, r => r[key], 'max'); return { label, value: text(found.value), where: when(found.records[0]), note: found.records.length > 1 ? `${found.records.length} tornadoes share this value; the earliest is shown.` : extra }; };
  const top = tracks.filter(track => track.rating === 'F/EF5').sort((a, b) => a.date.localeCompare(b.date));
  const tornadoItems = [
    { label: 'Tornadoes in the record', value: whole.format(tracks.length), where: `${Math.min(...byYear.keys())}–${Math.max(...byYear.keys())}` },
    { label: 'Year with the most', value: `${whole.format(busiest.value)} tornadoes`, where: busiest.records.map(r => r.year).sort().join(', ') },
    tornado('Longest path', 'length', v => `${one(v)} miles`), tornado('Widest path', 'width', v => `${whole.format(v)} yards`),
    tornado('Most reported deaths', 'fatalities', v => `${whole.format(v)} deaths`, 'Deaths are for the whole track, which can extend outside Kansas.'),
    { label: 'Rated F5 or EF5', value: `${top.length} tornadoes`, where: top.length ? `most recently on ${longDate(top.at(-1).date)}` : 'none' },
  ];

  return {
    sections: [
      { id: 'people', title: 'People', source: `U.S. Census Bureau July 1 population estimates, ${baseYear} and ${year}`, caution: 'A later release can revise earlier years.', snapshot: snapshotReference(SNAPSHOTS.population), items: people },
      { id: 'survey', title: 'Income, age, education and homes', source: `U.S. Census Bureau American Community Survey 5-year estimates, ${survey[0].period}`, caution: 'These are survey estimates with 90% margins of error. Where margins overlap, the county shown may not truly rank first.', snapshot: snapshotReference(SNAPSHOTS.conditions), items: surveyItems },
      { id: 'bridges', title: 'Bridges', source: `Kansas Department of Transportation bridge inventory as of ${bridges.data.inventoryAsOf}`, caution: 'Inventory records are not always one physical bridge each. Unknown built years are left out, not guessed.', snapshot: snapshotReference(SNAPSHOTS.bridges), items: bridgeItems },
      { id: 'tornadoes', title: 'Tornadoes', source: `NOAA Storm Prediction Center tornado tracks that started in Kansas, ${Math.min(...byYear.keys())}–${Math.max(...byYear.keys())}`, caution: 'Earlier tornadoes are under-reported, so counts by year are not a trend. Tracks that began in another state are not included.', snapshot: snapshotReference(SNAPSHOTS.tornadoes), items: tornadoItems },
    ].map(section => ({ ...section, items: section.items.map(item => Object.fromEntries(Object.entries(item).filter(([, v]) => v !== undefined))) })),
    sources: Object.fromEntries(Object.entries(SNAPSHOTS).map(([name, snapshot]) => [name, snapshot.sha256])),
  };
}

export async function readRecordBundles(root = process.cwd()) {
  const entries = await Promise.all(Object.entries(SNAPSHOTS).map(async ([name, snapshot]) => {
    const bytes = await readFile(resolve(root, 'public', snapshot.path.replace(/^\//, '')));
    if (bytes.length !== snapshot.bytes || createHash('sha256').update(bytes).digest('hex') !== snapshot.sha256) {
      throw new Error(`KANSAS_RECORDS_SNAPSHOT_MISMATCH ${name}`);
    }
    return [name, JSON.parse(bytes.toString('utf8'))];
  }));
  return Object.fromEntries(entries);
}

if (process.argv[1] && import.meta.url === pathToFileURL(resolve(process.argv[1])).href) {
  const records = buildKansasRecords(await readRecordBundles());
  await writeFile('app/kansas-records.generated.json', JSON.stringify(records, null, 1) + '\n');
  console.log(`Kansas records: ${records.sections.reduce((sum, section) => sum + section.items.length, 0)} entries in ${records.sections.length} sections`);
}
