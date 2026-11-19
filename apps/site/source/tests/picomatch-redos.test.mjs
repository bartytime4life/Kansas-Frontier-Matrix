import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { createRequire } from "node:module";
import test from "node:test";

// Keep the existing repeated-extglob hardening introduced for the now-withdrawn
// GHSA-fc5q-39xc-vjpf. package.json overrides picomatch to forks in vendor/
// (see vendor/picomatch-kfm.md): 4.0.7-kfm.1 for vite and tinyglobby,
// 2.3.2+kfm.1 for micromatch (used by fast-glob). Resolve the copies they load.
const require = createRequire(import.meta.url);
const semver = require("semver");
const loaders = {
  vite: { from: createRequire(require.resolve("vite/package.json")), version: "4.0.7-kfm.1" },
  tinyglobby: { from: createRequire(require.resolve("tinyglobby/package.json")), version: "4.0.7-kfm.1" },
  micromatch: { from: createRequire(require.resolve("micromatch/package.json")), version: "2.3.2+kfm.1" },
};

// Each advisory case runs in a child process with a hard timeout, so an
// unpatched copy fails this test instead of hanging the suite.
function timedIsMatch(picomatchPath, input, pattern) {
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

const advisoryCases = [
  ["a".repeat(48) + "/", "+(*a)"],
  ["a".repeat(5000) + "/", "+(*)"],
  ["ab".repeat(3000) + "/", "*(*a)"],
  ["a".repeat(60) + "/", "+(a*b)"],
  ["a".repeat(60) + "/", "@(*a)+"],
];

const ordinaryCases = [
  ["a.js", "*.js", true],
  ["abc", "*.js", false],
  ["src/a/b.ts", "src/**/*.ts", true],
  ["aaa", "+(a)", true],
  ["ab", "+(a|b)", true],
  ["a/b", "*", false],
  [".git/x", "**/*", false],
];

for (const [name, { from, version }] of Object.entries(loaders)) {
  test(`${name} resolves the patched picomatch fork`, () => {
    const installedVersion = from("picomatch/package.json").version;
    assert.equal(installedVersion, version);
    assert.ok(semver.gte(installedVersion, name === "micromatch" ? "2.3.2" : "4.0.4"));
    if (name === "micromatch") assert.ok(semver.satisfies(installedVersion, "^2.3.1"));
  });

  test(`${name}'s picomatch excludes inherited methods from POSIX classes`, () => {
    const picomatch = from("picomatch");
    // GHSA-3v7f-55p6-f55p: inherited names must never enter a generated regex.
    for (const key of ["constructor", "toString", "valueOf", "hasOwnProperty", "__proto__"]) {
      const pattern = `[[:${key}:]]`;
      assert.doesNotMatch(picomatch.makeRe(pattern).source, /function|native code|object Object/);
      for (const input of ["f", "u", "n", "c", "t", "i", "o"]) {
        assert.equal(picomatch.isMatch(input, pattern), false, `${pattern} on ${input}`);
      }
    }
  });

  test(`${name}'s picomatch preserves ordinary POSIX classes`, () => {
    const picomatch = from("picomatch");
    for (const [input, pattern, expected] of [
      ["a", "[[:alpha:]]", true], ["7", "[[:alpha:]]", false],
      ["7", "[[:digit:]]", true], ["a", "[[:digit:]]", false],
      ["F9", "[[:xdigit:]][[:xdigit:]]", true],
      ["file7.txt", "file[[:digit:]].txt", true],
      ["filea.txt", "file[[:digit:]].txt", false],
    ]) {
      assert.equal(picomatch.isMatch(input, pattern), expected, `${pattern} on ${input}`);
    }
  });

  test(`${name}'s picomatch answers the advisory's inputs promptly`, () => {
    const picomatchPath = from.resolve("picomatch");
    for (const [input, pattern] of advisoryCases) {
      const { result, ms } = timedIsMatch(picomatchPath, input, pattern);
      assert.equal(result, false, pattern);
      assert.ok(ms < 1000, `${pattern} took ${ms} ms`);
    }
  });

  test(`${name}'s picomatch keeps ordinary glob results`, () => {
    const picomatch = from("picomatch");
    for (const [input, pattern, expected] of ordinaryCases) {
      assert.equal(picomatch.isMatch(input, pattern), expected, `${pattern} on ${input}`);
    }
  });
}

test("micromatch keeps its results on the 2.x fork", () => {
  const micromatch = require("micromatch");
  assert.deepEqual(micromatch(["a.js", "b.ts", "src/c.js"], ["**/*.js"]), ["a.js", "src/c.js"]);
  assert.equal(micromatch.isMatch("foo/bar.md", "foo/*.{md,txt}"), true);
  assert.equal(micromatch.isMatch("foo/.bar", "foo/*"), false);
});
