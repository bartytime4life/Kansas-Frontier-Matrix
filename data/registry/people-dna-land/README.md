<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/people-dna-land/readme
name: People DNA Land Registry README
path: data/registry/people-dna-land/README.md
type: data-registry-people-dna-land-parent-readme
version: v0.2.0
status: draft
owners:
  - <registry-steward>
  - <people-dna-land-domain-steward>
  - <source-steward>
  - <dataset-steward>
  - <crosswalk-steward>
  - <privacy-steward>
  - <consent-steward>
  - <rights-steward>
  - <sensitivity-steward>
  - <sovereignty-reviewer>
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
registry_scope: people-dna-land-domain-first-registry-parent
domain: people-dna-land
path_posture: existing-parent-stub-replaced; sources-child-lane-confirmed; domain-first-registry-path-exists; canonical-subtype-first-and-people-slug-topology-needs-verification
sensitivity_posture: registry-internal; no-public-path; living-person-deny-default; dna-genomic-deny-default; consent-required; revocation-aware; person-parcel-joins-fail-closed; title-claims-require-evidence-chain; source-role-preserving; rights-aware; policy-aware; release-blocked-until-gates-close
related:
  - ../README.md
  - ../sources/README.md
  - ../sources/people-dna-land/
  - ../sources/people/
  - ../datasets/README.md
  - ../domains/README.md
  - ../crosswalks/README.md
  - sources/README.md
  - ../../raw/people-dna-land/
  - ../../work/people-dna-land/
  - ../../quarantine/people-dna-land/
  - ../../processed/people-dna-land/README.md
  - ../../catalog/domain/people-dna-land/
  - ../../published/layers/people-dna-land/
  - ../../receipts/people-dna-land/README.md
  - ../../proofs/
  - ../../../docs/domains/people-dna-land/SOURCE_LEDGER.md
  - ../../../docs/domains/people-dna-land/SOURCE_REGISTRY.md
  - ../../../docs/domains/people-dna-land/SOURCE_REGISTRY/README.md
  - ../../../docs/domains/people-dna-land/SOURCE_FAMILIES.md
  - ../../../docs/domains/people-dna-land/DATA_LIFECYCLE.md
  - ../../../docs/domains/people-dna-land/SENSITIVITY_PROFILE.md
  - ../../../docs/domains/people-dna-land/LAND_OWNERSHIP.md
  - ../../../docs/domains/people-dna-land/IDENTITY_MODEL.md
  - ../../../contracts/domains/people-dna-land/
  - ../../../schemas/contracts/v1/source/
  - ../../../schemas/contracts/v1/people/
  - ../../../policy/sensitivity/people/
  - ../../../policy/consent/people/
  - ../../../policy/rights/
  - ../../../release/
tags:
  - kfm
  - data
  - registry
  - people-dna-land
  - domain-first-registry
  - sources
  - source-descriptor
  - source-role
  - consent
  - revocation
  - privacy
  - living-person
  - dna
  - genomic
  - genealogy
  - land-ownership
  - title
  - parcel
  - person-parcel
  - rights
  - sensitivity
  - sovereignty
  - evidence
  - provenance
  - release-gated
  - no-public-path
notes:
  - "This README replaces the greenfield stub at `data/registry/people-dna-land/README.md`."
  - "This domain-first registry parent exists in the repository and currently has a confirmed `sources/` child README."
  - "The inspected People/DNA/Land docs surface unresolved slug drift between `people-dna-land` and `people`, and source-registry doctrine also points toward subtype-first source registry lanes. Therefore this parent is treated as a compatibility/routing lane until registry topology is reconciled."
  - "Living-person, DNA/genomic, DNA-derived relationship, private person-parcel, and land-title claims fail closed unless consent, rights, sensitivity, evidence, review, release, correction, and rollback gates close."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# People / DNA / Land Registry

