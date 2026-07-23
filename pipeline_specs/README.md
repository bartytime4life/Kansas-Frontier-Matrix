<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-readme
title: pipeline_specs/ — Governed Declarative Pipeline Specification Root
type: readme; root-readme; canonical-pipeline-spec-root; declarative-activation-boundary; compatibility-drift-index
version: v0.4
status: draft; repository-grounded; canonical-root-confirmed; placeholder-heavy; mixed-lane-maturity; no-active-spec-system-established; companion-boundaries-reconciled; non-authoritative
owners: OWNER_TBD — Pipeline-spec steward · Pipeline steward · Domain stewards · Source and rights steward · Contract and schema steward · Validation and CI steward · Evidence and receipt steward · Policy and sensitivity steward · Release steward · Security reviewer · Docs steward
created: 2026-06-13
updated: 2026-07-23
supersedes: v0.3
prepared_under_prompt: KFM Markdown Engineering, Modernization & GitHub Documentation Implementation Agent v5.0.0
policy_label: "public-doctrine; pipeline-specs-root; declarative-only; no-secrets; no-live-activation; no-direct-fetch; no-direct-admission; no-direct-lifecycle-write; no-direct-release; source-role-aware; rights-aware; sensitivity-aware; evidence-bound; policy-gated; review-gated; correction-aware; rollback-aware"
current_path: pipeline_specs/README.md
truth_posture: >
  CONFIRMED target v0.3 README at the pinned base; Directory Rules v1.4 canonical
  pipeline_specs responsibility root and mandatory root-README section order; current pipelines
  v0.3 executable-root contract; pipelines/specs v0.2 compatibility guardrail; bounded seventeen
  direct README lanes and five nested README sublanes recorded by the v0.3 evidence snapshot;
  representative empty-stage and documentation-inventory placeholders; schema-paired PROPOSED
  RunReceipt contract, closed schema, validator wrapper, and fixture lane; executable static
  connector/pipeline non-publisher guard; tests/pipelines README-only direct boundary; workflow
  inventory and bounded holds; generated-receipt lane and schema; and CODEOWNERS routing /
  PROPOSED accepted pipeline-spec contract and schema, deterministic canonicalization and hashing,
  explicit discovery and activation registry, parser/consumer compatibility contract, source
  activation binding, finite spec-validation decisions, controlled reason codes, dedicated
  no-network fixtures and tests, correction invalidation, and rollback automation /
  CONFLICTED v0.3 section order versus Directory Rules section 15; air versus atmosphere;
  people versus people-dna-land; settlement versus settlements-infrastructure; shared versus
  domain watcher placement; historical pipeline_specs/domains references; pipeline_specs versus
  pipelines/specs semantics; Directory Rules compatibility copy; and unratified overlap among
  spec state, validation result, RunReceipt outcome, runtime response, and release decision
  vocabularies /
  UNKNOWN exhaustive recursive inventory, active specs, parser and registry implementation,
  scheduler, source activation, consumers, runtime execution, emitted pipeline receipts,
  substantive spec CI, promotion dependency, branch protection, deployment, production use,
  and public effects /
  NEEDS VERIFICATION named owners, child-inventory freshness, accepted schema and IDs, alias and
  migration decisions, source-registry topology, rights and sensitivity enforcement, dedicated
  fixtures and tests, correction propagation, rollback drills, and the first active governed consumer
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 59938ab542b1ce5980fe2a93b2b806e362643ebd
  prior_blob: 7f35f1c06aaec08d03182cf71e88a812bf179ebf
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  pipelines_readme_blob: c2bee1db957a665b973b44aea8bda63bdd82b7e5
  pipelines_specs_compatibility_blob: 74ca6cff32623bdca785d47d088d04bdce6a80da
  tests_pipelines_blob: 08fa70cd33af2c04f03aadbf7d973c6f4e29fbf3
  non_publisher_test_blob: c6164787bc848eb2347c347af203d76afae37a2b
  run_receipt_contract_blob: 5592aa5e22bbdd0c668189f79b50c18f7d1b2479
  run_receipt_schema_blob: 80d13bcb750d56c769da2f8871242388f7f50a69
  run_receipt_validator_blob: 9b59481e90c021f0f92b74511c43fcefbbe3a057
  workflows_readme_blob: afb4f79ce2c5267cb1679f48186260e6edebf8b2
  generated_receipt_schema_blob: fba21ed27ebccf1362fe397fe0c3ebd85e072685
  agriculture_stage_scaffold_blob: 7d2ea19b770a5b8da5cf998dd39a3f5ae61301c9
  soil_stage_scaffold_blob: 1507c2d908da99646aac536a57bb7217c1d71ec8
  fauna_inventory_placeholder_blob: 172331bb32094b649362bb237f105d2a9c3c1a0b
  flora_inventory_placeholder_blob: 8aab817f869425f74b792f704157ad01f7b88270
  hazards_inventory_placeholder_blob: f4a0ecc773a61fb972d696aa96ca60740522fbad
  hydrology_inventory_placeholder_blob: 4109f3f596fdf1865f85b5670adb82ba6321b54e
  habitat_inventory_placeholder_blob: ccfed2a152ba2ac9de809f76ddfbe3c59dc14877
  watchers_readme_blob: d3f554a87a994ae32b9f3a6211a6224e5084b99f
  v0_3_bounded_direct_child_readmes: 17
  v0_3_bounded_nested_readmes: 5
  inventory_method: GitHub connector exact reads and bounded repository-index queries; counts and absence claims are not full-history, all-branch, generated-file, or runtime-discovery assertions
related:
  - ../CONTRIBUTING.md
  - ../SECURITY.md
  - ../docs/doctrine/directory-rules.md
  - ../docs/architecture/directory-rules.md
  - ../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - ../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md
  - ../docs/adr/ADR-0012-connector-outputs-to-data-raw-or-data-quarantine-only.md
  - ../docs/adr/ADR-0017-source-descriptor-admission-process.md
  - ../docs/adr/ADR-0018-promotion-gate-sequence.md
  - ../docs/adr/ADR-0021-quarantine-has-structured-exit-paths.md
  - ../docs/adr/ADR-0022-catalog-matrix--stac-+-dcat-+-prov-must-agree.md
  - ../docs/registers/DRIFT_REGISTER.md
  - ../pipelines/README.md
  - ../pipelines/specs/README.md
  - ../tests/pipelines/README.md
  - ../tests/policy/test_pipeline_connector_non_publisher.py
  - ../contracts/runtime/run_receipt.md
  - ../schemas/contracts/v1/runtime/run_receipt.schema.json
  - ../fixtures/contracts/v1/runtime/run_receipt/README.md
  - ../tools/validators/validate_run_receipt.py
  - ../data/receipts/pipeline/README.md
  - ../data/receipts/generated/README.md
  - ../schemas/contracts/v1/receipts/generated_receipt.schema.json
  - ../.github/workflows/README.md
  - ../.github/CODEOWNERS
  - agriculture/README.md
  - air/README.md
  - archaeology/README.md
  - atmosphere/README.md
  - fauna/README.md
  - flora/README.md
  - geology/README.md
  - habitat/README.md
  - hazards/README.md
  - hydrology/README.md
  - people-dna-land/README.md
  - people/README.md
  - roads-rail-trade/README.md
  - settlement/README.md
  - settlements-infrastructure/README.md
  - soil/README.md
  - watchers/README.md
