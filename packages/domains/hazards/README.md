<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS-VERIFICATION/packages-domains-hazards-readme
title: Hazards Domain Package README
type: standard
version: v1
status: draft
owners: OWNER_TBD
created: 2026-06-14
updated: 2026-06-14
policy_label: public
related: [docs/domains/hazards/README.md, docs/domains/hazards/ARCHITECTURE.md, docs/domains/hazards/SOURCE_ROLES.md, docs/domains/hazards/TIME_SEMANTICS.md, docs/domains/hazards/PROMOTION.md, docs/domains/hazards/UI_AND_EVIDENCE_DRAWER.md, schemas/contracts/v1/domains/hazards/, contracts/domains/hazards/, policy/hazards/, data/registry/hazards/, data/receipts/hazards/, data/proofs/hazards/, release/candidates/hazards/, tests/domains/hazards/, fixtures/domains/hazards/]
tags: [kfm, hazards, packages, source-roles, evidence, public-safety, finite-outcomes, map-layers]
notes: ["README-like package entrypoint for shared Hazards implementation helpers.", "Target path is user-requested and Directory Rules-compatible as a package/domain segment, but actual repo package layout remains NEEDS VERIFICATION until mounted repo evidence confirms package metadata, imports, tests, CI, and sibling conventions.", "Hazards helpers must never turn KFM into an emergency alerting system; operational warnings are contextual-only and must point users to official life-safety sources.", "This package may contain shared implementation helpers only; it must not become a schema, contract, policy, source-registry, lifecycle-data, release, receipt, proof, or public-publication authority."]
[/KFM_META_BLOCK_V2] -->

# Hazards Domain Package

Shared implementation package for KFM hazards helpers that preserve source roles, evidence closure, temporal semantics, public-safety boundaries, public-safe geometry, finite outcomes, and release-state separation.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Implementation: proposed" src="https://img.shields.io/badge/implementation-PROPOSED-orange">
  <img alt="Owner: OWNER_TBD" src="https://img.shields.io/badge/owner-OWNER__TBD-lightgrey">
  <img alt="Root: packages" src="https://img.shields.io/badge/root-packages-blue">
  <img alt="Domain: hazards" src="https://img.shields.io/badge/domain-hazards-red">
  <img alt="Emergency posture: contextual only" src="https://img.shields.io/badge/emergency-contextual__only-critical">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-blueviolet">
</p>

> [!IMPORTANT]
> **Status:** PROPOSED package README  
> **Path:** `packages/domains/hazards/README.md`  
> **Owning responsibility root:** `packages/`  
> **Domain lane:** `hazards`  
> **Repo implementation depth:** NEEDS VERIFICATION — package metadata, package manager, imports, tests, schemas, policies, registries, CI workflows, API routes, UI bindings, emitted receipts, proof objects, release manifests, and runtime behavior were not inspected in this file-generation pass.

## Quick links

