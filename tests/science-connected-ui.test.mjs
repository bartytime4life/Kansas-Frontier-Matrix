import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import * as handoff from "../app/science/science-handoff.mjs";
import { componentHarness, findNode, settle } from "./component-harness.mjs";

const styles = new Proxy({}, { get: (_target, key) => String(key) });
const text = node => typeof node === "string" || typeof node === "number" ? String(node) : [node?.props?.children].flat(Infinity).map(child => child ? text(child) : "").join("");
const named = (tree, name) => findNode(tree, node => node.props?.name === name);
const button = (tree, label) => findNode(tree, node => node.type === "button" && text(node).startsWith(label));

test("the question launcher opens native year selectors while explaining tool-specific coverage", async t => {
  const h = await componentHarness("app/science/science-launcher.jsx", {
    "next/link": { default: "a" }, "./science-handoff.mjs": handoff, "./science.module.css": { default: styles },
  });
  t.after(() => h.dispose());
  let tree = h.render(h.exports.default);
  assert.ok(findNode(tree, node => node.props?.href === "/labs/heat-and-rain?year=2025"));
  findNode(tree, node => node.type === "select" && node.props.value === "weather").props.onChange({ target: { value: "drought" } });
  findNode(tree, node => node.type === "select" && node.props.value === 2025).props.onChange({ target: { value: "2022" } });
  tree = h.render(h.exports.default);
  assert.ok(findNode(tree, node => node.props?.href === "/labs/county-drought?from=2022&to=2022"));
  assert.match(text(tree), /105 Kansas counties/);
  assert.match(text(tree), /Choose the place/);
  assert.match(text(tree), /Locations are not matched across tools/);
  findNode(tree, node => node.type === "select" && node.props.value === "drought").props.onChange({ target: { value: "comparison" } });
  assert.ok(findNode(h.render(h.exports.default), node => node.props?.href === "/science/compare?year=2022&compare=2025"));
});

async function navHarness(t) {
  const h = await componentHarness("app/science/science-nav.jsx", {
    "next/link": { default: "a" }, "./science-handoff.mjs": handoff, "./science-nav.module.css": { default: styles },
  });
  t.after(() => h.dispose());
  return h;
}

test("shared navigation retains the current selection, active page, source anchors and bounded inquiry context", async t => {
  const h = await navHarness(t);
  const selection = { countyId: "20055", compareId: "20161", fromYear: 2021, toYear: 2024, level: 3, threshold: 27.5 };
  const props = { active: "drought", selection, sourceHref: "#drought-evidence", extraLinks: [{ href: "#winter-wheat-replay", label: "Winter wheat replay ↓" }] };
  let tree = h.render(h.exports.default, props);
  const current = handoff.scienceSelectionPath("drought", selection);
  assert.ok(findNode(tree, node => node.props?.href === current && node.props["aria-current"] === "page"));
  assert.ok(findNode(tree, node => node.props?.href === "#drought-evidence"));
  assert.ok(findNode(tree, node => node.props?.href === "#winter-wheat-replay"));
  const inquiry = findNode(tree, node => node.props?.href?.startsWith("/science/services?"));
  assert.equal(new URL(inquiry.props.href, "https://example.test").searchParams.get("context"), current);
  assert.ok(findNode(tree, node => node.props?.href === "/science/compare?year=2024&compare=2025"));
  findNode(tree, node => node.type === "select").props.onChange({ target: { value: "soil" } });
  tree = h.render(h.exports.default, props);
  assert.ok(findNode(tree, node => node.props?.href === "/labs/soil-profile?year=2024"));
  assert.match(text(tree), /Other tools open in 2024/);
});

test("report navigation keeps both selected years, and non-tool pages have valid destinations", async t => {
  for (const active of ["hub", "services", "comparison"]) {
    const h = await navHarness(t);
    const tree = h.render(h.exports.default, { active, selection: active === "comparison" ? { year: 2021, compareYear: 2020 } : undefined });
    const expected = active === "comparison" ? "/science/compare?year=2021&compare=2020" : "/labs/heat-and-rain?year=2025";
    assert.ok(findNode(tree, node => node.props?.href === expected));
    if (active === "services") assert.ok(findNode(tree, node => node.props?.href === "#project-brief" && node.props["aria-current"] === "page"));
    if (active === "comparison") assert.ok(findNode(tree, node => node.props?.href === expected && node.props["aria-current"] === "page"));
  }
});

