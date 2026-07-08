<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-domains-soil-catalog-closure-readme
title: tools/validators/domains/soil/catalog_closure README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-soil-steward-plus-catalog-steward-plus-evidence-steward-plus-release-steward-plus-policy-steward
created: 2026-07-07
updated: 2026-07-07
policy_label: repository-facing; per-domain-validator; soil; catalog-closure; proof-side-readiness; SSURGO; MUKEY; release-gated; non-authoritative
owning_root: tools/
responsibility: proposed Soil-specific catalog-closure validator lane for Soil catalog packages, SSURGO/gSSURGO/gNATSGO/source-family closure, MUKEY/COKEY/CHKEY identity continuity, Soil-owned object-family coverage, source descriptors, EvidenceBundle/proof references, validation reports, policy posture, release references, correction lineage, rollback targets, lifecycle-state consistency, and public-surface denial checks while deferring shared catalog-closure rules to tools/validators/catalog_closure and Soil meaning, policy decisions, proof records, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../../README.md
  - ../../../README.md
  - ../../../_common/README.md
  - ../../../catalog/README.md
  - ../../../catalog_closure/README.md
  - ../../../cross-domain-joins/README.md
  - ../../../../../docs/domains/soil/README.md
  - ../../../../../docs/domains/soil/CANONICAL_PATHS.md
  - ../../../../../docs/domains/soil/DATA_LIFECYCLE.md
  - ../../../../../docs/runbooks/soil/ROLLBACK_RUNBOOK.md
  - ../../../../../data/catalog/domain/soil/
  - ../../../../../data/registry/sources/soil/
  - ../../../../../data/proofs/
  - ../../../../../data/receipts/
  - ../../../../../release/
  - ../../../../../contracts/data/catalog_matrix.md
  - ../../../../../contracts/data/validation_report.md
  - ../../../../../schemas/contracts/v1/data/catalog_matrix.schema.json
  - ../../../../../policy/domains/soil/
