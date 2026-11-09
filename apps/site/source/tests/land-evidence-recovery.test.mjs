import assert from "node:assert/strict";
import test from "node:test";
import { componentHarness, findNode, settle } from "./component-harness.mjs";

const record = id => ({record_digest:`sha256:${id}`,source_id:"fixture",source_record_id:`Record ${id}`,event_date:"1901-01-01",county:"Reno",instrument_type:"patent",transaction_status:"reported",parties:[],flags:[]});
const submission = id => ({id,title:`Bundle ${id}`,sourceId:"land-records",fileBytes:100,status:"submitted",startDate:"1901-01-01",endDate:"1901-01-01"});
const detail = (id="A",selected=null,evidence=[]) => ({submission:submission(id),records:[record("one"),record("two")],total:2,nextCursor:null,summary:{uniqueRecords:2,captures:1,bytes:100,sources:["fixture"],counties:["Reno"],kinds:["patent"],start:"1901-01-01",end:"1901-01-01",transferDigest:"fixture"},selected,evidence,reviews:[],canReview:false,integrity:"VERIFIED"});
const evidence = id => ({record_digest:`sha256:${id}`,bundle_digest:`bundle-${id}`,retrieved_at:`fixture evidence ${id}`,capture_method:"selected_export",locators:[],source_url:"https://example.test/evidence",coverage:{scope:"selected_export"},members:[],documents:[]});
const response = (body,status=200) => ({ok:status>=200&&status<300,status,json:async()=>body});
const deferred = () => {let resolve,reject;const promise=new Promise((done,fail)=>{resolve=done;reject=fail;});return {promise,resolve,reject};};
const textOf = node => typeof node==="string"||typeof node==="number" ? String(node) : node&&typeof node==="object" ? [node.props?.children].flat(Infinity).map(textOf).join(" ") : "";
const button = (tree,text) => findNode(tree,node=>node.type==="button"&&node.props.children===text);
const recordButton = (tree,id) => findNode(tree,node=>node.type==="button"&&findNode(node,child=>child.type==="small"&&child.props.children===`Record ${id}`));
const bundleButton = (tree,id) => findNode(tree,node=>node.type==="button"&&findNode(node,child=>child.type==="strong"&&child.props.children===`Bundle ${id}`));
const evidencePanel = tree => findNode(tree,node=>node.type==="section"&&findNode(node,child=>child.type==="h2"&&textOf(child)==="Record & evidence"));
function clock(){const timers=new Map();let id=0;return {timers,globals:{setTimeout:(fn,delay)=>{const key=++id;timers.set(key,{fn,delay});return key;},clearTimeout:key=>timers.delete(key)},expire(){const timer=timers.values().next().value;assert.ok(timer);assert.equal(timer.delay,15_000);timer.fn();}};}
async function setup(dispatch,time=clock()){
  const calls=[],document={activeElement:null};
  const h=await componentHarness("app/data/land-records/workspace.tsx",{
    "next/link":{default:"a"},"../../land-records":{LAND_SOURCES:{fixture:{title:"Synthetic fixture source",href:"https://example.test/",limitation:"Component fixture only"}}},"../../data-intake":{REVIEW_LABELS:{submitted:"Submitted"}},"../workspace.module.css":{default:{}},"./workspace.module.css":{default:{}},
  },{URLSearchParams,document,window:{history:{replaceState(){}}},...time.globals,fetch:(url,options={})=>{
    calls.push({url,options});
    if(!url.includes("?record="))return Promise.resolve(response(url.startsWith("/api/land-records?")?{items:[submission("A"),submission("B")],nextCursor:null}:detail(url.includes("/B?")?"B":"A")));
    return dispatch(url,options);
  }});
  const render=()=>{const tree=h.render(h.exports.default,{name:"Synthetic contributor",steward:true,initialId:"A"});h.commit();return tree;};
  render();await settle();const tree=render();
  const select=(id,trigger={id:`trigger-${id}`})=>{document.activeElement=trigger;recordButton(render(),id).props.onClick({currentTarget:trigger});return trigger;};
  return {h,render,calls,document,time,tree,select};
}

