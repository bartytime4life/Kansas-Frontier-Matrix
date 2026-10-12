<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-validate-readme
title: pipelines/validate/ - Shared Pipeline Validation Orchestration Boundary
type: readme; directory-readme; executable-lane-contract; validation-orchestration-boundary
version: v0.2
status: draft; repository-grounded; placeholder-only-executable; aggregate-validator-wiring-exists-elsewhere; no-active-shared-validate-pipeline-established
owners: OWNER_TBD - Pipeline steward · Validation steward · Domain stewards · Contract/schema steward · Evidence steward · Policy steward · Receipt steward · Release steward · Security reviewer · CI steward · Docs steward
created: 2026-06-13
updated: 2026-07-22
policy_label: public-documentation; executable-boundary; fail-closed; cite-or-abstain; no-direct-promotion; no-direct-publication
current_path: pipelines/validate/README.md
owning_root: pipelines/
responsibility: shared executable orchestration for a governed pipeline validation stage, if and when implemented; not validator-library, declarative-specification, schema, contract, policy, canonical-data, evidence, proof, review, receipt, release, or public-serving authority
truth_posture: CONFIRMED target v0.1 README, one-line placeholder main.py, active Makefile aggregate validation wiring, six fixture-backed validators selected by tools/validators/_common/run_all.py, README-only direct tests/pipelines lane, one empty-stage archaeology validate spec, checked absence of shared validate spec/test/fixture README paths, domain validation documentation, and non-publisher boundary test at the pinned snapshot / PROPOSED shared stage interface, caller protocol, accepted ValidationReport and receipt families, lifecycle writer, deterministic fixtures, dedicated tests, CI, correction cascade, and rollback integration / CONFLICTED two live Directory Rules editions and stale workflow inventory details, without conflict on the pipelines-versus-pipeline_specs root split / UNKNOWN complete recursive inventory, branch-local or external consumers, generated or ignored files, deployed behavior, current workflow conclusions, branch-protection requirements, and production use / NEEDS VERIFICATION named owners, canonical report and reason-code contracts, active spec discovery, validator registry, domain-adapter protocol, receipt home, promotion integration, and implementation graduation
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: d24c7bf9ee89c9bb3bd2cd14e0e60b1de6314bc0
  prior_blob: e6ed7beb4eb61b136ca830dc590d1a8574fa72af
  inspection_method: commit-pinned GitHub connector reads, exact-path checks, bounded repository code search, and supplied PDF extraction plus visual inspection for placement doctrine
related:
  - ../README.md
  - main.py
  - ../domains/README.md
  - ../domains/archaeology/validate/README.md
  - ../../pipeline_specs/README.md
  - ../../pipeline_specs/archaeology/validate.yaml
  - ../../tools/validators/README.md
  - ../../tools/validators/_common/run_all.py
  - ../../tests/pipelines/README.md
  - ../../tests/policy/test_pipeline_connector_non_publisher.py
  - ../../Makefile
  - ../../data/receipts/generated/README.md
  - ../../schemas/contracts/v1/receipts/generated_receipt.schema.json
  - ../../docs/architecture/directory-rules.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/doctrine/lifecycle-law.md
  - ../../docs/registers/DRIFT_REGISTER.md
  - ../../docs/adr/ADR-0018-promotion-gate-sequence.md
  - ../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../../.github/workflows/README.md
  - ../../.github/PULL_REQUEST_TEMPLATE.md
tags: [kfm, pipelines, validate, validation-orchestration, fail-closed, lifecycle, quarantine, evidence-ref, policy, receipts, correction, rollback, no-publication]
notes:
  - "v0.2 preserves the v0.1 placement, anti-collapse, lifecycle, evidence, policy, receipt, quarantine, correction, rollback, and no-direct-publication obligations while replacing a proposed helper tree with a commit-pinned current-state boundary."
  - "pipelines/validate/main.py is a single greenfield-placeholder comment; it defines no import, function, class, command, input, output, report, receipt, or failure contract."
  - "The repository's implemented make validate path runs tools/validators/_common/run_all.py and schema/contract tests; it does not call pipelines/validate/main.py and must not be represented as this pipeline lane."
  - "No pipeline_specs/validate/README.md, tests/pipelines/validate/README.md, or fixtures/validate/README.md was present at the checked paths."
  - "This documentation-only revision does not activate a source, validator, pipeline, spec, policy, lifecycle transition, quarantine write, receipt emitter, release path, API, UI, deployment, or publication."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `pipelines/validate/` - Shared Pipeline Validation Orchestration Boundary

> Repository-grounded boundary for shared executable orchestration of a governed pipeline validation stage. The lane is correctly placed under `pipelines/`, but its inspected Python entrypoint is still a one-line greenfield placeholder. No active shared validation pipeline is established by the current files.

