<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-roads-rail-trade-readme
title: pipeline_specs/roads-rail-trade/ — Governed Roads / Rail / Trade Pipeline Specification Boundary
type: readme
version: v0.2
status: draft; repository-grounded; mixed-scaffold; no-active-specification-established
owners: OWNER_TBD — Pipeline-spec steward · Roads/Rail/Trade domain steward · Roads steward · Rail steward · Historic/trade-routes steward · Source steward · Rights reviewer · Sensitivity reviewer · Evidence steward · Policy steward · Validation steward · Release steward · CI steward · Migration steward · Docs steward
created: 2026-06-13
updated: 2026-07-15
supersedes: v0.1
policy_label: "public-doctrine; pipeline-specification; roads-rail-trade; declarative-only; mixed-scaffold; no-live-activation; no-public-navigation; no-operational-authority; no-legal-access-authority; source-role-aware; time-aware; evidence-bound; graph-derived-only; historic-route-generalization; cultural-review; infrastructure-review; fail-closed; release-gated; correction-aware; rollback-aware"
current_path: pipeline_specs/roads-rail-trade/README.md
truth_posture: >
  CONFIRMED target README v0.1, pipeline_specs root declarative-configuration boundary,
  five six-line stage YAML scaffolds with empty stages arrays, one minimal PROPOSED historic_routes.yaml
  planning placeholder, Roads/Rail/Trade executable-pipeline and domain documentation, current observed
  semantic-contract lane under contracts/domains/roads-rail-trade, flat contracts/transport compatibility
  guard, current observed parent schema lane under schemas/contracts/v1/domains/roads-rail-trade, flat
  schemas/contracts/v1/transport compatibility index with one empty decision-envelope scaffold, subtype-first
  Roads/Rail/Trade source-registry lane plus competing domain-first registry topology, TODO-only domain workflow,
  and bounded absence of accepted pipeline-spec schema, parser, registry, scheduler, consumer binding,
  package-local tests, fixtures, active source descriptors, emitted receipts, release use, or operational health /
  PROPOSED minimum active-spec contract, finite state and activation model, deterministic consumer binding,
  stage-profile semantics, source-role/rights/freshness gates, historic-route and cultural-sensitivity controls,
  network-graph and operational-context boundaries, receipts, finite outcomes, validation matrix, migration,
  correction, deactivation, and rollback requirements / CONFLICTED roads-rail-trade versus transport and
  domains-versus-flat schema/contract placement; subtype-first versus domain-first source-registry topology;
  Historic Route versus Historic RouteClaim naming; older source-role vocabulary versus the seven-role source
  catalog; planning-file presence versus no accepted active-spec contract / UNKNOWN accepted schema, parser,
  loader, registry, scheduler, first executable consumer, activation authority, source activation, substantive
  tests and fixtures, CI enforcement, emitted receipts/proofs, release integration, deployment, and production use /
  NEEDS VERIFICATION owners, exhaustive recursive lane inventory, CODEOWNERS coverage, spec identity grammar,
  canonical digest rules, activation-record home, stage compatibility, source-descriptor topology, slug ADR,
  historic-route terminology, receipt vocabulary, correction propagation, and rollback execution
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 6c71c48e88b34d76d00b43ab39d0a3a1b99328c7
  prior_blob: 049fb6a76a36d6d8858e19be9874aa3ecdef9a23
  pipeline_specs_root_blob: 3a6599898606126604298a281de53e39fdba98ce
  executable_pipeline_readme_blob: 8753ddce040943449f0a01b173c08d711f20e09a
  domain_readme_blob: b4e2d45f183986040622882f2fe2a090ef9a118d
  canonical_paths_blob: 684de491db1cdd7d141954603842acc9244075db
  historic_routes_doc_blob: c0589a71849944c878b6628d33e703c828c91f66
  sources_doc_blob: c47861f0e3b68fc3a0ee65a5448252a69260e4ba
  source_registry_blob: 54087e02e329b98c595807e4c9041c97972c0179
  contracts_domain_readme_blob: 79422f2b9fddd8a2755f54e43f94890881223b98
  contracts_transport_guard_blob: 65f48f0212c7c3d0e5f29aa65e1c6bc2b432a76f
  schemas_transport_index_blob: 3213a67499f31057ec7b702af5f22be2eb60d534
  domain_workflow_blob: c6f547b0acd8018284001ed67d25b153c0d9992b
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  ingest_blob: 4bc94b872a8a593c8195dc66cc764c0f4dbb7d7b
  normalize_blob: 35423145ebd244452563ffd3e37e521d97b6b1cd
  validate_blob: 12fef065dce136db4024938a04b461e256e278f9
  catalog_blob: 8acd5447a3849578580af0de3ba991d1abb5b8d8
  publish_blob: d36dd90cedd4990ae82f922cc1aa41cfa284e832
  historic_routes_spec_blob: 78ea48fccfba238683c7a97c711329da6075a86c
  bounded_path_checks:
    - pipeline_specs/roads-rail-trade/README.md existed at v0.1 before this revision
    - ingest.yaml, normalize.yaml, validate.yaml, catalog.yaml, and publish.yaml each contain name, version 1, and stages: []
    - historic_routes.yaml is a minimal PROPOSED planning placeholder that cites MISSING_OR_PLANNED_FILES.md
    - triplets.yaml, rollback.yaml, watchers.yaml, roads.yaml, rail.yaml, network_graph.yaml, restrictions_context.yaml, crossings_facilities.yaml, and trade_routes.yaml were not found at checked paths
    - tests/pipeline_specs/roads-rail-trade/README.md and test_spec_shape.py were not found at checked paths
    - fixtures/pipeline_specs/roads-rail-trade/README.md was not found at the checked path
    - bounded code search surfaced no accepted PipelineSpec model, parser, loader, scheduler, or Roads/Rail/Trade spec consumer
    - domain-roads-rail-trade workflow jobs are echo-only TODO scaffolds
related:
  - ../README.md
  - ./ingest.yaml
  - ./normalize.yaml
  - ./validate.yaml
  - ./catalog.yaml
  - ./publish.yaml
  - ./historic_routes.yaml
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/doctrine/lifecycle-law.md
  - ../../docs/doctrine/trust-membrane.md
  - ../../docs/domains/roads-rail-trade/README.md
  - ../../docs/domains/roads-rail-trade/CANONICAL_PATHS.md
  - ../../docs/domains/roads-rail-trade/HISTORIC_ROUTES.md
  - ../../docs/domains/roads-rail-trade/SOURCES.md
  - ../../pipelines/domains/roads-rail-trade/README.md
  - ../../contracts/domains/roads-rail-trade/README.md
  - ../../contracts/transport/README.md
  - ../../schemas/contracts/v1/domains/roads-rail-trade/README.md
  - ../../schemas/contracts/v1/transport/README.md
  - ../../data/registry/sources/roads-rail-trade/README.md
  - ../../policy/domains/roads-rail-trade/
  - ../../tests/pipeline_specs/roads-rail-trade/
  - ../../fixtures/pipeline_specs/roads-rail-trade/
  - ../../.github/workflows/domain-roads-rail-trade.yml
tags: [kfm, pipeline-specs, roads-rail-trade, transport, declarative-config, roads, rail, historic-routes, trade-routes, restrictions, crossings, network-graph, source-roles, temporal-validity, evidence, receipts, policy, release, rollback]
notes:
  - "This revision changes only pipeline_specs/roads-rail-trade/README.md."
  - "The lane currently contains five inert stage YAML scaffolds and one minimal historic-routes planning placeholder; none is established as active."
  - "This README does not activate sources, populate stages, create a parser, validate specs, bind an executable consumer, emit receipts, accept a slug ADR, or approve release."
  - "File presence, valid YAML, merge state, workflow success, or a non-empty stages array must never be treated as activation by itself."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Governed Roads / Rail / Trade Pipeline Specification Boundary

`pipeline_specs/roads-rail-trade/`

