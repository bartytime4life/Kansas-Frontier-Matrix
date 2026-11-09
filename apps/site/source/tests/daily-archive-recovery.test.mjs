import assert from "node:assert/strict";
import test from "node:test";
import { componentHarness, findNode, settle } from "./component-harness.mjs";

const model = (await componentHarness("app/daily-archive.ts", {})).exports;
const today = new Date().toISOString().slice(0, 10);
const earlier = "2000-01-01";
const catalog = (day = today, entries = [], paused = false) => ({
  day, entries, days: entries.length ? [{ day, captures: entries.length }] : [],
  storage: { used: 0, budget: 2_000_000_000, paused }, feeds: model.DAILY_FEEDS, earliestDay: null, latestDay: null,
});
const entry = (id, feed = "usgs-streamflow", day = today) => ({
  id, feed, day, attempt: 1, status: "ready", review: "pending", started_at: `${day}T12:00:00Z`,
  finished_at: `${day}T12:01:00Z`, bytes: 20, sha256: "fixture", object_key: `fixture/${id}`,
  feature_count: 1, source_time: null, source_day: day, message: "Synthetic fixture", review_note: null,
});
const stored = row => ({ entry: row, reviews: [], payload: {
  feed: row.feed, state: "ready", source: `fixture source ${row.id}`, retrievedAt: row.started_at,
  upstreamUpdatedAt: null, featureCount: 1, data: { type: "FeatureCollection", features: [{ type: "Feature", geometry: { type: "Point", coordinates: [-98,38] }, properties: { fixture: row.id } }] },
  limitation: "Synthetic component fixture", truncated: false,
} });
const response = (body, status = 200) => ({ ok: status >= 200 && status < 300, status, json: async () => body });
const deferred = () => { let resolve; const promise = new Promise(done => { resolve = done; }); return { promise, resolve }; };
const button = (tree, text) => findNode(tree, node => node.type === "button" && node.props.children === text);
const captureButton = tree => button(tree, "Capture today’s sources");
const settingsButton = tree => button(tree, "Save capture settings");
const alert = tree => findNode(tree, node => node.props?.role === "alert");
const textOf = node => {
  if (typeof node === "string" || typeof node === "number") return String(node);
  if (!node || typeof node !== "object") return "";
  return [node.props?.children].flat(Infinity).map(textOf).join(" ");
};
const mapProps = tree => findNode(tree, node => typeof node.type === "function" && node.type.name === "ArchiveMap").props;
const mapPayload = tree => mapProps(tree).payload;
function clock() {
  const timers = new Map(); let index = 0;
  return { timers,
    globals: { setTimeout: (fn, delay) => { const id = ++index; timers.set(id, { fn, delay }); return id; }, clearTimeout: id => timers.delete(id) },
    expire: () => { const timer = timers.values().next().value; assert.ok(timer); assert.equal(timer.delay, 15_000); timer.fn(); },
  };
}
async function setup(fetch, time = clock(), hostname = "127.0.0.1") {
  const h = await componentHarness("app/daily-archive/workspace.tsx", {
    "next/link": { default: "a" }, "../daily-archive": model,
    "../maplibre-seam": { loadMapLibre: () => Promise.reject(new Error("No map needed in component tests")) },
    "../daily-archive-map": { applyArchiveMapData() {} }, "./archive.module.css": { default: {} },
  }, { fetch, Headers, window: { location: { hostname } }, ...time.globals });
  const render = () => { const tree = h.render(h.exports.default, {}); h.commit(); return tree; };
  return { h, render, time };
}

test("initial archive access and network failures end loading without claiming empty coverage or allowing writes", async () => {
  for (const status of [401, 403, 503, "network"]) {
    const requests = [];
    const { h, render } = await setup((url, options) => {
      requests.push({ url, options });
      return status === "network" ? Promise.reject(new TypeError("Failed to fetch")) : Promise.resolve(response({ error: status===401?"OWNER_ACCESS_REQUIRED":status===403?"OWNER_ACCESS_REJECTED":"ARCHIVE_STORAGE_UNAVAILABLE" }, status));
    });
    let tree = render();
    assert.match(textOf(tree), /Reading stored coverage/);
    assert.equal(captureButton(tree).props.disabled, true); assert.equal(settingsButton(tree).props.disabled, true);
    assert.doesNotMatch(textOf(tree), /No saved data|Missing · no capture|0 recent capture days/);
    await settle(); tree = render();
    assert.ok(alert(tree)); assert.match(textOf(tree), /Storage status is unavailable/);
    assert.doesNotMatch(textOf(tree), /OWNER_ACCESS_|ARCHIVE_STORAGE_UNAVAILABLE|Failed to fetch/);
    if(status===401||status===403)assert.match(textOf(alert(tree)), /local owner access.*retry/);
    assert.doesNotMatch(textOf(tree), /Reading storage status|Reading stored coverage|No saved data|Missing · no capture|0 recent capture days/);
    assert.equal(button(tree, "Retry archive check").props.disabled, false);
    captureButton(tree).props.onClick(); settingsButton(tree).props.onClick(); await settle();
    assert.equal(requests.length, 1, "unavailable actions stay guarded even if their handlers are called");
    assert.equal(requests.some(request => request.options.method === "POST"), false);
    h.dispose();
  }
});

