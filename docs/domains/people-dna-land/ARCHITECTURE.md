<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/people-dna-land/architecture
title: People / Genealogy / DNA / Land Ownership — Domain Architecture
type: standard
version: v1
status: draft
owners: <docs steward — TODO via CODEOWNERS>, <people-dna-land domain steward — TODO>, <sensitivity reviewer — TODO>
created: 2026-05-18
updated: 2026-06-06
policy_label: restricted
related:
  # NEEDS VERIFICATION — repo paths PROPOSED until checked against a mounted repo
  - docs/domains/README.md
  - docs/domains/people-dna-land/README.md
  - docs/domains/people-dna-land/API_CONTRACTS.md
  - docs/domains/people-dna-land/sublanes/README.md
  - docs/adr/ADR-NNNN-sublanes-docs-convention.md
  - directory-rules.md
  - ai-build-operating-contract.md
  - docs/standards/PROV.md
tags: [kfm, domain, people, genealogy, dna, land, sensitive, assertion-first]
notes:
  # CONTRACT_VERSION = "3.0.0"
  # Living-person, DNA, raw-kit, exact-burial, and private person-parcel outputs are deny-by-default.
  # Assessor/tax records are NOT title truth; parcel geometry is NOT title boundary proof.
  # Promotion Gates A-G corrected to canonical Pass 10 C5-01 labels; letter sequence is conventional pending ADR-S-08.
  # Segment naming people-dna-land (DIRRULES §12) vs people (Atlas §24.13) is an open ADR (OQ-PEOPLE-DNA-11).
  # All repo paths PROPOSED until verified against a mounted repo and Directory Rules.
[/KFM_META_BLOCK_V2] -->

# People / Genealogy / DNA / Land Ownership — Domain Architecture

> Assertion-first, evidence-bound, privacy-aware governance for person, genealogy, DNA, and land-ownership claims across Kansas Frontier Matrix — with default denial for living-person and DNA-derived outputs.

