<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-geology-mineral-occurrences-readme
title: Geology Mineral Occurrences Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <geology-pipeline-owner>
  - <geology-domain-steward>
  - <natural-resources-steward>
  - <mineral-occurrence-steward>
  - <usgs-source-steward>
  - <kgs-source-steward>
  - <evidence-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: restricted-by-default-for-exact-resource-location-context
path: pipelines/domains/geology/mineral_occurrences/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - pipelines/domains/geology/README.md
  - pipelines/domains/geology/well_logs/README.md
  - docs/domains/geology/README.md
  - docs/domains/geology/sublanes/natural_resources.md
  - docs/domains/geology/POLICY.md
  - docs/domains/geology/PRESERVATION_MATRIX.md
  - docs/sources/catalog/usgs/usgs-mrds.md
  - docs/sources/catalog/kansas/ksgs.md
  - pipeline_specs/geology/mineral_occurrences.yaml
  - contracts/domains/geology/
  - schemas/contracts/v1/domains/geology/
  - policy/domains/geology/
  - policy/sensitivity/geology/
  - data/raw/geology/
  - data/work/geology/
  - data/quarantine/geology/
  - data/processed/geology/
  - data/catalog/domain/geology/
  - data/triplets/geology/
  - data/published/layers/geology/
  - data/registry/sources/geology/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/geology/
  - release/manifests/geology/
tags:
  - kfm
  - pipelines
  - domains
  - geology
  - natural-resources
  - mineral-occurrences
  - resource-deposits
  - resource-estimates
  - extraction-context
  - mrds
  - kgs
  - critical-minerals
  - source-role
  - evidence
  - policy
  - restricted
  - governance
notes:
  - "This README fills the blank pipelines/domains/geology/mineral_occurrences path as a nested executable Geology mineral-occurrence sublane."
  - "Mineral-occurrence pipeline logic is executable implementation support only; it does not own source descriptors, source catalog profiles, connectors, schemas, policy, lifecycle data, catalog truth, resource decisions, reserve decisions, extraction rights, permits, titles, or release decisions."
  - "Occurrence, deposit, estimate, extraction site, production, permit, lease, title, and economic-resource claims are distinct and must not be promoted silently."
  - "MRDS-like records are compiled administrative/historical carriers unless a specific first-party observation is resolved through evidence and source attribution."
  - "Exact resource-location, critical-mineral, operator-private, land-rights, infrastructure-adjacent, and unresolved-rights material fails closed by default."
  - "Concrete executable behavior, source activation, schedules, CI coverage, schema paths, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Geology Mineral Occurrences Pipeline

