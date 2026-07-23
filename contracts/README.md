<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-readme
title: contracts/ — Canonical Semantic-Meaning Root and Contract Governance Boundary
type: README
version: v0.3
status: draft; repository-grounded; canonical-semantic-contract-root; mixed-maturity; configured-cross-root-validation; non-schema; non-policy; non-release
owner: NEEDS VERIFICATION — CODEOWNERS routes /contracts/ to @bartytime4life; no accepted contract steward, required-review enforcement, or independent approval control was verified
created: NEEDS VERIFICATION — a short root stub predated the v0.2 expansion
updated: 2026-07-23
supersedes: v0.2 documentation at the same path; no semantic contract, schema, policy, fixture, validator, test, runtime, release object, or public behavior is superseded
policy_label: repository-facing; contracts; semantic-meaning; cite-or-abstain; no-parallel-authority; evidence-aware; policy-aware; correction-aware; rollback-aware; non-publisher
current_path: contracts/README.md
owning_root: contracts/
responsibility: own human-readable semantic meaning, field intent, invariants, exclusions, compatibility semantics, and object-family navigation without becoming machine shape, admissibility, evidence, lifecycle, release, runtime, or publication authority
truth_posture: cite-or-abstain; contract Markdown defines meaning and promises but never makes a claim true, validates an instance, admits a source, authorizes exposure, approves release, or proves production behavior
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: e2466421ced8e41430737d4e7d51f19e3ab61d9f
  prior_blob: 6e05ba40fcc255e392210e56ef9519203aec6006
  directory_rules_blob: 18653c00ba193a4afaa3e07a0924452807fb98ef
  object_map_blob: 002366e3aac3086287eca93e1c69057da7cecebe
  domains_readme_blob: 9853efc4b2b8821ccd2b783f87e973c455c2558c
  contract_schema_policy_split_blob: 40ce4222a98fa7a033d3d383cd9cb557387f9a6e
  adr_0001_blob: 3c520ea8f2f8bcb3d478329a87d98b135ea335fd
  adr_0002_blob: 2da10fcf5836a44d46186c233b6b9664c9ccfda5
  schemas_contracts_v1_readme_blob: bbe931c9f7a5f0132522c0bda4fa5455c050a973
  tests_contracts_readme_blob: f58e0222de1c8228daff6d4dc6243ed713927607
  contracts_validate_workflow_blob: 7a14c94784c596b4f74996439217d8128d641bd1
  makefile_blob: 51537af34ee065c2de571134688415042b83b22a
  common_contract_test_blob: b04342cc034d7f1cc554e155fdd02d6e972976e6
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  object_family_register_blob: 930a9da30d5481f8d7ed5b7789d7846a30d3f4e1
related:
  - ./OBJECT_MAP.md
  - ./domains/README.md
  - ./source/README.md
  - ./evidence/README.md
  - ./runtime/README.md
  - ./policy/README.md
  - ./release/README.md
  - ./ui/README.md
  - ./v1/README.md
  - ../schemas/README.md
  - ../schemas/contracts/v1/README.md
  - ../policy/README.md
  - ../fixtures/README.md
  - ../tests/README.md
  - ../tests/contracts/README.md
  - ../tools/validators/README.md
  - ../data/README.md
  - ../release/README.md
  - ../docs/architecture/directory-rules.md
  - ../docs/architecture/contract-schema-policy-split.md
  - ../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - ../docs/adr/ADR-0002-contracts-vs-schemas-split.md
  - ../.github/workflows/contracts-validate.yml
