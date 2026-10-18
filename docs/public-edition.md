# Separate public KFM edition — restricted preview

Status: implementation in progress; no observational or subsurface release is approved.

This application is an isolated copy of the reviewed repository Site source at
3ec5f0d9640a88117ff45ae31d3347609b165e67. Its owner-private Sites identity is
appgprj_6acd1aafe0d88191a4306ea2ab44ed91. The original Site, source mirror,
local services, synced references, storage, and schedules are separate.

## Implemented boundary

* `app/public-profile.ts` fixes this application to the public edition. Private
  companion/cache/intake/Qwen clients refuse before contacting visitor loopback.
* `worker/index.ts` and `app/public-route-policy.ts` deny unlisted routes and
  legacy data/history paths. Generated static assets also require final inventory
  review because the hosting edge can dispatch assets before the Worker.
* `app/public-release.ts` and `app/public-release-server.ts` require the exact
  deployment-pinned catalog, individually resolved authority/source/object hashes,
  public field list, dates, validity, active pointer, and correction state.
  Browser inputs and syntactically valid decisions cannot grant release authority.
* Water/weather/soil/storm/earthquake readers enforce this additional boundary
  before their existing parsers project records. Subsurface/groundwater/archive
  objects are served only through approved immutable-object readers.
* Eight family owner consoles select trusted packages. Owner authentication,
  same-origin checks, immutable staging, bounded uploads and compare-and-swap
  activation/withdrawal remain independent of public reads. Tokens stage only.
* New additive migration `drizzle/0010_public_delivery.sql` stores pointer and
  append-only activation/withdrawal/staging history for the three asset families.
* Original recorded-log tools use governed asset URLs, verify integrity, retain
  limits, and clear records/exports on expiry or observed withdrawal. Exports
  revalidate the exact active package. Weather navigation uses actual station-local
  observation dates and preserves missing/null versus zero.
* `public/` excludes all old observational, history, groundwater and subsurface
  assets. Generated Vite client metadata is removed after build. The scanner blocks
  legacy stores, data files, symlinks and obvious secret material; it is not a full
  data classification or formal security audit.

## Build and restricted local preview

Use Node22.13+ and the retained lockfile/vendor Vinext archive. Never install into
or alter the original checkout or synced `sources/`.

```
npm run install:ci
npx tsc --noEmit
npm run lint
npm run build
bash scripts/serve-public-preview.sh
```

The launcher defaults to127.0.0.1:4328 and fresh checkout-local
`.sites-runtime/public-preview`. It refuses dotenv/development secret files and
imports no original keys or archive credentials. All local identity headers are
rejected. Stop only the process started by this copy. The final build removes
`.vite` client metadata and inventories deployed client assets.

Run the public/core/callback tests listed in the implementation receipt. The
inherited full suite also contains private-only routes and removed data assets;
its failures are recorded, not presented as passes. A public launch requires
passing changed-area checks and complete hosted, mobile, accessibility, security,
performance and real-package acceptance.

## Runtime configuration

Hosting manifest binds fresh `DB` and `BUCKET` for this new Site. No private store
identifiers, captures, schedules, local services, or original Site identity may
be copied. `KFM_PUBLIC_DELIVERY_SHA256` uses the full `sha256:<64 hex>` digest and pins the exact trusted catalog bytes; the
current empty catalog authorizes nothing. Populated entries also require `KFM_PUBLIC_IMPLEMENTATION_REF` to match their hash-bound reviewed implementation receipt, destination Site and allowed HTTPS hostnames. This refers to reviewed functional code; exact final native source/archive parity is a separate release gate. Missing configuration refuses serving and activation. Owner access is configured separately
for this new Site using the existing owner allowlist. Stage-only token is absent
until an operator configures it through Sites secret settings. Never send tokens
or passwords in chat or save credentials in source.

The compiler in `app/public-release.ts` resolves and validates actual bytes. Its
output is VALIDATION_ONLY. Seven authority references (including explicit target
publication authorization) plus source/version and rollback bindings must be
reviewed and resolved before compiling a delivery list. The existing candidate
ReleaseManifest schema remains unchanged and cannot grant public permission.

For approved legacy packages, POST exact package JSON to
`/api/governed/{family}-admin/stage` with the stage-only bearer token.
For subsurface/groundwater/archive, POST exact artifact bytes with
`Content-Type: application/octet-stream` to
`/api/governed/{family}-admin/stage?package_id=<approved-id>&name=<approved-name>`.
Names, keys, bytes and full hashes must match the trusted entry. Then the signed-in
owner activates the already authorized package from its console. Withdraw and
eligible rollback preserve append-only events. No upload activates a package.

## Remaining launch work

1. Establish numerical Sites account storage/runtime capacity and backup/export
   recovery; private creation/deployment is not account-wide capacity evidence.
2. Review real water/weather candidates and the minimal Kansas WWC5 candidate.
   Resolve rights, sensitivity, exact fields/precision, source-byte provenance,
   independent review where required, expiry, corrections and publication target.
   The large original KGS collection remains separately held. Raw KGS ZIP bytes
   were not re-captured; source closure must accurately bind preserved derived
   inputs or acquire and verify original archives.
3. Compile, stage and activate only approved entries in restricted staging. Test
   real dates, stations, original intervals, citations, permitted exports and
   unavailable-data journeys. Current private preview has no approved data.
4. Integrate released historical archive projections and qualify additional
   provider/imagery layers. Existing direct provider overlays remain disabled;
   not all original Explorer features are public-delivery-ready.
5. Complete real touch-device, keyboard/screen-reader/zoom, WebGL fallback,
   performance/resource, hosting-edge identity/header and failure acceptance.
6. Create separate private production Site with fresh resources; derive it from
   this final sanitized source, replace only destination identity, configure its
   independent owner and reviewed target-specific catalog, and rehearse recovery.
7. After publication approval, anonymous platform-host preflight, certificate and
   domain readiness, attach apex/www with native Sites tools. Capture fresh full
   GoDaddy zone, apply only exact returned records, retain GoDaddy nameservers,
   mail records and old placeholder. Never guess destination IP addresses.

DNS currently remains A@160.153.0.130, www alias apex, NS55/NS56, forwarding unset.
Full evidence and the rollback record live outside deployment output. Canonical
www→apex HTTPS308 is implemented; custom-domain routing/certificates remain untested.

## Recovery and maintenance

Restrict audience and withdraw offending releases first. Restore a saved source
version independently of eligible data-pointer rollback; neither deletes writes.
Restore captured DNS if cutover fails. Keep prior eligible immutable releases,
corrections, receipts and append-only events. Capture jobs never publish. Review
freshness/expiry/quota/errors regularly; provider terms/dependencies monthly;
restore rehearsals quarterly and before major migration. Previously downloaded
public bytes cannot be recalled.

Placement follows adopted `docs/doctrine/directory-rules.md`/ADR0029 responsibility
boundaries. The proposed operational contract/schema/ADR live in the isolated
repository's existing contracts/schemas/docs homes. No accepted ADR, release,
review, mirror promotion or original Site update is implied by this private copy.
