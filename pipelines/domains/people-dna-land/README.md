<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-people-dna-land-readme
title: People DNA Land Domain Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <people-dna-land-pipeline-owner>
  - <people-dna-land-domain-steward>
  - <privacy-steward>
  - <consent-steward>
  - <land-records-steward>
  - <source-steward>
  - <evidence-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: restricted-doctrine
path: pipelines/domains/people-dna-land/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - docs/domains/people-dna-land/ARCHITECTURE.md
  - docs/domains/people-dna-land/SCOPE_AND_BOUNDARY.md
  - docs/domains/people-dna-land/SENSITIVITY.md
  - docs/domains/people-dna-land/SENSITIVITY_PROFILE.md
  - docs/domains/people-dna-land/PEOPLE_DOMAIN_MODEL.md
  - docs/domains/people-dna-land/DATA_LIFECYCLE.md
  - docs/domains/people-dna-land/SOURCE_REGISTRY.md
  - docs/domains/people-dna-land/API_CONTRACTS.md
  - docs/domains/people-dna-land/MAP_UI_CONTRACTS.md
  - docs/domains/people-dna-land/CANONICAL_PATHS.md
  - docs/domains/people-dna-land/sublanes/people.md
  - docs/domains/people-dna-land/sublanes/dna.md
  - docs/domains/people-dna-land/sublanes/land.md
  - pipeline_specs/people-dna-land/
  - pipeline_specs/people/
  - contracts/domains/people-dna-land/
  - contracts/people/
  - schemas/contracts/v1/domains/people-dna-land/
  - schemas/contracts/v1/people/
  - policy/domains/people-dna-land/
  - policy/sensitivity/people-dna-land/
  - policy/consent/people-dna-land/
  - data/raw/people-dna-land/
  - data/work/people-dna-land/
  - data/quarantine/people-dna-land/
  - data/processed/people-dna-land/
  - data/catalog/domain/people-dna-land/
  - data/triplets/people-dna-land/
  - data/published/layers/people-dna-land/
  - data/registry/sources/people-dna-land/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/people-dna-land/
  - release/manifests/people-dna-land/
tags:
  - kfm
  - pipelines
  - domains
  - people-dna-land
  - people
  - genealogy
  - dna
  - land-ownership
  - consent
  - privacy
  - title-boundary
  - assertion-first
  - evidence
  - policy
  - governance
notes:
  - "This README replaces the greenfield scaffold for pipelines/domains/people-dna-land."
  - "People/DNA/Land pipeline logic is executable implementation support only; it does not own object meaning, schemas, source descriptors, policy, consent authority, lifecycle data, catalog truth, legal title determinations, genealogy truth, DNA relationship determinations, or release decisions."
  - "Living-person data, DNA/genomic data, raw kit/vendor identifiers, exact burial coordinates, and private person-parcel joins are deny-by-default."
  - "Assessor/tax records are not title truth, and parcel geometry is not title-boundary proof."
  - "Segment naming remains CONFLICTED / NEEDS VERIFICATION: Directory Rules/docs use people-dna-land while some Atlas/schema crosswalks use people. Do not create parallel authority homes without ADR/path resolution."
  - "Concrete executable behavior, source activation, schedules, CI coverage, schema paths, consent wiring, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# 🧬 People / DNA / Land Domain Pipeline

