<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/settlements-infrastructure/readme
name: Settlements Infrastructure Raw README
path: data/raw/settlements-infrastructure/README.md
type: data-raw-domain-index-readme
version: v0.1.0
status: draft
owners:
  - <settlements-infrastructure-domain-steward>
  - <settlements-source-steward>
  - <infrastructure-source-steward>
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
domain: settlements-infrastructure
artifact_family: immutable-settlements-infrastructure-source-capture-index
sensitivity_posture: raw-internal; source-role-preserving; no-public-path; critical-asset-detail-fail-closed; cultural-sovereignty-review-where-applicable; rights-needs-verification; release-blocked
related:
  - ../README.md
  - ../../README.md
  - ../../raw/settlement/README.md
  - ../../quarantine/settlements-infrastructure/README.md
  - ../../quarantine/settlement/README.md
  - ../../processed/settlements-infrastructure/README.md
  - ../../processed/settlement/README.md
  - ../../catalog/domain/settlements-infrastructure/README.md
  - ../../published/layers/settlements-infrastructure/README.md
  - ../../published/layers/settlements/README.md
  - ../../registry/sources/README.md
  - ../../../docs/domains/settlements-infrastructure/README.md
  - ../../../docs/domains/settlements-infrastructure/CANONICAL_PATHS.md
  - ../../../docs/domains/settlements-infrastructure/sublanes/settlements.md
  - ../../../docs/domains/settlements-infrastructure/sublanes/infrastructure.md
  - ../../../docs/sources/catalog/census/tiger-line.md
  - ../../../docs/sources/catalog/usgs/gnis-names.md
  - ../../../docs/architecture/source-roles.md
  - ../../../release/manifests/README.md
tags:
  - kfm
  - data
  - raw
  - settlements-infrastructure
  - settlements
  - infrastructure
  - municipality
  - census-place
  - townsite
  - ghost-town
  - fort
  - mission
  - reservation-community
  - facility
  - service-area
  - operator
  - condition-observation
  - source-capture
  - source-role
  - no-public-path
  - evidence-first
notes:
  - "This README replaces the greenfield stub at `data/raw/settlements-infrastructure/README.md`."
  - "The canonical data RAW lane is documented as `data/raw/settlements-infrastructure/`."
  - "The singular `data/raw/settlement/README.md` file exists as compatibility context, not as the canonical parent lane."
  - "No child RAW README lanes under `data/raw/settlements-infrastructure/` were confirmed during this edit."
  - "README presence confirms documentation only; it does not prove payloads, SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, review controls, or release readiness."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Settlements / Infrastructure RAW

Parent RAW lifecycle index for immutable Settlements/Infrastructure source captures and source-admission sidecars.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: settlements-infrastructure" src="https://img.shields.io/badge/domain-settlements--infrastructure-7048e8">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-blueviolet">
</p>