> Executable Geology sublane for transforming admitted mineral-occurrence, deposit, historical extraction, resource-estimate, and related natural-resource source material into governed candidates, quarantine records, normalized records, catalog/triplet handoffs, receipts, and release-review packages — while preserving source role, claim strength, location sensitivity, evidence, rights, correction path, and rollback boundaries.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-geology%20mineral%20occurrences-2e7d32)
![authority](https://img.shields.io/badge/authority-executable%20logic-0a7ea4)
![anti-collapse](https://img.shields.io/badge/occurrence%20%E2%89%A0%20deposit%20%E2%89%A0%20economic%20resource-d62728)
![sensitivity](https://img.shields.io/badge/exact%20locations-restricted%20by%20default-d62728)
![publication](https://img.shields.io/badge/publication-release%20gated-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/geology/mineral_occurrences/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Geology and Natural Resources  
**Sublane:** Mineral occurrences / natural-resource evidence  
**Placement posture:** nested executable sublane under `pipelines/domains/geology/`; concrete executable behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Public posture:** no direct publication; exact resource-location and critical-mineral context is restricted/generalized by default and requires EvidenceBundle, source-role, sensitivity, policy, catalog/triplet, release, correction, and rollback closure

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Mineral-occurrence anti-collapse rules](#3-mineral-occurrence-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Mineral-occurrence scope](#6-mineral-occurrence-scope)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Minimal mineral-occurrence candidate record](#11-minimal-mineral-occurrence-candidate-record)
- [12. Tests, fixtures, receipts, and proofs](#12-tests-fixtures-receipts-and-proofs)
- [13. Promotion, publication, correction, and rollback](#13-promotion-publication-correction-and-rollback)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipelines/domains/geology/mineral_occurrences/` is the executable sublane for Geology mineral-occurrence and natural-resource evidence processing.

It supports candidate processing for:

- `Mineral Occurrence` records;
- `Resource Deposit` characterization candidates;
- `ResourceEstimate` document references, without promoting estimates into economic-resource truth;
- historical extraction-site references and mining-record context where admitted;
- commodity, deposit-type, host-rock, geologic setting, source-vintage, and attribution fields;
- USGS MRDS-like compiled records, KGS/state geological survey records, academic publications, legacy mining records, and other admitted source families;
- geochemistry and geophysical context links only when evidence and method receipts are present;
- generalized public-safe summaries such as county or grid summaries where release policy permits;
- quarantine records for missing source descriptor, unresolved attribution, weak claim strength, source-role collapse, location uncertainty, exact-location sensitivity, rights uncertainty, critical-mineral exposure, schema drift, or validation failure;
- validation, catalog, triplet, EvidenceBundle, release-review, correction, and rollback handoff packages.

This directory implements or will implement the **how** of mineral-occurrence processing. It does not fetch source data, define Geology object meaning, define schemas, encode policy, store lifecycle data, decide release, certify deposits, certify reserves/resources, prove economic extractability, prove ownership/lease/title/permit claims, expose exact sensitive locations, or create public map products by itself.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/geology/`? | Geology is a domain lane under the domain-pipeline umbrella. | CONFIRMED path responsibility pattern; behavior NEEDS VERIFICATION |
| Why `mineral_occurrences/`? | This is a narrow executable sublane for occurrence/deposit/estimate evidence processing. | PROPOSED / NEEDS VERIFICATION |
| Is this a connector? | No. Source fetching belongs in `connectors/<source>` or an accepted source-edge home. | CONFIRMED separation |
| Does this own natural-resources doctrine? | No. Human-facing doctrine remains in `docs/domains/geology/sublanes/natural_resources.md`; object meaning belongs in contracts. | CONFIRMED doc separation |
| Does this own source profiles? | No. MRDS/KGS/source profiles remain under `docs/sources/catalog/...`; SourceDescriptors remain in registry homes. | CONFIRMED source separation |
| Can this sublane publish? | No. It may prepare candidates and release handoffs only through governed workflow. | CONFIRMED doctrine posture |

> [!IMPORTANT]
> Mineral-occurrence output is not public release, not deposit certainty, not economic-resource truth, not reserve truth, not extraction-rights truth, and not a public exact-location layer. It is source-bound geology evidence that must carry claim strength, source role, attribution, rights, sensitivity, EvidenceBundle, policy, correction, and rollback refs.

[⬆ Back to top](#top)

---

## 3. Mineral-occurrence anti-collapse rules

Mineral-occurrence processing must preserve source role, claim strength, attribution, and release state.

Disallowed collapses:

```text
occurrence -> deposit
deposit -> economic resource
resource estimate -> reserve certification
historical extraction site -> active operation
MRDS compiled record -> current first-hand observation
lease / parcel / operator relation -> deposit proof
permit or filing -> mineralization proof
geochemistry sample -> deposit without interpretation receipt
geophysical anomaly -> occurrence without evidence link
commodity mention -> verified mineral occurrence
exact resource location -> public point
AI summary -> EvidenceBundle
pipeline run -> release approval
```

Required distinctions:

- source identity, source role, source product, attribution chain, source vintage, commodity, claim type, confidence, location precision, and rights posture are explicit;
- occurrence, deposit, estimate, extraction site, production, permit, lease, title, operator, and generated-summary claims remain distinct;
- compiled/historical records carry source-vintage and attribution caveats;
- exact resource-location, critical-mineral, operator-private, infrastructure-adjacent, and land-rights joins fail closed until policy permits generalized release;
- every public claim resolves evidence or abstains;
- publication requires public-safe transforms, release review, correction path, and rollback target.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable Geology mineral-occurrence processing.

Appropriate contents include:

- fixture-only dry-run entrypoints;
- mineral-occurrence source-candidate normalizers;
- commodity, deposit-type, host-rock, source-vintage, and attribution normalizers;
- occurrence/deposit/estimate/extraction-site claim-type validators;
- MRDS-like compiled-record caveat validators;
- exact-location sensitivity and public-safe generalization preflight helpers;
- critical-minerals and infrastructure-adjacent exposure preflight helpers;
- geochemistry/geophysics context handoff validators that require method/evidence receipts;
- source-role anti-collapse validators for KGS, MRDS, KCC, permits, leases, and production-adjacent records;
- quarantine routing helpers for missing descriptor, unresolved attribution, rights uncertainty, source-role collapse, sensitivity failure, evidence gaps, or schema failures;
- receipt emitters, if not shared;
- handoff helpers for validation, catalog, triplet, and release workflow.

A good placement test:

> If the code transforms admitted mineral-occurrence lifecycle inputs into Geology occurrence/deposit/estimate candidates, quarantine records, validation handoffs, receipts, or downstream handoff packages, it may belong here. If it fetches source data, defines schemas, stores lifecycle data, decides policy, owns source profiles, writes catalog records directly, approves release, or creates public API/map payloads, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Source fetchers / connectors | `connectors/usgs/`, `connectors/kansas/kgs/`, or accepted connector home |
| Source catalog profiles | `docs/sources/catalog/usgs/usgs-mrds.md`, `docs/sources/catalog/kansas/ksgs.md`, or accepted source-profile home |
| Source descriptors / source registry entries | `data/registry/sources/geology/`, `data/registry/sources/usgs/`, or approved registry home |
| Geology doctrine and object meaning | `docs/domains/geology/...`, `contracts/domains/geology/` |
| JSON Schemas | `schemas/contracts/v1/domains/geology/` or accepted schema home |
| Policy, rights, sensitivity, release rules | `policy/...` responsibility roots |
| Declarative run specs | `pipeline_specs/geology/...` |
| Fixtures | `fixtures/domains/geology/mineral_occurrences/` or accepted fixture home |
| Tests | `tests/pipelines/domains/geology/mineral_occurrences/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet, or published outputs | `data/...` lifecycle homes |
| Reserve certification, economic-resource reporting, financing-grade disclosures | Outside KFM claim authority unless separately governed by approved legal/technical review |
| Permits, leases, titles, parcels, ownership, or operator-rights truth | Regulatory, land, legal, and release/policy roots; never this pipeline |
| Active mining operations or safety decisions | Owning regulatory/operational/hazards roots, not this pipeline |
| Public API or map code | `apps/governed-api/`, `apps/explorer-web/`, packages |
| Release decisions and manifests | `release/...` responsibility roots |

[⬆ Back to top](#top)

---

## 6. Mineral-occurrence scope

| Scope area | Pipeline responsibility | Failure behavior |
|---|---|---|
| Source identity | Preserve source id, descriptor refs, rights, source role, source product, attribution, and vintage. | Quarantine if missing. |
| Claim type | Preserve whether the record asserts occurrence, deposit, estimate, extraction site, or context. | Deny or quarantine on silent promotion. |
| Commodity | Preserve commodity code/name, vocabulary refs, critical-mineral posture, and source caveats. | Restrict or quarantine on ambiguity. |
| Location | Preserve original precision and public-safe transform state. | Restrict or quarantine exact sensitive points. |
| Attribution | Preserve source chain, citation refs, record date, source vintage, and maintenance state. | Abstain or quarantine if unresolved. |
| Cross-lane joins | Preserve regulatory, land, hazards, geochemistry, geophysics, and infrastructure context as context. | Deny if join becomes proof. |
| Evidence | Carry EvidenceBundle refs forward; do not invent support. | Abstain if unresolved. |
| Release handoff | Prepare public-safe candidates only after evidence, policy, and sensitivity closure. | No direct publication. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every Geology mineral-occurrence run must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** approved fixtures, immutable raw captures, work inputs, quarantine inputs in remediation mode, or prior processed occurrence baselines.
2. **Normalize** into Geology work candidates with source role, claim type, commodity refs, attribution refs, source vintage, location precision, sensitivity state, evidence refs, policy refs, and receipt refs.
3. **Quarantine** missing source descriptor, unresolved attribution, missing commodity, weak claim strength, silent occurrence-to-deposit promotion, rights failure, sensitivity failure, evidence gap, schema drift, or validation failure.
4. **Emit receipts** with input refs, source refs, attribution refs, claim-type refs, commodity refs, location-transform refs, validation refs, output refs, and outcomes.
5. **Support promotion** only by feeding downstream validation and review workflows.
6. **Never publish directly.**

Mineral-occurrence processing is a lifecycle transformation. It is not catalog closure, release approval, public artifact creation, reserve certification, or extraction-rights proof by itself.

[⬆ Back to top](#top)

---

## 8. Required gates

Every Geology mineral-occurrence run must check or explicitly fail closed on:

1. **Input lifecycle gate** — input is fixture, raw capture, work input, quarantine-remediation input, or accepted baseline.
2. **Source descriptor gate** — source identity, role, rights, citation, cadence/vintage, and sensitivity posture are known.
3. **Source-role gate** — administrative compilations, observations, candidate claims, interpretations, regulatory records, permits, leases, production records, and generated summaries remain distinct.
4. **Claim-strength gate** — occurrence, deposit, estimate, economic-resource, extraction, and context claims are not silently promoted.
5. **Attribution/vintage gate** — source attribution chain, record vintage, maintenance status, and citation refs are explicit.
6. **Commodity gate** — commodity vocabulary, critical-mineral posture, and source caveats are explicit.
7. **Location sensitivity gate** — exact resource, critical-mineral, operator-private, infrastructure-adjacent, and land-rights-sensitive locations are restricted or generalized unless release policy proves otherwise.
8. **Cross-lane ownership gate** — regulatory, land, hazards, geochemistry, geophysics, infrastructure, and operation context does not become deposit proof or rights proof.
9. **Evidence gate** — claim-bearing downstream candidates can resolve EvidenceBundle support or abstain.
10. **Policy/sensitivity gate** — unresolved rights, controlled joins, exact exposure risk, or public-safe transform gaps fail closed.
11. **Schema/contract gate** — candidates match accepted Geology schema and mineral-occurrence semantics.
12. **Correction/rollback gate** — release-facing handoff includes correction path and rollback target expectations.
13. **No-direct-publish gate** — no writes to public UI, public API, published layers, or release manifests as a pipeline side effect.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/domains/geology/mineral_occurrences/
├── README.md                              # this file
├── MINERAL_OCCURRENCES_PIPELINE_CONTRACT.md # PROPOSED: mineral-occurrence execution contract
├── run_dry_fixture.py                     # PROPOSED synthetic/generalized fixture only
├── normalize_occurrence_candidate.py      # PROPOSED
├── preserve_claim_type.py                 # PROPOSED
├── normalize_commodity_refs.py            # PROPOSED
├── validate_attribution_vintage.py        # PROPOSED
├── validate_claim_strength.py             # PROPOSED
├── validate_source_role.py                # PROPOSED
├── validate_location_sensitivity.py       # PROPOSED
├── validate_cross_lane_ownership.py       # PROPOSED
├── route_quarantine.py                    # PROPOSED
├── emit_receipt.py                        # PROPOSED only if not shared
└── adapters/                              # PROPOSED thin lifecycle adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/geology/mineral_occurrences.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside this code. Use accepted lifecycle homes under `data/work/geology/`, `data/quarantine/geology/`, `data/processed/geology/`, `data/catalog/domain/geology/`, `data/triplets/geology/`, `data/published/layers/geology/`, proof homes under `data/proofs/`, receipt homes under `data/receipts/`, and release homes under `release/`.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Fixture input | `fixtures/domains/geology/mineral_occurrences/` or accepted fixture home | Synthetic, generalized, or redacted. |
| Raw source capture | `data/raw/geology/<source_id>/<run_id>/` | Immutable source-edge capture with descriptor and receipt. |
| Work candidate | `data/work/geology/<run_id>/` | Candidate only. |
| Quarantine record | `data/quarantine/geology/<reason>/<run_id>/` | Failed, restricted, unresolved, or unsafe material. |
| Processed occurrence/deposit record | `data/processed/geology/<dataset_id>/<version>/` | Only after validation and governed promotion. |
| Catalog/triplet handoff | `data/catalog/domain/geology/`, `data/triplets/geology/` | Projection only; not publication. |
| Receipt | `data/receipts/pipeline/geology/mineral_occurrences/<run_id>.yml` or accepted receipt home | Records inputs, claim types, commodities, checks, outputs. |
| Evidence proof | `data/proofs/evidence_bundle/` or accepted proof home | Required for claim-bearing records. |
| Release handoff | `release/candidates/geology/` | Reviewable, release-gated output only. |

[⬆ Back to top](#top)

---

## 11. Minimal mineral-occurrence candidate record

The final schema is not defined here. This example shows the minimum information a Geology mineral-occurrence candidate should preserve.

```yaml
schema_version: kfm.geology_mineral_occurrence_candidate.v1
candidate_id: geology_mineral_occurrence_<source_id>_<record_id>_<claim_type>_<hash>
pipeline_id: domains.geology.mineral_occurrences
run_id: run_YYYYMMDDThhmmssZ
status: WORK_CANDIDATE
object_family: <MineralOccurrence|ResourceDeposit|ResourceEstimate|ExtractionSiteContext>
source:
  source_id: <source_id>
  source_role: <administrative|observed|candidate|authority|interpretation|regulatory|generated_context|synthetic>
  source_product: <mrds|kgs_minerals|state_survey|academic_publication|legacy_mining_record|other>
  lifecycle_ref: data/raw/geology/<source_id>/<run_id>/
  input_hash: sha256:<hash>
  rights_state: needs_review
claim:
  claim_type: <occurrence|deposit|resource_estimate|extraction_context|unknown>
  claim_strength: needs_review
  commodity_refs: []
  deposit_type_ref: null
  attribution_refs: []
  source_vintage: null
location:
  original_location_ref: null
  public_location_ref: null
  precision_class: restricted
  uncertainty_radius: null
  public_safe_transform_ref: null
policy:
  outcome: ABSTAIN
  reason_code: SOURCE_DESCRIPTOR_CLAIM_STRENGTH_POLICY_OR_EVIDENCE_NOT_RESOLVED
evidence:
  evidence_bundle_ref: null
  citation_state: ABSTAIN
anti_collapse:
  occurrence_is_deposit: false
  deposit_is_economic_resource: false
  estimate_is_reserve_certification: false
  regulatory_or_land_record_is_deposit_proof: false
  exact_resource_location_is_public: false
  generated_summary_is_evidence: false
outputs:
  candidate_record: data/work/geology/run_YYYYMMDDThhmmssZ/mineral_occurrence_candidate.yml
  receipt: data/receipts/pipeline/geology/mineral_occurrences/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 12. Tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic/generalized/redacted, and no-network** until source activation, mineral-occurrence spec, evidence, policy, sensitivity, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/geology/mineral_occurrences/
├── test_no_network_dry_run.py              # PROPOSED
├── test_source_descriptor_required.py      # PROPOSED
├── test_claim_type_required.py             # PROPOSED
├── test_occurrence_not_deposit.py          # PROPOSED
├── test_deposit_not_economic_resource.py   # PROPOSED
├── test_estimate_not_reserve_certification.py # PROPOSED
├── test_mrds_not_current_observation.py    # PROPOSED
├── test_land_or_regulatory_record_not_deposit_proof.py # PROPOSED
├── test_exact_location_restricted.py       # PROPOSED
├── test_commodity_refs_required.py         # PROPOSED
├── test_policy_public_safe_required.py     # PROPOSED
├── test_evidence_gap_abstains.py           # PROPOSED
├── test_receipt_hashes.py                  # PROPOSED
└── test_no_direct_publish.py               # PROPOSED
```

A dry run should prove fixtures load without network access, source descriptors are required, claim type is preserved, MRDS-like compiled records do not become current observations, occurrence/deposit/economic-resource claims do not collapse, exact sensitive locations fail closed, receipts are deterministic, and no run writes directly to public UI, public API, catalog store, published layers, or release manifests.

[⬆ Back to top](#top)

---

## 13. Promotion, publication, correction, and rollback

Geology mineral-occurrence pipelines may prepare candidates and handoff packages. They do not publish.

Required chain:

```text
admitted mineral/source capture
  -> mineral-occurrence work candidate
  -> validation report
  -> policy decision
  -> EvidenceBundle closure
  -> processed Mineral Occurrence / Resource Deposit / ResourceEstimate record
  -> catalog / triplet candidate
  -> release candidate
  -> ReleaseManifest
  -> RollbackCard
  -> public-safe artifact
```

Correction and rollback posture:

- denied, abstained, errored, restricted, stale, conflicted, and quarantined mineral-occurrence runs remain auditable;
- receipts preserve source refs, attribution refs, claim-type refs, commodity refs, location-transform refs, evidence refs, source-role refs, policy outcomes, and failure reasons;
- processed versions are produced by governed promotion, not hidden overwrite;
- downstream artifacts are invalidated if source refs, attribution refs, claim-type refs, commodity refs, EvidenceBundle refs, policy refs, source-role refs, location-transform refs, correction refs, or rollback refs drift;
- release rollback is owned by `release/`, not by this directory.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- fills the blank `pipelines/domains/geology/mineral_occurrences/README.md` file;
- identifies this directory as a nested executable Geology mineral-occurrence sublane;
- prevents connector, source-profile, schema, contract, policy, fixture, test, data, proof, catalog, graph, public API, UI, legal/resource decision, and release authority from being placed here;
- preserves mineral occurrence, resource deposit, resource estimate, extraction-context, source-role, claim-strength, attribution, commodity, location sensitivity, evidence, policy, lifecycle, catalog/triplet, release, correction, and rollback boundaries;
- blocks occurrence-as-deposit, deposit-as-economic-resource, estimate-as-reserve-certification, land/regulatory-record-as-deposit-proof, generated-summary-as-evidence, and direct publication writes;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable work in this sublane is done only when it has source-descriptor coverage, synthetic/generalized/redacted no-network fixtures, schema-backed candidates, contract conformance, claim-type/source-role/sensitivity/evidence/policy/no-direct-publish tests, deterministic receipts, CI coverage, steward-review handoff, and release/correction/rollback documentation.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `GEOL-MIN-OCC-001` | Should mineral-occurrence execution remain one sublane, or split into MRDS, KGS minerals, geochemistry references, extraction context, and resource estimates? | NEEDS VERIFICATION / ADR |
| `GEOL-MIN-OCC-002` | Which source-edge jobs own MRDS/KGS/state-survey retrieval before this sublane reads lifecycle inputs? | NEEDS VERIFICATION |
| `GEOL-MIN-OCC-003` | Which schema owns Mineral Occurrence, Resource Deposit, ResourceEstimate, and Extraction Site context candidates? | NEEDS VERIFICATION |
| `GEOL-MIN-OCC-004` | Which first-wave source is approved for fixture-only dry runs: MRDS, KGS, synthetic occurrences, or generalized county summaries? | NEEDS VERIFICATION |
| `GEOL-MIN-OCC-005` | Which CI job owns mineral-occurrence invariant tests? | UNKNOWN |
| `GEOL-MIN-OCC-006` | What public-safe location precision, commodity suppression, and caveat levels are allowed for released mineral-occurrence summaries? | NEEDS VERIFICATION |
| `GEOL-MIN-OCC-007` | Which receipt type owns claim-strength review, attribution/vintage reconciliation, and location generalization? | PROPOSED / NEEDS ADR |

---

## Maintainer note

Start with synthetic/generalized fixture-only dry runs and negative tests. Do not add live source fetching, source-profile editing, schema authority, policy authority, direct catalog writes, public exact-resource layers, release-manifest writes, or generated resource summaries until source roles, claim strength, attribution, EvidenceBundle closure, public-safe transforms, release review, and rollback are proven.
