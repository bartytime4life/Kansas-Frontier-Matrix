<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/usda-nass/readme
title: USDA NASS Raw Compatibility README
path: data/raw/usda-nass/README.md
type: data-raw-source-family-compatibility-readme
version: v0.2.0
prior_version: v0.1.0
status: draft
owners:
  - <agriculture-domain-steward>
  - <usda-nass-source-steward>
  - <data-steward>
  - <rights-reviewer>
  - <release-steward>
created: 2026-06-28
updated: 2026-10-11
policy_label: restricted-review
truth_posture: cite-or-abstain
lifecycle_phase: raw
owning_root: data/
responsibility: Preserve the tracked top-level USDA NASS RAW compatibility and reference documentation without treating this subtree as a physical source-first capture home or duplicating RAW bytes.
requested_path_segment: usda-nass
related_domain_lane: agriculture
sibling_compatibility_lane: data/raw/agriculture/usda-nass/
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
  - ../../../docs/doctrine/directory-rules.md
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
  - compatibility-reference
  - source-first
notes:
  - "This README replaces placeholder content at `data/raw/usda-nass/README.md`."
  - "Both this root-level path and `data/raw/agriculture/usda-nass/` are compatibility/reference documentation lanes; neither is an accepted physical capture home, and both must reference one source-first capture."
  - "README presence confirms documentation only; it does not prove payloads, SourceDescriptor records, connector activation, receipts, validators, fixtures, review controls, or release readiness."
  - "2026-10-11 reconciliation: aligned to accepted DIR-SOURCE-001 and the parent data/raw/README.md source-first contract; this lane is compatibility/reference documentation, not a physical capture home; metadata normalized to the required profile; no payload, path, writer, or release state changed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# USDA NASS RAW Compatibility Index

Compatibility and reference documentation for top-level USDA NASS RAW topology; not a physical source-capture home.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Segment: compatibility" src="https://img.shields.io/badge/segment-compatibility-orange">
  <img alt="Domain: agriculture" src="https://img.shields.io/badge/domain-agriculture-2e7d32">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
</p>

> [!CAUTION]
> `data/raw/usda-nass/` is a no-public-path compatibility/reference path. Accepted Directory Rules require one source-first capture identity, so neither this subtree nor `data/raw/agriculture/usda-nass/` is a default physical capture home, and neither may receive duplicate RAW payloads. This file is not processed truth, catalog truth, proof, receipt authority, source registry authority, rights authority, policy authority, release authority, public API/UI material, or published artifact authority.

---

## Canonical path warning

Directory Rules state that placement encodes ownership, governance, and lifecycle, and topic alone does not justify a root folder. Accepted rule `DIR-SOURCE-001` also requires one source-first capture identity: one USDA NASS capture may support Agriculture and other domains without duplicated RAW bytes.

This root-level path and the Agriculture-facing [`../agriculture/usda-nass/README.md`](../agriculture/usda-nass/README.md) document the same upstream source. Both lanes must reference the same single source-first capture, never two copies. Neither path is an accepted physical capture home; exact source-first placement and legacy lane disposition remain **HOLD / NEEDS VERIFICATION**.

Treat this root-level path as a compatibility pointer or migration holding index only unless an accepted placement decision or ADR authorizes otherwise.

---

## Scope

This directory may document compatibility handling for USDA NASS RAW topology. It may reference one governed source-first capture, but it does not establish where that capture is stored, and it must not become a parallel source lane or second writer.

Do not place raw payloads, copied source runs, source-head records, checksums, or other capture sidecars in this subtree merely because they relate to USDA NASS or support Agriculture. Exact physical placement and legacy migration remain **HOLD**.

USDA NASS material includes separate product surfaces such as QuickStats / Crop Progress and Cropland Data Layer. These products have different roles, cadences, geometry/support, query lineage, and downstream validation needs.

The governed source-first capture records capture context: source, product identity, query parameters, aggregation unit, source time, retrieval time, citation, rights posture, response digest, and review notes.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/usda-nass/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw` |
| Requested segment | `usda-nass` |
| Related domain lane | `agriculture` |
| Sibling compatibility lane | `data/raw/agriculture/usda-nass/` (references the same single source-first capture) |
| Artifact role | Compatibility/reference index for top-level USDA NASS documentation and unresolved legacy RAW topology |
| Upstream | References to an admitted source-first capture only; physical placement remains **NEEDS VERIFICATION** |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Downstream | Governed Agriculture WORK or QUARANTINE procedures consume references or approved handoffs, not assumed domain-local copies |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/`, not this directory |
| Receipt authority | `data/receipts/`, not this directory |
| Registry authority | `data/registry/sources/`, not this directory |
| Policy authority | `policy/`, not this directory |

---

## Product separation

| Product surface | Source-first capture must preserve | Boundary |
|---|---|---|
| USDA NASS QuickStats / Crop Progress | Preserve query parameters, geography, year/period, commodity, statistic, unit, aggregation unit, row count, retrieval time, and digest. | Aggregate statistics do not become field-level truth from RAW. |
| USDA NASS CDL / Cropland Data Layer | Preserve product identity, raster vintage, classification caveats, spatial support, source reference, rights posture, and digest. | CDL must not collapse into QuickStats aggregates. |
| Future USDA NASS product | Admit only after source role, rights, cadence, citation, and validation posture are recorded. | Compatibility path presence is not admission. |

---

