<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/NEEDS-VERIFICATION-contract-schema-policy-split
title: Contract, Schema, and Policy Split
type: standard
version: v1
status: draft
owners: OWNER_TBD_NEEDS_VERIFICATION
created: NEEDS_VERIFICATION
updated: 2026-05-06
policy_label: POLICY_LABEL_TBD_NEEDS_VERIFICATION
related: [../../README.md, ./README.md, ../adr/ADR-0001-schema-home.md, ../../contracts/README.md, ../../schemas/README.md, ../../policy/README.md, ../../tests/README.md, ../../tools/validators/README.md]
tags: [kfm, architecture, contracts, schemas, policy, validation, governance, evidence, release]
notes: [Expanded replacement for the prior thin split note; target path is CONFIRMED in the accessible GitHub repository, but owners, policy label, created date, CI enforcement, schema-home acceptance, validator behavior, branch protections, and runtime maturity remain NEEDS VERIFICATION.]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Contract, Schema, and Policy Split

Contracts explain meaning; schemas validate shape; policy decides release/public behavior.

<p align="left">
  <img alt="status: draft" src="https://img.shields.io/badge/status-draft-lightgrey">
  <img alt="truth posture: evidence first" src="https://img.shields.io/badge/truth-evidence--first-blue">
  <img alt="contract role: meaning" src="https://img.shields.io/badge/contracts-meaning-5319e7">
  <img alt="schema role: shape" src="https://img.shields.io/badge/schemas-shape-0a7ea4">
  <img alt="policy role: decisions" src="https://img.shields.io/badge/policy-decisions-b60205">
  <img alt="posture: fail closed" src="https://img.shields.io/badge/posture-fail--closed-critical">
</p>

