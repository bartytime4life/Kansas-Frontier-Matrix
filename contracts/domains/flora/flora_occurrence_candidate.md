<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domains/flora/flora-occurrence-candidate
title: FloraOccurrenceCandidate Contract
type: semantic-contract; flora; occurrence; Darwin-Core; normalization
version: v0.1.0
status: draft; PROPOSED; fixture-first; no-network; WORK-only
owners: OWNER_TBD — Flora steward · Source steward · Contract steward · Schema steward · Validation steward
created: 2026-08-05
updated: 2026-08-05
policy_label: public; contracts; flora; occurrence-candidate; no-publication-authority
related:
  - ./flora_occurrence.md
  - ../../../schemas/contracts/v1/domains/flora/flora_occurrence_candidate.schema.json
  - ../../../packages/domains/flora/normalizers/dwc_occurrence.py
  - ../../../fixtures/domains/flora/flora_occurrence_candidate/
  - ../../../tests/packages/domains/flora/normalizers/test_dwc_occurrence.py
  - ../../../docs/intake/exploratory/new-ideas-4-25-source-map.md
notes:
  - "Implements a bounded no-network Darwin Core normalization seam derived from the New Ideas 4-25-26 packet."
  - "The candidate remains WORK-stage and cannot be used as a public occurrence or source-admission decision."
[/KFM_META_BLOCK_V2] -->

# `FloraOccurrenceCandidate`

> A deterministic, source-role-preserving **WORK-stage candidate** produced from one bounded Darwin Core occurrence record. It is normalization output, not an admitted source, verified occurrence, EvidenceBundle, policy decision, review approval, public-safe geometry, release, or publication.

## Purpose

The existing `FloraOccurrence` contract is an umbrella semantic object and its paired schema remains permissive. This narrower candidate object creates an enforceable seam before broad occurrence hardening:

1. read one bounded UTF-8 JSON object without network access;
2. map an explicit GBIF or iDigBio Darwin Core profile;
3. preserve source-native identity and role;
4. normalize taxon, occurrence, space, and time fields;
5. bind the output to the input and normalizer version by digest;
6. keep exact coordinates internal and visibly non-public; and
7. return a finite normalization result without silently guessing missing identity or taxonomy.

## Directory Rules basis

The semantic meaning belongs under `contracts/domains/flora/`. The machine shape remains under `schemas/contracts/v1/domains/flora/`. Executable reusable Flora normalization code belongs under the existing `packages/domains/flora/normalizers/` lane. Synthetic examples and enforceability remain under `fixtures/` and `tests/`. Hosted orchestration remains under `.github/workflows/`.

No new repository root, source registry, policy home, lifecycle store, proof home, release family, or public route is created.

## Source profiles

| Profile | Bounded role | Identity preference |
|---|---|---|
| `GBIF_DWC` | Normalize one synthetic GBIF-style Darwin Core record. | `key`, `gbifID`, then `occurrenceID`. |
| `IDIGBIO_DWC` | Normalize one synthetic iDigBio-style Darwin Core record. | `uuid`, then `occurrenceID`. |

The adapter supports only the explicitly registered aliases in the implementation. Unknown source profiles abstain. This is not a generic “accept whatever resembles Darwin Core” parser.

## Required semantic output

A conforming candidate binds:

- deterministic candidate identity from `source_id` and source-record identity;
- source profile, record ID, institution/collection/catalog identifiers, license text, rights holder, and role;
- original scientific name, optional taxon identifier, and optional rank;
- basis of record, event date, and bounded occurrence status;
- Point geometry or explicit no-coordinate state in `EPSG:4326`;
- uncertainty and coordinate exposure;
- source-provided generalization/withholding hints;
- input digest and normalizer identity/version; and
- fixed governance non-effects.

## Finite normalizer outcomes

| Outcome | Meaning |
|---|---|
| `NORMALIZED` | A schema-checkable WORK candidate was produced. This is not evidence or release approval. |
| `ABSTAIN` | Stable source identity, scientific name, source ID, or supported source profile is missing. No candidate is emitted. |
| `ERROR` | Input safety, JSON, coordinate, or uncertainty validation failed. No candidate is emitted. |

A missing stable identity or scientific name is not repaired by generated text. The normalizer abstains.

## Deterministic identity and hashing

`candidate_id` is the first 32 hexadecimal characters of SHA-256 over the UTF-8 sequence:

```text
source_id + U+001F + source_record_id
```

`input_digest` is SHA-256 over sorted-key, compact UTF-8 JSON for the input object. `spec_hash` uses the same local `kfm-fixture-json-v1` profile over the candidate after removing top-level `spec_hash`. Arrays preserve order. This is a fixture/replay profile, not a repository-wide hash-policy amendment.

## Spatial and sensitivity boundary

A source coordinate is retained only as `INTERNAL_EXACT` on a WORK candidate. It is **not** generalized, redacted, released, rendered, or exposed to a public client by this slice. Source-provided `informationWithheld` and `dataGeneralizations` become sorted sensitivity hints. Later geoprivacy, policy, review, redaction-receipt, and release slices must decide whether any derivative may leave WORK.

## Non-effects

Conformance does not:

- activate or admit GBIF, iDigBio, or another live source;
- prove source rights, taxonomic correctness, occurrence truth, or spatial accuracy;
- resolve an `EvidenceRef` or `EvidenceBundle`;
- evaluate policy or complete review;
- deduplicate records or choose a canonical occurrence;
- generalize sensitive geometry;
- authorize promotion, release, publication, map display, Focus Mode use, or public access.

## Validation

```bash
python -m unittest discover \
  --start-directory tests/packages/domains/flora/normalizers \
  --pattern 'test_dwc_occurrence.py' \
  --verbose

python packages/domains/flora/normalizers/dwc_occurrence.py \
  --fixtures fixtures/domains/flora/flora_occurrence_candidate
```

A green result proves only the bounded no-network adapter, deterministic output, schema shape, fixture polarity, and fixed non-authority fields.

## Correction and rollback

The slice is additive. Before merge, close the draft pull request and abandon its branch. After an authorized merge, revert the contract, schema, adapter, fixtures, tests, and workflow through a reviewed corrective pull request. No source record, admitted source, lifecycle promotion, release, or public artifact requires restoration.
