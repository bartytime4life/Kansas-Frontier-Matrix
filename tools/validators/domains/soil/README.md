<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-domains-soil-readme
title: tools/validators/domains/soil README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-soil-steward-plus-source-steward-plus-evidence-steward-plus-policy-steward-plus-release-steward
created: 2026-07-08
updated: 2026-07-08
policy_label: repository-facing; per-domain-validator-index; soil; SSURGO; support-type-separation; source-role-aware; release-gated; non-authoritative
owning_root: tools/
responsibility: proposed per-domain Soil validator index for catalog closure, dual-hash posture, horizon-depth integrity, lineage closure, soil-moisture observations, support-type separation, source-role discipline, MUKEY/COKEY/CHKEY continuity, EvidenceRef/EvidenceBundle closure, policy, release, correction, rollback, and public-surface denial checks while deferring Soil meaning, source registry authority, evidence records, policy decisions, proof records, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../../README.md
  - ../../../README.md
  - ../../_common/README.md
  - ../../catalog_closure/README.md
  - ../../cross-domain-joins/README.md
  - catalog_closure/README.md
  - dual_hash/README.md
  - horizon_depth/README.md
  - lineage/README.md
  - moisture/README.md
  - support_type/README.md
  - ../../../../docs/domains/soil/README.md
  - ../../../../docs/domains/soil/CANONICAL_PATHS.md
  - ../../../../docs/domains/soil/DATA_LIFECYCLE.md
  - ../../../../contracts/domains/soil/README.md
  - ../../../../contracts/domains/soil/soil_moisture_observation.md
  - ../../../../pipelines/domains/soil/ssurgo_ingest/README.md
  - ../../../../data/registry/sources/soil/README.md
  - ../../../../data/catalog/domain/soil/README.md
  - ../../../../data/proofs/soil/README.md
  - ../../../../data/receipts/
  - ../../../../release/
