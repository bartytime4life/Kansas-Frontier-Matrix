# policy :: rights

> **One-line purpose.** `policy/rights/` is KFM's policy-source boundary for deciding whether a specifically requested use is admissible under already established rights, terms, attribution, redistribution, consent, stewardship, sovereignty, and related obligations—without creating those rights, interpreting law, accepting evidence, clearing sensitivity, approving release, or publishing anything.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/policy-rights-readme
title: policy/rights/ — Rights Admissibility Policy Boundary
type: readme
version: v0.1.0
status: draft; repository-grounded; placeholder-corpus; inactive; fail-closed-authoring-contract; non-legal; non-release; non-publication
owner: NEEDS VERIFICATION — CODEOWNERS routes /policy/ to @bartytime4life; an accepted rights steward and independent approver were not established
created: 2026-05-05
updated: 2026-08-13
current_path: policy/rights/README.md
owning_root: policy/
policy_label: internal; policy; rights; terms; attribution; redistribution; consent-aware; sensitivity-aware; non-release; non-publication
responsibility: Define the rights-admissibility policy-source boundary, current child inventory, input and outcome expectations, trust limits, validation posture, and correction triggers without becoming semantic, schema, registry, evidence, legal, runtime, release, or publication authority.
base_commit: f50e407026cef632f4d3f314b51884b29dfd9a45
prior_blob: 5dffc3a0ca80d8d94a8008e6c60b2f9489d5f077
directory_governance: ADR-0029 accepted Directory Rules v2 for placement; this README does not accept or activate a rights policy profile
truth_posture: CONFIRMED adopted policy placement, complete tracked child inventory, two default-only local Rego stubs, six domain terms scaffolds, three placeholder subtrees, 173 repository policy Rego files with one separately governed native test, fixture-only source-rights currentness assessment, and absent local package consumers / PROPOSED fail-closed rights authoring and evaluation contract / NEEDS VERIFICATION steward ownership, accepted RightsDecision semantics, registry schema, bundle, evaluator, normalization, obligation enforcement, review authentication, correction propagation, and required-check coupling / UNKNOWN production and public-surface enforcement
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#status)
[![Maturity: placeholder](https://img.shields.io/badge/maturity-M0%20placeholder-d97706?style=flat-square)](#current-maturity)
[![Local rules: inactive](https://img.shields.io/badge/local%20rules-inactive-b42318?style=flat-square)](#current-rule-inventory)
[![Default posture: fail closed](https://img.shields.io/badge/authoring%20posture-fail%20closed-2da44e?style=flat-square)](#default-deny-hold-and-abstain-posture)
[![Legal authority: no](https://img.shields.io/badge/legal%20authority-no-b42318?style=flat-square)](#authority-level)
[![Publisher: no](https://img.shields.io/badge/publisher-no-b42318?style=flat-square)](#authority-level)

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Children](#current-direct-child-map) · [Rules](#current-rule-inventory) · [Inputs](#candidate-inputs) · [Outcomes](#candidate-outcomes) · [Trust boundary](#rights-trust-boundary) · [Lifecycle](#lifecycle-and-public-trust-membrane) · [Validation](#validation) · [Review](#review-burden) · [Related](#related-surfaces) · [Rollback](#correction-revocation-and-rollback) · [Open work](#open-verification-register)

> [!IMPORTANT]
> **Safe current conclusion at `main@f50e407026ce`:** this lane contains policy-shaped placeholders, not an accepted rights evaluator. `attribution_required.rego` and `license_compatibility.rego` each declare `default deny := false`, expose no live decision rule beyond that default, have no native tests in this lane, and have no repository package consumer found by package-name search. The Fauna and Flora files are explicitly `PROPOSED` scaffolds, while correction, release, and sensitivity subtrees contain only placeholders. Do not use this directory as evidence that a source, dataset, derivative, claim, map, export, or AI answer is licensed, attributable, redistributable, releasable, or public-safe.

> [!CAUTION]
> A README, Rego package, schema-valid descriptor, registry record, workflow, successful test, human-readable terms summary, or absence of a denial can never create a license, infer consent, waive attribution, establish a rights holder, settle conflicting terms, override cultural or Indigenous stewardship, reduce sensitivity, authenticate review, approve release, or authorize publication.

---

## Purpose

`policy/rights/` is the policy-source lane for **rights admissibility**.

Its bounded question is:

> Given a named operation, audience, governed subject, source and evidence context, reviewed rights and terms posture, attribution and redistribution obligations, consent or agreement state, stewardship and sovereignty constraints, sensitivity posture, lifecycle state, and exact policy identity, may this operation proceed—and under which enforceable obligations or holds?

Rights policy should evaluate facts and reviewed statuses supplied by their owning systems. It should never discover rights through hidden network calls, copy license text into rule source as authority, or guess what missing terms mean.

The intended distinction is simple:

- **rights evidence and reviewed state** say what is known about permission and obligations;
- **rights policy** decides whether a specific requested operation is admissible under that state;
- **runtime enforcement** applies the normalized decision at a governed interface; and
- **release authority** separately approves, corrects, withdraws, or rolls back a released artifact.

[Back to top](#top)

---

## Authority level

**Canonical child policy boundary for rights admissibility source; non-legal, non-semantic, non-schema, non-registry, non-evidence, non-runtime, non-release, and non-publication authority.**

Accepted [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) makes [Directory Rules v2](../../docs/doctrine/directory-rules.md) effective for repository placement. The [root registry](../../control_plane/root_registry.yaml) projects `policy/` as the canonical, internal, durable home for normative policy rules and explicitly denies data instances, release decisions, and schemas in that root.

| Responsibility | Owning surface | Role of `policy/rights/` |
|---|---|---|
| Source and rights meaning | [`contracts/source/source_descriptor.md`](../../contracts/source/source_descriptor.md) and accepted rights contracts | Consume reviewed meaning; do not redefine it in Rego or prose. |
| Machine-checkable shape | [`schemas/contracts/v1/source/source_descriptor.schema.json`](../../schemas/contracts/v1/source/source_descriptor.schema.json) and rights-policy schemas if accepted | Require a versioned shape; do not become schema authority. |
| Source identity and reviewed posture | source and rights registry lanes, including [`data/registry/rights/`](../../data/registry/rights/README.md) | Consume stable references and states; do not create or mutate registry truth. |
| Evidence and terms records | governed evidence, review, agreement, or external source-of-record systems | Evaluate explicit references; do not invent, paraphrase, or authenticate them. |
| Rights admissibility rules | `policy/rights/` | Own reviewed, versioned rule source and local boundary documentation. |
| Sensitivity and consent | [`policy/sensitivity/`](../sensitivity/README.md) and consent policy | Compose independent decisions; never treat one clearance as the other. |
| Evaluation and normalization | an accepted evaluator, potentially under [`packages/policy-runtime/`](../../packages/policy-runtime/README.md) | Supply exact accepted source or bundle identity; do not execute itself. |
| Fixtures, tests, and validators | [`fixtures/`](../../fixtures/README.md), [`tests/`](../../tests/README.md), and [`tools/validators/`](../../tools/validators/README.md) | Provide evidence about bounded behavior; passing does not grant rights. |
| Decisions and process memory | accepted decision, review, receipt, and proof lanes | Provide evaluated results for recording; do not store instances here. |
| Release, correction, withdrawal, rollback | [`release/`](../../release/README.md) | Supply one gate result; never approve or publish. |
| Public enforcement | governed APIs and released public-safe artifacts | Consume normalized decisions; never load repository policy source directly. |

`CODEOWNERS` currently routes `/policy/` review to `@bartytime4life`. That is a GitHub routing fact, not proof of a verified rights steward, legal reviewer, independent approver, completed review, branch protection, or separation of duties.

[Back to top](#top)

---

## Status

| Surface | Evidence at `f50e407026ce` | Safe status |
|---|---|---:|
| This README | 44-byte greenfield stub before this revision | **CONFIRMED placeholder baseline** |
| Rights lane placement | Child of the adopted singular `policy/` root | **CONFIRMED placement; no activation implied** |
| `attribution_required.rego` | `package kfm.attribution_required`; `default deny := false`; example rule commented out | **PROPOSED / inactive / default-only** |
| `license_compatibility.rego` | `package kfm.license_compatibility`; `default deny := false`; example rule commented out | **PROPOSED / inactive / default-only** |
| Package consumers | Exact package-name searches returned only the defining files | **NONE FOUND in reviewed repository search** |
| Native tests in this lane | No `*_test.rego`, `tests/`, or executable local test payload | **NOT ESTABLISHED** |
| Fauna terms files | Two YAML placeholders sourced from a missing/planned-files inventory | **PROPOSED scaffolds** |
| Flora terms files | Four Markdown placeholders sourced from `CANONICAL_PATHS.md` | **PROPOSED scaffolds; not terms authority** |
| Correction and release lanes | `correction/` and `release/` contain only `.gitkeep` | **PLACEHOLDER ONLY** |
| Sensitivity crossover lanes | `sensitivity/release-state/` and `sensitivity/release/` contain only `.gitkeep` | **PLACEHOLDER ONLY** |
| Repository Rego corpus | 173 policy Rego files; one separately governed native test at `policy/rego/release_gate_v1_test.rego` | **CONFIRMED mixed maturity** |
| Broad `policy-test` workflow | Static readiness holds and one bounded release-gate wiring check; explicitly evaluates no general policy | **CONFIRMED non-evaluator guard** |
| `policy-boundary-guards` | 18 structural/static/API tests; explicitly not rights or sensitivity decision proof | **CONFIRMED bounded guard** |
| Source-rights currentness profile | Proposed contract, schema, fixtures, deterministic validator, tests, and dedicated workflow | **CONFIRMED fixture-only adjacent control** |
| SourceDescriptor rights shape | Proposed contract/schema require a structured rights object and controlled states | **CONFIRMED proposed shape; not rights approval** |
| Rights registry | Parent and Flora README surfaces exist; canonical record schema, emitted records, and runtime resolver remain unverified | **PARTIAL documentation / implementation unknown** |
| Rights validator lane | Documentation exists; it explicitly does not confirm executable rights validators or CI wiring | **DOCUMENTED BOUNDARY / execution unverified** |
| Accepted rights bundle, selector, evaluator, decision normalization, obligation enforcement, and production consumer | No complete flow established in reviewed evidence | **UNKNOWN / NEEDS VERIFICATION** |
| Required checks and independent approval | Workflow presence and CODEOWNERS do not establish them | **UNKNOWN / NEEDS VERIFICATION** |

### Truth labels used here

- **CONFIRMED** means verified from exact repository bytes or current remote state during this update.
- **PROPOSED** means a candidate design, scaffold, or future contract that is not accepted operational behavior.
- **NEEDS VERIFICATION** means the question is answerable but the reviewed evidence does not support acting on it.
- **UNKNOWN** means the implementation or authority state was not established; callers must not infer a permissive answer.

[Back to top](#top)

---

## What belongs here

- this README and local policy-family documentation;
- reviewed, versioned, declarative rules for operation-specific rights admissibility;
- rules that distinguish license or terms identity, attribution, redistribution, derivative use, commercial use, embargo, expiration, jurisdiction, consent, agreement, stewardship, sovereignty, and culturally governed obligations;
- fail-closed handling for missing, unknown, stale, expired, revoked, denied, incompatible, contested, or unreviewed rights state;
- explicit package names, entrypoints, policy versions, reason codes, obligations, effective times, and supersession notes;
- source- or domain-specific rule modules when their primary responsibility is rights admissibility and their ownership is explicit;
- public-safe native test cases only when an accepted local test-placement profile permits co-location;
- links to paired contracts, schemas, registries, synthetic fixtures, executable tests, validators, decision records, receipts, proofs, consumers, release gates, corrections, withdrawals, and rollback targets.

A file belongs here because it **decides admissibility under supplied rights context**. Merely mentioning a license, terms URL, attribution, access, consent, or release does not make a file rights policy.

[Back to top](#top)

---

## What does not belong here

| Do not place this in `policy/rights/` | Correct responsibility or handling |
|---|---|
| Legal advice, legal conclusions, negotiated agreements, or declarations of ownership | Authorized legal, rights-holder, or steward systems outside this policy-source lane |
| Full license or terms text treated as authoritative | Provider/source-of-record evidence with an immutable reviewed reference; policy consumes the reference and normalized state |
| Source identity, publisher facts, rights-holder identity, or registry instances | source and rights registry lanes |
| Semantic definitions of SourceDescriptor, PolicyDecision, or a future rights-decision object | `contracts/` |
| JSON Schema, enums, DTOs, or field shape | `schemas/contracts/v1/` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED data | the governed `data/` lifecycle |
| EvidenceBundles, proof packs, citations, screenshots, private agreements, or review evidence | their evidence/proof/review systems |
| Evaluated decision instances, validation reports, or run receipts | accepted decision, report, and receipt lanes |
| Evaluator, adapter, API, CLI, application, cache, or storage implementation | `packages/`, `runtime/`, `apps/`, or `tools/` by responsibility |
| Reusable synthetic fixtures or executable conformance tests | root `fixtures/` and `tests/`, unless an accepted engine-native profile says otherwise |
| ReleaseManifest, PromotionDecision, CorrectionNotice, WithdrawalNotice, or RollbackCard | `release/` |
| Public attribution rendering, exports, maps, UI, search, graph, or AI answers | governed application and released public-artifact surfaces |
| Credentials, access tokens, paywalled content, private correspondence, living-person data, genomic material, exact sensitive locations, or protected cultural knowledge | keep out of Git, logs, examples, reasons, and receipts; use authorized restricted systems |
| A second independently evolving policy root or duplicated domain truth | preserve the adopted root and resolve placement through reviewed governance |

Existing scaffolds do not authorize new rights claims. Replace or migrate a scaffold only through a bounded change that identifies the source of authority, affected consumers, validation, correction, and rollback.

[Back to top](#top)

---

## Current direct-child map

Directory Rules requires a full README to map direct children. This is the complete tracked inventory at the pinned base; nested files are shown only where needed to explain a placeholder subtree.

```text
policy/rights/
├── README.md
├── attribution_required.rego
├── correction/
│   └── .gitkeep
├── fauna/
│   ├── ebd_terms.yaml
│   └── source_terms.yaml
├── flora/
│   ├── gbif_license.md
│   ├── inaturalist_usage.md
│   ├── knhi_access.md
│   └── natureserve_explorer_pro.md
├── license_compatibility.rego
├── release/
│   └── .gitkeep
└── sensitivity/
    ├── release-state/
    │   └── .gitkeep
    └── release/
        └── .gitkeep
```

| Direct child | Current contents | Boundary and maturity |
|---|---|---|
| [`attribution_required.rego`](./attribution_required.rego) | Default-only Rego package plus a commented example | Not an attribution decision contract, test, or active gate. |
| [`correction/`](./correction/) | `.gitkeep` only | Reserves no correction authority; correction records belong under their accepted process and release lanes. |
| [`fauna/`](./fauna/) | Two short `PROPOSED` inventory-derived YAML placeholders | Records no verified terms, license, owner, review date, policy, or decision. |
| [`flora/`](./flora/) | Four `PROPOSED` Markdown scaffolds | Their titles are source-family hints, not authoritative license or access determinations. |
| [`license_compatibility.rego`](./license_compatibility.rego) | Default-only Rego package plus a commented example | Defines no compatibility matrix, input contract, reason vocabulary, or accepted outcome. |
| [`release/`](./release/) | `.gitkeep` only | Creates no release gate, decision, manifest, approval, correction, or rollback. |
| [`sensitivity/`](./sensitivity/) | Two nested placeholder lanes | Creates no combined rights/sensitivity decision or public-exposure authorization. |

The repository also contains rights-related policy scaffolds under [`../domains/`](../domains/) and [`../sources/rights/`](../sources/rights/). They remain separate policy-family placements and are not imported, selected, or activated by this directory.

[Back to top](#top)

---

## Current rule inventory

### Local Rego packages

| File | Package | Live exported posture | Current limitation |
|---|---|---|---|
| [`attribution_required.rego`](./attribution_required.rego) | `kfm.attribution_required` | `default deny := false` | The only candidate denial rule is commented out. No accepted input or output contract exists. |
| [`license_compatibility.rego`](./license_compatibility.rego) | `kfm.license_compatibility` | `default deny := false` | The only candidate denial rule is commented out. No compatibility vocabulary or matrix exists. |

`deny = false` is not a grant of rights. It is merely the current value of a placeholder Rego document. A consumer must not coerce absence of a denial, an undefined rule, an empty set, `false`, an evaluator error, or a missing package into `ALLOW`.

The commented `deny[reason]` examples are not executable interfaces. Their names, input fields, collection shape, and reason string are unaccepted examples and must not be treated as stable contracts.

### Adjacent rights-related Rego

The repository has additional generated rights-named stubs for archaeology, Flora, geology, roads/rail/trade, Mesonet, and NASA. Each reviewed adjacent file contains a `PROPOSED scaffold` comment and a default-only posture. File presence does not create a shared bundle, import graph, compatibility matrix, source admission rule, or runtime selection mechanism.

### Consumer search

Repository code search for `kfm.attribution_required` and `kfm.license_compatibility` returned only their defining files. This supports the bounded conclusion that no package-name consumer was found; it does not prove that an external system never reads the files.

[Back to top](#top)

---

## Rights trust boundary

Rights, access, sensitivity, consent, and release are related but non-substitutable controls.

| Question | Rights policy may evaluate | Rights policy must not assert |
|---|---|---|
| Is a license or terms posture known and reviewed? | Supplied normalized status, version, effective time, and evidence reference | That a URL, filename, SPDX-like token, or prose summary is legally valid |
| Is attribution required? | Reviewed obligation flag and template/reference presence | The correct legal wording or that UI rendered it |
| Is redistribution allowed? | Operation-specific reviewed state and conditions | That access implies redistribution or that transformation removes restrictions |
| Are derivative works allowed? | Reviewed permission for the requested transform | That aggregation, redaction, summarization, or AI generation automatically creates new rights |
| Does consent or an agreement apply? | Supplied applicability, scope, status, expiry, and revocation reference | Consent from silence, access, prior publication, or model inference |
| Do stewardship or sovereignty constraints apply? | Explicit reviewed obligations and decision references | Authority to waive or reinterpret community, cultural, Tribal, Indigenous, or institutional control |
| Is the content public-safe? | Require a separate sensitivity decision and necessary transforms | That rights clearance lowers sensitivity or that redaction clears rights |
| May release proceed? | Return a bounded rights result and obligations | Release approval, publication state, or public truth |

### Rights are not access

The ability to fetch, view, scrape, download, query, or authenticate to a source is not evidence of permission to ingest, transform, redistribute, publish, train on, or generate derivatives from it.

### Rights are not sensitivity

Openly licensed material may still be sensitive. Restricted material may become less sensitive after transformation without becoming redistributable. Both controls must close independently, and the stricter applicable obligation survives.

### Rights are not evidence

A rights-compatible source can still be inaccurate, stale, unsupported, or inappropriate for a claim. Evidence sufficiency and rights admissibility are separate gates.

### Rights are not release

An admissible result is one input to a release decision. It does not prove validation, evidence closure, review completion, catalog closure, correction readiness, or rollback safety.

[Back to top](#top)

---

## Candidate inputs

The current local rules do not define an accepted input contract. A future accepted rights evaluator should receive an explicit, normalized, versioned input assembled outside this directory. Candidate fields include:

| Input family | Candidate context | Fail-closed trigger |
|---|---|---|
| Requested action | operation, purpose, audience, delivery surface, requested precision, transform, export, or model use | missing or unsupported operation |
| Governed subject | stable source, dataset, object, derivative, claim, layer, release-candidate, or artifact reference | raw payload substituted for a stable governed identity |
| Source posture | SourceDescriptor reference, descriptor version/digest, source role, publisher, owner/steward, source-head/currentness reference | absent, stale, conflicted, superseded, or unreviewed descriptor |
| License or terms | reviewed identifier/reference, terms version, effective time, jurisdiction, review state, expiry, revocation | unknown, noassertion, denied, expired, stale, permission-dependent, or contradictory state |
| Attribution | required flag, exact reviewed template/reference, placement obligations, derivative propagation rule | required attribution cannot be satisfied or verified |
| Redistribution and derivatives | redistribution, derivative-use, commercial-use, sublicensing, share-alike, and downstream-carrier conditions | requested use exceeds reviewed permission or conditions are unenforceable |
| Consent and agreement | applicability, scope, subject/steward reference, status, expiry, revocation, agreement reference | missing, withdrawn, expired, scope mismatch, or unauthenticated authority |
| Stewardship and sovereignty | controlling authority reference, CARE/cultural obligations, restricted-purpose conditions, review state | unresolved authority or unmet steward obligation |
| Sensitivity | separate classification/decision reference, requested transform, residual-risk state | missing independent clearance or unsafe residual exposure |
| Evidence and review | evidence/proof references, reviewer role and state, review time, contradiction status | untrusted, incomplete, stale, self-approved, or unresolved review |
| Lifecycle and release | current/requested lifecycle state, prior releases, correction/withdrawal state, release candidate | skipped transition, withdrawn predecessor, or unresolved correction |
| Evaluation identity | policy/bundle ID, version, digest, entrypoint, evaluator version, evaluation time, input hash | unaccepted, mutable, unpinned, or non-replayable context |

These are authoring requirements, not claims that the current Rego files consume these fields.

Inputs should use stable references and normalized public-safe statuses. Private agreements, protected values, exact sensitive locations, credentials, and raw source payloads must not be copied into Rego input logs, denial reasons, receipts, or documentation.

[Back to top](#top)

---

## Candidate outcomes

The two local Rego stubs expose no accepted outcome contract. A mature rights policy should distinguish at least the following concepts without lossy coercion:

| Candidate outcome | Meaning | Typical next step |
|---|---|---|
| `ALLOW` | The requested operation is admissible under the supplied reviewed rights context and all returned obligations are enforceable. | Continue to independent evidence, sensitivity, review, and release gates. |
| `ALLOW_WITH_OBLIGATIONS` or `RESTRICT` | The operation is admissible only if named attribution, access, redistribution, transform, audience, retention, or downstream-propagation duties are enforced. | Bind and verify every obligation or hold. |
| `HOLD` | Context may be resolvable, but review, permission, currentness, contradiction, or obligation closure is incomplete. | Route to authorized review; do not proceed publicly. |
| `DENY` | The requested operation conflicts with established rights, terms, consent, agreement, stewardship, or sovereignty constraints. | Stop the operation and preserve a public-safe reason code. |
| `ABSTAIN` | The evaluator lacks a supported rule, sufficient trusted context, or authority to decide. | Fail closed and escalate; never convert to allow. |
| `ERROR` | Evaluation could not complete reliably. | Fail closed, record bounded operational evidence, and repair or roll back. |

A normalized decision should carry stable reason codes, obligations, policy and evaluator identity, input hash, evaluation time, expiry or recheck conditions, and references to the reviewed source state. Detailed protected reasons may require a restricted review channel; public-facing reason codes must not reveal the fact being protected.

An output is not self-authenticating. The repository's proposed [`PolicyDecision`](../../contracts/policy/policy_decision.md) surfaces and vocabularies remain separate candidate contracts. No accepted `RightsDecision` file or rights-specific normalization contract was found in the reviewed tree.

[Back to top](#top)

---

## Default-deny, hold, and abstain posture

The safe authoring posture is fail closed:

- missing, unknown, `NOASSERTION`, stale, expired, revoked, denied, permission-required, conflicting, or unreviewed rights must not become public permission;
- evaluator errors, undefined packages, absent rules, empty results, type mismatches, and normalization failures must not become `ALLOW`;
- inability to meet or verify an obligation must hold or deny the operation;
- a less restrictive downstream derivative must not silently erase upstream obligations;
- rights changes must propagate to derivatives, caches, catalogs, released carriers, citations, and AI outputs through governed correction or withdrawal flows;
- the stricter applicable rights, consent, stewardship, sovereignty, sensitivity, and release constraint governs until conflicts are resolved.

This posture is an authoring and integration requirement. It is **not** a claim that the current `default deny := false` stubs enforce it.

[Back to top](#top)

---

## Lifecycle and public trust membrane

| Stage | Required rights posture | What this directory cannot do |
|---|---|---|
| Candidate and pre-admission | Resolve source identity, terms, permission, attribution, access, currentness, and review ownership before governed admission. | Fetch a source, create a descriptor, accept legal terms, or admit bytes. |
| RAW / WORK / QUARANTINE | Preserve the exact rights posture and route unresolved state to hold or quarantine. | Move data, upgrade source role, or declare quarantine resolved. |
| Transform and derivation | Re-evaluate derivative, attribution, share-alike, redistribution, consent, and stewardship obligations for the named transform. | Assume transformation creates permission or erases lineage. |
| Catalog and release candidate | Bind current source/right references, obligations, sensitivity result, evidence, review, correction path, and rollback path. | Close the catalog, authenticate review, or approve release. |
| PUBLISHED and public interfaces | Enforce only through governed server-side interfaces and released public-safe carriers; propagate required attribution and conditions. | Rely on client-side hiding, repository source, or an AI explanation as enforcement. |
| Correction, revocation, withdrawal | Hold affected uses, identify downstream dependents, append accountable correction or withdrawal lineage, and verify propagation. | Rewrite history, delete evidence, or declare propagation complete without proof. |

Public clients must not read `policy/rights/`, internal registries, raw agreements, or source payloads directly. They should receive only released public-safe results and bounded explanations through governed interfaces.

[Back to top](#top)

---

## Current maturity

| Level | Evidence required | Current rights-lane posture |
|---|---|---:|
| M0 — Placeholder | Stub README, default-only module, `.gitkeep`, or inventory-derived scaffold | **CONFIRMED** |
| M1 — Boundary documented | Scope, authority split, inputs, outcomes, failures, review, validation, and rollback documented | **PROPOSED by this README; pending review** |
| M2 — Executable candidate | Reviewed semantic contract and schema, synthetic fixtures, deterministic evaluator tests, stable reasons and obligations | **NOT ESTABLISHED for this lane** |
| M3 — Integrated candidate | Accepted bundle/selector/evaluator, normalization, consumer, decision records, replay, and correction tests | **NOT ESTABLISHED** |
| M4 — Governed enforcement | Required checks, authenticated independent review, production enforcement, release coupling, monitoring, revocation propagation | **UNKNOWN / not proved** |

The adjacent SourceRightsCurrentnessAssessment reaches a bounded fixture-only candidate posture for dated source review. It does not raise this directory's maturity and does not activate, fetch, admit, release, or publish a source.

[Back to top](#top)

---

## Related surfaces

| Surface | Relationship and current boundary |
|---|---|
| [`../README.md`](../README.md) | Parent policy authority, maturity vocabulary, outcome separation, and trust membrane. |
| [`../source/README.md`](../source/README.md) | Source-admissibility policy boundary; rights remains a separate input and decision concern. |
| [`../intake/README.md`](../intake/README.md) | Intake policy context; must not treat rights placeholders as admission permission. |
| [`../sensitivity/README.md`](../sensitivity/README.md) | Independent sensitivity boundary; neither decision clears the other. |
| [`../sources/rights/`](../sources/rights/) | Separate source-specific rights scaffold lane; no import or selection relationship is established. |
| [`../../contracts/source/source_descriptor.md`](../../contracts/source/source_descriptor.md) | Proposed semantic source object with required rights, sensitivity, access, review, and release posture. |
| [`../../schemas/contracts/v1/source/source_descriptor.schema.json`](../../schemas/contracts/v1/source/source_descriptor.schema.json) | Proposed machine shape for SourceDescriptor rights state; schema validity is not permission. |
| [`../../contracts/source/source_rights_currentness_assessment.md`](../../contracts/source/source_rights_currentness_assessment.md) | Proposed fixture-only dated rights/currentness assessment. |
| [`../../fixtures/contracts/v1/source/source_rights_currentness_assessment/cases.json`](../../fixtures/contracts/v1/source/source_rights_currentness_assessment/cases.json) | Synthetic assessment cases; not live source or rights evidence. |
| [`../../tools/validators/source/validate_source_rights_currentness_assessment.py`](../../tools/validators/source/validate_source_rights_currentness_assessment.py) | Deterministic fixture validator; not a rights policy evaluator. |
| [`../../data/registry/rights/README.md`](../../data/registry/rights/README.md) | Candidate rights-state registry boundary; not policy, evidence, legal advice, or release. |
| [`../../tools/validators/rights/README.md`](../../tools/validators/rights/README.md) | Rights-validator routing contract; executable rights validation remains unconfirmed there. |
| [`../../docs/sources/RIGHTS_GUIDANCE.md`](../../docs/sources/RIGHTS_GUIDANCE.md) | Draft human guidance with explicitly proposed fields and stale “no mounted repo” caveats; consult as context, not current implementation authority. |
| [`../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md`](../../docs/sources/SOURCE_DESCRIPTOR_STANDARD.md) | Draft source-descriptor guidance; repository contracts and schemas control observed implementation claims. |
| [`../../contracts/policy/policy_decision.md`](../../contracts/policy/policy_decision.md) | Proposed general decision semantics; no accepted rights-specific binding was found. |
| [`../../packages/policy-runtime/README.md`](../../packages/policy-runtime/README.md) | General evaluator boundary; current package remains a placeholder under the parent policy evidence review. |
| [`../../release/README.md`](../../release/README.md) | Separate release, correction, withdrawal, and rollback authority. |

### ADRs and governance

| Decision or control | Status | Relevance |
|---|---:|---|
| [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | **ACCEPTED** | Establishes Directory Rules placement and the singular policy root. |
| [Directory Rules v2](../../docs/doctrine/directory-rules.md) | **ADOPTED through ADR-0029** | Governs responsibility placement, README expectations, and non-duplication. |
| [`control_plane/root_registry.yaml`](../../control_plane/root_registry.yaml) | **Machine projection only** | Projects `policy/` as internal normative policy source; creates no rights authority. |
| [CODEOWNERS](../../.github/CODEOWNERS) | **Review routing** | Routes `/policy/`; does not prove rights expertise or completed independent review. |
| [Pull-request template](../../.github/PULL_REQUEST_TEMPLATE.md) | **Work-intake control** | Requires scope, evidence, risk, validation, rollback, and generated-work provenance. |

No reviewed evidence established an accepted ADR that activates these rights rules, a rights bundle, a rights-decision object, or a public enforcement path.

[Back to top](#top)

---

## Validation

### What current repository checks cover

| Check | Actual coverage | Explicit limitation |
|---|---|---|
| [`policy-test`](../../.github/workflows/policy-test.yml) | Confirms policy inventory, the sole separately governed native Rego test lane, placeholder runtime posture, fixture shape, and general readiness holds. | It evaluates no repository-wide policy and does not execute `policy/rights/`. |
| [`policy-boundary-guards`](../../.github/workflows/policy-boundary-guards.yml) | Runs 18 structural/static/API tests across four named modules. | It explicitly does not prove rights or sensitivity decisions, evidence closure, or release approval. |
| [`source-rights-currentness-assessment`](../../.github/workflows/source-rights-currentness-assessment.yml) | Runs deterministic synthetic source-rights/currentness validation and its generated-receipt check. | It is fixture-only and does not activate a source, approve rights, fetch bytes, admit RAW data, release, or publish. |
| `make policy` | Prints `TODO: opa test policy/ -v` at the pinned base. | A successful echo is not OPA execution or policy validation. |
| `make validate` | Broad repository schema/contract baseline when its environment is available. | It is not a rights evaluator and cannot authenticate evidence, terms, review, or legal authority. |

### Minimum validation for a future rule change

A material rights-rule change should include, in the same dependency-closed review slice:

1. an accepted or explicitly proposed semantic input/output contract and paired schema;
2. exact package, entrypoint, version, bundle, evaluator, and normalization identities;
3. synthetic public-safe positive, negative, unknown, stale, conflicting, expired, revoked, obligation-failure, and evaluator-error cases;
4. native Rego tests or an accepted equivalent that execute the actual rule package;
5. stable public-safe reason codes and machine-enforceable obligations;
6. tests proving undefined, empty, `false`, error, or type-mismatched results cannot become allow;
7. consumer and governed-interface integration tests;
8. correction, revocation, withdrawal, cache-invalidation, and rollback tests;
9. a dedicated workflow with pinned dependencies, bounded permissions, deterministic commands, and explicit non-effects; and
10. generated-work provenance plus authorized rights, policy, domain, privacy/security, and release review.

For this README-only update, relevant validation is Markdown structure, direct-child reconciliation, local link and fragment resolution, receipt schema and hash integrity, sensitive-content review, remote changed-path verification, and exact-head hosted check reporting.

[Back to top](#top)

---

## Review burden

| Change class | Minimum review posture |
|---|---|
| README-only clarification | Policy-aware maintainer plus documentation review; verify no prose creates legal or operational authority. |
| Terms or source-profile scaffold | Source owner, rights steward, affected domain steward, and evidence reviewer; cite the external source of record without copying restricted terms. |
| Rights rule or native test | Rights steward, policy steward, affected domain/source owner, and validation reviewer. |
| License compatibility, consent, sovereignty, cultural or Indigenous stewardship | Authorized specialist and affected steward plus policy, privacy/security, and release review; fail closed without ownership. |
| Bundle, selector, evaluator, normalization, or consumer binding | Policy runtime, contracts, schemas, security/supply-chain, application, validation, and release review. |
| Public exposure, export, AI use, or redistribution behavior | Rights, sensitivity/privacy, affected domain, API/UI, evidence, and release review. |
| Correction, revocation, withdrawal, or rollback | Rights and release authority plus every affected owner; preserve prior decisions and dependency lineage. |

Reviewers should verify source authority, effective terms version, requested operation, audience, downstream obligations, sensitive-data posture, independent clearance of sensitivity and consent, fail-closed behavior, consumer enforcement, correction propagation, and rollback. A GitHub approval is not a legal determination or release decision.

[Back to top](#top)

---

## Correction, revocation, and rollback

### Documentation correction

For a defect in this README:

1. pin current `main`, target bytes, and any open overlapping work;
2. correct the smallest dependency-closed documentation and provenance set;
3. rerun structure, child-map, link, fragment, receipt, sensitive-content, and remote-diff checks;
4. preserve the prior blob and review record in Git history; and
5. state clearly that documentation rollback changes no rule or rights state.

Before merge, close or abandon the draft PR and branch if the change should not proceed. After an authorized merge, use a transparent revert or forward-fix PR; do not rewrite shared history. The README-only baseline before this modernization is blob `5dffc3a0ca80d8d94a8008e6c60b2f9489d5f077` from `main@f50e407026cef632f4d3f314b51884b29dfd9a45`.

### Rule correction and supersession

A material rule correction should preserve the prior source, package, bundle, evaluator, input, result, fixture, and test identities needed for replay; issue a versioned successor with effective time and supersession linkage; re-evaluate affected decisions and releases; append correction, withdrawal, or rollback records through their owning systems; invalidate affected governed caches and projections; and verify completion without leaking protected facts.

### Rights change or revocation

When terms, permission, consent, agreement, stewardship authority, or rights status is revoked, expires, narrows, or becomes disputed, the safe posture is immediate hold or denial for affected operations while scope is resolved. Propagation should follow stable lineage through derivatives, catalogs, release records, public carriers, caches, citations, exports, and AI outputs.

The current `correction/` and `release/` placeholders do not implement this flow. No repository-wide rights revocation propagation or completion proof was established in this review.

[Back to top](#top)

---

## Evidence snapshot

**Reviewed:** 2026-08-13 against exact `main@f50e407026cef632f4d3f314b51884b29dfd9a45` with base tree `3674f107f84d6ded25d45a7a83aaa60871ea6f95`.

Evidence included:

- the complete prior README, target history, direct-child directory, and recursive repository tree;
- both local Rego files and every nested Fauna, Flora, correction, release, and sensitivity placeholder;
- exact package-name and target-path repository searches;
- the parent policy README, sensitivity README, source and intake policy indexes, and related rights-named policy scaffolds;
- accepted ADR-0029, adopted Directory Rules v2, root registry, CODEOWNERS, and pull-request template;
- SourceDescriptor contract and schema, source-rights currentness contract/schema/fixtures/validator/tests/workflow, rights registry documentation, and rights validator documentation;
- `policy-test`, `policy-boundary-guards`, the placeholder policy runtime, `Makefile`, release boundary, and general PolicyDecision candidate surfaces; and
- the current generated-receipt schema and bounded integrity validator.

Re-review when child inventory, package name, default, input/output shape, rights vocabulary, terms source, owner, bundle, evaluator, consumer, workflow, required check, registry, review authority, sensitivity/consent composition, release integration, correction, revocation, rollback, or public behavior changes.

[Back to top](#top)

---

## Open verification register

| ID | Unresolved item | Current posture |
|---|---|---|
| RGT-001 | Accepted rights steward, source/domain reviewers, legal/escalation path, and independent approver | **NEEDS VERIFICATION** |
| RGT-002 | Whether the two `default deny := false` stubs should be corrected, replaced, migrated, or retired | **HOLD — separate policy change required** |
| RGT-003 | Accepted rights input contract, native result shape, normalized decision vocabulary, public-safe reason codes, and obligations | **UNKNOWN / NEEDS DECISION** |
| RGT-004 | Whether a rights-specific decision object is required or the general PolicyDecision family is sufficient | **NEEDS CONTRACT DECISION** |
| RGT-005 | Canonical rights registry object schema, emitted records, validator, fixtures, and authenticated review trail | **NOT ESTABLISHED** |
| RGT-006 | Accepted bundle manifest, selector, evaluator, signing/provenance, runtime consumer, decision receipt, replay, expiry, and cache-key contract | **UNKNOWN** |
| RGT-007 | Native positive and negative tests for every rights rule, including unknown/error anti-coercion coverage | **NOT ESTABLISHED** |
| RGT-008 | Verified authority, source snapshot, currentness, and disposition for every Fauna and Flora terms scaffold | **PROPOSED / NEEDS SOURCE REVIEW** |
| RGT-009 | Relationship and migration plan among `policy/rights/`, rights-named domain policies, and `policy/sources/rights/` | **NEEDS DIRECTORY AND POLICY REVIEW** |
| RGT-010 | Enforceable downstream attribution, redistribution, derivative, audience, retention, and stewardship obligations | **UNKNOWN** |
| RGT-011 | End-to-end correction, expiration, consent withdrawal, rights revocation, public withdrawal, cache invalidation, and completion proof | **UNKNOWN / FAIL CLOSED** |
| RGT-012 | Required-check, branch-ruleset, CODEOWNERS, and independent-review coupling | **UNKNOWN** |
| RGT-013 | External consumers not visible in repository search | **UNKNOWN** |
| RGT-014 | Private agreement storage, legal hold, retention, audit, and safe-reference requirements outside Git | **NEEDS POLICY AND OPERATIONS DECISION** |

[Back to top](#top)

---

## No-loss ledger

| Prior signal | Disposition in this revision |
|---|---|
| Stable H1 `policy :: rights` | Preserved exactly. |
| Greenfield bundle status | Preserved as confirmed placeholder/inactive maturity, with the actual child inventory exposed. |
| Policy-as-code intent | Preserved and bounded by accepted placement, explicit inputs/outcomes, tests, evaluator, and consumer requirements. |
| Attribution and license compatibility | Preserved as the two current local rule-family names without presenting their commented examples as contracts. |
| Fauna and Flora planned terms lanes | Preserved as proposed scaffolds; no source rights were invented or upgraded. |
| Correction, release, and sensitivity placeholders | Preserved and explicitly denied independent authority. |
| Unknown rights fail-closed intent from adjacent doctrine | Preserved as an authoring/integration requirement, not falsely attributed to the current stubs. |
| SourceDescriptor and rights-currentness machinery | Linked and accurately separated from rights policy execution and release authority. |
| Rights, sensitivity, consent, evidence, review, runtime, and release separation | Made explicit throughout. |
| Validation, review, correction, rollback, and open work | Added with current evidence and limitations. |
| Prior 44-byte README | Preserved in Git history and recorded by exact blob for documentation rollback. |

This revision changes documentation and generated provenance only. It does not change a Rego rule, package, contract, schema, fixture, validator, test, workflow, registry record, source descriptor, agreement, license, rights status, sensitivity decision, consent state, evaluator, runtime, release, deployment, publication, or public behavior.

<p align="right"><a href="#top">Back to top</a></p>
