<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-fixtures-hydrology-readme
title: Hydrology Compatibility Test Fixtures README
type: test-fixture-readme
version: v0.1
status: draft; placeholder-replaced; hydrology-compatibility-test-fixture-parent; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD - Hydrology domain steward
  - OWNER_TBD - Fixture steward
  - OWNER_TBD - Runtime/API steward
  - OWNER_TBD - QA steward
  - OWNER_TBD - Evidence steward
  - OWNER_TBD - Policy steward
  - OWNER_TBD - Release steward
created: 2026-07-06
updated: 2026-07-06
policy_label: public-doc; tests; fixtures; hydrology; compatibility-path; synthetic-only; no-network; public-safe; source-role-aware; temporal-role-aware; evidence-bound; policy-gated; release-gated; rollback-aware
tags: [kfm, tests, fixtures, hydrology, compatibility-fixtures, decision-envelope, EvidenceBundle, RunReceipt, SourceDescriptor, source-role, RuntimeResponseEnvelope, ANSWER, ABSTAIN, DENY, ERROR, no-network, public-safe]
related:
  - ../README.md
  - ../../README.md
  - ../../domains/hydrology/README.md
  - ../../domains/hydrology/runtime_proof/README.md
  - ../../fixtures/domains/hydrology/README.md
  - ../../../fixtures/domains/hydrology/README.md
  - ../../../fixtures/domains/hydrology/decision_envelope/README.md
  - ../../../fixtures/domains/hydrology/evidence_bundle/README.md
  - ../../../fixtures/domains/hydrology/run_receipt/README.md
  - ../../../fixtures/domains/hydrology/sources/README.md
  - ../../../fixtures/domains/hydrology/valid/README.md
  - ../../../fixtures/domains/hydrology/invalid/README.md
  - ../../../fixtures/domains/hydrology/negative/README.md
  - ../../../fixtures/domains/hydrology/golden/README.md
  - ../../../docs/domains/hydrology/README.md
  - ../../../docs/domains/hydrology/CANONICAL_PATHS.md
  - ../../../docs/domains/hydrology/API_CONTRACTS.md
  - ../../../docs/domains/hydrology/BOUNDARY.md
  - ../../../docs/domains/hydrology/SOURCE_REGISTRY.md
  - ../../../docs/domains/hydrology/SOURCE_ROLE_MATRIX.md
  - ../../../contracts/domains/hydrology/
  - ../../../schemas/contracts/v1/domains/hydrology/
  - ../../../schemas/contracts/v1/runtime/
  - ../../../schemas/contracts/v1/evidence/
  - ../../../schemas/contracts/v1/source/
  - ../../../policy/domains/hydrology/
  - ../../../policy/sensitivity/hydrology/
  - ../../../data/registry/sources/hydrology/
  - ../../../release/candidates/hydrology/
notes:
  - "This README replaces placeholder content at tests/fixtures/hydrology/README.md."
  - "This path is a compatibility/test-local parent lane for Hydrology fixture wrappers and smoke-test inputs. It intentionally does not become the canonical reusable Hydrology fixture root."
  - "Canonical reusable Hydrology fixtures live under fixtures/domains/hydrology/. Domain-scoped executable tests live under tests/domains/hydrology/."
  - "Fixture success is not evidence closure, source admission, policy approval, release approval, public-map authority, hydrology truth, or implementation proof."
  - "Executable tests, fixture payload inventory, validator/runtime wiring, CI jobs, and pass rates remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hydrology compatibility test fixtures

> Parent README for compatibility/test-local Hydrology fixtures under `tests/fixtures/hydrology/`. This path supports narrow unit-test-scoped fixture wrappers without replacing the canonical reusable fixture root at `fixtures/domains/hydrology/` or the executable domain-test root at `tests/domains/hydrology/`.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Lane: compatibility fixtures" src="https://img.shields.io/badge/lane-compatibility__fixtures-purple">
  <img alt="Domain: hydrology" src="https://img.shields.io/badge/domain-hydrology-blue">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: not canonical fixture root" src="https://img.shields.io/badge/boundary-not__canonical__fixture__root-critical">
