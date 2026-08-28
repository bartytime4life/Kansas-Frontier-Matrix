<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/habitat/readme
name: Habitat Registry README
path: data/registry/habitat/README.md
type: data-registry-habitat-parent-readme
version: v0.2.0
status: draft
owners:
  - <registry-steward>
  - <habitat-domain-steward>
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
registry_scope: habitat-domain-first-registry-parent
domain: habitat
path_posture: existing-parent-stub-replaced; sources-child-lane-confirmed; domain-first-registry-path-exists; canonical-subtype-first-topology-needs-verification
sensitivity_posture: registry-internal; no-public-path; sensitive-joins-fail-closed; source-role-preserving; evidence-aware; rights-aware; policy-aware; release-blocked-until-gates-close
related:
  - ../README.md
  - ../sources/README.md
  - ../sources/habitat/
  - ../datasets/README.md
  - ../domains/README.md
  - ../crosswalks/README.md
  - sources/README.md
  - ../../raw/habitat/
  - ../../work/habitat/
  - ../../quarantine/habitat/
  - ../../processed/habitat/
  - ../../catalog/domain/habitat/
  - ../../receipts/
  - ../../proofs/
  - ../../../docs/domains/habitat/SOURCE_REGISTRY.md
  - ../../../docs/domains/habitat/HABITAT_SOURCE_LEDGER.md
  - ../../../docs/domains/habitat/SOURCES.md
  - ../../../docs/domains/habitat/SOURCE_FAMILIES.md
  - ../../../docs/domains/habitat/DATA_LIFECYCLE.md
  - ../../../docs/domains/habitat/ARCHITECTURE.md
  - ../../../contracts/domains/habitat/
  - ../../../schemas/contracts/v1/source/
  - ../../../schemas/contracts/v1/domains/habitat/
  - ../../../policy/domains/habitat/
  - ../../../release/
tags:
  - kfm
  - data
  - registry
  - habitat
  - domain-first-registry
  - sources
  - source-descriptor
  - source-role
  - rights
  - sensitivity
  - geoprivacy
  - land-cover
  - wetlands
  - stewardship
  - ecological-systems
  - critical-habitat
  - occurrence-context
  - evidence
  - provenance
  - release-gated
  - no-public-path
notes:
  - "This README replaces the greenfield stub at `data/registry/habitat/README.md`."
  - "This domain-first registry parent exists in the repository and currently has a confirmed `sources/` child README."
  - "The inspected Habitat source-registry doctrine names `data/registry/sources/habitat/` as the machine-readable source registry lane and flags the path-form question. Therefore this parent is treated as a compatibility/routing lane until registry topology is reconciled."
  - "Sensitive joins, occurrence-context inputs, controlled ecological records, rights-unclear feeds, and source-role conflicts remain fail-closed until governed redaction/review/release gates close."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Habitat Registry

Domain-first registry parent for Habitat registry lanes.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: registry" src="https://img.shields.io/badge/family-registry-blueviolet">
  <img alt="Domain: habitat" src="https://img.shields.io/badge/domain-habitat-2e7d32">
  <img alt="Topology: needs verification" src="https://img.shields.io/badge/topology-NEEDS%20VERIFICATION-orange">
  <img alt="Boundary: not source data" src="https://img.shields.io/badge/boundary-not%20source%20data-critical">
  <img alt="Exposure: no public path" src="https://img.shields.io/badge/exposure-no%20public%20path-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Confirmed child lanes](#confirmed-child-lanes) · [Habitat registry boundary](#habitat-registry-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Suggested directory shape](#suggested-directory-shape) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/registry/habitat/` is a domain-first registry parent. It is not RAW source storage, WORK staging, QUARANTINE, PROCESSED data, catalog output, proof storage, receipt storage, semantic contract authority, schema authority, policy, release authority, public API/UI material, or generated-answer authority.

---

## Scope