Domain-first registry parent for People / DNA / Land registry lanes.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: registry" src="https://img.shields.io/badge/family-registry-blueviolet">
  <img alt="Domain: people-dna-land" src="https://img.shields.io/badge/domain-people--dna--land-7a4cff">
  <img alt="Topology: needs verification" src="https://img.shields.io/badge/topology-NEEDS%20VERIFICATION-orange">
  <img alt="Boundary: no public path" src="https://img.shields.io/badge/boundary-no%20public%20path-critical">
  <img alt="Consent: required" src="https://img.shields.io/badge/consent-required-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [Confirmed child lanes](#confirmed-child-lanes) · [People/DNA/Land registry boundary](#peoplednaland-registry-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Suggested directory shape](#suggested-directory-shape) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/registry/people-dna-land/` is a domain-first registry parent. It is not RAW source storage, WORK staging, QUARANTINE, PROCESSED data, catalog output, proof storage, receipt storage, semantic contract authority, schema authority, policy, release authority, public API/UI material, genealogy truth, title truth, identity truth, consent authority, or generated-answer authority.

---

## Scope

`data/registry/people-dna-land/` is a domain-first routing lane for People / DNA / Land registry material that already exists in the repository. Its current confirmed child is `sources/`, which documents source descriptor and source-admission records for the People / DNA / Land lane.

This parent README exists to prevent the domain-first path from becoming an unbounded parallel authority. It should route maintainers to the correct registry family and preserve the distinction between registry state and other KFM authority roots.

A People / DNA / Land registry lane may point to or summarize governance state for:

- source descriptors and source-admission records;
- source-role assignments and source-family posture;
- rights, consent, revocation, sensitivity, cadence, source-head, activation, intake, correction, supersession, stale-state, withdrawal, and freshness state;
- living-person, DNA/genomic, DNA-derived relationship, genealogy, title, parcel, person-parcel, cultural heritage, burial, and sovereignty-sensitive blockers;
- links to lifecycle payloads under RAW, WORK, QUARANTINE, PROCESSED, CATALOG/TRIPLET, and PUBLISHED phases;
- links to contracts, schemas, policies, receipts, proofs, catalog records, release candidates, correction notices, and rollback cards.

It must not contain source payloads, person identifiers, raw sensitive genomic material, private relationship detail, private person-parcel detail, title claims, proof packs, catalog records, release manifests, public map artifacts, or generated-answer carriers.

---

## Path posture

The requested and existing parent lane is:

```text
data/registry/people-dna-land/
```

This is a **domain-first** registry path. Current People / DNA / Land source-registry evidence also supports subtype-first and slug-reconciled source registry patterns:

```text
data/registry/sources/people-dna-land/
data/registry/sources/people/
```

The inspected docs also surface unresolved slug drift between the human-facing `people-dna-land` segment and the shorter `people` segment used in some policy/schema references. Therefore, `data/registry/people-dna-land/` is treated as **CONFIRMED path presence / NEEDS VERIFICATION topology**.

Until an ADR, Directory Rules update, registry README, migration note, or repository-wide inventory resolves the topology, do not create duplicate authoritative records in both domain-first and subtype-first locations, and do not silently normalize `people-dna-land` to `people` or `people` to `people-dna-land`.

---

## Repo fit

