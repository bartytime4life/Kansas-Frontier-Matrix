# Explorer card pipelines

The registry covers the current 22 visual welcome topics and six map recipes. It references the existing official-context registry and source/domain
lanes, specialty controls, calculated daylight and the permitted knowledge search
index; it is not a source descriptor, admission decision or publication authority.
The human-readable inventory is [the generated map](explorer-card-pipeline-map.md).

## See the coverage

Open `/pipelines` in the Explorer, or use **Card pipelines & source coverage**
from the welcome window. Switch between current welcome topics and map recipes.
The read-only `GET /api/pipeline/v1/cards` endpoint returns bounded public
metadata. Query parameters are rejected; writes are not supported. It works
before MySQL/publication setup and retains the registry when release checks fail.

The public view checks only approved hosted USGS streamflow, NWS alerts and USGS earthquake snapshots. Existing tile
and request-based display sources remain **not checked here**; their live map
controls own availability. Proposed lanes remain explicit coverage gaps.
Required-source failures produce partial coverage when another required source
is usable. Optional layers never establish complete domain coverage. Observation
times stay separate from snapshot retrieval times. Neither metadata nor opening
a card makes an AI request, downloads a candidate source or publishes anything.

## Private operations

Run the following from the standalone GoDaddy composition, using Node 22.13+:

```sh
node scripts/pc-pipeline/health.mjs status /absolute/config.json /absolute/run-directory
node scripts/card-pipeline-map.mjs > docs/explorer-card-pipeline-map.md
```

`health.mjs status` opens SQLite read-only and reports storage qualification,
last attempts/completions, retries/exhaustion, next eligible runs, intake counts,
and working backup/restore state. It neither initializes a missing journal nor
uploads anything. Old journal rows retain null clocks; the hour bucket is not
presented as a capture timestamp. The first normal tick adds nullable clock
columns without deleting or rewriting existing rows. Capture time is recorded
separately from publication completion, including when transfer later fails.

The existing kernel-locked capture wrapper can invoke:

```sh
node scripts/pc-pipeline/capture.mjs /absolute/config.json /absolute/run-directory
```

It performs the existing tick and then atomically writes
`data/work/pipeline-health.json` in the qualified private store. Failed storage
qualification never writes a fallback location. The intake desk reads this
bounded report through its session-authenticated, same-origin-only
`GET /api/pipeline-health` route. Reports older than 15 minutes are visibly stale.
The catalog-only imported library does not expose this route. A diagnostic-report
failure is logged separately and cannot turn a failed capture into success.

The report distinguishes receipt-file modification time from a backup operation
clock missing in older receipts. A restore of an older inventory is not described
as verification of the newest backup. Working-store coverage does not establish
a complete backup of the preserved imported archive.

## Configuration and source expansion

Existing v1 configurations remain supported. An optional v2 uses `pipelines`
instead of `sources`:

```json
{
  "format": "kfm-pc-pipeline-config-v2",
  "root": "/qualified/private/store",
  "mount": "/qualified",
  "device": "REPLACE_WITH_QUALIFIED_DEVICE",
  "storeId": "REPLACE_WITH_EXISTING_STORE_ID",
  "approvalDirectory": "/private/approvals",
  "publish": false,
  "remoteMode": "connection-only",
  "pipelines": [
    { "sourceId": "usgs-streamflow", "enabled": true },
    { "sourceId": "nws-alerts", "enabled": true }
  ]
}
```

This example is not an initialized operational config. Keep the existing mount,
device and store marker; never invent replacements from this example.
Both versions support the three implemented capture adapters. The installed PC
configuration still selects streamflow and alerts only; earthquakes remain unscheduled. Candidate registry
IDs, arbitrary URLs, custom request limits and duplicate adapters are rejected.
No live config migration is required for the registry or private health report.
Adapters remain hourly and the existing timer checks every five minutes.

Before extending the capture allowlist, qualify the exact provider product,
source descriptor, rights, sensitivity, bounds, schema, source-shaped fixtures,
normalizer and negative tests. Before extending publication, qualify the receiver,
serving validator and source-specific approval profile. Proposed registry metadata
alone satisfies none of these steps. Use the generated domain queue to track
soil/crops/resources, ecology/outdoors, heritage, infrastructure, and public
records/economic expansions in that order.

