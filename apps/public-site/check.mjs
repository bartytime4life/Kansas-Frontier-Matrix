#!/usr/bin/env node
// Fail-closed checks on the built public-site bundle before it may be deployed.
// Usage: node apps/public-site/check.mjs [distDir]

import { existsSync, readFileSync, readdirSync } from "node:fs";
import { dirname, extname, join, relative, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const HERE = dirname(fileURLToPath(import.meta.url));
const dist = resolve(process.argv[2] || process.env.KFM_SITE_OUT || join(HERE, "dist"));

const REQUIRED = [
  "index.html",
  "404.html",
  ".htaccess",
  "robots.txt",
  "sitemap.xml",
  "favicon.svg",
  "kfm-site.json",
  "features.json",
  ".well-known/security.txt",
  "assets/styles.css",
  "assets/og.png",
];
const ALLOWED_EXT = new Set([".html", ".css", ".svg", ".png", ".json", ".txt", ".xml", ""]);
const MAX_TOTAL_BYTES = 10 * 1024 * 1024;
const FORBIDDEN = [
  [/-----BEGIN [A-Z ]*PRIVATE KEY-----/, "private key"],
  [/\b(?:ghp|gho|ghs|github_pat)_[A-Za-z0-9_]{20,}/, "GitHub token"],
  [/\bAKIA[0-9A-Z]{16}\b/, "AWS access key"],
  [/\{\{[A-Z0-9_]+\}\}/, "unfilled template placeholder"],
  [/(?:https?:\/\/)?(?:localhost|127\.0\.0\.1|0\.0\.0\.0)(?::\d+)?\//, "loopback address"],
];

const failures = [];
const fail = (msg) => failures.push(msg);

function walk(dir) {
  return readdirSync(dir, { withFileTypes: true }).flatMap((entry) => {
    const path = join(dir, entry.name);
    return entry.isDirectory() ? walk(path) : [path];
  });
}

if (!existsSync(dist)) {
  console.error(`No bundle at ${dist}; run node apps/public-site/build.mjs first.`);
  process.exit(1);
}

for (const file of REQUIRED) if (!existsSync(join(dist, file))) fail(`missing required file ${file}`);

const files = walk(dist);
let total = 0;
for (const path of files) {
  const rel = relative(dist, path);
  const ext = rel === ".htaccess" ? "" : extname(rel);
  // Read each file once and size the same bytes that are scanned.
  const bytes = readFileSync(path);
  total += bytes.length;
  if (!ALLOWED_EXT.has(ext) || (ext === "" && rel !== ".htaccess")) fail(`unexpected file type ${rel}`);
  if (ext === ".png") continue;
  const text = bytes.toString("utf8");
  for (const [pattern, label] of FORBIDDEN) if (pattern.test(text)) fail(`${rel} contains ${label}`);
}
if (total > MAX_TOTAL_BYTES) fail(`bundle is ${total} bytes; limit ${MAX_TOTAL_BYTES}`);

// Every same-site reference in the pages must resolve to a bundled file.
for (const page of ["index.html", "404.html"]) {
  const path = join(dist, page);
  if (!existsSync(path)) continue;
  const html = readFileSync(path, "utf8");
  for (const [, ref] of html.matchAll(/\b(?:href|src|srcset)="([^"]+)"/g)) {
    if (/^(?:https:|mailto:|#)/.test(ref)) continue;
    if (/^http:/.test(ref)) {
      fail(`${page} links over plain http: ${ref}`);
      continue;
    }
    const target = ref.split(/[?#]/)[0];
    const file = target === "/" ? "index.html" : target.replace(/^\//, "");
    if (!existsSync(join(dist, file))) fail(`${page} references missing ${ref}`);
  }
  for (const [img] of html.matchAll(/<img\b[^>]*>/g)) if (!/\balt="/.test(img)) fail(`${page} image lacks alt: ${img.slice(0, 80)}`);
}

try {
  const manifest = JSON.parse(readFileSync(join(dist, "kfm-site.json"), "utf8"));
  const features = JSON.parse(readFileSync(join(dist, "features.json"), "utf8"));
  if (manifest.commit !== features.commit) fail("kfm-site.json and features.json disagree on commit");
  if (manifest.features.total !== features.features.length) fail("feature totals disagree");
  if (!manifest.site?.startsWith("https://")) fail("manifest site is not https");
} catch (error) {
  fail(`manifest JSON: ${error.message}`);
}

const security = existsSync(join(dist, ".well-known/security.txt")) ? readFileSync(join(dist, ".well-known/security.txt"), "utf8") : "";
const expires = /^Expires: (.+)$/m.exec(security)?.[1];
if (!/^Contact: https:\/\//m.test(security)) fail("security.txt lacks an https Contact");
if (!expires || Date.parse(expires) <= Date.now()) fail("security.txt Expires is missing or past");

const htaccess = existsSync(join(dist, ".htaccess")) ? readFileSync(join(dist, ".htaccess"), "utf8") : "";
for (const needle of ["acme-challenge", "Strict-Transport-Security", "Content-Security-Policy", "Options -Indexes"]) {
  if (!htaccess.includes(needle)) fail(`.htaccess lacks ${needle}`);
}

if (failures.length) {
  console.error(`public-site check FAILED (${failures.length}):\n- ${failures.join("\n- ")}`);
  process.exit(1);
}
console.log(`public-site check passed: ${files.length} files, ${(total / 1024).toFixed(0)} KiB in ${dist}`);
