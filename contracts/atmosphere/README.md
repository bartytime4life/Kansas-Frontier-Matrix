---
title: Atmosphere / Air Semantic Contract Compatibility Lane
version: 0.2
status: draft; repository-grounded; compatibility-index; mixed-content; non-canonical
updated: 2026-09-07
authority: current GitHub repository state
base: main@afe3d353023e83eebb8937874312942fbf5bfaf4
---

# Atmosphere / Air Semantic Contract Compatibility Lane

This README records the placement and compatibility posture of contracts/atmosphere. It is a repository-grounded index for an existing path, not a second semantic-contract authority.

## Status at a glance

- The current semantic contract home is contracts/domains/atmosphere/.
- The current machine-shape target is schemas/contracts/v1/domains/atmosphere/.
- contracts/atmosphere/ is a compatibility and placement lane with mixed content.
- The folder currently contains this README and air-observation.schema.json.
- air-observation.schema.json is an empty-property PROPOSED scaffold. Its current location and kfm://contracts/atmosphere/ identifier are placement residue, not an accepted schema authority.
- No migration, deletion, rename, release, publication, source activation, API binding, UI binding, or public promotion is implied by this document.
- This README is intentionally draft and non-canonical until an owner, applicable ADR or migration record, and exact target path are confirmed.

## Authority and placement

Current implementation truth is the GitHub repository at the exact main commit recorded above. Accepted placement authority is ADR-0029 and the adopted Directory Rules snapshot it names. The contracts root owns semantic meaning; it does not become the owner for schemas, policy, fixtures, tests, validators, source registries, lifecycle data, receipts, proofs, releases, runtime behavior, or public behavior.

The current Atmosphere evidence separates the lanes as follows:

| Surface | Current posture | What this README does |
| --- | --- | --- |
| contracts/domains/atmosphere/ | Current semantic-contract home | Points here; does not duplicate its definitions |
| schemas/contracts/v1/domains/atmosphere/ | Current machine-shape target | Points here; does not treat a contract-root schema as canonical |
| schemas/contracts/v1/atmosphere/ | Compatibility/index lane | Retains a pointer to the domain schema lane |
| schemas/contracts/v1/air/ | Compatibility/legacy lane | Retains a bounded placeholder and must not receive a second authority |
| contracts/air/ | Sibling compatibility lane | May carry air-to-atmosphere aliases and placement notes; it does not replace the domain lane |
| contracts/atmosphere/ | This lane | Records compatibility, drift, and migration status only |

The repository already contains an Atmosphere domain lane. Do not create a parallel contracts/air/, schemas/contracts/v1/air/, contracts/atmosphere/, or other authority home merely to satisfy an old path name.

## Current folder inventory

The direct contents observed on main are:

    contracts/atmosphere/
    ├── README.md
    └── air-observation.schema.json

The second file is a schema residue under a contracts root. It currently declares:

- title: Air Observation
- type: object
- additionalProperties: true
- properties: empty
- x-kfm.status: PROPOSED
- x-kfm.path: contracts/atmosphere/air-observation.schema.json
- x-kfm.source_docs: docs/domains/atmosphere/FILE_SYSTEM_PLAN.md
- x-kfm.contract_doc: null

Its $id is kfm://contracts/atmosphere/air-observation.schema.json. That identifier should not be used as evidence that this path is canonical, complete, validated, releasable, or public.

## Scope of this README

This file may:

- identify the current compatibility path and its direct contents;
- point to the current semantic and machine-shape lanes;
- record aliases, unresolved placement drift, migration preconditions, and rollback references;
- summarize repository evidence without promoting proposed scaffolds to accepted contracts;
- preserve the distinction between air terminology and the broader Atmosphere domain.

This file may not:

- define new object semantics or normative fields;
- add or bless schemas, policy, fixtures, validators, tests, registries, receipts, proofs, releases, or runtime behavior;
- declare a source active, rights-cleared, public-safe, health-safe, or life-safety capable;
- make a compatibility path a canonical path by assertion;
- replace an accepted ADR, Directory Rules, contract file, schema registry, validator, or release record.

## Semantic contract inventory

The current semantic lane documents fifteen primary object families plus a resolver-envelope support contract:

1. AirStation
2. AirObservation
3. PM25Observation
4. OzoneObservation
5. SmokeContext
6. AODRaster
7. WeatherStation
8. WeatherObservation
9. WindField
10. PrecipitationObservation
11. TemperatureObservation
12. ClimateNormal
13. ClimateAnomaly
14. ForecastContext
15. AdvisoryContext
16. AtmosphereAirDecisionEnvelope (support contract)

