<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs/domains/roads-rail-trade/SOURCE_REGISTRY
title: Roads / Rail / Trade Routes — Source Registry
type: standard
version: v1
status: draft
owners: <Roads/Rail/Trade domain steward — TODO>
created: 2026-05-19
updated: 2026-05-19
policy_label: public
related:
  - docs/doctrine/directory-rules.md
  - docs/atlases/KFM_Domains_Culmination_Atlas_v1_1.pdf
  - docs/standards/PROV.md
  - schemas/contracts/v1/source/source-descriptor.json
  - data/registry/sources/roads-rail-trade/
  - policy/domains/roads-rail-trade/
tags: [kfm, roads-rail-trade, source-registry, governance, doctrine]
notes:
  - Domain-scoped source registry doctrine; the machine-readable registry lives under data/registry/sources/roads-rail-trade/.
  - All implementation-layer paths are PROPOSED until verified against a mounted repo.
[/KFM_META_BLOCK_V2] -->

# Roads / Rail / Trade Routes — Source Registry

> Governed admission, role, rights, sensitivity, and freshness doctrine for every source that may enter the Roads / Rail / Trade Routes lane.

<!-- Badges -->

![status: draft](https://img.shields.io/badge/status-draft-yellow)
![doc type: standard](https://img.shields.io/badge/doc-standard-blue)
![domain: roads--rail--trade](https://img.shields.io/badge/domain-roads--rail--trade-1f6feb)
![lifecycle: RAW%20%E2%86%92%20PUBLISHED](https://img.shields.io/badge/lifecycle-RAW%20%E2%86%92%20PUBLISHED-3a3a3a)
![governance: deny--by--default](https://img.shields.io/badge/governance-deny--by--default-red)
![directory rules: v1.1](https://img.shields.io/badge/directory_rules-v1.1-555)
<!-- TODO: Replace with real CI / release / freshness endpoints once available -->
![CI: TODO](https://img.shields.io/badge/CI-TODO-lightgrey)
![last updated: 2026--05--19](https://img.shields.io/badge/last_updated-2026--05--19-informational)

**Status:** draft · **Owners:** Roads/Rail/Trade domain steward _(TODO)_ · **Last updated:** 2026-05-19

---

## Contents

1. [Purpose](#1-purpose)
2. [Repo fit](#2-repo-fit)
3. [Authority and scope](#3-authority-and-scope)
4. [Source admission flow](#4-source-admission-flow)
5. [Source families (CONFIRMED dossier list)](#5-source-families-confirmed-dossier-list)
6. [Source-role taxonomy (cross-cutting doctrine)](#6-source-role-taxonomy-cross-cutting-doctrine)
7. [SourceDescriptor surface](#7-sourcedescriptor-surface)
8. [Sensitivity, rights, and publication posture](#8-sensitivity-rights-and-publication-posture)
9. [Anti-collapse rules for this domain](#9-anti-collapse-rules-for-this-domain)
10. [Pipeline shape (RAW → PUBLISHED)](#10-pipeline-shape-raw--published)
11. [Validators, tests, and fixtures (PROPOSED)](#11-validators-tests-and-fixtures-proposed)
12. [Cross-lane source impact](#12-cross-lane-source-impact)
13. [Registry directory layout (PROPOSED)](#13-registry-directory-layout-proposed)
14. [Open verification backlog](#14-open-verification-backlog)
15. [Related docs](#15-related-docs)
16. [Appendix — historic and trade-corridor sources](#16-appendix--historic-and-trade-corridor-sources)

---

## 1. Purpose

This document is the **human-facing source registry doctrine** for the Roads / Rail / Trade Routes domain. It defines:

- **What** counts as a source for this lane.
- **How** a source is admitted, classified by role, rights-checked, sensitivity-checked, and either activated, restricted, quarantined, denied, or held for review.
- **Where** descriptors and registry entries live in the repository.
- **Which guardrails** prevent role-collapse failure modes that this lane is doctrinally at risk of (notably *administrative compilation cited as observation*).

> [!IMPORTANT]
> CONFIRMED doctrine: the KFM source registry is an **admission and authority-control surface**, not a bibliography. It governs whether material may shape public claims — not merely whether it can be cited. [BLD-GREEN §9; IMPL-PIPE §13; BLD-COMP §8; [KFM Unified Implementation Architecture Build Manual](../../atlases/) §3.6]

The companion **machine-readable registry** for this lane lives at `data/registry/sources/roads-rail-trade/` per Directory Rules §12. This document does **not** replace that data; it explains the rules the data must obey.

---

## 2. Repo fit

| Aspect | Value | Status |
|---|---|---|
| Responsibility root | `docs/` (human-facing control plane) | CONFIRMED rule [DIRRULES §5–6] |
| Domain segment | `docs/domains/roads-rail-trade/` | CONFIRMED rule [DIRRULES §12] |
| File path | `docs/domains/roads-rail-trade/SOURCE_REGISTRY.md` | PROPOSED — NEEDS VERIFICATION against mounted repo |
| Machine-readable companion | `data/registry/sources/roads-rail-trade/` | PROPOSED per [DIRRULES §12] |
| Canonical descriptor schema home | `schemas/contracts/v1/source/source-descriptor.json` per ADR-0001 | PROPOSED — NEEDS VERIFICATION |
| Sensitivity policy bundle | `policy/domains/roads-rail-trade/` | PROPOSED per [DIRRULES §12] |
| Connector home | `connectors/` (output → `data/raw/roads-rail-trade/` or `data/quarantine/roads-rail-trade/`) | CONFIRMED rule [DIRRULES §5] |

**Upstream doctrine sources (CONFIRMED):**
- `docs/doctrine/directory-rules.md` — placement law.
- KFM Domains Culmination Atlas, v1.1, ch. 13 (Roads / Rail / Trade Routes) — domain dossier.
- KFM Domains Culmination Atlas, v1.1, §24.1 (Master Source-Role Anti-Collapse Register) — cross-cutting role taxonomy.
- KFM Unified Implementation Architecture Build Manual §3.6 — source registry architecture.

**Downstream consumers (PROPOSED):**
- `connectors/` admitters for each source family.
- `pipelines/domains/roads-rail-trade/` normalization stages.
- `policy/domains/roads-rail-trade/` admission and publication gates.
- `data/published/layers/roads-rail-trade/` public-safe releases.
- `apps/governed-api/` Roads/Rail decision envelopes (route TBD).

---

## 3. Authority and scope

### 3.1 What this registry governs

CONFIRMED dossier scope: sources that contribute evidence about Kansas **roads, rail, historic routes, trade and mobility corridors, restrictions, facilities, graph projections**, and the catalog / proof / release objects derived from them. [DOM-ROADS; ENCY]

### 3.2 What this registry does NOT govern

CONFIRMED non-ownership (from the domain dossier):
- **Settlements / Infrastructure** owns settlement and infrastructure canonical claims (depots, yards, and crossings cite Settlements where applicable).
- **Hydrology** owns water evidence (bridge / ferry / ford evidence cites Hydrology).
- **Archaeology / People / Land / Hazards** retain their truth and sensitivity policies. [DOM-ROADS]

> [!NOTE]
> A source that primarily evidences a settlement, a watercourse, an archaeological site, or a person is admitted by the **owning lane**, not by Roads/Rail/Trade — even if it has incidental transport content. Roads/Rail/Trade then *cites* it through a governed join.

### 3.3 Conflict resolution

When this document and another source disagree, apply Directory Rules §2.1 authority order:

1. KFM core invariants and doctrine (lifecycle law, cite-or-abstain, trust membrane).
2. Accepted ADRs that explicitly amend Directory Rules.
3. `docs/doctrine/directory-rules.md`.
4. Per-root READMEs (refine, never contradict).
5. Domain dossiers and prior architecture reports (lineage / proposed).
6. Mounted-repo convention (raise as `docs/registers/DRIFT_REGISTER.md`, not new authority). [DIRRULES §2.1]

---

## 4. Source admission flow

CONFIRMED doctrine + PROPOSED implementation: every Roads/Rail/Trade source passes the same governed admission pipeline. Connectors and watchers remain **inactive** until each gate has resolved. [BLD-COMP §§8.1–8.2; IMPL-PIPE §13]

```mermaid
flowchart TD
  A["Candidate source<br/>identified"] --> B["Draft<br/>SourceDescriptor<br/>(identity, role, rights,<br/>cadence, steward,<br/>sensitivity)"]
  B --> C{Rights &<br/>terms gate}
  C -- denied --> X1["DENY<br/>(record reason)"]
  C -- restricted --> R1["Restricted use<br/>(record terms)"]
  C -- allowed --> D{Source-role<br/>classification}
  D -- observed/regulatory/modeled<br/>aggregate/administrative<br/>candidate/synthetic --> E{Sensitivity gate<br/>(Indigenous corridors,<br/>critical facilities)}
  E -- denied --> X2["DENY / HOLD for<br/>steward review"]
  E -- restricted --> R2["Generalize / redact<br/>(emit RedactionReceipt)"]
  E -- allowed --> F["Issue<br/>SourceActivationDecision<br/>(allowed | restricted |<br/>denied | needs-review)"]
  R1 --> F
  R2 --> F
  F --> G["Connector / watcher<br/>activated"]
  G --> H["RAW capture<br/>(immutable, hashed,<br/>cited)"]
  H --> I["WORK / QUARANTINE<br/>→ PROCESSED<br/>→ CATALOG / TRIPLET<br/>→ PUBLISHED"]
  X1 --> Z["Registry entry<br/>(DENY rationale,<br/>review path)"]
  X2 --> Z
```

<sub>**NEEDS VERIFICATION:** This flowchart reflects CONFIRMED doctrine. The actual gate identities, decision DTOs, and route names in a mounted repo remain PROPOSED until inspected.</sub>

### 4.1 Required outputs of admission (PROPOSED shape)

| Output | Purpose | Required content (PROPOSED) |
|---|---|---|
| `SourceDescriptor` | Anchors every downstream receipt. | `source_id`, `source_role`, `authority`, `rights`, `sensitivity`, `cadence`, ingest hash, time, citation. [ENCY; DIRRULES] |
| `SourceActivationDecision` | Gate record. | Outcome ∈ { allowed, restricted, denied, needs-review }, rationale, reviewer, expiry. [BLD-COMP §8.1–8.2] |
| Drift / verification entry (when applicable) | Tracks open questions. | Entry in `docs/registers/DRIFT_REGISTER.md` or `docs/registers/VERIFICATION_BACKLOG.md`. [DIRRULES §2.5] |

---

## 5. Source families (CONFIRMED dossier list)

CONFIRMED list (from KFM Domains Culmination Atlas v1.1, ch. 13 §D); **role**, **rights / sensitivity**, and **freshness** are intentionally generic in the dossier — they MUST be resolved per-source at admission, not assumed.

| # | Source family | Typical role(s) | Rights / sensitivity | Freshness | Status |
|---|---|---|---|---|---|
| 1 | **Census TIGER/Line — roads** | administrative / observation (geometry context); never observation of facility *condition* | Public-domain assumed; NEEDS VERIFICATION of current terms | Annual vintage | CONFIRMED family / PROPOSED admission |
| 2 | **FHWA HPMS** | administrative (network extent) / regulatory (functional classification, NHS) | Federal release; NEEDS VERIFICATION of redistribution and detail tiers | Annual submission cycle (NEEDS VERIFICATION) | CONFIRMED family / PROPOSED admission |
| 3 | **FHWA National Highway Freight Network** | regulatory (designations); administrative (network roster) | Federal release; NEEDS VERIFICATION of attribution requirements | Periodic; NEEDS VERIFICATION | CONFIRMED family / PROPOSED admission |
| 4 | **WZDx feeds** (Work-Zone Data Exchange) | observation (active work-zone events) | Variable per producer; NEEDS VERIFICATION per feed | Near-real-time; cadence per producer | CONFIRMED family / PROPOSED admission |
| 5 | **KDOT / KanPlan / KanDrive / Kansas GIS** | authority (state-route designation), observation (status), administrative (asset rosters) | State agency terms; NEEDS VERIFICATION per dataset | Mixed; NEEDS VERIFICATION | CONFIRMED family / PROPOSED admission |
| 6 | **County / state bridge and restriction data** | regulatory (posted restrictions) / administrative (inventories) | County / state; rights vary; NEEDS VERIFICATION | Mixed; NEEDS VERIFICATION | CONFIRMED family / PROPOSED admission |
| 7 | **GNIS names** | administrative (named features) | Public-domain assumed; NEEDS VERIFICATION | Periodic | CONFIRMED family / PROPOSED admission |
| 8 | **OpenStreetMap** | candidate / context (community-contributed) | ODbL — attribution and share-alike obligations apply; NEEDS VERIFICATION of joinability with non-ODbL outputs | Continuous; cadence per importer | CONFIRMED family / PROPOSED admission; **never an authority** for legal status [DOM-ROADS K. validator backlog] |

> [!CAUTION]
> **OSM / GNIS legal-status denial** is a PROPOSED test in the domain validator backlog. OSM and GNIS may evidence *presence and name* but MUST NOT be cited as authority for *legal designation* (route number, functional class, designated freight corridor, etc.). [DOM-ROADS §K; ENCY]

### 5.1 Historic and trade-corridor sources (PROPOSED)

The dossier names historic and trade-corridor evidence (Santa Fe Trail, Pony Express, Butterfield/Smoky Hill, military / mail / emigrant / stage / cattle corridors) as in scope for this lane. The corpus identifies a **PROPOSED** "Frontier routes FeatureCollection" deliverable (KFM-P20-PROG-0013, Pass 32). The source families that feed these — historic maps, GLO plats, military reports, archival narratives, Indigenous oral history — are not yet enumerated in the dossier as a single registry list and are tracked as **NEEDS VERIFICATION** in §14 below. See [Appendix — historic and trade-corridor sources](#16-appendix--historic-and-trade-corridor-sources).

---

## 6. Source-role taxonomy (cross-cutting doctrine)

CONFIRMED doctrine: KFM treats **source role as a first-class identity attribute** and fails closed when roles are conflated. The seven canonical roles are listed below; full doctrine lives in Atlas v1.1 §24.1. [ENCY §24.1]

| Role | One-line definition | Roads/Rail/Trade examples |
|---|---|---|
| **Observed** | First-hand reading / measurement / record tied to place and time. | A WZDx work-zone event message; a traffic counter reading; a field-observed bridge inspection note. |
| **Regulatory** | Authoritative determination by a regulating body with legal/administrative force. | NHS designation; designated freight corridor; posted weight restriction; railroad operating rights. |
| **Modeled** | Derived from inputs, assumptions, fitted parameters. | Travel-time model output; derived transport graph; freight-flow estimate. |
| **Aggregate** | Published summary over a unit (county, year, corridor). | County VMT total; annual segment AADT (when only aggregate); freight-flow corridor totals. |
| **Administrative** | Compiled agency record for administration, registration, accounting. | TIGER/Line geometry; HPMS submission rows; county bridge inventory; **transport facility roster**. [§24.1.1] |
| **Candidate** | Awaiting validation / dedup / steward review. | Unmerged OSM way claim; unresolved historic-route alignment; quarantined connector output. |
| **Synthetic** | Generated by simulation, reconstruction, AI, interpolation. | Reconstructed historic alignment; AI-drafted summary of a corridor EvidenceBundle. |

> [!IMPORTANT]
> The dossier explicitly flags **Roads** as a domain at risk of the *"administrative compilation cited as observation"* collapse pattern. TIGER/Line geometry, HPMS rows, and facility rosters are **administrative**; presenting them as an *observed event timeline* is **DENIED** at publication. [Atlas v1.1 §24.1.2]

---

## 7. SourceDescriptor surface

PROPOSED descriptor shape (illustrative — the canonical schema is owned by `schemas/contracts/v1/source/source-descriptor.json` per ADR-0001; field names below are NEEDS VERIFICATION against the mounted schema). [Atlas v1.1 §24.1.3]

<details>
<summary>Field reference (click to expand)</summary>

| Field | Type / vocabulary | Required? | Notes |
|---|---|---|---|
| `source_id` | string (stable, opaque) | MUST | Never reused; corrections produce a new descriptor with `superseded_by`. |
| `source_role` | enum: observed \| regulatory \| modeled \| aggregate \| administrative \| candidate \| synthetic | MUST | Set at admission; never edited in place. [§24.1.3] |
| `role_authority` | string (issuing body / model identity / steward) | MUST when role ∈ {regulatory, modeled, aggregate} | Disambiguates downstream cite text. |
| `role_aggregation_unit` | geometry-scope token (county, HUC, corridor, year, decade, …) | MUST when `source_role = aggregate` | Prevents geometry-scope drift on join. |
| `role_model_run_ref` | EvidenceRef → ModelRunReceipt | MUST when `source_role = modeled` | Pins inputs, parameters, version. |
| `role_synthetic_basis` | `{ method, inputs, reality_boundary_note_ref }` | MUST when `source_role = synthetic` | Records what is / is not real. |
| `role_candidate_disposition` | enum: pending \| merged \| rejected \| quarantined | MUST when `source_role = candidate` | PUBLISHED edge forbidden until merged. |
| `authority` | string | MUST | Agency / project / community of record. |
| `rights` | structured `{ license, attribution, redistribution, endpoint_terms }` | MUST | Drives the rights-and-terms gate. [KFM-P1-PROG-0032] |
| `sensitivity` | structured (tier + tags) | MUST | Resolves Indigenous-corridor, critical-facility, and other lane defaults. |
| `cadence` | structured `{ expected_period, freshness_tolerance }` | MUST | Feeds stale-state markers. [Atlas §24.8.1] |
| `access_method` | enum (api \| download \| feed \| archival \| derived) | MUST | Constrains connector design. |
| `steward` | string / kfm:// id | MUST | Named human / role for review. |
| `release_class` | enum (public \| restricted \| internal-only \| denied) | MUST | Anchors publication eligibility. |
| `ingest_hash` | digest | MUST | Pins the admitted payload. |
| `time` | structured (admitted, retrieved, valid-from, valid-to) | MUST | KFM's source / observed / valid / retrieval / release / correction distinction. |
| `citation` | string | MUST | Reader-facing attribution. |
| `superseded_by` | source_id \| null | OPTIONAL | Supersession lineage. |

</details>

---

## 8. Sensitivity, rights, and publication posture

CONFIRMED / PROPOSED (from the domain dossier):

- **Indigenous trade and mobility corridors**, oral history, treaty, cultural, and interpretive evidence **default to steward review and generalized public geometry**. [DOM-ROADS §I]
- **Critical transport facilities** require steward review before any precise-geometry public release. [DOM-ROADS §I]
- **Unclear rights, unresolved source role, missing evidence, unresolved sensitivity, or absent release state blocks public promotion.** This is a CONFIRMED operating invariant. [ENCY; DIRRULES]

| Trigger | Default posture | Required artifact |
|---|---|---|
| Indigenous corridor or oral-history evidence | Steward review; geometry generalized for public surfaces | RedactionReceipt + ReviewRecord |
| Living-person operator data in a feed | Strip / quarantine living-person fields | RedactionReceipt |
| Precise critical-facility geometry (bridge load posting, tunnel detail, hazardous-route detail) | HOLD for steward review; release only generalized public form | ReviewRecord + RedactionReceipt |
| Historic alignment with uncertain provenance | Source role = `candidate` until steward review; never `observed` | SourceActivationDecision = needs-review |
| Rights terms ambiguous | DENY admission until resolved | DENY decision recorded; no connector activation |

> [!WARNING]
> **No PUBLISHED edge** is permitted from material that has not cleared the rights, sensitivity, and release-state gates — regardless of source family. This is enforced by the trust membrane, not by the connector author. [ENCY; DIRRULES]

---

## 9. Anti-collapse rules for this domain

CONFIRMED guardrails the Roads/Rail/Trade lane MUST observe (Atlas v1.1 §24.1.2):

| Collapse pattern | Denied outcome | Required guardrail |
|---|---|---|
| **Administrative compilation cited as observation** (e.g., TIGER/Line geometry treated as a *segment was observed open on date X*) | DENY publication of compilation as observed event timeline. | Source-role tag preserved through every promotion; named `RouteEvent` / `RestrictionEvent` / `OperatorAssignment` types distinct from base geometry. [§24.1.2] |
| **Regulatory designation treated as an observed event** (e.g., NHS designation treated as a *historic event timeline* rather than a regulatory state) | DENY at publication. | Separate regulatory-state lane from observed-event lane. |
| **Modeled graph projection treated as canonical record** (e.g., a derived transport graph standing in for source segments) | DENY publication; ABSTAIN at AI surface. | Run receipt + role-preserving DTO; routing/traversal graphs MUST NOT replace canonical records. [Unified Manual §6.8] |
| **Aggregate cited as per-place truth** (e.g., a corridor-total cited as a per-segment fact) | DENY join from aggregate cell to single record. | AggregationReceipt; geometry-scope guard. |
| **Candidate exposed publicly** (e.g., OSM way exposed as authoritative legal status) | DENY at trust membrane; route to QUARANTINE. | Promotion gate; no PUBLISHED edge from WORK / QUARANTINE. |
| **AI text treated as evidence** (e.g., a Focus-Mode answer about a historic route presented as the route's evidence) | DENY publication; ABSTAIN at Focus Mode. | AIReceipt mandatory; cite-or-abstain rule. [GAI] |

---

## 10. Pipeline shape (RAW → PUBLISHED)

CONFIRMED doctrine / PROPOSED lane application — Roads/Rail/Trade observes the standard lifecycle invariant; promotion is a **governed state transition, not a file move**. [DIRRULES; DOM-ROADS §H]

| Stage | Handling | Gate | Status |
|---|---|---|---|
| **RAW** | Capture immutable source payload or reference with source role, rights, sensitivity, citation, time, hash. | `SourceDescriptor` exists. | PROPOSED |
| **WORK / QUARANTINE** | Normalize schema, geometry, time, identity, evidence, rights, policy; hold failures. | Validation + policy gate pass, **or** quarantine reason recorded. | PROPOSED |
| **PROCESSED** | Emit validated normalized objects, receipts, public-safe candidates. | `EvidenceRef`, `ValidationReport`, digest closure. | PROPOSED |
| **CATALOG / TRIPLET** | Emit catalog records, EvidenceBundles, graph/triplet projections, release candidates. | Catalog / proof closure passes. | PROPOSED |
| **PUBLISHED** | Serve released public-safe artifacts through governed APIs and manifests. | `ReleaseManifest`, correction path, rollback target, review/policy state exist. | PROPOSED |

---

## 11. Validators, tests, and fixtures (PROPOSED)

PROPOSED validator slate from the domain dossier [DOM-ROADS §K]:

- Route membership and designation separation tests.
- Operator / status temporal tests.
- **OSM / GNIS legal-status denial** test (see [§5](#5-source-families-confirmed-dossier-list)).
- Historic-route overprecision denial.
- Public generalization receipt tests.
- Transport graph projection rollback tests.

All PROPOSED until verified against `tests/domains/roads-rail-trade/` and `fixtures/domains/roads-rail-trade/` in a mounted repo. Cross-domain validators (e.g., source-role anti-collapse) live in non-domain segments per Directory Rules §12 "Multi-domain and cross-cutting files."

---

## 12. Cross-lane source impact

Sources admitted here can be **cited** by other lanes through governed joins, but **ownership** is preserved (a Roads source does not become a Hydrology source by virtue of touching a river crossing).

```mermaid
flowchart LR
  R["Roads / Rail / Trade<br/>SourceRegistry"] -- depots, crossings, facilities --> S["Settlements /<br/>Infrastructure"]
  R -- bridges, ferries, fords --> H["Hydrology"]
  R -- closures, detours,<br/>exposure context --> Z["Hazards"]
  R -- historic routes, Indigenous corridors,<br/>forts, missions --> A["Archaeology /<br/>Cultural Heritage"]
  S -. canonical settlement claims .-> R
  H -. canonical water evidence .-> R
  A -. cultural sensitivity policy .-> R
```

<sub>CONFIRMED relations from DOM-ROADS §F; each preserves ownership, source role, sensitivity, and EvidenceBundle support.</sub>

---

## 13. Registry directory layout (PROPOSED)

Per Directory Rules §12 (Domain Placement Law), the Roads/Rail/Trade registry materializes across lanes — not as a root folder.

```text
docs/domains/roads-rail-trade/
└── SOURCE_REGISTRY.md           # this file (doctrine; human-facing)

data/registry/sources/roads-rail-trade/
├── README.md                    # PROPOSED
├── <source_id>.json             # PROPOSED — one descriptor per admitted source
└── activations/
    └── <source_id>.<ts>.json    # PROPOSED — SourceActivationDecision records

schemas/contracts/v1/source/
└── source-descriptor.json       # canonical schema home (per ADR-0001); NEEDS VERIFICATION

policy/domains/roads-rail-trade/
├── rights.rego                  # PROPOSED — rights-and-terms gate
├── sensitivity.rego             # PROPOSED — Indigenous-corridor, critical-facility rules
└── role-anti-collapse.rego      # PROPOSED — references cross-cutting policy

connectors/
└── <one folder per source family>   # output → data/raw/roads-rail-trade/ or data/quarantine/roads-rail-trade/

tests/domains/roads-rail-trade/
└── source-registry/             # PROPOSED — validator suite (see §11)
```

> [!NOTE]
> Every path above is **PROPOSED** until verified against a mounted repository. The **rule** (responsibility-rooted placement, domain as segment) is CONFIRMED; the **specific files** are not. [DIRRULES §12]

---

## 14. Open verification backlog

| # | Item | Evidence that would settle it | Status |
|---|---|---|---|
| OPEN-RR-SR-01 | Verify the current terms and redistribution posture of each of the 8 CONFIRMED source families (esp. TIGER, HPMS, NHFN, WZDx, KDOT, county data, GNIS, OSM). | Source endpoint pages; license headers in delivered artifacts; agency communications. | NEEDS VERIFICATION [DOM-ROADS §D] |
| OPEN-RR-SR-02 | Enumerate the historic / trade-corridor source families (Santa Fe Trail, Pony Express, Butterfield/Smoky Hill, GLO plats, military reports, Indigenous oral-history sources) into descriptor entries with role, rights, sensitivity, and steward. | A `data/registry/sources/roads-rail-trade/` listing reviewed by the domain steward. | NEEDS VERIFICATION [Pass-20 KFM-P20-PROG-0013] |
| OPEN-RR-SR-03 | Confirm the canonical `SourceDescriptor` schema path and field names against the mounted schema; surface drift via `docs/registers/DRIFT_REGISTER.md`. | Inspection of `schemas/contracts/v1/source/source-descriptor.json`. | NEEDS VERIFICATION [DIRRULES §7.4 / ADR-0001] |
| OPEN-RR-SR-04 | Confirm the policy bundle home for this lane: `policy/domains/roads-rail-trade/` vs. compatibility `policies/`. | Inspection of `policy/` and `policies/`. | NEEDS VERIFICATION [DIRRULES §5 per-root table] |
| OPEN-RR-SR-05 | Implement `SourceActivationDecision` records and link them from descriptors. | Sample activation files; tests asserting connector inactivation absent activation. | PROPOSED [BLD-COMP §8.1–8.2] |
| OPEN-RR-SR-06 | Implement OSM / GNIS legal-status denial test in `tests/domains/roads-rail-trade/`. | Failing fixture asserting deny; CI workflow citing the rule. | PROPOSED [DOM-ROADS §K] |
| OPEN-RR-SR-07 | Implement historic-overprecision denial test. | Fixture + receipt asserting generalization. | PROPOSED [DOM-ROADS §K] |
| OPEN-RR-SR-08 | Decide whether `data/registry/<domain>/` (Directory Rules §3 Step 3) or `data/registry/sources/<domain>/` (Directory Rules §12) is the canonical home for source descriptors. Both phrasings appear in Directory Rules; an ADR or per-root README should resolve. | Per-root `data/registry/README.md` or accepted ADR. | NEEDS VERIFICATION — log to `docs/registers/DRIFT_REGISTER.md` if conflict persists. |

[⬆ Back to top](#contents)

---

## 15. Related docs

- `docs/doctrine/directory-rules.md` — canonical placement law. [CONFIRMED]
- `docs/atlases/KFM_Domains_Culmination_Atlas_v1_1.pdf` — ch. 13 (Roads/Rail/Trade) and §24.1 (Source-Role Anti-Collapse). [CONFIRMED]
- `docs/standards/PROV.md` — provenance standard (naming variance `PROV.md` vs `PROVENANCE.md` tracked in OPEN-DR-01). [CONFIRMED authored; NEEDS VERIFICATION in repo]
- `docs/standards/SENSITIVITY_RUBRIC.md` — sensitivity tier rubric. [PROPOSED in corpus; not yet authored]
- `docs/standards/SIGNING.md` — descriptor / receipt signing posture. [PROPOSED in corpus; not yet authored]
- `docs/sources/README.md` — source-descriptor standards and source-family doctrine. [PROPOSED — TODO link to existing README once verified]
- `docs/architecture/contract-schema-policy-split.md` — why contracts / schemas / policy are separate roots. [CONFIRMED in Directory Rules `related`]
- `docs/runbooks/roads-rail-trade/SOURCE_REFRESH_RUNBOOK.md` — operational refresh procedure. [PROPOSED — patterned after `docs/runbooks/fauna/SOURCE_REFRESH_RUNBOOK.md`; runbook-subfolder convention pending OPEN-DR-02]

---

## 16. Appendix — historic and trade-corridor sources

<details>
<summary>Provisional list (PROPOSED; not yet in the dossier source-family table)</summary>

The Atlas names — but does not enumerate as registry entries — the following historic and trade-corridor evidence streams. They are listed here as PROPOSED candidates pending steward review (OPEN-RR-SR-02).

- **National Park Service** trail descriptions (Santa Fe National Historic Trail, Pony Express NHT, Oregon NHT segments through Kansas).
- **GLO (General Land Office) plats and field notes** — administrative geometry, NOT observed events.
- **State and county historical society holdings** — typically `candidate` or `administrative` until steward review.
- **Kansas Memory and Kansas Historical Society collections** — see Pass 18 `KFM-P18-PROG-0033 — Kansas Memory source descriptor`.
- **Military post and route reports** — `observed` (eyewitness narratives) or `administrative` (compilations), case-by-case.
- **Indigenous oral-history sources and tribal historic preservation offices** — **MUST** route through CARE / sovereignty review; **default to steward review and generalized geometry** per [§8](#8-sensitivity-rights-and-publication-posture).
- **Historic cartography** (e.g., Frémont, Pacific Railroad Surveys, Sanborn maps where transport-relevant) — typically `administrative` or `candidate`; never `observed` of present-day condition.
- **Cattle-trail historiography** (Chisholm, Western, Shawnee) — `candidate` until alignment evidence is closed; corridor view is the public-safe form.

Each candidate must be drafted as a `SourceDescriptor` and passed through the admission flow in [§4](#4-source-admission-flow) before any data is fetched.

</details>

[⬆ Back to top](#contents)

---

<!-- Footer -->

---

**Related docs:** [Directory Rules](../../doctrine/directory-rules.md) · [PROV standard](../../standards/PROV.md) · [Roads/Rail/Trade dossier (Atlas ch. 13)](../../atlases/) · [Source refresh runbook (TODO)](../../runbooks/)

**Last updated:** 2026-05-19 · **Doc version:** v1 (draft)

[⬆ Back to top](#contents)
