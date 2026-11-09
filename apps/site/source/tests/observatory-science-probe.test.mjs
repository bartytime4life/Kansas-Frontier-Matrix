import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";
import { findNode } from "./component-harness.mjs";

// Execute the actual callbacks and JSX without loading providers or claiming browser QA.
const source = await readFile("app/observatory/workspace.tsx", "utf8");
const ast = ts.createSourceFile("workspace.tsx", source, ts.ScriptTarget.ES2022, true, ts.ScriptKind.TSX);
const declarations = new Map(), effects = [];
let pointerCallback, readout, launcher, toolbar;
function visit(node) {
  if (ts.isVariableDeclaration(node) && ts.isIdentifier(node.name) && node.initializer) declarations.set(node.name.text,node.initializer.getText(ast));
  if (ts.isCallExpression(node) && node.expression.getText(ast)==="useEffect") effects.push(node.arguments[0].getText(ast));
  if (ts.isCallExpression(node) && node.expression.getText(ast)==="map.on" && node.arguments[0]?.text==="click") pointerCallback=node.arguments[1].getText(ast);
  if (ts.isJsxElement(node)) {
    const attrs=node.openingElement.attributes.properties;
    if(attrs.some(a=>a.name?.getText(ast)==="className"&&a.initializer?.text==="event-science-probe-readout"))readout=node.parent.getText(ast);
    if(node.openingElement.tagName.getText(ast)==="button"){
      if(node.getText(ast).includes("<b>↔ Distance + bearing</b>"))launcher=node.getText(ast);
      if(attrs.some(a=>a.name?.getText(ast)==="ref"&&a.initializer?.expression?.getText(ast)==="scienceLabTriggerRef"))toolbar=node.getText(ast);
    }
  }
  ts.forEachChild(node,visit);
}
visit(ast);
const focusEffect=effects.find(value=>value.includes('map.on("moveend", updateCenter)'));
const scienceSource=await readFile("app/science-events.ts","utf8");
const scienceJs=ts.transpileModule(scienceSource,{compilerOptions:{module:ts.ModuleKind.ESNext,target:ts.ScriptTarget.ES2022}}).outputText;
const science=await import("data:text/javascript;base64,"+Buffer.from(scienceJs).toString("base64"));
const jsx=(type,props)=>({type,props});
function evaluate(expression,bindings){
  assert.ok(expression,"actual source expression exists");
  const compiled=ts.transpileModule("const result=("+expression+");",{compilerOptions:{module:ts.ModuleKind.CommonJS,target:ts.ScriptTarget.ES2022,jsx:ts.JsxEmit.ReactJSX}}).outputText;
  return new Function(...Object.keys(bindings),compiled+"return result;")(...Object.values(bindings));
}
const textOf=node=>typeof node==="string"||typeof node==="number"?String(node):!node||typeof node!=="object"?"":[node.props?.children].flat(Infinity).map(textOf).join("");
const button=(tree,label)=>findNode(tree,node=>node.type==="button"&&textOf(node)===label);

