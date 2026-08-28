<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/geology/readme
name: Geology Raw README
path: data/raw/geology/README.md
type: data-raw-domain-index-readme
version: v0.1.0
status: draft
owners:
  - <geology-domain-steward>
  - <geology-source-steward>
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
domain: geology
artifact_family: immutable-geology-source-capture
sensitivity_posture: raw-internal; source-role-preserving; no-public-path; exact-subsurface-points-deny-by-default; rights-needs-verification; release-blocked
related:
  - ../README.md
  - ../../README.md
  - ../../quarantine/geology/README.md
  - ../../quarantine/geology/rights_unknown/README.md
  - ../../processed/geology/README.md
  - ../../catalog/domain/geology/README.md
  - ../../published/layers/geology/README.md
  - ../../published/pmtiles/geology/README.md
  - ../../registry/sources/README.md
  - ../../../docs/domains/geology/README.md
  - ../../../docs/domains/geology/SOURCE_REGISTRY.md
  - ../../../docs/domains/geology/SOURCES.md
  - ../../../docs/domains/geology/SOURCE_LEDGER.md
  - ../../../docs/domains/geology/SENSITIVITY.md
  - ../../../docs/domains/geology/POLICY.md
  - ../../../docs/architecture/source-roles.md
  - ../../../release/manifests/README.md
tags:
  - kfm
  - data
  - raw
  - geology
  - natural-resources
  - source-role
  - source-capture
  - borehole
  - well-log
  - mineral-occurrence
  - private-well
  - no-public-path
  - evidence-first
notes:
  - "This README replaces the greenfield stub at `data/raw/geology/README.md`."
  - "No child source-family README lanes under `data/raw/geology/` were confirmed during this edit."
  - "The source-family backlog below is derived from current Geology source-registry doctrine and is not evidence of existing RAW payloads or child directories."
  - "Geology RAW records remain source captures until governed downstream lifecycle transitions close."
  - "Payload presence, SourceDescriptor records, connector activation, receipts, validators, fixtures, CI enforcement, sensitivity controls, and release readiness remain UNKNOWN or NEEDS VERIFICATION unless separately verified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Geology RAW

Parent RAW lifecycle index for immutable Geology and Natural Resources source captures and source-admission sidecars.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: geology" src="https://img.shields.io/badge/domain-geology-8b5e3c">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
  <img alt="Sensitivity: exact subsurface deny by default" src="https://img.shields.io/badge/exact%20subsurface-deny%20by%20default-red">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-blueviolet">
</p>

