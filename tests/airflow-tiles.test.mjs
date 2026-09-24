import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const source = await readFile(new URL("../app/airflow-tiles.ts", import.meta.url), "utf8");
const output = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const airflow = await import(`data:text/javascript;base64,${Buffer.from(output).toString("base64")}`);

test("airflow tiles use the fixed NWS wind-barb layer and only Kansas tile coordinates", () => {
  const upstream = new URL(airflow.airflowTileRequest(new URL("https://local.test/api/airflow-tile?z=5&x=7&y=12")));
  assert.equal(upstream.origin, "https://digital.weather.gov");
  assert.equal(upstream.searchParams.get("LAYERS"), "ndfd.conus.windspd.windbarbs");
  assert.equal(upstream.searchParams.get("SRS"), "EPSG:3857");
  assert.throws(() => airflow.airflowTileRequest(new URL("https://local.test/api/airflow-tile?z=5&x=7&y=12&url=https://other.test")));
  assert.throws(() => airflow.airflowTileRequest(new URL("https://local.test/api/airflow-tile?z=5&x=0&y=0")));
});

test("airflow tile failures return an unavailable response without substituted imagery", async () => {
  const request = new Request("https://local.test/api/airflow-tile?z=5&x=7&y=12");
  const result = await airflow.serveAirflowTile(request, async () => new Response("<ServiceException/>", { headers: { "Content-Type": "text/xml" } }));
  assert.equal(result.status, 502);
  assert.equal(result.headers.get("Cache-Control"), "no-store");
  const oversized = await airflow.serveAirflowTile(request, async () => new Response(new Uint8Array(512_001), { headers: { "Content-Type": "image/png" } }));
  assert.equal(oversized.status, 502);
});
