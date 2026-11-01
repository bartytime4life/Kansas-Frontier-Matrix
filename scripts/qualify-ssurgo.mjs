#!/usr/bin/env node
/**
 * Read-only SSURGO qualification of one Kansas soil survey area through USDA Soil Data Access.
 * It reports the survey version, map units, component percentages, map-unit polygons and the
 * units SSURGO publishes for core horizon properties, with a digest of every query and response.
 * It writes nothing unless asked to, admits no source and decides no rights; see
 * docs/ssurgo-qualification.md.
 */
import { createHash } from 'node:crypto';
import { writeFile } from 'node:fs/promises';
import { resolve } from 'node:path';
import { fileURLToPath } from 'node:url';

export const SDA_URL = 'https://sdmdataaccess.sc.egov.usda.gov/Tabular/post.rest';
const MAX_RESPONSE = 4 * 1024 ** 2;
// Core horizon properties a soil lane would carry; units come from SSURGO's own attribute table.
export const HORIZON_COLUMNS = Object.freeze(['awc_r', 'claytotal_r', 'dbthirdbar_r', 'ksat_r', 'om_r', 'ph1to1h2o_r', 'sandtotal_r']);
// Raw horizon units from USDA's Tables and Columns report. SDV storage is a
// separate, depth-integrated attribute; it never changes the unit of raw awc_r.
const RAW_UNITS = Object.freeze({ awc_r: 'cm/cm', claytotal_r: 'percent', dbthirdbar_r: 'g/cm3',
  ksat_r: 'um/s', om_r: 'percent', ph1to1h2o_r: null, sandtotal_r: 'percent' });
const COLUMNS = Object.freeze({
  survey: ['areasymbol', 'areaname', 'saversion', 'saverest'],
  mapunits: ['mukey', 'musym', 'muname', 'mukind', 'muacres'],
  components: ['mukey', 'components', 'unique_components', 'pct_count', 'min_pct', 'max_pct', 'pct', 'major'],
  polygons: ['mukey', 'polygons', 'unique_polygons'],
  units: ['attributekey', 'attributecolumnname', 'attributename', 'attributeuomabbrev', 'horzaggmeth'],
});
// A survey area symbol is the only interpolated value, so it is checked before any query is built.
const AREA = /^KS[0-9]{3}$/;

const sha = value => createHash('sha256').update(value).digest('hex');
const fail = code => { throw new Error(code); };

export function queries(area) {
  if (!AREA.test(area ?? '')) fail('AREA_SYMBOL_INVALID');
  const inArea = `INNER JOIN legend l ON l.lkey = mu.lkey WHERE l.areasymbol = '${area}'`;
  return {
    survey: `SELECT areasymbol, areaname, saversion, saverest FROM sacatalog WHERE areasymbol = '${area}'`,
    mapunits: `SELECT mu.mukey, mu.musym, mu.muname, mu.mukind, mu.muacres FROM mapunit mu ${inArea} ORDER BY mu.mukey`,
    components: `SELECT c.mukey, COUNT(*) AS components, COUNT(DISTINCT c.cokey) AS unique_components, COUNT(c.comppct_r) AS pct_count, MIN(c.comppct_r) AS min_pct, MAX(c.comppct_r) AS max_pct, SUM(c.comppct_r) AS pct, SUM(CASE WHEN c.majcompflag = 'Yes' THEN 1 ELSE 0 END) AS major FROM component c INNER JOIN mapunit mu ON mu.mukey = c.mukey ${inArea} GROUP BY c.mukey ORDER BY c.mukey`,
    polygons: `SELECT mukey, COUNT(*) AS polygons, COUNT(DISTINCT mupolygonkey) AS unique_polygons FROM mupolygon WHERE areasymbol = '${area}' GROUP BY mukey ORDER BY mukey`,
    units: `SELECT attributekey, attributecolumnname, attributename, attributeuomabbrev, horzaggmeth FROM sdvattribute WHERE attributetablename = 'chorizon' AND attributecolumnname IN (${HORIZON_COLUMNS.map(c => `'${c}'`).join(', ')}) ORDER BY attributecolumnname, attributename, attributekey`,
  };
}

