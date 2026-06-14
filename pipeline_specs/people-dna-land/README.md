<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-people-dna-land-readme
title: People DNA Land Pipeline Specs README
type: readme
version: v0.1
status: draft
owners:
  - <pipeline-spec-steward>
  - <people-dna-land-domain-steward>
  - <privacy-steward>
  - <consent-steward>
  - <land-records-steward>
  - <pipeline-owner>
  - <evidence-steward>
  - <policy-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: restricted-doctrine
path: pipeline_specs/people-dna-land/README.md
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - pipeline_specs/README.md
  - pipeline_specs/people/README.md
  - pipelines/README.md
  - pipelines/domains/people-dna-land/README.md
  - pipelines/domains/people/README.md
  - docs/domains/people-dna-land/ARCHITECTURE.md
  - docs/domains/people-dna-land/SCOPE_AND_BOUNDARY.md
  - docs/domains/people-dna-land/SENSITIVITY.md
  - docs/domains/people-dna-land/PEOPLE_DOMAIN_MODEL.md
  - docs/domains/people-dna-land/sublanes/people.md
  - docs/domains/people-dna-land/sublanes/dna.md
  - docs/domains/people-dna-land/sublanes/land.md
  - data/registry/sources/people-dna-land/
  - data/receipts/pipeline/people-dna-land/
  - data/proofs/evidence_bundle/
  - tests/pipeline_specs/people-dna-land/
  - fixtures/pipeline_specs/people-dna-land/
tags: [kfm, pipeline-specs, people-dna-land, people, genealogy, dna, land-ownership, declarative-config, privacy, consent, revocation, assertion-first, title-boundary, receipts, governance]
notes:
  - "This README replaces the short pipeline_specs/people-dna-land stub with a governed declarative-spec lane contract."
  - "pipeline_specs/ is declarative configuration — the what. pipelines/ is executable logic — the how."
  - "People/DNA/Land specs configure pipeline intent, source scope, lifecycle gates, consent and privacy gates, assertion-first posture, title-boundary posture, evidence gates, receipts, and release blockers. They do not execute pipeline logic or store lifecycle outputs."
  - "Living-person data, DNA/genomic evidence, raw kit/vendor identifiers, exact burial coordinates, and private person-parcel joins are deny-by-default."
  - "Assessor/tax records are not title truth, and parcel geometry is not title-boundary proof."
  - "Segment naming remains CONFLICTED / NEEDS VERIFICATION where people and people-dna-land both appear; do not create parallel authority homes without ADR/path-map/migration/rollback notes."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# People / Genealogy / DNA / Land Pipeline Specs

