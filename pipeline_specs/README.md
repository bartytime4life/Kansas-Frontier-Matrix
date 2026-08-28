<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-readme
title: pipeline_specs/ — Governed Declarative Pipeline Specification Root
type: readme; root-readme; canonical-pipeline-spec-root; declarative-activation-boundary; compatibility-drift-index
version: v0.5
status: draft; repository-grounded; canonical-root-confirmed; mixed-maturity; selected-fixture-first-validation-confirmed; no-general-active-spec-registry-or-live-activation-established; non-authoritative
owners:
  - OWNER_TBD — Pipeline-spec steward
  - OWNER_TBD — Pipeline steward
  - OWNER_TBD — Domain stewards
  - OWNER_TBD — Source and rights steward
  - OWNER_TBD — Contract and schema steward
  - OWNER_TBD — Validation and CI steward
  - OWNER_TBD — Evidence and receipt steward
  - OWNER_TBD — Policy and sensitivity steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Security reviewer
  - OWNER_TBD — Docs steward
created: 2026-06-13
updated: 2026-08-08
supersedes: v0.4
prepared_under_prompt: KFM Repository Build-Out & Markdown Modernization Implementation Agent v6.0.0
policy_label: "public-doc; pipeline-specs-root; declarative-only; no-secrets; no-live-activation; no-direct-fetch; no-direct-admission; no-direct-lifecycle-write; no-direct-release; source-role-aware; rights-aware; sensitivity-aware; evidence-bound; policy-gated; review-gated; correction-aware; rollback-aware"
current_path: pipeline_specs/README.md
truth_posture: >-
  CONFIRMED current same-path README, pipeline_specs tree, seventeen direct child lanes,
  five nested README sublanes, selected deterministic fixture-first profiles and validators,
  current Directory Rules README contract, executable-pipeline boundary, generated-receipt
  requirement, and absence of an open pull request touching this file at the pinned base /
  PROPOSED root-wide semantic contract, schema, canonicalizer, active-spec registry,
  parser/consumer compatibility contract, source-activation binding, common reason-code
  registry, correction invalidation, and rollback automation /
  CONFLICTED legacy aliases, shared-versus-domain watcher placement, child README freshness,
  current Directory Rules copy versus proposed successor, historical pipeline_specs/domains
  references, and overlapping state vocabularies /
  UNKNOWN live schedules, exhaustive runtime consumption, production execution, emitted
  receipts for every lane, branch-protection enforcement, deployments, release use, and public
  effects /
  NEEDS VERIFICATION named owners, accepted activation authority, complete consumer matrix,
  source rights and sensitivity decisions, root-wide fixture coverage, hosted workflow results,
  correction propagation, rollback drills, and first live governed activation
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  visibility: public
  base_ref: main
  base_commit: fa6da59b62aeb16336e889eebf93a3cab82f919e
  prior_blob: de6919212a75dd626f9a786c3fb83d7539ff41e9
  pipeline_specs_tree: 2347e92509e3a4c81fd55e03d08cf36e83a2ae33
  current_directory_rules: docs/architecture/directory-rules.md v1.3.1
  proposed_successor_directory_rules: docs/doctrine/directory-rules.md v2.0.0-draft.1
  bounded_direct_child_lanes: 17
  bounded_nested_readmes: 5
  open_prs_touching_target: 0
  inventory_method: GitHub connector exact file reads, commit-pinned tree inspection, bounded code search, and current open-PR/branch reconciliation
related:
  - ../CONTRIBUTING.md
  - ../SECURITY.md
  - ../docs/architecture/directory-rules.md
  - ../docs/doctrine/directory-rules.md
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
  - ../tools/validators/validate_run_receipt.py
  - ../data/receipts/generated/README.md
  - ../schemas/contracts/v1/receipts/generated_receipt.schema.json
  - ../.github/PULL_REQUEST_TEMPLATE.md
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
tags:
  - kfm
  - pipeline-specs
  - declarative-configuration
  - fixture-first
  - activation
  - pipelines
  - source-admission
  - lifecycle
  - receipts
  - evidence
  - policy
  - validation
  - correction
  - rollback
  - migration
notes:
  - "v0.5 refreshes the root README against current main and preserves the canonical declarative/executable split."
  - "Selected inactive or fixture-first profiles now have repository-backed contracts, schemas, validators, tests, or workflows; this does not establish a general active-spec system."
  - "The current v1.3.1 Directory Rules README order is preserved. The v2.0.0 draft is recorded as a proposed successor and is not treated as adopted."
  - "This change modifies this README and its required generated provenance receipt only."
  - "No specification payload, parser, consumer, source, policy, workflow, lifecycle object, release object, deployment, or public artifact is activated or changed."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>
<a id="pipeline-specs"></a>

# `pipeline_specs/` — Governed Declarative Pipeline Specification Root

> **One-line purpose.** Own the governed declarative intent for **what** a KFM pipeline may attempt—identity, admitted inputs, lifecycle transitions, constraints, evidence and policy prerequisites, expected outcomes, receipts, correction duties, and rollback targets—without becoming executable code, source authority, lifecycle storage, release approval, or a public serving surface.

