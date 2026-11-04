import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { terrainBrowserFixtures } from './terrain-detail-browser-fixtures.mjs';

// All tiles are synthetic transport fixtures, never scientific observations.
// Reuse the isolated terrain carrier, adding a uniform raster for classifications.
const PNG = 'iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAAAM0lEQVR4nO3OMQEAMAjEwKdGu9YbIosMlouBXL2+P4udzTkAAAAAAAAAAAAAAAAAAECSDG3QArEafGnSAAAAAElFTkSuQmCC';
export async function welcomeScientificBrowserFixtures(origin) {
  const base = await terrainBrowserFixtures(origin), hits = { land: 0, crops: 0, animals: 0 };
  let landFailed = false, animalsFailed = false;
  return { ...base, hits, failLand: () => { landFailed = true; }, failAnimals: () => { animalsFailed = true; },
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
      if(url.origin===origin.origin && url.pathname==='/api/live-context' && ['census-counties','deflock-alpr'].includes(url.searchParams.get('feed'))){
        const feed=url.searchParams.get('feed'), county=feed==='census-counties';
        const west=county?-95.95:-97.35, south=county?38.95:37.65, size=county?.3:.05;
        const data={feed,state:'ready',data:{type:'FeatureCollection',features:[{type:'Feature',properties:county?{geoid:'20177',name:'Synthetic county',population:1234}:{featureId:'synthetic-report-cell',name:'Synthetic report cell',reportCount:3},geometry:{type:'Polygon',coordinates:[[[west,south],[west+size,south],[west+size,south+size],[west,south+size],[west,south]]]}}]}};
        await fulfill(Buffer.from(JSON.stringify(data)).toString('base64'),'application/json');return true;
      }
      const animals = url.origin===origin.origin && url.pathname==='/api/event-atlas/tile' && url.searchParams.get('kind')==='fauna';
      if(animals){hits.animals++;await fulfill(animalsFailed?Buffer.from('Synthetic GBIF outage').toString('base64'):PNG,animalsFailed?'text/plain':'image/png',animalsFailed?503:200);return true;}
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
