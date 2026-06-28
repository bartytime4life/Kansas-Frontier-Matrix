<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/habitat/readme
name: Habitat Raw README
path: data/raw/habitat/README.md
type: data-raw-domain-index-readme
version: v0.1.0
status: draft
owners:
  - <habitat-domain-steward>
  - <habitat-source-steward>
  - <data-steward>
  - <rights-reviewer>
  - <sensitivity-reviewer>
  - <release-steward>
created: 2026-06-27
updated: 2026-06-27
policy_label: restricted-review
truth_posture: cite-or-abstain
lifecycle_phase: raw
responsibility_root: data/
domain: habitat
artifact_family: immutable-habitat-source-capture
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
notes:
  - "This README replaces the greenfield stub at `data/raw/habitat/README.md`."
  - "Confirmed child README lanes during this edit: `ecoregions/`, `gap-landfire/`, `kdwp/`, `natureserve/`, `nlcd/`, `nwi/`, `occurrence-context/`, `pad-us/`, and `usfws-ecos/`."
  - "README presence confirms documentation lanes only; it does not prove payloads, SourceDescriptor records, connector activation, receipts, validators, fixtures, CI enforcement, review controls, or release readiness."
  - "Habitat RAW records remain source captures until governed downstream lifecycle transitions close."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat RAW

Parent RAW lifecycle index for immutable Habitat source captures and source-admission sidecars.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-blueviolet">
</p>

