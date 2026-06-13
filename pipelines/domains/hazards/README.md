<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-hazards-readme
title: Hazards Domain Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <hazards-pipeline-owner>
  - <hazards-domain-steward>
  - <hydrology-domain-steward>
  - <atmosphere-domain-steward>
  - <settlements-infrastructure-steward>
  - <source-steward>
  - <evidence-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipelines/domains/hazards/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - docs/domains/hazards/ARCHITECTURE.md
  - docs/domains/hazards/DATA_LIFECYCLE.md
  - docs/domains/hazards/EXPANSION_BACKLOG.md
  - docs/domains/hazards/CONTINUITY_INVENTORY.md
  - docs/domains/hydrology/
  - docs/domains/atmosphere/
  - docs/domains/settlements-infrastructure/
  - docs/domains/roads-rail-trade/
  - pipeline_specs/hazards/
  - contracts/domains/hazards/
  - contracts/hazards/
  - schemas/contracts/v1/domains/hazards/
  - schemas/contracts/v1/hazards/
  - policy/domains/hazards/
  - policy/sensitivity/hazards/
  - data/raw/hazards/
  - data/work/hazards/
  - data/quarantine/hazards/
  - data/processed/hazards/
  - data/catalog/domain/hazards/
  - data/triplets/hazards/
  - data/published/layers/hazards/
  - data/registry/sources/hazards/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/hazards/
  - release/manifests/hazards/
tags:
  - kfm
  - pipelines
  - domains
  - hazards
  - severe-weather
  - flood
  - wildfire
  - smoke
  - drought
  - heat
  - earthquake
  - exposure
  - resilience
  - life-safety-boundary
  - evidence
  - policy
  - governance
notes:
  - "This README replaces the greenfield scaffold for pipelines/domains/hazards."
  - "Hazards pipeline logic is executable implementation support only; it does not own emergency alerts, life-safety instructions, official warnings, schemas, source descriptors, policy, lifecycle data, catalog truth, regulatory determinations, or release decisions."
  - "Hazards outputs must preserve knowledge-character separation between historical events, regulatory context, observations, remote-sensing detections, modeled derivatives, operational warning context, declarations, exposure summaries, and generated summaries."
  - "Operational warning/advisory/watch context is contextual only, must carry issue/expiry/freshness/source identity, and must redirect to official sources."
  - "Concrete executable behavior, source activation, schedules, CI coverage, schema paths, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# ⚠️ Hazards Domain Pipeline

