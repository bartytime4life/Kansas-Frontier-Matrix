import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import { isolateBrowserNetwork } from './browser-network.mjs';

// Disposable browser instrumentation only: never installed in the application.
export function installRenderDiagnostics(Map) {
  const state=window.__kfmRenderDiagnostics={maps:[],calls:[],longTasks:[],errors:[]};
  new PerformanceObserver(list=>state.longTasks.push(...list.getEntries().map(e=>({at:e.startTime,ms:e.duration})))).observe({type:'longtask',buffered:true});
  const sources=new WeakMap(),programs=new WeakMap();
  const gl=WebGL2RenderingContext.prototype;
  const source=gl.shaderSource,attach=gl.attachShader;
  gl.shaderSource=function(shader,text){sources.set(shader,text.includes('u_crest')||text.includes('a_ground')?'curtain':'renderer');return source.call(this,shader,text);};
  gl.attachShader=function(program,shader){if(sources.get(shader)==='curtain')programs.set(program,'curtain');return attach.call(this,program,shader);};
  for(const name of ['compileShader','linkProgram','getShaderParameter','getProgramParameter','deleteProgram']){
    const original=gl[name];
    gl[name]=function(object,...args){const at=performance.now();try{return original.call(this,object,...args);}finally{
      state.calls.push({name,owner:sources.get(object)??programs.get(object)??'renderer',at,ms:performance.now()-at});
    }};
  }
  const identify=map=>{
    let entry=state.maps.find(entry=>entry.map===map);
    if(!entry){entry={map,kind:map.getContainer().classList.contains('domain-stage-map')?'preview':'explorer',styles:0,renders:0,removed:false};state.maps.push(entry);
      map.on('style.load',()=>{entry.styles++;});map.on('render',()=>{entry.renders++;});map.on('error',e=>state.errors.push(String(e.error?.message??e.message)));}
    return entry;
  };
  for(const name of ['setStyle','setTerrain','setProjection','remove']){
    const original=Map.prototype[name];
    Map.prototype[name]=function(...args){const entry=identify(this),at=performance.now();try{return original.apply(this,args);}finally{
      state.calls.push({name,owner:entry.kind,at,ms:performance.now()-at});if(name==='remove')entry.removed=true;
    }};
  }
}

export function renderPerformanceFixtures(origin) {
  return {
    async isolate(call,base,options){
      await isolateBrowserNetwork(call,base,options);
      await call('Fetch.enable',{patterns:[{urlPattern:`${origin.origin}/api/*`},{urlPattern:`${origin.origin}/assets/maplibre-gl-*.js`}]});
    },
    async intercept({requestId,request},call){
      const url=new URL(request.url);
      if(url.origin!==origin.origin||!/^\/assets\/maplibre-gl-[\w-]+\.js$/.test(url.pathname))return false;
      let js=await readFile(`dist/client${url.pathname}`,'utf8');
      const name=js.match(/([\w$]+) as Map,/)?.[1];assert.ok(name,'instrument the built Map class');
      js+=`\n;(${installRenderDiagnostics.toString()})(${name});\n`;
      await call('Fetch.fulfillRequest',{requestId,responseCode:200,responseHeaders:[{name:'Content-Type',value:'text/javascript'}],body:Buffer.from(js).toString('base64')});return true;
    },
  };
}