The domain directory also contains lowercase compatibility forms and supporting records such as source-role, validation, correction, sensor-colocation, trigger-candidate, prescribed-burn, and layer-descriptor material. The existence of a markdown file is not proof that its schema, policy, fixtures, tests, source rights, or release gates are complete.

## Current neighboring surfaces

The following repository observations are useful for change review:

| Path | Observed evidence | Interpretation |
| --- | --- | --- |
| contracts/domains/atmosphere/ | 44 direct markdown entries, including the primary families, support contract, lowercase compatibility forms, and supporting records | Current semantic lane; mixed draft/proposed content remains possible |
| schemas/contracts/v1/domains/atmosphere/ | 72 files plus receipts/ and registry/ directories | Machine-shape target; draft/proposed scaffolds and casing mirrors require steward review |
| schemas/contracts/v1/atmosphere/ | Compatibility README | Index only; points toward the domain schema lane |
| schemas/contracts/v1/air/ | README plus AirStation.schema.json | Placeholder/legacy lane; no new authority or duplicate schemas |
| policy/domains/atmosphere/ | README plus 13 Rego files | Proposed/default-only rules; no accepted bundle or evaluator binding is established |
| fixtures/domains/atmosphere/ | README plus 11 child directories | Deterministic/offline fixture index; bounded profiles exist, broader coverage needs verification |
| tests/domains/atmosphere/ | README, Python test modules, and six child directories | Bounded no-network and separation checks; not a contract or release authority |
| docs/domains/atmosphere/ | Draft explanatory documentation | Documentation and boundaries; not a publisher or public-safety authority |

## Air and Atmosphere boundaries

Use the domain lane for semantic meaning and keep these distinctions explicit:

- AQI is not pollutant concentration.
- AOD is not surface PM2.5.
- Forecast, model, reanalysis, or fusion output is not an observation.
- A low-cost sensor is not a regulatory monitor.
- AirNow preliminary or operational context is not the AQS certified archive.
- Smoke, plume, hotspot, or prescribed-burn context is not ground-level exposure, a health effect, an evacuation order, or emergency authority.
- Climate normals and anomalies are not current weather observations.
- Advisory context is not a KFM-issued alert or instruction.
- A receipt is not proof; proof is not review; review is not promotion; promotion is not release, deployment, or publication.
- A derived tile, raster, index, graph edge, dashboard, or AI answer is not sovereign evidence.
- Stale data is not automatically false; correction, supersession, withdrawal, freshness, and lineage remain visible.

Cross-domain ownership remains separate. Hazards owns emergency and life-safety authority. Agriculture owns crop and field claims. Soil owns soil properties and soil-moisture truth. Hydrology owns gauge, watershed, flood, and hydrologic truth. Other domains retain their own canonical ecological, infrastructure, and network claims. Atmosphere may provide governed context or forcing without borrowing another domain's authority.

## Lifecycle and migration posture

A future migration from this lane must be explicit and reversible:

1. Re-pin main and inspect the exact target tree, current contracts/domains/atmosphere content, schema registries, policy, fixtures, tests, and open work.
2. Assign an owner and record the applicable ADR or migration decision for the air-observation residue.
3. Preserve an alias or compatibility note while deciding whether the file moves to schemas/contracts/v1/domains/atmosphere/ or is retired as an empty scaffold.
4. If a schema is retained, define its machine identity, required fields, source-role semantics, units, evidence references, rights, sensitivity, and migration fixtures in the canonical schema lane.
5. Pair any retained schema change with contract, policy, fixture, validator, test, registry, receipt, and rollback evidence as required by repository rules.
6. Verify no public API, UI, map, release, source activation, or runtime path reads the residue directly.
7. Update this README only after the target path, alias behavior, and rollback are reviewable.

Until those steps are complete, the safe posture is HOLD: compatibility pointer plus visible residue, with no new definitions in this folder.

## Validation posture

Repository evidence supports these bounded statements:

- The target directory and its two direct files are present on main.
- The semantic contract README identifies contracts/domains/atmosphere/ as the current home.
- The schema-domain README identifies schemas/contracts/v1/domains/atmosphere/ as the machine-shape target.
- The policy, fixture, and test READMEs describe draft, offline, repository-grounded surfaces with bounded profiles.
- The air-observation schema is syntactically shaped as a JSON Schema scaffold but has no properties and no linked contract document.

