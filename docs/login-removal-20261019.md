# Anonymous application and replacement preview — 2026-10-19

## Owner direction and source

The owner requested complete removal of application login, then removal of dead
connections and unavailable destination pages. The owner selected existing
GoDaddy preview app `urdng3v1vk` as the replacement. Base source is
`a0-hosted-ai-web-20261017@5b09c94de207409e4df08914f202097b2bcfae45`.
The prior app `q9r9beo47t` was initially retained as a recovery reference, then
recorded as deleted in the October 19 hosting update. It is historical only;
use `urdng3v1vk` for current operations and reverify its deployed source before
any later publication. See [current hosting documentation](godaddy-node-preview.md).
The original private Sites application and its data are separate and are not overwritten.

## Resulting application

- The map and hosted Qwen chat have no account button, username/password form,
  invitation, account activation, sign-in, sign-out, or account-status request.
- ChatGPT redirect helpers, GitHub owner OAuth/session handlers, account-backed
  PC AI service/store and provisioning/worker scripts are removed.
- Retired Data, Stewards, Source Operations, daily-archive, release-console and
  Earth Engine installer pages are removed rather than replaced with notices.
  Their map/Observatory/recipe/source links and obsolete feature/action/route
  registry entries are removed. Private submission APIs and their orphan source
  are removed. Public source downloads remain.
- The acquisition receipt inspector works from selected local files. Its
  unavailable hosted reads, saves, routes and persistence helpers are removed.
  Validation, latest-file ownership and source/coverage limits remain.
- The public AI evidence reader is retained as `app/hosted-ai-evidence.ts`.
  Anonymous guest/job isolation, cancellation, rate/queue/memory bounds, evidence
  rechecks, sensitive-location withholding and free report exports remain.
- No browser identity adapter remains. Retained private server contracts reject
  browser authority. Separately scoped local/scheduler machine capabilities
  remain; they do not grant anonymous access to private records or releases.
- Build identity names the selected replacement app. Hosted AI accepts only exact
  controlled origins, including the replacement preview; no wildcard was added.

## Runtime configuration and secrets

GoDaddy supplies the replacement app's own `DB_HOST`, `DB_PORT`, `DB_NAME`,
`DB_USER`, and `DB_PASSWORD`. No existing database credentials or private stores
are copied. Applied SQL migrations, stored records, private archives and model
caches are not reset, purged or reseeded by the source cleanup.

The replacement preview needs these runtime values, stored in GoDaddy Settings:

| Key | Value / handling |
| --- | --- |
| `KFM_HOSTED_AI` | `1`, enables the existing anonymous hosted model |
| `KFM_HOSTED_AI_ORIGIN` | `https://urdng3v1vk.preview.c38.airoapp.ai` |
| `VINEXT_TRUSTED_HOSTS` | `urdng3v1vk.preview.c38.airoapp.ai`, exact proxy host |
| `DB_*` | Provider-managed values belonging to the new app; preserve them |
| `KFM_PC_*` | Retired account system; do not migrate |
| `KFM_GITHUB_CLIENT_ID`, `KFM_GITHUB_CLIENT_SECRET`, `KFM_SESSION_KEY` | Retired owner login; do not migrate |
| `KFM_SITES_QWEN_TOKEN` | Optional separate Sites adapter, not needed for this app's public chat |
| `USGS_WATER_API_KEY` | Optional upstream credential, not available from the inspected Sites staging configuration; never substitute random bytes for a provider-issued key |

The pinned Qwen loader downloads exact public model artifacts into the new app's
private runtime cache and verifies their sizes/digests before execution. Model
weights are not credentials and are not committed. No paid inference key or
owner-PC connection is required. Current resource limits and qualification holds
remain in force.

Sites staging `appgprj_6acd1aafe0d88191a4306ea2ab44ed91` environment revision 2
contained only a delivery hash and a protected water-owner allowlist. Neither is
needed by the replacement. The original private Sites project returned
`Sites project not found` through the current connector, so its environment could
not be inventoried or migrated. Sites platform service-access credentials are
not GoDaddy runtime passwords and must stay scoped to their own Site.

## Validation and limits

Local production build and TypeScript pass. Changed-area lint has zero errors
and 41 inherited warnings. The production HTTP/targeted integration group passes
40 checks. It verifies removed routes return 404, private retained routes reject
anonymous/retired cookies/forged roles, public pages have no login controls or
retired links, and the public AI status declares no login requirement.

A full local run isolated one new test using POST for a PUT-only private staging
route. Correcting the test method preserves the intended assertion: a real PUT
with forged authority is denied. The corrected HTTP group passes. Focused
identity, origin, topology, local import, chat lifecycle and machine-capability
checks pass. Complete CI on the published candidate remains required, including
the unchanged county-search and startup-navigation browser suites.

The source cleanup does not establish production recovery. The old published
app reported a gateway error before this work. Replacement preview deployment,
source-digest parity, hosted model availability and eventual live routing are
separate checks. The new app currently requires a hosting-plan attachment before
publication; this record does not authorize a purchase or claim that it is live.

## Placement and recovery

Existing standalone application/server/scripts/tests roots own their established
responsibilities. This record uses `docs/`; its append-only provenance receipt
uses `data/receipts/generated/`, following Directory Rules v2 and ADR-0029.
No dataset, policy authority or source registry is introduced.

Rollback is a reviewed Git revert/source deployment from the preserved base;
retain database rows, archived bytes, private model caches and historical
receipts. No destructive data rollback is part of this change.
