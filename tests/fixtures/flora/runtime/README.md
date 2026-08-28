<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-fixtures-flora-runtime-readme
title: Flora Runtime Test Fixtures README
type: test-fixture-readme
version: v0.1
status: draft; placeholder-replaced; flora-runtime-test-fixture-lane; compatibility-path; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD - Flora domain steward
  - OWNER_TBD - Fixture steward
  - OWNER_TBD - Runtime/API steward
  - OWNER_TBD - QA steward
  - OWNER_TBD - Evidence steward
  - OWNER_TBD - Policy steward
  - OWNER_TBD - Release steward
created: 2026-07-06
updated: 2026-07-06
policy_label: public-doc; tests; fixtures; flora; runtime; finite-outcome; synthetic-only; no-network; public-safe; rare-plant-aware; source-role-aware; evidence-bound; policy-gated; release-gated; rollback-aware
tags: [kfm, tests, fixtures, flora, runtime, RuntimeResponseEnvelope, finite-outcomes, ANSWER, ABSTAIN, DENY, ERROR, AIReceipt, EvidenceRef, EvidenceBundle, PolicyDecision, RedactionReceipt, ReleaseManifest, RollbackCard, no-network, public-safe, rare-plants]
related:
  - ../../README.md
  - ../../../README.md
  - ../../../domains/flora/README.md
  - ../../../domains/flora/runtime_proof/README.md
  - ../../../fixtures/domains/flora/README.md
  - ../../../../fixtures/domains/flora/README.md
  - ../../../../fixtures/domains/flora/decision_envelopes/README.md
  - ../../../../fixtures/domains/flora/evidence_bundles/README.md
  - ../../../../fixtures/domains/flora/rare_plant_record/README.md
  - ../../../../fixtures/domains/flora/flora_occurrence/README.md
  - ../../../../fixtures/domains/flora/valid/README.md
  - ../../../../fixtures/domains/flora/invalid/README.md
  - ../../../../fixtures/domains/flora/golden/README.md
  - ../../../../docs/domains/flora/README.md
  - ../../../../docs/domains/flora/CANONICAL_PATHS.md
  - ../../../../docs/domains/flora/VERIFICATION_BACKLOG.md
  - ../../../../docs/domains/flora/API_CONTRACTS.md
  - ../../../../docs/domains/flora/SENSITIVITY.md
  - ../../../../docs/domains/flora/DATA_LIFECYCLE.md
  - ../../../../docs/domains/flora/THIN_SLICE_PLAN.md
  - ../../../../contracts/domains/flora/
  - ../../../../schemas/contracts/v1/domains/flora/
  - ../../../../policy/domains/flora/
  - ../../../../policy/sensitivity/flora/
  - ../../../../data/registry/sources/flora/
  - ../../../../release/candidates/flora/
notes:
  - "This README replaces placeholder content at tests/fixtures/flora/runtime/README.md."
  - "This path is a compatibility/test-local runtime fixture lane named by the Flora verification backlog for API finite-outcome fixtures. It intentionally does not become the canonical reusable Flora fixture root."
  - "Canonical reusable Flora fixtures live under fixtures/domains/flora/. Domain-scoped tests live under tests/domains/flora/."
  - "Runtime fixture success is not evidence closure, policy approval, release approval, public-map authority, or implementation proof."
  - "Executable tests, fixture payload inventory, runtime schema bindings, CI jobs, and pass rates remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Flora runtime test fixtures

> Compatibility/test-local documentation for runtime fixtures under `tests/fixtures/flora/runtime/`. This lane exists to support finite-outcome Flora runtime and Focus Mode checks without turning fixture examples into Flora truth, source truth, EvidenceBundle closure, policy approval, release approval, public map material, or public artifacts.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Lane: runtime fixtures" src="https://img.shields.io/badge/lane-runtime__fixtures-purple">
  <img alt="Domain: flora" src="https://img.shields.io/badge/domain-flora-green">
  <img alt="Outcomes: finite" src="https://img.shields.io/badge/outcomes-ANSWER%20%7C%20ABSTAIN%20%7C%20DENY%20%7C%20ERROR-informational">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
