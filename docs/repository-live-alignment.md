# Public Node application: source and live alignment

This document owns operation of this standalone GoDaddy composition. The
repository's [hosting entry point](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/runbooks/godaddy-hosting.md)
documents the separate monorepo boundary. Existing `app/`, `server/`, `scripts/`,
`tests/` and `docs/` retain their responsibilities under Directory Rules v2 and
accepted ADR-0029. The preserved Sites mirror, its identity and private stores
are separate; this change does not synchronize or replace them.

## Dated starting point: 2026-10-17

The [GoDaddy dashboard](https://host.godaddy.com/nodejs/projects/q9r9beo47t)
identifies KFM app `q9r9beo47t`, Node.js 22, connected to
`bartytime4life/Kansas-Frontier-Matrix`, branch `a0-hosted-ai-web-20261017`.
After a fresh reload its Published tab showed
`4b3cc837e9c131e5eb214427e0a55646fc76e52a`; Preview showed
`500a09935951b5bec7965174236c6aac33c3e933`. The source branch was newer at
`34fb6018ea9668ae81e64aa94b3948d4351147e8` and preview was out of sync.
These observations expire when the provider or branch changes.

The public origin is [kansasfrontiermatrix.com](https://kansasfrontiermatrix.com/).
The `source_commit` in `godaddy-source.json` records the historical Explorer v259
migration baseline, not a live deployment. The original Sites snapshots remain
dated lineage and do not establish this public app's version or current routing.

This alignment candidate starts at the exact **Published** commit above. It
excludes the held AI candidate changes on the connected branch. It adds public
application identity, About-page navigation and resource corrections, and ports
the narrowly scoped immutable asset staging repair from commit
`3d91d517057b3fce8b7a206e21a11db2b2723ec7`. Asset staging copies only exact
hashed browser assets, keeps old files for open tabs, and holds conflicting
immutable bytes. It neither loads models nor edits source data or stores.

## Build and verify

Use Node.js 22.13 or newer within Node 22. Keep the lockfile unchanged:

```bash
npm ci
npm run build
npx tsc --noEmit
node --test tests/build-identity.test.mjs tests/build-identity-http.test.mjs tests/public-client-assets.test.mjs tests/site-security-http.test.mjs tests/header-focus.test.mjs tests/explorer-menu-dismissal.test.mjs tests/mobile-compatibility.test.mjs tests/workspace-map-navigation.test.mjs tests/workspace-help-navigation.test.mjs
```

The production entry is `server/start.mjs` and uses the provider-assigned `PORT`.
For a bounded local smoke, start `PORT=5187 npm start` and in another terminal:

```bash
KFM_NODE_TEST_ORIGIN=http://127.0.0.1:5187 node --test tests/godaddy-node-runtime.test.mjs
node scripts/build-identity.mjs --verify http://127.0.0.1:5187
```

`npm run dev` builds and starts the same Node server for the GoDaddy preview.
The workflow at `.github/workflows/public-core-repair.yml` runs candidate identity
and asset checks after its production build. It does not publish or load models.

## What the build identity proves

Prebuild runs `scripts/build-identity.mjs`, generating the ignored
`app/build-info.generated.json`. `/api/build` returns only that application
identity with `Cache-Control: no-store`; it reads no environment or private store.
The digest covers named source roots and build/package configuration. Generated
browser assets, hidden files, local state, models, documentation and tests are
excluded. Symlinked source inputs fail closed. An exact clean Git checkout also
records its commit. A dirty or archive checkout omits it; no environment-variable
commit is assumed trustworthy.

Compare a deployment with this same checkout using:

```bash
node scripts/build-identity.mjs --print
node scripts/build-identity.mjs --verify https://kansasfrontiermatrix.com
```

`APPLICATION_INPUTS_MATCH` means bounded application-input parity. It does not
prove emitted build-byte parity, provider availability, browser acceptance,
configuration, source admission or release. Missing or HTTP-blocked identity is
a failed verification, never a match. The public baseline predates this endpoint;
it remains unavailable until this candidate is separately published.

## Delivery and rollback

Before changing the hosting source, preserve the current connected branch,
preview, published rollback commit and any unfinished work. Review the candidate
against that published source; never upload monorepo `main` or use cPanel/DNS
instructions to replace this Node application. Preview may share production
stores: leave acquisition workers disabled and retain account and data settings.

Finish build, type, HTTP and changed-workflow browser checks, then obtain the
applicable exact-source review/publication authority. An owner hold was recorded
on 2026-10-17 for the newer AI candidate. This production-based change does not
clear it or assume an exception. The published baseline also retains known AI
quality limitations and an unremediated Braces advisory; no security acceptance
or model-quality repair is claimed here.

The [2026-10-18 dependency investigation](dependency-audit-20261018.md) traces
all eight HIGH affected-package entries to one Braces advisory across lint and
Vinext build tooling. All are production-installed; public-request exploitability
was not established. No compatible patched release was available at inspection,
so the package/lock remain unchanged and the dependency/publication hold remains.
This evidence update grants no audit exception or publication authority.

After authorized preview/publication, re-read the provider's actual source
commit, check `/api/build`, modules, desktop/mobile navigation, layers/time,
free report exports, and denial of private operations. Preserve external-source
outage and uncertainty disclosures. Hosted health is distinct from these checks.

Rollback uses a reviewed application revert or verified retained provider
deployment, starting from the recorded published commit. It does not roll back
databases, source captures, model caches, account grants or DNS. Restore and
verify the prior preview/source selection if it was temporarily changed for a
bounded release. Report each transition and remaining hold separately.
