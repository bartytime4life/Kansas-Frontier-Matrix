<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://adr/ADR-0312-atmosphere-air-source-role-boundaries
title: ADR-0312: Atmosphere/Air Source-Role and Knowledge-Character Boundaries
type: architecture-decision-record
version: v1.0-draft
status: draft
owners: @bartytime4life; atmosphere-air-domain-steward NEEDS_VERIFICATION; policy-steward NEEDS_VERIFICATION
created: NEEDS_VERIFICATION-YYYY-MM-DD
updated: 2026-05-06
policy_label: public-draft-NEEDS_VERIFICATION
related: [./README.md, ./ADR-TEMPLATE.md, ./ADR-0001-schema-home.md, ../domains/atmosphere_air/README.md, ../domains/atmosphere_air/ADR-0003-atmosphere-source-role-boundaries.md, ../architecture/contract-schema-policy-split.md, ../../policy/crosswalk/domain-lane-policy-map.md, ../../connectors/pipelines/air/README.md, ../../connectors/pipelines/air/air_ingest.py, ../../pipelines/normalize/domains/atmosphere/README.md, ../../data/processed/air/qa_summary.example.json, ../../data/receipts/air/run_receipt.example.json]
tags: [kfm, adr, atmosphere-air, source-role, knowledge-character, air-quality, evidence, policy, no-network, fail-closed]
notes: [
  Existing repo-visible ADR revised in place for docs/adr/ADR-0312-atmosphere-air-source-role-boundaries.md.
  Expands the domain-local docs/domains/atmosphere_air/ADR-0003-atmosphere-source-role-boundaries.md decision without deleting lineage.
  Current implementation evidence confirms a no-network air connector, candidate QA summary, and run receipt; it does not confirm full schema, policy, CI, release, EvidenceBundle, or runtime enforcement.
  ADR meta-block type convention remains NEEDS_VERIFICATION because adjacent ADR files use mixed standard and ADR-specific type values.
  Owners, creation date, final policy label, source-rights posture, schema-home acceptance, executable policy, CI enforcement, release behavior, and rollback proof remain NEEDS_VERIFICATION.
]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ADR-0312: Atmosphere/Air Source-Role and Knowledge-Character Boundaries

Atmosphere and air-quality claims must preserve source role, knowledge character, temporal support, evidence closure, policy posture, and release state before they can be mapped, summarized, published, exported, or answered by Focus Mode.

<p align="center">
  <img alt="ADR status: draft proposed" src="https://img.shields.io/badge/ADR-draft%20%7C%20proposed-f59f00">
  <img alt="domain: atmosphere air" src="https://img.shields.io/badge/domain-atmosphere%20%2F%20air-6f42c1">
  <img alt="source role: required" src="https://img.shields.io/badge/source_role-required-2ea44f">
  <img alt="knowledge character: required" src="https://img.shields.io/badge/knowledge_character-required-0a7ea4">
  <img alt="policy posture: fail closed" src="https://img.shields.io/badge/policy-fail--closed-b60205">
  <img alt="publication: not authorized" src="https://img.shields.io/badge/publication-not_authorized-lightgrey">
</p>

<p align="center">
  <a href="#decision">Decision</a> ·
  <a href="#evidence-boundary">Evidence</a> ·
  <a href="#repo-fit">Repo fit</a> ·
  <a href="#boundary-taxonomy">Taxonomy</a> ·
  <a href="#anti-collapse-rules">Anti-collapse</a> ·
  <a href="#governed-flow">Flow</a> ·
  <a href="#enforcement-model">Enforcement</a> ·
  <a href="#acceptance-criteria">Acceptance</a> ·
  <a href="#rollback-and-supersession">Rollback</a>
</p>

> [!IMPORTANT]
> **Target path:** `docs/adr/ADR-0312-atmosphere-air-source-role-boundaries.md`  
> **Status:** `draft` / `proposed`  
> **Lineage:** expands `docs/domains/atmosphere_air/ADR-0003-atmosphere-source-role-boundaries.md` without deleting that domain-local decision.
>
> This ADR does **not** authorize live source fetching, public release, public map layers, Evidence Drawer claims, Focus Mode answers, or publication. It defines the source-role and knowledge-character boundary those later systems must preserve.

> [!CAUTION]
> AQI, PM2.5 concentration, AOD, smoke masks, model fields, climate anomalies, fusion products, advisories, run receipts, and no-network fixtures are not interchangeable.
>
> If KFM cannot prove the distinction, the system should `ABSTAIN`, `DENY`, `ERROR`, `HOLD`, or quarantine rather than flatten uncertainty into a polished map.

---

## Decision

KFM will treat **source role** and **knowledge character** as mandatory trust-bearing fields for the Atmosphere/Air lane.

This requirement applies to:

- source descriptors and source registries;
- connector candidates;
- normalization candidates;
- no-network fixtures;
- policy decisions and reason codes;
- EvidenceBundle closure;
- catalog, proof, and release review;
- public layer descriptors;
- governed API envelopes;
- MapLibre popups and Evidence Drawer payloads;
- Focus Mode request and response envelopes;
- correction and rollback records.

### Decision summary

