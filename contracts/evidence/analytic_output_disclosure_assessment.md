<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/evidence/analytic-output-disclosure-assessment
title: AnalyticOutputDisclosureAssessment Candidate Contract
type: semantic-contract
version: v0.1.0
status: proposed; inactive; fixture-only; review-required
owners: OWNER_TBD — Evidence steward · Analytics steward · Model-governance steward · Validation steward
created: 2026-08-09
updated: 2026-08-09
policy_label: internal; evidence; analytics; disclosure; no-network
owning_root: contracts/
responsibility: Define a bounded output-level assessment that keeps one statistic, indicator, model output, model interpretation, or planning scenario subordinate to evidence, method, assumptions, uncertainty, validation, confidence, and interpretation limits.
truth_posture: CONFIRMED source and repository gap / PROPOSED inactive assessment / NEEDS VERIFICATION steward adoption and hosted exact-head execution
related:
  - ./evidence_bundle.md
  - ../governance/model_card_envelope.md
  - ../runtime/run_receipt.md
  - ../data/validation_report.md
  - ../../schemas/contracts/v1/evidence/analytic_output_disclosure_assessment.schema.json
  - ../../fixtures/contracts/v1/evidence/analytic_output_disclosure_assessment/cases.json
  - ../../tools/validators/evidence/validate_analytic_output_disclosure_assessment.py
  - ../../tests/validators/evidence/test_validate_analytic_output_disclosure_assessment.py
  - ../../docs/intake/exploratory/analytic-output-disclosure-assessment-source-map.md
tags: [kfm, evidence, analytics, interpretation, disclosure, uncertainty, fixture-only]
notes:
  - "Adapts Full Atlas KFM-TRIAD-030 / KFM-CAND-0088 through KFM-CAND-0090 and retained analysis-as-interpretation lineage."
  - "The profile assesses one output disclosure; it does not create evidence, evaluate a model, decide policy, approve review, release, or publish."
[/KFM_META_BLOCK_V2] -->

# AnalyticOutputDisclosureAssessment Candidate

> A deterministic, fixture-only assessment that makes the support and limits of one analytic output inspectable without turning the output, its score, or its model language into root truth.

## Purpose

The repository already has independent families for EvidenceBundle, ModelCardEnvelope, run receipts, validation reports, environmental indicator evidence, model cards, source-role transitions, and representation fitness. The missing seam is an output-level disclosure that binds one concrete analytic result to those families without copying or replacing them.

`AnalyticOutputDisclosureAssessment` records:

- the analytic output identity, kind, source role, support state, scope, and valid time;
- each input's source role, EvidenceBundle reference, and source-lineage reference;
- a method reference and kind-specific IndicatorDefinition, FeatureSetManifest, ModelCardEnvelope, ModelRunReceipt, and training-lineage references;
- explicit assumption references;
- uncertainty identity and class;
- validation status and ValidationReport reference;
- confidence class, citations, and interpretation-limit codes;
- a finite `PASS`, `ABSTAIN`, `DENY`, or `ERROR` result; and
- deterministic JCS plus SHA-256 identity.

Every reference remains opaque. This validator does not resolve evidence, run a model, recompute a statistic, authenticate a receipt, or verify a citation.

## Analytic kinds and source roles

| Analytic kind | Required output role | Additional bindings |
|---|---|---|
| `STATISTIC` | `DERIVED` | Method, assumptions, uncertainty, validation, citations, limits. |
| `INDICATOR` | `DERIVED` | `IndicatorDefinition` plus the common disclosure. |
| `ML_MODEL` | `MODELED` | `FeatureSetManifest`, `ModelCardEnvelope`, `ModelRunReceipt`, and training lineage. |
| `MODEL_INTERPRETATION` | `INTERPRETIVE` | `ModelCardEnvelope` and `ModelRunReceipt`. |
| `PLANNING_SCENARIO` | `INTERPRETIVE` | Scenario assumptions plus `NO_AUTOMATED_RECOMMENDATION`. |

`OBSERVED` is not an allowed output role. Promotion or presentation cannot silently upgrade `DERIVED`, `MODELED`, or `INTERPRETIVE` output into observation evidence.

## Support states

| Support state | Assessment outcome | Meaning |
|---|---|---|
| `SUPPORTED` | `PASS` | Every input has an EvidenceBundle reference; validation passed with a report; uncertainty is named; confidence is resolved; citations and required limits are present. |
| `PARTIAL` | `ABSTAIN` | At least one support dimension remains incomplete and the output says so. |
| `UNSUPPORTED` | `ABSTAIN` | Support is insufficient for a bounded analytic claim; no fallback fact is invented. |
| `ERROR` | `ERROR` | The bounded assessment could not complete safely. |

A `SUPPORTED` overclaim with missing evidence, validation, uncertainty, confidence, citations, or required limits is `DENY`. A fully closed packet cannot call itself `PARTIAL` or `UNSUPPORTED` merely to avoid a stronger review path.

## Interpretation limits

Every output requires:

- `NOT_ROOT_TRUTH`;
- `NOT_OBSERVATION`;
- `SCOPE_BOUND`; and
- `NO_PUBLICATION_AUTHORITY`.

Statistics, indicators, and planning scenarios also require `NO_CAUSAL_CLAIM`. ML and model-interpretation outputs require `MODEL_LIMITS_APPLY`. Planning scenarios additionally require `NO_AUTOMATED_RECOMMENDATION`.

These are disclosure claims, not policy decisions. The governance block fixes policy evaluation, review approval, release, public use, and publication to false.

## Deterministic identity

The validator computes RFC 8785 JCS plus SHA-256 over the complete object after removing only `assessment_id` and `spec_hash`.

```text
spec_hash      = SHA-256(JCS(identity subject))
assessment_id  = kfm:analytic-output-disclosure:<first 24 digest hex>
```

Input bindings sort by `input_ref`; assumption, citation, and limit arrays are unique and lexical. Order, duplicate, stored-decision, or identity drift fails closed.

## Directory Rules basis

This object assesses evidence support for a derived or interpretive output, so meaning belongs under `contracts/evidence/`; shape under `schemas/contracts/v1/evidence/`; synthetic cases under `fixtures/contracts/v1/evidence/`; reusable validation under `tools/validators/evidence/`; executable evidence under `tests/validators/evidence/`; read-only orchestration under `.github/workflows/`; source adaptation under `docs/intake/exploratory/`; and AI authoring accountability under `data/receipts/generated/`.

These are existing responsibility roots adopted by ADR-0029. No analytics root, model store, evidence store, policy home, release lane, public API, UI surface, or publication path is created.

## Validation

```bash
python -m unittest -v tests.validators.evidence.test_validate_analytic_output_disclosure_assessment
python tools/validators/evidence/validate_analytic_output_disclosure_assessment.py --fixtures
```

## Non-effects and rollback

A passing fixture proves only local disclosure consistency. It does not prove an input, source, EvidenceBundle, method, IndicatorDefinition, FeatureSetManifest, ModelCardEnvelope, ModelRunReceipt, training lineage, uncertainty artifact, validation report, citation, policy decision, review, release, or public output exists.

Before merge, close the draft pull request and delete its branch. After an authorized merge, revert the additive packet. No live analysis, model, evidence, lifecycle state, policy decision, release, deployment, cache, or public artifact requires operational rollback.