<p>
  <a href="#status"><img alt="Status: repository-grounded draft" src="https://img.shields.io/badge/status-repository--grounded%20draft-yellow"></a>
  <a href="#authority-level"><img alt="Root: canonical pipeline specs" src="https://img.shields.io/badge/root-pipeline__specs%2F-blue"></a>
  <a href="#status"><img alt="Maturity: mixed" src="https://img.shields.io/badge/maturity-mixed-orange"></a>
  <a href="#validated-inactive-and-fixture-first-slices"><img alt="Selected fixture-first validation: confirmed" src="https://img.shields.io/badge/fixture--first-selected__slices-success"></a>
  <a href="#status"><img alt="General active specification registry: not established" src="https://img.shields.io/badge/active__registry-not__established-critical"></a>
  <a href="#outputs"><img alt="Publication authority: denied" src="https://img.shields.io/badge/publication-DENIED-red"></a>
  <a href="#validation"><img alt="Truth posture: cite or abstain" src="https://img.shields.io/badge/truth-cite__or__abstain-success"></a>
</p>

> [!IMPORTANT]
> **A file is not an active specification.** Current repository evidence includes empty-stage scaffolds, short proposed inventory files, schema-paired inactive profiles, and one explicit fixture-first implementation binding. Each class has a different proof burden. None authorizes live source access, lifecycle writes, promotion, release, or publication.

> [!CAUTION]
> **Keep the responsibility layers separate.** `pipeline_specs/` declares **what may run**; [`pipelines/`](../pipelines/README.md) implements **how governed execution occurs**; [`pipelines/specs/`](../pipelines/specs/README.md) is a compatibility guardrail and must not become a second specification authority.

> [!WARNING]
> **Secrets and restricted material never belong in specifications, examples, logs, receipts, issues, or pull requests.** Credentials, private endpoints, source payloads, protected coordinates, living-person or DNA data, rare-species or rare-plant locations, archaeology or cultural knowledge, private-land joins, infrastructure vulnerabilities, and unreviewed source terms require approved handling outside ordinary public repository surfaces.

**Quick navigation**

