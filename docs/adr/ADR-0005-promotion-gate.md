<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/TODO-NEEDS-UUID
title: ADR-0005: Promotion Gate
type: standard
version: v1
status: draft
owners: TODO-NEEDS-CODEOWNERS
created: TODO-NEEDS-CREATED-DATE
updated: 2026-04-27
policy_label: TODO-NEEDS-POLICY-LABEL
related: [docs/adr/README.md, docs/governance/promotion-gate.md, docs/architecture/evidence-flow.md, docs/governance/cite-or-abstain.md, schemas/contracts/v1/promotion/promotion_decision.schema.json, schemas/contracts/v1/release/release_manifest.schema.json, schemas/contracts/v1/evidence/evidence_bundle.schema.json, schemas/contracts/v1/catalog/catalog_matrix.schema.json, policy/promotion/README.md, tools/validators/promotion_gate/README.md, data/receipts/README.md, data/proofs/README.md]
tags: [kfm, adr, promotion, governance, release, evidence, proof, rollback]
notes: [Target path docs/adr/ADR-0005-promotion-gate.md; target file presence was not verified in the current workspace; related paths are doctrine-derived and need checkout verification; doc_id, owners, created date, and policy label remain review placeholders.]
[/KFM_META_BLOCK_V2] -->

# ADR-0005: Promotion Gate

Make publication a governed, evidence-bearing state transition rather than a file move.