async function inquiryHarness(t, search = "") {
  const window = new EventTarget();
  window.location = { search, origin: "https://kansasfrontiermatrix.com", pathname: "/science/services", hash: "" };
  const entries = [`/science/services${search}`];
  let entry = 0;
  function showLocation(path) {
    const url = new URL(path, window.location.origin);
    Object.assign(window.location, { search: url.search, pathname: url.pathname, hash: url.hash });
  }
  window.history = {
    pushState(_state, _title, path) { entries.splice(entry + 1); entries.push(path); entry += 1; showLocation(path); },
    back() { if (entry > 0) { entry -= 1; showLocation(entries[entry]); window.dispatchEvent(new Event("popstate")); } },
    forward() { if (entry + 1 < entries.length) { entry += 1; showLocation(entries[entry]); window.dispatchEvent(new Event("popstate")); } },
  };
  const copies = [], downloads = [], jumps = [];
  const navigator = { clipboard: { async writeText(value) { copies.push(value); } } };
  class DownloadURL extends URL {
    static createObjectURL(blob) { downloads.push({ blob }); return "blob:project-brief"; }
    static revokeObjectURL() {}
  }
  const document = {
    body: { appendChild() {} },
    createElement() { return { click() { downloads.at(-1).filename = this.download; }, remove() {} }; },
    getElementById(id) { return { scrollIntoView(options) { jumps.push({ id, action: "scroll", ...options }); }, focus(options) { jumps.push({ id, action: "focus", ...options }); } }; },
  };
  const h = await componentHarness("app/science/services/inquiry-builder.jsx", {
    "next/link": { default: "a" }, "../science-handoff.mjs": handoff, "./services.module.css": { default: styles },
  }, { window, document, navigator, URL: DownloadURL, Blob, setTimeout: () => 0 });
  t.after(() => h.dispose());
  return { window, navigator, copies, downloads, jumps, scopeLink: props => h.render(h.exports.ServiceScopeLink, props), render: () => { const tree = h.render(h.exports.default); h.commit(); return tree; } };
}

test("project inquiry actions use the current service, fields and public analysis without submitting", async t => {
  const context = "/labs/sunlight-and-sky?primary=wichita&comparison=topeka&year=2024&month=2&date=2024-02-29";
  const view = await inquiryHarness(t, new URL(handoff.serviceInquiryPath(context, "data"), "https://example.test").search);
  let tree = view.render();
  assert.equal(named(tree, "service").props.value, "data");
  assert.equal(button(tree, "Open email draft").props.disabled, true);
  assert.ok(findNode(tree, node => node.props?.href === context));
  named(tree, "question").props.onChange({ target: { value: "Help our team explain the two query points." } });
  named(tree, "area").props.onChange({ target: { value: "Kansas" } });
  named(tree, "timing").props.onChange({ target: { value: "Discuss this month" } });
  tree = view.render();
  const expected = handoff.inquiryDraft({ service: "data", question: "Help our team explain the two query points.", area: "Kansas", timing: "Discuss this month", context });
  assert.equal(findNode(tree, node => node.props?.readOnly).props.value, expected.text);
  await button(tree, "Copy brief").props.onClick();
  assert.deepEqual(view.copies, [expected.text]);
  button(view.render(), "Download .txt").props.onClick();
  assert.equal(view.downloads[0].filename, expected.filename);
  assert.equal(await view.downloads[0].blob.text(), `${expected.text}\n`);
  const email = findNode(view.render(), node => node.type === "a" && text(node).startsWith("Open email draft"));
  assert.equal(email.props.href, expected.mailto);
  email.props.onClick();
  assert.match(text(findNode(view.render(), node => node.props?.role === "status")), /Nothing has been submitted/);
  assert.match(text(tree), /Your draft stays on this page/);
});

test("copy fallback remains selectable and delayed feedback cannot survive edits or history changes", async t => {
  const view = await inquiryHarness(t, "?service=brief");
  let tree = view.render();
  named(tree, "question").props.onChange({ target: { value: "Read the source with us." } });
  tree = view.render();
  view.navigator.clipboard = undefined;
  await button(tree, "Copy brief").props.onClick();
  tree = view.render();
  assert.match(text(findNode(tree, node => node.props?.role === "status")), /Select the read-only project brief/);
  let selected = false;
  findNode(tree, node => node.props?.readOnly).props.onFocus({ currentTarget: { select() { selected = true; } } });
  assert.equal(selected, true);
  let resolve;
  view.navigator.clipboard = { writeText: () => new Promise(done => { resolve = done; }) };
  const pending = button(tree, "Copy brief").props.onClick();
  named(tree, "question").props.onChange({ target: { value: "A different current question." } });
  view.render();
  resolve();
  await pending;
  await settle();
  assert.equal(findNode(view.render(), node => node.props?.role === "status"), undefined);
  tree = view.render();
  named(tree, "service").props.onChange({ target: { value: "walkthrough" } });
  tree = view.render();
  assert.equal(named(tree, "service").props.value, "walkthrough");
  assert.match(findNode(tree, node => node.props?.readOnly).props.value, /Service: Guided team walkthrough/);
  const nextPending = button(tree, "Copy brief").props.onClick();
  view.window.location.search = "?service=data&context=%2Fscience%2Fcompare%3Fyear%3D2022%26compare%3D2020";
  view.window.dispatchEvent(new Event("popstate"));
  tree = view.render();
  resolve();
  await nextPending;
  assert.equal(named(tree, "service").props.value, "data");
  assert.equal(named(tree, "question").props.value, "A different current question.");
  assert.equal(findNode(view.render(), node => node.props?.role === "status"), undefined);
  assert.ok(findNode(tree, node => node.props?.href === "/science/compare?year=2022&compare=2020"));
  // Return to an earlier URL before an earlier clipboard promise finishes (ABA).
  tree = view.render();
  const abaPending = button(tree, "Copy brief").props.onClick();
  view.window.location.search = "?service=brief";
  view.window.dispatchEvent(new Event("popstate"));
  view.render();
  view.window.location.search = "?service=data&context=%2Fscience%2Fcompare%3Fyear%3D2022%26compare%3D2020";
  view.window.dispatchEvent(new Event("popstate"));
  view.render();
  resolve();
  await abaPending;
  assert.equal(findNode(view.render(), node => node.props?.role === "status"), undefined);
});

