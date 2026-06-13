<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-geology-well-logs-readme
title: Geology Well Logs Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <geology-pipeline-owner>
  - <geology-domain-steward>
  - <kgs-source-steward>
  - <kcc-source-steward>
  - <hydrology-domain-steward>
  - <evidence-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: restricted-by-default-for-exact-subsurface-and-private-well-context
path: pipelines/domains/geology/well_logs/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - pipelines/domains/geology/README.md
  - docs/domains/geology/README.md
  - docs/domains/geology/POLICY.md
  - docs/domains/geology/PRESERVATION_MATRIX.md
  - docs/sources/catalog/kansas/ksgs.md
  - docs/sources/catalog/kansas/kcc-oil-gas-reg.md
  - pipeline_specs/geology/well_logs.yaml
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
  - well-logs
  - boreholes
  - subsurface
  - stratigraphy
  - lithology
  - hydrostratigraphy
  - kgs
  - las
  - wwc5
  - kcc
  - evidence
  - policy
  - restricted
  - governance
notes:
  - "This README fills the blank pipelines/domains/geology/well_logs path as a nested executable Geology well-log sublane."
  - "Well-log pipeline logic is executable implementation support only; it does not own source descriptors, source catalog profiles, connectors, schemas, policy, lifecycle data, catalog truth, resource decisions, permit decisions, title decisions, or release decisions."
  - "Well logs, boreholes, cores, samples, well tops, LAS files, WWC5 records, and KCC regulatory records are related but distinct evidence/source-role classes."
  - "Exact subsurface, private-well, sensitive resource, infrastructure-adjacent, and unresolved-rights material fails closed by default."
  - "KGS geologic/subsurface authority and KCC regulatory posture must not be collapsed."
  - "Concrete executable behavior, source activation, schedules, CI coverage, schema paths, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Geology Well Logs Pipeline

