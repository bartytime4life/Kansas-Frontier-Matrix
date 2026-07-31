<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-hydrology-readme
title: Hydrology Domain Tests README
type: test-index-readme
version: v0.2
status: draft; parent-index; identity REMAIN_PROPOSED and unimplemented; bounded EvidenceBundle and separated aquifer-pair shape checks executable
owners:
  - OWNER_TBD — Hydrology domain steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Identity steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Redaction steward
  - OWNER_TBD — Temporal steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — QA steward
created: NEEDS VERIFICATION — greenfield stub existed before v0.1 expansion
updated: 2026-07-31
policy_label: public-doc; tests; hydrology; parent-index; no-network; evidence-bound; source-role-aware; temporal-aware; policy-filtered; release-gated; rollback-aware
tags: [kfm, tests, hydrology, parent-index, enforceability, no-network, fixtures, SourceDescriptor, ReachIdentity, JSON-Schema, PolicyDecision, RedactionReceipt, EvidenceBundle, ReleaseManifest, CorrectionNotice, RollbackCard, ABSTAIN, DENY, ERROR]
related:
  - ../../README.md
  - ../README.md
  - continuity_inventory_check/README.md
  - identity/README.md
  - no_network/README.md
  - policy/README.md
  - redaction/README.md
  - schema/README.md
  - sources/README.md
  - temporal/README.md
  - ../../../docs/domains/hydrology/README.md
  - ../../../docs/domains/hydrology/DATA_LIFECYCLE.md
  - ../../../docs/domains/hydrology/SOURCE_REGISTRY.md
  - ../../../docs/domains/hydrology/SOURCE_ROLE_MATRIX.md
  - ../../../docs/domains/hydrology/IDENTITY_MODEL.md
  - ../../../docs/domains/hydrology/PUBLICATION_POSTURE.md
  - ../../../docs/domains/hydrology/CONTINUITY_INVENTORY.md
  - ../../../contracts/domains/hydrology/
  - ../../../schemas/contracts/v1/domains/hydrology/
  - ../../../fixtures/domains/hydrology/
  - ../../../policy/domains/hydrology/
  - ../../../data/registry/sources/hydrology/
  - ../../../release/manifests/hydrology/
notes:
  - "This file replaces the greenfield stub at tests/domains/hydrology/README.md."
  - "This is a parent test index only. It does not define Hydrology doctrine, contracts, schemas, fixtures, source descriptors, lifecycle records, EvidenceBundles, policy rules, release decisions, pipeline code, public API material, public map material, public tiles, or published artifacts."
  - "The current executable slice checks the proposed Hydrology EvidenceBundle alias plus closed AquiferObservation and AquiferContextLink shapes, valid/invalid fixture polarity, type separation, optional-link behavior, and fail-closed in-process network guards."
  - "The broader parent invariant remains proposed: Hydrology tests should prove enforceable trust boundaries across continuity inventory, identity, no-network discipline, policy gates, redaction/generalization, schemas, source descriptors, temporal state, evidence posture, release relationship, correction, and rollback."
  - "Decision #1886 keeps the common feature-identity tuple REMAIN_PROPOSED; the identity and temporal child lanes document graduation tests but contain no dedicated executable common-profile modules."
  - "Default posture is deterministic and no-network. Live source checks, upstream fetches, real source exports, lifecycle data, public tiles, and restricted records do not belong in default Hydrology tests."
  - "Rollback target for this replacement is previous stub blob SHA 21c112566e721a6a831a263b1fefa1e102b28dee."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hydrology domain tests

> Parent index for Hydrology test lanes. These tests should prove that Hydrology contracts, schemas, fixtures, source descriptors, identity rules, time/freshness state, policy gates, redaction posture, release relationships, correction paths, and rollback targets are enforceable without turning tests into a source feed, lifecycle store, release authority, public surface, or generated truth source.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Domain: hydrology" src="https://img.shields.io/badge/domain-hydrology-2aa1c6">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: tests not release" src="https://img.shields.io/badge/boundary-tests__not__release-success">
</p>

