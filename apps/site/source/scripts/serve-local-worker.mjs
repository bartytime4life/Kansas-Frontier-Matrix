#!/usr/bin/env node
/** Serve the built Site on loopback using the lockfile's local Worker runtime. */
import { createHash } from "node:crypto";
import { lstatSync, mkdtempSync, readFileSync, readdirSync, realpathSync, rmSync } from "node:fs";
import { createRequire } from "node:module";
import { tmpdir } from "node:os";
import path from "node:path";
import { fileURLToPath } from "node:url";

const siteRoot = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..");
const versions = { wrangler: "4.127.1", miniflare: "5.20260828.0-alpha" };
const fail = (code) => { throw new Error(code); };
const equal = (a, b) => JSON.stringify(a) === JSON.stringify(b);
const populated = (value) => value && (typeof value !== "object" || Object.values(value).some(populated));

export function parseArguments(args) {
  const result = { port: 4173, state: null, localReviewedImagery: false };
  const seen = new Set();
  for (let i = 0; i < args.length; i++) {
    const arg = args[i];
    if (seen.has(arg)) fail("DUPLICATE_ARGUMENT");
    seen.add(arg);
    if (arg === "--local-reviewed-imagery") result.localReviewedImagery = true;
    else if (arg === "--port" && /^(?:[1-9][0-9]{3,4})$/.test(args[i + 1] ?? "")) result.port = Number(args[++i]);
    else if (arg === "--state" && args[i + 1] && !args[i + 1].startsWith("--")) result.state = path.resolve(args[++i]);
    else fail("INVALID_ARGUMENT");
  }
  if (result.port < 1024 || result.port > 65535) fail("INVALID_PORT");
  if (!result.state) fail("EXISTING_STATE_REQUIRED");
  if (result.localReviewedImagery && result.port !== 4173) fail("IMAGERY_ORIGIN_MUST_BE_4173");
  return result;
}

export function checkedPath(target, directory = false) {
  // The caller resolves the stable Site alias first; children cannot redirect.
  if (realpathSync(target) !== path.resolve(target)) fail("SYMLINK_PATH_REJECTED");
  const info = lstatSync(target);
  if (directory ? !info.isDirectory() : !info.isFile()) fail("WRONG_PATH_TYPE");
  if (info.uid !== process.getuid() || (info.mode & 0o002)) fail("UNSAFE_PATH_OWNER_OR_MODE");
  return info;
}

export function assertNoLocalSecretFiles(root) {
  // Wrangler reads both dotenv and .dev.vars files. The direct runtime must
  // not silently ignore an operator's configuration or read its secret values.
  if (readdirSync(root).some((name) => name === ".env" || name.startsWith(".env.") || name === ".dev.vars" || name.startsWith(".dev.vars."))) {
    fail("LOCAL_SECRET_CONFIGURATION_REQUIRES_REVIEW");
  }
}

export function validateConfiguration(config, hosting) {
  if (hosting.project_id !== "appgprj_6aa0b1c41bc08191bfd86003920f1631") fail("WRONG_SITE_PROJECT");
  if (config.name !== "kansas-frontier-matrix-explorer" || config.main !== "index.js" || config.no_bundle !== true) fail("UNSUPPORTED_BUILD");
  if (!equal(config.rules, [{ type: "ESModule", globs: ["**/*.js", "**/*.mjs"] }])) fail("UNSUPPORTED_MODULE_RULES");
  if (!equal(config.assets, { directory: "../client" })) fail("UNSUPPORTED_ASSETS");
  if (!equal(config.r2_buckets, [{ binding: "BUCKET", bucket_name: "site-creator-r2" }])) fail("R2_BINDING_CHANGED");
  const db = config.d1_databases;
  if (db?.length !== 1 || db[0].binding !== "DB" || db[0].database_name !== "site-creator-d1" || db[0].database_id !== "00000000-0000-4000-8000-000000000000" || db[0].remote) fail("D1_BINDING_CHANGED");
  if (populated(config.vars) || populated(config.define)) fail("UNREVIEWED_CONFIGURATION_VARIABLES");
}

export function collectModules(server, limit = 1024, maxBytes = 256 * 1024 * 1024) {
  checkedPath(server, true);
  const modules = [];
  let bytes = 0;
  let entries = 0;
  const visit = (directory, depth = 0) => {
    if (depth > 16) fail("MODULE_DEPTH_LIMIT");
    for (const name of readdirSync(directory).sort()) {
      if (++entries > limit) fail("MODULE_ENTRY_LIMIT");
      const file = path.join(directory, name);
      const info = lstatSync(file);
      checkedPath(file, info.isDirectory());
      if (info.isDirectory()) { visit(file, depth + 1); continue; }
      const type = /\.m?js$/.test(name) ? "ESModule" : /\.(?:txt|html|sql)$/.test(name) ? "Text" : /\.bin$/.test(name) ? "Data" : /\.wasm$/.test(name) ? "CompiledWasm" : null;
      if (!type) continue;
      bytes += info.size;
      if (bytes > maxBytes) fail("MODULE_BYTE_LIMIT");
      modules.push({ type, path: file });
    }
  };
  visit(server);
  const main = modules.find((m) => m.path === path.join(server, "index.js"));
  if (!main) fail("MISSING_WORKER_ENTRY");
  return [main, ...modules.filter((m) => m !== main)];
}

