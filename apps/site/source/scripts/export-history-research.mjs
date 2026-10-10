import { readFile, writeFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';
import { resolve } from 'node:path';

const fields = ['id', 'sourceId', 'kind', 'title', 'category', 'date', 'place', 'relation', 'sourceUrl', 'targetUrl', 'reviewNote', 'themes'];

// Quote CSV syntax and neutralize formulas before a spreadsheet interprets them.
export function historyCsvCell(value) {
  let text = value == null ? '' : Array.isArray(value) ? value.join('; ') : String(value);
  if (/^[\s\u0000-\u001f]*[=+@-]/u.test(text) || /^[\t\r\n]/u.test(text)) text = `'${text}`;
  return `"${text.replaceAll('"', '""')}"`;
}

export function historyResearchCsv(records) {
  return [fields.map(historyCsvCell).join(','), ...records.map(record => fields.map(field => historyCsvCell(record[field])).join(','))].join('\r\n') + '\r\n';
}

if (process.argv[1] && resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  const root = new URL('../public/history/', import.meta.url);
  const catalog = JSON.parse(await readFile(new URL('people-events.json', root), 'utf8'));
  await writeFile(new URL('people-events.csv', root), historyResearchCsv(catalog.records), 'utf8');
  console.log(`Exported ${catalog.records.length} research references.`);
}