`data/registry/habitat/` is a domain-first routing lane for Habitat registry material that already exists in the repository. Its current confirmed child is `sources/`, which documents source descriptor and source-admission records for the Habitat lane.

This parent README exists to prevent the domain-first path from becoming an unbounded parallel authority. It should route maintainers to the correct registry family and preserve the distinction between registry state and other KFM authority roots.

A Habitat registry lane may point to or summarize governance state for:

- Habitat source descriptors and source-admission records;
- source-role assignments and source-family posture;
- rights, sensitivity, cadence, source-head, activation, intake, correction, and supersession state;
- sensitive-join, occurrence-context, controlled ecological, rights-unclear, and source-role conflict blockers;
- links to lifecycle payloads under RAW, WORK, QUARANTINE, PROCESSED, CATALOG/TRIPLET, and PUBLISHED phases;
- links to contracts, schemas, policies, receipts, proofs, catalog records, release candidates, correction notices, and rollback cards.

It must not contain source payloads, sensitive joined details, proof packs, catalog records, release manifests, public map artifacts, or generated-answer carriers.

---

## Path posture

The requested and existing parent lane is:

```text
data/registry/habitat/
```

This is a **domain-first** registry path. Current Habitat source-registry evidence also supports a **subtype-first** source registry pattern:

```text
data/registry/sources/habitat/
```

Habitat source-registry doctrine explicitly notes the `sources/habitat` versus `habitat` path-form question. Other registry parents in this sequence use subtype-first lanes such as:

```text
data/registry/domains/
data/registry/datasets/
data/registry/crosswalks/
```

Therefore, `data/registry/habitat/` is treated as **CONFIRMED path presence / NEEDS VERIFICATION topology**. Until an ADR, Directory Rules update, registry README, migration note, or repository-wide inventory resolves the topology, do not create duplicate authoritative records in both domain-first and subtype-first locations.

---

## Repo fit

| Responsibility | Home | Boundary |
|---|---|---|
| Habitat domain-first registry parent | `data/registry/habitat/` | Routing/compatibility parent for existing domain-first registry lanes. |
| Confirmed Habitat child registry lane | `data/registry/habitat/sources/` | Source descriptor/admission records, with topology warning. |
| Cross-domain source registry parent | `data/registry/sources/README.md` | General source registry doctrine and subtype-first source registry pattern. |
| Potential canonical Habitat source lane | `data/registry/sources/habitat/` | Named by Habitat source-registry doctrine as machine-readable registry lane; needs topology reconciliation with this path. |
| Dataset registry records | `data/registry/datasets/` | Dataset identity and dataset-state records. |
| Domain registry records | `data/registry/domains/` | Domain-state records; do not duplicate here without topology decision. |
| Crosswalk registry records | `data/registry/crosswalks/` | Mapping state across source IDs, authority IDs, class systems, fields, and vocabularies. |
| Habitat source payloads | `data/raw/habitat/`, `data/work/habitat/`, `data/quarantine/habitat/`, `data/processed/habitat/` | Actual data belongs in lifecycle lanes, not registry parent files. |
| Habitat semantic meaning | `contracts/domains/habitat/` | Object-family meaning and invariants. |
| Habitat machine shape | `schemas/contracts/v1/source/`, `schemas/contracts/v1/domains/habitat/` | Schema enforcement; paths remain NEEDS VERIFICATION until inspected. |
| Habitat policy and sensitivity | `policy/domains/habitat/`, `policy/sensitivity/`, `policy/geoprivacy/`, `policy/rights/` | Exposure, rights, source-role, join sensitivity, and admissibility rules. |
| Habitat validation receipts | `data/receipts/validation/habitat/` if/when accepted | Process memory for validation checks. |
| Habitat proof/evidence | `data/proofs/` or accepted proof lanes | EvidenceBundle closure, proof packs, signatures, and citation validation. |
| Habitat catalog projections | `data/catalog/domain/habitat/`, STAC/DCAT/PROV lanes, and triplet lanes | Catalog/discovery carriers after catalog closure. |
| Habitat release decisions | `release/` | Promotion, correction, rollback, supersession, withdrawal, and release manifests. |
| Public surfaces | governed APIs and released artifacts only | Public clients do not read this registry parent directly. |

