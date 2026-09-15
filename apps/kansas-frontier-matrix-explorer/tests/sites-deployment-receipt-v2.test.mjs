import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import { validateReceipt, validateCurrentReceipt } from "../scripts/validate-sites-deployment-receipt.mjs";
const load = async () => JSON.parse(await readFile(new URL("../fixtures/sites-deployment-receipt/current-project-rehearsal.json", import.meta.url), "utf8"));
test("current project rehearsal remains HOLD with synthetic identities", async () => {
  const receipt = await load();
  assert.deepEqual(validateReceipt(receipt), { outcome: "PASS", errors: [] });
  assert.equal(receipt.outcome, "HOLD");
  assert.equal(receipt.checks.source_alignment.outcome, "NOT_RUN");
  assert.equal(receipt.authority.live_transition_performed, false);
});
for (const [name, change] of [
  ["legacy project replay", r => r.site.project_id = "appgprj_6a870a079c1c8191abb7401ef092a181"],
  ["mixed schema versions", r => r.schema_version = "1.0.0"],
  ["missing Sites source commit", r => delete r.source.sites_revision],
  ["moving source ref", r => r.source.sites_revision = "main"],
  ["missing source tree", r => delete r.source.source_tree],
  ["missing alignment evidence", r => delete r.checks.source_alignment],
  ["invalid alignment evidence type", r => r.checks.source_alignment.evidence = 1],
]) test(`current receipt rejects ${name}`, async () => {
  const receipt = await load(); change(receipt);
  assert.equal(validateReceipt(receipt).outcome, "DENY");
});
test("deployment cannot reuse unchecked mirror parity", async () => {
  const r = await load();
  r.mode = "OPERATOR_READBACK"; r.outcome = "DEPLOYED";
  r.site.previous_version_id = "synthetic-previous"; r.site.candidate_version_id = "synthetic-candidate";
  r.site.final_version_id = r.site.candidate_version_id; r.rollback.target_version_id = r.site.previous_version_id;
  r.authority.live_transition_performed = true;
  r.rollback.rehearsal_outcome = "PASS";
  for (const [name, check] of Object.entries(r.checks)) if (name !== "source_alignment") check.outcome = "PASS";
  assert.equal(validateReceipt(r).outcome, "DENY");
  r.checks.source_alignment.outcome = "PASS";
  assert.deepEqual(validateReceipt(r), { outcome: "PASS", errors: [] });
  r.rollback.rehearsal_outcome = "NOT_RUN";
  assert.equal(validateReceipt(r).outcome, "DENY");
  r.rollback.rehearsal_outcome = "PASS";
  r.checks.mobile_smoke.outcome = "NOT_RUN";
  assert.equal(validateReceipt(r).outcome, "DENY");
});
test("current operator validation cannot replay a valid historical receipt", async () => {
  const old = JSON.parse(await readFile(new URL("../fixtures/sites-deployment-receipt/repository-rehearsal.json", import.meta.url), "utf8"));
  assert.equal(validateReceipt(old).outcome, "PASS");
  assert.equal(validateCurrentReceipt(old).outcome, "DENY");
  assert.equal(validateCurrentReceipt(await load()).outcome, "PASS");
});