test("hosted access failures explain owner sign-in or account requirements without exposing backend codes", async () => {
  for(const status of [401,403]){
    const { h, render } = await setup(() => Promise.resolve(response({ error: "OWNER_INTERNAL_ACCESS_CODE" },status)),clock(),"private.example.test");
    render();await settle();const tree=render();
    assert.match(textOf(alert(tree)),status===401?/Sign in as an archive owner/:/Use an archive owner account/);
    assert.doesNotMatch(textOf(alert(tree)),/OWNER_INTERNAL_ACCESS_CODE|local owner access/);
    assert.equal(findNode(tree,node=>node.type==="input"&&node.props.type==="password"),undefined);
    assert.equal(captureButton(tree).props.disabled,true);h.dispose();
  }
});

test("retry success establishes truly empty coverage and restores actions according to the returned pause setting", async () => {
  for (const paused of [false, true]) {
    const retry = deferred(); let calls = 0;
    const { h, render } = await setup(() => ++calls === 1 ? Promise.resolve(response({ error: "Owner access required." }, 401)) : retry.promise);
    render(); await settle(); let tree = render();
    button(tree, "Retry archive check").props.onClick(); tree = render();
    assert.equal(alert(tree), undefined); assert.match(textOf(tree), /Reading stored coverage/);
    assert.equal(captureButton(tree).props.disabled, true);
    retry.resolve(response(catalog(today, [], paused))); await settle(); tree = render();
    assert.equal(alert(tree), undefined);
    assert.match(textOf(tree), /No captures for this day/); assert.match(textOf(tree), /No saved data for this source and day/);
    assert.match(textOf(tree), /Missing · no capture/); assert.match(textOf(tree), /0 recent capture days/);
    assert.equal(captureButton(tree).props.disabled, paused); assert.equal(settingsButton(tree).props.disabled, false);
    assert.equal(findNode(tree, node => node.type === "input" && node.props.type === "number").props.disabled, false);
    h.dispose();
  }
});

test("a failed refresh preserves previously verified capture data but blocks writes against unknown current status", async () => {
  const row = entry("retained"); let catalogs = 0;
  const { h, render } = await setup(url => url.includes("?id=") ? Promise.resolve(response(stored(row))) : ++catalogs === 1 ? Promise.resolve(response(catalog(today, [row]))) : Promise.resolve(response({ error: "Storage unavailable." }, 503)));
  render(); await settle(); render(); await settle(); let tree = render();
  assert.equal(mapPayload(tree).source, "fixture source retained");
  button(tree, "Refresh archive").props.onClick(); tree = render();
  assert.equal(mapPayload(tree).source, "fixture source retained"); assert.equal(captureButton(tree).props.disabled, true);
  await settle(); tree = render();
  assert.ok(alert(tree)); assert.match(textOf(tree), /Showing previously checked coverage/);
  assert.equal(mapPayload(tree).source, "fixture source retained"); assert.equal(settingsButton(tree).props.disabled, true);
  h.dispose();
});

test("stalled archive headers or JSON bodies time out, restore retry, and reject late success", async () => {
  for (const stage of ["headers", "body"]) {
    const stalled = deferred(), time = clock(); let signal;
    const { h, render } = await setup((_url, options) => {
      signal = options.signal;
      return stage === "headers" ? stalled.promise : Promise.resolve({ ok: true, status: 200, json: () => stalled.promise });
    }, time);
    render(); await settle(); time.expire(); await settle(); let tree = render();
    assert.equal(signal.aborted, true); assert.equal(time.timers.size, 0);
    assert.match(textOf(alert(tree)), /took too long/); assert.ok(button(tree, "Retry archive check"));
    assert.doesNotMatch(textOf(tree), /Reading storage status|No saved data|Missing · no capture/);
    stalled.resolve(stage === "headers" ? response(catalog()) : catalog()); await settle(); tree = render();
    assert.ok(alert(tree)); assert.equal(captureButton(tree).props.disabled, true);
    h.dispose();
  }
});

