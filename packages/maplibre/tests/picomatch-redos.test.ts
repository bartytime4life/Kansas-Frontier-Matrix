import { createRequire } from "node:module";
import { describe, expect, it } from "vitest";

// picomatch <=4.0.7 is vulnerable to GHSA-fc5q-39xc-vjpf and has no fixed
// release. The root workspace patches the copy vite and vitest load
// (configs/dependency-patches/picomatch-4.0.7.patch); resolve that exact copy.
const requireFromVitest = createRequire(createRequire(import.meta.url).resolve("vitest/package.json"));
const picomatch = requireFromVitest("picomatch") as {
  isMatch: (input: string, pattern: string) => boolean;
};

describe("patched picomatch", () => {
  it("answers the advisory's repeated-extglob inputs promptly", () => {
    // Unpatched 4.0.7 does not return from the first case within 10 seconds.
    const cases: [string, string][] = [
      ["a".repeat(48) + "/", "+(*a)"],
      ["a".repeat(5000) + "/", "+(*)"],
      ["ab".repeat(3000) + "/", "*(*a)"],
      ["a".repeat(60) + "/", "+(a*b)"],
      ["a".repeat(60) + "/", "@(*a)+"],
    ];
    for (const [input, pattern] of cases) {
      const started = performance.now();
      expect(picomatch.isMatch(input, pattern)).toBe(false);
      expect(performance.now() - started).toBeLessThan(1000);
    }
  });

  it("keeps ordinary glob results", () => {
    const cases: [string, string, boolean][] = [
      ["a.js", "*.js", true],
      ["abc", "*.js", false],
      ["src/a/b.ts", "src/**/*.ts", true],
      ["aaa", "+(a)", true],
      ["ab", "+(a|b)", true],
      ["a/b", "*", false],
      [".git/x", "**/*", false],
    ];
    for (const [input, pattern, expected] of cases) expect(picomatch.isMatch(input, pattern)).toBe(expected);
  });
});