test("access, missing, integrity, storage and network failures end loading with plain recovery guidance and a working retry",async()=>{
  for(const [status,guide] of [[401,/Sign in again with ChatGPT/],[403,/contributor or assigned steward account/],[404,/Refresh the bundle or choose another/],[409,/could not be verified or has changed/],[413,/exceeds the supported size/],[503,/storage is temporarily unavailable/],["network",/Check your connection and retry/]]){
    const retried=deferred();let reads=0;
    const {h,render,time,select}=await setup(()=>++reads===1?(status==="network"?Promise.reject(new TypeError("PRIVATE_BACKEND_LABEL")):Promise.resolve(response({error:"PRIVATE_BACKEND_LABEL"},status))):retried.promise);
    select("one");let tree=render();assert.match(textOf(evidencePanel(tree)),/Checking original evidence/);assert.doesNotMatch(textOf(tree),/no original evidence/);
    await settle();tree=render();assert.match(textOf(findNode(evidencePanel(tree),node=>node.props?.role==="alert")),guide);assert.doesNotMatch(textOf(evidencePanel(tree)),/Checking original evidence|PRIVATE_BACKEND_LABEL|no original evidence/);
    const retry=button(tree,"Retry evidence check");assert.equal(Boolean(retry.props.disabled),false);const trigger={id:"retry"};retry.props.onClick({currentTarget:trigger});tree=render();
    assert.match(textOf(evidencePanel(tree)),/Checking original evidence/);assert.equal(findNode(evidencePanel(tree),node=>node.props?.role==="alert"),undefined);
    retried.resolve(response(detail("A",record("one"),[evidence("one")])));await settle();tree=render();
    assert.match(textOf(evidencePanel(tree)),/fixture evidence one/);assert.doesNotMatch(textOf(evidencePanel(tree)),/Checking original evidence|Retry evidence/);assert.equal(time.timers.size,0);h.dispose();
  }
});

test("a matching verified response with no evidence is a terminal empty result",async()=>{
  const {h,render,select}=await setup(()=>Promise.resolve(response(detail("A",record("one")))));
  select("one");await settle();const tree=render();assert.match(textOf(evidencePanel(tree)),/verified bundle returned no original evidence for this record/);assert.doesNotMatch(textOf(evidencePanel(tree)),/Checking original evidence|Retry evidence/);assert.equal(findNode(evidencePanel(tree),node=>node.props?.role==="alert"),undefined);h.dispose();
});

test("evidence must confirm the requested bundle, record, integrity and evidence identity before display",async()=>{
  const mutations=[body=>body.submission.id="B",body=>body.selected=record("two"),body=>delete body.integrity,body=>body.evidence=[evidence("two")]];
  for(const mutate of mutations){
    const body=detail("A",record("one"),[evidence("one")]);mutate(body);
    const {h,render,select}=await setup(()=>Promise.resolve(response(body)));select("one");await settle();const tree=render();
    assert.match(textOf(evidencePanel(tree)),/could not be verified or has changed/);assert.doesNotMatch(textOf(evidencePanel(tree)),/fixture evidence one|fixture evidence two|verified bundle returned no original evidence/);assert.ok(button(tree,"Retry evidence check"));h.dispose();
  }
});

test("stalled headers and bodies reach a finite deadline, allow retry and ignore late adapters",async()=>{
  for(const stage of ["headers","body"]){
    const late=deferred();let signal,reads=0;
    const {h,render,time,select}=await setup((_url,options)=>{
      signal=options.signal;if(++reads>1)return Promise.resolve(response(detail("A",record("one"),[evidence("one")])));
      return stage==="headers"?late.promise:Promise.resolve({ok:true,status:200,json:()=>late.promise});
    });
    select("one");await settle();time.expire();await settle();let tree=render();assert.equal(signal.aborted,true);assert.equal(time.timers.size,0);assert.match(textOf(evidencePanel(tree)),/check took too long/);
    button(tree,"Retry evidence check").props.onClick({currentTarget:{id:"retry"}});await settle();tree=render();assert.match(textOf(evidencePanel(tree)),/fixture evidence one/);
    const old=detail("A",record("one"),[{...evidence("one"),retrieved_at:"late obsolete evidence"}]);late.resolve(stage==="headers"?response(old):old);await settle();tree=render();assert.doesNotMatch(textOf(evidencePanel(tree)),/late obsolete evidence|check took too long/);h.dispose();
  }
});

test("changing record aborts the former read and cannot display its evidence or steal focus",async()=>{
  const first=deferred(),second=deferred(),signals=[];
  const {h,render,select,document,time}=await setup((_url,options)=>{signals.push(options.signal);return signals.length===1?first.promise:second.promise;});
  select("one");let tree=render();let focuses=0;findNode(evidencePanel(tree),node=>node.type==="h2").props.ref.current={focus(){focuses++;}};
  const trigger=select("two");await settle();tree=render();assert.equal(signals[0].aborted,true);assert.equal(time.timers.size,1);
  first.resolve(response(detail("A",record("one"),[evidence("one")])));await settle();tree=render();assert.doesNotMatch(textOf(evidencePanel(tree)),/fixture evidence one/);assert.equal(focuses,0);
  document.activeElement={id:"newer-field"};second.resolve(response(detail("A",record("two"),[evidence("two")])));await settle();tree=render();
  assert.match(textOf(evidencePanel(tree)),/fixture evidence two/);assert.notEqual(document.activeElement,trigger);assert.equal(focuses,0);assert.equal(time.timers.size,0);h.dispose();
});

