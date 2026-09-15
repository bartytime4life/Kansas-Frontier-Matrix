import assert from "node:assert/strict";
import { execFileSync } from "node:child_process";
import { mkdtempSync, mkdirSync, writeFileSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import test from "node:test";
import { CURRENT_SITE_PROJECT, verifySourceAlignment } from "../scripts/verify-sites-source-alignment.mjs";

test("source parity binds identity and complete trees without claiming deployment or main parity", async (t) => {
  const root = mkdtempSync(join(tmpdir(), "kfm-site-parity-"));
  t.after(() => rmSync(root, { recursive: true, force: true }));
  const git = (...args) => execFileSync("git", ["-C", root, ...args], { encoding: "utf8", stdio: ["ignore", "pipe", "pipe"] }).trim();
  git("init", "-q"); git("config", "user.name", "Synthetic parity test");
  git("config", "user.email", "fixture@example.invalid");
  mkdirSync(join(root, ".openai"));
  const hosting = (project) => writeFileSync(join(root, ".openai/hosting.json"), JSON.stringify({ project_id: project }));
  const commit = (message) => { git("add", "."); git("commit", "-qm", message, "--allow-empty"); return git("rev-parse", "HEAD"); };
  hosting(CURRENT_SITE_PROJECT);
  writeFileSync(join(root, "app.js"), "export const fixture = true;\n");
  const siteRevision = commit("site fixture");
  const mirrorRevision = commit("independent mirror history, identical bytes");
  const input = { siteRoot: root, mirrorRoot: root, siteRevision, mirrorRevision };
  await t.test("distinct commits with identical complete trees pass", () => {
    const result = verifySourceAlignment(input);
    assert.equal(result.outcome, "PASS"); assert.notEqual(siteRevision, mirrorRevision);
    assert.equal(result.site.tree, result.mirror.tree); assert.equal(result.site.files, 2);
    assert.equal(result.deploymentAuthorized, false);
    assert.equal(result.monorepoRuntimeParity, "NOT_ESTABLISHED");
  });
  writeFileSync(join(root, "extra.js"), "export const drift = true;\n");
  const drift = commit("one added file is drift");
  await t.test("a file outside shared paths still prevents parity", () => {
    assert.deepEqual(verifySourceAlignment({ ...input, mirrorRevision: drift }).reasons, ["SOURCE_TREE_MISMATCH"]);
  });
  hosting("appgprj_6a870a079c1c8191abb7401ef092a181");
  const legacy = commit("historical project fixture");
  await t.test("matching legacy trees do not become the current Site", () => {
    const result = verifySourceAlignment({ ...input, siteRevision: legacy, mirrorRevision: legacy });
    assert.equal(result.outcome, "HOLD"); assert.deepEqual(result.reasons, ["SITE_IDENTITY_MISMATCH"]);
  });
  await t.test("moving branch names and abbreviated revisions fail closed", () => {
    for (const ref of ["main", "HEAD", siteRevision.slice(0, 7), "--help", null]) {
      assert.equal(verifySourceAlignment({ ...input, siteRevision: ref }).outcome, "ERROR");
    }
  });
  await t.test("missing source objects do not become parity", () => {
    const result = verifySourceAlignment({ ...input, mirrorRevision: "0".repeat(40) });
    assert.equal(result.outcome, "ERROR"); assert.equal(result.deploymentAuthorized, false);
  });
});
