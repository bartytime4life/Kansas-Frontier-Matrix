<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/source-catalog-usgs
title: USGS — Source Family Catalog Entry
type: standard
version: v1
status: draft
owners: TODO — Docs steward + Hydrology domain owner + Spatial Foundation domain owner
created: 2026-05-13
updated: 2026-05-13
policy_label: public
related:
  - docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - docs/doctrine/truth-posture.md
  - docs/domains/hydrology/README.md
  - connectors/usgs/README.md
  - schemas/contracts/v1/source/source_descriptor.schema.json
tags: [kfm, sources, catalog, usgs, hydrology, spatial-foundation, geology, hazards]
notes:
  - Catalog entry; not an admission decision. Activation lives in data/registry/sources/.
  - Per-sub-source rights/cadence remain NEEDS VERIFICATION until SourceDescriptor lands.
[/KFM_META_BLOCK_V2] -->

# USGS — Source Family Catalog Entry

> Catalog entry for U.S. Geological Survey (USGS) source families in the Kansas Frontier Matrix (KFM). Records identity, source roles, sensitivity posture, and lane fit — **not** an admission decision and **not** the SourceDescriptor itself.

<!-- Badges: targets are placeholders pending real CI / status endpoints. -->
![Status: draft](https://img.shields.io/badge/status-draft-lightgrey)
![Doc type: source-family-catalog](https://img.shields.io/badge/doc-source--family--catalog-blue)
![Policy label: public](https://img.shields.io/badge/policy-public-green)
![Truth posture: cite-or-abstain](https://img.shields.io/badge/posture-cite--or--abstain-orange)
![Lifecycle: governed transition](https://img.shields.io/badge/lifecycle-governed--state--transition-purple)
![Updated: 2026-05-13](https://img.shields.io/badge/updated-2026--05--13-informational)

| Field | Value |
|---|---|
| **Status** | `draft` |
| **Owners** | `TODO` — Docs steward · Hydrology domain owner · Spatial Foundation domain owner |
| **Last updated** | `2026-05-13` |
| **Path** | `docs/sources/catalog/usgs.md` *(PROPOSED — see §2 Repo fit)* |

---

## Quick jump

- [§1. Scope](#1-scope)
- [§2. Repo fit](#2-repo-fit)
- [§3. Inputs — what belongs here](#3-inputs--what-belongs-here)
- [§4. Exclusions — what does not belong here](#4-exclusions--what-does-not-belong-here)
- [§5. Sub-source registry (catalog index)](#5-sub-source-registry-catalog-index)
- [§6. Source-role posture (anti-collapse)](#6-source-role-posture-anti-collapse)
- [§7. Rights, sensitivity, freshness](#7-rights-sensitivity-freshness)
- [§8. Source admission flow](#8-source-admission-flow)
- [§9. Lifecycle hand-off](#9-lifecycle-hand-off)
- [§10. Task list — readiness backlog](#10-task-list--readiness-backlog)
- [§11. FAQ](#11-faq)
- [§12. Related docs](#12-related-docs)
- [§13. Appendix — schema field hooks](#13-appendix--schema-field-hooks)

---

## 1. Scope

**CONFIRMED doctrine.** USGS — the United States Geological Survey — operates several distinct geospatial and hydrologic data programs that KFM admits as a **source family**. Each program is a separate `SourceDescriptor` candidate with its own role, rights, cadence, steward, and sensitivity posture. This page catalogs the family at the doctrine level; it does **not** stand in for any single `SourceDescriptor` and is **not** a `SourceActivationDecision`.

The KFM source registry is, per doctrine, an *admission and authority-control surface, not a bibliography.* This entry exists so reviewers and stewards can locate the USGS family, see its sub-sources at a glance, and understand which lane each belongs to before any connector or pipeline is activated.

> [!NOTE]
> **CONFIRMED scope guard.** Cataloging USGS here does not grant any sub-source admission, activation, or public-release authority. A sub-source remains inactive until a `SourceDescriptor` is created, reviewed for role/rights/sensitivity/cadence/access, and a `SourceActivationDecision` is recorded. Connectors and watchers stay inactive until activation, fixtures, validators, and policy gates exist.

---

## 2. Repo fit

**Path:** `docs/sources/catalog/usgs.md` — **PROPOSED**.

| Aspect | Status | Basis |
|---|---|---|
| `docs/sources/` lane | **CONFIRMED** | Directory Rules §6.1 lists `docs/sources/` for "source-descriptor standards, source families." |
| `catalog/` subfolder | **PROPOSED** | Not explicitly named in Directory Rules; consistent with the lane's purpose (per-family catalog pages). Open a `docs/registers/DRIFT_REGISTER.md` entry if a different convention is preferred. |
| Domain placement | **CONFIRMED** | Cross-domain source family; therefore *not* under any single `docs/domains/<domain>/`. Directory Rules §12 — multi-domain files live under the lowest common responsibility root without a domain segment. |
| Connector home | **CONFIRMED** | `connectors/usgs/` is named in Directory Rules §7.3. |
| Schema home (descriptor) | **CONFIRMED default** | `schemas/contracts/v1/source/source_descriptor.schema.json` per ADR-0001 (schema home). Specific file presence is **NEEDS VERIFICATION** until the mounted repo is inspected. |

**Upstream of this page:**

- `docs/sources/README.md` *(PROPOSED — landing page for the `docs/sources/` lane)*
- `docs/sources/SOURCE_DESCRIPTOR_STANDARD.md` *(PROPOSED — referenced in the Whole-UI Expansion Report)*

**Downstream of this page:**

- `connectors/usgs/README.md` and per-sub-source connector READMEs
- `data/registry/sources/hydrology/usgs-*.yaml` and per-domain registry entries
- `schemas/contracts/v1/source/source_descriptor.schema.json` instances

---

## 3. Inputs — what belongs here

This catalog entry MUST describe, for each USGS sub-source KFM intends to consume:

1. The **canonical sub-source identity** (program name, URL or service endpoint, governing USGS office).
2. The **source role(s)** — `observed`, `regulatory`, `modeled`, `aggregate`, `administrative`, `candidate`, or `synthetic` — as defined in the Master Source-Role Anti-Collapse Register.
3. The **domain lanes** the sub-source feeds (e.g., Hydrology, Spatial Foundation, Geology, Hazards).
4. **Rights / sensitivity / freshness posture** at a doctrine level (NEEDS VERIFICATION at the per-`SourceDescriptor` level).
5. **Admission status**: not started · candidate · activated · restricted · denied · retired.
6. Links to **adjacent governance** (connector, descriptor schema, domain page, drift entries).

---

## 4. Exclusions — what does not belong here

This page is **not** the place for:

| If it is… | …it belongs in |
|---|---|
| The machine-readable `SourceDescriptor` for a sub-source | `schemas/contracts/v1/source/source_descriptor.schema.json` (shape) + `data/registry/sources/<domain>/<source_id>.yaml` (instance) — both PROPOSED until verified |
| Connector code, retrieval logic, credentials policy | `connectors/usgs/<sub-source>/` |
| Pipeline declarative spec for a USGS ingest | `pipeline_specs/<domain>/` |
| Pipeline executable steps | `pipelines/ingest/` and `pipelines/domains/<domain>/` |
| Activation / restriction / denial decisions | A `SourceActivationDecision` record (review record) |
| Rights or sensitivity rules | `policy/rights/` and `policy/sensitivity/` |
| Domain object meaning | `docs/domains/<domain>/` and `contracts/domains/<domain>/` |
| External standards (e.g., STAC, JSON Schema) | `docs/standards/` |

> [!IMPORTANT]
> **CONFIRMED rule (Directory Rules §7.3).** Connectors MUST NOT publish, mutate canonical truth, or write under `data/processed/`, `data/catalog/`, or `data/published/`. Connector output flows to `data/raw/<domain>/<source_id>/<run_id>/` or `data/quarantine/...`, with source descriptors, checksums, and ingest receipts. This entry's catalog status does not waive that boundary for any USGS sub-source.

---

## 5. Sub-source registry (catalog index)

The table below catalogs the USGS sub-sources KFM dossiers and the encyclopedia have **named** as in-scope. Sub-source identity, role(s), and feeding domains are CONFIRMED at the doctrine level. Per-sub-source **admission status** is **PROPOSED / NEEDS VERIFICATION** in every row — no row asserts that a connector or `SourceDescriptor` exists in the mounted repo.

| Sub-source | KFM short ID *(PROPOSED)* | Primary role(s) | Feeds domains | Admission status |
|---|---|---|---|---|
| **USGS Water Data APIs** (`api.waterdata.usgs.gov`) — successor to legacy WaterServices/NWIS | `usgs-water-data` | `observed` (gauges, sensor readings); `aggregate` (daily values, summaries) | Hydrology · Hazards (context) | PROPOSED — NEEDS VERIFICATION |
| **Watershed Boundary Dataset (WBD) / HUC** | `usgs-wbd` | `context` *(role-mapping note in §6)* / `administrative` (HUC accounting units) | Hydrology · Spatial Foundation · Agriculture · Habitat | PROPOSED — NEEDS VERIFICATION |
| **NHDPlus High Resolution (NHDPlus HR) / NHD / 3DHP** | `usgs-nhdplus-hr` | `context` (hydrography geometry); `modeled` (Value-Added Attributes such as cumulative drainage, mean annual flow/velocity, flow direction) | Hydrology · Spatial Foundation | PROPOSED — NEEDS VERIFICATION |
| **3D Elevation Program (3DEP)** — terrain, DEMs, LiDAR derivatives | `usgs-3dep` | `observed` (LiDAR returns); `modeled` (derived DEMs, hillshades, slope, contours) | Spatial Foundation · Hydrology · Hazards · Archaeology · Planetary/3D | PROPOSED — NEEDS VERIFICATION |
| **The National Map** — discovery/download platform | `usgs-tnm` | `aggregator` of program assets *(carrier; per-asset role applies)* | Spatial Foundation (cross-cutting) | PROPOSED — NEEDS VERIFICATION |
| **Geographic Names Information System (GNIS)** | `usgs-gnis` | `administrative` (official geographic names, populated places); `candidate` (historical identity ambiguity) | Settlements & Infrastructure · Spatial Foundation · People-DNA-Land · Roads-Rail-Trade | PROPOSED — NEEDS VERIFICATION |
| **USGS Science Data Catalog** — e.g., NHDPlus v2.1 COMID → WBD HU-12 crosswalk | `usgs-sdc` | `context` (crosswalks); `modeled` where derivation is documented | Hydrology (crosswalks) · cross-domain | PROPOSED — NEEDS VERIFICATION |
| **USGS Earthquakes** | `usgs-earthquakes` | `observed` (seismic events); `modeled` (PAGER, ShakeMap derivatives) | Hazards · Geology | PROPOSED — NEEDS VERIFICATION |
| **USGS Geologic Maps** | `usgs-geologic-maps` | `administrative` (compiled maps); `observed` where field surveys are first-party | Geology · Natural Resources | PROPOSED — NEEDS VERIFICATION |

> [!NOTE]
> **Source-role assignments above are PROPOSED at the descriptor level.** The Master Source-Role Anti-Collapse Register (Atlas v1.1 §24.1) requires that source role be set at admission on the `SourceDescriptor` and preserved through every promotion. Treat the rows above as a starting hypothesis for review, not as final descriptor values.

<details>
<summary><strong>USGS Water Data — current-API migration note (EXTERNAL: none; project-knowledge basis)</strong></summary>

The KFM `New_Ideas_5-8-26.pdf` packet records that the modern **USGS Water Data APIs** at `api.waterdata.usgs.gov` are replacing the legacy `waterservices.usgs.gov` (NWIS) endpoints, with the legacy surface in phase-out across 2026/2027. Any USGS Water Data `SourceDescriptor` SHOULD pin the modern endpoint, capture the legacy phase-out window as freshness/cadence context, and treat the cutover as a tracked migration. Live API surface and current terms remain **NEEDS VERIFICATION** at activation time.

</details>

---

## 6. Source-role posture (anti-collapse)

**CONFIRMED doctrine (Atlas v1.1 §24.1).** KFM treats `source_role` as a first-class identity attribute on every `SourceDescriptor`. The lifecycle and the governed API both fail closed when roles are conflated. For the USGS family, three anti-collapse patterns deserve specific attention:

| Anti-collapse risk | USGS context | Required guardrail |
|---|---|---|
| **Modeled product labeled as observed** | NHDPlus HR Value-Added Attributes (e.g., cumulative drainage, mean annual flow/velocity) are *derived*, not measured at each reach. 3DEP-derived DTMs, slope, hillshade, and SVF are *modeled* from LiDAR returns. | Carry `role_model_run_ref` on `SourceDescriptor`; preserve role through every transform; expose role in `EvidenceBundle`. |
| **Administrative compilation cited as observation** | GNIS entries and compiled geologic maps are *administrative compilations*, not first-hand observations of the named place at the cited time. | Cite as administrative context; never collapsed with observation. Use `LifeEvent` vs `AdminEvent` separation in People/Settlements lanes. |
| **Aggregate cited as per-place truth** | USGS Water Data daily-value or annual summaries are *aggregates* over time windows; some catalog products aggregate spatially. | `AggregationReceipt` with explicit `role_aggregation_unit`; DENY join from aggregate cell to single record; ABSTAIN at AI. |

> [!WARNING]
> **CONFIRMED rule.** A USGS dataset does **not** become regulatory simply by being federal. Regulatory flood-zone designations are FEMA NFHL — *not* USGS. Do not relabel USGS WBD/HUC, NHDPlus HR, or USGS Water Data observations as "regulatory" anywhere in this catalog or in any downstream `SourceDescriptor`.

---

## 7. Rights, sensitivity, freshness

| Posture | Default for the USGS family | Per-sub-source override required |
|---|---|---|
| **Rights / license** | Generally permissive for federal USGS open data | **NEEDS VERIFICATION** per dataset; capture license text and attribution requirement on each `SourceDescriptor`; unknown rights fail closed. |
| **Sensitivity** | Mostly low-sensitivity (terrain, hydrography, names, public observations) | Treat any precise location near a **deny-by-default class** (rare-species sites, archaeological coords, critical infrastructure, sacred/cultural places, living-person residence) as if it were sensitive: redact / generalize / deny by default until steward review. |
| **Freshness / cadence** | Highly source-vintage-specific (e.g., NHDPlus HR releases; 3DEP collection vintages; Water Data near-real-time vs daily values) | Record `cadence`, `retrieval_time`, and `stale-state` thresholds on each `SourceDescriptor`; surface stale/degraded badges on UI. |
| **Source-time vs observed-time vs retrieval-time** | All four hydrology temporal fields apply (observed, valid, source, retrieval, release time) | Keep distinct where material; ABSTAIN if material temporal scope is missing. |

> [!CAUTION]
> **CONFIRMED rule (Sensitive / Deny-by-Default Register).** USGS data is **not** automatically safe to publish at full precision. A USGS `observed` record near a rare species nest, archaeology coordinate, or sensitive infrastructure feature inherits the sensitivity of the joined object. The cross-source join, not the USGS feed alone, is what triggers `RedactionReceipt` and steward review.

---

## 8. Source admission flow

The diagram below reflects KFM's CONFIRMED source registry doctrine (Source registry architecture; Master Action Matrix; Lifecycle gates). The specific files, route names, and IDs labeled inside the nodes are **PROPOSED** until verified against the mounted repo.

```mermaid
flowchart TD
    A[USGS sub-source identified<br/>(this catalog entry)]:::doc
    B[SourceDescriptor draft<br/>schemas/contracts/v1/source/...<br/>data/registry/sources/&lt;domain&gt;/usgs-*.yaml]:::registry
    C{Review:<br/>role / rights / sensitivity /<br/>cadence / access}:::gate
    D[SourceActivationDecision<br/>allowed | restricted | denied | needs-review]:::gate
    E[connectors/usgs/&lt;sub-source&gt;/<br/>fetch + admit + receipts]:::code
    F[data/raw/&lt;domain&gt;/usgs-*/&lt;run_id&gt;/<br/>or data/quarantine/...]:::data
    G[pipelines/ingest -> normalize -> validate -> catalog]:::code
    H[data/processed -> data/catalog/domain/&lt;domain&gt;/]:::data
    I[EvidenceBundle resolution +<br/>release/candidates/&lt;domain&gt;/]:::gate
    J[data/published/layers/&lt;domain&gt;/<br/>ReleaseManifest + RollbackCard]:::published

    A --> B --> C -->|allowed / restricted| D --> E --> F --> G --> H --> I --> J
    C -->|denied / needs-review| K[Held: data/quarantine/<br/>or no connector activation]:::deny
    I -->|EvidenceRef cannot resolve| K

    classDef doc fill:#e8f0fe,stroke:#3367d6,color:#0b1f4d;
    classDef registry fill:#fef7e0,stroke:#b06000,color:#3d2400;
    classDef gate fill:#fce8e6,stroke:#a50e0e,color:#3d0a08;
    classDef code fill:#e6f4ea,stroke:#137333,color:#0a2e16;
    classDef data fill:#f1f3f4,stroke:#5f6368,color:#202124;
    classDef published fill:#e8eaf6,stroke:#3f51b5,color:#1a237e;
    classDef deny fill:#fff,stroke:#a50e0e,color:#a50e0e,stroke-dasharray: 4 2;
```

> [!NOTE]
> **PROPOSED diagram.** Paths inside nodes follow Directory Rules §5 and §12 patterns but are not verified against the mounted repo. If the repo names a path differently, raise a `docs/registers/DRIFT_REGISTER.md` entry; do not silently rename here.

---

## 9. Lifecycle hand-off

USGS sub-sources travel the standard KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

| Phase | What this catalog entry guarantees | What it does **not** guarantee |
|---|---|---|
| **RAW** | This page names the sub-source, its role hypothesis, and its lane fit. | That a connector exists, has run, or has emitted a `RawCaptureReceipt`. |
| **WORK / QUARANTINE** | Identifies the *kinds* of failures (rights unknown, sensitivity unresolved, schema mismatch, geometry invalid) that route a USGS payload to quarantine. | Any specific `QuarantineRecord` or its disposition. |
| **PROCESSED** | Notes that `TransformReceipt` and `ValidationReport` are required for any normalized USGS dataset. | That a normalized dataset exists. |
| **CATALOG / TRIPLET** | Notes that catalog closure requires resolvable `EvidenceRef` → `EvidenceBundle`. | Any `CatalogRecord` entry. |
| **PUBLISHED** | Notes that publication requires `ReleaseManifest`, review where required, and a `RollbackCard` target. | Any released layer or current release state. |

> [!IMPORTANT]
> **CONFIRMED invariant.** Promotion across these phases is a **governed state transition, not a file move.** Watchers may emit observations, receipts, and candidate decisions; they MUST NOT mutate catalog truth, publish directly, overwrite canonical records, or bypass review states.

---

## 10. Task list — readiness backlog

PROPOSED next steps to take this catalog entry from a doctrine-level page to an activated source family. None of the items below claims to already be done.

- [ ] **PROPOSED** — Create `docs/sources/README.md` as the lane landing page and link this catalog from it.
- [ ] **PROPOSED** — Create `docs/sources/SOURCE_DESCRIPTOR_STANDARD.md` (referenced in the Whole-UI Expansion Report) and link bidirectionally with this entry.
- [ ] **PROPOSED** — Open ADR if `docs/sources/catalog/` is to be canonized as the per-family page subfolder; otherwise note convention in `docs/sources/README.md`.
- [ ] **NEEDS VERIFICATION** — Confirm `schemas/contracts/v1/source/source_descriptor.schema.json` exists in the mounted repo; if not, defer descriptor authoring until the schema home is in place per ADR-0001.
- [ ] **PROPOSED** — For each row in §5, draft a `SourceDescriptor` instance under `data/registry/sources/<domain>/` once the schema is verified.
- [ ] **PROPOSED** — Stand up `connectors/usgs/<sub-source>/` skeletons with `README.md` declaring source descriptor reference, output target (`data/raw/...`), and ingest-receipt contract; keep them **inactive** until activation decision, fixtures, validators, and policy gates exist.
- [ ] **PROPOSED** — Author no-network fixtures (valid + invalid) under `tests/fixtures/<domain>/usgs-*/` and a connector-gate validator path.
- [ ] **PROPOSED** — Open `docs/registers/VERIFICATION_BACKLOG.md` entries for every row whose **Admission status** is currently `PROPOSED — NEEDS VERIFICATION`.
- [ ] **PROPOSED** — Surface the USGS Water Data legacy → modern API migration as a tracked drift entry with a freshness/cadence note.

---

## 11. FAQ

**Q. Why is USGS one entry, when it is really many programs?**
USGS is a single *source family* in the registry sense — one organizational identity, one stewardship surface, one rights/attribution starting point. Each program is a distinct `SourceDescriptor` with its own role, cadence, and sensitivity; this catalog page exists so reviewers can see the family at a glance before any one descriptor is admitted.

**Q. Can I treat NHDPlus HR Value-Added Attributes (VAAs) as "observed" because they live alongside the geometry?**
**No.** VAAs are *derived* — cumulative drainage, mean annual flow/velocity, and flow direction are computed from the network model. Use `source_role: modeled` with `role_model_run_ref` set, and never relabel them as observations downstream.

**Q. Is WBD/HUC a regulatory boundary?**
**No.** HUC accounting units are an administrative/topological framework, not a regulatory determination. Regulatory flood-zone authority is FEMA NFHL — a different source family. Do not collapse them in any USGS row.

**Q. Can a USGS Water Data gauge reading be published without further review?**
The doctrine answer is: **not without** a resolvable `EvidenceRef` → `EvidenceBundle`, a passing `ValidationReport`, a `PolicyDecision`, and a `ReleaseManifest`. The data being open does not waive the trust-membrane gates.

**Q. What about USGS data near sensitive features (rare species, archaeology, critical infrastructure)?**
The USGS feed is not the sensitivity source; the **join** is. Treat any precise join near a deny-by-default class as sensitive: apply `RedactionReceipt`, prefer generalization or staged access, and route through steward review.

**Q. Where does this page sit in the authority order?**
Below KFM core invariants, ADRs, and Directory Rules; above per-root READMEs only when no per-root README says otherwise. It is a *navigational* catalog, not an authoritative SourceDescriptor.

---

## 12. Related docs

- `docs/doctrine/directory-rules.md` — placement law, lifecycle invariant, anti-patterns.
- `docs/doctrine/lifecycle-law.md` *(PROPOSED canonical home)* — RAW → … → PUBLISHED.
- `docs/doctrine/truth-posture.md` *(PROPOSED canonical home)* — cite-or-abstain.
- `docs/doctrine/trust-membrane.md` *(PROPOSED canonical home)* — public clients use governed interfaces.
- `docs/sources/SOURCE_DESCRIPTOR_STANDARD.md` *(PROPOSED — referenced in the Whole-UI Expansion Report)*.
- `docs/standards/stac.md` *(TODO if not yet present)* — STAC profile and `kfm:evidence_bundle` embedding pattern for USGS-derived items.
- `docs/domains/hydrology/README.md` — primary downstream lane for USGS Water Data, WBD, NHDPlus HR.
- `docs/domains/spatial-foundation/README.md` *(PROPOSED short name)* — primary downstream lane for 3DEP, GNIS, TNM.
- `docs/domains/geology/README.md` — USGS geologic maps, earthquakes (with Hazards).
- `docs/domains/hazards/README.md` — USGS earthquakes, USGS Water (flood-context).
- `connectors/usgs/README.md` — connector home for the family.
- `schemas/contracts/v1/source/source_descriptor.schema.json` — descriptor shape (NEEDS VERIFICATION).
- `docs/adr/ADR-0001-schema-home.md` — schema-home rule under which descriptors live.

---

## 13. Appendix — schema field hooks

**PROPOSED** mapping from this catalog entry to fields a `SourceDescriptor` should carry (illustrative, not authoritative; the canonical shape is whatever `schemas/contracts/v1/source/source_descriptor.schema.json` defines once verified).

<details>
<summary><strong>Descriptor field hooks (PROPOSED — derived from Atlas v1.1 §24.1.3)</strong></summary>

```yaml
# illustrative SourceDescriptor instance fragment — PROPOSED, not validated
source_id: usgs-water-data           # PROPOSED short ID
source_family: usgs                  # this catalog page
source_role: observed                # one of: observed | regulatory | modeled |
                                     #         aggregate | administrative |
                                     #         candidate | synthetic
role_authority: "U.S. Geological Survey, Water Mission Area"   # required when role
                                                               # in {regulatory, modeled, aggregate}
role_aggregation_unit: null          # required when source_role = aggregate
role_model_run_ref: null             # required when source_role = modeled
role_synthetic_basis: null           # required when source_role = synthetic
role_candidate_disposition: null     # required when source_role = candidate

access:
  endpoint: "https://api.waterdata.usgs.gov/"      # NEEDS VERIFICATION at activation
  legacy_endpoint: "https://waterservices.usgs.gov/"   # phase-out 2026/2027 per New Ideas packet
  auth: none
rights:
  license: "TODO — NEEDS VERIFICATION"
  attribution_required: "TODO"
sensitivity:
  default_class: low
  join_sensitivity_inherits: true    # join near deny-by-default class -> sensitive
cadence:
  observation: near-real-time
  daily_values: T+1 day
  stale_thresholds: "TODO"
temporal:
  observed_time: required
  valid_time: required
  source_time: required
  retrieval_time: required
  release_time: required
steward:
  contact: "TODO"
release_class: "TODO — public | restricted | denied"
```

Field names follow the Atlas v1.1 §24.1.3 PROPOSED descriptor surface; **NEEDS VERIFICATION** against the mounted `source_descriptor.schema.json`.

</details>

<details>
<summary><strong>Cross-domain feed map (CONFIRMED at the encyclopedia / dossier level)</strong></summary>

| Domain | USGS sub-sources cited in dossiers |
|---|---|
| **Hydrology** | USGS Water Data APIs · WBD/HUC · NHDPlus HR / 3DHP · 3DEP terrain |
| **Spatial Foundation, Cartography, Reference Systems** | USGS 3DEP · The National Map · GNIS |
| **Geology and Natural Resources** | USGS geologic maps · 3DEP terrain |
| **Hazards** | USGS earthquakes · USGS Water (context) |
| **Roads, Rail, and Trade Routes** | GNIS · Census/TIGER joins |
| **Settlements, Cities, and Infrastructure** | GNIS · Census/TIGER · The National Map |
| **Archaeology and Cultural Heritage** | 3DEP-derived LiDAR (with sensitivity guards) |
| **Planetary, 3D, Digital Twin, and Synthetic Spatial Systems** | USGS 3DEP · LiDAR collections |
| **Agriculture (context)** | WBD/HUC for irrigation/water linkages |

Citations: KFM Encyclopedia Master Domain Atlas (§5) and Appendix D Source family index; KFM Domains Culmination Atlas v1.1 (Hydrology, Spatial Foundation, Geology, Hazards, Planetary/3D sections).

</details>

<details>
<summary><strong>Anti-collapse failure modes for this family (CONFIRMED doctrine)</strong></summary>

| Failure mode | Specific USGS risk | Required guardrail |
|---|---|---|
| Modeled labeled as observed | NHDPlus HR VAAs; 3DEP-derived rasters | `role_model_run_ref`; uncertainty surface; role-preserving DTO |
| Administrative cited as observation | GNIS entries; compiled geologic maps | Source-role tag preserved; named `LifeEvent` / `AdminEvent` types |
| Aggregate cited as per-place truth | Daily-value / annual-summary water data | `AggregationReceipt` with `role_aggregation_unit`; matrix-cell semantics |
| Candidate exposed on public surface | Unresolved crosswalk rows (e.g., alignment_score &lt; threshold) | Promotion gate; no PUBLISHED edge from WORK/QUARANTINE |
| Synthetic presented as observed | Synthetic terrain surfaces derived from 3DEP | Reality Boundary Note; Representation Receipt; UI badge |

</details>

---

> [!NOTE]
> **Authority caveat.** This page is a navigational catalog. The canonical sources of truth for any claim about USGS sub-sources in KFM remain: KFM doctrine, accepted ADRs, the `SourceDescriptor` schema and instances, and the relevant `EvidenceBundle`. Where this page conflicts with any of those, this page is the one that must change.

---

**Related:** [Directory Rules](../../../doctrine/directory-rules.md) · [Source Descriptor Standard](../../SOURCE_DESCRIPTOR_STANDARD.md) *(PROPOSED)* · [USGS Connector README](../../../../connectors/usgs/README.md) *(PROPOSED)* · [Hydrology Domain](../../../domains/hydrology/README.md)

**Last updated:** 2026-05-13

[Back to top](#usgs--source-family-catalog-entry)
