<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/standards/darwin-core
title: Darwin Core — KFM Standards Boundary, Mapping, and Graduation Plan
type: standard; external-vocabulary-reference; biodiversity-interoperability-boundary
version: v2.0-draft
status: "draft; repository-grounded; upstream-currentness-refreshed; no-profile-adoption; no-conformance-proof; no-release; no-publication"
owners:
  - "@bartytime4life — verified GitHub review route through CODEOWNERS"
  - "NEEDS VERIFICATION — biodiversity, fauna, flora, taxonomy, source, rights, sensitivity, catalog, schema, validation, and release stewards"
created: 2026-05-14
updated: 2026-08-18
policy_label: repository-facing; standards-guidance; biodiversity; sensitive-location-aware
owning_root: docs/
current_path: docs/standards/Darwin_Core.md
responsibility: >
  Explain the official Darwin Core baseline, the bounded relationship between Darwin Core
  and current KFM biodiversity objects, the unresolved STAC-DwC profile family, and the
  gates required before KFM may claim Darwin Core conformance or publish an interoperable
  biodiversity package.
truth_posture: >
  CONFIRMED current path, standards-lane placement, review route, current Fauna
  OccurrenceEvidence contract/schema/validator slice, OccurrencePublic scaffold posture,
  biodiversity-validator parent posture, sibling STAC-DwC document presence, and dated
  official TDWG publication facts / PROPOSED KFM term mappings, export profiles,
  conformance targets, mapper, fixtures, validators, producers, consumers, and graduation
  sequence / UNKNOWN adopted KFM Darwin Core profile, canonical Darwin Core serialization,
  complete term mapping, local ontology or vocabulary mirror, released Darwin Core package,
  production interoperability, and accountable specialist stewardship.
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: f9a515a1124f9f5397996f6bc7cb3fd1a3534c40
  target_prior_blob: f897db3b14796ae895646ff32d410762b972119a
  standards_readme_blob: a8cbe5d183448d5f0de37f8a4eacd6fcaca0d71b
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  occurrence_evidence_contract_blob: f38ae38055d03149471a97b63d38a7b8f7cfbd35
  occurrence_evidence_schema_blob: 55bfdf896627443281e41ef2761024bddedc7828
  occurrence_evidence_validator_blob: fd54968e4e013284d8c633ea6782252a0a4ec90c
  occurrence_public_contract_blob: d0c1481160b4979445a916915ff96d04d48f7033
  biodiversity_validator_readme_blob: 64f7e28635033a0b122b103889d5e8646d44e3c2
  sibling_stac_dwc_document_blobs:
    STAC-DwC.md: NEEDS_VERIFICATION
    STAC_DWC_PROFILE.md: b5cb510725a78fdf52033f36b127376e90e086f5
    stac-dwc-hybrid.md: 7599c4ba98a2b6e8f58b512c72581041cb94fde1
external_currentness_review:
  access_date: 2026-08-18
  issuer_scope: "Official TDWG and Darwin Core Maintenance Group sources"
  standard_status: "Current TDWG standard; permanent IRI http://www.tdwg.org/standards/450; ratified 2009-10-09"
  vocabulary_version: "Darwin Core List of Terms 2026-05-26"
  conceptual_model_version: "Darwin Core conceptual model 2026-05-26"
  data_package_version: "Darwin Core Data Package guide 2026-05-26"
  text_guide_version: "Darwin Core Text Guide 2023-09-13"
  active_review_note: "July 2026 review discussion closed 2026-08-15; unresolved proposals move to a later cycle and are not treated here as ratified standard"
related:
  - ./README.md
  - ./STAC-DwC.md
  - ./STAC_DWC_PROFILE.md
  - ./stac-dwc-hybrid.md
  - ./STAC_KFM_PROFILE.md
  - ./SENSITIVITY_RUBRIC.md
  - ./REDACTION_PROFILES.md
  - ./EVIDENCE_BUNDLE.md
  - ./CANONICALIZATION.md
  - ../doctrine/directory-rules.md
  - ../architecture/contract-schema-policy-split.md
  - ../../contracts/domains/fauna/occurrence_evidence.md
  - ../../contracts/domains/fauna/occurrence_public.md
  - ../../contracts/domains/fauna/occurrence_restricted.md
  - ../../schemas/contracts/v1/domains/fauna/occurrence_evidence.schema.json
  - ../../tools/validators/domains/fauna/occurrence/validate_occurrence_evidence.py
  - ../../tools/validators/biodiversity/README.md
tags: [kfm, standards, darwin-core, tdwg, biodiversity, fauna, flora, occurrence, event, data-package, dwca, interoperability]
notes:
  - "Same-path documentation modernization only; no contract, schema, policy, source, fixture, validator, workflow, lifecycle object, release, deployment, or public artifact changes."
  - "The prior claim that nested snake_case properties.taxon is already the KFM canonical Darwin Core encoding is narrowed to a proposed mapping/profile relationship."
  - "The current executable Fauna slice validates standalone OccurrenceEvidence, not a STAC Item, DwC-A, or DwC-DP package."
  - "Byte-for-byte equivalence between STAC JSON and Darwin Core package forms is withdrawn; future conformance must define semantic and identity-preserving mappings explicitly."
  - "All legacy section anchors are retained for inbound-link compatibility."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>
<a id="darwin-core-dwc--kfm-conformance-and-profile"></a>

# Darwin Core — KFM Standards Boundary, Mapping, and Graduation Plan

> **Purpose.** Explain what the official Darwin Core standard provides, how its terms may map to current KFM biodiversity objects, where repository evidence stops, and what must close before KFM claims Darwin Core conformance or releases a Darwin Core package.

