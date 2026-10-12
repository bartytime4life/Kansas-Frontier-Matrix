<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://data/registry/people-dna-land/sources/readme
name: People DNA Land Source Registry README
path: data/registry/people-dna-land/sources/README.md
type: data-registry-people-dna-land-sources-readme
version: v0.2.0
status: draft
owners:
  - <registry-steward>
  - <source-steward>
  - <people-dna-land-domain-steward>
  - <privacy-steward>
  - <consent-steward>
  - <rights-steward>
  - <sensitivity-steward>
  - <sovereignty-reviewer>
  - <policy-steward>
  - <proof-steward>
  - <release-steward>
created: 2026-06-28
updated: 2026-06-28
policy_label: restricted-review
truth_posture: cite-or-abstain
responsibility_root: data/
artifact_family: registry
registry_scope: people-dna-land-source-descriptor-records
domain: people-dna-land
path_posture: existing-thin-readme-replaced; domain-first-registry-path-confirmed; canonical-source-registry-pattern-points-to-data-registry-sources-people-dna-land-or-people; slug-topology-conflicted-needs-adr; layout-needs-verification
sensitivity_posture: registry-internal; no-public-path; living-person-deny-default; dna-genomic-deny-default; consent-required; revocation-aware; person-parcel-joins-fail-closed; title-claims-require-evidence-chain; source-role-preserving; rights-aware; policy-aware; release-blocked-until-gates-close
related:
  - ../README.md
  - ../../README.md
  - ../../sources/README.md
  - ../../sources/people-dna-land/
  - ../../sources/people/
  - ../../datasets/README.md
  - ../../domains/README.md
  - ../../crosswalks/README.md
  - ../../../raw/people-dna-land/
  - ../../../work/people-dna-land/
  - ../../../quarantine/people-dna-land/
  - ../../../processed/people-dna-land/README.md
  - ../../../catalog/domain/people-dna-land/
  - ../../../published/layers/people-dna-land/
  - ../../../receipts/people-dna-land/README.md
  - ../../../proofs/
  - ../../../../docs/domains/people-dna-land/SOURCE_LEDGER.md
  - ../../../../docs/domains/people-dna-land/SOURCE_REGISTRY.md
  - ../../../../docs/domains/people-dna-land/SOURCE_REGISTRY/README.md
  - ../../../../docs/domains/people-dna-land/SOURCE_FAMILIES.md
  - ../../../../docs/domains/people-dna-land/DATA_LIFECYCLE.md
  - ../../../../docs/domains/people-dna-land/SENSITIVITY_PROFILE.md
  - ../../../../docs/domains/people-dna-land/LAND_OWNERSHIP.md
  - ../../../../docs/domains/people-dna-land/IDENTITY_MODEL.md
  - ../../../../contracts/domains/people-dna-land/
  - ../../../../schemas/contracts/v1/source/
  - ../../../../schemas/contracts/v1/people/
  - ../../../../policy/sensitivity/people/
  - ../../../../policy/consent/people/
  - ../../../../policy/rights/
  - ../../../../release/
tags:
  - kfm
  - data
  - registry
  - people-dna-land
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
  - "This README expands the thin README at `data/registry/people-dna-land/sources/README.md`."
  - "People/DNA/Land source registry records are admission and authority-control records. They do not store source payloads, prove relationship/title/identity claims, define contracts, enforce schemas, hold policy, close catalogs, or publish artifacts."
  - "The inspected docs surface unresolved slug drift between `people-dna-land` and `people`. This requested domain-first path exists in the repository but remains layout-NEEDS VERIFICATION until registry topology is reconciled by ADR or directory guidance."
  - "Living-person, DNA/genomic, DNA-derived relationship, private person-parcel, and land-title claims fail closed unless consent, rights, sensitivity, evidence, review, release, correction, and rollback gates close."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# People / DNA / Land Source Registry

