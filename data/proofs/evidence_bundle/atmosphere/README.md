<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/data-proofs-evidence-bundle-atmosphere-readme
title: data/proofs/evidence_bundle/atmosphere/README.md — Atmosphere EvidenceBundle Proofs README
version: v0.1
type: readme; proof-lane-guide; evidence-bundle-lane; atmosphere-domain-proof-index; evidence-ref-resolution-lane; governed-answer-support-lane
status: draft; PROPOSED; data-root; proofs-root; evidence-bundle; atmosphere; evidence-bundle-index; evidence-ref; claim-support; digest-closure; cite-or-abstain; source-role-aware; caveat-aware; release-gated; evidence-first
authors: ChatGPT-5.5 Thinking; reviewed_by: OWNER_TBD
owners: OWNER_TBD — Atmosphere steward · Air-quality steward · Evidence steward · EvidenceBundle steward · Proof steward · Policy steward · Release steward · UI/Evidence Drawer steward · Docs steward
created: NEEDS VERIFICATION — blank placeholder existed before v0.1 expansion
updated: 2026-06-25
policy_label: public-doc; data; proofs; evidence-bundle; atmosphere; evidence; lifecycle; governed; release-gated
tags: [kfm, data, proofs, evidence-bundle, atmosphere, air, air-quality, EvidenceBundle, EvidenceRef, EvidenceDrawerPayload, DecisionEnvelope, cite-or-abstain, claim-resolution, citation-closure, proof, claim-support, digest-closure, SourceDescriptor, CatalogMatrix, ReleaseManifest, ReviewRecord, CorrectionNotice, RollbackCard, PolicyDecision, ValidationReport, RunReceipt, PM25Observation, AirObservation, AirStation, OzoneObservation, AODRaster, SmokeContext, ForecastContext, AdvisoryContext, AQI, observed-sensor, public-aqi-report, low-cost-sensor, AOD, smoke, model-field, advisory-boundary, RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, PUBLISHED]
related:
  - ../../README.md
  - ../../../README.md
  - ../README.md
  - ../../atmosphere/README.md
  - ../../atmosphere/pm25_2026/README.md
  - ../../citation_validation/README.md
  - ../../citation_validation/atmosphere/README.md
  - ../../../catalog/domain/atmosphere/README.md
  - ../../../catalog/domain/atmosphere/pm25_2026/README.md
  - ../../../processed/atmosphere/air_observations/README.md
  - ../../../processed/atmosphere/air_stations/README.md
  - ../../../processed/atmosphere/
  - ../../../receipts/
  - ../../../registry/sources/atmosphere/
  - ../../../published/
  - ../../../triplets/
  - ../../../../docs/architecture/ui/EVIDENCE_DRAWER.md
  - ../../../../docs/architecture/evidence-drawer.md
  - ../../../../docs/domains/atmosphere/DATA_LIFECYCLE.md
  - ../../../../docs/domains/atmosphere/CANONICAL_PATHS.md
  - ../../../../docs/domains/atmosphere/OBJECT_FAMILY_MAP.md
  - ../../../../docs/domains/atmosphere/POLICY.md
  - ../../../../docs/domains/atmosphere/PUBLICATION_POSTURE.md
  - ../../../../docs/domains/atmosphere/SENSITIVITY.md
  - ../../../../docs/domains/atmosphere/SOURCE_FAMILIES.md
  - ../../../../docs/domains/atmosphere/SOURCES.md
  - ../../../../docs/domains/atmosphere/API_CONTRACTS.md
  - ../../../../contracts/domains/atmosphere/PM25Observation.md
  - ../../../../contracts/domains/atmosphere/AirObservation.md
  - ../../../../contracts/domains/atmosphere/AirStation.md
  - ../../../../contracts/domains/atmosphere/OzoneObservation.md
  - ../../../../contracts/domains/atmosphere/AODRaster.md
  - ../../../../contracts/domains/atmosphere/SmokeContext.md
  - ../../../../contracts/domains/atmosphere/ForecastContext.md
  - ../../../../contracts/domains/atmosphere/AdvisoryContext.md
  - ../../../../schemas/contracts/v1/domains/atmosphere/
  - ../../../../schemas/contracts/v1/evidence/evidence_bundle.schema.json
  - ../../../../schemas/contracts/v1/ui/evidence_drawer_payload.schema.json
  - ../../../../policy/domains/atmosphere/
  - ../../../../release/candidates/atmosphere/
  - ../../../../release/
  - ../../../../tools/validators/
