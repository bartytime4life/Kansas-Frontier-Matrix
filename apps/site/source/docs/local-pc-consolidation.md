# Local Explorer consolidation — 2026-10-02

## Local operation checkpoint — 2026-10-05

The source-alignment session installed Site v153 from
`da94de300c1b20dc98e9f527ba54613cfd696f8b`. The stable
`~/Projects/KFM-Explorer-Site-current` alias selected that source, while the
service's explicit storage argument remained
`~/Projects/KFM-Explorer-Site-v109/.wrangler/local-state`. These paths have
different responsibilities: changing the source alias does not move the store.
The stopped-service backup was created at
`~/Projects/KFM-Explorer-local-state-pre-v153-20261005` and was verified and
relocated on 2026-10-06 to
`~/KFM-site-recovery/KFM-Explorer-local-state-pre-v153-20261005`. Preserve both
the physical store and its backup; an older folder name does not make data obsolete.

Resolve the current source with `readlink -f` and inspect the effective
`systemctl --user cat kfm-explorer-local.service` before any further update.
Use its physical `--state` argument; do not substitute the new source folder's
empty `.wrangler` directory. Keep origin `http://127.0.0.1:4173` to retain
device-local Places, reports, stories and the reviewed-imagery read exception.

The direct launcher requires Node 22.13 or a later 22.x release. It now refuses
both `.env` / `.env.*` and `.dev.vars` / `.dev.vars.*` without reading their
contents. Previously it could silently ignore dotenv configuration that Wrangler
would load. Reconcile those settings explicitly before selecting a runtime.
Do not rename or remove secret files just to make the startup check pass.

Local pages and held governed reads were reachable at the start of this audit;
`NO_APPROVED_SNAPSHOT`, `NO_APPROVED_KNOWLEDGE`, and `NO_APPROVED_SOIL_PACKAGE`
are successful withheld responses, not missing observations or broken routes.
Application HTTP availability does not prove map rendering or evidence release.
The sections below retain their dated implementation and recovery history.

This local candidate starts from the authoritative Site v134 source
`daf4905a8216103ecfcde5c0b8fe09b3cca5eb52` and reconciles the Site application in
repository main `7d38bc5e906523dd0d666ee97af2a86130485390`. The common Site
baseline used for the file comparison is v131 source
`75d749ed5711ab20e3edabeb1c6ba135417ec1c0`.

The comparison found 51 changed files, 49 repository-only files, and nine
Site-only files. All nine Site-only files are retained. Four overlapping files
were reconciled explicitly: the Earth Engine display and export modules, the
main map page, and Earth Engine documentation. Per-layer image years coexist
with the shared color ramps and complete source-inventory exports. The map's
selected-source count includes soil state. Historical overlays, governed water,
knowledge, disaster/BLM controls, and Crop-CASMA retain their existing review and
release requirements. The HUD structure, observed-lightning loop, report drafts,
Globe, and Places remain available.

The legacy export test now supplies an explicit annual year. It also checks a
365-day year with the same display palette and source-inventory task, and rejects
incomplete coverage. Missing imagery authentication is reported as owner sign-in
required rather than an unexplained missing snapshot; authentication is unchanged.

Local service checks also found that the bridge's direct-entry comparison failed
through the stable Site symlink. Startup now compares resolved filesystem paths;
a regression covers the alias and imported-module cases. The local Data and
Stewards pages show a sign-in notice instead of redirecting to an unavailable
local sign-in route. The notice grants no access, and nonlocal requests retain
the existing authentication flow.

## Operating boundaries

Use the existing stable local Site alias and the existing loopback origin on
port 4173. Keep its `.wrangler/local-state` directory, DB/R2 bindings, and local
environment files. Browser-local Places, reports, and stories belong to that
origin and must not be cleared as part of a source update. The updated Qwen
bridge accepts that exact origin and retains its request and concurrency bounds.

At the 2026-10-02 handoff, the primary external data store, Earth Engine exports,
raw source collections, and task-local candidate stores remained in their original locations. A private
operational index in the existing external store's `data/catalog` lane points to
them. It is an inventory, not a source-admission or release record. PRISM
acquisition may continue while inventory counts are collected. Do not merge
unreviewed candidates into an activated package or the hosted Site's storage.

