<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-hydrology-readme
title: pipeline_specs/hydrology/ — Governed Hydrology Pipeline Specification Boundary
type: readme
version: v0.2
status: draft; repository-grounded; scaffold-only; no-active-specification-established
owners: OWNER_TBD — Pipeline-spec steward · Hydrology domain steward · Hydrology pipeline owner · Source steward · Temporal/freshness steward · Geometry/topology steward · Evidence steward · Rights reviewer · Sensitivity reviewer · Policy steward · Validation steward · Release steward · CI steward · Migration steward · Docs steward
created: 2026-06-13
updated: 2026-07-15
supersedes: v0.1
policy_label: public-doctrine; pipeline-specs; hydrology; declarative-only; source-role-aware; time-aware; topology-aware; regulatory-context-separated; not-emergency-warning; no-secrets; no-live-activation; no-public-path; no-publication; release-gated
current_path: pipeline_specs/hydrology/README.md
truth_posture: CONFIRMED current target, pipeline_specs root contract, Hydrology domain and executable-pipeline documentation, current README plus five six-line YAML scaffold files, empty stages arrays, absent checked triplets/rollback/watchers and first-wave object-profile paths, TODO-only domain-hydrology workflow, and missing checked pipeline-spec test paths / PROPOSED minimum active-spec contract, finite state model, deterministic consumer binding, descriptor and source-role gates, temporal/freshness semantics, topology and identity requirements, receipt vocabulary, failure outcomes, validation matrix, migration discipline, and rollback requirements / UNKNOWN canonical pipeline-spec schema, parser, registry, loader, scheduler, approved source descriptors, executable consumer binding, active profiles, substantive tests, fixture corpus, validator wiring, receipt emission, CI enforcement, release integration, and production use / NEEDS VERIFICATION owners, exhaustive recursive lane inventory, path and slug conventions, schema and contract homes, source activation, rights and sensitivity policy, freshness budgets, hydrologic identity rules, topology checks, NFHL regulatory-context enforcement, current workflow behavior, correction propagation, deactivation, and rollback execution
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 3214733b6916377277c6b85fec4d19d9234ff1e9
  prior_blob: b554a168c176acc71ca6f10f81e253630c61532f
  authoring_prompt_sha256: b061d3d8b153af8083cd1f62f447b389c396b5a882e590328ede7c3e3ff25e85
  direct_lane_files_confirmed:
    - pipeline_specs/hydrology/README.md
    - pipeline_specs/hydrology/ingest.yaml
    - pipeline_specs/hydrology/normalize.yaml
    - pipeline_specs/hydrology/validate.yaml
    - pipeline_specs/hydrology/catalog.yaml
    - pipeline_specs/hydrology/publish.yaml
  checked_absent_paths:
    - pipeline_specs/hydrology/triplets.yaml
    - pipeline_specs/hydrology/rollback.yaml
    - pipeline_specs/hydrology/watchers.yaml
    - pipeline_specs/hydrology/watersheds_huc.yaml
    - tests/pipeline_specs/hydrology/README.md
    - tests/pipeline_specs/hydrology/test_spec_shape.py
  workflow_posture: .github/workflows/domain-hydrology.yml exists as TODO-only echo scaffolding
related:
  - ../README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/doctrine/lifecycle-law.md
  - ../../docs/doctrine/trust-membrane.md
  - ../../docs/domains/hydrology/README.md
  - ../../docs/domains/hydrology/DATA_LIFECYCLE.md
  - ../../docs/domains/hydrology/PUBLICATION_POSTURE.md
  - ../../pipelines/README.md
  - ../../pipelines/domains/hydrology/README.md
  - ./ingest.yaml
  - ./normalize.yaml
  - ./validate.yaml
  - ./catalog.yaml
  - ./publish.yaml
  - ../../data/registry/sources/hydrology/
  - ../../contracts/domains/hydrology/
  - ../../schemas/contracts/v1/domains/hydrology/
  - ../../policy/domains/hydrology/
  - ../../tests/pipeline_specs/hydrology/
  - ../../fixtures/pipeline_specs/hydrology/
  - ../../data/receipts/pipeline/hydrology/
  - ../../data/proofs/evidence_bundle/
  - ../../release/candidates/hydrology/
  - ../../release/manifests/hydrology/
  - ../../.github/workflows/domain-hydrology.yml
notes:
  - "v0.2 applies the KFM GitHub Repository Documentation Implementation Agent v3.1 pipeline-spec README profile."
  - "The direct lane is not README-only: five YAML files exist, but each is a six-line scaffold with an empty stages array and no verified parser, source binding, gates, fixtures, receipts, or consumer."
  - "File presence, YAML syntax, workflow success, or a non-empty schedule must never be treated as source admission, freshness proof, evidence closure, policy approval, release approval, or publication."
  - "NFHL and comparable regulatory flood-hazard context must remain distinct from observed inundation, modeled flood extent, forecast products, and official warnings."
  - "This revision changes documentation only. It does not activate, rewrite, or validate the five YAML scaffold files."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed Hydrology Pipeline Specification Boundary

`pipeline_specs/hydrology/`

> Declarative run-intent boundary for Hydrology pipelines. A file here may state **what** a verified Hydrology pipeline should run, against which admitted sources, under which temporal, identity, topology, evidence, policy, receipt, and release gates. It does not execute a pipeline, admit a source, prove freshness, issue a flood warning, close an `EvidenceBundle`, or authorize publication.

