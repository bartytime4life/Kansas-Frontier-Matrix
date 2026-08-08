<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/pass-2-idea-atlas-import-crosswalk
title: KFM Pass 2 Idea Atlas Import Crosswalk
type: exploratory-intake-source-map
version: v0.1.0
status: triaged; exploratory; non-authoritative; repository-grounded
owners: ["@bartytime4life"]
created: 2026-08-08
updated: 2026-08-08
policy_label: public; intake; exploratory; cite-or-abstain
owning_root: docs/
responsibility: Preserve the Pass 2 atlas source identity, all-new-card dispositions, implementation sequence, and complete stable-ID companion without promoting atlas prose into authority.
related:
  - ./README.md
  - ./pass-2-idea-atlas-stable-ids.md
  - ../NEW_IDEAS_INDEX.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../adr/ADR-0007 — MapLibre GL JS Is the Sole Browser-Side Renderer.md
tags: [kfm, intake, pass-2, stable-id, crosswalk, implementation-campaign]
notes:
  - "Source PDF SHA-256: 60451562c8be005ed77afa8c7eada978a7cec05f406cdff137d38ff60123d408."
  - "Repository comparison snapshot: main@e28a83d286cd16743665436001d8544943b366e0."
  - "The atlas is a downstream carrier; this crosswalk creates no source activation, policy, release, deployment, or publication authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KFM Pass 2 idea atlas import crosswalk

> **Outcome:** The Pass 2 source is captured as a governed exploratory input. All 36 new cards receive one repository-grounded disposition, while the companion [stable-ID ledger](pass-2-idea-atlas-stable-ids.md) preserves all 110 IDs, source `spec_hash` values, page hints, carry states, and dispositions exactly once.

## Source identity

| Field | Confirmed value |
|---|---|
| Artifact | `KFM_Pass_2_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf` |
| Source posture | `downstream-carrier` / `cite-or-abstain` |
| Pass / prior pass | `2` / `1` |
| Run date | `2026-05-16` |
| PDF | `996,334` bytes; `107` pages; SHA-256 `60451562c8be005ed77afa8c7eada978a7cec05f406cdff137d38ff60123d408` |
| Embedded manifest | `manifest-pass-2.jsonl`; SHA-256 `af3c1abbacd08359109a3729b596797a74499579c990cbbcff92bd1fceae57c9` |
| Embedded index | `index-pass-2.json`; SHA-256 `0626fe312148c06e5094984d3d158d10f969d272238a2aec77bccf26895bcd8a` |
| Embedded change report | `change-report-pass-2.json`; SHA-256 `cc89f588672490b4c4158a8b5aa43e7ddfb92a8d7197aa31970efc60d78e5fdb` |
| Card accounting | `110` total: `36 NEW`, `39 EXPANDED`, `35 UNCHANGED` |
| Repository snapshot | `main@e28a83d286cd16743665436001d8544943b366e0` |

The PDF is the human-readable source. Its embedded manifest supplies stable identity, class, category, carry state, title, `spec_hash`, and page hint. Neither artifact proves current implementation or authorizes an external source.

## Directory Rules basis

ADR-0029 accepts Directory Rules v2. This record belongs in `docs/intake/exploratory/` because it captures, compares, deduplicates, and routes ideas. Contract meaning stays in `contracts/`; machine shape in `schemas/`; admissibility in `policy/`; executable validation in `tools/`; proof in `tests/` and `fixtures/`; source identity and activation in admitted source/registry lanes; lifecycle data under `data/`; and publication/correction/rollback under governed release surfaces.

No new root or parallel contract, schema, policy, source, registry, proof, or release authority is created.

## Disposition accounting

| Disposition | Count | Meaning |
|---|---:|---|
| `RECONCILE_EXISTING` | 13 | Existing repository surfaces cover the core capability; link and harden them instead of duplicating them. |
| `HARDEN_EXISTING` | 18 | A related boundary exists, but an executable seam, rights/sensitivity rule, fixture, validator, performance proof, or completion step remains. |
| `IMPLEMENT_NEW_SLICE` | 4 | Start with an inactive, no-network, fixture-first slice. |
| `HOLD_GOVERNANCE` | 1 | A separate accepted architecture decision is required before implementation as written. |
| `ACCEPTANCE_OVERLAY` | 39 | Expanded cards become shared acceptance criteria, not 39 separate issues. |
| `LINEAGE_ONLY` | 35 | Unchanged cards retain identity and history without generating new work by default. |

## New-card reconciliation

