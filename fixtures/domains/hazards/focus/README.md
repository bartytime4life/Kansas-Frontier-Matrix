<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/fixtures-domains-hazards-focus-readme
title: Hazards Focus Mode Fixture README
type: fixture-readme
version: v0.2
status: draft; documentation-only fixture lane; adjacent general Focus proof is not Hazards-specific fixture proof
owners:
  - OWNER_TBD — Hazards domain steward
  - OWNER_TBD — Focus Mode steward
  - OWNER_TBD — Fixture steward
  - OWNER_TBD — Validation steward
created: 2026-07-02
updated: 2026-08-31
policy_label: public-doc; fixtures; hazards; focus-mode; synthetic-only; no-network; finite-outcomes; release-gated
owning_root: fixtures/
responsibility: Document the reserved Hazards Focus fixture lane and its verified empty state without creating fixture payload, contract, schema, policy, runtime, release, or publication authority.
truth_posture: "CONFIRMED documentation-only lane containing README and .gitkeep only; CONFIRMED populated parent and sibling Hazards fixture indexes; CONFIRMED separate PROPOSED bounded-executable general Focus proof; NEEDS VERIFICATION Hazards-specific fixture shape, payloads, validator, consumers, stewardship, CI binding, and promotion enforcement"
tags: [kfm, fixtures, hazards, focus, synthetic, no-network, RuntimeResponseEnvelope, AIReceipt, ANSWER, ABSTAIN, DENY, ERROR]
related:
  - ../README.md
  - ../feature_resolver/README.md
  - ../drawer/README.md
  - ../golden/README.md
  - ../invalid/README.md
  - ../../../README.md
  - ../../../../docs/domains/hazards/API_CONTRACTS.md
  - ../../../../docs/domains/hazards/MAP_UI_CONTRACTS.md
  - ../../../../docs/architecture/hazards-trust-membrane.md
  - ../../../../contracts/domains/hazards/hazards_decision_envelope.md
  - ../../../../contracts/evidence/evidence_drawer_payload.md
  - ../../../../schemas/contracts/v1/focus/
  - ../../../../schemas/contracts/v1/runtime/
  - ../../../../schemas/contracts/v1/ai/
  - ../../../../policy/domains/hazards/
  - ../../../../release/manifests/README.md
  - ../../../../tests/runtime_proof/test_mock_adapter_finite_outcomes.py
  - ../../../../tests/runtime_proof/test_envelope_finite_outcomes.py
  - ../../../../.github/workflows/focus-mock-test.yml
notes:
  - "This directory currently contains README and .gitkeep only; it has no fixture payloads."
  - "The general Focus mock-adapter and finite-envelope profile remains PROPOSED and does not prove Hazards-specific fixture behavior."
  - "This documentation-only correction does not admit a source, create evidence, activate policy, promote lifecycle state, release, deploy, or publish."
[/KFM_META_BLOCK_V2] -->

# Hazards Focus Mode fixtures

`fixtures/domains/hazards/focus/`

Status: draft / DOCUMENTATION_ONLY / NO_FIXTURE_PAYLOADS.

This directory is reserved for small synthetic Focus Mode fixture examples for the Hazards domain. It currently contains only this README and `.gitkeep`; no fixture payloads exist here. Future examples may exercise bounded request and response shapes: toy map context, toy evidence references, toy prompt metadata, toy response envelopes, toy AI receipts, citation-check states, policy states, release states, correction states, rollback states, and finite outcomes.

These files are examples only. They are not source records, lifecycle data, EvidenceBundles, source descriptors, review approvals, release state, public API material, public map material, public tiles, AI authority, domain truth, or published artifacts.

## Focus posture

The Hazards API contract describes the Focus Mode surface as evidence-bounded synthesis over released evidence bundles. It may summarize, compare, explain limits, or draft review notes, but generated language remains interpretive and never root truth.

The documented Focus Mode response shape is `RuntimeResponseEnvelope` plus `AIReceipt`. Expected outcomes are `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR`. Concrete routes, DTO field enforcement, validators, policy runtime, fixture payloads, release artifacts, UI behavior, and CI/test coverage remain `NEEDS VERIFICATION`.

This fixture lane can support future checks, but fixture examples do not prove governed API behavior, AI runtime behavior, citation validation, EvidenceBundle closure, policy enforcement, release integration, UI implementation, or schema enforcement by themselves.

## Placement basis

This lane belongs under `fixtures/` because it contains synthetic examples and runtime/checking inputs. It is not a lifecycle data root, schema root, contract root, pipeline root, policy root, receipt root, proof root, release root, source-registry root, catalog root, triplet root, tile root, or publication root.

The root fixture README says `fixtures/` is for operational rendering inputs, not validator-only test data. It also says RAW, WORK, or QUARANTINE data, sensitive exact geometry, and canonical-truth treatment do not belong here. The parent Hazards fixture README is a populated navigation and boundary index; it is not proof that this child has payloads or consumers.

## Relationship to adjacent lanes

| Adjacent lane | Relationship |
|---|---|
| `../README.md` | Populated parent Hazards fixture navigation and boundary index. |
| `../feature_resolver/` | Resolver fixtures may provide bounded context inputs. |
| `../drawer/` | Drawer fixtures may provide context-handoff examples. |
| `../golden/` | Existing documentation-only Hazards expected-output lane. |
| `../invalid/` | Existing Hazards invalid-case index and placeholder families. |
| `../../../../docs/domains/hazards/API_CONTRACTS.md` | Focus Mode surface doctrine; this lane supplies examples only. |
| `../../../../docs/architecture/hazards-trust-membrane.md` | Trust-membrane and generated-language posture; this lane supplies examples only. |
| `../../../../schemas/contracts/v1/focus/` | Expected Focus Mode schema home; fixture success does not prove schema authority. |
| `../../../../policy/domains/hazards/` | Policy home; fixtures do not decide policy. |
| `../../../../release/manifests/` | Existing release-manifest root; fixtures do not approve publication. |