**Quick links:** [Scope](#scope) · [Repo fit](#repo-fit) · [Domain halves](#domain-halves) · [Source-family posture](#source-family-posture) · [RAW source posture](#raw-source-posture) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/raw/settlements-infrastructure/` is a no-public-path RAW lifecycle lane. It is not processed Settlements/Infrastructure truth, catalog truth, proof, receipt authority, source registry authority, rights authority, policy authority, release authority, public API/UI material, public PMTiles material, critical-asset detail authority, place-status authority, or generated-answer authority.

---

## Scope

This directory indexes immutable RAW source captures and RAW-local sidecars for the Settlements/Infrastructure domain.

RAW exists for preservation, replay, and audit. It records what was admitted, where it came from, what source role it carried, and which identifiers, versions, vintages, source times, retrieval times, rights notes, citations, geometry/support metadata, source-head metadata, hashes, sensitivity notes, review notes, and caveats must travel downstream.

RAW does not decide whether a settlement, municipality, census place, historic townsite, facility, service area, operator, condition observation, dependency, boundary, status event, asset relation, map layer, public claim, or generated answer is true or release-ready.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/settlements-infrastructure/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw` |
| Domain lane | `settlements-infrastructure` |
| Artifact role | Parent RAW domain index for source captures and RAW-local sidecars |
| Related compatibility path | `data/raw/settlement/` |
| Confirmed child README lanes | None confirmed during this edit |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Upstream | Explicitly admitted connector/source-admission output only |
| Downstream | `data/work/settlements-infrastructure/` or `data/quarantine/settlements-infrastructure/` after governed triage |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/`, not this directory |
| Receipt authority | `data/receipts/`, not this directory |
| Registry authority | `data/registry/sources/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when source role, rights, source family, path authority, citation, geometry/support, sensitivity, validation, correction, rollback, or release support is insufficient |

---

## Domain halves

The domain owns both settlement/place identity and infrastructure-side object families. This parent RAW index does not create two domains; it preserves source-role and sensitivity boundaries inside one domain lane.

| Group | Object families | RAW boundary |
|---|---|---|
| Settlement / place identity | `Settlement`, `Municipality`, `CensusPlace`, `Townsite`, `GhostTown`, `Fort`, `Mission`, `ReservationCommunity` | Place evidence is source-roled and time-scoped. Census, legal, historic, and sovereignty-governed identities are not collapsed. |
| Infrastructure-side families | `InfrastructureAsset`, `NetworkNode`, `NetworkSegment`, `Facility`, `ServiceArea`, `Operator`, `ConditionObservation`, `Dependency` | Asset, operator, condition, service-area, and dependency evidence stays behind sensitivity, review, proof, and release gates. |

---

## Source-family posture

The domain docs identify source families that may feed this RAW lane after governed admission. This README does not prove that any payloads or source-family folders exist.

| Source family | Typical RAW posture | Boundary |
|---|---|---|
| Census TIGER / census place geography | Authority for `CensusPlace`; observation/context for boundary by vintage. | Census identity is statistical, not legal municipal status. |
| GNIS and gazetteers | Authority/context for place names and identity reconciliation. | Name evidence is not legal incorporation or current settlement status by itself. |
| State / local GIS | Administrative, authority, observed, or aggregate context depending on product. | GIS convenience does not decide source role or release state. |
| Municipal and local legal records | Authority for incorporation, annexation, dissolution, name-change, charter, or boundary events. | Legal-status events must stay source-roled and time-scoped. |
| Historical gazetteers, maps, and publications | Candidate/context evidence for townsites, ghost towns, forts, missions, and predecessor identities. | Historic material requires rights, provenance, and sensitivity review before public use. |
| Tribal-nation public registries and treaty context | Authority/context at an approved detail level. | Sovereignty and cultural-sensitivity review govern detail and exposure. |
| Infrastructure inventories and operator records | Administrative, regulatory, observed, or aggregate by source. | Asset identity, condition, service area, and dependency detail do not publish from RAW. |
| Condition, compliance, and inspection sources | Observed/regulatory context by source and time. | Condition and vulnerability detail requires review before downstream claim use. |
| Hazard, hydrology, roads, people/land, and archaeology context | Cross-lane evidence only. | Owning domains keep canonical truth; this lane consumes context through evidence-bound joins. |

---

## RAW source posture

| Rule | Handling |
|---|---|
| RAW is immutable source capture | Payloads or payload references must be hash-bound and should not be overwritten in place. |
| Source role is preserved | Observed, regulatory, modeled, aggregate, administrative, candidate, and synthetic roles must not be flattened. |
| Time kinds stay distinct | Source time, observed time, valid/effective time, retrieval time, release time, and correction time remain separate where material. |
| Census is not legal status | Census enumeration is not a municipal incorporation, annexation, or dissolution record. |
| Infrastructure detail fails closed | Critical-asset, condition, vulnerability, operator, dependency, and exact facility-geometry detail stays restricted until review/release gates close. |
| Context is not ownership | Roads, hazards, hydrology, people/land, and archaeology evidence remains owned by the source domain unless promoted through governed relation logic. |
| Public clients never read RAW | Public layers, reports, PMTiles, stories, graph edges, vector indexes, API payloads, and generated answers cannot read this RAW lane directly. |

---

## Accepted material

Accepted content is limited to source-capture material and RAW-local sidecars:

- source-reference manifests;
- raw payloads or raw payload references;
- SourceDescriptor references or admission-ticket references;
- source identity, source family, source role, source time, retrieval time, product vintage, legal-status references, place-name references, asset identifiers, operator references, condition/inspection references, geometry/support metadata, citation, attribution, rights posture, review notes, and digest sidecars;
- source-head records, retrieval metadata, status metadata, row counts, feature counts, asset counts, place counts, geometry counts, or package metadata where applicable, and checksums;
- local README or index sidecars that help a steward understand capture state without becoming proof, catalog, receipt, registry, policy, release, public artifact, place-status authority, infrastructure-authority, or answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Settlements/Infrastructure doctrine | `docs/domains/settlements-infrastructure/` |
| Source-family doctrine | `docs/sources/catalog/` or `docs/domains/settlements-infrastructure/` |
| Connector code or connector decisions | `connectors/` |
| Pipeline code or pipeline decisions | `pipelines/domains/settlements-infrastructure/` |
| Authoritative SourceDescriptor records or activation decisions | `data/registry/sources/` |
| Rights, terms, review, sovereignty, cultural sensitivity, critical-asset sensitivity, condition/vulnerability, or release policy | `policy/` and governed review lanes |
| Quarantine holds and remediation notes | `data/quarantine/settlements-infrastructure/` |
| Normalized working material | `data/work/settlements-infrastructure/` |
| Validated objects | `data/processed/settlements-infrastructure/` only after gates close |
| Catalog records, triplets, graph truth, or EvidenceBundle state | `data/catalog/`, `data/triplets/`, or proof lanes |
| Receipts as authority | `data/receipts/` |
| Release manifests, correction records, rollback records, signatures | `release/` |
| Public layers, PMTiles, reports, stories, API payloads, downloads, graph edges, vector indexes, or generated answers | `data/published/` only after release gates close |
| Canonical place truth, legal-status truth, infrastructure truth, condition truth, vulnerability detail, public artifact authority, or generated-answer authority | Owning governed downstream/proof/policy/release lanes, never this RAW directory alone |
| Contracts, schemas, validators, app/API/UI code | `contracts/`, `schemas/`, `tools/`, `apps/` |

---

## Directory map

```text
data/raw/settlements-infrastructure/
├── README.md
├── <future-source-family>/
│   └── README.md
└── index.local.json
```

Potential future source-family folders must be created only after admission/path review. Examples may include `census-places/`, `gnis-gazetteers/`, `state-local-gis/`, `municipal-legal-records/`, `historic-gazetteers-maps/`, `tribal-public-registries/`, `infrastructure-inventories/`, `operator-records/`, `condition-inspections/`, and `service-areas/`, but none are confirmed by this README.

`index.local.json` is optional and must remain RAW-local. It is not a public index, catalog record, registry record, release manifest, graph source, layer pointer, search index, vector index, map source, public-output authority, or retrieval source for generated answers.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay RAW | Source was admitted and captured, but no downstream normalization decision has been made. |
| Quarantine | Source role, rights, source family, product/vintage identity, citation, geometry/support, schema, sensitivity, or activation is unresolved. |
| Return / reject | Admission decision or steward review says the source should not be retained in this RAW lane. |
| Move to work | SourceDescriptor, rights posture, source role, source-family/product identity, citation, hash, source-head metadata, and minimal validation support are sufficient for normalization. |
| Promote downstream | Only after later WORK/PROCESSED/CATALOG/RELEASE gates close with receipts, EvidenceBundle support, review/generalization/redaction/model receipts where required, correction path, rollback target, and release manifest where applicable. |

---

## Forbidden shortcut

```text
data/raw/settlements-infrastructure/
→ data/processed/settlements-infrastructure/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm the source belongs to the Settlements/Infrastructure lane and a documented source family.
- [ ] Confirm SourceDescriptor or admission ticket records source ID, source role, rights, citation, product/vintage identity, retrieval time, sensitivity posture, and hash posture.
- [ ] Confirm settlement/place and infrastructure-side object families are not collapsed.
- [ ] Confirm CensusPlace, Municipality, Settlement, Townsite, GhostTown, Fort, Mission, and ReservationCommunity identities stay distinct where evidence requires it.
- [ ] Confirm infrastructure asset, node, segment, facility, service area, operator, condition observation, and dependency records stay behind sensitivity review where applicable.
- [ ] Confirm exact critical-asset geometry, condition/vulnerability detail, operator-sensitive material, and dependency detail are not exposed directly from RAW.
- [ ] Confirm rights, terms, citation, and allowed reuse have been reviewed or explicitly marked `NEEDS VERIFICATION`.
- [ ] Confirm raw payloads are immutable or hash-bound.
- [ ] Confirm no public artifact, graph edge, search index, vector index, public API payload, or generated answer uses RAW Settlements/Infrastructure material directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces the greenfield stub at `data/raw/settlements-infrastructure/README.md`. | **CONFIRMED authored** |
| The target path existed in the live repository as a greenfield stub before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| `data/raw/settlements-infrastructure/` is the documented canonical RAW lane for the domain. | **CONFIRMED by GitHub contents API during this edit** |
| `data/raw/settlement/README.md` exists as related compatibility context, not as the canonical parent lane. | **CONFIRMED by GitHub contents API during this edit** |
| Child RAW README lanes under `data/raw/settlements-infrastructure/` were confirmed during this edit. | **UNKNOWN / not confirmed** |
| README presence proves payloads, SourceDescriptors, connectors, validators, fixtures, CI checks, receipts, review controls, or release readiness. | **DENY** |
| Domain doctrine covers both settlement/place families and infrastructure-side families. | **CONFIRMED by GitHub contents API during this edit** |
| Actual Settlements/Infrastructure RAW payloads exist under this subtree. | **UNKNOWN** |
| SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, review controls, and downstream receipts are wired for this exact canonical lane. | **NEEDS VERIFICATION** |
| This README is proof, receipt authority, release authority, catalog authority, registry authority, policy authority, public artifact authority, place-status authority, infrastructure authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../raw/settlement/README.md`](../../raw/settlement/README.md)
- [`../../quarantine/settlements-infrastructure/README.md`](../../quarantine/settlements-infrastructure/README.md)
- [`../../quarantine/settlement/README.md`](../../quarantine/settlement/README.md)
- [`../../processed/settlements-infrastructure/README.md`](../../processed/settlements-infrastructure/README.md)
- [`../../processed/settlement/README.md`](../../processed/settlement/README.md)
- [`../../catalog/domain/settlements-infrastructure/README.md`](../../catalog/domain/settlements-infrastructure/README.md)
- [`../../published/layers/settlements-infrastructure/README.md`](../../published/layers/settlements-infrastructure/README.md)
- [`../../published/layers/settlements/README.md`](../../published/layers/settlements/README.md)
- [`../../registry/sources/README.md`](../../registry/sources/README.md)
- [`../../../docs/domains/settlements-infrastructure/README.md`](../../../docs/domains/settlements-infrastructure/README.md)
- [`../../../docs/domains/settlements-infrastructure/CANONICAL_PATHS.md`](../../../docs/domains/settlements-infrastructure/CANONICAL_PATHS.md)
- [`../../../docs/domains/settlements-infrastructure/sublanes/settlements.md`](../../../docs/domains/settlements-infrastructure/sublanes/settlements.md)
- [`../../../docs/domains/settlements-infrastructure/sublanes/infrastructure.md`](../../../docs/domains/settlements-infrastructure/sublanes/infrastructure.md)
- [`../../../docs/sources/catalog/census/tiger-line.md`](../../../docs/sources/catalog/census/tiger-line.md)
- [`../../../docs/sources/catalog/usgs/gnis-names.md`](../../../docs/sources/catalog/usgs/gnis-names.md)
- [`../../../docs/architecture/source-roles.md`](../../../docs/architecture/source-roles.md)
- [`../../../release/manifests/README.md`](../../../release/manifests/README.md)

---

KFM rule: this directory is a Settlements/Infrastructure RAW domain index for source capture only. It is not source-family doctrine, registry authority, rights authority, policy authority, proof authority, receipt authority, release authority, catalog authority, place-status authority, infrastructure authority, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
