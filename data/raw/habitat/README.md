<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/habitat/readme
title: Habitat Raw README
path: data/raw/habitat/README.md
type: data-raw-domain-index-readme
version: v0.2.0
prior_version: v0.1.0
status: draft
owners:
  - <habitat-domain-steward>
  - <habitat-source-steward>
  - <data-steward>
  - <rights-reviewer>
  - <sensitivity-reviewer>
  - <release-steward>
created: 2026-06-27
updated: 2026-10-11
policy_label: restricted-review
truth_posture: cite-or-abstain
lifecycle_phase: raw
owning_root: data/
responsibility: Preserve the tracked Habitat RAW compatibility and reference index without treating this domain subtree or its source-named children as physical source-first capture homes or duplicating RAW bytes.
domain: habitat
artifact_family: habitat-raw-compatibility-reference-index
sensitivity_posture: raw-internal; source-role-preserving; no-public-path; sensitive-joins-fail-closed; rights-needs-verification; release-blocked
related:
  - ecoregions/README.md
  - gap-landfire/README.md
  - kdwp/README.md
  - natureserve/README.md
  - nlcd/README.md
  - nwi/README.md
  - occurrence-context/README.md
  - pad-us/README.md
  - usfws-ecos/README.md
  - ../README.md
  - ../../README.md
  - ../../quarantine/habitat/README.md
  - ../../processed/habitat/README.md
  - ../../catalog/domain/habitat/README.md
  - ../../published/layers/habitat/README.md
  - ../../registry/sources/README.md
  - ../../../docs/domains/habitat/SOURCE_REGISTRY.md
  - ../../../docs/domains/habitat/SOURCE_FAMILIES.md
  - ../../../docs/domains/habitat/SOURCES.md
  - ../../../docs/domains/habitat/SENSITIVITY.md
  - ../../../docs/domains/habitat/POLICY.md
  - ../../../docs/architecture/source-roles.md
  - ../../../release/manifests/README.md
tags:
  - kfm
  - data
  - raw
  - habitat
  - source-capture
  - source-role
  - source-family-index
  - geoprivacy
  - no-public-path
  - evidence-first
  - compatibility-reference
  - source-first
notes:
  - "This README replaces the greenfield stub at `data/raw/habitat/README.md`."
  - "Confirmed child README lanes during this edit: `ecoregions/`, `gap-landfire/`, `kdwp/`, `natureserve/`, `nlcd/`, `nwi/`, `occurrence-context/`, `pad-us/`, and `usfws-ecos/`."
  - "Accepted Directory Rules require one source-first capture identity; these domain-scoped documentation lanes do not authorize duplicated RAW bytes or establish physical capture placement."
  - "README presence confirms documentation lanes only; it does not prove payloads, SourceDescriptor records, connector activation, receipts, validators, fixtures, CI enforcement, review controls, or release readiness."
  - "Habitat-relevant RAW material remains at its governed source-first capture until governed downstream lifecycle transitions close; this subtree does not establish where that capture is stored."
  - "2026-10-11 reconciliation: aligned to accepted DIR-SOURCE-001 and the parent data/raw/README.md source-first contract; this lane is compatibility/reference documentation, not a physical capture home; metadata normalized to the required profile; no payload, path, writer, or release state changed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat RAW

Compatibility and reference index for legacy Habitat-scoped RAW documentation; not a physical source-capture home.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-blueviolet">
</p>

