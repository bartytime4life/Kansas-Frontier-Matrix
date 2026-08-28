<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-domains-soil-horizon-depth-readme
title: tools/validators/domains/soil/horizon_depth README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-soil-steward-plus-soil-contract-steward-plus-evidence-steward-plus-policy-steward-plus-release-steward
created: 2026-07-07
updated: 2026-07-07
policy_label: repository-facing; per-domain-validator; soil; horizon-depth; SSURGO; component-horizon; pedon; fail-closed; non-authoritative
owning_root: tools/
responsibility: proposed Soil-specific horizon-depth validator lane for checking horizon top/bottom depth ordering, units, non-overlap, gap/continuity posture, component-horizon join consistency, pedon/profile depth posture, source-role separation, Soil identity continuity, evidence, policy, release, correction, rollback, and public-surface denial checks while deferring Soil meaning, schemas, policy decisions, proof records, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../../README.md
  - ../../../README.md
  - ../../../_common/README.md
  - ../catalog_closure/README.md
  - ../dual_hash/README.md
  - ../../../catalog_closure/README.md
  - ../../../cross-domain-joins/README.md
  - ../../../../../docs/domains/soil/README.md
  - ../../../../../docs/domains/soil/CANONICAL_PATHS.md
  - ../../../../../docs/domains/soil/DATA_LIFECYCLE.md
  - ../../../../../docs/runbooks/soil/NO_NETWORK_TEST_RUNBOOK.md
  - ../../../../../docs/runbooks/soil/PROMOTION_RUNBOOK.md
  - ../../../../../docs/runbooks/soil/ROLLBACK_RUNBOOK.md
  - ../../../../../data/registry/sources/soil/
  - ../../../../../data/catalog/domain/soil/
  - ../../../../../data/proofs/
  - ../../../../../data/receipts/
  - ../../../../../release/