test("a new capture day cancels the older catalog and never labels its late response as current coverage", async () => {
  const old = deferred(), next = deferred(); const requests = [];
  const { h, render } = await setup((url, options) => { requests.push({ url, signal: options.signal }); return url.includes(earlier) ? next.promise : old.promise; });
  let tree = render();
  findNode(tree, node => node.type === "input" && node.props.type === "date").props.onChange({ target: { value: earlier } }); tree = render();
  assert.equal(requests[0].signal.aborted, true);
  old.resolve(response(catalog(today, [entry("obsolete-day")]))); await settle(); tree = render();
  assert.doesNotMatch(textOf(tree), /obsolete-day|No saved data/); assert.equal(captureButton(tree).props.disabled, true);
  next.resolve(response(catalog(earlier))); await settle(); tree = render();
  assert.match(textOf(tree), /No saved data for this source and day/); assert.equal(alert(tree), undefined);
  h.dispose();
});

test("source selection rejects a late capture from the previous source", async () => {
  const river = entry("river"), quake = entry("quake", "usgs-earthquakes");
  const old = deferred(), next = deferred(); let oldSignal;
  const { h, render } = await setup((url, options) => {
    if (url.includes("id=river")) { oldSignal = options.signal; return old.promise; }
    return url.includes("id=quake") ? next.promise : Promise.resolve(response(catalog(today, [river, quake])));
  });
  render(); await settle(); let tree = render();
  findNode(tree, node => node.type === "button" && findNode(node, child => child.type === "strong" && child.props.children === "Earthquakes")).props.onClick(); tree = render();
  assert.equal(oldSignal.aborted, true);
  next.resolve(response(stored(quake))); await settle(); tree = render();
  old.resolve(response(stored(river))); await settle(); tree = render();
  assert.equal(mapPayload(tree).source, "fixture source quake");
  h.dispose();
});

test("changing local access hides the earlier owner's data and cancels its outstanding capture read", async () => {
  const row = entry("earlier-owner"), old = deferred(), next = deferred(); let oldSignal, nextHeader;
  const { h, render } = await setup((url, options) => {
    if (url.includes("?id=")) { oldSignal = options.signal; return old.promise; }
    if (options.headers.get("Authorization")) { nextHeader = options.headers.get("Authorization"); return next.promise; }
    return Promise.resolve(response(catalog(today, [row])));
  });
  render(); await settle(); let tree = render();
  findNode(tree, node => node.type === "input" && node.props.type === "password").props.onChange({ target: { value: "synthetic-owner-capability" } }); tree = render();
  findNode(tree, node => node.type === "form").props.onSubmit({ preventDefault() {} }); tree = render();
  assert.equal(oldSignal.aborted, true); assert.equal(nextHeader, "Bearer synthetic-owner-capability");
  old.resolve(response(stored(row))); await settle(); tree = render();
  assert.equal(mapPayload(tree), null); assert.doesNotMatch(textOf(tree), /earlier-owner|No saved data/);
  assert.equal(captureButton(tree).props.disabled, true);
  next.resolve(response(catalog())); await settle(); tree = render();
  assert.match(textOf(tree), /No saved data for this source and day/); assert.equal(mapPayload(tree), null);
  h.dispose();
});

test("unmount promptly clears stalled catalog deadlines and ignores late fetch adapters", async () => {
  for (const stage of ["headers", "body"]) {
    const stalled = deferred(), time = clock(); let signal;
    const { h, render } = await setup((_url, options) => {
      signal = options.signal;
      return stage === "headers" ? stalled.promise : Promise.resolve({ ok: true, status: 200, json: () => stalled.promise });
    }, time);
    render(); await settle(); const before = textOf(render());
    h.dispose(); await settle(); assert.equal(signal.aborted, true); assert.equal(time.timers.size, 0);
    stalled.resolve(stage === "headers" ? response(catalog()) : catalog()); await settle();
    assert.equal(textOf(h.render(h.exports.default, {})), before);
  }
});

test("fresh held or failed catalog entries hide same-ID capture records and county geometry before passive effects", async () => {
  for (const transition of ["held", "failed"]) {
    const river = entry("river"), county = entry("county", "census-counties"), fresh = deferred(); let catalogs = 0;
    const { h, render } = await setup(url => {
      if (url.includes("?id=")) return Promise.resolve(response(stored(url.includes("id=county") ? county : river)));
      return ++catalogs === 1 ? Promise.resolve(response(catalog(today, [river,county]))) : fresh.promise;
    });
    render(); await settle(); render(); await settle(); let tree = render();
    assert.ok(mapPayload(tree)); assert.ok(mapProps(tree).counties);
    button(tree,"Refresh archive").props.onClick(); render();
    const changed = row => transition === "held" ? { ...row, review:"held" } : { ...row, status:"failed" };
    fresh.resolve(response(catalog(today,[changed(river),changed(county)]))); await settle();
    tree = h.render(h.exports.default,{});
    assert.equal(mapPayload(tree),null); assert.equal(mapProps(tree).counties,null);
    assert.doesNotMatch(textOf(tree),/fixture source river|First 100 records below|"fixture"/);
    assert.match(textOf(tree),transition === "held" ? /held and hidden from the map/ : /Capture failed/);
    h.commit(); h.dispose();
  }
});

