<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/indicator-definition
title: IndicatorDefinition Candidate Contract
type: semantic-contract
version: v0.1.0
status: proposed; inactive; fixture-only; review-required
owners: OWNER_TBD — Evidence steward · Analytics steward · Indicator steward · Validation steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; evidence; analytics; indicator; no-network
owning_root: contracts/
responsibility: Define one immutable indicator method declaration with explicit components, denominator, missing-data, normalization, support, disclosure, and no-authority boundaries.
truth_posture: CONFIRMED source and repository gap / PROPOSED inactive definition / NEEDS VERIFICATION steward adoption and hosted exact-head execution
related:
  - ./analytic_output_disclosure_assessment.md
  - ./environmental_indicator_evidence_bundle_profile.md
  - ../../schemas/contracts/v1/evidence/indicator_definition.schema.json
  - ../../fixtures/contracts/v1/evidence/indicator_definition/cases.json
  - ../../tools/validators/evidence/validate_indicator_definition.py
  - ../../tests/validators/evidence/test_validate_indicator_definition.py
  - ../../docs/intake/exploratory/indicator-definition-source-map.md
tags: [kfm, evidence, analytics, indicator, denominator, missing-data, deterministic, fixture-only]
notes:
  - "Implements one bounded dependency named by Full Atlas KFM-TRIAD-030 / KFM-CAND-0090 and the AnalyticOutputDisclosureAssessment follow-up boundary."
  - "A definition declares method semantics only; it does not compute an indicator, resolve evidence, set policy thresholds, review, release, or publish."
[/KFM_META_BLOCK_V2] -->

# IndicatorDefinition Candidate

> A deterministic, fixture-only declaration for what one derived indicator means and how it must disclose its components, denominator, missing-data treatment, normalization, spatial/temporal support, and limits.

## Purpose

`AnalyticOutputDisclosureAssessment` already requires an `IndicatorDefinition` reference for an indicator result, but the referenced object family is not implemented on the pinned repository base. This packet fills only that declared-method seam.

An `IndicatorDefinition` records:

- a stable indicator key, label, description, value kind, unit, direction, and fixed `DERIVED` role;
- sorted component declarations with semantic role, allowed source roles, unit, and mandatory evidence requirement;
- opaque method and formula references;
- explicit aggregation, denominator, missing-data, normalization, percentile, and threshold-policy posture;
- spatial and temporal support requirements, including geography-version and valid-time discipline;
- mandatory uncertainty, missing-count, component, and interpretation-limit disclosure; and
- deterministic RFC 8785 JCS plus SHA-256 identity.

References remain opaque. The validator does not execute a formula, query data, resolve an EvidenceBundle, select a threshold, or calculate an indicator value.

## Indicator kinds and denominator rules

| Value kind | Denominator posture | Required method posture |
|---|---|---|
| `COUNT` | `NOT_APPLICABLE`; no denominator component | `COUNT` aggregation |
| `RATE`, `RATIO`, `PERCENT` | `REQUIRED`; exactly one denominator and at least one numerator | Matching aggregation |
| `INDEX` | `NOT_APPLICABLE`; no denominator component | Explicit non-`NONE` normalization |
| `CATEGORY` | `NOT_APPLICABLE`; no denominator component | Opaque threshold-policy reference |

The definition cannot encode an inline executable formula. `formula_ref` identifies separately reviewed method material. Category thresholds remain policy-owned; the definition may reference a threshold policy but cannot define or approve it.

## Missing data and composition

Missing data must use one explicit posture:

- `ABSTAIN` — no value when required support is missing;
- `EXCLUDE_WITH_DISCLOSURE` — exclude missing inputs and disclose missing counts/denominators; or
- `ZERO_ONLY_WITH_EVIDENCE` — treat zero as zero only when evidence establishes an observed zero.

Silent imputation is not representable. Every component declares allowed source roles, so upstream `DERIVED`, `MODELED`, or `INTERPRETIVE` analytics can retain their role rather than being relabeled as observations.

## Interpretation limits

Every definition requires:

- `NOT_ROOT_TRUTH`;
- `NOT_OBSERVATION`;
- `NO_CAUSAL_CLAIM`;
- `SCOPE_BOUND`; and
- `NO_PUBLICATION_AUTHORITY`.

These are disclosure constraints, not a policy decision. The governance block fixes execution to `FIXTURE_ONLY` and all evidence, policy, review, promotion, release, public-use, and publication effects to false.

## Deterministic identity

The validator removes only `definition_id` and `spec_hash`, canonicalizes the remaining object with RFC 8785 JCS, and computes SHA-256.

```text
spec_hash     = SHA-256(JCS(identity subject))
definition_id = kfm:indicator-definition:<first 24 digest hex>
```

Components sort by `component_ref`; each allowed-source-role array and the interpretation-limit array are unique and lexical. Order, duplicate, method, support, stored-identity, or authority drift fails closed.

## Directory Rules basis

Indicator method meaning belongs under `contracts/evidence/` because it defines the support and disclosure expectations for a derived analytic claim. Machine shape belongs under `schemas/contracts/v1/evidence/`; synthetic cases under `fixtures/contracts/v1/evidence/`; reusable validation under `tools/validators/evidence/`; executable evidence under `tests/validators/evidence/`; read-only orchestration under `.github/workflows/`; source reconciliation under `docs/intake/exploratory/`; and AI authoring accountability under `data/receipts/generated/`.

These are existing responsibility roots adopted by ADR-0029. The packet does not create an analytics root, dashboard authority, threshold-policy home, evidence store, runtime, public API, release lane, or publication path.

## Validation

```bash
python -m unittest -v tests.validators.evidence.test_validate_indicator_definition
python tools/validators/evidence/validate_indicator_definition.py --fixtures
```

## Non-effects and rollback

A passing fixture proves only local definition consistency. It does not prove any component, source, EvidenceBundle, formula, threshold, indicator result, validation report, policy decision, review, release, dashboard, or public output exists.

Before merge, close the draft pull request and delete its branch. After an authorized merge, revert the additive packet. No live computation, evidence, lifecycle state, policy, deployment, cache, release, or public artifact requires operational rollback.
