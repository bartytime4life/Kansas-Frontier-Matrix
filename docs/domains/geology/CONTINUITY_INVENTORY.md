<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/geology-continuity-inventory
title: Geology — Continuity Inventory
type: standard
version: v2.0.0
prior_version: v1.1.1
status: draft
owners: TODO — Geology domain steward; Directory Rules owner
created: 2026-05-16
updated: 2026-10-12
policy_label: public
owning_root: docs/
responsibility: Navigational register of every artifact Geology doctrine expects across responsibility roots, recording tree-verified presence, status label, and doctrine source; not evidence, policy, release, or publication authority.
truth_posture: cite-or-abstain; CONFIRMED tracked-file presence as of 2026-10-11 / HOLD source-first RAW placement / PROPOSED, MISSING, or NEEDS VERIFICATION for absent, unadmitted, or maturity-unknown artifacts
related:
  - docs/domains/geology/README.md
  - docs/domains/geology/CANONICAL_PATHS.md
  - docs/domains/geology/SENSITIVITY.md
  - docs/domains/geology/SOURCE_REGISTRY.md
  - docs/domains/geology/VERIFICATION_BACKLOG.md
  - docs/adr/ADR-0030-geology-resource-character-vocabulary.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - docs/doctrine/directory-rules.md
  - docs/doctrine/ai-build-operating-contract.md
  - data/raw/README.md
  - data/raw/geology/README.md
  - docs/registers/DRIFT_REGISTER.md
  - docs/registers/VERIFICATION_BACKLOG.md
tags: [kfm, geology, natural-resources, continuity, inventory, register, directory-rules]
notes:
  - "2026-10-12: links to merged redirect stubs repointed to their canonical files (owner-directed duplicate removal follow-up)"
  - "2026-10-11 (v2.0.0): replaces the placeholder copy of CANONICAL_PATHS.md with a real continuity inventory"
  - "Presence claims come from a git ls-files inventory of the working tree on 2026-10-11; presence is not source admission, evidence closure, policy approval, release, or publication."
  - "Placement authority stays with Directory Rules and CANONICAL_PATHS.md; drift found here is reported in section 8 and is not fixed by this file."
  - "Doctrine-adjacent; pins CONTRACT_VERSION = 3.0.0 per ai-build-operating-contract.md."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Geology — Continuity Inventory

> A root-by-root register of every artifact the Geology and Natural Resources lane is expected to carry across KFM responsibility roots, with the **expected path**, the **doctrine source** that expects it, the **presence actually found in the tree**, and a **status label**. It is an audit and navigation surface, not an implementation or release claim.