test("replacing the eligible county capture removes previous geometry until that exact new entry is read", async () => {
  const river=entry("river"),oldCounty=entry("old-county","census-counties"),nextCounty=entry("new-county","census-counties"),replacement=deferred();let catalogs=0;
  const { h,render }=await setup(url=>{
    if(url.includes("id=new-county"))return replacement.promise;
    if(url.includes("?id="))return Promise.resolve(response(stored(url.includes("id=old-county")?oldCounty:river)));
    return Promise.resolve(response(catalog(today,[river,++catalogs===1?oldCounty:nextCounty])));
  });
  render();await settle();render();await settle();let tree=render();
  assert.equal(mapProps(tree).counties.features[0].properties.fixture,"old-county");
  button(tree,"Refresh archive").props.onClick();render();await settle();
  tree=h.render(h.exports.default,{});assert.equal(mapProps(tree).counties,null,"render cannot reuse another capture's county geometry");
  h.commit();replacement.resolve(response(stored(nextCounty)));await settle();tree=render();
  assert.equal(mapProps(tree).counties.features[0].properties.fixture,"new-county");h.dispose();
});

test("an acknowledged hold immediately suppresses old in-flight reads and stays hidden if catalog refresh fails", async () => {
  for(const feed of ["usgs-streamflow","census-counties"]){
    const row={...entry(`hold-${feed}`,feed),review:"reviewed",review_note:"Earlier reviewed note."},late=deferred();let catalogs=0,reads=0;
    const submittedNote="Submitted hold explanation.",serverNote="Hold this exact capture for correction.";
    const acknowledgedNote=feed==="usgs-streamflow"?serverNote:submittedNote;
    const { h,render }=await setup((url,options)=>{
      if(options.method==="POST")return Promise.resolve(response({id:row.id,state:"held",...(feed==="usgs-streamflow"?{note:`  ${serverNote}  `}:{})}));
      if(url.includes("?id=")){reads++;return catalogs>=2?late.promise:Promise.resolve(response(stored(row)));}
      return ++catalogs<=2?Promise.resolve(response(catalog(today,[{...row}]))):Promise.resolve(response({error:"ARCHIVE_STORAGE_UNAVAILABLE"},503));
    });
    render();await settle();let tree=render();
    if(feed==="census-counties"){
      findNode(tree,node=>node.type==="button"&&findNode(node,child=>child.type==="strong"&&child.props.children==="County reference")).props.onClick();render();
    }
    await settle();tree=render();assert.ok(mapPayload(tree));
    button(tree,"Refresh archive").props.onClick();render();await settle();tree=render();
    assert.ok(reads>=2,"a fresh stored read is in flight while the owner records the hold");
    findNode(tree,node=>node.type==="select"&&findNode(node,child=>child.type==="option"&&child.props.value==="held")).props.onChange({target:{value:"held"}});
    findNode(tree,node=>node.type==="textarea").props.onChange({target:{value:`  ${submittedNote}  `}});tree=render();
    button(tree,"Save review").props.onClick();await settle();
    tree=h.render(h.exports.default,{});assert.equal(mapPayload(tree),null,"hold acknowledgement hides content before cleanup effects");
    assert.ok(textOf(tree).includes(`held  · ${acknowledgedNote}`),"the held review shows its acknowledged trimmed note, with a submitted-note fallback");
    assert.doesNotMatch(textOf(tree),/Earlier reviewed note/);
    if(feed==="census-counties")assert.equal(mapProps(tree).counties,null);
    assert.doesNotMatch(textOf(tree),/First 100 records below|"fixture"/);
    late.resolve(response(stored(row)));await settle();tree=h.render(h.exports.default,{});
    assert.equal(mapPayload(tree),null,"late adapter completion cannot resurrect an acknowledged hold");
    if(feed==="census-counties")assert.equal(mapProps(tree).counties,null);
    h.commit();await settle();tree=render();
    assert.ok(alert(tree));assert.match(textOf(tree),/held and hidden from the map/);assert.equal(mapPayload(tree),null);
    assert.ok(textOf(tree).includes(`held  · ${acknowledgedNote}`));assert.doesNotMatch(textOf(tree),/Earlier reviewed note/);
    if(feed==="census-counties")assert.equal(mapProps(tree).counties,null);
    assert.equal(settingsButton(tree).props.disabled,true);h.dispose();
  }
});
