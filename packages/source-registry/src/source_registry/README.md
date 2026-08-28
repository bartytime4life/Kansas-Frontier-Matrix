<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://package/source-registry/src/source_registry/readme
title: packages/source-registry/src/source_registry/ — Python Namespace and Governed Source-Context Candidate Scaffold
type: package-readme
version: v0.2
prior_version: v0.1
status: draft
owners: OWNER_TBD — Package steward · Source steward · Registry steward · Contracts steward · Schema steward · Policy steward · Rights steward · Sensitivity steward · Evidence steward · Catalog steward · Security steward · Validation steward · Runtime/API steward · CI steward · Docs steward
created: 2026-06-15
updated: 2026-07-19
policy_label: "public-doctrine; python-namespace; greenfield-placeholder; no-supported-api; candidate-only; source-authority-external; policy-authority-external; registry-persistence-external; no-network-by-default; explicit-inputs; fail-closed; rights-aware; sensitivity-aware; source-role-anti-collapse; correction-aware; rollback-aware"
current_path: packages/source-registry/src/source_registry/README.md
truth_posture: >
  CONFIRMED target README v0.1, source_registry namespace directory, empty __init__.py,
  kfm-source-registry distribution metadata version 0.0.0, substantial closed singular
  SourceDescriptor schema and semantic contract, currently wired validator/fixtures/schema
  test/workflow, proposed empty central authority register, permissive plural schema scaffold,
  placeholder intake/activation objects, proposed admission ADR, and registry placeholder
  records / PROPOSED a small reusable namespace for deterministic SourceDescriptor parsing,
  explicit-reference lookup adapters, conflict detection, candidate context assembly, and
  safe diagnostics / CONFLICTED singular-vs-plural schema authority, schema-declared-vs-wired
  validator and fixture homes, prior README module/API/result promises, and generic registry
  conventions / UNKNOWN accepted import API, build backend, Python support, dependencies,
  implementation modules, package-local tests, first consumer, registry reader wiring,
  policy-runtime handoff, deployment, and operational health / NEEDS VERIFICATION owners,
  schema migration decision, authority-register population, activation decision contract,
  policy enforcement, registry-instance conformance, consumer adoption, compatibility,
  correction, revocation, and rollback drills
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: c9eaa25dccc57dc22cc402147853924a5c7df66f
  prior_blob: 2dcec0f4ee82172af628928f50b96363df97dea0
  package_readme_blob: 194831d4b5a827599bcae780147af0c9ccfaf9f5
  source_readme_blob: e30f3b055c73b77e3078043196ade7497fccbe15
  package_metadata_blob: 3bf14d4b919fde034fa490cb7b099c4068f6b8f9
  namespace_init_blob: e69de29bb2d1d6434b8b29ae775ad8c2e48c5391
  source_descriptor_contract_blob: b57ae5ccc042c1423b75c168438800384c9b6713
  detailed_singular_schema_blob: 582e70b834278c3c6ca9a8b31efbe0989c96f0bc
  permissive_plural_schema_blob: 8d5cee60a711454a78cbf4a3c84eebbaed2503e8
  observed_validator_blob: 9d0538e727b5eb49c043998a3550972349d2e790
  fixture_readme_blob: 4df8a264ef6f8ba48dbfcf313d3d6390b557f5c5
  validation_workflow_blob: 8e286cb0a12aed6acffeceb5e4b90f18394039e9
  authority_register_blob: 82c23722520922f5ca0dad7f37ed794d1c2edf81
  registry_root_readme_blob: 2821e9681273bff6b430920d0a45312c5643ba33
  admission_adr_blob: 0e8d03786bcc99b19f179680890df9e30a27633a
  intake_placeholder_blob: dff2d03973abb2c6750aa2e4cfc2a5e2311635a5
  source_activation_placeholder_blob: 886965fca543ecba660827890e2ddf45efb90fab
  receipt_activation_placeholder_blob: 04f6074e63054d252a19ba30a71375b307d97062
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  bounded_path_checks:
    - packages/source-registry/src/source_registry/README.md existed at version v0.1 before this revision
    - packages/source-registry/pyproject.toml declares only project name kfm-source-registry and version 0.0.0
    - package metadata declares no build system, Python requirement, package discovery, dependencies, scripts, entry points, license, authors, or test configuration
    - packages/source-registry/src/source_registry/__init__.py is empty
    - bounded repository search surfaced no functional source_registry implementation module, consumer import, or package-local test reference
    - the detailed singular SourceDescriptor schema is closed, substantial, and PROPOSED
    - the schema-declared plural canonical path is a permissive empty PROPOSED scaffold
    - the observed validator, fixtures, targeted schema test, and CI workflow use the detailed singular schema through compatibility wiring
    - the schema-declared validator and fixture paths are absent and are explicitly held by CI
    - control_plane/source_authority_register.yaml is PROPOSED with no entries
    - SourceIntakeRecord and SourceActivationDecision schema surfaces are placeholder inventories, not executable contracts
    - data/registry/sources contains proposed registry guidance and domain placeholder records; package reader behavior is not implemented
related:
  - ../../README.md
  - ../README.md
  - ../../pyproject.toml
  - __init__.py
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../docs/doctrine/trust-membrane.md
  - ../../../../docs/doctrine/lifecycle-law.md
  - ../../../../docs/adr/ADR-0017-source-descriptor-admission-process.md
  - ../../../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../../../docs/sources/ADMISSION_PROCESS.md
  - ../../../../contracts/source/source_descriptor.md
  - ../../../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../../../schemas/contracts/v1/sources/source_descriptor.schema.json
  - ../../../../schemas/contracts/v1/source/source-intake-record.json
  - ../../../../schemas/contracts/v1/source/source-activation-decision.json
  - ../../../../schemas/contracts/v1/receipts/source-activation-decision.json
  - ../../../../control_plane/source_authority_register.yaml
  - ../../../../data/registry/sources/README.md
  - ../../../../fixtures/contracts/v1/source/source_descriptor/README.md
  - ../../../../tools/validators/validate_source_descriptor.py
  - ../../../../tests/schemas/test_common_contracts.py
  - ../../../../.github/workflows/source-descriptor-validate.yml
  - ../../../../policy/source/
  - ../../../../policy/rights/
  - ../../../../policy/sensitivity/
  - ../../../../packages/policy-runtime/README.md
  - ../../../../data/receipts/generated/README.md
  - ../../../../schemas/contracts/v1/receipts/generated_receipt.schema.json
