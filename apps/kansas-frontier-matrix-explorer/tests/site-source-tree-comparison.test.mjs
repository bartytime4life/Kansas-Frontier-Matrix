import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { copyFileSync, mkdirSync, mkdtempSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import path from "node:path";
import { test } from "node:test";
import { fileURLToPath } from "node:url";

const script = fileURLToPath(new URL("../scripts/compare-site-source-tree.mjs", import.meta.url));
const projectId = "appgprj_fixture123";
const gitEnv = {
  ...process.env,
  GIT_AUTHOR_NAME: "Fixture",
  GIT_AUTHOR_EMAIL: "fixture@example.invalid",
  GIT_COMMITTER_NAME: "Fixture",
  GIT_COMMITTER_EMAIL: "fixture@example.invalid",
};

function git(cwd, ...args) {
  const result = spawnSync("git", args, { cwd, encoding: "utf8", env: gitEnv });
  assert.equal(result.status, 0, result.stderr);
  return result.stdout.trim();
}

function fixture(t) {
  const root = mkdtempSync(path.join(tmpdir(), "kfm-site-tree-"));
  t.after(() => rmSync(root, { recursive: true, force: true }));
  const site = path.join(root, "site");
  const candidate = path.join(root, "candidate");
  mkdirSync(site);
  mkdirSync(candidate);
  for (const repo of [site, candidate]) {
    git(repo, "init", "-q", "-b", "main");
  }
  mkdirSync(path.join(site, ".openai"));
  writeFileSync(path.join(site, ".openai", "hosting.json"), `${JSON.stringify({ project_id: projectId })}\n`);
  writeFileSync(path.join(site, "README.md"), "fixture-only source\n");
  mkdirSync(path.join(candidate, "site-app", ".openai"), { recursive: true });
  copyFileSync(path.join(site, ".openai", "hosting.json"), path.join(candidate, "site-app", ".openai", "hosting.json"));
  copyFileSync(path.join(site, "README.md"), path.join(candidate, "site-app", "README.md"));
  for (const repo of [site, candidate]) {
    git(repo, "add", "--all");
    git(repo, "commit", "-q", "-m", "fixture");
  }
  const siteCommit = git(site, "rev-parse", "HEAD");
  const candidateCommit = git(candidate, "rev-parse", "HEAD");
  const args = [
    "--site-checkout", site,
    "--site-commit", siteCommit,
    "--project-id", projectId,
    "--candidate-repo", candidate,
    "--candidate-commit", candidateCommit,
    "--candidate-subtree", "site-app",
  ];
  return { site, candidate, siteCommit, args };
}

function run(args) {
  return spawnSync(process.execPath, [script, ...args], { encoding: "utf8" });
}

test("reports exact committed subtree equality without source paths", (t) => {
  const { site, candidate, args } = fixture(t);
  const result = run(args);
  assert.equal(result.status, 0, result.stderr);
  const report = JSON.parse(result.stdout);
  assert.equal(report.outcome, "MATCH");
  assert.deepEqual(report.counts, {
    site: 2, candidate: 2, common: 2, identical: 2,
    changed: 0, site_only: 0, candidate_only: 0,
  });
  assert.equal(report.authority.startsWith("NONE;"), true);
  assert.equal(result.stdout.includes(site), false);
  assert.equal(result.stdout.includes(candidate), false);
  const overridden = spawnSync(process.execPath, [script, ...args], {
    encoding: "utf8",
    env: { ...process.env, GIT_DIR: path.join(candidate, ".git"), GIT_WORK_TREE: candidate },
  });
  assert.equal(overridden.status, 0, overridden.stderr);
});

test("rejects a partial match and reports aggregate differences only", (t) => {
  const { candidate, args } = fixture(t);
  writeFileSync(path.join(candidate, "site-app", "secret-route.txt"), "never print this content\n");
  git(candidate, "add", "--all");
  git(candidate, "commit", "-q", "-m", "different");
  args[args.indexOf("--candidate-commit") + 1] = git(candidate, "rev-parse", "HEAD");
  const result = run(args);
  assert.equal(result.status, 1, result.stderr);
  const report = JSON.parse(result.stdout);
  assert.equal(report.outcome, "DIFFERENT");
  assert.equal(report.counts.candidate_only, 1);
  assert.equal(result.stdout.includes("secret-route"), false);
  assert.equal(result.stdout.includes("never print"), false);
});

test("rejects changed bytes even when both trees have the same paths and count", (t) => {
  const { candidate, args } = fixture(t);
  writeFileSync(path.join(candidate, "site-app", "README.md"), "changed fixture-only source\n");
  git(candidate, "add", "--all");
  git(candidate, "commit", "-q", "-m", "changed bytes");
  args[args.indexOf("--candidate-commit") + 1] = git(candidate, "rev-parse", "HEAD");
  const result = run(args);
  assert.equal(result.status, 1, result.stderr);
  assert.deepEqual(JSON.parse(result.stdout).counts, {
    site: 2, candidate: 2, common: 2, identical: 1,
    changed: 1, site_only: 0, candidate_only: 0,
  });
});

test("fails closed on stale source commit, dirty source, and wrong project", (t) => {
  const { site, args } = fixture(t);
  const stale = [...args];
  stale[stale.indexOf("--site-commit") + 1] = "0".repeat(40);
  assert.match(run(stale).stderr, /^SITE_SOURCE_COMPARISON_ERROR: SOURCE_HEAD_MISMATCH/);
  writeFileSync(path.join(site, "README.md"), "uncommitted private text\n");
  const dirty = run(args);
  assert.equal(dirty.status, 2);
  assert.match(dirty.stderr, /^SITE_SOURCE_COMPARISON_ERROR: SOURCE_WORKTREE_DIRTY/);
  assert.equal(dirty.stderr.includes("private text"), false);
  git(site, "checkout", "--", "README.md");
  const wrong = [...args];
  wrong[wrong.indexOf("--project-id") + 1] = "appgprj_other456";
  assert.match(run(wrong).stderr, /^SITE_SOURCE_COMPARISON_ERROR: SOURCE_PROJECT_MISMATCH/);
});