Domain-first registry lane for People / DNA / Land source descriptor and source-admission records.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Family: registry" src="https://img.shields.io/badge/family-registry-blueviolet">
  <img alt="Domain: people-dna-land" src="https://img.shields.io/badge/domain-people--dna--land-7a4cff">
  <img alt="Lane: sources" src="https://img.shields.io/badge/lane-sources-blue">
  <img alt="Boundary: no public path" src="https://img.shields.io/badge/boundary-no%20public%20path-critical">
  <img alt="Consent: required" src="https://img.shields.io/badge/consent-required-critical">
</p>

**Quick links:** [Scope](#scope) · [Path posture](#path-posture) · [Repo fit](#repo-fit) · [People/DNA/Land source boundary](#peoplednaland-source-boundary) · [Accepted material](#accepted-material) · [Exclusions](#exclusions) · [Suggested directory shape](#suggested-directory-shape) · [Suggested descriptor shape](#suggested-descriptor-shape) · [Required checks](#required-checks-before-use) · [Status notes](#status-notes)

> [!CAUTION]
> `data/registry/people-dna-land/sources/` is a source-registry lane for People / DNA / Land admission and authority-control records. It is not RAW source storage, WORK staging, QUARANTINE, PROCESSED data, catalog output, proof, receipt storage, semantic contract authority, policy, release authority, public API/UI material, genealogy truth, title truth, identity truth, consent authority, or generated-answer authority.

---

## Scope

This directory documents and may hold People / DNA / Land source descriptor records, activation/admission sidecars, source-family indexes, source-role review notes, source-head references, consent/revocation pointers, supersession references, and registry-local indexes for sources that may feed the People / DNA / Land lane.

People / DNA / Land source registry records describe how a source may be treated before source material reaches RAW. They may record:

- source identity and source family;
- canonical `source_role` assignment;
- rights, license, attribution, redistribution, terms, consent, and revocation posture;
- sensitivity posture for living-person, DNA/genomic, genealogical, land-title, parcel, and person-parcel content;
- cadence, source head, retrieval window, source vintage, record series, export version, and source version;
- steward, contact, reviewer, and activation state;
- permitted object families or claim families;
- required redaction, quarantine, validation, proof, catalog, release, correction, stale-state, withdrawal, and rollback requirements.

They do **not** record person truth, relationship truth, identity truth, title truth, parcel-boundary truth, or DNA-derived truth. A source descriptor can authorize or deny admission conditions, but every consequential claim still needs lifecycle processing, evidence support, policy decision, review state, catalog/proof support, release state, correction path, and rollback target.

---

## Path posture

The requested and existing lane is:

```text
data/registry/people-dna-land/sources/
```

This is a domain-first registry path. Inspected People / DNA / Land source docs also point toward subtype-first or slug-reconciled source registry patterns such as:

```text
data/registry/sources/people-dna-land/
data/registry/sources/people/
```

The docs also surface an unresolved slug conflict between `people-dna-land` and `people`. Until an ADR, Directory Rules update, registry README, migration note, or repository-wide inventory resolves that topology, this README treats the requested path as **CONFIRMED path presence / NEEDS VERIFICATION topology**.

Do not silently duplicate source descriptor instances across `data/registry/people-dna-land/sources/`, `data/registry/sources/people-dna-land/`, and `data/registry/sources/people/`. Prefer one canonical descriptor record with compatibility pointers, migration notes, and rollback history.

The domain-first parent exists but is currently a stub:

```text
data/registry/people-dna-land/README.md
```

---

## Repo fit

| Responsibility | Home | Boundary |
|---|---|---|
| People / DNA / Land source descriptor/admission records | `data/registry/people-dna-land/sources/` and/or reconciled `data/registry/sources/<slug>/` | Source identity, role, rights, terms, consent, sensitivity, cadence, activation, supersession, and authority limits. |
| Cross-domain source registry parent | `data/registry/sources/README.md` | General SourceDescriptor and admission-control doctrine. |
| Human-facing People / DNA / Land source orientation | `docs/domains/people-dna-land/SOURCE_LEDGER.md`, `SOURCE_REGISTRY.md`, `SOURCE_REGISTRY/README.md`, `SOURCE_FAMILIES.md` | Explains source families, admission posture, source-role discipline, and sensitivity gates; not machine descriptor storage. |
| People / DNA / Land source payloads | `data/raw/people-dna-land/`, `data/work/people-dna-land/`, `data/quarantine/people-dna-land/`, `data/processed/people-dna-land/` | Actual data belongs in lifecycle lanes, not registry records. |
| People / DNA / Land domain/dataset/crosswalk registry records | `data/registry/domains/`, `data/registry/datasets/`, `data/registry/crosswalks/` | Adjacent registry state; not source descriptor authority. |
| People / DNA / Land semantic meaning | `contracts/domains/people-dna-land/` and/or reconciled `contracts/people/` homes | Object-family meaning and invariants; slug topology remains NEEDS VERIFICATION. |
| People / DNA / Land machine shape | `schemas/contracts/v1/source/`, `schemas/contracts/v1/people/`, and accepted domain schema homes | Schema enforcement; slug and path form remain NEEDS VERIFICATION until ADR/repo evidence resolves them. |
| Consent, sensitivity, and rights policy | `policy/consent/people/`, `policy/sensitivity/people/`, `policy/rights/` | Consent, revocation, privacy, rights, source-role, exposure, and admissibility rules. |
| Validation/redaction/consent receipts | `data/receipts/people-dna-land/` and accepted receipt lanes | Process memory for checks and public-safe transforms. |
| Proof/evidence | `data/proofs/` or accepted proof lanes | EvidenceBundle closure, proof packs, signatures, and citation validation. |
| Catalog projections | `data/catalog/domain/people-dna-land/`, STAC/DCAT/PROV lanes, and triplet lanes | Catalog/discovery carriers after catalog closure. |
| Release decisions | `release/` | Promotion, correction, rollback, supersession, withdrawal, and release manifests. |
| Public surfaces | governed APIs and released artifacts only | Public clients do not read this registry lane directly. Sensitive classes remain denied unless release gates explicitly close. |

---

## People/DNA/Land source boundary

| Rule | Handling |
|---|---|
| Registry record is admission control | It governs how a source may be admitted and used; it does not contain the source payload. |
| Consent is not optional | Consent, revocation, and permitted-use constraints must be explicit before any DNA/genomic or living-person source can be used. |
| Living-person content fails closed | Living-person identifiers, relationship assertions, person-parcel joins, and private context remain denied or restricted unless policy/review/release gates explicitly permit a public-safe derivative. |
| DNA/genomic material fails closed | Source descriptors may record existence and control posture, but raw sensitive genomic material and DNA-derived relationship evidence do not become public artifacts. |
| Tree evidence is not authority | GEDCOM, tree overlays, and user-contributed genealogy assertions are candidate/model/context evidence until independently supported and reviewed. |
| Assessor and tax records are not title truth | Assessor/tax records are administrative context; they do not satisfy title or ownership claims. |
| Parcel geometry is not title boundary proof | Parcel, survey, PLSS, and derived geometry must preserve role, vintage, and uncertainty; geometry alone is not title proof. |
| Land instruments require chain context | Deeds, patents, liens, easements, leases, probate records, and related instruments support evidence-bound temporal assertions, not automatic ownership truth. |
| Sovereignty and cultural context fail closed | Burial, cultural heritage, tribal/sovereignty-sensitive, and living-descendant contexts require the most restrictive applicable policy posture. |
| Source role is fixed at admission | The canonical role must not be upgraded by processing, aggregation, cataloging, release review, map rendering, or generated explanation. |
| Registry is not evidence closure | EvidenceBundle/proof support remains separate. |
| Registry is not catalog closure | STAC/DCAT/PROV/domain catalog and graph projections remain separate. |
| Registry is not release | Public exposure requires validation, consent/rights/sensitivity policy, review, proof/catalog support, release manifest, correction path, and rollback path. |
| Public clients do not read this lane | Public UI/API surfaces consume governed APIs, released artifacts, and evidence/policy-safe envelopes. |

---

## Accepted material

Accepted content is limited to People / DNA / Land source registry records and registry-local support files:

- SourceDescriptor instances or pointers;
- SourceActivationDecision references or activation sidecars where accepted;
- SourceIntakeRecord references and source-head metadata summaries;
- source-family README files and local indexes;
- source-role review notes and role-assignment records;
- rights, consent, revocation, sensitivity, cadence, steward, endpoint, access, attribution, redistribution, and authority-scope metadata;
- source vintage, record series, jurisdiction, export version, terms review, consent grant/refusal/revocation refs, and source-head metadata summaries;
- supersession, withdrawal, correction, embargo, stale-state, quarantine, revocation, and rollback references;
- registry-local manifests, checksums, signatures, and index sidecars;
- pointers to validation receipts, redaction/generalization receipts, consent receipts, proof packs, catalog records, release candidates, release manifests, correction notices, and rollback cards.

Keep records compact and pointer-based. Do not embed sensitive payloads, living-person identifiers, private person-parcel details, DNA segment details, proof packs, policy decisions, catalog records, release manifests, source-native dumps, or People / DNA / Land claims in this lane.

---

## Exclusions

| Do not place here | Correct authority home |
|---|---|
| Raw People / DNA / Land source payloads, user exports, GEDCOM files, vital-record extracts, census schedules, DNA vendor exports, match tables, deed books, assessor/tax-roll extracts, parcel layers, scans, shapefiles, GeoParquet, COG, PMTiles, or source-native tables | `data/raw/people-dna-land/`, `data/work/people-dna-land/`, `data/quarantine/people-dna-land/`, or `data/processed/people-dna-land/` depending on lifecycle state |
| Living-person identifiers, private relationship assertions, sensitive genealogical joins, raw DNA/genomic payloads, private DNA-derived relationship details, person-parcel joins, access secrets, or restricted review material | denied, restricted, quarantined, or routed to governed restricted storage |
| Human-facing bibliography or source narrative | `docs/domains/people-dna-land/`, `docs/sources/`, or source catalog docs |
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

The map below is **PROPOSED** documentation guidance, not proof that child folders or records exist.

```text
data/registry/people-dna-land/sources/
├── README.md
├── person_vital_genealogy/
│   ├── README.md
│   └── index.local.json
├── tree_exports/
│   ├── README.md
│   └── index.local.json
├── dna_genomic/
│   ├── README.md
│   └── index.local.json
├── land_instruments/
│   ├── README.md
│   └── index.local.json
├── assessor_tax/
│   ├── README.md
│   └── index.local.json
├── parcel_geometry/
│   ├── README.md
│   └── index.local.json
├── plss_survey_patent/
│   ├── README.md
│   └── index.local.json
├── consent_frameworks/
│   ├── README.md
│   └── index.local.json
└── index.local.json
```

If `data/registry/sources/people-dna-land/` or `data/registry/sources/people/` is accepted as canonical, this domain-first path should either redirect to that lane or be migrated with a clear manifest, retained history, and rollback target. Do not maintain divergent descriptor sets.

---

## Suggested descriptor shape

The exact schema remains **NEEDS VERIFICATION**. A People / DNA / Land source registry record should be structured enough for audit, admission, consent, validation, correction, revocation, and rollback.

```json
{
  "id": "kfm-source:people-dna-land:<stable-source-id>",
  "record_type": "source_descriptor",
  "domain": "people-dna-land",
  "source_family": "person_vital_genealogy | tree_exports | dna_genomic | land_instruments | assessor_tax | parcel_geometry | plss_survey_patent | consent_frameworks | context_layer | other",
  "source_name": "Human-readable source name",
  "source_role": "observed | regulatory | modeled | aggregate | administrative | candidate | synthetic | context | restricted",
  "authority_scope": "What this source may and may not support",
  "rights_posture": "open | attribution-required | restricted | consent-bound | stewarded | unknown | denied",
  "consent_posture": "not-applicable | required | granted | revoked | expired | denied | needs-review",
  "sensitivity_posture": "public-safe | generalized | restricted | denied | needs-review",
  "cadence": "one-time | periodic | event-driven | user-supplied | unknown",
  "source_head_refs": [],
  "retrieval_refs": [],
  "activation_refs": [],
  "intake_refs": [],
  "consent_refs": [],
  "revocation_refs": [],
  "policy_refs": [],
  "validation_receipt_refs": [],
  "redaction_receipt_refs": [],
  "evidence_refs": [],
  "proof_refs": [],
  "catalog_refs": [],
  "review_refs": [],
  "release_refs": [],
  "correction_refs": [],
  "rollback_refs": [],
  "blockers": [],
  "public_exposure": "none | eligible-after-review | released-public-safe | permissioned | restricted | denied",
  "created_at": "timestamp",
  "updated_at": "timestamp"
}
```

Do not treat this JSON block as a live schema. It is a maintainer-facing sketch until paired contracts, schemas, validators, fixtures, examples, CI, and review workflows are verified.

---

## Required checks before use

- [ ] Confirm whether `data/registry/people-dna-land/sources/`, `data/registry/sources/people-dna-land/`, or `data/registry/sources/people/` is the accepted canonical descriptor lane before adding real descriptor payloads.
- [ ] Confirm the object is a source registry record, not source data, dataset registry record, crosswalk, domain registry record, proof, receipt, catalog record, release decision, policy, schema, validator, fixture, or test.
- [ ] Confirm source identity, source role, rights posture, consent posture, revocation posture, terms, cadence, source head, source vintage, jurisdiction, export version, and authority limits are preserved.
- [ ] Confirm source role is not upgraded by normalization, aggregation, cataloging, release review, API shaping, map rendering, or generated explanation.
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
- [ ] Confirm no public client, map layer, graph edge, vector index, generated answer, report, or dashboard reads this registry lane as direct public truth.

---

## Status notes

| Claim | Status |
|---|---:|
| This README expands the thin README at `data/registry/people-dna-land/sources/README.md`. | CONFIRMED authored |
| The target path existed in the live repository with a short source-descriptor note before this edit. | CONFIRMED by GitHub contents API during this edit |
| `data/registry/people-dna-land/README.md` exists and is currently a greenfield stub. | CONFIRMED by GitHub contents API during this edit |
| People / DNA / Land source ledger says the ledger is a control surface and does not activate, rights-clear, or publish a source. | CONFIRMED by GitHub contents API during this edit |
| People / DNA / Land source ledger says many sources carry living-person, DNA/genomic, or private person-parcel content and default to denied/restricted with sensitive joins fail-closed. | CONFIRMED by GitHub contents API during this edit |
| People / DNA / Land source-registry README says the lane fails closed and raw sensitive DNA-derived/publication-sensitive material is never public. | CONFIRMED by GitHub contents API during this edit |
| People / DNA / Land lifecycle docs state raw DNA-related sensitive material and person/parcel/title controls are gate-enforced and must not be carried in the document. | CONFIRMED by GitHub contents API during this edit |
| Concrete People / DNA / Land source descriptor payloads exist under this requested lane. | UNKNOWN |
| The final accepted topology between `people-dna-land` and `people` slugs is resolved. | NEEDS VERIFICATION |
| A canonical People / DNA / Land source descriptor schema is enforced. | NEEDS VERIFICATION |
| CI validates People / DNA / Land source registry records. | UNKNOWN |
| This README grants public access to People / DNA / Land source registry internals. | DENY |

---

## Maintainer note

People / DNA / Land source registry records are useful because they make source identity, source role, consent, revocation, rights, sensitivity, activation, correction, and rollback inspectable before admission. They become dangerous when treated as payloads, proofs, catalog closure, release decisions, genealogy truth, title truth, identity truth, or consent authority. Keep the chain explicit:

```text
SourceDescriptor -> SourceActivationDecision -> consent/rights/sensitivity gate -> RAW admission -> lifecycle processing -> validation/redaction receipt -> proof/catalog/policy/review -> release -> governed public surface
```

Never collapse it into:

```text
source descriptor -> public People / DNA / Land truth
```
