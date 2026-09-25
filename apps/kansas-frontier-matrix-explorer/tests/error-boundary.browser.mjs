/** Loopback-only browser regression fixture. Uses the real main.tsx, React and
 * recovery boundary, with synthetic route/auxiliary components. No Worker,
 * real feeds, renderer, hosted Site or production module injection is involved.
 * Run with Node, then open the printed URL in a browser; PASS/FAIL is in the DOM.
 */
import { createServer } from "node:http";
import { fileURLToPath } from "node:url";
import { build } from "vite";

const appRoot = fileURLToPath(new URL("../", import.meta.url));
const surfaces = new Map([
  ["app/page.tsx", "explorer"], ["app/about/page.tsx", "about"],
  ["app/operational-spine.tsx", "spine"], ["app/site-runtime-repair-client.tsx", "repair"],
]);
const fixtureComponent = (surface) => `
import { createElement, useEffect, useState } from 'react';
export default function Fixture() {
  const [, update] = useState(0);
  const current = window.recoveryFixture;
  useEffect(() => {
    const listener = () => update(value => value + 1);
    window.addEventListener('fixture-render', listener);
    current.active++;
    return () => { window.removeEventListener('fixture-render', listener); current.active--; };
  }, []);
  useEffect(() => {
    if (current.surface === '${surface}' && current.failing && current.kind === 'effect') throw current.error;
  });
  if (current.surface === '${surface}' && current.failing && current.kind !== 'effect') throw current.error;
  return createElement('p', { 'data-surface': '${surface}' }, '${surface}: SYNTHETIC / UNRELEASED / DENY fixture');
}`;

const result = await build({
  root: appRoot, configFile: false, logLevel: "error",
  define: { "process.env.NODE_ENV": '"production"' },
  plugins: [{
    name: "recovery-fixture-only", enforce: "pre",
    load(id) {
      const relative = id.startsWith(appRoot) ? id.slice(appRoot.length) : "";
      if (surfaces.has(relative)) return fixtureComponent(surfaces.get(relative));
      if (id.endsWith(".css")) return "";
    },
  }],
  build: { write: false, minify: false,
    lib: { entry: `${appRoot}main.tsx`, name: "RecoveryFixture", formats: ["iife"] },
  },
});
const outputs = Array.isArray(result) ? result : [result];
const bundle = outputs.flatMap(output => output.output).find(item => item.type === "chunk").code;

const fixtureSetup = `
const params = new URLSearchParams(location.search);
const surface = params.get('surface') || (location.pathname === '/about' ? 'about' : 'explorer');
const kind = params.get('kind') || 'render';
const error = kind === 'null' ? null : kind === 'undefined' ? undefined : kind === 'string' ? 'PRIVATE_THROW'
  : Object.assign(new Error('PRIVATE_MESSAGE'), {digest: kind === 'unsafe-digest' ? 'PRIVATE_TOKEN?secret=1' : 'fixture_trace-1'});
window.recoveryFixture = {surface, kind, error, failing: false, active: 0, logs: []};
const originalError = console.error;
console.error = (...args) => { window.recoveryFixture.logs.push(args); };
const stored = JSON.stringify([{id:'workspace-test',name:'Synthetic saved view',savedAt:'2026-09-25T00:00:00Z',
  view:{center:[-98.38,38.48],zoom:5.45,bearing:0,pitch:0},visibility:{'water-context':true},
  opacity:{'water-context':0.75},layerOrder:['water-context'],year:2026,basemap:'midnight',projection:'mercator',selection:null}]);
localStorage.setItem('kfm-map-workspaces-v1', stored);
`;

