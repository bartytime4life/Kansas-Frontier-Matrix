<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-atmosphere-readme
title: contracts/atmosphere/ — Atmosphere / Air Contract Compatibility Index
type: readme; directory-readme; compatibility-index
version: v0.3
status: draft; repository-grounded; compatibility-index; mixed-content; non-canonical
owners: OWNER_TBD — Atmosphere steward · Contract steward · Schema steward · Policy steward · Validation steward · Release steward · Docs steward
created: 2026-06-20
updated: 2026-09-07
policy_label: public; contracts; atmosphere; air; compatibility; no-parallel-authority; cite-or-abstain
related:
  - ../README.md
  - ../air/README.md
  - ../domains/atmosphere/README.md
  - ../../docs/domains/atmosphere/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../schemas/contracts/v1/domains/atmosphere/README.md
  - ../../schemas/contracts/v1/atmosphere/README.md
  - ../../schemas/contracts/v1/air/README.md
  - ../../policy/domains/atmosphere/README.md
  - ../../fixtures/domains/atmosphere/README.md
  - ../../tests/domains/atmosphere/README.md
tags: [kfm, contracts, atmosphere, air, compatibility, semantic-contracts, object-families, source-role, evidence, governance]
notes:
  - "This path is a compatibility and placement index, not a second semantic-contract authority."
  - "The direct inventory is README.md plus air-observation.schema.json; the schema is an empty-property PROPOSED residue under a contracts root."
  - "Current semantic meaning belongs under contracts/domains/atmosphere/; current machine shape belongs under schemas/contracts/v1/domains/atmosphere/."
  - "No migration, source activation, release, publication, API/UI binding, or life-safety authority is implied."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Atmosphere / Air Contract Compatibility Index

This README explains what the historical contracts/atmosphere path currently means, what it contains, and where maintained semantic and machine-shape material belongs. It is a repository-grounded compatibility index, not a second writable contract authority.

## Contents