- [Scope](#scope)
- [Repo fit](#repo-fit)
- [Accepted inputs](#accepted-inputs)
- [Exclusions](#exclusions)
- [Package responsibilities](#package-responsibilities)
- [Source-role anti-collapse rules](#source-role-anti-collapse-rules)
- [Public-safety boundary](#public-safety-boundary)
- [Trust-boundary flow](#trust-boundary-flow)
- [Proposed directory map](#proposed-directory-map)
- [Finite outcomes](#finite-outcomes)
- [Validation and quality gates](#validation-and-quality-gates)
- [Development rules](#development-rules)
- [Definition of done](#definition-of-done)
- [Verification checklist](#verification-checklist)
- [Rollback](#rollback)

---

## Scope

`packages/domains/hazards/` is the shared implementation package lane for hazard-domain helpers.

This package may contain reusable code that helps KFM normalize, classify, validate, compare, transform, and package hazards-related candidate records for governed downstream systems. It does **not** own truth, source authority, policy, lifecycle state, public publication, release approval, steward review, emergency guidance, or AI answers.

The package may support these hazards knowledge families:

- historical hazard event records;
- operational warning, advisory, and watch context, with strict contextual-only treatment;
- administrative declarations and incident-period records;
- regulatory hazard areas and effective-date/versioned context;
- scientific observations such as earthquakes, stream gauges, weather observations, or field observations;
- remote-sensing detections such as smoke, fire, flood extent, storm damage, heat, drought, or other detected signals;
- modeled derivatives, risk surfaces, exposure analyses, vulnerability overlays, and resilience-analysis candidates;
- local context where rights, source role, and steward review allow use;
- temporal semantics for event, issue, expiry, declaration, effective, retrieval, product, model-run, review, release, correction, and supersession time;
- public-safe generalized hazard layer preparation;
- EvidenceBundle-aware DTO preparation;
- MapLibre, Evidence Drawer, Focus Mode, and governed API support payloads after policy and release controls.

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

This package may help create WORK, QUARANTINE, PROCESSED, catalog-ready, proof-ready, receipt-ready, or layer-manifest-ready payloads. It must not publish, promote, bypass review, issue emergency instructions, or turn generated summaries, model outputs, map tiles, graph edges, operational feeds, public layer labels, or source convenience fields into sovereign truth.

---

## Repo fit

```text
packages/domains/hazards/
```

This path is appropriate for shared implementation helpers because `packages/` owns reusable library code and `hazards` is a domain segment inside that responsibility root.

| Relationship | Expected home | Boundary rule |
| --- | --- | --- |
| Shared package helpers | `packages/domains/hazards/` | Owns reusable implementation code only. |
| Domain documentation | `docs/domains/hazards/` | Explains domain purpose, stewardship, file map, source roles, temporal semantics, promotion, and lane boundaries. |
| Architecture docs | `docs/architecture/hazards/` or repo-confirmed docs home | Explains trust path, control plane, object model, lifecycle, and integration design. |
| ADRs | `docs/adr/ADR-hazards-*.md` | Records schema-home, source-role, public-safety, public-safe-geometry, and doc-lineage decisions. |
| Semantic contracts | `contracts/domains/hazards/` or repo-confirmed contract home | Defines object meaning; package code references, not redefines. |
| Machine schemas | `schemas/contracts/v1/domains/hazards/` or repo-confirmed schema home | Defines machine-checkable shape; package code validates against it. |
| Source registries | `data/registry/hazards/` or repo-confirmed source-registry home | Owns source identity, rights, role, cadence, caveats, sensitivity, and activation state. |
| Policy | `policy/hazards/` or repo-confirmed policy home | Decides allow / deny / restrict / abstain, emergency-boundary, freshness, and public-safe geometry rules. |
| Lifecycle data | `data/raw/hazards/`, `data/work/hazards/`, `data/quarantine/hazards/`, `data/processed/hazards/`, `data/catalog/.../hazards/`, `data/published/layers/hazards/` | Stores evidence-bearing and released data by lifecycle phase. |
| Receipts and proofs | `data/receipts/hazards/`, `data/proofs/hazards/`, or repo-confirmed trust-object homes | Stores process memory and release-significant proof artifacts. |
| Release decisions and rollback | `release/` | Owns release manifests, promotion decisions, correction notices, supersession records, and rollback targets. |
| Pipelines and source activation | `pipelines/domains/hazards/`, `pipeline_specs/hazards/`, `connectors/` | Owns executable flows, declarative pipeline config, and source-specific fetch/admission code. |
| Tests and fixtures | `tests/domains/hazards/`, `fixtures/domains/hazards/`, or repo-confirmed equivalents | Proves package behavior with deterministic no-network fixtures. |

> [!WARNING]
> This package must not become a shortcut around `schemas/`, `contracts/`, `policy/`, `data/registry/`, lifecycle directories, `data/receipts/`, `data/proofs/`, or `release/`. If a helper starts owning one of those responsibilities, split the file into the correct root and record the move.

---

## Accepted inputs

Package functions should accept explicit, inspectable values from governed callers. Inputs should carry source, evidence, temporal, spatial, rights, sensitivity, freshness, public-safety, and run context instead of relying on ambient global state.

| Input family | Accepted examples | Required handling |
| --- | --- | --- |
| Source descriptors | `source_id`, source role, rights profile, caveat text, authority limit, activation state, cadence, steward, citation template | Treat source role as a hard boundary; do not infer stronger authority from a convenient field. |
| Hazard candidate records | Historical events, warnings/advisories/watches, disaster declarations, regulatory areas, observations, detections, modeled derivatives, resilience-analysis rows | Preserve source-native fields and normalized fields separately. |
| Evidence context | EvidenceRef, EvidenceBundle reference, citation requirement, input digest, source descriptor ref | Preserve evidence closure requirements and return bounded outcomes when evidence is missing. |
| Spatial context | Internal geometry reference, CRS, source scale, resolution, support, uncertainty, generalized geometry, redaction class | Keep exact/internal and public-safe geometry separate. |
| Time context | observed time, event begin/end, issue time, expiry time, declaration time, effective date, retrieval time, product time, model-run time, review time, release time | Do not collapse these into one timestamp. |
| Freshness context | source cadence, retrieved_at, stale-after policy, expiry requirement, product latency, review window | Surface stale, expired, or ambiguous data; never silently refresh or silently reuse. |
| Public-safety context | contextual-only flag, not-for-life-safety flag, official-source handoff link, no-emergency-instruction reason | Required for operational warning/advisory/watch family outputs. |
| Policy context | sensitivity tier, public-safe geometry profile, source-role permissions, review burden, deny/abstain reason codes | Treat as policy inputs, not publication approval. |
| Run context | run ID, package version, actor/service ID, spec hash, input/output digests, timestamp | Emit receipt-ready metadata for the owning pipeline to persist. |

Missing source role, evidence context, time basis, freshness context, public-safety context, public-safe geometry context, or rights/sensitivity context should produce a finite failure outcome rather than a silent best-effort public output.

---

## Exclusions

| Do not put here | Correct home or owner | Why |
| --- | --- | --- |
| Live source fetchers, scrapers, credentials, or source-specific admission code | `connectors/`, `pipelines/domains/hazards/`, `pipeline_specs/hazards/`, `configs/`, secret-management infrastructure | Source activation is governed and source-specific, not package-local convenience code. |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, PUBLISHED data | `data/<phase>/hazards/` | Lifecycle state must remain auditable outside package source. |
| Source descriptors, source-role registries, rights/cadence/sensitivity registers | `data/registry/hazards/` or repo-confirmed source-registry home | Source authority and rights are governance data. |
| Semantic contracts | `contracts/domains/hazards/` or repo-confirmed contract home | Contracts define meaning. |
| JSON Schemas | `schemas/contracts/v1/domains/hazards/` or repo-confirmed schema home | Schemas define machine shape. |
| Policy rules, emergency-boundary rules, freshness gates, public-safe geometry law | `policy/hazards/` | Policy owns allow/deny/restrict/abstain decisions. |
| Proofs, receipts, EvidenceBundle stores, catalog matrices | `data/proofs/`, `data/receipts/`, `data/catalog/` | Trust objects must remain independently addressable. |
| Release manifests, promotion decisions, correction notices, rollback cards | `release/` | Publication is a governed state transition, not a package side effect. |
| Public API routes, UI components, MapLibre styles, Focus Mode answer surfaces | `apps/`, `ui/`, `web/`, or repo-confirmed equivalents | Package code may prepare DTOs but does not own public interfaces. |
| Emergency instructions, evacuation advice, medical/legal directives, or live-alert authority | Official alerting and emergency-management sources, not KFM package code | KFM hazards is evidence/context, not an emergency alert system. |
| AI prompts or generated hazard explanations as truth | Governed AI runtime and AIReceipt surfaces | Generated language is interpretive and evidence-subordinate. |

---

## Package responsibilities

The package should be conservative, deterministic, evidence-aware, and easy to test.

| Responsibility | Expected behavior |
| --- | --- |
| Normalize source payloads | Convert source-native hazard fields into typed candidate objects without deleting raw values, caveats, or source-role context. |
| Preserve source roles | Keep historical events, operational warnings, administrative declarations, regulatory areas, observations, detections, modeled derivatives, resilience analyses, and local context distinct. |
| Maintain deterministic identity | Build or support stable IDs from source ID, object family, hazard type, spatial/temporal scope, version, and digest-bearing inputs. |
| Represent uncertainty | Preserve geometry uncertainty, source scale, observation uncertainty, model uncertainty, source latency, freshness status, and classification caveats. |
| Keep temporal semantics separate | Retain event, issue, expiry, effective, declaration, retrieval, product, model-run, review, release, correction, and supersession time where material. |
| Enforce public-safety labels | Require contextual-only and not-for-life-safety posture for operational warning/advisory/watch outputs. |
| Prepare public-safe geometry | Support generalized/redacted/withheld output candidates only when policy context and reason codes are present. |
| Prepare Evidence Drawer payload fragments | Include what-this-is, what-this-is-not, source role, time basis, spatial basis, freshness, rights, review state, evidence links, and correction/supersession links. |
| Prepare catalog-ready payloads | Build STAC/DCAT/PROV-ready or layer-manifest-ready fragments for owning catalog/release systems. |
| Prepare receipt/proof-ready metadata | Return input digests, output digests, spec hash, run ID, reason codes, source refs, and evidence refs for the owning pipeline to persist. |
| Fail closed | Return `ABSTAIN`, `DENY`, or `ERROR` when evidence, source role, policy, rights, sensitivity, freshness, or schema support is insufficient. |

---

## Source-role anti-collapse rules

The most important hazards package rule is to keep source character visible.

| Source character | Can support | Must not be treated as |
| --- | --- | --- |
| `historical_event_record` | Published historical event evidence within stated source limits | Current warning, official instruction, or live-safety status. |
| `operational_warning` | Contextual warning record with issue, expiry, retrieval, and freshness labels | KFM-owned alert, life-safety instruction, or historical event record. |
| `operational_advisory` | Contextual advisory record with valid window and official-source attribution | Emergency instruction or release approval. |
| `operational_watch` | Contextual watch record with valid window and official-source attribution | Event confirmation or emergency instruction. |
| `administrative_declaration` | Administrative/legal declaration context and incident-period metadata | Physical observation, hazard boundary, or damage measurement. |
| `regulatory_context` | Effective-date/versioned regulatory area context | Observed event or current impact. |
| `scientific_observation` | Measurement or observation under method/uncertainty caveats | Regulatory determination or official warning. |
| `remote_sensing_detection` | Product-time detection with processing limitations | Field-confirmed event or official warning. |
| `modeled_derivative` | Derived analysis/model output with inputs, method, model run, and limitations | Observation, regulation, or official forecast. |
| `resilience_analysis` | Derived planning/context candidate with method and review state | Official emergency guidance or source truth. |
| `local_context` | Locally sourced context when rights and stewardship allow | Statewide authority or public-safe release by default. |
| `unknown_unclassified` | Quarantine target only | Public output or evidence-bearing claim. |

> [!CAUTION]
> Operational hazard feeds are high-risk. Package helpers may classify, normalize, or flag them for review; they must not promote them to public fact, emergency guidance, or official alerting authority.

---

## Public-safety boundary

KFM hazards may help users inspect evidence-backed hazard context, but it must not become an emergency alert system.

| User-facing situation | Package posture | Required result |
| --- | --- | --- |
| User asks what a released historical hazard record says | Evidence-bounded context | Return or prepare payload only if EvidenceRef resolves and release state allows it. |
| User asks whether they are safe now | Emergency boundary | `ABSTAIN` or `DENY`; point UI/API layer to official emergency sources. |
| User asks for evacuation, shelter, medical, legal, or safety instructions | Emergency boundary | `DENY`; no generated instructions from this package. |
| Operational warning is present but expired or stale | Freshness boundary | Mark expired/stale; do not summarize as current. |
| Operational warning lacks expiry, issue time, retrieval time, or source | Evidence/time boundary | Quarantine or finite negative outcome. |
| Regulatory area is mislabeled as observed event | Source-role boundary | `DENY` or quarantine with `regulatory_as_observed` reason. |
| Disaster declaration is mislabeled as physical observation | Source-role boundary | `DENY` or quarantine with `declaration_as_observation` reason. |
| Public layer requests restricted exact geometry | Sensitivity boundary | `DENY` or public-safe generalized geometry with transform receipt. |

---

## Trust-boundary flow

```mermaid
flowchart TD
  A[Source-specific connector or admitted fixture] --> B[Hazards package helpers]
  B --> C{Schema-valid candidate?}
  C -- No --> Q[QUARANTINE candidate<br/>schema_or_mapping_error]
  C -- Yes --> D{Source role supports claim?}
  D -- No --> Q2[ABSTAIN / QUARANTINE<br/>unsupported_source_role]
  D -- Yes --> E{Time and freshness basis present?}
  E -- No --> Q3[ABSTAIN / QUARANTINE<br/>missing_time_or_freshness]
  E -- Yes --> F{Operational context?}
  F -- Yes --> G{contextual_only and not_for_life_safety?}
  G -- No --> Q4[DENY<br/>emergency_boundary_violation]
  G -- Yes --> H[Preserve official-source handoff<br/>no emergency instructions]
  F -- No --> I[Continue evidence checks]
  H --> J{Rights and sensitivity context present?}
  I --> J
  J -- No --> Q5[ABSTAIN<br/>missing_rights_or_sensitivity]
  J -- Yes --> K{Public-safe geometry required?}
  K -- Yes --> L[Generalize / redact / withhold<br/>with reaso