![status](https://img.shields.io/badge/status-draft-blue)
![version](https://img.shields.io/badge/version-v0.2-informational)
![authority](https://img.shields.io/badge/authority-declarative__spec-green)
![inventory](https://img.shields.io/badge/inventory-5__inert__YAML__stubs-lightgrey)
![source role](https://img.shields.io/badge/source__roles-separated-0b7285)
![NFHL](https://img.shields.io/badge/NFHL-regulatory__context__only-critical)
![alerting](https://img.shields.io/badge/alerting-official__issuer__only-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-0b7285)

**Quick links:** [Purpose](#purpose) · [Authority](#authority-and-anti-collapse) · [Status](#current-status) · [Inventory](#current-inspected-inventory) · [Placement](#repository-fit) · [Scope](#hydrology-specification-scope) · [File contract](#minimum-active-specification-contract) · [State model](#specification-state-and-activation-model) · [Sources](#source-descriptors-roles-rights-and-activation) · [Time](#temporal-freshness-and-stale-state) · [Identity](#hydrologic-identity-geometry-and-topology) · [Flood boundary](#regulatory-flood-context-and-life-safety-boundary) · [Lifecycle](#lifecycle-gates-and-finite-outcomes) · [Stage profiles](#stage-profile-contracts) · [Watchers](#watchers-dry-runs-and-no-op-discipline) · [Receipts](#receipts-evidence-and-emitted-artifacts) · [Security](#security-secrets-and-network-posture) · [Validation](#validation-and-enforceability) · [Review](#review-migration-and-change-discipline) · [Rollback](#correction-deactivation-and-rollback) · [Directory map](#directory-map) · [Done](#definition-of-done) · [Backlog](#open-verification-register) · [Evidence](#evidence-ledger)

> [!IMPORTANT]
> **Evidence snapshot:** `main@3214733b6916377277c6b85fec4d19d9234ff1e9`
> **Target blob before this revision:** `b554a168c176acc71ca6f10f81e253630c61532f`
> **Confirmed direct-lane files:** this README plus `ingest.yaml`, `normalize.yaml`, `validate.yaml`, `catalog.yaml`, and `publish.yaml`
> **Confirmed YAML maturity:** each inspected YAML file contains only `name`, `version: 1`, and `stages: []` beneath a comment
> **Activation:** path, filename, merge, YAML syntax, workflow completion, or a future schedule activates nothing

> [!CAUTION]
> A Hydrology pipeline spec is not an emergency-warning product. A gauge record is not an official warning. NFHL is regulatory flood-hazard context, not observed inundation. A modeled hydrograph is not an observation. A schedule is not freshness proof. A successful run is not an `EvidenceBundle`, `PolicyDecision`, `ReleaseManifest`, or public release.

---

## Purpose

`pipeline_specs/hydrology/` is the Hydrology segment under the `pipeline_specs/` responsibility root.

Its safe role is to hold reviewed, deterministic declarative profiles that bind:

- a stable specification identity, version, owner, and finite status;
- one verified executable consumer under `pipelines/`;
- admitted `SourceDescriptor` references and explicit source roles;
- source rights, attribution, sensitivity, and allowed-use requirements;
- observation, issue, valid, retrieval, processing, source-vintage, release, and correction times where applicable;
- cadence, freshness budget, outage behavior, stale-state behavior, and no-op rules;
- hydrologic identity, coordinate reference, geometry, topology, scale, and spatial-support constraints;
- lifecycle input and output states;
- source-role, NFHL, model-versus-observation, and warning-boundary anti-collapse gates;
- schema, contract, policy, evidence, review, receipt, catalog, and release requirements;
- no-network fixtures and expected finite failure outcomes;
- correction, supersession, withdrawal, deactivation, and rollback behavior.

A spec may **require** these controls. It cannot satisfy them merely by naming them.

### Audience

- pipeline-spec and Hydrology maintainers;
- watershed, hydrography, gauge, groundwater, water-quality, flood-context, terrain, and topology stewards;
- source, rights, sensitivity, temporal, evidence, policy, validation, Hazards, release, and docs reviewers;
- maintainers implementing a future pipeline-spec parser, registry, loader, scheduler, or consumer;
- reviewers ensuring that public Hydrology outputs remain source-role-aware, time-aware, non-alerting, evidence-bound, and reversible.

[Back to top](#top)

---

## Authority and anti-collapse

### Responsibility split

```text
pipeline_specs/  = declarative run intent: WHAT may run and under which gates
pipelines/       = executable behavior: HOW processing occurs
connectors/      = source fetch and admission support; never publication
configs/         = safe-to-commit consumer settings; never secrets or activation authority
data/            = lifecycle state, registries, receipts, proofs, catalog/triplets, and published artifacts
contracts/       = semantic meaning
schemas/         = machine-checkable shape
policy/          = admissibility and obligations
tests/fixtures/  = enforceability proof and controlled examples
release/         = release, correction, supersession, withdrawal, and rollback authority
apps/            = governed serving surfaces; never direct reads from specs or internal stores
```

Directory Rules assign declarative configuration to `pipeline_specs/` and executable pipeline behavior to `pipelines/`. Hydrology is a domain segment within those responsibility roots, not a new root.

### What this README may decide

This README may define the maintenance boundary for the Hydrology pipeline-spec lane:

- what belongs here;
- what must remain under another responsibility root;
- what a future active Hydrology specification must contain;
- which source-role, temporal, topology, flood-context, evidence, policy, and failure boundaries must be preserved;
- what repository evidence is currently verified;
- what remains `UNKNOWN` or `NEEDS VERIFICATION`;
- how a documentation-only change is validated and rolled back.

### What this README cannot decide

This README cannot:

- admit, activate, suspend, retire, or supersede a source;
- define Hydrology object meaning, machine schema, policy, rights, sensitivity, or release authority;
- establish a canonical pipeline-spec schema by assertion;
- implement or activate a parser, registry, loader, schedule, connector, pipeline, validator, or public route;
- convert a source list into source authority;
- make stale material current or provisional material final;
- convert NFHL into observed inundation;
- convert a model, forecast, reconstruction, aggregate, or generated summary into an observation;
- issue watches, warnings, evacuation directions, protective instructions, or life-safety guidance;
- create an `EvidenceBundle`, close a proof, issue a `PolicyDecision`, approve a release, or publish an artifact;
- authorize a normal UI, map, tile, export, search, graph, screenshot, embedding, automation, or AI path.

### Disallowed collapses

```text
README or path existence          -> active specification
YAML file presence                -> active specification
non-empty stages                  -> approved execution plan
valid YAML                        -> valid governed specification
spec validation                   -> data validation
source reference                  -> admitted or active source
source list                       -> source authority
schedule                          -> source freshness proof
successful source fetch           -> source correctness
successful pipeline run           -> EvidenceBundle
successful pipeline run           -> release approval
gauge reading                     -> official warning
NFHL zone                         -> observed inundation
modeled hydrograph                -> observed gauge value
forecast or warning context       -> KFM-issued warning
catalog record                    -> publication
receipt                           -> proof
proof                             -> release decision
publish profile                   -> PUBLISHED state
generated summary                 -> evidence or official guidance
```

[Back to top](#top)

---

## Current status

### Safe conclusion

`pipeline_specs/hydrology/` is a repository-present declarative lane containing a substantial README and five inert YAML scaffolds. No active, parser-bound, consumer-bound, source-bound, scheduled, fixture-proven, receipt-emitting, release-linked Hydrology specification was established by the bounded inspection.

### Maturity matrix

| Capability or artifact | Status | Evidence-bounded conclusion |
|---|---:|---|
| Requested README | `CONFIRMED` | `pipeline_specs/hydrology/README.md` exists and was v0.1 before this revision. |
| `ingest.yaml` | `CONFIRMED SCAFFOLD` | Six lines; `name: hydrology-ingest`, `version: 1`, `stages: []`. |
| `normalize.yaml` | `CONFIRMED SCAFFOLD` | Six lines; `name: hydrology-normalize`, `version: 1`, `stages: []`. |
| `validate.yaml` | `CONFIRMED SCAFFOLD` | Six lines; `name: hydrology-validate`, `version: 1`, `stages: []`. |
| `catalog.yaml` | `CONFIRMED SCAFFOLD` | Six lines; `name: hydrology-catalog`, `version: 1`, `stages: []`. |
| `publish.yaml` | `CONFIRMED SCAFFOLD` | Six lines; `name: hydrology-publish`, `version: 1`, `stages: []`. |
| Checked `triplets.yaml`, `rollback.yaml`, `watchers.yaml`, `watersheds_huc.yaml` | `ABSENT AT CHECKED PATHS` | No file was returned at the inspected commit. This is a bounded path check, not a recursive inventory. |
| Canonical pipeline-spec schema | `UNKNOWN` | No accepted schema was established by the inspected evidence. |
| Parser, registry, loader, or scheduler | `UNKNOWN` | No consumer binding was established. |
| Active `SourceDescriptor` set | `UNKNOWN` | Source-registry paths are referenced, but activation was not proven. |
| Hydrology implementation lane | `DOCUMENTED / EXECUTION UNKNOWN` | `pipelines/domains/hydrology/README.md` exists; executable behavior remains unverified. |
| Domain workflow | `CONFIRMED TODO SCAFFOLD` | `.github/workflows/domain-hydrology.yml` checks out the repo and echoes TODO commands. |
| Hydrology pipeline-spec test README | `ABSENT AT CHECKED PATH` | `tests/pipeline_specs/hydrology/README.md` was not found. |
| Proposed `test_spec_shape.py` | `ABSENT AT CHECKED PATH` | The file proposed in v0.1 was not found. |
| Receipt instances and proof closure | `UNKNOWN` | Documentation points to homes; emitted instances were not established. |
| Public release integration | `UNKNOWN / DENY BY DEFAULT` | No release binding was proven. |

### Current scaffold interpretation

The five YAML files are **inventory scaffolds**, not active specs. Their current `stages: []` values establish no pipeline graph, no source scope, no lifecycle transition, no evidence requirements, no finite failure behavior, and no release authority.

A future change that populates a stage array is a material behavior proposal. It requires schema validation, consumer binding, fixtures, tests, source and rights review, evidence and receipt contracts, policy checks, and rollback planning before activation.

[Back to top](#top)

---

## Current inspected inventory

| Path | Confirmed content | Current posture | Required before activation |
|---|---|---|---|
| `README.md` | Lane boundary and proposed contract | Documentation only | Keep synchronized with behavior and evidence. |
| `ingest.yaml` | `hydrology-ingest`, version `1`, empty stages | Inert scaffold | Descriptor refs, admission prerequisites, consumer, outcomes, fixtures, receipts. |
| `normalize.yaml` | `hydrology-normalize`, version `1`, empty stages | Inert scaffold | Input contract, transforms, identity/time rules, quarantine behavior, transform receipts. |
| `validate.yaml` | `hydrology-validate`, version `1`, empty stages | Inert scaffold | Schema, policy, source-role, NFHL, temporal, geometry/topology, negative fixtures. |
| `catalog.yaml` | `hydrology-catalog`, version `1`, empty stages | Inert scaffold | Evidence closure, catalog/triplet rules, deterministic IDs, catalog validation. |
| `publish.yaml` | `hydrology-publish`, version `1`, empty stages | Inert scaffold | Release candidate binding, policy/review decisions, manifest, correction and rollback targets. |

### Inventory limits

The inventory above is bounded to direct paths named by the prior README and inspected individually. It is not a recursive directory listing and does not prove that no other file exists. Any future stronger inventory claim should be generated from repository tooling and pinned to a commit.

[Back to top](#top)

---

## Repository fit

```text
External source
  -> connectors/<source>/
  -> data/raw/hydrology/ or data/quarantine/hydrology/ + data/receipts/
  -> pipeline_specs/hydrology/<profile>.yaml       # declarative WHAT
  -> pipelines/domains/hydrology/                  # executable HOW
  -> data/work/hydrology/
  -> data/processed/hydrology/
  -> data/catalog/domain/hydrology/ + data/triplets/
  -> release/candidates/hydrology/
  -> data/published/layers/hydrology/
  -> apps/governed-api/ -> apps/explorer-web/
```

### Adjacent responsibility roots

| Root or lane | Relationship to this README |
|---|---|
| `docs/domains/hydrology/` | Domain doctrine, source-role meaning, lifecycle, publication posture, and open questions. |
| `pipelines/domains/hydrology/` | Verified executable consumer must live here or in an accepted shared pipeline lane. |
| `connectors/<source>/` | Source-specific fetch and admission support. Specs must not embed source clients. |
| `data/registry/sources/hydrology/` | Source identity and activation authority. Specs reference descriptors by stable identifier. |
| `contracts/domains/hydrology/` | Semantic meaning for Hydrology objects and decisions, subject to active path resolution. |
| `schemas/contracts/v1/domains/hydrology/` | Machine-checkable Hydrology object shapes, subject to active path resolution. |
| `policy/domains/hydrology/` | Hydrology admissibility and anti-collapse rules. |
| `tests/` and `fixtures/` | Enforceability proof and controlled no-network examples. |
| `data/receipts/` and `data/proofs/` | Execution memory and evidence closure. Specs name requirements; they do not emit instances. |
| `release/` | Promotion, publication, correction, withdrawal, and rollback authority. |
| `apps/governed-api/` | Public trust membrane. Public clients must not consume specs directly. |

### Path conflicts

Hydrology documentation records a path-form conflict between domain-segment forms such as `contracts/domains/hydrology/` and flatter historical forms such as `contracts/hydrology/`. This README does not settle that conflict. New references should follow current Directory Rules and accepted ADRs; unresolved paths remain `CONFLICTED / NEEDS VERIFICATION`.

[Back to top](#top)

---

## Hydrology specification scope

A future governed Hydrology spec may configure profiles for:

- WBD/HUC watershed and boundary-vintage processing;
- hydrographic feature, waterbody, stream, river, and reach identity;
- gauge and observation-site metadata;
- flow, stage, water-level, water-quality, aquifer, groundwater, and hydrograph observations;
- regulatory flood context, including NFHL, without treating it as observed inundation;
- terrain-derived hydrology and drainage context;
- upstream/downstream traces, network topology, catchment association, and pour-point handling;
- hydrostratigraphy and geology-hydrology bridge records;
- water use, drought, irrigation, soil, agriculture, habitat, hazards, and infrastructure context joins;
- catalog, triplet, public-safe map-product, Evidence Drawer, and Focus Mode handoffs after release gates.

Hydrology may cite other lanes for context. It does not absorb Soil, Agriculture, Geology, Hazards, Atmosphere, Habitat, Settlements/Infrastructure, or People/Land authority.

### Profile families

| Profile family | Declarative responsibility | Must not imply |
|---|---|---|
| `ingest` | Bind admitted source descriptors, capture requirements, and RAW/quarantine handoff expectations. | Source activation or connector implementation. |
| `normalize` | Bind transforms, target contracts, identity, unit, geometry, and temporal normalization requirements. | Successful transformation or processed status. |
| `validate` | Bind schema, policy, evidence, source-role, temporal, geometry, topology, and negative-state checks. | Data correctness or release. |
| `catalog` | Bind evidence closure and catalog/triplet prerequisites. | Catalog truth merely because a record is generated. |
| `publish` | Bind release-candidate prerequisites and public-safe output expectations. | Promotion or publication. |
| `triplets` | Bind graph-projection rules and source evidence references. | Canonical truth or graph authority. |
| `rollback` | Bind rollback-readiness, prior-release references, and validation expectations. | Rollback execution. |
| `watchers` | Bind change-observation and materiality rules. | Source admission, processing, or publication. |
| object-specific | Bind watershed, reach, gauge, groundwater, water-quality, flood-context, topology, or hydrostratigraphy variants. | A new canonical object model. |

[Back to top](#top)

---

## Minimum active specification contract

The repository has not established a canonical pipeline-spec schema in the inspected evidence. The following is a **PROPOSED minimum contract**, not a claim that these field names are accepted.

```yaml
api_version: kfm.pipeline-spec/v1        # PROPOSED
kind: HydrologyPipelineSpec              # PROPOSED
metadata:
  spec_id: hydrology.<profile>           # stable, unique, deterministic
  spec_version: 0.1.0
  status: draft                          # draft | review | approved | suspended | retired
  owner_refs: []
  spec_hash: <canonical-hash>
  supersedes: null
consumer:
  pipeline_ref: pipelines/domains/hydrology/<verified-lane>
  implementation_ref: <commit-or-release-ref>
execution:
  mode: dry_run_first
  network: denied_by_default
  schedule_ref: null
sources:
  descriptor_refs: []
  allowed_roles: []
  rights_required: true
  sensitivity_required: true
lifecycle:
  input_states: []
  output_state: null
  quarantine_on: []
temporal:
  required_time_kinds: []
  freshness_budget_ref: null
  stale_outcome: HOLD
spatial:
  crs_policy_ref: null
  geometry_policy_ref: null
  topology_policy_ref: null
hydrology_boundaries:
  nfhl_is_regulatory_context_only: true
  modeled_is_not_observed: true
  not_for_life_safety: true
gates:
  schema_refs: []
  contract_refs: []
  policy_refs: []
  evidence_requirements: []
  review_requirements: []
outcomes:
  allowed: [PASS, NO_OP, HOLD, QUARANTINE, DENY, ERROR]
receipts:
  required_types: []
release:
  release_ready: false
  manifest_required: true
  correction_path_required: true
  rollback_target_required: true
```

### Contract requirements

An active specification should not be accepted unless it includes:

1. **Identity** — stable `spec_id`, version, owner, status, canonical hash, and supersession lineage.
2. **Consumer binding** — one verified executable pipeline target and an implementation revision or release reference.
3. **Source binding** — active descriptor references, allowed roles, rights, sensitivity, and source-vintage expectations.
4. **Lifecycle binding** — permitted inputs, intended output, quarantine rules, and no lifecycle skip.
5. **Temporal binding** — required time kinds, freshness budget, stale-state action, and clock source.
6. **Spatial binding** — CRS, geometry, scale/support, topology, and public-safe representation requirements.
7. **Hydrology anti-collapse binding** — NFHL, modeled/observed, gauge/warning, and official-source boundaries.
8. **Gate binding** — schema, contract, policy, evidence, review, and release requirements by stable reference.
9. **Finite outcomes** — deterministic allowed outcomes and reason-code expectations.
10. **Receipt binding** — required process records and stable output homes.
11. **Correction and rollback binding** — supersession, withdrawal, correction propagation, and rollback target.
12. **Fixture binding** — valid, invalid, stale, denied, quarantined, no-op, and error fixtures where applicable.

### Secret prohibition

Specs must never contain API keys, passwords, tokens, private certificates, connection strings, or real sensitive values. A spec may reference an approved secret **binding name** only after the canonical configuration and secret-management contract is verified. Do not invent an environment-variable name in this lane and call it canonical.

[Back to top](#top)

---

## Specification state and activation model

### Proposed finite states

```text
DRAFT -> REVIEW -> APPROVED -> ACTIVE
  |        |          |          |
  v        v          v          v
REJECTED  CHANGES    SUSPENDED  RETIRED
```

These states are **PROPOSED** until a governing contract and schema are accepted.

| State | Meaning | Execution posture |
|---|---|---|
| `DRAFT` | Authoring or scaffold state. | No execution. |
| `REVIEW` | Submitted with evidence, fixtures, tests, and impact analysis. | No production execution. Controlled validation only. |
| `APPROVED` | Reviews passed and bindings verified. | Still inactive until a separate activation decision. |
| `ACTIVE` | Explicit activation record, consumer, schedule/manual trigger, source descriptors, and rollback target verified. | Governed execution permitted. |
| `SUSPENDED` | Temporarily disabled due to source, policy, quality, security, or operational concerns. | Execution denied except diagnostics explicitly allowed by policy. |
| `RETIRED` | Superseded or withdrawn. | No new runs; lineage retained. |
| `REJECTED` | Not accepted. | No execution. |

### Activation is a separate governed decision

None of the following activates a spec:

- creating or editing a file;
- merging a pull request;
- setting `status: approved` inside the file;
- adding a schedule string;
- passing YAML parsing or schema validation;
- completing a CI workflow;
- naming a source descriptor;
- populating `stages`;
- producing a dry-run output.

Activation requires an auditable decision that verifies the spec hash, consumer binding, active source descriptors, rights, sensitivity, policy, fixtures, tests, receipts, schedule/manual trigger, correction path, and rollback target.

[Back to top](#top)

---

## Source descriptors, roles, rights, and activation

### Descriptor-gated sources

Every source used by an active spec must resolve to an admitted, active `SourceDescriptor`. A plain URL, filename, source-family name, connector path, or README link is not sufficient.

The spec should bind, by stable reference:

- source identity and product identity;
- source role and authority;
- rights, attribution, redistribution, and access posture;
- sensitivity and public-safe handling;
- source cadence and source-vintage semantics;
- endpoint/distribution identity where relevant;
- source-native IDs and expected schema/version;
- citation requirements;
- activation, suspension, and retirement state.

### Hydrology source-role discipline

Hydrology repeatedly encounters evidence that looks spatially similar but has different authority and fitness for use. Specs must preserve these distinctions:

| Knowledge character | Example class | Required posture |
|---|---|---|
| observation | gauge, stage, flow, water-quality measurement | Preserve provider, site/series identity, method, unit, qualifier, observation time, retrieval time, and quality state. |
| regulatory context | NFHL and comparable legally effective flood-hazard context | Never relabel as observed inundation, forecast, or current flood state. |
| modeled | modeled hydrograph, terrain-derived output, simulation | Require model/run provenance and never relabel as observation. |
| forecast context | externally issued forecast product | Preserve issuer, issue/valid/expiry times, uncertainty, and official-source redirect. KFM does not issue the forecast. |
| administrative | source-maintained boundaries, station metadata, identifiers | Preserve source vintage and authority; do not treat as observation. |
| aggregate | rollups or summaries | Preserve aggregation unit, method, temporal support, and input evidence. |
| candidate or synthetic | inferred, test, generated, or provisional content | Never enter public truth without explicit governed disposition; synthetic fixtures never become source records. |

### Rights and sensitivity

A spec must fail closed when rights, terms, attribution, sensitivity, or allowed use cannot be resolved. Public-safe geometry is not implied by a public source. Joins involving private property, critical infrastructure, precise sensitive assets, or restricted datasets require the most restrictive applicable policy.

[Back to top](#top)

---

## Temporal, freshness, and stale state

Hydrology specs must keep distinct time kinds separate where material:

- observation time;
- valid time or validity interval;
- issue time;
- expiry time;
- source update or source-vintage time;
- retrieval time;
- processing time;
- catalog time;
- release time;
- correction time.

### Required temporal controls

A future active spec should declare:

- which time kinds are required for each object or stage;
- source timezone and normalization rules;
- ordering and interval constraints;
- maximum acceptable source age or a stable freshness-policy reference;
- stale-state behavior;
- preliminary, provisional, approved, corrected, and final distinctions where supplied;
- late-arriving and out-of-order handling;
- clock source and deterministic test clock;
- no-op behavior when no material change exists.

### Freshness failure posture

| Condition | Default outcome |
|---|---|
| required observation/valid/retrieval time missing | `QUARANTINE` or `HOLD` |
| stale beyond approved budget | `HOLD`, `ABSTAIN`, or `DENY` for public use |
| future-dated or impossible ordering | `QUARANTINE` |
| provisional value presented as final | `DENY` for publication |
| official warning/forecast expired | `DENY` current-state presentation; preserve historical context if allowed |
| no material source change | `NO_OP` with receipt; do not mint new canonical entities |

A schedule is merely an execution intent. It cannot prove that the source was available, current, complete, or fit for use.

[Back to top](#top)

---

## Hydrologic identity, geometry, and topology

### Identity

A spec should preserve source-native identifiers and bind to accepted deterministic identity rules rather than inventing identifiers inside stage logic.

Identity requirements may include:

- provider and source-product identity;
- station, site, series, reach, waterbody, HUC, well, aquifer, or feature identifiers;
- source vintage or version;
- geometry fingerprint or normalized record digest where approved;
- crosswalk references and ambiguity outcomes;
- correction and supersession lineage.

Ambiguous crosswalks must not silently choose a match. The finite outcome should be `ABSTAIN`, `HOLD`, or `QUARANTINE` according to the governing contract.

### Geometry and coordinate reference

Specs should declare or reference:

- accepted source CRS and target CRS;
- axis-order and coordinate normalization;
- geometry type and dimensionality;
- precision and snapping rules;
- validity checks and repair policy;
- extent/bounds constraints;
- generalization or redaction transforms;
- geometry-digest rules;
- public-safe representation requirements.

### Topology

Hydrology topology is claim-bearing. A spec that processes stream networks, catchments, flow direction, upstream/downstream traces, pour points, or reach associations should require:

- stable node and edge identity;
- directionality and connectivity checks;
- self-loop, duplicate-edge, orphan-node, and impossible-cycle handling;
- source-vintage compatibility;
- crosswalk ambiguity handling;
- topology validation receipts;
- deterministic output ordering;
- explicit statement that a graph projection does not replace canonical evidence.

[Back to top](#top)

---

## Regulatory flood context and life-safety boundary

### NFHL anti-collapse rule

> [!CAUTION]
> NFHL and comparable regulatory flood-hazard layers are regulatory context. They are not observed inundation, current flood extent, gauge observation, forecast, emergency warning, evacuation direction, or KFM-issued safety instruction.

Any spec touching regulatory flood context must require:

- regulatory source role;
- issuing authority and source-product identity;
- effective/version fields and source vintage;
- distinct object/record class from observed flood evidence;
- explicit denial of observed-event, forecast, or current-warning labels;
- public-facing caveat and official-source redirect requirements;
- negative fixtures proving that role collapse fails closed.

### Gauge and warning distinction

A gauge measurement may support context, analysis, or a released historical/current-state view after validation. It does not by itself become an official flood warning. Warning and life-safety authority remains with the official issuer.

### Finite boundary outcomes

| Request or candidate | Required posture |
|---|---|
| show an admitted, released gauge measurement with time and qualifiers | Potentially `PASS`, subject to evidence/policy/release gates |
| label NFHL polygon as observed flood | `DENY` |
| label modeled hydrograph as gauge observation | `DENY` |
| present stale value as current | `DENY` or `HOLD` |
| ask KFM what protective action to take | Redirect to official authorities; KFM does not issue instructions |
| missing source-role or time support | `ABSTAIN`, `HOLD`, or `QUARANTINE` |

[Back to top](#top)

---

## Lifecycle gates and finite outcomes

The canonical lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A spec may name intended transitions. It cannot perform or authorize a transition merely by existing.

### Gate matrix

| Gate | Minimum declarative binding | Failure posture |
|---|---|---|
| identity | spec ID, version, owner, hash, supersession | `ERROR` or `DENY` |
| consumer | verified pipeline target and implementation reference | `HOLD` |
| source | active descriptor refs, roles, rights, sensitivity | `DENY` or `QUARANTINE` |
| temporal | required time kinds, freshness, stale behavior | `HOLD` or `QUARANTINE` |
| geometry/topology | CRS, geometry, scale, topology, ambiguity rules | `QUARANTINE` |
| lifecycle | allowed input/output states and no skip | `DENY` |
| contract/schema | stable semantic and shape references | `ERROR` or `HOLD` |
| evidence | EvidenceRef/EvidenceBundle requirements | `ABSTAIN` or `HOLD` |
| policy/review | policy refs and required reviewers | `DENY` or `HOLD` |
| receipts | required receipt types and homes | `ERROR` or `HOLD` |
| release | manifest, policy/review closure, correction and rollback | `DENY` |

### Finite spec-run outcomes

The exact vocabulary is **NEEDS VERIFICATION**, but an active system should use a finite, machine-testable set such as:

- `PASS` — declared run intent executed and stage output met its stage contract; not release approval.
- `NO_OP` — no material change; receipt emitted; no new canonical entity.
- `HOLD` — prerequisite or review unresolved; prior state preserved.
- `QUARANTINE` — material captured but barred from progression with reason.
- `DENY` — policy, role, rights, sensitivity, lifecycle, or release rule blocks the action.
- `ABSTAIN` — evidence is insufficient for a claim-producing or interpretive step.
- `ERROR` — system or contract failure; no unsafe fallback.

Reason codes should be stable, reviewable, and included in receipts.

[Back to top](#top)

---

## Stage profile contracts

The five present YAML files are inert. This section defines what each profile family would need before it could graduate beyond scaffold status.

### `ingest.yaml`

Minimum responsibilities:

- bind active source descriptors and approved distributions/endpoints;
- reference connector/admission outputs rather than implement source access;
- declare RAW/quarantine targets and source-native preservation requirements;
- require retrieval metadata, source URL/distribution identity, digest, source role, rights, sensitivity, and time fields;
- define no-op, rate-limit, denied, failed, quarantined, and admitted outcomes;
- require ingest/probe/admission receipts;
- deny secrets in the file.

### `normalize.yaml`

Minimum responsibilities:

- bind accepted RAW/WORK inputs and target contracts/schemas;
- declare unit, null, qualifier, identifier, CRS, geometry, temporal, and field normalization rules;
- preserve source-native values alongside approved conversions where required;
- declare deterministic ordering and hashing inputs;
- route unresolved identity, unit, geometry, temporal, rights, and role cases to quarantine;
- require transform and lineage receipts.

### `validate.yaml`

Minimum responsibilities:

- bind schema, contract, policy, source-role, temporal, freshness, geometry, topology, evidence, and anti-collapse checks;
- require positive and negative fixtures;
- test NFHL-as-observed denial, modeled-as-observed denial, stale-as-current denial, unresolved-source denial, lifecycle-skip denial, and missing-evidence behavior;
- produce deterministic validation results and reason codes;
- separate spec validation from data validation.

### `catalog.yaml`

Minimum responsibilities:

- require validated processed inputs and resolvable source/evidence references;
- bind deterministic dataset/item identity and catalog profile versions;
- define STAC/DCAT/PROV or other accepted catalog mappings by stable reference;
- preserve source role, time, rights, sensitivity, evidence, correction, and release-candidate state;
- declare triplet/graph projection as derived, non-sovereign output;
- require catalog integrity and evidence-closure validation.

### `publish.yaml`

Minimum responsibilities:

- accept only catalog/proof-closed release candidates;
- require `PolicyDecision`, review state, `ReleaseManifest`, correction path, and rollback target;
- require public-safe geometry and representation validation;
- preserve stale, provisional, regulatory-context, modeled, observation, and warning-boundary cues;
- deny direct RAW/WORK/QUARANTINE or candidate exposure;
- never perform publication merely because `release_ready: true` appears in the spec.

### Missing stage profiles

`triplets.yaml`, `rollback.yaml`, and `watchers.yaml` were absent at the checked paths. Their names in prior planning text remain proposals, not repo facts. They should not be created until their responsibility, schema, consumer, tests, and lifecycle boundaries are verified.

[Back to top](#top)

---

## Watchers, dry runs, and no-op discipline

A watcher observes possible source or metadata change. It is not a publisher, source authority, validator, or promotion authority.

A future watcher spec should declare:

- active descriptor and distribution references;
- cadence or event trigger;
- low-cost change probes and materiality rules;
- deterministic comparison keys;
- rate-limit, outage, retry, backoff, and circuit-breaker posture;
- finite outcomes such as `NO_OP`, `CHANGED`, `HOLD`, `DENY`, and `ERROR`;
- receipt requirements;
- candidate handoff target;
- explicit prohibition on direct catalog mutation or publication.

### Dry-run-first rule

New or materially changed specs should run against no-network fixtures before any live source probe. A dry run must not write to canonical lifecycle or release homes unless the dry-run contract explicitly directs output to a disposable QA location.

### No-op rule

When inputs and governing metadata have not materially changed, the system should emit a no-op receipt and avoid minting new canonical records, catalog entries, proofs, or releases.

[Back to top](#top)

---

## Receipts, evidence, and emitted artifacts

Specs declare expected receipts; execution emits them.

### Candidate receipt families

The exact canonical vocabulary remains `NEEDS VERIFICATION`. Depending on stage, a spec may need to require:

- probe or source-head receipt;
- ingest/admission receipt;
- no-op or material-change receipt;
- transform receipt;
- unit-conversion receipt;
- temporal/freshness receipt;
- geometry/CRS/generalization receipt;
- identity/crosswalk receipt;
- topology validation receipt;
- source-role validation receipt;
- NFHL/regulatory-context separation receipt;
- schema and policy validation receipt;
- catalog/triplet emission receipt;
- release-readiness receipt;
- correction, withdrawal, or rollback receipt.

### Evidence boundary

A receipt proves that a process occurred under a declared contract. It does not by itself prove the truth of a public claim. `EvidenceRef` must resolve to `EvidenceBundle` where a claim depends on evidence, and release state remains separately required.

### Output homes

Specs must point to accepted responsibility roots and must not embed emitted artifacts beside the YAML file.

```text
data/receipts/...       # process memory
data/proofs/...         # EvidenceBundle / proof closure
data/catalog/...        # catalog records
data/triplets/...       # graph projections
data/published/...      # released public-safe artifacts
release/...             # release decisions, manifests, correction, rollback
```

[Back to top](#top)

---

## Security, secrets, and network posture

### No secrets

Pipeline specs and committed configs must not contain:

- API keys or tokens;
- usernames or passwords;
- private certificates or keys;
- database credentials;
- private endpoint query strings containing secrets;
- sensitive personal or infrastructure values used only for local operation.

### Network denied by default

No-network fixture validation is the default. A live probe or run requires explicit authorization, an active descriptor, approved source/rights posture, bounded endpoint/distribution scope, timeout, rate-limit, retry, and audit behavior.

### Least privilege

The executing consumer should receive only the permissions needed for the declared stage. An ingest or normalization job must not automatically receive publication or release privileges.

### Logging and redaction

Logs and receipts must not expose secrets. Request identities should be hashable and replayable without hashing secret values. Sensitive coordinates, private-property joins, and critical-infrastructure detail must follow policy and data-minimization rules.

[Back to top](#top)

---

## Validation and enforceability

A specification is not governed merely because it is detailed. Its claims must be enforced by schemas, parsers, tests, policies, receipts, and consumer behavior.

### Validation layers

| Layer | What it must prove | Current status |
|---|---|---:|
| syntax | YAML is parseable and duplicate-key handling is defined | `UNKNOWN` for current stubs |
| spec schema | required fields, enums, references, and finite outcomes are valid | `UNKNOWN` |
| semantic contract | fields mean what the contract says | `UNKNOWN` |
| reference resolution | consumer, descriptors, schemas, policies, fixtures, and output homes resolve | `UNKNOWN` |
| stage compatibility | output of prior stage matches input of next stage | `UNKNOWN` |
| lifecycle | no skipped states or direct-public paths | `PROPOSED REQUIREMENT` |
| Hydrology anti-collapse | NFHL, model/observation, stale/current, warning/gauge boundaries fail closed | `PROPOSED REQUIREMENT` |
| temporal | required time kinds and freshness behavior are deterministic | `PROPOSED REQUIREMENT` |
| spatial/topology | CRS, geometry, scale, topology, and ambiguity rules are enforced | `PROPOSED REQUIREMENT` |
| security | secrets absent; network and permissions bounded | `PROPOSED REQUIREMENT` |
| receipts | required receipts are emitted and validate | `UNKNOWN` |
| release | manifest, policy/review, correction, and rollback gates are enforced | `UNKNOWN` |

### Required fixture classes

An active spec should have controlled fixtures for:

- valid input and expected output;
- missing descriptor;
- inactive or suspended source;
- unresolved rights or sensitivity;
- stale source;
- future-dated or impossible time ordering;
- invalid unit or conversion;
- invalid CRS/geometry;
- ambiguous reach/site crosswalk;
- topology defect;
- NFHL mislabeled as observed flooding;
- modeled output mislabeled as observation;
- warning context treated as KFM instruction;
- lifecycle skip;
- missing receipt/evidence/release dependency;
- no material change;
- retry exhaustion or circuit open;
- correction and rollback scenario.

### Current workflow caution

`.github/workflows/domain-hydrology.yml` is confirmed as a greenfield scaffold whose jobs only echo TODO text. A successful run of that workflow does **not** establish pipeline-spec validation, Hydrology data validation, evidence closure, proof generation, publish dry-run fidelity, or release readiness.

### Bounded repair rule

A documentation update must not quietly create code, schemas, tests, policies, descriptors, or workflow behavior to make its claims appear implemented. Missing enforcement remains explicit in the verification register and is addressed in separate, reviewable changes.

[Back to top](#top)

---

## Review, migration, and change discipline

### Review-impact matrix

| Change | Minimum review pressure |
|---|---|
| prose-only clarification with no contract effect | docs + pipeline-spec steward |
| add or rename a spec file | pipeline-spec, Hydrology, pipeline consumer, validation, docs |
| populate or modify stages | pipeline owner, Hydrology steward, source/rights, evidence, policy, validation, release as applicable |
| change source descriptor refs or roles | source steward + affected domain/policy reviewers |
| change time/freshness behavior | temporal/freshness + Hydrology + affected public-surface reviewers |
| change identity, geometry, or topology rules | Hydrology + spatial/topology + downstream consumer reviewers |
| change release or rollback requirements | release + policy + evidence + Hydrology |
| move or rename the lane | Directory Rules preflight + ADR/migration note + rollback plan |

### Duplicate and supersession checks

Before adding a new profile:

1. inspect current lane files and adjacent pipeline/config/spec lanes;
2. check whether the behavior belongs in an existing stage profile;
3. check accepted contracts, schemas, ADRs, and drift registers;
4. identify the single owning responsibility root;
5. record supersession or compatibility behavior;
6. avoid parallel spec registries, source lists, schema homes, or activation mechanisms.

### Generated, mirrored, and localized files

A generated or mirrored spec must declare its canonical source and must not be edited independently. This lane currently has no verified generator or mirror contract.

### Base drift

When the base branch changes during work, compare the old and new base. If the target, governing docs, schema, workflow, or consumer changed, re-read the affected evidence before mutation. Do not overwrite concurrent work by relying only on an earlier blob.

[Back to top](#top)

---

## Correction, deactivation, and rollback

### Spec correction

A material correction should:

- create a new version rather than silently rewrite historical meaning;
- preserve the prior spec and hash in lineage;
- explain the defect and affected runs/artifacts;
- identify downstream receipts, proofs, catalog records, releases, and public surfaces requiring review;
- provide re-run, correction, withdrawal, or rollback steps;
- prevent the corrected spec from reusing stale approval without review.

### Deactivation

A source outage, terms change, schema drift, rights problem, sensitivity issue, identity defect, topology defect, evidence failure, security concern, or incorrect public output may require suspension. Deactivation must be auditable and should not depend on deleting the file.

### Rollback

Rollback may involve:

- returning the active alias or scheduler binding to a prior approved spec;
- stopping future runs;
- withdrawing or superseding affected release candidates or releases;
- restoring prior public artifacts or removing unsafe aliases;
- emitting rollback and correction records;
- performing a downstream impact sweep.

A `rollback.yaml` file, if created later, would declare rollback-readiness requirements. It would not execute rollback or become release authority.

### Documentation-only rollback

This README revision can be reverted by reverting its commit. The five existing YAML scaffolds are not modified by this documentation change.

[Back to top](#top)

---

## Directory map

```text
pipeline_specs/hydrology/
├── README.md          # governed lane boundary; this file
├── ingest.yaml        # CONFIRMED inert scaffold; stages: []
├── normalize.yaml     # CONFIRMED inert scaffold; stages: []
├── validate.yaml      # CONFIRMED inert scaffold; stages: []
├── catalog.yaml       # CONFIRMED inert scaffold; stages: []
└── publish.yaml       # CONFIRMED inert scaffold; stages: []

# Prior README proposals; absent at checked paths and not created here:
# triplets.yaml
# rollback.yaml
# watchers.yaml
# watersheds_huc.yaml
# streams_reaches.yaml
# gauges_observations.yaml
# groundwater.yaml
# water_quality.yaml
# regulatory_flood_context.yaml
# topology_traces.yaml
# hydrostratigraphy.yaml
```

### Placement rule

Do not create a file simply to make this tree look complete. Each new spec needs a verified owner, consumer, schema, source/fixture/test posture, lifecycle need, anti-collapse rules, and rollback plan.

### Files that do not belong here

| Material | Correct responsibility root |
|---|---|
| executable Hydrology code | `pipelines/domains/hydrology/` or accepted shared pipeline lane |
| source clients | `connectors/<source>/` |
| source descriptors and activation | `data/registry/sources/` |
| object meaning | `contracts/` |
| machine schemas | `schemas/` |
| policy | `policy/` |
| fixtures and tests | `fixtures/`, `tests/` |
| lifecycle outputs | `data/raw`, `work`, `quarantine`, `processed`, `catalog`, `triplets`, `published` |
| receipt and proof instances | `data/receipts/`, `data/proofs/` |
| release decisions, corrections, rollback | `release/` |
| public API or UI code | `apps/governed-api/`, `apps/explorer-web/`, accepted packages |
| secrets | never in the repository |

[Back to top](#top)

---

## Definition of done

### This README revision

| Criterion | Status |
|---|---:|
| identifies the responsibility root and executable-companion boundary | `PASS` |
| records current lane files and scaffold maturity without overclaiming activation | `PASS` |
| preserves RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED | `PASS` |
| preserves NFHL/regulatory, model/observation, gauge/warning, and stale/current separation | `PASS` |
| defines minimum active-spec, source, time, identity, topology, evidence, policy, receipt, validation, and rollback requirements | `PASS` |
| avoids changing YAML scaffolds, code, schemas, policies, tests, fixtures, workflows, sources, data, receipts, proofs, or releases | `PASS` |
| verifies all repo-native checks after PR creation | `PENDING UNTIL CI` |

### Future active specification

A Hydrology spec is not done until:

- its identity, version, owner, hash, lineage, and finite state validate;
- its consumer and implementation revision resolve;
- all source descriptors are active and role/rights/sensitivity reviewed;
- lifecycle, temporal, freshness, identity, geometry, topology, and anti-collapse behavior is explicit;
- schemas, contracts, policies, evidence, reviews, and receipts resolve;
- valid and negative no-network fixtures pass substantive tests;
- secret scanning and network/permission controls pass;
- dry-run output is deterministic and confined to approved QA locations;
- correction, deactivation, supersession, and rollback paths are exercised;
- publication remains separately governed by release authority.

[Back to top](#top)

---

## Open verification register

| ID | Question | Status | Evidence needed |
|---|---|---|---|
| `PIPE-SPEC-HYD-001` | What is the accepted pipeline-spec semantic contract and machine schema? | `UNKNOWN` | Accepted contract/schema and validator evidence. |
| `PIPE-SPEC-HYD-002` | Is there a canonical parser, registry, loader, or scheduler for `pipeline_specs/`? | `UNKNOWN` | Code, tests, runtime/config binding, and operation receipt. |
| `PIPE-SPEC-HYD-003` | Which executable consumer owns each of the five present stubs? | `NEEDS VERIFICATION` | Consumer code and deterministic binding. |
| `PIPE-SPEC-HYD-004` | Which Hydrology source descriptors are admitted and active? | `NEEDS VERIFICATION` | Registry records, activation decisions, rights and sensitivity review. |
| `PIPE-SPEC-HYD-005` | What source-role and knowledge-character vocabularies are canonical? | `NEEDS VERIFICATION` | Accepted contract/ADR and tests. |
| `PIPE-SPEC-HYD-006` | Which time kinds and freshness budgets apply per profile? | `NEEDS VERIFICATION` | Temporal contract, policy, fixtures, and tests. |
| `PIPE-SPEC-HYD-007` | What deterministic identity, geometry, and topology rules are accepted? | `NEEDS VERIFICATION` | Contracts, schemas, crosswalk rules, validators, and fixtures. |
| `PIPE-SPEC-HYD-008` | Where are Hydrology pipeline-spec tests and fixtures, and what do they enforce? | `UNKNOWN` | Recursive inventory and executable results. |
| `PIPE-SPEC-HYD-009` | Which receipt and finite-outcome vocabularies are accepted? | `NEEDS VERIFICATION` | Schemas/contracts, emitted examples, and validator tests. |
| `PIPE-SPEC-HYD-010` | Does any workflow substantively validate these YAML files? | `UNKNOWN` | Workflow commands, logs, and failure fixtures; current domain workflow is TODO-only. |
| `PIPE-SPEC-HYD-011` | Should missing stage/object profiles be created, or should the five present files be consolidated differently? | `PROPOSED / ADR OR ROOT-NOTE` | Consumer design, duplication analysis, schema, and migration plan. |
| `PIPE-SPEC-HYD-012` | How is activation, suspension, retirement, correction, and rollback recorded? | `UNKNOWN` | Accepted governance contract and operational evidence. |
| `PIPE-SPEC-HYD-013` | Which contract/schema path form is canonical for Hydrology domain artifacts? | `CONFLICTED / NEEDS VERIFICATION` | Directory Rules, accepted ADRs, and current repo migration state. |
| `PIPE-SPEC-HYD-014` | What is the exhaustive direct-lane inventory at the current commit? | `NEEDS VERIFICATION` | Repository-generated recursive inventory. |
| `PIPE-SPEC-HYD-015` | Are current external source APIs, terms, versions, and distributions fit for activation? | `NEEDS VERIFICATION` | Current official-source review at activation time. |

[Back to top](#top)

---

## Evidence ledger

| Evidence | Status | What it supports | What it does not prove |
|---|---:|---|---|
| `pipeline_specs/hydrology/README.md` prior blob `b554a168…` | `CONFIRMED` | Existing boundary language and proposed profile families. | Active specs or implementation. |
| `pipeline_specs/README.md` blob `3a659989…` | `CONFIRMED` | Root `pipeline_specs/` versus `pipelines/` separation and lifecycle posture. | Hydrology consumer behavior. |
| five Hydrology YAML blobs | `CONFIRMED SCAFFOLDS` | Direct file presence and empty stages. | Activation, completeness, or correctness. |
| `pipelines/domains/hydrology/README.md` blob `e9da559b…` | `CONFIRMED DOCUMENTATION` | Intended executable-companion boundary and Hydrology anti-collapse posture. | Executable behavior or tests. |
| `docs/domains/hydrology/README.md` blob `57e5662e…` | `CONFIRMED DOCTRINE DOCUMENT` | Hydrology scope, source-role separation, proof-lane posture, and path conflicts. | Runtime maturity. |
| `DATA_LIFECYCLE.md` blob `086686b8…` | `CONFIRMED DOCTRINE DOCUMENT` | Hydrology lifecycle, gate, evidence, and correction expectations. | Current implementation. |
| `PUBLICATION_POSTURE.md` blob `47a24eff…` | `CONFIRMED DOCTRINE DOCUMENT` | Publication denials, NFHL role separation, and release requirements. | Current enforcement. |
| `.github/workflows/domain-hydrology.yml` blob `b54f7dbd…` | `CONFIRMED TODO SCAFFOLD` | Workflow presence and exact echo-only commands. | Substantive Hydrology validation. |
| attached v3.1 authoring prompt SHA-256 `b061d3d8…` | `CONFIRMED INPUT` | Documentation implementation, evidence, concurrency, validation, and PR discipline. | Repository behavior. |

### Evidence hierarchy

Current repository files and CI/runtime evidence outrank planning documents for implementation behavior. Governing doctrine still controls KFM invariants and responsibility placement. Where documentation and implementation differ, this README surfaces the difference instead of smoothing it.

[Back to top](#top)

---

## Maintainer note

Keep this lane declarative. Do not add source clients, executable processing, schemas, contracts, policy decisions, lifecycle outputs, receipts, EvidenceBundles, release decisions, warning instructions, public API/UI behavior, or secrets here.

Do not treat the existing five YAML files as active because they exist. Their current empty `stages` arrays are scaffold evidence only. Graduate them one at a time through explicit schema, consumer, source, fixture, test, receipt, policy, correction, and rollback gates.

<p align="right"><a href="#top">Back to top</a></p>