| Responsibility | Home | Boundary |
|---|---|---|
| People / DNA / Land domain-first registry parent | `data/registry/people-dna-land/` | Routing/compatibility parent for existing domain-first registry lanes. |
| Confirmed People / DNA / Land child registry lane | `data/registry/people-dna-land/sources/` | Source descriptor/admission records, with slug/topology warning. |
| Cross-domain source registry parent | `data/registry/sources/README.md` | General source registry doctrine and subtype-first source registry pattern. |
| Potential canonical People / DNA / Land source lanes | `data/registry/sources/people-dna-land/` or `data/registry/sources/people/` | Needs topology and slug reconciliation with this path. |
| Dataset registry records | `data/registry/datasets/` | Dataset identity and dataset-state records. |
| Domain registry records | `data/registry/domains/` | Domain-state records; do not duplicate here without topology decision. |
| Crosswalk registry records | `data/registry/crosswalks/` | Mapping state across source IDs, authority IDs, identities, records, parcels, legal descriptions, and vocabularies. |
| People / DNA / Land source payloads | `data/raw/people-dna-land/`, `data/work/people-dna-land/`, `data/quarantine/people-dna-land/`, `data/processed/people-dna-land/` | Actual data belongs in lifecycle lanes, not registry parent files. |
| People / DNA / Land semantic meaning | `contracts/domains/people-dna-land/` and/or reconciled `contracts/people/` homes | Object-family meaning and invariants; slug topology remains NEEDS VERIFICATION. |
| People / DNA / Land machine shape | `schemas/contracts/v1/source/`, `schemas/contracts/v1/people/`, and accepted domain schema homes | Schema enforcement; slug and path form remain NEEDS VERIFICATION until ADR/repo evidence resolves them. |
| Consent, sensitivity, and rights policy | `policy/consent/people/`, `policy/sensitivity/people/`, `policy/rights/` | Consent, revocation, privacy, rights, source-role, exposure, and admissibility rules. |
| Validation/redaction/consent receipts | `data/receipts/people-dna-land/` and accepted receipt lanes | Process memory for checks and public-safe transforms. |
| Proof/evidence | `data/proofs/` or accepted proof lanes | EvidenceBundle closure, proof packs, signatures, and citation validation. |
| Catalog projections | `data/catalog/domain/people-dna-land/`, STAC/DCAT/PROV lanes, and triplet lanes | Catalog/discovery carriers after catalog closure. |
| Release decisions | `release/` | Promotion, correction, rollback, supersession, withdrawal, and release manifests. |
| Public surfaces | governed APIs and released artifacts only | Public clients do not read this registry parent directly. Sensitive classes remain denied unless release gates explicitly close. |

---

## Confirmed child lanes

This confirms only path/README evidence. It does not prove emitted records, schemas, validators, fixtures, CI enforcement, signing, release integration, correction hooks, rollback hooks, governed API behavior, or public-safe summaries.

| Child lane | Status | Purpose | Boundary |
|---|---:|---|---|
| [`sources/`](sources/README.md) | CONFIRMED README | Domain-first People / DNA / Land source descriptor and source-admission registry lane. | Not source payload storage, People / DNA / Land truth, consent authority, proof, receipt storage, catalog closure, semantic contract authority, policy, release authority, or public output. |

---

## People/DNA/Land registry boundary

| Rule | Handling |
|---|---|
| Registry parent is routing state | This parent orients to child registry lanes; it does not contain domain payloads. |
| Topology is unresolved | Do not silently duplicate records between `data/registry/people-dna-land/...`, `data/registry/sources/people-dna-land/`, and `data/registry/sources/people/`. |
| Consent is not optional | Consent, revocation, and permitted-use constraints must be explicit before any DNA/genomic or living-person source can be used. |
| Living-person content fails closed | Living-person identifiers, relationship assertions, person-parcel joins, and private context remain denied or restricted unless policy/review/release gates explicitly permit a public-safe derivative. |
| DNA/genomic material fails closed | Registry state may record existence and control posture, but raw sensitive genomic material and DNA-derived relationship evidence do not become public artifacts. |
| Tree evidence is not authority | GEDCOM, tree overlays, and user-contributed genealogy assertions are candidate/model/context evidence until independently supported and reviewed. |
| Assessor and tax records are not title truth | Assessor/tax records are administrative context; they do not satisfy title or ownership claims. |
| Parcel geometry is not title boundary proof | Parcel, survey, PLSS, and derived geometry must preserve role, vintage, and uncertainty; geometry alone is not title proof. |
| Land instruments require chain context | Deeds, patents, liens, easements, leases, probate records, and related instruments support evidence-bound temporal assertions, not automatic ownership truth. |
| Sovereignty and cultural context fail closed | Burial, cultural heritage, tribal/sovereignty-sensitive, and living-descendant contexts require the most restrictive applicable policy posture. |
| Source role is preserved | Registry state must not upgrade observed, regulatory, modeled, aggregate, administrative, candidate, synthetic, context, or restricted source roles. |
| Registry is not validation | Validation receipts and run receipts remain separate process-memory objects. |
| Registry is not proof | EvidenceBundle/proof support remains separate. |
| Registry is not catalog | STAC/DCAT/PROV/domain catalog records and graph projections live under catalog/triplet lanes. |
| Registry is not release | Public exposure requires validation, consent/rights/sensitivity policy, review, proof/catalog support, release manifest, correction path, and rollback path. |
| Public clients do not read this lane | Public UI/API surfaces consume governed APIs, released artifacts, catalog/triplet/proof-backed responses, and policy-safe envelopes. |

