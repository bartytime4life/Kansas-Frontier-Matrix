import test from 'node:test';
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { MAX_NOTE_CHARACTERS, validateInvestigationNotes, saveLocalInvestigation, listLocalInvestigations, getLocalInvestigation, updateLocalInvestigationNotes, exportLocalInvestigations, previewNotebookImport, importNotebook, deleteLocalInvestigation } from '../app/labs/notebook.mjs';
import { currentSourceBindings } from '../app/labs/investigation-state.mjs';
import { NOTEBOOK_STARTERS, starterInvestigationLink, createStarterNotebook } from '../app/labs/starter-investigations.mjs';
import { decodeWorkbenchView, encodeWorkbenchView } from '../app/labs/workbench-view.mjs';
import { PUBLIC_LAB_SNAPSHOTS } from '../app/labs/public-snapshots.mjs';
import { buildCountyModel } from '../app/labs/county-model.mjs';
import { countyHistory, findCountyPeers } from '../app/labs/county-investigations.mjs';
import { analyzeSignals } from '../app/labs/signal-model.mjs';
import { readCountyCSV } from '../app/labs/county-csv.mjs';
const key = 'kfm-science-notebook-v1';
const memory = () => { const map = new Map(); return { getItem: name => map.get(name) ?? null, setItem: (name, value) => map.set(name, value) }; };
const countyInput = { workspace: 'county', title: 'My question', state: { countyA: '20173', countyB: '20091', mapMetric: 'medianIncome' }, sourceBindings: currentSourceBindings('county') };

