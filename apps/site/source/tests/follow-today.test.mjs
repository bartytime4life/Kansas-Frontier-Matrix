import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import ts from "typescript";

const source = await readFile(new URL("../app/observatory/follow-today.ts", import.meta.url), "utf8");
const javascript = ts.transpileModule(source, { compilerOptions: { module: ts.ModuleKind.ESNext, target: ts.ScriptTarget.ES2022 } }).outputText;
const { shouldRefreshFollowToday } = await import(`data:text/javascript;base64,${Buffer.from(javascript).toString("base64")}`);

const base = { following: true, hidden: false, busy: false, lastRefreshAt: 1_000, now: 300_999, displayedDay: "2026-09-27", today: "2026-09-27" };

test("follow today refreshes a stale same-day tab on return", () => {
  assert.equal(shouldRefreshFollowToday(base), false);
  assert.equal(shouldRefreshFollowToday({ ...base, now: 301_000 }), true);
  assert.equal(shouldRefreshFollowToday({ ...base, now: 60_000, today: "2026-09-28" }), true);
});

test("follow today waits while hidden, busy, or manually browsing history", () => {
  assert.equal(shouldRefreshFollowToday({ ...base, now: 301_000, hidden: true }), false);
  assert.equal(shouldRefreshFollowToday({ ...base, now: 301_000, busy: true }), false);
  assert.equal(shouldRefreshFollowToday({ ...base, now: 301_000, following: false }), false);
  assert.equal(shouldRefreshFollowToday({ ...base, now: 301_000, lastRefreshAt: 0 }), false);
});
