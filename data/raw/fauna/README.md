<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/fauna/readme
name: Fauna Raw README
path: data/raw/fauna/README.md
type: data-raw-domain-index-readme
version: v0.1.0
status: draft
owners:
  - <fauna-domain-steward>
  - <fauna-source-steward>
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
artifact_family: immutable-fauna-source-capture
sensitivity_posture: raw-internal; source-role-preserving; no-public-path; deny-by-default-sensitive-geometry; rights-needs-verification; release-blocked
related:
  - ebird/README.md
  - eddmaps/README.md
  - gbif/README.md
  - inaturalist/README.md
  - natureserve/README.md
  - usfws_ecos/README.md
  - ../README.md
  - ../../README.md
  - ../../quarantine/fauna/README.md
  - ../../processed/fauna/README.md
  - ../../catalog/domain/fauna/README.md
  - ../../published/layers/fauna/README.md
  - ../../registry/sources/README.md
  - ../../../docs/domains/fauna/SOURCE_REGISTRY.md
  - ../../../docs/domains/fauna/DATA_LIFECYCLE.md
  - ../../../docs/domains/fauna/POLICY.md
  - ../../../docs/domains/fauna/CANONICAL_PATHS.md
  - ../../../docs/architecture/source-roles.md
  - ../../../release/manifests/README.md
tags:
  - kfm
  - data
  - raw
  - fauna
  - biodiversity
  - source-role
  - source-capture
  - sensitive-geometry
  - geoprivacy
  - no-public-path
  - evidence-first
notes:
  - "This README replaces the greenfield stub at `data/raw/fauna/README.md`."
  - "Confirmed child source-family README lanes during this edit: `ebird/`, `eddmaps/`, `gbif/`, `inaturalist/`, `natureserve/`, and `usfws_ecos/`."
  - "Fauna RAW records remain source captures until governed downstream lifecycle transitions close."
  - "Child README presence does not prove payloads, SourceDescriptor records, connector activation, receipts, validators, fixtures, CI enforcement, sensitivity controls, or release readiness."
  - "Payload presence, SourceDescriptor records, connector activation, receipts, validators, fixtures, CI enforcement, geoprivacy controls, review completion, and release readiness remain UNKNOWN or NEEDS VERIFICATION unless separately verified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Fauna RAW

Parent RAW lifecycle index for immutable Fauna source captures and source-admission sidecars.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Lifecycle: RAW" src="https://img.shields.io/badge/lifecycle-RAW-orange">
  <img alt="Domain: fauna" src="https://img.shields.io/badge/domain-fauna-2e8b57">
  <img alt="Posture: no public path" src="https://img.shields.io/badge/posture-no%20public%20path-critical">
  <img alt="Sensitivity: fail closed" src="https://img.shields.io/badge/sensitivity-fail%20closed-red">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite--or--abstain-blueviolet">
</p>

