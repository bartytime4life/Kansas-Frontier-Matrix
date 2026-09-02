<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-habitat-test-source-descriptors-readme
title: Habitat Source Descriptor Test README
type: test-readme
version: v0.1
status: draft; placeholder-expanded; test-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Habitat domain steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Rights reviewer
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — QA steward
created: NEEDS VERIFICATION — blank placeholder existed before v0.1 expansion
updated: 2026-07-05
policy_label: public-doc; tests; habitat; source-descriptors; no-network; admission-control; source-role-aware; rights-aware; cadence-aware; descriptor-not-payload; release-gated
tags: [kfm, tests, habitat, source-descriptors, test_source_descriptors, SourceDescriptor, SourceActivationDecision, source-role, rights, cadence, source-head, native-classification, evidence, policy, registry, admission, ABSTAIN, DENY]
related:
  - ../../../README.md
  - ../README.md
  - ../../../../docs/domains/habitat/SOURCE_FAMILIES.md
  - ../../../../docs/domains/habitat/SOURCE_REGISTRY.md
  - ../../../../docs/domains/habitat/SOURCE_REFRESH_RUNBOOK.md
  - ../../../../docs/domains/habitat/HABITAT_SOURCE_LEDGER.md
  - ../../../../data/registry/sources/habitat/README.md
  - ../../../../data/registry/sources/habitat/ecoregions/README.md
  - ../../../../data/registry/habitat/README.md
  - ../../../../data/registry/habitat/sources/README.md
  - ../../../../schemas/contracts/v1/source/source-descriptor.json
  - ../../../../policy/domains/habitat/
  - ../../../../policy/sensitivity/habitat/
  - ../../../../data/raw/habitat/
  - ../../../../data/work/habitat/
  - ../../../../data/quarantine/habitat/
  - ../../../../data/processed/habitat/
  - ../../../../release/manifests/habitat/
notes:
  - "This file replaces a blank placeholder at tests/domains/habitat/test_source_descriptors/README.md."
  - "This is a test-lane README only. It does not define Habitat source descriptors, source-family doctrine, source registries, schemas, fixtures, lifecycle records, evidence bundles, policy rules, release decisions, pipeline code, public API material, public map material, public tiles, or published artifacts."
  - "The tested invariant is that Habitat source-descriptor tests verify source admission metadata, role clarity, rights posture, cadence, native classification, source-head tracking, activation posture, and registry/lifecycle separation without turning descriptors into source payloads, EvidenceBundles, proof closure, catalog closure, policy decisions, release authority, public-layer truth, or AI/UI truth."
  - "Default posture is deterministic and no-network. Live source checks, real source exports, lifecycle data, public tiles, and restricted joined records do not belong in this lane."
  - "Rollback target for this replacement is previous blank blob SHA 8b137891791fe96927ad78e64b0aad7bded08bdc."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat source-descriptor tests

> Deterministic, no-network test documentation for proving that Habitat `SourceDescriptor` records remain admission and authority-control metadata, not source payloads, proof closure, policy decisions, release authority, public outputs, or AI truth.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Lane: source descriptors" src="https://img.shields.io/badge/lane-source__descriptors-blue">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: descriptor not payload" src="https://img.shields.io/badge/boundary-descriptor__not__payload-success">
</p>

**Path:** `tests/domains/habitat/test_source_descriptors/README.md`  
**Status:** draft / placeholder-expanded / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Domain segment:** `habitat`  
**Test lane:** `test_source_descriptors`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target was a blank placeholder before this expansion · CONFIRMED `tests/` is the canonical root for enforceability proof · CONFIRMED Habitat source-family docs say `SourceDescriptor` records under `data/registry/sources/` are the append-only authority and dossiers are descriptive · CONFIRMED `data/registry/sources/habitat/README.md` defines that registry lane as source admission metadata, not payload storage or public output · NEEDS VERIFICATION for executable test modules, descriptor fixture inventory, active source-descriptor schema shape, validator behavior, registry topology, activation-decision objects, policy runtime, CI coverage, and pass rates.