export function localEntry(port) {
  return `import worker from "./index.js";
export * from "./index.js";
export default { ...worker, fetch(request, env, ctx) {
  if (new URL(request.url).origin !== ${JSON.stringify(`http://127.0.0.1:${port}`)} ||
      [...request.headers.keys()].some((name) => name.startsWith("oai-authenticated-"))) {
    return new Response("Local request authority rejected.", { status: 403, headers: { "Cache-Control": "no-store" } });
  }
  return worker.fetch(request, env, ctx);
}};`;
}

export function prepareWorker(translated, server, client, modules, localReviewedImagery, port = 4173) {
  if (translated.main !== path.join(server, "index.js") || translated.externalWorkers.length || populated(translated.define)) fail("UNSUPPORTED_WORKER_TRANSLATION");
  const options = translated.workerOptions;
  const supported = new Set(["rootPath", "compatibilityDate", "compatibilityFlags", "modulesRules", "bindings", "r2Buckets", "d1Databases", "assets"]);
  for (const [key, value] of Object.entries(options)) {
    if (!supported.has(key) && populated(value)) fail("UNSUPPORTED_WORKER_BINDING");
  }
  if (populated(options.bindings) || options.assets?.directory !== client) fail("UNSUPPORTED_WORKER_BINDING");
  if (!equal(options.r2Buckets, { BUCKET: { id: "site-creator-r2" } }) || !equal(options.d1Databases, { DB: { id: "00000000-0000-4000-8000-000000000000" } })) fail("STORAGE_TRANSLATION_CHANGED");
  const worker = { ...options };
  delete worker.modulesRules;
  const entry = { type: "ESModule", path: path.join(server, "__kfm_local_entry.mjs"), contents: localEntry(port) };
  if (modules.some((module) => module.path === entry.path)) fail("LOCAL_ENTRY_COLLISION");
  return { ...worker, modules: [entry, ...modules], modulesRoot: server, bindings: localReviewedImagery ? { KFM_LOCAL_REVIEWED_IMAGERY_ORIGIN: "http://127.0.0.1:4173" } : {} };
}

export async function serve(args = process.argv.slice(2)) {
  const settings = parseArguments(args);
  const major = Number(process.versions.node.split(".")[0]);
  if (major !== 22 || Number(process.versions.node.split(".")[1]) < 13) fail("REQUIRES_NODE_22_13_OR_LATER_22_X");
  const server = path.join(siteRoot, "dist/server");
  const client = path.join(siteRoot, "dist/client");
  for (const directory of [client, settings.state, path.join(settings.state, "v3/d1"), path.join(settings.state, "v3/r2")]) checkedPath(directory, true);
  // Do not silently ignore developer secrets that Wrangler dev would load.
  assertNoLocalSecretFiles(siteRoot);
  const configPath = path.join(server, "wrangler.json");
  checkedPath(configPath);
  const configBytes = readFileSync(configPath);
  validateConfiguration(JSON.parse(configBytes), JSON.parse(readFileSync(path.join(siteRoot, ".openai/hosting.json"))));
  const modules = collectModules(server);
  process.env.WRANGLER_WRITE_LOGS = "false";
  const require = createRequire(import.meta.url);
  const runtimeRequire = createRequire(require.resolve("wrangler"));
  if (require("wrangler/package.json").version !== versions.wrangler || runtimeRequire("miniflare/package.json").version !== versions.miniflare) fail("RUNTIME_VERSION_REQUIRES_REVALIDATION");
  const { unstable_getMiniflareWorkerOptions } = require("wrangler");
  const { Miniflare, convertV4MiniflareOptions, Log, LogLevel } = runtimeRequire("miniflare");
  const translated = unstable_getMiniflareWorkerOptions(configPath);
  const worker = prepareWorker(translated, server, client, modules, settings.localReviewedImagery, settings.port);
  const temporary = mkdtempSync(path.join(tmpdir(), "kfm-local-worker-"));
  let runtime;
  let stopping;
  const stop = () => stopping ??= (async () => {
    try { await runtime?.dispose(); } finally { rmSync(temporary, { recursive: true, force: true }); }
  })();
  try {
    const signals = ["SIGINT", "SIGTERM", "SIGHUP"];
    const previousListeners = new Map(signals.map((signal) => [signal, new Set(process.listeners(signal))]));
    runtime = new Miniflare(convertV4MiniflareOptions({
      host: "127.0.0.1", port: settings.port, log: new Log(LogLevel.WARN),
      workers: [worker], resourcePersistencePath: path.join(settings.state, "v3"), resourceTmpPath: temporary,
    }));
    // This pinned Miniflare installs immediate-exit signal hooks. Replace only
    // hooks added by this constructor so dispose() finishes before exit. Keep
    // all pre-existing listeners and Miniflare's emergency process-exit hook.
    for (const signal of signals) {
      for (const listener of process.listeners(signal)) {
        if (!previousListeners.get(signal).has(listener)) process.removeListener(signal, listener);
      }
    }
    const onSignal = () => { stop().then(() => process.exit(0), () => process.exit(1)); };
    for (const signal of signals) process.once(signal, onSignal);
    const address = String(await runtime.ready);
    console.log(JSON.stringify({ event: "local_runtime_ready", address, versions, configSha256: createHash("sha256").update(configBytes).digest("hex"), entrySha256: createHash("sha256").update(readFileSync(translated.main)).digest("hex"), existingState: true, localReviewedImagery: settings.localReviewedImagery }));
    return { runtime, stop };
  } catch (error) { await stop(); throw error; }
}

// realpath also supports the owner's stable KFM-Explorer-Site-current alias.
if (process.argv[1] && realpathSync(process.argv[1]) === fileURLToPath(import.meta.url)) {
  serve().catch((error) => {
    console.error(JSON.stringify({ event: "local_runtime_failed", reason: /^[A-Z0-9_]+$/.test(error.message) ? error.message : "STARTUP_FAILED" }));
    process.exitCode = 1;
  });
}
