<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/pass-1-idea-index-coverage-source-map
title: KFM Pass 1 Idea Index - Governed Coverage and Import Source Map
type: exploratory-intake-source-map
version: v0.1.0
status: triaged; exploratory; non-authoritative; repository-grounded
owners: OWNER_TBD - intake steward; architecture reviewer; affected domain stewards
created: 2026-08-08
updated: 2026-08-08
policy_label: public; intake; exploratory; no-source-activation; no-publication
owning_root: docs/
responsibility: Preserve the KFM Pass 1 dossier identity, map all 74 stable cards to bounded repository work, distinguish existing implementation from gaps, and prevent duplicate or authority-creating imports.
source_evidence:
  - captured_filename: KFM_Pass_1_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf
    sha256: d73bf83f53b0aa4c56362b56fdba5dce81ca8dec2f5c48a189b62939a035cfa6
    page_count: 121
    card_count: 74
  - embedded_manifest_sha256: 60245bbcd7f569e93a5944c2551a50061d18cac51fade81a465770d1b8507cd2
  - embedded_index_sha256: 4639f312ba6e38ad5b94459b35966c68e1fd3828be18320bd0ca6a7f414575e8
  - embedded_change_report_sha256: b88ac39d565c4c06be7584e0fcba9c3d8f255a99f5860ee033134fdd0f06d615
repository_evidence:
  repository: bartytime4life/Kansas-Frontier-Matrix
  remote_main_snapshot: e28a83d286cd16743665436001d8544943b366e0
  reviewed_at: 2026-08-08
related:
  - ./README.md
  - ../README.md
  - ../NEW_IDEAS_INDEX.md
  - ../new-ideas-register.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, intake, pass-1, idea-index, coverage, lineage, repository-import, source-map]
notes:
  - "The Pass 1 atlas is a downstream planning carrier; this source map does not promote its cards or create implementation authority."
  - "All 74 source cards were marked NEW because the declared Pass 0 baseline was unavailable, not because all capabilities are absent."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# KFM Pass 1 idea index — governed coverage and import source map

> **Outcome:** preserve all 74 Pass 1 stable IDs, map them to bounded work, and
> route only dependency-closed gaps into later pull requests.

> [!IMPORTANT]
> This is **intake and coverage evidence only**. It does not adopt the atlas,
> activate a source, create policy or schema authority, promote lifecycle state,
> approve release, or publish anything.

## Executive disposition

The dossier records **74 active cards across 13 categories**. Every card is
`NEW` because `KFM-Atlas_Pass_0` was unavailable to that run. That is a
carry-forward fact, not evidence that the repository lacks all 74 capabilities.

Import uses reconcile-before-create:

```text
source card
  -> inspect current repository evidence
  -> PRESENT / PARTIAL / CONFLICTED / MISSING / DEFERRED
  -> select one owning responsibility root
  -> implement the smallest dependency-closed gap
  -X-> automatic promotion or publication
```

## Source identity and evidence boundary

| Field | Value |
|---|---|
| Source | `KFM_Pass_1_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf` |
| SHA-256 | `d73bf83f53b0aa4c56362b56fdba5dce81ca8dec2f5c48a189b62939a035cfa6` |
| Pages / cards / categories | 121 / 74 / 13 |
| Authority | downstream carrier / exploratory planning |
| Repository snapshot | `main@e28a83d286cd16743665436001d8544943b366e0` |
| Publication effect | none |

The PDF and embedded sidecars are not committed by this change. Their digests
are retained so later extraction and supersession checks can be reproduced.

## Directory Rules basis

`docs/intake/exploratory/` owns this human-readable, pre-promotion source map.
It is not a semantic contract, schema, policy, registry record, receipt, proof,
release decision, or published data artifact.

## Import bundle register

| Bundle | Priority | Cards | Disposition at reviewed snapshot | Smallest next action |
|---|---|---:|---|---|

