import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { createRequire } from "node:module";
import { dirname, join } from "node:path";
import { spawnSync } from "node:child_process";
import { fileURLToPath, pathToFileURL } from "node:url";
import test from "node:test";
import { withESLint10ReactContext } from "../../apps/kansas-frontier-matrix-explorer/eslint-react-context.mjs";
import candidate from "../../apps/kansas-frontier-matrix-explorer/eslint.config.mjs";

const app = fileURLToPath(new URL("../../apps/kansas-frontier-matrix-explorer/", import.meta.url));
const appRequire = createRequire(join(app, "package.json"));
const { ESLint } = appRequire("eslint");
const { defineConfig, globalIgnores } = appRequire("eslint/config");
const nextVitals = (await import(pathToFileURL(appRequire.resolve("eslint-config-next/core-web-vitals")).href)).default;
const nextTs = (await import(pathToFileURL(appRequire.resolve("eslint-config-next/typescript" )).href)).default;
const baseline = defineConfig([
  ...nextVitals, ...nextTs,
  globalIgnores([".next/**", "out/**", "build/**", "next-env.d.ts"]),
]);
const original = new ESLint({ cwd: app, overrideConfigFile: true, overrideConfig: baseline });
const repaired = new ESLint({ cwd: app, overrideConfigFile: true, overrideConfig: candidate });

for (const extension of ["js", "mjs", "jsx", "ts", "tsx"]) {
  test(`effective ${extension} rules, options, parser, and settings are unchanged`, async () => {
    const filename = `app/lint-contract.${extension}`;
    const before = await original.calculateConfigForFile(filename);
    const after = await repaired.calculateConfigForFile(filename);
    assert.ok(Object.keys(before.rules).length > 50);
    assert.deepEqual(after.rules, before.rules);
    assert.deepEqual(after.settings, before.settings);
    assert.deepEqual(after.linterOptions, before.linterOptions);
    assert.deepEqual(after.languageOptions, before.languageOptions);
    assert.deepEqual(Object.keys(after.plugins), Object.keys(before.plugins));
    for (const name of Object.keys(before.plugins)) {
      if (name !== "react") assert.equal(after.plugins[name], before.plugins[name]);
    }
  });
}

test("the complete React rule inventory and metadata remain unchanged", () => {
  const source = nextVitals.find((config) => config.plugins?.react).plugins.react;
  const bridge = withESLint10ReactContext(source);
  assert.deepEqual(Object.keys(bridge.rules), Object.keys(source.rules));
  for (const [name, rule] of Object.entries(source.rules)) {
    const { create: originalCreate, ...before } = rule;
    const { create: bridgedCreate, ...after } = bridge.rules[name];
    assert.deepEqual(after, before);
    assert.notEqual(bridgedCreate, originalCreate);
  }
  assert.equal(withESLint10ReactContext(source), bridge);
  assert.equal(withESLint10ReactContext(bridge), bridge);
});

test("existing ignores are unchanged", async () => {
  for (const filename of [".next/fixture.tsx", "out/fixture.js", "build/fixture.mjs", "next-env.d.ts", "app/page.tsx", "worker/index.ts"]) {
    assert.equal(await repaired.isPathIgnored(filename), await original.isPathIgnored(filename), filename);
  }
});

test("compiler and lint dependencies stay pinned; lint command is not weakened", () => {
  const manifest = JSON.parse(readFileSync(join(app, "package.json"), "utf8"));
  assert.equal(manifest.devDependencies.eslint, "10.9.1");
  assert.equal(manifest.devDependencies["eslint-config-next"], "16.3.3");
  assert.equal(manifest.devDependencies["@typescript/native"], "npm:typescript@7.0.2");
  assert.equal(manifest.scripts.lint, "bash scripts/sites-env.sh -- eslint . --ignore-pattern dist --ignore-pattern .next --ignore-pattern public/maplibre");
  assert.equal(ESLint.version, "10.9.1");
});

const good = 'export default function Example() { return <div>Public synthetic fixture</div>; }';
test("valid React source lints without errors or warnings", async () => {
  const [result] = await repaired.lintText(good, { filePath: "app/lint-contract.tsx" });
  assert.deepEqual(result.messages, []);
});

test("the unadapted locked configuration still reproduces the removed API crash", async () => {
  await assert.rejects(original.lintText(good, { filePath: "app/lint-contract.tsx" }), /getFilename is not a function/);
});