tags: [kfm, packages, source-registry, python, namespace, source-descriptor, source-admission, source-authority, rights, sensitivity, citation, freshness, fail-closed, anti-collapse, compatibility, correction, rollback]
notes:
  - "v0.2 replaces proposed module files, imports, and result vocabularies with the directly verified namespace inventory and current SourceDescriptor validation wiring."
  - "The namespace may prepare candidate source context from explicit inputs; it does not admit or activate sources, assign authority, evaluate policy, persist registry records, fetch upstream data, expose secrets, approve release, or publish."
  - "The singular/plural schema split and validator/fixture path split remain explicit conflicts; this README does not choose a canonical authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `source_registry` Python Namespace and Governed Source-Context Candidate Scaffold

`packages/source-registry/src/source_registry/`

> Future Python namespace for reusable, deterministic source-context candidate mechanics. Current evidence establishes this README and an empty `__init__.py`—not an installable package, supported API, registry reader, source-admission engine, policy evaluator, activation authority, connector, secret client, persisted registry, public endpoint, or publication authority.

![status](https://img.shields.io/badge/status-draft-yellow)
![version](https://img.shields.io/badge/version-v0.2-informational)
![maturity](https://img.shields.io/badge/maturity-greenfield__placeholder-lightgrey)
![distribution](https://img.shields.io/badge/distribution-kfm--source--registry-blue)
![package-version](https://img.shields.io/badge/package__version-0.0.0-lightgrey)
![exports](https://img.shields.io/badge/exports-none-orange)
![authority](https://img.shields.io/badge/source__authority-none-red)

**Quick links:** [Purpose](#purpose-and-audience) · [Evidence](#status-and-evidence) · [Layers](#package-source-and-namespace-layers) · [Authority](#directory-rules-and-authority-boundary) · [Inventory](#confirmed-namespace-inventory) · [Objects](#source-object-and-registry-maturity) · [Schema split](#singularplural-schema-conflict) · [API](#candidate-api-boundary) · [Inputs](#explicit-input-contract) · [Outputs](#candidate-output-and-persistence-boundary) · [Conflicts](#resolution-precedence-and-conflict-handling) · [Outcomes](#outcome-vocabularies-and-fail-closed-posture) · [Lifecycle](#admission-lifecycle-and-trust-membrane) · [Rights](#rights-sensitivity-and-public-release) · [Security](#access-network-secrets-and-side-effects) · [Reliability](#identity-canonicalization-freshness-and-replay) · [Consumers](#consumer-contract) · [Testing](#testing-fixtures-and-ci) · [Implementation](#smallest-sound-implementation-sequence) · [Done](#definition-of-done) · [Open](#verification-register) · [Compatibility](#versioning-correction-revocation-and-rollback) · [Evidence ledger](#evidence-ledger)

> [!IMPORTANT]
> **This README is not implementation evidence.** It establishes no working imports, exports, descriptor loader, authority resolver, activation decision, registry persistence, policy evaluation, network access, consumer adoption, deployment, or operational health.

> [!CAUTION]
> **Source metadata is not source truth or public permission.** A schema-valid `SourceDescriptor`, registry row, authority-register entry, workflow success, or local helper result cannot make a source's claims true, activate a source, satisfy rights or sensitivity policy, admit records into the lifecycle, or authorize publication.

---

## Purpose and audience

This README governs the future import namespace:

```text
packages/source-registry/src/source_registry/
```

It is written for:

- package and namespace implementers;
- source, registry, rights, sensitivity, evidence, catalog, policy, security, and release stewards;
- connector, watcher, pipeline, validator, governed API, review-console, and catalog consumers;
- contract, schema, fixture, test, CI, compatibility, correction, and rollback maintainers.

The intended future role is narrow:

> Accept explicit source-governance inputs, validate or normalize them deterministically where the governing contracts permit, surface conflicts without repairing them by guesswork, and return candidate context for downstream governed decisions.

The current role is narrower still:

- `README.md` exists;
- `__init__.py` is empty;
- the distribution manifest declares only `kfm-source-registry` version `0.0.0`;
- no package build system, Python support range, package discovery, dependency set, script, entry point, implementation module, export, package-local test, consumer import, registry adapter, policy handoff, or runtime deployment is established;
- the repository has real SourceDescriptor schema-validation wiring, but that wiring lives in schema, fixture, test, validator, and workflow roots—not in this namespace;
- authority, admission, and activation surfaces remain proposed, conflicted, empty, or placeholder-level.

This README therefore records the **CONFIRMED placeholder state**, defines **PROPOSED admission rules for future code**, and preserves explicit authority boundaries.

[Back to top](#top)

---

## Status and evidence

| Surface | Verified state | Safe conclusion |
|---|---|---|
| Target README | **CONFIRMED v0.1 before revision** | Prior documentation exceeded current implementation. |
| Namespace directory | **CONFIRMED present** | Placement exists; usability is unproved. |
| `__init__.py` | **CONFIRMED empty** | No supported exports. |
| Distribution metadata | **CONFIRMED placeholder** | `kfm-source-registry` `0.0.0`; installability is unproved. |
| Implementation modules | **NOT ESTABLISHED by bounded inspection** | Proposed files are not repo facts. |
| Consumer imports | **NOT ESTABLISHED by bounded search** | No package adoption is proved. |
| Package-local tests | **NOT ESTABLISHED by bounded search** | Namespace behavior is unproved. |
| Detailed SourceDescriptor schema | **CONFIRMED substantial, closed, PROPOSED** | Shape can be tested; policy/admission is not proved. |
| Plural declared schema | **CONFIRMED empty, permissive, PROPOSED** | Canonical schema authority is conflicted. |
| Semantic contract | **CONFIRMED draft / PROPOSED v0.3** | Meaning exists; acceptance and runtime use remain open. |
| Observed validator | **CONFIRMED** | Validates the detailed singular schema and observed fixture root. |
| Observed fixtures/test | **CONFIRMED bounded coverage** | One valid and one missing-`source_id` invalid fixture; shape only. |
| Validation workflow | **CONFIRMED active bounded check** | Runs compatibility wiring and records explicit holds; no source is admitted. |
| Central authority register | **CONFIRMED PROPOSED and empty** | No central authority row can be resolved. |
| Registry root | **CONFIRMED present / PROPOSED bundle** | Contains guidance and domain placeholders; no namespace reader exists. |
| SourceIntakeRecord | **CONFIRMED placeholder** | No executable intake contract. |
| SourceActivationDecision | **CONFIRMED duplicate placeholder surfaces** | No accepted activation object or authority. |
| Admission ADR | **CONFIRMED proposed** | Doctrine is stated; decision is not accepted. |
| Source/rights policy | **Workflow-confirmed greenfield hold** | Schema conditions are not equivalent to policy enforcement. |
| Runtime health | **UNKNOWN** | No operational namespace exists. |

### v0.1 corrections

This revision removes or narrows the following prior implications:

- `models.py`, `loaders.py`, `resolver.py`, `validation.py`, `policy_input.py`, and `errors.py` are not presented as expected implementation files;
- `RESOLVED`, `UNRESOLVED`, `CONFLICTED`, `STALE`, `INVALID`, and `ERROR` are not presented as a supported namespace enum;
- the namespace is not described as loading the authority register or persisted source registry today;
- schema validation is not equated with source admission, activation, authority assignment, rights approval, evidence sufficiency, release readiness, or public safety;
- the plural schema path is not treated as canonical merely because the detailed singular schema declares it;
- the schema-declared validator and fixture paths are not treated as implemented;
- domain placeholder registry files are not treated as admitted `SourceDescriptor` instances;
- a `public_release.allowed` field is not treated as a release decision.

[Back to top](#top)

---

## Package, source, and namespace layers

The three documentation layers are complementary.

| Layer | Path | Owns | Does not own |
|---|---|---|---|
| Package | `packages/source-registry/README.md` | Package identity, packaging, adoption, compatibility, package-level governance | Namespace API details or authority data |
| Source envelope | `packages/source-registry/src/README.md` | Source-file admission and source-layout boundaries | Package release or registry authority |
| Namespace | `packages/source-registry/src/source_registry/README.md` | Future import/API semantics, result discipline, dependency and side-effect rules | Source truth, admission decisions, policy, persisted registry records, public delivery |

When behavior changes materially, all affected layers must be reconciled. Until the parent READMEs are updated, their proposed interfaces and module maps remain design lineage rather than implementation facts.

[Back to top](#top)

---

## Directory Rules and authority boundary

Directory Rules assign reusable implementation to `packages/`, while truth-bearing and governance-bearing records remain in their responsibility roots.

| Responsibility | Authority home | Namespace relationship |
|---|---|---|
| Reusable candidate mechanics | `packages/source-registry/src/source_registry/` after implementation | May compute candidate context only |
| Package build/import metadata | `packages/source-registry/pyproject.toml` | Must establish installability before API claims |
| SourceDescriptor meaning | `contracts/source/source_descriptor.md` | Consume; never redefine |
| Machine shape | Accepted `schemas/contracts/v1/...` path | Validate through pinned accepted schema |
| Source admission doctrine | Accepted ADR and source docs | Consume; never self-ratify |
| Central authority register | `control_plane/` | Read through governed adapter only after acceptance/population |
| Persisted source registry records | `data/registry/sources/` or accepted registry home | Reference/read only through governed adapter; never own |
| Source, rights, sensitivity policy | `policy/` | Supply explicit input; never decide policy locally |
| Activation/intake decisions | Accepted contract/schema/receipt homes | Preserve refs; never mint authority without governed workflow |
| Evidence and citations | EvidenceBundle/EvidenceRef and catalog surfaces | Preserve refs and source posture; never claim truth |
| Connectors and watchers | `connectors/` and watcher roots | Fetch/discover sources; remain non-publishers |
| Lifecycle data | `data/<phase>/` | Never read or write directly in core namespace |
| Receipts and proofs | `data/receipts/`, `data/proofs/` | Produce candidate metadata only; persistence is external |
| Release/correction/rollback | `release/` and correction homes | Downstream authority; never bypass |
| Public API/UI/map/AI | Governed app and runtime roots | Must not import this namespace as public authority |

This namespace must never:

- create or upgrade source authority;
- choose source role when records conflict;
- infer rights or sensitivity from publisher identity or URL;
- mark a source admitted, active, public-safe, released, or authoritative;
- mutate the authority register or persisted registry;
- fetch upstream data or credentials;
- evaluate policy as the decision authority;
- resolve evidence as truth;
- write lifecycle data, receipts, proofs, release records, or public responses;
- hide missing support behind a permissive default.

[Back to top](#top)

---

## Confirmed namespace inventory

Current evidence supports this exact namespace inventory:

```text
packages/source-registry/src/source_registry/
├── README.md
└── __init__.py
```

| File | Blob/evidence | Current posture |
|---|---|---|
| `README.md` | Prior blob recorded in the Meta Block | Documentation only |
| `__init__.py` | Empty Git blob | No exports or initialization behavior |

No functional loader, resolver, model, validator, policy-input, cache, storage, CLI, or adapter module was established by bounded inspection.

> [!WARNING]
> A README proposal is not an implementation backlog that can be scaffolded blindly. Add a module only when a verified consumer, contract, test burden, dependency direction, and rollback path justify it.

[Back to top](#top)

---

## Source object and registry maturity

The package sits near several distinct object families. They must not be collapsed.

### `SourceDescriptor`

`SourceDescriptor` records how KFM may treat a source. The detailed inspected schema requires a rich field surface including identity, type, role, authority rank, publisher/steward, rights, sensitivity, cadence, access, citation, source-head metadata, admissibility limits, public-release posture, review state, release state, and lifecycle metadata.

Verified strengths:

- the detailed singular schema is closed with `additionalProperties: false`;
- required identity and governance fields are explicit;
- controlled vocabularies and conditional rights/sensitivity/public-release rules exist;
- a semantic contract explains that a descriptor is not source truth or release approval;
- an observed validator, fixture family, targeted schema test, and workflow exercise the detailed schema.

Verified limits:

- schema status remains `PROPOSED`;
- acceptance of the semantic contract remains open;
- schema path authority is conflicted;
- fixture coverage is narrow;
- no namespace code consumes or emits the object;
- policy, current rights verification, source reachability, steward review, activation, registry admission, and release are separate.

### `SourceAuthorityRegister`

The inspected central register is:

```yaml
meta:
  status: PROPOSED
entries: []
```

It establishes no resolvable source authority rows. A future namespace adapter may parse an explicit register snapshot, but it must return a missing-support result when no matching row exists. It must not synthesize a row from a descriptor, domain README, connector name, publisher reputation, or model output.

### Persisted source registry records

`data/registry/sources/` is the governed registry-instance responsibility root. Its README describes pre-RAW admission and authority control, but the bundle remains proposed and includes domain placeholder files.

A future reader must distinguish:

- complete SourceDescriptor instances;
- vocabularies and source-role matrices;
- rights/sensitivity/steward companion records;
- indexes and crosswalks;
- placeholder inventory files;
- superseded records;
- domain-specific non-SourceDescriptor YAML.

It must not assume every YAML or JSON beneath the registry root conforms to the SourceDescriptor schema.

### `SourceIntakeRecord`

The inspected `source-intake-record.json` is a proposed placeholder generated from documentation inventory. It does not define an executable intake contract. Discovery or watcher output remains candidate material and cannot activate or admit a source.

### `SourceActivationDecision`

Two inspected paths exist:

```text
schemas/contracts/v1/source/source-activation-decision.json
schemas/contracts/v1/receipts/source-activation-decision.json
```

Both are proposed placeholders. The object family, canonical home, fields, finite decision vocabulary, review burden, receipt relationship, and supersession rules remain unresolved.

This namespace must not mint or interpret an activation decision as authoritative until those seams are resolved by accepted contracts, schemas, policy, review, fixtures, validators, and workflows.

### `PolicyDecision`, evidence, and release objects

Source admission and activation remain distinct from:

- `PolicyDecision`;
- `EvidenceRef` and `EvidenceBundle`;
- ingest/run receipts;
- catalog records;
- `ReleaseManifest`;
- `CorrectionNotice`;
- `RollbackCard`;
- public response envelopes.

A valid or resolved source context is only input to later governed decisions.

[Back to top](#top)

---

## Singular/plural schema conflict

Current repository evidence contains two competing schema surfaces.

| Path | Current state | Consequence |
|---|---|---|
| `schemas/contracts/v1/source/source_descriptor.schema.json` | Detailed, closed, rich required fields, `PROPOSED` | Currently wired to validator/fixtures/test/workflow |
| `schemas/contracts/v1/sources/source_descriptor.schema.json` | Empty, permissive scaffold, `PROPOSED` | Declared canonical by detailed schema, but cannot enforce descriptor shape |

The detailed schema also declares:

- validator: `tools/validators/sources/validate_source_descriptor.py`;
- fixtures: `tests/fixtures/sources/source_descriptor/`.

Those declared paths are absent. Current compatibility wiring instead uses:

- `tools/validators/validate_source_descriptor.py`;
- `fixtures/contracts/v1/source/source_descriptor/`;
- `tests/schemas/test_common_contracts.py`;
- `.github/workflows/source-descriptor-validate.yml`.

The workflow explicitly preserves this drift as a **hold**, validates only the currently wired fixture family, and emits no admission or activation decision.

### Namespace rule

Until an ADR or migration resolves the split:

1. no namespace constant may silently choose one path as canonical;
2. callers must supply an explicit schema identity or accepted registry resolver;
3. conflicting schema identities fail closed;
4. cache keys and receipts must record the exact schema path/version/digest;
5. compatibility aliases must be visible and temporary;
6. migration tests must prove old and new behavior deliberately;
7. no successful shape check may be represented as accepted source admission.

[Back to top](#top)

---

## Candidate API boundary

No public or internal API is currently supported.

Future code may be admitted only when it is:

- reusable across more than one governed consumer;
- explicit-input and explicit-version;
- deterministic where promised;
- no-network by default;
- free of hidden registry, policy, lifecycle, or credential access;
- candidate-only;
- exhaustive over negative paths;
- backed by fixtures and tests;
- reversible and versioned.

### Allowed future mechanics

Subject to accepted contracts and tests, the namespace may eventually:

- parse explicit SourceDescriptor bytes or mappings;
- invoke an injected schema validator identified by path/version/digest;
- normalize explicit descriptor fields without changing their meaning;
- compare descriptor identity, version, source-head, and lifecycle refs;
- parse an explicitly supplied authority-register snapshot;
- locate an exact source id within an explicit registry index;
- surface descriptor/register/schema conflicts;
- assemble a candidate source-context object for policy input;
- preserve rights, sensitivity, citation, cadence, access, review, release, lifecycle, and supersession metadata;
- compare replay expectations and detect drift;
- produce safe diagnostics and receipt-ready candidate metadata;
- construct synthetic, sanitized, deterministic fixtures.

### Forbidden API behavior

A namespace function must not:

- scan repository roots implicitly;
- search the filesystem for the “best” descriptor;
- read live URLs, source APIs, secret stores, environment credentials, or UI state;
- choose the most permissive descriptor or register row;
- downgrade a sensitivity floor;
- convert unknown rights into allowed rights;
- treat publisher identity as authority proof;
- activate a connector or watcher;
- write or update registry records;
- issue policy, review, admission, activation, release, or public decisions;
- return full restricted descriptor bodies in errors or logs;
- expose implementation-specific paths as public API.

### Core and adapters

Preferred architectural split:

| Layer | Permitted behavior |
|---|---|
| Pure core | Parse, validate, normalize, compare, detect conflict, assemble candidate context |
| Injected repository adapter | Read exact caller-authorized refs from an accepted registry interface |
| Policy adapter | Submit explicit candidate input to policy runtime; return external decision unchanged |
| Persistence adapter | Owned outside this namespace; writes governed records and receipts |
| Public adapter | Owned by governed API/runtime; applies audience, release, evidence, and redaction gates |

The core should remain testable without network, repository checkout, secret store, clock, or mutable global state.

[Back to top](#top)

---

## Explicit input contract

Every operation should receive only the fields it needs and should identify their authority.

| Input family | Examples | Required posture |
|---|---|---|
| Descriptor input | exact bytes/mapping, source id, descriptor version, digest, schema id | Explicit and pinned |
| Schema input | accepted schema ref, digest, validator profile | No ambient default while schema conflict remains |
| Authority input | exact register snapshot/ref, register version/digest, row id | Explicit; no inferred fallback |
| Registry input | exact registry index/ref, record kind, lifecycle state | Scoped and typed |
| Caller context | operation, domain, audience, lifecycle stage, purpose | Required for bounded candidate output |
| Rights context | rights status, terms, attribution, redistribution/commercial limits, verification time | Preserved exactly |
| Sensitivity context | source default, policy floor, restricted categories, review refs | Most restrictive posture preserved |
| Citation context | required flag, template, guidance, preferred link | Never silently dropped |
| Freshness context | source time, observed time, retrieved time, review time, stale threshold | Time kinds remain distinct |
| Access context | access method/posture, endpoint metadata, auth-required flag | Secrets excluded |
| Governance context | review, policy, intake, activation, correction, supersession refs | References only; no invented decisions |
| Replay context | expected descriptor/register/schema digests, prior candidate digest | Explicit comparison target |
| Resource limits | max bytes, nesting depth, collection count, timeout | Enforced before expensive work |

Missing required support must remain missing. The namespace must not fill governance gaps from generated language, operator memory, neighboring records, or “reasonable defaults.”

[Back to top](#top)

---

## Candidate output and persistence boundary

A future result may carry candidate data such as:

- normalized source identity and descriptor version;
- exact schema identity and validation report ref;
- descriptor digest and source-head digest fields;
- explicit source role and authority rank;
- rights, sensitivity, citation, cadence, access, review, release, lifecycle, and supersession posture;
- matching authority-register row ref, if one exists;
- matching registry record ref and kind;
- conflict and missing-support details;
- safe reason codes;
- policy-input fragment candidate;
- replay comparison metadata.

It must not carry:

- an authoritative admission or activation decision created locally;
- a new source role not present in governed input;
- a less restrictive rights or sensitivity posture;
- raw credentials or secret-bearing endpoints;
- unrestricted sensitive registry content;
- a public-safe flag derived only from descriptor fields;
- evidence truth claims;
- release approval;
- persisted registry mutation confirmation unless returned by the external owning workflow.

### Persistence

Core namespace code does not persist:

- SourceDescriptor instances;
- authority-register rows;
- intake or activation decisions;
- policy decisions;
- receipts or proofs;
- lifecycle records;
- catalog records;
- release/correction/rollback records.

A governed external workflow may persist an accepted object after independent schema, policy, review, rights, sensitivity, and authority checks. Its receipt must reference exact input/output identities and the namespace version, if used.

[Back to top](#top)

---

## Resolution precedence and conflict handling

Resolution must be explicit, deterministic, and non-permissive.

### No implicit authority order

The namespace must not choose a winner merely because one record is:

- newer;
- in a “canonical-looking” path;
- more permissive;
- signed;
- associated with a government publisher;
- referenced by more documents;
- emitted by a successful workflow;
- generated by a model;
- already used by a consumer.

### Conflict examples

| Conflict | Required posture |
|---|---|
| Singular and plural schema disagree | Fail closed; require accepted schema identity |
| Descriptor role differs from authority row | Preserve both; report conflict; no role upgrade |
| Descriptor rights differ from rights review | Preserve most restrictive state; route to policy/review |
| Sensitivity defaults differ | Preserve the highest restriction; require steward resolution |
| Registry record is superseded/withdrawn | Do not return it as current |
| Descriptor digest differs from expected digest | Drift/error; no cache reuse |
| Source-head identity changed | Mark stale/drift; require refresh and review as policy requires |
| Activation decision is absent or placeholder | Do not activate |
| Public release field conflicts with policy/release state | Policy/release authority wins; fail closed |
| Multiple source ids claim same upstream endpoint | Return ambiguity; do not merge automatically |

### Source-role anti-collapse

A source may play only roles explicitly supported by accepted governance records. The namespace must not:

- promote `candidate_signal` to `authoritative_for_claim`;
- collapse aggregator and primary-source roles;
- use a citation source as occurrence evidence;
- infer legal or regulatory authority from naming;
- convert a derived public product into canonical truth;
- erase secondary-role caveats.

[Back to top](#top)

---

## Outcome vocabularies and fail-closed posture

No namespace result enum is currently ratified.

Keep these vocabularies separate:

| Vocabulary family | Current owner/use |
|---|---|
| SourceDescriptor fields | Schema-controlled `review_state`, `release_state`, lifecycle, rights, sensitivity, access, and public-release fields |
| JSON Schema validation | Error collection and process pass/fail |
| Workflow reporting | `PASS`, `FAIL`, `SKIPPED`, and explicit hold text |
| SourceActivationDecision | Placeholder; no accepted finite vocabulary |
| Policy/runtime decision | External policy/runtime contract; not invented here |
| Release state | Release governance |
| Proposed internal resolution statuses | Design-only until contract, schema, tests, and consumers ratify them |

A future typed result should separate:

- shape validity;
- descriptor identity;
- registry match state;
- authority match state;
- freshness/drift;
- rights/sensitivity completeness;
- policy/review/activation references;
- operational error.

Do not compress those dimensions into a single `RESOLVED` boolean.

Unknown, stale, conflicted, superseded, withdrawn, unreviewed, or unverifiable support must not produce an outwardly permissive result.

[Back to top](#top)

---

## Admission, lifecycle, and trust membrane

The lifecycle remains:

```text
source discovery
  -> descriptor candidate
  -> rights / sensitivity / role / access / citation review
  -> activation decision
  -> RAW
  -> WORK / QUARANTINE
  -> PROCESSED
  -> CATALOG / TRIPLET
  -> PUBLISHED
```

This namespace may eventually assist candidate parsing and comparison before or during the governed admission flow. It does not own any transition.

Key invariants:

- no source enters normal lifecycle processing without accepted admission support;
- watchers and connectors remain non-publishers;
- activation is not publication;
- registry presence is not truth;
- schema validity is not policy approval;
- evidence and release gates remain downstream;
- public clients never read raw registry internals or pre-publication stores directly;
- correction and supersession produce new governed records rather than silent mutation.

[Back to top](#top)

---

## Rights, sensitivity, and public release

The detailed SourceDescriptor schema includes rights and public-release conditionals. The current workflow verifies that selected blocked rights states cannot combine with `public_release.allowed: true`.

That is valuable shape enforcement, but it is not:

- current license verification;
- legal advice;
- a rights policy decision;
- sensitivity policy evaluation;
- steward approval;
- source activation;
- registry admission;
- release approval.

### Namespace obligations

Future code must:

- preserve every rights field and verification timestamp;
- preserve attribution and redistribution duties;
- preserve the most restrictive sensitivity posture;
- treat unknown, noassertion, denied, restricted, or expired support according to accepted policy—not a local shortcut;
- keep protected-location, living-person, DNA/genomic, cultural, infrastructure, and steward-controlled details out of public diagnostics;
- preserve redaction/generalization obligations as refs or external results;
- revalidate policy-significant context at the authority boundary;
- never convert `public_release.allowed` into a publication permission by itself.

[Back to top](#top)

---

## Access, network, secrets, and side effects

### No network by default

Core namespace behavior must be offline and deterministic. It must not:

- call source endpoints;
- perform HTTP HEAD/GET;
- refresh OAuth or API keys;
- query databases or vector indexes;
- call models;
- access KMS or secret managers;
- scan the repository;
- mutate caches with unreviewed data.

Network-capable source access belongs to connectors or approved adapters with explicit policy, credentials, rate limits, receipts, and tests.

### Secrets

Descriptor access metadata may say authentication is required, but secret values never belong in:

- descriptor candidates returned by this namespace;
- logs, traces, metrics, exceptions, snapshots, or fixtures;
- cache keys;
- generated documentation or receipts.

### Hidden side effects

Pure functions must not write files, mutate globals, alter environment variables, move lifecycle data, update registry records, or activate connectors.

[Back to top](#top)

---

## Identity, canonicalization, freshness, and replay

### Identity

Keep these identities distinct:

- source id;
- descriptor id/version;
- upstream version/revision;
- source-head content identity;
- schema id/version/digest;
- authority-register snapshot/row;
- registry record id/version;
- intake/activation decision id;
- policy/review/correction/release refs;
- namespace/package version.

### Canonicalization

Before content hashing is treated as deterministic:

- pin the accepted serialization/canonicalization profile;
- reject ambiguous numbers, encodings, duplicate keys, or unsupported types;
- record schema identity;
- separate descriptor digest from upstream payload digest;
- test semantically equivalent inputs and intentionally distinct inputs.

### Freshness

Do not collapse:

- upstream source time;
- observation time;
- retrieval time;
- source-head observed time;
- rights verification time;
- descriptor review/update time;
- activation decision time;
- policy evaluation time;
- release/correction time.

Freshness decisions belong to accepted policy and governance. The namespace may compute explicit age/difference values from an injected clock but must not invent the stale threshold.

### Replay

A replay result must compare pinned:

- descriptor bytes/digest;
- schema id/digest;
- authority-register snapshot/row;
- registry record;
- policy/review/activation refs;
- package/API version;
- canonicalization profile;
- resource limits;
- clock or evaluation time.

Any mismatch is visible drift, not a warning-only log.

[Back to top](#top)

---

## Consumer contract

The first consumer must be:

- internal and governed;
- explicitly named;
- reviewable and reversible;
- pinned to an accepted package/API version;
- supplied with exact descriptor/schema/register/registry refs;
- exhaustive over missing/conflicted/stale/invalid/error paths;
- unable to use namespace output as source truth or public permission;
- unable to mutate registry, lifecycle, or release state through core functions;
- covered by fixtures, integration tests, replay tests, and a kill switch.

### Consumer-specific rules

| Consumer | Required boundary |
|---|---|
| Connector/watcher | Uses accepted admission/activation externally; namespace does not fetch or enable |
| Ingest pipeline | Requires accepted descriptor and policy support; namespace result alone cannot admit to RAW |
| Validator | Pins schema and reports shape; does not assign authority |
| Policy runtime | Receives explicit candidate input; returns external decision |
| Catalog builder | Preserves source role, rights, citation, limitations, and evidence refs |
| Governed API/AI | Uses released, audience-safe envelopes; never exposes raw registry internals |
| Review console | Displays governed records with access controls; writes through owning workflows |
| Test harness | Uses synthetic public-safe fixtures only |

Public clients must never import or call this namespace directly as an authority surface.

[Back to top](#top)

---

## Testing, fixtures, and CI

### Confirmed current validation

Current repository wiring includes:

- detailed singular SourceDescriptor schema;
- observed validator at `tools/validators/validate_source_descriptor.py`;
- observed fixture root at `fixtures/contracts/v1/source/source_descriptor/`;
- one valid fixture;
- one invalid missing-`source_id` fixture plus expected-error text;
- targeted common-contract schema test;
- `source-descriptor-validate` workflow;
- workflow checks for required rights fields and selected fail-closed schema conditionals.

Current workflow boundaries:

- validates shape fixtures only;
- does not scan registry descriptors;
- does not populate the authority register;
- does not admit, fetch, activate, review, release, or publish a source;
- explicitly holds the singular/plural schema split and declared/observed path drift;
- explicitly notes the proposed admission ADR and greenfield policy stubs.

### Minimum namespace test matrix

Before implementation claims, add tests for:

#### Packaging and imports

- package builds in a clean environment;
- declared Python versions are tested;
- exact import path is stable;
- `__init__.py` exports only reviewed names;
- unknown exports fail;
- import has no network, filesystem scan, registry mutation, or secret access.

#### Descriptor parsing and validation

- valid rich descriptor;
- missing every required field family;
- unknown additional property;
- invalid source id and descriptor version;
- conditional rights/public-release failures;
- conditional sensitivity and connector failures;
- deprecated alias migration;
- unsupported schema id/version;
- singular/plural schema conflict;
- schema digest mismatch.

#### Authority and registry

- empty authority register;
- missing source row;
- duplicate source rows;
- descriptor/register role mismatch;
- rights mismatch;
- sensitivity mismatch;
- multiple registry record kinds;
- placeholder record rejection;
- superseded and withdrawn records;
- domain-specific companion records not mistaken for descriptors;
- deterministic exact-source lookup.

#### Intake and activation

- missing intake record;
- placeholder intake schema;
- absent activation decision;
- duplicate activation schema homes;
- unknown activation vocabulary;
- revoked/superseded activation ref;
- activation result never implies publication.

#### Freshness and replay

- stale source-head;
- changed ETag/checksum/revision;
- rights verification expiry;
- descriptor supersession;
- clock injection;
- deterministic replay;
- cache invalidation on any authority-significant digest change.

#### Security and privacy

- oversized and deeply nested input;
- excessive endpoint or connector counts;
- malicious YAML/JSON constructs where relevant;
- path traversal and symlink defense in adapters;
- no secret values in logs/errors;
- protected-location and personal-data redaction;
- timeout and memory bounds;
- fail-closed adapter exceptions.

#### Consumer and authority boundaries

- no registry writes from core;
- no connector activation;
- no policy decision creation;
- no lifecycle or release mutation;
- no public response construction;
- every negative result handled by first consumer;
- kill switch and rollback path.

[Back to top](#top)

---

## Smallest sound implementation sequence

1. **Resolve authority seams.** Accept one SourceDescriptor schema home and migration plan; resolve validator/fixture paths; resolve activation object family.
2. **Confirm ownership.** Assign package, source, schema, registry, policy, rights, sensitivity, security, and consumer reviewers.
3. **Complete packaging.** Add build backend, Python range, package discovery, dependencies, license/authors as appropriate, and test configuration.
4. **Ratify a minimal internal API.** Define exact input/result types without a permissive public-safe boolean.
5. **Implement pure descriptor parsing.** Explicit bytes/mappings only; no repository scan.
6. **Inject schema validation.** Require exact accepted schema id/version/digest.
7. **Implement explicit register/registry adapters.** Read exact refs; distinguish record kinds; remain read-only.
8. **Implement conflict and freshness comparison.** Preserve restrictive posture and explicit drift.
9. **Add safe diagnostics and resource bounds.**
10. **Add comprehensive unit, negative, replay, security, and compatibility tests.**
11. **Integrate one governed internal consumer.** No source activation, registry mutation, or publication shortcut.
12. **Prove handoff.** Policy, review, activation, persistence, receipts, correction, and rollback remain externally governed.
13. **Add observability and kill switch.**
14. **Document compatibility and deprecation.**
15. **Run correction and rollback drills.**

No stage may claim source admission, activation, evidence closure, release readiness, or publication merely because the prior stage passed.

[Back to top](#top)

---

## Definition of done

The namespace is not done until all applicable items are verified.

### Governance

- [ ] Owners are named and valid.
- [ ] Directory Rules placement remains accepted.
- [ ] SourceDescriptor schema authority is resolved.
- [ ] Validator and fixture homes are resolved.
- [ ] Admission ADR is accepted or superseded.
- [ ] SourceActivationDecision contract/schema/home is accepted.
- [ ] Authority-register ownership, population, review, and correction rules are accepted.
- [ ] Separation of duties is documented for policy-significant activation.

### Packaging and API

- [ ] Build backend and package discovery work.
- [ ] Supported Python versions are declared and tested.
- [ ] Dependencies are pinned and reviewed.
- [ ] Import namespace is confirmed.
- [ ] API version and compatibility policy exist.
- [ ] Exports are intentional and minimal.
- [ ] Core is no-network and side-effect free.
- [ ] Adapters are explicit and separately governed.

### Semantics and safety

- [ ] Descriptor, register, registry, intake, activation, policy, evidence, and release objects remain distinct.
- [ ] Source role cannot be inferred or upgraded.
- [ ] Rights and sensitivity cannot be silently relaxed.
- [ ] Schema, register, and registry conflicts fail closed.
- [ ] Placeholder records cannot be treated as admitted sources.
- [ ] Freshness and supersession are explicit.
- [ ] Secrets and restricted details are excluded from outputs and telemetry.
- [ ] Resource limits and safe errors are enforced.

### Validation and operation

- [ ] Positive and comprehensive negative fixtures exist.
- [ ] Package-local unit tests exist.
- [ ] First-consumer integration tests exist.
- [ ] Replay and drift tests exist.
- [ ] Security/privacy tests exist.
- [ ] CI runs package tests without granting authority.
- [ ] Operational metrics are safe and useful.
- [ ] Kill switch is tested.
- [ ] Correction, revocation, and rollback drills pass.
- [ ] Generated receipt and docs are updated.

[Back to top](#top)

---

## Verification register

| Item | Status |
|---|---|
| Namespace owners and independent reviewers | NEEDS VERIFICATION |
| Build backend, Python range, discovery, dependencies | UNKNOWN / NEEDS VERIFICATION |
| Supported imports and API version | UNKNOWN |
| Functional implementation modules | NOT ESTABLISHED |
| Consumer imports and first consumer | NOT ESTABLISHED |
| Package-local tests | NOT ESTABLISHED |
| Singular/plural schema authority | CONFLICTED / NEEDS VERIFICATION |
| Declared/observed validator path | CONFLICTED / NEEDS VERIFICATION |
| Declared/observed fixture path | CONFLICTED / NEEDS VERIFICATION |
| Detailed schema acceptance | PROPOSED / NEEDS VERIFICATION |
| Semantic contract acceptance | PROPOSED / NEEDS VERIFICATION |
| Admission ADR acceptance | PROPOSED |
| SourceAuthorityRegister population and governance | PROPOSED / EMPTY |
| Registry-instance conformance | NEEDS VERIFICATION |
| SourceIntakeRecord contract | PLACEHOLDER / NEEDS VERIFICATION |
| SourceActivationDecision family and fields | CONFLICTED PLACEHOLDERS |
| Source/rights/sensitivity policy behavior | GREENFIELD HOLD / NEEDS VERIFICATION |
| Descriptor-to-policy input contract | UNKNOWN |
| Activation-to-connector handoff | UNKNOWN |
| Receipt/proof persistence handoff | UNKNOWN |
| Canonicalization and digest profile | NEEDS VERIFICATION |
| Freshness and stale-threshold authority | NEEDS VERIFICATION |
| Cache/replay behavior | UNKNOWN |
| No-network/no-side-effect enforcement | NEEDS VERIFICATION |
| Secret and restricted-data telemetry controls | NEEDS VERIFICATION |
| Resource and parser security bounds | NEEDS VERIFICATION |
| Public API/runtime integration | UNKNOWN |
| Correction/supersession/revocation process | NEEDS VERIFICATION |
| Compatibility/deprecation policy | NEEDS VERIFICATION |
| Kill switch and rollback drill | NEEDS VERIFICATION |
| Operational health | UNKNOWN |
| Parent README reconciliation | NEEDS VERIFICATION |

[Back to top](#top)

---

## Drift and open conflicts

Current material drift includes:

1. detailed singular schema versus empty plural declared-canonical schema;
2. schema-declared validator versus observed validator;
3. schema-declared fixture root versus observed fixture root;
4. proposed admission ADR versus active compatibility validation;
5. central authority register path versus empty register content;
6. registry doctrine versus placeholder domain records;
7. two placeholder SourceActivationDecision schema homes;
8. placeholder SourceIntakeRecord;
9. schema conditionals versus greenfield policy stubs;
10. parent package/source READMEs that still name proposed interfaces or module concepts;
11. current validation workflow proving shape without package implementation.

This README records those conflicts; it does not resolve them.

A resolution that changes canonical paths, object homes, finite vocabularies, public API, or authority precedence requires an ADR or explicit migration note, fixtures, tests, compatibility analysis, and rollback.

[Back to top](#top)

---

## Versioning, correction, revocation, and rollback

### Versioning and compatibility

Any future supported API must define:

- package and API version;
- accepted SourceDescriptor schema versions;
- schema-id and path migration rules;
- result type and reason-code stability;
- consumer compatibility matrix;
- deprecation window;
- fixture and replay coverage;
- changelog and migration guide.

Do not treat a Python function name in documentation as a compatibility promise.

### Correction and supersession

If descriptor or authority context was interpreted incorrectly:

1. stop or disable affected consumers;
2. identify package version, input refs/digests, runs, registry records, policy decisions, releases, and public surfaces;
3. preserve prior records and audit history;
4. issue a new governed descriptor/register/activation/correction record as appropriate;
5. do not silently edit accepted source posture;
6. invalidate caches and downstream candidates through owning authorities;
7. rerun schema, policy, review, consumer, replay, and release checks;
8. communicate public correction only through governed release/correction surfaces.

### Revocation

Rights withdrawal, sensitivity discovery, source compromise, authority loss, or security incident may require:

- source activation hold or revocation;
- connector/watcher disablement;
- registry supersession or withdrawal;
- evidence/catalog/release re-evaluation;
- cache and derivative invalidation;
- public correction, abstention, restriction, or withdrawal;
- incident and receipt records.

This namespace may surface candidate impact metadata; it does not execute revocation.

### Documentation rollback

Before merge, close the PR and abandon the review branch.

After merge, use a revert PR and preserve shared history. Reverting this README does not roll back source descriptors, registry records, activation decisions, connectors, policy, lifecycle data, evidence, releases, or public outputs; those require their own governed rollback paths.

[Back to top](#top)

---

## Evidence ledger

| Evidence | Finding | Limit |
|---|---|---|
| Target README | v0.1 proposed module/API contract | Did not prove implementation |
| Package manifest | `kfm-source-registry` `0.0.0` only | No build/install/API |
| Namespace init | Empty | No exports |
| Parent READMEs | Package/source boundaries exist | Still proposal-heavy |
| Detailed singular schema | Rich, closed, PROPOSED | Not accepted admission authority |
| Plural schema | Empty permissive scaffold | Cannot enforce descriptor shape |
| Semantic contract | Rich draft meaning | Acceptance and consumers open |
| Observed validator | Wires detailed schema to observed fixtures | Shape only |
| Fixture family | One valid, one missing-id invalid | Narrow coverage |
| Workflow | Runs bounded validation and rights conditionals | Emits explicit holds; no admission |
| Authority register | PROPOSED with empty entries | No authority resolution |
| Registry root | Governed placement and domain placeholders | Instance conformance unresolved |
| Intake schema | Placeholder | No intake contract |
| Activation schemas | Two placeholders | Canonical family unresolved |
| Admission ADR | Proposed | Not accepted |
| Policy files via workflow | Greenfield hold | No real policy enforcement |
| Directory Rules | `packages/` is shared implementation root | Does not create implementation |

### Maintainer checklist

- [ ] Re-read current repository state before editing.
- [ ] Preserve source-role anti-collapse.
- [ ] Keep authority, policy, registry persistence, evidence, and release outside the namespace.
- [ ] Pin exact schema/register/registry identities.
- [ ] Add tests before exports.
- [ ] Treat placeholders and unknowns as unresolved.
- [ ] Protect rights, sensitivity, secrets, and restricted details.
- [ ] Record compatibility, correction, revocation, and rollback impact.
- [ ] Update parent docs and generated receipt.
- [ ] Require human review separate from generation and source activation.

[Back to top](#top)
