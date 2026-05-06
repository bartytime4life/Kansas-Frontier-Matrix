<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/TODO-ASSIGN-UUID
title: Atmosphere / Air Architecture
type: standard
version: v1
status: draft
owners: TODO-VERIFY: atmosphere-air domain steward, data steward, policy steward
created: TODO-VERIFY-YYYY-MM-DD
updated: 2026-05-06
policy_label: public-draft-NEEDS_VERIFICATION
related: [../README.md, ../../../adr/ADR-0312-atmosphere-air-source-role-boundaries.md, ../../../adr/ADR-0431-atmosphere-air-knowledge-character-boundary.md, ../../../adr/ADR-0418-atmosphere-air-schema-slug-compatibility.md, ../../../architecture/contract-schema-policy-split.md, ../../../../connectors/pipelines/air/README.md, ../../../../pipelines/normalize/domains/atmosphere/README.md, ../../../../policy/air/air_qa.rego, ../../../../tools/validators/air/validate_air_qa.py, ../../../../tools/publishers/air/build_air_release_candidate.py, ../../../../data/processed/air/qa_summary.example.json, ../../../../data/receipts/air/run_receipt.example.json, NEEDS_VERIFICATION: ../../../../schemas/contracts/v1/air/, NEEDS_VERIFICATION: ../../../../schemas/contracts/v1/atmosphere/]
tags: [kfm, atmosphere-air, architecture, evidence, source-role, knowledge-character, map-first, time-aware, governed-domain]
notes: [Revises repo-visible docs/domains/atmosphere_air/architecture/ARCHITECTURE.md. Local workspace was not a mounted Git checkout; repo path and adjacent files were checked through the GitHub connector. doc_id, owners, created date, final policy label, schema inventory, CI status, and release maturity remain NEEDS VERIFICATION.]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Atmosphere / Air Architecture

Trust-preserving architecture for atmosphere and air-quality evidence from source admission through governed map, API, Evidence Drawer, Focus Mode, publication, correction, and rollback surfaces.

<p align="center">
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Path: confirmed" src="https://img.shields.io/badge/path-confirmed_on_main-2ea44f">
  <img alt="Source role: required" src="https://img.shields.io/badge/source_role-required-0a7ea4">
  <img alt="Knowledge character: required" src="https://img.shields.io/badge/knowledge_character-required-6f42c1">
  <img alt="Publication: release gated" src="https://img.shields.io/badge/publication-release--gated-b60205">
  <img alt="Public access: governed only" src="https://img.shields.io/badge/public-governed_API_only-5319e7">
</p>

<p align="center">
  <a href="#architecture-posture">Posture</a> ·
  <a href="#repo-fit">Repo fit</a> ·
  <a href="#domain-boundary">Domain boundary</a> ·
  <a href="#trust-flow">Trust flow</a> ·
  <a href="#bounded-contexts">Bounded contexts</a> ·
  <a href="#knowledge-character-taxonomy">Taxonomy</a> ·
  <a href="#current-no-network-slice">Current slice</a> ·
  <a href="#validation-and-policy">Validation</a> ·
  <a href="#public-surface-contract">Public surfaces</a> ·
  <a href="#open-verification-backlog">Open verification</a>
</p>

> [!IMPORTANT]
> This architecture does **not** authorize live source fetching, public release, public map layers, direct UI/API access to internal lifecycle data, or Focus Mode answers. It defines the lane boundary that future schemas, validators, policy checks, EvidenceBundles, release manifests, and rollback records must preserve.

---

## Architecture posture

The Atmosphere / Air lane is not a single “air layer.” It is a governed domain lane for atmospheric observations, air-quality reports, regulatory archives, low-cost sensor candidates, model fields, smoke and aerosol context, remote-sensing masks, climate anomaly support, fusion products, advisories, station metadata, temporal support, and public-safe map delivery.

The architecture exists to prevent **epistemic collapse**: a visually persuasive map, chart, tile, popup, or AI answer must not make fundamentally different evidence classes look equivalent.

| Architectural rule | Status | Consequence |
|---|---:|---|
| Preserve `source_role` and `knowledge_character` end to end. | CONFIRMED doctrine / PROPOSED enforcement | Every consequential object must state what kind of source it came from and what kind of knowledge it represents. |
| Keep observed, modeled, reported, classified, advisory, and fused products distinct. | CONFIRMED doctrine | AQI, PM concentration, AOD, smoke masks, model fields, climate anomalies, advisories, and fusion products are not interchangeable. |
| Public delivery consumes released artifacts and governed envelopes only. | CONFIRMED doctrine | UI, API, exports, map layers, and Focus Mode must not read `RAW`, `WORK`, `QUARANTINE`, connector-private output, or unpublished candidates directly. |
| Promotion is a governed decision. | CONFIRMED doctrine | Promotion requires evidence, policy, review, proof, release, correction, and rollback state; it is not a file move or script success. |
| Current implementation depth is bounded. | CONFIRMED repo evidence / NEEDS VERIFICATION | A no-network air QA slice is repo-visible; complete schema inventory, CI enforcement, proof closure, and public release remain unverified. |

