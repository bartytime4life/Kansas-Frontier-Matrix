<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs/domains/settlements-infrastructure/CANONICAL_PATHS
title: Canonical Paths — Settlements / Infrastructure Domain
type: standard
version: v1.1
status: draft
owners: <Docs steward + Settlements/Infrastructure lane steward — TODO confirm via CODEOWNERS>
created: 2026-05-19
updated: 2026-06-07
policy_label: public
related:
  - ai-build-operating-contract.md            # canonical operating contract, CONTRACT_VERSION = "3.0.0"
  - docs/doctrine/directory-rules.md
  - docs/domains/settlements-infrastructure/README.md
  - docs/domains/settlements-infrastructure/ARCHITECTURE.md
  - docs/atlases/KFM_Domains_Culmination_Atlas_v1_1.pdf
  - docs/registers/DRIFT_REGISTER.md
  - docs/registers/VERIFICATION_BACKLOG.md
  - docs/adr/ADR-0001-schema-home.md
tags: [kfm, doctrine, directory-rules, domains, settlements-infrastructure, canonical-paths]
notes:
  - "CONTRACT_VERSION = \"3.0.0\" — doctrine-adjacent doc; operating-contract pin carried."
  - "Doctrine of canonical paths is CONFIRMED per Directory Rules §4 Step 3 / §12."
  - "Specific path presence in any mounted repo is NEEDS VERIFICATION until inspected."
  - "Slug variance between Directory Rules §4/§12 and Atlas v1.1 Ch. 24.13 / Encyclopedia §5.1 is filed as OPEN-CP-01 (CONFLICTED, ADR-class per §2.4(5); = ADR-S-01)."
[/KFM_META_BLOCK_V2] -->

# Canonical Paths — Settlements / Infrastructure Domain

> Authoritative single-page registry of **where Settlements/Infrastructure lives** across the KFM responsibility roots. Resolves any “what folder does this go in?” question for files owned by — or routed through — the Settlements/Infrastructure lane.

