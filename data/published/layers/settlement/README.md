<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/published/layers/settlement/readme
name: Settlement Published Layers README
path: data/published/layers/settlement/README.md
type: data-lane-readme
version: v0.1.0
status: draft
owners:
  - <settlements-infrastructure-domain-steward>
  - <release-steward>
  - <map-layer-steward>
created: 2026-06-26
updated: 2026-06-26
policy_label: restricted-review
truth_posture: cite-or-abstain
lifecycle_phase: published
responsibility_root: data/
domain: settlement
placement_status: CONFLICTED_NEEDS_VERIFICATION
artifact_family: released-public-safe-settlement-map-layers
sensitivity_posture: public-safe-derivatives-only; sovereignty-and-cultural-adjacency-review-required; release-required
related:
  - ../README.md
  - ../../README.md
  - ../../../README.md
  - ../../../../docs/domains/settlements-infrastructure/CANONICAL_PATHS.md
  - ../../../../docs/domains/settlements-infrastructure/DATA_LIFECYCLE.md
  - ../../../../docs/domains/settlements-infrastructure/sublanes/settlements.md
  - ../../../../docs/domains/settlements-infrastructure/RELEASE_INDEX.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../proofs/README.md
  - ../../../../release/manifests/README.md
tags:
  - kfm
  - data
  - published
  - layers
  - settlement
  - settlements-infrastructure
  - places
  - municipalities
  - census-places
  - historic-townsites
  - release
  - evidence-first
notes:
  - "This README documents the requested settlement published-layer path."
  - "Path segment is CONFLICTED / NEEDS VERIFICATION because current domain docs identify settlements-infrastructure as the canonical domain slug while Atlas-derived crosswalk material also uses settlement."
  - "Published artifacts here are downstream delivery artifacts; release, proof, receipt, policy, source, processed, and catalog authority stay in their owning roots."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Settlement Published Layers

Released public-safe settlement layer artifacts for place and community identity views.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: published" src="https://img.shields.io/badge/lifecycle-published-success">
  <img alt="Domain: settlement" src="https://img.shields.io/badge/domain-settlement-7048e8">
  <img alt="Placement: conflicted needs verification" src="https://img.shields.io/badge/placement-CONFLICTED%20%2F%20NEEDS%20VERIFICATION-orange">
  <img alt="Policy: restricted review" src="https://img.shields.io/badge/policy-restricted--review-critical">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-blueviolet">
</p>

