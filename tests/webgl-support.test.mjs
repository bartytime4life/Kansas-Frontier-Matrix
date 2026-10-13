import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

// Each import gets a fresh module instance so the page-level cache starts empty.
const source = ts.transpileModule(await readFile(new URL("../app/webgl-support.ts", import.meta.url), "utf8"), {
  compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
}).outputText;
let instance = 0;
const freshModule = () => import(`data:text/javascript;base64,${Buffer.from(`${source}\n// ${instance++}`).toString("base64")}`);

const withCanvas = async (getContext, run) => {
  const created = [];
  globalThis.document = { createElement: (tag) => { created.push(tag); return { getContext }; } };
  try { await run(created); } finally { delete globalThis.document; }
};

test("a successful WebGL2 probe is made once per page, not once per map mount", async () => {
  const { webgl2Available } = await freshModule();
  await withCanvas(() => ({}), async (created) => {
    for (let mount = 0; mount < 20; mount += 1) assert.equal(webgl2Available(), true);
    assert.deepEqual(created, ["canvas"]);
  });
});

test("an unavailable probe is retried, since it holds no context and the GPU may recover", async () => {
  const { webgl2Available } = await freshModule();
  let available = false;
  await withCanvas(() => (available ? {} : null), async (created) => {
    assert.equal(webgl2Available(), false);
    assert.equal(webgl2Available(), false);
    available = true;
    assert.equal(webgl2Available(), true);
    assert.equal(webgl2Available(), true);
    assert.equal(created.length, 3);
  });
});

test("a throwing getContext reports WebGL2 as unavailable", async () => {
  const { webgl2Available } = await freshModule();
  await withCanvas(() => { throw new Error("GPU process crashed"); }, async () => {
    assert.equal(webgl2Available(), false);
  });
});