tags: [kfm, pipeline-specs, declarative-configuration, activation, pipelines, placeholders, source-admission, lifecycle, receipts, evidence, policy, validation, correction, rollback, migration]
notes:
  - "This revision changes pipeline_specs/README.md and its required generated provenance receipt only."
  - "The canonical declarative root is preserved; compatibility and alias lanes remain visible rather than silently promoted or retired."
  - "The first twelve H2 sections now follow Directory Rules section 15 exactly."
  - "No pipeline-spec YAML, parser, scheduler, consumer, source activation, contract, schema, policy, fixture, test, workflow, lifecycle record, runtime, release object, or public artifact is created or modified."
  - "The prior README remains recoverable through the recorded blob and the v0.3 to v0.4 no-loss ledger."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>
<a id="pipeline-specs"></a>

# `pipeline_specs/` — Governed Declarative Pipeline Specification Root

> **One-line purpose.** Own the governed declarative intent for **what** a KFM pipeline may attempt—identity, admitted inputs, lifecycle transitions, constraints, evidence and policy prerequisites, expected outcomes, receipts, correction duties, and rollback targets—without becoming executable code, source authority, lifecycle storage, release approval, or a public serving surface.

<p>
  <a href="#status"><img alt="Status: repository-grounded draft" src="https://img.shields.io/badge/status-repository--grounded%20draft-yellow"></a>
  <a href="#authority-level"><img alt="Root: canonical pipeline specs" src="https://img.shields.io/badge/root-pipeline__specs%2F-blue"></a>
  <a href="#status"><img alt="Maturity: placeholder-heavy" src="https://img.shields.io/badge/maturity-placeholder--heavy-orange"></a>
  <a href="#status"><img alt="Active specification system: not established" src="https://img.shields.io/badge/active__spec__system-not__established-critical"></a>
  <a href="#validation"><img alt="Dedicated specification tests: not established" src="https://img.shields.io/badge/spec__tests-not__established-lightgrey"></a>
  <a href="#outputs"><img alt="Publication authority: denied" src="https://img.shields.io/badge/publication-DENIED-red"></a>
  <a href="#validation"><img alt="Truth posture: cite or abstain" src="https://img.shields.io/badge/truth-cite__or__abstain-success"></a>
</p>

> [!IMPORTANT]
> **A file is not an active specification.** Repository inspection confirms declarative files, READMEs, empty-stage scaffolds, and documentation-inventory placeholders, but it does not establish an accepted root schema, canonicalizer, parser, discovery registry, compatible consumer registry, scheduler, source-activation binding, dedicated spec test suite, or substantive spec CI gate.

> [!CAUTION]
> **Keep the layers separate.** `pipeline_specs/` declares **what may run**; [`pipelines/`](../pipelines/README.md) implements **how governed execution occurs**; [`pipelines/specs/`](../pipelines/specs/README.md) is a compatibility guardrail and must not become a second specification authority.

> [!WARNING]
> **Secrets and restricted material never belong in specs, examples, logs, receipts, issues, or pull requests.** Credentials, private endpoints, source payloads, protected coordinates, living-person or DNA data, rare-species or rare-plant locations, archaeology or cultural knowledge, private-land joins, infrastructure vulnerabilities, and unreviewed source terms require approved handling outside ordinary public repository surfaces.

**Quick navigation**

