<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/settlement/readme
name: Settlement Raw Compatibility README
path: data/raw/settlement/README.md
type: data-raw-domain-index-readme; compatibility-lane-readme
version: v0.1.0
status: draft
owners:
  - <settlements-infrastructure-domain-steward>
  - <settlements-sublane-steward>
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
requested_path_segment: settlement
canonical_domain_candidate: settlements-infrastructure
artifact_family: settlement-raw-compatibility-source-capture-index
sensitivity_posture: raw-internal; source-role-preserving; no-public-path; compatibility-path; rights-needs-verification; release-blocked
related:
  - ../README.md
  - ../../README.md
  - ../../quarantine/settlement/README.md
  - ../../quarantine/settlements-infrastructure/README.md
  - ../../processed/settlement/README.md
  - ../../processed/settlements-infrastructure/README.md
  - ../../catalog/domain/settlements-infrastructure/README.md
  - ../../published/layers/settlements/README.md
  - ../../published/layers/settlements-infrastructure/README.md
  - ../../registry/sources/README.md
  - ../../../docs/domains/settlements-infrastructure/README.md
  - ../../../docs/domains/settlements-infrastructure/CANONICAL_PATHS.md
  - ../../../docs/domains/settlements-infrastructure/sublanes/settlements.md
  - ../../../docs/sources/catalog/census/tiger-line.md
  - ../../../docs/sources/catalog/usgs/gnis-names.md
  - ../../../docs/architecture/source-roles.md
  - ../../../release/manifests/README.md
tags:
  - kfm
  - data
  - raw
  - settlement
  - settlements-infrastructure
  - compatibility-path
  - settlements
  - municipality
  - census-place
  - townsite
  - ghost-town
  - fort
  - mission
  - reservation-community
  - source-capture
  - source-role
  - no-public-path
  - evidence-first
notes:
  - "This README replaces placeholder content at `data/raw/settlement/README.md`."
  - "The canonical domain segment is documented as `settlements-infrastructure`; this singular `settlement` path is treated as a compatibility RAW index unless an ADR resolves otherwise."
  - "No child RAW README lanes under `data/raw/settlement/` were confirmed during this edit."
  - "README presence confirms documentation only; it does not prove payloads, SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, review controls, or release readiness."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Settlement RAW Compatibility Index

Compatibility RAW lifecycle index for settlement-place source captures associated with the Settlements/Infrastructure domain.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Segment: compatibility" src="https://img.shields.io/badge/segment-compatibility-orange">
  <img alt="Domain: settlements-infrastructure" src="https://img.shields.io/badge/domain-settlements--infrastructure-7048e8">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-blueviolet">
</p>

