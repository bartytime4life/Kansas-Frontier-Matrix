import assert from 'node:assert/strict';
import {readFile} from 'node:fs/promises';
import {isolateBrowserNetwork} from './browser-network.mjs';

// Executed only inside a disposable browser response. Keep native attribution
// creation, source updates and removal; add the empty credit source to every
// welcome style, including inline styles absent from the network fetch fixture.
export function installWelcomeAttributionFixture(Map, style) {
  const setStyle=Map.prototype.setStyle,addControl=Map.prototype.addControl;
  const state=map=>{
    const current=window.__welcomeCreditFixture;
    if(current?.map===map)return current;
    return window.__welcomeCreditFixture={map,control:null,node:null,styles:[]};
  };
  Map.prototype.setStyle=function(value,...options){
    if(value!==null&&this.getContainer().classList.contains('domain-stage-map')){
      const trace=state(this);if(trace.styles.length<32)trace.styles.push({input:typeof value,at:Math.round(performance.now())});
      const fixture=structuredClone(value&&typeof value==='object'?value:style);
      fixture.sources={...fixture.sources,'test-attribution':structuredClone(style.sources['test-attribution'])};
      fixture.layers=[...(fixture.layers??[]).filter(layer=>layer.id!=='test-attribution-layer'),structuredClone(style.layers.find(layer=>layer.id==='test-attribution-layer'))];
      return setStyle.call(this,fixture,...options);
    }
    return setStyle.call(this,value,...options);
  };
  Map.prototype.addControl=function(control,...options){
    const result=addControl.call(this,control,...options);
    if(this.getContainer().classList.contains('domain-stage-map')&&control._container?.classList.contains('maplibregl-ctrl-attrib')){
      Object.assign(state(this),{control,node:control._container});
    }
    return result;
  };
}

export function welcomeAttributionBrowserFixtures(origin,attribution){
  const style={version:8,sources:{'test-attribution':{type:'geojson',data:{type:'FeatureCollection',features:[]},attribution}},layers:[{id:'test-background',type:'background',paint:{'background-color':'#172832'}},{id:'test-attribution-layer',type:'circle',source:'test-attribution',paint:{'circle-opacity':0}}]};
  return {attribution,
    async isolate(call,base,options){
      await isolateBrowserNetwork(call,base,options);
      await call('Fetch.enable',{patterns:[{urlPattern:`${origin.origin}/api/*`},{urlPattern:`${origin.origin}/assets/maplibre-gl-*.js`}]});
    },
    async intercept({requestId,request},call){
      const url=new URL(request.url);
      if(url.origin!==origin.origin||!/^\/assets\/maplibre-gl-[\w-]+\.js$/.test(url.pathname))return false;
      let js=await readFile(`dist/client${url.pathname}`,'utf8');
      const name=js.match(/([\w$]+) as Map,/)?.[1];assert.ok(name,'instrument the built Map class in this disposable response only');
      js+=`\n;(${installWelcomeAttributionFixture.toString()})(${name},${JSON.stringify(style)});\n`;
      await call('Fetch.fulfillRequest',{requestId,responseCode:200,responseHeaders:[{name:'Content-Type',value:'text/javascript'}],body:Buffer.from(js).toString('base64')});return true;
    },
  };
}
