<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-geology-boreholes-readme
title: Geology Boreholes Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <geology-pipeline-owner>
  - <geology-domain-steward>
  - <boreholes-wells-steward>
  - <well-logs-steward>
  - <hydrology-domain-steward>
  - <people-land-privacy-steward>
  - <evidence-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: restricted-by-default-for-exact-borehole-and-private-well-location-context
path: pipelines/domains/geology/boreholes/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - pipelines/domains/geology/README.md
  - pipelines/domains/geology/well_logs/README.md
  - pipelines/domains/geology/cross_sections/README.md
  - docs/domains/geology/README.md
  - docs/domains/geology/sublanes/boreholes-wells.md
  - docs/domains/geology/sublanes/stratigraphy.md
  - docs/domains/geology/POLICY.md
  - docs/domains/geology/PRESERVATION_MATRIX.md
  - docs/sources/catalog/kansas/ksgs.md
  - docs/sources/catalog/kansas/kcc-oil-gas-reg.md
  - pipeline_specs/geology/boreholes.yaml
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
  - boreholes
  - wells
  - water-wells
  - oil-gas-wells
  - stratigraphic-tests
  - geotechnical-borings
  - core-samples
  - well-logs
  - exact-location-sensitive
  - redaction
  - aggregation
  - evidence
  - policy
  - restricted
  - governance
notes:
  - "This README fills the blank pipelines/domains/geology/boreholes path as a nested executable Geology boreholes sublane."
  - "Borehole pipeline logic is executable implementation support only; it does not own source descriptors, source catalog profiles, connectors, schemas, policy, lifecycle data, catalog truth, well-log truth, stratigraphy truth, hydrology truth, land/privacy truth, or release decisions."
  - "Boreholes are location-sensitive evidence carriers. Exact borehole, sample, well-log, and private-well locations are restricted or generalized by default."
  - "BoreholeReference, Well LogReference, core/cuttings descriptions, well-derived picks, completion records, permits, and production records are distinct source/evidence classes and must not be collapsed."
  - "Public derivatives are generalized or aggregated only, with redaction or aggregation receipts, review records, policy outcomes, correction paths, and rollback targets."
  - "Concrete executable behavior, source activation, schedules, CI coverage, schema paths, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Geology Boreholes Pipeline