</p>

**Path:** `tests/fixtures/hydrology/README.md`  
**Status:** draft / placeholder replaced / compatibility test-fixture parent / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Lane family:** `fixtures/hydrology`  
**Canonical reusable fixture root:** `fixtures/domains/hydrology/`  
**Canonical domain test root:** `tests/domains/hydrology/`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target file existed as placeholder content before replacement; CONFIRMED `tests/README.md` allows `tests/fixtures/` only as unit-test-scoped fixtures and separates it from root `fixtures/`; CONFIRMED `fixtures/domains/hydrology/` is the reusable Hydrology fixture root with decision-envelope, evidence-bundle, run-receipt, source, valid, invalid, negative, and golden child lanes; NEEDS VERIFICATION for executable tests, payload inventory, runtime/validator wiring, CI coverage, and pass rates.

---

## Purpose

`tests/fixtures/hydrology/` is a compatibility/test-local parent lane for Hydrology fixture wrappers and smoke-test inputs.

Use this lane only when a test-local fixture needs to sit under `tests/fixtures/` rather than the canonical reusable fixture root. It may hold compact manifests, wrapper examples, expected-outcome notes, or local parametrization material that points back to reusable Hydrology fixtures under `fixtures/domains/hydrology/`.

A fixture under this parent should not mean that a water condition is current, a gauge value has been admitted, a flood or groundwater claim is verified, an NFHL zone has been treated as observed inundation, a source descriptor is admitted, a policy decision is approved, a public layer is safe, or a release is published. It should mean only that a bounded synthetic fixture supports a bounded test expectation.