</p>

**Path:** `tests/fixtures/flora/runtime/README.md`  
**Status:** draft / placeholder replaced / compatibility runtime-fixture lane / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Lane family:** `fixtures/flora/runtime`  
**Canonical reusable fixture root:** `fixtures/domains/flora/`  
**Canonical domain test root:** `tests/domains/flora/`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target file existed as placeholder content before replacement; CONFIRMED Flora canonical path guidance places domain tests under `tests/domains/flora/` and reusable fixtures under `fixtures/domains/flora/`; CONFIRMED the Flora verification backlog names `tests/fixtures/flora/runtime/` as the settling-evidence home for API finite-outcome fixtures; NEEDS VERIFICATION for executable tests, payload inventory, runtime schema bindings, CI coverage, and pass rates.

---

## Purpose

`tests/fixtures/flora/runtime/` is a compatibility/test-local lane for Flora runtime fixture expectations.

Use this lane for fixture manifests, synthetic request/response examples, and expected-output notes that test Flora runtime behavior through finite outcomes:

- `ANSWER` when a public-safe, released, evidence-backed Flora response is allowed;
- `ABSTAIN` when evidence, source role, citation closure, release state, or review state is insufficient;
- `DENY` when rights, sensitivity, rare-plant geoprivacy, exact-location exposure, policy, review, or release state blocks exposure;
- `ERROR` when the fixture, runtime envelope, loader, schema, or local test setup is malformed.

A runtime fixture in this lane should not mean that a plant occurrence is true, a taxonomic resolution is authoritative, an exact location is publishable, a public layer is released, a policy decision is approved, or a Focus Mode answer is trustworthy. It means only that a bounded synthetic input is expected to produce a bounded runtime outcome.

