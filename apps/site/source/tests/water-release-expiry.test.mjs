import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const source = await readFile(new URL("../app/water-release-expiry.ts", import.meta.url), "utf8");
const compiled = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const { expiryText, expiryWarning, REFRESH_WARNING_MS } = await import("data:text/javascript;base64," + Buffer.from(compiled).toString("base64"));

const EXPIRES = "2026-10-18T19:00:00Z";
const active = { active_package_id: "sha256:" + "a".repeat(64), decision_expires_at: EXPIRES };
const at = (offsetMs) => Date.parse(EXPIRES) - offsetMs;
const HOUR = 3_600_000;

test("an open page moves from quiet to warning to expired as the clock advances", () => {
  // The same status read once, judged at three later times.
  assert.equal(expiryWarning(active, at(5 * 24 * HOUR)), null);
  assert.match(expiryText(active, at(5 * 24 * HOUR)), /in 5 days/);
  assert.match(expiryWarning(active, at(REFRESH_WARNING_MS)), /expires soon/);
  assert.match(expiryText(active, at(30 * HOUR)), /in 30 hours/);
  assert.match(expiryWarning(active, at(0)), /has expired/);
  assert.match(expiryText(active, at(-1)), /expired; the layer is not serving/);
});

test("no active package or no readable expiry shows nothing to act on", () => {
  for (const status of [null, { active_package_id: null, decision_expires_at: EXPIRES }, { ...active, decision_expires_at: null }, { ...active, decision_expires_at: "not a date" }]) {
    assert.equal(expiryText(status, at(0)), "–");
    assert.equal(expiryWarning(status, at(0)), null);
  }
});