| Field | Determination |
|---|---|
| ADR status | `draft` / `proposed` |
| Target file | `docs/adr/ADR-0312-atmosphere-air-source-role-boundaries.md` |
| Domain lane | Atmosphere / Air |
| Primary boundary | Source role + knowledge character separation |
| Lineage source | `docs/domains/atmosphere_air/ADR-0003-atmosphere-source-role-boundaries.md` |
| Public release effect | No public release authorized by this ADR |
| Confirmed current implementation surface | No-network air connector, candidate QA summary, and run receipt are repo-visible |
| Enforcement maturity | NEEDS VERIFICATION for schemas, validators, policy, CI, proof closure, release, and runtime behavior |
| Primary risk addressed | False certainty caused by collapsing observations, reports, models, masks, fusion products, advisories, receipts, and metadata |
| Default failure posture | `DENY` for unsafe exposure, `ABSTAIN` for insufficient evidence, `ERROR` for technical failure, `HOLD` for promotion gaps |

### Expansion from ADR-0003

| Prior decision element | ADR-0312 expansion |
|---|---|
| Enforce strict source-role separation. | Every consequential atmosphere/air object must carry a source role or resolve to a `SourceDescriptor` that does. |
| Preserve observed vs report vs model vs mask vs fusion boundaries. | Every consequential object must carry a `knowledge_character` from the accepted lane taxonomy or fail closed. |
| Apply across API, layer, and evidence surfaces. | Apply from source admission through normalization, policy decisions, release manifests, governed API envelopes, MapLibre layers, Evidence Drawer payloads, and Focus Mode responses. |
| Reduce semantic drift and false certainty. | Reject anti-collapse cases such as AQI-as-concentration, AOD-as-PM2.5, smoke-mask-as-exposure, model-as-observation, and fusion-as-canonical-source. |
| Add validator burden. | Require positive and negative fixtures, reason-coded denials, compatibility tests, and acceptance evidence before enforcement can be claimed. |

### Normative rules after acceptance

1. **Source role is required.** A record that supports a claim must identify the source’s role or resolve to a source descriptor that does.
2. **Knowledge character is required.** A record must state whether it is an observation, public report, regulatory archive, low-cost sensor record, model field, remote-sensing mask, anomaly context, fusion product, advisory context, site context, or temporal support object.
3. **Descriptors are not claim evidence by themselves.** A `SourceDescriptor` admits and constrains a source; public claims still require EvidenceBundle closure and release state.
4. **Run receipts are not release proof.** A connector or normalization run can be process memory, but it does not authorize publication.
5. **No direct public path.** Public UI, public API, map layers, Focus Mode, exports, and search must not read RAW, WORK, QUARANTINE, connector-private, normalize-stage, or unpublished candidate artifacts directly.
6. **Derived products stay derived.** Fusion, interpolation, NowCast-like candidates, masks, modeled fields, and layer products must expose input evidence, method, uncertainty, transform identity, and release state.
7. **Unknown rights block public release.** Unknown source rights, source terms, cadence, or public-release permission result in `DENY` for public release.
8. **Freshness must be explicit.** Current-state or live-context claims require retrieval time, valid time, observation/model time basis, and freshness posture.
9. **Focus Mode remains evidence-subordinate.** Focus Mode may synthesize only over admissible, policy-safe, EvidenceBundle-backed context and must return `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR`.
10. **Ambiguity fails closed.** If a validator, API, UI, or reviewer cannot determine the source role or knowledge character, the claim does not move toward publication.

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Evidence boundary

This ADR separates repo-visible evidence from proposed enforcement.

| Evidence | Status | Supports | Limits |
|---|---:|---|---|
| `docs/adr/ADR-0312-atmosphere-air-source-role-boundaries.md` | CONFIRMED existing repo file | This ADR target already exists and is the file being revised. | Existing file content does not prove validators, CI, runtime, release, or policy enforcement. |
| `docs/adr/README.md` | CONFIRMED existing repo file | ADRs are the human-facing decision ledger; the index distinguishes decision state from enforcement state. | ADR inventory, owners, and enforcement remain partly NEEDS VERIFICATION. |
| `docs/adr/ADR-TEMPLATE.md` | CONFIRMED existing repo file | KFM ADRs should carry evidence, scope, validation, rollback, and supersession. | Template conventions do not prove this ADR is accepted or enforced. |
| `docs/adr/ADR-0001-schema-home.md` | CONFIRMED existing repo file / PROPOSED decision | `schemas/contracts/v1/` is proposed as the canonical machine-schema home; `contracts/` defines meaning; `policy/` decides admissibility. | ADR-0001 remains draft/proposed and its acceptance/enforcement are not proven here. |
| `docs/domains/atmosphere_air/ADR-0003-atmosphere-source-role-boundaries.md` | CONFIRMED existing repo file | Domain-local prior decision: strict source-role separation across observed/report/model/mask/fusion. | Thin ADR does not define the full taxonomy, gates, evidence plan, or acceptance criteria. |
| `docs/domains/atmosphere_air/README.md` | CONFIRMED existing repo file | Atmosphere/Air lane scope, accepted inputs, exclusions, knowledge-character taxonomy, and public-safety posture. | Owners, policy label, schema home, tooling, and implementation remain partly NEEDS VERIFICATION. |
| `connectors/pipelines/air/README.md` | CONFIRMED existing repo file | No-network connector lane produces reviewable QA-summary candidates and run receipts, not public truth. | Does not claim live source activation, public release, CI enforcement, or complete proof closure. |
| `connectors/pipelines/air/air_ingest.py` | CONFIRMED existing repo file | Emits deterministic no-network PM2.5 QA summary and run receipt. | Script output is candidate/process memory, not EvidenceBundle or release proof. |
| `data/processed/air/qa_summary.example.json` | CONFIRMED existing repo file | Example candidate has `decision: candidate`, `source.dataset: no_network_stub`, PM2.5 aggregation, units, time window, and evidence/receipt refs. | Referenced EvidenceBundle closure is not proven here. |
| `data/receipts/air/run_receipt.example.json` | CONFIRMED existing repo file | Example receipt records `network_access: disabled`, output path, pipeline path, run ID, and completed status. | Receipt is not release proof. |
| `pipelines/normalize/domains/atmosphere/README.md` | CONFIRMED existing repo file | Normalization must preserve source role, knowledge character, raw/normalized values and units, time support, EvidenceRefs, receipt linkage, candidate status, and reason-coded failures. | Does not prove a normalizer script, schema gate, policy gate, CI workflow, or public release. |
| `docs/architecture/contract-schema-policy-split.md` | CONFIRMED existing repo file | Contracts explain meaning, schemas validate shape, policy decides release/public behavior. | Explanatory architecture doc is not enforcement proof. |
| `policy/crosswalk/domain-lane-policy-map.md` | CONFIRMED existing repo file | Atmosphere/Air/Climate/EO lane is contextual by default and must label observed/model/anomaly/fusion/remote-sensing character and freshness. | Crosswalk is not a policy engine. |
| Directory Rules | CONFIRMED project doctrine | ADRs belong under `docs/adr/`; domain materials belong under responsibility roots rather than root-level domain folders. | Does not prove branch-local enforcement. |
| Atmosphere/Air architecture report and KFM component passes | LINEAGE / CORPUS-CONFIRMED doctrine | Strong source-role and knowledge-character pressure for air, climate, HLS, smoke, modeled fields, and anomalies. | Prior reports do not prove current repo implementation unless current repo files are inspected. |

