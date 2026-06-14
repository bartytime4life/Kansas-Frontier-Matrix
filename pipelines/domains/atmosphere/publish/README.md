<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-atmosphere-publish-readme
title: Atmosphere Publish Pipeline README
type: readme
version: v0.1
status: draft
owners:
  - <atmosphere-pipeline-owner>
  - <atmosphere-domain-steward>
  - <release-steward>
  - <evidence-steward>
  - <policy-steward>
  - <validation-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-06-13
policy_label: public-with-atmosphere-publication-caveat-freshness-and-rollback-gates
path: pipelines/domains/atmosphere/publish/README.md
related:
  - docs/doctrine/directory-rules.md
  - pipelines/README.md
  - pipelines/domains/README.md
  - pipelines/domains/atmosphere/README.md
  - pipelines/domains/atmosphere/validate/README.md
  - pipelines/domains/air/README.md
  - docs/domains/atmosphere/README.md
  - docs/domains/atmosphere/DATA_LIFECYCLE.md
  - docs/domains/atmosphere/SOURCE_REGISTRY.md
  - docs/domains/atmosphere/CANONICAL_PATHS.md
  - docs/domains/atmosphere/API_CONTRACTS.md
  - docs/runbooks/atmosphere/PROMOTION_RUNBOOK.md
  - pipeline_specs/atmosphere/publish.yaml
  - contracts/domains/atmosphere/
  - schemas/contracts/v1/domains/atmosphere/
  - policy/domains/atmosphere/
  - data/catalog/domain/atmosphere/
  - data/triplets/atmosphere/
  - data/published/layers/atmosphere/
  - data/receipts/pipeline/
  - data/proofs/evidence_bundle/
  - release/candidates/atmosphere/
  - release/manifests/atmosphere/
tags:
  - kfm
  - pipelines
  - domains
  - atmosphere
  - air
  - publish
  - release-manifest
  - layer-manifest
  - rollback-card
  - correction-notice
  - air-quality
  - weather
  - smoke
  - aod
  - climate
  - model-context
  - advisory-context
  - freshness
  - caveats
  - evidence-bundle
  - policy
  - governance
notes:
  - "This README fills the blank pipelines/domains/atmosphere/publish path as a nested executable Atmosphere publication-artifact sublane."
  - "Atmosphere publish logic is executable artifact assembly only; it does not own release decisions, ReleaseManifests, RollbackCards, CorrectionNotices, policy, EvidenceBundle truth, catalog truth, source descriptors, schemas, or public API authority."
  - "Publication is a governed state transition, not a file move, not a UI action, and not a successful pipeline run."
  - "Low-cost sensor products require correction, caveats, confidence, limitations, and freshness state before public artifacts are assembled."
  - "AdvisoryContext / notice-context products must redirect to official issuing sources rather than reproducing issuing-authority text as KFM authority."
  - "Concrete executable behavior, CI coverage, release wiring, public API/map behavior, and artifact schemas remain NEEDS VERIFICATION until implemented and tested."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Atmosphere Publish Pipeline

> Executable Atmosphere / Air / Climate sublane for assembling release-approved public artifacts, layer manifests, tile/extract outputs, caveats, freshness badges, evidence links, correction hooks, rollback refs, and artifact receipts from governed catalog/triplet inputs — without deciding release, replacing official issuing sources, or exposing internal lifecycle stores.