### Non-negotiables

1. No direct public UI/API/Focus access to `RAW`, `WORK`, `QUARANTINE`, connector-private output, normalization candidates, unpublished processed candidates, or direct model outputs.
2. No public object without source role, knowledge character, rights posture, evidence closure, review state, release state, correction path, and rollback target appropriate to its public burden.
3. No modeled, fused, interpolated, or remote-sensing object labeled as observed.
4. No AQI or public report index presented as raw concentration.
5. No AOD, smoke mask, plume mask, hotspot, or classification product presented as surface exposure measurement without governed model/fusion support.
6. No run receipt, QA summary, map tile, graph projection, vector index, summary, or Focus answer treated as sovereign truth.

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Repo fit

This file belongs under the `docs/` responsibility root because it is human-facing architecture doctrine for a domain lane. Domain-specific material belongs under `docs/domains/<lane>/`; machine validation belongs under the active schema home; policy belongs under `policy/`; lifecycle data belongs under `data/`; connector logic belongs under `connectors/`; and runtime/public clients remain downstream of governed APIs and released artifacts.

| Surface | Path | Status | Role |
|---|---|---:|---|
| Architecture doc | `docs/domains/atmosphere_air/architecture/ARCHITECTURE.md` | CONFIRMED target | This file. Trust-preserving architecture for the lane. |
| Domain README | [`../README.md`](../README.md) | CONFIRMED | Lane orientation, accepted inputs, exclusions, knowledge-character posture, denial codes, and first-PR discipline. |
| Source-role ADR | [`../../../adr/ADR-0312-atmosphere-air-source-role-boundaries.md`](../../../adr/ADR-0312-atmosphere-air-source-role-boundaries.md) | CONFIRMED / draft | Mandatory source-role and knowledge-character decision boundary. |
| Knowledge-character ADR | [`../../../adr/ADR-0431-atmosphere-air-knowledge-character-boundary.md`](../../../adr/ADR-0431-atmosphere-air-knowledge-character-boundary.md) | CONFIRMED / draft | Release/UI/Focus boundary for knowledge characters and anti-collapse rules. |
| Slug compatibility ADR | [`../../../adr/ADR-0418-atmosphere-air-schema-slug-compatibility.md`](../../../adr/ADR-0418-atmosphere-air-schema-slug-compatibility.md) | CONFIRMED / proposed | Governs `atmosphere_air`, `air`, and `atmosphere` naming and migration compatibility. |
| Contract / schema / policy split | [`../../../architecture/contract-schema-policy-split.md`](../../../architecture/contract-schema-policy-split.md) | CONFIRMED / draft | Keeps semantic contracts, machine schemas, and admissibility policy separate. |
| No-network connector lane | [`../../../../connectors/pipelines/air/README.md`](../../../../connectors/pipelines/air/README.md) | CONFIRMED | Connector-local no-network candidate and receipt flow. |
| Normalization lane | [`../../../../pipelines/normalize/domains/atmosphere/README.md`](../../../../pipelines/normalize/domains/atmosphere/README.md) | CONFIRMED | Execution-near normalization guidance; not public release. |
| Policy example | [`../../../../policy/air/air_qa.rego`](../../../../policy/air/air_qa.rego) | CONFIRMED | Current air QA deny rules for threshold and missing-reference gates. |
| Validator example | [`../../../../tools/validators/air/validate_air_qa.py`](../../../../tools/validators/air/validate_air_qa.py) | CONFIRMED / blocked by schema inventory | Validates QA summary shape and local policy gates when required schema exists. |
| Release-candidate builder | [`../../../../tools/publishers/air/build_air_release_candidate.py`](../../../../tools/publishers/air/build_air_release_candidate.py) | CONFIRMED / NEEDS VERIFICATION | Builds catalog/proof/release candidates, but references schema files whose inventory must be verified. |
| QA candidate | [`../../../../data/processed/air/qa_summary.example.json`](../../../../data/processed/air/qa_summary.example.json) | CONFIRMED / candidate only | No-network processed candidate; not public truth. |
| Run receipt | [`../../../../data/receipts/air/run_receipt.example.json`](../../../../data/receipts/air/run_receipt.example.json) | CONFIRMED / process memory only | No-network connector receipt; not proof or release authority. |
| Schema family | `schemas/contracts/v1/air/` and/or `schemas/contracts/v1/atmosphere/` | NEEDS VERIFICATION | Do not claim schema authority or migration until ADR-0418 acceptance, inventory, fixtures, validators, and rollback evidence exist. |

