<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-specs-readme
title: Pipelines Specs Compatibility Guardrail
type: readme; directory-readme; compatibility-guardrail; migration-boundary
version: v0.2
status: draft; repository-grounded; non-authoritative; no-active-spec-system-established
owners:
  - OWNER_TBD — Pipeline owner
  - OWNER_TBD — Pipeline-spec steward
  - OWNER_TBD — Validation and CI steward
  - OWNER_TBD — Governance steward
  - OWNER_TBD — Docs steward
created: 2026-06-13
updated: 2026-07-22
supersedes: v0.1
policy_label: public-doc; compatibility-only; declarative-specs-prohibited; no-secrets; no-direct-execution; no-direct-activation; no-direct-release; no-publication
current_path: pipelines/specs/README.md
truth_posture: CONFIRMED existing guardrail README, canonical pipelines versus pipeline_specs responsibility split, companion root documentation, pipeline test boundary, pipeline receipt lane, generated-receipt requirement, and broad documentation workflow posture / PROPOSED automated misplaced-spec detection, explicit compatibility registry, and retirement plan / UNKNOWN exhaustive directory inventory, path consumers, parser discovery behavior, workflow enforcement, branch-protection coupling, runtime use, and external references / NEEDS VERIFICATION named owners, accepted retirement or retention decision, complete reference inventory, drift-register entry if misplaced content is found, and enforcement coverage
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 459b41d7ec91240742d8b2d3e5d9eb4dbd248df7
  target_prior_blob: 1314bf0fe34736e75f1a2d0900b049ebea2d87bd
  canonical_spec_readme_blob: 7f35f1c06aaec08d03182cf71e88a812bf179ebf
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  bounded_inventory_note: Direct file reads and repository-index queries do not establish an exhaustive recursive inventory or absence of branch-local, generated, historical, external, or dynamically discovered consumers.
related:
  - ../../CONTRIBUTING.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/architecture/directory-rules.md
  - ../../docs/registers/DRIFT_REGISTER.md
  - ../README.md
  - ../../pipeline_specs/README.md
  - ../../tests/pipelines/README.md
  - ../../data/receipts/pipeline/README.md
  - ../../data/receipts/generated/README.md
  - ../../.github/workflows/README.md
tags: [kfm, pipelines, pipeline-specs, compatibility, placement, migration, no-parallel-authority]
notes:
  - "This path is a compatibility and placement guardrail inside the executable pipelines responsibility root."
  - "Authoritative declarative pipeline configuration belongs in pipeline_specs/, not pipelines/specs/."
  - "This README does not activate a spec, parser, consumer, source, schedule, workflow, lifecycle transition, receipt, release, or public artifact."
  - "Changing the canonical pipelines/pipeline_specs split requires an accepted ADR; this documentation-only clarification does not."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Pipelines Specs Compatibility Guardrail

> Placement and migration guidance that prevents `pipelines/specs/` from becoming a second declarative pipeline-specification authority.

