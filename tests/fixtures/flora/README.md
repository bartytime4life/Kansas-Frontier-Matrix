<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-fixtures-flora-readme
title: Flora Compatibility Test Fixtures README
type: test-fixture-readme
version: v0.1
status: draft; placeholder-replaced; flora-compatibility-test-fixture-parent; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD - Flora domain steward
  - OWNER_TBD - Fixture steward
  - OWNER_TBD - Runtime/API steward
  - OWNER_TBD - Source steward
  - OWNER_TBD - QA steward
  - OWNER_TBD - Evidence steward
  - OWNER_TBD - Policy steward
  - OWNER_TBD - Release steward
created: 2026-07-06
updated: 2026-07-06
policy_label: public-doc; tests; fixtures; flora; compatibility-path; synthetic-only; no-network; public-safe; rare-plant-aware; source-role-aware; finite-outcome-aware; evidence-bound; policy-gated; release-gated; rollback-aware
tags: [kfm, tests, fixtures, flora, compatibility-fixtures, runtime, source-role-collapse, RuntimeResponseEnvelope, SourceDescriptor, EvidenceRef, EvidenceBundle, PolicyDecision, ReleaseManifest, ANSWER, ABSTAIN, DENY, ERROR, ROLE_COLLAPSE, ROLE_DOWNCAST_FORBIDDEN]
related:
  - ../README.md
  - ../../README.md
  - ../../domains/flora/README.md
  - ../../domains/flora/runtime_proof/README.md
  - ./runtime/README.md
  - ./source_role_collapse/README.md
  - ../../../fixtures/domains/flora/README.md
  - ../../../fixtures/domains/flora/decision_envelopes/README.md
  - ../../../fixtures/domains/flora/evidence_bundles/README.md
  - ../../../fixtures/domains/flora/source_descriptors/README.md
  - ../../../fixtures/domains/flora/sources/README.md
  - ../../../fixtures/domains/flora/valid/README.md
  - ../../../fixtures/domains/flora/invalid/README.md
  - ../../../fixtures/domains/flora/golden/README.md
  - ../../../docs/domains/flora/README.md
  - ../../../docs/domains/flora/CANONICAL_PATHS.md
  - ../../../docs/domains/flora/VERIFICATION_BACKLOG.md
  - ../../../docs/domains/flora/SOURCE_ROLES.md
  - ../../../docs/domains/flora/SOURCE_REGISTRY.md
  - ../../../docs/domains/flora/THIN_SLICE_PLAN.md
  - ../../../contracts/domains/flora/
  - ../../../schemas/contracts/v1/domains/flora/
  - ../../../schemas/contracts/v1/source/
  - ../../../policy/domains/flora/
  - ../../../policy/sensitivity/flora/
  - ../../../data/registry/sources/flora/
  - ../../../release/candidates/flora/
notes:
  - "This README replaces placeholder content at tests/fixtures/flora/README.md."
  - "This path is a compatibility/test-local parent lane for Flora fixture sets named by the Flora verification backlog, especially runtime finite-outcome fixtures and source-role-collapse negative fixtures."
  - "Canonical reusable Flora fixtures live under fixtures/domains/flora/. Domain-scoped executable tests live under tests/domains/flora/."
  - "This parent README prevents tests/fixtures/flora/ from becoming a parallel canonical fixture root."
  - "Fixture success is not evidence closure, source admission, policy approval, release approval, public-map authority, or implementation proof."
  - "Executable tests, fixture payload inventory, validator/runtime wiring, CI jobs, and pass rates remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Flora compatibility test fixtures

> Parent README for compatibility/test-local Flora fixtures under `tests/fixtures/flora/`. This path supports targeted verification-backlog fixture sets without replacing the canonical reusable fixture root at `fixtures/domains/flora/` or the executable domain-test root at `tests/domains/flora/`.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Lane: compatibility fixtures" src="https://img.shields.io/badge/lane-compatibility__fixtures-purple">
  <img alt="Domain: flora" src="https://img.shields.io/badge/domain-flora-green">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: not canonical fixture root" src="https://img.shields.io/badge/boundary-not__canonical__fixture__root-critical">
</p>

**Path:** `tests/fixtures/flora/README.md`  
**Status:** draft / placeholder replaced / compatibility test-fixture parent / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Lane family:** `fixtures/flora`  
**Canonical reusable fixture root:** `fixtures/domains/flora/`  
**Canonical domain test root:** `tests/domains/flora/`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target file existed as placeholder content before replacement; CONFIRMED child compatibility READMEs exist for `runtime/` and `source_role_collapse/`; CONFIRMED Flora backlog names `tests/fixtures/flora/` for no-network source fixtures, `tests/fixtures/flora/runtime/` for API finite-outcome fixtures, and `tests/fixtures/flora/source_role_collapse/` for source-role anti-collapse negative fixtures; NEEDS VERIFICATION for executable tests, payload inventory, runtime/validator wiring, CI coverage, and pass rates.