> [!WARNING]
> `atmosphere_air` is the current documentation lane, `air` is the current no-network implementation/tooling slice, and `atmosphere` is a proposed whole-domain schema/normalization concept. Do not silently rename, collapse, alias, or publish across those surfaces.

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Domain boundary

### Included object families

| Family | Examples | Architectural burden |
|---|---|---|
| Observed sensor records | PM2.5, PM10, ozone, NO₂, SO₂, CO, temperature, humidity, wind, pressure, visibility | Preserve source, instrument/site context, raw value/unit, normalized value/unit, source payload hash, time basis, and EvidenceRefs. |
| Public AQI reports | AQI, NowCast, public agency index/report objects | Treat as report/index objects; never as raw concentration. |
| Regulatory archives | AQS-like or equivalent quality-assured archives | Use as archive/regulatory evidence; do not imply live state by default. |
| Low-cost sensor candidates | PurpleAir-like or equivalent contributor networks | Require correction method, caveats, confidence, rights, and limitations before public use. |
| Model fields | Forecast, reanalysis, hindcast, transport, smoke, aerosol, chemistry fields | Label as modeled and expose model identity, uncertainty, valid time, and model-card support. |
| Remote-sensing masks | Smoke plumes, AOD, fire hotspots, aerosol/cloud/haze masks | Treat as classification/support context, not exposure or PM concentration. |
| Climate/anomaly context | Normals, anomalies, baselines, downscaling, hindcasts | Label as context; not live alerting or emergency instruction. |
| Fusion products | Interpolation, consensus, bias correction, ensembles, fused grids | Preserve input EvidenceRefs, method, transform hash, uncertainty, and derived status. |
| Advisory context | Public messages, health notices, agency advisories | Keep issuer, temporal scope, and source; KFM is not an emergency alerting system. |
| Network/site context | Station metadata, provider IDs, cadence, instrument state, siting caveats, station health | Supports interpretation; not a measurement value. |
| Temporal support | Freshness windows, rolling baselines, persistence/hysteresis windows | Prevents stale context from appearing current. |

### Excluded from this architecture surface

| Exclusion | Correct home or behavior | Reason |
|---|---|---|
| Source credentials, API keys, tokens, `.env` files | Never commit; use approved secrets management. | Docs must not expose access secrets. |
| Machine schema bodies | Active schema home after ADR verification. | Architecture explains boundaries; schemas validate shape. |
| Executable policy decisions | `policy/` and policy tests. | Policy must remain reviewable and testable. |
| RAW, WORK, QUARANTINE payloads | Lifecycle `data/` roots. | Public docs are not lifecycle storage. |
| Public-release artifacts | Release/catalog/proof homes after gates pass. | Publication is governed state, not documentation. |
| Direct UI or Focus Mode data fetches | Governed API and released envelopes only. | Preserves trust membrane. |
| Life-safety alerts or emergency instructions | Official systems and official source guidance. | KFM provides evidence context, not emergency alert authority. |

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Trust flow

```text
SOURCE EDGE -> RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PROOF -> PUBLISHED -> GOVERNED API -> UI / FOCUS
```

```mermaid
flowchart LR
  SD["SourceDescriptor<br/>source_role + knowledge_character<br/>rights + cadence + verification"] --> RAW["RAW<br/>source-native payload<br/>not public"]
  RAW --> WORK["WORK<br/>normalize units/time<br/>preserve traceability"]
  WORK --> GATE{"Boundary gates<br/>role + character + evidence + rights + freshness"}
  GATE -->|missing or unsafe| QUAR["QUARANTINE / HOLD<br/>DENY · ABSTAIN · ERROR"]
  GATE -->|candidate valid| PROC["PROCESSED<br/>validated candidate<br/>not public truth"]
  PROC --> CAT["CATALOG / TRIPLET<br/>catalog + provenance + relation projection"]
  CAT --> EB["EvidenceBundle closure<br/>EvidenceRef resolution"]
  EB --> POL["PolicyDecision<br/>rights + sensitivity + review"]
  POL --> PROMO{"PromotionDecision<br/>release + rollback target"}
  PROMO -->|blocked| QUAR
  PROMO -->|approved| PUB["PUBLISHED<br/>released artifact only"]
  PUB --> API["Governed API<br/>finite envelope"]
  API --> UI["MapLibre shell<br/>Evidence Drawer<br/>Focus Mode"]

  RAW -. "forbidden public bypass" .-> UI
  WORK -. "forbidden public bypass" .-> UI
  PROC -. "unreleased candidate: no public bypass" .-> UI
  QUAR -. "failure state may be summarized, not exposed as raw data" .-> API
```

