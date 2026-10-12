<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-domains-archaeology-ingest-readme
title: pipelines/domains/archaeology/ingest/ — Governed Archaeology Source-Admission Boundary
type: readme; directory-readme; domain-pipeline-sublane; source-admission-boundary; sensitive-domain; non-publisher-guardrail
version: v0.2
status: draft; repository-grounded; checked-execution-files-absent; placeholder-spec; placeholder-source-controls; tests-placeholder-heavy; validators-readme-only; workflow-readiness-holds
owners:
  - OWNER_TBD — Archaeology pipeline steward
  - OWNER_TBD — Archaeology domain steward
  - OWNER_TBD — Source and registry steward
  - OWNER_TBD — Ingest and lifecycle steward
  - OWNER_TBD — Cultural-review and sovereignty steward
  - OWNER_TBD — Rights-holder representative
  - OWNER_TBD — Policy and sensitivity steward
  - OWNER_TBD — Evidence and receipt steward
  - OWNER_TBD — Schema and contract steward
  - OWNER_TBD — Validation and CI steward
  - OWNER_TBD — Release and rollback steward
  - OWNER_TBD — Security reviewer
  - OWNER_TBD — Docs steward
created: 2026-06-13
updated: 2026-07-19
supersedes: v0.1
policy_label: public-doc; pipelines; domains; archaeology; ingest; source-admission; sensitive-domain; no-secrets; no-live-source-access; no-source-activation; no-exact-location-exposure; no-site-discovery; no-cultural-authority; no-policy-authority; no-release-authority; no-direct-publication; candidate-not-site; source-role-preserving; evidence-bound; review-gated; rights-aware; sovereignty-aware; correction-aware; rollback-aware
current_path: pipelines/domains/archaeology/ingest/README.md
owning_root: pipelines/
responsibility: preserve the Archaeology ingest execution boundary, current repository maturity, future file-admission contract, and fail-closed handoff from approved source-intake context toward immutable RAW capture or QUARANTINE without owning source access, source authority, object meaning, machine shape, policy, cultural or rights-holder authority, evidence/proof records, lifecycle storage, release decisions, public serving, or protected-location disclosure
truth_posture: CONFIRMED target README and prior blob; pipelines and Archaeology parent responsibilities; exact checked absence of INGEST_CONTRACT.md, run_dry_fixture.py, a dedicated pipeline-test README, and a dedicated reusable ingest-fixture README; ingest.spec.yaml is a seven-line PROPOSED inventory placeholder; the Archaeology source-registry README is grounded but inspected sources.yaml and source_roles.yaml are eight-line PROPOSED placeholders; the domain test lane has thirteen named modules while sampled modules are placeholder docstrings; the broad validator lane is README-only; the domain workflow is read-only and records validation, proof, and release readiness holds; the cross-domain sensitivity ADR is draft, proposed, and number-conflicted; no overlapping open pull request or matching task branch was found / PROPOSED one accepted ingest owner, consumer-bound specification, typed source-intake and raw-capture contracts, deterministic identity and hashing, no-network synthetic first slice, finite results and safe reason codes, immutable RAW or structured QUARANTINE routing, accepted ingest receipt binding, correction propagation, and rollback / CONFLICTED or unresolved pre-RAW event versus WORK intake placement, SourceIntakeRecord and RawCaptureReceipt ownership, source-role vocabulary authority, connector-versus-ingest admission responsibility, and domain-specific versus shared ingest mechanics / UNKNOWN exhaustive recursive inventory, differently named executables, accepted spec parser or registry, active source bindings, concrete SourceDescriptors, fixture payloads, executable tests, substantive CI, emitted receipts, runtime execution, monitoring, branch-protection significance, release integration, deployment, and production consumers / NEEDS VERIFICATION named owners and CODEOWNERS, accepted contracts and schemas, source-role and rights vocabulary, cultural and sovereignty review interfaces, sensitivity profiles, receipt and reason-code schemas, separation of duties, correction consumers, and rollback execution
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 860ccaececd0562dad22694a046215807495f1dc
  target_prior_blob: 6968b9f2876b8ee3b7ec2cf2ad1f27e157b6e566
  archaeology_pipeline_parent_blob: 50873232e09f66b060e94ac32ffe69efde68f541
  archaeology_spec_readme_blob: 7ca798d1482b8599942720d3e566ab2d21584f77
  archaeology_ingest_spec_blob: 4e41ac4f913d01ee38a18a1cf192c6be463388c4
  archaeology_source_registry_blob: 40f859e7b61cec8fb6e27268f2f5b38bcd57bb4f
  archaeology_sources_placeholder_blob: f7931a06c663c95267bf2c65da6519cb5ab2c2cd
  archaeology_source_roles_placeholder_blob: 21c6b6f818d554b2e46748c1a05fa3bb80673e57
  archaeology_test_blob: 229113afacc6acc0839e92318082ccce9e2ceab3
  archaeology_validator_blob: bae2eabb5d29bf7099ed74a66a17c0071ae98557
  archaeology_workflow_blob: 41e377f50ca310eccdc4b716ba8374c4fa8181db
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  sensitivity_adr_blob: 691251190211b32fe47cba1546adb6c93ad5ea76
  checked_absent_paths:
    - pipelines/domains/archaeology/ingest/INGEST_CONTRACT.md
    - pipelines/domains/archaeology/ingest/run_dry_fixture.py
    - tests/pipelines/domains/archaeology/ingest/README.md
    - fixtures/domains/archaeology/ingest/README.md
  concurrency_check: no open pull request matching archaeology ingest README and no branch matching archaeology-ingest were surfaced
  inventory_method: GitHub connector exact file reads, exact expected-path probes, commit inspection, and bounded pull-request/branch queries; absence and maturity conclusions are limited to checked paths and the pinned branch snapshot
