// Loopback-only transport fixtures. The application, MapLibre, source records,
// attribution control and terrain mesh are real; elevation pixels are synthetic.
import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import ts from 'typescript';

export async function terrainBrowserFixtures(origin, { fail3dep = true } = {}) {
  const compiled = { exports: {} };
  const source = await readFile('app/3dep-dem-tiles.ts', 'utf8');
  new Function('exports', 'require', ts.transpileModule(source, {
    compilerOptions: { module: ts.ModuleKind.CommonJS, target: ts.ScriptTarget.ES2022 },
  }).outputText)(compiled.exports, () => ({}));
  const pixels = Float32Array.from({ length: 256 * 256 }, (_, index) =>
    450 + 80 * Math.sin(2 * Math.PI * (index % 256) / 255) * Math.sin(2 * Math.PI * Math.floor(index / 256) / 255));
  const png = Buffer.from(await compiled.exports.lercToTerrarium(new Uint8Array(32), () => ({ width: 256, height: 256, pixels: [pixels] }))).toString('base64');
  const hits = { mapzen: 0, usgs: 0, instrumented: 0 };
  let failure = fail3dep;
  const mapzen = 'https://s3.amazonaws.com/elevation-tiles-prod/terrarium/';
  return {
    hits, fail3dep: value => { failure = value; }, waitTimeoutMs: 45000,
    async isolate(call) {
      // Catch every request before network I/O, including workers. This fixture
      // also runs on older Chromium versions without CDP allow-list patterns.
      await call('Fetch.enable', { patterns: [{ urlPattern: '*' }] });
    },
    async setup(call) {
      await call('Page.addScriptToEvaluateOnNewDocument', { source: `window.__terrainAcceptanceAnnouncements=[];new MutationObserver(()=>{const text=document.querySelector('.toast')?.textContent;if(text&&!window.__terrainAcceptanceAnnouncements.includes(text))window.__terrainAcceptanceAnnouncements.push(text);}).observe(document,{subtree:true,childList:true,characterData:true});` });
    },
    async intercept({ requestId, request }, call) {
      const url = new URL(request.url);
      const fulfill = (body, type, status = 200) => call('Fetch.fulfillRequest', {
        requestId, responseCode: status, responseHeaders: [
          { name: 'Content-Type', value: type }, { name: 'Access-Control-Allow-Origin', value: '*' },
        ], body,
      });
      if (url.origin === origin.origin && /^\/assets\/maplibre-gl-[\w-]+\.js$/.test(url.pathname)) {
        let js = await readFile(`dist/client${url.pathname}`, 'utf8');
        const name = js.match(/([\w$]+) as Map,/)[1];
        assert.ok(name, 'instrument the actual built Map class, only in this disposable browser response');
        js += `\n;{const original=${name}.prototype.on;${name}.prototype.on=function(...args){if(this.getContainer().id==='map-canvas')window.__terrainAcceptanceMap=this;return original.apply(this,args);};}\n`;
        await fulfill(Buffer.from(js).toString('base64'), 'text/javascript'); hits.instrumented++;
        return true;
      }
      const usgs = url.origin === origin.origin && url.pathname === '/api/3dep-dem-tile';
      if (usgs || request.url.startsWith(mapzen)) {
        hits[usgs ? 'usgs' : 'mapzen']++;
        if (usgs && failure) await fulfill(Buffer.from('Synthetic 3DEP outage').toString('base64'), 'text/plain', 503);
        else await fulfill(png, 'image/png');
        return true;
      }
      if (url.origin !== origin.origin && /^https?:$/.test(url.protocol)) {
        const style = url.pathname.includes('/styles/') || url.pathname.endsWith('/style.json');
        const body = style ? JSON.stringify({ version: 8, sources: {}, layers: [{ id: 'test-background', type: 'background', paint: { 'background-color': '#172832' } }] }) : 'Unrelated provider isolated in synthetic terrain test';
        await fulfill(Buffer.from(body).toString('base64'), style ? 'application/json' : 'text/plain', style ? 200 : 503);
        return true;
      }
      return false;
    },
  };
}
