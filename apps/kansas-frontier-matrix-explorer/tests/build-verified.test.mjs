import test from "node:test";
import assert from "node:assert/strict";
import { chmod, mkdir, mkdtemp, readFile, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import path from "node:path";
import { spawnSync } from "node:child_process";

const script = new URL("../scripts/build-verified.sh", import.meta.url).pathname;
const linuxOnly = { skip: process.platform !== "linux" };

async function executable(file, body) {
  await mkdir(path.dirname(file), { recursive: true });
  await writeFile(file, body);
  await chmod(file, 0o755);
}

async function fixture({ withSource = true, appLocal = false } = {}) {
  const root = await mkdtemp(path.join(tmpdir(), "kfm-vite-build-"));
  const app = path.join(root, "apps", "kansas-frontier-matrix-explorer");
  await mkdir(path.join(app, "scripts"), { recursive: true });
  await writeFile(path.join(app, "scripts", "build-verified.sh"), await readFile(script));
  await chmod(path.join(app, "scripts", "build-verified.sh"), 0o755);
  await executable(path.join(app, "scripts", "sites-env.sh"), '#!/usr/bin/env bash\nexport SITES_ENV_READY=1\nexport SITES_PROJECT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"\nexec "$@"\n');
  if (withSource) {
    await mkdir(path.join(root, "packages", "maplibre", "src"), { recursive: true });
    await writeFile(path.join(root, "packages", "maplibre", "src", "index.ts"), "export {};\n");
  }
  const bin = appLocal ? path.join(app, "node_modules", ".bin") : path.join(root, "node_modules", ".bin");
  return { root, app, bin };
}

function run(app, env = {}) {
  return spawnSync("bash", [path.join(app, "scripts", "build-verified.sh")], {
    cwd: app,
    encoding: "utf8",
    env: { ...process.env, ...env },
  });
}

test("build wrapper accepts a workspace-hoisted Vite executable", linuxOnly, async () => {
  const { app, bin } = await fixture();
  const record = path.join(app, "vite-args.txt");
  await executable(path.join(bin, "vite"), `#!/usr/bin/env bash\nprintf "%s\\n" "$*" > "${record}"\n`);
  const result = run(app, { PATH: `${bin}:${process.env.PATH}` });
  assert.equal(result.status, 0, result.stderr);
  assert.match(result.stdout, /Running bounded Vite build/);
  assert.equal((await readFile(record, "utf8")).trim(), "build");
});

test("build wrapper preserves the app-local Vite fallback", linuxOnly, async () => {
  const { app, bin } = await fixture({ appLocal: true });
  await executable(path.join(bin, "vite"), "#!/usr/bin/env bash\nexit 0\n");
  assert.equal(run(app, { PATH: "/usr/bin:/bin" }).status, 0);
});

test("build wrapper fails closed when Vite is absent", linuxOnly, async () => {
  const { app } = await fixture();
  const result = run(app, { PATH: "/usr/bin:/bin" });
  assert.equal(result.status, 69);
  assert.match(result.stderr, /vite is unavailable/);
});

test("build wrapper rejects missing sibling source before invoking Vite", linuxOnly, async () => {
  const { app, bin } = await fixture({ withSource: false });
  await executable(path.join(bin, "vite"), "#!/usr/bin/env bash\nexit 0\n");
  const result = run(app, { PATH: `${bin}:${process.env.PATH}` });
  assert.equal(result.status, 66);
  assert.match(result.stderr, /BUILD_CONTEXT_INCOMPLETE/);
});

test("build wrapper preserves Vite's nonzero exit", linuxOnly, async () => {
  const { app, bin } = await fixture();
  await executable(path.join(bin, "vite"), "#!/usr/bin/env bash\nexit 23\n");
  assert.equal(run(app, { PATH: `${bin}:${process.env.PATH}` }).status, 23);
});
