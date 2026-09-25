import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const source = await readFile(new URL("../app/catalog-source-roles.ts", import.meta.url), "utf8");
const compiled = ts.transpileModule(source, {
  compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 },
  fileName: "catalog-source-roles.ts",
}).outputText;
const { catalogSourceRoles, layerHasSourceRole } = await import(`data:text/javascript;base64,${Buffer.from(compiled).toString("base64")}`);

const layer = (...roles) => ({ data: { features: roles.map((sourceRole) => ({ properties: { sourceRole } })) } });

test("source roles remain exact and are sorted without collapsing synthetic roles", () => {
  const layers = [layer("observed", "synthetic aggregate", "observed"), layer(" aggregate ", "")];
  assert.deepEqual(catalogSourceRoles(layers), ["aggregate", "observed", "synthetic aggregate"]);
  assert.equal(layerHasSourceRole(layers[0], "aggregate"), false);
  assert.equal(layerHasSourceRole(layers[0], "synthetic aggregate"), true);
  assert.equal(layerHasSourceRole(layers[1], "observed"), false);
  assert.equal(layerHasSourceRole(layers[1], "ALL"), true);
  assert.equal(layerHasSourceRole(layer(), "observed"), false);
});

test("catalog control and function record retain the bounded scope", async () => {
  const page = await readFile(new URL("../app/page.tsx", import.meta.url), "utf8");
  const registry = await readFile(new URL("../app/function-registry.ts", import.meta.url), "utf8");
  assert.match(page, /Catalog source role/);
  assert.match(page, /layerHasSourceRole\(layer, catalogSourceRole\)/);
  assert.match(page, /setCatalogSourceRole\("ALL"\)/);
  assert.match(registry, /id: "filter-source-role",[\s\S]*?maturity: "PARTIAL"/);
});
