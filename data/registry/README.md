<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/readme
name: Data Registry README
path: data/registry/README.md
type: data-registry-root-readme
version: v0.2.0
status: draft
owners:
  - <registry-steward>
  - <source-steward>
  - <dataset-steward>
  - <domain-steward>
  - <crosswalk-steward>
  - <rights-steward>
  - <sensitivity-steward>
  - <layer-steward>
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
registry_scope: registry-root-and-family-routing
path_posture: existing-root-stub-replaced; major-registry-family-readmes-confirmed-for-sources-datasets-domains-crosswalks-rights-sensitivity-layers; domain-first-compatibility-lanes-exist-for-selected-domains; final-registry-taxonomy-needs-verification
sensitivity_posture: registry-internal; no-public-path; source-role-preserving; rights-and-sensitivity-fail-closed; evidence-aware; policy-aware; release-blocked-until-gates-close; public-clients-use-governed-interfaces-only
related:
  - sources/README.md
  - datasets/README.md
  - domains/README.md
  - crosswalks/README.md
  - rights/README.md
  - sensitivity/README.md
  - layers/README.md
  - roads-rail-trade/README.md
  - settlements-infrastructure/README.md
  - soil/README.md
  - flora/README.md
  - fauna/README.md
  - geology/README.md
  - habitat/README.md
  - hazards/README.md
  - hydrology/README.md
  - people-dna-land/README.md
  - ../raw/
  - ../work/
  - ../quarantine/
  - ../processed/
  - ../catalog/
  - ../triplets/
  - ../published/
  - ../receipts/
  - ../proofs/
  - ../../contracts/
  - ../../schemas/contracts/v1/
  - ../../policy/
  - ../../release/
  - ../../docs/architecture/directory-rules.md
  - ../../docs/doctrine/directory-rules.md
tags:
  - kfm
  - data
  - registry
  - registry-root
  - sources
  - datasets
  - domains
  - crosswalks
  - rights
  - sensitivity
  - layers
  - source-role
  - evidence
  - provenance
  - policy-aware
  - release-gated
  - rollback
  - no-public-path
notes:
  - "This README replaces the greenfield stub at `data/registry/README.md`."
  - "Registry records are governance/control records. They do not store source payloads, define semantic meaning, enforce schemas, decide policy, emit receipts, close proofs, close catalogs, or publish artifacts."
  - "Confirmed major registry-family READMEs during this edit: sources, datasets, domains, crosswalks, rights, sensitivity, and layers. This confirms README/path evidence only, not emitted registry payloads, schemas, validators, CI, runtime behavior, or public API behavior."
  - "Some domain-first registry compatibility/routing lanes also exist. Their final relationship to subtype-first registry families remains NEEDS VERIFICATION until topology is reconciled by ADR, Directory Rules update, migration note, or inventory."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Data Registry

Root governance lane for KFM registry records and registry-family routing.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Root: data" src="https://img.shields.io/badge/root-data%2F-0a7ea4">
  <img alt="Family: registry" src="https://img.shields.io/badge/family-registry-blueviolet">
  <img alt="Boundary: not source data" src="https://img.shields.io/badge/boundary-not%20source%20data-critical">
  <img alt="Boundary: not release" src="https://img.shields.io/badge/boundary-not%20release-critical">
  <img alt="Exposure: no public path" src="https://img.shields.io/badge/exposure-no%20public%20path-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Registry families](#registry-families) · [Domain-first compatibility lanes](#domain-first-compatibility-lanes) · [Registry boundary](#registry-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Suggested directory shape](#suggested-directory-shape) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/registry/` is a registry/control root for governed records that describe how KFM treats sources, datasets, domains, crosswalks, rights, sensitivity posture, layers, and selected compatibility lanes. It is not RAW source storage, WORK staging, QUARANTINE, PROCESSED data, catalog output, triplet output, published artifacts, proof storage, receipt storage, semantic contract authority, schema authority, policy, release authority, public API/UI material, or generated-answer authority.

---

## Scope

`data/registry/` is the data-side root for registry records: compact, auditable governance handles that help KFM decide what can be admitted, processed, linked, interpreted, reviewed, cataloged, released, corrected, superseded, withdrawn, or rolled back.

A registry record may point to:

- source descriptors and source-admission state;
- dataset identity and dataset-state records;
- domain-state records;
- crosswalk mapping records;
- rights-review state;
- sensitivity-review state;
- layer identity and layer-readiness records;
- lifecycle payloads under RAW, WORK, QUARANTINE, PROCESSED, CATALOG/TRIPLET, and PUBLISHED phases;
- contracts, schemas, policies, receipts, proofs, catalog records, release candidates, release manifests, correction notices, withdrawal notices, supersession notes, and rollback cards.

