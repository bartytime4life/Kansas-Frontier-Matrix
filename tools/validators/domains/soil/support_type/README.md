<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-domains-soil-support-type-readme
title: tools/validators/domains/soil/support_type README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-soil-steward-plus-soil-contract-steward-plus-source-steward-plus-evidence-steward-plus-policy-steward-plus-release-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; per-domain-validator; soil; support-type; support-type-separation; source-role-aware; static-survey; gridded-derivative; station-observation; satellite-grid; pedon-profile; interpretation; release-gated; non-authoritative
owning_root: tools/
responsibility: proposed Soil-specific support-type validator lane for checking static survey, gridded derivative, station observation, satellite grid, pedon/profile, interpretation, suitability, erosion-risk, hydrologic group, and public-safe derivative support labels, source-role separation, time/vintage posture, unit/method posture, EvidenceRef/EvidenceBundle posture, policy, release, correction, rollback, and public-surface denial posture while deferring Soil meaning, support-type vocabulary authority, source registry authority, evidence records, policy decisions, proof records, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../../README.md
  - ../../../README.md
  - ../../../_common/README.md
  - ../catalog_closure/README.md
  - ../dual_hash/README.md
  - ../horizon_depth/README.md
  - ../lineage/README.md
  - ../moisture/README.md
  - ../../../catalog_closure/README.md
  - ../../../cross-domain-joins/README.md
  - ../../../../../contracts/domains/soil/README.md
  - ../../../../../contracts/domains/soil/soil_moisture_observation.md
  - ../../../../../contracts/domains/soil/soil_property.md
  - ../../../../../contracts/domains/soil/hydrologic_soil_group.md
  - ../../../../../contracts/domains/soil/erosion_risk.md
  - ../../../../../contracts/domains/soil/suitability_rating.md
  - ../../../../../contracts/domains/soil/soil_time_caveat.md
  - ../../../../../docs/domains/soil/README.md
  - ../../../../../docs/domains/soil/CANONICAL_PATHS.md
  - ../../../../../docs/domains/soil/DATA_LIFECYCLE.md
  - ../../../../../docs/runbooks/soil/PROMOTION_RUNBOOK.md
  - ../../../../../docs/runbooks/soil/ROLLBACK_RUNBOOK.md
  - ../../../../../data/registry/sources/soil/README.md
  - ../../../../../data/catalog/domain/soil/README.md
  - ../../../../../data/proofs/soil/README.md
  - ../../../../../data/receipts/
  - ../../../../../release/
