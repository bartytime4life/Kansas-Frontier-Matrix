<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/common/temporal-support-acceptance-assessment
title: TemporalSupportAcceptanceAssessment Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Temporal-data steward · Evidence steward · Map steward · Governed-AI steward · Validation steward
created: 2026-08-10
updated: 2026-08-10
owning_root: contracts/
policy_label: internal; common; temporal-support; cross-surface; acceptance-assessment
responsibility: Define a fixture-only cross-surface assessment of declared temporal support without resolving referenced objects, evaluating freshness policy, or creating lifecycle, review, release, or publication authority.
truth_posture: "CONFIRMED Pass 20 requirement and repository gap; PROPOSED inactive assessment; UNKNOWN consumer adoption and domain-specific time criteria; NEEDS VERIFICATION human review and hosted CI"
related:
  - ../evidence/temporal_support_assessment.md
  - ../data/layer_manifest.md
  - ../../schemas/contracts/v1/common/temporal_support_acceptance_assessment.schema.json
  - ../../fixtures/contracts/v1/common/temporal_support_acceptance_assessment/cases.json
  - ../../tools/validators/validate_temporal_support_acceptance_assessment.py
  - ../../tests/cross_domain/test_temporal_support_acceptance_assessment.py
  - ../../docs/intake/exploratory/pass-20-temporal-support-acceptance-source-map.md
tags: [kfm, common, temporal-support, cross-surface, fixture-only, no-network]
notes:
  - "Implements the smallest dependency-closed portion of Pass 20 EXP-013."
  - "The profile composes the existing TemporalSupportAssessment by reference and does not replace its query-specific semantics."
[/KFM_META_BLOCK_V2] -->

# TemporalSupportAcceptanceAssessment

`TemporalSupportAcceptanceAssessment` applies one closed, versioned declaration checklist across five subject families: tile artifacts, `LayerManifest`, `EvidenceBundle`, `PolicyDecision`, and governed AI envelopes. It closes the specific Pass 20 gap where the existing `TemporalSupportAssessment` evaluates evidence support for one query but does not provide a shared cross-surface acceptance profile.

## Criteria matrix

| Subject kind | Required declared dimensions |
|---|---|
| `TILE_ARTIFACT` | valid interval; retrieval time |
| `LAYER_MANIFEST` | valid interval; retrieval time |
| `EVIDENCE_BUNDLE` | valid interval; observation time; retrieval time |
| `POLICY_DECISION` | valid interval; as-of time |
| `AI_ENVELOPE` | valid interval; retrieval time; as-of time |

A released, corrected, or withdrawn subject also declares release time. Corrected or withdrawn subjects declare correction/withdrawal time. A public-surface candidate must bind a released or corrected posture plus an Evidence Drawer section and temporal caveat. Withdrawn subjects fail the bounded acceptance check.

The validator checks declaration presence and internal ordering only. It does not decide whether a source cadence, freshness TTL, time interval, correction, policy, or release is substantively correct.

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Required dimensions and cross-field declarations are locally coherent. |
| `ABSTAIN` | Subject, support reference, or assessment state remains unresolved. |
| `DENY` | A complete declaration is undated, inconsistent, withdrawn, under-disclosed, or hash-invalid. |
| `ERROR` | The packet is schema-invalid or explicitly declares an evaluation error. |

These outcomes do not authenticate referenced objects or grant evidence, policy, review, release, publication, or runtime authority.

## Directory Rules basis

This is a cross-surface semantic profile, so meaning belongs under `contracts/common/`; shape under `schemas/contracts/v1/common/`; public-safe synthetic replay under `fixtures/contracts/v1/common/`; executable validation under `tools/validators/`; cross-domain proof under `tests/cross_domain/`; orchestration under `.github/workflows/`; source reconciliation under `docs/intake/exploratory/`; and authoring accountability under `data/receipts/generated/`.

These are existing responsibility roots adopted by ADR-0029. The assessment references, rather than duplicates, the existing evidence-specific temporal assessment and surface object families.

## Validation

```bash
python -m unittest tests.cross_domain.test_temporal_support_acceptance_assessment -v
python tools/validators/validate_temporal_support_acceptance_assessment.py --fixtures
```

## Rollback

Revert the additive packet. It changes no subject object, timestamp, cache, source, evidence, policy, review, lifecycle, release, deployment, or public surface.
