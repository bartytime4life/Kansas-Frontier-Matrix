<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract-guide/domains/flora/specimenrecord
title: Flora specimen candidate compatibility guide
type: draft-contract-guide
version: v1.0
status: draft; proposed; repository-grounded; review-required
owners:
  - OWNER_TBD - Flora and contracts stewards
created: 2026-10-08
updated: 2026-10-08
policy_label: public
owning_root: contracts/
responsibility: Flora specimen candidate compatibility guide; explain semantic review requirements without adopting a schema, policy, source, or release decision
truth_posture: CONFIRMED inspected repository shape and paths; PROPOSED semantic review examples; UNKNOWN operational acceptance
related:
  - contracts/domains/flora/specimen_record.md
  - schemas/contracts/v1/domains/flora/specimen_record.schema.json
  - tools/validators/domains/flora/validate_specimen_record.py
  - fixtures/domains/flora/specimen_record/README.md
evidence_snapshot: ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe
[/KFM_META_BLOCK_V2] -->

# Specimenrecord

This retained CamelCase entry routes to the detailed
[SpecimenRecord contract](specimen_record.md). Its purpose is to explain the
implemented bounded candidate and its limits without creating another semantic
or identity authority.

## Meaning and current implementation

A specimen record represents a voucher, herbarium sheet, accession, institutional
catalog record, image or determination used as Flora evidence. Collection date,
locality, source-native taxon label, later determination and retrieval time must
remain distinct. A historical specimen cannot establish current occurrence.

Unlike the surrounding open-object schemas, the
[specimen schema](../../../schemas/contracts/v1/domains/flora/specimen_record.schema.json)
is a closed synthetic profile. It fixes `schema_version` to
`kfm.flora.specimen-record.v1`, `object_type` to `SpecimenRecordCandidate`,
`domain` to `flora`, and `fixture_only` to true. Every profile object rejects
additional properties. All top-level profile fields are required.

## Enforced shape and semantic support

| Field group | What it carries |
|---|---|
| `record_id`, `spec_hash` | Deterministic candidate identity and full candidate-content integrity |
| `record_class`, `source_role` | Specimen class and evidence role, with no observed/synthetic collapse |
| `source` | Descriptor, source record/version, institution, collection, catalog number, terms and retrieval receipt |
| `collection_event` | Event date/precision, historical/current claim flags, locality support and restricted geometry reference |
| `determination` | Source taxon name, taxon/crosswalk references, status/date and label-text authority flag |
| `evidence_refs` | Bounded digest references supplied by the candidate |
| `rights` | Metadata and image-reuse permissions kept separate |
| `sensitivity` | Rare-taxon state, exact-location exposure, review and redaction references |
| `public_projection` | Candidate posture, historical/no-current claim, derivative/image references and null release reference |
| `governance` | Source, evidence, policy, review, release and publication effects fixed false |
| `correction` | Superseded record and correction references |

References are opaque, digest-bound declarations. The validator does not
resolve or authenticate sources, evidence, geometry, taxonomy, consent or review.

## Identity behavior

The [validator](../../../tools/validators/domains/flora/validate_specimen_record.py)
computes `record_id` from canonical sorted compact JSON containing the source
`descriptor_ref`, `institution_code`, `collection_code`, `catalog_number` and
`source_record_ref`, then SHA-256. The identifier uses the
`kfm://candidate/flora/specimen/sha256:` prefix.

`spec_hash` hashes the full canonical candidate excluding only its top-level
`spec_hash`. This separates the stable source/catalog identity subject from the
complete candidate contents. These are candidate algorithms, not adoption of a
public canonical specimen identity service.

## Examples and failure behavior

The [synthetic corpus](../../../fixtures/domains/flora/specimen_record/README.md)
covers a public-safe historical candidate, a sensitive specimen held from public
projection, an unresolved catalog candidate and an explicitly synthetic record.

Invalid cases include claiming current occurrence from historical evidence,
accepting label text as resolved taxonomy, exposing exact locality, setting
false governance authority, omitting redaction support, confusing metadata with
image rights, changing identity/hash, and losing correction lineage. A sensitive
held candidate can be structurally valid without being publishable.

```bash
python tests/domains/flora/test_specimen_record.py --verbose
python tools/validators/domains/flora/validate_specimen_record.py --fixtures
```

Use the repository's Python environment with the declared `jsonschema`
dependency. Passing these no-network fixtures proves their local schema and
semantic boundary; it does not verify a real herbarium or open media license.

## Review gaps and lifecycle

Broader source admission, taxonomic review, real rights/sensitivity handling,
public citation projection, re-determination, duplicate merge/split, image
takedown and released-derivative rollback remain separate work. Extend the
lowercase contract, paired schema, fixtures and tests together if that scope
changes. Preserve this compatibility path until inbound references are migrated
through review; its existence does not clear any release gate.