test("bundle, filter and access-scope changes cancel evidence and suppress late results",async()=>{
  for(const action of ["bundle","filter","access"]){
    const late=deferred();let signal;
    const {h,render,select,time}=await setup((_url,options)=>{signal=options.signal;return late.promise;});select("one");let tree=render();
    if(action==="bundle")bundleButton(tree,"B").props.onClick();
    else if(action==="filter")findNode(tree,node=>node.type==="form"&&findNode(node,child=>child.type==="button"&&child.props.children==="Apply filters")).props.onSubmit({preventDefault(){}});
    else findNode(tree,node=>node.type==="input"&&node.props.type==="checkbox"&&"checked" in node.props).props.onChange({target:{checked:true}});
    tree=render();await settle();tree=render();assert.equal(signal.aborted,true);assert.equal(time.timers.size,0);assert.equal(evidencePanel(tree),undefined);
    late.resolve(response(detail("A",record("one"),[evidence("one")])));await settle();tree=render();assert.equal(evidencePanel(tree),undefined);assert.doesNotMatch(textOf(tree),/fixture evidence one/);h.dispose();
  }
});

test("focus follows a completed matching selection only while its initiating control still owns focus",async()=>{
  for(const moved of [false,true]){
    const pending=deferred();const {h,render,select,document}=await setup(()=>pending.promise);
    const trigger=select("one");let tree=render(),focuses=0;const heading={focus(){focuses++;document.activeElement=heading;}};findNode(evidencePanel(tree),node=>node.type==="h2").props.ref.current=heading;
    if(moved)document.activeElement={id:"newer-input"};pending.resolve(response(detail("A",record("one"),[evidence("one")])));await settle();tree=render();
    assert.equal(focuses,moved?0:1);assert.equal(document.activeElement===heading,!moved);if(moved)assert.notEqual(document.activeElement,trigger);h.dispose();
  }
});

test("the pending retry remains focusable and restart aborts the old read before focusing the matching result",async()=>{
  const old=deferred(),fresh=deferred(),signals=[];
  const {h,render,select,document,time}=await setup((_url,options)=>{signals.push(options.signal);return signals.length===1?Promise.resolve(response({error:"Unavailable"},503)):signals.length===2?old.promise:fresh.promise;});
  select("one");await settle();let tree=render();const trigger={id:"retry"};document.activeElement=trigger;button(tree,"Retry evidence check").props.onClick({currentTarget:trigger});tree=render();
  const restart=button(tree,"Restart evidence check");assert.equal(Boolean(restart.props.disabled),false,"the initiating retry must retain browser focus while pending");
  let focuses=0;findNode(evidencePanel(tree),node=>node.type==="h2").props.ref.current={focus(){focuses++;}};
  restart.props.onClick({currentTarget:trigger});await settle();assert.equal(signals[1].aborted,true);assert.equal(time.timers.size,1);
  fresh.resolve(response(detail("A",record("one"),[evidence("one")])));await settle();tree=render();assert.equal(focuses,1);assert.match(textOf(evidencePanel(tree)),/fixture evidence one/);assert.equal(time.timers.size,0);
  old.resolve(response(detail("A",record("one"),[{...evidence("one"),retrieved_at:"obsolete retry"}])));await settle();tree=render();assert.equal(focuses,1);assert.doesNotMatch(textOf(evidencePanel(tree)),/obsolete retry/);h.dispose();
});

test("unmount promptly clears full-read deadlines and ignores late header/body completions",async()=>{
  for(const stage of ["headers","body"]){
    const late=deferred();let signal;
    const {h,render,select,time}=await setup((_url,options)=>{signal=options.signal;return stage==="headers"?late.promise:Promise.resolve({ok:true,status:200,json:()=>late.promise});});
    select("one");await settle();const before=textOf(render());h.dispose();await settle();assert.equal(signal.aborted,true);assert.equal(time.timers.size,0);
    const body=detail("A",record("one"),[evidence("one")]);late.resolve(stage==="headers"?response(body):body);await settle();assert.equal(textOf(h.render(h.exports.default,{name:"Synthetic contributor",steward:true,initialId:"A"})),before);
  }
});
