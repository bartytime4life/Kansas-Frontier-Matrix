<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/choropleth-classification-disclosure
title: ChoroplethClassificationDisclosureCandidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Evidence steward · Cartography steward · Analytics steward · Validation steward
created: 2026-08-10
updated: 2026-08-10
owning_root: contracts/
policy_label: internal; evidence; cartography; choropleth; classification; disclosure
responsibility: Define a fixture-only disclosure for one choropleth classification profile without computing classes, selecting a legend, resolving evidence, or creating analytics, policy, review, release, or publication authority.
truth_posture: "CONFIRMED supplied-card traceability and repository placement; PROPOSED inactive contract; UNKNOWN consumer adoption and domain-specific classification fitness; NEEDS VERIFICATION human review and hosted CI"
related:
  - ./analytic_output_disclosure_assessment.md
  - ./measurement_scale_operation_assessment.md
  - ../common/aggregate_statistic.md
  - ../common/geography_version.md
  - ../data/cartographic_omission_disclosure.md
  - ../../schemas/contracts/v1/evidence/choropleth_classification_disclosure.schema.json
  - ../../fixtures/contracts/v1/evidence/choropleth_classification_disclosure/cases.json
  - ../../tools/validators/evidence/validate_choropleth_classification_disclosure.py
  - ../../tests/validators/evidence/test_validate_choropleth_classification_disclosure.py
  - ../../docs/intake/exploratory/pass-18-choropleth-classification-disclosure-source-map.md
tags: [kfm, evidence, choropleth, classification, cartography, fixture-only, no-network]
notes:
  - "Implements the smallest dependency-closed portion of supplied Pass 18 card KFM-P18-INV-477."
  - "A PASS proves declaration coherence only; it does not establish statistical fitness, evidence closure, review, release, or publication."
[/KFM_META_BLOCK_V2] -->

# ChoroplethClassificationDisclosureCandidate

`ChoroplethClassificationDisclosureCandidate` makes the classification choices behind one synthetic choropleth or thematic aggregate layer inspectable. It records the method, class count, ordered breaks, boundary rule, geography unit, value-range assumption, null and outlier treatment, and review-facing disclosure references requested by supplied Pass 18 card `KFM-P18-INV-477`.

## Boundary

A validator `PASS` proves only that the closed candidate shape, deterministic profile hash, declared references, break ordering, class-count relationship, range endpoints, treatment references, disclosure fields, and fixed-false authority claims are locally coherent.

The profile does not read source values, calculate a classification, select a method, infer a geography, choose colors, render a legend, resolve a reference, validate an `AggregateStatistic`, assess scientific or cartographic fitness, decide policy or review, promote, release, deploy, publish, or authorize public use.

## Required disclosure

One complete declaration names:

- a candidate `LayerManifest`, `AggregateStatistic`, `IndicatorDefinition`, and `GeographyVersion` by digest-bound reference;
- an intended-use class;
- a classification method and method definition;
- an integer class count and exactly `class_count + 1` strictly increasing decimal break strings;
- an explicit boundary convention and geography unit;
- value-range, null-treatment, and outlier-treatment assumptions; and
- a legend, review record, Evidence Drawer section, and caveat for public or policy-context candidates.

Decimal breaks are strings under this fixture profile so their authored precision survives deterministic hashing. The validator compares them with decimal arithmetic but does not calculate or endorse the breaks.

## Finite validator outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | The declared classification and disclosure posture is locally coherent. |
| `ABSTAIN` | A required reference or classification state remains unresolved, incomplete, or unknown. |
| `DENY` | Breaks, counts, ranges, treatment references, public disclosure, deterministic identity, or method semantics are incoherent. |
| `ERROR` | The candidate cannot be evaluated safely or declares a classification error. |

These outcomes are validator results, not statistical findings, cartographic approvals, policy decisions, review approvals, release states, or runtime answers.

## Directory Rules basis

The object assesses disclosure and evidence support for a derived representation, so semantic meaning belongs under `contracts/evidence/`; machine shape under `schemas/contracts/v1/evidence/`; synthetic replay under `fixtures/contracts/v1/evidence/`; repository validation under `tools/validators/evidence/`; executable conformance evidence under `tests/validators/evidence/`; orchestration under `.github/workflows/`; source reconciliation under `docs/intake/exploratory/`; and authoring accountability under `data/receipts/generated/`.

These are existing responsibility roots adopted by ADR-0029. The profile composes existing layer, aggregate-statistic, indicator, geography-version, measurement-scale, analytic-output, and cartographic-disclosure families by opaque reference. It creates no parallel layer registry, statistics store, geography authority, legend authority, evidence store, policy rule, release record, or publication path.

## Validation

```bash
python -m unittest tests.validators.evidence.test_validate_choropleth_classification_disclosure -v
python tools/validators/evidence/validate_choropleth_classification_disclosure.py --fixtures
```

## Rollback

Revert the additive packet. It has no runtime consumer and changes no source value, statistic, geography, layer, legend, evidence, policy, lifecycle, review, release, deployment, or public artifact.
