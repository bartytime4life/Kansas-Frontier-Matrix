import assert from "node:assert/strict";
import test from "node:test";
import { componentHarness, findNode, settle } from "./component-harness.mjs";

const labels = { submitted:"Submitted", under_review:"In review", changes_requested:"Changes requested", accepted:"Accepted for preparation", rejected:"Declined" };
const submission = id => ({ id, title:`Submission ${id}`, sourceId:"general", ownerName:"Synthetic contributor", description:"Synthetic source for component tests only.", fileName:"fixture.csv", fileBytes:10, fileSha256:"fixture", status:"submitted", version:1, createdAt:"2026-01-01", updatedAt:"2026-01-01", sourceUrl:"", license:"Unknown", sensitivity:"unknown", startDate:"", endDate:"" });
const detail = (id, status="submitted", version=1) => ({ submission:{...submission(id),status,version}, reviews:version > 1 ? [{id:`review-${version}`,reviewerName:"Synthetic steward",status,previousStatus:"submitted",note:`Persisted fixture review ${version}`,version,createdAt:"2026-01-02"}] : [], canReview:true });
const response = (body,status=200) => ({ok:status>=200&&status<300,status,json:async()=>body});
const deferred = () => {let resolve,reject;const promise=new Promise((done,fail)=>{resolve=done;reject=fail;});return {promise,resolve,reject};};
const textOf = node => typeof node==="string"||typeof node==="number" ? String(node) : node&&typeof node==="object" ? [node.props?.children].flat(Infinity).map(textOf).join(" ").replace(/\s+/g," ") : "";
const button = (tree,text) => findNode(tree,node=>node.type==="button"&&node.props.children===text);
const item = (tree,id) => findNode(tree,node=>node.type==="button"&&findNode(node,child=>child.type==="strong"&&child.props.children===`Submission ${id}`));
const panel = tree => findNode(tree,node=>node.type==="section"&&node.props["aria-label"]==="Submission details");
const note = tree => findNode(panel(tree),node=>node.type==="textarea");
const decision = tree => findNode(panel(tree),node=>node.type==="select");
const form = tree => findNode(panel(tree),node=>node.type==="form");
const writeNote = (tree,value) => note(tree).props.onChange({target:{value}});
async function setup(dispatch) {
  const calls=[];
  const h=await componentHarness("app/data/workspace.tsx",{
    "next/link":{default:"a"}, "../data-intake":{DATA_SOURCES:[{id:"general",title:"General fixture"}],MAX_UPLOAD_BYTES:100,REVIEW_LABELS:labels,UPLOAD_EXTENSIONS:["csv"]}, "./workspace.module.css":{default:{}},
  },{URLSearchParams,fetch:(url,options={})=>{calls.push({url,options});return dispatch(url,options);}});
  const render=()=>{const tree=h.render(h.exports.default,{mode:"review",name:"Synthetic steward",steward:true});h.commit();return tree;};
  render();await settle();let tree=render();item(tree,"A").props.onClick();await settle();tree=render();
  return {h,render,calls,tree};
}
const list = () => response({items:[submission("A"),submission("B")],nextCursor:null});

test("a late review acknowledgement keeps a newer selection or closed panel and identifies its original target",async()=>{
  for(const action of ["select","close"]){
    const patch=deferred();let aReads=0;
    const {h,render,calls,tree:initial}=await setup((url,options)=>options.method==="PATCH"?patch.promise:Promise.resolve(url.includes("?")?list():response(detail(url.endsWith("/A")?(aReads++,"A"):"B"))));
    writeNote(initial,"  Submitted note for A.  ");let tree=render();const pending=form(tree).props.onSubmit({preventDefault(){}});tree=render();
    if(action==="select"){item(tree,"B").props.onClick();await settle();tree=render();writeNote(tree,"New unsaved note for B.");}
    else button(tree,"Close").props.onClick();
    patch.resolve(response({status:"under_review",version:2}));await pending;await settle();tree=render();
    assert.match(textOf(tree),/Review recorded for Submission A · version 2/);assert.match(textOf(tree),/Submitted note for A\./);
    assert.equal(aReads,1,"acknowledgement does not reopen the former selection");
    if(action==="select"){assert.match(textOf(panel(tree)),/Submission B/);assert.equal(note(tree).props.value,"New unsaved note for B.");}
    else assert.equal(panel(tree),undefined);
    assert.deepEqual(JSON.parse(calls.find(call=>call.options.method==="PATCH").options.body),{status:"under_review",note:"  Submitted note for A.  ",version:1});
    h.dispose();
  }
});