Registry records are **not** the same as the payloads or authorities they reference. They make state inspectable; they do not make claims true, sources usable, datasets public, mappings definitive, rights cleared, sensitivity resolved, layers rendered, catalogs closed, or releases approved.

---

## Path posture

The requested and existing root lane is:

```text
data/registry/
```

This README replaces a greenfield stub and documents the registry root only. It does not assert that every listed child lane has mature records, schemas, validators, fixtures, CI, runtime readers, governed API behavior, public UI behavior, or release wiring.

Several registry-family parents now exist as README-governed lanes:

```text
data/registry/sources/
data/registry/datasets/
data/registry/domains/
data/registry/crosswalks/
data/registry/rights/
data/registry/sensitivity/
data/registry/layers/
```

Some domain-first compatibility/routing lanes also exist, such as:

```text
data/registry/roads-rail-trade/
data/registry/settlements-infrastructure/
data/registry/soil/
```

Those domain-first paths are useful as current repo facts, but they must not create duplicate authority beside subtype-first registry families. Where both a domain-first and subtype-first path could apply, final topology remains **NEEDS VERIFICATION** until resolved by ADR, Directory Rules update, migration note, or repository inventory.

---

## Registry families

This table records current README/path evidence only. It does not prove emitted registry payloads or runtime enforcement.

| Registry family | Confirmed parent | Role | Boundary |
|---|---:|---|---|
| Source registry | `sources/README.md` | Pre-RAW admission and authority-control surface for sources and SourceDescriptor-style records. | Not raw data, schemas, policy decisions, receipts, proofs, releases, or bibliography. |
| Dataset registry | `datasets/README.md` | Dataset identity and dataset-state records. | Not dataset payloads, proof, policy, catalog closure, or release. |
| Domain registry | `domains/README.md` | Domain-state records, object-family coverage, source-family posture, blockers, and readiness. | Not domain payloads, source registry authority, contracts, schemas, policy, proof, or release. |
| Crosswalk registry | `crosswalks/README.md` | Mapping-state records across identifiers, vocabularies, fields, authority systems, and domain lanes. | Not semantic contracts, schemas, policy, validation output, proof, catalog closure, release, or public claims. |
| Rights registry | `rights/README.md` | Rights-review state, terms, attribution, redistribution posture, and release-readiness pointers. | Not legal advice, license authority, source payloads, policy, proof, catalog closure, or release. |
| Sensitivity registry | `sensitivity/README.md` | Sensitivity-review state, geoprivacy/redaction posture, blockers, and exposure-control pointers. | Not exact sensitive detail storage, policy, receipts, proofs, catalog closure, release, or public output. |
| Layer registry | `layers/README.md` | Layer identity, layer-family routing, domain-safe map-layer state, and release-readiness pointers. | Not layer bytes, tile storage, catalog output, proof, receipt storage, policy, release, public API/UI material, or generated answers. |

---

## Domain-first compatibility lanes

Domain-first lanes under `data/registry/<domain>/` should be treated as compatibility, routing, or transitional lanes unless an ADR or accepted registry contract says otherwise. They are useful when they make current repo state clearer, but they must not silently fork canonical records from subtype-first families.

Confirmed examples from the current README sequence include:

| Domain-first lane | Confirmed child/role | Topology posture |
|---|---|---|
| `data/registry/roads-rail-trade/` | Parent and `sources/` source-registry child. | CONFIRMED path presence / NEEDS VERIFICATION topology. |
| `data/registry/settlements-infrastructure/` | Parent and `sources/` source-registry child. | CONFIRMED path presence / NEEDS VERIFICATION topology. |
| `data/registry/soil/` | Parent and `sources/` source-registry child. | CONFIRMED path presence / NEEDS VERIFICATION topology. |

Other domain-first registry lanes may exist or be added later. Each must state whether it is canonical, compatibility-only, migration-only, mirrored, or pending reconciliation.

---

## Registry boundary

