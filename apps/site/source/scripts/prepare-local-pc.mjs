#!/usr/bin/env node
/** Prepare private local input/recovery folders without moving or serving data. */

import { lstat, mkdir, readFile } from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";

const siteRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const expectedProject = "appgprj_6aa0b1c41bc08191bfd86003920f1631";

async function checkedDirectory(target, home) {
  const absolute = path.resolve(target);
  if (absolute === home || !absolute.startsWith(home + path.sep)) throw new Error("TARGET_OUTSIDE_HOME");
  let current = home;
  for (const part of path.relative(home, absolute).split(path.sep)) {
    current = path.join(current, part);
    try {
      const state = await lstat(current);
      if (state.isSymbolicLink() || !state.isDirectory()) throw new Error("UNSAFE_PATH_COMPONENT");
    } catch (error) {
      if (error?.code === "ENOENT") return "MISSING";
      throw error;
    }
  }
  const targetState = await lstat(absolute);
  if ((targetState.mode & 0o077) !== 0) throw new Error(`INSECURE_DIRECTORY_MODE: ${absolute}; run chmod 700 on this folder after reviewing its contents`);
  return "PRESENT";
}

export async function inspectLocalPc(home = os.homedir(), apply = false) {
  const absoluteHome = path.resolve(home);
  const homeState = await lstat(absoluteHome);
  if (!homeState.isDirectory() || homeState.isSymbolicLink()) throw new Error("UNSAFE_HOME");
  const hosting = JSON.parse(await readFile(path.join(siteRoot, ".openai/hosting.json"), "utf8"));
  if (hosting.project_id !== expectedProject) throw new Error("WRONG_SITE_PROJECT");
  const targets = [
    { id: "download_inbox", path: path.join(absoluteHome, "Downloads", "KFM") },
    { id: "reference_library", path: path.join(absoluteHome, "KFM-references") },
    { id: "site_recovery", path: path.join(absoluteHome, "KFM-site-recovery") },
  ];
  // Inspect every path before writing. A symlink or non-directory blocks all writes.
  const before = await Promise.all(targets.map(async (target) => ({
    ...target, state: await checkedDirectory(target.path, absoluteHome),
  })));
  if (apply) {
    for (const target of before.filter((target) => target.state === "MISSING")) {
      await mkdir(target.path, { recursive: true, mode: 0o700 });
      if (await checkedDirectory(target.path, absoluteHome) !== "PRESENT") throw new Error("CREATE_VERIFICATION_FAILED");
    }
  }
  return {
    format: "kfm-site-local-pc-layout-v1",
    site_project: expectedProject,
    site_source: siteRoot,
    action: apply ? "PREPARED_INPUT_AND_RECOVERY_DIRECTORIES" : "INSPECTED_ONLY",
    directories: await Promise.all(targets.map(async (target) => ({
      ...target, state: await checkedDirectory(target.path, absoluteHome),
    }))),
    kfm_data_root: path.join(absoluteHome, "KFM-data"),
    kfm_data_root_owner: "Kansas-Frontier-Matrix/tools/local_data/manage.py init",
    public_site_effect: "NONE",
  };
}

if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url)) {
  const args = process.argv.slice(2);
  if (args.some((arg) => arg !== "--apply") || args.length > 1) {
    console.error("Usage: node scripts/prepare-local-pc.mjs [--apply]");
    process.exitCode = 2;
  } else {
    try {
      console.log(JSON.stringify(await inspectLocalPc(os.homedir(), args[0] === "--apply"), null, 2));
    } catch (error) {
      console.error(`Local PC layout blocked: ${error instanceof Error ? error.message : "UNKNOWN_ERROR"}`);
      process.exitCode = 1;
    }
  }
}
