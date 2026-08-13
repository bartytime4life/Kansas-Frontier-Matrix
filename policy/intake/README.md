<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://policy/intake
title: Intake Admissibility Policy Boundary and Pre-RAW Routing Contract
type: policy-readme
version: v0.2
status: draft; repository-grounded; boundary-compact; documentation-only; pre-raw-intake-routing; source-admission-aware; docs-intake-separated; fixture-first-companions; evaluator-unbound; fail-closed; non-release; non-publication
owner: NEEDS VERIFICATION — CODEOWNERS routes /policy/ to @bartytime4life; accepted intake stewardship, specialist review, and independent approval controls were not established
created: 2026-07-24
updated: 2026-08-13
policy_label: repository-facing; intake; source-admission; pre-raw; candidate-material; local-upload; quarantine-routing; source-role; rights; sensitivity; integrity; fail-closed; no-secrets; no-public-path
current_path: policy/intake/README.md
owning_root: policy/
responsibility: Define the documentation-only pre-RAW intake admissibility boundary, explicit separation from watcher intake, promotion, release, and docs/intake, and the evidence required before executable policy may be accepted without executing intake, mutating lifecycle state, approving release, or publishing data.
canonical_relationship: BOUNDARY_COMPACT documentation for a proposed pre-RAW admissibility lane beneath canonical policy/; it does not replace policy/source/, source contracts and registries, connectors, docs/intake idea canonicalization, quarantine-exit governance, promotion, release, or publication
evidence_repository: bartytime4life/Kansas-Frontier-Matrix
base_ref: main
base_commit: ad31275429d715ad92002f8f2e160299193c9f50
target_prior_blob: b5682be75bf480806dde2cfb3bbe2879fe52e454
directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
directory_rules_adr_blob: b01322ef64f8c2b1ecb41de7ef4685b97cfa2a62
policy_root_blob: 6c5021f9d92778581a4e9331a9dd6ddb7efc5e35
source_policy_readme_blob: e2c351c6b354a0c088cfd0205183a46aa53d13e4
promotion_policy_readme_blob: 79287df1d828010d716ed43d2e24d6dbd610305b
rights_policy_readme_blob: d51eb23c26e30df48263be00360729f167d30c84
sensitivity_policy_readme_blob: 06197c7a7255264b94fb9dd8d7f73844cfa35682
source_activation_contract_blob: 3a42d5b38ec7e83623f1de58a34e0b36ee582f81
source_activation_schema_blob: 017f9e14ba24a0ddb425ca2cfb018ec847812b7d
source_activation_validator_blob: 6e2bfceae3b58872d3f905f4d24003b80b7de422
source_activation_test_blob: 5f01edfedf67f37f25e06f4b1ee691638be0363b
source_activation_workflow_blob: 76f308ee5076ad6999d457beb4780917070cbc09
source_intake_record_contract_blob: f7842c43f0419aae6a84be30b952ed6686c9c3c8
source_intake_record_schema_blob: 5facaf967395cb0cd903395daa97c6b2a78ebb46
source_intake_record_validator_blob: 0b3378859a86e6e3b6999f0cd9550157917e1384
source_intake_record_test_blob: 7c98b45113cd711aacfe052b9a0bae84d678f0ca
source_intake_record_workflow_blob: b3ec6f33a071dfcb6e3f908a0f7729e5dece57a9
source_descriptor_contract_blob: b57ae5ccc042c1423b75c168438800384c9b6713
ingest_receipt_contract_blob: 8e76dc10aa23de967501bd32479f83788339a39b
policy_input_contract_blob: 545c352681dd0db0cd4d169a5d2f9c364356457c
policy_input_profile_blob: 3af1c2c8d525f60f6e2aac89c5a0455898d77768
policy_decision_contract_blob: ebfe97f98263e6309db6d2772cb2c5e548819650
policy_decision_schema_blob: 1472d26a42c73f17545b4464a275412ffa1d098e
source_admission_adr_blob: 58693830fcdf9746c5494fdd85298529fa5594a9
quarantine_exit_adr_blob: bcd98911a420a5cf00fd3571a8fe18e15e2efe70
source_registry_readme_blob: 2821e9681273bff6b430920d0a45312c5643ba33
open_overlapping_pull_requests_found: "0"
related:
  - ../README.md
  - ../source/README.md
  - ../promotion/README.md
  - ../rights/README.md
  - ../sensitivity/README.md
  - ../access/README.md
  - ../consent/README.md
  - ../bundles/README.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0017-source-descriptor-admission-process.md
  - ../../docs/adr/ADR-0021-quarantine-has-structured-exit-paths.md
  - ../../docs/sources/ADMISSION_PROCESS.md
  - ../../docs/intake/canonicalization-policy.md
  - ../../docs/runbooks/QUARANTINE_HANDLING.md
  - ../../contracts/source/source_descriptor.md
  - ../../contracts/source/source_activation_decision.md
  - ../../contracts/source/source_intake_record.md
  - ../../contracts/source/ingest_receipt.md
  - ../../contracts/policy/policy_input_bundle.md
  - ../../contracts/policy/policy_input_bundle_profile_v1.md
  - ../../contracts/policy/policy_decision.md
  - ../../schemas/contracts/v1/source/source_activation_decision.schema.json
  - ../../schemas/contracts/v1/source/source_intake_record.schema.json
  - ../../schemas/contracts/v1/policy/policy_input_bundle.schema.json
  - ../../schemas/contracts/v1/policy/policy_decision.schema.json
  - ../../fixtures/contracts/v1/source/source_activation_decision/README.md
  - ../../fixtures/contracts/v1/source/source_intake_record/README.md
  - ../../tools/validators/validate_source_activation_decision.py
  - ../../tools/validators/validate_source_intake_record.py
  - ../../data/registry/sources/README.md
  - ../../connectors/README.md
  - ../../pipelines/ingest/README.md
  - ../../packages/source-registry/README.md
  - ../../tools/validators/connector_gate/README.md
  - ../../apps/governed-api/README.md
  - ../../release/README.md
tags: [kfm, policy, intake, source-admission, pre-raw, source-descriptor, source-intake-record, source-activation-decision, ingest-receipt, connector, local-upload, quarantine, rights, sensitivity, source-role, integrity, fail-closed]
truth_posture: CONFIRMED adopted singular policy root, documentation-only intake lane, proposed fixture-first SourceActivationDecision and SourceIntakeRecord families with deterministic validators and read-only workflows, separate docs/intake canonicalization lane, proposed source-admission and quarantine ADRs, closed PolicyDecision family enum without intake/source, and no local intake rule module / PROPOSED pre-RAW policy boundary, activation route composition, reason and obligation vocabularies, future explicit intake input profile, native policy tests, consumer enforcement, correction, and rollback / UNKNOWN accepted intake policy family or bundle, active evaluator, authenticated decision authority, connector enforcement coverage, registry activation, quarantine-case implementation, operational audit sink, required-check coupling, deployed consumer, and production operation
notes:
  - "This revision updates documentation only. It creates or changes no policy rule, contract, schema, fixture, validator, workflow, registry record, lifecycle object, receipt, release object, or publication state."
  - "SourceActivationDecision and SourceIntakeRecord are distinct proposed object families: the former records a pre-RAW activation route; the latter records watcher/source-health observations limited to WORK or QUARANTINE candidates."
  - "The current PolicyDecision schema permits promotion, access, render, capability, consent, and sensitivity only; policy_family=intake and policy_family=source remain schema-invalid at the inspected snapshot."
  - "Secrets, credentials, private endpoints, bearer tokens, malware samples, protected identifiers, and raw sensitive payloads must never be placed in this repository-facing README or public fixtures."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Intake Admissibility Policy Boundary