const assertions = `
(async () => {
  const output = document.getElementById('results');
  const fixture = window.recoveryFixture;
  const results = [];
  const assert = (value, message) => { if (!value) throw Error(message); results.push(message); };
  const waitFor = async predicate => {
    const until = performance.now() + 3000;
    while (!predicate()) {
      if (performance.now() > until) throw Error('Timed out waiting for recovery UI');
      await new Promise(resolve => setTimeout(resolve, 10));
    }
  };
  try {
    const expected = location.pathname === '/about' ? 2 : 3;
    await waitFor(() => fixture.active === expected);
    assert(document.querySelector('[data-surface="'+fixture.surface+'"]'), 'Selected surface is mounted');
    assert(document.getElementById('root').textContent.includes('SYNTHETIC / UNRELEASED / DENY'), 'Negative/provenance labels remain ordinary UI');
    fixture.failing = true;
    window.dispatchEvent(new Event('fixture-render'));
    await waitFor(() => document.querySelector('[role="alert"]') && fixture.active === 0);
    assert(document.getElementById('root').querySelectorAll('[data-surface]').length === 0, 'Failed subtree unmounted and effects cleaned up');
    await waitFor(() => document.activeElement?.id === 'kfm-error-title');
    assert(true, 'Fallback heading receives focus');
    assert(document.querySelector('a[href="/"]'), 'Return to Explorer remains available');
    assert(!document.getElementById('root').textContent.includes('PRIVATE_'), 'No raw error in fallback');
    const retry = () => [...document.querySelectorAll('#root button')].find(button => button.textContent === 'Try again');
    retry().click();
    await waitFor(() => fixture.logs.length >= 2);
    assert(document.querySelector('[role="alert"]'), 'Repeated failure returns to the fallback without automatic retries');
    fixture.failing = false;
    retry().click();
    await waitFor(() => fixture.active === expected && !document.querySelector('[role="alert"]'));
    assert(document.querySelector('[data-surface="'+fixture.surface+'"]'), 'Explicit retry remounts selected route');
    assert(localStorage.getItem('kfm-map-workspaces-v1') === stored, 'Saved workspace bytes survive failure and retry');
    assert(document.getElementById('root').textContent.includes('SYNTHETIC / UNRELEASED / DENY'), 'Provenance and denial survive recovery');
    assert(fixture.logs.length === 2, 'One diagnostic per failed render; no retry loop');
    assert(fixture.logs.every(args => args.length === 2 && args[0] === '[KFM UI error boundary]'
      && args[1].code === 'KFM-UI-UNEXPECTED-ERROR'
      && Object.keys(args[1]).sort().join(',') === 'code,correlationId'), 'React root emits only safe diagnostics');
    assert(!JSON.stringify(fixture.logs).includes('PRIVATE_'), 'Raw exception and stack excluded from diagnostic arguments');
    output.textContent = 'PASS: '+surface+' / '+kind+' — '+results.length+' assertions\\n'+results.join('\\n');
    output.dataset.result = 'PASS';
  } catch (error) {
    output.textContent = 'FAIL: '+surface+' / '+kind+' — '+error.message+'\\n'+results.join('\\n');
    output.dataset.result = 'FAIL';
  } finally { console.error = originalError; }
})();
`;

const server = createServer((request, response) => {
  if (request.method !== "GET") { response.writeHead(405).end(); return; }
  if (request.url === "/fixture.js") {
    response.writeHead(200, { "Content-Type": "text/javascript", "Cache-Control": "no-store" }).end(bundle);
    return;
  }
  response.writeHead(200, {
    "Content-Type": "text/html", "Cache-Control": "no-store",
    "Content-Security-Policy": "default-src 'none'; script-src 'self' 'unsafe-inline'; connect-src 'none'; style-src 'unsafe-inline'",
  }).end(`<!doctype html><html lang="en"><meta charset="utf-8"><title>KFM recovery fixture</title>
<h1>Local synthetic recovery regression</h1><pre id="results">RUNNING</pre><div id="root"></div>
<script>${fixtureSetup}</script><script src="/fixture.js"></script><script>${assertions}</script></html>`);
});
server.listen(0, "127.0.0.1", () => {
  console.log(`Recovery fixture: http://127.0.0.1:${server.address().port}/`);
  console.log("Use /about for About; ?surface=spine or ?surface=repair for auxiliary UI.");
  console.log("Failure kinds: render, effect, null, undefined, string, unsafe-digest. Ctrl+C stops the server.");
});
for (const signal of ["SIGINT", "SIGTERM"]) process.once(signal, () => server.close());
