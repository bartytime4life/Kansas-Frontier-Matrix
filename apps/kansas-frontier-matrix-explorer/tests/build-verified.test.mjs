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
  [path.join(projectRoot, "scripts", "build-verified.sh")],
  {
    encoding: "utf8",
    cwd: projectRoot,
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


// This is a wrapper-control fixture, not a compiled or rendered KFM application.
// Keep it test-only: no package install, renderer acquisition, or source admission.
const createProject = async (root, { sourceEntry = "file" } = {}) => {
  const projectRoot = path.join(root, "apps", "kansas-frontier-matrix-explorer");
  const scripts = path.join(projectRoot, "scripts");
  await mkdir(scripts, { recursive: true });
  await writeExecutable(path.join(scripts, "build-verified.sh"), await readFile(buildScript, "utf8"));
  await writeFile(
    path.join(scripts, "sites-env.sh"),
    await readFile(new URL("../scripts/sites-env.sh", import.meta.url), "utf8"),
    "utf8",
  );
  const entry = path.join(root, "packages", "maplibre", "src", "index.ts");
  if (sourceEntry === "file") {
    await mkdir(path.dirname(entry), { recursive: true });
    await writeFile(entry, "// Synthetic minimum-input marker; not a renderer.\n", "utf8");
  } else if (sourceEntry === "directory") {
    await mkdir(entry, { recursive: true });
  } else {
    assert.equal(sourceEntry, "absent");
  }
  return projectRoot;
};

test("build wrapper accepts a workspace-hoisted vinext from npm PATH", linuxOnly, async (t) => {
  const root = await mkdtemp(path.join(tmpdir(), "kfm-vinext-workspace-"));
  t.after(() => rm(root, { recursive: true, force: true }));

  const projectRoot = await createProject(root);
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
  const projectRoot = await createProject(root);
  await mkdir(projectRoot, { recursive: true });

  const result = runBuild(projectRoot, "/usr/bin:/bin");

  assert.equal(result.status, 69, result.stderr || result.stdout);
  assert.match(result.stderr, /vinext is unavailable from the npm script PATH and app-local node_modules/);
});

test("build wrapper rejects a vinext executable outside node_modules", linuxOnly, async (t) => {
  const root = await mkdtemp(path.join(tmpdir(), "kfm-vinext-boundary-"));
  t.after(() => rm(root, { recursive: true, force: true }));
  const projectRoot = await createProject(root);
  const untrustedBin = path.join(root, "bin");
  await mkdir(projectRoot, { recursive: true });
  await writeExecutable(path.join(untrustedBin, "vinext"), "#!/usr/bin/env bash\nexit 0\n");

  const result = runBuild(projectRoot, `${untrustedBin}:/usr/bin:/bin`);

  assert.equal(result.status, 69, result.stderr || result.stdout);
  assert.match(result.stderr, /vinext is unavailable from the npm script PATH and app-local node_modules/);
});


test("build wrapper preserves app-local vinext fallback", linuxOnly, async (t) => {
  const root = await mkdtemp(path.join(tmpdir(), "kfm-vinext-local-"));
  t.after(() => rm(root, { recursive: true, force: true }));
  const projectRoot = await createProject(root);
  await writeExecutable(
    path.join(projectRoot, "node_modules", ".bin", "vinext"),
    "#!/usr/bin/env bash\n[[ \"$*\" == build ]]\n",
  );
  const result = runBuild(projectRoot, "/usr/bin:/bin");
  assert.equal(result.status, 0, result.stderr || result.stdout);
});

for (const sourceEntry of ["absent", "directory"]) {
  test(`build wrapper rejects ${sourceEntry} sibling source before invoking vinext`, linuxOnly, async (t) => {
    const root = await mkdtemp(path.join(tmpdir(), "kfm-vinext-source-"));
    t.after(() => rm(root, { recursive: true, force: true }));
    const projectRoot = await createProject(root, { sourceEntry });
    const bin = path.join(projectRoot, "node_modules", ".bin");
    const invocationRecord = path.join(root, "unexpected-build.txt");
    await writeExecutable(
      path.join(bin, "vinext"),
      '#!/usr/bin/env bash\nprintf "unexpected build\\n" > "${KFM_TEST_VINEXT_ARGS:?}"\n',
    );
    const result = runBuild(projectRoot, `${bin}:/usr/bin:/bin`, {
      KFM_TEST_VINEXT_ARGS: invocationRecord,
    });
    assert.equal(result.status, 66, result.stderr || result.stdout);
    assert.match(result.stderr, /BUILD_CONTEXT_INCOMPLETE: the @kfm\/maplibre workspace source entry/);
    assert.match(result.stderr, /app-only export needs a verified source-assembly step/);
    assert.doesNotMatch(result.stdout, /Running bounded vinext build/);
    await assert.rejects(readFile(invocationRecord), { code: "ENOENT" });
  });
}

test("build wrapper preserves the builder's nonzero exit", linuxOnly, async (t) => {
  const root = await mkdtemp(path.join(tmpdir(), "kfm-vinext-exit-"));
  t.after(() => rm(root, { recursive: true, force: true }));
  const projectRoot = await createProject(root);
  const bin = path.join(projectRoot, "node_modules", ".bin");
  await writeExecutable(path.join(bin, "vinext"), "#!/usr/bin/env bash\nexit 23\n");
  const result = runBuild(projectRoot, `${bin}:/usr/bin:/bin`);
  assert.equal(result.status, 23, result.stderr || result.stdout);
});

test("build wrapper initializes sites-env and preserves a source layout containing spaces", linuxOnly, async (t) => {
  const root = await mkdtemp(path.join(tmpdir(), "kfm source layout "));
  t.after(() => rm(root, { recursive: true, force: true }));
  const projectRoot = await createProject(root);
  const bin = path.join(root, "node_modules", ".bin");
  const invocationRecord = path.join(root, "working-directory.txt");
  await writeExecutable(
    path.join(bin, "vinext"),
    '#!/usr/bin/env bash\nprintf "%s\\n" "$PWD" > "${KFM_TEST_VINEXT_ARGS:?}"\n',
  );
  const result = runBuild(projectRoot, `${bin}:/usr/bin:/bin`, {
    SITES_ENV_READY: "0",
    KFM_TEST_VINEXT_ARGS: invocationRecord,
  });
  assert.equal(result.status, 0, result.stderr || result.stdout);
  assert.equal((await readFile(invocationRecord, "utf8")).trim(), projectRoot);
});

test("the minimum source-input gate follows the existing TypeScript and Vite alias", async () => {
  const config = JSON.parse(await readFile(new URL("../tsconfig.json", import.meta.url), "utf8"));
  const vite = await readFile(new URL("../vite.config.ts", import.meta.url), "utf8");
  assert.deepEqual(config.compilerOptions.paths["@kfm/maplibre"], ["../../packages/maplibre/src/index.ts"]);
  assert.match(vite, /find:\s*"@kfm\/maplibre"/);
  assert.match(vite, /new URL\("\.\.\/\.\.\/packages\/maplibre\/src\/index\.ts",\s*import\.meta\.url\)/);
});

test("non-authoritative Vercel projects disable automatic Git deployments", async () => {
  const expected = {
    $schema: "https://openapi.vercel.sh/vercel.json",
    git: { deploymentEnabled: false },
  };
  const configs = [
    ["Explorer", new URL("../vercel.json", import.meta.url)],
    ["USGS connector", new URL("../../../connectors/usgs/vercel.json", import.meta.url)],
  ];

  for (const [label, configUrl] of configs) {
    const actual = JSON.parse(await readFile(configUrl, "utf8"));
    assert.deepEqual(
      actual,
      expected,
      `${label} Vercel config must suspend Git deployment without adding an unadmitted adapter`,
    );
  }
});