### Stage obligations

| Stage | Atmosphere / Air obligation |
|---|---|
| `SOURCE EDGE` | Admit source families through descriptor-first review, including `source_role`, `knowledge_character`, rights, cadence, known limitations, and public-release posture. |
| `RAW` | Preserve source-native payloads, retrieval time, and payload hash. Do not expose to public clients. |
| `WORK` | Normalize units and timestamps while preserving raw values and source/site/model context. |
| `QUARANTINE / HOLD` | Hold missing rights, missing role, missing character, malformed unit/time support, source conflict, stale live-state claims, schema failure, or policy failure. |
| `PROCESSED` | Store validated candidates. Do not treat them as released truth. |
| `CATALOG / TRIPLET` | Build discovery, provenance, and relation projections without replacing source evidence. |
| `PROOF` | Resolve EvidenceRefs to EvidenceBundle and assemble validation, policy, catalog, and release-support material. |
| `PUBLISHED` | Release public-safe artifacts only with manifest, rollback target, and correction path. |
| `GOVERNED API` | Return finite envelopes and reason codes. |
| `UI / FOCUS` | Render or answer only from released artifacts or governed envelopes; show trust state, caveats, evidence, policy, freshness, and correction status. |

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Bounded contexts

### 1. Source admission

**Purpose:** decide whether a source may enter the lane and what claims it is competent to support.

| Required input | Required state |
|---|---|
| `source_id` | Stable, unique, deterministic where practical. |
| `source_role` | Observation provider, public reporting provider, regulatory archive, low-cost sensor provider, model provider, remote-sensing provider, advisory issuer, or derived-product generator. |
| `knowledge_character` | Accepted taxonomy value for the object family. |
| Rights and terms | Public release blocked while UNKNOWN or unresolved. |
| Cadence and freshness | Required for live/current-context claims. |
| Known limitations | Must reach Evidence Drawer or public caveat surfaces where material. |

### 2. Connector candidate production

**Current repo-visible slice:** `connectors/pipelines/air/air_ingest.py` writes a deterministic no-network PM2.5 QA candidate and run receipt.

| Output | Meaning | Public posture |
|---|---|---|
| `data/processed/air/qa_summary.example.json` | Processed candidate with `decision: candidate`. | Not public truth. |
| `data/receipts/air/run_receipt.example.json` | Run receipt with `network_access: disabled`. | Process memory only. |

### 3. Normalization

**Purpose:** make candidate records more inspectable without declaring truth or release.

Normalization must preserve:

- raw value and raw unit;
- normalized value and normalized unit;
- source identity and source role;
- knowledge character;
- observation/report/model/retrieval time support;
- source payload hash;
- transform/spec hash where applicable;
- run receipt reference;
- EvidenceRefs;
- candidate / denial / abstention / error state.

### 4. Validation and policy

**Purpose:** fail closed when shape, source role, rights, evidence, policy, freshness, or public-surface rules are not satisfied.

Validation checks structure and traceability. Policy decides admissibility. A schema-valid object may still be denied by rights, sensitivity, source-role, evidence, review, release, stale-state, or rollback gates.

### 5. Catalog, proof, and release

**Purpose:** make publication auditable and reversible.

| Object family | Required distinction |
|---|---|
| Run receipt | Process memory; not proof. |
| EvidenceBundle | Claim-supporting evidence closure. |
| Catalog / STAC / DCAT / PROV | Discovery and provenance; not truth by itself. |
| PromotionDecision | Governed decision; may approve, deny, hold, quarantine, or require review. |
| ReleaseManifest | Released artifact scope, hashes, evidence/proof refs, rollback target, correction path. |
| CorrectionNotice / rollback reference | Required when public meaning changes. |

### 6. Runtime, map, and Focus Mode

**Purpose:** expose released evidence with visible trust state.

| Surface | Required behavior |
|---|---|
| Governed API | Return finite outcome envelopes: `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`. |
| MapLibre shell | Render released layer descriptors only. |
| Evidence Drawer | Show source role, knowledge character, evidence, rights, review, release, freshness, caveats, transform, conflicts, and correction state. |
| Focus Mode | Synthesize only over admissible EvidenceBundle-backed context and citation-validated output. |
| Exports | Include release, evidence, caveat, correction, and rollback references. |

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Knowledge-character taxonomy

Every consequential object must carry or resolve one accepted `knowledge_character`.

