<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/fauna/usfws-ecos/readme
name: USFWS ECOS Raw Fauna README
path: data/raw/fauna/usfws_ecos/README.md
type: data-raw-source-family-lane-readme
version: v0.1.0
status: draft
owners:
  - <fauna-domain-steward>
  - <habitat-domain-steward>
  - <fauna-source-steward>
  - <usfws-ecos-source-steward>
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
domain: fauna
adjacent_domain: habitat
source_family: usfws_ecos
source_role: regulatory-authority-plus-administrative-context
artifact_family: immutable-usfws-ecos-source-capture
sensitivity_posture: raw-internal; source-role-preserving; no-public-path; federal-register-reality-boundary; sensitive-joins-fail-closed; ipac-project-review-required; release-blocked
related:
  - ../README.md
  - ../../README.md
  - ../../../README.md
  - ../../../quarantine/fauna/README.md
  - ../../../processed/fauna/README.md
  - ../../../catalog/domain/fauna/README.md
  - ../../../published/layers/fauna/README.md
  - ../../../registry/sources/README.md
  - ../../../../docs/sources/catalog/usfws_ecos/README.md
  - ../../../../docs/sources/catalog/usfws_ecos/species-profiles.md
  - ../../../../docs/sources/catalog/usfws_ecos/esa-listing-status.md
  - ../../../../docs/sources/catalog/usfws_ecos/critical-habitat.md
  - ../../../../docs/sources/catalog/usfws_ecos/ipac-project-lists.md
  - ../../../../docs/domains/fauna/SOURCE_REGISTRY.md
  - ../../../../docs/domains/fauna/DATA_LIFECYCLE.md
  - ../../../../docs/domains/fauna/POLICY.md
  - ../../../../docs/domains/fauna/CANONICAL_PATHS.md
  - ../../../../docs/architecture/source-roles.md
  - ../../../../release/manifests/README.md
tags:
  - kfm
  - data
  - raw
  - fauna
  - habitat-adjacent
  - usfws
  - ecos
  - esa
  - regulatory
  - authority-source
  - critical-habitat
  - conservation-status
  - federal-register
  - sensitive-join
  - no-public-path
  - evidence-first
notes:
  - "This README documents the requested USFWS ECOS Fauna RAW source-family lane."
  - "The target file existed as an empty file before this edit."
  - "Parent `data/raw/fauna/README.md` is currently a greenfield stub, so this child file stays source-family-lane bounded."
  - "USFWS ECOS is treated as a federal regulatory/authority carrier for status and critical-habitat source material, with ECOS species profiles as administrative context; the Federal Register remains the legal/reality boundary for listed status and designated critical habitat."
  - "Payload presence, SourceDescriptor records, connector activation, receipts, validators, fixtures, CI enforcement, sensitive-join controls, IPaC credential handling, review completion, and release readiness remain UNKNOWN or NEEDS VERIFICATION unless separately verified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# USFWS ECOS RAW Fauna Lane

RAW source-family lane for immutable USFWS ECOS source captures and source-admission sidecars in the Fauna domain, with Habitat adjacency for critical-habitat surfaces.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: fauna" src="https://img.shields.io/badge/domain-fauna-2e8b57">
  <img alt="Adjacent: habitat" src="https://img.shields.io/badge/adjacent-habitat-6f42c1">
  <img alt="Source family: USFWS ECOS" src="https://img.shields.io/badge/source-USFWS%20ECOS-1f6feb">
  <img alt="Role: regulatory authority" src="https://img.shields.io/badge/role-regulatory%20authority-7048e8">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-blueviolet">
</p>

