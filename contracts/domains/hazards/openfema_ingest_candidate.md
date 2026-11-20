<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/hazards/openfema-ingest-candidate
title: OpenFEMA Declarations Ingest Candidate
type: semantic-contract
version: v0.1.0
status: proposed; fixture-first; no-network; non-writing
owners: OWNER_TBD — Hazards steward · FEMA source steward · Validation steward
created: 2026-11-19
updated: 2026-11-19
policy_label: public-metadata; private-administrative-context; not-for-life-safety; no-eligibility-authority
owning_root: contracts/
responsibility: define a held administrative source-capture projection for OpenFEMA declarations
truth_posture: CONFIRMED bounded supplied-page replay; PROPOSED candidate profile; NEEDS VERIFICATION human review, source admission and any downstream use
[/KFM_META_BLOCK_V2] -->

# OpenFEMA declarations ingest candidate

`OpenFemaDeclarationsIngestCandidate` is a proposed private held projection of the
existing FEMA `CaptureCandidate`, for exactly Disaster Declarations Summaries v2.
It is administrative source context, never an observed hazard, damage footprint,
aid eligibility determination, public map product, emergency advice or release.
A designated jurisdiction is not a hazard footprint. Other OpenFEMA tables and
NFHL products are outside this profile.

This candidate uses established Hazards ingest homes under ADR-0029. The existing
[domain source descriptor](../../../data/registry/hazards/sources/fema_disaster_declarations.yaml)
remains proposed and unresolved. FEMA connector family settings do not admit the
domain source, its rights/sensitivity posture or any downstream use.

## Supplied capture and budgets

Input is JSON containing `pages`, each with exactly `source_url`, `status`,
`retrieved_at` and original JSON `body` text. Only HTTP 200 is accepted. URLs must
exactly match the existing Kansas counted keyset planner, with optional half-open
declaration-date bounds. No URL is fetched and no cursor is followed by this code.

The envelope is limited to 2 MiB; each body to 256 KiB; combined bodies to 1 MiB;
page count to 16; requested page size to 64; total records to 256; reported counts
to 1,000,000; canonical output to 8 MiB. Duplicate/nonfinite/deep JSON, duplicate
page requests, noncanonical queries, invalid metadata or unsorted page records
fail closed without truncation. A missing page or drifting count is preserved
as `INCOMPLETE_CAPTURE`, not turned into success.

Input page order is immaterial: cursor order defines deterministic output.
Capture times normalize to UTC and must be nondecreasing in that order. Declared
and refreshed record times, and provider run time when present, cannot exceed
page capture time in this profile. Subseconds are retained. Declaration, incident
begin/end, closeout, source refresh, provider run and KFM capture stay distinct.
Unknown incident ends remain null, with an explicit flag.

## Walk conformance versus completeness

The existing reconciler requires an uncursored first page, an unbroken cursor
chain, consistent remaining counts, and a short terminal page. An exact multiple
of page size therefore still requires its empty terminal page. Count drift,
missing start/end, early end, duplicates and order problems remain finite reasons.
Structurally malformed pages are rejected; semantically questionable records,
such as inverted incident times, retain explicit quarantine routes and snapshots.

`CAPTURE_CANDIDATE` proves only internal conformance of the supplied reported
walk. Counts alone do not prove a stable provider snapshot: content may change
without changing counts. Coverage stays `NOT_ESTABLISHED`. Empty captures never
prove no hazards, no declarations outside the query, complete geographic coverage
or any person's eligibility. Live keyset support and source activation remain
unverified.

## Identity, privacy and denial

Each original body has an exact byte digest and length. Candidate identity hashes
the canonical cursor-ordered list of URL, body digest and length. Capture times
are excluded from this byte identity; `spec_hash` binds the complete candidate
except itself, including source snapshots and normalized capture times.
Provider record `hash` remains a separate source field, not an authenticated byte
digest. Raw page bodies and canonical record snapshots remain private in memory;
no persistent capture availability or evidence closure is claimed.

Every final route is `HOLD`. Source admission, descriptor, rights and sensitivity
remain unresolved. All ten authority flags are false, including eligibility and
life-safety authority. CLI output contains only finite aggregate outcomes, counts,
reason codes and result digest, with no titles, record IDs, areas, source URLs,
program details or source body text. No file or lifecycle write occurs.

## Validation and rollback

The [closed schema](../../../schemas/contracts/v1/domains/hazards/openfema_ingest_candidate.schema.json)
checks shape and denied authority. Runtime validation fully rebuilds the candidate
from its original page snapshots; changing a count, role, route, digest or record
projection and merely recomputing a hash cannot make it conformant. This validates
internal consistency, not truth or source admission.

The [runbook](../../../docs/runbooks/openfema-fixture-ingest.md) binds synthetic
complete, count-drift and empty walks, source parser regressions and no-network CI.
Revert this bounded source/pipeline bundle through review. Preserve older receipts,
source records and any captured evidence; no provider or persistent-data migration
is introduced.
