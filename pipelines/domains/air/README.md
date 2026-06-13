<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-air-readme
title: Air Domain Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <air-atmosphere-pipeline-owner>
  - <atmosphere-domain-steward>
  - <source-steward>
  - <evidence-steward>
  - <policy-steward>
  - <release-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public
path: pipelines/domains/air/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - docs/domains/atmosphere/README.md
  - docs/domains/atmosphere/DATA_LIFECYCLE.md
  - docs/domains/atmosphere/SOURCE_REGISTRY.md
  - docs/domains/atmosphere/CANONICAL_PATHS.md
  - docs/domains/atmosphere/API_CONTRACTS.md
  - pipeline_specs/atmosphere/
  - pipeline_specs/air/
  - contracts/domains/atmosphere/
  - schemas/contracts/v1/domains/atmosphere/
  - policy/domains/atmosphere/
  - data/raw/atmosphere/
  - data/work/atmosphere/
  - data/quarantine/atmosphere/
  - data/processed/atmosphere/
  - data/catalog/domain/atmosphere/
  - data/published/layers/atmosphere/
  - data/registry/sources/atmosphere/
  - release/candidates/atmosphere/
tags:
  - kfm
  - pipelines
  - domains
  - air
  - atmosphere
  - air-quality
  - weather
  - smoke
  - climate
  - aod
  - evidence
  - policy
  - governance
notes:
  - "This README governs the requested pipelines/domains/air path as an air/atmosphere pipeline lane placeholder."
  - "The repo doctrine visible in docs/domains/atmosphere identifies a slug conflict between air and atmosphere; this README therefore treats air as NEEDS VERIFICATION / alias-candidate, not as an independently canonical domain lane."
  - "Air/Atmosphere pipeline logic is executable implementation support only; it does not own object meaning, schemas, source descriptors, policy, lifecycle data, catalog truth, official advisories, or release decisions."
  - "Concrete executable behavior, source activation, schedules, CI coverage, schema paths, release wiring, and public API/map behavior remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# 🌬️ Air Domain Pipeline

