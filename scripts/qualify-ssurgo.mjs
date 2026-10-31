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
    components: `SELECT c.mukey, COUNT(*) AS components, SUM(c.comppct_r) AS pct, SUM(CASE WHEN c.majcompflag = 'Yes' THEN 1 ELSE 0 END) AS major FROM component c INNER JOIN mapunit mu ON mu.mukey = c.mukey ${inArea} GROUP BY c.mukey ORDER BY c.mukey`,
    polygons: `SELECT mukey, COUNT(*) AS polygons FROM mupolygon WHERE areasymbol = '${area}' GROUP BY mukey ORDER BY mukey`,
    units: `SELECT DISTINCT attributecolumnname, attributename, attributeuomabbrev FROM sdvattribute WHERE attributetablename = 'chorizon' AND attributecolumnname IN (${HORIZON_COLUMNS.map(c => `'${c}'`).join(', ')}) ORDER BY attributecolumnname, attributename`,
  };
}

/** One bounded POST; SDA answers {} for no rows and an XML ServiceException for a failed query. */
async function sda(query, fetcher) {
  const response = await fetcher(SDA_URL, { method: 'POST', headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ query, format: 'JSON+COLUMNNAME' }), signal: AbortSignal.timeout(90_000) });
  const text = await response.text();
  if (!response.ok || text.length > MAX_RESPONSE) fail('SDA_QUERY_FAILED');
  let value;
  try { value = JSON.parse(text); } catch { fail('SDA_QUERY_FAILED'); }
  const [columns, ...rows] = Array.isArray(value?.Table) ? value.Table : [[]];
  if (!Array.isArray(columns) || rows.some(row => !Array.isArray(row) || row.length !== columns.length)) fail('SDA_RESPONSE_INVALID');
  return { rows: rows.map(row => Object.fromEntries(columns.map((name, i) => [name, row[i]]))), responseSha256: sha(text) };
}

const count = value => { const n = Number(value); return Number.isFinite(n) ? n : null; };

export async function qualifySsurgo(area, { fetcher = fetch, now = Date.now } = {}) {
  const text = queries(area);
  const results = {}, receipts = [];
  for (const [name, query] of Object.entries(text)) {
    results[name] = await sda(query, fetcher);
    receipts.push({ name, querySha256: sha(query), responseSha256: results[name].responseSha256, rows: results[name].rows.length });
  }
  const holds = [], findings = [];
  const survey = results.survey.rows;
  if (survey.length !== 1) holds.push('SURVEY_AREA_NOT_FOUND');
  const mapunits = results.mapunits.rows, keys = mapunits.map(m => String(m.mukey));
  if (!mapunits.length) holds.push('NO_MAP_UNITS');
  if (new Set(keys).size !== keys.length) holds.push('MAP_UNIT_KEYS_DUPLICATED');
  const components = new Map(results.components.rows.map(c => [String(c.mukey), c]));
  const withoutComponents = keys.filter(key => !components.has(key));
  // Representative component percentages should account for the whole map unit.
  const notWhole = [...components.values()].filter(c => count(c.pct) !== 100).map(c => ({ mukey: String(c.mukey), pct: count(c.pct) }));
  const noMajor = [...components.values()].filter(c => !(count(c.major) > 0)).map(c => String(c.mukey));
  if (withoutComponents.length) holds.push('MAP_UNITS_WITHOUT_COMPONENTS');
  if (notWhole.length) findings.push({ code: 'COMPONENT_PERCENT_NOT_100', mapUnits: notWhole });
  if (noMajor.length) findings.push({ code: 'NO_MAJOR_COMPONENT', mapUnits: noMajor });
  // Every tabular map unit needs a polygon, and every polygon a tabular map unit.
  const polygons = new Map(results.polygons.rows.map(p => [String(p.mukey), count(p.polygons)]));
  const unmapped = keys.filter(key => !polygons.has(key)), orphaned = [...polygons.keys()].filter(key => !keys.includes(key));
  if (unmapped.length || orphaned.length) holds.push('SPATIAL_TABULAR_MISMATCH');
  // The same column can be published under several attributes with different units
  // (awc_r is cm/cm per horizon and cm as depth-summed storage), so units bind to the attribute.
  const units = HORIZON_COLUMNS.map(column => {
    const rows = results.units.rows.filter(u => u.attributecolumnname === column);
    const published = [...new Set(rows.map(u => u.attributeuomabbrev ?? null))];
    return { column, units: published, attributes: rows.map(u => ({ name: u.attributename, unit: u.attributeuomabbrev ?? null })) };
  });
  const missingUnits = units.filter(u => !u.attributes.length).map(u => u.column);
  if (missingUnits.length) holds.push('HORIZON_UNITS_UNPUBLISHED');
  const ambiguous = units.filter(u => u.units.filter(Boolean).length > 1).map(u => ({ column: u.column, units: u.units }));
  if (ambiguous.length) findings.push({ code: 'UNIT_DEPENDS_ON_ATTRIBUTE', columns: ambiguous });
  return {
    format: 'kfm-ssurgo-qualification-v1', areaSymbol: area, checkedAt: new Date(now()).toISOString(), source: SDA_URL,
    state: holds.length ? 'held' : 'ready-for-owner-review', holds, findings,
    survey: survey[0] ? { name: survey[0].areaname, version: survey[0].saversion, savedAt: survey[0].saverest } : null,
    mapUnits: { count: mapunits.length, acres: mapunits.reduce((sum, m) => sum + (count(m.muacres) ?? 0), 0),
      byKind: Object.fromEntries([...new Set(mapunits.map(m => m.mukind))].map(kind => [kind, mapunits.filter(m => m.mukind === kind).length])),
      largest: [...mapunits].sort((a, b) => (count(b.muacres) ?? 0) - (count(a.muacres) ?? 0)).slice(0, 5).map(m => ({ mukey: String(m.mukey), symbol: m.musym, name: m.muname, acres: count(m.muacres) })) },
    components: { mapUnitsWithComponents: components.size, total: [...components.values()].reduce((sum, c) => sum + (count(c.components) ?? 0), 0) },
    polygons: { count: [...polygons.values()].reduce((sum, n) => sum + (n ?? 0), 0), mapUnits: polygons.size, unmapped, orphaned },
    horizonUnits: units, receipts,
    // Qualification evidence only: rights, sensitivity and admission stay with the owner.
    rights: 'REVIEW_REQUIRED', admitted: false, publication: false,
  };
}

if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  const [area, flag, out] = process.argv.slice(2);
  try {
    if (flag !== undefined && (flag !== '--out' || !out)) fail('USE_AREA_SYMBOL_OR_OUT_FILE');
    const report = await qualifySsurgo(area);
    const json = JSON.stringify(report, null, 2) + '\n';
    if (out) await writeFile(resolve(out), json, { flag: 'wx', mode: 0o644 }); else process.stdout.write(json);
    if (report.state === 'held') process.exitCode = 2;
  } catch (error) {
    console.error(JSON.stringify({ state: 'held', reason: /^[A-Z][A-Z_]{1,63}$/.test(error.message ?? '') ? error.message : 'SSURGO_QUALIFICATION_FAILED' }));
    process.exitCode = 1;
  }
}
