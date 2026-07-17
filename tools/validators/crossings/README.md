<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-crossings-readme
title: tools/validators/crossings/ — Generic Crossings Validator Parent and Delegation Boundary
type: readme; directory-readme; validator-parent; crossings; roads-rail-trade; cross-domain-boundary; non-authoritative
version: v0.2
status: draft; repository-grounded; README-only-lane; executable-enforcement-unestablished; child-specialization-confirmed; shared-validator-runtime-confirmed; aggregate-registration-absent; paired-schema-missing; crossings-schema-compatibility-only; domain-policy-greenfield; dedicated-tests-unestablished; domain-ci-todo-only; fail-closed
owners: OWNER_TBD — Validator steward · Roads/Rail/Trade steward · Crossings steward · Hydrology steward · Settlements/Infrastructure steward · Hazards steward · Archaeology/Cultural Heritage reviewer · Graph/topology steward · Source-role steward · Temporal/freshness steward · Geometry steward · Rights/sensitivity reviewer · Evidence steward · Policy steward · Security reviewer · Release steward · Correction/rollback steward · CI steward · Docs steward
created: 2026-07-07
updated: 2026-07-17
supersedes: v0.1 generic crossings validator parent guide
policy_label: "repository-facing; tools; validators; crossings-parent; generic-crossing; transport-side-claim; carried-object; crossed-object; geometry-not-evidence; graph-derived; source-role; temporal-scope; current-status; legal-access; structural-condition; flood-condition; critical-infrastructure; cultural-corridor; archaeology; evidence-aware; policy-aware; release-gated; correction-aware; rollback-aware; no-network-by-default; fail-closed; no-truth-authority; no-routing-authority; no-safety-authority; no-release-authority"
owning_root: tools/
current_path: tools/validators/crossings/README.md
responsibility: >
  Repository-grounded parent, orchestration, and delegation boundary for deterministic checks over generic Roads/Rail/Trade
  Crossing candidates. This lane preserves transport-side claim scope; carried-versus-crossed identity; generic Crossing versus
  Bridge, RiverCrossing, Ferry, transport-facility, route, segment, event, restriction, Hydrology, infrastructure, archaeology,
  hazards, and graph boundaries; source role; temporal and current-status posture; geometry and topology lineage; sensitivity
  and rights; evidence closure; policy obligations; release state; correction lineage; and rollback. It delegates narrow
  specialization checks to accepted child lanes and never becomes crossing truth, bridge or water truth, live routing, legal
  access authority, structural or safe-passage authority, graph truth, policy authority, evidence authority, or publication
  authority.
truth_posture: >
  CONFIRMED target v0.1 README and prior blob; bounded repository reads and direct probes did not confirm a generic crossing
  executable, dedicated crossings test lane, paired crossing schema, structured result producer, aggregate registration, or
  substantive domain CI; tools/validators/bridge_river_crossing/ is the confirmed documented child; tools/validators/domains/roads-rail-trade/ is the confirmed per-domain index; tools/validators/transport-facility-topology/ is an adjacent topology
  boundary; tools/validators/_common/ contains working shared JSON Schema plumbing and a five-entry aggregate that does not
  include crossings; the Crossing semantic contract exists as a draft and records its paired schema as missing; the domain
  schema lane is index-only, schemas/contracts/v1/crossings/ is compatibility/index-only, domain policy is a greenfield
  scaffold, domain tests are documentation-led, and the domain workflow executes TODO-only echo jobs / PROPOSED immutable
  validation packet, parent/child orchestration envelope, finite findings and reason codes, no-network public-safe fixtures,
  security/resource limits, CI admission, correction cascade, migration, deprecation, and rollback / CONFLICTED or drift-prone
  generic parent versus specialization ownership, roads-rail-trade versus transport contract/schema slugs, domain-first versus
  subtype-first source-registry topology, crossings compatibility schema versus domain schema candidates, and duplicate
  Directory Rules homes / NEEDS VERIFICATION owners, canonical executable and registry entry, accepted contracts/schemas,
  source descriptors and rights, policy entrypoints, status/freshness profiles, sensitivity profiles, fixtures/tests,
  structured report destination, CI significance, correction cascade, and release-gate adoption / UNKNOWN runtime invocation,
  production consumers, emitted reports, operational metrics, deployment, current pass results, and branch-protection
  significance
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: "7af05fc50e5a1bab28b314532b0a66d2839a229b"
  prior_blob: 7807275a0afca4aa1518787a392225e2732a6757
  validators_root_blob: e35742288404a1eeb214f8269fbacb1429c0f86a
  shared_runtime_readme_blob: 12df3198498356b32bf309a314eb255604b37415
  shared_run_all_blob: 3375cce172631dc3675cf2e46bb7788d273ff425
  child_specialization_blob: 406360500118414937e1f3e4a839832203712716
  domain_validator_index_blob: 1d5942ab5499cd752974aee804372d89e3c315c0
  topology_validator_blob: 35773f93f2d3a4684e4419719e9e79b724cb06fa
  crossing_contract_blob: a2c2b97da6741d6fa24ad271f2b3fa0a05848ede
  domain_schema_index_blob: 91cd62a640d5a91270564727ff3704a8c236b012
  crossings_schema_index_blob: cf4ef35500c71060065e80b8ce7ae0aac2dc9665
  domain_policy_blob: 508062700bc3f56fb05914290fc160d7634b53f4
  domain_tests_blob: 3c362bf18f228e5b23a533eb4fc0214ca80a614a
  domain_workflow_blob: c6f547b0acd8018284001ed67d25b153c0d9992b
  source_registry_blob: 54087e02e329b98c595807e4c9041c97972c0179
  doctrine_directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  architecture_directory_rules_blob: 18653c00ba193a4afaa3e07a0924452807fb98ef
  schema_home_adr_blob: ab0010a278d766356845c23055f882f328abb418
  drift_register_blob: 97a775522dcd058299f752ac7862d0fc56c13280
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  workflow_readme_blob: c3dfbe1168d405e7244c6a7dacf0e0616faf120e
  generated_receipt_schema_blob: fba21ed27ebccf1362fe397fe0c3ebd85e072685
  bounded_path_checks:
    - tools/validators/crossings/README.md was the confirmed target
    - tools/validators/crossings/validate_crossing_candidate.py returned Not Found
    - tests/validators/crossings/README.md returned Not Found
    - schemas/contracts/v1/domains/roads-rail-trade/crossing.schema.json returned Not Found
    - no AGENTS.md was found at the repository root, tools/, tools/validators/, or tools/validators/crossings/
    - the generic crossings parent was not present in the five-entry shared aggregate
    - no open pull request or branch matching the target crossings README was found in bounded preflight
related:
  - ../README.md
  - ../_common/README.md
  - ../bridge_river_crossing/README.md
  - ../domains/roads-rail-trade/README.md
  - ../transport-facility-topology/README.md
  - ../../../contracts/domains/roads-rail-trade/crossing.md
  - ../../../schemas/contracts/v1/domains/roads-rail-trade/README.md
  - ../../../schemas/contracts/v1/crossings/README.md
  - ../../../policy/domains/roads-rail-trade/README.md
  - ../../../data/registry/sources/roads-rail-trade/README.md
  - ../../../tests/domains/roads-rail-trade/README.md
  - ../../../.github/workflows/domain-roads-rail-trade.yml
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/architecture/directory-rules.md
  - ../../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - ../../../docs/registers/DRIFT_REGISTER.md
  - ../../../.github/CODEOWNERS
  - ../../../data/receipts/generated/README.md
tags: [kfm, tools, validators, crossings, roads-rail-trade, bridge, river-crossing, ferry, hydrology, infrastructure, hazards, archaeology, graph, topology, source-role, time, freshness, sensitivity, evidence, policy, release, correction, rollback]
notes:
  - "This revision changes only tools/validators/crossings/README.md plus the required generated-work provenance receipt."
  - "No validator executable, schema, semantic contract, policy rule, source descriptor, fixture, test, workflow, pipeline, lifecycle object, EvidenceBundle, release record, route status, crossing condition, water condition, graph artifact, model call, or public artifact is created or modified."
  - "The README contains no current conditions, operational guidance, restricted infrastructure detail, precise cultural or archaeological location, private-access detail, hidden policy threshold, or control-defeating value."
  - "A future generic parent must remain thin, delegate shared and specialized checks, and must not duplicate geometry, topology, freshness, evidence, policy, release, or domain meaning."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Generic Crossings Validator Parent and Delegation Boundary

`tools/validators/crossings/`

> **One-line purpose.** Define the deterministic generic-parent boundary for Crossing candidates—preserving transport-side claim scope, carried-versus-crossed identity, source role, time/current-status posture, geometry and graph derivation, specialization ownership, sensitivity, evidence, policy, release, correction, and rollback without becoming crossing truth, bridge or water truth, live routing, legal-access authority, safety authority, graph truth, or publication authority.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Version: v0.2" src="https://img.shields.io/badge/version-v0.2-informational">
  <img alt="Root: tools" src="https://img.shields.io/badge/root-tools%2F-blue">
  <img alt="Role: generic parent" src="https://img.shields.io/badge/role-generic__parent-blueviolet">
  <img alt="Implementation: README only" src="https://img.shields.io/badge/implementation-README__only-orange">
  <img alt="Schema: missing" src="https://img.shields.io/badge/paired__schema-missing-red">
  <img alt="CI: TODO only" src="https://img.shields.io/badge/domain__CI-TODO__only-red">
  <img alt="Boundary: not live routing" src="https://img.shields.io/badge/boundary-not__live__routing-critical">
  <img alt="Posture: cite or abstain" src="https://img.shields.io/badge/posture-cite__or__abstain-success">
</p>

> [!IMPORTANT]
> **Generic crossing enforcement is not established.** The checked lane contains this README; no generic crossing executable, dedicated test package, paired `crossing.schema.json`, structured result producer, or aggregate registration was confirmed.

> [!CAUTION]
> **Geometry, proximity, and topology are not crossing evidence.** A line intersection, shared coordinate, nearest-neighbor result, network node, graph edge, map label, OCR result, model output, or generated explanation cannot by itself prove a Crossing, Bridge, RiverCrossing, Ferry, grade separation, legal access, current passage, or transport relationship.

> [!WARNING]
> **This lane is never navigation, structural, access, or emergency authority.** It must deny or abstain from safe-passage, bridge-condition, load/clearance, fordability, water-depth/flow, flood state, navigability, legal access, right-of-way, current closure, service availability, emergency routing, and operational-status claims unless a separate governed authoritative path supports the exact requested use. Validator success still does not authorize that use.

