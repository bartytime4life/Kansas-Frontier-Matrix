import { readdir, readFile, stat } from "node:fs/promises";
import { createHash } from "node:crypto";
import { resolve, relative } from "node:path";

const root = resolve(process.argv[2] ?? "public");
const deniedRoots = new Set(["data", "history", ".git", ".wrangler", ".sites-runtime"]);
const failures = [];
const inventory = [];
let files = 0, bytes = 0;
async function walk(dir) {
  for (const entry of await readdir(dir, { withFileTypes: true })) {
    const path = resolve(dir, entry.name), rel = relative(root, path).replaceAll("\\", "/");
    if (entry.isSymbolicLink() || deniedRoots.has(rel.split("/")[0]) || /(?:^|\/)\.env(?:\.|$)/.test(rel) || /\.(?:sqlite|db|pem|key|tar|zip)$/i.test(rel)) { failures.push(rel); continue; }
    if (entry.isDirectory()) await walk(path);
    else if (entry.isFile()) {
      files++; const size = (await stat(path)).size; bytes += size;
      inventory.push({ path: rel, bytes: size, sha256: createHash("sha256").update(await readFile(path)).digest("hex") });
      if (/\.(?:json|csv|geojson|json\.gz)$/i.test(rel)) failures.push(rel);
      if (/\.(?:js|mjs|html|css|txt|json)$/i.test(rel)) {
        const text = await readFile(path, "utf8");
        if (/-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|\b(?:sk-proj-|github_pat_)[a-zA-Z0-9_]{16,}/.test(text)) failures.push(rel);
      }
    } else failures.push(rel);
  }
}
await walk(root);
const report = { profile: "kfm.public-asset-inventory/v1", root, files, bytes, unapproved_paths: [...new Set(failures)], outcome: failures.length ? "HOLD" : "PASS", data_publication_authorized: false, inventory };
console.log(JSON.stringify(report, null, 2));
if (failures.length) process.exitCode = 1;