## Current inventory and adjacent proof

| Evidence | Status | What it proves | What it does not prove |
|---|---|---|---|
| This directory | CONFIRMED documentation-only | `README.md` and `.gitkeep` are the only tracked files. | No Hazards Focus fixture shape, payload, validator, consumer, or pass rate. |
| General Focus mock profile | CONFIRMED bounded executable / PROPOSED profile | Dedicated tests exercise deterministic mock-adapter and finite-envelope behavior in dedicated CI. | Not Hazards-specific fixture proof; no live route, provider, policy execution, evidence closure, release, or publication. |
| Parent and sibling Hazards fixture indexes | CONFIRMED present | Navigation and placement targets exist under the same `fixtures/` responsibility root. | Their presence does not populate or activate this lane. |

## Related references

- `../README.md`
- `../feature_resolver/README.md`
- `../drawer/README.md`
- `../golden/README.md`
- `../invalid/README.md`
- `../../../README.md`
- `../../../../docs/domains/hazards/API_CONTRACTS.md`
- `../../../../docs/domains/hazards/MAP_UI_CONTRACTS.md`
- `../../../../docs/architecture/hazards-trust-membrane.md`
- `../../../../contracts/domains/hazards/hazards_decision_envelope.md`
- `../../../../contracts/evidence/evidence_drawer_payload.md`
- `../../../../schemas/contracts/v1/focus/`
- `../../../../schemas/contracts/v1/runtime/`
- `../../../../schemas/contracts/v1/ai/`
- `../../../../policy/domains/hazards/`
- `../../../../release/manifests/README.md`
- `../../../../tests/runtime_proof/test_mock_adapter_finite_outcomes.py`
- `../../../../tests/runtime_proof/test_envelope_finite_outcomes.py`
- `../../../../.github/workflows/focus-mock-test.yml`
- `../../../../docs/doctrine/directory-rules.md`

## Accepted material

This lane may contain:

- small synthetic `*.input.json`, `*.valid.json`, `*.invalid.json`, `*.expected.json`, `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.svg`, or `*.md` examples;
- toy Focus Mode requests with map context, evidence refs, question text, access posture, source-role context, and temporal scope;
- toy `RuntimeResponseEnvelope` and `AIReceipt` outputs using `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`;
- toy citation-validation, visible-limitations, policy-state, release-state, freshness-state, correction-state, rollback-state, and boundary-label examples;
- toy review-note drafts where clearly labeled as draft/support material;
- paired expected outputs in a future Hazards `golden/` lane when behavior becomes stable.

## Exclusions

Do not use this lane for real records, source exports, lifecycle data, EvidenceBundles, actual source descriptors, proof packs, release manifests, implementation code, public API material, public map material, public tiles, direct model runtime output, AI authority, source authority, policy authority, release authority, or published artifacts.

## Fixture design rules

- Keep examples synthetic, compact, deterministic, reviewable, and public-safe.
- Use toy IDs, toy map-context refs, toy feature refs, toy evidence refs, toy citation refs, toy prompt refs, toy timestamps, toy digests, and toy hashes.
- Make Focus posture explicit: `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, stale, expired, missing evidence, failed citation validation, conflicting source roles, unsupported inference, release-blocked, correction-visible, rollback-visible, or boundary-labeled.
- Keep source role, evidence state, citation state, policy state, release state, freshness state, temporal scope, visible limitations, AI receipt state, correction state, rollback state, and expected outcome explicit where material.
- Pair each input with an expected output when practical.
- Keep schema validity, semantic validity, evidence support, citation validation, policy filtering, release posture, freshness posture, source-role validity, AI receipt completeness, trust-membrane safety, drawer handoff, and resolver context separate.
- Do not treat fixture success as EvidenceBundle closure, source authority, policy approval, release state, AI correctness proof, API implementation proof, public-map authority, or published output.

## Verification status

- Target README: populated documentation; current lane remains documentation-only.
- Parent Hazards fixture README: CONFIRMED populated navigation and boundary index.
- Fixture payload inventory: CONFIRMED no payloads; this directory contains only README and `.gitkeep`.
- Hazards Focus Mode API alignment: PARTIALLY VERIFIED against `docs/domains/hazards/API_CONTRACTS.md`.
- Hazards trust-membrane alignment: PARTIALLY VERIFIED against `docs/architecture/hazards-trust-membrane.md`.
- Hazards feature-resolver fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hazards/feature_resolver/README.md`.
- Hazards drawer fixture alignment: PARTIALLY VERIFIED against `fixtures/domains/hazards/drawer/README.md`.
- Root fixture alignment: PARTIALLY VERIFIED against `fixtures/README.md`.
- General Focus mock and finite-envelope proof: CONFIRMED separate bounded executable profile; remains PROPOSED and is not Hazards-specific fixture proof.
- Consumer alignment: NEEDS VERIFICATION against Hazards-specific validators, Focus Mode checks, governed-API tests, drawer handoff checks, feature-resolver checks, release-readiness checks, schema checks, policy checks, AIReceipt checks, citation-validation checks, and UI implementation.
- Hazards-specific fixture tests and validators: NOT AVAILABLE while this lane has no payloads or consumers.
