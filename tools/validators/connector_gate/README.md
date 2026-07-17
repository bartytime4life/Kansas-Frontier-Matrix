<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-connector-gate-readme
title: tools/validators/connector_gate/ — Connector Admission Readiness Validator Boundary
type: readme; directory-readme; validator-lane; connector-admission-readiness; pre-RAW; source-governance; non-authoritative
version: v0.2
status: draft; repository-grounded; README-only-lane; direct-executable-unestablished; direct-tests-unestablished; workflow-todo-only; source-descriptor-validator-executable; source-descriptor-aggregate-registered; source-descriptor-schema-conflicted; activation-vocabulary-conflicted; source-role-vocabulary-conflicted; source-activation-object-unestablished; ingest-receipt-schema-fielded; ingest-receipt-validator-missing; source-authority-register-empty; policy-greenfield; connectors-core-scaffold; no-network-by-default; fail-closed; raw-quarantine-receipts-only; release-gated
owners: OWNER_TBD — Connector steward · Source steward · Admission steward · Contract steward · Schema steward · Registry steward · Rights steward · Sensitivity steward · Security reviewer · Policy steward · Receipt steward · Evidence steward · Lifecycle steward · Release steward · Correction/Rollback steward · CI steward · Docs steward
created: 2026-07-08
updated: 2026-07-16
supersedes: v0.1 planning-oriented connector-gate README
policy_label: "repository-facing; tools; validators; connector-gate; source-admission; pre-RAW; source-descriptor; source-activation; rights-aware; sensitivity-aware; source-head-aware; credential-safe; no-network; deterministic; fail-closed; no-source-admission-authority; no-lifecycle-authority; no-policy-authority; no-release-authority; no-public-serving-authority"
owning_root: tools/
current_path: tools/validators/connector_gate/README.md
responsibility: >
  Repository-grounded boundary for deterministic validation of connector and intake readiness at the pre-RAW membrane. This lane
  may validate a pinned SourceDescriptor, connector identity and declared endpoint plan, activation/review state, rights and
  sensitivity prerequisites, source-role and authority limits, source-head observations, route constraints, receipt/report
  references, safe failure behavior, and correction state. It does not perform network access, run connectors, mint source
  admission or activation decisions, write lifecycle payloads, store credentials, create evidence, decide policy, approve
  release, or serve public clients.
truth_posture: >
  CONFIRMED target v0.1 and prior blob; direct connector_gate lane README-only in bounded search; representative direct
  executable and dedicated test paths absent; connector-gate workflow contains only echo-TODO steps; connectors root limits
  direct connector handoff to RAW or QUARANTINE plus receipts; fielded singular SourceDescriptor schema and top-level executable
  validator exist and the validator is in the five-entry aggregate; plural SourceDescriptor schema is empty/permissive despite
  being named canonical by the fielded schema; schema-declared validator and fixture paths differ from observed executable and
  fixture paths; SourceDescriptor fixture family has one valid and one invalid example; SourceActivationDecision is doctrinal
  but representative contract/schema paths were absent; source authority register exists with zero entries; IngestReceipt has
  a fielded closed schema while its dedicated validator path is absent; source/rights/sensitivity policy READMEs are greenfield
  stubs; connectors-core is a Python placeholder; source-role and activation-state vocabularies conflict across doctrine,
  contract, and schema / PROPOSED phase-specific immutable gate packet, dependency envelopes, deterministic ConnectorGateReport,
  finite CG_ reason codes, no-network fixtures, CI admission, correction cascade, migration/deprecation, and rollback /
  CONFLICTED singular versus plural SourceDescriptor schema authority, top-level versus schema-declared validator path,
  observed versus declared fixture root, seven-role doctrine versus schema role enum, ADR activation states versus schema
  connector activation states, SourceIntakeRecord versus IngestReceipt/RunReceipt naming, and policy/source versus policy/sources
  references / NEEDS VERIFICATION accepted owners, CODEOWNERS, canonical schema/profile and vocabularies, SourceActivationDecision
  contract/schema, connector registry, exact executable and registry id, report schema/home, receipt family, policies, fixtures,
  tests, CI significance, source-refresh integration, quarantine handling, correction cascade, and operational rollback /
  UNKNOWN exhaustive connector inventory, active sources, production invocation, emitted decisions/reports/receipts, endpoint
  health, metrics, deployment, current pass results, and branch-protection significance
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: "6829e8daed19521f59a82780974f643771e898eb"
  prior_blob: bfd5ff3875509f46e050c980891e23841cbae53e
  connectors_root_blob: bdd50032bed62ac36964c79f16cf5541b21759a6
  connectors_core_blob: 0db121b6f378b64bacaf74af57dbfcd40c969d1f
  source_descriptor_contract_blob: b57ae5ccc042c1423b75c168438800384c9b6713
  source_descriptor_singular_schema_blob: 582e70b834278c3c6ca9a8b31efbe0989c96f0bc
  source_descriptor_plural_schema_blob: 8d5cee60a711454a78cbf4a3c84eebbaed2503e8
  source_descriptor_validator_blob: 9d0538e727b5eb49c043998a3550972349d2e790
  source_descriptor_fixtures_blob: 4df8a264ef6f8ba48dbfcf313d3d6390b557f5c5
  source_registry_blob: 2821e9681273bff6b430920d0a45312c5643ba33
  source_admission_process_blob: ab27618a4b1b0e6775d18bedca37aa7d6c514e6e
  source_admission_adr_blob: 0e8d03786bcc99b19f179680890df9e30a27633a
  source_roles_blob: e67784de62b9b919fd7673fce4157be607a65ebf
  source_authority_register_blob: 82c23722520922f5ca0dad7f37ed794d1c2edf81
  ingest_receipt_contract_blob: 4273a9bad9edc7ce7f54c288075f8a49b0f2fe80
  ingest_receipt_schema_blob: 4e9707bec7da63049c5043562c9470564b77184f
  connector_gate_workflow_blob: fc36ecced55bb0b4002d551cb28addfff0be918a
  validator_aggregate_blob: 3375cce172631dc3675cf2e46bb7788d273ff425
  validator_tests_blob: c703a64eef3f69044a54696f121f4e5ae05a3631
  policy_source_blob: 943fa9991f259721920b93f9c13eec07b4197502
  policy_rights_blob: 5dffc3a0ca80d8d94a8008e6c60b2f9489d5f077
  policy_sensitivity_blob: 635bbed7f1ca58f7fea5bd0a4956cdc8becb7529
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  generated_receipt_schema_blob: fba21ed27ebccf1362fe397fe0c3ebd85e072685
bounded_path_checks:
  - tools/validators/connector_gate/ indexed as README-only
  - tools/validators/connector_gate/validate_connector_gate.py absent at tested path
  - tests/validators/connector_gate/README.md absent at tested path
  - tools/validators/sources/validate_source_descriptor.py absent at schema-declared path
  - tools/validators/validate_source_descriptor.py exists and is aggregate-registered
  - tools/validators/validate_ingest_receipt.py absent at schema-declared path
  - representative SourceActivationDecision contract and singular/plural schema paths absent
  - source authority register exists and entries is empty
  - connector-gate workflow is TODO-only
