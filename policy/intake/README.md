<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://policy/intake
title: Intake Admissibility Policy Boundary and Pre-RAW Routing Contract
type: policy-readme
version: v0.1
status: draft; repository-grounded; empty-target-completion; pre-raw-intake-routing; source-admission-aware; docs-intake-separated; non-connector; non-registry; non-promotion; evaluator-unbound; fail-closed; non-release; non-publication
owner: NEEDS VERIFICATION — intake steward, source steward, policy steward, rights reviewer, sensitivity reviewer, security reviewer, affected domain stewards, connector maintainer, registry maintainer, quarantine steward, release reviewer, docs steward
created: 2026-07-24
updated: 2026-07-24
policy_label: repository-facing; intake; source-admission; pre-raw; candidate-material; local-upload; quarantine-routing; source-role; rights; sensitivity; integrity; fail-closed; no-secrets; no-public-path
current_path: policy/intake/README.md
owning_root: policy/
canonical_relationship: PROPOSED pre-RAW intake admissibility-routing boundary; it must not replace policy/source/, source registry authority, connector behavior, docs/intake idea canonicalization, quarantine exit governance, or downstream promotion
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  target_prior_blob: 8b137891791fe96927ad78e64b0aad7bded08bdc
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  policy_root_blob: fa9378a6a699d0985fd018dbdb9f27c15efcb1c3
  source_policy_stub_blob: 943fa9991f259721920b93f9c13eec07b4197502
  promotion_policy_stub_blob: b082c06e5f0889739e56a07216e89164e46e4076
  rights_policy_stub_blob: 5dffc3a0ca80d8d94a8008e6c60b2f9489d5f077
  sensitivity_policy_stub_blob: 635bbed7f1ca58f7fea5bd0a4956cdc8becb7529
  source_admission_adr_blob: 58693830fcdf9746c5494fdd85298529fa5594a9
  quarantine_exit_adr_blob: 95648b9967e02bfe662d4f6103de10ee5a467d21
  admission_process_doc_blob: ab27618a4b1b0e6775d18bedca37aa7d6c514e6e
  docs_intake_canonicalization_blob: f38582fa6aa84f2069d66a09ea6af502414e9165
  source_descriptor_contract_blob: b57ae5ccc042c1423b75c168438800384c9b6713
  ingest_receipt_contract_blob: 4273a9bad9edc7ce7f54c288075f8a49b0f2fe80
  policy_input_contract_blob: 545c352681dd0db0cd4d169a5d2f9c364356457c
  policy_input_schema_blob: b89db4b1730c61258441e0eed037276b910b1990
  policy_decision_contract_blob: ebfe97f98263e6309db6d2772cb2c5e548819650
  policy_decision_schema_blob: 1472d26a42c73f17545b4464a275412ffa1d098e
  quarantine_runbook_blob: 89193c775cb27dac245d9552a3b5bf0c15c11eac
  source_registry_readme_blob: 2821e9681273bff6b430920d0a45312c5643ba33
  local_upload_product_doc_blob: 8e621cf36c2d6ad2d74a0f8e3badee6a8fc998f6
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
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0017-source-descriptor-admission-process.md
  - ../../docs/adr/ADR-0021-quarantine-has-structured-exit-paths.md
  - ../../docs/sources/ADMISSION_PROCESS.md
  - ../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md
  - ../../docs/intake/canonicalization-policy.md
  - ../../docs/runbooks/QUARANTINE_HANDLING.md
  - ../../contracts/source/source_descriptor.md
  - ../../contracts/source/ingest_receipt.md
  - ../../contracts/policy/policy_input_bundle.md
  - ../../contracts/policy/policy_decision.md
  - ../../schemas/contracts/v1/source/source_descriptor.schema.json
  - ../../schemas/contracts/v1/source/ingest_receipt.schema.json
  - ../../schemas/contracts/v1/policy/policy_input_bundle.schema.json
  - ../../schemas/contracts/v1/policy/policy_decision.schema.json
  - ../../data/registry/sources/README.md
  - ../../connectors/README.md
  - ../../pipelines/ingest/README.md
  - ../../packages/source-registry/README.md
  - ../../packages/policy-runtime/README.md
  - ../../tools/validators/connector_gate/README.md
  - ../../apps/governed-api/README.md
  - ../../release/README.md