function harness({mapReady=true,reduced=false}={}){
  const state={mapReady,reduced,scienceProbeActive:false,scienceProbePoints:[],scienceProbeCenter:null,scienceOpen:true,layersOpen:false,detailsOpen:false,calendarOpen:false,playing:true};
  const focusCalls=[],listeners=new Map(),body={name:"body"},document={body,activeElement:body};
  const focusable=name=>({name,isConnected:true,focus(options){focusCalls.push({name,options});document.activeElement=this;}});
  const trigger=focusable("science-toolbar"),origin=focusable("distance-launcher"),centerButton=focusable("center-button"),canvas=focusable("map-canvas"),outside=focusable("query-input");
  const center={lng:-98,lat:38};
  const map={getCenter:()=>center,getCanvas:()=>canvas,on:(type,fn)=>listeners.set(type,fn),off:(type,fn)=>{assert.equal(listeners.get(type),fn);listeners.delete(type);},queryRenderedFeatures:()=>[],getLayer:()=>undefined,easeTo(){assert.fail("probe must not animate the camera");},flyTo(){assert.fail("probe must not move the camera");}};
  const refs={mapRef:{current:map},scienceProbeActiveRef:{current:false},scienceLabTriggerRef:{current:trigger},scienceProbeCenterButtonRef:{current:centerButton},scienceProbeReadoutRef:{current:{contains:node=>node===centerButton}},scienceProbeFocusOriginRef:{current:null}};
  const setter=key=>value=>{state[key]=typeof value==="function"?value(state[key]):value;};
  const base=()=>({...state,...refs,document,exports:{},useCallback:fn=>fn,
    setPlaying:setter("playing"),setScienceProbePoints:setter("scienceProbePoints"),setScienceProbeCenter:setter("scienceProbeCenter"),setScienceProbeActive:setter("scienceProbeActive"),
    setScienceOpen:setter("scienceOpen"),setLayersOpen:setter("layersOpen"),setDetailsOpen:setter("detailsOpen"),setCalendarOpen:setter("calendarOpen"),
    require:name=>{assert.equal(name,"react/jsx-runtime");return {jsx,jsxs:jsx,Fragment:"fragment"};},
    SCIENCE_EVENTS:science.SCIENCE_EVENTS,compassPoint:()=> "E",
  });
  const bindings=()=>{
    const b=base();
    for(const name of ["readScienceProbeCenter","appendScienceProbePoint","restoreScienceProbeFocus","beginScienceProbe","addScienceProbeCenter","panScienceProbeMap","finishScienceProbe","clearScienceProbe"])b[name]=evaluate(declarations.get(name),b);
    b.probeMeasurement=science.scienceMeasurement(state.scienceProbePoints);
    return b;
  };
  const begin=(detail=0)=>{document.activeElement=origin;bindings().beginScienceProbe({detail,currentTarget:origin});};
  return {state,refs,map,center,document,trigger,origin,centerButton,canvas,outside,focusCalls,listeners,bindings,begin,
    render:()=>evaluate(readout,bindings()),launcher:()=>evaluate(launcher,bindings()),toolbar:()=>evaluate(toolbar,bindings()),
    commitFocus:()=>evaluate(focusEffect,bindings())(),escape:()=>evaluate(declarations.get("key"),bindings())({key:"Escape"}),
    pointer:coordinate=>evaluate(pointerCallback,{...bindings(),map})({lngLat:{lng:coordinate[0],lat:coordinate[1]},point:{x:0,y:0}}),
  };
}

test("keyboard center controls complete A/B measurement with labeled coordinates and no camera animation",()=>{
  for(const reduced of [false,true]){
    const h=harness({reduced});h.begin();
    h.origin.isConnected=false;h.document.activeElement=h.document.body;
    const cleanup=h.commitFocus();assert.equal(h.document.activeElement,h.centerButton);
    let tree=h.render(),a=button(tree,"Use map center for point A");
    assert.equal(a.props.type,"button");assert.equal(a.props.disabled,false);
    assert.equal(a.props["aria-describedby"],"science-probe-center science-probe-instructions");
    assert.match(textOf(tree),/Map center: latitude 38\.0000, longitude -98\.0000/);
    a.props.onClick();tree=h.render();assert.match(textOf(tree),/Point A: latitude 38\.0000, longitude -98\.0000/);
    button(tree,"Pan map with keyboard").props.onClick();assert.equal(h.document.activeElement,h.canvas);
    h.center.lng=-97;h.listeners.get("moveend")();tree=h.render();
    assert.match(textOf(tree),/Map center: latitude 38\.0000, longitude -97\.0000/);
    button(tree,"Use map center for point B").props.onClick();tree=h.render();
    assert.equal(h.state.scienceProbePoints.length,2);assert.ok(science.scienceMeasurement(h.state.scienceProbePoints).miles>53);
    assert.match(textOf(tree),/Point B: latitude 38\.0000, longitude -97\.0000/);
    assert.match(textOf(findNode(tree,node=>node.props?.role==="status")),/mi.*km.*°/);
    assert.match(textOf(tree),/approximate, not survey or evidence/);
    h.center.lng=-96;button(tree,"Use map center for new point A").props.onClick();
    assert.deepEqual(h.state.scienceProbePoints,[[-96,38]]);
    cleanup();assert.equal(h.listeners.size,0);
  }
});

