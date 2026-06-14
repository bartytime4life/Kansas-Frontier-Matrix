<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-people-dna-land-land-ownership-readme
title: People DNA Land Land Ownership Pipeline Specs README
type: readme
version: v0.1
status: draft
owners:
  - <pipeline-spec-steward>
  - <people-dna-land-domain-steward>
  - <land-records-steward>
  - <privacy-steward>
  - <evidence-steward>
  - <policy-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: restricted-doctrine
path: pipeline_specs/people-dna-land/land-ownership/README.md
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - pipeline_specs/README.md
  - pipeline_specs/people-dna-land/README.md
  - pipelines/README.md
  - pipelines/domains/people-dna-land/README.md
  - pipelines/domains/people-dna-land/land-ownership/README.md
  - docs/domains/people-dna-land/ARCHITECTURE.md
  - docs/domains/people-dna-land/sublanes/land.md
  - docs/domains/people-dna-land/sublanes/land_ownership.md
  - docs/domains/people-dna-land/CHAIN_OF_TITLE_NOTES.md
  - data/registry/sources/people-dna-land/
  - data/receipts/pipeline/people-dna-land/land-ownership/
  - data/proofs/evidence_bundle/
  - tests/pipeline_specs/people-dna-land/land-ownership/
  - fixtures/pipeline_specs/people-dna-land/land-ownership/
tags: [kfm, pipeline-specs, people-dna-land, land-ownership, deed, title-instrument, land-instrument, assessor-record, tax-record, parcel-version, legal-description, ownership-interval, chain-of-title, declarative-config, receipts, governance]
notes:
  - "This README replaces the one-character pipeline_specs/people-dna-land/land-ownership stub with a governed declarative land-ownership-spec contract."
  - "pipeline_specs/ is declarative configuration — the what. pipelines/ is executable logic — the how."
  - "Land Ownership specs configure source scope, instrument and parcel posture, temporal gates, assertion-first boundaries, title-boundary anti-collapse rules, evidence gates, receipts, and release blockers. They do not execute pipeline logic or store lifecycle outputs."
  - "Assessor/tax records are not title truth, and parcel geometry is not title-boundary proof."
  - "Land ownership is an evidence-bound assertion workflow, not a bare public map label."
  - "Sensitive joins, unresolved rights, unsupported chain outputs, and over-broad public derivatives fail closed by default."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Land Ownership Pipeline Specs

