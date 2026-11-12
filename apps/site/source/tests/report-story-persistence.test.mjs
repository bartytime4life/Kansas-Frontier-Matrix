import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";
import { componentHarness, findNode, settle } from "./component-harness.mjs";

// Load the actual model and strict storage validators, rather than accepting test-only drafts.
const urls = new Map();
async function moduleUrl(name) {
  if (urls.has(name)) return urls.get(name);
  let js = ts.transpileModule(await readFile(new URL(`../app/${name}.ts`, import.meta.url), "utf8"), {
    compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
  }).outputText;
  js = js.replaceAll('from "sunrise-sunset-js"', `from ${JSON.stringify(import.meta.resolve("sunrise-sunset-js"))}`)
    .replaceAll('from "polygon-clipping"', `from ${JSON.stringify(new URL("../node_modules/polygon-clipping/dist/polygon-clipping.esm.js", import.meta.url).href)}`);
  for (const [, dependency] of [...js.matchAll(/from "\.\/([a-z-]+)"/g)]) js = js.replaceAll(`from "./${dependency}"`, `from "${await moduleUrl(dependency)}"`);
  const url = `data:text/javascript;base64,${Buffer.from(js).toString("base64")}`;
  urls.set(name, url);
  return url;
}
const model = await import(await moduleUrl("workspace-model"));
const storage = await import(await moduleUrl("workspace-storage"));
const imports = {
  "./workspace-model": model, "./workspace-storage": storage, "./snapshot-map": { default: "snapshot-map" },
  "./fire-report-analysis": await import(await moduleUrl("fire-report-analysis")),
  "./subsurface-model": await import(await moduleUrl("subsurface-model")),
  "./research-context": await import(await moduleUrl("research-context")),
};
const snapshot = id => ({
  id, createdAt: "2026-11-09T12:00:00Z", area: { kind: "viewport", label: `Synthetic Kansas ${id}` },
  camera: { center: [-98.38, 38.48], zoom: 5.4, pitch: 0, bearing: 0 }, representation: "2D", projection: "mercator", basemap: "standard",
  committedTime: { start: 2026, end: 2026, label: "2026", mode: "instant" },
  visibleLayers: [], selection: null, evidenceRefs: [], inspectableFeatureIds: [],
  inspectableRecordCount: 0, sourceBackedCount: 0, boundedCount: 0, policy: model.policyDecisionFromEvidenceState("MISSING_EVIDENCE"),
});
const reportDraft = id => ({ ...model.createReportDraft(snapshot(id), []), title: `Report ${id}`, sections: { ...model.createReportDraft(snapshot(id), []).sections, summary: `Unique report prose ${id}` } });
const storyDraft = id => ({ ...model.createTrustStory(snapshot(id), []), title: `Story ${id}`, scenes: [{ ...model.createTrustStory(snapshot(id), []).scenes[0], narrative: `Unique story prose ${id}` }] });
function browser(initial = {}) {
  const values = new Map(Object.entries(initial)), writes = [], timers = new Map(), listeners = new Set(), events = new Map(), downloads = [];
  let serial = 0, denied = false;
  const window = {
    localStorage: { getItem: key => values.get(key) ?? null, setItem(key, raw) { if (denied) throw new Error("storage denied"); writes.push(key); values.set(key, raw); } },
    setTimeout(fn, delay = 0) { timers.set(++serial, { fn, delay }); return serial; }, clearTimeout(id) { timers.delete(id); },
    matchMedia: () => ({ matches: false, addEventListener(_type, fn) { listeners.add(fn); }, removeEventListener(_type, fn) { listeners.delete(fn); } }),
  };
  const document = {
    hidden: false,
    addEventListener(type, fn) { listeners.add(fn); if (!events.has(type)) events.set(type, new Set()); events.get(type).add(fn); }, removeEventListener(type, fn) { listeners.delete(fn); events.get(type)?.delete(fn); },
    body: { append() {} }, createElement() { return { click() {}, remove() {} }; },
  };
  return { window, document, values, writes, timers, listeners, downloads,
    URL: { createObjectURL(blob) { downloads.push(blob); return `blob:synthetic-${downloads.length}`; }, revokeObjectURL() {} },
    deny() { denied = true; }, flush() { for (const [id, entry] of [...timers]) { timers.delete(id); entry.fn(); } },
    dispatch(type) { for (const callback of events.get(type) ?? []) callback({ type }); },
  };
}
async function mount(b, initialProps) {
  globalThis.window = b.window;
  const harness = await componentHarness(new URL("../app/report-story-workspaces.tsx", import.meta.url), imports, { window: b.window, document: b.document, URL: b.URL, Blob, queueMicrotask });
  let props = { evidenceRecords: [], onReturnToMap() {}, onInspectEvidence() {}, onApplyScene() {}, getCurrentSnapshot: () => snapshot("current-map"), ...initialProps };
  props.onModeChange = mode => { props = { ...props, mode }; };
  let tree;
  const draw = () => { tree = harness.render(harness.exports.default, props); harness.commit(); return tree; };
  draw();
  return {
    draw, get tree() { return tree; }, changeProps(patch) { props = { ...props, ...patch }; return draw(); },
    switch(mode) { findNode(tree, n => n.type === "button" && n.props.children === (mode === "reports" ? "Reports" : "Stories")).props.onClick(); draw(); },
    edit(label, value) {
      const field = findNode(tree, n => n.type === "label" && [n.props.children].flat().some(child => child?.type === "span" && child.props.children === label));
      assert.ok(field, `actual ${label} field exists`);
      findNode(field, n => n.type === "input" || n.type === "textarea").props.onChange({ target: { value } }); draw();
    },
    dispose() { harness.dispose(); },
  };
}

