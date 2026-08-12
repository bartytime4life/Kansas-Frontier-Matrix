<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-readme
title: contracts/ — Canonical Semantic-Meaning Root and Contract Governance Boundary
type: README
version: v0.4
status: draft; repository-grounded; canonical-semantic-contract-root; mixed-maturity; configured-cross-root-validation; non-schema; non-policy; non-release
owner: NEEDS VERIFICATION — CODEOWNERS routes /contracts/ to @bartytime4life; no accepted contract steward, required-review enforcement, or independent approval control was verified
created: 2026-02-21
updated: 2026-08-12
supersedes: v0.3 documentation at the same path; no semantic contract, schema, policy, fixture, validator, test, runtime, release object, or public behavior is superseded
policy_label: repository-facing; contracts; semantic-meaning; cite-or-abstain; no-parallel-authority; evidence-aware; policy-aware; correction-aware; rollback-aware; non-publisher
current_path: contracts/README.md
owning_root: contracts/
responsibility: own human-readable semantic meaning, field intent, invariants, exclusions, compatibility semantics, and object-family navigation without becoming machine shape, admissibility, evidence, lifecycle, release, runtime, or publication authority
truth_posture: cite-or-abstain; contract Markdown defines meaning and promises but never makes a claim true, validates an instance, admits a source, authorizes exposure, approves release, or proves production behavior
evidence_snapshot: bartytime4life/Kansas-Frontier-Matrix@6c78cfd3ef8ccc9608800c132e7da2222c812e57
audit_baseline: 60a54f63404929a4ccb3043a5059a2351747df50
prior_blob: 1561841b0bfdc64c07e8d3bf0aa6a6d5cc240a88
authority_evidence: ADR-0029 blob b01322ef64f8c2b1ecb41de7ef4685b97cfa2a62 adopts Directory Rules blob fd49a0b83e55cef52c1124281f093e263526898d
implementation_evidence: validator registry c65c1c2b27b85be4bdc3c42d0555c6e8e44698e2; object-family register 8673b21ea49cb4a2852595208efdb206ed040690; Makefile c5d0aee3de558d76c1e1639bcfd8cf1c71a0d326
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
  - ../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../docs/doctrine/directory-rules.md
  - ../docs/architecture/directory-rules.md
  - ../docs/architecture/contract-schema-policy-split.md
  - ../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - ../docs/adr/ADR-0002-contracts-vs-schemas-split.md
  - ../.github/workflows/contracts-validate.yml