| Knowledge character | Boundary | Required handling |
|---|---|---|
| `OBSERVED_SENSOR` | Ground/station/instrument measurement. | Preserve site/instrument/time, raw/normalized units, and source payload hash. |
| `PUBLIC_AQI_REPORT` | AQI, NowCast, public index, or agency report. | Treat as report/index; never raw concentration. |
| `REGULATORY_ARCHIVE` | Quality-assured or regulatory archive evidence. | Use with archive/regulatory temporal caveats; not live by default. |
| `LOW_COST_SENSOR` | Contributor or consumer sensor candidate. | Require correction method, caveats, confidence, rights, and limitations. |
| `ATMOSPHERIC_MODEL_FIELD` | Forecast, reanalysis, hindcast, transport, aerosol, smoke, or chemistry model field. | Label as modeled; expose model identity, uncertainty, and valid time. |
| `REMOTE_SENSING_MASK` | Smoke, AOD, fire, aerosol, haze, cloud, plume, or classification support product. | Treat as context/classification; not surface exposure. |
| `CLIMATE_ANOMALY_CONTEXT` | Normals, anomalies, baselines, downscaling, hindcasts. | Keep contextual; not live emergency alerting. |
| `DERIVED_FUSION` | Interpolation, bias correction, consensus, ensemble, fused grid. | Preserve inputs, method, transform hash, uncertainty, and derived status. |
| `METEOROLOGICAL_CONTEXT` | Wind, temperature, humidity, pressure, boundary-layer and transport support. | Support interpretation; do not become air-quality concentration unless measured as such. |
| `VISIBILITY_AND_AEROSOL_CONTEXT` | Visibility, haze, AOD, opacity, optical aerosol burden. | Do not treat as PM concentration without model assumptions. |
| `FIRE_AND_EMISSIONS_CONTEXT` | Fire hotspots, source indicators, emissions inventory, smoke-source context. | Not exposure measurement by default. |
| `ALERT_AND_ADVISORY_CONTEXT` | Agency notices, public health messages, recommendations. | Preserve issuer and scope; not KFM emergency instruction. |
| `NETWORK_AND_SITE_CONTEXT` | Station metadata, provider IDs, cadence, active/inactive state, siting caveats, instrument health. | Context only; not a measurement value. |
| `BASELINE_AND_TEMPORAL_SUPPORT` | Climatology, rolling baseline, persistence, hysteresis, freshness support. | Supports scoped claims; not standalone proof. |

### Anti-collapse reason codes

| Code | Denial condition |
|---|---|
| `ATMOS_AQI_AS_CONCENTRATION` | AQI/report index is treated as raw concentration. |
| `ATMOS_AOD_AS_PM25` | AOD is treated as PM2.5 without governed model support. |
| `ATMOS_MASK_AS_EXPOSURE` | Smoke/plume/remote mask is treated as exposure measurement. |
| `ATMOS_MODEL_AS_OBSERVED` | Model output is labeled as observed measurement. |
| `ATMOS_FUSION_INPUTS_HIDDEN` | Fusion product hides input EvidenceRefs, method, uncertainty, or transform identity. |
| `ATMOS_UNKNOWN_RIGHTS_PUBLIC` | Public output requested while rights remain unknown. |
| `ATMOS_PUBLIC_INTERNAL_ACCESS` | Public surface attempts internal lifecycle or candidate access. |
| `ATMOS_RECEIPT_AS_PROOF` | Run receipt is used as EvidenceBundle, proof pack, or release manifest. |
| `ATMOS_STALE_CONTEXT_UNLABELED` | Stale or expired operational context appears current. |

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Current no-network slice

The repo-visible implementation pressure is a small, no-network `air` slice. It is useful because it proves candidate/receipt shape pressure without pretending to be a complete Atmosphere / Air release system.

```mermaid
flowchart LR
  SCRIPT["connectors/pipelines/air/air_ingest.py<br/>network_access: disabled"] --> QA["data/processed/air/qa_summary.example.json<br/>decision: candidate"]
  SCRIPT --> RR["data/receipts/air/run_receipt.example.json<br/>status: completed"]
  QA --> VAL["tools/validators/air/validate_air_qa.py<br/>schema + policy checks"]
  RR --> VAL
  POLICY["policy/air/air_qa.rego<br/>threshold + reference gates"] --> VAL
  VAL -->|requires schema inventory| BUILD["tools/publishers/air/build_air_release_candidate.py<br/>catalog/proof/release candidate"]
  BUILD -->|not publication by itself| HOLD["catalog_candidate / quarantine / hold"]
```