![Doctrine](https://img.shields.io/badge/doctrine-CONFIRMED-2c7be5)
![Path presence](https://img.shields.io/badge/repo--presence-NEEDS%20VERIFICATION-orange)
![Domain](https://img.shields.io/badge/domain-settlements--infrastructure-7048e8)
![Sensitivity](https://img.shields.io/badge/posture-critical--asset%20deny%20lane-c92a2a)
![Lifecycle](https://img.shields.io/badge/lifecycle-RAW%20%E2%86%92%20PUBLISHED-1c7c54)
![Contract](https://img.shields.io/badge/CONTRACT__VERSION-3.0.0-black)
![Status](https://img.shields.io/badge/status-draft-lightgrey)

<!-- TODO: CI / docs-lint / link-check badges once badge endpoints are CONFIRMED in repo. -->

|Field                  |Value                                                                                                    |
|-----------------------|---------------------------------------------------------------------------------------------------------|
|**Status**             |`draft`                                                                                                  |
|**Owners**             |Docs steward + Settlements/Infrastructure lane steward *(placeholder — confirm via CODEOWNERS)*          |
|**Contract**           |`CONTRACT_VERSION = "3.0.0"`                                                                             |
|**Doctrinal anchor**   |Directory Rules §3, §4 (Step 3), §12 (Domain Placement Law)                                              |
|**Domain slug**        |`settlements-infrastructure`                                                                             |
|**Sensitivity posture**|T4 default for critical-asset detail; T1 for generalized footprints; T0 for legal-status settlement names|
|**Last updated**       |2026-06-07                                                                                               |

-----

## 📑 Contents

- [1. Scope and role of this document](#1-scope-and-role-of-this-document)
- [2. Doctrinal basis](#2-doctrinal-basis)
- [3. Domain slug — why `settlements-infrastructure`](#3-domain-slug--why-settlements-infrastructure)
- [4. Canonical-path map](#4-canonicalpath-map)
- [5. Lane-by-lane canonical paths](#5-lanebylane-canonical-paths)
- [6. Sensitivity-aware policy lanes](#6-sensitivityaware-policy-lanes)
- [7. Cross-domain placement](#7-crossdomain-placement)
- [8. Compatibility roots and anti-patterns](#8-compatibility-roots-and-antipatterns)
- [9. Reviewer placement checklist](#9-reviewer-placement-checklist)
- [10. Open questions register](#10-open-questions-register)
- [11. Related docs](#11-related-docs)
- [12. Glossary](#12-glossary)

-----

## 1. Scope and role of this document

This document is a **per-domain canonical-path registry**. It enumerates every responsibility-root lane segment that the Settlements/Infrastructure domain may legitimately occupy, and pins each enumeration to a doctrinal citation. It is the single page a reviewer should reach for when asking *“does this Settlements/Infrastructure-related file go here or there?”*.

**This document is.** A doctrine-grounded path index for the Settlements/Infrastructure lane. A reviewer’s quick-reference. A reconciliation surface for naming variance across KFM sources (Directory Rules vs Atlas v1.1 vs Encyclopedia).

**This document is not.** A claim that any of these paths currently exists in the mounted repository. It is not a substitute for `contracts/`, `schemas/`, `policy/`, or per-root READMEs that define **what** lives there — only **where** it lives. It is not an authority for **whether** a file should exist; that is decided by source descriptors, ADRs, schemas, contracts, and reviews.

> [!IMPORTANT]
> Per Directory Rules §5 (“Status of the rules below: CONFIRMED; status of any specific repo’s presence: PROPOSED until verified”), **the rules below are CONFIRMED doctrine; any specific path’s presence in a mounted repo is PROPOSED / NEEDS VERIFICATION until inspected.** This document does not promote a proposed path to repo fact.

[↑ back to top](#-contents)

-----

## 2. Doctrinal basis

This registry derives from the following CONFIRMED sources:

|Source                                                   |Authority for                                                                                       |Truth label                                                                                 |
|---------------------------------------------------------|----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------|
|`ai-build-operating-contract.md` (CONTRACT_VERSION 3.0.0)|The operating spine; truth labels; evidence rule                                                    |CONFIRMED                                                                                   |
|Directory Rules §3 (the Deeper Rule)                     |Which folders may be roots; “responsibility root wins over topic name”                              |CONFIRMED                                                                                   |
|Directory Rules §4 (placement protocol, Steps 1–5)       |The five-step placement decision (responsibility → lifecycle → domain → authority → cite)           |CONFIRMED                                                                                   |
|Directory Rules §4 Step 3 + §12 (Domain Placement Law)   |The lane pattern: domains live as **segments** under responsibility roots, never as **root folders**|CONFIRMED                                                                                   |
|Directory Rules §6.1 (`docs/` tree)                      |Enumeration of `docs/domains/settlements-infrastructure/` as a canonical domain folder              |CONFIRMED                                                                                   |
|Directory Rules §13.4 / Atlas §24.9.1                    |“Domain folder at repo root” named anti-pattern (`settlements/` forbidden)                          |CONFIRMED                                                                                   |
|Atlas v1.1 Ch. 14 (Settlements / Infrastructure)         |Domain identity, ownership, cross-lane relations, sensitivity posture                               |CONFIRMED doctrine / PROPOSED implementation                                                |
|Atlas v1.1 Ch. 24.13 (responsibility-root crosswalk)     |Domain ↔ responsibility-root mapping (uses singular `settlement/`)                                  |CONFIRMED text; **CONFLICTED** vs §4/§12 — see [§10 OPEN-CP-01](#10-open-questions-register)|
|Encyclopedia §5.1 / §7.12 (per-domain index)             |Restates the Atlas crosswalk with sensitivity tiers                                                 |CONFIRMED text; same variance                                                               |


> [!NOTE]
> **Conflict precedence (corrected).** Directory Rules do not contain a one-line “§2.2 wins on paths” clause. The governing rule is **§2.5**: where the repo (or another doc) contradicts the Rules, *do not silently conform* — open a drift entry, mark affected paths `PROPOSED / CONFLICTED`, and resolve by ADR. Creating a parallel schema/policy/contract home is **ADR-class per §2.4(5)**. This document therefore treats Directory Rules §4/§12 as the **working canonical form** while flagging the Atlas §24.13 form as variance under OPEN-CP-01 — it does **not** unilaterally declare one the winner.

[↑ back to top](#-contents)

-----

## 3. Domain slug — why `settlements-infrastructure`

The canonical domain segment for this lane is **`settlements-infrastructure`** (lowercase, hyphenated). This is:

- CONFIRMED in Directory Rules §6.1, which lists `docs/domains/settlements-infrastructure/` alongside the other domain folders.
- CONFIRMED in Directory Rules §4 Step 3 / §12, whose lane pattern applies the hyphenated slug across responsibility roots.
- Consistent with the hyphenated convention used by sibling domains (`roads-rail-trade`, `people-dna-land`).

The Atlas v1.1 Ch. 24.13 crosswalk uses **`settlement/`** (singular, no `domains/` segment) as a `contracts/`/`schemas/` lane name, and `policy/sensitivity/infrastructure/` for the deny lane. These are projections from the dossier short-name `[DOM-SETTLE]`; they conflict in *path shape* with §4/§12 and are filed as OPEN-CP-01. See [§10](#10-open-questions-register).

|Surface                                                         |Slug form                   |Truth label                                    |
|----------------------------------------------------------------|----------------------------|-----------------------------------------------|
|`docs/domains/<slug>/`                                          |`settlements-infrastructure`|CONFIRMED (Directory Rules §6.1)               |
|`schemas/contracts/v1/domains/<slug>/` (per §4 Step 3)          |`settlements-infrastructure`|CONFIRMED doctrine / NEEDS VERIFICATION in repo|
|Atlas crosswalk `schemas/contracts/v1/<slug>/` (per Atlas 24.13)|`settlement`                |**CONFLICTED** — see OPEN-CP-01                |
|Policy crosswalk `policy/sensitivity/<slug>/` (per Atlas 24.13) |`infrastructure`            |**CONFLICTED** — see OPEN-CP-01 / OPEN-CP-02   |
|Dossier short-name                                              |`[DOM-SETTLE]`              |CONFIRMED (Atlas v1.0 §2; v1.1 Appx. B)        |

[↑ back to top](#-contents)

-----

## 4. Canonical-path map

The diagram below summarizes the responsibility-root reach of the Settlements/Infrastructure lane. Topology only — no claim is made about which boxes currently exist in any mounted repo.

```mermaid
flowchart LR
  subgraph Doc["docs/ — human control plane"]
    D1["docs/domains/settlements-infrastructure/"]
  end

  subgraph CP["control_plane/ — machine indexes"]
    CP1["domain_lane_register.yaml (entry)"]
    CP2["source_authority_register.yaml (entries)"]
  end

  subgraph Meaning["contracts/ — object meaning"]
    C1["contracts/domains/settlements-infrastructure/ (per §4/§12)"]
    C1b["contracts/settlement/ (per Atlas 24.13) — variance"]
  end

  subgraph Shape["schemas/ — machine shape"]
    S1["schemas/contracts/v1/domains/settlements-infrastructure/ (per §4/§12)"]
    S1b["schemas/contracts/v1/settlement/ (per Atlas 24.13) — variance"]
  end

  subgraph Pol["policy/ — admissibility and release"]
    P1["policy/domains/settlements-infrastructure/ (per §4/§12)"]
    P2["policy/sensitivity/infrastructure/ (per Atlas 24.13)"]
  end

  subgraph Proof["tests/ + fixtures/"]
    T1["tests/domains/settlements-infrastructure/"]
    F1["fixtures/domains/settlements-infrastructure/"]
  end

  subgraph Code["packages/ + connectors/ + pipelines/"]
    K1["packages/domains/settlements-infrastructure/"]
    K2["connectors/&lt;source-id&gt;/ (emits to data/raw/)"]
    K3["pipelines/domains/settlements-infrastructure/"]
    K4["pipeline_specs/settlements-infrastructure/"]
  end

  subgraph Data["data/ — lifecycle"]
    DA1["data/raw/settlements-infrastructure/"]
    DA2["data/work/settlements-infrastructure/"]
    DA3["data/quarantine/settlements-infrastructure/"]
    DA4["data/processed/settlements-infrastructure/"]
    DA5["data/catalog/domain/settlements-infrastructure/"]
    DA6["data/published/layers/settlements-infrastructure/"]
    DA7["data/registry/sources/settlements-infrastructure/"]
  end

  subgraph Rel["release/ — decisions"]
    R1["release/candidates/settlements-infrastructure/"]
  end

  subgraph Gov["apps/ — governed API (trust membrane)"]
    G1["apps/governed-api/ (settlements/infra routes — public-safe only)"]
  end

  D1 --> CP1
  CP2 --> K2
  K2 --> DA1
  K3 -.->|"uses"| K4
  DA1 --> DA2
  DA2 -.->|"fail"| DA3
  DA2 --> DA4
  DA4 --> DA5
  DA5 --> R1
  R1 --> DA6
  DA6 --> G1
  S1 -.->|"validates"| DA2
  C1 -.->|"defines meaning of"| S1
  P1 -.->|"gates"| DA2
  P2 -.->|"gates"| DA5
  T1 -.->|"proves"| S1
  F1 -.->|"supplies"| T1
```

> [!NOTE]
> Two pairs of variance boxes (`contracts/settlement/` vs `contracts/domains/settlements-infrastructure/`, and `schemas/contracts/v1/settlement/` vs `schemas/contracts/v1/domains/settlements-infrastructure/`) reflect a real disagreement between Directory Rules §4/§12 and Atlas v1.1 Ch. 24.13 (whose row 14 reads `schemas/contracts/v1/settlement/; contracts/settlement/; policy/sensitivity/infrastructure/`). Until OPEN-CP-01 is resolved by ADR, **Directory Rules §4/§12 is the working canonical form**.

[↑ back to top](#-contents)

-----

## 5. Lane-by-lane canonical paths

The table below enumerates every responsibility root that may legitimately host a Settlements/Infrastructure-segment file. Paths are written as **PROPOSED** unless explicitly verified in a mounted repo. The **doctrine** of the lane pattern is CONFIRMED per Directory Rules §4 Step 3 / §12; the **specific path text** is the form Directory Rules §4 Step 3 prescribes (enumeration confirmed verbatim).

### 5.1 Authority / governance roots

|Responsibility root|Canonical path (PROPOSED)                                                                                  |What lives here                                                                                                                                                                                                                                                     |Doctrine                  |Truth label                                                                                    |
|-------------------|-----------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|-----------------------------------------------------------------------------------------------|
|`docs/`            |`docs/domains/settlements-infrastructure/`                                                                 |Domain README, this CANONICAL_PATHS, ARCHITECTURE, dossier excerpts, ADR backlog, sensitivity briefs                                                                                                                                                                |§6.1, §4 Step 3           |CONFIRMED doctrine / NEEDS VERIFICATION presence                                               |
|`control_plane/`   |`control_plane/domain_lane_register.yaml` (entry), `control_plane/source_authority_register.yaml` (entries)|Machine-readable registry **entries** for this lane (not a per-domain file)                                                                                                                                                                                         |§6.2                      |CONFIRMED doctrine / NEEDS VERIFICATION presence                                               |
|`contracts/`       |`contracts/domains/settlements-infrastructure/`                                                            |Object meaning: `Settlement`, `Municipality`, `CensusPlace`, `Townsite`, `GhostTown`, `Fort`, `Mission`, `ReservationCommunity`, `InfrastructureAsset`, `NetworkNode`, `NetworkSegment`, `Facility`, `ServiceArea`, `Operator`, `ConditionObservation`, `Dependency`|§6.3, §4 Step 3           |CONFIRMED doctrine (Atlas Ch. 14 §B owns this set) / NEEDS VERIFICATION presence               |
|`schemas/`         |`schemas/contracts/v1/domains/settlements-infrastructure/`                                                 |JSON Schemas for every contract above; `schemas/tests/valid/` and `schemas/tests/invalid/` carry golden samples                                                                                                                                                     |§6.4 (ADR-0001), §4 Step 3|CONFIRMED doctrine / NEEDS VERIFICATION presence / **CONFLICTED** with Atlas 24.13 → OPEN-CP-01|
|`policy/`          |`policy/domains/settlements-infrastructure/` **and** `policy/sensitivity/infrastructure/` (per Atlas 24.13)|Sensitivity classification, redaction, and release policy for critical-asset detail                                                                                                                                                                                 |§6.5, §4 Step 3           |CONFIRMED doctrine / NEEDS VERIFICATION presence / **CONFLICTED** → OPEN-CP-01 / OPEN-CP-02    |

### 5.2 Proof roots

|Responsibility root|Canonical path (PROPOSED)                     |What lives here                                                                       |
|-------------------|----------------------------------------------|--------------------------------------------------------------------------------------|
|`tests/`           |`tests/domains/settlements-infrastructure/`   |Validator tests, deny-lane proofs, public-safe no-leak tests, condition-temporal tests|
|`fixtures/`        |`fixtures/domains/settlements-infrastructure/`|Golden valid / invalid sample data for the tests above                                |

Per Atlas Ch. 14 §K, the Settlements/Infrastructure test families include — all PROPOSED implementation:

- Legal municipality evidence tests
- Census-vs-municipality distinction tests
- Infrastructure topology tests
- `observed_at` temporal tests for condition observations
- **Restricted-geometry no-leak tests** *(critical-asset deny lane)*
- Catalog / proof / release closure tests
- Negative-state coverage (every validator exercises `DENY` / `ABSTAIN` / `ERROR` / `FAIL`)

### 5.3 Code roots

|Responsibility root|Canonical path (PROPOSED)                                                                                                  |What lives here                                                                                                                                                                                 |
|-------------------|---------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|`packages/`        |`packages/domains/settlements-infrastructure/`                                                                             |Shared lane libraries: identity helpers, normalization adapters, generalization utilities                                                                                                       |
|`connectors/`      |`connectors/<source-id>/` (**no `domains/` segment** — confirmed: connectors absent from the §4 Step 3 domain-segment list)|Source-specific fetchers / admitters. Connectors **do not publish**: they emit to `data/raw/<domain>/` or `data/quarantine/<domain>/` — Directory Rules §13.5 (Connector-publishes anti-pattern)|
|`pipelines/`       |`pipelines/domains/settlements-infrastructure/`                                                                            |Executable promotion logic                                                                                                                                                                      |
|`pipeline_specs/`  |`pipeline_specs/settlements-infrastructure/`                                                                               |Declarative pipeline configuration (note: **no `domains/` segment** here per §4 Step 3 — confirmed verbatim)                                                                                    |
|`tools/`           |`tools/validators/<topic>/` (cross-domain shared tooling lives **without** a domain segment)                               |Repo-wide validators that may include Settlements/Infrastructure cases                                                                                                                          |

### 5.4 Lifecycle data root

Per Directory Rules §4 Step 2, files under `data/` carry an explicit phase. Per §4 Step 3, **the domain segment follows the phase** — `data/<phase>/<domain>/` — and does **not** appear under a `domains/` sub-segment (confirmed verbatim).

|Phase     |Canonical path (PROPOSED)                          |Promotion gate (Atlas Ch. 14 §H)                                                                      |
|----------|---------------------------------------------------|------------------------------------------------------------------------------------------------------|
|RAW       |`data/raw/settlements-infrastructure/`             |`SourceDescriptor` exists; rights, sensitivity, citation, time, hash captured                         |
|WORK      |`data/work/settlements-infrastructure/`            |Schema, geometry, time, identity, evidence, rights, and policy normalization runnable                 |
|QUARANTINE|`data/quarantine/settlements-infrastructure/`      |Validation or policy failure; reason recorded; **never silently promotes**                            |
|PROCESSED |`data/processed/settlements-infrastructure/`       |`EvidenceRef`, `ValidationReport`, and digest closure exist; `RedactionReceipt` if sensitivity applies|
|CATALOG   |`data/catalog/domain/settlements-infrastructure/`  |`CatalogMatrix` entry; `EvidenceBundle`; graph/triplet projections if applicable                      |
|PUBLISHED |`data/published/layers/settlements-infrastructure/`|`ReleaseManifest`, rollback target, correction path, `ReviewRecord` where required                    |

Adjacent emitted artifacts (per §4 Step 2: receipts, proofs, registry, rollback **are emitted alongside lifecycle directories; they do not replace them**):

|Artifact                            |Canonical path (PROPOSED)                                                                                                            |
|------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|
|Receipts                            |`data/receipts/settlements-infrastructure/`                                                                                          |
|Proofs (`EvidenceBundle` resolution)|`data/proofs/settlements-infrastructure/`                                                                                            |
|Source registry                     |`data/registry/sources/settlements-infrastructure/` (or `data/registry/settlements-infrastructure/` — both forms appear in §4 Step 3)|
|Rollback targets                    |`data/rollback/settlements-infrastructure/`                                                                                          |


> [!CAUTION]
> Per Directory Rules §13.5 (Watcher-as-non-publisher invariant) and §13 (Lifecycle-skip anti-pattern), a pipeline **MUST NOT** write directly from `data/raw/settlements-infrastructure/` to `data/published/layers/settlements-infrastructure/`. Every phase runs; promotion is a governed state transition.

### 5.5 Release root

|Surface                 |Canonical path (PROPOSED)                                                                       |
|------------------------|------------------------------------------------------------------------------------------------|
|Release candidates      |`release/candidates/settlements-infrastructure/` (confirmed in §4 Step 3)                       |
|`ReleaseManifest` files |`release/manifests/settlements-infrastructure/` *(PROPOSED — sibling convention per OPEN-CP-03)*|
|`RollbackCard` files    |`release/rollback/settlements-infrastructure/` *(PROPOSED — convention pending OPEN-CP-03)*     |
|`CorrectionNotice` files|`release/corrections/settlements-infrastructure/` *(PROPOSED — convention pending OPEN-CP-03)*  |


> [!NOTE]
> Per Directory Rules §13.2, release **decisions** live in `release/`; release **artifacts** live in `data/published/`. They are distinct.

### 5.6 Runtime / infra / examples

|Responsibility root|Canonical path (PROPOSED)                                                                                                 |Notes                                                                                              |
|-------------------|--------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|
|`runtime/`         |`runtime/adapters/<topic>/` (no domain segment)                                                                           |Local runtime adapters; never a public surface                                                     |
|`apps/`            |`apps/governed-api/` (no domain segment)                                                                                  |The **trust membrane**. Settlements/Infrastructure routes live here, not in a per-domain app folder|
|`infra/`           |`infra/` (no domain segment)                                                                                              |Deploy posture is repo-wide                                                                        |
|`configs/`         |`configs/` (no domain segment, unless a per-domain template)                                                              |Templates and defaults only — no secrets                                                           |
|`migrations/`      |`migrations/<change-id>/` (no domain segment)                                                                             |Includes a `rollback/` subtree                                                                     |
|`examples/`        |`examples/settlements-infrastructure/` *(PROPOSED — `examples/` is not in the §4 Step 3 lane enumeration; see OPEN-CP-05)*|Runnable, kept current                                                                             |

[↑ back to top](#-contents)

-----

## 6. Sensitivity-aware policy lanes

Atlas Ch. 14 §I designates Settlements/Infrastructure as a **critical-asset deny lane**, and Atlas §24.5.2 sets the tiers. The canonical-path implications:

|Lane                                                    |Sensitivity tier (Atlas 24.5.2 / 24.14) |Canonical policy path (PROPOSED)                                                       |Default outcome                                       |
|--------------------------------------------------------|----------------------------------------|---------------------------------------------------------------------------------------|------------------------------------------------------|
|Critical infrastructure asset detail                    |**T4** default                          |`policy/sensitivity/infrastructure/` *and* `policy/domains/settlements-infrastructure/`|DENY → review-then-generalize → T1                    |
|Utility / dependency edges                              |**T4** for detail; T1 for aggregate     |same                                                                                   |DENY detail; ALLOW aggregate with `AggregationReceipt`|
|Exact facility geometry                                 |**T4**                                  |same                                                                                   |DENY → `RedactionReceipt` + generalized footprint     |
|Condition observations / vulnerability                  |**T4** raw; T3 to named authorities only|same                                                                                   |DENY raw publication; never T0/T1                     |
|Legal-status `Settlement` / `Municipality` / `GhostTown`|**T0**                                  |`policy/domains/settlements-infrastructure/`                                           |ALLOW with `EvidenceBundle`                           |
|Generalized footprint of critical asset (post-review)   |**T1**                                  |same + `RedactionReceipt` in `data/receipts/`                                          |ALLOW after redaction                                 |


> [!WARNING]
> Per Atlas Ch. 14 §I and Atlas Ch. 24.9.2 trust-membrane anti-patterns: **public clients MUST NOT read from `data/processed/` or `data/catalog/` directly.** All public routes for Settlements/Infrastructure flow through `apps/governed-api/`, which enforces evidence, policy, release, and finite outcomes. Governed-surface outcomes are `ANSWER` / `ABSTAIN` / `DENY` / `ERROR`; the underlying `PolicyDecision` carries `allow | deny | restrict | hold | abstain` (distinct enums, never conflated).

The `SettlementsInfrastructureDecisionEnvelope` DTO and the layer-manifest / Evidence Drawer payload schemas land under `schemas/contracts/v1/domains/settlements-infrastructure/runtime/` (PROPOSED — pending OPEN-CP-01 resolution and ADR-S-03 receipt-class home decision).

[↑ back to top](#-contents)

-----

## 7. Cross-domain placement

Settlements/Infrastructure has CONFIRMED cross-lane relations to Roads/Rail, Hazards, Hydrology, People/Land, and Archaeology (Atlas Ch. 14 §F; Ch. 24.4). When a file legitimately spans Settlements/Infrastructure and one or more of these lanes, the Directory Rules multi-domain rule applies (confirmed verbatim):

|Situation                                                                                             |Canonical placement (per §4/§12 multi-domain rule)                 |Example                                                                       |
|------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------|------------------------------------------------------------------------------|
|Shared validator across Settlements/Infrastructure × Roads/Rail (e.g., depot–bridge–crossing topology)|`tools/validators/<topic>/` — **no domain segment**                |`tools/validators/transport-facility-topology/`                               |
|Shared schema across Settlements × Hazards (e.g., exposure indices)                                   |`schemas/contracts/v1/<topic>/` — **no domain segment**            |`schemas/contracts/v1/exposure/`                                              |
|Shared cross-lane doctrine                                                                            |`docs/architecture/<topic>.md` — **no domain segment**             |`docs/architecture/critical-asset-exposure.md`                                |
|File owned by Roads/Rail but consumed here                                                            |Lives under `roads-rail-trade` segments; cited here, not duplicated|`schemas/contracts/v1/domains/roads-rail-trade/transport-facility.schema.json`|


> [!TIP]
> The rule from Directory Rules §4/§12 is: **place a cross-cutting file under the lowest common responsibility root that owns the file’s responsibility, without a domain segment.** Picking one of the two domains as the home is drift, not a solution.

### 7.1 Object-family ownership reference

From Atlas Ch. 24.14 — these object families are **owned** by Settlements/Infrastructure (lives under the slug above) but **cited** from other lanes:

|Object family                              |Citing domains                           |Sensitivity default                         |
|-------------------------------------------|-----------------------------------------|--------------------------------------------|
|`Settlement` / `Municipality` / `GhostTown`|People/Land; Frontier Matrix; Archaeology|T0                                          |
|`InfrastructureAsset` (critical)           |Hazards (with restriction)               |**T4 default**; T1 for generalized footprint|

Conversely, the following are **cited** by Settlements/Infrastructure but **owned** elsewhere (do **not** place under Settlements/Infrastructure paths):

|Object family                                      |Owner           |Path home (per §4/§12)                          |
|---------------------------------------------------|----------------|------------------------------------------------|
|`HUC` / `Watershed` / `Reach`                      |Hydrology       |`schemas/contracts/v1/domains/hydrology/`       |
|`NFHLZone` (regulatory floodplain)                 |Hydrology       |same                                            |
|`SoilMapUnit` / `SoilComponent` (advisory)         |Soil            |`schemas/contracts/v1/domains/soil/`            |
|`RoadSegment` / `RailSegment` / `TransportFacility`|Roads/Rail      |`schemas/contracts/v1/domains/roads-rail-trade/`|
|`HazardEvent` / `DisasterDeclaration`              |Hazards         |`schemas/contracts/v1/domains/hazards/`         |
|`PersonAssertion` (with restrictions)              |People/Genealogy|`schemas/contracts/v1/domains/people-dna-land/` |


> [!NOTE]
> The owner-side path homes in the right column follow Directory Rules §4/§12 (`domains/<domain>/`). The Atlas §24.13 crosswalk renders these in short form (e.g., `schemas/contracts/v1/hydrology/`); the same OPEN-CP-01 variance applies repo-wide, not only to this lane.

[↑ back to top](#-contents)

-----

## 8. Compatibility roots and anti-patterns

### 8.1 What `settlements-infrastructure/` MUST NOT become

Per Directory Rules §3, §13.4, and Atlas §24.9.1 (“Domain folder at repo root”), a root folder named `settlements-infrastructure/` (or `settlements/`) at the **repo root** is forbidden — `settlements` is explicitly named among the forbidden domain-root names in §3:

```text
# FORBIDDEN — domain folder at repo root (Directory Rules §13.4 / Atlas §24.9.1)
settlements-infrastructure/
├── data/
├── schemas/
├── policy/
└── docs/
```

This pattern competes with responsibility roots, fragments the lifecycle, and creates parallel authority homes. The fix is to migrate every file into the lane pattern shown in [§5](#5-lanebylane-canonical-paths).

### 8.2 Other anti-patterns specifically risky for this domain

|Anti-pattern                                                                                                          |Why it’s risky here                                                                                       |Counter-rule                                                                        |
|----------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
|Critical-asset detail leaked through `data/processed/` to a public client                                             |T4 deny lane bypassed                                                                                     |All public reads go through `apps/governed-api/`; trust membrane (§6)               |
|`policy/sensitivity/infrastructure/` and `policy/domains/settlements-infrastructure/` evolving in parallel without ADR|Two parallel policy homes; reviewers can’t tell which is authoritative                                    |Single policy home per topic; ADR if both are needed; see OPEN-CP-02                |
|`RedactionReceipt` for generalized footprint stored in `artifacts/`                                                   |Trust-bearing receipt in build-scratch root (§13.2 / Atlas §24.9.1 “Artifacts directory holding receipts”)|Receipts live in `data/receipts/settlements-infrastructure/`, never `artifacts/`    |
|`ConditionObservation` schema authored next to a CSV instance                                                         |Schema-alongside-data drift (§13 / Atlas §24.9.1 “Schema authored alongside data file”)                   |Shape under `schemas/`; meaning under `contracts/`; instance under `data/`          |
|Aggregate `ServiceArea` cited as per-place observation                                                                |Source-role collapse (Atlas §24.9.2 / §24.1)                                                              |Validator + Focus Mode citation evaluator enforces aggregate vs per-place separation|
|Two parallel schema homes (`settlement/` and `domains/settlements-infrastructure/`)                                   |Reviewers cannot tell which schema is authoritative (Atlas §24.9.1)                                       |Single schema home under ADR-0001; resolve via OPEN-CP-01                           |

[↑ back to top](#-contents)

-----

## 9. Reviewer placement checklist

When reviewing a PR that adds, moves, or renames a Settlements/Infrastructure-related path, work through this list (extends Directory Rules §16):

- [ ] **Responsibility identified.** Maps to exactly one of Directory Rules §4 Step 1 categories.
- [ ] **Right root.** Chosen root matches that responsibility (use [§5](#5-lanebylane-canonical-paths) as the lookup).
- [ ] **Domain segment correct.** Slug is `settlements-infrastructure` (not `settlement`, `settlements`, `infrastructure`, or `settlement-and-infrastructure`) unless OPEN-CP-01 has been resolved otherwise by ADR.
- [ ] **`domains/` segment present where §4 Step 3 requires it.** Specifically under `docs/`, `contracts/`, `schemas/contracts/v1/`, `policy/`, `tests/`, `fixtures/`, `packages/`, `pipelines/`.
- [ ] **`domains/` segment absent where §4 Step 3 forbids it.** Specifically under `pipeline_specs/`, `data/<phase>/`, `release/candidates/`, `connectors/`, `tools/`, `runtime/`, `apps/`, `infra/`, `configs/`, `migrations/`.
- [ ] **Lifecycle phase correct** (data only). File is in the right phase; no skipping.
- [ ] **No new root without ADR.** No new canonical or compatibility root introduced silently (§2.4(1)).
- [ ] **No parallel authority.** No new schema home, policy home, receipt home, or release home created without an ADR (§2.4(5)).
- [ ] **Trust content placement.** Receipts → `data/receipts/`; proofs → `data/proofs/`; release decisions → `release/`. Never `artifacts/`.
- [ ] **Sensitivity-aware.** Critical-asset detail (T4) is not exposed through a non-governed path.
- [ ] **Public path discipline.** Public reads route through `apps/governed-api/`, not direct stores.
- [ ] **Variance flagged.** Any deviation from §4/§12 in favor of Atlas 24.13 form (`settlement/`, `policy/sensitivity/infrastructure/`) is filed against OPEN-CP-01 in `docs/registers/DRIFT_REGISTER.md`.
- [ ] **Rule cited in PR description.** PR names the Directory Rules section that justifies the placement (§4 Step 5).

> [!IMPORTANT]
> A reviewer who cannot tick every applicable box SHOULD request changes or open an entry in `docs/registers/DRIFT_REGISTER.md`.

[↑ back to top](#-contents)

-----

## 10. Open questions register

These items are tracked here for triage; resolutions migrate to `docs/registers/VERIFICATION_BACKLOG.md`, `docs/registers/DRIFT_REGISTER.md`, or `docs/adr/` as appropriate.

### Variance and ADR-class

- **OPEN-CP-01 — Slug variance between Directory Rules §4/§12 and Atlas v1.1 Ch. 24.13.** `CONFLICTED`.
  Directory Rules §4 Step 3 / §12 prescribe `schemas/contracts/v1/domains/settlements-infrastructure/` and `policy/domains/settlements-infrastructure/`. Atlas v1.1 Ch. 24.13 row 14 (and Encyclopedia §5.1 / §7.12) cite `schemas/contracts/v1/settlement/`, `contracts/settlement/`, and `policy/sensitivity/infrastructure/` — confirmed verbatim. The two forms cannot both be canonical without an ADR. Parallel to OPEN-DR-01 (`PROV.md` vs `PROVENANCE.md`) and the geology slug variance. **Resolution required by ADR (= ADR-S-01 in the §24.12 backlog; ADR-0001 confirm-or-amend).** Until resolved, this document treats Directory Rules §4/§12 as canonical and flags Atlas 24.13 form as variance.
- **OPEN-CP-02 — Sensitivity policy home: `policy/sensitivity/<topic>/` vs `policy/domains/<domain>/`.** `CONFLICTED`.
  Atlas 24.13 places critical-asset deny rules at `policy/sensitivity/infrastructure/`; Directory Rules §4 Step 3 implies `policy/domains/settlements-infrastructure/`. The actual `policy/` tree (§6.5) shows **both** a `sensitivity/` axis and a `domains/` axis exist as siblings — so the open question is whether the lane uses the sensitivity-axis home, the domain-axis home, or both with one mirroring the other. ADR-class per Directory Rules §2.4(5). **Resolution via ADR.**
- **OPEN-CP-03 — Release sub-structure for this lane.** `PROPOSED`.
  Whether `release/manifests/<domain>/`, `release/rollback/<domain>/`, and `release/corrections/<domain>/` are the correct sibling structure, or whether a flatter layout applies. (§4 Step 3 confirms only `release/candidates/<domain>/`.) Touches ADR-S-11 (story/export receipt policy) and ADR-S-03 (receipt-class home). **Resolution via ADR.**

### Repo-evidence

- **OPEN-CP-04 — Mounted-repo verification of every path above.** `NEEDS VERIFICATION`.
  Every PROPOSED path in [§5](#5-lanebylane-canonical-paths) NEEDS VERIFICATION against a mounted repo. The doctrine is CONFIRMED; presence is not.
- **OPEN-CP-05 — Per-domain `examples/` convention.** `PROPOSED`.
  Whether `examples/settlements-infrastructure/` is the convention, or examples live under `examples/<topic>/` without a domain segment. Directory Rules §4 Step 3 does not list `examples/` in the lane-pattern enumeration; §12 is silent. **Resolution via routine PR + Docs steward decision.**

### Naming and casing

- **OPEN-CP-06 — Hyphen vs underscore for the slug.** `NEEDS VERIFICATION`.
  Existing KFM convention uses hyphenated lowercase slugs (`settlements-infrastructure`, `roads-rail-trade`). NEEDS VERIFICATION that no mounted-repo file uses `settlements_infrastructure` or `SettlementsInfrastructure`. If inconsistency exists, file to `docs/registers/DRIFT_REGISTER.md`.

[↑ back to top](#-contents)

-----

## 11. Related docs

- `ai-build-operating-contract.md` — canonical operating contract; `CONTRACT_VERSION = "3.0.0"`.
- `docs/doctrine/directory-rules.md` — source of the lane-pattern doctrine (§§3, 4, 12, 13).
- `docs/domains/settlements-infrastructure/README.md` — domain orientation *(PROPOSED — TODO confirm)*.
- `docs/domains/settlements-infrastructure/ARCHITECTURE.md` — domain architecture dossier *(PROPOSED)*.
- `docs/atlases/KFM_Domains_Culmination_Atlas_v1_1.pdf` — Atlas v1.1 Ch. 14 (Settlements/Infrastructure) and Ch. 24.13 (responsibility-root crosswalk).
- `docs/encyclopedia/` — Encyclopedia §5.1 / §7.12 (per-domain index).
- `docs/adr/ADR-0001-schema-home.md` — schema-home authority (governs §5.1 schemas row).
- `docs/registers/DRIFT_REGISTER.md` — where variance entries land.
- `docs/registers/VERIFICATION_BACKLOG.md` — where NEEDS VERIFICATION items land.
- `docs/standards/PROV.md` — provenance standard *(per Directory Rules §6.1 v1.1 note; naming variance flagged as OPEN-DR-01)*.

[↑ back to top](#-contents)

-----

## 12. Glossary

<details>
<summary>Click to expand glossary</summary>

Terms used in this document with placement-disambiguating definitions. Full definitions live in `docs/doctrine/` and `contracts/`.

|Term                            |Short definition                                                                                                                                                                                                                                |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|**Authority root**              |A repo-root folder that carries one of the Directory Rules §3 responsibilities.                                                                                                                                                                 |
|**Compatibility root**          |A root that exists for legacy, mirror, deprecated, or transitional reasons (Directory Rules §8).                                                                                                                                                |
|**Critical-asset deny lane**    |The Settlements/Infrastructure posture under which utility detail, condition observations, dependencies, operator-sensitive details, and exact facility geometry default to T4 (DENY) until reviewed and generalized (Atlas Ch. 14 §I; §24.5.2).|
|**Domain segment**              |The hyphenated slug `settlements-infrastructure` appearing **inside** a responsibility root, never as a root itself.                                                                                                                            |
|**EvidenceBundle / EvidenceRef**|Resolved support package for claims; lives in `data/proofs/`. Outranks generated language.                                                                                                                                                      |
|**Governed API**                |The trust-membrane operational surface — `apps/governed-api/`. All public reads route through it.                                                                                                                                               |
|**Lane**                        |A domain or topic segment inside a responsibility root (e.g., `data/processed/settlements-infrastructure/`).                                                                                                                                    |
|**Lane pattern**                |The Directory Rules §4 Step 3 / §12 enumeration of canonical responsibility-root × domain-segment combinations.                                                                                                                                 |
|**Lifecycle invariant**         |RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED. Promotion is a governed state transition, not a file move.                                                                                                                 |
|**PolicyDecision**              |A policy verdict carrying `allow                                                                                                                                                                                                                |
|**Promotion**                   |A governed state transition between lifecycle phases. Not a file move. Atlas Ch. 14 §H gates apply.                                                                                                                                             |
|**RedactionReceipt**            |Trust-bearing record of a public-safe field or geometry transformation; emitted under `data/receipts/`.                                                                                                                                         |
|**ReleaseManifest**             |Release decision; lives in `release/`. Published artifact lives in `data/published/`.                                                                                                                                                           |
|**Responsibility root**         |One of the Directory Rules §3 canonical or compatibility root folders.                                                                                                                                                                          |
|**Sensitivity tier**            |T0 (open public) through T4 (deny default); Atlas Ch. 24.5 defines transitions.                                                                                                                                                                 |
|**Slug**                        |The hyphenated lowercase domain identifier: `settlements-infrastructure`.                                                                                                                                                                       |
|**Trust membrane**              |The boundary that prevents raw / unreviewed / model-generated / internal state from becoming public truth (Atlas Ch. 24.9.2). Operational form: `apps/governed-api/`.                                                                           |

</details>

[↑ back to top](#-contents)

-----

<sub>📂 **Canonical Paths — Settlements / Infrastructure Domain** · doc_id: `kfm://doc/docs/domains/settlements-infrastructure/CANONICAL_PATHS` · version `v1.1` (draft) · last updated **2026-06-07** · `CONTRACT_VERSION = "3.0.0"` · doctrine CONFIRMED · repo presence NEEDS VERIFICATION · [↑ back to top](#-contents)</sub>

**Related:** [`directory-rules.md`](../../doctrine/directory-rules.md) · [`README.md`](./README.md) · [`ARCHITECTURE.md`](./ARCHITECTURE.md) · [`Atlas v1.1 Ch. 14`](../../atlases/KFM_Domains_Culmination_Atlas_v1_1.pdf) · [`DRIFT_REGISTER.md`](../../registers/DRIFT_REGISTER.md) · [`VERIFICATION_BACKLOG.md`](../../registers/VERIFICATION_BACKLOG.md)

-----

## Changelog

|Version|Date      |Type (per contract §37)     |Change                                                                                                                                                                                                                                                                                                                                                                  |
|-------|----------|----------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|v1     |2026-05-19|new                         |Initial canonical-path registry; grounded in Directory Rules §3/§4/§12 + Atlas v1.1 Ch. 14 / 24.13.                                                                                                                                                                                                                                                                     |
|v1.1   |2026-06-07|reconciliation / gap closure|Pinned `CONTRACT_VERSION = "3.0.0"` (badge, Status table, footer); corrected the conflict-precedence citation from “§2.2 wins” to the actual §2.5 drift rule + §2.4(5) ADR-class clause; elevated OPEN-CP-01 / OPEN-CP-02 to `CONFLICTED` now that the Atlas §24.13 row-14 text is confirmed verbatim and tied OPEN-CP-01 to ADR-S-01; added the `PolicyDecision` `allow|


> **Backward compatibility.** H1, the `#-contents` anchor, and all section anchors preserved; section numbers unchanged. Material edits are the §2 conflict-precedence citation (corrected), the OPEN-CP labels (now CONFLICTED), and the PolicyDecision enum (added) — each flagged inline.