[Back to top](#top)

---

## Placement basis

`tests/README.md` disambiguates fixture homes: `tests/fixtures/` is for unit-test-scoped fixtures local to a test's needs, while root `fixtures/` is for cross-cutting golden, valid, invalid, and synthetic fixtures shared across test areas and pipelines. Hydrology already has a canonical reusable fixture root at `fixtures/domains/hydrology/`, so this requested path must stay compatibility/test-local.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Compatibility/test-local Hydrology fixture wrappers | `tests/fixtures/hydrology/` | This directory. |
| Executable Hydrology tests | `tests/domains/hydrology/` | Consumers and validators; not fixture authority. |
| Reusable Hydrology fixtures | `fixtures/domains/hydrology/` | Canonical reusable fixture root; referenced, not replaced. |
| Decision-envelope examples | `fixtures/domains/hydrology/decision_envelope/` | Reusable finite-outcome/runtime examples. |
| EvidenceBundle-like examples | `fixtures/domains/hydrology/evidence_bundle/` | Reusable evidence-support examples. |
| RunReceipt-like examples | `fixtures/domains/hydrology/run_receipt/` | Reusable provenance/replay examples. |
| Source-like examples | `fixtures/domains/hydrology/sources/` | Reusable source-role, rights, sensitivity, cadence, and source-head examples. |
| Semantic contracts | `contracts/domains/hydrology/` | Defines object meaning; not owned here. |
| Machine schemas | `schemas/contracts/v1/domains/hydrology/`, runtime, evidence, and source schema roots | Defines accepted shape; not owned here. |
| Policy authority | `policy/domains/hydrology/` and `policy/sensitivity/hydrology/` | Referenced by expected outcomes; not defined here. |
| Source registry | `data/registry/sources/hydrology/` | Source identity, role, rights, sensitivity, cadence, and freshness records; not owned here. |
| Release decisions | `release/` roots | Referenced through synthetic refs; not decided here. |

> [!IMPORTANT]
> Do not expand this parent into a second Hydrology fixture root. Prefer `fixtures/domains/hydrology/` for reusable payloads and use this path only for test-local wrappers, temporary manifests, and unit-test-scoped compatibility material.

---

## Expected child lanes

This parent currently has no verified child README inventory in this update. Future child lanes may be added only when a test suite, backlog row, or parent README justifies the `tests/fixtures/hydrology/` compatibility path instead of `fixtures/domains/hydrology/`.

Potential child lanes remain PROPOSED:

| Child lane | Purpose | Expected posture |
|---|---|---|
| `runtime/` | Test-local wrappers for Hydrology runtime finite outcomes. | Synthetic, no-network, finite outcome only. |
| `source_role/` | Test-local canaries for NFHL/NWIS/NHD/model/source-role mismatch. | Synthetic, no-network, fail-closed. |
| `temporal/` | Test-local canaries proving observed/source/retrieval/release/expiry times do not collapse. | Synthetic, no-network, time roles explicit. |
| `policy/` | Test-local denial and abstention examples for sensitive precision, rights, release, and public-safe exposure. | Synthetic, no-network, fail-closed. |

---

## Invariant under test

> **Hydrology fixtures are downstream test carriers, not Hydrology truth.** A passing fixture under this parent proves only a bounded test expectation, never source admission, evidence closure, policy approval, release approval, public-map authority, or implementation maturity.

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Parent-boundary check | `tests/fixtures/hydrology/` remains compatibility/test-local, not canonical fixture authority. | drift entry / validation failure. |
| Canonical fixture-root check | Reusable payloads are placed under or referenced from `fixtures/domains/hydrology/`. | validation failure. |
| Synthetic-only check | Fixtures use fake IDs, toy source refs, toy timestamps, toy geometry, toy gauge values, and synthetic refs. | quarantine / validation failure. |
| No-network check | Fixture loaders do not call live USGS, FEMA, NOAA, state water offices, public APIs, map services, model runtimes, or release services. | `ERROR`. |
| Source-role check | NFHL regulatory context, NWIS observations, NHD/NHDPlus/3DHP reference geometry, models/forecasts, administrative/status context, and synthetic examples remain distinct. | `DENY` / `ABSTAIN`. |
| Temporal-role check | Observed time, valid time, source time, retrieval time, release time, expiry time, and stale-state markers remain separate where material. | `DENY` / `ABSTAIN`. |
| Evidence check | Claim-like `ANSWER` fixtures require synthetic EvidenceRef / EvidenceBundle closure or abstain. | `ABSTAIN`. |
| Policy check | Rights, sensitivity, release state, review state, source role, freshness, public geometry, and precision blockers fail closed. | `DENY` / `ABSTAIN`. |
| Emergency-system check | Fixtures never present KFM as an emergency warning, flood instruction, evacuation, or operational alert system. | `DENY`. |
| Release check | Release-shaped refs remain synthetic and do not authorize publication. | promotion block. |

---

## Accepted material

Only bounded, synthetic, reviewable material belongs in this lane:

- README files for compatibility/test-local child fixture lanes
- fixture manifests that point to canonical reusable examples under `fixtures/domains/hydrology/`
- synthetic runtime, source-role, temporal, no-network, rights, sensitivity, evidence, policy, release, correction, withdrawal, stale-state, and rollback canaries
- synthetic `RuntimeResponseEnvelope`, `DecisionEnvelope`, `SourceDescriptor`, `EvidenceRef`, `EvidenceBundle`, `RunReceipt`, `PolicyDecision`, `ValidationReport`, `ReviewRecord`, `ReleaseManifest`, `CorrectionNotice`, `WithdrawalNotice`, and `RollbackCard` refs
- synthetic Hydrology references such as toy `GaugeSite`, `FlowObservation`, `WaterLevelObservation`, `WaterQualityObservation`, `GroundwaterWell`, `AquiferObservation`, `Watershed`, `HUCUnit`, `ReachIdentity`, `NFHLZone`, and `Hydrograph` examples
- expected finite outcomes such as `PASS`, `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR`
- small `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.geojson`, `*.md`, or expected-output examples when clearly test-local

Safe outputs may include public-safe fields such as fixture ID, source role, route name, runtime surface, expected outcome, expected reason code, EvidenceRef placeholder, PolicyDecision placeholder, source-head placeholder, validation placeholder, release placeholder, correction placeholder, rollback placeholder, and no-network posture.

---

## Exclusions

Do not place these materials in this lane:

| Excluded material | Why it does not belong here |
|---|---|
| Real source exports, live source responses, production payloads, or public payloads | Default tests must stay synthetic, deterministic, and no-network. |
| Real `SourceDescriptor`s, source activation decisions, license reviews, source-head records, or registry entries | Registry/source authority belongs in `data/registry/sources/hydrology/` and source governance roots. |
| Live gauge readings, flood warnings, advisories, forecasts, evacuation instructions, or operational public-safety guidance | KFM is not an emergency system. |
| Exact sensitive groundwater-well precision, private property/person joins, critical infrastructure exposure, or restricted incident records | Sensitive and rights-limited material must fail closed. |
| Direct reads from RAW, WORK, QUARANTINE, internal stores, unpublished candidates, canonical stores, public APIs, or model runtime outputs | Bypasses the trust membrane and no-network posture. |
| Secrets, credentials, private endpoints, production logs, telemetry, or access tokens | Security and exposure risk. |
| Real EvidenceBundles, ProofPacks, production receipts, release manifests, rollback cards, correction notices, withdrawal notices, public artifacts, or audit ledgers | Governed trust records and release artifacts belong in their own roots. |
| Binding policy rules, schema definitions, contract prose, release procedures, pipeline implementation, connector implementation, map implementation, API implementation, or AI runtime implementation | Authority and implementation belong in their own responsibility roots. |

---

## Suggested layout

```text
tests/fixtures/hydrology/
|-- README.md
|-- manifest_expectations.json
|-- runtime/
|   `-- README.md
|-- source_role/
|   `-- README.md
|-- temporal/
|   `-- README.md
`-- policy/
    `-- README.md
```

Additional files are PROPOSED until executable tests, payload inventories, or verification-backlog rows justify them.

---

## Run posture

No executable runner was verified while authoring this README. Once tests exist, the expected local command should be documented and verified here and in any child READMEs.

```bash
: "PROPOSED / NEEDS VERIFICATION"
pytest tests/domains/hydrology tests/fixtures/hydrology
```

Required run posture: no network access, no live source calls, no direct lifecycle-store reads, no direct model runtime calls, no real secrets, no production logs, no production trust artifacts, no live water/flood/emergency content, no exact sensitive groundwater precision, no public artifact writes, deterministic fixture inputs, and finite outcomes only.

---

## Minimal fixture manifest

Synthetic manifests should describe fixture expectations without carrying real Hydrology data.

```json
{
  "fixture_manifest_id": "hydrology-compat-fixture-public-safe-example",
  "domain": "hydrology",
  "fixture_family": "compatibility_wrapper",
  "canonical_fixture_ref": "fixtures/domains/hydrology/decision_envelope/valid/example-fixture.json",
  "expected_outcome": "PASS",
  "source_role": "synthetic",
  "evidence_ref": "evidence:synthetic:hydrology:compat:example",
  "policy_decision_ref": "policy:synthetic:hydrology:allow-public-safe-example",
  "network": "disabled",
  "uses_real_source_data": false,
  "authorizes_publication": false
}
```

For denial cases, make the denial explicit without carrying restricted or live operational material:

```json
{
  "fixture_manifest_id": "hydrology-compat-fixture-deny-nfhl-as-observed-inundation",
  "domain": "hydrology",
  "fixture_family": "source_role_collapse_denial",
  "source_role": "regulatory_context",
  "attempted_claim_type": "observed_inundation",
  "expected_outcome": "DENY",
  "expected_reason_codes": [
    "SOURCE_ROLE_COLLAPSE_BLOCKED",
    "NFHL_IS_REGULATORY_CONTEXT_NOT_OBSERVED_INUNDATION"
  ],
  "network": "disabled",
  "uses_real_source_data": false,
  "authorizes_publication": false
}
```

---

## Finite outcome expectations

| Outcome | Meaning in this lane | Example |
|---|---|---|
| `PASS` | The synthetic fixture satisfies a bounded test expectation. | A test-local wrapper correctly points to a canonical Hydrology fixture. |
| `ANSWER` | Runtime-oriented fixture has released/evidence-backed, policy-allowed context. | Public-safe hydrology context with synthetic citations. |
| `ABSTAIN` | Evidence, citation, source role, freshness, release, or review support is insufficient. | Missing EvidenceRef for a claim-like water-level answer. |
| `DENY` | Policy, rights, sensitivity, freshness, emergency-system, release, source-role, temporal, or precision checks block exposure. | NFHL-as-observed-inundation or sensitive well-precision canary. |
| `ERROR` | Fixture, loader, schema, or test setup is malformed, unavailable, non-deterministic, or tries to use the network. | Test helper attempts a live source request. |

---

## Maintenance checklist

Before adding or changing material in this lane, verify:

- [ ] the fixture is synthetic, compact, deterministic, public-safe, and no-network
- [ ] reusable payloads belong under `fixtures/domains/hydrology/` unless there is a documented test-local reason
- [ ] each child lane has a README describing purpose, accepted material, exclusions, finite outcomes, and verification status
- [ ] source role, temporal role, evidence state, citation state, rights state, sensitivity state, policy state, review state, release state, correction state, rollback state, and expected outcome are explicit where material
- [ ] regulatory context, observations, reference geometry, model/forecast output, administrative/status context, and synthetic examples are not flattened into one source role
- [ ] `DENY` fixtures do not expose restricted values or operational emergency guidance
- [ ] `ABSTAIN` fixtures make missing support explicit
- [ ] `ERROR` fixtures distinguish malformed state from policy denial
- [ ] test-local wrappers do not become a parallel fixture authority
- [ ] release-shaped refs remain synthetic and do not authorize publication
- [ ] docs, tests, schemas, contracts, source registries, and policy references are updated when behavior changes

---

## Change discipline

Changes to this lane should be small, inspectable, and reversible.

| Change type | Required action |
|---|---|
| Add a child lane | Cite the test suite, backlog item, or parent README that requires `tests/fixtures/hydrology/` instead of `fixtures/domains/hydrology/`. |
| Add a fixture manifest | Add expected outcome, reason code, no-network posture, and synthetic support refs. |
| Add a source-role fixture | Keep source role, attempted claim type, and reason code explicit. |
| Add a temporal fixture | Keep observed/source/retrieval/release/expiry time roles explicit. |
| Add a policy fixture | State denial/abstention reason without exposing restricted or live operational material. |
| Add release-shaped material | Keep it synthetic and non-authorizing; real release objects belong under `release/`. |
| Discover real data in this lane | Move it out, quarantine through the governed lifecycle or registry process, and record the correction path. |

---

## Verification status

- Target README: replaced placeholder content.
- Child README inventory: no child READMEs under `tests/fixtures/hydrology/` were verified during this update.
- Canonical Hydrology fixture root: verified as present and README-backed during authoring.
- Fixture payload inventory: not exhaustively verified in this update.
- Test-root alignment: verified against `tests/README.md` for tests as enforceability proof, optional `tests/fixtures/` split, five-fixture rule, forbidden boundaries, sensitive-fixture safeguards, and deterministic no-network default.
- Hydrology fixture-root alignment: verified against `fixtures/domains/hydrology/README.md` for decision-envelope, evidence-bundle, run-receipt, sources, valid, invalid, negative, golden, accepted-material, exclusion, and shared-design posture.
- Contract/schema alignment: NEEDS VERIFICATION against Hydrology domain schemas, runtime envelope schemas, EvidenceBundle schemas, RunReceipt schemas, SourceDescriptor schemas, and policy bundles.
- Consumer alignment: NEEDS VERIFICATION against Hydrology validators, governed-API tests, decision-envelope checks, evidence-bundle checks, run-receipt checks, source-descriptor checks, source-role checks, temporal checks, drawer checks, Focus Mode checks, layer-manifest checks, citation-validation checks, rights checks, sensitivity checks, source-head checks, trust-membrane checks, release-readiness checks, rollback-readiness checks, renderer checks, and CI coverage.
- Tests and validators: NOT RUN.