/** One bounded POST; SDA answers {} for no rows and an XML ServiceException for a failed query. */
async function sda(query, expected, fetcher) {
  const response = await fetcher(SDA_URL, { method: 'POST', headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ query, format: 'JSON+COLUMNNAME' }), signal: AbortSignal.timeout(90_000) });
  if (!response.ok || !response.body) { await response.body?.cancel(); fail('SDA_QUERY_FAILED'); }
  const chunks = []; let bytes = 0;
  for await (const chunk of response.body) {
    bytes += chunk.byteLength;
    if (bytes > MAX_RESPONSE) fail('SDA_QUERY_FAILED');
    chunks.push(chunk);
  }
  const text = Buffer.concat(chunks).toString('utf8');
  let value;
  try { value = JSON.parse(text); } catch { fail('SDA_QUERY_FAILED'); }
  if (!value || typeof value !== 'object' || Array.isArray(value)) fail('SDA_RESPONSE_INVALID');
  // Only {} is SDA's documented empty result. Error objects and wrong headers
  // must never turn into apparently valid empty or partially populated tables.
  if (!Object.keys(value).length) return { rows: [], responseSha256: sha(text) };
  if (Object.keys(value).length !== 1 || !Array.isArray(value.Table) || !value.Table.length) fail('SDA_RESPONSE_INVALID');
  const [columns, ...rows] = value.Table;
  if (!Array.isArray(columns) || columns.length !== expected.length || new Set(columns).size !== columns.length
    || expected.some(name => !columns.includes(name))
    || rows.some(row => !Array.isArray(row) || row.length !== columns.length
      || row.some(cell => cell !== null && !['string', 'number'].includes(typeof cell)))) fail('SDA_RESPONSE_INVALID');
  return { rows: rows.map(row => Object.fromEntries(columns.map((name, i) => [name, row[i]]))), responseSha256: sha(text) };
}

const nonempty = value => typeof value === 'string' && value.trim().length > 0;
const count = value => {
  if (typeof value !== 'number' && (typeof value !== 'string' || !/^-?\d+(?:\.\d+)?$/.test(value))) return null;
  const n = Number(value); return Number.isFinite(n) ? n : null;
};
const integer = value => { const n = count(value); return Number.isSafeInteger(n) && n >= 0 ? n : null; };
const key = value => /^(?:0|[1-9]\d*)$/.test(String(value)) && integer(value) !== null;
const duplicateKeys = rows => new Set(rows.map(r => String(r.mukey))).size !== rows.length;
const validSurvey = (rows, area) => rows.length === 1 && rows[0].areasymbol === area
  && nonempty(rows[0].areaname) && integer(rows[0].saversion) > 0 && nonempty(rows[0].saverest)
  && Number.isFinite(Date.parse(rows[0].saverest));

