import assert from "node:assert/strict";
import test from "node:test";
import { modelUrl } from "../scripts/lib/typescript-model.mjs";

const { bindCollectionScrollBoundary } = await import(await modelUrl("app/data-library/scroll-boundary.ts"));

// Small DOM-contract fixture: these tests exercise the actual native listeners,
// not browser rendering or real input delivery. The production browser journey
// separately checks mouse/touch handoff over the rendered list.
class Scroller {
  constructor({ height, content, top = 0, lineHeight = "24px", refuse = false }) {
    this.clientHeight = height;
    this.scrollHeight = content;
    this.position = top;
    this.refuse = refuse;
    this.listeners = new Map();
    this.ownerDocument = { defaultView: { getComputedStyle: () => ({ lineHeight }) } };
  }
  get scrollTop() { return this.position; }
  set scrollTop(value) { if (!this.refuse) this.position = Math.max(0, Math.min(this.scrollHeight - this.clientHeight, value)); }
  addEventListener(type, handler, options) { this.listeners.set(type, { handler, options }); }
  removeEventListener(type, handler) { if (this.listeners.get(type)?.handler === handler) this.listeners.delete(type); }
  emit(type, properties = {}, onCancel = () => {}) {
    const event = {
      cancelable: true, defaultPrevented: false,
      deltaX: 0, deltaY: 0, deltaMode: 0, touches: [],
      preventDefault() { onCancel(); this.defaultPrevented = true; },
      ...properties,
    };
    this.listeners.get(type)?.handler(event);
    return event;
  }
}

function fixture(listOptions = {}, pageOptions = {}) {
  const list = new Scroller({ height: 100, content: 500, top: 400, ...listOptions });
  const page = new Scroller({ height: 300, content: 1000, top: 200, ...pageOptions });
  const dispose = bindCollectionScrollBoundary(list, page);
  return { list, page, dispose };
}
const point = (x, y, identifier = 1) => ({ identifier, clientX: x, clientY: y });

test("list wheel boundaries hand off only the bounded movement the page actually consumes", () => {
  const { list, page, dispose } = fixture();
  assert.equal(list.listeners.get("wheel").options.passive, false);
  const down = list.emit("wheel", { deltaY: 60 }, () => assert.equal(page.scrollTop, 260, "move the page before canceling native input"));
  assert.equal(down.defaultPrevented, true);
  assert.equal(list.scrollTop, 400, "the list is unchanged");
  page.scrollTop = 680;
  assert.equal(list.emit("wheel", { deltaY: 100 }).defaultPrevented, true);
  assert.equal(page.scrollTop, 700, "the page cannot move past its end");
  assert.equal(list.emit("wheel", { deltaY: 100 }).defaultPrevented, false, "nothing is canceled when both scrollers are at the end");
  list.scrollTop = 0;
  page.scrollTop = 50;
  assert.equal(list.emit("wheel", { deltaY: -120 }).defaultPrevented, true);
  assert.equal(page.scrollTop, 0, "reverse/top handoff is bounded too");
  assert.equal(list.emit("wheel", { deltaY: -120 }).defaultPrevented, false);
  dispose();
});

test("wheel normalization uses pixels, computed lines and page heights", () => {
  for (const [deltaMode, deltaY, expected, lineHeight] of [[0, 3, 203, "24px"], [1, 3, 272, "24px"], [1, 2, 232, "normal"], [2, 1, 500, "24px"]]) {
    const { list, page, dispose } = fixture({ lineHeight });
    assert.equal(list.emit("wheel", { deltaMode, deltaY }).defaultPrevented, true);
    assert.equal(page.scrollTop, expected);
    dispose();
  }
});

test("native inner scrolling, horizontal input, modifiers and uncancelable events remain untouched", () => {
  const { list, page, dispose } = fixture();
  list.scrollTop = 200;
  assert.equal(list.emit("wheel", { deltaY: 70 }).defaultPrevented, false);
  assert.equal(page.scrollTop, 200);
  list.scrollTop = 400;
  assert.equal(list.emit("wheel", { deltaY: -70 }).defaultPrevented, false, "upward input at the list end still belongs to the list");
  list.scrollTop = 0;
  assert.equal(list.emit("wheel", { deltaY: 70 }).defaultPrevented, false, "downward input at the list start still belongs to the list");
  list.scrollTop = 400;
  for (const properties of [
    { deltaX: 1 }, { deltaX: 100 }, { ctrlKey: true }, { metaKey: true }, { shiftKey: true }, { altKey: true },
    { cancelable: false }, { defaultPrevented: true }, { deltaMode: 99 }, { deltaY: NaN }, { deltaY: Infinity }, { deltaY: 0 },
  ]) {
    const event = list.emit("wheel", { deltaY: 70, ...properties });
    assert.equal(page.scrollTop, 200, JSON.stringify(properties));
    assert.equal(event.defaultPrevented, Boolean(properties.defaultPrevented));
  }
  dispose();
  const plain = fixture({ height: 500, content: 500, top: 0 });
  assert.equal(plain.list.emit("wheel", { deltaY: 60 }).defaultPrevented, false, "a list without overflow uses native page scrolling");
  assert.equal(plain.page.scrollTop, 200);
  plain.dispose();
  const refused = fixture({}, { refuse: true });
  assert.equal(refused.list.emit("wheel", { deltaY: 70 }).defaultPrevented, false, "a refused outer scroll must not swallow input");
  refused.dispose();
});

