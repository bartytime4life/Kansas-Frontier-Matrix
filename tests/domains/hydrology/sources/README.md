<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tests-domains-hydrology-sources-readme
title: Hydrology Sources Test README
type: test-readme
version: v0.1
status: draft; placeholder-expanded; sources-test-lane; PROPOSED / NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Hydrology domain steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Evidence steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — QA steward
created: NEEDS VERIFICATION — blank placeholder existed before v0.1 expansion
updated: 2026-07-05
policy_label: public-doc; tests; hydrology; sources; source-descriptor; no-network; source-role-aware; rights-aware; cadence-aware; evidence-bound; release-gated; rollback-aware
tags: [kfm, tests, hydrology, sources, SourceDescriptor, SourceActivationDecision, source-role, permitted-claims, not-authoritative-for, rights, cadence, freshness, EvidenceBundle, PolicyDecision, ReleaseManifest, CorrectionNotice, RollbackCard, ABSTAIN, DENY, ERROR]
related:
  - ../../../README.md
  - ../README.md
  - ../policy/README.md
  - ../no_network/README.md
  - ../schema/README.md
  - ../identity/README.md
  - ../../../../docs/domains/hydrology/SOURCE_REGISTRY.md
  - ../../../../docs/domains/hydrology/SOURCE_ROLE_MATRIX.md
  - ../../../../docs/domains/hydrology/SOURCE_FAMILIES.md
  - ../../../../docs/domains/hydrology/PUBLICATION_POSTURE.md
  - ../../../../docs/domains/hydrology/DATA_LIFECYCLE.md
  - ../../../../docs/domains/hydrology/IDENTITY_MODEL.md
  - ../../../../data/registry/sources/hydrology/
  - ../../../../data/registry/hydrology/sources/README.md
  - ../../../../schemas/contracts/v1/source/source-descriptor.json
  - ../../../../contracts/source/SOURCE_DESCRIPTOR.md
  - ../../../../contracts/domains/hydrology/
  - ../../../../schemas/contracts/v1/domains/hydrology/
  - ../../../../fixtures/domains/hydrology/sources/
  - ../../../../policy/domains/hydrology/
  - ../../../../policy/sensitivity/hydrology/
  - ../../../../release/manifests/hydrology/
notes:
  - "This file replaces a blank placeholder at tests/domains/hydrology/sources/README.md."
  - "This is a test-lane README only. It does not define Hydrology doctrine, source registry doctrine, source descriptors, connector behavior, schemas, fixtures, lifecycle records, EvidenceBundles, policy rules, release decisions, pipeline code, public API material, public map material, public tiles, or published artifacts."
  - "The tested invariant is that Hydrology source checks preserve admission and authority-control boundaries: source identity, role, rights, cadence, sensitivity, permitted claims, not-authoritative-for claims, activation state, freshness state, evidence relationship, policy posture, release relationship, correction, and rollback remain visible before a source shapes public claims."
  - "Default posture is deterministic and no-network. Live source checks, upstream fetches, real source exports, lifecycle data, public tiles, and restricted records do not belong in this lane."
  - "Rollback target for this replacement is previous blank blob SHA 8b137891791fe96927ad78e64b0aad7bded08bdc."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Hydrology source tests

> Deterministic, no-network test documentation for proving that Hydrology source descriptors, source-role posture, rights/cadence metadata, permitted claims, activation state, evidence relationships, policy gates, correction, and rollback remain enforceable before a source shapes public claims.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: tests" src="https://img.shields.io/badge/root-tests%2F-blue">
  <img alt="Domain: hydrology" src="https://img.shields.io/badge/domain-hydrology-2aa1c6">
  <img alt="Lane: sources" src="https://img.shields.io/badge/lane-sources-blue">
  <img alt="Network: disabled by default" src="https://img.shields.io/badge/network-disabled__by__default-critical">
  <img alt="Boundary: admission not bibliography" src="https://img.shields.io/badge/boundary-admission__not__bibliography-success">
</p>

**Path:** `tests/domains/hydrology/sources/README.md`  
**Status:** draft / placeholder-expanded / PROPOSED until executable tests are verified  
**Owning root:** `tests/`  
**Domain segment:** `hydrology`  
**Test lane:** `sources`  
**Default execution posture:** deterministic, synthetic, no-network, public-safe fixtures only  
**Truth posture:** CONFIRMED target was a blank placeholder before this expansion · CONFIRMED `tests/` is the canonical root for enforceability proof · CONFIRMED Hydrology source registry doctrine says the registry is admission and authority control, not a bibliography · CONFIRMED unknown rights, unknown source role, access conditions, cadence, or release class fail closed · CONFIRMED source role is fixed at admission and never upgraded by promotion · NEEDS VERIFICATION for executable source tests, fixture payload inventory, source-descriptor schema enforcement, registry activation, connector isolation, policy runtime, release integration, CI coverage, and pass rates.

