<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-fixtures-flora-source-role-collapse-readme
title: Flora Source-Role Collapse Test Fixtures README
type: test-fixture-readme
version: v0.1
status: draft; placeholder-replaced; flora-source-role-collapse-test-fixture-lane; compatibility-path; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD - Flora domain steward
  - OWNER_TBD - Source steward
  - OWNER_TBD - Fixture steward
  - OWNER_TBD - QA steward
  - OWNER_TBD - Evidence steward
  - OWNER_TBD - Policy steward
  - OWNER_TBD - Release steward
created: 2026-07-06
updated: 2026-07-06
policy_label: public-doc; tests; fixtures; flora; source-role-collapse; synthetic-only; no-network; public-safe; anti-collapse; source-role-aware; evidence-bound; policy-gated; release-gated; rollback-aware
tags: [kfm, tests, fixtures, flora, source-role-collapse, SourceDescriptor, source_role, observed, regulatory, modeled, aggregate, administrative, candidate, synthetic, ROLE_COLLAPSE, ROLE_DOWNCAST_FORBIDDEN, EvidenceRef, EvidenceBundle, PolicyDecision, ReleaseManifest, ABSTAIN, DENY, ERROR]
related:
  - ../../README.md
  - ../../../README.md
  - ../../../domains/flora/README.md
  - ../../../domains/flora/runtime_proof/README.md
  - ../../../fixtures/domains/flora/README.md
  - ../../../../fixtures/domains/flora/README.md
  - ../../../../fixtures/domains/flora/source_descriptors/README.md
  - ../../../../fixtures/domains/flora/sources/README.md
  - ../../../../fixtures/domains/flora/sources/plants/README.md
  - ../../../../fixtures/domains/flora/plants_drift/README.md
  - ../../../../fixtures/domains/flora/evidence_bundles/README.md
  - ../../../../fixtures/domains/flora/decision_envelopes/README.md
  - ../../../../fixtures/domains/flora/valid/README.md
  - ../../../../fixtures/domains/flora/invalid/README.md
  - ../../../../fixtures/domains/flora/golden/README.md
  - ../../../../docs/domains/flora/README.md
  - ../../../../docs/domains/flora/CANONICAL_PATHS.md
  - ../../../../docs/domains/flora/VERIFICATION_BACKLOG.md
  - ../../../../docs/domains/flora/SOURCE_ROLES.md
  - ../../../../docs/domains/flora/SOURCE_FAMILIES.md
  - ../../../../docs/domains/flora/SOURCES.md
  - ../../../../docs/domains/flora/SOURCE_INTAKE.md
  - ../../../../docs/domains/flora/SOURCE_REGISTRY.md
  - ../../../../contracts/domains/flora/
  - ../../../../schemas/contracts/v1/domains/flora/
  - ../../../../schemas/contracts/v1/source/
  - ../../../../policy/domains/flora/
  - ../../../../policy/sensitivity/flora/
  - ../../../../data/registry/sources/flora/
  - ../../../../release/candidates/flora/
notes:
  - "This README replaces placeholder content at tests/fixtures/flora/source_role_collapse/README.md."
  - "This path is a compatibility/test-local fixture lane named by the Flora verification backlog for source-role anti-collapse negative fixtures. It intentionally does not become the canonical reusable Flora fixture root."
  - "Canonical reusable Flora fixtures live under fixtures/domains/flora/. Domain-scoped tests live under tests/domains/flora/."
  - "Source role is fixed at admission and must not be upgraded by promotion."
  - "Fixture success is not evidence closure, source admission, policy approval, release approval, public-map authority, or implementation proof."
  - "Executable tests, fixture payload inventory, validator reason-code wiring, CI jobs, and pass rates remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Flora source-role collapse test fixtures

> Compatibility/test-local documentation for source-role anti-collapse fixtures under `tests/fixtures/flora/source_role_collapse/`. This lane exists to support negative fixture coverage for `ROLE_COLLAPSE` and `ROLE_DOWNCAST_FORBIDDEN` without turning fixture examples into source truth, source-registry authority, Flora truth, policy approval, release approval, public map material, or public artifacts.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Lane: source role collapse" src="https://img.shields.io/badge/lane-source__role__collapse-purple">
  <img alt="Domain: flora" src="https://img.shields.io/badge/domain-flora-green">
  <img alt="Reason: ROLE_COLLAPSE" src="https://img.shields.io/badge/reason-ROLE__COLLAPSE-critical">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
