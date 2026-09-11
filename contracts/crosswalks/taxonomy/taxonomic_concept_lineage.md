<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-crosswalks-taxonomy-concept-lineage
title: Taxonomic Concept and Name-Usage Lineage Contract
type: semantic-contract
version: v0.2.1
status: draft; PROPOSED; repository-grounded; executable-fixture-profile; human-review-hold; no-taxonomic-or-release-authority
owners: OWNER_TBD — Taxonomy steward · Flora steward · Fauna steward · Contracts steward · Schema steward · Validation steward
created: 2026-08-05
updated: 2026-09-08
owning_root: contracts/
policy_label: public; contracts; crosswalks; taxonomy; non-authoritative; fixture-scoped-validation
responsibility: Define cross-domain meaning and anti-collapse invariants for source-native name usages, taxon concepts, typed concept relations, and reversible reconciliation decisions without creating taxonomic, occurrence, source, policy, review, or release authority.
truth_posture: cite-or-abstain
related:
  - ./README.md
  - ../../../schemas/contracts/v1/crosswalks/taxonomy/taxonomic_concept_lineage.schema.json
  - ../../../tools/validators/validate_taxonomic_concept_lineage.py
  - ../../../tests/validators/test_validate_taxonomic_concept_lineage.py
  - ../../../.github/workflows/taxonomic-concept-lineage.yml
  - ../../../data/receipts/generated/genrec-taxonomic-concept-lineage-20260805.json
  - ../../../data/receipts/generated/genrec-taxonomic-concept-lineage-contract-currentness-20260908.json
  - ../../source/plants_taxa_drift_assessment.md
  - ../../../docs/intake/exploratory/new-ideas-4-25-source-map.md
  - ../../../docs/kfm_full_atlas_seed_cards.md
  - ../../../docs/intake/exploratory/full-atlas-semantic-disposition-crosswalk.md
notes:
  - "Implements the bounded KFM-TRIAD-060 gap retained from New Ideas 4-25-26."
  - "A scientific-name string is never treated as timeless taxon identity."
  - "v0.2.0 documents the exact schema, validator, test, workflow, and downstream boundary present at main@b20d25d2e2012881049fa96c3d65611ff5616bdc; it changes no executable behavior."
  - "v0.2.1 repairs current metadata conformance after merged PR #4436 and moves subsequent integrity binding to a new currentness receipt without rewriting the retained 2026-08-05 receipt again."
[/KFM_META_BLOCK_V2] -->

# Taxonomic Concept and Name-Usage Lineage

`TaxonomicConceptLineagePacket` is a proposed, fixture-first crosswalk profile for preserving source-native name usage, versioned taxon concepts, evidence-bound concept relations, and reversible reconciliation decisions. It prevents a scientific-name string from being used as timeless taxon identity.

This contract describes the executable repository slice as it exists. It does not select a live taxonomy, admit a source, resolve external references, or create release or publication authority.

## 1. Authority and scope

The packet has one bounded authority: **taxonomy lineage and reconciliation representation**.

It may represent:

- the exact name usage asserted by a source and treatment;
- a source-native taxon concept with a versioned circumscription digest;
- a typed relation between two concepts;
- a profile-bound reconciliation decision that can later be corrected or superseded; and
- the evidence and authoring provenance attached to those records.

It must not be interpreted as:

- an accepted or current taxonomic authority;
- evidence that a taxon occurred at a place or time;
- a distribution, range, habitat, conservation, or abundance claim;
- source admission, rights clearance, policy evaluation, promotion, release, or publication approval; or
- proof that any referenced external object exists, is retrievable, or is authoritative.

`ABSTAIN`, `HOLD`, `PROVISIONAL`, and `UNRESOLVED` are intentional fail-closed states. They must not be collapsed into acceptance merely to produce a complete-looking crosswalk.

## 2. Repository binding

The current binding is frozen to repository `main` at commit `2bddc4b4e453a7396d654d5f988911e9ee3af1ef` for this documentation revision.

