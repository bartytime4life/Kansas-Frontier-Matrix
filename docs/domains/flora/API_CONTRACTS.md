<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/domains/flora/api-contracts
title: Flora — API Contracts
type: standard
version: v1
status: draft
owners: <flora-domain-steward + governed-api-owner — placeholder>
created: 2026-05-16
updated: 2026-05-16
policy_label: public
related:
  - docs/domains/flora/README.md
  - docs/domains/flora/SOURCES.md
  - docs/domains/flora/SENSITIVITY.md
  - docs/architecture/governed-api.md
  - docs/architecture/trust-membrane.md
  - contracts/runtime/decision_envelope.md
  - contracts/runtime/runtime_response_envelope.md
  - contracts/evidence/evidence_bundle.md
  - contracts/domains/flora/
  - schemas/contracts/v1/domains/flora/
  - policy/domains/flora/
  - policy/sensitivity/flora/
  - docs/doctrine/directory-rules.md
tags: [kfm, flora, api, governed-api, contracts, trust-membrane]
notes:
  - Implementation-layer claims (routes, payload shapes, file paths) are PROPOSED until verified against a mounted repo and ADR-0001.
  - Source-role anti-collapse and T4 default for sensitive flora locations are CONFIRMED doctrine.
[/KFM_META_BLOCK_V2] -->

# Flora — API Contracts

> The governed-API surface and finite-outcome contract for the Flora domain. Defines the request shapes, response envelopes, schema homes, and gate semantics through which Flora evidence reaches public, reviewer, and AI surfaces — without bypassing the trust membrane.

