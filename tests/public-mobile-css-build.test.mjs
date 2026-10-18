import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import { optimize } from "@tailwindcss/node";

test("optimized mobile Data-sheet CSS retains the standard viewport-containing-block override", async () => {
  const source = await readFile(new URL("../app/globals.css", import.meta.url), "utf8");
  const rule = source.match(/\.topbar:has\(\.data-notices-panel\)\s*\{[^}]+\}/)?.[0];
  assert.ok(rule, "the open mobile Data sheet has a targeted header override");
  // Exercise the real build optimizer: vendor-last declarations previously
  // removed the standard property and left Chrome's header blur active.
  const built = optimize(`@media (max-width:760px) { ${rule} }`, { minify: true }).code;
  assert.match(built, /(?:\{|;)backdrop-filter:none(?=;|\})/,
    "Chrome must receive the unprefixed override after CSS optimization");
});