**Quick jumps:** [Purpose](#purpose) · [Placement basis](#placement-basis) · [Invariant under test](#invariant-under-test) · [Expected scope](#expected-scope) · [Fixture posture](#fixture-posture) · [Assertions](#assertions) · [Finite outcomes](#finite-outcomes) · [Forbidden shortcuts](#forbidden-shortcuts) · [Suggested layout](#suggested-layout) · [Run posture](#run-posture) · [Evidence ledger](#evidence-ledger) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

---

## Purpose

`tests/domains/habitat/test_source_descriptors/` is the intended home for Habitat source-descriptor tests.

This lane should prove that Habitat source descriptors preserve source identity, source role, rights, terms, attribution, cadence, steward/reviewer posture, source vintage, source head, native classification, sensitivity posture, activation state, evidence pointers, correction references, and rollback targets without becoming source payloads or public truth.

A passing test here should **not** mean that a real source is activated, a real source payload is admitted, a Habitat claim is proven, or a public layer is released. It should mean only that descriptor guardrails behaved as expected against bounded fixtures.

---

## Placement basis

`tests/` is the canonical root for enforceability proof. Habitat is a domain segment inside that root. `test_source_descriptors` is a test lane, not a source registry, lifecycle, schema, policy, release, proof, or public-map home.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Habitat source-descriptor tests | `tests/domains/habitat/test_source_descriptors/` | This directory. |
| Source-family dossiers | `docs/domains/habitat/SOURCE_FAMILIES.md` | Descriptive dossiers; tests do not redefine them. |
| Habitat source registry docs | `docs/domains/habitat/SOURCE_REGISTRY.md` and related Habitat source docs | Maintainer-facing registry guidance; tests verify boundaries. |
| Machine-readable source registry | `data/registry/sources/habitat/` | Descriptor/admission metadata under test; not owned here. |
| Active descriptor schema | `schemas/contracts/v1/source/source-descriptor.json` or accepted successor | Shape checks where accepted. |
| Raw/work/quarantine payloads | `data/raw/habitat/`, `data/work/habitat/`, `data/quarantine/habitat/` | Source payload lifecycle homes; tests must not store payloads. |
| Policy and sensitivity homes | `policy/domains/habitat/`, `policy/sensitivity/habitat/` | Referenced by tests, not bypassed here. |
| Release decisions | `release/` and `release/manifests/habitat/` | Publication, correction, and rollback authority; tests cannot replace it. |

---

## Invariant under test

> **Descriptor controls admission; descriptor does not prove claims.** A Habitat `SourceDescriptor` records how a source may be treated before and during governed intake. It does not store the source payload, close evidence, approve policy, publish artifacts, or authorize public UI use.

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Source identity | Stable source ID, provider, product, native version, source vintage, and source-head metadata are explicit. | validation failure / `ERROR`. |
| Source role | Role is explicit and not inferred from filename, provider name, map appearance, or convenience. | validation failure / `ABSTAIN`. |
| Rights and cadence | Rights, terms, attribution, cadence, steward, and reviewer posture are explicit or held. | hold / validation failure. |
| Native classification | Native classes and versions remain visible; crosswalks are advisory and separate. | validation failure. |
| Activation posture | Activation decision or hold/deny state is explicit before controlled intake. | hold / `DENY`. |
| Registry/lifecycle split | Descriptor metadata does not become raw payload, processed artifact, catalog closure, proof, policy, or release. | validation failure. |
| Public boundary | Public clients do not read registry internals or unreleased descriptor candidates. | `DENY` / validation failure. |
| No authority upgrade | Descriptor cannot become EvidenceBundle, proof closure, release manifest, public layer truth, or AI truth. | validation failure / `ABSTAIN`. |

---

## Expected scope

Tests in this lane may validate:

- required descriptor identity, source role, native version, source vintage, source head, rights, terms, attribution, cadence, steward, reviewer, sensitivity, and authority-limit fields where accepted;
- denial or hold when rights, cadence, source role, source head, or sensitivity posture is missing;
- role anti-collapse across observed, regulatory, modeled, aggregate, administrative, candidate, and synthetic source families;
- preservation of native classifications and rejection of silent crosswalk substitution;
- rejection of registry entries that store source payloads, proof packs, policy rules, release manifests, public tiles, or API/UI artifacts;
- finite outcomes when descriptor schema, evidence resolver, policy runtime, activation decision, or registry topology is unresolved.

Live source checks, live downloads, production credentials, public tile generation, and real payload storage are out of scope for the default suite.

---

## Fixture posture

Use synthetic, public-safe descriptor fixtures only.

Fixture requirements:

- deterministic and no-network;
- compact enough for review in a PR;
- explicit expected outcome;
- explicit source ID, source role, rights posture, cadence, native version, source vintage, source head, steward/reviewer, sensitivity posture, activation posture, evidence pointer posture, correction, and rollback posture where material;
- no real source exports, lifecycle data, public tiles, credentials, production tokens, or published artifacts.

Preferred fixture families:

| Fixture kind | Expected outcome |
|---|---|
| Valid synthetic descriptor with role, rights, cadence, native version, and activation posture | accepted descriptor support only. |
| Missing source role | validation failure / `ABSTAIN`. |
| Missing rights or terms | hold / `DENY` / validation failure. |
| Native classification overwritten by crosswalk | validation failure. |
| Descriptor contains payload-like data | validation failure. |
| Public client consumes registry candidate | `DENY`. |
| Test pass treated as source activation or release approval | validation failure. |
| AI/UI answer treats descriptor as evidence closure | `ABSTAIN` / validation failure. |

---

## Assertions

A useful Habitat source-descriptor test should make the admission-control boundary obvious.

### Positive path

- source identity, role, rights, cadence, source vintage, and source-head posture are explicit;
- native classification and crosswalk posture are separated;
- activation, hold, restricted, deny, stale, superseded, correction, and rollback states are visible where material;
- downstream lifecycle, evidence, policy, catalog, proof, release, API, map, and AI surfaces remain separate.

### Negative path

- descriptor cannot store payloads;
- descriptor cannot activate a source by file existence alone;
- descriptor cannot become observation truth, regulatory truth, model truth, proof closure, or release authority;
- registry internals cannot be read by normal public UI/API surfaces;
- test pass cannot become source activation or public release;
- missing role, rights, cadence, or evidence produces hold/deny/abstain rather than a fluent claim.

---

## Finite outcomes

| Condition | Expected outcome |
|---|---|
| Valid synthetic descriptor with role, rights, cadence, source-head, activation posture, correction, and rollback context | accepted descriptor support only. |
| Missing source identity, role, rights, cadence, native version, or source head | validation failure / hold / `ABSTAIN`. |
| Descriptor attempts to store source payload or release artifact | validation failure. |
| Descriptor treated as evidence closure, policy approval, catalog closure, source activation, or release authority | validation failure. |
| Public-facing surface requests registry candidate/internal descriptor | `DENY`. |
| Policy engine unavailable | `ERROR` or `ABSTAIN`, never public exposure. |

---

## Forbidden shortcuts

Do not use this test lane to:

- fetch live upstream source systems;
- store real source exports, lifecycle data, source-native tables, public tiles, or release artifacts;
- store credentials, tokens, API keys, cookies, production endpoints, or restricted access details;
- store proof packs, EvidenceBundles, release manifests, source payloads, policy rules, or generated public layers;
- redefine Habitat source-family doctrine, source-descriptor schemas, registry topology, policy rules, receipts, proofs, release decisions, renderer code, or production code;
- infer source activation from file existence, folder name, fixture success, test success, source family name, layer name, map rendering, tile availability, or AI wording;
- publish, promote, activate, or release anything.

Any test that needs live source checking belongs in a gated integration tier with source admission, lifecycle state, policy, receipts, release controls, and rollback targets.

---

## Suggested layout

The exact test module names remain **NEEDS VERIFICATION** until the runner and existing conventions are inspected.

```text
tests/domains/habitat/test_source_descriptors/
├── README.md
├── test_descriptor_identity.py
├── test_source_role_required.py
├── test_rights_and_cadence_required.py
├── test_native_classification_preserved.py
├── test_descriptor_not_payload.py
├── test_activation_and_release_boundaries.py
└── test_public_surface_denies_registry_candidates.py
```

---

## Run posture

```bash
pytest tests/domains/habitat/test_source_descriptors
```

Status of the command above: **PROPOSED / NEEDS VERIFICATION**. It assumes `pytest` is the accepted test runner and that executable test modules exist. This README does not claim the command currently passes.

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `tests/domains/habitat/test_source_descriptors/README.md` existed as a blank placeholder before this replacement. | Did not define the lane. |
| `tests/README.md` | CONFIRMED | `tests/` is enforceability proof and failure should block promotion where trust-spine checks fail. | Does not prove this lane's modules or pass rate. |
| `docs/domains/habitat/SOURCE_FAMILIES.md` | CONFIRMED docs-side source dossier | Habitat source-family docs say dossiers are descriptive and SourceDescriptor records under `data/registry/sources/` are append-only authority. | Rights/terms and per-family role assignments remain NEEDS VERIFICATION unless descriptor records prove them. |
| `data/registry/sources/habitat/README.md` | CONFIRMED registry orientation | Habitat source registry records are admission/authority-control records and not payloads, proof closure, catalog closure, policy, release authority, public output, or public UI material. | Registry topology has unresolved subtype-first/domain-first companion paths. |
| Repo search | CONFIRMED | Habitat source-family, source-refresh, source-registry, registry, raw, work, and context paths exist or are referenced. | Search is not proof of executable tests, fixture inventory, active schema fields, or CI behavior. |

---

## Validation checklist

Before treating this README as implemented behavior, verify:

- [ ] Executable test modules exist under this lane.
- [ ] Test runner and import paths match the repo's accepted convention.
- [ ] Synthetic descriptor fixtures exist for valid, missing role, missing rights, missing cadence, missing source head, crosswalk overwrite, descriptor-as-payload, candidate-public-read, and release-boundary cases.
- [ ] Active SourceDescriptor schema path and required fields are accepted.
- [ ] Habitat registry topology between `data/registry/sources/habitat/`, `data/registry/habitat/`, and `data/registry/habitat/sources/` is resolved or explicitly tolerated.
- [ ] SourceActivationDecision behavior is available to tests or safely stubbed.
- [ ] EvidenceRef / EvidenceBundle behavior is available to tests or safely stubbed.
- [ ] PolicyDecision, ReviewRecord, ReleaseManifest, CorrectionNotice, RedactionReceipt, and RollbackCard expectations are defined before enforcing them.
- [ ] CI runs the no-network Habitat source-descriptor suite.
- [ ] Failures block source admission, public carrier promotion, or release candidate approval where material.

---

## Rollback

Rollback is required if this lane becomes a live source-fetcher, source export store, lifecycle data store, registry authority, fixture root, schema authority, policy authority, proof store, release-decision root, public map/API/tile surface, AI surface, renderer implementation, pipeline implementation, or publication shortcut.

Rollback target for this replacement: previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