`health.mjs backfill-plan SOURCE FROM THROUGH` validates an hour-aligned,
non-future window of at most 31 days. The current active-alert and latest-water
products cannot reconstruct missed snapshots, so the plan explicitly holds
execution pending a qualified historical product. It performs no network request
and does not fabricate completed capture slots.

## Publication and recovery

Publication stays disabled until owner review. The existing Ed25519 profiles,
HMAC transport, hash verification, expected-active conflict checks, approval
expiry/revocation, withdrawal and rollback remain authoritative. The new public
endpoint checks the existing serving gate per source and drops payloads and
private diagnostics from its response. Preview/disabled environments do not
connect to the release store.

Review material is in [the USGS/NWS packet](pipeline-source-review.md). Do not
sign placeholder references or enable publication to test the new coverage view.
A clean synthetic publication/rollback rehearsal is covered by the existing
pipeline tests; actual hosted acceptance remains separate.

Pause the four user timers and wait on their shared kernel lock before installing
worker changes, preserve local edits, test, then restore the timers. The current
`dev` deployment remains a user-level installation; do not run the system
installer or switch to `/srv` as part of this update. The test PC `devil`, inference
services, DNS and the preserved Sites app have no new role.


## Candidate validation and offline corrections

A successful capture is separate from candidate validation. The worker now
validates its normalized output before recording a completed product. Private
health checks also validate the latest stored candidate and its content hash;
invalid older candidates produce a visible hold without becoming public data.
USGS scalar and array qualifiers are preserved as bounded arrays of up to 16
strings. Invalid qualifier shapes are rejected rather than changed to null.

`node scripts/pc-pipeline/revalidate.mjs audit CONFIG` audits at most 1,000 private
job candidates, with a 512 MiB total read budget. Under the existing shared
kernel lock, `repair CONFIG` can rebuild invalid candidates from their exact
preserved raw bytes and matching immutable capture receipts. Repair requires
publication disabled and connection-only mode. It writes a new content-addressed
candidate and correction receipt, then conditionally changes only the unpublished
job pointer. Original raw bytes, old candidate bytes, retrieval times and prior
receipts remain intact. Published releases and active leases are excluded.
Missing or ambiguous receipts, corrupt bytes and changed jobs remain held.
A changed normalizer changes the recipe digest and requires a new source review.

## Reconciliation with the current repository

The integration candidate starts from hosted branch `a0-hosted-ai-web-20261017`
at `8dcc13cf95`, including the October 29 Flora and crop-history work. The live build readback was
`5baefffe96`. The former 22-question guide was removed upstream; the registry
now follows the current 22 topics and six recipes. Category starter layers,
optional context and every category-specific map control are included directly
from `CATEGORY_MAPS`, alongside the official/specialty registries. This includes
Flora's land-cover, plant-record and crop controls. Their display availability
is checked in their own controls; no scheduled capture is implied.

The newer earthquake adapter, manual county-history path, storage priorities,
one-publication budget, outage deferrals and installed-kit dependencies are
preserved. The PC's installed two-source configuration and runtime remain on
the previously validated local version until a separate controlled installation.
Do not copy the entire hosted branch over the running PC checkout.

Next implementation order:

1. Review and merge the hosted coverage candidate into the verified GoDaddy
   source branch; deploy it to the same app and check `/api/build`, `/pipelines`
   and `/api/pipeline/v1/cards`. Expect 28 cards and setup-pending while disabled.
2. Review the separate main-repository private-health candidate. Keep the
   imported library catalog-only and its existing loopback/session boundaries.
3. Before a PC runtime upgrade, pause timers, preserve the installed code and
   config, take a fresh working backup and verified restore, then hold the shared
   lock. Review the reconciled recipe against preserved raw bytes; existing
   source profiles cannot authorize the changed recipe. Resume and verify both
   originally configured sources and actual attempt/capture/completion clocks.
4. Qualify earthquakes separately before adding it to this PC's configuration.
   Its existing adapter is implementation evidence, not permission to schedule
   or publish it. County history remains manual and unscheduled.
5. Use current Aviation/Flora display controls as references for bounded product
   qualification. Keep Fauna's landscape and separate Observatory context
   distinct from reviewed occurrences. Government/public-safety cards retain
   their explicit source and personal-location limits. Proposed domain jobs
   remain disabled until product-specific validation and review are complete.
6. Complete the independent full-archive backup and attended reboot acceptance.
   Hosted storage/TLS, profile approval, activation, withdrawal and rollback
   acceptance remain prerequisites for routine publication.