> **One-line purpose.** `policy/intake/` documents the fail-closed policy boundary that decides whether externally supplied material has enough explicit source, rights, sensitivity, integrity, role, review, and routing context to enter KFM's governed lifecycle at the pre-RAW edge—without becoming a connector, source registry, idea-intake process, quarantine-exit authority, promotion gate, release authority, or publication path.

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#status-and-evidence)
[![Scope: pre-RAW intake](https://img.shields.io/badge/scope-pre--RAW%20intake-0969da?style=flat-square)](#purpose)
[![Directory Rules: adopted](https://img.shields.io/badge/Directory%20Rules-v2%20adopted-2da44e?style=flat-square)](#authority-level)
[![Local lane: documentation only](https://img.shields.io/badge/local%20lane-documentation%20only-6e7781?style=flat-square)](#current-direct-child-map)
[![Default: fail closed](https://img.shields.io/badge/default-fail%20closed-b42318?style=flat-square)](#default-posture)
[![Activation profile: fixture first](https://img.shields.io/badge/activation%20profile-fixture%20first-8250df?style=flat-square)](#source-registry-and-activation-boundary)
[![Publisher: no](https://img.shields.io/badge/publisher-no-6e7781?style=flat-square)](#authority-level)

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status-and-evidence) · [Child map](#current-direct-child-map) · [Scope](#scope-and-bounded-context) · [Separation](#intake-concept-separation) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#explicit-policy-input-profile) · [Evaluation](#evaluation-order) · [Decisions](#decision-contract-compatibility) · [Routing](#proposed-intake-routing-states) · [Outcomes](#normalized-policy-outcomes) · [Reasons](#reason-code-vocabulary) · [Obligations](#obligation-vocabulary) · [Registry](#source-registry-and-activation-boundary) · [Receipts](#receipt-and-audit-boundary) · [Quarantine](#quarantine-boundary) · [Threats](#threat-model) · [Validation](#validation-and-acceptance) · [Review](#review-burden) · [Rollback](#correction-re-admission-revocation-and-rollback) · [Open work](#open-verification-register)

> [!IMPORTANT]
> **Safe current conclusion:** `policy/intake/` contains this README and an empty `.gitkeep`; it contains no executable intake rule, native policy test, bundle, or evaluator. The wider repository now has proposed, fixture-first `SourceActivationDecision` and `SourceIntakeRecord` contract/schema/fixture/validator slices with read-only workflows. Those slices make bounded shapes and consistency rules testable; they do **not** accept ADR-0017, activate a source, admit bytes, run an intake policy bundle, create authenticated review, promote, release, deploy, or publish.

> [!CAUTION]
> **Do not collapse the two intake records.** Proposed `SourceActivationDecision` records an operation-specific pre-RAW route such as `ADMIT_TO_RAW`, `QUARANTINE`, `DENY_INTAKE`, `HOLD`, or `ERROR`. Proposed `SourceIntakeRecord` records watcher/source-health observations limited to `WORK` or `QUARANTINE` candidates and always requires later promotion. Neither object is active policy or publication authority.

> [!WARNING]
> **Admission is not promotion, and this lane is not `docs/intake/`.** Source/material intake concerns operation-specific admissibility at the lifecycle edge. Documentation intake handles ideas, drafts, packets, and canonicalization proposals. Promotion and release remain later governed transitions; no file move, green check, polished document, or generated summary substitutes for them.

---

## Purpose

`policy/intake/` exists to answer one bounded policy-routing question:

> Given an explicit intake attempt, candidate source or material, source identity and role posture, rights, sensitivity, access, integrity, content classification, domain scope, review state, prior decisions, evaluator context, and requested lifecycle destination, may the material enter KFM—and with which mandatory routing and handling obligations?

A future accepted intake policy may evaluate:

- external publisher feeds;
- API or bulk-download captures;
- watcher or scheduled-source observations;
- manual steward curation;
- browser, CLI, or operator file uploads;
- correction or re-admission attempts for changed sources;
- source refreshes whose rights, role, cadence, or sensitivity posture may have changed;
- restricted or partial captures that may require quarantine;
- candidate source descriptors proposed by connectors or humans;
- intake attempts that must be denied without storing the supplied payload.

This lane should produce policy-relevant guidance for a governed intake orchestrator. It must not directly fetch, parse, scan, transform, register, promote, release, render, or publish material.

[Back to top](#top)

---

## Authority level

This README is a **`BOUNDARY_COMPACT` repository-facing draft**, not active policy. It inherits from [`policy/`](../README.md), which accepted [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) and the [Directory Rules v2](../../docs/doctrine/directory-rules.md) place normative allow, deny, hold, restrict, and abstain rule source under singular `policy/`. The machine [root registry](../../control_plane/root_registry.yaml) projects the same root; it does not create authority.

[CODEOWNERS](../../.github/CODEOWNERS) routes `/policy/` changes to `@bartytime4life`. That route is not an accepted intake-steward assignment, authenticated review, independent approval, policy decision, release approval, or publication authority.

| Concern | Owning surface | Role of `policy/intake/` |
|---|---|---|
| Intake admissibility rules | `policy/` after accepted rule, bundle, evaluator, and review | Document the local boundary; no executable rule exists here now |
| Source meaning and admissibility fields | [`contracts/source/source_descriptor.md`](../../contracts/source/source_descriptor.md) | Consume; never redefine |
| Pre-RAW activation decision meaning | [`contracts/source/source_activation_decision.md`](../../contracts/source/source_activation_decision.md) | Reference the proposed profile; never emit, authenticate, or persist a decision here |
| Watcher/source-health intake meaning | [`contracts/source/source_intake_record.md`](../../contracts/source/source_intake_record.md) | Keep distinct from pre-RAW activation and downstream promotion |
| Ingest receipt meaning | [`contracts/source/ingest_receipt.md`](../../contracts/source/ingest_receipt.md) | Consume or require; never emit/store here |
| Machine shape | `schemas/contracts/v1/` | Require accepted shapes; never define them here |
| Source registry instances and authority posture | [`data/registry/sources/`](../../data/registry/sources/README.md) | Resolve; never silently activate or mutate |
| Source-admission architecture | proposed ADR-0017 and source-admission standards | Follow as proposed design evidence; never accept the ADR by documentation |
| Connector and watcher execution | `connectors/` | Constrain through policy; never implement fetching here |
| Ingest implementation | `pipelines/ingest/`, connector-local code, accepted runtime roots | Constrain; never become pipeline code |
| Security/content scanning | accepted tools/services and validators | Consume bounded results; never store samples or secrets |
| Quarantine records and handling | `data/quarantine/`, runbooks, accepted contracts/schemas | Route into; never invent an exit or publish from quarantine |
| Policy evaluation mechanics | `packages/policy-runtime/` or accepted evaluator | Supply accepted rules; never become runtime helpers |
| Validation | `tools/validators/`, `tests/`, `fixtures/`, read-only workflows | Describe bounded checks; a passing fixture profile is not active policy |
| Promotion | `policy/promotion/`, promotion contracts, lifecycle gates | Remain separate; admission does not promote |
| Release, correction, withdrawal, rollback | `release/` and governed runbooks | Remain separate; intake cannot publish or withdraw alone |
| Public API/UI/AI behavior | governed applications using released outputs | No direct public path |

A schema-valid or validator-passing candidate means only that its bounded shape and local invariants passed. It does not establish source truth, policy evaluation, authenticated review, lifecycle mutation, evidence closure, catalog authority, public safety, or release approval.

[Back to top](#top)

---

## Status and evidence

### Current repository state

| Surface | Status at `main@ad31275429d7` | Safe conclusion |
|---|---:|---|
| `policy/intake/` | **CONFIRMED documentation-only** | Contains this README and an empty `.gitkeep`; no Rego module, native policy test, manifest, or evaluator is local to this lane. |
| `policy/` root | **CONFIRMED adopted placement / mixed maturity** | ADR-0029 and Directory Rules v2 establish singular policy-source placement; bounded policy profiles elsewhere do not create a general intake evaluator. |
| Adjacent `source/`, `rights/`, `sensitivity/`, and `promotion/` lanes | **CONFIRMED independently documented / mixed maturity** | Each owns a separate policy concern. Their files and checks must not be collapsed into one intake decision or treated as proof of operational composition. |
| ADR-0017 | **CONFIRMED `proposed`** | Source-admission architecture is documented but not accepted or operationally graduated. |
| ADR-0021 | **CONFIRMED `proposed`** | The five-exit quarantine grammar remains proposed; the current runbook and lifecycle controls remain separate evidence. |
| `SourceDescriptor` | **CONFIRMED proposed semantic contract and bounded validation** | Rich meaning and fixture coverage exist; singular/plural schema authority remains conflicted and descriptor validity does not activate a source. |
| `SourceActivationDecision` | **CONFIRMED proposed, fixture-first profile** | Contract, canonical underscore schema, synthetic fixtures, deterministic validator, focused tests, and read-only workflow exist. They do not run policy, authenticate references, activate a source, or write lifecycle state. |
| `SourceIntakeRecord` | **CONFIRMED proposed, inactive watcher envelope** | Contract, canonical underscore schema, compatibility pointer, synthetic fixtures, deterministic validator, focused tests, and read-only workflow exist. The object is limited to `WORK`/`QUARANTINE` candidate observation and is not pre-RAW activation. |
| `IngestReceipt` | **CONFIRMED proposed semantic contract and schema-paired surface** | Records capture facts and digests; it is not admission, policy, evidence truth, promotion, or release. |
| Source registry | **CONFIRMED documentation and candidate implementation surfaces** | Source identity and treatment posture remain separate from policy evaluation and activation authority. Operational population and consumer enforcement are not proved here. |
| `PolicyInputBundle` | **CONFIRMED permissive parent plus explicit inactive profile v1** | Profile v1 models `ANSWER`, `RENDER`, `EXPORT`, `PROMOTE`, and `RELEASE`; it explicitly does not model intake or source activation. |
| `PolicyDecision` | **CONFIRMED proposed closed schema** | Outcomes are `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR`; families exclude `intake`, `source`, and `admission`. |
| Intake rule/bundle/evaluator/consumer | **UNKNOWN / NOT ESTABLISHED** | No accepted local rule source, input profile, active bundle, general evaluator, authenticated decision flow, governed consumer, or production operation was proved. |
| Required-check and independent-review enforcement | **UNKNOWN / NEEDS VERIFICATION** | Workflow presence and CODEOWNERS routing are not ruleset or separation-of-duties evidence. |

### Truth labels used here

| Label | Meaning |
|---|---|
| **CONFIRMED** | Verified from the pinned tree, exact tracked bytes, accepted ADR, deterministic tests, validator, or workflow definition. |
| **PROPOSED** | A candidate contract, rule, route, vocabulary, integration, or behavior not accepted as current operation. |
| **NEEDS VERIFICATION** | A bounded check, assignment, migration, or decision remains before reliance. |
| **UNKNOWN** | The inspected repository evidence cannot support a stronger statement. |

### Evidence boundary

This README may state current repository facts and bounded doctrine. It must not claim:

- any named source is admitted, active, current, reachable, or licensed;
- any connector is safely enabled;
- any upload route is deployed;
- any malware or content-scanning service is configured;
- any source authority register is populated;
- any `SourceActivationDecision` is authenticated, emitted by an accepted evaluator, or enforced by a connector;
- any `SourceIntakeRecord` is emitted from a deployed watcher or accepted as lifecycle authority;
- referenced policy, descriptor, review, receipt, or registry objects are resolved or authentic;
- intake decisions are operationally cached, replayed, expired, revoked, or receipt-backed;
- native intake policy tests run in CI;
- quarantine exits are operational;
- a release or publication occurred.

Those claims remain `UNKNOWN` or `NEEDS VERIFICATION` until current implementation, test, workflow, artifact, and runtime evidence proves them.

[Back to top](#top)

---

## Current direct-child map

Directory Rules `DIR-README-003` requires this README to show only the directory it governs and its direct children. The map is verified from the complete tracked directory at the pinned base.

```text
policy/intake/
├── .gitkeep   # Empty placeholder; no rule, bundle, test, or authority
└── README.md  # This BOUNDARY_COMPACT policy-lane contract
```

Neither file is marked generated, mirrored, localized, or converted. A future child rule, bundle relationship, or generated output must identify its writable authority, package/entrypoint, accepted input profile, evaluator, tests, consumer, and rollback before this README treats it as implemented.

[Back to top](#top)

---

## Scope and bounded context

### In scope

- policy-relevant classification of an intake attempt;
- operation-specific admission prerequisites;
- source identity and descriptor resolution requirements;
- source-role anti-collapse;
- rights, terms, attribution, access, redistribution, and embargo checks;
- sensitivity and harmful-precision checks;
- candidate-source defaults for user uploads and uncertain material;
- content-type, format, integrity, and safe-scan result requirements;
- domain-scope and steward-routing requirements;
- freshness, cadence, supersession, and re-admission triggers;
- finite policy outcomes, reason codes, and obligations;
- routing to RAW, QUARANTINE, terminal denial, or an explicit error/hold;
- audit, data minimization, correction, re-admission, revocation, and rollback expectations;
- child-lane admission rules after placement is accepted.

### Out of scope

- discovering sources;
- fetching bytes;
- connector scheduling or retry logic;
- parsing, normalizing, or transforming payloads;
- storing credentials, tokens, or private endpoints;
- antivirus or content-scanner implementation;
- source registry record storage;
- SourceDescriptor contract or schema definition;
- idea, document, or architecture-packet canonicalization;
- quarantine exit approval;
- downstream promotion;
- catalog or triplet closure;
- release approval;
- public API, map, export, search, graph, vector, screenshot, or AI output;
- generated inference that upgrades source authority.

[Back to top](#top)

---

## Intake concept separation

The word **intake** appears in several distinct KFM responsibilities. They must not collapse.

| Concept | Primary question | Correct home | This lane's relationship |
|---|---|---|---|
| Source/material intake policy | May this external material enter the lifecycle under explicit conditions? | `policy/intake/` under the adopted policy root | Primary documented scope; no local rule exists yet |
| Source admission architecture | What records, stages, and authority boundaries govern admission? | ADR-0017 and `docs/sources/` | Follow |
| Source identity and treatment | What is the source, and how may KFM treat it? | `SourceDescriptor` + source registry | Resolve and evaluate |
| Pre-RAW activation decision | What operation-specific route follows descriptor, policy, and review context? | proposed `SourceActivationDecision` contract family | Reference; do not emit or authenticate here |
| Watcher/source-health intake record | What bounded source observation should enter WORK or QUARANTINE review? | proposed `SourceIntakeRecord` contract family | Keep distinct from activation and promotion |
| Connector intake | How are bytes observed or captured? | `connectors/` | Constrain, not implement |
| Ingest execution | What happened during capture? | ingest pipelines + `IngestReceipt` | Require/reference |
| Idea/document intake | How do notes or proposals become canonical repo artifacts? | `docs/intake/` | Explicitly separate |
| Quarantine entry | Why is material held, and what review is required? | intake/validation policy + quarantine record | May route into |
| Quarantine exit | How does held material leave quarantine? | ADR-0021, runbooks, promotion/release controls | Must not decide |
| Promotion | May admitted material advance through lifecycle stages? | promotion gates and `policy/promotion/` | Explicitly separate |
| Release | May a reviewed derivative become public? | `release/` | No authority |
| Public serving | May a released artifact be rendered or answered? | governed API/runtime + render/access/sensitivity policy | No direct path |

### Non-collapse rules

1. A discovered URL is not an admitted source.
2. A downloaded file is not an admitted source.
3. A user upload is not an authoritative source.
4. A valid `SourceDescriptor` is not an activation decision.
5. A valid `SourceActivationDecision` fixture is not an authenticated or enforced decision.
6. A `SourceIntakeRecord` is not a `SourceActivationDecision` or promotion decision.
7. A successful `IngestReceipt` is not an admissibility decision.
8. An intake route is not a promotion decision or quarantine exit.
9. A passed validator, schema, scanner, or workflow is not evidence truth or rights clearance.
10. A source registry entry is not claim truth.
11. An idea promoted through `docs/intake/` is not automatically admissible source material.

[Back to top](#top)

---

## What belongs here

Good fits for `policy/intake/` after an accepted rule, bundle, and native-test convention exists include:

- reviewed declarative intake-admissibility rules;
- parent routing documentation for source/material intake policy;
- common fail-closed intake invariants;
- operation-specific input requirements;
- reason-code and obligation vocabularies aligned with contracts and schemas;
- rules that require a resolvable source descriptor or explicit candidate posture;
- rules that preserve source-role, rights, sensitivity, access, and cadence context;
- rules that route uncertainty to quarantine or denial;
- rules that prevent connectors, uploads, or manual curation from bypassing admission;
- rules that require digest-pinned capture and receipt linkage where applicable;
- synthetic, no-network native policy tests if the accepted policy convention colocates them;
- supersession and migration notes for intake rules.

A file belongs here because its primary responsibility is **pre-RAW admissibility**, not merely because it mentions uploading, importing, sources, data quality, security, quarantine, or pipelines.

[Back to top](#top)

---

## What does not belong here

| Do not put in `policy/intake/` | Correct responsibility |
|---|---|
| SourceDescriptor, SourceActivationDecision, SourceIntakeRecord, or IngestReceipt meaning | `contracts/source/` |
| Source, activation, intake-record, or policy JSON Schema | `schemas/contracts/v1/` |
| SourceDescriptor instances or source authority records | `data/registry/sources/` and accepted control-plane registers |
| Raw, uploaded, downloaded, or quarantined payloads | governed `data/` lifecycle lanes |
| Connector, watcher, crawler, importer, upload, or fetch code | `connectors/`, `packages/`, `apps/`, or pipelines by responsibility |
| Parser, normalizer, transformer, or content conversion code | `packages/` and `pipelines/` |
| Antivirus binaries, signatures, malware samples, exploit samples | approved secure tooling and test systems; never public policy docs |
| Credentials, API keys, bearer tokens, private endpoints, session data | secret management and approved runtime configuration |
| Ingest receipts, run receipts, quarantine records, review records | accepted receipt, data, review, or governance roots |
| PolicyDecision instances | accepted emitted-decision or receipt lanes |
| SourceActivationDecision or SourceIntakeRecord instances | accepted process, lifecycle, registry, or receipt home after a separate placement decision; never beside rule source by type name alone |
| Idea intake registers and canonicalization workflow | `docs/intake/` |
| Quarantine exit records | quarantine/release/correction governance roots |
| Promotion decisions | promotion governance and receipt roots |
| Release manifests, corrections, withdrawals, rollback cards | `release/` |
| Public routes, UI logic, tiles, exports, AI answers | governed application/runtime roots |
| Generated prose treated as source authority | denied; require admissible evidence and source posture |
| A second independently evolving source-policy authority | resolve through ADR/migration rather than parallel rule homes |

[Back to top](#top)

---

## Default posture

| Condition | Default route or policy outcome |
|---|---|
| Intake class unknown or unsupported | `ABSTAIN` or `ERROR`; do not store as admitted RAW |
| Source identity missing or unresolved | QUARANTINE or `DENY`, according to accepted contract |
| SourceDescriptor absent | Candidate-only hold or QUARANTINE; never active admission |
| Rights unknown, denied, or unverifiable | QUARANTINE or `DENY` |
| Sensitivity unknown or potentially high-risk | QUARANTINE; public use denied |
| Source role missing, contradictory, or overclaimed | QUARANTINE or `DENY` |
| Candidate local upload | Candidate role; public release denied by default |
| Required integrity digest missing | QUARANTINE or `ERROR` |
| Digest mismatch | `ERROR` and quarantine/invalid-capture handling |
| Content-type or format unsupported | QUARANTINE, safe rejection, or `DENY` |
| Security/content scan unavailable where required | `ERROR` or QUARANTINE; never implicit allow |
| Credential or secret detected | QUARANTINE/deny secure handling; minimize logs |
| Required review incomplete | QUARANTINE or `ABSTAIN` |
| Evaluator or bundle unavailable | `ERROR`; no admission |
| All accepted admission gates pass | Eligible for governed routing to RAW with obligations; not promotion or release |
| Caller cannot enforce an obligation | `DENY` or `ERROR` |

Unknown context never becomes permission.

[Back to top](#top)

---

## Explicit policy input profile

A mature intake evaluation should receive an explicit, versioned, immutable input profile. The current repository has two relevant but non-equivalent surfaces:

| Surface | Current boundary |
|---|---|
| Parent [`PolicyInputBundle`](../../contracts/policy/policy_input_bundle.md) | Its schema requires only `id`, permits additional properties, and does not make intake context explicit. |
| [`PolicyInputBundle` profile v1](../../contracts/policy/policy_input_bundle_profile_v1.md) | Proposed inactive explicit-context profile for `ANSWER`, `RENDER`, `EXPORT`, `PROMOTE`, and `RELEASE`; it expressly does not model intake or source activation. |
| [`SourceActivationDecision.context`](../../contracts/source/source_activation_decision.md#decision-context) | Proposed decision-record context for descriptor, rights, sensitivity, access, review, and registry posture; it is not a policy input bundle or evaluator. |

No accepted intake-specific input profile is established. The fields below are **PROPOSED graduation requirements**, not current machine-enforced facts.

### Bundle identity

- immutable input-bundle id;
- version and optional canonical content hash;
- evaluation time;
- policy bundle id, version, digest, and entrypoint;
- evaluator name/version and fail-closed mode;
- prior decision references and supersession state.

### Intake operation

- requested operation such as `discover`, `observe`, `upload`, `fetch`, `refresh`, `re_admit`, or `correct`;
- intake class such as publisher source, local upload, steward curation, scheduled watcher, or correction intake;
- requested route: RAW candidate, quarantine review, or denial-only evaluation;
- caller, service, connector, or steward reference;
- purpose and affected domain lanes.

### Source candidate context

- candidate source id or descriptor reference;
- descriptor version and review state;
- publisher and steward references;
- source type and source role;
- authority rank and admissibility limits;
- domain scope;
- current registry state and supersession links;
- connector activation posture where present.

### Rights and access context

- rights status;
- license or terms reference;
- attribution requirement;
- redistribution and commercial-use posture;
- embargo or access restrictions;
- authentication/access posture represented without credentials;
- verification time, verifier reference, and expiry.

### Sensitivity context

- default sensitivity classification;
- living-person, DNA/genomic, rare-species, archaeology/cultural, infrastructure, precise-location, private-land, or other protected-class flags;
- requested geometry or temporal precision;
- redaction/generalization status;
- required specialist review;
- public-release class.

### Capture and integrity context

- event/run reference;
- content type and declared format;
- safe file/payload metadata;
- byte count;
- digest algorithm and digest references;
- source-head observations such as safe ETag/version/checksum refs;
- transport or archive integrity status;
- content/security scan result reference where required;
- scanner profile/version reference without signatures, samples, or sensitive details;
- duplicate/collision detection result.

### Freshness and cadence context

- expected update cadence;
- observed retrieval time;
- upstream version/revision;
- staleness policy;
- stale, superseded, retired, or withdrawn flags;
- re-admission trigger reason.

### Review and lifecycle context

- required reviewers and current review state;
- rights/sensitivity/source/domain review references;
- current lifecycle posture;
- requested pre-RAW route;
- quarantine reason and steward route if applicable;
- correction, withdrawal, and rollback references;
- receipt/audit destination references.

### Input invariants

1. No hidden fetches from external systems, RAW stores, user sessions, operator memory, model prompts, or vector indexes.
2. Raw credentials and private tokens never enter the policy bundle.
3. Sensitive payload values are referenced or summarized safely, not embedded.
4. Missing fields are explicit, not guessed.
5. The source role is never upgraded by fluency, repetition, or parser success.
6. A prior decision does not authorize a new operation after expiry, source change, rights change, or sensitivity change.
7. Inputs are immutable for one evaluation; changed context creates a new bundle.
8. The evaluation target and intended route are explicit.
9. Policy-relevant scan results identify the checked profile and time.
10. Public-safe logging is designed before production activation.

[Back to top](#top)

---

## Evaluation order

A deterministic intake evaluation should proceed in this order:

1. **Validate the input envelope.** Reject malformed, unversioned, unhashable, or ambiguous input.
2. **Classify the intake operation.** Distinguish source/material intake from documentation/idea intake and downstream promotion.
3. **Resolve source candidate posture.** Locate the current descriptor or mark the candidate explicitly unresolved.
4. **Verify descriptor state.** Check identity, version, review, registry, supersession, and activation references.
5. **Check capture integrity.** Verify required digests, byte accounting, source-head observations, and duplicate posture.
6. **Check safe content classification.** Confirm format/content class and required scan result without exposing sensitive scan details.
7. **Evaluate rights and access.** Fail closed on unknown, denied, expired, or incompatible terms.
8. **Evaluate sensitivity.** Apply the most restrictive applicable class across source, payload, joins, geometry, time, and derivatives.
9. **Evaluate source role and admissibility.** Prevent candidate, contextual, fixture, aggregate, modeled, or restricted material from being upgraded.
10. **Evaluate domain scope.** Require affected-domain stewardship where the material crosses lanes.
11. **Evaluate freshness and cadence.** Detect stale descriptors, changed upstream state, or re-admission triggers.
12. **Evaluate review state.** Require human/steward review where policy cannot close the decision automatically.
13. **Compose independent policy results.** Preserve rights, sensitivity, access, consent, and other family decisions separately.
14. **Choose a pre-RAW route.** Use the proposed activation vocabulary—`ADMIT_TO_RAW`, `QUARANTINE`, `DENY_INTAKE`, `HOLD`, or `ERROR`—only through an accepted routing contract and evaluator.
15. **Attach enforceable obligations.** The caller must prove it can satisfy each obligation.
16. **Emit or link receipts and audit metadata.** Preserve input hash, policy version, reasons, obligations, route, and supersession.
17. **Return a normalized governed response.** Do not expose protected details or internal lifecycle stores.

A failure at any step cannot be repaired by silently skipping to a later step.

[Back to top](#top)

---

## Decision contract compatibility

### Current schema constraint

The current `PolicyDecision.policy_family` enum is:

```text
promotion | access | render | capability | consent | sensitivity
```

It does **not** include:

```text
intake | source | admission
```

Therefore:

- `policy_family=intake` is schema-invalid;
- `policy_family=source` is schema-invalid;
- this README does not create either family;
- an intake orchestrator must not mislabel admission as `promotion`;
- rights, sensitivity, access, consent, or capability checks should retain their own accepted family;
- an overall admission/activation result requires an accepted contract decision.

### Acceptable convergence options

The repository now has one concrete **proposed** convergence path, while the other options remain unimplemented:

| Option | Current status | Required boundary |
|---|---:|---|
| Composed existing families plus separate activation object | **CONFIRMED fixture-first candidate** | Proposed `SourceActivationDecision` references independent policy decisions and records a finite pre-RAW route. Its validator does not resolve or authenticate those references, run a policy bundle, or activate a source. |
| Versioned `intake` or `source` policy family | **NOT IMPLEMENTED** | Requires contract/schema versioning, fixtures, validators, normalization, consumers, receipts, compatibility, and rollback. |
| Reuse `promotion` for pre-RAW admission | **NOT ACCEPTED / DO NOT INFER** | Admission and promotion remain separate; reuse would require an explicit reviewed architecture and migration decision. |
| Transitional routing envelope | **NEEDS VERIFICATION** | Must remain visibly non-authoritative and must not masquerade as `PolicyDecision` or `SourceActivationDecision`. |

`SourceIntakeRecord` is not another convergence option for pre-RAW activation. Its proposed contract records watcher/source-health observations limited to `WORK` or `QUARANTINE` candidates and always leaves promotion required.

### Required migration burden for a new family

Adding a family requires synchronized changes to:

- semantic contract;
- JSON Schema enum and version;
- valid and invalid fixtures;
- validators;
- policy bundle manifest;
- native policy tests;
- runtime adapter;
- governed API and review console consumers;
- audit and receipt schemas;
- source-registry and connector integration;
- compatibility handling for old decisions;
- correction, revocation, cache invalidation, and rollback documentation.

[Back to top](#top)

---

## Proposed intake routing states

These are the closed route enum in the **proposed, fixture-first** `SourceActivationDecision` schema. They are canonical only within that inactive profile; no accepted policy evaluator, decision authority, connector, or lifecycle writer is bound to them.

| Route | Meaning | Allowed destination | Not equivalent to |
|---|---|---|---|
| `ADMIT_TO_RAW` | Required pre-RAW gates pass for the evaluated capture | governed RAW lane with descriptor/receipt obligations | evidence truth, promotion, or release |
| `QUARANTINE` | Material may be retained only in a governed restricted hold pending review/remediation | `data/quarantine/` with structured reason and review route | denial, publication, or promotion |
| `DENY_INTAKE` | Material must not be admitted for the evaluated operation | no admitted lifecycle entry; retain only minimum lawful/auditable metadata | source deletion policy or global ban |
| `HOLD` | Review or external decision is required before a route can be chosen | pending decision outside normal public paths | silent retry or implied allow |
| `ERROR` | Evaluator, integrity, schema, dependency, or process failure prevents a trustworthy route | safe failure path; normally no admitted RAW use | abstention due only to weak evidence |

### Route invariants

- `ADMIT_TO_RAW` requires approved descriptor posture, policy references, permitted rights, compatible activation state/scope, review evidence where required, and `require_ingest_receipt` for raw capture.
- `QUARANTINE` requires quarantined state, quarantine-only scope, `route_to_quarantine`, and `open_quarantine_case`.
- `DENY_INTAKE` cannot grant a usable activation scope and requires safe reason codes.
- `HOLD` requires pending review, review references, and a bounded `hold_expires_at` value.
- `ERROR` cannot grant a usable activation scope or create partial admitted state.
- No route can write directly to PROCESSED, CATALOG, TRIPLET, PUBLISHED, release manifests, or public APIs.
- A route is operation-specific and time-bounded.
- Re-evaluation creates a new decision rather than mutating the old one.

[Back to top](#top)

---

## Normalized policy outcomes

The proposed `PolicyDecision` schema uses this closed outward outcome vocabulary. It is not evidence of an accepted runtime evaluator:

| Outcome | Intake meaning |
|---|---|
| `ANSWER` | The evaluated family permits its portion of the intake operation, subject to obligations |
| `ABSTAIN` | Admissible context is insufficient or unresolved; normally route to hold/quarantine or deny |
| `DENY` | The evaluated family blocks the intake operation |
| `ERROR` | The input, evaluator, integrity, dependency, or process failed |

### Proposed composition rules

1. Any `DENY` blocks `ADMIT_TO_RAW`.
2. Any unresolved mandatory family result blocks `ADMIT_TO_RAW`.
3. Any `ERROR` fails closed.
4. The most restrictive applicable sensitivity/rights posture wins.
5. An `ANSWER` in one family never overrides `DENY` or `ERROR` in another.
6. Obligations accumulate unless they conflict.
7. Conflicting obligations require `ERROR`, `ABSTAIN`, or steward review.
8. The composed route must cite every contributing decision.
9. Public-safe explanation is separated from internal detail.
10. No decision family may upgrade source role or claim authority.

[Back to top](#top)

---

## Reason-code vocabulary

The following codes are the closed enum in the **proposed** `SourceActivationDecision` schema at the pinned base. They are not an accepted repository-wide reason registry or evidence that any decision was evaluated.

### Input and evaluation

- `INTAKE_ADMITTED`
- `INTAKE_INPUT_INVALID`
- `INTAKE_OPERATION_MISSING`
- `INTAKE_CLASS_UNKNOWN`
- `INTAKE_ROUTE_UNSUPPORTED`
- `INTAKE_POLICY_BUNDLE_MISSING`
- `INTAKE_POLICY_BUNDLE_STALE`
- `INTAKE_EVALUATOR_ERROR`
- `INTAKE_DECISION_FAMILY_UNRESOLVED`

### Source identity and authority

- `INTAKE_SOURCE_DESCRIPTOR_MISSING`
- `INTAKE_SOURCE_ID_UNRESOLVED`
- `INTAKE_DESCRIPTOR_STALE`
- `INTAKE_DESCRIPTOR_SUPERSEDED`
- `INTAKE_SOURCE_ROLE_MISSING`
- `INTAKE_SOURCE_ROLE_CONFLICT`
- `INTAKE_SOURCE_ROLE_OVERCLAIM`
- `INTAKE_AUTHORITY_INSUFFICIENT`
- `INTAKE_DOMAIN_SCOPE_UNRESOLVED`

### Rights, access, and sensitivity

- `INTAKE_RIGHTS_UNKNOWN`
- `INTAKE_RIGHTS_DENIED`
- `INTAKE_RIGHTS_EXPIRED`
- `INTAKE_ATTRIBUTION_UNRESOLVED`
- `INTAKE_REDISTRIBUTION_RESTRICTED`
- `INTAKE_ACCESS_POSTURE_UNRESOLVED`
- `INTAKE_SENSITIVITY_UNRESOLVED`
- `INTAKE_PROTECTED_CLASS_REVIEW_REQUIRED`
- `INTAKE_PRECISION_OVEREXPOSED`
- `INTAKE_CONSENT_UNRESOLVED`

### Capture, integrity, and content safety

- `INTAKE_DIGEST_MISSING`
- `INTAKE_DIGEST_MISMATCH`
- `INTAKE_BYTES_UNACCOUNTED`
- `INTAKE_CONTENT_TYPE_UNKNOWN`
- `INTAKE_FORMAT_UNSUPPORTED`
- `INTAKE_ARCHIVE_UNSAFE`
- `INTAKE_CONTENT_SCAN_REQUIRED`
- `INTAKE_CONTENT_SCAN_FAILED`
- `INTAKE_CREDENTIAL_MATERIAL_DETECTED`
- `INTAKE_DUPLICATE_CAPTURE`
- `INTAKE_SOURCE_HEAD_CHANGED`

### Review and routing

- `INTAKE_REVIEW_REQUIRED`
- `INTAKE_REVIEW_INSUFFICIENT`
- `INTAKE_REVIEW_REJECTED`
- `INTAKE_QUARANTINE_REQUIRED`
- `INTAKE_QUARANTINE_ROUTE_MISSING`
- `INTAKE_RECEIPT_REQUIRED`
- `INTAKE_AUDIT_CONTEXT_MISSING`
- `INTAKE_RETRY_NOT_AUTHORIZED`
- `INTAKE_RE_ADMISSION_REQUIRED`
- `INTAKE_DENIED`

### Reason-code rules

- Codes are stable identifiers, not sensitive narratives.
- Public messages must not reveal protected source, security, or location details.
- Internal detail belongs in restricted review/audit records.
- Codes must identify the failed gate without embedding payload values.
- New or reinterpreted codes require synchronized contract, schema, fixture, validator, consumer, compatibility, and rollback review.
- A reason code never substitutes for the contributing evidence or decision record.

[Back to top](#top)

---

## Obligation vocabulary

The following obligations are the closed enum in the **proposed** `SourceActivationDecision` schema. They remain inactive until an accepted evaluator and caller enforce them; a string in a valid fixture is not enforcement.

### Source and descriptor obligations

- `require_source_descriptor`
- `require_descriptor_review`
- `require_source_activation_decision`
- `preserve_candidate_source_role`
- `preserve_source_role_limitations`
- `record_domain_scope`
- `record_source_head`
- `require_re_admission_on_source_change`

### Rights and sensitivity obligations

- `require_rights_review`
- `require_attribution`
- `block_redistribution`
- `block_public_release`
- `require_sensitivity_review`
- `withhold_exact_location`
- `generalize_geometry_before_downstream_use`
- `minimize_living_person_data`
- `block_dna_genomic_intake`
- `require_cultural_or_sovereignty_review`

### Capture and security obligations

- `require_digest_pinning`
- `require_ingest_receipt`
- `require_safe_content_scan`
- `strip_or_isolate_credential_material`
- `block_active_content_execution`
- `limit_archive_expansion`
- `use_no_network_processing`
- `store_only_in_restricted_lane`
- `minimize_audit_payload`

### Routing and review obligations

- `route_to_raw_candidate`
- `route_to_quarantine`
- `open_quarantine_case`
- `assign_source_steward`
- `assign_domain_steward`
- `assign_security_review`
- `require_second_review`
- `set_hold_expiry`
- `block_automatic_retry`
- `preserve_prior_decision_refs`

### Correction and rollback obligations

- `emit_superseding_descriptor`
- `invalidate_cached_decisions`
- `link_affected_ingest_receipts`
- `open_correction_review`
- `withdraw_affected_derivatives`
- `preserve_audit_history`
- `verify_rollback_target`

### Obligation enforcement

An obligation is mandatory. If a caller cannot prove that it can enforce every obligation before writing or exposing material, the caller must fail closed.

[Back to top](#top)

---

## Source registry and activation boundary

The source registry records source identity and treatment posture. Intake policy evaluates that posture; it does not create registry truth.

### Registry rules

- A connector may propose a candidate descriptor but must not self-activate it.
- A source steward reviews descriptor identity, role, rights, sensitivity, cadence, access, and citation posture.
- A registry entry must remain distinguishable from an activation decision.
- Descriptor supersession is append-only and traceable.
- Unknown or stale registry state blocks automatic admission.
- A registry record cannot grant public release.
- Public clients must not query internal source registry state directly.

### `SourceActivationDecision` posture

The repository now contains a bounded proposed profile:

| Surface | Current evidence |
|---|---|
| Semantic meaning | [`contracts/source/source_activation_decision.md`](../../contracts/source/source_activation_decision.md), `v0.1.0`, proposed and non-operational |
| Machine shape | [`source_activation_decision.schema.json`](../../schemas/contracts/v1/source/source_activation_decision.schema.json), closed route/reason/obligation vocabularies |
| Fixtures | Synthetic valid, structural-invalid, and semantic-invalid families under [`fixtures/contracts/v1/source/source_activation_decision/`](../../fixtures/contracts/v1/source/source_activation_decision/README.md) |
| Validation | Deterministic no-network validator, focused unit tests, common-contract schema coverage, and read-only [`source-activation-decision-validate`](../../.github/workflows/source-activation-decision-validate.yml) workflow |
| Operational binding | **NOT ESTABLISHED** — no accepted evaluator, bundle, decision authority, reference resolver, registry writer, connector enforcement, receipt sink, governed consumer, or lifecycle writer was proved |

The profile validates bounded shape and local cross-field consistency. It does not accept ADR-0017, authenticate descriptor/policy/review references, activate a source, admit bytes, mutate a registry, create an `IngestReceipt`, write RAW or QUARANTINE, release, or publish.

Until operational binding is accepted:

- use the versioned proposed shape for synthetic review instead of inventing ad hoc activation records;
- do not treat a valid fixture, workflow pass, connector enablement, or descriptor presence as activation evidence;
- do not persist candidate records into an authority lane whose placement has not been accepted;
- fail closed when the caller cannot resolve and enforce every referenced policy, review, and obligation;
- preserve exact profile version, digests, decision lineage, and public-use/release false invariants.

### `SourceIntakeRecord` posture

The proposed [`SourceIntakeRecord`](../../contracts/source/source_intake_record.md) is a separate watcher/source-health candidate envelope. Its schema, fixtures, deterministic validator, focused tests, and read-only [`source-intake-record`](../../.github/workflows/source-intake-record.yml) workflow are **CONFIRMED** at the pinned base.

| Disposition | Permitted candidate posture | Non-effect |
|---|---|---|
| `NO_MATERIAL_CHANGE` | `WORK` observation with no downstream delta | No admission, promotion, or publication |
| `PROPOSED_WORK_RECORD` | `WORK`; may reference a separately governed candidate delta | No automatic mutation or promotion |
| `QUARANTINED` | `QUARANTINE` with blocking drift and policy review required | No pre-RAW activation or quarantine exit |
| `ABSTAIN` | `QUARANTINE`; insufficient support | No implied denial or permission |
| `ERROR` | `QUARANTINE`; bounded processing failure | No partial lifecycle or public effect |

Every proposed record fixes `promotion_required=true` and forbids `PUBLISHED`. It cannot substitute for `SourceActivationDecision`, `PolicyDecision`, `IngestReceipt`, EvidenceBundle, PromotionDecision, or ReleaseManifest.

### Candidate local uploads

User uploads are elevated-uncertainty candidates:

- default source role remains candidate;
- public release is denied by default;
- uploader claims are assertions, not verified metadata;
- rights and sensitivity must be independently reviewed;
- credentials or private data must not be copied into public logs;
- original files remain internal and governed;
- downstream domain binding does not upgrade source authority.

[Back to top](#top)

---

## Receipt and audit boundary

### `IngestReceipt`

`IngestReceipt` records capture facts:

- source id;
- run id;
- start and finish time;
- `SUCCESS`, `PARTIAL`, or `FAIL`;
- byte count;
- SHA-256 digest references.

It does not establish:

- source admission;
- source truth;
- rights clearance;
- sensitivity clearance;
- validation success;
- promotion;
- release;
- public access.

### Proposed intake decision audit

A mature intake audit record should bind:

- immutable input-bundle reference/hash;
- descriptor and registry references;
- contributing policy decisions;
- composed pre-RAW route;
- reason codes;
- obligations;
- evaluator/bundle identity;
- review references;
- ingest receipt or no-capture reason;
- quarantine case reference where applicable;
- evaluation time, expiry, supersession, and correction links.

### Data minimization

Audit records must not include:

- raw file contents;
- secrets or credentials;
- private endpoint tokens;
- complete identity-provider assertions;
- protected personal identifiers;
- exact sensitive locations;
- malware samples;
- full archive listings where names are sensitive;
- unrestricted scanner output;
- source data copied for convenience.

Use safe hashes, references, bounded classifications, and restricted detail stores.

[Back to top](#top)

---

## Quarantine boundary

Intake policy may route material into quarantine. It does not decide how quarantine ends.

### Entry requirements

A quarantine route should identify:

- case/reference id;
- subject/source/material reference;
- reason codes;
- blocked stage;
- required review;
- safe plain-language explanation;
- candidate remediation or safer representation;
- exit criteria;
- audit and receipt references;
- owner, timestamps, and expiry/escalation.

### Exit separation

ADR-0021 proposes five structured exit classes:

1. return to WORK;
2. promote to a PROCESSED candidate;
3. release a safer derivative through normal release gates;
4. deny public use;
5. withdraw or correct a release.

This intake lane:

- may open or require a quarantine case;
- may state why intake cannot proceed;
- must not choose a later promotion or release exit;
- must not move a file as a substitute for a governed transition;
- must not expose quarantine to public clients;
- must preserve original decision and receipt lineage.

### Re-evaluation

A quarantined intake attempt may be re-evaluated only when:

- missing context is supplied;
- rights or sensitivity review changes;
- a corrected descriptor supersedes the prior descriptor;
- content is safely remediated;
- a new policy bundle/version is intentionally selected;
- the prior case and decision remain linked.

Silent retries are forbidden.

[Back to top](#top)

---

## Public-surface and governed-AI boundary

Intake material is never public merely because it was:

- uploaded;
- downloaded;
- parsed;
- scanned;
- hashed;
- assigned a source id;
- placed in RAW;
- recorded in an ingest receipt;
- routed through an intake decision;
- visible in a review console;
- summarized by AI.

Public clients may consume only governed outputs that have traversed the normal evidence, validation, policy, review, promotion, release, correction, and rollback path.

Governed AI must:

- treat intake records as internal process context;
- resolve admissible evidence rather than quoting raw intake;
- abstain when source authority is unresolved;
- never infer rights, sensitivity, source role, or activation from prose;
- never use an intake success as publication permission;
- preserve safe reason codes and avoid exposing protected details.

[Back to top](#top)

---

## Threat model

| Threat | Required control |
|---|---|
| Untrusted upload becomes authoritative | Candidate role, descriptor review, source-role anti-collapse |
| Connector bypasses admission | Pre-RAW gate, descriptor/activation checks, enforced destination limits |
| Rights-unknown content enters public pipeline | Fail closed, quarantine, rights review, public-release denial |
| Sensitive location or personal data leaks through metadata | Minimize metadata, classify sensitivity, quarantine, no public raw path |
| Credential or token embedded in uploaded material | Detection, isolation, restricted handling, secret-safe logging |
| Malicious or active content executes during intake | Sandboxed/no-network processing, content-type checks, execution denial |
| Archive expansion or resource exhaustion | Bounded resource policy, safe failure, quarantine/deny |
| Hash or byte-accounting mismatch hidden by retries | Immutable receipt, explicit error, re-ingest with new run |
| Source role upgraded by user claims or AI | Registry-backed role, steward review, no generated authority |
| Stale descriptor reused after terms change | freshness/expiry checks, re-admission, cache invalidation |
| Duplicate capture creates conflicting identities | duplicate/collision checks, deterministic refs, steward resolution |
| Quarantine becomes a staging shortcut | structured case, governed exits, no public client access |
| Intake is mislabeled as promotion | contract distinction and dedicated orchestration decision |
| `docs/intake/` proposal is treated as admitted source | concept separation and source descriptor requirement |
| Audit log leaks protected payloads | references, hashes, minimization, restricted detail records |
| Retry storm repeatedly fetches denied content | retry authorization, backoff outside policy, terminal denial/hold |
| Compromised connector changes source silently | source-head checks, digest comparison, review, deactivation path |
| AI explains denial with sensitive detail | public-safe reason mapping and restricted internal reasons |

[Back to top](#top)

---

## Validation and acceptance

### Validation layers

| Layer | Current evidence | What it cannot prove alone |
|---|---|---|
| Markdown validation | Bounded local link/fragment checker plus structural review for this README | Policy correctness, accepted authority, or runtime enforcement |
| Activation contract/schema validation | Proposed `SourceActivationDecision` schema, exact fixture polarity, semantic validator, focused tests, and read-only workflow | Policy evaluation, reference authenticity, connector enforcement, lifecycle writes, or source activation |
| Watcher intake-record validation | Proposed `SourceIntakeRecord`/`DriftSummary` shapes, fixtures, validator, focused tests, and read-only workflow | Pre-RAW admission, policy approval, promotion, release, or deployed watcher behavior |
| Native intake-policy tests | **NOT ESTABLISHED** because no executable rule is local to `policy/intake/` | Any allow, deny, hold, quarantine, or error behavior |
| Connector contract tests | Adjacent connector-gate and connector suites exist; complete intake-policy binding is **UNKNOWN** | Rights or sensitivity truth, registry authority, or public safety |
| Registry and quarantine tests | Adjacent candidate surfaces exist; end-to-end activation/exit enforcement is **NOT ESTABLISHED** | Admission, promotion, release, or publication approval |
| Runtime and release drills | **UNKNOWN / NOT ESTABLISHED for this lane** | Production health, historical replay, or source/evidence truth |

### Current repository-native checks

These commands exercise the bounded companions and documentation surface. They do not run an intake policy evaluator:

```bash
# Proposed SourceActivationDecision: shape, polarity, and semantic invariants.
python -m unittest discover \
  --start-directory tests/validators \
  --pattern 'test_validate_source_activation_decision.py' \
  --verbose

python tools/validators/validate_source_activation_decision.py --fixtures

python -m pytest -q tests/schemas/test_common_contracts.py \
  -k source_activation_decision

# Proposed SourceIntakeRecord: watcher candidate envelope, not activation policy.
python -m unittest tests.validators.test_validate_source_intake_record -v
python tools/validators/validate_source_intake_record.py --fixtures

# This README: local files, fragments, and repository-relative targets.
python tools/validators/docs/link-check/check_links.py \
  --repo-root . \
  --format text \
  policy/intake/README.md

git diff --check
```

The `source-activation-decision-validate` and `source-intake-record` workflow definitions use read-only contents permission and no-network validator posture. Their presence does not prove required-check coupling or a successful run for this revision.

### Minimum synthetic test matrix

The matrix below is the minimum **future native-policy and integration burden**. Some activation-record cases overlap existing fixture coverage; no local `policy/intake/` rule suite covers the complete matrix today.

#### Positive

- admitted public publisher source with verified open rights and current descriptor;
- restricted source admitted to RAW with public-release block;
- user upload routed as candidate with steward-review obligation;
- metadata-only refresh with unchanged source head;
- corrected descriptor triggering controlled re-admission;
- safe partial capture routed to quarantine with complete audit context.

#### Negative

- missing descriptor;
- stale or superseded descriptor;
- source-role overclaim;
- unknown or denied rights;
- unresolved sensitivity;
- exact sensitive location in metadata;
- missing digest;
- digest mismatch;
- unsupported format;
- required scan unavailable;
- credential material detected;
- archive/resource bound exceeded;
- unknown domain scope;
- missing reviewer;
- evaluator unavailable;
- caller cannot satisfy obligations;
- direct write request to PROCESSED or PUBLISHED;
- retry of denied intake without new basis;
- attempt to use `policy_family=intake`;
- attempt to treat `IngestReceipt.SUCCESS` as admission.

#### Composition

- sensitivity `DENY` + access `ANSWER` => no admission;
- rights unresolved + all other checks pass => quarantine/hold;
- policy evaluator error => no admitted state;
- descriptor changed after decision => stale decision invalidated;
- candidate source + public destination request => deny public route;
- quarantine case missing => routing failure;
- public client requests RAW intake record => deny.

### No-network fixture requirements

- all fixtures synthetic;
- no real credentials or tokens;
- no live endpoint calls;
- no real protected identities or exact sensitive locations;
- no executable malicious samples;
- deterministic timestamps/hashes where practical;
- explicit expected reason codes and obligations;
- valid and invalid cases both required.

### Acceptance gates

Before executable intake policy is treated as active, require:

1. accepted ADR-0017 disposition and a local rule/package/precedence decision consistent with the adopted policy root;
2. complete intake-specific input profile with no hidden fetches or secret-bearing fields;
3. accepted or explicitly replaced `SourceActivationDecision` contract/schema strategy;
4. explicit composition with independent rights, sensitivity, access, consent, and other applicable policy decisions;
5. source-descriptor schema-authority convergence and compatibility handling;
6. immutable bundle manifest, selector, module digest, and entrypoint;
7. pinned evaluator plus positive, negative, abstain, deny, error, and obligation native tests;
8. connector enforcement and destination/no-bypass tests;
9. source-registry activation, supersession, deactivation, and re-admission tests;
10. quarantine-case contract plus structured entry and exit integration;
11. decision receipt/audit contract with data-minimization review;
12. governed consumer resolution and obligation enforcement;
13. correction, re-admission, expiry, revocation, cache invalidation, and rollback drills;
14. observed required CI checks and branch/ruleset coupling;
15. accountable owners, specialist review, and separation of duties.

`SourceIntakeRecord` graduation is required only for watcher/source-health flows that use that object. It is not a substitute for, or universal prerequisite of, the pre-RAW activation decision.

[Back to top](#top)

---

## Smallest sound implementation sequence

1. Accept, revise, or supersede ADR-0017 responsibility boundaries.
2. Define the local intake-rule package, input profile, entrypoint, native outcomes, precedence, and relationship to `policy/source/`, `policy/rights/`, and `policy/sensitivity/`.
3. Review and either accept, revise, or replace the fixture-first `SourceActivationDecision` profile; preserve its public-use and release-denial boundary.
4. Create an explicit intake-specific input profile instead of extending the permissive parent bundle by convention.
5. Bind independent policy-family results without adding an unversioned family or misusing promotion.
6. Converge SourceDescriptor schema authority and preserve compatibility pointers.
7. Add native policy modules, synthetic fixtures, and positive/negative/abstain/deny/error tests.
8. Bind source-registry resolution, descriptor supersession, and activation lineage.
9. Bind connector destinations and prove no bypass into RAW, PROCESSED, or public paths.
10. Implement structured quarantine-case creation while keeping exits separately governed.
11. Add decision receipt/audit emission with safe reasons, enforceable obligations, and data minimization.
12. Bind governed review and operational consumers; integrate `SourceIntakeRecord` only for watcher flows that require it.
13. Run correction, re-admission, deactivation, expiry, cache invalidation, and rollback drills.
14. Activate only through an immutable reviewed bundle, required checks, independent review, and a verified rollback target.

Each step should remain independently reviewable and reversible.

[Back to top](#top)

---

## Review burden

| Change class | Minimum review posture |
|---|---|
| README-only clarification | policy-aware maintainer + docs review |
| Intake rule module | policy steward + intake/source steward + validation reviewer |
| Source role or authority rule | source steward + affected domain steward + evidence reviewer |
| Rights or license rule | rights reviewer + policy steward |
| Sensitive class or precision rule | specialist steward + privacy/security + policy reviewer |
| Local upload or active-content rule | security reviewer + connector/app owner + policy reviewer |
| Descriptor or intake contract/schema change | contract + schema + policy + validator/test + migration reviewers |
| New decision family | contracts + schemas + runtime + consumers + migration + release/rollback review |
| Source activation or deactivation | source steward + policy + registry/connector owner |
| Quarantine route or reason code | quarantine steward + policy + affected domain reviewer |
| Bundle/selector/signing change | policy-runtime + supply-chain/security + validation + operations |
| Public API/UI exposure | governed API/UI + policy + privacy/security + release review |
| Correction/re-admission/withdrawal | source + policy + evidence + release + operations, with separation of duties |

CODEOWNERS routing is not proof of accepted stewardship or independent approval.

[Back to top](#top)

---

## Correction, re-admission, revocation, and rollback

### Re-admission triggers

A new intake evaluation is required when:

- source terms or rights change;
- sensitivity classification changes;
- source role or authority posture changes;
- upstream ownership/stewardship changes;
- endpoint/access posture changes;
- source-head identity changes materially;
- cadence or staleness policy expires;
- connector implementation changes trust-relevant behavior;
- a prior decision expires or is revoked;
- a correction affects source identity or captured bytes;
- a previously denied source supplies new admissible evidence.

### Correction rules

- Never edit a historical decision to appear current.
- Supersede descriptors and decisions with explicit links.
- Preserve affected ingest receipts and run references.
- Identify downstream derivatives affected by the changed source.
- Do not silently recalculate public outputs.
- Require normal promotion/release review for corrected derivatives.
- Preserve the original denial/quarantine rationale subject to minimization.

### Revocation and deactivation

A source or intake permission may need deactivation when:

- rights are withdrawn;
- credentials or access were compromised;
- source integrity fails;
- publisher identity changes;
- sensitivity is reclassified;
- source authority was overstated;
- repeated harmful or malformed submissions occur;
- required reviews expire;
- the policy bundle is revoked.

Deactivation must invalidate cached decisions and prevent new captures without destroying audit lineage.

### Documentation rollback

Before merge, close or abandon the draft pull request and its feature branch. After merge, use a reviewed revert or forward-fix pull request; do not rewrite shared history. The v0.1 baseline is blob `b5682be75bf480806dde2cfb3bbe2879fe52e454`.

Reverting this README alone changes no runtime policy because this lane contains no executable rule. It would, however, restore materially stale claims that the activation/intake-record contract families do not exist. Prefer a forward fix when repository evidence has advanced.

### Operational rollback

A future intake implementation must support:

- bundle rollback;
- connector disablement;
- registry activation rollback;
- decision-cache invalidation;
- quarantine-route rollback without public exposure;
- receipt and audit preservation;
- restoration of the last known safe descriptor/activation state;
- downstream correction or withdrawal where admitted material already propagated.

[Back to top](#top)

---

## Open verification register

| ID | Question | Status | Closure evidence |
|---|---|---|---|
| `INTAKE-POL-001` | What local rule/package role should `policy/intake/` have beneath the adopted policy root? | **CONFIRMED placement / NEEDS VERIFICATION for the local role** | accepted ADR-0017 disposition, package/entrypoint contract, and bundle map |
| `INTAKE-POL-002` | How does it compose with `policy/source/`, `policy/rights/`, and `policy/sensitivity/`? | **NEEDS VERIFICATION** | bundle contract and native tests |
| `INTAKE-POL-003` | Is source admission the only scope, or are other material-intake classes included? | **NEEDS VERIFICATION** | accepted scope statement and fixtures |
| `INTAKE-POL-004` | Which decision contract represents overall pre-RAW admission? | **PROPOSED fixture-first `SourceActivationDecision`; acceptance and operation unresolved** | accepted semantic contract, schema, ADR disposition, evaluator, and consumer |
| `INTAKE-POL-005` | Does `SourceActivationDecision` remain the accepted object name and version lineage? | **PROPOSED / NEEDS VERIFICATION** | contract review, ADR disposition, compatibility policy, and consumer tests |
| `INTAKE-POL-006` | What is the accepted role of `SourceIntakeRecord` relative to watcher observations and activation? | **PROPOSED watcher envelope / CONFIRMED separation** | accepted event-family decision and watcher integration tests |
| `INTAKE-POL-007` | Which SourceDescriptor schema path is canonical? | **CONFLICTED** | ADR/schema migration and compatibility tests |
| `INTAKE-POL-008` | Which intake fields become required in an explicit policy input profile? | **NEEDS VERIFICATION; existing profile v1 excludes intake** | accepted profile schema, fixtures, and no-hidden-fetch tests |
| `INTAKE-POL-009` | Which policy family or composition strategy is accepted? | **PROPOSED separate activation composition / UNKNOWN active binding** | accepted contract/schema/runtime integration |
| `INTAKE-POL-010` | Which routing states are accepted? | **PROPOSED closed enum in `SourceActivationDecision`** | accepted contract, evaluator, consumer, and migration evidence |
| `INTAKE-POL-011` | Which reason codes and obligations are accepted and enforced? | **PROPOSED closed enums in `SourceActivationDecision`** | adopted registry/schema plus caller enforcement tests |
| `INTAKE-POL-012` | Which evaluator, bundle, selector, and entrypoint are accepted? | **UNKNOWN** | pinned runtime and native test run |
| `INTAKE-POL-013` | Which connectors enforce admission before RAW writes? | **UNKNOWN** | connector inventory and contract tests |
| `INTAKE-POL-014` | Which local-upload surfaces are deployed? | **UNKNOWN** | application/runtime evidence |
| `INTAKE-POL-015` | Which content/security scanner profiles are approved? | **UNKNOWN** | security architecture and observed tests |
| `INTAKE-POL-016` | Is the source authority register populated and consumed? | **UNKNOWN** | register entries and consumer evidence |
| `INTAKE-POL-017` | Which quarantine-record contract/schema is accepted? | **UNKNOWN** | accepted contract, schema, fixtures, validator |
| `INTAKE-POL-018` | Which receipt/audit sink records admission safely? | **UNKNOWN** | threat-reviewed contract and tests |
| `INTAKE-POL-019` | Which governed applications enforce obligations? | **UNKNOWN** | implementation and integration tests |
| `INTAKE-POL-020` | How are retries, holds, expiry, and escalation governed? | **CONFIRMED fixture-first invariants / UNKNOWN operation** | operational contract, consumer tests, and drills |
| `INTAKE-POL-021` | How are source changes detected and re-admission triggered? | **NEEDS VERIFICATION** | source-head/cadence tests and runbook |
| `INTAKE-POL-022` | How are cached decisions invalidated on rights/sensitivity changes? | **UNKNOWN** | dependency graph and invalidation drill |
| `INTAKE-POL-023` | Which CI checks are required and branch-protected? | **UNKNOWN** | workflow runs and ruleset evidence |
| `INTAKE-POL-024` | Who owns intake, source, rights, sensitivity, security, registry, connector, quarantine, and release review? | **NEEDS VERIFICATION** | accepted stewardship and separation-of-duties record |
| `INTAKE-POL-025` | Has an end-to-end admit/quarantine/deny/re-admit/rollback drill succeeded? | **UNKNOWN** | signed drill report and verified artifact state |
| `INTAKE-POL-026` | Are public fixtures/logs free of secrets and protected payloads? | **CONFIRMED bounded synthetic fixtures / NEEDS VERIFICATION for system evidence** | secret scan, fixture review, and deployed log tests |
| `INTAKE-POL-027` | Has `docs/intake/` versus source/material intake terminology been formally reconciled? | **CONFIRMED documented separation / NEEDS VERIFICATION for a formal decision** | glossary/ADR/documentation review |
| `INTAKE-POL-028` | Are activation, watcher intake, promotion, and release prevented from collapsing? | **CONFIRMED partial contract-level separation / UNKNOWN runtime** | cross-object tests, static guards, and end-to-end runtime evidence |

[Back to top](#top)

---

## Evidence and no-loss ledger

| Baseline element | v0.2 disposition |
|---|---|
| Stable path, document ID, H1, top anchor, and major section anchors | **PRESERVED** |
| Purpose, authority split, scope, non-collapse rules, fail-closed posture, threat model, review, correction, and public trust membrane | **PRESERVED and clarified** |
| Empty-target and greenfield-sibling claims | **REPAIRED** because they no longer describe the pinned tree |
| `SourceActivationDecision` absence claim | **REPAIRED** with exact proposed contract/schema/fixture/validator/test/workflow evidence and non-effects |
| `SourceIntakeRecord` absence claim | **REPAIRED** and separated from pre-RAW activation and promotion |
| Reason and obligation lists | **BOUND** to the current proposed activation schema; added `INTAKE_ADMITTED` and removed the non-schema `INTAKE_ACTIVATION_DECISION_MISSING` value |
| Policy input posture | **UPDATED** for explicit profile v1, which exists but excludes intake and source activation |
| Directory Rules and README inheritance | **ADDED** with accepted ADR-0029 basis, `BOUNDARY_COMPACT` profile, and verified direct-child map |
| Validation | **UPDATED** with current repository-native commands and explicit proof limits |
| Runtime, release, and publication claims | **PRESERVED as unproved/non-effects** |

This ledger records documentation reconciliation only. No contract, schema, fixture, validator, workflow, rule, registry, lifecycle record, receipt, release, or public artifact changed.

[Back to top](#top)

---

## Last reviewed

**2026-08-13** against `main@ad31275429d715ad92002f8f2e160299193c9f50`.

Reviewed the complete prior README; accepted ADR-0029 and Directory Rules sections 9.3 and 16; parent and adjacent policy READMEs; the complete local directory; ADR-0017 and ADR-0021 status; SourceDescriptor, SourceActivationDecision, SourceIntakeRecord, IngestReceipt, PolicyInputBundle, and PolicyDecision families; related fixtures, validators, tests, workflows, CODEOWNERS, contribution rules, source-registry, connector, ingest, quarantine, and release boundaries; and open pull-request overlap.

This review confirms current repository bytes and bounded validation definitions. It does not accept ADR-0017 or ADR-0021, activate an intake bundle, authenticate a decision, approve a source, enable a connector, admit a file, mutate a registry, clear rights or sensitivity, open or close a quarantine case, promote material, approve release, deploy, or create publication state.

---

## Changelog

| Version | Date | Change | Rollback |
|---|---|---|---|
| v0.1 | 2026-07-24 | Completed the previously empty lane with a repository-grounded pre-RAW admissibility boundary and explicit non-effects. | Historical blob `b5682be75bf480806dde2cfb3bbe2879fe52e454` |
| v0.2 | 2026-08-13 | Reconciled adopted Directory Rules, current policy siblings, fixture-first activation/intake-record families, exact proposed vocabularies, validation commands, open work, and rollback while preserving the documentation-only boundary. | Revert or forward-fix the v0.2 documentation commit; no operational cleanup is required. |

[Back to top](#top)

---

## Maintainer checklist

Before adding executable intake policy or child lanes:

- [ ] preserve the adopted singular `policy/` placement and decide the local package/entrypoint relationship to `policy/source/`;
- [ ] preserve the separation between source/material intake and `docs/intake/`;
- [ ] accept, revise, or supersede ADR-0017 before claiming operational admission architecture;
- [ ] accept, revise, or replace the proposed `SourceActivationDecision` profile and its compatibility lineage;
- [ ] keep `SourceIntakeRecord` limited to watcher/source-health candidate observations unless a reviewed versioned change says otherwise;
- [ ] decide the policy-family composition strategy without misusing promotion;
- [ ] converge SourceDescriptor schema authority;
- [ ] create an explicit non-secret intake input profile; do not infer intake support from the permissive parent or profile v1;
- [ ] bind exact package, entrypoint, bundle, evaluator, reasons, obligations, version, and rollback;
- [ ] use synthetic, no-network fixtures;
- [ ] test local upload, publisher feed, refresh, correction, and denial paths;
- [ ] test rights, sensitivity, source-role, integrity, format, scan, review, and evaluator failures;
- [ ] prove connectors cannot bypass the gate;
- [ ] prove quarantine records are structured and not public;
- [ ] prove obligations are enforced by callers;
- [ ] minimize payload data in decisions, logs, and receipts;
- [ ] prove re-admission, deactivation, cache invalidation, correction, and rollback;
- [ ] keep promotion, release approval, and publication outside this directory.

> **Final boundary:** intake policy may decide whether external material is admissible at the pre-RAW edge; source descriptors and registries preserve source posture; connectors capture; receipts remember; quarantine holds; promotion advances; evidence supports claims; release governs publication; and public clients consume only released outputs through governed interfaces.

[Back to top](#top)
