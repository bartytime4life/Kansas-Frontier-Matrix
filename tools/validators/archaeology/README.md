<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-archaeology-readme
title: tools/validators/archaeology/ — Archaeology Validator Boundary and Maturity Guide
type: readme; directory-readme; domain-validator-lane; archaeology; sensitive-domain; non-authoritative
version: v0.2
status: draft; repository-grounded; README-only-lane; executable-enforcement-unestablished; schemas-mixed-scaffold; policy-scaffold; tests-placeholder; ci-todo-only; fail-closed
owners: OWNER_TBD — Archaeology steward · Validator steward · Evidence steward · Schema steward · Policy steward · Sensitivity reviewer · Cultural-review steward · Rights-holder representative · Release steward · Security steward · Docs steward
created: 2026-07-07
updated: 2026-07-16
supersedes: v0.1 broad Archaeology validator-lane README
policy_label: "repository-facing; tools; validators; archaeology; sensitive-domain; cultural-heritage; evidence-aware; source-role-aware; candidate-not-site; public-no-leak; exact-location-deny; cultural-review; sovereignty; CARE; rights; consent; redaction; catalog-closure; AI-location-deny; release-gated; correction-aware; rollback-aware; no-network-by-default; fail-closed; no-truth-authority; no-policy-authority; no-release-authority"
owning_root: tools/
current_path: tools/validators/archaeology/README.md
responsibility: >
  Repository-grounded boundary and implementation guide for broad Archaeology-domain validation under
  tools/validators/archaeology/. The lane coordinates EvidenceBundle closure, candidate-versus-confirmed-site
  separation, public no-leak checks, rights and cultural review, exact sensitive geometry denial, catalog/proof/release
  closure, AI exact-location denial, deterministic reports, and replay expectations while deferring Archaeology meaning,
  machine shape, policy decisions, source registry authority, cultural authority, evidence/proof records, receipts,
  release authority, public serving, and protected data to their owning roots.
truth_posture: >
  CONFIRMED target README v0.1 and prior blob; tools/validators/archaeology/ surfaced only README.md in bounded
  repository search; tools/validators/domains/archaeology/ is the child-validator index and explicitly defers broad
  Archaeology validation here; canonical domain validator doctrine names seven validator families; contracts, schemas,
  policy files, fixtures, tests, lifecycle documentation, and the domain workflow exist / PROPOSED validation packet,
  deterministic ValidationReport, finite findings, reason-code families, child delegation, no-network fixtures, CI
  admission, migration, correction, deprecation, and rollback / CONFLICTED or drift-prone duplicate homes for broad
  versus child validator routing, contracts/archaeology versus contracts/domains/archaeology, short schema alias versus
  domain schema lane, source-registry paths, and catalog roots / NEEDS VERIFICATION owners, CODEOWNERS, accepted
  contract and schema mappings, source descriptors and rights, policy bundle entrypoints and digest parity, meaningful
  fixtures, executable validators, report/receipt destinations, CI significance, correction cascade, and release-gate
  use / UNKNOWN runtime invocation, production consumers, emitted Archaeology ValidationReports, operational metrics,
  deployment, and current pass results
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  repository_id: "1059091169"
  visibility: public
  base_ref: main
  base_commit: "04e9cbac69305a5d708509ceef62c6f43ca1f41c"
  prior_blob: ce0a80baa25538566fac39864c8f836505ce9aab
  child_index_blob: 8bcf32cdfad56dd8703a27849682c8b9067f0c5c
  validators_doctrine_blob: cec8098a7a71cfc43a5e0370822520c7ef4b5449
  sensitivity_doctrine_blob: ca7888f2d43f022faeef5e1a6e16ab00526cf7aa
  validators_root_blob: e35742288404a1eeb214f8269fbacb1429c0f86a
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  schema_home_adr_blob: ab0010a278d766356845c23055f882f328abb418
  sensitivity_adr_blob: 691251190211b32fe47cba1546adb6c93ad5ea76
  schema_index_blob: 1d2708f4cd74c458258cef457085f058a400681a
  site_schema_blob: 804320ad16317695329a68e7c19ef7e6f79bc42c
  evidence_bundle_schema_blob: 7c952c085d4e5dad026a60e76dabbed79852f1c5
  archaeology_policy_readme_blob: 8d03cdb11361739e7ad33214f76a0cfe4836ff9b
  candidate_not_site_policy_blob: f570a241cf5b7512e9512d146f82c18c1ad91b45
  site_policy_blob: 5796f8c1c586bd517c7dbd46f7c577f750a173a3
  tests_parent_blob: 2b739d5bdf322de4523faa09a2b788be910bf8b0
  evidence_test_blob: 8c3203b7ad4b732ece60e5267bb0df2df8002158
  public_no_leak_test_blob: a980e7db572586cdf2f8e31fae643a841c0f58e1
  workflow_blob: b6a2869314efe2e34890baa5bbbe41d656629dd3
  global_orchestrator_blob: 5f01ac208c46f4ee98750af4fc1032604b670e9b
  codeowners_blob: 6adabefcbe58b9d281f105dbabaea451aa165619
  bounded_path_checks:
    - tools/validators/archaeology/ surfaced only README.md
    - no executable validator or implemented Archaeology ValidationReport producer surfaced under the broad lane
    - tools/validators/domains/archaeology/ surfaced as a README-only child-validator index
    - sampled Archaeology schemas are PROPOSED or permissive scaffolds
    - sampled Archaeology policy files are default-deny PROPOSED scaffolds
    - sampled Archaeology test modules are one-line placeholder docstrings
    - tools/validate_all.py is a placeholder module
    - domain-archaeology workflow executes TODO-only echo commands
related:
  - ../README.md
  - ../_common/README.md
  - ../domains/archaeology/README.md
  - ../../../docs/doctrine/directory-rules.md
  - ../../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - ../../../docs/adr/ADR-0010-deny-by-default-for-dna-rare-species-archaeology-infrastructure.md
  - ../../../docs/domains/archaeology/VALIDATORS.md
  - ../../../docs/domains/archaeology/SENSITIVITY.md
  - ../../../docs/domains/archaeology/CULTURAL_REVIEW.md
  - ../../../docs/domains/archaeology/PUBLICATION_AND_POLICY.md
  - ../../../docs/domains/archaeology/OBJECT_FAMILIES.md
  - ../../../docs/domains/archaeology/PIPELINE.md
  - ../../../docs/domains/archaeology/RELEASE_INDEX.md
  - ../../../contracts/domains/archaeology/
  - ../../../schemas/contracts/v1/domains/archaeology/
  - ../../../policy/domains/archaeology/
  - ../../../policy/sensitivity/archaeology/
  - ../../../fixtures/domains/archaeology/
  - ../../../tests/domains/archaeology/
  - ../../../data/registry/
  - ../../../data/proofs/
  - ../../../data/receipts/
  - ../../../release/
  - ../../../.github/workflows/domain-archaeology.yml
tags: [kfm, tools, validators, archaeology, cultural-heritage, sensitive-location, evidence, candidate-not-site, cultural-review, sovereignty, CARE, redaction, release, rollback]
notes:
  - "This revision changes only this README plus the required generated-work provenance receipt."
  - "No validator code, contract, schema, policy rule, fixture, test, workflow, source descriptor, lifecycle record, release record, API route, map layer, AI answer, or protected payload is created or modified."
  - "File presence is not enforcement: current sampled schemas, policies, tests, orchestrator, and workflow remain scaffolds or placeholders."
  - "Human review is required before any validator, policy, redaction, cultural-review, release, or public-surface claim is promoted."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Archaeology Validator Boundary and Maturity Guide

