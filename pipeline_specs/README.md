<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipeline-specs-readme
title: pipeline_specs/ — Governed Declarative Pipeline Specification Root
type: readme; directory-readme; declarative-pipeline-spec-root; compatibility-and-activation-boundary
version: v0.3
status: draft; repository-grounded; placeholder-heavy; mixed-lane-maturity; no-active-root-spec-system-established
owners:
  - OWNER_TBD — Pipeline-spec steward
  - OWNER_TBD — Pipeline owner
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
updated: 2026-07-18
supersedes: v0.2
policy_label: public-doc; pipeline-specs; declarative-only; no-secrets; no-live-activation; no-direct-fetch; no-direct-admission; no-direct-lifecycle-write; no-direct-release; source-role-aware; rights-aware; sensitivity-aware; evidence-bound; policy-gated; review-gated; correction-aware; rollback-aware
current_path: pipeline_specs/README.md
truth_posture: CONFIRMED target README, declarative pipeline_specs responsibility root, executable pipelines companion root, pipelines/specs compatibility guardrail, bounded seventeen direct child README lanes, representative empty-stage YAML scaffolds, representative short PROPOSED documentation-inventory placeholders, README-only compatibility aliases, checked absence of root AGENTS.md and pipeline_specs/AGENTS.md, checked absence of tests/pipeline_specs/README.md and fixtures/pipeline_specs/README.md, tests/pipelines repository-grounded boundary, CODEOWNERS routing, and no open PR targeting this README / PROPOSED accepted pipeline-spec schema, deterministic canonicalization and hashing, parser and consumer registry, activation state model, source binding, lifecycle grammar, finite outcomes, reason-code vocabulary, no-network fixtures, spec-to-consumer tests, receipt bindings, correction propagation, and rollback / CONFLICTED air versus atmosphere, people versus people-dna-land, settlement versus settlements-infrastructure, shared versus domain watcher placement, historical pipeline_specs/domains references, child README inventory freshness, and pipeline_specs versus pipelines/specs compatibility semantics / UNKNOWN exhaustive recursive inventory, active specifications, parser discovery, consumers, scheduler, source activation, runtime execution, emitted receipts, substantive spec CI, promotion dependency, branch protection, production use, and public effects / NEEDS VERIFICATION named owners, accepted Directory Rules copy, schema and ID vocabularies, alias and migration decisions, source-registry topology, rights and sensitivity policy, fixtures and tests, correction behavior, and rollback execution
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: 527ac01444c23046f0406dbb9e4cf5b2a74cd4cc
  target_prior_blob: 3a6599898606126604298a281de53e39fdba98ce
  bounded_direct_child_readmes: 17
  bounded_nested_readmes: 5
  checked_absent_paths:
    - AGENTS.md
    - pipeline_specs/AGENTS.md
    - tests/pipeline_specs/README.md
    - fixtures/pipeline_specs/README.md
  inventory_method: GitHub connector exact reads and bounded code-index queries; counts and absence claims are not full-history or all-branch assertions
related:
  - ../CONTRIBUTING.md
  - ../SECURITY.md
  - ../docs/architecture/directory-rules.md
  - ../docs/doctrine/directory-rules.md
  - ../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - ../docs/adr/ADR-0017-source-descriptor-admission-process.md
  - ../docs/registers/DRIFT_REGISTER.md
  - ../pipelines/README.md
  - ../pipelines/specs/README.md
  - ../tests/pipelines/README.md
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
  - ../data/receipts/generated/README.md
  - ../schemas/contracts/v1/receipts/generated_receipt.schema.json
  - ../.github/workflows/README.md
  - ../.github/CODEOWNERS
  - ../.github/PULL_REQUEST_TEMPLATE.md
