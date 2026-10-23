// Synthetic transport only. No provider I/O; each route import is a new instance.
import { readFile } from "node:fs/promises";
import path from "node:path";
import { pathToFileURL } from "node:url";
import ts from "typescript";

let instance = 0;
export async function compile(file, routeSource) {
  const source = file === "app/api/hydrology/flowlines/route.ts" && routeSource !== undefined ? routeSource : await readFile(file, "utf8");
  let js = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
  for (const match of [...js.matchAll(/from "(\.[^"]+)"/g)]) js = js.replace(match[0], `from ${JSON.stringify(await compile(path.normalize(path.join(path.dirname(file), match[1])) + ".ts", routeSource))}`);
  js = js.replace('from "next/server"', `from ${JSON.stringify(pathToFileURL(path.resolve("node_modules/next/server.js")).href)}`);
  return "data:text/javascript;base64," + Buffer.from(js).toString("base64");
}
export const loadRoute = async source => (await import(await compile("app/api/hydrology/flowlines/route.ts", source) + "#instance=" + instance++)).GET;
export const request = (query = "cell=-97.25,38.00", signal = new AbortController().signal) => ({ nextUrl: new URL("https://synthetic.invalid/api/hydrology/flowlines?" + query), signal });
export const tick = () => new Promise(resolve => setImmediate(resolve));
export function deferred() { let resolve, reject; const promise = new Promise((a, b) => { resolve = a; reject = b; }); return { promise, resolve, reject }; }
export const feature = { properties: { id3dhp: "SYNTH1", flowdirection: 1, featuretype: 1, streamorder: 6 }, geometry: { type: "LineString", coordinates: [[-97.2, 38.1], [-97.19, 38.11]] } };

export function installProvider(t, handler) {
  const original = globalThis.fetch;
  t.after(() => { globalThis.fetch = original; });
  const reads = [];
  globalThis.fetch = (url, options) => {
    if (new URL(url).hostname !== "3dhp.nationalmap.gov") throw new Error("Unexpected synthetic upstream.");
    reads.push({ url: new URL(url), ...options });
    return handler(url, options, reads.length);
  };
  return reads;
}
