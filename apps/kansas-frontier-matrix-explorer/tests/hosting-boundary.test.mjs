import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";

const EXPECTED = Object.freeze({
  projectId: "appgprj_6a870a079c1c8191abb7401ef092a181",
  slug: "kansas-frontier-matrix-explorer",
  publicUrl: "https://kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site",
  replacementSha256: "6444f960bee9d2269fbf6854733bc63a59d2dd14c486670a0bfb040fd6136655",
});

const files = Object.freeze({
  hosting: new URL("../.openai/hosting.json", import.meta.url),
  vercel: new URL("../vercel.json", import.meta.url),
  layout: new URL("../app/layout.tsx", import.meta.url),
  readme: new URL("../README.md", import.meta.url),
  handoff: new URL("../docs/openai-sites-in-place-replacement.md", import.meta.url),
});

const readText = (url) => readFile(url, "utf8");

const assertIncludes = (text, value, label) => {
  assert.ok(text.includes(value), `${label} must include ${value}`);
};

test("OpenAI Sites identity and public URL remain coherent across app surfaces", async () => {
  const hosting = JSON.parse(await readText(files.hosting));
  const vercel = JSON.parse(await readText(files.vercel));
  const [layout, readme, handoff] = await Promise.all([
    readText(files.layout),
    readText(files.readme),
    readText(files.handoff),
  ]);

  assert.equal(hosting.project_id, EXPECTED.projectId);
  assert.deepEqual(vercel.git, { deploymentEnabled: false });

  for (const [label, text] of [
    ["layout metadata", layout],
    ["application README", readme],
    ["replacement handoff", handoff],
  ]) {
    assertIncludes(text, EXPECTED.publicUrl, label);
    assertIncludes(text, EXPECTED.slug, label);
  }

  assertIncludes(readme, EXPECTED.projectId, "application README");
  assertIncludes(handoff, EXPECTED.projectId, "replacement handoff");
  assert.ok(!readme.includes("kansas-frontier-matrix-explorer-web.vercel.app"));
  assert.ok(!handoff.includes("kansas-frontier-matrix-explorer-web.vercel.app"));
});

test("replacement handoff pins integrity, validation, rollback, and non-effect evidence", async () => {
  const handoff = await readText(files.handoff);

  for (const required of [
    EXPECTED.replacementSha256,
    "node --check core.mjs",
    "node --check app.mjs",
    "node --test tests/core.test.mjs",
    "python3 tests/validate_static.py",
    "previous_site_version_id",
    "candidate_saved_version_id",
    "new_site_version_id",
    "rollback_target_version_id",
    "PUBLISHED_SITE_VERSION",
    "ROLLED_BACK",
    "restricted archaeology fixture",
    "Do not create a second Site",
    "github_mutated_by_site_execution",
    "vercel_mutated",
  ]) {
    assertIncludes(handoff, required, "replacement handoff");
  }

  assert.match(handoff, /failed, skipped, unavailable, stale, or package-unbound result is not a pass/i);
  assert.match(handoff, /Do not copy that acquisition pattern into the\s+repository/i);
  assert.match(handoff, /Site rollback does not rewrite Git history/i);
  assert.match(handoff, /does not define Site platform behavior, grant deployment authority/i);
});

// These are source-level retirement guards, not proof of remote disconnection.
const assertDisableOnly = (config) => {
  assert.deepEqual(config, {
    $schema: "https://openapi.vercel.sh/vercel.json",
    git: { deploymentEnabled: false },
  });
};

const assertNoDirectVercelIntegration = (manifest) => {
  for (const section of ["dependencies", "devDependencies", "optionalDependencies", "peerDependencies"]) {
    for (const [name, specifier] of Object.entries(manifest[section] ?? {})) {
      assert.doesNotMatch(name, /^(?:vercel$|@vercel\/)/i);
      assert.doesNotMatch(String(specifier), /^npm:(?:vercel(?:@|$)|@vercel\/)/i);
    }
  }
  for (const command of Object.values(manifest.scripts ?? {})) {
    assert.doesNotMatch(command, /\bvercel\b/i);
  }
};

test("Vercel retirement: both retained manifests are disable-only", async () => {
  for (const url of [
    files.vercel,
    new URL("../../../connectors/usgs/vercel.json", import.meta.url),
  ]) {
    assertDisableOnly(JSON.parse(await readText(url)));
  }
});

test("Vercel retirement: Explorer has no direct SDK, CLI, or deployment script", async () => {
  const manifest = JSON.parse(await readText(new URL("../package.json", import.meta.url)));
  assertNoDirectVercelIntegration(manifest);
});

test("Vercel retirement: negative controls reject activation and integration", () => {
  assert.throws(() => assertDisableOnly({ git: { deploymentEnabled: true } }));
  assert.throws(() => assertDisableOnly({
    $schema: "https://openapi.vercel.sh/vercel.json",
    git: { deploymentEnabled: false },
    builds: [],
  }));
  for (const section of ["dependencies", "devDependencies", "optionalDependencies", "peerDependencies"]) {
    for (const dependency of [
      { vercel: "0.0.0-fixture" },
      { "@vercel/analytics": "0.0.0-fixture" },
      { alias: "npm:@vercel/analytics@0.0.0-fixture" },
      { alias: "npm:vercel@0.0.0-fixture" },
    ]) {
      assert.throws(() => assertNoDirectVercelIntegration({ [section]: dependency }));
    }
  }
  assert.throws(() => assertNoDirectVercelIntegration({ scripts: { deploy: "npx vercel --prod" } }));
  // Library authorship is not hosting integration: do not remove Next.js by name.
  assertNoDirectVercelIntegration({ dependencies: { next: "0.0.0-fixture" }, scripts: { test: "node --test" } });
});
