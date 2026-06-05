<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/domains/habitat/readme
title: Habitat Domain — Lane README
type: standard
version: v1.1
status: draft
owners: [NEEDS_VERIFICATION — habitat domain steward, docs steward]
created: 2026-05-17
updated: 2026-06-05
policy_label: public
contract_version: "3.0.0"   # pinned per ai-build-operating-contract.md
related:
  - docs/domains/README.md
  - docs/domains/fauna/README.md
  - docs/domains/flora/README.md
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - docs/doctrine/trust-membrane.md
  - docs/standards/PROV.md
  - docs/standards/ISO-19115.md
  - ai-build-operating-contract.md
tags: [kfm, domain, habitat, ecology, suitability, connectivity, sensitivity]
notes:
  - "Domain README — orients the Habitat lane across all responsibility roots."
  - "Implementation maturity is PROPOSED pending mounted-repo verification."
  - "PATH DOCTRINE: this README uses the Directory Rules §12 segment form (docs/domains/habitat/, contracts/domains/habitat/, schemas/contracts/v1/domains/habitat/). The Atlas §24.13 crosswalk uses a flat form (contracts/habitat/). The Atlas's own §24 authority rule makes its tables navigational-not-authoritative, so §12 segment form governs placement; the flat form is a drift candidate. Conflict surfaced in §16 / HAB-V-009."
  - "Source-role labels in §3 align to the CONFIRMED 7-role enum (Atlas §24.1): observed | regulatory | modeled | aggregate | administrative | candidate | synthetic."
  - "CONTRACT_VERSION = \"3.0.0\""
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# 🌿 Habitat — Domain Lane

> Governed, evidence-first lane for **habitat patches, classes, suitability, connectivity, corridors, restoration opportunity, and stewardship zones** in the Kansas Frontier Matrix (KFM). Habitat models landscape; it does not own species records.

<p align="center">
  <b>Map-first · Time-aware · Evidence-bounded · Sensitivity-redacted by default</b>
</p>