---

## Purpose

`tests/domains/hydrology/sources/` is the intended home for Hydrology source-admission and source-role tests.

This lane should prove that a Hydrology source can be used only through bounded local source metadata that records identity, role, rights posture, access method, cadence, steward, sensitivity, freshness expectations, attribution requirements, activation state, and public-release class where material.

A passing test here should **not** mean that a live source is admitted, an upstream endpoint is current, a connector is safe, source rights are resolved, or a release is approved. It should mean only that source guardrails behaved as expected against bounded fixtures and local files.

---

## Placement basis

`tests/` is the canonical root for enforceability proof. Hydrology is a domain segment inside that root. `sources/` is a test lane, not the source registry authority, source catalog, connector implementation, schema authority, lifecycle store, proof store, policy home, release home, public API surface, or public map surface.

| Responsibility | Correct home | This lane's relationship |
|---|---|---|
| Hydrology source tests | `tests/domains/hydrology/sources/` | This directory. |
| Human-facing source registry doctrine | `docs/domains/hydrology/SOURCE_REGISTRY.md` | Doctrine under test; not redefined here. |
| Source-role matrix | `docs/domains/hydrology/SOURCE_ROLE_MATRIX.md` | Role/claim guardrails under test. |
| SourceDescriptor data | `data/registry/sources/hydrology/` | Expected registry data home; tests do not replace it. |
| Source descriptor schema | `schemas/contracts/v1/source/source-descriptor.json` | Shape source where accepted. |
| Source connectors | `connectors/` source-specific homes | Not executed by default; integration only. |
| Synthetic fixtures | `fixtures/domains/hydrology/sources/` | Preferred toy descriptors and expected outcomes if populated. |
| Policy homes | `policy/domains/hydrology/`, `policy/sensitivity/hydrology/` | Referenced by tests, not bypassed here. |
| Release decisions | `release/` and `release/manifests/hydrology/` | Publication, correction, and rollback authority; tests cannot replace it. |

---

## Invariant under test

> **Hydrology source admission is authority control.** A source descriptor records how a source may be used; it does not prove what the source says, activate a connector by itself, or approve publication. Unknown role, rights, access, cadence, sensitivity, or release class must fail closed.

Core checks:

| Check | Required behavior | Failure outcome |
|---|---|---|
| Source identity | Source ID, family, steward, version/vintage/cadence posture, and authority class are explicit where material. | validation failure / `ABSTAIN`. |
| Role fixed at admission | Observed, regulatory, modeled, aggregate, administrative, candidate, and synthetic roles are explicit and not silently upgraded. | validation failure / `DENY`. |
| Permitted claims | Descriptor or fixture names what a source can and cannot prove. | validation failure / `ABSTAIN`. |
| Rights posture | Unknown or changed rights fail closed. | `DENY` / `HOLD` / `ABSTAIN`. |
| Cadence/freshness | Source cadence, source-head, or stale-state expectation remains visible where material. | `ABSTAIN` / validation failure. |
| Activation boundary | Connectors/watchers do not run unless an activation decision exists in the governed flow. | validation failure. |
| Descriptor is not evidence | SourceDescriptor existence never substitutes for EvidenceBundle closure. | `ABSTAIN`. |
| Release boundary | Source tests do not approve release or public source use. | promotion-blocking failure. |

---

## Expected scope

Tests in this lane may validate:

- local SourceDescriptor-like fixture shape and required governance fields;
- missing source role, rights, cadence, steward, attribution, release class, or activation state;
- Hydrology source-family role expectations for WBD/HUC, NHDPlus/3DHP, NWIS, NFHL/MSC, 3DEP, water-quality, groundwater, drought, irrigation, and historical observed-flood evidence;
- NFHL/regulatory context blocked from observed-flood claims;
- observed gauge readings blocked from regulatory flood-zone claims;
- candidate or synthetic material blocked from public truth claims;
- no connector execution or live source fetch in the default suite;
- evidence, policy, release, correction, and rollback handoff expectations before public use.

Live source checks, upstream endpoint calls, real source exports, production credentials, public tile generation, and real hydrology payloads are out of scope for the default suite.

---

## Fixture posture