notes:
  - "This file replaces a blank placeholder at `data/proofs/evidence_bundle/atmosphere/README.md`."
  - "This is an Atmosphere EvidenceBundle proof lane guide under `data/proofs/`. It supports Atmosphere EvidenceBundle / EvidenceRef closure, claim support, digest closure, citation readiness, and governed answer readiness. It is not RAW source storage, WORK scratch, QUARANTINE holding, PROCESSED data, CATALOG, TRIPLET, PUBLISHED output, receipt storage, source registry, policy authority, release authority, schema home, validator home, public API/UI output, public map/tile output, AQI advisory service, medical advice, emergency alert, regulatory-exceedance authority, exposure/impact claim surface, or life-safety guidance."
  - "EvidenceBundle artifacts in this lane may reference SourceDescriptor, processed artifacts, catalog rows, triplets, receipts, policy decisions, review records, release manifests, correction notices, and rollback cards; this lane does not own those records."
  - "Atmosphere EvidenceBundle support must preserve source-role and caveat boundaries: observed sensor readings, public AQI/report posture, low-cost sensor records, regulatory/archive posture, AOD/smoke proxies, model fields, forecasts, and advisory context are not interchangeable evidence."
  - "The parent `data/proofs/evidence_bundle/README.md` is currently a greenfield stub, so global EvidenceBundle family behavior remains NEEDS VERIFICATION."
  - "This README is a proof-lane guide only. Contracts define semantic object meaning; schemas define machine shape; policy decides admissibility; release records decide publication."
  - "Rollback target for this expansion is previous blank placeholder blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# data/proofs/evidence_bundle/atmosphere

> Atmosphere EvidenceBundle proof lane for resolvable claim-support bundles, EvidenceRef closure, digest closure, source-role/caveat preservation, release linkage, correction lineage, rollback linkage, and governed answer support for Atmosphere / Air claims.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: data/proofs/evidence_bundle/atmosphere" src="https://img.shields.io/badge/root-data%2Fproofs%2Fevidence__bundle%2Fatmosphere-blue">
  <img alt="Domain: atmosphere" src="https://img.shields.io/badge/domain-atmosphere%2Fair-1f8fff">
  <img alt="Family: EvidenceBundle" src="https://img.shields.io/badge/family-EvidenceBundle-purple">
  <img alt="Posture: evidence first" src="https://img.shields.io/badge/posture-evidence--first-green">
  <img alt="Exposure: not public" src="https://img.shields.io/badge/exposure-not__public-critical">
</p>

**Status:** draft / PROPOSED  
**Owners:** OWNER_TBD — Atmosphere steward · Air-quality steward · Evidence steward · EvidenceBundle steward · Proof steward · Policy steward · Release steward · UI/Evidence Drawer steward · Docs steward  
**Path:** `data/proofs/evidence_bundle/atmosphere/README.md`  
**Owning root:** `data/proofs/`  
**Proof family segment:** `evidence_bundle`  
**Domain segment:** `atmosphere`  
**Lifecycle role:** EvidenceBundle proof support referenced by processed Atmosphere artifacts, catalog records, triplets, release candidates, citation-validation lanes, corrections, rollbacks, and governed answer surfaces; not a lifecycle phase substitute  
**Exposure posture:** not public by default; public use requires governed projection, policy/review state, release state, correction path, and rollback target.  
**Truth posture:** CONFIRMED target was a blank placeholder · CONFIRMED parent `data/proofs/evidence_bundle/README.md` is still a greenfield stub · CONFIRMED Atmosphere proof parent defines EvidenceBundle/EvidenceRef closure and proof support while excluding public outputs, receipts, source registry, policy, release authority, schemas, and validators · CONFIRMED PM2.5 child proof lane already uses EvidenceBundle/EvidenceRef closure · CONFIRMED Evidence Drawer doctrine requires EvidenceBundle resolution through governed APIs, not direct browser access to canonical stores · PROPOSED EvidenceBundle lane details · NEEDS VERIFICATION for actual EvidenceBundle schema, concrete bundle inventory, validators, fixtures, access controls, release linkage, and governed route behavior.

