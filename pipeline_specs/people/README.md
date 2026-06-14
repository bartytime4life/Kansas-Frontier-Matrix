<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-people-readme
title: People Pipeline Specs Alias README
type: readme
version: v0.1
status: draft
owners:
  - <pipeline-spec-steward>
  - <people-dna-land-domain-steward>
  - <privacy-steward>
  - <consent-steward>
  - <pipeline-owner>
  - <evidence-steward>
  - <policy-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: restricted-doctrine
path: pipeline_specs/people/README.md
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - pipeline_specs/README.md
  - pipeline_specs/people-dna-land/
  - pipelines/README.md
  - pipelines/domains/people/README.md
  - pipelines/domains/people-dna-land/README.md
  - docs/domains/people-dna-land/ARCHITECTURE.md
  - docs/domains/people-dna-land/SCOPE_AND_BOUNDARY.md
  - docs/domains/people-dna-land/SENSITIVITY.md
  - docs/domains/people-dna-land/PEOPLE_DOMAIN_MODEL.md
  - data/registry/sources/people-dna-land/
  - data/receipts/pipeline/people-dna-land/
  - data/proofs/evidence_bundle/
  - tests/pipeline_specs/people/
  - fixtures/pipeline_specs/people/
tags: [kfm, pipeline-specs, people, people-dna-land, compatibility-alias, genealogy, assertions, privacy, consent, living-person, dna-boundary, land-boundary, receipts, governance]
notes:
  - "This README replaces the one-character pipeline_specs/people stub with a governed declarative-spec alias contract."
  - "pipeline_specs/ is declarative configuration — the what. pipelines/ is executable logic — the how."
  - "The governing bounded context remains People / Genealogy / DNA / Land Ownership unless an ADR resolves the people vs people-dna-land segment naming conflict differently."
  - "Living-person fields, DNA/genomic outputs, raw kit/vendor identifiers, exact burial coordinates, and private person-parcel joins are deny-by-default."
  - "Assessor/tax records are not title truth, and parcel geometry is not title-boundary proof."
  - "Concrete spec filenames, schema validation, CI coverage, consent wiring, and activation state remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# People Pipeline Specs Alias

