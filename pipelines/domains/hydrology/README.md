<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-hydrology-readme
title: Hydrology Domain Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <hydrology-pipeline-owner>
  - <hydrology-domain-steward>
  - <hazards-domain-steward>
  - <geology-domain-steward>
  - <source-steward>
  - <evidence-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipelines/domains/hydrology/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - docs/domains/hydrology/README.md
  - docs/domains/hydrology/PUBLICATION_POSTURE.md
  - docs/domains/hydrology/DATA_LIFECYCLE.md
  - docs/domains/hazards/ARCHITECTURE.md
  - docs/domains/geology/README.md
  - docs/domains/soil/
  - docs/domains/agriculture/
  - pipeline_specs/hydrology/
  - contracts/domains/hydrology/
  - contracts/hydrology/
  - schemas/contracts/v1/domains/hydrology/
  - schemas/contracts/v1/hydrology/
  - policy/domains/hydrology/
  - policy/sensitivity/hydrology/
  - data/raw/hydrology/
  - data/work/hydrology/
  - data/quarantine/hydrology/
  - data/processed/hydrology/
  - data/catalog/domain/hydrology/
  - data/triplets/hydrology/
  - data/published/layers/hydrology/
  - data/registry/sources/hydrology/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/hydrology/
  - release/manifests/hydrology/
  - release/promotion_decisions/hydrology/
tags:
  - kfm
  - pipelines
  - domains
  - hydrology
  - watershed
  - huc
  - stream
  - gauge
  - groundwater
  - water-quality
  - nfhl
  - flood-context
  - evidence
  - policy
  - governance
notes:
  - "This README replaces the greenfield scaffold for pipelines/domains/hydrology while preserving the observed promotion-gate slice note as a governed candidate behavior."
  - "Hydrology pipeline logic is executable implementation support only; it does not own emergency warnings, flood alerts, official forecasts, schemas, source descriptors, policy, lifecycle data, catalog truth, regulatory determinations, or release decisions."
  - "Hydrology outputs must preserve anti-collapse boundaries between observed gauge readings, modeled hydrographs, regulatory flood context, forecasts, operational warnings, source observations, and generated summaries."
  - "NFHL is regulatory context only and must never be published as observed flooding."
  - "Concrete executable behavior, source activation, schedules, CI coverage, schema paths, release wiring, public API/map behavior, and the promotion decision stub remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# 💧 Hydrology Domain Pipeline

