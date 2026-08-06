<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/domains/flora/flora-occurrence-intake-decision
title: FloraOccurrenceIntakeDecision Contract
type: semantic-contract; flora; occurrence; deduplication; intake-governance
version: v0.1.0
status: draft; PROPOSED; fixture-first; no-network; non-authoritative
owners: OWNER_TBD — Flora steward · Source steward · Rights reviewer · Sensitivity reviewer · Contract steward · Validation steward
created: 2026-08-05
updated: 2026-08-05
policy_label: public; contracts; flora; intake-classification; no-publication-authority
related:
  - ./flora_occurrence_candidate.md
  - ./flora_occurrence.md
  - ../../../schemas/contracts/v1/domains/flora/flora_occurrence_intake_decision.schema.json
  - ../../../packages/domains/flora/normalizers/intake_governance.py
  - ../../../fixtures/domains/flora/flora_occurrence_intake_decision/
  - ../../../tests/packages/domains/flora/normalizers/test_intake_governance.py
  - ../../../docs/intake/exploratory/new-ideas-4-25-source-map.md
notes:
  - "Implements deterministic deduplication and conservative license/sensitivity intake classification derived from the New Ideas 4-25-26 packet."
  - "Classification proposes handling only; it is not policy, review, admission, lifecycle, release, or publication authority."
[/KFM_META_BLOCK_V2] -->

# `FloraOccurrenceIntakeDecision`

> A deterministic, no-network classification over one `FloraOccurrenceCandidate` and a bounded peer set. It identifies likely duplicates and proposes WORK, QUARANTINE, or steward-review handling without becoming a legal-rights decision, policy result, review approval, lifecycle transition, release, or publication action.

## Purpose

The document-derived occurrence pipeline calls for two controls immediately after normalization:

1. deterministic deduplication that preserves the preferred source-native key and a bounded fallback; and
2. explicit handling for unknown/conditional licenses and source-provided sensitivity hints.

This contract turns those controls into an inspectable object rather than embedding them as hidden branching inside a connector.

## Directory Rules basis

Semantic meaning belongs in `contracts/domains/flora/`; machine shape in `schemas/contracts/v1/domains/flora/`; reusable executable logic in the existing `packages/domains/flora/normalizers/` lane; synthetic cases in `fixtures/domains/flora/`; enforceability in `tests/packages/domains/flora/`; and hosted orchestration in `.github/workflows/`.

The slice creates no source registry, policy authority, lifecycle store, proof store, release family, or public API route.

## Deduplication order

The classifier evaluates peers in canonical `candidate_id` order.

| Priority | Method | Key | Boundary |
|---|---|---|---|
| 1 | `PRIMARY_INSTITUTION_CATALOG` | normalized `institution_code + catalog_number` | Preferred when both fields exist. It is an intake duplicate signal, not canonical-record authority. |
| 2 | `FALLBACK_SPATIOTEMPORAL_TAXON` | normalized scientific name + event date + coordinates rounded to four decimal places | Used only when no primary match exists. Rounding is a comparison aid; it does not alter or publish geometry. |
| 3 | `NONE` | no matching peer | No uniqueness claim beyond the bounded peer set. |

A matching peer produces `DEDUPLICATE` and names the candidate that should receive steward attention. The object does not delete, merge, supersede, or choose the canonical occurrence.

## License profile

The profile is deliberately small and conservative:

- `CC0-1.0`, `CC-BY-4.0`, `PDDL-1.0`, and `PUBLIC-DOMAIN` are classified `OPEN_DECLARED` for continued WORK-stage processing;
- strings containing conditional/restricted markers such as `CC-BY-NC`, `CC-BY-SA`, `ODBL`, `RESTRICTED`, or `CUSTOM` are classified `RESTRICTED_OR_CONDITIONAL` and proposed for QUARANTINE; and
- missing or unrecognized license text is `UNKNOWN` and proposed for QUARANTINE.

This is a deterministic profile match, not legal advice, rights clearance, source admission, or a policy decision. A steward and applicable policy must make any consequential use decision.

## Sensitivity profile

Source-provided `informationWithheld` and `dataGeneralizations` hints are carried from the normalized candidate.

| State | Classification |
|---|---|
| No source sensitivity hint | `NO_SPECIAL_HANDLING` at this bounded intake seam. This is not proof that the occurrence is non-sensitive. |
| Hint with no exact geometry | `HOLD_FOR_REVIEW`. |
| Hint with `INTERNAL_EXACT` geometry | `GENERALIZE_REQUIRED` and `HOLD_FOR_REVIEW`. |

The classifier never generalizes coordinates. A later geoprivacy transform must emit its own receipt and be reviewed before any release candidate exists.

## Finite decision precedence

1. malformed candidate or peer set → `ERROR`;
2. duplicate match → `DEDUPLICATE`;
3. missing/unknown/conditional license → `QUARANTINE`;
4. source sensitivity hint → `HOLD_FOR_REVIEW`;
5. otherwise → `ACCEPT_FOR_WORK`.

These outcomes are proposed handling dispositions. None executes a lifecycle transition.

## Determinism

- peer candidates are sorted by `candidate_id` before comparison;
- the peer-set digest binds the exact ordered peer objects;
- `decision_id` binds candidate `spec_hash`, peer-set digest, and engine version;
- `spec_hash` uses `kfm-fixture-json-v1` over the decision after removing top-level `spec_hash`.

## Non-effects

A conforming decision does not:

- establish source admission, occurrence truth, canonical identity, or taxonomic authority;
- provide legal advice or resolve rights;
- evaluate the repository’s policy bundle;
- complete human/steward review;
- execute WORK/QUARANTINE movement;
- delete or merge duplicates;
- generalize, redact, release, render, or expose geometry;
- authorize promotion, release, publication, map use, Focus Mode use, or public access.

## Validation

```bash
python -m unittest discover \
  --start-directory tests/packages/domains/flora/normalizers \
  --pattern 'test_intake_governance.py' \
  --verbose

python packages/domains/flora/normalizers/intake_governance.py \
  --fixtures fixtures/domains/flora/flora_occurrence_intake_decision
```

A green result proves only deterministic bounded classification and exact synthetic fixture outcomes.

## Correction and rollback

This stacked slice is additive and depends on the candidate-normalizer slice. Before merge, close the draft PR and abandon its branch. After authorized merges, revert this contract/schema/classifier/fixture/test/workflow packet through a reviewed corrective PR. No admitted source, lifecycle state, release, or public artifact requires restoration.
