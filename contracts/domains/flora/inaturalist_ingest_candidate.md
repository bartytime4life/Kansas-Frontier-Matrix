<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/flora/inaturalist-ingest-candidate
title: iNaturalist Flora Ingest Candidate
type: semantic-contract
version: v0.1.0
status: proposed; fixture-first; no-network; non-writing
owners: OWNER_TBD — Flora steward · iNaturalist source steward · Rights and sensitivity reviewers · Validation steward
created: 2026-11-19
updated: 2026-11-19
policy_label: public-metadata; private-source-candidates; no-public-coordinates
owning_root: contracts/
responsibility: define a private held plant-query capture projection
truth_posture: CONFIRMED bounded supplied-page replay; PROPOSED candidate profile; NEEDS VERIFICATION cross-domain source admission, human review and downstream use
[/KFM_META_BLOCK_V2] -->

# iNaturalist Flora Ingest Candidate

`INaturalistFloraIngestCandidate` is a private held source-edge projection of the
existing observation parser and cursor reconciler. It is not a FloraOccurrence,
Darwin Core normalization, KFM taxonomy determination, sensitivity assessment,
redaction receipt, source admission or public-safe artifact.

## Scope and placement

This profile requires exactly the existing Kansas context bbox and `taxon_id=47126`
(Plantae), ascending observation-ID cursor order, and no grade, date or place filter.
The provider's [search guidance](https://help.inaturalist.org/en/support/solutions/articles/151000170738-how-to-use-inaturalist-search-urls)
identifies that plant taxon ID. The bbox is context, not a legal Kansas boundary.
A request filter is not proof that every supplied record has plant lineage.

A record with taxon ID 47126 or a well-formed `ancestor_ids` containing it receives
`SOURCE_PLANT_LINEAGE`; otherwise its Flora check is `UNVERIFIED` and quarantined.
This checks supplied source assertions only; names, lineage, quality grades and
source taxon IDs are not reconciled against a KFM taxonomic authority. Unknown
lineage is retained, never dropped or inferred from a name.

The existing [Fauna source template](../../../data/registry/fauna/sources/inaturalist.yaml)
is referenced without duplication or amendment. Its role, rights and sensitivity
remain unresolved; Flora use adds `CROSS_DOMAIN_USE_UNREVIEWED`. ADR-0029 supports
the established source-edge contract/schema/pipeline homes only. It does not admit
this source, approve cross-domain use or establish botanical meaning.

## Input and bounds

Input JSON contains only `pages`. Each page contains exactly `source_url`, actual
integer HTTP `status` 200, `retrieved_at`, and original UTF-8 JSON `body` text.
Requests must exactly match the fixed planner profile. Nothing is fetched, followed,
scheduled or written. Non-200 and malformed pages reject the whole capture; no
partial success or row truncation is returned.

Limits: 2 MiB envelope, 256 KiB per source body, 1 MiB combined source bodies,
16 pages, 64 records requested per page, 256 records in total, reported count at
most 1,000,000, container nesting depth 32 and canonical output at most 8 MiB.
JSON must have unique keys and finite numbers. Duplicate request URLs or repeated
observation IDs are refused. Page-size mixtures and noncanonical or out-of-profile
queries are refused. Present ancestry arrays contain at most 64 positive integer
IDs; malformed arrays fail instead of guessing their meaning.

Pages sort by cursor independently of input order. Capture times normalize to UTC
with fractional seconds retained and must be nondecreasing in that order. Present
`updated_at` must be an explicit zoned timestamp no later than capture. Present
`observed_on` must be a valid complete calendar date no later than the UTC capture
date. Null source dates remain null; no timestamp fallback or temporal inference
is performed. These are narrow profile constraints, not changes to provider data.

## Walk conformance and routing

The existing reconciler requires a start cursor of zero, unbroken cursor links,
consistent remaining counts and a short terminal page. Exact page-size multiples
require an empty final page. Gaps, missing start/end, early end and count drift
remain `INCOMPLETE_CAPTURE`. Count consistency cannot prove an unchanged provider
snapshot. Coverage stays `NOT_ESTABLISHED`; empty captures do not establish plant
absence, abundance, survey effort or complete geographic coverage.

Existing source rights, attribution, grade, captive/cultivated and geoprivacy
flags survive unchanged. Unknown rights or restricted precision keep their source
quarantine routes. Flora checks can add quarantine for unverified plant lineage.
All final candidates are `HOLD`, including internally consistent walks and open,
research-grade, recognized-license records. Every authority flag is false.

## Minimized replay and original-byte proof

Before a candidate is returned, top-level incidental response fields are discarded
and every nested `user` dictionary is projected to scalar ID/login attribution.
Unexpected user shapes and non-scalar ID/login values reject the capture. Returned
page snapshots contain only `total_results`, `per_page` and minimized records.
Unknown record fields remain private and source-faithful. This is targeted user
minimization, not comprehensive personal-data redaction: text, media references,
source-supplied private coordinates and unknown fields can still be sensitive.

Original source bytes and minimized replay bytes have **separate SHA-256 digests
and lengths**. Original bodies are never returned in the candidate. Candidate ID
binds the cursor-ordered URL, original digest and original length, excluding
capture time. `spec_hash` binds the full candidate except itself. No digest is
provider authentication or evidence closure; no persistent availability is claimed.

`validate_candidate(candidate)` validates the closed schema, canonical minimized
body identity, replayed records/Flora checks, cursor result and denied authorities.
It cannot verify a discarded original preimage. Original digests remain lineage
assertions in that mode. Pass `original_capture=raw_bytes` to additionally rebuild
from and compare every original supplied page. `prepare_capture` always performs
this stronger check before returning. Both modes remain internal consistency
checks, not validation that the caller's bytes came from iNaturalist.

Source geoprivacy is never repaired, deobscured, recentered or joined to infer a
location. Obscured coordinates remain randomized source points; private or missing
coordinates remain distinct. Candidate data requires private handling. The fixed
CLI emits aggregate counts, finite reasons and a result digest, with no IDs,
logins, taxon names, URLs, source text or geometry. It writes no files.

## Validation and correction

The [closed schema](../../../schemas/contracts/v1/domains/flora/inaturalist_ingest_candidate.schema.json)
and [runbook](../../../docs/runbooks/inaturalist-fixture-ingest.md) bind sealed
synthetic complete/count-drift/empty cases and Python 3.11/3.12 offline CI.
Source regression tests also preserve finite malformed-quality-grade errors and
subsecond capture time. Revert the bounded bundle through review, preserving
historical receipts and source records. No migration or provider change occurs.