> Executable People / Genealogy / DNA / Land Ownership pipeline lane for converting admitted person, genealogy, consent, DNA evidence, land-instrument, assessor, tax, parcel, ownership-interval, residence, and relationship-hypothesis source material into governed candidates, quarantine records, processed records, catalog/triplet handoffs, receipts, and release-review packages — **without exposing living-person, DNA, raw-kit, title, parcel-boundary, private person-parcel, or culturally sensitive information outside governed review**.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-people%20DNA%20land%20pipeline-2e7d32)
![authority](https://img.shields.io/badge/authority-executable%20logic-0a7ea4)
![sensitivity](https://img.shields.io/badge/T4%20deny--by--default-d62728)
![consent](https://img.shields.io/badge/consent-required%20where%20applicable-d62728)
![publication](https://img.shields.io/badge/publication-release%20gated-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/people-dna-land/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** People / Genealogy / DNA / Land Ownership  
**Placement posture:** `people-dna-land` child lane under `pipelines/domains/`; segment naming and schema/contract path forms remain `CONFLICTED / NEEDS VERIFICATION` until ADR/path resolution  
**Public posture:** no direct publication; public output requires lifecycle, EvidenceBundle, source-role, rights, consent where applicable, sensitivity, policy, catalog/triplet, release, correction, and rollback closure

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Sensitivity and consent boundary](#3-sensitivity-and-consent-boundary)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Pipeline scope](#6-pipeline-scope)
- [7. Source-family posture](#7-source-family-posture)
- [8. Lifecycle contract](#8-lifecycle-contract)
- [9. Required gates](#9-required-gates)
- [10. Assertion-first, title-boundary, and public-safe posture](#10-assertion-first-title-boundary-and-public-safe-posture)
- [11. Directory contract](#11-directory-contract)
- [12. Inputs and outputs](#12-inputs-and-outputs)
- [13. Minimal pipeline candidate record](#13-minimal-pipeline-candidate-record)
- [14. Dry-run, tests, fixtures, receipts, and proofs](#14-dry-run-tests-fixtures-receipts-and-proofs)
- [15. Promotion, publication, correction, and rollback](#15-promotion-publication-correction-and-rollback)
- [16. Definition of done](#16-definition-of-done)
- [17. Open questions](#17-open-questions)

---

## 1. Purpose

`pipelines/domains/people-dna-land/` is the executable pipeline lane for People / Genealogy / DNA / Land Ownership transformations.

It supports candidate processing for:

- person assertions, name assertions, person identity candidates, and reviewed person canonicalization inputs;
- life events, residence events, migration events, family groups, genealogy relationships, and relationship hypotheses;
- DNA match evidence, consent grants, revocation receipts, internal DNA kit tokens, and DNA-derived relationship hypotheses;
- land ownership assertions, ownership intervals, deeds, title instruments, assessor records, tax records, legal descriptions, parcel versions, and land instruments;
- public-safe, release-reviewed, evidence-backed derivatives that do not expose living persons, DNA, private person-parcel joins, exact burial coordinates, raw kit/vendor identifiers, or title/boundary overclaims;
- catalog, graph, Evidence Drawer, Focus Mode, and correction/rollback handoff packages.

This directory implements or will implement the **how** of People/DNA/Land processing. It does not define object meaning, schemas, policy, consent authority, source descriptors, legal title truth, genealogy truth, DNA relationship truth, lifecycle storage, catalog truth, or release approval.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/people-dna-land/`? | The requested path follows the visible People/DNA/Land domain segment used in docs. | CONFIRMED requested path; concrete executable behavior NEEDS VERIFICATION |
| What about `people` vs `people-dna-land`? | Domain docs record a segment-name conflict: Directory Rules/docs use `people-dna-land`, while some Atlas/schema crosswalks use `people`. | CONFLICTED / NEEDS ADR |
| Where do declarative specs live? | `pipeline_specs/people-dna-land/` or accepted spec home; `pipeline_specs/people/` is only a conflict/alias candidate until ADR resolution. | NEEDS VERIFICATION |
| Where do source fetchers live? | `connectors/<source>`, not here. | CONFIRMED separation |
| Where do schemas live? | `schemas/contracts/v1/domains/people-dna-land/`, `schemas/contracts/v1/people/`, or accepted ADR path. | CONFLICTED / NEEDS VERIFICATION |
| Where does policy live? | `policy/domains/people-dna-land/`, `policy/sensitivity/people-dna-land/`, `policy/consent/people-dna-land/`, or accepted ADR path. | PROPOSED / NEEDS VERIFICATION |
| Where do outputs live? | Lifecycle homes under `data/`, not beside pipeline code. | CONFIRMED lifecycle posture |
| Can this lane publish? | No. It may prepare candidates and release handoffs only through governed workflow. | CONFIRMED doctrine posture |
| Can this lane decide legal title, biological relationship truth, or living-person public disclosure? | No. It may preserve evidence-bound assertions, consent state, review state, and policy outcomes only. | CONFIRMED doctrine posture |

> [!IMPORTANT]
> People/DNA/Land pipeline code is subordinate to source descriptors, source roles, rights, consent grants, revocation receipts, EvidenceBundle closure, sensitivity transforms, review records, policy decisions, release manifests, correction notices, and rollback cards. A successful run is not public release and never authorizes living-person, DNA, legal-title, or private person-parcel exposure.

[⬆ Back to top](#top)

---

## 3. Sensitivity and consent boundary

This lane is deny-by-default for high-consequence personal, genetic, and land-interest outputs.

A pipeline must fail closed when it cannot prove safe handling for:

- living-person fields;
- DNA/genomic evidence;
- raw kit IDs, vendor identifiers, segment data, triangulation details, or match lists;
- relationship hypotheses involving living people or DNA-derived evidence;
- consent grants, consent scope, retention scope, revocation receipts, and dereference-time enforcement;
- private person-parcel joins;
- exact burial coordinates or culturally sensitive family/place context;
- assessor/tax records that could be mistaken for title truth;
- parcel geometry that could be mistaken for title-boundary proof;
- land-instrument interpretation that could be mistaken for legal advice or legal determination.

Allowed behavior:

```text
Admitted source -> assertion candidate -> consent/rights/sensitivity validation -> evidence closure -> restricted or public-safe derivative after release
```

Disallowed behavior:

```text
DNA match -> public relationship truth
Assessor record -> title truth
Parcel geometry -> boundary proof
Living-person assertion -> public profile
Generated summary -> evidence or legal/genealogy determination
Revoked consent -> continued release eligibility
```

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable People/DNA/Land-domain processing.

Appropriate contents include:

- fixture-only dry-run entrypoints with synthetic/redacted data only;
- person-assertion, name-assertion, event, residence, migration, and relationship candidate builders;
- land-instrument, assessor, tax, parcel-version, legal-description, and ownership-interval normalizers;
- consent-grant and revocation-receipt enforcement helpers, if not centralized elsewhere;
- DNA evidence tokenization and redaction helpers that never expose raw kit/vendor identifiers;
- assertion-first validators for person, genealogy, DNA, and land claims;
- title-boundary anti-collapse validators;
- living-person, DNA, consent, and private person-parcel denial validators;
- quarantine routing helpers for unresolved, sensitive, revoked, over-precise, or unreviewed material;
- catalog/triplet handoff helpers, if not centralized in `pipelines/catalog/`;
- receipt emitters, if not shared;
- thin adapters that read governed lifecycle inputs, not live source systems.

A good placement test:

> If the code transforms People/DNA/Land lifecycle inputs into assertion candidates, processed restricted records, consent-checked handoffs, restricted catalog/triplet candidates, receipts, or review handoffs, it may belong here. If it fetches source data, defines meaning, defines schema, encodes policy, stores lifecycle data, approves release, decides legal title, or publishes living-person/DNA claims, it belongs somewhere else — or nowhere in KFM.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Source fetchers / connectors | `connectors/<source>` |
| Source catalog profiles | `docs/sources/catalog/...` |
| Source descriptors / source registry entries | `data/registry/sources/people-dna-land/` or approved registry home |
| Domain architecture / doctrine | `docs/domains/people-dna-land/...` |
| Object meaning contracts | `contracts/domains/people-dna-land/`, `contracts/people/`, or accepted ADR home |
| JSON Schemas | `schemas/contracts/v1/domains/people-dna-land/`, `schemas/contracts/v1/people/`, or accepted ADR home |
| Policy, sensitivity, consent, retention, release rules | `policy/domains/people-dna-land/`, `policy/sensitivity/...`, `policy/consent/...`, `policy/rights/`, `policy/release/` |
| Declarative run specs | `pipeline_specs/people-dna-land/...` or accepted spec home |
| Fixtures | `fixtures/domains/people-dna-land/` or accepted fixture home |
| Tests | `tests/pipelines/domains/people-dna-land/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet, or published outputs | `data/...` lifecycle homes |
| Receipts and proofs | `data/receipts/...`, `data/proofs/...` |
| Release decisions | `release/candidates/people-dna-land/`, `release/manifests/people-dna-land/`, `release/rollback_cards/`, `release/correction_notices/` |
| Public API or map code | `apps/governed-api/`, `apps/explorer-web/`, `packages/ui/`, `packages/maplibre-runtime/` |
| Legal advice, title determinations, boundary determinations, genealogical truth declarations, relationship truth declarations, or public DNA/living-person disclosure decisions | Outside this executable pipeline lane; governed review/release may approve only bounded public-safe artifacts |
| Raw DNA kit IDs, vendor IDs, match lists, segment details, exact burial coordinates, or real living-person fixture examples | Not in this README or fixture examples; use restricted lifecycle/proof homes with consent and review controls only |

> [!WARNING]
> The previous scaffold wording allowed “docs, contracts, schemas, policies, fixtures, tests, packages, pipelines, registries, or data lifecycle artifacts” here. This README narrows the boundary: **only executable People/DNA/Land pipeline logic belongs here.** The other responsibility roots remain separate authority surfaces.

[⬆ Back to top](#top)

---

## 6. Pipeline scope

People/DNA/Land pipeline work may include these governed processing responsibilities:

| Scope area | Pipeline responsibility | Publication posture |
|---|---|---|
| Person assertions | Normalize evidence-bound person claims. | Living-person public release denied by default. |
| Identity candidates | Build pre-review identity groupings. | Candidate only; not canonical truth. |
| Genealogy relationships | Normalize relationship assertions and hypotheses. | Hypothesis until review; DNA-derived claims restricted. |
| Life/residence/migration events | Normalize event claims with source, time, place, uncertainty, and evidence. | Public release depends on living-person and sensitivity gates. |
| DNA evidence | Tokenize and route restricted DNA evidence and consent state. | Raw kit/vendor/segment details never public. |
| Consent and revocation | Enforce consent scope, purpose, retention, and revocation. | Revocation blocks dereference/release where applicable. |
| Land instruments | Normalize deeds, title instruments, liens, easements, leases, mineral/water/access records. | Evidence-bound, not legal advice or title determination. |
| Assessor/tax records | Normalize administrative property records. | Not title truth. |
| Parcels/legal descriptions | Normalize parcel versions and descriptions with temporal scope. | Geometry is not title-boundary proof. |
| Ownership intervals | Build evidence-bound ownership assertions. | Review, evidence, and title-boundary anti-collapse required. |
| Person-parcel joins | Prepare restricted relationship candidates. | Private person-parcel joins denied from public release by default. |
| Catalog/triplet handoff | Prepare restricted or public-safe catalog/graph candidates after evidence closure. | Graph projection does not replace canonical review state. |

[⬆ Back to top](#top)

---

## 7. Source-family posture

People/DNA/Land pipeline code may consume only admitted or fixture-bound source material.

Candidate source families may include, subject to source descriptors, rights, consent, sensitivity, and steward review:

- vital, cemetery, obituary, church, school, military, census, directory, court, probate, and immigration/naturalization records;
- GEDCOM, GEDZip, and tree-overlay material;
- DNA vendor match exports, segment files, triangulation notes, and DNA-derived relationship hints only through restricted consent/tokenization gates;
- patents, deeds, mortgages, liens, easements, leases, mineral/water/access instruments, probate land records, and other land instruments;
- assessor, tax-roll, parcel, legal description, plat, survey, PLSS, subdivision, and derived geometry sources;
- settlements, roads, archaeology, hydrology, soil, agriculture, hazards, spatial foundation, and frontier-matrix context through governed joins;
- local upload or steward-curated material only through source-descriptor, rights, sensitivity, consent, and review gates.

This README does not activate any source. Each source family requires SourceDescriptor coverage, source role, rights posture, sensitivity classification, consent posture where applicable, attribution, fixtures, validation, and review routing before use.

[⬆ Back to top](#top)

---

## 8. Lifecycle contract

Every People/DNA/Land pipeline must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal People/DNA/Land pipeline stance:

1. **Read** approved synthetic/redacted fixtures, immutable raw captures, work candidates, quarantine inputs in remediation mode, or prior processed baselines.
2. **Normalize** into work candidates with source role, rights, temporal scope, spatial scope, assertion status, consent state, sensitivity class, evidence references, and public-safe transform posture.
3. **Quarantine** unresolved rights, missing consent, revoked consent, living-person exposure, raw DNA identifiers, private person-parcel joins, title-boundary collapse, schema drift, sensitivity risk, over-precise geometry, or validation failure.
4. **Promote to processed** only after validation, policy, consent where applicable, evidence, sensitivity/public-safe transform, review, and reviewer gates appropriate to significance.
5. **Prepare catalog/triplet handoffs** only after processed-state and evidence closure, and only with sensitivity-safe payloads.
6. **Publish** only through release decisions, public-safe artifacts, rollback targets, and correction paths.

Do not treat a move from one lifecycle folder to another as promotion. Promotion is a governed state transition with receipts and review evidence.

[⬆ Back to top](#top)

---

## 9. Required gates

Every People/DNA/Land pipeline run must check or explicitly fail closed on:

1. **Source descriptor gate** — every input has stable source identity, role, cadence, rights, and sensitivity posture.
2. **Source-role gate** — assertion, administrative, legal-instrument, DNA-evidence, aggregate, candidate, synthetic, and context records are not silently collapsed.
3. **Living-person gate** — living-person fields and joins are denied from public release unless explicit policy approval and lawful/public-safe basis close.
4. **DNA/genomic gate** — DNA evidence, raw kit/vendor IDs, segment data, triangulation data, and DNA-derived relationship hypotheses are restricted by default.
5. **Consent gate** — consent scope, purpose, retention, revocation, and dereference-time enforcement must close before use.
6. **Revocation gate** — revoked consent blocks downstream dereference, reuse, and release where applicable.
7. **Person-parcel join gate** — private person-parcel joins fail closed by default.
8. **Title-boundary gate** — assessor/tax records are not title truth, and parcel geometry is not title-boundary proof.
9. **Relationship hypothesis gate** — relationship hypotheses remain hypotheses unless evidence and review close; generated language cannot promote them.
10. **Rights gate** — unknown or restrictive license, permission, attribution, privacy, or redistribution terms block public release.
11. **Sensitivity gate** — exact burial coordinates, cultural/family sensitivity, living-person, DNA, private land-interest, and identity-resolution risks fail closed.
12. **Public-safe transform gate** — public products require approved redaction, aggregation, pseudonymization, delay, restriction, or denial decisions with receipts.
13. **Temporal gate** — source time, event time, valid time, assertion time, consent time, revocation time, processing time, catalog time, and release time remain distinct.
14. **Spatial gate** — place, parcel, geometry, legal-description, and public-safe spatial transforms remain distinct.
15. **Schema gate** — candidate and processed records match approved schemas.
16. **Contract gate** — object meanings match People/DNA/Land contracts and do not invent new semantics silently.
17. **Evidence gate** — claim-bearing outputs resolve EvidenceBundle support or abstain.
18. **Policy gate** — policy decisions are finite and recorded; no silent allow.
19. **Validation gate** — validators exercise pass, fail, restrict, abstain, deny, and error paths, not only success.
20. **Receipt gate** — every run records input refs, versions, parameters, transforms, consent refs, hashes, output refs, and outcomes.
21. **No-direct-publish gate** — no writes to public UI, public API, or `data/published/` without release workflow authority.
22. **Catalog/triplet gate** — catalog and graph projections preserve provenance and do not replace canonical records or review state.
23. **Release gate** — public release requires ReleaseManifest, rollback target, correction path, and review state.

[⬆ Back to top](#top)

---

## 10. Assertion-first, title-boundary, and public-safe posture

People/DNA/Land is fail-closed wherever output could expose living persons, DNA, private family relationships, private land interests, or legal/title overclaims.

Default posture:

- person records are assertion-first and evidence-bound;
- identity candidates are not canonical persons;
- relationship hypotheses are not relationship truth;
- DNA evidence is restricted and consent-scoped;
- assessor and tax records are administrative records, not title truth;
- parcel geometry is not title-boundary proof;
- land instruments are evidence, not legal advice;
- public products must preserve source role, time, method, uncertainty, consent, policy, and EvidenceBundle support;
- generated summaries cannot replace evidence, consent, revocation state, title review, steward review, policy, or release state;
- outputs that could imply unsupported living-person facts, DNA relationships, title ownership, boundary proof, private person-parcel linkage, or legal determination must abstain, deny, quarantine, or require reviewer handoff.

[⬆ Back to top](#top)

---

## 11. Directory contract

Recommended shape:

```text
pipelines/domains/people-dna-land/
├── README.md                         # this file
├── PIPELINE_CONTRACT.md              # PROPOSED: People/DNA/Land execution contract
├── run_dry_fixture.py                # PROPOSED if repo Python convention is accepted
├── normalize_person_assertion.py     # PROPOSED
├── normalize_life_event.py           # PROPOSED
├── normalize_relationship_assertion.py # PROPOSED
├── tokenize_dna_evidence.py          # PROPOSED; no raw kit/vendor IDs in logs
├── enforce_consent.py                # PROPOSED; may belong in shared policy tools if reused
├── normalize_land_instrument.py      # PROPOSED
├── normalize_assessor_record.py      # PROPOSED
├── normalize_parcel_version.py       # PROPOSED
├── build_ownership_interval.py       # PROPOSED
├── validate_living_person_boundary.py # PROPOSED
├── validate_dna_denial.py            # PROPOSED
├── validate_title_boundary.py        # PROPOSED
├── apply_public_safe_transform.py    # PROPOSED; may belong in shared tools if reused
├── build_catalog_handoff.py          # PROPOSED if not centralized in pipelines/catalog/
├── validate_people_dna_land_candidate.py # PROPOSED wrapper if not centralized in tools/
├── emit_receipt.py                   # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/people-dna-land/
├── README.md                         # PROPOSED / NEEDS VERIFICATION
├── person_assertion_dry_run.yaml     # PROPOSED
├── relationship_hypothesis_dry_run.yaml # PROPOSED
├── dna_consent_dry_run.yaml          # PROPOSED
├── land_instrument_dry_run.yaml      # PROPOSED
├── title_boundary_checks.yaml        # PROPOSED
├── public_safe_transform.yaml        # PROPOSED; policy ownership must be resolved
└── catalog_handoff.yaml              # PROPOSED
```

Generated outputs must not be written beside the code that generated them. Use lifecycle homes under `data/`, proof homes under `data/proofs/`, receipt homes under `data/receipts/`, and release homes under `release/`.

[⬆ Back to top](#top)

---

## 12. Inputs and outputs

### Inputs

| Input class | Allowed source | Required condition |
|---|---|---|
| No-network fixture | `fixtures/domains/people-dna-land/` or accepted fixture home | Synthetic, redacted, consent-scoped; no real raw DNA IDs, living-person examples, or private joins. |
| Raw capture | `data/raw/people-dna-land/<source_id>/<run_id>/` | Immutable source-edge capture with source descriptor, checksums, rights, and sensitivity posture. |
| Work candidate | `data/work/people-dna-land/<run_id>/` | Candidate-only; not public. |
| Quarantine input | `data/quarantine/people-dna-land/<reason>/<run_id>/` | Audit/remediation mode only. |
| Prior processed baseline | `data/processed/people-dna-land/<dataset_id>/<version>/` | Validated restricted baseline for diff/supersession. |
| Source registry / descriptor | `data/registry/sources/people-dna-land/`, `docs/sources/catalog/...` | Source role, rights, cadence, attribution, sensitivity, consent posture. |
| Consent / revocation state | approved policy/proof/receipt home | Required before DNA/living-person processing where applicable. |
| Cross-lane context | Settlements, Roads/Rail, Archaeology, Hydrology, Soil, Agriculture, Hazards, Spatial Foundation, Frontier Matrix, or other lifecycle homes | Must preserve source role and never weaken People/DNA/Land controls. |
| Policy / schema / contract refs | `policy/`, `schemas/`, `contracts/` | Referenced by validators, not stored here. |

### Outputs

| Output class | Correct home | Notes |
|---|---|---|
| Work candidate | `data/work/people-dna-land/<run_id>/` | Candidate only. |
| Quarantine record | `data/quarantine/people-dna-land/<reason>/<run_id>/` | Failed, restricted, revoked, unresolved, or unsafe material. |
| Processed restricted dataset version | `data/processed/people-dna-land/<dataset_id>/<version>/` | Validated/restricted; not automatically public. |
| Public-safe catalog candidate | `data/catalog/domain/people-dna-land/...` or approved catalog home | After processed-state, transform, consent, and evidence gates. |
| Triplet / graph delta | `data/triplets/people-dna-land/...` or approved graph-delta home | Projection; does not replace canonical truth or review state. |
| Consent / revocation / redaction receipt | `data/receipts/...` or approved receipt/proof home | Required before any public-safe derivative where applicable. |
| Run receipt | `data/receipts/pipeline/...` | Process memory, not release proof. |
| Evidence / validation proof | `data/proofs/...` | EvidenceBundle, validation reports, proof packs. |
| Release handoff | `release/candidates/people-dna-land/...` | Only through release workflow. |

[⬆ Back to top](#top)

---

## 13. Minimal pipeline candidate record

The final schema is not defined here. This example shows the minimum information a People/DNA/Land pipeline candidate should preserve.

```yaml
schema_version: kfm.people_dna_land_pipeline_candidate.v1
candidate_id: pdl_<object_family>_<run_id>_<hash>
pipeline_id: domains.people-dna-land
run_id: run_YYYYMMDDThhmmssZ
status: WORK_CANDIDATE
object_family: <person_assertion|name_assertion|life_event|relationship_assertion|relationship_hypothesis|dna_match_evidence|consent_grant|revocation_receipt|land_instrument|assessor_record|tax_record|parcel_version|ownership_interval|...>
source_inputs:
  - source_id: src_people_dna_land_example
    source_role: <assertion|administrative|legal_instrument|dna_evidence|context|aggregate|candidate|synthetic|restricted>
    lifecycle_ref: data/raw/people-dna-land/<source_id>/<run_id>/
    input_hash: sha256:<hash>
    rights_state: needs_review
anti_collapse:
  assessor_record_is_title_truth: false
  parcel_geometry_is_boundary_proof: false
  dna_match_is_relationship_truth: false
  relationship_hypothesis_is_confirmed: false
  generated_summary_is_evidence: false
consent:
  required: unknown
  consent_grant_ref: null
  revocation_receipt_ref: null
  dereference_allowed: false
spatial_scope:
  place_ref: restricted_or_public_safe_ref
  parcel_ref: restricted_or_public_safe_ref
  public_precision: denied_until_public_safe_transform
temporal_scope:
  source_time: null
  event_time: null
  valid_start: null
  valid_end: null
  consent_time: null
  revocation_time: null
  retrieved_at: YYYY-MM-DDThh:mm:ssZ
  processed_at: YYYY-MM-DDThh:mm:ssZ
method:
  transform_family: people_dna_land_candidate_normalization
  algorithm_version: <version>
  parameter_hash: sha256:<hash>
sensitivity:
  living_person_risk: needs_review
  dna_risk: needs_review
  person_parcel_join_risk: needs_review
  burial_or_cultural_sensitivity: needs_review
  public_release_default: DENY
policy:
  outcome: ABSTAIN
  reason_code: CONSENT_SENSITIVITY_OR_EVIDENCE_NOT_RESOLVED
evidence:
  evidence_bundle_ref: null
  citation_state: ABSTAIN
outputs:
  candidate_record: data/work/people-dna-land/run_YYYYMMDDThhmmssZ/candidate.yml
  receipt: data/receipts/pipeline/people-dna-land/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 14. Dry-run, tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic/redacted, consent-scoped, and no-network** until source activation, rights review, consent review, sensitivity review, title-boundary review, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/people-dna-land/
├── test_no_network_dry_run.py                    # PROPOSED
├── test_no_real_living_person_fixture.py         # PROPOSED
├── test_no_raw_dna_ids_in_logs.py                # PROPOSED
├── test_source_role_required.py                  # PROPOSED
├── test_rights_unknown_denied.py                 # PROPOSED
├── test_living_person_public_denied.py           # PROPOSED
├── test_dna_relationship_public_denied.py        # PROPOSED
├── test_revoked_consent_blocks_dereference.py    # PROPOSED
├── test_person_parcel_join_quarantines.py        # PROPOSED
├── test_assessor_not_title_truth.py              # PROPOSED
├── test_parcel_geometry_not_boundary_proof.py    # PROPOSED
├── test_missing_evidence_abstains.py             # PROPOSED
├── test_receipt_hashes.py                        # PROPOSED
└── test_no_direct_publish.py                     # PROPOSED
```

A dry run should prove:

- fixtures load without network access;
- fixtures are synthetic/redacted and contain no real living-person, private DNA, raw kit/vendor, or private person-parcel examples;
- every input has source identity and source role;
- unknown rights produce `ABSTAIN`, `DENY`, or quarantine;
- missing, expired, out-of-scope, or revoked consent blocks downstream use where applicable;
- DNA-derived relationship hypotheses remain restricted;
- assessor/tax records cannot become title truth;
- parcel geometry cannot become title-boundary proof;
- private person-parcel joins quarantine by default;
- missing EvidenceBundle support produces `ABSTAIN`;
- invalid records fail validation;
- receipts include input hashes, method hashes, consent refs, revocation refs, transform refs, output refs, and outcomes;
- no outputs are written to public UI, public API, `data/published/`, or release manifests by default.

[⬆ Back to top](#top)

---

## 15. Promotion, publication, correction, and rollback

People/DNA/Land pipelines may prepare candidates. They do not publish.

Required promotion chain:

```text
people / dna / land source or work input
  -> assertion candidate
  -> validation report
  -> policy decision
  -> consent / revocation check where required
  -> public-safe transform receipt where required
  -> EvidenceBundle closure
  -> processed restricted dataset version
  -> catalog / triplet candidate
  -> release candidate
  -> ReleaseManifest
  -> RollbackCard
  -> public-safe artifact
```

Correction and rollback posture:

- denied, abstained, errored, revoked, restricted, and quarantined runs remain auditable;
- candidate rollback preserves receipts and proof state;
- processed versions are superseded by governed state transition, not hidden overwrite;
- consent revocation invalidates downstream dereference/release where applicable;
- public artifact rollback is owned by `release/`, not by this directory;
- correction notices must point back to source, evidence, consent/revocation state, title-boundary checks, validation, catalog, release, and rollback state.

[⬆ Back to top](#top)

---

## 16. Definition of done

This README is done when it:

- replaces the greenfield scaffold with a usable People/DNA/Land pipeline contract;
- identifies this directory as executable pipeline logic only;
- corrects the boundary so docs, schemas, contracts, policy, fixtures, tests, data, registries, receipts, proofs, and release decisions do not live here;
- preserves assertion-first, consent, revocation, living-person, DNA, title-boundary, person-parcel, evidence, policy, lifecycle, catalog/triplet, release, correction, and rollback boundaries;
- denies direct publication and living-person/DNA/private-land exposure;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable People/DNA/Land pipeline implementation is done only when it has:

- owners and review burden;
- source-descriptor coverage;
- synthetic/redacted no-network fixtures;
- schema-backed candidates;
- People/DNA/Land contract conformance;
- rights, sensitivity, consent, revocation, title-boundary, temporal, spatial, and evidence tests;
- deterministic receipts;
- no-direct-publish tests;
- CI coverage;
- steward-review handoff;
- release, correction, and rollback documentation.

[⬆ Back to top](#top)

---

## 17. Open questions

| ID | Question | Status |
|---|---|---|
| `PDL-PIPE-001` | Which child modules should be implemented first: person assertions, land instruments, consent enforcement, DNA tokenization, title-boundary checks, or catalog handoff? | NEEDS VERIFICATION |
| `PDL-PIPE-002` | Which segment is canonical for contracts, schemas, specs, policy, and data lanes: `people-dna-land` or `people`? | CONFLICTED / NEEDS ADR |
| `PDL-PIPE-003` | Which object family owns consent, revocation, redaction, and public-safe transform receipts if they become reusable outside this lane? | PROPOSED / NEEDS ADR |
| `PDL-PIPE-004` | Which source descriptors are first-wave approved for fixture-only dry runs? | NEEDS VERIFICATION |
| `PDL-PIPE-005` | Which CI job owns People/DNA/Land pipeline invariant tests? | UNKNOWN |
| `PDL-PIPE-006` | Should catalog handoff logic live here or in centralized `pipelines/catalog/` with People/DNA/Land adapters? | NEEDS VERIFICATION |
| `PDL-PIPE-007` | How should consent revocation invalidate prior processed records, catalog projections, graph projections, and released derivatives? | NEEDS VERIFICATION |
| `PDL-PIPE-008` | Which public-safe map/API products are allowed after review and release, and at what redaction/generalization level? | NEEDS VERIFICATION |
| `PDL-PIPE-009` | How should cross-lane joins with Settlements, Roads/Rail, Archaeology, Hydrology, Soil, Agriculture, Hazards, Spatial Foundation, or Frontier Matrix be denied, restricted, or generalized? | NEEDS VERIFICATION |

---

## Maintainer note

Start with synthetic/redacted fixture-only dry runs and negative tests. Do not add live source fetching, raw DNA identifiers, real living-person fixture examples, private person-parcel joins, legal-title assertions, public map layers, release handoff automation, or direct API payload generation until source roles, rights, consent/revocation enforcement, title-boundary checks, public-safe transforms, evidence closure, and rollback are proven.
