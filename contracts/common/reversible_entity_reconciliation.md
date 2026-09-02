<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-common-reversible-entity-reconciliation
title: Reversible Entity Reconciliation Contract
type: semantic-contract; shared-kernel; reconciliation; deduplication
version: v0.1.0
status: draft; PROPOSED; fixture-first; no-merge-or-release-authority
owners: OWNER_TBD — Contracts steward · Identity steward · Domain stewards · Schema steward · Validation steward
created: 2026-08-05
updated: 2026-08-05
policy_label: public; contracts; common; identity; reconciliation; non-authoritative
related:
  - ./README.md
  - ../../schemas/contracts/v1/common/reversible_entity_reconciliation.schema.json
  - ../../tools/validators/validate_reversible_entity_reconciliation.py
  - ../../tests/validators/test_validate_reversible_entity_reconciliation.py
  - ../../docs/intake/exploratory/new-ideas-4-25-source-map.md
  - ../../docs/kfm_full_atlas_seed_cards.md
notes:
  - "Implements the bounded KFM-TRIAD-059 gap retained from New Ideas 4-25-26."
  - "Source-native assertions remain immutable inputs; matching and clustering are reversible decisions."
[/KFM_META_BLOCK_V2] -->

# Reversible Entity Reconciliation

`ReversibleEntityReconciliationPacket` is a fixture-first shared profile for proposing and reviewing whether source-native assertions refer to the same entity without destroying disagreement or silently manufacturing a canonical winner.

## Purpose

The packet separates five concerns:

1. **SourceAssertion** preserves each source-native identity assertion and its evidence.
2. **MatchProposal** records blocking keys, feature comparisons, confidence bounds, and the exact candidates considered.
3. **ReconciliationDecision** records `MATCH`, `NO_MATCH`, `HOLD`, or `ABSTAIN` with authority and evidence.
4. **EntityCluster** is a derived review view backed only by explicit `MATCH` decisions.
5. **SplitDecision** reverses a prior cluster while preserving the historical decision and every source assertion.

This profile addresses the packet-derived warning that rounded coordinates, normalized names, dates, or taxon strings are unsafe automatic dedupe keys. It also rejects winner-takes-all normalization.

## Why this belongs in `common/`

Entity reconciliation is reused by biodiversity, taxonomy, place identity, source records, historic features, infrastructure, and other lanes. No single domain owns the narrow decision vocabulary. Domains retain ownership of their atomic facts, blocking features, scientific or legal meaning, and review thresholds.

## Directory Rules basis

| Responsibility | Home |
|---|---|
| Shared meaning | `contracts/common/` |
| Machine shape | `schemas/contracts/v1/common/` |
| Synthetic examples | `fixtures/contracts/v1/common/` |
| Validation | `tools/validators/` |
| Tests | `tests/validators/` |
| Focused CI | `.github/workflows/` |
| Authoring provenance | `data/receipts/generated/` |

No new root, source registry, canonical entity store, policy authority, lifecycle store, release object, or public route is introduced.

## Required invariants

- Every source assertion remains present and independently addressable.
- A proposal never performs a merge and always requires a decision.
- A `MATCH` decision is reversible and cites evidence.
- A cluster may reference only assertions covered by explicit `MATCH` decisions.
- Transitive closure is not silently applied.
- A split partitions the complete prior cluster without adding, dropping, or duplicating members.
- Confidence is bounded by the declared profile limit and never substitutes for authority.
- `HOLD` and `ABSTAIN` remain first-class outcomes.
- Validation success grants no source, evidence, policy, review, merge, release, or publication authority.

## Deterministic fixture identity

`spec_hash` uses `kfm-fixture-json-v1`: remove the top-level `spec_hash`, serialize UTF-8 JSON with sorted keys and no insignificant whitespace, preserve array order, compute SHA-256, and prefix `sha256:`. This is a local fixture profile, not a repository-wide hash-policy decision.

## Validator outcomes

The validator emits stable, non-echoing findings for:

- automatic or destructive merge behavior;
- unresolved or duplicated references;
- confidence-limit violations;
- cluster membership not backed by `MATCH`;
- transitive or overlapping clusters;
- split partitions that add, drop, or duplicate members;
- noncanonical reason/reference arrays;
- deterministic hash mismatch; and
- governance overclaim.

## Validation

```bash
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_reversible_entity_reconciliation.py' \
  --verbose
```

A green result proves only the proposed schema, fixture hash profile, exact synthetic fixture polarity, and local reconciliation invariants. It does not prove two real-world records identify the same entity.

## Rollback
Before merge, close the draft pull request and delete the feature branch. After an authorized merge, revert the dependency-closed contract/schema/fixtures/validator/tests/workflow/receipt change. Preserve any later relied-on decision history through correction or supersession rather than destructive deletion.