**Quick links:** [Purpose](#purpose) · [Status](#status-and-evidence) · [Placement](#directory-rules-and-authority) · [Inventory](#confirmed-repository-inventory) · [Topology](#validator-topology-and-delegation) · [Language](#bounded-context-and-ubiquitous-language) · [Packet](#validation-input-packet) · [Invariants](#generic-crossing-validation-invariants) · [Families](#object-family-and-specialization-anti-collapse) · [Geometry](#geometry-topology-and-graph-boundary) · [Time](#source-role-time-and-freshness) · [Operational](#operational-safety-routing-and-access-boundary) · [Sensitivity](#sensitivity-rights-and-public-surface-boundary) · [Report](#validation-report-contract) · [Outcomes](#finite-outcomes-and-reason-codes) · [Maturity](#contract-schema-policy-source-and-test-maturity) · [Security](#security-untrusted-content-and-resource-limits) · [Lifecycle](#lifecycle-release-correction-and-rollback) · [Tests](#tests-fixtures-and-no-network-posture) · [CI](#ci-admission-contract) · [Implementation](#smallest-sound-implementation-sequence) · [Done](#definition-of-done) · [Migration](#migration-compatibility-and-deprecation) · [Open](#open-verification-register) · [Rollback](#rollback-path) · [Ledger](#evidence-ledger) · [Changelog](#changelog)

**Repository references:** [`tools/validators/`](../README.md) · [shared validator runtime](../_common/README.md) · [Bridge/RiverCrossing child](../bridge_river_crossing/README.md) · [Roads/Rail/Trade validator index](../domains/roads-rail-trade/README.md) · [transport-facility topology](../transport-facility-topology/README.md) · [Crossing contract](../../../contracts/domains/roads-rail-trade/crossing.md) · [domain schema index](../../../schemas/contracts/v1/domains/roads-rail-trade/README.md) · [crossings schema compatibility index](../../../schemas/contracts/v1/crossings/README.md) · [domain policy scaffold](../../../policy/domains/roads-rail-trade/README.md) · [source registry](../../../data/registry/sources/roads-rail-trade/README.md) · [domain tests](../../../tests/domains/roads-rail-trade/README.md) · [domain workflow](../../../.github/workflows/domain-roads-rail-trade.yml) · [Directory Rules doctrine](../../../docs/doctrine/directory-rules.md) · [Directory Rules architecture copy](../../../docs/architecture/directory-rules.md) · [ADR-0001](../../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) · [drift register](../../../docs/registers/DRIFT_REGISTER.md) · [CODEOWNERS](../../../.github/CODEOWNERS) · [generated receipt lane](../../../data/receipts/generated/README.md)

---

<a id="purpose"></a>

## Purpose

`tools/validators/crossings/` is the generic parent boundary for deterministic validation of source-scoped transport Crossing candidates.

The durable question is:

> Does the candidate remain a properly typed and evidenced transport-side crossing claim, with explicit carried and crossed objects, preserved source role and time, evidence-supported geometry and topology, correct specialization routing, safe sensitivity posture, and complete policy/release/correction/rollback support for the requested use?

This lane may eventually orchestrate checks for:

- generic road–road, road–rail, rail–rail, route–route, trail, water, grade-separated, historic, administrative, observed, modeled, candidate, and synthetic crossing claims;
- carried and crossed object identity;
- generic Crossing versus Bridge, RiverCrossing, Ferry, tunnel, culvert-like passage, facility, route, membership, event, restriction, node, and edge separation;
- source role, authority limits, rights, citation, cadence, and source vintage;
- source time, observed or asserted time, valid or effective time, retrieval time, status time, release time, correction time, and stale state;
- geometry role, spatial support, uncertainty, topology derivation, and graph lineage;
- EvidenceRef/EvidenceBundle, PolicyDecision, ReviewRecord, validation receipt, ReleaseManifest, CorrectionNotice, WithdrawalNotice, and rollback linkage;
- public map, tile, API, search, graph, Focus Mode, export, screenshot, embedding, and AI carrier boundaries.

It must not:

- define Crossing, Bridge, RiverCrossing, Ferry, Hydrology, infrastructure, route, segment, or graph meaning;
- infer a crossing merely from geometry, topology, labels, OCR, or model output;
- decide structural condition, passability, access, closure, flood state, navigability, or safety;
- create SourceDescriptors, EvidenceBundles, PolicyDecisions, receipts, proofs, or release records;
- materialize graph truth or route guidance;
- publish or approve a public artifact.

[Back to top](#top)

---

<a id="status-and-evidence"></a>

## Status and evidence

### Confirmed snapshot

| Surface | Current-session finding | Truth label |
|---|---|---|
| `tools/validators/crossings/README.md` | v0.1 existed at blob `7807275a0afca4aa1518787a392225e2732a6757`. | **CONFIRMED** |
| Direct lane inventory | The checked target and direct probes established a README-only generic lane. | **CONFIRMED**, bounded |
| Generic executable | `tools/validators/crossings/validate_crossing_candidate.py` returned Not Found. | **NOT FOUND in direct probe** |
| Structured result producer | No generic `CROSSINGS_VALIDATION` producer was confirmed. | **NOT CONFIRMED** |
| Dedicated tests | `tests/validators/crossings/README.md` returned Not Found. | **NOT FOUND in direct probe** |
| Paired Crossing schema | `schemas/contracts/v1/domains/roads-rail-trade/crossing.schema.json` returned Not Found. | **NOT FOUND in direct probe** |
| Generic Crossing contract | `contracts/domains/roads-rail-trade/crossing.md` exists as draft v0.2 and explicitly records the paired schema as missing. | **CONFIRMED draft contract** |
| Child specialization | `tools/validators/bridge_river_crossing/README.md` exists as the documented Bridge/RiverCrossing child; enforcement remains unestablished. | **CONFIRMED README-only child** |
| Domain parent | `tools/validators/domains/roads-rail-trade/README.md` exists as a per-domain index. | **CONFIRMED README-only index** |
| Adjacent topology lane | `tools/validators/transport-facility-topology/README.md` exists as an adjacent topology/facility boundary. | **CONFIRMED README** |
| Shared validator runtime | `_common/` contains executable local schema resolution, Draft 2020-12 validation, fixture mode, and a five-entry aggregate. | **CONFIRMED adjacent implementation** |
| Aggregate registration | The hard-coded aggregate does not include a crossings entrypoint. | **CONFIRMED absent from inspected list** |
| Domain schema lane | Index exists and records no concrete Roads/Rail/Trade schema in its checked inventory. | **CONFIRMED index / schema implementation absent in checked inventory** |
| Crossings schema lane | `schemas/contracts/v1/crossings/` is compatibility/index-only and warns against parallel schema authority. | **CONFIRMED compatibility README** |
| Domain policy | `policy/domains/roads-rail-trade/README.md` is a PROPOSED greenfield scaffold. | **CONFIRMED file / enforcement PROPOSED** |
| Domain tests | Documentation-led test parent and children exist; executable crossing behavior and pass rates were not established. | **CONFIRMED docs / execution NEEDS VERIFICATION** |
| Domain workflow | Three jobs execute `echo TODO ...` only. | **CONFIRMED** |
| Source registry | Roads/Rail/Trade source registry documentation exists, but registry topology and active descriptors remain unresolved. | **CONFIRMED docs / active records NEEDS VERIFICATION** |
| Runtime use and current results | No runtime consumer, emitted crossing validation report, deployment, metric, or current result was inspected. | **UNKNOWN** |

### What this revision establishes

This README establishes a repository-grounded parent boundary, delegation model, finite-result vocabulary, and implementation acceptance contract.

It does **not** establish executable enforcement.

### What this revision does not prove

It does not prove:

- a generic crossings package or CLI exists;
- a Crossing schema exists;
- a schema registry accepts a Crossing family;
- source descriptors are active;
- policy evaluation is wired;
- tests or fixtures execute;
- CI blocks on crossing validation;
- graph projections are operational;
- public APIs or maps consume crossing records;
- current crossing, bridge, water, access, restriction, or closure conditions;
- any release is approved.

[Back to top](#top)

---

<a id="directory-rules-and-authority"></a>

## Directory Rules and authority

Directory Rules place durable validators and checker helpers under `tools/`. The existing target therefore remains:

```text
tools/validators/crossings/
```

This path-preserving README revision does not add a canonical root, move authority, create a parallel validator home, or require an ADR.

### Responsibility split

| Responsibility | Owning root or lane | Crossings parent role |
|---|---|---|
| Generic crossing invariants and child orchestration | `tools/validators/crossings/` | Own narrow parent validation and delegation only. |
| Bridge/RiverCrossing specialization | `tools/validators/bridge_river_crossing/` | Delegate specialization checks; do not duplicate. |
| Domain-wide transport validation | `tools/validators/domains/roads-rail-trade/` | Participate as one domain child or parent result. |
| Facility/node/edge topology | `tools/validators/transport-facility-topology/` | Delegate facility and graph-topology concerns. |
| Shared schema mechanics | `tools/validators/_common/` | Reuse accepted mechanics if implementation is admitted. |
| Shared geometry and freshness checks | accepted shared validator lanes | Delegate reusable carrier and stale-state checks. |
| Domain meaning | `docs/domains/...`, `contracts/domains/...` | Consume; never redefine. |
| Machine shape | accepted `schemas/contracts/v1/...` lane | Consume accepted schema refs; do not invent locally. |
| Source admission and authority | `data/registry/sources/...` plus source validators | Check refs and role posture; never admit locally. |
| Hydrology truth | Hydrology docs, contracts, data, and releases | Cite; never absorb water, flow, flood, or ford truth. |
| Infrastructure/place/asset truth | Settlements/Infrastructure homes | Cite; never absorb canonical asset or place authority. |
| Hazard/current event truth | Hazards and source-specific governed lanes | Cite; never become alert or current-condition authority. |
| Archaeology/cultural truth | Archaeology/Cultural Heritage lanes | Cite only under sensitivity and rights policy. |
| Policy decisions | `policy/` and accepted decision stores | Consume decisions; never define hidden policy. |
| Evidence, proofs, and receipts | `data/proofs/`, `data/receipts/` | Resolve or verify refs; never store instances here. |
| Lifecycle records | `data/` lifecycle roots | Never use validator source path as data storage. |
| Release, correction, and rollback | `release/` | Check refs; never approve publication. |
| Executable proof | `tests/`, `fixtures/` | Tests prove behavior; this README is not proof. |
| Public serving | governed applications and released artifacts | No direct public read from this lane. |

### Directory Rules conflict

Two Directory Rules copies are present:

- `docs/doctrine/directory-rules.md`;
- `docs/architecture/directory-rules.md`.

The architecture copy records the placement question as open. This README does not choose between them. Both agree that validators belong under `tools/`, so the target path is not blocked by that document-placement conflict.

### Schema-home conflict

ADR-0001 is still `proposed`. It points domain schemas to `schemas/contracts/v1/domains/<domain>/`, while the repository also contains a compatibility/index-only `schemas/contracts/v1/crossings/` lane and transport/slug lineage.

This README therefore:

- treats `schemas/contracts/v1/domains/roads-rail-trade/crossing.schema.json` as the current candidate named by the semantic contract;
- records the direct probe as Not Found;
- treats `schemas/contracts/v1/crossings/` as compatibility/index-only;
- forbids a validator-local schema copy;
- does not accept ADR-0001 or resolve slug/path drift.

### Denied placement shortcuts

Do not use this directory for:

- semantic contracts;
- JSON Schemas, contexts, or enums;
- source descriptors or source payloads;
- road, rail, route, bridge, ferry, water, infrastructure, access, condition, closure, or restriction records;
- hidden policy thresholds or sensitivity parameters;
- EvidenceBundle, proof, or receipt instances;
- RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data;
- graph/triplet outputs;
- release manifests, corrections, withdrawals, or rollback cards;
- public API, map, tile, route, navigation, emergency, or AI runtime code.

[Back to top](#top)

---

<a id="confirmed-repository-inventory"></a>

## Confirmed repository inventory

### Direct lane

```text
tools/validators/crossings/
└── README.md
```

This is a bounded inventory based on the target read and direct probes. Ignored, generated, unindexed, branch-local, package-local, or external code remains unknown.

### Nearby validator topology

```text
tools/validators/
├── _common/                           # implemented shared JSON Schema mechanics
├── crossings/                         # this generic parent; README only
├── bridge_river_crossing/             # documented child specialization; README only
├── domains/roads-rail-trade/          # documented domain index
└── transport-facility-topology/       # adjacent facility/node/edge boundary
```

Other shared validator lanes exist under the parent index, but a future crossings implementation must verify exact paths and compatibility before importing them.

### Confirmed semantic surfaces

The checked Roads/Rail/Trade contract lane includes a generic `Crossing` semantic contract and adjacent contracts for:

- Bridge;
- RiverCrossing;
- Ferry;
- road and rail segments;
- route, corridor, and membership;
- status and restriction events;
- network nodes and edges;
- transport facilities.

Those contracts remain semantic inputs. Their existence does not establish schemas, validator code, source records, policy enforcement, test coverage, or release readiness.

### Known maturity constraints

- The generic Crossing contract is draft and schema-missing.
- The domain schema lane is an index and did not confirm concrete schemas.
- The generic crossings schema lane is compatibility/index-only.
- Contract and schema slugs retain `roads-rail-trade` versus `transport` drift.
- Source registry topology retains domain-first versus subtype-first drift.
- Policy is a greenfield scaffold.
- Domain tests are primarily documentation-led in the inspected surface.
- The domain workflow does not execute substantive crossing checks.
- Shared validator runtime does not establish registration or coverage for crossings.
- No structured generic crossing validation report was confirmed.

[Back to top](#top)

---

<a id="validator-topology-and-delegation"></a>

## Validator topology and delegation

The generic parent should be a **thin orchestrator**, not a second implementation of every crossing-adjacent rule.

### Delegation map

| Concern | Primary validator or authority lane | Generic parent behavior |
|---|---|---|
| Generic Crossing identity and family | `crossings/` plus accepted contract/schema | Validate generic packet and dispatch. |
| Spatial intersection is not evidence | generic crossing plus shared geometry checks | Require evidence support; never promote an intersection alone. |
| Bridge/RiverCrossing specialization | `bridge_river_crossing/` | Delegate when specialization is declared or required. |
| Facility/node/edge topology | `transport-facility-topology/` | Delegate facility and graph topology checks. |
| Domain-wide Roads/Rail/Trade invariants | `domains/roads-rail-trade/` | Compose or report domain result without redefining it. |
| Schema loading and fixture mechanics | `_common/` or accepted shared runtime | Reuse mechanics; do not fork registry behavior. |
| Source-role validation | source registry and source-role validators | Require valid refs and preserved role. |
| Time/current-status validation | accepted temporal/freshness lane | Require bounded time support; stale cannot masquerade as current. |
| Evidence closure | evidence validators and proof homes | Require resolvable evidence when use requires it. |
| Policy, rights, and sensitivity | policy/rights/sensitivity validators and authority roots | Consume finite decision; never decide locally. |
| Release/correction/rollback | release validators and `release/` | Require refs for public-bound use; never authorize. |
| Public carrier readiness | governed API/map/tile/export validators | Confirm release-bound carrier; never expose directly. |

### Parent/child rule

A child may add stricter requirements. It must not weaken parent invariants.

The parent should reject or hold a packet when:

- a required specialization is not declared;
- a declared specialization has no accepted child validator;
- a child result is missing, stale, incompatible, or malformed;
- a child reports a blocking finding;
- parent and child disagree about object family, source role, time scope, sensitivity, or requested use.

### Proposed orchestration sequence

```text
validate packet envelope
  -> resolve declared generic Crossing contract and schema
  -> validate source role, time, identity, and evidence references
  -> validate generic object-family separation
  -> dispatch required specialization and shared checks
  -> reconcile parent and child findings
  -> evaluate policy/release/correction/rollback references for requested use
  -> emit one deterministic parent report
```

This sequence is **PROPOSED**. No current executable or registry binding is claimed.

### Idempotence and side effects

A future parent validator should:

- be deterministic for the same pinned inputs and validator configuration;
- perform no network calls by default;
- make no repository writes in validation mode;
- create no lifecycle transition;
- create no policy or release decision;
- expose no sensitive payload in logs;
- return a finite result and nonzero process status for blocking validation failures.

[Back to top](#top)

---

<a id="bounded-context-and-ubiquitous-language"></a>

## Bounded context and ubiquitous language

The terms below are repository-facing validator language. Contract and schema authority still live elsewhere.

| Term | Bounded meaning in this README |
|---|---|
| `Crossing` | A source-scoped transport-side relation claiming that carried and crossed objects meet, intersect, pass over or under, or otherwise require a governed relationship. |
| carried object | The road, rail, trail, route, corridor, or transport feature carried through or across the crossing. |
| crossed object | The road, rail, route, water feature, landscape barrier, facility relation, or other object crossed. |
| crossing family | Generic classification such as road–road, road–rail, rail–rail, water, trail, grade separation, historic, administrative, observed, modeled, candidate, synthetic, or unknown. |
| crossing mode | At-grade, overpass, underpass, bridge, ferry, ford, tunnel, culvert-like, source-specific, modeled, or unknown—subject to contract/schema acceptance. |
| specialization | A narrower object or validator lane, such as Bridge, RiverCrossing, Ferry, facility topology, or access/status event. |
| generic parent | The thin orchestrator that enforces generic Crossing invariants and delegates specialized checks. |
| child result | A versioned, input-bound result emitted by a required specialization or shared validator. |
| source role | The admitted role of the source material; processing and display must not upcast it. |
| valid time | When the asserted crossing relation is intended to apply. |
| retrieval time | When KFM retrieved the source material. |
| status time | When a status or restriction was observed or asserted; not interchangeable with valid time. |
| stale state | A state in which current-use support is outside the accepted freshness profile or cannot be confirmed. |
| geometry role | Point, line, polygon, centroid, envelope, source trace, generalized geometry, or derived support as declared by accepted shape. |
| graph projection | A downstream node/edge representation derived from source-bound crossing evidence. |
| requested use | The bounded operation being evaluated, such as internal normalization, catalog candidate, public map, export, Focus Mode, or AI answer. |
| public-bound | A candidate that could reach a public or semi-public carrier and therefore requires evidence, policy, review, release, correction, and rollback support appropriate to significance. |
| blocking finding | A deterministic finding that prevents the requested use until corrected, narrowed, reviewed, or denied. |
| `ABSTAIN` | The validator cannot safely determine conformance from available accepted inputs. |
| `DENY` | The requested use is prohibited by policy, authority boundary, or unsupported operational/safety claim. |
| `ERROR` | The validator could not safely complete because of operational or input-processing failure. |

Do not invent new synonyms that collapse Crossing, Bridge, RiverCrossing, Ferry, facility, route, segment, node, edge, status, and restriction objects.

[Back to top](#top)

---

<a id="validation-input-packet"></a>

## Validation input packet

A future generic parent should accept an immutable, versioned packet or equivalent explicit arguments. The exact machine shape remains **PROPOSED** until accepted schemas and implementation exist.

### Minimum packet fields

| Field | Purpose | Required posture |
|---|---|---|
| `packet_version` | Version the validation request envelope. | Required. |
| `request_id` | Deterministic or traceable request identifier. | Required; not a truth identifier. |
| `candidate_ref` or `candidate` | The Crossing candidate or immutable content reference. | Required; raw sensitive payload should not be echoed. |
| `candidate_digest` | Digest of the exact candidate bytes or canonical form. | Required when deterministic comparison is expected. |
| `crossing_family` | Generic family under evaluation. | Required or result `ABSTAIN`/finding. |
| `crossing_mode` | Declared mode or explicit unknown. | Required where the contract demands it. |
| `carried_object_ref` | Carried transport object reference. | Required when applicable. |
| `crossed_object_ref` | Crossed object reference. | Required when applicable. |
| `source_ref` | SourceDescriptor or registry reference. | Required. |
| `source_role` | Accepted source role. | Required and immutable through validation. |
| `source_time` | Source publication or assertion time where material. | Required by source profile. |
| `valid_time` | Valid or effective interval. | Required where material. |
| `retrieval_time` | Retrieval timestamp. | Required for retrievable sources. |
| `status_time` | Time of status/restriction observation, if present. | Separate from valid time. |
| `geometry_role` | Declared spatial support. | Required when geometry is supplied. |
| `geometry_digest` | Digest of normalized geometry or carrier. | Required when geometry participates in identity or comparison. |
| `evidence_refs` | EvidenceRef/EvidenceBundle references. | Required for consequential or public-bound use. |
| `policy_decision_ref` | PolicyDecision reference. | Required when policy applies. |
| `review_record_ref` | Review record reference. | Required where policy or significance requires review. |
| `release_manifest_ref` | Governing release reference. | Required for released/public-bound use. |
| `correction_ref` | Correction or supersession lineage. | Required when applicable. |
| `rollback_ref` | Rollback target or card. | Required for public-bound release. |
| `requested_use` | Exact operation being evaluated. | Required. |
| `child_requirements` | Required child validators and expected versions. | Required when specialization or shared checks apply. |
| `limits` | Accepted resource and payload limits. | Required by execution profile. |

### Input rules

The parent must fail closed or abstain when:

- the packet version is unsupported;
- required refs cannot be resolved locally under the selected profile;
- digests do not match;
- source role or time fields conflict;
- the requested use is broader than the evidence, policy, or release scope;
- sensitive or restricted material is embedded when only refs are allowed;
- a required child validator version is unavailable;
- the packet asks the validator to make a policy, release, legal, safety, or emergency decision.

### Untrusted content

All candidate labels, descriptions, metadata, OCR output, model output, source text, graph text, and embedded instructions are untrusted task data.

A validator must not:

- execute embedded instructions;
- treat a source-provided “approved”, “safe”, “public”, or “current” string as authority;
- follow candidate URLs in no-network mode;
- interpolate candidate text into shell commands;
- write candidate-controlled paths;
- expose candidate payloads in logs without redaction.

[Back to top](#top)

---

<a id="generic-crossing-validation-invariants"></a>

## Generic Crossing validation invariants

### GCR-01 — Transport-side scope

A generic Crossing record represents a transport-side relation. It does not replace Hydrology, infrastructure, property, legal access, hazard, structural, or operational truth.

**Blocking conditions:**

- canonical water or infrastructure claims are embedded without owning-domain refs;
- a Crossing is used as the sole proof of a bridge, ford, ferry, tunnel, facility, or safe passage;
- the candidate claims publication or policy authority.

### GCR-02 — Carried and crossed objects remain explicit

Where the crossing semantics depend on two objects, carried and crossed roles must be explicit and must not silently swap.

**Blocking conditions:**

- both refs are missing;
- both refs point to the same object without a justified self-intersection contract;
- carried and crossed roles conflict with the declared family;
- the same field is overloaded for segment, route, facility, and graph identity.

### GCR-03 — Spatial intersection is not evidence

Geometry may support or locate a claim. It cannot establish a crossing by itself.

**Blocking conditions:**

- candidate provenance is only a spatial operation without source evidence;
- an overlap, nearest point, snapped node, raster crossing, or inferred label is presented as confirmed;
- uncertainty or method is omitted for modeled/candidate geometry.

### GCR-04 — Object families do not collapse

Crossing, Bridge, RiverCrossing, Ferry, RoadSegment, RailSegment, CorridorRoute, RouteMembership, TransportFacility, NetworkNode, NetworkEdge, AccessRestriction, StatusEvent, and RestrictionEvent remain distinct.

**Blocking conditions:**

- one identifier is reused as canonical identity across incompatible families;
- a graph node/edge replaces the source Crossing;
- status or restriction fields are embedded as timeless Crossing truth;
- a generic Crossing silently upgrades to a Bridge or RiverCrossing.

### GCR-05 — Source role is immutable

Observed, regulatory, administrative, modeled, aggregate, candidate, contextual, synthetic, historic, and restricted roles must not be upgraded by processing, graph projection, rendering, cataloging, or generated language.

**Blocking conditions:**

- role is absent;
- role is incompatible with the requested claim;
- a modeled/candidate record is labeled observed or authoritative;
- a contextual source is the only support for a consequential public claim.

### GCR-06 — Time kinds stay separate

Source, observed/asserted, valid/effective, retrieval, status, release, and correction times must remain distinct where material.

**Blocking conditions:**

- current status is inferred from an old source without freshness support;
- historic evidence becomes modern access or passage truth;
- release time is presented as observation time;
- missing temporal scope makes the claim materially ambiguous.

### GCR-07 — Specialization routing is explicit

A candidate requiring Bridge, RiverCrossing, Ferry, facility topology, status/restriction, or another accepted specialization must route to that validator.

**Blocking conditions:**

- required child is absent;
- child version or input digest does not match;
- child finding is ignored;
- parent attempts to reproduce child-specific truth instead of delegating.

### GCR-08 — Graph projection remains downstream

Network nodes and edges may derive from a released or internal Crossing record, but they must cite the source record and remain invalidatable.

**Blocking conditions:**

- graph output lacks source record refs;
- graph output is treated as sovereign Crossing evidence;
- correction/withdrawal cannot cascade to graph derivatives;
- graph topology is used as live routing authority without a separate governed path.

### GCR-09 — Evidence closure matches requested use

Consequential and public-bound uses require resolvable evidence appropriate to significance.

**Blocking conditions:**

- required EvidenceRef/EvidenceBundle support is missing;
- cited evidence does not support the claimed family, object roles, time, or geometry;
- evidence is stale, conflicted, withdrawn, restricted, or outside release scope;
- citation formatting substitutes for evidence closure.

### GCR-10 — Policy, rights, and sensitivity fail closed

Rights, redistribution, sensitivity, legal-access, cultural, infrastructure, and exact-location constraints must be evaluated before exposure.

**Blocking conditions:**

- policy decision is missing where required;
- most-restrictive posture is not propagated;
- public-safe transform or review receipt is missing;
- exact geometry could reveal sensitive infrastructure, cultural/archaeological context, or restricted access.

### GCR-11 — Release, correction, and rollback remain separate

Validator success is not release approval.

**Blocking conditions:**

- public-bound use lacks a release reference;
- no correction/supersession path exists;
- no rollback target exists where release significance requires it;
- candidate attempts to move itself directly to PUBLISHED.

### GCR-12 — Operational claims are denied or narrowed

Crossing validation cannot provide live routing, emergency, legal, structural, safe-passage, closure, flood/ford, navigability, or service advice.

**Blocking conditions:**

- requested use asks for such advice without a separate accepted authority path;
- a stale or historic record is presented as current;
- a generic source is treated as legal or engineering authority;
- a map, graph, or AI carrier presents unsupported operational certainty.

### GCR-13 — Determinism and traceability

The parent result should bind exact inputs, configuration, child results, and validator version.

**Blocking conditions:**

- result cannot identify its input digest;
- child results are not traceable;
- nondeterministic ordering changes the canonical result;
- network or ambient state changes the result without being declared.

### GCR-14 — No hidden side effects

Validation mode must not publish, promote, mutate lifecycle data, create policy decisions, or write unreviewed trust objects.

**Blocking conditions:**

- validator writes to `data/published/`, `release/`, policy decision stores, or canonical data;
- validator fetches live data without an explicit authorized profile;
- validator writes candidate-controlled paths;
- validation success automatically triggers publication.

[Back to top](#top)

---

<a id="object-family-and-specialization-anti-collapse"></a>

## Object-family and specialization anti-collapse

| Object family | Generic parent may validate | Generic parent must not assert | Delegation posture |
|---|---|---|---|
| `Crossing` | Generic family, object refs, source role, time, geometry role, evidence, requested use. | Physical existence or current operational state without evidence. | Parent-owned generic checks. |
| `Bridge` | Presence and compatibility of a bridge ref when declared. | Structural identity, condition, inspection, load, clearance, ownership, or safety. | Bridge/RiverCrossing child plus infrastructure authority. |
| `RiverCrossing` | Presence and compatibility of a river-crossing ref. | Water depth, flow, flood state, fordability, navigability, or hydrology truth. | Bridge/RiverCrossing child plus Hydrology. |
| `Ferry` | Presence and compatibility of a ferry ref. | Service availability, schedule, legal access, capacity, or safety. | Accepted Ferry specialization. |
| `RoadSegment` | Reference type and relation consistency. | Road ownership, legal designation, current closure, or passability. | Domain contract/source/status lanes. |
| `RailSegment` | Reference type and relation consistency. | Rail operating status, authority, current service, or safe crossing. | Domain contract/source/status lanes. |
| `CorridorRoute` | Relation and membership refs. | Canonical route truth or current navigable path. | Route/membership validators. |
| `RouteMembership` | Compatibility and time scope. | Membership without source evidence. | Route/membership validators. |
| `TransportFacility` | Facility-role ref compatibility. | Canonical place/asset identity, condition, ownership, access, or service. | Transport-facility-topology and Settlements/Infrastructure. |
| `NetworkNode` | Traceability to source record and derivation method. | Canonical place or Crossing truth. | Topology/graph validator. |
| `NetworkEdge` | Traceability, invalidation, and use boundary. | Live route, legal access, or sovereign truth. | Topology/graph validator. |
| `StatusEvent` | Reference, time, source role, and freshness compatibility. | Timeless or current status without accepted source. | Status/freshness validator. |
| `RestrictionEvent` | Reference, time, authority, and scope compatibility. | Legal or operational restriction beyond source authority. | Restriction/policy validator. |
| `AccessRestriction` | Existence of governed ref and policy support. | Legal advice, right-of-way, or public access determination. | Policy/legal-source path. |
| `Hydrology` object | Reference and evidence linkage. | Waterbody, stream, flow, flood, or water-condition truth. | Hydrology-owned. |
| infrastructure asset | Reference and sensitivity compatibility. | Canonical asset identity, vulnerability, structural status, or ownership. | Settlements/Infrastructure-owned. |
| archaeology/cultural object | Safe ref and policy compatibility. | Exact location, cultural authority, or public-release permission. | Archaeology/Cultural Heritage-owned. |
| map/tile/API/AI carrier | Release and evidence reference compatibility. | Canonical truth, policy decision, or release approval. | Governed public-surface validators. |

### Unknown or ambiguous families

Unknown is a valid input state. It is not permission to choose the most convenient family.

A future validator should:

1. preserve the source-stated family;
2. record competing candidate families where supported;
3. return `ABSTAIN`, `REVIEW_REQUIRED`, or a blocking finding;
4. avoid minting a specialized canonical object until accepted evidence and review support it.

[Back to top](#top)

---

<a id="geometry-topology-and-graph-boundary"></a>

## Geometry, topology, and graph boundary

### Geometry roles

A Crossing packet may carry:

- source point;
- source line or trace;
- source polygon or footprint;
- generalized public geometry;
- centroid or representative point;
- bounding box;
- uncertainty envelope;
- derived intersection candidate;
- graph node location;
- no geometry.

The role must be explicit. The validator must not treat all geometry as equivalent.

### Generic geometry checks

A future parent may check:

- declared CRS and axis order;
- geometry type compatibility with the accepted schema;
- finite coordinates and valid encoding;
- geometry digest;
- declared precision and uncertainty;
- self-intersection or invalid topology where the representation requires validity;
- spatial support consistent with the source role;
- public-safe generalization reference where policy requires it.

It must not:

- “repair” a geometry in place without a separate transform and receipt;
- infer source authority from precision;
- interpret a graph-node point as source location;
- publish exact coordinates because they pass geometric validity;
- make crossing existence or safety claims from spatial relations alone.

### Topology checks

Topology may support consistency questions such as:

- are carried and crossed refs present;
- do referenced segments exist in the validation packet;
- is a derived node linked to the source Crossing;
- are route memberships time-compatible;
- do bridge/ferry/river refs agree with the declared generic family.

Topology cannot prove:

- legal connectivity;
- current access;
- grade-crossing safety;
- bridge capacity;
- ferry service;
- ford passability;
- emergency route suitability.

### Graph lineage

Every derived node or edge that depends on a Crossing should preserve:

- source Crossing ref;
- input digest;
- projection method/version;
- valid-time scope;
- sensitivity/public-safe transform refs;
- evidence and release refs appropriate to use;
- correction, withdrawal, and rollback invalidation hooks.

A graph result missing those bindings should not be treated as a public-ready carrier.

[Back to top](#top)

---

<a id="source-role-time-and-freshness"></a>

## Source role, time, and freshness

### Source-role preservation

The source role should come from a governed source descriptor or accepted registry record. The validator may check the role but must not assign authority by convenience.

| Role example | Generic interpretation | Prohibited upcast |
|---|---|---|
| observed | Source reports an observed crossing relation under stated method/time. | Current operational status or safety. |
| regulatory | Source carries regulatory or administrative context. | Physical condition or hydrology truth. |
| administrative | Source records an administrative relation or inventory. | Legal access or current passability without authority. |
| modeled | Algorithmic or analytical estimate. | Observed or confirmed crossing. |
| candidate | Candidate requiring evidence/review. | Published Crossing truth. |
| historic | Evidence about a past relation or route. | Modern crossing, access, or service. |
| contextual | Corroborating/background context. | Primary support for consequential claim. |
| synthetic | Test, simulation, or generated input. | Real-world claim. |
| restricted | Source with access, rights, or sensitivity limits. | Public exposure. |

The accepted vocabulary itself remains an external contract/schema/registry concern.

### Time-kind separation

At minimum, do not collapse:

- source publication time;
- observation or assertion time;
- valid/effective interval;
- retrieval time;
- status time;
- release time;
- correction or withdrawal time.

### Current-status rule

A Crossing record is not current merely because:

- it was retrieved recently;
- it appears in a current release;
- its map tile loaded successfully;
- a graph edge exists;
- a source has no end date;
- generated language uses the present tense.

A current-status request should require:

- an accepted freshness profile;
- a source authorized for that status;
- status time and retrieval time;
- stale-state behavior;
- policy/release scope matching the use.

Otherwise the result should narrow to historical/contextual scope, abstain, or deny the operational use.

### Historic crossing rule

Historic evidence must preserve:

- source vintage;
- mapped or described time;
- uncertainty;
- interpretation method;
- source conflicts;
- geometry precision limits;
- non-equivalence to current access or infrastructure.

[Back to top](#top)

---

<a id="operational-safety-routing-and-access-boundary"></a>

## Operational safety, routing, and access boundary

### Always out of scope for generic validation

The parent must not answer or certify:

- whether a crossing is safe;
- whether a bridge is structurally sound;
- load, height, width, speed, or clearance limits;
- whether a ford is passable;
- current water depth, flow, ice, flood, or debris condition;
- whether a ferry is operating;
- whether a road or rail crossing is open;
- legal access, right-of-way, ownership, trespass, or permit status;
- emergency route or evacuation suitability;
- railroad operating instructions;
- navigation directions;
- compliance with engineering, transport, or safety regulation.

### Accepted validator behavior

For such requests, the validator may only:

1. identify that the requested use is outside generic Crossing authority;
2. require a separate accepted source and policy path;
3. return a finite denial or abstention reason;
4. preserve any safe pointer to official channels if a governed public surface supplies one;
5. avoid reproducing restricted details or operational instructions.

### Suggested reason posture

| Request | Generic result |
|---|---|
| “Does this crossing exist in the admitted historical source?” | Validate bounded source claim if evidence/schema exist; otherwise abstain. |
| “Can I drive across it now?” | `DENY_OPERATIONAL_USE` or `ABSTAIN_CURRENT_STATUS`. |
| “Is the bridge safe for this load?” | `DENY_STRUCTURAL_OR_LOAD_AUTHORITY`. |
| “Is the ford safe today?” | `DENY_WATER_AND_SAFE_PASSAGE_AUTHORITY`. |
| “Is this public right-of-way?” | `DENY_OR_ABSTAIN_LEGAL_ACCESS`. |
| “Use the graph edge as a route.” | `DENY_GRAPH_AS_LIVE_ROUTING`. |
| “Publish exact crossing coordinates near a sensitive site.” | `DENY_SENSITIVE_LOCATION_EXPOSURE` unless accepted policy/review/release supports a public-safe transform. |

The reason names are **PROPOSED** until a result schema and registry are accepted.

[Back to top](#top)

---

<a id="sensitivity-rights-and-public-surface-boundary"></a>

## Sensitivity, rights, and public-surface boundary

### Sensitivity categories that may affect crossings

- critical or security-relevant infrastructure;
- restricted rail, utility, military, correctional, emergency, or industrial facilities;
- private access, private roads, gates, easements, and landowner-sensitive context;
- archaeological sites, historic crossings, cultural corridors, sacred places, and Indigenous knowledge;
- rare-species or habitat joins that make sensitive locations reconstructable;
- current operational restrictions or vulnerabilities;
- restricted-source-derived coordinates;
- precise historic-route geometry that overstates evidence.

### Most-restrictive propagation

When a Crossing joins multiple objects or sources, the validator should require the most restrictive applicable rights/sensitivity posture unless an accepted policy decision and transform receipt establish a safe derivative.

A public-safe transform does not erase lineage. It should preserve:

- restricted source refs under controlled access;
- transform method/version;
- input and output digests;
- reason and policy decision;
- reviewer where required;
- spatial support and uncertainty;
- release/correction/rollback refs.

### Public carriers

A passing generic shape check is insufficient for:

- MapLibre layer;
- PMTiles or other tile artifact;
- governed API payload;
- popup or Evidence Drawer item;
- search or catalog result;
- graph/triplet result;
- Focus Mode context;
- screenshot or export;
- AI response.

The validator should require a public-bound packet that proves the carrier is downstream of released, policy-safe, evidence-backed material.

### Reconstruction risk

Generalized points, aggregated counts, graph edges, labels, and narrative text may still reveal an exact location when combined.

A future validator should support a reconstruction-risk finding when:

- public geometry and attributes can be joined back to a restricted source;
- a graph or route sequence reconstructs a hidden corridor;
- a label or description identifies a sensitive crossing;
- an export exposes more precision than the map;
- model-generated text reintroduces redacted details.

[Back to top](#top)

---

<a id="validation-report-contract"></a>

## Validation report contract

No current generic Crossing result schema or producer was confirmed. The shape below is a **PROPOSED** review target.

### Required report properties

| Property | Purpose |
|---|---|
| `report_version` | Version the result envelope. |
| `validator_id` | Stable parent validator identity. |
| `validator_version` | Implementation/config version. |
| `request_id` | Bind result to request. |
| `candidate_ref` | Safe candidate reference. |
| `candidate_digest` | Bind exact input. |
| `requested_use` | State the bounded use evaluated. |
| `started_at` / `completed_at` | Operational trace, not claim time. |
| `outcome` | Finite parent outcome. |
| `findings` | Deterministic ordered findings. |
| `child_results` | Required child result refs/digests/outcomes. |
| `schema_refs` | Accepted schemas used. |
| `contract_refs` | Semantic contracts used. |
| `source_refs` | Source descriptor/registry refs checked. |
| `evidence_refs` | Evidence refs checked, without embedding restricted payloads. |
| `policy_decision_refs` | Policy results consumed. |
| `release_refs` | Release/correction/rollback refs checked. |
| `configuration_digest` | Bind profiles, rule registry, and limits. |
| `errors` | Safe operational errors. |
| `redactions` | Fields omitted from report/log output. |

### Finding shape

Each finding should have:

- stable `code`;
- finite `severity`;
- blocking boolean;
- object field or safe JSON Pointer when applicable;
- short human-readable message;
- machine-readable details without sensitive values;
- owning authority or next review lane;
- cited contract/schema/policy/evidence ref;
- correction suggestion that does not invent truth.

### Finding order

Results should be deterministic. A recommended order is:

1. packet and digest failures;
2. schema and contract binding;
3. source role and time;
4. generic object-family invariants;
5. child/dependency results;
6. evidence;
7. policy/rights/sensitivity;
8. release/correction/rollback;
9. public-carrier and requested-use boundaries;
10. operational errors.

### Report authority

A ValidationReport may prove that declared checks ran over declared inputs. It cannot prove the Crossing is true, safe, public, or approved for release.

[Back to top](#top)

---

<a id="finite-outcomes-and-reason-codes"></a>

## Finite outcomes and reason codes

### Parent outcomes

| Outcome | Meaning |
|---|---|
| `CROSSINGS_VALIDATION_PASS` | All configured checks for the requested use passed. This is not truth or release approval. |
| `CROSSINGS_VALIDATION_FAIL` | One or more blocking findings were produced. |
| `CROSSINGS_VALIDATION_ABSTAIN` | Accepted inputs were insufficient to determine the requested use safely. |
| `CROSSINGS_VALIDATION_DENY` | The requested use is prohibited or outside validator/system authority. |
| `CROSSINGS_VALIDATION_ERROR` | The validator could not safely complete. |
| `CROSSINGS_VALIDATION_REVIEW_REQUIRED` | A governed steward decision is required before the requested use can proceed. |

### Envelope and configuration reasons

| Code | Blocking meaning |
|---|---|
| `PACKET_VERSION_UNSUPPORTED` | Input packet version is unsupported. |
| `CANDIDATE_REF_MISSING` | Candidate or immutable reference is absent. |
| `CANDIDATE_DIGEST_MISMATCH` | Candidate bytes do not match the declared digest. |
| `REQUESTED_USE_MISSING` | Requested operation is not declared. |
| `RESOURCE_LIMIT_EXCEEDED` | Input exceeds accepted size, depth, count, or time limits. |
| `VALIDATOR_CONFIGURATION_UNRESOLVED` | Rule/configuration registry cannot be resolved. |
| `CROSSING_SCHEMA_UNAVAILABLE` | No accepted Crossing schema is available for the requested validation. |
| `CROSSING_CONTRACT_UNRESOLVED` | Required semantic contract cannot be resolved. |

### Identity and family reasons

| Code | Blocking meaning |
|---|---|
| `CROSSING_FAMILY_MISSING` | Generic family is absent or unusably ambiguous. |
| `CROSSING_MODE_INCOMPATIBLE` | Declared mode conflicts with family or refs. |
| `CARRIED_OBJECT_REF_MISSING` | Required carried object is absent. |
| `CROSSED_OBJECT_REF_MISSING` | Required crossed object is absent. |
| `CARRIED_CROSSED_ROLE_CONFLICT` | Carried and crossed roles are inconsistent. |
| `OBJECT_FAMILY_COLLAPSE` | Incompatible object families are merged. |
| `SPECIALIZATION_REQUIRED` | Candidate requires a narrower specialization. |
| `SPECIALIZATION_CONFLICT` | Generic and specialized classifications conflict. |

### Geometry, topology, and graph reasons

| Code | Blocking meaning |
|---|---|
| `SPATIAL_INTERSECTION_NOT_EVIDENCE` | Geometry operation is presented as Crossing proof. |
| `GEOMETRY_ROLE_MISSING` | Spatial support is not declared. |
| `GEOMETRY_DIGEST_MISMATCH` | Geometry does not match its digest. |
| `GEOMETRY_PRECISION_UNSUPPORTED` | Precision exceeds evidence or public-safe scope. |
| `TOPOLOGY_RELATION_UNSUPPORTED` | Topology relation lacks accepted support. |
| `GRAPH_AUTHORITY_COLLAPSE` | Derived graph object replaces source Crossing evidence. |
| `GRAPH_LINEAGE_MISSING` | Node/edge lacks source and projection lineage. |
| `GRAPH_AS_LIVE_ROUTING_DENIED` | Graph is used as live route authority. |

### Source, time, and evidence reasons

| Code | Blocking meaning |
|---|---|
| `SOURCE_REF_MISSING` | Source descriptor/registry ref is absent. |
| `SOURCE_ROLE_MISSING` | Source role is absent. |
| `SOURCE_ROLE_COLLAPSE` | Role is upgraded or conflated. |
| `SOURCE_RIGHTS_UNRESOLVED` | Rights or permitted use is unresolved. |
| `TIME_SCOPE_MISSING` | Material temporal scope is absent. |
| `TIME_KIND_COLLAPSE` | Distinct time kinds are conflated. |
| `STALE_FOR_REQUESTED_USE` | Source/status is too stale for requested use. |
| `HISTORIC_AS_CURRENT_DENIED` | Historic evidence is presented as current. |
| `EVIDENCE_REF_MISSING` | Required evidence reference is absent. |
| `EVIDENCE_UNRESOLVED` | Evidence cannot be resolved. |
| `EVIDENCE_SCOPE_MISMATCH` | Evidence does not support family, time, geometry, or use. |

### Child and dependency reasons

| Code | Blocking meaning |
|---|---|
| `CHILD_VALIDATOR_REQUIRED` | A specialization/shared child must run. |
| `CHILD_VALIDATOR_UNAVAILABLE` | Required child is not implemented or admitted. |
| `CHILD_RESULT_MISSING` | Required child result is absent. |
| `CHILD_RESULT_DIGEST_MISMATCH` | Child result is not bound to the same input. |
| `CHILD_RESULT_STALE` | Child result version/config/input is stale. |
| `CHILD_VALIDATOR_FAILED` | Child reported blocking findings. |
| `PARENT_CHILD_OUTCOME_CONFLICT` | Parent and child results cannot be reconciled. |

### Policy, release, and public-boundary reasons

| Code | Blocking meaning |
|---|---|
| `POLICY_DECISION_MISSING` | Required policy decision is absent. |
| `RIGHTS_OR_SENSITIVITY_DENIED` | Policy denies requested use. |
| `PUBLIC_SAFE_TRANSFORM_MISSING` | Required redaction/generalization receipt is absent. |
| `RECONSTRUCTION_RISK_UNRESOLVED` | Public carrier could reconstruct sensitive detail. |
| `RELEASE_REFERENCE_MISSING` | Required release reference is absent. |
| `CORRECTION_PATH_MISSING` | Correction/supersession path is absent. |
| `ROLLBACK_REFERENCE_MISSING` | Rollback target is absent. |
| `LIFECYCLE_VIOLATION` | Candidate skips a required lifecycle state. |
| `PUBLIC_BOUNDARY_VIOLATION` | Candidate could bypass governed public interfaces. |
| `VALIDATOR_AS_RELEASE_AUTHORITY_DENIED` | Validator success is treated as publication approval. |

### Operational and safety reasons

| Code | Blocking meaning |
|---|---|
| `DENY_LIVE_ROUTING_AUTHORITY` | Requested use requires live route authority. |
| `DENY_CURRENT_CLOSURE_AUTHORITY` | Requested use requires current closure status. |
| `DENY_LEGAL_ACCESS_AUTHORITY` | Requested use asks for legal access/right-of-way. |
| `DENY_STRUCTURAL_OR_LOAD_AUTHORITY` | Requested use asks for structural/load/clearance judgment. |
| `DENY_WATER_OR_FLOOD_AUTHORITY` | Requested use asks for water, ford, flood, or navigability judgment. |
| `DENY_SAFE_PASSAGE_AUTHORITY` | Requested use asks whether passage is safe. |
| `DENY_EMERGENCY_GUIDANCE` | Requested use asks for emergency or evacuation guidance. |
| `DENY_RAIL_OPERATING_AUTHORITY` | Requested use asks for railroad operating instructions/status. |

### Compatibility rule

Reason-code names become stable only after a result schema, registry, tests, and migration policy are accepted. Until then they are **PROPOSED** and must not be consumed as a hidden external API.

[Back to top](#top)

---

<a id="contract-schema-policy-source-and-test-maturity"></a>

## Contract, schema, policy, source, and test maturity

| Surface | Repository-grounded state | Consequence |
|---|---|---|
| Generic Crossing semantic contract | Draft v0.2 exists. | Meaning guidance exists; not accepted machine enforcement. |
| Paired Crossing schema | Direct candidate path returned Not Found. | Generic schema validation cannot be claimed. |
| Domain schema index | README only; checked inventory reports no concrete schema. | Candidate schema work remains future and ADR/slug-aware. |
| Crossings schema compatibility lane | Index-only, canonical status unresolved. | Do not create a duplicate schema there. |
| Generic parent executable | Direct expected path returned Not Found. | README does not imply CLI or package behavior. |
| Shared validator runtime | Executable and CI-invoked for other families. | Reuse is possible, but registration and compatibility require implementation review. |
| Parent aggregate | Five hard-coded validators, none crossings. | `make schemas` does not establish crossing coverage. |
| Bridge/RiverCrossing child | Repository-grounded README-only specialization. | Child design exists; no child enforcement. |
| Domain validator index | README-only parent. | Domain aggregation does not establish runtime. |
| Transport-facility topology lane | README-based adjacent boundary. | No topology executable claimed. |
| Domain policy | Greenfield scaffold. | Policy decisions and enforcement are not established. |
| Source registry | Documentation exists with unresolved topology. | Active descriptors, rights, cadence, and source-role records need verification. |
| Domain tests | Documentation-led lanes. | Dedicated generic crossing fixtures/tests and pass rates are unestablished. |
| Domain workflow | TODO-only echo jobs. | Workflow existence is not enforcement. |
| Release integration | No generic crossing report or release consumer inspected. | Public readiness is UNKNOWN. |

### Promotion threshold for an executable lane

Do not promote the parent beyond README-only maturity until all of these are present and cross-linked:

- accepted generic Crossing semantic contract;
- accepted paired schema in the selected canonical home;
- schema or object registry entry;
- explicit source-role vocabulary and source descriptor examples;
- public-safe valid fixtures;
- negative and malformed fixtures;
- generic parent executable;
- child/dependency registry;
- deterministic report schema;
- policy and sensitivity tests;
- no-network test command;
- CI job invoking the real command;
- documented correction, deprecation, and rollback;
- owner and reviewer assignments;
- proof that public carriers remain downstream of release.

[Back to top](#top)

---

<a id="security-untrusted-content-and-resource-limits"></a>

## Security, untrusted content, and resource limits

### Threat model

Crossing validation may process adversarial or malformed:

- JSON/YAML;
- deeply nested arrays and objects;
- oversized geometries;
- invalid coordinates;
- duplicate or cyclic refs;
- path traversal strings;
- URLs;
- source labels and descriptions;
- OCR or generated text;
- graph payloads;
- metadata that claims approval or public status.

### Required controls for future code

A future implementation should:

- default to local, no-network resolution;
- resolve only within approved repository roots or immutable artifact stores;
- reject path traversal and unsupported URI schemes;
- cap file bytes, geometry coordinates, feature counts, nesting depth, child count, finding count, and runtime;
- use deterministic parsing and ordering;
- reject duplicate identifiers and ambiguous registry entries;
- avoid dynamic imports from candidate values;
- avoid shell interpolation;
- avoid following candidate URLs;
- redact sensitive values from logs;
- emit bounded error messages;
- return nonzero exit status for blocking failure or unsafe error;
- separate validation output from publication or lifecycle writes.

### Sensitive logging

Logs and reports should prefer:

- digests;
- safe object refs;
- field pointers;
- finite codes;
- counts;
- coarse geometry descriptors;
- redaction markers.

They should not contain:

- exact restricted coordinates;
- private access notes;
- critical-infrastructure vulnerability details;
- credentials or private endpoints;
- restricted source payloads;
- hidden policy thresholds;
- living-person or private-land joins;
- full untrusted text when a digest and safe excerpt suffice.

### Dependency and parser posture

Before implementation, verify:

- Python and JSON Schema versions;
- schema dialect;
- format-checking behavior;
- YAML safety if YAML is accepted;
- geospatial parser dependencies and denial-of-service limits;
- local resolver behavior;
- exception and exit-code contract;
- supply-chain and action-pinning posture.

[Back to top](#top)

---

<a id="lifecycle-release-correction-and-rollback"></a>

## Lifecycle, release, correction, and rollback

The generic parent must preserve:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

### Lifecycle posture by stage

| Stage | Crossing validator posture |
|---|---|
| RAW | May validate envelope integrity and source refs; must not rewrite source payload as truth. |
| WORK | May validate candidate normalization and hold unresolved families, roles, time, or geometry. |
| QUARANTINE | May confirm reason structure and correction requirements; must not make held data public. |
| PROCESSED | May validate normalized Crossing candidates and transform receipts. |
| CATALOG/TRIPLET | May validate catalog/graph references while preserving source/evidence lineage. |
| PUBLISHED | May verify release-bound public-safe derivative refs; cannot publish or approve. |
| correction/withdrawal/rollback support | May validate cascade refs and invalidation completeness. |

### Promotion boundary

A parent result may be one input to a promotion decision. It is never the decision itself.

### Correction cascade

A correction to a source Crossing may affect:

- specialized Bridge/RiverCrossing/Ferry records;
- route memberships;
- network nodes and edges;
- map/tile artifacts;
- catalog and graph records;
- Evidence Drawer or Focus Mode carriers;
- exports and screenshots;
- AI answers or cached summaries.

A future result should identify known derivative refs or an invalidation query reference. It must not silently mutate them.

### Withdrawal

A withdrawn Crossing should not remain public through:

- stale tile bundles;
- graph edges;
- search indexes;
- cached API payloads;
- generated narratives;
- unversioned exports.

### Rollback

Rollback should restore the last accepted compatible implementation/configuration or release target. It must preserve:

- the failed candidate/result;
- reason and reviewer record;
- prior version;
- migration/deprecation state;
- audit trail.

[Back to top](#top)

---

<a id="tests-fixtures-and-no-network-posture"></a>

## Tests, fixtures, and no-network posture

### Current test finding

No dedicated `tests/validators/crossings/README.md` was found in the direct probe. The domain test tree documents no-network posture and several transport guardrails, but dedicated generic Crossing executable coverage was not established.

### Proposed test roots

Placement must be rechecked before implementation. The lowest-common test responsibility may use:

```text
tests/validators/crossings/
```

and fixtures may use an accepted `fixtures/validators/crossings/` or domain fixture convention.

Do not place fixtures under `tools/validators/crossings/`.

### Minimum positive fixtures

- valid generic road–road Crossing with evidence and bounded time;
- valid road–rail Crossing with explicit carried/crossed roles;
- valid historic Crossing narrowed to historic/contextual use;
- valid modeled candidate held for review rather than promoted;
- valid public-safe generalized derivative with release/correction/rollback refs;
- valid child orchestration packet whose child result matches the same candidate digest.

### Minimum negative fixtures

- spatial intersection presented as confirmed Crossing;
- missing source role;
- modeled candidate upcast to observed;
- missing valid time where material;
- historic evidence presented as current access;
- carried/crossed role conflict;
- generic Crossing silently used as Bridge;
- graph edge used as source record;
- graph used as live route;
- missing child result;
- child digest mismatch;
- missing evidence;
- policy decision missing;
- release reference missing;
- rollback reference missing;
- sensitive exact location exposed;
- legal-access claim without authority;
- bridge safety/load claim;
- fordability/water-condition claim;
- current closure claim from stale source;
- emergency routing request;
- malformed or oversized geometry;
- path traversal or network URL in no-network mode.

### Determinism tests

- same inputs/config produce byte-equivalent canonical report;
- finding order is stable;
- child result order does not affect canonical parent result;
- invalid fixtures return nonzero status;
- errors do not silently become pass;
- logs omit sensitive fixture canaries;
- no network socket or HTTP client is used in default mode.

### Contract tests

Test the split:

- contract defines meaning;
- schema defines shape;
- validator checks;
- policy decides admissibility;
- tests prove behavior;
- release decides public use.

No fixture should make the validator the source of domain truth.

[Back to top](#top)

---

<a id="ci-admission-contract"></a>

## CI admission contract

### Current workflow finding

`.github/workflows/domain-roads-rail-trade.yml` is triggered by pull requests and pushes to `main`, but its three jobs execute only TODO echo commands. It does not currently prove generic Crossing enforcement.

The shared schema workflows invoke the five-entry aggregate. Because the aggregate does not include crossings and no paired Crossing schema was confirmed, those workflows do not establish Crossing coverage.

### Future CI admission requirements

A substantive crossing CI job should:

- invoke a repository-owned command rather than inline validation logic;
- run no-network synthetic fixtures by default;
- pin the accepted contract/schema/config refs;
- fail on invalid-fixture acceptance;
- produce a bounded machine report or test report;
- upload only public-safe reviewer artifacts;
- use least-privilege explicit permissions;
- avoid secrets for pull requests;
- avoid write, release, deployment, comment, or publication side effects;
- use immutable third-party action pins or record the gap;
- set timeouts and concurrency controls;
- preserve stable check names only after branch-protection coupling is reviewed.

### Workflow threat posture for this README change

The target README path may trigger:

- the TODO-only Roads/Rail/Trade workflow;
- repository documentation or link workflows where path filters apply;
- broader workflow defaults not exhaustively inspected.

Repository evidence does not establish branch protection, effective default token permissions, required checks, or recent pass rates. Those remain **NEEDS VERIFICATION**.

### Watcher and publisher boundary

No watcher, connector, workflow, or validator may publish a Crossing merely because validation passed. At most, automation may emit a candidate result and open a reviewable change under accepted governance.

[Back to top](#top)

---

<a id="smallest-sound-implementation-sequence"></a>

## Smallest sound implementation sequence

This sequence is **PROPOSED** and deliberately excludes live connectors and public release.

### Phase 0 — resolve authority inputs

1. Confirm owners and CODEOWNERS enforcement.
2. Resolve or explicitly maintain the generic parent versus domain/specialization topology.
3. Resolve Crossing schema home and slug drift through accepted governance.
4. Confirm source-role vocabulary, time profile, sensitivity profile, and result-code registry.
5. Confirm whether `_common` is the accepted shared runtime for this family.

### Phase 1 — shape and fixtures

1. Accept the Crossing contract version.
2. Add a paired schema in the selected home.
3. Add schema registry/index entry.
4. Add public-safe valid, invalid, malformed, and edge fixtures.
5. Add direct schema tests.

### Phase 2 — generic parent

1. Implement a thin parent entrypoint.
2. Bind exact packet, schema, contract, and configuration versions.
3. Implement generic invariants only.
4. Emit deterministic parent reports.
5. Enforce no-network and resource limits.

### Phase 3 — delegation

1. Register accepted child validators.
2. Bind child results to candidate/config digests.
3. Reconcile parent/child findings.
4. Add child missing/failure/conflict tests.
5. Prove correction/withdrawal cascade.

### Phase 4 — policy and release gates

1. Add rights/sensitivity/public-safe policy tests.
2. Add evidence closure tests.
3. Add release/correction/rollback reference tests.
4. Prove public carriers cannot bypass release.
5. Keep live routing, safety, legal access, and emergency uses denied.

### Phase 5 — CI and observability

1. Add a command-bearing CI job.
2. Run positive and negative fixtures.
3. Emit bounded artifacts and exit codes.
4. Add metrics for pass/fail/abstain/deny/error and reason codes without sensitive data.
5. Document kill switch, compatibility, deprecation, and rollback.

No phase authorizes public release by itself.

[Back to top](#top)

---

<a id="definition-of-done"></a>

## Definition of done

The generic Crossings parent is not implementation-ready merely because a README, script, or schema exists.

### Documentation

- [ ] README reflects current repo evidence and exact implementation.
- [ ] One canonical parent topology is documented.
- [ ] Child/dependency responsibilities are explicit.
- [ ] Safety, legal-access, Hydrology, infrastructure, graph, sensitivity, and release boundaries remain visible.
- [ ] Open drift and ADR dependencies are linked.

### Contract and schema

- [ ] Generic Crossing contract is reviewed.
- [ ] Paired schema exists in the accepted home.
- [ ] Schema and contract versions cross-link.
- [ ] Schema registry/index entry exists.
- [ ] Compatibility crossings schema lane does not carry divergent authority.

### Implementation

- [ ] Generic parent executable exists.
- [ ] Shared runtime dependency is explicit.
- [ ] Parent performs only generic checks.
- [ ] Child registry and version compatibility exist.
- [ ] Structured deterministic report exists.
- [ ] Default mode is no-network and side-effect-free.
- [ ] Resource and path-security limits exist.

### Sources, evidence, policy, and release

- [ ] Source-role vocabulary and source refs are validated.
- [ ] Time/freshness profiles are validated.
- [ ] Evidence closure is checked for consequential use.
- [ ] Rights/sensitivity decisions fail closed.
- [ ] Public-safe transform refs are checked.
- [ ] Release/correction/rollback refs are checked.
- [ ] Validator success cannot publish.

### Tests and CI

- [ ] Positive fixtures pass.
- [ ] Negative, malformed, and adversarial fixtures fail as expected.
- [ ] Child missing/failure/conflict tests exist.
- [ ] Sensitive logging tests exist.
- [ ] No-network tests exist.
- [ ] CI invokes real repository-owned commands.
- [ ] Invalid-fixture acceptance fails CI.
- [ ] Current check names and branch-protection significance are verified.

### Operations and governance

- [ ] Owners and reviewers are assigned.
- [ ] Migration/deprecation policy is accepted.
- [ ] Rollback is tested.
- [ ] Correction and withdrawal cascade is tested.
- [ ] Runtime consumers and release dependencies are inventoried.
- [ ] No unsupported routing, safety, legal, structural, or emergency use is exposed.

[Back to top](#top)

---

<a id="migration-compatibility-and-deprecation"></a>

## Migration, compatibility, and deprecation

### Compatibility surfaces

Potential compatibility-sensitive surfaces include:

- parent validator ID and command;
- packet/report schema versions;
- reason codes;
- process exit codes;
- child registry IDs;
- contract/schema refs;
- configuration paths;
- report destination;
- CI check names;
- imported shared-helper API.

### Migration rules

A material change should:

1. record old and new version;
2. identify consumers;
3. provide a compatibility or explicit breaking-change plan;
4. add fixtures covering both sides where required;
5. update docs and registries;
6. preserve old reports long enough for audit;
7. define correction and rollback;
8. avoid dual active parent authorities.

### Schema migration

If Crossing schemas move from a compatibility path to the accepted domain path:

- use a migration note or ADR;
- preserve `$id` and alias behavior intentionally;
- prevent divergent content;
- update validator registry and fixtures atomically;
- verify all consumers;
- deprecate the old path visibly;
- test rollback.

### Parent/child migration

If generic and specialized checks are reorganized:

- generic invariants remain in one parent;
- specialization invariants remain in accepted children;
- result compatibility is versioned;
- no rule silently disappears;
- parent/child conflict tests are updated;
- public release remains blocked until parity is proven.

### Deprecation criteria

A path, command, result code, or child ID may be deprecated only when:

- replacement is accepted;
- consumers are inventoried;
- migration is documented;
- CI proves the replacement;
- rollback exists;
- deprecation does not weaken fail-closed behavior.

[Back to top](#top)

---

<a id="open-verification-register"></a>

## Open verification register

| ID | Question | Evidence that would settle it | Status |
|---|---|---|---|
| `CROSS-OPEN-001` | Who owns the generic parent and required reviews? | Accepted stewardship records and enforced CODEOWNERS/rulesets. | **NEEDS VERIFICATION** |
| `CROSS-OPEN-002` | Is `tools/validators/crossings/` the accepted generic parent code home? | Accepted ADR/register plus implemented entrypoint and consumers. | **NEEDS VERIFICATION** |
| `CROSS-OPEN-003` | Is there any unindexed or branch-local generic executable? | Recursive tree/clone inspection and import/entrypoint search. | **UNKNOWN** |
| `CROSS-OPEN-004` | What is the canonical Crossing schema home? | Accepted ADR/migration/schema registry decision. | **NEEDS VERIFICATION** |
| `CROSS-OPEN-005` | Is the Crossing contract accepted, and what version? | Contract review record and registry entry. | **NEEDS VERIFICATION** |
| `CROSS-OPEN-006` | What source-role enum is canonical? | Accepted schema/registry and source descriptors. | **NEEDS VERIFICATION** |
| `CROSS-OPEN-007` | Which source descriptors support generic crossing families? | Source registry inventory with rights, cadence, role, and review state. | **NEEDS VERIFICATION** |
| `CROSS-OPEN-008` | What freshness profiles apply to current-status fields? | Accepted policy/config and tests. | **NEEDS VERIFICATION** |
| `CROSS-OPEN-009` | What sensitivity profiles apply to infrastructure, archaeology, cultural corridors, and private access? | Accepted policy, transforms, and negative fixtures. | **NEEDS VERIFICATION** |
| `CROSS-OPEN-010` | Is Bridge/RiverCrossing the only accepted child? | Validator registry and complete child inventory. | **NEEDS VERIFICATION** |
| `CROSS-OPEN-011` | Which shared validators are stable dependencies? | Accepted helper API/registry and compatibility tests. | **NEEDS VERIFICATION** |
| `CROSS-OPEN-012` | What is the result schema and reason-code registry? | Accepted schema, registry, fixtures, and migration policy. | **NEEDS VERIFICATION** |
| `CROSS-OPEN-013` | Where do generic crossing fixtures and tests belong? | Directory Rules/ADR review plus implemented paths. | **NEEDS VERIFICATION** |
| `CROSS-OPEN-014` | What CI job must block crossing changes? | Command-bearing workflow plus branch-protection settings. | **NEEDS VERIFICATION** |
| `CROSS-OPEN-015` | What report/receipt destination is accepted? | Contract/schema/Directory Rules decision and emitter implementation. | **NEEDS VERIFICATION** |
| `CROSS-OPEN-016` | How do corrections invalidate graph, map, search, export, and AI derivatives? | Executable cascade test and release records. | **NEEDS VERIFICATION** |
| `CROSS-OPEN-017` | Are public consumers already using Crossing records? | API/UI/runtime inventory, logs, manifests, and release refs. | **UNKNOWN** |
| `CROSS-OPEN-018` | What are current pass rates and operational metrics? | Current workflow runs and emitted reports. | **UNKNOWN** |
| `CROSS-OPEN-019` | Which Directory Rules copy is canonical? | Accepted ADR or document registry decision. | **CONFLICTED / NEEDS VERIFICATION** |
| `CROSS-OPEN-020` | Is source-registry topology domain-first or subtype-first? | Accepted registry ADR/migration and canonical inventory. | **CONFLICTED / NEEDS VERIFICATION** |
| `CROSS-OPEN-021` | Are action refs, token permissions, and required checks hardened? | Workflow/settings/ruleset inspection. | **NEEDS VERIFICATION** |
| `CROSS-OPEN-022` | Has rollback been tested? | Recorded rollback drill or revert test. | **UNKNOWN** |

[Back to top](#top)

---

<a id="rollback-path"></a>

## Rollback path

### Documentation-only rollback

For this README revision:

- revert the README commit and the generated receipt commit;
- or close the draft pull request without merge.

The prior target blob is:

```text
7807275a0afca4aa1518787a392225e2732a6757
```

No executable, schema, contract, policy, test, source record, lifecycle data, release, runtime, or public behavior changes with this documentation-only update.

### Future implementation rollback

A future code change should document:

- previous parent version;
- previous packet/report schema;
- previous child registry;
- previous CI command and check name;
- compatibility window;
- report/data migration impact;
- consumer rollback;
- correction or withdrawal cascade;
- kill switch.

Rollback must not restore an unsafe allow path or republish withdrawn content.

[Back to top](#top)

---

<a id="evidence-ledger"></a>

## Evidence ledger

| Evidence | Blob or pinned state | What it supports | Limitation |
|---|---|---|---|
| `tools/validators/crossings/README.md` | `7807275a...` at `main@7af05fc50e5a1bab28b314532b0a66d2839a229b` | Prior v0.1 target and generic-parent intent. | README did not prove executable behavior. |
| `tools/validators/README.md` | `e3574228...` | Validator-root authority and fail-closed posture. | Parent inventory is not exhaustive runtime proof. |
| `tools/validators/_common/README.md` | `12df3198...` | Shared runtime is executable and CI-invoked for configured families. | Does not prove Crossing registration. |
| `tools/validators/_common/run_all.py` | `3375cce1...` | Five hard-coded aggregate entries; no Crossing entry. | Does not prove no other entrypoint exists elsewhere. |
| `tools/validators/bridge_river_crossing/README.md` | `40636050...` | Confirmed child specialization design and current README-only maturity. | Does not prove child enforcement. |
| `tools/validators/domains/roads-rail-trade/README.md` | `1d5942ab...` | Domain validator index and transport authority boundaries. | Does not prove domain runtime. |
| `tools/validators/transport-facility-topology/README.md` | `35773f93...` | Adjacent topology/facility boundary. | Does not prove topology executable. |
| `contracts/domains/roads-rail-trade/crossing.md` | `a2c2b97d...` | Crossing semantic meaning, exclusions, candidate schema path. | Draft; schema missing. |
| `schemas/contracts/v1/domains/roads-rail-trade/README.md` | `91cd62a6...` | Domain schema index and no concrete checked inventory. | Bounded search, not recursive proof forever. |
| `schemas/contracts/v1/crossings/README.md` | `cf4ef355...` | Compatibility/index-only status and no-parallel-authority rule. | Canonical status unresolved. |
| `policy/domains/roads-rail-trade/README.md` | `50806270...` | Policy file is greenfield scaffold. | No enforcement. |
| `tests/domains/roads-rail-trade/README.md` | `3c362bf1...` | Domain test posture and documentation-led inventory. | Executable coverage/pass rates unverified. |
| `.github/workflows/domain-roads-rail-trade.yml` | `c6f547b0...` | Workflow contains TODO-only echo jobs. | Settings and runs not inspected. |
| `data/registry/sources/roads-rail-trade/README.md` | `54087e02...` | Source-role/rights/freshness boundary and registry topology drift. | Active descriptor inventory unverified. |
| `docs/doctrine/directory-rules.md` | `2affb080...` | Validator placement under `tools/` and responsibility-root doctrine. | Duplicate canonical-document question unresolved. |
| `docs/architecture/directory-rules.md` | `18653c00...` | Confirms placement conflict is open. | Does not resolve it. |
| ADR-0001 | `ab0010a2...` | Proposed schema-home direction. | Status remains proposed. |
| `docs/registers/DRIFT_REGISTER.md` | `97a77552...` | Current recorded drift entries. | Does not yet contain a crossings-specific resolution. |
| `.github/CODEOWNERS` | `dd2a84aa...` | `/tools/validators/` and receipts route to `@bartytime4life`. | Required review/rulesets unverified. |
| `.github/workflows/README.md` | `c3dfbe11...` | Workflow maturity and threat posture. | Current run history/settings not inspected. |
| generated receipt schema | `fba21ed2...` | Machine shape for the companion generated-work receipt. | Receipt is provenance, not proof or release. |
| uploaded implementation prompt v3.1 | `sha256:b061d3d8b153af8083cd1f62f447b389c396b5a882e590328ede7c3e3ff25e85` | Task authority, implementation route, evidence/validation/receipt requirements. | Does not prove repo implementation. |

### Evidence boundary

The repository observations above are bounded to the recorded base and direct reads/probes. They do not establish:

- exhaustive recursive absence;
- branch-protection settings;
- workflow success;
- production deployment;
- current operational conditions;
- release approval.

[Back to top](#top)

---

<a id="changelog"></a>

## Changelog

### v0.2 — 2026-07-17

- Replaced planning-heavy status language with a pinned repository evidence snapshot.
- Confirmed the lane remains README-only in direct probes.
- Confirmed no expected generic executable, dedicated crossings test README, or paired Crossing schema at the probed paths.
- Documented the working shared validator runtime and the absence of Crossing from its five-entry aggregate.
- Documented Bridge/RiverCrossing as the confirmed README-only child, the per-domain index, and the adjacent facility/topology lane.
- Added generic parent/child delegation and reconciliation rules.
- Added bounded language, immutable packet expectations, generic invariants, object-family anti-collapse, geometry/graph, time/freshness, safety/access, sensitivity/public-surface, report, reason-code, security, lifecycle, test, CI, implementation, definition-of-done, migration, open-verification, rollback, and evidence-ledger sections.
- Surfaced rather than resolved schema-home, slug, source-registry, and Directory Rules conflicts.
- Preserved the core rule that validators check declared inputs but do not create crossing truth, policy, release, or public authority.

### v0.1 — 2026-07-07

- Replaced an empty file with an initial generic crossings validator parent guide.
- Introduced anti-collapse, lifecycle, outcome, proposed test, and review-checklist guidance.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Date | 2026-07-17 |
| Evidence snapshot | `main@7af05fc50e5a1bab28b314532b0a66d2839a229b` |
| Review state | Draft repository-grounded README replacement; human review pending. |
| Implementation maturity | README-only generic parent; shared runtime exists elsewhere; generic enforcement unestablished. |
| Next smallest safe change | Resolve schema/slug and parent/child topology, then add one accepted Crossing schema plus public-safe valid/invalid fixtures and direct no-network tests before implementing or registering a generic parent executable. |

[Back to top](#top)
