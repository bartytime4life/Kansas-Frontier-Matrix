import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { createRequire } from "node:module";
import { join } from "node:path";
import test from "node:test";

const app = new URL("../../apps/kansas-frontier-matrix-explorer/", import.meta.url).pathname;
const appRequire = createRequire(join(app, "package.json"));
const { ESLint } = appRequire("eslint");
const candidate = (await import("../../apps/kansas-frontier-matrix-explorer/eslint.config.mjs")).default;
const eslint = new ESLint({ cwd: app, overrideConfigFile: true, overrideConfig: candidate });

test("TypeScript and TSX use the declared parser", async () => {
  for (const filename of ["app/lint-contract.ts", "app/lint-contract.tsx"]) {
    const config = await eslint.calculateConfigForFile(filename);
    assert.ok(config.languageOptions.parser, filename);
    assert.ok(Object.keys(config.rules).length > 20, filename);
  }
});

test("compiler and lint dependencies stay pinned", () => {
  const manifest = JSON.parse(readFileSync(join(app, "package.json"), "utf8"));
  assert.equal(manifest.devDependencies.eslint, "10.11.0");
  assert.equal(manifest.devDependencies["typescript-eslint"], "8.70.0");
  assert.equal(manifest.devDependencies["@typescript/native"], "npm:typescript@7.0.2");
  assert.equal(manifest.scripts.lint, "bash scripts/sites-env.sh -- eslint . --ignore-pattern dist --ignore-pattern public/maplibre");
  assert.equal(ESLint.version, "10.11.0");
});

test("valid React source lints without fatal errors", async () => {
  const [result] = await eslint.lintText(
    'export default function Example() { return <div>Public synthetic fixture</div>; }',
    { filePath: "app/lint-contract.tsx" },
  );
  assert.equal(result.fatalErrorCount, 0);
});

test("unsafe explicit any remains blocked", async () => {
  const [result] = await eslint.lintText(
    "export function identity(value: any) { return value; }",
    { filePath: "app/lint-contract.ts" },
  );
  assert.ok(result.messages.some((message) => message.ruleId === "@typescript-eslint/no-explicit-any"));
});

test("syntax failures remain fatal", async () => {
  const [result] = await eslint.lintText("export default function (", { filePath: "app/lint-contract.tsx" });
  assert.ok(result.fatalErrorCount > 0);
});