related:
  - ../../../README.md
  - ../../README.md
  - ../README.md
  - ../normalize/README.md
  - ../validate/README.md
  - ../catalog/README.md
  - ../publish/README.md
  - ../../../../docs/doctrine/directory-rules.md
  - ../../../../docs/domains/archaeology/README.md
  - ../../../../pipeline_specs/archaeology/README.md
  - ../../../../pipeline_specs/archaeology/ingest.spec.yaml
  - ../../../../data/registry/sources/archaeology/README.md
  - ../../../../data/registry/sources/archaeology/sources.yaml
  - ../../../../data/registry/sources/archaeology/source_roles.yaml
  - ../../../../contracts/domains/archaeology/README.md
  - ../../../../schemas/contracts/v1/domains/archaeology/README.md
  - ../../../../policy/domains/archaeology/README.md
  - ../../../../tests/domains/archaeology/README.md
  - ../../../../tools/validators/archaeology/README.md
  - ../../../../docs/adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md
  - ../../../../.github/workflows/domain-archaeology.yml
  - ../../../../data/receipts/generated/README.md
  - ../../../../schemas/contracts/v1/receipts/generated_receipt.schema.json
tags: [kfm, pipelines, archaeology, ingest, source-admission, raw, quarantine, source-descriptor, source-role, rights, cultural-review, sovereignty, sensitivity, receipts, correction, rollback]
notes:
  - "v0.2 replaces a design-forward proposed executable tree and pseudo-machine receipt example with a commit-pinned maturity, authority, file-admission, and implementation-graduation boundary."
  - "The checked ingest sublane has a README, while the expected local execution contract and no-network runner were absent at their checked paths; exhaustive differently named content remains UNKNOWN."
  - "The declarative ingest specification and inspected Archaeology source-control files are placeholders and activate no source or executable behavior."
  - "This documentation-only revision changes no executable code, source activation, specification, contract, schema, policy rule, fixture, test, workflow, lifecycle record, receipt instance, proof, release object, runtime behavior, route, map, AI answer, or protected payload."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `pipelines/domains/archaeology/ingest/` — Governed Archaeology Source-Admission Boundary

> **One-line purpose.** Preserve a reviewable, fail-closed execution boundary for future Archaeology source admission into immutable RAW capture or structured QUARANTINE—without turning a connector payload, source-registry placeholder, candidate detection, workflow result, or generated summary into archaeological truth, cultural authority, release approval, or public location disclosure.

<p>
  <img alt="Status: repository-grounded draft" src="https://img.shields.io/badge/status-repository--grounded%20draft-yellow">
  <img alt="Implementation: not established at checked paths" src="https://img.shields.io/badge/implementation-not__established-critical">
  <img alt="Specification: placeholder" src="https://img.shields.io/badge/spec-placeholder-orange">
  <img alt="Source controls: placeholders" src="https://img.shields.io/badge/source__controls-placeholders-orange">
  <img alt="Sensitivity: deny by default" src="https://img.shields.io/badge/sensitivity-deny__by__default-critical">
  <img alt="Publication: denied" src="https://img.shields.io/badge/publication-DENIED-red">
</p>

**Path:** `pipelines/domains/archaeology/ingest/README.md`  
**Version:** `v0.2`  
**Owning root:** [`pipelines/`](../../../README.md) — executable pipeline logic, the **how**  
**Parent lane:** [`pipelines/domains/archaeology/`](../README.md) — Archaeology-domain execution routing  
**Declarative companion:** [`pipeline_specs/archaeology/ingest.spec.yaml`](../../../../pipeline_specs/archaeology/ingest.spec.yaml) — current seven-line `PROPOSED` placeholder  
**Source-control companion:** [`data/registry/sources/archaeology/`](../../../../data/registry/sources/archaeology/README.md) — grounded control-lane README with inspected placeholder registry files  
**Public posture:** no direct public path; no site confirmation, source activation, cultural approval, rights clearance, evidence closure, release decision, map/API serving, or publication  
**Evidence snapshot:** `main@860ccaececd0562dad22694a046215807495f1dc`

> [!IMPORTANT]
> **Current executable ingest behavior is not established by the checked evidence.** The target README exists, but exact probes found no local `INGEST_CONTRACT.md`, no local `run_dry_fixture.py`, no dedicated pipeline-test README, and no dedicated reusable ingest-fixture README. Differently named or external implementation remains `UNKNOWN`; do not turn bounded absence into a permanent repository claim.

> [!CAUTION]
> **The declarative and source-control surfaces are placeholders.** `ingest.spec.yaml` contains seven planning lines. The inspected `sources.yaml` and `source_roles.yaml` each contain eight planning lines. File presence, a `status: PROPOSED` value, or a source name activates nothing and clears no rights, sensitivity, cultural-review, sovereignty, consent, or evidence obligation.

> [!WARNING]
> **Archaeology ingest is a protected-information boundary.** Exact or reverse-engineerable site locations, burial or human-remains context, sacred or culturally restricted knowledge, collection-security detail, looting-risk information, private-landowner detail, consent secrets, steward-only review substance, and transform offsets must not enter public documentation, ordinary fixtures, logs, receipts, workflow summaries, search indexes, map layers, API output, or AI answers.

