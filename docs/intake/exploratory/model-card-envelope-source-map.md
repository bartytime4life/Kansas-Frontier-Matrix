<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake-model-card-envelope-source-map
title: Governed ModelCardEnvelope source map
type: exploratory-source-map
version: v1.0.0
status: draft; source-bounded; PROPOSED implementation
owners:
  - OWNER_TBD model-governance steward
  - OWNER_TBD intake steward
created: 2026-08-07
updated: 2026-08-07
policy_label: internal-review; exploratory; model-card; no-source-activation
owning_root: docs/
responsibility: Record which attached model-card ideas were admitted, adapted, deferred, or rejected for the fixture-first ModelCardEnvelope slice.
truth_posture: CONFIRMED source and repository observations; PROPOSED adaptation; UNKNOWN model inventory and production adoption.
related:
  - ../../../contracts/governance/model_card_envelope.md
  - ../../../schemas/contracts/v1/governance/model_card_envelope.schema.json
  - ../../../fixtures/contracts/v1/governance/model_card_envelope/README.md
  - ../../../tools/validators/governance/model_card_envelope_core.py
  - ../../../tools/validators/governance/validate_model_card_envelope.py
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
[/KFM_META_BLOCK_V2] -->

# Governed `ModelCardEnvelope` source map

## Source seam

The attached `New Ideas 2.pdf` contains several model-card examples—environmental reconstruction, governed narrative reasoning, spatial alignment, and hydrology—with a repeated metadata shape: stable identity, review cadence, FAIR+CARE labels, STAC/DCAT/PROV profile references, provenance chains, signatures, attestations, SBOMs, telemetry, allowed uses, prohibited uses, and AI-transform permissions/prohibitions.

The same source also states model-specific limits. Environmental reconstruction is not forecasting or emergency alerting. Governed narrative output must remain evidence-linked, citation-bearing, sovereignty-aware, masked where required, and human-reviewed. Spatial alignment must not expose protected coordinates or perform sensitive cultural, archaeological-precision, or cadastral correction work.

The consolidated KFM atlas carries the same pressure as `KFM-P11-PROG-0001`: model cards should become machine-extractable governed artifacts with signatures, SBOM references, telemetry, permission/prohibition lists, and source-bound use limits. That atlas entry is proposal pressure, not proof that a live model-card registry exists.

## Current repository seam

Current-main inspection established:

- ADR-0029 adopts Directory Governance Standard v2 and the responsibility-root placement model;
- `contracts/governance/`, `schemas/contracts/v1/governance/`, governance fixtures, validators, and tests are active implementation lanes;
- the shared hashing package implements RFC 8785 JCS plus SHA-256 `spec_hash` behavior;
- `schemas/contracts/v1/ai/` is an index/compatibility lane rather than a second canonical DTO authority; and
- habitat model-card doctrine requires a model card, model-run receipt, uncertainty linkage, and an explicit modeled-not-observed boundary.

## Admitted ideas

| Source idea | Adaptation in this slice | Status |
|---|---|---|
| Machine-extractable model-card metadata | Strict shared `ModelCardEnvelope` schema and semantic contract | PROPOSED, fixture-first |
| Stable model and document identity | Deterministic IDs derived from model slug and semantic version | PROPOSED, enforced by validator |
| FAIR+CARE, rights, sensitivity, sovereignty | Explicit classification and finite governance fields | PROPOSED, declared-state validation only |
| STAC/DCAT/PROV alignment | Version/profile declarations plus digest-pinned bindings | PROPOSED; no remote dereference |
| Signature, attestation, SBOM, telemetry, metrics, drift, explainability | Required role-correct references with SHA-256 digests | PROPOSED; existence/authenticity not asserted |
| Provenance, evidence, review, correction, rollback | Required bindings and release-state consistency checks | PROPOSED; does not create those objects |
| Allowed/prohibited uses and transforms | Model-kind-specific minimum denials plus baseline safety prohibitions | PROPOSED, enforced by validator |
| Human and sovereignty review | Independent declared review flags and finite outcomes | PROPOSED; external review records remain authoritative |
| Reality boundary | Modeled/interpreted output cannot claim observation, operational, or publication authority | PROPOSED, enforced by schema |

## Deliberately adapted rather than copied

The PDF includes operational-sounding release stages, certification language, paths such as `mcp/model_cards/`, model metrics, model versions, dataset identifiers, and artifact references. This slice does **not** copy those as repository facts. It converts the reusable governance pattern into synthetic fixtures and labels all named model cases as non-evidentiary examples.

The shared object is placed under existing governance responsibility roots. No `mcp/` root, training pipeline, model registry, graph node, public API, or release artifact is introduced.

## Deferred candidates

These require separate evidence and review boundaries:

1. projection from an approved human model card into `ModelCardEnvelope`;
2. signature, SLSA, SBOM, telemetry, and catalog resolvers;
3. a reviewable model-card registry projection;
4. domain profiles for climate, hydrology, habitat, narrative, and spatial alignment;
5. governed Focus Mode consumption of released model cards; and
6. actual model evaluation and drift-policy gates.

## Rejected from this slice

- creating or training any model;
- asserting that a named model, metric, dataset, experiment, certification, signature, attestation, or release exists;
- live network access or source activation;
- autonomous publishing or policy/review approval;
- precise sensitive-coordinate handling; and
- treating a model card or validator pass as EvidenceBundle, proof, release, or public-use authority.

## Acceptance boundary

The slice is complete when synthetic PASS/HOLD/DENY cases and exact negative cases validate deterministically without network access, the generated authoring receipt binds all final repository bytes, and hosted CI reports the exact-head result. Production adoption remains a later governed decision.
