<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/settlements-infrastructure/file-system-plan
title: Settlements & Infrastructure — Domain File-System Plan
type: standard
version: v0.2
status: draft
owners: <docs steward> / <domain steward — Settlements & Infrastructure>   # PLACEHOLDER — assign before review
created: 2026-05-19
updated: 2026-06-08
policy_label: public
related:
  - ai-build-operating-contract.md
  - docs/doctrine/directory-rules.md
  - docs/domains/README.md
  - docs/standards/PROV.md
  - docs/runbooks/README.md
  - kfm://atlas/domains/v1_1#ch-14-settlements-infrastructure
  - kfm://encyclopedia/section-7-12
tags: [kfm, domain, settlements, infrastructure, directory-rules, file-system-plan]
notes:
  - "CONTRACT_VERSION pinned to 3.0.0 per ai-build-operating-contract.md authority."
  - "All concrete paths in this plan are PROPOSED until verified against a mounted repository."
  - "Slug 'settlements-infrastructure/' is grounded in directory-rules.md v1.3 6.1; schema-folder variance vs. the Atlas '[DOM-SETTLE] schemas/contracts/v1/settlement/' singular form is filed as OPEN-FSP-01 and is independently tracked in the KFM slug-drift register."
[/KFM_META_BLOCK_V2] -->

# Settlements & Infrastructure — Domain File-System Plan

A responsibility-rooted map of every place files for the **Settlements & Infrastructure** domain are expected to live, what they hold, what they must not hold, and which gates govern them.