test("Reports A to Stories B preserves independent saved prose, snapshots, edits and exported story", async () => {
  const report = reportDraft("A"), story = storyDraft("B");
  const rawStory = JSON.stringify(story);
  const b = browser({ [storage.REPORT_STORAGE_KEY]: JSON.stringify(report), [storage.STORY_STORAGE_KEY]: rawStory });
  const h = await mount(b, { mode: "reports", snapshot: snapshot("A") });
  try {
    assert.equal(b.values.get(storage.STORY_STORAGE_KEY), rawStory, "opening Reports must not write the inactive story");
    h.edit("Report title", "Report A edited");
    h.switch("stories");
    assert.equal(storage.readDraft(storage.STORY_STORAGE_KEY).scenes[0].narrative, "Unique story prose B");
    assert.equal(storage.readDraft(storage.STORY_STORAGE_KEY).baseSnapshot.id, "B");
    h.edit("Narrative", "Unique story prose B edited");
    findNode(h.tree, n => n.type === "button" && n.props.children === "Export story JSON").props.onClick();
    const exported = JSON.parse(await b.downloads[0].text());
    assert.equal(exported.scenes[0].narrative, "Unique story prose B edited");
    assert.equal(exported.baseSnapshot.id, "B");
    assert.equal(exported.authority, "DRAFT_NOT_PUBLISHED");
    h.switch("reports");
    assert.equal(storage.readDraft(storage.REPORT_STORAGE_KEY).title, "Report A edited");
    assert.equal(storage.readDraft(storage.REPORT_STORAGE_KEY).snapshot.id, "A");
    assert.equal(storage.readDraft(storage.STORY_STORAGE_KEY).scenes[0].narrative, "Unique story prose B edited");
  } finally { h.dispose(); delete globalThis.window; }
});

test("Stories B to Reports A also resumes independent drafts and survives remount", async () => {
  const b = browser({ [storage.REPORT_STORAGE_KEY]: JSON.stringify(reportDraft("A")), [storage.STORY_STORAGE_KEY]: JSON.stringify(storyDraft("B")) });
  let h = await mount(b, { mode: "stories", snapshot: snapshot("B") });
  try {
    h.edit("Narrative", "Only copy of a revised B story");
    h.switch("reports");
    assert.equal(storage.readDraft(storage.REPORT_STORAGE_KEY).sections.summary, "Unique report prose A");
    h.dispose();
    h = await mount(b, { mode: "stories", snapshot: snapshot("unrelated-current-map") });
    assert.equal(storage.readDraft(storage.STORY_STORAGE_KEY).scenes[0].narrative, "Only copy of a revised B story");
    assert.equal(storage.readDraft(storage.STORY_STORAGE_KEY).baseSnapshot.id, "B");
    h.switch("reports");
    assert.equal(storage.readDraft(storage.REPORT_STORAGE_KEY).snapshot.id, "A");
  } finally { h.dispose(); delete globalThis.window; }
});

