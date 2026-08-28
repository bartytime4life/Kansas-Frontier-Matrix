<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-joins-agriculture-soil-readme
title: tools/validators/joins/agriculture-soil README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-join-steward-plus-agriculture-steward-plus-soil-steward-plus-schema-steward-plus-policy-steward-plus-evidence-steward-plus-release-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; joins-validator; agriculture-soil; cross-domain-validator; MUKEY; COKEY; CHKEY; source-role-aware; support-type-aware; release-gated; non-authoritative
owning_root: tools/
responsibility: shared Agriculture-Soil join validator routing lane under tools/validators/joins for checking MUKEY/COKEY/CHKEY continuity, Soil-owned EvidenceRef consumption, Agriculture-owned derivative boundaries, support-type separation, source-role anti-collapse, sensitivity and public-surface posture, evidence/proof linkage, policy/review/release linkage, correction cascade, rollback support, and finite validation outcomes while deferring Agriculture meaning, Soil meaning, schemas, policy decisions, evidence records, receipts, lifecycle data, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../../README.md
  - ../../_common/README.md
  - ../../cross-domain-joins/README.md
  - ../../cross-lane/README.md
  - ../../domains/agriculture/README.md
  - ../../domains/agriculture/soil-join/README.md
  - ../../domains/soil/README.md
  - ../../agriculture/README.md
  - ../../soil/README.md
  - ../../../../docs/domains/agriculture/README.md
  - ../../../../docs/domains/agriculture/CROSS_LANE.md
  - ../../../../docs/domains/agriculture/OBJECTS.md
  - ../../../../docs/domains/agriculture/POLICY.md
  - ../../../../docs/domains/agriculture/VERIFICATION_BACKLOG.md
  - ../../../../docs/domains/soil/README.md
  - ../../../../docs/domains/soil/ARCHITECTURE.md
  - ../../../../docs/domains/soil/CANONICAL_PATHS.md
  - ../../../../docs/domains/soil/DATA_LIFECYCLE.md
  - ../../../../contracts/domains/agriculture/
  - ../../../../contracts/domains/soil/
  - ../../../../schemas/contracts/v1/domains/agriculture/
  - ../../../../schemas/contracts/v1/domains/soil/
  - ../../../../schemas/contracts/v1/joins/agriculture-soil/
  - ../../../../schemas/contracts/v1/joins/agriculture_soil/
  - ../../../../policy/domains/agriculture/
  - ../../../../policy/domains/soil/
  - ../../../../data/registry/sources/agriculture/
  - ../../../../data/registry/sources/soil/
  - ../../../../data/proofs/evidence_bundle/
  - ../../../../data/proofs/
  - ../../../../data/receipts/
  - ../../../../release/