test("acknowledgement and fresh history preserve newer edits in the same submission",async()=>{
  const patch=deferred(),fresh=deferred();let reads=0;
  const {h,render,tree:initial}=await setup((url,options)=>options.method==="PATCH"?patch.promise:url.includes("?")?Promise.resolve(list()):++reads===1?Promise.resolve(response(detail("A"))):fresh.promise);
  writeNote(initial,"  The submitted review note.  ");let tree=render();const pending=form(tree).props.onSubmit({preventDefault(){}});
  writeNote(tree,"A later unsaved working note.");decision(tree).props.onChange({target:{value:"rejected"}});tree=render();
  patch.resolve(response({status:"under_review",version:2}));await settle();tree=render();
  assert.equal(note(tree).props.value,"A later unsaved working note.");assert.equal(decision(tree).props.value,"rejected");
  assert.match(textOf(tree),/In review · The submitted review note\./);assert.equal(button(tree,"Save review").props.disabled,false,"saving ends at acknowledgement, independently of a pending history refresh");
  fresh.resolve(response(detail("A","under_review",2)));await pending;tree=render();
  assert.equal(note(tree).props.value,"A later unsaved working note.");assert.equal(decision(tree).props.value,"rejected");assert.match(textOf(panel(tree)),/Persisted fixture review 2/);
  h.dispose();
});

test("returning to the same submission before acknowledgement advances only its status/version and preserves the new draft",async()=>{
  const patch=deferred(),payloads=[];
  const {h,render,tree:initial}=await setup((url,options)=>{
    if(options.method==="PATCH"){payloads.push(JSON.parse(options.body));return payloads.length===1?patch.promise:Promise.resolve(response({status:"rejected",version:3}));}
    return Promise.resolve(url.includes("?")?list():response(detail(url.endsWith("/B")?"B":"A")));
  });
  writeNote(initial,"The first submitted review note.");const pending=form(render()).props.onSubmit({preventDefault(){}});let tree=render();item(tree,"B").props.onClick();await settle();tree=render();item(tree,"A").props.onClick();await settle();tree=render();
  writeNote(tree,"A new draft after returning to A.");decision(tree).props.onChange({target:{value:"rejected"}});
  patch.resolve(response({status:"under_review",version:2}));await pending;tree=render();
  assert.equal(note(tree).props.value,"A new draft after returning to A.");assert.equal(decision(tree).props.value,"rejected");assert.ok(findNode(panel(tree),node=>node.props?.["data-state"]==="under_review"));
  await form(tree).props.onSubmit({preventDefault(){}});assert.equal(payloads[1].version,2);h.dispose();
});

test("failed or older refreshes keep the acknowledged version and note, and the next write uses that version",async()=>{
  for(const failure of ["http","network","older"]){
    let reads=0,writes=0;const payloads=[];
    const {h,render,tree:initial}=await setup((url,options)=>{
      if(options.method==="PATCH"){payloads.push(JSON.parse(options.body));return Promise.resolve(response({status:++writes===1?"under_review":"changes_requested",version:writes+1}));}
      if(url.includes("?"))return Promise.resolve(list());
      if(++reads===1)return Promise.resolve(response(detail("A")));
      if(reads>2)return Promise.resolve(response(detail("A","changes_requested",3)));
      return failure==="network"?Promise.reject(new TypeError("Synthetic network error")):Promise.resolve(failure==="http"?response({error:"Unavailable"},503):response(detail("A")));
    });
    writeNote(initial,"Recorded note survives refresh failure.");let tree=render();await form(tree).props.onSubmit({preventDefault(){}});tree=render();
    assert.match(textOf(tree),/Review recorded for Submission A · version 2/);assert.match(textOf(tree),/Recorded note survives refresh failure/);
    assert.match(textOf(findNode(tree,node=>node.props?.role==="alert")),/review was recorded, but refreshed details/);
    assert.doesNotMatch(textOf(panel(tree)),/Awaiting a steward’s first review/);
    assert.ok(findNode(panel(tree),node=>node.props?.["data-state"]==="under_review"));
    writeNote(tree,"The next review uses the acknowledged version.");tree=render();await form(tree).props.onSubmit({preventDefault(){}});
    assert.equal(payloads[1].version,2);h.dispose();
  }
});