**Quick links:** [Scope](#scope) · [Repo fit](#repo-fit) · [Inputs](#inputs) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Publication boundary](#publication-boundary) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> **Placement is CONFLICTED / NEEDS VERIFICATION.** This requested path uses `settlement/`. The current domain-path registry identifies `settlements-infrastructure` as the working canonical domain slug while also recording a conflict with Atlas-derived `settlement/` crosswalk material. Treat this path as a restricted-review placeholder until an ADR, migration note, or directory-rule decision resolves the slug.

---

## Scope

This directory may hold released public-safe settlement layer artifacts for place and community identity views. Settlement layers may support map viewing, Evidence Drawer lookups, historical-place context, municipal/census-place display, or public-safe settlement status context after the normal KFM release gates have passed.

A layer here is a downstream delivery artifact. It is not the source record, settlement truth, municipality truth, cultural authority, catalog truth, proof bundle, release decision, registry authority, or AI interpretation.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/published/layers/settlement/` |
| Responsibility root | `data/` |
| Lifecycle phase | `published/` |
| Requested domain segment | `settlement` |
| Related canonical-path domain segment | `settlements-infrastructure` |
| Placement status | **CONFLICTED / NEEDS VERIFICATION** |
| Artifact role | Released public-safe settlement layer bytes and sidecars |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/` and `data/receipts/`, not this directory |
| Default failure posture | `DENY`, `HOLD`, `RESTRICT`, or `ABSTAIN` when evidence, source role, sensitivity, sovereignty/cultural review, rights, release, or rollback support is insufficient |

---

## Inputs

Accepted content is limited to release-approved, public-safe derivatives such as:

- settlement, municipality, census-place, townsite, ghost-town, fort, mission, or reservation-community layer artifacts after review;
- generalized public-safe footprints, points, or boundary views whose precision is supported by evidence and release state;
- PMTiles, GeoParquet, GeoJSON, vector-tile artifacts, or API payload sidecars;
- layer manifests, caveat summaries, and tile metadata;
- field allowlists, digests, and generated release pointers;
- release-local notes that explain artifact contents without replacing proof or release authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| RAW source captures or source mirrors | `data/raw/settlements-infrastructure/` or source-specific intake |
| WORK files, candidates, unresolved joins, or review drafts | `data/work/settlements-infrastructure/` |
| Quarantined or unclear material | `data/quarantine/settlements-infrastructure/` |
| Canonical processed settlement or infrastructure objects | `data/processed/settlements-infrastructure/` or the ADR-confirmed lane |
| Catalog records, triplets, or graph truth | `data/catalog/` and triplet/projection lanes |
| EvidenceBundle / ProofPack | `data/proofs/` |
| Validation, transform, redaction, build, or release receipts | `data/receipts/` |
| Release manifests or promotion decisions | `release/` |
| Exact restricted cultural, sacred-site, living-person, parcel, or sensitive infrastructure detail | Restricted governed lanes only; not public published layers |
| Direct model-generated claims | Governed answer/provenance paths only |

---

## Directory map

```text
data/published/layers/settlement/
├── README.md
├── <release_id>/
│   ├── settlement.pmtiles
│   ├── settlement.geoparquet
│   ├── settlement.sha256
│   ├── layer.manifest.json
│   ├── fields.allowlist.json
│   ├── review.summary.json
│   └── README.md
└── latest.json
```

`latest.json` must be generated from release state. Remove or withhold it when release, review, digest, registry, correction, or rollback support is incomplete.

---

## Publication boundary

```mermaid
flowchart LR
    RAW["RAW<br/>source capture"] --> WORK["WORK<br/>normalize + candidate"]
    WORK --> GATE{Evidence + role + rights + sensitivity gate}
    GATE -->|fail / unclear| QUAR["QUARANTINE<br/>hold or deny"]
    GATE -->|pass| PROC["PROCESSED<br/>validated settlement objects"]
    PROC --> CAT["CATALOG / TRIPLET<br/>EvidenceBundle refs"]
    CAT --> REL["RELEASE<br/>manifest + rollback"]
    REL --> PUB["PUBLISHED<br/>settlement layer artifacts"]
    PUB --> API["governed API / layer resolver"]
    API --> UI["MapLibre + Evidence Drawer"]
```

The forbidden shortcut is:

```text
RAW / WORK / QUARANTINE / processed candidate / direct source record / direct model output
→ direct public settlement layer
```

---

## Required checks before use

- [ ] Resolve or explicitly document the `settlement/` versus `settlements-infrastructure/` path segment decision.
- [ ] Confirm the release manifest and promotion decision.
- [ ] Confirm proof and receipt closure.
- [ ] Confirm source descriptors, source roles, and rights posture.
- [ ] Confirm sensitivity, sovereignty/cultural-adjacency, and living-person/privacy review outcomes where applicable.
- [ ] Confirm field allowlist and released-byte digest.
- [ ] Confirm layer registry entry.
- [ ] Confirm rollback target and correction path.
- [ ] Confirm `latest.json`, if present, is generated from release state.
- [ ] Confirm public clients consume this layer through governed APIs or release-resolved artifacts.
- [ ] Confirm no restricted detail is exposed by relying on style-only hiding.

---

## Status notes

| Claim | Status |
|---|---|
| This README defines the requested path boundary. | **CONFIRMED authored** |
| The target path exists in the live repository. | **CONFIRMED by GitHub contents API during this edit** |
| Current domain docs record a slug/path conflict involving `settlement` and `settlements-infrastructure`. | **CONFIRMED by GitHub contents API during this edit** |
| This path is canonical. | **CONFLICTED / NEEDS VERIFICATION** |
| Actual released artifacts exist in this subtree. | **UNKNOWN** |
| Validators for this exact layer are implemented and wired in CI. | **NEEDS VERIFICATION** |
| A release manifest currently approves a settlement layer. | **UNKNOWN** |

---

## Related files

- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../../README.md`](../../../README.md)
- [`../../../../docs/domains/settlements-infrastructure/CANONICAL_PATHS.md`](../../../../docs/domains/settlements-infrastructure/CANONICAL_PATHS.md)
- [`../../../../docs/domains/settlements-infrastructure/DATA_LIFECYCLE.md`](../../../../docs/domains/settlements-infrastructure/DATA_LIFECYCLE.md)
- [`../../../../docs/domains/settlements-infrastructure/sublanes/settlements.md`](../../../../docs/domains/settlements-infrastructure/sublanes/settlements.md)
- [`../../../../docs/domains/settlements-infrastructure/RELEASE_INDEX.md`](../../../../docs/domains/settlements-infrastructure/RELEASE_INDEX.md)
- [`../../../proofs/README.md`](../../../proofs/README.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)

---

KFM rule: this directory is a released settlement layer lane only. It is not source authority, proof authority, release authority, catalog authority, settlement truth, cultural authority, registry authority, or AI truth.

[Back to top](#top)