---

## Purpose

`tests/fixtures/flora/` is a compatibility/test-local parent lane for Flora fixture sets that were named directly by Flora verification backlog rows.

This lane should organize narrow test-local fixture documentation for checks that need paths under `tests/fixtures/flora/`, while preserving the normal KFM split:

- reusable Flora examples belong under `fixtures/domains/flora/`;
- executable domain tests belong under `tests/domains/flora/`;
- this path hosts compatibility fixture wrappers, manifests, negative canaries, finite-outcome examples, and no-network fixture expectations named by backlog rows.

A fixture under this parent should not mean that a plant occurrence is true, a taxonomic resolution is authoritative, a source descriptor is admitted, an exact rare-plant location is publishable, a policy decision is approved, a public layer is safe, or a release is published. It should mean only that a bounded synthetic fixture supports a bounded test expectation.

[Back to top](#top)

---

## Placement basis

The standard Flora path register places domain tests under `tests/domains/flora/` and reusable fixtures under `fixtures/domains/flora/`. The Flora verification backlog also names several `tests/fixtures/flora/...` settling-evidence paths. This README therefore treats `tests/fixtures/flora/` as a compatibility/test-local parent, not as a competing canonical fixture root.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Compatibility/test-local Flora fixture wrappers | `tests/fixtures/flora/` | This directory. |
| Runtime finite-outcome fixtures | `tests/fixtures/flora/runtime/` | Child lane indexed here. |
| Source-role-collapse negative fixtures | `tests/fixtures/flora/source_role_collapse/` | Child lane indexed here. |
| Executable Flora tests | `tests/domains/flora/` | Consumers and validators; not fixture authority. |
| Reusable Flora fixtures | `fixtures/domains/flora/` | Canonical reusable fixture root; referenced, not replaced. |
| SourceDescriptor examples | `fixtures/domains/flora/source_descriptors/` and `fixtures/domains/flora/sources/` | Reusable examples; this lane may wrap them for test-local purposes. |
| Runtime/API contracts | `contracts/` and `contracts/domains/flora/` | Defines object/envelope meaning; not owned here. |
| Machine schemas | `schemas/contracts/v1/domains/flora/` and `schemas/contracts/v1/source/` | Defines accepted shape; not owned here. |
| Policy authority | `policy/domains/flora/` and `policy/sensitivity/flora/` | Referenced by expected outcomes; not defined here. |
| Source registry | `data/registry/sources/flora/` | Source identity, role, rights, sensitivity, and cadence records; not owned here. |
| Release decisions | `release/` roots | Referenced through synthetic refs; not decided here. |

> [!IMPORTANT]
> Do not expand this parent into a second Flora fixture root. Prefer `fixtures/domains/flora/` for reusable payloads. Use this path only for test-local compatibility wrappers and backlog-named fixture sets.

---

## Child lanes

| Child lane | Purpose | Expected posture |
|---|---|---|
| `runtime/` | Runtime and Focus Mode finite-outcome fixtures covering `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR`. | Synthetic, no-network, evidence/policy/release-aware. |
| `source_role_collapse/` | Negative fixtures for source-role anti-collapse, especially `ROLE_COLLAPSE` and `ROLE_DOWNCAST_FORBIDDEN`. | Synthetic, no-network, fail-closed. |

Future child lanes may be added only when a backlog row, test suite, or parent README justifies this compatibility path instead of `fixtures/domains/flora/`.

---

## Invariant under test

> **Fixtures are downstream test carriers, not truth.** A passing fixture under this parent proves only a bounded test expectation, never source admission, evidence closure, policy approval, release approval, public-map authority, or implementation maturity.

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Parent-boundary check | `tests/fixtures/flora/` remains compatibility/test-local, not canonical fixture authority. | drift entry / validation failure. |
| Canonical fixture-root check | Reusable payloads are placed under or referenced from `fixtures/domains/flora/`. | validation failure. |
| Synthetic-only check | Fixtures use fake IDs, toy taxa, toy sources, toy timestamps, toy geometry, and synthetic refs. | quarantine / validation failure. |
| No-network check | Fixture loaders do not call live source APIs, public APIs, map services, release services, AI runtimes, or external connectors. | `ERROR`. |
| Rare-plant check | Exact sensitive geometry, steward-only locality, culturally sensitive plant knowledge, or protected-taxon side channels fail closed. | `DENY`. |
| Evidence check | Claim-like `ANSWER` fixtures require synthetic EvidenceRef / EvidenceBundle closure or abstain. | `ABSTAIN`. |
| Policy check | Rights, sensitivity, source role, release state, review state, and public-geometry blockers fail closed. | `DENY` / `ABSTAIN`. |
| Release check | Release-shaped refs remain synthetic and do not authorize publication. | promotion block. |

---

## Accepted material

Only bounded, synthetic, reviewable material belongs in this lane:

- README files for compatibility/test-local child fixture lanes
- fixture manifests that point to canonical reusable examples under `fixtures/domains/flora/`
- synthetic runtime, source-role, no-network, rights, sensitivity, evidence, policy, release, correction, and rollback canaries
- synthetic `RuntimeResponseEnvelope`, `DecisionEnvelope`, `SourceDescriptor`, `EvidenceRef`, `EvidenceBundle`, `AIReceipt`, `PolicyDecision`, `RedactionReceipt`, `ValidationReport`, `ReviewRecord`, `ReleaseManifest`, `CorrectionNotice`, `WithdrawalNotice`, and `RollbackCard` refs
- expected finite outcomes such as `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, `ROLE_COLLAPSE`, and `ROLE_DOWNCAST_FORBIDDEN`
- small `*.json`, `*.jsonl`, `*.yaml`, `*.yml`, `*.geojson`, `*.md`, or expected-output examples when clearly test-local

Safe outputs may include public-safe fields such as fixture ID, source role, route name, runtime surface, expected outcome, expected reason code, EvidenceRef placeholder, PolicyDecision placeholder, RedactionReceipt placeholder, release placeholder, correction placeholder, rollback placeholder, and no-network posture.

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
tests/fixtures/flora/
|-- README.md
|-- runtime/
|   `-- README.md
`-- source_role_collapse/
    `-- README.md
```

Additional files are PROPOSED until executable tests, payload inventories, or verification-backlog rows justify them.

---

## Run posture

No executable runner was verified while authoring this README. Once tests exist, the expected local command should be documented and verified here and in the child READMEs.

```bash
: "PROPOSED / NEEDS VERIFICATION"
pytest tests/domains/flora tests/fixtures/flora
```

Required run posture: no network access, no live source calls, no direct lifecycle-store reads, no real secrets, no production logs, no production trust artifacts, no exact sensitive flora locations, no steward-controlled locality data, no public artifact writes, deterministic fixture inputs, and finite outcomes only.

---

## Maintenance checklist

Before adding or changing material in this lane, verify:

- [ ] the fixture is synthetic, compact, deterministic, public-safe, and no-network
- [ ] reusable payloads belong under `fixtures/domains/flora/` unless there is a documented test-local reason
- [ ] each child lane has a README describing purpose, accepted material, exclusions, finite outcomes, and verification status
- [ ] source role, evidence state, citation state, rights state, sensitivity state, policy state, review state, release state, correction state, rollback state, and expected outcome are explicit where material
- [ ] `DENY` fixtures do not expose blocked rare-plant, steward-only, or source-controlled values
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
| Add a child lane | Cite the backlog item, test suite, or parent README that requires `tests/fixtures/flora/` instead of `fixtures/domains/flora/`. |
| Add a fixture manifest | Add expected outcome, reason code, no-network posture, and synthetic support refs. |
| Add a runtime fixture | Prefer `runtime/`; keep `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` outcomes explicit. |
| Add a source-role-collapse fixture | Prefer `source_role_collapse/`; keep source role, attempted claim type, and reason code explicit. |
| Add release-shaped material | Keep it synthetic and non-authorizing; real release objects belong under `release/`. |
| Discover real data in this lane | Move it out, quarantine through the governed lifecycle or registry process, and record the correction path. |

---

## Verification status

- Target README: replaced placeholder content.
- Child README inventory: verified for `runtime/README.md` and `source_role_collapse/README.md` during authoring.
- Canonical Flora fixture root: verified as present and README-backed during authoring.
- Fixture payload inventory: not exhaustively verified in this update.
- Flora backlog alignment: verified against `docs/domains/flora/VERIFICATION_BACKLOG.md` for no-network source fixtures, runtime finite-outcome fixtures, and source-role anti-collapse fixtures.
- Flora canonical path alignment: verified against `docs/domains/flora/CANONICAL_PATHS.md` in preceding Flora fixture updates for domain-placement, test/fixture lane, lifecycle, no-network first-slice, and connector non-publisher posture.
- Contract/schema alignment: NEEDS VERIFICATION against Flora runtime envelope schemas, SourceDescriptor schema fields, and validator reason-code wiring.
- Consumer alignment: NEEDS VERIFICATION against Flora validators, runtime-proof tests, source-admission tests, governed-API tests, Evidence Drawer checks, Focus Mode checks, release-manifest checks, policy checks, source-role checks, and CI coverage.
- Tests and validators: NOT RUN.