> Declarative configuration lane for People / Genealogy / DNA / Land pipeline profiles, source scopes, schedules, lifecycle gates, consent and privacy controls, assertion-first boundaries, title-boundary rules, evidence requirements, fixtures, receipts, and release-readiness intent — separate from executable pipeline logic.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipeline__specs%2F-0a7ea4)
![authority](https://img.shields.io/badge/authority-declarative%20config-0a7ea4)
![implementation](https://img.shields.io/badge/implementation-pipelines%2Fdomains%2Fpeople--dna--land%2F-d62728)
![sensitivity](https://img.shields.io/badge/living%20person%20%2F%20DNA-deny%20by%20default-d62728)

**Status:** Draft  
**Path:** `pipeline_specs/people-dna-land/README.md`  
**Responsibility root:** `pipeline_specs/` — declarative pipeline configuration, the **what**  
**Companion implementation lane:** `pipelines/domains/people-dna-land/` — executable pipeline logic, the **how**  
**Alias note:** `pipeline_specs/people/` is an alias/conflict path and must not become a parallel authority lane.  
**Placement posture:** People / Genealogy / DNA / Land declarative specs belong here unless an ADR resolves segment naming differently.  
**Public posture:** no public release, data storage, privacy decision, consent decision, title decision, relationship truth decision, or executable side effect; specs only configure governed pipeline runs.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Sensitivity and consent boundary](#3-sensitivity-and-consent-boundary)
- [4. Spec anti-collapse rules](#4-spec-anti-collapse-rules)
- [5. What belongs here](#5-what-belongs-here)
- [6. What does not belong here](#6-what-does-not-belong-here)
- [7. Spec scope](#7-spec-scope)
- [8. Lifecycle posture](#8-lifecycle-posture)
- [9. Required gates](#9-required-gates)
- [10. Directory contract](#10-directory-contract)
- [11. Spec profile families](#11-spec-profile-families)
- [12. Inputs and outputs](#12-inputs-and-outputs)
- [13. Minimal spec profile shape](#13-minimal-spec-profile-shape)
- [14. Tests, fixtures, and validation](#14-tests-fixtures-and-validation)
- [15. Definition of done](#15-definition-of-done)
- [16. Open questions](#16-open-questions)

---

## 1. Purpose

`pipeline_specs/people-dna-land/` owns declarative People / Genealogy / DNA / Land pipeline configuration.

It may describe:

- which person, genealogy, DNA, consent, land-record, parcel, ownership, or public-derivative profile should run;
- which source descriptor ids are in scope;
- which assertion-first, privacy, consent, revocation, DNA-boundary, title-boundary, and release-readiness gates apply;
- which lifecycle gates are required;
- which fixtures support no-network tests without leaking restricted content;
- which receipts, reports, blockers, and review handoffs are expected;
- which downstream implementation lane is authorized to execute the spec.

It does **not** implement pipeline behavior. People / Genealogy / DNA / Land implementation belongs under `pipelines/domains/people-dna-land/` and related executable lanes.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipeline_specs/`? | This root owns declarative pipeline configuration, separate from implementation. | CONFIRMED root contract |
| Why `people-dna-land/`? | This is the visible bounded-context segment used by the governing People / Genealogy / DNA / Land docs. | CONFIRMED docs posture / NEEDS VERIFICATION for active specs |
| What about `people/`? | `people` is an alias/conflict path and must not create duplicate authority. | CONFLICTED / NEEDS ADR |
| Does this execute pipelines? | No. Execution belongs under `pipelines/`. | CONFIRMED separation |
| Does this define object meaning? | No. Object meaning belongs under contracts/domain doctrine. | CONFIRMED authority separation |
| Does this store data or receipts? | No. Lifecycle data and receipts belong under `data/`. | CONFIRMED lifecycle posture |
| Can this approve publication, consent, relationship truth, or title truth? | No. Specs can require gates only; review, policy, title, consent, and release decisions remain separate. | CONFIRMED boundary posture |

> [!IMPORTANT]
> A pipeline spec says what should run and under which constraints. It is not a run, not a receipt, not evidence, not processed data, not catalog truth, not consent authority, not legal title truth, not DNA relationship truth, and not release approval.

[⬆ Back to top](#top)

---

## 3. Sensitivity and consent boundary

People / Genealogy / DNA / Land specs inherit one of KFM's strictest deny-by-default boundaries:

- living-person fields are deny-by-default;
- DNA and genomic evidence are restricted by default;
- raw DNA kit ids, vendor identifiers, match lists, triangulation details, and segment details must not appear here;
- consent scope, purpose, retention, and revocation must be enforced where applicable;
- exact burial coordinates and culturally sensitive family/place context fail closed;
- private person-parcel joins must not publish without explicit release authority;
- assessor/tax records must not become title truth;
- parcel geometry must not become title-boundary proof;
- generated summaries cannot convert assertions or hypotheses into confirmed truth.

When a profile cannot prove consent, rights, living-person status, privacy posture, title-boundary posture, or release posture, the profile must fail closed or route to quarantine/review.

[⬆ Back to top](#top)

---

## 4. Spec anti-collapse rules

Disallowed collapses:

```text
spec file -> executable pipeline
spec profile -> release approval
source list -> source authority
Person Assertion -> public person truth
Person Identity Candidate -> canonical person
Relationship Hypothesis -> confirmed relationship
DNA Match Evidence -> public kinship claim
ConsentGrant reference -> unrestricted publication
RevocationReceipt ignored -> permitted publication
Assessor Record -> title truth
TaxRecord -> title truth
Parcel Version -> title-boundary proof
person-parcel context -> public ownership truth
generated summary -> evidence
```

Required separations:

- declarative specs stay in `pipeline_specs/`;
- executable logic stays in `pipelines/`;
- source descriptors stay in the source registry;
- lifecycle data stays in `data/`;
- receipts and proofs stay in their receipt/proof homes;
- contracts, schemas, and policy stay in their own roots;
- person assertion, identity candidate, canonical identity, relationship hypothesis, relationship assertion, DNA evidence, consent, revocation, land instrument, assessor record, tax record, parcel version, ownership interval, and title-boundary posture remain separately labeled;
- release decisions stay under `release/`.

[⬆ Back to top](#top)

---

## 5. What belongs here

Appropriate contents include declarative specs for:

- person assertion and name assertion profiles;
- person identity candidate profiles;
- life event, residence event, and migration event profiles;
- genealogy relationship, relationship assertion, relationship hypothesis, and family group profiles;
- DNA evidence profile gates, consent gates, revocation gates, and DNA-boundary checks;
- land ownership assertion, deed/title instrument, assessor/tax record, legal-description, parcel-version, and ownership-interval profile gates;
- public-safe derivative profiles;
- watcher, validation, catalog, triplet, publish-readiness, rollback-readiness, and dry-run profiles.

A good placement test:

> If the file answers “what People / Genealogy / DNA / Land profile should run, with what scope, consent, privacy, assertion, title-boundary, evidence, and release blockers?”, it may belong here. If it answers “how does the pipeline execute?”, it belongs under `pipelines/`.

[⬆ Back to top](#top)

---

## 6. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Executable People/DNA/Land pipeline code | `pipelines/domains/people-dna-land/` |
| Alias-only executable code | `pipelines/domains/people/` only when ADR-safe and bounded |
| Source connectors | `connectors/<source>` |
| Source descriptors | `data/registry/sources/people-dna-land/` or accepted registry home |
| Object meaning | `contracts/domains/people-dna-land/`, `contracts/people/`, and domain doctrine |
| JSON Schemas | `schemas/contracts/v1/domains/people-dna-land/`, `schemas/contracts/v1/people/`, or accepted schema home |
| Policy, consent, privacy, rights, or sensitivity decisions | `policy/domains/people-dna-land/`, `policy/consent/people-dna-land/`, `policy/sensitivity/people-dna-land/`, review roots |
| Tests | `tests/pipeline_specs/people-dna-land/` or accepted test home |
| Fixtures | `fixtures/pipeline_specs/people-dna-land/` or accepted fixture home |
| Lifecycle data | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/triplets`, `data/published` |
| EvidenceBundles | `data/proofs/evidence_bundle/` |
| Release decisions/manifests/corrections/rollback cards | `release/` |
| Public API/UI code | `apps/governed-api/`, `apps/explorer-web/`, packages |

[⬆ Back to top](#top)

---

## 7. Spec scope

People / Genealogy / DNA / Land specs may configure profiles for object families and candidate products such as:

- Person Assertion, PersonCanonical review inputs, Person Identity Candidate, and NameAssertion;
- LifeEvent, Residence Event, and Migration Event;
- Genealogy Relationship, RelationshipAssertion, Relationship Hypothesis, and FamilyGroup;
- DNA Match Evidence, DNAKitToken references, DNASegment handling boundaries, ConsentGrant, and RevocationReceipt gates;
- Land Ownership Assertion, Deed Instrument, Title Instrument, LandInstrument, Assessor Record, TaxRecord, LegalDescription, Parcel Version, and Ownership Interval;
- public-safe, release-reviewed derivatives that preserve privacy, consent, review, and rollback posture.

This lane may cite other domains for place, infrastructure, roads, archaeology, hydrology, soil, agriculture, hazards, and spatial context, but those cross-lane contexts must not weaken living-person, DNA, consent, title, or parcel-boundary controls.

[⬆ Back to top](#top)

---

## 8. Lifecycle posture

Specs may target lifecycle stages, but do not create lifecycle transitions themselves:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A spec may declare input lifecycle state, expected output lifecycle state, source descriptor refs, assertion boundaries, living-person checks, consent and revocation checks, DNA-boundary posture, title-boundary posture, EvidenceBundle requirements, receipt requirements, release blockers, rollback support, and correction support.

Only governed pipeline implementation and release authority can perform transitions.

[⬆ Back to top](#top)

---

## 9. Required gates

Every People / Genealogy / DNA / Land spec should declare or explicitly mark not applicable:

1. **Profile identity gate** — stable `spec_id`, owner, bounded context, lane, and version.
2. **Implementation gate** — target executable lane under `pipelines/`.
3. **Source gate** — source descriptor refs and source roles.
4. **Lifecycle gate** — allowed input and output lifecycle states.
5. **Assertion gate** — assertion, candidate, reviewed identity, hypothesis, and public derivative distinctions.
6. **Living-person gate** — deny-by-default unless release posture is explicitly permitted.
7. **Consent gate** — scope, purpose, retention, and revocation checks where applicable.
8. **DNA-boundary gate** — DNA evidence, relationship hypotheses, kit references, and segment data remain restricted.
9. **Land-boundary gate** — assessor/tax records and parcel geometry do not become title truth.
10. **Evidence gate** — EvidenceRef/EvidenceBundle requirements for claims.
11. **Receipt gate** — required run, transform, validation, consent, revocation, review, redaction, title-boundary, or release-readiness receipts.
12. **Release gate** — ReleaseManifest input requirements, rollback target, and correction path where output can publish.

[⬆ Back to top](#top)

---

## 10. Directory contract

Recommended shape:

```text
pipeline_specs/people-dna-land/
├── README.md
├── ingest.yaml                  # PROPOSED
├── normalize.yaml               # PROPOSED
├── validate.yaml                # PROPOSED
├── catalog.yaml                 # PROPOSED
├── triplets.yaml                # PROPOSED
├── publish.yaml                 # PROPOSED
├── rollback.yaml                # PROPOSED
├── watchers.yaml                # PROPOSED
├── people_assertions.yaml       # PROPOSED
├── genealogy_relationships.yaml # PROPOSED
├── dna_evidence.yaml            # PROPOSED
├── consent_revocation.yaml      # PROPOSED
├── land_instruments.yaml        # PROPOSED
├── assessor_tax_records.yaml    # PROPOSED
├── parcel_versions.yaml         # PROPOSED
└── public_derivatives.yaml      # PROPOSED
```

These filenames are proposed placeholders until actual spec files, schema validation, CI coverage, and ADR/path resolution are implemented.

[⬆ Back to top](#top)

---

## 11. Spec profile families

| Profile family | Purpose | Implementation lane |
|---|---|---|
| `ingest` | Declare source intake scope and prerequisites. | `pipelines/domains/people-dna-land/` or shared ingest lane |
| `normalize` | Declare transform profile, expected receipts, and blockers. | People/DNA/Land normalize implementation |
| `validate` | Declare privacy, consent, assertion, DNA, and land-boundary checks. | People/DNA/Land validate implementation |
| `catalog` | Declare catalog closure requirements. | People/DNA/Land catalog implementation |
| `triplets` | Declare graph/triplet projection profile without replacing review state. | People/DNA/Land triplet implementation |
| `publish` | Declare release-candidate readiness checks. | People/DNA/Land publish support |
| `rollback` | Declare rollback-readiness check profile. | People/DNA/Land rollback support |
| `watchers` | Declare source-change observation profiles. | People/DNA/Land watcher support |
| `people` | Declare person assertion, identity, name, event, residence, migration, and relationship profiles. | People sublane implementation |
| `dna` | Declare DNA evidence, consent, revocation, and hypothesis-boundary profiles. | DNA sublane implementation |
| `land` | Declare deed/title instrument, assessor/tax, parcel, ownership interval, and title-boundary profiles. | Land sublane implementation |

[⬆ Back to top](#top)

---

## 12. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Spec file | `pipeline_specs/people-dna-land/` | Declarative config only. |
| Alias spec | `pipeline_specs/people/` | Compatibility only; no parallel authority. |
| Executable target | `pipelines/domains/people-dna-land/` or accepted sublane | The spec references it; it does not implement it. |
| Source descriptor | `data/registry/sources/people-dna-land/` | Stable source ref; path needs ADR confirmation where conflicted. |
| Fixture | `fixtures/pipeline_specs/people-dna-land/` or accepted fixture home | Must avoid living-person, DNA, private identifiers, or sensitive raw values. |
| Spec validation test | `tests/pipeline_specs/people-dna-land/` | Verifies shape, boundaries, and deny-by-default gates. |
| Runtime output | `data/` lifecycle homes | Never beside the spec. |
| Receipts | `data/receipts/pipeline/people-dna-land/` or accepted receipt home | Emitted by execution, not by spec file alone. |
| Evidence proof | `data/proofs/evidence_bundle/` | Referenced by spec; not created here. |
| Release material | `release/candidates/people-dna-land/`, `release/manifests/people-dna-land/` | Release authority owns final state. |

[⬆ Back to top](#top)

---

## 13. Minimal spec profile shape

```yaml
schema_version: kfm.pipeline_spec.people_dna_land.v1
spec_id: people-dna-land.<profile>
version: 0.1.0
status: draft
bounded_context: people-dna-land
owner: <people-dna-land-domain-steward>
implementation:
  target_pipeline: pipelines/domains/people-dna-land/<lane>
  execution_mode: dry_run_first
sources:
  source_descriptor_refs: []
lifecycle:
  input_state: WORK
  output_state: PROCESSED
requirements:
  evidence_bundle_required: true
  living_person_deny_by_default: true
  consent_scope_required: true
  revocation_check_required: true
  dna_boundary_required: true
  title_boundary_required: true
  receipts_required: []
  release_ready: false
anti_collapse:
  spec_is_executable: false
  assertion_is_public_truth: false
  relationship_hypothesis_is_confirmed: false
  dna_hint_is_public_kinship_claim: false
  assessor_record_is_title_truth: false
  parcel_geometry_is_title_boundary_proof: false
  spec_is_release_approval: false
```

[⬆ Back to top](#top)

---

## 14. Tests, fixtures, and validation

Recommended validation coverage:

```text
tests/pipeline_specs/people-dna-land/
├── test_spec_shape.py                    # PROPOSED
├── test_no_runtime_outputs.py            # PROPOSED
├── test_alias_boundary.py                # PROPOSED
├── test_implementation_refs.py           # PROPOSED
├── test_source_descriptor_refs.py        # PROPOSED
├── test_living_person_deny_by_default.py # PROPOSED
├── test_consent_and_revocation_gates.py  # PROPOSED
├── test_dna_boundary.py                  # PROPOSED
├── test_land_title_boundary.py           # PROPOSED
├── test_required_receipts.py             # PROPOSED
└── test_root_boundary.py                 # PROPOSED
```

A spec is not ready for execution until it has schema validation, fixture coverage, owner review, source descriptor refs, lifecycle-state assertions, privacy/consent gates, DNA and land-boundary gates, receipt requirements, and release/correction/rollback posture where applicable.

[⬆ Back to top](#top)

---

## 15. Definition of done

This README is done when it:

- replaces the short `pipeline_specs/people-dna-land/README.md` stub;
- identifies this path as People / Genealogy / DNA / Land declarative pipeline configuration;
- preserves the `pipeline_specs/` versus `pipelines/` split;
- blocks specs from becoming executable logic, data storage, proof storage, privacy or consent decisions, relationship truth, DNA publication, title truth, release approval, or public API/UI authority;
- defines expected People/DNA/Land profile families, lifecycle gates, privacy/consent gates, DNA and land-boundary gates, receipts, tests, and open questions.

Future spec files are done only when they validate, point to executable lanes, use stable source descriptors, declare lifecycle states, require receipts, preserve evidence/privacy/consent/anti-collapse posture, and document release/correction/rollback expectations.

[⬆ Back to top](#top)

---

## 16. Open questions

| ID | Question | Status |
|---|---|---|
| `PIPE-SPEC-PDL-001` | Which People / Genealogy / DNA / Land spec schema is canonical? | NEEDS VERIFICATION |
| `PIPE-SPEC-PDL-002` | Should `pipeline_specs/people/` remain an alias or be migrated fully into this path? | NEEDS VERIFICATION / ADR |
| `PIPE-SPEC-PDL-003` | Which first-wave source descriptors can be activated without living-person, DNA, or private person-parcel leakage? | NEEDS VERIFICATION |
| `PIPE-SPEC-PDL-004` | Which CI workflow validates People/DNA/Land specs and alias boundaries? | UNKNOWN |
| `PIPE-SPEC-PDL-005` | Which consent, revocation, privacy, review, redaction, title-boundary, and release-readiness receipt vocabulary is canonical? | NEEDS VERIFICATION |
| `PIPE-SPEC-PDL-006` | Should specs be split by sublane, assertion type, source family, privacy tier, consent tier, or release tier? | NEEDS VERIFICATION / ADR |

---

## Maintainer note

Keep this directory declarative and governance-heavy. Do not add executable code, source clients, schemas, contracts, policy decisions, consent decisions, lifecycle outputs, receipts, EvidenceBundles, release decisions, public API code, UI code, living-person records, DNA records, title decisions, parcel-boundary proof, person-parcel public joins, or generated summaries here. Add those to their responsibility roots and reference them from specs by stable path or identifier.