![status](https://img.shields.io/badge/status-draft-yellow)
![implementation](https://img.shields.io/badge/implementation-placeholder-lightgrey)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![posture](https://img.shields.io/badge/posture-fail--closed-d62728)
![publication](https://img.shields.io/badge/direct%20publication-denied-d62728)

> [!IMPORTANT]
> A validation pass is bounded evidence about checks that actually ran against identified inputs. It is not an `EvidenceBundle`, policy decision, human approval, lifecycle promotion, catalog closure, release decision, or public claim.

> [!WARNING]
> Do not treat [`main.py`](main.py), the proposed tree in the prior README, `make validate`, a green check, or a successful merge as proof that this shared pipeline stage exists. At the pinned snapshot, the shared entrypoint is only a comment; the implemented aggregate validator command lives under `tools/validators/` and tests.

**Quick navigation:** [Purpose](#purpose) · [Status](#status-and-evidence-boundary) · [Authority](#authority-boundary) · [Current state](#confirmed-current-state) · [Placement](#placement-and-repository-fit) · [Lifecycle](#lifecycle-and-operating-boundary) · [Contract](#validation-stage-contract-before-implementation) · [Outcomes](#finite-outcomes-and-failure-behavior) · [I/O](#inputs-outputs-and-side-effects) · [Trust](#source-evidence-policy-and-sensitivity) · [Tests](#tests-fixtures-receipts-and-ci) · [Security](#security-and-publication-boundaries) · [Review](#review-correction-and-rollback) · [No loss](#no-loss-preservation) · [Done](#definition-of-done) · [Open](#open-verification-backlog) · [Evidence](#evidence-ledger)

---

## Purpose

`pipelines/validate/` is reserved for executable orchestration that is genuinely shared across domain pipelines and evaluates identified candidate records at a named lifecycle boundary.

If implemented, this lane may coordinate:

- accepted reusable validators from [`tools/validators/`](../../tools/validators/README.md);
- domain-owned checks supplied through explicit adapters;
- contract and schema validation against pinned versions;
- lifecycle-state, source-role, evidence, policy, review, and receipt preconditions;
- deterministic finite outcomes and reason codes;
- validation-report candidate construction;
- quarantine or hold recommendations returned to the owning domain pipeline;
- no-network fixture execution and deterministic replay; and
- auditable handoff to a separately governed promotion decision.

It does not own the validators' semantic rules, the meaning or shape of domain objects, source admission, policy decisions, evidence, human review, lifecycle state, promotion, release, or public delivery.

### Audience

This README is for pipeline and domain maintainers, validator authors, contract/schema stewards, evidence and receipt reviewers, policy and sensitivity reviewers, CI maintainers, release stewards, and agents deciding where validation-related work belongs.

### Non-goals of this revision

This revision does not:

- implement or activate the shared validation stage;
- define a `ValidationReport`, reason-code, quarantine, or validation-receipt schema;
- create a shared declarative validation spec;
- move validator code out of `tools/validators/` or domain lanes;
- add fixtures, tests, workflows, Make targets, lifecycle writers, or release gates;
- approve either live Directory Rules copy as the sole canonical edition;
- change any source, contract, schema, policy, data, receipt, proof, catalog, release, runtime, or public artifact; or
- resolve open architecture decisions through README prose.

[Back to top](#top)

---

## Status and evidence boundary

### Safe conclusion

The directory is an accepted executable-logic location in KFM placement doctrine, but its shared implementation is a placeholder. The repository has a separate, implemented aggregate validation command under `tools/validators/` and tests. This README defines the boundary a future pipeline-stage implementation must satisfy; it does not certify that the stage exists.

| Surface | Evidence at `main@d24c7bf9` | Status |
|---|---|---|
| This README | Existing v0.1 governance draft. | **CONFIRMED** |
| [`main.py`](main.py) | One comment: `validate stage - greenfield placeholder`. | **CONFIRMED placeholder** |
| Shared functions, classes, imports, CLI, or package API | None in the opened entrypoint. | **NOT ESTABLISHED** |
| Shared declarative validation lane | `pipeline_specs/validate/README.md` returned not found. | **NOT FOUND AT CHECKED PATH** |
| Dedicated shared tests | `tests/pipelines/validate/README.md` returned not found. | **NOT FOUND AT CHECKED PATH** |
| Dedicated shared fixtures | `fixtures/validate/README.md` returned not found. | **NOT FOUND AT CHECKED PATH** |
| Parent pipeline test boundary | [`tests/pipelines/README.md`](../../tests/pipelines/README.md) is the only confirmed direct file in its own bounded inventory. | **CONFIRMED documentation; dedicated suite not established** |
| Repository aggregate validation | [`make validate`](../../Makefile) calls `make schemas` and `make test`. | **CONFIRMED command wiring** |
| Shared validator runner | [`tools/validators/_common/run_all.py`](../../tools/validators/_common/run_all.py) selects six fixture-backed validator scripts and stops on the first non-zero result. | **CONFIRMED executable wiring; current run result not established here** |
| Domain validation example | Archaeology has a validation README and an empty-stage [`validate.yaml`](../../pipeline_specs/archaeology/validate.yaml). | **CONFIRMED documentation and scaffold; active behavior not established** |
| Direct-publication guard | [`test_pipeline_connector_non_publisher.py`](../../tests/policy/test_pipeline_connector_non_publisher.py) scans connector and pipeline files for nearby write calls targeting catalog, published, or release paths. | **CONFIRMED bounded static test** |
| Dedicated shared stage workflow or check | No dedicated command or workflow was established by the bounded reads and searches. | **UNKNOWN / NEEDS VERIFICATION** |
| Runtime, deployed consumer, receipt instance, or promotion dependency | Not established by source inspection. | **UNKNOWN** |

### Truth labels

| Label | Meaning here |
|---|---|
| **CONFIRMED** | Verified from commit-pinned repository content, supplied doctrine, or generated validation output in this work. |
| **PROPOSED** | A future interface, rule, path, or implementation obligation not established as active. |
| **UNKNOWN** | Available evidence does not establish the claim strongly enough. |
| **NEEDS VERIFICATION** | A specific repository, governance, test, runtime, or release check remains open. |

`CONFLICTED` qualifies the two live Directory Rules editions and stale workflow-inventory details; it does not replace a core truth label. Both Directory Rules copies agree on the `pipelines/` versus `pipeline_specs/` responsibility split.

Bounded absence is not historical or global absence. Branch-local files, ignored or generated artifacts, external services, unindexed content, and later commits were not exhaustively inspected.

[Back to top](#top)

---

## Authority boundary

`pipelines/validate/` may eventually own shared executable **stage orchestration** only.

| Concern | Owning responsibility | This lane's role |
|---|---|---|
| Shared pipeline-stage orchestration | `pipelines/validate/` | Coordinate accepted checks only after code, interface, tests, and receipts exist. |
| Reusable validators and checkers | [`tools/validators/`](../../tools/validators/README.md) | Invoke pinned validator IDs or interfaces; do not duplicate their implementation. |
| Domain-specific validation meaning | Domain contracts, policy, and `pipelines/domains/<domain>/` | Consume explicit domain adapters without transferring domain authority. |
| Declarative run intent | [`pipeline_specs/`](../../pipeline_specs/README.md) | Read an accepted spec; do not embed a parallel configuration store. |
| Semantic meaning and invariants | `contracts/` | Implement accepted meaning; do not redefine it in code or this README. |
| Machine-checkable shape | `schemas/` | Validate against accepted versions; do not invent schemas here. |
| Admissibility, rights, sensitivity, access | `policy/` | Enforce resolved decisions and fail closed; do not decide policy here. |
| Expected behavior | `tests/` and `fixtures/` | Consume deterministic cases; do not store fixtures beside production code. |
| Lifecycle records and quarantine | `data/` through accepted writers | Return candidates or requested dispositions; do not mutate state by path alone. |
| Evidence and proof | `data/proofs/` and accepted evidence contracts | Resolve and preserve references; never fabricate or replace support. |
| Process receipts | `data/receipts/` | Emit through accepted schemas and writers; receipts remain process memory. |
| Promotion, release, correction, rollback | `release/` and accepted governance | Supply a reviewable handoff; never approve or publish. |
| Public API, UI, map, search, export, or AI | Governed applications and released artifacts | No direct consumer access to this source lane or unreleased outputs. |

### Anti-collapse rules

The following equivalences are always invalid:

```text
schema-valid == semantically valid
validator pass == evidence closure
ValidationReport == EvidenceBundle
validation receipt == proof
policy check executed == policy ALLOW
all checks passed == human approval
processed-ready == lifecycle promotion
quarantine recommendation == lifecycle write authority
pipeline completion == catalog closure
green CI == release approval
merge == KFM publication
generated validation summary == evidence
```

A valid report remains scoped to its declared inputs, checks, versions, and time. It must not be reused as general truth after those bounds change.

[Back to top](#top)

---

## Confirmed current state

### Shared lane

The checked shared implementation surface is:

```text
pipelines/validate/
├── README.md    # this boundary document
└── main.py      # one-line greenfield placeholder
```

The entrypoint contains no executable statement, import, function, class, command parser, validator registry, input reader, output writer, receipt emitter, policy call, evidence resolver, quarantine router, or failure behavior.

### Aggregate repository validation is a different surface

The root [`Makefile`](../../Makefile) defines:

```text
make validate
  -> make schemas
       -> python tools/validators/_common/run_all.py
  -> make test
       -> pytest tests/schemas tests/contracts -q
```

The shared validator runner invokes these fixture modes in order:

1. source descriptor;
2. evidence reference;
3. evidence bundle;
4. runtime response envelope;
5. decision envelope; and
6. run receipt.

The runner returns the first non-zero subprocess result. This is real command wiring, but it is not evidence that every validator exists for every domain, that current execution passes, or that `pipelines/validate/main.py` participates.

### Domain validation is not shared validation

[`pipelines/domains/archaeology/validate/README.md`](../domains/archaeology/validate/README.md) documents an Archaeology-specific validation boundary. Its referenced [`pipeline_specs/archaeology/validate.yaml`](../../pipeline_specs/archaeology/validate.yaml) contains `stages: []`.

That pair establishes planned naming and a domain-specific documentation surface. It does not establish an active shared stage, an accepted adapter protocol, or executable Archaeology validation.

### Documentation and workflow drift

Two Directory Rules files are live:

- [`docs/architecture/directory-rules.md`](../../docs/architecture/directory-rules.md), version 1.3.1; and
- [`docs/doctrine/directory-rules.md`](../../docs/doctrine/directory-rules.md), version 1.4 presentation refresh.

Their self-described canonical relationship remains unresolved. Both place executable logic under `pipelines/`, declarative configuration under `pipeline_specs/`, reusable validators under `tools/validators/`, behavior proof under `tests/`, and controlled examples under `fixtures/`.

The [workflow inventory](../../.github/workflows/README.md) is also snapshot-bounded and contains details that can become stale as workflow files change. This README therefore cites current command wiring directly and leaves current run conclusions and required-check status open.

[Back to top](#top)

---

## Placement and repository fit

The supplied Directory Rules and both repository editions assign:

```text
pipelines/       executable pipeline logic - HOW a governed stage runs
pipeline_specs/  declarative pipeline configuration - WHAT should run
tools/validators reusable validators and checkers
tests/           executable behavior proof
fixtures/        controlled valid, invalid, denied, held, and error cases
data/            lifecycle records, receipts, proofs, catalogs, and artifacts
release/         promotion, correction, withdrawal, and rollback decisions
```

That makes the existing `pipelines/validate/` location appropriate for shared **orchestration**. It does not make all validation-related code appropriate here.

### Admission test

A future file belongs here only when all are true:

1. its primary responsibility is executable orchestration of a validation stage;
2. at least two accepted domain consumers need the shared mechanics, or an accepted decision establishes shared ownership;
3. validator logic remains in its owning reusable or domain lane;
4. meaning, shape, policy, evidence, review, lifecycle, receipt, and release authority remain external;
5. it consumes accepted declarative configuration instead of becoming a hidden spec store;
6. it returns finite, deterministic, scope-bound outcomes;
7. side effects occur only through accepted report, receipt, or lifecycle-writer interfaces;
8. positive and negative fixtures can prove the behavior without live sources; and
9. correction, invalidation, retry, cancellation, and rollback effects are explicit.

If a checker is reusable outside pipeline orchestration, place it under `tools/validators/` or an accepted package. If behavior is domain-specific, keep it in that domain's pipeline lane. If it stores a record or decides admissibility, route it to the owning authority root.

### Files that do not belong here

- reusable validator implementations or a second validator registry;
- declarative YAML or JSON run profiles;
- semantic contracts, JSON Schemas, vocabularies, or policy rules;
- source descriptors, connectors, credentials, or source-admission decisions;
- raw, work, quarantine, processed, catalog, triplet, or published data;
- EvidenceBundles, ProofPacks, policy decisions, review records, or release manifests;
- fixtures, tests, generated reports, dashboards, or workflow definitions;
- API, UI, MapLibre, search, Focus Mode, export, or AI-serving code; and
- secrets, restricted payloads, living-person data, or exact sensitive locations.

No ADR is required for this in-place documentation clarification. An ADR or accepted migration decision is required before changing a canonical root, creating parallel authority, changing lifecycle or promotion semantics, or establishing a privileged public path.

[Back to top](#top)

---

## Lifecycle and operating boundary

Shared validation orchestration must preserve:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Validation usually evaluates a named candidate and returns a disposition to the caller. It is not the state transition itself.

| Stage concern | Permitted role for a future shared runner | Forbidden shortcut |
|---|---|---|
| Input admission | Accept pinned fixture, WORK, or approved recheck references from an authorized caller. | Fetch sources or admit arbitrary inputs. |
| Validation | Run declared checks against pinned contracts, schemas, policy inputs, and validator versions. | Select hidden checks or infer missing authority. |
| Reporting | Return a complete, bounded result with checks, versions, outcomes, and reasons. | Emit an unqualified boolean or discard failures. |
| Quarantine | Recommend or request a structured hold through an accepted interface. | Move or relabel data merely because a check failed. |
| Promotion | Supply a readiness candidate and supporting receipt references. | Write to PROCESSED or later phases directly. |
| Review | Preserve human-review state and required reviewer classes. | Self-approve or infer approval from merge state. |
| Release | Provide immutable inputs, outputs, digests, and blockers. | Create a release decision or publish. |
| Correction | Re-evaluate affected candidates and emit invalidation or supersession requests. | Delete or silently overwrite prior reports or released meaning. |

### Caller ownership

A future call must identify the owning domain or approved cross-domain lane, requested lifecycle boundary, input refs and hashes, spec/profile refs, validator set, evidence and policy context, and expected output class. Filesystem location alone is not authorization.

### Idempotency and retries

The same pinned inputs, code, validator set, contracts, schemas, policy bundle, and parameters should produce the same material outcome or an explicitly bounded variance. A retry must not duplicate quarantine records, reports, or receipts, and cancellation must leave partial output non-public and recoverable.

[Back to top](#top)

---

## Validation-stage contract before implementation

The v0.1 README proposed a helper tree. No accepted shared interface or active directory shape was verified, so v0.2 retains the obligations without presenting speculative filenames as current structure.

Before code graduates beyond the placeholder, accepted contracts must define at least:

| Concern | Required decision | Why it matters |
|---|---|---|
| Stage identity | Stable component ID, version, implementation digest, and owner. | Reproducibility and review routing. |
| Caller scope | Domain/cross-domain owner and authorized lifecycle boundary. | Prevent ownerless validation. |
| Input contract | Allowed refs, lifecycle states, hashes, schemas, and immutability rules. | Prevent raw or ambiguous input laundering. |
| Spec binding | Accepted spec ID/version/hash and activation state. | Prevent hidden configuration. |
| Validator set | Stable validator IDs, versions, order, dependencies, and required/optional state. | Make coverage inspectable. |
| Contract/schema binding | Exact semantic and machine-shape versions. | Prevent schema drift and semantic substitution. |
| Evidence | `EvidenceRef` resolution requirements and abstention behavior. | Cite-or-abstain compliance. |
| Source role | Source IDs, roles, rights, vintage, and citation requirements. | Prevent source-role collapse. |
| Time | Observation, valid, retrieval, processing, validation, release, and correction times as applicable. | Prevent temporal collapse. |
| Policy | Bundle/version, decision refs, sensitivity, rights, access, and obligations. | Fail-closed handling. |
| Review | Required reviewer classes and review-state input. | Separation of duties. |
| Outcome | Finite status and stable reason-code vocabulary. | No silent or ambiguous success. |
| Report | Complete checks, failures, warnings, skipped checks, scope, and hashes. | Auditable handoff. |
| Receipt | Accepted family, schema, writer, and artifact binding. | Process memory without proof inflation. |
| Side effects | Allowed report/receipt/lifecycle interfaces and transaction boundary. | Prevent direct path mutation. |
| Correction | Revalidation triggers, affected-reference discovery, supersession, and invalidation. | No stale validation authority. |
| Rollback | Last-known-good code/spec/validator/policy combination and recovery procedure. | Reversibility. |

The semantic contract belongs under `contracts/`; machine shape under `schemas/`; admissibility under `policy/`; run intent under `pipeline_specs/`; validator implementation under `tools/validators/` or an accepted domain lane. This pipeline lane may orchestrate those decisions after they are accepted.

### Report integrity

A future report must say exactly what ran and what did not run. It should bind:

- candidate and caller identifiers;
- input refs and content hashes;
- component, spec, contract, schema, validator, policy, and tool versions;
- each check's finite outcome, reason code, and relevant evidence refs;
- required checks that were skipped, unavailable, stale, or not applicable;
- proposed disposition without impersonating lifecycle authority;
- report and receipt hashes; and
- correction, expiry, and revalidation triggers.

Warnings must not be silently converted into readiness. A missing required check is not a pass.

[Back to top](#top)

---

## Finite outcomes and failure behavior

The accepted enum and reason-code schema remain open. Behavior must nevertheless distinguish at least:

- candidate ready for the next named review or promotion gate;
- no-op because pinned inputs produce no material validation delta;
- abstention because evidence or scope is insufficient;
- denial because policy, rights, sensitivity, or access forbids the operation;
- hold or quarantine request because review, identity, schema, provenance, freshness, or ownership is unresolved;
- validation failure because declared checks found a defect; and
- system error because execution, dependency, integrity, or receipt writing failed.

Until a contract freezes exact names, these are behavioral classes, not a normative machine enum.

### Fail-closed conditions

A future implementation must refuse readiness when any required item is missing, stale, inconsistent, or unverifiable, including:

- caller identity or ownership;
- allowed input lifecycle state;
- input hash or immutable reference;
- accepted spec, contract, or schema version;
- required validator or negative control;
- source identity, role, rights, or citation state;
- evidence support or required `EvidenceBundle` resolution;
- policy bundle, sensitivity, access, or obligation result;
- required time/freshness fields;
- human review state;
- report or receipt integrity;
- correction, expiry, or affected-reference linkage; or
- release-aware rollback target when the result can influence released material.

Partial output must remain non-public, identified as incomplete, and safe to retry. The runner must preserve the first failure and any later diagnostic failures without masking the governing outcome.

[Back to top](#top)

---

## Inputs, outputs, and side effects

### Inputs

Future shared orchestration may accept only explicit, immutable references supplied by an authorized caller, such as:

- synthetic/public-safe fixture refs;
- WORK candidate refs or approved recheck refs;
- caller and domain identity;
- activated spec/profile ref and digest;
- contract and schema refs;
- validator-set ref and versions;
- source descriptors, source roles, rights, and citation refs;
- evidence refs and required evidence-resolution results;
- policy inputs, bundle/version, and prior decisions;
- review state and required reviewer classes; and
- prior reports, receipts, correction notices, or rollback targets relevant to revalidation.

The runner must not discover authority from ambient files, environment state, branch names, or prose.

### Outputs

Future outputs may include, through accepted contracts:

- a validation-report candidate;
- per-check structured outcomes and reason codes;
- readiness, abstention, denial, hold, quarantine-request, no-op, or error disposition;
- an accepted validation/run receipt candidate;
- affected-reference and correction-impact records; and
- a handoff to the owning domain or promotion workflow.

### Side-effect boundary

The safe default is pure evaluation plus a controlled result. If report or receipt persistence is required, use an accepted writer with an explicit transaction boundary. The runner must not:

- rename or move lifecycle files as promotion;
- write directly to catalog, triplet, published, or release paths;
- change source registry, evidence, policy, review, or release state;
- overwrite prior reports in place;
- call public APIs or UI backends as a storage route; or
- log candidate payloads or sensitive values merely for diagnostics.

[Back to top](#top)

---

## Source, evidence, policy, and sensitivity

### Source-role discipline

- Preserve stable source identity and role through every check.
- Do not collapse primary, corroborating, contextual, or restricted roles.
- Do not let source count substitute for authority or independent corroboration.
- Carry rights, terms, attribution, vintage, retrieval time, and payload hashes where required.
- Treat unknown or conflicting source state as a blocker, not a warning-only success.

### Evidence discipline

- `EvidenceRef` is a reference, not an `EvidenceBundle`.
- Validation may check that required evidence resolves; it does not create truth by doing so.
- Evidence scope must match the candidate, spatial/temporal scope, and claim significance.
- Generated text, dashboards, maps, graph edges, logs, and reports are not evidence merely because they are inspectable.
- A correction or withdrawal of supporting evidence must trigger bounded revalidation and downstream impact analysis.

### Policy and sensitivity discipline

- Policy decisions remain external inputs or separately governed outputs.
- Unknown rights, sovereignty, consent, sensitivity, access, or redistribution state fails closed.
- A validator must not encode hidden policy thresholds that belong in policy authority.
- Generalization, redaction, aggregation, or delay must be bound to accepted policy and transform receipts.
- Public-safe validation fixtures must not contain reconstructive sensitive detail.

[Back to top](#top)

---

## Tests, fixtures, receipts, and CI

### Current boundary

No dedicated shared validation spec, fixture README, test README, or pipeline-stage command was found at the checked paths. The parent [`tests/pipelines/README.md`](../../tests/pipelines/README.md) documents a README-only direct lane at its evidence snapshot.

The repository does have executable aggregate schema validation and contract/schema tests. Those surfaces prove only their declared scopes and do not establish the shared pipeline stage.

### Graduation proof burden

Before [`main.py`](main.py) becomes active, deterministic positive and negative coverage should include:

- one valid synthetic/public-safe candidate;
- unknown caller or domain ownership;
- disallowed lifecycle input;
- missing or mismatched input hash;
- absent, inactive, malformed, or stale spec;
- contract/schema disagreement;
- unavailable, skipped, duplicated, or reordered required validator;
- invalid source descriptor or collapsed source role;
- unresolved or mismatched evidence support;
- missing or stale policy bundle/decision;
- rights, sovereignty, consent, or sensitivity denial;
- living-person, DNA/genomic, archaeology/cultural, rare-species, private-land, or infrastructure exposure;
- temporal-field collapse or stale support;
- review-required state presented as ready;
- report/receipt write failure or hash mismatch;
- direct write to catalog, triplet, published, release, API, or UI paths;
- deterministic replay and repeated-run no-op;
- cancellation and partial-output cleanup;
- correction-driven revalidation and invalidation; and
- rollback to the last known-good code/spec/validator/policy combination.

Fixtures should be synthetic, minimal, no-network, public-safe, and independently reviewable. A fixture is test input, not evidence for a real-world claim.

### Receipt discipline

A validation or run receipt records process memory: inputs, versions, checks, outcomes, hashes, and references. It is not an `EvidenceBundle`, proof, policy decision, review approval, promotion receipt, or release manifest.

The exact accepted receipt family and instance home for this shared stage remain **NEEDS VERIFICATION**. Do not infer a canonical path from the v0.1 proposal or create a parallel receipt authority from this README.

This AI-authored documentation change separately requires a [`GENERATED_RECEIPT`](../../data/receipts/generated/README.md) conforming to the [generated-receipt schema](../../schemas/contracts/v1/receipts/generated_receipt.schema.json). That receipt proves provenance of the edit, not validation-stage implementation or correctness.

### CI boundary

A future workflow should call a repository-owned command, declare explicit least-privilege permissions, use hosted runners unless a separately reviewed need exists, and fail visibly on negative controls. It must not embed a second implementation in YAML, run untrusted pull-request code with privileged credentials, upload sensitive candidate data, or treat workflow success as promotion or release approval.

The current [workflow inventory](../../.github/workflows/README.md) reports broad pull-request checks and snapshot-bounded maturity. Current run results, required-check coupling, and a validation-stage-specific workflow remain **UNKNOWN** here.

### README-only validation

This documentation revision should prove:

- one H1 and one closed KFM Meta Block;
- balanced fenced blocks and unique GitHub anchors;
- repository-relative links resolve at the pinned or proposed head;
- current implementation claims match exact opened files;
- `make validate` and `pipelines/validate/` are not conflated;
- no speculative helper tree is presented as current shape;
- no loss of v0.1 placement, anti-collapse, lifecycle, evidence, policy, receipt, correction, rollback, and no-publication controls;
- no secret, restricted payload, or sensitive location is introduced; and
- a schema-valid generated-work receipt binds the README content hash.

[Back to top](#top)

---

## Security and publication boundaries

Validation commonly touches the exact material that public systems must not expose. Logs, reports, fixtures, receipts, CI artifacts, and error messages therefore need the same sensitivity discipline as inputs.

High-risk classes include:

- living-person, genealogy, DNA/genomic, kinship, address, or private-contact data;
- archaeology, burial, sacred, cultural, tribal, or repatriation-sensitive information;
- rare species, collection, nest, den, migration, or exact habitat locations;
- critical infrastructure, facility dependencies, access routes, vulnerabilities, or operational state;
- private-land ownership, access, easement, occupancy, or dispute information;
- source-restricted identifiers, private URLs, joins, and redistribution-limited fields; and
- combinations that create a sensitive inference absent from each input alone.

Required posture:

- deny or hold unknown rights, consent, sovereignty, sensitivity, or access state;
- minimize candidate content in logs and diagnostics;
- keep exact sensitive values out of pull requests, CI summaries, receipts, and public fixtures;
- separate internal validation detail from public-safe explanations;
- record redaction/generalization transforms and reasons through accepted artifacts;
- re-evaluate downstream products after correction, policy change, or source withdrawal; and
- keep public clients behind governed interfaces and released, policy-filtered artifacts.

The bounded static test at [`tests/policy/test_pipeline_connector_non_publisher.py`](../../tests/policy/test_pipeline_connector_non_publisher.py) rejects certain nearby write-call/target patterns in pipeline and connector files. It is a useful guard, not a complete data-flow, runtime, indirect-write, or publication proof.

This README contains no candidate payload or sensitive operational detail and changes no access boundary.

[Back to top](#top)

---

## Review, correction, and rollback

### Review burden

Future executable changes require review from owners of the responsibilities actually affected: pipeline orchestration, domain meaning, validator implementation, contract/schema, evidence, source role, policy/sensitivity, receipts, tests/CI, lifecycle/promotion, release, security, and documentation.

[`CODEOWNERS`](../../.github/CODEOWNERS) routes `pipelines/`, `tools/validators/`, `pipeline_specs/`, and `data/receipts/` to `@bartytime4life` at the pinned snapshot. That routing does not prove independent stewardship assignment, semantic approval, policy approval, evidence closure, or release approval.

### Promotion and release boundary

The safe conceptual flow is:

```text
authorized caller + pinned candidate/spec/context
  -> shared orchestration invokes accepted validators
  -> bounded report + disposition + receipt candidate
  -> owning domain and review gates
  -> separately governed promotion decision
  -> catalog/triplet closure and release gates
  -> released public-safe artifact through governed interfaces
```

[`ADR-0018`](../../docs/adr/ADR-0018-promotion-gate-sequence.md) describes a proposed promotion sequence, and [`ADR-0011`](../../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md) describes proposed artifact-family separation. Both are `proposed`, not accepted, at the pinned snapshot. They may inform review but do not establish active behavior.

### Correction and revalidation

A correction, source withdrawal, policy change, schema/contract update, validator change, evidence change, or material freshness event must not silently leave a prior validation result authoritative. An accepted design should record:

1. the invalidating event and affected refs;
2. prior report and receipt identifiers;
3. revalidation scope and pinned replacements;
4. superseded, withdrawn, or still-valid outcomes;
5. downstream catalog, triplet, release, API, map, export, and cache impacts; and
6. reviewer and notification obligations without disclosing sensitive detail.

### Rollback

For this documentation-only revision, rollback is a transparent revert of the implementation or merge commit followed by Markdown/link/receipt validation. Do not rewrite shared history.

For future executable work, rollback must identify the last-known-good code, spec, contract, schema, validator set, policy bundle, fixture set, and report/receipt compatibility. Reverting code does not erase previously emitted reports or released artifacts; correction and withdrawal remain separate governed actions.

[Back to top](#top)

---

## No-loss preservation

This v0.2 revision preserves the v0.1 document's material obligations while grounding its implementation claims.

| v0.1 substance | v0.2 treatment |
|---|---|
| `pipelines/` owns executable logic; `pipeline_specs/` owns declarative intent. | **Retained and grounded** in both live Directory Rules editions and parent READMEs. |
| Shared validation must not replace domain validators. | **Retained and clarified** through the orchestration-versus-domain boundary. |
| Validation pass is not evidence, approval, promotion, catalog truth, or publication. | **Retained and expanded** into explicit anti-collapse rules. |
| Lifecycle, source-role, evidence, review, receipt, quarantine, and no-direct-publish gates. | **Retained** with caller, version, finite-outcome, retry, correction, and side-effect requirements. |
| Proposed helper tree. | **Removed as current shape**; obligations remain in the graduation contract because only `README.md` and placeholder `main.py` were established. |
| Proposed `pipeline_specs/validate/`, tests, and fixtures homes. | **Narrowed** to checked absence plus future placement requiring accepted contracts and evidence. |
| ValidationReport and receipt output ideas. | **Retained as proposed families** without asserting an accepted schema or instance home. |
| Definition of done and six open questions. | **Expanded** into implementation graduation, documentation acceptance, and an evidence-backed verification backlog. |
| Maintainer warning to start fixture-first and avoid publication shortcuts. | **Retained** across tests, security, side-effect, and review sections. |

No existing stable `doc_id`, created date, lifecycle invariant, or trust boundary was removed. Headings were reorganized because the prior eleven-section outline could not distinguish the real aggregate validator surface from the placeholder pipeline lane; all material governance meaning is carried forward.

[Back to top](#top)

---

## Definition of done

### This README revision

This revision is review-ready when:

- [ ] the exact base commit and prior blob are recorded;
- [ ] the shared placeholder and separate aggregate validator wiring are accurately described;
- [ ] links and internal anchors resolve;
- [ ] the v0.1 no-loss assessment remains accurate;
- [ ] no current implementation, CI, promotion, or publication claim outruns evidence;
- [ ] sensitive and public-interface boundaries remain fail closed;
- [ ] the generated receipt validates and binds the final README hash;
- [ ] the remote branch bytes and exact changed-path set match the prepared artifacts;
- [ ] the draft pull request records pending human review and current checks separately; and
- [ ] nothing is merged, activated, promoted, released, deployed, or KFM-published by this change.

### Future implementation graduation

The shared lane is not active until all applicable items are satisfied:

- [ ] named owners and independent review burden are accepted;
- [ ] shared orchestration need is proven against domain and validator-library alternatives;
- [ ] caller, input, spec, validator-set, report, outcome, receipt, and side-effect contracts are accepted;
- [ ] contract/schema/policy/evidence/review/lifecycle authority remains external and pinned;
- [ ] deterministic synthetic positive and negative fixtures exist;
- [ ] no-network tests prove failure, denial, abstention, hold/quarantine, no-op, error, retry, cancellation, and correction behavior;
- [ ] direct catalog/triplet/published/release writes and public-interface bypasses fail closed;
- [ ] receipt and report integrity, retention, expiry, supersession, and revalidation are tested;
- [ ] a repository-owned command and least-privilege CI job exist with honest check names;
- [ ] current checks pass for the implementation commit;
- [ ] promotion and release integration is separately reviewed; and
- [ ] rollback and correction drills preserve audit history.

A green workflow, parseable spec, or new Python function satisfies none of the unchecked obligations by itself.

[Back to top](#top)

---

## Open verification backlog

| ID | Question or required check | Current state | Graduation evidence |
|---|---|---|---|
| `PIPE-VALIDATE-001` | Is a shared orchestration lane needed, or should validation stay in domain pipelines plus `tools/validators/`? | **NEEDS VERIFICATION / ADR if authority changes** | Consumer inventory, duplication evidence, ownership decision. |
| `PIPE-VALIDATE-002` | Which accepted contract and schema own `ValidationReport`? | **UNKNOWN** | Canonical contract/schema refs and compatibility plan. |
| `PIPE-VALIDATE-003` | Which finite outcome and reason-code vocabulary is normative? | **UNKNOWN** | Accepted contract, negative fixtures, validator tests. |
| `PIPE-VALIDATE-004` | What is the caller/domain adapter protocol? | **PROPOSED** | Interface contract plus two proven domain consumers. |
| `PIPE-VALIDATE-005` | Is there a canonical shared validation spec lane and activation model? | **NOT ESTABLISHED** | Accepted spec schema, parser, registry, fixtures, and consumer binding. |
| `PIPE-VALIDATE-006` | Which validators are required, optional, ordered, or domain-supplied? | **NEEDS VERIFICATION** | Versioned validator registry and deterministic set digest. |
| `PIPE-VALIDATE-007` | Which receipt family and instance home record stage execution? | **NEEDS VERIFICATION** | Accepted receipt contract/schema/writer and Directory Rules decision. |
| `PIPE-VALIDATE-008` | Does orchestration persist reports or return pure results to the caller? | **NEEDS VERIFICATION** | Transaction/side-effect contract and failure tests. |
| `PIPE-VALIDATE-009` | How does a hold or quarantine request become a governed lifecycle transition? | **NEEDS VERIFICATION** | Accepted writer protocol, review rules, receipts, rollback tests. |
| `PIPE-VALIDATE-010` | Which current workflow and job would enforce this lane? | **UNKNOWN** | Command-bearing workflow, least-privilege threat review, current run. |
| `PIPE-VALIDATE-011` | Are any branch-protection rules coupled to aggregate validator job names? | **UNKNOWN** | Repository ruleset/required-check inspection. |
| `PIPE-VALIDATE-012` | Which events invalidate prior reports and trigger revalidation? | **PROPOSED** | Correction contract, affected-reference index, replay tests. |
| `PIPE-VALIDATE-013` | Which Directory Rules edition is canonical? | **CONFLICTED / NEEDS VERIFICATION** | Accepted ADR or registry decision plus synchronized supersession metadata. |
| `PIPE-VALIDATE-014` | Who owns and independently reviews the shared stage? | **OWNER_TBD** | Accepted ownership and separation-of-duties record. |

Do not close an item because prose now describes it. Close it only with the named repository or governance evidence.

[Back to top](#top)

---

## Evidence ledger

This ledger is bounded to the repository and commit in the metadata block.

| Source | Evidence role | Observation supported | Does not prove |
|---|---|---|---|
| [`pipelines/validate/README.md` prior blob](README.md) | Target baseline | v0.1 governance draft existed at the recorded blob. | Implemented behavior. |
| [`main.py`](main.py) | Current implementation | One-line placeholder only. | Hidden/external runtime absence. |
| [`pipelines/README.md`](../README.md) | Parent convention | `pipelines/` is executable logic and validation is non-publishing. | This child lane is active. |
| [`pipeline_specs/README.md`](../../pipeline_specs/README.md) | Declarative authority | `pipeline_specs/` owns declarative intent and is placeholder-heavy. | Active shared validation spec. |
| [`tools/validators/README.md`](../../tools/validators/README.md) | Validator authority | Reusable validators/checkers belong under `tools/validators/`. | Every documented validator executes. |
| [`run_all.py`](../../tools/validators/_common/run_all.py) | Executable wiring | Six named fixture validator scripts run sequentially and fail on non-zero. | Current pass result or complete coverage. |
| [`Makefile`](../../Makefile) | Command surface | `make validate` invokes aggregate schemas and tests, not this placeholder entrypoint. | Shared pipeline-stage implementation. |
| [`tests/pipelines/README.md`](../../tests/pipelines/README.md) | Test boundary | Direct lane was README-only at its recorded snapshot. | No package/domain tests anywhere. |
| [Archaeology validation README](../domains/archaeology/validate/README.md) and [`validate.yaml`](../../pipeline_specs/archaeology/validate.yaml) | Domain example | Domain docs and empty-stage spec scaffold exist. | Active domain or shared execution. |
| [`test_pipeline_connector_non_publisher.py`](../../tests/policy/test_pipeline_connector_non_publisher.py) | Negative guard | Bounded static scan rejects certain nearby direct write patterns. | Full data-flow or runtime non-publication proof. |
| [Architecture](../../docs/architecture/directory-rules.md) and [doctrine](../../docs/doctrine/directory-rules.md) Directory Rules | Placement doctrine | Both preserve the implementation/spec/validator/test/fixture root split. | Which edition is canonical. |
| [`lifecycle-law.md`](../../docs/doctrine/lifecycle-law.md) | Lifecycle doctrine | Promotion is governed and validation is not publication. | Active stage or gate implementation. |
| [`DRIFT_REGISTER.md`](../../docs/registers/DRIFT_REGISTER.md) | Drift control | Existing register does not record this lane as implemented. | Exhaustive absence of related drift. |
| [`GENERATED_RECEIPT` README](../../data/receipts/generated/README.md) and [schema](../../schemas/contracts/v1/receipts/generated_receipt.schema.json) | Contribution convention | AI-authored artifacts require provenance distinct from approval. | Validation-stage receipt authority. |
| [Workflow inventory](../../.github/workflows/README.md) and [PR template](../../.github/PULL_REQUEST_TEMPLATE.md) | CI/review convention | Checks, threat preflight, receipt, validation, and rollback must remain explicit. | Current required checks or pass state. |

### Inspection limits

- The review used commit-pinned connector reads and bounded code search, not a full clone or exhaustive history scan.
- Exact missing-path checks were limited to the three shared spec/test/fixture README paths named above.
- Repository settings, branch protection, environments, deployments, runtime logs, generated files, ignored files, external services, and private branches were not inspected.
- Workflow conclusions must be rechecked at the review branch because the workflow README is a prior snapshot and workflow files can change independently.
- The supplied Directory Rules PDF was text-extracted and the pipeline/spec/tools pages were visually inspected; other supplied reports were used as doctrine or lineage, not current implementation proof.

[Back to top](#top)

---

## Maintainer checklist

Before changing this lane:

- [ ] Pin the base commit and re-open this README plus `main.py`.
- [ ] Check root/path-scoped instructions, Directory Rules, ADRs, and the drift register.
- [ ] Search for overlapping branches and pull requests.
- [ ] Decide whether the change is orchestration, validator implementation, domain logic, spec, test, fixture, data, policy, receipt, or release work.
- [ ] Keep validator and domain authority out of the shared orchestrator.
- [ ] Bind callers, inputs, specs, validators, contracts, schemas, evidence, policy, review, outcomes, and receipts explicitly.
- [ ] Add deterministic public-safe positive and negative fixtures before live-source use.
- [ ] Prove fail-closed behavior for sensitive and public-interface boundaries.
- [ ] Inspect workflow triggers, permissions, runner trust, secrets, artifacts, and required-check coupling.
- [ ] Record correction, revalidation, expiry, supersession, and rollback behavior.
- [ ] Emit the required generated-work receipt for AI-authored changes.
- [ ] Read the remote branch bytes and complete diff back before opening or updating a draft PR.
- [ ] Keep human review, merge, promotion, release, and publication as separate decisions.

[Back to top](#top)
