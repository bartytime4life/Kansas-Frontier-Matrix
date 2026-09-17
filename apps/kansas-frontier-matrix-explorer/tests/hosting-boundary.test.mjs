import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";

const EXPECTED = Object.freeze({
  projectId: "appgprj_6aa0b1c41bc08191bfd86003920f1631",
  historicalProjectId: "appgprj_6a870a079c1c8191abb7401ef092a181",
  slug: "kansas-frontier-matrix-explorer",
  publicUrl: "https://kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site",
  sitesRevision: "2a0bd440a1aa5ff375efea5af87f283cd62c464b",
  sitesVersion: "appgprj_6aa0b1c41bc08191bfd86003920f1631~appgver_62df758dd2e0819197329087b6c2fe57",
  archiveSha256: "b1415f7325668ac766240be8a94dd9b80b1ac5453ef5fa33049841a5d39034f3",
  deploymentId: "appgdep_6aab4ac3bb64819182773975685b99e8",
  recoveryRevision: "b893683c33ef1a85d75f88db58e27e361c7e01a0",
  recoveryArchiveSha256: "0653b89744b7ff44fa08570dcf75055b80d6c5449322cff655a550eb6043c637",
  replacementSha256: "6444f960bee9d2269fbf6854733bc63a59d2dd14c486670a0bfb040fd6136655",
});

const files = Object.freeze({
  hosting: new URL("../.openai/hosting.json", import.meta.url),
  shell: new URL("../index.html", import.meta.url),
  readme: new URL("../README.md", import.meta.url),
  alignment: new URL("../docs/sites-source-alignment.md", import.meta.url),
  handoff: new URL("../docs/openai-sites-in-place-replacement.md", import.meta.url),
});

const readText = (url) => readFile(url, "utf8");

const assertIncludes = (text, value, label) => {
  assert.ok(text.includes(value), `${label} must include ${value}`);
};

test("OpenAI Sites identity and public URL remain coherent across app surfaces", async () => {
  const hosting = JSON.parse(await readText(files.hosting));
  const [shell, readme, alignment] = await Promise.all([
    readText(files.shell),
    readText(files.readme),
    readText(files.alignment),
  ]);

  assert.equal(hosting.project_id, EXPECTED.projectId);
  assert.equal(hosting.d1, null);
  assert.equal(hosting.r2, null);

  for (const [label, text] of [
    ["application shell metadata", shell],
    ["application README", readme],
    ["source-alignment hold", alignment],
  ]) {
    assertIncludes(text, EXPECTED.publicUrl, label);
    assertIncludes(text, EXPECTED.slug, label);
  }

  assertIncludes(readme, EXPECTED.projectId, "application README");
  assertIncludes(alignment, EXPECTED.projectId, "source-alignment hold");
});

test("current source evidence stays explicitly non-equivalent and held", async () => {
  const alignment = await readText(files.alignment);

  for (const required of [
    "SOURCE_EQUIVALENCE_HOLD",
    "ACCEPTANCE_HOLD",
    EXPECTED.sitesRevision,
    EXPECTED.sitesVersion,
    EXPECTED.archiveSha256,
    EXPECTED.deploymentId,
    EXPECTED.recoveryRevision,
    EXPECTED.recoveryArchiveSha256,
    "No full-tree comparison",
    "not a rehearsed restoration",
    "does not authorize deployment",
    "Do not merge",
  ]) {
    assertIncludes(alignment, required, "source-alignment hold");
  }
});

test("historical replacement handoff remains intact and cannot masquerade as current", async () => {
  const handoff = await readText(files.handoff);

  for (const required of [
    "Historical checkpoint",
    "not a current execution procedure",
    EXPECTED.historicalProjectId,
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
  ]) {
    assertIncludes(handoff, required, "replacement handoff");
  }

  assert.match(handoff, /failed, skipped, unavailable, stale, or package-unbound result is not a pass/i);
  assert.match(handoff, /Do not copy that acquisition pattern into the\s+repository/i);
  assert.match(handoff, /Site rollback does not rewrite Git history/i);
  assert.match(handoff, /does not define Site platform behavior, grant deployment authority/i);
});