| File | CONFIRMED role | Boundary |
|---|---|---|
| [`../../../../connectors/pipelines/air/air_ingest.py`](../../../../connectors/pipelines/air/air_ingest.py) | Writes deterministic PM2.5 QA summary and run receipt. | Candidate writer; no live source activation. |
| [`../../../../data/processed/air/qa_summary.example.json`](../../../../data/processed/air/qa_summary.example.json) | Contains PM2.5 `nowcast_hourly` candidate, metrics, source labels, and refs. | `decision: candidate`; not public truth. |
| [`../../../../data/receipts/air/run_receipt.example.json`](../../../../data/receipts/air/run_receipt.example.json) | Contains run ID, pipeline path, output path, status, and `network_access: disabled`. | Receipt; not evidence closure or release proof. |
| [`../../../../policy/air/air_qa.rego`](../../../../policy/air/air_qa.rego) | Denies threshold exceedance, low coverage, AQS baseline hard-denials, and missing refs. | Policy fragment; not complete domain policy. |
| [`../../../../tools/validators/air/validate_air_qa.py`](../../../../tools/validators/air/validate_air_qa.py) | Runs schema and local policy checks over QA summaries. | References `schemas/contracts/v1/air/qa_summary.schema.json`; schema inventory remains NEEDS VERIFICATION. |
| [`../../../../tools/publishers/air/build_air_release_candidate.py`](../../../../tools/publishers/air/build_air_release_candidate.py) | Builds candidate EvidenceBundle, promotion decision, catalog candidate, triplets, and release manifest. | Requires schema files and proof/release validation; not evidence of public publication. |

> [!CAUTION]
> A completed no-network run does not prove a public air-quality claim. It proves that a candidate and receipt can be emitted. Release still requires schema availability, evidence closure, policy, review, manifest, correction path, rollback target, and captured validation results.

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Validation and policy

### Validation ladder

| Gate | Required evidence | Failure outcome |
|---|---|---|
| Source-role gate | `source_role` or source descriptor reference exists. | `DENY` |
| Knowledge-character gate | Accepted `knowledge_character` exists. | `DENY` |
| Shape gate | Candidate validates against active schema family. | `ERROR` or `DENY` |
| Rights gate | Rights, terms, attribution, and public-release permission are known. | `DENY` |
| Traceability gate | Source payload hash and transform/spec hash exist where applicable. | `DENY` |
| Evidence gate | EvidenceRefs resolve to EvidenceBundle before consequential claims. | `ABSTAIN` or `DENY` |
| Temporal gate | Observation/report/model/retrieval/freshness time is present where material. | `ABSTAIN`, `DENY`, or stale-labeled response |
| Anti-collapse gate | AQI, concentration, AOD, smoke masks, model fields, advisories, and fusion products remain distinct. | `DENY` |
| Public boundary gate | Public surfaces do not read internal lifecycle or candidate artifacts. | `DENY` |
| Receipt/proof split gate | Run receipts are not accepted as proof or release manifests. | `DENY` |
| Release gate | ReleaseManifest has evidence refs, policy decision, review state, correction path, and rollback target. | `DENY` or `HOLD` |

### Current QA policy pressure

The current air QA policy denies:

- `nowcast_max > 35`;
- `nowcast_vs_baseline_sigma > 2`;
- `station_coverage_pct < 75`;
- any hard-denial AQS rows in baseline;
- missing `run_receipt_ref` for candidate public promotion;
- missing `evidence_bundle_ref` for candidate public promotion.

That policy is a useful first gate, but the full lane must also enforce source-role, knowledge-character, rights, evidence closure, freshness, public-surface, release, correction, and rollback rules.

### Schema inventory warning

The current validator and release-candidate builder reference `schemas/contracts/v1/air/*` files. This architecture treats those references as **implementation pressure**, not proof that the schema family is complete or canonical. ADR-0418 must remain the governing compatibility bridge until maintainers verify the active schema inventory and any aliases.

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Public surface contract

| Surface | Must show or enforce | Must not do |
|---|---|---|
| Map layer | Layer type, source role, knowledge character, freshness, release state, caveat badge. | Render raw/work/quarantine/unreleased candidates directly. |
| Popup | What the value is, what it is not, time support, and evidence link. | Present model/mask/report/fusion as observed measurement. |
| Evidence Drawer | Source, role, character, rights, review, release, hashes, transform, freshness, caveats, conflicts, correction state. | Hide uncertainty, method, or disagreement behind polished prose. |
| Focus Mode | Scoped, EvidenceBundle-backed, policy-checked, citation-validated finite outcome. | Direct model chat, uncited claim, raw model output, or policy bypass. |
| Export | Release manifest ref, evidence/caveat refs, correction path, rollback awareness. | Export internal candidates as public truth. |
| API response | `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` with reason/obligation context. | Return ambiguous success or unbounded confidence. |
| Advisory display | Issuer, scope, time basis, official-source context. | KFM emergency instruction or life-safety authority. |