tags: [kfm, policy, intake, source-admission, pre-raw, source-descriptor, source-intake-record, source-activation-decision, ingest-receipt, connector, local-upload, quarantine, rights, sensitivity, source-role, integrity, fail-closed]
truth_posture: CONFIRMED empty tracked target, singular policy root, proposed source-admission and quarantine ADRs, source-admission guidance, separate docs/intake idea-canonicalization lane, SourceDescriptor and IngestReceipt contracts, source registry documentation, local-upload risk posture, greenfield source/rights/sensitivity/promotion policy stubs, PolicyInputBundle placeholder schema, closed PolicyDecision families without intake or source, and unproved admission evaluator/runtime/release integration / PROPOSED intake routing contract, explicit inputs, evaluation order, reason codes, obligations, composed decisions, pre-RAW routing states, tests, convergence plan, correction, re-admission, revocation, and rollback / UNKNOWN accepted intake policy family, SourceActivationDecision contract, SourceIntakeRecord contract, active bundle, native tests, connector enforcement, registry activation, quarantine-record schema, audit sink, branch-protection enforcement, and production operation
notes:
  - "This revision completes an existing empty README in place. It creates no source descriptor instance, connector, parser, scanner, policy module, schema, contract, fixture, validator, registry record, quarantine record, receipt, runtime route, release object, or publication state."
  - "Source admission, idea canonicalization, ingest execution, source registry authority, quarantine handling, promotion, and release are separate governed responsibilities."
  - "The current PolicyDecision schema permits promotion, access, render, capability, consent, and sensitivity only; policy_family=intake and policy_family=source are schema-invalid at the inspected snapshot."
  - "Secrets, credentials, private endpoints, bearer tokens, malware samples, protected identifiers, and raw sensitive payloads must never be placed in this repository-facing README or public fixtures."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Intake Admissibility Policy Boundary