![status](https://img.shields.io/badge/status-draft-blue)
![authority](https://img.shields.io/badge/authority-compatibility%20guardrail-455a64)
![canonical-spec-root](https://img.shields.io/badge/canonical%20spec%20root-pipeline__specs%2F-d62728)
![publication](https://img.shields.io/badge/publication-none-d62728)

**Path:** `pipelines/specs/README.md`

**Audience:** pipeline, pipeline-spec, domain, validation, CI, governance, release, and documentation maintainers

**Owning responsibility root:** [`pipelines/`](../README.md) — executable pipeline logic, the **how**

**Canonical declarative root:** [`pipeline_specs/`](../../pipeline_specs/README.md) — governed configuration, the **what**

**Authority level:** compatibility and migration guidance only

**Current maturity:** documentation guardrail; active parser, registry, consumer, and enforcement depth remain `UNKNOWN`

> [!IMPORTANT]
> Do not add or activate declarative pipeline specifications here. A filename, YAML document, parser success, schedule, workflow result, pipeline run, or merge does not create source authority, evidence closure, policy approval, lifecycle promotion, release approval, or publication.

> [!NOTE]
> This README records doctrine and the bounded repository evidence listed below. It does not prove that every file, consumer, branch, workflow, or external reference has been inventoried.

## Quick navigation

[Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Repository fit](#repository-fit) · [Admission](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Discovery](#consumer-and-discovery-rules) · [Migration](#misplaced-content-and-migration) · [Validation](#validation) · [Review](#review-adrs-and-drift) · [Done](#definition-of-done) · [Open items](#open-verification-register) · [Evidence](#evidence-ledger) · [Rollback](#correction-and-rollback)

## Purpose

`pipelines/specs/` exists to make a repository boundary explicit:

```text
pipelines/       = executable pipeline logic and orchestration — HOW work runs
pipeline_specs/  = declarative pipeline configuration — WHAT may run
```

This lane prevents convenience, an old path reference, or a generic tool convention from creating a parallel specification home inside the executable root.

It serves three bounded purposes:

1. route declarative work to `pipeline_specs/`;
2. describe safe handling of content discovered under this path; and
3. preserve a reviewable compatibility pointer while retention or retirement remains unresolved.

It does not define a pipeline-spec schema, canonicalization algorithm, parser, registry, consumer binding, activation state, source decision, schedule, policy result, receipt shape, or release process.

[Back to top](#top)

## Authority level

**Compatibility and migration guidance; non-authoritative for pipeline specifications.**

[Directory Rules](../../docs/doctrine/directory-rules.md) assigns both `pipelines/` and `pipeline_specs/` as canonical responsibility roots but gives them different responsibilities. The companion [`pipeline_specs/` README](../../pipeline_specs/README.md) is the declarative-root landing page. This nested guardrail cannot amend either root contract.

| Responsibility | Owning surface | Rule for this lane |
|---|---|---|
| Executable pipeline behavior | [`pipelines/`](../README.md) | Do not place executable modules in `pipelines/specs/`; use the appropriate executable lane. |
| Declarative pipeline configuration | [`pipeline_specs/`](../../pipeline_specs/README.md) | All new authoritative specs and profiles route there. |
| Semantic meaning | `contracts/` | A document here cannot define object meaning by location. |
| Machine-checkable shape | `schemas/` | A parser accepting a file here does not make this a schema home. |
| Admissibility, rights, sensitivity, and access | `policy/` | Specs may reference governed policy but cannot replace a policy decision. |
| Tests and fixtures | [`tests/`](../../tests/pipelines/README.md) and `fixtures/` | Evidence of enforceability belongs outside this lane. |
| Lifecycle data and process receipts | `data/` and [`data/receipts/pipeline/`](../../data/receipts/pipeline/README.md) | Never store run output or receipts beside this README. |
| Release, correction, and rollback decisions | `release/` | No path or run in this lane can approve a transition to `PUBLISHED`. |

Changing the canonical split, promoting this path into a second spec home, or retiring a canonical root requires an accepted ADR under Directory Rules. Clarifying the existing guardrail does not.

[Back to top](#top)

## Status

### Confirmed at the evidence snapshot

- This README already existed as a compatibility guardrail at the pinned base.
- `pipelines/` and `pipeline_specs/` are documented as separate executable and declarative responsibility roots.
- The current `pipeline_specs/` landing page also identifies this path as a guardrail rather than an alternate authority.
- The inspected `pipeline_specs/` landing page does not establish an accepted root spec schema, active parser, consumer registry, scheduler, source-activation binding, dedicated root fixture/test suite, or substantive spec CI gate.
- The inspected pipeline test README describes distributed negative coverage but does not establish a dedicated executable `tests/pipelines/` suite.
- Generated provenance records have an established receipt lane and schema; those records remain process memory, not proof, approval, or release authority.

### Not established

| Question | State | Consequence |
|---|---|---|
| Exhaustive contents of `pipelines/specs/` across refs and history | `UNKNOWN` | Do not claim this README is the only file everywhere. |
| Repository-wide or external consumers of this path | `UNKNOWN` | Do not rename, delete, or redirect without a reference inventory. |
| Parser or directory scanner exclusion | `UNKNOWN` | A consumer must not assume the path is inert merely because this README says so. |
| Automated misplaced-spec linting | `PROPOSED` | Documentation is the current guardrail; executable enforcement is not claimed. |
| Retain-versus-retire decision | `NEEDS VERIFICATION` | Keep the pointer stable until owners review compatibility needs. |
| Named accountable owners | `NEEDS VERIFICATION` | Placeholder roles remain visible; no person or team is invented. |

[Back to top](#top)

## Repository fit

```text
pipelines/
├── README.md
├── <executable lanes>/
└── specs/
    └── README.md      # compatibility and migration guardrail

pipeline_specs/
├── README.md          # canonical declarative-root boundary
└── <reviewed lanes>/  # mixed maturity; file presence is not activation
```

The tree is a responsibility map, not a complete inventory. The canonical root README records placeholder-heavy and compatibility-oriented lanes whose activation maturity remains bounded. Moving a file from this path into `pipeline_specs/` corrects placement only; it does not activate or validate that file.

KFM lifecycle law remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A spec may describe prerequisites or candidate transitions. Neither a spec nor this directory performs a governed promotion.

[Back to top](#top)

## What belongs here

New content is restricted to compatibility and migration material:

- this README;
- a short pointer to an exact canonical `pipeline_specs/` target during a reviewed migration;
- a deprecation notice with owner, decision reference, compatibility window, and rollback target; or
- a migration note that inventories old references and records their verified replacement.

Every additional file must answer:

| Admission question | Required answer |
|---|---|
| Is it an executable module? | No; route executable logic to the appropriate `pipelines/` lane. |
| Is it a declarative spec or profile? | No; route it to `pipeline_specs/`. |
| Does it create independent rules or fields? | No; compatibility material must not evolve separately. |
| Is the canonical target exact and verified? | Yes. |
| Is its owner, review state, expiration or retirement condition, and rollback path visible? | Yes. |
| Is an ADR or migration record required? | Linked and accepted where Directory Rules requires one. |

If these answers are unavailable, do not add the file. Record the uncertainty for review.

[Back to top](#top)

## What does not belong here

| Do not place here | Correct responsibility home or action |
|---|---|
| Pipeline-spec YAML, JSON, TOML, or other declarative payloads | `pipeline_specs/<reviewed-lane>/` |
| Parser, loader, registry, scheduler, runner, or adapter code | Appropriate `pipelines/`, `packages/`, `tools/`, or application lane after ownership review |
| Contract or schema definitions | `contracts/` and `schemas/` |
| Policy rules or decisions | `policy/` and governed decision records |
| Source descriptors, credentials, endpoints, or activation records | Accepted source registry/configuration surfaces; never secrets in this public README lane |
| Test code or test data | `tests/` and `fixtures/` |
| RAW, WORK, QUARANTINE, PROCESSED, catalog, triplet, or published data | Correct lifecycle phase under `data/` |
| Run receipts, proofs, evidence bundles, or validation reports | Accepted receipt, proof, evidence, or validation homes |
| Release manifests, promotion decisions, correction notices, or rollback cards | `release/` and accepted companion object families |
| Public API, UI, map, AI, or export code | Governed application and package surfaces |

Do not add a symlink, mirror, copied spec, generated spec, sample that looks active, or fallback search path. Each can become a second authority even when introduced as a convenience.

[Back to top](#top)

## Consumer and discovery rules

Until an accepted migration decision says otherwise, consumers must treat `pipelines/specs/` as non-discoverable for active configuration.

| Consumer behavior | Required posture |
|---|---|
| Recursive spec scan | Exclude this path and use an explicit governed registry or accepted `pipeline_specs/` discovery rule. |
| Direct file reference | Replace with a verified canonical reference through a reviewed migration. |
| Fallback lookup | Reject or hold rather than silently read from this lane. |
| Duplicate ID or schedule | Freeze activation and resolve authority before execution. |
| Compatibility pointer | Follow only when the pointer names one canonical target and its migration state is reviewable. |
| Missing canonical target | Fail safely; do not reactivate the compatibility copy. |

These are documentation requirements. Executable enforcement, parser behavior, reason-code vocabulary, and current consumer coverage remain `UNKNOWN` until verified in code, tests, workflows, and emitted records.

Directory scanning alone is not a safe activation mechanism. The canonical root contains scaffolds, placeholders, and compatibility lanes of mixed maturity, so activation requires accepted shape, identity, parser, consumer, source, policy, fixtures, tests, review, receipt, correction, and rollback controls.

[Back to top](#top)

## Misplaced content and migration

If any non-guardrail content is found here, stop new writes and classify it before moving or using it.

| Finding | Immediate posture | Candidate destination | Decision burden |
|---|---|---|---|
| Declarative spec or profile | Freeze activation; mark placement drift. | `pipeline_specs/<reviewed-lane>/` | Reference inventory, schema/consumer/activation review, migration and rollback. |
| Executable code | Do not run from this lane. | Appropriate executable responsibility lane | Ownership, dependency, test, and side-effect review. |
| Test or fixture | Keep out of discovery until classified. | `tests/` or `fixtures/` | Rights/sensitivity review and deterministic no-network coverage. |
| Receipt, proof, evidence, or lifecycle output | Quarantine the placement; do not publish. | Accepted `data/` object-family lane | Integrity, sensitivity, lineage, and authority review. |
| Release or correction record | Hold; this lane has no release authority. | `release/` | Release-steward review and rollback/correction lineage. |
| Unclear file | Do not guess. | Undecided | Add a bounded drift or verification item and request steward review. |

### Migration sequence

1. Pin the repository ref, target blob, and complete candidate path set.
2. Inventory inbound references, generated copies, `$id` or stable identifiers, schedules, parser rules, consumers, workflows, releases, and external dependencies.
3. Classify each file by responsibility and lifecycle, not by filename or topic.
4. Record the conflict in the [drift register](../../docs/registers/DRIFT_REGISTER.md) when actual misplaced content or authority conflict is confirmed.
5. Obtain an accepted ADR before changing the canonical root or authority model; use a bounded migration note for routine relocation within the existing split.
6. Prepare the canonical file, reference updates, tests, fixtures, deactivation behavior, compatibility window, correction handling, and rollback as one reviewable change.
7. Verify that no active consumer still reads the old path and that no duplicate authority remains.
8. Retain a pointer only for a documented compatibility need; otherwise retire the path through a separate authorized change.

A Git move preserves history but does not, by itself, prove semantic compatibility, parser agreement, consumer migration, source authority, policy closure, release safety, or rollback readiness.

[Back to top](#top)

## Security, rights, and publication boundary

This public documentation lane must not contain:

- credentials, tokens, private endpoints, connection strings, or operational secrets;
- restricted source payloads or terms-controlled content;
- exact sensitive ecological, archaeological, cultural, infrastructure, private-land, living-person, or DNA/genomic information;
- real lifecycle records, receipts, evidence, review records, or release decisions; or
- examples that could be mistaken for activated production configuration.

Unknown rights, source role, sensitivity, evidence, review, or release state fails closed. Use quarantine, restriction, redaction, generalization, delayed activation, or denial through the owning governance surfaces.

Watcher activity, parser success, validation success, pipeline completion, pull-request merge, or GitHub release is not KFM publication. Public clients remain downstream of governed APIs and released, policy-filtered artifacts.

[Back to top](#top)

## Validation

### Documentation checks for this lane

- [ ] Exactly one H1 and a coherent heading hierarchy.
- [ ] KFM Meta Block wrapper is closed; document ID and creation date are preserved.
- [ ] Relative links and quick-navigation anchors resolve at the pinned ref.
- [ ] Code fences, tables, callouts, and HTML anchors are balanced.
- [ ] No unverified owner, active consumer, enforcement, runtime, CI, release, or publication claim is promoted to fact.
- [ ] No secret, restricted payload, or sensitive location is present.
- [ ] The diff contains only authorized documentation and required provenance.
- [ ] Final newline, whitespace, and remote read-back checks pass.

### Migration or enforcement checks

When a future change moves content, adds linting, or changes consumer behavior, also require:

- a pinned recursive tree and complete reference inventory;
- explicit parser and consumer discovery tests;
- duplicate-ID, duplicate-schedule, fallback-path, and missing-target negative cases;
- deterministic no-network fixtures by default;
- proof that old-path content cannot activate or publish;
- receipt hashes and bounded side-effect checks;
- correction, deactivation, compatibility-window, and rollback tests; and
- workflow-trigger and permission review for any CI change.

The [`tests/pipelines/` README](../../tests/pipelines/README.md) defines the broader intended pipeline behavior test boundary. Passing Markdown checks proves only document structure and link integrity. It does not prove an active spec system, pipeline behavior, evidence closure, policy approval, release readiness, or publication safety.

[Back to top](#top)

## Review, ADRs, and drift

### Review burden

A change limited to this README needs pipeline, pipeline-spec, governance, and documentation review. A migration or enforcement change also needs the owners of every affected parser, consumer, domain, source, contract/schema, policy, fixture/test, receipt, release, security, rights, and sensitivity surface.

CODEOWNERS routing is review routing, not a `ReviewRecord`, policy approval, release decision, or publication authorization.

### ADR boundary

An accepted ADR is required before a change:

- promotes `pipelines/specs/` into an authoritative spec home;
- renames, removes, or changes the responsibility of `pipelines/` or `pipeline_specs/`;
- creates another parallel contract, schema, policy, source, registry, receipt, proof, release, or lifecycle authority; or
- bends a KFM trust, lifecycle, public-path, evidence, policy, review, correction, or rollback invariant.

No ADR is required for this in-place documentation clarification because it preserves the existing responsibility split and creates no new authority.

### Drift posture

The inspected [drift register](../../docs/registers/DRIFT_REGISTER.md) did not contain a `pipelines/specs/` entry at the pinned snapshot. That absence does not prove the path has no consumers or misplaced content. Add a focused register entry only when a concrete conflict is verified; do not create speculative drift records.

Two Directory Rules copies are present under [`docs/doctrine/`](../../docs/doctrine/directory-rules.md) and [`docs/architecture/`](../../docs/architecture/directory-rules.md). This README relies only on their shared executable/declarative split and does not resolve their own authority or supersession conflict.

[Back to top](#top)

## Definition of done

### This README revision

- [x] Preserves the existing document ID, created date, guardrail role, and canonical-root split.
- [x] Identifies scope, audience, authority, repository fit, accepted content, exclusions, migration, validation, review, and rollback.
- [x] Replaces unbounded implementation implications with pinned repository evidence and explicit uncertainty.
- [x] Separates documentation, activation, execution, validation, receipts, release, and publication.
- [x] Adds an evidence ledger and correction triggers without creating a second authority.

### Compatibility lane maturity

- [ ] Named owners and reviewers are assigned.
- [ ] The complete directory, history, consumer, and external-reference inventory is verified.
- [ ] Parser and registry behavior explicitly excludes this path.
- [ ] Any misplaced content is migrated with tests, receipts, correction, and rollback evidence.
- [ ] Retention or retirement is decided and recorded.
- [ ] Any required ADR or drift entry is accepted and linked.
- [ ] Independent human review is complete.

Completing this README does not complete any executable, activation, lifecycle, evidence, policy, release, correction, rollback, or publication gate.

[Back to top](#top)

## Open verification register

| ID | Item | Status | Evidence needed |
|---|---|---|---|
| `PIPE-SPECS-001` | Named accountable owners | `NEEDS VERIFICATION` | Reviewed stewardship assignment; do not infer from placeholder roles. |
| `PIPE-SPECS-002` | Exhaustive path and history inventory | `UNKNOWN` | Pinned recursive tree plus relevant history and branch review. |
| `PIPE-SPECS-003` | Parser, registry, scheduler, workflow, and runtime references | `UNKNOWN` | Code-aware search, configuration inspection, tests, and owner confirmation. |
| `PIPE-SPECS-004` | External references or downstream consumers | `UNKNOWN` | Compatibility owner survey and migration inventory. |
| `PIPE-SPECS-005` | Automated misplaced-spec lint rule | `PROPOSED` | Accepted rule, safe workflow, negative fixtures, and current passing evidence. |
| `PIPE-SPECS-006` | Retain or retire this guardrail path | `NEEDS VERIFICATION` | Consumer inventory, owner decision, compatibility window, and rollback plan. |
| `PIPE-SPECS-007` | Directory Rules copy authority | `CONFLICTED` qualifier on `NEEDS VERIFICATION` | Accepted canonical-document/supersession decision; this README does not decide it. |
| `PIPE-SPECS-008` | Branch protection and required-check coupling | `UNKNOWN` | Repository ruleset and required-check inspection before merge. |

[Back to top](#top)

## Evidence ledger

Repository claims in this revision are bounded to `bartytime4life/Kansas-Frontier-Matrix@459b41d7ec91240742d8b2d3e5d9eb4dbd248df7` unless another ref is stated.

| Evidence | Status | Supports | Does not prove |
|---|---|---|---|
| Prior `pipelines/specs/README.md` blob `1314bf0fe34736e75f1a2d0900b049ebea2d87bd` | `CONFIRMED` | Existing guardrail role, canonical-root routing, migration intent, and retained open questions. | Exhaustive inventory, active enforcement, or retirement readiness. |
| [`pipelines/README.md`](../README.md) | `CONFIRMED` root documentation | Executable **how** responsibility and this lane's stated guardrail role. | That every described executable lane is implemented. |
| [`pipeline_specs/README.md`](../../pipeline_specs/README.md) blob `7f35f1c06aaec08d03182cf71e88a812bf179ebf` | `CONFIRMED` declarative-root documentation | Canonical **what** responsibility, mixed-maturity inventory, compatibility conflicts, and unestablished activation machinery. | Accepted schema, parser, active registry, runtime use, or production effect. |
| [Directory Rules](../../docs/doctrine/directory-rules.md) blob `2affb080e6f0043867c64c7f06c1ca52030fbd55` | `CONFIRMED` governing document at pinned ref | Responsibility-root placement, canonical split, no-parallel-authority rule, README burden, ADR triggers, and migration discipline. | Resolution of the doctrine-versus-architecture copy conflict or current implementation of every proposed path. |
| [`tests/pipelines/README.md`](../../tests/pipelines/README.md) | `CONFIRMED` test-boundary documentation | Intended pipeline behavior test burden and current dedicated-suite limitations. | A current passing test run or coverage of this path. |
| [`data/receipts/pipeline/README.md`](../../data/receipts/pipeline/README.md) | `CONFIRMED` receipt-lane documentation | Pipeline receipts belong under `data/receipts/` and remain process memory. | Receipt emission for any spec or pipeline run. |
| [`data/receipts/generated/README.md`](../../data/receipts/generated/README.md) and current schema | `CONFIRMED` provenance lane and shape | AI-authored documentation receipt requirements and non-authoritative receipt posture. | Human approval, factual correctness, mergeability, release, or publication. |
| [Workflow README](../../.github/workflows/README.md) | `CONFIRMED` bounded workflow inventory | Broad PR workflows may run for documentation changes; names do not prove substantive checks. | Current run results, branch-protection requirements, or privileged settings not exposed by the file. |
| [Drift register](../../docs/registers/DRIFT_REGISTER.md) blob `97a775522dcd058299f752ac7862d0fc56c13280` | `CONFIRMED` register surface | Correct place to record a verified placement or authority conflict. | Absence of unregistered drift or complete pipeline-spec coverage. |

### Evidence limits

The GitHub connector exposed exact file reads, repository metadata, branch and pull-request searches, commits, comparisons, and writes. It did not establish a complete mounted-tree inventory, dynamic parser behavior, external consumers, branch-protection policy, runtime logs, deployment state, or production effects for this documentation task. Those claims remain `UNKNOWN` or `NEEDS VERIFICATION`.

[Back to top](#top)

## Change history

### v0.2 — 2026-07-22

- retained the compatibility guardrail and canonical `pipeline_specs/` routing;
- added a commit-pinned evidence and authority boundary;
- distinguished confirmed repository documentation from unverified parser, consumer, enforcement, and runtime behavior;
- added admission, exclusion, discovery, migration, security, validation, review, drift, evidence, correction, and rollback guidance; and
- separated README completion from compatibility-lane maturity.

### v0.1 — 2026-06-13

- established the guardrail path;
- documented the `pipelines/` versus `pipeline_specs/` responsibility split; and
- recorded initial migration questions.

## Correction and rollback

Correct this README when:

- an accepted ADR changes the `pipelines/` and `pipeline_specs/` split;
- a parser, consumer, registry, scheduler, workflow, test, or lint rule begins using or enforcing this path;
- non-guardrail content is found, migrated, or retired;
- the canonical spec schema, activation contract, receipt binding, or test boundary becomes established;
- the Directory Rules copy conflict is resolved;
- named owners or a retain/retire decision are approved; or
- any evidence-ledger statement stops matching the repository.

Before merge, rollback means closing the draft pull request and abandoning the scoped branch. After merge, create a transparent revert of the documentation and generated-receipt commits, restore the prior README blob, and re-run the same documentation and receipt validations. Do not force-push shared history.

Reverting this README changes documentation only. It does not move a spec, deactivate a consumer, alter executable behavior, undo a lifecycle transition, correct evidence, revoke policy, withdraw a release, or change a public artifact. Any such operational effect requires its own governed correction or rollback process.

[Back to top](#top)