## Validation and recovery

Run `npm run install:ci`, `npm run build`, `node --test tests/*.test.mjs`, and
`npx tsc --noEmit`. The local handoff also checks page/assets, the bridge's exact
allowed and rejected origins, DB integrity, and held API outcomes. Browser
interaction is a separate acceptance gate: the browser tool's admin-enforced
security check was unavailable during this reconciliation.

Before updating the running copy, preserve its source commit, build, service
definition, local state, and unfinished changes outside the app tree. Roll back
the local application using the preserved build/source and service definition;
restore a transactional DB backup only while the service is stopped, after
preserving any new records. Source rollback does not authorize data withdrawal
or hosted publication. This change is local only.

Placement: application implementation and its tests stay in this standalone
Site; explanatory instructions reuse `docs/`. Operational inventories and
recovery archives remain outside application source and deployment assets,
consistent with Directory Rules v2 and accepted ADR-0029.

## Unfinished-edit accounting

All eight original unfinished repository files are preserved byte-for-byte in a
local recovery commit. The pixel-center labels and captured-fire selection
disclosure are carried forward. The original navigation work is represented by
the newer Site layer workflow and its current tests, rather than reverting to
older headings or the former single-year imagery controls. Historical checkpoint
text and the proposed archive-day limit change remain preserved for reference;
they are not silently reapplied over newer source behavior.

## Selection and request repair — 2026-10-03

Historical sheet detail now owns its image, review preview, review note, and
requests in a component keyed by catalog edition and scan ID. Switching sheets
removes the old raster and cancels pending status/review requests; a late result
cannot populate the next sheet's controls. The opacity choice remains in the
parent panel. Source links, Kansas-only selection, flat-map guidance, printed
scale, fit action, and explicit owner activation remain available.

Historical catalog, overlay status, preparation, review, and activation requests
have a 15-second deadline through body decoding, with their existing byte limits.
Timeouts produce a visible failure and a status-recheck action. Cancellation of
an already submitted preparation/activation request does not undo a server-side
write: check status before retrying an unconfirmed operation. Browser controls
continue to rely on the existing server owner checks; no automatic activation
or new publication authority is introduced.

Knowledge search associates each response with the exact submitted query.
Record navigation observes the current URL identifier and starts a new record
component when it changes. Both use cancellable reads capped at 1 MiB and 15
seconds. Display validation reuses the existing public-record validator, checks
record/release identity and result counts, and discards data on negative
outcomes. These checks protect presentation; they do not replace server-side
rights, sensitivity, review, release, correction, or digest validation.

Validation: `node --test tests/browser-request-lifecycle.test.mjs
 tests/historical-topo*.test.mjs tests/kansas-knowledge.test.mjs` covers response
limits, cancellation, stalled bodies, late results, identity mismatches,
withheld records, and the existing server-side review/activation boundaries.
Run the production build, complete Node suite, TypeScript, and full-tree lint
before installing the local application. The reviewed-water control derives
release expiry and evidence visibility from the active package and selection;
an expired release is withheld without waiting for a follow-up fetch. The
observed-lightning loop remounts when its external layer is disabled, so a
previous play action cannot resume after re-enabling it. HMS still cancels
pending publication and map requests when visibility or reduced-motion state
changes; it stops at the range end after the selected frame hold.
Browser map selection and record-navigation journeys remain a separate check.

Placement remains application implementation under `app/`, application
regressions under `tests/`, and this operational explanation under `docs/`,
consistent with Directory Rules and ADR-0029. No schema, data-store, dependency,
service binding, or hosted-source migration is part of this repair. Recover by
restoring the preserved prior application source and build without rolling back
D1/R2 data or device-local Places/reports.

## Direct local Worker runtime — 2026-10-03

The local production-build launcher is `scripts/serve-local-worker.mjs`. It uses
the already pinned Wrangler configuration translator and Miniflare/Workerd
runtime directly. This avoids Wrangler's development proxy, which returned an
intermittent HTTP 500 after a rejected owner request whose response body was
left unread. In a controlled five-start comparison with the same build and
copied storage, the proxy failed four times and the direct runtime passed all
five. This is a local runtime repair, not a general claim about upstream versions.

