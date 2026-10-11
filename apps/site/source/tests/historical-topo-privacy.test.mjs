import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const source = await readFile(new URL("../app/historical-topo-control.tsx", import.meta.url), "utf8");
const tree = ts.createSourceFile("control.tsx", source, ts.ScriptTarget.Latest, true, ts.ScriptKind.TSX);
let initializer, requestEffect;
const walk = node => {
  if (ts.isVariableDeclaration(node) && node.name.getText(tree) === "[search, setSearch]") initializer = node.initializer.arguments[0];
  if (ts.isCallExpression(node) && node.expression.getText(tree) === "useEffect" && !requestEffect) requestEffect = node.arguments[0];
  ts.forEachChild(node, walk);
};
walk(tree);
assert.ok(initializer && requestEffect);
const compile = node => ts.transpileModule(`const callback = ${node.getText(tree)};`, {compilerOptions:{target:ts.ScriptTarget.ES2022}}).outputText;
const initialize = new Function("map", "locationPrivate", `${compile(initializer)}; return callback();`);
const execute = values => new Function(...Object.keys(values), `${compile(requestEffect)}; return callback();`)(...Object.values(values));

test("held historical search never retains private coordinates for a later Fit Kansas request", async () => {
  let reads = 0;
  const map = {getCenter: () => {reads++; return {lng:-97.1234567,lat:38.7654321};}};
  const search = initialize(map,true);
  assert.equal(reads,0,"private camera is never captured");
  const urls = [];
  const values = {search,locationPrivate:true,AbortController,URLSearchParams,
    setLoading:()=>{},setError:()=>{},setRows:()=>{},setMore:()=>{},setRetrievedAt:()=>{},
    browserJsonRequest:async url=>{urls.push(url);return {response:{ok:true},body:{state:"available",sheets:[],more:false,retrievedAt:"fixture"}};}};
  assert.equal(execute(values),undefined);
  await new Promise(resolve=>setImmediate(resolve));
  assert.deepEqual(urls,[],"private request remains held");
  const cleanup = execute({...values,locationPrivate:false});
  await new Promise(resolve=>setImmediate(resolve));
  assert.equal(urls.length,1);
  const query = new URL(urls[0],"http://fixture.invalid").searchParams;
  assert.equal(query.get("lng"),"-98.4");
  assert.equal(query.get("lat"),"38.5");
  assert.ok(!urls[0].includes("97.1234567") && !urls[0].includes("38.7654321"));
  cleanup();
});

test("ordinary historical searches retain the deliberately selected public map center", () => {
  const search = initialize({getCenter:()=>({lng:-95.68,lat:39.05})},false);
  assert.equal(search.lng,-95.68);
  assert.equal(search.lat,39.05);
});