notes:
  - "This README replaces an empty file. It does not confirm executable files."
  - "The broad catalog-closure validator lane remains tools/validators/catalog_closure/. This child lane is only for Soil-specific catalog-closure checks and must not create a parallel catalog authority."
  - "Soil owns static survey, gridded derivative, station soil-moisture, satellite-grid, pedon, interpretation, suitability, and erosion-context surfaces. Soil does not own crop/yield, hydrology/flood, or geology/borehole truth."
  - "Catalog closure is proof-side/readiness validation. It is not catalog storage, proof storage, receipt storage, release approval, publication, or public API behavior."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/domains/soil/catalog_closure

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-soil--catalog--closure-informational)
![boundary](https://img.shields.io/badge/boundary-proof--side--readiness-blueviolet)
![authority](https://img.shields.io/badge/authority-validator--only-lightgrey)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/domains/soil/catalog_closure/` is the proposed Soil-specific catalog-closure validator lane for checking whether Soil catalog candidates have enough source, evidence, identity, validation, policy, release, correction, rollback, and lifecycle support to proceed to the next governed state.

---

## Purpose

`tools/validators/domains/soil/catalog_closure/` exists for Soil-specific catalog-closure checks that are narrower than the shared `tools/validators/catalog_closure/` lane.

The durable KFM question for this lane is:

> Does a Soil catalog candidate preserve Soil object-family coverage, SSURGO/gSSURGO/gNATSGO/source-family lineage, MUKEY/COKEY/CHKEY identity continuity, source-role posture, EvidenceBundle/proof support, validation reports, policy posture, release references, correction lineage, rollback targets, and lifecycle-state consistency before it is considered for governed release or downstream public-safe use?

The answer should be a deterministic validation result. This folder should not create Soil truth, source truth, catalog records, EvidenceBundles, CatalogMatrix instances, PolicyDecisions, ReleaseManifests, public map layers, API payloads, AI answers, or publication approval.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/domains/soil/catalog_closure/README.md` | **CONFIRMED** | This README replaces the previous empty file. |
| Parent `tools/validators/domains/soil/README.md` | **CONFIRMED stub** | Parent file currently says only `# validators :: soil`; this README keeps its own boundary explicit. |
| Shared catalog-closure lane | **CONFIRMED in repo evidence / draft** | `tools/validators/catalog_closure/README.md` defines broad catalog-closure readiness checks and separates catalog closure from catalog validation, proof storage, receipt storage, release approval, and publication. |
| Soil top README | **CONFIRMED placeholder** | `docs/domains/soil/README.md` currently contains only a greenfield placeholder. |
| Soil lifecycle and canonical-path docs | **CONFIRMED in repo evidence / draft** | `docs/domains/soil/DATA_LIFECYCLE.md` and `CANONICAL_PATHS.md` provide the current inspected Soil lane evidence for lifecycle, object families, source families, placement, and verification posture. |
| Executables, schemas, fixtures, policy bundles, source registry behavior, and CI wiring | **NEEDS VERIFICATION** | No script names, test paths, schema maturity, policy bundles, receipts, runtime behavior, or CI behavior are claimed as implemented here. |

[Back to top](#top)

---

## Relationship to the shared catalog-closure validator

Use this split:

| Concern | Preferred lane |
|---|---|
| Generic CatalogMatrix-style readiness, source/evidence/policy/release/correction/rollback completeness | `tools/validators/catalog_closure/` |
| Catalog record/discovery/interchange validation | `tools/validators/catalog/` |
| Soil-specific catalog closure for Soil object families, SSURGO identity keys, Soil source-family closure, and Soil public-safe release posture | `tools/validators/domains/soil/catalog_closure/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Cross-domain Soil joins, such as Soil × Agriculture or Soil × Hydrology closure checks | `tools/validators/cross-domain-joins/` or an accepted cross-lane validator lane |

This README does not move, replace, or override the broad catalog-closure validator. It adds a narrow Soil child lane so Soil closure checks can be inspected without becoming a new catalog, proof, release, or domain authority.

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Soil-specific catalog-closure validator entrypoints | `tools/validators/domains/soil/catalog_closure/` |
| Broad catalog-closure validator entrypoints | `tools/validators/catalog_closure/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Soil validator parent index | `tools/validators/domains/soil/` |
| Soil domain meaning and doctrine | `docs/domains/soil/`, `contracts/domains/soil/`, `contracts/soil/`, or ADR-selected contract home |
| Soil schemas | `schemas/contracts/v1/domains/soil/`, `schemas/contracts/v1/soil/`, or ADR-selected schema home |
| Soil policy rules | `policy/domains/soil/` or accepted policy homes |
| Soil source descriptors | `data/registry/sources/soil/` or accepted source registry home |
| Soil catalog records | `data/catalog/domain/soil/` or accepted catalog home |
| CatalogMatrix meaning | `contracts/data/catalog_matrix.md` |
| EvidenceBundle and proof support | `data/proofs/` |
| Receipts and run memory | `data/receipts/` |
| Release decisions, manifests, rollback, corrections | `release/` |
| Published public-safe Soil artifacts | `data/published/layers/soil/` or accepted published-artifact home |
| Tests and fixtures | `tests/validators/domains/soil/catalog_closure/`, `tests/domains/soil/`, `fixtures/domains/soil/`, or accepted conventions |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live here when it checks declared Soil catalog-closure, evidence, identity, policy, and release-reference rules.
- **NEEDS VERIFICATION:** exact executable names, schema homes, source registry shape, fixture shape, policy bundles, report destinations, receipts, release integration, runtime behavior, and CI wiring.
- **DENY:** using this folder as catalog storage, proof storage, receipt storage, source registry, lifecycle data store, release record store, published artifact store, contract home, schema home, policy home, or public runtime surface.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/domains/soil/catalog_closure/` include checks that:

- validate Soil catalog-closure packages against shared CatalogMatrix-style closure expectations;
- require every Soil catalog entry to resolve to a Soil source descriptor and admissible EvidenceRef/EvidenceBundle or proof reference;
- require validation reports for Soil schema, source-role, identity, lifecycle, policy, sensitivity, and public-safe geometry checks;
- verify Soil object-family coverage for `SoilMapUnit`, `SoilComponent`, `Horizon`, `SoilProperty`, `HydrologicSoilGroup`, `SoilMoistureObservation`, `ErosionRisk`, `SuitabilityRating`, `Pedon` / `SoilProfileView`, `ComponentHorizonJoin`, and `SoilTimeCaveat` where configured;
- preserve SSURGO/gSSURGO/gNATSGO/SDA source-family distinctions and any configured MUKEY/COKEY/CHKEY continuity checks;
- confirm Soil catalog closure does not treat Agriculture crop/yield, Hydrology/flood, or Geology/borehole claims as Soil-owned truth;
- confirm public-bound Soil entries carry required policy posture, review state, release reference, correction lineage, and rollback target;
- detect drift between Soil catalog records, triplets, proof bundles, source registry entries, validation reports, and release references;
- confirm catalog closure does not point public surfaces at RAW, WORK, QUARANTINE, unresolved candidates, or direct internal stores.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/domains/soil/catalog_closure/` | Correct home |
|---|---|
| Broad catalog-closure semantics | `tools/validators/catalog_closure/` and `contracts/data/catalog_matrix.md` |
| Catalog-record storage | `data/catalog/` |
| Soil source descriptors | `data/registry/sources/soil/` |
| Soil domain docs | `docs/domains/soil/` |
| Soil contracts | `contracts/domains/soil/`, `contracts/soil/`, or ADR-selected home |
| Soil schemas | `schemas/contracts/v1/domains/soil/`, `schemas/contracts/v1/soil/`, or ADR-selected home |
| Soil policy rules | `policy/domains/soil/` or accepted policy homes |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| EvidenceBundles, proofs, receipts, ValidationReports, ModelRunReceipts | `data/proofs/`, `data/receipts/` |
| Release manifests, decisions, rollback, corrections | `release/` |
| Generated QA reports that are not source code | `artifacts/qa/` or accepted report lane |
| Tests and fixtures | `tests/` and fixture conventions |
| Public API, UI, map, tile, export, search, graph, Focus Mode, or AI runtime code | governed application/runtime roots |

[Back to top](#top)

---

## Soil catalog-closure validator posture

This validator lane must fail closed, deny, abstain, or route to review when a candidate:

- lacks a Soil source descriptor, EvidenceRef, EvidenceBundle/proof reference, validation report, policy posture, review state, release reference, correction path, or rollback target required for its use;
- collapses SSURGO, SDA, gSSURGO, gNATSGO, Mesonet, SCAN, USCRN, SMAP, or other configured source-family roles;
- breaks configured Soil identity continuity across MUKEY, COKEY, CHKEY, component-horizon joins, mapunit/component/horizon references, survey versions, source vintages, or derived grids;
- treats modeled, gridded, interpreted, suitability, erosion-risk, station, satellite, or survey products as the same truth class;
- treats Agriculture, Hydrology, Habitat, Fauna, Flora, Geology, or Hazards claims as Soil-owned truth in a Soil catalog closure package;
- promotes farm-/owner-specific or operational sensor detail without required rights, sensitivity, policy, review, and release support;
- points public surfaces at RAW, WORK, QUARANTINE, unresolved candidates, direct internal stores, incomplete CatalogMatrix rows, or unclosed proof packages;
- treats catalog closure as EvidenceBundle creation, PolicyDecision creation, release approval, publication, or public API behavior.

The validator lane must preserve the KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `SOIL_CATALOG_CLOSURE_PASS` | Configured Soil catalog-closure checks passed. |
| `SOIL_CATALOG_CLOSURE_FAIL` | One or more configured checks failed. |
| `SOIL_SOURCE_DESCRIPTOR_MISSING` | Required Soil source descriptor is absent or unresolved. |
| `SOIL_EVIDENCE_REF_MISSING` | Required EvidenceRef, EvidenceBundle, or proof reference is absent. |
| `SOIL_VALIDATION_REPORT_MISSING` | Required validation report is absent. |
| `SOIL_POLICY_POSTURE_MISSING` | Required policy or sensitivity posture is absent. |
| `SOIL_RELEASE_REFERENCE_MISSING` | Required ReleaseManifest, correction path, or rollback target is absent. |
| `SOIL_IDENTITY_CONTINUITY_BROKEN` | Configured MUKEY/COKEY/CHKEY, mapunit/component/horizon, source-vintage, or join continuity is incomplete. |
| `SOIL_SOURCE_ROLE_COLLAPSE` | Survey, gridded, modeled, station, satellite, interpreted, suitability, or erosion-risk roles are conflated. |
| `SOIL_CROSS_DOMAIN_AUTHORITY_COLLAPSE` | Candidate absorbs another domain's truth into Soil without preserving boundaries. |
| `SOIL_PUBLIC_SURFACE_LEAK_RISK` | Candidate is unsafe for public/governed output as shaped. |
| `CATALOG_PROOF_RELEASE_COLLAPSE` | Candidate treats catalog closure as proof creation, release approval, or publication. |
| `LIFECYCLE_VIOLATION` | Candidate appears to skip required lifecycle states. |
| `REPORT_DESTINATION_INVALID` | QA report or receipt destination is outside an accepted root. |
| `IGNORED_WITH_REASON` | Finding was ignored under an explicit, reviewable rule. |
| `IGNORE_RULE_EXPIRED` | Ignore rule is stale and must be reviewed. |
| `ABSTAIN` | Validator cannot decide safely with available context. |
| `ERROR` | Validator could not safely complete. |

[Back to top](#top)

---

## Validation

Suggested future test surface:

```text
tests/validators/domains/soil/catalog_closure/
├── README.md
├── test_soil_catalog_closure.py
└── fixtures/
    ├── valid_soil_catalog_closure_bundle/
    ├── missing_source_descriptor/
    ├── missing_evidence_ref/
    ├── missing_validation_report/
    ├── missing_policy_posture/
    ├── missing_release_reference/
    ├── broken_mukey_cokey_chkey_continuity/
    ├── source_role_collapse/
    ├── cross_domain_authority_collapse/
    └── lifecycle_violation/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/domains/soil/catalog_closure
```

```bash
python tools/validators/domains/soil/catalog_closure/validate_soil_catalog_closure.py --repo-root . --format json
```

> [!NOTE]
> This is a proposed interface, not proof that `validate_soil_catalog_closure.py` or the test path exists.

[Back to top](#top)

---

## Review checklist

- [ ] Validator reuses shared catalog-closure concepts instead of redefining them locally.
- [ ] Validator reads declared Soil contracts, schemas, source descriptors, and policy rather than defining meaning locally.
- [ ] Soil object families and source families remain distinct.
- [ ] SSURGO/SDA/gSSURGO/gNATSGO and configured Soil identity keys remain traceable.
- [ ] Catalog closure does not replace EvidenceBundle, proof, PolicyDecision, ReleaseManifest, correction, or rollback records.
- [ ] Cross-domain joins preserve Agriculture, Hydrology, Habitat, Fauna, Flora, Geology, and Hazards ownership boundaries.
- [ ] Public-bound catalog closure never points clients at RAW, WORK, QUARANTINE, unresolved candidates, or direct internal stores.
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
| Review state | Draft README replacement for empty Soil catalog-closure validator file. |
| Next smallest safe change | Verify actual Soil catalog-closure scripts, accepted profiles, schemas, source descriptors, CatalogMatrix fields, policy bundles, fixtures, report destinations, receipts, release linkage, cross-domain join behavior, and CI/runtime wiring before promoting this lane beyond draft. |