### Truth labels used here

| Label | Meaning |
|---|---|
| `CONFIRMED` | Verified from current repository evidence, surfaced project docs, or current workspace/retrieval evidence. |
| `PROPOSED` | Recommended decision or implementation not proven by current tests, workflows, logs, proof objects, or release artifacts. |
| `NEEDS VERIFICATION` | A specific check can retire the uncertainty. |
| `UNKNOWN` | Not verified strongly enough in this session. |
| `LINEAGE` | Prior project artifact that informs continuity but does not prove current behavior. |
| `DENY` / `ABSTAIN` / `ERROR` / `HOLD` | System or gate outcomes, not rhetorical emphasis. |

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Repo fit

### Path decision

| Path | Status | Decision |
|---|---:|---|
| `docs/adr/ADR-0312-atmosphere-air-source-role-boundaries.md` | CONFIRMED existing target path | Revise this file as the repo-wide ADR for Atmosphere/Air source-role and knowledge-character boundaries. |
| `docs/domains/atmosphere_air/ADR-0003-atmosphere-source-role-boundaries.md` | CONFIRMED existing lineage file | Preserve as domain-local lineage and link to ADR-0312 as the expanded governing decision after review. |
| `docs/domains/ADR/ADR-0003-atmosphere-source-role-boundaries.md` | NEEDS VERIFICATION / not selected | Do not create a parallel `docs/domains/ADR/` home without an ADR and migration note. |
| `docs/domains/atmosphere/ADR-0003-atmosphere-source-role-boundaries.md` | LINEAGE / prior report path family | Do not assume this path exists or is canonical unless repo evidence confirms it. |

### Directory-rule rationale

`docs/adr/` is the human-facing decision ledger. The Atmosphere/Air lane remains under `docs/domains/atmosphere_air/`. Connector execution remains under `connectors/pipelines/air/`. Normalization guidance remains under `pipelines/normalize/domains/atmosphere/`.

This split preserves responsibility roots:

| Root | Role in this ADR |
|---|---|
| `docs/adr/` | Architecture decision and supersession record. |
| `docs/domains/atmosphere_air/` | Domain scope, knowledge-character definitions, and lane-specific guidance. |
| `connectors/pipelines/air/` | Source-facing no-network connector candidate lane. |
| `pipelines/normalize/domains/atmosphere/` | Execution-near normalization guidance. |
| `schemas/contracts/v1/` | Proposed machine-shape authority after ADR-0001 acceptance. |
| `contracts/` | Semantic meaning surface. |
| `policy/` | Admissibility, release, and runtime decision surface. |
| `data/processed/`, `data/receipts/`, `data/proofs/`, `release/` | Lifecycle, process memory, proof, and release artifacts when present and verified. |

> [!WARNING]
> Do not keep duplicate governing ADR copies under multiple ADR-like homes. If the domain-local ADR remains, link it as lineage and make ADR-0312 the successor only after review.

### Naming compatibility note

Current repo-visible surfaces use three slugs:

| Slug | Confirmed use | Working interpretation |
|---|---|---|
| `atmosphere_air` | `docs/domains/atmosphere_air/` | Domain documentation slug. |
| `air` | `connectors/pipelines/air/`, `data/processed/air/`, `data/receipts/air/` | Connector and current no-network artifact slug. |
| `atmosphere` | `pipelines/normalize/domains/atmosphere/` | Normalization-domain execution slug. |

This ADR does **not** rename those surfaces. It records the compatibility pressure and requires any future rename or consolidation to preserve lineage, update links, add tests, and document rollback.

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Scope and non-goals

### In scope

This ADR governs source-role and knowledge-character separation for:

- source descriptors and source registries;
- atmosphere/air connector candidates;
- normalization candidates;
- no-network fixtures;
- valid and invalid fixtures;
- schema expectations;
- policy decisions and reason codes;
- EvidenceBundle closure;
- catalog, proof, and release handoff;
- public layer descriptors;
- MapLibre popups and Evidence Drawer payloads;
- Focus Mode payloads and runtime envelopes;
- correction and rollback records.