> [!IMPORTANT]
> **Status:** `draft`  
> **Path:** `docs/architecture/contract-schema-policy-split.md`  
> **Owning root:** `docs/` as the human-facing architecture and control-plane surface.  
> **Truth posture:** CONFIRMED doctrine and repo placement / PROPOSED enforcement model / NEEDS VERIFICATION for active CI, validators, branch protections, release gates, and runtime behavior.  
> **Quick jumps:** [Scope](#scope) · [Repo fit](#repo-fit) · [The split](#the-split-at-a-glance) · [Architecture flow](#architecture-flow) · [Responsibility seams](#responsibility-seams) · [Object families](#object-family-placement-map) · [Change workflow](#change-workflow) · [Gates](#gates-and-definition-of-done) · [Anti-patterns](#anti-patterns-to-reject) · [Open verification](#open-verification-backlog)

> [!NOTE]
> This architecture note does **not** accept or supersede `ADR-0001` by itself. It documents the operating split that KFM should preserve while ADRs, validators, fixtures, and CI decide the exact enforcement mechanics.

---

## Scope

This document explains how KFM keeps three trust-critical surfaces separate without letting them drift:

| Surface | Short rule | Consequence |
|---|---|---|
| `contracts/` | Define meaning. | A maintainer can understand what an object is for, what its fields mean, and what compatibility promises it carries. |
| `schemas/` | Validate shape. | A tool can check whether an object is structurally valid for a versioned contract family. |
| `policy/` | Decide admissibility. | A rule can allow, deny, restrict, abstain, hold, generalize, embargo, correct, or block release/runtime behavior. |

This document is for architecture, documentation, schema, policy, validator, API, UI, release, and domain-lane maintainers. It is not a schema registry, policy bundle, validator implementation, release manifest, or proof pack.

### Accepted content

Content belongs in this architecture note when it clarifies:

- how contract meaning, machine schema shape, and policy decisions relate;
- which adjacent lane owns validation, fixtures, receipts, proofs, release records, or runtime behavior;
- how reviewers should detect split-authority drift;
- how object-family changes should move through contracts, schemas, policy, tests, validators, release, and docs;
- what must be verified before calling a split “enforced.”

### Exclusions

Do **not** use this document to store or define:

| Exclusion | Proper home |
|---|---|
| JSON Schema bodies | `../../schemas/` or the ADR-approved schema home |
| Object semantics as machine schemas only | `../../contracts/` plus schema references |
| Policy allow/deny logic | `../../policy/` |
| Valid/invalid fixtures | `../../tests/` or the ADR-approved fixture home |
| Validator code | `../../tools/validators/` |
| Receipts, proofs, manifests, rollback cards, or catalog records | lifecycle, proof, release, or catalog homes after repo verification |
| API handlers, UI conditionals, or model adapters | app/package/runtime homes after repo verification |
| Claims that tests, workflows, or runtime enforcement exist | only with current repo, CI, log, receipt, proof, or workflow evidence |

[Back to top](#top)

---

## Repo fit

| Field | Value |
|---|---|
| Target file | `docs/architecture/contract-schema-policy-split.md` |
| Document role | Architecture note that keeps `contracts/`, `schemas/`, `policy/`, tests, validators, receipts, proofs, release, and runtime boundaries legible. |
| Owning root | `docs/` because this is human-facing architecture and governance guidance. |
| Upstream orientation | [`../../README.md`](../../README.md), [`./README.md`](./README.md), [`../adr/ADR-0001-schema-home.md`](../adr/ADR-0001-schema-home.md) |
| Primary adjacent roots | [`../../contracts/README.md`](../../contracts/README.md), [`../../schemas/README.md`](../../schemas/README.md), [`../../policy/README.md`](../../policy/README.md) |
| Verification roots | [`../../tests/README.md`](../../tests/README.md), [`../../tools/validators/README.md`](../../tools/validators/README.md) |
| Update trigger | Any material change to object-family meaning, schema-home authority, policy gates, fixture homes, validator behavior, runtime envelopes, release proof, correction, or rollback. |

> [!WARNING]
> `docs/architecture/` explains the split. It does not create machine authority. Enforcement lives in the verified combination of ADRs, schema files, fixtures, validators, policy tests, workflow checks, release receipts, and review state.

[Back to top](#top)

---

## The split at a glance

### One governing sentence

> Contracts explain meaning; schemas validate shape; policy decides release/public behavior.

### Division of labor

| Lane | Owns | Must not silently own | Typical review question |
|---|---|---|---|
| `contracts/` | Object meaning, field intent, lifecycle semantics, compatibility rules, human-readable examples. | Machine validation as the only source of truth; policy decisions; emitted instances. | “Does this prose define what downstream systems may rely on?” |
| `schemas/` | Versioned machine-checkable shape, `$id`/version discipline, structural constraints, schema fixtures when approved. | Source authority, policy permission, release readiness, steward review. | “Can tools validate the object without guessing?” |
| `policy/` | Allow/deny/restrict/hold/abstain logic, obligations, reason codes, sensitivity, rights, review, release, correction, runtime admissibility. | Object meaning, schema storage, data lifecycle storage, UI-only trust state. | “What is permitted, blocked, generalized, or held, and why?” |
| `tests/` / fixtures | Positive and negative proof that the split behaves as claimed. | Contract authority, schema authority, policy authority. | “Can the happy path and failure path both be demonstrated?” |
| `tools/validators/` | Deterministic checks over schemas, fixtures, links, manifests, evidence, citations, and release candidates. | Policy law, publication, signing, receipt storage, proof custody. | “Can the validator fail closed with stable reasons?” |
| data / release / proof lanes | Instances, receipts, proof packs, manifests, published pointers, correction and rollback records. | Contract/schema/policy definitions. | “Can the published state be audited and reversed?” |
| apps / packages | Runtime consumers and implementations. | Hidden contract, schema, or policy authority. | “Does runtime consume the governed split instead of replacing it?” |

### What “valid” does not mean

A schema-valid object is not automatically publishable.

```text
schema-valid
≠ evidence-resolved
≠ rights-cleared
≠ sensitivity-safe
≠ policy-allowed
≠ reviewed
≠ released
≠ correction-ready
```

A KFM object becomes public-safe only when meaning, shape, evidence, policy, review, release, and rollback all line up.

[Back to top](#top)

---

## Architecture flow

```mermaid
flowchart LR
    D[Doctrine / domain need / source rule] --> C[contracts/<br/>meaning and compatibility]
    C --> S[schemas/<br/>versioned machine shape]
    C --> T[tests + fixtures<br/>valid and invalid examples]
    S --> V[tools/validators/<br/>shape, links, hashes, citations, closure]
    T --> V

    V --> P[policy/<br/>allow, deny, restrict, hold, abstain, obligations]
    P --> R[review + promotion<br/>state transition]
    R --> M[release manifest<br/>proof + rollback target]
    M --> PUB[PUBLISHED<br/>released artifacts]
    PUB --> API[governed API / tile service]
    API --> UI[Map shell / Evidence Drawer / Focus Mode]

    REC[data/receipts<br/>process memory] -. supports .-> R
    PROOF[data/proofs<br/>release-grade evidence] -. supports .-> M
    CAT[data/catalog<br/>discovery + provenance] -. supports .-> M

    RAW[RAW / WORK / QUARANTINE] -. forbidden public bypass .-> API
    RAW -. forbidden runtime bypass .-> UI

    C -. not policy .-> P
    S -. not meaning .-> C
    V -. not publication .-> M
```

> [!CAUTION]
> A public map layer, search index, dashboard value, model answer, export, or story node is downstream of this flow. It must not become a shortcut around evidence, policy, review, release, correction, or rollback.

[Back to top](#top)

---

## Responsibility seams

### Contract seam

A contract change is needed when object **meaning** changes.

Examples:

- a field’s interpretation changes;
- a new object family is introduced;
- a lifecycle meaning changes;
- compatibility promises change;
- a runtime surface relies on a new trust-bearing field;
- a release or correction workflow depends on a new semantic link.

A contract change should usually trigger a schema, fixture, validator, policy, and docs review.

### Schema seam

A schema change is needed when machine **shape** changes.

Examples:

- required fields change;
- enum members change;
- `$id` or versioning changes;
- cross-object `$ref` targets change;
- a fixture starts passing or failing differently;
- machine consumers need a new structural guarantee.

A schema change should not define public permission. It should give validators and tests the shape they need.

### Policy seam

A policy change is needed when **permission, restriction, review, or release behavior** changes.

Examples:

- a source role is allowed or denied for a claim type;
- unknown rights fail closed;
- exact geometry must be generalized;
- a runtime answer must abstain without citations;
- a release requires rollback target and correction path;
- a steward review threshold changes.

A policy change should ship with negative fixtures, reason/obligation codes, and review notes.

### Validator seam

A validator change is needed when enforceable **checking behavior** changes.

Examples:

- a new schema must compile;
- a new fixture family must pass/fail;
- `EvidenceRef` must resolve to `EvidenceBundle`;
- a `ReleaseManifest` must prove rollback closure;
- a runtime envelope must reject non-finite outcomes.

Validators operationalize the split. They do not replace it.

[Back to top](#top)

---

## Object-family placement map

The table below is a placement guide, not a claim that every file already exists or is enforcement-grade. Exact paths, aliases, and versioning must follow the active ADR and repository evidence.

| Object family | Contract meaning home | Machine shape home | Policy touchpoint | Proof pressure |
|---|---|---|---|---|
| `SourceDescriptor` | `contracts/source/` | `schemas/contracts/v1/source/` | source role, rights, terms, cadence, sensitivity | source registry fixtures; source admission checks |
| `EvidenceRef` | `contracts/evidence/` | `schemas/contracts/v1/evidence/` | citation eligibility, evidence admissibility | resolver tests; unresolved-ref negative cases |
| `EvidenceBundle` | `contracts/evidence/` | `schemas/contracts/v1/evidence/` | public support, rights, review, release state | bundle composition fixtures; Evidence Drawer payload checks |
| `DecisionEnvelope` | `contracts/runtime/` or policy contract lane | `schemas/contracts/v1/policy/` or runtime family | allow, deny, abstain, hold, obligations | finite outcome fixtures |
| `RuntimeResponseEnvelope` | `contracts/runtime/` | `schemas/contracts/v1/runtime/` | cite-or-abstain, public response permission | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` fixtures |
| `ValidationReport` | `contracts/data/` or validation contract lane | `schemas/contracts/v1/data/` | policy consumes validator result | pass/fail report fixtures |
| `PolicyDecision` | `contracts/policy/` or policy contract lane | `schemas/contracts/v1/policy/` | policy result itself | reason-code and obligation-code tests |
| `ReleaseManifest` | `contracts/release/` | `schemas/contracts/v1/release/` | publication state, release scope, rollback target | release closure tests |
| `ProofPack` | `contracts/release/` | `schemas/contracts/v1/release/` | promotion and public support | proof closure tests |
| `CorrectionNotice` | `contracts/correction/` | `schemas/contracts/v1/correction/` | supersession, withdrawal, correction propagation | correction and rollback drills |
| `AIReceipt` / `RunReceipt` | `contracts/runtime/` or receipt contract lane | `schemas/contracts/v1/runtime/` | runtime audit, no-hidden-truth posture | process-memory fixture tests |

> [!NOTE]
> If `contracts/` and `schemas/` both appear to contain normative machine definitions for the same object, stop and resolve the authority path before adding another file. Do not maintain divergent definitions in parallel.

[Back to top](#top)

---

## Change workflow

Use this workflow whenever a new trust-bearing object or rule appears.

```text
1. Name the object family or policy seam.
2. Define or update contract meaning.
3. Define or update machine schema shape.
4. Add valid and invalid fixtures.
5. Add or update validators.
6. Add or update policy rules when release/public/runtime behavior changes.
7. Add reviewer-facing tests or CI summaries.
8. Update docs, ADRs, runbooks, and registers.
9. Confirm release, correction, and rollback impact.
10. Merge only with a visible validation and rollback story.
```

### Change matrix

| Change type | Minimum companion changes |
|---|---|
| New object family | contract card, schema, valid/invalid fixtures, validator path, docs links |
| Field added | schema change, contract meaning, fixture update, compatibility note |
| Required field added | breaking-change review, negative fixtures, downstream consumer review |
| Enum changed | vocabulary/reason-code review, policy impact review, fixtures |
| Policy rule changed | policy fixture pair, reason/obligation code review, release/runtime impact note |
| Runtime envelope changed | contract, schema, policy postcheck, Evidence Drawer/Focus Mode payload tests |
| Release object changed | release manifest validation, proof closure, rollback drill |
| Correction behavior changed | correction notice, supersession/withdrawal fixture, propagation test |
| Schema home moved | ADR or migration note, alias registry if needed, consumer inventory, rollback path |

[Back to top](#top)

---

## Gates and definition of done

A change that affects this split is not done until the relevant boxes are true.

### Architecture gate

- [ ] The owning surface is explicit: `contracts/`, `schemas/`, `policy/`, `tests/`, `tools/validators/`, data/proof/release, or runtime.
- [ ] No domain-specific shortcut creates a new root-level authority.
- [ ] The change preserves the RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED lifecycle boundary.
- [ ] Public clients remain downstream of governed APIs and released artifacts.

### Contract/schema gate

- [ ] Contract meaning and schema shape agree.
- [ ] Schema-home authority follows the active ADR or is visibly marked `NEEDS VERIFICATION`.
- [ ] Valid fixtures prove the intended shape.
- [ ] Invalid fixtures prove fail-closed behavior.
- [ ] Compatibility impact is marked: additive, breaking, deprecated, alias-backed, or docs-only.

### Policy gate

- [ ] Unknown rights, sensitivity, review state, source role, or release state fails closed.
- [ ] Policy reason codes and obligations are stable enough to test.
- [ ] Runtime outcomes remain finite.
- [ ] Publication remains a governed state transition.
- [ ] Correction and rollback impacts are visible.

### Validator/test gate

- [ ] Validators consume contracts/schemas/policy rather than redefining them.
- [ ] Tests include at least one negative path for consequential behavior.
- [ ] No test or validator silently reads RAW, WORK, QUARANTINE, unpublished candidates, secrets, or direct model outputs.
- [ ] CI/workflow claims are made only after workflow evidence is checked.

### Documentation gate

- [ ] Adjacent READMEs are updated when behavior changes.
- [ ] ADR links are updated when authority changes.
- [ ] Open placeholders remain visible instead of being smoothed into confident prose.
- [ ] Rollback or supersession path is described.

[Back to top](#top)

---

## Anti-patterns to reject

| Anti-pattern | Why it is unsafe |
|---|---|
| “It validates, so it can publish.” | Shape validation does not prove evidence, rights, policy, review, release, or rollback. |
| Contract meaning only in JSON Schema descriptions. | Human-readable doctrine becomes hidden inside machine files and hard to review. |
| Policy logic in UI conditionals. | Public behavior drifts from backend, release, and review gates. |
| Validators deciding release by themselves. | Validators verify; policy and promotion decide. |
| Receipts treated as proof packs. | Process memory is not release-grade proof. |
| Proof packs stored as schema examples. | Examples are not published proof custody. |
| `contracts/` and `schemas/` both carrying divergent definitions. | Split authority breaks auditability and testability. |
| Public runtime reading RAW or WORK data directly. | Bypasses the trust membrane. |
| AI output treated as evidence. | Generated text is interpretive and subordinate to `EvidenceBundle`, policy, review, and release state. |
| Future paths copied from prior reports without repo verification. | Repetition is lineage, not implementation proof. |

[Back to top](#top)

---

## Reviewer quickstart

Run these from a real checkout before reviewing a split-sensitive change. Adapt to repo-native tools after confirming the package manager and CI conventions.

```bash
git status --short
git branch --show-current || true
git rev-parse --show-toplevel || true

find docs/architecture docs/adr contracts schemas policy tests tools/validators \
  -maxdepth 3 -type f 2>/dev/null | sort | sed -n '1,300p'

git grep -nE \
  'contract-schema-policy|schema home|canonical schema|EvidenceBundle|DecisionEnvelope|RuntimeResponseEnvelope|PolicyDecision|ReleaseManifest|CorrectionNotice|ABSTAIN|DENY|fail closed|RAW|QUARANTINE' \
  -- docs contracts schemas policy tests tools 2>/dev/null || true
```

### Review questions

1. What does the contract say this object **means**?
2. What schema proves the object **shape**?
3. What policy decides whether the object is **admissible**?
4. Which fixtures prove the **happy path and failure path**?
5. Which validator produces a **stable report**?
6. Which release, correction, or rollback object changes?
7. Which UI or runtime surface consumes the result?
8. What happens when evidence, rights, sensitivity, or release state is unknown?

[Back to top](#top)

---

## Open verification backlog

| Item | Status | Why it matters |
|---|---:|---|
| `OWNER_TBD_NEEDS_VERIFICATION` | NEEDS VERIFICATION | The document needs owner review routing before publication. |
| `policy_label` | NEEDS VERIFICATION | Public/restricted status must match repo policy. |
| Created date | NEEDS VERIFICATION | Existing file did not carry a meta block; creation lineage needs maintainer confirmation. |
| `ADR-0001` acceptance state | NEEDS VERIFICATION | This note should not claim schema-home law until ADR status and acceptance evidence are confirmed. |
| Schema-home aliases | NEEDS VERIFICATION | If old paths exist, aliases must be explicit, tested, and dated. |
| Canonical fixture home | NEEDS VERIFICATION | `schemas/tests/fixtures/` and repo-wide `tests/` must not fork proof authority. |
| Validator enforcement | UNKNOWN until current tests/workflows are inspected | README presence does not prove merge-blocking validation. |
| Policy engine and runner | UNKNOWN | OPA/Conftest or equivalent enforcement cannot be claimed without tool evidence. |
| Runtime/API consumers | UNKNOWN | Route names, DTOs, and runtime behavior require source inspection. |
| Branch protections and CI status | UNKNOWN | Workflow files alone do not prove enforcement. |
| Release/proof artifacts | UNKNOWN | Release manifests, proof packs, receipts, and rollback objects require emitted artifact evidence. |

[Back to top](#top)

---

## Appendix: glossary

<details>
<summary><strong>Core terms</strong></summary>

| Term | Meaning in this document |
|---|---|
| Contract | Human-readable meaning and compatibility intent for a KFM object or seam. |
| Schema | Machine-checkable structure for a versioned object family. |
| Policy | Decision logic governing admissibility, restrictions, review, release, correction, runtime, and exposure. |
| Validator | Deterministic tool that checks shape, linkage, closure, hashes, citations, manifests, or fixture expectations. |
| Fixture | Small valid or invalid example used to prove behavior. |
| Receipt | Process-memory artifact that records what happened in a run. |
| Proof pack | Release-grade closure artifact that bundles validation, evidence, policy, integrity, and release support. |
| Release manifest | Governed declaration of published artifacts, scope, hashes, correction links, and rollback target. |
| EvidenceBundle | Resolved evidence support for a claim or runtime response. |
| Fail closed | Block, deny, abstain, hold, generalize, quarantine, or error instead of guessing. |
| Trust membrane | Boundary preventing public clients, UI, AI, exports, and derivatives from bypassing governed evidence, policy, and release paths. |

</details>

<details>
<summary><strong>Pre-publish checklist for this file</strong></summary>

- [x] KFM Meta Block V2 is present.
- [x] One H1 only.
- [x] Purpose line appears directly below the title.
- [x] Badges and quick jumps are present.
- [x] Repo fit is explicit.
- [x] Contract/schema/policy roles are separate.
- [x] Mermaid diagram is meaningful and grounded.
- [x] Tables clarify responsibility seams and object placement.
- [x] Code fences are language-tagged.
- [x] Long reference content is wrapped in `<details>`.
- [x] Unknowns and placeholders are visible.
- [ ] Owners, policy label, created date, ADR status, validator behavior, CI enforcement, and release proof are verified by maintainers before promotion.

</details>

[Back to top](#top)