> **One-line purpose.** `policy/intake/` documents the fail-closed policy boundary that decides whether externally supplied material has enough explicit source, rights, sensitivity, integrity, role, review, and routing context to enter KFM's governed lifecycle at the pre-RAW edge—without becoming a connector, source registry, idea-intake process, quarantine-exit authority, promotion gate, release authority, or publication path.

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#status-and-evidence)
[![Scope: pre-RAW intake](https://img.shields.io/badge/scope-pre--RAW%20intake-0969da?style=flat-square)](#purpose)
[![Default: fail closed](https://img.shields.io/badge/default-fail%20closed-b42318?style=flat-square)](#default-posture)
[![Decision family: unresolved](https://img.shields.io/badge/decision%20family-unresolved-d97706?style=flat-square)](#decision-contract-compatibility)
[![Quarantine: governed route](https://img.shields.io/badge/quarantine-governed%20route-8250df?style=flat-square)](#quarantine-boundary)
[![Publisher: no](https://img.shields.io/badge/publisher-no-6e7781?style=flat-square)](#authority-level)

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status-and-evidence) · [Scope](#scope-and-bounded-context) · [Separation](#intake-concept-separation) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#explicit-policy-input-profile) · [Evaluation](#evaluation-order) · [Decisions](#decision-contract-compatibility) · [Routing](#proposed-intake-routing-states) · [Outcomes](#normalized-policy-outcomes) · [Reasons](#reason-code-vocabulary) · [Obligations](#obligation-vocabulary) · [Registry](#source-registry-and-activation-boundary) · [Receipts](#receipt-and-audit-boundary) · [Quarantine](#quarantine-boundary) · [Threats](#threat-model) · [Validation](#validation-and-acceptance) · [Review](#review-burden) · [Rollback](#correction-re-admission-revocation-and-rollback) · [Open work](#open-verification-register)

> [!IMPORTANT]
> **Safe current conclusion:** the repository has source-admission doctrine, a rich proposed `SourceDescriptor` contract and schema slice, an `IngestReceipt` contract, source-registry documentation, quarantine guidance, and shape-validation evidence. It does **not** establish an accepted intake policy family, active intake bundle, `SourceActivationDecision` contract, `SourceIntakeRecord` contract, populated authority register, native intake-policy tests, functional admission service, complete connector enforcement, decision-receipt flow, or production operation.

> [!CAUTION]
> **Admission is not promotion.** Intake decides whether material may cross the pre-RAW trust edge into RAW, QUARANTINE, or a terminal denial posture. Promotion later decides whether admitted material may advance through `RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED`. Neither transition is a file move.

> [!WARNING]
> **Do not confuse this lane with `docs/intake/`.** The documentation-intake lane handles ideas, drafts, packets, and canonicalization proposals. This policy lane concerns operation-specific admissibility of external material at the lifecycle boundary. A long, polished, repeated, or plausible document is not automatically admissible data, policy, doctrine, or implementation truth.

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

This README is a **repository-facing draft boundary**, not active policy.

| Concern | Owning surface | Role of `policy/intake/` |
|---|---|---|
| Intake admissibility rules | `policy/` after accepted placement, rule, bundle, and review | Potential rule/routing authority only after acceptance |
| Source meaning and admissibility fields | [`contracts/source/source_descriptor.md`](../../contracts/source/source_descriptor.md) | Consume; never redefine |
| Ingest receipt meaning | [`contracts/source/ingest_receipt.md`](../../contracts/source/ingest_receipt.md) | Consume or require; never emit/store here |
| Machine shape | `schemas/contracts/v1/` | Require accepted shapes; never define them here |
| Source registry instances and authority posture | [`data/registry/sources/`](../../data/registry/sources/README.md) | Resolve; never silently activate or mutate |
| Source-admission architecture | ADR-0017 and source-admission standards | Follow; never accept the ADR by documentation |
| Connector and watcher execution | `connectors/` | Constrain through policy; never implement fetching here |
| Ingest implementation | `pipelines/ingest/`, connector-local code, accepted runtime roots | Constrain; never become pipeline code |
| Security/content scanning | accepted tools/services and validators | Consume bounded results; never store samples or secrets |
| Quarantine records and handling | `data/quarantine/`, runbooks, accepted contracts/schemas | Route into; never invent an exit or publish from quarantine |
| Policy evaluation mechanics | `packages/policy-runtime/` or accepted evaluator | Supply accepted rules; never become runtime helpers |
| Validation | `tools/validators/`, `tests/`, `fixtures/` | Specify expected behavior; never claim unobserved coverage |
| Promotion | `policy/promotion/`, promotion contracts, lifecycle gates | Remain separate; admission does not promote |
| Release, correction, withdrawal, rollback | `release/` and governed runbooks | Remain separate; intake cannot publish or withdraw alone |
| Public API/UI/AI behavior | governed applications using released outputs | No direct public path |

A successful intake decision means only that the evaluated intake operation satisfied its current gate. It does not establish source truth, evidence closure, catalog authority, public safety, or release approval.

[Back to top](#top)

---

## Status and evidence

### Current repository state

| Surface | Status | Safe conclusion |
|---|---:|---|
| `policy/intake/README.md` | **CONFIRMED empty before this revision** | A tracked lane existed without a documented boundary |
| `policy/README.md` | **CONFIRMED repository-grounded draft** | Singular `policy/` is the admissibility root; evaluator and bundle remain unproved |
| `policy/source/README.md` | **CONFIRMED greenfield stub** | Source-policy authority is not operationally established |
| `policy/rights/README.md` | **CONFIRMED greenfield stub** | Rights-policy evaluation is not established by the stub |
| `policy/sensitivity/README.md` | **CONFIRMED greenfield stub** | Sensitivity-policy evaluation is not established by the stub |
| `policy/promotion/README.md` | **CONFIRMED greenfield stub** | Promotion-policy implementation remains unproved and separate from intake |
| ADR-0017 | **CONFIRMED proposed** | Source admission architecture is documented but not accepted or operational |
| ADR-0021 | **CONFIRMED proposed** | Quarantine exit discipline is documented but not accepted as implementation proof |
| `docs/sources/ADMISSION_PROCESS.md` | **CONFIRMED draft** | Defines the pre-RAW admission membrane and separates admission from promotion |
| `docs/intake/canonicalization-policy.md` | **CONFIRMED draft** | Governs idea/document canonicalization, not source-material admission |
| `SourceDescriptor` contract | **CONFIRMED draft / PROPOSED** | Rich semantic contract exists |
| SourceDescriptor schema/fixtures/workflow | **CONFIRMED partial slice** | Shape validation exists; admission authority does not |
| `IngestReceipt` contract | **CONFIRMED draft / PROPOSED** | Records capture outcome and digests; not policy or release |
| Source registry README | **CONFIRMED documentation / mixed freshness** | Intended authority surface exists; populated operational conformance is unproved |
| `PolicyInputBundle` | **CONFIRMED semantic contract + permissive schema stub** | Complete intake context is not machine-enforced |
| `PolicyDecision` | **CONFIRMED closed outcome/family schema** | No `intake` or `source` policy family exists |
| `SourceActivationDecision` | **Doctrine-named / contract not established** | Must not be treated as implemented |
| `SourceIntakeRecord` | **Doctrine-named / contract not established** | Must not be treated as implemented |
| Active intake evaluator, bundle, selector, receipts, runtime, CI, deployment | **UNKNOWN / NEEDS VERIFICATION** | This README is not implementation proof |

### Evidence boundary

This README may state current repository facts and bounded doctrine. It must not claim:

- any named source is admitted, active, current, reachable, or licensed;
- any connector is safely enabled;
- any upload route is deployed;
- any malware or content-scanning service is configured;
- any source authority register is populated;
- any `SourceActivationDecision` is emitted;
- any `SourceIntakeRecord` schema exists;
- intake decisions are cached, replayed, or receipt-backed;
- native intake policy tests run in CI;
- quarantine exits are operational;
- a release or publication occurred.

Those claims remain `UNKNOWN` or `NEEDS VERIFICATION` until current implementation, test, workflow, artifact, and runtime evidence proves them.

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
| Source/material intake policy | May this external material enter the lifecycle under explicit conditions? | `policy/intake/` if accepted | Primary scope |
| Source admission architecture | What records, stages, and authority boundaries govern admission? | ADR-0017 and `docs/sources/` | Follow |
| Source identity and treatment | What is the source, and how may KFM treat it? | `SourceDescriptor` + source registry | Resolve and evaluate |
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
5. A successful `IngestReceipt` is not an admissibility decision.
6. An intake decision is not a promotion decision.
7. A quarantine route is not a quarantine exit.
8. A passed scanner result is not evidence or rights clearance.
9. A source registry entry is not claim truth.
10. An idea promoted through `docs/intake/` is not automatically admissible source material.

[Back to top](#top)

---

## What belongs here

Good fits for `policy/intake/` after placement is accepted include:

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
| SourceDescriptor meaning | `contracts/source/` |
| SourceDescriptor or intake JSON Schema | `schemas/contracts/v1/` |
| SourceDescriptor instances or source authority records | `data/registry/sources/` and accepted control-plane registers |
| Raw, uploaded, downloaded, or quarantined payloads | governed `data/` lifecycle lanes |
| Connector, watcher, crawler, importer, upload, or fetch code | `connectors/`, `packages/`, `apps/`, or pipelines by responsibility |
| Parser, normalizer, transformer, or content conversion code | `packages/` and `pipelines/` |
| Antivirus binaries, signatures, malware samples, exploit samples | approved secure tooling and test systems; never public policy docs |
| Credentials, API keys, bearer tokens, private endpoints, session data | secret management and approved runtime configuration |
| Ingest receipts, run receipts, quarantine records, review records | accepted receipt, data, review, or governance roots |
| PolicyDecision instances | accepted emitted-decision or receipt lanes |
| Source activation records | accepted governance/receipt home after contract decision |
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

A mature intake evaluation should receive an explicit `PolicyInputBundle` or a versioned intake-specific profile. The current schema requires only `id` and permits additional properties, so the fields below are **PROPOSED semantics**, not machine-enforced facts.

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
14. **Choose a pre-RAW route.** ADMIT-to-RAW candidate, QUARANTINE, DENY, or ERROR/HOLD under an accepted routing contract.
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

The repository must choose one reviewed option before implementation:

1. **Composed existing families plus separate activation object.** Independent `PolicyDecision` records remain in their existing families; an accepted `SourceActivationDecision` composes them into the pre-RAW route.
2. **Versioned new policy family.** Add `intake` or `source` only through contract/schema versioning, fixtures, validators, consumer migration, decision receipts, and rollback.
3. **Promotion-family reuse with explicit pre-RAW operation.** This is **not recommended without an ADR**, because current doctrine explicitly separates admission from promotion.
4. **Transitional routing envelope.** Use a bounded non-authoritative orchestration result until an accepted contract replaces it; it must never be mistaken for `PolicyDecision`.

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

These are **PROPOSED orchestration states**, not current canonical contract enums.

| Route | Meaning | Allowed destination | Not equivalent to |
|---|---|---|---|
| `ADMIT_TO_RAW` | Required pre-RAW gates pass for the evaluated capture | governed RAW lane with descriptor/receipt obligations | evidence truth, promotion, or release |
| `QUARANTINE` | Material may be retained only in a governed restricted hold pending review/remediation | `data/quarantine/` with structured reason and review route | denial, publication, or promotion |
| `DENY_INTAKE` | Material must not be admitted for the evaluated operation | no admitted lifecycle entry; retain only minimum lawful/auditable metadata | source deletion policy or global ban |
| `ERROR` | Evaluator, integrity, schema, dependency, or process failure prevents a trustworthy route | safe failure path; normally no admitted RAW use | abstention due only to weak evidence |
| `HOLD` | Review or external decision is required before a route can be chosen | pending decision outside normal public paths | silent retry or implied allow |

### Route invariants

- `ADMIT_TO_RAW` requires a resolvable source posture and required receipts.
- `QUARANTINE` requires a structured case/reason/reviewer route.
- `DENY_INTAKE` requires safe reason codes and minimum audit metadata.
- `ERROR` must not create partial admitted state.
- `HOLD` must have owner, expiry, and escalation.
- No route can write directly to PROCESSED, CATALOG, TRIPLET, PUBLISHED, release manifests, or public APIs.
- A route is operation-specific and time-bounded.
- Re-evaluation creates a new decision rather than mutating the old one.

[Back to top](#top)

---

## Normalized policy outcomes

Individual policy-family checks still use the canonical runtime outcomes:

| Outcome | Intake meaning |
|---|---|
| `ANSWER` | The evaluated family permits its portion of the intake operation, subject to obligations |
| `ABSTAIN` | Admissible context is insufficient or unresolved; normally route to hold/quarantine or deny |
| `DENY` | The evaluated family blocks the intake operation |
| `ERROR` | The input, evaluator, integrity, dependency, or process failed |

### Composition rules

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

The following codes are **PROPOSED** until a reviewed contract/schema registry establishes them.

### Input and evaluation

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
- `INTAKE_ACTIVATION_DECISION_MISSING`

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
- New codes require compatibility review.
- A reason code never substitutes for the contributing evidence or decision record.

[Back to top](#top)

---

## Obligation vocabulary

The following obligations are **PROPOSED**.

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

Repository doctrine names `SourceActivationDecision`, but the inspected evidence does not establish an accepted contract, schema, fixture family, validator, storage home, evaluator, or consumer.

Until those exist:

- do not emit invented activation records;
- do not serialize unversioned ad hoc decision shapes;
- do not treat connector enablement as activation evidence;
- do not treat descriptor presence as activation;
- record the gap as `NEEDS VERIFICATION`;
- use steward-reviewed temporary holds only through an accepted governance process.

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

| Layer | What it should prove | What it cannot prove alone |
|---|---|---|
| Markdown validation | README structure, links, anchors, metadata | Policy correctness or runtime enforcement |
| Contract/schema validation | Input and decision shape | Correct source authority or policy outcome |
| Native policy tests | Rule behavior for synthetic cases | Connector, registry, or release integration |
| Connector contract tests | Connector honors destinations and gate results | Rights or sensitivity truth |
| Registry tests | Descriptor resolution, supersession, role preservation | Admission or publication approval |
| Quarantine tests | Structured case creation and no public path | Later release safety |
| Integration tests | End-to-end routing and obligations | Production health unless observed |
| Runtime evidence | Deployed evaluation and enforcement | Historical correctness without receipts |
| Release drills | No intake bypass into public output | Source truth or evidence sufficiency |

### Minimum synthetic test matrix

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

1. accepted placement/precedence decision;
2. accepted decision-contract strategy;
3. complete `PolicyInputBundle` intake profile;
4. accepted SourceActivationDecision or equivalent;
5. accepted SourceIntakeRecord or equivalent;
6. source descriptor/schema convergence;
7. immutable bundle manifest and selector;
8. pinned evaluator and no-network native tests;
9. connector enforcement and destination tests;
10. source registry activation/supersession tests;
11. quarantine case schema and structured exit integration;
12. receipt/audit schema with minimization review;
13. governed consumer obligation enforcement;
14. correction, re-admission, expiry, revocation, and rollback drills;
15. required CI checks and branch protection;
16. accountable owners and separation of duties.

[Back to top](#top)

---

## Smallest sound implementation sequence

1. Accept or revise ADR-0017 responsibility boundaries.
2. Decide whether `policy/intake/` is canonical, transitional, or a routing index.
3. Reconcile `policy/intake/` with `policy/source/`, `policy/rights/`, and `policy/sensitivity/`.
4. Decide the admission-decision contract strategy without misusing promotion.
5. Define `SourceActivationDecision` semantics and machine shape if retained.
6. Define `SourceIntakeRecord` semantics and machine shape if retained.
7. Harden `PolicyInputBundle` with explicit intake context.
8. Define stable reason codes and obligations.
9. Add synthetic intake fixtures and native policy tests.
10. Bind source registry resolution and descriptor supersession checks.
11. Bind connector destinations and no-bypass enforcement.
12. Implement structured quarantine-case creation.
13. Add receipt/audit emission with data minimization.
14. Bind governed API/review-console consumers.
15. Run correction, re-admission, deactivation, cache invalidation, and rollback drills.
16. Activate only through an immutable reviewed bundle and rollback target.

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

This README can be reverted to the prior empty blob without changing runtime behavior because it activates none.

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
| `INTAKE-POL-001` | Is `policy/intake/` canonical, transitional, or only a routing index? | **NEEDS VERIFICATION** | accepted ADR or policy-root decision |
| `INTAKE-POL-002` | How does it compose with `policy/source/`, `policy/rights/`, and `policy/sensitivity/`? | **NEEDS VERIFICATION** | bundle contract and native tests |
| `INTAKE-POL-003` | Is source admission the only scope, or are other material-intake classes included? | **NEEDS VERIFICATION** | accepted scope statement and fixtures |
| `INTAKE-POL-004` | Which decision contract represents overall admission? | **UNKNOWN** | accepted semantic contract and schema |
| `INTAKE-POL-005` | Does `SourceActivationDecision` remain the canonical object name? | **NEEDS VERIFICATION** | contract review and ADR update |
| `INTAKE-POL-006` | Does `SourceIntakeRecord` remain the canonical event/object name? | **NEEDS VERIFICATION** | contract/schema and event-family review |
| `INTAKE-POL-007` | Which SourceDescriptor schema path is canonical? | **CONFLICTED** | ADR/schema migration and compatibility tests |
| `INTAKE-POL-008` | Which intake fields become required in PolicyInputBundle? | **NEEDS VERIFICATION** | accepted schema and fixtures |
| `INTAKE-POL-009` | Which policy family or composition strategy is accepted? | **UNKNOWN** | contract/schema/runtime migration |
| `INTAKE-POL-010` | Which routing states are canonical? | **PROPOSED** | accepted orchestration contract |
| `INTAKE-POL-011` | Which reason codes and obligations are canonical? | **PROPOSED** | registry/schema and consumer tests |
| `INTAKE-POL-012` | Which evaluator, bundle, selector, and entrypoint are accepted? | **UNKNOWN** | pinned runtime and native test run |
| `INTAKE-POL-013` | Which connectors enforce admission before RAW writes? | **UNKNOWN** | connector inventory and contract tests |
| `INTAKE-POL-014` | Which local-upload surfaces are deployed? | **UNKNOWN** | application/runtime evidence |
| `INTAKE-POL-015` | Which content/security scanner profiles are approved? | **UNKNOWN** | security architecture and observed tests |
| `INTAKE-POL-016` | Is the source authority register populated and consumed? | **UNKNOWN** | register entries and consumer evidence |
| `INTAKE-POL-017` | Which quarantine-record contract/schema is accepted? | **UNKNOWN** | accepted contract, schema, fixtures, validator |
| `INTAKE-POL-018` | Which receipt/audit sink records admission safely? | **UNKNOWN** | threat-reviewed contract and tests |
| `INTAKE-POL-019` | Which governed applications enforce obligations? | **UNKNOWN** | implementation and integration tests |
| `INTAKE-POL-020` | How are retries, holds, expiry, and escalation governed? | **UNKNOWN** | operational contract and drills |
| `INTAKE-POL-021` | How are source changes detected and re-admission triggered? | **NEEDS VERIFICATION** | source-head/cadence tests and runbook |
| `INTAKE-POL-022` | How are cached decisions invalidated on rights/sensitivity changes? | **UNKNOWN** | dependency graph and invalidation drill |
| `INTAKE-POL-023` | Which CI checks are required and branch-protected? | **UNKNOWN** | workflow runs and ruleset evidence |
| `INTAKE-POL-024` | Who owns intake, source, rights, sensitivity, security, registry, connector, quarantine, and release review? | **NEEDS VERIFICATION** | accepted stewardship and separation-of-duties record |
| `INTAKE-POL-025` | Has an end-to-end admit/quarantine/deny/re-admit/rollback drill succeeded? | **UNKNOWN** | signed drill report and verified artifact state |
| `INTAKE-POL-026` | Are public fixtures/logs free of secrets and protected payloads? | **NEEDS VERIFICATION** | secret scan, fixture review, and log tests |
| `INTAKE-POL-027` | Has `docs/intake/` versus source/material intake terminology been formally reconciled? | **NEEDS VERIFICATION** | glossary/ADR/documentation review |
| `INTAKE-POL-028` | Are promotion and admission decisions prevented from collapsing in code and schemas? | **UNKNOWN** | contract tests and static/runtime guards |

[Back to top](#top)

---

## Last reviewed

**2026-07-24 — initial repository-grounded completion of the previously empty README.**

This review confirms the documented repository surfaces and current maturity boundary. It does not accept this lane, activate an intake bundle, approve a source, enable a connector, admit a file, create a registry entry, clear rights or sensitivity, open or close a quarantine case, promote material, approve release, or create publication state.

---

## Maintainer checklist

Before adding executable intake policy or child lanes:

- [ ] resolve lane placement and relationship to `policy/source/`;
- [ ] preserve the separation between source/material intake and `docs/intake/`;
- [ ] decide the admission-decision contract and policy-family strategy;
- [ ] converge SourceDescriptor schema authority;
- [ ] define SourceActivationDecision and SourceIntakeRecord only through contracts/schemas;
- [ ] harden PolicyInputBundle with explicit non-secret intake context;
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