test("pointer input retains append, third-point restart, and pause behavior alongside center input",()=>{
  const h=harness();h.begin(1);
  const cleanup=h.commitFocus();assert.equal(h.focusCalls.length,0,"pointer launch must not autofocus another control");
  h.pointer([-98,38]);h.pointer([-97,38]);assert.deepEqual(h.state.scienceProbePoints,[[-98,38],[-97,38]]);
  h.pointer([-96,39]);assert.deepEqual(h.state.scienceProbePoints,[[-96,39]]);assert.equal(h.state.playing,false);
  h.bindings().finishScienceProbe();h.pointer([-95,40]);assert.deepEqual(h.state.scienceProbePoints,[[-96,39]]);
  cleanup();
});

test("keyboard launch respects a newer focus choice and cancellation before its effect commits",()=>{
  for(const cancelled of [false,true]){
    const h=harness();h.begin();h.origin.isConnected=false;h.document.activeElement=h.outside;
    if(cancelled)h.bindings().finishScienceProbe();
    const cleanup=h.commitFocus();assert.equal(h.document.activeElement,h.outside);assert.equal(h.focusCalls.length,0);
    cleanup?.();
  }
});

test("Done, Clear and Escape return probe-owned focus while toolbar switches retain their clicked focus",()=>{
  for(const action of ["Done","Clear","Escape"]){
    const h=harness();h.begin();const cleanup=h.commitFocus();
    h.document.activeElement=h.centerButton;
    if(action==="Escape")h.escape();else button(h.render(),action).props.onClick();
    assert.equal(h.document.activeElement,h.trigger);assert.equal(h.state.scienceProbeActive,false);assert.equal(h.refs.scienceProbeFocusOriginRef.current,null);
    cleanup();
  }
  const h=harness();h.begin();const cleanup=h.commitFocus();h.document.activeElement=h.outside;
  h.escape();assert.equal(h.document.activeElement,h.outside,"Escape cannot steal focus from a different task");
  h.begin();h.document.activeElement=h.outside;h.bindings().finishScienceProbe();assert.equal(h.document.activeElement,h.outside);
  h.begin();h.document.activeElement=h.trigger;h.toolbar().props.onClick();
  assert.equal(h.document.activeElement,h.trigger);assert.equal(h.state.scienceOpen,true);assert.equal(h.state.scienceProbeActive,false);
  cleanup();
});

test("unavailable or invalid centers cannot add endpoints and unavailable maps cannot start the tool",()=>{
  const unavailable=harness({mapReady:false});assert.equal(unavailable.launcher().props.disabled,true);
  unavailable.begin();assert.equal(unavailable.state.scienceProbeActive,false);assert.equal(unavailable.render(),false);
  const h=harness();h.begin();const cleanup=h.commitFocus();
  for(const center of [{lng:NaN,lat:38},{lng:-98,lat:91},{lng:181,lat:38}]){
    Object.assign(h.center,center);h.listeners.get("moveend")();const tree=h.render();
    assert.equal(button(tree,"Use map center for point A").props.disabled,true);assert.match(textOf(tree),/Map center is unavailable/);
    button(tree,"Use map center for point A").props.onClick();assert.equal(h.state.scienceProbePoints.length,0);
  }
  h.refs.mapRef.current=null;h.bindings().addScienceProbeCenter();assert.equal(h.state.scienceProbePoints.length,0);
  cleanup();
});

test("Done retains completed points, Edit resumes keyboard entry, and Clear removes the readout",()=>{
  const h=harness();h.begin();let cleanup=h.commitFocus();
  h.pointer([-98,38]);h.pointer([-97,38]);h.document.activeElement=h.centerButton;
  button(h.render(),"Done").props.onClick();cleanup();let tree=h.render();
  assert.equal(h.state.scienceProbePoints.length,2);assert.ok(button(tree,"Edit"));assert.equal(button(tree,"Pan map with keyboard"),undefined);
  h.document.activeElement=h.origin;button(tree,"Edit").props.onClick({detail:0,currentTarget:h.origin});
  cleanup=h.commitFocus();assert.equal(h.document.activeElement,h.centerButton);
  button(h.render(),"Clear").props.onClick();assert.equal(h.render(),false);assert.deepEqual(h.state.scienceProbePoints,[]);
  cleanup();
});