| Responsibility | Current repository object | Binding |
|---|---|---|
| Semantic meaning | This contract | Document profile `v0.2.1`; prior blob `a9c50d8567f4cbd3f9e470145c6414f468d4a827` |
| Machine shape | [`taxonomic_concept_lineage.schema.json`](../../../schemas/contracts/v1/crosswalks/taxonomy/taxonomic_concept_lineage.schema.json) | JSON Schema Draft 2020-12; packet `schema_version` is exactly `1.0.0`; blob `a9896bb2582ed33a92442b1623245c43c1ee4a34` |
| Validation | [`validate_taxonomic_concept_lineage.py`](../../../tools/validators/validate_taxonomic_concept_lineage.py) | Local, no-network validation; blob `47a42651c164214ecddcc31ac4a82db16ad85b3d` |
| Executable examples | [`test_validate_taxonomic_concept_lineage.py`](../../../tests/validators/test_validate_taxonomic_concept_lineage.py) | Six unit tests with embedded compressed synthetic vectors; blob `6e0ae104b630e0fded68124e92b1ea7c9c89aed0` |
| CI | [`taxonomic-concept-lineage.yml`](../../../.github/workflows/taxonomic-concept-lineage.yml) | Path-scoped Python 3.11 workflow; blob `8a497185f1e16e2530d3adffe6fef4227acc8cd6` |
| Retained authoring provenance | [`genrec-taxonomic-concept-lineage-20260805.json`](../../../data/receipts/generated/genrec-taxonomic-concept-lineage-20260805.json) | Post-PR #4436 receipt bytes are retained without another in-place refresh; blob `3fae4f0aabe2580114177f6622d3213dc8a60fb6` |
| Currentness provenance | [`genrec-taxonomic-concept-lineage-contract-currentness-20260908.json`](../../../data/receipts/generated/genrec-taxonomic-concept-lineage-contract-currentness-20260908.json) | Binds this metadata/currentness repair, the workflow pointer, and the current unchanged packet companions; human review remains pending |
| Downstream reference | [`plants_taxa_drift_assessment.md`](../../source/plants_taxa_drift_assessment.md) | Consumes an opaque `taxonomic_concept_lineage_ref`; it does not dereference or establish live taxonomy authority |

The existing `contracts/crosswalks/taxonomy/` lane owns semantic crosswalk meaning. The paired schema, validator, tests, workflow, and receipt remain in their existing responsibility roots. This revision creates no new root, authority lane, schema family, or compatibility path.

## 3. Packet envelope

The schema closes the root object and all nested records with `additionalProperties: false`. A packet requires every field below.

| Field | Required value or constraint |
|---|---|
| `object_type` | Exactly `TaxonomicConceptLineagePacket` |
| `schema_version` | Exactly `1.0.0` |
| `packet_id` | `taxonomy-lineage:` identifier; lowercase pattern; maximum 258 characters including prefix |
| `hash_profile` | Exactly `kfm-fixture-json-v1` |
| `spec_hash` | `sha256:` plus 64 lowercase hexadecimal characters |
| `name_usages` | 1–128 `NameUsage` records |
| `taxon_concepts` | 1–128 `TaxonConcept` records |
| `concept_relations` | 0–256 `ConceptRelation` records |
| `reconciliation_decisions` | 1–128 `TaxonomyReconciliationDecision` records |
| `separation` | Five explicit `true` boundary assertions |
| `provenance` | Resolver, input, run-receipt, version, and recorded-time fields |
| `governance` | Eight explicit `false` authority claims and a null `release_ref` |

Reference strings are opaque, nonblank values of at most 640 characters. Reference arrays contain at most 128 unique strings; all evidence arrays and provenance `input_refs` contain at least one item. The schema checks reference shape but neither schema nor validator dereferences a reference.

## 4. Record families

### 4.1 `NameUsage`

`NameUsage` preserves what one source and treatment said. Its identity is `usage_id`, not `name_string`.

| Required field | Meaning |
|---|---|
| `usage_id` | Pattern-bound `name-usage:` identifier |
| `source_descriptor_ref` | Opaque reference to the source descriptor |
| `source_role` | Uppercase role code |
| `source_native_id` | Exact nonblank identifier supplied by the source |
| `name_string` | Exact nonblank scientific-name string used in the treatment |
| `authorship` | Nonblank text or null |
| `rank` | Lowercase rank token |
| `usage_status` | One finite status from the vocabulary below |
| `treatment_ref` | Opaque reference to the treatment |
| `valid_from`, `valid_to` | Offset-aware date-times or null; interval ordering is not currently enforced |
| `evidence_refs` | One or more unique opaque references |
| `native_identity_preserved` | Exactly `true` |

`usage_status` is one of `ORIGINAL`, `ACCEPTED`, `SYNONYM`, `MISAPPLIED`, `HOMONYM`, or `UNRESOLVED`.

### 4.2 `TaxonConcept`