**Quick links:** [Scope](#scope) · [Repo fit](#repo-fit) · [Confirmed source-family lanes](#confirmed-source-family-lanes) · [RAW source posture](#raw-source-posture) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/raw/habitat/` is a no-public-path RAW lifecycle lane. It is not processed Habitat truth, catalog truth, proof, receipt authority, source registry authority, rights authority, policy authority, release authority, public API/UI material, public PMTiles material, or generated-answer authority.

---

## Scope

This directory indexes immutable RAW source captures and source-admission sidecars for the Habitat domain.

RAW exists for preservation, replay, and audit. It records what was admitted, where it came from, what source role it carried, and which identifiers, versions, times, rights notes, citations, geometry/support metadata, classification fields, hashes, review notes, and caveats must travel downstream.

RAW does not decide what a source means, whether rights permit reuse, whether a record can publish, whether a class crosswalk is final, whether a habitat association is true, whether a regulatory layer is equivalent to a model, or whether a downstream claim is release-ready.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/habitat/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw` |
| Domain lane | `habitat` |
| Artifact role | Parent RAW domain index for Habitat source captures and RAW-local sidecars |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Upstream | Accepted connector/source-admission output only |
| Downstream | `data/work/habitat/` or `data/quarantine/habitat/` after governed admission/triage |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/`, not this directory |
| Receipt authority | `data/receipts/`, not this directory |
| Registry authority | `data/registry/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when source role, rights, source family, citation, geometry/support, classification, review state, validation, correction, rollback, or release support is insufficient |

---

## Confirmed source-family lanes

The child lanes below are README paths confirmed by current-session GitHub fetches. This table confirms README presence only; it does **not** prove payloads, SourceDescriptors, connectors, validators, fixtures, receipts, CI checks, review controls, or release readiness.

| Source-family lane | Status | Parent boundary |
|---|---|---|
| [`ecoregions/`](ecoregions/README.md) | **CONFIRMED README** | Landscape context fabric and administrative/context source capture; not Habitat truth or public release authority. |
| [`gap-landfire/`](gap-landfire/README.md) | **CONFIRMED README** | GAP/LANDFIRE material treated conservatively as modeled Habitat source capture unless SourceDescriptor splits a product role. |
| [`kdwp/`](kdwp/README.md) | **CONFIRMED README** | State review context; state designations and survey observations require separate source-role handling. |
| [`natureserve/`](natureserve/README.md) | **CONFIRMED README** | Ecological-system and conservation context; implementation wiring and payload presence remain unverified. |
| [`nlcd/`](nlcd/README.md) | **CONFIRMED README** | Multi-year remotely sensed land-cover source capture; native classes and vintages must be preserved. |
| [`nwi/`](nwi/README.md) | **CONFIRMED README** | Federal wetlands inventory mapping source capture; Cowardin classes and delta strategy must be preserved. |
| [`occurrence-context/`](occurrence-context/README.md) | **CONFIRMED README** | Occurrence records enter Habitat only as context; Fauna and Flora retain occurrence-truth ownership. |
| [`pad-us/`](pad-us/README.md) | **CONFIRMED README** | PAD-US is administrative stewardship context source capture, not public artifact authority. |
| [`usfws-ecos/`](usfws-ecos/README.md) | **CONFIRMED README** | USFWS ECOS is regulatory/context source capture; SourceDescriptor and source-catalog boundaries decide downstream use. |

---

## RAW source posture

| Rule | Handling |
|---|---|
| RAW is immutable source capture | Payloads or payload references must be hash-bound and should not be overwritten in place. |
| Source role is preserved | Observed, regulatory, modeled, aggregate, administrative, candidate, and synthetic roles must not be flattened. |
| Native classification remains visible | Cowardin, NLCD, GAP-status, ecological-system, land-cover, and provider classifications stay visible before crosswalk. |
| Crosswalks are advisory until proven | Habitat vocabulary, Fauna/Flora joins, stewardship classes, and model inputs require downstream proof/release closure. |
| Sensitive joins fail closed | Occurrence-linked habitat products and rare-element context need governed review, transform receipts where required, and release state before public use. |
| Watchers do not publish | Watchers may emit intake candidates; they do not admit, promote, publish, or answer public claims. |
| Public use requires governed release | Public layers, PMTiles, reports, stories, API payloads, graph edges, vector indexes, and generated answers cannot read RAW directly. |

---

## Accepted material

Accepted content is limited to source-capture material and RAW-local sidecars:

- source-reference manifests;
- raw payloads or raw payload references;
- SourceDescriptor references or admission-ticket references;
- source identity, source family, source role, source time, retrieval time, product version/vintage, classification fields, geometry/support metadata, citation, attribution, rights posture, review notes, and digest sidecars;
- source-head records, retrieval metadata, status metadata, row counts where applicable, and checksums;
- local README or index sidecars that help a steward understand capture state without becoming proof, catalog, receipt, registry, policy, release, public artifact, or answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
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
├── usfws-ecos/
│   └── README.md
├── <future-source-family>/
│   └── README.md
└── index.local.json
```

`index.local.json` is optional and must remain RAW-local. It is not a public index, catalog record, registry record, release manifest, graph source, layer pointer, search index, vector index, map source, public-output authority, or retrieval source for generated answers.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay RAW | Source was admitted and captured, but no downstream normalization decision has been made. |
| Quarantine | Source role, rights, source family, product/version identity, citation, geometry/support, classification, schema, or source activation is unresolved. |
| Return / reject | Admission decision or steward review says the source should not be retained in this RAW lane. |
| Move to work | SourceDescriptor, rights posture, source role, source-family/product identity, citation, hash, and minimal validation support are sufficient for normalization. |
| Promote downstream | Only after later WORK/PROCESSED/CATALOG/RELEASE gates close with receipts, EvidenceBundle support, review/generalization/model/geoprivacy receipts where required, correction path, rollback target, and release manifest where applicable. |

---

## Forbidden shortcut

```text
data/raw/habitat/
→ data/processed/habitat/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm the source belongs to the Habitat lane and a documented source-family subfolder.
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
| Actual Habitat RAW payloads exist under this subtree. | **UNKNOWN** |
| SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, review controls, and downstream receipts are wired for this exact parent lane. | **NEEDS VERIFICATION** |
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
- [`../../../docs/domains/habitat/POLICY.md`](../../../docs/domains/habitat/POLICY.md)
- [`../../../docs/architecture/source-roles.md`](../../../docs/architecture/source-roles.md)
- [`../../../release/manifests/README.md`](../../../release/manifests/README.md)

---

KFM rule: this directory is a Habitat RAW domain index for source capture only. It is not source-family doctrine, registry authority, rights authority, policy authority, proof authority, receipt authority, release authority, catalog authority, Habitat suitability truth, occurrence truth, regulatory truth, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
