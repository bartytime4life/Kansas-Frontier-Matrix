# Water pilot: acquisition, candidate review and governed reads

Status: implemented delivery candidate, pending independent review and deployment.
No real water source was admitted, released, activated or published by this batch.
The first milestone remains open until the real reviewed package completes the
local browser journey and private Site acceptance/rollback gates.

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

Use an absolute, owner-private external data root (not inside the checkout):

```bash
.venv/bin/python tools/local_data/water_pilot.py --root /absolute/private/KFM-data capture --start 2026-09-29T18:00:00Z --end 2026-09-30T18:00:00Z
.venv/bin/python tools/local_data/water_pilot.py --root /absolute/private/KFM-data replay --capture-id sha256:CAPTURE_DIGEST
.venv/bin/python tools/release/water_snapshot.py --root /absolute/private/KFM-data --candidate-id sha256:CANDIDATE_DIGEST
```

Replace digest placeholders with returned identities. Rerunning replay never
changes captured bytes or invents approvals. Failed validation preserves raw
bytes and writes a quarantine outcome. Valid candidates remain WORK;
source admission, rights and release remain pending. Earlier valid candidates
are not overwritten. Provider values, units, qualifiers, provisional status,
observation and revision instants, station geometry, retrieval time, response
headers and content hashes survive normalization. Null remains missing, not zero.
Candidate freshness and coverage count only observations with a non-null flow
value; a timestamp on a null reading cannot make a station recent.
Revision conflicts and malformed completeness claims fail validation.
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