![status](https://img.shields.io/badge/status-draft-blue)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![scope](https://img.shields.io/badge/scope-atmosphere%20publish-2e7d32)
![authority](https://img.shields.io/badge/authority-artifact%20assembly%20only-0a7ea4)
![official-source](https://img.shields.io/badge/official%20source-redirection%20required-d62728)
![rollback](https://img.shields.io/badge/rollback-required-d62728)
![ci](https://img.shields.io/badge/CI-TODO-lightgrey)

**Status:** Draft  
**Path:** `pipelines/domains/atmosphere/publish/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Domain lane:** Atmosphere / Air / Climate  
**Sublane:** Publish / release-artifact assembly  
**Placement posture:** nested executable sublane under `pipelines/domains/atmosphere/`; concrete executable behavior remains `PROPOSED / NEEDS VERIFICATION` unless backed by tests and repo evidence  
**Public posture:** no independent release authority; this lane may assemble only release-approved artifacts with ReleaseManifest, EvidenceBundle, policy, caveat, freshness, correction, and rollback closure.

---

## Quick jump

- [1. Purpose](#1-purpose)
- [2. Placement and authority](#2-placement-and-authority)
- [3. Publish anti-collapse rules](#3-publish-anti-collapse-rules)
- [4. What belongs here](#4-what-belongs-here)
- [5. What does not belong here](#5-what-does-not-belong-here)
- [6. Publication-artifact scope](#6-publication-artifact-scope)
- [7. Lifecycle contract](#7-lifecycle-contract)
- [8. Required gates](#8-required-gates)
- [9. Directory contract](#9-directory-contract)
- [10. Inputs and outputs](#10-inputs-and-outputs)
- [11. Minimal publish artifact receipt](#11-minimal-publish-artifact-receipt)
- [12. Tests, fixtures, receipts, and proofs](#12-tests-fixtures-receipts-and-proofs)
- [13. Correction, stale state, and rollback](#13-correction-stale-state-and-rollback)
- [14. Definition of done](#14-definition-of-done)
- [15. Open questions](#15-open-questions)

---

## 1. Purpose

`pipelines/domains/atmosphere/publish/` is the executable sublane for Atmosphere publication-artifact assembly.

It supports artifact preparation for:

- release-approved air-quality, weather, smoke, AOD, climate, model-context, and notice/advisory-context layers, tiles, extracts, cards, indexes, manifests, and metadata bundles;
- public derivatives of `AirStation`, `AirObservation`, `PM25Observation`, `OzoneObservation`, `SmokeContext`, `AODRaster`, `WeatherStation`, `WeatherObservation`, `WindField`, `PrecipitationObservation`, `TemperatureObservation`, `ClimateNormal`, `ClimateAnomaly`, `ForecastContext`, and `AdvisoryContext` records;
- caveat, confidence, correction, limitation, and freshness surfaces for low-cost sensors, model products, derived-fusion products, and advisory-context outputs;
- ReleaseManifest-bound dataset, layer, tile, EvidenceBundle, policy, review, CorrectionNotice, RollbackCard, and artifact-digest refs;
- public attribute include-lists, unit/parameter labels, stale-state badges, source-vintage badges, official-source redirection labels, and Evidence Drawer refs;
- artifact receipts that record digests, input refs, release refs, caveat/freshness refs, public representation refs, and rollback target refs;
- hold records for missing release decision, missing rollback target, unresolved evidence, unresolved policy, stale state, missing caveats, or artifact-integrity failure.

This directory implements or will implement the **how** of Atmosphere publication artifact assembly. It does not decide release, define ReleaseManifest shape, define policy, issue or rewrite official source notices, own EvidenceBundle truth, own catalog truth, own source descriptors, mutate canonical stores, serve public API responses, or create public UI state by itself.

[⬆ Back to top](#top)

---

## 2. Placement and authority

| Question | Answer | Status |
|---|---|---|
| Why `pipelines/`? | This is executable pipeline logic: the **how**. | CONFIRMED root responsibility |
| Why `domains/atmosphere/`? | Visible domain docs use `atmosphere` as the lane and treat `air` as slug drift / alias pending ADR. | CONFIRMED documentation pattern; implementation NEEDS VERIFICATION |
| Why `publish/`? | This is a narrow executable sublane for assembling release-approved public artifacts. | PROPOSED / NEEDS VERIFICATION |
| Does this publish by itself? | No. It consumes release-approved inputs and emits artifacts/receipts; release authority lives under `release/`. | CONFIRMED governance posture |
| Does this own official-source text? | No. Advisory/notice context redirects to official sources and remains context only. | CONFIRMED boundary posture |
| Can public clients read this lane? | No. Public clients use governed APIs and released artifacts only. | CONFIRMED trust membrane posture |

> [!IMPORTANT]
> A successful publish-artifact run is not a release decision. Atmosphere output is public only when a ReleaseManifest with resolvable EvidenceBundle refs, policy outcomes, caveats, freshness state, correction path, and rollback target has already authorized the artifact set.

[⬆ Back to top](#top)

---

## 3. Publish anti-collapse rules

Publish-artifact assembly must preserve release authority, evidence bindings, caveat state, freshness state, correction state, and rollback state.

Disallowed collapses:

```text
pipeline run -> release approval
copy to published path -> publication
published layer -> canonical atmosphere truth
catalog record -> public artifact
AQI -> concentration
AOD -> PM2.5
model field -> observation
low-cost sensor output -> direct truth without caveat/correction
advisory context -> official issuing-source text
EvidenceRef -> EvidenceBundle
ReleaseManifest -> mutable latest pointer
CorrectionNotice -> silent edit
generated public summary -> evidence
public UI payload -> canonical store
```

Required distinctions:

- ReleaseManifest, LayerManifest, EvidenceBundle, ReviewRecord, PolicyDecision, ValidationReport, CorrectionNotice, RollbackCard, catalog record, graph projection, and public artifact remain separate;
- low-cost sensor products carry correction, caveats, confidence, and limitations before public artifact assembly;
- advisory-context artifacts carry official-source redirection rather than KFM-authored operational instructions;
- public artifacts bind to content hashes and release refs, not floating latest pointers;
- stale, superseded, corrected, withdrawn, denied, and held states remain visible;
- public clients never read RAW, WORK, QUARANTINE, canonical/internal stores, source APIs, graph internals, vector indexes, or direct model outputs.

[⬆ Back to top](#top)

---

## 4. What belongs here

Files belong here when their primary responsibility is executable Atmosphere publication-artifact assembly.

Appropriate contents include:

- fixture-only release-artifact dry-run entrypoints;
- ReleaseManifest input validators;
- EvidenceBundle, policy, review, ValidationReport, CorrectionNotice, and RollbackCard presence checks;
- public layer/PMTiles/extract/card/index builders;
- artifact digest and manifest writers;
- public attribute include-list, unit-label, caveat, confidence, limitation, and official-source-redirection injectors;
- freshness, stale, corrected, superseded, and withdrawn badge builders;
- artifact-integrity and rollback-target validators;
- release receipt emitters, if not shared;
- hold/quarantine routing helpers for missing release preconditions.

A good placement test:

> If the code assembles artifacts from an already-approved Atmosphere release candidate and writes content-addressed artifact outputs plus receipts, it may belong here. If it decides release, edits policy, decides official-source wording, validates raw source material, owns catalog truth, serves the API, or writes UI state, it belongs somewhere else.

[⬆ Back to top](#top)

---

## 5. What does not belong here

| Do not place here | Correct responsibility home |
|---|---|
| Source fetchers, API clients, watchers | `connectors/` or watcher roots |
| Source descriptors / source registry entries | `data/registry/sources/atmosphere/` or approved registry home |
| Ingest, normalize, validate, or catalog logic | sibling Atmosphere pipeline sublanes |
| Atmosphere doctrine and object meaning | `docs/domains/atmosphere/`, `contracts/domains/atmosphere/` |
| JSON Schemas | `schemas/contracts/v1/domains/atmosphere/` or accepted schema home |
| Policy, rights, sensitivity, release rules | `policy/...` responsibility roots |
| Release decisions, ReleaseManifest authorship, RollbackCards | `release/...` responsibility roots |
| Official-source notices, warnings, or operational instructions | Official issuing sources and governed context only |
| Fixtures | `fixtures/domains/atmosphere/publish/` or accepted fixture home |
| Tests | `tests/pipelines/domains/atmosphere/publish/` or accepted test home |
| Raw, work, quarantine, processed, catalog, triplet lifecycle records | `data/...` lifecycle homes |
| Public API or map viewer code | `apps/governed-api/`, `apps/explorer-web/`, packages |
| Direct model summaries or generated answer text | Governed AI/released artifact paths only after review |

[⬆ Back to top](#top)

---

## 6. Publication-artifact scope

| Scope area | Publish-lane responsibility | Failure behavior |
|---|---|---|
| Release input | Confirm release candidate and ReleaseManifest refs are present and resolvable. | Hold; no artifact change. |
| Evidence binding | Confirm EvidenceBundle refs resolve and digests match. | Hold or quarantine. |
| Validation | Confirm ValidationReport pass and knowledge-character denials are honored. | Hold on missing/failed validation. |
| Caveats/freshness | Confirm low-cost sensor/model/fusion/notice context caveats and stale-state badges. | Hold release-facing output. |
| Artifact integrity | Write content-addressed artifacts, manifests, checksums, and receipts. | Fail closed on digest mismatch. |
| Correction path | Carry CorrectionNotice and invalidation expectations. | Hold if missing for corrected releases. |
| Rollback | Confirm rollback target or RollbackCard precondition is present. | Hold release-facing output. |
| Public interface | Produce artifacts for governed API/UI consumption only. | No direct UI/API side effects. |

[⬆ Back to top](#top)

---

## 7. Lifecycle contract

Every Atmosphere publish run must preserve the KFM lifecycle:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Normal stance:

1. **Read** release-approved inputs only: ReleaseManifest refs, release candidates, catalog/triplet refs, EvidenceBundle refs, ValidationReports, policy decisions, review records, CorrectionNotices, rollback targets, and artifact specs.
2. **Verify** every required reference resolves and every digest matches expected inputs.
3. **Assemble** public artifacts such as layers, tiles, extracts, cards, caveats, indexes, and manifest sidecars.
4. **Emit** artifact receipts, digests, freshness/caveat refs, and rollback/correction/invalidation links.
5. **Hold or quarantine** missing release, evidence, validation, policy, caveat, correction, rollback, freshness, or integrity preconditions.
6. **Never mutate canonical stores, source captures, catalog truth, release decisions, public UI state, official-source text, or direct API behavior.**

Publish here means artifact assembly after a governed release decision. It is not an approval gate and not a shortcut from catalog to public exposure.

[⬆ Back to top](#top)

---

## 8. Required gates

Every Atmosphere publish run must check or explicitly fail closed on:

1. **ReleaseManifest gate** — release identity, contents, digests, evidence refs, rollback target, time, and correction path are present.
2. **EvidenceBundle gate** — all public claims resolve evidence and digest closure passes.
3. **ValidationReport gate** — validation pass exists and knowledge-character denials are preserved.
4. **Policy/review gate** — release policy outcome and review state are present; no silent allow.
5. **Caveat gate** — low-cost sensor, model, derived-fusion, and advisory/notice-context artifacts carry required caveats, confidence, limitations, or official-source redirection.
6. **Freshness gate** — source cadence, stale-state threshold, source vintage, and freshness badge are explicit.
7. **Rights gate** — unresolved rights or source-role uncertainty blocks public promotion.
8. **Artifact digest gate** — artifact content hashes, manifests, tiles, extracts, and indexes match release refs.
9. **Correction gate** — corrected outputs carry CorrectionNotice and invalidation list where required.
10. **Rollback gate** — rollback target is resolvable before artifact publication.
11. **Trust membrane gate** — outputs are suitable for governed APIs; no public client reads internal stores.
12. **No-direct-decision gate** — this lane does not create release decisions or policy decisions.
13. **No-direct-UI/API gate** — no side effects in public UI, public API routes, or direct model responses.

[⬆ Back to top](#top)

---

## 9. Directory contract

Recommended shape:

```text
pipelines/domains/atmosphere/publish/
├── README.md                         # this file
├── PUBLISH_CONTRACT.md               # PROPOSED: Atmosphere publish artifact execution contract
├── run_dry_fixture.py                # PROPOSED synthetic fixture only
├── validate_release_manifest.py      # PROPOSED
├── validate_evidence_bundle_refs.py  # PROPOSED
├── validate_validation_report.py     # PROPOSED
├── validate_policy_review.py         # PROPOSED
├── validate_freshness_caveats.py     # PROPOSED
├── validate_rollback_target.py       # PROPOSED
├── build_public_layer_manifest.py    # PROPOSED
├── build_public_artifacts.py         # PROPOSED
├── emit_publish_receipt.py           # PROPOSED only if not shared
└── adapters/                         # PROPOSED thin lifecycle adapters, no source fetching
```

Declarative specs should live outside this directory:

```text
pipeline_specs/atmosphere/publish.yaml # PROPOSED / NEEDS VERIFICATION
```

Generated outputs must not be written beside this code. Use accepted release/public artifact homes under `data/published/layers/atmosphere/`, `data/receipts/`, `release/candidates/atmosphere/`, and `release/manifests/atmosphere/`, with decisions remaining in `release/` and public serving remaining behind governed API/UI roots.

[⬆ Back to top](#top)

---

## 10. Inputs and outputs

| Class | Correct home | Notes |
|---|---|---|
| Fixture input | `fixtures/domains/atmosphere/publish/` or accepted fixture home | Synthetic release fixture. |
| Release candidate | `release/candidates/atmosphere/` | Reviewable input only. |
| ReleaseManifest | `release/manifests/atmosphere/` | Decision authority, not owned here. |
| Evidence proof | `data/proofs/evidence_bundle/` | Required and resolved before artifact assembly. |
| ValidationReport | `data/processed/atmosphere/` or accepted validation-report home | Input by stable ref/digest. |
| Catalog/triplet refs | `data/catalog/domain/atmosphere/`, `data/triplets/atmosphere/` | Inputs by stable refs/digests. |
| Published artifact | `data/published/layers/atmosphere/` or accepted public artifact home | Content-addressed output only. |
| Receipt | `data/receipts/pipeline/atmosphere/publish/<run_id>.yml` or accepted receipt home | Records release refs, digests, checks, outputs. |
| Correction / rollback refs | `release/...` | Required refs for release-capable artifacts. |

[⬆ Back to top](#top)

---

## 11. Minimal publish artifact receipt

The final schema is not defined here. This example shows the minimum information an Atmosphere publish run should preserve.

```yaml
schema_version: kfm.atmosphere_publish_receipt.v1
publish_run_id: atmosphere_publish_run_YYYYMMDDThhmmssZ
pipeline_id: domains.atmosphere.publish
status: HELD
release:
  release_manifest_ref: release/manifests/atmosphere/<release_id>.json
  release_manifest_hash: sha256:<hash>
  release_candidate_ref: release/candidates/atmosphere/<candidate_id>.json
inputs:
  catalog_refs: []
  triplet_refs: []
  validation_report_refs: []
  evidence_bundle_refs: []
  policy_decision_refs: []
  review_record_refs: []
  correction_notice_refs: []
  rollback_target_ref: null
publication_controls:
  caveats_ready: false
  freshness_badge_ready: false
  official_source_redirection_ready: false
  low_cost_sensor_limitations_ready: false
artifacts:
  layer_manifest_ref: null
  pmtiles_ref: null
  extract_refs: []
  artifact_digests: {}
checks:
  evidence_resolved: false
  validation_resolved: false
  policy_resolved: false
  rollback_resolved: false
  digests_match: false
anti_collapse:
  publish_run_is_release_decision: false
  copied_file_is_publication: false
  public_layer_is_canonical_truth: false
  aqi_is_concentration: false
  aod_is_pm25: false
  model_field_is_observation: false
outputs:
  receipt_ref: data/receipts/pipeline/atmosphere/publish/run_YYYYMMDDThhmmssZ.yml
  published_artifact_refs: []
rollback:
  required_before_publication: true
```

[⬆ Back to top](#top)

---

## 12. Tests, fixtures, receipts, and proofs

Default execution is **fixture-only, synthetic, and no-network** until publish specs, release fixtures, evidence, policy, caveat, freshness, and CI coverage are approved.

Recommended tests:

```text
tests/pipelines/domains/atmosphere/publish/
├── test_no_network_dry_run.py              # PROPOSED
├── test_release_manifest_required.py       # PROPOSED
├── test_evidence_bundle_required.py        # PROPOSED
├── test_validation_report_required.py      # PROPOSED
├── test_policy_review_required.py          # PROPOSED
├── test_low_cost_sensor_caveats_required.py # PROPOSED
├── test_official_source_redirection_required.py # PROPOSED
├── test_freshness_badge_required.py        # PROPOSED
├── test_artifact_digests_match_manifest.py # PROPOSED
├── test_stale_state_surfaces.py            # PROPOSED
├── test_correction_notice_invalidates.py   # PROPOSED
├── test_publish_run_not_release_decision.py # PROPOSED
├── test_no_internal_store_exposure.py      # PROPOSED
└── test_no_direct_ui_api_side_effect.py    # PROPOSED
```

A dry run should prove fixtures load without network access, ReleaseManifest and rollback target are required, EvidenceBundle and policy refs resolve, low-cost sensor caveats are present when needed, official-source redirection exists for notice context, artifacts are content-addressed, receipts are deterministic, stale/correction states are surfaced, and no run mutates release decisions, canonical stores, public UI, or public API routes.

[⬆ Back to top](#top)

---

## 13. Correction, stale state, and rollback

Atmosphere publish pipelines may materialize correction and rollback-aware artifacts. They do not approve corrections or rollbacks.

Required chain:

```text
catalog / triplet + EvidenceBundle + policy + review
  -> release candidate
  -> ReleaseManifest + rollback target
  -> publish artifact assembly
  -> artifact receipt + public layer/extract/index
  -> governed API/UI consumption
```

Correction and rollback posture:

- stale is visible and not silently refreshed;
- correction is a governed forward transition, not a silent edit;
- rollback is authenticated and receipt-backed, not ad-hoc cleanup;
- `CorrectionNotice`, `RollbackCard`, invalidation lists, and prior release refs stay attached to public artifacts;
- released artifacts are invalidated when source cadence, source rights, evidence, validation, policy, caveat, freshness, correction, or rollback refs drift;
- release rollback is owned by `release/`, not by this directory.

[⬆ Back to top](#top)

---

## 14. Definition of done

This README is done when it:

- fills the blank `pipelines/domains/atmosphere/publish/README.md` file;
- identifies this directory as a nested executable Atmosphere publish-artifact sublane;
- prevents source, ingest, normalize, validate, catalog, schema, contract, policy, release-decision, public API, UI, official-source authority, and canonical-store authority from being placed here;
- preserves ReleaseManifest, EvidenceBundle, ValidationReport, PolicyDecision, ReviewRecord, CorrectionNotice, RollbackCard, caveat, freshness, catalog/triplet, artifact digest, release, correction, and rollback boundaries;
- blocks pipeline-run-as-release, copy-as-publication, catalog-as-public-artifact, AQI-as-concentration, AOD-as-PM2.5, model-field-as-observation, generated-summary-as-evidence, direct UI/API side effects, and internal-store exposure;
- gives maintainers a fixture-first, fail-closed expansion pattern.

Future executable work in this sublane is done only when it has release-fixture coverage, schema-backed artifact receipts, ReleaseManifest/EvidenceBundle/ValidationReport/policy/caveat/freshness/rollback/digest tests, deterministic receipts, CI coverage, steward-review handoff, and rollback/correction documentation.

[⬆ Back to top](#top)

---

## 15. Open questions

| ID | Question | Status |
|---|---|---|
| `ATM-PUB-001` | Should Atmosphere publish remain one sublane, or split into layer, tile, extract, Evidence Drawer, time-series, and Focus Mode artifact builders? | NEEDS VERIFICATION / ADR |
| `ATM-PUB-002` | Which object owns the binding between `ReleaseManifest`, `LayerManifest`, PMTiles digests, and public API payload digests? | NEEDS VERIFICATION |
| `ATM-PUB-003` | Which schema owns Atmosphere publish receipts and public artifact manifests? | NEEDS VERIFICATION |
| `ATM-PUB-004` | Which CI job owns Atmosphere publish invariant tests? | UNKNOWN |
| `ATM-PUB-005` | What is the approved caveat vocabulary for low-cost sensors, models, derived-fusion products, and notice context? | NEEDS VERIFICATION / ADR |
| `ATM-PUB-006` | What artifact homes are approved for Atmosphere public layers, time-series, extracts, cards, and indexes? | NEEDS VERIFICATION |
| `ATM-PUB-007` | Which rollback proof must be present before Atmosphere artifacts are materialized? | NEEDS VERIFICATION |

---

## Maintainer note

Start with synthetic release fixtures and negative tests. Do not add live source fetching, source-profile editing, schema authority, policy authority, release-decision authority, direct catalog writes, public UI code, public API code, release-manifest authorship, official-source notice generation, or generated atmospheric summaries until ReleaseManifest refs, EvidenceBundle refs, ValidationReport refs, policy decisions, review state, caveats, freshness, artifact digests, correction paths, and rollback targets are proven.