> Executable Air / Atmosphere pipeline lane for converting admitted air-quality, weather, smoke, aerosol, climate, and forecast-context source material into governed candidates, processed records, catalog/triplet handoffs, receipts, and release-review packages without bypassing evidence, policy, caveat, sensitivity, or release gates.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-air%20%2F%20atmosphere%20pipeline-2e7d32)
![authority](https://img.shields.io/badge/authority-executable%20logic-0a7ea4)
![slug](https://img.shields.io/badge/slug-air%20vs%20atmosphere%20NEEDS%20VERIFICATION-d62728)
![lifecycle](https://img.shields.io/badge/lifecycle-RAW%E2%86%92PUBLISHED-0a7ea4)
![publication](https://img.shields.io/badge/publication-release%20gated-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/air/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Air / Atmosphere  
**Placement posture:** `NEEDS VERIFICATION` because existing domain docs use `atmosphere` as the visible lane while also recording `air` vs `atmosphere` slug drift  
**Public posture:** no direct publication; outputs must pass lifecycle, evidence, caveat, policy, catalog/triplet, release, correction, and rollback gates

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Slug posture: air vs atmosphere](#3-slug-posture-air-vs-atmosphere)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Air / Atmosphere pipeline scope](#6-air--atmosphere-pipeline-scope)
- [7. Source-family posture](#7-source-family-posture)
- [8. Lifecycle contract](#8-lifecycle-contract)
- [9. Required gates](#9-required-gates)
- [10. Directory contract](#10-directory-contract)
- [11. Inputs and outputs](#11-inputs-and-outputs)
- [12. Minimal air pipeline candidate record](#12-minimal-air-pipeline-candidate-record)
- [13. Dry-run, tests, fixtures, receipts, and proofs](#13-dry-run-tests-fixtures-receipts-and-proofs)
- [14. Promotion, publication, correction, and rollback](#14-promotion-publication-correction-and-rollback)
- [15. Definition of done](#15-definition-of-done)
- [16. Open questions](#16-open-questions)

---

## 1. Purpose

`pipelines/domains/air/` is the requested executable pipeline lane for Air / Atmosphere-domain transformations.

It supports candidate processing for:

- air stations and air observations;
- PM2.5 and ozone observations;
- smoke context;
- aerosol optical depth rasters;
- weather stations and weather observations;
- wind, precipitation, and temperature observations;
- climate normals and anomalies;
- forecast context;
- advisory context with official-source redirection;
- public-safe, caveat-aware, evidence-backed derived products.

This directory implements or will implement the **how** of Air / Atmosphere processing. It does not define object meaning, source roles, schemas, policy, source descriptors, lifecycle storage, catalog truth, official advisories, or release approval.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/air/`? | User requested this path; it is treated as an Air / Atmosphere child lane under the domain-pipeline umbrella. | PROPOSED / NEEDS VERIFICATION |
| Is `air` the canonical slug? | Not proven. Existing domain docs use `atmosphere` and explicitly record `air` vs `atmosphere` slug drift. | CONFLICTED / NEEDS VERIFICATION |
| Where do declarative specs live? | Likely `pipeline_specs/atmosphere/` or `pipeline_specs/air/`, pending ADR or placement decision. | NEEDS VERIFICATION |
| Where do source fetchers live? | `connectors/<source>/`, not here. | CONFIRMED separation |
| Where do schemas live? | Likely `schemas/contracts/v1/domains/atmosphere/` per visible domain README, pending slug resolution. | PROPOSED / NEEDS VERIFICATION |
| Where does policy live? | `policy/domains/atmosphere/` or accepted air/atmosphere policy home. | PROPOSED / NEEDS VERIFICATION |
| Where do outputs live? | Lifecycle homes under `data/`, not beside pipeline code. | CONFIRMED lifecycle posture |
| Can this lane publish? | No. It may prepare candidates and release handoffs only through governed workflow. | CONFIRMED doctrine posture |

> [!IMPORTANT]
> Air / Atmosphere pipeline code is subordinate to source descriptors, source roles, rights, caveats, EvidenceBundle closure, sensitivity review, policy decisions, release manifests, correction notices, and rollback cards. A successful run is not a public release.

[⬆ Back to top](#top)

---

## 3. Slug posture: air vs atmosphere

The requested path uses `air`, while visible domain documentation uses `atmosphere` as the domain lane and records `air` vs `atmosphere` slug drift.

Until an ADR or domain-lane register resolves the canonical slug:

- treat `pipelines/domains/air/` as an alias-candidate or transitional implementation lane;
- do not create parallel schemas, contracts, policies, source registries, fixtures, or release paths under both `air` and `atmosphere`;
- prefer existing `atmosphere` documentation and lifecycle lane names where they already exist;
- record any migration from `air` to `atmosphere`, or from `atmosphere` to `air`, with a drift-register entry, path map, compatibility note, tests, and rollback note;
- do not let slug choice change evidence, policy, source-role, or release semantics.

> [!CAUTION]
> The slug decision is a governance decision, not a naming preference. It affects contracts, schemas, policies, data lanes, tests, fixtures, catalog records, release candidates, and public routing.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here only when their primary responsibility is executable Air / Atmosphere-domain processing.

Appropriate contents include:

- fixture-only dry-run entrypoints for Air / Atmosphere pipeline behavior;
- air-quality and weather observation normalizers;
- station and parameter candidate builders;
- smoke / aerosol / AOD context candidate builders;
- climate normal or anomaly normalization helpers;
- advisory-context passthrough processors with official-source redirection checks;
- caveat and confidence annotation helpers, if not centralized elsewhere;
- Air / Atmosphere validator wrappers, if not reusable under `tools/`;
- catalog/triplet handoff helpers, if not centralized in `pipelines/catalog/`;
- receipt emitters, if not shared;
- thin adapters that read governed lifecycle inputs, not live source systems.

A good placement test:

> If the code transforms Air / Atmosphere lifecycle inputs into candidates, processed records, catalog/triplet handoffs, or receipts, it may belong here. If it fetches source data, defines meaning, defines schema, encodes policy, stores lifecycle data, or approves release, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Air-quality, weather, satellite, smoke, or model fetchers | `connectors/<source>/` |
| Source catalog profiles | `docs/sources/catalog/...` |
| Source descriptors / source registry entries | `data/registry/sources/atmosphere/` or accepted registry home |
| Air / Atmosphere architecture and explanation | `docs/domains/atmosphere/...` or accepted canonical doc lane |
| Object meaning contracts | `contracts/domains/atmosphere/...` or accepted contract home |
| JSON Schemas | `schemas/contracts/v1/domains/atmosphere/...` or accepted schema home |
| Policy bundles, caveat tables, release rules | `policy/domains/atmosphere/`, `policy/sensitivity/`, `policy/rights/`, `policy/release/` |
| Declarative run specs | `pipeline_specs/atmosphere/...`, `pipeline_specs/air/...`, or accepted spec lane |
| Fixtures | `fixtures/domains/atmosphere/` or accepted fixture home |
| Tests | `tests/pipelines/domains/air/`, `tests/pipelines/domains/atmosphere/`, or accepted test home |
| Lifecycle outputs | `data/raw/`, `data/work/`, `data/quarantine/`, `data/processed/`, `data/catalog/`, `data/triplets/`, `data/published/` |
| Receipts and proofs | `data/receipts/...`, `data/proofs/...` |
| Release decisions | `release/candidates/atmosphere/`, `release/manifests/atmosphere/`, `release/rollback_cards/`, `release/correction_notices/` |
| Public API or map code | `apps/governed-api/`, `apps/explorer-web/`, `packages/ui/`, `packages/maplibre-runtime/` |

[⬆ Back to top](#top)

---

## 6. Air / Atmosphere pipeline scope

Air / Atmosphere pipeline work may include these governed processing responsibilities:

| Scope area | Pipeline responsibility | Publication posture |
|---|---|---|
| Air stations | Normalize station identity, location, source role, and operational metadata. | Public only when rights, freshness, caveats, and release state close. |
| Air observations | Normalize pollutant observations, units, time windows, methods, and qualifiers. | Caveat-heavy; no direct public instruction. |
| PM2.5 / ozone | Normalize parameter-specific observations and reporting context. | Do not conflate concentration, AQI, forecast, and advisory state. |
| Smoke context | Normalize smoke plume or smoke-context products. | Context only; official public direction stays with issuing authorities / Hazards. |
| AOD rasters | Normalize aerosol optical depth context and uncertainty. | AOD is not PM2.5; derived products require caveats and evidence. |
| Weather observations | Normalize wind, precipitation, temperature, station, and mesonet context. | Observation context only. |
| Climate context | Normalize normals, anomalies, and departures. | Time period, baseline, and method must be explicit. |
| Forecast / model fields | Normalize model or forecast context. | Model fields are not observations; public products require limitations. |
| Advisory context | Carry official-source advisory metadata and redirects. | KFM is not the issuing authority. |

[⬆ Back to top](#top)

---

## 7. Source-family posture

Air / Atmosphere pipeline code may consume only admitted or fixture-bound source material.

Candidate source families may include, subject to source descriptors and rights review:

- regulatory air-quality archives and station observations;
- AirNow-style public air-quality snapshots;
- official weather/advisory context;
- Kansas Mesonet-style weather station context;
- satellite aerosol, smoke, fire, or atmospheric products;
- HRRR-Smoke or other model-field context;
- climate normals and anomaly products;
- local upload or steward-curated material only through source-descriptor and rights gates.

This README does not activate any source. Each source family requires a SourceDescriptor, source role, rights posture, cadence, sensitivity classification, attribution, fixtures, and validation before use.

[⬆ Back to top](#top)

---

## 8. Lifecycle contract

Every Air / Atmosphere pipeline must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal Air / Atmosphere pipeline stance:

1. **Read** approved fixtures, immutable raw captures, work candidates, quarantine inputs in remediation mode, or prior processed baselines.
2. **Normalize** into work candidates with source role, rights, temporal scope, spatial scope, units, caveats, evidence references, and sensitivity posture.
3. **Quarantine** unresolved rights, source-role mismatch, schema drift, sensitivity risk, unit ambiguity, stale source state, over-precise geometry, or validation failures.
4. **Promote to processed** only after validation, policy, caveat, evidence, and reviewer gates appropriate to significance.
5. **Prepare catalog/triplet handoffs** only after processed-state and evidence closure.
6. **Publish** only through release decisions, public-safe artifacts, rollback targets, and correction paths.

Do not treat a move from one lifecycle folder to another as promotion. Promotion is a governed state transition with receipts and review evidence.

[⬆ Back to top](#top)

---

## 9. Required gates

Every Air / Atmosphere pipeline run must check or explicitly fail closed on:

1. **Source descriptor gate** — every input has stable source identity, role, cadence, rights, and sensitivity posture.
2. **Source-role gate** — model fields, advisories, context, forecasts, and observations are not silently collapsed.
3. **Rights gate** — unknown or restrictive license, attribution, or redistribution terms block public release.
4. **Unit and parameter gate** — units, averaging period, pollutant parameter, measurement method, and qualifiers are explicit.
5. **AQI/concentration gate** — AQI, concentration, forecasts, alerts, and advisory context remain distinct.
6. **AOD/PM2.5 gate** — AOD is not PM2.5; derived relations require method, evidence, and caveats.
7. **Observation/model gate** — observations, forecasts, model fields, and advisory context remain distinct.
8. **Freshness gate** — stale current-state products are marked stale or denied from current-state display.
9. **Sensitivity gate** — infrastructure, private sensor, or precise location risks fail closed where applicable.
10. **Schema gate** — candidate and processed records match approved schemas.
11. **Contract gate** — object meanings match Air / Atmosphere contracts and do not invent new semantics silently.
12. **Evidence gate** — claim-bearing outputs resolve EvidenceBundle support or abstain.
13. **Temporal gate** — observation, report, valid, forecast, retrieval, processing, catalog, and release times remain distinct.
14. **Spatial gate** — CRS, geometry precision, raster grid, station location precision, and public-safe transforms are recorded.
15. **Policy gate** — policy decisions are finite and recorded; no silent allow.
16. **Validation gate** — validators exercise pass, fail, abstain/deny/error paths, not only success.
17. **Receipt gate** — every run records input refs, versions, parameters, hashes, output refs, and outcomes.
18. **No-direct-publish gate** — no writes to public UI, public API, or `data/published/` without release workflow authority.
19. **Catalog/triplet gate** — catalog and graph projections preserve provenance and do not replace canonical records.
20. **Release gate** — public release requires ReleaseManifest, rollback target, correction path, and review state.

[⬆ Back to top](#top)

---

## 10. Directory contract

Recommended shape:

```text
pipelines/domains/air/
├── README.md                         # this file; alias/slug-warning lane
├── PIPELINE_CONTRACT.md              # PROPOSED: Air / Atmosphere execution contract
├── run_dry_fixture.py                # PROPOSED if repo Python convention is accepted
├── normalize_air_observation.py      # PROPOSED
├── normalize_weather_observation.py  # PROPOSED
├── normalize_smoke_context.py        # PROPOSED
├── normalize_aod_raster.py           # PROPOSED
├── build_caveat_receipt.py           # PROPOSED; may belong in shared tools if reused
├── build_catalog_handoff.py          # PROPOSED if not centralized in pipelines/catalog/
├── validate_air_candidate.py         # PROPOSED wrapper if not centralized in tools/
├── emit_receipt.py                   # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no source fetching
```

If slug resolution chooses `atmosphere`, migrate toward:

```text
pipelines/domains/atmosphere/
├── README.md
└── ...
```

Declarative specs should live outside this directory, likely under `pipeline_specs/atmosphere/` after slug resolution. Generated outputs must not be written beside the code that generated them. Use lifecycle homes under `data/`, proof homes under `data/proofs/`, receipt homes under `data/receipts/`, and release homes under `release/`.

[⬆ Back to top](#top)

---

## 11. Inputs and outputs

### Inputs

| Input class | Allowed source | Required condition |
|---|---|---|
| No-network fixture | `fixtures/domains/atmosphere/` or accepted fixture home | Safe default for tests and dry runs. |
| Raw Air / Atmosphere capture | `data/raw/atmosphere/<source_id>/<run_id>/` or accepted `air` lane | Immutable source-edge capture with source descriptor, checksums, and ingest receipt. |
| Work candidate | `data/work/atmosphere/<run_id>/` or accepted `air` lane | Candidate-only; not public. |
| Quarantine input | `data/quarantine/atmosphere/<reason>/<run_id>/` or accepted `air` lane | Audit/remediation mode only. |
| Prior processed baseline | `data/processed/atmosphere/<dataset_id>/<version>/` or accepted `air` lane | Validated baseline for diff/supersession. |
| Source registry / descriptor | `data/registry/sources/atmosphere/`, `docs/sources/catalog/...` | Source role, rights, cadence, attribution, sensitivity. |
| Cross-lane context | Hazards, Agriculture, Hydrology, Habitat, Flora, Fauna, Settlements, or other lifecycle homes | Must preserve source role and domain ownership. |
| Policy / schema / contract refs | `policy/`, `schemas/`, `contracts/` | Referenced by validators, not stored here. |

### Outputs

| Output class | Correct home | Notes |
|---|---|---|
| Work candidate | `data/work/atmosphere/<run_id>/` or accepted lane | Candidate only. |
| Quarantine record | `data/quarantine/atmosphere/<reason>/<run_id>/` or accepted lane | Failed, restricted, unresolved, stale, or unsafe material. |
| Processed dataset version | `data/processed/atmosphere/<dataset_id>/<version>/` or accepted lane | Validated; not automatically public. |
| Catalog candidate | `data/catalog/domain/atmosphere/...` or approved catalog home | After processed-state and evidence gates. |
| Triplet / graph delta | `data/triplets/atmosphere/...` or approved graph-delta home | Projection; does not replace canonical truth. |
| Caveat / freshness / transform receipt | `data/receipts/...` or approved receipt/proof home | Required for high-consequence public products. |
| Run receipt | `data/receipts/pipeline/...` | Process memory, not release proof. |
| Evidence / validation proof | `data/proofs/...` | EvidenceBundle, validation reports, proof packs. |
| Release handoff | `release/candidates/atmosphere/...` | Only through release workflow. |

[⬆ Back to top](#top)

---

## 12. Minimal air pipeline candidate record

The final schema is not defined here. This example shows the minimum information an Air / Atmosphere pipeline candidate should preserve.

```yaml
schema_version: kfm.air_pipeline_candidate.v1
candidate_id: air_<object_family>_<run_id>_<hash>
pipeline_id: domains.air
canonical_slug_status: NEEDS_VERIFICATION
preferred_domain_lane: atmosphere
run_id: run_YYYYMMDDThhmmssZ
status: WORK_CANDIDATE
object_family: <air_observation|pm25_observation|ozone_observation|smoke_context|aod_raster|weather_observation|climate_anomaly|forecast_context|advisory_context>
source_inputs:
  - source_id: src_air_example
    source_role: <observation|context|forecast|advisory|restricted>
    lifecycle_ref: data/raw/atmosphere/<source_id>/<run_id>/
    input_hash: sha256:<hash>
    rights_state: needs_review
semantic_guards:
  aqi_is_concentration: false
  aod_is_pm25: false
  model_field_is_observation: false
  kfm_is_official_issuer: false
spatial_scope:
  geometry_ref: <governed_station_or_grid_ref>
  public_precision: withheld_until_review
temporal_scope:
  observed_at: YYYY-MM-DDThh:mm:ssZ
  valid_at: null
  forecast_reference_time: null
  retrieved_at: YYYY-MM-DDThh:mm:ssZ
  processed_at: YYYY-MM-DDThh:mm:ssZ
freshness:
  state: needs_review
  current_display_allowed: false
method:
  transform_family: air_observation_normalization
  algorithm_version: <version>
  parameter_hash: sha256:<hash>
caveats:
  required: true
  caveat_receipt_ref: null
sensitivity:
  official_context_confusion_risk: needs_review
  private_sensor_risk: unknown
  public_release_default: DENY_UNTIL_REVIEW
policy:
  outcome: ABSTAIN
  reason_code: CAVEAT_AND_EVIDENCE_NOT_RESOLVED
evidence:
  evidence_bundle_ref: null
  citation_state: ABSTAIN
outputs:
  candidate_record: data/work/atmosphere/run_YYYYMMDDThhmmssZ/candidate.yml
  receipt: data/receipts/pipeline/air/run_YYYYMMDDThhmmssZ.yml
review:
  reviewer_required: true
  reviewer_roles:
    - atmosphere-domain-steward
    - policy-steward
    - release-steward
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 13. Dry-run, tests, fixtures, receipts, and proofs

Default execution is **fixture-only and no-network** until source activation, rights review, sensitivity review, caveat review, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/air/
├── test_no_network_dry_run.py             # PROPOSED
├── test_source_role_required.py           # PROPOSED
├── test_rights_unknown_denied.py          # PROPOSED
├── test_aqi_not_concentration.py          # PROPOSED
├── test_aod_not_pm25.py                   # PROPOSED
├── test_model_not_observation.py          # PROPOSED
├── test_stale_current_display_denied.py   # PROPOSED
├── test_official_context_redirect.py      # PROPOSED
├── test_missing_evidence_abstains.py      # PROPOSED
├── test_receipt_hashes.py                 # PROPOSED
└── test_no_direct_publish.py              # PROPOSED
```

A dry run should prove:

- fixtures load without network access;
- every input has source identity and source role;
- unknown rights produce `ABSTAIN`, `DENY`, or quarantine;
- AQI, concentration, forecast, model, and advisory states remain distinct;
- AOD-derived products are caveated and do not become PM2.5 observations;
- stale current-state outputs are denied or marked stale;
- missing EvidenceBundle support produces `ABSTAIN`;
- cross-lane context preserves domain ownership and source role;
- invalid records fail validation;
- receipts include input hashes, method hashes, caveat refs, output refs, and outcomes;
- no outputs are written to public UI, public API, `data/published/`, or release manifests by default.

[⬆ Back to top](#top)

---

## 14. Promotion, publication, correction, and rollback

Air / Atmosphere pipelines may prepare candidates. They do not publish.

Required promotion chain:

```text
air / atmosphere source or work input
  -> air / atmosphere candidate
  -> validation report
  -> policy decision
  -> caveat / freshness receipt where required
  -> EvidenceBundle closure
  -> processed air / atmosphere dataset version
  -> catalog / triplet candidate
  -> steward review
  -> release candidate
  -> ReleaseManifest
  -> RollbackCard
  -> public-safe artifact
```

Correction and rollback posture:

- denied, abstained, errored, stale, and quarantined runs remain auditable;
- candidate rollback preserves receipts and proof state;
- processed versions are superseded by governed state transition, not hidden overwrite;
- public artifact rollback is owned by `release/`, not by this directory;
- correction notices must point back to source, evidence, caveat/freshness state, validation, catalog, release, and rollback state.

[⬆ Back to top](#top)

---

## 15. Definition of done

This README is done when it:

- fills the requested `pipelines/domains/air/README.md` path;
- marks `air` vs `atmosphere` slug status as `CONFLICTED / NEEDS VERIFICATION`;
- identifies this directory as executable Air / Atmosphere pipeline logic only;
- keeps docs, schemas, contracts, policy, fixtures, tests, data, registries, receipts, proofs, and release decisions in their proper homes;
- preserves source-role, evidence, caveat, sensitivity, policy, lifecycle, catalog/triplet, release, correction, and rollback boundaries;
- denies direct publication and official-advisory behavior;
- gives maintainers a fixture-first expansion and migration pattern.

Future executable Air / Atmosphere pipeline implementation is done only when it has:

- slug decision or compatibility plan;
- owners and review burden;
- source-descriptor coverage;
- no-network fixtures;
- schema-backed candidates;
- Air / Atmosphere contract conformance;
- rights, caveat, sensitivity, freshness, temporal, spatial, and evidence tests;
- deterministic receipts;
- no-direct-publish tests;
- CI coverage;
- steward-review handoff;
- release, correction, and rollback documentation.

[⬆ Back to top](#top)

---

## 16. Open questions

| ID | Question | Status |
|---|---|---|
| `AIR-PIPE-001` | Should this executable lane remain `pipelines/domains/air/`, migrate to `pipelines/domains/atmosphere/`, or keep one as a compatibility alias? | NEEDS VERIFICATION / ADR |
| `AIR-PIPE-002` | Should declarative specs live at `pipeline_specs/air/` or `pipeline_specs/atmosphere/`? | NEEDS VERIFICATION |
| `AIR-PIPE-003` | Which object family owns caveat, freshness, and official-source redirect receipts? | PROPOSED / NEEDS ADR if new object family |
| `AIR-PIPE-004` | Which source descriptors are first-wave approved for fixture-only dry runs? | NEEDS VERIFICATION |
| `AIR-PIPE-005` | Which CI job owns Air / Atmosphere pipeline invariant tests? | UNKNOWN |
| `AIR-PIPE-006` | Should catalog handoff logic live here or in centralized `pipelines/catalog/` with Air / Atmosphere adapters? | NEEDS VERIFICATION |
| `AIR-PIPE-007` | Which public-safe map/API products are allowed after release, and at what freshness/caveat level? | NEEDS VERIFICATION |
| `AIR-PIPE-008` | How should official advisory context be displayed so KFM cannot be mistaken for the issuing authority? | NEEDS VERIFICATION |
| `AIR-PIPE-009` | How should private or low-cost sensor observations be corrected, caveated, restricted, or denied? | NEEDS VERIFICATION |

---

## Maintainer note

Start with fixture-only dry runs and negative tests. Do not add live source fetching, public current-state displays, official advisory behavior, public map layers, release handoff automation, or direct API payload generation until source roles, rights, caveats, freshness, sensitivity, evidence closure, and rollback are proven.