notes:
  - "This README replaces an empty file. It does not confirm executable files."
  - "Horizon and Component Horizon Join are confirmed Soil-owned object-family terms in current repo evidence. Exact field names, schema paths, validator names, fixture paths, and executable behavior remain NEEDS VERIFICATION."
  - "This validator lane is for checking Soil horizon-depth integrity only. It must not define Soil horizon meaning, create schemas, decide policy, create EvidenceBundles, approve release, or publish public outputs."
  - "Depth field names such as top_depth, bottom_depth, hzdept, and hzdepb are examples/proposed placeholders until accepted Soil schemas or source mappings are verified."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/domains/soil/horizon_depth

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-soil--horizon--depth-informational)
![boundary](https://img.shields.io/badge/boundary-validator--only-lightgrey)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/domains/soil/horizon_depth/` is the proposed Soil-specific validator lane for checking horizon-depth integrity across Soil horizons, components, pedons/profile views, component-horizon joins, catalog entries, proof references, release candidates, and public-safe derivatives.

---

## Purpose

`tools/validators/domains/soil/horizon_depth/` exists for Soil horizon-depth checks under the durable `tools/validators/` surface.

The durable KFM question for this lane is:

> Do Soil horizon-depth candidates preserve horizon identity, component/profile context, depth units, top/bottom ordering, non-overlap, gap/continuity posture, source-role labels, evidence references, policy posture, release references, correction lineage, rollback targets, and public-surface boundaries before they are used by catalog, proof, release, map, API, graph, Focus Mode, or AI surfaces?

The answer should be a deterministic validation result. This folder should not create Soil truth, source truth, horizon meaning, schema fields, EvidenceBundles, receipts, proofs, PolicyDecisions, ReleaseManifests, public map layers, API payloads, AI answers, or publication approval.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/domains/soil/horizon_depth/README.md` | **CONFIRMED** | This README replaces the previous empty file. |
| Parent `tools/validators/domains/soil/README.md` | **CONFIRMED stub** | Parent file currently says only `# validators :: soil`; this README keeps its own boundary explicit. |
| Soil object-family evidence | **CONFIRMED in repo evidence / draft** | Current Soil lifecycle evidence names `Horizon`, `Pedon / SoilProfileView`, and `Component Horizon Join` among Soil-owned object families. |
| Soil canonical placement evidence | **CONFIRMED in repo evidence / draft** | Soil canonical-path evidence says Soil files appear as domain segments under responsibility roots and that path presence remains proposed until verified. |
| No-network test doctrine | **CONFIRMED in repo evidence / draft** | Soil no-network runbook describes synthetic fixture posture and trust-spine testing before live source admission; concrete validator names remain proposed. |
| Horizon-depth schema, exact fields, units, fixtures, source mappings, and CI wiring | **PROPOSED / NEEDS VERIFICATION** | This README does not claim that a horizon-depth schema, executable, fixture set, source mapping, runtime integration, or CI check exists. |

[Back to top](#top)

---

## Proposed validation focus

Until a Soil contract/schema confirms exact field names, this README treats the following as proposed validation concepts, not implemented fields:

| Concept | Proposed meaning | Notes |
|---|---|---|
| Horizon top depth | The upper boundary of a soil horizon within a component, pedon, or profile view. | Example field names might include `top_depth`, `hzdept`, or accepted schema equivalents. |
| Horizon bottom depth | The lower boundary of a soil horizon within the same context. | Example field names might include `bottom_depth`, `hzdepb`, or accepted schema equivalents. |
| Depth unit | The unit used by the source and normalized KFM record. | Unit normalization must be explicit and evidence-bound. |
| Horizon order | The vertical sequence of horizons within one component/profile context. | Ordering must not rely on row order alone unless the source contract allows it. |
| Continuity posture | Whether gaps, overlaps, missing bounds, or partial ranges are allowed, denied, or routed to review. | Accepted rules must come from Soil contracts, schemas, source mappings, or policy. |
| Component-horizon join | The linkage between SoilComponent and Horizon records. | Join integrity must preserve source role, identity keys, and EvidenceBundle support. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Soil-specific horizon-depth validator entrypoints | `tools/validators/domains/soil/horizon_depth/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Soil validator parent index | `tools/validators/domains/soil/` |
| Soil catalog closure validator | `tools/validators/domains/soil/catalog_closure/` |
| Soil dual-hash validator | `tools/validators/domains/soil/dual_hash/` |
| Soil domain meaning and doctrine | `docs/domains/soil/`, `contracts/domains/soil/`, `contracts/soil/`, or ADR-selected contract home |
| Soil schemas | `schemas/contracts/v1/domains/soil/`, `schemas/contracts/v1/soil/`, or ADR-selected schema home |
| Soil policy rules | `policy/domains/soil/` or accepted policy homes |
| Soil source descriptors | `data/registry/sources/soil/` or accepted source registry home |
| Soil catalog records | `data/catalog/domain/soil/` or accepted catalog home |
| EvidenceBundle and proof support | `data/proofs/` |
| Receipts and run memory | `data/receipts/` |
| Release decisions, manifests, rollback, corrections | `release/` |
| Tests and fixtures | `tests/validators/domains/soil/horizon_depth/`, `tests/domains/soil/`, `fixtures/domains/soil/`, or accepted conventions |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live here when it checks declared Soil horizon-depth, component-horizon, evidence, identity, policy, and release-reference rules.
- **NEEDS VERIFICATION:** exact executable names, field names, schema homes, units, source mappings, fixture shape, policy bundles, report destinations, receipts, release integration, runtime behavior, and CI wiring.
- **DENY:** using this folder as Soil doctrine, horizon contract, schema home, policy home, source registry, catalog storage, proof storage, receipt storage, lifecycle data store, release record store, published artifact store, or public runtime surface.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/domains/soil/horizon_depth/` include checks that:

- verify a horizon has an accepted top-depth and bottom-depth representation where required;
- reject negative, inverted, impossible, malformed, or unitless depth ranges unless an accepted source/profile rule permits them;
- verify depth units are declared and normalized through accepted source mappings;
- verify horizons within the same component, pedon, or profile view have deterministic ordering;
- detect unintended overlap, duplicate depth ranges, missing ranges, or unexplained gaps according to accepted Soil rules;
- preserve Component Horizon Join integrity across MUKEY, COKEY, CHKEY, horizon identifiers, survey versions, source vintages, and EvidenceRef links where configured;
- detect when derived Soil properties, interpretations, suitability ratings, erosion-risk summaries, public map layers, or catalog entries cite horizon data whose depth integrity has not been validated;
- emit deterministic validation reports without creating receipts, proofs, release manifests, or public artifacts.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/domains/soil/horizon_depth/` | Correct home |
|---|---|
| Soil horizon meaning | `contracts/domains/soil/`, `contracts/soil/`, or accepted contract home |
| Soil horizon schema | `schemas/contracts/v1/domains/soil/`, `schemas/contracts/v1/soil/`, or accepted schema home |
| Soil source descriptors and source mappings | `data/registry/sources/soil/` or accepted source registry/source-profile home |
| Soil domain docs | `docs/domains/soil/` |
| Soil policy rules | `policy/domains/soil/` or accepted policy homes |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| EvidenceBundles, proofs, receipts, ValidationReports, ModelRunReceipts | `data/proofs/`, `data/receipts/` |
| Release manifests, decisions, rollback, corrections | `release/` |
| Generated QA reports that are not source code | `artifacts/qa/` or accepted report lane |
| Tests and fixtures | `tests/` and fixture conventions |
| Public API, UI, map, tile, export, search, graph, Focus Mode, or AI runtime code | governed application/runtime roots |

[Back to top](#top)

---

## Soil horizon-depth validator posture

This validator lane must fail closed, deny, abstain, or route to review when a candidate:

- lacks EvidenceRef, EvidenceBundle/proof reference, source descriptor, source-role, source vintage, units, horizon identity, component/profile context, validation report, policy posture, release reference, correction path, or rollback target required for its use;
- uses unknown or unsupported depth fields without an accepted source mapping;
- has negative depth, inverted bounds, malformed units, mixed units, duplicate ranges, overlapping ranges, unexplained gaps, missing top or bottom depth, or ambiguous ordering where accepted rules do not allow that posture;
- breaks configured MUKEY/COKEY/CHKEY, mapunit/component/horizon, pedon/profile, survey-version, source-vintage, or Component Horizon Join continuity;
- treats gridded, modeled, interpreted, suitability, erosion-risk, station, satellite, or survey products as the same truth class without preserving source role and evidence support;
- treats Agriculture crop/yield, Hydrology/flood, Geology/borehole, Habitat, Fauna, Flora, or Hazards claims as Soil-owned truth through a horizon-depth artifact;
- allows catalog, proof, release, map, API, graph, Focus Mode, export, or AI surfaces to depend on unvalidated horizon-depth ranges;
- points public surfaces at RAW, WORK, QUARANTINE, unresolved candidates, direct internal stores, or stale Soil horizon profiles;
- treats horizon-depth validation as EvidenceBundle creation, PolicyDecision creation, release approval, publication, or public API behavior.

The validator lane must preserve the KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `SOIL_HORIZON_DEPTH_PASS` | Configured Soil horizon-depth checks passed. |
| `SOIL_HORIZON_DEPTH_FAIL` | One or more configured horizon-depth checks failed. |
| `SOIL_HORIZON_DEPTH_MISSING` | Required top or bottom depth is absent. |
| `SOIL_HORIZON_DEPTH_UNIT_MISSING` | Required unit declaration is absent. |
| `SOIL_HORIZON_DEPTH_UNIT_INVALID` | Depth unit is unsupported or mixed without accepted conversion. |
| `SOIL_HORIZON_DEPTH_INVERTED` | Bottom depth is shallower than top depth. |
| `SOIL_HORIZON_DEPTH_NEGATIVE` | Depth value is negative where not allowed. |
| `SOIL_HORIZON_DEPTH_OVERLAP` | Horizons overlap within the same component/profile context. |
| `SOIL_HORIZON_DEPTH_GAP_UNEXPLAINED` | Gap appears where configured continuity rules require explanation. |
| `SOIL_HORIZON_ORDER_AMBIGUOUS` | Horizon sequence cannot be determined safely. |
| `SOIL_COMPONENT_HORIZON_JOIN_BROKEN` | Component-horizon linkage is missing, stale, or inconsistent. |
| `SOIL_IDENTITY_CONTINUITY_BROKEN` | Configured MUKEY/COKEY/CHKEY, mapunit/component/horizon, source-vintage, or join continuity is incomplete. |
| `SOIL_SOURCE_ROLE_COLLAPSE` | Horizon-depth package hides source-role or object-family distinction. |
| `SOIL_CROSS_DOMAIN_AUTHORITY_COLLAPSE` | Candidate absorbs another domain's truth into Soil without preserving boundaries. |
| `PUBLIC_SURFACE_LEAK_RISK` | Candidate is unsafe for public/governed output as shaped. |
| `LIFECYCLE_VIOLATION` | Candidate appears to skip required lifecycle states. |
| `REPORT_DESTINATION_INVALID` | QA report or receipt destination is outside an accepted root. |
| `ABSTAIN` | Validator cannot decide safely with available context. |
| `ERROR` | Validator could not safely complete. |

[Back to top](#top)

---

## Validation

Suggested future test surface:

```text
tests/validators/domains/soil/horizon_depth/
├── README.md
├── test_soil_horizon_depth.py
└── fixtures/
    ├── valid_ordered_horizons/
    ├── missing_top_depth/
    ├── missing_bottom_depth/
    ├── missing_units/
    ├── invalid_units/
    ├── inverted_depths/
    ├── overlapping_horizons/
    ├── unexplained_gap/
    ├── broken_component_horizon_join/
    └── cross_domain_authority_collapse/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/domains/soil/horizon_depth
```

```bash
python tools/validators/domains/soil/horizon_depth/validate_soil_horizon_depth.py --repo-root . --format json
```

> [!NOTE]
> This is a proposed interface, not proof that `validate_soil_horizon_depth.py` or the test path exists.

[Back to top](#top)

---

## Review checklist

- [ ] Validator reads declared Soil contracts, schemas, source descriptors, and policy rather than defining meaning locally.
- [ ] Horizon-depth fields, units, and source mappings are backed by schema/contract/source-profile evidence before implementation claims are made.
- [ ] Soil object families and source families remain distinct.
- [ ] MUKEY/COKEY/CHKEY and configured mapunit/component/horizon continuity remain traceable.
- [ ] Horizon-depth checks do not replace EvidenceBundle, proof, receipt, PolicyDecision, ReleaseManifest, correction, or rollback records.
- [ ] Cross-domain joins preserve Agriculture, Hydrology, Habitat, Fauna, Flora, Geology, and Hazards ownership boundaries.
- [ ] Public-bound outputs never point clients at RAW, WORK, QUARANTINE, unresolved candidates, or direct internal stores.
- [ ] Reports and receipts are written only to accepted roots.
- [ ] Validator output is not described as truth, policy, release, publication, or Directory Rules approval.
- [ ] Tests use public-safe or synthetic fixtures.
- [ ] Executable claims are backed by current repo evidence.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft README replacement for empty Soil horizon-depth validator file. |
| Next smallest safe change | Verify actual Soil horizon-depth scripts, accepted field names, unit rules, schemas, source mappings, source descriptors, fixtures, report destinations, receipts, release linkage, cross-domain join behavior, and CI/runtime wiring before promoting this lane beyond draft. |