## RAW source posture

| Rule | Handling |
|---|---|
| Capture identity is source-first | Register one `source_id` and preserve one immutable capture identity; domain references may support Agriculture without duplicating RAW bytes. |
| Physical placement is held | Do not infer `data/raw/usda-nass/` or `data/raw/agriculture/usda-nass/` as the capture home. Use only an accepted writer/path contract; none is established by this README. |
| Compatibility path is not authority | Neither `data/raw/usda-nass/` nor `data/raw/agriculture/usda-nass/` is placement authority; both are compatibility/reference documentation. |
| RAW is immutable source capture | Payloads or payload references at the accepted source-first home must be hash-bound and should not be overwritten in place. |
| Product identity is preserved | QuickStats, Crop Progress, CDL, and future NASS products remain separate surfaces. |
| Aggregates remain aggregates | County, CRD, state, year, or period summaries must carry aggregation scope and query lineage. |
| Public clients never read RAW | Public layers, reports, PMTiles, stories, graph edges, vector indexes, API payloads, and generated answers cannot read this RAW path directly. |

---

## Directory map

```text
data/raw/usda-nass/
└── README.md
```

This is the confirmed documentation topology, not a storage specification. Do not add a legacy/migration reference directory, payload, or local index here until an accepted source-first placement or compatibility decision defines its role. New USDA NASS captures belong at one accepted source-first RAW home whose exact path remains **NEEDS VERIFICATION** — not in this subtree and not in a second domain-scoped copy.

Any optional RAW-local index (previously sketched in this map as a local JSON index file) is a proposed shape for a future accepted source-first home or documentation contract, not this subtree.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Remain at the source-first RAW home | Capture is admitted, but no downstream normalization decision has been made. This compatibility lane may retain a governed, non-canonical reference only. |
| Quarantine | Path authority, rights, source role, product identity, query lineage, aggregation unit, citation, digest, schema, admission state, or physical placement is unresolved. |
| Return / reject or migrate | Steward review says legacy material must not be retained here; correction or migration occurs through the owning source-first or quarantine procedure to one accepted source-first home, with hashes and references preserved — never by copying into `data/raw/agriculture/usda-nass/`. |
| Move to work | A governed reference or approved handoff may enter Agriculture WORK only when source role, product separation, citation, hash, and validation support are sufficient. |
| Promote downstream | Only after later WORK, PROCESSED, CATALOG, and RELEASE gates close with inspectable evidence. |

---

## Forbidden shortcut

```text
source-first RAW capture (physical path NEEDS VERIFICATION)
→ data/processed/agriculture/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces placeholder content at `data/raw/usda-nass/README.md`. | **CONFIRMED authored** |
| The target path existed and contained only placeholder content before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| `data/raw/agriculture/usda-nass/README.md` exists as the Agriculture-facing USDA NASS README. | **CONFIRMED by GitHub contents API during this edit**; its earlier "canonical source lane" framing is superseded — it is a compatibility/reference lane under `DIR-SOURCE-001` |
| Agriculture RAW parent README confirms `usda-nass/` as a child lane under `data/raw/agriculture/`. | **CONFIRMED by GitHub contents API during this edit** |
| Directory Rules say placement encodes ownership, governance, and lifecycle; topic alone does not justify a root folder. | **CONFIRMED by GitHub contents API during this edit** |
| README presence proves payloads, SourceDescriptors, connectors, validators, fixtures, checks, review controls, or release readiness. | **DENY** |
| Accepted Directory Rules require one source-first capture identity and prohibit duplicated RAW bytes across domains. | **CONFIRMED** (`DIR-SOURCE-001`) |
| This subtree (or `data/raw/agriculture/usda-nass/`) is an accepted physical source-first capture home. | **DENY — no placement decision found as of 2026-10-11** |
| Actual USDA NASS raw payloads exist under this compatibility subtree. | **UNKNOWN; none added or moved by this documentation correction.** No payload files are tracked under this subtree at `main@9e8bf3e6`; external or untracked stores remain UNKNOWN |
| This README is reconciled to the parent source-first contract. | **CONFIRMED authored 2026-10-11** |
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
- [`../../../docs/doctrine/directory-rules.md`](../../../docs/doctrine/directory-rules.md) — accepted Directory Rules (`DIR-SOURCE-001`)
- [`../../../docs/architecture/directory-rules.md`](../../../docs/architecture/directory-rules.md)
- [`../../../docs/domains/agriculture/SOURCE_REGISTRY.md`](../../../docs/domains/agriculture/SOURCE_REGISTRY.md)
- [`../../../docs/domains/agriculture/SOURCES.md`](../../../docs/domains/agriculture/SOURCES.md)
- [`../../../docs/sources/catalog/usda/usda-nass-quickstats.md`](../../../docs/sources/catalog/usda/usda-nass-quickstats.md)
- [`../../../docs/sources/catalog/usda/usda-nass-cdl.md`](../../../docs/sources/catalog/usda/usda-nass-cdl.md)
- [`../../../release/manifests/README.md`](../../../release/manifests/README.md)

---

KFM rule: this directory is a USDA NASS compatibility/reference index. One governed source-first capture may support Agriculture without duplicated RAW bytes; this subtree does not establish physical placement. It is not a capture home, source-family doctrine, registry authority, rights authority, policy authority, proof authority, receipt authority, release authority, catalog authority, crop truth, field truth, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
