# Reviewed water delivery candidate

This documents the owner-private Site's reviewed-water boundary. Site v147 was
deployed on 2026-10-04; a Site deployment alone does not establish whether a
real water package is active. Existing DB/BUCKET bindings and audience remain
the same in this correction candidate.

`app/governed-water.ts` verifies the bounded snapshot carrier and projects the
same synthetic bootstrap/layers/evidence responses as the monorepo Python API.
The closed RuntimeResponseEnvelope is nested under envelope; data is omitted
for every negative outcome. `app/governed-water-server.ts` reads immutable R2
bytes and separately trusted D1 activation metadata. It accepts only two fixed
station IDs and never accepts upstream URLs, uploaded approval fields or a
write operation. Additive migration 0001 creates metadata tables only.

The reviewed-water map control exposes observation, provider revision, retrieval,
review and release times separately, displays coverage/freshness and evidence,
and revalidates bounded exports. Refresh/failure/withdrawal/expiry withholds prior
data while retaining station selection. Existing provider-context layers remain
external context. Hosted audience enforcement remains a platform prerequisite;
this read-only route supplies approved public-safe data, not owner administration.
The browser also checks that evidence belongs to the selected station and the
same reviewed package, release, and measurement references. A fresh export must
contain only that station; changing selection while its requests are in flight
withholds the download. These checks protect the browser journey if a response
is unexpectedly broad or malformed; server-side projection and release checks
remain authoritative.
The export also tracks station-selection generation. A rapid A→B→A selection
round trip during either request withholds the older in-flight download even
though the station name has returned to A.
The current monorepo control distinguishes a browser request failure from a
successful response that reports no active reviewed release. It labels other
successful negative responses as withheld; none establishes that no source
observation exists.

Do not stage or activate a package via an ordinary client. Hosted authenticated
staging, review and activation operations are still pending. A manifest does not
supply its own trusted approvals. Applying SQL or receiving HTTP 200 cannot
establish admission, evidence eligibility or a reviewed release.

Local conformance: `node --test tests/governed-water.test.mjs`; full validation:
`npm test` and `npx tsc --noEmit`. Browser visual acceptance remains unverified
because the admin security check was unavailable. Synthetic fixture approval is
explicitly synthetic and must never be copied onto the captured real package.

Dependency fixes reconcile Next 16.3.7, Undici 7.29.1 and fast-uri 3.1.8. A
fresh 2026-10-03 lockfile audit reports eight high findings in development
dependencies and zero production-dependency findings with `--omit=dev`; the
development findings remain open for review. The inspected next/og advisory
path is not used by app code; vendored Vinext returns its own unsupported shim.
Package presence alone was not treated as proof of deployed exploitation.
KML text stripping is linear and bounded. The Qwen bridge adds only the exact
127.0.0.1:4173 origin while retaining existing request/response and model limits.

Reconciliation retains newer v129 soil playback, wind/globe and hover work. It
also restores repository-only Earth Engine inventory export, zoom-0 display and
palette parity, and carries soil state through share links and Hide all. The
retired synthetic analysis-recipes carrier is not restored. The monorepo mirror
receipt records exact file-level parity with this candidate, not hosted parity.

Rollback before publication is to retain the current live Site and abandon the
candidate. After an authorized publication, use the exact previous application
version and eligible package with fresh validation. Local synthetic package
rollback was rehearsed separately; hosted rollback was not.
