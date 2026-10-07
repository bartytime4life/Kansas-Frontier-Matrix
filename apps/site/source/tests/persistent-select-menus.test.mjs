import assert from "node:assert/strict";
import test from "node:test";
import { componentHarness, findNode } from "./component-harness.mjs";

async function harness() {
  const listeners = {}, attrs = {}, events = [];
  const focused = [];
  class Element { closest() { return this; } }
  class Group extends Element {}
  class Select extends Element {
    _value = "a"; disabled = false; isConnected = true; multiple = false; size = 0;
    options = [{ value: "a", label: "A" }, { value: "b", label: "B" }, { value: "c", label: "Unavailable", disabled: true }];
    get value() { return this._value; } set value(value) { this._value = value; }
    get selectedIndex() { return this.options.findIndex(option => option.value === this.value); }
    getClientRects() { return [1]; } getBoundingClientRect() { return { width: 200, left: 20, top: 30, bottom: 70 }; }
    getAttribute(name) { return attrs[name] ?? null; } setAttribute(name, value) { attrs[name] = value; } removeAttribute(name) { delete attrs[name]; }
    focus() { focused.push(this); } dispatchEvent(event) { events.push(event.type); }
  }
  const select = new Select();
  const h = await componentHarness("app/persistent-select-menus.tsx", {
    "react-dom": { createPortal: node => node },
  }, { Element, Node: Element, HTMLSelectElement: Select, HTMLOptGroupElement: Group,
    document: { body: {}, addEventListener: (name, fn) => { listeners[name] = fn; }, removeEventListener() {} },
    window: { innerWidth: 800, innerHeight: 600, addEventListener() {}, removeEventListener() {} },
  });
  const render = () => { const tree = h.render(h.exports.PersistentSelectMenus, {}); h.commit(); return tree; };
  render();
  listeners.pointerdown({ target: select, preventDefault() {} });
  return { h, select, listeners, events, render, focused: () => focused.at(-1), attrs };
}
test("Escape dismisses the dropdown before a surrounding panel can consume it", async () => {
  const t = await harness(); let prevented = false, stopped = false;
  assert.equal(t.attrs["aria-expanded"], "true");
  t.listeners.keydown({ target: t.select, key: "Escape", preventDefault() { prevented = true; }, stopImmediatePropagation() { stopped = true; } });
  assert.equal(prevented, true); assert.equal(stopped, true);
  assert.equal(t.render(), null); assert.equal(t.attrs["aria-expanded"], "false");
  t.h.dispose();
});
test("pointer choices keep focus in the owning modal and disabled choices cannot become active", async () => {
  const t = await harness(); const tree = t.render();
  const enabled = findNode(tree, n => n.props?.role === "option" && n.props.children === "B");
  let prevented = false; enabled.props.onPointerDown({ preventDefault() { prevented = true; } });
  assert.equal(prevented, true); assert.equal(enabled.props.tabIndex, -1); assert.equal(t.focused(), t.select);
  findNode(tree, n => n.props?.disabled).props.onPointerEnter();
  assert.equal(t.attrs["aria-activedescendant"], "site-persistent-select-menu-option-0");
  enabled.props.onClick();
  assert.equal(t.select.value, "b"); assert.deepEqual(t.events, ["input", "change"]); assert.equal(t.focused(), t.select);
  t.h.dispose();
});
test("options disabled after opening cannot change the underlying select", async () => {
  const t = await harness(); const tree = t.render(); t.select.options[1].disabled = true;
  findNode(tree, n => n.props?.role === "option" && n.props.children === "B").props.onClick();
  assert.equal(t.select.value, "a"); assert.deepEqual(t.events, []); assert.equal(t.render(), null);
  t.h.dispose();
});