test("single-finger vertical touch relays both boundaries and releases tracking on end/cancel", () => {
  const { list, page, dispose } = fixture();
  assert.equal(list.listeners.get("touchstart").options.passive, true);
  assert.equal(list.listeners.get("touchmove").options.passive, false);
  list.emit("touchstart", { touches: [point(100, 400)] });
  assert.equal(list.emit("touchmove", { touches: [point(101, 350)] }).defaultPrevented, true);
  assert.equal(page.scrollTop, 250);
  assert.equal(list.emit("touchmove", { touches: [point(101, 320)] }).defaultPrevented, true);
  assert.equal(page.scrollTop, 280);
  list.scrollTop = 0;
  assert.equal(list.emit("touchmove", { touches: [point(101, 380)] }).defaultPrevented, true);
  assert.equal(page.scrollTop, 220);
  list.emit("touchend");
  assert.equal(list.emit("touchmove", { touches: [point(101, 430)] }).defaultPrevented, false);
  list.emit("touchstart", { touches: [point(100, 400)] });
  list.emit("touchcancel");
  assert.equal(list.emit("touchmove", { touches: [point(100, 450)] }).defaultPrevented, false);
  dispose();
});

test("touch preserves inner scrolling, horizontal gestures, pinch, modifiers and changed touch identity", () => {
  const { list, page, dispose } = fixture();
  list.scrollTop = 200;
  list.emit("touchstart", { touches: [point(100, 400)] });
  assert.equal(list.emit("touchmove", { touches: [point(100, 350)] }).defaultPrevented, false);
  assert.equal(page.scrollTop, 200);
  list.scrollTop = 400;
  list.emit("touchstart", { touches: [point(100, 400)] });
  assert.equal(list.emit("touchmove", { touches: [point(200, 398)] }).defaultPrevented, false);
  assert.equal(list.emit("touchmove", { touches: [point(200, 300)] }).defaultPrevented, false, "a gesture that began horizontally stays native");
  list.emit("touchstart", { touches: [point(100, 400), point(200, 400, 2)] });
  assert.equal(list.emit("touchmove", { touches: [point(100, 350)] }).defaultPrevented, false);
  list.emit("touchstart", { touches: [point(100, 400)] });
  list.emit("touchmove", { touches: [point(100, 350), point(200, 400, 2)] });
  assert.equal(list.emit("touchmove", { touches: [point(100, 300)] }).defaultPrevented, false, "pinch ends tracking until a new gesture");
  list.emit("touchstart", { touches: [point(100, 400)] });
  assert.equal(list.emit("touchmove", { touches: [point(100, 350, 2)] }).defaultPrevented, false);
  for (const properties of [{ ctrlKey: true }, { metaKey: true }, { altKey: true }, { shiftKey: true }, { defaultPrevented: true }]) {
    list.emit("touchstart", { touches: [point(100, 400)], ...properties });
    assert.equal(list.emit("touchmove", { touches: [point(100, 350)] }).defaultPrevented, false);
  }
  list.emit("touchstart", { touches: [point(100, 400)] });
  assert.equal(list.emit("touchmove", { touches: [point(100, 350)], cancelable: false }).defaultPrevented, false);
  assert.equal(page.scrollTop, 200);
  dispose();
});

test("touch never cancels when the page has no remaining range or refuses movement", () => {
  for (const pageOptions of [{ top: 700 }, { refuse: true }]) {
    const { list, page, dispose } = fixture({}, pageOptions);
    const before = page.scrollTop;
    list.emit("touchstart", { touches: [point(100, 400)] });
    assert.equal(list.emit("touchmove", { touches: [point(100, 350)] }).defaultPrevented, false);
    assert.equal(page.scrollTop, before);
    dispose();
  }
});

test("cleanup removes every native listener and pending touch state", () => {
  const { list, page, dispose } = fixture();
  assert.deepEqual([...list.listeners.keys()].sort(), ["touchcancel", "touchend", "touchmove", "touchstart", "wheel"]);
  list.emit("touchstart", { touches: [point(100, 400)] });
  dispose();
  assert.equal(list.listeners.size, 0);
  assert.equal(list.emit("wheel", { deltaY: 70 }).defaultPrevented, false);
  assert.equal(list.emit("touchmove", { touches: [point(100, 350)] }).defaultPrevented, false);
  assert.equal(page.scrollTop, 200);
});
