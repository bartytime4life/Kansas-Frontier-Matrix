<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/fauna/readme
name: Fauna Registry README
path: data/registry/fauna/README.md
type: data-registry-fauna-parent-readme
version: v0.2.0
status: draft
owners:
  - <registry-steward>
  - <fauna-domain-steward>
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
registry_scope: fauna-domain-first-registry-parent
domain: fauna
path_posture: existing-parent-stub-replaced; sources-child-lane-confirmed; domain-first-registry-path-exists; canonical-subtype-first-topology-needs-verification
sensitivity_posture: registry-internal; no-public-path; deny-by-default-sensitive-sites; source-role-preserving; evidence-aware; rights-aware; policy-aware; release-blocked-until-gates-close
related:
  - ../README.md
  - ../sources/README.md
  - ../sources/fauna/
  - ../datasets/README.md
  - ../domains/README.md
  - ../crosswalks/README.md
  - sources/README.md
  - ../../raw/fauna/
  - ../../work/fauna/
  - ../../quarantine/fauna/
  - ../../processed/fauna/
  - ../../catalog/domain/fauna/
  - ../../receipts/
  - ../../proofs/
  - ../../../docs/domains/fauna/SOURCE_REGISTRY.md
  - ../../../docs/domains/fauna/SOURCE_ROLES.md
  - ../../../docs/domains/fauna/SOURCE_FAMILIES.md
  - ../../../docs/domains/fauna/DATA_LIFECYCLE.md
  - ../../../docs/domains/fauna/SENSITIVITY.md
  - ../../../contracts/domains/fauna/
  - ../../../schemas/contracts/v1/source/
  - ../../../schemas/contracts/v1/domains/fauna/
  - ../../../policy/domains/fauna/
  - ../../../release/
tags:
  - kfm
  - data
  - registry
  - fauna
  - domain-first-registry
  - sources
  - source-descriptor
  - source-role
  - rights
  - sensitivity
  - geoprivacy
  - evidence
  - provenance
  - release-gated
  - no-public-path
notes:
  - "This README replaces the greenfield stub at `data/registry/fauna/README.md`."
  - "This domain-first registry parent exists in the repository and currently has a confirmed `sources/` child README."
  - "The inspected source-registry doctrine also names `data/registry/sources/fauna/` as the machine-readable source registry lane. Therefore this parent is treated as a compatibility/routing lane until registry topology is reconciled."
  - "Fauna exact occurrence geometry, nests, dens, roosts, hibernacula, spawning sites, and steward-controlled records remain deny-by-default until governed redaction/review/release gates close."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Fauna Registry

Domain-first registry parent for Fauna registry lanes.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: registry" src="https://img.shields.io/badge/family-registry-blueviolet">
  <img alt="Domain: fauna" src="https://img.shields.io/badge/domain-fauna-2e8b57">
  <img alt="Topology: needs verification" src="https://img.shields.io/badge/topology-NEEDS%20VERIFICATION-orange">
  <img alt="Boundary: not source data" src="https://img.shields.io/badge/boundary-not%20source%20data-critical">
  <img alt="Exposure: no public path" src="https://img.shields.io/badge/exposure-no%20public%20path-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Confirmed child lanes](#confirmed-child-lanes) · [Fauna registry boundary](#fauna-registry-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Suggested directory shape](#suggested-directory-shape) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/registry/fauna/` is a domain-first registry parent. It is not RAW source storage, WORK staging, QUARANTINE, PROCESSED data, catalog output, proof storage, receipt storage, semantic contract authority, schema authority, policy, release authority, public API/UI material, or generated-answer authority.

---

## Scope

`data/registry/fauna/` is a domain-first routing lane for Fauna registry material that already exists in the repository. Its current confirmed child is `sources/`, which documents source descriptor and source-admission records for Fauna.

This parent README exists to prevent the domain-first path from becoming an unbounded parallel authority. It should route maintainers to the correct registry family and preserve the distinction between registry state and other KFM authority roots.

A Fauna registry lane may point to or summarize governance state for:

- Fauna source descriptors and source-admission records;
- source-role assignments and source-family posture;
- rights, sensitivity, geoprivacy, cadence, source-head, activation, intake, correction, and supersession state;
- links to lifecycle payloads under RAW, WORK, QUARANTINE, PROCESSED, CATALOG/TRIPLET, and PUBLISHED phases;
- links to contracts, schemas, policies, receipts, proofs, catalog records, release candidates, correction notices, and rollback cards.

It must not contain source payloads, exact sensitive animal locations, proof packs, catalog records, release manifests, public map artifacts, or generated-answer carriers.

---

## Path posture

The requested and existing parent lane is:

```text
data/registry/fauna/
```

This is a **domain-first** registry path. Current source-registry evidence also supports a **subtype-first** source registry pattern:

```text
data/registry/sources/fauna/
```

Other registry parents in this sequence use subtype-first lanes such as:

```text
data/registry/domains/
data/registry/datasets/
data/registry/crosswalks/
```