`tools/validators/archaeology/`

> **One-line purpose.** This lane defines the broad, fail-closed validation boundary for Archaeology candidates and release-bound derivatives—checking evidence, candidate/site identity, rights, cultural review, sensitivity, redaction, catalog closure, AI-location safety, correction, and rollback without becoming Archaeology truth, cultural authority, policy authority, release authority, or a protected-data store.

<p>
  <img alt="Status: draft" src="https://img.shields.io/badge/status-draft-yellow">
  <img alt="Version: v0.2" src="https://img.shields.io/badge/version-v0.2-informational">
  <img alt="Root: tools" src="https://img.shields.io/badge/root-tools%2F-blue">
  <img alt="Lane: archaeology validators" src="https://img.shields.io/badge/lane-archaeology__validators-6E4C1E">
  <img alt="Implementation: README only" src="https://img.shields.io/badge/implementation-README__only-orange">
  <img alt="Sensitivity: T4 default" src="https://img.shields.io/badge/sensitivity-T4__default-critical">
  <img alt="Posture: fail closed" src="https://img.shields.io/badge/posture-fail__closed-critical">
  <img alt="Truth: cite or abstain" src="https://img.shields.io/badge/truth-cite__or__abstain-success">
</p>

> [!IMPORTANT]
> **Current executable enforcement is not established.** Bounded repository search surfaced only this README under `tools/validators/archaeology/`; no broad-lane validator executable or implemented Archaeology `ValidationReport` producer was found.

> [!CAUTION]
> **Presence is not maturity.** Archaeology contracts, schemas, policy files, fixtures, tests, and a domain workflow are present, but sampled schemas are permissive `PROPOSED` scaffolds, sampled policy files contain only default-deny scaffolding, sampled tests are placeholder modules, the global validator orchestrator is a placeholder, and the domain workflow runs TODO-only echo commands.

> [!WARNING]
> **Protected locations and cultural information must fail closed.** Exact site geometry, burial and human-remains information, sacred or culturally sensitive material, collection-security detail, looting-risk information, restricted oral history, sovereignty-bearing knowledge, and reverse-engineerable derivatives must not be exposed through logs, reports, maps, tiles, APIs, exports, search, graph projections, screenshots, embeddings, Focus Mode, or AI answers.

