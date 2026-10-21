import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

// Execute the actual page callbacks, including their async stale-response guards.
const page = await readFile("app/page.tsx", "utf8");
const sections = [["commitTemporalFrame", "stepTemporalSweep"], ["refreshOfficialContext", "reserveSmokePlayback"], ["loadOfficialArchiveDay", "returnOfficialSourceToCurrent"]];
const source = sections.map(([start, end]) => page.slice(page.indexOf(`  const ${start} =`), page.indexOf(`  const ${end} =`))).join("\n");
const code = ts.transpileModule(source, { compilerOptions: { target: ts.ScriptTarget.ES2022 } }).outputText;
const feed = "usgs-earthquakes", hidden = "raspberry-shake-stations";
const day = "2026-10-01";
const payload = (name = "archive") => ({ feed, state: "ready", featureCount: 1, retrievedAt: "2026-10-02T00:00:00Z", data: { type: "FeatureCollection", features: [{ id: name }] } });
function harness() {
  const ref = current => ({ current }), state = {}, reads = [], cleared = [];
  const context = {
    useCallback: fn => fn, announce() {}, temporalMode: "snapshot", OFFICIAL_CONTEXT_PRESENT_FRAME: 2026,
    CALENDAR_ARCHIVE_BOUNDS: { [feed]: "1800-01-01", [hidden]: "1800-01-01" },
    OFFICIAL_CONTEXT_BY_ID: { [feed]: { apiPath: "/source", shortTitle: "Quakes" } },
    calendarSeekGeneration: ref(0), calendarSweepRef: ref({ day }), calendarArchiveLoads: ref(new Map()),
    officialArchiveDaysRef: ref({ [feed]: day, [hidden]: day }),
    officialArchivePayloadsRef: ref({ [feed]: payload(), [hidden]: payload() }),
    officialPayloadsRef: ref({ [feed]: payload(), [hidden]: payload(), unrelated: { id: "retained" } }),
    officialRequestsRef: ref(new Map()), officialVisibilityRef: ref({ [feed]: true, [hidden]: false }),
    yearRef: ref(2026), buildYearCurrentRef: ref(true), temporalQueryRef: ref({ frame: 2026 }),
    selectedRef: ref({ feed }), mapRef: ref({}), styleGenerationReadyRef: ref(true),
    noaaRadarReadyRef: ref(false), noaaRadarFrameTimeRef: ref(null), officialOpacityRef: ref({}),
    officialContextIdForSelection: selection => selection?.feed,
    clearOfficialContextFeed: (_map, id) => cleared.push(id), updateSelectionSource() {},
    runMapMutation: (_label, fn) => fn(), runtimeOfficialVisibility: v => v, applyOfficialContextState() {},
    currentUtcDay: () => "2026-10-21", readFireDay: async () => null, validLayerPayload: () => true,
    earthquakeEventTimes: () => [], smokeValidityTimes: () => [], smokeInitialFrameIndex: () => -1,
    layerJsonReadsRef: ref({ read: (url, options) => new Promise(resolve => reads.push({ url, options, resolve: body => resolve({ body, response: { ok: true } }) })) }),
  };
  for (const key of ["CalendarSweep", "SweepRangeStart", "SweepRangeEnd", "Year", "PreviewYear", "CompareTimeB", "OfficialArchiveDays", "OfficialPayloads", "OfficialStates", "OfficialErrors", "OfficialReadPhases", "EarthquakeArchiveFrameIndex", "SmokeArchiveFrameIndex", "Selected", "RightOpen"])
    context["set" + key] = value => { state[key] = typeof value === "function" ? value(state[key] ?? {}) : value; };
  const callbacks = new Function(...Object.keys(context), code + "\nreturn { commitTemporalFrame, loadOfficialArchiveDay, refreshOfficialContext };")(...Object.values(context));
  return { ...callbacks, context, state, reads, cleared };
}
for (const year of [2026, 2024, -1000]) test(`annual transition to ${year} clears dated payloads, selected archived record, and hidden archives`, () => {
  const h = harness(); h.commitTemporalFrame(year);
  assert.equal(h.context.calendarSweepRef.current, null);
  for (const id of [feed, hidden]) {
    assert.equal(h.context.officialArchiveDaysRef.current[id], undefined);
    assert.equal(h.context.officialPayloadsRef.current[id], undefined);
    assert.equal(h.context.officialArchivePayloadsRef.current[id], undefined);
  }
  assert.equal(h.context.selectedRef.current, null);
  assert.equal(h.state.OfficialStates[feed], "idle");
  assert.equal(h.context.officialPayloadsRef.current.unrelated.id, "retained");
  assert.equal(h.context.officialVisibilityRef.current[feed], true);
  assert.equal(h.state.Year, year);
});
test("calendar-internal commits preserve the exact archive and selection; annual exits preserve an unrelated selected place", () => {
  const h = harness(), original = h.context.officialPayloadsRef.current[feed];
  h.commitTemporalFrame(2026, undefined, true);
  assert.equal(h.context.officialPayloadsRef.current[feed], original);
  h.context.selectedRef.current = { id: "place" }; h.commitTemporalFrame(2026);
  assert.equal(h.context.selectedRef.current.id, "place");
});
test("pending archive cannot repopulate Present, and repeated same-day entry starts a new request", async () => {
  const h = harness();
  const first = h.loadOfficialArchiveDay(feed, day);
  assert.equal(h.reads.length, 1);
  h.commitTemporalFrame(2026);
  assert.equal(h.reads[0].options.signal.aborted, true);
  assert.equal(h.context.calendarArchiveLoads.current.has(feed), false);
  const current = h.refreshOfficialContext(feed);
  assert.equal(h.state.OfficialStates[feed], "loading");
  const present = payload("present"); present.retrievedAt = "2026-10-21T12:00:00Z";
  h.reads[1].resolve(present); await current;
  h.reads[0].resolve(payload()); await first;
  assert.equal(h.context.officialPayloadsRef.current[feed], present);
  const again = h.loadOfficialArchiveDay(feed, day);
  h.commitTemporalFrame(2026);
  const repeated = h.loadOfficialArchiveDay(feed, day);
  assert.equal(h.reads.length, 4);
  h.reads[2].resolve(payload("stale")); await again;
  assert.equal(h.context.officialPayloadsRef.current[feed], undefined);
  h.reads[3].resolve(payload("new")); await repeated;
  assert.equal(h.context.officialPayloadsRef.current[feed].data.features[0].id, "new");
});
test("failed current response after exit stays unavailable with no archived fallback", async () => {
  const h = harness(); h.commitTemporalFrame(2026);
  const current = h.refreshOfficialContext(feed); h.reads[0].resolve({ error: "unavailable" }); await current;
  assert.equal(h.state.OfficialStates[feed], "error");
  assert.equal(h.context.officialPayloadsRef.current[feed], undefined);
});
test("leaving history never bypasses the build-year or non-Present current-source hold", async () => {
  for (const reason of ['build-year', 'historical-year']) {
    const h = harness(); h.commitTemporalFrame(reason === 'historical-year' ? 2024 : 2026);
    if (reason === 'build-year') h.context.buildYearCurrentRef.current = false;
    else h.context.temporalQueryRef.current = { frame: 2024 };
    await h.refreshOfficialContext(feed);
    assert.equal(h.reads.length, 0);
    assert.equal(h.context.officialPayloadsRef.current[feed], undefined);
    assert.equal(h.state.OfficialStates[feed], 'idle');
  }
});