Therefore, `data/registry/fauna/` is treated as **CONFIRMED path presence / NEEDS VERIFICATION topology**. Until an ADR, Directory Rules update, registry README, migration note, or repository-wide inventory resolves the topology, do not create duplicate authoritative records in both domain-first and subtype-first locations.

---

## Repo fit

| Responsibility | Home | Boundary |
|---|---|---|
| Fauna domain-first registry parent | `data/registry/fauna/` | Routing/compatibility parent for existing domain-first registry lanes. |
| Confirmed Fauna child registry lane | `data/registry/fauna/sources/` | Source descriptor/admission records, with topology warning. |
| Cross-domain source registry parent | `data/registry/sources/README.md` | General source registry doctrine and subtype-first source registry pattern. |
| Potential canonical Fauna source lane | `data/registry/sources/fauna/` | Named by Fauna source-registry doctrine as machine-readable registry lane; needs topology reconciliation with this path. |
| Dataset registry records | `data/registry/datasets/` | Dataset identity and dataset-state records. |
| Domain registry records | `data/registry/domains/` | Domain-state records; do not duplicate here without topology decision. |
| Crosswalk registry records | `data/registry/crosswalks/` | Mapping state across source IDs, authority IDs, fields, and vocabularies. |
| Fauna source payloads | `data/raw/fauna/`, `data/work/fauna/`, `data/quarantine/fauna/`, `data/processed/fauna/` | Actual data belongs in lifecycle lanes, not registry parent files. |
| Fauna semantic meaning | `contracts/domains/fauna/` | Object-family meaning and invariants. |
| Fauna machine shape | `schemas/contracts/v1/source/`, `schemas/contracts/v1/domains/fauna/` | Schema enforcement; paths remain NEEDS VERIFICATION until inspected. |
| Fauna policy and sensitivity | `policy/domains/fauna/`, `policy/sensitivity/`, `policy/geoprivacy/`, `policy/rights/` | Exposure, rights, geoprivacy, source-role, and admissibility rules. |
| Fauna validation receipts | `data/receipts/validation/fauna/` if/when accepted | Process memory for validation checks. |
| Fauna proof/evidence | `data/proofs/` or accepted proof lanes | EvidenceBundle closure, proof packs, signatures, and citation validation. |
| Fauna catalog projections | `data/catalog/domain/fauna/`, STAC/DCAT/PROV lanes, and triplet lanes | Catalog/discovery carriers after catalog closure. |
| Fauna release decisions | `release/` | Promotion, correction, rollback, supersession, withdrawal, and release manifests. |
| Public surfaces | governed APIs and released artifacts only | Public clients do not read this registry parent directly. |

---

## Confirmed child lanes

This confirms only path/README evidence. It does not prove emitted records, schemas, validators, fixtures, CI enforcement, signing, release integration, correction hooks, rollback hooks, governed API behavior, or public-safe summaries.

| Child lane | Status | Purpose | Boundary |
|---|---:|---|---|
| [`sources/`](sources/README.md) | CONFIRMED README | Domain-first Fauna source descriptor and source-admission registry lane. | Not source payload storage, animal truth, proof, receipt storage, catalog closure, semantic contract authority, policy, release authority, or public output. |

---

## Fauna registry boundary

| Rule | Handling |
|---|---|
| Registry parent is routing state | This parent orients to child registry lanes; it does not contain domain payloads. |
| Topology is unresolved | Do not silently duplicate records between `data/registry/fauna/...` and subtype-first lanes such as `data/registry/sources/fauna/`. |
| Source role is preserved | Fauna registry state must not upgrade observed, regulatory, modeled, aggregate, administrative, candidate, synthetic, context, or restricted source roles. |
| Sensitive sites fail closed | Exact occurrence geometry, nests, dens, roosts, hibernacula, spawning sites, breeding sites, and steward-controlled records are denied or restricted unless policy/review/redaction gates explicitly permit a public-safe derivative. |
| Context is not Fauna truth | Habitat, soil, hydrology, land cover, PAD-US, NWI, roads, settlements, and similar context sources support governed joins only. |
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
| Raw Fauna source payloads, occurrence downloads, telemetry feeds, disease surveillance data, mortality reports, acoustic files, eDNA results, rasters, shapefiles, GeoParquet, COG, PMTiles, or source-native tables | `data/raw/fauna/`, `data/work/fauna/`, `data/quarantine/fauna/`, or `data/processed/fauna/` depending on lifecycle state |
| Exact sensitive coordinates, nests, dens, roosts, hibernacula, spawning sites, breeding sites, private identifiers, steward-only notes, tokens, credentials, or API keys | restricted lifecycle lane, quarantine, secret manager, or governed restricted storage |
| Human-facing bibliography or source narrative | `docs/domains/fauna/`, `docs/sources/`, or source catalog docs |
| Canonical source descriptor records if `data/registry/sources/fauna/` is accepted as canonical | `data/registry/sources/fauna/` after topology reconciliation |
| Dataset identity records | `data/registry/datasets/` |
| Crosswalk mapping records | `data/registry/crosswalks/` |
| Domain-state records | `data/registry/domains/` |
| Semantic object contracts | `contracts/domains/fauna/` |
| JSON Schema | `schemas/contracts/v1/source/` or `schemas/contracts/v1/domains/fauna/` |
| Policy rules, sensitivity rules, geoprivacy rules, rights rules, access-control logic, or release rules | `policy/` |
| Validation receipts, run receipts, redaction receipts, policy receipts, review receipts, or process-memory logs | `data/receipts/` |
| EvidenceBundle records, proof packs, signatures, or citation-validation closure | `data/proofs/` |
| STAC/DCAT/PROV/domain catalog records or graph/triplet projections | `data/catalog/` and `data/triplets/` |
| Published Fauna layers, reports, dashboards, tiles, API payloads, or generated-answer carriers | `data/published/`, governed app/API roots, and release-approved public artifact lanes |
| ReleaseManifest, PromotionDecision, CorrectionNotice, RollbackCard, withdrawal notice, or supersession notice | `release/` |
| Validator code, connector code, pipelines, fixtures, tests, or CI workflows | `tools/`, `connectors/`, `pipelines/`, `fixtures/`, `tests/`, `.github/workflows/` |

