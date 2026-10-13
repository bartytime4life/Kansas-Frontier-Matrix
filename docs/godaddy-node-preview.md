# GoDaddy Node preview candidate

This is a separate runtime composition of Explorer v259, source
`441c3e29581ffb0293d8e643e5c37eed50319032`. It does not alter the
preserved Sites deployment, its audience, storage, or source-data values.

Verified destination: GoDaddy Node.js app `q9r9beo47t`, named
Kansas-Frontier-Matrix, connected to
`bartytime4life/Kansas-Frontier-Matrix` branch `main`. The app is
attached to the owner's Plus Launch plan. The existing preview has a
failed npm/runtime build. The repository root is a pnpm workspace
coordinator, not the Explorer application's package.

The Node candidate keeps the same Vinext and MapLibre versions and
rendering path, uses a standalone package at the application root, keeps
build/start dependencies in `dependencies`, and listens on the assigned
`PORT` on `0.0.0.0`. It builds without the Cloudflare Vite plugin.
Run `npm ci`, `npm run build`, then `npm start`.

Sites identity headers are untrusted outside Sites. They cannot sign in or
grant a staff role here. Identity, staff assignments, D1/R2-compatible
storage migration, and report billing require configured server adapters.
This candidate is for preview verification. It must not be represented as
a completed public paid-report application.

The owner selected GoDaddy Payments and confirmed there is no existing
staff sign-in service or role list. Merchant configuration and evidence,
value, and effort pricing still require owner setup. Report download
controls are unavailable and the quote API returns a non-cacheable 503.

GoDaddy's branch picker exposes only the first 100 alphabetical branches.
The canonical candidate uses `codex/godaddy-node-preview`; an identical
`a0-godaddy-node-preview` compatibility ref is used for that picker.
Both point to the same self-contained source tree and have no private
Sites Git history. Neither replaces the public monorepo's main branch.

No stored data or credentials are included in this source package. The
scalar server environment is available to existing provider handlers;
D1 and R2 bindings remain explicitly unavailable until migration. Existing
routes preserve their unavailable responses. GoDaddy's preview and
published MySQL environments share a database; do not import SQLite
migrations or reset that database without a tested migration.

The owner explicitly excluded Airo. Deploy through the existing GoDaddy
Node hosting app and GitHub connection. Production domain controls are
unavailable until a successful publish. Preserve the current DNS and email
records until the app has passed preview verification and GoDaddy supplies
the real routing and certificate requirements.
