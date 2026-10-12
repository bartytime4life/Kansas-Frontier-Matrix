#!/usr/bin/env node
// Build the static public front door for kansasfrontiermatrix.com.
//
// Zero-dependency Node 22 script. It reads the page templates in src/, the
// illustrative README artwork in docs/brand/readme/, and the Explorer feature
// registry in apps/site/source/app/site-features.ts, then writes a static
// bundle to dist/ that any Apache host (GoDaddy cPanel web hosting) can serve.
// The bundle restates repository facts at the build commit; it creates no
// source admission, release, deployment, or publication authority.
//
// Settings (environment variables, all optional):
//   KFM_SITE_ORIGIN   canonical public origin   (default https://kansasfrontiermatrix.com)
//   KFM_EXPLORER_URL  Explorer address           (default: the stable Sites address)
//   KFM_BUILD_COMMIT  commit to stamp            (default: git rev-parse HEAD)
//   KFM_BUILD_TIME    ISO-8601 build time        (default: commit time, for reproducible output)
//   KFM_SITE_OUT      output directory           (default apps/public-site/dist)

import { execFileSync } from "node:child_process";
import { createHash } from "node:crypto";
import { copyFileSync, mkdirSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const HERE = dirname(fileURLToPath(import.meta.url));
const REPO = resolve(HERE, "../..");
const SRC = join(HERE, "src");
const ART = join(REPO, "docs/brand/readme");

export const DEFAULTS = Object.freeze({
  origin: "https://kansasfrontiermatrix.com",
  explorerUrl: "https://kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site",
  repoUrl: "https://github.com/bartytime4life/Kansas-Frontier-Matrix",
});

// Artwork copied into dist/assets/. Each light file may have a -dark twin.
const ARTWORK = [
  ["kfm-hero.svg", false],
  ["kfm-explorer-walkthrough.svg", true],
  ["kfm-time-depth.svg", true],
  ["kfm-source-lanes.svg", true],
  ["kfm-trust-membrane.svg", true],
  ["kfm-trust-path.svg", true],
  ["kfm-divider.svg", false],
];

const STATUS_COPY = Object.freeze({
  LIVE_UI: ["Working in the interface", "Interface tools that run in the Explorer today."],
  ACTIVE_CONTEXT: ["Live provider context", "Connected to official public providers and shown as attributed external context, not as released KFM data."],
  BOUNDED_PROOF: ["Bounded proof", "Demonstrated within stated limits; broader acceptance is still ahead."],
  HELD: ["Held", "Designed but deliberately held back until evidence, review, or policy allows it."],
});

const escapeHtml = (value) =>
  String(value).replace(/[&<>"']/g, (ch) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[ch]);

const escapeRegex = (value) => String(value).replace(/[\\^$.*+?()[\]{}|]/g, "\\$&");

// Stable asset names get a content-hash query so long cache lifetimes never
// pair a new page with stale CSS or artwork.
function fingerprintAssets(html, out) {
  return html.replace(/\b(href|src|srcset)="(\/(?:assets\/[^"?#]+|favicon\.svg))"/g, (match, attr, ref) => {
    const digest = createHash("sha256").update(readFileSync(join(out, ref.slice(1)))).digest("hex").slice(0, 12);
    return `${attr}="${ref}?v=${digest}"`;
  });
}

function requireHttpsUrl(name, value) {
  let url;
  try {
    url = new URL(value);
  } catch {
    throw new Error(`${name} is not a URL: ${value}`);
  }
  if (url.protocol !== "https:" || url.username || url.password || url.search || url.hash) {
    throw new Error(`${name} must be a plain https URL: ${value}`);
  }
  return url.href.replace(/\/$/, "");
}

function git(args, fallback) {
  try {
    return execFileSync("git", args, { cwd: REPO, encoding: "utf8", stdio: ["ignore", "pipe", "ignore"] }).trim();
  } catch {
    return fallback;
  }
}

export async function loadFeatures() {
  const mod = await import(pathToFileURL(join(REPO, "apps/site/source/app/site-features.ts")).href);
  if (!Array.isArray(mod.SITE_FEATURES)) throw new Error("SITE_FEATURES is not an array");
  return mod.SITE_FEATURES.map((f) => ({
    id: f.id,
    title: f.title,
    domain: f.domain,
    status: f.status,
    surface: f.surface,
    user_outcome: f.userOutcome,
    boundary: f.boundary,
    source_ids: [...f.sourceIds],
  }));
}

function renderFeatureSections(features) {
  return Object.keys(STATUS_COPY)
    .map((status) => {
      const group = features.filter((f) => f.status === status);
      if (group.length === 0) return "";
      const [label, blurb] = STATUS_COPY[status];
      const cards = group
        .map(
          (f) => `        <li class="card" id="feature-${escapeHtml(f.id)}">
          <h4>${escapeHtml(f.title)}</h4>
          <p class="surface">${escapeHtml(f.surface)}</p>
          <p>${escapeHtml(f.user_outcome)}</p>
          <details><summary>Limits</summary><p>${escapeHtml(f.boundary)}</p></details>
        </li>`,
        )
        .join("\n");
      return `    <section class="feature-group" aria-labelledby="status-${status}">
      <h3 id="status-${status}"><span class="pill pill-${status.toLowerCase()}">${escapeHtml(label)}</span> <span class="count">${group.length}</span></h3>
      <p class="muted">${escapeHtml(blurb)}</p>
      <ul class="cards">
${cards}
      </ul>
    </section>`;
    })
    .filter(Boolean)
    .join("\n");
}

function fill(template, values) {
  return template.replace(/\{\{([A-Z0-9_]+)\}\}/g, (match, key) => {
    if (!(key in values)) throw new Error(`Unfilled template key ${match}`);
    return values[key];
  });
}

export async function build(env = process.env) {
  const origin = requireHttpsUrl("KFM_SITE_ORIGIN", env.KFM_SITE_ORIGIN || DEFAULTS.origin);
  const explorerUrl = requireHttpsUrl("KFM_EXPLORER_URL", env.KFM_EXPLORER_URL || DEFAULTS.explorerUrl);
  const repoUrl = DEFAULTS.repoUrl;
  const commit = env.KFM_BUILD_COMMIT || git(["rev-parse", "HEAD"], "unknown");
  if (commit !== "unknown" && !/^[0-9a-f]{40}$/.test(commit)) throw new Error(`KFM_BUILD_COMMIT is not a full SHA: ${commit}`);
  const builtAt = new Date(env.KFM_BUILD_TIME || git(["show", "-s", "--format=%cI", "HEAD"], "") || Date.now()).toISOString();
  const out = resolve(env.KFM_SITE_OUT || join(HERE, "dist"));

  const features = await loadFeatures();
  const counts = Object.fromEntries(Object.keys(STATUS_COPY).map((s) => [s, features.filter((f) => f.status === s).length]));
  const unknown = features.filter((f) => !(f.status in STATUS_COPY));
  if (unknown.length) throw new Error(`Unknown feature status: ${unknown.map((f) => f.status).join(", ")}`);
  const providerIds = [...new Set(features.flatMap((f) => f.source_ids))].sort();

  rmSync(out, { recursive: true, force: true });
  mkdirSync(join(out, "assets"), { recursive: true });
  mkdirSync(join(out, ".well-known"), { recursive: true });

  for (const [name, hasDark] of ARTWORK) {
    copyFileSync(join(ART, name), join(out, "assets", name));
    if (hasDark) {
      const dark = name.replace(/\.svg$/, "-dark.svg");
      copyFileSync(join(ART, dark), join(out, "assets", dark));
    }
  }
  copyFileSync(join(ART, "kfm-social-preview.png"), join(out, "assets/og.png"));
  copyFileSync(join(REPO, "apps/site/source/public/favicon.svg"), join(out, "favicon.svg"));
  copyFileSync(join(SRC, "styles.css"), join(out, "assets/styles.css"));

  const shortCommit = commit === "unknown" ? "unknown" : commit.slice(0, 7);
  const values = {
    ORIGIN: escapeHtml(origin),
    EXPLORER_URL: escapeHtml(explorerUrl),
    REPO_URL: escapeHtml(repoUrl),
    COMMIT_URL: escapeHtml(commit === "unknown" ? repoUrl : `${repoUrl}/tree/${commit}`),
    BUILD_COMMIT_SHORT: escapeHtml(shortCommit),
    BUILD_DATE: escapeHtml(builtAt.slice(0, 10)),
    FEATURE_TOTAL: String(features.length),
    PROVIDER_TOTAL: String(providerIds.length),
    LIVE_UI_TOTAL: String(counts.LIVE_UI),
    ACTIVE_CONTEXT_TOTAL: String(counts.ACTIVE_CONTEXT),
    FEATURE_SECTIONS: renderFeatureSections(features),
  };
  for (const page of ["index.html", "404.html"]) {
    writeFileSync(join(out, page), fingerprintAssets(fill(readFileSync(join(SRC, page), "utf8"), values), out));
  }

  // Values land in mod_rewrite patterns and substitutions; strip characters
  // that carry meaning there (the URLs were already validated above).
  const canonicalHost = new URL(origin).host;
  writeFileSync(
    join(out, ".htaccess"),
    fill(readFileSync(join(REPO, "infra/godaddy/htaccess.template"), "utf8"), {
      CANONICAL_HOST: escapeRegex(canonicalHost),
      CANONICAL_HOST_PLAIN: canonicalHost,
      EXPLORER_URL: explorerUrl.replace(/[\\$%\s"]/g, ""),
    }),
  );

  const manifest = {
    schema: "kfm.public-site-manifest.v1",
    site: origin,
    explorer: explorerUrl,
    repository: repoUrl,
    commit,
    built_at: builtAt,
    features: { total: features.length, by_status: counts, provider_source_ids: providerIds.length, registry: "apps/site/source/app/site-features.ts" },
    endpoints: { features: `${origin}/features.json`, sitemap: `${origin}/sitemap.xml`, security: `${origin}/.well-known/security.txt` },
    non_effects: [
      "restates repository facts at the build commit",
      "not a KFM data release, evidence bundle, or publication decision",
      "artwork is illustrative, not map products or screenshots",
    ],
  };
  writeFileSync(join(out, "kfm-site.json"), `${JSON.stringify(manifest, null, 2)}\n`);
  writeFileSync(
    join(out, "features.json"),
    `${JSON.stringify({ schema: "kfm.public-site-features.v1", commit, registry: manifest.features.registry, features }, null, 2)}\n`,
  );

  writeFileSync(join(out, "robots.txt"), `User-agent: *\nAllow: /\n\nSitemap: ${origin}/sitemap.xml\n`);
  writeFileSync(
    join(out, "sitemap.xml"),
    `<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n  <url><loc>${escapeHtml(origin)}/</loc><lastmod>${builtAt.slice(0, 10)}</lastmod></url>\n</urlset>\n`,
  );
  const expires = new Date(Date.parse(builtAt) + 365 * 24 * 3600 * 1000).toISOString();
  writeFileSync(
    join(out, ".well-known/security.txt"),
    [
      `Contact: ${repoUrl}/security/advisories/new`,
      `Expires: ${expires}`,
      `Policy: ${repoUrl}/blob/main/SECURITY.md`,
      `Canonical: ${origin}/.well-known/security.txt`,
      "Preferred-Languages: en",
      "",
    ].join("\n"),
  );

  return { out, origin, explorerUrl, commit, features: features.length, counts };
}

if (import.meta.url === pathToFileURL(process.argv[1]).href) {
  const result = await build();
  console.log(
    `Built ${result.out} for ${result.origin} at ${result.commit.slice(0, 12)}: ` +
      `${result.features} Explorer features (${Object.entries(result.counts).map(([k, v]) => `${k}=${v}`).join(", ")}).`,
  );
}
