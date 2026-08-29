<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/raw/fauna/readme
name: Fauna Raw README
path: data/raw/fauna/README.md
type: data-raw-domain-index-readme
version: v0.1.1
prior_version: v0.1.0
status: draft
owners:
  - <fauna-domain-steward>
  - <fauna-source-steward>
  - <data-steward>
  - <rights-reviewer>
  - <sensitivity-reviewer>
  - <release-steward>
created: 2026-06-27
updated: 2026-08-28
policy_label: restricted-review
truth_posture: cite-or-abstain
lifecycle_phase: raw
responsibility_root: data/
responsibility: Preserve the tracked Fauna RAW compatibility and reference index without treating this domain subtree or its source-named children as physical capture homes.
domain: fauna
artifact_family: fauna-raw-compatibility-reference-index
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
  - "Confirmed child source-family README references during this reconciliation: `ebird/`, `eddmaps/`, `gbif/`, `inaturalist/`, `natureserve/`, and `usfws_ecos/`."
  - "Accepted Directory Rules require one source-first capture identity; these domain-scoped documentation lanes do not authorize duplicated RAW bytes or establish physical capture placement."
  - "Child README presence does not prove payloads, SourceDescriptor records, connector activation, receipts, validators, fixtures, CI enforcement, sensitivity controls, or release readiness."
  - "Payload presence, SourceDescriptor records, connector activation, receipts, validators, fixtures, CI enforcement, geoprivacy controls, review completion, and release readiness remain UNKNOWN or NEEDS VERIFICATION unless separately verified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Fauna RAW

Compatibility and reference index for legacy Fauna-scoped RAW documentation; not a physical source-capture home.

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
> `data/raw/fauna/` is a no-public-path compatibility/reference index inside the RAW lifecycle boundary. Accepted Directory Rules require one source-first capture identity, so this domain subtree and its source-named children are not default physical capture homes and must not receive duplicate RAW payloads. It is not processed Fauna truth, catalog truth, proof, receipt authority, source registry authority, rights authority, sensitivity policy authority, release authority, public API/UI material, exact public occurrence authority, or generated-answer authority.

---

## Scope

This directory indexes tracked Fauna-facing source documentation and legacy domain-scoped RAW topology. It may reference one governed source-first capture, but it does not establish where that capture is stored.

The canonical RAW boundary exists for preservation, replay, and audit. A governed source-first capture records what was admitted, where it came from, what source role it carried, and which identifiers, times, rights, citations, geometry/support metadata, sensitivity posture, hashes, and caveats must travel with it.

RAW does not decide what a source means, whether rights permit reuse, whether a record can publish, whether a taxon identity is final, whether a sensitive location is safe to expose, or whether a downstream claim is true.

---

## Repo fit

| Field | Value |
|---|---|
| Path | `data/raw/fauna/` |
| Responsibility root | `data/` |
| Lifecycle phase | `raw/` |
| Domain lane | `fauna` |
| Artifact role | Compatibility/reference index for Fauna-facing source documentation and unresolved legacy RAW topology |
| Public access posture | No public path; no normal UI; no governed-public API exposure |
| Upstream | References to an admitted source-first capture only; physical placement remains **NEEDS VERIFICATION** |
| Downstream | Governed Fauna WORK or QUARANTINE procedures consume references or approved handoffs, not assumed domain-local copies |
| Release authority | `release/`, not this directory |
| Proof authority | `data/proofs/`, not this directory |
| Receipt authority | `data/receipts/`, not this directory |
| Registry authority | `data/registry/`, not this directory |
| Policy authority | `policy/`, not this directory |
| Default failure posture | `HOLD`, `QUARANTINE`, `DENY`, or `ABSTAIN` when source role, rights, provenance, taxon identity, geometry/support, sensitivity, citation, validation, correction, rollback, or release support is insufficient |

---

## Confirmed source-family lanes

The child lanes below are confirmed README paths. Treat them as compatibility/reference documentation or unresolved legacy topology, not source-first capture homes. Their presence does **not** prove or authorize payloads, source descriptors, connectors, validators, fixtures, receipts, CI checks, sensitivity controls, migration, or release readiness.

| Source-family lane | Status | Boundary summary |
|---|---|---|
| [`ebird/`](ebird/README.md) | **CONFIRMED README / COMPATIBILITY REFERENCE** | Community/citizen-science avian occurrence source documentation; not specimen-backed evidence, a capture home, or public release authority. |
| [`eddmaps/`](eddmaps/README.md) | **CONFIRMED README / COMPATIBILITY REFERENCE** | Mixed observation and aggregator source documentation for invasive-species records; verifier status is evidence metadata, not KFM release approval or capture placement. |
| [`gbif/`](gbif/README.md) | **CONFIRMED README / COMPATIBILITY REFERENCE** | Federated occurrence aggregator and Backbone/crosswalk documentation; per-dataset license, DOI, provenance, sensitivity, and the single source-first capture remain visible. |
| [`inaturalist/`](inaturalist/README.md) | **CONFIRMED README / COMPATIBILITY REFERENCE** | Community-observation source documentation; research grade, license, geoprivacy, taxonomy, capture placement, and reuse remain fail-closed until reviewed. |
| [`natureserve/`](natureserve/README.md) | **CONFIRMED README / COMPATIBILITY REFERENCE** | Heritage/status/rank/sensitivity context documentation; not a capture home, taxonomic final authority, or public conservation-status truth by itself. |
| [`usfws_ecos/`](usfws_ecos/README.md) | **CONFIRMED README / COMPATIBILITY REFERENCE** | Federal regulatory/context source documentation for ESA status, critical habitat, IPaC, and species profiles; not observed occurrence evidence or a capture home. |