### Out of scope

This ADR does **not**:

- authorize live AirNow, AQS, OpenAQ, PurpleAir, Mesonet, model, smoke, satellite, or advisory connectors;
- define final source descriptors;
- define final JSON Schemas;
- define final Rego/OPA policy;
- approve public release of any air-quality artifact;
- claim CI enforces the rules;
- prove the referenced EvidenceBundle file exists;
- define emergency or life-safety alerting behavior;
- replace the Atmosphere/Air README, connector README, normalization README, policy crosswalk, or contract/schema/policy split document.

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Boundary taxonomy

Every consequential atmosphere/air object must carry `knowledge_character` or resolve to a source descriptor that supplies it.

| Knowledge character | Boundary | Must never masquerade as |
|---|---|---|
| `OBSERVED_SENSOR` | Measured station or ground observation with site/instrument context. | AQI report, model field, interpolation, remote mask, or fusion product. |
| `PUBLIC_AQI_REPORT` | AQI, NowCast, public index, or agency report. | Raw concentration measurement. |
| `REGULATORY_ARCHIVE` | Quality-assured or regulatory archive evidence. | Live operational state by default. |
| `LOW_COST_SENSOR` | Contributor or consumer sensor network requiring correction, caveat, rights, and confidence handling. | Regulatory truth or unrestricted public observation. |
| `ATMOSPHERIC_MODEL_FIELD` | Forecast, reanalysis, hindcast, transport, chemistry, aerosol, or smoke model field. | Observed measurement. |
| `REMOTE_SENSING_MASK` | Smoke, AOD, fire, aerosol, haze, cloud, or plume classification/support product. | Surface exposure measurement. |
| `CLIMATE_ANOMALY_CONTEXT` | Normals, anomalies, hindcasts, downscaling, or baseline context. | Emergency alert or live hazard state. |
| `DERIVED_FUSION` | Interpolation, consensus, bias correction, ensemble, or fused product. | Canonical source observation. |
| `METEOROLOGICAL_CONTEXT` | Wind, temperature, humidity, pressure, boundary-layer, and transport support. | Air-quality concentration unless measured as such. |
| `VISIBILITY_AND_AEROSOL_CONTEXT` | Visibility, haze, AOD, opacity, aerosol optical burden. | PM concentration without model assumptions. |
| `FIRE_AND_EMISSIONS_CONTEXT` | Fire hotspots, source indicators, inventories, smoke-source context. | Exposure measurement. |
| `ALERT_AND_ADVISORY_CONTEXT` | Agency notices, public health messages, public recommendations. | Observation, model, or KFM life-safety instruction. |
| `NETWORK_AND_SITE_CONTEXT` | Station metadata, provider IDs, cadence, active/inactive state, siting caveats, instrument health. | Measurement value. |
| `BASELINE_AND_TEMPORAL_SUPPORT` | Climatology, rolling baseline, persistence window, hysteresis, freshness support. | Standalone claim without scoped target. |

### Required companion fields

A consequential atmosphere/air object should include or resolve:

| Field | Purpose |
|---|---|
| `source_id` or source descriptor ref | Links the object to source identity, role, rights, and review state. |
| `source_role` | States what the source is competent to support. |
| `knowledge_character` | States what kind of knowledge the object represents. |
| `raw_value` / `raw_unit` | Preserves source-native measurement or report value where applicable. |
| `normalized_value` / `normalized_unit` | Enables comparison without losing raw value. |
| `observed_time`, `valid_time`, `retrieved_at`, or equivalent | Keeps temporal support explicit. |
| `freshness_status` | Prevents stale material from appearing current. |
| `source_payload_hash` | Preserves source traceability. |
| `transform_hash` or `spec_hash` | Preserves transform identity for derivatives. |
| `evidence_refs` | Enables EvidenceBundle closure. |
| `public_release_allowed` | Blocks public exposure until rights/review allow it. |
| `decision` | Keeps finite posture visible: `candidate`, `ANSWER`, `ABSTAIN`, `DENY`, `ERROR`, or release-specific equivalent. |

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Anti-collapse rules

These rules are the core of ADR-0312.

| Rule ID | Anti-collapse rule | Required failure behavior |
|---|---|---|
| `ATMOS-R001` | AQI or NowCast-style public report must not be treated as raw concentration. | `DENY` with `ATMOS_AQI_AS_CONCENTRATION`. |
| `ATMOS-R002` | AOD must not be treated as PM2.5 without a governed model, assumptions, and evidence. | `DENY` with `ATMOS_AOD_AS_PM25`. |
| `ATMOS-R003` | Smoke/plume/fire mask must not be treated as exposure measurement. | `DENY` or `ABSTAIN` unless model/fusion evidence supports the claim. |
| `ATMOS-R004` | Forecast, reanalysis, transport, smoke, or chemistry model field must not be labeled as observed measurement. | `DENY` with `ATMOS_MODEL_AS_OBSERVED`. |
| `ATMOS-R005` | Regulatory archive must not imply live current state unless the temporal scope supports it. | `ABSTAIN` or stale-context response. |
| `ATMOS-R006` | Low-cost sensor data must not be promoted without correction method, caveats, rights, and confidence support. | `DENY` with low-cost/correction reason code. |
| `ATMOS-R007` | Fusion product must not hide input evidence, method, uncertainty, or transform identity. | `DENY` with missing evidence/transform reason code. |
| `ATMOS-R008` | Advisory context must not become KFM emergency instruction. | `DENY` life-safety framing; route users to official sources. |
| `ATMOS-R009` | Site metadata must not be presented as measurement value. | `DENY` or `ERROR` depending on request shape. |
| `ATMOS-R010` | No-network fixture or stub output must not become public truth. | `DENY` public release until proof/release closure exists. |
| `ATMOS-R011` | Run receipt must not become EvidenceBundle or ReleaseManifest. | `DENY` proof substitution. |
| `ATMOS-R012` | Public clients must not read connector, normalize, RAW, WORK, QUARANTINE, or unpublished candidate artifacts directly. | `DENY` with `ATMOS_PUBLIC_INTERNAL_ACCESS`. |

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Current repo pressure