notes:
  - "This is a same-path Markdown modernization. It creates no root, sibling README, schema, policy rule, fixture, validator, test, receipt, proof, release record, runtime behavior, or publication state."
  - "Path history identifies the first tracked contracts/README.md at commit 8a96629e3fc85872e7fdf4781af767f69b1d7f66 on 2026-02-21; the original file was one newline byte."
  - "Accepted ADR-0029 adopts the exact docs/doctrine/directory-rules.md bytes as the sole writable human Directory Rules authority; §16 defines the ROOT_FULL profile used here."
  - "The repository configures schemas/contracts/v1/ as a machine-shape validation surface, while ADR-0001 and ADR-0002 remain proposed rather than accepted."
  - "At the evidence snapshot, contracts/ has 47 direct entries (45 directories and two Markdown files) and 818 tracked files recursively."
  - "The full validator profile contains ten validators; the historical run_all.py path is a compatibility entrypoint to that profile, not a six-validator authority surface."
  - "The object-family register contains six bounded runtime-family entries and remains PROPOSED, partial, and navigational only."
  - "contracts/OBJECT_MAP.md is an evidence-limited maintainer crosswalk, not a generated or complete object-family registry."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `contracts/` — Canonical Semantic-Meaning Root and Contract Governance Boundary

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#status)
[![Authority: canonical semantic meaning](https://img.shields.io/badge/authority-canonical%20semantic%20meaning-1f6feb?style=flat-square)](#authority-level)
[![Schema-home ADR: proposed](https://img.shields.io/badge/schema--home%20ADR-proposed-d4a72c?style=flat-square)](#adrs)
[![Validation: full profile = 10](https://img.shields.io/badge/full%20profile-10%20validators-8250df?style=flat-square)](#validation)
[![Publisher: no](https://img.shields.io/badge/publisher-no-6e7781?style=flat-square)](#authority-level)

> **One-line purpose.** `contracts/` owns KFM's human-readable object meaning: vocabulary, field intent, invariants, exclusions, compatibility semantics, and the promises that schemas, policy, validators, applications, and release processes must preserve.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Responsibility](#responsibility-and-ownership) · [Status](#status) · [Map](#current-direct-child-map) · [Belongs](#what-belongs-here) · [Does not belong](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Lifecycle](#lifecycle-exposure-and-storage) · [Validation](#validation) · [Review](#review-burden) · [Related roots](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed) · [Authoring contract](#contract-authoring-contract) · [Maturity](#maturity-and-claim-discipline) · [Lanes](#verified-lane-inventory) · [Drift](#compatibility-versioning-and-drift) · [Open verification](#open-verification-register)

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

## Responsibility and ownership

| Concern | Current posture |
|---|---|
| **Authority responsibility** | `contracts/` owns semantic meaning and interface promises under accepted Directory Rules v2; it does not own shape, admissibility, instances, or release state |
| **Accepted authority owner** | **NEEDS VERIFICATION** — no separate accepted contract-steward identity or assignment was verified |
| **Named repository route** | [`CODEOWNERS`](../.github/CODEOWNERS) routes `/contracts/` to `@bartytime4life` |
| **Machine projection** | [`root_registry.yaml`](../control_plane/root_registry.yaml) projects `contracts/` as a public, versioned, durable canonical root and names `@bartytime4life` as owner, reviewer, and permitted writer; the register cannot grant or amend authority |
| **Permitted-writer enforcement** | **NEEDS VERIFICATION** beyond the projection — repository access, rulesets, and branch protection were not treated as proof of an accepted semantic-steward assignment or required review |
| **Accepted stewardship** | **NEEDS VERIFICATION** — CODEOWNERS and projection defaults are routing evidence, not a verified stewardship charter |
| **Required approval controls** | **NEEDS VERIFICATION** — CODEOWNERS and registry entries do not prove required review, branch protection, separation of duties, or approval |
| **Escalation** | Meaning changes go to the contract and affected domain reviewers; placement or authority disputes go through accepted Directory Rules and, when the decision changes authority, an accepted ADR or governed migration |

Contributors may propose changes through repository review, but neither authorship nor write access establishes semantic correctness, policy admission, review approval, release authority, or publication authority.

[Back to top](#top)

---

## Status

Implementation snapshot: `main@6c78cfd3ef8ccc9608800c132e7da2222c812e57`, inspected on 2026-08-12. The target and its listed governing evidence are byte-identical to audit baseline `60a54f63404929a4ccb3043a5059a2351747df50`; nine later commits changed only two worker READMEs and one API-security workflow.

| Surface | Current evidence | Safe conclusion |
|---|---|---|
| `contracts/README.md` profile coverage | **CONFIRMED** at prior blob `1561841b...`; this revision is v0.4 | The same-path document now covers the adopted `ROOT_FULL` fields against the current implementation snapshot; coverage does not certify subtree conformance |
| Root conformance | **PARTIAL / CONFIRMED DRIFT** | Authority and current-state documentation are reconciled, but the three inherited schema files below remain nonconforming and are neither accepted nor migrated by this README |
| Directory Rules authority | **CONFIRMED / ACCEPTED** by [`ADR-0029`](../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md), which adopts exact blob `fd49a0b...` at [`docs/doctrine/directory-rules.md`](../docs/doctrine/directory-rules.md) | The doctrine path is the sole writable human Directory Rules authority; the architecture copy is read-only compatibility pending a separately governed tombstone migration |
| Direct and recursive inventory | **CONFIRMED**: 47 direct entries — 45 directories, `README.md`, and `OBJECT_MAP.md`; 818 tracked files recursively | Presence and counts are current-tree evidence, not proof that every lane is canonical, mature, paired, or consumed |
| Machine-shape placement drift | **CONFIRMED**: three `PROPOSED` scaffold schemas remain at `contracts/atmosphere/air-observation.schema.json`, `contracts/domains/habitat/habitat_patch.schema.json`, and `contracts/people-dna-land/land_ownership_assertion.schema.json` | These files conflict with the adopted responsibility split; disclose and hold new schema writes here pending governed classification and reversible migration rather than treating drift as canonical |
| `contracts/OBJECT_MAP.md` | **CONFIRMED** evidence-limited crosswalk | Useful maintainer orientation; not a complete generated registry or implementation proof |
| Child contract-family documentation | **CONFIRMED** across multiple direct and nested lanes | Descendant-specific authority, alias, compatibility, and maturity statements remain local and mixed |
| `schemas/contracts/v1/` | **CONFIRMED** nonempty configured validation surface with mixed-maturity and compatibility lanes | Machine-shape work exists; completeness and canonical acceptance remain unresolved |
| ADR-0001 | **CONFIRMED `proposed`** | Schema-home proposal is not accepted decision authority |
| ADR-0002 | **CONFIRMED `proposed`** despite draft-form prose | It is not accepted decision authority; the mandatory three-way root split comes from adopted Directory Rules v2 |
| `contracts-validate` workflow | **CONFIRMED command-bearing**; validates a three-family fixture manifest, then runs `make test` | CI definition exercises bounded schema/fixture and test surfaces; a current pass is not inferred from the file alone |
| `make test` | **CONFIRMED narrow aggregate** | Runs `pytest tests/schemas tests/contracts -q`; it is not a complete semantic-contract suite |
| Contract-backed schema fixture test | **CONFIRMED** in `tests/schemas/test_common_contracts.py` | Exercises selected schema families and valid/invalid fixtures; does not prove prose semantics |
| Direct `tests/contracts/` evidence | **CONFIRMED**: two direct `test_*.py` modules plus a bounded manifest lane | Direct executable coverage exists; complete semantic-contract coverage is not established |
| Full validator profile | **CONFIRMED bounded**: ten registered validators, invoked by the compatibility aggregate through the full orchestrator | Configuration and execution scope are implementation evidence, not doctrine or semantic authority |
| Machine object-family register | **CONFIRMED**: six runtime-family entries; status `PROPOSED`, authority `navigational_index_only`, completeness `partial` | The register is a bounded projection, not complete object-family authority or proof of runtime, release, or publication |
| Contract inventory and consumer coverage | **UNKNOWN / incomplete** | No complete contract-to-schema-to-policy-to-consumer registry or coverage artifact was verified |
| Required reviews and branch protection | **NEEDS VERIFICATION** | CODEOWNERS routing does not prove required review or separation of duties |
| Release, publication, and production parity | **DENIED as inference** | Contract presence, schema validity, workflow success, or a merged PR does not establish KFM release or publication |

<a id="material-corrections-from-v02"></a>

### Material corrections from v0.3

- Accepted ADR-0029 and the canonical doctrine path replace the obsolete open-conflict and legacy §15 claims; Directory Rules v2 §16 supplies the current `ROOT_FULL` profile.
- The direct-child map and recursive count are pinned to the implementation snapshot without upgrading descendant maturity.
- `schemas/contracts/v1/` is described as the **configured** v1 machine-shape surface while ADR-0001 remains proposed; the root-level meaning/shape/admissibility split is separately mandatory through adopted Directory Rules v2.
- `make test`, `make validate`, the three-family fixture-manifest step and subsequent test aggregate, the ten-validator full profile, and the common contract-schema fixture test are distinguished by actual scope.
- Direct `tests/contracts/` modules are acknowledged without claiming complete prose-semantic coverage.
- `OBJECT_MAP.md` remains evidence-limited, and the six-entry machine object-family register remains partial, proposed, and navigational only.
- CODEOWNERS routing is separated from stewardship, approval, branch protection, and release authority.
- Immediate documentation rollback targets the prior v0.3 blob.

[Back to top](#top)

---

## Current direct-child map

Verified from `main@6c78cfd3ef8ccc9608800c132e7da2222c812e57`. This map shows direct entries only. A directory's presence does not make it canonical, mature, schema-linked, policy-admitted, implemented, reviewed, released, or published; child documentation owns deeper detail.

```text
contracts/
├── OBJECT_MAP.md        # Evidence-limited navigation crosswalk; not object-family authority
├── README.md            # This ROOT_FULL semantic-meaning boundary
├── agriculture/         # Direct contract lane; local authority and maturity vary
├── ai/                  # Direct contract lane; local authority and maturity vary
├── air/                 # Direct contract lane; alias status remains local evidence
├── archaeology/         # Direct contract lane; local authority and maturity vary
├── atmosphere/          # Direct contract lane; alias status remains local evidence
├── biodiversity/        # Direct contract lane; local authority and maturity vary
├── biotopes/            # Direct contract lane; local authority and maturity vary
├── common/              # Shared semantic-contract lane; not schema or policy authority
├── correction/          # Correction-object meaning; not correction state or execution
├── cross_domain/        # Cross-domain seam meaning; registered ownership still applies
├── crosswalks/          # Semantic navigation/crosswalk lane; not generated authority
├── data/                # Data-object meaning; governed instances remain under data/
├── domains/             # Domain-specific semantic contracts; child lanes own detail
├── evidence/            # Evidence-object meaning; not materialized evidence or proof
├── fauna/               # Direct contract lane; local authority and maturity vary
├── flora/               # Direct contract lane; local authority and maturity vary
├── focus/               # Direct contract lane; alias status remains local evidence
├── focus_mode/          # Direct contract lane; alias status remains local evidence
├── geology/             # Direct contract lane; local authority and maturity vary
├── governance/          # Governance-object meaning; not decisions or approval records
├── habitat/             # Direct contract lane; local authority and maturity vary
├── hazards/             # Direct contract lane; local authority and maturity vary
├── joins/               # Join-object meaning; not executable join behavior
├── layers/              # Layer-object meaning; not rendered or released layers
├── map/                 # Map-object meaning; not UI, tile, or publication state
├── people-dna-land/     # Direct contract lane; alias status remains local evidence
├── people/              # Direct contract lane; alias status remains local evidence
├── policy/              # Policy-object meaning; executable rules remain under policy/
├── receipts/            # Receipt-object meaning; emitted receipts remain elsewhere
├── release/             # Release-object meaning; release decisions remain under release/
├── review/              # Review-object meaning; not proof that review occurred
├── runtime/             # Runtime-object meaning; not runtime execution or state
├── schemas/             # Existing direct lane; no canonical machine-shape authority
├── settlement/          # Direct contract lane; local authority and maturity vary
├── shared/              # Shared semantic-contract lane; ownership remains explicit
├── soil/                # Direct contract lane; local authority and maturity vary
├── source/              # Source-object meaning; not source admission or registry state
├── spatial-foundation/  # Spatial-foundation meaning; local maturity varies
├── story/               # Story-object meaning; not publication authority
├── telemetry/           # Telemetry-object meaning; not logs, receipts, or runtime state
├── transport/           # Direct contract lane; alias status remains local evidence
├── ui/                  # UI payload meaning; not component or public-interface code
├── v1/                  # Compatibility guard; not a second semantic authority
├── validation/          # Validation-object meaning; not validator implementation
└── watchers/            # Proposed-inactive watcher-gate semantics; direct README missing
```

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

## Lifecycle, exposure, and storage

| Dimension | Root posture |
|---|---|
| **Lifecycle relationship** | Contract prose may define the meaning of lifecycle objects and transitions, but governed instances and transition records remain in their accepted data, evidence, policy, review, and release homes |
| **Document change state** | Git history makes proposed and merged bytes inspectable; a commit, merge, or README status does not by itself accept an ADR, approve a semantic change, or transition a governed object |
| **Public exposure** | Tracked contract documents are repository-visible at this snapshot, and the active root registry projects public exposure. They must not embed secrets, private payloads, precise sensitive data, or restricted source material; the projection itself grants no exposure or authority |
| **Sensitivity** | Contracts describe sensitivity, rights, access, and redaction obligations at the semantic level; executable restrictions and decisions remain under policy and governed decision surfaces |
| **Mutation** | Versioned review in place; semantic identity changes require compatibility and migration analysis rather than silent replacement or parallel authority |
| **Retention** | Durable repository documentation with Git lineage; removal or relocation must preserve references, aliases, supersession, consumers, and rollback evidence |
| **Generation** | Human-authored semantic Markdown by default. Any generated projection must identify its source and deterministic regeneration path and must not become semantic authority by generation |
| **Physical storage** | Repository Markdown and navigation only; contract instances, evidence, receipts, proofs, runtime state, release records, and published carriers are prohibited here |

No accepted repository-wide contract-document state machine was verified. Descendant status labels must therefore remain evidence-bounded, and a consumer must not infer implementation or release maturity from a file's presence or merge state.

[Back to top](#top)

---

## Validation

Validation is layered. Machine-shape validation can support a contract; it cannot prove prose semantics by itself.

### Confirmed repository commands and workflows

| Surface | Command or behavior | What it proves | What it does not prove |
|---|---|---|---|
| Validator-registry integrity | `make validator-registry-check` | The bounded registry parses, names existing scripts, and has a valid ten-validator `full` profile for the checked revision | That any validator ran or any contract is semantically correct |
| Root test aggregate | `make test` | Runs `pytest tests/schemas tests/contracts -q` for the checked revision | Complete contract inventory, semantic equivalence, policy behavior, or release readiness |
| Root validation aggregate | `make validate` | Runs `make schemas test`; `schemas` invokes the historical compatibility entrypoint, which delegates to the ten-validator `full` profile, and `test` runs the selected schema/contract tests | Full repository validation, complete semantic coverage, policy admission, or release readiness |
| Canonical validator entrypoint | `python tools/validate_all.py --profile full` | Runs the exact registry-defined full profile for the checked revision | Doctrine, semantic authority, source truth, policy approval, or lifecycle state |
| Compatibility entrypoint | `python tools/validators/_common/run_all.py` | Delegates to the same full orchestrator profile while preserving the historical path and fixture-runner inventory surface | A separate six-validator aggregate or independent authority |
| Contract/schema workflow | `.github/workflows/contracts-validate.yml` | Runs the three-family fixture-manifest validator and then `make test` | Current pass rate, branch-protection coupling, all-family coverage, or complete semantic equivalence |
| Contract fixture manifest | `python tools/validators/validate_contract_fixture_manifest.py tests/contracts/manifests/contract_fixture_families.v1.json --format text` | Declared schema/fixture paths, nonempty valid/invalid lanes, and expected JSON Schema polarity for three families | Markdown semantics, policy, evidence closure, review, release, or publication |
| Common contract-schema fixture test | `python -m pytest tests/schemas/test_common_contracts.py -q` | Valid/invalid fixture behavior for discovered schemas in selected families | Contract Markdown meaning or every schema family |
| Contract object-map overlay | `PYTHONPATH=apps/governed-api/src python tools/validators/docs/validate_contract_object_map_lifecycle.py contracts/OBJECT_MAP.md --repo-root .` | Adjacent sanity check for required overlay markers, selected resource coverage, referenced paths, and governed-API stub-registry parity | Complete object inventory, semantic maturity, deployment, authority, or this README's conformance |
| Changed-file Markdown links | `python tools/validators/docs/link-check/check_links.py --repo-root . --git-diff "<base-sha>...HEAD" --format text` | Local target and fragment integrity for changed Markdown | External-link availability or semantic correctness |
| Target metadata | `python tools/validators/docs/meta-block/check_meta_blocks.py --repo-root . --profile present --format text contracts/README.md` | Bounded structural QA for this metadata block | Doctrine, review, release, or registry mutation; nested evidence metadata remains outside the bounded parser profile |

The full validator profile is configuration, not doctrine. At the snapshot it lists, in registry order: `source-descriptor`, `evidence-ref`, `evidence-bundle`, `layer-manifest`, `runtime-response-envelope`, `decision-envelope`, `run-receipt`, `ingest-receipt`, `workflow-security`, and `repository-topology`. The first eight are fixture-invoked object or carrier checks; the last two are repository guardrails. The `changed-area` profile selects dynamically from path globs and is not evidence of zero capability merely because its static registry list is empty.

The contract workflow's manifest wave covers only `decision-envelope`, `evidence-bundle`, and `runtime-response-envelope`. The selected schema-fixture test separately enumerates the families `evidence`, `runtime`, `common`, `policy`, `source`, `governance`, and `release` when matching schemas and fixture directories exist. Neither scope is a complete semantic-contract inventory.

The validator orchestrator and contract fixture-manifest validator both use finite process outcomes: `PASS` exits `0`, a bounded validation or fixture-polarity `FAIL` exits `1`, and an unsafe input, malformed inventory, or evaluation `ERROR` exits `2`. A caller must preserve those distinctions rather than collapsing every nonzero result into a semantic failure.

The current `docs-meta-block` workflow triggers on Markdown changes but scopes its changed-document scan to root `README.md`, `docs/`, and `tools/validators/docs/`; it does not collect `contracts/README.md`. The explicit target command above is therefore required for this file. That workflow-scope gap is implementation evidence, not authority to widen the workflow in a README-only change.

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
| Validator registry is invalid or the orchestrator cannot run | Report `ERROR` and preserve the nonzero result; do not infer validation success |
| A configured validator rejects its bounded input | Report `FAIL` for that named check and revision; do not generalize the result into policy or release state |
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
| [`tests/contracts/`](../tests/contracts/README.md) | Bounded direct tests and fixture-manifest lane; complete prose-semantic coverage is not established |
| [`tools/validators/`](../tools/validators/README.md) | Reusable validator implementation |
| [`data/`](../data/README.md) | Lifecycle records, source registries, receipts, proofs, catalogs, and published artifacts in their owning lanes |
| [`release/`](../release/README.md) | Release-governance records and decisions |
| [Contract/schema/policy/test split](../docs/architecture/contract-schema-policy-split.md) | Human-readable four-layer boundary explanation |
| [Accepted ADR-0029](../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Adoption decision for the exact Directory Rules v2 bytes and single-write authority |
| [Directory Rules](../docs/doctrine/directory-rules.md) | Sole writable human placement authority; §9.3 defines the three-way split and §16 defines README profiles |
| [Legacy Directory Rules copy](../docs/architecture/directory-rules.md) | Read-only compatibility body pending separately governed tombstone migration; not a writable authority |
| [`contracts-validate`](../.github/workflows/contracts-validate.yml) | Command-bearing CI workflow for the selected schema/contract test aggregate |
| [`root_registry.yaml`](../control_plane/root_registry.yaml) | Active machine projection of adopted root classes; cannot amend doctrine |
| [`object_family_register.yaml`](../control_plane/object_family_register.yaml) | Six-entry partial, proposed, navigational-only runtime-family projection; not complete authority |

[Back to top](#top)

---

## ADRs

Accepted ADR-0029 governs root placement and README conformance. It does not accept a contract-schema split proposal, define object meaning, or establish object-family maturity.

### Current decision posture

- [`ADR-0029 — Adopt Directory Governance Standard v2`](../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) is **accepted**. It adopts the exact bytes at [`docs/doctrine/directory-rules.md`](../docs/doctrine/directory-rules.md) as the sole writable human Directory Rules authority. The adopted rules make the `contracts/` / `schemas/` / `policy/` split mandatory and place `ROOT_FULL` README requirements in §16.
- [`ADR-0001 — Schema Home`](../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) is **proposed**. The repository configures `schemas/contracts/v1/`, but the ADR is not accepted.
- [`ADR-0002 — Contracts vs Schemas Split`](../docs/adr/ADR-0002-contracts-vs-schemas-split.md) is **proposed** despite draft-form prose. It is not accepted decision authority; adopted Directory Rules v2 independently require the root-level meaning/shape/admissibility split.
- [`contracts/v1/`](./v1/README.md) remains a compatibility guard. Making it canonical, mirroring schemas into it, or moving canonical semantic contracts there requires reviewed path authority and a reversible migration.
- [`docs/architecture/directory-rules.md`](../docs/architecture/directory-rules.md) remains a full read-only compatibility dependency. Accepted ADR-0029 keeps tombstoning, reference closure, and deletion on a separately governed hold; its continued presence does not reopen writable authority.

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

**2026-08-12**

Evidence snapshot: `bartytime4life/Kansas-Frontier-Matrix` at implementation base `main@6c78cfd3ef8ccc9608800c132e7da2222c812e57`, prior target blob `1561841b0bfdc64c07e8d3bf0aa6a6d5cc240a88`. The target and listed governing evidence were compared with audit baseline `60a54f63404929a4ccb3043a5059a2351747df50`; no post-audit material file change was present at that implementation base. Live pull-request collision checks are recorded in the implementation PR rather than treated as durable repository fact here.

Review this README again when:

- authority, root class, owner, permitted writer, reviewer, exposure, sensitivity, storage, retention, or generation posture changes;
- a direct contract lane is added, moved, renamed, consolidated, reclassified, or retired;
- an ADR governing placement, semantic identity, schema home, or compatibility is accepted, superseded, or reconsidered;
- ADR-0001 or ADR-0002 changes status;
- `contracts/v1/` changes classification;
- an automated semantic-contract inventory or linter is established;
- the object-family register changes scope, status, authority, or completeness;
- the root test or validation aggregate changes scope;
- a public API, UI, map, export, AI, release, correction, or rollback contract changes materially;
- Directory Rules or accepted placement ADRs change the responsibility split;
- drift, security, correction, withdrawal, or rollback evidence affects this boundary;
- a future risk-based maximum review interval adopted for this root expires.

### Rollback and correction

Documentation rollback is a same-path revert of the commit that introduces this v0.4 README. The immediate byte-level rollback target is prior v0.3 blob `1561841b0bfdc64c07e8d3bf0aa6a6d5cc240a88`.

Reverting this README restores documentation bytes only. It does not revert ADR-0029, Directory Rules, registries, validators, schemas, policy, fixtures, tests, workflows, contract documents, object instances, releases, or public state. The prior v0.3 bytes contain known stale authority and implementation claims, so a revert is a recoverability mechanism, not a recommendation to restore those claims as current truth.

Correct factual errors through a same-path review that re-pins evidence. Reconsider semantic authority through the governing ADR or migration process; README prose must not overturn an accepted decision. When a claim is unresolved, narrow it to `UNKNOWN` or `NEEDS VERIFICATION` rather than filling the gap with implementation inference.

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
| Contract vs schema duplication | Three confirmed `PROPOSED` scaffold schemas remain under `contracts/`: atmosphere air observation, habitat patch, and land ownership assertion | Treat as nonconforming drift; deny new machine-shape writes here and migrate only through governed identity/consumer inventory with rollback |
| Aliases and casing | Runtime and other lanes document snake_case, CamelCase, or folder-form aliases | Identify one semantic authority; keep aliases as explicit compatibility surfaces |
| Domain slug conflicts | Atmosphere/air and Roads-Rail-Trade/transport forms are documented as unresolved | Mark `path-conflicted`; do not add parallel canonical contracts |
| Release/correction seam | Release contracts reference correction objects in a separate family | Preserve distinct responsibilities and resolve ownership through reviewed crosswalks, not silent moves |
| Navigation map vs registry | `OBJECT_MAP.md` is evidence-limited; `object_family_register.yaml` projects six runtime families and declares itself `PROPOSED`, partial, and navigational only | Treat both as bounded navigation; neither is complete semantic or implementation authority |

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

- Complete semantic inventory and ownership classification across the confirmed 818-file `contracts/` subtree.
- Accepted canonical status of ADR-0001 and ADR-0002.
- Complete contract-to-schema-to-fixture-to-validator-to-policy-to-consumer crosswalk.
- Expansion, acceptance posture, governing schema, and completeness criteria for the six-entry partial `control_plane/object_family_register.yaml`.
- Complete semantic-contract tests, runner diagnostics, coverage policy, and CI gate ownership beyond the current bounded modules and fixture-manifest wave.
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