![Status](https://img.shields.io/badge/status-draft-lightgrey)
![ADR](https://img.shields.io/badge/ADR-0005-blue)
![Decision](https://img.shields.io/badge/decision-proposed-orange)
![Posture](https://img.shields.io/badge/posture-fail--closed-0a7ea4)
![Scope](https://img.shields.io/badge/scope-release%20promotion-6f42c1)

> [!IMPORTANT]
> **Status:** draft / NEEDS VERIFICATION  
> **Path:** `docs/adr/ADR-0005-promotion-gate.md`  
> **Decision posture:** PROPOSED until the active repository confirms existing ADR numbering, owners, schema homes, workflow names, and promotion tooling.

## Quick jumps

[Decision](#decision) · [Context](#context) · [Scope](#scope) · [Gate model](#gate-model) · [Outcome grammar](#outcome-grammar) · [Trust object split](#trust-object-split) · [Implementation contract](#implementation-contract) · [Validation](#validation) · [Rollback](#rollback) · [Open verification](#open-verification)

---

## Decision

KFM adopts a **Promotion Gate** as the mandatory governance membrane between release candidates and the `PUBLISHED` state.

Promotion is not a copy operation, a successful build, a UI action, a model answer, or a file move. Promotion is a controlled state transition that evaluates whether a candidate artifact, claim surface, layer, dataset, bundle, or release object may become externally relied upon.

The Promotion Gate must produce one finite promotion decision:

| Decision | Meaning |
|---|---|
| `PROMOTE` | Required gates pass, obligations are satisfied, and the candidate may become the active published release. |
| `ABSTAIN` | The gate lacks enough evidence to promote or deny safely; the candidate remains unpublished until obligations are resolved. |
| `DENY` | The candidate conflicts with policy, rights, evidence, integrity, sensitivity, review, or release requirements. |
| `ERROR` | The evaluator, schema, contract, runtime, or verification step failed before a trustworthy decision could be made. |

> [!NOTE]
> Runtime answer outcomes such as `ANSWER` are not promotion outcomes. Promotion governs publication state. Runtime envelopes govern user-facing response behavior.

---

## Context

KFM’s core truth path is:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

The Promotion Gate protects the final transition into `PUBLISHED`.

A release candidate may already be useful, indexed, rendered, or internally reviewable before promotion. That does not make it public truth. `PROCESSED` artifacts remain unpublished. `CATALOG` and `TRIPLET` surfaces provide discoverability and linkage. `PUBLISHED` is the release state where outward-facing clients, maps, Focus Mode, Evidence Drawer payloads, exports, and semi-public users may rely on the artifact or claim.

### Why this ADR exists

KFM needs a stable answer to five recurring design pressures:

1. How does a release candidate become public without bypassing evidence?
2. What blocks promotion when evidence, rights, sensitivity, or policy is incomplete?
3. How do receipts, proofs, manifests, catalogs, and decisions stay distinct?
4. How does rollback happen without deleting evidence or hiding correction lineage?
5. How do UI and AI surfaces know whether a claim is release-safe?

This ADR makes the release boundary explicit.

---

## Scope

### Applies to

The Promotion Gate applies to release-significant objects and surfaces, including:

- dataset releases
- overlay releases
- map layer descriptors
- PMTiles / COG / GeoParquet / other spatial artifacts
- source-derived public products
- Evidence Drawer payloads that support consequential claims
- release manifests
- catalog matrices and provenance closures
- runtime fixtures when they assert published behavior
- public-safe derived surfaces
- rollback and correction transitions

### Does not apply to

The Promotion Gate is not a substitute for:

- source intake validation
- raw ingest quarantine rules
- schema validation during development
- local preview rendering
- model inference
- human review alone
- CI success alone
- signing alone
- emergency alerting or operational life-safety systems

Those may feed the gate, but they do not replace it.

---

## Decision summary

| Area | Decision |
|---|---|
| Promotion boundary | `PUBLISHED` requires an explicit Promotion Gate decision. |
| Candidate identity | Every candidate must have stable identity anchored by `spec_hash` or an equivalent approved canonical hash. |
| Gate shape | Use Gates A–G as the default cross-lane promotion model. |
| Decision object | Emit a machine-readable `PromotionDecision` / `DecisionEnvelope`-compatible object. |
| Evidence posture | EvidenceRefs must resolve to EvidenceBundles before consequential publication. |
| Catalog posture | STAC / DCAT / PROV / release-manifest closure must be checked where relevant. |
| Policy posture | Missing policy labels, unknown rights, unresolved sensitivity, or invalid source roles fail closed. |
| Receipt/proof split | Receipts record process memory; proofs support release trust. They are not interchangeable. |
| Rollback | Rollback emits new receipt and correction lineage; it never deletes prior proof, catalog, or release objects. |
| UI / AI boundary | UI and AI consume only governed, released, policy-safe promotion outputs. |

---

## Gate model

The default KFM promotion membrane uses **Gates A–G**.

| Gate | Name | What it checks | Minimum evidence |
|---|---|---|---|
| **A** | Identity & closure | Stable candidate ID, canonical `spec_hash`, required identity fields, deterministic release target, no floating blob. | Candidate ID, canonical spec bytes, declared hash, release subject identity. |
| **B** | Asset & schema integrity | Required schemas validate; every declared asset exists, is checksummed, and matches reviewed bytes. | Asset manifest, checksums, schema report, STAC / manifest asset linkage where relevant. |
| **C** | Spatial, geometry, and CRS invariants | Geometry validity, CRS allowlist, bbox consistency, deterministic transforms, sane geometry summaries, public-safe geometry where required. | Geometry-bearing assets, CRS metadata, bbox, transform/generalization parameters, public-safe transform receipt when applicable. |
| **D** | Temporal and coverage semantics | Valid intervals, coherent temporal/spatial coverage, source-aligned scope, freshness declarations where policy requires them. | Time fields, coverage metadata, source date, retrieved date, valid-time statement, freshness metadata. |
| **E** | Rights, sensitivity, and policy | License, rights posture, policy label, source role, sensitivity class, obligations, and deny-by-default handling for unknowns. | Rights metadata, policy label, source descriptor, sensitivity classification, policy decision. |
| **F** | Evidence, provenance, proofs, and receipts | EvidenceRefs resolve; EvidenceBundles exist; receipts are present; proofs and attestations verify when configured; catalog/provenance closure is coherent. | EvidenceBundle, run receipt, validation report, proof pack, attestation refs, catalog refs, PROV/STAC/DCAT closure. |
| **G** | Review, rollback, and correction readiness | Steward review is recorded; prior release reference exists when replacing; rollback target is verifiable; correction path is visible. | Review record, prior `spec_hash`, rollback card or rollback receipt plan, correction notice posture, immutable version/tag intent. |

> [!WARNING]
> A `verified: true` field is not trusted by itself. Verification must be backed by the actual verification step, report, proof reference, or explicit `ABSTAIN` / obligation when the verification infrastructure is unavailable.

---

## Outcome grammar

The gate collapses per-gate results into one final promotion decision.

| Gate condition | Final decision |
|---|---|
| All required gates pass and obligations are satisfied. | `PROMOTE` |
| Any required gate fails due to policy, rights, evidence, sensitivity, integrity, or review defect. | `DENY` |
| Evidence is insufficient, source authority is unresolved, rights are unknown, or reviewer obligations remain without contradiction. | `ABSTAIN` |
| Schema, validator, evaluator, catalog resolver, proof verifier, or policy engine fails before a trustworthy decision can be formed. | `ERROR` |

### Required decision fields

A promotion decision should include, at minimum:

| Field | Purpose |
|---|---|
| `decision` | One of `PROMOTE`, `ABSTAIN`, `DENY`, `ERROR`. |
| `candidate_id` | Stable subject of the decision. |
| `candidate_type` | Dataset, overlay, layer, bundle, claim surface, release, or other approved type. |
| `spec_hash` | Canonical identity anchor for the candidate. |
| `prior_spec_hash` | Rollback / supersession anchor when replacing an existing release. |
| `reason_codes` | Explicit failure, abstention, or error reasons. |
| `obligations` | Required follow-up actions before promotion can continue. |
| `gates` | Per-gate results for reviewer and CI visibility. |
| `policy_ref` | Policy decision or policy evaluation report reference. |
| `proof_ref` | Proof pack, attestation, or verification report reference. |
| `release_ref` | ReleaseManifest or release candidate reference. |
| `audit_ref` | Audit, receipt, or review trail reference. |
| `generated_at` | Time the decision was produced. |

---

## Trust object split

KFM keeps trust surfaces separate so that one object family cannot masquerade as another.

| Surface | Role | Must not become |
|---|---|---|
| `data/receipts/` | Process memory: run receipts, validation reports, replay/correction references. | Release proof by itself. |
| `data/proofs/` | Release-grade trust artifacts, proof packs, attestations, verification reports. | Raw source truth or mutable log storage. |
| `data/catalog/` | Discoverability, linkage, STAC/DCAT/PROV closure, catalog matrix. | Authorization to publish. |
| `schemas/` / `contracts/` | Machine-readable authority for object shape and interface contracts. | Runtime policy decision. |
| `policy/` | Release and runtime decision logic. | Evidence source. |
| `ReleaseManifest` | Release artifact set, digests, source refs, catalog/proof links. | Proof pack by itself. |
| `EvidenceBundle` | Reviewable evidence support bundle resolving EvidenceRefs. | AI summary or UI popup. |
| `PromotionDecision` | Governed state-transition decision. | File move, CI pass, or human comment. |

---

## Promotion flow

```mermaid
flowchart LR
    A[RAW] --> B[WORK]
    A --> C[QUARANTINE]
    B --> D[PROCESSED]
    C --> D
    D --> E[CATALOG / TRIPLET]
    E --> F[Release candidate]
    F --> G[Promotion Gate A-G]
    G -->|PROMOTE| H[PUBLISHED]
    G -->|ABSTAIN| I[Obligations / rework]
    G -->|DENY| J[Blocked / quarantine / correction]
    G -->|ERROR| K[Fix evaluator or contract]
    H --> L[Governed API]
    L --> M[Map / Evidence Drawer / Focus Mode]
```

---

## Implementation contract

### Required invariants

1. **Promotion is explicit.** A candidate does not become published without a promotion decision.
2. **Identity is deterministic.** Candidate identity is anchored by canonical bytes and `spec_hash` or an approved equivalent.
3. **Evidence is resolvable.** EvidenceRefs used by the candidate must resolve to EvidenceBundles before release.
4. **Policy fails closed.** Unknown rights, missing source role, missing policy label, unresolved sensitivity, or policy engine failure cannot silently promote.
5. **Catalog closure is checked.** ReleaseManifest, CatalogMatrix, and STAC/DCAT/PROV records must align where relevant.
6. **Receipts are not proofs.** Process receipts can support audit and replay; they cannot replace proof packs or release manifests.
7. **UI and AI are downstream.** Map surfaces, Evidence Drawer payloads, and Focus Mode may consume released artifacts; they do not decide promotion.
8. **Rollback is governed.** Rollback is another state transition with its own receipt, review, correction notice, and proof linkage.
9. **Prior artifacts are retained.** Correction and rollback never delete prior proofs, receipts, catalogs, or release manifests.
10. **No hidden bypass.** Public clients and ordinary UI surfaces must not read RAW, WORK, QUARANTINE, internal canonical stores, or model runtimes directly.

### Proposed file surfaces

The exact file homes require active-repo verification.

| Surface | Proposed path | Status |
|---|---|---|
| ADR | `docs/adr/ADR-0005-promotion-gate.md` | NEEDS VERIFICATION |
| Human governance doc | `docs/governance/promotion-gate.md` | PROPOSED |
| Promotion decision schema | `schemas/contracts/v1/promotion/promotion_decision.schema.json` | PROPOSED |
| Release manifest schema | `schemas/contracts/v1/release/release_manifest.schema.json` | PROPOSED |
| EvidenceBundle schema | `schemas/contracts/v1/evidence/evidence_bundle.schema.json` | PROPOSED |
| CatalogMatrix schema | `schemas/contracts/v1/catalog/catalog_matrix.schema.json` | PROPOSED |
| Promotion policy | `policy/promotion/` | PROPOSED |
| Gate validator | `tools/validators/promotion_gate/` | PROPOSED |
| Promotion fixtures | `tests/fixtures/promotion/` | PROPOSED |
| Receipt output | `data/receipts/promotions/` | PROPOSED |
| Proof output | `data/proofs/promotions/` | PROPOSED |
| Release output | `data/releases/` | PROPOSED |

> [!CAUTION]
> Do not create parallel schema homes if the active repository already treats a different path as canonical. Resolve schema-home authority through the existing ADR process before landing machine-contract files.

---

## Validation

Promotion validation must include positive and negative fixtures.

| Fixture | Expected decision | Purpose |
|---|---:|---|
| `valid_promote_release_candidate` | `PROMOTE` | Proves complete evidence, policy, catalog, proof, review, and rollback readiness. |
| `deny_missing_evidence_bundle` | `DENY` | EvidenceRefs do not resolve. |
| `deny_unresolved_rights` | `DENY` | Rights or redistribution posture is missing or incompatible. |
| `deny_sensitive_exact_geometry_public` | `DENY` | Public release would expose restricted exact geometry. |
| `deny_signature_mismatch` | `DENY` | Verification fails where signature infrastructure is configured. |
| `abstain_policy_unresolved` | `ABSTAIN` | Evidence is not contradictory, but policy obligations remain unresolved. |
| `error_malformed_candidate` | `ERROR` | Candidate shape prevents trustworthy evaluation. |
| `rollback_to_prior_spec_hash` | `PROMOTE` or `ABSTAIN` | Proves rollback verifies prior proof bundle and emits correction lineage. |

### Illustrative validation command

```bash
# PROPOSED: adapt names, runners, paths, and tools to the active repository.
python tools/validators/promotion_gate/promotion_gate.py \
  tests/fixtures/promotion/valid_release_candidate.json \
  --out build/promotion/decision.json

python tools/validators/promotion_gate/validate_decision_envelope.py \
  build/promotion/decision.json

conftest test build/promotion/decision.json \
  --policy policy/promotion
```

---

## Rollback

Rollback is a governed transition from one published release target to another previously verified release target.

Rollback must:

1. select a prior immutable `spec_hash`;
2. verify the prior ReleaseManifest, EvidenceBundle, CatalogMatrix, and proof pack;
3. emit a rollback receipt;
4. emit or update a correction notice when user-visible state changes;
5. run policy over the rollback decision;
6. update the current alias or release pointer only after verification;
7. preserve prior artifacts;
8. expose correction state through governed public surfaces when applicable.

Rollback must not:

- delete prior receipts, proofs, catalogs, release manifests, or decision objects;
- silently rewrite published history;
- bypass policy because the prior artifact was previously published;
- hide the correction reason from downstream Evidence Drawer or API payloads when the change is consequential.

---

## Consequences

### Positive

- Makes publication inspectable and reversible.
- Keeps evidence, policy, proof, catalog, review, and release state connected.
- Prevents convenient intermediate files from becoming public truth.
- Gives CI, reviewers, UI, and AI a shared release decision object.
- Makes rollback and correction part of trust rather than signs of failure.

### Costs

- Adds contract, fixture, validator, and policy work before public release.
- Slows early publication until proof-object and catalog closure are real.
- Requires strict source-role, rights, sensitivity, and review data that may not exist for every source.
- Requires maintaining negative fixtures and correction drills.

### Rejected alternatives

| Alternative | Rejection reason |
|---|---|
| Treat file movement into `published/` as promotion. | Bypasses evidence, policy, proof, and review. |
| Treat CI success as publication authority. | CI can validate mechanics but cannot replace policy or review. |
| Treat signatures as sufficient proof. | Signatures prove integrity or identity, not rights, sensitivity, evidence completeness, or source role. |
| Let UI or Focus Mode decide publishability. | UI and AI are downstream interpretive layers, not governance authorities. |
| Use manual review only. | Review must be recorded and machine-checkable enough to support audit, rollback, and repeatable gates. |

---

## Open verification

The following items remain NEEDS VERIFICATION before this ADR can be treated as accepted implementation guidance:

- active ADR numbering and whether `ADR-0005` is available;
- `docs/adr/` local formatting conventions;
- CODEOWNERS or steward owner for promotion governance;
- current schema home: `contracts/`, `schemas/contracts/v1/`, or another repo convention;
- whether `PromotionDecision`, `DecisionEnvelope`, or both are canonical;
- existing promotion gate tooling and workflow names;
- OPA / Conftest / Cosign / attestation availability and pinned versions;
- release manifest storage location;
- proof pack storage location;
- catalog matrix storage location;
- whether a `HOLD` display state exists locally, and whether it maps to `ABSTAIN` or requires a separate ADR;
- whether any already-published artifact has a rollback/correction fixture that this ADR must preserve.

---

## Acceptance checklist

- [ ] ADR path and numbering verified.
- [ ] Owner and policy label confirmed.
- [ ] Schema-home conflict resolved or explicitly deferred.
- [ ] Promotion decision schema has positive and negative fixtures.
- [ ] Gate A–G evaluator emits finite outcomes.
- [ ] EvidenceRef-to-EvidenceBundle resolution is tested.
- [ ] Catalog closure is tested.
- [ ] Rights, sensitivity, and source-role policy denials are tested.
- [ ] Receipts and proofs remain separate.
- [ ] Rollback drill emits receipt and correction lineage.
- [ ] UI and AI surfaces consume only governed release decisions.
- [ ] Documentation links are verified from `docs/adr/`.