**Quick navigation:** [Status](#0-status-and-evidence-boundary) · [Purpose](#1-purpose) · [Authority](#2-placement-and-authority) · [Anti-collapse](#3-ingest-anti-collapse-rules) · [Maturity](#4-current-repository-maturity) · [Belongs](#5-what-belongs-here) · [Does not](#6-what-does-not-belong-here) · [Inputs](#7-source-admission-input-boundary) · [Lifecycle](#8-lifecycle-and-finite-result-contract) · [Gates](#9-sensitive-domain-admission-gates) · [Receipt](#10-minimum-ingest-result-and-receipt-obligations) · [Implementation](#11-file-admission-and-smallest-sound-implementation-sequence) · [Testing](#12-tests-fixtures-validation-and-ci) · [Rollback](#13-correction-supersession-and-rollback) · [Done](#14-definition-of-done) · [Open](#15-open-verification-register) · [Evidence](#16-evidence-ledger) · [History](#17-change-history)

---

## 0. Status and evidence boundary

### Current determination

`pipelines/domains/archaeology/ingest/` is an existing Archaeology pipeline-documentation sublane. It is **not** a verified source-admission implementation.

| Surface | Inspected state | Evidence-bounded conclusion |
|---|---:|---|
| Target README | `CONFIRMED` | v0.1 existed; this revision updates it in place. |
| Local execution contract | `NOT FOUND AT CHECKED PATH` | No adopted local ingest contract is established. |
| Local no-network runner | `NOT FOUND AT CHECKED PATH` | No fixture-backed local dry-run entrypoint is established. |
| Declarative ingest spec | `PLACEHOLDER` | `ingest.spec.yaml` has seven planning lines and activates nothing. |
| Archaeology source registry | `GROUNDED README / PLACEHOLDER FILES` | The lane documents source controls; inspected `sources.yaml` and `source_roles.yaml` are placeholders. |
| Parent Archaeology pipeline | `DRAFT README` | Defines the execution boundary; concrete ingest behavior remains unverified. |
| Semantic contracts | `DRAFT / PARTIAL` | An accepted Archaeology ingest contract and object ownership are not established here. |
| Machine schemas | `INDEX / MIXED MATURITY` | Source-intake, raw-capture, ingest-receipt, and quarantine-reason ownership remain verification-bound. |
| Domain policy | `DRAFT / RUNTIME UNKNOWN` | Fail-closed intent exists; accepted evaluator and runtime binding are unverified. |
| Sensitivity ADR | `PROPOSED / CONFLICTED` | Deny-by-default doctrine is documented, but ADR number and acceptance remain unresolved. |
| Broad validator | `README ONLY` | No broad Archaeology validator executable or implemented ValidationReport producer is established. |
| Domain tests | `13 NAMES / PLACEHOLDER-HEAVY` | Named test topology exists; sampled modules are placeholder docstrings and executable enforcement is unestablished. |
| Dedicated pipeline tests | `NOT FOUND AT CHECKED PATH` | No ingest-specific pipeline-test README is established. |
| Reusable ingest fixtures | `NOT FOUND AT CHECKED PATH` | No dedicated reusable ingest-fixture README is established. |
| Domain workflow | `READ-ONLY READINESS HOLDS` | It inspects structural maturity and performs no source admission, validation, proof construction, release, or publication. |
| Runtime / production use | `UNKNOWN` | No execution trace, retained ingest receipt, monitoring surface, deployment, or production consumer was inspected. |

### Safe conclusions

- **CONFIRMED:** the target path and README exist under the executable `pipelines/` responsibility root.
- **CONFIRMED:** current ingest intent is represented by documentation plus placeholder spec and source-control files, not verified executable behavior.
- **CONFIRMED:** connectors, source registries, contracts, schemas, policy, evidence, lifecycle data, tests, validators, release, and public serving remain separate authorities.
- **PROPOSED:** this sublane may own Archaeology-specific source-admission orchestration after placement, contracts, schemas, source controls, interfaces, and tests are accepted.
- **CONFLICTED:** pre-RAW event versus WORK intake placement, connector-versus-ingest admission responsibility, and shared-versus-domain ingest mechanics remain unresolved.
- **UNKNOWN:** exhaustive recursive inventory, differently named modules, live source use, concrete descriptors, runtime consumers, and production behavior.
- **NEEDS VERIFICATION:** every future contract, schema, executable, fixture, test, validator, receipt, source binding, policy evaluator, review handoff, correction consumer, and rollback path.

### Truth and result vocabulary

| Term | Use in this README |
|---|---|
| `CONFIRMED` | Verified at the pinned repository snapshot. |
| `PROPOSED` | Design or behavior not yet established as implementation. |
| `UNKNOWN` | Not resolved by bounded inspection. |
| `NEEDS VERIFICATION` | Checkable, but not verified strongly enough to rely on. |
| `CONFLICTED` | Current evidence exposes overlapping or incompatible claims without an accepted resolution. |
| `ADMIT_RAW` / `HOLD` / `QUARANTINE` / `DENY` / `ERROR` | Proposed ingest result classes for future design discussion; not an adopted machine enum. |

[Back to top](#top)

---

## 1. Purpose

The durable question for this lane is:

> Can a governed Archaeology process admit an approved source-intake packet to immutable RAW capture—or route it to a structured hold—while preserving source identity, source role, rights, cultural and sovereignty review, sensitivity, temporal scope, payload integrity, correction lineage, and downstream rollback dependencies, without exposing protected information or falsely confirming a site?

A mature ingest process may eventually:

- read only explicit, authorized source-intake references or synthetic public-safe fixtures;
- resolve an accepted `SourceDescriptor` and preserve its role, rights, attribution, sensitivity, access, cadence, and review requirements;
- validate immutable payload identity, digest, media type, size, retrieval context, and source vintage;
- create an immutable RAW capture reference only when admission controls close;
- route unresolved, restricted, malformed, conflicted, or unsafe material to a governed QUARANTINE or HOLD result;
- emit a deterministic ingest/run receipt under an accepted receipt family;
- prepare a downstream normalization handoff without normalizing the payload;
- preserve correction, supersession, revocation, withdrawal, and rollback dependencies.

This lane must not:

- fetch from live upstream systems by default;
- activate a source or edit authoritative source controls;
- define Archaeology object meaning, schemas, policy, or cultural authority;
- confirm an archaeological site, burial, feature, chronology, or cultural interpretation;
- create an `EvidenceBundle` from a source payload or descriptor;
- store RAW, QUARANTINE, receipt, review, policy, proof, or release records beside code;
- expose exact or triangulable protected locations;
- normalize, validate, catalog, publish, or serve public artifacts.

[Back to top](#top)

---

## 2. Placement and authority

### Directory Rules basis

The owning root is `pipelines/` because the intended responsibility is executable orchestration. Archaeology remains a domain segment inside that root. Source access belongs under `connectors/`; source identity and admission controls belong under `data/registry/`; object meaning belongs under `contracts/`; machine shape belongs under `schemas/`; policy belongs under `policy/`; lifecycle state belongs under `data/`; release authority belongs under `release/`.

| Responsibility | Owning home | This lane's role |
|---|---|---|
| Archaeology ingest orchestration | `pipelines/domains/archaeology/ingest/` after accepted file admission | Potential execution support only. |
| Declarative run intent | [`pipeline_specs/archaeology/`](../../../../pipeline_specs/archaeology/README.md) | Consumed only after parser, schema, owner, and binding are accepted. |
| Live source access | `connectors/` and approved source-specific packages | External to this lane. |
| Source identity, role, rights, sensitivity, activation | [`data/registry/sources/archaeology/`](../../../../data/registry/sources/archaeology/README.md) and accepted control-plane surfaces | Referenced; never invented or approved here. |
| Archaeology semantic meaning | [`contracts/domains/archaeology/`](../../../../contracts/domains/archaeology/README.md) | Consumed; never redefined here. |
| Machine-checkable shape | [`schemas/contracts/v1/domains/archaeology/`](../../../../schemas/contracts/v1/domains/archaeology/README.md) and accepted source/receipt schema homes | Consumed; never silently selected. |
| Policy and sensitivity | [`policy/domains/archaeology/`](../../../../policy/domains/archaeology/README.md) and accepted shared policy homes | Applied through a verified evaluator; not encoded by README prose. |
| RAW / WORK / QUARANTINE state | governed `data/` lifecycle homes | Written only through accepted lifecycle adapters. |
| Evidence and proof | governed `data/proofs/` homes | Downstream dependency; never synthesized at ingest. |
| Receipts and review records | accepted `data/receipts/` and review homes | Emitted or referenced only through accepted contracts. |
| Tests and validators | [`tests/domains/archaeology/`](../../../../tests/domains/archaeology/README.md), fixtures, and [`tools/validators/archaeology/`](../../../../tools/validators/archaeology/README.md) | Prove behavior; do not confer authority. |
| Release, correction, withdrawal, rollback | `release/` | Downstream authority; ingest cannot publish. |
| Public API, map, search, export, AI | governed applications and released artifacts | No direct access to this lane or internal stores. |

### Pre-RAW boundary note

KFM documents a pre-RAW event family in planning and doctrine. That admission edge must not become an ungoverned parallel lifecycle phase or storage root. Before implementation, reviewers must settle:

1. whether source-intake records are events, WORK candidates, registry/control-plane records, or a typed handoff spanning those responsibilities;
2. which root owns the authoritative record and which roots hold projections;
3. how a connector handoff differs from an ingest admission decision;
4. how correction and replay preserve the original intake event without rewriting RAW;
5. which accepted ADR or contract resolves the placement.

### Authority of this README

This README may define:

- the local documentation boundary;
- current verified maturity;
- admission conditions for future files;
- anti-collapse, sensitivity, security, test, review, correction, and rollback obligations;
- unresolved placement and ownership questions.

It cannot define:

- Archaeology truth or machine shape;
- accepted source roles or rights;
- source activation;
- cultural, sovereignty, consent, or rights-holder authority;
- policy outcomes;
- evidence truth;
- release approval;
- public exposure permission.

[Back to top](#top)

---

## 3. Ingest anti-collapse rules

A future implementation must preserve these distinctions:

```text
connector payload                 != admitted RAW capture
source filename                   != source identity
source registry placeholder       != accepted SourceDescriptor
source reference                  != source activation
valid YAML                        != valid governed run
ingest.spec.yaml existence        != executable pipeline
payload hash match                != rights or cultural clearance
source-role label                 != accepted role assignment
candidate anomaly                 != confirmed archaeological site
historic-map proximity            != archaeological confirmation
RAW capture                       != normalized record
RAW capture                       != EvidenceBundle
ingest receipt                    != ValidationReport or ProofPack
review reference                  != current valid cultural review
policy reference                  != PolicyDecision
generalized geometry              != permission to disclose
workflow success                  != source admission or release
generated summary                 != evidence or cultural authority
merge                             != lifecycle promotion
```

Required invariants:

1. **Candidate status remains explicit.** No source label, score, anomaly, map proximity, OCR extraction, or generated description confirms a site.
2. **Source role is inherited from authority.** Ingest may preserve or reject a role; it may not invent one.
3. **Rights and review are not inferred.** Public availability, an upstream API, or prior publication does not prove reuse rights, cultural authority, consent, or current review.
4. **Sensitivity never decreases by convenience.** Hashing, buffering, aggregation, file renaming, or coordinate removal does not automatically make material public-safe.
5. **RAW is immutable source capture.** Admission preserves source bytes or governed immutable references; it does not silently normalize or repair.
6. **Quarantine is auditable.** Holds and denials require safe reason codes without echoing protected content.
7. **Evidence remains downstream.** An admitted payload can support later evidence work but is not itself an admissible `EvidenceBundle`.
8. **Lifecycle state remains explicit.** Intake, RAW, WORK, QUARANTINE, PROCESSED, CATALOG/TRIPLET, release candidate, and PUBLISHED remain separate.
9. **Correction and rollback stay attached.** A replay or re-pull must reference the prior intake, source state, affected downstream artifacts, and rollback targets.
10. **No public client bypass exists.** Public surfaces use governed APIs and released artifacts, never source systems or internal lifecycle stores.

[Back to top](#top)

---

## 4. Current repository maturity

### Placeholder specification

The current [`ingest.spec.yaml`](../../../../pipeline_specs/archaeology/ingest.spec.yaml) is inventory scaffolding:

```yaml
status: PROPOSED
source_doc: docs/domains/archaeology/MISSING_OR_PLANNED_FILES.md
path: pipeline_specs/archaeology/ingest.spec.yaml
notes:
  - Placeholder created from docs/domains markdown inventory.
```

It does not define:

- a specification identity or version;
- parser or consumer binding;
- source descriptor references;
- input and output contracts;
- accepted lifecycle transitions;
- review, rights, sensitivity, evidence, or receipt gates;
- deterministic reason codes;
- fixtures, tests, schedules, or rollback behavior.

### Placeholder source controls

The inspected `sources.yaml` and `source_roles.yaml` each declare `status: PROPOSED` and point to planning documentation. They do not establish:

- a concrete active source inventory;
- accepted source roles;
- rights or attribution state;
- cultural or sovereignty authority;
- access class or sensitivity profile;
- source activation decisions;
- ingest eligibility.

### Workflow posture

The [`domain-archaeology` workflow](../../../../.github/workflows/domain-archaeology.yml):

- runs on pull requests, pushes to `main`, and manual dispatch;
- has read-only contents permission;
- checks selected Archaeology boundary paths;
- rejects unexpected maturity drift;
- records explicit validation, proof, and release readiness holds;
- performs no source access, admission, payload processing, lifecycle write, proof build, release, deployment, or publication.

A green workflow result is structural readiness evidence only. It is not an ingest receipt, source activation, cultural approval, policy decision, evidence closure, or release.

### Safety consequence

The safe default remains documentation-only and no-network. Live source acquisition, source activation, payload admission, and protected-data handling are out of scope until an accepted implementation packet exists.

[Back to top](#top)

---

## 5. What belongs here

Only files whose primary responsibility is Archaeology-specific source-admission execution may be admitted after contracts, placement, source controls, and tests close.

Potential future responsibilities include:

- loading an explicit source-intake record or synthetic fixture reference;
- resolving accepted source-control records through a governed interface;
- validating payload digests, sizes, media types, timestamps, and immutable capture requirements;
- preserving source identity, source role, source vintage, rights, attribution, access, sensitivity, and review requirements;
- creating an immutable RAW capture reference through an accepted adapter;
- routing unresolved or unsafe cases to structured QUARANTINE or HOLD results;
- emitting an accepted ingest/run receipt;
- creating a downstream normalization handoff reference;
- recording correction, supersession, revocation, replay, and rollback dependencies.

A file does not belong merely because it reads a source, writes a file, validates YAML, or contains the word `ingest`.

[Back to top](#top)

---

## 6. What does not belong here

| Does not belong | Correct responsibility home |
|---|---|
| Live API clients, scrapers, downloaders, and watchers | `connectors/` and accepted source-specific packages |
| SourceDescriptor records, source roles, rights, sensitivity, and activation decisions | `data/registry/`, `control_plane/`, policy, and accepted review homes |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG/TRIPLET, or PUBLISHED payloads | Governed `data/` lifecycle homes |
| Archaeology domain doctrine | `docs/domains/archaeology/` |
| Object meaning | `contracts/domains/archaeology/` |
| JSON Schema and schema registries | `schemas/` and accepted registry homes |
| Policy rules or evaluator implementation | `policy/` and verified policy-runtime packages |
| Cultural, steward, rights-holder, sovereignty, consent, or revocation decisions | Accepted review/governance record homes |
| EvidenceBundle, ProofPack, or ValidationReport records | Governed proof, report, and receipt homes |
| Reusable fixtures and executable tests | `fixtures/` and `tests/` |
| Shared ingest mechanics | Accepted shared package or pipeline home |
| Release candidates, manifests, promotion decisions, corrections, withdrawals, rollback cards | `release/` |
| Public API, map, tile, search, graph, export, screenshot, or AI behavior | Governed app/runtime roots and released artifacts |
| Exact or reverse-engineerable locations and protected cultural substance | Restricted governed stores only; never public docs or ordinary logs |
| Credentials, tokens, private endpoints, consent secrets, transform offsets | Secret manager or governed restricted stores |

[Back to top](#top)

---

## 7. Source-admission input boundary

A future ingest run must use explicit references. It must not discover authority from filenames, folder proximity, environment variables, or unrestricted network access.

### Candidate input packet

An accepted input packet should eventually bind, by reference:

| Input | Minimum purpose | Failure posture |
|---|---|---|
| Specification identity | Select the reviewed ingest intent and consumer version. | `ERROR` or `HOLD` if absent or unsupported. |
| Source control reference | Resolve source identity, role, rights, attribution, access, sensitivity, cadence, and review requirements. | `QUARANTINE` or `DENY` if unresolved. |
| Source-intake record | Identify the handoff, retrieval context, source vintage, and intended lifecycle entry. | `HOLD` if missing or ambiguous. |
| Payload manifest | Bind digest, size, media type, immutable reference, and capture time. | `QUARANTINE` on mismatch. |
| Review and policy references | Declare required cultural, sovereignty, rights-holder, sensitivity, embargo, consent, and revocation state. | `DENY` or `HOLD` when required state is absent. |
| Prior correction context | Link re-pulls or replay to superseded intake and affected downstream artifacts. | `HOLD` if correction lineage is required but absent. |
| Execution context | Bind run identity, code/spec digests, environment class, and no-network posture. | `ERROR` if reproducibility fields are unavailable. |

### Prohibited implicit inputs

A future implementation must not treat these as authority:

- a source URL alone;
- a source filename or directory name;
- public availability;
- a prior cached copy;
- a database row without a current source-control reference;
- a human-readable review note without a typed current decision;
- a policy path without a verified evaluator result;
- a source-role string supplied by ingest code;
- model confidence, geocoding proximity, or generated interpretation.

[Back to top](#top)

---

## 8. Lifecycle and finite-result contract

### Lifecycle position

The canonical lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A pre-RAW intake event may govern the admission edge, but it does not authorize a shortcut or create a public path.

A future ingest process should:

1. receive an explicit source-intake packet or synthetic fixture;
2. resolve accepted source, rights, sensitivity, review, and policy context;
3. verify immutable payload identity and capture requirements;
4. return exactly one terminal admission result;
5. write only through accepted lifecycle and receipt adapters;
6. produce no normalization, validation-pass, catalog, proof, release, or public-serving side effect.

### Proposed result classes

These labels are design guidance, not an adopted schema enum:

| Result | Meaning | Allowed output |
|---|---|---|
| `ADMIT_RAW` | Required admission controls close for an immutable source-bound capture. | RAW reference, ingest receipt, normalization handoff reference. |
| `HOLD` | Required human, cultural, rights, sovereignty, consent, embargo, or policy state is pending. | Safe hold record and receipt; no RAW or public output. |
| `QUARANTINE` | Payload, source-control, integrity, schema, or safety requirements fail deterministically. | Quarantine reference and safe reason codes. |
| `DENY` | Policy or authority explicitly prohibits admission for the requested use. | Denial receipt with safe obligations; no protected echo. |
| `ERROR` | Infrastructure or execution failed before a governed result could close. | Error receipt and repair target; no silent allow. |

No failure may fall back to `ADMIT_RAW`.

[Back to top](#top)

---

## 9. Sensitive-domain admission gates

Every future ingest run must fail closed unless applicable gates close through accepted implementations.

### Required gates

1. **Specification gate** — accepted spec identity, version, digest, owner, parser, and executable consumer binding.
2. **Source authority gate** — source identity, source role, rights, attribution, access class, cadence, source vintage, and activation state.
3. **Payload integrity gate** — immutable reference, digest, size, media type, retrieval/capture time, and source correlation.
4. **Candidate boundary gate** — anomaly, OCR extraction, geocode, map proximity, remote-sensing detection, model output, or source lead remains a candidate.
5. **Sensitivity gate** — exact or reverse-engineerable location, burial/human-remains, sacred/culturally restricted, collection-security, looting-risk, private-land, and steward-only material defaults to deny or hold.
6. **Cultural and sovereignty gate** — authority-to-control, consultation, CARE, consent, revocation, embargo, and allowed representation are explicit where applicable.
7. **Policy evaluator gate** — policy version, input digest, result, reason codes, obligations, and evaluator identity are recorded.
8. **No-public gate** — ingest outputs cannot be served to public clients, maps, search, graph, exports, screenshots, or AI.
9. **Quarantine-safety gate** — reason codes and diagnostics reveal no protected coordinates, identifiers, cultural substance, or reversible transform parameters.
10. **Receipt gate** — every terminal result emits a deterministic accepted receipt with input/output references and digests.
11. **No-side-effect gate** — no normalization, validation pass, evidence closure, catalog, proof, release, deployment, or publication occurs.
12. **Correction and rollback gate** — replay, re-pull, or source change identifies affected prior intake and downstream invalidation targets.

### Deny-by-default status

The repository contains a deny-by-default Archaeology ADR, but it is `draft`, `proposed`, and number-conflicted. This README preserves the broader fail-closed doctrine without promoting that ADR to accepted status or claiming executable enforcement.

[Back to top](#top)

---

## 10. Minimum ingest result and receipt obligations

This README does not define a receipt schema. It records obligations that an accepted contract should make machine-checkable.

A future result should bind:

### Identity and reproducibility

- stable run ID and ingest pipeline ID;
- specification ID, version, and digest;
- code or executable digest;
- source-control reference and digest;
- source-intake record reference;
- payload manifest reference and digest;
- deterministic execution-time and environment class;
- replay/correction correlation identifiers.

### Decision context

- source role and source vintage;
- rights and attribution state;
- sensitivity and access class;
- cultural, sovereignty, consent, revocation, embargo, and review references where applicable;
- policy decision reference, version, result, reason codes, and obligations;
- payload-integrity checks;
- candidate-versus-confirmed state;
- no-network or approved-network posture.

### Terminal outcome

- one terminal result class;
- RAW, HOLD, QUARANTINE, or error reference as applicable;
- safe reason codes;
- normalization handoff reference only for `ADMIT_RAW`;
- no protected payload echo;
- no release or public artifact reference.

### Correction and rollback

- prior intake or source version superseded;
- affected downstream artifact references when known;
- correction notice or reprocessing trigger reference;
- rollback target owned by the appropriate downstream authority;
- retention and deletion obligations where lawful and policy-approved.

An ingest receipt is process provenance. It is not archaeological evidence, cultural authority, a policy decision, a ValidationReport, an EvidenceBundle, a ProofPack, release approval, or publication.

[Back to top](#top)

---

## 11. File admission and smallest sound implementation sequence

### File admission rule

Do not add an executable merely because the README names a future responsibility. A new file under this sublane should be admitted only when the pull request can identify:

- the accepted responsibility owner;
- the accepted spec and executable consumer binding;
- input and output contracts plus schema versions;
- source-control and policy interfaces;
- no-network synthetic fixtures;
- deterministic tests and safe diagnostics;
- receipt destination and contract;
- correction and rollback behavior;
- workflow effect and rollback plan;
- why the file belongs here instead of a shared ingest package or connector.

### Smallest sound implementation sequence

1. **Resolve ownership and placement.** Decide connector-versus-ingest responsibility, shared-versus-domain mechanics, pre-RAW/WORK record ownership, and receipt family.
2. **Accept the contracts.** Define or adopt `SourceIntakeRecord`, payload manifest, raw-capture result, quarantine result, and ingest receipt semantics.
3. **Accept machine schemas and reason codes.** Bind versions, finite outcomes, safe diagnostics, correction fields, and no-public guarantees.
4. **Graduate the declarative spec.** Replace the placeholder only after a parser, consumer, owner, source bindings, validators, and rollback are reviewable.
5. **Add one synthetic no-network fixture packet.** It must contain no real site, coordinate, cultural, landowner, collection-security, or reverse-engineerable detail.
6. **Implement one narrow dry-run path.** Prove one admissible synthetic packet reaches an in-memory or isolated RAW adapter and one defective packet reaches QUARANTINE.
7. **Add executable negative tests.** Missing rights, source role, digest, review, sensitivity, or policy must fail closed.
8. **Emit a deterministic receipt.** Validate it against the accepted schema and recompute hashes.
9. **Wire CI deliberately.** Replace readiness holds only when the executable suite is nonempty, deterministic, no-network, and independently reviewed.
10. **Run correction and rollback drills.** Prove a source change or revoked review invalidates the admission and blocks downstream use.

Do not begin with live source fetching, bulk source activation, exact coordinates, public layers, AI summaries, or release wiring.

[Back to top](#top)

---

## 12. Tests, fixtures, validation, and CI

### Minimum executable test families

A first accepted suite should cover:

- accepted synthetic packet returns only `ADMIT_RAW`;
- missing or unsupported spec returns `ERROR` or `HOLD`;
- missing source-control reference fails closed;
- placeholder or inactive source control cannot activate a run;
- missing or ambiguous source role fails closed;
- payload digest, size, or media-type mismatch routes to QUARANTINE;
- unresolved rights, attribution, cultural review, sovereignty, consent, revocation, embargo, sensitivity, or policy blocks admission;
- candidate anomaly never becomes a confirmed site;
- protected coordinates and identifiers never appear in diagnostics, snapshots, receipts, workflow summaries, or result objects;
- RAW adapter is immutable and receives no normalized rewrite;
- no validation-pass, EvidenceBundle, catalog, proof, release, public API, map, search, graph, export, or AI side effect occurs;
- receipts are deterministic and schema-valid;
- replay and correction preserve prior lineage and identify downstream invalidation targets;
- network access is denied unless an explicitly reviewed test profile authorizes it.

### Fixture rules

Fixtures must be:

- synthetic and public-safe;
- deterministic and minimal;
- free of real coordinates, site IDs, burial/human-remains detail, sacred or culturally controlled knowledge, private-land detail, collection-security information, and transform secrets;
- labeled as synthetic so they cannot be mistaken for evidence;
- stored under the accepted fixture responsibility root, not beside pipeline code;
- reviewable for reverse-inference risk.

### Current CI consequence

The current domain workflow may run on a documentation PR, but its Archaeology jobs are readiness holds. Report them as workflow results, not proof that ingest behavior passed. No agent should rerun, bypass, or reinterpret privileged workflows without explicit authority.

### Validation required before implementation graduation

- Markdown, meta-block, relative-link, and security checks for this README;
- contract and schema validation for machine artifacts;
- nonempty pytest collection;
- no-network enforcement;
- deterministic receipt hash checks;
- protected-output leak tests;
- policy and review-interface tests;
- correction and rollback drills;
- remote branch, diff, and pull-request read-back.

[Back to top](#top)

---

## 13. Correction, supersession, and rollback

### Documentation rollback

Revert the scoped README and generated-work receipt commit through a transparent Git revert or equivalent reviewed reversal. Do not rewrite shared history.

### Future ingest correction

A mature implementation must support:

- source descriptor correction or deactivation;
- rights, attribution, sensitivity, review, consent, revocation, or embargo changes;
- payload corruption or digest mismatch discovered after admission;
- source-vintage or provenance correction;
- candidate-state correction;
- policy-version changes;
- ingest receipt correction without erasing the original record;
- downstream invalidation and reprocessing;
- release withdrawal and rollback by downstream release authority.

### Required correction behavior

1. preserve the original intake and decision record;
2. create a correction or supersession relationship;
3. identify affected RAW captures, WORK candidates, processed objects, evidence/proof objects, catalog projections, releases, caches, and public derivatives;
4. fail closed while required review or reprocessing is incomplete;
5. avoid republishing a corrected result until all downstream gates close;
6. record the rollback target and validation used to restore safety.

A Git revert alone cannot recall protected information already published. That is why ingest must never become a public path.

[Back to top](#top)

---

## 14. Definition of done

### README v0.2

This documentation revision is complete when:

- the target is updated in place with stable document identity;
- current repository maturity is separated from proposed implementation;
- checked absences are bounded rather than overclaimed;
- placeholder spec and source-control files are identified accurately;
- connector, registry, contract, schema, policy, evidence, lifecycle, test, validator, release, and public-serving authorities remain separate;
- candidate-not-site and exact-location denial are explicit;
- cultural, sovereignty, rights-holder, consent, revocation, and embargo obligations fail closed;
- future input, result, receipt, test, correction, and rollback obligations are reviewable;
- no protected content, source payload, executable, spec, policy, schema, fixture, test, workflow, or release state is changed;
- branch, diff, content hash, pull request, and generated receipt are remotely verified.

### Future executable ingest

Executable ingest is not done until:

- ownership and placement are accepted;
- spec, parser, consumer, contracts, schemas, source controls, policy interfaces, and reason codes are versioned;
- at least one synthetic admissible and multiple negative fixtures exist;
- tests collect and run deterministically with no network;
- RAW and QUARANTINE adapters are isolated and immutable;
- receipts are schema-valid and replayable;
- protected-output leak tests pass;
- workflow holds are replaced by substantive reviewed checks;
- correction, revocation, supersession, and rollback drills pass;
- no public or release path bypasses governed downstream gates.

[Back to top](#top)

---

## 15. Open verification register

| ID | Question | Status | Evidence needed |
|---|---|---|---|
| `ARCH-INGEST-001` | Does any differently named ingest implementation exist outside the checked paths? | `UNKNOWN` | Recursive tree and code search at a pinned commit. |
| `ARCH-INGEST-002` | Which root and object family own `SourceIntakeRecord` and the pre-RAW admission event? | `CONFLICTED / NEEDS VERIFICATION` | Accepted ADR, contract, schema, and registry binding. |
| `ARCH-INGEST-003` | Does connector code stage payloads, make admission decisions, or both? | `NEEDS VERIFICATION` | Connector contracts, tests, and runtime traces. |
| `ARCH-INGEST-004` | Which source-role vocabulary is authoritative for Archaeology ingest? | `NEEDS VERIFICATION` | Accepted source contract, registry records, policy, and validator tests. |
| `ARCH-INGEST-005` | Which contract owns raw-capture, quarantine, and ingest receipt semantics? | `NEEDS VERIFICATION` | Contract/schema decision and generated valid/invalid fixtures. |
| `ARCH-INGEST-006` | What is the accepted local finite-result vocabulary? | `NEEDS VERIFICATION` | Schema enum, policy mapping, tests, and consumer behavior. |
| `ARCH-INGEST-007` | Which role approves source activation, cultural use, raw admission, and later release? | `NEEDS VERIFICATION` | Separation-of-duties matrix, CODEOWNERS, review records, and policy. |
| `ARCH-INGEST-008` | How are CARE, sovereignty, consent, revocation, embargo, and authority-to-control represented? | `NEEDS VERIFICATION` | Accepted contracts, policy, review interfaces, and restricted fixtures. |
| `ARCH-INGEST-009` | Which CI job will own executable no-network ingest tests? | `UNKNOWN` | Accepted command, nonempty collection, workflow change, and required-check policy. |
| `ARCH-INGEST-010` | How do source corrections cascade through evidence, catalog, release, caches, and rollback? | `NEEDS VERIFICATION` | Correction drill, dependency graph, receipts, and rollback evidence. |
| `ARCH-INGEST-011` | Is this sublane canonical, an adapter over shared ingest mechanics, or documentation-only? | `CONFLICTED / ADR` | Responsibility decision and migration plan. |
| `ARCH-INGEST-012` | What monitoring and retained receipt evidence prove production behavior? | `UNKNOWN` | Runtime logs, metrics, retained receipts, dashboards, and incident records. |

[Back to top](#top)

---

## 16. Evidence ledger

| Evidence | Status | Supports | Does not prove |
|---|---|---|---|
| Target README at `main@860ccaec...` | `CONFIRMED` | Existing path, v0.1 content, prior blob, documented boundary. | Executable ingest behavior. |
| [`pipelines/domains/archaeology/README.md`](../README.md) | `CONFIRMED` | Parent execution responsibility and sensitive-domain posture. | Child implementation maturity. |
| [`pipeline_specs/archaeology/README.md`](../../../../pipeline_specs/archaeology/README.md) | `CONFIRMED` | Five-stage placeholder inventory and declarative-versus-executable boundary. | Accepted spec schema, parser, or source activation. |
| [`ingest.spec.yaml`](../../../../pipeline_specs/archaeology/ingest.spec.yaml) | `CONFIRMED PLACEHOLDER` | Seven-line planning artifact. | Runnable or accepted specification. |
| [`data/registry/sources/archaeology/README.md`](../../../../data/registry/sources/archaeology/README.md) | `CONFIRMED` | Source-control responsibility, T4/fail-closed documentation posture. | Concrete valid SourceDescriptors or runtime consumers. |
| [`sources.yaml`](../../../../data/registry/sources/archaeology/sources.yaml) and [`source_roles.yaml`](../../../../data/registry/sources/archaeology/source_roles.yaml) | `CONFIRMED PLACEHOLDERS` | Eight-line planning files. | Active sources or accepted roles. |
| [`tests/domains/archaeology/README.md`](../../../../tests/domains/archaeology/README.md) | `CONFIRMED` | Thirteen named modules and sampled placeholder-heavy maturity. | Current executable case count or pass rate. |
| [`tools/validators/archaeology/README.md`](../../../../tools/validators/archaeology/README.md) | `CONFIRMED` | README-only broad validator lane and maturity limits. | Validator execution or emitted ValidationReports. |
| [`domain-archaeology.yml`](../../../../.github/workflows/domain-archaeology.yml) | `CONFIRMED` | Read-only structural readiness holds and no publication behavior. | Source admission, evidence, policy, proof, or release success. |
| [`Directory Rules`](../../../../docs/doctrine/directory-rules.md) | `CONFIRMED doctrine` | Responsibility-root placement and lifecycle separation. | Whether a future file should exist. |
| [`ADR-0010`](../../../../docs/adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md) | `PROPOSED / CONFLICTED` | Documented fail-closed design pressure and exact-location risks. | Accepted ADR status or executable enforcement. |
| Exact 404 probes at pinned base | `CONFIRMED BOUNDED ABSENCE` | Checked expected files were absent at named paths. | Permanent or exhaustive absence. |
| Uploaded documentation implementation prompt v3.1 | `CONFIRMED instruction source` | Implementation method, evidence, validation, PR, and rollback expectations. | Repository implementation facts. |

[Back to top](#top)

---

## 17. Change history

### v0.2 — 2026-07-19

- replaced design-forward executable-tree claims with commit-pinned repository maturity;
- corrected the declarative companion from `ingest.yaml` to the repository-present `ingest.spec.yaml`;
- identified the ingest spec and inspected source-control files as placeholders;
- recorded bounded checked absences without claiming exhaustive directory emptiness;
- aligned status with placeholder-heavy tests, README-only validators, and workflow readiness holds;
- strengthened connector-versus-ingest, candidate-not-site, source-role, rights, cultural, sovereignty, sensitivity, receipt, correction, and rollback boundaries;
- replaced the pseudo-machine receipt example with obligations that defer to accepted contracts and schemas;
- added file-admission criteria, a smallest-sound implementation sequence, an evidence ledger, and an open verification register.

### v0.1 — 2026-06-13

- established the initial Archaeology ingest documentation boundary and lifecycle guardrails.

---

## Maintainer note

Start with ownership, contracts, schemas, source controls, synthetic no-network fixtures, and negative tests. Do not add live source fetching, source activation, exact coordinates, protected cultural content, bulk admission, public layers, generated Archaeology summaries, or release wiring until the trust boundary is executable, independently reviewed, receipt-backed, correction-aware, and rollback-tested.