![status](https://img.shields.io/badge/status-v2.0--draft-yellow)
![evidence](https://img.shields.io/badge/evidence-repository--grounded-success)
![upstream](https://img.shields.io/badge/Darwin%20Core-current-blue)
![terms](https://img.shields.io/badge/terms-2026--05--26-blueviolet)
![adoption](https://img.shields.io/badge/KFM%20profile-NOT%20ESTABLISHED-orange)
![publication](https://img.shields.io/badge/publication-none-critical)

> [!IMPORTANT]
> **A standards page is not conformance proof.** This document does not adopt Darwin Core for KFM, define a canonical KFM biodiversity package, change object meaning or machine shape, admit a source, certify a mapping, authorize sensitive-location exposure, approve a release, or prove interoperability with any external consumer.

> [!CAUTION]
> **Current KFM machine evidence is not a STAC × DwC implementation.** The repository has a closed `OccurrenceEvidence` schema and a deterministic no-network validator for a standalone Fauna object. That slice does not emit a STAC Item, Darwin Core Archive, Darwin Core Data Package, RDF graph, or external interoperability proof.

> [!WARNING]
> **Do not publish nested KFM aliases as though they were canonical Darwin Core terms.** Keys such as `taxon.scientific_name`, `observation.event_date`, and `geometry.latitude` are KFM fields. They may map to Darwin Core IRIs through a reviewed profile, but external Darwin Core consumers will not infer that mapping merely from similar names.

| Field | Current bounded result |
|---|---|
| **Directory result** | `PLACE` at the existing `docs/standards/Darwin_Core.md` path; human-readable external-standard guidance belongs in the standards lane |
| **Official upstream status** | Darwin Core is a current TDWG technical standard, ratified 2009-10-09 |
| **Current vocabulary baseline** | Darwin Core List of Terms dated **2026-05-26** |
| **Current structural additions** | Darwin Core Conceptual Model and Darwin Core Data Package Guide dated **2026-05-26** |
| **July 2026 review** | Active discussion ended 2026-08-15; unratified proposals remain review material, not this document's normative baseline |
| **KFM adoption/profile state** | **UNKNOWN / NEEDS VERIFICATION**; no accepted KFM Darwin Core application profile was established in this review |
| **Current machine slice** | `OccurrenceEvidence` contract, closed Draft 2020-12 schema, deterministic validator, fixtures/tests, and a focused workflow exist for a bounded Fauna object |
| **Public occurrence state** | `OccurrencePublic` meaning exists, but its paired schema remains a permissive proposal-era scaffold |
| **Cross-domain biodiversity validator** | Parent lane is README-only; no executable parent composition validator was established |
| **STAC × DwC profile family** | Four overlapping standards documents exist; their canonical relationship is unresolved and remains on `HOLD` |
| **Release/publication effect** | None |

**Quick navigation:** [Scope](#1-scope-and-role-at-kfm) · [Upstream](#2-source-standard-reference-tdwg) · [Representations](#3-kfm-canonical-encoding-the-stac--dwc-hybrid) · [Mapping](#4-term-map--dwc--kfm-propertiestaxon) · [Classes](#5-event-records-and-measurementorfact) · [Taxonomy](#6-taxonomic-authority-anchoring) · [Sensitivity](#7-sensitivity-redaction-and-public-safety-gates) · [Intake/export](#8-source-intake--dwc-a-archives-and-live-apis) · [Repository](#9-schema-home-validators-and-fixtures) · [Example](#10-worked-example-illustrative) · [Questions](#11-open-questions-and-verification-backlog) · [Evidence](#12-related-docs) · [Term reference](#appendix-a--dwc-term-cheat-sheet) · [Review checklist](#appendix-b--conformance-checklist)

---

<a id="1-scope-and-role-at-kfm"></a>

## 1. Scope, authority, and role at KFM

### 1.1 What this page owns

This page owns human-readable guidance for:

- the official Darwin Core baseline and version posture;
- the difference among Darwin Core vocabulary, conceptual model, controlled vocabularies, and exchange representations;
- a bounded candidate mapping between Darwin Core terms and current KFM biodiversity objects;
- the current repository evidence and implementation limits;
- the overlap among KFM's Darwin Core and STAC-DwC documentation;
- the rights, sensitivity, source-role, evidence, release, correction, and rollback boundaries that remain independent of Darwin Core; and
- the graduation evidence required before KFM may claim conformance.

### 1.2 What this page does not own

| Question | Owning authority |
|---|---|
| Where this guidance belongs | Adopted Directory Rules, accepted ADRs, and [`docs/standards/README.md`](./README.md) |
| What `OccurrenceEvidence`, `OccurrencePublic`, or another KFM object means | `contracts/`, especially the Fauna occurrence contracts |
| What machine shape is valid | `schemas/` and its accepted schema-home rules |
| What is allowed, denied, generalized, withheld, quarantined, or abstained | `policy/`, source terms, sensitivity controls, and governed review |
| Whether a source may be used | Source admission, rights review, `SourceDescriptor`, and source registry |
| Whether a mapping or exporter works | Exact-revision code, fixtures, validators, tests, generated reports, and observed producer/consumer behavior |
| Whether evidence supports a claim | `EvidenceRef` resolution to `EvidenceBundle` and applicable evidence authorities |
| Whether an artifact may release or publish | Review, proof, release, correction, withdrawal, and rollback authorities |
| What Darwin Core normatively means | TDWG's official Darwin Core standard, term IRIs, definitions, and normative guides |

### 1.3 Non-effects

This same-path revision does **not**:

- accept `properties.taxon` or any sibling STAC-DwC document as KFM's canonical biodiversity representation;
- select DwC-A, DwC-DP, Simple Darwin Core, RDF, XML, or STAC as the canonical KFM export;
- modify the current occurrence contracts, schemas, fixtures, validator, tests, or workflow;
- create a term mirror, mapping table, package schema, source adapter, or profile identifier;
- activate GBIF, iNaturalist, eBird, iDigBio, Symbiota, NatureServe, KDWP, a herbarium, or another source;
- approve a taxonomic backbone or conflict-resolution rule;
- disclose or authorize exact sensitive locations;
- release, deploy, publish, or claim external interoperability.

### 1.4 KFM operating boundary

Darwin Core is an external interoperability standard. It does not replace KFM's trust membrane:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A Darwin Core-valid record can still be inadmissible, under-supported, rights-restricted, sensitive, unreleased, stale, corrected, withdrawn, or unsafe for the requested audience. Conversely, a current KFM occurrence object can be useful inside KFM without yet conforming to a Darwin Core exchange profile.

[Back to top](#top)

---

<a id="2-source-standard-reference-tdwg"></a>

## 2. Official upstream baseline and currentness

### 2.1 Standard identity

| Surface | Official identity | Current bounded use |
|---|---|---|
| Darwin Core standard | [`http://www.tdwg.org/standards/450`](http://www.tdwg.org/standards/450) | Permanent citation IRI; current TDWG technical standard |
| Main term namespace | [`http://rs.tdwg.org/dwc/terms/`](http://rs.tdwg.org/dwc/terms/) | Canonical term IRIs such as `dwc:scientificName` |
| IRI-valued namespace | [`http://rs.tdwg.org/dwc/iri/`](http://rs.tdwg.org/dwc/iri/) | Terms intended for non-literal objects in RDF-oriented use |
| Current List of Terms | [`http://rs.tdwg.org/dwc/doc/list/2026-05-26`](http://rs.tdwg.org/dwc/doc/list/2026-05-26) | Current term definitions and metadata reviewed for this page |
| Current vocabulary version | [`http://rs.tdwg.org/version/dwc/2026-05-26`](http://rs.tdwg.org/version/dwc/2026-05-26) | Candidate version pin for any future KFM mapping profile |
| Conceptual Model | [`http://rs.tdwg.org/dwc/doc/cm/2026-05-26`](http://rs.tdwg.org/dwc/doc/cm/2026-05-26) | Technology-neutral class relationship guidance |
| Data Package Guide | [`http://rs.tdwg.org/dwc/doc/dp/2026-05-26`](http://rs.tdwg.org/dwc/doc/dp/2026-05-26) | Normative DwC-DP package requirements except sections marked non-normative |
| Text Guide | [`http://rs.tdwg.org/dwc/doc/text/2023-09-13`](http://rs.tdwg.org/dwc/doc/text/2023-09-13) | Current dated guidance for Darwin Core text / archive implementation |
| Humboldt Extension | [`http://rs.tdwg.org/dwc/doc/eco/2024-03-26`](http://rs.tdwg.org/dwc/doc/eco/2024-03-26) | Official vocabulary for ecological inventories and survey context; KFM adoption not established |

The official term list contains recommended terms from `dwc:`, `dwciri:`, `dc:`, and `dcterms:` namespaces. Deprecation and replacement metadata matter: a KFM profile must not treat every historical term as current merely because it can be resolved.

### 2.2 What changed since the prior KFM page

The prior page cited the 2025-07-10 List of Terms and described Darwin Core primarily as terms plus DwC-A. The current official baseline is broader:

- the List of Terms was issued on 2026-05-26;
- the Darwin Core Conceptual Model now describes relationships among Darwin Core classes without prescribing a technology;
- the Darwin Core Data Package Guide defines a Frictionless Data-based exchange package for that model;
- DwC-A remains a supported text representation rather than the only package option; and
- controlled vocabularies and extension vocabularies are distinct versioned surfaces.

### 2.3 July 2026 review boundary

TDWG opened another public-review cycle on 2026-07-16. It includes proposed term additions for mineralogical collections, initial schemas implementing the Conceptual Model and DwC-DP, and other post-ratification issues. Active discussion was expected to conclude on 2026-08-15; unresolved issues move to a later cycle.

Therefore:

- **CONFIRMED:** the 2026-05-26 ratified terms/model/package documents are the current baseline used here.
- **NEEDS VERIFICATION:** any proposal from the July review that receives later ratification.
- **DENY:** silently pinning review-branch schemas or proposed terms as the KFM production baseline before an official successor release is verified.

### 2.4 Version-pin rule

A future KFM Darwin Core profile must record, at minimum:

- the Darwin Core vocabulary version IRI;
- each controlled-vocabulary version it depends on;
- the selected representation/profile version;
- mapping-table identity and digest;
- source-native profile/version when one exists;
- producer and validator versions;
- release/correction lineage; and
- the exact artifact digest.

This page does not decide whether those pins belong in a profile manifest, `RunReceipt`, `ReleaseManifest`, source descriptor, or a combination. That ownership remains `NEEDS VERIFICATION`.

[Back to top](#top)

---

<a id="3-kfm-canonical-encoding-the-stac--dwc-hybrid"></a>

## 3. Darwin Core model and representation choices

The prior heading called the STAC × DwC hybrid “KFM canonical encoding.” Current repository evidence does not support that claim. The safe replacement is a representation matrix.

| Representation | Upstream role | Current KFM status |
|---|---|---|
| **Darwin Core terms** | Stable semantic vocabulary expressed through term IRIs and definitions | External reference baseline; no complete KFM mapping profile established |
| **Darwin Core Conceptual Model (DwC-CM)** | Explains class relationships independently of implementation technology | External structural guidance; no KFM class-binding decision established |
| **Simple Darwin Core** | Flat, simplified sharing form | No KFM producer/consumer established |
| **Darwin Core text / DwC-A** | Delimited core and extension files described by `meta.xml`, commonly packaged with metadata | Candidate batch import/export representation; no KFM round-trip implementation established |
| **Darwin Core Data Package (DwC-DP)** | Frictionless Data-based package implementing DwC-CM | Current external option; no KFM profile, schemas, or package producer established |
| **Darwin Core XML** | XML implementation guidance | No KFM implementation established |
| **Darwin Core RDF** | RDF use of Darwin Core terms and IRI-valued terms | No KFM RDF producer/consumer established |
| **STAC × DwC mapping** | KFM-proposed spatial/catalog projection combining a STAC envelope with biodiversity semantics | Multiple draft documents exist; adoption, machine shape, producer, validator, and consumer remain unresolved |
| **KFM `OccurrenceEvidence`** | Standalone source-bound Fauna object before public/restricted split | Current bounded repository implementation; not itself a Darwin Core representation |

### 3.1 Semantic preservation, not byte equality

The prior page proposed byte-for-byte agreement after canonicalization between a STAC Item and DwC-A. That is not a sound general conformance target because the representations have different containers, metadata, ordering, field names, relationship mechanisms, and serialization rules.

A future round-trip claim must instead define:

1. **identity preservation** — which source and KFM identifiers survive;
2. **semantic preservation** — which Darwin Core term values and class relationships survive;
3. **cardinality preservation** — how one-to-many records and extensions survive;
4. **null and absence semantics** — whether absent, empty, unknown, and withheld remain distinct;
5. **rights and sensitivity preservation** — what must not be exported and which public-safe transform is represented;
6. **temporal preservation** — source, event, retrieval, valid, release, and correction times;
7. **ordering/canonicalization boundary** — which representation, if any, has deterministic bytes;
8. **loss report** — any field or relationship omitted, generalized, renamed, or downcast; and
9. **replay evidence** — mapping version, fixtures, validator result, and artifact digest.

Exact byte equality is appropriate only when replaying the *same representation* under the same canonicalization contract.

### 3.2 Source form, KFM form, and distribution form

These states must remain separate:

```text
source-native DwC / API / archive
        |
        v
KFM source-bound object + evidence + rights + sensitivity
        |
        v
reviewed mapping / public-safe transformation
        |
        v
selected distribution profile (DwC-A, DwC-DP, STAC projection, other)
        |
        v
release manifest + correction / withdrawal / rollback
```

No distribution form replaces the source-native capture or KFM evidence authority.

[Back to top](#top)

---

<a id="4-term-map--dwc--kfm-propertiestaxon"></a>

## 4. Candidate KFM-to-Darwin Core mapping boundary

### 4.1 Current executable KFM object

The current closed `OccurrenceEvidence` schema requires a standalone object with:

- source record identity, source family, and canonical source role;
- a `taxon` object;
- an `observation` object;
- exact/internal and explicit public-safe geometry;
- rights and sensitivity objects;
- provenance and validation state;
- deterministic RFC 8785 JCS + SHA-256 identity; and
- finite validator handling.

That schema uses KFM snake_case keys and KFM-specific enums. The validator checks the bounded KFM profile; it does not dereference Darwin Core term IRIs, validate a DwC package, or certify external conformance.

### 4.2 Candidate field crosswalk

The table below is **PROPOSED mapping guidance**, not an adopted binding.

| Current KFM field | Candidate Darwin Core term | Mapping notes |
|---|---|---|
| `taxon.scientific_name` | `dwc:scientificName` | Candidate direct lexical mapping; preserve source value |
| `taxon.accepted_scientific_name` | `dwc:acceptedNameUsage` and/or an authority identifier | The accepted-name string and taxonomic concept identifier are different concerns |
| `taxon.common_name` | `dwc:vernacularName` | Language and source attribution require an explicit rule |
| `taxon.taxon_rank` | `dwc:taxonRank` | KFM enum is narrower than unrestricted source strings |
| `source_record_id` | `dwc:occurrenceID`, `dwc:materialEntityID`, `dwc:eventID`, or another identifier | Depends on what the source record represents; never map mechanically by filename |
| `observation.event_date` | `dwc:eventDate` | KFM currently requires a date; Darwin Core can carry richer ranges/values |
| `observation.event_time` | `dwc:eventTime` | Preserve timezone and source precision |
| `observation.basis_of_record` | `dwc:basisOfRecord` only for compatible values | Several KFM values represent knowledge character or source role and are not Darwin Core basis-of-record vocabulary terms |
| `observation.observation_method` | `dwc:samplingProtocol` or `dwc:recordedBy`-adjacent context | Exact mapping depends on event/occurrence semantics |
| `observation.observed_by` | `dwc:recordedBy` / `dwc:recordedByID` | Living-person, privacy, and stable-identifier review remains independent |
| `observation.individual_count` | `dwc:individualCount` | Preserve unknown versus observed zero |
| `geometry.latitude` | `dwc:decimalLatitude` | Internal exact values may be withheld from a public package |
| `geometry.longitude` | `dwc:decimalLongitude` | Same sensitivity boundary as latitude |
| `geometry.precision_class` | `dwc:coordinateUncertaintyInMeters` plus KFM policy metadata | A KFM class label does not equal a numeric uncertainty |
| `geometry.geoprivacy_status` | No single core DwC equivalent | KFM policy/source posture; package-specific mapping needed |
| `geometry.public_safe_geometry` | Distribution-specific location fields or geometry asset | KFM public-safe derivative, not source evidence |
| `rights.license` | `dcterms:license` | Preserve source-level licensing and record-level variation |
| `rights.attribution_required` | `dcterms:bibliographicCitation`, `dcterms:rightsHolder`, or KFM release obligations | No single boolean Darwin Core equivalent |
| `source_role` | No single Darwin Core term | KFM anti-collapse vocabulary; retain as namespaced extension or package metadata |
| `sensitivity.*` | No single Darwin Core term | KFM policy/review state; never infer from Darwin Core validity |
| `provenance.evidence_refs` | No single Darwin Core term | KFM evidence authority; may be linked through package metadata or a namespaced extension |
| `validation.*` | No single Darwin Core term | KFM validator state; not part of biological semantics |

### 4.3 Basis-of-record anti-collapse

Current KFM `observation.basis_of_record` includes direct forms such as human observation, machine observation, preserved specimen, material sample, living specimen, fossil specimen, and literature record. It also includes administrative, regulatory, aggregate, model, candidate, and synthetic values.

A Darwin Core export must not misrepresent those latter knowledge characters as direct occurrences. The mapper must either:

- map to a legitimate Darwin Core class/term combination with explicit context;
- carry a reviewed KFM extension while preserving source role;
- emit a narrowed aggregate/model/candidate package profile; or
- return `ABSTAIN` / `DENY` for the requested export.

### 4.4 Names and IRIs

KFM aliases may improve local implementation ergonomics, but a conformance profile must bind each alias to a canonical term IRI. The normative anchor is the term IRI and definition, not an English label or a snake_case spelling.

A mapping registry should eventually include:

```yaml
mapping_id: kfm-dwc-occurrence-mapping-v1
darwin_core_version: http://rs.tdwg.org/version/dwc/2026-05-26
entries:
  - kfm_pointer: /taxon/scientific_name
    term_iri: http://rs.tdwg.org/dwc/terms/scientificName
    direction: bidirectional
    transform: identity_string
    loss_class: none
  - kfm_pointer: /source_role
    term_iri: null
    direction: export
    transform: kfm_extension
    loss_class: none_if_extension_preserved
```

This example is illustrative. No registry path, schema, identifier, or transform is adopted here.

[Back to top](#top)

---

<a id="5-event-records-and-measurementorfact"></a>

## 5. Classes, Events, and MeasurementOrFact

The 2026 Darwin Core Conceptual Model clarifies relationships among Darwin Core classes without prescribing a specific implementation technology. That is useful pressure for KFM because occurrence evidence can involve a Taxon, Organism, MaterialEntity, Occurrence, Event, Location, GeologicalContext, Identification, MeasurementOrFact, and ResourceRelationship.

### 5.1 Do not flatten class identity

A future KFM mapper must first determine what each record *is*.

| KFM/source subject | Likely Darwin Core class pressure | Caution |
|---|---|---|
| Observation/detection record | `dwc:Occurrence` | Occurrence is not automatically a taxon record or event |
| Specimen/sample | `dwc:MaterialEntity` with occurrence/event context | Preserve institution, catalog, and preparation identity |
| Survey/checklist/transect | `dwc:Event` | Event hierarchy and sampling design may require DwC-DP/Humboldt modeling |
| Taxonomic assertion | `dwc:Taxon` and `dwc:Identification` | Name usage, concept, identification event, and accepted status differ |
| Measurement | `dwc:MeasurementOrFact` | State the subject and measurement context |
| Relationship | `dwc:ResourceRelationship` | Preserve subject/object identity and relationship semantics |
| Aggregate/model/candidate | No automatic class conversion | Keep KFM source role and knowledge character explicit |

### 5.2 Event and measurement mapping

The prior page proposed `properties.event` and inline `properties.measurements`. Those remain possible **KFM profile designs**, not current implementation facts.

A reviewed event mapping should establish:

- event identity and hierarchy;
- event time and source precision;
- location and geometry support;
- sampling protocol and effort;
- target taxonomic, life-stage, sex, habitat, and scope constraints;
- whether absence/non-detection is meaningful;
- measurement subject, unit, accuracy, method, and identifier;
- complete-checklist or inventory-completeness semantics;
- Humboldt Extension use where appropriate;
- sensitive-location transformation; and
- correction/supersession behavior.

### 5.3 Inline versus relational representation

Inline measurements can be convenient for a small JSON projection. DwC-A extensions and DwC-DP tables support relational/package forms. KFM must not choose solely by convenience.

The decision must account for:

- cardinality and streaming;
- stable row identity;
- event and occurrence joins;
- package round-trip;
- query and correction behavior;
- evidence and source lineage;
- sensitivity inheritance;
- validator complexity; and
- consumer expectations.

Until a contract, schema, fixtures, producer, validator, and consumer agree, the inline/split threshold remains `UNKNOWN`.

[Back to top](#top)

---

<a id="6-taxonomic-authority-anchoring"></a>

## 6. Taxonomic identity and authority boundaries

Darwin Core provides terms for taxonomic names, identifiers, classifications, and identifications. It does not select KFM's taxonomic backbone or resolve conflicts among ITIS, GBIF, Catalogue of Life, taxonomic specialists, source institutions, and other authorities.

### 6.1 Current repository state

The current `OccurrenceEvidence` machine shape requires:

- `scientific_name`;
- `accepted_scientific_name`;
- `common_name`; and
- `taxon_rank`.

It does **not** currently require an ITIS TSN, GBIF key, backbone DOI/version, name-usage identifier, identification record, or crosswalk object. The current validator checks accepted-name normalization but does not perform network taxonomy resolution.

Therefore the prior claim that every species-level record already “must anchor to ITIS or GBIF” is narrowed to a **proposed graduation requirement**, not current behavior.

### 6.2 Candidate identity packet

A future profile should distinguish:

| Concern | Candidate field/evidence |
|---|---|
| Source-supplied name | Verbatim scientific name and authorship |
| Source taxon identifier | Source-native stable identifier |
| Interpreted accepted usage | Accepted-name usage identifier and name |
| Taxonomic backbone | Authority name, release/version, identifier, retrieval evidence |
| Identification event | Who/what identified the material or occurrence, when, and under which method |
| Conflicts | Competing names/usages, match type, score only as secondary evidence, steward disposition |
| Correction | Reidentification, synonym change, backbone update, supersession lineage |

A numeric match score cannot silently decide taxonomic truth. Ambiguous or conflicting matches should produce a reviewable candidate and a finite `ABSTAIN`, `DENY`, or `HOLD` posture for consequential use.

### 6.3 Backbones do not replace source evidence

An external taxonomic backbone can normalize identity and enable federation. It does not prove:

- that an occurrence happened;
- that a specimen is correctly identified;
- that coordinates are accurate;
- that use is rights-cleared;
- that a taxon is safe to expose; or
- that a KFM release is current.

[Back to top](#top)

---

<a id="7-sensitivity-redaction-and-public-safety-gates"></a>

## 7. Rights, sensitivity, redaction, and public safety

Darwin Core validity has no automatic public-safety effect.

### 7.1 Independent gates

Before any Darwin Core-bearing package is public or semi-public, KFM must independently resolve:

- source identity and authority role;
- source and record-level license/rights;
- attribution and redistribution obligations;
- living-person or observer privacy where applicable;
- taxon and site sensitivity;
- exact-location and reconstructability risk;
- private-land, cultural, sovereign, or steward restrictions;
- evidence support and source-role caveats;
- named public-safe transform and transform receipt;
- review and separation-of-duties requirements;
- release state, correction path, withdrawal path, and rollback target.

### 7.2 Current KFM occurrence split

The repository distinguishes:

| Object | Current role | Publication consequence |
|---|---|---|
| `OccurrenceEvidence` | Source-bound record before public/restricted split | Never publication authority by itself |
| `OccurrenceRestricted` | Restricted/steward-controlled semantic sibling | Machine enforcement remains to be verified |
| `OccurrencePublic` | Intended public-safe semantic sibling | Meaning exists; paired schema is still permissive and does not prove release readiness |

The implemented `OccurrenceEvidence` schema explicitly separates internal geometry from `public_safe_geometry`, rights from sensitivity, and validation from publication. That separation should survive any Darwin Core export.

### 7.3 Most-restrictive projection rule

A distribution package must not become less restrictive merely because a target format lacks KFM fields. When a selected Darwin Core representation cannot carry a necessary sensitivity, rights, evidence, or release obligation safely, KFM must:

- include a governed namespaced extension or package metadata binding;
- publish a generalized/aggregated derivative;
- stage access;
- omit the unsafe distribution;
- or return `DENY`.

Dropping a restriction during export is a conformance failure even if the resulting file is valid Darwin Core.

### 7.4 No policy by taxonomy shorthand

NatureServe, federal, state, tribal, institutional, or partner status may inform policy. No single rank, list membership, or taxonomic field automatically decides public precision. The decision must be policy-versioned, evidence-backed, reviewable, and correctable.

[Back to top](#top)

---

<a id="8-source-intake--dwc-a-archives-and-live-apis"></a>

## 8. Source intake and distribution packages

### 8.1 Source admission precedes parsing

A source that emits Darwin Core is not automatically admitted. Before retrieval or use, KFM still needs a source descriptor and review appropriate to:

- source identity and authority;
- endpoint or archive identity;
- access method and authentication;
- terms, license, attribution, and redistribution;
- update cadence and correction behavior;
- record-level license variation;
- sensitive fields and precision;
- stable identifiers and deletion/tombstone semantics;
- expected profile/version; and
- permitted lifecycle and audience.

### 8.2 DwC-A intake boundary

A Darwin Core Archive commonly includes a `meta.xml` descriptor, a core delimited file, optional extension files, and often `eml.xml` metadata. A safe KFM intake should eventually:

1. preserve the original archive or immutable reference and digest;
2. validate archive safety and resource limits before extraction;
3. parse `meta.xml` rather than infer columns by order or filename;
4. preserve core/extension identifiers and row relationships;
5. record the source profile and term IRIs;
6. distinguish malformed, unknown, deprecated, and extension terms;
7. bind rights and attribution at the correct dataset/record level;
8. retain source-native values before normalization;
9. emit mapping and validation reports;
10. quarantine unresolved rights, identity, sensitivity, or relationship failures; and
11. create no public derivative until policy/review/release closure.

No current KFM DwC-A parser, archive validator, or round-trip producer was established in this review.

### 8.3 DwC-DP boundary

DwC-DP is now an official normative package guide based on Frictionless Data and implementing the Darwin Core Conceptual Model. Its existence does not automatically make it KFM's preferred format.

A KFM decision should compare DwC-DP and DwC-A for:

- class/relationship fidelity;
- schema validation;
- identifier preservation;
- ecosystem/tool support;
- package size and streaming;
- source compatibility;
- rights/sensitivity metadata;
- deterministic build and digest behavior;
- correction and incremental update behavior; and
- external consumers KFM actually needs to support.

### 8.4 Live API boundary

API JSON that uses Darwin Core-like field names is not necessarily a complete Darwin Core package or profile. Each adapter must preserve:

- source-native identity and fields;
- query/pagination parameters;
- response version and headers;
- retrieval time and digest;
- omitted or interpreted fields;
- per-record license and geoprivacy;
- source-side corrections/deletions; and
- the mapping version used.

Live network access, source activation, and operational credentials remain outside this documentation change.

[Back to top](#top)

---

<a id="9-schema-home-validators-and-fixtures"></a>

## 9. Current repository implementation and authority map

### 9.1 Confirmed bounded implementation

| Surface | Current evidence | Safe conclusion |
|---|---|---|
| `contracts/domains/fauna/occurrence_evidence.md` | v0.3 semantic contract | Defines source-bound Fauna occurrence evidence before public/restricted split |
| `schemas/contracts/v1/domains/fauna/occurrence_evidence.schema.json` | Closed Draft 2020-12 schema | Enforces a KFM-specific machine shape, not Darwin Core package conformance |
| `tools/validators/domains/fauna/occurrence/validate_occurrence_evidence.py` | Deterministic no-network validator | Checks schema, identity, source-role/basis, rights, geometry, sensitivity, and finite-state consistency |
| `fixtures/domains/fauna/occurrence_evidence/` and tests | Referenced by the contract/validator | Bounded fixture-first proof for the KFM object |
| `contracts/domains/fauna/occurrence_public.md` | Expanded semantic contract | Defines intended public-safe meaning; machine enforcement remains incomplete |
| `tools/validators/biodiversity/README.md` | README-only parent | Coordinates future cross-domain composition; no executable parent validator established |

### 9.2 Not established by exact-path checks

The review did not establish:

- `schemas/contracts/v1/biodiversity/stac_dwc_profile.schema.json`;
- `schemas/contracts/v1/domains/fauna/stac_dwc_profile.schema.json`;
- a Darwin Core term mapping registry;
- a DwC-A or DwC-DP parser/exporter;
- a Darwin Core package validator;
- an executable cross-domain biodiversity parent validator;
- a released STAC-DwC profile schema URL;
- a production consumer that round-trips KFM biodiversity data; or
- an immutable released Darwin Core package.

A bounded search result is not proof of permanent absence. These remain `UNKNOWN` outside the exact paths and evidence inspected.

### 9.3 Documentation overlap register

`DWC-DRIFT-001 — CONFLICTED / HOLD`

| Document | Declared role | Current issue |
|---|---|---|
| `Darwin_Core.md` | External standard/conformance description | This revision narrows it to upstream reference, current-state map, and graduation boundary |
| `STAC-DwC.md` | STAC × DwC hybrid profile | Proposal-era implementation and authority claims require reconciliation |
| `STAC_DWC_PROFILE.md` | Named KFM STAC-DwC profile | Separate profile identity and field model; no adoption proof established |
| `stac-dwc-hybrid.md` | Lowercase named hybrid profile | Overlaps the two profile documents with additional casing and field differences |

This update does not rename, delete, merge, tombstone, redirect, or select a winner. A separate convergence packet must inspect:

- stable document identities;
- full semantic overlap and contradictions;
- inbound links and fragments;
- schemas, fixtures, validators, producers, and consumers;
- naming/case portability;
- accepted ADR or standards-owner authority;
- migration, alias, rollback, and supersession requirements.

### 9.4 Responsibility split for future work

| Responsibility | Owning root |
|---|---|
| External-standard guidance and mapping explanation | `docs/standards/` |
| KFM occurrence/event/package meaning | `contracts/` |
| Machine profile and mapping-registry shape | `schemas/` |
| Source identity, terms, rights, cadence | source registry and `docs/sources/` |
| Admissibility, sensitivity, geoprivacy, export obligations | `policy/` |
| Mapper/exporter/parser implementation | appropriate package/tool/connector root after placement review |
| Positive/negative package fixtures | `fixtures/` |
| Deterministic validation and round-trip tests | `tools/validators/` and `tests/` |
| Evidence, receipts, proofs, and catalog closure | their owning data/control roots |
| Release, correction, withdrawal, rollback | `release/` and accepted correction authorities |

[Back to top](#top)

---

<a id="10-worked-example-illustrative"></a>

## 10. Worked mapping example — illustrative, not a contract

The example below shows a source-bound KFM object and a *candidate* Darwin Core projection. It intentionally omits real coordinates and identifiers.

### 10.1 KFM source-bound input

```json
{
  "object_type": "occurrence_evidence",
  "schema_version": "v1",
  "source_record_id": "synthetic-source-record-001",
  "source_family": "other",
  "source_role": "observed",
  "taxon": {
    "scientific_name": "Example species",
    "accepted_scientific_name": "Example species",
    "common_name": null,
    "taxon_rank": "species"
  },
  "observation": {
    "event_date": "2026-01-15",
    "event_time": null,
    "basis_of_record": "human_observation",
    "observation_method": "synthetic fixture",
    "observed_by": null,
    "individual_count": 1
  },
  "geometry": {
    "latitude": null,
    "longitude": null,
    "precision_class": "withheld",
    "geoprivacy_status": "withheld",
    "public_safe_geometry": {
      "geometry_type": "withheld",
      "coordinates": null,
      "precision_class": "withheld",
      "generalization_method": null
    }
  }
}
```

The complete current schema also requires rights, sensitivity, provenance, validation, and deterministic identity fields. They are omitted here to focus on mapping; this fragment is **not** schema-valid.

### 10.2 Candidate Darwin Core row

```json
{
  "occurrenceID": "synthetic-source-record-001",
  "scientificName": "Example species",
  "acceptedNameUsage": "Example species",
  "taxonRank": "species",
  "eventDate": "2026-01-15",
  "basisOfRecord": "HumanObservation",
  "individualCount": 1,
  "informationWithheld": "Location withheld under KFM public-safety policy",
  "dataGeneralizations": "No public coordinates emitted"
}
```

### 10.3 Required companion evidence before this could be a KFM release

A real export would still need:

- a source and mapping profile;
- exact term and controlled-vocabulary version pins;
- rights and attribution fields;
- evidence and provenance linkage;
- review of whether `occurrenceID` may be disclosed;
- a public-safe transform/review record;
- deterministic package construction and validation;
- a release manifest and artifact digest;
- correction, withdrawal, and rollback paths; and
- a consumer or interoperability test appropriate to the claim.

The example does not establish that the listed fields are the final KFM export subset.

[Back to top](#top)

---

<a id="11-open-questions-and-verification-backlog"></a>

## 11. Conformance graduation and open verification backlog

### 11.1 Dependency-ordered graduation plan

| Gate | Required evidence | Failure posture |
|---|---|---|
| 1. Upstream baseline | Official Darwin Core version, term IRIs, controlled vocabularies, representation guide | `HOLD` on unratified review material |
| 2. Document-role convergence | One reviewed relationship among `Darwin_Core.md` and the three STAC-DwC siblings | `HOLD`; no silent winner |
| 3. Scope decision | Named object families and uses: occurrence, material entity, event, measurement, inventory, package/export | `ABSTAIN` on unspecified scope |
| 4. Mapping contract | Versioned field/class/relationship mapping with loss and null semantics | `ERROR` on ambiguous or undeclared mapping |
| 5. Representation decision | DwC-A, DwC-DP, STAC projection, RDF/XML, or bounded combination | `HOLD` pending producer/consumer need |
| 6. Machine shape | Closed schemas for mapping manifest and selected package/profile | `ERROR` on invalid shape |
| 7. Fixtures | Public-safe positive and negative fixtures, including rights, sensitivity, class, relationship, and correction cases | `DENY` on sensitive fixture leakage |
| 8. Implementation | Deterministic parser/mapper/exporter with no hidden network calls | `ERROR` on nondeterminism or undeclared fetch |
| 9. Validation | Term-version, controlled-vocabulary, package, round-trip/loss, rights, sensitivity, evidence, and identity checks | Finite findings; no broad “valid” claim |
| 10. Producer/consumer proof | At least one KFM producer and intended consumer agree on the frozen profile | `ABSTAIN` on documentation-only conformance |
| 11. Release closure | Evidence, policy, review, proof, artifact digest, release manifest, correction and rollback | `DENY` publication without closure |
| 12. Maintenance | Upstream watch, deprecation handling, migration, replay, withdrawal, and compatibility window | `HOLD` on unowned drift |

### 11.2 Open decisions

| ID | Question | Status |
|---|---|---|
| `DWC-OQ-001` | Which KFM document, if any, owns the STAC-DwC application profile after convergence? | `HOLD` |
| `DWC-OQ-002` | Is a STAC projection needed for per-record occurrences, dataset assets, only released public derivatives, or none? | `NEEDS VERIFICATION` |
| `DWC-OQ-003` | Which exchange target is required first: DwC-A, DwC-DP, both, or another bounded consumer profile? | `NEEDS VERIFICATION` |
| `DWC-OQ-004` | Which current KFM object families map to `Occurrence`, `MaterialEntity`, `Event`, `Taxon`, `Identification`, `MeasurementOrFact`, and `ResourceRelationship`? | `NEEDS VERIFICATION` |
| `DWC-OQ-005` | Which term aliases and KFM extensions are admitted, and where is their machine registry owned? | `NEEDS VERIFICATION` |
| `DWC-OQ-006` | Which controlled vocabularies and versions are mandatory for each profile? | `NEEDS VERIFICATION` |
| `DWC-OQ-007` | Which taxonomic backbone(s), versions, match classes, and steward rules control accepted-name interpretation? | `NEEDS VERIFICATION` |
| `DWC-OQ-008` | How are non-observed source roles and model/aggregate/candidate records represented without becoming occurrence truth? | `NEEDS VERIFICATION` |
| `DWC-OQ-009` | Which public-safe terms may disclose withholding/generalization without enabling reconstruction? | `NEEDS VERIFICATION` |
| `DWC-OQ-010` | What semantic-loss threshold blocks an export, and how is the loss report bound to the artifact? | `NEEDS VERIFICATION` |
| `DWC-OQ-011` | How are deletions, reidentifications, taxonomic changes, source corrections, rights changes, and sensitivity changes propagated? | `NEEDS VERIFICATION` |
| `DWC-OQ-012` | Is Humboldt Extension support required for KFM inventory/checklist use cases? | `NEEDS VERIFICATION` |
| `DWC-OQ-013` | What does external conformance mean: package validity, term mapping, consumer ingestion, round-trip fidelity, or all of these? | `DECISION REQUIRED` |
| `DWC-OQ-014` | Who provides accountable biodiversity/taxonomy review and independent release review? | `UNKNOWN` |

### 11.3 Negative-path minimums

Any future profile should prove at least:

- unknown or deprecated term;
- invalid controlled-vocabulary value;
- ambiguous KFM-to-DwC field mapping;
- source-role/basis-of-record collapse;
- lost one-to-many relationship;
- absent source/version pin;
- unresolved taxonomic conflict;
- missing or conflicting rights;
- sensitive location without approved public-safe transform;
- withheld value reintroduced by a join;
- identifier disclosure not approved for public use;
- malformed or unsafe archive/package;
- mapping digest mismatch;
- nondeterministic rebuild;
- correction not propagated;
- withdrawn record retained in a public package;
- unsupported consumer/profile version; and
- missing rollback target.

[Back to top](#top)

---

<a id="12-related-docs"></a>

## 12. Evidence ledger and related docs

### 12.1 Repository evidence

| Surface | What it supports | What it does not prove |
|---|---|---|
| [`docs/standards/README.md`](./README.md) | Standards-lane responsibility, state separation, current sibling inventory | Darwin Core adoption or conformance |
| [`contracts/domains/fauna/occurrence_evidence.md`](../../contracts/domains/fauna/occurrence_evidence.md) | Current source-bound occurrence semantics and implementation boundary | Public release or Darwin Core mapping |
| [`schemas/contracts/v1/domains/fauna/occurrence_evidence.schema.json`](../../schemas/contracts/v1/domains/fauna/occurrence_evidence.schema.json) | Closed current KFM shape | STAC, DwC-A, DwC-DP, or external package validity |
| [`tools/validators/domains/fauna/occurrence/validate_occurrence_evidence.py`](../../tools/validators/domains/fauna/occurrence/validate_occurrence_evidence.py) | Deterministic bounded KFM validation | Source admission, taxonomy resolution, EvidenceBundle closure, or publication |
| [`contracts/domains/fauna/occurrence_public.md`](../../contracts/domains/fauna/occurrence_public.md) | Intended public-safe semantic boundary | Field-level machine enforcement or released public occurrence |
| [`tools/validators/biodiversity/README.md`](../../tools/validators/biodiversity/README.md) | Parent routing proposal and evidence limits | Executable cross-domain biodiversity validation |
| [`STAC-DwC.md`](./STAC-DwC.md), [`STAC_DWC_PROFILE.md`](./STAC_DWC_PROFILE.md), [`stac-dwc-hybrid.md`](./stac-dwc-hybrid.md) | Existing profile proposals and overlap evidence | Canonical profile identity or implementation |

### 12.2 Official upstream sources

- [TDWG Darwin Core standard](https://www.tdwg.org/standards/dwc/)
- [Darwin Core List of Terms — 2026-05-26](https://dwc.tdwg.org/list/)
- [Darwin Core Conceptual Model — 2026-05-26](https://dwc.tdwg.org/cm/)
- [Darwin Core Data Package Guide — 2026-05-26](https://dwc.tdwg.org/dp/)
- [Darwin Core Text Guide](https://dwc.tdwg.org/text/)
- [Darwin Core Quick Reference Guide](https://dwc.tdwg.org/terms/)
- [Humboldt Extension vocabulary](https://dwc.tdwg.org/eco/)
- [Darwin Core GitHub repository](https://github.com/tdwg/dwc)
- [July 2026 public-review announcement](https://www.tdwg.org/news/2026/dwc-july-review/)
- [August 2026 review-cycle reminder](https://www.tdwg.org/news/2026/dwc-july-review-reminder/)

### 12.3 Adjacent KFM guidance

- [`CANONICALIZATION.md`](./CANONICALIZATION.md) — repository-grounded JSON canonicalization boundary.
- [`EVIDENCE_BUNDLE.md`](./EVIDENCE_BUNDLE.md) — evidence documentation profile.
- [`SENSITIVITY_RUBRIC.md`](./SENSITIVITY_RUBRIC.md) and [`REDACTION_PROFILES.md`](./REDACTION_PROFILES.md) — sensitivity/redaction guidance; adoption and enforcement require their own evidence.
- [`STAC_KFM_PROFILE.md`](./STAC_KFM_PROFILE.md) — KFM STAC profile proposal; relationship to Darwin Core profiles remains subject to convergence.
- [`contract-schema-policy-split.md`](../architecture/contract-schema-policy-split.md) — authority separation.
- [`directory-rules.md`](../doctrine/directory-rules.md) — placement authority and non-effects.

[Back to top](#top)

---

<a id="appendix-a--dwc-term-cheat-sheet"></a>

## Appendix A — Darwin Core reference surface

This appendix is navigational, not a KFM normative subset.

### A.1 Common classes

| Class | Typical subject | KFM review pressure |
|---|---|---|
| `dwc:Event` | Sampling or collecting event | Event hierarchy, time, location, protocol, effort |
| `dwc:Occurrence` | Evidence of an organism at a place/time or associated with a material entity/event | Do not collapse model, aggregate, candidate, or administrative context |
| `dwc:Organism` | Particular organism or organismal entity | Identifier and privacy/sensitivity implications |
| `dwc:MaterialEntity` | Physical specimen, sample, or other material entity | Institution/catalog identity and custody |
| `dwc:Taxon` | Taxonomic name usage/concept context | Backbone/version and identification conflict |
| `dwc:Identification` | Assignment of taxonomic identity | Agent, date, evidence, method, correction |
| `dcterms:Location` | Spatial context | Exact/public-safe split and uncertainty |
| `dwc:GeologicalContext` | Geological/stratigraphic context | Source-role and geology-domain boundary |
| `dwc:MeasurementOrFact` | Measurement or factual assertion about a subject | Subject identity, unit, method, accuracy |
| `dwc:ResourceRelationship` | Typed relation between resources | Stable identifiers and relation semantics |

### A.2 Common term groups

| Group | Example term IRIs |
|---|---|
| Record and rights | `dcterms:type`, `dwc:basisOfRecord`, `dcterms:license`, `dcterms:rightsHolder`, `dcterms:bibliographicCitation` |
| Occurrence | `dwc:occurrenceID`, `dwc:recordedBy`, `dwc:recordedByID`, `dwc:individualCount`, `dwc:occurrenceStatus`, `dwc:lifeStage`, `dwc:sex` |
| Event | `dwc:eventID`, `dwc:parentEventID`, `dwc:eventDate`, `dwc:eventTime`, `dwc:samplingProtocol`, `dwc:samplingEffort` |
| Location | `dwc:locationID`, `dwc:decimalLatitude`, `dwc:decimalLongitude`, `dwc:geodeticDatum`, `dwc:coordinateUncertaintyInMeters`, `dwc:informationWithheld`, `dwc:dataGeneralizations` |
| Identification | `dwc:identificationID`, `dwc:identifiedBy`, `dwc:identifiedByID`, `dwc:dateIdentified`, `dwc:identificationVerificationStatus` |
| Taxon | `dwc:taxonID`, `dwc:scientificNameID`, `dwc:acceptedNameUsageID`, `dwc:scientificName`, `dwc:acceptedNameUsage`, `dwc:taxonRank`, `dwc:scientificNameAuthorship` |
| Measurement | `dwc:measurementID`, `dwc:measurementType`, `dwc:measurementValue`, `dwc:measurementUnit`, `dwc:measurementAccuracy`, `dwc:measurementMethod` |

Always inspect the current List of Terms for definitions, status, deprecation, replacements, and normative metadata.

### A.3 Package-choice reminder

```text
DwC terms / conceptual model
    ├── Simple Darwin Core
    ├── Darwin Core text / DwC-A
    ├── Darwin Core Data Package
    ├── XML
    ├── RDF
    └── bounded application profiles and projections
```

A vocabulary is not a package, and package validity is not KFM release authority.

[Back to top](#top)

---

<a id="appendix-b--conformance-checklist"></a>

## Appendix B — Review checklist

### B.1 Documentation/profile review

- [ ] The official standard and term-version IRIs are current and dated.
- [ ] Unratified public-review material is labeled as proposal, not baseline.
- [ ] The use case and Darwin Core classes are named.
- [ ] The selected representation and external consumer need are explicit.
- [ ] Every KFM alias is bound to a canonical term IRI or an explicit KFM extension.
- [ ] Source role and knowledge character cannot collapse into observed occurrence truth.
- [ ] Identity, null, absence, unknown, withheld, and corrected states are defined.
- [ ] Mapping loss and round-trip claims are bounded and testable.
- [ ] Rights, attribution, sensitivity, geoprivacy, and observer privacy remain independent gates.
- [ ] EvidenceRef/EvidenceBundle, review, release, correction, and rollback remain outside vocabulary validity.
- [ ] Sibling STAC-DwC documents are reconciled or explicitly held.
- [ ] No documentation status or badge is presented as implementation or conformance proof.

### B.2 Implementation graduation

- [ ] Mapping contract and mapping-registry schema are reviewed.
- [ ] Selected package/profile schemas are closed and versioned.
- [ ] Public-safe positive fixtures contain no real restricted data.
- [ ] Negative fixtures cover identity, relationships, rights, sensitivity, correction, and package failures.
- [ ] Parser/mapper/exporter is deterministic and records every transform.
- [ ] No hidden network access occurs in unit/fixture tests.
- [ ] Term and controlled-vocabulary versions are pinned.
- [ ] Validator outcomes and reason codes are finite and stable.
- [ ] Semantic-loss report is generated and bound to the artifact.
- [ ] Producer and intended consumer interoperate at an exact revision.
- [ ] Source admission and terms are current for every included record family.
- [ ] Evidence, policy, review, proof, release, correction, withdrawal, and rollback close.
- [ ] A later upstream version triggers review rather than silent reinterpretation.

---

> [!NOTE]
> **Current conclusion:** Darwin Core is a valid and current external interoperability standard for biodiversity information. KFM has a meaningful, executable source-bound Fauna occurrence slice, but no adopted Darwin Core profile or released Darwin Core package was established. The next legitimate step is profile-family convergence and a fixture-first mapping decision—not a claim of conformance.

**Last evidence review:** 2026-08-18 · **Prior blob:** `f897db3b14796ae895646ff32d410762b972119a` · **Rollback:** revert this same-path documentation change or restore that blob; no runtime or publication state is affected. · [Back to top](#top)