Run from this Site with Node 22.13 or a later Node 22 release:

```sh
node scripts/serve-local-worker.mjs --state "$(pwd -P)/.wrangler/local-state" --port 4173 --local-reviewed-imagery
```

Use the existing service's explicit Node path and working directory. Pass the
verified physical storage path in ExecStart; a stable checkout alias may locate
the script, but must not redirect its storage argument. The
launcher binds only `127.0.0.1`; it has no remote/deploy mode. `--state` must
already contain `v3/d1` and `v3/r2`. It never initializes a substitute data
store. For an isolated rehearsal use copied state and another port, omitting
`--local-reviewed-imagery`. That optional flag preserves the existing exact
4173 imagery-read exception; it does not grant owner review or activation.
The local entry also rejects a mismatched request origin/Host and any supplied
`oai-authenticated-*` header. The workstation has no trusted hosted identity
proxy, so clients cannot impersonate its authentication headers. Ordinary
same-origin requests continue to the unchanged application authorization.

Startup rejects changed storage identities, unsupported module rules,
additional Worker bindings, symlinked build/state paths, unexpected runtime
versions, and `.env` / `.dev.vars` files requiring configuration review. A future
runtime/configuration change must be explicitly reconciled and retested.
Generated build modules are enumerated within bounded depth, size and count.
The launcher logs readiness, pinned versions, configuration and entry digests;
ordinary request URLs/bodies are not logged by its runtime. Readiness means the
listener started, not that data is admitted, fresh, or ready for evidence use.

Keep the current service and its imagery override in the recovery archive.
After backing up the stopped application's source/build/state, replace the
service's effective ExecStart with this launcher. Validate imagery bytes,
application tables, static assets, held governed reads, rejected owner writes,
and the unread-response reproduction before accepting the local handoff.
Restore the old ExecStart, source and build on failure, then reload and restart
only this Site service. Do not replace D1/R2 or clear browser storage merely to
roll back application code. Browser acceptance remains a separate gate.

Placement: this is an existing Site `scripts/` runtime responsibility, with
regressions under `tests/` and this runbook under `docs/`, following Directory
Rules v2 / ADR-0029. Dependencies, hosted bindings, hosted deployment and data
publication are unchanged.

## Physical folder consolidation — 2026-10-06

The private data catalog now records a completed relocation of 25 inactive
directories: 18 Desktop reference folders into `~/KFM-references`, six prior
build/state/sync recovery packages into `~/KFM-site-recovery`, and the existing
Earth Engine working collection into
`~/Projects/KFM-data/data/work/earth-engine`. A single Desktop shortcut opens
the references. Only the empty former `~/KFM-data` container was removed;
49,749 payload files (11,030,136,366 logical bytes) were preserved and hashed
before and after each no-overwrite move.

Use `~/KFM-site-recovery/KFM-Explorer-local-state-pre-v153-20261005` for the
pre-v153 backup. Do not confuse it with live `.wrangler/local-state` or infer
that it supersedes newer user records. The Earth Engine preparation tools take
an explicit `--data-root`, and restoration takes an explicit `--package`;
use the new path. Existing display-set IDs, manifests, review labels, and
historical receipts remain byte-identical. No admission, activation, release,
or publication state changed.

The full manifest and rollback helper are private under
`~/Projects/KFM-data/data/receipts/local-organization/20261006T163401Z/`, linked
from the existing `data/catalog/KFM-LOCAL-DATA-CATALOG.md`. Rollback rejects
content drift and occupied original paths. Source checkouts, unfinished work,
synced project files, active PRISM acquisition, current Site source/alias, and
actual D1/R2 persistence were preserved. Explorer, Qwen, and PRISM process IDs
and service states were unchanged; Explorer and the origin-checked bridge
returned HTTP 200. The relocated reviewed imagery package passed read-only
validation for 15,839 objects with the same manifest digest. These are storage
and HTTP checks, not a new browser acceptance or source-release decision.