test("explicit fresh capture replaces only the selected kind, even when the captured ID is unchanged", async () => {
  for (const mode of ["reports", "stories"]) {
    const report = reportDraft("A"), story = storyDraft("B");
    const b = browser({ [storage.REPORT_STORAGE_KEY]: JSON.stringify(report), [storage.STORY_STORAGE_KEY]: JSON.stringify(story) });
    const id = mode === "reports" ? "A" : "B";
    const fresh = { ...snapshot(id), camera: { ...snapshot(id).camera, center: [-97, 39] } };
    const h = await mount(b, { mode, snapshot: fresh, freshDraftMode: mode });
    try {
      const replaced = storage.readDraft(mode === "reports" ? storage.REPORT_STORAGE_KEY : storage.STORY_STORAGE_KEY);
      const captured = mode === "reports" ? replaced.snapshot : replaced.baseSnapshot;
      assert.deepEqual(captured.camera.center, [-97, 39]);
      assert.notEqual(replaced.title, mode === "reports" ? report.title : story.title);
      h.switch(mode === "reports" ? "stories" : "reports");
      const other = storage.readDraft(mode === "reports" ? storage.STORY_STORAGE_KEY : storage.REPORT_STORAGE_KEY);
      assert.equal(other.title, mode === "reports" ? story.title : report.title);
    } finally { h.dispose(); delete globalThis.window; }
  }
});

test("new no-data story edits survive reload and failed saves leave previous bytes with an honest status", async () => {
  const b = browser();
  let h = await mount(b, { mode: "stories", snapshot: snapshot("new-map") });
  try {
    h.edit("Narrative", "A new story with no invented evidence");
    const saved = b.values.get(storage.STORY_STORAGE_KEY);
    assert.equal(storage.validStoryDraft(JSON.parse(saved)), true);
    h.dispose();
    h = await mount(b, { mode: "stories", snapshot: snapshot("later-map") });
    assert.equal(storage.readDraft(storage.STORY_STORAGE_KEY).scenes[0].narrative, "A new story with no invented evidence");
    b.deny();
    h.edit("Narrative", "Keep this unsaved edit exportable");
    b.flush(); h.draw();
    assert.equal(b.values.get(storage.STORY_STORAGE_KEY), saved);
    assert.ok(findNode(h.tree, n => n.type === "small" && n.props.children === "Not saved on this device · export a copy"));
    findNode(h.tree, n => n.type === "button" && n.props.children === "Export story JSON").props.onClick();
    assert.equal(JSON.parse(await b.downloads[0].text()).scenes[0].narrative, "Keep this unsaved edit exportable");
    h.dispose();
    assert.equal(b.timers.size, 1, "only the export URL cleanup remains after component timers are removed");
    b.flush();
    assert.equal(b.listeners.size, 0);
  } finally { h.dispose(); delete globalThis.window; }
});

