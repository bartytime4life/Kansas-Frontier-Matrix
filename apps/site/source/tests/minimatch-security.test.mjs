import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { createRequire } from "node:module";
import test from "node:test";

const require = createRequire(import.meta.url);
// Resolve from the affected consumer, never the legacy minimatch used by ESLint.
const parserRequire = createRequire(require.resolve("@typescript-eslint/typescript-estree"));
const parserMatcher = parserRequire.resolve("minimatch");

function isolatedMatcherCheck(source) {
  const result = spawnSync(process.execPath, ["--max-old-space-size=128", "-e", `
    const assert = require("node:assert/strict");
    const { Minimatch, minimatch } = require(process.argv[1]);
    ${source}
  `, parserMatcher], { timeout: 10_000, maxBuffer: 64 * 1024, encoding: "utf8" });
  assert.equal(result.error, undefined, result.error?.message);
  assert.equal(result.signal, null, `matcher terminated: ${result.signal}`);
  assert.equal(result.status, 0, result.stderr || result.stdout);
}

test("parser minimatch bounds globparts amplification at the requested expansion limit", () => {
  isolatedMatcherCheck(`
    // Eight segments keep the vulnerable baseline bounded to 256 alternatives.
    // The patched optimizer must respect the cap for both forms, not just braces.
    for (const pattern of [
      Array(8).fill("**/../a/b").join("/"),
      "src/" + Array(8).fill("**/../c/d").join("/") + "/file.ts",
    ]) {
      const matcher = new Minimatch(pattern, { optimizationLevel: 2, braceExpandMax: 32 });
      assert.ok(matcher.set.length <= 32, "globparts exceeded braceExpandMax: " + matcher.set.length);
    }
  `);
});

test("large alternative sets avoid quadratic deduplication and retain matching semantics", () => {
  isolatedMatcherCheck(`
    const small = new Minimatch("{x,*}/{0..9}", { optimizationLevel: 2 });
    assert.equal(small.set.length, 10, "small sets retain ordinary optimization");
    const large = new Minimatch("{x,*}/{0..599}", { optimizationLevel: 2 });
    assert.equal(large.set.length, 1200, "large sets must skip pairwise deduplication");
    assert.equal(large.match("x/5"), true);
    assert.equal(large.match("y/599"), true);
    assert.equal(large.match(".y/5"), false);
    assert.equal(large.match("y/600"), false);
  `);
});

test("bounded optimization preserves ordinary globstar and parent-segment matches", () => {
  isolatedMatcherCheck(`
    const pattern = "**/../a/b/**/../c/d";
    const matcher = new Minimatch(pattern, { optimizationLevel: 2 });
    assert.equal(matcher.set.length, 4);
    assert.equal(matcher.match("../a/b/../c/d"), true);
    assert.equal(matcher.match("x/a/b/y/c/d"), true);
    assert.equal(matcher.match("x/a/b/y/c/e"), false);
    for (const optimizationLevel of [0, 1, 2]) {
      assert.equal(minimatch("src/.hidden.ts", "src/**/*.ts", { dot: true, optimizationLevel }), true);
      assert.equal(minimatch("src/file.ts", "src/**/*.ts", { dot: true, optimizationLevel }), true);
      assert.equal(minimatch("src/file.js", "src/**/*.ts", { dot: true, optimizationLevel }), false);
      assert.equal(minimatch("test/file.ts", "src/**/*.ts", { dot: true, optimizationLevel }), false);
    }
  `);
});

test("the parser keeps the named matcher API while legacy ESLint callers stay callable", () => {
  assert.equal(typeof parserRequire("minimatch").minimatch, "function");
  for (const consumer of ["eslint", "eslint-plugin-import", "eslint-plugin-react", "eslint-plugin-jsx-a11y"]) {
    const consumerRequire = createRequire(require.resolve(consumer));
    const matcher = consumerRequire("minimatch");
    assert.equal(typeof matcher, "function", `${consumer} needs the legacy callable export`);
    assert.equal(matcher(".component.tsx", "*.tsx", { dot: true }), true);
    assert.equal(matcher("component.js", "*.tsx", { dot: true }), false);
  }
});
