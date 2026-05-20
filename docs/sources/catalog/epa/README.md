<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/source-family-brief-epa
title: EPA — Source Family Brief
type: standard
version: v1
status: draft
owners: TODO — Atmosphere/Air domain steward; Source registry steward
created: 2026-05-13
updated: 2026-05-13
policy_label: public
related:
  - docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - docs/domains/atmosphere/README.md
  - docs/domains/hazards/README.md
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0001-schema-home.md
  - docs/registers/VERIFICATION_BACKLOG.md
tags: [kfm, sources, source-family, epa, atmosphere-air, hazards]
notes:
  - Path docs/sources/catalog/ is PROPOSED grouping of per-agency source briefs under docs/sources/.
  - All schema, policy, and registry paths are PROPOSED until mounted-repo evidence verifies them.
  - "Catalog" in this path means a documentation catalog of source briefs; it is NOT the data/catalog/ lifecycle phase.
[/KFM_META_BLOCK_V2] -->

# EPA — Source Family Brief

> Source-admission and authority-control brief for U.S. Environmental Protection Agency (EPA) data programs used by Kansas Frontier Matrix (KFM). EPA is a **multi-program source family**, not a single source.

![status](https://img.shields.io/badge/status-draft-lightgrey) ![doc-type](https://img.shields.io/badge/doc--type-source--family--brief-blue) ![activation](https://img.shields.io/badge/activation-NEEDS%20VERIFICATION-orange) ![source-role](https://img.shields.io/badge/source--roles-regulatory%20%7C%20context%20%7C%20model-informational) ![lifecycle](https://img.shields.io/badge/lifecycle-PROPOSED-yellow) ![updated](https://img.shields.io/badge/updated-2026--05--13-lightgrey)

| Field | Value |
|---|---|
| **Status** | `draft` (review pending) |
| **Doc type** | Source family brief — informative, not normative |
| **Owners** | TODO — Atmosphere/Air domain steward; Source registry steward |
| **Last updated** | 2026-05-13 |
| **Schema authority** | `schemas/contracts/v1/source/source-descriptor.json` per ADR-0001 (PROPOSED path; NEEDS VERIFICATION in mounted repo) |
| **Activation state** | NEEDS VERIFICATION — no mounted `SourceActivationDecision` confirmed in this session |

---

## Quick jump

- [1. Scope](#1-scope)
- [2. Repo fit](#2-repo-fit)
- [3. EPA in KFM at a glance](#3-epa-in-kfm-at-a-glance)
- [4. Programs covered](#4-programs-covered)
- [5. Source-role assignment](#5-source-role-assignment)
- [6. Cross-domain placement](#6-cross-domain-placement)
- [7. Lifecycle and admission flow](#7-lifecycle-and-admission-flow)
- [8. Rights, sensitivity, publication posture](#8-rights-sensitivity-publication-posture)
- [9. Anti-collapse rules](#9-anti-collapse-rules)
- [10. Schemas, contracts, and policy references](#10-schemas-contracts-and-policy-references)
- [11. Validators and tests (proposed)](#11-validators-and-tests-proposed)
- [12. Open verification items](#12-open-verification-items)
- [13. Related docs](#13-related-docs)
- [Appendix A — Field-level descriptor surface (illustrative)](#appendix-a--field-level-descriptor-surface-illustrative)
- [Appendix B — Glossary](#appendix-b--glossary)

---

## 1. Scope

**CONFIRMED** — This brief covers how KFM treats data programs published by the **U.S. Environmental Protection Agency (EPA)** as a source family, including admission gates, source-role assignment, rights/sensitivity posture, cross-domain placement, anti-collapse rules, and the lifecycle stages each program must traverse before public surfaces can cite it.

It does **not** define schemas, decide release admissibility, or replace the authoritative `SourceDescriptor` schema. Field-level shape belongs in `schemas/`; allow/deny logic belongs in `policy/`; release decisions belong in `release/`. (Directory Rules §2.3.)

> [!NOTE]
> **PROPOSED placement.** The `docs/sources/catalog/` subdirectory is a PROPOSED grouping of per-agency source briefs under the canonical `docs/sources/` lane (Directory Rules §6.1, which lists `sources/` as "source-descriptor standards, source families"). The word *catalog* here means a documentation catalog of source briefs and is **not** the `data/catalog/` lifecycle phase. If the mounted repo uses a different convention, open a `docs/registers/DRIFT_REGISTER.md` entry rather than silently re-homing.

[Back to top](#epa--source-family-brief)

---

## 2. Repo fit

**PROPOSED** — All paths below are placement proposals consistent with Directory Rules; none has been verified against a mounted repository in this session.

```text
docs/
└── sources/
    ├── SOURCE_DESCRIPTOR_STANDARD.md      # cross-family standard (PROPOSED)
    └── catalog/                            # per-agency source briefs (PROPOSED grouping)
        ├── README.md                       # PROPOSED index
        ├── epa.md                          # ← this file
        ├── noaa.md                         # PROPOSED sibling
        ├── usgs.md                         # PROPOSED sibling
        ├── fema.md                         # PROPOSED sibling
        ├── usda.md                         # PROPOSED sibling
        └── kdhe.md                         # PROPOSED sibling (state-level neighbour)
```

| Direction | Relationship | Truth label |
|---|---|---|
| **Upstream doctrine** | `docs/doctrine/directory-rules.md`, `docs/doctrine/lifecycle-law.md`, `docs/doctrine/truth-posture.md` | CONFIRMED doctrine; specific file paths PROPOSED |
| **Sibling standard** | `docs/sources/SOURCE_DESCRIPTOR_STANDARD.md` (canonical descriptor rules) | PROPOSED |
| **Domain consumers** | `docs/domains/atmosphere/README.md`, `docs/domains/hazards/README.md` | PROPOSED paths; CONFIRMED domain ownership per encyclopedia §7.9 and §7.10 |
| **Schema home** | `schemas/contracts/v1/source/source-descriptor.json` per ADR-0001 | PROPOSED path; CONFIRMED schema-home convention |
| **Registry home** | `data/registry/sources/atmosphere/epa/` | PROPOSED — per Directory Rules §7.5 / §12 pattern |
| **Policy home** | `policy/sensitivity/atmosphere/`, `policy/source/<…>/` | PROPOSED |

> [!IMPORTANT]
> **Watcher-as-non-publisher.** Connectors that pull EPA data MUST write only to `data/raw/atmosphere/<source_id>/<run_id>/` or `data/quarantine/...`, with source descriptors, checksums, and ingest receipts. Connectors MUST NOT publish, mutate canonical truth, or write under `data/processed/`, `data/catalog/`, or `data/published/`. (Directory Rules §7.3.)

[Back to top](#epa--source-family-brief)

---

## 3. EPA in KFM at a glance

**CONFIRMED doctrine / PROPOSED implementation.**

EPA appears in KFM primarily as the source authority behind regulatory air-quality archives, near-real-time public AQI services, smoke-trajectory contexts, and ancillary hydrography/regulatory-watershed attributes. It is referenced in the encyclopedia source register under two stable identifiers and called out in the Atmosphere/Air and Hazards domain dossiers.

| KFM source ID | EPA product / service | Encyclopedia status | Encyclopedia note |
|---|---|---|---|
| `EXT-AQS` | EPA AQS / AirData | EXTERNALLY CHECKED | "Regulatory ambient air quality archive. Operational freshness and parameter handling required." |
| `EXT-AIRNOW` | AirNow API | EXTERNALLY CHECKED | "Near-real-time public air quality context. Not regulatory record; official docs warn accordingly." |

> [!NOTE]
> **Not a single source.** EPA is treated as a **source family** — each EPA program (AQS, AirNow, Barkjohn correction for low-cost sensors, smoke products, NHD/RAD attributes) receives its own `SourceDescriptor` and its own `SourceActivationDecision`. Source role cannot be inferred from convenience or shared agency identity. *(Source-role anti-collapse rule, CONFIRMED doctrine.)*

[Back to top](#epa--source-family-brief)

---

## 4. Programs covered

The programs below are the EPA products referenced in current KFM project knowledge. Each is a distinct source under KFM admission rules.

| Program | What it is | Typical product shape | Primary KFM domain | KFM source ID | Status |
|---|---|---|---|---|---|
| **EPA AQS / AirData** | Validated, regulatory-grade ambient pollutant archive from federal/state/local monitors. | Row-level monitor records (PM2.5, ozone, NO₂, etc.), QA/QC flags, daily summaries. | Atmosphere/Air | `EXT-AQS` | CONFIRMED reference; activation NEEDS VERIFICATION |
| **AirNow API** | Near-real-time public AQI service; not a regulatory record. | AQI values and preliminary criteria-pollutant readings. | Atmosphere/Air | `EXT-AIRNOW` | CONFIRMED reference; activation NEEDS VERIFICATION |
| **EPA Barkjohn correction** | Published regression that reconciles PurpleAir low-cost sensors to regulatory monitors. | Versioned regression coefficients applied at processing. | Atmosphere/Air (modeled adjunct) | TODO (no project-knowledge ID) | PROPOSED — required before any PurpleAir reading is published |
| **EPA NHD / RAD attributes** | EPA-published service attributes attached to NHDPlus hydrography (e.g., HUC12 fields). | Tabular attributes joined to NHDPlus features. | Hydrology (auxiliary corroboration) | TODO (no project-knowledge ID) | PROPOSED — supports COMID↔HUC12 crosswalk QA |
| **HMS smoke (NOAA-led, EPA-adjacent reporting)** | Smoke-plume context products often co-cited with EPA AirNow. | Polygon/raster smoke products. | Hazards (smoke context) | TODO (NOAA-primary; included for cross-reference) | PROPOSED — see `noaa.md` (PROPOSED sibling) |

> [!TIP]
> **PurpleAir + Barkjohn pairing.** When a PurpleAir-derived value is published, KFM convention is to preserve **both** the corrected and the uncorrected reading, plus the Barkjohn regression version pin, so the correction is reversible and auditable. *(Encyclopedia C10-02, CONFIRMED.)*

[Back to top](#epa--source-family-brief)

---

## 5. Source-role assignment

**CONFIRMED doctrine.** Source role is a first-class identity attribute. An observed monitor reading is **not** interchangeable with a near-real-time AQI report, a regulatory determination, or a modeled adjustment. The lifecycle and the governed API both fail closed when these roles are conflated. (Master Source-Role Anti-Collapse Register §24.1.)

The canonical role classes are: `observed | regulatory | modeled | aggregate | administrative | candidate | synthetic`.

| EPA program | KFM source role(s) | Why |
|---|---|---|
| AQS monitor record (row-level) | `observed` | A direct, QA/QC-validated reading from a sited monitor. |
| AQS annual/decennial summary | `aggregate` | Published summary over a unit; loss of per-record fidelity. |
| AQS regulatory non-attainment ruling (if ingested) | `regulatory` | Authoritative determination with administrative force. |
| AirNow AQI value | `aggregate` *(category/index)* + `context` posture | AQI is an index, not a concentration; preliminary, not regulatory. |
| AirNow raw pollutant value | `observed` *(provisional)* | Direct reading, but preliminary; flag accordingly. |
| Barkjohn-corrected PurpleAir value | `modeled` | Derived via a fitted regression; uncertainty and version must be preserved. |
| EPA NHD/RAD attributes | `administrative` *(reference compilation)* | Compiled attribute joined to canonical hydrography. |
| HMS smoke polygon | `modeled` *(context)* | Derived smoke estimate; not observed inundation/exposure. |

> [!WARNING]
> **Never relabel a role to satisfy a join.** A community-science co-located sensor is not a regulatory authority; a smoke model is not an observed exposure; an AirNow AQI is not an AQS concentration. KFM denies publication that collapses these roles.

[Back to top](#epa--source-family-brief)

---

## 6. Cross-domain placement

EPA programs flow primarily into the **Atmosphere/Air** domain lane, with secondary placements in **Hazards** (smoke/wildfire context) and **Hydrology** (NHD/RAD auxiliary corroboration only — never as observed hydrologic truth).

```mermaid
flowchart TD
    subgraph EPA["EPA — External Source Family"]
        AQS["AQS / AirData<br/>(regulatory archive)"]
        AIRNOW["AirNow API<br/>(near-real-time context)"]
        BARK["Barkjohn correction<br/>(published regression)"]
        NHDRAD["NHD / RAD attributes<br/>(administrative compilation)"]
    end

    DESC["SourceDescriptor<br/>(per program)<br/><i>schema PROPOSED</i>"]
    DECIDE{"SourceActivationDecision<br/>(allowed / restricted /<br/>denied / needs-review)"}

    AQS --> DESC
    AIRNOW --> DESC
    BARK --> DESC
    NHDRAD --> DESC
    DESC --> DECIDE

    DECIDE -- "allowed" --> RAW["data/raw/&lt;domain&gt;/&lt;source_id&gt;/&lt;run_id&gt;/"]
    DECIDE -- "restricted / denied / review" --> QUAR["data/quarantine/...<br/>(no PUBLISHED edge)"]

    RAW --> WORK["WORK"]
    WORK --> PROC["PROCESSED<br/>(validated normalized records)"]
    PROC --> CAT["CATALOG / TRIPLET<br/>(STAC/DCAT/PROV, graph)"]
    CAT --> PUB["PUBLISHED<br/>(governed API only)"]

    PUB --> ATM["Atmosphere / Air<br/>(primary domain)"]
    PUB --> HAZ["Hazards<br/>(smoke context only)"]
    PUB --> HYD["Hydrology<br/>(NHD/RAD aux. corroboration)"]

    classDef src fill:#eef,stroke:#447,color:#000
    classDef gate fill:#ffd,stroke:#a80,color:#000
    classDef pub fill:#dfd,stroke:#272,color:#000
    classDef deny fill:#fdd,stroke:#a22,color:#000
    class AQS,AIRNOW,BARK,NHDRAD src
    class DESC,DECIDE gate
    class PUB,ATM,HAZ,HYD pub
    class QUAR deny
```

| Domain | EPA contribution | Boundary |
|---|---|---|
| **Atmosphere, Air, and Climate** | Station observations (AQS), near-real-time context (AirNow), modeled adjuncts (Barkjohn) | KFM **does not** replace official advisories or emergency alerting. |
| **Hazards** | Smoke/wildfire context co-cited with EPA AirNow advisories | KFM **does not** act as a life-safety alerting system. Operational warnings are **context only**. |
| **Hydrology** | EPA NHD/RAD service attributes (e.g., HUC12 fields) for crosswalk QA | EPA NHD/RAD is **corroborative**, never the canonical hydrography source (USGS WBD/NHDPlus HR remain canonical). |

> [!CAUTION]
> **Domain boundary integrity.** EPA AirNow is *not* a hazards alerting system inside KFM. Hazards may quote AirNow as advisory **context** and MUST redirect life-safety action to official sources via the not-for-life-safety disclaimer.

[Back to top](#epa--source-family-brief)

---

## 7. Lifecycle and admission flow

**CONFIRMED invariant.** RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED. Promotion is a **governed state transition, not a file move.**

| Phase | What EPA data looks like here | Gate to next phase | Status |
|---|---|---|---|
| `raw/` | Immutable source-edge capture (raw AQS pull, AirNow JSON response), with retrieval metadata, ETag/Last-Modified, checksum, and source descriptor. | `SourceDescriptor` exists; `SourceActivationDecision` says allowed/restricted. | PROPOSED |
| `work/` / `quarantine/` | Normalized AQS row → `AirObservation` candidate; AirNow → provisional `PM25Observation`/`OzoneObservation`; Barkjohn applied as a `TransformReceipt`. Failed/ambiguous records routed to `quarantine/`. | Validation report + policy gate pass; otherwise quarantine reason recorded. | PROPOSED |
| `processed/` | Validated canonical `AirObservation`, `AirStation`, etc., with unit-conversion receipts and freshness tags. | `EvidenceRef`, `ValidationReport`, and digest closure exist. | PROPOSED |
| `catalog/` / `triplets/` | STAC items per AQS monitor-year; DCAT distribution per AirNow feed; PROV lineage; graph projections. | Catalog/proof closure; `EvidenceBundle` resolvable from claim. | PROPOSED |
| `published/` | Governed-API payloads for the Atmosphere/Air map layers, Evidence Drawer, and station time-series fixtures. | `ReleaseManifest`, correction path, rollback target, review/policy state all exist. | PROPOSED |

**PROPOSED source-activation flow.** Create or update `SourceDescriptor`; review source role, rights, sensitivity, cadence, and access; issue `SourceActivationDecision` declaring `allowed | restricted | denied | needs-review`; keep connectors/watchers inactive until activation decision, fixtures, validators, and policy gates exist. *(Per Unified Implementation Manual §3.6.)*

[Back to top](#epa--source-family-brief)

---

## 8. Rights, sensitivity, publication posture

| Concern | Posture | Status |
|---|---|---|
| **License / terms** | EPA AQS and AirNow are public U.S. federal products; **specific current terms (key requirements, attribution clauses, redistribution constraints, rate limits) NEEDS VERIFICATION before connector activation.** | NEEDS VERIFICATION |
| **Attribution** | Cite the originating EPA program and the retrieval time. Distinct citations for AQS vs AirNow vs Barkjohn-derived values. | PROPOSED |
| **Sensitivity** | Air quality monitor locations are generally public. Sensitive joins (e.g., to private health data) fail closed by default. | CONFIRMED posture |
| **Freshness** | AQS validated data lags months; AirNow is near-real-time but **preliminary**. Freshness badge required on UI surfaces. | CONFIRMED doctrine |
| **Life-safety** | EPA AirNow operational warnings are **context**, never KFM emergency instructions. UI MUST redirect to official sources. | CONFIRMED doctrine |
| **Low-cost sensor publication** | Requires Barkjohn correction, caveats, confidence interval, and limitations text before publication; uncorrected reading retained alongside corrected. | CONFIRMED doctrine |

> [!IMPORTANT]
> **Unknown rights fail closed.** Per the encyclopedia's sensitive / deny-by-default register, source-rights-limited records DENY public release until terms resolved. Until the explicit EPA terms and rate-limit posture are recorded in `data/registry/rights/atmosphere/epa/` (PROPOSED), connector activation must remain `needs-review`.

[Back to top](#epa--source-family-brief)

---

## 9. Anti-collapse rules

**CONFIRMED doctrine.** These are the EPA-specific anti-collapse rules drawn from project knowledge. Violating any of them is a publication blocker.

| Anti-collapse rule | Rationale | Default outcome |
|---|---|---|
| **AQI is not concentration.** | AQI is a categorical index; mg/m³ or ppb concentrations are not AQI values. | DENY publication that labels AQI as concentration; ABSTAIN at Focus Mode. |
| **AOD is not PM2.5.** | Satellite aerosol optical depth is a column property; surface PM2.5 is a near-ground concentration. | DENY publication that equates them; require modeled-link receipt. |
| **AirNow is not AQS.** | AirNow is near-real-time preliminary; AQS is the validated regulatory archive. | DENY publication that cites AirNow as regulatory-grade. |
| **Low-cost sensor unadjusted ≠ regulatory monitor.** | PurpleAir raw readings systematically overstate PM. | DENY publication of uncorrected PurpleAir values; require Barkjohn version pin. |
| **Model output is not observation.** | HMS smoke / modeled adjustments must cite model identity, run receipt, and bounds. | Cite as modeled context; never relabel as observation. |
| **Advisory is not life-safety authority.** | EPA AirNow advisories are contextual. | UI MUST redirect to official source; not-for-life-safety disclaimer required. |

[Back to top](#epa--source-family-brief)

---

## 10. Schemas, contracts, and policy references

**PROPOSED — paths below are placement proposals per Directory Rules §6.1, §7.4, ADR-0001; NEEDS VERIFICATION in mounted repo.**

| Concern | Proposed path | Status |
|---|---|---|
| `SourceDescriptor` schema | `schemas/contracts/v1/source/source-descriptor.json` | PROPOSED per ADR-0001 |
| `SourceActivationDecision` schema | `schemas/contracts/v1/source/source-activation-decision.json` | PROPOSED |
| `AirStation` / `AirObservation` object meaning | `contracts/atmosphere/air-objects.md` | PROPOSED |
| `AirStation` / `AirObservation` schemas | `schemas/contracts/v1/domains/atmosphere/*.schema.json` | PROPOSED |
| EPA program rights registry | `data/registry/rights/atmosphere/epa/` | PROPOSED |
| EPA program source descriptors | `data/registry/sources/atmosphere/epa/` | PROPOSED |
| Atmosphere policy gates | `policy/domains/atmosphere/` | PROPOSED |
| Atmosphere sensitivity policy | `policy/sensitivity/atmosphere/` | PROPOSED |
| Atmosphere fixtures | `fixtures/domains/atmosphere/epa/` | PROPOSED |

> [!NOTE]
> **No parallel authority.** Creating a parallel home for schemas, contracts, policy, sources, registries, releases, or proofs requires an accepted ADR. (Directory Rules §2.4.)

[Back to top](#epa--source-family-brief)

---

## 11. Validators and tests (proposed)

**PROPOSED.** None of the validators below have been verified in a mounted repository in this session. They are the validator surface implied by the Atmosphere/Air dossier and the EPA anti-collapse rules.

- Knowledge-character registry tests for `OBSERVED_SENSOR`, `PUBLIC_AQI_REPORT`, `REGULATORY_ARCHIVE`, `LOW_COST_SENSOR`, `ATMOSPHERIC_MODEL_FIELD`, `ALERT_AND_ADVISORY_CONTEXT`, `NETWORK_AND_SITE_CONTEXT`.
- Unit normalization tests (e.g., ppb ↔ µg/m³ where conversion is defined; reject where it isn't).
- **AQI-as-concentration denial test.**
- **AOD-as-PM2.5 denial test.**
- **Model-as-observed denial test.**
- **Low-cost sensor caveat presence test** (Barkjohn version pin required; uncorrected pair retained).
- **AirNow-as-regulatory denial test.**
- **Life-safety disclaimer presence test** for any AirNow advisory carrier on public surfaces.
- Dry-run no-live-fetch tests (offline fixtures only; no network calls in CI).

[Back to top](#epa--source-family-brief)

---

## 12. Open verification items

These items remain `UNKNOWN` or `NEEDS VERIFICATION` until a mounted repository or runtime evidence is inspected.

- [ ] Does `schemas/contracts/v1/source/source-descriptor.json` exist? Fields and required-set NEEDS VERIFICATION.
- [ ] Does `data/registry/sources/atmosphere/epa/` contain any `SourceDescriptor` or `SourceActivationDecision` records? UNKNOWN.
- [ ] Current EPA AQS API key, rate-limit, and terms posture: NEEDS VERIFICATION.
- [ ] Current AirNow API terms and bulk-access constraints: NEEDS VERIFICATION.
- [ ] Barkjohn regression version in use (and its pin location): UNKNOWN.
- [ ] Atmosphere/Air `LayerManifest` entries that cite EPA sources: UNKNOWN.
- [ ] Are any EPA-citing layers currently in `data/published/layers/atmosphere/`? UNKNOWN.
- [ ] Is `policy/sensitivity/atmosphere/` configured with the AQI ≠ concentration denial rule? UNKNOWN.
- [ ] Is the not-for-life-safety disclaimer rendered for AirNow advisory carriers in the map UI? UNKNOWN.
- [ ] Drift entry: confirm `docs/sources/catalog/` is the actual home or open a `DRIFT_REGISTER` entry. UNKNOWN.

> [!TIP]
> Open verification items belong in `docs/registers/VERIFICATION_BACKLOG.md` once that register exists. Move them there during the first review pass; keep a back-pointer in this brief.

[Back to top](#epa--source-family-brief)

---

## 13. Related docs

- `docs/sources/SOURCE_DESCRIPTOR_STANDARD.md` — cross-family descriptor standard *(PROPOSED)*
- `docs/sources/catalog/README.md` — catalog index of source briefs *(PROPOSED)*
- `docs/domains/atmosphere/README.md` — Atmosphere, Air, and Climate domain dossier *(PROPOSED path; CONFIRMED domain in encyclopedia §7.9)*
- `docs/domains/hazards/README.md` — Hazards domain dossier *(PROPOSED path; CONFIRMED domain in encyclopedia §7.10)*
- `docs/doctrine/directory-rules.md` — placement law *(CONFIRMED doctrine)*
- `docs/doctrine/lifecycle-law.md` — RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED invariant
- `docs/doctrine/truth-posture.md` — cite-or-abstain default
- `docs/adr/ADR-0001-schema-home.md` — schema-home decision
- `docs/registers/DRIFT_REGISTER.md` — for placement conflicts
- `docs/registers/VERIFICATION_BACKLOG.md` — for items in §12

---

<details>
<summary><strong>Appendix A — Field-level descriptor surface (illustrative)</strong></summary>

> **PROPOSED, illustrative only.** Reproduced and condensed from the Domains Atlas §24.1.3. Actual field presence and names are NEEDS VERIFICATION in the mounted `SourceDescriptor` schema.

| Field | Type / vocabulary | Required? | Notes for EPA programs |
|---|---|---|---|
| `source_id` | string (stable) | MUST | e.g., `EXT-AQS`, `EXT-AIRNOW`; per-program, not per-agency. |
| `source_role` | enum: `observed | regulatory | modeled | aggregate | administrative | candidate | synthetic` | MUST | See §5. Set at admission. Never edited in place; corrections produce a new descriptor + `CorrectionNotice`. |
| `role_authority` | string (issuing body / model identity) | MUST when role ∈ {`regulatory`, `modeled`, `aggregate`} | "U.S. EPA, AirNow Program Office", "Barkjohn et al. (regression vX)", etc. |
| `role_aggregation_unit` | geometry-scope token (county, HUC, tract, year, decade, …) | MUST when `source_role = aggregate` | AQI is an index aggregation; AQS annual summaries are temporal aggregates. |
| `role_model_run_ref` | `EvidenceRef` → `ModelRunReceipt` | MUST when `source_role = modeled` | Pin the Barkjohn regression version, HMS smoke run, etc. |
| `rights_posture` | structured: license, attribution, redistribution, rate-limit | MUST | EPA terms NEEDS VERIFICATION before activation. |
| `cadence` | structured: poll interval, freshness expectation | MUST | AirNow ≈ near-real-time; AQS ≈ months-delayed validated. |
| `sensitivity_class` | enum | MUST | Default `public`; sensitive joins fail closed. |
| `release_class` | enum | MUST | Required before a `LayerManifest` may cite the source. |

</details>

<details>
<summary><strong>Appendix B — Glossary</strong></summary>

| Term | Definition |
|---|---|
| `SourceDescriptor` | Machine-readable source identity: role, rights, cadence, access, steward, sensitivity, release posture. |
| `SourceActivationDecision` | Gate record deciding whether a source may be `allowed`, `restricted`, `denied`, or `needs-review`. |
| `EvidenceRef` | Reference that must resolve to an `EvidenceBundle` before public claim authority. |
| `EvidenceBundle` | Resolved evidence package: sources, excerpts, provenance, policy/review/release state. **Outranks generated language.** |
| `PolicyDecision` | Explicit `allow | deny | restrict | abstain | error` decision. |
| `RuntimeResponseEnvelope` | Finite answer envelope for governed AI/API surfaces. |
| `AIReceipt` | Runtime accountability record for bounded AI use; **never** a substitute for `EvidenceBundle`. |
| `LayerManifest` | Binds a UI layer to governed source/evidence semantics. |
| `ReleaseManifest` | Defines a complete published release; carries rollback target. |
| `RollbackCard` | Rollback target/drill object that preserves history while repointing release state. |
| `Promotion` | Governed release **state transition**, not a file move. |
| **Source role** | First-class identity attribute distinguishing observed / regulatory / modeled / aggregate / administrative / candidate / synthetic content. |

</details>

---

**Related docs:** see [§13](#13-related-docs) · **Last updated:** 2026-05-13 · [Back to top](#epa--source-family-brief)