**Quick jumps:** [Purpose](#purpose) · [Lifecycle relationship](#lifecycle-relationship) · [Repo fit](#repo-fit) · [Accepted contents](#accepted-contents) · [Exclusions](#exclusions) · [EvidenceBundle requirements](#evidencebundle-requirements) · [Atmosphere EvidenceBundle guardrails](#atmosphere-evidencebundle-guardrails) · [Directory map](#directory-map) · [Evidence ledger](#evidence-ledger) · [Validation checklist](#validation-checklist) · [Rollback](#rollback)

---

## Purpose

`data/proofs/evidence_bundle/atmosphere/` is a specialized proof lane for Atmosphere-domain EvidenceBundle support. It should hold or index bundle-like proof artifacts that make Atmosphere claims resolvable, inspectable, and cite-or-abstain safe.

This lane may contain or reference proof support for:

- EvidenceBundle closure for Atmosphere catalog/triplet candidates;
- EvidenceRef resolution targets used by release-linked or governed Atmosphere payloads;
- claim-support bundles for AirObservation, AirStation, PM25Observation, OzoneObservation, AODRaster, SmokeContext, ForecastContext, and AdvisoryContext claims;
- digest closure tying source captures, processed Atmosphere artifacts, catalog rows, triplets, receipts, release candidates, correction records, rollback targets, and governed answer examples to evidence;
- bundle indexes that preserve source role, units, averaging windows, observed time, retrieval time, correction time, freshness state, QA state, station/network context, model/advisory boundary, policy state, release state, and limitation posture;
- negative-state evidence support explaining why a governed Atmosphere answer must `ABSTAIN`, `DENY`, `HOLD`, or `ERROR` instead of answering.

This lane does not create, store, or decide the underlying Atmosphere data, catalog records, triplets, receipts, policy decisions, release decisions, public AQI payloads, public maps, medical advice, emergency alerts, regulatory determinations, or life-safety instructions. It supports evidence resolution; it does not publish claims.

## Lifecycle relationship

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
                           \-> data/proofs/evidence_bundle/atmosphere supports EvidenceBundle closure
```

```mermaid
flowchart LR
  RAW[data/raw/atmosphere] --> WORK[data/work/atmosphere]
  WORK --> QUAR[data/quarantine/atmosphere]
  WORK --> PROC[data/processed/atmosphere]
  QUAR --> PROC
  PROC --> CAT[data/catalog/domain/atmosphere]
  CAT --> PMCAT[data/catalog/domain/atmosphere/pm25_2026]
  CAT --> TRIP[data/triplets/.../atmosphere]
  CAT --> PUB[data/published/.../atmosphere]
  TRIP --> PUB
  PUB --> REL[release]

  PROC -. evidence refs .-> EB[data/proofs/evidence_bundle/atmosphere]
  CAT -. EvidenceBundle closure .-> EB
  PMCAT -. PM2.5 bundle closure .-> EB
  TRIP -. claim support .-> EB
  REL -. release cites .-> EB
  EB -. citation validation .-> CIT[data/proofs/citation_validation/atmosphere]
  EB -. references receipts .-> RECEIPTS[data/receipts]
  EB -. references sources .-> REG[data/registry/sources/atmosphere]
```

EvidenceBundle proof artifacts support catalog, triplet, release, correction, rollback, citation validation, Evidence Drawer, and governed answers. They do not publish anything by themselves.

## Repo fit

| Responsibility | Correct home | Rule |
|---|---|---|
| Raw sensor feeds, regulatory/source downloads, station payloads, source QA payloads, logs, or source-native records | `data/raw/atmosphere/` | Not this lane. |
| In-process parsing, correction, QA, calibration, joins, model comparisons, redaction trials, notebooks, or scratch outputs | `data/work/atmosphere/` | Not this lane. |
| Rights-unclear, source-role-unclear, stale, malformed, unsupported, disputed, low-cost-caveat-missing, station-sensitive, or release-unclear Atmosphere material | `data/quarantine/atmosphere/` | Not this lane until review/admission allows. |
| Normalized Atmosphere processed artifacts | `data/processed/atmosphere/` | Not this lane. |
| Atmosphere domain catalog records | `data/catalog/domain/atmosphere/` | Catalog records, not EvidenceBundle storage. |
| PM2.5 2026 catalog records | `data/catalog/domain/atmosphere/pm25_2026/` | Dataset catalog records, not EvidenceBundle storage. |
| Triplets/graph records | `data/triplets/.../atmosphere/` | Graph projection, not EvidenceBundle storage. |
| General Atmosphere proof support | `data/proofs/atmosphere/` | Domain proof lane. |
| Atmosphere EvidenceBundle proof support | `data/proofs/evidence_bundle/atmosphere/` | This lane. |
| Atmosphere citation-validation proof support | `data/proofs/citation_validation/atmosphere/` | Validates citations; not the bundle lane. |
| Receipts | `data/receipts/` | Referenced by bundles; not stored here. |
| Source registry records | `data/registry/sources/atmosphere/` | SourceDescriptor/source-admission authority. |
| Published public-safe outputs | `data/published/.../atmosphere/` | Downstream after release only. |
| Release candidates and release manifests | `release/candidates/atmosphere/`, `release/` | Publication authority, not EvidenceBundle storage. |
| Atmosphere contracts | `contracts/domains/atmosphere/` | Semantic meaning; not proof artifacts. |
| Atmosphere schemas | `schemas/contracts/v1/domains/atmosphere/` and `schemas/contracts/v1/evidence/` | Machine shape; not proof artifacts. |
| Atmosphere policy | `policy/domains/atmosphere/` | Admissibility authority; not proof artifacts. |
| Validators, tests, fixtures, pipelines, apps, packages | `tools/validators/`, `tests/`, `fixtures/`, `pipelines/`, `apps/`, `packages/` | Separate roots. |

## Accepted contents

Atmosphere EvidenceBundle proof artifacts may include:

- EvidenceBundle records, indexes, or bundle pointers for Atmosphere claims when this lane is accepted as a projection/index home;
- EvidenceRef resolution maps that point to bundle members without duplicating raw source or receipt authority;
- claim-to-bundle maps for catalog records, triplets, Evidence Drawer payloads, release candidates, and governed answer examples;
- digest-closure manifests tying source captures, processed artifacts, catalog rows, triplets, receipts, release records, and proof manifests to evidence;
- bundle member indexes for AirObservation, AirStation, PM25Observation, OzoneObservation, AODRaster, SmokeContext, ForecastContext, and AdvisoryContext claims;
- QA/freshness/correction/caveat evidence summaries that preserve source role, units, averaging window, time semantics, and release posture;
- negative-state support records explaining `ABSTAIN`, `DENY`, `HOLD`, or `ERROR` outcomes for missing, stale, conflicting, restricted, unreleased, caveat-missing, or source-role-unclear evidence;
- lane-local README or index notes that explain EvidenceBundle boundaries without becoming public outputs or authority records.

## Exclusions

Do not store these under `data/proofs/evidence_bundle/atmosphere/`:

- RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data artifacts.
- Canonical EvidenceBundle authority if another ADR-resolved evidence store owns canonical bundles.
- RunReceipt, TransformReceipt, ValidationReport, PolicyDecision, ReviewRecord, ReleaseManifest, RollbackCard, CorrectionNotice, WithdrawalNotice, AIReceipt, or release signatures as primary receipt/release records.
- SourceDescriptor/source registry records.
- Contracts, schemas, policy bundles, validators, tests, fixtures, pipelines, app/UI/API code, packages, notebooks, or executable tooling.
- Public AQI/map/tile/API/UI payloads, Focus Mode answer payloads, direct downloads, model-answer text, release manifests, signatures, changelogs, or published products.
- Health/medical advice, emergency advisories, evacuation guidance, regulatory-exceedance determinations, exposure/impact claims, damages claims, or life-safety instructions.
- Claims that turn AQI/report posture into raw concentration, low-cost sensor records into reference-grade concentration without caveats, AOD/smoke proxies into PM2.5/ozone observations, model fields into observed sensor values, or air-quality values into health/action instructions.

## EvidenceBundle requirements

PROPOSED until concrete EvidenceBundle schemas, validators, fixtures, and route behavior are verified:

| Requirement | Meaning |
|---|---|
| EvidenceRef resolution | Each bundle or bundle index should identify every EvidenceRef it resolves and every claim it supports. |
| Bundle closure | SourceDescriptor, processed artifact, catalog row, triplet, receipt, policy, review, release, correction, and rollback references should resolve or produce a finite negative state. |
| Digest closure | Bundles should include or point to content digests for evidence inputs, processed artifacts, catalog rows, triplets, receipts, and proof manifests. |
| Claim scope | Bundles should record the exact claim being supported, including object family, time, location/generalization, source role, units, averaging window, QA/correction posture, freshness, caveat, and release posture. |
| Source-role preservation | Observed sensor, public AQI/report, low-cost sensor, regulatory/archive, AOD/smoke proxy, model, forecast, and advisory context roles must not be interchangeable. |
| Caveat preservation | Low-cost sensor, model, proxy, stale, corrected, missingness, confidence, station-sensitive, and rights-limited caveats should remain attached to bundle entries. |
| Release posture | Public-facing bundle use should verify release state, policy-safe representation, correction path, rollback target, and current/non-withdrawn posture. |
| Negative outcomes | Missing, stale, conflicting, restricted, unreleased, role-collapsed, caveat-missing, or source-rights-unclear bundle support should produce `ABSTAIN`, `DENY`, `HOLD`, or `ERROR`, not an uncited answer. |
| UI projection boundary | Evidence Drawer and Focus Mode should consume governed projection payloads, not canonical stores or raw proof files directly. |
| No public surface by default | EvidenceBundle proof files are not direct public APIs, tiles, downloads, Focus Mode answers, or model-answer sources. |

## Atmosphere EvidenceBundle guardrails

- EvidenceBundle records support evidence closure; they are not source data, processed data, receipts, catalog records, release manifests, or public products.
- EvidenceBundle outranks generated summaries.
- If an Atmosphere claim lacks resolvable EvidenceBundle support, the safe outcome is `ABSTAIN`, `DENY`, `HOLD`, or `ERROR`, not an uncited answer.
- Concentration, AQI/report posture, low-cost sensor records, regulatory/archive posture, AOD/smoke proxies, model fields, forecasts, and advisory context are different evidence roles.
- AQI/report posture must not be bundled as raw pollutant concentration.
- AOD rasters, smoke masks, and model fields must not be bundled as observed PM2.5 or ozone measurements.
- Low-cost sensor values require caveat, correction, confidence, limitation, source-rights, policy, and review posture before public use.
- Atmosphere EvidenceBundle support does not create emergency, medical, life-safety, regulatory, exposure, damages, or impact conclusions by itself.
- AI summaries may reference only governed, released, evidence-supported surfaces and must preserve source-role and caveat posture; AI text is not evidence.
- Public clients and Focus Mode must use governed APIs, released artifacts, catalog/triplet records, EvidenceBundle-backed payloads, and policy-safe envelopes, not this directory directly.

> [!CAUTION]
> Do not expose `data/proofs/evidence_bundle/atmosphere/` directly as a public map, API, UI, download, Focus Mode answer, AI answer source, AQI advisory service, health/medical advice source, regulatory-exceedance determination, emergency alert, exposure/impact claim surface, or life-safety product. EvidenceBundle proof artifacts support governed evidence closure; they do not publish Atmosphere claims by themselves.

## Directory map

Actual child inventory remains **NEEDS VERIFICATION**. Use this as a proposed local organization pattern only after confirming current repo convention and validators.

```text
data/proofs/evidence_bundle/atmosphere/
├── README.md
├── bundles/                  # PROPOSED — Atmosphere EvidenceBundle records or indexes
├── evidence_refs/            # PROPOSED — EvidenceRef resolution maps
├── claim_support/            # PROPOSED — claim-to-bundle manifests
├── digest_closure/           # PROPOSED — source/processed/catalog/triplet/receipt digest closure
├── source_roles/             # PROPOSED — observed/AQI/low-cost/model/proxy role support
├── qa_freshness/             # PROPOSED — QA, correction, freshness, caveat bundle support
├── catalog_links/            # PROPOSED — bundle pointers used by catalog records
├── citation_validation/      # PROPOSED — pointers to citation-validation results, not validator authority
├── releases/                 # PROPOSED — bundle pointers used by release candidates, not ReleaseManifest authority
├── corrections/              # PROPOSED — bundle invalidation/correction pointers, not CorrectionNotice authority
├── validation/               # PROPOSED — lane-local validation notes, not ValidationReport authority
└── _README_TODO.md           # PROPOSED — remove after actual child inventory is documented
```

## Evidence ledger

| Source | Status | Supports | Limits |
|---|---|---|---|
| Previous file | CONFIRMED | Target existed as a blank placeholder. | Did not define Atmosphere EvidenceBundle boundaries. |
| `data/proofs/evidence_bundle/README.md` | CONFIRMED | Parent EvidenceBundle proof family currently exists as a greenfield stub. | Does not define global EvidenceBundle family behavior yet. |
| Repository search | CONFIRMED | Search found the Atmosphere proof parent, PM2.5 proof child, Evidence Drawer docs, Atmosphere catalog/lifecycle docs, and package docs. | Search is not a full tree audit. |
| `data/proofs/atmosphere/README.md` | CONFIRMED current repo doc / PROPOSED implementation | Defines Atmosphere proof support as EvidenceBundle/EvidenceRef closure and explicitly excludes public outputs, receipts, source registry, policy, release authority, schemas, and validators. | Does not prove concrete EvidenceBundle inventory or validator behavior. |
| `data/proofs/atmosphere/pm25_2026/README.md` | CONFIRMED child README | PM2.5 2026 child proof lane uses EvidenceBundle/EvidenceRef closure and PM2.5 anti-collapse guardrails. | Does not prove source manifest, receipt set, release state, or public route behavior. |
| `docs/architecture/ui/EVIDENCE_DRAWER.md` | CONFIRMED doctrine / PROPOSED implementation | Evidence Drawer requires cite-or-abstain, governed API claim resolution, EvidenceBundle resolution, policy gate, citation validation, finite negative states, and no direct browser access to canonical stores. | Does not prove implementation, route names, schemas, or validators. |
| `schemas/contracts/v1/evidence/evidence_bundle.schema.json` | NEEDS VERIFICATION | Expected EvidenceBundle machine-shape home. | Current schema contents and validator behavior were not verified in this task. |
| `policy/domains/atmosphere/` and `release/` | NEEDS VERIFICATION | Expected admissibility and release homes. | Current policy/release enforcement was not verified in this task. |

## Validation checklist

- [ ] Confirm actual child files and EvidenceBundle proof inventory under `data/proofs/evidence_bundle/atmosphere/`.
- [ ] Expand or reconcile parent `data/proofs/evidence_bundle/README.md` beyond stub.
- [ ] Confirm whether Atmosphere EvidenceBundle files are concrete records here, indexes pointing to global proof stores, or generated artifacts linked from catalog/release/governed API tests.
- [ ] Confirm EvidenceBundle, EvidenceRef, EvidenceDrawerPayload, DecisionEnvelope, proof index, claim-support, digest-closure, QA/freshness proof, source-role proof, and proof-invalidation schemas and contract homes.
- [ ] Confirm validators, fixtures, CI checks, EvidenceRef resolution checks, source-role checks, units checks, averaging-window checks, QA/correction checks, low-cost caveat checks, freshness checks, release-link checks, negative-state checks, and access-control enforcement.
- [ ] Confirm bundle references to RunReceipt, TransformReceipt, ValidationReport, PolicyDecision, ReviewRecord, ReleaseManifest, RollbackCard, CorrectionNotice, WithdrawalNotice, and AIReceipt are pointers, not misplaced records.
- [ ] Confirm AQI-as-concentration, AOD-as-PM2.5, model-as-observed, low-cost-without-caveat, stale-without-freshness, rights-unclear, source-role-unclear, health/action claims, emergency/advisory claims, and release-unclear artifacts cannot pass from bundle support into public routes.
- [ ] Confirm public-candidate transitions are governed, evidence-backed, citation-safe, source-role-safe, units-safe, caveat-safe, rights-safe, freshness-safe, policy-safe, review-backed, release-linked, and reversible.
- [ ] Confirm no RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, PUBLISHED, receipt, registry, release, schema, policy, validator, package, pipeline, app, API, public map, public tile, direct download, Focus Mode answer, advisory service, health/medical advice, regulatory-exceedance determination, emergency alert, exposure/impact claim, or life-safety artifact is misplaced here.
- [ ] Confirm public clients and Focus Mode cannot read this lane directly as public truth, public Atmosphere service, public AQI service, public map, public tile, public API, public UI, or AI-answer source.

## Rollback

Rollback is required if this lane becomes a RAW source-data root, WORK scratch root, QUARANTINE bypass, PROCESSED substitute, catalog root, triplet root, public output root, `data/published/` substitute, receipt store, source-registry root, release-decision root, schema root, policy root, validator root, implementation root, direct public API shortcut, direct public UI shortcut, direct public tile shortcut, direct public exposure shortcut, unrestricted canonical EvidenceBundle authority root without ADR, citation-bypass path, AQI-as-concentration path, AOD-as-observed-pollutant path, model-as-observed path, low-cost-without-caveat path, stale-without-freshness path, proof-without-evidence path, uncited-AI-answer source, advisory service, health/medical advice surface, regulatory-exceedance determination, emergency alert, exposure/impact claim surface, or life-safety guidance source.

Rollback target for this expansion: previous blank placeholder blob SHA `8b137891791fe96927ad78e64b0aad7bded08bdc`.

<p align="right"><a href="#top">Back to top</a></p>