### Runtime finite outcomes

| Outcome | Use when |
|---|---|
| `ANSWER` | EvidenceBundle is resolved, policy allows the scope, source role/character are clear, freshness is adequate, citations validate, and release/public-surface state is satisfied. |
| `ABSTAIN` | Evidence is incomplete, source role is insufficient for the claim, freshness is unclear, or the question exceeds the released evidence scope. |
| `DENY` | Rights, sensitivity, public-surface boundary, exact-location/precision, unknown release permission, internal lifecycle access, or policy rule blocks the action. |
| `ERROR` | Schema, validator, resolver, integrity, manifest, runtime, or tool failure prevents reliable evaluation. |

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Source and parameter registry architecture

The registry architecture should be descriptor-first and fail-closed by default.

### SourceDescriptor minimum fields

| Field | Purpose |
|---|---|
| `source_id` | Stable source identity. |
| `display_name` | Human-readable source name. |
| `source_role` | What the source is competent to support. |
| `knowledge_character` | What kind of knowledge objects it contributes. |
| `publisher` | Responsible publisher or steward. |
| `access_url` / `api_docs_url` | Retrieval and documentation references. |
| `rights_spdx` / `rights_status` | Rights and license posture. |
| `attribution` | Required public attribution. |
| `rate_limit_notes` / `auth_required` | Operational constraints. |
| `freshness_expectation` | Expected update cadence and stale-state handling. |
| `spatial_support` / `temporal_support` | Support scale and time basis. |
| `parameters_supported` | Parameter families. |
| `known_limitations` | Caveats for drawer/runtime display. |
| `public_release_allowed` | Default release posture; false until verified. |
| `default_policy_label` | Suggested policy label. |
| `raw_retention_policy` | Lifecycle retention expectation. |
| `last_verified_at` / `verification_status` | Source verification state. |

### Seed source-family posture

Source families such as OpenAQ, EPA AQS, AirNow, Kansas Mesonet context, CAMS, HRRR-Smoke, HMS smoke, GOES AOD, VIIRS fire, PurpleAir-like networks, advisory feeds, and climate anomaly products may be valuable, but they must enter as `verification_status: UNKNOWN` and `public_release_allowed: false` until rights, terms, schema, cadence, source role, rate limits, freshness, and public-release constraints are verified.

### Parameter rules

- Preserve raw units and normalized units.
- Keep AQI/index values distinct from concentration.
- Keep AOD and visibility/aerosol context distinct from PM concentration.
- Keep model variables distinct from observed sensor parameters.
- Require explicit transform rules for any derived or fused product.
- Show unit, method, and caveat information in Evidence Drawer and API payloads where material.

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Publication, correction, and rollback

Publication is a governed transition from proof-supported candidate to released public-safe artifact.

```mermaid
stateDiagram-v2
  [*] --> Candidate
  Candidate --> Quarantine: schema / rights / evidence / policy failure
  Candidate --> ProofCandidate: validation + evidence refs
  ProofCandidate --> Hold: review or source-role gap
  ProofCandidate --> ReleaseCandidate: policy + catalog + proof closure
  ReleaseCandidate --> Published: PromotionDecision approved
  ReleaseCandidate --> Quarantine: gates fail
  Published --> Corrected: CorrectionNotice
  Published --> Withdrawn: withdrawal decision
  Published --> Superseded: successor release
  Published --> RolledBack: rollback card / alias repoint
  Corrected --> Published: corrected release
  Superseded --> [*]
  Withdrawn --> [*]
  RolledBack --> [*]
```

| Change type | Required artifact behavior |
|---|---|
| Source descriptor change | Revalidate affected candidates, catalog records, layer descriptors, EvidenceBundles, and Focus payloads. |
| Parameter/unit conversion change | Recompute transform hashes, fixtures, normalized values, and downstream released products. |
| Schema slug migration | Follow ADR-0418 with aliases, fixtures, migration notes, validation reports, and rollback. |
| Policy threshold change | Re-run policy fixtures and release-candidate evaluation; record reason-code changes. |
| EvidenceBundle correction | Emit CorrectionNotice or supersession record; mark derived products stale until revalidated. |
| Public layer withdrawal | Keep old release discoverable; update current alias only through governed rollback/correction path. |
| Live-source activation | Require source descriptor verification, rights review, fixtures, rate-limit handling, and no-public-release dryrun first. |

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Definition of done

This architecture should not be treated as enforcement-ready until the following are satisfied.

### Documentation readiness