export async function qualifySsurgo(area, { fetcher = fetch, now = Date.now, expectedVersion } = {}) {
  const text = queries(area);
  if (expectedVersion !== undefined && !(integer(expectedVersion) > 0)) fail('SURVEY_VERSION_INVALID');
  const results = {}, receipts = [];
  // SDA serves current data. Bracket the reads to detect an observed revision
  // during qualification; this is not an atomic snapshot or historical selector.
  for (const [name, query] of [...Object.entries(text), ['surveyEnd', text.survey]]) {
    results[name] = await sda(query, COLUMNS[name === 'surveyEnd' ? 'survey' : name], fetcher);
    receipts.push({ name, query, querySha256: sha(query), responseSha256: results[name].responseSha256, rows: results[name].rows.length });
  }
  const holds = [], findings = [];
  const survey = results.survey.rows;
  if (survey.length !== 1) holds.push('SURVEY_AREA_NOT_FOUND');
  if (!validSurvey(survey, area) || !validSurvey(results.surveyEnd.rows, area)) holds.push('SURVEY_IDENTITY_INVALID');
  const identity = rows => rows.map(r => [r.areasymbol, r.areaname, String(r.saversion), r.saverest]);
  if (JSON.stringify(identity(survey)) !== JSON.stringify(identity(results.surveyEnd.rows))) holds.push('SURVEY_CHANGED_DURING_QUALIFICATION');
  if (expectedVersion !== undefined && (integer(survey[0]?.saversion) !== integer(expectedVersion)
    || integer(results.surveyEnd.rows[0]?.saversion) !== integer(expectedVersion))) holds.push('SURVEY_VERSION_MISMATCH');
  const mapunits = results.mapunits.rows, keys = mapunits.map(m => String(m.mukey));
  if (!mapunits.length) holds.push('NO_MAP_UNITS');
  if (new Set(keys).size !== keys.length) holds.push('MAP_UNIT_KEYS_DUPLICATED');
  if (mapunits.some(m => !key(m.mukey) || !nonempty(m.musym) || !nonempty(m.muname) || !nonempty(m.mukind)
    || count(m.muacres) === null || count(m.muacres) < 0)) holds.push('MAP_UNIT_VALUES_INVALID');
  const componentRows = results.components.rows;
  if (duplicateKeys(componentRows) || componentRows.some(c => !key(c.mukey) || !keys.includes(String(c.mukey))
    || !(integer(c.components) > 0) || integer(c.unique_components) !== integer(c.components)
    || integer(c.pct_count) !== integer(c.components) || integer(c.major) === null || integer(c.major) > integer(c.components)
    || count(c.min_pct) === null || count(c.max_pct) === null || count(c.min_pct) < 0 || count(c.max_pct) > 100
    || count(c.min_pct) > count(c.max_pct))) holds.push('COMPONENT_VALUES_INVALID');
  const components = new Map(results.components.rows.map(c => [String(c.mukey), c]));
  const withoutComponents = keys.filter(key => !components.has(key));
  // Representative component percentages should account for the whole map unit.
  const notWhole = [...components.values()].filter(c => count(c.pct) !== 100).map(c => ({ mukey: String(c.mukey), pct: count(c.pct) }));
  const noMajor = [...components.values()].filter(c => !(count(c.major) > 0)).map(c => String(c.mukey));
  if (withoutComponents.length) holds.push('MAP_UNITS_WITHOUT_COMPONENTS');
  if (notWhole.length) { holds.push('COMPONENT_PERCENT_NOT_100'); findings.push({ code: 'COMPONENT_PERCENT_NOT_100', mapUnits: notWhole }); }
  if (noMajor.length) { holds.push('NO_MAJOR_COMPONENT'); findings.push({ code: 'NO_MAJOR_COMPONENT', mapUnits: noMajor }); }
  // Every tabular map unit needs a polygon, and every polygon a tabular map unit.
  const polygonRows = results.polygons.rows;
  if (duplicateKeys(polygonRows) || polygonRows.some(p => !key(p.mukey) || !(integer(p.polygons) > 0)
    || integer(p.unique_polygons) !== integer(p.polygons))) holds.push('POLYGON_VALUES_INVALID');
  const polygons = new Map(polygonRows.map(p => [String(p.mukey), count(p.polygons)]));
  const unmapped = keys.filter(key => !(polygons.get(key) > 0)), orphaned = [...polygons.keys()].filter(key => !keys.includes(key));
  if (unmapped.length || orphaned.length) holds.push('SPATIAL_TABULAR_MISMATCH');
  // The same column can be published under several attributes with different units
  // (awc_r is cm/cm per horizon and cm as depth-summed storage), so units bind to the attribute.
  const units = HORIZON_COLUMNS.map(column => {
    const rows = results.units.rows.filter(u => u.attributecolumnname === column);
    const unit = u => typeof u.attributeuomabbrev === 'string' ? u.attributeuomabbrev.trim() || null : u.attributeuomabbrev;
    return { column, rawUnit: RAW_UNITS[column], units: [...new Set(rows.map(unit))],
      attributes: rows.map(u => ({ key: String(u.attributekey), name: u.attributename, unit: unit(u), horizonAggregation: u.horzaggmeth })) };
  });
  // Check every attribute, not merely whether one sibling has a unit. Only pH
  // may be unitless. Unknown/mismatched units and conflicting identities hold.
  const missingUnits = units.filter(u => !u.attributes.length || u.rawUnit !== null
    && (u.attributes.some(a => a.unit === null) || !u.attributes.some(a => a.unit === u.rawUnit))).map(u => u.column);
  if (missingUnits.length) { holds.push('HORIZON_UNITS_UNPUBLISHED'); findings.push({ code: 'HORIZON_UNITS_UNPUBLISHED', columns: missingUnits }); }
  const badUnits = units.flatMap(u => u.attributes.filter(a => {
    const storage = u.column === 'awc_r' && a.name === 'Available Water Storage';
    const expected = storage ? 'cm' : u.rawUnit;
    return !key(a.key) || !nonempty(a.name) || a.unit !== null && a.unit !== expected
      || a.horizonAggregation !== (storage ? 'Weighted Sum' : 'Weighted Average')
      || storage && a.key !== '101';
  }).map(a => ({ column: u.column, ...a })));
  const attributeKeys = units.flatMap(u => u.attributes.map(a => a.key));
  const attributeNames = units.flatMap(u => u.attributes.map(a => a.name));
  if (badUnits.length || results.units.rows.some(u => !HORIZON_COLUMNS.includes(u.attributecolumnname))
    || new Set(attributeKeys).size !== attributeKeys.length || new Set(attributeNames).size !== attributeNames.length) {
    holds.push('HORIZON_UNITS_CONTRADICTORY'); findings.push({ code: 'HORIZON_UNITS_CONTRADICTORY', attributes: badUnits });
  }
  const ambiguous = units.filter(u => u.units.filter(Boolean).length > 1).map(u => ({ column: u.column, units: u.units }));
  if (ambiguous.length) findings.push({ code: 'UNIT_DEPENDS_ON_ATTRIBUTE', columns: ambiguous });
  return {
    format: 'kfm-ssurgo-qualification-v2', areaSymbol: area, checkedAt: new Date(now()).toISOString(), source: SDA_URL,
    state: holds.length ? 'held' : 'ready-for-owner-review', holds, findings,
    survey: survey[0] ? { name: survey[0].areaname, version: survey[0].saversion, savedAt: survey[0].saverest } : null,
    expectedVersion: expectedVersion === undefined ? null : integer(expectedVersion),
    mapUnits: { count: mapunits.length, acres: mapunits.reduce((sum, m) => sum + (count(m.muacres) ?? 0), 0),
      byKind: Object.fromEntries([...new Set(mapunits.map(m => m.mukind))].map(kind => [kind, mapunits.filter(m => m.mukind === kind).length])),
      largest: [...mapunits].sort((a, b) => (count(b.muacres) ?? 0) - (count(a.muacres) ?? 0)).slice(0, 5).map(m => ({ mukey: String(m.mukey), symbol: m.musym, name: m.muname, acres: count(m.muacres) })) },
    components: { mapUnitsWithComponents: components.size, total: [...components.values()].reduce((sum, c) => sum + (count(c.components) ?? 0), 0) },
    polygons: { count: [...polygons.values()].reduce((sum, n) => sum + (n ?? 0), 0), mapUnits: polygons.size, unmapped, orphaned },
    horizonUnits: units, receipts,
    // Qualification evidence only: rights, sensitivity and admission stay with the owner.
    rights: 'REVIEW_REQUIRED', admitted: false, capture: false, publication: false,
  };
}

if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  const [area, ...args] = process.argv.slice(2);
  try {
    let out, expectedVersion;
    for (let i = 0; i < args.length; i += 2) {
      if (args[i] === '--out' && out === undefined && args[i + 1]) out = args[i + 1];
      else if (args[i] === '--expected-version' && expectedVersion === undefined && args[i + 1]) expectedVersion = args[i + 1];
      else fail('USE_AREA_SYMBOL_WITH_OUT_OR_EXPECTED_VERSION');
    }
    const report = await qualifySsurgo(area, { expectedVersion });
    const json = JSON.stringify(report, null, 2) + '\n';
    if (out) await writeFile(resolve(out), json, { flag: 'wx', mode: 0o644 }); else process.stdout.write(json);
    if (report.state === 'held') process.exitCode = 2;
  } catch (error) {
    console.error(JSON.stringify({ state: 'held', reason: /^[A-Z][A-Z_]{1,63}$/.test(error.message ?? '') ? error.message : 'SSURGO_QUALIFICATION_FAILED' }));
    process.exitCode = 1;
  }
}
