#!/usr/bin/env node
/** Compare two committed Git trees without printing source paths or content. */
import { spawnSync } from "node:child_process";
import { realpathSync } from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const COMMIT = /^[0-9a-f]{40}$/;
const PROJECT = /^appgprj_[A-Za-z0-9]+$/;
const SUBTREE = /^[A-Za-z0-9._/-]+$/;
const ERROR_CODES = new Set([
  "INVALID_ARGUMENTS",
  "GIT_INSPECTION_FAILED",
  "SOURCE_HEAD_MISMATCH",
  "SOURCE_WORKTREE_DIRTY",
  "TREE_FORMAT_MISMATCH",
  "SOURCE_MANIFEST_INVALID",
  "SOURCE_PROJECT_MISMATCH",
]);
const REQUIRED = new Set([
  "--site-checkout",
  "--site-commit",
  "--project-id",
  "--candidate-repo",
  "--candidate-commit",
  "--candidate-subtree",
]);

function argsFrom(argv) {
  if (argv.length !== REQUIRED.size * 2) throw new Error("INVALID_ARGUMENTS");
  const result = new Map();
  for (let i = 0; i < argv.length; i += 2) {
    if (!REQUIRED.has(argv[i]) || result.has(argv[i]) || !argv[i + 1]) {
      throw new Error("INVALID_ARGUMENTS");
    }
    result.set(argv[i], argv[i + 1]);
  }
  if (result.size !== REQUIRED.size ||
    !COMMIT.test(result.get("--site-commit")) ||
    !COMMIT.test(result.get("--candidate-commit")) ||
    !PROJECT.test(result.get("--project-id"))) {
    throw new Error("INVALID_ARGUMENTS");
  }
  const subtree = result.get("--candidate-subtree");
  if (subtree !== "." && (!SUBTREE.test(subtree) ||
    subtree.startsWith("/") || subtree.split("/").some((part) => part === ".." || !part))) {
    throw new Error("INVALID_ARGUMENTS");
  }
  for (const key of ["--site-checkout", "--candidate-repo"]) {
    const value = result.get(key);
    if (!path.isAbsolute(value)) throw new Error("INVALID_ARGUMENTS");
    try { result.set(key, realpathSync(value)); }
    catch { throw new Error("INVALID_ARGUMENTS"); }
  }
  return result;
}

function git(cwd, args) {
  const env = { ...process.env };
  for (const key of Object.keys(env)) {
    if (key.startsWith("GIT_")) delete env[key];
  }
  env.GIT_CONFIG_NOSYSTEM = "1";
  env.GIT_CONFIG_GLOBAL = "/dev/null";
  env.GIT_OPTIONAL_LOCKS = "0";
  const result = spawnSync("git", args, {
    cwd,
    encoding: null,
    maxBuffer: 16 * 1024 * 1024,
    env,
  });
  if (result.status !== 0 || result.error) throw new Error("GIT_INSPECTION_FAILED");
  return result.stdout;
}

function ascii(buffer) { return buffer.toString("ascii").trim(); }

function entries(cwd, tree) {
  const raw = git(cwd, ["ls-tree", "-r", "-z", tree]);
  const records = new Map();
  let start = 0;
  while (start < raw.length) {
    const end = raw.indexOf(0, start);
    if (end < 0) throw new Error("GIT_INSPECTION_FAILED");
    const tab = raw.indexOf(9, start);
    if (tab < 0 || tab >= end) throw new Error("GIT_INSPECTION_FAILED");
    const header = raw.subarray(start, tab).toString("ascii");
    const key = raw.subarray(tab + 1, end).toString("base64");
    if (records.has(key)) throw new Error("GIT_INSPECTION_FAILED");
    records.set(key, header);
    start = end + 1;
  }
  return records;
}

export function compareSiteSourceTrees(argv) {
  const options = argsFrom(argv);
  const site = options.get("--site-checkout");
  const candidate = options.get("--candidate-repo");
  const siteCommit = options.get("--site-commit");
  const candidateCommit = options.get("--candidate-commit");
  if (ascii(git(site, ["rev-parse", "HEAD"])) !== siteCommit) {
    throw new Error("SOURCE_HEAD_MISMATCH");
  }
  if (git(site, ["status", "--porcelain=v1"]).length !== 0) {
    throw new Error("SOURCE_WORKTREE_DIRTY");
  }
  const siteFormat = ascii(git(site, ["rev-parse", "--show-object-format"]));
  const candidateFormat = ascii(git(candidate, ["rev-parse", "--show-object-format"]));
  if (siteFormat !== "sha1" || candidateFormat !== siteFormat) {
    throw new Error("TREE_FORMAT_MISMATCH");
  }
  let manifest;
  try {
    manifest = JSON.parse(git(site, ["show", `${siteCommit}:.openai/hosting.json`]).toString("utf8"));
  } catch { throw new Error("SOURCE_MANIFEST_INVALID"); }
  if (manifest?.project_id !== options.get("--project-id")) {
    throw new Error("SOURCE_PROJECT_MISMATCH");
  }
  const candidateSubtree = options.get("--candidate-subtree");
  const siteTree = ascii(git(site, ["rev-parse", `${siteCommit}^{tree}`]));
  const candidateTree = ascii(git(candidate, ["rev-parse", candidateSubtree === "."
    ? `${candidateCommit}^{tree}`
    : `${candidateCommit}:${candidateSubtree}`]));
  if (ascii(git(site, ["cat-file", "-t", siteTree])) !== "tree" ||
    ascii(git(candidate, ["cat-file", "-t", candidateTree])) !== "tree") {
    throw new Error("GIT_INSPECTION_FAILED");
  }
  const siteEntries = entries(site, siteTree);
  const candidateEntries = entries(candidate, candidateTree);
  let common = 0;
  let identical = 0;
  for (const [name, header] of siteEntries) {
    if (!candidateEntries.has(name)) continue;
    common += 1;
    if (candidateEntries.get(name) === header) identical += 1;
  }
  const result = {
    profile: "kfm.sites.source-tree-comparison.v1",
    scope: "COMMITTED_GIT_TREES_ONLY",
    site_commit: siteCommit,
    site_tree: siteTree,
    candidate_commit: candidateCommit,
    candidate_tree: candidateTree,
    outcome: siteTree === candidateTree ? "MATCH" : "DIFFERENT",
    counts: {
      site: siteEntries.size,
      candidate: candidateEntries.size,
      common,
      identical,
      changed: common - identical,
      site_only: siteEntries.size - common,
      candidate_only: candidateEntries.size - common,
    },
    authority: "NONE; Site version binding, review, deployment, and acceptance require separate evidence",
  };
  return result;
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  try {
    const result = compareSiteSourceTrees(process.argv.slice(2));
    process.stdout.write(`${JSON.stringify(result, null, 2)}\n`);
    process.exitCode = result.outcome === "MATCH" ? 0 : 1;
  } catch (error) {
    const code = error instanceof Error && ERROR_CODES.has(error.message)
      ? error.message
      : "UNKNOWN";
    process.stderr.write(`SITE_SOURCE_COMPARISON_ERROR: ${code}\n`);
    process.exitCode = 2;
  }
}
