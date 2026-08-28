<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-soil-readme
title: pipeline_specs/soil/ — Governed Soil Pipeline Specification Boundary
type: readme; directory-readme; declarative-pipeline-spec-boundary
version: v0.2
status: draft; repository-grounded; five-placeholder-specs-confirmed; no-active-soil-spec-established
owners:
  - OWNER_TBD — Pipeline-spec steward
  - OWNER_TBD — Soil domain steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Evidence and receipt steward
  - OWNER_TBD — Policy and rights steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Docs steward
created: 2026-06-13
updated: 2026-07-18
supersedes: v0.1
policy_label: public-doc; pipeline-specs; soil; declarative-only; source-role-aware; support-type-separated; evidence-bound; policy-gated; release-gated; no-public-path
current_path: pipeline_specs/soil/README.md
truth_posture: CONFIRMED target README, parent pipeline-spec boundary, five direct Soil YAML files with empty stages arrays, Soil executable-lane READMEs, Soil semantic-contract and schema lanes, flat schema compatibility index, source-registry topology warning, Soil policy scaffold, Soil test-parent README, Soil fixture stub, TODO-only domain-soil workflow, CODEOWNERS routing, and absence of a checked nested pipeline_specs/domains/soil compatibility README / PROPOSED future Soil pipeline-spec schema, parser-consumer binding, source-descriptor binding, support-type enum, lifecycle-transition grammar, negative fixtures, spec-to-implementation tests, generated receipt requirements, activation registry, schedules, correction behavior, and rollback behavior / UNKNOWN exhaustive branch history, unindexed or generated specs, accepted pipeline-spec schema, active parser, active consumer, live-source activation, deployed schedules, runtime execution, emitted Soil pipeline receipts, promotion dependency, branch protection, recent workflow results, and production publication behavior / NEEDS VERIFICATION named owners, accepted Directory Rules copy, schema-path migration, source-registry topology, rights and operator-consent decisions, fixture and validator coverage, no-network enforcement, field/parcel/owner-specific policy, review separation, release integration, correction propagation, and rollback execution
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  visibility: public
  base_ref: main
  base_commit: 2bde43821a398aff1fa1a862e6d7f61e7d68e6c9
  target_prior_blob: 4069a620b637b2098465dd2800fd16c269318281
  direct_lane_files_confirmed:
    - pipeline_specs/soil/README.md
    - pipeline_specs/soil/ingest.yaml
    - pipeline_specs/soil/normalize.yaml
    - pipeline_specs/soil/validate.yaml
    - pipeline_specs/soil/catalog.yaml
    - pipeline_specs/soil/publish.yaml
  checked_absent_paths:
    - pipeline_specs/domains/soil/README.md
    - tests/pipeline_specs/soil/README.md
    - fixtures/pipeline_specs/soil/README.md
  inventory_method: GitHub connector file reads plus bounded repository code-index queries; absence claims are limited to checked paths and indexed results
related:
  - ../README.md
  - ../../CONTRIBUTING.md
  - ../../docs/architecture/directory-rules.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - ../../docs/registers/DRIFT_REGISTER.md
  - ../../docs/domains/soil/CANONICAL_PATHS.md
  - ../../docs/domains/soil/ARCHITECTURE.md
  - ../../pipelines/domains/soil/README.md
  - ../../pipelines/domains/soil/ssurgo_ingest/README.md
  - ../../pipelines/domains/soil/mesonet_normalizer/README.md
  - ../../pipelines/domains/soil/moisture_validator/README.md
  - ../../contracts/domains/soil/README.md
  - ../../schemas/contracts/v1/domains/soil/README.md
  - ../../schemas/contracts/v1/soil/README.md
  - ../../policy/domains/soil/README.md
  - ../../tests/pipelines/README.md
  - ../../tests/domains/soil/README.md
  - ../../fixtures/domains/soil/README.md
  - ../../data/registry/sources/soil/README.md
  - ../../data/receipts/generated/README.md
  - ../../schemas/contracts/v1/receipts/generated_receipt.schema.json
  - ../../.github/workflows/README.md
  - ../../.github/workflows/domain-soil.yml
  - ../../.github/workflows/codeql.yml
  - ../../.github/CODEOWNERS
notes:
  - "v0.2 replaces planning-heavy file trees and activation implications with a commit-pinned inventory of the five direct Soil YAML scaffolds."
  - "All five confirmed YAML files contain only name, version, and an empty stages array; they are placeholder declarations, not active pipelines."
  - "The README preserves the Soil support-type anti-collapse invariant across static survey, gridded derivative, station observation, satellite grid, pedon/profile evidence, and interpretation."
  - "This documentation-only revision does not change any YAML payload, executable pipeline, connector, schema, contract, policy, fixture, test, workflow, lifecycle record, release object, public artifact, API, map, or AI behavior."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `pipeline_specs/soil/` — Governed Soil Pipeline Specification Boundary

> Declarative Soil pipeline-spec lane for describing **what** a Soil pipeline is allowed to attempt, which admitted sources and support types it may consume, which lifecycle transitions and governance gates it requires, and which finite failure states must block execution or release—without becoming executable pipeline logic, source admission, evidence, policy, release authority, or soil truth.

<p>
  <img alt="Status: repository-grounded draft" src="https://img.shields.io/badge/status-repository--grounded%20draft-yellow">
  <img alt="Direct specs: five placeholders" src="https://img.shields.io/badge/direct__specs-five__placeholders-lightgrey">
  <img alt="Stages: empty" src="https://img.shields.io/badge/stages-empty-orange">
  <img alt="Support type: separated" src="https://img.shields.io/badge/support__types-separated-critical">
  <img alt="Network: not activated" src="https://img.shields.io/badge/network-not__activated-critical">
  <img alt="Publication: denied" src="https://img.shields.io/badge/publication-DENIED-red">
</p>

**Path:** `pipeline_specs/soil/README.md`
**Version:** `v0.2`
**Status:** draft / repository-grounded / five placeholder YAML specs confirmed / no active Soil spec established
**Owning root:** `pipeline_specs/` — declarative pipeline configuration
**Domain segment:** `soil`
**Public posture:** no direct public path; no spec, run, check, commit, pull request, or workflow completion is publication
**Evidence snapshot:** `main@2bde43821a398aff1fa1a862e6d7f61e7d68e6c9`