const page = ts.createSourceFile("page.tsx", await readFile(new URL("../app/page.tsx", import.meta.url), "utf8"), ts.ScriptTarget.ES2022, true, ts.ScriptKind.TSX);
let openWorkspace, workspaceElement;
function visit(node) {
  if (ts.isVariableDeclaration(node) && node.name.getText(page) === "openPrimaryWorkspace") openWorkspace = node.initializer.arguments[0].getText(page);
  if (ts.isJsxSelfClosingElement(node) && node.tagName.getText(page) === "ReportStoryWorkspaces") workspaceElement = node.getText(page);
  ts.forEachChild(node, visit);
}
visit(page);
function evaluate(source, scope) {
  const code = ts.transpileModule(`return (${source});`, { compilerOptions: { target: ts.ScriptTarget.ES2022, jsx: ts.JsxEmit.React, jsxFactory: "jsx" } }).outputText;
  return new Function(...Object.keys(scope), code)(...Object.values(scope));
}
test("actual page opener and rendered props distinguish resume, fresh capture and repeated same-ID creation", () => {
  assert.ok(openWorkspace); assert.ok(workspaceElement);
  const state = { mode: "map", snapshot: null, request: { freshMode: null, revision: 0 } }, calls = [];
  const scope = {
    setWorkspaceSnapshot: value => { state.snapshot = value; },
    setWorkspaceDraftRequest: update => { state.request = update(state.request); },
    readDraftSnapshot(mode) { calls.push(`read:${mode}`); return snapshot(mode === "reports" ? "saved-report" : "saved-story"); },
    captureMapSnapshot() { calls.push("capture"); return snapshot("same-captured-id"); },
    setPrimaryWorkspace: mode => { state.mode = mode; },
    setFireReportContext() {}, setResearchReportContext() {}, setSubsurfaceReportContext() {}, setMapContextOpen() {}, setHelpOpen() {}, setQwenOpen() {}, announce() {},
    persistableResearch: value => value, persistableSubsurface: value => value,
    researchLocationRedacted: false, locationCameraRedacted: false, locationDerivedViewRef: { current: false }, subsurfacePrivate: false,
  };
  const open = (...args) => evaluate(openWorkspace, { ...scope, primaryWorkspace: state.mode, workspaceSnapshot: state.snapshot })(...args);
  const rendered = () => evaluate(workspaceElement, {
    jsx: (_type, props) => props, ReportStoryWorkspaces: "actual-workspace",
    workspaceSnapshot: state.snapshot, workspaceDraftRequest: state.request, primaryWorkspace: state.mode,
    fireReportContext: null, researchReportContext: null, subsurfaceReportContext: null, allEvidenceRecords: [],
    setPrimaryWorkspace: scope.setPrimaryWorkspace, returnToPrimaryMap() {}, inspectWorkspaceEvidence() {}, applyStoryScene() {}, captureMapSnapshot: scope.captureMapSnapshot,
  });
  open("reports");
  assert.equal(rendered().snapshot.id, "saved-report"); assert.equal(rendered().freshDraftMode, null);
  const activeKey = rendered().key;
  open("stories");
  assert.equal(rendered().key, activeKey, "nonfresh header navigation retains in-memory edits if storage is unavailable");
  state.mode = "map";
  open("stories");
  assert.equal(rendered().snapshot.id, "saved-story"); assert.equal(rendered().freshDraftMode, null);
  open("stories", true);
  const first = rendered();
  assert.equal(first.snapshot.id, "same-captured-id"); assert.equal(first.freshDraftMode, "stories");
  open("stories", true);
  assert.notEqual(rendered().key, first.key, "a repeated explicit capture must remount even when IDs collide");
  state.mode = "map";
  open("reports");
  assert.equal(rendered().freshDraftMode, null, "resuming after fresh creation must not create another new draft");
  assert.deepEqual(calls, ["read:reports", "read:stories", "capture", "capture", "read:reports"]);
});

const playerButton=(tree,name)=>findNode(tree,n=>n.type==='button'&&n.props.children===name);
const previewLabel=tree=>findNode(tree,n=>n.type==='snapshot-map').props.label;
const chapters=()=>{const draft=storyDraft('playback');return{...draft,scenes:Array.from({length:3},(_,i)=>({...draft.scenes[0],id:`chapter-${i}`,title:`Chapter ${i+1}`}))};};
test('switching to Reports stops story playback and returning does not silently resume',async()=>{
 const b=browser({[storage.STORY_STORAGE_KEY]:JSON.stringify(chapters())}),h=await mount(b,{mode:'stories',snapshot:snapshot('playback')});
 try{
  playerButton(h.tree,'Preview full story').props.onClick();h.draw();assert.ok([...b.timers.values()].some(entry=>entry.delay>=4800));
  h.changeProps({mode:'reports'});await settle();h.draw();b.flush();h.draw();h.changeProps({mode:'stories'});
  assert.equal(previewLabel(h.tree),'Story scene: Chapter 1');assert.ok(playerButton(h.tree,'Preview full story'));assert.equal(playerButton(h.tree,'Pause'),undefined);
 }finally{h.dispose();delete globalThis.window;}
});
test('hiding the document pauses immediately and requires an explicit restart',async()=>{
 const b=browser({[storage.STORY_STORAGE_KEY]:JSON.stringify(chapters())}),h=await mount(b,{mode:'stories',snapshot:snapshot('playback')});
 try{
  playerButton(h.tree,'Preview full story').props.onClick();h.draw();b.document.hidden=true;b.dispatch('visibilitychange');b.flush();h.draw();
  assert.equal(previewLabel(h.tree),'Story scene: Chapter 1');assert.ok(playerButton(h.tree,'Preview full story'));
  b.document.hidden=false;b.dispatch('visibilitychange');h.draw();assert.ok(playerButton(h.tree,'Preview full story'));assert.equal([...b.timers.values()].filter(entry=>entry.delay>=4800).length,0);
 }finally{h.dispose();assert.equal(b.listeners.size,0);delete globalThis.window;}
});