**Quick links:** [Scope](#scope) · [Repo fit](#repo-fit) · [Confirmed source-family lanes](#confirmed-source-family-lanes) · [RAW source posture](#raw-source-posture) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/raw/habitat/` is a no-public-path compatibility/reference index inside the RAW lifecycle boundary. Accepted Directory Rules require one source-first capture identity, so this domain subtree and its source-named children are not default physical capture homes and must not receive duplicate RAW payloads. It is not processed Habitat truth, catalog truth, proof, receipt authority, source registry authority, rights authority, policy authority, release authority, public API/UI material, public PMTiles material, or generated-answer authority.

---

## Scope

This directory indexes tracked Habitat-facing source documentation and legacy domain-scoped RAW topology. It may reference one governed source-first capture, but it does not establish where that capture is stored.

The canonical RAW boundary exists for preservation, replay, and audit. A governed source-first capture records what was admitted, where it came from, what source role it carried, and which identifiers, versions, times, rights notes, citations, geometry/support metadata, classification fields, hashes, review notes, and caveats must travel downstream.

RAW does not decide what a source means, whether rights permit reuse, whether a record can publish, whether a class crosswalk is final, whether a habitat association is true, whether a regulatory layer is equivalent to a model, or whether a downstream claim is release-ready.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/habitat/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw` |
| Domain lane | `habitat` |
| Artifact role | Compatibility/reference index for Habitat-facing source documentation and unresolved legacy RAW topology |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Upstream | References to an admitted source-first capture only; physical placement remains **NEEDS VERIFICATION** |
| Downstream | Governed Habitat WORK or QUARANTINE procedures consume references or approved handoffs, not assumed domain-local copies |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/`, not this directory |
| Receipt authority | `data/receipts/`, not this directory |
| Registry authority | `data/registry/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when source role, rights, source family, citation, geometry/support, classification, review state, validation, correction, rollback, or release support is insufficient |

---

## Confirmed source-family lanes

The child lanes below are README paths confirmed by current-session GitHub fetches. Treat them as compatibility/reference documentation or unresolved legacy topology, not source-first capture homes. This table confirms README presence only; it does **not** prove or authorize payloads, SourceDescriptors, connectors, validators, fixtures, receipts, CI checks, review controls, migration, or release readiness.

| Source-family lane | Status | Parent boundary |
|---|---|---|
| [`ecoregions/`](ecoregions/README.md) | **CONFIRMED README / COMPATIBILITY REFERENCE** | Landscape context fabric and administrative/context source documentation; not Habitat truth, a capture home, or public release authority. |
| [`gap-landfire/`](gap-landfire/README.md) | **CONFIRMED README / COMPATIBILITY REFERENCE** | GAP/LANDFIRE material treated conservatively as modeled Habitat source material unless SourceDescriptor splits a product role; not a capture home. |
| [`kdwp/`](kdwp/README.md) | **CONFIRMED README / COMPATIBILITY REFERENCE** | State review context; state designations and survey observations require separate source-role handling; not a capture home. |
| [`natureserve/`](natureserve/README.md) | **CONFIRMED README / COMPATIBILITY REFERENCE** | Ecological-system and conservation context; implementation wiring, capture placement, and payload presence remain unverified. |
| [`nlcd/`](nlcd/README.md) | **CONFIRMED README / COMPATIBILITY REFERENCE** | Multi-year remotely sensed land-cover source documentation; native classes and vintages must be preserved at the single source-first capture. |
| [`nwi/`](nwi/README.md) | **CONFIRMED README / COMPATIBILITY REFERENCE** | Federal wetlands inventory mapping source documentation; Cowardin classes and delta strategy must be preserved at the single source-first capture. |
| [`occurrence-context/`](occurrence-context/README.md) | **CONFIRMED README / COMPATIBILITY REFERENCE** | Occurrence records enter Habitat only as context; Fauna and Flora retain occurrence-truth ownership; not a second occurrence capture home. |
| [`pad-us/`](pad-us/README.md) | **CONFIRMED README / COMPATIBILITY REFERENCE** | PAD-US is administrative stewardship context source documentation, not a capture home or public artifact authority. |
| [`usfws-ecos/`](usfws-ecos/README.md) | **CONFIRMED README / COMPATIBILITY REFERENCE** | USFWS ECOS is regulatory/context source documentation; SourceDescriptor and source-catalog boundaries decide downstream use; not a capture home. |

Cross-domain overlaps: `natureserve/` and `usfws-ecos/` document the same upstream sources as [`../fauna/natureserve/`](../fauna/natureserve/README.md) and [`../fauna/usfws_ecos/`](../fauna/usfws_ecos/README.md), and `occurrence-context/` overlaps [`../fauna/gbif/`](../fauna/gbif/README.md) and [`../fauna/inaturalist/`](../fauna/inaturalist/README.md). Each upstream source keeps its own `source_id`; every lane that uses it must reference that source's single source-first capture, never two copies.

---

## RAW source posture

| Rule | Handling |
|---|---|
| Capture identity is source-first | Register one `source_id` and preserve one immutable capture identity; domain references may support Habitat without duplicating RAW bytes. |
| Physical placement is held | Do not infer `data/raw/habitat/` or a child directory as the capture home. Use only an accepted writer/path contract; none is established by this README. |
| RAW is immutable source capture | Payloads or payload references at the accepted source-first home must be hash-bound and should not be overwritten in place. |
| Source role is preserved | Observed, regulatory, modeled, aggregate, administrative, candidate, and synthetic roles must not be flattened. |
| Native classification remains visible | Cowardin, NLCD, GAP-status, ecological-system, land-cover, and provider classifications stay visible before crosswalk. |
| Crosswalks are advisory until proven | Habitat vocabulary, Fauna/Flora joins, stewardship classes, and model inputs require downstream proof/release closure. |
| Sensitive joins fail closed | Occurrence-linked habitat products and rare-element context need governed review, transform receipts where required, and release state before public use. |
| Watchers do not publish | Watchers may emit intake candidates; they do not admit, promote, publish, or answer public claims. |
| Public use requires governed release | Public layers, PMTiles, reports, stories, API payloads, graph edges, vector indexes, and generated answers cannot read RAW directly. |

---

## Accepted material

Accepted content is limited to documentation and governed references that do not duplicate source-first captures:

- the tracked README files listed below;
- links to canonical SourceDescriptor, admission-ticket, source-admission, rights, sensitivity, and connector authority;
- references to a governed source-first capture or quarantine handoff when an accepted contract defines their shape;
- migration or correction notes that label legacy topology without moving or copying payloads;
- an optional local documentation index only after its schema, producer, owner, and non-authoritative role are accepted; it must not become proof, catalog, receipt, registry, policy, release, public artifact, or answer authority.

The governed source-first capture (not this subtree) is what must carry source-reference manifests, raw payloads or payload references, SourceDescriptor or admission-ticket references, source identity, source family, source role, source time, retrieval time, product version/vintage, classification fields, geometry/support metadata, citation, attribution, rights posture, review notes, digest sidecars, source-head records, retrieval metadata, status metadata, row counts where applicable, and checksums.

Do not place raw payloads, copied source runs, source-head records, checksums, or other capture sidecars in this subtree merely because they support Habitat. Exact physical placement and legacy migration remain **HOLD**.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Domain-scoped copies of source captures or new source-run directories | One accepted source-first RAW home after a reviewed placement decision; exact path remains **NEEDS VERIFICATION** |
| Habitat domain doctrine | `docs/domains/habitat/` |
| Source-family doctrine | `docs/sources/catalog/` or `docs/domains/habitat/` |
| Connector code or connector decisions | `connectors/` |
| Authoritative SourceDescriptor records or activation decisions | `data/registry/sources/` |
| Rights, terms, review, sensitivity, geoprivacy, or release policy | `policy/` and governed review lanes |
| Quarantine holds and remediation notes | `data/quarantine/habitat/` |
| Normalized working material | `data/work/habitat/` |
| Validated Habitat objects | `data/processed/habitat/` |
| Catalog records, triplets, graph truth, or EvidenceBundle state | `data/catalog/`, `data/triplets/`, or proof lanes |
| EvidenceBundle / ProofPack | `data/proofs/` |
| Ingest, validation, review, source-role, geoprivacy, model, AI, or release receipts as authority | `data/receipts/` |
| Release manifests, correction records, rollback records, signatures | `release/` |
| Public layers, PMTiles, reports, stories, API payloads, downloads, or published artifacts | `data/published/` only after release gates close |
| Habitat suitability truth, occurrence truth, taxonomic truth, regulatory truth, stewardship truth, public artifact authority, or generated-answer authority | Owning governed downstream/policy/proof/release lanes, never this RAW directory alone |
| Contracts, schemas, validators, app/API/UI code | `contracts/`, `schemas/`, `tools/`, `apps/` |

---

## Directory map

```text
data/raw/habitat/
├── README.md
├── ecoregions/
│   └── README.md
├── gap-landfire/
│   └── README.md
├── kdwp/
│   └── README.md
├── natureserve/
│   └── README.md
├── nlcd/
│   └── README.md
├── nwi/
│   └── README.md
├── occurrence-context/
│   └── README.md
├── pad-us/
│   └── README.md
└── usfws-ecos/
    └── README.md
```

This is the confirmed documentation topology, not a storage specification. Do not add a future source directory, payload, or local index here until an accepted source-first placement or compatibility decision defines its role. Any local documentation index accepted later must not be a public index, catalog record, registry record, release manifest, graph source, layer pointer, search index, vector index, map source, public-output authority, or retrieval source for generated answers.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Remain at the source-first RAW home | Source was admitted and captured, but no downstream normalization decision has been made. This index may retain a governed reference only. |
| Quarantine | Source role, rights, source family, product/version identity, citation, geometry/support, classification, schema, source activation, or physical placement is unresolved. |
| Return / reject | Admission decision or steward review says the capture must not be retained; correction occurs through the owning source-first or quarantine procedure. |
| Move to work | A governed reference or approved handoff may enter Habitat WORK only when SourceDescriptor, rights posture, source role, source-family/product identity, citation, hash, and minimal validation support are sufficient for normalization. |
| Promote downstream | Only after later WORK/PROCESSED/CATALOG/RELEASE gates close with receipts, EvidenceBundle support, review/generalization/model/geoprivacy receipts where required, correction path, rollback target, and release manifest where applicable. |

---

## Forbidden shortcut

```text
source-first RAW capture (physical path NEEDS VERIFICATION)
→ data/processed/habitat/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm one registered `source_id` and one immutable source-first capture identity; do not create a second Habitat-scoped copy.
- [ ] Treat this README and any source-named child README as compatibility/reference documentation only; do not create a child directory as a payload destination.
- [ ] Confirm SourceDescriptor or admission ticket records source ID, source role, product identity, rights, cadence, citation, review posture, and hash posture.
- [ ] Confirm source roles are not collapsed across observed, regulatory, modeled, aggregate, administrative, candidate, or synthetic products.
- [ ] Confirm native classification fields are preserved before advisory crosswalks.
- [ ] Confirm occurrence-context joins preserve Fauna/Flora ownership where applicable.
- [ ] Confirm model outputs are not framed as regulatory determinations.
- [ ] Confirm regulatory/context sources are not framed as observations or models.
- [ ] Confirm rights, current terms, citation, and allowed reuse have been reviewed or explicitly marked `NEEDS VERIFICATION`.
- [ ] Confirm raw payloads are immutable or hash-bound and do not overwrite prior captures in place.
- [ ] Confirm required downstream receipts are present or explicitly marked missing before anything leaves RAW.
- [ ] Confirm no public artifact, graph edge, search index, vector index, or generated answer uses RAW material directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces the greenfield stub at `data/raw/habitat/README.md`. | **CONFIRMED authored** |
| The target path existed in the live repository as a greenfield stub before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Child README lanes confirmed during this edit: ecoregions, gap-landfire, kdwp, natureserve, nlcd, nwi, occurrence-context, pad-us, and usfws-ecos. | **CONFIRMED by GitHub contents API during this edit** |
| Child README presence proves payloads, SourceDescriptors, connectors, validators, fixtures, CI checks, receipts, review controls, or release readiness. | **DENY** |
| Habitat source-registry doctrine lists Habitat source families and marks activation as proposed, with rights/current terms needing verification and sensitive joins failing closed. | **CONFIRMED by GitHub contents API during this edit** |
| Accepted Directory Rules require one source-first capture identity and prohibit duplicated RAW bytes across domains. | **CONFIRMED** (`DIR-SOURCE-001`) |
| This subtree is an accepted physical source-first capture home. | **DENY — no placement decision found as of 2026-10-11** |
| Actual Habitat RAW payloads exist under this subtree. | **UNKNOWN; none added or moved by this documentation correction.** No payload files are tracked under this subtree at `main@9e8bf3e6`; external or untracked stores remain UNKNOWN |
| `natureserve/`, `usfws-ecos/`, and `occurrence-context/` overlap Fauna source-named lanes for the same upstream sources. | **CONFIRMED README presence; each upstream source keeps its own `source_id`, and both sides must reference that source's single source-first capture, never two copies** |
| This README and its nine child READMEs are reconciled to the parent source-first contract. | **CONFIRMED authored 2026-10-11** |
| SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, review controls, and downstream receipts are wired to an accepted source-first RAW writer for Habitat-relevant sources. | **NEEDS VERIFICATION** |
| This README is proof, receipt, release, catalog, registry, policy, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`ecoregions/README.md`](ecoregions/README.md)
- [`gap-landfire/README.md`](gap-landfire/README.md)
- [`kdwp/README.md`](kdwp/README.md)
- [`natureserve/README.md`](natureserve/README.md)
- [`nlcd/README.md`](nlcd/README.md)
- [`nwi/README.md`](nwi/README.md)
- [`occurrence-context/README.md`](occurrence-context/README.md)
- [`pad-us/README.md`](pad-us/README.md)
- [`usfws-ecos/README.md`](usfws-ecos/README.md)
- [`../README.md`](../README.md)
- [`../fauna/natureserve/README.md`](../fauna/natureserve/README.md)
- [`../fauna/usfws_ecos/README.md`](../fauna/usfws_ecos/README.md)
- [`../fauna/gbif/README.md`](../fauna/gbif/README.md)
- [`../fauna/inaturalist/README.md`](../fauna/inaturalist/README.md)
- [`../../README.md`](../../README.md)
- [`../../quarantine/habitat/README.md`](../../quarantine/habitat/README.md)
- [`../../processed/habitat/README.md`](../../processed/habitat/README.md)
- [`../../catalog/domain/habitat/README.md`](../../catalog/domain/habitat/README.md)
- [`../../published/layers/habitat/README.md`](../../published/layers/habitat/README.md)
- [`../../registry/sources/README.md`](../../registry/sources/README.md)
- [`../../../docs/domains/habitat/SOURCE_REGISTRY.md`](../../../docs/domains/habitat/SOURCE_REGISTRY.md)
- [`../../../docs/domains/habitat/SOURCE_FAMILIES.md`](../../../docs/domains/habitat/SOURCE_FAMILIES.md)
- [`../../../docs/domains/habitat/SOURCES.md`](../../../docs/domains/habitat/SOURCES.md)
- [`../../../docs/domains/habitat/SENSITIVITY.md`](../../../docs/domains/habitat/SENSITIVITY.md)
- `../../../docs/domains/habitat/POLICY.md` (not present)
- [`../../../docs/architecture/source-roles.md`](../../../docs/architecture/source-roles.md)
- [`../../../release/manifests/README.md`](../../../release/manifests/README.md)

---

KFM rule: this directory is a Habitat-facing compatibility/reference index. One governed source-first capture may support Habitat without duplicated RAW bytes; this subtree does not establish physical placement. It is not source-family doctrine, registry authority, rights authority, policy authority, proof authority, receipt authority, release authority, catalog authority, Habitat suitability truth, occurrence truth, regulatory truth, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