> Executable Geology sublane for transforming admitted well-log, borehole, core, sample, well-top, LAS, WWC5, and related subsurface source material into governed candidates, quarantine records, normalized records, catalog/triplet handoffs, receipts, and release-review packages — while preserving source role, evidence, rights, sensitivity, location precision, stratigraphic uncertainty, correction path, and rollback boundaries.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-geology%20well%20logs-2e7d32)
![authority](https://img.shields.io/badge/authority-executable%20logic-0a7ea4)
![sensitivity](https://img.shields.io/badge/exact%20subsurface-restricted%20by%20default-d62728)
![publication](https://img.shields.io/badge/publication-release%20gated-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/geology/well_logs/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Geology and Natural Resources  
**Sublane:** Well logs / boreholes / subsurface observations  
**Placement posture:** nested executable sublane under `pipelines/domains/geology/`; concrete executable behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Public posture:** no direct publication; exact subsurface and private-well material is restricted/generalized by default and requires EvidenceBundle, source-role, sensitivity, policy, catalog/triplet, release, correction, and rollback closure

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Well-log anti-collapse rules](#3-well-log-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Well-log scope](#6-well-log-scope)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Minimal well-log candidate record](#11-minimal-well-log-candidate-record)
- [12. Tests, fixtures, receipts, and proofs](#12-tests-fixtures-receipts-and-proofs)
- [13. Promotion, publication, correction, and rollback](#13-promotion-publication-correction-and-rollback)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipelines/domains/geology/well_logs/` is the executable sublane for Geology well-log and subsurface observation processing.

It supports candidate processing for:

- boreholes, wells, well-log records, LAS logs, scanned logs, digital curves, and well tops;
- lithology, stratigraphy, geologic age, formation/top picks, interval descriptions, depth intervals, and sample/core references;
- water-well completion records, WWC5-style completion context, and hydrostratigraphy bridge candidates where admitted;
- oil/gas well and production-adjacent subsurface observations where admitted from KGS-style sources;
- KCC regulatory references only as regulatory context, not subsurface truth;
- location, datum, depth-reference, coordinate-precision, operator/owner redaction, and sensitivity transforms;
- quarantine records for missing source descriptor, missing well identity, missing depth reference, source-role collapse, location precision risk, private-well exposure, rights uncertainty, schema drift, or validation failure;
- validation, catalog, triplet, EvidenceBundle, release-review, correction, and rollback handoff packages.

This directory implements or will implement the **how** of well-log processing. It does not fetch source data, define Geology object meaning, define schemas, encode policy, store lifecycle data, decide release, certify resource/reserve/production claims, decide permits/titles, expose exact sensitive locations, or create public map products by itself.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/geology/`? | Geology is a domain lane under the domain-pipeline umbrella. | CONFIRMED path responsibility pattern; behavior NEEDS VERIFICATION |
| Why `well_logs/`? | This is a narrow executable sublane for well-log, borehole, and subsurface-observation processing. | PROPOSED / NEEDS VERIFICATION |
| Is this a connector? | No. Source fetching belongs in `connectors/<source>` or an accepted source-edge home. | CONFIRMED separation |
| Does this own well-log doctrine? | No. Human-facing doctrine remains in `docs/domains/geology/`; object meaning belongs in contracts. | CONFIRMED doc separation |
| Does this own source profiles? | No. KGS and KCC source profiles remain under `docs/sources/catalog/kansas/`; SourceDescriptors remain in registry homes. | CONFIRMED source separation |
| Can this sublane publish? | No. It may prepare candidates and release handoffs only through governed workflow. | CONFIRMED doctrine posture |

> [!IMPORTANT]
> Well-log output is not public release, not resource/reserve truth, not permit truth, not title truth, and not a public exact-subsurface layer. It is source-bound subsurface evidence that must carry source role, rights, sensitivity, EvidenceBundle, policy, correction, and rollback refs.

[⬆ Back to top](#top)

---

## 3. Well-log anti-collapse rules

Well-log processing must preserve source role, source family, depth/reference semantics, and release state.

Disallowed collapses:

```text
well log -> reserve estimate
well log -> production record
well log -> permit approval
KCC regulatory filing -> subsurface occurrence truth
KGS observed/geologic record -> KCC regulatory status
WWC5 water-well record -> oil/gas production evidence
LAS curve -> interpreted formation top without interpretation receipt
well top -> continuous stratigraphic surface without model receipt
private well location -> public exact point
sample/core note -> verified lithology without review
AI summary -> EvidenceBundle
pipeline run -> release approval
```

Required distinctions:

- source identity, source role, source product, well id, borehole id, source vintage, location precision, depth reference, datum, units, and rights posture are explicit;
- observed/submitted logs, interpreted tops, modeled surfaces, regulatory records, production records, permits, estimates, and generated summaries remain distinct;
- location precision, private-well sensitivity, infrastructure-adjacent risk, and resource-location sensitivity fail closed until policy permits generalized release;
- every public claim must resolve evidence or abstain;
- publication requires public-safe transforms, release review, correction path, and rollback target.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable Geology well-log processing.

Appropriate contents include:

- fixture-only dry-run entrypoints;
- well-log source-candidate normalizers;
- LAS metadata and curve-manifest normalizers;
- scanned-log metadata and OCR-output quarantine helpers;
- well/borehole identity and crosswalk helpers;
- depth-reference, datum, unit, interval, and curve validators;
- lithology, stratigraphy, formation/top, core, sample, and hydrostratigraphy candidate builders;
- KGS/KCC source-role anti-collapse validators;
- private-well and exact-subsurface sensitivity preflight helpers;
- public-safe generalization and redaction preflight helpers;
- quarantine routing helpers for missing descriptor, missing depth reference, rights uncertainty, source-role collapse, sensitivity failure, evidence gaps, or schema failures;
- receipt emitters, if not shared;
- handoff helpers for validation, catalog, triplet, and release workflow.

A good placement test:

> If the code transforms admitted well-log lifecycle inputs into Geology well-log/subsurface candidates, quarantine records, validation handoffs, receipts, or downstream handoff packages, it may belong here. If it fetches source data, defines schemas, stores lifecycle data, decides policy, owns source profiles, writes catalog records directly, approves release, or creates public API/map payloads, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Source fetchers / connectors | `connectors/kansas/kgs/`, `connectors/kansas/kcc-oil-gas-reg/`, or accepted connector home |
| Source catalog profiles | `docs/sources/catalog/kansas/ksgs.md`, `docs/sources/catalog/kansas/kcc-oil-gas-reg.md`, or accepted source-profile home |
| Source descriptors / source registry entries | `data/registry/sources/geology/`, `data/registry/sources/kansas/`, or approved registry home |
| Geology doctrine and object meaning | `docs/domains/geology/...`, `contracts/domains/geology/` |
| JSON Schemas | `schemas/contracts/v1/domains/geology/` or accepted schema home |
| Policy, rights, sensitivity, release rules | `policy/...` responsibility roots |
| Declarative run specs | `pipeline_specs/geology/...` |
| Fixtures | `fixtures/domains/geology/well_logs/` or accepted fixture home |
| Tests | `tests/pipelines/domains/geology/well_logs/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet, or published outputs | `data/...` lifecycle homes |
| Resource, reserve, production, permit, lease, or title decisions | Owning Geology/resource/regulatory/legal domains and release/policy roots |
| Hydrology production truth or water-rights decisions | Hydrology and water-rights responsibility roots |
| Public API or map code | `apps/governed-api/`, `apps/explorer-web/`, packages |
| Release decisions and manifests | `release/...` responsibility roots |

[⬆ Back to top](#top)

---

## 6. Well-log scope

| Scope area | Pipeline responsibility | Failure behavior |
|---|---|---|
| Source identity | Preserve source id, descriptor refs, rights, source role, source product, and vintage. | Quarantine if missing. |
| Well identity | Preserve well id, borehole id, API/permit/source ids, crosswalks, and uncertainty. | Quarantine on unresolved identity. |
| Location | Preserve original precision and public-safe transform state. | Restrict or quarantine exact sensitive points. |
| Depth | Preserve depth reference, datum, units, intervals, measured/true vertical depth posture, and source units. | Quarantine on ambiguity. |
| Logs/curves | Preserve curve names, mnemonics, units, sampling interval, null values, and LAS/source headers. | Quarantine on unsupported parse. |
| Stratigraphy/lithology | Preserve interpreted vs observed/support roles, interval refs, and method receipts. | Deny silent interpretation. |
| KCC context | Carry regulatory refs only as regulatory context. | Deny if treated as subsurface truth. |
| Release handoff | Prepare public-safe candidates only after evidence, policy, and sensitivity closure. | No direct publication. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every Geology well-log run must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** approved fixtures, immutable raw captures, work inputs, quarantine inputs in remediation mode, or prior processed well-log baselines.
2. **Normalize** into Geology work candidates with source role, well identity, depth reference, datum, units, curve/interval refs, location precision, sensitivity state, evidence refs, policy refs, and receipt refs.
3. **Quarantine** missing source descriptor, missing well identity, missing depth datum, unsupported LAS/log parse, source-role collapse, rights failure, sensitivity failure, evidence gap, schema drift, or validation failure.
4. **Emit receipts** with input refs, source refs, parser refs, depth/datum refs, curve refs, validation refs, output refs, and outcomes.
5. **Support promotion** only by feeding downstream validation and review workflows.
6. **Never publish directly.**

Well-log processing is a lifecycle transformation. It is not catalog closure, release approval, or public artifact creation by itself.

[⬆ Back to top](#top)

---

## 8. Required gates

Every Geology well-log run must check or explicitly fail closed on:

1. **Input lifecycle gate** — input is fixture, raw capture, work input, quarantine-remediation input, or accepted baseline.
2. **Source descriptor gate** — source identity, role, rights, citation, cadence/vintage, and sensitivity posture are known.
3. **Source-role gate** — observed/submitted logs, interpreted tops, modeled surfaces, regulatory records, production records, permits, estimates, and generated summaries remain distinct.
4. **Well identity gate** — well/borehole/API/permit/source ids and crosswalk confidence are explicit.
5. **Location sensitivity gate** — exact subsurface/private-well/resource/infrastructure-adjacent locations are restricted or generalized unless release policy proves otherwise.
6. **Depth/datum gate** — depth reference, datum, units, interval bounds, and curve units are explicit.
7. **Parser/method gate** — LAS/scanned/OCR/formation-top extraction methods and parser versions have receipts.
8. **Evidence gate** — claim-bearing downstream candidates can resolve EvidenceBundle support or abstain.
9. **Policy/sensitivity gate** — unresolved rights, controlled joins, exact exposure risk, or public-safe transform gaps fail closed.
10. **Schema/contract gate** — candidates match accepted Geology schema and well-log semantics.
11. **Correction/rollback gate** — release-facing handoff includes correction path and rollback target expectations.
12. **No-direct-publish gate** — no writes to public UI, public API, published layers, or release manifests as a pipeline side effect.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/domains/geology/well_logs/
├── README.md                         # this file
├── WELL_LOGS_PIPELINE_CONTRACT.md    # PROPOSED: well-log execution contract
├── run_dry_fixture.py                # PROPOSED synthetic/generalized fixture only
├── normalize_well_log_candidate.py   # PROPOSED
├── normalize_las_metadata.py         # PROPOSED
├── normalize_well_identity.py        # PROPOSED
├── validate_depth_datum_units.py     # PROPOSED
├── validate_source_role.py           # PROPOSED
├── validate_location_sensitivity.py  # PROPOSED
├── validate_parser_receipts.py       # PROPOSED
├── build_stratigraphy_candidates.py  # PROPOSED
├── route_quarantine.py               # PROPOSED
├── emit_receipt.py                   # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/geology/well_logs.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside this code. Use accepted lifecycle homes under `data/work/geology/`, `data/quarantine/geology/`, `data/processed/geology/`, `data/catalog/domain/geology/`, `data/triplets/geology/`, `data/published/layers/geology/`, proof homes under `data/proofs/`, receipt homes under `data/receipts/`, and release homes under `release/`.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Fixture input | `fixtures/domains/geology/well_logs/` or accepted fixture home | Synthetic, generalized, or redacted. |
| Raw source capture | `data/raw/geology/<source_id>/<run_id>/` | Immutable source-edge capture with descriptor and receipt. |
| Work candidate | `data/work/geology/<run_id>/` | Candidate only. |
| Quarantine record | `data/quarantine/geology/<reason>/<run_id>/` | Failed, restricted, unresolved, or unsafe material. |
| Processed well-log record | `data/processed/geology/<dataset_id>/<version>/` | Only after validation and governed promotion. |
| Catalog/triplet handoff | `data/catalog/domain/geology/`, `data/triplets/geology/` | Projection only; not publication. |
| Receipt | `data/receipts/pipeline/geology/well_logs/<run_id>.yml` or accepted receipt home | Records inputs, parsers, depth refs, checks, outputs. |
| Evidence proof | `data/proofs/evidence_bundle/` or accepted proof home | Required for claim-bearing records. |
| Release handoff | `release/candidates/geology/` | Reviewable, release-gated output only. |

[⬆ Back to top](#top)

---

## 11. Minimal well-log candidate record

The final schema is not defined here. This example shows the minimum information a Geology well-log candidate should preserve.

```yaml
schema_version: kfm.geology_well_log_candidate.v1
candidate_id: geology_well_log_<source_id>_<well_id>_<log_id>_<hash>
pipeline_id: domains.geology.well_logs
run_id: run_YYYYMMDDThhmmssZ
status: WORK_CANDIDATE
object_family: <WellLog|Borehole|WellTop|CoreSample|LithologyInterval|HydrostratigraphyBridge>
source:
  source_id: <source_id>
  source_role: <observed|authority|regulatory|aggregate|model|interpretation|generated_context|synthetic>
  source_product: <las|wwc5|well_top|scanned_log|core_report|kcc_regulatory_ref|other>
  lifecycle_ref: data/raw/geology/<source_id>/<run_id>/
  input_hash: sha256:<hash>
  rights_state: needs_review
well_identity:
  well_id: null
  borehole_id: null
  api_number: null
  permit_id: null
  identity_confidence: needs_review
location:
  original_location_ref: null
  public_location_ref: null
  precision_class: restricted
  public_safe_transform_ref: null
depth:
  depth_reference: null
  datum: null
  units: null
  intervals: []
log:
  log_id: null
  curve_mnemonics: []
  parser_receipt_ref: null
interpretation:
  interpreted_tops: []
  interpretation_receipt_ref: null
policy:
  outcome: ABSTAIN
  reason_code: SOURCE_DESCRIPTOR_WELL_ID_DEPTH_POLICY_OR_EVIDENCE_NOT_RESOLVED
evidence:
  evidence_bundle_ref: null
  citation_state: ABSTAIN
anti_collapse:
  well_log_is_reserve_estimate: false
  regulatory_record_is_subsurface_truth: false
  exact_private_well_location_is_public: false
  generated_summary_is_evidence: false
outputs:
  candidate_record: data/work/geology/run_YYYYMMDDThhmmssZ/well_log_candidate.yml
  receipt: data/receipts/pipeline/geology/well_logs/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 12. Tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic/generalized/redacted, and no-network** until source activation, well-log spec, evidence, policy, sensitivity, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/geology/well_logs/
├── test_no_network_dry_run.py              # PROPOSED
├── test_source_descriptor_required.py      # PROPOSED
├── test_well_identity_required.py          # PROPOSED
├── test_depth_reference_required.py        # PROPOSED
├── test_las_parser_receipt_required.py     # PROPOSED
├── test_source_role_preserved.py           # PROPOSED
├── test_kcc_not_subsurface_truth.py        # PROPOSED
├── test_well_log_not_reserve_estimate.py   # PROPOSED
├── test_exact_location_restricted.py       # PROPOSED
├── test_policy_public_safe_required.py     # PROPOSED
├── test_evidence_gap_abstains.py           # PROPOSED
├── test_quarantine_on_schema_failure.py    # PROPOSED
├── test_receipt_hashes.py                  # PROPOSED
└── test_no_direct_publish.py               # PROPOSED
```

A dry run should prove fixtures load without network access, source descriptors are required, well identity/depth refs are preserved, KGS/KCC roles do not collapse, exact sensitive locations fail closed, receipts are deterministic, and no run writes directly to public UI, public API, catalog store, published layers, or release manifests.

[⬆ Back to top](#top)

---

## 13. Promotion, publication, correction, and rollback

Geology well-log pipelines may prepare candidates and handoff packages. They do not publish.

Required chain:

```text
admitted well-log source capture
  -> well-log work candidate
  -> validation report
  -> policy decision
  -> EvidenceBundle closure
  -> processed well-log / subsurface record
  -> catalog / triplet candidate
  -> release candidate
  -> ReleaseManifest
  -> RollbackCard
  -> public-safe artifact
```

Correction and rollback posture:

- denied, abstained, errored, restricted, stale, conflicted, and quarantined well-log runs remain auditable;
- receipts preserve source refs, well id refs, depth refs, parser refs, interpretation refs, evidence refs, source-role refs, policy outcomes, and failure reasons;
- processed versions are produced by governed promotion, not hidden overwrite;
- downstream artifacts are invalidated if source refs, well ids, depth refs, parser refs, interpretation refs, EvidenceBundle refs, policy refs, source-role refs, correction refs, or rollback refs drift;
- release rollback is owned by `release/`, not by this directory.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- fills the blank `pipelines/domains/geology/well_logs/README.md` file;
- identifies this directory as a nested executable Geology well-log sublane;
- prevents connector, source-profile, schema, contract, policy, fixture, test, data, proof, catalog, graph, public API, UI, legal/resource decision, and release authority from being placed here;
- preserves well-log, borehole, LAS, well-top, WWC5, KGS/KCC, source-role, well identity, depth/datum, location sensitivity, evidence, policy, lifecycle, catalog/triplet, release, correction, and rollback boundaries;
- blocks well-log-as-reserve, regulatory-record-as-subsurface-truth, private-well-location-as-public, generated-summary-as-evidence, and direct publication writes;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable work in this sublane is done only when it has source-descriptor coverage, synthetic/generalized/redacted no-network fixtures, schema-backed candidates, contract conformance, identity/depth/source-role/sensitivity/evidence/policy/no-direct-publish tests, deterministic receipts, CI coverage, steward-review handoff, and release/correction/rollback documentation.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `GEOL-WELLLOG-001` | Should well-log execution remain one sublane, or split into LAS, WWC5, scanned logs, well tops, cores/samples, and KCC regulatory refs? | NEEDS VERIFICATION / ADR |
| `GEOL-WELLLOG-002` | Which source-edge jobs own KGS, KCC, WWC5, LAS, and scanned-log retrieval before this sublane reads lifecycle inputs? | NEEDS VERIFICATION |
| `GEOL-WELLLOG-003` | Which schema owns WellLog, Borehole, WellTop, LithologyInterval, and HydrostratigraphyBridge candidates? | NEEDS VERIFICATION |
| `GEOL-WELLLOG-004` | Which first-wave source is approved for fixture-only dry runs: KGS LAS, WWC5, KGS well tops, scanned logs, or a synthetic well log? | NEEDS VERIFICATION |
| `GEOL-WELLLOG-005` | Which CI job owns Geology well-log invariant tests? | UNKNOWN |
| `GEOL-WELLLOG-006` | What public-safe location precision and caveat levels are allowed for released well-log context layers? | NEEDS VERIFICATION |
| `GEOL-WELLLOG-007` | Which receipt type owns LAS parsing, OCR parsing, formation-top interpretation, and depth/datum transforms? | PROPOSED / NEEDS ADR |

---

## Maintainer note

Start with synthetic/generalized fixture-only dry runs and negative tests. Do not add live source fetching, source-profile editing, schema authority, policy authority, direct catalog writes, public exact-subsurface layers, release-manifest writes, or generated resource summaries until source roles, well identity, depth references, EvidenceBundle closure, public-safe transforms, release review, and rollback are proven.