notes:
  - "v0.3 replaces the planning-oriented root tree with a commit-pinned maturity and routing boundary."
  - "Representative YAML payloads are either empty-stage scaffolds or short PROPOSED inventory placeholders."
  - "A file, parse result, merge, schedule string, or workflow conclusion activates nothing without accepted schema, parser, consumer, source decision, fixtures, tests, and review state."
  - "This documentation-only revision changes no pipeline-spec YAML, executable behavior, source activation, policy, schema, test, workflow, lifecycle record, release object, runtime, or public artifact."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `pipeline_specs/` — Governed Declarative Pipeline Specification Root

> Declarative boundary for stating **what** a KFM pipeline may attempt, against which admitted sources, through which lifecycle and governance gates, with which deterministic outcomes, receipts, correction obligations, and rollback targets—without becoming executable code, source authority, lifecycle data, evidence, policy, release approval, or a public serving surface.

![status](https://img.shields.io/badge/status-repository--grounded%20draft-yellow)
![lanes](https://img.shields.io/badge/direct__README__lanes-17-informational)
![maturity](https://img.shields.io/badge/payload__maturity-placeholder--heavy-orange)
![activation](https://img.shields.io/badge/active__spec__system-not__established-critical)
![publication](https://img.shields.io/badge/publication-DENIED-red)

**Path:** `pipeline_specs/README.md`
**Version:** `v0.3`
**Owning root:** `pipeline_specs/` — declarative configuration, the **what**
**Executable companion:** [`pipelines/`](../pipelines/README.md) — implementation, the **how**
**Compatibility guardrail:** [`pipelines/specs/`](../pipelines/specs/README.md) — not an alternate authoritative spec root
**Evidence snapshot:** `main@527ac01444c23046f0406dbb9e4cf5b2a74cd4cc`

> [!IMPORTANT]
> Bounded inspection found many files but did not establish an accepted root schema, active parser, consumer registry, scheduler, source-activation binding, dedicated spec-test suite, or substantive root CI gate. File presence is evidence of repository state—not activation, implementation, or release proof.

> [!CAUTION]
> Two placeholder shapes recur: empty-stage scaffolds with `stages: []`, and short `status: PROPOSED` files created from documentation inventories. Neither is an active specification.

> [!WARNING]
> Never place credentials, private endpoints, restricted payloads, exact sensitive locations, living-person or DNA data, owner-resolved private-land joins, infrastructure vulnerability detail, or reconstructive cultural/ecological information in specs, examples, logs, receipts, issues, or pull requests.

## Quick navigation

[Purpose](#purpose) · [Authority](#authority-boundary) · [Current state](#current-state) · [Inventory](#bounded-root-inventory) · [Payloads](#payload-taxonomy) · [Lanes](#direct-lane-registry) · [Conflicts](#compatibility-and-placement-conflicts) · [Contract](#minimum-active-spec-contract) · [Lifecycle](#lifecycle-source-and-release-gates) · [Outcomes](#finite-outcomes) · [Validation](#validation-and-ci) · [Review](#review-versioning-and-migration) · [Rollback](#correction-deactivation-and-rollback) · [Done](#definition-of-done) · [Open](#open-verification-register) · [Evidence](#evidence-ledger)

---

## Purpose

A mature pipeline specification may declare:

- stable identity, semantic version, state, owners, and content digest;
- the exact parser and executable consumer allowed to interpret it;
- admitted `SourceDescriptor` references and fixed source roles;
- cadence, freshness, valid-time, source-vintage, and stale-state behavior;
- allowed lifecycle inputs and candidate outputs;
- contract and schema references;
- domain anti-collapse and cross-lane boundaries;
- rights, sensitivity, evidence, policy, review, and release prerequisites;
- deterministic no-network fixtures, replay, idempotency, retry, cancellation, quarantine, and no-op behavior;
- expected reports, receipts, hashes, correction, supersession, deactivation, and rollback behavior;
- finite outcomes and stable reason codes.

A spec does not execute itself. Code belongs under [`pipelines/`](../pipelines/README.md), a verified package, or another responsibility-rooted implementation home.

This README does not activate any current YAML, define an accepted schema, create a parser or scheduler, admit a source, prove a claim, approve release, or publish a product.

[Back to top](#top)

---

## Authority boundary

```text
pipeline_specs/  = WHAT may run and under which gates
pipelines/       = HOW governed execution occurs
connectors/      = HOW an approved source is accessed or staged
data/registry/   = WHICH source is admitted, in which role, under which rights
contracts/       = WHAT objects mean
schemas/         = WHAT accepted objects look like
policy/          = WHETHER use or exposure is allowed
tests/fixtures/  = WHETHER bounded behavior is enforceable
data/            = WHERE lifecycle records, receipts, proofs, catalogs, and artifacts live
release/         = WHETHER public state changes
```

| Concern | Correct authority | Spec role |
|---|---|---|
| Executable behavior | `pipelines/` | References a verified consumer; never implements it. |
| Source access | `connectors/` | Declares source refs only after admission. |
| Source identity/activation | `data/registry/sources/` or accepted control home | Resolves stable IDs; never self-activates. |
| Meaning and shape | `contracts/`, `schemas/` | References accepted versions. |
| Admissibility | `policy/` | Requires decisions; never creates permission. |
| Tests and fixtures | `tests/`, `fixtures/` | Supplies deterministic proof cases. |
| Lifecycle data | `data/<phase>/` | Declares candidate transitions; stores nothing here. |
| Receipts/proofs | `data/receipts/`, `data/proofs/` | Requires emitted records; is neither record type. |
| Release/correction/rollback | `release/` | Declares readiness prerequisites only. |
| Public delivery | governed apps and released artifacts | Specs are never public truth sources. |

A spec may require a gate. Naming the gate does not satisfy it.

[Back to top](#top)

---

## Current state

### Confirmed

- `pipeline_specs/` is the declarative root and `pipelines/` is the executable companion.
- `pipelines/specs/` is documented as a compatibility guardrail.
- Bounded search surfaced seventeen direct child README lanes and five nested README sublanes.
- Representative YAMLs are empty-stage scaffolds or short documentation-inventory placeholders.
- `air/`, `people/`, and `settlement/` are compatibility-oriented rather than proven parallel authorities.
- Checked `tests/pipeline_specs/README.md` and `fixtures/pipeline_specs/README.md` do not exist.
- [`tests/pipelines/README.md`](../tests/pipelines/README.md) records no dedicated executable pipeline suite at its evidence snapshot.
- Bounded search did not surface a canonical `pipeline_spec` schema or active YAML source-descriptor binding.
- CODEOWNERS routes this root to `@bartytime4life`; routing is not approval.

### Not established

| Capability | Status |
|---|---:|
| Accepted pipeline-spec schema | `UNKNOWN` |
| Canonicalization and digest algorithm | `UNKNOWN` |
| Parser, discovery, and active-spec registry | `UNKNOWN` |
| Deterministic consumer binding | `UNKNOWN` |
| Source activation binding | `NOT ESTABLISHED` |
| Root fixtures and spec tests | `NOT ESTABLISHED` |
| Substantive root CI | `NOT ESTABLISHED` |
| Current active specifications | `NOT ESTABLISHED` |
| Runtime use, receipts, promotion dependency, production effects | `UNKNOWN` |

[Back to top](#top)

---

## Bounded root inventory

```text
pipeline_specs/
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

Bounded nested READMEs also surfaced under Fauna/Flora watchers, Habitat ecoregions/land-cover, and People/DNA/Land land-ownership.

This is not a recursive manifest. Before activation or migration, generate a pinned recursive tree and compare it with affected READMEs, registries, consumers, workflows, and release dependencies.

[Back to top](#top)

---

## Payload taxonomy

### Empty-stage scaffold

```yaml
name: agriculture-normalize
version: 1
stages: []
```

This proves only a path and minimal shell. It declares no operation graph, source, lifecycle transition, contract, schema, policy, evidence, receipt, consumer, schedule, or release behavior.

### Documentation-inventory placeholder

```yaml
status: PROPOSED
source_doc: docs/domains/example/MISSING_OR_PLANNED_FILES.md
path: pipeline_specs/example/example.yaml
notes:
  - Placeholder created from docs/domains markdown inventory.
```

This preserves planning lineage. It must not be discovered or executed as active merely because it parses.

### Compatibility or README-only lane

A README may preserve routing, safety, or migration guidance without containing active profiles. Compatibility paths must not duplicate IDs, schedules, consumers, source refs, or release semantics.

### Proposed state vocabulary

`inventory_placeholder` → `stage_scaffold` → `proposed` → `candidate` → `active_internal` or `active_public_candidate` → `deprecated` / `disabled` / `retired`.

These labels are guidance until an accepted schema and activation contract exist.

[Back to top](#top)

---

## Direct lane registry

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

Do not add a lane unless its responsibility, consumer, source, rights, sensitivity, fixtures, tests, receipts, owners, migration, and rollback posture are known.

[Back to top](#top)

---

## Compatibility and placement conflicts

- **`pipeline_specs/` versus `pipelines/specs/`:** authoritative declarations belong here; the latter is a guardrail.
- **`air/` versus `atmosphere/`:** current documentation prefers Atmosphere; prevent duplicate active authority.
- **`people/` versus `people-dna-land/`:** People is an alias; sensitive governance remains in People/DNA/Land.
- **`settlement/` versus `settlements-infrastructure/`:** Settlement is an alias; governing behavior remains in Settlements/Infrastructure.
- **Shared versus domain watchers:** use shared specs only for truly cross-domain behavior; domain roles, rights, sensitivity, or materiality favor domain sublanes.
- **Historical `pipeline_specs/domains/...` references:** checked root evidence did not establish a parent README there; treat references as drift signals.
- **Directory Rules copies:** this README follows the shared responsibility-root rule without resolving the doctrine file's own placement conflict.

Conflict handling: freeze activation, inventory IDs/paths/consumers/schedules, preserve history, record drift, decide authority through ADR or migration review, test compatibility and rollback, then retire aliases only after consumers move.

[Back to top](#top)

---

## Minimum active spec contract

An active spec requires at least:

| Area | Requirement |
|---|---|
| Identity | Stable ID, semantic version, state, owners, immutable digest. |
| Shape | Accepted schema and canonicalization rules. |
| Binding | Exact parser and compatible executable consumer. |
| Sources | Admitted SourceDescriptor refs, roles, activation, rights, versions. |
| Support | Spatial/temporal support, scale, uncertainty, domain knowledge character. |
| Lifecycle | Allowed inputs, candidate outputs, quarantine/no-op, prohibited transitions. |
| References | Resolvable contracts, schemas, evidence, policy, review, receipt, release, rollback refs. |
| Execution | Dry-run/network posture, resource limits, side effects, idempotency, retry, cancellation. |
| Outcomes | Finite outcomes and stable reason codes. |
| Migration | Supersession, correction, deactivation, withdrawal, rollback. |

Directory scanning alone is unsafe activation because the tree contains placeholders and aliases. Activation requires an explicit governed registry or decision record.

[Back to top](#top)

---

## Lifecycle, source, and release gates

```text
source decision -> RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A spec may declare prerequisites and candidate transitions. It cannot grant source authority, store data, create evidence closure, approve policy, or write `PUBLISHED`.

Required gates for non-trivial activation:

1. identity, version, digest;
2. parser and consumer binding;
3. source activation, role, rights, sensitivity;
4. contract/schema resolution;
5. lifecycle allow/deny validation;
6. domain anti-collapse checks;
7. deterministic fixtures and validation;
8. evidence and policy resolution;
9. receipt emission;
10. catalog/triplet closure where applicable;
11. independent review and release decision;
12. correction and rollback readiness.

Default CI is no-network. Live network use needs explicit activation, reviewed connector, least privilege, rate limits, timeouts, safe logs, bounded lifecycle writes, and a kill switch. It can never directly publish.

[Back to top](#top)

---

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Bounded operation completed; not release approval. |
| `NO_OP` | No authorized delta. |
| `ABSTAIN` | Evidence, role, time, or claim support is insufficient. |
| `DENY` | Rights, sensitivity, policy, security, or transition blocks action. |
| `HOLD` | Resolvable prerequisite or review is pending. |
| `QUARANTINE` | Isolated review is required. |
| `ERROR` | Parser, consumer, validator, storage, receipt, or other operation failed. |
| `CANCELLED` | Operator, policy, timeout, supersession, or kill switch stopped execution. |

Candidate reason-code families include schema/digest failure, unresolved consumer, inactive source, role mismatch, unresolved rights/sensitivity, denied lifecycle transition, unresolved evidence/policy, validation failure, missing receipt/catalog closure/review/release manifest/rollback target.

[Back to top](#top)

---

## Validation and CI

Current root limitations:

- no checked root spec-test or spec-fixture README;
- no accepted schema, canonicalization algorithm, parser, discovery registry, active-spec registry, or substantive root CI gate established;
- no verified current pass rate, coverage, mutation score, runtime, flake rate, receipt emission, or promotion dependency.

An active system needs deterministic cases for schema/canonicalization, duplicate IDs and aliases, parser/consumer agreement, source activation and roles, lifecycle transitions, sensitive-domain denials, no-direct-publish, no-network default, replay/idempotency/retry/cancellation, receipt hashes, correction, supersession, deactivation, and rollback.

A substantive workflow should use safe PR events, least-privilege permissions, repository-owned commands, changed-spec dependency closure, positive and negative fixtures, stable check names, bounded artifacts, and a disable/rollback path.

A green check proves only the declared check completed.

[Back to top](#top)

---

## Review, versioning, and migration

Material changes require the pipeline-spec owner, affected domain/source owner, contract/schema/validation reviewer, evidence/receipt reviewer, rights/sensitivity/security reviewer, and release reviewer where applicable. CODEOWNERS routing is not a `ReviewRecord` or release decision.

Rules:

- do not reuse versions for changed semantics;
- preserve immutable digests and supersession lineage;
- separate file, schema, and implementation versions;
- document consumer compatibility;
- never auto-activate an alias;
- keep merge, activation, execution, promotion, and publication separate;
- require migration and rollback plans for moves, renames, aliases, or authority changes;
- require an accepted ADR before changing the canonical root or authority model.

[Back to top](#top)

---

## Correction, deactivation, and rollback

Disable active specs through explicit records, not silent deletion. Preserve ID, version, digest, reason, effective time, affected sources/consumers/schedules/runs, lifecycle and release refs, correction obligations, rollback target, and reviewer state.

A corrected or superseded source, spec, contract, schema, policy, or implementation may invalidate queued/completed runs, lifecycle candidates, receipts, EvidenceBundles, catalogs/triplets, release candidates, and public derivatives. Dependency and invalidation machinery remains `UNKNOWN` until verified.

Documentation rollback for this README is ordinary Git rollback. No runtime, data, release, or public state is changed by this revision.

[Back to top](#top)

---

## Definition of done

An active specification must have:

- [ ] stable identity, version, state, owners, digest;
- [ ] accepted schema and canonicalization;
- [ ] accepted parser and deterministic discovery;
- [ ] verified consumer/version binding;
- [ ] admitted sources, roles, rights, sensitivity, scale, time, uncertainty;
- [ ] allowed lifecycle inputs and candidate outputs, with direct publication denied;
- [ ] resolvable contract/schema/evidence/policy/review/receipt/release/rollback refs;
- [ ] valid, invalid, denied, held, abstain, no-op, sensitive, and migration fixtures;
- [ ] spec-to-consumer agreement tests;
- [ ] deterministic no-network CI;
- [ ] replay, idempotency, retry, cancellation, quarantine, and partial-state tests;
- [ ] correction, deactivation, withdrawal, supersession, and rollback procedures;
- [ ] independent human review separate from generation, validation, merge, activation, and release.

Until then, label the file as placeholder, scaffold, proposed, or candidate—not active.

[Back to top](#top)

---

## Open verification register

| Item | Status |
|---|---:|
| Exhaustive recursive inventory | `NEEDS VERIFICATION` |
| Canonical schema, canonicalization, digest | `UNKNOWN` |
| Parser, discovery, consumer registry | `UNKNOWN` |
| Active-spec inventory | `NOT ESTABLISHED` |
| Meaning of `version: 1` in scaffolds | `UNKNOWN` |
| Air/People/Settlement alias decisions | `NEEDS VERIFICATION` |
| Shared/domain watcher placement | `CONFLICTED` |
| Historical `pipeline_specs/domains/...` references | `CONFLICTED` |
| Child README inventory freshness | `NEEDS VERIFICATION` |
| Source activation vocabulary/topology | `NEEDS VERIFICATION` |
| Root fixtures, tests, substantive CI | `NOT ESTABLISHED` |
| Rights/sensitivity policy enforcement | `NEEDS VERIFICATION` |
| Pipeline receipt bindings and promotion dependency | `UNKNOWN` |
| Correction propagation and rollback drills | `UNKNOWN` |
| Named owners and independent reviewers | `NEEDS VERIFICATION` |
| Production execution and public effects | `UNKNOWN` |

[Back to top](#top)

---

## Evidence ledger

| Evidence | Observation | Status |
|---|---|---:|
| This README at the pinned base | Existing v0.2 contract; target blob recorded above. | `CONFIRMED` |
| [`pipelines/README.md`](../pipelines/README.md) | Executable behavior belongs under `pipelines/`. | `CONFIRMED` |
| [`pipelines/specs/README.md`](../pipelines/specs/README.md) | Compatibility guardrail, not alternate authority. | `CONFIRMED` |
| Bounded README search | Seventeen direct and five nested README lanes. | `CONFIRMED bounded result` |
| Agriculture/Soil stage YAML samples | Empty-stage scaffold shape. | `CONFIRMED` |
| Archaeology/Geology/Hazards/Hydrology/Roads samples | Short `PROPOSED` inventory-placeholder shape. | `CONFIRMED` |
| [`air/`](air/README.md), [`people/`](people/README.md), [`settlement/`](settlement/README.md) | Compatibility boundaries. | `CONFIRMED` |
| [`watchers/README.md`](watchers/README.md) | Shared placeholder-only, placement-conflicted watcher lane. | `CONFIRMED` |
| [`tests/pipelines/README.md`](../tests/pipelines/README.md) | Shared pipeline-test lane README-only; dedicated suite not established. | `CONFIRMED` |
| Checked root fixture/test paths | Both absent. | `CONFIRMED checked-path absence` |
| Search for pipeline-spec schema/source bindings | No accepted schema or active YAML binding surfaced. | `CONFIRMED bounded no-result` |
| Directory Rules and [`ADR-0017`](../docs/adr/ADR-0017-source-descriptor-admission-process.md) | Responsibility placement and proposed source-admission process. | `CONFIRMED files / decisions not accepted here` |
| [`.github/CODEOWNERS`](../.github/CODEOWNERS) | Root review routing; enforcement and role separation unverified. | `CONFIRMED routing` |
| [`data/receipts/generated/README.md`](../data/receipts/generated/README.md) | AI receipts are process provenance, not proof or approval. | `CONFIRMED` |

### Evidence limits

Search is bounded and may lag branch-local content. Checked absence is not a full-history claim. Child READMEs can be stale. No clone, recursive tree, repository-native tests, branch settings, deployment, source system, dashboard, or production runtime was inspected.

[Back to top](#top)

---

## Change history

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

[Back to top](#top)
