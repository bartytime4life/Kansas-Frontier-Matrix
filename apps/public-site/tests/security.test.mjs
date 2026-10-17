import assert from "node:assert/strict";
import { spawn, spawnSync } from "node:child_process";
import { createHash } from "node:crypto";
import { cpSync, mkdirSync, mkdtempSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import http from "node:http";
import https from "node:https";
import net from "node:net";
import { tmpdir } from "node:os";
import { dirname, join, resolve } from "node:path";
import { after, before, test } from "node:test";
import { fileURLToPath } from "node:url";
import { runInNewContext } from "node:vm";
import { build, DEFAULTS, escapeRegex } from "../build.mjs";

const REPO = resolve(dirname(fileURLToPath(import.meta.url)), "../../..");
const scratch = mkdtempSync(join(tmpdir(), "kfm-public-security-"));
const dist = join(scratch, "bundle");
const workflow = readFileSync(join(REPO, ".github/workflows/godaddy-public-site.yml"), "utf8");
const deploy = workflow.split(/^  deploy:\s*$/m)[1];
const env = { ...process.env, KFM_SITE_ORIGIN: DEFAULTS.origin, KFM_EXPLORER_URL: DEFAULTS.explorerUrl,
  KFM_BUILD_COMMIT: "a".repeat(40), KFM_BUILD_TIME: new Date().toISOString(), KFM_SITE_OUT: dist };
let server;
let httpPort;
let httpsPort;
let diagnostics = "";
let localCa;

function check(directory = dist, args = []) {
  return spawnSync(process.execPath, [...args, join(REPO, "apps/public-site/check.mjs"), directory], { encoding: "utf8" });
}

function mutatedBundle(name, mutate) {
  const directory = join(scratch, name);
  cpSync(dist, directory, { recursive: true });
  mutate(directory);
  return directory;
}

async function unusedPort() {
  const listener = net.createServer();
  await new Promise((resolve, reject) => { listener.once("error", reject); listener.listen(0, "127.0.0.1", resolve); });
  const port = listener.address().port;
  await new Promise((resolve) => listener.close(resolve));
  return port;
}

function request(path, { tls = false, host = "kansasfrontiermatrix.com", headers = {} } = {}) {
  return new Promise((resolve, reject) => {
    const transport = tls ? https : http;
    // Verify TLS against the throwaway local certificate rather than disabling validation.
    const trust = tls ? { ca: localCa, servername: "localhost", rejectUnauthorized: true } : {};
    transport.get({ hostname: "127.0.0.1", port: tls ? httpsPort : httpPort, path,
      ...trust, headers: { Host: host, ...headers }, timeout: 2000 }, (response) => {
      response.resume();
      response.on("end", () => resolve({ status: response.statusCode, headers: response.headers }));
    }).on("error", reject).on("timeout", function () { this.destroy(new Error("local Apache request timeout")); });
  });
}

before(async () => {
  await build(env);
  assert.equal(check().status, 0, check().stderr);
  mkdirSync(join(dist, ".well-known/acme-challenge"), { recursive: true });
  mkdirSync(join(dist, ".well-known/pki-validation"), { recursive: true });
  writeFileSync(join(dist, ".well-known/acme-challenge/token"), "local challenge");
  writeFileSync(join(dist, ".well-known/pki-validation/token"), "local validation");
  writeFileSync(join(dist, ".private"), "never public");
  const cert = spawnSync("openssl", ["req", "-x509", "-newkey", "rsa:2048", "-nodes", "-days", "1",
    "-subj", "/CN=localhost", "-addext", "subjectAltName=DNS:localhost",
    "-keyout", join(scratch, "key.pem"), "-out", join(scratch, "cert.pem")], { encoding: "utf8" });
  assert.equal(cert.status, 0, cert.stderr);
  localCa = readFileSync(join(scratch, "cert.pem"));
  httpPort = await unusedPort();
  httpsPort = await unusedPort();
  const modules = process.env.KFM_APACHE_MODULES || "/usr/lib/apache2/modules";
  const moduleNames = ["mpm_event", "authz_core", "authz_host", "dir", "mime", "rewrite", "headers", "ssl", "socache_shmcb"];
  const config = [
    `ServerRoot "${scratch}"`, `PidFile "${scratch}/httpd.pid"`, `ErrorLog "${scratch}/error.log"`,
    "ServerName localhost", `Listen 127.0.0.1:${httpPort}`, `Listen 127.0.0.1:${httpsPort}`,
    ...moduleNames.map((name) => `LoadModule ${name}_module "${modules}/mod_${name}.so"`),
    "User nobody", "Group nogroup", `TypesConfig "${scratch}/mime.types"`,
    `DocumentRoot "${dist}"`, `<Directory "${dist}">`, "AllowOverride All", "Require all granted", "</Directory>",
    `<VirtualHost 127.0.0.1:${httpsPort}>`, "SSLEngine on", `SSLCertificateFile "${scratch}/cert.pem"`,
    `SSLCertificateKeyFile "${scratch}/key.pem"`, "</VirtualHost>",
  ].join("\n");
  writeFileSync(join(scratch, "mime.types"), "text/html html\ntext/css css\nimage/png png\n");
  writeFileSync(join(scratch, "httpd.conf"), config);
  const binary = process.env.KFM_APACHE_BIN || "/usr/sbin/apache2";
  const args = ["-X", "-f", join(scratch, "httpd.conf")];
  // Optional container-only adapter for a namespace with only uid 0 mapped.
  // CI uses Apache directly under the runner's normal unprivileged account.
  server = process.env.KFM_APACHE_UNMAPPED_USER === "true"
    ? spawn("unshare", ["--user", binary, ...args]) : spawn(binary, args);
  server.on("error", (error) => { diagnostics += error.message; });
  server.stderr.on("data", (data) => { diagnostics += data; });
  for (let attempt = 0; attempt < 50; attempt++) {
    try { await request("/"); return; } catch { await new Promise((resolve) => setTimeout(resolve, 50)); }
  }
  let log = "";
  try { log = readFileSync(join(scratch, "error.log"), "utf8"); } catch { /* Startup may fail before the log is opened. */ }
  assert.fail(`Apache unavailable: ${diagnostics}\n${log}`);
});

after(async () => {
  if (server?.pid && server.exitCode === null && server.signalCode === null) {
    const exited = new Promise((resolve) => server.once("exit", resolve));
    server.kill("SIGTERM");
    await exited;
  }
  rmSync(scratch, { recursive: true, force: true });
});

test("actual deployment predicate denies unauthorized events, refs and disabled states", () => {
  const expression = /^    if: \$\{\{ (.+) \}\}$/m.exec(deploy)?.[1];
  assert.ok(expression, "credential job needs an explicit gate");
  // Evaluate only the bounded boolean/comparison grammar used by this gate;
  // never execute run steps. GitHub string comparisons are case-insensitive.
  assert.match(expression, /^(?:vars\.GODADDY_DEPLOY_ENABLED|github\.ref_protected|github\.ref|github\.event_name|true|'[^']*'| == | && | \|\| |[()])+$/);
  for (const enabled of [undefined, "", "false", "true"]) {
    for (const event of ["push", "workflow_dispatch", "pull_request", "pull_request_target", "workflow_run", "repository_dispatch"]) {
      for (const ref of ["refs/heads/main", "refs/heads/attacker", "refs/tags/main", "refs/tags/release", "refs/pull/5105/merge", "refs/heads/main-evil", ""]) {
        for (const protectedRef of [false, true]) {
          const allowed = runInNewContext(expression, { vars: { GODADDY_DEPLOY_ENABLED: enabled }, github: { ref, ref_protected: protectedRef, event_name: event } });
          assert.equal(allowed, enabled === "true" && protectedRef && ref === "refs/heads/main" && ["push", "workflow_dispatch"].includes(event), `${enabled}/${event}/${ref}/${protectedRef}`);
        }
      }
    }
  }
});

test("hosting secrets remain confined to guarded environment and immutable event checkout", () => {
  assert.match(deploy, /needs: build/);
  assert.match(deploy, /environment:\n      name: godaddy-production/);
  const steps = deploy.split(/^      - name: /m);
  const secretSteps = steps.filter((step) => /\$\{\{ secrets\./.test(step));
  assert.equal(secretSteps.length, 1);
  assert.match(secretSteps[0], /^Mirror bundle to GoDaddy hosting/);
  assert.equal((workflow.match(/\$\{\{ secrets\./g) || []).length, 5);
  assert.equal((workflow.match(/ref: \$\{\{ github.sha \}\}/g) || []).length, 2);
  assert.equal((workflow.match(/persist-credentials: false/g) || []).length, 2);
  assert.doesNotMatch(workflow, /secrets: inherit|pull_request_target:|inputs\.(?:ref|commit|branch|tag)/);
  assert.match(workflow.split(/^  deploy:/m)[0], /--test apps\/public-site\/tests\/security\.test\.mjs/);
  const runbook = readFileSync(join(REPO, "docs/runbooks/godaddy-hosting.md"), "utf8");
  assert.match(runbook, /exactly\s+one allowed policy: branch `main`/);
  assert.match(runbook, /reviewed pull request/);
  assert.match(runbook, /never roll back by dispatching an old branch\/tag/);
});

test("regex escaping treats every metacharacter as literal", () => {
  for (const value of ["kansasfrontiermatrix.com", "a\\b", "\\^$.*+?()[]{}|", "kfm+test.example:8443"]) {
    const pattern = new RegExp(`^${escapeRegex(value)}$`);
    assert.ok(pattern.test(value));
    assert.ok(!pattern.test(`${value}evil`));
  }
  assert.ok(!new RegExp(`^${escapeRegex("kfm.example")}$`).test("kfmXexample"));
});

test("transfer controls retain pinned SFTP, verified FTPS and deletion-off defaults", () => {
  const bin = join(scratch, "mock-bin");
  mkdirSync(bin);
  // No network client is executed. Capture only arguments for synthetic input.
  writeFileSync(join(bin, "lftp"), '#!/bin/sh\nprintf "%s\\n" "$@"\n', { mode: 0o755 });
  for (const protocol of ["sftp", "ftps"]) {
    const result = spawnSync("bash", [join(REPO, "infra/godaddy/deploy.sh")], {
      env: { PATH: `${bin}:${process.env.PATH}`, SITE_DIR: dist, GODADDY_HOST: "hosting.example",
        GODADDY_USER: "fixture", GODADDY_PASSWORD: "synthetic-only", GODADDY_PROTOCOL: protocol,
        GODADDY_KNOWN_HOSTS: "synthetic host pin", DRY_RUN: "true" }, encoding: "utf8",
    });
    assert.equal(result.status, 0, result.stderr);
    assert.match(result.stdout, /--dry-run/);
    assert.doesNotMatch(result.stdout, /--delete/);
    for (const path of ["acme-challenge", "pki-validation", "cgi-bin", ".user.ini", ".htpasswd"]) {
      assert.ok(result.stdout.includes(`--exclude-glob ${path.startsWith("acme") || path.startsWith("pki") ? ".well-known/" : ""}${path}`));
    }
    if (protocol === "sftp") {
      assert.match(result.stdout, /StrictHostKeyChecking=yes/);
      assert.match(result.stdout, /sftp:auto-confirm no/);
    } else {
      assert.match(result.stdout, /ftp:ssl-force true/);
      assert.match(result.stdout, /ssl:verify-certificate true/);
      assert.match(result.stdout, /ftp:ssl-protect-data true/);
    }
  }
});

test("all alias hosts and HTTP requests go directly to canonical HTTPS", async () => {
  for (const tls of [false, true]) {
    for (const host of ["www.kansasfrontiermatrix.com", "preview.cpanel.example", "kansasfrontiermatrix.com.evil", "kansasXfrontiermatrixXcom"]) {
      const response = await request("/features.json?test=1", { tls, host });
      assert.equal(response.status, 301, `${tls}/${host}`);
      assert.equal(response.headers.location, "https://kansasfrontiermatrix.com/features.json?test=1");
    }
  }
  for (const headers of [{}, { "X-Forwarded-Proto": "https" }]) {
    const response = await request("/", { headers });
    assert.equal(response.status, 301);
    assert.equal(response.headers.location, "https://kansasfrontiermatrix.com/");
  }
  assert.equal((await request("/", { tls: true })).status, 200);
});

test("mutable assets revalidate with or without a fingerprint query", async () => {
  for (const path of ["/assets/styles.css", "/favicon.svg", "/assets/kfm-hero.svg", "/assets/og.png", "/assets/styles.css?v=old"]) {
    const response = await request(path, { tls: true });
    assert.equal(response.status, 200, path);
    assert.match(response.headers["cache-control"], /(?:^|,\s*)no-cache(?:,|$)/, path);
    assert.doesNotMatch(response.headers["cache-control"], /max-age=604800/, path);
  }
  assert.equal((await request("/kfm-site.json", { tls: true })).headers["cache-control"], "no-cache");
});

test("AutoSSL exceptions, private Explorer redirect and security headers remain intact", async () => {
  for (const path of ["/.well-known/acme-challenge/token", "/.well-known/pki-validation/token"]) {
    for (const host of ["kansasfrontiermatrix.com", "preview.cpanel.example"]) {
      assert.equal((await request(path, { host })).status, 200);
    }
  }
  const explorer = await request("/explorer", { tls: true });
  assert.equal(explorer.status, 302);
  assert.equal(explorer.headers.location.replace(/\/$/, ""), DEFAULTS.explorerUrl);
  for (const path of ["/.htaccess", "/.private"]) assert.equal((await request(path, { tls: true })).status, 403);
  const page = await request("/", { tls: true });
  assert.match(page.headers["content-security-policy"], /script-src 'none'/);
  assert.equal(page.headers["x-frame-options"], "DENY");
  assert.equal(page.headers["x-content-type-options"], "nosniff");
  assert.equal(page.headers["strict-transport-security"], "max-age=31536000");
});

test("page asset queries match their bytes and change with changed CSS", async () => {
  const html = readFileSync(join(dist, "index.html"), "utf8");
  const refs = [...html.matchAll(/\b(?:href|src|srcset)="(\/(?:assets\/[^"?]+|favicon\.svg))\?v=([a-f0-9]+)"/g)];
  assert.equal(refs.length, 14);
  for (const [, path, digest] of refs) {
    assert.equal(digest, createHash("sha256").update(readFileSync(join(dist, path.slice(1)))).digest("hex").slice(0, 12));
  }
  const fixture = join(scratch, "fixture");
  for (const path of ["apps/public-site/build.mjs", "apps/public-site/src", "docs/brand/readme", "infra/godaddy/htaccess.template", "apps/site/source/app/site-features.ts", "apps/site/source/public/favicon.svg"]) {
    mkdirSync(dirname(join(fixture, path)), { recursive: true });
    cpSync(join(REPO, path), join(fixture, path), { recursive: true });
  }
  writeFileSync(join(fixture, "apps/public-site/src/styles.css"), ":root { color: blue; }\n");
  const output = join(scratch, "changed-css");
  const result = spawnSync(process.execPath, ["--experimental-strip-types", "--no-warnings", join(fixture, "apps/public-site/build.mjs")], { env: { ...env, KFM_SITE_OUT: output }, encoding: "utf8" });
  assert.equal(result.status, 0, result.stderr);
  const query = /href="\/assets\/styles.css\?v=([a-f0-9]+)"/;
  assert.notEqual(query.exec(html)[1], query.exec(readFileSync(join(output, "index.html"), "utf8"))[1]);
});

test("bundle checks fail closed on secrets, missing files, expiry and oversized bytes", () => {
  // Remove Apache-only fixtures so each candidate is a valid bundle baseline.
  const clean = mutatedBundle("clean", (directory) => {
    rmSync(join(directory, ".private"));
    rmSync(join(directory, ".well-known/acme-challenge"), { recursive: true });
    rmSync(join(directory, ".well-known/pki-validation"), { recursive: true });
  });
  assert.equal(check(clean).status, 0);
  const cases = [
    ["secret", "contains private key", (d) => writeFileSync(join(d, "assets/styles.css"), "-----BEGIN PRIVATE KEY-----")],
    ["missing", "missing required file", (d) => rmSync(join(d, "favicon.svg"))],
    ["expired", "Expires is missing or past", (d) => writeFileSync(join(d, ".well-known/security.txt"), "Contact: https://example.com\nExpires: 2000-01-01T00:00:00Z\n")],
    ["size", "limit 10485760", (d) => writeFileSync(join(d, "assets/og.png"), Buffer.alloc(11 * 1024 * 1024))],
  ];
  for (const [name, diagnostic, mutate] of cases) {
    const directory = join(scratch, `negative-${name}`);
    cpSync(clean, directory, { recursive: true });
    mutate(directory);
    const result = check(directory);
    assert.notEqual(result.status, 0, name);
    assert.ok(result.stderr.includes(diagnostic), result.stderr);
  }
  // Simulate a size/content view changing at read time. Counting stat bytes
  // while scanning separately would accept this oversized content.
  const preload = join(scratch, "grow-on-read.mjs");
  writeFileSync(preload, `import fs from 'node:fs'; import {syncBuiltinESMExports} from 'node:module';
const read = fs.readFileSync;
fs.readFileSync = function(path, options) {
  if (String(path).endsWith('/assets/styles.css')) {
    const bytes = Buffer.alloc(11 * 1024 * 1024, 32);
    return typeof options === 'string' ? bytes.toString(options) : bytes;
  }
  return read.call(this, path, options);
}; syncBuiltinESMExports();`);
  const grown = check(clean, ["--import", preload]);
  assert.notEqual(grown.status, 0);
  assert.match(grown.stderr, /limit 10485760/);
});