| Rule | Handling |
|---|---|
| Registry records are control state | They describe admission, identity, mapping, rights, sensitivity, layer, readiness, correction, and rollback posture. They do not contain the underlying data payloads. |
| Registry is pre-public | Registry state can block admission, processing, catalog closure, release, map display, or AI response. It does not by itself authorize publication. |
| Source role is preserved | Registry state must not upgrade observed, regulatory, administrative, modeled, aggregate, candidate, context, synthetic, restricted, primary, corroborating, or review-needed source roles. |
| Rights and sensitivity fail closed | Missing, stale, conflicted, restricted, or unresolved rights/sensitivity state blocks public exposure until reviewed and receipted. |
| Registry is not lifecycle data | RAW, WORK, QUARANTINE, PROCESSED, CATALOG/TRIPLET, and PUBLISHED payloads stay in their lifecycle lanes. |
| Registry is not contracts | Object meaning belongs under `contracts/`. |
| Registry is not schemas | Machine shape belongs under `schemas/contracts/v1/` or an ADR-selected schema home. |
| Registry is not policy | Allow, deny, restrict, abstain, access, redaction, sensitivity, rights, and release rules belong under `policy/`. |
| Registry is not receipts | Validation, transform, redaction, aggregation, model, policy, review, run, and pipeline receipts belong under `data/receipts/`. |
| Registry is not proof | EvidenceBundle records, proof packs, signatures, and citation-validation closure belong under proof lanes. |
| Registry is not catalog | STAC/DCAT/PROV/domain catalog records and graph/triplet projections live under catalog/triplet lanes. |
| Registry is not release | ReleaseManifest, PromotionDecision, CorrectionNotice, RollbackCard, withdrawal, and supersession authority lives under `release/` and accepted release lanes. |
| Public clients do not read registry internals directly | Public UI/API surfaces consume governed APIs, released artifacts, catalog/triplet/proof-backed responses, and policy-safe envelopes. |
| Unknown maturity stays unknown | README presence is not proof of emitted records, schemas, validators, tests, runtime readers, public APIs, or release maturity. |

---

## Accepted material

Accepted content in `data/registry/` is limited to registry-control records and registry-local support files:

- registry-family parent READMEs and domain/scope child READMEs;
- SourceDescriptor-style source records, dataset registry records, domain-state records, crosswalk records, rights records, sensitivity records, and layer records when the specific lane accepts them;
- registry-local indexes, manifests, checksums, signatures, and pointer maps;
- compatibility, migration, redirect, topology, correction, stale-state, supersession, withdrawal, and rollback notes;
- pointers to lifecycle payloads, contracts, schemas, policies, receipts, proofs, catalog records, release candidates, release manifests, correction notices, and rollback cards;
- blocker records that identify missing source, rights, sensitivity, evidence, receipt, catalog, review, release, correction, or rollback support.

Keep registry records compact and pointer-based. Do not embed full payloads, proof packs, policy decisions, catalog objects, release manifests, public tiles, generated answers, secrets, or private/restricted details in this root.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw source payloads or source-native exports | `data/raw/`, `data/work/`, or `data/quarantine/` depending on state |
| Processed domain objects, normalized tables, derived features, rasters, vectors, GeoParquet, COG, PMTiles, or other data payloads | `data/processed/`, `data/catalog/`, `data/triplets/`, or `data/published/` depending on lifecycle/release state |
| Source fetchers, endpoint clients, watchers, connector code, pipeline code, or automation | `connectors/`, `pipelines/`, `pipeline_specs/`, `packages/`, `tools/`, `configs/`, or accepted implementation roots |
| Semantic object contracts | `contracts/` |
| JSON Schema or machine shape | `schemas/contracts/v1/` or accepted schema root |
| Policy rules, access-control logic, rights decisions, sensitivity rules, geoprivacy rules, release rules, or runtime allow/deny logic | `policy/` |
| Validation receipts, transform receipts, redaction receipts, aggregation receipts, model receipts, policy receipts, review receipts, run receipts, or logs | `data/receipts/` |
| EvidenceBundle records, proof packs, signatures, or citation-validation closure | `data/proofs/` or accepted proof lane |
| STAC/DCAT/PROV/domain catalog records or graph/triplet projections | `data/catalog/` and `data/triplets/` |
| Published layers, reports, dashboards, tiles, API payloads, UI payloads, or generated-answer carriers | `data/published/`, governed app/API roots, and release-approved public artifact lanes |
| ReleaseManifest, PromotionDecision, CorrectionNotice, RollbackCard, withdrawal notice, or supersession notice | `release/` |
| Secrets, credentials, private keys, endpoint tokens, private/restricted details, or sensitive exact-location payloads | never in registry; use approved restricted storage and secret management |

---

## Suggested directory shape

This shape is **PROPOSED** as root-level guidance. Confirm child README/path evidence before adding payload records.