> Declarative run-intent boundary for Roads / Rail / Trade pipeline profiles. A reviewed specification may state **what** a verified pipeline should run, against which admitted sources, under which source-role, temporal, lifecycle, evidence, policy, graph, sensitivity, receipt, and release gates. It does not execute code, admit a source, determine a route or restriction as current, provide navigation or legal-access advice, establish graph truth, or publish an artifact.

![status](https://img.shields.io/badge/status-draft-blue)
![version](https://img.shields.io/badge/version-v0.2-informational)
![authority](https://img.shields.io/badge/authority-declarative__spec-green)
![inventory](https://img.shields.io/badge/inventory-5__inert__stage__stubs%20%2B%20historic__placeholder-lightgrey)
![activation](https://img.shields.io/badge/activation-none-orange)
![navigation](https://img.shields.io/badge/navigation-authority__denied-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-0b7285)

**Quick links:** [Purpose](#purpose) · [Authority](#authority-and-anti-collapse) · [Status](#current-status) · [Inventory](#current-inspected-inventory) · [Placement](#repository-fit-and-path-conflicts) · [Scope](#specification-scope) · [File contract](#minimum-active-specification-contract) · [State model](#specification-state-and-activation-model) · [Stage profiles](#root-stage-profile-contracts) · [Sources](#sources-roles-rights-and-freshness) · [Time](#temporal-validity-and-stale-state) · [Historic routes](#historic-route-and-cultural-corridor-boundary) · [Operations](#operational-restriction-and-access-boundary) · [Graphs](#network-graph-and-derived-projection-boundary) · [Lifecycle](#lifecycle-gates-and-finite-outcomes) · [Receipts](#receipts-evidence-and-emitted-artifacts) · [Security](#security-secrets-network-and-logging) · [Validation](#validation-and-enforceability) · [Review](#review-migration-and-change-discipline) · [Rollback](#correction-deactivation-and-rollback) · [Directory map](#directory-map) · [Done](#definition-of-done) · [Backlog](#open-verification-register) · [Evidence](#evidence-ledger)

> [!IMPORTANT]
> **Evidence snapshot:** `main@6c71c48e88b34d76d00b43ab39d0a3a1b99328c7`
> **Target blob before this revision:** `049fb6a76a36d6d8858e19be9874aa3ecdef9a23`
> **Confirmed stage scaffolds:** `ingest.yaml`, `normalize.yaml`, `validate.yaml`, `catalog.yaml`, and `publish.yaml`; each has `stages: []`.
> **Confirmed object-family placeholder:** `historic_routes.yaml`; it is a minimal `PROPOSED` planning pointer, not an active profile.
> **Activation:** path, filename, valid YAML, a populated `stages` list, merge, workflow completion, schedule text, or source-list text activates nothing.

> [!CAUTION]
> **Transport context is not operational authority.** A spec, geometry, route label, graph edge, restriction record, closure context, operator record, or generated explanation must not be presented as current navigation, traffic control, dispatch, emergency routing, railroad operating instruction, legal access determination, or safety advice. Redirect consequential operational questions to the appropriate official authority and preserve the source time and authority limit.

> [!WARNING]
> Historic and Indigenous trade or mobility corridors, cultural-route evidence, sensitive infrastructure, private access details, exact protected locations, credentials, and restricted-source content do not belong in specifications, examples, logs, screenshots, or PR bodies. Use identifiers and synthetic/public-safe examples; fail closed when rights, sensitivity, precision, authority, or release state is unresolved.

---

<a id="purpose"></a>

## Purpose

`pipeline_specs/roads-rail-trade/` is the Roads / Rail / Trade segment under the `pipeline_specs/` responsibility root.

Its safe future role is to hold reviewed, deterministic declarative profiles that bind:

- a stable specification identity, version, state, owner, digest, lineage, and correction path;
- exactly one verified executable consumer under `pipelines/`;
- admitted `SourceDescriptor` references and explicit source roles;
- source rights, access, attribution, authority scope, permitted use, and activation state;
- observation, event, valid, effective, source-vintage, retrieval, processing, review, release, correction, and supersession times;
- lifecycle input and output states plus quarantine behavior;
- object-family scope for roads, rail, crossings, facilities, restrictions, historic routes, trade corridors, graph projections, and derived narratives;
- schema, contract, policy, evidence, review, receipt, catalog, graph, release, and rollback requirements;
- public-safe geometry, overprecision denial, cultural review, infrastructure review, and no-operational-instruction obligations;
- no-network fixtures and expected finite outcomes.

A specification may **require** these controls. It cannot satisfy them merely by naming them.

### Audience

- pipeline-spec and Roads/Rail/Trade maintainers;
- road, rail, historic-route, trade-route, crossing, facility, restriction, graph, and movement-story stewards;
- source, rights, sensitivity, temporal, evidence, policy, validation, release, security, and documentation reviewers;
- maintainers implementing a future spec schema, parser, registry, scheduler, activation record, or executable consumer;
- reviewers preventing compatibility paths, aliases, or generated derivatives from becoming parallel authority.

[Back to top](#top)

---

<a id="authority-and-anti-collapse"></a>

## Authority and anti-collapse

### Responsibility split

```text
pipeline_specs/  = declarative run intent: WHAT may run and under which gates
pipelines/       = executable behavior: HOW processing occurs
connectors/      = source fetch and intake support; never publication
configs/         = safe-to-commit consumer settings; never secrets or activation authority
data/            = lifecycle state, registries, receipts, proofs, catalog/triplets, and released artifacts
contracts/       = semantic meaning
schemas/         = machine-checkable shape
policy/          = admissibility, rights, sensitivity, operational-use, and release obligations
tests/fixtures/  = enforceability proof and controlled synthetic/public-safe examples
release/         = release, correction, supersession, withdrawal, and rollback authority
apps/            = governed serving surfaces; never direct reads from specs as public truth
```

Directory Rules assign declarative configuration to `pipeline_specs/` and executable behavior to `pipelines/`. `roads-rail-trade` is a lane segment within responsibility roots, not a new root.

### This README may decide

This README may define:

- the maintenance boundary for this specification lane;
- current evidence and maturity;
- minimum requirements for a future active specification;
- anti-collapse, safety, sensitivity, graph, temporal, and release guardrails;
- validation, migration, correction, deactivation, and rollback expectations.

### This README cannot decide

This README cannot:

- admit, activate, suspend, or retire a source;
- determine route, road, rail, operator, closure, restriction, access, or facility truth;
- define semantic contracts or machine schemas;
- select a canonical slug or registry topology;
- execute a stage or schedule a run;
- persist lifecycle data, receipts, proofs, catalogs, graphs, or release records;
- approve exact historic or cultural geometry;
- authorize navigation, emergency routing, rail operations, legal access, or public release.

### Disallowed collapses

```text
spec file -> executable pipeline
spec presence -> active specification
valid YAML -> semantic validity
non-empty stages -> activation
source list -> source admission
schedule -> freshness proof
geometry -> legal access or passability
restriction context -> current instruction
operator row -> current operating authority
historic corridor -> survey-grade route
modern linework join -> historic precision
network edge -> source truth or public routing instruction
movement story -> evidence
successful run -> EvidenceBundle or release
workflow success -> implementation maturity
merge -> KFM PUBLISHED
```

[Back to top](#top)

---

<a id="current-status"></a>

## Current status

| Surface | Status | Safe conclusion |
|---|---:|---|
| Lane README | **CONFIRMED v0.1 before revision** | Existing guide was planning-heavy and did not accurately describe the current mixed scaffold. |
| Root stage files | **CONFIRMED five inert stubs** | Each declares `name`, integer `version: 1`, and `stages: []`. |
| Historic-routes file | **CONFIRMED minimal PROPOSED placeholder** | Cites a planning register; no active profile contract. |
| Spec schema | **NOT FOUND by bounded checks** | No accepted machine contract surfaced for these YAML files. |
| Parser/loader/registry | **NOT FOUND by bounded search** | No executable activation or validation path is established. |
| Consumer binding | **NOT FOUND by bounded search** | The companion pipeline README does not prove a consumer implementation. |
| Source activation | **UNKNOWN** | No active source descriptor set was established for a spec. |
| Tests/fixtures | **NOT FOUND at checked paths** | No dedicated Roads/Rail/Trade spec proof surfaced. |
| Domain workflow | **CONFIRMED TODO-only** | Echo jobs cannot prove validation, proof generation, or dry-run behavior. |
| Receipts/proofs | **UNKNOWN** | No emitted records tied to these specs were established. |
| Release/deployment | **UNKNOWN** | No use in a release or deployment was established. |

### Safe conclusion

The lane is a **mixed scaffold**. It contains declarative placeholders, but no specification is established as `ACTIVE`, executable, source-admitted, validated, receipt-producing, release-integrated, or production-ready.

### Corrections from v0.1

| Prior implication | Current evidence | Correction |
|---|---|---|
| The directory was mostly a proposed future tree | Six non-README YAML files are present | Record exact checked inventory. |
| `transport/` was the settled contract/schema segment | Current domain contract/schema lanes coexist with flat compatibility guards | Mark placement `CONFLICTED`; do not choose a winner. |
| Proposed imports/tests/files described likely implementation | No parser, consumer, tests, or accepted schema surfaced | Treat all such names as lineage, not facts. |
| A minimal example implied a usable profile shape | Existing stage files contain only empty `stages` arrays | Define a future contract without calling it implemented. |
| Workflow presence implied domain checks | Jobs only echo TODO text | Do not treat green status as enforceability proof. |

[Back to top](#top)

---

<a id="current-inspected-inventory"></a>

## Current inspected inventory

Bounded direct-file inspection established:

```text
pipeline_specs/roads-rail-trade/
├── README.md
├── ingest.yaml              # name/version + stages: []
├── normalize.yaml           # name/version + stages: []
├── validate.yaml            # name/version + stages: []
├── catalog.yaml             # name/version + stages: []
├── publish.yaml             # name/version + stages: []
└── historic_routes.yaml     # minimal PROPOSED planning pointer
```

Checked but not found at the inspected base:

```text
triplets.yaml
rollback.yaml
watchers.yaml
roads.yaml
rail.yaml
trade_routes.yaml
network_graph.yaml
restrictions_context.yaml
crossings_facilities.yaml
tests/pipeline_specs/roads-rail-trade/README.md
tests/pipeline_specs/roads-rail-trade/test_spec_shape.py
fixtures/pipeline_specs/roads-rail-trade/README.md
```

This is a bounded inventory, not a permanent claim that no other generated, historical, or unindexed references exist.

### Inert stage rule

`stages: []` means **no stage behavior is declared**. It must not be interpreted as:

- a no-op run that is safe to activate;
- a default stage list supplied elsewhere;
- a valid production profile;
- an instruction to discover stages dynamically;
- approval to call the matching executable lane.

A future parser should return an explicit inactive or invalid result unless an accepted profile contract deliberately defines another posture.

[Back to top](#top)

---

<a id="repository-fit-and-path-conflicts"></a>

## Repository fit and path conflicts

### Placement basis

The requested target is correctly placed because:

- `pipeline_specs/` owns declarative pipeline configuration;
- `roads-rail-trade/` is the domain segment used by this root;
- executable logic remains under `pipelines/domains/roads-rail-trade/`;
- no new root, move, or parallel spec home is introduced.

### Contract and schema placement is conflicted

Current repository evidence differs from the older v0.1 wording:

| Surface | Current observed posture | This spec lane must do |
|---|---|---|
| `contracts/domains/roads-rail-trade/` | Observed working semantic-contract lane; mostly draft/scaffold | Reference explicitly where needed; do not redefine. |
| `contracts/transport/` | Compatibility guard only | Do not treat as canonical object meaning. |
| `schemas/contracts/v1/domains/roads-rail-trade/` | Observed parent domain schema lane | Reference only after exact schema acceptance. |
| `schemas/contracts/v1/transport/` | Flat compatibility index with one empty decision-envelope scaffold | Do not use as blanket validation authority. |

The unresolved dimensions are:

1. `roads-rail-trade` versus `transport`;
2. `domains/<domain>/` versus a flat family path.

A spec must carry exact contract and schema refs. It must not derive them from the domain slug, follow “latest,” search both roots and pick the first match, or accept a fabricated hybrid path such as `domains/transport/`.

### Source-registry topology is also conflicted

Current docs expose both:

```text
data/registry/sources/roads-rail-trade/
data/registry/roads-rail-trade/sources/
```

A future spec must reference stable descriptor identifiers, not infer authority from whichever path exists. Registry topology requires an ADR, migration note, or accepted index before automated resolution.

### Historic-route naming is conflicted

Both `Historic Route` and `Historic RouteClaim` occur in governing documentation. Specifications must not silently normalize one into the other until a contract or ADR resolves the term. Where claim semantics and uncertainty matter, preserve the explicit claim nature and the source term.

[Back to top](#top)

---

<a id="specification-scope"></a>

## Specification scope

A future Roads/Rail/Trade specification may configure reviewed run intent for:

- road-segment intake, normalization, validation, catalog, and release-candidate preparation;
- rail segments, operators, depots, sidings, yards, crossings, and status events;
- bridges, ferries, and river-crossing transport relations while preserving Hydrology and Infrastructure authority;
- historic-route claims, trade corridors, frontier routes, military/mail/stage/cattle/emigrant routes, and cultural mobility context;
- freight corridors and logistics context;
- restrictions, work zones, closures, permits, height/weight limits, and stale-state handling;
- route events, designation changes, abandonment, renaming, and jurisdiction/operator assertions;
- derived nodes, edges, route memberships, graph projections, and no-routing-authority constraints;
- movement-story and Focus Mode handoffs that retain evidence and uncertainty;
- public-safe geometry, generalization, withholding, and review obligations;
- catalog, triplet, proof, release-readiness, correction, and rollback preflight.

### Cross-domain references

A spec may require governed references to:

- Settlements / Infrastructure for asset identity;
- Hydrology for water evidence;
- Hazards for event authority;
- Archaeology / Cultural Heritage for sovereignty and sensitive-site controls;
- People / DNA / Land for private-property or living-person context;
- Spatial Foundation for CRS and geometry operations.

A cross-domain reference never transfers canonical authority into Roads/Rail/Trade.

[Back to top](#top)

---

<a id="minimum-active-specification-contract"></a>

## Minimum active specification contract

Everything in this section is **PROPOSED** until accepted in a semantic contract, machine schema, parser, tests, and consumer integration.

An active specification should contain or resolve the following fields without hidden defaults.

### Identity and lineage

| Field | Requirement |
|---|---|
| `spec_id` | Stable immutable identifier with accepted grammar. |
| `spec_version` | Immutable version; no mutable `latest`. |
| `state` | Finite state from an accepted state model. |
| `owner` | Accountable steward or team identifier. |
| `domain` | Exact `roads-rail-trade` lane identifier. |
| `profile_kind` | Stage or object-family profile type. |
| `spec_digest` | Canonical digest produced by an accepted algorithm. |
| `supersedes` | Prior version or specification reference where applicable. |
| `correction_ref` | Correction record when replacing erroneous intent. |

### Contract, schema, and consumer binding

| Field | Requirement |
|---|---|
| `contract_ref` | Exact accepted semantic contract and version. |
| `schema_ref` | Exact accepted machine schema and version. |
| `consumer_ref` | Exact executable pipeline entrypoint or registered consumer. |
| `consumer_version` | Version proven compatible with the spec. |
| `compatibility_profile` | Rules for spec/consumer/schema compatibility. |
| `activation_ref` | External activation decision or registry record. |

### Sources and authority

| Field | Requirement |
|---|---|
| `source_descriptor_refs` | Stable admitted descriptor identifiers. |
| `source_roles` | Explicit role per descriptor; never inferred from filename. |
| `source_activation_required` | Must be true for live access. |
| `rights_profile_refs` | Rights, license, permitted-use, and attribution refs. |
| `authority_limits` | What each source may and may not establish. |
| `freshness_policy` | Source-vintage and stale-state handling. |

### Time and lifecycle

| Field | Requirement |
|---|---|
| `input_state` | Allowed lifecycle input state. |
| `output_state` | Candidate output state; never direct publication. |
| `quarantine_on` | Finite conditions that route to QUARANTINE. |
| `source_time_fields` | Source publication/vintage/issue times. |
| `valid_time_fields` | Effective/valid intervals for status-bearing records. |
| `retrieval_time_required` | Required for fetched inputs. |
| `processing_time_policy` | Injected or explicitly recorded processing time. |
| `stale_behavior` | BLOCK, QUARANTINE, ABSTAIN, or another accepted result. |

### Domain and safety gates

| Field | Requirement |
|---|---|
| `object_families` | Exact included families; no wildcard expansion without review. |
| `historic_route_policy` | Claim/uncertainty/generalization requirements. |
| `cultural_review_required` | Explicit trigger and steward surface. |
| `infrastructure_review_required` | Explicit trigger and exposure limits. |
| `operational_context_not_instruction` | Must remain true. |
| `legal_access_not_inferred` | Must remain true. |
| `graph_is_derived` | Must remain true. |
| `public_precision_profile` | Exact generalization/withholding profile. |

### Evidence, policy, receipts, and release

| Field | Requirement |
|---|---|
| `evidence_requirements` | EvidenceRef/EvidenceBundle resolution obligations. |
| `policy_requirements` | Policy families, version refs, and finite decision handling. |
| `review_requirements` | Steward roles and required review state. |
| `receipt_requirements` | Run, transform, validation, temporal, graph, generalization, and other receipt refs. |
| `catalog_requirements` | Catalog closure and provenance requirements. |
| `release_requirements` | ReleaseManifest inputs and blocker behavior. |
| `rollback_ref` | Known safe rollback target or explicit blocker. |
| `expected_outcomes` | Finite expected results for fixtures and dry runs. |

### Illustrative shape only

```yaml
spec_id: rrt.ingest.example
spec_version: 0.1.0
state: DRAFT
owner: OWNER_TBD
domain: roads-rail-trade
profile_kind: ingest
spec_digest: sha256:PROPOSED
supersedes: null
contract_ref: NEEDS_VERIFICATION
schema_ref: NEEDS_VERIFICATION
consumer:
  ref: NEEDS_VERIFICATION
  version: NEEDS_VERIFICATION
activation_ref: null
sources:
  source_descriptor_refs: []
  require_active: true
lifecycle:
  input_state: RAW
  output_state: WORK
  quarantine_on: [missing_rights, unresolved_source_role, stale_status]
requirements:
  evidence_bundle_required: true
  policy_required: true
  operational_context_not_instruction: true
  legal_access_not_inferred: true
  graph_is_derived: true
  receipts_required: []
release:
  release_ready: false
  rollback_ref: null
```

This example is not a schema, active profile, compatibility promise, or authorization to populate existing stubs.

[Back to top](#top)

---

<a id="specification-state-and-activation-model"></a>

## Specification state and activation model

A finite state model is required before any file can drive execution. Proposed states:

```text
SCAFFOLD -> DRAFT -> REVIEWED -> ACTIVE -> SUSPENDED -> RETIRED
                    \-> REJECTED
```

| State | Meaning | May drive execution? |
|---|---|---:|
| `SCAFFOLD` | Placeholder lacking an accepted contract or complete fields. | No |
| `DRAFT` | Authoring candidate under review. | No |
| `REVIEWED` | Content reviewed but activation not granted. | No |
| `ACTIVE` | Explicit activation record binds exact spec, consumer, sources, policy, and environment. | Only within that binding |
| `SUSPENDED` | Temporarily disabled due to drift, incident, stale source, policy, or review. | No |
| `RETIRED` | Permanently superseded or withdrawn. | No |
| `REJECTED` | Not admissible for activation. | No |

### Activation invariants

Activation must be an explicit governed binding containing at least:

- exact `spec_id`, version, and digest;
- exact consumer identity and version;
- exact source descriptor identities and activation states;
- policy and rights profile versions;
- environment or execution profile;
- activation time, actor, review refs, expiry, and rollback target;
- finite failure posture.

File placement, a Git merge, YAML parsing, schema validation, workflow success, or a schedule is insufficient.

### No implicit discovery

A consumer must not:

- scan this directory and execute every YAML file;
- select the newest filename or highest version automatically;
- activate a profile because `stages` is non-empty;
- follow symlinks or aliases outside an accepted root;
- fall back from a missing profile to another file;
- accept UI, query-string, prompt, or untrusted runtime selection as activation authority.

[Back to top](#top)

---

<a id="root-stage-profile-contracts"></a>

## Root stage profile contracts

The five checked root files are inert scaffolds. Future stage semantics should be ratified without mutating their meaning implicitly.

### `ingest.yaml`

A future ingest spec may bind admitted source descriptors to a connector and declare RAW-to-WORK/QUARANTINE intake gates. It must not fetch from an unadmitted source, upgrade source role, or write directly to PROCESSED/PUBLISHED.

Required proof should cover source activation, rights, endpoint/config refs, retrieval time, payload identity, hashing, immutable RAW handling, quarantine, and intake receipts.

### `normalize.yaml`

A future normalize spec may select transforms from WORK/QUARANTINE candidates. It must preserve source-native fields, source roles, temporal semantics, uncertainty, rights, restrictions, and raw lineage.

Required proof should cover deterministic identity, schema/contract refs, class maps, geometry handling, historic-route uncertainty, negative cases, and transform receipts.

### `validate.yaml`

A future validate spec may require machine-shape, semantic, source-role, temporal, rights, sensitivity, graph, operational-context, and evidence checks. It must not define policy or treat validation as release.

Required proof should cover both valid and invalid fixtures, expected reason codes, no warning-only bypass, and deterministic validation reports.

### `catalog.yaml`

A future catalog spec may declare closure requirements for discoverability/provenance records. It must not convert an unsupported candidate into catalog truth or omit EvidenceBundle and source-role links.

Required proof should cover identity, provenance, citation, time, rights, sensitivity, support refs, correction lineage, and catalog closure.

### `publish.yaml`

A future publish-readiness spec may evaluate whether a release candidate contains required proofs, policies, reviews, transformations, and rollback targets. It must not publish, sign, or create release approval.

Required proof should cover ReleaseManifest input completeness, public-safe geometry, obligation enforcement, correction/takedown path, rollback target, and denial cases.

### Missing stage profiles

`triplets.yaml`, `rollback.yaml`, and `watchers.yaml` were not found at checked paths. Their names in older planning material do not authorize creation. Add them only after ownership, consumer, contract/schema, tests, and Directory Rules placement are verified.

[Back to top](#top)

---

<a id="sources-roles-rights-and-freshness"></a>

## Sources, roles, rights, and freshness

### SourceDescriptor-first rule

A spec must reference admitted source descriptors. It must not embed credentials, full provider configuration, source payloads, or a prose list treated as activation.

Each descriptor should provide or resolve:

- stable source identity and version;
- source role and authority scope;
- rights, license, attribution, permitted use, and redistribution posture;
- cadence, source vintage, issue/effective time, and freshness expectations;
- sensitivity and precision limits;
- endpoint/config references without secrets;
- activation, suspension, supersession, and review state;
- citation template and known limitations.

### Source-role anti-collapse

The Roads/Rail source catalog documents seven roles:

```text
observed | regulatory | modeled | aggregate | administrative | candidate | synthetic
```

Role is fixed at admission and must survive normalization, graph projection, cataloging, rendering, and generated explanation.

Examples of disallowed upcasts:

```text
administrative facility roster -> observed event timeline
candidate OSM geometry -> legal road or rail status
modeled historic corridor -> observed alignment
aggregate freight context -> per-segment movement observation
synthetic route narrative -> source evidence
```

Other older domain documents use different illustrative role vocabularies such as `authority | observation | context | model`. That vocabulary difference is **CONFLICTED** and must be normalized through an accepted source-role contract, never by ad hoc spec logic.

### Source-family posture

Likely families include federal, state, county, railroad, historic-map, archive, OSM, GNIS, WZDx, bridge/restriction, freight-network, and cultural/interpretive sources. Their exact role, rights, endpoints, freshness, and activation remain `NEEDS VERIFICATION` until an admitted descriptor is inspected.

[Back to top](#top)

---

<a id="temporal-validity-and-stale-state"></a>

## Temporal validity and stale state

Roads/Rail/Trade carries multiple time kinds that must not collapse:

| Time kind | Example |
|---|---|
| Observation time | When a condition or feature was observed. |
| Event time | When designation, closure, abandonment, or status change occurred. |
| Valid/effective time | Interval during which a restriction or operator status applies. |
| Source publication/vintage | Edition or release date of the source. |
| Retrieval time | When KFM fetched or received the source. |
| Processing time | When the pipeline transformed it. |
| Review time | When a steward reviewed it. |
| Release time | When a governed artifact became public. |
| Correction/supersession time | When prior material was corrected or replaced. |

### Status-bearing data

Current road conditions, closures, restrictions, permits, operator state, rail service, and infrastructure status require:

- explicit authoritative source and authority limit;
- valid/effective interval;
- issue/source time and retrieval time;
- stale threshold and expiry behavior;
- clear non-operational disclaimer where appropriate;
- no reuse after expiry without re-evaluation.

A stale or time-ambiguous status must not silently remain active. The default result should be BLOCK, QUARANTINE, ABSTAIN, or another accepted negative state.

### Historic time

Historic route claims require source vintage, claimed historical interval, uncertainty, and method. A modern layer cannot supply missing historical time or certainty.

[Back to top](#top)

---

<a id="historic-route-and-cultural-corridor-boundary"></a>

## Historic-route and cultural-corridor boundary

`historic_routes.yaml` is currently a planning pointer only. It does not establish a usable specification.

A future historic-route profile must preserve:

- claim semantics rather than survey-line semantics;
- `Historic Route` versus `Historic RouteClaim` terminology conflict;
- source role and authority limits;
- source vintage and historical validity interval;
- alignment uncertainty as first-class data;
- generalized public geometry and overprecision denial;
- EvidenceRef/EvidenceBundle requirements;
- Indigenous, treaty, oral-history, cultural, and sovereignty review;
- Archaeology/Cultural-Heritage policy authority;
- correction, withdrawal, and public-layer rollback.

### No precision laundering

The following is forbidden:

```text
uncertain historic claim
  + modern precise road/parcel/PLSS geometry
  -> falsely precise historic alignment
```

Joining to modern geometry may support context, but it cannot upgrade the historic claim’s precision or source role. Public geometry remains bounded by the historic evidence and applicable sensitivity policy.

### Most-restrictive posture

Where cultural, Indigenous, archaeological, restricted-source, or protected-location concerns overlap, apply the most restrictive applicable policy. Generalization or withholding is the default until steward review and release gates close.

[Back to top](#top)

---

<a id="operational-restriction-and-access-boundary"></a>

## Operational, restriction, and access boundary

A specification may require processing of restriction or operational context, but it cannot turn KFM into an operational service.

### Never infer

- current passability from geometry;
- legal access from road, parcel, or route presence;
- safe travel from absence of a closure record;
- railroad operating permission from alignment/operator records;
- bridge clearance or load safety from stale inventory;
- emergency or evacuation routing from graph connectivity;
- private-road permission from mapping tags;
- official closure status from an unverified feed or old record.

### Required negative behavior

When a user-facing consequence could be mistaken for current operational advice, downstream systems must:

- cite the official authority and timestamp;
- state authority and freshness limits;
- avoid imperative routing language;
- deny or abstain when current official support is missing;
- redirect to official real-time sources for safety-critical decisions.

### Restricted and sensitive context

Specifications must minimize and policy-gate:

- critical transport facilities;
- restricted crossings or access points;
- private access notes;
- security-sensitive operational detail;
- exact protected or cultural locations;
- non-public railroad or infrastructure information.

[Back to top](#top)

---

<a id="network-graph-and-derived-projection-boundary"></a>

## Network graph and derived projection boundary

Graph nodes, edges, route memberships, connectivity, and inferred corridors are **derived projections**.

A future graph profile must bind:

- source records and exact source roles;
- node/edge identity grammar;
- directionality and temporal scope;
- topology and connectivity confidence;
- uncertainty and generalization;
- forbidden operational uses;
- graph build/version digest;
- source-to-edge lineage;
- correction and rebuild behavior;
- graph receipt and proof requirements.

### Anti-collapse

```text
graph edge != road segment
graph edge != legal route
graph connectivity != access permission
shortest path != recommended route
historic route projection != surveyed alignment
triplet != evidence
movement story != source truth
```

Graph output may support analysis and governed display after policy/release review. It must not replace canonical evidence-bearing records or become a direct public routing engine.

[Back to top](#top)

---

<a id="lifecycle-gates-and-finite-outcomes"></a>

## Lifecycle gates and finite outcomes

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Specifications may constrain a transition. They do not perform or approve it.

### Lifecycle gate rules

| Transition | Minimum spec posture |
|---|---|
| Source intake -> RAW | Admitted source, rights, source role, immutable capture, receipt expectation. |
| RAW -> WORK | Explicit transform intent and lineage. |
| WORK -> QUARANTINE | Finite reason and correction/review path. |
| WORK -> PROCESSED | Schema, semantic, source-role, temporal, rights, sensitivity, and evidence checks. |
| PROCESSED -> CATALOG/TRIPLET | Closure, provenance, identity, graph/support refs, no truth collapse. |
| CATALOG/TRIPLET -> PUBLISHED | Policy, review, release manifest, public-safe transforms, correction, rollback. |

### Proposed spec-evaluation outcomes

These outcomes are **PROPOSED** and must remain distinct from policy outcomes, validation reports, run receipts, lifecycle states, and release decisions.

| Outcome | Meaning |
|---|---|
| `SPEC_VALID` | Shape and semantic profile pass; not active. |
| `SPEC_INVALID` | Contract/schema or semantic requirements fail. |
| `NOT_ACTIVE` | No accepted activation binding exists. |
| `BLOCKED` | Required source, rights, policy, evidence, consumer, or release prerequisite is absent. |
| `QUARANTINE` | Reviewable risk requires isolation. |
| `NO_CHANGE` | Dry-run detects no material change under an accepted comparison rule. |
| `SUSPENDED` | Previously active binding is disabled. |
| `ERROR` | Evaluation could not complete safely. |

`SPEC_VALID` must never be rendered as “allowed,” “published,” or “safe to navigate.”

[Back to top](#top)

---

<a id="receipts-evidence-and-emitted-artifacts"></a>

## Receipts, evidence, and emitted artifacts

A specification may require outputs; it does not emit or persist them merely by existing.

### Candidate receipt families

A future active profile may require references to:

- source-intake receipt;
- run receipt;
- transform receipt;
- validation report/receipt;
- temporal/freshness receipt;
- source-role preservation receipt;
- geometry/generalization receipt;
- historic-route uncertainty/overprecision receipt;
- graph-build/topology receipt;
- sensitivity/rights review record;
- policy decision;
- catalog/triplet closure record;
- release-readiness report;
- correction, withdrawal, or rollback record.

Exact canonical families and fields remain `NEEDS VERIFICATION`.

### Evidence rules

- Claims depending on evidence must retain resolvable EvidenceRefs.
- EvidenceBundle closure outranks a successful spec validation or run.
- A receipt records process; it does not prove the underlying route claim by itself.
- A graph or catalog object remains derived and source-bound.
- Generated movement narratives remain interpretive and citation-bound.

### Output placement

Specifications must identify output responsibility roots, but never write outputs beside YAML profiles. Runtime artifacts belong under governed data, receipt, proof, catalog, triplet, and release homes.

[Back to top](#top)

---

<a id="security-secrets-network-and-logging"></a>

## Security, secrets, network, and logging

### Specifications must not contain

- API keys, tokens, credentials, cookies, certificates, or private keys;
- private endpoints or internal hostnames when disclosure is unsafe;
- raw source payloads or proprietary extracts;
- exact sensitive cultural, archaeological, infrastructure, or private-access locations;
- living-person or private-property joins;
- unrestricted railroad-operating or security-sensitive detail;
- raw prompts, chain-of-thought, or generated private context.

### Network posture

Parsing and validating a spec should be offline and deterministic. A spec may reference an approved connector/config identity, but must not embed arbitrary URLs that a parser fetches during validation.

Live network access belongs to the bound connector or pipeline under explicit source activation, configuration, egress, timeout, retry, and receipt controls.

### Path and reference safety

A future parser must reject or constrain:

- absolute paths outside accepted roots;
- `..` traversal;
- arbitrary symlinks;
- mutable “latest” aliases;
- environment-variable expansion for authority-bearing refs;
- unbounded includes or recursive references;
- duplicate spec identities;
- oversized or deeply nested YAML;
- unsafe YAML object tags.

### Logging

Log stable identifiers, finite outcomes, and safe reason codes. Do not log secrets, raw restricted payloads, exact protected coordinates, private access notes, or full sensitive evidence.

[Back to top](#top)

---

<a id="validation-and-enforceability"></a>

## Validation and enforceability

Current status: the five stage files are syntactically small YAML scaffolds; no accepted spec schema, parser, dedicated tests, fixtures, or substantive domain workflow was established.

### Validation layers

| Layer | Must prove |
|---|---|
| YAML safety | Safe loader; no duplicate keys, unsafe tags, traversal, or uncontrolled includes. |
| Machine shape | Exact accepted schema and version. |
| Semantic completeness | Required identity, consumer, sources, time, lifecycle, safety, evidence, policy, receipts, and rollback. |
| Reference integrity | Contract/schema/consumer/source/policy refs resolve to accepted versions. |
| Activation | Exact activation binding exists and is not expired/suspended. |
| Stage compatibility | Stage profile and consumer version are compatible. |
| Source authority | Descriptor role, rights, activation, cadence, and authority limits are preserved. |
| Historic/cultural | Uncertainty, generalization, cultural review, overprecision denial. |
| Operational safety | No navigation, legal-access, emergency-routing, or rail-operating authority. |
| Graph boundary | Derived graph cannot replace source records or route authority. |
| Lifecycle | No illegal state transition or direct publication. |
| Receipts/release | Required process memory and release blockers are explicit. |

### Minimum test matrix

| Family | Required cases |
|---|---|
| Inventory | Exact supported files; unknown files rejected or ignored by accepted rule. |
| Empty stages | Current `stages: []` files remain inactive. |
| Identity | Missing/duplicate/malformed ID, version, digest, owner. |
| Schema/contract | Missing, wrong version, compatibility conflict, unresolved slug path. |
| Consumer | Missing consumer, wrong version, unknown stage, unsupported profile. |
| Sources | Missing descriptor, inactive source, role mismatch, rights unresolved, stale source. |
| Time | Missing valid time, expired restriction, stale operational status, historic interval ambiguity. |
| Lifecycle | RAW-to-PUBLISHED bypass, missing quarantine, invalid output state. |
| Historic routes | Overprecision, modern precision laundering, cultural review absent, uncertain geometry. |
| Operations | Navigation instruction, emergency route, legal access inference, stale closure. |
| Graph | Edge without source lineage, route recommendation, unsupported topology. |
| Evidence/policy | Unresolved EvidenceRef, negative policy result, unmet obligation. |
| Receipts | Missing required receipt/ref, mismatched digest, correction lineage absent. |
| Security | Secret pattern, unsafe YAML tag, traversal, symlink escape, oversized input. |
| Determinism | Stable parse/index/digest/outcome across repeated runs. |
| Correction/rollback | Suspension, supersession, withdrawal, restoration, downstream invalidation. |

### CI requirements

A meaningful lane must replace echo-only workflow jobs with actual checks for:

- README/link/metadata validation;
- YAML safe parsing and schema validation;
- semantic/profile validation;
- fixture and negative-case tests;
- spec-to-consumer compatibility;
- source-role, time, historic/cultural, operational, graph, and lifecycle boundaries;
- no-secret and no-network validation;
- deterministic output and rollback tests.

A green TODO workflow is not evidence of enforceability.

[Back to top](#top)

---

<a id="review-migration-and-change-discipline"></a>

## Review, migration, and change discipline

### Review burden

At minimum, changes require:

- pipeline-spec and executable-pipeline review;
- Roads/Rail/Trade domain review;
- source and rights review when sources change;
- temporal review for status-bearing profiles;
- cultural/Archaeology review for Indigenous or protected historic corridors;
- infrastructure/security review for sensitive facilities;
- graph review for topology or route derivation;
- evidence, policy, validation, and release review for public-facing consequences.

### Compatibility

A breaking spec change must identify:

- prior and next spec versions/digests;
- affected consumers and compatible versions;
- source descriptor and policy dependencies;
- stage/state changes;
- receipt/proof/release consequences;
- migration fixtures and negative tests;
- deactivation and rollback order.

### Slug and topology migration

No README edit may settle:

- `roads-rail-trade` versus `transport`;
- `domains/` versus flat schema/contract lanes;
- subtype-first versus domain-first source registries;
- `Historic Route` versus `Historic RouteClaim`;
- old versus seven-role source vocabulary.

Resolve each through accepted contracts/ADRs/migration notes, update refs and validators together, preserve compatibility pointers, and define rollback.

### Smallest useful change

Populate one profile only after its consumer, source descriptors, contract/schema, fixtures, tests, owners, activation, and rollback are established. Do not populate all scaffolds at once to create an appearance of completeness.

[Back to top](#top)

---

<a id="correction-deactivation-and-rollback"></a>

## Correction, deactivation, and rollback

### Documentation rollback

Revert the documentation or eventual merge commit, or restore prior blob `049fb6a76a36d6d8858e19be9874aa3ecdef9a23`. Preserve history; do not reset or force-rewrite shared history.

### Specification correction

A wrong active specification should be:

1. suspended through its owning activation surface;
2. prevented from scheduling or binding new runs;
3. linked to a correction/supersession record;
4. assessed for affected runs, receipts, lifecycle outputs, catalogs, graphs, releases, and public artifacts;
5. replaced by a new immutable version if appropriate;
6. revalidated with negative and regression fixtures.

Do not rewrite an active file in place while retaining the same identity/version/digest.

### Rollback is multi-surface

Rolling back a spec file does not automatically roll back:

- source activation;
- already captured RAW material;
- WORK/QUARANTINE/PROCESSED records;
- receipts or proofs;
- catalog or triplet outputs;
- graph projections;
- release manifests;
- public layers or cached responses.

Each affected authority must perform its own governed correction or rollback.

### Immediate rollback triggers

Review and likely rollback are required if a spec:

- executes from file presence or mutable discovery;
- bypasses source descriptors or activation;
- contains secrets or arbitrary endpoints;
- upgrades source roles;
- treats stale operational context as current;
- provides navigation, emergency, legal-access, or rail-operating instructions;
- launders historic precision or bypasses cultural review;
- treats graph edges as source truth;
- writes lifecycle/release artifacts directly;
- creates parallel contract, schema, policy, registry, or release authority;
- allows public clients to consume internal specs directly.

[Back to top](#top)

---

<a id="directory-map"></a>

## Directory map

### Confirmed current lane

```text
pipeline_specs/roads-rail-trade/
├── README.md
├── ingest.yaml
├── normalize.yaml
├── validate.yaml
├── catalog.yaml
├── publish.yaml
└── historic_routes.yaml
```

### Responsibility map

```text
pipeline_specs/roads-rail-trade/                  # declarative run intent
pipelines/domains/roads-rail-trade/               # executable behavior
docs/domains/roads-rail-trade/                    # domain doctrine and control docs
contracts/domains/roads-rail-trade/               # observed semantic-contract lane
contracts/transport/                              # compatibility guard
schemas/contracts/v1/domains/roads-rail-trade/    # observed parent domain schema lane
schemas/contracts/v1/transport/                   # compatibility index / empty scaffold
data/registry/sources/roads-rail-trade/           # one source-registry topology candidate
data/registry/roads-rail-trade/sources/           # competing topology candidate
policy/domains/roads-rail-trade/                  # admissibility and obligations
tests/pipeline_specs/roads-rail-trade/            # proposed spec test home; not found at checked path
fixtures/pipeline_specs/roads-rail-trade/         # proposed fixture home; not found at checked path
data/<phase>/roads-rail-trade/                    # lifecycle records
release/                                          # release/correction/rollback authority
```

Compatibility and proposed paths must not be treated as active or canonical merely because this map names them.

[Back to top](#top)

---

<a id="smallest-sound-implementation-sequence"></a>

## Smallest sound implementation sequence

### Gate 0 — ownership and decisions

- [ ] Assign owners and CODEOWNERS coverage.
- [ ] Select one first consumer and stage profile.
- [ ] Decide spec schema/contract home and identity grammar.
- [ ] Resolve or explicitly carry slug and registry-topology conflicts.
- [ ] Define activation-record authority and finite states.
- [ ] Define correction, deactivation, and rollback ownership.

### Gate 1 — accepted inert contract

- [ ] Create semantic contract and machine schema for one profile.
- [ ] Define safe YAML parsing and reference containment.
- [ ] Define digest/canonicalization delegation.
- [ ] Add valid, invalid, edge, and golden fixtures.
- [ ] Prove current empty-stage scaffolds remain inactive.

### Gate 2 — parser and registry

- [ ] Implement deterministic offline parsing.
- [ ] Reject duplicate identities, unsafe references, and unsupported fields.
- [ ] Produce typed validation results.
- [ ] Build an inspectable registry from explicit accepted inputs.
- [ ] Add unit/property/security tests.

### Gate 3 — one consumer binding

- [ ] Bind one exact spec version to one consumer version.
- [ ] Preserve no-network validation.
- [ ] Prove unsupported versions fail closed.
- [ ] Add parity tests for dry-run and negative outcomes.

### Gate 4 — sources, time, and lifecycle

- [ ] Bind admitted SourceDescriptor refs.
- [ ] Enforce role, rights, authority, activation, and freshness.
- [ ] Enforce valid/effective/retrieval times.
- [ ] Enforce input/output lifecycle and quarantine behavior.

### Gate 5 — domain safety

- [ ] Add historic-route uncertainty and overprecision denial.
- [ ] Add cultural/Indigenous review requirements.
- [ ] Add operational/no-navigation and legal-access denial tests.
- [ ] Add infrastructure exposure and graph-derived-only tests.

### Gate 6 — receipts and evidence

- [ ] Define required receipt/ref vocabulary.
- [ ] Resolve EvidenceRefs to EvidenceBundles where required.
- [ ] Preserve policy decisions and obligations.
- [ ] Prove a run cannot self-authorize release.

### Gate 7 — activation and operations

- [ ] Implement external activation/suspension/retirement records.
- [ ] Add expiry and stale-dependency handling.
- [ ] Add observability without sensitive logging.
- [ ] Exercise correction and rollback drills.

### Gate 8 — CI and release integration

- [ ] Replace TODO workflow jobs with substantive checks.
- [ ] Verify required checks and ownership.
- [ ] Integrate one release-readiness flow without publication authority.
- [ ] Document compatibility, deprecation, and restoration evidence.

[Back to top](#top)

---

<a id="definition-of-done"></a>

## Definition of done

### This README revision

- [x] Records current checked inventory rather than a proposed empty tree.
- [x] Classifies all six YAML files conservatively.
- [x] Preserves the `pipeline_specs/` versus `pipelines/` split.
- [x] Corrects contract/schema placement certainty using current repository evidence.
- [x] Keeps source-registry topology and terminology conflicts visible.
- [x] Defines activation, source-role, time, lifecycle, historic/cultural, operational, graph, evidence, receipt, release, correction, and rollback boundaries.
- [x] Does not change or activate YAML files.

### A future active specification

- [ ] Has accepted contract/schema, stable identity, digest, state, owner, and lineage.
- [ ] Binds one compatible executable consumer.
- [ ] References admitted active source descriptors and explicit roles.
- [ ] Enforces rights, authority, time, freshness, lifecycle, quarantine, and safety.
- [ ] Preserves historic uncertainty and cultural/infrastructure review.
- [ ] Preserves graph-derived-only and no-operational-instruction boundaries.
- [ ] Has valid/invalid/edge/golden fixtures and deterministic tests.
- [ ] Requires evidence, policy, review, receipts, release blockers, correction, and rollback.
- [ ] Is activated externally through an auditable binding.
- [ ] Has substantive CI and a tested deactivation/rollback path.

[Back to top](#top)

---

<a id="open-verification-register"></a>

## Open verification register

| ID | Verification item | Status | Evidence required |
|---|---|---:|---|
| RRT-SPEC-001 | Assign lane owners | **NEEDS VERIFICATION** | Maintainer assignment. |
| RRT-SPEC-002 | Confirm CODEOWNERS coverage | **UNKNOWN** | CODEOWNERS inspection/settings. |
| RRT-SPEC-003 | Confirm exhaustive direct inventory | **NEEDS VERIFICATION** | Recursive tree listing. |
| RRT-SPEC-004 | Accept spec semantic contract | **UNKNOWN** | Contract review. |
| RRT-SPEC-005 | Accept machine schema | **UNKNOWN** | Schema, fixtures, validator. |
| RRT-SPEC-006 | Define safe YAML parser | **UNKNOWN** | Source/tests/security review. |
| RRT-SPEC-007 | Define spec registry/index | **UNKNOWN** | Accepted object/home. |
| RRT-SPEC-008 | Define spec ID/version grammar | **UNKNOWN** | Contract/ADR/tests. |
| RRT-SPEC-009 | Define canonical digest rules | **UNKNOWN** | Canonicalization/hash decision. |
| RRT-SPEC-010 | Define finite state model | **UNKNOWN** | Contract/schema/tests. |
| RRT-SPEC-011 | Define activation-record authority | **UNKNOWN** | ADR/register/workflow. |
| RRT-SPEC-012 | Confirm first consumer | **UNKNOWN** | Executable integration. |
| RRT-SPEC-013 | Confirm stage compatibility model | **UNKNOWN** | Version matrix/tests. |
| RRT-SPEC-014 | Prove empty stages remain inactive | **NEEDS VERIFICATION** | Parser negative tests. |
| RRT-SPEC-015 | Resolve contract path conflict | **CONFLICTED** | ADR/migration. |
| RRT-SPEC-016 | Resolve schema path conflict | **CONFLICTED** | ADR/migration. |
| RRT-SPEC-017 | Resolve source-registry topology | **CONFLICTED** | Registry ADR/migration. |
| RRT-SPEC-018 | Resolve Historic Route terminology | **CONFLICTED** | Contract/ADR. |
| RRT-SPEC-019 | Resolve source-role vocabulary | **CONFLICTED** | Accepted role contract/mapping. |
| RRT-SPEC-020 | Confirm active source descriptors | **UNKNOWN** | Registry and activation records. |
| RRT-SPEC-021 | Confirm rights/current terms | **UNKNOWN** | Source review. |
| RRT-SPEC-022 | Define freshness/stale policy | **UNKNOWN** | Contract/tests. |
| RRT-SPEC-023 | Define temporal field profile | **UNKNOWN** | Time contract/schema. |
| RRT-SPEC-024 | Define lifecycle transition profile | **UNKNOWN** | Pipeline/lifecycle tests. |
| RRT-SPEC-025 | Define quarantine reasons | **UNKNOWN** | Finite reason registry. |
| RRT-SPEC-026 | Define historic uncertainty carrier | **CONFLICTED** | UncertaintySurface/Profile decision. |
| RRT-SPEC-027 | Implement overprecision denial | **UNKNOWN** | Validator/tests. |
| RRT-SPEC-028 | Implement cultural review gate | **UNKNOWN** | Policy/steward tests. |
| RRT-SPEC-029 | Implement infrastructure exposure gate | **UNKNOWN** | Policy/security tests. |
| RRT-SPEC-030 | Implement no-navigation boundary | **UNKNOWN** | Negative integration tests. |
| RRT-SPEC-031 | Implement legal-access denial | **UNKNOWN** | Policy/consumer tests. |
| RRT-SPEC-032 | Define graph identity/lineage | **UNKNOWN** | Graph contract/tests. |
| RRT-SPEC-033 | Enforce graph-derived-only posture | **UNKNOWN** | Validator/consumer tests. |
| RRT-SPEC-034 | Define evidence requirements | **UNKNOWN** | Evidence contract/resolver tests. |
| RRT-SPEC-035 | Define policy requirements/outcomes | **UNKNOWN** | Policy mapping/tests. |
| RRT-SPEC-036 | Define receipt vocabulary | **UNKNOWN** | Contracts/schemas/emitters. |
| RRT-SPEC-037 | Define catalog/triplet closure | **UNKNOWN** | Catalog/graph tests. |
| RRT-SPEC-038 | Define release-readiness handoff | **UNKNOWN** | Release integration. |
| RRT-SPEC-039 | Create dedicated fixtures | **NOT FOUND** | Fixture files/review. |
| RRT-SPEC-040 | Create dedicated tests | **NOT FOUND** | Test files/results. |
| RRT-SPEC-041 | Replace TODO domain workflow | **NEEDS VERIFICATION** | Substantive workflow jobs. |
| RRT-SPEC-042 | Confirm required-check enforcement | **UNKNOWN** | Repository settings. |
| RRT-SPEC-043 | Define compatibility/deprecation | **UNKNOWN** | Version policy/migration tests. |
| RRT-SPEC-044 | Define correction propagation | **UNKNOWN** | Correction workflow/drill. |
| RRT-SPEC-045 | Define deactivation/suspension | **UNKNOWN** | Activation system tests. |
| RRT-SPEC-046 | Test software/data rollback | **UNKNOWN** | Rollback drill evidence. |
| RRT-SPEC-047 | Confirm emitted receipts/proofs | **UNKNOWN** | Runtime artifacts. |
| RRT-SPEC-048 | Confirm release/deployment use | **UNKNOWN** | Release/deployment evidence. |

README edits do not upgrade these statuses.

[Back to top](#top)

---

<a id="drift-and-conflicts"></a>

## Drift and conflicts

| Topic | Observed state | Risk | Required posture |
|---|---|---|---|
| Lane maturity | Six YAML scaffolds; no active contract | File presence overread as implementation | Record exact state and activation rule. |
| Contract path | Domain lane plus flat compatibility guard | Parallel semantic authority | ADR/migration; exact refs only. |
| Schema path | Domain lane plus flat compatibility index | Validation drift | ADR/migration; exact refs only. |
| Source registry | Subtype-first and domain-first paths | Split admission authority | One record family; migration/index. |
| Historic terminology | Historic Route / Historic RouteClaim | Meaning loss | Preserve conflict until contract decision. |
| Source roles | Seven-role catalog and older alternate vocabularies | Role upcast/downcast | Versioned mapping or one accepted model. |
| Stage stubs | `stages: []` | Implicit defaults/activation | Inactive until contract and activation. |
| Historic placeholder | Planning pointer only | Treated as profile | Require full contract and review. |
| Workflow | Echo-only TODO jobs | Green checks overread | Replace with substantive validation. |
| Operational context | Closures/restrictions/access | Safety/legal misuse | Official source/time + deny/redirect. |
| Graph projection | Derived nodes/edges | Routing or truth collapse | Preserve source lineage and no-routing rule. |
| Public release | Spec/readiness flags | Merge treated as publication | Release remains external governed transition. |

When docs, specs, implementation, contracts, schemas, registries, policy, tests, receipts, or runtime disagree: stop activation, preserve exact versions, classify the conflict, use the appropriate authority surface to resolve it, update dependent refs/tests together, and retain rollback.

[Back to top](#top)

---

<a id="maintenance-checklist"></a>

## Maintenance checklist

### Before changing a specification

- [ ] Pin base commit and existing blobs.
- [ ] Verify owners, consumer, schema, contract, registry, and activation state.
- [ ] Inspect current source rights, role, authority, and freshness.
- [ ] Inspect historic/cultural/infrastructure implications.
- [ ] Define compatibility, correction, deactivation, and rollback.
- [ ] Confirm no duplicate spec or parallel authority exists.

### During change

- [ ] Keep one primary responsibility and one stable identity.
- [ ] Avoid hidden defaults and dynamic discovery.
- [ ] Preserve source roles, times, rights, uncertainty, and lineage.
- [ ] Keep operational and graph boundaries explicit.
- [ ] Add valid, invalid, edge, and regression fixtures.
- [ ] Keep specs free of secrets and sensitive payloads.

### Before review

- [ ] Run safe YAML, schema, semantic, reference, and security validation.
- [ ] Run source/time/lifecycle/historic/operational/graph negative tests.
- [ ] Verify exact consumer compatibility.
- [ ] Inspect final changed paths and remote blobs.
- [ ] Record evidence, unresolved conflicts, and non-goals.

### Before activation or release use

- [ ] Confirm external activation binding and expiry.
- [ ] Confirm source activation and policy obligations.
- [ ] Confirm evidence and receipt requirements.
- [ ] Confirm public-safe transforms and steward review.
- [ ] Confirm correction, withdrawal, and rollback targets.
- [ ] Do not equate merge, workflow success, or `SPEC_VALID` with release.

[Back to top](#top)

---

<a id="evidence-ledger"></a>

## Evidence ledger

| Evidence | Status | Supports | Does not support |
|---|---:|---|---|
| Target README v0.1 | **CONFIRMED** | Prior documentation lineage. | Current implementation maturity. |
| Five root YAML files | **CONFIRMED inert** | Stage scaffold presence. | Active stages or consumer. |
| `historic_routes.yaml` | **CONFIRMED placeholder** | Planning lineage. | Active historic-route profile. |
| Pipeline Specs root README | **CONFIRMED root contract** | Declarative what/how split. | Parser or activation. |
| Executable pipeline README | **CONFIRMED docs boundary** | Intended implementation home. | Executable behavior. |
| Domain dossier | **CONFIRMED doctrine** | Scope, ownership, sensitivity, object families. | Runtime truth. |
| Canonical Paths / planning docs | **CONFIRMED documents** | Known path conflicts and proposals. | Settled ADR or current canonical winner. |
| Domain contracts README | **CONFIRMED observed lane** | Current semantic-contract path evidence. | Contract completeness. |
| `contracts/transport/` README | **CONFIRMED compatibility guard** | Flat path is not canonical authority. | Resolved slug. |
| Transport schema README | **CONFIRMED compatibility index** | Flat schema posture and empty scaffold. | Validator-ready shape. |
| Source catalog/registry READMEs | **CONFIRMED control docs** | Source-role, rights, topology, safety boundaries. | Active descriptors/current rights. |
| Historic Routes doc | **CONFIRMED doctrine-adjacent** | Claim, uncertainty, cultural review, overprecision posture. | Implemented validator. |
| Domain workflow | **CONFIRMED TODO-only** | Trigger/job names. | Enforceability. |
| Bounded search/path checks | **CONFIRMED bounded** | No parser/tests/selected files surfaced. | Permanent or exhaustive absence. |
| This revision | **CONFIRMED docs-only** | One README change. | Activation, implementation, validation, or release. |

[Back to top](#top)

---

<a id="final-status"></a>

## Final status

**CONFIRMED:** `pipeline_specs/roads-rail-trade/` is a repository-present declarative lane containing this README, five inert root stage scaffolds, and one minimal historic-routes planning placeholder.

**PROPOSED:** evolve one profile at a time into a deterministic, explicit-source, source-role-aware, time-aware, evidence-bound, safety-bounded, externally activated specification after contract, schema, parser, consumer, source, policy, test, receipt, correction, and rollback gates are accepted.

**CONFLICTED:** contract/schema placement, source-registry topology, historic-route terminology, source-role vocabulary, and uncertainty-carrier naming.

**UNKNOWN:** accepted spec API/schema, parser, registry, scheduler, active consumer, active source descriptors, substantive tests/CI, receipts/proofs, release use, deployment, and operational health.

**DO NOT CLAIM:** active specification, source admission, current route/restriction truth, navigation or legal authority, graph truth, evidence closure, policy approval, release approval, publication, or production readiness.

[Back to top](#top)