---

## Confirmed child lanes

This confirms only path/README evidence. It does not prove emitted records, schemas, validators, fixtures, CI enforcement, signing, release integration, correction hooks, rollback hooks, governed API behavior, or public-safe summaries.

| Child lane | Status | Purpose | Boundary |
|---|---:|---|---|
| [`sources/`](sources/README.md) | CONFIRMED README | Domain-first Habitat source descriptor and source-admission registry lane. | Not source payload storage, habitat truth, proof, receipt storage, catalog closure, semantic contract authority, policy, release authority, or public output. |

---

## Habitat registry boundary

| Rule | Handling |
|---|---|
| Registry parent is routing state | This parent orients to child registry lanes; it does not contain domain payloads. |
| Topology is unresolved | Do not silently duplicate records between `data/registry/habitat/...` and subtype-first lanes such as `data/registry/sources/habitat/`. |
| Source role is preserved | Habitat registry state must not upgrade observed, regulatory, modeled, aggregate, administrative, candidate, synthetic, context, or restricted source roles. |
| Habitat does not own occurrence truth | Occurrence aggregators and Flora/Fauna occurrence records are join context unless the owning lane releases a public-safe derivative. |
| Sensitive joins fail closed | Public-safe habitat context can become restricted when joined to sensitive Flora/Fauna, heritage, stewardship, or other protected context. The most restrictive joined tier governs. |
| Regulatory and modeled products remain scoped | Critical-habitat designations, wetland inventories, modeled suitability layers, and stewardship overlays must retain their source role and authority limits. |
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
| Raw Habitat source payloads, land-cover packages, wetland inventories, stewardship layers, ecological-system tables, remote-sensing products, field-survey files, model outputs, rasters, shapefiles, GeoParquet, COG, PMTiles, or source-native tables | `data/raw/habitat/`, `data/work/habitat/`, `data/quarantine/habitat/`, or `data/processed/habitat/` depending on lifecycle state |
| Sensitive joined context, protected occurrence-derived locations, steward-only notes, private identifiers, access secrets, or restricted review material | restricted lifecycle lane, quarantine, secret manager, or governed restricted storage |
| Human-facing bibliography or source narrative | `docs/domains/habitat/`, `docs/sources/`, or source catalog docs |
| Canonical source descriptor records if `data/registry/sources/habitat/` is accepted as canonical | `data/registry/sources/habitat/` after topology reconciliation |
| Dataset identity records | `data/registry/datasets/` |
| Crosswalk mapping records | `data/registry/crosswalks/` |
| Domain-state records | `data/registry/domains/` |
| Semantic object contracts | `contracts/domains/habitat/` |
| JSON Schema | `schemas/contracts/v1/source/` or `schemas/contracts/v1/domains/habitat/` |
| Policy rules, sensitivity rules, geoprivacy rules, rights rules, access-control logic, or release rules | `policy/` |
| Validation receipts, run receipts, redaction receipts, policy receipts, review receipts, or process-memory logs | `data/receipts/` |
| EvidenceBundle records, proof packs, signatures, or citation-validation closure | `data/proofs/` |
| STAC/DCAT/PROV/domain catalog records or graph/triplet projections | `data/catalog/` and `data/triplets/` |
| Published Habitat layers, reports, dashboards, tiles, API payloads, or generated-answer carriers | `data/published/`, governed app/API roots, and release-approved public artifact lanes |
| ReleaseManifest, PromotionDecision, CorrectionNotice, RollbackCard, withdrawal notice, or supersession notice | `release/` |
| Validator code, connector code, pipelines, fixtures, tests, or CI workflows | `tools/`, `connectors/`, `pipelines/`, `fixtures/`, `tests/`, `.github/workflows/` |

---

## Suggested directory shape

