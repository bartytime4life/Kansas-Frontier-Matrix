<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/flora/readme
name: Flora Registry README
path: data/registry/flora/README.md
type: data-registry-flora-parent-readme
version: v0.2.0
status: draft
owners:
  - <registry-steward>
  - <flora-domain-steward>
  - <source-steward>
  - <dataset-steward>
  - <crosswalk-steward>
  - <policy-steward>
  - <proof-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: registry
registry_scope: flora-domain-first-registry-parent
domain: flora
path_posture: existing-parent-stub-replaced; sources-child-lane-confirmed; domain-first-registry-path-exists; canonical-subtype-first-topology-needs-verification
sensitivity_posture: registry-internal; no-public-path; rare-plant-deny-default; culturally-sensitive-plant-knowledge-protected; source-role-preserving; evidence-aware; rights-aware; policy-aware; release-blocked-until-gates-close
related:
  - ../README.md
  - ../sources/README.md
  - ../sources/flora/
  - ../datasets/README.md
  - ../datasets/flora/README.md
  - ../domains/README.md
  - ../crosswalks/README.md
  - sources/README.md
  - ../../raw/flora/
  - ../../work/flora/
  - ../../quarantine/flora/
  - ../../processed/flora/
  - ../../catalog/domain/flora/
  - ../../catalog/stac/flora/README.md
  - ../../receipts/
  - ../../proofs/
  - ../../../docs/domains/flora/SOURCE_REGISTRY.md
  - ../../../docs/domains/flora/SOURCE_FAMILIES.md
  - ../../../docs/domains/flora/SOURCES.md
  - ../../../docs/domains/flora/SOURCE_INTAKE.md
  - ../../../docs/domains/flora/DATA_LIFECYCLE.md
  - ../../../docs/domains/flora/SENSITIVITY.md
  - ../../../contracts/domains/flora/
  - ../../../schemas/contracts/v1/source/
  - ../../../schemas/contracts/v1/domains/flora/
  - ../../../policy/domains/flora/
  - ../../../release/
tags:
  - kfm
  - data
  - registry
  - flora
  - domain-first-registry
  - sources
  - source-descriptor
  - source-role
  - rights
  - sensitivity
  - geoprivacy
  - rare-plants
  - culturally-sensitive-plants
  - taxonomy
  - specimens
  - occurrences
  - vegetation
  - evidence
  - provenance
  - release-gated
  - no-public-path
notes:
  - "This README replaces the greenfield stub at `data/registry/flora/README.md`."
  - "This domain-first registry parent exists in the repository and currently has a confirmed `sources/` child README."
  - "The inspected Flora source-registry doctrine names `data/registry/sources/flora/` as the machine-readable source registry lane. Therefore this parent is treated as a compatibility/routing lane until registry topology is reconciled."
  - "Rare-plant exact geometry, culturally sensitive plant knowledge, steward-controlled records, rights-unclear feeds, taxonomy collisions, and join-induced sensitivity remain fail-closed until governed redaction/review/release gates close."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Flora Registry

Domain-first registry parent for Flora registry lanes.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: registry" src="https://img.shields.io/badge/family-registry-blueviolet">
  <img alt="Domain: flora" src="https://img.shields.io/badge/domain-flora-2ea44f">
  <img alt="Topology: needs verification" src="https://img.shields.io/badge/topology-NEEDS%20VERIFICATION-orange">
  <img alt="Boundary: not source data" src="https://img.shields.io/badge/boundary-not%20source%20data-critical">
  <img alt="Exposure: no public path" src="https://img.shields.io/badge/exposure-no%20public%20path-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Confirmed child lanes](#confirmed-child-lanes) · [Flora registry boundary](#flora-registry-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Suggested directory shape](#suggested-directory-shape) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/registry/flora/` is a domain-first registry parent. It is not RAW source storage, WORK staging, QUARANTINE, PROCESSED data, catalog output, proof storage, receipt storage, semantic contract authority, schema authority, policy, release authority, public API/UI material, or generated-answer authority.

---

## Scope

`data/registry/flora/` is a domain-first routing lane for Flora registry material that already exists in the repository. Its current confirmed child is `sources/`, which documents source descriptor and source-admission records for Flora.

This parent README exists to prevent the domain-first path from becoming an unbounded parallel authority. It should route maintainers to the correct registry family and preserve the distinction between registry state and other KFM authority roots.