</p>

**Path:** `tests/fixtures/flora/source_role_collapse/README.md`  
**Status:** draft / placeholder replaced / compatibility source-role-collapse fixture lane / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Lane family:** `fixtures/flora/source_role_collapse`  
**Canonical reusable fixture root:** `fixtures/domains/flora/`  
**Canonical domain test root:** `tests/domains/flora/`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target file existed as placeholder content before replacement; CONFIRMED the Flora verification backlog names `tests/fixtures/flora/source_role_collapse/` as the negative-fixture-set location for source-role anti-collapse verification; CONFIRMED Flora source-role doctrine defines the seven-role enum and treats role collapse as fail-closed; NEEDS VERIFICATION for executable tests, payload inventory, validator reason-code coverage, CI coverage, and pass rates.

---

## Purpose

`tests/fixtures/flora/source_role_collapse/` is a compatibility/test-local lane for Flora source-role anti-collapse fixture expectations.

Use this lane for synthetic negative fixtures that prove a Flora source role cannot be silently upgraded, downcast, reinterpreted, or cited for the wrong claim type. These fixtures should exercise, at minimum, the proposed reason codes:

- `ROLE_COLLAPSE`
- `ROLE_DOWNCAST_FORBIDDEN`

A fixture in this lane should not mean that a source has been admitted, a `SourceDescriptor` is authoritative, a claim is evidence-backed, a policy decision is approved, a release is safe, or a public layer is published. It should mean only that a bounded synthetic input is expected to fail closed when the source role is misused.