The map below is **PROPOSED** documentation guidance, not proof that child folders or records exist beyond confirmed README evidence.

```text
data/registry/habitat/
├── README.md
├── sources/
│   └── README.md
└── index.local.json
```

If subtype-first lanes are accepted as canonical, prefer a migration such as:

```text
data/registry/sources/habitat/       # canonical source descriptors
data/registry/habitat/README.md      # compatibility pointer / migration note only
```

Do not maintain two divergent descriptor sets.

---

## Required checks before use

- [ ] Confirm whether `data/registry/habitat/...` or subtype-first lanes such as `data/registry/sources/habitat/` are canonical before adding real registry payloads.
- [ ] Confirm a child object is a registry record, not source data, proof, receipt, catalog record, release decision, policy, schema, validator, fixture, or test.
- [ ] Confirm source identity, source role, rights posture, terms, cadence, source head, access posture, steward, and authority limits are preserved for any source-registry child records.
- [ ] Confirm registry state does not upgrade source role, evidence strength, review state, catalog state, release state, or public-safe posture.
- [ ] Confirm occurrence context, habitat context, regulatory designations, observed land-cover, modeled suitability, stewardship overlays, and aggregate products are not collapsed.
- [ ] Confirm sensitive joined details are not exposed in registry files, local indexes, or public summaries.
- [ ] Confirm joined products inherit the most restrictive applicable sensitivity posture and fail closed when unresolved.
- [ ] Confirm context sources are marked as context/join support and never treated as Habitat-owned truth beyond their admitted scope.
- [ ] Confirm validation receipts exist before catalog or release eligibility is asserted.
- [ ] Confirm EvidenceRef/EvidenceBundle and proof refs exist for consequential use.
- [ ] Confirm catalog refs point to STAC/DCAT/PROV/domain catalog records rather than embedding them.
- [ ] Confirm release refs point to ReleaseManifest/PromotionDecision objects rather than implying publication from registry state.
- [ ] Confirm correction, supersession, withdrawal, stale-state, and rollback paths exist for mutable or externally governed Habitat source material.
- [ ] Confirm no public client, map layer, graph edge, vector index, generated answer, report, or dashboard reads this registry parent as direct public truth.

---

## Status notes

| Claim | Status |
|---|---:|
| This README replaces the greenfield stub at `data/registry/habitat/README.md`. | CONFIRMED authored |
| The target path existed in the live repository as a greenfield stub before this edit. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/habitat/sources/README.md` exists as a confirmed child lane. | CONFIRMED by GitHub contents API during this edit |
| The Habitat child `sources/` README marks the domain-first path as confirmed but layout-NEEDS VERIFICATION against `data/registry/sources/habitat/`. | CONFIRMED by GitHub contents API during this edit |
| Habitat source-registry doctrine names `data/registry/sources/habitat/` as the machine-readable registry lane and notes the path-form question. | CONFIRMED by GitHub contents API in this sequence |
| Habitat source ledger states authoritative SourceDescriptor records live under `data/registry/sources/habitat/` and that admission is deny-by-default until descriptor and activation decision exist. | CONFIRMED by GitHub contents API in this sequence |
| Habitat source ledger describes occurrence aggregators as join context and warns joined products inherit the most restrictive applicable tier. | CONFIRMED by GitHub contents API in this sequence |
| Concrete Habitat registry payloads exist under this parent lane. | UNKNOWN |
| The final accepted topology between domain-first and subtype-first registry lanes is resolved. | NEEDS VERIFICATION |
| CI validates Habitat registry records. | UNKNOWN |
| This README grants public access to Habitat registry internals. | DENY |

---

## Maintainer note

This parent exists because the repository already has a domain-first Habitat registry lane. Keep it useful but constrained. The safe chain is:

```text
registry pointer -> canonical registry record -> lifecycle payload -> validation receipt -> proof/catalog/policy/review -> release -> governed public surface
```

Never collapse it into:

```text
registry parent -> public Habitat truth
```
