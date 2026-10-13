# GoDaddy Node preview candidate

This is a separate runtime composition of Explorer v259, source
`441c3e29581ffb0293d8e643e5c37eed50319032`. It does not alter the
preserved Sites deployment, its audience, storage, or source-data values.

Verified destination: GoDaddy Node.js app `q9r9beo47t`, named
Kansas-Frontier-Matrix, connected to
`bartytime4life/Kansas-Frontier-Matrix`. The app is attached to the owner's
Plus Launch plan and its deployed source branch is `a0-godaddy-node-preview`.
The initial import used monorepo `main` and failed its npm/runtime build;
this standalone root package repaired that composition. The prior deployed
revision is `49ccc422e7ddbb36f5abe0e16c04649b7c7f313f`.

The Node candidate keeps the same Vinext and MapLibre versions and
rendering path, uses a standalone package at the application root, keeps
build/start dependencies in `dependencies`, and listens on the assigned
`PORT` on `0.0.0.0`. It builds without the Cloudflare Vite plugin.
Run `npm ci`, `npm run build`, then `npm start`.

Sites identity headers are untrusted outside Sites. They cannot sign in or
grant a staff role here. Identity, staff assignments and D1/R2-compatible
storage migration require configured server adapters. Existing private and
administrative endpoints keep their access controls.

On 2026-10-13 the owner canceled pricing, checkout and payment setup and
requested free reports/downloads. The custom map report supports copy,
JSON and printable HTML downloads; the evidence/fire/research/underground
report workspace supports Markdown and JSON exports. These run on the
visitor's device without login, payment or private-store access. The unused
pricing endpoint is removed. Draft labels, source/time/uncertainty notes,
location redaction and controlled publication remain in place. Eligible
public-data and story downloads retain their existing free workflows.
Production deployment and browser download acceptance require separate proof.

GoDaddy's branch picker exposes only the first 100 alphabetical branches.
The hosting connection uses `a0-godaddy-node-preview`. It originally matched
`codex/godaddy-node-preview`, but the latter subsequently received the earlier
pricing-service PR. This free-export repair starts from the actual hosting
branch, without that pricing service. Preserve both histories and do not
replace the public monorepo's main branch or the private Sites history.

No stored data or credentials are included in this source package. The
scalar server environment is available to existing provider handlers;
D1 and R2 bindings remain explicitly unavailable until migration. Existing
routes preserve their unavailable responses. GoDaddy's preview and
published MySQL environments share a database; do not import SQLite
migrations or reset that database without a tested migration.

The owner explicitly excluded Airo. Deploy through the existing GoDaddy
Node hosting app and GitHub connection. The domain connection and original
email records were restored before this repair. Preserve those DNS values;
free report exports do not require routing, account or merchant changes.
