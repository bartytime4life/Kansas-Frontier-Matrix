<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-domains-roads-rail-trade-catalog-index
title: Catalog Index — Roads / Rail / Trade Routes Domain
type: standard
version: v0.1
status: draft
owners: <roads-rail-trade stewards; catalog/release steward — TODO confirm>
created: 2026-06-07
updated: 2026-06-07
policy_label: public
related:
  - docs/domains/roads-rail-trade/README.md
  - docs/domains/roads-rail-trade/CANONICAL_PATHS.md
  - docs/domains/roads-rail-trade/ARCHITECTURE.md
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - docs/standards/STAC.md
  - docs/standards/DCAT.md
  - docs/standards/PROV.md
  - docs/adr/ADR-0001-schema-home.md
tags: [kfm, domain, roads-rail-trade, transport, catalog, stac, dcat, prov, triplet, evidence-bundle]
notes:
  - 'CONTRACT_VERSION = "3.0.0" pinned per ai-build-operating-contract.md'
  - "SCOPE GUARD: this is a CATALOG-LAYER INDEX (what catalog records this lane emits + how they are keyed + the closure gate). It is NOT the path registry (see CANONICAL_PATHS.md §5.5) and NOT the architecture explainer (ARCHITECTURE.md §9). Overlap flagged in §1."
  - "PLACEMENT SUBTLETY (Directory Rules): data/catalog/ is structured stac/ dcat/ prov/ domain/. The domain-scoped record home is data/catalog/domain/roads-rail-trade/. The stac/ dcat/ prov/ homes are FORMAT homes; a domain/area appears as a SUB-SEGMENT inside them (data/catalog/stac/<area>/), never the reverse. Do not imply this lane owns data/catalog/stac/."
  - "Schema/contract slug CONFLICTED (domains/roads-rail-trade/ §12 vs transport/ §24.13). Catalog records reference contracts/schemas by the resolved slug; see CANONICAL_PATHS §3."
  - "All concrete paths/keys/record counts are PROPOSED until verified against a mounted repository."
[/KFM_META_BLOCK_V2] -->

# Catalog Index — Roads / Rail / Trade Routes Domain

> Index of the **CATALOG / TRIPLET**-phase records the Roads / Rail / Trade Routes lane emits: STAC items, DCAT datasets, PROV bundles, EvidenceBundle references, and graph/triplet projections — how they are keyed, what closes the catalog gate, and where they live. This is the *catalog-contents* view, not the path registry and not the architecture explainer.

