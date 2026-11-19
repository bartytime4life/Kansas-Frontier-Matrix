import { validKansasFips } from './county-csv.mjs';
import { validateInvestigationState } from './investigation-state.mjs';
const KEY = 'kfm-science-notebook-v1', MAX_BYTES = 512 * 1024;
export const MAX_NOTE_CHARACTERS = 4000;
const forbidden = new Set(['__proto__', 'constructor', 'prototype']);
const plain = value => value !== null && typeof value === 'object' && !Array.isArray(value) && (Object.getPrototypeOf(value) === Object.prototype || Object.getPrototypeOf(value) === null);
export function validateInvestigationNotes(value) {
  if (typeof value !== 'string' || value.length > MAX_NOTE_CHARACTERS) throw new Error('Research notes must be plain text of 4,000 characters or fewer.');
  return value.trim() ? value : '';
}
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
  const notes = input.notes === undefined ? '' : validateInvestigationNotes(input.notes);
  return { id: input.id, workspace: input.workspace, title: input.title.trim(), createdAt: input.createdAt, state: validateWorkbenchState(input.state), sourceBindings: validateSourceBindings(input.sourceBindings), ...(input.privateData ? { privateData: validatePrivate(input.privateData) } : {}), ...(notes ? { notes } : {}) };
}
const getStorage = storage => { const target = storage ?? globalThis.localStorage; if (!target) throw new Error('Browser storage is unavailable. Download an analysis receipt instead.'); return target; };
export function listLocalInvestigations(storage) {
  return readStrict(storage);
}
function write(entries, storage) {
  const text = JSON.stringify({ format: KEY, entries });
  if (new TextEncoder().encode(text).length > MAX_BYTES) throw new Error('This notebook exceeds 512 KB. Download it and remove an older investigation first.');
  try { getStorage(storage).setItem(KEY, text); } catch { throw new Error('This browser could not save the notebook. Download an analysis receipt instead.'); }
}
export function saveLocalInvestigation(input, storage) {
  const entries = readStrict(storage);
  if (entries.length >= 12) throw new Error('Your notebook has 12 investigations. Download it or remove an older entry first.');
  const entry = validateEntry({ ...input, id: globalThis.crypto.randomUUID(), createdAt: new Date().toISOString() });
  write([entry, ...entries], storage); return entry;
}
export function deleteLocalInvestigation(id, storage) { write(readStrict(storage).filter(entry => entry.id !== id), storage); }
export function exportLocalInvestigations(storage) { return JSON.stringify({ format: KEY, exportedAt: new Date().toISOString(), entries: readStrict(storage) }, null, 2); }

// Update only the reasoning attached to an entry, retaining its analytical snapshot.
export function updateLocalInvestigationNotes(id, notes, { expectedNotes, expectedEntry, storage } = {}) {
  if (typeof id !== 'string' || !/^[a-zA-Z0-9-]{1,80}$/.test(id)) throw new Error('Invalid investigation identifier.');
  const normalized = validateInvestigationNotes(notes), entries = readStrict(storage);
  const index = entries.findIndex(entry => entry.id === id);
  if (index === -1) throw new Error('That investigation is no longer saved in this browser. Your draft has not been saved.');
  if (expectedEntry !== undefined) {
    const expected = validateEntry(expectedEntry);
    if (expected.id !== id || canonical(expected) !== canonical(entries[index])) throw new Error('This saved investigation changed in another tab. Your draft has been kept; reload and review the saved record before editing again.');
  }
  if (expectedNotes !== undefined && validateInvestigationNotes(expectedNotes) !== (entries[index].notes || '')) throw new Error('These notes changed in another tab. Your draft has been kept; reload the saved notes before editing again.');
  const updated = { ...entries[index] };
  if (normalized) updated.notes = normalized; else delete updated.notes;
  entries[index] = updated;
  try { write(entries, storage); }
  catch (error) {
    if (error.message.includes('512 KB')) throw error;
    throw new Error('This browser could not save these notes. Copy your draft before leaving or retry when storage is available.');
  }
  return updated;
}

// Imports and reopening validate supported controls as well as the storage shape.
export function validateInvestigation(input) {
  const entry = validateEntry(input);
  entry.state = validateInvestigationState(entry.workspace, entry.state, { privateData: entry.privateData });
  return entry;
}
function readStrict(storage) {
  const raw = getStorage(storage).getItem(KEY);
  if (!raw) return [];
  try {
    if (new TextEncoder().encode(raw).length > MAX_BYTES) throw new Error();
    const doc = JSON.parse(raw);
    if (!plain(doc) || doc.format !== KEY || !Array.isArray(doc.entries) || doc.entries.length > 12) throw new Error();
    const entries = doc.entries.map(validateEntry);
    if (new Set(entries.map(entry => entry.id)).size !== entries.length) throw new Error();
    return entries;
  } catch { throw new Error('The existing browser notebook is unreadable and has not been changed. Keep its browser data; use an existing backup or recover the stored notebook before continuing.'); }
}
export function getLocalInvestigation(id, storage) {
  if (typeof id !== 'string' || !/^[a-zA-Z0-9-]{1,80}$/.test(id)) throw new Error('Invalid investigation identifier.');
  const entry = readStrict(storage).find(item => item.id === id);
  return entry ? validateInvestigation(entry) : null;
}
const canonical = value => JSON.stringify(value, function (_key, item) { return plain(item) ? Object.fromEntries(Object.keys(item).sort().map(key => [key, item[key]])) : item; });
function prepareImport(text, storage) {
  if (typeof text !== 'string' || new TextEncoder().encode(text).length > 2 * 1024 * 1024) throw new Error('Choose a notebook JSON file no larger than 2 MB.');
  let doc;
  try { doc = JSON.parse(text); } catch { throw new Error('This file is not valid notebook JSON.'); }
  if (!plain(doc) || doc.format !== KEY || !Array.isArray(doc.entries) || !doc.entries.length || doc.entries.length > 12) throw new Error('Choose a kfm-science-notebook-v1 export containing 1–12 investigations.');
  const entries = doc.entries.map(validateInvestigation), existing = readStrict(storage), byId = new Map(existing.map(entry => [entry.id, entry]));
  const incoming = new Set(), additions = []; let duplicates = 0;
  for (const entry of entries) {
    if (incoming.has(entry.id)) throw new Error('The import contains repeated investigation identifiers.');
    incoming.add(entry.id);
    if (byId.has(entry.id)) {
      if (canonical(entry) !== canonical(byId.get(entry.id))) throw new Error(`Investigation ${entry.id} conflicts with a saved entry. Nothing was imported.`);
      duplicates++;
    } else additions.push(entry);
  }
  const merged = [...additions, ...existing];
  if (merged.length > 12) throw new Error('This merge would exceed 12 investigations. Export and remove an older entry first.');
  if (new TextEncoder().encode(JSON.stringify({ format: KEY, entries: merged })).length > MAX_BYTES) throw new Error('This merge would exceed the 512 KB browser notebook limit. Nothing was imported.');
  return { entries, merged, additions: additions.length, duplicates, privateAttachments: entries.filter(entry => entry.privateData).length };
}
export function previewNotebookImport(text, storage) {
  const { entries, additions, duplicates, privateAttachments } = prepareImport(text, storage);
  return { entries, additions, duplicates, privateAttachments };
}
export function importNotebook(text, storage) {
  const prepared = prepareImport(text, storage);
  if (prepared.additions) write(prepared.merged, storage);
  return { added: prepared.additions, duplicates: prepared.duplicates, total: prepared.merged.length };
}
