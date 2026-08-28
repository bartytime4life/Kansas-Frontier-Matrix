<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/usda-nass/readme
name: USDA NASS Raw Compatibility README
path: data/raw/usda-nass/README.md
type: data-raw-source-family-compatibility-readme
version: v0.1.0
status: draft
owners:
  - <agriculture-domain-steward>
  - <usda-nass-source-steward>
  - <data-steward>
  - <rights-reviewer>
  - <release-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: restricted-review
truth_posture: cite-or-abstain
lifecycle_phase: raw
responsibility_root: data/
requested_path_segment: usda-nass
canonical_domain_lane: agriculture
canonical_source_lane: data/raw/agriculture/usda-nass/
artifact_family: usda-nass-raw-compatibility-index
sensitivity_posture: raw-internal; compatibility-path; no-public-path; aggregate-guard-required; rights-needs-verification; release-blocked
related:
  - ../agriculture/usda-nass/README.md
  - ../agriculture/README.md
  - ../README.md
  - ../../README.md
  - ../../quarantine/agriculture/README.md
  - ../../processed/agriculture/README.md
  - ../../catalog/domain/agriculture/README.md
  - ../../published/layers/agriculture/README.md
  - ../../registry/sources/README.md
  - ../../../docs/architecture/directory-rules.md
  - ../../../docs/domains/agriculture/SOURCE_REGISTRY.md
  - ../../../docs/domains/agriculture/SOURCES.md
  - ../../../docs/sources/catalog/usda/usda-nass-quickstats.md
  - ../../../docs/sources/catalog/usda/usda-nass-cdl.md
  - ../../../release/manifests/README.md
tags:
  - kfm
  - data
  - raw
  - usda-nass
  - agriculture
  - compatibility-path
  - quickstats
  - crop-progress
  - cdl
  - aggregate
  - source-capture
  - source-role
  - no-public-path
notes:
  - "This README replaces placeholder content at `data/raw/usda-nass/README.md`."
  - "The canonical Agriculture source lane is `data/raw/agriculture/usda-nass/`; this root-level path is compatibility-only unless an ADR says otherwise."
  - "README presence confirms documentation only; it does not prove payloads, SourceDescriptor records, connector activation, receipts, validators, fixtures, review controls, or release readiness."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# USDA NASS RAW Compatibility Index

Compatibility RAW lifecycle index for USDA NASS source captures associated with the Agriculture domain.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Segment: compatibility" src="https://img.shields.io/badge/segment-compatibility-orange">
  <img alt="Domain: agriculture" src="https://img.shields.io/badge/domain-agriculture-2e7d32">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
</p>

> [!CAUTION]
> `data/raw/usda-nass/` is a compatibility RAW path. The canonical Agriculture source lane is `data/raw/agriculture/usda-nass/`. This file is not processed truth, catalog truth, proof, receipt authority, source registry authority, rights authority, policy authority, release authority, public API/UI material, or published artifact authority.

---

## Canonical path warning

Directory Rules state that placement encodes ownership, governance, and lifecycle, and topic alone does not justify a root folder. USDA NASS is a source family inside the Agriculture domain, so new captures should normally use:

```text
data/raw/agriculture/usda-nass/
```

Treat this root-level path as a compatibility pointer or migration holding index only unless an accepted ADR authorizes it.

---

## Scope

This directory may document compatibility handling for USDA NASS RAW source-capture material. It should not become a parallel Agriculture source lane.

USDA NASS material includes separate product surfaces such as QuickStats / Crop Progress and Cropland Data Layer. These products have different roles, cadences, geometry/support, query lineage, and downstream validation needs.

RAW records capture context: source, product identity, query parameters, aggregation unit, source time, retrieval time, citation, rights posture, response digest, and review notes.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/usda-nass/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw` |
| Requested segment | `usda-nass` |
| Canonical domain lane | `agriculture` |
| Canonical source lane | `data/raw/agriculture/usda-nass/` |
| Lane type | Compatibility RAW index |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Downstream | Canonical Agriculture work/quarantine lanes only after governed triage |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/`, not this directory |
| Receipt authority | `data/receipts/`, not this directory |
| Registry authority | `data/registry/sources/`, not this directory |
| Policy authority | `policy/`, not this directory |

---

## Product separation

| Product surface | RAW handling | Boundary |
|---|---|---|
| USDA NASS QuickStats / Crop Progress | Preserve query parameters, geography, year/period, commodity, statistic, unit, aggregation unit, row count, retrieval time, and digest. | Aggregate statistics do not become field-level truth from RAW. |
| USDA NASS CDL / Cropland Data Layer | Preserve product identity, raster vintage, classification caveats, spatial support, source reference, rights posture, and digest. | CDL must not collapse into QuickStats aggregates. |
| Future USDA NASS product | Admit only after source role, rights, cadence, citation, and validation posture are recorded. | Compatibility path presence is not admission. |

