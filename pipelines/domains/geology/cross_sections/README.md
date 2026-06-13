<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-geology-cross-sections-readme
title: Geology Cross Sections Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <geology-pipeline-owner>
  - <geology-domain-steward>
  - <stratigraphy-steward>
  - <bedrock-geology-steward>
  - <surficial-geology-steward>
  - <well-logs-steward>
  - <geophysics-steward>
  - <evidence-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: restricted-by-default-for-exact-subsurface-and-sensitive-section-context
path: pipelines/domains/geology/cross_sections/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - pipelines/domains/geology/README.md
  - pipelines/domains/geology/well_logs/README.md
  - pipelines/domains/geology/surficial_units/README.md
  - docs/domains/geology/README.md
  - docs/domains/geology/sublanes/stratigraphy.md
  - docs/domains/geology/sublanes/bedrock_geology.md
  - docs/domains/geology/sublanes/surficial.md
  - docs/domains/geology/POLICY.md
  - docs/domains/geology/PRESERVATION_MATRIX.md
  - docs/sources/catalog/kansas/ksgs.md
  - pipeline_specs/geology/cross_sections.yaml
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
  - cross-sections
  - stratigraphy
  - correlation
  - well-logs
  - boreholes
  - geophysics
  - bedrock
  - surficial-units
  - subsurface
  - interpretation
  - evidence
  - policy
  - restricted
  - governance
notes:
  - "This README fills the blank pipelines/domains/geology/cross_sections path as a nested executable Geology cross-section sublane."
  - "Cross-section pipeline logic is executable implementation support only; it does not own source descriptors, source catalog profiles, connectors, schemas, policy, lifecycle data, catalog truth, stratigraphic truth, bedrock truth, surficial truth, well-log truth, geophysics truth, or release decisions."
  - "Cross sections are interpretive 2D subsurface projections assembled from evidence-bearing inputs; they are not direct observations, canonical map facts, reserve/resource estimates, permit decisions, or public-safe artifacts by default."
  - "Stratigraphic correlation, well tops, geophysical horizons, modeled surfaces, and generalized display panels must preserve uncertainty, method receipts, source roles, and evidence refs."
  - "Exact subsurface, private-well, resource-location, infrastructure-adjacent, and unresolved-rights material fails closed by default."
  - "Concrete executable behavior, source activation, schedules, CI coverage, schema paths, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Geology Cross Sections Pipeline