The current no-network air connector creates useful implementation pressure for this ADR without proving full enforcement.

### Confirmed candidate shape

| Field family | Current value or behavior |
|---|---|
| Parameter | `pm25` |
| Units | `ug_m3` |
| Averaging window | `nowcast_hourly` |
| Source provider | `kfm_air_pipeline` |
| Source dataset | `no_network_stub` |
| Decision | `candidate` |
| Evidence bundle ref | `data/processed/air/evidence_bundle.example.json` |
| Run receipt ref | `data/receipts/air/run_receipt.example.json` |
| Time window | `2026-05-01T00:00:00Z` to `2026-05-01T01:00:00Z` |

### Confirmed receipt shape

| Receipt field | Current value or behavior |
|---|---|
| Pipeline | `connectors/pipelines/air/air_ingest.py` |
| Network access | `disabled` |
| Output | `data/processed/air/qa_summary.example.json` |
| Status | `completed` |
| Run ID | `air-ingest-no-network-2026-05-01T01:00:00Z` |

### Decision pressure

| Current artifact | ADR-0312 requires |
|---|---|
| `decision: candidate` | Keep candidate posture until downstream gates pass. |
| `source.dataset: no_network_stub` | Do not treat as real-world public evidence. |
| `network_access: disabled` | Preserve no-network fixture discipline for early proof slices. |
| `evidence_bundle_ref` path | Verify the referenced bundle exists and is valid before any claim relies on it. |
| PM2.5 + NowCast-like metadata | Preserve PM2.5 concentration, AQI/report, and NowCast/report distinctions. |
| Run receipt | Keep receipt separate from proof, release, and publication state. |

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Governed flow

```mermaid
flowchart LR
  SD["SourceDescriptor<br/>source_role + rights + review"] --> RAW["RAW / candidate source payload<br/>not public"]
  RAW --> NORM["Normalize<br/>preserve raw unit, normalized unit,<br/>knowledge_character, time, hashes"]
  NORM --> GATE{"Boundary gates<br/>role + character + evidence + policy"}
  GATE -->|missing or unsafe| HOLD["ABSTAIN / DENY / ERROR<br/>or QUARANTINE"]
  GATE -->|candidate valid| PROC["PROCESSED candidate<br/>not public"]
  PROC --> CAT["CATALOG / TRIPLET candidate"]
  CAT --> EB["EvidenceBundle closure"]
  EB --> POL["PolicyDecision<br/>rights + sensitivity + review"]
  POL --> REL{"PromotionDecision<br/>release + rollback target"}
  REL -->|approved| PUB["PUBLISHED released artifact"]
  REL -->|blocked| HOLD
  PUB --> API["Governed API<br/>finite envelope"]
  API --> UI["MapLibre shell<br/>Evidence Drawer<br/>Focus Mode"]

  NORM -. "no direct public access" .-> UI
  RAW -. "no direct public access" .-> UI
  HOLD -. "visible failure state" .-> API
```

### Flow rules

1. A source descriptor can admit and constrain source identity, but it cannot support a public claim by itself.
2. Normalization must make source role, knowledge character, unit, time, and traceability clearer; it must not publish.
3. EvidenceBundle closure is required before consequential public claims.
4. Policy decides release/public behavior; schema validity alone is not enough.
5. The public map shell consumes governed API envelopes and released artifacts only.

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Enforcement model

### Required validation gates

| Gate | Required behavior | Failure outcome |
|---|---|---|
| Source role gate | Every consequential object has `source_role` or source descriptor ref. | `DENY` / `ATMOS_MISSING_SOURCE_ROLE` |
| Knowledge-character gate | Every consequential object has an accepted `knowledge_character`. | `DENY` / `ATMOS_MISSING_KNOWLEDGE_CHARACTER` |
| Rights gate | Unknown rights or terms block public release. | `DENY` / `ATMOS_UNKNOWN_RIGHTS_PUBLIC` |
| Traceability gate | Source payload hash and transform hash are present where applicable. | `DENY` / missing hash reason |
| Evidence gate | Public claims resolve EvidenceRefs to EvidenceBundle. | `ABSTAIN` or `DENY` |
| Temporal gate | Observation/model/report/retrieval/freshness times are present where material. | `ABSTAIN`, `DENY`, or stale context |
| Anti-collapse gate | AQI, concentration, AOD, smoke mask, model, fusion, and advisory roles stay distinct. | `DENY` with rule-specific reason |
| Public boundary gate | No public client reads RAW/WORK/QUARANTINE/connector/normalize candidates directly. | `DENY` / `ATMOS_PUBLIC_INTERNAL_ACCESS` |
| Receipt/proof split gate | Run receipts are not accepted as proof or release manifests. | `DENY` / `ATMOS_RECEIPT_AS_PROOF` |
| Focus Mode gate | AI responses cite admissible EvidenceBundle-backed support or abstain. | `ABSTAIN`, `DENY`, or `ERROR` |