![status: draft](https://img.shields.io/badge/status-draft-yellow)
![type: continuity register](https://img.shields.io/badge/type-continuity%20register-blue)
![version: v2.0.0](https://img.shields.io/badge/version-v2.0.0-informational)
![presence: tree-verified](https://img.shields.io/badge/presence-tree--verified-success)
![RAW placement: HOLD](https://img.shields.io/badge/RAW%20placement-HOLD-orange)
![exact subsurface points: deny by default](https://img.shields.io/badge/exact%20subsurface%20points-deny%20by%20default-critical)
![contract: 3.0.0](https://img.shields.io/badge/CONTRACT__VERSION-3.0.0-informational)
![last updated: 2026-10-11](https://img.shields.io/badge/updated-2026--10--11-blue)

| Field | Value |
|---|---|
| **Status** | `draft` · v2.0.0 |
| **Owners** | TODO — Geology domain steward; Directory Rules owner |
| **Last updated** | 2026-10-11 |
| **Authority class** | Navigational register (not canonical authority) |
| **Placement authority** | [`directory-rules.md`](../../doctrine/directory-rules.md) §12 (accepted via ADR-0029) · [`CANONICAL_PATHS.md`](CANONICAL_PATHS.md) for the Geology lane |
| **Presence method** | `git ls-files` over tracked files, 2026-10-11 (see [§1](#1-scope-and-method)) |
| **Contract** | Pinned `CONTRACT_VERSION = "3.0.0"` per `ai-build-operating-contract.md` |

> [!IMPORTANT]
> **Presence is not admission.** A row marked `CONFIRMED present` means a tracked file exists at that path. It does not mean a source is admitted, rights are cleared, an `EvidenceBundle` closes, a policy evaluates, a proof is accepted, or anything is released or published. Unknown rights or sensitivity stay fail-closed.

---

## Contents

1. [Scope and method](#1-scope-and-method)
2. [Status legend](#2-status-legend)
3. [At a glance](#3-at-a-glance)
4. [Inventory by responsibility root](#4-inventory-by-responsibility-root)
5. [Object-family continuity](#5-object-family-continuity)
6. [Continuity rules](#6-continuity-rules)
7. [Cross-lane edges](#7-cross-lane-edges)
8. [Drift and compatibility lanes found](#8-drift-and-compatibility-lanes-found)
9. [Verification backlog](#9-verification-backlog)
10. [Changelog](#10-changelog)
11. [Related docs](#11-related-docs)

---

## 1. Scope and method

**In scope.** Every Geology-segmented artifact across `docs/`, `contracts/`, `schemas/`, `policy/`, `tests/`, `fixtures/`, `tools/validators/`, `packages/`, `pipelines/`, `pipeline_specs/`, `configs/`, `connectors/`, `data/<phase>/`, `release/`, `apps/`, and `.github/workflows/`, plus the Geology-relevant source-first surfaces (`data/registry/sources/`, `docs/sources/`).

**Out of scope.** Object meaning (owned by `contracts/domains/geology/`), machine shape (owned by `schemas/contracts/v1/domains/geology/`), allow/deny decisions (owned by `policy/`), and placement law (owned by Directory Rules and `CANONICAL_PATHS.md`). This register points at those owners; it never restates them as authority.

**How presence was verified.**

- Tracked-file inventory: `git ls-files | grep -i geolog` across the whole repository, then per-root listings (`git ls-files <root>/…/geology`) for every path in §4.
- Absence checks: per-root `git ls-files` for the doctrinally expected path (for example `data/catalog/domains/`, `release/rollback_cards/`, `apps/governed-api/routes/domains/`) returning no Geology file.
- Substance checks: line counts on code files, so a one-line stub is not reported as an implementation.
- Duplicate checks: `cmp` between sibling Geology docs that share a subject.

Doctrine was read from `directory-rules.md` §12.2–§12.3 and the release rules `DIR-RELEASE-003`/`DIR-RELEASE-004`, `data/raw/README.md`, `data/raw/geology/README.md`, ADR-0030, and the Geology docs listed in [§11](#11-related-docs). Where doctrine and tree disagree, the tree decides **presence** and doctrine decides **expectation**; the disagreement goes to [§8](#8-drift-and-compatibility-lanes-found).

[Back to top](#top)

---

## 2. Status legend

| Label | Meaning in this register |
|---|---|
| `CONFIRMED present` | A tracked file exists at the expected path on 2026-10-11. Says nothing about maturity, admission, or release. |
| `MISSING` | An accepted rule or a current lane doc expects the artifact now, and the tree has none. |
| `PROPOSED` | Named only by draft or proposed docs or ADRs; absent; no accepted rule requires it yet. |
| `HOLD` | An accepted rule exists, but the concrete path or decision it needs does not. Do not create the artifact until an accepted decision exists. |
| `NEEDS VERIFICATION` | Present or absent, but its role, authority, or relation to doctrine cannot be settled from the tree alone. |

---

## 3. At a glance

| Attribute | Value | Basis |
|---|---|---|
| Lane segments present | `docs/`, `contracts/`, `schemas/`, `policy/`, `tests/`, `fixtures/`, `tools/validators/`, `packages/`, `pipelines/`, `pipeline_specs/`, `configs/`, `connectors/`, `data/<phase>/`, `release/candidates/`, `.github/workflows/` | §4 tree checks |
| Domain docs | 43 tracked files under `docs/domains/geology/` (32 top level, 11 under `sublanes/`) | `git ls-files` |
| Semantic contracts | 30 tracked files under `contracts/domains/geology/` | `git ls-files` |
| Machine schemas | 40 `*.schema.json` under `schemas/contracts/v1/domains/geology/` | `git ls-files` |
| Executable validation | 4 no-network fixture profiles in `.github/workflows/domain-geology.yml` (resource class, AEM campaign, public-safe geometry, production material change) | Geology README §15 + workflow file |
| Source descriptors | 1 JSON descriptor in `data/registry/sources/geology/` (KGS M-118, proposed inactive); 6 YAML entries in `data/registry/geology/sources/` | `git ls-files` |
| RAW placement | `HOLD` under `DIR-SOURCE-001`; `data/raw/geology/` is a compatibility/reference lane with no payloads | `data/raw/README.md`, `data/raw/geology/README.md` |
| Release state | Candidate index README only; no manifest, rollback card, or published payload | §4.11 |
| Resource-character vocabulary | ADR-0030 `proposed`; three characters fixture-positive, four unadmitted | ADR-0030 |

---

## 4. Inventory by responsibility root

Each row gives the artifact, the expected path, the doctrine source that expects it, what the tree holds, and the status label from [§2](#2-status-legend).

### 4.1 `docs/`

| Artifact | Expected path | Doctrine source | Tree presence | Status |
|---|---|---|---|---|
| Lane doc folder | `docs/domains/geology/` | Directory Rules §12.2 | 43 tracked files | `CONFIRMED present` |
| Lane landing README | `docs/domains/geology/README.md` | Directory Rules §12.2; Geology README §3 | Present, v1.2 | `CONFIRMED present` |
| Lane placement map | `docs/domains/geology/CANONICAL_PATHS.md` | Directory Rules §12 | Present | `CONFIRMED present` |
| This continuity inventory | `docs/domains/geology/CONTINUITY_INVENTORY.md` | Domain continuity-register pattern (sibling lanes) | Present, v2.0.0 | `CONFIRMED present` |
| Source docs (registry, sources, ledger, role matrix) | `docs/domains/geology/SOURCE_REGISTRY.md`, `SOURCES.md`, `SOURCE_LEDGER.md`, `SOURCE_ROLE_MATRIX.md` | Geology README §9 | All four present | `CONFIRMED present` |
| Sensitivity and policy docs | `docs/domains/geology/SENSITIVITY.md`, `POLICY.md` | Geology README §10 | Present; `SENSITIVITY_POSTURE.md` is a byte copy of `SENSITIVITY.md` (see §8) | `CONFIRMED present` |
| Object and identity docs | `docs/domains/geology/OBJECT_FAMILIES.md`, `IDENTITY_MODEL.md`, `UBIQUITOUS_LANGUAGE.md` | Geology README §7–§8 | All three present | `CONFIRMED present` |
| Lifecycle doc | `docs/domains/geology/DATA_LIFECYCLE.md` | Geology README §6 | Present | `CONFIRMED present` |
| Verification backlog | `docs/domains/geology/VERIFICATION_BACKLOG.md` | Geology README §16 | Present (`GEO-VB`, `GEO-SR`, `GEO-VT`, `GEO-AQ`, `GEO-IU` ids) | `CONFIRMED present` |
| API / map / Evidence Drawer docs | `docs/domains/geology/API_CONTRACTS.md`, `MAP_UI_CONTRACTS.md`, `UI_MAP_SURFACES.md`, `EVIDENCE_DRAWER_PAYLOAD.md`, `EVIDENCE_DRAWER_LANGUAGE.md` | Geology README §12–§13 | All five present | `CONFIRMED present` |
| Sublane docs | `docs/domains/geology/sublanes/` | Geology README §3 | 11 files; bedrock and surficial each have more than one doc (see §8) | `NEEDS VERIFICATION` |
| Runbooks | `docs/runbooks/geology/` | Geology runbook pattern | 6 files: README, BEDROCK_REVIEW, NO_NETWORK_TEST_RUNBOOK, PROMOTION_RUNBOOK, ROLLBACK_RUNBOOK, SOURCE_REFRESH_RUNBOOK | `CONFIRMED present` |
| Resource-character ADR | `docs/adr/ADR-0030-geology-resource-character-vocabulary.md` | Geology README §10; `GEO-AQ-04` | Present; status `proposed` | `CONFIRMED present` |
| Geology resource-classification ADR acceptance | ADR-0030 status `accepted` | `GEO-VB-03`, `GEO-AQ-04` | Not accepted | `PROPOSED` |
| Public-geometry threshold ADR | none filed | `GEO-AQ-05` | No ADR | `PROPOSED` |
| Domain dashboard | `docs/dashboards/domain/geology.md` | Dashboard index pattern | Present | `CONFIRMED present` |
| Intake source maps | `docs/intake/exploratory/geology-*-source-map.md` | ADR-0030 references | 4 files present | `CONFIRMED present` |
| Human source guidance | `docs/sources/catalog/kansas/ksgs.md`, `kcc-oil-gas-reg.md`; `docs/sources/catalog/usgs/usgs-mrds.md`, `usgs-ngmdb.md` | `DIR-SOURCE-003` | All four present; no dedicated page for KGS LAS, KGS/KDHE WWC5, or KGS oil and gas wells | `NEEDS VERIFICATION` |

### 4.2 `contracts/` — object meaning

| Artifact | Expected path | Doctrine source | Tree presence | Status |
|---|---|---|---|---|
| Lane contract folder | `contracts/domains/geology/` | Directory Rules §12.2 | 30 tracked files | `CONFIRMED present` |
| Object-family contracts | `contracts/domains/geology/<Family>.md` | Geology README §8 | 19 family contracts (see §5) | `CONFIRMED present` |
| Shared domain profile contracts | `domain_feature_identity.md`, `domain_layer_descriptor.md`, `domain_observation.md`, `domain_validation_report.md` | Directory Rules `DIR-SCOPELANE-004` | All four present | `CONFIRMED present` |
| Assessment-profile contracts | `geology_pipeline_specification_assessment.md`, `production_material_change.md`, `public_safe_geometry_assessment.md`, `subsurface_public_geometry_assessment.md` | Geology README §15 | All four present | `CONFIRMED present` |
| Reserve / production / permit / modeled-potential contracts | none | ADR-0030 (unadmitted characters) | Absent | `PROPOSED` |
| Flat contract alias | `contracts/geology/README.md` | Atlas v1.1 §24.13 short form (lineage) | README-only compatibility page | `NEEDS VERIFICATION` |

### 4.3 `schemas/` — machine shape

| Artifact | Expected path | Doctrine source | Tree presence | Status |
|---|---|---|---|---|
| Lane schema folder | `schemas/contracts/v1/domains/geology/` | `DIR-AUTHROOT-001`; Directory Rules §12.2 | 40 `*.schema.json` + READMEs | `CONFIRMED present` |
| Object-family schemas | `schemas/contracts/v1/domains/geology/<family>.schema.json` | Geology README §13 | 18 of 19 contracted families (see §5) | `CONFIRMED present` |
| `GeologyBoundaryVersion` schema | `schemas/contracts/v1/domains/geology/geology_boundary_version.schema.json` | Contract `GeologyBoundaryVersion.md` exists | Absent | `MISSING` |
| Proof-object schemas | `evidence_bundle`, `decision_envelope`, `geology_decision_envelope`, `release_manifest`, `rollback_card`, `run_receipt`, `promotion_decision`, `correction_notice`, `geoprivacy_transform_receipt` | Geology README §13 | All present (domain-local) | `NEEDS VERIFICATION` |
| Shared `resource_character` schema | shared vocabulary schema | ADR-0030 ("Shared schema: ABSENT") | Absent | `PROPOSED` |
| Flat schema alias | `schemas/contracts/v1/geology/README.md` | Atlas v1.1 §24.13 short form (lineage) | README-only alias guardrail; no schema files | `NEEDS VERIFICATION` |

### 4.4 `policy/`

| Artifact | Expected path | Doctrine source | Tree presence | Status |
|---|---|---|---|---|
| Lane policy folder | `policy/domains/geology/` | Directory Rules §12.2 | 16 tracked files | `CONFIRMED present` |
| Resource-class anti-collapse | `policy/domains/geology/resource-class-anti-collapse.rego` | `GEO-VT-02`; ADR-0030 | Present | `CONFIRMED present` |
| Public-geometry gates | `public-geometry.rego`, `public_safe_geometry.policy.json`, `release/public_safe_geometry.rego` | `GEO-VT-03`; SENSITIVITY.md | All present | `CONFIRMED present` |
| Exact subsurface sensitivity | `policy/domains/geology/sensitivity/borehole_exact_geometry.rego`, `extraction_site_exposure.rego`, `well_log_disclosure.rego` | SENSITIVITY.md decision lattice | All present | `CONFIRMED present` |
| Rights posture | `policy/domains/geology/rights/kgs_terms.yaml`, `kcc_terms.yaml`, `usgs_ngmdb_terms.yaml`; `borehole-rights.rego` | `GEO-VT-04`; `GEO-IU-01` | All present; terms content not verified as cleared | `NEEDS VERIFICATION` |
| Source-role anti-collapse | `policy/domains/geology/release/source_role_anti_collapse.rego` | `GEO-VT-01` | Present | `CONFIRMED present` |
| Abstain / unpublished gates | `abstain_on_ambiguous.rego`, `deny_unpublished.rego` | Geology README §14 | Both present | `CONFIRMED present` |
| Surficial sublane policy | `policy/domains/geology/sublanes/surficial/` | Geology sublane docs | `.gitkeep` only | `NEEDS VERIFICATION` |
| Policy evaluation evidence | `PolicyDecision` records for a Geology release | Geology README §10 | None | `MISSING` |

### 4.5 `tests/` and `fixtures/`

| Artifact | Expected path | Doctrine source | Tree presence | Status |
|---|---|---|---|---|
| Lane test folder | `tests/domains/geology/` | Directory Rules §12.2 | 23 tracked files | `CONFIRMED present` |
| Anti-collapse, geometry, AEM, production tests | `test_source_role_anti_collapse.py`, `test_public_safe_geometry.py`, `test_aem_campaign.py`, `test_production_material_change.py` | `GEO-VT-01`–`GEO-VT-03`; README §15 | All present and substantive | `CONFIRMED present` |
| No-network and smoke tests | `test_no_network_proof.py`, `test_geology_smoke.py` | No-network runbook | Both present | `CONFIRMED present` |
| Borehole-rights, catalog-closure, evidence-before-AI tests | `tests/domains/geology/test_borehole_rights/`, `test_catalog_closure/`, `test_evidence_before_ai/` | `GEO-VT-04`–`GEO-VT-06` | README-only directories; no test code | `MISSING` |
| Validator entrypoint tests | `tests/validators/domains/geology/` | Validator pattern | 8 files | `CONFIRMED present` |
| Lane fixture folder | `fixtures/domains/geology/` | Directory Rules §12.2 | 62 tracked files | `CONFIRMED present` |
| Resource-class fixtures | `fixtures/domains/geology/resource_class/{valid,invalid}/` | ADR-0030; `GEO-VT-02` | 3 valid, 8 invalid cases | `CONFIRMED present` |
| AEM campaign fixtures | `fixtures/domains/geology/aem_survey_campaign/` | README §15 | 1 valid, 11 invalid cases | `CONFIRMED present` |
| Contract-profile fixtures | `fixtures/contracts/v1/domains/geology/` | Assessment contracts | 19 files | `CONFIRMED present` |
| Golden / valid / invalid generic fixtures | `fixtures/domains/geology/{golden,valid,invalid}/` | `GEO-FB-06` thin slice | `PLACEHOLDER.md` + README only | `MISSING` |

### 4.6 `tools/validators/`

| Artifact | Expected path | Doctrine source | Tree presence | Status |
|---|---|---|---|---|
| Lane validator folder | `tools/validators/domains/geology/` | ADR-0042 convention note in DRIFT_REGISTER | 8 validators + README | `CONFIRMED present` |
| Resource-class validator | `validate_resource_class_distinction.py` | ADR-0030; `GEO-VT-02` | Present (513 lines) | `CONFIRMED present` |
| Public-safe geometry validator | `tools/validators/geology/public_safe_geometry/validate_public_safe_geometry.py` | `GEO-VT-03` | Present (568 lines); the `domains/` copy is a 6-line shim | `NEEDS VERIFICATION` |
| Assessment validators | `tools/validators/validate_geology_pipeline_specification_assessment.py`, `validate_geology_subsurface_public_geometry_assessment.py`, `validate_geology_evidence_bundle_projection.py` | Assessment contracts | Present at `tools/validators/` top level | `NEEDS VERIFICATION` |
| Borehole-rights validator | `tools/validators/geology/borehole_rights/` | `GEO-VT-04` | README only | `MISSING` |

### 4.7 `packages/`, `pipelines/`, `pipeline_specs/`, `configs/`

| Artifact | Expected path | Doctrine source | Tree presence | Status |
|---|---|---|---|---|
| Domain package | `packages/domains/geology/` | Directory Rules §12.2 | 10 files; `src/geology/__init__.py` is empty; submodules are READMEs | `NEEDS VERIFICATION` |
| Pipelines | `pipelines/<stage>/geology/` | Directory Rules §12.2 | None under stage roots; `pipelines/domains/geology/` holds 7 READMEs, no code | `NEEDS VERIFICATION` |
| Declarative specs | `pipeline_specs/geology/` | Directory Rules §12.2 | 12 files (stage specs + per-family specs) | `CONFIRMED present` |
| Lane config | `configs/domains/geology/` | Config root pattern | README only | `CONFIRMED present` |

### 4.8 `connectors/` and source registry

| Artifact | Expected path | Doctrine source | Tree presence | Status |
|---|---|---|---|---|
| KGS connectors | `connectors/<source_id or provider>/` | `DIR-SOURCE-002`, `DIR-SOURCE-003` | `connectors/kgs/`, `kgs_bedrock/`, `kgs_surficial/`, `kgs_las/`, `kgs_oil_gas_wells/`, `kgs_kdhe_wwc5/` — README only | `NEEDS VERIFICATION` |
| KSGS connector package | `connectors/ksgs/` | `DIR-SOURCE-002` | Package scaffold; `fetch.py` and `admit.py` are 1-line stubs | `NEEDS VERIFICATION` |
| KCC and USGS connectors | `connectors/kcc_oil_gas_reg/`, `connectors/usgs_mrds/`, `connectors/usgs_ngmdb/` | `DIR-SOURCE-002` | README only | `NEEDS VERIFICATION` |
| Domain-named connector index | `connectors/geology/` | Rejected as runtime hierarchy by its own README | README + `kgs/README.md` compatibility index | `NEEDS VERIFICATION` |
| Canonical source descriptors | `data/registry/sources/<source_id>/` | `DIR-SOURCE-003` | One descriptor at `data/registry/sources/geology/kgs-m118-surficial-geology.source.json` (domain subfolder, not `<source_id>`) | `NEEDS VERIFICATION` |
| Descriptors for the eight ledger families | `data/registry/sources/…` | `GEO-VB-01`; `GEO-SR-01`–`GEO-SR-08` | None besides KGS M-118 | `MISSING` |
| Domain registry view | `data/registry/geology/sources/` | `DIR-SOURCE-004` (generated view only) | 6 YAML entries written directly, not generated | `NEEDS VERIFICATION` |
| Sensitivity registry | `data/registry/sensitivity/geology/` | Directory Rules §12.3 subtype-first registry | README only | `CONFIRMED present` |

### 4.9 `data/` lifecycle phases

| Phase | Expected path | Doctrine source | Tree presence | Status |
|---|---|---|---|---|
| RAW (source-first capture) | Source-first capture home; exact physical path undecided | `DIR-SOURCE-001`; `data/raw/README.md` | `data/raw/geology/README.md` only, as a compatibility/reference lane; no payloads | `HOLD` |
| WORK | `data/work/geology/` | Directory Rules §12.2 | README only | `CONFIRMED present` |
| QUARANTINE | `data/quarantine/geology/` (+ `rights_unknown/`) | Directory Rules §12.2 | READMEs only | `CONFIRMED present` |
| PROCESSED | `data/processed/geology/` | Directory Rules §12.2 | README only | `CONFIRMED present` |
| CATALOG (subtype-first) | `data/catalog/domains/geology/` | Directory Rules §12.3 catalog projections | Absent; `data/catalog/domain/geology/` holds the lane README | `MISSING` |
| TRIPLETS | `data/triplets/geology/` | `DIR-DATA-002` (optional) | `.gitkeep` only, plus `data/triplets/exports/geology/.gitkeep` | `NEEDS VERIFICATION` |
| PUBLISHED | `data/published/layers/geology/` | Geology README §5 | READMEs only (incl. `surficial/`); sibling `published/geology/`, `geoparquet/geology/`, `pmtiles/geology/` READMEs | `CONFIRMED present` |
| Receipts | `data/receipts/geology/` | Directory Rules §12.2 | README; 20 Geology generation receipts in `data/receipts/generated/` | `CONFIRMED present` |
| Proofs | `data/proofs/geology/` | `GEO-IU-07` | README only; no accepted proof packet | `CONFIRMED present` |
| Reports | `data/reports/geology/` | Data-root lane | README only | `CONFIRMED present` |
| Lane registry indexes | `data/registry/geology/` (file register, missing-or-planned, preservation matrix, release index, source-state index, verification backlog) | Geology registry README | 7 top-level files plus `sources/` | `NEEDS VERIFICATION` |
| Rollback lane | `data/rollback/geology/` | `DIR-RELEASE-004` deprecates `data/rollback/` | README present | `NEEDS VERIFICATION` |

### 4.10 `apps/` and `.github/workflows/`

| Artifact | Expected path | Doctrine source | Tree presence | Status |
|---|---|---|---|---|
| Governed-API Geology route | `apps/governed-api/routes/domains/geology/` | Route-family README (listed `PROPOSED`) | Absent | `PROPOSED` |
| Explorer Geology legend route | `apps/site/source/app/api/event-atlas/geology-legend/route.ts` | Explorer site | Present; proxies an upstream KGS legend at request time (see §8) | `NEEDS VERIFICATION` |
| Lane CI workflow | `.github/workflows/domain-geology.yml` | `GEO-IU-06` | Present; four bounded no-network profiles | `CONFIRMED present` |
| Assessment workflows | `.github/workflows/geology-evidence-bundle-convergence.yml`, `geology-pipeline-specification-assessment.yml`, `geology-subsurface-public-geometry-assessment.yml` | Assessment contracts | All three present | `CONFIRMED present` |
| Source-descriptor workflow | `.github/workflows/kgs-m118-source-descriptor.yml` | KGS M-118 descriptor | Present | `CONFIRMED present` |

### 4.11 `release/`

| Artifact | Expected path | Doctrine source | Tree presence | Status |
|---|---|---|---|---|
| Candidate index | `release/candidates/geology/` | Directory Rules §12.2 (`release/<object_family>/geology/`) | README only; no child candidate dossier | `CONFIRMED present` |
| Release manifest | `release/manifests/` (Geology entry) | Geology README §6 PUBLISHED gate | None | `PROPOSED` |
| Rollback card | `release/rollback_cards/` (Geology entry) | `DIR-RELEASE-003` | None (no Geology release exists to roll back) | `PROPOSED` |
| Rollback execution receipts | `data/receipts/rollback/` (Geology entry) | `DIR-RELEASE-003` | None | `PROPOSED` |

[Back to top](#top)

---

## 5. Object-family continuity

Family names follow the current carriers in `contracts/domains/geology/` and `schemas/contracts/v1/domains/geology/`. The short-form versus `…Reference` naming conflict stays `CONFLICTED` (`GEO-AQ-08`); a carrier's existence does not resolve it.

| Family | Contract | Schema | Status |
|---|---|---|---|
| `GeologicUnit` | `GeologicUnit.md` | `geologic_unit.schema.json` | `CONFIRMED present` |
| `SurficialUnit` | none | none | `NEEDS VERIFICATION` (folded into `GeologicUnit` in README §7) |
| `Lithology` | `Lithology.md` | `lithology.schema.json` | `CONFIRMED present` |
| `StratigraphicInterval` | `StratigraphicInterval.md` | `stratigraphic_interval.schema.json` | `CONFIRMED present` |
| `GeologicAge` | `GeologicAge.md` | `geologic_age.schema.json` | `CONFIRMED present` |
| `StructureFeature` | `StructureFeature.md` | `structure_feature.schema.json` | `CONFIRMED present` |
| `GeologyBoundaryVersion` | `GeologyBoundaryVersion.md` | none | `MISSING` (schema) |
| `BoreholeReference` | `BoreholeReference.md` | `borehole_reference.schema.json` | `CONFIRMED present` |
| `WellLogReference` | `WellLogReference.md` | `well_log_reference.schema.json` | `CONFIRMED present` |
| `CoreSample` | `CoreSample.md` | `core_sample.schema.json` | `CONFIRMED present` |
| `GeophysicalObservation` | `GeophysicalObservation.md` | `geophysical_observation.schema.json` | `CONFIRMED present` |
| `GeochemistrySample` | `GeochemistrySample.md` | `geochemistry_sample.schema.json` | `CONFIRMED present` |
| `MineralOccurrence` | `MineralOccurrence.md` | `mineral_occurrence.schema.json` | `CONFIRMED present` |
| `ResourceDeposit` | `ResourceDeposit.md` | `resource_deposit.schema.json` | `CONFIRMED present` |
| `ResourceEstimate` | `ResourceEstimate.md` | `resource_estimate.schema.json` | `CONFIRMED present` |
| `ExtractionSite` | `ExtractionSite.md` | `extraction_site.schema.json` | `CONFIRMED present` |
| `ReclamationRecord` | `ReclamationRecord.md` | `reclamation_record.schema.json` | `CONFIRMED present` |
| `CrossSection` | `CrossSection.md` | `cross_section.schema.json` | `CONFIRMED present` |
| `HydrostratigraphicUnit` | `HydrostratigraphicUnit.md` | `hydrostratigraphic_unit.schema.json` | `CONFIRMED present` |
| `AemSurveyCampaign` | `AemSurveyCampaign.md` | `aem_survey_campaign.schema.json` | `CONFIRMED present` (not in the README §8 list) |
| Reserve, production, permit, modeled-potential records | none | none | `PROPOSED` (unadmitted per ADR-0030) |

[Back to top](#top)

---

## 6. Continuity rules

These rules must survive every change to the lane. Each one cites its owner; this register only records that it must persist.

### 6.1 Lifecycle and no-skip

- Geology moves RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED. Promotion is a governed state transition that emits a new state or version, never a copy, move, filename, or job completion (`DIR-DATA-003`, `DIR-DATA-004`).
- No pipeline writes to `data/published/layers/geology/` from RAW or WORK. Every gate in Geology README §6 applies: `SourceDescriptor` before WORK; validation and policy (or a recorded quarantine reason) before PROCESSED; `EvidenceRef`, `ValidationReport`, and digest closure before CATALOG; `ReleaseManifest`, correction path, rollback target, and review state before PUBLISHED.
- A source without a `SourceDescriptor` that confirms rights, attribution, and source role does not pass WORK / QUARANTINE (Geology README §9).

### 6.2 Source-first RAW

- One capture, one identity: a Geology-supporting capture is stored once under the source-first home and may support several domains without duplicate bytes (`DIR-SOURCE-001`).
- The exact physical source-first path is `HOLD`. `data/raw/geology/` is a compatibility/reference lane only; it receives no payloads and is not a capture home (`data/raw/README.md`, `data/raw/geology/README.md`).
- A `source_id` is registered once; machine descriptors live under `data/registry/sources/`, human guidance under `docs/sources/`, connector code under `connectors/` (`DIR-SOURCE-002`, `DIR-SOURCE-003`). `data/registry/geology/sources/` may only be a generated view (`DIR-SOURCE-004`).

### 6.3 Watcher as non-publisher

Connectors and watchers emit only to the source-first RAW home (path `HOLD`) or to `data/quarantine/geology/`. A watcher that sees a change records a receipt or a candidate decision; it never promotes or publishes. The production material-change profile keeps this boundary: its `watcher_publication_authority.json` fixture is an invalid case.

### 6.4 Schema home

Machine schemas default to `schemas/contracts/v1/domains/geology/` (`DIR-AUTHROOT-001`; ADR-0001 is still `proposed` but the accepted Directory Rules carry the default). `contracts/` owns meaning, `schemas/` owns shape. The flat `schemas/contracts/v1/geology/` and `contracts/geology/` paths are alias or compatibility pages and must not gain parallel schema or contract content.

### 6.5 Knowledge-character anti-collapse

Geology keeps distinct the character of every resource-related claim. Per ADR-0030 and Geology README §10:

| Character | Is | Is not |
|---|---|---|
| Occurrence (`MINERAL_OCCURRENCE`) | Reported presence at a source-supported place | Deposit, quantity, reserve, permit, production, ownership |
| Deposit (`RESOURCE_DEPOSIT`) | Named or delineated body | Estimate, reserve, permit, production, title, operation |
| Estimate (`RESOURCE_ESTIMATE`) | Quantity or classification under a stated method | Direct observation, deposit identity, reserve by default |
| Reserve (`RESERVE`) | Source-classified reserve under a cited scheme | Estimate, deposit, occurrence, KFM certification |
| Permit (`PERMIT`) | Issuer- and jurisdiction-bound authorization | Resource existence, extraction, production, compliance |
| Operation | An operating or extraction-site record (`ExtractionSite`) | Proof of production, permit validity, or current operation from a permit alone |
| Production (`PRODUCTION`) | Time-bounded reported production record | Deposit, reserve, estimate, permit validity, current operation |
| Map | A scale-bound interpreted compilation (for example KGS M-118) | Point-level observed fact |
| Model (`MODELED_POTENTIAL`, `CrossSection`) | Model-derived or interpretive product with version and uncertainty | Occurrence or deposit truth; an attestation |
| Legal title | Ownership or lease assertion owned by People / Land | Anything a Geology object can prove |

Rules that persist: one record carries exactly one normalized character; unknown or multiple values fail closed; a public-safe geometry declaration, a validator pass, or a release path does not establish character; AI wording cannot upgrade an estimate to a reserve. Today only `MINERAL_OCCURRENCE`, `RESOURCE_DEPOSIT`, and `RESOURCE_ESTIMATE` are fixture-positive; the other characters are unadmitted until ADR-0030 is accepted and their contracts exist.

### 6.6 Exact subsurface points: deny or generalize by default

- Exact borehole, well-log, core, geochemistry-sample, sensitive-resource, extraction-targetable deposit, and private-well locations enter at the most restrictive tier and are `DENY` for public exact exposure (SENSITIVITY.md decision lattice and table).
- Public release requires a generalization transform (cell binning, county or basin rollup) recorded in a `RedactionReceipt` or `AggregationReceipt`, plus the reviewer that SENSITIVITY.md names. An aggregate tier does not back-fill onto the underlying point records.
- Rights-controlled content (for example KGS LAS curves) is `DENY` for derivative public release until terms are cleared.
- Where sibling docs disagree on the default tier (see §8, D-05), the most restrictive applicable default governs, per the `ai-build-operating-contract.md` §23.2/§23.3 rule that SENSITIVITY.md cites.
- Until `GEO-VB-02` closes, no public surface bypasses this posture without a documented exception in `docs/registers/DRIFT_REGISTER.md`.

### 6.7 Trust membrane and governed AI

Public clients read released artifacts through `apps/governed-api/`, never RAW, WORK, QUARANTINE, or PROCESSED stores. Governed AI reads released `EvidenceBundle`s only, `ABSTAIN`s on thin evidence, `DENY`s on policy, rights, sensitivity, or release blocks, and emits an `AIReceipt` (Geology README §14).

[Back to top](#top)

---

## 7. Cross-lane edges

Geology README §11 lists the edges. Each must keep ownership, source role, sensitivity, and `EvidenceBundle` support.

| Related lane | Edge | Constraint that must persist | Tree evidence |
|---|---|---|---|
| Soil | Parent material and surficial context | Soil owns soil objects | Doctrine only |
| Hydrology | `HydrostratigraphicUnit`; aquifer context | Geology does not replace hydrology measurements | Hydrology invalid fixtures `aquifer_context_link/invalid/invalid_geology_geometry.json` and `aquifer_observation/invalid/invalid_embedded_geology.json` exist |
| Hazards | Fault, landslide, subsidence context | Hazards owns risk | Doctrine only |
| People / Land | Lease, parcel, operator relation | Geology objects never prove ownership or title; parcel joins with exact points `DENY` | Doctrine only |
| Planetary / 3D | Subsurface scenes, cross-sections | 3D is an alternate renderer, not an alternate truth path | `INFERRED` edge (README §11) |
| Archaeology | Lithic source-area context | Archaeology owns sensitivity and review | `INFERRED` edge (README §11) |

No `contracts/cross_domain/`, `tests/cross_domain/`, or `tools/validators/cross_domain/` seam exists for Geology (Directory Rules §12.5); join policy stays open under `GEO-AQ-06`.

[Back to top](#top)

---

## 8. Drift and compatibility lanes found

Reported here, not fixed here. Each item belongs to its owning doc, register, or ADR.

| ID | Finding | Evidence | Suggested owner |
|---|---|---|---|
| D-01 | `SENSITIVITY_POSTURE.md` is a byte-for-byte copy of `SENSITIVITY.md` and shares its `doc_id` (`kfm://doc/geology-sensitivity`) — the same pattern this file had before v2.0.0. | `cmp` reports identical files | Geology docs steward |
| D-02 | `CANONICAL_PATHS.md` §6.1 still names RAW as `data/raw/geology/<source_id>/<run_id>/` and §8 routes connectors there, contrary to `DIR-SOURCE-001` (placement `HOLD`; domain lane is reference-only). | `CANONICAL_PATHS.md` §6.1, §8, §9 | `CANONICAL_PATHS.md` owner |
| D-03 | `CANONICAL_PATHS.md` §6.1 names rollback as `data/rollback/geology/<release_id>/`; `DIR-RELEASE-003`/`004` put `RollbackCard` under `release/rollback_cards/` and deprecate `data/rollback/`. `data/rollback/geology/README.md` is tracked. | `CANONICAL_PATHS.md` §6.1; `directory-rules.md` | `CANONICAL_PATHS.md` owner; release steward |
| D-04 | Catalog lane is `data/catalog/domain/geology/` (singular, sibling form); Directory Rules §12.3 makes subtype-first `data/catalog/domains/` canonical and calls `data/catalog/domain/` a migration candidate. A root-level `catalog/domain/geology/` compatibility redirect also exists. | `git ls-files data/catalog catalog` | Catalog steward |
| D-05 | Default tier for exact borehole / well-log points: `CANONICAL_PATHS.md` §7 says T1 generalized (T4 only for private or rights-restricted); `SENSITIVITY.md` puts exact `Borehole`, `WellLog`, `CoreSample`, `GeochemistrySample` at T4. | Both docs | Sensitivity reviewer; `GEO-AQ-03` |
| D-06 | `data/registry/geology/sources/` holds six hand-written YAML entries (`ksgs_*`, `usgs_*`, `kgs_gmd3_aem_2026`); `DIR-SOURCE-004` allows only a generated view. The one JSON descriptor sits at `data/registry/sources/geology/` (domain segment) rather than a `<source_id>` folder. | `git ls-files data/registry` | Source steward |
| D-07 | Validators are split across `tools/validators/domains/geology/`, `tools/validators/geology/`, and top-level `tools/validators/validate_geology_*.py`; the public-safe geometry validator is real under `geology/` and a 6-line shim under `domains/geology/`. | Line counts | Validation steward |
| D-08 | Three overlapping catalog-closure test folders: `tests/domains/geology/catalog-closure/`, `catalog_closure/`, `test_catalog_closure/` (all README-only). | `git ls-files tests/domains/geology` | Test steward |
| D-09 | Bedrock had three docs (`SUBLANE-BEDROCK.md`, `sublanes/bedrock.md`, `sublanes/bedrock_geology.md`); on 2026-10-12 both sublane drafts were merged into `SUBLANE-BEDROCK.md` and are now redirect stubs, so the bedrock half is resolved (OQ-GEOL-BED-05). Surficial had two (`surficial.md`, `sublanes/surficial.md`); on 2026-10-12 `sublanes/surficial.md` was merged into the flat `surficial.md` and is now a redirect stub, so D-09 is resolved. | `cmp`, titles | Geology docs steward |
| D-10 | Pipelines sit at `pipelines/domains/geology/` while Directory Rules §12.2 illustrates `pipelines/<stage>/<domain>/`. | `git ls-files pipelines` | Pipeline steward |
| D-11 | Empty-scaffold markers (`.gitkeep`) in `data/triplets/geology/`, `data/triplets/exports/geology/`, `catalog/domain/geology/`, and `policy/domains/geology/sublanes/surficial/`; `DIR-SCOPELANE-003` prohibits empty symmetry scaffolding. | `git ls-files` | Directory Rules owner |
| D-12 | The Explorer route `geology-legend/route.ts` fetches an upstream KGS ArcGIS legend at request time, outside `apps/governed-api/`. `apps/site/source/public/data/subsurface/geophysics.json` carries a KGS "All Rights Reserved" attribution, and the hydrology-facing `kgs-monitoring-wells.geojson` holds exact well points. Trust-membrane, rights, and exact-point posture for these need review. | File reads | Explorer owner; rights and sensitivity reviewers |
| D-13 | Domain-named connector folder `connectors/geology/` exists although its own README says source-first doctrine rejects it as a runtime hierarchy. | `connectors/geology/README.md` | Connector steward |

[Back to top](#top)

---

## 9. Verification backlog

Items this inventory adds or carries. Lane-wide ids (`GEO-*`) stay owned by `VERIFICATION_BACKLOG.md`.

| ID | Item | Evidence that would settle it | Links | Status |
|---|---|---|---|---|
| CI-GEO-01 | Source-first physical RAW placement for Geology captures, and disposition of `data/raw/geology/` | Accepted placement and migration decision under `DIR-SOURCE-001` | D-02 | `HOLD` |
| CI-GEO-02 | `SourceDescriptor`s with rights, role, and cadence for all eight ledger families | Descriptors under `data/registry/sources/` + rights review records | `GEO-VB-01`, `GEO-SR-01`–`08`, D-06 | `MISSING` |
| CI-GEO-03 | Borehole / well-log public policy and tier reconciliation | Accepted tier scheme + reconciled docs | `GEO-VB-02`, `GEO-AQ-03`, D-05 | `NEEDS VERIFICATION` |
| CI-GEO-04 | Resource-character vocabulary acceptance and contracts for reserve, production, permit, modeled potential | ADR-0030 accepted + contracts + fixtures | `GEO-VB-03`, `GEO-AQ-04` | `PROPOSED` |
| CI-GEO-05 | `GeologyBoundaryVersion` schema | Schema file + fixture + contract cross-link | §5 | `MISSING` |
| CI-GEO-06 | Borehole-rights, catalog-closure, evidence-before-AI tests and validators | Test code + fixtures + CI step | `GEO-VT-04`–`06`, D-08 | `MISSING` |
| CI-GEO-07 | Governed-API Geology route, Explorer layer adapter, Evidence Drawer runtime | Route code + smoke test | `GEO-VB-04`, `GEO-IU-08`, D-12 | `PROPOSED` |
| CI-GEO-08 | Catalog lane convergence to `data/catalog/domains/` | Catalog steward decision + migration plan | D-04 | `NEEDS VERIFICATION` |
| CI-GEO-09 | Rollback lane convergence to `release/rollback_cards/` | Classification of `data/rollback/geology/` per `DIR-RELEASE-004` | D-03 | `NEEDS VERIFICATION` |
| CI-GEO-10 | First Geology release: manifest, rollback card, `PolicyDecision`, accepted proof | Release candidate dossier under `release/candidates/geology/` | §4.11, `GEO-IU-07` | `PROPOSED` |
| CI-GEO-11 | Retire duplicate docs (`SENSITIVITY_POSTURE.md`; bedrock and surficial doubles) | Steward decision + redirects | D-01, D-09 | `NEEDS VERIFICATION` |

[Back to top](#top)

---

## 10. Changelog

| Version | Date | Change |
|---|---|---|
| v2.0.0 | 2026-10-11 | Replaces the placeholder copy of `CANONICAL_PATHS.md` with a real continuity inventory: tree-verified presence for every Geology lane across responsibility roots, object-family contract/schema pairing, continuity rules (lifecycle, source-first RAW, watcher as non-publisher, schema home, knowledge-character anti-collapse, exact subsurface-point defaults), cross-lane edges, a drift report, and a verification backlog. |
| v1.1.1 | 2026-10-11 | Gave the file its own `doc_id` and a placeholder note; body was still a copy of `CANONICAL_PATHS.md`. |
| v1.1 and earlier | 2026-05-16 onward | Byte-for-byte copy of `CANONICAL_PATHS.md` sharing its `doc_id`. |

**When to update this register:** a Geology lane path is added, removed, or moved; a `MISSING` or `PROPOSED` row gains a file; ADR-0030 or a `GEO-AQ` ADR is accepted; a drift item in §8 is resolved. Re-run the presence checks in §1 and bump `version` and `updated` in the meta block.

---

## 11. Related docs

- [`docs/domains/geology/README.md`](README.md) — lane landing, object families, source families, sensitivity summary
- [`docs/domains/geology/CANONICAL_PATHS.md`](CANONICAL_PATHS.md) — Geology placement map
- [`docs/domains/geology/SENSITIVITY.md`](SENSITIVITY.md) — tier lattice and exact-point defaults
- [`docs/domains/geology/SOURCE_REGISTRY.md`](SOURCE_REGISTRY.md) — source families and roles
- [`docs/domains/geology/VERIFICATION_BACKLOG.md`](VERIFICATION_BACKLOG.md) — lane-wide `GEO-*` backlog
- [`docs/adr/ADR-0030-geology-resource-character-vocabulary.md`](../../adr/ADR-0030-geology-resource-character-vocabulary.md) — resource-character vocabulary (proposed)
- [`docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md`](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) — accepted Directory Rules adoption
- [`docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md`](../../adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) — schema home (proposed)
- [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md) — §12 lane pattern, §12.3 source identity, `DIR-RELEASE-003`/`004`
- [`data/raw/README.md`](../../../data/raw/README.md) — RAW root contract; source-first identity, placement `HOLD`
- [`data/raw/geology/README.md`](../../../data/raw/geology/README.md) — Geology RAW compatibility/reference lane
- [`docs/registers/DRIFT_REGISTER.md`](../../registers/DRIFT_REGISTER.md) — repository drift register
- [`docs/registers/VERIFICATION_BACKLOG.md`](../../registers/VERIFICATION_BACKLOG.md) — repository verification backlog

---

**Version:** v2.0.0 · **Last updated:** 2026-10-11 · **Owners:** TODO — Geology domain steward; Directory Rules owner · [Back to top](#top)