A Flora registry lane may point to or summarize governance state for:

- Flora source descriptors and source-admission records;
- source-role assignments and source-family posture;
- rights, sensitivity, geoprivacy, cadence, source-head, activation, intake, correction, and supersession state;
- rare-plant, culturally sensitive plant knowledge, steward-controlled, taxonomy-collision, rights-unclear, and join-induced sensitivity blockers;
- links to lifecycle payloads under RAW, WORK, QUARANTINE, PROCESSED, CATALOG/TRIPLET, and PUBLISHED phases;
- links to contracts, schemas, policies, receipts, proofs, catalog records, release candidates, correction notices, and rollback cards.

It must not contain source payloads, exact sensitive plant locations, culturally sensitive plant knowledge, proof packs, catalog records, release manifests, public map artifacts, or generated-answer carriers.

---

## Path posture

The requested and existing parent lane is:

```text
data/registry/flora/
```

This is a **domain-first** registry path. Current Flora source-registry evidence also supports a **subtype-first** source registry pattern:

```text
data/registry/sources/flora/
```

Other registry parents in this sequence use subtype-first lanes such as:

```text
data/registry/domains/
data/registry/datasets/
data/registry/crosswalks/
```

Therefore, `data/registry/flora/` is treated as **CONFIRMED path presence / NEEDS VERIFICATION topology**. Until an ADR, Directory Rules update, registry README, migration note, or repository-wide inventory resolves the topology, do not create duplicate authoritative records in both domain-first and subtype-first locations.

---

## Repo fit

| Responsibility | Home | Boundary |
|---|---|---|
| Flora domain-first registry parent | `data/registry/flora/` | Routing/compatibility parent for existing domain-first registry lanes. |
| Confirmed Flora child registry lane | `data/registry/flora/sources/` | Source descriptor/admission records, with topology warning. |
| Cross-domain source registry parent | `data/registry/sources/README.md` | General source registry doctrine and subtype-first source registry pattern. |
| Potential canonical Flora source lane | `data/registry/sources/flora/` | Named by Flora source-registry doctrine as machine-readable registry lane; needs topology reconciliation with this path. |
| Flora dataset registry records | `data/registry/datasets/flora/` | Dataset identity and dataset-state records. |
| Domain registry records | `data/registry/domains/` | Domain-state records; do not duplicate here without topology decision. |
| Crosswalk registry records | `data/registry/crosswalks/` | Mapping state across source IDs, authority IDs, fields, taxa, and vocabularies. |
| Flora source payloads | `data/raw/flora/`, `data/work/flora/`, `data/quarantine/flora/`, `data/processed/flora/` | Actual data belongs in lifecycle lanes, not registry parent files. |
| Flora semantic meaning | `contracts/domains/flora/` | Object-family meaning and invariants. |
| Flora machine shape | `schemas/contracts/v1/source/`, `schemas/contracts/v1/domains/flora/` | Schema enforcement; paths remain NEEDS VERIFICATION until inspected. |
| Flora policy and sensitivity | `policy/domains/flora/`, `policy/sensitivity/`, `policy/geoprivacy/`, `policy/rights/` | Exposure, rights, geoprivacy, source-role, and admissibility rules. |
| Flora validation receipts | `data/receipts/validation/flora/` | Process memory for validation checks. |
| Flora proof/evidence | `data/proofs/` or accepted proof lanes | EvidenceBundle closure, proof packs, signatures, and citation validation. |
| Flora catalog projections | `data/catalog/domain/flora/`, `data/catalog/stac/flora/`, STAC/DCAT/PROV lanes, and triplet lanes | Catalog/discovery carriers after catalog closure. |
| Flora release decisions | `release/` | Promotion, correction, rollback, supersession, withdrawal, and release manifests. |
| Public surfaces | governed APIs and released artifacts only | Public clients do not read this registry parent directly. |

---

## Confirmed child lanes

This confirms only path/README evidence. It does not prove emitted records, schemas, validators, fixtures, CI enforcement, signing, release integration, correction hooks, rollback hooks, governed API behavior, or public-safe summaries.

| Child lane | Status | Purpose | Boundary |
|---|---:|---|---|
| [`sources/`](sources/README.md) | CONFIRMED README | Domain-first Flora source descriptor and source-admission registry lane. | Not source payload storage, botanical truth, proof, receipt storage, catalog closure, semantic contract authority, policy, release authority, or public output. |