> [!IMPORTANT]
> The direct Soil lane contains five YAML files, but every one has `stages: []`. Their presence proves only that placeholder declarations exist. It does **not** prove a parser accepts them, a consumer binds them to executable code, a source is admitted, a run is scheduled, validation is enforced, receipts are emitted, promotion is blocked, or public artifacts are released.

> [!CAUTION]
> Soil support types are not interchangeable. Static SSURGO-style survey evidence, gridded derivatives, station observations, satellite grids, pedon/profile evidence, and interpretations must remain distinguishable through source role, spatial support, temporal support, uncertainty, evidence, policy, and release state.

---

## Quick navigation

[Purpose](#purpose) · [Authority](#authority-boundary) · [Current state](#confirmed-current-state) · [Placement](#placement-and-drift-posture) · [Inventory](#direct-lane-inventory) · [Support types](#soil-support-type-boundary) · [Minimum contract](#minimum-future-spec-contract) · [Sources](#source-admission-rights-and-activation) · [Lifecycle](#lifecycle-and-gates) · [Outcomes](#finite-outcomes-and-reason-codes) · [Sensitivity](#sensitivity-scale-and-public-safety) · [Receipts](#evidence-receipts-catalog-and-release) · [Validation](#validation-and-enforceability) · [Review](#review-and-change-discipline) · [Rollback](#deactivation-correction-and-rollback) · [Done](#definition-of-done-for-an-active-soil-spec) · [Open](#open-verification-register) · [Evidence](#evidence-ledger) · [History](#change-history)

---

## Purpose

`pipeline_specs/soil/` is the declarative configuration lane for Soil-domain pipelines.

A mature Soil pipeline spec should make a bounded, reviewable statement about:

- the intended pipeline or validation operation;
- the executable consumer that is allowed to interpret the spec;
- admitted source-descriptor references and fixed source roles;
- the Soil support type carried by each input and output;
- lifecycle input and output states;
- temporal scope, source vintage, retrieval basis, and freshness posture;
- required contracts, schemas, validators, policy checks, and evidence closure;
- deterministic run identity, idempotency, retry, quarantine, and no-op behavior;
- receipt, proof, catalog, release, correction, and rollback obligations;
- dry-run and no-network fixture behavior;
- the conditions that require `ABSTAIN`, `DENY`, `HOLD`, or `ERROR`.

A spec does not execute itself. Executable Soil logic belongs under [`pipelines/domains/soil/`](../../pipelines/domains/soil/README.md) or another verified implementation home.

### Primary audience

- Soil domain and pipeline-spec stewards;
- source, rights, evidence, policy, validation, release, and docs reviewers;
- maintainers connecting source descriptors to Soil pipeline implementations;
- test and CI maintainers proving that a spec is parsed, bound, and enforced;
- reviewers deciding whether a YAML file is a placeholder, candidate, active spec, deprecated spec, or retained historical record.

### Non-goals

This README does not:

- activate a source or schedule a run;
- define Soil object meaning or JSON shape;
- create a canonical support-type enum;
- approve rights, operator consent, or source terms;
- implement a parser, pipeline, connector, validator, policy engine, or release gate;
- claim current Soil data, scientific truth, field conditions, farm conditions, parcel conditions, or management advice;
- publish a layer, PMTiles archive, API payload, EvidenceBundle, catalog item, graph projection, dashboard, or AI answer;
- accept the proposed schema-home ADR;
- resolve competing Directory Rules copies, schema compatibility paths, or source-registry topologies.

[Back to top](#top)

---

## Authority boundary

The Soil pipeline-spec lane owns declarative intent only.

| Concern | Owning responsibility | Soil spec relationship |
|---|---|---|
| Declarative pipeline configuration | `pipeline_specs/soil/` | Owns the declared operation, references, gates, and execution posture. |
| Executable pipeline behavior | [`pipelines/domains/soil/`](../../pipelines/domains/soil/README.md) | Consumer implementation; must not be inferred from YAML presence. |
| Source fetching and admission helpers | `connectors/` plus source-registry records | May supply admitted inputs; the spec cannot grant authority. |
| Soil object meaning | [`contracts/domains/soil/`](../../contracts/domains/soil/README.md) | Semantic contract authority, separate from the spec. |
| Machine-checkable Soil shape | [`schemas/contracts/v1/domains/soil/`](../../schemas/contracts/v1/domains/soil/README.md) | Draft machine-shape lane; schema completeness remains unproven. |
| Admissibility, rights, sensitivity, and release obligations | [`policy/domains/soil/`](../../policy/domains/soil/README.md) and cross-cutting policy roots | Policy authority; the spec may require a decision but cannot create it. |
| Test enforceability | [`tests/pipelines/`](../../tests/pipelines/README.md), [`tests/domains/soil/`](../../tests/domains/soil/README.md), and accepted package/connector test homes | Proves bounded behavior; test success is not release. |
| Fixtures | [`fixtures/domains/soil/`](../../fixtures/domains/soil/README.md) or an accepted spec-fixture lane | Deterministic examples; current Soil fixture README remains a greenfield stub. |
| Source identity and activation state | [`data/registry/sources/soil/`](../../data/registry/sources/soil/README.md) or an ADR-selected source-registry lane | Source-control record; topology remains unresolved. |
| Lifecycle data | `data/raw|work|quarantine|processed|catalog|triplets|published/.../soil/` | Actual data and emitted artifacts; never stored beside the spec. |
| Receipts and proofs | `data/receipts/`, `data/proofs/` | Process memory and proof; the spec can require them but is neither. |
| Release, correction, and rollback decisions | `release/` | Governs promotion and public state; a `publish.yaml` placeholder is not release authority. |
| Public delivery | governed APIs and released artifacts | Public clients do not read this spec lane directly. |

> [!WARNING]
> A file named `publish.yaml` is still declarative input. It cannot authorize promotion, write to `PUBLISHED`, bypass review, or become a release manifest.

[Back to top](#top)

---

## Confirmed current state

The following claims are bounded to the evidence snapshot recorded above.

### Safe conclusions

- **CONFIRMED:** this README exists at `pipeline_specs/soil/README.md`.
- **CONFIRMED:** five direct Soil YAML files exist: `ingest.yaml`, `normalize.yaml`, `validate.yaml`, `catalog.yaml`, and `publish.yaml`.
- **CONFIRMED:** each YAML file declares `name`, `version: 1`, and `stages: []`.
- **CONFIRMED:** the checked nested compatibility path `pipeline_specs/domains/soil/README.md` does not exist.
- **CONFIRMED:** exact indexed searches did not establish source-specific Soil spec files such as `ssurgo_ingest.yaml`, `mesonet_normalizer.yaml`, or `moisture_validator.yaml`.
- **CONFIRMED:** Soil executable sublane READMEs exist for SSURGO ingest, Mesonet normalization, and moisture validation, but those READMEs label executable behavior and consumer binding `NEEDS VERIFICATION`.
- **CONFIRMED:** `tests/pipelines/README.md` records the shared pipeline-test lane as README-only and says sampled Soil pipeline specs are minimal scaffolds.
- **CONFIRMED:** `tests/domains/soil/README.md` is a domain test-parent and says executable Soil test coverage remains unverified.
- **CONFIRMED:** `fixtures/domains/soil/README.md` is a greenfield stub.
- **CONFIRMED:** `.github/workflows/domain-soil.yml` contains TODO-only echo jobs.
- **CONFIRMED:** `.github/CODEOWNERS` routes `/pipeline_specs/` review to `@bartytime4life`; that is GitHub routing, not Soil stewardship approval or release authority.
- **UNKNOWN:** exhaustive spec inventory outside indexed and checked paths, accepted parser, active consumers, current run results, deployment, schedules, receipt emission, promotion dependency, and public behavior.

### Maturity matrix

| Surface | Current status | Evidence-bounded conclusion |
|---|---:|---|
| Directory README | `CONFIRMED` | Human boundary and inventory document. |
| Direct YAML payloads | `CONFIRMED: 5` | Placeholder declarations only. |
| Non-empty stages | `NOT ESTABLISHED` | All five specs have empty stage arrays. |
| Canonical Soil spec schema | `NOT ESTABLISHED` | No accepted pipeline-spec schema was identified for these files. |
| Parser and consumer binding | `UNKNOWN` | No indexed binding from the five spec names to an active consumer was established. |
| SourceDescriptor binding | `NOT PRESENT IN DIRECT YAML` | The five files contain no source refs. |
| Support-type binding | `NOT PRESENT IN DIRECT YAML` | The five files contain no support-type field. |
| Lifecycle transition grammar | `NOT PRESENT IN DIRECT YAML` | Stage and state transitions are undeclared. |
| Evidence, policy, review, and receipt gates | `NOT PRESENT IN DIRECT YAML` | No gate declarations exist. |
| Spec-specific fixtures and tests | `NOT ESTABLISHED` | Checked `tests/pipeline_specs/soil/README.md` and `fixtures/pipeline_specs/soil/README.md` are absent. |
| Domain policy enforcement | `SCAFFOLD` | Soil policy README is a greenfield scaffold; rule execution was not established. |
| CI enforcement | `TODO STUB` | Domain workflow only echoes TODO messages. |
| Activation or schedule | `UNKNOWN` | No accepted activation record or schedule was verified. |
| Release integration | `UNKNOWN` | File naming and README promises do not prove release gating. |
| Current public output | `NOT CLAIMED` | No public mutation occurs from this lane. |

[Back to top](#top)

---

## Placement and drift posture

### Why this path is appropriate

The parent [`pipeline_specs/README.md`](../README.md) and the repository contribution guide assign declarative pipeline configuration to `pipeline_specs/`. Soil is a domain segment under that responsibility root, so `pipeline_specs/soil/` fits the responsibility-root model.

This revision does not create, move, rename, or delete a path.

### Directory Rules conflict remains visible

[`CONTRIBUTING.md`](../../CONTRIBUTING.md) identifies a live conflict among Directory Rules artifacts. The newer architecture-side copy is [`docs/architecture/directory-rules.md`](../../docs/architecture/directory-rules.md); a doctrine-side copy also exists at [`docs/doctrine/directory-rules.md`](../../docs/doctrine/directory-rules.md). The architecture-side document treats its own placement as an open ADR-class question.

This README does not select a winner or create a third copy. Both agree on the material rule that:

- `pipeline_specs/` owns declarative pipeline configuration;
- `pipelines/` owns executable pipeline logic;
- domains appear as segments inside responsibility roots;
- lifecycle phases remain separate;
- promotion is a governed state transition.

### Schema compatibility path

The proposed [`ADR-0001`](../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) identifies `schemas/contracts/v1/domains/<domain>/` as the intended domain schema home. The repository also retains [`schemas/contracts/v1/soil/`](../../schemas/contracts/v1/soil/README.md) as a flat compatibility guardrail.

This README points to the populated domain schema lane and does not create parallel schema authority. ADR-0001 remains `proposed`, not accepted.

### Source-registry topology

The Soil source-registry README records both subtype-first and domain-first source-registry paths. Until an ADR or migration record resolves them:

- do not maintain divergent SourceDescriptor instances in both homes;
- do not let a spec choose a source by path alone;
- bind future specs to stable source-descriptor IDs and verified versions;
- treat missing or ambiguous source authority as `HOLD`, `ABSTAIN`, or `DENY`.

### Drift register limit

The current [`DRIFT_REGISTER.md`](../../docs/registers/DRIFT_REGISTER.md) does not record these newer Soil spec and topology details exhaustively. Absence from that short register is not proof that drift is resolved.

[Back to top](#top)

---

## Direct lane inventory

```text
pipeline_specs/soil/
├── README.md       # CONFIRMED — this boundary and inventory
├── ingest.yaml     # CONFIRMED placeholder — name/version/stages:[]
├── normalize.yaml  # CONFIRMED placeholder — name/version/stages:[]
├── validate.yaml   # CONFIRMED placeholder — name/version/stages:[]
├── catalog.yaml    # CONFIRMED placeholder — name/version/stages:[]
└── publish.yaml    # CONFIRMED placeholder — name/version/stages:[]
```

### Payload inventory

| File | Declared name | Version | Stages | Current interpretation |
|---|---|---:|---|---|
| `ingest.yaml` | `soil-ingest` | `1` | `[]` | Placeholder declaration; no source, lifecycle, implementation, or gate binding. |
| `normalize.yaml` | `soil-normalize` | `1` | `[]` | Placeholder declaration; no object-family or support-type transformation contract. |
| `validate.yaml` | `soil-validate` | `1` | `[]` | Placeholder declaration; no validator list, reason codes, or failure policy. |
| `catalog.yaml` | `soil-catalog` | `1` | `[]` | Placeholder declaration; no catalog closure, evidence, proof, or receipt requirements. |
| `publish.yaml` | `soil-publish` | `1` | `[]` | Placeholder declaration; no release decision, review, correction, or rollback binding. |

### Files not established in this lane

The previous README displayed a large proposed file tree. That tree is retained only as historical design pressure, not current inventory.

The following families remain **PROPOSED / NEEDS VERIFICATION** until a real file, schema, consumer, fixture, validator, and owner justify them:

- source-specific specs for SSURGO/SDA, gSSURGO/gNATSGO, SoilGrids, Mesonet, SCAN/AWDB, USCRN, or SMAP;
- pedon/profile, hydrologic-soil-group, erosion, or suitability specs;
- watcher or differential-update specs;
- rollback-specific specs;
- triplet-emission specs;
- support-type-check specs.

Do not create empty placeholder files merely to complete this list.

[Back to top](#top)

---

## Soil support-type boundary

Support-type separation is the Soil-specific invariant.

| Support type | Meaning | Must not masquerade as |
|---|---|---|
| `authoritative_static_soil` | Source-vintage-bound soil survey evidence such as admitted SSURGO/SDA products. | Current condition, station observation, satellite grid, or field truth. |
| `gridded_derivative_soil` | Raster or grid derived from survey, modeled, or harmonized inputs. | Original survey polygons, measured station data, or parcel truth. |
| `station_soil_moisture` | Point-station observations with station, depth, cadence, QA, and time context. | Countywide surface, satellite grid, map-unit property, or owner-specific field fact. |
| `satellite_soil_moisture` | Satellite or assimilated grid product with resolution, product level, uncertainty, and temporal support. | In-situ reading, raw ground observation, or static soil survey. |
| `pedon_evidence` | Profile-level observation, description, sample, or analytical result. | Map-unit-wide condition without a governed derivation. |
| `interpretation` | Erosion, suitability, hydrologic, or other derived interpretation with method and limitations. | Measured property, legal determination, crop/yield truth, hazard authority, or management prescription. |

A future spec must not omit support type when the operation can change meaning, scale, temporal support, or public interpretation.

### Required anti-collapse rules

```text
map unit != component != horizon
survey polygon != current condition
station != grid != county != field != parcel
sensor depth A != sensor depth B
native cadence != aggregated cadence
satellite surface != in-situ observation
interpretation != measurement
validation pass != evidence closure
catalog candidate != release
publish spec != publication authority
generated summary != evidence
```

### Cross-lane constraints

- Agriculture owns crop, yield, production, and agricultural-economy claims.
- Hydrology owns streamflow, groundwater, and observed/regulatory flood distinctions.
- Geology owns lithology, boreholes, stratigraphy, and parent-material geology.
- Habitat, Flora, and Fauna own ecological-system, plant, and animal claims.
- Hazards owns hazard-event and official warning context.
- People/Land lanes own person, title, parcel, and land-assertion semantics.

A Soil spec may reference cross-lane evidence. It must not silently reauthor another lane's canonical truth.

[Back to top](#top)

---

## Minimum future spec contract

No accepted machine schema for the five direct YAML files was established by this review. The following is a **PROPOSED contract**, not a currently executable format.

A future active Soil spec should define or resolve:

| Field family | Minimum obligation |
|---|---|
| Identity | Stable `spec_id`, semantic version, status, owner refs, and content/spec hash. |
| Role | `declarative` role and bounded operation type such as ingest, normalize, validate, catalog-candidate, or publish-readiness. |
| Consumer | Exact implementation or runner identity plus accepted version range. |
| Sources | Stable SourceDescriptor IDs, source roles, versions/vintages, rights state, and activation requirements. |
| Support | Input and output support types, spatial support, scale/resolution, temporal support, and uncertainty posture. |
| Lifecycle | Allowed input states, output candidates, quarantine paths, no-op behavior, and prohibited transitions. |
| Contracts and schemas | Resolvable contract/schema refs; no inline duplicate authority. |
| Gates | Evidence, rights, sensitivity, validation, policy, review, receipt, catalog, release, correction, and rollback prerequisites. |
| Execution | Dry-run default, no-network fixture mode, retry/idempotency rules, resource bounds, and explicit side effects. |
| Outcomes | Finite outcomes and stable reason codes. |
| Observability | Run identity, input/output digests, validator results, receipt refs, and safe logs. |
| Deprecation | Supersession, deactivation, migration, correction, and rollback references. |

### Illustrative non-executable example

```yaml
spec_id: kfm.pipeline_spec.soil.example
version: 0.0.0-proposed
status: proposed
domain: soil
role: declarative

consumer:
  implementation_ref: NEEDS_VERIFICATION
  accepted_versions: []

inputs:
  source_descriptor_refs: []
  support_types: []
  lifecycle_states: []

outputs:
  candidate_states: []
  prohibited_states:
    - published

gates:
  evidence_required: true
  policy_required: true
  review_required: true
  receipt_required: true
  release_manifest_required: true
  rollback_target_required: true

execution:
  dry_run_default: true
  network_default: deny
  idempotency_required: true

outcomes:
  success: candidate_only
  failures:
    - ABSTAIN
    - DENY
    - HOLD
    - ERROR
```

This example intentionally contains unresolved values. It must not be copied into an active file until a schema, parser, consumer, fixtures, tests, policy, and review process exist.

[Back to top](#top)

---

## Source admission, rights, and activation

A Soil spec may reference an admitted source. It cannot admit one.

Before a spec becomes active, every source reference should resolve to a reviewed source-control record that states:

- source identity and source family;
- source role and permitted claim families;
- rights, terms, attribution, redistribution, and access posture;
- source version, vintage, endpoint or snapshot basis, and retrieval method;
- cadence, freshness, effective time, observed time, valid time, and correction behavior;
- spatial support, scale, resolution, and field/parcel/owner sensitivity;
- required transforms, generalization, aggregation, quarantine, and redaction;
- activation state, steward, reviewer, supersession, withdrawal, and rollback refs.

### Candidate proof slice

The attached Soil architecture planning report recommends a first proof slice combining static Kansas SSURGO/SDA evidence with a bounded Kansas Mesonet sample. In this repository, that remains **PROPOSED lineage**, not implementation proof.

Before such a slice is activated, maintainers still need to verify:

- accepted source descriptors and source rights;
- exact SSURGO/SDA snapshot/query identity and query hash;
- Mesonet operator-consent and station-health posture;
- implementation consumers and no-network fixtures;
- support-type, unit, depth, cadence, and source-vintage checks;
- receipt, catalog, release, correction, and rollback wiring.

### Network posture

Default CI and review validation should be no-network and fixture-backed.

Live access, when approved, must be:

- explicit rather than implied by a spec filename;
- source-specific and terms-aware;
- least-privilege and secret-safe;
- rate-limited, bounded, observable, and cancelable;
- unable to promote or publish directly;
- able to quarantine malformed, ambiguous, stale, restricted, or unsupported material.

[Back to top](#top)

---

## Lifecycle and gates

The governing lifecycle remains:

```text
Pre-RAW admission edge
  -> RAW
  -> WORK / QUARANTINE
  -> PROCESSED
  -> CATALOG / TRIPLET
  -> PUBLISHED
```

A spec may declare allowed movement and required gates. It cannot perform promotion merely by naming a later stage.

### Stage obligations

| Stage | Spec may declare | Required blocker examples |
|---|---|---|
| Pre-RAW | SourceDescriptor refs, activation requirement, retrieval mode, source head, expected rights and sensitivity posture. | Missing/ambiguous descriptor, denied source, unresolved rights, unsupported source role. |
| RAW | Immutable input reference, digest, source version/vintage, retrieval receipt requirement. | Mutable or unpinned input, missing provenance, unexpected source family. |
| WORK | Normalization profile, contract/schema refs, support type, temporal model, geometry/unit/depth rules. | Shape failure, lineage failure, support-type collapse, time/scale ambiguity. |
| QUARANTINE | Reason-code vocabulary, retained evidence refs, re-entry conditions, reviewer role. | Missing quarantine reason, silent discard, unsafe retry. |
| PROCESSED | Validation report, output digest, derivation receipt, uncertainty and caveat requirements. | Unresolved evidence, failed validation, unrecorded aggregation or interpolation. |
| CATALOG / TRIPLET | Candidate catalog/graph mappings, EvidenceBundle refs, proof and policy prerequisites. | Catalog before proof/evidence closure, unsupported graph edge, missing correction lineage. |
| PUBLISHED | No direct write. Require separate ReleaseManifest, review, correction path, and rollback target. | Any spec or ordinary workflow attempting to self-promote or publish. |

### Required gates for an active spec

1. **Identity gate** — stable spec ID, version, digest, owner refs, and supersession state.
2. **Consumer gate** — exact parser/runner and implementation version are known.
3. **Source gate** — every source ref resolves to a reviewed descriptor and permitted role.
4. **Support gate** — input and output support types are explicit and compatible.
5. **Temporal gate** — source, observed, valid, retrieval, release, and correction times remain distinct where material.
6. **Contract/schema gate** — refs resolve and candidate data validates.
7. **Lineage gate** — identifiers such as MUKEY/COKEY/CHKEY and derivation ancestry remain inspectable where applicable.
8. **Evidence gate** — consequential output can resolve EvidenceRef to EvidenceBundle or abstains.
9. **Rights/sensitivity gate** — source terms, scale, field/parcel/owner detail, and exact operational context are allowed.
10. **Validation gate** — domain and cross-lane checks pass with stable reason codes.
11. **Receipt gate** — run and transform receipts are emitted through accepted tooling.
12. **Catalog gate** — catalog/triplet candidates derive from validated evidence and receipts.
13. **Review/release gate** — independent review and release decision exist where required.
14. **Correction/rollback gate** — correction propagation and rollback target are defined.

[Back to top](#top)

---

## Finite outcomes and reason codes

A Soil spec or validator should fail closed.

| Outcome | Use |
|---|---|
| `PASS` | The scoped spec or validation check passed. Does not imply evidence closure or release. |
| `ABSTAIN` | Evidence, temporal support, source role, scale, or claim support is insufficient. |
| `DENY` | Rights, sensitivity, policy, source terms, or prohibited transition blocks the operation. |
| `HOLD` | Review, source activation, schema decision, correction, or another resolvable prerequisite is pending. |
| `ERROR` | Parser, consumer, validator, storage, receipt, or other operation failed. |
| `NO_OP` | Inputs are unchanged and the deterministic operation has no authorized delta. |

Reason codes should be stable, reviewable, and safe to expose. Candidate families include:

```text
SPEC_SCHEMA_MISSING
SPEC_CONSUMER_UNRESOLVED
SOURCE_DESCRIPTOR_MISSING
SOURCE_ROLE_MISMATCH
RIGHTS_UNRESOLVED
SUPPORT_TYPE_MISSING
SUPPORT_TYPE_COLLAPSE
TEMPORAL_SCOPE_MISSING
SOURCE_VINTAGE_MISSING
LINEAGE_MISSING
UNIT_OR_DEPTH_INVALID
EVIDENCE_UNRESOLVED
POLICY_DENY
VALIDATION_FAILED
RECEIPT_MISSING
CATALOG_CLOSURE_MISSING
REVIEW_PENDING
RELEASE_MANIFEST_MISSING
ROLLBACK_TARGET_MISSING
```

The final vocabulary requires contract, schema, policy, validator, test, and steward alignment.

[Back to top](#top)

---

## Sensitivity, scale, and public safety

Most general soil-survey data may be low sensitivity, but derived joins and operational detail can raise risk.

A future spec must fail closed for:

- private-land, parcel, owner, farm, field, or operation-specific joins without a reviewed purpose and policy;
- restricted source terms, operator-consent gaps, private-network station data, or non-public endpoints;
- false precision that turns a survey unit, grid cell, or station into a field-specific claim;
- current operational sensor details that create security, privacy, or contractual concerns;
- conservation-practice, compliance, eligibility, appraisal, lending, insurance, legal, or regulatory conclusions not supported for that use;
- crop-management, irrigation, fertilizer, pesticide, engineering, or safety prescriptions presented as authoritative;
- rare-species, rare-plant, archaeology, cultural, critical-infrastructure, or living-person joins that inherit stricter cross-lane controls;
- public artifacts that omit source role, support type, time caveat, uncertainty, evidence, release state, correction state, or generalization receipt.

### Public-safe transformation

Generalization, aggregation, interpolation, field suppression, station suppression, or redaction must become explicit derived operations with:

- input and output scope;
- method and parameters;
- evidence and source refs;
- transform receipt;
- policy decision;
- validation result;
- review state;
- correction and rollback implications.

A spec cannot silently convert precision into safety.

[Back to top](#top)

---

## Evidence, receipts, catalog, and release

### Evidence

A spec may require EvidenceRef resolution. It is not an EvidenceBundle and does not create factual support.

### Receipts

An active run should emit accepted process-memory records such as:

- retrieval or admission receipt;
- run receipt;
- normalization/transform receipt;
- aggregation/interpolation/generalization receipt;
- validation report or receipt;
- catalog-emission receipt;
- correction or rollback execution receipt where applicable.

Receipts do not become proof, policy approval, release approval, or publication authority.

### Catalog and triplets

`catalog.yaml` may eventually declare catalog-candidate obligations. It must not:

- author catalog records before evidence, proof, policy, and receipt closure;
- turn graph relations into sovereign truth;
- hide support type, uncertainty, temporal scope, correction state, or source role;
- bypass catalog integrity validation.

### Publish readiness

`publish.yaml` may eventually declare release-readiness checks. It must never:

- write to a public artifact home by itself;
- create its own PolicyDecision, ReviewRecord, or ReleaseManifest;
- treat a successful workflow, merge, or spec validation as promotion;
- omit correction, withdrawal, supersession, or rollback handling.

Public clients remain downstream of governed APIs and released artifacts.

[Back to top](#top)

---

## Validation and enforceability

### Current limitations

- No accepted schema for the five direct Soil YAML files was established.
- The five files have empty stages and no governance fields.
- No checked `tests/pipeline_specs/soil/README.md` or `fixtures/pipeline_specs/soil/README.md` exists.
- The shared [`tests/pipelines/`](../../tests/pipelines/README.md) lane is a documented boundary, not an established executable suite.
- The Soil domain test README is a backlog parent; executable child coverage remains unverified.
- The Soil fixture README is a greenfield stub.
- The domain workflow is TODO-only.
- No current run, coverage report, parser-consumer contract test, or promotion dependency was inspected.

Therefore the current Soil YAML files should be treated as **scaffolds**, not active, validated, or release-bearing specs.

### Minimum future validation suite

An active Soil spec should have deterministic, no-network tests for:

- YAML parse and schema conformance;
- stable spec identity and content hashing;
- consumer binding and version compatibility;
- source-descriptor resolution and source-role preservation;
- rights, operator-consent, and sensitivity failures;
- support-type presence and no-collapse behavior;
- lifecycle transition allow/deny matrix;
- MUKEY/COKEY/CHKEY and component-horizon lineage where applicable;
- units, depth, cadence, timezone, quality flags, uncertainty, and freshness;
- static survey versus grid versus station versus satellite versus pedon versus interpretation distinctions;
- quarantine, retry, idempotency, replay, and no-op behavior;
- evidence resolution and citation requirements;
- receipt generation and digest verification;
- catalog/triplet candidate closure;
- publish-readiness denial without review, release manifest, correction path, and rollback target;
- no direct writes to `PUBLISHED`;
- no live network access in default CI;
- logs and diagnostics free of secrets and restricted payloads.

### Workflow posture

[`domain-soil.yml`](../../.github/workflows/domain-soil.yml) runs on pull requests and pushes to `main`, but all three jobs only echo TODO messages. It uses a mutable major action tag and has no explicit permissions block.

The repository-wide [`CodeQL workflow`](../../.github/workflows/codeql.yml) uses `pull_request`, not `pull_request_target`, and declares read-oriented permissions plus `security-events: write` for result upload. Its actions also use mutable major tags rather than immutable commit SHAs.

No workflow result is reported as passing by this README.

### Documentation checks

For changes to this README:

1. preserve one H1 and unique heading anchors;
2. keep the KFM Meta Block parseable;
3. validate repository-relative links;
4. keep code fences balanced;
5. run whitespace and final-newline checks;
6. verify the remote changed-path set;
7. add a generated-work receipt for substantive AI-authored changes;
8. keep repository-native execution truthfully `NOT RUN` or `SKIPPED` when the repository is not checked out.

[Back to top](#top)

---

## Review and change discipline

### Required review roles

Owners are not yet assigned as verified repository identities. Material changes should identify, at minimum:

- pipeline-spec steward;
- Soil domain steward;
- affected source steward;
- contract/schema and validation steward;
- evidence/receipt steward;
- policy/rights/sensitivity steward;
- release steward when release-readiness semantics change;
- docs steward.

[`CODEOWNERS`](../../.github/CODEOWNERS) currently routes this path to `@bartytime4life`. That routing does not prove the required domain, policy, evidence, or release review occurred.

### Change classes

| Change | Minimum consequence |
|---|---|
| README clarification only | Documentation review, link/structure checks, generated receipt when AI-authored. |
| Populate an empty `stages` array | Schema/consumer/fixture/test review; no activation by merge alone. |
| Add a source ref | Source descriptor, rights, source-role, citation, and activation review. |
| Add or change support type | Contract/schema/policy/test alignment. |
| Add network or schedule behavior | Security, terms, secrets, rate-limit, observability, kill-switch, and no-network CI review. |
| Add catalog or publish-readiness behavior | Evidence, receipt, policy, review, release, correction, and rollback review. |
| Rename or move a spec | Consumer inventory, migration note, deprecation window, redirect/alias decision, and rollback. |
| Change a canonical root or parallel authority | ADR and migration plan before implementation. |

### Versioning

- Increment the spec version for a material semantic change.
- Do not reuse a version number for different content.
- Preserve superseded specs when audit or replay requires them.
- Record consumer compatibility and migration posture.
- Distinguish `proposed`, `candidate`, `active`, `deprecated`, `superseded`, `disabled`, and `retired`.
- A Git merge changes repository state; it does not automatically change activation or release state.

[Back to top](#top)

---

## Deactivation, correction, and rollback

### Documentation rollback

Rollback for this README is ordinary Git rollback:

- close the draft pull request before merge; or
- revert the documentation commit after merge.

No data, runtime, source, release, or public state is mutated by this documentation-only revision.

### Future spec deactivation

An active spec should be disabled through an explicit control record, not by silent deletion.

A deactivation record should preserve:

- spec ID and version;
- reason and effective time;
- affected consumers and schedules;
- last successful and failed runs;
- source, evidence, receipt, catalog, release, and public artifact refs;
- correction or withdrawal obligations;
- rollback target;
- reviewer and decision state.

### Correction propagation

A corrected or superseded source, schema, policy, implementation, or spec may invalidate downstream candidates and released derivatives. The system should be able to identify affected:

- processed records;
- EvidenceBundles;
- catalog/triplet records;
- layers, PMTiles, API payloads, screenshots, and exports;
- Focus Mode or generated summaries;
- release manifests;
- correction notices and rollback cards.

This README does not prove that dependency or invalidation machinery exists.

[Back to top](#top)

---

## Definition of done for an active Soil spec

A Soil YAML file is not active merely because it exists or has non-empty stages.

An active spec should satisfy all applicable items:

- [ ] Stable spec ID, version, status, owner refs, and digest.
- [ ] Accepted machine schema and parser.
- [ ] Verified consumer implementation and compatible version.
- [ ] Resolvable SourceDescriptor refs and activation records.
- [ ] Explicit source roles, support types, spatial/temporal support, and uncertainty.
- [ ] Allowed lifecycle transitions and prohibited public writes.
- [ ] Contract and schema refs resolve.
- [ ] Rights, sensitivity, field/parcel/owner, and scale policy decisions are enforced.
- [ ] Deterministic no-network valid, invalid, denied, held, and error fixtures exist.
- [ ] Spec-to-consumer agreement tests pass.
- [ ] Idempotency, replay, retry, quarantine, and no-op behavior are tested.
- [ ] Evidence and citation requirements are testable.
- [ ] Receipts and output digests are emitted and validated.
- [ ] Catalog/triplet candidates preserve source role, support type, time, and correction lineage.
- [ ] Publish-readiness cannot bypass review, ReleaseManifest, correction path, or rollback target.
- [ ] CI invokes real repository-owned checks and fails closed.
- [ ] Branch-protection and required-check dependencies are verified where relied upon.
- [ ] Activation, deactivation, supersession, correction, and rollback are documented.
- [ ] Human review is recorded separately from generation, validation, merge, release, and publication.

Until then, label the file `PROPOSED`, `SCAFFOLD`, or `NEEDS VERIFICATION`.

[Back to top](#top)

---

## Open verification register

| Item | Status | Evidence needed |
|---|---|---|
| Accepted Soil pipeline-spec schema | `UNKNOWN` | Accepted schema/ADR plus parser and fixtures. |
| Exhaustive direct Soil spec inventory | `NEEDS VERIFICATION` | Recursive tree at a pinned commit. |
| Parser for the five YAML files | `UNKNOWN` | Executable parser entrypoint and tests. |
| Consumer binding for `soil-ingest`, `soil-normalize`, `soil-validate`, `soil-catalog`, and `soil-publish` | `UNKNOWN` | Registry or code binding plus agreement tests. |
| Meaning of `version: 1` | `UNKNOWN` | Versioning contract and compatibility policy. |
| Accepted support-type vocabulary | `NEEDS VERIFICATION` | Contract/schema/policy/test alignment. |
| SourceDescriptor instances and activation state | `NEEDS VERIFICATION` | Canonical registry inventory and reviewed records. |
| Soil source-registry canonical topology | `NEEDS VERIFICATION` | ADR or migration note reconciling subtype-first/domain-first lanes. |
| Soil schema canonical/compatibility topology | `NEEDS VERIFICATION` | Accepted ADR and migration inventory. |
| Soil policy implementation | `NEEDS VERIFICATION` | Rego or accepted policy files, fixtures, tests, and run results. |
| Spec-specific fixtures and tests | `NOT ESTABLISHED` | Concrete fixture/test files and current pass results. |
| No-network enforcement | `NEEDS VERIFICATION` | Test harness and workflow evidence. |
| Field/parcel/owner-specific deny/default behavior | `NEEDS VERIFICATION` | Policy, negative fixtures, and review record. |
| Workflow token defaults and branch protection | `UNKNOWN` | Repository settings evidence. |
| Recent Soil workflow results | `UNKNOWN` | Current run IDs, logs, and conclusions. |
| Receipt emission and proof closure | `UNKNOWN` | Emitted records validated against accepted schemas. |
| Catalog and release dependency | `UNKNOWN` | Workflow/registry/manifest evidence. |
| Correction, withdrawal, and rollback execution | `UNKNOWN` | Tested dependency graph, runbooks, records, and drill results. |
| Named responsible owners and separation of duties | `NEEDS VERIFICATION` | Verified assignments and review records. |

[Back to top](#top)

---

## Evidence ledger

| Evidence | Observation supported | Status |
|---|---|---:|
| [`pipeline_specs/README.md`](../README.md) | `pipeline_specs/` owns declarative configuration and remains separate from executable pipelines and publication. | `CONFIRMED` |
| `pipeline_specs/soil/{ingest,normalize,validate,catalog,publish}.yaml` | Five direct YAML files exist and each has `stages: []`. | `CONFIRMED` |
| [`pipelines/domains/soil/README.md`](../../pipelines/domains/soil/README.md) | Soil executable lane is separate and labels concrete behavior unverified. | `CONFIRMED documentation boundary` |
| [`ssurgo_ingest/README.md`](../../pipelines/domains/soil/ssurgo_ingest/README.md) | SSURGO executable sublane is README-backed; its proposed spec path is not current direct inventory. | `CONFIRMED README / behavior NEEDS VERIFICATION` |
| [`mesonet_normalizer/README.md`](../../pipelines/domains/soil/mesonet_normalizer/README.md) | Mesonet normalization boundary preserves station/depth/cadence/rights distinctions. | `CONFIRMED README / behavior NEEDS VERIFICATION` |
| [`moisture_validator/README.md`](../../pipelines/domains/soil/moisture_validator/README.md) | Moisture validation boundary preserves source role and support type; validation is not promotion. | `CONFIRMED README / behavior NEEDS VERIFICATION` |
| [`contracts/domains/soil/README.md`](../../contracts/domains/soil/README.md) | Soil semantic-contract lane exists and is separate from schemas and specs. | `CONFIRMED path / maturity mixed` |
| [`schemas/contracts/v1/domains/soil/README.md`](../../schemas/contracts/v1/domains/soil/README.md) | Populated Soil schema index exists; opened examples remain permissive scaffolds. | `CONFIRMED path / NEEDS VERIFICATION maturity` |
| [`schemas/contracts/v1/soil/README.md`](../../schemas/contracts/v1/soil/README.md) | Flat Soil schema path is a compatibility guardrail, not parallel authority. | `CONFIRMED compatibility index` |
| [`policy/domains/soil/README.md`](../../policy/domains/soil/README.md) | Soil policy lane is a short greenfield scaffold. | `CONFIRMED scaffold` |
| [`tests/pipelines/README.md`](../../tests/pipelines/README.md) | Dedicated pipeline suite not established; sampled Soil spec is an empty-stage scaffold. | `CONFIRMED documentation inventory` |
| [`tests/domains/soil/README.md`](../../tests/domains/soil/README.md) | Soil domain test-parent exists; executable child coverage is unverified. | `CONFIRMED README / NEEDS VERIFICATION coverage` |
| [`fixtures/domains/soil/README.md`](../../fixtures/domains/soil/README.md) | Soil fixture lane remains a greenfield stub. | `CONFIRMED stub` |
| [`data/registry/sources/soil/README.md`](../../data/registry/sources/soil/README.md) | Source-registry lane exists; subtype-first/domain-first topology remains unresolved. | `CONFIRMED path / NEEDS VERIFICATION topology` |
| [`docs/domains/soil/CANONICAL_PATHS.md`](../../docs/domains/soil/CANONICAL_PATHS.md) | Soil belongs as a segment under responsibility roots; path guidance retains historical variances. | `CONFIRMED document / draft` |
| [`docs/architecture/directory-rules.md`](../../docs/architecture/directory-rules.md) and [`docs/doctrine/directory-rules.md`](../../docs/doctrine/directory-rules.md) | Placement doctrine copies coexist; architecture-side placement records the conflict as open. | `CONFIRMED files / unresolved authority placement` |
| [`ADR-0001`](../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) | Intended schema-home split is documented but ADR status is proposed. | `CONFIRMED proposed ADR` |
| [`domain-soil.yml`](../../.github/workflows/domain-soil.yml) | Soil workflow is TODO-only and does not enforce its advertised jobs. | `CONFIRMED stub` |
| [`codeql.yml`](../../.github/workflows/codeql.yml) | CodeQL uses `pull_request`, explicit permissions, GitHub-hosted runners, and mutable major action refs. | `CONFIRMED workflow content` |
| [`.github/CODEOWNERS`](../../.github/CODEOWNERS) | `/pipeline_specs/` review routes to `@bartytime4life`; enforcement and role separation remain unverified. | `CONFIRMED routing file` |
| [`data/receipts/generated/README.md`](../../data/receipts/generated/README.md) | AI-authored work requires inspectable process provenance; receipt is not approval or release. | `CONFIRMED lane contract` |

### Evidence limits

- Repository search is bounded and index-dependent.
- Checked-path absence is not a full-history or all-branch absence claim.
- README and schema-index statements may lag later files.
- No repository clone, recursive tree command, local test run, workflow run log, branch-protection setting, deployed runtime, or source system was inspected by this documentation update.
- Attached architecture reports are planning and lineage inputs; current repository files outrank them for implementation claims.

[Back to top](#top)

---

## Change history

### v0.2 — 2026-07-18

- replaced the v0.1 planning-heavy current-state narrative with a pinned repository inventory;
- confirmed five direct Soil YAML scaffolds and recorded their empty-stage contents;
- removed the speculative file tree as an implied current repository plan;
- distinguished placeholder file presence from schema, parser, consumer, source, schedule, test, receipt, release, and runtime activation;
- strengthened Soil support-type, source-role, lifecycle, rights, sensitivity, evidence, correction, and rollback boundaries;
- surfaced Directory Rules, schema compatibility, and source-registry topology conflicts without resolving them;
- added finite outcomes, reason-code guidance, active-spec definition of done, validation burden, and evidence ledger;
- changed documentation only.

### v0.1 — 2026-06-13

- established the initial Soil pipeline-spec planning contract;
- documented declarative-versus-executable separation, support-type anti-collapse, lifecycle, gates, and proposed file families;
- did not verify the direct YAML inventory or current enforcement state.

[Back to top](#top)