[![Status: draft](https://img.shields.io/badge/status-draft-orange)](#status--authority)
[![Authority: Directory Rules v1.3](https://img.shields.io/badge/authority-Directory_Rules_v1.3-blue)](../../doctrine/directory-rules.md)
[![Truth posture: cite-or-abstain](https://img.shields.io/badge/truth_posture-cite--or--abstain-7a3fa1)](../../doctrine/truth-posture.md)
[![Critical-asset deny lane](https://img.shields.io/badge/sensitivity-T4_critical_asset_lane-c0382b)](#7--sensitivity-rights--release-posture)
[![Lifecycle: RAW → PUBLISHED](https://img.shields.io/badge/lifecycle-RAW%20%E2%86%92%20PUBLISHED-2e7d32)](#6--lifecycle--data-lanes)
[![CONTRACT_VERSION: 3.0.0](https://img.shields.io/badge/CONTRACT__VERSION-3.0.0-informational)](../../../ai-build-operating-contract.md)
[![Mounted-repo presence: NEEDS VERIFICATION](https://img.shields.io/badge/mounted--repo-NEEDS_VERIFICATION-lightgrey)](#11--open-questions--verification-backlog)

> **Status · Owners · Updated**
> Status: **draft** · Owners: `<docs steward>` / `<domain steward — Settlements & Infrastructure>` *(placeholder — assign before review)* · Last reviewed: **2026-06-08** · `CONTRACT_VERSION = "3.0.0"`

---

## Quick jump

- [1 · Scope](#1--scope)
- [2 · Repo fit](#2--repo-fit)
- [3 · Inputs](#3--inputs-what-belongs-in-this-domain)
- [4 · Exclusions](#4--exclusions-what-does-not-belong-here)
- [5 · Domain file-system map](#5--domain-file-system-map)
- [6 · Lifecycle / data lanes](#6--lifecycle--data-lanes)
- [7 · Sensitivity, rights & release posture](#7--sensitivity-rights--release-posture)
- [8 · Per-lane placement table](#8--per-lane-placement-table)
- [9 · Naming & casing](#9--naming--casing)
- [10 · FAQ](#10--faq)
- [11 · Open questions & verification backlog](#11--open-questions--verification-backlog)
- [12 · Related docs](#12--related-docs)

---

## 1 · Scope

**CONFIRMED doctrine / PROPOSED implementation.** This plan describes where the **Settlements & Infrastructure** domain's files are expected to land across the repository's responsibility roots. It is a *placement* document, not a contract or schema: it tells reviewers and authors *where* a file goes once `contracts/`, `schemas/`, `policy/`, source descriptors, ADRs, and reviews have decided that the file *should* exist.

The plan is governed by:

- The lifecycle invariant **RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED** *(CONFIRMED doctrine; promotion is a governed state transition, not a file move).*
- The **trust membrane** boundary that prevents raw, unreviewed, restricted, or model-generated state from becoming public truth.
- The **critical-asset deny lane** for this domain *(CONFIRMED doctrine: critical infrastructure, condition observations, dependencies, operator-sensitive details, and exact facility geometry default to restricted or review — T4 per Atlas §24.5)*.

> [!NOTE]
> Every concrete path in this document is **PROPOSED** until verified against a mounted repository. No mounted repo, CI workflow, dashboard, or runtime log was inspected when authoring this plan; placements are grounded in `docs/doctrine/directory-rules.md` (v1.3) and the Domains v1.1 Atlas Ch. 14 / §20.5 / §24.5 / §24.13 / §24.14 only.

[↑ Back to top](#settlements--infrastructure--domain-file-system-plan)

---

## 2 · Repo fit

| Field | Value | Status |
|---|---|---|
| Owning responsibility root for **this file** | `docs/` (human-facing control plane) | CONFIRMED rule `[DIRRULES §3, §6.1]` |
| Domain segment slug | `settlements-infrastructure/` | CONFIRMED (slug appears in `directory-rules.md` v1.3 §6.1 `docs/domains/` listing) |
| This file's path | `docs/domains/settlements-infrastructure/FILE_SYSTEM_PLAN.md` | PROPOSED (path home confirmed; filename convention pending §11 OPEN-FSP-02) |
| Upstream doctrine | `ai-build-operating-contract.md` (`CONTRACT_VERSION 3.0.0`); `docs/doctrine/directory-rules.md` v1.3; Domains v1.1 Atlas Ch. 14; KFM Encyclopedia §7.12 | CONFIRMED references |
| Downstream consumers | `docs/domains/settlements-infrastructure/README.md` *(planned)*; per-domain runbooks; per-domain ADRs; reviewers proposing files in this lane | PROPOSED |
| Authority order over conflicts | Per `directory-rules.md` §2.1: KFM invariants → accepted ADRs → Directory Rules → per-root READMEs → dossiers → mounted-repo convention | CONFIRMED |

[↑ Back to top](#settlements--infrastructure--domain-file-system-plan)

---

## 3 · Inputs (what belongs in this domain)

**CONFIRMED scope (object families owned by Settlements & Infrastructure)** *[DOM-SETTLE] [ENCY]* — Atlas Ch. 14 §B names all sixteen.

| Object family | Purpose (per Atlas Ch. 14 §E) | Identity rule | Status |
|---|---|---|---|
| Settlement | Represents Settlement evidence or released derivative within Settlements/Infrastructure. | PROPOSED deterministic basis: source id + object role + temporal scope + normalized digest. | CONFIRMED doctrine (§E table) |
| Municipality | Legal-municipality evidence or derivative. | Same identity rule. | CONFIRMED doctrine (§E table) |
| CensusPlace | Census-place geography evidence or derivative. | Same identity rule. | CONFIRMED doctrine (§E table) |
| Townsite | Historic townsite evidence or derivative. | Same identity rule. | CONFIRMED doctrine (§E table) |
| GhostTown | Ghost-town evidence or derivative. | Same identity rule. | CONFIRMED doctrine (§E table) |
| Fort | Fort evidence or derivative. | Same identity rule. | CONFIRMED doctrine (§E table) |
| Mission | Mission evidence or derivative. | Same identity rule. | CONFIRMED doctrine (§E table) |
| ReservationCommunity | Reservation-community evidence or derivative. | Same identity rule. | CONFIRMED doctrine (§E table) |
| Infrastructure Asset | Infrastructure-asset evidence or derivative. | Same identity rule. | CONFIRMED doctrine (§E table) |
| Network Node | Network-node evidence or derivative. | Same identity rule. | CONFIRMED doctrine (§E table) |
| Network Segment | Network-segment evidence or derivative. | Same identity rule. | CONFIRMED doctrine (§E table) |
| Facility | Facility evidence or derivative. | Same identity rule. | CONFIRMED doctrine (§E table) |
| Service Area | Service-area evidence or derivative. | Same identity rule. | CONFIRMED scope (§B); **PROPOSED object-family entry** — not enumerated in §E table or §24.14 core matrix. |
| Operator | Operator evidence or derivative. | Same identity rule. | CONFIRMED scope (§B); **PROPOSED object-family entry**. |
| Condition Observation | Condition-observation evidence or derivative. | Same identity rule. | CONFIRMED scope (§B); **PROPOSED object-family entry**. |
| Dependency | Dependency evidence or derivative. | Same identity rule. | CONFIRMED scope (§B); **PROPOSED object-family entry**. |

> [!IMPORTANT]
> Identity rules above are **PROPOSED**. Schema and identity realization land under `schemas/` and `contracts/` — *not* in this plan. See §8. The four "PROPOSED object-family entry" rows are named in Atlas §B (Scope) but are **not** enumerated as standalone families in the Atlas §E table or the §24.14 Core-Object-Family × Domain matrix; whether each becomes its own object-family schema is a `contracts/` / `schemas/` decision (see §10 FAQ).

[↑ Back to top](#settlements--infrastructure--domain-file-system-plan)

---

## 4 · Exclusions (what does **not** belong here)

**CONFIRMED doctrine — explicit non-ownership** *[DOM-SETTLE] [ENCY]* (Atlas Ch. 14 §B):

| If the file is about… | …it belongs in domain… |
|---|---|
| Transport routes (road segments, rail segments, corridor routes, route membership, route status) | **Roads/Rail** (`roads-rail-trade/`) |
| Water evidence (gauges, watersheds, NFHL zones, flow, reaches) | **Hydrology** |
| Hazard events, warnings, advisories, disaster declarations | **Hazards** |
| Ownership, living-person privacy, raw DNA, person-parcel joins | **People / Genealogy / DNA / Land** |

> [!CAUTION]
> A file that crosses these boundaries is a **cross-lane relation**, not a domain reassignment. Cross-lane relations preserve the owner's source role, sensitivity, and EvidenceBundle support; they do not move the object. See §5 diagram for the four canonical cross-lane edges (Atlas Ch. 14 §F).

[↑ Back to top](#settlements--infrastructure--domain-file-system-plan)

---

## 5 · Domain file-system map

The diagram below shows the **responsibility roots** where Settlements & Infrastructure files are expected to land. Each leaf is a *lane*, not a root; the domain never owns a root folder.

```mermaid
%% PROPOSED placement map — each responsibility root carries a settlements-infrastructure lane.
%% Slug: settlements-infrastructure/   (CONFIRMED via directory-rules.md v1.3 6.1)
flowchart LR
    classDef root fill:#0b4a8a,stroke:#062f57,color:#fff,stroke-width:1px,font-weight:bold;
    classDef lane fill:#eef4fb,stroke:#5c84b1,color:#0b2a4a;
    classDef deny fill:#fde9e7,stroke:#c0382b,color:#7a1d12,font-weight:bold;
    classDef external fill:#f3eaf8,stroke:#7a3fa1,color:#3a1b54,stroke-dasharray:4 2;

    DOCS["docs/"]:::root
    CTRL["control_plane/"]:::root
    CONT["contracts/"]:::root
    SCH["schemas/"]:::root
    POL["policy/"]:::root
    TST["tests/"]:::root
    FX["fixtures/"]:::root
    PKG["packages/"]:::root
    PIPE["pipelines/"]:::root
    PSP["pipeline_specs/"]:::root
    CONN["connectors/"]:::root
    DATA["data/"]:::root
    REL["release/"]:::root

    DOCS --> D1["docs/domains/settlements-infrastructure/ (this file lives here)"]:::lane
    CTRL --> C1["control_plane/domain_lane_register.yaml (domain entry)"]:::lane
    CONT --> CN1["contracts/settlement/ OR contracts/domains/settlements-infrastructure/ (OPEN-FSP-01)"]:::lane
    SCH --> S1["schemas/contracts/v1/settlement/ OR schemas/contracts/v1/domains/settlements-infrastructure/ (OPEN-FSP-01)"]:::lane
    POL --> P1["policy/domains/settlements-infrastructure/ + policy/sensitivity/infrastructure/"]:::lane
    POL --> P2["Critical-asset deny lane (T4)"]:::deny
    TST --> T1["tests/domains/settlements-infrastructure/"]:::lane
    FX --> F1["fixtures/domains/settlements-infrastructure/ (valid + invalid + public-safe)"]:::lane
    PKG --> PK1["packages/domains/settlements-infrastructure/ (optional; only if shared library)"]:::lane
    PIPE --> PI1["pipelines/domains/settlements-infrastructure/"]:::lane
    PSP --> PS1["pipeline_specs/settlements-infrastructure/"]:::lane
    CONN --> CO1["connectors/ census/ gnis/ kdot/ fema/ state-local-gis/ operators/ ..."]:::external
    DATA --> DA1["data/phase/settlements-infrastructure/ RAW WORK QUARANTINE PROCESSED CATALOG TRIPLETS PUBLISHED"]:::lane
    DATA --> DA2["data/registry/sources/source/"]:::lane
    REL --> RE1["release/candidates/settlements-infrastructure/"]:::lane

    P2 -.governs.-> S1
    P2 -.governs.-> RE1
    P2 -.governs.-> DA1
```

> [!NOTE]
> The diagram is **illustrative** of the responsibility-rooted layout. Concrete folder presence is **NEEDS VERIFICATION** against a mounted repo. The domain-segment naming variance (`settlement/` short slug per Atlas §24.13 vs `settlements-infrastructure/` / `domains/settlements-infrastructure/` per Directory Rules §6.4) is filed as **OPEN-FSP-01** in §11 and is independently tracked in the KFM slug-drift register (deep-research report, Domains §slug-drift).

[↑ Back to top](#settlements--infrastructure--domain-file-system-plan)

---

## 6 · Lifecycle / data lanes

**CONFIRMED doctrine / PROPOSED lane application.** This domain follows the universal lifecycle invariant. Promotion between phases is a **governed state transition**, never a file move *[DIRRULES] [DOM-SETTLE] [ENCY]*. Lane paths shown in the Atlas §24.13 short-slug form (`settlement/`) pending **OPEN-FSP-01**.

| Stage | Handling (per Atlas Ch. 14 §H) | Gate | Proposed home | Status |
|---|---|---|---|---|
| **RAW** | Capture immutable source payload or reference with source role, rights, sensitivity, citation, time, and hash. | SourceDescriptor exists. | `data/raw/settlement/<source_id>/<run_id>/` | PROPOSED |
| **WORK / QUARANTINE** | Normalize schema, geometry, time, identity, evidence, rights, and policy; hold failures. | Validation and policy gate pass, or quarantine reason is recorded. | `data/work/settlement/...` ; `data/quarantine/settlement/...` | PROPOSED |
| **PROCESSED** | Emit validated normalized objects, receipts, and public-safe candidates. | EvidenceRef, ValidationReport, and digest closure exist. | `data/processed/settlement/...` ; `data/receipts/settlement/...` ; `data/proofs/settlement/...` | PROPOSED |
| **CATALOG / TRIPLET** | Emit catalog records, EvidenceBundles, graph / triplet projections, and release candidates. | Catalog / proof closure passes. | `data/catalog/domain/settlement/...` ; `data/triplets/settlement/...` | PROPOSED |
| **PUBLISHED** | Serve released public-safe artifacts through governed APIs and manifests. | ReleaseManifest, correction path, rollback target, and review/policy state exist. | `data/published/layers/settlement/...` ; manifests under `release/manifests/`; promotion under `release/promotion_decisions/`; rollback under `release/rollback_cards/` | PROPOSED |

> [!WARNING]
> **No file MAY skip a phase.** Connectors emit only to `data/raw/...` or `data/quarantine/...`. Workers emit receipts and candidate decisions; they do not publish. The trust membrane (governed API) is the only normal public path.

<details>
<summary><strong>Compatibility note — receipts, proofs, registry, rollback</strong></summary>

Per `directory-rules.md` §4 Step 2, receipts, proofs, registry, and rollback are emitted **alongside** lifecycle directories — they do not replace them. The Settlements & Infrastructure lane respects that convention; e.g. `data/receipts/settlement/...` is a *sibling* of `data/processed/settlement/...`, not a replacement for it.

Whether `data/rollback/` (data-plane alias revert) and `release/rollback_cards/` (decision plane) co-exist or merge is an **open ADR-class question** carried forward from Directory Rules §18.a. This plan keeps both pending resolution.

</details>

[↑ Back to top](#settlements--infrastructure--domain-file-system-plan)

---

## 7 · Sensitivity, rights & release posture

**CONFIRMED doctrine.** **Critical infrastructure** detail defaults to **T4 — Denied**; the critical-asset deny lane is the most important boundary in this domain *[DOM-SETTLE] [ENCY] [Atlas v1.1 §20.5, §24.5, §24.14]*. Public-safe settlement/place objects sit at the open end of the tier scale.

| Object class | Default tier | Allowed transforms (PROPOSED) | Required gates | Status |
|---|---|---|---|---|
| Settlement / Municipality / GhostTown / Townsite (public-safe historical / place) | **T0–T1 — Open / Generalized** | None beyond standard release (T0), or vintage/precision flagging (T1). | ReleaseManifest + EvidenceBundle. | **INFERRED** — per-object tier not assigned verbatim in §24.5; T0–T1 is the reasonable public-safe default |
| Infrastructure Asset (critical) | **T4 — Denied** | Generalized facility footprint + suppressed dependency → T1. | Steward review + RedactionReceipt. | CONFIRMED doctrine (§24.5, §24.14: "T4 default for critical detail; T1 for generalized footprint") |
| Infrastructure — condition / vulnerability | **T4 — Denied** | T3 to named authorities only; never T0 / T1. | Steward review + named-party agreement. | CONFIRMED doctrine (§24.5) |
| Operator-sensitive details, exact facility geometry, dependencies | **Restricted or Review (T4)** | Generalization / redaction; named-agreement release as policy permits. | RedactionReceipt + ReviewRecord + PolicyDecision. | CONFIRMED doctrine (Atlas §I, §20.5) |

> [!CAUTION]
> **Unclear rights, unresolved source role, missing evidence, unresolved sensitivity, or absent release state blocks public promotion.** This is invariant, not advisory (Atlas Ch. 14 §I).

> [!NOTE]
> **Tier transitions are reversible** (Atlas §24.5). `T4 → T1` requires `RedactionReceipt + ReviewRecord`; a `CorrectionNotice` may demote a published `T1` back to `T4`. This reversibility is the rollback basis for any public-safe asset layer.

**Policy lane homes (PROPOSED):**

```text
policy/domains/settlements-infrastructure/   # general domain admissibility
policy/sensitivity/infrastructure/           # critical-asset deny lane (CONFIRMED form, §24.13)
policy/release/settlements-infrastructure/   # release-stage admissibility (if needed)
```

The `policy/sensitivity/infrastructure/` path is **CONFIRMED in doctrine** *(named in Atlas Ch. 24.13 row 14 and the KFM Encyclopedia §7.12 schema-folder table)*; its mounted-repo presence is **NEEDS VERIFICATION**.

[↑ Back to top](#settlements--infrastructure--domain-file-system-plan)

---

## 8 · Per-lane placement table

The canonical reference: for each file kind, the responsibility root, the domain segment, and the gating authority. **All paths PROPOSED** unless otherwise marked.

| Responsibility root | Domain-lane path (PROPOSED) | What lives here | Governing authority |
|---|---|---|---|
| `docs/` | `docs/domains/settlements-infrastructure/` | Human-facing domain operating manual: this plan, domain README, decision notes, glossary alignments. | DIRRULES §6.1 (slug CONFIRMED) |
| `control_plane/` | `control_plane/domain_lane_register.yaml` *(entry for this domain)* | Machine-readable "what governs what" — domain-to-source, domain-to-schema, domain-to-policy maps. | DIRRULES §6.2 |
| `contracts/` | `contracts/settlement/` *(Atlas §24.13)* — **or** `contracts/domains/settlements-infrastructure/` *(DIRRULES §6.3 segment form)* — see OPEN-FSP-01 | Markdown describing what each object **means** (Settlement, Municipality, Infrastructure Asset, …), its fields' intent, its invariants. No machine validation here. | DIRRULES §6.3 |
| `schemas/` | `schemas/contracts/v1/settlement/` *(Atlas §24.13)* — **or** `schemas/contracts/v1/domains/settlements-infrastructure/` *(DIRRULES §6.4 generic form)* — see OPEN-FSP-01 | JSON Schema and JSON-LD contexts; machine-checkable shape. **Schema-home rule (ADR-0001) is canonical;** divergent `contracts/<x>.schema.json` paths are forbidden. | DIRRULES §6.4 / ADR-0001 |
| `policy/` | `policy/domains/settlements-infrastructure/` ; `policy/sensitivity/infrastructure/` *(deny lane)* | Allow / deny / restrict / abstain decisions; critical-asset deny lane lives here. | DIRRULES §3 / Atlas §I, §20.5 |
| `tests/` | `tests/domains/settlements-infrastructure/` | Proof that the rules are enforceable. Includes the proposed test set from Atlas §K: legal-municipality evidence; census-vs-municipality distinction; infrastructure topology; condition `observed_at`; restricted-geometry no-leak; catalog/proof/release closure. | DIRRULES §3 |
| `fixtures/` | `fixtures/domains/settlements-infrastructure/{valid,invalid}/` ; `fixtures/public_safe/settlements-infrastructure/` | Golden, valid, invalid, and public-safe sample data for tests and review. | DIRRULES §3 |
| `connectors/` | `connectors/census/` ; `connectors/gnis/` ; `connectors/kdot/` ; `connectors/fema/` ; `connectors/<state-local-gis>/` ; `connectors/<operator>/` *(plus historical-gazetteer connectors as added)* | Source-specific fetch / admit. Connectors emit to `data/raw/...` or `data/quarantine/...`; they MUST NOT publish or mutate canonical truth. | DIRRULES §7.3 |
| `pipelines/` | `pipelines/domains/settlements-infrastructure/` | Executable pipeline logic (ingest → normalize → validate → catalog → publish → rollback) for this domain. | DIRRULES §7.4 |
| `pipeline_specs/` | `pipeline_specs/settlements-infrastructure/` | Declarative configuration of what should run. | DIRRULES §7.4 |
| `packages/` | `packages/domains/settlements-infrastructure/` *(optional)* | Shared libraries used by multiple deployables for this domain. Create only when reuse is real; otherwise a `tools/` or `pipelines/` helper is preferred. | DIRRULES §7.2 |
| `data/` | `data/{raw,work,quarantine,processed,catalog/domain,triplets,receipts,proofs,published/layers,rollback,registry}/settlement/...` | See §6 lifecycle table. | DIRRULES §4 Step 2 |
| `release/` | `release/candidates/settlement/` ; `release/manifests/...` ; `release/promotion_decisions/...` ; `release/rollback_cards/...` ; `release/correction_notices/...` | Release decisions, manifests, rollback cards, correction notices. | DIRRULES §3 |

> [!TIP]
> The cross-cutting source descriptors for this domain's sources live under `data/registry/sources/<source>/` (per `directory-rules.md` §4 Step 3), **not** under the domain lane. The connector under `connectors/<source>/` and the descriptor under `data/registry/sources/<source>/` are different responsibilities.

> [!IMPORTANT]
> **Segment-name consistency under OPEN-FSP-01.** The lifecycle/data and release rows above use the Atlas §24.13 short slug `settlement/`, while the human-facing `docs/`, `policy/`, `tests/`, `fixtures/`, `pipelines/` rows use the compound `settlements-infrastructure/` segment that Directory Rules §6 trees demonstrate. This split is exactly the conflict OPEN-FSP-01 must resolve; the ADR should **freeze a single pair** (one slug for `schemas/`+`contracts/`, one for the rest) rather than leaving both live. Until then, both forms are PROPOSED.

**Source families relevant to this domain** *(authority/observation/context/model roles vary per source; rights & current terms NEEDS VERIFICATION; sensitive joins fail closed)* — per Atlas §D:

- Census TIGER / census-place geography
- GNIS and gazetteers
- State/local GIS / Kansas Geoportal-style sources
- Municipal and local legal records
- Historical gazetteers and maps
- Infrastructure operators and providers *(rights typically restricted; T4 default for sensitive detail)*
- KDOT / bridge / facility sources *(cross-cuts with Roads/Rail)*
- FEMA / hazards / resilience sources *(cross-cuts with Hazards)*

[↑ Back to top](#settlements--infrastructure--domain-file-system-plan)

---

## 9 · Naming & casing

**CONFIRMED** anchors:

- The `docs/` domain segment slug is **`settlements-infrastructure/`** (kebab-case, lowercase) per `directory-rules.md` v1.3 §6.1.
- The dossier short-name is **`[DOM-SETTLE]`** per Atlas Appendix B and Master Source Ledger.

**Naming variances surfaced — not silently smoothed** *(independently tracked in the KFM slug-drift register: row 14 "Singular schema slug vs plural domain name")*:

| Surface | Variant A | Variant B | Status |
|---|---|---|---|
| Schema folder | `schemas/contracts/v1/settlement/` *(Atlas Ch. 24.13 & Encyclopedia §7.12 form)* | `schemas/contracts/v1/domains/settlements-infrastructure/` *(DIRRULES §6.4 generic form)* | **OPEN-FSP-01** — ADR-class per DIRRULES §2.4(5) if it standardizes a parallel home; maps to Atlas open-ADR ADR-S-01. |
| Contract folder | `contracts/settlement/` *(Atlas Ch. 24.13)* | `contracts/domains/settlements-infrastructure/` *(DIRRULES §6.3)* | **OPEN-FSP-01** — same family of question; maps to ADR-S-02. |
| Domain-segment singular vs compound | `settlement/` *(short, matches `[DOM-SETTLE]`)* | `settlements-infrastructure/` *(matches `docs/` slug)* | **OPEN-FSP-01** — recommendation: align human-facing roots (`docs/`, and `policy/sensitivity/infrastructure/` already uses the compound topic) on the compound; accept `settlement/` for the `schemas/` / `contracts/` short slug if the ADR confirms — but **freeze the pair, not both**. |
| Filename pattern for this doc | `FILE_SYSTEM_PLAN.md` *(SCREAMING_SNAKE — matches authored `SOURCE_REFRESH_RUNBOOK.md`)* | Plain `file-system-plan.md` *(matches `directory-rules.md` kebab pattern)* | **OPEN-FSP-02** — pending ADR on docs-file naming conventions; parallel to DIRRULES OPEN-DR-04. The path *as supplied by the requesting user* uses SCREAMING_SNAKE; this draft accepts that form. |

> [!IMPORTANT]
> Until OPEN-FSP-01 and OPEN-FSP-02 are resolved by ADR, this plan treats the supplied path (`docs/domains/settlements-infrastructure/FILE_SYSTEM_PLAN.md`) as the live artifact and flags any new cross-reference under a competing form as a **drift candidate** for `docs/registers/DRIFT_REGISTER.md`.

[↑ Back to top](#settlements--infrastructure--domain-file-system-plan)

---

## 10 · FAQ

> [!NOTE]
> **Q. Why does the domain own *settlements* but not *roads*, *bridges*, or *parcels*?**
> **A.** Roads and rail are owned by the **Roads/Rail** domain. Parcels are owned by **People / Genealogy / DNA / Land**. Settlements & Infrastructure cites those objects via cross-lane relations (Atlas Ch. 14 §F) — it does not relocate them. Bridges are a special case: the geometry and route membership live with Roads/Rail; the dependency on a settlement or a service area lives here.

> [!NOTE]
> **Q. Where does a new historical-gazetteer source go?**
> **A.** The connector goes under `connectors/<gazetteer-id>/`. The source descriptor lives under `data/registry/sources/<gazetteer-id>/`. The lifecycle output lands under `data/raw/settlement/<gazetteer-id>/<run_id>/`. The schema for whatever object the gazetteer produces lives under `schemas/contracts/v1/settlement/` *(pending OPEN-FSP-01)*. The connector folder is **not** a settlements lane — it is a source lane.

> [!NOTE]
> **Q. A team wants to publish a public-safe substation map. Where does it land?**
> **A.** It does **not** land — at least not without passing the critical-asset deny lane. Default tier is **T4**. Allowed motion is T4 → T1 via generalized facility footprint + suppressed dependency, with a `RedactionReceipt` and a steward `ReviewRecord`. The published layer would land under `data/published/layers/settlement/<layer>/` only after the gates close. The redaction transform itself is recorded under `data/receipts/settlement/...` so the public derivative is auditable.

> [!NOTE]
> **Q. Why are `Service Area`, `Operator`, `Condition Observation`, and `Dependency` flagged "PROPOSED object-family entry"?**
> **A.** Atlas Ch. 14 §B (Scope) names them; Atlas Ch. 14 §E (Main object families) and the Atlas v1.1 Master Object-Family × Domain Reference Matrix (Ch. 24.14) do **not** enumerate them as standalone object families — both stop at `Facility`. The terms are part of the domain's ubiquitous language; whether each gets its own object-family schema is a `contracts/`/`schemas/` decision, not a file-system decision. This plan leaves a placement lane for them but does not assert that the contracts exist.

[↑ Back to top](#settlements--infrastructure--domain-file-system-plan)

---

## 11 · Open questions & verification backlog

Tracked here for triage; resolutions migrate to `docs/registers/VERIFICATION_BACKLOG.md` or `docs/adr/` as appropriate.

### 11.a Placement (potentially ADR-class)

- **OPEN-FSP-01 — Domain segment under `schemas/` and `contracts/`.** The Atlas v1.1 master crosswalk (Ch. 24.13) and Encyclopedia §7.12 show `schemas/contracts/v1/settlement/` and `contracts/settlement/` (short slug, matching the `[DOM-SETTLE]` dossier). The Directory Rules §6.4 schema tree and §6.3 contract tree show the generic `schemas/contracts/v1/domains/<domain>/` and `contracts/domains/<domain>/` form. The KFM slug-drift register independently records this as "singular schema slug vs plural domain name." Until reconciled, **either** form may be defended; the live repo should not carry both. **Resolution by ADR** per DIRRULES §2.4(5); maps to Atlas open-ADRs ADR-S-01 (schema home) and ADR-S-02 (artifact placement), and ADR-0001.
- **OPEN-FSP-02 — Filename convention for this class of doc.** `FILE_SYSTEM_PLAN.md` (SCREAMING_SNAKE, matching authored `SOURCE_REFRESH_RUNBOOK.md`) vs `file-system-plan.md` (kebab, matching `directory-rules.md`). Parallel to the Directory Rules OPEN-DR-04 family. **Resolution by docs-steward decision or ADR.**

### 11.b Carried forward from Directory Rules §18

- **NEEDS VERIFICATION:** Whether `contracts/` or `schemas/contracts/v1/` is the live machine-schema authority. ADR-0001 defaults to `schemas/contracts/v1/`. Affects this domain directly.
- **NEEDS VERIFICATION:** Whether `policy/` or `policies/` is canonical. Default is `policy/`. Affects `policy/domains/settlements-infrastructure/` and `policy/sensitivity/infrastructure/`.
- **OPEN-DR-02 (DIRRULES):** Runbook subfolder vs flat pattern. When this domain's runbooks are authored (e.g. critical-asset redaction drill), they should land at `docs/runbooks/settlements-infrastructure/<RUNBOOK>.md` per Pattern A, consistent with the fauna runbook precedent — pending the ADR that freezes the convention.

### 11.c Domain-specific (carried from Atlas §N)

| Item to verify | Evidence that would settle it | Status |
|---|---|---|
| Source rights and municipal legal-source roles. | Mounted repo files, schemas, registry entries, tests, logs, emitted artifacts, review records, release manifests. | NEEDS VERIFICATION |
| Critical infrastructure policy (the `policy/sensitivity/infrastructure/` deny lane). | As above; specifically, presence of `policy/sensitivity/infrastructure/` and at least one enforced gate. | NEEDS VERIFICATION |
| Public-safe layer registry. | Presence of `data/registry/layers/<settlement-layer>/` entries with rights, sensitivity, and release-state fields. | NEEDS VERIFICATION |
| API and Focus Mode auth/policy behavior for `Settlements/Infrastructure feature/detail resolver`. | Governed-API route registration; runtime envelope schema; policy bundle; AIReceipt schema. | NEEDS VERIFICATION |

### 11.d Other unknowns surfaced by this plan

- **UNKNOWN:** Whether `docs/domains/settlements-infrastructure/` already exists in the mounted repo, and whether a sibling `README.md` is present or pending.
- **UNKNOWN:** Whether any of the proposed connector folders (`census/`, `gnis/`, `kdot/`, `fema/`, etc.) are present, what their source-descriptor coverage is, and which (if any) have produced RAW outputs.
- **UNKNOWN:** Whether the test set proposed by Atlas §K (legal-municipality evidence; census-vs-municipality distinction; infrastructure topology; condition `observed_at`; restricted-geometry no-leak; catalog/proof/release closure) has any implementation under `tests/domains/settlements-infrastructure/`.

[↑ Back to top](#settlements--infrastructure--domain-file-system-plan)

---

## 12 · Related docs

- [`ai-build-operating-contract.md`](../../../ai-build-operating-contract.md) — canonical operating contract, `CONTRACT_VERSION = "3.0.0"`
- [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md) — placement authority, **v1.3** *(CONFIRMED reference)*
- [`docs/domains/README.md`](../README.md) — domain-index landing *(PROPOSED — confirm presence)*
- [`docs/domains/settlements-infrastructure/README.md`](./README.md) — domain operating manual *(PROPOSED — planned sibling)*
- [`docs/adr/`](../../adr/) — accepted ADRs; OPEN-FSP-01 and OPEN-FSP-02 would land here once raised
- [`docs/standards/PROV.md`](../../standards/PROV.md) — provenance standard *(CONFIRMED authored; naming-variance question OPEN-DR-01)*
- [`docs/runbooks/README.md`](../../runbooks/README.md) — runbook index *(any future settlements-infrastructure runbook should land per Pattern A — `docs/runbooks/settlements-infrastructure/...`)*
- [`docs/registers/DRIFT_REGISTER.md`](../../registers/DRIFT_REGISTER.md) — drift entries *(PROPOSED home for naming-variance drifts)*
- [`docs/registers/VERIFICATION_BACKLOG.md`](../../registers/VERIFICATION_BACKLOG.md) — verification queue
- `kfm://atlas/domains/v1_1#ch-14-settlements-infrastructure` — Atlas Ch. 14 dossier
- `kfm://encyclopedia/section-7-12` — Encyclopedia per-domain entry for Settlements/Infrastructure

---

> **Last reviewed:** 2026-06-08 · **Authored by:** `<docs steward>` *(placeholder)* · **Status:** draft · `CONTRACT_VERSION = "3.0.0"`
> **Authority basis:** `ai-build-operating-contract.md` (v3.0) · `directory-rules.md` **v1.3** §§2–4, §6, §13, §18 · Domains v1.1 Atlas Ch. 14, §20.5, §24.5, §24.13, §24.14 · KFM Encyclopedia §7.12.
>
> [↑ Back to top](#settlements--infrastructure--domain-file-system-plan)
