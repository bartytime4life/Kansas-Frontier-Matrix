import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";

test("the unauthenticated Vite development server is loopback-only", async () => {
  const config = await readFile(new URL("../vite.config.ts", import.meta.url), "utf8");

  assert.match(config, /server:\s*{[\s\S]*?host:\s*["']127\.0\.0\.1["']/);
  assert.doesNotMatch(config, /host:\s*["']0\.0\.0\.0["']/);
});