---

## RAW source posture

| Rule | Handling |
|---|---|
| Capture identity is source-first | Register one `source_id` and preserve one immutable capture identity; domain references may support Fauna without duplicating RAW bytes. |
| Physical placement is held | Do not infer `data/raw/fauna/` or a child directory as the capture home. Use only an accepted writer/path contract; none is established by this README. |
| RAW is immutable source capture | Payloads or payload references at the accepted source-first home must be hash-bound and should not be overwritten in place. |
| Source role is preserved | Observed, regulatory, authority, aggregate, administrative, candidate, modeled, context, and synthetic roles must not be flattened. |
| Sensitive geometry fails closed | Exact occurrence geometry, sensitive taxa, nests, dens, roosts, hibernacula, spawning sites, steward-controlled records, and risky joins remain internal until policy/review gates close. |
| Rights and citations travel with the source | SourceDescriptor, citation, rights posture, cadence, sensitivity, and digest closure are required before downstream use. |
| Public use requires governed release | Public layers, reports, stories, API payloads, graph edges, vector indexes, and generated answers cannot read RAW directly. |

---

## Accepted material

Accepted content is limited to documentation and governed references that do not duplicate source-first captures:

- the tracked README files listed below;
- links to canonical SourceDescriptor, source-admission, rights, sensitivity, and connector authority;
- references to a governed source-first capture or quarantine handoff when an accepted contract defines their shape;
- migration or correction notes that label legacy topology without moving or copying payloads;
- an optional local documentation index only after its schema, producer, owner, and non-authoritative role are accepted.

Do not place raw payloads, copied source runs, source-head records, checksums, or other capture sidecars in this subtree merely because they support Fauna. Exact physical placement and legacy migration remain **HOLD**.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Domain-scoped copies of source captures or new source-run directories | One accepted source-first RAW home after a reviewed placement decision; exact path remains **NEEDS VERIFICATION** |
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
├── ebird/README.md
├── eddmaps/README.md
├── gbif/README.md
├── inaturalist/README.md
├── natureserve/README.md
└── usfws_ecos/README.md
```

This is the confirmed documentation topology, not a storage specification. Do not add a future source directory, payload, or local index here until an accepted source-first placement or compatibility decision defines its role.

---

## Exit gates

| Exit route | Minimum requirement |
|---|---|
| Remain at the source-first RAW home | Source was admitted and captured, but no downstream normalization decision has been made. This index may retain a governed reference only. |
| Quarantine | Source role, rights, sensitivity, taxon identity, geometry/support, attribution, citation, digest, schema, source activation, or physical placement is unresolved. |
| Return / reject | Admission or steward review says the capture must not be retained; correction occurs through the owning source-first or quarantine procedure. |
| Move to work | A governed reference or approved handoff may enter Fauna WORK only when SourceDescriptor, rights posture, source role, product identity, citation, hash, and minimal validation support are sufficient. |
| Promote downstream | Only after later WORK/PROCESSED/CATALOG/RELEASE gates close with receipts, EvidenceBundle support, redaction/generalization/aggregation receipts where required, correction path, rollback target, and release manifest where applicable. |

---

## Forbidden shortcut

```text
source-first RAW capture (physical path NEEDS VERIFICATION)
→ data/processed/fauna/
→ data/catalog/ or data/triplets/
→ data/published/
→ public API / MapLibre / PMTiles / report / story / graph / vector index / generated answer
```

This is forbidden unless each governed lifecycle transition has actually happened and left inspectable evidence.

---

## Required checks before use

- [ ] Confirm one registered `source_id` and one immutable source-first capture identity; do not create a second Fauna-scoped copy.
- [ ] Treat the source-named child README as compatibility/reference documentation only; do not create a child directory as a payload destination.
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
| `ebird/README.md`, `eddmaps/README.md`, `gbif/README.md`, `inaturalist/README.md`, `natureserve/README.md`, and `usfws_ecos/README.md` exist as child compatibility/reference documents. | **CONFIRMED at reconciliation base** |
| Child README presence proves payloads, SourceDescriptors, connectors, validators, fixtures, CI checks, downstream receipts, sensitivity controls, or release readiness. | **DENY** |
| Fauna lifecycle doctrine says RAW captures immutable source payload/reference with source role, rights, sensitivity, citation, time, and content hash, with no public access. | **CONFIRMED by GitHub contents API during this edit** |
| Fauna source registry doctrine identifies authority, observation, aggregator, heritage/status, invasive-species, context, and steward/restricted source families for Fauna. | **CONFIRMED by GitHub contents API during this edit** |
| Accepted Directory Rules require one source-first capture identity and prohibit duplicated RAW bytes across domains. | **CONFIRMED** |
| This subtree is an accepted physical source-first capture home. | **DENY — no placement decision found** |
| Actual Fauna RAW payloads exist under this subtree. | **UNKNOWN; do not add or move any during this documentation correction** |
| Child README content is fully reconciled to the source-first parent contract. | **HOLD — child documents retain legacy physical-lane language and require separate review** |
| SourceDescriptor records, connector activation, receipts, validators, fixtures, CI checks, geoprivacy controls, and downstream receipts are wired to an accepted source-first RAW writer. | **NEEDS VERIFICATION** |
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

KFM rule: this directory is a Fauna-facing compatibility/reference index. One governed source-first capture may support Fauna without duplicated RAW bytes; this subtree does not establish physical placement. It is not source-family doctrine, source registry authority, rights authority, sensitivity policy authority, proof authority, receipt authority, release authority, catalog authority, taxonomic final authority, exact public occurrence authority, public artifact authority, UI authority, graph authority, vector-index authority, or generated-answer truth.

[Back to top](#top)