`TaxonConcept` represents a source-native circumscription, separately from every name string.

| Required field | Meaning |
|---|---|
| `concept_id` | Pattern-bound `taxon-concept:` identifier |
| `source_descriptor_ref` | Opaque source reference |
| `source_native_id` | Exact nonblank source-native concept identifier |
| `circumscription_digest` | SHA-256 digest of the version-bound circumscription representation |
| `accepted_usage_ref` | In-packet reference to a `NameUsage` |
| `rank` | Lowercase rank token |
| `valid_from`, `valid_to` | Offset-aware date-times or null; interval ordering is not currently enforced |
| `evidence_refs` | One or more unique opaque references |

The validator requires `accepted_usage_ref` to resolve to a usage in the same packet. It does not compare ranks, source descriptors, source-native identifiers, or valid-time intervals across the linked records.

### 4.3 `ConceptRelation`

`ConceptRelation` is a reversible, directed assertion between two in-packet concepts.

| Required field | Meaning |
|---|---|
| `relation_id` | Pattern-bound `concept-relation:` identifier |
| `from_concept_ref`, `to_concept_ref` | In-packet concept references |
| `relation_type` | One finite relation from the vocabulary below |
| `effective_at` | Offset-aware date-time |
| `evidence_refs` | One or more unique opaque references |
| `reversible` | Exactly `true` |

`relation_type` is one of `SAME_AS`, `OVERLAPS`, `INCLUDES`, `EXCLUDES`, `SPLIT_FROM`, `LUMPED_INTO`, `SUPERSEDES`, or `UNRESOLVED`.

Both endpoints must resolve and must differ. Every relation type requires evidence by schema, but the current validator does not apply extra evidence semantics to split, lump, overlap, or supersession relations.

### 4.4 `TaxonomyReconciliationDecision`

A reconciliation decision records an accountable outcome under one named profile and authority role. It does not mutate the source-native records.

| Required field | Meaning |
|---|---|
| `decision_id` | Pattern-bound `taxonomy-decision:` identifier |
| `usage_refs` | One or more unique in-packet usage references |
| `concept_refs` | Zero or more unique in-packet concept references |
| `outcome` | One finite outcome from the vocabulary below |
| `authority_role` | Uppercase role code; a label, not proof of assignment |
| `profile_id` | Pattern-bound `taxonomy-profile:` identifier |
| `profile_version` | Three-part numeric semantic version |
| `rationale_codes` | 1–32 unique uppercase reason codes |
| `evidence_refs` | One or more unique opaque references |
| `recorded_at` | Offset-aware date-time |
| `supersedes_decision_ref` | Opaque reference or null |
| `reversible` | Exactly `true` |
| `automatic_resolution` | Exactly `false` |

`outcome` is one of `ACCEPT`, `PROVISIONAL`, `HOLD`, `ABSTAIN`, or `REJECT`.

Every referenced usage and concept must resolve within the packet. `ACCEPT` and `PROVISIONAL` require at least one concept. `ACCEPT` must not include a usage whose status is `MISAPPLIED`, `HOMONYM`, or `UNRESOLVED`. `PROVISIONAL` deliberately retains a lower-confidence route; it does not equal acceptance.

## 5. Separation and governance assertions

The `separation` object requires all of these values to be `true`:

- `name_string_is_not_identity`
- `source_native_ids_preserved`
- `concept_circumscription_versioned`
- `unresolved_conflict_preserved`
- `taxonomy_is_not_occurrence_evidence`

The `governance` object requires all of these values to be `false`:

- `taxonomic_authority_created`
- `occurrence_evidence_claimed`
- `distribution_claimed`
- `source_admitted`
- `policy_evaluated`
- `promotion_authorized`
- `release_authorized`
- `publication_authorized`

`release_ref` must be null. A role code, profile ID, evidence reference, deterministic hash, passing validator, green workflow, merged pull request, or repository path cannot change those non-effects.

## 6. Provenance

The packet requires:

- `recorded_at`: an offset-aware date-time;
- `run_receipt_ref`: an opaque reference to the producing run receipt;
- `resolver_id`: an opaque resolver identity;
- `resolver_version`: a semantic version with optional prerelease or build suffix; and
- `input_refs`: one or more unique opaque input references.

These fields preserve authoring lineage. The validator checks their shape only. It does not establish that the resolver ran, the receipt exists, the inputs are admitted, or the evidence chain is closed.

## 7. Deterministic fixture identity