> Executable Hydrology-domain pipeline lane for converting admitted watershed, HUC, stream/reach, gauge, groundwater, water-quality, regulatory-flood-context, terrain, topology, and cross-lane water-context source material into governed candidates, quarantine records, processed records, catalog/triplet handoffs, receipts, promotion-decision stubs, and release-review packages — **without acting as an emergency flood-warning system or collapsing observed, modeled, regulatory, and operational truth classes**.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-hydrology%20domain%20pipeline-2e7d32)
![authority](https://img.shields.io/badge/authority-executable%20logic-0a7ea4)
![anti-collapse](https://img.shields.io/badge/NFHL%20%E2%89%A0%20observed%20flooding-d62728)
![publication](https://img.shields.io/badge/publication-release%20gated-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/hydrology/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Hydrology  
**Placement posture:** hydrology child lane under `pipelines/domains/`; concrete executable behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Public posture:** no direct publication and no emergency warning behavior; public output requires lifecycle, EvidenceBundle, source-role, temporal/freshness, sensitivity, policy, catalog/triplet, release, correction, and rollback closure

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Emergency-warning boundary](#3-emergency-warning-boundary)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Hydrology pipeline scope](#6-hydrology-pipeline-scope)
- [7. Source-family posture](#7-source-family-posture)
- [8. Lifecycle contract](#8-lifecycle-contract)
- [9. Required gates](#9-required-gates)
- [10. Sensitivity, source-role separation, and public-safe posture](#10-sensitivity-source-role-separation-and-public-safe-posture)
- [11. Directory contract](#11-directory-contract)
- [12. Inputs and outputs](#12-inputs-and-outputs)
- [13. Minimal hydrology pipeline candidate record](#13-minimal-hydrology-pipeline-candidate-record)
- [14. Promotion-gate slice](#14-promotion-gate-slice)
- [15. Dry-run, tests, fixtures, receipts, and proofs](#15-dry-run-tests-fixtures-receipts-and-proofs)
- [16. Promotion, publication, correction, and rollback](#16-promotion-publication-correction-and-rollback)
- [17. Definition of done](#17-definition-of-done)
- [18. Open questions](#18-open-questions)

---

## 1. Purpose

`pipelines/domains/hydrology/` is the executable pipeline lane for Hydrology-domain transformations.

It supports candidate processing for:

- watersheds and HUC units;
- stream, river, reach, waterbody, and hydrographic identity;
- gauge sites and hydrologic observation sites;
- flow, stage, water-level, water-quality, aquifer, groundwater, and hydrograph observations;
- regulatory flood context such as NFHL zones without treating them as observed inundation;
- upstream/downstream traces and topology candidates;
- hydrostratigraphy links and geology-hydrology bridge records;
- water-use, drought, irrigation, habitat, hazards, agriculture, soil, and infrastructure context joins;
- public-safe hydrology map products after evidence, policy, and release review;
- catalog, graph, Evidence Drawer, Focus Mode, and promotion-decision handoff packages.

This directory implements or will implement the **how** of Hydrology processing. It does not define Hydrology object meaning, schemas, policy, source descriptors, emergency warnings, official forecasts, flood determinations, lifecycle storage, catalog truth, or release approval.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/hydrology/`? | Hydrology is a domain lane under the domain-pipeline umbrella and is shown in the Hydrology docs as the executable pipeline segment. | CONFIRMED documentation pattern; executable behavior NEEDS VERIFICATION |
| Where do declarative specs live? | `pipeline_specs/hydrology/` or accepted spec home. | PROPOSED / NEEDS VERIFICATION |
| Where do source fetchers live? | `connectors/<source>`, not here. | CONFIRMED separation |
| Where do schemas live? | `schemas/contracts/v1/domains/hydrology/` is the segment-form path in Hydrology docs; `schemas/contracts/v1/hydrology/` is also referenced as a conflict. | CONFLICTED / NEEDS VERIFICATION |
| Where does policy live? | `policy/domains/hydrology/`, `policy/sensitivity/hydrology/`, `policy/rights/`, and `policy/release/` as applicable. | PROPOSED / NEEDS VERIFICATION |
| Where do outputs live? | Lifecycle homes under `data/`, not beside pipeline code. | CONFIRMED lifecycle posture |
| Can this lane publish? | No. It may prepare candidates, promotion decision stubs, and release handoffs only through governed workflow. | CONFIRMED doctrine posture |
| Can this lane issue flood warnings? | No. It can carry official-source context and redirects only. | CONFIRMED doctrine posture |

> [!IMPORTANT]
> Hydrology pipeline code is subordinate to source descriptors, source roles, rights, EvidenceBundle closure, temporal/freshness checks, NFHL/regulatory-context separation, sensitivity transforms, policy decisions, release manifests, correction notices, and rollback cards. A successful run is not public release and never authorizes emergency flood instruction.

[⬆ Back to top](#top)

---

## 3. Emergency-warning boundary

KFM Hydrology is not an emergency flood-warning system.

Every near-current or operational-context output must preserve:

- official source identity;
- observation time, valid time, retrieval time, and processing time;
- freshness or stale-state classification;
- source role and knowledge-character label;
- `not_for_life_safety: true` or equivalent policy flag where the output could be mistaken for current warning status;
- official-source redirect where the user needs current safety information;
- EvidenceBundle or source reference appropriate to the claim;
- finite policy outcome.

A Hydrology pipeline must fail closed when it cannot prove those fields for warning-adjacent, current-state, flood-context, or operational products.

Allowed behavior:

```text
Official or admitted hydrology source -> KFM context candidate -> freshness/source-role validation -> public-safe context + official redirect after release
```

Disallowed behavior:

```text
KFM candidate -> life-safety instruction
NFHL zone -> observed inundation
Modeled hydrograph -> observed gauge reading
Stale gauge record -> current flood state
Generated summary -> official flood warning
```

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable Hydrology-domain processing.

Appropriate contents include:

- fixture-only dry-run entrypoints for Hydrology pipeline behavior;
- hydrology-specific candidate builders;
- watershed, HUC, stream, reach, waterbody, gauge, well, and observation normalizers;
- gauge and hydrologic time-series normalization helpers;
- NFHL/regulatory-context processors that preserve regulatory source role;
- topology, upstream trace, and hydrologic identity helpers;
- model-output processors that preserve ModelRunReceipt-style provenance when applicable;
- source-role and NFHL anti-collapse validators;
- emergency-boundary and freshness validators;
- promotion decision stub emitters when governed by release validator contracts;
- public-safe geometry and sensitivity transform helpers, if not centralized elsewhere;
- quarantine routing helpers for stale, sensitive, unresolved, or over-precise material;
- catalog/triplet handoff helpers, if not centralized in `pipelines/catalog/`;
- receipt emitters, if not shared;
- thin adapters that read governed lifecycle inputs, not live source systems.

A good placement test:

> If the code transforms Hydrology lifecycle inputs into candidates, processed records, restricted catalog/triplet handoffs, receipts, promotion-decision stubs, or review handoffs, it may belong here. If it fetches source data, defines meaning, defines schema, encodes policy, stores lifecycle data, approves release, or issues emergency instructions, it belongs somewhere else — or nowhere in KFM.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Source fetchers / connectors | `connectors/<source>` |
| Source catalog profiles | `docs/sources/catalog/...` |
| Source descriptors / source registry entries | `data/registry/sources/hydrology/` or approved registry home |
| Hydrology architecture / doctrine | `docs/domains/hydrology/...` |
| Hydrology object meaning contracts | `contracts/domains/hydrology/`, `contracts/hydrology/`, or the accepted contract home after ADR/path resolution |
| JSON Schemas | `schemas/contracts/v1/domains/hydrology/`, `schemas/contracts/v1/hydrology/`, or the accepted schema home after ADR/path resolution |
| Policy bundles, sensitivity rules, release rules | `policy/domains/hydrology/`, `policy/sensitivity/hydrology/`, `policy/rights/`, `policy/release/` |
| Declarative run specs | `pipeline_specs/hydrology/...` |
| Fixtures | `fixtures/domains/hydrology/` or accepted fixture home |
| Tests | `tests/pipelines/domains/hydrology/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet, or published outputs | `data/...` lifecycle homes |
| Receipts and proofs | `data/receipts/...`, `data/proofs/...` |
| Release decisions and manifests | `release/candidates/hydrology/`, `release/manifests/hydrology/`, `release/rollback_cards/`, `release/correction_notices/` |
| Promotion decision validation schemas/tools | `schemas/`, `tools/validators/release/`, or accepted release validation home |
| Public API or map code | `apps/governed-api/`, `apps/explorer-web/`, `packages/ui/`, `packages/maplibre-runtime/` |
| Emergency warning issuance, evacuation instruction, or official current-state flood authority | Outside KFM; redirect to official authorities |

> [!WARNING]
> The previous scaffold wording allowed “docs, contracts, schemas, policies, fixtures, tests, packages, pipelines, registries, or data lifecycle artifacts” here. This README narrows the boundary: **only executable Hydrology pipeline logic belongs here.** The other responsibility roots remain separate authority surfaces.

[⬆ Back to top](#top)

---

## 6. Hydrology pipeline scope

Hydrology pipeline work may include these governed processing responsibilities:

| Scope area | Pipeline responsibility | Publication posture |
|---|---|---|
| Watersheds / HUCs | Normalize watershed units, identifiers, hierarchy, and source metadata. | Public only when source role, rights, and evidence close. |
| Streams / reaches / waterbodies | Normalize hydrographic identity, geometry, and topology. | Scale and source-vintage limits required. |
| Gauges / wells / sites | Normalize site identity and observation-site metadata. | Current-state displays require freshness handling. |
| Flow / stage / water-level observations | Normalize time series, units, qualifiers, and temporal scope. | Observations are not warnings or forecasts. |
| Water quality / aquifer observations | Normalize measurements, methods, units, and limits. | Method and evidence required before claims. |
| NFHL / regulatory context | Normalize regulatory flood-zone context and effective dates. | NFHL is not observed inundation. |
| Modeled hydrology | Prepare modeled hydrograph or derivative candidates. | Model output stays modeled and requires method receipts. |
| Topology / upstream traces | Build trace candidates and uncertainty notes. | Derived; needs method and graph provenance. |
| Cross-lane water links | Prepare water-use, drought, irrigation, habitat, geology, soil, hazards, agriculture, or infrastructure joins. | Other domains keep ownership; joins are derived. |
| Catalog/triplet handoff | Prepare restricted or public-safe catalog/graph candidates after evidence closure. | Does not replace canonical review state. |
| Promotion decision stub | Emit governed promotion-decision candidate only if release validator contract is satisfied. | Not a release decision by itself. |

[⬆ Back to top](#top)

---

## 7. Source-family posture

Hydrology pipeline code may consume only admitted or fixture-bound source material.

Candidate source families may include, subject to source descriptors, rights, freshness, and steward review:

- USGS water observation sources;
- WBD/HUC and watershed boundary sources;
- NHDPlus HR, 3DHP, or hydrographic network sources;
- FEMA NFHL or flood-regulatory context sources;
- terrain, elevation, and derived-flow context sources;
- groundwater, aquifer, well, and water-quality sources;
- hydrology-relevant state or local sources;
- geology, soil, agriculture, hazards, habitat, roads, settlements, infrastructure, atmosphere, and people/land context through governed joins;
- local upload or steward-curated material only through source-descriptor, rights, sensitivity, and review gates.

This README does not activate any source. Each source family requires SourceDescriptor coverage, source role, rights posture, sensitivity classification, attribution, fixtures, validation, and review routing before use.

[⬆ Back to top](#top)

---

## 8. Lifecycle contract

Every Hydrology pipeline must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal Hydrology pipeline stance:

1. **Read** approved fixtures, immutable raw captures, work candidates, quarantine inputs in remediation mode, or prior processed baselines.
2. **Normalize** into work candidates with source role, rights, temporal scope, spatial scope, unit/method posture, freshness state, knowledge-character label, sensitivity posture, evidence references, and public-safe geometry handling.
3. **Quarantine** unresolved rights, source-role mismatch, schema drift, sensitivity risk, unit ambiguity, missing freshness/valid-time state, NFHL/observed-flood collapse, over-precise geometry, stale warning-adjacent context, or validation failure.
4. **Promote to processed** only after validation, policy, evidence, freshness, sensitivity/public-safe transform, review, and reviewer gates appropriate to significance.
5. **Prepare catalog/triplet handoffs** only after processed-state and evidence closure, and only with sensitivity-safe payloads.
6. **Prepare promotion-decision stubs** only as candidates for release validation, not as release decisions.
7. **Publish** only through release decisions, public-safe artifacts, rollback targets, and correction paths.

Do not treat a move from one lifecycle folder to another as promotion. Promotion is a governed state transition with receipts and review evidence.

[⬆ Back to top](#top)

---

## 9. Required gates

Every Hydrology pipeline run must check or explicitly fail closed on:

1. **Source descriptor gate** — every input has stable source identity, role, cadence, rights, and sensitivity posture.
2. **Source-role gate** — observed, regulatory, modeled, administrative, aggregate, candidate, and synthetic records are not silently collapsed.
3. **Emergency boundary gate** — KFM never issues flood warnings, instructions, evacuation advice, or emergency determinations.
4. **NFHL/regulatory-context gate** — NFHL and regulatory zones remain regulatory context and are never emitted as observed flooding.
5. **Observation/model gate** — observed gauge readings, modeled hydrographs, reconstructions, forecasts, and operational context remain distinct.
6. **Freshness/staleness gate** — stale near-current products are marked stale, held, redirected, or denied.
7. **Unit and qualifier gate** — units, vertical datum where applicable, measurement method, qualifiers, and time basis are explicit.
8. **Rights gate** — unknown or restrictive license, permission, attribution, or redistribution terms block public release.
9. **Sensitivity gate** — private wells, infrastructure exposure, water-use sensitivity, living-person/land joins, archaeology/cultural overlays, sensitive ecology, and security-relevant joins fail closed.
10. **Public-safe geometry gate** — public products require approved generalization, redaction, aggregation, delay, restriction, or denial decisions with receipts.
11. **Scale and uncertainty gate** — method, confidence, uncertainty, spatial resolution, vertical datum, and source-vintage are recorded.
12. **Topology gate** — upstream/downstream traces and graph-derived paths preserve method and topology provenance.
13. **Review gate** — required steward or domain review state is recorded before promotion beyond candidate or quarantine where applicable.
14. **Schema gate** — candidate and processed records match approved schemas.
15. **Contract gate** — object meanings match Hydrology contracts and do not invent new semantics silently.
16. **Evidence gate** — claim-bearing outputs resolve EvidenceBundle support or abstain.
17. **Temporal gate** — observation, valid, forecast, issue, expiry, retrieval, processing, catalog, and release times remain distinct.
18. **Spatial gate** — CRS, geometry precision, aggregation/generalization method, hydrologic topology, and public-safe transforms are recorded.
19. **Policy gate** — policy decisions are finite and recorded; no silent allow.
20. **Validation gate** — validators exercise pass, fail, restrict, abstain, deny, and error paths, not only success.
21. **Receipt gate** — every run records input refs, versions, parameters, transforms, hashes, output refs, and outcomes.
22. **No-direct-publish gate** — no writes to public UI, public API, or `data/published/` without release workflow authority.
23. **Catalog/triplet gate** — catalog and graph projections preserve provenance and do not replace canonical records or review state.
24. **Promotion-decision gate** — promotion stubs are release-validation inputs only and must be validated by the release validator before any release workflow can consume them.
25. **Release gate** — public release requires ReleaseManifest, rollback target, correction path, and review state.

[⬆ Back to top](#top)

---

## 10. Sensitivity, source-role separation, and public-safe posture

Hydrology is fail-closed where output could be mistaken for current warning authority, expose sensitive water infrastructure/private wells, or overinterpret regulatory/model context.

Default posture:

- KFM is not an emergency flood-warning or life-safety instruction system;
- official warnings, watches, forecasts, and advisories redirect to official authorities;
- stale near-current hydrology material is withheld, marked stale, redirected, or denied;
- observed gauge readings, regulatory NFHL zones, modeled hydrographs, forecasts, administrative declarations, and generated summaries remain distinct;
- public products must preserve source role, units, temporal basis, method, uncertainty, freshness, and EvidenceBundle support;
- sensitive exact geometry and high-risk joins are generalized, redacted, delayed, restricted, aggregated, or withheld where needed;
- generated summaries cannot replace evidence, source role, freshness, official-source redirect, transform receipts, policy, or release state;
- outputs that could imply unsupported current flood status, water-rights/usage inference, private-well status, infrastructure vulnerability, regulatory determination, or emergency condition must abstain, deny, quarantine, or require reviewer handoff.

[⬆ Back to top](#top)

---

## 11. Directory contract

Recommended shape:

```text
pipelines/domains/hydrology/
├── README.md                         # this file
├── PIPELINE_CONTRACT.md              # PROPOSED: Hydrology execution contract
├── promote.py                        # EXISTING / NEEDS VERIFICATION: promotion decision stub emitter
├── run_dry_fixture.py                # PROPOSED if repo Python convention is accepted
├── normalize_watershed.py            # PROPOSED
├── normalize_hydro_feature.py        # PROPOSED
├── normalize_gauge_site.py           # PROPOSED
├── normalize_flow_observation.py     # PROPOSED
├── normalize_water_level.py          # PROPOSED
├── normalize_water_quality.py        # PROPOSED
├── normalize_nfhl_context.py         # PROPOSED
├── build_upstream_trace.py           # PROPOSED
├── validate_source_role_anticollapse.py # PROPOSED
├── validate_nfhl_not_observed_flood.py # PROPOSED
├── validate_freshness_boundary.py    # PROPOSED
├── apply_public_safe_geometry.py     # PROPOSED; may belong in shared tools if reused
├── build_catalog_handoff.py          # PROPOSED if not centralized in pipelines/catalog/
├── validate_hydrology_candidate.py   # PROPOSED wrapper if not centralized in tools/
├── emit_receipt.py                   # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/hydrology/
├── README.md                         # PROPOSED / NEEDS VERIFICATION
├── watershed_dry_run.yaml            # PROPOSED
├── gauge_observation_dry_run.yaml    # PROPOSED
├── nfhl_context_dry_run.yaml         # PROPOSED
├── source_role_anticollapse.yaml     # PROPOSED
├── public_safe_geometry.yaml         # PROPOSED; policy ownership must be resolved
└── catalog_handoff.yaml              # PROPOSED
```

Generated outputs must not be written beside the code that generated them. Use lifecycle homes under `data/`, proof homes under `data/proofs/`, receipt homes under `data/receipts/`, and release homes under `release/`.

[⬆ Back to top](#top)

---

## 12. Inputs and outputs

### Inputs

| Input class | Allowed source | Required condition |
|---|---|---|
| No-network fixture | `fixtures/domains/hydrology/` or accepted fixture home | Synthetic, generalized, stale-marked, or redacted where needed. |
| Raw hydrology capture | `data/raw/hydrology/<source_id>/<run_id>/` | Immutable source-edge capture with source descriptor, checksums, and ingest receipt. |
| Work candidate | `data/work/hydrology/<run_id>/` | Candidate-only; not public. |
| Quarantine input | `data/quarantine/hydrology/<reason>/<run_id>/` | Audit/remediation mode only. |
| Prior processed baseline | `data/processed/hydrology/<dataset_id>/<version>/` | Validated restricted baseline for diff/supersession. |
| Source registry / descriptor | `data/registry/sources/hydrology/`, `docs/sources/catalog/...` | Source role, rights, cadence, attribution, sensitivity. |
| Cross-lane context | Hazards, Geology, Soil, Agriculture, Habitat, Flora, Fauna, Roads, Settlements, Infrastructure, Atmosphere, People/Land, or other lifecycle homes | Must preserve source role and domain ownership. |
| Release validation contract | `tools/validators/release/validate_promotion_decision.py` and its accepted fixtures | Required before any promotion decision stub is treated as valid. |
| Policy / schema / contract refs | `policy/`, `schemas/`, `contracts/` | Referenced by validators, not stored here. |

### Outputs

| Output class | Correct home | Notes |
|---|---|---|
| Hydrology work candidate | `data/work/hydrology/<run_id>/` | Candidate only. |
| Hydrology quarantine record | `data/quarantine/hydrology/<reason>/<run_id>/` | Failed, restricted, stale, unresolved, or unsafe material. |
| Hydrology processed dataset version | `data/processed/hydrology/<dataset_id>/<version>/` | Validated/restricted; not automatically public. |
| Public-safe catalog candidate | `data/catalog/domain/hydrology/...` or approved catalog home | After processed-state, transform, and evidence gates. |
| Triplet / graph delta | `data/triplets/hydrology/...` or approved graph-delta home | Projection; does not replace canonical truth or review state. |
| Freshness / NFHL anti-collapse / public-safe transform receipt | `data/receipts/...` or approved receipt/proof home | Required for warning-adjacent or public-safe derivatives. |
| Run receipt | `data/receipts/pipeline/...` | Process memory, not release proof. |
| Evidence / validation proof | `data/proofs/...` | EvidenceBundle, validation reports, proof packs. |
| Promotion decision candidate | `release/promotion_decisions/hydrology/` | Candidate/stub only; must pass release validator and review. |
| Release handoff | `release/candidates/hydrology/...` | Only through release workflow. |

[⬆ Back to top](#top)

---

## 13. Minimal hydrology pipeline candidate record

The final schema is not defined here. This example shows the minimum information a Hydrology pipeline candidate should preserve.

```yaml
schema_version: kfm.hydrology_pipeline_candidate.v1
candidate_id: hyd_<object_family>_<run_id>_<hash>
pipeline_id: domains.hydrology
run_id: run_YYYYMMDDThhmmssZ
status: WORK_CANDIDATE
object_family: <watershed|huc_unit|hydro_feature|reach_identity|gauge_site|groundwater_well|flow_observation|water_level_observation|water_quality_observation|nfhl_zone|upstream_trace|water_use_link|...>
source_inputs:
  - source_id: src_hydrology_example
    source_role: <observed|regulatory|modeled|aggregate|administrative|candidate|synthetic|restricted>
    lifecycle_ref: data/raw/hydrology/<source_id>/<run_id>/
    input_hash: sha256:<hash>
    rights_state: needs_review
knowledge_character:
  nfhl_is_observed_flooding: false
  modeled_hydrograph_is_observation: false
  operational_warning_is_kfm_instruction: false
  generated_summary_is_evidence: false
emergency_boundary:
  not_for_life_safety: true
  official_source_redirect_required: true
  kfm_is_warning_issuer: false
spatial_scope:
  geometry_ref: restricted_or_public_safe_ref
  public_precision: denied_until_public_safe_transform
temporal_scope:
  observed_at: null
  valid_start: null
  valid_end: null
  retrieved_at: YYYY-MM-DDThh:mm:ssZ
  processed_at: YYYY-MM-DDThh:mm:ssZ
freshness:
  state: needs_review
  current_display_allowed: false
method:
  transform_family: hydrology_candidate_normalization
  algorithm_version: <version>
  parameter_hash: sha256:<hash>
scale_and_uncertainty:
  source_scale: unknown
  vertical_datum: unknown
  confidence: needs_review
  limitations:
    - candidate_only
sensitivity:
  private_well_risk: needs_review
  infrastructure_exposure_risk: needs_review
  water_use_inference_risk: needs_review
  join_induced_risk: needs_review
  public_release_default: DENY_UNTIL_REVIEW
policy:
  outcome: ABSTAIN
  reason_code: EVIDENCE_OR_SOURCE_ROLE_NOT_RESOLVED
evidence:
  evidence_bundle_ref: null
  citation_state: ABSTAIN
outputs:
  candidate_record: data/work/hydrology/run_YYYYMMDDThhmmssZ/candidate.yml
  receipt: data/receipts/pipeline/hydrology/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 14. Promotion-gate slice

The previous scaffold recorded a promotion-gate slice:

```text
promote.py emits a hydrology promotion decision stub to release/promotion_decisions/hydrology/.
Validate fixtures with python tools/validators/release/validate_promotion_decision.py --fixtures.
```

This README preserves that as `NEEDS VERIFICATION` behavior and constrains it:

- a promotion-decision stub is not a release decision;
- it must carry input refs, run refs, policy outcome, EvidenceBundle refs or abstention reason, validation refs, rollback target expectation, and reviewer burden;
- it must pass the release validator before any release workflow consumes it;
- it must not write public artifacts;
- it must not bypass source-role, NFHL, freshness, sensitivity, evidence, catalog/triplet, or release gates.

[⬆ Back to top](#top)

---

## 15. Dry-run, tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic/generalized/stale-marked/redacted, and no-network** until source activation, rights review, freshness review, sensitivity review, source-role anti-collapse review, promotion-stub review, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/hydrology/
├── test_no_network_dry_run.py                  # PROPOSED
├── test_source_role_required.py                # PROPOSED
├── test_rights_unknown_denied.py               # PROPOSED
├── test_nfhl_not_observed_flooding.py          # PROPOSED
├── test_model_not_observation.py               # PROPOSED
├── test_stale_current_context_denied.py        # PROPOSED
├── test_kfm_not_warning_issuer.py              # PROPOSED
├── test_private_well_or_infrastructure_quarantine.py # PROPOSED
├── test_topology_method_required.py            # PROPOSED
├── test_promotion_stub_validates.py            # PROPOSED
├── test_missing_evidence_abstains.py           # PROPOSED
├── test_receipt_hashes.py                      # PROPOSED
└── test_no_direct_publish.py                   # PROPOSED
```

A dry run should prove:

- fixtures load without network access;
- every input has source identity and source role;
- unknown rights produce `ABSTAIN`, `DENY`, or quarantine;
- NFHL/regulatory context never becomes observed flooding;
- observed readings, modeled hydrographs, forecasts, and operational context remain distinct;
- KFM never emits flood-warning issuance, emergency instructions, or life-safety guidance;
- stale current-state outputs are denied, marked stale, or redirected;
- sensitive or over-precise geometry is withheld from public-safe outputs;
- missing EvidenceBundle support produces `ABSTAIN`;
- promotion decision stubs validate before release workflow consumption;
- invalid records fail validation;
- receipts include input hashes, method hashes, transform refs, freshness refs, output refs, and outcomes;
- no outputs are written to public UI, public API, `data/published/`, or release manifests by default.

[⬆ Back to top](#top)

---

## 16. Promotion, publication, correction, and rollback

Hydrology pipelines may prepare candidates. They do not publish.

Required promotion chain:

```text
hydrology source/work input
  -> hydrology candidate
  -> validation report
  -> policy decision
  -> NFHL anti-collapse / freshness / public-safe transform receipt where required
  -> EvidenceBundle closure
  -> processed hydrology dataset version
  -> catalog / triplet candidate
  -> promotion decision candidate where used
  -> release candidate
  -> ReleaseManifest
  -> RollbackCard
  -> public-safe artifact
```

Correction and rollback posture:

- denied, abstained, errored, stale, restricted, and quarantined runs remain auditable;
- candidate rollback preserves receipts and proof state;
- processed versions are superseded by governed state transition, not hidden overwrite;
- promotion decision candidates are invalidated if their input refs, evidence refs, policy refs, or validation refs drift;
- public artifact rollback is owned by `release/`, not by this directory;
- correction notices must point back to source, evidence, freshness state, NFHL anti-collapse checks, validation, catalog, release, and rollback state.

[⬆ Back to top](#top)

---

## 17. Definition of done

This README is done when it:

- replaces the greenfield scaffold with a usable Hydrology pipeline contract;
- preserves the existing promotion-gate slice as bounded `NEEDS VERIFICATION` behavior;
- identifies this directory as executable Hydrology pipeline logic only;
- corrects the boundary so docs, schemas, contracts, policy, fixtures, tests, data, registries, receipts, proofs, and release decisions do not live here;
- preserves source-role, NFHL anti-collapse, emergency-boundary, freshness, evidence, public-safe geometry, policy, lifecycle, catalog/triplet, promotion-stub, release, correction, and rollback boundaries;
- denies direct publication and emergency-warning behavior;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable Hydrology pipeline implementation is done only when it has:

- owners and review burden;
- source-descriptor coverage;
- synthetic/generalized/stale-marked/redacted no-network fixtures;
- schema-backed candidates;
- Hydrology contract conformance;
- rights, sensitivity, freshness, source-role, NFHL, topology, temporal, spatial, and evidence tests;
- deterministic receipts;
- validated promotion-decision stubs where used;
- no-direct-publish tests;
- CI coverage;
- steward-review handoff;
- release, correction, and rollback documentation.

[⬆ Back to top](#top)

---

## 18. Open questions

| ID | Question | Status |
|---|---|---|
| `HYD-PIPE-001` | Which Hydrology child modules should be implemented first: watersheds/HUCs, hydro features, gauges, observations, NFHL context, upstream traces, promotion decision stubs, or catalog handoff? | NEEDS VERIFICATION |
| `HYD-PIPE-002` | Which schema path is canonical for Hydrology: `schemas/contracts/v1/domains/hydrology/` or `schemas/contracts/v1/hydrology/`? | CONFLICTED / NEEDS ADR |
| `HYD-PIPE-003` | Which object family owns freshness, NFHL anti-collapse, topology, and public-safe transform receipts? | PROPOSED / NEEDS ADR |
| `HYD-PIPE-004` | Which source descriptors are first-wave approved for fixture-only dry runs? | NEEDS VERIFICATION |
| `HYD-PIPE-005` | Which CI job owns Hydrology pipeline invariant tests? | UNKNOWN |
| `HYD-PIPE-006` | Should catalog handoff logic live here or in centralized `pipelines/catalog/` with Hydrology adapters? | NEEDS VERIFICATION |
| `HYD-PIPE-007` | How should `release/promotion_decisions/hydrology/` relate to `release/candidates/hydrology/` and release manifests? | NEEDS VERIFICATION |
| `HYD-PIPE-008` | Which public-safe map/API products are allowed after review and release, and at what freshness/generalization level? | NEEDS VERIFICATION |
| `HYD-PIPE-009` | How should cross-lane joins with Hazards, Geology, Soil, Agriculture, Habitat, Roads, Settlements, Infrastructure, Atmosphere, People/Land, Flora, or Fauna be denied, restricted, or generalized? | NEEDS VERIFICATION |

---

## Maintainer note

Start with synthetic/generalized/stale-marked fixture-only dry runs and negative tests. Do not add live source fetching, current-state public flood displays, emergency-warning behavior, public private-well/infrastructure-exposure products, public map layers, release handoff automation, or direct API payload generation until source roles, rights, freshness, NFHL anti-collapse, public-safe transforms, evidence closure, promotion-stub validation, and rollback are proven.
