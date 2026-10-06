import assert from "node:assert/strict";
import { existsSync } from "node:fs";
import { chmod, mkdir, mkdtemp, readFile, rm, symlink, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { spawnSync } from "node:child_process";
import test from "node:test";
import {
  QWEN_LOCAL_MODEL,
  QWEN_LOCAL_MODEL_DIGEST,
  QWEN_LOCAL_OLLAMA_VERSION,
} from "../scripts/qwen-local-contract.mjs";

const installerPath = fileURLToPath(new URL("../scripts/install-local-qwen-macos.sh", import.meta.url));

const installSource = await readFile(
  new URL("../scripts/install-local-qwen-macos.sh", import.meta.url),
  "utf8",
);
const uninstallSource = await readFile(
  new URL("../scripts/uninstall-local-qwen-macos.sh", import.meta.url),
  "utf8",
);

test("installer pins Ollama CLI traffic and validates the copied runtime", () => {
  assert.match(installSource, /env OLLAMA_HOST="\$ollama_origin"/);
  assert.match(installSource, /Node\.js 22\.13\.0 or newer/);
  assert.match(installSource, /"\$installed_node" -e/);
  assert.match(installSource, /QWEN_LOCAL_OLLAMA_VERSION/);
  assert.match(installSource, /Run this installer as the signed-in macOS user/);
  assert.match(installSource, /escape_plist_text/);
  assert.match(installSource, /only current-user loopback listeners/);
  assert.match(installSource, /-iTCP:"\$ollama_port" -sTCP:LISTEN -Fpucn/);
});

test("installer rejects a wildcard Ollama listener before mutation", async (context) => {
  if (typeof process.getuid === "function" && process.getuid() === 0) {
    context.skip("the installer intentionally refuses root execution");
    return;
  }
  const fixture = await mkdtemp(join(tmpdir(), "kfm-qwen-listener-test."));
  const fakeBin = join(fixture, "bin");
  const fakeHome = join(fixture, "home");
  const installMarker = join(fixture, "install-command-ran");
  await mkdir(fakeBin);
  await mkdir(fakeHome);
  const fakeCommand = async (name, body) => {
    const path = join(fakeBin, name);
    await writeFile(path, `#!/bin/bash\n${body}\n`, "utf8");
    await chmod(path, 0o755);
  };
  try {
    await symlink(process.execPath, join(fakeBin, "node"));
    await fakeCommand("uname", "printf 'Darwin\\n'");
    await fakeCommand("ollama", "if [[ \"$1\" == \"list\" ]]; then printf 'NAME ID SIZE MODIFIED\\n'; exit 0; fi\nexit 1");
    await fakeCommand("lsof", `printf 'p5150\\nu${process.getuid()}\\ncollama\\nn*:11434\\n'`);
    await fakeCommand("install", `: > "${installMarker}"\nexit 99`);

    const result = spawnSync("/bin/bash", [installerPath], {
      cwd: dirname(installerPath),
      encoding: "utf8",
      env: {
        ...process.env,
        HOME: fakeHome,
        PATH: `${fakeBin}:/usr/bin:/bin:/usr/sbin:/sbin`,
        TMPDIR: fixture,
      },
    });
    assert.notEqual(result.status, 0, result.stderr);
    assert.match(result.stderr, /only current-user loopback listeners/);
    assert.equal(existsSync(installMarker), false, "installer mutated files after detecting a wildcard Ollama listener");
  } finally {
    await rm(fixture, { recursive: true, force: true });
  }
});

test("installer preserves the previous service until unload succeeds", () => {
  const unload = installSource.indexOf(
    'launchctl bootout "gui/$UID/$service_label"',
  );
  const firstInstall = installSource.indexOf(
    'install -m 0755 "$node_bin" "$installed_node"',
  );
  assert.ok(unload >= 0 && firstInstall > unload);
  assert.match(installSource, /restore_previous_installation/);
  assert.match(installSource, /trap restore_previous_installation ERR/);
  assert.match(installSource, /passed governed health checks/);
  assert.match(installSource, /Rollback is incomplete/);
  assert.match(installSource, /rollback_loaded/);
  assert.match(installSource, /rollback_ready/);
  assert.match(installSource, /preserve_backup=true/);
  assert.match(installSource, /Backup preserved at/);
  assert.match(installSource, /diff -qr/);
  assert.match(installSource, /cmp -s/);
  assert.match(installSource, /launchctl print-disabled/);
  assert.match(installSource, /previous_disabled/);
  assert.match(installSource, /launchctl disable/);
  assert.match(installSource, /no previous installation existed/);
  const restoredHealth = installSource.indexOf('rollback_ready" != true');
  const restoredDisable = installSource.indexOf(
    'launchctl disable "gui/$UID/$service_label"',
    restoredHealth,
  );
  const restoredClaim = installSource.indexOf(
    "restored and passed governed health checks",
    restoredHealth,
  );
  assert.ok(restoredHealth >= 0 && restoredDisable > restoredHealth && restoredClaim > restoredDisable);
});

test("installer enables before bootstrap and requires exact owned health", () => {
  const enable = installSource.indexOf(
    'launchctl enable "gui/$UID/$service_label"',
    installSource.indexOf("mutation_started=true"),
  );
  const bootstrap = installSource.indexOf(
    'launchctl bootstrap "gui/$UID" "$plist_path"',
    enable,
  );
  assert.ok(enable >= 0 && bootstrap > enable);
  assert.match(installSource, /localQwenHealthStatus\(payload\) === "ready"/);
  assert.match(installSource, /-p "\$service_pid" -iTCP:"\$bridge_port"/);
  assert.match(installSource, /"\$http_status" == "200"/);
});

test("an unload fault exits before any replacement command can run", async (context) => {
  if (typeof process.getuid === "function" && process.getuid() === 0) {
    context.skip("the installer intentionally refuses root execution");
    return;
  }
  const fixture = await mkdtemp(join(tmpdir(), "kfm-qwen-installer-test."));
  const fakeBin = join(fixture, "bin");
  const fakeHome = join(fixture, "home");
  const installMarker = join(fixture, "install-command-ran");
  await mkdir(fakeBin);
  await mkdir(fakeHome);
  const fakeCommand = async (name, body) => {
    const path = join(fakeBin, name);
    await writeFile(path, `#!/bin/bash\n${body}\n`, "utf8");
    await chmod(path, 0o755);
  };
  try {
    await symlink(process.execPath, join(fakeBin, "node"));
    await fakeCommand("uname", "printf 'Darwin\\n'");
    await fakeCommand("ollama", `if [[ "$1" == "list" ]]; then printf 'NAME ID SIZE MODIFIED\\n%s id 5.2GB now\\n' '${QWEN_LOCAL_MODEL}'; exit 0; fi\nexit 1`);
    await fakeCommand("curl", `case "$*" in\n  *'/api/version'*) printf '%s\\n' '${JSON.stringify({ version: QWEN_LOCAL_OLLAMA_VERSION })}' ;;\n  *'/api/tags'*) printf '%s\\n' '${JSON.stringify({ models: [{ name: QWEN_LOCAL_MODEL, digest: QWEN_LOCAL_MODEL_DIGEST }] })}' ;;\n  *) exit 1 ;;\nesac`);
    await fakeCommand("launchctl", "case \"$1\" in\n  print-disabled) exit 0 ;;\n  print) printf 'pid = 4242\\n'; exit 0 ;;\n  bootout) exit 37 ;;\n  *) exit 1 ;;\nesac");
    await fakeCommand("plutil", "exit 0");
    await fakeCommand("lsof", `if [[ "$*" == *"-iTCP:11434"* ]]; then printf 'p4241\\nu${process.getuid()}\\ncollama\\nn127.0.0.1:11434\\n'; exit 0; fi\nexit 1`);
    await fakeCommand("install", ": > \"${KFM_INSTALL_MARKER:?}\"\nexit 99");

    const result = spawnSync("/bin/bash", [installerPath], {
      cwd: dirname(installerPath),
      encoding: "utf8",
      env: {
        ...process.env,
        HOME: fakeHome,
        KFM_INSTALL_MARKER: installMarker,
        PATH: `${fakeBin}:/usr/bin:/bin:/usr/sbin:/sbin`,
        TMPDIR: fixture,
      },
    });
    assert.notEqual(result.status, 0, result.stderr);
    assert.match(result.stderr, /could not be unloaded; no files were replaced/);
    assert.equal(existsSync(installMarker), false, "replacement install command ran after the unload fault");
    assert.doesNotMatch(result.stdout, /installed and ready/);
  } finally {
    await rm(fixture, { recursive: true, force: true });
  }
});

test("uninstaller refuses to delete files while the service or process remains", () => {
  const bootout = uninstallSource.indexOf(
    'launchctl bootout "gui/$UID/$service_label"',
  );
  const processCheck = uninstallSource.indexOf(
    'pgrep -f "$support_root/scripts/local-qwen-bridge.mjs"',
  );
  const listenerCheck = uninstallSource.indexOf(
    'lsof_bin" -nP -iTCP:"$bridge_port" -sTCP:LISTEN',
  );
  const firstRemoval = uninstallSource.indexOf('rm -f "$plist_path"');
  assert.ok(bootout >= 0 && processCheck > bootout && listenerCheck > processCheck && firstRemoval > listenerCheck);
  assert.match(uninstallSource, /could not be unloaded; no files were removed/);
  assert.match(uninstallSource, /is still registered; no files were removed/);
  assert.match(uninstallSource, /process is still running; no files were removed/);
  assert.match(uninstallSource, /still listening on the governed local Qwen port; no files were removed/);
  assert.match(uninstallSource, /QWEN_LOCAL_BRIDGE_PORT/);
  assert.doesNotMatch(uninstallSource, /rm\s+-rf/);
});

test("uninstaller retains Ollama, its model, and logs by default", () => {
  assert.match(uninstallSource, /Ollama and its model were left unchanged/);
  assert.match(uninstallSource, /if \[\[ "\$remove_logs" == true \]\]/);
  assert.doesNotMatch(uninstallSource, /ollama\s+(rm|stop)/);
});