**Quick links:** [Scope](#scope) · [Repo fit](#repo-fit) · [Confirmed child lanes](#confirmed-child-lanes) · [Source-family backlog](#source-family-backlog) · [RAW source posture](#raw-source-posture) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/raw/geology/` is a no-public-path RAW lifecycle lane. It is not processed Geology truth, catalog truth, proof, receipt authority, source registry authority, rights authority, sensitivity policy authority, release authority, public API/UI material, legal/title authority, resource-reserve authority, exact public borehole/well-log authority, or generated-answer authority. Public clients, normal UI surfaces, and AI surfaces must not read this lane directly.

---

## Scope

This directory indexes immutable RAW source captures and source-admission sidecars for the Geology and Natural Resources domain.

RAW exists for preservation, replay, and audit. It records what was admitted, where it came from, what source role it carried, and which identifiers, times, rights, citations, geometry/support metadata, source role, sensitivity posture, hashes, and caveats must travel with it.

RAW does not decide what a source means, whether rights permit reuse, whether a record can publish, whether a mineral occurrence is a deposit, whether a deposit is a reserve, whether a permit proves operation, whether a geologic map is observed fact, or whether a downstream claim is true.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/geology/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw/` |
| Domain lane | `geology` |
| Artifact role | Parent RAW domain index for Geology source captures and RAW-local sidecars |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Upstream | Accepted connector/source-admission output only |
| Downstream | `data/work/geology/` or `data/quarantine/geology/` after governed admission/triage |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/`, not this directory |
| Receipt authority | `data/receipts/`, not this directory |
| Registry authority | `data/registry/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when source role, rights, provenance, geometry/support, aggregation unit, model basis, sensitivity, citation, validation, correction, rollback, or release support is insufficient |

---

## Confirmed child lanes

No child source-family README lanes under `data/raw/geology/` were confirmed during this edit.

This statement confirms only the current edit boundary. It does **not** prove that no directories or payloads exist elsewhere, and it does not prove connector, registry, validator, receipt, CI, or release state.

---

## Source-family backlog

The source families below are admitted or proposed by current Geology source-registry doctrine. They are listed here as RAW lane planning targets only; child README files, payloads, SourceDescriptors, connectors, validators, fixtures, receipts, and release readiness remain unverified unless separately confirmed.

| Source family | Indicative role posture | RAW boundary |
|---|---|---|
| Kansas Geological Survey umbrella | observed · administrative · aggregate | Separate each role into its own SourceDescriptor; do not flatten KGS products into one authority. |
| KGS surficial geology / Kansas geologic maps | observed · modeled | Preserve source scale and model/interpretation basis; compiled maps are not automatically field observations. |
| USGS NGMDB / GeMS | aggregate · administrative · modeled | Preserve compilation identity and map/source vintage; do not cite index entries as observed geology. |
| KGS oil-and-gas wells and production | observed · regulatory · aggregate | Exact well points and operator joins require review; aggregate production is not per-well truth. |
| KCC oil-and-gas regulatory data | regulatory · administrative | Filing facts are not independent rock, production, or operation observations. |
| KGS / KDHE WWC5 water-well program | observed · regulatory · administrative | Private-well exact locations default to restricted/generalized posture. |
| KGS LAS digital well logs and well tops | observed · modeled | Exact well-log points and interpreted tops require sensitivity, rights, and role gates. |
| USGS MRDS | aggregate · observed · administrative | Occurrence records do not become deposit, reserve, or production claims by default. |
| 3DEP terrain | observed · modeled | Public-safe at standard resolutions, but geomorphology derivatives still require source-role and transform receipts. |
| Non-KGS borehole / well-log repositories | observed | Rights and exact-point sensitivity fail closed until verified. |
| Geophysics and geochemistry sources | observed | Sample sites and lab/field evidence need provenance, sensitivity, and citation closure. |
| Mining / reclamation program records | regulatory · administrative | Site-level exposure and public derivatives require review and release gates. |

---

## RAW source posture

| Rule | Handling |
|---|---|
| RAW is immutable source capture | Payloads or payload references must be hash-bound and should not be overwritten in place. |
| Source role is preserved | Observed, regulatory, modeled, aggregate, administrative, candidate, and synthetic roles must not be flattened. |
| Knowledge characters stay distinct | Occurrence, deposit, estimate, permit, operation, production, reserve, map, model, and legal/title claims are separate. |
| Exact subsurface points fail closed | Borehole points, well-log points, sample points, private wells, and sensitive mineral occurrence points default to restricted or generalized public geometry. |
| Rights and citations travel with the source | SourceDescriptor, citation, rights posture, cadence, sensitivity, and digest closure are required before downstream use. |
| Public use requires governed release | Public layers, reports, stories, API payloads, graph edges, vector indexes, and generated answers cannot read RAW directly. |

---

## Accepted material

Accepted content is limited to source-capture material and RAW-local sidecars:

- source-reference manifests;
- raw payloads or raw payload references;
- SourceDescriptor references or admission-ticket references;
- source role, source identity, geologic/mineral/well identifiers, source time, retrieval time, version, quality fields, geometry/support metadata, aggregation unit where applicable, model-run reference where applicable, citation, rights, attribution, sensitivity hints, and digest sidecars;
- source-head records, retrieval metadata, status metadata, row counts where applicable, and checksums;
- local README or index sidecars that help a steward understand capture state without becoming proof, catalog, receipt, registry, policy, release, public artifact, legal/title authority, reserve authority, or answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Product and source-family doctrine | `docs/sources/catalog/` or `docs/domains/geology/` |
| Geology source-registry doctrine | `docs/domains/geology/SOURCE_REGISTRY.md` |
| Geology sensitivity doctrine | `docs/domains/geology/SENSITIVITY.md` |
| Connector code or connector decisions | `connectors/` |
| Authoritative SourceDescriptor records or activation decisions | `data/registry/sources/` |
| Rights, terms, sensitivity, geoprivacy, redaction, or release policy | `policy/` and governed review lanes |
| Quarantine holds and remediation notes | `data/quarantine/geology/` |
| Normalized working material | `data/work/geology/` |
| Validated Geology objects | `data/processed/geology/` |
| Catalog records, triplets, graph truth, or EvidenceBundle state | `data/catalog/`, `data/triplets/`, or proof lanes |
| EvidenceBundle / ProofPack | `data/proofs/` |
| Ingest, validation, redaction, aggregation, source-role, model, AI, or release receipts as authority | `data/receipts/` |
| Release manifests, correction records, rollback records, signatures | `release/` |
| Public layers, PMTiles, reports, stories, API payloads, downloads, or published artifacts | `data/published/` only after release gates close |
| Title, parcel ownership, lease ownership, operator truth, reserve truth, exact public borehole/well-log authority, or generated-answer authority | Owning governed downstream/policy/proof/release lanes, never this RAW directory alone |
| Contracts, schemas, validators, app/API/UI code | `contracts/`, `schemas/`, `tools/`, `apps/` |

---

## Directory map

```text
data/raw/geology/
├── README.md
├── <future-source-family>/
│   └── README.md
└── index.local.json
```

`index.local.json` is optional and must remain RAW-local. It is not a public index, catalog record, registry record, release manifest, graph source, layer pointer, search index, vector index, map source, legal/title authority, resource authority, rights authority, geoprivacy authority, public-output authority, or retrieval source for generated answers.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay RAW | Source was admitted and captured, but no downstream normalization decision has been made. |
| Quarantine | Source role, rights, sensitivity, model basis, aggregation unit, geometry/support, attribution, citation, digest, schema, or source activation is unresolved. |
| Return / reject | Admission decision or steward review says the source should not be retained in this RAW lane. |
| Move to work | SourceDescriptor, rights posture, source role, source-family/product identity, citation, hash, and minimal validation support are sufficient for normalization. |
| Promote downstream | Only after later WORK/PROCESSED/CATALOG/RELEASE gates close with receipts, EvidenceBundle support, model/aggregation/generalization receipts where required, correction path, rollback target, and release manifest where applicable. |

---

## Forbidden shortcut

```text
data/raw/geology/
→ data/processed/geology/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm the source belongs to the Geology lane.
- [ ] Confirm the correct source-family subfolder or create a documented child README before adding payloads.
- [ ] Confirm a SourceDescriptor or admission ticket identifies source ID, source family, source role, rights, cadence, citation, sensitivity posture, and hash posture.
- [ ] Confirm observed, regulatory, modeled, aggregate, administrative, candidate, synthetic, context, and interpretation outputs are not collapsed into one source role.
- [ ] Confirm occurrence, deposit, reserve estimate, production, permit, operation, compiled map, model, ownership, lease, and title claims are not collapsed.
- [ ] Confirm exact borehole, well-log, sample, private-well, and sensitive resource locations are handled by fail-closed policy before downstream use.
- [ ] Confirm source identity, source time, retrieval time, version, quality fields, model/crosswalk posture, geometry/support, aggregation unit, and caveats are recorded where material.
- [ ] Confirm rights, endpoint/current terms, citation, and allowed reuse have been reviewed or explicitly marked `NEEDS VERIFICATION`.
- [ ] Confirm raw payloads are immutable or hash-bound and do not overwrite prior runs in place.
- [ ] Confirm required downstream receipts are present or explicitly marked missing before anything leaves RAW.
- [ ] Confirm no public artifact, graph edge, search index, vector index, or generated answer uses RAW material directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces the greenfield stub at `data/raw/geology/README.md`. | **CONFIRMED authored** |
| The target path existed in the live repository as a greenfield stub before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| Child source-family README lanes under `data/raw/geology/` were confirmed during this edit. | **UNKNOWN / none confirmed in this edit** |
| The source-family backlog in this README is derived from Geology source-registry doctrine, not from confirmed RAW child directories. | **CONFIRMED authored** |
| Geology source-registry doctrine says source role, rights, sensitivity, freshness, and activation gates must be recorded before connector/watcher activation. | **CONFIRMED by GitHub contents API during this edit** |
| Geology source-registry doctrine says borehole/well-log/private-well/sensitive-resource exact geometry defaults to restricted or generalized public posture. | **CONFIRMED by GitHub contents API during this edit** |
| Actual Geology RAW payloads exist under this subtree. | **UNKNOWN** |
| SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, geoprivacy controls, and downstream receipts are wired for this exact parent lane. | **NEEDS VERIFICATION** |
| This README is proof, receipt, release, catalog, registry, policy, legal/title authority, reserve authority, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../quarantine/geology/README.md`](../../quarantine/geology/README.md)
- [`../../quarantine/geology/rights_unknown/README.md`](../../quarantine/geology/rights_unknown/README.md)
- [`../../processed/geology/README.md`](../../processed/geology/README.md)
- [`../../catalog/domain/geology/README.md`](../../catalog/domain/geology/README.md)
- [`../../published/layers/geology/README.md`](../../published/layers/geology/README.md)
- [`../../published/pmtiles/geology/README.md`](../../published/pmtiles/geology/README.md)
- [`../../registry/sources/README.md`](../../registry/sources/README.md)
- [`../../../docs/domains/geology/README.md`](../../../docs/domains/geology/README.md)
- [`../../../docs/domains/geology/SOURCE_REGISTRY.md`](../../../docs/domains/geology/SOURCE_REGISTRY.md)
- [`../../../docs/domains/geology/SOURCES.md`](../../../docs/domains/geology/SOURCES.md)
- [`../../../docs/domains/geology/SOURCE_LEDGER.md`](../../../docs/domains/geology/SOURCE_LEDGER.md)
- [`../../../docs/domains/geology/SENSITIVITY.md`](../../../docs/domains/geology/SENSITIVITY.md)
- [`../../../docs/domains/geology/POLICY.md`](../../../docs/domains/geology/POLICY.md)
- [`../../../docs/architecture/source-roles.md`](../../../docs/architecture/source-roles.md)
- [`../../../release/manifests/README.md`](../../../release/manifests/README.md)

---

KFM rule: this directory is a Geology RAW domain index for source capture only. It is not source-family doctrine, source registry authority, rights authority, sensitivity policy authority, proof authority, receipt authority, release authority, catalog authority, legal/title authority, resource-reserve authority, exact public borehole/well-log authority, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