### Suggested denial codes

| Code | Condition |
|---|---|
| `ATMOS_MISSING_KNOWLEDGE_CHARACTER` | Object lacks `knowledge_character`. |
| `ATMOS_MISSING_SOURCE_ROLE` | Object lacks source role or source descriptor ref. |
| `ATMOS_MISSING_RIGHTS` | Source rights or terms are missing. |
| `ATMOS_UNKNOWN_RIGHTS_PUBLIC` | Public output requested while rights are unknown. |
| `ATMOS_MISSING_EVIDENCE_REFS` | Consequential claim lacks EvidenceRefs. |
| `ATMOS_MISSING_SOURCE_PAYLOAD_HASH` | Normalized record cannot be traced to source payload. |
| `ATMOS_MISSING_TRANSFORM_HASH` | Derived record lacks transform identity. |
| `ATMOS_PUBLIC_RELEASE_FALSE` | Source descriptor or release gate blocks public release. |
| `ATMOS_LOW_COST_NO_CORRECTION` | Low-cost sensor lacks correction/caveat support. |
| `ATMOS_MODEL_AS_OBSERVED` | Model output is labeled as observed measurement. |
| `ATMOS_AQI_AS_CONCENTRATION` | AQI/report index is treated as raw concentration. |
| `ATMOS_AOD_AS_PM25` | AOD is treated as PM2.5 without governed model support. |
| `ATMOS_MASK_AS_EXPOSURE` | Remote-sensing/smoke mask is treated as exposure measurement. |
| `ATMOS_FUSION_INPUTS_HIDDEN` | Fusion product omits input EvidenceRefs or method. |
| `ATMOS_ANOMALY_AS_ALERT` | Climate anomaly is promoted as emergency alert. |
| `ATMOS_PUBLIC_INTERNAL_ACCESS` | Public surface attempts internal lifecycle or candidate access. |
| `ATMOS_RECEIPT_AS_PROOF` | Run receipt is used as EvidenceBundle or ReleaseManifest. |
| `ATMOS_STALE_CONTEXT_UNLABELED` | Stale/expired operational context lacks visible stale posture. |

### Schema-valid is not release-ready

```text
schema-valid
≠ evidence-resolved
≠ rights-cleared
≠ source-role-admissible
≠ freshness-current
≠ policy-allowed
≠ reviewed
≠ released
≠ correction-ready
```

### Illustrative validator sketch

```python
# Illustrative only — adapt to the repo's actual validator framework before implementation.
# Purpose: enforce atmosphere/air source-role and knowledge-character anti-collapse rules.

ALLOWED_KNOWLEDGE_CHARACTERS = {
    "OBSERVED_SENSOR",
    "PUBLIC_AQI_REPORT",
    "REGULATORY_ARCHIVE",
    "LOW_COST_SENSOR",
    "ATMOSPHERIC_MODEL_FIELD",
    "REMOTE_SENSING_MASK",
    "CLIMATE_ANOMALY_CONTEXT",
    "DERIVED_FUSION",
    "METEOROLOGICAL_CONTEXT",
    "VISIBILITY_AND_AEROSOL_CONTEXT",
    "FIRE_AND_EMISSIONS_CONTEXT",
    "ALERT_AND_ADVISORY_CONTEXT",
    "NETWORK_AND_SITE_CONTEXT",
    "BASELINE_AND_TEMPORAL_SUPPORT",
}

def validate_atmosphere_boundary(record: dict) -> list[str]:
    failures: list[str] = []

    source_role = record.get("source_role") or record.get("source_descriptor_ref")
    knowledge_character = record.get("knowledge_character")

    if not source_role:
        failures.append("ATMOS_MISSING_SOURCE_ROLE")

    if knowledge_character not in ALLOWED_KNOWLEDGE_CHARACTERS:
        failures.append("ATMOS_MISSING_KNOWLEDGE_CHARACTER")

    if knowledge_character == "PUBLIC_AQI_REPORT" and record.get("claims_raw_concentration"):
        failures.append("ATMOS_AQI_AS_CONCENTRATION")

    if (
        knowledge_character == "VISIBILITY_AND_AEROSOL_CONTEXT"
        and record.get("claims_pm25")
        and not record.get("model_assumptions_ref")
    ):
        failures.append("ATMOS_AOD_AS_PM25")

    if knowledge_character == "REMOTE_SENSING_MASK" and record.get("claims_exposure_measurement"):
        failures.append("ATMOS_MASK_AS_EXPOSURE")

    if knowledge_character == "ATMOSPHERIC_MODEL_FIELD" and record.get("observation_type") == "observed":
        failures.append("ATMOS_MODEL_AS_OBSERVED")

    if knowledge_character == "DERIVED_FUSION" and not record.get("input_evidence_refs"):
        failures.append("ATMOS_FUSION_INPUTS_HIDDEN")

    if record.get("public_release_requested") and record.get("rights_status") in {None, "UNKNOWN", "NOASSERTION"}:
        failures.append("ATMOS_UNKNOWN_RIGHTS_PUBLIC")

    if record.get("public_surface") and record.get("lifecycle_state") in {
        "RAW",
        "WORK",
        "QUARANTINE",
        "CONNECTOR_CANDIDATE",
        "NORMALIZE_CANDIDATE",
    }:
        failures.append("ATMOS_PUBLIC_INTERNAL_ACCESS")

    if record.get("uses_run_receipt_as_release_proof"):
        failures.append("ATMOS_RECEIPT_AS_PROOF")

    return failures
```

