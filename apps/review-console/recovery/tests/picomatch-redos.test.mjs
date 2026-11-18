import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { createRequire } from "node:module";
import test from "node:test";

// picomatch <=4.0.7 is vulnerable to GHSA-fc5q-39xc-vjpf and has no fixed
// release. package.json overrides every picomatch to the patched fork in
// vendor/ (see vendor/picomatch-kfm.md). Resolve the copy vite loads.
const require = createRequire(import.meta.url);
const fromVite = createRequire(require.resolve("vite/package.json"));
const picomatchPath = fromVite.resolve("picomatch");

// Each advisory case runs in a child process with a hard timeout, so an
// unpatched copy fails this test instead of hanging the suite.
function timedIsMatch(input, pattern) {
  const script = `
    const pm = require(${JSON.stringify(picomatchPath)});
    const started = performance.now();
    const result = pm.isMatch(process.argv[1], process.argv[2]);
    process.stdout.write(JSON.stringify({ result, ms: performance.now() - started }));
  `;
  const run = spawnSync(process.execPath, ["-e", script, input, pattern], { encoding: "utf8", timeout: 5000 });
  assert.equal(run.error, undefined, `${pattern} did not return within 5 s`);
  assert.equal(run.status, 0, run.stderr);
  return JSON.parse(run.stdout);
}

test("vite resolves the patched picomatch fork", () => {
  assert.equal(fromVite("picomatch/package.json").version, "4.0.7-kfm.1");
});

test("the advisory's repeated-extglob inputs return promptly", () => {
  const cases = [
    ["a".repeat(48) + "/", "+(*a)"],
    ["a".repeat(5000) + "/", "+(*)"],
    ["ab".repeat(3000) + "/", "*(*a)"],
    ["a".repeat(60) + "/", "+(a*b)"],
    ["a".repeat(60) + "/", "@(*a)+"],
  ];
  for (const [input, pattern] of cases) {
    const { result, ms } = timedIsMatch(input, pattern);
    assert.equal(result, false, pattern);
    assert.ok(ms < 1000, `${pattern} took ${ms} ms`);
  }
});

test("ordinary globs keep their results", () => {
  const picomatch = fromVite("picomatch");
  const cases = [
    ["a.js", "*.js", true],
    ["abc", "*.js", false],
    ["src/a/b.ts", "src/**/*.ts", true],
    ["aaa", "+(a)", true],
    ["ab", "+(a|b)", true],
    ["a/b", "*", false],
    [".git/x", "**/*", false],
  ];
  for (const [input, pattern, expected] of cases) assert.equal(picomatch.isMatch(input, pattern), expected, `${pattern} on ${input}`);
});
