import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { terrainBrowserFixtures } from './terrain-detail-browser-fixtures.mjs';

// All tiles are synthetic transport fixtures, never scientific observations.
// Reuse the isolated terrain carrier, adding a uniform raster for classifications.
const PNG = 'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAM0lEQVR4nO3OMQEAMAjEwKdGu9YbIosMlouBXL2+P4udzTkAAAAAAAAAAAAAAAAAAECSDG3QArEafGnSAAAAAElFTkSuQmCC';
export async function welcomeScientificBrowserFixtures(origin) {
  const base = await terrainBrowserFixtures(origin), hits = { land: 0, crops: 0 };
  let landFailed = false;
  return { ...base, hits, failLand: () => { landFailed = true; },
    async intercept(event, call) {
      const { requestId, request } = event, url = new URL(request.url);
      const fulfill = (body, type, status = 200) => call('Fetch.fulfillRequest', { requestId, responseCode: status,
        responseHeaders: [{ name: 'Content-Type', value: type }, { name: 'Access-Control-Allow-Origin', value: '*' }], body });
      if (url.origin === origin.origin && /^\/assets\/maplibre-gl-[\w-]+\.js$/.test(url.pathname)) {
        let js = await readFile(`dist/client${url.pathname}`, 'utf8');
        const name = js.match(/([\w$]+) as Map,/)[1]; assert.ok(name);
        js += `\n;{const on=${name}.prototype.on;${name}.prototype.on=function(...args){if(this.getContainer().classList.contains('domain-stage-map'))window.__welcomeScientificMap=this;return on.apply(this,args);};}\n`;
        await fulfill(Buffer.from(js).toString('base64'), 'text/javascript'); return true;
      }
      const land = url.hostname === 'www.mrlc.gov' && url.pathname === '/geoserver/wms';
      const crops = url.origin === origin.origin && url.pathname === '/api/cropland/tile';
      if (land || crops) {
        hits[land ? 'land' : 'crops']++;
        if (land && landFailed) await fulfill(Buffer.from('Synthetic land-cover outage').toString('base64'), 'text/plain', 503);
        else await fulfill(PNG, 'image/png');
        return true;
      }
      return base.intercept(event, call);
    },
  };
}