| `P1-IMPORT-01` — Pass 1 coverage, lineage, and intake register | P0 control-plane precursor | 7 | **PARTIAL** — `docs/intake/` already contains packet indexes and exploratory source maps; no Pass 1 source map was found. | Add this bounded coverage map; later PRs cite its stable IDs. |
| `P1-IMPORT-02` — Source admission, source-head evidence, and watcher candidate lifecycle | P0 trust boundary | 10 | **PARTIAL** — `SourceDescriptor` schema/fixtures, receipts, domain validators, and a fixture-only CDL comparator exist; generic entrypoint execution remains brittle. | Harden the existing generic SourceDescriptor validator and tests. |
| `P1-IMPORT-03` — Evidence resolution, process-memory receipts, and deterministic identity | P0 shared trust kernel | 6 | **SUBSTANTIAL / BOUNDED** — `packages/evidence-resolver/` already implements bounded resolution and correction-history checks. | Reconcile coverage; do not create a competing resolver. |
| `P1-IMPORT-04` — Promotion, release, correction, rollback, and policy parity | P0 publication control | 11 | **PARTIAL** — Promotion, release, correction, rollback, receipts, proofs, and validators exist; end-to-end release closure remains unproved here. | Select one synthetic release dry run after gate vocabulary and homes are reverified. |
| `P1-IMPORT-05` — Immutable PMTiles/COG artifact verification and fail-closed map trust states | P1 map trust proof | 8 | **PARTIAL / ADR PROPOSED** — PMTiles/COG and KFMGeoManifest surfaces exist; ADR-0023 remains proposed. | Add only fixture-first negative-path proof under current homes. |
| `P1-IMPORT-06` — STAC/DCAT/PROV and biodiversity STAC × Darwin Core profile consolidation | P1 standards convergence | 2 | **CONFLICTED** — Multiple STAC × Darwin Core profile documents are present. | Inventory and converge; do not add another profile. |
| `P1-IMPORT-07` — CARE-aware metadata, rights gates, geoprivacy, and steward review | P1 sensitivity control | 7 | **PARTIAL** — Rights, consent, geoprivacy, sensitivity, and source-role surfaces exist. | Prove one public-safe transform with negative fixtures. |
| `P1-IMPORT-08` — Knowledge-character, temporal, geography-version, and assertion semantics | P1 shared modeling kernel | 9 | **PARTIAL / NEEDS VERIFICATION** — Temporal, geography-version, source-role, and assertion semantics exist across lanes without one Pass 1 closure proof. | Select one shared-kernel contract gap after current schema/ADR inspection. |
| `P1-IMPORT-09` — Evidence Drawer, Focus Mode, bounded AI, and StoryNode inheritance | P1 trust-visible UI | 5 | **PARTIAL** — Evidence Drawer, Focus Mode, Story, and runtime evidence-resolution surfaces exist. | Audit parity and harden one non-conflicted payload boundary. |
| `P1-IMPORT-10` — Policy-bound analytics, model/assumption cards, and controlled materiality triggers | P2 analytical hardening | 5 | **PARTIAL / DOMAIN-SPECIFIC** — Fixture-first CDL materiality logic and analytical lanes exist. | Keep thresholds policy/caller supplied; add assumption cards only for a selected use case. |
| `P1-IMPORT-11` — Proof-bearing domain slices and Frontier county-year panel roadmap | P1/P2 product roadmap | 4 | **MIXED** — Domain proof slices exist; Frontier object families remain mainly planning/reference surfaces. | Hold the county-year panel until shared evidence/geography/release controls are fixture-proven. |

## Stable-ID coverage by bundle

The following membership is the complete 74-card coverage map. A card listed in
more than one bundle is intentionally cross-cutting; it is not duplicated.

### `P1-IMPORT-01` — Pass 1 coverage, lineage, and intake register

`KFM-P1-IDEA-0001`, `KFM-P1-IDEA-0002`, `KFM-P1-IDEA-0003`, `KFM-P1-IDEA-0004`, `KFM-P1-IDEA-0005`,
`KFM-P1-PROG-0060`, `KFM-P1-PROG-0055`

### `P1-IMPORT-02` — Source admission, source-head evidence, and watcher candidate lifecycle

`KFM-P1-IDEA-0006`, `KFM-P1-IDEA-0011`, `KFM-P1-IDEA-0014`, `KFM-P1-PROG-0007`, `KFM-P1-PROG-0008`,
`KFM-P1-PROG-0009`, `KFM-P1-PROG-0010`, `KFM-P1-PROG-0026`, `KFM-P1-PROG-0027`, `KFM-P1-IDEA-0059`

### `P1-IMPORT-03` — Evidence resolution, process-memory receipts, and deterministic identity

`KFM-P1-IDEA-0012`, `KFM-P1-IDEA-0019`, `KFM-P1-PROG-0013`, `KFM-P1-PROG-0015`, `KFM-P1-PROG-0016`,
`KFM-P1-PROG-0054`

### `P1-IMPORT-04` — Promotion, release, correction, rollback, and policy parity

`KFM-P1-IDEA-0020`, `KFM-P1-IDEA-0056`, `KFM-P1-PROG-0057`, `KFM-P1-PROG-0058`, `KFM-P1-PROG-0017`,
`KFM-P1-PROG-0053`, `KFM-P1-PROG-0025`, `KFM-P1-PROG-0028`, `KFM-P1-PROG-0024`, `KFM-P1-PROG-0029`,
`KFM-P1-PROG-0030`