---

## Accepted material

Accepted content is limited to README/routing material and registry-local sidecars that do not duplicate authority from subtype-first lanes:

- parent README and routing notes;
- compatibility notes explaining domain-first versus subtype-first topology;
- slug reconciliation notes for `people-dna-land` versus `people`;
- migration notes, redirect notes, rollback notes, or topology decision notes;
- local indexes that point to child registry lanes without becoming authoritative records themselves;
- checksums, manifests, and signatures for registry routing material where applicable;
- pointers to source descriptors, dataset registry records, crosswalk registry records, domain registry records, contracts, schemas, policy refs, lifecycle payloads, validation receipts, consent/revocation receipts, redaction receipts, proof refs, catalog refs, release candidates, correction notices, supersession notices, withdrawal notices, stale-state notices, and rollback cards.

If a child lane under this parent stores actual registry records, it must state whether it is canonical, compatibility, migration-only, or mirrored, and it must name its conflict/rollback path.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw People / DNA / Land source payloads, user exports, GEDCOM files, vital-record extracts, census schedules, DNA vendor exports, match tables, deed books, assessor/tax-roll extracts, parcel layers, scans, shapefiles, GeoParquet, COG, PMTiles, or source-native tables | `data/raw/people-dna-land/`, `data/work/people-dna-land/`, `data/quarantine/people-dna-land/`, or `data/processed/people-dna-land/` depending on lifecycle state |
| Living-person identifiers, private relationship assertions, sensitive genealogical joins, raw DNA/genomic payloads, private DNA-derived relationship details, person-parcel joins, access secrets, or restricted review material | denied, restricted, quarantined, or routed to governed restricted storage |
| Human-facing bibliography or source narrative | `docs/domains/people-dna-land/`, `docs/sources/`, or source catalog docs |
| Canonical source descriptor records if a subtype-first lane is accepted as canonical | `data/registry/sources/people-dna-land/` or `data/registry/sources/people/` after topology reconciliation |
| Dataset identity records | `data/registry/datasets/` |
| Crosswalk mapping records | `data/registry/crosswalks/` |
| Domain-state records | `data/registry/domains/` |
| Semantic object contracts | `contracts/domains/people-dna-land/` or reconciled `contracts/people/` homes |
| JSON Schema | `schemas/contracts/v1/source/`, `schemas/contracts/v1/people/`, or ADR-selected schema lane |
| Policy rules, sensitivity rules, consent rules, revocation rules, rights rules, access-control logic, or release rules | `policy/` |
| Validation receipts, redaction receipts, consent receipts, revocation receipts, policy receipts, review receipts, or process-memory logs | `data/receipts/` |
| EvidenceBundle records, proof packs, signatures, or citation-validation closure | `data/proofs/` |
| STAC/DCAT/PROV/domain catalog records or graph/triplet projections | `data/catalog/` and `data/triplets/` |
| Published layers, reports, dashboards, tiles, API payloads, or generated-answer carriers | `data/published/`, governed app/API roots, and release-approved public artifact lanes |
| ReleaseManifest, PromotionDecision, CorrectionNotice, RollbackCard, withdrawal notice, or supersession notice | `release/` |
| Validator code, connector code, pipelines, fixtures, tests, or CI workflows | `tools/`, `connectors/`, `pipelines/`, `fixtures/`, `tests/`, `.github/workflows/` |

---

## Suggested directory shape

The map below is **PROPOSED** documentation guidance, not proof that child folders or records exist beyond confirmed README evidence.

```text
data/registry/people-dna-land/
├── README.md
├── sources/
│   └── README.md
└── index.local.json
```

If subtype-first lanes are accepted as canonical, prefer a migration such as:

```text
data/registry/sources/people-dna-land/       # possible canonical source descriptors
data/registry/sources/people/                # possible canonical source descriptors after slug ADR
data/registry/people-dna-land/README.md      # compatibility pointer / migration note only
```