| Stable ID | Title | Disposition | Repository-grounded action |
|---|---|---|---|
| `KFM-P2-FEAT-0012` | Cesium 3D Tiles for 3D scenes, with MapLibre overlay synchronization | `HOLD_GOVERNANCE` | Hold dual-renderer work pending an accepted renderer decision. |
| `KFM-P2-FEAT-0013` | Mobile-first tile playbook for Kansas network conditions | `HARDEN_EXISTING` | Define constrained Kansas network/device profiles. |
| `KFM-P2-FEAT-0032` | Mobile QA harness running on a reference low-end device class | `HARDEN_EXISTING` | Add a low-end reference-device browser profile. |
| `KFM-P2-FEAT-0035` | Cold-start strategy for first-time and intermittent users | `HARDEN_EXISTING` | Define a manifest-bound public-safe cold-start capsule. |
| `KFM-P2-FEAT-0036` | Offline-first behavior with cached EvidenceBundles | `HARDEN_EXISTING` | Cache only released public-safe Evidence Drawer projections. |
| `KFM-P2-IDEA-0014` | Performance budgets per layer | `HARDEN_EXISTING` | Extend existing map performance budgets with per-layer enforcement. |
| `KFM-P2-IDEA-0015` | k-Anonymity for tabular sensitive data | `HARDEN_EXISTING` | Add a fixture-first k-anonymity assessment; policy selects k. |
| `KFM-P2-IDEA-0016` | BLM CadNSDI as the canonical PLSS source, GLO records as historical layer | `HARDEN_EXISTING` | Complete BLM CadNSDI/GLO modules behind source-role boundaries. |
| `KFM-P2-IDEA-0018` | GBIF as the canonical aggregated biodiversity authority | `RECONCILE_EXISTING` | Existing GBIF/Darwin Core source and connector surfaces. |
| `KFM-P2-IDEA-0019` | KANU, KSC, iDigBio, USDA PLANTS as Kansas-specific biodiversity authorities | `HARDEN_EXISTING` | Close Kansas biodiversity source/version/taxonomy seams. |
| `KFM-P2-IDEA-0020` | eBird as the canonical citizen-science avian authority | `RECONCILE_EXISTING` | Existing eBird source and sampling-event surfaces. |
| `KFM-P2-IDEA-0021` | USGS as the canonical hydrology / streamgage authority | `RECONCILE_EXISTING` | Existing USGS/NHDPlus hydrology identity surfaces. |
| `KFM-P2-IDEA-0022` | EPA AQS / AirNow as canonical air-quality authorities | `RECONCILE_EXISTING` | Existing AirNow/AQS reconciliation contract and fixtures. |
| `KFM-P2-IDEA-0023` | NASA SMAP L4 for soil moisture; Kansas Mesonet for in-situ climate | `RECONCILE_EXISTING` | Existing SMAP L4 and Mesonet source/support distinctions. |
| `KFM-P2-IDEA-0024` | USDA NASS, KGS, KDA, KDHE, KDWP as Kansas-specific agricultural and environmental authorities | `HARDEN_EXISTING` | Reconcile Kansas agency roles, identifiers, terms, and cadence. |
| `KFM-P2-IDEA-0025` | EPA ECHO and TRI as canonical compliance authorities | `IMPLEMENT_NEW_SLICE` | Inactive ECHO/TRI source-role profile; no live activation. |
| `KFM-P2-IDEA-0026` | FEMA NFHL and USACE NLD/NID as flood and infrastructure authorities | `IMPLEMENT_NEW_SLICE` | Separate NFHL, NLD, and NID source-role admission. |
| `KFM-P2-IDEA-0027` | WIMAS, WWC5 for water rights and use | `HARDEN_EXISTING` | Add aggregate-first WIMAS/WWC5 identity and privacy gates. |
| `KFM-P2-IDEA-0028` | USDA CDL, NLCD, LANDFIRE, GAP for land cover | `RECONCILE_EXISTING` | Existing CDL/NLCD/LANDFIRE/GAP source-family coverage. |
| `KFM-P2-IDEA-0029` | HLS / Landsat for vegetation change | `RECONCILE_EXISTING` | Existing HLS source and NDVI materiality validation. |
| `KFM-P2-IDEA-0033` | Per-journey performance budgets | `HARDEN_EXISTING` | Add end-to-end journey performance budgets. |
| `KFM-P2-IDEA-0034` | Browser-side performance discipline: bundle size, code splitting, deferred work | `HARDEN_EXISTING` | Measure Explorer bundle, route, and deferred-work regressions. |
| `KFM-P2-PROG-0001` | Kansas biodiversity ETL (GBIF + DwC-A) thin-slice recipe | `RECONCILE_EXISTING` | Existing GBIF/DwC-A source, connector, and standards lanes. |
| `KFM-P2-PROG-0002` | Kansas flora watcher (kansas_flora_watch) blueprint | `HARDEN_EXISTING` | Complete USDA PLANTS distribution and taxonomy-drift validation. |
| `KFM-P2-PROG-0003` | Soil and air watcher pattern (SoilGrids, SSURGO, EPA AQS, EPA AirNow) | `RECONCILE_EXISTING` | Existing soil and atmosphere watcher families; preserve separation. |
| `KFM-P2-PROG-0004` | SMAP L4 soil moisture ingest with CI-friendly QA | `RECONCILE_EXISTING` | Existing SMAP L4 source, fixtures, validator, and pipeline. |
| `KFM-P2-PROG-0005` | eBird connector with built-in QA for citizen-science observations | `RECONCILE_EXISTING` | Existing eBird connector/source surfaces. |
| `KFM-P2-PROG-0006` | USDA PLANTS ingestion as flora taxonomy and state/county presence baseline | `HARDEN_EXISTING` | Implement a bounded USDA PLANTS loader after rights review. |
| `KFM-P2-PROG-0007` | EPA ECHO and TRI compliance/release ingest | `IMPLEMENT_NEW_SLICE` | Fixture-first facility evidence profile with temporal lineage. |
| `KFM-P2-PROG-0008` | FEMA NFHL and USACE NLD/NID flood and infrastructure ingest | `IMPLEMENT_NEW_SLICE` | Synthetic public-safe NFHL/NLD/NID profile before connectors. |
| `KFM-P2-PROG-0009` | Kansas-specific water systems (WIMAS and WWC5) ingest | `HARDEN_EXISTING` | Build a synthetic WIMAS/WWC5 bridge with positional quality. |
| `KFM-P2-PROG-0010` | Satellite-driven vegetation change alerts (HLS / Landsat) | `RECONCILE_EXISTING` | Existing HLS NDVI schema, validator, tests, receipt, and workflow. |
| `KFM-P2-PROG-0011` | BLM CadNSDI and GLO records ingest as the cadastral spine | `HARDEN_EXISTING` | Complete side-effect-free BLM modules and fixtures. |
| `KFM-P2-PROG-0017` | Waterbody crosswalks: NHDPlus, NWIS site, KGS, and Kansas Mesonet | `RECONCILE_EXISTING` | Existing NHDPlus waterbody crosswalk and identity bridge. |
| `KFM-P2-PROG-0030` | Mermaid as primary diagram source, Kroki as fallback rendering path | `HARDEN_EXISTING` | Add deterministic local Mermaid validation/rendering. |
| `KFM-P2-PROG-0031` | CITATION.cff for each repository | `HARDEN_EXISTING` | Replace the root CITATION.cff placeholder with reviewed metadata. |

