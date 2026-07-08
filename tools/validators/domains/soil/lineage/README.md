<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-domains-soil-lineage-readme
title: tools/validators/domains/soil/lineage README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner-plus-soil-steward-plus-source-steward-plus-evidence-steward-plus-policy-steward-plus-release-steward
created: 2026-07-07
updated: 2026-07-07
policy_label: repository-facing; per-domain-validator; soil; lineage; source-role; provenance; SSURGO; MUKEY; COKEY; CHKEY; release-gated; non-authoritative
owning_root: tools/
responsibility: proposed Soil-specific lineage validator lane for checking source descriptor linkage, source family separation, support-type separation, source vintage, retrieval/run references, transform identifiers, MUKEY/COKEY/CHKEY continuity, map-unit/component/horizon lineage, component-horizon join posture, EvidenceRef/EvidenceBundle references, catalog/proof/release/correction/rollback linkage, and public-surface denial checks while deferring Soil meaning, source registry authority, evidence records, policy decisions, proof records, and release authority to their owning roots
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../../README.md
  - ../../../README.md
  - ../../../_common/README.md
  - ../catalog_closure/README.md
  - ../dual_hash/README.md
  - ../horizon_depth/README.md
  - ../../../catalog_closure/README.md
  - ../../../cross-domain-joins/README.md
  - ../../../../../docs/domains/soil/README.md
  - ../../../../../docs/domains/soil/CANONICAL_PATHS.md
  - ../../../../../docs/domains/soil/DATA_LIFECYCLE.md
  - ../../../../../docs/runbooks/soil/NO_NETWORK_TEST_RUNBOOK.md
  - ../../../../../docs/runbooks/soil/PROMOTION_RUNBOOK.md
  - ../../../../../docs/runbooks/soil/ROLLBACK_RUNBOOK.md
  - ../../../../../pipelines/domains/soil/ssurgo_ingest/README.md
  - ../../../../../data/registry/sources/soil/README.md
  - ../../../../../data/catalog/domain/soil/README.md
  - ../../../../../data/proofs/
  - ../../../../../data/receipts/
  - ../../../../../release/