`spec_hash` uses `kfm-fixture-json-v1`:

1. Remove the top-level `spec_hash` member.
2. Serialize the remaining JSON with keys sorted, UTF-8 encoding, no insignificant whitespace, and non-finite numbers denied.
3. Preserve array order exactly as authored.
4. Compute SHA-256 over those bytes.
5. Prefix the lowercase digest with `sha256:`.

This hash detects changes to the packet representation under the profile. It is not a signature, evidence digest, source checksum, release digest, or authority grant. The validator does not sort arrays or require an independently canonical order for reference or reason-code arrays.

## 8. Validator behavior

The local validator performs three layers.

### 8.1 Input safety

- Denies symlink inputs and files larger than 1 MiB.
- Requires an existing regular UTF-8 JSON file with an object root.
- Rejects duplicate object keys, invalid JSON, non-finite numbers, read failures, and excessive JSON complexity.
- Returns only finding codes and JSON-pointer fields; the CLI does not echo candidate values.

### 8.2 Schema validation

- Checks the bundled schema as Draft 2020-12 before applying it.
- Uses format checking for offset-aware date-time strings.
- Caps schema findings at 100 and emits `SCHEMA_FINDINGS_TRUNCATED` when more exist.
- Fails closed with `SCHEMA_UNAVAILABLE` when the schema cannot be loaded or validated.

### 8.3 Semantic validation

- Recomputes and compares `spec_hash`.
- Resolves relation endpoints, concept accepted-usage references, and decision usage/concept references within the packet.
- Denies relation self-loops.
- Requires concept references for `ACCEPT` and `PROVISIONAL` decisions.
- Denies acceptance of `MISAPPLIED`, `HOMONYM`, and `UNRESOLVED` usages.
- Enforces decision reversibility, denial of automatic resolution, separation assertions, and governance non-authority fields.

Current semantic finding codes are:

`SPEC_HASH_MISMATCH`, `RELATION_CONCEPT_UNRESOLVED`, `RELATION_SELF_LOOP_DENIED`, `CONCEPT_USAGE_UNRESOLVED`, `DECISION_USAGE_UNRESOLVED`, `DECISION_CONCEPT_UNRESOLVED`, `DECISION_CONCEPT_REQUIRED`, `UNRESOLVED_USAGE_ACCEPTED`, `AUTOMATIC_TAXONOMY_RESOLUTION_DENIED`, `DECISION_NOT_REVERSIBLE`, `NAME_STRING_IDENTITY_COLLAPSE`, `TAXONOMY_SEPARATION_VIOLATION`, and `GOVERNANCE_BOUNDARY_VIOLATION`.

The CLI exits `0` for a packet with no findings, `1` for schema or semantic findings, and `2` for input or validator errors.

## 9. Executable coverage

The test module currently contains six tests. Its synthetic vectors are compressed and embedded in the test source rather than stored as standalone JSON files.

| Vector or check | Expected result |
|---|---|
| Valid synthetic packet | Passes |
| Name string treated as identity | `NAME_STRING_IDENTITY_COLLAPSE` and schema failure |
| Unresolved usage accepted | `UNRESOLVED_USAGE_ACCEPTED` |
| Relation endpoint missing | `RELATION_CONCEPT_UNRESOLVED` |
| Altered hash | `SPEC_HASH_MISMATCH` |
| Duplicate JSON key | Fails closed |
| CLI candidate-value sentinel | Not echoed |
| Repeated hash computation | Deterministic |
| Bundled JSON Schema | Valid Draft 2020-12 schema |

The schema metadata declares `fixtures/contracts/v1/crosswalks/taxonomy/taxonomic_concept_lineage/` as `fixtures_root`, but that directory is absent at the frozen repository commit. The workflow and generated receipt also do not include standalone fixture files. Until a dependency-closed follow-up adds and wires that root, the embedded test vectors are the only executable examples and the declared fixture root is repository drift.

The path-scoped workflow runs the dedicated unit test module and validates the current packet receipt. The retained 2026-08-05 receipt remains process history rather than the mutable integrity target for later revisions. A passing run proves only that this proposed local profile satisfies those checks at that commit.

## 10. Known enforcement gaps

The current schema and validator do **not** enforce:

- uniqueness of `usage_id`, `concept_id`, `relation_id`, or `decision_id` across their arrays;
- canonical ordering of reference arrays, reason-code arrays, records, or relations;
- chronological ordering of `valid_from` and `valid_to`;
- cross-record agreement of rank, source, source-native ID, or valid time;
- split/lump-specific evidence rules beyond the general nonempty `evidence_refs` requirement;
- dereferencing or existence of source, treatment, evidence, receipt, resolver, input, release, or superseded-decision references;
- cycle detection, transitive consistency, or contradiction detection across concept relations;
- a live taxonomy authority, live-source retrieval, source admission, or evidence closure;
- rights, sensitivity, conservation, policy, review, promotion, release, or publication decisions; or
- downstream dereferencing of `taxonomic_concept_lineage_ref` in the PLANTS taxa-drift assessment family.
- single-revision replay of the retained 2026-08-05 receipt: PR #4436 refreshed its contract digest in place while retaining its authoring-time workflow digest, so no one Git revision satisfies both bindings. The separate currentness receipt binds the retained bytes and becomes the CI pointer without erasing that provenance limitation.

These are explicit limits, not implied validator behavior. Any executable expansion requires a dependency-closed change to the contract, schema, validator, positive and negative fixtures, tests, workflow paths, and generated receipt as applicable.

## 11. Evidence and coordination lineage

| Source | Supports | Limits |
|---|---|---|
| GitHub `main@2bddc4b4e453a7396d654d5f988911e9ee3af1ef` and [merged PR #4436](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/4436) | Current implementation bytes, the v0.2 semantic reconciliation, and the observed merge event. | Merge and green CI are not independent taxonomic, policy, review, or release approval. |
| [Repository source map](../../../docs/intake/exploratory/new-ideas-4-25-source-map.md), [KFM-TRIAD-060](../../../docs/kfm_full_atlas_seed_cards.md#kfm-triad-060--taxonomic-concept-and-name-usage-lineage), and [semantic disposition](../../../docs/intake/exploratory/full-atlas-semantic-disposition-crosswalk.md) | Proposal lineage and the current `EXECUTABLE_FIXTURE_PROFILE` / `HUMAN_REVIEW/HOLD` classification. | Proposed/partial lineage does not establish a live authority. |
| [Drive: New Ideas 4-25-26](https://docs.google.com/document/d/1uTY-mR9y3ReKdvbwsjAy0PeVtScN118_7hqDFPpYi_k/edit?usp=drivesdk) | Read-only proposal material about taxonomic backbones, native identifiers, accepted/synonym relationships, provenance, licensing, and crosswalks. | It does not define the exact KFM object-family names or prove that external authority facts remain current. |
| [Drive: Flora builder](https://docs.google.com/document/d/1SdZMLyyPbzywH4KUmEpuPsRic8_rFyQrIowns45vVfU/edit?usp=drivesdk) and [Drive: Fauna builder](https://docs.google.com/document/d/1RKUhZRdssRFWNFWzcsrHFahB4xAMCxiGafclb1_xNkA/edit?usp=drivesdk) | Domain guidance that synonymy must preserve source-native names and historical identity while taxonomy remains distinct from occurrence evidence. | Read-only coordination lineage is subordinate to repository evidence. |
| [Notion: Flora builder](https://app.notion.com/p/3caa92021bf6815db884de68502fb21f) and [Notion: Fauna builder](https://app.notion.com/p/3caa92021bf6811b8926dc0010d67672) | Current coordination statements for plant/animal ownership and non-collapse rules. | Both pages are unverified coordination records, not implementation or approval authority. |

GitHub remains implementation authority. Drive supplies read-only proposal lineage, and Notion supplies coordination context. None supplies source admission, taxonomic acceptance, review approval, or publication permission.

## 12. Validation

Run the dedicated suite from the repository root:

```bash
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_taxonomic_concept_lineage.py' \
  --verbose
```

Reviewers should also confirm that the schema, validator, test, workflow, and receipt paths still resolve; the target workflow is triggered for the changed path; and no overlapping pull request changes this object family.

## 13. Acceptance and rollback

Acceptance of this document revision requires:

- the semantic edit is confined to this file; a currentness receipt and its workflow pointer may accompany it without rewriting the retained 2026-08-05 receipt again;
- no unsupported validator claim;
- exact preservation of the non-authority boundary;
- review through the repository `CODEOWNERS` route; and
- a green target workflow for the exact pull-request head.

Before merge, rollback is closing the pull request and deleting its branch. After an authorized merge, rollback is a normal revert of this documentation change. If later data depends on packet, usage, concept, relation, or decision IDs, correct and supersede those records; do not erase lineage.