test("service card clicks update the builder, preserve fields and context, and follow Back and Forward", async t => {
  const context = "/labs/daily-air-quality?county=20177&year=2023&month=9&threshold=100&date=2023-09-06";
  const view = await inquiryHarness(t, new URL(handoff.serviceInquiryPath(context), "https://example.test").search);
  let tree = view.render();
  named(tree, "question").props.onChange({ target: { value: "Prepare a documented table for our team." } });
  named(tree, "area").props.onChange({ target: { value: "Shawnee County" } });
  tree = view.render();
  await button(tree, "Copy brief").props.onClick();
  assert.ok(findNode(view.render(), node => node.props?.role === "status"));
  const link = view.scopeLink({ service: "data", children: "Discuss this scope" });
  const url = new URL(link.props.href, "https://example.test");
  assert.equal(url.searchParams.get("context"), context);
  assert.equal(url.searchParams.get("service"), "data");
  assert.equal(url.hash, "#project-brief");
  let prevented = false, changes = 0;
  view.window.addEventListener("kfm-science-inquiry-selection", () => { changes += 1; });
  link.props.onClick({ button: 0, currentTarget: { target: "" }, preventDefault() { prevented = true; } });
  tree = view.render();
  assert.equal(prevented, true);
  assert.equal(changes, 1, "the same-page card click notifies the live builder");
  assert.equal(named(tree, "service").props.value, "data");
  assert.equal(named(tree, "question").props.value, "Prepare a documented table for our team.");
  assert.equal(named(tree, "area").props.value, "Shawnee County");
  assert.match(findNode(tree, node => node.props?.readOnly).props.value, /Service: Reusable data pack/);
  assert.equal(findNode(tree, node => node.props?.role === "status"), undefined);
  assert.equal(view.jumps.map(item => `${item.id}:${item.action}`).join(","), "project-brief:scroll,project-brief:focus");
  await button(tree, "Copy brief").props.onClick();
  assert.ok(findNode(view.render(), node => node.props?.role === "status"));
  view.window.history.back();
  tree = view.render();
  assert.equal(named(tree, "service").props.value, "brief");
  assert.match(findNode(tree, node => node.props?.readOnly).props.value, /Service: Custom evidence brief/);
  assert.equal(findNode(tree, node => node.props?.role === "status"), undefined);
  view.window.history.forward();
  tree = view.render();
  assert.equal(named(tree, "service").props.value, "data");
  assert.equal(named(tree, "question").props.value, "Prepare a documented table for our team.");
  assert.equal(findNode(tree, node => node.props?.role === "status"), undefined, "old copied feedback cannot return with a previous URL");
  assert.ok(findNode(tree, node => node.props?.href === context));

  // Modified and new-tab actions retain ordinary link behavior.
  const currentSearch = view.window.location.search;
  for (const options of [{ metaKey: true }, { ctrlKey: true }, { shiftKey: true }, { altKey: true }, { button: 1 }, { currentTarget: { target: "_blank" } }, { defaultPrevented: true }]) {
    let intercepted = false;
    link.props.onClick({ button: 0, currentTarget: { target: "" }, preventDefault() { intercepted = true; }, ...options });
    assert.equal(intercepted, false);
    assert.equal(view.window.location.search, currentSearch);
  }
  assert.equal(view.jumps.length, 2);
  view.window.location.search = "?context=https%3A%2F%2Fforeign.test%2Fprivate";
  const unsafe = view.scopeLink({ service: "data", children: "Discuss this scope" });
  assert.equal(new URL(unsafe.props.href, "https://example.test").searchParams.has("context"), false);
});

test("services discovery and free worked-example links are registered without data-source admission", async () => {
  const page = await readFile("app/science/services/page.tsx", "utf8");
  const science = await readFile("app/science/page.tsx", "utf8");
  const about = await readFile("app/about/page.tsx", "utf8");
  let discovery;
  try { discovery = await readFile("app/crawler-discovery.ts", "utf8"); }
  catch { discovery = await readFile("app/sitemap.ts", "utf8"); }
  assert.match(page, /href="\/science\/compare"/);
  for (const source of [science, about, discovery]) assert.match(source, /\/science\/services/);
  assert.match(page, /public tools stay free/);
  assert.doesNotMatch(page, /<form|checkout|payment setup/);
});