Use synthetic, public-safe fixtures only.

Fixture requirements:

- deterministic and no-network;
- compact enough for review in a PR;
- explicit expected outcome;
- explicit source family, source role, rights posture, cadence posture, permitted claims, activation state, evidence posture, policy state, release relationship, correction, and rollback posture where material;
- no real source exports, lifecycle data, public tiles, credentials, restricted records, or published artifacts.

---

## Finite outcomes

| Condition | Expected outcome |
|---|---|
| Valid synthetic source descriptor has role, rights, cadence, steward, permitted claims, activation, evidence, policy, release, correction, and rollback context | accepted source-test support only. |
| Missing source role | `ABSTAIN` / validation failure. |
| Unknown or changed rights | `DENY` / `HOLD` / `ABSTAIN`. |
| Missing cadence or stale-state posture for time-sensitive source | `ABSTAIN` / validation failure. |
| NFHL regulatory context asserted as observed flood evidence | `DENY`. |
| SourceDescriptor treated as EvidenceBundle or release authority | validation failure / `ABSTAIN`. |
| Connector or live source fetch runs in default lane | validation failure / `ERROR`. |
| Release relationship or rollback target is missing for public carrier candidate | promotion-blocking failure. |

---

## Suggested layout

```text
tests/domains/hydrology/sources/
├── README.md
├── test_source_descriptor_shape.py
├── test_source_role_required.py
├── test_permitted_claims_required.py
├── test_rights_and_cadence_fail_closed.py
├── test_activation_before_connector.py
├── test_nfhl_not_observed_flood.py
├── test_descriptor_not_evidence_or_release.py
└── test_release_correction_rollback_handoff.py
```

---

## Run posture

```bash
pytest tests/domains/hydrology/sources
```

Status of the command above: **PROPOSED / NEEDS VERIFICATION**. It assumes `pytest` is the accepted test runner and that executable test modules exist. This README does not claim the command currently passes.

---

## Evidence ledger

| Evidence | Status | Supports | Limits |
|---|---|---|---|
| Previous target file | CONFIRMED | `tests/domains/hydrology/sources/README.md` existed as a blank placeholder before this replacement. | Did not define the lane. |
| `tests/README.md` | CONFIRMED | `tests/` is enforceability proof and failure should block promotion where trust-spine checks fail. | Does not prove this lane's modules or pass rate. |
| `tests/domains/hydrology/README.md` | CONFIRMED | Hydrology test parent currently exists as a greenfield stub. | Parent lane still needs expansion. |
| `docs/domains/hydrology/SOURCE_REGISTRY.md` | CONFIRMED doctrine / PROPOSED implementation | Defines source registry as admission and authority control; records source identity, role, rights, cadence, sensitivity, freshness expectations, activation, and fail-closed posture. | Descriptor counts, exact field names, endpoints, validators, and pass rates remain NEEDS VERIFICATION. |
| `docs/domains/hydrology/SOURCE_ROLE_MATRIX.md` | CONFIRMED doctrine / PROPOSED implementation | Defines source role as first-class, fixed at admission, preserved through promotion, and role-collapse fail-closed behavior. | Machine policy enforcement remains NEEDS VERIFICATION. |
| Repo search | CONFIRMED | Found Hydrology source registry and source-role test placement references. | Search is not proof of executable tests or full fixture coverage. |

---

## Validation checklist

- [ ] Executable test modules exist under this lane.
- [ ] Test runner and import paths match the repo's accepted convention.
- [ ] Synthetic source fixtures exist for valid source, missing role, missing rights, missing cadence, missing permitted claims, missing activation, source-role collapse, connector-attempt, and missing release/rollback cases.
- [ ] SourceDescriptor schema and field expectations are accepted or safely stubbed.
- [ ] SourceActivationDecision behavior is available to tests or safely stubbed.
- [ ] EvidenceRef / EvidenceBundle behavior is available to tests or safely stubbed.
- [ ] PolicyDecision, ReleaseManifest, CorrectionNotice, RedactionReceipt, and RollbackCard expectations are defined before enforcing them.
- [ ] CI runs the no-network Hydrology sources suite or marks it as an expected gap.
- [ ] Failures block public carrier promotion or release candidate approval where material.

---

## Rollback

Rollback is required if this lane becomes a live source-fetcher, connector implementation, lifecycle data store, source registry authority, contract root, schema authority, policy authority, proof store, release-decision root, public map/API/tile surface, AI surface, renderer implementation, pipeline implementation, or publication shortcut.

Rollback target for this replacement: previous blank blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