> Executable Hazards-domain pipeline lane for converting admitted historical, regulatory, observational, remote-sensing, modeled, administrative, exposure, resilience, and operational-context source material into governed candidates, quarantine records, processed records, catalog/triplet handoffs, receipts, and release-review packages — **without acting as an emergency alert system or life-safety authority**.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-hazards%20domain%20pipeline-2e7d32)
![authority](https://img.shields.io/badge/authority-executable%20logic-0a7ea4)
![life-safety](https://img.shields.io/badge/life--safety-boundary%20required-d62728)
![publication](https://img.shields.io/badge/publication-release%20gated-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/hazards/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Hazards  
**Placement posture:** hazards child lane under `pipelines/domains/`; concrete executable behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Public posture:** no direct publication and no life-safety alerting; public output requires lifecycle, EvidenceBundle, source-role, freshness/expiry, sensitivity, policy, catalog/triplet, release, correction, and rollback closure

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Life-safety boundary](#3-life-safety-boundary)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Hazards pipeline scope](#6-hazards-pipeline-scope)
- [7. Source-family posture](#7-source-family-posture)
- [8. Lifecycle contract](#8-lifecycle-contract)
- [9. Required gates](#9-required-gates)
- [10. Sensitivity, knowledge-character separation, and public-safe posture](#10-sensitivity-knowledge-character-separation-and-public-safe-posture)
- [11. Directory contract](#11-directory-contract)
- [12. Inputs and outputs](#12-inputs-and-outputs)
- [13. Minimal hazards pipeline candidate record](#13-minimal-hazards-pipeline-candidate-record)
- [14. Dry-run, tests, fixtures, receipts, and proofs](#14-dry-run-tests-fixtures-receipts-and-proofs)
- [15. Promotion, publication, correction, and rollback](#15-promotion-publication-correction-and-rollback)
- [16. Definition of done](#16-definition-of-done)
- [17. Open questions](#17-open-questions)

---

## 1. Purpose

`pipelines/domains/hazards/` is the executable pipeline lane for Hazards-domain transformations.

It supports candidate processing for:

- historical hazard events, including severe weather, flood, wildfire, smoke, drought, earthquake, heat, cold, hail, wind, and tornado records;
- regulatory hazard context, including flood zones and comparable regulatory archives;
- scientific observations and remote-sensing detections;
- modeled derivatives, exposure summaries, resilience timelines, and risk-context candidates;
- operational warning, watch, and advisory context with issue time, expiry time, source identity, freshness state, and official-source redirect;
- administrative declarations and emergency-management context as administrative records;
- public-safe Hazards map products after evidence, policy, and release review;
- catalog, graph, Evidence Drawer, and Focus Mode handoff packages.

This directory implements or will implement the **how** of Hazards processing. It does not define Hazards object meaning, schemas, policy, source descriptors, emergency warnings, life-safety instructions, regulatory determinations, lifecycle storage, catalog truth, or release approval.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/hazards/`? | Hazards is a domain lane under the domain-pipeline umbrella. | CONFIRMED path responsibility pattern; executable behavior NEEDS VERIFICATION |
| Where do declarative specs live? | `pipeline_specs/hazards/` or accepted spec home. | PROPOSED / NEEDS VERIFICATION |
| Where do source fetchers live? | `connectors/<source>`, not here. | CONFIRMED separation |
| Where do schemas live? | `schemas/contracts/v1/hazards/` is called out in Hazards architecture; `schemas/contracts/v1/domains/hazards/` also appears in segment-pattern docs. This is CONFLICTED pending ADR/path decision. | CONFLICTED / NEEDS VERIFICATION |
| Where does policy live? | `policy/domains/hazards/`, `policy/sensitivity/hazards/`, `policy/rights/`, and `policy/release/` as applicable. | PROPOSED / NEEDS VERIFICATION |
| Where do outputs live? | Lifecycle homes under `data/`, not beside pipeline code. | CONFIRMED lifecycle posture |
| Can this lane publish? | No. It may prepare candidates and release handoffs only through governed workflow. | CONFIRMED doctrine posture |
| Can this lane issue alerts? | No. It can carry official-source context and redirects only. | CONFIRMED doctrine posture |

> [!IMPORTANT]
> Hazards pipeline code is subordinate to source descriptors, source roles, rights, EvidenceBundle closure, freshness/expiry checks, knowledge-character labels, sensitivity transforms, policy decisions, release manifests, correction notices, and rollback cards. A successful run is not public release and never authorizes emergency instruction.

[⬆ Back to top](#top)

---

## 3. Life-safety boundary

KFM Hazards is not an emergency alerting system.

Every operational-context output must preserve:

- official source identity;
- issue time;
- expiry time or valid-through state;
- retrieval and processing time;
- freshness status;
- `not_for_life_safety: true` or equivalent policy flag;
- official-source redirect;
- EvidenceBundle or source reference appropriate to the claim;
- finite policy outcome.

A Hazards pipeline must fail closed when it cannot prove those fields for operational warning, watch, or advisory context.

Allowed behavior:

```text
Official hazard source -> KFM context candidate -> freshness/expiry validation -> public-safe context + official redirect after release
```

Disallowed behavior:

```text
KFM candidate -> life-safety instruction
KFM model output -> emergency alert
KFM generated summary -> official warning
KFM stale record -> current hazard state
```

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable Hazards-domain processing.

Appropriate contents include:

- fixture-only dry-run entrypoints for Hazards pipeline behavior;
- hazards-specific candidate builders;
- historical event normalizers;
- regulatory-context normalizers;
- remote-sensing and scientific-observation normalizers;
- modeled-derivative and exposure-summary builders;
- operational-context processors that preserve freshness, expiry, and official-source redirect;
- knowledge-character separation validators;
- life-safety-boundary validators;
- public-safe geometry and sensitivity transform helpers, if not centralized elsewhere;
- quarantine routing helpers for stale, sensitive, unresolved, or over-precise material;
- catalog/triplet handoff helpers, if not centralized in `pipelines/catalog/`;
- receipt emitters, if not shared;
- thin adapters that read governed lifecycle inputs, not live source systems.

A good placement test:

> If the code transforms Hazards lifecycle inputs into candidates, processed records, restricted catalog/triplet handoffs, receipts, or review handoffs, it may belong here. If it fetches source data, defines meaning, defines schema, encodes policy, stores lifecycle data, approves release, or issues emergency instructions, it belongs somewhere else — or nowhere in KFM.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Source fetchers / connectors | `connectors/<source>` |
| Source catalog profiles | `docs/sources/catalog/...` |
| Source descriptors / source registry entries | `data/registry/sources/hazards/` or approved registry home |
| Hazards architecture / doctrine | `docs/domains/hazards/...` |
| Hazards object meaning contracts | `contracts/hazards/`, `contracts/domains/hazards/`, or the accepted contract home after ADR/path resolution |
| JSON Schemas | `schemas/contracts/v1/hazards/`, `schemas/contracts/v1/domains/hazards/`, or the accepted schema home after ADR/path resolution |
| Policy bundles, sensitivity rules, release rules | `policy/domains/hazards/`, `policy/sensitivity/hazards/`, `policy/rights/`, `policy/release/` |
| Declarative run specs | `pipeline_specs/hazards/...` |
| Fixtures | `fixtures/domains/hazards/` or accepted fixture home |
| Tests | `tests/pipelines/domains/hazards/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet, or published outputs | `data/...` lifecycle homes |
| Receipts and proofs | `data/receipts/...`, `data/proofs/...` |
| Release decisions | `release/candidates/hazards/`, `release/manifests/hazards/`, `release/rollback_cards/`, `release/correction_notices/` |
| Public API or map code | `apps/governed-api/`, `apps/explorer-web/`, `packages/ui/`, `packages/maplibre-runtime/` |
| Emergency alerting, dispatch, paging, warning issuance, evacuation instruction, or official current-state authority | Outside KFM; redirect to official authorities |

> [!WARNING]
> The previous scaffold wording allowed “docs, contracts, schemas, policies, fixtures, tests, packages, pipelines, registries, or data lifecycle artifacts” here. This README narrows the boundary: **only executable Hazards pipeline logic belongs here.** The other responsibility roots remain separate authority surfaces.

[⬆ Back to top](#top)

---

## 6. Hazards pipeline scope

Hazards pipeline work may include these governed processing responsibilities:

| Scope area | Pipeline responsibility | Publication posture |
|---|---|---|
| Historical events | Normalize event records, source roles, time windows, impacts, and evidence. | Public only when source role, rights, and evidence close. |
| Regulatory context | Normalize regulatory hazard boundaries and effective dates. | Regulatory context, not observed event truth. |
| Operational context | Carry warnings, watches, advisories, issue/expiry, and official redirects. | Not-for-life-safety; freshness required. |
| Scientific observations | Normalize sensor, station, seismic, fire, smoke, or other observations. | Observation truth remains distinct from warning state. |
| Remote-sensing detections | Normalize detections and uncertainty. | Detection is not verified incident unless evidence closes. |
| Modeled derivatives | Prepare modeled risk, exposure, or susceptibility candidates. | Model output is not observed event or official determination. |
| Exposure summaries | Compose released or governed assets with hazard context. | Derived and sensitivity-reviewed. |
| Administrative declarations | Normalize declarations and authority metadata. | Administrative status, not physical observation. |
| Resilience timelines | Prepare evidence-backed history and recovery context. | Interpretive; cite-or-abstain. |
| Catalog/triplet handoff | Prepare restricted or public-safe catalog/graph candidates after evidence closure. | Does not replace canonical review state. |

[⬆ Back to top](#top)

---

## 7. Source-family posture

Hazards pipeline code may consume only admitted or fixture-bound source material.

Candidate source families may include, subject to source descriptors, rights, freshness, and steward review:

- official weather, warning, advisory, and watch context;
- FEMA and state/local regulatory hazard or declaration archives;
- historical severe-weather, flood, fire, drought, smoke, earthquake, heat, and storm records;
- scientific observation feeds and catalogs;
- satellite and remote-sensing detection products;
- modeled hazard, exposure, susceptibility, and resilience products;
- hydrology, atmosphere, geology, soil, agriculture, roads, settlements, infrastructure, archaeology, people/land, flora, fauna, and habitat context through governed joins;
- local upload or steward-curated material only through source-descriptor, rights, sensitivity, and review gates.

This README does not activate any source. Each source family requires SourceDescriptor coverage, source role, rights posture, sensitivity classification, attribution, fixtures, validation, and review routing before use.

[⬆ Back to top](#top)

---

## 8. Lifecycle contract

Every Hazards pipeline must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal Hazards pipeline stance:

1. **Read** approved fixtures, immutable raw captures, work candidates, quarantine inputs in remediation mode, or prior processed baselines.
2. **Normalize** into work candidates with source role, rights, temporal scope, spatial scope, freshness/expiry where applicable, knowledge-character label, sensitivity posture, evidence references, and public-safe geometry handling.
3. **Quarantine** unresolved rights, source-role mismatch, schema drift, sensitivity risk, missing freshness/expiry, missing not-for-life-safety flag, over-precise geometry, stale operational context, or validation failure.
4. **Promote to processed** only after validation, policy, evidence, freshness, sensitivity/public-safe transform, review, and reviewer gates appropriate to significance.
5. **Prepare catalog/triplet handoffs** only after processed-state and evidence closure, and only with sensitivity-safe payloads.
6. **Publish** only through release decisions, public-safe artifacts, rollback targets, and correction paths.

Do not treat a move from one lifecycle folder to another as promotion. Promotion is a governed state transition with receipts and review evidence.

[⬆ Back to top](#top)

---

## 9. Required gates

Every Hazards pipeline run must check or explicitly fail closed on:

1. **Source descriptor gate** — every input has stable source identity, role, cadence, rights, and sensitivity posture.
2. **Source-role gate** — historical, regulatory, observed, modeled, administrative, operational, aggregate, candidate, and synthetic records are not silently collapsed.
3. **Life-safety boundary gate** — KFM never issues warnings, instructions, evacuation advice, or emergency determinations.
4. **Operational-context gate** — warning/watch/advisory context must carry issue time, expiry/valid-through, freshness, official source, redirect, and not-for-life-safety marker.
5. **Knowledge-character gate** — event, regulatory context, observation, detection, model, exposure summary, declaration, and generated summary remain distinct.
6. **Rights gate** — unknown or restrictive license, permission, attribution, or redistribution terms block public release.
7. **Sensitivity gate** — infrastructure exposure, private impacts, living-person data, archaeology/cultural overlays, sensitive ecology, and security-relevant joins fail closed.
8. **Public-safe geometry gate** — public products require approved generalization, redaction, aggregation, delay, restriction, or denial decisions with receipts.
9. **Freshness/staleness gate** — stale operational or near-current products are marked stale, held, redirected, or denied.
10. **Scale and uncertainty gate** — method, confidence, uncertainty, spatial resolution, and source-vintage are recorded.
11. **Review gate** — required steward or domain review state is recorded before promotion beyond candidate or quarantine where applicable.
12. **Schema gate** — candidate and processed records match approved schemas.
13. **Contract gate** — object meanings match Hazards contracts and do not invent new semantics silently.
14. **Evidence gate** — claim-bearing outputs resolve EvidenceBundle support or abstain.
15. **Temporal gate** — event, issue, expiry, observed, valid, retrieval, processing, catalog, and release times remain distinct.
16. **Spatial gate** — CRS, geometry precision, aggregation/generalization method, and public-safe transforms are recorded.
17. **Policy gate** — policy decisions are finite and recorded; no silent allow.
18. **Validation gate** — validators exercise pass, fail, restrict, abstain, deny, and error paths, not only success.
19. **Receipt gate** — every run records input refs, versions, parameters, transforms, hashes, output refs, and outcomes.
20. **No-direct-publish gate** — no writes to public UI, public API, or `data/published/` without release workflow authority.
21. **Catalog/triplet gate** — catalog and graph projections preserve provenance and do not replace canonical records or review state.
22. **Release gate** — public release requires ReleaseManifest, rollback target, correction path, and review state.

[⬆ Back to top](#top)

---

## 10. Sensitivity, knowledge-character separation, and public-safe posture

Hazards is fail-closed where output could be mistaken for official current-state authority, expose sensitive places or people, or overinterpret context.

Default posture:

- KFM is not an emergency alerting or life-safety instruction system;
- operational context always redirects to official authorities;
- stale operational material is withheld, marked stale, redirected, or denied;
- historical events, regulatory context, observations, detections, models, declarations, and exposure summaries remain distinct;
- public products must preserve source role, scale, method, uncertainty, freshness, and EvidenceBundle support;
- sensitive exact geometry and high-risk joins are generalized, redacted, delayed, restricted, aggregated, or withheld where needed;
- generated summaries cannot replace evidence, source role, freshness, official-source redirect, transform receipts, policy, or release state;
- outputs that could imply unsupported warning status, personal impact, infrastructure vulnerability, regulatory determination, or current emergency condition must abstain, deny, quarantine, or require reviewer handoff.

[⬆ Back to top](#top)

---

## 11. Directory contract

Recommended shape:

```text
pipelines/domains/hazards/
├── README.md                         # this file
├── PIPELINE_CONTRACT.md              # PROPOSED: Hazards execution contract
├── run_dry_fixture.py                # PROPOSED if repo Python convention is accepted
├── normalize_historical_event.py     # PROPOSED
├── normalize_regulatory_context.py   # PROPOSED
├── normalize_operational_context.py  # PROPOSED
├── normalize_remote_sensing_detection.py # PROPOSED
├── build_exposure_summary.py         # PROPOSED
├── validate_life_safety_boundary.py  # PROPOSED
├── validate_knowledge_character.py   # PROPOSED
├── validate_freshness_expiry.py      # PROPOSED
├── apply_public_safe_geometry.py     # PROPOSED; may belong in shared tools if reused
├── build_catalog_handoff.py          # PROPOSED if not centralized in pipelines/catalog/
├── validate_hazards_candidate.py     # PROPOSED wrapper if not centralized in tools/
├── emit_receipt.py                   # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/hazards/
├── README.md                         # PROPOSED / NEEDS VERIFICATION
├── historical_event_dry_run.yaml     # PROPOSED
├── regulatory_context_dry_run.yaml   # PROPOSED
├── operational_context_dry_run.yaml  # PROPOSED
├── life_safety_boundary.yaml         # PROPOSED
├── freshness_expiry_checks.yaml      # PROPOSED
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
| No-network fixture | `fixtures/domains/hazards/` or accepted fixture home | Synthetic, generalized, stale-marked, or redacted where needed. |
| Raw hazards capture | `data/raw/hazards/<source_id>/<run_id>/` | Immutable source-edge capture with source descriptor, checksums, and ingest receipt. |
| Work candidate | `data/work/hazards/<run_id>/` | Candidate-only; not public. |
| Quarantine input | `data/quarantine/hazards/<reason>/<run_id>/` | Audit/remediation mode only. |
| Prior processed baseline | `data/processed/hazards/<dataset_id>/<version>/` | Validated restricted baseline for diff/supersession. |
| Source registry / descriptor | `data/registry/sources/hazards/`, `docs/sources/catalog/...` | Source role, rights, cadence, attribution, sensitivity. |
| Cross-lane context | Hydrology, Atmosphere, Geology, Soil, Agriculture, Roads, Settlements, Infrastructure, Archaeology, People/Land, Flora, Fauna, Habitat, or other lifecycle homes | Must preserve source role and domain ownership. |
| Policy / schema / contract refs | `policy/`, `schemas/`, `contracts/` | Referenced by validators, not stored here. |

### Outputs

| Output class | Correct home | Notes |
|---|---|---|
| Hazards work candidate | `data/work/hazards/<run_id>/` | Candidate only. |
| Hazards quarantine record | `data/quarantine/hazards/<reason>/<run_id>/` | Failed, restricted, stale, unresolved, or unsafe material. |
| Hazards processed dataset version | `data/processed/hazards/<dataset_id>/<version>/` | Validated/restricted; not automatically public. |
| Public-safe catalog candidate | `data/catalog/domain/hazards/...` or approved catalog home | After processed-state, transform, and evidence gates. |
| Triplet / graph delta | `data/triplets/hazards/...` or approved graph-delta home | Projection; does not replace canonical truth or review state. |
| Freshness / expiry / life-safety-boundary receipt | `data/receipts/...` or approved receipt/proof home | Required for operational-context derivatives. |
| Run receipt | `data/receipts/pipeline/...` | Process memory, not release proof. |
| Evidence / validation proof | `data/proofs/...` | EvidenceBundle, validation reports, proof packs. |
| Release handoff | `release/candidates/hazards/...` | Only through release workflow. |

[⬆ Back to top](#top)

---

## 13. Minimal hazards pipeline candidate record

The final schema is not defined here. This example shows the minimum information a Hazards pipeline candidate should preserve.

```yaml
schema_version: kfm.hazards_pipeline_candidate.v1
candidate_id: haz_<object_family>_<run_id>_<hash>
pipeline_id: domains.hazards
run_id: run_YYYYMMDDThhmmssZ
status: WORK_CANDIDATE
object_family: <historical_event|regulatory_context|operational_warning_context|operational_watch_context|operational_advisory_context|remote_sensing_detection|modeled_derivative|exposure_summary|administrative_declaration|...>
source_inputs:
  - source_id: src_hazards_example
    source_role: <historical|regulatory|observed|operational|modeled|administrative|aggregate|candidate|synthetic|restricted>
    lifecycle_ref: data/raw/hazards/<source_id>/<run_id>/
    input_hash: sha256:<hash>
    rights_state: needs_review
knowledge_character:
  historical_event_is_current_warning: false
  regulatory_context_is_observed_event: false
  model_output_is_observation: false
  generated_summary_is_evidence: false
life_safety_boundary:
  not_for_life_safety: true
  official_source_redirect_required: true
  kfm_is_alert_issuer: false
operational_context:
  issue_time: null
  expiry_time: null
  freshness_state: not_applicable
  official_source_ref: null
spatial_scope:
  geometry_ref: restricted_or_public_safe_ref
  public_precision: denied_until_public_safe_transform
temporal_scope:
  event_start: null
  event_end: null
  observed_at: null
  retrieved_at: YYYY-MM-DDThh:mm:ssZ
  processed_at: YYYY-MM-DDThh:mm:ssZ
method:
  transform_family: hazards_candidate_normalization
  algorithm_version: <version>
  parameter_hash: sha256:<hash>
scale_and_uncertainty:
  source_scale: unknown
  confidence: needs_review
  limitations:
    - candidate_only
sensitivity:
  infrastructure_exposure_risk: needs_review
  personal_impact_risk: needs_review
  join_induced_risk: needs_review
  public_release_default: DENY_UNTIL_REVIEW
policy:
  outcome: ABSTAIN
  reason_code: EVIDENCE_OR_FRESHNESS_NOT_RESOLVED
evidence:
  evidence_bundle_ref: null
  citation_state: ABSTAIN
outputs:
  candidate_record: data/work/hazards/run_YYYYMMDDThhmmssZ/candidate.yml
  receipt: data/receipts/pipeline/hazards/run_YYYYMMDDThhmmssZ.yml
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 14. Dry-run, tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic/generalized/stale-marked/redacted, and no-network** until source activation, rights review, freshness review, sensitivity review, life-safety-boundary review, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/hazards/
├── test_no_network_dry_run.py                  # PROPOSED
├── test_source_role_required.py                # PROPOSED
├── test_rights_unknown_denied.py               # PROPOSED
├── test_kfm_not_alert_issuer.py                # PROPOSED
├── test_operational_context_requires_expiry.py # PROPOSED
├── test_stale_current_context_denied.py        # PROPOSED
├── test_regulatory_not_observed_event.py       # PROPOSED
├── test_model_not_observation.py               # PROPOSED
├── test_sensitive_join_quarantines.py          # PROPOSED
├── test_missing_evidence_abstains.py           # PROPOSED
├── test_receipt_hashes.py                      # PROPOSED
└── test_no_direct_publish.py                   # PROPOSED
```

A dry run should prove:

- fixtures load without network access;
- every input has source identity and source role;
- unknown rights produce `ABSTAIN`, `DENY`, or quarantine;
- operational context carries official source, issue time, expiry/valid-through, freshness state, and not-for-life-safety marker;
- KFM never emits alert issuance, emergency instructions, or life-safety guidance;
- historical, regulatory, observation, detection, model, declaration, exposure, and generated summary states remain distinct;
- sensitive or over-precise geometry is withheld from public-safe outputs;
- missing EvidenceBundle support produces `ABSTAIN`;
- steward review and public-safe transform receipts are required where sensitivity is unresolved;
- invalid records fail validation;
- receipts include input hashes, method hashes, transform refs, freshness refs, output refs, and outcomes;
- no outputs are written to public UI, public API, `data/published/`, or release manifests by default.

[⬆ Back to top](#top)

---

## 15. Promotion, publication, correction, and rollback

Hazards pipelines may prepare candidates. They do not publish.

Required promotion chain:

```text
hazards source/work input
  -> hazards candidate
  -> validation report
  -> policy decision
  -> freshness / expiry / life-safety-boundary receipt where required
  -> public-safe transform receipt where required
  -> EvidenceBundle closure
  -> processed hazards dataset version
  -> catalog / triplet candidate
  -> release candidate
  -> ReleaseManifest
  -> RollbackCard
  -> public-safe artifact
```

Correction and rollback posture:

- denied, abstained, errored, stale, restricted, and quarantined runs remain auditable;
- candidate rollback preserves receipts and proof state;
- processed versions are superseded by governed state transition, not hidden overwrite;
- public artifact rollback is owned by `release/`, not by this directory;
- correction notices must point back to source, evidence, freshness/expiry state, life-safety-boundary checks, validation, catalog, release, and rollback state.

[⬆ Back to top](#top)

---

## 16. Definition of done

This README is done when it:

- replaces the greenfield scaffold with a usable Hazards pipeline contract;
- identifies this directory as executable Hazards pipeline logic only;
- corrects the boundary so docs, schemas, contracts, policy, fixtures, tests, data, registries, receipts, proofs, and release decisions do not live here;
- preserves source-role, knowledge-character separation, freshness/expiry, evidence, public-safe geometry, policy, lifecycle, catalog/triplet, release, correction, and rollback boundaries;
- denies direct publication and life-safety alerting behavior;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable Hazards pipeline implementation is done only when it has:

- owners and review burden;
- source-descriptor coverage;
- synthetic/generalized/stale-marked/redacted no-network fixtures;
- schema-backed candidates;
- Hazards contract conformance;
- rights, sensitivity, freshness, expiry, knowledge-character, temporal, spatial, and evidence tests;
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
| `HAZ-PIPE-001` | Which Hazards child modules should be implemented first: historical events, regulatory context, operational context, freshness/expiry checks, life-safety-boundary checks, exposure summaries, or catalog handoff? | NEEDS VERIFICATION |
| `HAZ-PIPE-002` | Which schema path is canonical for Hazards: `schemas/contracts/v1/hazards/` or `schemas/contracts/v1/domains/hazards/`? | CONFLICTED / NEEDS ADR |
| `HAZ-PIPE-003` | Which object family owns freshness, expiry, life-safety-boundary, and official-source redirect receipts? | PROPOSED / NEEDS ADR |
| `HAZ-PIPE-004` | Which source descriptors are first-wave approved for fixture-only dry runs? | NEEDS VERIFICATION |
| `HAZ-PIPE-005` | Which CI job owns Hazards pipeline invariant tests? | UNKNOWN |
| `HAZ-PIPE-006` | Should catalog handoff logic live here or in centralized `pipelines/catalog/` with Hazards adapters? | NEEDS VERIFICATION |
| `HAZ-PIPE-007` | Which public-safe map/API products are allowed after review and release, and at what freshness/generalization level? | NEEDS VERIFICATION |
| `HAZ-PIPE-008` | How should cross-lane joins with Hydrology, Atmosphere, Settlements, Roads, Geology, Soil, Agriculture, Archaeology, People/Land, Flora, Fauna, or Habitat be denied, restricted, or generalized? | NEEDS VERIFICATION |

---

## Maintainer note

Start with synthetic/generalized/stale-marked fixture-only dry runs and negative tests. Do not add live source fetching, current-state public displays, official-alert behavior, public emergency guidance, public infrastructure-exposure products, public map layers, release handoff automation, or direct API payload generation until source roles, rights, freshness/expiry checks, life-safety-boundary checks, public-safe transforms, evidence closure, and rollback are proven.