---

## Flora registry boundary

| Rule | Handling |
|---|---|
| Registry parent is routing state | This parent orients to child registry lanes; it does not contain domain payloads. |
| Topology is unresolved | Do not silently duplicate records between `data/registry/flora/...` and subtype-first lanes such as `data/registry/sources/flora/`. |
| Source role is preserved | Flora registry state must not upgrade observed, regulatory, modeled, aggregate, administrative, candidate, synthetic, context, or restricted source roles. |
| Rare/sensitive plant data fail closed | Exact rare/protected/culturally sensitive plant locations, culturally sensitive plant knowledge, steward-controlled records, taxonomy collisions, rights-unclear feeds, and join-induced sensitivity are denied, restricted, or quarantined unless policy/review/redaction gates explicitly permit a public-safe derivative. |
| Context is not Flora truth | Soil, hydrology, habitat, land cover, roads, settlements, archaeology, and similar context sources support governed joins only. |
| Watchers are non-publishers | Source-health, source-head, and drift watchers may create candidate intake records; they must not write directly to processed, catalog, published, or public surfaces. |
| Registry is not validation | Validation receipts and run receipts remain separate process-memory objects. |
| Registry is not proof | EvidenceBundle/proof support remains separate. |
| Registry is not catalog | STAC/DCAT/PROV/domain catalog records and graph projections live under catalog/triplet lanes. |
| Registry is not release | Public exposure requires validation, policy, review, proof/catalog support, release manifest, correction path, and rollback path. |
| Public clients do not read this lane | Public UI/API surfaces consume governed APIs, released artifacts, catalog/triplet/proof-backed responses, and policy-safe envelopes. |

---

## Accepted material

Accepted content is limited to README/routing material and registry-local sidecars that do not duplicate authority from subtype-first lanes:

- parent README and routing notes;
- compatibility notes explaining the domain-first versus subtype-first topology;
- migration notes, redirect notes, rollback notes, or topology decision notes;
- local indexes that point to child registry lanes without becoming authoritative records themselves;
- checksums, manifests, and signatures for registry routing material where applicable;
- pointers to source descriptors, dataset registry records, crosswalk registry records, domain registry records, contracts, schemas, policy refs, lifecycle payloads, validation receipts, proof refs, catalog refs, release candidates, correction notices, supersession notices, withdrawal notices, and rollback cards.

If a child lane under this parent stores actual registry records, it must state whether it is canonical, compatibility, migration-only, or mirrored, and it must name its conflict/rollback path.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw Flora source payloads, herbarium archives, occurrence exports, taxonomy tables, rare-plant feeds, vegetation datasets, invasive records, phenology feeds, restoration records, remote-sensing scenes, rasters, shapefiles, GeoParquet, COG, PMTiles, or source-native tables | `data/raw/flora/`, `data/work/flora/`, `data/quarantine/flora/`, or `data/processed/flora/` depending on lifecycle state |
| Exact rare/protected/culturally sensitive plant coordinates, steward-only notes, private identifiers, tokens, credentials, API keys, or culturally sensitive plant knowledge | restricted lifecycle lane, quarantine, secret manager, or governed restricted storage |
| Human-facing bibliography or source narrative | `docs/domains/flora/`, `docs/sources/`, or source catalog docs |
| Canonical source descriptor records if `data/registry/sources/flora/` is accepted as canonical | `data/registry/sources/flora/` after topology reconciliation |
| Dataset identity records | `data/registry/datasets/` and `data/registry/datasets/flora/` |
| Crosswalk mapping records | `data/registry/crosswalks/` |
| Domain-state records | `data/registry/domains/` |
| Semantic object contracts | `contracts/domains/flora/` |
| JSON Schema | `schemas/contracts/v1/source/` or `schemas/contracts/v1/domains/flora/` |
| Policy rules, sensitivity rules, geoprivacy rules, rights rules, access-control logic, or release rules | `policy/` |
| Validation receipts, run receipts, redaction receipts, policy receipts, review receipts, or process-memory logs | `data/receipts/` |
| EvidenceBundle records, proof packs, signatures, or citation-validation closure | `data/proofs/` |
| STAC/DCAT/PROV/domain catalog records or graph/triplet projections | `data/catalog/` and `data/triplets/` |
| Published Flora layers, reports, dashboards, tiles, API payloads, or generated-answer carriers | `data/published/`, governed app/API roots, and release-approved public artifact lanes |
| ReleaseManifest, PromotionDecision, CorrectionNotice, RollbackCard, withdrawal notice, or supersession notice | `release/` |
| Validator code, connector code, pipelines, fixtures, tests, or CI workflows | `tools/`, `connectors/`, `pipelines/`, `fixtures/`, `tests/`, `.github/workflows/` |

