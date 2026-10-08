import { readFile } from "node:fs/promises";
import vm from "node:vm";
import ts from "typescript";

// Runs component hooks and event handlers without claiming browser or WebGL QA.
export async function componentHarness(file, imports, globals = {}, extra = "") {
  const slots = [], pending = [];
  let cursor = 0;
  const same = (a, b) => a && b && a.length === b.length && a.every((value, i) => Object.is(value, b[i]));
  const hooks = {
    lazy: loader => ({ lazy: loader }), Suspense: "suspense",
    useSyncExternalStore(_subscribe, getSnapshot) { return getSnapshot(); },
    useRef(value) { const i = cursor++; return slots[i] ??= { current: value }; },
    useState(value) {
      const i = cursor++;
      if (!slots[i]) slots[i] = { value: typeof value === "function" ? value() : value };
      return [slots[i].value, next => { slots[i].value = typeof next === "function" ? next(slots[i].value) : next; }];
    },
    useMemo(fn, deps) { const i = cursor++; if (!same(slots[i]?.deps, deps)) slots[i] = { deps, value: fn() }; return slots[i].value; },
    useCallback(fn, deps) { return hooks.useMemo(() => fn, deps); },
    useEffect(fn, deps) {
      const i = cursor++;
      if (!same(slots[i]?.deps, deps)) pending.push(() => { slots[i]?.cleanup?.(); slots[i] = { deps, cleanup: fn() }; });
    },
  };
  hooks.useLayoutEffect = hooks.useEffect;
  const jsx = (type, props) => ({ type, props });
  const exports = {};
  const code = ts.transpileModule(await readFile(file, "utf8") + extra, { compilerOptions: {
    module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022, jsx: ts.JsxEmit.ReactJSX,
  } }).outputText;
  vm.runInNewContext(code, {
    exports, console, AbortController, AbortSignal, Date, URL, Event, setTimeout, clearTimeout,
    require(name) {
      if (name === "react") return hooks;
      if (name === "react/jsx-runtime") return { jsx, jsxs: jsx, Fragment: "fragment" };
      if (name in imports) return imports[name];
      throw new Error(`Unexpected component import: ${name}`);
    }, ...globals,
  });
  return {
    exports,
    render(component, props) { cursor = 0; return component(props); },
    commit() { for (const fn of pending.splice(0)) fn(); },
    dispose() { for (const slot of slots) slot?.cleanup?.(); },
  };
}
export function findNode(node, predicate) {
  if (!node || typeof node !== "object") return;
  if (predicate(node)) return node;
  for (const child of [node.props?.children].flat(Infinity)) {
    const result = findNode(child, predicate); if (result) return result;
  }
}
export async function settle() { for (let i = 0; i < 12; i++) await Promise.resolve(); }