notes:
  - "This is a same-path Markdown modernization. It creates no root, sibling README, schema, policy rule, fixture, validator, test, receipt, proof, release record, runtime behavior, or publication state."
  - "Directory Rules §15 controls the required canonical-root README section order."
  - "The repository configures schemas/contracts/v1/ as a machine-shape validation surface, while ADR-0001 and ADR-0002 remain proposed rather than accepted."
  - "The direct tests/contracts lane is documentation-only in the bounded evidence snapshot; selected contract-backed schema fixtures are exercised from tests/schemas/test_common_contracts.py."
  - "contracts/OBJECT_MAP.md is an evidence-limited maintainer crosswalk, not a generated or complete object-family registry."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `contracts/` — Canonical Semantic-Meaning Root and Contract Governance Boundary

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#status)
[![Authority: canonical semantic meaning](https://img.shields.io/badge/authority-canonical%20semantic%20meaning-1f6feb?style=flat-square)](#authority-level)
[![Schema-home ADR: proposed](https://img.shields.io/badge/schema--home%20ADR-proposed-d4a72c?style=flat-square)](#adrs)
[![Validation: configured but partial](https://img.shields.io/badge/validation-configured%20but%20partial-8250df?style=flat-square)](#validation)
[![Publisher: no](https://img.shields.io/badge/publisher-no-6e7781?style=flat-square)](#authority-level)

> **One-line purpose.** `contracts/` owns KFM's human-readable object meaning: vocabulary, field intent, invariants, exclusions, compatibility semantics, and the promises that schemas, policy, validators, applications, and release processes must preserve.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Does not belong](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related roots](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed) · [Authoring contract](#contract-authoring-contract) · [Maturity](#maturity-and-claim-discipline) · [Lanes](#verified-lane-inventory) · [Drift](#compatibility-versioning-and-drift) · [Open verification](#open-verification-register)

> [!IMPORTANT]
> A semantic contract can state what an object **means**, which invariants bind it, and what support it requires. It does **not** make an instance true, valid, admissible, reviewed, released, public-safe, or implemented.

> [!CAUTION]
> The repository currently exercises `schemas/contracts/v1/` through validators and tests, but [`ADR-0001`](../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) and [`ADR-0002`](../docs/adr/ADR-0002-contracts-vs-schemas-split.md) remain **proposed**. Configured behavior is repository evidence; it is not accepted decision authority.

---

## Purpose

`contracts/` is KFM's canonical responsibility root for **semantic meaning**.

A contract answers questions such as:

- What is this object, message, envelope, receipt, decision, source descriptor, UI projection, runtime response, release record, or domain concept?
- Which identity, field intent, invariants, relationships, and compatibility promises define it?
- What may the object assert, and what must it never be used to assert?
- Which source roles, evidence support, spatial and temporal scope, rights, sensitivity, policy, review, release, correction, and rollback state must remain visible?
- Which companion schema, fixture, validator, policy, data, proof, runtime, API, UI, and release surfaces are relevant?
- Which consumer may interpret the object after the required gates close?

A contract is a **published language for maintainers and implementations**, not a source of evidence. When a claim depends on evidence, `EvidenceRef` must resolve to an admissible `EvidenceBundle` or the consuming surface must narrow, abstain, deny, hold, or report an error according to its governing contract.

### Primary audiences

- contract and schema authors;
- domain and source stewards;
- policy, evidence, review, and release reviewers;
- validator and test authors;
- API, runtime, MapLibre, UI, export, and governed-AI implementers;
- maintainers evaluating compatibility, correction, and rollback impact.

[Back to top](#top)

---

## Authority level

| Field | Authority posture |
|---|---|
| **Directory class** | **Canonical responsibility root** |
| **Primary responsibility** | Human-readable semantic meaning and object-family vocabulary |
| **May own** | Markdown contracts, contract-family README files, semantic crosswalks, compatibility pointers, migration notes, field intent, invariants, exclusions, and versioning semantics |
| **Must not own** | JSON Schema, executable policy, fixtures, test code, validator implementations, source registry records, lifecycle data, EvidenceBundles, receipts, proofs, release decisions, runtime execution, public UI code, or published artifacts |
| **Truth posture** | Cite or abstain; contract prose is subordinate to admissible evidence for factual claims |
| **Public-path posture** | Contract Markdown may be public documentation, but ordinary public clients do not use it as a data, policy, evidence, or release interface |
| **Promotion posture** | A contract may define promotion-object meaning; it cannot promote, release, correct, withdraw, or roll back an artifact |

### Responsibility split

| Question | Owning surface | Relationship to `contracts/` |
|---|---|---|
| What does the object mean? | [`contracts/`](./) | **Owns** the semantic answer |
| What machine shape is accepted? | [`schemas/contracts/v1/`](../schemas/contracts/v1/README.md) or an accepted successor | References the contract; does not replace meaning |
| May this object or operation proceed? | [`policy/`](../policy/README.md) | Applies admissibility, rights, sensitivity, access, and release rules |
| Which examples define the boundary? | [`fixtures/`](../fixtures/README.md) | Exercises the contract and schema without becoming either authority |
| Can the rule be enforced? | [`tests/`](../tests/README.md) and [`tools/validators/`](../tools/validators/README.md) | Provides bounded executable proof |
| What source is authoritative? | Accepted source registries and authority registers | Resolves source identity and role outside contract prose |
| What evidence supports the claim? | Accepted evidence and proof roots | Evidence outranks the contract for factual support |
| What lifecycle state exists? | [`data/`](../data/README.md) | Owns governed instances and phase transitions |
| What is released, corrected, or rolled back? | [`release/`](../release/README.md) | Owns release-governance records and decisions |
| What behavior runs? | Accepted `apps/`, `packages/`, `runtime/`, `pipelines/`, and API roots | Implements the declared meaning through governed interfaces |

> [!WARNING]
> `contracts/` must not become a second schema registry, policy registry, source registry, evidence store, fixture registry, validator root, runtime, release system, or generated implementation inventory.

[Back to top](#top)

---

## Status

Snapshot: `main@e2466421ced8e41430737d4e7d51f19e3ab61d9f`, inspected on 2026-07-23.

| Surface | Current evidence | Safe conclusion |
|---|---|---|
| `contracts/README.md` | **CONFIRMED** at prior blob `6e05ba40...`; this revision is v0.3 | Canonical-root documentation exists and is modernized in place |
| `contracts/OBJECT_MAP.md` | **CONFIRMED** evidence-limited crosswalk | Useful maintainer orientation; not a complete generated registry or implementation proof |
| Child contract-family READMEs | **CONFIRMED** for domains, source, evidence, runtime, policy, release, UI, and the versioned compatibility guard | Multiple semantic lanes are documented; maturity varies by object and companion surface |
| `schemas/contracts/v1/` | **CONFIRMED** nonempty configured validation surface with mixed-maturity and compatibility lanes | Machine-shape work exists; completeness and canonical acceptance remain unresolved |
| ADR-0001 | **CONFIRMED `proposed`** | Schema-home proposal is not accepted decision authority |
| ADR-0002 | **CONFIRMED draft / effective `proposed`** | The contract/schema/policy/test split is documented and partially exercised, but not accepted by ADR status |
| `contracts-validate` workflow | **CONFIRMED command-bearing**; installs `.[test]` and runs `make test` | CI definition exercises the selected test aggregate; a current pass is not inferred from the file alone |
| `make test` | **CONFIRMED narrow aggregate** | Runs `pytest tests/schemas tests/contracts -q`; it is not a complete semantic-contract suite |
| Contract-backed schema fixture test | **CONFIRMED** in `tests/schemas/test_common_contracts.py` | Exercises selected schema families and valid/invalid fixtures; does not prove prose semantics |
| Direct `tests/contracts/` executables | **Not established** in the bounded test-lane evidence | A dedicated semantic-contract runner and direct modules remain **NEEDS VERIFICATION** |
| Aggregate validators | **CONFIRMED bounded** | Six configured fixture-backed validators cover SourceDescriptor, EvidenceRef, EvidenceBundle, RuntimeResponseEnvelope, DecisionEnvelope, and RunReceipt |
| Machine object-family register | **CONFIRMED empty** at `control_plane/object_family_register.yaml` | No populated authoritative machine crosswalk exists yet |
| Contract inventory and consumer coverage | **UNKNOWN / incomplete** | No complete contract-to-schema-to-policy-to-consumer registry or coverage artifact was verified |
| Required reviews and branch protection | **NEEDS VERIFICATION** | CODEOWNERS routing does not prove required review or separation of duties |
| Release, publication, and production parity | **DENIED as inference** | Contract presence, schema validity, workflow success, or a merged PR does not establish KFM release or publication |

### Material corrections from v0.2

- The README now follows the mandatory Directory Rules §15 root-section sequence.
- `schemas/contracts/v1/` is described as the **configured** v1 machine-shape surface while ADR-0001 remains proposed.
- `make test`, `make validate`, the contract workflow, the aggregate validator set, and the common contract-schema fixture test are distinguished by their actual scope.
- The direct `tests/contracts/` semantic suite is not presented as implemented.
- `OBJECT_MAP.md` remains an evidence-limited crosswalk, and the empty machine-readable object-family register is visible.
- CODEOWNERS routing is separated from stewardship, approval, branch protection, and release authority.
- Immediate rollback now targets the prior v0.2 blob rather than the older pre-v0.2 stub.

[Back to top](#top)

---

## What belongs here

Place material under `contracts/` when its primary responsibility is to define **human-readable semantic meaning**.

### Accepted material

- object-family contracts in Markdown;
- field intent and invariant definitions;
- identity, compatibility, versioning, supersession, correction, and rollback semantics;
- explicit exclusions and unsupported-use statements;
- source-role, evidence, spatial, temporal, rights, sensitivity, policy, review, release, and public-use requirements at the semantic level;
- contract-family and domain-lane README files;
- object maps and crosswalks that are clearly bounded as navigation rather than generated truth;
- compatibility pointers, migration notes, backlink audits, and ADR pointers that do not duplicate canonical contract content.

### Routing patterns

| Contract responsibility | Preferred existing pattern | Notes |
|---|---|---|
| Cross-family object meaning | `contracts/<family>/<object>.md` | Use when one semantic family owns the object |
| Domain-specific object meaning | `contracts/domains/<domain>/<object>.md` | Domain appears as a lane inside the responsibility root |
| Root navigation | `contracts/README.md`, `contracts/OBJECT_MAP.md` | Root boundary and evidence-limited crosswalk |
| Compatibility or migration guard | Documented compatibility lane such as `contracts/v1/` | Pointer only unless an accepted ADR and migration changes authority |

### Verified semantic lanes

- [`domains/`](./domains/README.md) — domain-specific object meaning;
- [`source/`](./source/README.md) — source-governance object meaning;
- [`evidence/`](./evidence/README.md) — evidence pointer, closure, and citation semantics;
- [`runtime/`](./runtime/README.md) — runtime envelope and governed-interface semantics;
- [`policy/`](./policy/README.md) — policy-object meaning, not executable policy;
- [`release/`](./release/README.md) — release-governance object meaning, not release state;
- [`ui/`](./ui/README.md) — UI-facing payload meaning, not component implementation;
- [`v1/`](./v1/README.md) — compatibility guard, not a second semantic authority.

This is a targeted verified list, not a complete recursive contract inventory.

[Back to top](#top)

---

## What does NOT belong here

| Excluded material | Correct responsibility root |
|---|---|
| JSON Schema, JSON-LD contexts, or other machine-shape definitions | [`schemas/`](../schemas/README.md) and its accepted schema homes |
| Rego, OPA bundles, access rules, sensitivity rules, or policy decisions | [`policy/`](../policy/README.md) |
| Valid, invalid, denied, abstaining, stale, correction, rollback, or golden examples | [`fixtures/`](../fixtures/README.md) or a verified test-local fixture lane |
| Test code, assertions, collection rules, or reusable validator implementation | [`tests/`](../tests/README.md), [`tools/validators/`](../tools/validators/README.md) |
| SourceDescriptor instances, source activation records, or source authority registry entries | accepted source registry and control-plane roots |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG/TRIPLET, or PUBLISHED instances | [`data/`](../data/README.md) lifecycle roots |
| Materialized EvidenceBundles, receipts, proof packs, or attestations | accepted proof, receipt, and evidence roots |
| Release manifests, PromotionDecisions, CorrectionNotices, WithdrawalNotices, or RollbackCards as governed instances | [`release/`](../release/README.md) and accepted lifecycle homes |
| Runtime/API response instances, logs, model output, or service state | accepted runtime, API, log, and receipt roots |
| React, MapLibre, UI, API, pipeline, connector, or package implementation | accepted `apps/`, `packages/`, `pipelines/`, `connectors/`, and runtime roots |
| PMTiles, COGs, GeoParquet, tiles, screenshots, dashboards, exports, or published artifacts | release-governed delivery and published-data roots |
| Generated prose or diagrams treated as evidence, policy, review, or release authority | Not permitted; resolve to the owning evidence or governance surface |

Do not place `.schema.json`, executable policy, production payloads, source exports, secrets, private data, sensitive exact geometry, or release-bearing records in this root.

[Back to top](#top)

---

## Inputs

Contracts are authored from evidence and decisions, not from file-name intuition.

### Acceptable inputs

- accepted KFM doctrine and unsuperseded ADRs;
- verified domain vocabulary and source-role distinctions;
- current repository implementation evidence where the contract describes existing behavior;
- paired schema, fixture, validator, test, policy, API, UI, runtime, evidence, and release surfaces, each with its own truth status;
- source, rights, sensitivity, temporal, spatial, and public-use requirements;
- reviewed compatibility, migration, correction, and rollback requirements;
- user requirements that do not override evidence, policy, review, or release controls.

### Minimum authoring input record

The following is an **illustrative checklist**, not a repository schema:

```text
ContractAuthoringInput
  object_family_or_lane
  owning_context
  semantic_definition
  field_intent_and_invariants
  explicit_exclusions
  identity_and_versioning_posture
  source_and_evidence_requirements
  spatial_and_temporal_scope
  rights_sensitivity_policy_and_review_impact
  schema_posture
  fixture_test_and_validator_posture
  consumer_and_public_use_boundary
  compatibility_correction_and_rollback_path
```

### Inputs that are insufficient by themselves

- a JSON Schema;
- a fixture or passing test;
- a map layer, screenshot, tile, graph edge, vector-search result, or dashboard;
- generated language or model confidence;
- a planning path not verified in the repository;
- a commit, pull request, merge, badge, or workflow name;
- repeated terminology without a bounded context and reviewed meaning.

[Back to top](#top)

---

## Outputs

This root emits or supports **semantic documentation**, not governed object instances.

### Direct outputs

- reviewed Markdown contracts;
- contract-family and domain-lane navigation;
- explicit field intent, invariants, exclusions, and compatibility semantics;
- semantic references to companion roots with bounded truth labels;
- contract change-impact and rollback notes;
- evidence-limited object maps or crosswalks that remain visibly non-authoritative.

### Downstream support

| Consumer | What the contract supplies | What remains outside the contract |
|---|---|---|
| Schema authors | Field intent, identity rules, invariants, and semantic constraints | Machine shape and schema acceptance |
| Policy authors | Named concepts, decision inputs, obligations, and prohibited uses | Executable allow/deny/restrict/hold/abstain logic |
| Fixture and test authors | Positive and negative semantic boundaries | Test authority and pass evidence |
| Validator authors | Checkable invariants and diagnostic expectations | Validator implementation and execution evidence |
| API/runtime authors | Message meaning, finite outcomes, correction and stale-state semantics | Route implementation and runtime behavior |
| Map/UI/AI authors | Trust-visible payload meaning and evidence/release obligations | Rendering, model execution, public admission, and citation truth |
| Release reviewers | Meaning of manifests, decisions, correction, withdrawal, and rollback objects | The actual release decision and governed records |

No file under `contracts/` is a release, publication, source admission, PolicyDecision, EvidenceBundle, receipt, proof, or runtime response merely because it describes one.

[Back to top](#top)

---

## Validation

Validation is layered. Machine-shape validation can support a contract; it cannot prove prose semantics by itself.

### Confirmed repository commands and workflows

| Surface | Command or behavior | What it proves | What it does not prove |
|---|---|---|---|
| Root test aggregate | `make test` | Runs `pytest tests/schemas tests/contracts -q` for the checked revision | Complete contract inventory, semantic equivalence, policy behavior, or release readiness |
| Root validation aggregate | `make validate` | Runs six configured fixture-backed validators, then the root test aggregate | Full repository validation or complete object-family coverage |
| Contract/schema workflow | `.github/workflows/contracts-validate.yml` → `make test` | Command-bearing CI intent for the selected lane | Current pass rate, branch-protection coupling, or complete semantic coverage |
| Common contract-schema fixture test | `python -m pytest tests/schemas/test_common_contracts.py -q` | Valid/invalid fixture behavior for discovered schemas in selected families | Contract Markdown meaning or every schema family |
| Aggregate validators | `python tools/validators/_common/run_all.py` | Bounded validation for six configured object families | Unconfigured families, policy execution, runtime behavior, or release state |

The selected schema-fixture test currently enumerates the families `evidence`, `runtime`, `common`, `policy`, `source`, `governance`, and `release` when matching schemas and fixture directories exist.

### Required semantic review checks

Until an accepted automated semantic-contract linter exists, reviewers must check:

- stable document identity and path;
- one clear semantic definition;
- field intent and invariants rather than type repetition;
- explicit exclusions and unsupported uses;
- bounded-context and ownership clarity;
- source role and evidence requirements where claims depend on support;
- spatial and temporal scope where material;
- rights, sensitivity, policy, review, release, correction, and rollback posture;
- companion schema posture: confirmed, linked, missing, scaffold, conflicted, or not applicable;
- fixture, validator, and test posture without invented paths or pass claims;
- compatibility, supersession, and migration impact;
- public-client and AI trust-membrane boundaries;
- relative links and anchors introduced by the change.

### Failure interpretation

| Failure | Required response |
|---|---|
| Meaning and schema disagree | Mark the relationship `CONFLICTED`; do not silently choose one |
| Schema or validator is missing | Keep the contract semantic claim; label enforcement `NEEDS VERIFICATION` |
| Rights, sensitivity, source role, evidence, or release support is unclear | Narrow, hold, abstain, deny, or require review according to the owning policy surface |
| Compatibility path duplicates canonical meaning | Stop expansion; record drift and require migration or ADR resolution |
| Test infrastructure fails | Report `ERROR`; do not convert infrastructure failure into semantic success |
| A contract change breaks object identity or public compatibility | Require versioning, migration, old-fixture parity, correction impact, and rollback planning |

> [!NOTE]
> A green workflow supports only its named revision, command, tests, fixtures, and assertions. It is not source authority, evidence closure, policy approval, review approval, release, publication, or production parity.

[Back to top](#top)

---

## Review burden

[`CODEOWNERS`](../.github/CODEOWNERS) routes `/contracts/` review requests to `@bartytime4life`. That route is **CONFIRMED**, but it is not a StewardshipAssignment, required-review rule, ReviewRecord, approval, PolicyDecision, release decision, or proof that separation of duties occurred.

### Review by change class

| Change class | Review burden |
|---|---|
| README navigation, clarification, or dead-link repair | Contracts/docs review; verify no authority or behavior claim changed |
| New or changed object meaning, identity, invariant, or field intent | Contracts review plus the owning domain or object-family reviewer |
| Schema-linked semantic change | Contract and schema review; verify ADR status, fixtures, validators, compatibility, and versioning impact |
| Policy-, rights-, sensitivity-, or access-significant meaning | Contract review plus applicable policy and sensitivity review |
| Public API, UI, map, export, or governed-AI meaning | Contract review plus affected runtime/API/UI/evidence review and finite negative-state coverage |
| Release, correction, withdrawal, or rollback semantics | Contract review plus release/evidence/correction review; no self-approval inference |
| Move, rename, duplicate-home cleanup, or `contracts/v1/` authority change | Directory Rules preflight, accepted ADR or migration authority where required, compatibility map, and rollback |

### Review limits

- Accepted steward assignments remain **NEEDS VERIFICATION**.
- Required CODEOWNERS review, branch protection, ruleset coupling, and independent author/approver separation remain **NEEDS VERIFICATION**.
- A contract author must not infer approval from a successful commit, workflow, or merge.
- Policy-significant or release-significant changes should separate authoring from approval when project maturity and governance require it.

[Back to top](#top)

---

## Related folders

| Surface | Relationship |
|---|---|
| [`OBJECT_MAP.md`](./OBJECT_MAP.md) | Evidence-limited contract-to-companion-root crosswalk; not complete inventory |
| [`domains/`](./domains/README.md) | Domain-specific semantic contracts and bounded-context guidance |
| [`source/`](./source/README.md) | Source-governance object meaning |
| [`evidence/`](./evidence/README.md) | EvidenceRef, EvidenceBundle, citation, and evidence-facing semantics |
| [`runtime/`](./runtime/README.md) | Runtime envelope and governed-interface semantics |
| [`policy/`](./policy/README.md) | Policy object meaning; executable rules remain under root `policy/` |
| [`release/`](./release/README.md) | Release, promotion, withdrawal, and rollback object meaning |
| [`ui/`](./ui/README.md) | UI-facing payload meaning and trust-surface boundaries |
| [`v1/`](./v1/README.md) | Versioned compatibility guard; not a second semantic root |
| [`schemas/`](../schemas/README.md) | Machine-checkable shape responsibility root |
| [`schemas/contracts/v1/`](../schemas/contracts/v1/README.md) | Configured mixed-maturity v1 schema index |
| [`policy/`](../policy/README.md) | Canonical admissibility responsibility root |
| [`fixtures/`](../fixtures/README.md) | Reusable deterministic examples |
| [`tests/`](../tests/README.md) | Authored enforceability proof |
| [`tests/contracts/`](../tests/contracts/README.md) | Intended semantic-contract test lane; direct executable suite not established in bounded evidence |
| [`tools/validators/`](../tools/validators/README.md) | Reusable validator implementation |
| [`data/`](../data/README.md) | Lifecycle records, source registries, receipts, proofs, catalogs, and published artifacts in their owning lanes |
| [`release/`](../release/README.md) | Release-governance records and decisions |
| [Contract/schema/policy/test split](../docs/architecture/contract-schema-policy-split.md) | Human-readable four-layer boundary explanation |
| [Directory Rules](../docs/architecture/directory-rules.md) | Placement authority and required root README contract |
| [`contracts-validate`](../.github/workflows/contracts-validate.yml) | Command-bearing CI workflow for the selected schema/contract test aggregate |
| [`object_family_register.yaml`](../control_plane/object_family_register.yaml) | Proposed machine-readable object-family map; currently empty |

[Back to top](#top)

---

## ADRs

No accepted contracts-root-specific ADR was verified for this documentation update.

### Current decision posture

- [`ADR-0001 — Schema Home`](../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) is **proposed**. The repository configures `schemas/contracts/v1/`, but the ADR is not accepted.
- [`ADR-0002 — Contracts vs Schemas Split`](../docs/adr/ADR-0002-contracts-vs-schemas-split.md) is **draft** with effective status **proposed**. The repository documents and partially exercises the split without converting configuration into accepted decision authority.
- [`contracts/v1/`](./v1/README.md) remains a compatibility guard. Making it canonical, mirroring schemas into it, or moving canonical semantic contracts there requires reviewed path authority and a reversible migration.
- The Directory Rules document-location conflict between `docs/architecture/` and `docs/doctrine/` remains open. New links here follow current contribution guidance and point to the live architecture-path artifact; this README does not settle the conflict.

An accepted ADR and migration plan are required before:

- moving machine schemas into `contracts/`;
- creating another canonical semantic-contract root;
- promoting a compatibility lane to canonical authority;
- changing the contract/schema division of labor;
- moving or renaming an object in a way that changes semantic identity;
- creating parallel contract, schema, policy, source, registry, evidence, receipt, proof, release, or publication authority.

[Back to top](#top)

---

## Last reviewed

**2026-07-23**

Evidence snapshot: `bartytime4life/Kansas-Frontier-Matrix` at `main@e2466421ced8e41430737d4e7d51f19e3ab61d9f`, prior target blob `6e05ba40fcc255e392210e56ef9519203aec6006`.

Review this README again when:

- six months pass without review;
- a top-level contract family is added, moved, renamed, consolidated, or retired;
- ADR-0001 or ADR-0002 changes status;
- `contracts/v1/` changes classification;
- an automated semantic-contract inventory or linter is established;
- the object-family register is populated;
- the root test or validation aggregate changes scope;
- a public API, UI, map, export, AI, release, correction, or rollback contract changes materially;
- Directory Rules or accepted placement ADRs change the responsibility split.

### Rollback and correction

Documentation rollback is a same-path revert of the commit that introduces this v0.3 README. The immediate byte-level rollback target is prior blob `6e05ba40fcc255e392210e56ef9519203aec6006`.

The v0.2 README recorded the older pre-expansion stub blob `a2c5150814c1cac5a360fb03b8ddbfb4d98bb2d7` as lineage. That older blob is not the immediate rollback target for this revision.

A semantic contract change that has already influenced schemas, fixtures, policy, runtime behavior, releases, public artifacts, or dependent documentation requires coordinated correction and rollback across those consumers. Reverting Markdown alone is not sufficient evidence that downstream state was corrected.

[Back to top](#top)

---

## Contract authoring contract

A non-trivial contract should make the following dimensions inspectable. Requirements apply according to the object's significance and maturity; unsupported dimensions must be labeled rather than invented.

| Dimension | Required content |
|---|---|
| Identity | Stable document/object identity, family, owning context, status, version or compatibility posture |
| Definition | One concise semantic definition using the owning bounded-context vocabulary |
| Field intent | What each material field means and what it does not mean |
| Invariants | Conditions that remain true across implementations and representations |
| Exclusions | Unsupported claims, prohibited uses, and adjacent authority boundaries |
| Source and evidence | Source-role and `EvidenceRef` / `EvidenceBundle` requirements for consequential claims |
| Space and time | Spatial reference, scale, geometry role, valid/observed/source/retrieval/release/correction time where material |
| Rights and sensitivity | Rights, access, sovereignty, cultural, living-person, genomic, rare-species, archaeology, infrastructure, or precision constraints |
| Policy and review | Required policy decisions, obligations, review states, and fail-closed outcomes |
| Shape posture | Paired schema path or explicit `schema-missing`, `schema-scaffold`, `schema-conflicted`, or not-applicable rationale |
| Enforceability | Fixture, validator, test, diagnostic, and negative-state expectations without invented implementation claims |
| Consumers | Which governed APIs, runtime envelopes, UI/map/export/AI surfaces may consume the object and under which release state |
| Lifecycle and release | Instance homes, promotion dependencies, publication limits, correction, withdrawal, and rollback semantics |
| Compatibility | Supersession, aliases, migrations, old-version behavior, and deprecation windows |
| Evidence ledger | Precise repository evidence for implementation claims and visible open verification items |

### Semantic contract rule

A contract should explain **why a field or state matters**, not simply restate JSON types. Schemas may constrain that a field is a string or enum; the contract must explain what the value promises, which distinctions must not collapse, and how downstream consumers interpret it safely.

### Finite negative states

Where the object participates in a governed operation, the contract should define applicable negative states explicitly. Common KFM outcomes include `ABSTAIN`, `DENY`, `HOLD`, `ERROR`, stale, withdrawn, superseded, correction-required, and rollback-required. Do not standardize an enum across surfaces unless an accepted contract or ADR authorizes it.

[Back to top](#top)

---

## Maturity and claim discipline

Maturity labels describe **bounded support for an object family or contract relationship**. They do not substitute for document lifecycle, policy approval, release state, or publication.

| Label | Meaning | Safe claim |
|---|---|---|
| `scaffold` | Placeholder or path marker; semantic content is insufficient | Path exists only |
| `draft` | Human-readable meaning and boundaries exist | Semantic draft exists; no enforcement or release claim |
| `schema-missing` | No paired machine shape was confirmed | Shape remains unresolved |
| `schema-scaffold` | Paired schema exists but is permissive, empty, or incomplete | Schema surface exists; maturity is limited |
| `schema-linked` | A paired schema path is confirmed | Relationship exists; semantic alignment not yet proven |
| `schema-aligned` | Reviewed contract and schema agree for the checked version | Meaning/shape alignment is bounded to that review |
| `fixture-backed` | Deterministic positive and negative examples exist | Example boundary is inspectable |
| `validated` | Named validators/tests pass for the checked revision | Only the named assertions are enforced |
| `policy-bound` | Applicable policy inputs, decisions, and negative states are wired and tested | Admissibility behavior is bounded to reviewed rules and tests |
| `release-integrated` | Review, evidence, policy, release, correction, and rollback relationships are verified | Object family participates in governed release flow; publication still depends on actual release records |
| `compatibility-guard` | Path prevents drift or preserves migration lineage | Not canonical object authority |
| `path-conflicted` | Two or more plausible homes or names remain unresolved | Do not create or promote parallel authority |

Never upgrade maturity from prose alone. A badge, README, plan, schema file, passing fixture, or workflow name is evidence only for the surface it directly demonstrates.

[Back to top](#top)

---

## Verified lane inventory

The following inventory is bounded to targeted current-session reads. It is not a recursive manifest.

| Lane | Verified documentation | Current posture |
|---|---|---|
| Root navigation | [`README.md`](./README.md) | Canonical semantic-root boundary |
| Object crosswalk | [`OBJECT_MAP.md`](./OBJECT_MAP.md) | Evidence-limited; not complete registry |
| Domains | [`domains/README.md`](./domains/README.md) | Active domain semantic-contract lane with known slug/path conflicts |
| Source | [`source/README.md`](./source/README.md) | Source-governance semantics; paired SourceDescriptor surfaces confirmed, broader enforcement incomplete |
| Evidence | [`evidence/README.md`](./evidence/README.md) | EvidenceRef/EvidenceBundle semantics; materialized proofs remain elsewhere |
| Runtime | [`runtime/README.md`](./runtime/README.md) | Runtime envelope semantics; aliases/scaffolds and implementation gaps remain |
| Policy | [`policy/README.md`](./policy/README.md) | Policy-object semantics; executable policy remains in root `policy/` |
| Release | [`release/README.md`](./release/README.md) | Mixed-maturity release-object semantics; release state remains elsewhere |
| UI | [`ui/README.md`](./ui/README.md) | Evidence-bounded UI payload semantics; implementation and canonical per-object homes need verification |
| Versioned path | [`v1/README.md`](./v1/README.md) | Compatibility guard; no parallel authority |

Use repository tree generation or an accepted object-family registry for a complete inventory. Do not infer that every file in a listed lane has a paired schema, fixture, validator, policy rule, consumer, or release path.

[Back to top](#top)

---

## Compatibility, versioning, and drift

### Versioned contract path

`contracts/v1/` is currently documented as a compatibility guard. It must not mirror `schemas/contracts/v1/` or become a second semantic-contract root merely because its name contains a version.

### Known drift classes

| Drift class | Current signal | Required posture |
|---|---|---|
| Semantic root vs versioned mirror | `contracts/` and `contracts/v1/` both exist | Keep `contracts/v1/` pointer-only until accepted authority changes |
| Contract vs schema duplication | Historical and compatibility paths can contain schema-like or duplicate definitions | Machine shape stays outside `contracts/`; migrate with ADR/rollback when required |
| Aliases and casing | Runtime and other lanes document snake_case, CamelCase, or folder-form aliases | Identify one semantic authority; keep aliases as explicit compatibility surfaces |
| Domain slug conflicts | Atmosphere/air and Roads-Rail-Trade/transport forms are documented as unresolved | Mark `path-conflicted`; do not add parallel canonical contracts |
| Release/correction seam | Release contracts reference correction objects in a separate family | Preserve distinct responsibilities and resolve ownership through reviewed crosswalks, not silent moves |
| Navigation map vs registry | `OBJECT_MAP.md` exists while `object_family_register.yaml` has `entries: []` | Treat the Markdown map as evidence-limited and populate a machine register only through a reviewed process |

### Change discipline

A change that alters semantic identity, field meaning, compatibility, public behavior, or release interpretation may require:

- ADR review;
- schema versioning;
- migration and deprecation records;
- old-fixture parity;
- consumer updates;
- correction notices for released artifacts;
- rollback targets and a verified reversal path.

Do not create a new path simply to avoid resolving an existing conflict.

[Back to top](#top)

---

## Open verification register

- Complete recursive inventory of `contracts/**/*.md`, file counts, identities, aliases, and ownership.
- Accepted canonical status of ADR-0001 and ADR-0002.
- Complete contract-to-schema-to-fixture-to-validator-to-policy-to-consumer crosswalk.
- Population and governing schema for `control_plane/object_family_register.yaml`.
- Dedicated semantic-contract tests, runner, diagnostics, and CI gate ownership.
- Contract metadata requirements and whether KFM Meta Block v2 is machine-enforced.
- Canonical naming and alias rules for snake_case, CamelCase, folder-form, singular/plural, and domain slugs.
- Classification and migration of `contracts/v1/` and other compatibility surfaces.
- Contract maturity evidence for every public API, UI, map, export, AI, release, correction, and rollback object family.
- Branch protection, required checks, CODEOWNERS enforcement, steward assignments, and independent review thresholds.
- Link and anchor validation across all contract documents and their companion roots.
- Versioning, deprecation, correction, withdrawal, and rollback requirements for released contract-backed objects.
- Whether a generated contract inventory can be produced without turning generated output into authority.

> [!NOTE]
> This README is a repository-grounded documentation contract. It does not claim that every semantic contract is complete, every schema is aligned, every validator runs, every policy is active, every consumer is wired, or any object family is released or published.

[Back to top](#top)