- [Status](#status)
- [Placement and related paths](#placement-and-related-paths)
- [Direct inventory](#direct-inventory)
- [Scope and non-goals](#scope-and-non-goals)
- [Semantic inventory and boundaries](#semantic-inventory-and-boundaries)
- [Migration and lifecycle](#migration-and-lifecycle)
- [Validation and maintenance](#validation-and-maintenance)
- [Evidence ledger](#evidence-ledger)
- [Definition of done](#definition-of-done)
- [Rollback and review note](#rollback-and-review-note)

## Status

> [!IMPORTANT]
> **Status:** draft / compatibility index / mixed content  
> **Path:** contracts/atmosphere/  
> **Semantic home:** [contracts/domains/atmosphere/](../domains/atmosphere/README.md)  
> **Machine-shape target:** [schemas/contracts/v1/domains/atmosphere/](../../schemas/contracts/v1/domains/atmosphere/README.md)  
> **Current posture:** the requested path exists, but its schema residue is not canonical, complete, validated, releasable, or public.

The direct folder inventory is confirmed on current main. The previous documentation correction was merged in [PR #4409](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/4409); this follow-up is a new docs-only draft. No migration, deletion, rename, release, publication, source activation, API binding, UI binding, or public promotion is implied.

## Placement and related paths

Current implementation truth is the exact GitHub repository state. Accepted placement guidance is [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) together with the adopted [Directory Rules](../../docs/doctrine/directory-rules.md). The [contracts root guidance](../README.md) assigns semantic meaning to contracts and keeps schemas, policy, fixtures, tests, validators, registries, lifecycle data, receipts, proofs, release state, runtime behavior, and public behavior in their responsibility roots.

| Surface | Current posture | Role of this README |
| --- | --- | --- |
| [contracts/domains/atmosphere/](../domains/atmosphere/README.md) | Current semantic-contract home | Point here; do not duplicate definitions |
| [schemas/contracts/v1/domains/atmosphere/](../../schemas/contracts/v1/domains/atmosphere/README.md) | Current machine-shape target | Point here; do not treat a contract-root schema as canonical |
| [contracts/air/](../air/README.md) | Merged sibling compatibility/index lane | Preserve the historical air slug without creating another authority |
| [schemas/contracts/v1/atmosphere/](../../schemas/contracts/v1/atmosphere/README.md) | Atmosphere schema compatibility index | Retain as a pointer, not a second schema home |
| [schemas/contracts/v1/air/](../../schemas/contracts/v1/air/README.md) | Air schema compatibility/legacy lane | Retain its bounded placeholder; add no parallel definitions |
| contracts/atmosphere/ | This path | Record direct contents, drift, aliases, and migration conditions only |
| [docs/domains/atmosphere/](../../docs/domains/atmosphere/README.md) | Explanatory domain documentation | Use for domain scope and boundaries, not implementation authority |
| [policy/domains/atmosphere/](../../policy/domains/atmosphere/README.md) | Proposed/default-only policy lane | Use for policy posture; do not infer an accepted evaluator or bundle |
| [fixtures/domains/atmosphere/](../../fixtures/domains/atmosphere/README.md) | Deterministic/offline fixture index | Use for bounded examples; fixtures are not evidence or release state |
| [tests/domains/atmosphere/](../../tests/domains/atmosphere/README.md) | Bounded domain test lane | Use for test posture; tests do not become contract authority |

Do not create a parallel contracts/air/, contracts/atmosphere/, schemas/contracts/v1/air/, schemas/contracts/v1/atmosphere/, or other authority home merely to satisfy a historical path name.

## Direct inventory

The direct contents observed on current main are:

~~~text
contracts/atmosphere/
├── README.md
└── air-observation.schema.json
~~~

The second file is a schema residue under a contracts root. Its current shape is:

| Field | Observed value | Meaning |
| --- | --- | --- |
| title | Air Observation | Descriptive title only |
| type | object | Broad JSON Schema type |
| additionalProperties | true | Open scaffold, not a constrained contract |
| properties | empty | No normative fields are defined |
| x-kfm.status | PROPOSED | Proposed scaffold, not accepted shape |
| x-kfm.path | contracts/atmosphere/air-observation.schema.json | Historical placement record |
| x-kfm.source_docs | [FILE_SYSTEM_PLAN.md](../../docs/domains/atmosphere/FILE_SYSTEM_PLAN.md) | Lineage pointer only |
| x-kfm.contract_doc | null | No linked contract document |

Its identifier is kfm://contracts/atmosphere/air-observation.schema.json. That identifier must not be used as evidence that the file is canonical, complete, validated, releasable, or public.

## Scope and non-goals

This README may:

- identify the current path and direct contents;
- link to the maintained semantic, schema, policy, fixture, test, and domain-documentation lanes;
- record aliases, placement drift, migration preconditions, and rollback references;
- summarize current repository evidence without promoting proposed scaffolds;
- preserve the distinction between the historical air slug and the broader Atmosphere domain.

This README does not:

- define new object semantics or normative fields;
- add or bless schemas, policy, fixtures, validators, tests, registries, receipts, proofs, releases, or runtime behavior;
- declare a source active, rights-cleared, public-safe, health-safe, or life-safety capable;
- make a compatibility path canonical by assertion;
- replace an accepted ADR, Directory Rules, contract file, schema registry, validator, or release record.

## Semantic inventory and boundaries

The maintained semantic lane documents fifteen primary object families plus a support decision envelope:

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

The domain directory also contains lowercase compatibility forms and supporting records for source role, validation, correction, sensor colocation, trigger candidates, prescribed burns, and layer descriptors. A Markdown file is not proof that its schema, policy, fixtures, tests, source rights, or release gates are complete.

Preserve these non-collapse rules:

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

Cross-domain ownership remains separate. Hazards owns emergency and life-safety authority. Agriculture owns crop and field claims. Soil owns soil properties and soil-moisture truth. Hydrology owns gauge, watershed, flood, and hydrologic truth. Other domains retain their own ecological, infrastructure, and network claims. Atmosphere may provide governed context or forcing without borrowing another domain's authority.

## Migration and lifecycle

Any migration of air-observation.schema.json must be explicit, dependency-closed, and reversible:

1. Re-pin current main and inspect the target tree, semantic contracts, schema registry, policy, fixtures, tests, and open work.
2. Name an owner and record the applicable ADR or migration decision.
3. Choose one outcome: move the schema to the domain schema lane, retain a documented compatibility alias, or retire the empty scaffold.
4. If retained, define machine identity, required fields, source role, units, evidence references, rights, sensitivity, and migration fixtures in the maintained schema lane.
5. Pair a retained schema with the relevant contract, policy, fixture, validator, test, registry, receipt, and rollback evidence.
6. Verify that no public API, UI, map, release, source activation, or runtime path reads this residue directly.
7. Update this README only after the target path, alias behavior, and rollback are reviewable.

Until then, the safe posture is HOLD: visible compatibility pointer plus visible residue, with no new definitions in this folder.

## Validation and maintenance

### Confirmed on current main

- The target folder contains README.md and air-observation.schema.json.
- The semantic README identifies contracts/domains/atmosphere/ as the current contract home.
- The schema-domain README identifies schemas/contracts/v1/domains/atmosphere/ as the machine-shape target.
- The sibling contracts/air/ compatibility README is present on main.
- Policy, fixture, test, and documentation READMEs describe draft or bounded surfaces.
- The residue schema has no properties and no linked contract document.

### Still unproven

- Complete contract-to-schema coverage for every object family.
- Accepted schema registry ownership or a release-ready version.
- Validator, policy evaluator, CI, or hosted-check binding for this exact residue path.
- Scientific validity, source freshness, rights verification, sensitivity clearance, or public-release eligibility.
- API, MapLibre, dashboard, catalog, graph, or AI-consumer safety.
- Migration or rollback completion for air-observation.schema.json.

### Documentation update checklist

For future edits to this README:

- Re-pin current main before drafting.
- Fetch every linked path whose status or role is being changed.
- Review headings, anchors, tables, code fences, links, and direct inventory.
- Keep proposed, unknown, and confirmed claims visibly distinct.
- Re-fetch the branch blob and compare changed paths before opening or updating a draft PR.
- Report repository tests, schema validation, Rego evaluation, hosted checks, browser/runtime checks, release checks, and live connectors as not run unless actually executed.

## Evidence ledger

| Evidence | Exact reference | Role |
| --- | --- | --- |
| Current main | [f73daca](https://github.com/bartytime4life/Kansas-Frontier-Matrix/commit/f73dacaee38d7be1722200fccd2fe73251afb7e3) | Base for this follow-up; includes the merged predecessor |
| Previous documentation update | [PR #4409](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/4409) | Merged README correction; not a current work branch |
| Current target README | [db947e0](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/f73dacaee38d7be1722200fccd2fe73251afb7e3/contracts/atmosphere/README.md) | Prior blob and rollback target |
| Target schema residue | [c99cde1](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/f73dacaee38d7be1722200fccd2fe73251afb7e3/contracts/atmosphere/air-observation.schema.json) | Current proposed empty-property scaffold |
| Semantic contract README | [2626d011](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/contracts/domains/atmosphere/README.md) | Current semantic placement evidence |
| Domain schema README | [cad321bf](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/schemas/contracts/v1/domains/atmosphere/README.md) | Current machine-shape evidence |
| Air compatibility README | [6ee8922](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/contracts/air/README.md) | Merged sibling compatibility posture |
| Contracts root README | [e0b7c126](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/contracts/README.md) | Responsibility-root boundary |
| Directory Rules | [fd49a0b8](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/doctrine/directory-rules.md) | Adopted placement guidance |
| ADR-0029 | [a4de0d7a](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Accepted placement decision |
| Policy README | [a300dfd5](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/policy/domains/atmosphere/README.md) | Proposed/default-only policy posture |
| Fixture README | [121ec0e4](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/fixtures/domains/atmosphere/README.md) | Deterministic/offline fixture posture |
| Test README | [29204b56](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/tests/domains/atmosphere/README.md) | Bounded no-network test posture |
| Domain docs README | [7e7a96a3](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/main/docs/domains/atmosphere/README.md) | Explanatory documentation boundary |
| Notion builder page | [KFM Hourly Atmosphere Domain Builder](https://app.notion.com/p/3caa92021bf68112bb24dac33bca6357?pvs=204) | Coordination and historical handoff only |
| Drive architecture report | [KFM Atmosphere / Air report](https://drive.google.com/file/d/1gHk6Jp3fGfrPTgvczwxyNXxvNopiKgRw/view) | Read-only lineage; its unmounted-repo result is historical |

Notion is a coordination projection. Google Drive is read-only lineage. Current GitHub state, accepted placement decisions, and exact-head checks control implementation claims.

## Definition of done

- [ ] Current main and the target tree are re-pinned immediately before change.
- [ ] An owner and applicable ADR or migration record are named.
- [ ] The schema residue is classified as move, alias, or retire.
- [ ] Semantic and machine-shape paths are unambiguous.
- [ ] Contract, schema, policy, fixture, validator, test, registry, and rollback coverage is independently checked.
- [ ] Source role, knowledge character, units, rights, sensitivity, freshness, and public boundary are explicit.
- [ ] No public API, UI, map, release, source activation, or runtime path bypasses governed lanes.
- [ ] Exact-head validation is recorded with PASS, FAIL, SKIPPED, NOT_RUN, or UNKNOWN labels.
- [ ] The change remains reviewable, draft, reversible, and unmerged until independently approved.

## Rollback and review note

The rollback target for this follow-up is the current main blob [db947e095](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/f73dacaee38d7be1722200fccd2fe73251afb7e3/contracts/atmosphere/README.md). Do not delete air-observation.schema.json as part of a README-only update. Any schema move, rename, or retirement requires its own reviewed change, migration record, and rollback plan.

Last reviewed: 2026-09-07 against main@f73dacaee38d7be1722200fccd2fe73251afb7e3. This follow-up is documentation-only and does not merge, mark ready, approve, release, deploy, publish, activate a source, change settings, or claim passing hosted checks.

<p align="right"><a href="#top">Back to top</a></p>
