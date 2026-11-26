// Public projection contains only USDA's final regional country-elevator cash bids.
import { fail } from './pipeline-contract.mjs';

export const GRAIN_SOURCE = 'usda-kansas-grain-bids';
export const GRAIN_URL = 'https://www.ams.usda.gov/mnreports/ams_2886.pdf';
const crops = new Map([
  ['US #2 Yellow Corn (Bulk)', 'Corn'], ['US #2 Sorghum (Bulk)', 'Sorghum'],
  ['US #1 Soybeans (Bulk)', 'Soybeans'], ['US #1 Hard Red Winter Wheat (Bulk)', 'Hard red winter wheat'],
]);
const regions = /^(Northwest|North|Northeast|West|Central|East|Southwest|South|Southeast)$/;
const exact = (v, keys) => v && typeof v === 'object' && Object.keys(v).sort().join() === keys.split(' ').sort().join();
const price = v => typeof v === 'number' && Number.isFinite(v) && v > 0 && v < 1000;
export function validateGrain(p) {
  if (!exact(p,'format sourceId sourceUrl captureSha256 reportDate retrievedAt unit rows') ||
      p.format !== 'kfm-kansas-grain-bids-v1' || p.sourceId !== GRAIN_SOURCE || p.sourceUrl !== GRAIN_URL ||
      !/^[a-f0-9]{64}$/.test(p.captureSha256) || p.unit !== 'USD/bu' ||
      !/^\d{4}-\d\d-\d\d$/.test(p.reportDate) || !Number.isFinite(Date.parse(p.reportDate)) ||
      new Date(p.reportDate).toISOString().slice(0,10) !== p.reportDate ||
      typeof p.retrievedAt !== 'string' || !Number.isFinite(Date.parse(p.retrievedAt)) ||
      new Date(p.retrievedAt).toISOString() !== p.retrievedAt || p.reportDate > p.retrievedAt.slice(0,10) ||
      !Array.isArray(p.rows) || !p.rows.length || p.rows.length > 36) fail('GRAIN_REPORT_INVALID');
  const seen = new Set();
  for (const row of p.rows) {
    const key = row?.crop + '/' + row?.region;
    if (!exact(row,'crop region low high average') || ![...crops.values()].includes(row.crop) ||
        typeof row.region !== 'string' || !regions.test(row.region) || ![row.low,row.average,row.high].every(price) ||
        row.low > row.average || row.average > row.high || seen.has(key)) fail('GRAIN_ROW_INVALID');
    seen.add(key);
  }
  return p;
}

export function parseGrainReport(text, captureSha256, retrievedAt) {
  const date = /^Grain Report for (\d\d)\/(\d\d)\/(\d{4}) - Final\s*$/mi.exec(text);
  if (!date || !/^\s*Kansas Daily Grain Bids\s*$/m.test(text) ||
      !text.includes('mymarketnews.ams.usda.gov/viewReport/2886')) fail('GRAIN_REPORT_IDENTITY');
  const rows = [];
  let crop = null, country = false, cashHeader = false;
  for (const raw of text.split(/\r?\n/)) {
    const line = raw.trim();
    if (/\(Bulk\)$/.test(line) || /^US #/.test(line)) {
      crop = crops.get(line) ?? null; country = false; cashHeader = false;
    } else if (/ - (Conventional|Organic)$/.test(line)) {
      country = line === 'Country Elevators - Conventional'; cashHeader = false;
    } else if (line.startsWith('Region/Location')) {
      cashHeader = /Price\(\$\/Bu\).*Price Change.*Average.*Freight.*Delivery/.test(line);
    } else if (country && crop && /\bBid\b/.test(line)) {
      // Only current delivered-truck bids; other delivery periods and protein grades have different meanings.
      if (!/DLVD-T\s+Current$/.test(line)) continue;
      if (crop === 'Hard red winter wheat' && !/\bBid\s+Ordinary\b/.test(line)) continue;
      const region = line.split(/\s+/)[0];
      const fields = /(?:^|\s)(\d+\.\d{4})(?:-(\d+\.\d{4}))?\s+(?:UNCH|(?:UP|DN)\s+\d+\.\d{4}(?:-(?:(?:UP|DN)\s+\d+\.\d{4}|UNCH))?|UNCH-(?:UP|DN)\s+\d+\.\d{4})\s+(\d+\.\d{4})(?:\s+\d+\.\d{4})?\s+DLVD-T\s+Current$/.exec(line);
      if (!cashHeader || !regions.test(region) || !fields) fail('GRAIN_LAYOUT_CHANGED');
      rows.push({ crop, region, low:Number(fields[1]), high:Number(fields[2] ?? fields[1]), average:Number(fields[3]) });
    }
  }
  return validateGrain({ format:'kfm-kansas-grain-bids-v1', sourceId:GRAIN_SOURCE, sourceUrl:GRAIN_URL,
    reportDate:date[3]+'-'+date[1]+'-'+date[2], captureSha256, retrievedAt, unit:'USD/bu', rows });
}