**Quick links:** [Scope](#scope) · [Repo fit](#repo-fit) · [Confirmed source-family lanes](#confirmed-source-family-lanes) · [RAW source posture](#raw-source-posture) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Directory map](#directory-map) · [Exit gates](#exit-gates) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/raw/fauna/` is a no-public-path RAW lifecycle lane. It is not processed Fauna truth, catalog truth, proof, receipt authority, source registry authority, rights authority, sensitivity policy authority, release authority, public API/UI material, exact public occurrence authority, or generated-answer authority. Public clients, normal UI surfaces, and AI surfaces must not read this lane directly.

---

## Scope

This directory indexes immutable RAW source captures and source-admission sidecars for the Fauna domain.

RAW exists for preservation, replay, and audit. It records what was admitted, where it came from, what source role it carried, and which identifiers, times, rights, citations, geometry/support metadata, sensitivity posture, hashes, and caveats must travel with it.

RAW does not decide what a source means, whether rights permit reuse, whether a record can publish, whether a taxon identity is final, whether a sensitive location is safe to expose, or whether a downstream claim is true.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/fauna/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw/` |
| Domain lane | `fauna` |
| Artifact role | Parent RAW domain index for Fauna source captures and RAW-local sidecars |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Upstream | Accepted connector/source-admission output only |
| Downstream | `data/work/fauna/` or `data/quarantine/fauna/` after governed admission/triage |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/`, not this directory |
| Receipt authority | `data/receipts/`, not this directory |
| Registry authority | `data/registry/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when source role, rights, provenance, taxon identity, geometry/support, sensitivity, citation, validation, correction, rollback, or release support is insufficient |

---

## Confirmed source-family lanes

The child lanes below are README paths confirmed by current-session GitHub fetches/edits. This table confirms README presence only; it does **not** prove payloads, source descriptors, connectors, validators, fixtures, receipts, CI checks, sensitivity controls, or release readiness exist.

| Source-family lane | Status | Boundary summary |
|---|---|---|
| [`ebird/`](ebird/README.md) | **CONFIRMED README** | Observed community/citizen-science avian occurrence source capture; not specimen-backed evidence or public release authority. |
| [`eddmaps/`](eddmaps/README.md) | **CONFIRMED README** | Mixed observation plus aggregator source capture for invasive-species records; verifier status is evidence metadata, not KFM release approval. |
| [`gbif/`](gbif/README.md) | **CONFIRMED README** | Federated occurrence aggregator and Backbone/crosswalk support; per-dataset license, DOI, provenance, and sensitivity remain visible. |
| [`inaturalist/`](inaturalist/README.md) | **CONFIRMED README** | Community-observation occurrence evidence; research grade, license, geoprivacy, and taxonomy gates remain fail-closed until reviewed. |
| [`natureserve/`](natureserve/README.md) | **CONFIRMED README** | Heritage/status/rank/sensitivity context source capture; not taxonomic final authority or public conservation-status truth by itself. |
| [`usfws_ecos/`](usfws_ecos/README.md) | **CONFIRMED README** | Federal regulatory/authority carrier for ESA listing/status, critical habitat, IPaC, and species-profile context; not observed occurrence evidence. |

---

## RAW source posture

| Rule | Handling |
|---|---|
| RAW is immutable source capture | Payloads or payload references must be hash-bound and should not be overwritten in place. |
| Source role is preserved | Observed, regulatory, authority, aggregate, administrative, candidate, modeled, context, and synthetic roles must not be flattened. |
| Sensitive geometry fails closed | Exact occurrence geometry, sensitive taxa, nests, dens, roosts, hibernacula, spawning sites, steward-controlled records, and risky joins remain internal until policy/review gates close. |
| Rights and citations travel with the source | SourceDescriptor, citation, rights posture, cadence, sensitivity, and digest closure are required before downstream use. |
| Public use requires governed release | Public layers, reports, stories, API payloads, graph edges, vector indexes, and generated answers cannot read RAW directly. |

---

## Accepted material

Accepted content is limited to source-capture material and RAW-local sidecars:

- source-reference manifests;
- raw payloads or raw payload references;
- SourceDescriptor references or admission-ticket references;
- source role, source identity, taxon/source identifiers, source time, retrieval time, version, quality fields, geometry/support metadata, citation, rights, attribution, sensitivity hints, geoprivacy state, and digest sidecars;
- source-head records, retrieval metadata, status metadata, row counts where applicable, and checksums;
- local README or index sidecars that help a steward understand capture state without becoming proof, catalog, receipt, registry, policy, release, public artifact, or answer authority.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Product and source-family doctrine | `docs/sources/catalog/` |
| Fauna domain doctrine | `docs/domains/fauna/` |
| Connector code or connector decisions | `connectors/` |
| Authoritative SourceDescriptor records or activation decisions | `data/registry/sources/` |
| Rights, terms, sensitivity, geoprivacy, redaction, or release policy | `policy/` and governed review lanes |
| Quarantine holds and remediation notes | `data/quarantine/fauna/` |
| Normalized working material | `data/work/fauna/` |
| Validated Fauna objects | `data/processed/fauna/` |
| Catalog records, triplets, graph truth, or EvidenceBundle state | `data/catalog/`, `data/triplets/`, or proof lanes |
| EvidenceBundle / ProofPack | `data/proofs/` |
| Ingest, validation, redaction, aggregation, source-role, AI, or release receipts as authority | `data/receipts/` |
| Release manifests, correction records, rollback records, signatures | `release/` |
| Public layers, PMTiles, reports, stories, API payloads, downloads, or published artifacts | `data/published/` only after release gates close |
| Taxonomic final authority, specimen authority, conservation-status final authority, exact public occurrence authority, public artifact authority, UI authority, or generated-answer authority | Owning governed downstream/policy/proof/release lanes, never this RAW directory alone |
| Contracts, schemas, validators, app/API/UI code | `contracts/`, `schemas/`, `tools/`, `apps/` |

---

## Directory map

```text
data/raw/fauna/
├── README.md
├── ebird/
│   └── README.md
├── eddmaps/
│   └── README.md
├── gbif/
│   └── README.md
├── inaturalist/
│   └── README.md
├── natureserve/
│   └── README.md
├── usfws_ecos/
│   └── README.md
├── <future-source-family>/
│   └── README.md
└── index.local.json
```

`index.local.json` is optional and must remain RAW-local. It is not a public index, catalog record, registry record, release manifest, graph source, layer pointer, search index, vector index, map source, taxonomic authority, rights authority, geoprivacy authority, public-output authority, or retrieval source for generated answers.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Stay RAW | Source was admitted and captured, but no downstream normalization decision has been made. |
| Quarantine | Source role, rights, sensitivity, taxon identity, geometry/support, attribution, citation, digest, schema, or source activation is unresolved. |
| Return / reject | Admission decision or steward review says the source should not be retained in this RAW lane. |
| Move to work | SourceDescriptor, rights posture, source role, source-family/product identity, citation, hash, and minimal validation support are sufficient for normalization. |
| Promote downstream | Only after later WORK/PROCESSED/CATALOG/RELEASE gates close with receipts, EvidenceBundle support, redaction/generalization/aggregation receipts where required, correction path, rollback target, and release manifest where applicable. |

---

## Forbidden shortcut

```text
data/raw/fauna/
→ data/processed/fauna/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm the source belongs to the Fauna lane.
- [ ] Confirm the correct source-family subfolder or create a documented child README before adding payloads.
- [ ] Confirm a SourceDescriptor or admission ticket identifies source ID, source family, source role, rights, cadence, citation, sensitivity posture, and hash posture.
- [ ] Confirm observed, regulatory, authority, aggregate, administrative, candidate, modeled, context, and interpretation outputs are not collapsed into one source role.
- [ ] Confirm sensitive taxa, exact geometry, nest/den/roost/hibernacula/spawning locations, steward-controlled records, restricted-use records, observer/user-like fields, and risky joins are handled by fail-closed policy before downstream use.
- [ ] Confirm source identity, source time, retrieval time, version, quality fields, taxon/crosswalk posture, geometry/support, and caveats are recorded where material.
- [ ] Confirm rights, endpoint/current terms, citation, and allowed reuse have been reviewed or explicitly marked `NEEDS VERIFICATION`.
- [ ] Confirm raw payloads are immutable or hash-bound and do not overwrite prior runs in place.
- [ ] Confirm required downstream receipts are present or explicitly marked missing before anything leaves RAW.
- [ ] Confirm no public artifact, graph edge, search index, vector index, or generated answer uses RAW material directly.

---

## Status notes

| Claim | Status |
|---|---|
| This README replaces the greenfield stub at `data/raw/fauna/README.md`. | **CONFIRMED authored** |
| The target path existed in the live repository as a greenfield stub before this edit. | **CONFIRMED by GitHub contents API during this edit** |
| `ebird/README.md`, `eddmaps/README.md`, `gbif/README.md`, `inaturalist/README.md`, `natureserve/README.md`, and `usfws_ecos/README.md` exist as confirmed child source-family lanes. | **CONFIRMED by GitHub contents API during this edit** |
| Child README presence proves payloads, SourceDescriptors, connectors, validators, fixtures, CI checks, downstream receipts, sensitivity controls, or release readiness. | **DENY** |
| Fauna lifecycle doctrine says RAW captures immutable source payload/reference with source role, rights, sensitivity, citation, time, and content hash, with no public access. | **CONFIRMED by GitHub contents API during this edit** |
| Fauna source registry doctrine identifies authority, observation, aggregator, heritage/status, invasive-species, context, and steward/restricted source families for Fauna. | **CONFIRMED by GitHub contents API during this edit** |
| Actual Fauna RAW payloads exist under this subtree. | **UNKNOWN** |
| SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, geoprivacy controls, and downstream receipts are wired for this exact parent lane. | **NEEDS VERIFICATION** |
| This README is proof, receipt, release, catalog, registry, policy, public artifact authority, or generated-answer authority. | **DENY** |

---

## Related files

- [`ebird/README.md`](ebird/README.md)
- [`eddmaps/README.md`](eddmaps/README.md)
- [`gbif/README.md`](gbif/README.md)
- [`inaturalist/README.md`](inaturalist/README.md)
- [`natureserve/README.md`](natureserve/README.md)
- [`usfws_ecos/README.md`](usfws_ecos/README.md)
- [`../README.md`](../README.md)
- [`../../README.md`](../../README.md)
- [`../../quarantine/fauna/README.md`](../../quarantine/fauna/README.md)
- [`../../processed/fauna/README.md`](../../processed/fauna/README.md)
- [`../../catalog/domain/fauna/README.md`](../../catalog/domain/fauna/README.md)
- [`../../published/layers/fauna/README.md`](../../published/layers/fauna/README.md)
- [`../../registry/sources/README.md`](../../registry/sources/README.md)
- [`../../../docs/domains/fauna/SOURCE_REGISTRY.md`](../../../docs/domains/fauna/SOURCE_REGISTRY.md)
- [`../../../docs/domains/fauna/DATA_LIFECYCLE.md`](../../../docs/domains/fauna/DATA_LIFECYCLE.md)
- [`../../../docs/domains/fauna/POLICY.md`](../../../docs/domains/fauna/POLICY.md)
- [`../../../docs/domains/fauna/CANONICAL_PATHS.md`](../../../docs/domains/fauna/CANONICAL_PATHS.md)
- [`../../../docs/architecture/source-roles.md`](../../../docs/architecture/source-roles.md)
- [`../../../release/manifests/README.md`](../../../release/manifests/README.md)

---

KFM rule: this directory is a Fauna RAW domain index for source capture only. It is not source-family doctrine, source registry authority, rights authority, sensitivity policy authority, proof authority, receipt authority, release authority, catalog authority, taxonomic final authority, exact public occurrence authority, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