**Quick links:** [Purpose](#purpose) · [Status](#status-and-evidence) · [Placement](#directory-rules-and-authority) · [Inventory](#confirmed-repository-inventory) · [Topology](#validator-lane-topology) · [Packet](#validation-input-packet) · [Validators](#seven-canonical-validator-families) · [Invariants](#validation-invariants) · [Report](#validation-report-contract) · [Outcomes](#finite-outcomes-and-reason-codes) · [Maturity](#contract-schema-policy-test-and-ci-maturity) · [Security](#security-privacy-and-untrusted-content) · [Lifecycle](#lifecycle-release-correction-and-rollback) · [Tests](#tests-fixtures-and-no-network-posture) · [CI](#ci-admission-contract) · [Implementation](#smallest-sound-implementation-sequence) · [Done](#definition-of-done) · [Migration](#migration-compatibility-and-deprecation) · [Open](#open-verification-register) · [Rollback](#rollback-path) · [Ledger](#evidence-ledger) · [Changelog](#changelog)

---

<a id="purpose"></a>

## Purpose

`tools/validators/archaeology/` is the broad Archaeology validator lane under the durable `tools/validators/` checker surface.

The durable validation question is:

> Does the candidate preserve Archaeology object identity, evidence closure, source role, candidate-versus-confirmed status, rights, sovereignty and cultural review, sensitivity, public-safe transformation, release state, correction lineage, and rollback support for the requested use—without revealing protected information or allowing a validator result to become authority?

This lane may eventually orchestrate deterministic checks for:

- `EvidenceRef` resolution to an admissible `EvidenceBundle`;
- candidate-feature versus confirmed-site separation;
- public no-leak constraints across structured and narrative output;
- rights, attribution, sovereignty, CARE, consent, revocation, embargo, and cultural-review posture;
- exact sensitive geometry denial and public-safe transform receipts;
- catalog, proof, review, release, correction, withdrawal, and rollback closure;
- AI and Focus Mode exact-location denial, including triangulation and reverse inference;
- schema/contract/policy version references, `spec_hash`, replay, and deterministic report integrity.

This lane must not:

- define Archaeology object meaning;
- define or silently select machine schemas;
- define policy or sensitivity thresholds;
- decide cultural authority, rights-holder authority, or release approval;
- store source payloads, exact coordinates, protected cultural records, receipts, proofs, or release records;
- serve public API, map, tile, export, search, graph, or AI output;
- convert a candidate, anomaly, model, or remote-sensing feature into a confirmed archaeological site.

[Back to top](#top)

---

<a id="status-and-evidence"></a>

## Status and evidence

### Task contract

| Field | Value |
|---|---|
| `task_id` | `kfm-doc-tools-validators-archaeology-readme-20260716` |
| Goal | Replace v0.1 with a repository-grounded v0.2 README that accurately describes the broad Archaeology validator lane, current maturity, safety boundaries, test/CI expectations, implementation sequence, and rollback. |
| Repository | `github.com/bartytime4life/Kansas-Frontier-Matrix` |
| Base | `main` pinned at `04e9cbac69305a5d708509ceef62c6f43ca1f41c` for authoring and mutation; rechecked before write. |
| Target | `tools/validators/archaeology/README.md` |
| Operation | `revise-existing-doc` |
| Authority | `IMPLEMENT` |
| Delivery | Scoped branch plus draft pull request |
| Execution profile | `API_ONLY_STRICT` |
| Change budget | Two files: this README and one generated provenance receipt under `data/receipts/generated/`. |
| Non-goals | No executable validator, schema, policy, fixture, test, workflow, source registry, lifecycle, release, API/UI/map, or sensitive-data change. |
| Stop conditions | Target blob drift, repository identity mismatch, unsafe mutation primitive, path-authority conflict requiring structural change, or evidence that the requested edit would expose protected information. |

### Current repository status

| Surface | Status | Evidence-bounded finding |
|---|---|---|
| `tools/validators/archaeology/README.md` | **CONFIRMED** | v0.1 exists at prior blob `ce0a80baa25538566fac39864c8f836505ce9aab`. |
| Broad-lane executable | **UNKNOWN / not surfaced** | Bounded search found only this README under the target folder. Absence is bounded to the search performed; it is not a recursive clone proof. |
| `tools/validators/domains/archaeology/README.md` | **CONFIRMED** | Child-validator index exists and explicitly defers broad validation to this lane. |
| Canonical validator doctrine | **CONFIRMED repo evidence / draft** | `docs/domains/archaeology/VALIDATORS.md` names seven validator families and receipt/replay/CI expectations. |
| Sensitivity doctrine | **CONFIRMED repo evidence / draft** | `docs/domains/archaeology/SENSITIVITY.md` defaults protected Archaeology material to T4/rank 5 and requires named, receipted transforms plus review. |
| Contracts | **CONFIRMED files / maturity mixed** | Many Archaeology semantic contracts exist; duplicate or compatibility contract homes remain unresolved. |
| Schemas | **CONFIRMED files / sampled scaffolds** | Many domain schemas exist; sampled schemas remain permissive or minimal `PROPOSED` scaffolds. |
| Policy | **CONFIRMED files / sampled scaffolds** | Domain and sensitivity policy files exist; sampled files are default-deny `PROPOSED` scaffolds rather than complete rule sets. |
| Tests | **CONFIRMED filenames / sampled placeholders** | Archaeology test modules exist; sampled modules contain only placeholder docstrings. |
| Fixtures | **CONFIRMED README surfaces / payload maturity NEEDS VERIFICATION** | Domain, public-safe, golden, valid/invalid, and object-family fixture lanes are visible, but meaningful coverage was not proven here. |
| Global orchestrator | **CONFIRMED placeholder** | `tools/validate_all.py` contains only a generated placeholder docstring. |
| Domain workflow | **CONFIRMED TODO-only** | `.github/workflows/domain-archaeology.yml` triggers on PR/push but runs only TODO echo steps. |
| Runtime use and emitted reports | **UNKNOWN** | No runtime invocation, production consumer, generated Archaeology `ValidationReport`, dashboard metric, or current pass result was verified. |

### Truth-label rule

- **CONFIRMED** means a path, blob, field, or content claim was inspected in the pinned repository state.
- **PROPOSED** means this README defines a future contract, implementation sequence, report shape, test, or enforcement behavior.
- **NEEDS VERIFICATION** means the item is checkable but not proven strongly enough for use.
- **UNKNOWN** means current behavior or operational maturity could not be established.
- `DENY`, `ABSTAIN`, `ERROR`, and `NEEDS_REVIEW` are finite system outcomes, not truth labels.

[Back to top](#top)

---

<a id="directory-rules-and-authority"></a>

## Directory Rules and authority

The existing target path is correctly rooted by responsibility:

| Concern | Owning root or lane | This README's relationship |
|---|---|---|
| Broad Archaeology validator coordination | `tools/validators/archaeology/` | **This lane.** Durable checker/orchestrator boundary. |
| Narrow Archaeology child validators | `tools/validators/domains/archaeology/<child>/` | Delegated child or edge lanes; not a competing broad implementation. |
| Shared validator plumbing | `tools/validators/_common/` | Shared deterministic helpers only. |
| Archaeology meaning | `contracts/domains/archaeology/` plus reviewed compatibility/migration records | Read and validate; do not redefine. |
| Machine shape | `schemas/contracts/v1/domains/archaeology/` under the schema-home decision | Read and validate; do not redefine. |
| Policy and sensitivity | `policy/domains/archaeology/`, `policy/sensitivity/archaeology/`, and accepted policy homes | Evaluate; do not author decisions locally. |
| Domain doctrine | `docs/domains/archaeology/` | Human authority and scope guidance. |
| Source identity and rights | Accepted `data/registry/` source lanes | Resolve references; do not create source authority here. |
| Evidence, receipts, and proofs | Accepted `data/proofs/` and `data/receipts/` lanes | Reference outputs; do not store them here. |
| Tests and fixtures | `tests/domains/archaeology/`, `fixtures/domains/archaeology/`, and accepted shared fixture lanes | Prove enforcement; do not embed production data. |
| Release, correction, withdrawal, rollback | `release/` | Check references; do not approve or publish. |
| Public API/UI/map/AI | Governed `apps/`, packages, and runtime paths | Consume only released, public-safe results. |

**Directory Rules basis:**

- `tools/` owns durable validators, generators, builders, and checkers.
- domain names appear as segments inside responsibility roots, not as new roots;
- contracts own semantic meaning, schemas own machine shape, policy owns admissibility, tests/fixtures prove enforcement, data owns lifecycle/evidence/receipt artifacts, and release owns release decisions;
- changing schema-home authority or creating parallel contract/schema/policy/registry/release homes requires ADR or migration discipline;
- this edit keeps the existing path and creates no new authority root.

### Authority ladder for this lane

1. Core KFM lifecycle, trust-membrane, cite-or-abstain, and fail-closed doctrine.
2. Accepted ADRs and machine-readable contracts/schemas/policy that actually govern the validation run.
3. Current repository implementation and tests for current behavior.
4. `docs/domains/archaeology/VALIDATORS.md` and sensitivity/publication doctrine.
5. This README as a routing and implementation guide.
6. Domain reports and older blueprints as lineage.
7. Generated prose, path names, UI state, map state, and AI output—never authority.

[Back to top](#top)

---

<a id="confirmed-repository-inventory"></a>

## Confirmed repository inventory

The table records what was inspected, not what is assumed.

| Surface | Confirmed evidence | Maturity interpretation |
|---|---|---|
| Broad validator lane | `tools/validators/archaeology/README.md` only | README-only; executable enforcement unestablished. |
| Child validator index | `tools/validators/domains/archaeology/README.md` | README-only; no confirmed child lane in the inspected index. |
| Domain validator doctrine | `docs/domains/archaeology/VALIDATORS.md` | Detailed draft doctrine; not executable proof. |
| Sensitivity doctrine | `docs/domains/archaeology/SENSITIVITY.md` | Detailed draft posture; machine enforcement still requires policy, tests, and release integration. |
| Semantic contracts | `contracts/domains/archaeology/` contains site, candidate, review, transform, observation, receipt, and release-related documents | File presence confirmed; duplicate names/homes and acceptance state require review. |
| Schema family | `schemas/contracts/v1/domains/archaeology/` contains many `.schema.json` files | Presence confirmed; sampled shapes are permissive/minimal and cannot prove strong validation. |
| Policy family | `policy/domains/archaeology/` and sensitivity lanes contain `.rego` files | Presence confirmed; sampled modules only default deny and identify themselves as `PROPOSED` scaffolds. |
| Test family | `tests/domains/archaeology/test_*.py` contains validator-oriented filenames | Presence confirmed; sampled files are one-line placeholder docstrings. |
| Fixture family | `fixtures/domains/archaeology/` and `fixtures/domains/archaeology-public-safe/` | README/structure presence confirmed; substantive fixture completeness needs verification. |
| Orchestrator | `tools/validate_all.py` | Placeholder; not a functioning all-validator command. |
| Workflow | `.github/workflows/domain-archaeology.yml` | Runs checkout plus TODO echo steps; no substantive validation or publication. |
| CODEOWNERS | `.github/CODEOWNERS` | Generic team placeholders exist; no Archaeology- or tools-specific owner rule is present. |

### Sampled maturity evidence

The following sampled files bound current claims:

- `site.schema.json` has an empty `properties` object and `additionalProperties: true`;
- `evidence_bundle.schema.json` requires only `id`, allows additional properties, and references an unverified child-validator path;
- `candidate_not_site.rego` and `site.rego` contain package declarations, scaffold comments, and `default allow := false`;
- `test_evidence_bundle_required.py` and `test_public_no_leak.py` contain only placeholder module docstrings;
- `tools/validate_all.py` contains only a placeholder docstring;
- `domain-archaeology.yml` runs `echo TODO ...` for validation, proof build, and publish dry run.

These samples do **not** prove every file in those families is a scaffold. They prove only that file presence cannot be treated as lane-wide enforcement maturity.

[Back to top](#top)

---

<a id="validator-lane-topology"></a>

## Validator lane topology

KFM currently exposes two Archaeology validator paths. Their roles must remain distinct:

```text
tools/validators/
├── archaeology/
│   └── README.md                  # broad domain validation boundary; this document
└── domains/
    └── archaeology/
        └── README.md              # narrow child/edge validator index
```

| Concern | Preferred lane | Rule |
|---|---|---|
| Seven broad canonical Archaeology validator families | `tools/validators/archaeology/` | One broad orchestrator/contract boundary. |
| Narrow specialty, edge, or object-family validator | `tools/validators/domains/archaeology/<child>/` | Must have distinct scope, accepted inputs, outputs, policy, fixtures, and owner. |
| Shared evidence, geometry, citation, release, or sensitivity helper | Existing shared validator lane or `_common/` | Do not fork a local copy. |
| Cross-domain Archaeology join | `tools/validators/cross-domain-joins/` or accepted cross-lane path | Preserve both domain authorities; no role collapse. |

### Anti-duplication rule

A future executable must not be implemented independently in both broad and child trees.

Before adding code:

1. name the validator family and owner;
2. decide whether it is broad orchestration, narrow child logic, or shared logic;
3. record the canonical entrypoint and any compatibility alias;
4. use one reason-code namespace and one report contract;
5. add migration/deprecation notes for any replaced path;
6. add valid, invalid, and no-network fixtures;
7. prove the broad runner delegates rather than duplicates.

### Related placement drift that validators must not resolve silently

The inspected repository also contains unresolved or compatibility-prone surfaces:

- `contracts/archaeology/` and `contracts/domains/archaeology/`;
- `schemas/contracts/v1/archaeology/` and `schemas/contracts/v1/domains/archaeology/`;
- case/filename variants for publication-transform receipt contracts;
- source-registry paths under both domain-first and source-first shapes;
- top-level `catalog/` lineage beside canonical `data/catalog/`.

This README does not select or migrate those authorities. A validator implementation must consume an accepted mapping and fail closed when authority is ambiguous.

[Back to top](#top)

---

<a id="validation-input-packet"></a>

## Validation input packet

The broad runner should receive one immutable, serializable packet rather than reach into ambient stores.

### Proposed minimum packet

```yaml
validation_request:
  request_id: <stable id>
  contract_version: "3.0.0"
  validator_profile: archaeology
  requested_operation: <ingest | normalize | catalog | release | api | map | export | focus_mode | ai>
  requested_surface: <internal | steward | restricted | public>
  audience_tier: <T0 | T1 | T2 | T3 | T4>
  object_ref: <stable object reference>
  object_family: <declared Archaeology object family>
  domain_slug: archaeology
  candidate_status: <candidate | reviewed_candidate | confirmed | disputed | withdrawn>
  source_descriptor_refs: []
  evidence_refs: []
  contract_ref: <semantic contract>
  schema_ref: <machine schema>
  policy_bundle_ref: <bundle id + digest>
  sensitivity:
    rank: <0-5>
    exact_geometry_present: <true | false>
    protected_attributes_present: []
    sovereignty_labels: []
  rights:
    status: <known | restricted | unknown>
    attribution_refs: []
    consent_refs: []
    embargo_refs: []
    revocation_refs: []
  cultural_review:
    required: <true | false>
    review_refs: []
    rights_holder_refs: []
  transform:
    required: <true | false>
    profile_ref: <named versioned profile or null>
    receipt_ref: <RedactionReceipt or equivalent>
  release:
    state: <candidate | reviewed | released | superseded | withdrawn>
    policy_decision_ref: <ref or null>
    release_manifest_ref: <ref or null>
  correction:
    correction_notice_ref: <ref or null>
  rollback:
    rollback_card_ref: <ref or null>
  integrity:
    spec_hash: <canonical hash>
    input_hashes: []
```

### Packet rules

- No packet may embed protected source payloads when stable references suffice.
- Exact coordinates and protected fields must be excluded, encrypted, or represented by restricted references according to accepted policy.
- Remote URLs must not be fetched implicitly by the default validator.
- `schema_ref`, `contract_ref`, and `policy_bundle_ref` must be versioned and integrity-pinned.
- Missing or ambiguous authority references must not fall back to path guessing.
- `requested_surface` controls required strictness; public is never inferred from a filename.
- The most restrictive sensitivity, rights, consent, embargo, and review posture wins across joins and derivatives.
- The validator must return a deterministic report for the same packet, rules, and dependency digests.

[Back to top](#top)

---

<a id="seven-canonical-validator-families"></a>

## Seven canonical validator families

The domain doctrine names seven broad families. The table translates them into an implementation contract without claiming they are implemented.

| ID | Family | Minimum checks | Primary reason codes | Current maturity |
|---|---|---|---|---|
| `ARCH-V1` | EvidenceBundle required | EvidenceRef presence; resolver result; source role; citation support; temporal/spatial scope; release eligibility | `EVIDENCE_BUNDLE_REQUIRED`, `EVIDENCE_UNRESOLVED`, `CITATION_INVALID`, `SOURCE_ROLE_UNRESOLVED` | Schema/test names present; sampled test placeholder; executable not surfaced. |
| `ARCH-V2` | Candidate not site | Object family; candidate state; confirmation evidence; review state; language and map-label posture | `CANDIDATE_SITE_COLLAPSE`, `CONFIRMATION_EVIDENCE_MISSING`, `STATUS_MISREPRESENTED` | Policy/test names present; sampled policy/test scaffolds; executable not surfaced. |
| `ARCH-V3` | Public no leak | Exact geometry; identifiers; collection security; sacred/human-remains detail; looting risk; reverse inference across all public carriers | `PUBLIC_LEAK_DENIED`, `RECONSTRUCTION_RISK`, `PROTECTED_ATTRIBUTE_PRESENT` | Test filename present; sampled test placeholder; executable not surfaced. |
| `ARCH-V4` | Rights and cultural review | Rights status; attribution; CARE; sovereignty; consent; revocation; embargo; required reviewers; separation of duties | `CULTURAL_REVIEW_REQUIRED`, `RIGHTS_UNRESOLVED`, `CONSENT_REQUIRED`, `EMBARGO_ACTIVE`, `SOVEREIGNTY_REVIEW_REQUIRED` | Policy/test names present; sampled policy scaffold; executable not surfaced. |
| `ARCH-V5` | Exact sensitive geometry denial | Geometry precision; public audience; named transform profile; transform receipt; minimum generalization; leakage via joins/tiles | `SENSITIVE_GEOMETRY_DENIED`, `REDACTION_PROFILE_MISSING`, `REDACTION_RECEIPT_MISSING`, `GENERALIZATION_INSUFFICIENT` | Schema/policy/test paths present; enforcement and thresholds need verification. |
| `ARCH-V6` | Catalog closure | Catalog record; proof/evidence references; hashes; review/policy state; release manifest; correction and rollback targets | `CATALOG_CLOSURE_MISSING`, `PROOF_REFERENCE_MISSING`, `RELEASE_MANIFEST_MISSING`, `ROLLBACK_REFERENCE_MISSING` | Catalog/release schemas and test filename present; executable not surfaced. |
| `ARCH-V7` | AI exact-location denial | Prompt intent; response content; map context; indirect clues; coordinate narrowing; hidden identifiers; safe redirect/abstention | `AI_LOCATION_DENIED`, `AI_TRIANGULATION_RISK`, `AI_POLICY_CONTEXT_MISSING`, `AI_CITATION_INVALID` | Policy/test names present; sampled test placeholder; executable not surfaced. |

### Cross-cutting checks

Every family should also evaluate:

- schema validity against the pinned schema;
- policy bundle digest and CI/runtime parity;
- contract/schema pair consistency;
- deterministic `spec_hash`;
- source and evidence freshness where material;
- correction, supersession, withdrawal, and rollback references;
- safe logs and report redaction;
- replay/golden-hash stability;
- no-network behavior for default fixtures.

[Back to top](#top)

---

<a id="validation-invariants"></a>

## Validation invariants

| Invariant | Required behavior | Forbidden shortcut |
|---|---|---|
| Cite or abstain | Claim-bearing output resolves evidence or returns `ABSTAIN`/`DENY`. | Generated language, UI labels, filenames, or model confidence as proof. |
| Candidate is not site | Candidate/anomaly/model output remains candidate until accepted confirmation and review exist. | Promoting by map display, classifier score, repetition, or source count alone. |
| Most restrictive posture wins | Joins and derivatives inherit the strongest rights/sensitivity/review constraints. | Using the least restrictive input or public style as policy. |
| Exact protected location defaults to deny | Public-bound exact geometry and reverse-engineerable detail are denied. | Client-side hiding, undocumented jitter, or coarse styling over precise payloads. |
| Transform must be named and receipted | Public-safe transform references a versioned profile and receipt. | Ad hoc coordinate edits or unrecorded field deletion. |
| Cultural review is not generic QA | Required cultural/rights-holder review is explicit and role-aware. | Treating developer approval or validator pass as cultural authority. |
| Validator pass is not release | ValidationReport is one input to promotion. | Writing directly to `data/published/` or marking released on pass. |
| Public clients stay downstream | Public surfaces use governed APIs and released artifacts. | Direct reads from RAW, WORK, QUARANTINE, restricted, canonical, graph-internal, or model stores. |
| Receipts remain auditable | Report, policy, transform, release, correction, and rollback references are stable and integrity-bound. | Mutable in-place “latest” records with no lineage. |
| Failure is finite and safe | Unknown or failed prerequisites produce structured negative outcomes. | Warning-only pass, best-effort allow, or implicit default. |
| Sensitive data stays out of tooling logs | Findings use safe references and coarse descriptions. | Coordinates, exact site IDs, sacred details, collection locations, or access tokens in logs. |
| Watchers and validators are non-publishers | They may report, quarantine, or open review work. | Silent publication or auto-approval. |

[Back to top](#top)

---

<a id="validation-report-contract"></a>

## Validation report contract

A future runner should emit a deterministic `ValidationReport` or accepted Archaeology specialization.

### Proposed minimum report

```json
{
  "report_id": "archval:<request-id>:<spec-hash-prefix>",
  "contract_version": "3.0.0",
  "validator_profile": "archaeology",
  "validator_version": "<version>",
  "outcome": "PASS | DENY | ABSTAIN | ERROR | NEEDS_REVIEW",
  "request_id": "<stable id>",
  "object_ref": "<safe reference>",
  "requested_operation": "<operation>",
  "requested_surface": "<surface>",
  "checks_run": [],
  "findings": [
    {
      "validator_id": "ARCH-Vx",
      "outcome": "PASS | DENY | ABSTAIN | ERROR | NEEDS_REVIEW",
      "reason_code": "<stable code>",
      "message": "<public-safe explanation>",
      "evidence_refs": [],
      "obligations": []
    }
  ],
  "dependency_digests": {
    "contract": "<digest>",
    "schema": "<digest>",
    "policy_bundle": "<digest>",
    "fixture_lock": "<digest or null>"
  },
  "input_hashes": [],
  "spec_hash": "<canonical hash>",
  "started_at": "<timestamp>",
  "finished_at": "<timestamp>",
  "receipt_refs": [],
  "human_review": {
    "required": true,
    "review_refs": []
  }
}
```

### Report rules

- One invocation produces one report even when the outcome is negative or an internal error occurs.
- Reports contain references, reason codes, and obligations—not protected data.
- Finding order is deterministic.
- Dependency digests are mandatory for promotion-bound use.
- A `PASS` means only that configured checks passed for the packet and rule versions.
- A report cannot approve publication, satisfy cultural review, or replace a `PolicyDecision`, `ReleaseManifest`, `CorrectionNotice`, or `RollbackCard`.
- Human review state must remain independent from AI authorship and validator execution.

[Back to top](#top)

---

<a id="finite-outcomes-and-reason-codes"></a>

## Finite outcomes and reason codes

### Top-level outcomes

| Outcome | Meaning | Required handling |
|---|---|---|
| `PASS` | All configured checks passed for the requested operation and surface. | Continue to the next governed gate; do not publish solely because of this result. |
| `DENY` | Policy or sensitivity posture blocks the requested operation. | Stop; preserve safe reason codes and obligations; do not expose protected detail. |
| `ABSTAIN` | Evidence or authority is insufficient or unresolved. | Do not make the claim; request narrower scope or missing governed support. |
| `NEEDS_REVIEW` | A named human/cultural/rights-holder/release review is required. | Hold the candidate; do not auto-approve. |
| `ERROR` | Validation could not complete safely. | Fail closed; record the error without sensitive payload leakage. |

### Stable reason-code families

| Family | Example codes |
|---|---|
| Evidence | `EVIDENCE_BUNDLE_REQUIRED`, `EVIDENCE_UNRESOLVED`, `CITATION_INVALID`, `SOURCE_ROLE_UNRESOLVED` |
| Identity/status | `CANDIDATE_SITE_COLLAPSE`, `STATUS_MISREPRESENTED`, `OBJECT_FAMILY_UNRESOLVED` |
| Public safety | `PUBLIC_LEAK_DENIED`, `RECONSTRUCTION_RISK`, `PROTECTED_ATTRIBUTE_PRESENT` |
| Rights/culture | `CULTURAL_REVIEW_REQUIRED`, `RIGHTS_UNRESOLVED`, `CONSENT_REQUIRED`, `REVOCATION_ACTIVE`, `EMBARGO_ACTIVE`, `SOVEREIGNTY_REVIEW_REQUIRED` |
| Geometry/transform | `SENSITIVE_GEOMETRY_DENIED`, `REDACTION_PROFILE_MISSING`, `REDACTION_RECEIPT_MISSING`, `GENERALIZATION_INSUFFICIENT` |
| Catalog/release | `CATALOG_CLOSURE_MISSING`, `PROOF_REFERENCE_MISSING`, `POLICY_DECISION_MISSING`, `RELEASE_MANIFEST_MISSING`, `CORRECTION_REFERENCE_MISSING`, `ROLLBACK_REFERENCE_MISSING` |
| AI/runtime | `AI_LOCATION_DENIED`, `AI_TRIANGULATION_RISK`, `AI_POLICY_CONTEXT_MISSING`, `AI_CITATION_INVALID` |
| Integrity/operations | `SCHEMA_INVALID`, `CONTRACT_SCHEMA_DRIFT`, `POLICY_PARITY_UNVERIFIED`, `SPEC_HASH_MISMATCH`, `REPLAY_DRIFT`, `REPORT_DESTINATION_INVALID`, `INTERNAL_ERROR` |

Reason codes should live in an accepted contract/schema or registry, not only in this README.

[Back to top](#top)

---

<a id="contract-schema-policy-test-and-ci-maturity"></a>

## Contract, schema, policy, test, and CI maturity

### Maturity model

| Level | Meaning | Evidence needed |
|---|---|---|
| `README_ONLY` | Routing or intent documented. | README exists. |
| `SCAFFOLD` | File exists with placeholder/default-deny/permissive content. | Direct file inspection. |
| `DRAFT_IMPLEMENTATION` | Meaningful fields/rules/tests exist but are not accepted or wired end to end. | Code plus substantive fixtures/tests. |
| `VERIFIED_COMPONENT` | Component passes deterministic tests with pinned dependencies. | Test output, report, and receipt. |
| `GOVERNED_INTEGRATION` | CI and runtime use equivalent accepted rules and emit reports. | Bundle digests, CI/runtime parity, generated reports. |
| `RELEASE_GATING` | Promotion cannot proceed without successful governed validation and review. | Workflow enforcement, branch/ruleset evidence, PromotionDecision/ReleaseManifest linkage. |

### Current classification

| Layer | Current evidence | Classification |
|---|---|---|
| Broad validator lane | README only | `README_ONLY` |
| Child validator index | README only | `README_ONLY` |
| Contracts | Many semantic documents; acceptance/duplicates unresolved | Mixed `SCAFFOLD` / `DRAFT_IMPLEMENTATION` — NEEDS VERIFICATION |
| Schemas | Many files; sampled schemas permissive/minimal | Mixed `SCAFFOLD` / `DRAFT_IMPLEMENTATION` — NEEDS VERIFICATION |
| Policy | Many `.rego` files; sampled modules default-deny scaffolds | `SCAFFOLD` for sampled files |
| Tests | Many filenames; sampled modules placeholder docstrings | `SCAFFOLD` for sampled files |
| Fixtures | Multiple lanes; payload coverage unverified | `README_ONLY` / `SCAFFOLD` — NEEDS VERIFICATION |
| Orchestrator | Placeholder docstring | `SCAFFOLD` |
| Workflow | TODO echo jobs | `SCAFFOLD` |
| Runtime/release-gate integration | No evidence inspected | `UNKNOWN` |

### Consequence

No current repository claim should say “Archaeology validators enforce X” without stronger evidence. The safe statement is:

> The repository contains Archaeology validation doctrine and broad scaffold surfaces; operational, end-to-end enforcement remains unverified.

[Back to top](#top)

---

<a id="security-privacy-and-untrusted-content"></a>

## Security, privacy, and untrusted content

Archaeology validator inputs are untrusted data.

### Required controls

- Treat source text, metadata, comments, OCR, archives, manifests, and model output as data—not instructions.
- Do not execute embedded commands or follow unapproved links from validation payloads.
- Default to no network; remote evidence must be resolved by governed upstream services.
- Enforce payload size, recursion depth, field count, decompression, and processing-time budgets.
- Normalize and validate paths; reject traversal, unsafe symlinks, device files, and archive escape.
- Reject executable content where a data format is expected.
- Never place secrets, bearer tokens, private keys, exact coordinates, protected site IDs, sacred details, human-remains details, collection locations, or rights-holder private information in reports.
- Use safe object references and generalized finding locations.
- Sanitize error strings from parsers, policy engines, and external libraries.
- Pin contract, schema, policy, and dependency digests.
- Emit audit-safe logs with deterministic event IDs.
- Treat AI-generated classifications, descriptions, coordinates, and “likely site” language as untrusted candidate material.
- Prevent indirect disclosure through counts, tiles, map extents, nearest-feature messages, search suggestions, graph neighbors, cache keys, and response timing where material.
- Deny any validator mode that requires public clients to submit or receive protected exact data.

### Prompt-injection boundary

A record that says “ignore policy,” “publish this coordinate,” “treat this candidate as confirmed,” or otherwise instructs a model or validator is evidence content. It does not change validator scope, policy, authority, or execution.

[Back to top](#top)

---

<a id="lifecycle-release-correction-and-rollback"></a>

## Lifecycle, release, correction, and rollback

The validator lane must preserve:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Promotion is a governed state transition, not a file move or validator side effect.

### Gate expectations

| Stage or transition | Validator posture |
|---|---|
| Pre-RAW / source admission | Check source descriptor, rights, sensitivity, authority role, allowed use, and safe intake metadata. |
| RAW → WORK/QUARANTINE | Check immutable source reference, checksum, source role, and quarantine reasons. |
| WORK/QUARANTINE → PROCESSED | Check schema, contract, identity, candidate/site separation, evidence, policy, rights, cultural review, and transform prerequisites. |
| PROCESSED → CATALOG/TRIPLET | Check evidence/proof closure, safe graph projection, catalog metadata, source-role preservation, and sensitivity propagation. |
| CATALOG/TRIPLET → PUBLISHED | Check PolicyDecision, ReviewRecord, public-safe transform receipt, ReleaseManifest, correction path, rollback target, and no-leak result. |
| Post-release correction | Check supersession, withdrawal, cache/tile/index invalidation, correction lineage, and rollback completion. |

### Correction cascade

A material correction or revocation may require invalidating or rebuilding:

- catalog records;
- evidence bundles and claim envelopes;
- graph/triplet projections;
- public-safe geometry;
- tiles, PMTiles, COGs, search indexes, embeddings, screenshots, and exports;
- Evidence Drawer and Focus Mode caches;
- release manifests and public API payloads.

The validator may check that cascade references exist. It must not execute publication or deletion outside an authorized runbook.

[Back to top](#top)

---

<a id="tests-fixtures-and-no-network-posture"></a>

## Tests, fixtures, and no-network posture

### Current evidence

Archaeology test filenames exist for evidence closure, candidate-not-site, public no-leak, exact sensitive geometry, rights/cultural review, catalog closure, release manifests, AI exact-location denial, schema validation, temporal logic, no-network fixtures, source descriptors, and rollback drills. Sampled modules are placeholders, so filenames do not prove test coverage.

### Required fixture classes

| Fixture class | Minimum case |
|---|---|
| Valid public-safe | Synthetic generalized summary with evidence, review, transform receipt, release, correction, and rollback references. |
| Missing evidence | EvidenceRef absent or unresolved. |
| Candidate/site collapse | Candidate labeled or rendered as confirmed site. |
| Public exact geometry | Exact protected geometry requested for a public surface. |
| Reverse inference | Coarse payload plus context can narrow a protected location. |
| Rights/cultural gap | Rights, CARE, sovereignty, consent, review, embargo, or revocation incomplete. |
| Missing transform receipt | Generalized output lacks named profile or receipt. |
| Catalog/release gap | Proof, policy, release, correction, or rollback reference missing. |
| AI exact-location request | Direct and indirect location disclosure prompts. |
| Schema drift | Contract/schema pair mismatch or permissive scaffold used as active shape. |
| Policy parity | CI and runtime bundle digest mismatch. |
| Replay drift | Same inputs and pinned rules produce different report/hash. |
| Malicious input | Oversized, recursive, path-traversal, archive escape, injection text, malformed encoding, and parser-bomb cases. |

### Fixture safety

- Use synthetic or explicitly public-safe data only.
- Never copy protected coordinates into repository fixtures.
- Mark all examples as synthetic/test-only.
- Avoid real site identifiers that can be resolved externally.
- Keep invalid fixtures minimal and non-sensitive.
- Default tests to no network.
- Keep live-source probes manual, isolated, and non-publishing.

### Proposed commands after implementation exists

```bash
pytest -q tests/domains/archaeology
opa test policy/domains/archaeology policy/sensitivity/archaeology
python tools/validate_all.py --domain archaeology --fixtures --no-network
```

These commands are **PROPOSED**. The inspected orchestrator and tests do not currently establish that these commands perform substantive Archaeology validation.

[Back to top](#top)

---

<a id="ci-admission-contract"></a>

## CI admission contract

### Workflow-trigger threat preflight

The inspected `.github/workflows/domain-archaeology.yml`:

- triggers on every pull request and pushes to `main`;
- uses `actions/checkout@v7`;
- declares no explicit write permissions, secrets, environment, deployment, artifact upload, release, or publication step;
- runs three jobs that only echo TODO messages.

**Immediate threat posture:** no privileged mutation or publishing behavior was visible in this workflow.

**Validation value:** effectively none. Successful TODO jobs must not be interpreted as Archaeology validation, proof construction, or publish-dry-run success.

### Proposed CI gates

A substantive workflow should eventually:

1. validate modified Archaeology schemas against valid/invalid fixtures;
2. run OPA policy tests;
3. run the seven validator families over synthetic no-network packets;
4. assert candidate/site, no-leak, cultural-review, geometry, catalog, and AI-denial negative cases;
5. verify contract/schema/policy/fixture digests;
6. emit a deterministic `ValidationReport`;
7. fail when no tests are collected;
8. compare CI policy bundle digest with the runtime bundle digest;
9. run replay/golden-hash checks;
10. prohibit any workflow step that publishes, contacts restricted sources, or exposes secrets on untrusted pull requests;
11. require human sensitivity/cultural/release review before any promotion-bound status is accepted.

### Required-check caution

Branch protection, rulesets, required checks, fork behavior, environment approvals, and current workflow success were not inspected. Their status remains **NEEDS VERIFICATION**.

[Back to top](#top)

---

<a id="smallest-sound-implementation-sequence"></a>

## Smallest sound implementation sequence

Implement the lane in bounded, reversible pull requests.

### PR 1 — Authority and report contract

- settle the broad-versus-child executable topology;
- inventory and classify contract/schema aliases and duplicates;
- accept one `ValidationReport` contract/schema and reason-code registry;
- define safe report destination and generated receipt linkage;
- add no protected data.

### PR 2 — One proof-bearing validator

Implement `ARCH-V2 Candidate not site` first because:

- it is narrow and deterministic;
- a default-deny policy scaffold already exists;
- it exercises contract, schema, policy, fixtures, report emission, and negative outcomes;
- it prevents one of the highest-risk semantic collapses.

Required proof:

- substantive valid/invalid synthetic fixtures;
- policy rules beyond a bare default;
- executable validator;
- deterministic report;
- tests that fail before the implementation and pass after;
- no-network execution;
- reviewed owner and reason codes.

### PR 3 — Public no-leak and exact geometry

- implement `ARCH-V3` and `ARCH-V5`;
- include structured, narrative, tile/map, export, and AI-context leakage cases;
- bind named redaction profiles and receipts;
- obtain sensitivity and cultural-review approval.

### PR 4 — Evidence, rights/culture, catalog, and AI denial

- implement `ARCH-V1`, `ARCH-V4`, `ARCH-V6`, and `ARCH-V7`;
- prove EvidenceRef resolution, policy parity, release closure, correction, rollback, and indirect AI-location denial.

### PR 5 — Orchestration and CI

- implement one broad runner that delegates without duplicating child logic;
- replace TODO workflow steps;
- fail on zero tests;
- emit deterministic reports;
- prove CI/runtime policy parity;
- keep publishing disabled;
- document rollback and deprecation of any compatibility entrypoint.

No PR should combine schema-home migration, policy activation, validator implementation, runtime integration, and publication authority without an explicit change budget and ADR/migration review.

[Back to top](#top)

---

<a id="definition-of-done"></a>

## Definition of done

The broad Archaeology validator lane is not operationally complete until all applicable items pass.

### Authority and placement

- [ ] Broad and child validator responsibilities are accepted and non-duplicative.
- [ ] Owners and review roles are assigned.
- [ ] Contract and schema authority mappings are accepted.
- [ ] Compatibility aliases have migration/deprecation records.
- [ ] No parallel policy, registry, evidence, receipt, or release home is created.

### Implementation

- [ ] Seven canonical families have executable entrypoints or an explicit accepted subset.
- [ ] One deterministic broad runner delegates to child/shared validators.
- [ ] Stable reason codes and report schema are versioned.
- [ ] Contract, schema, policy, fixture, and dependency digests are recorded.
- [ ] Reports contain no protected data.

### Proof

- [ ] Valid and invalid synthetic fixtures exist for every active family.
- [ ] Default suite uses no network.
- [ ] Negative cases prove deny/abstain/review/error behavior.
- [ ] Zero collected tests fails CI.
- [ ] Replay produces the expected golden hash.
- [ ] CI and runtime policy bundle digests match.
- [ ] Workflow steps perform substantive validation rather than echo TODO.

### Governance

- [ ] Evidence, rights, sovereignty, cultural review, consent, revocation, embargo, sensitivity, and release obligations are enforced where applicable.
- [ ] Exact protected geometry and reverse inference are denied.
- [ ] Candidate/site separation is enforced across API, map, export, search, graph, and AI representations.
- [ ] Validator pass cannot publish or approve release.
- [ ] Correction, withdrawal, cache invalidation, and rollback references are tested.
- [ ] Sensitivity reviewer, cultural/rights-holder reviewer, policy steward, release steward, and security reviewer approve the applicable scope.

### Operations

- [ ] ValidationReports are discoverable and integrity-bound.
- [ ] Metrics distinguish pass, deny, abstain, review, error, and skipped checks.
- [ ] Alerting does not reveal protected information.
- [ ] Runbooks cover policy failure, false pass, false deny, data leak, correction, revocation, and rollback.
- [ ] Current implementation status is reflected in this README and domain docs.

[Back to top](#top)

---

<a id="migration-compatibility-and-deprecation"></a>

## Migration, compatibility, and deprecation

This v0.2 README supersedes v0.1 as documentation only. It does not migrate code.

### Compatibility rules

- Keep `tools/validators/archaeology/` as the broad boundary unless a reviewed ADR/migration changes it.
- Keep `tools/validators/domains/archaeology/` as a child index, not a competing broad implementation.
- Do not create a second broad executable under the child tree.
- Do not choose between contract, schema, source-registry, or catalog aliases inside validator code without an accepted mapping.
- Compatibility shims must be time-bounded, logged, tested, and documented.
- A deprecated entrypoint must identify its replacement and removal criteria.
- Report and reason-code compatibility must be versioned.

### Material-change rule

The following require reviewed migration or ADR consideration:

- changing the canonical validator entrypoint;
- collapsing or renaming the broad/child lanes;
- choosing or changing contract/schema authority;
- activating policy as a release gate;
- changing sensitive-location posture or redaction semantics;
- adding public/runtime use;
- changing report or receipt authority;
- adding automatic publication, deletion, or external source access.

[Back to top](#top)

---

<a id="open-verification-register"></a>

## Open verification register

| ID | Item | Status | Evidence needed |
|---|---|---|---|
| `ARCH-VAL-OPEN-001` | Named owner and CODEOWNERS coverage for this lane | NEEDS VERIFICATION | Accepted owner assignment and CODEOWNERS rule. |
| `ARCH-VAL-OPEN-002` | Canonical broad runner path and CLI | NEEDS VERIFICATION | Reviewed topology decision plus executable and tests. |
| `ARCH-VAL-OPEN-003` | Child validator inventory | NEEDS VERIFICATION | Recursive inventory and accepted child scopes. |
| `ARCH-VAL-OPEN-004` | Contract authority across duplicate/compatibility homes | CONFLICTED / NEEDS VERIFICATION | ADR/migration record and contract registry. |
| `ARCH-VAL-OPEN-005` | Schema authority and alias state | NEEDS VERIFICATION | Accepted schema-home decision, registry, and migration status. |
| `ARCH-VAL-OPEN-006` | Field completeness of Archaeology schemas | NEEDS VERIFICATION | Schema review plus valid/invalid fixtures and coverage report. |
| `ARCH-VAL-OPEN-007` | Policy bundle entrypoint and rule completeness | NEEDS VERIFICATION | Bundle manifest, substantive Rego, tests, and digest. |
| `ARCH-VAL-OPEN-008` | CI/runtime policy parity | UNKNOWN | CI report and runtime policy digest evidence. |
| `ARCH-VAL-OPEN-009` | Source registry canonical path and active source descriptors | CONFLICTED / NEEDS VERIFICATION | Registry ADR/migration plus active descriptor inventory. |
| `ARCH-VAL-OPEN-010` | Source rights and terms | NEEDS VERIFICATION | Current source descriptors, terms review, and rights decision. |
| `ARCH-VAL-OPEN-011` | EvidenceRef resolver and admissible EvidenceBundle profile | UNKNOWN | Resolver implementation, schema, tests, and runtime evidence. |
| `ARCH-VAL-OPEN-012` | Cultural-review and rights-holder workflow integration | UNKNOWN | Review records, role assignments, tests, and runbook execution. |
| `ARCH-VAL-OPEN-013` | Named redaction profiles and transform receipt enforcement | NEEDS VERIFICATION | Accepted profile registry, receipt schema, policy, fixtures, tests. |
| `ARCH-VAL-OPEN-014` | Meaningful test implementation | NEEDS VERIFICATION | Non-placeholder test bodies and test run evidence. |
| `ARCH-VAL-OPEN-015` | Meaningful fixture coverage | NEEDS VERIFICATION | Synthetic valid/invalid/public-safe fixture inventory and hashes. |
| `ARCH-VAL-OPEN-016` | Broad ValidationReport schema and destination | NEEDS VERIFICATION | Accepted contract/schema, report path, and sample receipt. |
| `ARCH-VAL-OPEN-017` | Stable reason-code registry | NEEDS VERIFICATION | Machine-readable registry and compatibility policy. |
| `ARCH-VAL-OPEN-018` | Functional global/domain orchestrator | UNKNOWN | Executable implementation and deterministic run report. |
| `ARCH-VAL-OPEN-019` | Substantive CI and required-check significance | UNKNOWN | Workflow run, branch/ruleset evidence, and failure demonstration. |
| `ARCH-VAL-OPEN-020` | Runtime consumers and invocation path | UNKNOWN | Code references, configuration, logs, and deployment evidence. |
| `ARCH-VAL-OPEN-021` | Correction/revocation cascade | UNKNOWN | Runbook test, affected-artifact graph, and rollback receipt. |
| `ARCH-VAL-OPEN-022` | Release-gate adoption | UNKNOWN | Promotion policy, workflow gate, PromotionDecision, and ReleaseManifest evidence. |
| `ARCH-VAL-OPEN-023` | Operational metrics and dashboards | UNKNOWN | Metric definitions, emitted telemetry, and dashboard evidence. |
| `ARCH-VAL-OPEN-024` | Current pass/fail state | NOT RUN / UNKNOWN | A governed validator execution after implementation. |

[Back to top](#top)

---

<a id="rollback-path"></a>

## Rollback path

### This documentation change

Before merge:

- close the draft pull request;
- abandon the scoped branch;
- no runtime, policy, source, data, release, or publication rollback is needed.

After merge:

- revert the README commit and paired generated provenance receipt through a reviewed branch; or
- restore prior README blob `ce0a80baa25538566fac39864c8f836505ce9aab` and remove/revert the paired generated receipt.

### Future validator implementation

A validator rollout must define:

- prior executable/version and policy bundle digest;
- feature flag or release-gate toggle;
- report-schema compatibility;
- handling of in-flight candidates;
- invalidation of false-pass reports;
- correction notices for affected releases;
- public cache/tile/search/graph/AI invalidation where material;
- rollback completion receipt;
- post-rollback review.

Rollback must never re-enable a less restrictive public path for protected Archaeology content.

[Back to top](#top)

---

<a id="evidence-ledger"></a>

## Evidence ledger

| Evidence | What it supports | What it does not prove |
|---|---|---|
| Target v0.1 README | Prior lane intent and safety posture | Executable behavior. |
| `tools/validators/README.md` | Validator-root authority and fail-closed boundary | Archaeology implementation. |
| Child Archaeology index | Broad-versus-child topology | Child executable inventory beyond inspected README. |
| `docs/domains/archaeology/VALIDATORS.md` | Seven canonical families, outcomes, receipts, replay, CI intent | Current code or CI enforcement. |
| `docs/domains/archaeology/SENSITIVITY.md` | T4/rank-5 default and transform/review posture | Active policy bundle or reviewed release. |
| Directory Rules | Correct responsibility roots and non-collapse | Current implementation completeness. |
| Schema-home ADR | Proposed canonical machine-shape placement | Accepted status or field completeness. |
| Sensitive-domain ADR | Fail-closed Archaeology policy rationale | Accepted ADR number or runtime enforcement. |
| Contract and schema inventory | Presence of many semantic and machine files | Acceptance, completeness, or parity. |
| Sampled schemas | Permissive/minimal scaffold evidence | Maturity of every schema in the family. |
| Policy inventory and sampled Rego | File presence and default-deny scaffold evidence | Complete rules, bundle wiring, or runtime parity. |
| Test inventory and sampled modules | Filename presence and placeholder evidence | Substantive test coverage. |
| `tools/validate_all.py` | Placeholder global orchestrator | Functional validator execution. |
| Domain workflow | Trigger shape and TODO-only jobs | Required-check status, branch protection, or substantive validation. |
| CODEOWNERS | Generic placeholder ownership | Valid teams or Archaeology-specific reviewers. |
| User-supplied v3.1 prompt | Task authority, implementation route, evidence and acceptance discipline | Repository facts. |

### Evidence precision note

Repository searches were bounded connector searches, not a full local clone or exhaustive tree traversal. Statements about absence use “not surfaced” or “not established,” not categorical nonexistence.

[Back to top](#top)

---

<a id="changelog"></a>

## Changelog

### v0.2 — 2026-07-16

- grounds the README in current repository evidence;
- records the broad-versus-child validator topology;
- replaces “all implementation is only proposed” with a mixed-maturity inventory;
- distinguishes present contracts/schemas/policies/tests from sampled scaffold quality;
- records placeholder orchestrator and TODO-only domain workflow;
- adds task contract, authority ladder, input packet, report contract, finite outcomes, stable reason-code families, security controls, no-network posture, CI threat preflight, implementation sequence, definition of done, migration rules, 24-item verification register, evidence ledger, and rollback;
- preserves exact-location denial, candidate-not-site, cultural review, public no-leak, catalog closure, and AI-location denial;
- creates no executable behavior and grants no publication, cultural, policy, evidence, or release authority.

### v0.1 — 2026-07-07

- replaced an empty file with a broad proposed Archaeology validator-lane README;
- named seven validator families and standard outcomes;
- documented fail-closed sensitivity posture and proposed tests.

---

## Maintainer summary

**CONFIRMED:** this is the broad Archaeology validator boundary, the child index is separate, and repository scaffolds now exist across contracts, schemas, policy, fixtures, tests, orchestration, and workflow.

**PROPOSED:** implement one narrow proof-bearing validator first, emit deterministic safe reports, then expand through reviewed, no-network, fail-closed slices.

**NEEDS VERIFICATION:** authority mappings, owners, substantive schemas/policy/tests, evidence resolution, cultural review, redaction profiles, CI/runtime parity, correction cascade, and release-gate integration.

**UNKNOWN:** production use, runtime invocation, emitted reports, operational metrics, deployment, and current pass state.

[Back to top](#top)