test("an older in-flight history refresh cannot downgrade a subsequent acknowledged review",async()=>{
  const older=deferred();let reads=0,writes=0;
  const {h,render,tree:initial}=await setup((url,options)=>{
    if(options.method==="PATCH")return Promise.resolve(response({status:++writes===1?"under_review":"changes_requested",version:writes+1}));
    if(url.includes("?"))return Promise.resolve(list());
    return ++reads===1?Promise.resolve(response(detail("A"))):reads===2?older.promise:Promise.resolve(response(detail("A","changes_requested",3)));
  });
  writeNote(initial,"First recorded working review.");let tree=render();const first=form(tree).props.onSubmit({preventDefault(){}});await settle();tree=render();
  writeNote(tree,"Second recorded working review.");tree=render();await form(tree).props.onSubmit({preventDefault(){}});tree=render();
  older.resolve(response(detail("A","under_review",2)));await first;tree=render();
  assert.match(textOf(tree),/Submission A · version 3/);assert.ok(findNode(panel(tree),node=>node.props?.["data-state"]==="changes_requested"));assert.match(textOf(panel(tree)),/Persisted fixture review 3/);
  h.dispose();
});

test("rejected writes retain the draft and do not claim an acknowledgement or refresh details",async()=>{
  let reads=0;
  const {h,render,tree:initial}=await setup((url,options)=>Promise.resolve(options.method==="PATCH"?response({error:"Another steward updated this submission. Reload it before reviewing."},409):url.includes("?")?list():(reads++,response(detail("A")))));
  writeNote(initial,"Keep this unsaved review note.");let tree=render();await form(tree).props.onSubmit({preventDefault(){}});tree=render();
  assert.equal(note(tree).props.value,"Keep this unsaved review note.");assert.match(textOf(tree),/Another steward updated/);assert.doesNotMatch(textOf(tree),/Review recorded for/);assert.equal(reads,1);assert.equal(button(tree,"Save review").props.disabled,false);h.dispose();
});

test("reopening a submission cannot accept details older than its acknowledged review",async()=>{
  let reads=0;
  const {h,render,tree:initial}=await setup((url,options)=>Promise.resolve(options.method==="PATCH"?response({status:"under_review",version:2}):url.includes("?")?list():++reads===2?response({error:"Unavailable"},503):response(detail("A",reads>3?"under_review":"submitted",reads>3?2:1))));
  writeNote(initial,"Preserve the acknowledged review across reopening.");await form(render()).props.onSubmit({preventDefault(){}});let tree=render();
  item(tree,"A").props.onClick();await settle();tree=render();assert.equal(note(tree),undefined);assert.match(textOf(tree),/could not be confirmed against the recorded review/);assert.match(textOf(tree),/Submission A · version 2/);
  item(tree,"A").props.onClick();await settle();tree=render();assert.ok(note(tree));assert.ok(findNode(panel(tree),node=>node.props?.["data-state"]==="under_review"));h.dispose();
});

test("unmount ignores a late write acknowledgement without dispatching follow-up reads",async()=>{
  const patch=deferred();
  const {h,render,calls,tree:initial}=await setup((url,options)=>options.method==="PATCH"?patch.promise:Promise.resolve(url.includes("?")?list():response(detail("A"))));
  writeNote(initial,"No late updates after disposal.");const pending=form(render()).props.onSubmit({preventDefault(){}});const before=textOf(render()),count=calls.length;
  h.dispose();patch.resolve(response({status:"under_review",version:2}));await pending;await settle();assert.equal(calls.length,count);assert.equal(textOf(render()),before);
});