The following remain unproven by this README:

- complete contract-to-schema coverage for every object family;
- accepted schema registry ownership or a single release-ready version;
- validator, policy evaluator, CI, or hosted-check binding for this exact path;
- scientific validity, source freshness, rights verification, sensitivity clearance, or public-release eligibility;
- API, MapLibre, dashboard, catalog, graph, or AI-consumer safety;
- migration or rollback completion for air-observation.schema.json.

A documentation-only update does not run repository tests, schema validation, Rego evaluation, workflow checks, browser/runtime checks, release checks, or live connectors.

## Source, rights, sensitivity, and public boundary

Any future Atmosphere or Air record must carry an explicit knowledge character and source role. Observed, modeled, derived, remote-sensing, advisory, and context records must not be collapsed. Rights, terms, attribution, sensitivity, retention, and public_release_allowed state must remain attached to the source descriptor and evidence path. Unknown rights or unresolved sensitivity block public promotion; they do not become safe through a compatibility alias.

This lane has no source activation, network fetch, production retrieval, public publication, emergency dispatch, or health decision authority.

## Evidence ledger

| Evidence | Exact reference | Role |
| --- | --- | --- |
| Current main | afe3d353023e83eebb8937874312942fbf5bfaf4 | Base for this draft |
| Prior target README | e366429f3ff6c53d11faea39e7a64251a803811a | Rollback blob; prior file was not blank |
| Target schema residue | c99cde1da161a39db8cb041855d91cbbb52649cf | Current air-observation.schema.json |
| Semantic contract README | 2626d011b5d80e6d58870be3eff817d95116ffc7 | Current contracts/domains/atmosphere placement evidence |
| Domain schema README | cad321bf62d7da2a723388d5978e04fbfc694b5b | Current machine-shape lane evidence |
| Air schema compatibility README | 6f2504a9054769f343cc33424171ebdb80157576 | Legacy/placeholder path evidence |
| Contracts root README | e0b7c126e00a8ac6e8890774ed26cf21aef534ba | Contracts responsibility boundary |
| ADR-0029 | a4de0d7a96b78da59cfc499d1025e1508afd8dd9 | Accepted placement authority |
| Policy README | a300dfd5abda1b58a07fd978935dd40ef232ec71 | Proposed/default-only policy posture |
| Fixture README | 121ec0e4547384cb14f1a46ca6e93cbdbcc9c4b1 | Deterministic/offline fixture posture |
| Test README | 29204b56a1e35ff74ba8a2e33bd8a424175e9dab | Bounded no-network test posture |
| Docs README | 7e7a96a3f22547fd12afcce5dc7ccd82ddd226af | Explanatory docs boundary |
| Notion builder page | https://app.notion.com/p/3caa92021bf68112bb24dac33bca6357?pvs=204 | Coordination and historical handoff only |
| Drive architecture report | https://drive.google.com/file/d/1gHk6Jp3fGfrPTgvczwxyNXxvNopiKgRw/view | Read-only lineage; its unmounted-repo result is historical |

Notion remains a coordination projection. Google Drive remains read-only lineage. Current GitHub state, accepted placement decisions, and exact-head checks control implementation claims.

## Definition of done for a future migration

- [ ] Current main and the target tree are re-pinned immediately before change.
- [ ] An owner and applicable ADR or migration record are named.
- [ ] The air-observation residue is classified as move, alias, or retire.
- [ ] Canonical contract and schema paths are unambiguous.
- [ ] Contract, schema, policy, fixture, validator, test, registry, and rollback coverage is independently checked.
- [ ] Source role, knowledge character, units, rights, sensitivity, freshness, and public boundary are explicit.
- [ ] No public API, UI, map, release, source activation, or runtime path bypasses the governed lanes.
- [ ] Exact-head validation is recorded with PASS, FAIL, SKIPPED, NOT_RUN, or UNKNOWN labels.
- [ ] The change remains reviewable, draft, reversible, and unmerged until independently approved.

## Rollback

To restore the prior README content, use blob e366429f3ff6c53d11faea39e7a64251a803811a from the pre-change main commit. Do not delete air-observation.schema.json as part of a README-only update. Any schema move, rename, or retirement requires its own reviewed change, migration record, and rollback plan.

## Review note

Last reviewed: 2026-09-07 against main@afe3d353023e83eebb8937874312942fbf5bfaf4. This is a docs-only draft update. It does not merge, mark ready, approve, release, deploy, publish, activate a source, change settings, or claim passing hosted checks.