**Quick links:** [Scope](#scope) · [Repo fit](#repo-fit) · [USFWS ECOS source posture](#usfws-ecos-source-posture) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/raw/fauna/usfws_ecos/` is a no-public-path RAW source-family lane. It is not processed Fauna truth, catalog truth, proof, receipt authority, source registry authority, rights authority, sensitivity policy authority, release authority, occurrence evidence, public API/UI material, or generated-answer authority. Public clients and normal UI surfaces must not read this lane directly.

---

## Scope

This directory holds immutable RAW captures and source-admission sidecars for USFWS ECOS material admitted to the Fauna lane.

KFM treats USFWS ECOS as a federal regulatory and authority carrier for ESA listing/status, critical-habitat, IPaC project-list, and species-profile source material. The Federal Register rule remains the legal/reality boundary for listed status and designated critical habitat; ECOS carries and exposes source material for governed KFM use.

RAW exists for preservation, replay, and audit. It records what was admitted, where it came from, which ECOS surface or product was used, what source role it carried, and which identifiers, times, rights, citations, rule references, geometry/support notes, sensitivity labels, hashes, and caveats must travel with it.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/fauna/usfws_ecos/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw/` |
| Domain lane | `fauna` |
| Adjacent domain | `habitat` for critical-habitat surfaces and habitat joins |
| Source family | `usfws_ecos` |
| Source role | `regulatory` for ESA listing/status, critical habitat, and IPaC; `administrative` for species-profile narrative/reference graph |
| Artifact role | RAW source-family lane for USFWS ECOS captures and RAW-local sidecars |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Upstream | Accepted connector/source-admission output only |
| Downstream | `data/work/fauna/`, `data/work/habitat/`, or `data/quarantine/fauna/` after governed admission/triage |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/`, not this directory |
| Receipt authority | `data/receipts/`, not this directory |
| Registry authority | `data/registry/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when source role, Federal Register reference, API/product identity, IPaC credential posture, rights/citation, sensitive-join risk, geometry support, validation, correction, rollback, or release support is insufficient |

---

## USFWS ECOS source posture

| ECOS surface | RAW handling | Boundary |
|---|---|---|
| ESA listing/status records | Capture as `regulatory` source material when admitted. | Status text is not occurrence evidence and does not prove where an animal was observed. |
| Final/proposed critical habitat | Capture as regulatory geometry/source support, usually Habitat-adjacent. | KFM-derived geometry requires generalization/sensitivity labels before publication; sensitive joins fail closed. |
| IPaC project species list | Capture only when source activation, credential, project-scope, and policy posture are documented. | Project-scoped lists may be sensitive and require policy review before any public use. |
| Species profile narrative/reference graph | Capture as `administrative` context. | Profile narrative explains and links; it is not the legal determination itself. |
| Direct ECOS URL reference | Preserve as source reference and citation. | Link-only references do not authorize KFM republication or derivative public layers. |

---

## Accepted material

Accepted content is limited to source-capture material and RAW-local sidecars:

- source-reference manifests;
- ECOS listing/status response references, critical-habitat service references, IPaC list references, species-profile narrative/reference-graph references, or restricted raw payload references;
- Federal Register citation references, ECOS species identifiers, entity identifiers, request parameters, service URLs, issue/retrieval times, status/proposal/final flags, geometry/support notes, no-warranty/disclaimer notes, citation, attribution, rights posture, sensitivity hints, and digest sidecars;
- source-head records, retrieval metadata, status metadata, row counts where applicable, job/status records where applicable, and checksums;
- local README or index sidecars that help a steward understand capture state without becoming proof, catalog, receipt, registry, policy, release, public artifact, or answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| USFWS ECOS source/product doctrine | `docs/sources/catalog/usfws_ecos/` |
| Fauna or Habitat domain doctrine | `docs/domains/fauna/`, `docs/domains/habitat/` |
| Connector code or connector decisions | `connectors/usfws_ecos/` or accepted connector home if/when present |
| Authoritative SourceDescriptor records or activation decisions | `data/registry/sources/` |
| Rights, terms, sensitivity, geoprivacy, sensitive-join, redaction, or release policy | `policy/` and governed review lanes |
| Quarantine holds and remediation notes | `data/quarantine/fauna/` |
| Normalized working material | `data/work/fauna/` or `data/work/habitat/` |
| Validated Fauna/Habitat objects | `data/processed/fauna/` or `data/processed/habitat/` |
| Catalog records, triplets, graph truth, or EvidenceBundle state | `data/catalog/`, `data/triplets/`, or proof lanes |
| EvidenceBundle / ProofPack | `data/proofs/` |
| Ingest, validation, redaction, aggregation, source-role, AI, or release receipts as authority | `data/receipts/` |
| Release manifests, correction records, rollback records, signatures | `release/` |
| Public layers, PMTiles, reports, stories, API payloads, downloads, or published artifacts | `data/published/` only after release gates close |
| Observed occurrence evidence, state heritage rank authority, NatureServe sensitivity authority, KDWP state-status authority, or public answer authority | Owning governed downstream/policy/proof lanes, never this RAW directory alone |
| Contracts, schemas, validators, app/API/UI code | `contracts/`, `schemas/`, `tools/`, `apps/` |

---

## Directory map

```text
data/raw/fauna/usfws_ecos/
├── README.md
├── esa-listing-status/
│   └── <run_id>/
│       ├── source_reference.json
│       ├── request_parameters.json
│       ├── listing_status_ref.json
│       ├── federal_register_ref.json
│       ├── checksums.sha256
│       └── README.md
├── critical-habitat/
│   └── <run_id>/
│       ├── source_reference.json
│       ├── service_ref.json
│       ├── geometry_support_ref.json
│       ├── sensitivity_review_ref.json
│       ├── checksums.sha256
│       └── README.md
├── ipac-project-lists/
│   └── <run_id>/
│       ├── source_reference.json
│       ├── project_scope_ref.json
│       ├── list_ref.json
│       ├── policy_review_ref.json
│       ├── checksums.sha256
│       └── README.md
├── species-profiles/
│   └── <run_id>/
│       ├── source_reference.json
│       ├── narrative_ref.json
│       ├── reference_graph_ref.json
│       ├── checksums.sha256
│       └── README.md
└── index.local.json
```

`index.local.json` is optional and must remain RAW-local. It is not a public index, catalog record, registry record, release manifest, graph source, layer pointer, search index, vector index, map source, legal authority, occurrence authority, rights authority, sensitive-join authority, public-output authority, or retrieval source for generated answers.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay RAW | Source was admitted and captured, but no downstream normalization decision has been made. |
| Quarantine | Source role, Federal Register reference, product identity, rights/citation, project-scope sensitivity, sensitive-join risk, geometry support, attribution, digest, schema, or source activation is unresolved. |
| Return / reject | Admission decision or steward review says the source should not be retained in this RAW lane. |
| Move to work | SourceDescriptor, rights/citation posture, source role, product/surface identity, Federal Register reference where needed, hash, and minimal validation support are sufficient for normalization. |
| Promote downstream | Only after later WORK/PROCESSED/CATALOG/RELEASE gates close with receipts, EvidenceBundle support, redaction/generalization receipts where required, correction path, rollback target, and release manifest where applicable. |

---

## Forbidden shortcut

```text
data/raw/fauna/usfws_ecos/
→ data/processed/fauna/ or data/processed/habitat/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm the source belongs to the Fauna lane and the USFWS ECOS source family, with Habitat adjacency recorded where critical-habitat material is involved.
- [ ] Confirm whether the captured material is ESA listing/status, critical-habitat geometry/service support, IPaC project-list support, species-profile narrative/reference graph, or a mixed package.
- [ ] Confirm a SourceDescriptor or admission ticket identifies source ID, source role, product/surface identity, Federal Register reference where required, rights/citation posture, sensitive-join posture, and hash posture.
- [ ] Confirm ECOS regulatory material is not being cited as observed occurrence evidence.
- [ ] Confirm species-profile narrative is not being treated as the legal determination itself.
- [ ] Confirm KFM-derived critical-habitat geometry is not published without generalization/sensitivity labels, receipts, review state, and release state.
- [ ] Confirm IPaC project-scoped material has credential, project-scope, privacy/sensitivity, and policy posture recorded before any downstream use.
- [ ] Confirm rights, current terms, citation, no-warranty/disclaimer handling, and allowed reuse have been reviewed or explicitly marked `NEEDS VERIFICATION`.
- [ ] Confirm raw payloads are immutable or hash-bound and do not overwrite prior runs in place.
- [ ] Confirm required downstream receipts are present or explicitly marked missing before anything leaves RAW.
- [ ] Confirm no public artifact, graph edge, search index, vector index, or generated answer uses RAW material directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README defines the requested USFWS ECOS Fauna RAW source-family lane boundary. | **CONFIRMED authored** |
| The target path existed in the live repository as an empty file before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Parent `data/raw/fauna/README.md` is currently a greenfield stub. | **CONFIRMED by GitHub contents API during this edit** |
| USFWS ECOS source docs identify ECOS as a regulatory/authority carrier for ESA listing/status, critical habitat, and IPaC project-list support. | **CONFIRMED by GitHub contents API during this edit** |
| USFWS ECOS source docs say the Federal Register rule is the legal source and ECOS is the carrier. | **CONFIRMED by GitHub contents API during this edit** |
| USFWS ECOS source docs say source role is regulatory for listing/status/critical habitat/IPaC and administrative for species-profile narrative/reference graph. | **CONFIRMED by GitHub contents API during this edit** |
| Fauna lifecycle doctrine says RAW captures immutable source payload/reference with source role, rights, sensitivity, citation, time, and content hash, with no public access. | **CONFIRMED by GitHub contents API during this edit** |
| Actual USFWS ECOS RAW payloads exist under this subtree. | **UNKNOWN** |
| SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, sensitive-join controls, IPaC credential handling, and downstream receipts are wired for this exact lane. | **NEEDS VERIFICATION** |
| This README is proof, receipt, release, catalog, registry, policy, observed occurrence evidence, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../../README.md`](../../../README.md)
- [`../../../quarantine/fauna/README.md`](../../../quarantine/fauna/README.md)
- [`../../../processed/fauna/README.md`](../../../processed/fauna/README.md)
- [`../../../catalog/domain/fauna/README.md`](../../../catalog/domain/fauna/README.md)
- [`../../../published/layers/fauna/README.md`](../../../published/layers/fauna/README.md)
- [`../../../registry/sources/README.md`](../../../registry/sources/README.md)
- [`../../../../docs/sources/catalog/usfws_ecos/README.md`](../../../../docs/sources/catalog/usfws_ecos/README.md)
- [`../../../../docs/sources/catalog/usfws_ecos/species-profiles.md`](../../../../docs/sources/catalog/usfws_ecos/species-profiles.md)
- [`../../../../docs/sources/catalog/usfws_ecos/esa-listing-status.md`](../../../../docs/sources/catalog/usfws_ecos/esa-listing-status.md)
- [`../../../../docs/sources/catalog/usfws_ecos/critical-habitat.md`](../../../../docs/sources/catalog/usfws_ecos/critical-habitat.md)
- [`../../../../docs/sources/catalog/usfws_ecos/ipac-project-lists.md`](../../../../docs/sources/catalog/usfws_ecos/ipac-project-lists.md)
- [`../../../../docs/domains/fauna/SOURCE_REGISTRY.md`](../../../../docs/domains/fauna/SOURCE_REGISTRY.md)
- [`../../../../docs/domains/fauna/DATA_LIFECYCLE.md`](../../../../docs/domains/fauna/DATA_LIFECYCLE.md)
- [`../../../../docs/domains/fauna/POLICY.md`](../../../../docs/domains/fauna/POLICY.md)
- [`../../../../docs/domains/fauna/CANONICAL_PATHS.md`](../../../../docs/domains/fauna/CANONICAL_PATHS.md)
- [`../../../../docs/architecture/source-roles.md`](../../../../docs/architecture/source-roles.md)
- [`../../../../release/manifests/README.md`](../../../../release/manifests/README.md)

---

KFM rule: this directory is a USFWS ECOS Fauna RAW source-family lane for source capture only. It is not source-family doctrine, source registry authority, rights authority, sensitivity policy authority, proof authority, receipt authority, release authority, catalog authority, observed occurrence evidence, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