notes:
  - "This README replaces an empty file. It does not confirm executable files."
  - "Soil contract evidence says support type is part of meaning and that static survey, gridded derivative, station observation, satellite grid, pedon/profile, and interpretation are not interchangeable."
  - "Soil proof evidence says support-type separation is mandatory: static survey, gridded derivative, station reading, satellite grid, pedon evidence, and interpretation cannot masquerade as one surface."
  - "This validator lane checks support-type posture only. It must not define Soil meaning, create SourceDescriptors, create EvidenceBundles, approve release, publish layers, certify agronomic suitability, or provide operational/engineering/legal/hazard advice."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/domains/soil/support_type

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-soil--support--type-informational)
![boundary](https://img.shields.io/badge/boundary-validator--only-lightgrey)
![invariant](https://img.shields.io/badge/invariant-no--support--collapse-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/domains/soil/support_type/` is the proposed Soil-specific validator lane for checking whether Soil records, catalog entries, proof references, release candidates, map/API payloads, Focus Mode context, and AI context preserve support-type separation before public or governed use.

---

## Purpose

`tools/validators/domains/soil/support_type/` exists for Soil support-type checks under the durable `tools/validators/` surface.

The durable KFM question for this lane is:

> Do Soil candidates declare and preserve their support type — static survey, gridded derivative, station observation, satellite grid, pedon/profile, interpretation, or accepted equivalent — with source role, time/vintage, units/method, EvidenceRef/EvidenceBundle posture, policy, release, correction, rollback, and public-use limitations intact before they are used by catalog, proof, release, map, API, graph, Focus Mode, export, or AI surfaces?

The answer should be a deterministic validation result. This folder should not create Soil truth, support-type vocabulary, source truth, SourceDescriptors, EvidenceBundles, receipts, proofs, PolicyDecisions, ReleaseManifests, public map layers, API payloads, AI answers, or publication approval.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/domains/soil/support_type/README.md` | **CONFIRMED** | This README replaces the previous empty file. |
| Parent `tools/validators/domains/soil/README.md` | **CONFIRMED stub** | Parent file currently says only `# validators :: soil`; this README keeps its own boundary explicit. |
| Soil contract-lane support-type doctrine | **CONFIRMED in repo evidence / draft** | `contracts/domains/soil/README.md` says support type is part of meaning and lists static survey, gridded derivative, station observation, satellite grid, pedon/profile, and interpretation as non-interchangeable support classes. |
| Soil proof-lane support-type doctrine | **CONFIRMED in repo evidence / draft** | `data/proofs/soil/README.md` says support-type separation is mandatory and that static survey, gridded derivative, station reading, satellite grid, pedon evidence, and interpretation cannot masquerade as one surface. |
| Soil catalog posture | **CONFIRMED in repo evidence / draft** | `data/catalog/domain/soil/README.md` says Soil catalog records must keep support types separate and preserve source, evidence, policy, receipts, release, correction, and rollback linkage. |
| Support-type schema, exact field name, fixture set, and CI wiring | **PROPOSED / NEEDS VERIFICATION** | This README does not claim that a support-type schema, executable, fixture set, runtime integration, or CI check exists. |

[Back to top](#top)

---

## Proposed validation focus

Until a Soil contract/schema/source profile confirms exact field names and accepted vocabulary, this README treats the following as proposed validation concepts, not implemented fields:

| Support type | Typical source family | Must not be treated as |
|---|---|---|
| `static_survey` | SSURGO / SDA-backed survey attributes / gNATSGO-style survey support | Live observation, farm-specific condition, station reading, or operational advice. |
| `gridded_derivative` | gSSURGO, rasterized survey products, derived grids | Source-of-record polygon, station observation, or field-verified condition. |
| `station_observation` | Mesonet / SCAN / USCRN-style measurements | Countywide truth, survey map unit, gridded satellite product, or management recommendation. |
| `satellite_grid` | SMAP-style gridded observations | Station reading, SSURGO map unit, private sensor feed, or field-verified condition. |
| `pedon_profile` | Pedon records, profile descriptions, lab/profile data | Map-unit truth by itself, countywide surface, or source-independent property. |
| `interpretation` | Erosion risk, suitability, hydrologic soil group, derived rating | Legal, hazard, crop, engineering, economic, or operational advice. |
| `public_safe_derivative` | Released generalized/aggregated/map/API derivative | Canonical/internal truth, raw source, proof closure, policy approval, or release approval by itself. |

A future implementation may choose different field names or enumerations. The invariant is stronger than the names: **support type must remain visible, evidence-bound, policy-aware, and non-interchangeable**.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Soil-specific support-type validator entrypoints | `tools/validators/domains/soil/support_type/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Soil validator parent index | `tools/validators/domains/soil/` |
| Soil catalog closure validator | `tools/validators/domains/soil/catalog_closure/` |
| Soil dual-hash validator | `tools/validators/domains/soil/dual_hash/` |
| Soil horizon-depth validator | `tools/validators/domains/soil/horizon_depth/` |
| Soil lineage validator | `tools/validators/domains/soil/lineage/` |
| Soil moisture validator | `tools/validators/domains/soil/moisture/` |
| Soil support-type meaning | `contracts/domains/soil/`, `docs/domains/soil/`, or accepted contract/doctrine home |
| Soil schemas | `schemas/contracts/v1/domains/soil/`, `schemas/contracts/v1/soil/`, or ADR-selected schema home |
| Soil policy rules | `policy/domains/soil/` or accepted policy homes |
| Soil source descriptors and source registry | `data/registry/sources/soil/` or accepted source registry home |
| Soil catalog records | `data/catalog/domain/soil/` or accepted catalog home |
| EvidenceBundle and proof support | `data/proofs/soil/`, `data/proofs/` |
| Receipts and run memory | `data/receipts/` |
| Release decisions, manifests, rollback, corrections | `release/` |
| Tests and fixtures | `tests/validators/domains/soil/support_type/`, `tests/domains/soil/`, `fixtures/domains/soil/`, or accepted conventions |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live here when it checks declared Soil support-type, source-role, evidence, policy, and release-reference rules.
- **NEEDS VERIFICATION:** exact executable names, field names, schema homes, accepted vocabulary, source mappings, fixture shape, policy bundles, report destinations, receipts, release integration, runtime behavior, and CI wiring.
- **DENY:** using this folder as Soil doctrine, support-type vocabulary authority, schema home, policy home, source registry, catalog storage, proof storage, receipt storage, lifecycle data store, release record store, published artifact store, public runtime surface, operational advice surface, or agronomic/engineering/legal/hazard recommendation authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/domains/soil/support_type/` include checks that:

- verify every consequential Soil candidate declares an accepted support type or abstains;
- verify support type remains paired with source role, source family, time/vintage, units/method, EvidenceRef/EvidenceBundle posture, policy, release, correction, and rollback references where required;
- detect when static survey records are treated as live observations, station readings, private field conditions, or operational advice;
- detect when gridded derivatives are treated as source-of-record survey polygons or station readings;
- detect when station observations are treated as countywide surfaces, satellite grids, survey map units, or management recommendations;
- detect when satellite-grid products are treated as station readings, private sensors, survey map units, or field-verified conditions;
- detect when pedon/profile evidence is treated as map-unit truth without appropriate support and evidence closure;
- detect when interpretations such as erosion risk, suitability, or hydrologic soil group are treated as legal, hazard, crop, economic, engineering, or operational advice;
- ensure public-safe derivatives remain derived/released projections, not canonical internal truth or proof closure;
- emit deterministic validation reports without creating receipts, proofs, release manifests, public artifacts, or operational recommendations.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/domains/soil/support_type/` | Correct home |
|---|---|
| Soil support-type meaning and contract prose | `contracts/domains/soil/`, `docs/domains/soil/`, or accepted contract/doctrine home |
| Soil support-type schema or enum | `schemas/contracts/v1/domains/soil/`, `schemas/contracts/v1/soil/`, or accepted schema home |
| Soil source descriptors and source mappings | `data/registry/sources/soil/` or accepted source registry/source-profile home |
| Soil domain docs | `docs/domains/soil/` |
| Soil policy rules | `policy/domains/soil/` or accepted policy homes |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| EvidenceBundles, proofs, receipts, ValidationReports, ModelRunReceipts | `data/proofs/`, `data/receipts/` |
| Release manifests, decisions, rollback, corrections | `release/` |
| Pipeline execution logic, ETL, or source parsers | `pipelines/domains/soil/`, `packages/domains/soil/`, or accepted implementation roots |
| Generated QA reports that are not source code | `artifacts/qa/` or accepted report lane |
| Tests and fixtures | `tests/` and fixture conventions |
| Public API, UI, map, tile, export, search, graph, Focus Mode, AI runtime code, operational advice, agronomic recommendation, legal determination, engineering recommendation, or hazard warning output | governed application/runtime roots |

[Back to top](#top)

---

## Soil support-type validator posture

This validator lane must fail closed, deny, abstain, or route to review when a candidate:

- lacks source descriptor, source role, source family, support type, source vintage, units/method, EvidenceRef, EvidenceBundle/proof reference, validation report, policy posture, release reference, correction path, or rollback target required for its use;
- collapses static survey, gridded derivative, station observation, satellite grid, pedon/profile, interpretation, public-safe derivative, candidate, or private operational support classes;
- treats SSURGO/gNATSGO/SDA survey support as current field condition, parcel/farm truth, Hydrology truth, crop/yield truth, or operational recommendation;
- treats gSSURGO/rasterized derivative support as source-of-record polygon truth without source/provenance caveats;
- treats Mesonet/SCAN/USCRN station support as countywide truth, survey map-unit truth, satellite-grid truth, or management advice;
- treats SMAP/satellite-grid support as station reading, survey map-unit truth, private sensor feed, or field-verified condition;
- treats pedon/profile support as map-unit truth or countywide surface without evidence and release closure;
- treats interpretations such as erosion risk, suitability rating, or hydrologic soil group as legal, hazard, crop, economic, engineering, or operational advice;
- treats public-safe derivatives as canonical/internal truth, proof closure, policy approval, or release approval;
- allows catalog, proof, release, map, API, graph, Focus Mode, export, or AI surfaces to depend on support-type-collapsed Soil records;
- points public surfaces at RAW, WORK, QUARANTINE, unresolved candidates, direct internal stores, stale readings, stale source descriptors, or incomplete proof closure;
- treats support-type validation as EvidenceBundle creation, PolicyDecision creation, release approval, publication, operational advice, or public API behavior.

The validator lane must preserve the KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `SOIL_SUPPORT_TYPE_PASS` | Configured Soil support-type checks passed. |
| `SOIL_SUPPORT_TYPE_FAIL` | One or more configured Soil support-type checks failed. |
| `SOIL_SUPPORT_TYPE_MISSING` | Required support-type label is absent. |
| `SOIL_SUPPORT_TYPE_UNKNOWN` | Support-type label is not accepted by configured schema/policy/source profile. |
| `SOIL_STATIC_SURVEY_COLLAPSE` | Static survey support is treated as live observation, private condition, or operational advice. |
| `SOIL_GRIDDED_DERIVATIVE_COLLAPSE` | Gridded derivative support is treated as source-of-record polygon or station truth. |
| `SOIL_STATION_OBSERVATION_COLLAPSE` | Station observation support is treated as countywide, survey, satellite-grid, or advisory truth. |
| `SOIL_SATELLITE_GRID_COLLAPSE` | Satellite-grid support is treated as station, survey, private-sensor, or field-verified truth. |
| `SOIL_PEDON_PROFILE_COLLAPSE` | Pedon/profile support is treated as map-unit truth or broad public surface without support. |
| `SOIL_INTERPRETATION_COLLAPSE` | Interpretive support is treated as legal, hazard, crop, engineering, economic, or operational advice. |
| `SOIL_PUBLIC_DERIVATIVE_COLLAPSE` | Public-safe derivative is treated as canonical truth, proof closure, or release approval. |
| `SOIL_SOURCE_ROLE_MISSING` | Required source-role posture is absent. |
| `SOIL_EVIDENCE_REF_MISSING` | Required EvidenceRef, EvidenceBundle, or proof reference is absent. |
| `SOIL_POLICY_OR_RELEASE_GAP` | Required policy, review, release, correction, or rollback support is absent. |
| `SOIL_CROSS_DOMAIN_AUTHORITY_COLLAPSE` | Candidate absorbs another domain's truth into Soil without preserving boundaries. |
| `SOIL_PUBLIC_SURFACE_LEAK_RISK` | Candidate is unsafe for public/governed output as shaped. |
| `SOIL_LIFECYCLE_VIOLATION` | Candidate appears to skip required lifecycle states. |
| `REPORT_DESTINATION_INVALID` | QA report or receipt destination is outside an accepted root. |
| `ABSTAIN` | Validator cannot decide safely with available context. |
| `ERROR` | Validator could not safely complete. |

[Back to top](#top)

---

## Validation

Suggested future test surface:

```text
tests/validators/domains/soil/support_type/
├── README.md
├── test_soil_support_type.py
└── fixtures/
    ├── valid_static_survey_support/
    ├── valid_gridded_derivative_support/
    ├── valid_station_observation_support/
    ├── valid_satellite_grid_support/
    ├── valid_pedon_profile_support/
    ├── valid_interpretation_support/
    ├── missing_support_type/
    ├── unknown_support_type/
    ├── station_as_countywide_truth_denied/
    ├── satellite_as_station_truth_denied/
    ├── interpretation_as_advice_denied/
    └── cross_domain_authority_collapse/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/domains/soil/support_type
```

```bash
python tools/validators/domains/soil/support_type/validate_soil_support_type.py --repo-root . --format json
```

> [!NOTE]
> This is a proposed interface, not proof that `validate_soil_support_type.py` or the test path exists.

[Back to top](#top)

---

## Review checklist

- [ ] Validator reads declared Soil contracts, schemas, source descriptors, source-role rules, and policy rather than defining meaning locally.
- [ ] Static survey, gridded derivative, station observation, satellite grid, pedon/profile, interpretation, and public-safe derivative support types remain distinct.
- [ ] Source role, source family, time/vintage, units/method, EvidenceRef support, policy posture, and public-use limitations remain visible.
- [ ] Support-type checks do not replace SourceDescriptor, EvidenceBundle, proof, receipt, PolicyDecision, ReleaseManifest, correction, or rollback records.
- [ ] Cross-domain joins preserve Agriculture, Hydrology, Atmosphere, Habitat, Fauna, Flora, Geology, and Hazards ownership boundaries.
- [ ] Public-bound outputs never point clients at RAW, WORK, QUARANTINE, unresolved candidates, direct internal stores, private operational sensors, stale readings, or source-role-collapsed candidates.
- [ ] Reports and receipts are written only to accepted roots.
- [ ] Validator output is not described as truth, policy, release, publication, operational advice, source authority, or Directory Rules approval.
- [ ] Tests use public-safe or synthetic fixtures.
- [ ] Executable claims are backed by current repo evidence.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-08 |
| Review state | Draft README replacement for empty Soil support-type validator file. |
| Next smallest safe change | Verify actual Soil support-type scripts, accepted field names, support-type vocabulary, schemas, source mappings, source descriptors, fixtures, report destinations, receipts, release linkage, cross-domain join behavior, and CI/runtime wiring before promoting this lane beyond draft. |
