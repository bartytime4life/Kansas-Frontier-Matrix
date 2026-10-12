# Owner acquisition receipt projection

`/acquisition` inspects the local worker's candidate-only inventory. The current
cache ceiling is 500 GB, exactly 500,000,000,000 bytes (about 465.7 GiB).
The owner selects local storage for Kansas full-history downloads under the
existing `Projects/KFM-data` data root. Provider originals remain remotely
available; protected originals, evidence and backups remain separate from the
replaceable cache. Global selections and their volumes are the owner's choice.
Historical receipts retain their captured storage destinations; the UI does not
rewrite provider-hosted selections into local completion claims.
Receipts describe a captured worker
state; importing or saving them does not start transfers, verify provider bytes,
admit a source, approve a dataset, or release evidence.

Historical receipts retain their recorded positive byte budget up to the current
ceiling, including earlier 100 GB snapshots. Their limits are never replaced with
500 GB during parsing or saving. The UI distinguishes the current ceiling from
the recorded snapshot budget; every selected file bound must fit the recorded
budget. A policy increase does not enlarge a historical file selection or rewrite
stored receipt bytes. Observed use above a receipt's own budget remains visible.

The Site parser accepts the worker's nullable reason and rights link, preserving
unknown expected sizes and an optional selected maximum separately. A completed
job requires a reported verified checksum, positive captured bytes, local storage,
and either its exact expected byte count or a selected maximum that contains its
actual size. Protection remains visible. An additive `captured` state records an owner-acquired
protected candidate when a provider supplies no digest. It requires
`checksum_basis: "capture-readback"`, `provider_digest: null`, a lowercase local
SHA-256, `checksum_verified: false`, and positive `bytes_received` equal to
`downloaded_bytes`, within the expected size or selected maximum. Its storage
must be `local-protected-candidate`, with `protected: true` and
`intended_destination: "local-pc"`. It does not become ordinary `complete`, enter
replaceable-cache accounting, or grant review/admission. The UI says “Stored-file
hash checked; provider checksum unavailable” and labels its hash as a stored-file
digest. Optional fields are omitted from historical projections when absent, so
old receipt digests retain their meaning. These checks validate the receipt's
internal consistency, not the referenced payload. Uninspected or legacy cache
snapshots display unknown use and available capacity; zero in an offline plan is
not interpreted as measured empty space. Temporary and replaceable completed
bytes must be disjoint portions of reported total use, which may include other
metadata and protected files.

Local JSON reads are capped at 1 MiB. New inventory selections retire pending
saved-state requests and older local reads. Saving disables inventory selection,
retains the preview on failure, and verifies the returned canonical inventory and
SHA-256 before marking it saved. A malformed saved response is an error, distinct
from an explicitly empty inventory.

`/api/acquisition` requires the existing owner identity on reads and writes. POST
also requires same-origin JSON, bounded input, and valid inventory. Each import
creates a hash-addressed receipt under `acquisition/v1/receipts/`. The route reads
it back before writing `acquisition/v1/latest.json`. This pointer has exactly the
schema, immutable receipt key, and digest fields; GET bounds it to 1,000 bytes and
checks the receipt size, SHA-256, and inventory contract. No history listing is
needed. Concurrent imports use the last verified pointer write as the active
snapshot, retaining previous receipt objects. No source URL in the receipt is
fetched by this route.

The terrain selector separately previews a local `discovery.json`, bounded to
1 MiB and projected through `parseTerrainDiscovery`. Persistence rejects invalid
or duplicate work-unit identities and mismatched record counts; only supported
provenance fields survive the projection. Unsupported CRS and unknown dates remain
unknown. `TerrainProvenancePanel` displays this candidate metadata. A separate save
button writes it to `/api/acquisition/terrain` through the same owner, origin,
size, digest, and readback gates. Its fixed `acquisition/terrain/v1/` namespace
cannot point into inventory receipts. The terrain and inventory snapshots remain
independent; saving one cannot replace the other. Local previews are explicitly
not uploaded until their own save button succeeds. Separate selection epochs
prevent delayed terrain reads from replacing a newer selection. No point clouds
are fetched and no metadata is made publicly accessible by these routes.

Application behavior and projection types remain in the existing `app/` root,
regressions in `tests/`, and this note in `docs/`, following the adopted Directory
Rules and ADR-0029 responsibilities. This creates no canonical schema, source
registry, acquisition worker, or release authority. Rollback restores the prior
Site application; private receipt objects can remain preserved for later review.

`tests/acquisition-integrity.test.mjs` covers invalid calendar dates, impossible
cache totals, nullable worker fields, bounded unknown-size completion, uninspected
cache state, stale local reads, malformed responses, save identity, authentication,
origin checks, aborted imports, corrupt pointers, failed readback, concurrent
imports, histories longer than 1,000 receipts, terrain projection stability,
terrain owner/origin checks, and independent storage namespaces. Browser acceptance and hosted
owner access are separate checks, not established by these unit tests.