> [!WARNING]
> The Python sketch is an implementation note, not proof. Enforcement requires repo-native validators, fixtures, policy tests, CI evidence, and review.

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Options considered

| Option | Decision | Why |
|---|---:|---|
| Keep only the thin domain-local ADR-0003 | Rejected | It preserves the seed decision but is too thin to govern source registry, normalization, evidence, policy, UI, Focus Mode, release, and rollback behavior. |
| Treat all air-like material as one integrated “air layer” | Rejected | It would hide the difference between observation, AQI report, model field, mask, anomaly, advisory, and fusion products. |
| Let connector output shape imply downstream semantics | Rejected | Current connector output is candidate/process memory only; it is not proof, release state, or public truth. |
| Move all atmosphere decision material into the domain README | Rejected | The domain README orients maintainers; repo-wide decisions belong in `docs/adr/`. |
| Create ADR-0312 in `docs/adr/` and preserve ADR-0003 as lineage | Accepted / proposed | Keeps repo-wide decision governance in the ADR ledger while preserving the domain-local continuity trail. |

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Consequences

### Positive consequences

- Reduces semantic drift between observations, reports, models, masks, fusion products, advisories, and metadata.
- Gives validators and policy tests stable reason-code targets.
- Keeps current no-network connector artifacts useful without overclaiming them.
- Makes Evidence Drawer and Focus Mode explainability requirements explicit.
- Preserves ADR-0003 as lineage while giving maintainers a fuller repo-wide decision record.
- Keeps publication separate from connector success, schema validity, receipt emission, and UI rendering.

### Costs and tradeoffs

| Cost | Mitigation |
|---|---|
| More fields are required before public claims can move forward. | Keep fixtures small and no-network first; use reason-coded denials. |
| Validators become stricter. | Ship valid/invalid examples and keep failure reasons stable. |
| Domain slug differences remain visible. | Record compatibility pressure and defer renames to a separate ADR/migration note. |
| Source onboarding slows down. | Require descriptors before live connectors; this is intentional. |
| Existing examples may fail new gates. | Keep candidate posture and add migration/fixture notes rather than silently upgrading examples. |

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Validation plan

### Required checks before acceptance

| Check | Required evidence | Status |
|---|---|---:|
| ADR index update | `docs/adr/README.md` links ADR-0312 and notes ADR-0003 lineage. | PROPOSED |
| Domain-local ADR link | `docs/domains/atmosphere_air/ADR-0003...` links to ADR-0312 or carries a supersession note. | PROPOSED |
| Source-role fixture pair | Valid and invalid source-role fixtures exist. | PROPOSED |
| Knowledge-character fixture pair | Valid and invalid knowledge-character fixtures exist. | PROPOSED |
| AQI/concentration negative test | AQI-as-concentration fails with `ATMOS_AQI_AS_CONCENTRATION`. | PROPOSED |
| AOD/PM2.5 negative test | AOD-as-PM2.5 fails without governed model assumptions. | PROPOSED |
| Smoke-mask/exposure negative test | Mask-as-exposure fails without model/fusion support. | PROPOSED |
| Model-as-observed negative test | Model field labeled as observation fails. | PROPOSED |
| Receipt/proof split test | RunReceipt cannot be used as EvidenceBundle or ReleaseManifest. | PROPOSED |
| Public-boundary test | Public API/UI/Focus cannot read connector or normalize candidates directly. | PROPOSED |
| EvidenceBundle closure test | `evidence_bundle_ref` resolves before any consequential claim is answered. | PROPOSED |
| Policy crosswalk alignment | Policy denies unknown rights/source-role/knowledge-character public release. | PROPOSED |
| CI or local validation receipt | Workflow run, validation report, or local command output captured in PR notes. | NEEDS VERIFICATION |
| Rollback path | Revert and supersession plan documented. | PROPOSED |

### Suggested local checks

```bash
# Confirm repository context.
git rev-parse --show-toplevel
git status --short
git branch --show-current

# Confirm ADR and related files.
find docs/adr docs/domains/atmosphere_air connectors/pipelines/air pipelines/normalize/domains/atmosphere \
  -maxdepth 2 -type f | sort

# Confirm current no-network artifacts parse.
python -m json.tool data/processed/air/qa_summary.example.json > /dev/null
python -m json.tool data/receipts/air/run_receipt.example.json > /dev/null

# Search for anti-collapse terms and reason codes.
git grep -nE 'ATMOS_AQI_AS_CONCENTRATION|ATMOS_AOD_AS_PM25|ATMOS_MODEL_AS_OBSERVED|ATMOS_PUBLIC_INTERNAL_ACCESS|knowledge_character|source_role' \
  -- docs connectors pipelines policy schemas contracts tests tools data 2>/dev/null || true
```

### Acceptance fixture matrix

| Fixture | Expected result |
|---|---:|
| Observed PM2.5 station record with source role, raw/normalized unit, time, EvidenceRefs | Pass as candidate; not public by itself. |
| AQI report carrying `PUBLIC_AQI_REPORT` and public-report method | Pass as report/index object. |
| AQI report claiming raw concentration | Fail with `ATMOS_AQI_AS_CONCENTRATION`. |
| AOD product claiming PM2.5 without model assumptions | Fail with `ATMOS_AOD_AS_PM25`. |
| Smoke plume mask claiming exposure measurement | Fail with `ATMOS_MASK_AS_EXPOSURE`. |
| Model field marked as observed | Fail with `ATMOS_MODEL_AS_OBSERVED`. |
| Derived fusion without input EvidenceRefs or transform identity | Fail with `ATMOS_FUSION_INPUTS_HIDDEN`. |
| Run receipt used as release proof | Fail with `ATMOS_RECEIPT_AS_PROOF`. |
| No-network stub requested for public publication | Fail with `ATMOS_PUBLIC_RELEASE_FALSE` or equivalent. |
| Public UI reads connector candidate directly | Fail with `ATMOS_PUBLIC_INTERNAL_ACCESS`. |

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Acceptance criteria

