import test from 'node:test';
import assert from 'node:assert/strict';
import {execFileSync} from 'node:child_process';
import {installSkyRenderObserver} from './kansas-sky-render-observer.mjs';

const install=process.env.KFM_SKY_OBSERVER_BASELINE ? MapClass=>{
  const source=execFileSync('git',['show','5d45a7365d18339348153e603e6f2442b76b66c7:tests/kansas-sky.browser.mjs'],{encoding:'utf8'});
  const line=source.split('\n').find(line=>line.includes('const add=${name}.prototype.addLayer')&&line.includes('window.__skyRender='));
  assert.ok(line);const code=new Function('name',`let js='';${line};return js;`)('MapClass');
  new Function('window','MapClass',code)(window,MapClass);
}:installSkyRenderObserver;

function observe(render,assertions){
  const previous=globalThis.window;globalThis.window={};
  class FakeMap{addLayer(layer){this.layer=layer;return this;}}
  let program='aircraft',buffer='planes';const calls=[];
  const gl={TRIANGLES:4,LINES:1,CURRENT_PROGRAM:1,ARRAY_BUFFER_BINDING:2,VERTEX_ATTRIB_ARRAY_STRIDE:3,VERTEX_ATTRIB_ARRAY_BUFFER_BINDING:4,
    getParameter:key=>key===1?program:buffer,
    getAttribLocation:(_,name)=>name==='a_position'?0:name==='a_edge'&&program==='stroke'?1:-1,
    getVertexAttrib:(_,key)=>key===3?24:buffer,
    drawArrays:(...args)=>calls.push(args),bufferSubData(){},
  };
  const draw=gl.drawArrays,upload=gl.bufferSubData;
  try{
    install(FakeMap);const map=new FakeMap();map.addLayer({id:'kfm-kansas-sky',render:context=>render(context,value=>{program=value;buffer=value==='stroke'?'paths':'planes';})});
    assertions({run:()=>map.layer.render(gl),stats:window.__skyRender,gl,calls});
    assert.equal(gl.drawArrays,draw);assert.equal(gl.bufferSubData,upload,'observer restores WebGL methods');
  }finally{if(previous===undefined)delete globalThis.window;else globalThis.window=previous;}
}

test('real aircraft and stroked path draws remain distinct; terrain guides do not establish a route',()=>{
  observe((gl,program)=>{const data=new Float32Array(6*6);for(let i=2;i<data.length;i+=6)data[i]=1230;gl.bufferSubData(0,0,data);gl.drawArrays(gl.TRIANGLES,0,6);program('stroke');gl.drawArrays(gl.TRIANGLES,0,12);gl.drawArrays(gl.TRIANGLES,0,12);gl.drawArrays(gl.TRIANGLES,12,18);},({run,stats,calls})=>{
    run();assert.equal(stats.aircraftVertices,6);assert.equal(stats.pathTriangles,24);assert.equal(stats.trailVertices,24);assert.equal(stats.maxZ,1230);assert.equal(stats.frames,1);assert.equal(calls.length,4,'observer forwards every real draw');
  });
});
test('a retained route cannot masquerade as an aircraft during an observation gap',()=>{
  observe((gl,program)=>{program('stroke');gl.drawArrays(gl.TRIANGLES,0,12);},({run,stats})=>{run();assert.equal(stats.aircraftVertices,0);assert.equal(stats.pathTriangles,12);});
});
test('ordinary line fallback is observed, while guides alone do not establish path triangles',()=>{
  observe((gl,program)=>{gl.drawArrays(gl.LINES,100,2);program('stroke');gl.drawArrays(gl.TRIANGLES,12,18);},({run,stats})=>{run();assert.equal(stats.aircraftVertices,0);assert.equal(stats.lineTrailVertices,2);assert.equal(stats.pathTriangles,0);});
});
test('observer propagates renderer failures and restores interception methods',()=>{
  observe(()=>{throw new Error('fixture shader failure');},({run,stats})=>{assert.throws(run,/fixture shader failure/);assert.equal(stats.frames,0);});
});