[Back to top](#top)

---

## Placement basis

The standard Flora lane pattern keeps domain tests under `tests/domains/flora/` and reusable fixtures under `fixtures/domains/flora/`. The Flora verification backlog also names `tests/fixtures/flora/runtime/` as the proposed fixture set for API finite-outcome coverage. This README therefore treats the requested path as a compatibility/test-local runtime lane, not a competing canonical fixture root.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Runtime fixture expectations for finite outcomes | `tests/fixtures/flora/runtime/` | This directory; compatibility/test-local lane named by the Flora backlog. |
| Flora runtime proof tests | `tests/domains/flora/runtime_proof/` | Expected executable consumer lane; not fixture authority. |
| Reusable Flora fixtures | `fixtures/domains/flora/` | Canonical reusable fixture root; referenced, not replaced. |
| Runtime response schemas | `schemas/contracts/v1/` and Flora-specific schema homes | Defines accepted shape; not owned here. |
| Runtime/API contracts | `contracts/` and `contracts/domains/flora/` | Defines object and envelope meaning; not owned here. |
| Policy authority | `policy/domains/flora/` and `policy/sensitivity/flora/` | Referenced by expected outcomes; not defined here. |
| Source registry | `data/registry/sources/flora/` | Source identity, role, rights, sensitivity, and cadence records; not owned here. |
| Evidence, receipts, and proof | `data/proofs/`, `data/receipts/`, and accepted trust roots | Referenced through synthetic refs; not stored here. |
| Release decisions | `release/` roots | Referenced through synthetic refs; not decided here. |

> [!IMPORTANT]
> Do not expand this path into a parallel Flora fixture root. Prefer `fixtures/domains/flora/` for reusable examples and keep this path focused on runtime finite-outcome fixture sets and test-local expectations.

---

## Invariant under test

> **Flora runtime fixtures are synthetic bounded examples, not runtime truth or Flora truth.** Passing fixtures prove only that expected finite-outcome behavior is documented and, once tests exist, enforceable.

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Finite-outcome boundary | Every runtime fixture expects exactly one of `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`. | validation failure. |
| Fixture-root boundary | Reusable payloads live under `fixtures/domains/flora/`; test-local runtime wrappers require a documented reason. | validation failure. |
| Synthetic-only boundary | Fixtures use fake IDs, toy taxa, toy sources, toy timestamps, toy geometries, and synthetic refs. | quarantine / validation failure. |
| No-network boundary | Fixture loaders do not call live source APIs, map services, release services, governed APIs, or AI runtimes. | `ERROR`. |
| Evidence boundary | Claim-like `ANSWER` fixtures require synthetic EvidenceRef / EvidenceBundle closure or explicitly state why evidence is out of scope. | `ABSTAIN`. |
| Citation boundary | Runtime text fixtures that assert Flora claims carry citation-validation expectations. | `ABSTAIN` / validation failure. |
| Rare-plant boundary | Exact sensitive geometry, steward-only locality, culturally sensitive plant knowledge, or protected-taxon side channels fail closed. | `DENY`. |
| AI no-leak boundary | AI/Focus Mode text must not echo exact sensitive coordinates, locality names below public threshold, or steward-only attributes. | `DENY`. |
| Policy boundary | Rights, sensitivity, source role, release state, review state, and public-geometry blockers fail closed. | `DENY` / `ABSTAIN`. |
| Release boundary | Fixture success does not become release approval, publication, correction approval, or rollback approval. | promotion block. |

---

## Expected runtime fixture families

| Family | Purpose | Boundary |
|---|---|---|
| `ANSWER` fixtures | Public-safe, released, evidence-backed examples with bounded text/payload expectations. | `ANSWER` does not create Flora truth. |
| `ABSTAIN` fixtures | Missing evidence, unresolved taxonomy, insufficient citation closure, stale review, or unreleased state. | Abstention is an outcome, not failure. |
| `DENY` fixtures | Rare-plant exact geometry, steward-only locality, unresolved rights, sensitivity block, or policy block. | Denial does not disclose the blocked value. |
| `ERROR` fixtures | Malformed envelopes, loader errors, impossible state, invalid schema, or non-deterministic setup. | Error is operational, not a policy denial. |
| AI receipt fixtures | Expected `AIReceipt` refs with evidence, policy decision, and citation-validation fields. | Receipt fixture is not production receipt storage. |
| Evidence Drawer fixtures | Runtime payloads that should display evidence status, limits, policy, release, and correction context. | Drawer fixture is not EvidenceBundle closure. |
| Focus Mode fixtures | Bounded Flora Focus responses, limitations, disclaimers, citations, and no-leak expectations. | Focus text is not authority. |
| Rare-plant no-leak fixtures | Negative side-channel checks for exact coordinates, locality names, sensitive attributes, and hidden geometry. | No real locations. |
| Release-state fixtures | Released, unreleased, withdrawn, corrected, and rollback-visible runtime cases. | Release-shaped refs are synthetic. |
| Source-role fixtures | Observed, regulatory, modeled, aggregate, administrative, candidate, and synthetic roles remain distinct. | Source role is fixed at admission. |

---

## Accepted inputs

Only bounded, synthetic, reviewable material belongs in this lane:

- fixture manifests describing expected runtime outcome, reason codes, and no-network posture
- synthetic runtime request and response envelopes
- synthetic `RuntimeResponseEnvelope`, `DecisionEnvelope`, `AIReceipt`, `EvidenceRef`, `EvidenceBundle`, `PolicyDecision`, `RedactionReceipt`, `ReviewRecord`, `ReleaseManifest`, `CorrectionNotice`, `WithdrawalNotice`, and `RollbackCard` refs
- synthetic `PlantTaxon`, `SpecimenRecord`, `FloraOccurrence`, `RarePlantRecord`, `VegetationCommunity`, `InvasivePlantRecord`, `PhenologyObservation`, `RangePolygon`, `HabitatAssociation`, `BotanicalSurvey`, and `RestorationPlanting` references
- expected-output snippets for `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR`
- canary values that make evidence gaps, citation gaps, source-role collapse, rare-plant leakage, exact-location exposure, AI side-channel leakage, public-route bypass, map-truth leakage, or release approval obvious
- test-local wrappers that point to canonical fixtures under `fixtures/domains/flora/`

Safe outputs may include public-safe fields such as fixture ID, route name, request shape, outcome, reason code, evidence ref, citation-validation ref, policy decision ref, redaction receipt ref, release ref, correction ref, rollback ref, AI receipt ref, and expected display limits.

---

## Exclusions

Do not place these materials in this lane:

| Excluded material | Why it does not belong here |
|---|---|
| Real source exports, live source responses, production payloads, or public payloads | Default tests must stay synthetic, deterministic, and no-network. |
| Exact rare-plant coordinates, protected-species locality, steward-only locality, culturally sensitive plant knowledge, or private property/person joins | Sensitive and rights-limited material must fail closed. |
| Direct reads from RAW, WORK, QUARANTINE, internal stores, unpublished candidates, canonical stores, public APIs, or model runtime outputs | Bypasses the trust membrane and no-network posture. |
| Secrets, credentials, private endpoints, production logs, telemetry, or access tokens | Security and exposure risk. |
| Real EvidenceBundles, ProofPacks, production receipts, release manifests, rollback cards, correction notices, withdrawal notices, public artifacts, or audit ledgers | Governed trust records and release artifacts belong in their own roots. |
| Binding policy rules, schema definitions, contract prose, source descriptors, release procedures, pipeline implementation, connector implementation, map implementation, API implementation, or AI runtime implementation | Authority and implementation belong in their own responsibility roots. |

---

## Suggested layout

```text
tests/fixtures/flora/runtime/
|-- README.md
|-- manifest_expectations.json
|-- answer_public_safe.example.json
|-- abstain_missing_evidence.example.json
|-- deny_rare_plant_exact_location.example.json
|-- deny_ai_side_channel.example.json
|-- error_malformed_envelope.example.json
|-- expected_reason_codes.json
`-- expected_ai_receipt_fields.json
```

This layout is PROPOSED until executable files exist in the repository.

---

## Run posture

No executable runner was verified while authoring this README. Once tests exist, the expected local command should be documented and verified here.

```bash
: "PROPOSED / NEEDS VERIFICATION"
pytest tests/domains/flora/runtime_proof tests/fixtures/flora/runtime
```

Required run posture: no network access, no live source calls, no direct lifecycle-store reads, no real secrets, no production logs, no production trust artifacts, no exact sensitive flora locations, no steward-controlled locality data, no public artifact writes, deterministic fixture inputs, and finite outcomes only: `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`.

---

## Minimal runtime fixture manifest

Synthetic runtime manifests should describe fixture expectations without carrying real Flora data.

```json
{
  "fixture_manifest_id": "flora-runtime-fixture-answer-public-safe-example",
  "domain": "flora",
  "runtime_surface": "focus_mode",
  "fixture_family": "answer_public_safe",
  "canonical_fixture_ref": "fixtures/domains/flora/valid/example-fixture.json",
  "expected_outcome": "ANSWER",
  "expected_reason_codes": [],
  "evidence_ref": "evidence:synthetic:flora:runtime:example",
  "policy_decision_ref": "policy:synthetic:flora:allow-public-safe-example",
  "citation_validation_ref": "citation:synthetic:flora:runtime:example",
  "ai_receipt_required": true,
  "network": "disabled",
  "uses_real_source_data": false,
  "authorizes_publication": false
}
```

For denial cases, the manifest should make the denial cause explicit without carrying the sensitive value:

```json
{
  "fixture_manifest_id": "flora-runtime-fixture-deny-rare-plant-exact-location",
  "domain": "flora",
  "runtime_surface": "focus_mode",
  "fixture_family": "rare_plant_exact_location_denial",
  "expected_outcome": "DENY",
  "expected_reason_codes": [
    "SENSITIVE_EXACT_LOCATION_BLOCKED",
    "AI_SIDE_CHANNEL_BLOCKED"
  ],
  "redaction_receipt_ref": "receipt:synthetic:flora:redaction:exact-location-denied",
  "ai_receipt_required": true,
  "network": "disabled",
  "uses_real_source_data": false,
  "authorizes_publication": false
}
```

---

## Finite outcome expectations

| Outcome | Meaning in this lane | Example |
|---|---|---|
| `ANSWER` | Synthetic public-safe request can be answered with released/evidence-backed context. | Generalized public-safe vegetation community summary. |
| `ABSTAIN` | Evidence, citation, release, taxonomy, review, or source-role support is insufficient. | Missing EvidenceRef for a plant occurrence claim. |
| `DENY` | Rights, sensitivity, rare-plant geoprivacy, review, release, or policy blocks exposure. | Exact sensitive rare-plant location requested. |
| `ERROR` | Envelope, fixture, loader, schema, or test setup is malformed or non-deterministic. | Runtime fixture omits required outcome field. |

---

## Maintenance checklist

Before adding or changing material in this lane, verify:

- [ ] fixture material is synthetic, compact, deterministic, and no-network
- [ ] reusable payloads belong under `fixtures/domains/flora/` unless there is a test-local reason
- [ ] each fixture declares exactly one expected runtime outcome
- [ ] source role, evidence state, citation state, rights state, sensitivity state, policy state, review state, release state, correction state, rollback state, AI receipt state, and expected outcome are explicit where material
- [ ] `ANSWER` fixtures do not bypass evidence, policy, release, or citation closure
- [ ] `DENY` fixtures do not expose the blocked sensitive value
- [ ] `ABSTAIN` fixtures make the missing support explicit
- [ ] `ERROR` fixtures distinguish malformed state from policy denial
- [ ] test-local wrappers do not become a parallel fixture authority
- [ ] release-shaped refs remain synthetic and do not authorize publication
- [ ] docs, tests, schemas, contracts, and policy references are updated when runtime behavior changes

---

## Change discipline

Changes to this lane should be small, inspectable, and reversible.

| Change type | Required action |
|---|---|
| Add a runtime fixture | Add expected outcome, reason code, no-network posture, and synthetic support refs. |
| Add an `ANSWER` fixture | Include evidence, citation, policy, release, and AI receipt expectations. |
| Add an `ABSTAIN` fixture | State the missing evidence, citation, taxonomy, source-role, review, or release condition. |
| Add a `DENY` fixture | State the policy/sensitivity reason without exposing the sensitive value. |
| Add an `ERROR` fixture | Make the malformed envelope or setup problem explicit. |
| Add release-shaped material | Keep it synthetic and non-authorizing; real release objects belong under `release/`. |
| Discover real data in this lane | Move it out, quarantine through the governed lifecycle or registry process, and record the correction path. |

---

## Verification status

- Target README: replaced placeholder content.
- Path convention: `tests/fixtures/flora/runtime/` is named by the Flora verification backlog for API finite-outcome fixtures; it is treated here as compatibility/test-local, not canonical fixture-root authority.
- Canonical Flora fixture root: verified as present and README-backed during authoring.
- Fixture payload inventory: not exhaustively verified in this update.
- Runtime fixture alignment: verified against `docs/domains/flora/VERIFICATION_BACKLOG.md` for finite-outcome, AI no-leak, AI receipt, citation-validation, and API fixture expectations.
- Flora canonical path alignment: verified against `docs/domains/flora/CANONICAL_PATHS.md` for domain-placement, test/fixture lane, lifecycle, source-role, rare-plant sensitivity, no-network first-slice, and connector non-publisher posture.
- Contract/schema alignment: NEEDS VERIFICATION against runtime envelope schemas and Flora API contracts.
- Consumer alignment: NEEDS VERIFICATION against runtime-proof tests, governed-API tests, Focus Mode checks, Evidence Drawer checks, AI receipt checks, citation-validation checks, rare-plant no-leak checks, policy checks, release-state checks, and CI coverage.
- Tests and validators: NOT RUN.