> Executable Geology sublane for assembling evidence-bound geologic cross-section candidates, quarantine records, normalized section panels, catalog/triplet handoffs, receipts, and release-review packages from admitted stratigraphy, bedrock/surficial units, well logs, boreholes, cores, measured sections, and geophysical context — while preserving interpretation status, uncertainty, source role, location sensitivity, evidence, correction path, and rollback boundaries.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-geology%20cross%20sections-2e7d32)
![authority](https://img.shields.io/badge/authority-executable%20logic-0a7ea4)
![anti-collapse](https://img.shields.io/badge/cross--section%20%E2%89%A0%20canonical%20truth-d62728)
![sensitivity](https://img.shields.io/badge/exact%20subsurface-restricted%20by%20default-d62728)
![publication](https://img.shields.io/badge/publication-release%20gated-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/geology/cross_sections/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Geology and Natural Resources  
**Sublane:** Cross sections / subsurface interpretation panels  
**Placement posture:** nested executable sublane under `pipelines/domains/geology/`; concrete executable behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Public posture:** no direct publication; exact subsurface cross-section material is restricted/generalized by default and requires EvidenceBundle, source-role, sensitivity, policy, catalog/triplet, release, correction, and rollback closure

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Cross-section anti-collapse rules](#3-cross-section-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Cross-section scope](#6-cross-section-scope)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Minimal cross-section candidate record](#11-minimal-cross-section-candidate-record)
- [12. Tests, fixtures, receipts, and proofs](#12-tests-fixtures-receipts-and-proofs)
- [13. Promotion, publication, correction, and rollback](#13-promotion-publication-correction-and-rollback)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipelines/domains/geology/cross_sections/` is the executable sublane for Geology cross-section and subsurface-panel processing.

It supports candidate processing for:

- geologic cross-section panels, lines, section traces, vertical scales, datum references, and display envelopes;
- stratigraphic interval correlation and unit order candidates;
- well tops, borehole references, well-log picks, core/sample references, measured sections, and lithologic interval evidence;
- bedrock and surficial unit references where section panels intersect map units or boundary versions;
- geophysical horizon/context references where method receipts and uncertainty are present;
- hydrostratigraphy bridge context where admitted by Geology and Hydrology review;
- uncertainty bands, inferred contacts, faults, folds, contacts, truncations, and interpretation caveats;
- generalized public-safe cross-section views, diagrams, and metadata packages where release policy permits;
- quarantine records for missing source descriptor, unresolved section trace, missing vertical datum, unsupported correlation, missing method receipt, source-role collapse, exact-subsurface sensitivity, rights uncertainty, schema drift, or validation failure;
- validation, catalog, triplet, EvidenceBundle, release-review, correction, and rollback handoff packages.

This directory implements or will implement the **how** of cross-section processing. It does not fetch source data, define Geology object meaning, define schemas, encode policy, store lifecycle data, decide release, certify subsurface truth, certify resource/reserve claims, expose exact sensitive subsurface context, or create public map/API products by itself.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/geology/`? | Geology is a domain lane under the domain-pipeline umbrella. | CONFIRMED path responsibility pattern; behavior NEEDS VERIFICATION |
| Why `cross_sections/`? | This is a narrow executable sublane for cross-section and subsurface-interpretation panel processing. | PROPOSED / NEEDS VERIFICATION |
| Is this a connector? | No. Source fetching belongs in `connectors/<source>` or an accepted source-edge home. | CONFIRMED separation |
| Does this own stratigraphy doctrine? | No. Stratigraphy doctrine remains in `docs/domains/geology/sublanes/stratigraphy.md`; object meaning belongs in contracts. | CONFIRMED doc separation |
| Does this own well-log or geophysics truth? | No. It references accepted evidence from those lanes but does not become their authority. | CONFIRMED boundary posture |
| Can this sublane publish? | No. It may prepare candidates and release handoffs only through governed workflow. | CONFIRMED doctrine posture |

> [!IMPORTANT]
> Cross-section output is interpretive. A section panel is not a direct observation, not canonical map truth, not reserve proof, not permit/title proof, and not public-safe by default. It must carry source-role refs, evidence refs, uncertainty, sensitivity, policy, correction, and rollback refs.

[⬆ Back to top](#top)

---

## 3. Cross-section anti-collapse rules

Cross-section processing must preserve interpretation status, input evidence, uncertainty, and release state.

Disallowed collapses:

```text
cross-section panel -> canonical subsurface truth
stratigraphic correlation -> map fact
well top -> continuous horizon without method receipt
geophysical horizon -> observed contact
interpolated surface -> observed boundary
generalized display panel -> exact subsurface geometry
section trace -> property / permit / title claim
resource-bearing interval -> reserve estimate
private well evidence -> public exact point
AI-generated panel annotation -> EvidenceBundle
pipeline run -> release approval
```

Required distinctions:

- source identity, source role, input family, section trace, vertical/horizontal datum, units, scale, exaggeration, uncertainty, method receipts, and rights posture are explicit;
- observations, picks, interpretations, correlations, modeled surfaces, generalized panels, and generated labels remain distinct;
- every relationship between section elements and source evidence is auditable;
- public views require generalization/redaction and must not reveal exact private-well, resource, or infrastructure-adjacent sensitive context;
- every public claim resolves evidence or abstains;
- publication requires public-safe transforms, release review, correction path, and rollback target.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable Geology cross-section processing.

Appropriate contents include:

- fixture-only dry-run entrypoints;
- section trace and panel metadata normalizers;
- vertical datum, horizontal datum, unit, scale, and vertical-exaggeration validators;
- evidence-link builders for well logs, boreholes, cores, measured sections, map units, and geophysics;
- stratigraphic correlation validators that preserve uncertainty and method receipts;
- contact, fault, fold, horizon, interval, and unit panel candidate builders;
- generalized public-safe diagram/panel builders with transform receipts;
- exact-subsurface and private-well sensitivity preflight helpers;
- cross-lane ownership validators for Hydrology, Soil, Hazards, Natural Resources, Archaeology, and Infrastructure context;
- quarantine routing helpers for missing descriptor, missing datum, unsupported interpolation, evidence gaps, sensitivity failure, source-role collapse, or schema failures;
- receipt emitters, if not shared;
- handoff helpers for validation, catalog, triplet, and release workflow.

A good placement test:

> If the code transforms admitted Geology lifecycle inputs into evidence-bound cross-section candidates, quarantine records, validation handoffs, receipts, or downstream handoff packages, it may belong here. If it fetches source data, defines schemas, stores lifecycle data, decides policy, owns source profiles, writes catalog records directly, approves release, or creates public API/map payloads, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Source fetchers / connectors | `connectors/<source>` or accepted connector home |
| Source catalog profiles | `docs/sources/catalog/...` |
| Source descriptors / source registry entries | `data/registry/sources/geology/` or approved registry home |
| Stratigraphy doctrine and object meaning | `docs/domains/geology/sublanes/stratigraphy.md`, `contracts/domains/geology/` |
| Well-log parsing and well identity authority | `pipelines/domains/geology/well_logs/` and related contracts |
| Bedrock/surficial map unit authority | `pipelines/domains/geology/surficial_units/`, bedrock lanes, and contracts |
| Geophysics acquisition/processing authority | Geophysics lane or accepted Geology geophysics root |
| JSON Schemas | `schemas/contracts/v1/domains/geology/` or accepted schema home |
| Policy, rights, sensitivity, release rules | `policy/...` responsibility roots |
| Declarative run specs | `pipeline_specs/geology/...` |
| Fixtures | `fixtures/domains/geology/cross_sections/` or accepted fixture home |
| Tests | `tests/pipelines/domains/geology/cross_sections/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet, or published outputs | `data/...` lifecycle homes |
| Resource/reserve, permit, lease, title, or engineering decisions | Owning legal/regulatory/resource/release roots |
| Public API or map code | `apps/governed-api/`, `apps/explorer-web/`, packages |
| Release decisions and manifests | `release/...` responsibility roots |

[⬆ Back to top](#top)

---

## 6. Cross-section scope

| Scope area | Pipeline responsibility | Failure behavior |
|---|---|---|
| Source identity | Preserve source ids, descriptor refs, rights, source role, product, and vintage. | Quarantine if missing. |
| Section trace | Preserve line/trace id, coordinate refs, public-safe transform, and uncertainty. | Restrict or quarantine on ambiguity. |
| Vertical frame | Preserve vertical datum, units, scale, vertical exaggeration, and depth/elevation reference. | Quarantine on ambiguity. |
| Evidence links | Link every interval/contact/horizon to source evidence or method receipt. | Abstain or quarantine if unresolved. |
| Correlation | Preserve interpretive status and uncertainty. | Deny if promoted to map fact. |
| Interpolation/modeling | Preserve method refs and modeled status. | Deny if treated as observation. |
| Public-safe views | Produce generalized panels only after policy and transform refs. | No direct publication. |
| Release handoff | Prepare candidates only after evidence, sensitivity, and policy closure. | No direct release decision. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every Geology cross-section run must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** approved fixtures, immutable raw captures, processed inputs, work inputs, quarantine inputs in remediation mode, or prior processed cross-section baselines.
2. **Normalize** into Geology work candidates with source role, section trace, datum refs, evidence links, method receipts, uncertainty, location sensitivity, policy refs, and receipt refs.
3. **Quarantine** missing source descriptor, missing section trace, missing vertical datum, unsupported correlation, missing method receipt, source-role collapse, rights failure, sensitivity failure, evidence gap, schema drift, or validation failure.
4. **Emit receipts** with input refs, source refs, trace refs, datum refs, method refs, evidence refs, validation refs, output refs, and outcomes.
5. **Support promotion** only by feeding downstream validation and review workflows.
6. **Never publish directly.**

Cross-section processing is an interpretive lifecycle transformation. It is not catalog closure, release approval, canonical truth, or public artifact creation by itself.

[⬆ Back to top](#top)

---

## 8. Required gates

Every Geology cross-section run must check or explicitly fail closed on:

1. **Input lifecycle gate** — input is fixture, raw capture, work/processed input, quarantine-remediation input, or accepted baseline.
2. **Source descriptor gate** — source identity, role, rights, citation, cadence/vintage, and sensitivity posture are known.
3. **Source-role gate** — observation, pick, interpretation, correlation, modeled surface, generalized display, and generated summary remain distinct.
4. **Trace/datum gate** — section trace, horizontal CRS, vertical datum, units, scale, and vertical exaggeration are explicit.
5. **Evidence-link gate** — contacts, horizons, intervals, well tops, and correlations resolve source evidence or method receipts.
6. **Correlation gate** — stratigraphic correlations preserve interpretive status and uncertainty.
7. **Interpolation/model gate** — interpolated or modeled elements carry method receipts and do not become observations.
8. **Location sensitivity gate** — exact private-well, resource-location, infrastructure-adjacent, and sensitive subsurface details are restricted or generalized unless release policy proves otherwise.
9. **Cross-lane ownership gate** — cross-section context does not become Hydrology, Soil, Hazards, Natural Resources, Archaeology, or Infrastructure truth.
10. **Evidence gate** — claim-bearing downstream candidates can resolve EvidenceBundle support or abstain.
11. **Policy/sensitivity gate** — unresolved rights, controlled joins, exact exposure risk, or public-safe transform gaps fail closed.
12. **Schema/contract gate** — candidates match accepted Geology schema and cross-section semantics.
13. **Correction/rollback gate** — release-facing handoff includes correction path and rollback target expectations.
14. **No-direct-publish gate** — no writes to public UI, public API, published layers, or release manifests as a pipeline side effect.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/domains/geology/cross_sections/
├── README.md                            # this file
├── CROSS_SECTIONS_PIPELINE_CONTRACT.md  # PROPOSED: cross-section execution contract
├── run_dry_fixture.py                   # PROPOSED synthetic/generalized fixture only
├── normalize_section_trace.py           # PROPOSED
├── normalize_panel_frame.py             # PROPOSED
├── link_evidence_refs.py                # PROPOSED
├── validate_vertical_datum.py           # PROPOSED
├── validate_correlation_uncertainty.py  # PROPOSED
├── validate_method_receipts.py          # PROPOSED
├── validate_location_sensitivity.py     # PROPOSED
├── build_section_panel_candidate.py     # PROPOSED
├── route_quarantine.py                  # PROPOSED
├── emit_receipt.py                      # PROPOSED only if not shared
└── adapters/                            # PROPOSED thin lifecycle adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/geology/cross_sections.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside this code. Use accepted lifecycle homes under `data/work/geology/`, `data/quarantine/geology/`, `data/processed/geology/`, `data/catalog/domain/geology/`, `data/triplets/geology/`, `data/published/layers/geology/`, proof homes under `data/proofs/`, receipt homes under `data/receipts/`, and release homes under `release/`.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Fixture input | `fixtures/domains/geology/cross_sections/` or accepted fixture home | Synthetic, generalized, or redacted. |
| Raw source capture | `data/raw/geology/<source_id>/<run_id>/` | Immutable source-edge capture with descriptor and receipt. |
| Work candidate | `data/work/geology/<run_id>/` | Candidate only. |
| Quarantine record | `data/quarantine/geology/<reason>/<run_id>/` | Failed, restricted, unresolved, or unsafe material. |
| Processed cross-section record | `data/processed/geology/<dataset_id>/<version>/` | Only after validation and governed promotion. |
| Catalog/triplet handoff | `data/catalog/domain/geology/`, `data/triplets/geology/` | Projection only; not publication. |
| Receipt | `data/receipts/pipeline/geology/cross_sections/<run_id>.yml` or accepted receipt home | Records inputs, trace, datum, methods, evidence, outputs. |
| Evidence proof | `data/proofs/evidence_bundle/` or accepted proof home | Required for claim-bearing records. |
| Release handoff | `release/candidates/geology/` | Reviewable, release-gated output only. |

[⬆ Back to top](#top)

---

## 11. Minimal cross-section candidate record

The final schema is not defined here. This example shows the minimum information a Geology cross-section candidate should preserve.

```yaml
schema_version: kfm.geology_cross_section_candidate.v1
candidate_id: geology_cross_section_<source_id>_<section_trace_id>_<run_id>_<hash>
pipeline_id: domains.geology.cross_sections
run_id: run_YYYYMMDDThhmmssZ
status: WORK_CANDIDATE
object_family: <CrossSection|SectionTrace|SectionPanel|StratigraphicCorrelation|InterpretedHorizon>
source:
  source_id: <source_id>
  source_role: <observed|authority|interpretation|model|aggregate|generated_context|synthetic>
  lifecycle_ref: data/raw/geology/<source_id>/<run_id>/
  input_hash: sha256:<hash>
  rights_state: needs_review
section:
  section_trace_id: null
  horizontal_crs: null
  vertical_datum: null
  vertical_units: null
  vertical_exaggeration: null
  public_safe_transform_ref: null
evidence_links:
  well_log_refs: []
  borehole_refs: []
  measured_section_refs: []
  map_unit_refs: []
  geophysics_refs: []
  method_receipt_refs: []
interpretation:
  correlation_refs: []
  uncertainty_class: needs_review
  modeled_elements: []
policy:
  outcome: ABSTAIN
  reason_code: SOURCE_DESCRIPTOR_TRACE_DATUM_POLICY_OR_EVIDENCE_NOT_RESOLVED
evidence:
  evidence_bundle_ref: null
  citation_state: ABSTAIN
anti_collapse:
  cross_section_is_canonical_truth: false
  correlation_is_map_fact: false
  modeled_surface_is_observation: false
  generalized_panel_is_exact_geometry: false
  generated_label_is_evidence: false
outputs:
  candidate_record: data/work/geology/run_YYYYMMDDThhmmssZ/cross_section_candidate.yml
  receipt: data/receipts/pipeline/geology/cross_sections/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 12. Tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic/generalized/redacted, and no-network** until source activation, cross-section spec, evidence, policy, sensitivity, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/geology/cross_sections/
├── test_no_network_dry_run.py              # PROPOSED
├── test_source_descriptor_required.py      # PROPOSED
├── test_section_trace_required.py          # PROPOSED
├── test_vertical_datum_required.py         # PROPOSED
├── test_evidence_links_required.py         # PROPOSED
├── test_method_receipts_required.py        # PROPOSED
├── test_correlation_not_map_fact.py        # PROPOSED
├── test_cross_section_not_canonical_truth.py # PROPOSED
├── test_modeled_surface_not_observation.py # PROPOSED
├── test_exact_subsurface_restricted.py     # PROPOSED
├── test_policy_public_safe_required.py     # PROPOSED
├── test_evidence_gap_abstains.py           # PROPOSED
├── test_receipt_hashes.py                  # PROPOSED
└── test_no_direct_publish.py               # PROPOSED
```

A dry run should prove fixtures load without network access, source descriptors are required, section traces and datums are preserved, correlations remain interpretive, modeled elements do not become observations, exact sensitive subsurface content fails closed, receipts are deterministic, and no run writes directly to public UI, public API, catalog store, published layers, or release manifests.

[⬆ Back to top](#top)

---

## 13. Promotion, publication, correction, and rollback

Geology cross-section pipelines may prepare candidates and handoff packages. They do not publish.

Required chain:

```text
admitted section evidence / source capture
  -> cross-section work candidate
  -> validation report
  -> policy decision
  -> EvidenceBundle closure
  -> processed cross-section / section panel record
  -> catalog / triplet candidate
  -> release candidate
  -> ReleaseManifest
  -> RollbackCard
  -> public-safe artifact
```

Correction and rollback posture:

- denied, abstained, errored, restricted, stale, conflicted, and quarantined cross-section runs remain auditable;
- receipts preserve source refs, trace refs, datum refs, method refs, evidence refs, source-role refs, policy outcomes, and failure reasons;
- processed versions are produced by governed promotion, not hidden overwrite;
- downstream artifacts are invalidated if source refs, section trace refs, datum refs, method refs, EvidenceBundle refs, policy refs, source-role refs, public-safe transform refs, correction refs, or rollback refs drift;
- release rollback is owned by `release/`, not by this directory.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- fills the blank `pipelines/domains/geology/cross_sections/README.md` file;
- identifies this directory as a nested executable Geology cross-sections sublane;
- prevents connector, source-profile, schema, contract, policy, fixture, test, data, proof, catalog, graph, public API, UI, legal/resource decision, and release authority from being placed here;
- preserves section traces, vertical datum, stratigraphic correlations, well-log/borehole evidence, geophysical evidence, modeled/interpretive status, location sensitivity, evidence, policy, lifecycle, catalog/triplet, release, correction, and rollback boundaries;
- blocks cross-section-as-canonical-truth, correlation-as-map-fact, modeled-surface-as-observation, generalized-panel-as-exact-geometry, generated-label-as-evidence, and direct publication writes;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable work in this sublane is done only when it has source-descriptor coverage, synthetic/generalized no-network fixtures, schema-backed candidates, contract conformance, trace/datum/evidence/method/source-role/sensitivity/no-direct-publish tests, deterministic receipts, CI coverage, steward-review handoff, and release/correction/rollback documentation.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `GEOL-XSEC-001` | Should cross-section execution remain one sublane, or split into stratigraphic panels, structural sections, hydrostratigraphic sections, and geophysical sections? | NEEDS VERIFICATION / ADR |
| `GEOL-XSEC-002` | Which source-edge jobs own section traces, measured sections, KGS panels, well logs, and geophysical inputs before this sublane reads lifecycle inputs? | NEEDS VERIFICATION |
| `GEOL-XSEC-003` | Which schema owns CrossSection, SectionTrace, SectionPanel, InterpretedHorizon, and correlation elements? | NEEDS VERIFICATION |
| `GEOL-XSEC-004` | Which first-wave source is approved for fixture-only dry runs: synthetic section, KGS cross-section panel, well-log derived section, or generalized stratigraphic panel? | NEEDS VERIFICATION |
| `GEOL-XSEC-005` | Which CI job owns Geology cross-section invariant tests? | UNKNOWN |
| `GEOL-XSEC-006` | What public-safe generalization, vertical exaggeration disclosure, and exact-location suppression levels are allowed for released cross-section artifacts? | NEEDS VERIFICATION |
| `GEOL-XSEC-007` | Which receipt type owns correlation, interpolation, vertical datum, and section-panel rendering transforms? | PROPOSED / NEEDS ADR |

---

## Maintainer note

Start with synthetic/generalized fixture-only dry runs and negative tests. Do not add live source fetching, source-profile editing, schema authority, policy authority, direct catalog writes, exact subsurface public panels, release-manifest writes, or generated cross-section summaries until source roles, evidence links, correlations, method receipts, public-safe transforms, release review, and rollback are proven.