![Status: draft](https://img.shields.io/badge/status-draft-orange)
![Doctrine: CONFIRMED](https://img.shields.io/badge/doctrine-CONFIRMED-2ea44f)
![Implementation: PROPOSED](https://img.shields.io/badge/implementation-PROPOSED-9c6ade)
![Sensitivity: high](https://img.shields.io/badge/sensitivity-HIGH-b91c1c)
![Policy: deny-by-default](https://img.shields.io/badge/policy-deny--by--default-1f2937)
![CONTRACT_VERSION 3.0.0](https://img.shields.io/badge/CONTRACT__VERSION-3.0.0-informational)
![Build](https://img.shields.io/badge/build-TODO-lightgrey)

**Status:** `draft` · **Owners:** `<docs steward + people-dna-land stewards — TODO>` · **Last updated:** `2026-06-06` · **`CONTRACT_VERSION = "3.0.0"`**

> [!IMPORTANT]
> This domain owns some of KFM’s most consequential restrictions. Living-person fields, DNA / genomic outputs, raw kit or vendor identifiers, exact burial coordinates, and person↔parcel joins are **deny-by-default**. Assessor or tax records are not equivalent to title; parcel geometry is not title-boundary proof. When in doubt: quarantine, generalize, delay, or deny — never silently publish.

-----

## Contents

- [1. Mission and boundary](#1-mission-and-boundary)
- [2. Scope and explicit non-ownership](#2-scope-and-explicit-non-ownership)
- [3. Ubiquitous language](#3-ubiquitous-language)
- [4. Bounded-context diagram](#4-bounded-context-diagram)
- [5. Canonical object families](#5-canonical-object-families)
- [6. Source families and source roles](#6-source-families-and-source-roles)
- [7. Spatial and temporal model](#7-spatial-and-temporal-model)
- [8. Pipeline shape: RAW → PUBLISHED](#8-pipeline-shape-raw--published)
- [9. Sensitivity, rights, and publication posture](#9-sensitivity-rights-and-publication-posture)
- [10. Cross-lane relations](#10-cross-lane-relations)
- [11. API, contract, and schema surfaces](#11-api-contract-and-schema-surfaces)
- [12. Governed AI behavior for this domain](#12-governed-ai-behavior-for-this-domain)
- [13. Validators, tests, and fixtures](#13-validators-tests-and-fixtures)
- [14. Publication, correction, and rollback](#14-publication-correction-and-rollback)
- [15. Directory Rules placement](#15-directory-rules-placement)
- [16. Open questions and verification backlog](#16-open-questions-and-verification-backlog)
- [17. Related docs](#17-related-docs)

-----

## 1. Mission and boundary

**`CONFIRMED` doctrine / `PROPOSED` implementation.** This domain represents people, genealogy, DNA evidence, and land ownership as **assertion-first, evidence-bound, privacy-aware claims** with strong default denial for living-person and DNA / genomic data. It owns person assertions, identity resolution, genealogy relations, family groups, life and residence events, migrations, land-ownership assertions, deed and title instruments, assessor and tax records, parcels, temporal ownership, and DNA match evidence.

It **must not** infer living-person or DNA relationships publicly without policy approval, and it **must not** equate assessor records or parcel geometry with title truth.

Doctrinal anchors: KFM Encyclopedia §7.14, Culmination Atlas Ch. 16, Unified Manual §10.14 (`[DOM-PEOPLE]`, `[ENCY]`, `[UNIFIED]`).

> [!NOTE]
> The lane is described in the corpus as one of the strongest illustrations of “evidence is insufficient for publication by itself.” A relationship hypothesis, DNA match, lineage inference, person assertion, or land-ownership statement can affect privacy, family identity, living persons, legal interests, and cultural sensitivity. This domain is deliberately governance-heavy.

[⬆ back to top](#contents)

-----

## 2. Scope and explicit non-ownership

### 2.1 What this domain owns

`CONFIRMED` doctrine / `PROPOSED` implementation. The owned object families are:

`Person Assertion`, `PersonCanonical`, `Person Identity Candidate`, `NameAssertion`, `Genealogy Relationship`, `RelationshipAssertion`, `FamilyGroup`, `LifeEvent`, `Residence Event`, `Migration Event`, `Land Ownership Assertion`, `Deed Instrument`, `Title Instrument`, `Assessor Record`, `TaxRecord`, `Parcel Version`, `Ownership Interval`, `DNA Match Evidence`, `DNASegment`, `DNAKitToken`, `ConsentGrant`, `RevocationReceipt`, `Relationship Hypothesis`. `[DOM-PEOPLE]` `[ENCY]`

> [!NOTE]
> `ReviewRecord` is a **cross-cutting governance receipt** (Atlas §24.2 receipt catalog — steward/rights-holder/policy review of admission, redaction, promotion, release), not an object owned by this domain. This domain *triggers and references* it at its gates; it does not define it.

### 2.2 What this domain explicitly does **not** own

|Adjacent lane                                                    |Why it is **not** owned here                                                                                                                                                                                   |
|-----------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|**Settlements / Infrastructure**                                 |Owns legal-municipality, census-place, infrastructure-asset, service-area, and condition semantics.                                                                                                            |
|**Roads / Rail / Trade**                                         |Owns route, corridor, network-graph, and historic-route semantics.                                                                                                                                             |
|**Archaeology / Cultural Heritage**                              |Owns site, survey, oral-history, exact-location-denial, and steward-review semantics.                                                                                                                          |
|**Hydrology · Soil · Agriculture · Hazards · Spatial Foundation**|Provide context only; **must not** weaken living-person, DNA, title, or parcel-boundary controls.                                                                                                              |
|**Frontier Matrix**                                              |Owns county-year analytical panels **plus `Land Office Record` and `Public Land Record`**; this domain feeds residence/population observations as inputs only and does not own land-office/public-land records.|

`CONFIRMED` doctrine: Settlements, roads, archaeology, hydrology, agriculture, hazards, and spatial foundation provide context but do not weaken living-person, DNA, title, or parcel-boundary controls. The Frontier↔People/Land edge carries public-land and land-office context **without living/DNA/title leakage**. `[DOM-PEOPLE]` `[ENCY]` `[Atlas §17.F]`

[⬆ back to top](#contents)

-----

## 3. Ubiquitous language

`CONFIRMED` terms / `PROPOSED` field realization. These terms are used inside this bounded context with meaning constrained by source role, evidence, time, and release state. Preserve casing and compound forms exactly. `[DOM-PEOPLE]` `[ENCY]` `[DDD]`

|Term                                                           |Meaning inside this bounded context                                                                                                                    |
|---------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
|**Person Assertion**                                           |A claim that a person existed with given attributes at a given time, evidence-bound and source-role-tagged. Never a canonical person record on its own.|
|**PersonCanonical**                                            |A reconciled person identity resolved from multiple `Person Assertion`s and accepted via review. Internal-only by default for living persons.          |
|**NameAssertion**                                              |A claim of a name, alias, or variant for a person within a specific source and time.                                                                   |
|**Person Identity Candidate**                                  |A pre-reconciliation grouping suggesting multiple assertions may refer to the same person. Not a confirmation.                                         |
|**LifeEvent**                                                  |Birth, death, baptism, marriage, divorce, naturalization, or comparable life event, asserted with evidence.                                            |
|**Residence Event**                                            |A residency claim at a place over a time interval, evidence-bound.                                                                                     |
|**Migration Event**                                            |A movement between residences/places with temporal scope and uncertainty.                                                                              |
|**Genealogy Relationship** / **RelationshipAssertion**         |An evidence-bound assertion of relationship (parent, child, spouse, sibling, etc.); remains a hypothesis until reviewed.                               |
|**FamilyGroup**                                                |A reviewed grouping of `RelationshipAssertion`s under a stewarded canonical view.                                                                      |
|**Relationship Hypothesis**                                    |A proposed but not-yet-reviewed relationship, often DNA-derived; remains restricted by default.                                                        |
|**DNA Match Evidence**                                         |DNA match record from a vendor or registry. Restricted by default; raw kit/vendor IDs are not public.                                                  |
|**DNASegment**                                                 |A specific DNA segment record; never public.                                                                                                           |
|**DNAKitToken**                                                |An opaque, internal-only handle for a DNA kit. Raw kit/vendor identifiers must not be logged or exposed.                                               |
|**ConsentGrant**                                               |Holder-controlled consent (issuer, subject pseudonym, purposes, scope, retention, revocation pointer). Releasable only when explicitly scoped.         |
|**RevocationReceipt**                                          |Tamper-evident record that a previously granted consent has been revoked; enforced at dereference time.                                                |
|**Land Ownership Assertion**                                   |A claim that a person, entity, or assertion held an interest in a parcel over a time interval. Distinct from title truth.                              |
|**Deed Instrument** / **Title Instrument** / **LandInstrument**|A recorded legal instrument (patent, deed, mortgage, lien, easement, lease, mineral, water, access, probate) bound to source role and rights.          |
|**Assessor Record** / **TaxRecord**                            |Property roll record from an assessor or tax authority. **Not title truth.**                                                                           |
|**Parcel Version**                                             |A versioned parcel-geometry snapshot. **Not a title-boundary proof** on its own.                                                                       |
|**Ownership Interval**                                         |A temporally bounded ownership claim derived from `LandInstrument`s, with `valid_time` and `source_time`.                                              |
|**LegalDescription**                                           |A metes-and-bounds or PLSS textual description; carries its own provenance and uncertainty.                                                            |
|**LandParcel**                                                 |The current bounded-context use of a parcel reference; meaning constrained by source role, evidence, time, and release state.                          |


> [!TIP]
> External standards (GEDCOM, schema.org `Person`, W3C PROV, FAIR/CARE) are **crosswalk targets**, not authority. They never overwrite KFM terminology — `Person Assertion` is not a GEDCOM `INDI`, and a `Land Ownership Assertion` is not a county-recorder DTO.

[⬆ back to top](#contents)

-----

## 4. Bounded-context diagram

`PROPOSED` rendering. The diagram reflects doctrine boundaries; route names, package names, and store identifiers are illustrative until a mounted-repo scan confirms them.

```mermaid
flowchart LR
  subgraph SRC["Source families — raw, rights-tagged"]
    VITAL["Vital · cemetery · obituary<br/>church · school · military<br/>census · directory · court · probate"]
    GED["GEDCOM / GEDZip /<br/>tree overlays"]
    DNA_SRC["DNA vendor match CSV ·<br/>segment · triangulation"]
    INSTR["Patent · deed · mortgage · lien<br/>easement · lease · mineral · water"]
    ASSESS["Assessor · tax-roll records"]
    PLSS["Plat · survey · metes/bounds<br/>PLSS · subdivision · derived geom."]
  end

  subgraph LIFECYCLE["KFM lifecycle — governed promotion"]
    RAW["RAW<br/>SourceDescriptor"]
    WORK["WORK / QUARANTINE<br/>Normalize · ConsentGrant<br/>RedactionReceipt"]
    PROC["PROCESSED<br/>EvidenceRef · ValidationReport<br/>Person/Land assertions"]
    CAT["CATALOG / TRIPLET<br/>EvidenceBundle · graph projection"]
    PUB["PUBLISHED<br/>ReleaseManifest · RollbackCard"]
  end

  subgraph MEMBRANE["Trust membrane — governed APIs only"]
    API["apps/governed-api/<br/>PROPOSED"]
    DRAWER["Evidence Drawer payload"]
    FOCUS["Focus Mode answer<br/>ANSWER · ABSTAIN · DENY · ERROR"]
  end

  subgraph SENSITIVE["Sensitive lanes — deny-by-default"]
    LIVING["Living-person fields"]
    DNAOUT["DNA-derived outputs"]
    BURIAL["Exact burial coordinates"]
    PJOIN["Person to parcel joins (private)"]
  end

  SRC --> RAW --> WORK --> PROC --> CAT --> PUB
  PUB --> API
  API --> DRAWER
  API --> FOCUS

  WORK -.fail-closed.-> LIVING
  WORK -.fail-closed.-> DNAOUT
  WORK -.fail-closed.-> BURIAL
  WORK -.fail-closed.-> PJOIN

  classDef sensitive fill:#fef2f2,stroke:#b91c1c,color:#7f1d1d;
  class SENSITIVE,LIVING,DNAOUT,BURIAL,PJOIN sensitive
  classDef membrane fill:#eef2ff,stroke:#4338ca,color:#312e81;
  class MEMBRANE,API,DRAWER,FOCUS membrane
```

> [!NOTE]
> `NEEDS VERIFICATION`: actual route names (`apps/governed-api/...`), package boundaries, and per-feature drawer payload shapes are `PROPOSED` until repo inspection. The diagram captures the **doctrinal** flow.

[⬆ back to top](#contents)

-----

## 5. Canonical object families

`CONFIRMED` term / `PROPOSED` implementation. Identity rules are deterministic: `source_id` + `object_role` + `temporal_scope` + normalized digest. Temporal handling keeps `source_time`, `observed_time`, `valid_time`, `retrieval_time`, `release_time`, and `correction_time` distinct where material. `[DOM-PEOPLE]` `[ENCY]`

|Object family                         |Purpose                                      |Identity rule                                                                               |Temporal handling                        |
|--------------------------------------|---------------------------------------------|--------------------------------------------------------------------------------------------|-----------------------------------------|
|`Person Assertion`                    |Source-bound claim of a person               |`PROPOSED` deterministic basis: source id + object role + temporal scope + normalized digest|`CONFIRMED` six-time discipline preserved|
|`PersonCanonical`                     |Reviewed canonical person record             |same                                                                                        |same                                     |
|`NameAssertion`                       |Source-bound name / alias claim              |same                                                                                        |same                                     |
|`LifeEvent`                           |Birth / death / marriage / etc. with evidence|same                                                                                        |same                                     |
|`Residence Event`                     |Residency over an interval                   |same                                                                                        |same                                     |
|`Migration Event`                     |Movement between residences                  |same                                                                                        |same                                     |
|`Genealogy Relationship`              |Evidence-bound relationship assertion        |same                                                                                        |same                                     |
|`FamilyGroup`                         |Reviewed relationship aggregation            |same                                                                                        |same                                     |
|`Land Ownership Assertion`            |Temporal ownership claim                     |same                                                                                        |same                                     |
|`Deed Instrument` / `Title Instrument`|Recorded legal instrument                    |same                                                                                        |same                                     |
|`Assessor Record` / `TaxRecord`       |Roll record (not title truth)                |same                                                                                        |same                                     |
|`Parcel Version`                      |Parcel geometry snapshot                     |same                                                                                        |same                                     |
|`Ownership Interval`                  |Time-bounded ownership derivation            |same                                                                                        |same                                     |
|`DNA Match Evidence`                  |Vendor / registry match record               |same                                                                                        |same                                     |
|`DNASegment`                          |DNA segment data (never public)              |same                                                                                        |same                                     |
|`Relationship Hypothesis`             |Pre-review relationship proposal             |same                                                                                        |same                                     |


> [!CAUTION]
> `Assessor Record` and `TaxRecord` are **never** to be rendered as title truth. `Parcel Version` is **never** to be rendered as title boundary proof. Any UI badge, API field, or Focus Mode summary that conflates these is a doctrine violation (source-role / geometry-role collapse, Atlas §24.1).

[⬆ back to top](#contents)

-----

## 6. Source families and source roles

`CONFIRMED` / `PROPOSED`. Source roles use the canonical seven-role vocabulary (`observed`, `regulatory`, `modeled`, `aggregate`, `administrative`, `candidate`, `synthetic`) from the Atlas §24.1 anti-collapse register. Source rights and current terms are `NEEDS VERIFICATION` per source; sensitive joins **fail closed**. `[DOM-PEOPLE]` `[ENCY]` `[Atlas §24.1]`

|Source family                                                                                           |Typical role(s)                                     |Rights / sensitivity                                                    |Cadence                           |
|--------------------------------------------------------------------------------------------------------|----------------------------------------------------|------------------------------------------------------------------------|----------------------------------|
|Vital · cemetery · burial · obituary · church · school · military · census · directory · court · probate|`authority` / `observed` / `context` per source role|Rights + current terms `NEEDS VERIFICATION`; sensitive joins fail closed|Source-vintage or cadence specific|
|GEDCOM / GEDZip / tree overlays                                                                         |`modeled` / `candidate` (treated as hypothesis)     |Living-person fields + raw identifiers restricted                       |Per upload                        |
|DNA vendor match CSV / segment / triangulation data                                                     |`observed` (restricted-by-default)                  |Raw kit / vendor IDs not public; consent required                       |Per upload                        |
|Patent / deed / mortgage / lien / easement / lease / mineral / water / access / probate instruments     |`authority` / `observed`                            |Per recorder; some restrictions apply                                   |Source-cadence specific           |
|Assessor and tax-roll records                                                                           |`administrative` (**not** title)                    |Per assessor terms                                                      |Annual / per cadence              |
|Plat / survey / metes-bounds / PLSS / subdivision / derived geometry                                    |`authority` / `observed` / `modeled` (derived)      |Per source; geometry-as-truth carefully bounded                         |Source-cadence specific           |


> [!IMPORTANT]
> Treat GEDCOM as **RAW only.** Never directly publish, directly map, or directly expose GEDCOM identifiers. Promotion path: `GEDCOM → RAW → evidence extraction → governed claims → EvidenceBundle → policy review → OverlayPointer → published runtime envelope.` Citing an assessor/tax record (role `administrative`) as ownership is a source-role collapse and is denied.

[⬆ back to top](#contents)

-----

## 7. Spatial and temporal model

`CONFIRMED` doctrine / `PROPOSED` implementation:

- **Spatial.** Residences, parcels, and land claims have spatial scope but **must not** be equated with title truth. Parcel geometry is a versioned representation, not a legal boundary. Burial-site exact coordinates are restricted; public exposure requires generalization or denial.
- **Temporal.** Every assertion keeps `source_time`, `observed_time`, `valid_time`, `retrieval_time`, `release_time`, and `correction_time` distinct where material. `Ownership Interval`s use bitemporal modeling (valid + source) so chain-of-title reconstructions are correctable.
- **Uncertainty.** Genealogy relations and DNA-derived inferences are first-class **hypotheses** with confidence bounds; they are not promoted to canonical relationships without review.

`[DOM-PEOPLE]` `[ENCY]`

[⬆ back to top](#contents)

-----

## 8. Pipeline shape: RAW → PUBLISHED

`CONFIRMED` lifecycle doctrine / `PROPOSED` lane application. People / DNA / Land follows the canonical KFM invariant, with promotion as a **governed state transition** — not a file move. `[DIRRULES]` `[DOM-PEOPLE]` `[ENCY]`

|Stage                |Handling                                                                                                                                       |Gate                                                                                          |Status    |
|---------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|----------|
|**RAW**              |Capture immutable source payload (or reference) with source role, rights, sensitivity, citation, time, and hash.                               |`SourceDescriptor` exists.                                                                    |`PROPOSED`|
|**WORK / QUARANTINE**|Normalize schema, geometry, time, identity, evidence, rights, and policy. Hold failures. Issue `ConsentGrant` / `RedactionReceipt` as required.|Validation + policy gate passes, or `quarantine_reason` is recorded.                          |`PROPOSED`|
|**PROCESSED**        |Emit validated normalized objects, transform receipts, and public-safe candidates.                                                             |`EvidenceRef` resolves; `ValidationReport` passes; digest closure exists.                     |`PROPOSED`|
|**CATALOG / TRIPLET**|Emit catalog records, `EvidenceBundle`s, graph / triplet projections, and release candidates.                                                  |Catalog + proof closure passes.                                                               |`PROPOSED`|
|**PUBLISHED**        |Serve released, public-safe artifacts through governed APIs and manifests.                                                                     |`ReleaseManifest` + rollback target + correction path + `ReviewRecord` (where required) exist.|`PROPOSED`|

<details>
<summary><strong>Promotion Gates A–G (canonical KFM matrix, applied to this lane)</strong></summary>

`CONFIRMED` doctrine: every released item flows through the KFM seven-gate matrix. The matrix below is the **canonical** labelling from Pass 10 C5-01; the corpus notes the gates appear “in slightly different forms in different sections” and that a single canonical labelling and sequence is to be frozen by **ADR-S-08**. The **sequence is the doctrine; the letter labels are conventional.** `[Pass 10 C5-01; unified-doctrine §8]`

|Gate |Intent (CONFIRMED — C5-01)  |Machine check                                                    |Required evidence                                                                               |
|-----|----------------------------|-----------------------------------------------------------------|------------------------------------------------------------------------------------------------|
|**A**|Structure & metadata        |MetaBlock presence / zone correctness (`check_structure`)        |KFM Meta Block valid                                                                            |
|**B**|Schemas & contracts         |JSON Schema + OpenAPI validation                                 |`ValidationReport` pass                                                                         |
|**C**|Policy parity (CI = runtime)|Conftest / OPA decisions, same pinned bundle in CI and at runtime|`PolicyDecision` = allow; no deny                                                               |
|**D**|Security & sensitivity      |sensitivity + license scans                                      |`RedactionReceipt` where applicable; **no PII / sensitivity leak**                              |
|**E**|Data quality                |DQ profilers / assertions with thresholds                        |DQ checks pass                                                                                  |
|**F**|Provenance & lineage        |receipt + OpenLineage validation                                 |`EvidenceRef`/receipt closure; lineage to receipts                                              |
|**G**|Reviewability (two-key)     |CODEOWNERS-enforced human + policy approval                      |`ReviewRecord` with steward identity; prior-state reference; rollback target (KFM-P22-PROG-0040)|

Auto-merge / promotion fires only when **all seven** pass; any failure blocks until remediation (default-deny, C5-02). For this domain, **Gate D** carries the heaviest load: no living-person field leak, no raw GEDCOM identifier leak, no DNA segment exposure, no exact burial coordinates, no private person↔parcel join in any published payload.

> [!WARNING]
> An earlier draft of this doc labelled the gates A=STAC/Evidence, B=Policy, C=Signing,
> D=Attestation, E=Steward, F=Smoke, G=Publish-ledger. That sequence does **not** match the
> canonical C5-01 matrix and has been corrected above. Signing/attestation (cosign/DSSE) and
> the publish ledger are real promotion requirements (C5-02, C1-03, C5-08) but they are
> *evidence within* gates C/D/F/G, not the gate labels themselves. Until ADR-S-08 freezes the
> labelling, treat the **C5-01 intents** as canonical and the letters as conventional.

</details>

[⬆ back to top](#contents)

-----

## 9. Sensitivity, rights, and publication posture

`CONFIRMED` / `PROPOSED`: Living-person output and DNA-derived outputs are denied or restricted by default; raw kit / vendor IDs and DNA segments are not public; assessor / tax records and parcel geometry are not title truth. `[DOM-PEOPLE]` `[ENCY]`

`CONFIRMED` doctrine: Unclear rights, unresolved source role, missing evidence, unresolved sensitivity, or absent release state **blocks** public promotion. `[ENCY]` `[DIRRULES]`

### 9.1 MUST-DENY conditions

> [!CAUTION]
> The following conditions **must deny** publication. Fail-closed defaults apply.

|Condition                                           |Result  |
|----------------------------------------------------|--------|
|Missing `ConsentGrant` / consent receipt            |**DENY**|
|Missing retention bound                             |**DENY**|
|Unknown subject scope                               |**DENY**|
|Living-person field without explicit, scoped consent|**DENY**|
|DNA / genomic payload in public path                |**DENY**|
|Exact burial coordinates in public export           |**DENY**|
|Raw GEDCOM identifiers in overlay or tile           |**DENY**|
|Unresolved `EvidenceRef`                            |**DENY**|
|Publication before promotion                        |**DENY**|
|Revoked consent (`RevocationReceipt` present)       |**DENY**|
|Missing `spec_hash`                                 |**DENY**|
|Invalid DSSE signature                              |**DENY**|
|Person ↔ parcel join exposing private linkage       |**DENY**|
|`Assessor Record` / `TaxRecord` rendered as title   |**DENY**|
|`Parcel Version` rendered as title-boundary proof   |**DENY**|

### 9.2 Sensitivity tier defaults

`PROPOSED` tier mapping (subject to ADR-S-05 sensitivity tier scheme; tier transitions follow Atlas §24.5.3):

|Object family                          |Default tier       |Notes                                                                                         |
|---------------------------------------|-------------------|----------------------------------------------------------------------------------------------|
|`Person Assertion` (living)            |**T4** (restricted)|Requires consent + review for any public exposure; T4→T1 via AggregationReceipt + ReviewRecord|
|`Person Assertion` (deceased, historic)|T1 / T2            |Tier rises with proximity, fame, or sensitive context                                         |
|`DNA Match Evidence`, `DNASegment`     |**T4**             |Never public; raw segment data has no public-tier transform                                   |
|`Relationship Hypothesis`              |**T3**             |Promotes only via review                                                                      |
|`Land Ownership Assertion` (historic)  |T1 / T2            |With evidence and rights                                                                      |
|`Assessor Record`, `TaxRecord`         |T2                 |Never title truth                                                                             |
|Exact burial coordinates               |**T4**             |Generalize before any public surface                                                          |
|Private person↔parcel join             |**T4**             |Generalized parcel + de-identified person → T2 only                                           |


> [!NOTE]
> `NEEDS VERIFICATION`: the canonical sensitivity tier scheme (T0–T4) is doctrine-significant and gated by ADR-S-05. Tier defaults above are best-fit mappings pending adoption. The Pass 10 C6-01 rubric (0–5) is a second scale in the corpus; its reconciliation with T0–T4 is itself open (ADR-S-05).

[⬆ back to top](#contents)

-----

## 10. Cross-lane relations

`CONFIRMED` / `PROPOSED`: every relation **must** preserve ownership, source role, sensitivity, and `EvidenceBundle` support. Cross-lane joins that bypass these are denied by default. `[DOM-PEOPLE]` `[ENCY]` `[Atlas §16.F]`

|This domain        |Related lane                       |Relation type                                                       |Constraint                                                                                                         |
|-------------------|-----------------------------------|--------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------|
|People / DNA / Land|**Settlements / Infrastructure**   |Residence, cemetery, school, court, county, township, place relation|Living-person fields **fail closed** at the join                                                                   |
|People / DNA / Land|**Roads / Rail / Trade**           |Migration, access, movement                                         |Sensitive route handling preserved                                                                                 |
|People / DNA / Land|**Archaeology / Cultural Heritage**|Historic person, land, documentary, cultural-place context          |Steward-reviewed and rights-bounded                                                                                |
|People / DNA / Land|**Agriculture**                    |Farm, land use, producer-adjacent context (with privacy)            |Private person ↔ parcel joins **denied by default**                                                                |
|People / DNA / Land|**Frontier Matrix**                |Aggregated population observations feed matrix cells                |Aggregation receipts required; Frontier owns land-office/public-land records; edge forbids living/DNA/title leakage|


> [!NOTE]
> Where the Atlas v1.0 base text conflicts with a later supplement, the corpus convention is to record the conflict against the supplement and resolve by ADR — not to silently prefer one. (This is the §2.5 drift procedure; do not treat “v1.0 governs” as an automatic rule without a recorded decision.) `[DIRRULES §2.5]`

[⬆ back to top](#contents)

-----

## 11. API, contract, and schema surfaces

`PROPOSED` governed-API surface. Routes, payload field names, and store boundaries are `UNKNOWN` until repo inspection. All public access goes through `apps/governed-api/` per Directory Rules §7.1; canonical stores are never client-reachable. Finite outcomes use the canonical set. See the companion `API_CONTRACTS.md` for the full surface contract. `[DIRRULES]` `[GAI]` `[Atlas §24.3]`

|Endpoint or artifact                       |DTO / schema                                                                                     |Finite outcomes                            |Status                                            |
|-------------------------------------------|-------------------------------------------------------------------------------------------------|-------------------------------------------|--------------------------------------------------|
|`People/DNA/Land` feature / detail resolver|`PeopleDNALandDecisionEnvelope`                                                                  |`ANSWER` / `ABSTAIN` / `DENY` / `ERROR`    |`PROPOSED` route; name `UNKNOWN`                  |
|`People/DNA/Land` layer manifest resolver  |`LayerManifest` / domain layer descriptor                                                        |`ANSWER` / `DENY` / `ERROR`                |`PROPOSED`; public-safe release only              |
|`People/DNA/Land` Evidence Drawer payload  |`EvidenceDrawerPayload` + `EvidenceBundle` projection                                            |`ANSWER` / `ABSTAIN` / `DENY` / `ERROR`    |`PROPOSED`; evidence + policy filtered            |
|`People/DNA/Land` Focus Mode answer        |`RuntimeResponseEnvelope` + `AIReceipt`                                                          |`ANSWER` / `ABSTAIN` / `DENY` / `ERROR`    |`PROPOSED`; AI is never root truth                |
|Consent receipt                            |`ConsentGrant` schema                                                                            |governed gate outcome                      |`PROPOSED`; holder-controlled VC compatible       |
|Overlay pointer (public-safe)              |`OverlayPointer` schema                                                                          |dereferenced server-side under policy      |`PROPOSED`; opaque, short-lived                   |
|Schema responsibility root                 |`schemas/contracts/v1/domains/people-dna-land/` *(or `…/people/` per Atlas §24.13 — see §16 Q-9)*|finite validator outcomes (`PASS` / `FAIL`)|`PROPOSED`; verify with Directory Rules + ADR-0001|

### 11.1 Public runtime envelope shape (illustrative)

`PROPOSED` envelope; field names are illustrative until contract verification.

```json
{
  "outcome": "ANSWER",
  "overlay_pointer": "overlay://9f2a...",
  "policy_label": "public",
  "retention": "P90D",
  "no_reidentification": true,
  "evidence_bundle_refs": ["kfm://evidence/..."],
  "release_state": "PUBLISHED",
  "rollback_target": "kfm://release/.../rollback"
}
```

The envelope **never** carries: names, raw lineage IDs, exact coordinates, raw GEDCOM payloads, DNA segments, kit/vendor identifiers, or family identifiers.

> [!IMPORTANT]
> Deny is a **first-class outcome**, not an error condition. `NARROWED` and `BOUNDED` answers are also legitimate (`RuntimeResponseEnvelope` extensions, operating contract §8). The trust membrane prefers a labeled refusal over a fluent guess.

[⬆ back to top](#contents)

-----

## 12. Governed AI behavior for this domain

`CONFIRMED` doctrine / `PROPOSED` implementation. `[GAI]` `[DOM-PEOPLE]` `[ENCY]`

|AI surface behavior                            |Allowed|Forbidden                    |
|-----------------------------------------------|-------|-----------------------------|
|Summarize released `EvidenceBundle`s           |yes    |—                            |
|Compare evidence across released claims        |yes    |—                            |
|Explain limitations and source-role posture    |yes    |—                            |
|Draft steward-review notes                     |yes    |—                            |
|Generate living-person identity inferences     |—      |DENY                         |
|Generate DNA-derived relationship inferences   |—      |DENY                         |
|Cite uncited / unresolved claims               |—      |DENY                         |
|Synthesize chain-of-title in a definitive voice|—      |DENY — use hypothesis framing|
|Render exact burial coordinates                |—      |DENY                         |

When evidence is insufficient, the AI must **ABSTAIN** with a reason; when policy / rights / sensitivity / release state blocks, the AI must **DENY** with a reason code. Every Focus Mode answer carries an `AIReceipt`, and an answer without a passing `CitationValidationReport` is coerced to `ABSTAIN`.

[⬆ back to top](#contents)

-----

## 13. Validators, tests, and fixtures

`PROPOSED` validator set. Each becomes a fixture-backed test with deterministic inputs. Validator/fixture homes use the **whole-domain** `people-dna-land` segment per §12 (not subdivided by sublane). `[DOM-PEOPLE]` `[ENCY]`

|Validator                                    |Purpose                                                                                                                                                                                                                                                                                                                                                                                |
|---------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|Person assertion evidence test               |Every `Person Assertion` resolves to an `EvidenceRef`                                                                                                                                                                                                                                                                                                                                  |
|GEDCOM import rights / living-flag test      |Imports cannot publish living-person fields without consent                                                                                                                                                                                                                                                                                                                            |
|DNA consent and raw-ID no-log test           |Raw kit / vendor IDs never appear in logs or exports                                                                                                                                                                                                                                                                                                                                   |
|Revocation cleanup test                      |`RevocationReceipt` invalidates downstream renders + caches                                                                                                                                                                                                                                                                                                                            |
|Legal-description and chain-of-title gap test|Gaps in instrument chains are surfaced, not papered over                                                                                                                                                                                                                                                                                                                               |
|Assessor-as-title denial test                |`Assessor Record` cannot satisfy a title query                                                                                                                                                                                                                                                                                                                                         |
|Parcel-as-boundary denial test               |`Parcel Version` cannot satisfy a title-boundary query                                                                                                                                                                                                                                                                                                                                 |
|Graph projection safety test                 |Sensitive edges (living, DNA, private person↔parcel) are absent from public graph                                                                                                                                                                                                                                                                                                      |
|Reidentification-risk screen                 |`PROPOSED`/`INFERRED`: a pre-publication screen over uniqueness, spatial precision, temporal precision, relationship density, and small-community exposure, emitting `ANSWER` / `GENERALIZE` / `DELAY` / `DENY`. **Not found as a named corpus object** — derived from the k-anonymity / geoprivacy doctrine (Pass 10 C6-06); needs an ADR or schema before it is treated as canonical.|

<details>
<summary><strong>Recommended negative-path fixtures</strong> (PROPOSED, illustrative)</summary>

|Fixture                        |Expected outcome|
|-------------------------------|----------------|
|`expired_receipt.json`         |FAIL            |
|`revoked_receipt.json`         |FAIL            |
|`living_person_export.json`    |FAIL            |
|`missing_retention.json`       |FAIL            |
|`raw_gedcom_overlay.json`      |FAIL            |
|`unresolved_evidence_ref.json` |FAIL            |
|`exact_burial_coordinates.json`|FAIL            |
|`invalid_signature.json`       |FAIL            |
|`assessor_as_title.json`       |FAIL            |
|`parcel_as_boundary.json`      |FAIL            |
|`valid_public_overlay.json`    |PASS            |

</details>

[⬆ back to top](#contents)

-----

## 14. Publication, correction, and rollback

`CONFIRMED` doctrine / `PROPOSED` implementation. People / DNA / Land publication requires `ReleaseManifest`, `EvidenceBundle`, validation / policy support, review state where required, a correction path, a stale-state rule, and a rollback target. `[ENCY Appendix E]` `[DOM-PEOPLE]`

### 14.1 Three-layer separation (architectural invariant)

> [!IMPORTANT]
> Keep these three layers explicitly separate. Collapsing them is how genealogy systems drift into unsourced folklore.

1. **Canonical human assertions** — internal only. Examples: person existed, relationship claim, event claim, location claim. **Never public by default.**
1. **Evidence layer** — `EvidenceBundle`-backed. Examples: census image, church record, obituary, gravestone image, archive citation. **Immutable lineage.**
1. **Publication / experience layer** — derived and policy-filtered. Examples: map overlays, timelines, story exports, graph views, scene annotations, public tile layers. **Always downstream carriers — never sovereign truth.**

### 14.2 Correction and rollback

- A `CorrectionNotice` enumerates what changed, why, and which derivatives are invalidated.
- A `RollbackCard` records the rollback target and reason; previous release state is preserved while current release is repointed.
- Per Atlas §24.5.3: any tier **downgrade** (toward less public) may proceed on `CorrectionNotice` + `ReviewRecord`; tier **upgrades** require both a transform receipt and a `ReviewRecord`.
- Revocation invalidates caches, tiles, and overlays; render-time enforcement is required.

[⬆ back to top](#contents)

-----

## 15. Directory Rules placement

`PROPOSED` placement, per Directory Rules §3, §12 (Domain Placement Law). The domain appears as a **segment** inside each responsibility root, never as a root itself. `[DIRRULES]`

|Responsibility root|Path segment (PROPOSED)                                                                                                           |Purpose                                                                       |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
|`docs/`            |`docs/domains/people-dna-land/`                                                                                                   |Human-facing architecture, runbooks, ADRs (this file lives here)              |
|`contracts/`       |`contracts/domains/people-dna-land/`                                                                                              |Object **meaning** for this lane                                              |
|`schemas/`         |`schemas/contracts/v1/domains/people-dna-land/` *(per ADR-0001 schema-home; Atlas §24.13 uses `…/people/` — see Q-9)*             |Machine-checkable **shape**                                                   |
|`policy/`          |`policy/domains/people-dna-land/` *(Atlas §24.13 uses `policy/sensitivity/people/`, `policy/consent/people/` — see Q-9)*          |Allow / deny / restrict / abstain / review                                    |
|`tests/`           |`tests/domains/people-dna-land/`                                                                                                  |Enforceable proofs                                                            |
|`fixtures/`        |`fixtures/domains/people-dna-land/` (or `tests/fixtures/...`)                                                                     |Golden / valid / invalid samples                                              |
|`tools/`           |`tools/validators/people-dna-land/`, `tools/ingest/people-dna-land/`                                                              |Repo-wide validators / ingest helpers (whole-domain segment, not `genealogy/`)|
|`pipelines/`       |`pipelines/domains/people-dna-land/`                                                                                              |Executable pipeline logic                                                     |
|`data/`            |`data/raw/people-dna-land/<source_id>/<run_id>/` → `…/work` → `…/quarantine` → `…/processed` → `…/catalog/...` → `…/published/...`|Lifecycle artifacts                                                           |
|`release/`         |`release/candidates/people-dna-land/`                                                                                             |Release decisions, correction notices, rollback cards                         |
|`runtime/`         |`runtime/...` adapters (behind governed API)                                                                                      |Local adapter / harness                                                       |


> [!NOTE]
> All paths are `PROPOSED` and require verification against a mounted repo. The schema-home default (`schemas/contracts/v1/...`) follows ADR-0001; any deviation needs its own ADR. **Segment-naming conflict:** Directory Rules §12 uses `people-dna-land`; the Atlas §24.13 crosswalk uses a shorter `people/` segment for schemas/policy. Both are PROPOSED; do not create both as parallel homes (§2.4(5)). Tracked as Q-9 / OQ-PEOPLE-DNA-11. The `docs/domains/<domain>/sublanes/` documentation convention is governed by the separate `sublanes/` ADR (ADR-NNNN).

[⬆ back to top](#contents)

-----

## 16. Open questions and verification backlog

`NEEDS VERIFICATION` items. Each becomes a backlog row resolvable by mounted-repo inspection, ADR adoption, or steward decision. `[DOM-PEOPLE]` `[ENCY]`

|# |Item to verify                                                                           |Evidence that would settle it                                                                               |Status                           |
|-:|-----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------|---------------------------------|
|1 |Living-person policy scope (definition, edge cases, decedent transitions)                |Mounted policy files, schemas, registry entries, tests, emitted artifacts, review records, release manifests|`NEEDS VERIFICATION`             |
|2 |DNA consent / revocation enforcement at render time                                      |Same + revocation cleanup tests + cache invalidation hooks                                                  |`NEEDS VERIFICATION`             |
|3 |Land instrument chain logic (gaps, conflicts, supersession)                              |Mounted validators + chain-of-title fixtures                                                                |`NEEDS VERIFICATION`             |
|4 |Geometry-role boundary logic (`Parcel Version` vs. title)                                |Mounted contracts + parcel-as-boundary denial tests                                                         |`NEEDS VERIFICATION`             |
|5 |UI / API restricted-field no-leak behavior                                               |E2E tests + restricted-field fixtures                                                                       |`NEEDS VERIFICATION`             |
|6 |Exact route names for governed-API endpoints                                             |Mounted `apps/governed-api/` source                                                                         |`UNKNOWN`                        |
|7 |Sensitivity tier scheme adoption (T0–T4) and its reconciliation with the C6-01 0–5 rubric|ADR-S-05 outcome                                                                                            |`NEEDS VERIFICATION`             |
|8 |Reidentification-risk screen — is it a named, canonical object?                          |ADR or schema; currently INFERRED from C6-06 geoprivacy doctrine                                            |`OPEN / INFERRED`                |
|9 |Segment naming: `people-dna-land/` (DIRRULES §12) vs. `people/` (Atlas §24.13)           |ADR or repo convention scan                                                                                 |`CONFLICTED` (= OQ-PEOPLE-DNA-11)|
|10|Promotion Gate A–G canonical labelling and sequence                                      |ADR-S-08 outcome                                                                                            |`NEEDS VERIFICATION`             |
|11|`PROV.md` vs. `PROVENANCE.md` naming (cross-doc, OPEN-DR-01)                             |ADR resolution                                                                                              |`NEEDS VERIFICATION`             |
|12|`sublanes/` documentation convention                                                     |ADR-NNNN (drafted)                                                                                          |`PROPOSED`                       |

### Suggested ADR candidates (this domain)

- Consent Receipts / ConsentSidecar as first-class governance objects
- Overlay Pointer public-safe publication model
- Living-Person Restriction Defaults
- Revocation Status List strategy
- Derived Story Layers Are Non-Canonical
- Reidentification-risk screen (adopt or reject as a named object)

[⬆ back to top](#contents)

-----

## 17. Related docs

- [`docs/domains/README.md`](../README.md) — Domain index
- [`docs/domains/people-dna-land/README.md`](./README.md) — Domain landing *(PROPOSED)*
- [`docs/domains/people-dna-land/API_CONTRACTS.md`](./API_CONTRACTS.md) — governed-API surface contract
- [`docs/domains/people-dna-land/sublanes/README.md`](./sublanes/README.md) — sublanes index *(convention pending ADR-NNNN)*
- [`docs/adr/ADR-NNNN-sublanes-docs-convention.md`](../../adr/ADR-NNNN-sublanes-docs-convention.md) — `sublanes/` convention ADR
- [`directory-rules.md`](../../../directory-rules.md) — Path authority and responsibility roots (§3, §12, §2.4, §2.5)
- [`ai-build-operating-contract.md`](../../../ai-build-operating-contract.md) — operating law (`CONTRACT_VERSION = "3.0.0"`)
- [`docs/standards/PROV.md`](../../standards/PROV.md) — W3C PROV-O profile *(see open question #11)*
- `docs/adr/` — Accepted ADRs *(enumeration NEEDS VERIFICATION)*
- `contracts/domains/people-dna-land/` · `schemas/contracts/v1/domains/people-dna-land/` · `policy/domains/people-dna-land/` — object meaning / shape / policy *(PROPOSED)*
- Trust-membrane and lifecycle doctrine: exact filenames NEEDS VERIFICATION (corpus places these under `docs/doctrine/` in some trees)

-----

<sub>**Last updated:** 2026-06-06 · **Doc id:** `kfm://doc/people-dna-land/architecture` · **Version:** `v1` · **Status:** `draft` · `CONTRACT_VERSION = "3.0.0"` · [⬆ back to top](#contents)</sub>