> Compatibility README for the requested `pipeline_specs/people/` path. This path must not become a parallel authority beside the People / Genealogy / DNA / Land bounded context. Until an ADR resolves segment naming, use this path only for carefully bounded People-sublane declarative profiles or compatibility documentation.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipeline__specs%2F-0a7ea4)
![authority](https://img.shields.io/badge/authority-compatibility%20alias-d62728)
![canonical](https://img.shields.io/badge/governing%20context-people--dna--land-d62728)
![sensitivity](https://img.shields.io/badge/living%20person%20%2F%20DNA-deny%20by%20default-d62728)

**Status:** Draft  
**Path:** `pipeline_specs/people/README.md`  
**Responsibility root:** `pipeline_specs/` — declarative pipeline configuration, the **what**  
**Bounded-context posture:** `people` is a compatibility/alias segment for People / Genealogy / DNA / Land controls  
**Companion implementation posture:** `pipelines/domains/people/` is also alias-gated; whole-context execution should resolve through the accepted People / Genealogy / DNA / Land lane  
**Placement posture:** `CONFLICTED / NEEDS VERIFICATION` until the `people` vs `people-dna-land` segment naming conflict is resolved by ADR, path map, migration note, and rollback note.  
**Public posture:** no public release, data storage, source admission, consent decision, privacy decision, or executable side effect; specs only configure governed pipeline runs.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Alias and authority posture](#2-alias-and-authority-posture)
- [3. Sensitivity and consent boundary](#3-sensitivity-and-consent-boundary)
- [4. Spec anti-collapse rules](#4-spec-anti-collapse-rules)
- [5. What belongs here](#5-what-belongs-here)
- [6. What does not belong here](#6-what-does-not-belong-here)
- [7. People spec scope](#7-people-spec-scope)
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

`pipeline_specs/people/` is a compatibility/alias lane for declarative People-sublane pipeline profiles.

It may describe:

- which People-sublane profile should run;
- which source descriptor ids are in scope;
- which assertion, identity-candidate, relationship, life-event, residence, migration, or public-safe derivative profile is intended;
- which privacy, consent, living-person, DNA-boundary, title-boundary, and public-safe transform gates apply;
- which lifecycle gates are required;
- which fixtures support no-network tests;
- which receipts, reports, blockers, and review handoffs are expected;
- which downstream implementation lane is authorized to execute the spec.

It does **not** establish `people` as a new canonical bounded context. The governing semantics, privacy posture, consent posture, title-boundary posture, and release posture are inherited from People / Genealogy / DNA / Land.

[⬆ Back to top](#top)

---

## 2. Alias and authority posture

| Question | Answer | Status |
|---|---|---|
| Why `pipeline_specs/`? | This root owns declarative pipeline configuration, separate from implementation. | CONFIRMED root contract |
| Why `people/`? | User requested this path, and `people` appears as a short segment in the People/DNA/Land naming conflict. | PROPOSED / NEEDS VERIFICATION |
| Is `people` canonical? | Not proven. The visible domain docs identify `people-dna-land` as the governing bounded context and record `people` vs `people-dna-land` as an open conflict. | CONFLICTED / NEEDS ADR |
| Can this path create parallel authority? | No. It must not create duplicate schemas, contracts, policies, registries, data lanes, or release lanes. | CONFIRMED governance posture |
| Does this execute pipelines? | No. Execution belongs under `pipelines/`. | CONFIRMED separation |
| Does this store data or receipts? | No. Lifecycle data and receipts belong under `data/`. | CONFIRMED lifecycle posture |
| Can this approve release? | No. Specs can require gates only; release authority remains separate. | CONFIRMED release separation |

> [!IMPORTANT]
> A short path is not a shortcut around People / Genealogy / DNA / Land controls. This directory cannot publish living-person, DNA, relationship, land-title, parcel, or person-parcel claims.

[⬆ Back to top](#top)

---

## 3. Sensitivity and consent boundary

People-sublane specs inherit the strict People / Genealogy / DNA / Land boundary:

- living-person fields are deny-by-default;
- DNA-derived relationship hypotheses are restricted even when a People profile references them;
- raw DNA kit ids, vendor identifiers, match lists, and segment details must not appear here;
- consent scope, purpose, retention, and revocation must be enforced where applicable;
- exact burial coordinates and culturally sensitive family/place context fail closed;
- generated summaries cannot convert assertions or hypotheses into confirmed truth;
- graph projections cannot replace canonical review state;
- public derivatives require release review, rollback, correction path, and public-safe transform receipts.

When a profile cannot prove consent, rights, living-person status, privacy posture, or release posture, the profile must fail closed or route to quarantine/review.

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
DNA hint -> public kinship claim
ConsentGrant reference -> unrestricted publication
Assessor Record -> title truth
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
- person assertion, identity candidate, canonical identity, relationship hypothesis, relationship assertion, DNA evidence, consent, land instrument, assessor record, parcel version, and title-boundary posture remain separately labeled;
- release decisions stay under `release/`.

[⬆ Back to top](#top)

---

## 5. What belongs here

Appropriate contents include declarative People-sublane specs for:

- assertion-intake profiles;
- identity-candidate grouping profiles;
- name assertion profiles;
- life-event profiles;
- residence and migration profiles;
- relationship assertion profiles;
- family-group review-handoff profiles;
- public-safe person-context derivative profiles;
- watcher, validation, catalog, triplet, publish-readiness, rollback-readiness, and dry-run profiles that preserve People / Genealogy / DNA / Land controls.

A good placement test:

> If the file answers “what People-sublane profile should run, with what scope, privacy gates, consent gates, assertion boundaries, and release blockers?”, it may belong here. If it answers “how does the pipeline execute?”, it belongs under `pipelines/`.

[⬆ Back to top](#top)

---

## 6. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Executable People pipeline code | `pipelines/domains/people/` or accepted People / Genealogy / DNA / Land implementation lane |
| DNA pipeline logic | accepted People / Genealogy / DNA / Land DNA implementation lane |
| Land-title or parcel pipeline logic | accepted People / Genealogy / DNA / Land land implementation lane |
| Source connectors | `connectors/<source>` |
| Source descriptors | `data/registry/sources/people-dna-land/` or accepted registry home |
| Object meaning | `contracts/domains/people-dna-land/`, `contracts/people/`, and domain doctrine |
| JSON Schemas | `schemas/contracts/v1/domains/people-dna-land/`, `schemas/contracts/v1/people/`, or accepted schema home |
| Policy, consent, privacy, rights, or sensitivity decisions | `policy/domains/people-dna-land/`, `policy/consent/people-dna-land/`, `policy/sensitivity/people-dna-land/`, review roots |
| Tests | `tests/pipeline_specs/people/` or accepted test home |
| Fixtures | `fixtures/pipeline_specs/people/` or accepted fixture home |
| Lifecycle data | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/triplets`, `data/published` |
| EvidenceBundles | `data/proofs/evidence_bundle/` |
| Release decisions/manifests/corrections/rollback cards | `release/` |
| Public API/UI code | `apps/governed-api/`, `apps/explorer-web/`, packages |

[⬆ Back to top](#top)

---

## 7. People spec scope

People-sublane specs may configure profiles for object families and candidate products such as:

- Person Assertion;
- Person Identity Candidate;
- PersonCanonical review handoff, not public truth;
- NameAssertion;
- LifeEvent;
- Residence Event;
- Migration Event;
- RelationshipAssertion;
- FamilyGroup review handoff;
- public-safe, release-reviewed person-context derivatives.

DNA-derived evidence, land ownership assertions, deed/title instruments, assessor/tax records, parcel versions, ownership intervals, and person-parcel joins remain governed by the wider People / Genealogy / DNA / Land context and must not be smuggled through this alias path.

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

Every People-sublane spec should declare or explicitly mark not applicable:

1. **Profile identity gate** — stable `spec_id`, owner, bounded context, lane, and version.
2. **Implementation gate** — target executable lane under `pipelines/`.
3. **Source gate** — source descriptor refs and source roles.
4. **Lifecycle gate** — allowed input and output lifecycle states.
5. **Assertion gate** — assertion, candidate, reviewed identity, and public derivative distinctions.
6. **Living-person gate** — deny-by-default unless release posture is explicitly permitted.
7. **Consent gate** — scope, purpose, retention, and revocation checks where applicable.
8. **DNA-boundary gate** — DNA hints and relationship hypotheses remain restricted.
9. **Land-boundary gate** — assessor/tax records and parcel geometry do not become title truth.
10. **Evidence gate** — EvidenceRef/EvidenceBundle requirements for claims.
11. **Receipt gate** — required run, transform, validation, consent, revocation, review, redaction, or release-readiness receipts.
12. **Release gate** — ReleaseManifest input requirements, rollback target, and correction path where output can publish.

[⬆ Back to top](#top)

---

## 10. Directory contract

Recommended alias-safe shape:

```text
pipeline_specs/people/
├── README.md
├── assertions.yaml              # PROPOSED
├── identity_candidates.yaml     # PROPOSED
├── names.yaml                   # PROPOSED
├── life_events.yaml             # PROPOSED
├── residence_migration.yaml     # PROPOSED
├── relationships.yaml           # PROPOSED
├── family_groups.yaml           # PROPOSED
├── public_derivatives.yaml      # PROPOSED
├── validate.yaml                # PROPOSED
├── publish_readiness.yaml       # PROPOSED
├── rollback.yaml                # PROPOSED
└── watchers.yaml                # PROPOSED
```

These filenames are proposed placeholders until actual spec files, schema validation, CI coverage, and ADR/path resolution are implemented.

[⬆ Back to top](#top)

---

## 11. Spec profile families

| Profile family | Purpose | Implementation lane |
|---|---|---|
| `assertions` | Declare person assertion intake and evidence requirements. | accepted People implementation lane |
| `identity_candidates` | Declare identity grouping without creating canonical public identity. | accepted People implementation lane |
| `names` | Declare name assertion normalization and source-role checks. | accepted People implementation lane |
| `life_events` | Declare event assertion profile and temporal gates. | accepted People implementation lane |
| `residence_migration` | Declare place/time assertion profile and public-safe posture. | accepted People implementation lane |
| `relationships` | Declare relationship assertion or hypothesis profiles without public confirmation. | accepted People implementation lane |
| `family_groups` | Declare review handoff for grouped relationship assertions. | accepted People implementation lane |
| `public_derivatives` | Declare release-reviewed public-safe derivatives only. | accepted People implementation lane |
| `watchers` | Declare source-change observation profiles. | accepted watcher implementation lane |

[⬆ Back to top](#top)

---

## 12. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Spec file | `pipeline_specs/people/` | Alias-gated declarative config only. |
| Executable target | `pipelines/domains/people/` or accepted People / Genealogy / DNA / Land implementation lane | The spec references it; it does not implement it. |
| Source descriptor | `data/registry/sources/people-dna-land/` | Stable source ref; path needs ADR confirmation. |
| Fixture | `fixtures/pipeline_specs/people/` or accepted fixture home | Must avoid living-person, DNA, private identifiers, or sensitive raw values. |
| Spec validation test | `tests/pipeline_specs/people/` | Verifies shape, alias boundaries, and deny-by-default gates. |
| Runtime output | `data/` lifecycle homes | Never beside the spec. |
| Receipts | `data/receipts/pipeline/people-dna-land/` or accepted receipt home | Emitted by execution, not by spec file alone. |
| Evidence proof | `data/proofs/evidence_bundle/` | Referenced by spec; not created here. |
| Release material | `release/candidates/people-dna-land/`, `release/manifests/people-dna-land/` | Release authority owns final state. |

[⬆ Back to top](#top)

---

## 13. Minimal spec profile shape

```yaml
schema_version: kfm.pipeline_spec.people.v1
spec_id: people.<profile>
version: 0.1.0
status: draft
bounded_context: people-dna-land
lane: people
owner: <people-dna-land-domain-steward>
implementation:
  target_pipeline: pipelines/domains/people/<lane>
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
  assessor_record_is_title_truth: false
  parcel_geometry_is_title_boundary_proof: false
  spec_is_release_approval: false
```

[⬆ Back to top](#top)

---

## 14. Tests, fixtures, and validation

Recommended validation coverage:

```text
tests/pipeline_specs/people/
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

- replaces the one-character `pipeline_specs/people/README.md` stub;
- marks this path as a People-sublane compatibility/alias spec lane;
- preserves the `pipeline_specs/` versus `pipelines/` split;
- blocks specs from becoming executable logic, data storage, proof storage, privacy or consent decisions, relationship truth, DNA publication, title truth, release approval, or public API/UI authority;
- defines expected People profile families, lifecycle gates, privacy/consent gates, DNA and land-boundary gates, receipts, tests, and open questions.

Future spec files are done only when they validate, point to executable lanes, use stable source descriptors, declare lifecycle states, require receipts, preserve evidence/privacy/consent/anti-collapse posture, and document release/correction/rollback expectations.

[⬆ Back to top](#top)

---

## 16. Open questions

| ID | Question | Status |
|---|---|---|
| `PIPE-SPEC-PEOPLE-001` | Should `pipeline_specs/people/` remain an alias or be migrated into `pipeline_specs/people-dna-land/`? | NEEDS VERIFICATION / ADR |
| `PIPE-SPEC-PEOPLE-002` | Which People spec schema is canonical for this alias path? | NEEDS VERIFICATION |
| `PIPE-SPEC-PEOPLE-003` | Which first-wave source descriptors can be used without living-person or DNA leakage? | NEEDS VERIFICATION |
| `PIPE-SPEC-PEOPLE-004` | Which CI workflow validates People specs and alias boundaries? | UNKNOWN |
| `PIPE-SPEC-PEOPLE-005` | Which consent, revocation, privacy, review, redaction, and release-readiness receipt vocabulary is canonical? | NEEDS VERIFICATION |
| `PIPE-SPEC-PEOPLE-006` | Should People specs be split by assertion type, source family, privacy tier, consent tier, or release tier? | NEEDS VERIFICATION / ADR |

---

## Maintainer note

Keep this directory declarative and alias-safe. Do not add executable code, source clients, schemas, contracts, policy decisions, consent decisions, lifecycle outputs, receipts, EvidenceBundles, release decisions, public API code, UI code, living-person records, DNA records, title decisions, parcel-boundary proof, person-parcel public joins, or generated summaries here. Add those to their responsibility roots and reference them from specs by stable path or identifier.
