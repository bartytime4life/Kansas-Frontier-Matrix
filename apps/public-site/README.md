<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/apps/public-site
title: apps/public-site — static public front door
type: README
subtype: boundary-compact
version: v1
status: retained static alternative; not the active public Explorer
owners: ["@bartytime4life"]
created: 2026-10-12
updated: 2026-10-17
policy_label: public
current_path: apps/public-site/README.md
owning_root: apps/
responsibility: Retain and check the earlier static-front-door alternative from repository facts and illustrative artwork
truth_posture: CONFIRMED retained static builder; artwork is illustrative; this alternative does not establish the active Node deployment
related:
  - ../../docs/runbooks/godaddy-hosting.md
  - ../../infra/godaddy/README.md
  - ../../.github/workflows/godaddy-public-site.yml
  - ../site/README.md
  - ../../docs/brand/readme/README.md
[/KFM_META_BLOCK_V2] -->

# `apps/public-site/`

This static front-door implementation records an earlier hosting plan. The active public Explorer uses a separate GoDaddy Node composition; follow the [Node runbook](../../docs/runbooks/godaddy-node-hosting.md). This directory and its cPanel workflow are retained as an alternative and must not replace that running app.

| | |
|---|---|
| **Is** | A zero-dependency Node 22 build that turns `src/` templates, [README artwork](../../docs/brand/readme/README.md) and the Explorer's [feature registry](../site/source/app/site-features.ts) into plain HTML, CSS, SVG and JSON. |
| **Is not** | A data release, a map, an API, or a copy of the Explorer. It reads no lifecycle, private or runtime store and runs no JavaScript in the browser. |
| **Deploys via** | [`godaddy-public-site.yml`](../../.github/workflows/godaddy-public-site.yml) → [`infra/godaddy/deploy.sh`](../../infra/godaddy/deploy.sh). Setup: [GoDaddy hosting runbook](../../docs/runbooks/godaddy-hosting.md). |

## Build and check

```bash
node --experimental-strip-types --no-warnings apps/public-site/build.mjs
```

```bash
node apps/public-site/check.mjs
```

The bundle is written to `apps/public-site/dist/`, which git ignores. Preview it with any static server, for example `python3 -m http.server -d apps/public-site/dist 8090`.

Run the focused security regression suite with Node 22 and Apache 2.4
(`apache2-bin` on Ubuntu):

```bash
node --experimental-strip-types --no-warnings --test apps/public-site/tests/security.test.mjs
```

It evaluates the committed deployment predicate, checks secret scope and
immutable checkout, builds synthetic local bundles, and exercises redirects,
TLS, cache headers, AutoSSL exceptions, and denied dotfiles on a loopback-only
Apache server. It uses no hosting credentials and makes no external requests.

Build settings come from environment variables: `KFM_SITE_ORIGIN`, `KFM_EXPLORER_URL`, `KFM_BUILD_COMMIT`, `KFM_BUILD_TIME` and `KFM_SITE_OUT`. Each is described at the top of [`build.mjs`](build.mjs).

## Output

| File | Content |
|---|---|
| `index.html`, `404.html` | Pages. The feature section is generated from `SITE_FEATURES`, grouped by its declared status. |
| `features.json` | The feature registry as public JSON (no code paths). |
| `kfm-site.json` | Build manifest. The deploy workflow reads it back from the live site to confirm the commit. |
| `.htaccess` | Rendered from [`infra/godaddy/htaccess.template`](../../infra/godaddy/htaccess.template): HTTPS, canonical host, `/explorer` redirect, security headers, caching. |
| `robots.txt`, `sitemap.xml`, `.well-known/security.txt`, `favicon.svg`, `assets/` | Indexing, security contact, icon, stylesheet and artwork. |

`check.mjs` fails the build in any of these cases:

- a required file is missing;
- a same-site link is broken;
- an image lacks alt text;
- a template placeholder is left unfilled;
- the bundle contains a secret-shaped string or a loopback address;
- the bundle exceeds 10 MiB;
- `security.txt` has expired;
- the `.htaccess` safeguards are missing.

## Editing

- Wording and layout: edit `src/index.html` and `src/styles.css`. Keep the active-build disclosure and the illustration notice.
- Feature cards change automatically when `apps/site/source/app/site-features.ts` changes.
- Artwork: add the file name to `ARTWORK` in `build.mjs`. Do not show artwork that states numbers which have drifted from the registry.
- Rollback: revert the commit. The next `main` deploy mirrors the earlier bundle.