---

## RAW source posture

| Rule | Handling |
|---|---|
| Compatibility path is not authority | `data/raw/usda-nass/` does not replace `data/raw/agriculture/usda-nass/`. |
| RAW is source capture | Payloads or payload references must be hash-bound and should not be overwritten in place. |
| Product identity is preserved | QuickStats, Crop Progress, CDL, and future NASS products remain separate surfaces. |
| Aggregates remain aggregates | County, CRD, state, year, or period summaries must carry aggregation scope and query lineage. |
| Public clients never read RAW | Public layers, reports, PMTiles, stories, graph edges, vector indexes, API payloads, and generated answers cannot read this RAW path directly. |

---

## Directory map

```text
data/raw/usda-nass/
├── README.md
├── <legacy-or-migration-reference>/
│   └── README.md
└── index.local.json
```

New source-family captures should normally use:

```text
data/raw/agriculture/usda-nass/
```

`index.local.json` is optional and must remain RAW-local.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay RAW compatibility | Compatibility reference is intentionally retained and marked as non-canonical. |
| Quarantine | Path authority, rights, source role, product identity, query lineage, aggregation unit, citation, digest, schema, or admission state is unresolved. |
| Move to canonical RAW lane | Steward review confirms material belongs under `data/raw/agriculture/usda-nass/`, with hashes and references preserved. |
| Move to work | Only through the canonical Agriculture lane after source role, product separation, citation, hash, and validation support are sufficient. |
| Promote downstream | Only after later WORK, PROCESSED, CATALOG, and RELEASE gates close with inspectable evidence. |

---

## Forbidden shortcut

```text
data/raw/usda-nass/
→ data/processed/agriculture/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has happened through the canonical Agriculture lane.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces placeholder content at `data/raw/usda-nass/README.md`. | **CONFIRMED authored** |
| The target path existed and contained only placeholder content before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| `data/raw/agriculture/usda-nass/README.md` exists as the canonical Agriculture USDA NASS RAW source lane. | **CONFIRMED by GitHub contents API during this edit** |
| Agriculture RAW parent README confirms `usda-nass/` as a child lane under `data/raw/agriculture/`. | **CONFIRMED by GitHub contents API during this edit** |
| Directory Rules say placement encodes ownership, governance, and lifecycle; topic alone does not justify a root folder. | **CONFIRMED by GitHub contents API during this edit** |
| README presence proves payloads, SourceDescriptors, connectors, validators, fixtures, checks, review controls, or release readiness. | **DENY** |
| Actual USDA NASS raw payloads exist under this compatibility subtree. | **UNKNOWN** |
| This README is proof, receipt, release, catalog, registry, policy, crop truth, field truth, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`../agriculture/usda-nass/README.md`](../agriculture/usda-nass/README.md)
- [`../agriculture/README.md`](../agriculture/README.md)
- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../quarantine/agriculture/README.md`](../../quarantine/agriculture/README.md)
- [`../../processed/agriculture/README.md`](../../processed/agriculture/README.md)
- [`../../catalog/domain/agriculture/README.md`](../../catalog/domain/agriculture/README.md)
- [`../../published/layers/agriculture/README.md`](../../published/layers/agriculture/README.md)
- [`../../registry/sources/README.md`](../../registry/sources/README.md)
- [`../../../docs/architecture/directory-rules.md`](../../../docs/architecture/directory-rules.md)
- [`../../../docs/domains/agriculture/SOURCE_REGISTRY.md`](../../../docs/domains/agriculture/SOURCE_REGISTRY.md)
- [`../../../docs/domains/agriculture/SOURCES.md`](../../../docs/domains/agriculture/SOURCES.md)
- [`../../../docs/sources/catalog/usda/usda-nass-quickstats.md`](../../../docs/sources/catalog/usda/usda-nass-quickstats.md)
- [`../../../docs/sources/catalog/usda/usda-nass-cdl.md`](../../../docs/sources/catalog/usda/usda-nass-cdl.md)
- [`../../../release/manifests/README.md`](../../../release/manifests/README.md)

---

KFM rule: this directory is a USDA NASS RAW compatibility index only. It is not the canonical Agriculture source lane, source-family doctrine, registry authority, rights authority, policy authority, proof authority, receipt authority, release authority, catalog authority, crop truth, field truth, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