### `P1-IMPORT-05` — Immutable PMTiles/COG artifact verification and fail-closed map trust states

`KFM-P1-PROG-0018`, `KFM-P1-FEAT-0038`, `KFM-P1-FEAT-0039`, `KFM-P1-FEAT-0042`, `KFM-P1-FEAT-0044`,
`KFM-P1-IDEA-0040`, `KFM-P1-PROG-0041`, `KFM-P1-PROG-0043`

### `P1-IMPORT-06` — STAC/DCAT/PROV and biodiversity STAC × Darwin Core profile consolidation

`KFM-P1-PROG-0021`, `KFM-P1-PROG-0022`

### `P1-IMPORT-07` — CARE-aware metadata, rights gates, geoprivacy, and steward review

`KFM-P1-PROG-0023`, `KFM-P1-IDEA-0031`, `KFM-P1-IDEA-0033`, `KFM-P1-IDEA-0034`, `KFM-P1-IDEA-0037`,
`KFM-P1-PROG-0032`, `KFM-P1-PROG-0035`

### `P1-IMPORT-08` — Knowledge-character, temporal, geography-version, and assertion semantics

`KFM-P1-IDEA-0045`, `KFM-P1-IDEA-0046`, `KFM-P1-IDEA-0047`, `KFM-P1-IDEA-0049`, `KFM-P1-IDEA-0050`,
`KFM-P1-IDEA-0051`, `KFM-P1-IDEA-0072`, `KFM-P1-PROG-0048`, `KFM-P1-PROG-0052`

### `P1-IMPORT-09` — Evidence Drawer, Focus Mode, bounded AI, and StoryNode inheritance

`KFM-P1-FEAT-0065`, `KFM-P1-FEAT-0066`, `KFM-P1-FEAT-0067`, `KFM-P1-FEAT-0068`, `KFM-P1-FEAT-0074`

### `P1-IMPORT-10` — Policy-bound analytics, model/assumption cards, and controlled materiality triggers

`KFM-P1-IDEA-0036`, `KFM-P1-IDEA-0061`, `KFM-P1-IDEA-0064`, `KFM-P1-PROG-0062`, `KFM-P1-PROG-0063`

### `P1-IMPORT-11` — Proof-bearing domain slices and Frontier county-year panel roadmap

`KFM-P1-IDEA-0069`, `KFM-P1-IDEA-0070`, `KFM-P1-IDEA-0071`, `KFM-P1-IDEA-0073`

## Dependency-ordered waves

### Wave 1 — intake and source admission

1. Preserve this stable-ID map.
2. Harden the existing generic `SourceDescriptor` validator entrypoint and
   no-network tests without creating another validator authority.
3. Keep watchers fixture-only and non-publishing until rights, role, cadence,
   and activation are independently approved.

### Wave 2 — trust and publication proof

1. Reuse the current evidence resolver rather than duplicating it.
2. Prove one synthetic release candidate through finite gate outcomes,
   correction lineage, and rollback without writing `PUBLISHED`.
3. Keep receipts, proofs, policies, catalogs, manifests, corrections, and
   rollback records separate.

### Wave 3 — map, standards, policy, and UI convergence

1. Reconcile PMTiles/COG verification with the still-proposed signing ADR.
2. Consolidate duplicate STAC/Darwin Core documentation.
3. Prove one public-safe transform and one Evidence Drawer/Story/Focus parity
   boundary using negative fixtures.

### Wave 4 — analytics and products

1. Require explicit method, assumptions, uncertainty, and policy-bound
   materiality for analytical outputs.
2. Prefer an existing public-safe hydrology or ecology slice.
3. Hold the Frontier county-year panel until geography, evidence, and release
   controls are fixture-proven.

## Non-effects

This change does not promote cards, activate sources, settle ADRs, change
contracts/schemas/policy/runtime/release, infer full enforcement from search
hits, or delete/supersede prior intake material.

## Acceptance checks

- [x] Source PDF and all three sidecar identities are recorded.
- [x] All 74 stable IDs are mapped to the 11 bundles.
- [x] Existing overlap is separated from remaining work.
- [x] No source activation, promotion, release, or publication occurs.
- [ ] Hosted documentation checks pass.
- [ ] Reviewer confirms later PRs cite stable IDs and avoid parallel authority.

## Rollback

Revert the commit adding this file. The source dossier, prior intake records,
existing implementation, and Git history remain untouched.

[Back to top](#top)