| Root contract | Trust and activation | Maintenance |
|---|---|---|
| [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) | [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Operating model](#operating-model-and-activation-boundary) · [Contract](#minimum-active-spec-contract) | [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed) · [Conflicts](#compatibility-and-placement-conflicts) · [Rollback](#correction-deactivation-and-rollback) |

---

## Purpose

`pipeline_specs/` is the canonical KFM responsibility root for declarative pipeline configuration and activation intent.

It answers five questions:

1. Which stable specification identity and version is being requested?
2. Which admitted sources, lifecycle inputs, contracts, schemas, policies, and consumers does it depend on?
3. Which transitions, side effects, resource limits, network posture, and finite outcomes are permitted?
4. Which reports, receipt facts, evidence checks, review states, correction obligations, and rollback targets are required?
5. How can the declaration be disabled, superseded, migrated, replayed, or retired without rewriting history?

A specification does not execute itself. Executable logic belongs under [`pipelines/`](../pipelines/README.md), an admitted shared package, or another verified implementation root.

This README does not activate any payload, define an accepted root-wide pipeline-spec schema, create a parser or scheduler, admit a source, prove a claim, approve a release, or publish a product.

[Back to top](#top)

---

## Authority level

**Canonical declarative pipeline-specification root; non-authoritative for execution, evidence, policy, lifecycle promotion, release, and publication.**

The current Directory Rules artifact at [`docs/architecture/directory-rules.md`](../docs/architecture/directory-rules.md) assigns `pipeline_specs/` and `pipelines/` separate responsibilities and requires this root README to preserve the ordered contract used here. The newer [`docs/doctrine/directory-rules.md`](../docs/doctrine/directory-rules.md) is a `PROPOSED_FOR_ADOPTION` successor and has no supersession effect until accepted.

```text
pipeline_specs/  = WHAT may run and under which declared gates
pipelines/       = HOW governed execution occurs
```

| Concern | Owning authority | Role of a pipeline spec |
|---|---|---|
| Executable behavior | [`pipelines/`](../pipelines/README.md), admitted packages, governed applications | References a compatible consumer; never implements it. |
| Source access | `connectors/` | Names admitted source references; never fetches or activates a source. |
| Source identity, role, rights, activation | Accepted registry and source-decision surfaces | Resolves governed IDs and prerequisites; never creates permission. |
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
| `pipeline_specs/` | Canonical declarative root | Authoritative specification work lands here after contract, placement, and activation review. |
| [`pipelines/`](../pipelines/README.md) | Canonical executable root | Implements governed execution; must not absorb declarative authority. |
| [`pipelines/specs/`](../pipelines/specs/README.md) | Compatibility and migration guardrail | Do not add active specifications or fallback discovery here. |
| `pipeline_specs/air/` | Compatibility-oriented lane | Do not create parallel authority with Atmosphere. |
| `pipeline_specs/people/` | Compatibility alias | Do not create a lighter path around People/DNA/Land controls. |
| `pipeline_specs/settlement/` | Compatibility alias | Do not create parallel authority with Settlements/Infrastructure. |

Changing the canonical split, creating another active spec root, or silently promoting an alias requires the decision and migration burden established by adopted governance.

[Back to top](#top)

---

## Status

### Evidence snapshot

| Field | Value |
|---|---|
| Base | `main@fa6da59b62aeb16336e889eebf93a3cab82f919e` |
| Prior README blob | `de6919212a75dd626f9a786c3fb83d7539ff41e9` |
| `pipeline_specs/` tree | `2347e92509e3a4c81fd55e03d08cf36e83a2ae33` |
| Current document version before this change | `v0.4` |
| Direct child lanes | `17` |
| Nested README sublanes | `5` |
| Open pull requests touching this path at discovery time | `0` |
| Inventory posture | Commit-pinned and recursive for this root; runtime and all-branch behavior remain outside the evidence boundary |
| Implementation effect of this revision | Documentation and generated provenance only |

### Confirmed current state

- The root remains a mixed-maturity declarative surface.
- Empty-stage scaffolds remain present across several domain lanes.
- Short `status: PROPOSED` inventory candidates remain present for source or domain ideas.
- Selected JSON profiles now have real `spec_hash` values and paired contracts, schemas, validators, tests, fixtures, or workflows.
- `pipeline_specs/hydrology/wbd_huc12_ingest.yaml` explicitly binds a deterministic, no-network fixture-first candidate producer and dedicated workflow while denying live source access and lifecycle writes.
- Soil now contains several inactive, fixture-bound governance profiles for support types, time caveats, materiality, and yearly diff behavior.
- The shared watcher lane includes an inactive Soil SSURGO/gNATSGO watcher specification with source, support-type, QA, materiality, receipt, and finite-zone declarations, while all execution and publication authority remains false.
- Flora source-readiness and Habitat land-cover materiality profiles remain `PROPOSED_INACTIVE`; their presence does not activate sources or publish outputs.
- A common, accepted root-wide specification schema, canonicalizer, active-spec registry, discovery mechanism, parser compatibility registry, scheduler, or live activation authority is still not established by the inspected evidence.
- CODEOWNERS routing exists, but routing is not domain stewardship approval, source admission, activation, release, or publication authority.

### Maturity matrix

| Capability | Current posture | Safe conclusion |
|---|---:|---|
| Root README | `CONFIRMED` | Canonical responsibility and safety boundary exist. |
| Child README network | `CONFIRMED, bounded` | Mixed domain, alias, watcher, and sublane docs exist; freshness varies. |
| Declarative payload files | `CONFIRMED` | Multiple payload classes exist and must not be collapsed. |
| Empty-stage scaffolds | `CONFIRMED` | Placeholder stage shells remain; they declare no executable graph. |
| Proposed inventory candidates | `CONFIRMED` | Planned paths or source ideas exist; they are not active specs. |
| Selected inactive profile validation | `CONFIRMED` | Some profiles have contract/schema/validator/test/workflow closure. |
| Hydrology WBD HUC12 fixture-first binding | `CONFIRMED` | Deterministic local candidate production is implemented; live source and lifecycle effects remain denied. |
| Accepted root-wide pipeline-spec schema | `NOT ESTABLISHED` | No single active shape may be inferred for all files. |
| Canonicalization and digest policy | `PARTIAL` | Selected profiles declare canonicalization and hashes; no root-wide accepted profile is established. |
| Parser and active-spec registry | `NOT ESTABLISHED` | Directory scanning remains unsafe activation. |
| Consumer/version binding | `PARTIAL` | WBD HUC12 names an implementation; a complete consumer matrix is absent. |
| Source activation binding | `NOT ESTABLISHED ROOT-WIDE` | Inactive profiles can point to source records but cannot self-admit them. |
| Dedicated profile fixtures and tests | `SELECTED SLICES` | Several focused validators/workflows exist; root-wide coverage is absent. |
| Current live specifications | `NOT ESTABLISHED` | Fixture-first or inactive status must remain visible. |
| Scheduler, production execution, public effects | `UNKNOWN` | No deployment or publication claim is supported. |

> [!NOTE]
> The repository has advanced beyond the v0.4 phrase “dedicated specification tests not established” in a narrow sense: selected profiles now have dedicated validation. It has **not** advanced to a general active-spec platform. This distinction is the central v0.5 correction.

[Back to top](#top)

---

## What belongs here

The root and its reviewed lanes may contain:

- this root README and lane-level READMEs;
- declarative YAML, JSON, TOML, or another admitted specification format;
- stable specification identity, semantic version, declared maturity, owner roles, digest, and supersession metadata;
- references to admitted sources, contracts, schemas, policies, lifecycle inputs, evidence requirements, review records, receipt profiles, release prerequisites, and rollback targets;
- declarative stage or dependency graphs that a named, compatible consumer can interpret deterministically;
- cadence, freshness, valid-time, source-vintage, stale-state, no-op, retry, cancellation, and resource-limit declarations;
- explicit network, filesystem, tool, side-effect, and data-minimization posture;
- finite spec-validation expectations and stable reason-code references;
- compatibility maps, deprecation notices, and migration pointers that name one canonical target and do not evolve independently;
- synthetic, local, fixture-first profiles when clearly marked inactive and denied all live/public authority.

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

A new implementation-bearing payload must identify its responsibility, consumer, source, rights, sensitivity, tests, receipts, migration, correction, and rollback posture. Missing answers mean `HOLD`, not implicit admission.

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
- deterministic canonical bytes and a `spec_hash` under a declared, validated profile;
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
- A fixture-first implementation is not live source activation.
- A run receipt is process memory, not evidence or release approval.
- A successful pipeline run is not lifecycle promotion.
- A release candidate is not `PUBLISHED`.
- A public client must never discover or render specifications directly.

[Back to top](#top)

---

## Validation

Validation must separate **document presence, specification shape, canonical identity, bindings, behavior, policy, integration, and release readiness**.

### Current profile-specific executable evidence

| Slice | Repository-backed validation | Authority boundary |
|---|---|---|
| Soil support-type profile | `tools/validators/domains/soil/support_type/validate_support_type_profile.py`, paired schemas, fixture tree, and `soil-support-type-profile` workflow | Fixture-only, no public use, no evidence/policy/promotion/release authority |
| Soil support-type alias map | Dedicated validator, schema, and workflow | Alias mapping cannot create source or claim authority |
| Soil time-caveat profile | Dedicated contract, validator, and workflow | Temporal caveat validation does not prove source freshness |
| Soil promotion-materiality profile | Contract, schema, validator, tests, and workflow | Materiality result is not PromotionDecision or release approval |
| Soil SSURGO yearly-diff profile | Contract, schema, validator, tests, and workflow | Fixture-only diff result targets WORK; all activation and publication authority false |
| Soil SSURGO/gNATSGO watcher spec | Schema, validator, tests, workflow, and watcher-registry reference | Watcher is inactive and non-publishing; unknowns quarantine |
| Hydrology WBD HUC12 ingest candidate | Named deterministic producer, focused tests, and dedicated workflow | Fixture-only; network, lifecycle persistence, promotion, release, and publication denied |
| Flora source-readiness materiality | Contract, schemas, validator, and workflow | Profile is inactive and cannot activate a source |
| Habitat land-cover materiality | Contract and schema paired to an inactive profile | Dedicated executable validator/workflow was not established by the bounded search |

These slices prove specific, bounded behavior. They do not establish a universal specification grammar, global active registry, compatible consumer inventory, scheduler, or production deployment.

### Representative focused commands

Run only in a reviewed checkout with repository dependencies installed from the lockfile:

```bash
python tools/validators/domains/soil/support_type/validate_support_type_profile.py --fixtures

python -m pytest \
  tests/validators/domains/soil/test_validate_ssurgo_yearly_diff_profile.py \
  tests/validators/domains/soil/watcher_spec/test_validate_soil_watcher_spec.py \
  tests/validators/test_validate_soil_promotion_materiality.py \
  -q --strict-config --strict-markers

python -m pytest \
  tests/pipelines/domains/hydrology/test_wbd_huc12_ingest_candidate.py \
  tests/validators/domains/hydrology/wbd_huc12_material_change/test_validate_wbd_huc12_material_change.py \
  -q --strict-config --strict-markers

python tools/validators/validate_generated_receipt.py \
  data/receipts/generated/<receipt>.json

git diff --check
```

> [!NOTE]
> These commands are changed-area examples, not a claim that they were executed by this README. Hosted workflows remain separate evidence and may be pending on a draft pull request.

### Required root-wide specification validation layers

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

| Layer | Current or proposed vocabulary | Authority note |
|---|---|---|
| Specification maturity | `inventory_placeholder`, `stage_scaffold`, `proposed_inactive`, `implemented_fixture_first`, `candidate`, `active_internal`, `active_public_candidate`, `deprecated`, `disabled`, `retired` | Root-wide vocabulary remains PROPOSED. |
| Spec-validation decision | `PASS`, `HOLD`, `DENY`, `ERROR` plus controlled reasons | Must not be reused as runtime or release state. |
| Pipeline `RunReceipt.outcome` | `SUCCESS`, `PARTIAL`, `FAIL` | Receipt surface; not source or release authority. |
| Governed runtime response | `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` where applicable | Public/runtime envelope, not a pipeline-spec state. |
| Lifecycle | `RAW`, `WORK`, `QUARANTINE`, `PROCESSED`, `CATALOG`, `TRIPLET`, `PUBLISHED` | Governed state transition, not a parser result. |
| Promotion/release decision | Vocabulary defined by accepted promotion and release contracts | Independent authority; a spec never self-promotes. |

A future shared contract must define mappings explicitly. Similar words do not imply equivalent meaning.

### Documentation validation for this revision

This README change must pass:

- UTF-8 and LF normalization;
- exactly one H1;
- the twelve current Directory Rules root sections in exact order;
- balanced fenced blocks and HTML tags;
- unique custom anchors and resolvable internal fragments;
- repository-relative link review for introduced destinations;
- no credential-like or sensitive payload introduction;
- semantic no-loss review against v0.4;
- generated-receipt artifact/hash closure;
- remote readback and diff verification after mutation.

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

The same actor must not be the sole generator, validator, merger, activator, operator, and release approver for a policy-significant specification. Activation and release decisions remain independent from authoring, parser success, CI success, and merge.

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
| `data/registry/` | Source identity, role, rights, sensitivity, cadence, and activation records. |
| `data/receipts/` | Process-memory receipt families. |
| `data/proofs/` | Proof objects; distinct from receipts and specs. |
| `data/catalog/` and `data/triplets/` | Derived discovery and relation surfaces after governed closure. |
| `release/` | Promotion, release, correction, withdrawal, and rollback decisions. |
| `runtime/` and governed applications | Bounded execution and serving behind the trust membrane. |

### Validation counterparts

| Path | Relationship |
|---|---|
| [`contracts/runtime/run_receipt.md`](../contracts/runtime/run_receipt.md) | Semantic receipt contract for a governed run/stage. |
| [`schemas/contracts/v1/runtime/run_receipt.schema.json`](../schemas/contracts/v1/runtime/run_receipt.schema.json) | Paired machine shape. |
| [`tools/validators/validate_run_receipt.py`](../tools/validators/validate_run_receipt.py) | Receipt validator wrapper. |
| [`tests/policy/test_pipeline_connector_non_publisher.py`](../tests/policy/test_pipeline_connector_non_publisher.py) | Bounded static no-direct-publish guard. |
| [`data/receipts/generated/`](../data/receipts/generated/README.md) | AI-authored artifact provenance lane; not implementation proof. |
| [`schemas/contracts/v1/receipts/generated_receipt.schema.json`](../schemas/contracts/v1/receipts/generated_receipt.schema.json) | Generated-receipt machine shape. |
| [Pull-request template](../.github/PULL_REQUEST_TEMPLATE.md) | Requires a generated receipt for AI-authored diff files. |

### Direct lane registry

| Lane | Current bounded posture | Governing issue |
|---|---|---|
| [`agriculture/`](agriculture/README.md) | Stage scaffolds plus a short NASS candidate. | Aggregate versus field/operator specificity; inventory drift. |
| [`air/`](air/README.md) | Compatibility guardrail. | Avoid parallel authority with Atmosphere. |
| [`archaeology/`](archaeology/README.md) | Sensitive-domain boundary with stage and `.spec.yaml` candidates. | Sovereignty, cultural review, exact locations, rights. |
| [`atmosphere/`](atmosphere/README.md) | Preferred Atmosphere/Air lane; stage scaffolds. | Observation/model/advisory and life-safety separation. |
| [`fauna/`](fauna/README.md) | Stage scaffolds, refresh candidate, nested watcher guidance. | Rare-species geoprivacy. |
| [`flora/`](flora/README.md) | Source candidates, dry-run/watcher declarations, inactive source-readiness profile. | Rare plants, cultural/stewardship rights, watcher placement. |
| [`geology/`](geology/README.md) | Stage scaffolds and six `.spec.yaml` candidates. | Observation/deposit/resource/reserve/production distinctions. |
| [`habitat/`](habitat/README.md) | Source candidates and inactive land-cover materiality profile. | Habitat context is not species occurrence. |
| [`hazards/`](hazards/README.md) | Stage and source-oriented candidates. | Not emergency or official-alert authority. |
| [`hydrology/`](hydrology/README.md) | Stage/source candidates plus fixture-first WBD HUC12 binding. | Observation/model/regulatory-context separation. |
| [`people-dna-land/`](people-dna-land/README.md) | Governing sensitive lane with stage scaffolds and land-ownership sublane. | Living-person, consent/revocation, DNA, title boundaries. |
| [`people/`](people/README.md) | README-only alias. | No lighter or parallel sensitive-data path. |
| [`roads-rail-trade/`](roads-rail-trade/README.md) | Stage and source candidates. | Network identity, operating status, infrastructure sensitivity. |
| [`settlement/`](settlement/README.md) | README-only alias. | No parallel authority. |
| [`settlements-infrastructure/`](settlements-infrastructure/README.md) | Governing lane with stage scaffolds. | Legal/operational status and infrastructure sensitivity. |
| [`soil/`](soil/README.md) | Stage scaffolds plus multiple validated inactive governance profiles. | Static survey/grid/station/satellite/pedon/interpretation separation. |
| [`watchers/`](watchers/README.md) | Shared watcher lane with inactive Soil watcher profile and gate profile. | Shared/domain delegation and non-publisher rule. |

The registry is orientation, not an activation database. Child README descriptions may lag current files; the current tree and direct implementation evidence control current-state claims.

[Back to top](#top)

---

## ADRs

The records below are repository-present. Their operative status must be read from the current artifact and accepted decision index; this README does not adopt them.

| Record | Pipeline-spec consequence |
|---|---|
| [`ADR-0001 — schema home`](../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) | Machine shapes belong under `schemas/contracts/v1/...`, not beside specs. |
| [`ADR-0011 — receipts, proofs, manifests, catalogs`](../docs/adr/ADR-0011-receipts-vs-proofs-vs-manifests-vs-catalog-separation.md) | A spec or receipt must not become proof, catalog, or publication authority. |
| [`ADR-0012 — connector outputs`](../docs/adr/ADR-0012-connector-outputs-to-data-raw-or-data-quarantine-only.md) | Source-edge output and later pipeline intent remain separate; connectors do not publish. |
| [`ADR-0017 — source descriptor admission`](../docs/adr/ADR-0017-source-descriptor-admission-process.md) | Source identity, role, rights, sensitivity, and activation precede use. |
| [`ADR-0018 — promotion gate sequence`](../docs/adr/ADR-0018-promotion-gate-sequence.md) | A spec may name readiness gates but cannot pass or approve them by declaration. |
| [`ADR-0021 — structured quarantine exits`](../docs/adr/ADR-0021-quarantine-has-structured-exit-paths.md) | Quarantine transitions require named governed exits; no silent release. |
| [`ADR-0022 — STAC/DCAT/PROV agreement`](../docs/adr/ADR-0022-catalog-matrix--stac-+-dcat-+-prov-must-agree.md) | Catalog closure remains downstream and independently validated. |

### Decisions still needed

- accepted root-wide pipeline-spec semantic contract and schema family;
- canonicalization algorithm and `spec_hash` profile across object families;
- stable ID, version, state, reason-code, and activation vocabularies;
- parser, discovery, active-spec registry, and consumer compatibility contract;
- alias disposition for Air, People, and Settlement;
- shared/domain watcher placement and plants-drift duplication;
- historical `pipeline_specs/domains/...` reference disposition;
- source registry and activation-decision topology;
- receipt joins from spec to execution, validation, evidence, catalog, and release;
- root-wide fixture/test/CI contract;
- correction invalidation, deactivation, migration, and rollback automation;
- adoption or rejection of Directory Rules v2.0.0-draft.1.

Do not create a parallel authority while these decisions remain open.

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-08-08 |
| Evidence base | `main@fa6da59b62aeb16336e889eebf93a3cab82f919e` |
| Prior target blob | `de6919212a75dd626f9a786c3fb83d7539ff41e9` |
| Review mode | Same-path repository-grounded Markdown modernization with direct generated-receipt dependency |
| Prompt | KFM Repository Build-Out & Markdown Modernization Implementation Agent v6.0.0 |
| Implementation effect | None — no spec, parser, source, pipeline, policy, test, workflow, data, release, runtime, or public state changed |
| Rollback | Before merge, close or abandon the draft PR; after merge, revert the implementation commit and its generated receipt |

### Maintenance triggers

Re-review this README when:

- a root-wide pipeline-spec schema, canonicalizer, parser, registry, or consumer contract becomes accepted;
- a specification moves beyond inactive/fixture-first/candidate state;
- a source activation or rights/sensitivity binding changes;
- a dedicated shared fixture/test lane or root-wide CI gate is introduced;
- an alias, watcher lane, or compatibility path moves, retires, or gains implementation;
- RunReceipt or another execution/validation receipt profile changes;
- correction, invalidation, deactivation, migration, or rollback behavior becomes executable;
- branch protection or CODEOWNERS enforcement changes;
- adopted Directory Rules or an accepted ADR changes the canonical responsibility split.

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

Every arrow after the declarative candidate is outside the authority of the file itself. Selected fixture-first slices implement parts of this flow locally; the root-wide chain remains incomplete.

### Activation anti-collapses

```text
path exists                     != accepted specification
JSON/YAML parses                != schema-valid specification
schema-valid                    != admitted source
fixture-first implementation    != live-source activation
merge completed                 != activation approved
schedule declared               != scheduler configured
consumer named                  != compatibility proven
pipeline run succeeded          != evidence closure
RunReceipt validates            != policy or release approval
release candidate exists        != PUBLISHED
public client can fetch a file  != governed public delivery
```

Directory scanning alone is unsafe activation because the root contains placeholders, aliases, compatibility lanes, inactive profiles, and multiple vocabularies.

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
│   └── watchers/
├── flora/
│   ├── source_readiness/
│   └── watchers/
├── geology/
├── habitat/
│   ├── ecoregions/
│   └── land_cover/
├── hazards/
├── hydrology/
├── people-dna-land/
│   └── land-ownership/
├── people/                      # compatibility alias
├── roads-rail-trade/
├── settlement/                  # compatibility alias
├── settlements-infrastructure/
├── soil/
└── watchers/                    # shared intent; placement-sensitive
```

This direct tree is confirmed at the pinned base. It is not an activation manifest. Before deletion, migration, or live activation, compare it with registries, consumers, workflows, receipts, release dependencies, and inbound references.

[Back to top](#top)

---

## Payload maturity taxonomy

### 1. Documentation-inventory candidate

```yaml
status: PROPOSED
source_doc: docs/domains/example/MISSING_OR_PLANNED_FILES.md
path: pipeline_specs/example/example.yaml
notes:
  - Placeholder created from a documentation inventory.
```

This proves a planned reference. It does not establish stable identity, schema, parser, source, lifecycle, consumer, schedule, fixture, receipt, activation, or release behavior.

### 2. Empty-stage scaffold

```yaml
name: agriculture-normalize
version: 1
stages: []
```

This proves a minimal shell. An empty stage list declares no operation graph, inputs, outputs, constraints, source refs, policy, evidence, receipt, or rollback behavior.

### 3. Inactive governance profile

An inactive profile may have a schema, deterministic hash, validator, fixtures, tests, and CI while explicitly denying activation, public use, promotion, and release. This is meaningful implementation, but its authority is bounded to validation of the profile and its candidates.

### 4. Implemented fixture-first binding

A fixture-first spec may name an executable producer, tests, and workflow while denying network access, lifecycle persistence, promotion, release, and publication. It proves local behavior only.

### 5. Active governed specification

No file is upgraded to this class by this README. An active specification must satisfy the minimum contract, validation, review, activation, correction, and rollback requirements below.

[Back to top](#top)

---

## Validated inactive and fixture-first slices

| Slice | Current declaration | Confirmed direct dependencies | What remains denied or unknown |
|---|---|---|---|
| Soil support-type profile | `PROPOSED_INACTIVE` | Profile, candidate schema, validator, fixtures, workflow | Source activation, evidence closure, policy, promotion, release, public use |
| Soil support-type alias map | Inactive compatibility mapping | Schema, validator, workflow | Canonical source/claim authority |
| Soil time-caveat profile | `PROPOSED_INACTIVE` | Contract, validator, workflow | Live freshness proof and source activation |
| Soil promotion-materiality profile | `PROPOSED_INACTIVE` | Contract, schema, validator, tests, workflow | PromotionDecision and release authority |
| Soil SSURGO yearly-diff profile | `PROPOSED_INACTIVE`, `FIXTURE_ONLY` | Contract, schema, validator, tests, workflow | Network, source activation, RAW admission, promotion, release, publication |
| Soil SSURGO/gNATSGO watcher | `PROPOSED_INACTIVE`, `FIXTURE_ONLY` | Registry reference, schema, validator, tests, workflow | Execution, network, activation, lifecycle admission, promotion, publication |
| Hydrology WBD HUC12 ingest candidate | `PROPOSED`, `IMPLEMENTED_FIXTURE_FIRST` | Named producer, contracts, schemas, tests, workflow | Live WBD request, lifecycle persistence, evidence closure, promotion, release, publication |
| Flora source-readiness materiality | `PROPOSED_INACTIVE` | Contract, schemas, validator, workflow | Source activation, policy, promotion, public use |
| Habitat land-cover materiality | `PROPOSED_INACTIVE` | Contract and schema | Dedicated executable validation and workflow remain NEEDS VERIFICATION |

### Soil support-type anti-collapse

The current support profile explicitly distinguishes:

- authoritative static soil survey;
- governed change evidence;
- gridded derivative soil;
- pedon/profile evidence;
- reference-station soil climate;
- satellite soil-moisture grid;
- soil interpretation;
- station soil moisture.

A profile or consumer must preserve those roles. Static survey, station condition, satellite grid, and interpretation cannot silently substitute for one another.

[Back to top](#top)

---

## Minimum active spec contract

An active specification requires at least:

| Area | Requirement |
|---|---|
| Identity | Stable ID, semantic version, state, owners, digest, supersession lineage. |
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
- **Current versus proposed Directory Rules:** `docs/architecture/directory-rules.md` v1.3.1 remains the current placement artifact used for this same-path edit; `docs/doctrine/directory-rules.md` v2.0.0-draft.1 is proposed and cannot authorize dependent changes before adoption.
- **`air/` versus `atmosphere/`:** current documentation prefers Atmosphere; duplicate active authority is denied.
- **`people/` versus `people-dna-land/`:** People remains an alias; sensitive governance stays in People/DNA/Land.
- **`settlement/` versus `settlements-infrastructure/`:** Settlement remains an alias; governing behavior stays in Settlements/Infrastructure.
- **Shared versus domain watchers:** use shared specs only for genuinely cross-domain behavior; domain roles, rights, sensitivity, or materiality favor domain sublanes.
- **Plants-drift duplication:** shared watcher and Flora-specific paths remain conflicted; this README does not choose one silently.
- **Historical `pipeline_specs/domains/...` references:** the current root does not establish that parent as canonical; treat references as drift signals.
- **Child README freshness:** current tree evidence outranks stale lane summaries; update child docs when their bounded responsibility changes.
- **State vocabulary overlap:** spec maturity, spec validation, RunReceipt, runtime envelope, lifecycle, and release vocabularies remain distinct until accepted mappings exist.

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

Until then, label the file `inventory_placeholder`, `stage_scaffold`, `proposed_inactive`, `implemented_fixture_first`, or `candidate`—never active by implication.

[Back to top](#top)

---

## Open verification register

| Item | Status | Evidence needed |
|---|---:|---|
| Child README freshness | `NEEDS VERIFICATION` | README-to-tree comparison and owner confirmation. |
| Accepted root-wide semantic contract and schema | `UNKNOWN` | Contract, schema, fixtures, validator, tests, and decision record. |
| Root-wide canonicalization and digest | `PARTIAL` | One accepted profile, vectors, collision/error handling, and CI. |
| Parser, discovery, active registry | `UNKNOWN` | Code, explicit paths, compatibility exclusions, duplicate/alias tests. |
| Complete consumer compatibility matrix | `UNKNOWN` | Named consumers, versions, agreement tests, failure mapping. |
| Active-spec inventory | `NOT ESTABLISHED` | Governed registry and activation decisions. |
| Meaning of legacy `version: 1` | `UNKNOWN` | Accepted version semantics and migration rules. |
| Air/People/Settlement aliases | `NEEDS VERIFICATION` | Inbound references, ADR/migration disposition, rollback. |
| Shared/domain watcher placement | `CONFLICTED` | Source/domain ownership decision and plants-drift migration plan. |
| Historical `pipeline_specs/domains/...` refs | `CONFLICTED` | Reference inventory and canonical target decision. |
| Source activation vocabulary/topology | `NEEDS VERIFICATION` | Source descriptor, activation decision, registry, policy, tests. |
| Rights/sensitivity enforcement | `NEEDS VERIFICATION` | Executable policy, negative fixtures, decision records. |
| Root-wide fixtures/tests/CI | `PARTIAL` | Shared test lane and changed-spec orchestration across all profiles. |
| RunReceipt binding and persistence | `UNKNOWN` | Spec-to-run join, emitted receipts, validation, retention, redaction. |
| Catalog/promotion dependency | `UNKNOWN` | Closure resolver, promotion checks, release manifests, negative tests. |
| Correction propagation | `UNKNOWN` | Dependency graph, invalidation records, cache/public derivative tests. |
| Deactivation and rollback drills | `UNKNOWN` | Runbook, fixtures, executed drill, receipt, verified recovery target. |
| Named owners and separation of duties | `NEEDS VERIFICATION` | CODEOWNERS plus accepted steward roles and enforcement. |
| Hosted workflow outcomes for this PR | `PENDING` | Exact-head Actions results after draft PR creation. |
| Production execution and public effects | `UNKNOWN` | Deployment, logs, metrics, dashboards, release state, incidents. |

[Back to top](#top)

---

## Evidence ledger

| Evidence | Observation | Status |
|---|---|---:|
| Current README and tree at the pinned base | Same-path v0.4 README plus complete recursive `pipeline_specs/` tree. | `CONFIRMED` |
| [Directory Rules v1.3.1](../docs/architecture/directory-rules.md#15-required-readme-contract) | Current README order and responsibility-root placement basis. | `CONFIRMED current artifact` |
| [Directory Rules v2 draft](../docs/doctrine/directory-rules.md) | Complete proposed successor; no supersession effect until adoption. | `CONFIRMED file / PROPOSED authority` |
| [`pipelines/README.md`](../pipelines/README.md) | Executable root remains separate from declarative configuration. | `CONFIRMED` |
| [`pipelines/specs/README.md`](../pipelines/specs/README.md) | Compatibility guardrail; active declarative discovery is prohibited there. | `CONFIRMED` |
| Empty-stage samples | Multiple lanes retain `stages: []` shells. | `CONFIRMED` |
| Short proposed candidates | Source or domain idea files remain non-active. | `CONFIRMED` |
| Soil support-type profile and validator | Deterministic hash/schema/profile/fixture validation with public authority denied. | `CONFIRMED code and profile` |
| Soil yearly-diff profile | Fixture-only, no-network, work-targeted diff profile with contract/schema/validator/tests/workflow. | `CONFIRMED` |
| Soil watcher profile | Inactive fixture-only watcher with source/support/QA/materiality/receipt declarations and fail-closed zones. | `CONFIRMED` |
| Hydrology WBD HUC12 candidate spec | Fixture-first implementation binding with dedicated tests/workflow and explicit non-effects. | `CONFIRMED` |
| Flora source-readiness profile | Inactive materiality profile with contract/schema/validator/workflow. | `CONFIRMED` |
| Habitat land-cover profile | Inactive profile with contract/schema; broader executable closure not established by bounded search. | `CONFIRMED bounded` |
| [`test_pipeline_connector_non_publisher.py`](../tests/policy/test_pipeline_connector_non_publisher.py) | Static no-direct-publish guard for connector/pipeline code. | `CONFIRMED code` |
| [Generated receipt lane](../data/receipts/generated/README.md) | Pull-request template requires a receipt for AI-authored diff files; receipt is process memory only. | `CONFIRMED` |
| Open PR search | No open PR touching `pipeline_specs/README.md` at task discovery. | `CONFIRMED at search time` |

### Evidence limits

The repository tree proves file presence at the pinned commit, not runtime use, source activation, policy enforcement, deployment, release, or publication. Search is bounded and can miss dynamic consumers or branch-local work. Child READMEs can be stale. Hosted checks are separate from local Markdown validation and may remain pending on a draft PR.

[Back to top](#top)

---

## v0.4 to v0.5 no-loss ledger

| v0.4 material | v0.5 disposition |
|---|---|
| Declarative versus executable separation | Preserved under Purpose and Authority level. |
| Canonical versus compatibility paths | Preserved and updated with current Directory Rules posture. |
| Root README section order | Preserved exactly for the first twelve H2 sections. |
| Placeholder and scaffold taxonomy | Preserved and expanded into a five-level maturity taxonomy. |
| Seventeen direct lane registry | Preserved and refreshed against the current tree. |
| Five nested sublane READMEs | Preserved in the current bounded inventory. |
| Air, People, Settlement, watcher, historical-path, and state conflicts | Preserved under Compatibility and placement conflicts. |
| Minimum active spec contract | Preserved. |
| Lifecycle, source, and release gates | Preserved. |
| Finite-outcome vocabulary separation | Preserved and expanded with current inactive/fixture-first states. |
| Validation and CI limitations | Preserved, narrowed where selected profile validation now exists. |
| Review and separation of duties | Preserved. |
| Correction, deactivation, rollback | Preserved. |
| Definition of done | Preserved. |
| Open verification register and evidence ledger | Preserved and refreshed. |
| Prior history | Preserved below. |

No stable identity, canonical path, lane link, conflict, uncertainty, governance boundary, or rollback posture was intentionally removed.

### v0.5 — 2026-08-08

- repinned the evidence snapshot to current main and the current `pipeline_specs/` tree;
- replaced the stale root-wide “no dedicated spec tests” implication with a mixed-maturity model;
- documented selected validated inactive and fixture-first slices without upgrading them to live activation;
- preserved the Directory Rules v1.3.1 README order and recorded v2.0.0-draft.1 as proposed, not adopted;
- refreshed lane maturity, child-document freshness warnings, validation examples, open questions, and rollback;
- changed this README and its required generated provenance receipt only.

### v0.4 — 2026-07-23

- reordered the first twelve H2 sections to match the then-current Directory Rules contract;
- reconciled the declarative root with executable and compatibility boundaries;
- added static non-publisher and RunReceipt evidence;
- separated specification maturity, validation, run receipt, runtime response, lifecycle, and release vocabularies;
- preserved inventory, conflict, definition-of-done, open-verification, and evidence content;
- changed documentation and generated provenance only.

### v0.3 — 2026-07-18

- replaced a planning tree with a repository-grounded maturity and routing boundary;
- recorded seventeen direct README lanes and five nested lanes;
- classified placeholder and compatibility shapes;
- surfaced alias, watcher, historical path, and inventory-freshness conflicts;
- strengthened source, lifecycle, parser/consumer, sensitive-domain, validation, correction, and rollback requirements;
- added lane registry, definition of done, open verification register, and evidence ledger.

### v0.2 — 2026-06-13

- expanded the root stub into a governed declarative configuration contract;
- defined declarative/executable separation, lifecycle gates, anti-collapse rules, a recommended tree, minimal profile example, and open questions.

<p align="right"><a href="#top">Back to top</a></p>
