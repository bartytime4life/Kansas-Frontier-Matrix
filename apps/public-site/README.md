<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/apps/public-site
title: apps/public-site — static public front door
type: README
subtype: boundary-compact
version: v2
status: retained build-only static bundle; deployment retired
owners: ["@bartytime4life"]
created: 2026-10-12
updated: 2026-10-20
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

This static front-door implementation records an earlier hosting plan. The intended public production path is the existing GoDaddy Node app `urdng3v1vk`, using the standalone source branch `a0-hosted-ai-web-20261017`; follow the [Node runbook](../../docs/runbooks/godaddy-node-hosting.md) and verify its current Published and Preview revisions before any authorized operation. This directory remains buildable for review and recovery, but its credentialed static deployment job was retired by [PR #5361](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5361).

| | |
|---|---|
| **Is** | A zero-dependency Node 22 build that turns `src/` templates, [README artwork](../../docs/brand/readme/README.md) and the Explorer's [feature registry](../site/source/app/site-features.ts) into plain HTML, CSS, SVG and JSON. |
| **Is not** | A data release, a map, an API, or a copy of the Explorer. It reads no lifecycle, private or runtime store and runs no JavaScript in the browser. |
| **Build validation** | [`godaddy-public-site.yml`](../../.github/workflows/godaddy-public-site.yml) retains the `build` check and downloadable `public-site-<github.sha>` review artifact for affected changes. It has no static deployment job, hosting secrets, deployment environment or transfer inputs. |
| **Production operation** | The existing GoDaddy Node app `urdng3v1vk` follows the [Node runbook](../../docs/runbooks/godaddy-node-hosting.md). Setting the former `GODADDY_DEPLOY_ENABLED` variable cannot restore the removed job. |

The workflow runs on every pull request, with its `changes` job selecting whether to build; scoped `main` pushes and manual dispatches also build for review. It does not invoke the retained historical [`infra/godaddy/deploy.sh`](../../infra/godaddy/deploy.sh) helper. Reintroducing static transfer requires a separately reviewed change. The [historical hosting plan](../../docs/runbooks/godaddy-hosting.md) remains evidence, not current deployment instructions. Sites environments, historical deployment records and the Node app's rollback controls remain separate.

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
node --experimental-strip-types --no-warnings --test apps/public-site/tests/*.test.mjs
```

`workflow.test.mjs` checks that the workflow cannot deploy or access hosting
credentials while retaining its validation, checkout credential isolation and review
artifact. `security.test.mjs` checks the retained transfer helper's fail-closed
controls, builds synthetic local bundles, and exercises redirects, TLS, cache
headers, AutoSSL exceptions and denied dotfiles on a loopback-only Apache
server. The tests use no hosting credentials and make no external requests;
testing the helper does not enable deployment.

Build settings come from environment variables: `KFM_SITE_ORIGIN`, `KFM_EXPLORER_URL`, `KFM_BUILD_COMMIT`, `KFM_BUILD_TIME` and `KFM_SITE_OUT`. Each is described at the top of [`build.mjs`](build.mjs).

## Output

| File | Content |
|---|---|
| `index.html`, `404.html` | Pages. The feature section is generated from `SITE_FEATURES`, grouped by its declared status. |
| `features.json` | The feature registry as public JSON (no code paths). |
| `kfm-site.json` | Static build manifest included in the review artifact. The build-only workflow does not read it back from a live site or establish the Node app's deployed revision. |
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
- Static bundle recovery: revert the relevant source change and rerun the build and checks. This produces a review bundle without deploying it. Retain Git history and historical transfer tooling; restoring a deployment path requires separate review.
- Production rollback: use the [Node runbook](../../docs/runbooks/godaddy-node-hosting.md#rollback-and-maintenance). A static source revert does not roll back the Node app or change a Sites environment.