related:
  - ../README.md
  - ../_common/README.md
  - ../sources/README.md
  - ../citation/README.md
  - ../evidence/README.md
  - ../validate_source_descriptor.py
  - ../../../connectors/README.md
  - ../../../packages/connectors-core/README.md
  - ../../../contracts/source/source_descriptor.md
  - ../../../contracts/source/ingest_receipt.md
  - ../../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../../schemas/contracts/v1/sources/source_descriptor.schema.json
  - ../../../schemas/contracts/v1/source/ingest_receipt.schema.json
  - ../../../fixtures/contracts/v1/source/source_descriptor/README.md
  - ../../../data/registry/sources/README.md
  - ../../../control_plane/source_authority_register.yaml
  - ../../../docs/sources/ADMISSION_PROCESS.md
  - ../../../docs/architecture/source-roles.md
  - ../../../docs/architecture/source-role-anti-collapse.md
  - ../../../docs/adr/ADR-0017-source-descriptor-admission-process.md
  - ../../../policy/source/README.md
  - ../../../policy/rights/README.md
  - ../../../policy/sensitivity/README.md
  - ../../../data/raw/
  - ../../../data/quarantine/
  - ../../../data/receipts/
  - ../../../release/
  - ../../../tests/validators/README.md
  - ../../../.github/workflows/connector-gate.yml
  - ../../../.github/workflows/validator-suite.yml
tags: [kfm, tools, validators, connector-gate, pre-raw, source-descriptor, source-activation, ingest-receipt, rights, sensitivity, source-head, quarantine, fail-closed]
notes:
  - "Documentation-only update paired with a generated provenance receipt."
  - "No connector implementation, validator executable, schema, contract, policy, fixture, test, workflow, lifecycle data, source registry entry, receipt instance other than generated provenance, release record, route, or public artifact behavior changes."
  - "Direct connector writes are limited to RAW or QUARANTINE plus receipts; WORK and later stages are downstream pipeline responsibilities."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Connector Admission Readiness Validator Boundary

`tools/validators/connector_gate/`

> Validate whether a declared connector or intake attempt is ready for the next governed pre-RAW action without running the connector, storing credentials, admitting a source, writing payloads, or granting policy, release, or publication authority.

<p>
  <img alt="Status draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Implementation README only" src="https://img.shields.io/badge/implementation-README__only-orange">
  <img alt="Boundary pre RAW" src="https://img.shields.io/badge/boundary-pre--RAW-blueviolet">
  <img alt="Network denied" src="https://img.shields.io/badge/network-denied__by__default-critical">
  <img alt="Route raw quarantine receipts only" src="https://img.shields.io/badge/direct__route-RAW__%7C__QUARANTINE__%7C__receipts-red">
  <img alt="Authority validator only" src="https://img.shields.io/badge/authority-validator__only-informational">
</p>

> [!IMPORTANT]
> No direct connector-gate executable or dedicated tests were established. The connector-gate workflow is TODO-only. A real SourceDescriptor shape validator exists, but its schema, validator, fixture, role, and activation authorities are internally conflicted. This README therefore documents a bounded future contract and current evidence; it does not claim source-admission enforcement.

