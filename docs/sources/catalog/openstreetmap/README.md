<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/source-family/openstreetmap
title: OpenStreetMap (Source Family)
type: standard
version: v1
status: draft
owners: Docs steward + Source steward (Roads/Rail domain steward as co-reviewer)
created: 2026-05-13
updated: 2026-05-13
policy_label: public
related:
  - docs/sources/README.md
  - docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - docs/doctrine/trust-membrane.md
  - docs/domains/roads-rail-trade/README.md
  - docs/domains/settlements-infrastructure/README.md
  - docs/domains/hydrology/README.md
  - docs/domains/archaeology/README.md
  - schemas/contracts/v1/source/source-descriptor.schema.json
  - connectors/osm/README.md
tags: [kfm, source-family, openstreetmap, osm, rights, governance]
notes:
  - Rights, attribution, and share-alike posture for KFM use remain NEEDS VERIFICATION.
  - This document is a source-family standard. It is NOT a SourceDescriptor instance.
  - Any specific path quoted here is PROPOSED until verified against mounted-repo evidence.
[/KFM_META_BLOCK_V2] -->

# 🗺️ OpenStreetMap — Source Family Standard

> Governance, rights posture, and lifecycle treatment for OpenStreetMap (OSM) inputs in the Kansas Frontier Matrix.