> Declarative configuration lane for People / Genealogy / DNA / Land land-ownership profiles: land instruments, deed/title instrument handling, assessor/tax context, parcel-version refs, legal descriptions, ownership intervals, chain-of-title candidates, evidence requirements, fixtures, receipts, and release-readiness intent — separate from executable land-ownership pipeline logic.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipeline__specs%2F-0a7ea4)
![authority](https://img.shields.io/badge/authority-declarative%20config-0a7ea4)
![implementation](https://img.shields.io/badge/implementation-pipelines%2Fdomains%2Fpeople--dna--land%2Fland--ownership%2F-d62728)
![title](https://img.shields.io/badge/title%20truth-not%20determined%20here-d62728)

**Status:** Draft  
**Path:** `pipeline_specs/people-dna-land/land-ownership/README.md`  
**Responsibility root:** `pipeline_specs/` — declarative pipeline configuration, the **what**  
**Parent spec lane:** `pipeline_specs/people-dna-land/`  
**Companion implementation lane:** `pipelines/domains/people-dna-land/land-ownership/` — executable pipeline logic, the **how**  
**Placement posture:** land-ownership specs belong here as declarative profiles unless an ADR or migration note establishes a different accepted spec home.  
**Public posture:** no public release, data storage, title determination, parcel-boundary determination, ownership-label decision, or executable side effect; specs only configure governed pipeline runs.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Land-ownership boundary](#3-land-ownership-boundary)
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

`pipeline_specs/people-dna-land/land-ownership/` owns declarative Land Ownership pipeline configuration inside the People / Genealogy / DNA / Land bounded context.

It may describe:

- which land-ownership profile should run;
- which source descriptor ids are in scope;
- which deed, title instrument, land instrument, assessor, tax, legal-description, parcel-version, ownership-interval, or chain-of-title candidate profile is intended;
- which source-role, time, rights, title-boundary, person-link, privacy, and release-readiness gates apply;
- which lifecycle gates are required;
- which fixtures support no-network tests without leaking restricted content;
- which receipts, reports, blockers, and review handoffs are expected;
- which downstream implementation lane is authorized to execute the spec.

It does **not** implement pipeline behavior. Land Ownership execution belongs under `pipelines/domains/people-dna-land/land-ownership/` or an accepted implementation lane.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipeline_specs/`? | This root owns declarative pipeline configuration, separate from implementation. | CONFIRMED root contract |
| Why `people-dna-land/land-ownership/`? | This narrows the People / Genealogy / DNA / Land spec lane to land-instrument and ownership-assertion profiles. | CONFIRMED path pattern / NEEDS VERIFICATION for active specs |
| Does this execute pipelines? | No. Execution belongs under `pipelines/`. | CONFIRMED separation |
| Does this determine title or parcel boundaries? | No. Specs can require evidence and review gates only. | CONFIRMED boundary posture |
| Does this store data or receipts? | No. Lifecycle data and receipts belong under `data/`. | CONFIRMED lifecycle posture |
| Can this approve release? | No. Release decisions, manifests, correction notices, and rollback cards belong under release authority. | CONFIRMED release separation |

> [!IMPORTANT]
> A land-ownership spec says what should run and under which constraints. It is not a run, not a receipt, not evidence, not processed data, not title truth, not parcel-boundary proof, not a public ownership label, and not release approval.

[⬆ Back to top](#top)

---

## 3. Land-ownership boundary

Land Ownership specs inherit the People / Genealogy / DNA / Land sensitivity boundary:

- living-person or private-party exposure is deny-by-default unless explicitly reviewed and released;
- private person-parcel joins must not publish without explicit release authority;
- land instruments are evidence inputs, not automatic ownership truth;
- assessor and tax records are administrative context, not title truth;
- parcel geometry is versioned spatial evidence, not title-boundary proof;
- legal descriptions carry provenance, uncertainty, and interpretation limits;
- chain-of-title outputs are candidates or reports until reviewed;
- public derivatives require release review, rollback, correction path, and public-safe transform receipts.

When a profile cannot prove rights, source role, title-boundary posture, privacy posture, living-person posture, or release posture, the profile must fail closed or route to quarantine/review.

[⬆ Back to top](#top)

---

## 4. Spec anti-collapse rules

Disallowed collapses:

```text
spec file -> executable pipeline
spec profile -> release approval
source list -> source authority
assessor record -> title truth
tax record -> title truth
parcel polygon -> boundary proof
current parcel id -> stable historical parcel identity
land instrument mention -> confirmed ownership
ownership assertion -> public map label
chain-of-title candidate -> title determination
sensitive relation join -> public fact
generated summary -> evidence
```

Required separations:

- declarative specs stay in `pipeline_specs/`;
- executable logic stays in `pipelines/`;
- source descriptors stay in the source registry;
- lifecycle data stays in `data/`;
- receipts and proofs stay in their receipt/proof homes;
- contracts, schemas, and policy stay in their own roots;
- party references, land instruments, deed instruments, title instruments, assessor records, tax records, legal descriptions, parcel versions, ownership intervals, and chain-of-title candidates remain separately labeled;
- release decisions stay under `release/`.

[⬆ Back to top](#top)

---

## 5. What belongs here

Appropriate contents include declarative specs for:

- land ownership assertion profiles;
- ownership interval profiles;
- deed instrument and title instrument profile gates;
- land instrument and legal-description profile gates;
- assessor-record and tax-record context profiles;
- parcel-version and parcel-history profile gates;
- chain-of-title candidate and contradiction-report profiles;
- public-safe derivative profiles;
- watcher, validation, catalog, triplet, publish-readiness, rollback-readiness, and dry-run profiles that preserve People / Genealogy / DNA / Land controls.

A good placement test:

> If the file answers “what land-ownership profile should run, with what source scope, instrument posture, title-boundary checks, temporal gates, evidence requirements, and release blockers?”, it may belong here. If it answers “how does the pipeline execute?”, it belongs under `pipelines/`.

[⬆ Back to top](#top)

---

## 6. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Executable land-ownership pipeline code | `pipelines/domains/people-dna-land/land-ownership/` |
| Source connectors | `connectors/<source>` |
| Source descriptors | `data/registry/sources/people-dna-land/` or accepted registry home |
| Object meaning | `contracts/domains/people-dna-land/`, `contracts/people/`, and domain doctrine |
| JSON Schemas | `schemas/contracts/v1/domains/people-dna-land/`, `schemas/contracts/v1/people/`, or accepted schema home |
| Policy, privacy, rights, or sensitivity decisions | `policy/domains/people-dna-land/`, `policy/sensitivity/people-dna-land/`, review roots |
| Tests | `tests/pipeline_specs/people-dna-land/land-ownership/` or accepted test home |
| Fixtures | `fixtures/pipeline_specs/people-dna-land/land-ownership/` or accepted fixture home |
| Lifecycle data | `data/raw`, `data/work`, `data/quarantine`, `data/processed`, `data/catalog`, `data/triplets`, `data/published` |
| EvidenceBundles | `data/proofs/evidence_bundle/` |
| Release decisions/manifests/corrections/rollback cards | `release/` |
| Public API/UI code | `apps/governed-api/`, `apps/explorer-web/`, packages |

[⬆ Back to top](#top)

---

## 7. Spec scope

Land Ownership specs may configure profiles for object families and candidate products such as:

- Land Ownership Assertion;
- Ownership Interval;
- Deed Instrument;
- Title Instrument;
- LandInstrument;
- LegalDescription;
- Assessor Record;
- TaxRecord;
- Parcel Version;
- party reference and person/entity linking handoffs;
- chain-of-title candidates, gap reports, contradiction reports, and review handoff packages;
- public-safe, release-reviewed derivatives that avoid title, boundary, and privacy overclaims.

This sublane may cite People, Spatial Foundation, Settlements, Roads/Rail, Archaeology, Hydrology, Agriculture, Hazards, and other domains for context, but those cross-lane contexts must not weaken privacy, title-boundary, source-role, or release controls.

[⬆ Back to top](#top)

---

## 8. Lifecycle posture

Specs may target lifecycle stages, but do not create lifecycle transitions themselves:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A spec may declare input lifecycle state, expected output lifecycle state, source descriptor refs, source-role labels, instrument-date and recording-date gates, valid-time and source-time handling, parcel-version refs, legal-description posture, EvidenceBundle requirements, receipt requirements, release blockers, rollback support, and correction support.

Only governed pipeline implementation and release authority can perform transitions.

[⬆ Back to top](#top)

---

## 9. Required gates

Every Land Ownership spec should declare or explicitly mark not applicable:

1. **Profile identity gate** — stable `spec_id`, owner, bounded context, sublane, and version.
2. **Implementation gate** — target executable lane under `pipelines/`.
3. **Source gate** — source descriptor refs and source roles.
4. **Lifecycle gate** — allowed input and output lifecycle states.
5. **Instrument gate** — deed/title/land-instrument source role, recording date, instrument date, parties, and provenance.
6. **Parcel-version gate** — parcel id, geometry version, source time, valid time, uncertainty, and non-boundary-proof posture.
7. **Assessor/tax gate** — administrative context only, not title truth.
8. **Title-boundary gate** — no title or boundary determination is created by a spec or run.
9. **Privacy gate** — living-person and private relation joins fail closed until reviewed and released.
10. **Evidence gate** — EvidenceRef/EvidenceBundle requirements for claims.
11. **Receipt gate** — required run, transform, validation, chain-review, contradiction, title-boundary, redaction, or release-readiness receipts.
12. **Release gate** — ReleaseManifest input requirements, rollback target, and correction path where output can publish.

[⬆ Back to top](#top)

---

## 10. Directory contract

Recommended shape:

```text
pipeline_specs/people-dna-land/land-ownership/
├── README.md
├── ingest.yaml                  # PROPOSED
├── normalize.yaml               # PROPOSED
├── validate.yaml                # PROPOSED
├── catalog.yaml                 # PROPOSED
├── triplets.yaml                # PROPOSED
├── publish.yaml                 # PROPOSED
├── rollback.yaml                # PROPOSED
├── watchers.yaml                # PROPOSED
├── land_instruments.yaml        # PROPOSED
├── deed_title_instruments.yaml  # PROPOSED
├── assessor_tax_records.yaml    # PROPOSED
├── parcel_versions.yaml         # PROPOSED
├── ownership_intervals.yaml     # PROPOSED
├── legal_descriptions.yaml      # PROPOSED
└── chain_of_title_candidates.yaml # PROPOSED
```

These filenames are proposed placeholders until actual spec files, schema validation, CI coverage, and ADR/path resolution are implemented.

[⬆ Back to top](#top)

---

## 11. Spec profile families

| Profile family | Purpose | Implementation lane |
|---|---|---|
| `ingest` | Declare source intake scope and prerequisites. | `pipelines/domains/people-dna-land/land-ownership/` or shared ingest lane |
| `normalize` | Declare transform profile, expected receipts, and blockers. | Land Ownership normalize implementation |
| `validate` | Declare source-role, instrument, parcel-version, time, rights, and title-boundary checks. | Land Ownership validate implementation |
| `catalog` | Declare catalog closure requirements. | Land Ownership catalog implementation |
| `triplets` | Declare graph/triplet projection profile without replacing review state. | Land Ownership triplet implementation |
| `publish` | Declare release-candidate readiness checks. | Land Ownership publish support |
| `rollback` | Declare rollback-readiness check profile. | Land Ownership rollback support |
| `watchers` | Declare source-change observation profiles. | Land Ownership watcher support |
| `instrument` | Declare deed, title, land instrument, legal description, assessor/tax, and parcel-version variants. | Domain sublane implementations |
| `chain` | Declare chain-of-title candidate, gap, contradiction, and review-handoff profiles. | Domain sublane implementations |

[⬆ Back to top](#top)

---

## 12. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Spec file | `pipeline_specs/people-dna-land/land-ownership/` | Declarative config only. |
| Executable target | `pipelines/domains/people-dna-land/land-ownership/` or accepted pipeline lane | The spec references it; it does not implement it. |
| Source descriptor | `data/registry/sources/people-dna-land/` | Stable source ref; path needs ADR confirmation where conflicted. |
| Fixture | `fixtures/pipeline_specs/people-dna-land/land-ownership/` or accepted fixture home | Must avoid living-person, private identifiers, or sensitive raw values. |
| Spec validation test | `tests/pipeline_specs/people-dna-land/land-ownership/` | Verifies shape, boundaries, and anti-collapse gates. |
| Runtime output | `data/` lifecycle homes | Never beside the spec. |
| Receipts | `data/receipts/pipeline/people-dna-land/land-ownership/` or accepted receipt home | Emitted by execution, not by spec file alone. |
| Evidence proof | `data/proofs/evidence_bundle/` | Referenced by spec; not created here. |
| Release material | `release/candidates/people-dna-land/`, `release/manifests/people-dna-land/` | Release authority owns final state. |

[⬆ Back to top](#top)

---

## 13. Minimal spec profile shape

```yaml
schema_version: kfm.pipeline_spec.people_dna_land.land_ownership.v1
spec_id: people-dna-land.land-ownership.<profile>
version: 0.1.0
status: draft
bounded_context: people-dna-land
sublane: land-ownership
owner: <land-records-steward>
implementation:
  target_pipeline: pipelines/domains/people-dna-land/land-ownership/<lane>
  execution_mode: dry_run_first
sources:
  source_descriptor_refs: []
lifecycle:
  input_state: WORK
  output_state: PROCESSED
requirements:
  evidence_bundle_required: true
  source_role_required: true
  instrument_date_required: true
  recording_date_required: true
  parcel_version_required: true
  legal_description_provenance_required: true
  title_boundary_overclaim_blocked: true
  assessor_tax_context_only: true
  receipts_required: []
  release_ready: false
anti_collapse:
  spec_is_executable: false
  assessor_record_is_title_truth: false
  tax_record_is_title_truth: false
  parcel_geometry_is_title_boundary_proof: false
  chain_candidate_is_title_determination: false
  ownership_assertion_is_public_label: false
  spec_is_release_approval: false
```

[⬆ Back to top](#top)

---

## 14. Tests, fixtures, and validation

Recommended validation coverage:

```text
tests/pipeline_specs/people-dna-land/land-ownership/
├── test_spec_shape.py                    # PROPOSED
├── test_no_runtime_outputs.py            # PROPOSED
├── test_implementation_refs.py           # PROPOSED
├── test_source_descriptor_refs.py        # PROPOSED
├── test_instrument_temporal_gates.py     # PROPOSED
├── test_parcel_version_boundary.py       # PROPOSED
├── test_assessor_tax_context_only.py     # PROPOSED
├── test_chain_candidate_not_title.py     # PROPOSED
├── test_required_receipts.py             # PROPOSED
└── test_root_boundary.py                 # PROPOSED
```

A spec is not ready for execution until it has schema validation, fixture coverage, owner review, source descriptor refs, lifecycle-state assertions, instrument/time gates, parcel-version gates, assessor/tax context-only checks, title-boundary checks, receipt requirements, and release/correction/rollback posture where applicable.

[⬆ Back to top](#top)

---

## 15. Definition of done

This README is done when it:

- replaces the one-character `pipeline_specs/people-dna-land/land-ownership/README.md` stub;
- identifies this path as Land Ownership declarative pipeline configuration;
- preserves the `pipeline_specs/` versus `pipelines/` split;
- blocks specs from becoming executable logic, data storage, proof storage, policy decisions, title determinations, parcel-boundary determinations, public ownership labels, release approval, or public API/UI authority;
- defines expected Land Ownership profile families, lifecycle gates, instrument gates, parcel-version gates, title-boundary gates, receipts, tests, and open questions.

Future spec files are done only when they validate, point to executable lanes, use stable source descriptors, declare lifecycle states, require receipts, preserve evidence/source-role/title-boundary posture, and document release/correction/rollback expectations.

[⬆ Back to top](#top)

---

## 16. Open questions

| ID | Question | Status |
|---|---|---|
| `PIPE-SPEC-PDL-LAND-001` | Which Land Ownership spec schema is canonical? | NEEDS VERIFICATION |
| `PIPE-SPEC-PDL-LAND-002` | Should the canonical profile file be `land-ownership.yaml`, this nested directory, or both with one as an alias? | NEEDS VERIFICATION / ADR |
| `PIPE-SPEC-PDL-LAND-003` | Which first-wave source descriptors can be activated without living-person, rights, or private person-parcel leakage? | NEEDS VERIFICATION |
| `PIPE-SPEC-PDL-LAND-004` | Which CI workflow validates Land Ownership specs and title-boundary gates? | UNKNOWN |
| `PIPE-SPEC-PDL-LAND-005` | Which instrument, chain-review, parcel-version, title-boundary, contradiction, and release-readiness receipt vocabulary is canonical? | NEEDS VERIFICATION |
| `PIPE-SPEC-PDL-LAND-006` | Should specs be split by source family, instrument type, parcel workflow, chain-of-title workflow, or release tier? | NEEDS VERIFICATION / ADR |

---

## Maintainer note

Keep this directory declarative and title-boundary safe. Do not add executable code, source clients, schemas, contracts, policy decisions, lifecycle outputs, receipts, EvidenceBundles, release decisions, public API code, UI code, title determinations, parcel-boundary proof, public ownership labels, private person-parcel joins, or generated summaries here. Add those to their responsibility roots and reference them from specs by stable path or identifier.