notes:
  - "This README replaces an empty file at tools/validators/joins/agriculture-soil/README.md. It does not confirm executable validator code."
  - "tools/validators/domains/agriculture/soil-join/ already documents the Agriculture-facing Agriculture x Soil join validator lane. This joins/ path is shared join routing, not a competing Agriculture-domain child authority."
  - "Agriculture consumes Soil-owned objects by EvidenceRef. Agriculture must not re-publish Soil objects as Agriculture canonical truth."
  - "The load-bearing Agriculture x Soil join key is MUKEY; unresolved MUKEY should produce ABSTAIN or review, not fabricated suitability or geometry-snapped identity."
  - "Soil support types, source roles, MUKEY/COKEY/CHKEY identity, evidence closure, policy posture, release references, correction paths, and rollback targets must remain visible across joins."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/joins/agriculture-soil

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-agriculture--soil--join-informational)
![join](https://img.shields.io/badge/join-MUKEY-blueviolet)
![authority](https://img.shields.io/badge/authority-routing--lane-lightgrey)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/joins/agriculture-soil/` is the shared Agriculture × Soil join validator routing lane for MUKEY/COKEY/CHKEY continuity, Soil-owned evidence consumption, Agriculture-owned derivatives, source-role discipline, support-type separation, release readiness, correction cascade, rollback support, and public-surface denial.

---

## Purpose

`tools/validators/joins/agriculture-soil/` exists to make Agriculture × Soil join validation visible at the shared join layer without moving Agriculture meaning, Soil meaning, schemas, policy, evidence, receipts, fixtures, lifecycle data, or release authority into a validator folder.

The durable KFM question for this lane is:

> Does an Agriculture × Soil candidate consume Soil-owned objects through governed EvidenceRefs, preserve MUKEY/COKEY/CHKEY identity, preserve Soil support type and source role, produce only Agriculture-owned derivatives, and include the evidence, policy, review, release, correction, rollback, and public-surface safeguards required for its intended use?

The answer should be a deterministic validation result or routing decision. This folder should not create Agriculture truth, Soil truth, SoilMapUnit truth, field-level truth, suitability truth, EvidenceBundles, receipts, proofs, PolicyDecisions, ReleaseManifests, public map layers, API payloads, AI answers, or publication approval.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/joins/agriculture-soil/README.md` | **CONFIRMED README** | This README replaces the previous empty file. |
| Agriculture-facing soil-join validator lane | **CONFIRMED README / executable NEEDS VERIFICATION** | `tools/validators/domains/agriculture/soil-join/README.md` documents the Agriculture-facing join lane and MUKEY/EvidenceRef posture. |
| Per-domain Agriculture validator index | **CONFIRMED README / executable NEEDS VERIFICATION** | `tools/validators/domains/agriculture/README.md` routes edge-specific Agriculture validators and identifies `soil-join/` as a child lane. |
| Per-domain Soil validator index | **CONFIRMED README / executable NEEDS VERIFICATION** | `tools/validators/domains/soil/README.md` preserves Soil support-type separation, source-role discipline, MUKEY/COKEY/CHKEY continuity, evidence, policy, release, correction, rollback, and public-surface boundaries. |
| Shared join schema home | **NEEDS VERIFICATION** | Candidate homes include `schemas/contracts/v1/joins/agriculture-soil/` and `schemas/contracts/v1/joins/agriculture_soil/`; exact accepted schema path and field-level contents were not verified in this edit. |
| Executables, registry wiring, fixtures, schema bindings, policy bundles, report destinations, receipt emission, runtime behavior, and CI wiring | **NEEDS VERIFICATION** | This README does not claim a runnable validator, test suite, receipt path, runtime route, or CI check exists. |

[Back to top](#top)

---

## Relationship to nearby lanes

| Concern | Preferred home | Boundary |
|---|---|---|
| Shared Agriculture × Soil join validation | `tools/validators/joins/agriculture-soil/` | Shared join routing lane; does not define domain meaning. |
| Agriculture-facing Agriculture × Soil edge validation | `tools/validators/domains/agriculture/soil-join/` | Agriculture-owned derivative and Agriculture-domain edge posture. |
| Agriculture per-domain validator index | `tools/validators/domains/agriculture/` | Edge-specific Agriculture validator routing. |
| Soil per-domain validator index | `tools/validators/domains/soil/` | Soil support type, source role, identity, lineage, evidence, release, and public-surface posture. |
| Generic cross-domain join invariants | `tools/validators/cross-domain-joins/`, `tools/validators/cross-lane/` | Shared anti-collapse and routing invariants. |
| Agriculture and Soil meaning | `docs/domains/agriculture/`, `docs/domains/soil/`, `contracts/domains/agriculture/`, `contracts/domains/soil/` | Contracts/docs define meaning; validators check conformance. |
| Machine shape | `schemas/contracts/v1/domains/agriculture/`, `schemas/contracts/v1/domains/soil/`, accepted join schema homes | Schemas define shape; this folder does not. |
| Policy and release posture | `policy/domains/agriculture/`, `policy/domains/soil/`, `release/` | Validator reports gaps; does not decide policy or release. |
| Evidence/proof support | `data/proofs/evidence_bundle/`, `data/proofs/` | Validator checks references; does not create proof authority. |
| Receipts | `data/receipts/` | Receipts remain separate from validator docs. |

[Back to top](#top)

---

## Join invariants

| Invariant | Validator expectation | Fail / abstain condition |
|---|---|---|
| Soil ownership preserved | Soil objects remain Soil-owned and are cited by EvidenceRef. | SoilMapUnit, SoilComponent, Horizon, SoilProperty, Hydrologic Soil Group, Pedon, or SuitabilityRating is republished as Agriculture canonical truth. |
| Agriculture derivative preserved | Agriculture may produce Agriculture-owned derivatives such as crop suitability, stress, or management-context summaries when supported. | Derivative is presented as raw Soil truth, direct field truth, or unreviewed public fact. |
| MUKEY resolves | MUKEY is preserved verbatim from Soil admission and resolves for the join. | MUKEY is missing, malformed, fabricated, geometry-derived only, stale, or unresolved. |
| COKEY/CHKEY continuity | Component/horizon identifiers remain visible where component or horizon joins are material. | COKEY/CHKEY are dropped, synthesized, or used outside verified scope. |
| Support type preserved | Soil static survey, gridded derivative, station observation, satellite grid, pedon/profile, interpretation, and public-safe derivative support types remain separate. | Support types collapse into generic Agriculture truth. |
| Source role preserved | Soil observed, regulatory, modeled, aggregate, candidate, and public-safe roles remain visible across the join. | Pedon observed data, SSURGO regulatory context, or gridded derivative context is relabeled as generic Agriculture modeled truth. |
| Sensitivity preserved | Public output stays aggregate/public-safe; field-level or operator-adjacent joins follow deny/default or review posture. | Private, field-level, operator-adjacent, or sensitive details are surfaced publicly without aggregation, redaction, review, and release support. |
| Evidence and release support | Public-bound Agriculture derivative carries EvidenceBundle, policy, review, release, correction, and rollback references where required. | Output is published, mapped, exported, searched, graphed, summarized, or answered without required trust artifacts. |
| Correction cascade | Soil-side correction, withdrawal, stale-state, source update, or EvidenceBundle invalidation propagates to Agriculture derivatives. | Agriculture derivative remains published or treated as current after Soil-side correction without review. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Shared Agriculture × Soil join validator routing | `tools/validators/joins/agriculture-soil/` |
| Agriculture-facing soil-join validator | `tools/validators/domains/agriculture/soil-join/` |
| Agriculture per-domain validator index | `tools/validators/domains/agriculture/` |
| Soil per-domain validator index | `tools/validators/domains/soil/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Cross-domain invariant validators | `tools/validators/cross-domain-joins/`, `tools/validators/cross-lane/` |
| Agriculture domain meaning | `docs/domains/agriculture/`, `contracts/domains/agriculture/` |
| Soil domain meaning and Soil-owned objects | `docs/domains/soil/`, `contracts/domains/soil/` |
| Agriculture and Soil schemas | `schemas/contracts/v1/domains/agriculture/`, `schemas/contracts/v1/domains/soil/`, accepted join schema homes |
| Policy rules | `policy/domains/agriculture/`, `policy/domains/soil/`, accepted policy homes |
| Source descriptors | `data/registry/sources/agriculture/`, `data/registry/sources/soil/`, accepted source registry homes |
| EvidenceBundles and proof support | `data/proofs/evidence_bundle/`, `data/proofs/` |
| Receipts | `data/receipts/` |
| Release decisions, manifests, rollback, corrections, withdrawal | `release/` |
| Tests and fixtures | `tests/validators/joins/agriculture-soil/`, `tests/validators/domains/agriculture/soil-join/`, `fixtures/domains/agriculture/`, `fixtures/domains/soil/`, or accepted conventions |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live here when it checks declared Agriculture × Soil join invariants and delegates meaning, schemas, policy, evidence, receipts, lifecycle data, and release authority to owning roots.
- **NEEDS VERIFICATION:** exact executable names, schema homes, source descriptors, fixtures, policy bundles, report destinations, receipt emission, runtime behavior, release integration, and CI wiring.
- **DENY:** using this folder as Agriculture doctrine, Soil doctrine, schema home, policy home, source registry, evidence store, lifecycle data store, proof store, receipt store, release record store, public runtime surface, field-level publication surface, AI answer authority, or domain-meaning authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/joins/agriculture-soil/` include checks that:

- validate MUKEY presence, shape, preservation, and resolvability for Agriculture × Soil joins;
- preserve COKEY and CHKEY where component/horizon joins are material;
- reject geometry-only joins that invent Soil identity without governed Soil evidence;
- require Agriculture candidates to cite Soil-owned EvidenceRefs instead of copying Soil objects into Agriculture authority;
- require Agriculture-owned derivatives to remain clearly derived, modeled, reviewed, and release-scoped;
- preserve Soil source-role labels, especially observed Pedon data, SSURGO/regulatory context, gridded derivatives, and interpretation support;
- preserve Soil support-type separation across the Agriculture join;
- require aggregation, redaction, review, and release support before field-level, operator-adjacent, or sensitive joins reach public surfaces;
- downgrade, abstain, or route to review when Soil-side correction, revocation, stale source, unresolved EvidenceBundle, or missing policy invalidates the join;
- check release references, rollback targets, and correction propagation for public-bound Agriculture derivatives.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/joins/agriculture-soil/` | Correct home |
|---|---|
| Agriculture contracts or doctrine | `contracts/domains/agriculture/`, `docs/domains/agriculture/` |
| Soil contracts or doctrine | `contracts/domains/soil/`, `docs/domains/soil/` |
| Schemas, DTOs, enums, or join machine shape | `schemas/contracts/v1/...` |
| Policy rules, thresholds, release gates, or steward decisions | `policy/...`, `release/` |
| Source descriptors | `data/registry/sources/...` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| EvidenceBundles, proofs, receipts, ValidationReports | `data/proofs/`, `data/receipts/`, accepted report lanes |
| Release manifests, decisions, rollback cards, corrections, withdrawals | `release/` |
| Generated QA reports that are not source code | `artifacts/qa/` or accepted report lane |
| Tests and fixtures | `tests/` and `fixtures/` conventions |
| Public API, UI, map, tile, export, search, graph, Focus Mode, field-level publication, private/operator-facing output, or AI runtime code | governed application/runtime roots |

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `AGRICULTURE_SOIL_JOIN_PASS` | Candidate passed configured Agriculture × Soil join checks. |
| `AGRICULTURE_SOIL_JOIN_FAIL` | Candidate failed one or more configured checks. |
| `ROUTE_TO_AGRICULTURE_SOIL_JOIN_DOMAIN_LANE` | Candidate should be checked by `tools/validators/domains/agriculture/soil-join/`. |
| `ROUTE_TO_SOIL_VALIDATOR` | Candidate needs Soil-side validation before Agriculture can consume it. |
| `ROUTE_TO_CROSS_DOMAIN_JOIN_VALIDATOR` | Candidate needs generic cross-domain join invariant checks. |
| `MUKEY_MISSING` | Required MUKEY is absent. |
| `MUKEY_UNRESOLVED` | MUKEY does not resolve to governed Soil evidence. |
| `MUKEY_FABRICATED_OR_GEOMETRY_ONLY` | Soil identity was fabricated, inferred only from geometry, or snapped without governed Soil evidence. |
| `COKEY_CHKEY_CONTEXT_MISSING` | Component/horizon context is required but missing or unverified. |
| `SOIL_OWNERSHIP_COLLAPSE` | Soil-owned object is republished as Agriculture canonical truth. |
| `AGRICULTURE_DERIVATIVE_OVERCLAIM` | Agriculture derivative is presented as raw Soil truth, direct field truth, or unreviewed public fact. |
| `SOURCE_ROLE_COLLAPSE` | Soil observed, regulatory, modeled, aggregate, candidate, or public-safe role is hidden or relabeled. |
| `SUPPORT_TYPE_COLLAPSE` | Soil support type separation is lost. |
| `SENSITIVITY_OR_PUBLIC_SURFACE_GAP` | Field-level, private, operator-adjacent, or sensitive join lacks aggregation/redaction/review/release support. |
| `EVIDENCE_REF_MISSING` | Required Soil-owned EvidenceRef or EvidenceBundle pointer is absent. |
| `REVIEW_OR_POLICY_GAP` | Required review state or PolicyDecision is absent. |
| `RELEASE_REFERENCE_MISSING` | Required ReleaseManifest, correction path, rollback target, or withdrawal path is absent. |
| `CORRECTION_CASCADE_MISSING` | Soil-side correction, withdrawal, stale-state, or invalidation did not propagate to Agriculture derivative. |
| `VALIDATOR_SYSTEM_ERROR` | Validator could not complete because of malformed input, missing dependency, missing registry entry, or unexpected runtime error. |

[Back to top](#top)

---

## Minimal future implementation sketch

Future implementation should remain small and reversible:

```text
tools/validators/joins/agriculture-soil/
├── README.md
├── validate_agriculture_soil_join.py    # PROPOSED; not confirmed
└── registry_notes.md                    # PROPOSED; documentation only
```

If `validate_agriculture_soil_join.py` is added, it should delegate domain meaning, schemas, policy, evidence, fixtures, receipts, and release checks to accepted Agriculture, Soil, cross-domain, and shared validator homes. It should not redefine domain meaning, copy schemas, copy policy, store fixtures, write lifecycle data, approve release, or publish public outputs.

[Back to top](#top)

---

## Acceptance checklist

This README is complete for documentation purposes when:

- [x] It replaces the empty file at `tools/validators/joins/agriculture-soil/README.md`.
- [x] It marks this path as a shared Agriculture × Soil join validator routing lane, not Agriculture or Soil authority.
- [x] It distinguishes the shared joins lane from `tools/validators/domains/agriculture/soil-join/`.
- [x] It preserves MUKEY/COKEY/CHKEY continuity, Soil ownership, Agriculture derivative boundaries, source-role discipline, support-type separation, sensitivity, evidence, policy, release, correction, rollback, and public-surface denial posture.
- [x] It routes machine shape, policy, fixtures, evidence, receipts, release, lifecycle data, tests, and domain meaning to their owning roots.
- [x] It marks executable behavior, registry wiring, schema bindings, policy bundles, fixture files, receipt emission, runtime behavior, and CI wiring as **NEEDS VERIFICATION**.

Future implementation is not complete until:

- [ ] Validator registry or CLI references to `joins/agriculture-soil` are searched and classified.
- [ ] Accepted schema homes, policy homes, fixture homes, test paths, and report destinations are verified.
- [ ] Tests exercise valid and invalid MUKEY, COKEY/CHKEY, EvidenceRef, source-role, support-type, sensitivity, correction-cascade, release, and public-surface cases.
- [ ] CI invokes the relevant Agriculture × Soil join validators in deterministic order.
- [ ] Any generated validation outputs write only to accepted report, proof, receipt, or artifact roots.

[Back to top](#top)

---

## Changelog

| Date | Change | Status |
|---|---|---|
| 2026-07-08 | Replaced empty README with shared Agriculture × Soil join validator routing documentation. | **CONFIRMED README / implementation NEEDS VERIFICATION** |