| Root contract | Trust and activation | Maintenance |
|---|---|---|
| [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) | [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Operating model](#operating-model-and-activation-boundary) · [Contract](#minimum-active-spec-contract) | [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed) · [Conflicts](#compatibility-and-placement-conflicts) · [Rollback](#correction-deactivation-and-rollback) |

---

## Purpose

`pipeline_specs/` is the canonical KFM responsibility root for declarative pipeline configuration and activation intent.

It answers these questions:

1. Which stable specification identity and version is being requested?
2. Which admitted sources, lifecycle inputs, contracts, schemas, policies, and consumers does it depend on?
3. Which transitions, side effects, resource limits, network posture, and finite outcomes are permitted?
4. Which reports, receipt facts, evidence checks, review states, correction obligations, and rollback targets are required?
5. How can the declaration be disabled, superseded, migrated, replayed, or retired without rewriting history?

A specification does not execute itself. Executable logic belongs under [`pipelines/`](../pipelines/README.md), an admitted shared package, or another verified implementation root.

This README does not activate any current YAML, define an accepted pipeline-spec schema, create a parser or scheduler, admit a source, prove a claim, approve a release, or publish a product.

[Back to top](#top)

---

## Authority level

**Canonical declarative pipeline-specification root; non-authoritative for execution, evidence, policy, lifecycle promotion, release, and publication.**

Directory Rules assigns `pipeline_specs/` and `pipelines/` separate canonical responsibilities:

```text
pipeline_specs/  = WHAT may run and under which declared gates
pipelines/       = HOW governed execution occurs
```

| Concern | Owning authority | Role of a pipeline spec |
|---|---|---|
| Executable behavior | [`pipelines/`](../pipelines/README.md), admitted packages, governed applications | References a compatible consumer; never implements it. |
| Source access | `connectors/` | Names admitted source references; never fetches or activates a source. |
| Source identity, role, rights, activation | `data/registry/sources/` or an accepted control-plane home | Resolves governed IDs and prerequisites; never creates permission. |
| Object meaning | `contracts/` | References accepted semantic contracts. |
| Machine shape | `schemas/` | References accepted schemas; does not define a parallel schema here. |
| Admissibility and obligations | `policy/` | Requires policy results; never self-allows. |
| Enforceability | `tests/`, `fixtures/`, validators under `tools/` | Declares expected cases; does not count itself as proof. |
| Lifecycle state and records | `data/<phase>/` | Declares candidate transitions; stores no lifecycle payload here. |
| Receipts and proofs | `data/receipts/`, `data/proofs/` | Requires emitted references; is neither object family. |
| Release, correction, withdrawal, rollback | `release/` | Declares prerequisites and targets; cannot approve a state transition. |
| Public delivery | governed applications and released artifacts | Is never a public truth source or direct public endpoint. |

### Canonical and compatibility posture

| Path | Classification | Rule |
|---|---|---|
| `pipeline_specs/` | Canonical declarative root | New authoritative specification work lands here only after contract, placement, and activation review. |
| [`pipelines/`](../pipelines/README.md) | Canonical executable root | Implements governed execution; must not absorb declarative authority. |
| [`pipelines/specs/`](../pipelines/specs/README.md) | Compatibility and migration guardrail | Do not add active specifications or fallback discovery here. |
| `pipeline_specs/air/` | Compatibility-oriented lane | Do not create parallel authority with Atmosphere. |
| `pipeline_specs/people/` | Compatibility alias | Do not create a lighter path around People/DNA/Land controls. |
| `pipeline_specs/settlement/` | Compatibility alias | Do not create parallel authority with Settlements/Infrastructure. |

Changing the canonical split, creating another active spec root, or silently promoting an alias requires the ADR and migration burden defined by Directory Rules.

[Back to top](#top)

---

## Status

### Evidence snapshot

| Field | Value |
|---|---|
| Base | `main@59938ab542b1ce5980fe2a93b2b806e362643ebd` |
| Prior README blob | `7f35f1c06aaec08d03182cf71e88a812bf179ebf` |
| Current document version before this change | `v0.3` |
| Inventory posture | Bounded and repository-index-assisted; not a complete recursive or runtime inventory |
| Implementation effect of this revision | None — documentation and generated provenance only |

### Confirmed current state

- The current root contains declarative documentation and payload files of mixed maturity.
- The v0.3 evidence snapshot recorded seventeen direct child README lanes and five nested README sublanes; freshness remains bounded rather than assumed complete.
- Sampled payloads still represent two non-active shapes:
  - empty-stage scaffolds such as `agriculture/normalize.yaml` and `soil/ingest.yaml`;
  - short `status: PROPOSED` files created from documentation inventories, including sampled Fauna, Flora, Hazards, Hydrology, and Habitat files.
- [`pipelines/README.md`](../pipelines/README.md) is now a repository-grounded v0.3 executable-root contract and records placeholder-heavy implementation, a static non-publisher guard, and a schema-paired PROPOSED `RunReceipt` family.
- [`pipelines/specs/README.md`](../pipelines/specs/README.md) is a v0.2 compatibility guardrail; active configuration must not be discovered there.
- [`tests/pipelines/README.md`](../tests/pipelines/README.md) remains a README-only direct test boundary; no dedicated executable pipeline suite is established there.
- [`tests/policy/test_pipeline_connector_non_publisher.py`](../tests/policy/test_pipeline_connector_non_publisher.py) is executable and scans connector/pipeline write contexts for direct writes to `data/catalog`, `data/published`, or `release/`. It does not validate pipeline-spec shape or activation.
- `RunReceipt` has a paired PROPOSED contract and closed schema plus a validator wrapper. That proves a machine-shaped receipt family exists; it does not prove pipeline-spec binding, receipt emission, persistence, or promotion dependency.
- The workflow inventory records broad domain holds and command-bearing partial gates, but no dedicated substantive pipeline-spec workflow is established by the inspected evidence.
- CODEOWNERS routes this root to `@bartytime4life`; routing is not human approval or release authority.

### Maturity matrix

| Capability | Current posture | Safe conclusion |
|---|---:|---|
| Root README | `CONFIRMED` | Canonical responsibility and safety boundary exist. |
| Child README network | `CONFIRMED, bounded` | Mixed domain, alias, and watcher lanes are documented. |
| Declarative payload files | `CONFIRMED` | File presence and placeholder shapes exist. |
| Accepted pipeline-spec schema | `NOT ESTABLISHED` | No current active shape may be inferred. |
| Canonicalization and digest algorithm | `UNKNOWN` | No stable `spec_hash` computation is accepted here. |
| Parser and discovery registry | `NOT ESTABLISHED` | Directory scanning is unsafe activation. |
| Consumer/version binding | `UNKNOWN` | No active spec-to-consumer contract is established. |
| Source activation binding | `NOT ESTABLISHED` | A source reference cannot self-admit. |
| Dedicated spec fixtures and tests | `NOT ESTABLISHED` | Adjacent pipeline test documentation is not a spec suite. |
| Substantive pipeline-spec CI | `NOT ESTABLISHED` | Workflow presence does not prove this root is enforced. |
| RunReceipt shape | `PROPOSED, schema-paired` | A closed receipt shape exists; runtime binding is unproved. |
| Current active specifications | `NOT ESTABLISHED` | Placeholder, scaffold, proposed, or candidate labels remain required. |
| Scheduler, runtime use, production effects | `UNKNOWN` | No deployment or public behavior claim is supported. |

### Root-README conformance correction

The v0.3 document preserved strong content but did not place the first twelve H2 sections in the order required by Directory Rules section 15. v0.4 corrects that documentation drift without changing the root's responsibility or implementation.

[Back to top](#top)

---

## What belongs here

The root and its reviewed lanes may contain:

- this root README and lane-level READMEs;
- declarative YAML, JSON, TOML, or another accepted specification format after schema and parser admission;
- stable specification identity, semantic version, declared maturity, owner roles, digest, and supersession metadata;
- references to admitted sources, contracts, schemas, policies, lifecycle inputs, evidence requirements, review records, receipt profiles, release prerequisites, and rollback targets;
- declarative stage or dependency graphs that a named, compatible consumer can interpret deterministically;
- cadence, freshness, valid-time, source-vintage, stale-state, no-op, retry, cancellation, and resource-limit declarations;
- explicit network, filesystem, tool, side-effect, and data-minimization posture;
- finite spec-validation expectations and stable reason-code references;
- compatibility maps, deprecation notices, and migration pointers that name one canonical target and do not evolve independently;
- examples only when unmistakably labeled synthetic, non-active, bounded, and schema-valid under the profile they illustrate.

### Required admission fields for implementation-bearing specs

| Field family | Minimum expectation |
|---|---|
| Identity | Stable `spec_id`, version, state, owner roles, immutable digest, supersession link. |
| Shape | Accepted semantic contract, machine schema, canonicalization rules, and unknown-field behavior. |
| Consumer | Exact parser, compatible executable consumer, supported version range, and failure posture. |
| Sources | Admitted `SourceDescriptor` refs, source roles, activation state, rights, sensitivity, vintage, and freshness. |
| Support | Spatial and temporal scope, scale, uncertainty, source knowledge character, and anti-collapse rules. |
| Lifecycle | Allowed inputs, candidate outputs, quarantine/no-op behavior, and prohibited transitions. |
| Execution | Network/tool/filesystem posture, side effects, idempotency, retries, timeouts, cancellation, resource limits. |
| Outcomes | Spec-validation decision vocabulary, reason codes, and mapping to consumer/run outcomes. |
| Receipts | Required run/transform/validation receipt profiles and reference bindings. |
| Governance | Evidence, policy, review, catalog, release, correction, withdrawal, and rollback prerequisites. |
| Proof | Positive and negative fixtures, spec-to-consumer agreement tests, CI check, and replay evidence. |

A new lane or implementation-bearing payload must identify its responsibility, consumer, source, rights, sensitivity, tests, receipts, migration, correction, and rollback posture. Missing answers mean `HOLD`, not implicit admission.

[Back to top](#top)

---

## What does NOT belong here

| Prohibited or misplaced material | Correct authority or action |
|---|---|
| Executable pipeline modules, runners, schedulers, adapters, or orchestration logic | [`pipelines/`](../pipelines/README.md), admitted packages, or governed applications |
| Source-specific fetch and connector logic | `connectors/` |
| Source descriptors, activation decisions, credentials, tokens, or private endpoints | Accepted source registry/decision surfaces; secrets remain external |
| Contract meaning or machine schema definitions | `contracts/` and `schemas/` |
| Policy rules, policy bundles, or policy decisions | `policy/` and governed decision records |
| Test source or golden/invalid payloads | `tests/` and `fixtures/` |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED material | Correct lifecycle phase under `data/` |
| Run receipts, validation receipts, proofs, EvidenceBundles, catalogs, or generated reports | Accepted `data/receipts/`, `data/proofs/`, evidence, catalog, or report homes |
| Release manifests, PromotionDecisions, corrections, withdrawals, rollback cards, signatures | `release/` |
| Public API, UI, map, AI, export, or alerting behavior | Governed application and package surfaces |
| Direct lifecycle writer instructions that bypass policy/review/promotion | Nowhere; deny or redesign |
| Real source payloads or sensitive examples | Governed lifecycle storage; public repository examples must be synthetic and reviewed |
| Symlinks, mirrors, fallback copies, or generated duplicates that can become a second active authority | Use one canonical target plus an explicit migration record |
| Active specifications under `pipelines/specs/` | Move through reviewed migration to `pipeline_specs/`; keep the compatibility lane non-discoverable |

A schedule string, parser success, merge, green workflow, pipeline run, receipt, or release-adjacent filename cannot by itself activate a spec or authorize public state.

[Back to top](#top)

---

## Inputs

A reviewed specification may reference only bounded, governed inputs.

### Permitted input classes

- stable request, spec, run, trace, decision, and audit identities;
- admitted source descriptor and activation-decision references;
- immutable or versioned source/lifecycle artifact references appropriate to the declared stage;
- accepted contract and schema versions;
- policy profile, rights, sensitivity, consent, access, review, release, freshness, and correction references;
- deterministic fixtures and expected outcomes;
- explicit parser and consumer versions;
- non-secret configuration references;
- network, tool, filesystem, time, memory, concurrency, queue, retry, timeout, and cancellation limits;
- prior-state, supersession, invalidation, correction, and rollback references.

### Forbidden normal inputs

- credentials, secret values, private endpoints, signing material, or secret-bearing `.env` content;
- inline source payloads, canonical evidence bodies, or unrestricted lifecycle-store dumps;
- unresolved exact sensitive geometry or restricted domain records;
- living-person data, DNA/genomic material, consent-sensitive joins, title conclusions, or owner-resolved private-land data;
- browser or issue text treated as system authority;
- prompt-like text embedded in evidence treated as executable instruction;
- private chain-of-thought or hidden reasoning;
- unrestricted filesystem, shell, network, or tool authority;
- stale, corrected, withdrawn, superseded, or denied inputs without explicit state handling;
- directory presence treated as activation.

### Input admission checklist

- [ ] Specification identity, state, version, owner roles, and digest are explicit.
- [ ] Parser and compatible executable consumer are named and admitted.
- [ ] Every source reference resolves to an activation state, role, rights, sensitivity, and vintage.
- [ ] Contract and schema references resolve to accepted profiles.
- [ ] Lifecycle inputs are allowed for the declared stage.
- [ ] Context and configuration are minimized and secret-free.
- [ ] Network, tool, filesystem, side-effect, and resource permissions are bounded.
- [ ] Evidence, policy, review, receipt, correction, and rollback obligations are known.
- [ ] A safe no-op, quarantine, hold, deny, error, cancellation, or disable path exists.

[Back to top](#top)

---

## Outputs

Specifications emit or support **declarative intent and reviewable bindings**, not runtime truth or public artifacts.

### Permitted output classes

- a schema-valid specification candidate;
- deterministic canonical bytes and a `spec_hash` after an accepted canonicalizer exists;
- a parser/consumer compatibility result;
- a source-binding and lifecycle-transition validation result;
- a finite spec-validation decision with reason codes;
- a changed-spec dependency-closure report;
- a migration, deprecation, supersession, correction, deactivation, or rollback reference;
- requirements for future execution receipts, validation reports, evidence checks, catalog closure, and release review;
- a candidate activation request for an independent governed decision.

### Output boundary

| Downstream surface | What a spec may supply | What the downstream authority must still decide or prove |
|---|---|---|
| Parser/registry | Identity, schema profile, canonical bytes | Parse safety, duplicate handling, discovery, state, activation |
| Pipeline consumer | Stage graph, constraints, expected outputs | Executable behavior, sandboxing, failure handling, receipt emission |
| Source gate | Source refs and required roles | Admission, rights, sensitivity, activation, current source state |
| Validation | Expected fixtures and decisions | Actual test execution and enforceability |
| Lifecycle handoff | Candidate transition declaration | Whether the transition is allowed and completed |
| Receipt system | Required receipt profile | Emission, persistence, validation, joins, retention, redaction |
| Catalog/triplet | Closure prerequisites | Identifier/digest/release agreement |
| Release | Readiness prerequisites and rollback target | Independent promotion, release, correction, withdrawal, rollback decisions |
| Public client | Nothing directly | Governed API and released artifacts only |

### Non-authority invariants

- Raw parser output is not the public contract.
- A schema-valid spec is not an admitted source or executable pipeline.
- An active-looking filename is not an activation record.
- A run receipt is process memory, not evidence or release approval.
- A successful pipeline run is not lifecycle promotion.
- A release candidate is not `PUBLISHED`.
- A public client must never discover or render specifications directly.

[Back to top](#top)

---

## Validation

Validation must separate **document presence, specification shape, canonical identity, bindings, behavior, policy, integration, and release readiness**.

### Current adjacent executable evidence

| Check or surface | Confirmed role | Limit |
|---|---|---|
| [`tests/policy/test_pipeline_connector_non_publisher.py`](../tests/policy/test_pipeline_connector_non_publisher.py) | Static guard against direct connector/pipeline write contexts targeting catalog, published, or release paths. | Does not inspect `pipeline_specs/` shape, discovery, activation, or consumer agreement. |
| [`RunReceipt` schema](../schemas/contracts/v1/runtime/run_receipt.schema.json) | Closed PROPOSED receipt shape with required run, stage, input/output, code, spec hash, source, validation, and outcome fields. | Does not prove emission, persistence, spec validity, or release permission. |
| [`validate_run_receipt.py`](../tools/validators/validate_run_receipt.py) | Repository-owned wrapper for the paired RunReceipt fixture lane. | Validates receipts, not pipeline specs. |
| [`tests/pipelines/README.md`](../tests/pipelines/README.md) | Documents cross-cutting pipeline behavior proof expectations. | Direct lane remains README-only at its evidence snapshot. |
| [Workflow inventory](../.github/workflows/README.md) | Records broad domain holds and command-bearing partial gates. | No dedicated substantive pipeline-spec gate is established here. |

Repository-owned adjacent commands, **not run in this documentation-only change**:

```bash
python -m pytest tests/policy/test_pipeline_connector_non_publisher.py -q --strict-config --strict-markers
python tools/validators/validate_run_receipt.py --fixtures
```

These commands do not validate a pipeline spec. No accepted repository-native pipeline-spec validator command was established by this edit.

### Required specification validation layers

| Layer | Minimum positive and negative evidence |
|---|---|
| Shape | Valid spec; unknown field; missing required field; invalid version/state. |
| Canonicalization | Stable bytes; key-order variation; line-ending variation; digest mismatch. |
| Identity | Duplicate ID; reused version with changed meaning; alias collision; supersession cycle. |
| Parser and discovery | Unsupported schema; unsafe fallback path; compatibility-root discovery; malformed payload. |
| Consumer binding | Missing consumer; incompatible version; unsupported stage; changed consumer contract. |
| Source binding | Inactive source; role mismatch; unknown rights; denied sensitivity; stale/withdrawn source. |
| Lifecycle | Allowed transition; lifecycle skip; direct catalog/published/release target; unstructured quarantine exit. |
| Domain anti-collapse | Observation/model/advisory conflation; occurrence/range conflation; title/ownership conflation; static/station/satellite conflation. |
| Execution posture | Network denied by default; forbidden tool/filesystem permission; retry exhaustion; timeout; cancellation; duplicate run. |
| Outcomes | Unknown state; validation result treated as run result; negative result converted to success. |
| Receipts | Missing `spec_hash`; mismatched source refs; missing validation refs; invalid receipt outcome. |
| Correction and rollback | Corrected source; superseded spec; deactivation; queued-run invalidation; rollback target missing. |
| Public boundary | Browser/spec direct read; spec merge treated as activation; run treated as publication. |

### Vocabulary separation

Do not collapse distinct state machines:

| Layer | Confirmed or proposed vocabulary | Authority note |
|---|---|---|
| Specification maturity | `inventory_placeholder`, `stage_scaffold`, `proposed`, `candidate`, `active_internal`, `active_public_candidate`, `deprecated`, `disabled`, `retired` | **PROPOSED** until a spec contract accepts it. |
| Spec-validation decision | `PASS`, `HOLD`, `DENY`, `ERROR` plus controlled reasons | **PROPOSED**; should not be reused as runtime or release state. |
| Pipeline `RunReceipt.outcome` | `SUCCESS`, `PARTIAL`, `FAIL` | **CONFIRMED schema surface; contract status PROPOSED.** |
| Governed runtime response | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` where the runtime contract applies | Public/runtime envelope, not a pipeline-spec state. |
| Lifecycle | `RAW`, `WORK`, `QUARANTINE`, `PROCESSED`, `CATALOG`, `TRIPLET`, `PUBLISHED` | Governed lifecycle; not a parser result. |
| Promotion/release decision | Vocabulary defined by accepted promotion and release contracts | Independent authority; a spec never self-promotes. |

A future contract must define mappings explicitly. Similar words do not imply equivalent meaning.

### Documentation validation for this revision

This README change must pass:

- UTF-8 and LF normalization;
- exactly one H1;
- the twelve Directory Rules root sections in exact order;
- balanced fenced blocks and HTML tags;
- unique custom anchors and resolvable internal fragments;
- repository-relative link review for introduced destinations;
- no credential-like or sensitive payload introduction;
- semantic no-loss review against v0.3;
- remote readback and content-hash verification after mutation.

[Back to top](#top)

---

## Review burden

A pipeline specification can affect source use, lifecycle movement, policy, sensitive data, receipts, release readiness, and public derivatives. Review burden scales with that effect.

| Change class | Minimum review burden |
|---|---|
| Root or lane README wording only | Pipeline-spec steward and docs steward; additional owner when a material boundary changes. |
| Placeholder or scaffold metadata | Pipeline-spec owner plus affected domain/source owner; confirm it remains non-active. |
| Spec identity, version, state, or canonicalization | Pipeline-spec, contract, schema, validation, migration, and consumer owners. |
| Parser, discovery, registry, or consumer binding | Pipeline-spec, pipeline/package, security, validation, and operations owners. |
| Source refs, rights, sensitivity, consent, or access | Source/domain steward plus rights, policy, sensitivity, security, and evidence reviewers. |
| Lifecycle transition or side-effect posture | Pipeline, lifecycle/data, policy, evidence/receipt, validation, and release reviewers. |
| Schedule, network, tool, filesystem, or resource change | Pipeline, connector, configuration, infrastructure, security, and operations reviewers. |
| Receipt, evidence, catalog, promotion, correction, or rollback binding | Owning receipt/evidence/catalog/release/correction stewards; the spec author cannot self-approve. |
| Alias move, rename, retirement, or authority change | Migration and docs stewards, inbound-reference inventory, compatibility window, ADR where required, and tested rollback. |
| Sensitive People/DNA/Land, archaeology, rare-species/flora, infrastructure, or sovereignty-related spec | Owning domain and cultural/consent/privacy/sensitivity reviewers plus security and release stewards. |

### Separation of duties

The same actor must not be the sole generator, validator, merger, activator, operator, and release approver for a policy-significant specification. At minimum, activation and release decisions remain independent from authoring and parser success.

### CODEOWNERS posture

[`.github/CODEOWNERS`](../.github/CODEOWNERS) routes this root to `@bartytime4life`. Enforcement, branch protection, delegated domain review, and separation-of-duties automation remain `NEEDS VERIFICATION`.

[Back to top](#top)

---

## Related folders

### Responsibility counterparts

| Path | Relationship |
|---|---|
| [`pipelines/`](../pipelines/README.md) | Canonical executable pipeline and orchestration root. |
| [`pipelines/specs/`](../pipelines/specs/README.md) | Compatibility guardrail; not an alternate specification root. |
| `connectors/` | Source-specific fetch and staging implementation. |
| `contracts/` | Semantic meaning of specifications and referenced objects. |
| `schemas/` | Machine-checkable specification and referenced object shapes. |
| `policy/` | Source, rights, sensitivity, lifecycle, release, and obligation decisions. |
| [`tests/pipelines/`](../tests/pipelines/README.md) | Cross-cutting pipeline behavior test boundary. |
| `fixtures/` | Deterministic valid, invalid, denied, held, and migration examples. |
| `tools/validators/` | Repository-owned validators and canonicalization utilities. |
| `data/registry/sources/` | Source identity, role, rights, sensitivity, cadence, and activation. |
| [`data/receipts/pipeline/`](../data/receipts/pipeline/README.md) | Pipeline process-memory receipt lane. |
| `data/proofs/` | Proof objects; distinct from receipts and specs. |
| `data/catalog/` and `data/triplets/` | Derived discovery and relation surfaces after governed closure. |
| `release/` | Promotion, release, correction, withdrawal, and rollback decisions. |
| `runtime/` and governed applications | Bounded execution and serving behind the trust membrane. |

### Contract and validation counterparts

| Path | Relationship |
|---|---|
| [`contracts/runtime/run_receipt.md`](../contracts/runtime/run_receipt.md) | PROPOSED semantic receipt contract for a governed run/stage. |
| [`schemas/contracts/v1/runtime/run_receipt.schema.json`](../schemas/contracts/v1/runtime/run_receipt.schema.json) | Paired closed machine shape. |
| [`fixtures/contracts/v1/runtime/run_receipt/`](../fixtures/contracts/v1/runtime/run_receipt/README.md) | Receipt fixture family. |
| [`tools/validators/validate_run_receipt.py`](../tools/validators/validate_run_receipt.py) | Receipt validator wrapper. |
| [`tests/policy/test_pipeline_connector_non_publisher.py`](../tests/policy/test_pipeline_connector_non_publisher.py) | Bounded static no-direct-publish guard. |
| [Workflow inventory](../.github/workflows/README.md) | CI maturity and permission boundary index. |
| [`data/receipts/generated/`](../data/receipts/generated/README.md) | AI-authored artifact provenance lane; not implementation proof. |

### Direct lane registry

| Lane | Bounded posture | Governing issue |
|---|---|---|
| [`agriculture/`](agriculture/README.md) | Placeholder payloads and empty-stage scaffolds. | Aggregate versus field/operator specificity; inventory drift. |
| [`air/`](air/README.md) | Compatibility guardrail. | Avoid parallel authority with Atmosphere. |
| [`archaeology/`](archaeology/README.md) | Sensitive-domain boundary with planning placeholders. | Sovereignty, cultural review, exact locations, rights. |
| [`atmosphere/`](atmosphere/README.md) | Preferred Atmosphere/Air lane; scaffold maturity. | Observation/model/advisory and life-safety separation. |
| [`fauna/`](fauna/README.md) | Sensitive-domain lane with nested watcher guidance. | Rare-species geoprivacy. |
| [`flora/`](flora/README.md) | Sensitive-domain lane with watcher/path conflicts. | Rare plants, cultural/stewardship rights. |
| [`geology/`](geology/README.md) | Stage scaffolds and inventory placeholders. | Occurrence/deposit/reserve/permit/production distinctions. |
| [`habitat/`](habitat/README.md) | Nested lanes and placeholders. | Habitat context is not species occurrence. |
| [`hazards/`](hazards/README.md) | Source-oriented placeholders. | Not emergency or official-alert authority. |
| [`hydrology/`](hydrology/README.md) | Mixed scaffolds and source placeholders. | Observation/model/regulatory-context separation. |
| [`people-dna-land/`](people-dna-land/README.md) | Governing lane with empty-stage scaffolds. | Living-person, consent/revocation, DNA, title boundaries. |
| [`people/`](people/README.md) | README-only alias. | No lighter or parallel sensitive-data path. |
| [`roads-rail-trade/`](roads-rail-trade/README.md) | Scaffolds and placeholders. | Network identity, operating status, infrastructure sensitivity. |
| [`settlement/`](settlement/README.md) | README-only alias. | No parallel authority. |
| [`settlements-infrastructure/`](settlements-infrastructure/README.md) | Governing lane with empty-stage scaffolds. | Legal/operational status and infrastructure sensitivity. |
| [`soil/`](soil/README.md) | Five empty-stage scaffolds. | Survey/grid/station/satellite/pedon/interpretation separation. |
| [`watchers/`](watchers/README.md) | Shared placeholder-only boundary. | Shared/domain delegation and non-publisher rule. |

The registry is a bounded orientation surface, not an activation registry or complete recursive manifest.

[Back to top](#top)

---

## ADRs

The records below are repository-present. Their current files remain `proposed` or `draft/proposed`; this README does not accept them.

| Record | Current file status | Pipeline-spec consequence if accepted or otherwise governing |
|---|---:|---|
| [`ADR-0001 — schema home`](../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) | Verify against current ADR index | Machine shapes belong under `schemas/contracts/v1/...`, not beside specs. |
| [`ADR-0011 — receipts, proofs, manifests, catalogs`](../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md) | `proposed` | Prevents a spec or receipt from becoming proof, catalog, or publication authority. |
| [`ADR-0012 — connector outputs`](../docs/adr/ADR-0012-connector-outputs-to-data-raw-or-data-quarantine-only.md) | `draft / proposed` | Keeps source-edge output and later pipeline intent separate; connectors do not publish. |
| [`ADR-0017 — source descriptor admission`](../docs/adr/ADR-0017-source-descriptor-admission-process.md) | `proposed` | Requires source identity, role, rights, sensitivity, and activation before use. |
| [`ADR-0018 — promotion gate sequence`](../docs/adr/ADR-0018-promotion-gate-sequence.md) | `proposed` | A spec may name readiness gates but cannot pass or approve them by declaration. |
| [`ADR-0021 — structured quarantine exits`](../docs/adr/ADR-0021-quarantine-has-structured-exit-paths.md) | `proposed` | Quarantine transitions require named governed exits; no silent release. |
| [`ADR-0022 — STAC/DCAT/PROV agreement`](../docs/adr/ADR-0022-catalog-matrix--stac-+-dcat-+-prov-must-agree.md) | `proposed` | Catalog closure remains downstream and independently validated. |

### Decisions still needed

- accepted pipeline-spec semantic contract and schema family;
- canonicalization algorithm and `spec_hash` profile;
- stable ID, version, state, reason-code, and activation vocabularies;
- parser, discovery, active-spec registry, and consumer compatibility contract;
- alias disposition for Air, People, and Settlement;
- shared/domain watcher placement and plants-drift duplication;
- historical `pipeline_specs/domains/...` reference disposition;
- source registry and activation-decision topology;
- receipt profile and joins from spec to execution, validation, evidence, catalog, and release;
- dedicated fixture/test/CI contract;
- correction invalidation, deactivation, migration, and rollback automation.

Do not create a parallel authority while these decisions remain open.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-23 |
| Evidence base | `main@59938ab542b1ce5980fe2a93b2b806e362643ebd` |
| Prior target blob | `7f35f1c06aaec08d03182cf71e88a812bf179ebf` |
| Review mode | Same-path repository-grounded Markdown upgrade; documentation/provenance-only scope |
| Prompt | KFM Markdown Engineering, Modernization & GitHub Documentation Implementation Agent v5.0.0 |
| Implementation effect | None — no spec, parser, source, pipeline, policy, test, workflow, data, release, runtime, or public state changed |
| Rollback | Revert the update and generated-receipt commits, or restore the prior README blob and remove the new receipt |

### Maintenance triggers

Re-review this README when:

- a pipeline-spec schema, canonicalizer, parser, registry, or consumer becomes accepted;
- a specification moves beyond placeholder/scaffold/candidate state;
- a source activation or rights/sensitivity binding changes;
- a dedicated fixture/test lane or CI gate is introduced;
- an alias, watcher lane, or compatibility path moves, retires, or gains implementation;
- RunReceipt or another execution/validation receipt profile changes;
- correction, invalidation, deactivation, migration, or rollback behavior becomes executable;
- branch protection or CODEOWNERS enforcement changes;
- Directory Rules or an accepted ADR changes the canonical responsibility split.

[Back to top](#top)

---

## Operating model and activation boundary

```text
reviewed declarative candidate
  -> shape and canonicalization validation
  -> identity, version, alias, and supersession validation
  -> parser and consumer compatibility validation
  -> source activation, role, rights, sensitivity, and freshness checks
  -> lifecycle and domain anti-collapse validation
  -> deterministic no-network fixtures and negative cases
  -> evidence, policy, receipt, correction, and rollback prerequisite checks
  -> independent activation decision
  -> governed executable pipeline invocation
  -> validation records and RunReceipt candidate
  -> downstream catalog / proof / release review, if applicable
```

Every arrow after the declarative candidate is **outside the authority of the file itself**. The flow is a PROPOSED operating model, not a claim that the chain is implemented.

### Activation anti-collapses

```text
path exists                    != accepted specification
YAML parses                    != schema-valid specification
schema-valid                   != admitted source
merge completed                != activation approved
schedule declared              != scheduler configured
consumer named                 != compatibility proven
pipeline run succeeded         != evidence closure
RunReceipt validates           != policy or release approval
release candidate exists       != PUBLISHED
public client can fetch a file != governed public delivery
```

Directory scanning alone is unsafe activation because the root contains placeholders, aliases, compatibility lanes, and unratified vocabularies.

[Back to top](#top)

---

## Bounded root inventory

```text
pipeline_specs/
├── README.md
├── agriculture/
├── air/                         # compatibility guardrail
├── archaeology/
├── atmosphere/                  # preferred Atmosphere/Air lane
├── fauna/
├── flora/
├── geology/
├── habitat/
├── hazards/
├── hydrology/
├── people-dna-land/             # governing sensitive-domain lane
├── people/                      # compatibility alias
├── roads-rail-trade/
├── settlement/                  # compatibility alias
├── settlements-infrastructure/  # governing lane
├── soil/
└── watchers/                    # shared intent; placement-sensitive
```

The v0.3 evidence snapshot also recorded nested READMEs under Fauna/Flora watchers, Habitat ecoregions/land-cover, and People/DNA/Land land-ownership.

This map preserves the prior orientation. It is not a recursive manifest. Before activation, deletion, or migration, generate a commit-pinned recursive inventory and compare it with registries, consumers, workflows, receipts, release dependencies, and inbound links.

[Back to top](#top)

---

## Payload taxonomy

### Documentation-inventory placeholder

```yaml
status: PROPOSED
source_doc: docs/domains/example/MISSING_OR_PLANNED_FILES.md
path: pipeline_specs/example/example.yaml
notes:
  - Placeholder created from docs/domains markdown inventory.
```

This proves a planned path reference. It does not establish stable identity, schema, parser, source, lifecycle, consumer, schedule, fixtures, receipt, activation, or release behavior.

### Empty-stage scaffold

```yaml
name: agriculture-normalize
version: 1
stages: []
```

This proves a minimal shell. An empty stage list declares no operation graph, inputs, outputs, constraints, source refs, policy, evidence, receipt, or rollback behavior.

### Compatibility or README-only lane

A README may preserve routing, safety, or migration guidance without containing active profiles. Compatibility paths must not duplicate IDs, schedules, consumers, source refs, or release semantics.

### Candidate or active profile

No current root profile is upgraded to this class by this README. A candidate or active profile must satisfy the minimum contract, validation, review, activation, correction, and rollback requirements below.

[Back to top](#top)

---

## Minimum active spec contract

An active specification requires at least:

| Area | Requirement |
|---|---|
| Identity | Stable ID, semantic version, state, owners, immutable digest, supersession lineage. |
| Shape | Accepted contract, schema, canonicalization, closed/known extension behavior. |
| Binding | Exact parser and compatible executable consumer with version constraints. |
| Sources | Admitted SourceDescriptor refs, roles, activation, rights, sensitivity, versions, freshness. |
| Support | Spatial/temporal scope, scale, uncertainty, and domain knowledge character. |
| Lifecycle | Allowed inputs, candidate outputs, quarantine/no-op, and prohibited transitions. |
| References | Resolvable contracts, schemas, evidence, policy, review, receipt, release, correction, rollback refs. |
| Execution | Dry-run/network posture, resource limits, side effects, idempotency, retry, timeout, cancellation. |
| Outcomes | Separate spec-validation, run-receipt, runtime-response, and release mappings. |
| Migration | Compatibility, supersession, correction, deactivation, withdrawal, invalidation, rollback. |
| Proof | Positive/negative fixtures, spec-to-consumer tests, CI evidence, replay, public-boundary denial. |

Activation requires an explicit governed registry or decision record. A recursive file scan is not an activation registry.

[Back to top](#top)

---

## Lifecycle, source, and release gates

```text
source decision -> RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A spec may declare prerequisites and candidate transitions. It cannot grant source authority, store data, create evidence closure, approve policy, or write `PUBLISHED`.

Minimum gates for non-trivial activation:

1. identity, version, canonical bytes, and digest;
2. parser and compatible consumer binding;
3. source activation, role, rights, sensitivity, freshness, and correction state;
4. contract and schema resolution;
5. lifecycle transition allow/deny validation;
6. domain anti-collapse checks;
7. deterministic no-network fixtures and negative cases;
8. evidence and policy prerequisites;
9. execution and validation receipt requirements;
10. catalog/triplet closure requirements where applicable;
11. independent activation, review, promotion, and release decisions;
12. correction, withdrawal, deactivation, invalidation, and rollback readiness.

Default CI is no-network. Live network use needs explicit source activation, a reviewed connector, least privilege, rate limits, timeouts, bounded writes, safe logs, and a kill switch. It can never directly publish.

[Back to top](#top)

---

## Compatibility and placement conflicts

- **`pipeline_specs/` versus `pipelines/specs/`:** authoritative declarations belong here; the nested executable-root path is a compatibility guardrail.
- **`air/` versus `atmosphere/`:** current documentation prefers Atmosphere; duplicate active authority is denied.
- **`people/` versus `people-dna-land/`:** People remains an alias; sensitive governance stays in People/DNA/Land.
- **`settlement/` versus `settlements-infrastructure/`:** Settlement remains an alias; governing behavior stays in Settlements/Infrastructure.
- **Shared versus domain watchers:** use shared specs only for genuinely cross-domain behavior; domain roles, rights, sensitivity, or materiality favor domain sublanes.
- **Plants-drift duplication:** shared watcher and Flora-specific paths remain conflicted; this README does not choose one silently.
- **Historical `pipeline_specs/domains/...` references:** current root evidence does not establish that parent as canonical; treat references as drift signals.
- **Directory Rules copies:** [`docs/doctrine/directory-rules.md`](../docs/doctrine/directory-rules.md) is the governing doctrine file; the architecture copy remains a compatibility/drift surface until resolved.
- **State vocabulary overlap:** spec maturity, spec validation, RunReceipt, runtime envelope, lifecycle, and release vocabularies remain distinct until accepted mappings exist.
- **Child inventory freshness:** lane READMEs may lag files, consumers, source state, and workflows; do not treat the registry as an activation database.

Conflict handling:

1. freeze new activation or authority accumulation;
2. pin the current tree and inventory IDs, paths, consumers, schedules, source refs, receipts, and inbound links;
3. record drift and determine whether an ADR or migration decision is required;
4. select one canonical authority and one compatibility window;
5. validate parser/consumer behavior, negative paths, correction, and rollback;
6. migrate consumers and references;
7. retire the alias only after verification and rollback windows close.

This README authorizes none of those mutations.

[Back to top](#top)

---

## Correction, deactivation, and rollback

Disable or supersede a specification through explicit records, not silent deletion.

A deactivation or correction record should preserve:

- stable spec ID, version, digest, and prior path;
- reason and effective time;
- affected sources, consumers, schedules, queued/running/completed runs, and receipts;
- affected lifecycle candidates, EvidenceBundles, catalogs/triplets, release candidates, and public derivatives;
- source, contract, schema, policy, and correction references;
- replacement or superseding spec where applicable;
- reviewer and activation-decision state;
- rollback target and cache/invalidation obligations.

A corrected or withdrawn source, spec, contract, schema, policy, or consumer may invalidate work already produced. Dependency and invalidation machinery remains `UNKNOWN` until verified in code, tests, receipts, workflows, and release records.

Documentation rollback for this README is ordinary Git rollback. It does not mutate runtime, lifecycle, source, release, or public state.

[Back to top](#top)

---

## Definition of done

An active specification must have:

- [ ] stable identity, semantic version, state, owners, digest, and supersession lineage;
- [ ] accepted semantic contract, machine schema, canonicalization, and unknown-field behavior;
- [ ] accepted parser, deterministic discovery, and active-spec registry;
- [ ] verified consumer and version binding;
- [ ] admitted sources, roles, rights, sensitivity, freshness, scale, time, uncertainty, and correction state;
- [ ] allowed lifecycle inputs and candidate outputs, with direct publication denied;
- [ ] explicit network, tool, filesystem, side-effect, resource, retry, timeout, and cancellation posture;
- [ ] resolvable contract, schema, evidence, policy, review, receipt, catalog, release, correction, and rollback refs;
- [ ] valid, invalid, denied, held, no-op, sensitive, alias, migration, and rollback fixtures;
- [ ] spec-to-consumer agreement and compatibility-root exclusion tests;
- [ ] deterministic no-network CI with stable check names and visible negative cases;
- [ ] replay, idempotency, duplicate-run, retry-exhaustion, cancellation, quarantine, and partial-state tests;
- [ ] execution and validation receipt binding with digest/source/validation agreement;
- [ ] correction, deactivation, withdrawal, supersession, dependency invalidation, and rollback procedures;
- [ ] public-client denial and no-direct-publish tests;
- [ ] independent human activation and review separate from generation, validation, merge, execution, and release.

Until then, label the file `inventory_placeholder`, `stage_scaffold`, `proposed`, or `candidate`—never active by implication.

[Back to top](#top)

---

## Open verification register

| Item | Status | Evidence needed |
|---|---:|---|
| Exhaustive recursive inventory | `NEEDS VERIFICATION` | Commit-pinned tree, file classification, IDs, references, and consumers. |
| Child README freshness | `NEEDS VERIFICATION` | README-to-tree comparison and owner confirmation. |
| Accepted semantic contract and schema | `UNKNOWN` | Contract, schema, fixtures, validator, tests, and decision record. |
| Canonicalization and digest | `UNKNOWN` | Canonical bytes algorithm, vectors, collision/error handling, and CI. |
| Parser, discovery, registry | `UNKNOWN` | Code, explicit paths, compatibility exclusions, duplicate/alias tests. |
| Consumer compatibility | `UNKNOWN` | Named consumers, version matrix, agreement tests, failure mapping. |
| Active-spec inventory | `NOT ESTABLISHED` | Governed registry and activation decisions. |
| Meaning of `version: 1` | `UNKNOWN` | Accepted version semantics and migration rules. |
| Air/People/Settlement aliases | `NEEDS VERIFICATION` | Inbound references, ADR/migration disposition, rollback. |
| Shared/domain watcher placement | `CONFLICTED` | Source/domain ownership decision and plants-drift migration plan. |
| Historical `pipeline_specs/domains/...` refs | `CONFLICTED` | Reference inventory and canonical target decision. |
| Source activation vocabulary/topology | `NEEDS VERIFICATION` | Source descriptor, activation decision, registry, policy, tests. |
| Rights/sensitivity enforcement | `NEEDS VERIFICATION` | Executable policy, negative fixtures, decision records. |
| Dedicated spec fixtures/tests/CI | `NOT ESTABLISHED` | Test lane, fixtures, repository command, workflow, current run evidence. |
| RunReceipt binding and persistence | `UNKNOWN` | Spec-to-run join, emitted receipts, validation, retention, redaction. |
| Catalog/promotion dependency | `UNKNOWN` | Closure resolver, promotion checks, release manifests, negative tests. |
| Correction propagation | `UNKNOWN` | Dependency graph, invalidation records, cache/public derivative tests. |
| Deactivation and rollback drills | `UNKNOWN` | Runbook, fixtures, executed drill, receipt, verified recovery target. |
| Named owners and separation of duties | `NEEDS VERIFICATION` | CODEOWNERS plus accepted steward roles and enforcement. |
| Production execution and public effects | `UNKNOWN` | Deployment, logs, metrics, dashboards, release state, incidents. |

[Back to top](#top)

---

## Evidence ledger

| Evidence | Observation | Status |
|---|---|---:|
| This README at the pinned base | Existing v0.3 root contract; prior blob recorded in metadata. | `CONFIRMED` |
| [Directory Rules section 15](../docs/doctrine/directory-rules.md#15-required-readme-contract) | Canonical root READMEs require twelve sections in a fixed order. | `CONFIRMED doctrine` |
| [`pipelines/README.md`](../pipelines/README.md) | Current executable-root v0.3 documents placeholder-heavy lanes, non-publisher posture, receipt family, and open implementation gaps. | `CONFIRMED` |
| [`pipelines/specs/README.md`](../pipelines/specs/README.md) | Compatibility guardrail; active declarative discovery is prohibited there. | `CONFIRMED` |
| Agriculture and Soil stage samples | `stages: []` empty-stage scaffold shape. | `CONFIRMED samples` |
| Fauna, Flora, Hazards, Hydrology, Habitat samples | Short `status: PROPOSED` documentation-inventory placeholder shape. | `CONFIRMED samples` |
| [`watchers/README.md`](watchers/README.md) | Shared placeholder-only watcher boundary with placement conflicts and non-publisher constraints. | `CONFIRMED` |
| [`tests/pipelines/README.md`](../tests/pipelines/README.md) | Cross-cutting test boundary remains README-only at its snapshot. | `CONFIRMED` |
| [`test_pipeline_connector_non_publisher.py`](../tests/policy/test_pipeline_connector_non_publisher.py) | Executable bounded static guard exists for connector/pipeline publish-target write contexts. | `CONFIRMED code` |
| [`RunReceipt` contract](../contracts/runtime/run_receipt.md) | PROPOSED semantic receipt contract; schema pairing and field surface documented. | `CONFIRMED file / PROPOSED contract` |
| [`RunReceipt` schema](../schemas/contracts/v1/runtime/run_receipt.schema.json) | Closed object with required refs, `spec_hash`, and `SUCCESS/PARTIAL/FAIL`. | `CONFIRMED shape / PROPOSED status` |
| [`RunReceipt` validator](../tools/validators/validate_run_receipt.py) | Repository-owned wrapper points to schema and fixture root. | `CONFIRMED code` |
| [Workflow inventory](../.github/workflows/README.md) | Broad workflow inventory exists; current run results and dedicated spec enforcement remain unproved. | `CONFIRMED documentation / execution NEEDS VERIFICATION` |
| Bounded search for pipeline-spec schema/parser/registry | No accepted root shape or active parser/registry surfaced. | `CONFIRMED bounded no-result` |
| [CODEOWNERS](../.github/CODEOWNERS) | Root review routing exists; enforcement and correct steward review remain unverified. | `CONFIRMED routing` |
| [Generated receipts](../data/receipts/generated/README.md) | AI-authored provenance lane exists; receipts are process memory, not approval or implementation proof. | `CONFIRMED` |

### Evidence limits

Repository search is bounded and may lag branch-local content. Checked absence is not a full-history, ignored-file, generated-file, dynamic-discovery, or external-system assertion. Child READMEs can be stale. No clone, repository-native spec test run, workflow run inspection, branch-protection query, source system, scheduler, deployment, dashboard, or production runtime was inspected for this documentation revision.

[Back to top](#top)

---

## v0.3 to v0.4 no-loss ledger

| v0.3 material | v0.4 disposition |
|---|---|
| Declarative versus executable separation | Preserved and strengthened under Purpose and Authority level. |
| Current maturity and bounded inventory | Preserved under Status and Bounded root inventory. |
| Empty-stage and documentation-inventory placeholder taxonomy | Preserved under Payload taxonomy with clearer activation consequences. |
| Seventeen direct lane registry | Preserved under Related folders; still bounded and non-activating. |
| Air, People, Settlement, watcher, historical-path, and Directory Rules conflicts | Preserved under Compatibility and placement conflicts. |
| Minimum active spec contract | Preserved and expanded with canonicalization, consumer compatibility, receipt joins, and proof. |
| Lifecycle, source, and release gates | Preserved and reconciled with current pipeline and ADR evidence. |
| Finite outcomes | Preserved as a concern but separated into distinct spec, run, runtime, lifecycle, and release vocabularies. |
| Validation and CI limitations | Preserved and updated with the static non-publisher guard and RunReceipt validator boundary. |
| Review, versioning, migration | Preserved under Review burden, ADRs, conflicts, and rollback. |
| Correction, deactivation, rollback | Preserved and expanded with dependency invalidation obligations. |
| Definition of done | Preserved and expanded. |
| Open verification register and evidence ledger | Preserved and refreshed. |
| Change history | Preserved below. |

No stable identity, canonical path, lane link, conflict, uncertainty, governance boundary, or rollback posture was intentionally removed.

### v0.4 — 2026-07-23

- reordered the first twelve H2 sections to match Directory Rules section 15 exactly;
- reconciled the declarative root with the current pipelines v0.3 and pipelines/specs v0.2 contracts;
- added current static non-publisher and RunReceipt contract/schema/validator evidence;
- separated specification maturity, validation, run receipt, runtime response, lifecycle, and release vocabularies;
- strengthened inputs, outputs, public-client denial, activation anti-collapse, review burden, and invalidation/rollback guidance;
- preserved all v0.3 inventory, payload, lane, conflict, definition-of-done, open-verification, and evidence content;
- changed documentation and generated provenance only.

### v0.3 — 2026-07-18

- replaced the planning tree with a repository-grounded maturity and routing boundary;
- recorded seventeen direct README lanes and five nested lanes;
- classified placeholder and compatibility shapes;
- surfaced alias, watcher, historical path, and inventory-freshness conflicts;
- strengthened source, lifecycle, parser/consumer, sensitive-domain, validation, correction, and rollback requirements;
- added lane registry, definition of done, open verification register, and evidence ledger;
- changed documentation only.

### v0.2 — 2026-06-13

- expanded the root stub into a governed declarative configuration contract;
- defined declarative/executable separation, lifecycle gates, anti-collapse rules, a recommended tree, minimal profile example, and open questions.

<p align="right"><a href="#top">Back to top</a></p>