const negatives = [
  ["react/display-name", "jsx", 'import { memo } from "react"; export default memo(() => <div />);'],
  ["react/jsx-key", "tsx", 'export default function Example() { return <ul>{[1, 2].map(value => <li>{value}</li>)}</ul>; }'],
  ["react/no-unknown-property", "jsx", 'export default function Example() { return <div class="fixture" />; }'],
  ["react/no-unescaped-entities", "tsx", 'export default function Example() { return <div>can\'t</div>; }'],
  ["react/jsx-no-duplicate-props", "jsx", 'export default function Example() { return <div title="one" title="two" />; }'],
  ["react-hooks/rules-of-hooks", "tsx", 'import { useState } from "react"; export default function Example({ enabled }: { enabled: boolean }) { if (enabled) { useState(0); } return <div />; }'],
  ["@typescript-eslint/no-explicit-any", "ts", 'export function identity(value: any) { return value; }'],
  ["jsx-a11y/alt-text", "tsx", 'export default function Example() { return <img src="/synthetic.png" />; }'],
  ["import/no-anonymous-default-export", "mjs", 'export default {};'],
];
for (const [rule, extension, source] of negatives) {
  test(`negative fixture still reports ${rule}`, async () => {
    const filename = `app/lint-contract.${extension}`;
    const config = await original.calculateConfigForFile(filename);
    assert.ok(config.rules[rule][0] > 0, `${rule} must already be enabled`);
    const [result] = await repaired.lintText(source, { filePath: filename });
    assert.equal(result.fatalErrorCount, 0);
    assert.ok(result.messages.some((message) => message.ruleId === rule && message.severity === config.rules[rule][0]), JSON.stringify(result.messages));
  });
}

test("syntax failures remain fatal", async () => {
  const [result] = await repaired.lintText("export default function (", { filePath: "app/lint-contract.tsx" });
  assert.ok(result.fatalErrorCount > 0);
});

test("CLI exits nonzero for a retained blocking React rule", () => {
  const cli = join(dirname(appRequire.resolve("eslint/package.json")), "bin/eslint.js");
  const result = spawnSync(process.execPath, [cli, "--stdin", "--stdin-filename", "app/lint-contract.tsx", "--format", "json"], {
    cwd: app, encoding: "utf8", timeout: 60000,
    input: negatives.find(([rule]) => rule === "react/jsx-key")[2],
  });
  assert.ifError(result.error);
  assert.equal(result.status, 1, result.stderr);
  assert.ok(JSON.parse(result.stdout)[0].messages.some((message) => message.ruleId === "react/jsx-key"));
});

test("metadata getters forward exact values without changing SourceCode or the original context", () => {
  const sourceCode = Object.freeze({ marker: "source" });
  const parserOptions = Object.freeze({ ecmaVersion: 2024 });
  const context = Object.freeze({ filename: "fixture.tsx", physicalFilename: "/fixture.tsx", cwd: "/fixture", sourceCode, languageOptions: { parserOptions } });
  const visitor = { Program() {} };
  const plugin = { rules: { fixture: { meta: {}, create(received) {
    assert.equal(received.getFilename(), context.filename);
    assert.equal(received.getPhysicalFilename(), context.physicalFilename);
    assert.equal(received.getCwd(), context.cwd);
    assert.equal(received.getSourceCode(), sourceCode);
    assert.equal(received.sourceCode, sourceCode);
    assert.equal(received.parserOptions, parserOptions);
    assert.ok(Object.isFrozen(received));
    return visitor;
  } } } };
  assert.equal(withESLint10ReactContext(plugin).rules.fixture.create(context), visitor);
  assert.equal(context.getFilename, undefined);
});

test("old-API contexts are passed through unchanged", () => {
  const context = { getFilename() { return "fixture.jsx"; } };
  const plugin = { rules: { fixture: { create(received) { assert.equal(received, context); return {}; } } } };
  withESLint10ReactContext(plugin).rules.fixture.create(context);
});

test("rule failures propagate without suppression", () => {
  const error = new Error("synthetic plugin failure");
  const plugin = { rules: { fixture: { create() { throw error; } } } };
  assert.throws(() => withESLint10ReactContext(plugin).rules.fixture.create({ languageOptions: { parserOptions: {} } }), (actual) => actual === error);
});

test("unsupported rule definitions fail closed", () => {
  assert.throws(() => withESLint10ReactContext({ rules: { fixture: {} } }), /Unsupported React rule definition/);
});
