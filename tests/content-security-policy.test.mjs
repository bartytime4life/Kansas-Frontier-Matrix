import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import { browserHeaders } from "../server/browser-headers.mjs";

const directives = Object.fromEntries(browserHeaders["Content-Security-Policy"].split(";").map(part => part.trim().split(/\s+/)).map(([name, ...values]) => [name, values]));

test("images the page hands to the map as blob URLs can be fetched", async () => {
  // The Event Observatory downloads a radar frame, checks it, and gives the map a blob URL for it.
  // The map library reads that URL with fetch, which connect-src governs, not img-src.
  const workspace = await readFile("app/observatory/workspace.tsx", "utf8");
  assert.match(workspace, /const url = URL\.createObjectURL\(blob\); urls\.current\.set\(time, url\);/);
  assert.ok(directives["connect-src"].includes("blob:"), "connect-src allows blob: so those frames are not refused");
  assert.ok(directives["img-src"].includes("blob:"));
});

test("allowing blob: opens no outside destination", () => {
  // Everything else in connect-src stays as it was: this origin and https only.
  assert.deepEqual(directives["connect-src"], ["'self'", "https:", "blob:"]);
  for (const forbidden of ["*", "http:", "data:", "ws:", "wss:", "'unsafe-inline'", "'unsafe-eval'"]) assert.ok(!directives["connect-src"].includes(forbidden), forbidden);
  assert.deepEqual(directives["default-src"], ["'self'"]);
  assert.deepEqual(directives["object-src"], ["'none'"]);
  assert.deepEqual(directives["base-uri"], ["'self'"]);
});

test("the build's page headers come from the same definition the server applies", async () => {
  const config = await readFile("next.config.ts", "utf8");
  assert.match(config, /import \{ browserHeaders \} from "\.\/server\/browser-headers\.mjs";/);
});