Do not maintain divergent descriptor sets.

---

## Required checks before use

- [ ] Confirm whether `data/registry/people-dna-land/...`, `data/registry/sources/people-dna-land/`, or `data/registry/sources/people/` is canonical before adding real registry payloads.
- [ ] Confirm a child object is a registry record, not source data, proof, receipt, catalog record, release decision, policy, schema, validator, fixture, or test.
- [ ] Confirm source identity, source role, rights posture, consent posture, revocation posture, terms, cadence, source head, source vintage, jurisdiction, export version, and authority limits are preserved for any source-registry child records.
- [ ] Confirm registry state does not upgrade source role, evidence strength, review state, catalog state, release state, consent state, or public-safe posture.
- [ ] Confirm living-person, DNA/genomic, DNA-derived relationship, title, parcel-boundary, assessor/tax, person-parcel, cultural heritage, burial, and sovereignty-sensitive contexts are not collapsed.
- [ ] Confirm assessor/tax records are never treated as title truth.
- [ ] Confirm tree exports and relationship hypotheses are not treated as verified relationship authority without independent support.
- [ ] Confirm consent, revocation, policy, and review states are current before any use beyond restricted processing.
- [ ] Confirm sensitive details are not exposed in registry files, local indexes, public summaries, vector indexes, map labels, or generated responses.
- [ ] Confirm validation receipts exist before catalog or release eligibility is asserted.
- [ ] Confirm EvidenceRef/EvidenceBundle and proof refs exist for consequential use.
- [ ] Confirm catalog refs point to STAC/DCAT/PROV/domain catalog records rather than embedding them.
- [ ] Confirm release refs point to ReleaseManifest/PromotionDecision objects rather than implying publication from registry state.
- [ ] Confirm correction, revocation, supersession, withdrawal, stale-state, and rollback paths exist for mutable, consent-bound, rights-bound, or externally governed source material.
- [ ] Confirm no public client, map layer, graph edge, vector index, generated answer, report, or dashboard reads this registry parent as direct public truth.

---

## Status notes

| Claim | Status |
|---|---:|
| This README replaces the greenfield stub at `data/registry/people-dna-land/README.md`. | CONFIRMED authored |
| The target path existed in the live repository as a greenfield stub before this edit. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/people-dna-land/sources/README.md` exists as a confirmed child lane. | CONFIRMED by GitHub contents API during this edit |
| The child `sources/` README marks the domain-first path as confirmed but layout-NEEDS VERIFICATION against subtype-first/source-slug alternatives. | CONFIRMED by GitHub contents API during this edit |
| People / DNA / Land source ledger says the ledger is a control surface and does not activate, rights-clear, or publish a source. | CONFIRMED by GitHub contents API in this sequence |
| People / DNA / Land source-registry README says the lane fails closed for living-person and DNA-derived outputs and blocks public promotion when rights/sensitivity/evidence/release state is unresolved. | CONFIRMED by GitHub contents API in this sequence |
| People / DNA / Land lifecycle docs state living-person, DNA, and person/parcel/title controls are gate-enforced and raw sensitive material must not be carried in public-facing docs. | CONFIRMED by GitHub contents API in this sequence |
| Concrete People / DNA / Land registry payloads exist under this parent lane. | UNKNOWN |
| The final accepted topology between domain-first and subtype-first registry lanes is resolved. | NEEDS VERIFICATION |
| The final accepted slug between `people-dna-land` and `people` is resolved. | NEEDS VERIFICATION |
| CI validates People / DNA / Land registry records. | UNKNOWN |
| This README grants public access to People / DNA / Land registry internals. | DENY |

---

## Maintainer note

This parent exists because the repository already has a domain-first People / DNA / Land registry lane. Keep it useful but constrained. The safe chain is:

```text
registry pointer -> canonical registry record -> consent/rights/sensitivity gate -> lifecycle payload -> validation/redaction receipt -> proof/catalog/policy/review -> release -> governed public surface
```

Never collapse it into:

```text
registry parent -> public People / DNA / Land truth
```
