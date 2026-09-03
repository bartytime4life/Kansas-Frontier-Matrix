import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { chmod, mkdtemp, mkdir, readFile, rm, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";
import test from "node:test";

const buildScript = fileURLToPath(new URL("../scripts/build-verified.sh", import.meta.url));
const linuxOnly = { skip: process.platform !== "linux" };

const runBuild = (projectRoot, pathValue, extraEnvironment = {}) => spawnSync(
  "/usr/bin/bash",
  [buildScript],
  {
    encoding: "utf8",
    env: {
      ...process.env,
      PATH: pathValue,
      SITES_ENV_READY: "1",
      SITES_PROJECT_ROOT: projectRoot,
      SITES_BUILD_TIMEOUT: "15s",
      SITES_BUILD_KILL_AFTER: "2s",
      ...extraEnvironment,
    },
  },
);

const writeExecutable = async (filePath, source) => {
  await mkdir(path.dirname(filePath), { recursive: true });
  await writeFile(filePath, source, "utf8");
  await chmod(filePath, 0o755);
};

test("build wrapper accepts a workspace-hoisted vinext from npm PATH", linuxOnly, async (t) => {
  const root = await mkdtemp(path.join(tmpdir(), "kfm-vinext-workspace-"));
  t.after(() => rm(root, { recursive: true, force: true }));

  const projectRoot = path.join(root, "apps", "kansas-frontier-matrix-explorer");
  const workspaceBin = path.join(root, "node_modules", ".bin");
  const invocationRecord = path.join(root, "vinext-args.txt");
  await mkdir(projectRoot, { recursive: true });
  await writeExecutable(
    path.join(workspaceBin, "vinext"),
    [
      "#!/usr/bin/env bash",
      "set -euo pipefail",
      'printf "%s\\n" "$*" > "${KFM_TEST_VINEXT_ARGS:?}"',
      "",
    ].join("\n"),
  );

  const result = runBuild(
    projectRoot,
    `${workspaceBin}:/usr/bin:/bin`,
    { KFM_TEST_VINEXT_ARGS: invocationRecord },
  );

  assert.equal(result.status, 0, result.stderr || result.stdout);
  assert.match(result.stdout, /Running bounded vinext build from .*node_modules\/\.bin\/vinext/);
  assert.equal((await readFile(invocationRecord, "utf8")).trim(), "build");
});

test("build wrapper fails closed when vinext is absent", linuxOnly, async (t) => {
  const root = await mkdtemp(path.join(tmpdir(), "kfm-vinext-missing-"));
  t.after(() => rm(root, { recursive: true, force: true }));
  const projectRoot = path.join(root, "app");
  await mkdir(projectRoot, { recursive: true });

  const result = runBuild(projectRoot, "/usr/bin:/bin");

  assert.equal(result.status, 69, result.stderr || result.stdout);
  assert.match(result.stderr, /vinext is unavailable from the npm script PATH and app-local node_modules/);
});

test("build wrapper rejects a vinext executable outside node_modules", linuxOnly, async (t) => {
  const root = await mkdtemp(path.join(tmpdir(), "kfm-vinext-boundary-"));
  t.after(() => rm(root, { recursive: true, force: true }));
  const projectRoot = path.join(root, "app");
  const untrustedBin = path.join(root, "bin");
  await mkdir(projectRoot, { recursive: true });
  await writeExecutable(path.join(untrustedBin, "vinext"), "#!/usr/bin/env bash\nexit 0\n");

  const result = runBuild(projectRoot, `${untrustedBin}:/usr/bin:/bin`);

  assert.equal(result.status, 69, result.stderr || result.stdout);
  assert.match(result.stderr, /vinext is unavailable from the npm script PATH and app-local node_modules/);
});