notes:
  - "This README replaces an empty file. It does not confirm executable files."
  - "Soil source-registry records are admission and authority-control records. They do not store source payloads, prove soil claims, define contracts, enforce schemas, hold policy, close catalogs, or publish artifacts."
  - "SSURGO ingest evidence says MUKEY/COKEY/CHKEY lineage, map-unit/component/horizon hierarchy, source vintage, support type, geometry scope, attribute provenance, and receipt lineage must be preserved."
  - "This validator lane checks lineage posture only. It must not define Soil meaning, create SourceDescriptors, create EvidenceBundles, approve release, or publish public outputs."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/validators/domains/soil/lineage

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-soil--lineage-informational)
![boundary](https://img.shields.io/badge/boundary-validator--only-lightgrey)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **One-line purpose.** `tools/validators/domains/soil/lineage/` is the proposed Soil-specific validator lane for checking source/provenance lineage across Soil source descriptors, ingest candidates, catalog entries, proof references, receipts, release candidates, corrections, rollback targets, and public-safe derivatives.

---

## Purpose

`tools/validators/domains/soil/lineage/` exists for Soil lineage checks under the durable `tools/validators/` surface.

The durable KFM question for this lane is:

> Do Soil candidates preserve source identity, source family, source role, support type, source vintage, retrieval/run references, transform identifiers, MUKEY/COKEY/CHKEY continuity, map-unit/component/horizon lineage, EvidenceRef/EvidenceBundle support, catalog/proof/release linkage, correction lineage, rollback targets, and public-surface boundaries before they are used by catalog, proof, release, map, API, graph, Focus Mode, export, or AI surfaces?

The answer should be a deterministic validation result. This folder should not create Soil truth, source truth, SourceDescriptors, EvidenceBundles, receipts, proofs, PolicyDecisions, ReleaseManifests, public map layers, API payloads, AI answers, or publication approval.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/validators/domains/soil/lineage/README.md` | **CONFIRMED** | This README replaces the previous empty file. |
| Parent `tools/validators/domains/soil/README.md` | **CONFIRMED stub** | Parent file currently says only `# validators :: soil`; this README keeps its own boundary explicit. |
| Soil source-registry evidence | **CONFIRMED in repo evidence / draft** | `data/registry/sources/soil/README.md` defines Soil source registry as admission and authority-control, not source payload storage, claim proof, contract, schema, policy, catalog closure, or publication. |
| Soil catalog evidence | **CONFIRMED in repo evidence / draft** | `data/catalog/domain/soil/README.md` requires support-type separation and SSURGO/gSSURGO lineage for public-bound catalog posture. |
| SSURGO ingest evidence | **CONFIRMED in repo evidence / draft** | `pipelines/domains/soil/ssurgo_ingest/README.md` says SSURGO ingest must preserve MUKEY/COKEY/CHKEY lineage, map-unit/component/horizon hierarchy, source vintage, support type, geometry scope, attribute provenance, and receipt lineage. |
| Soil lifecycle and canonical-path docs | **CONFIRMED in repo evidence / draft** | `docs/domains/soil/DATA_LIFECYCLE.md` and `CANONICAL_PATHS.md` provide current inspected Soil lane evidence for lifecycle, object families, source families, placement, and verification posture. |
| Lineage schema, exact fields, source mappings, fixtures, and CI wiring | **PROPOSED / NEEDS VERIFICATION** | This README does not claim that a lineage schema, executable, fixture set, source mapping, runtime integration, or CI check exists. |

[Back to top](#top)

---

## Proposed validation focus

Until a Soil contract/schema/source profile confirms exact field names, this README treats the following as proposed validation concepts, not implemented fields:

| Concept | Proposed meaning | Notes |
|---|---|---|
| Source identity | Stable pointer to the admitted Soil source descriptor or source-family record. | Must not be replaced by a human-readable source label alone. |
| Source role | The role a source plays for the candidate claim, such as authority, observation, context, model, derivative, or restricted support. | Exact allowed vocabulary must come from accepted source-role policy/schema. |
| Support type | Static survey, gridded derivative, station observation, satellite grid, pedon/profile, interpretation, suitability, erosion-risk, or accepted equivalent. | Support types are not interchangeable. |
| Source vintage | Source date/version/survey vintage/retrieval window/effective time needed to reproduce the candidate. | Should remain distinct from release and correction time. |
| Transform lineage | Transform identifier, parameters/profile, code/version reference, run receipt, and input/output references. | Validator checks pointers; it does not create receipts. |
| Soil identity lineage | MUKEY, COKEY, CHKEY, mapunit/component/horizon references, survey area, source vintage, and join posture where configured. | Exact key requirements depend on source family and object family. |
| Evidence lineage | EvidenceRef/EvidenceBundle/proof reference closure. | A lineage pointer is not proof closure by itself. |
| Release lineage | ReleaseManifest, correction, rollback, supersession, or withdrawal references where public-bound. | Release remains outside this folder. |

[Back to top](#top)

---

## Authority boundary

| Responsibility | Home |
|---|---|
| Soil-specific lineage validator entrypoints | `tools/validators/domains/soil/lineage/` |
| Shared validator plumbing | `tools/validators/_common/` |
| Soil validator parent index | `tools/validators/domains/soil/` |
| Soil catalog closure validator | `tools/validators/domains/soil/catalog_closure/` |
| Soil dual-hash validator | `tools/validators/domains/soil/dual_hash/` |
| Soil horizon-depth validator | `tools/validators/domains/soil/horizon_depth/` |
| Soil domain meaning and doctrine | `docs/domains/soil/`, `contracts/domains/soil/`, `contracts/soil/`, or ADR-selected contract home |
| Soil schemas | `schemas/contracts/v1/domains/soil/`, `schemas/contracts/v1/soil/`, or ADR-selected schema home |
| Soil policy rules | `policy/domains/soil/` or accepted policy homes |
| Soil source descriptors and source registry | `data/registry/sources/soil/` or accepted source registry home |
| Soil catalog records | `data/catalog/domain/soil/` or accepted catalog home |
| EvidenceBundle and proof support | `data/proofs/` |
| Receipts and run memory | `data/receipts/` |
| Release decisions, manifests, rollback, corrections | `release/` |
| Tests and fixtures | `tests/validators/domains/soil/lineage/`, `tests/domains/soil/`, `fixtures/domains/soil/`, or accepted conventions |

Safe interpretation:

- **CONFIRMED:** this README exists.
- **PROPOSED:** validator code may live here when it checks declared Soil lineage, evidence, identity, policy, and release-reference rules.
- **NEEDS VERIFICATION:** exact executable names, field names, schema homes, source mappings, fixture shape, policy bundles, report destinations, receipts, release integration, runtime behavior, and CI wiring.
- **DENY:** using this folder as Soil doctrine, source registry, source descriptor store, source payload storage, contract home, schema home, policy home, catalog storage, proof storage, receipt storage, lifecycle data store, release record store, published artifact store, or public runtime surface.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/validators/domains/soil/lineage/` include checks that:

- verify every consequential Soil candidate points to an admitted Soil source descriptor or source-registry record;
- verify source family, source role, support type, source vintage, retrieval/run reference, transform identifier, and source head remain visible where required;
- verify SSURGO/gSSURGO/gNATSGO/SDA/Mesonet/SCAN/USCRN/SMAP and other configured source families are not collapsed into one authority or support type;
- verify MUKEY/COKEY/CHKEY, mapunit/component/horizon, component-horizon, survey-area, source-vintage, and derived-grid lineage where configured;
- detect when a derived Soil record, catalog entry, proof reference, release candidate, map layer, or public-safe derivative lost its upstream lineage;
- detect when source descriptors, transforms, run receipts, or EvidenceRefs changed without dependent Soil candidates being refreshed or reviewed;
- require fail-closed findings for missing, stale, ambiguous, circular, cross-domain-collapsed, or unsupported lineage;
- emit deterministic validation reports without creating receipts, proofs, release manifests, or public artifacts.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/validators/domains/soil/lineage/` | Correct home |
|---|---|
| Soil source descriptors or source registry records | `data/registry/sources/soil/` or accepted source registry home |
| Soil source payloads | `data/raw/soil/` or accepted RAW lifecycle home |
| Soil domain docs | `docs/domains/soil/` |
| Soil contracts | `contracts/domains/soil/`, `contracts/soil/`, or accepted contract home |
| Soil schemas | `schemas/contracts/v1/domains/soil/`, `schemas/contracts/v1/soil/`, or accepted schema home |
| Soil policy rules | `policy/domains/soil/` or accepted policy homes |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | dedicated `data/` lifecycle roots |
| EvidenceBundles, proofs, receipts, ValidationReports, ModelRunReceipts | `data/proofs/`, `data/receipts/` |
| Release manifests, decisions, rollback, corrections | `release/` |
| Pipeline execution logic | `pipelines/domains/soil/` and `pipeline_specs/soil/` |
| Generated QA reports that are not source code | `artifacts/qa/` or accepted report lane |
| Tests and fixtures | `tests/` and fixture conventions |
| Public API, UI, map, tile, export, search, graph, Focus Mode, or AI runtime code | governed application/runtime roots |

[Back to top](#top)

---

## Soil lineage validator posture

This validator lane must fail closed, deny, abstain, or route to review when a candidate:

- lacks source descriptor, source role, support type, source vintage, retrieval/run reference, transform identifier, EvidenceRef, EvidenceBundle/proof reference, validation report, policy posture, release reference, correction path, or rollback target required for its use;
- collapses static survey, gridded derivative, station observation, satellite grid, pedon/profile, interpretation, suitability, erosion-risk, or other configured support types;
- collapses SSURGO, SDA, gSSURGO, gNATSGO, Kansas Mesonet, SCAN, USCRN, SMAP, or other configured source-family roles;
- breaks configured MUKEY/COKEY/CHKEY, mapunit/component/horizon, component-horizon, source-vintage, survey-area, or derived-grid continuity;
- treats Agriculture crop/yield, Hydrology/flood, Geology/borehole, Habitat, Fauna, Flora, or Hazards claims as Soil-owned truth through a lineage artifact;
- points public surfaces at RAW, WORK, QUARANTINE, unresolved candidates, direct internal stores, stale source descriptors, stale transforms, or incomplete lineage closure;
- treats lineage validation as SourceDescriptor creation, EvidenceBundle creation, PolicyDecision creation, release approval, publication, or public API behavior.

The validator lane must preserve the KFM lifecycle invariant:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

[Back to top](#top)

---

## Standard outcomes

| Outcome | Meaning |
|---|---|
| `SOIL_LINEAGE_PASS` | Configured Soil lineage checks passed. |
| `SOIL_LINEAGE_FAIL` | One or more configured lineage checks failed. |
| `SOIL_SOURCE_DESCRIPTOR_MISSING` | Required Soil source descriptor or source registry pointer is absent. |
| `SOIL_SOURCE_ROLE_MISSING` | Required source-role posture is absent. |
| `SOIL_SUPPORT_TYPE_MISSING` | Required support-type label is absent. |
| `SOIL_SUPPORT_TYPE_COLLAPSE` | Static survey, gridded, station, satellite, pedon/profile, or interpretation support types are conflated. |
| `SOIL_SOURCE_FAMILY_COLLAPSE` | Source-family roles are conflated or unsupported. |
| `SOIL_SOURCE_VINTAGE_MISSING` | Required source vintage, retrieval window, source version, or effective/valid time is absent. |
| `SOIL_TRANSFORM_LINEAGE_MISSING` | Required transform identifier, parameters/profile, code/version, or run reference is absent. |
| `SOIL_EVIDENCE_REF_MISSING` | Required EvidenceRef, EvidenceBundle, or proof reference is absent. |
| `SOIL_IDENTITY_CONTINUITY_BROKEN` | Configured MUKEY/COKEY/CHKEY, mapunit/component/horizon, source-vintage, or join continuity is incomplete. |
| `SOIL_LINEAGE_STALE` | Upstream source, transform, evidence, or release reference changed without dependent Soil update. |
| `SOIL_CROSS_DOMAIN_AUTHORITY_COLLAPSE` | Candidate absorbs another domain's truth into Soil without preserving boundaries. |
| `LINEAGE_AS_TRUTH_DENIED` | Candidate treats lineage as proof closure, policy approval, source authority, or release approval. |
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
tests/validators/domains/soil/lineage/
├── README.md
├── test_soil_lineage.py
└── fixtures/
    ├── valid_soil_lineage_bundle/
    ├── missing_source_descriptor/
    ├── missing_source_role/
    ├── support_type_collapse/
    ├── source_family_collapse/
    ├── missing_source_vintage/
    ├── missing_transform_lineage/
    ├── broken_mukey_cokey_chkey_continuity/
    ├── stale_lineage/
    └── cross_domain_authority_collapse/
```

Suggested future command pattern:

```bash
pytest -q tests/validators/domains/soil/lineage
```

```bash
python tools/validators/domains/soil/lineage/validate_soil_lineage.py --repo-root . --format json
```

> [!NOTE]
> This is a proposed interface, not proof that `validate_soil_lineage.py` or the test path exists.

[Back to top](#top)

---

## Review checklist

- [ ] Validator reads declared Soil contracts, schemas, source descriptors, source-role rules, and policy rather than defining meaning locally.
- [ ] Source family, source role, support type, source vintage, transform lineage, and EvidenceRef support remain visible.
- [ ] MUKEY/COKEY/CHKEY and configured mapunit/component/horizon continuity remain traceable.
- [ ] Lineage checks do not replace SourceDescriptor, EvidenceBundle, proof, receipt, PolicyDecision, ReleaseManifest, correction, or rollback records.
- [ ] Cross-domain joins preserve Agriculture, Hydrology, Habitat, Fauna, Flora, Geology, and Hazards ownership boundaries.
- [ ] Public-bound outputs never point clients at RAW, WORK, QUARANTINE, unresolved candidates, direct internal stores, stale source descriptors, or stale transforms.
- [ ] Reports and receipts are written only to accepted roots.
- [ ] Validator output is not described as truth, policy, release, publication, source authority, or Directory Rules approval.
- [ ] Tests use public-safe or synthetic fixtures.
- [ ] Executable claims are backed by current repo evidence.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft README replacement for empty Soil lineage validator file. |
| Next smallest safe change | Verify actual Soil lineage scripts, accepted field names, schemas, source mappings, source descriptors, fixtures, report destinations, receipts, release linkage, cross-domain join behavior, and CI/runtime wiring before promoting this lane beyond draft. |
