import assert from "node:assert/strict";
import test from "node:test";
import { componentHarness, findNode } from "./component-harness.mjs";

const button = tree => findNode(tree, node => node.type === "button");
const nodes = tree => {
  const result = [];
  const visit = node => {
    if (!node || typeof node !== "object") return;
    result.push(node);
    for (const child of [node.props?.children].flat(Infinity)) visit(child);
  };
  visit(tree); return result;
};

test("route recovery saves the imported lighter rendering preference and resets once", async () => {
  const writes = []; let resets = 0, reloads = 0;
  const h = await componentHarness("app/error.tsx", { "./map-performance": { QUALITY_STORAGE_KEY: "quality-setting" } }, {
    window: { localStorage: { setItem: (...args) => writes.push(args) }, location: { reload: () => reloads++ } },
  });
  const tree = h.render(h.exports.default, { error: new Error("private details"), reset: () => resets++ });
  button(tree).props.onClick();
  assert.deepEqual(writes, [["quality-setting", "efficient"]]);
  assert.equal(resets, 1); assert.equal(reloads, 0);
  assert.equal(button(tree).props.type, "button");
  h.dispose();
});

test("route recovery still resets or reloads when browser storage is blocked", async () => {
  for (const hasReset of [true, false]) {
    let resets = 0, reloads = 0;
    const h = await componentHarness("app/error.tsx", { "./map-performance": { QUALITY_STORAGE_KEY: "quality-setting" } }, {
      window: { get localStorage() { throw new Error("blocked"); }, location: { reload: () => reloads++ } },
    });
    const tree = h.render(h.exports.default, { error: new Error("unavailable"), ...(hasReset ? { reset: () => resets++ } : {}) });
    assert.doesNotThrow(() => button(tree).props.onClick());
    assert.equal(resets, hasReset ? 1 : 0); assert.equal(reloads, hasReset ? 0 : 1);
    h.dispose();
  }
});

test("global recovery retries using the boundary reset or a full reload", async () => {
  for (const hasReset of [true, false]) {
    let resets = 0, reloads = 0;
    const h = await componentHarness("app/global-error.tsx", {}, { window: { location: { reload: () => reloads++ } } });
    const tree = h.render(h.exports.default, { error: new Error("unavailable"), ...(hasReset ? { reset: () => resets++ } : {}) });
    button(tree).props.onClick();
    assert.equal(resets, hasReset ? 1 : 0); assert.equal(reloads, hasReset ? 0 : 1);
    h.dispose();
  }
});

test("both recovery surfaces offer named full-navigation exits without rendering exception details", async () => {
  for (const file of ["app/error.tsx", "app/global-error.tsx"]) {
    const h = await componentHarness(file, { "./map-performance": { QUALITY_STORAGE_KEY: "quality-setting" } });
    const tree = h.render(h.exports.default, { error: new Error("private-token-do-not-render") });
    const alert = findNode(tree, node => node.props?.role === "alert");
    assert.ok(alert.props["aria-labelledby"]);
    assert.ok(findNode(tree, node => node.type === "h1" && node.props.id === alert.props["aria-labelledby"]));
    const nav = findNode(tree, node => node.type === "nav");
    assert.equal(nav.props["aria-label"], "Recovery options");
    const links = nodes(nav).filter(node => node.type === "a");
    assert.deepEqual(links.map(node => node.props.href), ["/downloads", "/about"]);
    for (const link of links) {
      assert.equal(typeof link.props.children, "string");
      assert.equal(link.props.onClick, undefined, "native anchors leave the failed client state");
      assert.equal(link.props.target, undefined, "recover in the current tab");
    }
    assert.doesNotMatch(JSON.stringify(tree), /private-token-do-not-render/);
    h.dispose();
  }
});