ADR-0312 can move from `draft/proposed` to `accepted` only when all relevant checks pass.

- [ ] ADR owners and policy label are verified.
- [ ] ADR meta-block type convention is resolved or accepted as an ADR-specific exception.
- [ ] ADR index includes ADR-0312.
- [ ] Domain-local ADR-0003 links to ADR-0312 or is marked as superseded/lineage.
- [ ] Source-role and knowledge-character fields are represented in the accepted schema/contract lane.
- [ ] Source descriptors require source role, rights, cadence, public-release posture, verification state, and caveats.
- [ ] Positive and negative fixtures exist for observed, AQI/report, regulatory archive, low-cost sensor, model field, remote mask, anomaly context, fusion product, advisory context, site context, and baseline/freshness support.
- [ ] Policy or validator checks deny AQI-as-concentration, AOD-as-PM2.5, smoke-mask-as-exposure, model-as-observed, missing rights, missing source role, missing knowledge character, and receipt-as-proof.
- [ ] Current no-network air connector artifacts remain candidate/process memory only.
- [ ] EvidenceBundle closure is required before any consequential public claim.
- [ ] Public API/UI/Focus Mode cannot read RAW, WORK, QUARANTINE, connector, normalize, or unpublished candidates directly.
- [ ] CI or documented local validation output is captured.
- [ ] Rollback/supersession path is documented and tested where implementation changed.

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Rollback and supersession

### Rollback plan

If this ADR causes incorrect enforcement or breaks valid candidate workflows:

1. Keep ADR-0312 as lineage; do not delete it.
2. Revert enforcement code or schema/policy changes through a PR.
3. Restore candidate-only handling for current no-network artifacts.
4. Preserve domain-local ADR-0003 and any successor links.
5. Add a correction note to the ADR index if public documentation changed.
6. Re-run fixture, validator, policy, and public-boundary checks.
7. Record which claims, if any, were public-facing and whether correction/withdrawal is needed.

### Rollback triggers

| Trigger | Required action |
|---|---|
| Valid observed records are denied because taxonomy is too narrow. | Add a reviewed taxonomy amendment and fixture pair; do not silently loosen policy. |
| Existing examples are mistakenly treated as public truth. | Revert publication path, restore candidate label, and add negative fixture. |
| Run receipts are used as proof. | Block release, add `ATMOS_RECEIPT_AS_PROOF`, and update proof/release docs. |
| Public UI/API reads connector or normalize candidates. | Revert public route/layer, add public-boundary denial test. |
| Source rights are discovered to be unknown or restrictive. | Block public release and update SourceDescriptor review state. |
| ADR-0003 and ADR-0312 diverge. | Add supersession link and reconcile through ADR index update. |
| A later ADR changes schema-home or policy-home authority. | Update related links and compatibility notes; preserve historical path mapping. |

### Supersession rule

A future ADR may supersede ADR-0312 only if it:

- names what is superseded;
- preserves ADR-0003 and ADR-0312 lineage;
- provides stronger repo evidence, tests, policy, schema, or runtime proof;
- updates ADR index and domain docs;
- describes compatibility and migration;
- retains rollback and correction visibility.

<p align="right"><a href="#top">Back to top ↑</a></p>

---

## Open verification

| Item | Status | Why it matters |
|---|---:|---|
| ADR owners | NEEDS VERIFICATION | Owner and review routing are required before acceptance. |
| Creation date | NEEDS VERIFICATION | Existing target has a placeholder creation date. |
| Policy label | NEEDS VERIFICATION | Public/restricted status must match repo policy. |
| ADR meta-block type | NEEDS VERIFICATION | Current target uses `architecture-decision-record`; adjacent ADR files also show `standard`. |
| ADR numbering and index status | NEEDS VERIFICATION | ADR index should link ADR-0312 and clarify its relationship to ADR-0003. |
| Schema-home acceptance | NEEDS VERIFICATION | ADR-0001 remains proposed; avoid claiming final machine-schema authority. |
| Source registry path and descriptor schema | NEEDS VERIFICATION | Source-role enforcement depends on descriptor home and fields. |
| Policy engine and deny-code implementation | UNKNOWN | Crosswalk/docs exist, but executable policy enforcement is not proven here. |
| Validator and fixture coverage | UNKNOWN | Required before enforcement maturity can be upgraded. |
| CI workflow enforcement | UNKNOWN | Workflow presence or docs do not prove merge-blocking checks. |
| EvidenceBundle referenced by QA summary | NEEDS VERIFICATION | `qa_summary.example.json` references an EvidenceBundle path; closure is not proven here. |
| Public API/UI/Focus binding | UNKNOWN | No direct public route/component behavior is claimed by this ADR. |
| Live source rights and terms | UNKNOWN | Public release must fail closed while rights remain unknown. |
| Release/proof/rollback artifacts | UNKNOWN | No release authorization is made by this ADR. |

<p align="right"><a href="#top">Back to top ↑</a></p>
