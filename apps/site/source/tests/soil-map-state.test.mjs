import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import typescriptCompiler from "typescript";

const source = await readFile(new URL("../app/soil-moisture.ts", import.meta.url), "utf8");
const javascript = typescriptCompiler.transpileModule(source, {
  compilerOptions: { module: typescriptCompiler.ModuleKind.ESNext, target: typescriptCompiler.ScriptTarget.ES2022 },
  fileName: "soil-moisture.ts",
}).outputText;
const soilState = await import(`data:text/javascript;base64,${Buffer.from(javascript).toString("base64")}`);

test("soil visual context participates in Hide all visibility and preserves its settings", async () => {
  const selected = { visible: true, view: "root-uncertainty", day: "2026-09-26", opacity: 0.42 };
  assert.equal(soilState.visibleExternalContextCount(0, selected.visible), 1);
  const hidden = soilState.hideSoilContext(selected);
  assert.deepEqual(hidden, { ...selected, visible: false });
  assert.equal(soilState.visibleExternalContextCount(0, hidden.visible), 0);

  const page = await readFile(new URL("../app/page.tsx", import.meta.url), "utf8");
  assert.match(page, /setSoilMapState\(current => hideSoilContext\(current\)\)/);
  assert.match(page, /disabled=\{visibleOfficialCount === 0\} onClick=\{hideAllOfficialContext\}/);
});

test("shared soil visibility, view, UTC day, and opacity restore as one map state", async () => {
  const selected = { visible: true, view: "root-uncertainty", day: "2026-09-26", opacity: 0.42 };
  const params = new URLSearchParams("c=-98.38,38.48");
  soilState.serializeSoilMapState(params, selected);
  assert.equal(params.get("soil"), "1|root-uncertainty|2026-09-26|0.42");
  assert.deepEqual(soilState.restoreSoilMapState(new URLSearchParams(params)), selected);

  const page = await readFile(new URL("../app/page.tsx", import.meta.url), "utf8");
  assert.match(page, /serializeSoilMapState\(params, soilMapState\)/);
  assert.match(page, /setSoilMapState\(restoreSoilMapState\(params\)\)/);
  assert.match(page, /state=\{soilMapState\} onChange=\{changeSoilMapState\}/);
});

test("invalid soil share state falls back safely while valid off-state settings round-trip", () => {
  assert.deepEqual(soilState.restoreSoilMapState(new URLSearchParams("soil=1%7Croot%7C2026-02-30%7C2")), soilState.DEFAULT_SOIL_MAP_STATE);
  assert.deepEqual(soilState.restoreSoilMapState(new URLSearchParams("soil=1%7CtoString%7C2026-09-26%7C")), soilState.DEFAULT_SOIL_MAP_STATE);
  const saved = { visible: false, view: "surface", day: "2026-09-26", opacity: 0.31 };
  const params = new URLSearchParams();
  soilState.serializeSoilMapState(params, saved);
  assert.deepEqual(soilState.restoreSoilMapState(params), saved);
});
