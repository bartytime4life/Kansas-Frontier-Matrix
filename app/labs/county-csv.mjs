export const COUNTY_CSV_MAX_BYTES = 512 * 1024;
const missing = /^(?:|NA|N\/A|null|\.)$/i;
export const validKansasFips = value => /^20\d{3}$/.test(value) && Number(value.slice(2)) >= 1 && Number(value.slice(2)) <= 209 && Number(value.slice(2)) % 2 === 1;

function csvRows(text) {
  const rows = []; let row = [], cell = '', quoted = false, closed = false;
  for (let index = 0; index < text.length; index++) {
    const char = text[index];
    if (quoted) {
      if (char === '"' && text[index + 1] === '"') { cell += '"'; index++; }
      else if (char === '"') { quoted = false; closed = true; }
      else cell += char;
    } else if (char === '"') {
      if (cell || closed) throw new Error('A CSV quote must begin a field.');
      quoted = true;
    } else if (char === ',' || char === '\n' || char === '\r') {
      row.push(cell); cell = ''; closed = false;
      if (char !== ',') { rows.push(row); row = []; if (char === '\r' && text[index + 1] === '\n') index++; }
    } else {
      if (closed) throw new Error('Unexpected text after a quoted CSV field.');
      cell += char;
    }
  }
  if (quoted) throw new Error('The CSV has an unclosed quoted field.');
  if (cell || row.length || closed) { row.push(cell); rows.push(row); }
  return rows.filter(row => row.some(value => value.trim()));
}

export function parseCountyCSV(text) {
  if (typeof text !== 'string' || new TextEncoder().encode(text).length > COUNTY_CSV_MAX_BYTES) throw new Error('Choose a CSV no larger than 512 KB.');
  const table = csvRows(text.replace(/^\uFEFF/, ''));
  if (table.length < 2) throw new Error('Include a header and at least one county row.');
  const headers = table.shift().map(value => value.trim());
  if (headers.length < 2 || headers.length > 13 || headers.some(value => !value || value.length > 100 || /[\u0000-\u001f]/.test(value)) || new Set(headers.map(value => value.toLowerCase())).size !== headers.length) throw new Error('Use a FIPS header and 1–12 uniquely named numeric columns.');
  const fipsIndexes = headers.flatMap((value, index) => /^(?:fips|county[ _-]?fips|geoid)$/i.test(value) ? [index] : []);
  if (fipsIndexes.length !== 1) throw new Error('Include exactly one FIPS, CountyFIPS or GEOID column with five-digit Kansas county codes.');
  const fipsIndex = fipsIndexes[0], indexes = headers.flatMap((_, index) => index !== fipsIndex ? [index] : []);
  const columns = indexes.map((index, order) => ({ key: `csv_${order}`, label: headers[index], type: 'number', unit: null }));
  const seen = new Set(); let missingValues = 0;
  const rows = table.map((values, rowIndex) => {
    if (values.length !== headers.length) throw new Error(`Row ${rowIndex + 2} has a different number of fields from the header.`);
    const fips = values[fipsIndex].trim();
    if (!validKansasFips(fips)) throw new Error(`Row ${rowIndex + 2} needs a valid five-digit Kansas county FIPS code.`);
    if (seen.has(fips)) throw new Error(`County ${fips} appears more than once. Use one row per county.`);
    seen.add(fips);
    const row = { fips };
    indexes.forEach((index, order) => {
      const value = values[index].trim();
      if (missing.test(value)) { row[`csv_${order}`] = null; missingValues++; return; }
      if (!/^[+-]?(?:\d+\.?\d*|\.\d+)(?:e[+-]?\d+)?$/i.test(value) || !Number.isFinite(Number(value)) || Math.abs(Number(value)) > 1e12) throw new Error(`Row ${rowIndex + 2}, ${headers[index]} must contain a finite number or a blank.`);
      row[`csv_${order}`] = Number(value);
    });
    return row;
  });
  if (rows.length > 105) throw new Error('Use at most 105 unique Kansas county rows.');
  return { rows, columns, diagnostics: { rows: rows.length, missingValues, unmatched: [] } };
}

export async function readCountyCSV(file) {
  if (!file || file.size > COUNTY_CSV_MAX_BYTES) throw new Error('Choose a CSV no larger than 512 KB.');
  const buffer = await file.arrayBuffer();
  if (buffer.byteLength > COUNTY_CSV_MAX_BYTES) throw new Error('Choose a CSV no larger than 512 KB.');
  const parsed = parseCountyCSV(new TextDecoder('utf-8', { fatal: true }).decode(buffer));
  const hash = await globalThis.crypto.subtle.digest('SHA-256', buffer);
  return { ...parsed, sha256: Array.from(new Uint8Array(hash), value => value.toString(16).padStart(2, '0')).join(''), fileName: String(file.name || 'county-data.csv').slice(0, 120), bytes: buffer.byteLength };
}
