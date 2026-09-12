import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";

const compileModule = async (path, fileName) => {
  const ts = await import("typescript");
  const source = await readFile(new URL(path, import.meta.url), "utf8");
  const javascript = ts.transpileModule(source, {
    compilerOptions: {
      module: ts.ModuleKind.ESNext,
      target: ts.ScriptTarget.ES2022,
    },
    fileName,
  }).outputText;
  return import(`data:text/javascript;base64,${Buffer.from(javascript).toString("base64")}`);
};

test("canonicalizes opacity overrides and fails invalid trust deep links closed", async () => {
  const repair = await compileModule("../app/site-runtime-repair.ts", "site-runtime-repair.ts");
  const layers = [
    { id: "alpha", defaultOpacity: 0.5 },
    { id: "beta", defaultOpacity: 0.4 },
  ];
  const invalid = repair.canonicalizeExplorerUrl(
    "https://example.invalid/explorer?o=unknown:0.90,alpha:0.50,beta:0.82&ws=trust&f=missing&panel=evidence&drawer=open&focusStage=outcome&focusIntent=explain",
    layers,
    () => false,
  );

  assert.equal(invalid.searchParams.get("o"), "beta:0.82");
  assert.equal(invalid.searchParams.get("ws"), "explore");
  for (const parameter of ["f", "panel", "drawer", "focusStage", "focusIntent"]) {
    assert.equal(invalid.searchParams.has(parameter), false);
  }

  const valid = repair.canonicalizeExplorerUrl(
    "https://example.invalid/explorer?o=alpha:0.51&ws=trust&f=known",
    layers,
    (featureId) => featureId === "known",
  );
  assert.equal(valid.searchParams.get("o"), "alpha:0.51");
  assert.equal(valid.searchParams.get("ws"), "trust");
  assert.equal(valid.searchParams.get("f"), "known");
});

test("redacts private coordinates from assistive status text", async () => {
  const repair = await compileModule("../app/site-runtime-repair.ts", "site-runtime-repair.ts");
  const status = "Renderer acquisition is held. Map center 38.3666° N, 97.7836° W. 7 layers visible. No feature selected.";
  const redacted = repair.redactScreenReaderStatus(status);

  assert.match(redacted, /Map center private camera, coordinates redacted\./);
  assert.doesNotMatch(redacted, /38\.3666|97\.7836/);
});

test("mounts the bounded client repair from the root layout", async () => {
  const layout = await readFile(new URL("../app/layout.tsx", import.meta.url), "utf8");
  const client = await readFile(new URL("../app/site-runtime-repair-client.tsx", import.meta.url), "utf8");

  assert.match(layout, /import SiteRuntimeRepair from "\.\/site-runtime-repair-client"/);
  assert.match(layout, /<SiteRuntimeRepair \/>/);
  assert.match(client, /new MutationObserver\(scheduleSync\)/);
  assert.match(client, /window\.history\.replaceState/);
  assert.match(client, /runtime-degraded-banner/);
  assert.match(client, /aria-label="Open degraded-runtime guide"/);
  assert.match(client, /window\.dispatchEvent\(new PopStateEvent/);
});
