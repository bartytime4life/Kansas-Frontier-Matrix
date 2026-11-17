import { validKansasFips } from './county-csv.mjs';
const KEY = 'kfm-science-notebook-v1', MAX_BYTES = 512 * 1024;
const forbidden = new Set(['__proto__', 'constructor', 'prototype']);
const plain = value => value !== null && typeof value === 'object' && !Array.isArray(value) && (Object.getPrototypeOf(value) === Object.prototype || Object.getPrototypeOf(value) === null);
export function validateWorkbenchState(state) {
  if (!plain(state) || Object.keys(state).length > 40 || JSON.stringify(state).length > 5000) throw new Error('Invalid investigation settings.');
  for (const [key, value] of Object.entries(state)) {
    if (!/^[a-zA-Z][\w-]{0,49}$/.test(key) || forbidden.has(key) || !(value === null || typeof value === 'boolean' || (typeof value === 'number' && Number.isFinite(value) && Math.abs(value) <= 1e12) || (typeof value === 'string' && value.length <= 300))) throw new Error('Invalid investigation settings.');
  }
  return { ...state };
}
export function validateSourceBindings(bindings) {
  if (!plain(bindings) || Object.keys(bindings).length > 20 || !Object.keys(bindings).length || Object.entries(bindings).some(([key, value]) => !/^[a-z][a-z0-9-]{0,70}$/.test(key) || forbidden.has(key) || !/^[a-f0-9]{64}$/.test(value))) throw new Error('Invalid source fingerprints.');
  return { ...bindings };
}
export function sourceBindingsMatch(expected, current) {
  try { const a = validateSourceBindings(expected), b = validateSourceBindings(current); return Object.keys(a).length === Object.keys(b).length && Object.entries(a).every(([key, value]) => b[key] === value); } catch { return false; }
}
function validatePrivate(data) {
  if (!plain(data) || !Array.isArray(data.rows) || !data.rows.length || data.rows.length > 105 || !Array.isArray(data.columns) || !data.columns.length || data.columns.length > 12 || !/^[a-f0-9]{64}$/.test(data.sha256) || !Number.isInteger(data.bytes) || data.bytes < 1 || data.bytes > MAX_BYTES || typeof data.fileName !== 'string' || data.fileName.length > 120) throw new Error('Invalid private county data.');
  const columns = data.columns.map((column, index) => {
    if (!plain(column) || column.key !== `csv_${index}` || typeof column.label !== 'string' || !column.label.trim() || column.label.length > 100 || column.type !== 'number' || column.unit !== null) throw new Error('Invalid private county columns.');
    return { key: column.key, label: column.label, type: 'number', unit: null };
  });
  const seen = new Set(); let missingValues = 0;
  const rows = data.rows.map(input => {
    if (!plain(input) || !validKansasFips(input.fips) || seen.has(input.fips) || Object.keys(input).length !== columns.length + 1) throw new Error('Invalid private county rows.');
    seen.add(input.fips); const row = { fips: input.fips };
    for (const column of columns) { const value = input[column.key]; if (!(value === null || (typeof value === 'number' && Number.isFinite(value) && Math.abs(value) <= 1e12))) throw new Error('Invalid private county value.'); if (value === null) missingValues++; row[column.key] = value; }
    return row;
  });
  return { rows, columns, diagnostics: { rows: rows.length, missingValues, unmatched: [] }, sha256: data.sha256, bytes: data.bytes, fileName: data.fileName };
}
function validateEntry(input) {
  if (!plain(input) || !['county', 'signal'].includes(input.workspace) || typeof input.title !== 'string' || !input.title.trim() || input.title.length > 120 || typeof input.id !== 'string' || !/^[a-zA-Z0-9-]{1,80}$/.test(input.id) || typeof input.createdAt !== 'string' || !Number.isFinite(Date.parse(input.createdAt))) throw new Error('Invalid saved investigation.');
  return { id: input.id, workspace: input.workspace, title: input.title.trim(), createdAt: input.createdAt, state: validateWorkbenchState(input.state), sourceBindings: validateSourceBindings(input.sourceBindings), ...(input.privateData ? { privateData: validatePrivate(input.privateData) } : {}) };
}
const getStorage = storage => { const target = storage ?? globalThis.localStorage; if (!target) throw new Error('Browser storage is unavailable. Download an analysis receipt instead.'); return target; };
export function listLocalInvestigations(storage) {
  const raw = getStorage(storage).getItem(KEY);
  if (!raw) return [];
  try { if (new TextEncoder().encode(raw).length > MAX_BYTES) return []; const doc = JSON.parse(raw); if (doc.format !== KEY || !Array.isArray(doc.entries) || doc.entries.length > 12) return []; return doc.entries.map(validateEntry); } catch { return []; }
}
function write(entries, storage) {
  const text = JSON.stringify({ format: KEY, entries });
  if (new TextEncoder().encode(text).length > MAX_BYTES) throw new Error('This notebook exceeds 512 KB. Download it and remove an older investigation first.');
  try { getStorage(storage).setItem(KEY, text); } catch { throw new Error('This browser could not save the notebook. Download an analysis receipt instead.'); }
}
export function saveLocalInvestigation(input, storage) {
  const entries = listLocalInvestigations(storage);
  if (entries.length >= 12) throw new Error('Your notebook has 12 investigations. Download it or remove an older entry first.');
  const entry = validateEntry({ ...input, id: globalThis.crypto.randomUUID(), createdAt: new Date().toISOString() });
  write([entry, ...entries], storage); return entry;
}
export function deleteLocalInvestigation(id, storage) { write(listLocalInvestigations(storage).filter(entry => entry.id !== id), storage); }
export function exportLocalInvestigations(storage) { return JSON.stringify({ format: KEY, exportedAt: new Date().toISOString(), entries: listLocalInvestigations(storage) }, null, 2); }