[![status: draft](https://img.shields.io/badge/status-draft-yellow.svg)](#)
[![authority: standard doc](https://img.shields.io/badge/authority-standard%20doc-blue.svg)](#)
[![doctrine: CONFIRMED](https://img.shields.io/badge/doctrine-CONFIRMED-success.svg)](#)
[![implementation: PROPOSED](https://img.shields.io/badge/implementation-PROPOSED-orange.svg)](#)
[![sensitivity: deny-by-default](https://img.shields.io/badge/sensitivity-deny--by--default-critical.svg)](#)
[![policy-label: public](https://img.shields.io/badge/policy--label-public-blue.svg)](#)
<!-- TODO: replace with live Shields.io endpoints once docs CI badge contract is established. -->

| Field | Value |
|---|---|
| **Status** | `draft` |
| **Owners** | `<flora-domain-steward + governed-api-owner>` *(placeholder — confirm against `CODEOWNERS`)* |
| **Updated** | `2026-05-16` |
| **Doctrine layer** | CONFIRMED (Atlas v1.1 §24.3, ENCY §7.6 J., GAI envelopes) |
| **Implementation layer** | PROPOSED / NEEDS VERIFICATION (routes, paths, payload shapes) |

---

## Contents

1. [Scope and boundary](#1-scope-and-boundary)
2. [Trust membrane and authority](#2-trust-membrane-and-authority)
3. [API surfaces (governed)](#3-api-surfaces-governed)
4. [Finite-outcome contract](#4-finite-outcome-contract)
5. [Per-surface contracts](#5-per-surface-contracts)
6. [Object families and schema homes](#6-object-families-and-schema-homes)
7. [Source-role anti-collapse for Flora](#7-source-role-anti-collapse-for-flora)
8. [Sensitivity tiers — Flora defaults](#8-sensitivity-tiers--flora-defaults)
9. [Cross-lane request constraints](#9-cross-lane-request-constraints)
10. [Lifecycle and promotion gates](#10-lifecycle-and-promotion-gates)
11. [Governed AI / Focus Mode behavior](#11-governed-ai--focus-mode-behavior)
12. [Validators, tests, and fixtures](#12-validators-tests-and-fixtures)
13. [Open questions and verification backlog](#13-open-questions-and-verification-backlog)
14. [Related docs](#14-related-docs)

---

## 1. Scope and boundary

This document specifies the **governed-API contract surface** for the Flora domain: how Flora evidence is requested, how the system answers, what the system refuses, and what artifacts every response must carry. It is a **standard doc**, not a runbook and not a schema definition — schemas live under `schemas/contracts/v1/` and policy lives under `policy/`.

**In scope.** Domain feature/detail lookup, layer manifest resolution, Evidence Drawer payloads, Focus Mode requests/responses, correction submission, and review decisions — as they apply to Flora object families.

**Out of scope.** Internal pipeline contracts (RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET), watcher non-publisher contracts, executable JSON Schema definitions, and policy bundle implementations. Those are anchored elsewhere; this doc references them.

> [!IMPORTANT]
> **Doctrine vs. implementation.** The decision-envelope grammar, finite-outcome set, trust membrane, and sensitivity tiering rules cited here are **CONFIRMED doctrine** from KFM core sources. Concrete route names, payload field lists, file paths, and CI behavior are **PROPOSED** or **NEEDS VERIFICATION** until checked against a mounted repository and accepted ADRs. Do not read this document as proof of route existence or implementation maturity.

[Back to top](#flora--api-contracts)

---

## 2. Trust membrane and authority

CONFIRMED doctrine: public clients and normal UI surfaces consume **governed APIs** that enforce release state, policy, evidence, rights, and sensitivity before any payload leaves the trust spine. Direct reads from canonical stores, RAW/WORK/QUARANTINE, internal triplets, model runtimes, or unpublished candidates are forbidden by the trust membrane.

```mermaid
flowchart LR
    subgraph Public["Public surface (deny-by-default)"]
        UI[MapLibre shell · Evidence Drawer · Focus Mode]
    end

    subgraph Membrane["Governed API (apps/governed-api/ — PROPOSED)"]
        ROUTE[Routes]
        POL[PolicyDecision check]
        EVD[EvidenceRef → EvidenceBundle resolver]
        REL[ReleaseManifest check]
        AIR[AIReceipt emit · cite-or-abstain]
        ENV[Finite outcome envelope]
    end

    subgraph Internal["Internal — never directly public"]
        RAW[(RAW)]
        WQ[(WORK / QUARANTINE)]
        PROC[(PROCESSED)]
        CAT[(CATALOG / TRIPLET)]
        PUB[(PUBLISHED — public-safe artifacts)]
    end

    UI -->|HTTP request| ROUTE
    ROUTE --> POL
    POL --> EVD
    EVD --> REL
    REL --> AIR
    AIR --> ENV
    ENV -->|ANSWER / ABSTAIN / DENY / ERROR / HOLD| UI

    REL -.reads.-> PUB
    EVD -.resolves from.-> CAT
    POL -.consults.-> CAT

    UI -.X forbidden direct read X.-> RAW
    UI -.X forbidden direct read X.-> WQ
    UI -.X forbidden direct read X.-> PROC
```

> [!NOTE]
> **Co-location does not erase the boundary.** Even if the governed API and the UI ship in the same monorepo, the trust membrane is enforced at the API contract — not at the network seam. The Flora domain inherits this rule with no carve-out.

[Back to top](#flora--api-contracts)

---

## 3. API surfaces (governed)

The following surfaces are the **Flora-specific projections** of the cross-cutting governed-API surfaces named in ENCY §J and Atlas v1.1 §24.3.2. Routes are PROPOSED; the precise path strings are subject to backend framework verification and ADR.

| # | Surface | Method / route (PROPOSED) | Request DTO | Response envelope | Allowed outcomes | Status |
|---|---|---|---|---|---|---|
| F1 | Flora feature/detail lookup | `GET /api/v1/domains/flora/features/{feature_id}` | path + query | **FloraDecisionEnvelope** *(projection of `DecisionEnvelope`)* | `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` | PROPOSED |
| F2 | Flora layer manifest resolver | `GET /api/v1/layers/{layer_id}/manifest` *(layer_id ∈ flora.*)* | path | `LayerManifest` / `LayerDescriptor` | `ANSWER` / `DENY` / `ERROR` | PROPOSED |
| F3 | Flora Evidence Drawer payload | `GET /api/v1/domains/flora/drawer/{feature_id}` *(or composed)* | path + `MapContextEnvelope` | `EvidenceDrawerPayload` (Flora projection) | `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` | PROPOSED |
| F4 | Flora Focus Mode answer | `POST /api/v1/focus` *(domain-scoped)* | `FocusModeRequest` + `MapContextEnvelope` | `FocusModeResponse` / `RuntimeResponseEnvelope` + `AIReceipt` | `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` | PROPOSED |
| F5 | Flora evidence resolution | `GET /api/v1/evidence/{evidence_ref}` | path | `EvidenceBundle` | `ANSWER` / `DENY` / `ERROR` | PROPOSED |
| F6 | Flora correction submit | `POST /api/v1/corrections` *(target ∈ flora)* | `CorrectionNoticeCandidate` | `CorrectionNotice` receipt | `ACCEPTED` / `DENY` / `ERROR` | PROPOSED |
| F7 | Flora review decision | `POST /api/v1/review/{queue}/{id}/decision` *(steward only)* | `ReviewRecord` candidate | `ReviewRecord` | `ALLOW` / `RESTRICT` / `DENY` / `HOLD` / `ERROR` | PROPOSED |

> [!CAUTION]
> **Routes are PROPOSED.** The Atlas v1.1 §J table records "Flora feature/detail resolver; route TBD" with status "PROPOSED governed API surface; exact route UNKNOWN." If the mounted repo or an accepted ADR fixes a different shape (e.g., `apps/governed_api` vs. `apps/governed-api`, plural `features` vs. nested `species`), this table updates and a DRIFT_REGISTER entry is opened.

[Back to top](#flora--api-contracts)

---

## 4. Finite-outcome contract

CONFIRMED doctrine: every Flora governed-API response returns a **finite outcome** drawn from a known set. Deny, abstain, and error are first-class outcomes — not failure modes. The shape varies by surface, but the outcome enum is constant.

| Outcome | When (CONFIRMED doctrine) | Required artifacts | Flora-specific examples |
|---|---|---|---|
| `ANSWER` | Evidence sufficient, policy permits, release state allows, review state recorded where required. | Resolved `EvidenceBundle`; `PolicyDecision = allow`; applicable `ReleaseManifest`; for AI: `AIReceipt` + passing `CitationValidationReport`. | Released vegetation community polygon click; generalized public range layer; phenology summary citation. |
| `ABSTAIN` | Evidence insufficient/incomplete, citation cannot resolve, evidence stale with no released alternative, or AI surface cannot cite. | `AIReceipt` with reason; no claim emitted. | Plant taxon page with unresolved synonymy; Focus Mode question that exceeds released evidence; stale specimen evidence beyond cadence. |
| `DENY` | Policy, rights, sensitivity, or release state forbids the answer. **Sensitive Flora lanes default here.** | `PolicyDecision = deny` + `reason_code`; for AI: `AIReceipt` records the denial. | Exact rare-plant coordinates; ethnobotanical site location; pre-release candidate; rights-unclear specimen geometry. |
| `ERROR` | Governed API cannot evaluate — missing schema, malformed query, contract violation, infrastructure failure. | Error envelope with diagnostic code; no claim leakage; no silent fall-through to another lane. | Malformed `feature_id`; schema-validation failure on inbound `FocusModeRequest`. |
| `HOLD` | Promotion / release / correction is paused pending steward, rights-holder, or policy review. | `ReviewRecord` pending; `PolicyDecision = hold`; surface remains in prior state. | Rare-plant redaction approval awaiting steward; ethnobotanical content awaiting cultural review. |

Validator-class outcomes `PASS` / `FAIL` are internal to admission and promotion gates (Section 10); they do not appear in public response envelopes directly but feed `PolicyDecision` and `PromotionDecision`.

> [!WARNING]
> **Deny is not error.** A Flora response of `DENY` for an exact sensitive location is **operating correctly**. UI surfaces must render denial reason and offer the non-restricted alternative (e.g., a generalized public range layer) where available. Treating `DENY` as an error condition collapses the sensitivity discipline.

[Back to top](#flora--api-contracts)

---

## 5. Per-surface contracts

This section sketches the **request/response shape** for each Flora surface. Exact field lists are PROPOSED and must be reconciled against the canonical schemas under `schemas/contracts/v1/` (see Section 6).

### 5.1 F1 — Flora feature/detail lookup

PROPOSED behavior: resolves a Flora feature (occurrence, specimen, community, range polygon, rare-plant record) to an evidence-bounded detail payload through the governed-API trust membrane.

<details>
<summary><b>Illustrative envelope sketch — PROPOSED, not normative</b></summary>

```json
{
  "outcome": "ANSWER",
  "domain": "flora",
  "feature": {
    "feature_id": "kfm:flora:occurrence:<id>",
    "object_family": "FloraOccurrence",
    "source_role": "observed",
    "geometry": { /* public-safe — may be generalized */ },
    "valid_time": { "start": "...", "end": "..." },
    "observed_time": "...",
    "release_state": "PUBLISHED"
  },
  "evidence_refs": [
    { "evidence_ref": "kfm:evd:<bundle-id>", "role": "primary" }
  ],
  "policy_decision": {
    "outcome": "allow",
    "reasons": ["public-safe", "rights-resolved"],
    "obligations": ["display-citation"]
  },
  "release_manifest_ref": "kfm:rel:<manifest-id>",
  "freshness": { "state": "fresh" },
  "audit_ref": "kfm:audit:<id>"
}
```

This sketch is illustrative only. Authoritative shape is the `DecisionEnvelope` schema at `schemas/contracts/v1/runtime/decision_envelope.schema.json` (PROPOSED home).

</details>

### 5.2 F2 — Flora layer manifest resolver

Returns the released `LayerManifest` for a Flora layer (e.g., generalized occurrence layer, public range layer, vegetation community layer, invasive plant layer, phenology/condition layer). PROPOSED behavior: serving a layer that lacks a `ReleaseManifest` is forbidden; WORK and CATALOG layers are never served to public clients.

### 5.3 F3 — Flora Evidence Drawer payload

CONFIRMED doctrine: `EvidenceDrawerPayload` is a **governed projection** of the canonical `EvidenceBundle`, not a parallel evidence store. The projection lets UI evolve without renegotiating canonical evidence shape, and tests must verify the projection does not drop citation, policy, review, or release state.

### 5.4 F4 — Flora Focus Mode answer

CONFIRMED doctrine: governed AI is **interpretive, not authoritative**. Focus Mode answers over Flora must:

- Operate over a typed `MapContextEnvelope` composed of evidence building blocks — never freeform map text.
- Resolve every citation through `CitationValidationReport` before emitting `ANSWER`.
- ABSTAIN when evidence is insufficient or stale; DENY when policy, rights, sensitivity, or release state forbids the answer.
- Emit an `AIReceipt` carrying model/provider, prompt scope, evidence IDs, policy decision, outcome, and citation report ID.

### 5.5 F5 — Flora evidence resolution

Resolves an `EvidenceRef` to the corresponding `EvidenceBundle`. Returns `DENY` if the bundle's release state, rights, or sensitivity forbids public exposure for the requesting role.

### 5.6 F6 / F7 — Correction and review

Correction submission and review-decision posting follow the cross-cutting governed-API contract. Flora-specific behavior: corrections targeting sensitive geometry transit through the same redaction/generalization review path as initial publication.

[Back to top](#flora--api-contracts)

---

## 6. Object families and schema homes

CONFIRMED Flora object families (ENCY §7.6, Atlas v1.1 §8.E); identity rule is PROPOSED.

| Object family | Purpose in Flora | Canonical home (PROPOSED) | Status |
|---|---|---|---|
| `PlantTaxon` | Plant taxonomic identity, synonymy, authority. | `schemas/contracts/v1/domains/flora/plant_taxon.schema.json` | PROPOSED |
| `FloraTaxon Crosswalk` | Cross-vocabulary alignment (e.g., GBIF / iNat / PLANTS / NatureServe). | `schemas/contracts/v1/domains/flora/` | PROPOSED |
| `FloraOccurrence` | Specimen- or observation-derived occurrence, with uncertainty and geoprivacy. | `schemas/contracts/v1/domains/flora/` | PROPOSED |
| `SpecimenRecord` | Herbarium specimen record. | `schemas/contracts/v1/domains/flora/` | PROPOSED |
| `RarePlantRecord` | Steward-controlled rare/protected record. **T4 default.** | `schemas/contracts/v1/domains/flora/` | PROPOSED |
| `VegetationCommunity` | Community polygon and classification. | `schemas/contracts/v1/domains/flora/` | PROPOSED |
| `InvasivePlantRecord` | Invasive-species record. | `schemas/contracts/v1/domains/flora/` | PROPOSED |
| `PhenologyObservation` | Phenology time-series observation. | `schemas/contracts/v1/domains/flora/` | PROPOSED |
| `RangePolygon` | Distribution/range polygon (generalized public derivative or modeled surface). | `schemas/contracts/v1/domains/flora/` | PROPOSED |
| `HabitatAssociation` | Cross-lane link to habitat (not habitat truth). | `schemas/contracts/v1/domains/flora/` | PROPOSED |
| `BotanicalSurvey` | Survey campaign metadata. | `schemas/contracts/v1/domains/flora/` | PROPOSED |
| `RestorationPlanting` | Restoration planting record. | `schemas/contracts/v1/domains/flora/` | PROPOSED |
| `RedactionReceipt` | Transform receipt for sensitivity redaction/generalization. | `schemas/contracts/v1/policy/` *(cross-cutting)* | PROPOSED |

Cross-cutting envelope and evidence schemas referenced by Flora surfaces (canonical, not Flora-owned):

| Schema | Canonical home (PROPOSED per ADR-0001) | Owning layer |
|---|---|---|
| `DecisionEnvelope` | `schemas/contracts/v1/runtime/decision_envelope.schema.json` | Runtime |
| `RuntimeResponseEnvelope` | `schemas/contracts/v1/runtime/runtime_response_envelope.schema.json` | Runtime |
| `EvidenceDrawerPayload` | `schemas/contracts/v1/ui/evidence_drawer_payload.schema.json` | UI projection |
| `EvidenceBundle` / `EvidenceRef` | `schemas/contracts/v1/evidence/` | Evidence |
| `LayerManifest` / `LayerDescriptor` | `schemas/contracts/v1/layers/` *(or `schemas/contracts/v1/map/`)* | Layer |
| `FocusModeRequest` / `FocusModeResponse` | `schemas/contracts/v1/focus/` *(or `schemas/contracts/v1/ai/`)* | Focus / AI |
| `CitationValidationReport` | `schemas/contracts/v1/evidence/` *(or `schemas/contracts/v1/ai/`)* | Evidence / AI |
| `AIReceipt` | `schemas/contracts/v1/ai/ai_receipt.schema.json` | AI runtime |
| `PolicyDecision` | `schemas/contracts/v1/policy/policy_decision.schema.json` | Policy |
| `SourceDescriptor` | `schemas/contracts/v1/source/source_descriptor.schema.json` | Source |

> [!NOTE]
> **Schema-home conflict surfaced.** Atlas v1.1 §24.13 records the Flora schema root as `schemas/contracts/v1/flora/`; Directory Rules §6.4 records the canonical pattern as `schemas/contracts/v1/domains/<domain>/` (e.g., `schemas/contracts/v1/domains/flora/`). This document follows the Directory-Rules canonical pattern per ADR-0001 (schema home) and flags the Atlas crosswalk as a candidate `DRIFT_REGISTER` entry. **NEEDS VERIFICATION**: actual repo layout against ADR-0001.

[Back to top](#flora--api-contracts)

---

## 7. Source-role anti-collapse for Flora

CONFIRMED doctrine (Atlas v1.1 §24.1): `source_role` is a first-class identity attribute on every `SourceDescriptor`. A Flora API response **must never** collapse source roles — an observation is not a model, a regulatory designation is not an observation, a community-science aggregate is not a steward-reviewed record. Mismatch between claim type and source role is a **deny condition**, not a quality issue.

PROPOSED Flora role-to-claim matrix:

| Source role | Typical Flora example | Claim it may support | Claim it may **NOT** support |
|---|---|---|---|
| `observed` | KU herbarium specimen; ground botanical survey. | Specimen-level occurrence at observed time. | Regulatory listing status; modeled range. |
| `regulatory` | USFWS ECOS plant listing; state rare-plant designation. | Legal/conservation status. | An observed occurrence event. |
| `modeled` | Distribution suitability surface; restoration suitability model. | Modeled range / suitability with model run receipt. | A field-confirmed occurrence. |
| `aggregate` | GBIF download / aggregator; county taxa package. | County- or region-level aggregate counts. | A per-place record. |
| `administrative` | Restoration project registry; state stewardship list. | Administrative context. | Independent ecological observation. |
| `candidate` | Pre-review iNaturalist record; PLANTS drift candidate. | Pending steward review only. | Any public claim until promoted. |
| `synthetic` | Reconstructed range from interpretive synthesis. | Surface representation with `RealityBoundaryNote`. | Direct evidence. |

> [!IMPORTANT]
> **Join-induced sensitivity (CONFIRMED).** PLANTS-style county taxa packages and GBIF/iNaturalist aggregates are individually benign but can become sensitive when joined to occurrence sources for rare or culturally significant taxa. Sensitivity is a property of the **resulting product**, not just the inputs. Flora API surfaces must treat join-induced sensitivity as a deny condition for the join product.

[Back to top](#flora--api-contracts)

---

## 8. Sensitivity tiers — Flora defaults

CONFIRMED doctrine (Atlas v1.1 §24.5): KFM publishes the safest representation that still answers reasonable steward and public needs. Flora sensitivity defaults extend the cross-cutting tier scheme.

| Flora class | Default tier | Allowed transforms (PROPOSED) | Required gates |
|---|---|---|---|
| Public, non-listed, non-sensitive taxon | `T0` | None required beyond standard release. | `ReleaseManifest`. |
| Generalized public range / distribution layer | `T0` / `T1` | Aggregation / generalization to coarse cell. | `AggregationReceipt` or `RedactionReceipt`. |
| Generalized occurrence layer (non-sensitive) | `T0` / `T1` | Public-safe generalization where uncertainty is high. | `RedactionReceipt`. |
| Rare or culturally sensitive plant location | **`T4`** | Generalized geometry + steward review → `T2` or `T1`. | `RedactionReceipt` + `ReviewRecord`. |
| Ethnobotanical / culturally sensitive context | **`T4`** | Cultural review required; transforms recorded. | Cultural review + `ReviewRecord` + `PolicyDecision`. |
| Steward-controlled records | **`T4`** | Steward review with named-party agreement → `T3` or `T2`. | `PolicyDecision` + `ReviewRecord`. |
| RAW / WORK / QUARANTINE access via API | **`T4` forever** | None — AI and public surfaces never read pre-release content. | Trust membrane (Section 2). |

Tier transitions follow the cross-cutting motion table (Atlas v1.1 §24.5.3): upgrades toward public require both a transform receipt and a review record; downgrades to T4 are always permitted via `CorrectionNotice` alone.

> [!CAUTION]
> **Style-only hiding is not redaction.** Hiding a Flora feature with a MapLibre style filter while serving the underlying tile **is not** an acceptable sensitivity transform. The deny must happen at the API and tile-artifact level (per the Master MapLibre sensitive-geometry-deny fixture standard).

[Back to top](#flora--api-contracts)

---

## 9. Cross-lane request constraints

Flora API responses must preserve cross-lane ownership boundaries. Requests that would relabel a non-Flora object as Flora — or vice versa — are policy violations.

| This domain | Related lane | Relation type | API constraint |
|---|---|---|---|
| Flora | Habitat | Habitat association, vegetation-community context. | Flora API returns habitat **association** only; habitat patches/suitability resolve through the Habitat API. |
| Flora | Fauna | Pollinator, food-web, invasive, biodiversity context. | Flora API does not return fauna occurrences; Fauna sensitivity discipline still applies to any cross-cited surface. |
| Flora | Soil / Hydrology | Substrate, wetland, riparian, drought context. | Flora API may cite Soil/Hydrology evidence but does not own it; canonical truth resolves through those domains. |
| Flora | Hazards | Fire, drought, flood, smoke, vegetation stress. | Flora API may cite hazard context; **KFM is never an alert authority**. |
| Flora | Archaeology | Ethnobotanical context. | Sovereignty / sensitivity review required; deny-default applies to cultural location detail. |

[Back to top](#flora--api-contracts)

---

## 10. Lifecycle and promotion gates

CONFIRMED doctrine: every Flora object follows `RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED`. Promotion is a **governed state transition, not a file move**. The governed API surfaces released artifacts only.

| Gate (transition) | Pre-condition | Required artifacts (PROPOSED minimum) | Failure-closed outcome |
|---|---|---|---|
| Admission (— → RAW) | Source identity, rights, role intent established. | `SourceDescriptor` (role, authority, rights, sensitivity, cadence); payload hash. | Source not admitted; logged as candidate awaiting steward. |
| Normalization (RAW → WORK / QUARANTINE) | Schema, geometry, time, identity, evidence, rights, policy runnable. | `TransformReceipt`; `ValidationReport`; `PolicyDecision`; quarantine for failures. | Quarantine with reason; never silent promote. |
| Validation (WORK → PROCESSED) | Validators deterministic; required receipts present. | `ValidationReport` pass; `RedactionReceipt` if sensitivity applies. | Stay in WORK; structured `FAIL`. |
| Catalog closure (PROCESSED → CATALOG / TRIPLET) | EvidenceRefs resolve; catalog/proof closure passes. | `EvidenceBundle`; graph/triplet projection where applicable. | HOLD at PROCESSED; no public edge. |
| Release (CATALOG → PUBLISHED) | Review state where required; release authority separated where materiality applies. | `ReleaseManifest`; rollback target; correction path; `ReviewRecord`. | HOLD at CATALOG; no public surface change. |
| Correction (PUBLISHED → PUBLISHED′) | Detected error or new evidence; derivatives identified. | `CorrectionNotice`; `RollbackCard` where applicable. | Stale-state badge; original surface preserved during review. |

Surfaces F1–F5 read only from `PUBLISHED`; F6 (correction) and F7 (review) operate on candidate or published artifacts under steward authority.

[Back to top](#flora--api-contracts)

---

## 11. Governed AI / Focus Mode behavior

CONFIRMED doctrine / PROPOSED implementation:

| AI behavior | Rule (CONFIRMED) |
|---|---|
| **Allowed** | Evidence-bounded summarization over released Flora `EvidenceBundle`s; citation-backed explanation; evidence comparison; steward-review draft notes; anomaly explanation. |
| **Required denial** | DENY direct RAW / WORK / QUARANTINE access; DENY sensitive-location exposure; DENY rights-unclear or stewardcontrolled record exposure; DENY uncited authoritative claims. |
| **Required abstention** | ABSTAIN when evidence is insufficient, stale without released alternative, or when citation cannot resolve. |
| **Required receipt** | Every Focus Mode answer emits an `AIReceipt` with `outcome ∈ {ANSWER, ABSTAIN, DENY, ERROR}`, `evidence_refs`, `policy_decision`, and `citation_validation` report ID. |

> [!IMPORTANT]
> **AI is interpretive, not authoritative.** A Flora Focus Mode answer is an API outcome, not a sovereign generation. Fluent text never substitutes for `EvidenceBundle`. Where evidence resolution fails, the answer ABSTAINS.

[Back to top](#flora--api-contracts)

---

## 12. Validators, tests, and fixtures

PROPOSED minimum test families for Flora API contracts (Atlas v1.1 §K, ENCY §K):

- Schema validation for inbound/outbound DTOs at every Flora surface.
- `SourceDescriptor` validation including `source_role`, rights, sensitivity.
- Rights and sensitivity validators (deny on unresolved rights or sensitivity).
- Evidence closure: every `EvidenceRef` in a Flora `ANSWER` resolves to a released `EvidenceBundle`.
- Temporal logic: source, observed, valid, retrieval, release, and correction times stay distinct where material.
- Geometry validity, including public-safe generalization checks.
- Policy DENY tests — including the **exact sensitive public geometry denial** fixture.
- Taxonomy reconciliation and synonymy tests.
- Citation validation: cite-or-abstain enforced before `ANSWER`.
- Stale-source fixture (cadence drift triggers stale badge or ABSTAIN).
- Release-manifest validation and rollback drill.
- No-network / no-live-source fixture pipeline so contract tests run hermetically.
- Source-role mismatch denial — e.g., aggregate cited as per-place truth fails closed.
- Non-regression for prior published lineage where relevant.

> [!TIP]
> **First credible thin-slice (ENCY §N).** One common species occurrence/specimen fixture plus one vegetation community polygon, both with `EvidenceBundle`-backed species page and public-safe map. This is the minimum slice to prove the Flora governed-API contract end-to-end without activating live sources.

[Back to top](#flora--api-contracts)

---

## 13. Open questions and verification backlog

| # | Item | Evidence that would settle it | Status |
|---|---|---|---|
| 1 | Exact Flora route names and HTTP shape under `apps/governed-api/`. | Mounted repo; accepted backend ADR. | NEEDS VERIFICATION |
| 2 | Schema-home: `schemas/contracts/v1/flora/` (Atlas §24.13) vs. `schemas/contracts/v1/domains/flora/` (Directory Rules §6.4). | ADR-0001 reconciliation; mounted repo. | NEEDS VERIFICATION (likely DRIFT entry) |
| 3 | `FloraDecisionEnvelope` vs. generic `DecisionEnvelope` — is the projection a distinct schema or a discriminator on the generic envelope? | ADR + schema definition. | UNKNOWN |
| 4 | Where do Focus Mode schemas live: `schemas/contracts/v1/focus/` or `schemas/contracts/v1/ai/`? | Mounted repo; ADR. | UNKNOWN |
| 5 | Exact thresholds for "exact" vs. "generalized" geometry for rare-plant publication (e.g., grid cell size, jitter radius). | Steward policy; PolicyDecision implementation. | NEEDS VERIFICATION |
| 6 | KDWP / Kansas Biological Survey / KU herbarium rights and steward roles for live source activation. | Live source agreements; SourceDescriptor entries. | NEEDS VERIFICATION |
| 7 | PLANTS / GBIF / iNaturalist join-sensitivity policy — exact deny rules and review queue routing. | Policy bundle; review-queue implementation. | NEEDS VERIFICATION |
| 8 | Layer-manifest resolver: shared with other domains or Flora-specific endpoint? | Mounted repo; ADR. | UNKNOWN |
| 9 | Whether correction-submit and review-decision are governed under domain-scoped policy bundles (`policy/domains/flora/`) or only cross-cutting bundles. | Policy layout under `policy/`. | NEEDS VERIFICATION |
| 10 | `RealityBoundaryNote` requirements for any Flora synthetic surface (e.g., suitability rasters rendered as continuous fields). | Schema + UI doctrine. | NEEDS VERIFICATION |

[Back to top](#flora--api-contracts)

---

## 14. Related docs

<!-- Many of these are PROPOSED siblings; placeholder links until repo evidence is confirmed. -->

- [`docs/domains/flora/README.md`](./README.md) — Flora domain landing doc *(PROPOSED)*
- [`docs/domains/flora/SOURCES.md`](./SOURCES.md) — Flora source families and source-role registry *(PROPOSED)*
- [`docs/domains/flora/SENSITIVITY.md`](./SENSITIVITY.md) — Flora sensitivity tiers and redaction policy *(PROPOSED)*
- [`docs/architecture/governed-api.md`](../../architecture/governed-api.md) — Trust membrane and governed-API doctrine *(PROPOSED)*
- [`docs/architecture/contract-schema-policy-split.md`](../../architecture/contract-schema-policy-split.md) — Layering reference *(PROPOSED)*
- [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md) — Placement and lifecycle doctrine
- [`docs/standards/PROV.md`](../../standards/PROV.md) — Provenance standards profile
- [`contracts/runtime/decision_envelope.md`](../../../contracts/runtime/decision_envelope.md) — `DecisionEnvelope` meaning *(PROPOSED)*
- [`contracts/runtime/runtime_response_envelope.md`](../../../contracts/runtime/runtime_response_envelope.md) — `RuntimeResponseEnvelope` meaning *(PROPOSED)*
- [`contracts/evidence/evidence_bundle.md`](../../../contracts/evidence/evidence_bundle.md) — `EvidenceBundle` meaning *(PROPOSED)*
- [`schemas/contracts/v1/domains/flora/`](../../../schemas/contracts/v1/domains/flora/) — Flora JSON Schemas home *(PROPOSED)*
- [`policy/domains/flora/`](../../../policy/domains/flora/) — Flora policy bundle home *(PROPOSED)*
- [`policy/sensitivity/flora/`](../../../policy/sensitivity/flora/) — Flora sensitivity policy *(PROPOSED)*

---

<sub><b>Last updated:</b> 2026-05-16 · <b>Doc status:</b> draft · <b>Doctrine basis:</b> CONFIRMED · <b>Implementation basis:</b> PROPOSED / NEEDS VERIFICATION · <a href="#flora--api-contracts">↑ Back to top</a></sub>