**Path:** `tests/domains/hydrology/README.md`  
**Status:** draft / parent index / common feature identity `REMAIN_PROPOSED` and unimplemented / bounded EvidenceBundle and aquifer-pair shape slices executable

**Owning root:** `tests/`  
**Domain segment:** `hydrology`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED `tests/` is the canonical enforceability root · CONFIRMED three bounded modules exercise EvidenceBundle, AquiferObservation, and AquiferContextLink local shapes with synthetic fixture polarity and network denial · CONFIRMED the Hydrology workflow runs those modules · NEEDS VERIFICATION for endpoint/evidence resolution, every broader lane, policy runtime, release integration, public route/UI behavior, and broader pass rates.

---

## Purpose

`tests/domains/hydrology/` is the Hydrology segment of the KFM test tree.

Its job is to prove Hydrology boundary discipline. A Hydrology test should show that source identity, source role, machine shape, deterministic identity, temporal state, evidence resolution, policy checks, redaction posture, review state, release posture, correction path, and rollback target are preserved through a bounded fixture or implementation path.

A passing test in this subtree should **not** mean that a real source is admitted, a real Hydrology claim is proven, a public layer is safe, current source freshness is validated, or a release is approved. It should mean only that the scoped guardrail behaved as expected.

---

## Parent invariant

> **Hydrology tests prove enforceability; they do not become Hydrology authority.** The subtree may validate Hydrology contracts, schemas, fixtures, source descriptors, source roles, identity rules, temporal posture, policy decisions, redaction receipts, and release readiness, but it must not become a source registry, connector, lifecycle store, proof store, policy root, release root, public API/map/tile surface, or generated truth surface.

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Source-role preservation | Observed, regulatory, modeled, aggregate, administrative, candidate, and synthetic roles remain visible where material. | validation failure / `ABSTAIN`. |
| Proposed common identity | Once accepted, source, mirrored role, temporal scope, profile versions, and digest posture remain stable and auditable. Until then, identity-profile admission is `HOLD`. | validation failure / `ABSTAIN` / `HOLD`. |
| Evidence support | Evidence-dependent claims resolve support or return a finite non-answer. | `ABSTAIN`. |
| Policy posture | Rights, sensitivity, source-role, lifecycle, and release checks return finite outcomes and fail closed where unresolved. | `DENY` / `ABSTAIN` / `ERROR`. |
| Temporal posture | Source vintage, observed time, valid time, retrieval time, release time, stale state, correction, and rollback remain distinct. | validation failure / `ABSTAIN`. |
| Redaction posture | Public-safe transforms are named, deterministic, receipt-backed, and not improvised at the UI or AI edge. | validation failure / `DENY`. |
| Lifecycle boundary | Tests do not read or write RAW / WORK / QUARANTINE / PROCESSED / PUBLISHED as authority unless explicitly in a gated integration tier. | validation failure. |
| Release boundary | Test success does not become release approval, release manifest, correction notice, or rollback card. | promotion block. |

---

## Lane index

| Lane | Primary responsibility | Boundary |
|---|---|---|
| [`continuity_inventory_check/`](continuity_inventory_check/README.md) | Check that the Hydrology continuity inventory remains lineage, disposition, and verification guidance. | Continuity is not implementation proof, source admission, policy approval, or promotion authority. |
| [`identity/`](identity/README.md) | Documentation for the future common-profile suite. | No executable module currently proves the #1886 tuple, SourceDescriptor parity, SpecHash derivation, family profiles, migration, or correction lineage. |
| [`no_network/`](no_network/README.md) | Default offline / fixture-only Hydrology test enforcement. | Default tests do not fetch live sources, call upstream services, read lifecycle stores as authority, or depend on public tiles. |
| [`policy/`](policy/README.md) | Hydrology policy fail-closed checks. | Policy tests prove finite outcomes; they do not approve publication. |
| [`redaction/`](redaction/README.md) | Hydrology redaction/generalization checks. | Redaction is deterministic governance, not presentation polish or release approval. |
| [`schema/`](schema/README.md) | Hydrology contract/schema parity and schema scaffold honesty. | Schemas define machine shape, not evidence closure, policy approval, or release truth. |
| [`sources/`](sources/README.md) | Source descriptor, source-role, rights, cadence, activation, and permitted-claims tests. | Source tests do not admit live sources, run connectors, or prove what a source says. |
| [`temporal/`](temporal/README.md) | Time-kind, cadence, stale-state, correction, and rollback tests. | Temporal tests do not validate current source freshness or run live source checks. |