## Dependency-ordered campaign

| Order | Slice | Source cards | Boundary |
|---:|---|---|---|
| 1 | Pass 2 crosswalk | All 110 | Documentation intake and authoring receipt only. |
| 2 | K-anonymity assessment | `KFM-P2-IDEA-0015` | Fixture-first contract/schema/validator/tests. The referenced policy profile selects `k`; the atlas does not. |
| 3 | ECHO/TRI facility evidence profile | `KFM-P2-IDEA-0025`; `KFM-P2-PROG-0007` | Reuse the existing EvidenceBundle family; separate compliance/inspection from annual release reporting; no network. |
| 4 | NFHL/NLD/NID profile | `KFM-P2-IDEA-0026`; `KFM-P2-PROG-0008` | Future independent slice; preserve hazard/infrastructure source roles and fail closed on operational detail. |
| 5 | Mobile/offline performance | Pass 2 MAP cards | Future campaign after representative Explorer and release fixtures exist. |
| 6 | BLM and WIMAS/WWC5 completion | Cadastral and water-use cards | Future source-admission work after endpoint, terms, rights, sensitivity, and identity review. |
| 7 | Diagram/citation hardening | `KFM-P2-PROG-0030`; `KFM-P2-PROG-0031` | Future docs/tooling work; remote rendering remains optional until admitted. |

Each implementation slice requires its own review boundary and rollback. Passing tests or merging a pull request remains distinct from source activation, promotion, release, deployment, and publication.

## Pass 2 acceptance overlay

The 39 expanded cards are imported as applicable acceptance pressure:

1. fixture-first, no-network CI;
2. deterministic identity and source-card lineage;
3. explicit source roles and anti-collapse behavior;
4. EvidenceRef/EvidenceBundle closure where claims depend on evidence;
5. rights, sensitivity, time, geography, review, and release state;
6. finite outcomes with stable reason codes;
7. input/transform/validation/authoring receipts;
8. versioned artifacts and no in-place public replacement;
9. correction, withdrawal, rollback, cache invalidation, and supersession;
10. trust-visible UI only after governed release; and
11. no watcher, renderer, tile, graph, model, or AI output treated as sovereign truth.

Which controls apply is decided by the affected object family and consequence. This overlay does not create a universal schema or policy bundle.

## Validation and rollback

Local authoring validation confirmed 110 unique stable IDs, exact carry-state counts, one disposition for every new card, disposition closure to 110, source and sidecar digests, and receipt-to-artifact SHA-256 binding. A passing result proves local accounting only, not source currentness, rights, runtime behavior, hosted CI, human review, release, or publication.

Before merge, close the draft pull request and delete its branch. After an authorized merge, revert the bounded commit or merge commit. If later repository evidence changes a disposition, update the row in place, preserve the prior commit as lineage, and never delete the stable ID.

<p align="right"><a href="#top">Back to top</a></p>
