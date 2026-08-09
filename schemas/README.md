# schemas

> **One-line purpose.** `schemas/` owns KFM's machine-checkable object shapes. It constrains payload structure without becoming semantic meaning, evidence, policy, source authority, lifecycle state, release approval, or public truth.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-readme
title: schemas/ — Canonical Machine-Shape Root and Compatibility Boundary
type: README
version: v0.6
status: draft; repository-grounded; canonical-machine-shape-root; adopted-directory-rules-aligned; registry-driven-validation-surface; compatibility-debt-visible; non-semantic; non-policy; non-release
owner: NEEDS VERIFICATION — explicit CODEOWNERS routing is @bartytime4life; no independently verified schema-steward assignment, required-review enforcement, or separation-of-duties control was established
created: NEEDS VERIFICATION — a short root stub existed before v0.2
updated: 2026-08-09
supersedes: v0.5 schema-root boundary and aggregate-runner guide
policy_label: repository-facing; schemas; json-schema; machine-shape; no-parallel-authority; fail-closed; correction-aware; rollback-aware
current_path: schemas/README.md
owning_root: schemas/
responsibility: own machine-checkable shape, identity constraints, reference structure, and schema-family navigation while preserving the contract/schema/policy/evidence/release split
truth_posture: cite-or-abstain; schema validity proves only the tested machine shape and never proves semantic truth, evidence closure, source authority, rights, sensitivity, policy approval, release state, or publication safety
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 3a9715582adf17a682920ca98f15aa3582ee8cdc
  target_prior_blob: 7e29afc982af13b3dea313bb524664b520b07beb
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption_adr: docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  schema_home_adr_blob: 3c520ea8f2f8bcb3d478329a87d98b135ea335fd
  contract_schema_split_adr_blob: 2da10fcf5836a44d46186c233b6b9664c9ccfda5
  contracts_v1_readme_blob: bbe931c9f7a5f0132522c0bda4fa5455c050a973
  validator_registry_blob: 12517f368cb1c8b850d3a7138a968cee889875ba
  validator_orchestrator_blob: 728cf1404839a5b95e03d70d44567863a6f9b6df
  validator_entrypoint_blob: c308015da780d7b72f56277b521fb0e42317651e
  compatibility_runner_blob: c3a87b45bb199d9d2bc07715d7432ec5cc9d6369
  schema_validation_workflow_blob: 3deebb4fa1e5db00108e0b43804ac633083d94c2
  validator_suite_workflow_blob: b028ae1bd92f4c708d2b27bb15d88d1ab85657e7
  makefile_blob: 4abc7f941ce25d7d14703e87e387cef6e96d1592
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
related:
  - ./contracts/v1/README.md
  - ./atmosphere/README.md
  - ./biotopes/README.md
  - ./policy/README.md
  - ./tests/README.md
  - ./evidence/README.md
  - ./governance/README.md
  - ./maplibre/README.md
  - ./people-dna-land/README.md
  - ../contracts/README.md
  - ../fixtures/README.md
  - ../tests/README.md
  - ../tests/schemas/README.md
  - ../tools/validate_all.py
  - ../tools/validators/README.md
  - ../tools/validators/validator_registry.json
  - ../tools/validators/validate_all.py
  - ../tools/validators/_common/README.md
  - ../tools/validators/_common/jsonschema_runner.py
  - ../tools/validators/_common/run_all.py
  - ../tests/validators/test_jsonschema_runner.py
  - ../.github/workflows/schema-validation.yml
  - ../.github/workflows/validator-suite.yml
  - ../docs/adr/INDEX.md
  - ../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - ../docs/adr/ADR-0002-contracts-vs-schemas-split.md
  - ../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../docs/doctrine/directory-rules.md
  - ../docs/registers/DRIFT_REGISTER.md
  - ../data/receipts/generated/README.md
notes:
  - "v0.6 reconciles the schema root with the registry-driven validator orchestrator, eight-validator full profile, changed-area and release-dry-run profiles, and current workflow definitions."
  - "The first twelve H2 sections preserve the adopted Directory Rules folder-README contract and the stable anchors used by v0.5."
  - "ADR-0029 accepts the exact Directory Rules v2 bytes at docs/doctrine/directory-rules.md; the embedded pre-adoption status string remains part of those pinned bytes."
  - "schemas/contracts/v1 is the current configured v1 validation surface, while ADR-0001 remains proposed and ADR-0002 remains effectively proposed."
  - "Root-level atmosphere, biotopes, evidence, governance, maplibre, and people-dna-land lanes are compatibility or migration surfaces, not silently promoted parallel authority."
  - "tools/validate_all.py is the canonical operator entrypoint; tools/validators/_common/run_all.py is a compatibility entrypoint used by make schemas."
  - "This change updates documentation only; it changes no schema, semantic contract, fixture payload, validator, workflow, policy, lifecycle object, release state, deployment, or public surface."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#status)
