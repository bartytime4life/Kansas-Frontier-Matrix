# Water pilot: acquisition, candidate review and governed reads

Status: implemented delivery candidate. On 2026-10-10 the owner admitted the USGS
discharge source and accepted ADR-0044; see [Releasing the discharge layer](#releasing-the-discharge-layer).
No real package has been released, activated or published yet.
The first milestone remains open until the real reviewed package completes the
local browser journey and private Site acceptance/rollback gates.

## Current cutaway image-status candidate — v220 / 2026-10-10

Owner-private Site v220 source `19d19c2cb8ac02ba36389e863aba6d2e5b498878`
deployed successfully as `appgdep_6acab87ad70081918a81cdfc918fc69e`.
Underground now reports **HIGH-DETAIL MAP** only after an intersecting
high-detail mesh attaches. If it clears or never attaches, the caption describes
the selected-area fallback image or states that no map image is available.
The actual component-callback regression failed on v219 and passes on v220.
All 1,006 Site tests, type checking and the production build pass, including
28 focused tests. The 928 source files and 427 build files checksum-match the
new PC installation; port 4173 returns HTTP 200. The original persistent store
and v219 installation remain intact. There is no data or storage migration.
The [926-file receipt](../../data/receipts/generated/site-v220-cutaway-image-status-20261010.json)
retains two canonical tool mappings and is REVIEW_ONLY with human acceptance
pending. The built browser rendered a ready 4096 × 3437 surface, 28 recorded
columns and one aquifer overlap with partial-coverage disclosure. Its caption
visibly read **HIGH-DETAIL MAP** below the rendered model. Broader device and
hosted acceptance remain open. Rollback to v219 was prepared, not rehearsed this batch.
Source admission, data activation, acquisition jobs and infrastructure are
unchanged.

## Previous cutaway texture checkpoint — v219 / 2026-10-10

Owner-private source `24b469fab699a04db1a0ce6730a9257b1b800a4c` deployed as
`appgdep_6acab51384c8819192cfc1f570059373`. Appearance controls reuse the
current map texture; changing its sampling mode or replacing its image still
updates it. New high-detail frames retain Exact pixels/Smooth image. Source
pixels, geographic mapping, camera behavior, data and release boundaries remain
unchanged. The 24-update regression now marks zero extra texture uploads,
previously 24; this is work-count evidence, not browser FPS or provider latency.
Both added regressions failed before the fix. All 1,006 Site tests, type checking
and production build pass, including 28 focused tests. The built browser rendered
one aquifer range and 28 columns from 50 records, disclosed partial coverage,
selected Smooth image and changed opacity by keyboard and pointer. Surface
refresh reached ready at 4096 × 3437 pixels, retaining Smooth image and 65%
opacity. Intermittent browser-control timeouts recovered. Broader acceptance
remains open. An older MAP IMAGE UNAVAILABLE caption remains below the rendered
detail; diagnosis and correction of that fallback-image status are separate.
All 928 source and 427 build files checksum-match the new v219 PC installation;
port 4173 returns HTTP 200. The original persistent store and v218 installation
remain intact. No data migration; rollback has not been re-rehearsed this batch.
The [926-file mirror receipt](../../data/receipts/generated/site-v219-cutaway-textures-20261010.json)
retains two canonical mappings, PENDING human review and unevaluated hosted
parity. The owner marked PR #5018 ready for review at 21:55:13Z on October 10;
this does not approve or merge it. Predecessor head `c31f097bc4f25eb8731148097a87272997dec43e`
completed 107 checks successfully with two skipped. Updated-head checks are separate.
No new source admission, data activation, acquisition jobs or infrastructure.

## Previous cutaway rendering checkpoint — v218 / 2026-10-10

Owner-private source `ca42e125009db406f9fa12700185559aac717008` deployed as
`appgdep_6acab203acf88191b9383bffa79560e7`. Camera, appearance and surface
redraws share one animation-frame request. Every input step still updates the
camera, damping settles without an idle loop, and hidden/lost/disposed views
cancel pending work. Geometry, source values, sampling and hit targets are unchanged.
The synthetic 40-pose test reduced 80 draw calls to one with identical final pose;
this does not measure real browser FPS or provider latency.
All 1,004 Site tests, type checking and build pass, including 29 focused tests.
The browser rendered one aquifer range and 28 columns from 50 records with partial
coverage, then exercised Top view, sample selection, evidence drawer and Zoom to
sample. Some browser-control calls timed out; the last Reset view attempt remains
unverified and full device/accessibility/hosted acceptance remains open.
All 928 source and 427 build files in the new local v218 installation checksum
match; port 4173 returns HTTP 200. The original store and v217 installation remain
available. Rollback was not re-rehearsed; no data migration occurred.
The [926-file receipt](../../data/receipts/generated/site-v218-cutaway-render-20261010.json)
retains two canonical tool mappings, PENDING human review and NOT_EVALUATED hosted
equivalence. PR #5017 merged externally to `8d109497c04e34a25154de81b095bbb0deb6a5ad`
with 107 successful checks and two skipped. This candidate requires its own checks.
No new source admission, data release/activation or acquisition-job installation.

## Previous map loading checkpoint — v217 / 2026-10-10

Owner-private source `c1a192997c8ae94296756cc3406dd77b09eed880` deployed as
`appgdep_6acaaa1f8a5c8191bcdf80c1bb44f1f8`. The map now downloads Underground
controls when requested. Shared imports, current privacy/context props, close,
cancellation and retry preserve the original panel's boundaries. The initial
map JavaScript list shrank from 1,637,812 to 1,591,522 bytes (14,293 gzip bytes
saved); no whole-map startup or FPS improvement has been measured.
All 999 Site tests, type checking and build pass; loader/test lint has zero errors
or warnings. A built browser opened Underground, loaded the High Plains example,
closed and reopened the panel. Source coverage remained explicit. Some browser
control calls timed out; full device, accessibility and hosted acceptance remain
open. The local PC has 927 source and 427 build files checksum matched, with HTTP
200 on port 4173 and its original store. The v216 installation is retained;
rollback was not re-rehearsed in this batch.
The [925-file receipt](../../data/receipts/generated/site-v217-deferred-underground-20261010.json)
keeps two canonical tool mappings, PENDING human review and NOT_EVALUATED hosted
equivalence. PR #5016 merged externally to `23bdd31f8fd0ce9011c4a6206348c798aaefc38b`
with 107 successful checks and two skipped; this candidate needs its own checks.
No data admission, release, activation or acquisition-job installation occurred.

## Previous map startup checkpoint — v216 / 2026-10-10

Owner-private source `e7ec041d96fae5a4defc16b495d00ca817249da0` deployed as
`appgdep_6acaa4eb66f4819191ea4102598f9459`. Its initial map load reuses the
successful style setup instead of repeating all layer/terrain/overlay updates;
failed setup retries and later style loads still rebuild their layers.
All 994 Site tests pass, including four callback regression cases; type checking
and build pass. Changed-area lint retains the same 41 warnings with zero errors.
The built local browser reached ready, switched to Midnight navy, returned to
standard and showed no console errors during that bounded journey. This proves
neither full device acceptance nor an overall startup timing improvement.
The local PC has all 924 source and 426 build files SHA-256 checked, HTTP 200 on
port 4173 and its original store. The v215 installation remains the rollback;
rollback was not re-rehearsed in this batch.
The [current receipt](../../data/receipts/generated/site-v216-map-startup-20261010.json)
records 922 matching mirror files and two canonical tool mappings. Content parity
is separate from PENDING human review and NOT_EVALUATED hosted equivalence. No
data release, activation, source admission or water-job installation occurred.

## Previous water rendering checkpoint — v215 / 2026-10-10

Owner-private Site source `1d74c8ea4e4aff4eb14c62f7799ee65a3d36dcec` is deployed
as `appgdep_6acaa14425988191a75b67a21fbdf46c`; the local copy uses the same
source and build, with its original store and v214 recovery installation retained.
The [new receipt](../../data/receipts/generated/site-v215-water-flow-performance-20261010.json)
records 921 matching mirror files and two canonical tool mappings. The selector
checks current content parity only; human review remains PENDING / NOT_EVALUATED.
The change batches geometry from cell/gauge callbacks, rejects cancelled old
responses and cleans up on map removal. All 990 Site tests pass; the
[performance note](../../apps/site/source/docs/water-flow.md#frame-batching-follow-up--2026-10-10)
separates synthetic work reduction from broader browser performance. No data
admission, package release, activation or job installation occurred in this batch.
PR #5015 merged at `b20a692efd5b2882935682c2556a0dc670cb95f0`; its head finished with 107 successful checks and two skipped. Those checks do not release a data package.

## Previous Site reconciliation — v214 / 2026-10-10

The [reconciliation report](../reports/kfm-reconciliation-20261010.md) records
owner-private v214 source `11f1c546d56dcaec08454f99130350ce536328a2`, deployed as
`appgdep_6aca9c6e29a48191aac22f020f764428`, and the matching local installation.
That checkpoint selected the [921-file receipt](../../data/receipts/generated/site-v214-reconciliation-20261010.json)
for **CONTENT_PARITY_ONLY**, with two additional canonical local-tool mappings.
All prior receipts remain historical. Source/overlay review is **PENDING**;
`review_acceptance` is **NOT_EVALUATED**. No source admission, package approval,
activation or hosted equivalence is inferred from this check. PR #5014 subsequently merged at `033f8466c28e7de32fcac95c441fa9f8cbeade2d`.
The following audit explains the separation between content parity and acceptance.

## Mirror governance audit — 2026-10-10

**CONFIRMED at repository `main@82dfddf806f0c0e0ab7c67b139d17490abb8352f`:**
[PR #5010](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5010)
merged at 18:01:01 UTC and selected the
[896-file v192 refresh](../../data/receipts/generated/site-mirror-v192-repository-refresh-20261010.json).
Before this audit, [PR #5012](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5012)
merged at 19:18:14 UTC and selected the
[907-file successor](../../data/receipts/generated/site-mirror-v192-water-release-20261010.json).
Both retain the independently recorded
[private v192 checkpoint](../reports/repo-live-alignment-20261009.md), source
`424e62cd429ba3ea13a109e6e37953eea857857f`, as their Site basis.
Neither receipt attests that its repository overlays are deployed.

| Receipt | Identical to attested v192 bytes | Modified v192 files | Repository-only additions | Total overlays |
|---|---:|---:|---:|---:|
| #5010 refresh, now superseded | 761 | 56 | 79 | 135 |
| #5012 successor, active at the audit head | 759 | 58 | 90 | 148 |

Read-only Git-object verification recomputed every mirror digest at #5010's
repository base `40302b708cacfa92ce7304b76cfb65e37ab7f403` and the audited
current head, and every Site-basis digest at repository
`899dc274ffe37d2900f49eabd66ea3c7b0b2a484`. All 896 and 907 recorded paths,
digests and classifications matched, with zero errors. This verifies the
recorded repository basis; the standalone Site and its current deployment were
not re-read for this audit.

Both receipts declare `status: review_pending`,
`review.source_and_overlay_review: PENDING`, and the blocking items
`repository_review` and `overlay_reconciliation_with_next_site_version`.
The deployed-candidate flag refers to the historical v192 source checkpoint;
it is not a deployment flag for any overlay.

### Consumers and authority

The only executable consumer found for `site_mirror.py --check` is
[water-pilot.yml](../../.github/workflows/water-pilot.yml), job
`water-conformance`. It consumes the exit status after the synthetic water tests
and isolated fixture regeneration. At the audited head,
[run 38079262403](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/38079262403/job/114292620519)
passed: 287 water tests, eight regenerated synthetic outputs, and a mirror result
of `PASS`, `files: 907`, `authority: CONTENT_PARITY_ONLY`,
`hosted_equivalence: false`. The old step label, **Check reviewed mirror digests**,
overstated what that step evaluated; its output omitted the receipt's review
declarations. This is a reporting ambiguity, not a demonstrated defect in the
content-parity algorithm.

| Related readiness surface | Verified relationship to the mirror result |
|---|---|
| `water-pilot` / `water-conformance` | Exit-status consumer; green means its bounded tests, regeneration and recorded-content parity passed. It does not establish review acceptance or hosted equivalence. |
| [policy-test](../../.github/workflows/policy-test.yml), [hydrology-proof-slice](../../.github/workflows/hydrology-proof-slice.yml) | Inspect the water workflow's test coverage paths; do not consume the mirror outcome or accept overlays. |
| [Readiness lane registry](../../control_plane/readiness/lanes.json) / [runner](../../tools/readiness/run_lane.py) | No mirror-result consumer. Policy/proof-slice PASS retains explicit authority boundaries; fixtures/catalog remain separate HOLD lanes. |
| [release-dry-run](../../.github/workflows/release-dry-run.yml), [validator-suite](../../.github/workflows/validator-suite.yml) | No mirror-result consumer or promotion from parity. Their own bounded checks do not establish Site deployment. |
| [Water delivery settings proposal](../security/water-delivery-review.md#ruleset-correction-for-owner-review) | Names `water-conformance` as a proposed required CI context. The proposal is not an applied approval policy, and a CI conclusion cannot stand in for review acceptance. |

No executable path was found that converts the mirror PASS into overlay
acceptance, source admission, release, activation, or deployment. Existing
dated mirror holds elsewhere remain historical observations, not claims about
the current parity result.

### Owner disposition and remaining reconciliation

The [owner-account response on #5010](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5010#discussion_r4238649722)
states that the owner's merge is the receipt review decision and that pending
receipts have historically been checked for content parity. GitHub records
the subsequent merge. The reply is AI-generated text posted under the owner
account; it is recorded disposition, not proof of an independent file-by-file
review. The receipt still carries the pending declarations above. This audit
records both facts without changing either record or treating a parity result
as approval.

Remaining obligations are to reconcile the recorded PR disposition with the
source/overlay review fields at the appropriate scope, and to reconcile the
overlays against a later immutable Site source/version if deployment is chosen.
Fresh hosted equivalence, browser acceptance and deployment/rollback evidence
remain separate. The later #5012 source-admission and ADR-0044 decisions are
outside this mirror audit and are not inferred from the mirror check.

The reporting correction keeps the existing parity validation, allowed states,
PASS/FAIL and exit codes. JSON now includes file-state counts and a separate
`review_acceptance` projection: `outcome: NOT_EVALUATED`,
`authority: RECEIPT_DECLARATION_ONLY`, and the receipt's status, source/overlay
review and blocking declarations. Missing declarations are `null`; even an
accepted declaration is not authenticated by this check. No external PR
disposition is fetched or inferred at runtime.
`python tools/qa/site_mirror.py --check --format markdown` renders these
dimensions independently in the GitHub step summary. The workflow uses Bash
with `pipefail`, so writing the summary cannot hide a parity failure. Its
focused tests cover pending and absent declarations, all historical overlay
states, and successful/failing execution of the actual summary command.

Local validation of the reporting correction: 18 focused mirror tests and the
complete 305-test water command passed; isolated fixture regeneration produced
eight outputs without overwriting reviewed files. Workflow security passed
28 tests and the 492-workflow scan with zero new drift. The documentation gap
ratchet passed 13 tests and retained its 138-link historical baseline. Repository
topology passed for 14,575 tracked paths with zero new drift. Hosted execution
of this reporting correction remains pending; the hosted run cited above tests
the pre-correction audit head.

Rollback: revert the reporting changes to the tool, workflow, tests and guidance.
Preserve both receipts and their selector; no private Site or data state is
changed by this audit.

## Identity and placement

Implementation starts at monorepo `6994a65843c4999313fda01183b63333213134f3`.
The standalone Site is authoritative for application source. This candidate
rebases on owner-private Site v130, source
`8d82d9af72930e2df9e3b14e15b0a5bf6463799c`; the earlier security scan pins v126.
Site version, deployed version, source commit, local build and package identity
are independent. The mirror receipt names the unpublished candidate commit;
it does not attest to hosted equivalence.

[Directory Rules](../doctrine/directory-rules.md), adopted by
[ADR-0029](../adr/ADR-0029-adopt-directory-governance-standard-v2.md), determine placement:
connectors acquire; pipelines transform; packages provide reusable parsing,
catalog, evidence, policy and release mechanisms; apps serve; tools operate;
schemas/contracts define machine shapes; contracts explain semantics; infra
contains deployment templates; control_plane retains projections; external data
stores preserve lifecycle bytes. Synced project sources remain read-only.

## Site mirror review checkpoint — 2026-10-01

**CONFIRMED at monorepo `main@6c57290f9c729c8036dcf3d9d5d674a3e767b695`:**
the [reviewed mirror receipt](../../data/receipts/generated/site-disaster-blm-knowledge-soil-mirror-20260930.json)
records standalone Site candidate `041f626585804e5c90b8075cc506aeff5333d3b1`
and 283 monorepo mirror files. A read-only comparison of that exact Site commit
found all 280 candidate-file hashes equal to the receipt's `site_sha256` values.
The monorepo has 21 files whose bytes differ from that candidate and three
repository-only water files, consistent with the receipt's explicit overlay
model. The standalone Site working checkout has unfinished edits; these were
not included in the commit-pinned comparison or changed by this review.

Seven **monorepo** files now differ from their recorded `mirror_sha256` values:

| Receipt state | Paths with current mirror drift | Recorded monorepo changes after the receipt |
|---|---|---|
| `inherited_repository_overlay` | `README.md` | `00450b00caf6e0227e37cbef93e76c4799e1ddff` |
| `merged_water_overlay` | `app/page.tsx` | `00450b00caf6e0227e37cbef93e76c4799e1ddff` |
| `identical` at receipt time | `app/crop-casma-control.tsx`, `app/map-layer-composition.ts`, `app/map-layers.css`, `tests/crop-casma-storage.test.mjs`, `tests/map-composition.test.mjs` | `00450b00caf6e0227e37cbef93e76c4799e1ddff`; the last test also changed in `2457ef08694805139a0a1018a1209d512a864cb0` |

The receipt was last committed at `4793bb07f80506f35ed3515439e10c9906737e2e`.
[`site_mirror.py --check`](../../tools/qa/site_mirror.py) therefore returns
`MIRROR_REVIEW_REQUIRED`, as the `water-conformance` job reports. This is a
content-parity hold, not evidence that the seven newer overlays are wrong or
that the standalone candidate was deployed. The receipt declares that candidate
unpublished; hosted equivalence and current deployment remain **UNKNOWN**.

**NEEDS VERIFICATION before a successor receipt:** the Site owner must establish
which newer monorepo overlays belong in the next standalone Site source commit,
and which remain explicitly governed repository overlays. Compare the resulting
immutable Site commit against every mirror file; independently review overlay
reasons and source identity; run Site and monorepo changed-area tests, type checks,
mirror integrity, and the relevant browser journey. Preserve the existing
receipt as historical evidence. A successor receipt may record reviewed current
bytes only after that review; a matching digest alone does not authorize Site
deployment, water activation, release, publication, or owner acceptance.

This checkpoint changes documentation only. Reverting it restores the previous
runbook text; it does not alter the held mirror check or any Site/data state.

## Site mirror currentness — 2026-10-01

**CONFIRMED at monorepo `main@bc4b3ca4ad4defa390166741b21b714b6ab85f87`:**
a read-only SHA-256 comparison of every tracked file in standalone candidate
`041f626585804e5c90b8075cc506aeff5333d3b1` against the historical mirror
receipt found no candidate/receipt hash mismatch. The monorepo still has 283
tracked mirror files and the candidate has 280; neither file set drifted from
the receipt. Current monorepo bytes differ from the receipt for ten files,
up from seven at the earlier checkpoint. Current monorepo bytes differ from
the pinned candidate for 23 files. These counts do not include uncommitted
standalone Site work or establish hosted equivalence.

The three newly drifted mirror paths are `app/governed-water-control.tsx`
(`repository_only_water_overlay`), `app/governed-water.ts` and
`tests/governed-water.test.mjs` (both `identical` at receipt time). Their
post-receipt changes are in `91656a5e0a`, `1344ad677b`, and `1beb3a1a8b`;
the control component changed in the last of these. The earlier seven drifted
paths remain listed above. The current `site_mirror.py --check` still returns
`MIRROR_REVIEW_REQUIRED`; changing that result requires a reviewed successor
source/overlay decision and receipt, not a digest update to historical proof.

The standalone checkout at the pinned candidate commit also has 11 unfinished
tracked edits, including `app/page.tsx`, which overlaps an existing monorepo
mirror drift. Its other edited paths are `app/earth-engine-display.tsx`,
`app/fire-report-analysis.ts`, `app/globals.css`,
`app/report-story-workspaces.tsx`, `app/workspace-model.ts`,
`app/workspace-storage.ts`, `docs/EARTH_ENGINE_CONTEXT.md`,
`tests/earth-engine-rendered.test.mjs`, `tests/fire-report-analysis.test.mjs`,
and `tests/snapshot-workflows.test.mjs`. These edits were preserved and were
not treated as an immutable Site source commit. Before a successor receipt,
the Site owner must select which monorepo overlays belong in a new standalone
source commit and which remain reviewed repository overlays, then resolve the
unfinished source edits independently. Site tests, rendered browser behavior,
deployment, source admission, release, publication, and owner acceptance were
not established by this read-only comparison.

## Site mirror source-identity guard — 2026-10-01

**CONFIRMED at monorepo `main@9465a573d8859cd1564124897d10d848f9c7c350`:**
`site_mirror.py --source` previously read working-tree bytes but labeled its
comparison with `git rev-parse HEAD`. On a dirty standalone checkout, that
could associate uncommitted Site content with an immutable commit ID. The
comparison now requires a clean source before reading files and rechecks the
commit and worktree status afterward. A dirty or changed source returns the
existing finite `MIRROR_REVIEW_REQUIRED` failure; synthetic tests cover both
conditions. The held historical receipt and `--check` decision are unchanged.

A read-only comparison of the **clean local** standalone Site checkout at
`58aac81757639c2226187810b486b8a8de4b9c22` reported 51 differing shared
paths and 50 monorepo mirror paths absent from that checkout. These counts
describe this local commit against the current working monorepo tree, not a
reviewed successor source, deployed Site, or approved overlay set. The Site
preservation instructions prohibit bulk replacement. `MOD-01` therefore
remains held until the source owner reviews the source lineage and each overlay
before a new receipt is authored. No historical receipt is rewritten here.

## Site mirror drift diagnostic — 2026-10-01

From the repository root, `python tools/qa/site_mirror.py --diagnose` reports
tracked mirror files whose working-tree hashes differ from the reviewed receipt,
plus recorded paths that are missing and newly tracked paths absent from that
receipt. It exits nonzero when review is required. The output identifies its
byte source as the working tree and reports whether the repository is dirty;
`repository_head` must not be treated as the identity of dirty bytes. No file
contents are printed. Run `--check` separately for the unchanged conformance
decision. Diagnostic hashes and path lists organize overlay review; they do not
approve a source commit, update a receipt, or establish hosted equivalence.

At monorepo `main@5021bc0a686a9b0df67858ac8ddf624ec1663030`, the
diagnostic found 15 tracked paths with changed digests and six newly tracked
mirror paths absent from the historical receipt. The comparison was run from a
working tree with tool edits, so the result is a dated review inventory, not a
commit-bound source artifact. The mirror hold remains in force.

## Site mirror successor receipt — 2026-10-03

At the repository owner's request, the
[successor mirror receipt](../../data/receipts/generated/site-mirror-overlay-refresh-20261003.json)
records the 289 mirror files at monorepo `main@2da0fd9f8134b87bdc3f1a0642a301a7b6350dba`,
and [`site_mirror.py`](../../tools/qa/site_mirror.py) now checks against it. The
[2026-09-30 receipt](../../data/receipts/generated/site-disaster-blm-knowledge-soil-mirror-20260930.json)
is unchanged and is named in the successor's `supersedes` field.

The successor compares against the same pinned standalone candidate
`041f626585804e5c90b8075cc506aeff5333d3b1`. No newer standalone Site commit was
available, so its `site_sha256` values are carried from the earlier receipt. The
receipt lists all 21 changed paths with their previous state and digest:

- The 15 drifted paths keep their overlay state. A path that was `identical`
  becomes `inherited_repository_overlay`.
- `app/governed-water-availability.ts` and its test are
  `repository_only_water_overlay`.
- The Qwen availability, Qwen context-safety, and client-store boundary files
  use a new `repository_only_overlay` state for monorepo-only files outside the
  water slice.

Validation on a copy of the mirror: `npm test` passed 267 of 267, and
`tsc --noEmit` passed. `npm audit` reports eight high-severity advisories, all
through `braces`; they are recorded, not fixed. The browser journey was not run.
On 2026-10-03, `@bartytime4life`, as repository and Site owner, accepted all
21 paths as governed monorepo overlays with the states recorded in the receipt.
This meets the prerequisite in the review checkpoint above, and the receipt
records the decision under `refresh.overlay_acceptance`. `site_mirror.py --check`
now passes. That is content parity only. Whether each accepted overlay is
folded into a successor standalone Site commit, hosted equivalence, deployment,
and water activation remain **NEEDS VERIFICATION**.

## Saved Site v138 mirror candidate — 2026-10-04

The [v138 successor receipt](../../data/receipts/generated/site-mirror-v138-candidate-20261004.json)
pins owner-private Site source `cdbab7bc0f599d3e2d199a310c803d98565bbbd7`
and repository base `ef9c5e19e373d51c2bf878aaf8c3a5ddf0deb35e`. A clean,
isolated copy of that Site source supplied the tracked files. The repository
mirror now has the same 336 tracked paths and bytes: 229 were already equal,
60 existing paths changed to the Site version, and 47 Site paths were added.
There were no mirrored paths to delete. The prior receipt and its overlay
decision remain in history; this new candidate does not retroactively change
them. `site_mirror.py --check` checks the new receipt for content parity only.

Saved v136 moved device-only GeoPDF protocol registration through the Site's
existing `maplibre-seam.ts`, without changing the tile callback or teardown.
The acquisition inventory now returns its inherited `HOLD` for the accepted
candidate seam, rather than the new outside-seam `FAIL` seen on the first draft.
Saved v137 renamed five new Site documentation files to lowercase names and
updated their three links. The repository topology ratchet now reports zero
new drift, zero stale baseline entries, and no invariant failures; its
baseline was not expanded.
Saved v138 makes local Earth Engine package reads verify the opened Linux file
descriptor and enforce a byte limit during reading. Focused tests reject
traversal, leaf and ancestor symlinks, and oversized files. This addresses the
CodeQL high finding on the first draft; CI rescan of the new source is pending.

The mirrored Site passed its locked `npm ci`, production build, 346 Node tests,
TypeScript `--noEmit`, and eight mirror-tool tests. Full Site lint failed with
six `react-hooks/set-state-in-effect` errors and 39 warnings: three errors are
in the unchanged water control; three came with the new smoke and lightning
controls. A fresh `npm audit` found eight high findings and no critical ones
through the unchanged lockfile. These are review holds, not green checks.
Browser acceptance remains unrun because the available browser control failed
its security verification.
The saved Site v138 is **not deployed**; deployed version v131, hosted
equivalence, source/overlay review of this successor, activation, publication,
and water admission are separate pending decisions. The Site source repository
advanced to saved v138, while D1/R2 bindings and the deployed Site stayed as
they were. To roll back the mirror, revert this candidate commit and restore
the previous receipt selector; do not change deployed Site or stored data as
part of that rollback. Saved v137, v136 and v135 remain available as source
recovery points.

## Saved Site v139 mirror candidate — 2026-10-04

The [v139 successor receipt](../../data/receipts/generated/site-mirror-v139-candidate-20261004.json)
pins owner-private Site source `25238b376ef5cbfc1918a2e48f1e508ad8017fd6`
and repository base `3315c6712145a00af5ba8a732743085df0a20523`,
which includes the merged v138 mirror PR #4876. Five existing Site paths
changed and no paths were added or removed. The preceding v138 receipt remains
in Git history. This mirror is a content-parity candidate, not hosted
equivalence or a data release.

The reviewed-water control now derives visibility from the release approval
time and associates evidence with the selected station and package, so stale
evidence is hidden immediately on selection or expiry. The lightning loop
remounts after its external layer is disabled; an old play action cannot
resume on re-enable. HMS playback cancels outstanding publication and map
requests when disabled and ends after the selected frame hold. The Site's HUD,
data bindings, and existing map layers are unchanged by this slice.

The authoritative Site v139 source passed full lint with zero errors and 39
warnings, TypeScript checking, and `npm test` (production build and 346 Node
tests). Browser acceptance is unrun because browser control remains
unavailable. A fresh audit of the unchanged dependency lockfile found eight
high findings and no critical findings; reachability and remediation remain
open. The mirror check passed for all 336 tracked files, the eight mirror-tool
tests passed, topology showed zero new drift, and the MapLibre acquisition
inventory retained its accepted-seam `HOLD`. New-head CI is separate evidence.
Site v139 was saved with an archive and is **not
deployed**; deployed v131, release activation, source review, and publication
remain distinct. Restore the previous mirror commit and v138 receipt selector
to roll back this repository candidate. Saved v138 remains a Site source
recovery point; do not alter D1/R2 or the deployed Site as part of a mirror
rollback.

## Saved Site v140 mirror candidate — 2026-10-04

The [v140 successor receipt](../../data/receipts/generated/site-mirror-v140-candidate-20261004.json)
pins owner-private Site source `ebd5a5c11ee21f0658ef6b4c4e213814346d2aec`
and repository base `7721237ad670ffd948a0c7e8b496f509dad6a0c4`,
which includes merged v139 mirror PR #4877. Four existing Site paths changed;
no paths were added or removed. All 336 tracked Site files are byte-identical
to the mirror candidate. The v139 receipt remains historical. Parity is source
evidence, not hosted equivalence or a data release.

The selected-station evidence control now checks the station, package, release
times, correction state, dataset reference, and measurement references before
showing evidence. A fresh export rejects a response containing any other
station, and changing selection during the export withholds the download.
These are browser-side integrity checks over the existing governed API; they
do not grant release authority or replace server validation.

The saved v140 source passed TypeScript, full lint with zero errors and 39
warnings, and `npm test` with its production build and 349 Node tests. The
mirror comparison, receipt check, eight mirror-tool tests, and repository
topology checks passed; topology reported zero new drift and 113 baselined
warnings. The MapLibre inventory retained its accepted-seam `HOLD`. A fresh
lockfile audit reports eight high development-dependency findings and zero
production-dependency findings with `--omit=dev`; disposition remains open.
Browser acceptance, new-head CI, and hosted equivalence are unverified.

Site v140 was saved with an archive and is **not deployed**. The deployed Site
remains v131; D1/R2 bindings, water release state, and existing map layers were
not changed. Roll back the repository candidate by reverting its mirror commit
and restoring the v139 receipt selector. Saved v139 remains a source recovery
point; any future deployed rollback requires its own release review.

## Deployed Site v153 progressive water paths — 2026-10-05

The [v153 mirror receipt](../../data/receipts/generated/site-mirror-v153-water-paths-candidate-20261005.json)
pins owner-private Site source `da94de300c1b20dc98e9f527ba54613cfd696f8b`.
Six changed Site paths preserve 370 tracked paths with no deletions. A selected
gauge now displays the verified nearby USGS 3DHP segment while the same request
continues to the longer downstream route and 3DEP terrain; interrupted or
malformed streams cannot be presented as a completed route. Station identity
and coordinates, rather than changing observations, key the request. Completed
routes are reused for 15 minutes within the page for at most 24 stations. The
original JSON route remains compatible. This is external context and does not
admit, approve, or release water data.

At one local live-provider gauge, the nearby segment arrived in 1.64 s and the
full route with terrain in 10.65 s. Through the local Site HTTP route, the
nearby segment arrived in 1.52 s and the full 40 km route in 6.37 s. These
dated samples show earlier first display, not a guaranteed provider response
time. TypeScript, production build, and 385 Node tests passed on the exact
v153 source. The owner-private v153 deployment
`appgdep_6ac3bc6ea4148191adb9c80575feb842` succeeded. V152 remains saved
and was the immediately preceding deployed version. Browser visual acceptance
was blocked by the unavailable admin-enforced browser security check; hosted
streaming, repository review, and v153 changed-area security review remain
separate checks. Rollback is saved Site v152 plus the previous mirror receipt.

## Saved Site v152 smoke repair candidate — 2026-10-05

The [v152 mirror receipt](../../data/receipts/generated/site-mirror-v152-smoke-candidate-20261005.json)
pins owner-private Site source `c7718fe5c8ee5f002c9ed522d16f4dcb48e51782`.
Four changed paths preserve 370 tracked Site paths with no deletions. Checking
a dated HMS smoke publication now opens at its first provider-supported
footprint rather than the empty midnight stop; midnight remains available in
the time sweep. The layer row distinguishes zero Kansas footprints in a checked
window from a failed source. NOAA daily KML and the local API returned two
Kansas polygons for 2026-10-02 and zero for 2026-10-04. This does not establish
live-browser rendering. TypeScript, the production build and 383 Node tests
passed on the exact v152 source. Lint had zero errors and 42 warnings. The
repository topology ratchet reported no new drift. The dependency audit
reported eight high development-dependency findings and zero production
findings.

At candidate capture, Site v152 was saved with an archive and not deployed.
Following the owner's explicit deployment request, the private deployment
`appgdep_6ac3b4f9d6c48191b47c3232b82a062c` succeeded on 2026-10-05 at
14:32:39 UTC for the exact saved v152 version. V147 remains the previous
deployed recovery version. Browser acceptance is still unverified because the
admin-enforced security check was unavailable; v151 security follow-up, v152
changed-area review, source provenance and repository review remain separate
gates. Deployment did not activate a governed water release or admit a source.

## Saved Site v151 mirror candidate — 2026-10-04

The [v151 mirror receipt](../../data/receipts/generated/site-mirror-v151-candidate-20261004.json)
pins owner-private Site source `c390a9b1fbb9a079d23325ad21c52f226ed105c8`
and 370 byte-identical tracked paths. It preserves the v150 candidate and adds
an aggregate time, response-byte, and observation budget to statewide USGS
streamflow requests, plus a per-Worker concurrent-request guard. When a budget
ends acquisition, the response discloses partial coverage or fails without a
usable inventory. A host-wide limit across Worker instances is still not
established. The locked install, production build, 383 Node tests, TypeScript
check, and lint passed; lint reported 42 warnings. The security follow-up,
provider provenance, browser acceptance, and new-head CI remain review gates.
Site v151 is saved with an archive but is not deployed; v147 remains live.

## Saved Site v150 mirror candidate — 2026-10-04

The [v150 mirror receipt](../../data/receipts/generated/site-mirror-v150-candidate-20261004.json)
pins owner-private Site source `ba7438a9820a0b2d9beed675b96cf1dfac510d43`
and repository base `0835f02f0bcf7c19c9a4fdcbe509dc1770e9b0f3`.
Its 369 tracked Site paths were byte-identical to the v150 mirror candidate: 64
changed paths, including 32 additions, and no deletions. The previous mirror
receipt remains as dated evidence. Site v147 is deployed; v150 is saved with a
build archive and has no deployment. Neither parity nor deployment grants water
source admission or release authority.

Saved Site versions v148 (`c16269b8`) and v149 (`0d588909`) were superseded
before mirror review. Their lightning fixture note and three local
timestamp filenames added one topology path-grammar drift. V150 uses lowercase
fixture paths without changing the captured NOAA bytes or runtime code. The
topology ratchet now reports zero new drift and 113 baselined warnings.

The saved Site includes the A→B→A water-export selection guard and keeps newer
lightning archive, river, smoke, and groundwater work from the authoritative
Site. Its locked install, production build, 379 Node tests, TypeScript check,
and lint passed; lint reported 42 warnings. The lockfile audit reported eight
high development-dependency findings and zero findings with `--omit=dev`.
Source/security review, browser acceptance, hosted equivalence, and any real
water-package admission remain separate gates. Roll back this repository
candidate by reverting its mirror commit and restoring the prior receipt
selector; v147 remains the live Site recovery point until a separately
reviewed deployment changes that fact.

## Reproducible environment

Use Python 3.11 or newer; this batch used Python 3.12.3. From the repository root:

```bash
/usr/bin/python3 -m venv .venv
.venv/bin/python tools/ci/install_python_ci.py water-pilot
.venv/bin/python tools/local_data/doctor.py --water-runtime
```

The installer uses existing hash-locked test dependencies and installs local
packages without dependency resolution. A source archive also needs those local
package directories. Root pnpm and the Site's npm lockfile remain separate.
The doctor distinguishes interpreter/package failures, missing release-store
configuration and unestablished service/evidence readiness. It does not start
services or fetch source data.

## Bounded acquisition and replay

The source profile is `configs/domains/hydrology/usgs-water-pilot.json`.
It fixes USGS OGC v1, discharge 00060, stations USGS-06892518 and USGS-07156900,
a maximum 24-hour interval and a two-hour freshness threshold. Transport limits:
25-second requests, five-second connection setup, 180-second total budget,
2 MiB/page, 8 MiB total, twelve pages and bounded retries. Redirects and changed
pagination scope are rejected. A long Retry-After does not cause an early retry.
An HTTP success, empty response or stale latest record never establishes recency.
Before staging, the operator verifies all object digests and enforces twelve
distinct objects, 2 MiB per object, 10 MiB of retained raw objects and a 256 KiB
manifest. The 10 MiB staging ceiling allows the final successful page that
capture retains for quarantine when it crosses the 8 MiB acquisition limit.
Replay rejects manifests with more than twelve page references before reading
objects. Inputs rejected by these preflight checks write no lifecycle objects.

Use an absolute, owner-private external data root (not inside the checkout):

```bash
.venv/bin/python tools/local_data/water_pilot.py --root /absolute/private/KFM-data capture --start 2026-09-29T18:00:00Z --end 2026-09-30T18:00:00Z
.venv/bin/python tools/local_data/water_pilot.py --root /absolute/private/KFM-data replay --capture-id sha256:CAPTURE_DIGEST
.venv/bin/python tools/release/water_snapshot.py --root /absolute/private/KFM-data --candidate-id sha256:CANDIDATE_DIGEST
```

Replace digest placeholders with returned identities. Rerunning replay never
changes captured bytes or invents approvals. Replay requires the manifest's
capture ID to match the requested immutable run path before loading page
objects. A mismatched path is an operation error. Failed validation preserves
raw bytes and writes a quarantine outcome. Valid candidates remain WORK;
source admission, rights and release remain pending. Earlier valid candidates
are not overwritten. Package preparation checks that the requested candidate
digest matches the identity inside the stored WORK candidate before writing a
review package; a mismatch is an operation error. Provider values, units,
qualifiers, provisional status, observation and revision instants, station
geometry, retrieval time, response
headers and content hashes survive normalization. Null remains missing, not zero.
Candidate freshness and coverage count only observations with a non-null flow
value; a timestamp on a null reading cannot make a station recent.
Revision conflicts and malformed completeness claims fail validation.
When station metadata supplies a provider revision time, normalization and
candidate validation require a valid timezone-aware timestamp no later than
that station page's retrieval time. Missing station revision time remains
unknown. Invalid or future revision metadata leaves the capture quarantined
without a WORK candidate.
Station-health receipts distinguish recorded timeout, HTTP and access failures
from a complete capture that fails normalization. Incomplete acquisition without
a more specific recorded cause is `ACQUISITION_ERROR`, not a claimed parse error.
An immutable candidate-store conflict is an operation error, not source quarantine.

The dated acceptance capture returned four HTTP 200 responses and 193 discharge
observations across two stations (96 and 97), for the interval above.
Capture `sha256:c20610cad951f2c830647f6f967572a38c356c353409415baf25640b7f67ec52`;
candidate `sha256:5718217864b88c2551effd7c4653a376a08e93ae952532fb1632d8ed0c8850bc`;
review package `sha256:5dde4c0463677549a5a27f437812e389ca78c2c66dc6d610f59d7d403e710ec5`.
Repeated replay reproduced the candidate. This is a dated capture, not a
continuously current observation claim. Private raw bytes are not committed.
The preserved capture manifest and page hashes bind the 96 and 97 discharge
observations to USGS-06892518 and USGS-07156900, respectively; the review
package names the same stations and remains unreleased.

## Catalog, evidence and release

`tools/catalog_builders/build_catalog.py` produces a non-authoritative preview
from one validated WORK candidate. Its declared profile lives in
`control_plane/readiness/catalog-build-profile.json`. This is not the broad
production catalog builder; the general readiness lane stays HOLD.

`tools/fixtures/regenerate.py` rebuilds the synthetic water conformance package
from pinned input, into an empty isolated directory. It compares exact reviewed
bytes and digests and never overwrites fixtures. The broader fixture lane also
stays HOLD. The prior synthetic hydrology proof remains distinct.

A package contains exactly candidate, catalog, validation and evidence artifact
texts. Artifact hashes cover exact UTF-8 bytes; manifest identity uses RFC 8785.
The earlier candidate identity retains its Python canonical JSON profile.
The package is capped at 8 MiB. Evidence membership, page hashes, validation,
station scope, verification history and correction state are bound together.
Technical verification is not permission to answer.
The local owner staging and activation functions require the operator to supply
`pipelines.domains.hydrology.validate.validate_candidate` as their `validator`
argument at both transitions. They compare the embedded receipt with the fresh
result before changing state. A
resealed but fabricated `PASS` receipt is rejected even when carrier hashes
match. This check applies to local staging and activation; hosted administrative
review and activation remain unimplemented. Other callers of these local
functions must pass that validator explicitly; omitting it is a call error.

Serving also requires separately trusted activation metadata with source,
rights, sensitivity, policy, independent review and release references. Review
and release identities must differ. The manifest cannot self-approve. Real
candidate bundles remain quarantine/review-required and therefore withhold data.
This pilot gate is not the full repository policy engine or a signature-based
release system. Trusted operator-store provisioning remains an explicit
administrative responsibility, not a user-submitted API operation.

## Local API and Site

```bash
KFM_RELEASE_STORE=/absolute/private/KFM-release-serving .venv/bin/kfm-governed-api
```

The private serving store is distinct from the acquisition store. Missing
configuration is permitted for diagnostics; malformed configured storage fails
startup or safely returns unavailable. `/healthz` describes process liveness and
configuration only. `/v1/bootstrap`, `/v1/layers` and `/v1/evidence` return
`{envelope,data}` only when eligible; negative results omit data. The legacy
bootstrap/layers/evidence scaffold routes remain unchanged. The server binds
127.0.0.1:8000, uses bounded sockets, emits safe fixed-field events and suppresses
access logs that would reflect arbitrary request query strings.

The Site equivalents are `/api/governed/v1/{bootstrap,layers,evidence}`.
Existing R2 binding BUCKET reads immutable `governed-water/v1/objects/<hash>.json`;
D1 stores staged metadata and an active pointer. Additive migration
`drizzle/0001_governed_water.sql` activates nothing. Missing tables/buckets,
tampering, missing review, expiry, withdrawal and unresolved evidence withhold
responses. The hosted Site's owner-only audience remains unchanged. No hosted
package, migration or pointer was written by this batch. Hosted staging/owner
review operations remain to be implemented and independently exercised.

The new reviewed-water control keeps provider context separate, preserves
station selection across refresh/failure, shows independent source/retrieval/
review/release times and approval expiry, links evidence and bounds exports.
Serving freshness uses the latest non-null discharge measurement among the
selected stations. Null readings remain in the released record, but do not
make an older measurement current; if none has a value, freshness is `unknown`.
The Site serving boundary rejects impossible calendar dates in release metadata
and package timestamps instead of accepting JavaScript date normalization. The
browser also withholds a displayed release and export when approval expiry is
missing, malformed, or elapsed.
Refresh, evidence denial and expiry clear prior water observations. Browser
fetch, map frame, source coverage and evidence eligibility are distinct states.
A successful build or server HTML check is not rendered-browser acceptance.

## Telemetry, workers and automation

Existing RunReceipt and SourceHealthAssessment contracts carry safe events and
freshness. No prompts, raw observations, private paths, credentials or restricted
coordinates are included in telemetry. The optional operational receipt profile
adds component/source identity, correlation, outcome and safe reason codes.
Health grants no approval. Full OCI trace-to-receipt attestation is not claimed.
Incomplete multi-station captures preserve each station's recorded retrieval
result. A station whose pages succeeded but whose shared candidate did not close
is `SUCCESS` / `UNKNOWN` with `CAPTURE_INCOMPLETE`; an unattempted station is
`NOT_PROBED` / `UNKNOWN`. Neither is a healthy or released observation.
A complete local candidate also requires each captured page to have a matching
successful retrieval attempt for its station and collection, with the attempt
no later than that page's retrieval time. A rehashed manifest with missing,
extra, mis-scoped, or future success attempts is quarantined. This checks
internal capture consistency; it does not authenticate the provider.
Quarantine health counts a prior station success only when the attempt has
`FETCH_SUCCESS`, HTTP 200, and a valid time no later than capture completion.

Ingest/validate/catalog worker entry points delegate to bounded tools. The
hourly `water_job.py` can acquire and prepare candidates only. Tests assert that
it creates no activation database or approval records. Service/timer templates
in `infra/systemd/` are not installed or enabled. Review host paths, ownership,
provider rate limits and service-manager support before enabling them.
Injected job clocks must be timezone-aware; the job converts them to UTC and
rejects invalid clocks before initializing its local candidate store.
The proposed cadence remains: probes 15 minutes, candidate capture hourly,
source drift daily and dependency review weekly. Broad unattended operations
remain held until their actual deployed checks and recovery are proven.

## Validation and recovery

```bash
.venv/bin/python -m pytest -q tests/connectors/usgs/water_data tests/domains/hydrology/test_usgs_water_normalizer.py tests/packages/release tests/packages/connectors_core apps/governed-api/tests tests/tools/test_water_job.py
.venv/bin/python tools/fixtures/regenerate.py
.venv/bin/python tools/qa/completion_queue.py --check
.venv/bin/python tools/qa/site_mirror.py --check
.venv/bin/python tools/qa/scaffold_inventory.py --check
```

Synthetic tests stage without activation, reject an unreviewed package, activate
two synthetic packages through compare-and-swap and restore the first with the
same evidence response. Withdrawal/tampering/expiry/missing review tests fail
closed. These are local rehearsals, not proof of real release approval or hosted
rollback. Browser acceptance remains blocked by the unavailable admin security
check; no bypass or substitute visual claim was made.

Original monorepo unfinished changes and separate Site history were preserved
before implementation. Roll back authoring by abandoning/reverting the isolated
candidate commits. Do not reset the active checkout. Preserve immutable raw,
validation and historical receipt bytes. A deployed rollback requires exact
previous package/application identities, renewed eligibility and separately
recorded operator action. Never activate a withdrawn package to make a test pass.

## Releasing the discharge layer

**Admitted 2026-10-10 by @bartytime4life.** The
[USGS source descriptor](../../data/registry/sources/hydrology/usgs_nwis.yaml)
admits provisional discharge (00060) at USGS-06892518 and USGS-07156900 as U.S.
public domain, provisional data subject to revision. Under
[ADR-0044](../adr/ADR-0044-owner-self-release-for-admitted-public-water-data.md)
the owner may review and release a package alone, but only when every bundle is
public and carries that admitted license. Anything else still needs a second
reviewer.

Run these on the computer that holds the private data root. Live capture needs
network access to `api.waterdata.usgs.gov`.

```bash
ROOT=/absolute/private/KFM-data
# 1. Capture, replay and prepare with the admitted license.
.venv/bin/python tools/local_data/water_pilot.py --root $ROOT capture --start START --end END
.venv/bin/python tools/local_data/water_pilot.py --root $ROOT replay --capture-id sha256:CAPTURE
.venv/bin/python tools/release/water_snapshot.py --root $ROOT --candidate-id sha256:CANDIDATE --admitted-source
# 2. Write the release decision. It is written only if the serving gate answers.
.venv/bin/python tools/release/water_release.py decide --root $ROOT --package-id sha256:PACKAGE \
  --reviewer @bartytime4life --releaser @bartytime4life --valid-days 7
```

A package prepared without `--admitted-source` keeps the rights hold, and
`decide` refuses it with `INDEPENDENT_REVIEW_REQUIRED`. Use `--rollback-target`
with the currently active package when you prepare a replacement.

**Local serving.** Stage and activate into a private serving store, then start
the governed API against it:

```bash
STORE=/absolute/private/KFM-release-serving
.venv/bin/python tools/release/water_release.py stage --root $ROOT --store $STORE --package-id sha256:PACKAGE --actor @bartytime4life
.venv/bin/python tools/release/water_release.py activate --root $ROOT --store $STORE --decision release/decisions/hydrology/HASH/STAMP.json --expected-active none
KFM_RELEASE_STORE=$STORE .venv/bin/kfm-governed-api   # /v1/layers now answers
```

**Hosted Site.** One-time setup in the Site's runtime settings:
`KFM_WATER_WORKER_TOKEN` (32+ random characters, staging only) and
`KFM_WATER_OWNER_IDS` or `KFM_WATER_OWNER_EMAILS` (who may activate). Confirm the
deployed Site has applied `drizzle/0001_governed_water.sql`. Then:

```bash
KFM_WATER_WORKER_TOKEN=... KFM_SITES_BYPASS_TOKEN=... \
  .venv/bin/python tools/release/water_release.py stage-hosted --root $ROOT --package-id sha256:PACKAGE \
  --site-url https://kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site
```

Staging stores the package and cannot activate it. Open `/governed/water-release`
on the Site, paste the decision file, and press **Activate package**. The page
shows the active and previous package; **Withdraw active package** stops serving
at once, and **Roll back to previous** reactivates the earlier package with its
decision. Activation is compare-and-swap: if the active package changed since
the page loaded, it refuses with `ACTIVATION_CONFLICT`.

Decisions expire (7 days by default, 30 at most). An expired decision stops the
layer from answering; write a new decision and activate again.

Validation: `tests/packages/release/test_water_self_release.py` (gate and
admission), `tests/tools/test_water_release.py` (decide, stage, activate,
loopback `/v1/layers`, hosted staging request) and the Site's
`tests/governed-water-admin.test.mjs` (staging, compare-and-swap activation,
withdrawal and route authorization against the real D1 migration on SQLite).
Hosted staging and activation have not yet been run against the deployed Site.

## Completion queue and next gates

The existing verification backlog accounts for the original 949 markers across
747 paths, with baseline evidence, priority, owning-root role, next change,
acceptance and rollback. Inventory accounting is not implementation completion.
The scaffold baseline decreases from 949 to 925 markers across 732 paths in this batch, with 24 marker resolutions across 15 implemented artifacts and no new markers. The topology baseline strictly removes three scaffold-only directory members; its 115 warning groups remain, with no new drift or invariant failure.

Remaining first-milestone gates: source admission/rights/sensitivity review;
independent release authority and authenticated hosted staging/review/activation;
D1/R2 integration tests; rendered local/hosted selection-to-evidence acceptance;
production telemetry retention and recovery; host adoption of timers; hosted
rollback. After these gates, expand Census, PRISM/wind, terrain/imagery/soil,
weather/hazards and other domains through the same governed workflow.

## CI integration and historical receipts

Legacy scaffold API imports stay independent of optional water packages. The
water and domain hydrology lanes install the `water-pilot` profile and execute
the new normalization/denial tests. The OPA and synthetic proof guards recognize
this bounded implementation without granting broader policy or release readiness.
The NWIS v0 authoring receipt is checked against its original ancestor
`597897584478820f051388bc2a7c734429be7a16`; current v1 tests run separately.
The dependency-migration replay reads both ledger and workflow bytes from its
pinned historical revision. Current workflow exceptions remain hash-bound to the
current ledger; historical receipt files are preserved.

The source-neutral bounded curl transport now owns temporary network-response
files under `packages/connectors-core`. The USGS connector still owns its exact
provider profile, request scope, pagination and capture. This follows the
existing shared-transport responsibility and adds no lifecycle write authority.

## Repository selection-generation repair — 2026-10-04

At `main@d5d4337e8ecfae45e32a195abcb6f1e84f92e642`, the exact-head
PR #4878 P2 still matched the export handler despite the resolved review thread.
An export from A could survive A→B→A because only its final station ID was
checked. The repository repair increments a generation for each station change
through the shared dropdown/map handler and captures it when export begins.
A changed generation withholds the download after the sequential layer and
evidence requests. Reselecting the same station does not invalidate an export.

The component-handler regressions fail on unrepaired main for A→B→A during
either request and pass with the repair; unchanged selection still exports.
Validation passed 17 focused governed-water tests, the production build and
352 Site tests on Node 22.13.1, TypeScript, lint (0 errors, 39 existing warnings),
280 water/mirror tests, isolated synthetic fixture regeneration, and 28 workflow
security tests plus the security ratchet. The initial Node 24 run rejected the
runtime's required Node 22 version; the supported-version rerun passed.

The [overlay receipt](../../data/receipts/generated/site-v140-water-selection-overlay-20261004.json)
preserves the historical v140 receipt and records one changed source file plus
one repository-only regression file. It verifies 337 repository paths against
recorded digests; it does not assert byte parity for the two overlays with saved
Site v140. No Site synchronization or deployment occurred in this repair.
New-head hosted checks and independent review remain separate. Existing
dependency-audit holds remain open. Water admission, release activation, Site
deployment, hosted equivalence, release, publication, rendered-browser
acceptance, and owner acceptance are not established by these tests.