---

## Expected test families

The documented lanes support these Hydrology trust families:

| Family | Expected proof point |
|---|---|
| Source admission | SourceDescriptor-like fixtures expose source identity, role, rights, cadence, permitted claims, activation state, evidence relationship, policy, correction, and rollback. |
| Identity | Future tests prove the accepted common and family profiles across source/version/role/time/digest posture; decision #1886 prevents treating the planned suite as current behavior. |
| Schema/contract parity | Machine schemas stay paired with semantic contracts and keep scaffold maturity visible. |
| Aquifer responsibility separation | `AquiferObservation` carries the measurement; `AquiferContextLink` carries typed relation metadata and rejects measurement or copied Geology geometry. |
| Temporal state | Time fields and freshness state remain distinct and auditable. |
| Policy | Rights, sensitivity, source-role, evidence, lifecycle, and release gates fail closed where unresolved. |
| Redaction/generalization | Public-safe transforms are deterministic, named, receipt-backed, and release-gated. |
| Continuity governance | Continuity records guide verification without upgrading PROPOSED material to CONFIRMED behavior. |
| No-network discipline | Default tests run from local fixtures, stubs, and local contract/schema files. |

---

## What belongs here

Appropriate contents include:

- deterministic no-network tests;
- compact synthetic fixtures or fixture pointers;
- import and schema smoke checks;
- contract/schema/policy parity checks;
- source-role anti-collapse checks;
- source descriptor and permitted-claims checks;
- temporal/freshness and stale-state checks;
- evidence, policy, release, correction, and rollback gate checks;
- child-lane README files that explain scope, limits, and validation posture.

---

## Forbidden shortcuts

Do not use this subtree to:

- fetch live upstream source systems by default;
- store real source exports, lifecycle data, public tiles, proof artifacts, release artifacts, or generated public layers;
- redefine Hydrology doctrine, contracts, schemas, fixtures, source registries, policy rules, release decisions, renderer code, or production pipeline code;
- infer release state from file existence, test success, source role label, schema pass, layer name, map rendering, tile availability, Focus answer text, or AI wording;
- publish, promote, approve, or release anything.

Any test that needs live source access, production source data, connector execution, or public tile output belongs in a gated integration tier with explicit source admission, lifecycle state, policy, receipts, release controls, correction path, and rollback targets.

---

## Run posture

Accepted bounded command:

```bash
PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
python -m pytest -q -p no:cacheprovider \
  tests/domains/hydrology/test_hydrology_smoke.py \
  tests/domains/hydrology/test_aquifer_observation.py \
  tests/domains/hydrology/test_aquifer_context_link.py
```

This command runs thirteen tests over the proposed EvidenceBundle alias and the
two closed aquifer schemas. It checks synthetic valid/invalid polarity,
optional-link behavior, type separation, and in-process socket/DNS/URL denial.
It does not resolve endpoints or EvidenceRefs or establish source admission,
scientific correctness, policy, review, proof, release, or publication.

Selected broader child-lane commands remain proposed. In particular,
`identity/` and `temporal/` are documentation-only lanes at this snapshot:

```bash
pytest tests/domains/hydrology/continuity_inventory_check
pytest tests/domains/hydrology/identity
pytest tests/domains/hydrology/no_network
pytest tests/domains/hydrology/policy
pytest tests/domains/hydrology/redaction
pytest tests/domains/hydrology/schema
pytest tests/domains/hydrology/sources
pytest tests/domains/hydrology/temporal
```

