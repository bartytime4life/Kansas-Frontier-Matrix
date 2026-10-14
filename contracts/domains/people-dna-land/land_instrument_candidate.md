<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domains/people-dna-land/land-instrument-candidate
title: Land instrument candidate v1
type: contract
version: v1
status: draft
owners: ["@bartytime4life"]
created: 2026-10-13
updated: 2026-10-13
policy_label: public
owning_root: contracts/
responsibility: Human semantics for the closed private land-instrument candidate; machine validation is owned by the linked schema.
truth_posture: "CONFIRMED implemented candidate contract; review and release remain PENDING."
related: [schemas/contracts/v1/domains/people-dna-land/land_instrument_candidate.schema.json, docs/runbooks/land-records-ingest.md]
tags: [land-records, candidate, evidence, privacy]
[/KFM_META_BLOCK_V2] -->

# Land instrument candidate v1

An unreleased instrument/index assertion with a source-local identity, dates,
parties, legal description, financial role and evidence reference. This
contract does not redefine the proposed land-ownership assertion scaffold.

Machine home: [land_instrument_candidate.schema.json](../../../schemas/contracts/v1/domains/people-dna-land/land_instrument_candidate.schema.json).
Operating home: [land intake runbook](../../../docs/runbooks/land-records-ingest.md).

- `source_record_id` identifies an instrument within its source. GLO captured
  CDI cards use a flagged composite index key because a unique instrument ID
  was not captured. No cross-source person/parcel identity is inferred.
- `record_digest` binds all normalized content except the digest and derived
  `evidence_ref`. Capture times and raw page bytes belong to the linked bundle;
  unchanged content across another page/capture retains the record digest.
- `event_date` is the source instrument/index date, `recording_date` is separate
  and nullable. Neither establishes an ownership interval. Full historic county
  boundary reconciliation is not implemented.
- `transaction_status` is `RECORDED`, `ISSUED`, `PROPOSED`, `CASE_ACTION` or
  `UNKNOWN`. All records have `sale_completion=NOT_ESTABLISHED` and
  `title_claim=NOT_ESTABLISHED`. A proposed sale or MLRS case cannot be normalized
  as a completed sale. Mineral leases and assessor/tax values are excluded.
- Amounts are exact decimal strings with `USD` and one of `sale_price`,
  `consideration`, `nominal_consideration`, `recorded_principal`,
  `appraised_value`, `minimum_bid`. The role must be explicitly supplied; it is
  not upgraded to a verified sale price. Source absent amount is `null`, never
  zero. Dollar values are historical source values, with no inflation adjustment.
- Acreage is a nullable positive decimal string. A PLSS legal description
  remains source text. `geometry=null`, `geometry_role=UNLOCATED`; no synthetic
  centroid, parcel boundary, current address or inferred acreage is produced.
- Party labels retain the source wording. `living_status=UNKNOWN` even for
  old documents. No genealogical or DNA join, owner dossier, person search or
  legal title assertion is implemented. These fields are private review only.
- Rights, source admission and review are `PENDING`; sensitivity is
  `REVIEW_REQUIRED`; release is `UNRELEASED`. A self-hashed candidate cannot
  change those values: the writer must replay normalization against captured
  bytes, and no public projection/release writer exists.
- `evidence_ref` resolves only in the private administrative runtime to
  `kfm.land-evidence-bundle-candidate/v1` objects with member hashes, source URL,
  capture time/method and card/row locators. A rendered DOM capture is a
  derivative of an index, not a fetched patent image or HTTP response. CSV
  mapping/transcription is an interpretation awaiting review.
- Capture withdrawal excludes its occurrences from ordinary private review
  queries and evidence resolution. Original records, objects and receipts
  remain immutable. A later import does not overwrite another version.