```text
data/registry/
├── README.md
├── sources/
│   └── README.md
├── datasets/
│   └── README.md
├── domains/
│   └── README.md
├── crosswalks/
│   └── README.md
├── rights/
│   └── README.md
├── sensitivity/
│   └── README.md
├── layers/
│   └── README.md
├── roads-rail-trade/              # domain-first compatibility/routing lane
│   └── README.md
├── settlements-infrastructure/    # domain-first compatibility/routing lane
│   └── README.md
├── soil/                          # domain-first compatibility/routing lane
│   └── README.md
└── index.local.json               # PROPOSED local index, not catalog/release/policy authority
```

Domain-specific records should generally live under the responsibility family that owns them, for example:

```text
data/registry/sources/<domain>/
data/registry/datasets/<domain>/
data/registry/domains/<domain>/
data/registry/rights/<domain-or-scope>/
data/registry/sensitivity/<domain-or-scope>/
data/registry/layers/<domain>/
```

When a domain-first lane exists, do not duplicate authoritative records. Add a redirect, migration note, or topology decision before splitting records across both shapes.

---

## Required checks before use

- [ ] Confirm the record belongs under `data/registry/`, not lifecycle data, contracts, schemas, policy, receipts, proofs, catalog, published artifacts, release, code, tests, or docs.
- [ ] Confirm the correct registry family: sources, datasets, domains, crosswalks, rights, sensitivity, layers, or a documented compatibility lane.
- [ ] Confirm whether the lane is canonical, compatibility-only, migration-only, mirrored, or pending topology reconciliation.
- [ ] Confirm source role, rights state, sensitivity state, support type, evidence state, review state, stale-state, correction state, and rollback state are preserved where material.
- [ ] Confirm registry state does not upgrade evidence strength, source authority, domain truth, public-safe status, catalog closure, release state, or generated-answer eligibility.
- [ ] Confirm public-safe transforms point to named/versioned profiles and required receipts where relevant.
- [ ] Confirm EvidenceRef/EvidenceBundle and proof refs exist before consequential registry state is used in public-facing logic.
- [ ] Confirm catalog refs point to STAC/DCAT/PROV/domain catalog records rather than embedding them.
- [ ] Confirm release refs point to ReleaseManifest/PromotionDecision objects rather than implying publication from registry state.
- [ ] Confirm correction, supersession, withdrawal, stale-state, rights-change, sensitivity-change, and rollback paths exist for mutable or externally governed material.
- [ ] Confirm no public client, map layer, graph edge, vector index, generated answer, report, or dashboard reads this registry root as direct public truth.

---

## Status notes

| Claim | Status |
|---|---:|
| This README replaces the greenfield stub at `data/registry/README.md`. | CONFIRMED authored |
| The target path existed in the live repository as a greenfield stub before this edit. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/sources/README.md` exists and says the source registry is admission and authority-control, not a bibliography. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/datasets/README.md` exists and says dataset registry records are governance handles, not dataset payloads or publication. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/domains/README.md` exists and says domain registry records are governance handles, not domain payloads or publication. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/crosswalks/README.md` exists and says crosswalk registry records are mapping-state records, not semantic contracts, schemas, policy, proof, catalog closure, or release. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/rights/README.md` exists and says rights registry records are review/control records, not legal advice, source license authority, policy, release, or permission to publish. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/sensitivity/README.md` exists and says sensitivity registry records are review/control records, not policy, release, public output, or exact sensitive-location storage. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/layers/README.md` exists and says layer registry records are control records, not layer bytes, tile storage, catalog output, policy, release, public API/UI material, or generated-answer authority. | CONFIRMED by GitHub contents API during this edit |
| Concrete registry payloads exist across all listed families. | UNKNOWN |
| Final registry topology across subtype-first and domain-first lanes is resolved. | NEEDS VERIFICATION |
| Canonical registry schemas are enforced for every family. | NEEDS VERIFICATION |
| CI validates registry records across every family. | UNKNOWN |
| Runtime registry resolution or governed API behavior reads this root. | UNKNOWN |
| This README grants public access to registry internals. | DENY |

---

## Maintainer note

The registry root is the trust membrane between proposed/admitted control state and downstream claims. Keep the safe chain explicit:

```text
registry record -> lifecycle payload refs -> policy/review outcome -> validation/redaction/transform receipts -> EvidenceBundle/proof -> catalog/triplet -> release -> governed public surface
```

Never collapse it into:

```text
registry record -> public truth
```