Status: the bounded command above is **CONFIRMED executable** in the Hydrology
workflow. The broader child-lane commands remain **PROPOSED / NEEDS
VERIFICATION** and must not be inferred from the bounded pass.

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `tests/domains/hydrology/README.md` existed as a greenfield stub before this replacement. | Did not define the parent lane. |
| `tests/README.md` | CONFIRMED | `tests/` is enforceability proof, canonical, trust-bearing, and failure should block promotion where trust-spine checks fail. | Does not prove Hydrology executable modules or pass rate. |
| `test_hydrology_smoke.py`, the EvidenceBundle alias schema/wrapper, and its fixture pair | CONFIRMED bounded executable slice | Local alias shape, valid/invalid polarity, and fail-closed process-level network guards. | Does not prove EvidenceRef resolution, EvidenceBundle closure, source or semantic validity, policy, proof, release, or publication. |
| `test_aquifer_observation.py` and `test_aquifer_context_link.py` with their schemas, wrappers, and fixtures | CONFIRMED bounded executable slice | Closed local shapes, valid/invalid polarity, optional observation links, typed endpoints, responsibility separation, and network denial. | Does not prove endpoint resolution, aquifer membership, real source validity, evidence, policy, proof, release, or publication. |
| Child README files under this subtree | CONFIRMED for files updated in this documentation pass | Provide lane-specific scope and boundary statements. | Do not prove executable tests, fixtures, validators, CI, or release wiring. |
| `docs/domains/hydrology/DATA_LIFECYCLE.md` | CONFIRMED doctrine / PROPOSED implementation | Provides Hydrology lifecycle, source-role, source-vintage, evidence, release, correction, and rollback posture. | Concrete validators, fixtures, routes, policy runtime, and pass rates remain NEEDS VERIFICATION. |
| `docs/domains/hydrology/SOURCE_REGISTRY.md` and `SOURCE_ROLE_MATRIX.md` | CONFIRMED doctrine / PROPOSED implementation | Provide source admission, source-role, rights, cadence, permitted-claims, and fail-closed posture. | Machine enforcement remains NEEDS VERIFICATION. |
| `docs/domains/hydrology/PUBLICATION_POSTURE.md` | CONFIRMED doctrine / PROPOSED realization | Provides publish/hold/deny, release, stale-state, correction, rollback, and public-safe posture. | Documentation evidence only; runtime remains NEEDS VERIFICATION. |

---

## Validation checklist

Before treating this parent README as implemented behavior, verify:

- [x] One bounded EvidenceBundle alias-shape module executes with valid/invalid fixture polarity and fail-closed process-level network guards.
- [x] Two bounded aquifer-pair modules execute with closed shapes, fixture
  polarity, separation assertions, and fail-closed network guards.
- [ ] Executable test modules exist for each documented lane or the lane is explicitly documentation-only.
- [ ] Test runner and import paths match the repo's accepted convention.
- [ ] Synthetic fixtures exist in accepted fixture homes and are not source payloads.
- [ ] Schema paths and field expectations are accepted beyond scaffold status where tests enforce them.
- [ ] SourceDescriptor and source-role behavior are available to tests or safely stubbed.
- [ ] Common `identity_profile` and per-family `family_profile` are accepted;
      legacy-profile, profile-mismatch, role-parity, canonical-equivalence,
      rotation, correction, migration, and rollback fixtures exist.
- [ ] EvidenceRef resolution and EvidenceBundle closure behavior is available to tests or safely stubbed; alias shape alone is insufficient.
- [ ] PolicyDecision, RuntimeResponseEnvelope, ReleaseManifest, CorrectionNotice, RedactionReceipt, and RollbackCard expectations are defined before enforcing them.
- [x] CI runs the three bounded no-network schema slices and marks incomplete
  lanes as held.
- [ ] Failures block public carrier promotion or release candidate approval where material.

---

## Rollback

Rollback is required if this parent lane becomes a live source-fetcher, connector implementation, lifecycle data store, fixture authority, source registry, contract root, schema authority, policy authority, proof store, release-decision root, public map/API/tile surface, AI surface, renderer implementation, pipeline implementation, or publication shortcut.

Rollback target for this replacement: previous stub blob SHA `21c112566e721a6a831a263b1fefa1e102b28dee`.

<p align="right"><a href="#top">Back to top</a></p>
