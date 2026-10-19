import { readFileSync, statSync } from "node:fs";
import { createRequire } from "node:module";

const root = new URL("../", import.meta.url);
const packageJson = JSON.parse(readFileSync(new URL("package.json", root), "utf8"));
const nodeComposition = packageJson.scripts?.start === "node server/start.mjs";
const require = createRequire(import.meta.url);

function unavailable(label, missing) {
  if (!missing.length) return false;
  const reason = `${label} requires ${missing.join(", ")}`;
  // Other compositions must not silently turn missing required build inputs
  // into successful tests. This exception belongs to the standalone Node app.
  if (!nodeComposition) throw new Error(reason);
  return `${reason}; not shipped by the standalone GoDaddy Node composition`;
}

function missingPaths(paths) {
  const missing = paths.filter(path => {
    try { statSync(new URL(path, root)); return false; }
    catch (error) { if (error.code === "ENOENT") return true; throw error; }
  });
  return missing;
}

// Source files belong to this composition even when their platform integration
// cannot run. A partial/sparse checkout must fail instead of hiding omissions.
export function requireSourceFiles(paths) {
  for (const path of paths) statSync(new URL(path, root));
}

export function workerConfigurationPrerequisite() {
  return unavailable("Cloudflare Worker build", missingPaths(["dist/server/wrangler.json"]));
}

export function externalSourcePrerequisite(paths, label) {
  for (const path of paths) {
    if (new URL(path, root).href.startsWith(root.href)) throw new Error("Application source cannot be an optional external prerequisite");
  }
  return unavailable(label, missingPaths(paths));
}

export function workerPrerequisite({ viaWrangler = false, builtApplication = false } = {}) {
  let runtimeRequire = require;
  const missing = [];
  if (viaWrangler) {
    try { runtimeRequire = createRequire(require.resolve("wrangler")); }
    catch (error) { if (error.code !== "MODULE_NOT_FOUND") throw error; missing.push("wrangler"); }
  }
  if (!missing.length) {
    try { runtimeRequire.resolve("miniflare"); }
    catch (error) { if (error.code !== "MODULE_NOT_FOUND") throw error; missing.push("miniflare"); }
  }
  const filesReason = builtApplication && workerConfigurationPrerequisite();
  const runtimeReason = unavailable("Cloudflare Worker integration", missing);
  return {
    skip: [filesReason, runtimeReason].filter(Boolean).join("; ") || false,
    // Loading and all actual Worker errors remain ordinary test failures.
    load: () => runtimeRequire("miniflare"),
  };
}