---

## Suggested directory shape

The map below is **PROPOSED** documentation guidance, not proof that child folders or records exist beyond confirmed README evidence.

```text
data/registry/fauna/
├── README.md
├── sources/
│   └── README.md
└── index.local.json
```

If subtype-first lanes are accepted as canonical, prefer a migration such as:

```text
data/registry/sources/fauna/       # canonical source descriptors
data/registry/fauna/README.md      # compatibility pointer / migration note only
```

Do not maintain two divergent descriptor sets.

---

## Required checks before use

- [ ] Confirm whether `data/registry/fauna/...` or subtype-first lanes such as `data/registry/sources/fauna/` are canonical before adding real registry payloads.
- [ ] Confirm a child object is a registry record, not source data, proof, receipt, catalog record, release decision, policy, schema, validator, fixture, or test.
- [ ] Confirm source identity, source role, rights posture, terms, cadence, source head, access posture, steward, and authority limits are preserved for any source-registry child records.
- [ ] Confirm registry state does not upgrade source role, evidence strength, review state, catalog state, release state, or public-safe posture.
- [ ] Confirm sensitive details are not exposed in registry files, local indexes, or public summaries.
- [ ] Confirm nests, dens, roosts, hibernacula, spawning sites, exact sensitive occurrence geometry, and steward-controlled records fail closed when unresolved.
- [ ] Confirm context sources are marked as context/join support and never treated as Fauna truth.
- [ ] Confirm validation receipts exist before catalog or release eligibility is asserted.
- [ ] Confirm EvidenceRef/EvidenceBundle and proof refs exist for consequential use.
- [ ] Confirm catalog refs point to STAC/DCAT/PROV/domain catalog records rather than embedding them.
- [ ] Confirm release refs point to ReleaseManifest/PromotionDecision objects rather than implying publication from registry state.
- [ ] Confirm correction, supersession, withdrawal, stale-state, and rollback paths exist for mutable or externally governed Fauna source material.
- [ ] Confirm no public client, map layer, graph edge, vector index, generated answer, report, or dashboard reads this registry parent as direct public truth.

---

## Status notes

| Claim | Status |
|---|---:|
| This README replaces the greenfield stub at `data/registry/fauna/README.md`. | CONFIRMED authored |
| The target path existed in the live repository as a greenfield stub before this edit. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/fauna/sources/README.md` exists as a confirmed child lane. | CONFIRMED by GitHub contents API during this edit |
| The Fauna child `sources/` README marks the domain-first path as confirmed but layout-NEEDS VERIFICATION against `data/registry/sources/fauna/`. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/sources/README.md` exists and defines the source registry as an admission and authority-control surface, not a bibliography. | CONFIRMED by GitHub contents API in this sequence |
| Fauna source-registry doctrine names `data/registry/sources/fauna/` as the machine-readable registry lane and treats the docs file as human-facing orientation. | CONFIRMED by GitHub contents API in this sequence |
| Fauna lifecycle docs require SourceDescriptor at RAW admission and deny-by-default handling for sensitive sites. | CONFIRMED by GitHub contents API in this sequence |
| Concrete Fauna registry payloads exist under this parent lane. | UNKNOWN |
| The final accepted topology between domain-first and subtype-first registry lanes is resolved. | NEEDS VERIFICATION |
| CI validates Fauna registry records. | UNKNOWN |
| This README grants public access to Fauna registry internals. | DENY |

---

## Maintainer note

This parent exists because the repository already has a domain-first Fauna registry lane. Keep it useful but constrained. The safe chain is:

```text
registry pointer -> canonical registry record -> lifecycle payload -> validation receipt -> proof/catalog/policy/review -> release -> governed public surface
```

Never collapse it into:

```text
registry parent -> public Fauna truth
```
