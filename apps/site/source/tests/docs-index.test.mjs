import assert from "node:assert/strict";
import { readdir, readFile, access } from "node:fs/promises";
import test from "node:test";

test("the Explorer docs index links every Markdown guide and every link resolves", async () => {
  const index = await readFile("docs/README.md", "utf8");
  const files = (await readdir("docs")).filter(name => name.endsWith(".md") && name !== "README.md");
  for (const name of files) assert.ok(index.includes(`(${name})`), `docs/README.md links ${name}`);
  for (const [, target] of index.matchAll(/\]\(([^)#\s]+\.md)(?:#[^)]*)?\)/g)) {
    if (/^https?:/.test(target)) continue;
    await access(new URL(`../docs/${target}`, import.meta.url));
  }
});