- [ ] KFM Meta Block values are verified or intentionally left as visible placeholders.
- [ ] Owners are verified through CODEOWNERS or maintainer routing.
- [ ] This file is linked from `../README.md` and any domain file index.
- [ ] ADR-0312, ADR-0418, and ADR-0431 relationships remain synchronized.
- [ ] No duplicate architecture authority is introduced under a parallel domain or ADR path.

### Implementation readiness

- [ ] Active schema home for `air` and/or `atmosphere` is inventoried and recorded.
- [ ] Referenced schema files exist or the validator/publisher defaults are updated.
- [ ] Valid and invalid fixtures cover observed sensor, AQI report, regulatory archive, low-cost sensor, model field, remote mask, fusion product, stale context, unknown rights, missing evidence, and internal public access.
- [ ] Validators fail closed with stable reason codes.
- [ ] Policy gates cover thresholds, source role, knowledge character, rights, freshness, evidence closure, public lifecycle boundaries, release, correction, and rollback.
- [ ] No-network connector output remains candidate-only.
- [ ] Run receipts remain process memory.
- [ ] Release-candidate builder outputs are validated without implying public release.
- [ ] CI/workflow evidence is captured before claiming merge-blocking enforcement.
- [ ] Public UI/API/Focus consumes only released artifacts or governed envelopes.
- [ ] Rollback drill proves old release refs remain resolvable and current aliases update through governed receipts.

### Release readiness

- [ ] Source rights and terms are verified for each source family.
- [ ] EvidenceRefs resolve to EvidenceBundle.
- [ ] Catalog/proof/release objects close.
- [ ] Review state is recorded.
- [ ] ReleaseManifest includes hashes, artifact refs, policy decision, correction path, and rollback target.
- [ ] Evidence Drawer and Focus payloads expose source role, knowledge character, freshness, caveats, and conflicts.
- [ ] Public artifacts do not reference internal lifecycle paths.

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Open verification backlog

| Item | Status | Why it matters |
|---|---:|---|
| `doc_id`, owners, created date, final policy label | NEEDS VERIFICATION | Required before publishing this architecture as stable. |
| Local mounted checkout | UNKNOWN in authoring workspace | GitHub connector verified repo files; local repo commands could not be run against a mounted checkout. |
| Schema family inventory | NEEDS VERIFICATION | Validator and publisher reference `schemas/contracts/v1/air/*`; active canonical schema path remains governed by ADR-0418. |
| `schemas/contracts/v1/air/qa_summary.schema.json` | NEEDS VERIFICATION | Referenced by current validator; not confirmed in this authoring pass. |
| Complete air/atmosphere test status | UNKNOWN | File presence does not prove tests pass or CI enforces gates. |
| Policy engine and Conftest/OPA runtime | NEEDS VERIFICATION | Rego file exists; enforcement maturity and workflow use are not proven here. |
| EvidenceBundle example closure | NEEDS VERIFICATION | QA summary references `data/processed/air/evidence_bundle.example.json`; release use requires proof closure. |
| Release-candidate schema files | NEEDS VERIFICATION | Publisher validates multiple `schemas/contracts/v1/air/*` files; inventory and run results must be checked. |
| Live source descriptors | UNKNOWN / PROPOSED | Source families must remain `public_release_allowed=false` until rights and terms are verified. |
| MapLibre / Evidence Drawer / Focus integration | UNKNOWN | Architecture defines payload obligations; runtime integration must be proven by app code/tests. |
| Public release state | UNKNOWN | No public Atmosphere / Air release should be claimed without ReleaseManifest, proof, review, correction, and rollback evidence. |
| Slug migration from `air` to `atmosphere` | PROPOSED / NEEDS VERIFICATION | Requires ADR-0418 acceptance, alias registry, fixtures, validators, migration notes, and rollback path. |

<p align="right"><a href="#top">Back to top ↑</a></p>

---

<details>
<summary><strong>Pre-publish checklist for this file</strong></summary>

- [x] KFM Meta Block V2 present.
- [x] One H1 only.
- [x] Purpose line directly below title.
- [x] Status and trust posture visible.
- [x] Repo fit and owning root stated.
- [x] Directory Rules responsibility-root posture preserved.
- [x] Source-role and knowledge-character boundaries explicit.
- [x] Current repo-visible implementation slice separated from release claims.
- [x] Mermaid diagrams are meaningful and grounded.
- [x] Tables clarify architecture, gates, objects, and rollback.
- [x] Code fences are language-tagged.
- [x] Unknowns and placeholders are explicit.
- [x] Public RAW/WORK/QUARANTINE/candidate/direct-model access denied.
- [x] AI/Focus Mode kept evidence-subordinate.
- [ ] Owners, policy label, schema inventory, CI enforcement, runtime integration, and release proof verified by maintainers before promotion.

</details>

<p align="right"><a href="#top">Back to top ↑</a></p>