**Quick links:** [Purpose](#purpose) · [Status](#status) · [Placement](#placement) · [Vocabulary](#vocabulary) · [Gate phases](#phases) · [Topology](#topology) · [Authority and routes](#routes) · [Conflict register](#conflicts) · [Input packet](#packet) · [Dependency envelope](#dependencies) · [Descriptor checks](#descriptor) · [Connector checks](#connector) · [Access and secrets](#access) · [Source-head checks](#source-head) · [Probe and capture](#probe) · [Lifecycle routing](#lifecycle) · [Receipts](#receipts) · [Rights and sensitivity](#sensitivity) · [Report](#report) · [Invariants](#invariants) · [Outcomes](#outcomes) · [Reason codes](#reason-codes) · [Security](#security) · [Tests](#tests) · [CI](#ci) · [Implementation sequence](#sequence) · [Definition of done](#done) · [Migration](#migration) · [Correction and rollback](#rollback) · [Open verification](#open) · [Evidence ledger](#ledger) · [Changelog](#changelog)

---

<a id="purpose"></a>

## Purpose

This lane answers a phase-specific readiness question:

> Given a pinned source descriptor, connector identity, activation context, requested action, declared endpoint or local-input plan, source-head or capture observations, intended lifecycle route, and policy/evidence dependencies, may the caller continue to the next pre-RAW step, or must it stop, abstain, hold, deny, quarantine, no-op, review, or error?

A connector-gate pass means only that the configured checks passed for the exact phase, packet, dependency results, rules, and digests named in the report.

A pass is not:

- a `SourceActivationDecision`;
- permission to make a network request;
- proof that credentials are valid;
- proof that an endpoint is healthy;
- source admission;
- source truth;
- evidence closure;
- policy permission;
- permission to write to RAW;
- release approval;
- public-client access.

[Back to top](#top)

---

<a id="status"></a>

## Status and evidence boundary

**Snapshot:** `main@6829e8daed19521f59a82780974f643771e898eb`

**Prior target blob:** `bfd5ff3875509f46e050c980891e23841cbae53e`

| Surface | Status | Consequence |
|---|---|---|
| Direct `connector_gate/` lane | **CONFIRMED README-only in bounded search** | Do not claim executable behavior. |
| Direct gate executable | **NOT ESTABLISHED** | CLI, registry id, exit codes, report emission, and consumers remain proposed. |
| Dedicated gate tests | **NOT ESTABLISHED** | No pass rate or refusal coverage is claimed. |
| Connector-gate workflow | **CONFIRMED TODO-only** | Workflow success cannot prove enforcement. |
| Connectors root | **CONFIRMED governed boundary** | Direct outputs are RAW or QUARANTINE plus receipts; later stages are outside connector authority. |
| Connectors-core package | **CONFIRMED Python placeholder** | No shared runtime maturity is inferred. |
| SourceDescriptor singular schema | **CONFIRMED fielded and closed; status PROPOSED** | Strongest current machine-shape candidate. |
| SourceDescriptor plural schema | **CONFIRMED empty and permissive** | Cannot replace the fielded schema without migration. |
| SourceDescriptor validator | **CONFIRMED top-level executable** | Runs singular schema and observed fixture family. |
| Shared aggregate | **CONFIRMED five entrypoints including SourceDescriptor** | SourceDescriptor shape is aggregate-covered; connector gate is not. |
| SourceDescriptor fixtures | **CONFIRMED one valid and one invalid** | Real but narrow schema coverage. |
| SourceActivationDecision | **CONFIRMED doctrine; implementation NOT ESTABLISHED** | Gate cannot mint or assume an activation decision. |
| Source authority register | **CONFIRMED file; zero entries** | No active-source inventory is established from this register. |
| IngestReceipt schema | **CONFIRMED fielded and closed** | Dedicated validator path is absent. |
| Source/rights/sensitivity policy | **CONFIRMED greenfield README stubs** | Automated admissibility is unestablished. |
| Production consumers, reports, decisions, receipts, and metrics | **UNKNOWN** | No operational behavior is claimed. |

Bounded absence is not historical or global proof. Generated, ignored, branch-local, dynamically loaded, unindexed, package-local, or externally deployed implementations remain possible.

[Back to top](#top)

---

<a id="placement"></a>

## Directory Rules and authority

| Responsibility | Owning home | This lane's relationship |
|---|---|---|
| Connector-gate validator implementation | `tools/validators/connector_gate/` | Check declared readiness rules only. |
| Shared validator mechanics | `tools/validators/_common/` | Deterministic local validation support. |
| SourceDescriptor validation | Verified source validator entrypoint | Dependency; not duplicated here. |
| SourceDescriptor meaning | `contracts/source/` | Semantic authority. |
| Machine shape | `schemas/contracts/v1/` | Schema authority after drift resolution. |
| Source registry and activation records | `data/registry/sources/` and accepted control-plane homes | Admission authority; read-only dependency. |
| Connector implementation | `connectors/` | Performs source-specific probes/fetches under orchestration. |
| Shared connector primitives | `packages/connectors-core/` | Reusable helpers after implementation; no authority. |
| Source payloads | `data/raw/` or `data/quarantine/` | Connector handoff destinations. |
| Process memory | `data/receipts/` | Stores ingest/probe/no-op/denial receipts. |
| Rights, sensitivity, and source policy | `policy/` | Decides admissibility and obligations. |
| Evidence/proof support | `data/proofs/` | Downstream claim support, not gate output. |
| Release, correction, withdrawal, rollback | `release/` | Publication and reversibility authority. |
| Tests and fixtures | `tests/` and `fixtures/` | Prove behavior and refusal. |
| Public serving | Governed application/runtime roots | Consumes released public-safe projections only. |

This directory must not become a connector runtime, network client, credential store, source registry, activation ledger, policy engine, payload store, receipt store, proof store, release service, public API, or AI answer authority.

[Back to top](#top)

---

<a id="vocabulary"></a>

## Bounded vocabulary

| Term | Meaning here | Not equivalent to |
|---|---|---|
| Source candidate | Proposed external/internal source identity before activation. | Admitted source. |
| `SourceDescriptor` | Versioned governance record for source identity and treatment. | Source truth or release approval. |
| `SourceActivationDecision` | Governed decision allowing a source to operate in a stated scope. | Connector-gate report. |
| Connector | Source-specific transport/probe/capture implementation. | Source authority. |
| Watcher | Observes change or emits pre-RAW signals. | Publisher. |
| Intake adapter | Local upload, manual curation, file drop, or event intake implementation. | Bypass around source admission. |
| Source-head observation | ETag, Last-Modified, revision, length, checksum, or equivalent observation. | Content proof by default. |
| Probe | Bounded attempt to observe endpoint/source behavior. | Admission or ingest. |
| Capture | Acquisition of source bytes or a governed pointer. | Validation, evidence, or release. |
| `IngestReceipt` | Digest-pinned source-capture process memory. | SourceDescriptor, PolicyDecision, EvidenceBundle, or ReleaseManifest. |
| Connector-gate report | Readiness findings for a specific phase. | Activation decision or lifecycle transition. |
| RAW | Source-native admitted capture. | Public or processed truth. |
| QUARANTINE | Isolated material needing review, correction, or denial. | Failure to preserve evidence. |
| WORK | Downstream transformation workspace. | Direct connector output. |

[Back to top](#top)

---

<a id="phases"></a>

## Gate phases

The gate must declare one phase. A single ambiguous “connector gate” invocation is insufficient.

| Phase | Input being evaluated | Allowed conclusion |
|---|---|---|
| `descriptor_admission_readiness` | Descriptor, registry, rights, sensitivity, role, activation proposal | Ready/not ready for steward admission review. |
| `connector_static_preflight` | Connector declaration, descriptor, endpoint/local-input plan, limits, route | Ready/not ready for fixture or dry-run work. |
| `probe_observation_evaluation` | Bounded probe result produced elsewhere | Continue, no-op, hold, deny, quarantine recommendation, or error. |
| `capture_intake_evaluation` | Capture metadata, digests, IngestReceipt candidate, route | Ready/not ready for governed RAW/QUARANTINE handoff. |
| `source_refresh_revalidation` | Prior descriptor/head/receipt plus current observations | No-op, refresh candidate, hold, quarantine, retire/review, or error. |
| `correction_replay` | Corrected descriptor/policy/source-head and affected lineage | Rerun readiness and identify invalidated dependents. |

The validator itself performs no live network access and writes no lifecycle payload.

[Back to top](#top)

---

<a id="topology"></a>

## Validator topology and delegation

```text
source candidate / connector change / refresh event
  -> SourceDescriptor shape validator
  -> connector admission readiness validator
       - phase and profile
       - connector identity and declared plan
       - activation/review state presence
       - rights/sensitivity/source-role prerequisites
       - endpoint/local-input safety metadata
       - source-head/probe/capture observation consistency
       - allowed RAW/QUARANTINE/receipt route
       - receipt/report dependency presence
  -> source/rights/sensitivity policy
  -> steward SourceActivationDecision or intake decision
  -> connector or intake adapter executes in bounded environment
  -> capture to RAW or QUARANTINE + receipt
  -> downstream pipelines and later lifecycle gates
```

Dependency results are monotonic. The gate cannot upgrade a dependency `DENY`, `HOLD`, `REVIEW_REQUIRED`, `ABSTAIN`, or `ERROR` into a render-, fetch-, or admit-permitting result.

[Back to top](#top)

---

<a id="routes"></a>

## Authority and direct route law

The connector root establishes the direct handoff:

```text
external source
  -> connector
  -> RAW or QUARANTINE + receipts
  -> downstream pipelines
  -> WORK
  -> PROCESSED
  -> CATALOG / TRIPLET
  -> PUBLISHED
```

Therefore:

- `RAW` is permitted only after governed admission prerequisites and orchestration authorize the capture.
- `QUARANTINE` is the safe route for unresolved rights, sensitivity, identity, content, integrity, or review.
- Receipts may record success, partial capture, failure, denial, rate limit, no-op, or quarantine.
- A connector must not directly write `WORK`, `PROCESSED`, `CATALOG`, `TRIPLET`, `PUBLISHED`, proof, release, API, UI, or AI surfaces.
- The gate may recommend a route; it does not execute or authorize the write.
- A file path alone does not prove the lifecycle transition was governed.

[Back to top](#top)

---

<a id="conflicts"></a>

## Conflict and drift register

| Conflict | Confirmed evidence | Safe default |
|---|---|---|
| Singular vs plural SourceDescriptor schema | `source/` is fielded/closed; `sources/` is empty/permissive but named canonical | Pin the fielded schema explicitly until accepted migration; do not silently switch. |
| Validator path | Top-level executable exists; schema names `tools/validators/sources/...` which is absent | Use only a registry/entrypoint accepted by review; report drift. |
| Fixture root | Executable/common harness uses `fixtures/contracts/v1/source/...`; schema metadata names `tests/fixtures/sources/...` | Pin observed fixture root; do not claim metadata alignment. |
| Source-role vocabulary | Seven-role doctrine differs from fielded schema's detailed role enum | Require an accepted profile/crosswalk; otherwise `HOLD`. |
| Activation vocabulary | ADR states `denied`, `draft`, `active_internal`, `active_public_candidate`, `retired`; schema connector state uses `disabled`, `fixture_only`, `live_candidate`, `live_active`, `quarantined`, `retired` | Do not infer equivalence; require a pinned activation profile. |
| Activation object | Doctrine names `SourceActivationDecision`; representative contract/schema paths were absent | Treat decision as required external dependency where configured; do not mint it locally. |
| Receipt naming | Doctrine uses `SourceIntakeRecord` and ingest `RunReceipt`; a fielded `IngestReceipt` also exists | Require a profile naming the expected receipt family and relationships. |
| Policy root | `policy/source/` exists as stub; doctrine also names `policy/sources/` | No implicit fallback; require configured policy refs or fail closed. |
| Authority register | File exists with `entries: []` | Do not infer active sources from documentation or connector presence. |
| Connector path patterns | Family, nested-product, flat-product, compound, and source-package patterns coexist | Connector identity must be explicit; path convention is not authority. |
| Workflow maturity | Connector-gate jobs echo TODO | CI presence is not enforcement. |

These are design inputs for ADR or migration work, not license for the validator README to choose canon.

[Back to top](#top)

---

<a id="packet"></a>

## Proposed immutable gate packet

```yaml
packet_version: kfm.connector_gate_packet.v1
request_id: gate_<stable-id>
phase: <descriptor_admission_readiness|connector_static_preflight|probe_observation_evaluation|capture_intake_evaluation|source_refresh_revalidation|correction_replay>
requested_action: <fixture|dry_run|probe|capture|refresh|replay>
source:
  source_id: <stable source id>
  descriptor_ref: <immutable ref>
  descriptor_digest: <sha256>
  descriptor_version: <version>
  schema_ref: <pinned schema>
  schema_digest: <sha256>
  registry_ref: <registry snapshot ref>
  activation_decision_ref: <ref or null>
  activation_profile_ref: <profile ref>
connector:
  connector_ref: <stable code/package ref>
  connector_digest: <sha256>
  connector_version: <version>
  entrypoint: <declared entrypoint>
  config_digest: <redacted config digest>
  fixture_refs: []
plan:
  endpoint_or_input_ids: []
  method: <HEAD|GET|API|FILE|UPLOAD|MANUAL|EVENT>
  expected_media_types: []
  expected_formats: []
  max_bytes: <bounded integer>
  timeout_ms: <bounded integer>
  redirect_policy_ref: <ref>
  retry_policy_ref: <ref>
  network_mode: denied
route:
  proposed_destination: <RAW|QUARANTINE|NO_OP|STOP>
  domain: <domain>
  source_segment: <source id>
observations:
  source_head: <safe metadata or null>
  probe_result_ref: <ref or null>
  capture_manifest_ref: <ref or null>
  ingest_receipt_ref: <ref or null>
dependencies:
  source_descriptor_validation: <result envelope>
  rights: <result envelope>
  sensitivity: <result envelope>
  source_policy: <result envelope>
  review: <result envelope>
  release_or_correction: <result envelope>
execution:
  validator_ref: <registry id + version>
  rule_hash: <sha256>
  profile_hash: <sha256>
  clock_ref: <injected clock>
  max_items: <bounded integer>
```

The packet contains references, hashes, safe metadata, and bounded observations—not secret values, source payloads, tokens, private cookies, or unrestricted response bodies.

[Back to top](#top)

---

<a id="dependencies"></a>

## Proposed dependency-result envelope

Each dependency result should identify:

```yaml
dependency_id: <stable id>
dependency_type: <schema|registry|activation|rights|sensitivity|source_policy|review|receipt|correction|release>
input_ref: <immutable ref>
input_digest: <sha256>
validator_or_policy_ref: <versioned ref>
outcome: <PASS|WARN|FAIL|HOLD|DENY|ABSTAIN|ERROR|REVIEW_REQUIRED>
reason_codes: []
blocking: true
report_ref: <safe ref or null>
evaluated_at: <timestamp>
limitations: []
```

Rules:

- mandatory dependency missing, stale, unknown, or errored means the parent cannot pass;
- negative outcomes remain negative;
- reports are referenced, not copied;
- restricted findings are not exposed in public-safe messages;
- timestamps do not substitute for version or digest identity.

[Back to top](#top)

---

<a id="descriptor"></a>

## SourceDescriptor and activation checks

A mature gate should verify, as configured:

1. Descriptor shape passes the pinned field-complete schema.
2. `source_id`, descriptor version, schema version, and digest match the registry request.
3. Registry record resolves and is not silently superseded, retired, withdrawn, quarantined, or unknown.
4. Source type, domain scope, source role, authority rank, admissibility limits, review state, release state, and lifecycle state are explicit.
5. Rights, sensitivity, cadence, access, citation, source-head, public-release, and governance references are present.
6. Connector reference and declared activation state match the requested connector and phase.
7. Activation/review requirements are satisfied by an external decision where required.
8. Legacy aliases are not used to bypass canonical fields.
9. Public-release metadata is not mistaken for a release decision.
10. Descriptor success is not source truth.

Unknown schema/profile, vocabulary conflict, missing crosswalk, or stale descriptor produces `HOLD`, `ABSTAIN`, `FAIL`, or `ERROR` according to the accepted profile.

[Back to top](#top)

---

<a id="connector"></a>

## Connector identity and static preflight checks

| Check | Required posture |
|---|---|
| Connector identity | Stable ref, version, digest, declared entrypoint, owning lane. |
| Descriptor binding | Connector ref matches the admitted descriptor/profile. |
| Side effects | Imports and static validation do not perform network or writes. |
| Configuration | Schema-bound, redacted, deterministic; no secret values. |
| Endpoint/input declaration | Every target is listed and purpose-scoped. |
| Formats/media types | Explicit allowlist and size expectations. |
| Retry/timeout/cancel | Bounded; rate-limit and `Retry-After` aware where applicable. |
| Redirects | Deny by default or allowlist with hop limit. |
| Storage plan | RAW or QUARANTINE plus receipts only. |
| Fixtures | No-network synthetic/public-safe fixture exists before live work. |
| Logging | Safe metadata only; no credentials or restricted payload fragments. |
| Idempotency/no-op | Repeated identical observations do not silently duplicate captures. |
| Clock/randomness | Injected or recorded where determinism matters. |
| Failure vocabulary | Finite and stable. |

The gate may inspect connector metadata or code declarations. It must not dynamically import untrusted plugins or execute connector code merely to “validate” it.

[Back to top](#top)

---

<a id="access"></a>

## Access, endpoint, and secret posture

- Only approved schemes and hosts may appear in an executable plan.
- URLs with embedded credentials, tokens, signatures, or private query data are denied or redacted.
- DNS, redirect, proxy, and local-address handling must prevent SSRF and metadata-service access.
- Authentication type may be declared; secret material must remain in a secret manager or injected runtime environment.
- Reports may record secret reference identifiers or config digests only when policy permits.
- Credential validation belongs to a bounded runtime adapter, not documentation or static fixtures.
- Terms, account requirements, rate limits, robots/access restrictions, and attribution duties remain explicit.
- Unknown access posture fails closed.
- Public endpoints do not imply unrestricted redistribution or public release.
- Local uploads and manual intake must enforce path allowlists, symlink/traversal denial, file-size limits, archive limits, and safe content handling.

[Back to top](#top)

---

<a id="source-head"></a>

## Source-head and freshness checks

The fielded SourceDescriptor schema supports ETag, Last-Modified, content length, content SHA-256, upstream version, revision id, or an explicit not-applicable reason.

The gate must preserve the distinction:

| Observation | What it may show | What it does not prove |
|---|---|---|
| ETag | Server-selected version token | Cryptographic content identity unless explicitly specified. |
| Last-Modified | Claimed modification time | Completeness, monotonicity, or truth. |
| Content-Length | Transfer size | Content identity. |
| SHA-256 | Byte identity for hashed content | Semantic validity or policy permission. |
| Upstream version/revision | Publisher version label | Byte identity unless bound to digest. |
| HTTP 304/no change | Conditional request outcome | Source still valid for every use. |
| Manual review | Human observation | Deterministic automated identity. |

Freshness is defined by the descriptor cadence/profile. A newly retrieved old artifact is not automatically current. A static historic source is not stale merely because it is old. Unknown source-head posture may produce no-op, hold, quarantine, or abstention; it must not silently become “unchanged.”

[Back to top](#top)

---

<a id="probe"></a>

## Probe and capture evaluation

The validator does not make network requests. A connector or sandboxed probe runner may produce a bounded observation envelope for evaluation.

A probe/capture envelope should include:

- connector and source refs;
- endpoint/input id, method, start/finish time, and safe status category;
- redirect count and final approved endpoint id;
- safe headers or metadata allowlisted by profile;
- source-head observation;
- bytes observed/captured;
- media type and format;
- content/archive member counts and limit results;
- digest refs;
- rate-limit/retry/no-op state;
- error category;
- proposed RAW/QUARANTINE route;
- receipt candidate ref.

Full response bodies, credentials, cookies, signed URLs, private file paths, restricted coordinates, and unbounded stack traces do not belong in the gate packet or report.

[Back to top](#top)

---

<a id="lifecycle"></a>

## Lifecycle routing checks

| Proposed direct route | Gate posture |
|---|---|
| `RAW` | Conditional: descriptor/activation/policy/identity/integrity prerequisites pass and orchestration owns the write. |
| `QUARANTINE` | Safe default for unresolved, restricted, malformed, partial, suspicious, or review-required material. |
| `NO_OP` | Allowed when pinned rules establish no meaningful source change and a no-op receipt is emitted where required. |
| `STOP` | Used for deny, retired source, invalid connector, secret exposure, policy block, or unsafe operation. |
| `WORK` | **DENY as direct connector output.** Downstream pipeline responsibility. |
| `PROCESSED` | **DENY.** |
| `CATALOG` / `TRIPLET` | **DENY.** |
| `PUBLISHED` | **DENY.** |
| Proof or release homes | **DENY as connector payload destination.** |
| Public API/UI/AI | **DENY.** |

The gate may recommend `RAW`, `QUARANTINE`, `NO_OP`, or `STOP`; a governed caller with lifecycle authority performs the transition and emits the required decision/receipt.

[Back to top](#top)

---

<a id="receipts"></a>

## Receipt and process-memory boundary

Current evidence includes a fielded `IngestReceipt` schema with required source/run/time/outcome/byte/digest fields, but its dedicated validator path is absent. Doctrine also names `SourceIntakeRecord` and ingest `RunReceipt`.

Until receipt authority is reconciled:

- profiles must name the required receipt family for each phase;
- a gate report must not masquerade as an ingest or activation receipt;
- `SUCCESS`, `PARTIAL`, and `FAIL` are capture outcomes, not policy or release outcomes;
- `PARTIAL` remains first-class and normally routes to review or quarantine;
- digest mismatch invalidates the capture candidate;
- no-op, denial, rate-limit, and failed attempts remain auditable;
- receipt instances belong under `data/receipts/`, not this directory;
- corrections supersede receipts or link new receipts; they do not rewrite history.

[Back to top](#top)

---

<a id="sensitivity"></a>

## Rights, sensitivity, source role, and public safety

The gate consumes policy and review results; it does not decide them locally.

Fail closed when:

- rights status, license/terms, attribution, redistribution, commercial-use, or consent posture is unknown or incompatible;
- sensitivity is unknown, restricted, location-sensitive, living-person, DNA/genomic, cultural, infrastructure-sensitive, steward-controlled, or otherwise requires review;
- the requested connector or route exceeds the source's admitted domain/claim roles;
- source role or authority is collapsed or silently upgraded;
- precise restricted locations, vulnerability details, living-person identifiers, credentials, or private source-system metadata could enter logs, fixtures, reports, receipts, or public paths;
- redaction/generalization obligations are not defined before outward use;
- a connector's source metadata is treated as EvidenceBundle closure;
- `public_release.allowed` is treated as current release approval.

The most restrictive applicable policy wins. Client-side hiding or later cleanup is not an admission control.

[Back to top](#top)

---

<a id="report"></a>

## Proposed deterministic ConnectorGateReport

```yaml
report_version: kfm.connector_gate_report.v1
report_id: cgr_<content-hash>
request_id: <request id>
phase: <gate phase>
source_id: <source id>
descriptor_ref: <ref>
descriptor_digest: <sha256>
connector_ref: <ref>
connector_digest: <sha256>
profile_ref: <ref>
profile_hash: <sha256>
validator_ref: <registry id>
validator_version: <version>
rule_hash: <sha256>
network_mode: denied
overall_outcome: <PASS|WARN|FAIL|HOLD|DENY|ABSTAIN|ERROR|REVIEW_REQUIRED>
recommended_next_action: <PROCEED_TO_FIXTURE|PROCEED_TO_DRY_RUN|REQUEST_GOVERNED_CAPTURE|ROUTE_QUARANTINE|NO_OP|STOP|REQUEST_REVIEW>
recommended_route: <RAW|QUARANTINE|NO_OP|STOP|null>
findings:
  - finding_id: <stable id>
    outcome: <finite outcome>
    reason_code: <CG_*>
    blocking: true
    dependency_refs: []
    public_safe_message: <bounded message>
dependency_results: []
observed_source_head: <safe summary or null>
receipt_requirements: []
policy_decision_refs: []
review_refs: []
correction_refs: []
rollback_refs: []
input_hashes: {}
limitations: []
```

The recommended action is advisory and cannot replace a `SourceActivationDecision`, `PolicyDecision`, lifecycle transition record, or release decision.

Given identical packet bytes, profiles/rules, dependency results, and validator version, the report body excluding run timestamps should be byte-stable after accepted canonicalization.

[Back to top](#top)

---

<a id="invariants"></a>

## Connector-gate invariants

1. Validator does not perform network access.
2. Validator does not execute connector code.
3. Connector success is not source admission.
4. Source admission is not record-level validity.
5. RAW capture is not promotion.
6. Descriptor metadata is not source truth.
7. SourceDescriptor pass is not activation.
8. Activation is not public release.
9. `public_release.allowed` is not a ReleaseManifest.
10. Source-head observation is not EvidenceBundle closure.
11. ETag is not assumed to be a digest.
12. Last-Modified is not assumed monotonic.
13. Content length is not identity.
14. Matching digest is not semantic validity.
15. No-change response is not universal freshness.
16. Source role cannot be upgraded by connector or gate.
17. Vocabulary conflicts require a pinned profile or `HOLD`.
18. Unknown rights fail closed.
19. Unknown sensitivity fails closed.
20. Unknown activation state fails closed.
21. Missing mandatory dependency cannot pass.
22. Negative dependency outcomes are monotonic.
23. Secrets never enter packets, fixtures, logs, reports, or receipts.
24. Private/signed URLs are redacted or denied.
25. Redirects and targets are allowlisted.
26. Local file intake denies traversal and symlink escape.
27. Resource limits are explicit.
28. Retries are bounded and rate-limit aware.
29. Fixtures precede live connector activation.
30. Fixtures are not production evidence.
31. Watchers are non-publishers.
32. Direct connector destinations are RAW, QUARANTINE, or receipts only.
33. Direct WORK writes are denied.
34. Direct later-stage writes are denied.
35. QUARANTINE is a governed safe state, not deletion.
36. Partial and failed captures remain visible.
37. Gate report is not an IngestReceipt.
38. Receipt is not a PolicyDecision.
39. Receipt is not EvidenceBundle.
40. Receipt is not ReleaseManifest.
41. Reports reference restricted findings without copying them.
42. Public-safe messages reveal no hidden policy thresholds.
43. Corrected/superseded descriptors invalidate dependent readiness reports.
44. Retired or withdrawn sources cannot silently refresh.
45. Cached gate results are bound to input/profile/rule digests.
46. A pass is phase-, action-, source-, connector-, and time-scoped.
47. Human review remains visible when required.
48. Gate cannot authorize its own use or release.

[Back to top](#top)

---

<a id="outcomes"></a>

## Finite outcomes

| Outcome | Meaning | Typical next step |
|---|---|---|
| `PASS` | Configured phase checks passed. | Continue to the separately authorized next action. |
| `WARN` | Accepted non-blocking limitation. | Continue with visible caveat. |
| `FAIL` | Deterministic validation defect. | Correct packet/config/code and rerun. |
| `HOLD` | Governance or dependency state incomplete. | Await steward, rights, sensitivity, or source review. |
| `DENY` | Action or route is explicitly unsafe/disallowed. | Stop; do not fetch/admit/write. |
| `ABSTAIN` | Available evidence is insufficient to decide. | Gather support or keep held. |
| `ERROR` | Validator/dependency/runtime failed. | Repair and rerun; do not infer readiness. |
| `REVIEW_REQUIRED` | Human review is mandatory. | Route to authorized review queue. |

[Back to top](#top)

---

<a id="reason-codes"></a>

## Proposed `CG_` reason-code families

| Family | Examples |
|---|---|
| Packet/profile | `CG_PACKET_INVALID`, `CG_PHASE_MISSING`, `CG_PROFILE_UNKNOWN`, `CG_RULE_HASH_MISMATCH` |
| Source identity | `CG_SOURCE_ID_MISSING`, `CG_DESCRIPTOR_UNRESOLVED`, `CG_DESCRIPTOR_VERSION_MISMATCH` |
| Schema drift | `CG_SCHEMA_AUTHORITY_CONFLICT`, `CG_VALIDATOR_PATH_DRIFT`, `CG_FIXTURE_ROOT_DRIFT` |
| Registry | `CG_REGISTRY_ENTRY_MISSING`, `CG_REGISTRY_EMPTY`, `CG_SOURCE_SUPERSEDED`, `CG_SOURCE_RETIRED` |
| Activation | `CG_ACTIVATION_DECISION_MISSING`, `CG_ACTIVATION_VOCABULARY_CONFLICT`, `CG_CONNECTOR_DISABLED` |
| Role/authority | `CG_SOURCE_ROLE_MISSING`, `CG_SOURCE_ROLE_VOCABULARY_CONFLICT`, `CG_AUTHORITY_LIMIT_EXCEEDED` |
| Rights/access | `CG_RIGHTS_UNKNOWN`, `CG_ACCESS_NOT_ALLOWED`, `CG_TERMS_STALE`, `CG_ATTRIBUTION_GAP` |
| Sensitivity | `CG_SENSITIVITY_UNKNOWN`, `CG_SENSITIVITY_DENY`, `CG_METADATA_LEAK_RISK` |
| Connector | `CG_CONNECTOR_UNKNOWN`, `CG_CONNECTOR_DIGEST_MISMATCH`, `CG_ENTRYPOINT_UNDECLARED` |
| Endpoint/input | `CG_ENDPOINT_UNDECLARED`, `CG_SCHEME_DENIED`, `CG_HOST_DENIED`, `CG_REDIRECT_DENIED` |
| Secrets | `CG_SECRET_VALUE_PRESENT`, `CG_SIGNED_URL_PRESENT`, `CG_PRIVATE_CONFIG_EXPOSED` |
| Resource | `CG_SIZE_LIMIT_MISSING`, `CG_TIMEOUT`, `CG_RETRY_BUDGET_EXCEEDED`, `CG_ARCHIVE_LIMIT_EXCEEDED` |
| Source head | `CG_SOURCE_HEAD_MISSING`, `CG_HEAD_METHOD_UNSUPPORTED`, `CG_DIGEST_MISMATCH`, `CG_FRESHNESS_UNRESOLVED` |
| Probe/capture | `CG_PROBE_RESULT_MISSING`, `CG_MEDIA_TYPE_DENIED`, `CG_CAPTURE_PARTIAL`, `CG_CAPTURE_FAILED` |
| Route | `CG_DIRECT_WORK_WRITE_DENIED`, `CG_LATER_STAGE_WRITE_DENIED`, `CG_ROUTE_INVALID` |
| Receipt | `CG_RECEIPT_PROFILE_CONFLICT`, `CG_INGEST_RECEIPT_MISSING`, `CG_RECEIPT_DIGEST_GAP` |
| Policy/review | `CG_POLICY_MISSING`, `CG_POLICY_DENY`, `CG_REVIEW_REQUIRED` |
| Correction | `CG_CORRECTION_UNAPPLIED`, `CG_SUPERSESSION_UNRESOLVED`, `CG_ROLLBACK_TARGET_MISSING` |
| Operational | `CG_DEPENDENCY_ERROR`, `CG_NETWORK_ACCESS_DENIED`, `CG_INTERNAL_ERROR` |

Reason codes remain proposed until accepted contracts and registries exist. Public messages should expose only safe, actionable summaries.

[Back to top](#top)

---

<a id="security"></a>

## Security and resource posture

- Network is denied in the validator process.
- Live probes run only in a separate bounded connector/sandbox context.
- Packets are size-limited and parsed without executing embedded content.
- Configuration is treated as untrusted data.
- URL schemes, hosts, ports, redirects, and resolved address classes are policy-controlled.
- Local paths are normalized beneath approved roots with symlink and traversal checks.
- Archive recursion, compression ratio, member count, file count, and byte limits are enforced before extraction.
- Media types and formats are allowlisted.
- Logs and reports redact secrets, tokens, cookies, signed parameters, private endpoints, and restricted payload values.
- Regex, parsing, hashing, and decompression have bounded resources.
- Error output is deterministic, bounded, and safe.
- Connector-provided instructions cannot override policy or gate rules.
- Failure or timeout never defaults to `PASS`.

[Back to top](#top)

---

<a id="tests"></a>

## Proposed tests and fixtures

No dedicated connector-gate test lane was established. Future no-network coverage should include:

- complete admitted descriptor and fixture-only connector preflight;
- missing, invalid, superseded, retired, quarantined, or unreviewed descriptor;
- singular/plural schema conflict;
- validator and fixture-root drift;
- role and activation vocabulary conflicts;
- missing activation decision;
- empty authority register;
- rights, access, terms, attribution, and sensitivity gaps;
- disabled, fixture-only, candidate, active, quarantined, and retired connector states;
- undeclared endpoint, unsafe scheme/host/redirect, signed URL, embedded credential, and private-address targets;
- retry, rate-limit, timeout, cancellation, size, content-type, archive, and path limits;
- ETag/Last-Modified/length/digest distinctions;
- 304/no-op, changed head, partial capture, failed capture, and digest mismatch;
- valid RAW route, valid QUARANTINE route, no-op, and stop;
- direct WORK/PROCESSED/CATALOG/TRIPLET/PUBLISHED writes denied;
- missing/invalid IngestReceipt and receipt-family conflict;
- watcher/local-upload/manual-intake boundaries;
- deterministic reruns and correction invalidation.

Anti-tautology controls:

- valid and invalid fixture sets are nonempty;
- every blocking reason family has a negative fixture;
- expected-invalid fixtures fail for the intended reason;
- tests pin descriptor schema, gate profile, policy, and rule hashes;
- fixture-only activation cannot execute a live probe;
- mock network results remain visibly synthetic;
- permissive-schema success is not accepted as semantic completeness.

[Back to top](#top)

---

<a id="ci"></a>

## CI admission contract

The current `connector-gate` workflow is a scaffold with two `echo TODO` steps.

A meaningful future required check should:

1. run with network disabled;
2. validate the accepted SourceDescriptor schema/profile;
3. resolve connector/profile/registry references locally;
4. run positive and negative connector-gate fixtures;
5. assert fixture families are nonempty;
6. validate secret, path, URI, redirect, route, resource, and dependency monotonicity behavior;
7. verify direct WORK and later-stage routes are denied;
8. validate report determinism and safe diagnostics;
9. publish a bounded structured QA artifact;
10. fail on schema/validator/fixture/activation-vocabulary drift;
11. prove IngestReceipt or accepted receipt-profile requirements;
12. retain stable required-check naming through coordinated governance.

Workflow presence, a green echo job, and branch-protection significance are separate facts.

[Back to top](#top)

---

<a id="sequence"></a>

## Smallest sound implementation sequence

1. **ADR/profile decision:** resolve SourceDescriptor schema authority, role/activation vocabularies, SourceActivationDecision, receipt family, and direct-route contract.
2. **Schemas/fixtures:** close gate packet/report schemas and expand nonempty valid/invalid fixtures.
3. **Registry/policy adapters:** define read-only source registry, activation, rights, and sensitivity dependency interfaces.
4. **Validator:** implement one deterministic no-network entrypoint and registry id with finite outcomes and `CG_` reasons.
5. **Connector integration:** add static metadata contracts and sandboxed probe/capture observation envelopes without hidden writes.
6. **CI/correction:** replace TODO workflow steps, prove refusal, correction invalidation, quarantine routing, and rollback.

Each PR should be independently reversible and must not combine generation, approval, activation, and release in one unreviewed path.

[Back to top](#top)

---

<a id="done"></a>

## Definition of done

- [ ] Owners and CODEOWNERS accepted.
- [ ] SourceDescriptor schema authority and migration resolved.
- [ ] Source-role and activation-state vocabularies accepted.
- [ ] SourceActivationDecision meaning and shape accepted.
- [ ] Receipt family and relationships accepted.
- [ ] Connector identity/metadata profile accepted.
- [ ] Gate packet/report schemas closed and versioned.
- [ ] One executable entrypoint and registry id implemented.
- [ ] No-network default enforced.
- [ ] Source registry/activation dependency tested read-only.
- [ ] SourceDescriptor dependency uses pinned field-complete schema.
- [ ] Rights, sensitivity, access, and policy dependencies implemented.
- [ ] RAW/QUARANTINE/receipt-only direct route enforced.
- [ ] Direct WORK and later-stage writes denied.
- [ ] URI, SSRF, secret, path, archive, and resource controls tested.
- [ ] Source-head semantics tested.
- [ ] Ingest/no-op/partial/failure receipt requirements tested.
- [ ] Positive and negative fixture sets nonempty.
- [ ] Reports deterministic and safe.
- [ ] Connector-gate workflow runs real checks.
- [ ] Required-check significance verified.
- [ ] Correction/supersession invalidates affected readiness.
- [ ] Quarantine/review/rollback paths exercised.
- [ ] Documentation matches implementation.

[Back to top](#top)

---

<a id="migration"></a>

## Migration and deprecation

Known drift includes:

- singular fielded versus plural permissive SourceDescriptor schema;
- top-level observed validator versus schema-declared absent validator;
- observed fixture root versus schema-declared fixture root;
- source-role vocabulary conflict;
- activation-state vocabulary conflict;
- absent SourceActivationDecision contract/schema;
- SourceIntakeRecord/IngestReceipt/RunReceipt overlap;
- `policy/source/` versus `policy/sources/`;
- empty authority register;
- mixed connector path patterns;
- TODO-only workflow.

Canonicalization requires an accepted ADR or migration note, explicit versioned adapters/crosswalks, input/output hashes and receipts, shared-corpus comparison during a bounded compatibility window, no weakening of deny/quarantine defaults, deprecation notices, and a tested rollback target. Do not delete legacy paths until consumers and historical references are inventoried.

[Back to top](#top)

---

<a id="rollback"></a>

## Correction, supersession, retirement, and rollback

A gate report becomes stale when any of these change:

- descriptor content/version/schema;
- source role, authority, rights, sensitivity, cadence, access, citation, source head, admissibility, review, release, or lifecycle state;
- activation decision or authority-register entry;
- connector code/version/digest/entrypoint;
- endpoint/input plan;
- profile, policy, rule, or resource limits;
- source-head/probe/capture observation;
- receipt or digest;
- correction, supersession, retirement, withdrawal, or rollback state.

```text
changed dependency
  -> identify affected gate reports and connector runs
  -> mark reports stale/superseded
  -> block or hold new probe/capture as required
  -> identify affected RAW/QUARANTINE captures and downstream derivatives
  -> route to correction, review, withdrawal, or rollback
  -> rerun against pinned corrected inputs
  -> emit new decisions/receipts without erasing history
```

Before merge, close the draft PR and abandon the branch. After merge, revert the README commit and revert or supersede the generated receipt. This documentation change requires no runtime, lifecycle, connector, policy, or release rollback.

[Back to top](#top)

---

<a id="open"></a>

## Open verification register

1. Owners and CODEOWNERS.
2. Accepted SourceDescriptor schema path and version.
3. Singular/plural schema migration.
4. Canonical SourceDescriptor validator path and registry id.
5. Fixture-root convention.
6. Seven-role doctrine to schema-role mapping.
7. ADR activation state to schema connector-state mapping.
8. SourceActivationDecision contract/schema/home.
9. Source authority register ownership and population.
10. Descriptor-level versus record-level admission responsibilities.
11. SourceIntakeRecord/IngestReceipt/RunReceipt relationship.
12. IngestReceipt validator and fixture coverage.
13. Connector identity/manifest/registry contract.
14. Exhaustive connector inventory and path conventions.
15. Connector entrypoint and config schema conventions.
16. Local upload/manual curation/watcher profiles.
17. Endpoint allowlist, redirect, SSRF, proxy, TLS, and DNS posture.
18. Secret-reference and redaction conventions.
19. Retry, rate-limit, timeout, cancellation, and no-op semantics.
20. Source-head canonicalization and freshness policies.
21. Capture manifest and digest requirements.
22. Archive and parser safety limits.
23. RAW/QUARANTINE writer authority.
24. Quarantine entry/review/recovery contract.
25. Policy source/rights/sensitivity paths and runtime.
26. Report schema, home, retention, and public projection.
27. Finite outcomes and reason-code registry.
28. Direct gate executable and shared runtime integration.
29. Dedicated tests and fixture inventory.
30. Workflow implementation and required-check significance.
31. Production consumers and invocation points.
32. Emitted decisions, reports, receipts, and metrics.
33. Source refresh/re-admission cadence.
34. Correction cascade and downstream invalidation.
35. Operational quarantine and rollback drills.
36. Compatibility retirement plan.

Unresolved items remain `NEEDS VERIFICATION`, not repository facts.

[Back to top](#top)

---

<a id="ledger"></a>

## Evidence ledger

| Evidence | Status | Supports | Does not prove |
|---|---|---|---|
| Target README v0.1 | CONFIRMED | Existing lane and prior proposed scope | Executable behavior |
| `connectors/README.md` | CONFIRMED root contract | RAW/QUARANTINE/receipt direct handoff and non-publisher boundary | Child runtime completeness |
| Connectors-core README | CONFIRMED scaffold | Shared-package maturity and documented drift | Implemented primitives |
| SourceDescriptor contract | CONFIRMED draft | Source governance meaning and required semantics | Accepted admission or release |
| Singular SourceDescriptor schema | CONFIRMED fielded/closed | Strong machine-shape candidate and connector-state fields | Canonical authority after conflict |
| Plural SourceDescriptor schema | CONFIRMED empty/permissive | Authority conflict | Semantic completeness |
| Top-level SourceDescriptor validator | CONFIRMED executable | Singular schema/fixture wrapper | Connector-gate behavior |
| SourceDescriptor fixtures README | CONFIRMED narrow fixture family | One valid/one invalid and fixture-root drift | Broad coverage/current pass |
| Source registry README | CONFIRMED documentation | Pre-RAW admission boundary | Populated active registry |
| Source authority register | CONFIRMED file with empty entries | No entries in inspected snapshot | Global absence of admission records |
| Admission Process | CONFIRMED doctrine document | Admission/promotion split and SourceActivationDecision doctrine | Implemented gates |
| ADR-0017 | CONFIRMED proposed ADR | Descriptor/record admission model and activation states | Accepted decision |
| Source-role taxonomy | CONFIRMED doctrine document | Seven-role vocabulary | Schema mapping |
| IngestReceipt contract/schema | CONFIRMED draft/fielded | Capture receipt semantics and shape | Dedicated validator/runtime emission |
| Connector-gate workflow | CONFIRMED TODO-only | Workflow scaffold | Enforcement |
| Validator aggregate | CONFIRMED executable | SourceDescriptor included; connector gate absent | Complete validator coverage |
| Validator tests README | CONFIRMED repository-grounded | Partial coverage and anti-tautology gaps | Direct gate tests |
| Source/rights/sensitivity policy READMEs | CONFIRMED greenfield stubs | Policy homes | Policy automation |
| Directory Rules | CONFIRMED doctrine | Responsibility-root placement | Runtime maturity |
| Generated receipt schema | CONFIRMED schema | Provenance record shape | Human approval |

[Back to top](#top)

---

<a id="changelog"></a>

## Changelog

### v0.2 — 2026-07-16

- Replaced planning language with a repository-grounded pre-RAW validator boundary.
- Recorded README-only direct lane, TODO-only workflow, and absence from the aggregate.
- Recorded working SourceDescriptor validation alongside schema/validator/fixture drift.
- Recorded activation, role, receipt, policy, register, and connector-path conflicts.
- Corrected the direct connector route to RAW or QUARANTINE plus receipts; WORK and later stages are downstream.
- Added phase model, topology, packet, dependency envelope, descriptor/connector/access/source-head/probe/route/receipt controls, report profile, 48 invariants, outcomes, `CG_` reason codes, security, tests, CI, implementation sequence, migration, correction, rollback, verification register, and evidence ledger.
- Added generated-work provenance receipt requirement.

### v0.1 — 2026-07-08

- Replaced a stray one-character file with an initial proposed connector-gate guide.

<p align="right"><a href="#top">Back to top</a></p>