notes:
  - "This README replaces a greenfield stub. It does not confirm executable files."
  - "Confirmed child README lanes in this task sequence: catalog_closure, dual_hash, horizon_depth, lineage, moisture, and support_type. Executable behavior remains NEEDS VERIFICATION."
  - "Soil validators enforce declared contracts, schemas, source-role rules, support-type separation, evidence closure, policy posture, release references, correction paths, and rollback targets. They do not define Soil meaning, create SourceDescriptors, create EvidenceBundles, decide policy, approve release, or publish public outputs."
  - "Static survey, gridded derivative, station observation, satellite grid, pedon/profile, and interpretation support types must not collapse."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/domains/soil

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-soil--validators-informational)
![invariant](https://img.shields.io/badge/invariant-no--support--collapse-critical)
![authority](https://img.shields.io/badge/authority-index--only-lightgrey)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/domains/soil/` is the per-domain Soil validator index for catalog closure, dual-hash posture, horizon-depth integrity, lineage closure, moisture observations, support-type separation, source-role discipline, Soil identity continuity, evidence, policy, release, correction, rollback, and public-surface denial checks.

---

## Purpose

`tools/validators/domains/soil/` exists to organize Soil validators under the durable `tools/validators/` surface.

The durable KFM question for this index is:

> Do Soil candidates preserve Soil object-family identity, support-type separation, source-role posture, source lineage, MUKEY/COKEY/CHKEY continuity, horizon-depth integrity, soil-moisture time/QC/depth posture, EvidenceRef/EvidenceBundle support, policy posture, release linkage, correction lineage, rollback targets, and public-surface boundaries before they are used by catalog, proof, release, map, API, graph, Focus Mode, export, or AI surfaces?

The answer should be a navigable validator index and deterministic validation outputs from configured child lanes. This folder should not create Soil truth, support-type vocabulary, source truth, SourceDescriptors, EvidenceBundles, receipts, proofs, PolicyDecisions, ReleaseManifests, public map layers, API payloads, AI answers, or publication approval.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/domains/soil/README.md` | **CONFIRMED** | This README replaces the previous greenfield stub. |
| Parent per-domain validators README | **CONFIRMED stub** | `tools/validators/domains/README.md` currently says only `# Per-domain validators`; this file keeps Soil-specific boundaries explicit. |
| Child README lanes | **CONFIRMED** | `catalog_closure/`, `dual_hash/`, `horizon_depth/`, `lineage/`, `moisture/`, and `support_type/` each have README guidance. |
| Soil contract/proof/catalog evidence | **CONFIRMED in repo evidence / draft** | Current repo evidence defines Soil contract, proof, source-registry, catalog, and selected object-family surfaces as draft/release-gated and support-type-aware. |
| Executables, schemas, fixtures, policy bundles, source mappings, and CI wiring | **NEEDS VERIFICATION** | No parent runner, executable behavior, test paths, field-level schema enforcement, report destinations, policy bundle behavior, receipt emission, runtime behavior, or CI behavior are claimed as implemented here. |

[Back to top](#top)

---

## Child lanes

| Child lane | Purpose | Status |
|---|---|---|
| [`catalog_closure/`](catalog_closure/README.md) | Soil-specific catalog closure across source descriptors, EvidenceBundle/proof refs, validation reports, policy posture, release refs, correction lineage, rollback targets, lifecycle consistency, and public-surface denial. | **CONFIRMED README / executable NEEDS VERIFICATION** |
| [`dual_hash/`](dual_hash/README.md) | Soil-specific paired content/provenance hash posture using accepted canonicalization while delegating generic hashing to `tools/spec_hash/`. | **CONFIRMED README / executable NEEDS VERIFICATION** |
| [`horizon_depth/`](horizon_depth/README.md) | Horizon top/bottom depth ordering, units, non-overlap, gap/continuity posture, component-horizon join consistency, and pedon/profile depth checks. | **CONFIRMED README / executable NEEDS VERIFICATION** |
| [`lineage/`](lineage/README.md) | Source descriptor linkage, source-family separation, support-type separation, source vintage, transform lineage, MUKEY/COKEY/CHKEY continuity, and release/correction/rollback lineage. | **CONFIRMED README / executable NEEDS VERIFICATION** |
| [`moisture/`](moisture/README.md) | SoilMoistureObservation unit, depth, QC, cadence, stale-state, source-role, support-type, evidence, policy, release, correction, rollback, and public-surface posture. | **CONFIRMED README / executable NEEDS VERIFICATION** |
| [`support_type/`](support_type/README.md) | Static survey, gridded derivative, station observation, satellite grid, pedon/profile, interpretation, and public-safe derivative anti-collapse checks. | **CONFIRMED README / executable NEEDS VERIFICATION** |

Possible future child lanes remain **PROPOSED** until created and verified:

- `schema_contract/` for Soil schema/contract pairing checks;
- `mukey_cokey_chkey/` for dedicated mapunit/component/horizon identity continuity;
- `property_units/` for SoilProperty unit/method/depth support checks;
- `public_surface/` for map/API/export/AI release-envelope checks;
- `cross_domain/` for Soil × Agriculture, Soil × Hydrology, Soil × Geology, Soil × Habitat/Fauna/Flora join posture when not handled by shared cross-domain validator lanes.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Per-domain Soil validator index | `tools/validators/domains/soil/` |
| Soil child validator lanes | `tools/validators/domains/soil/*/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Shared catalog closure | `tools/validators/catalog_closure/` |
| Cross-domain invariant validators | `tools/validators/cross-domain-joins/` |
| Generic spec hash helper | `tools/spec_hash/` |
| Soil domain meaning and doctrine | `docs/domains/soil/`, `contracts/domains/soil/`, `contracts/soil/`, or ADR-selected contract home |
| Soil schemas | `schemas/contracts/v1/domains/soil/`, `schemas/contracts/v1/soil/`, or ADR-selected schema home |
| Soil policy rules | `policy/domains/soil/` or accepted policy homes |
| Soil source descriptors and source registry | `data/registry/sources/soil/` or accepted source registry home |
| Soil catalog records | `data/catalog/domain/soil/` or accepted catalog home |
| Soil EvidenceBundle/proof support | `data/proofs/soil/`, `data/proofs/` |
| Receipts and run memory | `data/receipts/` |
| Release decisions, manifests, rollback, corrections | `release/` |
| Tests and fixtures | `tests/validators/domains/soil/`, `tests/domains/soil/`, `fixtures/domains/soil/`, or accepted conventions |

Safe interpretation:

- **CONFIRMED:** this README exists and the listed child README lanes exist.
- **PROPOSED:** validator code may live in this folder tree when it checks declared Soil validation invariants and delegates meaning, source roles, policy, evidence, proof, receipt, and release authority to owning roots.
- **NEEDS VERIFICATION:** parent runner name, child executable names, exact schemas, source mappings, source descriptor shapes, fixture shape, policy bundles, report destinations, receipts, release integration, runtime behavior, and CI wiring.
- **DENY:** using this folder as Soil doctrine, support-type vocabulary authority, source registry, source payload storage, contract home, schema home, policy home, catalog storage, proof storage, receipt storage, lifecycle data store, release record store, published artifact store, public runtime surface, operational advice surface, or agronomic/engineering/legal/hazard recommendation authority.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/domains/soil/` include:

- this parent/index README;
- narrow Soil validator child lanes;
- optional parent runner code that delegates to child validators without redefining their rules;
- validators that check Soil object-family boundaries, support-type separation, source-role posture, lineage, hash posture, horizon-depth integrity, moisture unit/depth/QC/cadence posture, catalog closure, evidence closure, policy state, release references, correction lineage, and rollback support;
- validators that check public-bound Soil artifacts do not point to RAW, WORK, QUARANTINE, unresolved candidates, direct internal stores, stale readings, private operational sensors, or support-type-collapsed candidates;
- validators that check cross-domain joins preserve Agriculture, Hydrology, Atmosphere, Habitat, Fauna, Flora, Geology, and Hazards ownership boundaries;
- synthetic fixture references and test-surface guidance;
- docs or reports that explain validator scope without becoming authoritative Soil doctrine.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/domains/soil/` | Correct home |
|---|---|
| Soil domain meaning and contract prose | `docs/domains/soil/`, `contracts/domains/soil/`, `contracts/soil/`, or accepted contract/doctrine home |
| Soil schemas or enums | `schemas/contracts/v1/domains/soil/`, `schemas/contracts/v1/soil/`, or accepted schema home |
| Soil source descriptors and source mappings | `data/registry/sources/soil/` or accepted source registry/source-profile home |
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

## Soil validator posture

Soil validators must fail closed, deny, abstain, or route to review when a candidate:

- lacks required source descriptor, source role, support type, source vintage, lineage, units/method, EvidenceRef, EvidenceBundle/proof reference, validation report, policy posture, release reference, correction path, or rollback target;
- collapses static survey, gridded derivative, station observation, satellite grid, pedon/profile, interpretation, public-safe derivative, candidate, or private operational support classes;
- collapses SoilMapUnit, SoilComponent, Horizon, SoilProperty, HydrologicSoilGroup, SoilMoistureObservation, Pedon, SoilProfileView, ErosionRisk, SuitabilityRating, SoilTimeCaveat, or ComponentHorizonJoin roles;
- breaks configured MUKEY/COKEY/CHKEY, mapunit/component/horizon, source-vintage, survey-area, component-horizon, or derived-grid continuity;
- treats station readings as countywide truth, satellite grids as station readings, survey data as live field condition, pedon/profile data as map-unit truth, or interpretations as legal/hazard/crop/economic/engineering/operational advice;
- treats Agriculture crop/yield, Hydrology/flood/groundwater, Atmosphere precipitation, Habitat/Flora/Fauna ecology, Geology/boreholes/stratigraphy, or Hazards claims as Soil-owned truth;
- allows catalog, proof, release, map, API, graph, Focus Mode, export, or AI surfaces to depend on unvalidated, unclosed, or support-type-collapsed Soil records;
- points public surfaces at RAW, WORK, QUARANTINE, unresolved candidates, direct internal stores, stale readings, private operational sensors, stale source descriptors, or incomplete proof closure;
- treats validator output as SourceDescriptor creation, EvidenceBundle creation, PolicyDecision creation, release approval, publication, operational advice, or public API behavior.

The validator tree must preserve the KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

[Back to top](#top)

---

## Standard parent outcomes

| Outcome | Meaning |
|---|---|
| `SOIL_DOMAIN_VALIDATORS_PASS` | Configured Soil validators passed. |
| `SOIL_DOMAIN_VALIDATORS_FAIL` | One or more configured Soil validators failed. |
| `CHILD_VALIDATOR_MISSING` | Expected Soil child validator lane or runner is absent. |
| `CHILD_VALIDATOR_FAILED` | Child validator reported one or more findings. |
| `SOIL_SOURCE_DESCRIPTOR_MISSING` | Required Soil source descriptor or source registry pointer is absent. |
| `SOIL_SOURCE_ROLE_MISSING` | Required source-role posture is absent. |
| `SOIL_SUPPORT_TYPE_MISSING` | Required support-type label is absent. |
| `SOIL_SUPPORT_TYPE_COLLAPSE` | Soil support classes are conflated. |
| `SOIL_IDENTITY_CONTINUITY_BROKEN` | Configured MUKEY/COKEY/CHKEY, mapunit/component/horizon, source-vintage, or join continuity is incomplete. |
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
tests/validators/domains/soil/
├── README.md
├── test_soil_domain_validator_parent.py
├── catalog_closure/
├── dual_hash/
├── horizon_depth/
├── lineage/
├── moisture/
├── support_type/
└── fixtures/
    ├── valid_soil_validation_bundle/
    ├── missing_source_descriptor/
    ├── support_type_collapse/
    ├── broken_mukey_cokey_chkey_continuity/
    ├── missing_evidence_ref/
    ├── policy_or_release_gap/
    ├── cross_domain_authority_collapse/
    └── public_surface_leak_risk/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/domains/soil
```

```bash
python tools/validators/domains/soil/run_soil_domain_validators.py --repo-root . --format json
```

> [!NOTE]
> This is a proposed interface, not proof that `run_soil_domain_validators.py` or the test path exists.

[Back to top](#top)

---

## Review checklist

- [ ] Parent runner delegates to child validators instead of redefining their rules.
- [ ] Validators read declared Soil contracts, schemas, source descriptors, source-role rules, and policy rather than defining meaning locally.
- [ ] Static survey, gridded derivative, station observation, satellite grid, pedon/profile, interpretation, and public-safe derivative support types remain distinct.
- [ ] MUKEY/COKEY/CHKEY and configured mapunit/component/horizon continuity remain traceable.
- [ ] Soil validation does not replace SourceDescriptor, EvidenceBundle, proof, receipt, PolicyDecision, ReleaseManifest, correction, or rollback records.
- [ ] Cross-domain joins preserve Agriculture, Hydrology, Atmosphere, Habitat, Fauna, Flora, Geology, and Hazards ownership boundaries.
- [ ] Public-bound outputs never point clients at RAW, WORK, QUARANTINE, unresolved candidates, direct internal stores, private operational sensors, stale readings, source-role-collapsed candidates, or incomplete proof closure.
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
| Review state | Draft README replacement for greenfield Soil validator parent stub. |
| Next smallest safe change | Verify actual Soil parent runner, child scripts, accepted field names, support-type vocabulary, schemas, source mappings, source descriptors, fixtures, report destinations, receipts, release linkage, cross-domain join behavior, and CI/runtime wiring before promoting this lane beyond draft. |