![status: draft](https://img.shields.io/badge/status-draft-yellow)
![authority: doctrine](https://img.shields.io/badge/authority-doctrine-blue)
![rights: NEEDS%20VERIFICATION](https://img.shields.io/badge/rights-NEEDS%20VERIFICATION-orange)
![lifecycle: RAW%20→%20PUBLISHED](https://img.shields.io/badge/lifecycle-RAW%20%E2%86%92%20PUBLISHED-informational)
![source-role: TBD](https://img.shields.io/badge/source--role-TBD-lightgrey)
<!-- Shields targets are placeholders; replace once badge endpoints are decided. -->

| Field | Value |
|---|---|
| **Status** | Draft (review pending) |
| **Owners** | Docs steward · Source steward · Roads/Rail domain steward (co-reviewer) |
| **Updated** | 2026-05-13 |
| **Authority of this document** | CONFIRMED — KFM doctrine + project source-family list |
| **Authority of OSM rights claims herein** | NEEDS VERIFICATION until a `SourceActivationDecision` is recorded |
| **Lifecycle invariant** | RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED |

---

## Contents

1. [Scope and purpose](#1-scope-and-purpose)
2. [Source identity at a glance](#2-source-identity-at-a-glance)
3. [Source role — decision, not default](#3-source-role--decision-not-default)
4. [Rights, license, and attribution](#4-rights-license-and-attribution)
5. [Sensitivity posture and deny-by-default cases](#5-sensitivity-posture-and-deny-by-default-cases)
6. [Freshness, cadence, and stale-state](#6-freshness-cadence-and-stale-state)
7. [Retrieval methods and admission boundary](#7-retrieval-methods-and-admission-boundary)
8. [Lifecycle and gates](#8-lifecycle-and-gates)
9. [Domain applicability matrix](#9-domain-applicability-matrix)
10. [Anti-patterns — what OSM is NOT](#10-anti-patterns--what-osm-is-not)
11. [Illustrative SourceDescriptor fields](#11-illustrative-sourcedescriptor-fields)
12. [Open questions and verification backlog](#12-open-questions-and-verification-backlog)
13. [Related docs](#13-related-docs)

---

## 1. Scope and purpose

OpenStreetMap is a community-maintained, global, structured geographic database. KFM project doctrine lists OSM as a **source family** in the Roads/Rail/Trade Routes domain dossier, with explicit cautions that source role, rights, and current terms are **NEEDS VERIFICATION** and that sensitive joins must **fail closed**. This document records how KFM admits, governs, and bounds OSM-derived evidence so that:

- OSM data enters the lifecycle through the same gates as any other source family.
- OSM's source role is set by **decision**, not by convenience or analogy.
- Rights, attribution, and share-alike obligations are resolved **before** any released artifact carries OSM-derived geometry, attribution, or claims.
- OSM is never silently elevated into an authoritative role it does not hold for a given object family.

> [!IMPORTANT]
> This file is a **standards / governance note** for a source family. It is **not** a `SourceDescriptor` instance. The canonical home for `SourceDescriptor` records defaults to `schemas/contracts/v1/source/source-descriptor.json` per Directory Rules §7.4 / ADR-0001; PROPOSED until verified.

---

## 2. Source identity at a glance

| Attribute | Value | Truth label |
|---|---|---|
| Source family name | OpenStreetMap | CONFIRMED in project doctrine |
| Common short name | OSM | CONFIRMED |
| Source kind | Community-edited geographic database | EXTERNAL (general knowledge) |
| KFM source ID | `src-osm` (suggested) | PROPOSED |
| Watcher kind | `file` / `api` / `tile` per access method | PROPOSED |
| Default policy posture | Deny-by-default until activation; quarantine on rights ambiguity | CONFIRMED doctrine |
| Default source role | **Not pre-assigned** — set per object family at admission | CONFIRMED rule |
| Public release class | Restricted pending `SourceActivationDecision` | PROPOSED |
| Authority position vs. authoritative state/federal data | **Lower** — observation/context, never substitutes for KDOT, TIGER, GNIS, etc. as authority | PROPOSED policy, derived from project doctrine |

> [!NOTE]
> KFM doctrine treats source role as a **descriptor field set at admission, never edited in place**. Corrections must produce a new descriptor and a `CorrectionNotice`. See §3.

[Back to top](#contents)

---

## 3. Source role — decision, not default

KFM enumerates source roles in the SourceDescriptor as: `observed | regulatory | modeled | aggregate | administrative | candidate | synthetic` (PROPOSED vocabulary; CONFIRMED project rule that the role is set at admission and cannot be inferred from convenience).

OSM is **none of these by default**. Each KFM use of OSM data must specify the role the project is admitting it under, for the specific object family involved.

```mermaid
flowchart TD
    A["OSM feature considered<br/>for KFM admission"] --> B{For which object<br/>family / domain lane?"}
    B --> C["Roads / Rail / Trade Routes"]
    B --> D["Settlements / Infrastructure"]
    B --> E["Hydrology (waterways)"]
    B --> F["Archaeology / Cultural sites"]
    B --> G["Other domains"]

    C --> H{"Source role<br/>for THIS object"}
    D --> H
    E --> H
    F --> H
    G --> H

    H -->|community report| I["observation<br/>(low-authority)"]
    H -->|secondary compilation| J["context"]
    H -->|community-edited shape| K["candidate"]
    H -->|tagging derived from elsewhere| L["administrative<br/>(check upstream)"]

    I --> M{"Rights resolved?<br/>Sensitivity cleared?"}
    J --> M
    K --> M
    L --> M

    M -->|No| N["QUARANTINE<br/>fail closed"]
    M -->|Yes| O["RAW capture<br/>with SourceDescriptor"]

    style N fill:#ffe6e6
    style O fill:#e6f5e6
```

> [!CAUTION]
> Even when OSM-tagged data appears to be sourced from an authoritative upstream (e.g., a TIGER import, a KDOT shapefile, a USGS layer), the KFM-side ingestion **must** point at the upstream authority directly. Inheriting authority from a copy is the role-collapse anti-pattern (`ROLE_COLLAPSE` / `ROLE_DOWNCAST_FORBIDDEN`).

[Back to top](#contents)

---

## 4. Rights, license, and attribution

### 4.1 Project posture (CONFIRMED)

The Roads/Rail dossier records OSM with the following rights status: *"rights and current terms NEEDS VERIFICATION; sensitive joins fail closed."* That posture binds every domain that consumes OSM until a `SourceActivationDecision` records otherwise.

KFM doctrine requires `LayerManifest` to carry `attribution`, `license_spdx`, `rights_statement`, and review status before any public release; rights-unknown blocks release. CONFIRMED.

### 4.2 Generally known OSM license posture (EXTERNAL)

For working context only — **not** a substitute for a recorded `SourceActivationDecision`:

| Item | Generally known posture | Treatment in KFM |
|---|---|---|
| Data license | Open Database License (ODbL 1.0) — *EXTERNAL, NEEDS VERIFICATION for current effective text and any region-specific overlays* | Resolve before activation; record SPDX in LayerManifest |
| Tile / cartographic style license | Separate from data license; OSM Foundation tile cartography is published under its own terms — *EXTERNAL, NEEDS VERIFICATION* | KFM should not assume tile-style and database licenses are interchangeable |
| Attribution requirement | "© OpenStreetMap contributors" attribution is the project's standing convention — *EXTERNAL* | LayerManifest attribution string and Evidence Drawer citation must carry this when activated |
| Share-alike (derivative database) | ODbL imposes share-alike obligations on **derivative databases**; produced works are treated differently — *EXTERNAL, version-sensitive* | Treat any KFM emitted database (catalog tables, GeoParquet, tile derivatives) as potentially share-alike until reviewed |

> [!WARNING]
> ODbL's share-alike obligation interacts with KFM's lifecycle in ways that **require legal/steward review** before publication. Catalog tables, GeoParquet exports, PMTiles, COGs, and graph projections derived from OSM may constitute a derivative database. Do not publish OSM-derived database artifacts without an activation decision that explicitly addresses this.

### 4.3 KFM release requirements that bind regardless of license

CONFIRMED doctrine: before public or semi-public release of any OSM-derived layer or claim, KFM requires identity, rights, sensitivity, validation, provenance, integrity, receipts, policy checks, review state, release state, correction path, and rollback path — appropriate to the significance of the claim.

[Back to top](#contents)

---

## 5. Sensitivity posture and deny-by-default cases

CONFIRMED doctrine: when rights, sovereignty, cultural sensitivity, living-person data, DNA/genomic data, rare-species locations, archaeology, infrastructure, or precise location exposure are unclear, KFM prefers **quarantine, redaction, generalization, staged access, delayed publication, or denial** — and records the transforms and reasons.

OSM-specific sensitivity surfaces:

| OSM content class | Default posture in KFM | Reason |
|---|---|---|
| Culturally sensitive corridors, sacred routes, Indigenous trade alignments | **DENY** exact public exposure | Roads/Rail dossier explicitly forbids exposing culturally sensitive corridors |
| Exact archaeological points (sites tagged `historic=archaeological_site` or similar) | **DENY** exact public exposure | Archaeology domain blanket rule |
| Critical infrastructure precision (power, water, telecom nodes) | **RESTRICT / DENY** | Settlements/Infrastructure default |
| Private landowner-sensitive geometry (e.g., field boundaries, residential addresses) | **DENY** exact public exposure if rights or owner identity are unclear | Sensitive register default |
| Rare species occurrence points (when present in OSM via `species=` or similar) | **DENY** exact location | Fauna/Flora rare-species default |
| Standard roads, settlements, place names, hydrography | Eligible for processing through normal gates | Subject to source-role assignment per §3 |

> [!IMPORTANT]
> Sensitivity must be **detected before publication**, not after. Style-level hiding (e.g., a MapLibre filter that simply doesn't draw a layer) is **not** a sensitivity control. CONFIRMED doctrine: "relying on style filters for sensitive geometry" is an anti-pattern.

[Back to top](#contents)

---

## 6. Freshness, cadence, and stale-state

OSM is **continuously edited**; in KFM lifecycle terms this means:

- **Source freshness** is defined per snapshot or per extract, not for "OSM" in the abstract. A `SourceDescriptor` must record the snapshot or extract timestamp it represents.
- **Cadence** is set in the `SourceDescriptor` and tracked by a watcher. Once the cadence elapses without a new admission, the Evidence Drawer must surface a *stale source* badge.
- **Watcher-as-non-publisher** invariant applies: an OSM watcher detects material change and opens a reviewed PR or review packet; it never publishes refreshed artifacts directly.

> [!TIP]
> Prefer **regional extract snapshots** (e.g., a state-level extract published on a known schedule) over live API scraping for the canonical RAW capture. Snapshot identity is easier to hash, cite, and roll back.

[Back to top](#contents)

---

## 7. Retrieval methods and admission boundary

EXTERNAL summary (general working knowledge — **not** a KFM endorsement; live use requires `SourceActivationDecision`):

| Retrieval method | Typical use | KFM admission notes |
|---|---|---|
| Regional extracts (state/country-level snapshots, e.g., from third-party redistributors) | Canonical RAW capture for KFM bulk processing | Preferred; snapshot timestamp + checksum form deterministic source identity |
| Planet-level dump | Full-extent processing | Heavyweight; only when state/regional extracts are insufficient |
| Read-only query API (Overpass) | Targeted feature queries during normalization | Use cautiously; rate-limit and politeness budgets per project watcher doctrine (PROPOSED) |
| Live editing API | **Not used by KFM** for read paths | KFM is a consumer, not a contributor pipeline |
| Pre-rendered raster tiles from OSMF infrastructure | Visual reference only, never as evidence | Tile use carries separate terms; treat as context layer only |
| Third-party hosted PMTiles / MVT mirrors | Visualization context | SourceDescriptor required; downstream carrier, not authority |

CONFIRMED doctrine (Directory Rules §7.3): connector output **must** go to `data/raw/<domain>/<source_id>/<run_id>/` or `data/quarantine/...`, with source descriptors, checksums, and ingest receipts. Connectors **must not** publish, mutate canonical truth, or write under `data/processed/`, `data/catalog/`, or `data/published/`.

Proposed connector home (PROPOSED, NEEDS VERIFICATION against mounted repo):

```text
connectors/
└── osm/
    ├── README.md           # references this source-family standard
    ├── source-descriptor.yaml  # PROPOSED — instance lives per ADR-0001 schema home
    ├── extract_fetch.py    # PROPOSED — regional-extract retrieval
    ├── overpass_query.py   # PROPOSED — bounded Overpass admission
    └── fixtures/           # no-network fixtures for connector tests
```

> [!NOTE]
> The exact connector layout above is **PROPOSED**. Directory Rules §7.3 names the lane (`connectors/<source-or-provider>/`) but does not assert that `connectors/osm/` currently exists in the repo. Verify before treating any path as canonical.

[Back to top](#contents)

---

## 8. Lifecycle and gates

OSM-derived material follows the universal lifecycle invariant. CONFIRMED doctrine; specific implementation **PROPOSED** until a mounted repo verifies it.

```mermaid
flowchart LR
    R["RAW<br/>(extract + checksum + SourceDescriptor)"] --> WQ{"Normalize<br/>schema · geometry · time<br/>identity · evidence · rights · policy"}
    WQ -->|fail closed| Q["QUARANTINE<br/>(reason recorded)"]
    WQ -->|pass| W["WORK"]
    W --> V{"Validate<br/>(deterministic, fixture-bound)"}
    V -->|fail| W2["HOLD in WORK"]
    V -->|pass| P["PROCESSED"]
    P --> CT{"Catalog closure<br/>EvidenceRef resolves"}
    CT -->|fail| P2["HOLD in PROCESSED"]
    CT -->|pass| C["CATALOG / TRIPLET"]
    C --> RG{"Release gate<br/>(rights, review, manifest, rollback)"}
    RG -->|fail| C2["HOLD in CATALOG"]
    RG -->|pass| PUB["PUBLISHED"]

    style Q fill:#ffe6e6
    style PUB fill:#e6f5e6
```

Gate-specific consequences for OSM:

| Gate | OSM-specific fail-closed reason codes (PROPOSED) | Recovery path |
|---|---|---|
| Admission | `RIGHTS_UNKNOWN` (no `SourceActivationDecision`); `SOURCE_ROLE_UNSET` | Record rights resolution; steward review |
| Normalization | `SCHEMA_MISMATCH` on OSM tag heterogeneity; `SENSITIVITY_UNRESOLVED` on cultural/archaeological tags | Tag normalization rules; sensitivity tagging; quarantine ambiguous cases |
| Validation | `EVIDENCE_INSUFFICIENT` if claim depends on a single OSM edit with no corroboration | Cross-check authoritative source; downgrade role; abstain |
| Catalog closure | `ATTRIBUTION_MISSING`; `LICENSE_NOT_SPECIFIED` | Populate `LayerManifest.attribution` / `license_spdx`; refresh manifest |
| Release | `REVIEW_NEEDED` for any sensitive lane; `ROLLBACK_TARGET_MISSING` | Run steward review; bind rollback target |

[Back to top](#contents)

---

## 9. Domain applicability matrix

OSM intersects multiple KFM domain lanes. PROPOSED applicability (informational; binding per-lane in the relevant domain dossier):

| Domain lane | Typical OSM contribution | Default KFM role posture | Notes |
|---|---|---|---|
| Roads, Rail, and Trade Routes | Modern roads, rail alignments, historic-tagged routes | **context / candidate** — *never* primary authority; KDOT / TIGER / GNIS take authority | OSM listed explicitly in Roads/Rail source families |
| Settlements, Cities, Infrastructure | Place names, settlement footprints, points of interest | **context / candidate** — secondary to TIGER, GNIS, state/local GIS | Public-safe view only |
| Hydrology | Waterways, dams, bridges-over-water tagging | **context** — NHDPlus HR / WBD / authoritative state hydro datasets take authority | Bridge/ferry tagging may corroborate Roads/Rail |
| Archaeology | Sites tagged `historic=archaeological_site` and similar | **Default DENY exact** — sensitivity rules dominate | Generalized public view only; steward review required |
| Hazards | Crowdsourced damage reports, road closures (rare) | **observation (low-authority)** — not for life-safety routing | Not-for-life-safety disclaimer applies |
| Atmosphere / Air | Not applicable in normal use | — | — |
| People / DNA / Land | Not applicable; OSM does not carry person-level data | — | — |

> [!IMPORTANT]
> A single OSM feature can legitimately be admitted into multiple lanes with **different roles** (e.g., a railway as `context` for Roads/Rail and as `candidate` corroborating evidence for a historical Settlement claim). Each admission is a separate `SourceDescriptor` instance.

[Back to top](#contents)

---

## 10. Anti-patterns — what OSM is NOT

> [!CAUTION]
> The following anti-patterns are **forbidden** by KFM doctrine. Several are restatements of universal rules; they are listed here because they recur specifically around community-edited spatial data.

| Anti-pattern | What it looks like | Why it is forbidden |
|---|---|---|
| **Authority laundering** | Treating an OSM feature as authoritative because it was imported from TIGER years ago | Source role cannot be inferred from an intermediary copy; `ROLE_COLLAPSE` |
| **Style-hidden sensitivity** | "It's only sensitive if it's rendered" — a MapLibre filter hiding a sensitive layer | Style is not a policy control; sensitive geometry must be removed or generalized upstream |
| **Live API as canonical** | Using Overpass as the canonical RAW source for catalogued artifacts | Snapshots are auditable; API results drift; live API is not deterministic |
| **Released-without-attribution** | A LayerManifest, tile, or evidence drawer payload that omits attribution | Public release requires source rights, attribution, and license metadata |
| **Share-alike-blind publication** | Publishing OSM-derived GeoParquet/PMTiles without addressing derivative-database obligations | Treats license as solved when it has not been reviewed |
| **AI-as-evidence** | Letting a Focus Mode answer say "OSM shows…" without resolving the underlying EvidenceBundle | AI text is never evidence; cite-or-abstain applies |
| **Tile-as-truth** | Treating an OSM raster tile as proof of a fact | Tiles are downstream carriers, not sovereign truth |
| **One-PR roll-up** | A single PR that fetches, normalizes, catalogs, and releases OSM data in one step | Lifecycle skip; promotion is a governed state transition, not a file move |

[Back to top](#contents)

---

## 11. Illustrative SourceDescriptor fields

> [!NOTE]
> This block is **illustrative** and **PROPOSED**. It is not the canonical schema. The canonical schema home defaults to `schemas/contracts/v1/source/source-descriptor.schema.json` per Directory Rules §7.4 / ADR-0001 — actual file presence and field names are NEEDS VERIFICATION.

<details>
<summary>Click to expand — illustrative OSM SourceDescriptor (PROPOSED, not authoritative)</summary>

```yaml
# docs/sources/examples/osm-extract-kansas.yaml  (PROPOSED — illustrative only)
source_id: src-osm-kansas-extract-2026-04
source_family: openstreetmap
provider: third_party_redistributor   # PROPOSED enum value
provider_terms_ref: docs/sources/openstreetmap.md#4-rights-license-and-attribution
endpoint:
  kind: file
  url_template: "<provider-extract-url>"   # PROPOSED — fill at activation
  snapshot_timestamp: "2026-04-01T00:00:00Z"
  checksum_algorithm: sha256
  checksum_value: "<sha256-of-extract>"
retrieval:
  method: regional_extract
  watcher_kind: file
  cadence: monthly
  politeness_budget_ref: docs/standards/connector-rate-limits.md   # PROPOSED
rights:
  status: NEEDS_VERIFICATION
  license_spdx: ODbL-1.0                # EXTERNAL working assumption; verify
  attribution: "© OpenStreetMap contributors"
  share_alike_review_ref: docs/governance/osm-sharealike-review.md   # PROPOSED
sensitivity:
  default_tier: T2                      # PROPOSED — see sensitivity tier doctrine
  domain_overrides:
    archaeology: T4
    settlements_infrastructure_critical: T3
source_role:
  # MUST be set per object family at admission. No default.
  by_object_family:
    road_segment: context
    rail_segment: context
    settlement: context
    historic_route_claim: candidate
authority_class: secondary              # Not authoritative for KFM publication
release_class: restricted_until_activation
steward: source-steward@kfm.example     # PROPOSED placeholder
notes:
  - "Source-role per object family must be reaffirmed on every refresh."
  - "Sensitive-tag filter must run before any catalog closure."
```

</details>

[Back to top](#contents)

---

## 12. Open questions and verification backlog

| # | Question | Label | Resolution path |
|---|---|---|---|
| 1 | Has a `SourceActivationDecision` been issued for OSM in any KFM lane? | UNKNOWN | Inspect `control_plane/source_authority_register.yaml` once mounted |
| 2 | Does the repo currently host `connectors/osm/`? | NEEDS VERIFICATION | Verify against mounted repo before treating the path as canonical |
| 3 | What SPDX identifier and effective version best represents OSM's current data license terms for KFM purposes? | NEEDS VERIFICATION (EXTERNAL informational baseline only) | Steward + legal review |
| 4 | Does any KFM-derived database artifact (catalog table, GeoParquet, PMTiles, COG, graph projection) constitute a derivative database under share-alike obligations? | NEEDS VERIFICATION | Per-artifact review during release gate |
| 5 | Which OSM tag patterns trigger sensitive-class denial (cultural corridors, archaeology, critical infrastructure, private landowner data)? | PROPOSED | Author a sensitive-tag denylist in policy lane |
| 6 | What is the canonical extract provider and cadence for KFM's RAW captures of OSM Kansas data? | UNKNOWN | Source steward decision; record in SourceDescriptor |
| 7 | How does an OSM watcher distinguish a *material* change from churn? | NEEDS VERIFICATION | Define material-property allowlist per project watcher doctrine |
| 8 | Where does OSM-specific tag normalization logic live? | PROPOSED | `pipelines/normalize/osm/` (PROPOSED) per Directory Rules §7.4 |

[Back to top](#contents)

---

## 13. Related docs

> Placeholders are linked relative to repo root. Some targets are **PROPOSED** and may not yet exist.

- [`docs/sources/README.md`](../../README.md) — index of source families
- [`docs/sources/SOURCE_DESCRIPTOR_STANDARD.md`](../../SOURCE_DESCRIPTOR_STANDARD.md) — descriptor field standard
- [`docs/doctrine/directory-rules.md`](../../../doctrine/directory-rules.md) — placement law
- [`docs/doctrine/lifecycle-law.md`](../../../doctrine/lifecycle-law.md) — RAW → PUBLISHED invariant
- [`docs/doctrine/trust-membrane.md`](../../../doctrine/trust-membrane.md) — public-surface boundary
- [`docs/doctrine/truth-posture.md`](../../../doctrine/truth-posture.md) — cite-or-abstain
- [`docs/domains/roads-rail-trade/README.md`](../../../domains/roads-rail-trade/README.md) — primary consuming domain
- [`docs/domains/settlements-infrastructure/README.md`](../../../domains/settlements-infrastructure/README.md) — secondary consuming domain
- [`docs/domains/hydrology/README.md`](../../../domains/hydrology/README.md) — secondary consuming domain
- [`docs/domains/archaeology/README.md`](../../../domains/archaeology/README.md) — sensitivity-dominant domain
- [`docs/adr/`](../../../adr/) — ADR index (e.g., ADR-0001 schema home)
- [`connectors/osm/`](../../../../connectors/osm/) — connector home
- [`schemas/contracts/v1/source/source-descriptor.schema.json`](../../../../schemas/contracts/v1/source/source-descriptor.schema.json) — canonical schema home

---

<sub>**Last updated:** 2026-05-13 · **Document version:** v1 (draft) · **Authority:** doctrine + project source-family list (CONFIRMED) · Specific paths quoted herein are PROPOSED until verified against mounted-repo evidence. · [Back to top](#-openstreetmap--source-family-standard)</sub>