![Status: draft](https://img.shields.io/badge/status-draft-yellow)
![CONTRACT_VERSION 3.0.0](https://img.shields.io/badge/CONTRACT__VERSION-3.0.0-1f6feb)
![Domain: roads--rail--trade](https://img.shields.io/badge/domain-roads--rail--trade-slategray)
![Phase: CATALOG / TRIPLET](https://img.shields.io/badge/phase-CATALOG%20%2F%20TRIPLET-8250df)
![View: catalog index (not path registry)](https://img.shields.io/badge/view-catalog%20index-purple)
![Verification: pending](https://img.shields.io/badge/repo%20verification-pending-orange)

**Status:** draft · **Parent dossier:** `docs/domains/roads-rail-trade/` · **Owners:** roads-rail-trade + catalog/release steward `TODO` · **Last updated:** 2026-06-07

> [!IMPORTANT]
> **Scope and overlap.** This file indexes the **records** in the CATALOG / TRIPLET phase for this lane. It deliberately does **not** restate the full path tree (that is `CANONICAL_PATHS.md`) or the responsibility-root architecture (that is `ARCHITECTURE.md`). Where it names a path it is for catalog context only. **No mounted repository was inspected**; every record key, count, and path is **PROPOSED / NEEDS VERIFICATION**. **`CONTRACT_VERSION = "3.0.0"`.**

---

## Quick navigation

- [1. What this index is (and is not)](#1-what-this-index-is-and-is-not)
- [2. Where catalog records live](#2-where-catalog-records-live)
- [3. Record families emitted by this lane](#3-record-families-emitted-by-this-lane)
- [4. Keying & identity](#4-keying--identity)
- [5. EvidenceBundle references](#5-evidencebundle-references)
- [6. Triplet & graph projections](#6-triplet--graph-projections)
- [7. Catalog closure gate](#7-catalog-closure-gate)
- [8. Sensitivity at the catalog layer](#8-sensitivity-at-the-catalog-layer)
- [9. What the catalog layer must never do](#9-what-the-catalog-layer-must-never-do)
- [10. Open questions & verification backlog](#10-open-questions--verification-backlog)
- [11. Related docs](#11-related-docs)

---

## 1. What this index is (and is not)

**Is.** An inventory of the catalog-layer outputs the Roads / Rail / Trade Routes lane produces when evidence is promoted from PROCESSED into **CATALOG / TRIPLET**: STAC items, DCAT datasets, PROV bundles, the EvidenceBundle references those records carry, and the graph/triplet projections derived alongside them. It answers *"what catalog records does this lane emit, how are they keyed, and what closes the gate?"*

**Is not.** A path registry (that is [`CANONICAL_PATHS.md`](./CANONICAL_PATHS.md) §5.5) or an architecture explainer (that is [`ARCHITECTURE.md`](./ARCHITECTURE.md) §9). Those define *where files go* and *how the lane fits the roots*; this file lists *what the catalog phase contains*.

**Doctrine basis (CONFIRMED).** The CATALOG / TRIPLET phase "emit[s] catalog records, EvidenceBundles, graph/triplet projections, and release candidates" with the gate "Catalog/proof closure passes" (Atlas Ch. 13 §H; `[DIRRULES]` lifecycle invariant). `data/catalog/` is internally structured as `stac/ dcat/ prov/ domain/` (`[DIRRULES]`).

[↑ back to top](#catalog-index--roads--rail--trade-routes-domain)

---

## 2. Where catalog records live

CONFIRMED from `[DIRRULES]`: `data/catalog/` is structured by **format** and by **domain**, and an **area or domain appears as a sub-segment inside the format homes**, never the reverse.

```text
data/catalog/
├── stac/        # STAC items/collections — FORMAT home; domain appears as a sub-segment: data/catalog/stac/roads-rail-trade/
├── dcat/        # DCAT datasets/catalogs — FORMAT home; data/catalog/dcat/roads-rail-trade/
├── prov/        # W3C PROV bundles — FORMAT home; data/catalog/prov/roads-rail-trade/
└── domain/
    └── roads-rail-trade/   # DOMAIN-scoped catalog record home for this lane
```

> [!CAUTION]
> **Placement subtlety (Domain Placement Law).** The lane's **domain-scoped** catalog home is `data/catalog/domain/roads-rail-trade/`. The `stac/`, `dcat/`, and `prov/` directories are **format homes** that compose across domains; this lane contributes records *under* them as a sub-segment (`data/catalog/stac/roads-rail-trade/`), and it does **not own** `data/catalog/stac/`. Do not author a `data/catalog/domain/roads-rail-trade/stac/` tree that shadows the format home — that fragments the catalog. `[DIRRULES]`

> [!NOTE]
> The schema/contract slug a catalog record points back to (`…/domains/roads-rail-trade/` per §12 vs `…/transport/` per §24.13) is **CONFLICTED** — see [`CANONICAL_PATHS.md`](./CANONICAL_PATHS.md) §3. Catalog records MUST reference whichever form the ADR resolves; until then, the reference is recorded as the resolved-slug placeholder and flagged.

[↑ back to top](#catalog-index--roads--rail--trade-routes-domain)

---

## 3. Record families emitted by this lane

PROPOSED inventory, grounded in the CONFIRMED owned-object set (Atlas Ch. 13 §B) and the CONFIRMED catalog formats. Counts are unknowable without a mounted repo.

| Record family | Format home | What it describes for this lane | Status |
|---|---|---|---|
| **STAC items / collections** | `data/catalog/stac/roads-rail-trade/` | Spatiotemporal assets: published road/rail layers, historic-route-claim layers, generalized trade-corridor layers, derived graph views (each STAC item links its released asset + EvidenceBundle ref) | PROPOSED |
| **DCAT datasets** | `data/catalog/dcat/roads-rail-trade/` | Dataset-level descriptors for each released transport dataset (title, source family, rights label, cadence, distribution) | PROPOSED |
| **PROV bundles** | `data/catalog/prov/roads-rail-trade/` | W3C PROV-O lineage: which SourceDescriptors, runs, validations, and receipts produced each catalog record | PROPOSED |
| **Domain catalog records** | `data/catalog/domain/roads-rail-trade/` | The lane's own catalog records for owned objects (Road Segment, Rail Segment, CorridorRoute, Crossing, Bridge, Ferry, River Crossing, Freight Corridor, Depot/Siding/Yard, Route Event, Operator Status, Access Restriction, Historic Route, Movement Story Node) with EvidenceBundle refs | PROPOSED |
| **Triplet / graph projections** | `data/triplets/roads-rail-trade/` (+ `data/triplets/graph_deltas/`, `data/triplets/exports/`) | Route-membership and network-edge projections — **derived, never canonical** | PROPOSED |
| **Release candidates** | `release/candidates/roads-rail-trade/` | Catalog records assembled into release candidates (a catalog record is not a release; see §7) | PROPOSED |

> [!NOTE]
> A single owned object typically produces records in **several** format homes for one release: a STAC item (where spatial), a DCAT dataset descriptor, a PROV bundle, and a domain catalog record, all sharing the same EvidenceBundle reference (§5) and deterministic key (§4).

[↑ back to top](#catalog-index--roads--rail--trade-routes-domain)

---

## 4. Keying & identity

PROPOSED, derived from the CONFIRMED deterministic-identity basis (Atlas Ch. 13 §E: `source_id + object_role + temporal_scope + normalized_digest`).

- **Catalog record key** is derived from the cataloged object's deterministic identity, not minted independently — so the same object resolves to the same catalog key across re-runs.
- **`spec_hash`** for any schema a record validates against is recorded as `jcs:sha256:<hex>` (RFC 8785 JCS + SHA-256), so a record pins the exact contract shape it conformed to at catalog time.
- **Cross-format linkage:** the STAC item, DCAT dataset, PROV bundle, and domain record for one release share the object key and point to one EvidenceBundle; they are facets of one cataloged thing, not independent records.
- **Snapshot-week pinning** (rail): STB Class I weekly snapshots overlap, so any catalog record derived from STB MUST pin the snapshot-week in its provenance to prevent downstream double-counting (Pass-10 C10-05).
- **`.proto` version pinning** (transit): GTFS-RT records pin the protobuf `.proto` schema version used at decode in their PROV bundle (Pass-10 C10-04).

[↑ back to top](#catalog-index--roads--rail--trade-routes-domain)

---

## 5. EvidenceBundle references

CONFIRMED doctrine: catalog records carry **EvidenceBundle references**, and a public claim resolves `EvidenceRef → EvidenceBundle` before it can be cited as authoritative. `[ENCY]` `[GAI]`

- Every domain catalog record and every STAC item for this lane MUST carry a resolvable `EvidenceRef`; a record without one is not catalog-closed (§7).
- The EvidenceBundle is the **truth-bearing object** — it outranks any generated summary, rendered tile, or graph projection built from it.
- Catalog records reference EvidenceBundles; they do **not** inline or duplicate them. Receipts created earlier (ingest, validation) are referenced via `EvidenceRef`, not copied into the catalog record.

[↑ back to top](#catalog-index--roads--rail--trade-routes-domain)

---

## 6. Triplet & graph projections

CONFIRMED doctrine / PROPOSED lane application. The TRIPLET side of the phase emits graph/triplet projections — for this lane, route-membership and network-edge graphs.

| Projection | Home | Constraint |
|---|---|---|
| Route-membership / corridor graph | `data/triplets/roads-rail-trade/` | Derived from catalog records + EvidenceBundles; reversible to that source state. |
| Network-edge connectivity graph | `data/triplets/roads-rail-trade/` (+ `graph_deltas/` for incremental updates) | **Never canonical truth.** A graph edge does not replace the Road/Rail Segment evidence it was built from. |
| Graph exports (for clients) | `data/triplets/exports/` → public-safe copy under `data/published/layers/roads-rail-trade/<graph-view>/` | Clearly labeled *derived*; carries a rollback target (Atlas Ch. 13 §K "transport graph projection rollback tests"). |

> [!IMPORTANT]
> **A derived graph is a carrier, not a source.** If a canonical Road/Rail Segment is corrected, every triplet/graph projection derived from it MUST roll back or re-derive — never be patched in place. The rollback drill is a §K test obligation. `[DOM-ROADS]` `[ENCY]`

[↑ back to top](#catalog-index--roads--rail--trade-routes-domain)

---

## 7. Catalog closure gate

CONFIRMED doctrine (Atlas Ch. 13 §H): the gate from CATALOG / TRIPLET toward PUBLISHED is **"catalog / proof closure passes."** A catalog record is *closed* for this lane when:

1. It carries a resolvable **EvidenceRef → EvidenceBundle** (§5).
2. Its **deterministic key** is derived from the object identity (§4), not minted ad hoc.
3. Its **PROV bundle** records the full lineage (SourceDescriptor → run → validation → receipts).
4. Any **schema it validates against** is pinned by `spec_hash` (`jcs:sha256:<hex>`).
5. **Source-rights** are resolved (not "NEEDS VERIFICATION") — unresolved rights hold the record at PROCESSED/QUARANTINE, not CATALOG.
6. **Sensitivity** is resolved (§8) — Indigenous/cultural-corridor records are not catalog-closed for public release without a steward `ReviewRecord`.

> [!IMPORTANT]
> **Catalog closure is not release.** A closed catalog record is a *release candidate*, assembled under `release/candidates/roads-rail-trade/`. Publication requires the §M / Atlas Ch. 13 release artifacts (`ReleaseManifest`, correction path, rollback target, review/policy state). Promotion across the gate is a **governed state transition, not a file move**. `[DIRRULES]` `[ENCY]`

[↑ back to top](#catalog-index--roads--rail--trade-routes-domain)

---

## 8. Sensitivity at the catalog layer

CONFIRMED / PROPOSED (Atlas Ch. 13 §I, applied to catalog records):

- **Indigenous, treaty, cultural, and oral-history corridor records** default to steward review + generalized public geometry. Their catalog records are **not** closed for public release without a `ReviewRecord`; cultural truth and the sensitivity tier are owned by Archaeology / Cultural Heritage (`[DOM-ARCH]`), not by this lane. A generalized public record carries a `RedactionReceipt`.
- **Critical transport facility records** (key bridges, intermodal terminals, fuel/freight nodes) require review before a public catalog record is closed.
- **Aggregate records** (e.g., aggregated rail-incident or freight-flow summaries) carry an `AggregationReceipt`; an aggregate record MUST NOT be re-keyed to a single underlying object.
- **Source-rights-unresolved** records are held at QUARANTINE with a recorded reason, never catalog-closed.

> [!WARNING]
> A catalog record's **format does not lower its sensitivity**. A STAC item or DCAT dataset for a sensitive corridor is as restricted as the underlying evidence; publishing the descriptor while withholding the asset still leaks the corridor's existence and approximate location. The most-restrictive applicable row of the operating contract's §23.2 matrix governs the whole record set. `[ENCY]`

[↑ back to top](#catalog-index--roads--rail--trade-routes-domain)

---

## 9. What the catalog layer must never do

CONFIRMED doctrine (`[DIRRULES]` anti-patterns; trust membrane):

- **No connector writes to `data/catalog/`.** Connectors emit to `data/raw/` or `data/quarantine/`; pipelines promote. (Watcher/connector-as-non-publisher.)
- **No catalog record without an EvidenceRef** — it is not closed (§7).
- **No graph/triplet projection treated as canonical** — derived only (§6).
- **No `data/catalog/domain/roads-rail-trade/stac/` shadow tree** — STAC records go under the `data/catalog/stac/` format home as a sub-segment (§2).
- **No public client reading `data/catalog/` directly** — public surfaces consume `apps/governed-api/` projections, not the catalog store.
- **No sensitive-corridor record closed for public release** without a steward `ReviewRecord` (§8).
- **No release minted by copying a catalog record** — release is a governed transition with its own artifacts (§7).

[↑ back to top](#catalog-index--roads--rail--trade-routes-domain)

---

## 10. Open questions & verification backlog

Track in `docs/registers/VERIFICATION_BACKLOG.md` / `docs/registers/DRIFT_REGISTER.md`.

| ID | Item | Evidence that would settle it | Status |
|---|---|---|---|
| **OQ-CAT-01** | Does this lane's catalog use the `data/catalog/{stac,dcat,prov}/roads-rail-trade/` sub-segment form, and is there a `data/catalog/domain/roads-rail-trade/` record home? | repo tree listing | NEEDS VERIFICATION |
| **OQ-CAT-02** | Schema/contract slug that catalog records reference (`domains/roads-rail-trade/` vs `transport/`) | ADR resolving CANONICAL_PATHS §3 / OPEN-RRT-01 | CONFLICTED |
| **VB-CAT-01** | Catalog-record key derivation matches the §E deterministic identity (not independently minted) | record sample + key-derivation code | NEEDS VERIFICATION |
| **VB-CAT-02** | Every domain catalog record / STAC item carries a resolvable EvidenceRef | record sample; closure validator | NEEDS VERIFICATION |
| **VB-CAT-03** | STB snapshot-week pinning present in rail-derived records (C10-05) | PROV bundle sample | NEEDS VERIFICATION |
| **VB-CAT-04** | GTFS-RT `.proto` version pinned in transit-derived records (C10-04) | PROV bundle sample | NEEDS VERIFICATION |
| **VB-CAT-05** | Catalog-closure validator enforces the six §7 conditions | validator + CI output | NEEDS VERIFICATION |
| **VB-CAT-06** | Triplet/graph projections have rollback targets (Atlas §K) | rollback card + test | NEEDS VERIFICATION |
| **VB-CAT-07** | Sensitive-corridor records are blocked from public catalog closure without a ReviewRecord | policy + negative fixture | NEEDS VERIFICATION |

[↑ back to top](#catalog-index--roads--rail--trade-routes-domain)

---

## 11. Related docs

- **Path registry:** [`CANONICAL_PATHS.md`](./CANONICAL_PATHS.md) — where catalog files go; §5.5 lifecycle-data paths; §3 slug conflict.
- **Architecture:** [`ARCHITECTURE.md`](./ARCHITECTURE.md) — responsibility-root fit; §9 pipeline shape.
- Parent dossier: `docs/domains/roads-rail-trade/README.md` *(PROPOSED — verify on mount)*.
- Doctrine: [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md) — `data/catalog/` structure, lifecycle invariant, catalog-area placement rule.
- Doctrine: [`docs/doctrine/lifecycle-law.md`](../../doctrine/lifecycle-law.md) — RAW → PUBLISHED, promotion as governed transition.
- Standards: [`docs/standards/STAC.md`](../../standards/STAC.md), [`docs/standards/DCAT.md`](../../standards/DCAT.md), [`docs/standards/PROV.md`](../../standards/PROV.md) — the catalog formats this lane conforms to.
- ADR: [`docs/adr/ADR-0001-schema-home.md`](../../adr/ADR-0001-schema-home.md) — schema-home rule that catalog records reference via `spec_hash`.
- Atlas Ch. 13 §H (lifecycle/gate), §E (identity), §I (sensitivity), §K (graph rollback) — doctrine basis.
- Registers: `docs/registers/VERIFICATION_BACKLOG.md`, `docs/registers/DRIFT_REGISTER.md` — destinations for §10 items.

---

<sub><strong>Last updated:</strong> 2026-06-07 · <strong>Doc version:</strong> v0.1 (draft) · <strong>View:</strong> catalog-layer index (not path registry) · <strong>CONTRACT_VERSION:</strong> 3.0.0 · <strong>Owners:</strong> `TODO` · [↑ back to top](#catalog-index--roads--rail--trade-routes-domain)</sub>
