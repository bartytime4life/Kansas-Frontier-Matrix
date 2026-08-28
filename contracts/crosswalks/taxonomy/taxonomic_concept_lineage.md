<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-crosswalks-taxonomy-concept-lineage
title: Taxonomic Concept and Name-Usage Lineage Contract
type: semantic-contract; taxonomy-crosswalk; name-usage; concept-lineage
version: v0.1.0
status: draft; PROPOSED; fixture-first; no-taxonomic-or-release-authority
owners: OWNER_TBD — Taxonomy steward · Flora steward · Fauna steward · Contracts steward · Schema steward · Validation steward
created: 2026-08-05
updated: 2026-08-05
policy_label: public; contracts; crosswalks; taxonomy; non-authoritative
related:
  - ./README.md
  - ../../../schemas/contracts/v1/crosswalks/taxonomy/taxonomic_concept_lineage.schema.json
  - ../../../tools/validators/validate_taxonomic_concept_lineage.py
  - ../../../tests/validators/test_validate_taxonomic_concept_lineage.py
  - ../../../docs/intake/exploratory/new-ideas-4-25-source-map.md
  - ../../../docs/kfm_full_atlas_seed_cards.md
notes:
  - "Implements the bounded KFM-TRIAD-060 gap retained from New Ideas 4-25-26."
  - "A scientific-name string is never treated as timeless taxon identity."
[/KFM_META_BLOCK_V2] -->

# Taxonomic Concept and Name-Usage Lineage

`TaxonomicConceptLineagePacket` separates source-native name usage from taxon concepts and records how concepts relate through time.

## Purpose

Taxonomic sources can use the same string for different concepts, different strings for one concept, and different circumscriptions across treatments. KFM therefore needs four explicit object families:

- **NameUsage** — the exact source-native name, identifier, authorship, rank, status, treatment, time, and evidence.
- **TaxonConcept** — a source-native concept with a versioned circumscription digest and an accepted usage reference.
- **ConceptRelation** — typed, evidence-bound relations such as `SAME_AS`, `OVERLAPS`, `SPLIT_FROM`, `LUMPED_INTO`, or `SUPERSEDES`.
- **TaxonomyReconciliationDecision** — a reversible `ACCEPT`, `PROVISIONAL`, `HOLD`, `ABSTAIN`, or `REJECT` decision under a named profile and authority role.

The profile preserves synonyms, homonyms, misapplications, split/lump history, unresolved mappings, and supersession instead of flattening them into one accepted-name string.

## Placement basis

The repository already has `contracts/crosswalks/taxonomy/` as the semantic-contract lane and `schemas/contracts/v1/crosswalks/` as the paired machine-shape family. This slice adds one topic sublane without creating a new root or a sovereign biodiversity schema family.

| Responsibility | Home |
|---|---|
| Taxonomy crosswalk meaning | `contracts/crosswalks/taxonomy/` |
| Machine shape | `schemas/contracts/v1/crosswalks/taxonomy/` |
| Synthetic examples | `fixtures/contracts/v1/crosswalks/taxonomy/` |
| Validation | `tools/validators/` |
| Tests | `tests/validators/` |
| CI | `.github/workflows/` |
| Authoring provenance | `data/receipts/generated/` |

## Required invariants

- Every source-native identifier and name string is preserved.
- Name usage and taxon concept are separate identities.
- A concept is version-bound through source, native ID, valid time, and circumscription digest.
- Homonyms, misapplications, and unresolved usages cannot be silently accepted.
- Split, lump, overlap, and supersession relations are typed and evidence-bound.
- Reconciliation decisions are reversible and profile-bound.
- Taxonomic resolution is not occurrence, distribution, conservation, rights, policy, or release evidence.
- `ABSTAIN` and `HOLD` are valid outcomes when support is insufficient.

## Deterministic fixture identity

`spec_hash` uses the local `kfm-fixture-json-v1` profile: remove top-level `spec_hash`, serialize sorted-key UTF-8 JSON without insignificant whitespace, preserve array order, compute SHA-256, and prefix `sha256:`.

## Validator behavior

The no-network validator checks:

- schema and deterministic hash integrity;
- unique, resolvable usage, concept, relation, and decision identities;
- canonical reason/reference ordering;
- valid-time ordering;
- concept-to-accepted-usage linkage;
- relation endpoint and self-loop rules;
- split/lump evidence support;
- denial of unresolved, homonym, or misapplied usage under `ACCEPT`;
- source-native identity preservation and concept/name separation; and
- explicit non-authority governance fields.

## Validation

```bash
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_taxonomic_concept_lineage.py' \
  --verbose
```

A green result proves only the proposed fixture profile and local lineage invariants. It does not establish a current accepted taxonomy, resolve a live authority, prove an occurrence, or authorize public use.

## Rollback
Before merge, close the draft pull request and remove its branch. After an authorized merge, revert this dependency-closed slice. If later records rely on concept or decision IDs, preserve them through correction and supersession rather than deleting history.