[Back to top](#top)

---

## Placement basis

The standard Flora lane pattern keeps domain tests under `tests/domains/flora/` and reusable fixtures under `fixtures/domains/flora/`. The Flora verification backlog specifically names `tests/fixtures/flora/source_role_collapse/` as the negative-fixture-set home for the anti-collapse check. This README therefore treats the requested path as a compatibility/test-local fixture lane, not a competing canonical fixture root.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Source-role collapse negative fixtures | `tests/fixtures/flora/source_role_collapse/` | This directory; compatibility/test-local lane named by the Flora backlog. |
| Flora domain source-role tests | `tests/domains/flora/` | Expected executable consumer lane; not fixture authority. |
| Reusable Flora fixtures | `fixtures/domains/flora/` | Canonical reusable fixture root; referenced, not replaced. |
| SourceDescriptor examples | `fixtures/domains/flora/source_descriptors/` and `fixtures/domains/flora/sources/` | Reusable examples; not replaced by this lane. |
| Source-role doctrine | `docs/domains/flora/SOURCE_ROLES.md` | Human-facing rule localization; not executable proof. |
| Source registry | `data/registry/sources/flora/` | Source identity, role, rights, sensitivity, and cadence records; not owned here. |
| Source schema | `schemas/contracts/v1/source/` | Machine shape for source descriptor fields; not owned here. |
| Policy authority | `policy/domains/flora/` and `policy/sensitivity/flora/` | Referenced by expected outcomes; not defined here. |
| Evidence, receipts, and proof | `data/proofs/`, `data/receipts/`, and accepted trust roots | Referenced through synthetic refs; not stored here. |
| Release decisions | `release/` roots | Referenced through synthetic refs; not decided here. |

> [!IMPORTANT]
> Do not expand this path into a parallel Flora fixture root. Prefer `fixtures/domains/flora/` for reusable examples and keep this path focused on source-role anti-collapse negative fixture sets and test-local expectations.

---

## Invariant under test

> **Source role is fixed at admission and is never upgraded by promotion.** A source role mismatch is a fail-closed condition, not a cleanup warning.

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Role enum boundary | Fixtures use one of `observed`, `regulatory`, `modeled`, `aggregate`, `administrative`, `candidate`, or `synthetic`. | `ERROR` / validation failure. |
| Role fixed at admission | Promotion cannot relabel a role toward higher authority or different truth type. | `DENY` with `ROLE_DOWNCAST_FORBIDDEN`. |
| Observed boundary | Observed specimen/occurrence examples may support place/time claims only with evidence and uncertainty. | `DENY` / `ABSTAIN` if cited for legal status. |
| Regulatory boundary | USFWS, NatureServe, or KDWP status examples may support legal/conservation status only. | `DENY` with `ROLE_COLLAPSE` if cited as an observed occurrence. |
| Modeled boundary | NDVI, suitability, restoration, or distribution-model examples remain modeled. | `DENY` / `ABSTAIN` if labeled observed. |
| Aggregate boundary | GBIF/PLANTS/iDigBio aggregate examples remain aggregate and scope-bounded. | `DENY` / `ABSTAIN` if cited as per-place originality. |
| Administrative boundary | Program, stewardship, or roster examples remain administrative context. | `DENY` if cited as field observation. |
| Candidate boundary | Candidate examples remain internal review only until admitted through governed transition. | `DENY` at trust membrane. |
| Synthetic boundary | Synthetic examples require a reality-boundary note and never support observed-reality claims. | `DENY` / `ABSTAIN`. |
| Evidence boundary | Role-appropriate claims require EvidenceRef expectations or explicit abstention. | `ABSTAIN`. |
| Release boundary | Fixture success does not become release approval, publication, correction approval, or rollback approval. | promotion block. |

---

## Expected negative fixture families

| Family | Misuse being tested | Expected result |
|---|---|---|
| Regulatory-as-observed | USFWS/NatureServe/KDWP status cited as field occurrence. | `DENY` / `ROLE_COLLAPSE`. |
| Observed-as-regulatory | Herbarium or iNaturalist observation cited as legal listing status. | `DENY` / `ROLE_COLLAPSE`. |
| Modeled-as-observed | NDVI/suitability/range model labeled as observed occurrence. | `DENY` or `ABSTAIN` / `ROLE_COLLAPSE`. |
| Aggregate-as-per-place | GBIF/PLANTS county or aggregate record cited as exact locality. | `DENY` or `ABSTAIN` / `ROLE_COLLAPSE`. |
| Administrative-as-observed | Stewardship roster or program record cited as field observation. | `DENY` / `ROLE_COLLAPSE`. |
| Candidate-to-public | Unreviewed candidate exposed to public runtime, layer, or catalog surface. | `DENY` / publication block. |
| Synthetic-as-reality | Synthetic example used as observed Flora evidence. | `DENY` / `ABSTAIN`. |
| Promotion role upgrade | Pipeline or fixture attempts to relabel modeled/aggregate/candidate as observed. | `DENY` / `ROLE_DOWNCAST_FORBIDDEN`. |
| Claim-scope mismatch | EvidenceBundle role does not match claim type. | `DENY` / `ABSTAIN`. |
| Release-manifest mismatch | Release-shaped fixture references a layer whose source role cannot support the public claim. | `DENY` / release block. |

---

## Accepted inputs

Only bounded, synthetic, reviewable material belongs in this lane:

- fixture manifests describing source role, attempted claim type, expected fail-closed outcome, and expected reason codes
- synthetic `SourceDescriptor` refs and role-bearing source examples
- synthetic `EvidenceRef`, `EvidenceBundle`, `PolicyDecision`, `ValidationReport`, `ReviewRecord`, `ReleaseManifest`, `CorrectionNotice`, `WithdrawalNotice`, and `RollbackCard` refs
- synthetic `PlantTaxon`, `SpecimenRecord`, `FloraOccurrence`, `RarePlantRecord`, `VegetationCommunity`, `InvasivePlantRecord`, `PhenologyObservation`, `RangePolygon`, `HabitatAssociation`, `BotanicalSurvey`, and `RestorationPlanting` references where role mismatch matters
- negative examples for `observed`, `regulatory`, `modeled`, `aggregate`, `administrative`, `candidate`, and `synthetic`
- canary values that make role collapse, claim-scope mismatch, public-candidate exposure, synthetic-as-reality, aggregate-as-locality, regulatory-as-observation, model-as-observation, or release approval obvious
- test-local wrappers that point to canonical fixtures under `fixtures/domains/flora/`

Safe outputs may include public-safe fields such as fixture ID, source role, attempted claim type, expected outcome, expected reason code, EvidenceRef placeholder, policy decision placeholder, validation placeholder, release placeholder, and correction placeholder.

---

## Exclusions

Do not place these materials in this lane:

| Excluded material | Why it does not belong here |
|---|---|
| Real source exports, live source responses, production payloads, or public payloads | Default tests must stay synthetic, deterministic, and no-network. |
| Real `SourceDescriptor`s, source activation decisions, license reviews, or registry entries | Registry/source authority belongs in `data/registry/sources/flora/` and source governance roots. |
| Exact rare-plant coordinates, protected-species locality, steward-only locality, culturally sensitive plant knowledge, or private property/person joins | Sensitive and rights-limited material must fail closed. |
| Direct reads from RAW, WORK, QUARANTINE, internal stores, unpublished candidates, canonical stores, public APIs, or model runtime outputs | Bypasses the trust membrane and no-network posture. |
| Secrets, credentials, private endpoints, production logs, telemetry, or access tokens | Security and exposure risk. |
| Real EvidenceBundles, ProofPacks, production receipts, release manifests, rollback cards, correction notices, withdrawal notices, public artifacts, or audit ledgers | Governed trust records and release artifacts belong in their own roots. |
| Binding policy rules, schema definitions, contract prose, release procedures, pipeline implementation, connector implementation, map implementation, API implementation, or AI runtime implementation | Authority and implementation belong in their own responsibility roots. |

---

## Suggested layout

```text
tests/fixtures/flora/source_role_collapse/
|-- README.md
|-- manifest_expectations.json
|-- regulatory_as_observed.deny.json
|-- observed_as_regulatory.deny.json
|-- modeled_as_observed.deny.json
|-- aggregate_as_per_place.deny.json
|-- administrative_as_observed.deny.json
|-- candidate_to_public.deny.json
|-- synthetic_as_reality.deny.json
|-- role_upgrade_forbidden.deny.json
`-- expected_reason_codes.json
```

This layout is PROPOSED until executable files exist in the repository.

---

## Run posture

No executable runner was verified while authoring this README. Once tests exist, the expected local command should be documented and verified here.

```bash
: "PROPOSED / NEEDS VERIFICATION"
pytest tests/domains/flora tests/fixtures/flora/source_role_collapse
```

Required run posture: no network access, no live source calls, no direct lifecycle-store reads, no real secrets, no production logs, no production trust artifacts, no exact sensitive flora locations, no steward-controlled locality data, no public artifact writes, deterministic fixture inputs, and finite outcomes only: `PASS`, `DENY`, `ABSTAIN`, or `ERROR`.

---

## Minimal source-role collapse manifest

Synthetic negative manifests should describe role misuse without carrying real Flora data.

```json
{
  "fixture_manifest_id": "flora-source-role-collapse-regulatory-as-observed",
  "domain": "flora",
  "fixture_family": "regulatory_as_observed",
  "source_role": "regulatory",
  "attempted_claim_type": "observed_occurrence",
  "expected_outcome": "DENY",
  "expected_reason_codes": [
    "ROLE_COLLAPSE"
  ],
  "source_descriptor_ref": "source:synthetic:flora:regulatory-status-example",
  "policy_decision_ref": "policy:synthetic:flora:deny-role-collapse",
  "network": "disabled",
  "uses_real_source_data": false,
  "authorizes_publication": false
}
```

For promotion-role misuse, the manifest should make the forbidden relabel explicit:

```json
{
  "fixture_manifest_id": "flora-source-role-collapse-modeled-upgraded-to-observed",
  "domain": "flora",
  "fixture_family": "role_upgrade_forbidden",
  "source_role_before": "modeled",
  "attempted_source_role_after": "observed",
  "attempted_transition": "promotion",
  "expected_outcome": "DENY",
  "expected_reason_codes": [
    "ROLE_DOWNCAST_FORBIDDEN"
  ],
  "source_descriptor_ref": "source:synthetic:flora:modeled-suitability-example",
  "correction_required": true,
  "network": "disabled",
  "uses_real_source_data": false,
  "authorizes_publication": false
}
```

---

## Finite outcome expectations

| Outcome | Meaning in this lane | Example |
|---|---|---|
| `PASS` | The negative fixture itself is well-formed and verifies the expected fail-closed behavior. | A regulatory-as-observed case is correctly rejected. |
| `ABSTAIN` | The runtime cannot answer because role support, evidence, citation, review, or release state is insufficient. | Aggregate fixture asked for exact-place originality. |
| `DENY` | Role mismatch, attempted role upgrade, public-candidate exposure, or synthetic-as-reality blocks exposure. | Modeled suitability labeled as observed occurrence. |
| `ERROR` | The fixture or loader is malformed, unavailable, non-deterministic, or tries to use the network. | Test helper attempts a live source request. |

---

## Maintenance checklist

Before adding or changing material in this lane, verify:

- [ ] fixture material is synthetic, compact, deterministic, and no-network
- [ ] reusable payloads belong under `fixtures/domains/flora/` unless there is a test-local reason
- [ ] every fixture declares source role, attempted claim type, expected outcome, and expected reason code
- [ ] role enum values are limited to `observed`, `regulatory`, `modeled`, `aggregate`, `administrative`, `candidate`, and `synthetic`
- [ ] role upgrades or downcasts through promotion are denied, not silently corrected
- [ ] `DENY` fixtures do not expose blocked rare-plant, steward-only, or source-controlled values
- [ ] `ABSTAIN` fixtures make the missing role/evidence/citation/review support explicit
- [ ] `ERROR` fixtures distinguish malformed state from policy denial
- [ ] test-local wrappers do not become a parallel fixture authority
- [ ] release-shaped refs remain synthetic and do not authorize publication
- [ ] docs, tests, schemas, contracts, source registries, and policy references are updated when source-role behavior changes

---

## Change discipline

Changes to this lane should be small, inspectable, and reversible.

| Change type | Required action |
|---|---|
| Add a role-collapse fixture | Add source role, attempted claim type, expected outcome, expected reason code, and no-network posture. |
| Add a `ROLE_DOWNCAST_FORBIDDEN` fixture | State original role, attempted role, attempted transition, and correction requirement. |
| Add a source-family example | Keep it synthetic and point to reusable fixtures/source docs rather than creating source authority. |
| Add a rare-plant role case | Use synthetic placeholders only; do not include exact sensitive coordinates or steward-only locality. |
| Add release-shaped material | Keep it synthetic and non-authorizing; real release objects belong under `release/`. |
| Discover real data in this lane | Move it out, quarantine through the governed lifecycle or registry process, and record the correction path. |

---

## Verification status

- Target README: replaced placeholder content.
- Path convention: `tests/fixtures/flora/source_role_collapse/` is named by the Flora verification backlog for source-role anti-collapse negative fixtures; it is treated here as compatibility/test-local, not canonical fixture-root authority.
- Canonical Flora fixture root: verified as present and README-backed during authoring.
- Fixture payload inventory: not exhaustively verified in this update.
- Source-role alignment: verified against `docs/domains/flora/SOURCE_ROLES.md` for seven-role enum, role-claim matrix, role-collapse failure modes, role fixed at admission, and reason-code backlog.
- Flora backlog alignment: verified against `docs/domains/flora/VERIFICATION_BACKLOG.md` for FLO-VB-015 and its named negative-fixture-set path.
- Flora canonical path alignment: verified against `docs/domains/flora/CANONICAL_PATHS.md` for domain-placement, test/fixture lane, lifecycle, no-network first-slice, and connector non-publisher posture.
- Contract/schema alignment: NEEDS VERIFICATION against `SourceDescriptor` schema fields and validator reason-code wiring.
- Consumer alignment: NEEDS VERIFICATION against Flora validators, source-admission tests, governed-API tests, Evidence Drawer checks, Focus Mode checks, release-manifest checks, policy checks, source-role checks, and CI coverage.
- Tests and validators: NOT RUN.