**Quick links:** [Canonical path warning](#canonical-path-warning) · [Scope](#scope) · [Repo fit](#repo-fit) · [Source-family posture](#source-family-posture) · [RAW source posture](#raw-source-posture) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/raw/settlement/` is a no-public-path compatibility RAW lane. It is not canonical domain authority, processed settlement truth, catalog truth, proof, receipt authority, source registry authority, rights authority, policy authority, release authority, public API/UI material, public PMTiles material, or generated-answer authority.

---

## Canonical path warning

Settlements/Infrastructure canonical-path doctrine identifies `settlements-infrastructure` as the working domain segment across responsibility roots, while acknowledging a documented slug variance where Atlas crosswalk material uses singular `settlement`. Until the open path question is resolved by ADR, this requested singular path is treated as a compatibility RAW index, not a new canonical authority root.

Do not create parallel schema, contract, policy, registry, proof, release, public-layer, graph, vector-index, or generated-answer authority from this compatibility path.

---

## Scope

This directory indexes settlement-place RAW source-capture material only when the repository intentionally preserves the singular `settlement` path as a compatibility bridge.

The settlement sublane covers place and community identity evidence for:

- `Settlement`;
- `Municipality`;
- `CensusPlace`;
- `Townsite`;
- `GhostTown`;
- `Fort`;
- `Mission`;
- `ReservationCommunity`.

RAW records what was captured, where it came from, what source role it carried, and which identifiers, names, vintages, source times, retrieval times, rights notes, citations, geometry/support metadata, hashes, review notes, and caveats must travel downstream.

RAW does not decide whether a place identity, legal status, census identity, historic townsite, ghost-town status, fort, mission, reservation-community detail, boundary, status event, map layer, public claim, or generated answer is true or release-ready.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/settlement/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw` |
| Requested segment | `settlement` |
| Working canonical domain candidate | `settlements-infrastructure` |
| Lane type | Compatibility RAW index for settlement-place source capture |
| Confirmed child README lanes | None confirmed during this edit |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Upstream | Explicitly admitted connector/source-admission output only |
| Downstream | `data/work/settlements-infrastructure/`, `data/quarantine/settlement/`, or `data/quarantine/settlements-infrastructure/` after governed triage and path review |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/`, not this directory |
| Receipt authority | `data/receipts/`, not this directory |
| Registry authority | `data/registry/sources/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when source role, rights, path authority, citation, geometry/support, sensitivity, validation, correction, rollback, or release support is insufficient |

---

## Source-family posture

The settlement sublane doctrine identifies source families that may feed settlement-place identity after governed admission. This parent README does not prove that any payloads or child source-family folders exist.

| Source family | Typical RAW posture | Boundary |
|---|---|---|
| Census TIGER / census place geography | Authority for `CensusPlace`; observation/context for boundary by vintage. | Census place identity is statistical, not legal municipality truth. |
| GNIS and gazetteers | Authority/context for place-name records and identity reconciliation. | Place name evidence is not legal incorporation or settlement-status proof by itself. |
| State / local GIS | Administrative or authority context for boundaries and current place records by source. | GIS boundary refreshes do not erase older legal, census, or historic identity evidence. |
| Municipal and local legal records | Authority for municipality charter, incorporation, annexation, dissolution, or name-change events. | Legal-status events must stay source-roled and time-scoped. |
| Historical gazetteers and maps | Historical evidence for townsites, ghost towns, forts, missions, and predecessor place identities. | Historical sources need rights/provenance review and cannot be silently upgraded to current status. |
| Tribal-nation public registries and treaty context | Authority/context for reservation-community identification at an approved detail level. | Sovereignty and cultural-sensitivity review govern detail and public exposure. |
| Academic and historical-society publications | Context or interpretive evidence. | Secondary works are not primary legal authority by themselves. |

---

## RAW source posture

| Rule | Handling |
|---|---|
| Compatibility path is not authority | `data/raw/settlement/` does not create a new canonical Settlement authority root. |
| RAW is immutable source capture | Payloads or payload references must be hash-bound and should not be overwritten in place. |
| Source role is preserved | Observed, regulatory, modeled, aggregate, administrative, candidate, and synthetic roles must not be flattened. |
| Census is not legal status | A census enumeration is not a legal incorporation, annexation, or dissolution record. |
| Historical context is not current status | Gazetteers, historic maps, and settlement histories require review before current/public place claims. |
| Sensitive place detail fails closed | Reservation-community detail, archaeology-adjacent townsites, forts, missions, and cultural context require steward review where applicable. |
| Public clients never read RAW | Public layers, reports, PMTiles, stories, graph edges, vector indexes, API payloads, and generated answers cannot read this RAW lane directly. |

---

## Accepted material

Accepted content is limited to source-capture material and RAW-local sidecars:

- source-reference manifests;
- raw payloads or raw payload references;
- SourceDescriptor references or admission-ticket references;
- source identity, source family, source role, source time, retrieval time, census vintage, legal-status event references, place-name references, geometry/support metadata, citation, attribution, rights posture, review notes, and digest sidecars;
- source-head records, retrieval metadata, status metadata, row counts, feature counts, place counts, geometry counts, or package metadata where applicable, and checksums;
- local README or index sidecars that help a steward understand capture state without becoming proof, catalog, receipt, registry, policy, release, public artifact, place-status authority, legal-status authority, or answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Settlements/Infrastructure doctrine | `docs/domains/settlements-infrastructure/` |
| Source-family doctrine | `docs/sources/catalog/` or `docs/domains/settlements-infrastructure/` |
| Connector code or connector decisions | `connectors/` |
| Pipeline code or pipeline decisions | `pipelines/domains/settlements-infrastructure/` |
| Authoritative SourceDescriptor records or activation decisions | `data/registry/sources/` |
| Rights, terms, review, sovereignty, cultural sensitivity, archaeology adjacency, or release policy | `policy/` and governed review lanes |
| Quarantine holds and remediation notes | `data/quarantine/settlement/` or `data/quarantine/settlements-infrastructure/` |
| Normalized working material | `data/work/settlements-infrastructure/` after path review |
| Validated Settlement objects | `data/processed/settlement/` or `data/processed/settlements-infrastructure/` only after gates close and path variance is resolved/recorded |
| Catalog records, triplets, graph truth, or EvidenceBundle state | `data/catalog/`, `data/triplets/`, or proof lanes |
| Receipts as authority | `data/receipts/` |
| Release manifests, correction records, rollback records, signatures | `release/` |
| Public layers, PMTiles, reports, stories, API payloads, downloads, graph edges, vector indexes, or generated answers | `data/published/` only after release gates close |
| Canonical place truth, legal-status truth, census-status truth, cultural-site truth, public artifact authority, or generated-answer authority | Owning governed downstream/proof/policy/release lanes, never this RAW directory alone |
| Contracts, schemas, validators, app/API/UI code | `contracts/`, `schemas/`, `tools/`, `apps/` |

---

## Directory map

```text
data/raw/settlement/
├── README.md
├── <future-source-family>/
│   └── README.md
└── index.local.json
```

Potential future source-family folders must be created only after admission/path review. Examples may include `census-places/`, `gnis-gazetteers/`, `state-local-gis/`, `municipal-legal-records/`, `historic-gazetteers-maps/`, `tribal-public-registries/`, and `historical-society-publications/`, but none are confirmed by this README.

`index.local.json` is optional and must remain RAW-local. It is not a public index, catalog record, registry record, release manifest, graph source, layer pointer, search index, vector index, map source, public-output authority, or retrieval source for generated answers.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay RAW | Source was admitted and captured, but no downstream normalization decision has been made. |
| Quarantine | Source role, rights, source family, path authority, product/vintage identity, citation, geometry/support, schema, sensitivity, or activation is unresolved. |
| Return / reject | Admission decision or steward review says the source should not be retained in this RAW lane. |
| Move to work | SourceDescriptor, rights posture, source role, source-family/product identity, citation, hash, source-head metadata, and minimal validation support are sufficient for normalization. |
| Promote downstream | Only after later WORK/PROCESSED/CATALOG/RELEASE gates close with receipts, EvidenceBundle support, review/generalization receipts where required, correction path, rollback target, and release manifest where applicable. |

---

## Forbidden shortcut

```text
data/raw/settlement/
→ data/processed/settlement/ or data/processed/settlements-infrastructure/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm the singular `settlement` path is being used as a compatibility RAW index, not a new canonical authority root.
- [ ] Confirm the source belongs to the settlement sublane and a documented source family.
- [ ] Confirm SourceDescriptor or admission ticket records source ID, source role, rights, citation, product/vintage identity, retrieval time, and hash posture.
- [ ] Confirm CensusPlace, Municipality, Settlement, Townsite, GhostTown, Fort, Mission, and ReservationCommunity identities are not collapsed.
- [ ] Confirm census enumeration is not treated as legal municipal status by itself.
- [ ] Confirm historic gazetteer/map evidence is not treated as current settlement status without review.
- [ ] Confirm reservation-community, archaeology-adjacent, cultural, sacred, or sovereignty-sensitive details are reviewed and generalized where required.
- [ ] Confirm rights, terms, citation, and allowed reuse have been reviewed or explicitly marked `NEEDS VERIFICATION`.
- [ ] Confirm raw payloads are immutable or hash-bound.
- [ ] Confirm no public artifact, graph edge, search index, vector index, public API payload, or generated answer uses RAW Settlement material directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces placeholder content at `data/raw/settlement/README.md`. | **CONFIRMED authored** |
| The target path existed and contained only placeholder content before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| The working canonical domain segment is documented as `settlements-infrastructure`; singular `settlement` is a documented path variance. | **CONFIRMED by GitHub contents API during this edit** |
| Child RAW README lanes under `data/raw/settlement/` were confirmed during this edit. | **UNKNOWN / not confirmed** |
| README presence proves payloads, SourceDescriptors, connectors, validators, fixtures, CI checks, receipts, review controls, or release readiness. | **DENY** |
| Settlement sublane doctrine lists source families including Census TIGER/census place geography, GNIS/gazetteers, state/local GIS, municipal/local legal records, historical gazetteers/maps, tribal public registries/treaty context, and academic/historical-society publications. | **CONFIRMED by GitHub contents API during this edit** |
| Actual Settlement RAW payloads exist under this subtree. | **UNKNOWN** |
| SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, review controls, and downstream receipts are wired for this exact compatibility lane. | **NEEDS VERIFICATION** |
| This README is canonical domain authority, proof, receipt authority, release authority, catalog authority, registry authority, policy authority, public artifact authority, legal-status authority, place-truth authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../quarantine/settlement/README.md`](../../quarantine/settlement/README.md)
- [`../../quarantine/settlements-infrastructure/README.md`](../../quarantine/settlements-infrastructure/README.md)
- [`../../processed/settlement/README.md`](../../processed/settlement/README.md)
- [`../../processed/settlements-infrastructure/README.md`](../../processed/settlements-infrastructure/README.md)
- [`../../catalog/domain/settlements-infrastructure/README.md`](../../catalog/domain/settlements-infrastructure/README.md)
- [`../../published/layers/settlements/README.md`](../../published/layers/settlements/README.md)
- [`../../published/layers/settlements-infrastructure/README.md`](../../published/layers/settlements-infrastructure/README.md)
- [`../../registry/sources/README.md`](../../registry/sources/README.md)
- [`../../../docs/domains/settlements-infrastructure/README.md`](../../../docs/domains/settlements-infrastructure/README.md)
- [`../../../docs/domains/settlements-infrastructure/CANONICAL_PATHS.md`](../../../docs/domains/settlements-infrastructure/CANONICAL_PATHS.md)
- [`../../../docs/domains/settlements-infrastructure/sublanes/settlements.md`](../../../docs/domains/settlements-infrastructure/sublanes/settlements.md)
- [`../../../docs/sources/catalog/census/tiger-line.md`](../../../docs/sources/catalog/census/tiger-line.md)
- [`../../../docs/sources/catalog/usgs/gnis-names.md`](../../../docs/sources/catalog/usgs/gnis-names.md)
- [`../../../docs/architecture/source-roles.md`](../../../docs/architecture/source-roles.md)
- [`../../../release/manifests/README.md`](../../../release/manifests/README.md)

---

KFM rule: this directory is a Settlement compatibility RAW index for source capture only. It is not canonical domain authority, source-family doctrine, registry authority, rights authority, policy authority, proof authority, receipt authority, release authority, catalog authority, place-truth authority, legal-status authority, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