test('plain-text notes retain Unicode, newlines and literal markup while rejecting invalid or oversized fields', () => {
  const notes = 'Question: Δ population?\nObserved: <script>literal text</script>\nNext check: compare MOEs.';
  assert.equal(validateInvestigationNotes(notes), notes); assert.equal(validateInvestigationNotes(' \n '), '');
  assert.equal(validateInvestigationNotes('x'.repeat(MAX_NOTE_CHARACTERS)).length, MAX_NOTE_CHARACTERS);
  for (const value of [null, 5, {}, [], true, 'x'.repeat(MAX_NOTE_CHARACTERS + 1)]) assert.throws(() => validateInvestigationNotes(value), /plain text/);
});
test('notes survive save, export, preview, import, duplicate handling and semantic reopening', () => {
  const a = memory(), b = memory(), notes = 'Question\nWhat changed?\n\nEvidence\nNot yet recorded.';
  const saved = saveLocalInvestigation({ ...countyInput, notes }, a), text = exportLocalInvestigations(a);
  assert.equal(getLocalInvestigation(saved.id, a).notes, notes);
  assert.equal(previewNotebookImport(text, b).entries[0].notes, notes); assert.equal(b.getItem(key), null);
  assert.equal(importNotebook(text, b).added, 1); assert.equal(getLocalInvestigation(saved.id, b).notes, notes);
  assert.deepEqual(importNotebook(text, b), { added: 0, duplicates: 1, total: 1 });
  const changed = JSON.parse(text); changed.entries[0].notes = 'A different local finding';
  const before = b.getItem(key); assert.throws(() => importNotebook(JSON.stringify(changed), b), /conflicts/); assert.equal(b.getItem(key), before);
});
test('editing notes preserves exact analysis state, source hashes, attachment and creation identity', async () => {
  const storage = memory(), privateData = await readCountyCSV(new File(['FIPS,Local\n20001,0'], 'local.csv'));
  const saved = saveLocalInvestigation({ ...countyInput, privateData, notes: 'First draft' }, storage);
  const updated = updateLocalInvestigationNotes(saved.id, 'Second draft\nSame inputs.', { expectedNotes: 'First draft', storage });
  const { notes, ...rest } = updated; assert.equal(notes, 'Second draft\nSame inputs.');
  const { notes: originalNotes, ...original } = saved; assert.equal(originalNotes, 'First draft'); assert.deepEqual(rest, original);
  assert.deepEqual(listLocalInvestigations(storage), [updated]);
  updateLocalInvestigationNotes(saved.id, '', { expectedNotes: notes, storage }); assert.equal(Object.hasOwn(getLocalInvestigation(saved.id, storage), 'notes'), false);
});
test('stale edits and externally deleted entries cannot overwrite or resurrect saved data', () => {
  const storage = memory(), entry = saveLocalInvestigation({ ...countyInput, notes: 'Original' }, storage);
  updateLocalInvestigationNotes(entry.id, 'Other tab', { expectedNotes: 'Original', storage });
  const afterOther = storage.getItem(key);
  assert.throws(() => updateLocalInvestigationNotes(entry.id, 'Stale draft', { expectedNotes: 'Original', storage }), /another tab/); assert.equal(storage.getItem(key), afterOther);
  deleteLocalInvestigation(entry.id, storage); const afterDeletion = storage.getItem(key);
  assert.throws(() => updateLocalInvestigationNotes(entry.id, 'Retained draft', { expectedNotes: 'Other tab', storage }), /no longer saved/); assert.equal(storage.getItem(key), afterDeletion);
});
test('a removed/reimported identity with changed analysis cannot silently receive notes for its old evidence', () => {
  const storage = memory(), saved = saveLocalInvestigation({ ...countyInput, notes: 'Original reasoning' }, storage);
  const modified = JSON.parse(exportLocalInvestigations(storage)); modified.entries[0].state.countyB = '20001';
  deleteLocalInvestigation(saved.id, storage); importNotebook(JSON.stringify(modified), storage);
  const before = storage.getItem(key);
  assert.throws(() => updateLocalInvestigationNotes(saved.id, 'Reasoning about the original comparison', { expectedNotes: saved.notes, expectedEntry: saved, storage }), /saved investigation changed/);
  assert.equal(storage.getItem(key), before); assert.equal(getLocalInvestigation(saved.id, storage).state.countyB, '20001');
});
test('malformed imports, invalid edits, corrupt storage and quota failures preserve existing notebook bytes', () => {
  const storage = memory(), saved = saveLocalInvestigation(countyInput, storage), before = storage.getItem(key);
  for (const notes of [{ html: 'nested' }, 'x'.repeat(MAX_NOTE_CHARACTERS + 1)]) {
    assert.throws(() => updateLocalInvestigationNotes(saved.id, notes, { storage }));
    const imported = JSON.parse(exportLocalInvestigations(storage)); imported.entries[0].notes = notes;
    assert.throws(() => importNotebook(JSON.stringify(imported), storage)); assert.equal(storage.getItem(key), before);
  }
  assert.throws(() => updateLocalInvestigationNotes('../bad', '', { storage }), /identifier/);
  assert.throws(() => updateLocalInvestigationNotes(saved.id, 'Draft', { storage: { getItem: () => before, setItem: () => { throw new Error('quota'); } } }), /could not save/);
  storage.setItem(key, 'corrupt'); assert.throws(() => updateLocalInvestigationNotes(saved.id, 'Draft', { storage }), /unreadable/); assert.equal(storage.getItem(key), 'corrupt');
});
test('earlier notebook entries without notes remain compatible and public URLs exclude note contents', () => {
  const storage = memory(), saved = saveLocalInvestigation(countyInput, storage); assert.equal(Object.hasOwn(saved, 'notes'), false);
  const withNotes = updateLocalInvestigationNotes(saved.id, 'PRIVATE-DRAFT-DO-NOT-SHARE', { expectedNotes: '', storage });
  const token = encodeWorkbenchView(withNotes), encoded = atob(token.replaceAll('-', '+').replaceAll('_', '/'));
  assert.ok(!encoded.includes('PRIVATE-DRAFT')); assert.ok(!encoded.includes('notes'));
  assert.deepEqual(decodeWorkbenchView(token, { workspace: 'county', sourceBindings: withNotes.sourceBindings }), { state: countyInput.state });
});
test('valid imported identifiers resembling object properties retain independent notes and identities', () => {
  const storage = memory(), document = JSON.parse(createStarterNotebook());
  const ids = ['constructor', 'toString', 'hasOwnProperty'];
  document.entries.forEach((entry, index) => { entry.id = ids[index]; });
  assert.equal(importNotebook(JSON.stringify(document), storage).added, 3);
  for (const id of ids) {
    const original = listLocalInvestigations(storage).find(entry => entry.id === id);
    const updated = updateLocalInvestigationNotes(id, `Reasoning for ${id}`, { expectedEntry: original, expectedNotes: original.notes, storage });
    assert.equal(updated.id, id); assert.equal(getLocalInvestigation(id, storage).notes, `Reasoning for ${id}`);
  }
  assert.deepEqual(new Set(listLocalInvestigations(storage).map(entry => entry.id)), new Set(ids));
});
test('notes-only editing preserves older stored settings without allowing an unsupported workspace restore', () => {
  const storage = memory(), original = saveLocalInvestigation(countyInput, storage);
  const document = JSON.parse(storage.getItem(key)); document.entries[0].state.mapMetric = 'retiredMetric';
  storage.setItem(key, JSON.stringify(document));
  const legacy = listLocalInvestigations(storage)[0];
  assert.throws(() => getLocalInvestigation(original.id, storage), /unsupported|invalid/i);
  const updated = updateLocalInvestigationNotes(original.id, 'Keep the historical reasoning.', { expectedEntry: legacy, expectedNotes: '', storage });
  assert.deepEqual(updated.state, legacy.state); assert.deepEqual(updated.sourceBindings, legacy.sourceBindings);
  assert.equal(listLocalInvestigations(storage)[0].notes, 'Keep the historical reasoning.');
  assert.throws(() => getLocalInvestigation(original.id, storage), /unsupported|invalid/i);
});
test('notes respect the combined 512 KB notebook cap and a rejected edit preserves the last saved bytes', async () => {
  const headers = ['FIPS', ...Array.from({ length: 12 }, (_, index) => `m${index}` + 'x'.repeat(97))];
  const lines = Array.from({ length: 105 }, (_, index) => [`20${String(index * 2 + 1).padStart(3, '0')}`, ...Array(12).fill(-1e12)].join(','));
  const privateData = await readCountyCSV(new File([[headers.join(','), ...lines].join('\n')], 'full-local.csv'));
  const storage = memory(), entries = Array.from({ length: 12 }, () => saveLocalInvestigation({ ...countyInput, privateData }, storage));
  let capacityHeld = false;
  for (const entry of entries) {
    const before = storage.getItem(key);
    try { updateLocalInvestigationNotes(entry.id, '界'.repeat(MAX_NOTE_CHARACTERS), { expectedNotes: '', storage }); }
    catch (error) { assert.match(error.message, /512 KB/); assert.equal(storage.getItem(key), before); capacityHeld = true; break; }
  }
  assert.equal(capacityHeld, true); assert.ok(new TextEncoder().encode(storage.getItem(key)).length <= 512 * 1024);
});
test('all starter links decode to validated public controls with exact current fingerprints', () => {
  assert.equal(NOTEBOOK_STARTERS.length, 3); assert.equal(new Set(NOTEBOOK_STARTERS.map(starter => starter.id)).size, 3);
  for (const starter of NOTEBOOK_STARTERS) {
    const url = new URL(starterInvestigationLink(starter.id), 'https://kansasfrontiermatrix.com');
    assert.equal(url.pathname, starter.workspace === 'county' ? '/labs/observatory' : '/labs/signals');
    assert.deepEqual(decodeWorkbenchView(url.searchParams.get('view'), { workspace: starter.workspace, sourceBindings: currentSourceBindings(starter.workspace) }), { state: starter.state });
    assert.deepEqual([...url.searchParams.keys()], ['view']); assert.ok(!url.href.includes('csv_')); assert.ok(starter.question && starter.coverage && starter.method);
  }
  assert.throws(() => starterInvestigationLink('made-up'));
});
test('starter download is an importable optional notebook with fresh identities and editable prompts, never preset findings', () => {
  const storage = memory(), first = createStarterNotebook(), second = createStarterNotebook();
  const preview = previewNotebookImport(first, storage); assert.equal(preview.additions, 3); assert.equal(preview.privateAttachments, 0); assert.equal(storage.getItem(key), null);
  const firstDoc = JSON.parse(first), secondDoc = JSON.parse(second); assert.equal(firstDoc.format, key);
  assert.ok(firstDoc.entries.every((entry, index) => entry.id !== secondDoc.entries[index].id));
  for (const entry of firstDoc.entries) { assert.ok(!entry.privateData); assert.match(entry.notes, /Evidence I observed\n\nAlternative explanations\n\nNext check/); assert.ok(entry.notes.length < MAX_NOTE_CHARACTERS); }
  assert.equal(importNotebook(first, storage).added, 3); assert.equal(listLocalInvestigations(storage).length, 3);
  assert.equal(importNotebook(first, storage).duplicates, 3);
});
test('starter questions resolve actual source periods, county histories, peer cohort and consecutive energy pairs', async () => {
  const bundles = Object.fromEntries(await Promise.all(Object.entries(PUBLIC_LAB_SNAPSHOTS).map(async ([id, snapshot]) => [id, JSON.parse(await readFile(new URL('../public' + snapshot.path, import.meta.url)))])));
  const model = buildCountyModel(bundles, { snapshots: PUBLIC_LAB_SNAPSHOTS });
  const change = NOTEBOOK_STARTERS.find(starter => starter.id === 'county-change').state;
  const history = countyHistory(model, { fipsA: change.countyA, fipsB: change.countyB, metric: change.historyMetric });
  assert.equal(history.counties.a.name, 'Finney County'); assert.equal(history.counties.b.name, 'Riley County');
  assert.equal(history.population.length, 6); assert.equal(history.conditions.length, 3); assert.ok(history.conditions.every(row => row.valueA !== null && row.moeA !== null && row.valueB !== null && row.moeB !== null));
  const peerState = NOTEBOOK_STARTERS.find(starter => starter.id === 'comparison-county').state;
  const peers = findCountyPeers(model, { fips: peerState.countyA, keys: peerState.peerKeys.split(',') }); assert.equal(peers.cohortCount, 105); assert.equal(peers.reason, null);
  const energy = analyzeSignals(bundles, NOTEBOOK_STARTERS.find(starter => starter.id === 'energy-changes').state);
  assert.equal(energy.pairs.length, 34); assert.equal(energy.bounds.from, 1990); assert.equal(energy.bounds.to, 2024); assert.equal(energy.x.spec.series, 'SEDS.WYPRB.KS.A'); assert.equal(energy.y.spec.series, 'SEDS.CLTCB.KS.A');
  assert.ok(energy.pairs.every(row => row.xYear === row.yYear && row.xYear >= 1991));
});