> Executable Geology sublane for transforming admitted borehole, well, stratigraphic-test, geotechnical boring, core/cuttings, completion, and related subsurface point records into governed candidates, quarantine records, normalized records, catalog/triplet handoffs, receipts, and release-review packages — while preserving exact-location sensitivity, source role, owner/privacy posture, evidence, correction path, and rollback boundaries.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-geology%20boreholes-2e7d32)
![authority](https://img.shields.io/badge/authority-executable%20logic-0a7ea4)
![sensitivity](https://img.shields.io/badge/exact%20boreholes-restricted%20by%20default-d62728)
![publication](https://img.shields.io/badge/publication-generalized%20or%20aggregated%20only-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/geology/boreholes/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Geology and Natural Resources  
**Sublane:** Boreholes / wells / subsurface point evidence  
**Placement posture:** nested executable sublane under `pipelines/domains/geology/`; concrete executable behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Public posture:** no direct publication; exact borehole, well-log, sample, core, and private-well locations are restricted by default, and public derivatives require generalization or aggregation with EvidenceBundle, policy, review, correction, and rollback closure

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Borehole anti-collapse rules](#3-borehole-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Borehole scope](#6-borehole-scope)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Minimal borehole candidate record](#11-minimal-borehole-candidate-record)
- [12. Tests, fixtures, receipts, and proofs](#12-tests-fixtures-receipts-and-proofs)
- [13. Promotion, publication, correction, and rollback](#13-promotion-publication-correction-and-rollback)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipelines/domains/geology/boreholes/` is the executable sublane for Geology borehole and subsurface point-evidence processing.

It supports candidate processing for:

- `BoreholeReference` candidates for drilled holes, water wells, oil/gas wells, stratigraphic tests, geotechnical borings, monitoring wells, and related subsurface point records;
- borehole identity, source identifiers, permit identifiers, API numbers, water-well identifiers, stratigraphic-test identifiers, and crosswalk confidence;
- borehole location, coordinate precision, public-safe generalized geometry, aggregation products, owner/privacy posture, rights posture, and source-vintage state;
- drilling/completion metadata, depth, total depth, screened interval, casing interval, completion date, driller/operator fields, and datum/unit metadata where admitted;
- well logs, well tops, core/cuttings, and stratigraphic picks as linked evidence, not as borehole-owned truth;
- hydrostratigraphy and water-well context handoffs to Hydrology only with owning-domain refs and policy outcomes;
- generalized/aggregated public products such as borehole-density or well-availability layers where release workflow permits them;
- quarantine records for missing source descriptor, unresolved well identity, missing depth/datum, exact-location exposure risk, owner/privacy uncertainty, source-role collapse, rights uncertainty, schema drift, or validation failure;
- validation, catalog, triplet, EvidenceBundle, release-review, correction, and rollback handoff packages.

This directory implements or will implement the **how** of borehole processing. It does not fetch source data, parse well logs as the primary owner, define Geology object meaning, define schemas, encode policy, store lifecycle data, decide release, certify subsurface truth, certify resource/reserve/production claims, decide permits/titles, expose exact sensitive locations, or create public map/API products by itself.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/geology/`? | Geology is a domain lane under the domain-pipeline umbrella. | CONFIRMED path responsibility pattern; behavior NEEDS VERIFICATION |
| Why `boreholes/`? | This is a narrow executable sublane for borehole and subsurface point-evidence processing. | PROPOSED / NEEDS VERIFICATION |
| Is this a connector? | No. Source fetching belongs in `connectors/<source>` or an accepted source-edge home. | CONFIRMED separation |
| Does this own boreholes-and-wells doctrine? | No. Human-facing doctrine remains in `docs/domains/geology/sublanes/boreholes-wells.md`; object meaning belongs in contracts. | CONFIRMED doc separation |
| Does this replace `well_logs/`? | No. `well_logs/` owns log/curve/parsing-focused execution; this lane owns borehole identity, point sensitivity, and subsurface point-evidence candidates. | PROPOSED boundary |
| Can this sublane publish? | No. It may prepare generalized/aggregated release handoffs only through governed workflow. | CONFIRMED doctrine posture |

> [!IMPORTANT]
> Borehole output is location-sensitive evidence. Exact point geometry, owner identity, proprietary log content, and private-well context are denied by default. Public release requires generalization or aggregation plus redaction/aggregation receipts, review, policy, correction, and rollback refs.

[⬆ Back to top](#top)

---

## 3. Borehole anti-collapse rules

Borehole processing must preserve point-evidence status, source role, privacy posture, and release state.

Disallowed collapses:

```text
borehole point -> public exact point
private well -> public owner/location record
borehole encountering unit -> mapped unit boundary
well top -> continuous stratigraphic surface without model receipt
well log -> borehole identity proof without source id
completion record -> aquifer measurement
water well -> water-rights decision
oil/gas well record -> production proof
permit record -> subsurface truth
core/cuttings note -> verified lithology without review
generalized density layer -> exact source locations
AI summary -> EvidenceBundle
pipeline run -> release approval
```

Required distinctions:

- source identity, source role, source product, borehole id, well id, source identifiers, source vintage, location precision, rights posture, owner/privacy posture, and sensitivity tier are explicit;
- borehole, well log, well top, core/cuttings, completion record, permit, production record, water-rights context, and generated summary remain distinct;
- exact geometry remains restricted unless release policy explicitly allows a public-safe representation;
- public derivatives are generalized or aggregated, never raw point exposure by default;
- every public claim resolves evidence or abstains;
- publication requires public-safe transforms, review, correction path, and rollback target.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable Geology borehole and subsurface point-evidence processing.

Appropriate contents include:

- fixture-only dry-run entrypoints;
- borehole source-candidate normalizers;
- borehole/well identity and crosswalk helpers;
- source-id, API number, permit id, water-well id, stratigraphic-test id, and monitoring-well id validators;
- location precision, owner/privacy, private-well, and exact-subsurface sensitivity preflight helpers;
- redaction, aggregation, and public-safe geometry preflight helpers;
- depth, datum, total-depth, completion, casing, screened-interval, and source-unit validators;
- links to well logs, well tops, cores, cuttings, measured sections, geochemistry, and geophysics as evidence refs;
- source-role anti-collapse validators for KGS/KCC/KDHE/WWC5-style records, permits, completions, and production-adjacent records;
- quarantine routing helpers for missing descriptor, unresolved identity, rights uncertainty, source-role collapse, sensitivity failure, evidence gaps, or schema failures;
- receipt emitters, if not shared;
- handoff helpers for validation, catalog, triplet, and release workflow.

A good placement test:

> If the code transforms admitted borehole lifecycle inputs into Geology borehole candidates, quarantine records, validation handoffs, receipts, or downstream handoff packages, it may belong here. If it fetches source data, owns well-log parsing, defines schemas, stores lifecycle data, decides policy, owns source profiles, writes catalog records directly, approves release, or creates public API/map payloads, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Source fetchers / connectors | `connectors/kansas/kgs/`, `connectors/kansas/kcc-oil-gas-reg/`, `connectors/kansas/kdhe/`, or accepted connector home |
| Source catalog profiles | `docs/sources/catalog/...` |
| Source descriptors / source registry entries | `data/registry/sources/geology/`, `data/registry/sources/kansas/`, or approved registry home |
| Geology doctrine and object meaning | `docs/domains/geology/...`, `contracts/domains/geology/` |
| Well-log parsing, LAS curves, and log-specific extraction | `pipelines/domains/geology/well_logs/` |
| Stratigraphic correlation and interval nomenclature | Stratigraphy docs/contracts and accepted stratigraphy pipeline roots |
| Bedrock or surficial map unit authority | Bedrock/surficial lanes and contracts |
| Hydrology measurements, water rights, and water-use decisions | Hydrology/water-rights responsibility roots |
| Land/privacy owner, parcel, title, lease, or permit truth | People/Land/legal/regulatory responsibility roots |
| JSON Schemas | `schemas/contracts/v1/domains/geology/` or accepted schema home |
| Policy, rights, sensitivity, release rules | `policy/...` responsibility roots |
| Declarative run specs | `pipeline_specs/geology/...` |
| Fixtures | `fixtures/domains/geology/boreholes/` or accepted fixture home |
| Tests | `tests/pipelines/domains/geology/boreholes/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet, or published outputs | `data/...` lifecycle homes |
| Public API or map code | `apps/governed-api/`, `apps/explorer-web/`, packages |
| Release decisions and manifests | `release/...` responsibility roots |

[⬆ Back to top](#top)

---

## 6. Borehole scope

| Scope area | Pipeline responsibility | Failure behavior |
|---|---|---|
| Source identity | Preserve source id, descriptor refs, rights, source role, source product, and vintage. | Quarantine if missing. |
| Borehole identity | Preserve borehole id, well id, source ids, permit/API/water-well ids, and identity confidence. | Quarantine on unresolved identity. |
| Location | Preserve original precision, privacy class, and public-safe transform state. | Restrict or quarantine exact sensitive points. |
| Depth/completion | Preserve total depth, depth datum, units, screened intervals, casing/completion metadata, and source units. | Quarantine on ambiguity. |
| Evidence links | Preserve well-log, well-top, core/cuttings, measured-section, geochemistry, and geophysics refs. | Abstain or quarantine if unsupported. |
| Cross-lane context | Carry Hydrology, land/privacy, regulatory, and resource context as context only. | Deny if it becomes proof or decision authority. |
| Public derivatives | Prepare generalized/aggregated candidates only with receipts. | Deny exact public exposure by default. |
| Release handoff | Prepare public-safe candidates only after evidence, policy, and sensitivity closure. | No direct publication. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every Geology borehole run must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** approved fixtures, immutable raw captures, work inputs, quarantine inputs in remediation mode, or prior processed borehole baselines.
2. **Normalize** into Geology work candidates with source role, borehole identity, source identifiers, depth/datum refs, location precision, owner/privacy posture, sensitivity state, evidence refs, policy refs, and receipt refs.
3. **Quarantine** missing source descriptor, missing borehole/well identity, missing depth datum, unresolved source-id crosswalk, source-role collapse, rights failure, privacy failure, sensitivity failure, evidence gap, schema drift, or validation failure.
4. **Emit receipts** with input refs, source refs, identity refs, location-transform refs, depth/datum refs, evidence refs, validation refs, output refs, and outcomes.
5. **Support promotion** only by feeding downstream validation and review workflows.
6. **Never publish directly.**

Borehole processing is a lifecycle transformation. It is not catalog closure, release approval, public artifact creation, resource proof, permit proof, or owner/title proof by itself.

[⬆ Back to top](#top)

---

## 8. Required gates

Every Geology borehole run must check or explicitly fail closed on:

1. **Input lifecycle gate** — input is fixture, raw capture, work input, quarantine-remediation input, or accepted baseline.
2. **Source descriptor gate** — source identity, role, rights, citation, cadence/vintage, and sensitivity posture are known.
3. **Source-role gate** — borehole records, well logs, well tops, core/cuttings, completion records, permits, production records, interpretations, and generated summaries remain distinct.
4. **Identity gate** — borehole/well/source/API/permit/water-well ids and crosswalk confidence are explicit.
5. **Location sensitivity gate** — exact borehole, sample, private-well, sensitive-resource, infrastructure-adjacent, and owner-linked locations are restricted or generalized unless release policy proves otherwise.
6. **Depth/datum gate** — total depth, depth reference, datum, units, interval bounds, casing/screen/completion refs are explicit where material.
7. **Evidence-link gate** — well-log, top, core, cutting, geochemistry, geophysics, and measured-section refs are links with receipts, not silent truth promotion.
8. **Owner/privacy gate** — private-well owner identity, parcel joins, and contact information fail closed unless explicitly permitted by policy.
9. **Evidence gate** — claim-bearing downstream candidates can resolve EvidenceBundle support or abstain.
10. **Policy/sensitivity gate** — unresolved rights, controlled joins, exact exposure risk, or public-safe transform gaps fail closed.
11. **Schema/contract gate** — candidates match accepted Geology schema and borehole semantics.
12. **Correction/rollback gate** — release-facing handoff includes correction path and rollback target expectations.
13. **No-direct-publish gate** — no writes to public UI, public API, published layers, or release manifests as a pipeline side effect.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/domains/geology/boreholes/
├── README.md                         # this file
├── BOREHOLES_PIPELINE_CONTRACT.md    # PROPOSED: borehole execution contract
├── run_dry_fixture.py                # PROPOSED synthetic/generalized fixture only
├── normalize_borehole_candidate.py   # PROPOSED
├── normalize_borehole_identity.py    # PROPOSED
├── normalize_location_precision.py   # PROPOSED
├── validate_source_role.py           # PROPOSED
├── validate_identity_crosswalks.py   # PROPOSED
├── validate_depth_completion.py      # PROPOSED
├── validate_location_sensitivity.py  # PROPOSED
├── validate_owner_privacy.py         # PROPOSED
├── build_public_aggregation.py       # PROPOSED if approved
├── route_quarantine.py               # PROPOSED
├── emit_receipt.py                   # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/geology/boreholes.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside this code. Use accepted lifecycle homes under `data/work/geology/`, `data/quarantine/geology/`, `data/processed/geology/`, `data/catalog/domain/geology/`, `data/triplets/geology/`, `data/published/layers/geology/`, proof homes under `data/proofs/`, receipt homes under `data/receipts/`, and release homes under `release/`.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Fixture input | `fixtures/domains/geology/boreholes/` or accepted fixture home | Synthetic, generalized, or redacted. |
| Raw source capture | `data/raw/geology/<source_id>/<run_id>/` | Immutable source-edge capture with descriptor and receipt. |
| Work candidate | `data/work/geology/<run_id>/` | Candidate only. |
| Quarantine record | `data/quarantine/geology/<reason>/<run_id>/` | Failed, restricted, unresolved, or unsafe material. |
| Processed borehole record | `data/processed/geology/<dataset_id>/<version>/` | Only after validation and governed promotion. |
| Generalized/aggregated derivative | `data/processed/geology/<dataset_id>/<version>/` before release | Candidate only; exact input remains protected. |
| Catalog/triplet handoff | `data/catalog/domain/geology/`, `data/triplets/geology/` | Projection only; not publication. |
| Receipt | `data/receipts/pipeline/geology/boreholes/<run_id>.yml` or accepted receipt home | Records inputs, identities, privacy/sensitivity checks, outputs. |
| Evidence proof | `data/proofs/evidence_bundle/` or accepted proof home | Required for claim-bearing records. |
| Release handoff | `release/candidates/geology/` | Reviewable, release-gated output only. |

[⬆ Back to top](#top)

---

## 11. Minimal borehole candidate record

The final schema is not defined here. This example shows the minimum information a Geology borehole candidate should preserve.

```yaml
schema_version: kfm.geology_borehole_candidate.v1
candidate_id: geology_borehole_<source_id>_<borehole_id>_<hash>
pipeline_id: domains.geology.boreholes
run_id: run_YYYYMMDDThhmmssZ
status: WORK_CANDIDATE
object_family: <BoreholeReference|WellReference|CoreSampleReference|CompletionContext>
source:
  source_id: <source_id>
  source_role: <observed|authority|administrative|regulatory|interpretation|generated_context|synthetic>
  source_product: <wwc5|kgs_well_record|kcc_well_record|stratigraphic_test|geotechnical_boring|monitoring_well|other>
  lifecycle_ref: data/raw/geology/<source_id>/<run_id>/
  input_hash: sha256:<hash>
  rights_state: needs_review
identity:
  borehole_id: null
  well_id: null
  api_number: null
  permit_id: null
  water_well_id: null
  identity_confidence: needs_review
location:
  original_location_ref: null
  public_location_ref: null
  precision_class: restricted
  privacy_class: restricted
  public_safe_transform_ref: null
depth_completion:
  total_depth: null
  depth_units: null
  vertical_datum: null
  screened_intervals: []
  casing_intervals: []
evidence_links:
  well_log_refs: []
  well_top_refs: []
  core_sample_refs: []
  geochemistry_refs: []
  geophysics_refs: []
policy:
  outcome: ABSTAIN
  reason_code: SOURCE_DESCRIPTOR_IDENTITY_LOCATION_POLICY_OR_EVIDENCE_NOT_RESOLVED
evidence:
  evidence_bundle_ref: null
  citation_state: ABSTAIN
anti_collapse:
  exact_borehole_location_is_public: false
  private_well_owner_is_public: false
  borehole_is_unit_boundary: false
  permit_record_is_subsurface_truth: false
  generated_summary_is_evidence: false
outputs:
  candidate_record: data/work/geology/run_YYYYMMDDThhmmssZ/borehole_candidate.yml
  receipt: data/receipts/pipeline/geology/boreholes/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 12. Tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic/generalized/redacted, and no-network** until source activation, boreholes spec, evidence, policy, sensitivity, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/geology/boreholes/
├── test_no_network_dry_run.py              # PROPOSED
├── test_source_descriptor_required.py      # PROPOSED
├── test_borehole_identity_required.py      # PROPOSED
├── test_location_precision_required.py     # PROPOSED
├── test_exact_point_restricted.py          # PROPOSED
├── test_private_well_owner_denied.py       # PROPOSED
├── test_depth_completion_refs_required.py  # PROPOSED
├── test_source_role_preserved.py           # PROPOSED
├── test_borehole_not_unit_boundary.py      # PROPOSED
├── test_permit_not_subsurface_truth.py     # PROPOSED
├── test_policy_public_safe_required.py     # PROPOSED
├── test_evidence_gap_abstains.py           # PROPOSED
├── test_receipt_hashes.py                  # PROPOSED
└── test_no_direct_publish.py               # PROPOSED
```

A dry run should prove fixtures load without network access, source descriptors are required, borehole identity and location precision are preserved, exact point geometry fails closed, private-well owner exposure is denied by default, receipts are deterministic, and no run writes directly to public UI, public API, catalog store, published layers, or release manifests.

[⬆ Back to top](#top)

---

## 13. Promotion, publication, correction, and rollback

Geology borehole pipelines may prepare candidates and handoff packages. They do not publish.

Required chain:

```text
admitted borehole / well source capture
  -> borehole work candidate
  -> validation report
  -> policy decision
  -> EvidenceBundle closure
  -> processed BoreholeReference / generalized derivative
  -> catalog / triplet candidate
  -> release candidate
  -> ReleaseManifest
  -> RollbackCard
  -> public-safe artifact
```

Correction and rollback posture:

- denied, abstained, errored, restricted, stale, conflicted, and quarantined borehole runs remain auditable;
- receipts preserve source refs, identity refs, location precision refs, redaction/aggregation refs, evidence refs, source-role refs, policy outcomes, and failure reasons;
- processed versions are produced by governed promotion, not hidden overwrite;
- downstream artifacts are invalidated if source refs, borehole ids, location-transform refs, EvidenceBundle refs, policy refs, source-role refs, privacy refs, correction refs, or rollback refs drift;
- release rollback is owned by `release/`, not by this directory.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- fills the blank `pipelines/domains/geology/boreholes/README.md` file;
- identifies this directory as a nested executable Geology boreholes sublane;
- prevents connector, source-profile, schema, contract, policy, fixture, test, data, proof, catalog, graph, public API, UI, owner/privacy decision, legal/resource decision, and release authority from being placed here;
- preserves borehole, well, core/cuttings, completion, well-log links, source-role, identity, depth/datum, exact-location sensitivity, owner/privacy, evidence, policy, lifecycle, catalog/triplet, release, correction, and rollback boundaries;
- blocks exact-point-as-public, private-owner-as-public, borehole-as-unit-boundary, permit-record-as-subsurface-truth, generated-summary-as-evidence, and direct publication writes;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable work in this sublane is done only when it has source-descriptor coverage, synthetic/generalized/redacted no-network fixtures, schema-backed candidates, contract conformance, identity/location/source-role/sensitivity/evidence/policy/no-direct-publish tests, deterministic receipts, CI coverage, steward-review handoff, and release/correction/rollback documentation.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `GEOL-BORE-001` | Should borehole execution remain separate from `well_logs/`, or should the two be merged with subcommands for identity, logs, tops, and privacy? | NEEDS VERIFICATION / ADR |
| `GEOL-BORE-002` | Which source-edge jobs own KGS, KDHE/WWC5, KCC, geotechnical, monitoring-well, and stratigraphic-test retrieval before this sublane reads lifecycle inputs? | NEEDS VERIFICATION |
| `GEOL-BORE-003` | Which schema owns BoreholeReference, WellReference, CoreSampleReference, location precision, redaction receipts, and quarantine reasons? | NEEDS VERIFICATION |
| `GEOL-BORE-004` | Which first-wave source is approved for fixture-only dry runs: synthetic boreholes, KGS wells, WWC5, KCC well records, or generalized density fixtures? | NEEDS VERIFICATION |
| `GEOL-BORE-005` | Which CI job owns Geology borehole invariant tests? | UNKNOWN |
| `GEOL-BORE-006` | What public-safe precision, aggregation, suppression, and caveat levels are allowed for released borehole-density or availability products? | NEEDS VERIFICATION |
| `GEOL-BORE-007` | Which receipt type owns redaction, aggregation, owner/privacy review, and location generalization? | PROPOSED / NEEDS ADR |

---

## Maintainer note

Start with synthetic/generalized fixture-only dry runs and negative tests. Do not add live source fetching, source-profile editing, schema authority, policy authority, direct catalog writes, public exact-point layers, release-manifest writes, or generated well summaries until source roles, borehole identity, location/privacy review, EvidenceBundle closure, public-safe transforms, release review, and rollback are proven.