---

## Suggested directory shape

The map below is **PROPOSED** documentation guidance, not proof that child folders or records exist beyond confirmed README evidence.

```text
data/registry/flora/
├── README.md
├── sources/
│   └── README.md
└── index.local.json
```

If subtype-first lanes are accepted as canonical, prefer a migration such as:

```text
data/registry/sources/flora/       # canonical source descriptors
data/registry/flora/README.md      # compatibility pointer / migration note only
```

Do not maintain two divergent descriptor sets.

---

## Required checks before use

- [ ] Confirm whether `data/registry/flora/...` or subtype-first lanes such as `data/registry/sources/flora/` are canonical before adding real registry payloads.
- [ ] Confirm a child object is a registry record, not source data, proof, receipt, catalog record, release decision, policy, schema, validator, fixture, or test.
- [ ] Confirm source identity, source role, rights posture, terms, cadence, source head, access posture, steward, and authority limits are preserved for any source-registry child records.
- [ ] Confirm registry state does not upgrade source role, evidence strength, review state, catalog state, release state, or public-safe posture.
- [ ] Confirm sensitive details are not exposed in registry files, local indexes, or public summaries.
- [ ] Confirm exact rare/protected/culturally sensitive plant locations, steward-controlled records, culturally sensitive plant knowledge, taxonomy collisions, rights-unclear feeds, and join-induced sensitivity fail closed when unresolved.
- [ ] Confirm context sources are marked as context/join support and never treated as Flora truth.
- [ ] Confirm validation receipts exist before catalog or release eligibility is asserted.
- [ ] Confirm EvidenceRef/EvidenceBundle and proof refs exist for consequential use.
- [ ] Confirm catalog refs point to STAC/DCAT/PROV/domain catalog records rather than embedding them.
- [ ] Confirm release refs point to ReleaseManifest/PromotionDecision objects rather than implying publication from registry state.
- [ ] Confirm correction, supersession, withdrawal, stale-state, and rollback paths exist for mutable or externally governed Flora source material.
- [ ] Confirm no public client, map layer, graph edge, vector index, generated answer, report, or dashboard reads this registry parent as direct public truth.

---

## Status notes

| Claim | Status |
|---|---:|
| This README replaces the greenfield stub at `data/registry/flora/README.md`. | CONFIRMED authored |
| The target path existed in the live repository as a greenfield stub before this edit. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/flora/sources/README.md` exists as a confirmed child lane. | CONFIRMED by GitHub contents API during this edit |
| The Flora child `sources/` README marks the domain-first path as confirmed but layout-NEEDS VERIFICATION against `data/registry/sources/flora/`. | CONFIRMED by GitHub contents API during this edit |
| Flora source-registry doctrine names `data/registry/sources/flora/` as the machine-readable registry lane and treats the docs file as human-readable doctrine. | CONFIRMED by GitHub contents API in this sequence |
| Flora lifecycle docs require RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED and place watchers/source-head checks at the pre-RAW edge. | CONFIRMED by GitHub contents API in this sequence |
| Flora lifecycle docs identify rare-plant exact geometry, rights-unclear feeds, taxonomy collisions, and join-induced sensitivity as quarantine concerns. | CONFIRMED by GitHub contents API in this sequence |
| Concrete Flora registry payloads exist under this parent lane. | UNKNOWN |
| The final accepted topology between domain-first and subtype-first registry lanes is resolved. | NEEDS VERIFICATION |
| CI validates Flora registry records. | UNKNOWN |
| This README grants public access to Flora registry internals. | DENY |

---

## Maintainer note

This parent exists because the repository already has a domain-first Flora registry lane. Keep it useful but constrained. The safe chain is:

```text
registry pointer -> canonical registry record -> lifecycle payload -> validation receipt -> proof/catalog/policy/review -> release -> governed public surface
```

Never collapse it into:

```text
registry parent -> public Flora truth
```
