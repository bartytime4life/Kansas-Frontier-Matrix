import { readFile } from "node:fs/promises";
const E = Object.freeze({ profile: "kfm.sites.deployment-receipt.v1", schema: "1.0.0", project: "appgprj_6a870a079c1c8191abb7401ef092a181", slug: "kansas-frontier-matrix-explorer", url: "https://kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site", repo: "bartytime4life/Kansas-Frontier-Matrix", procedure: "Restore target_version_id through the existing Site version history, then re-run identity, access, desktop/mobile, restricted-state, and core-flow smoke checks." });
const CHECKS = ["frozen_install", "build", "tests", "lint", "desktop_smoke", "mobile_smoke", "restricted_state"];
const eq = (errors, actual, expected, path) => { if (actual !== expected) errors.push(`${path} must equal ${JSON.stringify(expected)}`); };
export function validateReceipt(r) {
  const errors = [];
  eq(errors, r?.profile, E.profile, "profile"); eq(errors, r?.schema_version, E.schema, "schema_version");
  if (!["REPOSITORY_REHEARSAL", "OPERATOR_READBACK"].includes(r?.mode)) errors.push("mode is invalid");
  if (!["READY_FOR_OPERATOR", "HOLD", "DEPLOYED", "ROLLED_BACK", "ERROR"].includes(r?.outcome)) errors.push("outcome is invalid");
  if (Number.isNaN(Date.parse(r?.recorded_at))) errors.push("recorded_at is invalid");
  eq(errors, r?.site?.project_id, E.project, "site.project_id"); eq(errors, r?.site?.slug, E.slug, "site.slug"); eq(errors, r?.site?.public_url, E.url, "site.public_url"); eq(errors, r?.source?.repository, E.repo, "source.repository");
  if (!/^[0-9a-f]{40}$/.test(r?.source?.revision ?? "")) errors.push("source.revision must be a full commit SHA");
  if (!/^[0-9a-f]{64}$/.test(r?.source?.artifact_sha256 ?? "")) errors.push("source.artifact_sha256 must be SHA-256");
  for (const name of CHECKS) { const c = r?.checks?.[name]; if (!["PASS", "FAIL", "NOT_RUN"].includes(c?.outcome)) errors.push(`checks.${name}.outcome is invalid`); if (!c?.evidence?.trim()) errors.push(`checks.${name}.evidence is required`); }
  eq(errors, r?.rollback?.procedure, E.procedure, "rollback.procedure");
  for (const flag of ["second_site_created", "vercel_mutated", "release_authorized", "publication_authorized"]) eq(errors, r?.authority?.[flag], false, `authority.${flag}`);
  if (r?.mode === "REPOSITORY_REHEARSAL") {
    for (const field of ["previous_version_id", "candidate_version_id", "final_version_id"]) eq(errors, r?.site?.[field], null, `site.${field}`);
    eq(errors, r?.rollback?.target_version_id, null, "rollback.target_version_id"); eq(errors, r?.rollback?.operator_restore_confirmed, false, "rollback.operator_restore_confirmed"); eq(errors, r?.authority?.live_transition_performed, false, "authority.live_transition_performed");
    if (!["READY_FOR_OPERATOR", "HOLD", "ERROR"].includes(r?.outcome)) errors.push("repository rehearsal cannot report a live outcome");
  }
  if (r?.mode === "OPERATOR_READBACK" && ["DEPLOYED", "ROLLED_BACK"].includes(r?.outcome)) {
    for (const field of ["previous_version_id", "candidate_version_id", "final_version_id"]) if (!r?.site?.[field]) errors.push(`site.${field} is required for live readback`);
    if (!r?.rollback?.target_version_id) errors.push("rollback.target_version_id is required for live readback");
    eq(errors, r?.rollback?.operator_restore_confirmed, true, "rollback.operator_restore_confirmed"); eq(errors, r?.authority?.live_transition_performed, true, "authority.live_transition_performed");
    for (const name of CHECKS) if (r?.checks?.[name]?.outcome !== "PASS") errors.push(`checks.${name} must PASS for ${r.outcome}`);
  }
  return { outcome: errors.length ? "DENY" : "PASS", errors };
}
if (import.meta.url === `file://${process.argv[1]}`) { const result = validateReceipt(JSON.parse(await readFile(process.argv[2], "utf8"))); console.log(JSON.stringify(result)); if (result.outcome !== "PASS") process.exitCode = 1; }