![status](https://img.shields.io/badge/status-draft-orange)
![authority](https://img.shields.io/badge/authority-canonical%20%28docs%29-blue)
![lifecycle](https://img.shields.io/badge/lifecycle-RAW%E2%86%92PUBLISHED-informational)
![policy](https://img.shields.io/badge/policy-fail--closed-critical)
![sensitivity](https://img.shields.io/badge/sensitivity-redacted--by--default-red)
![contract](https://img.shields.io/badge/CONTRACT__VERSION-3.0.0-blueviolet)
![doc--type](https://img.shields.io/badge/doc--type-domain%20README-lightgrey)
<!-- TODO: replace placeholder Shields.io badges with CI/version/last-updated badges once owners and CI targets are verified (NEEDS VERIFICATION). -->

| Field | Value |
|---|---|
| **Domain** | `habitat` |
| **Path** | `docs/domains/habitat/README.md` (Directory Rules §12 segment form — **CONFIRMED pattern**) |
| **Authority level** | **Canonical** (under `docs/`, the human-facing control plane) |
| **Status** | **PROPOSED** lane implementation; **CONFIRMED** doctrine |
| **Contract** | `CONTRACT_VERSION = "3.0.0"` |
| **Owners** | NEEDS VERIFICATION — habitat domain steward (CODEOWNERS placeholder) |
| **Reviewers** | Habitat domain steward + docs steward; policy steward for sensitivity changes |
| **Last reviewed** | 2026-06-05 |

---

## Contents

1. [Purpose & one-line scope](#1-purpose--one-line-scope)
2. [Repo fit — where Habitat lives](#2-repo-fit--where-habitat-lives)
3. [Inputs — accepted source families](#3-inputs--accepted-source-families)
4. [Exclusions — what does NOT belong here](#4-exclusions--what-does-not-belong-here)
5. [Object families & ubiquitous language](#5-object-families--ubiquitous-language)
6. [Lifecycle — RAW → PUBLISHED](#6-lifecycle--raw--published)
7. [Sensitivity, rights, & publication posture](#7-sensitivity-rights--publication-posture)
8. [Cross-lane relations](#8-cross-lane-relations)
9. [Map & viewing products](#9-map--viewing-products)
10. [Governed AI behavior](#10-governed-ai-behavior)
11. [Validation, tests, fixtures](#11-validation-tests-fixtures)
12. [API & contract surfaces](#12-api--contract-surfaces)
13. [Lane diagram](#13-lane-diagram)
14. [Open questions & verification backlog](#14-open-questions--verification-backlog)
15. [Changelog & definition of done](#15-changelog--definition-of-done)
16. [Related folders, docs & ADRs](#16-related-folders-docs--adrs)

---

## 1. Purpose & one-line scope

**Habitat** models land cover, ecological systems, habitat quality and connectivity as **evidence-backed observations and models**, and emits **public-safe derivatives** for sensitive ecological contexts. Habitat is the landscape lane: it owns *places of habitat* and *modeled habitat suitability*, and joins to species records owned by **Fauna** and **Flora** through governed relationships only.

- **Status — doctrine.** CONFIRMED via the KFM Encyclopedia §7.4 and the Domains Culmination Atlas v1.1 Ch. 6 (Habitat dossier §A–§N).
- **Status — implementation.** PROPOSED. Existing habitat files, schema home, source rights, model fitness, live-data permissions, and MapLibre/Evidence-Drawer wiring remain NEEDS VERIFICATION pending mounted-repo inspection.

> [!IMPORTANT]
> **Habitat owns landscape, not species.** Occurrence truth belongs to **Fauna**; plant records belong to **Flora**. A modeled habitat patch is not a critical-habitat designation, and a suitability raster is not an occurrence. Source-role anti-collapse is enforced: the seven roles *observed*, *regulatory*, *modeled*, *aggregate*, *administrative*, *candidate*, and *synthetic* are never interchangeable. **(CONFIRMED — Atlas §24.1; Habitat dossier §I.)**

[⬆ back to top](#top)

---

## 2. Repo fit — where Habitat lives

Per **Directory Rules §12 — Domain Placement Law**, a domain MUST NOT become a root folder. The Habitat lane appears as a **segment** inside each responsibility root. This README anchors only the `docs/` segment; sibling segments live in their own responsibility roots and link back here.

```text
docs/domains/habitat/                         ← this README (canonical)
contracts/domains/habitat/                    ← object meanings — PROPOSED
schemas/contracts/v1/domains/habitat/         ← machine shape (ADR-0001 home) — PROPOSED
policy/domains/habitat/                       ← allow/deny/restrict/abstain — PROPOSED
tests/domains/habitat/                        ← enforceability proofs — PROPOSED
fixtures/domains/habitat/                     ← golden / negative samples — PROPOSED
packages/domains/habitat/                     ← shared lane library — PROPOSED
pipelines/domains/habitat/                    ← executable pipeline logic — PROPOSED
pipeline_specs/habitat/                       ← declarative pipeline configs — PROPOSED
data/raw/habitat/                             ← immutable source payloads
data/work/habitat/                            ← in-progress normalization
data/quarantine/habitat/                      ← failed-gate holds
data/processed/habitat/                       ← validated normalized objects
data/catalog/domain/habitat/                  ← catalog/triplet/bundles
data/published/layers/habitat/                ← released, public-safe artifacts
data/registry/sources/habitat/                ← SourceDescriptors for the lane
release/candidates/habitat/                   ← release candidates + manifests
```

> [!NOTE]
> The segment **pattern** above is **CONFIRMED** by Directory Rules §12 (which lists habitat among the domains it governs); the **specific siblings present in your branch** are **PROPOSED** until verified against the mounted repo.

> [!WARNING]
> **Path-form conflict between two governing docs (CONFLICTED — see HAB-V-009).** Directory Rules §12 uses the **segment form** (`contracts/domains/habitat/`, `schemas/contracts/v1/domains/habitat/`). The Atlas §24.13 responsibility-root crosswalk uses a **flat form** (`contracts/habitat/`, `schemas/contracts/v1/habitat/`). The Atlas's own Chapter-24 authority rule states its master tables are *navigational, not authoritative*, and that a Chapter-24 table disagreeing with v1.0/Directory Rules is *a drift entry, not a correction*. **Disposition:** this README follows the Directory Rules §12 segment form as governing; the Atlas flat form is logged as a drift candidate for ADR/DRIFT_REGISTER resolution. This README does not silently adopt the flat form.

[⬆ back to top](#top)

---

## 3. Inputs — accepted source families

The Habitat lane admits sources only via a `SourceDescriptor` carrying source role, rights, sensitivity, citation, time, and hash. **Source role is a first-class identity attribute** (Atlas §24.1) and is never collapsed. The `source_role` enum is **CONFIRMED**: `observed | regulatory | modeled | aggregate | administrative | candidate | synthetic`.

| Source family | `source_role` (CONFIRMED enum) | Rights / sensitivity | Freshness | Status |
|---|---|---|---|---|
| **USFWS ECOS / Critical Habitat services** | **regulatory** (designated critical-habitat unit) | rights & current terms NEEDS VERIFICATION; sensitive joins fail closed | source-vintage / cadence specific | PROPOSED |
| **NLCD land cover** | **observed** (remote-sensed) → may feed **modeled** classification | rights & current terms NEEDS VERIFICATION | source-vintage / cadence specific | PROPOSED |
| **NWI wetlands** | **regulatory** (wetland regulatory class) | rights & current terms NEEDS VERIFICATION | source-vintage / cadence specific | PROPOSED |
| **GAP / LANDFIRE ecological systems** | **modeled** (classification) | rights & current terms NEEDS VERIFICATION | source-vintage / cadence specific | PROPOSED |
| **NatureServe & controlled biodiversity** | **aggregate** (summary) / authority context | rights & current terms NEEDS VERIFICATION; **steward-controlled** | source-vintage / cadence specific | PROPOSED |
| **KDWP state ecological / habitat context** | **regulatory** / **aggregate** as the descriptor sets | rights & current terms NEEDS VERIFICATION | source-vintage / cadence specific | PROPOSED |
| **PAD-US stewardship context** | **administrative** | rights & current terms NEEDS VERIFICATION | source-vintage / cadence specific | PROPOSED |
| **GBIF / iNaturalist / iDigBio (occurrence inputs)** | **observed** (occurrence) — **owned by Fauna**; admitted here only as join context under geoprivacy | rights & current terms NEEDS VERIFICATION; geoprivacy applies | source-vintage / cadence specific | PROPOSED |
| **Remote-sensing vegetation indices** | **observed** → may feed **modeled** | rights & current terms NEEDS VERIFICATION | source-vintage / cadence specific | PROPOSED |
| **Field surveys & steward-reviewed habitat models** | **observed** (survey) / **modeled** (model) | rights & current terms NEEDS VERIFICATION | source-vintage / cadence specific | PROPOSED |

> [!NOTE]
> Role assignment is **set at admission** in the `SourceDescriptor` and **preserved through every promotion**. Promotion never upgrades a role — an observation is never relabeled regulatory, a model never relabeled aggregate. The role pairings above (e.g., "observed → may feed modeled") describe *allowed downstream products carrying their own role*, not in-place relabeling. **(CONFIRMED — Atlas §24.1.1 reading note.)**

[⬆ back to top](#top)

---

## 4. Exclusions — what does NOT belong here

Habitat is a lane, not a topic bucket. The following are explicitly out of scope; misplaced content should be moved to the indicated home before review.

| Out-of-scope content | Correct home | Why |
|---|---|---|
| Animal taxonomic identity, conservation status, occurrence evidence | `docs/domains/fauna/` | Owned by **Fauna**. Habitat may cite occurrence context only under geoprivacy. |
| Plant taxonomic identity, specimens, rare-plant locations | `docs/domains/flora/` | Owned by **Flora**. Habitat may cite vegetation-community context only. |
| Watersheds, gauges, wetlands hydrology root truth | `docs/domains/hydrology/` | Hydrology owns water lineage; Habitat consumes context joins. |
| Soil map units, components, horizons | `docs/domains/soil/` | Soil owns substrate; Habitat consumes context joins. |
| Crop & field records | `docs/domains/agriculture/` | Agriculture owns crop lineage. |
| Cross-domain validators (e.g., habitat × fauna × hydrology) | `tools/validators/<topic>/...` | Per Directory Rules §12 "Multi-domain & cross-cutting files" — lowest common responsibility root, **no domain segment**. |
| Release decisions, signed manifests, rollback cards | `release/candidates/habitat/`, `release/decisions/`, `data/receipts/` | Release lives in `release/`; receipts and proofs live under `data/`. `artifacts/` is not a trust-content home (Directory Rules §13.2). |
| New schema home outside `schemas/contracts/v1/domains/habitat/` | An accepted ADR is required first | Per **ADR-0001** (accepted), `schemas/contracts/v1/...` is canonical. No parallel schema homes. |

> [!WARNING]
> **Watcher-as-non-publisher invariant.** Any process under `tools/`, `pipelines/`, or `connectors/` that observes habitat source state MUST emit candidate decisions and receipts, never write to `data/catalog/` or `data/published/`. Promotion is a governed state transition, not a file move. **(CONFIRMED doctrine.)**

[⬆ back to top](#top)

---

## 5. Object families & ubiquitous language

Habitat's eleven canonical object families. The Atlas Habitat dossier §B/§E names the spine (CONFIRMED); field-level realization is PROPOSED; the temporal handling rule (distinct source / observed / valid / retrieval / release / correction times) is **CONFIRMED**.

| Object | Purpose | Identity (PROPOSED) | Temporal handling (CONFIRMED) |
|---|---|---|---|
| **HabitatPatch** | Discrete polygonal habitat unit | source id + object role + temporal scope + normalized digest | source / observed / valid / retrieval / release / correction times kept distinct |
| **LandCoverObservation** | Observed land cover at place + time | same | same |
| **EcologicalSystem** | Classified ecological-system unit | same | same |
| **Habitat Quality Score** | Scalar / categorical patch quality | same | same |
| **SuitabilityModel** | Modeled suitability surface w/ version & bounds | same | same |
| **ConnectivityEdge** | Patch-graph edge (least-cost / resistance) | same | same |
| **Corridor** | Linear corridor derived from connectivity | same | same |
| **Restoration Opportunity** | Restoration candidate site | same | same |
| **StewardshipZone** | Stewardship / management context | same | same |
| **Model Run Receipt** | Receipt for a habitat model run (inputs, params, digests) | same | same |
| **UncertaintySurface** | Spatial uncertainty for modeled products | same | same |

**Ubiquitous-language terms** (kept stable; never silently aliased to generic equivalents):
`HabitatPatch`, `LandCoverObservation`, `EcologicalSystem`, `Habitat Quality Score`, `SuitabilityModel`, `ConnectivityEdge`, `Corridor`, `Restoration Opportunity`, `StewardshipZone`, `Regulatory critical habitat`, `Modeled habitat`, `Geoprivacy transform`.

> [!IMPORTANT]
> **"Modeled habitat" is not "regulatory critical habitat."** A suitability surface, however confident, is a **modeled** product and MUST NOT be presented or labeled as a **regulatory** determination. The Atlas anti-collapse register names *"modeled product labeled or queried as observed"* and *"synthetic content presented as observed reality"* as DENY conditions for which Habitat is among the at-risk domains. The validator suite includes a modeled-as-critical denial test (PROPOSED). **(CONFIRMED — Atlas §24.1.2.)**

[⬆ back to top](#top)

---

## 6. Lifecycle — RAW → PUBLISHED

Habitat follows the KFM lifecycle invariant: **RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED.** Promotion is a **governed state transition**, not a file move. *(Invariant CONFIRMED; per-stage handling marked PROPOSED in the Habitat dossier §H.)*

| Stage | Handling | Gate | Status |
|---|---|---|---|
| **RAW** | Capture immutable source payload or reference with source role, rights, sensitivity, citation, time, and hash. | `SourceDescriptor` exists. | PROPOSED |
| **WORK / QUARANTINE** | Normalize schema, geometry, time, identity, evidence, rights, and policy; hold failures. | Validation + policy gate pass, **or** quarantine reason is recorded. | PROPOSED |
| **PROCESSED** | Emit validated normalized objects, receipts, and public-safe candidates. | `EvidenceRef`, `ValidationReport`, and digest closure exist. | PROPOSED |
| **CATALOG / TRIPLET** | Emit catalog records, `EvidenceBundle`s, graph/triplet projections, and release candidates. | Catalog / proof closure passes. | PROPOSED |
| **PUBLISHED** | Serve released public-safe artifacts through governed APIs and manifests. | `ReleaseManifest`, correction path, rollback target, and review/policy state exist. | PROPOSED |

<details>
<summary><b>Promotion preconditions (expand)</b></summary>

A habitat artifact MAY only advance to **PUBLISHED** when **all** of the following resolve:

- `SourceDescriptor` admissibility — source role, rights, sensitivity, citation, time, hash.
- `EvidenceRef` resolves to a complete `EvidenceBundle` for every supporting claim.
- `ValidationReport` is clean (or accompanied by a documented quarantine path).
- `PolicyDecision` returns **allow** (deny-by-default for any unresolved sensitivity).
- `PromotionDecision` exists, signed by the responsible role(s); separation of duties where maturity justifies it.
- `ReleaseManifest` references all artifacts, model-run receipts, and tile/style digests.
- `RollbackCard` and a correction path are in place.

Any unresolved gate fails closed.
</details>

[⬆ back to top](#top)

---

## 7. Sensitivity, rights, & publication posture

Habitat layers can reveal sensitive species context when joined to occurrence records. Exact occurrence-linked habitat outputs **must be generalized, redacted, reviewed, or denied** when they create exposure risk. **(CONFIRMED — Habitat dossier §I.)**

> [!CAUTION]
> **Deny-by-default joins.** A regulatory critical-habitat unit + sensitive-species occurrence + exact geometry is a fail-closed combination. Public-safe derivatives (generalized patches, summary suitability, grid- or watershed-level reporting) are the **only** path to publication unless a documented `Geoprivacy transform` receipt and review state allow it. Per the Atlas master tier matrix, sensitive Fauna occurrence defaults to **T4** and reaches **T1** only via geoprivacy generalization + RedactionReceipt + ReviewRecord + PolicyDecision.

Publication posture, in short:
- **Regulatory critical habitat**, **modeled habitat**, **species range**, **occurrence points**, and **landscape context** are not flattened into one another.
- **Sensitive occurrence details deny by default.**
- **Unclear rights, unresolved source role, missing evidence, unresolved sensitivity, or absent release state** blocks public promotion. **(CONFIRMED — Habitat dossier §I; Encyclopedia; Directory Rules.)**
- All transforms (generalize, suppress, jitter under constraints, delayed publication, steward-only exact access) emit a **transform receipt** stating input class, output class, reason, policy, reviewer, and residual risk.

[⬆ back to top](#top)

---

## 8. Cross-lane relations

Habitat joins to other lanes through governed relationships that **preserve ownership, source role, sensitivity, and EvidenceBundle support**. Habitat never adopts the truth of a related lane. *(Relation existence CONFIRMED — Habitat dossier §F; constraint CONFIRMED doctrine.)*

| This domain | Related lane | Relation type | Constraint |
|---|---|---|---|
| Habitat | **Fauna** | Habitat assignment & occurrence context (with geoprivacy) | Ownership, source role, sensitivity, evidence preserved |
| Habitat | **Flora** | Vegetation community & rare-plant context under Flora controls | Ownership, source role, sensitivity, evidence preserved |
| Habitat | **Soil / Hydrology** | Substrate, moisture, wetlands, riparian context | Ownership, source role, sensitivity, evidence preserved |
| Habitat | **Hazards** | Fire, drought, flood, smoke, resilience-stress context | Ownership, source role, sensitivity, evidence preserved |
| Habitat | **Agriculture** | Land-use adjacency, CDL crosswalks | Context join only; not a truth path |

The **Habitat × Fauna thin slice** (DOM-HF) is the proposed first proof for the ecological lanes: one public-safe occurrence-to-habitat assignment with evidence, sensitivity, release, map, drawer, and Focus-Mode controls — fixture-first, not live-sensitive-source. The Atlas §24.13 crosswalk notes Habitat *"pairs with Fauna under the thin-slice plan."* **(CONFIRMED pairing intent; PROPOSED implementation.)**

[⬆ back to top](#top)

---

## 9. Map & viewing products

PROPOSED Habitat-specific viewing products (all subject to the governed UI rules — popups are never an Evidence Drawer substitute, and clicks must resolve through governed APIs):

- Habitat overlay registry (with source-role badges).
- Critical-habitat view (regulatory layer, clearly labeled).
- Modeled-habitat view (suitability surface + uncertainty mode).
- Habitat patch map (polygonal patches + class).
- Connectivity / corridor view.
- Restoration-opportunity view.
- Sensitivity-redacted mode (deny-by-default for sensitive joins).
- Habitat–Fauna / Habitat–Flora join view (public-safe).
- Evidence Drawer **Habitat panel** with citations, digests, and model-run receipts.

Cross-cutting viewing products (CONFIRMED doctrine, applied here): Evidence Drawer, time-aware state, trust badges, correction / stale-state view, governed Focus Mode.

> [!NOTE]
> **No sensitive geometry hidden only by style.** Sensitive geometry must be generalized, redacted, delayed, restricted, or denied **before** tile generation. Style filters are not a sensitivity control. **(CONFIRMED doctrine.)**

[⬆ back to top](#top)

---

## 10. Governed AI behavior

CONFIRMED doctrine / PROPOSED implementation. Within this lane, AI is interpretive and evidence-subordinate. The Habitat Focus-Mode adapter:

- **MAY** summarize **released** Habitat `EvidenceBundle`s, compare evidence across versions, explain limitations, and draft steward-review notes.
- **MUST ABSTAIN** when evidence is insufficient, when citations cannot be validated, or when a confidence bound cannot be supported.
- **MUST DENY** where policy, rights, sensitivity (e.g., exact location of a sensitive habitat–occurrence join), or release state blocks the request.
- **MUST NOT** treat a tile, popup, AI summary, search index, or graph projection as sovereign truth.
- **MUST NOT** read RAW or WORK content; AI reads only released `EvidenceBundle` (Atlas §24.5.2: Governed AI RAW/WORK access = **T4**).
- **MUST** emit an `AIReceipt` and a `RuntimeResponseEnvelope` with a finite outcome — `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` — plus `evidence_refs`, `policy_decision`, and `citation_validation`.

[⬆ back to top](#top)

---

## 11. Validation, tests, fixtures

PROPOSED test families for the Habitat lane (all expected to fail closed):

- Source-descriptor tests — rights, role, sensitivity, freshness completeness.
- Critical-habitat source-role tests — never relabel a regulatory designation as observed or modeled (and vice versa).
- **Modeled-as-critical denial tests** — a suitability surface MUST NOT be served as a regulatory critical-habitat designation.
- Occurrence geoprivacy tests — generalized, redacted, or denied outputs for sensitive joins.
- Geometry validity, identity-determinism, and temporal-logic tests.
- Catalog-closure & digest-closure tests.
- Release-manifest validation & rollback-drill tests.
- No-network fixtures — public-safe, fixture-first.
- **Habitat + Fauna thin-slice fixtures** — one Kansas habitat patch (e.g., NLCD-derived) plus one public-safe fauna occurrence association, uncertainty / citation report, and one generalized public tile.

> [!NOTE]
> Test homes follow Directory Rules §12: `tests/domains/habitat/...` for enforceability proofs, `fixtures/domains/habitat/...` for golden / negative samples. Validator code, when cross-domain, lives under `tools/validators/<topic>/`, **not** under a domain segment.

[⬆ back to top](#top)

---

## 12. API & contract surfaces

PROPOSED governed surfaces for the Habitat lane. Public clients reach Habitat **only** through the governed-API trust membrane; canonical stores are never read directly.

| Endpoint / artifact | DTO / schema | Finite outcomes | Status |
|---|---|---|---|
| Habitat feature / detail resolver (route TBD) | `HabitatDecisionEnvelope` | `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` | PROPOSED; exact route UNKNOWN |
| Habitat layer-manifest resolver | `LayerManifest` (domain layer descriptor) | `ANSWER` / `DENY` / `ERROR` | PROPOSED; public-safe release only |
| Habitat Evidence Drawer payload | `EvidenceDrawerPayload` + `EvidenceBundle` projection | `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` | PROPOSED; evidence + policy filtered |
| Habitat Focus-Mode answer | `RuntimeResponseEnvelope` + `AIReceipt` | `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` | PROPOSED; AI never root truth |
| Schema responsibility root | `schemas/contracts/v1/domains/habitat/` | finite validator outcomes | PROPOSED; ADR-0001 home (segment form per Directory Rules §12) |

[⬆ back to top](#top)

---

## 13. Lane diagram

```mermaid
flowchart LR
  classDef raw fill:#fff7e6,stroke:#d28b00,color:#5a3b00;
  classDef work fill:#fff0f0,stroke:#cc3333,color:#660000;
  classDef proc fill:#eef7ff,stroke:#2e6fb5,color:#0b3a66;
  classDef cat fill:#eef9ee,stroke:#2e7d32,color:#1b4d1f;
  classDef pub fill:#f0eafc,stroke:#5e35b1,color:#2d1a5e;
  classDef gov fill:#f5f5f5,stroke:#666,color:#222;
  classDef ext fill:#ffffff,stroke:#888,color:#333,stroke-dasharray: 4 3;

  subgraph SOURCES["Source families (SourceDescriptor required)"]
    direction TB
    NLCD["NLCD / NWI / GAP / LANDFIRE<br/>(observed / regulatory / modeled)"]:::ext
    USFWS["USFWS Critical Habitat<br/>(regulatory)"]:::ext
    NSERVE["NatureServe / KDWP / PAD-US<br/>(aggregate / administrative)"]:::ext
    OCC["GBIF / iNat / iDigBio<br/>(occurrence — Fauna-owned)"]:::ext
  end

  R["data/raw/habitat/"]:::raw
  W["data/work/habitat/"]:::work
  Q["data/quarantine/habitat/"]:::work
  P["data/processed/habitat/"]:::proc
  C["data/catalog/domain/habitat/"]:::cat
  PUB["data/published/layers/habitat/"]:::pub

  SOURCES -->|"connector + admit"| R
  R -->|"normalize · validate · policy"| W
  W -. "fail-closed" .-> Q
  W -->|"EvidenceRef · ValidationReport"| P
  P -->|"EvidenceBundle · catalog closure"| C
  C -->|"PromotionDecision · ReleaseManifest"| PUB

  subgraph GOV["Governed delivery (trust membrane)"]
    direction TB
    API["apps/governed-api/"]:::gov
    UI["apps/explorer-web/<br/>(MapLibre + Evidence Drawer + Focus Mode)"]:::gov
  end

  PUB --> API --> UI

  subgraph LATERAL["Lateral relations (governed joins only)"]
    direction TB
    F["Fauna (occurrence — geoprivacy)"]:::ext
    FL["Flora (vegetation / rare plants)"]:::ext
    H["Hydrology / Soil (substrate · wetlands)"]:::ext
    HZ["Hazards (fire / drought / flood)"]:::ext
  end
  C <-->|"EvidenceBundle-preserving"| LATERAL
```

> [!NOTE]
> Diagram reflects **CONFIRMED doctrine** (lifecycle invariant, trust membrane, source-role anti-collapse, governed joins). Specific path siblings are **PROPOSED** until the mounted repo confirms them. Source-role labels updated to the CONFIRMED 7-role enum.

[⬆ back to top](#top)

---

## 14. Open questions & verification backlog

The following items remain **NEEDS VERIFICATION** until resolved against mounted-repo files, schemas, registry entries, tests, logs, emitted artifacts, review records, or release manifests.

| # | Item | Evidence that would settle it | Status |
|---|---|---|---|
| HAB-V-001 | Official critical-habitat source descriptors (USFWS ECOS endpoint, terms, cadence, rights). | `data/registry/sources/habitat/*` + SourceDescriptor validator pass | NEEDS VERIFICATION |
| HAB-V-002 | Sensitive-occurrence policy and geoprivacy-transform receipt schema for habitat × fauna joins. | `policy/domains/habitat/*`, `schemas/contracts/v1/domains/habitat/geoprivacy_transform_receipt.schema.json`, denial tests | NEEDS VERIFICATION |
| HAB-V-003 | Model-card requirements for suitability products (inputs, training/source support, bounds, uncertainty). | `contracts/domains/habitat/SuitabilityModel.md` + model-run-receipt schema + sample card | NEEDS VERIFICATION |
| HAB-V-004 | Habitat MapLibre overlay registry & Focus-Mode behavior. | `data/published/layers/habitat/*` registry, layer-manifest fixture, Focus-Mode citation-validation tests | NEEDS VERIFICATION |
| HAB-V-005 | Habitat × Fauna thin-slice fixture set (one Kansas patch + one public-safe occurrence + uncertainty report + generalized tile). | `fixtures/domains/habitat/thin_slice/*` + green CI run | NEEDS VERIFICATION |
| HAB-V-006 | Validator exit-code contract for habitat-specific denials (modeled-as-critical, sensitive-join). | `tools/validators/...` + pinned exit-code matrix (pending ADR) | NEEDS VERIFICATION |
| HAB-V-007 | Owners + CODEOWNERS for `docs/domains/habitat/` and sibling segments. | `.github/CODEOWNERS` + per-root README owner lines | NEEDS VERIFICATION |
| HAB-V-008 | Runbook subfolder convention (e.g., `docs/runbooks/habitat/` vs. flat `docs/runbooks/habitat_*.md`). | ADR or accepted convention in `docs/runbooks/README.md` | NEEDS VERIFICATION |
| HAB-V-009 | **Path-form conflict:** Directory Rules §12 segment form (`contracts/domains/habitat/`) vs Atlas §24.13 flat form (`contracts/habitat/`). | ADR resolving the two governing docs; `docs/registers/DRIFT_REGISTER.md` entry. **Interim disposition: §12 segment form governs (Atlas §24 tables are navigational-not-authoritative).** | CONFLICTED / NEEDS ADR |
| HAB-V-010 | Whether Habitat carries `policy/domains/habitat/` of its own, or inherits sensitivity through the joined lane's policy home. | Directory-Rules §12 check + Atlas §24.13 (lists no Habitat `policy/sensitivity/` root). | NEEDS VERIFICATION |

[⬆ back to top](#top)

---

## 15. Changelog & definition of done

### 15.1 Changelog v1 → v1.1

| Change | Type (per contract §37) | Reason |
|---|---|---|
| Aligned §3 source-role labels to the CONFIRMED 7-role enum (`observed \| regulatory \| modeled \| aggregate \| administrative \| candidate \| synthetic`). | reconciliation | Atlas §24.1.1 confirms the enum and the role of each habitat source family (USFWS = regulatory, NLCD = observed, GAP/LANDFIRE = modeled, NatureServe = aggregate, PAD-US = administrative). |
| Surfaced the Directory Rules §12 vs Atlas §24.13 path-form conflict (§2 callout, HAB-V-009). | gap closure | Two governing docs disagree on segment vs flat form; Atlas §24 is navigational-not-authoritative, so §12 governs. |
| Added HAB-V-009 (path-form) and HAB-V-010 (`policy/domains/habitat/` ownership) to the backlog. | gap closure | Makes the open path questions explicit and ADR-routed. |
| Pinned `CONTRACT_VERSION = "3.0.0"` in meta block, badge row, and impact table. | housekeeping | Required for doctrine-adjacent docs. |
| Normalized object-family display names to Atlas spelling (`Habitat Quality Score`, `Restoration Opportunity`, `Model Run Receipt`). | clarification | Keeps ubiquitous language stable across the doc suite. |
| Quoted all Mermaid node and edge labels containing `/`, `(`, `)`, `·`. | housekeeping | Mermaid-safety rule. |
| Added a consolidated changelog + definition-of-done section (§15). | new | Companion-section pattern for standard/doctrine-adjacent docs. |
| Bumped version v1 → v1.1; `updated` → 2026-06-05. | housekeeping | MINOR bump: reconciliation + gap closure, no operating-law change. |

> **Backward compatibility.** Section anchors §1–§14 are preserved. The prior §15 "Related folders & docs" and §16 "ADRs" sections were consolidated into the new §16 "Related folders, docs & ADRs"; inbound links to `#15-related-folders--docs` and `#16-adrs` should be repointed to `#16-related-folders-docs--adrs`. A new §15 (Changelog & DoD) was inserted.

### 15.2 Definition of done

This README is done enough to enter the repository when:

- it is placed at `docs/domains/habitat/README.md` per Directory Rules §12 — **with HAB-V-009 path-form conflict logged in `docs/registers/DRIFT_REGISTER.md`** before sibling-segment files are created;
- a docs steward and the habitat domain steward review it; policy steward signs off on §7 sensitivity posture;
- it is linked from `docs/domains/README.md` and the doctrine/standards index;
- it does not conflict with accepted ADRs (notably ADR-0001) and routes open ADR-class questions (HAB-V-006, HAB-V-008, HAB-V-009) correctly;
- the `GENERATED_RECEIPT.json` planned in the PR is wired into CI with `contract_version: "3.0.0"`;
- future changes follow the operating contract's §37 lifecycle.

[⬆ back to top](#top)

---

## 16. Related folders, docs & ADRs

### 16.1 Related folders & docs

- **Doctrine.** [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md) · [`docs/doctrine/lifecycle-law.md`](../../doctrine/lifecycle-law.md) · [`docs/doctrine/trust-membrane.md`](../../doctrine/trust-membrane.md) · [`docs/doctrine/truth-posture.md`](../../doctrine/truth-posture.md)
- **Sibling domain READMEs.** [`docs/domains/fauna/README.md`](../fauna/README.md) · [`docs/domains/flora/README.md`](../flora/README.md) · [`docs/domains/hydrology/README.md`](../hydrology/README.md) · [`docs/domains/soil/README.md`](../soil/README.md) · [`docs/domains/hazards/README.md`](../hazards/README.md)
- **Architecture.** [`docs/architecture/governed-api.md`](../../architecture/governed-api.md) · [`docs/architecture/map-shell.md`](../../architecture/map-shell.md) · [`docs/architecture/contract-schema-policy-split.md`](../../architecture/contract-schema-policy-split.md)
- **Standards.** [`docs/standards/PROV.md`](../../standards/PROV.md) · [`docs/standards/ISO-19115.md`](../../standards/ISO-19115.md) · [`docs/standards/PMTILES.md`](../../standards/PMTILES.md) · [`docs/standards/OGC-API-TILES.md`](../../standards/OGC-API-TILES.md) · [`docs/standards/OAI-PMH.md`](../../standards/OAI-PMH.md)
- **Sources.** [`docs/sources/SOURCE_DESCRIPTOR_STANDARD.md`](../../sources/SOURCE_DESCRIPTOR_STANDARD.md)
- **Registers.** [`docs/registers/AUTHORITY_LADDER.md`](../../registers/AUTHORITY_LADDER.md) · [`docs/registers/DRIFT_REGISTER.md`](../../registers/DRIFT_REGISTER.md) · [`docs/registers/VERIFICATION_BACKLOG.md`](../../registers/VERIFICATION_BACKLOG.md)
- **Operating contract.** [`ai-build-operating-contract.md`](../../../ai-build-operating-contract.md) *(`CONTRACT_VERSION = "3.0.0"`)*
- **Lane siblings (responsibility roots — Directory Rules §12 segment form).**
  - `contracts/domains/habitat/` — object meanings
  - `schemas/contracts/v1/domains/habitat/` — object shape (ADR-0001 home)
  - `policy/domains/habitat/` — allow / deny / restrict / abstain
  - `tests/domains/habitat/` · `fixtures/domains/habitat/`
  - `pipelines/domains/habitat/` · `pipeline_specs/habitat/`
  - `data/raw|work|quarantine|processed/habitat/` · `data/catalog/domain/habitat/` · `data/published/layers/habitat/`
  - `data/registry/sources/habitat/`
  - `release/candidates/habitat/`

> [!NOTE]
> Links above are **relative** and **PROPOSED**. Any link to a file not yet present should remain in this list as a placeholder so the verification backlog stays explicit. Path form follows Directory Rules §12 (segment form), pending HAB-V-009 resolution.

### 16.2 ADRs

| ADR | Title | Status | Bearing on Habitat |
|---|---|---|---|
| **ADR-0001** | Schema home (`schemas/contracts/v1/...` canonical) | **accepted** (CONFIRMED) | Habitat schemas MUST land under `schemas/contracts/v1/domains/habitat/`. No parallel home. |
| **ADR-S-04** | Source-role enum — canonical vocabulary & evolution rule | proposed (Atlas §24.12 backlog) | Pins the 7-role enum used in §3; reason-code/role stability. |
| **ADR-S-05** | Sensitivity tier scheme (T0–T4) — adopt or revise | proposed (Atlas §24.12 backlog) | Governs the public-release tiers referenced in §7. |
| **ADR-S-14** | Cross-lane join policy | proposed (Atlas §24.12 backlog) | Governs habitat × fauna / flora join review/deny posture (§7, §8). |
| **ADR-TBD** | Validator exit-code contract | proposed | Pins finite-outcome codes for habitat denials (modeled-as-critical, sensitive-join). See HAB-V-006. |
| **ADR-TBD** | `PROV.md` vs `PROVENANCE.md` naming | proposed | Affects how this README's `docs/standards/PROV.md` link resolves once normalized. |
| **ADR-TBD** | Runbook subfolder convention | proposed | Affects `docs/runbooks/habitat/...` vs flat prefix. See HAB-V-008. |
| **ADR-TBD** | **Path-form reconciliation:** Directory Rules §12 segment form vs Atlas §24.13 flat form | proposed | Resolves HAB-V-009. Interim: §12 segment form governs (Atlas §24 tables navigational-not-authoritative). |

[⬆ back to top](#top)

---

<details>
<summary><b>Appendix A — Source-role anti-collapse quick reference (expand)</b></summary>

KFM treats source role as a first-class identity attribute (Atlas §24.1, CONFIRMED). The canonical enum is `observed | regulatory | modeled | aggregate | administrative | candidate | synthetic`. For Habitat in particular:

| Role | Habitat example | Forbidden relabeling |
|---|---|---|
| **observed** | NLCD land-cover classification at a place + time; field survey | Never call an observed land-cover sample a "regulatory" designation. |
| **regulatory** | USFWS designated critical-habitat unit; NWI wetland regulatory class | Never call a critical-habitat unit an "observation" or a "modeled" estimate. |
| **modeled** | GAP/LANDFIRE ecological-system classification; suitability raster; corridor least-cost surface | Never serve a modeled suitability surface as a regulatory critical habitat. |
| **aggregate** | NatureServe summary; county-level habitat totals | Never treat as per-place evidence; carry an aggregation receipt. |
| **administrative** | PAD-US stewardship boundary | Never collapse with observation or regulation. |
| **candidate** | Quarantined connector output; unmerged habitat-model candidate | May be cited as candidate in WORK / QUARANTINE; no PUBLISHED edge until promoted. |
| **synthetic** | Reconstructed scene; AI-drafted habitat summary | Carries a Reality Boundary Note + Representation Receipt; never presented as observed reality. |

The lifecycle and the governed API both fail closed when these roles are conflated. **(CONFIRMED — Atlas §24.1.1–§24.1.2.)**

</details>

<details>
<summary><b>Appendix B — Habitat × Fauna thin-slice acceptance sketch (expand)</b></summary>

The thin slice (PROPOSED) is the proof that the Habitat lane can publish one occurrence-to-habitat assignment **safely**:

1. **One Kansas habitat patch fixture** (e.g., NLCD-derived) under `fixtures/domains/habitat/thin_slice/`.
2. **One public-safe fauna occurrence** (Fauna-owned, geoprivacy-transformed) cited via EvidenceRef.
3. **One assignment** linking the patch to the occurrence under a governed relation, with EvidenceBundle support.
4. **One ValidationReport** clean for schema, geometry, time, identity, evidence, rights, sensitivity.
5. **One PolicyDecision** = allow (deny-by-default for any unresolved sensitivity).
6. **One PromotionDecision** + **ReleaseManifest** + **RollbackCard**.
7. **One LayerManifest** + **generalized public tile** + **EvidenceDrawerPayload**.
8. **One Focus-Mode answer** with finite outcome and AIReceipt; citation validation green.
9. **One rollback drill** completing cleanly.

Acceptance is reached when each of (1)–(9) exists, is digest-closed, and a no-network CI run passes.

</details>

---

**Last updated:** 2026-06-05 · **Status:** draft · **Authority:** canonical (under `docs/`) · **Contract:** `CONTRACT_VERSION = "3.0.0"` · **Lifecycle posture:** deny-by-default for sensitive joins.

[⬆ back to top](#top)