[![Authority: machine shape](https://img.shields.io/badge/authority-machine%20shape-1f6feb?style=flat-square)](#authority-level)
[![Dialect: JSON Schema 2020-12](https://img.shields.io/badge/JSON%20Schema-2020--12-8250df?style=flat-square)](#authoring-and-identity-contract)
[![Full-profile validators: 8](https://img.shields.io/badge/full%20profile-8%20validators-2da44e?style=flat-square)](#configured-validator-surface)
[![Profiles: 4](https://img.shields.io/badge/orchestrator%20profiles-4-0969da?style=flat-square)](#configured-validator-surface)
[![Publisher: no](https://img.shields.io/badge/publisher-no-6e7781?style=flat-square)](#authority-level)

**Quick navigation:** [Purpose](#purpose) · [Authority boundary](#authority-boundary) · [Status](#status) · [Belongs](#what-belongs-here) · [Does not belong](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related roots](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed) · [Topology](#current-child-lanes) · [Authoring](#authoring-rules) · [Aliases](#domain-alias-schemas) · [Strictness](#strictness) · [`$id`](#id-guidance) · [Validator profiles](#configured-validator-surface) · [Versioning](#versioning) · [Planning](#change-planning) · [Open verification](#open-questions)

> [!IMPORTANT]
> **Schema validity is necessary but never sufficient.** A schema-valid object may still be semantically wrong, unsupported by evidence, stale, source-role-confused, rights-uncleared, sensitivity-restricted, policy-denied, unreleased, or unsafe for public use.

> [!CAUTION]
> **Placement authority and schema-home status are different.** Accepted ADR-0029 makes the exact Directory Rules v2 bytes at `docs/doctrine/directory-rules.md` the adopted placement authority. `schemas/` is therefore the machine-shape responsibility root. The narrower proposal to treat `schemas/contracts/v1/` as the single default contract-backed schema home remains ADR-0001 `proposed`; ADR-0002's split remains effectively `proposed` even though current repository guidance already follows it in part.

> [!WARNING]
> **Compatibility paths must not evolve independently.** Root-level lanes such as `schemas/atmosphere/`, `schemas/biotopes/`, `schemas/evidence/`, `schemas/governance/`, `schemas/maplibre/`, and `schemas/people-dna-land/` are compatibility, migration, or transitional surfaces. New canonical fields belong in the reviewed versioned family selected by current authority and object ownership; a compatibility README or filename never creates a second schema authority.

---

## Purpose

`schemas/` is KFM's responsibility root for **machine-checkable shape**.

It owns JSON Schema documents, schema-family indexes, stable schema identifiers, structural reference rules, and shape-level compatibility guidance. A schema can require fields, constrain enums and primitive values, compose definitions, and reject structurally invalid payloads. It cannot decide what an object means, whether a claim is true, whether evidence is admissible, whether a source is authoritative, whether rights permit use, whether a location is too sensitive, or whether an object is released.

The governing split is:

```text
contracts/  -> semantic meaning and claim limits
schemas/    -> machine-checkable shape
policy/     -> allow / deny / restrict / hold / abstain decisions
fixtures/   -> representative valid, invalid, edge, and golden examples
tests/      -> executable enforceability proof
tools/      -> validator implementation and orchestration
data/       -> lifecycle material, receipts, proofs, catalogs, and published artifacts
release/    -> promotion, release, correction, withdrawal, and rollback decisions
```

A schema participates in the trust membrane only when it remains paired with those other authorities rather than pretending to replace them.

[Back to top](#top)

---

<a id="authority-boundary"></a>

## Authority level

**Canonical responsibility root for machine shape; non-semantic, non-policy, non-evidence, non-release authority.**

| Concern | Owning authority | `schemas/` role |
|---|---|---|
| Object-family meaning | [`contracts/`](../contracts/) | Constrains the machine representation of contract-backed objects; does not redefine meaning. |
| JSON shape and reference structure | `schemas/` | Owns schema documents, `$id`, `$ref`, composition, required fields, enums, and basic value constraints. |
| Policy, rights, sensitivity, consent, access | `policy/` plus governed review | Exposes fields policy can evaluate; does not make the decision. |
| Source identity and activation | governed source registry and source policy | May shape `SourceDescriptor`; cannot activate or rank a source. |
| Evidence support | EvidenceRef/EvidenceBundle authorities | May shape evidence objects; cannot establish evidence closure or claim truth. |
| Examples | [`fixtures/`](../fixtures/) | Schemas consume examples; example presence does not grant authority. |
| Executable proof | [`tests/`](../tests/) | Tests prove selected behavior; schema text alone is not an observed run. |
| Validator implementation | [`tools/validators/`](../tools/validators/) | Validators execute schemas; validator code does not own schema meaning. |
| Validator selection | [`validator_registry.json`](../tools/validators/validator_registry.json) | Selects repository validators and profiles; it is not a schema registry or adoption record. |
| Lifecycle state | governed `data/` phases | May shape lifecycle records; cannot promote them. |
| Receipts and proofs | `data/receipts/`, `data/proofs/` | May shape records; a receipt- or proof-shaped JSON file is not automatically governed. |
| Release, correction, withdrawal, rollback | [`release/`](../release/) | May shape release objects; cannot approve, publish, correct, or roll back. |
| API/UI/MapLibre behavior | accepted app/package/runtime roots | May shape payload envelopes; cannot authorize public routes or rendered state. |

### Anti-collapse rules

`schemas/` must not collapse:

- structure into semantics;
- schema success into claim truth;
- a permissive placeholder into implementation maturity;
- a JSON filename into governed object identity;
- `$id` uniqueness into a complete schema registry;
- the validator registry into a schema registry;
- fixture polarity into policy approval;
- validator execution into release approval;
- a compatibility wrapper into parallel canonical authority;
- a schema change into an implicit backward-compatibility promise;
- a passing workflow into public safety or KFM publication.

Public clients use governed APIs and released artifacts. They do not treat schemas or raw schema instances as public truth sources.

[Back to top](#top)

---

<a id="repo-fit"></a>
<a id="status"></a>

## Status

### Repository-grounded status matrix

| Surface | Current evidence at the pinned snapshot | Safe conclusion |
|---|---:|---|
| `schemas/README.md` | **CONFIRMED v0.5 baseline** | Stable path, H1, document ID, purpose, anchors, no-loss ledger, and compatibility warnings are preserved in v0.6. |
| Accepted Directory Rules | **CONFIRMED through ADR-0029** | The exact v2 bytes at `docs/doctrine/directory-rules.md` are adopted despite their retained pre-adoption label. Placement remains responsibility-rooted and no-parallel-authority. |
| `schemas/contracts/v1/` | **CONFIRMED configured v1 validation surface** | Current schema CI meta-validates the tree, requires Draft 2020-12 and unique canonical `$id` values, and wires eight fixture-backed validators through the full profile. This does not accept ADR-0001. |
| ADR-0001 | **CONFIRMED present; status `proposed`** | `schemas/contracts/v1/` is current configured direction, not an accepted subroot decision. |
| ADR-0002 | **CONFIRMED present; effective status `proposed`** | Current roots partially implement the split, but the decision is not accepted by documentation alone. |
| `tools/validate_all.py` | **CONFIRMED canonical thin entrypoint** | Delegates to the registry-driven orchestrator; it does not own validator semantics or release authority. |
| `tools/validators/validator_registry.json` | **CONFIRMED bounded validator registry** | Registers eight validators and four profiles. It does not enumerate every schema or prove complete validation coverage. |
| `tools/validators/validate_all.py` | **CONFIRMED deterministic orchestrator** | Validates registry safety, selects validators, runs all selected entries, and emits a deterministic JSON result unless timing is requested. |
| `tools/validators/_common/run_all.py` | **CONFIRMED compatibility entrypoint** | Exports the historical `RUNNER_VALIDATORS` surface and delegates `make schemas` to the full orchestrator profile. |
| `schemas/atmosphere/` | **CONFIRMED compatibility/migration index** | New schemas are frozen there; Air/Atmosphere path, filename, `$id`, and ownership drift remain unresolved. |
| `schemas/biotopes/` | **CONFIRMED compatibility/vocabulary index** | `Biotope` is not accepted as a new object family; migration must route artifacts object by object. |
| `schemas/policy/` | **CONFIRMED compatibility/documentation lane** | It does not establish executable policy or a second policy authority. |
| `schemas/tests/` | **CONFIRMED compatibility/documentation lane** | Executable tests run from accepted test roots, currently including `tests/schemas/` and `tests/contracts/`. |
| `schemas/evidence/` | **CONFIRMED transitional compatibility lane** | Root-level evidence schemas remain migration debt; compatibility files must not evolve independently. |
| `schemas/governance/` | **CONFIRMED transitional compatibility lane** | Permissive or compatibility shapes do not prove accepted governance contracts. |
| `schemas/maplibre/` | **CONFIRMED transitional compatibility lane** | Permissive placeholders remain readiness-held; path presence is not renderer or release proof. |
| `schemas/people-dna-land/` | **CONFIRMED transitional sensitive-domain lane** | Migration requires privacy, policy, domain, and public-safe denial review. |
| `schema-validation` workflow | **CONFIRMED command-bearing definition** | Checks all schema JSON, canonical v1 identity, eight configured fixture families, aggregate validators, and schema/contract tests. |
| `validator-suite` workflow | **CONFIRMED command-bearing definition** | Tests shared-runner semantics, generated-receipt validation, MaterialChangeAssessment, aggregate validation, and one reviewed EvidenceBundle rejection canary. |
| Current PR-run results | **NEEDS VERIFICATION per revision** | Workflow definitions are not proof that this branch passed. |
| Complete recursive schema inventory | **UNKNOWN in this README update** | The topology below is a bounded direct-child view, not a complete schema census. |
| Authoritative schema registry | **NOT ESTABLISHED** | The validator registry exists, but no accepted complete schema registry/generator and ownership model was verified. |
| Ownership and required review | **NEEDS VERIFICATION** | CODEOWNERS routes `/schemas/` to `@bartytime4life`; stewardship, ruleset enforcement, and independent approval remain separate controls. |

### Truth labels used here

| Label | Meaning |
|---|---|
| `CONFIRMED` | Verified from pinned repository content, workflow definitions, tests, logs, or generated artifacts inspected for this update. |
| `PROPOSED` | Design, future state, migration target, or recommendation not established as current implementation. |
| `UNKNOWN` | Evidence is insufficient to support a stronger statement. |
| `NEEDS VERIFICATION` | A concrete check is available but not closed strongly enough to act as fact. |
| `CONFLICTED` | Relevant implementation and doctrine, or two authority surfaces, disagree. |

[Back to top](#top)

---

<a id="what-belongs-here"></a>

## What belongs here

- This root README and schema-family indexes.
- JSON Schema documents for KFM object families.
- Versioned machine-shape families under the reviewed v1 tree.
- Stable `$id` values and local `$ref` composition.
- Shape-level compatibility aliases that are explicitly frozen, transitional, deprecated, or mirrored.
- Schema migration notes, compatibility maps, and deprecation guidance.
- Schema-local examples in prose when they are documentation, not competing fixture authority.
- Links to paired contracts, fixtures, validators, tests, policy, source registry, receipts, proofs, and release objects.
- Schema-specific limitations, strictness guidance, known permissive placeholders, and correction instructions.
- Machine-readable constraints that can be tested without embedding business approval or release decisions.

Every consequential schema should identify or make discoverable:

- its semantic contract;
- schema dialect;
- stable `$id`;
- version and compatibility posture;
- local references;
- valid and invalid fixture roots;
- validator and test surfaces;
- policy-sensitive fields;
- owning object family;
- change and rollback implications.

[Back to top](#top)

---

<a id="what-does-not-belong-here"></a>

## What does NOT belong here

| Do not place or authorize here | Owning root or action |
|---|---|
| Semantic contract prose and claim limits | [`contracts/`](../contracts/) |
| Policy rules, access grants, rights decisions, sensitivity decisions, consent, redaction approval | `policy/` and governed review |
| Fixture authority, golden payloads, negative examples | [`fixtures/`](../fixtures/) unless an accepted migration says otherwise |
| Validator code, generators, registry builders | [`tools/`](../tools/) |
| Test cases and assertions | [`tests/`](../tests/) |
| Source records, source activation, source rankings | governed source registry and policy roots |
| RAW, WORK, QUARANTINE, PROCESSED, CATALOG, TRIPLET, or PUBLISHED payloads | governed `data/` lifecycle roots |
| Canonical receipts, proofs, catalogs, or lifecycle records | their accepted `data/` lanes |
| Promotion decisions, release manifests, corrections, withdrawals, rollback cards, signatures | [`release/`](../release/) |
| Runtime, API, package, UI, MapLibre, or model implementation | owning app, package, runtime, or tool root |
| Public tiles, screenshots, dashboards, model output, generated summaries | governed delivery/publication roots after release checks |
| Secrets, credentials, private endpoints, protected payloads | approved external secret system or restricted data lane |
| A second canonical schema tree or independently evolving mirror | migrate, freeze, deprecate, or obtain accepted authority |
| Claims that a schema-valid object is true, cited, rights-cleared, public-safe, released, or implemented | evidence, policy, review, runtime, and release authorities |

[Back to top](#top)

---

<a id="inputs"></a>

## Inputs

Schemas may be authored or revised from:

- accepted or proposed semantic contracts, clearly labeled by status;
- object-family definitions and field semantics;
- public API or runtime envelope requirements;
- source descriptor and evidence object requirements;
- policy input/output field needs without embedding policy decisions;
- existing compatibility schemas and migration maps;
- valid, invalid, edge, and golden fixture requirements;
- validator and test failures;
- observed consumer compatibility requirements;
- accepted external standards or profiles where KFM adoption is documented;
- correction notices, drift entries, and accepted ADRs.

### Required input controls

Before changing a consequential schema:

1. pin the target schema and paired contract;
2. identify local `$ref` dependencies and known consumers;
3. inspect valid and invalid fixtures;
4. inspect validator and test coverage;
5. identify compatibility aliases and generated mirrors;
6. classify the change as additive, narrowing, widening, semantic, or identity-affecting;
7. identify policy- and sensitivity-significant fields;
8. determine whether a version bump or migration is required;
9. preserve a rollback target;
10. avoid changing a compatibility copy independently of its canonical source.

A missing contract, consumer inventory, fixture family, or rollback path is a visible `NEEDS VERIFICATION` condition—not permission to guess.

[Back to top](#top)

---

<a id="outputs"></a>

## Outputs

A schema change may produce:

| Output | Authority limit |
|---|---|
| JSON Schema document | Machine-shape definition only. |
| Schema-family README update | Human navigation and claim limits only. |
| Valid/invalid fixture changes | Representative examples; not truth or release evidence. |
| Validator/test changes | Executable checks; not policy or release approval. |
| Compatibility alias or deprecation map | Transition support; not a second authority. |
| Migration note | Planned or executed compatibility transition; must preserve lineage. |
| Validation logs | Run evidence for selected checks; not a governed ValidationReport unless emitted under an accepted contract. |
| Orchestrator JSON report | Deterministic execution summary; not EvidenceBundle closure, review, release, or publication authority. |
| Generated schema inventory | Discoverability aid; not authoritative unless its generator, source, ownership, and review state are accepted. |
| Generated receipt for an AI-authored change | Process provenance; not human approval, schema proof, or publication authority. |

### Schema change outcomes

Use explicit outcomes for review:

| Outcome | Meaning |
|---|---|
| `NO_CHANGE` | Current shape and documentation already satisfy the scoped requirement. |
| `ADDITIVE` | Optional or backward-compatible shape is added, subject to consumer verification. |
| `BREAKING` | Existing valid instances or consumers may fail; version/migration/review required. |
| `HELD` | Contract, fixtures, consumers, policy, or ownership are unresolved. |
| `DENIED` | Change would create parallel authority, weaken fail-closed behavior, or expose unsafe shape. |
| `ERROR` | Validation or migration execution failed. |

These are review outcomes for schema work, not universal runtime or policy enums.

[Back to top](#top)

---

<a id="testing"></a>
<a id="validation"></a>

## Validation

### Canonical orchestrator commands

Install only the repository-declared test dependencies in an isolated environment when needed:

```bash
python -m pip install -e ".[test]"
```

Inspect and validate the registry before relying on a profile:

```bash
python tools/validate_all.py --validate-registry
python tools/validate_all.py --list
```

Run a bounded profile:

```bash
python tools/validate_all.py --profile focused
python tools/validate_all.py --profile release-dry-run
python tools/validate_all.py --profile full
```

Run changed-area selection with one or more repository-relative paths:

```bash
python tools/validate_all.py \
  --profile changed-area \
  --changed-path schemas/contracts/v1/evidence/evidence_bundle.schema.json
```

A changed-area request with no matching path glob returns `ABSTAIN` / `NO_MATCHING_VALIDATORS` with exit `0`. That is an explicit no-selection result, not validation of the changed file.

The historical and Make-compatible route remains:

```bash
make schemas
make test
make validate
```

### Command scope

| Command | Confirmed behavior | Claim limit |
|---|---|---|
| `python tools/validate_all.py --validate-registry` | Validates registry structure, profiles, IDs, paths, scripts, limits, and full-profile closure. | Registry configuration only. |
| `python tools/validate_all.py --list` | Prints registry identity, digest, profiles, and validator IDs. | Inventory snapshot only. |
| `--profile focused` | Runs SourceDescriptor, EvidenceRef, EvidenceBundle, and RuntimeResponseEnvelope validators. | Focused bounded surface. |
| `--profile changed-area` | Selects validators whose registered path globs match supplied changed paths. | Coverage depends on maintained globs; no match is `ABSTAIN`. |
| `--profile release-dry-run` | Runs EvidenceBundle, LayerManifest, DecisionEnvelope, RunReceipt, and IngestReceipt validators. | Fixture validation only; not a release dry run, release decision, or publication. |
| `--profile full` | Runs all eight registered validators and aggregates every selected result. | Registered surface only; not complete schema-tree coverage. |
| `make schemas` | Runs `python tools/validators/_common/run_all.py`, which delegates to the full orchestrator profile. | Compatibility command; same bounded registered surface. |
| `make test` | Runs `python -m pytest tests/schemas tests/contracts -q`. | Collected schema/contract tests only. |
| `make validate` | Runs `make schemas` and `make test`. | Not a full repository, policy, release, or publication gate. |

### Orchestrator outcomes and exit semantics

The orchestrator runs every selected validator instead of stopping after the first rejection. It reports validator-level status and a top-level outcome with this precedence:

| Exit | Top-level outcome | Meaning |
|---:|---|---|
| `0` | `PASS` | Every selected validator returned its success code. |
| `0` | `ABSTAIN` | Changed-area selection matched no registered validator. |
| `1` | `FAIL` | One or more validators rejected their inputs. |
| `2` | `ERROR` | Registry, I/O, timeout, or validator execution produced an orchestrator error. |

Default reports omit timing so identical selected outputs can produce identical JSON bytes. `--include-timing` deliberately adds nondeterministic duration fields. The report records hashes and line counts of captured output rather than turning console text into authority.

### Shared JSON Schema runner semantics

> [!NOTE]
> The shared JSON Schema runner prints `EXPECTED_FAIL` only when a well-formed declared-invalid fixture is schema-invalid as required. `FAIL` means an empty lane, malformed fixture, validator exception, or polarity error. Specialized validators may use their own bounded diagnostics. `EXPECTED_FAIL`, `PASS`, `FAIL`, `ABSTAIN`, or `ERROR` console/report tokens are not policy decisions, ValidationReports, release results, or publication decisions.

| Exit | Shared runner meaning |
|---:|---|
| `0` | Every explicit file validated, or both fixture lanes were nonempty and every fixture satisfied its declared polarity. |
| `1` | An explicit file failed, a lane was empty, polarity was wrong, or parsing/validation raised. |
| `2` | Neither explicit files nor `--fixtures` was supplied. |

### Workflow coverage

[`schema-validation.yml`](../.github/workflows/schema-validation.yml) currently:

1. installs the declared test dependencies on Python 3.11;
2. requires the compatibility inventory to match eight configured schema/fixture families;
3. requires nonempty valid and invalid fixture lanes;
4. requires reviewed rejection evidence—per-fixture `.expected_error.txt` sidecars or the LayerManifest expectation manifest;
5. parses every JSON file under `schemas/`;
6. meta-validates every `*.schema.json` with Draft 2020-12;
7. requires every `schemas/contracts/v1/**/*.schema.json` file to declare Draft 2020-12;
8. requires canonical v1 schemas to have unique `$id` values;
9. runs `make schemas`;
10. runs `python -m pytest -q tests/schemas tests/contracts`;
11. records only logs and a step summary.

[`validator-suite.yml`](../.github/workflows/validator-suite.yml) separately exercises shared-runner tests, generated-receipt validation, MaterialChangeAssessment, the aggregate full profile, and a reviewed invalid EvidenceBundle canary that must fail for missing `bundle_id` rather than for an arbitrary command error.

Neither workflow emits or authorizes a governed ValidationReport, receipt, proof, policy decision, lifecycle record, release record, deployment, or publication.

### Documentation-only validation for this README

```bash
git diff -- schemas/README.md
git diff --check
```

Also verify one H1, heading order, explicit anchors, internal fragment targets, fenced-block closure, table delimiter shape, final newline, and base-to-head changed paths. Repository-native hosted CI remains the source for branch-current execution results.

[Back to top](#top)

---

<a id="review-burden"></a>

## Review burden

### Baseline review

README-only reconciliation requires:

- schema-root maintainer review;
- complete-diff and no-loss review;
- link, anchor, and GFM checks;
- verification that no machine file or authority decision changed;
- confirmation that current commands and status claims match the pinned repository.

### Schema-family review

A schema change requires review by the affected schema and contract owners, plus the owners of touched fixtures, validators, tests, and known consumers.

### Elevated review

Additional policy, security, sensitivity, domain, release, or API/UI review is required when a schema affects:

- evidence resolution or citation;
- source activation or provenance;
- rights, consent, access, or sensitivity;
- living-person, DNA/genomic, archaeology, rare-species, infrastructure, or precise-location data;
- runtime answer envelopes;
- public API or map payloads;
- promotion, release, correction, withdrawal, or rollback;
- signatures, receipts, proofs, or catalog closure;
- compatibility aliases used by external consumers;
- identity, hashing, or deterministic replay.

### CODEOWNERS boundary

`.github/CODEOWNERS` routes `/schemas/` to `@bartytime4life`. That is a GitHub review-routing fact only. It is not a StewardshipAssignment, completed ReviewRecord, ruleset requirement, independent approval, schema acceptance, release approval, or KFM publication.

### Separation of duties

Where maturity and consequence justify it, the same actor should not silently:

1. redefine semantic meaning;
2. change machine shape;
3. update fixtures and expected errors;
4. alter the validator or registry selection;
5. approve the policy consequence;
6. approve release.

Any temporary consolidation of duties must be explicit, reviewed, bounded, and reversible.

[Back to top](#top)

---

<a id="related-folders"></a>

## Related folders

| Path | Relationship |
|---|---|
| [`schemas/contracts/v1/`](./contracts/v1/) | Current configured v1 machine-schema surface and proposed default contract-backed family. |
| [`schemas/atmosphere/`](./atmosphere/) | Frozen compatibility/migration index; Air/Atmosphere authority and identity drift remain unresolved. |
| [`schemas/biotopes/`](./biotopes/) | Frozen vocabulary and object-split compatibility index; not a `Biotope` object-family authority. |
| [`schemas/policy/`](./policy/) | Policy-schema compatibility/documentation lane; not executable policy authority. |
| [`schemas/tests/`](./tests/) | Compatibility placement index; executable schema tests are elsewhere. |
| [`schemas/evidence/`](./evidence/) | Transitional evidence-schema compatibility lane. |
| [`schemas/governance/`](./governance/) | Transitional governance-schema compatibility lane. |
| [`schemas/maplibre/`](./maplibre/) | Transitional MapLibre schema lane and readiness-held placeholders. |
| [`schemas/people-dna-land/`](./people-dna-land/) | Sensitive-domain compatibility lane requiring migration and policy review. |
| [`contracts/`](../contracts/) | Semantic meaning and claim limits. |
| [`fixtures/`](../fixtures/) | Valid, invalid, negative, edge, and golden examples. |
| [`tests/`](../tests/) | Executable test authority. |
| [`tests/schemas/`](../tests/schemas/) | Schema test index and executable schema tests. |
| [`tools/validate_all.py`](../tools/validate_all.py) | Canonical thin validator-orchestrator entrypoint. |
| [`tools/validators/validator_registry.json`](../tools/validators/validator_registry.json) | Bounded validator/profile selection registry; not a schema registry. |
| [`tools/validators/validate_all.py`](../tools/validators/validate_all.py) | Deterministic orchestrator implementation. |
| [`tools/validators/_common/run_all.py`](../tools/validators/_common/run_all.py) | Historical compatibility entrypoint used by `make schemas`. |
| [`data/receipts/generated/`](../data/receipts/generated/) | Generated provenance records for AI-authored changes when repository doctrine requires them. |
| [`release/`](../release/) | Promotion, release, correction, withdrawal, and rollback authority. |
| [Schema validation workflow](../.github/workflows/schema-validation.yml) | Canonical v1 identity, fixture, aggregate, and schema/contract test checks. |
| [Validator suite workflow](../.github/workflows/validator-suite.yml) | Focused harness, generated-receipt, material-change, aggregate, and canary checks. |
| [Directory Rules](../docs/doctrine/directory-rules.md) | Adopted responsibility-root, compatibility, migration, and README doctrine through ADR-0029. |
| [ADR index](../docs/adr/INDEX.md) | Current decision inventory and effective status. |
| [Drift register](../docs/registers/DRIFT_REGISTER.md) | Repository drift disclosures; schema migration coverage remains incomplete. |

[Back to top](#top)

---

<a id="adrs"></a>

## ADRs

### Current schema and placement decisions

| Decision | Current status | Consequence for this README |
|---|---:|---|
| [ADR-0029 — adopt Directory Governance Standard v2](../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | `accepted` | The exact Directory Rules v2 bytes govern placement and make `schemas/` the machine-shape responsibility root. |
| [ADR-0001 — `schemas/contracts/v1` is canonical](../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) | `proposed` | Use as proposed direction and current configured path, not as accepted subroot authority. |
| [ADR-0002 — contracts versus schemas split](../docs/adr/ADR-0002-contracts-vs-schemas-split.md) | effective status `proposed` | Preserve the observed split while avoiding any claim that this README accepts the ADR. |

### Decisions still needed

- Accept, revise, supersede, or reject ADR-0001.
- Accept, revise, supersede, or reject ADR-0002.
- Decide the authoritative schema registry, generator, ownership, and correction policy.
- Classify every root-level compatibility lane and define migration, freeze, or retirement.
- Define version-bump and compatibility policy by change class.
- Define cross-schema reference and cycle rules.
- Define externally consumed schema support and deprecation windows.
- Define generated schema-inventory and release binding.
- Define schema steward and independent-review requirements.
- Decide how hardcoded CI fixture-family maps remain synchronized with the validator registry without creating two authorities.

This README implements no ADR, schema migration, or authority transition.

[Back to top](#top)

---

<a id="last-reviewed"></a>

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-08-09 |
| Evidence base | `main@3a9715582adf17a682920ca98f15aa3582ee8cdc` |
| Prior README blob | `7e29afc982af13b3dea313bb524664b520b07beb` |
| Review mode | Complete-file, same-path validator-orchestrator, workflow, Directory Rules, and direct-child reconciliation |
| Change class | Documentation-only semantic correction and additive navigation; no authority change |
| Implementation effect | None; registry/orchestrator/workflow behavior already existed at the pinned base |
| Runtime/release effect | None |
| Human review | Pending |
| Rollback | Close the draft PR before merge, or revert the README-only commit and restore the prior blob after merge |

Re-review this README when:

- validator registry entries or profiles change;
- orchestrator exit/report semantics change;
- `make schemas` stops using the compatibility entrypoint;
- canonical v1 `$id` policy changes;
- ADR-0001 or ADR-0002 changes status;
- a compatibility schema lane is added, migrated, frozen, or removed;
- an authoritative schema registry appears;
- fixture expectation conventions change;
- the local reference resolver changes;
- `schema-validation` or `validator-suite` changes scope;
- a schema becomes externally published or version-supported;
- a policy-sensitive object family changes;
- CODEOWNERS, rulesets, or stewardship changes;
- adopted Directory Rules changes schema placement or README requirements.

[Back to top](#top)

---

<a id="current-child-lanes"></a>

## Repository topology and compatibility lanes

### Bounded inspected topology

```text
schemas/
├── README.md
├── atmosphere/                  # compatibility, drift, and migration index
├── biotopes/                    # compatibility vocabulary/object-split index
├── contracts/
│   └── v1/                      # current configured v1 machine-schema tree
├── evidence/                    # transitional compatibility lane
├── governance/                  # transitional compatibility lane
├── maplibre/                    # transitional compatibility + permissive placeholders
├── people-dna-land/             # sensitive-domain transitional compatibility
├── policy/                      # compatibility/documentation lane
└── tests/                       # compatibility/documentation lane
```

This is a **bounded direct-child view**, not a complete recursive inventory or claim that every child is equally mature.

### Lane classification

| Lane | Classification | Write posture |
|---|---|---|
| `contracts/v1/` | Current configured versioned schema tree; proposed default contract-backed home | New reviewed canonical schema work generally lands here under current configuration unless accepted authority or a governed migration says otherwise. |
| `atmosphere/` | Compatibility/migration index | Freeze new schemas; inventory and resolve Air/Atmosphere path, name, `$id`, contract, fixture, validator, and consumer drift first. |
| `biotopes/` | Compatibility vocabulary/object-split index | Freeze new schemas; route any artifact to its actual Habitat, land-cover, ecoregion, ecological-system, or Flora object family. |
| `policy/` | Compatibility/documentation | Do not add executable policy or independently evolve duplicate schema authority. |
| `tests/` | Compatibility/documentation | Do not move executable tests here without an accepted ownership/migration decision. |
| `evidence/` | Transitional compatibility | Migrate or freeze against versioned evidence families; do not add divergent fields. |
| `governance/` | Transitional compatibility | Treat permissive shapes as incomplete; do not infer governance maturity. |
| `maplibre/` | Transitional compatibility | Treat accept-any-object schemas as readiness-held placeholders. |
| `people-dna-land/` | Transitional compatibility / sensitive | Require domain, policy, privacy, security, and migration review before change. |

### Current documentation reconciliation

v0.5 described a seven-entry, stop-on-first-nonzero aggregate. Current repository evidence supersedes that operational description: `run_all.py` is now a compatibility shim over the registry-driven orchestrator, the full profile contains eight validators including LayerManifest, and all selected validators run before the aggregate outcome is computed. This README corrects only the documentation; it does not alter those behavior surfaces.

[Back to top](#top)

---

<a id="authoring-rules"></a>

## Authoring and identity contract

### Required document properties

A canonical v1 JSON Schema should normally include:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://kansasfrontiermatrix.org/schemas/contracts/v1/<family>/<name>.schema.json",
  "title": "<OBJECT_FAMILY>",
  "type": "object",
  "additionalProperties": false,
  "required": [],
  "properties": {}
}
```

The exact fields come from the paired contract and object family, not from this illustrative skeleton.

### Authoring rules

| Rule | Requirement |
|---|---|
| Dialect | Canonical v1 schemas declare JSON Schema Draft 2020-12. |
| Identity | Every canonical v1 schema declares a unique stable `$id`; namespace policy remains subject to ADR and enforcement status below. |
| Meaning | Pair consequential schemas with a semantic contract or label the missing contract. |
| Strictness | Prefer explicit object closure where appropriate; do not accidentally reject composed inherited properties. |
| References | Resolve local references through the reviewed repository-local schema helper. |
| Unknown fields | Reject or explicitly model them according to the contract; do not silently widen sensitive objects. |
| Enums | Treat enum changes as compatibility-significant. |
| Defaults | Do not use defaults to smuggle policy, authority, or inferred truth. |
| Examples | Keep authoritative fixture payloads in the accepted fixture root. |
| Placeholders | Mark permissive schemas visibly and prevent readiness claims. |
| Compatibility | Freeze mirrors and aliases; canonical-first changes only. |
| Documentation | State claim limits, consumers, fixtures, validators, migration, and rollback. |

<a id="id-guidance"></a>

### `$id` guidance

The current schema workflow requires every canonical v1 schema to declare:

- Draft 2020-12;
- a nonempty `$id`;
- a unique `$id` across the canonical tree.

ADR-0001 proposes the prefix `https://kansasfrontiermatrix.org/schemas/contracts/v1/`, but the ADR remains proposed and the current workflow does not enforce that prefix. Treat it as a proposed namespace convention until the decision and enforcement are accepted.

A stable `$id` supports schema resolution. It is not proof that:

- the URL is deployed;
- an external registry serves it;
- all references resolve outside the repository;
- the schema is accepted or released;
- the underlying object is semantically valid.

Changing `$id` may be identity-breaking even when the file path remains unchanged.

[Back to top](#top)

---

<a id="strictness"></a>

## Reference resolution and strictness

### Local reference resolution

The shared local resolver:

- scans `schemas/contracts/v1/**/*.schema.json`;
- loads schemas with nonempty `$id`;
- fails on duplicate `$id`;
- creates an in-memory referencing registry;
- supports repository-local `$ref` evaluation without implying a public registry service.

Reference validation should fail closed when a required schema cannot be loaded or resolved.

<a id="domain-alias-schemas"></a>

### Domain alias schemas

When a domain alias wraps a shared schema using `allOf` and `$ref`, object closure belongs at the composed result:

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://kansasfrontiermatrix.org/schemas/contracts/v1/domains/<domain>/<alias>.schema.json",
  "allOf": [
    {
      "$ref": "https://kansasfrontiermatrix.org/schemas/contracts/v1/<family>/<base>.schema.json"
    }
  ],
  "unevaluatedProperties": false
}
```

Do not add wrapper-level `additionalProperties: false` when it would reject properties evaluated by the referenced base schema. Under Draft 2020-12, `unevaluatedProperties: false` closes the composed object after referenced properties are evaluated.

### Reference review checklist

- [ ] Every `$ref` target exists or is intentionally external.
- [ ] Local IDs are unique.
- [ ] No circular reference creates uncontrolled evaluation or tooling failure.
- [ ] Alias schemas add domain identity without changing shared semantics.
- [ ] Compatibility wrappers do not widen or narrow canonical shape silently.
- [ ] External references have version, availability, rights, and offline-test posture.
- [ ] Reference changes have fixtures and rollback.

[Back to top](#top)

---

<a id="configured-validator-surface"></a>

## Configured validator surface

### Registry-driven execution model

```text
tools/validate_all.py
  -> tools/validators/validate_all.py
     -> tools/validators/validator_registry.json
        -> selected repository validators

tools/validators/_common/run_all.py
  -> compatibility wrapper for --profile full
  -> preserves RUNNER_VALIDATORS and make schemas compatibility
```

The registry is an execution-selection contract for the orchestrator. It does not establish complete schema inventory, schema adoption, semantic meaning, policy, review, release, or publication.

### Profiles

| Profile | Registered selection | Intended use | Boundary |
|---|---|---|---|
| `focused` | SourceDescriptor, EvidenceRef, EvidenceBundle, RuntimeResponseEnvelope | Fast shared trust-shape checks | Not all registered validators. |
| `changed-area` | Dynamic matches from changed repository paths and registered globs | Risk-proportionate validation | Coverage is only as complete as the globs; no match is `ABSTAIN`. |
| `release-dry-run` | EvidenceBundle, LayerManifest, DecisionEnvelope, RunReceipt, IngestReceipt | Release-adjacent fixture checks | Does not assemble, approve, sign, release, roll back, or publish. |
| `full` | All eight validators in registry order | Aggregate compatibility path | Registered surface only; not the full schema tree. |

### Full-profile inventory

| Order | Registry ID | Validator script | Principal schema / fixture surface |
|---:|---|---|---|
| 1 | `source-descriptor` | `tools/validators/validate_source_descriptor.py` | `schemas/contracts/v1/source/source_descriptor.schema.json`; `fixtures/contracts/v1/source/source_descriptor/` |
| 2 | `evidence-ref` | `tools/validators/validate_evidence_ref.py` | `schemas/contracts/v1/evidence/evidence_ref.schema.json`; `fixtures/contracts/v1/evidence/evidence_ref/` |
| 3 | `evidence-bundle` | `tools/validators/validate_evidence_bundle.py` | `schemas/contracts/v1/evidence/evidence_bundle.schema.json`; `fixtures/contracts/v1/evidence/evidence_bundle/` |
| 4 | `layer-manifest` | `tools/validators/data/validate_layer_manifest.py` | `schemas/contracts/v1/data/layer_manifest.schema.json`; `fixtures/data/layer_manifest/` |
| 5 | `runtime-response-envelope` | `tools/validators/validate_runtime_response_envelope.py` | `schemas/contracts/v1/runtime/runtime_response_envelope.schema.json`; `fixtures/contracts/v1/runtime/runtime_response_envelope/` |
| 6 | `decision-envelope` | `tools/validators/validate_decision_envelope.py` | `schemas/contracts/v1/runtime/decision_envelope.schema.json`; `fixtures/contracts/v1/runtime/decision_envelope/` |
| 7 | `run-receipt` | `tools/validators/validate_run_receipt.py` | `schemas/contracts/v1/runtime/run_receipt.schema.json`; `fixtures/contracts/v1/runtime/run_receipt/` |
| 8 | `ingest-receipt` | `tools/validators/validate_ingest_receipt.py` | `schemas/contracts/v1/source/ingest_receipt.schema.json`; `fixtures/contracts/v1/source/ingest_receipt/` |

For each configured family, current schema CI requires the schema and validator to exist, positive and negative fixture lanes to be nonempty, reviewed rejection expectations to cover negative fixtures, and the compatibility inventory to match the workflow's configured family map. LayerManifest uses a fixture expectation manifest; the other listed shared families use adjacent expected-error sidecars.

This is deliberately bounded. It does not imply that every implementation-bearing schema has a registered top-level validator, fixtures, policy checks, consumer tests, or release integration.

[Back to top](#top)

---

## Schema maturity and admission

### Maturity classes

| Class | Meaning | Release implication |
|---|---|---|
| `PLACEHOLDER` | Accept-any or minimally constrained shape used to reserve an object name. | Cannot support readiness or release claims. |
| `PROPOSED` | Meaningful draft shape with incomplete review or adoption. | May support design/testing only. |
| `FIXTURE_BACKED` | Valid and invalid fixtures exist with reviewed expected failures. | Stronger shape evidence; still not semantic/policy/release proof. |
| `VALIDATOR_WIRED` | Repository validator invokes the schema and fixtures. | Bounded executable evidence. |
| `PROFILE_REGISTERED` | Validator is selectable through the bounded orchestrator registry. | Selection evidence only; does not prove full coverage. |
| `CONSUMER_TESTED` | Known consumers have compatibility tests. | Supports migration decisions. |
| `RELEASE_BOUND` | Accepted release objects identify schema version and rollback. | Requires separate release authority. |
| `DEPRECATED` | Superseded with compatibility and sunset guidance. | New writes should stop. |

A file can carry more than one qualifier, but no maturity label should be inferred from filename, age, permissive success, or registry membership.

### Admission checklist

Before calling a schema implementation-bearing:

- [ ] paired contract exists;
- [ ] nontrivial required fields and constraints exist;
- [ ] `additionalProperties` / `unevaluatedProperties` posture is intentional;
- [ ] valid fixtures are nonempty;
- [ ] invalid fixtures are nonempty;
- [ ] expected errors are reviewed;
- [ ] validator wiring exists;
- [ ] registry/profile coverage is understood when applicable;
- [ ] consumer tests exist where material;
- [ ] policy-sensitive fields have policy tests;
- [ ] migration and rollback are defined;
- [ ] release binding is separate and explicit.

[Back to top](#top)

---

<a id="change-planning"></a>

## Change planning and compatibility

### Change-impact matrix

| Change | Likely class | Required action |
|---|---|---|
| Add optional property | Potentially additive | Verify consumers, generated code, and strict aliases. |
| Add required property | Breaking | Version/migration, fixture updates, consumer updates, rollback. |
| Remove property | Breaking | Deprecation, compatibility window, migration, correction if released. |
| Narrow enum or numeric range | Breaking for previously valid data | Inventory affected instances and consumers. |
| Widen enum or shape | Additive structurally; may be semantic/policy-significant | Contract and policy review. |
| Change `$id` | Identity-breaking | New version/alias/migration; update all references. |
| Change `$ref` target | Potential semantic and shape change | Dependency diff, fixtures, consumer tests, rollback. |
| Change permissive placeholder to typed schema | Maturity transition, often breaking | Valid/invalid fixtures, validator wiring, migration and held-readiness review. |
| Add or remove a registry entry/profile member | Behavioral validation change | Registry tests, profile intent, path-glob review, CI parity, rollback. |
| Change a validator path glob | Changed-area coverage change | Positive/negative selection tests and no-match interpretation review. |
| Move compatibility schema | Placement change | Directory Rules/ADR review, redirect or alias strategy, inbound-link update. |
| Change sensitivity-bearing fields | Elevated | Domain, policy, privacy, security, and release review. |

### Consumer-impact questions

- Which validators import the schema?
- Which registry entries or profiles select those validators?
- Which schemas reference its `$id`?
- Which fixtures and tests exercise it?
- Which apps, packages, connectors, pipelines, or tools generate or consume it?
- Which receipts, proofs, catalogs, or releases cite its version?
- Which compatibility aliases or external users depend on the old shape?
- Which published objects require correction or migration?
- What exact prior version is the rollback target?

[Back to top](#top)

---

<a id="versioning"></a>

## Versioning, deprecation, and supersession

The configured tree is named `v1`, but the complete per-object versioning and release policy remains `NEEDS VERIFICATION`.

Until accepted policy exists:

1. treat `$id` and required-field changes as potentially breaking;
2. preserve old schemas needed to validate retained historical records;
3. do not rewrite released schemas in place without compatibility and correction analysis;
4. use explicit deprecation notes and forward links;
5. maintain fixtures for old/new parity where consumers span versions;
6. preserve migration receipts or manifests where governed records are transformed;
7. keep compatibility aliases frozen except for canonical reference updates;
8. define a mechanical rollback to the prior schema, validator, registry, and consumer state.

A version directory or registry entry does not by itself prove semantic versioning, external support, deployment, or release.

[Back to top](#top)

---

## Correction and rollback

### Documentation rollback

Before merge, close or abandon the draft PR and branch. After merge, revert the README-only commit or restore prior blob `7e29afc982af13b3dea313bb524664b520b07beb`. Because v0.6 changes documentation only, do not roll back the pre-existing registry, orchestrator, Make, workflow, schema, or fixture behavior merely to match the older README.

### Schema correction triggers

Correct, hold, or withdraw a schema change when:

- documented meaning and machine shape diverge;
- a `$ref` resolves to the wrong object family;
- a schema accepts known-invalid sensitive or release objects;
- a schema rejects previously supported released records without migration;
- an alias diverges from its canonical base;
- valid/invalid fixture polarity is wrong;
- expected errors no longer represent the intended failure;
- a workflow, validator, registry entry, or path glob silently skips the required family;
- `$id` collides or changes unintentionally;
- permissive placeholders are cited as readiness;
- consumers or published artifacts cannot roll back.

### Operational rollback sequence

For a consequential schema regression:

1. stop promotion and public rollout;
2. identify affected schema IDs, instances, validators, profiles, consumers, releases, and caches;
3. preserve failure evidence;
4. restore the prior schema/validator/registry/consumer set or activate an accepted compatibility path;
5. re-run fixtures, selected profiles, consumer tests, policy checks, and release checks;
6. invalidate unsafe generated artifacts;
7. issue correction, withdrawal, or migration records through the owning authority where required;
8. document root cause and prevention;
9. remove temporary compatibility only after the verification window.

[Back to top](#top)

---

<a id="open-questions"></a>

## Open verification register

| ID | Item | Evidence needed |
|---|---|---|
| KFM-SCH-01 | Accept/revise/reject ADR-0001 | Accountable ADR review and decision record |
| KFM-SCH-02 | Accept/revise/reject ADR-0002 | Accountable ADR review and decision record |
| KFM-SCH-03 | Authoritative schema registry | Implemented registry/generator, ownership, tests, CI, correction policy |
| KFM-SCH-04 | Complete recursive schema inventory | Commit-pinned tree, classifications, schema counts, compatibility status |
| KFM-SCH-05 | Compatibility-lane migration plan | Per-lane source/target map, ADR/drift entry, consumers, rollback |
| KFM-SCH-06 | MapLibre placeholder graduation | Meaningful schemas, fixtures, validators, runtime tests, accepted output roots |
| KFM-SCH-07 | Evidence/governance compatibility closure | Canonical counterparts, parity tests, deprecation and removal plan |
| KFM-SCH-08 | People/DNA/land compatibility closure | Domain/privacy/policy review, migration, public-safe denial tests |
| KFM-SCH-09 | Cross-schema dependency graph | Deterministic `$id`/`$ref` graph, cycle detection, orphan report |
| KFM-SCH-10 | Consumer inventory | Static search plus app/package/pipeline/runtime and external consumer evidence |
| KFM-SCH-11 | Versioning policy | Accepted compatibility classes, bump rules, support windows, rollback |
| KFM-SCH-12 | External schema publication | Hosting, immutable IDs, cache, availability, security, release manifest |
| KFM-SCH-13 | Schema steward and separation of duties | StewardshipAssignment, CODEOWNERS/ruleset evidence, review policy |
| KFM-SCH-14 | Full validator coverage | Registry of implementation-bearing schemas, fixture/test matrix, and disclosed gaps |
| KFM-SCH-15 | Policy-significant field coverage | Policy fixtures and tests for rights, sensitivity, access, and release fields |
| KFM-SCH-16 | Generated code compatibility | Generator identity, locked versions, reproducibility, diff, and rollback tests |
| KFM-SCH-17 | Validator registry versus schema registry terminology | Accepted naming and documentation that prevents authority collapse |
| KFM-SCH-18 | Branch protection and required checks | Repository ruleset evidence |
| KFM-SCH-19 | Schema release binding | ReleaseManifest/receipt/proof references and rollback drill |
| KFM-SCH-20 | Historical-record validation | Retained schema versions and fixtures for released/corrected records |
| KFM-SCH-21 | Changed-area profile coverage | Path-glob coverage tests, explicit no-match expectations, and orphan-change report |
| KFM-SCH-22 | CI/registry synchronization | One reviewed source of truth or deterministic parity generator/test for workflow family maps |
| KFM-SCH-23 | Atmosphere compatibility closure | Object/path inventory, Air/Atmosphere decision, aliases, migration, consumers, rollback |
| KFM-SCH-24 | Biotopes compatibility closure | Vocabulary decision and object-by-object Habitat/Flora routing manifest |
| KFM-SCH-25 | Profile names versus actual authority | Ensure `release-dry-run` remains visibly fixture-only and cannot be mistaken for governed release execution |

[Back to top](#top)

---

## No-loss ledger

| v0.5 surface | v0.6 disposition |
|---|---|
| Stable path, H1, and `kfm://doc/schemas-readme` identity | Preserved |
| Machine-shape purpose | Preserved and tightened |
| Contracts/schemas/policy/data/release split | Preserved |
| Schema-valid-is-not-truth warning | Preserved and elevated |
| Required root-README section order | Preserved |
| Stable custom anchors and quick navigation | Preserved; missing explicit section anchors added without removing prior fragments |
| JSON Schema 2020-12 posture | Preserved and grounded in current workflow |
| Contract pairing and domain alias strictness | Preserved |
| Shared-runner `EXPECTED_FAIL` versus `FAIL` semantics | Preserved and separated from orchestrator outcomes |
| `$id` uniqueness guidance | Preserved; proposed prefix remains visibly proposed |
| Versioning, change planning, correction, and rollback | Preserved and expanded for registry/profile changes |
| Open questions | Preserved and extended with orchestrator, CI parity, atmosphere, and biotopes items |
| Root-level compatibility lanes | Preserved; atmosphere and biotopes added from current direct-child evidence |
| Seven-validator stop-on-first-failure description | Repaired to the current eight-validator registry and all-selected aggregation behavior |
| `make schemas` guidance | Preserved as compatibility route; canonical operator entrypoint surfaced |
| Directory Rules status | Repaired to distinguish accepted ADR-0029 from the pinned artifact's retained pre-adoption label |
| Validator registry | Newly documented without misclassifying it as a schema registry |
| Ownership | Preserved as verified CODEOWNERS routing with stewardship limitations |
| Legacy fragments | Preserved through explicit anchors |

[Back to top](#top)

---

## Evidence ledger

| Evidence | Observation supported | Status |
|---|---|---:|
| `schemas/README.md@3a97155…` / blob `7e29afc…` | Complete v0.5 baseline and stable identity | `CONFIRMED` |
| `docs/doctrine/directory-rules.md` / blob `fd49a0b…` plus accepted ADR-0029 | Adopted responsibility-root, compatibility, migration, and README law | `CONFIRMED doctrine / ACCEPTED decision` |
| ADR-0001 / blob `3c520ea…` | Proposed `schemas/contracts/v1` default-home decision | `CONFIRMED file; PROPOSED decision` |
| ADR-0002 / blob `2da10fc…` | Proposed contracts/schemas/policy/fixtures/tests/validators split | `CONFIRMED file; effectively PROPOSED decision` |
| `schemas/contracts/v1/README.md` / blob `bbe931c…` | Current mixed-maturity versioned schema-family index | `CONFIRMED` |
| `tools/validators/validator_registry.json` / blob `12517f3…` | Eight validators and focused, changed-area, release-dry-run, and full profiles | `CONFIRMED source` |
| `tools/validators/validate_all.py` / blob `728cf14…` | Registry validation, deterministic selection/reporting, all-selected aggregation, exit semantics | `CONFIRMED source` |
| `tools/validate_all.py` / blob `c308015…` | Canonical thin operator entrypoint | `CONFIRMED source` |
| `tools/validators/_common/run_all.py` / blob `c3a87b4…` | Historical compatibility entrypoint and `RUNNER_VALIDATORS` export | `CONFIRMED source` |
| `schema-validation.yml` / blob `3deebb4…` | Eight configured families, schema identity checks, aggregate run, and schema/contract tests | `CONFIRMED workflow definition` |
| `validator-suite.yml` / blob `b028ae1…` | Harness, generated-receipt, material-change, aggregate, and canary checks | `CONFIRMED workflow definition` |
| `Makefile` / blob `4abc7f9…` | `make schemas`, `make test`, and `make validate` command routing | `CONFIRMED source` |
| `schemas/atmosphere/README.md` / `schemas/biotopes/README.md` | Direct compatibility lanes, frozen writes, and unresolved migration/vocabulary boundaries | `CONFIRMED bounded inspection` |
| `.github/CODEOWNERS` / blob `dd2a84a…` | `/schemas/` review routing and its authority limits | `CONFIRMED` |

[Back to top](#top)

---

## Changelog

| Version | Date | Change | Rollback |
|---|---|---|---|
| v0.2 | Before 2026-07-19 | Expanded the short schema-root stub into a boundary guide | Retained in Git history |
| v0.3 | 2026-07-19 | Added child-lane, CI, strictness, alias, `$id`, and change-planning guidance | Restore v0.2 through Git history |
| v0.4 | 2026-07-23 | Reordered to Directory Rules, refreshed workflows and validator inventory, surfaced compatibility lanes and ADR status, replaced placeholder ownership, and added no-loss/evidence/rollback registers | Restore blob `43c989a3bead8289bdbaba1a645980f95b0baf3a` |
| v0.5 | 2026-08-01 | Reconciled the seven-entry aggregate, sorted nonempty fixture lanes, `EXPECTED_FAIL` diagnostics, focused direct tests, and aligned workflow guidance | Restore blob `15c84131862c00584664dfafa497c012ae765d33` with its paired historical behavior surfaces |
| v0.6 | 2026-08-09 | Reconciled the registry-driven eight-validator orchestrator, four profiles, current workflows, accepted Directory Rules status, and direct atmosphere/biotopes compatibility lanes without changing behavior | Restore blob `7e29afc982af13b3dea313bb524664b520b07beb` or revert the README-only commit |

<p align="right"><a href="#top">Back to top</a></p>
