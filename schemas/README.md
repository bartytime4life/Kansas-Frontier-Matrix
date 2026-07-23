# schemas

> **One-line purpose.** `schemas/` owns KFM's machine-checkable object shapes. It constrains payload structure without becoming semantic meaning, evidence, policy, source authority, lifecycle state, release approval, or public truth.

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-readme
title: schemas/ — Canonical Machine-Shape Root and Compatibility Boundary
type: README
version: v0.4
status: draft; repository-grounded; canonical-machine-shape-root; configured-v1-validation-surface; compatibility-debt-visible; non-semantic; non-policy; non-release
owner: NEEDS VERIFICATION — explicit CODEOWNERS routing is @bartytime4life; no accepted schema-steward assignment, required-review enforcement, or independent approval control was established
created: NEEDS VERIFICATION — a short root stub existed before v0.2
updated: 2026-07-23
supersedes: v0.3 documentation at the same path; no schema, contract, policy, fixture, validator, workflow, runtime, release, or publication behavior is superseded
policy_label: repository-facing; schemas; json-schema; machine-shape; no-parallel-authority; fail-closed; correction-aware; rollback-aware
current_path: schemas/README.md
owning_root: schemas/
responsibility: own machine-checkable shape, identity constraints, reference structure, and schema-family navigation while preserving the contract/schema/policy/evidence/release split
truth_posture: cite-or-abstain; schema validity proves only the tested machine shape and never proves semantic truth, evidence closure, source authority, rights, sensitivity, policy approval, release state, or publication safety
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 0ca82aaaf6aac8e7fe5e1a91892c2ffb2132d050
  target_prior_blob: 43c989a3bead8289bdbaba1a645980f95b0baf3a
  directory_rules_blob: 2affb080e6f0043867c64c7f06c1ca52030fbd55
  schema_home_adr_blob: ab0010a278d766356845c23055f882f328abb418
  contracts_v1_readme_blob: bbe931c9f7a5f0132522c0bda4fa5455c050a973
  schema_validation_workflow_blob: e6b26337aa1eea142b96560e041419f855c44d59
  validator_suite_workflow_blob: 1694afdd762ce515b53fc8e9d7d51324c2d0929d
  aggregate_runner_blob: f734a3e0944346bf2635fb9188702f13b45c8a64
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
related:
  - ./contracts/v1/README.md
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
  - ../tools/validators/README.md
  - ../tools/validators/_common/run_all.py
  - ../.github/workflows/schema-validation.yml
  - ../.github/workflows/validator-suite.yml
  - ../docs/adr/INDEX.md
  - ../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - ../docs/adr/ADR-0002-contracts-vs-schemas-split.md
  - ../docs/doctrine/directory-rules.md
  - ../docs/registers/DRIFT_REGISTER.md
  - ../data/receipts/generated/README.md
notes:
  - "v0.4 is a same-path documentation modernization and current-evidence reconciliation."
  - "The first twelve H2 sections follow the Directory Rules folder-README contract exactly."
  - "schemas/contracts/v1 is the current configured validation surface and the Directory Rules default logical home, while ADR-0001 and ADR-0002 remain proposed rather than accepted."
  - "Root-level evidence, governance, maplibre, and people-dna-land schema lanes are documented as compatibility debt, not silently promoted to parallel authority."
  - "The aggregate runner currently invokes six fixture-backed validators and stops on the first nonzero exit."
  - "No executable, schema, contract, fixture, validator, policy, workflow, lifecycle, release, deployment, or public-surface behavior changes in this documentation update."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

[![Status: repository-grounded draft](https://img.shields.io/badge/status-repository--grounded%20draft-f59e0b?style=flat-square)](#status)
[![Authority: machine shape](https://img.shields.io/badge/authority-machine%20shape-1f6feb?style=flat-square)](#authority-level)
[![Dialect: JSON Schema 2020-12](https://img.shields.io/badge/JSON%20Schema-2020--12-8250df?style=flat-square)](#authoring-and-identity-contract)
[![Aggregate validators: 6](https://img.shields.io/badge/aggregate%20validators-6-2da44e?style=flat-square)](#configured-validator-surface)
[![CI: bounded shape checks](https://img.shields.io/badge/CI-bounded%20shape%20checks-0969da?style=flat-square)](#validation)
[![Publisher: no](https://img.shields.io/badge/publisher-no-6e7781?style=flat-square)](#authority-level)

**Quick navigation:** [Purpose](#purpose) · [Authority boundary](#authority-boundary) · [Status](#status) · [Belongs](#what-belongs-here) · [Does not belong](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related roots](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed) · [Topology](#current-child-lanes) · [Authoring](#authoring-rules) · [Aliases](#domain-alias-schemas) · [Strictness](#strictness) · [`$id`](#id-guidance) · [Versioning](#versioning) · [Planning](#change-planning) · [Open verification](#open-questions)

> [!IMPORTANT]
> **Schema validity is necessary but never sufficient.** A schema-valid object may still be semantically wrong, unsupported by evidence, stale, source-role-confused, rights-uncleared, sensitivity-restricted, policy-denied, unreleased, or unsafe for public use.

> [!CAUTION]
> **Current configuration is not settled doctrine.** `schemas/contracts/v1/` is the configured v1 validation surface and the Directory Rules default logical home, but the schema-home and contract/schema split ADRs remain proposed. This README records the implementation boundary without converting a proposed ADR into accepted authority.

> [!WARNING]
> **Compatibility paths must not evolve independently.** Confirmed root-level lanes such as `schemas/evidence/`, `schemas/governance/`, `schemas/maplibre/`, and `schemas/people-dna-land/` are compatibility or transitional surfaces. New canonical fields belong in the reviewed `schemas/contracts/v1/...` family unless an accepted ADR or migration decision says otherwise.

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

A schema is part of the trust membrane only when it remains paired with the other authorities rather than pretending to replace them.

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
| Lifecycle state | governed `data/` phases | May shape lifecycle records; cannot promote them. |
| Receipts and proofs | `data/receipts/`, `data/proofs/` | May shape records; a receipt- or proof-shaped JSON file is not automatically governed. |
| Release, correction, withdrawal, rollback | [`release/`](../release/) | May shape release objects; cannot approve, publish, correct, or roll back. |
| API/UI/MapLibre behavior | accepted app/package/runtime roots | May shape payload envelopes; cannot authorize public routes or render state. |

### Anti-collapse rules

`schemas/` must not collapse:

- structure into semantics;
- schema success into claim truth;
- a permissive placeholder into implementation maturity;
- a JSON filename into a governed object identity;
- `$id` uniqueness into a complete schema registry;
- fixture polarity into policy approval;
- validator execution into release approval;
- a compatibility wrapper into parallel canonical authority;
- a schema change into an implicit backward-compatibility promise;
- a passing workflow into public safety or KFM publication.

Public clients use governed APIs and released artifacts. They do not treat schemas or raw schema instances as public truth sources.

[Back to top](#top)

---

<a id="repo-fit"></a>

## Status

### Repository-grounded status matrix

| Surface | Current evidence at the pinned snapshot | Safe conclusion |
|---|---:|---|
| `schemas/README.md` | **CONFIRMED v0.3 baseline** | Root guidance exists, but its three-child topology and CI snapshot are stale. |
| `schemas/contracts/v1/` | **CONFIRMED configured v1 validation surface** | Current schema workflow meta-validates this tree, requires Draft 2020-12 and unique canonical `$id` values, and wires six fixture-backed object families. |
| ADR-0001 / ADR-0002 | **CONFIRMED present; status `proposed`** | The default schema-home and contracts-versus-schemas split are documented but not accepted ADR decisions. |
| `schemas/policy/` | **CONFIRMED compatibility/documentation lane** | It does not establish executable policy or a second policy authority. |
| `schemas/tests/` | **CONFIRMED compatibility/documentation lane** | Executable tests currently run from `tests/schemas/` and `tests/contracts/`. |
| `schemas/evidence/` | **CONFIRMED transitional compatibility lane** | Root-level evidence schemas remain migration debt; compatibility files must not evolve independently. |
| `schemas/governance/` | **CONFIRMED transitional compatibility lane** | Permissive or compatibility shapes do not prove accepted governance contracts. |
| `schemas/maplibre/` | **CONFIRMED transitional compatibility lane** | Eight MapLibre schema names currently remain accept-any-object placeholders under the readiness workflow. |
| `schemas/people-dna-land/` | **CONFIRMED transitional compatibility lane** | Sensitive-domain legacy paths remain migration and policy-review work, not parallel authority. |
| `schema-validation` workflow | **CONFIRMED command-bearing definition** | Parses schema JSON, meta-validates schemas, checks canonical IDs and configured fixtures, then runs aggregate validators and schema/contract tests. |
| `validator-suite` workflow | **CONFIRMED command-bearing definition** | Requires a nonempty aggregate inventory, runs it, and exercises one fail-closed EvidenceBundle canary. |
| Current PR-run results | **NEEDS VERIFICATION per revision** | A workflow definition is not proof that the current branch passed. |
| Complete recursive schema inventory | **UNKNOWN in this README edit** | The compatibility list below is bounded to inspected direct lanes; it is not a complete tree claim. |
| Authoritative schema registry | **NOT ESTABLISHED in bounded inspection** | ADR-0001 names a proposed registry path, but the referenced registry file was not found at this snapshot. |
| Ownership and required review | **NEEDS VERIFICATION** | CODEOWNERS routes `/schemas/` to `@bartytime4life`; stewardship, branch rules, and independent approval remain separate controls. |

### Truth labels used here

| Label | Meaning |
|---|---|
| `CONFIRMED` | Verified from pinned repository content, workflow definition, tests, logs, or generated artifacts inspected for this update. |
| `PROPOSED` | Design, future state, migration target, or recommendation not established as current implementation. |
| `UNKNOWN` | Evidence is insufficient to support a stronger statement. |
| `NEEDS VERIFICATION` | A concrete check is available but not closed strongly enough to act as fact. |
| `CONFLICTED` | Relevant implementation and doctrine or two authority surfaces disagree. |

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
| A second canonical schema tree or independently evolving mirror | migrate, freeze, deprecate, or obtain an accepted ADR |
| Claims that a schema-valid object is true, cited, rights-cleared, public-safe, released, or implemented | evidence, policy, review, runtime, and release authorities |

[Back to top](#top)

---

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
2. identify all local `$ref` dependencies and known consumers;
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
| Generated schema inventory | Discoverability aid; not authoritative unless its generator, source, and review state are accepted. |
| Generated receipt for an AI-authored documentation change | Process provenance; not human approval, schema proof, or publication authority. |

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

## Validation

### Repository commands

```bash
python -m pip install -e ".[test]"

make schemas
make test
make validate
```

Current command scope:

| Command | Confirmed behavior | Claim limit |
|---|---|---|
| `make schemas` | Runs `python tools/validators/_common/run_all.py`. | Only configured fixture-backed validator families. |
| `make test` | Runs `python -m pytest tests/schemas tests/contracts -q`. | Only collected schema/contract tests. |
| `make validate` | Runs `make schemas` and `make test`. | Not a full repository or release gate. |

### Workflow coverage

[`schema-validation.yml`](../.github/workflows/schema-validation.yml) currently:

1. installs the declared test dependencies on Python 3.11;
2. requires the configured validator inventory to match six exact schema/fixture families;
3. requires nonempty valid and invalid fixture lanes;
4. requires an `.expected_error.txt` sidecar for each configured invalid fixture;
5. parses every JSON file under `schemas/`;
6. meta-validates every `*.schema.json` with Draft 2020-12;
7. requires every `schemas/contracts/v1/**/*.schema.json` file to declare Draft 2020-12;
8. requires canonical v1 schemas to have unique `$id` values;
9. runs `make schemas`;
10. runs `python -m pytest -q tests/schemas tests/contracts`;
11. records only workflow logs and a step summary.

[`validator-suite.yml`](../.github/workflows/validator-suite.yml) separately requires a nonempty, unique aggregate inventory, confirms fixture-mode invocation, runs `make schemas`, and rejects a reviewed invalid EvidenceBundle canary with the expected missing-`bundle_id` failure.

Neither workflow emits or authorizes a governed ValidationReport, receipt, proof, policy decision, lifecycle record, release record, or publication.

### Validation interpretation

> [!NOTE]
> The shared runner intentionally prints expected-invalid fixtures with a `FAIL` line. The fixture is successful when the validator rejects it for the reviewed reason and the final validator process exits successfully. Read the terminal exit and final summary, not an isolated line label.

| Exit | Shared schema-runner meaning |
|---:|---|
| `0` | All configured valid fixtures passed and all configured invalid fixtures were rejected for expected reasons. |
| `1` | A tested valid fixture failed, an invalid fixture was accepted, or expected error evidence did not match. |
| `2` | Schema, reference, fixture, or operating error prevented valid evaluation. |

### Documentation-only validation for this README

```bash
git diff -- schemas/README.md
git diff --check
```

Repository-native CI remains the source for branch-current execution results.

[Back to top](#top)

---

## Review burden

### Baseline review

README-only clarification requires:

- schema-root maintainer review;
- link and anchor checks;
- no-loss review;
- verification that no machine file or authority claim changed.

### Schema-family review

A schema change requires review by the affected schema and contract owners, plus the owners of touched fixtures, validators, tests, and consumers.

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

`.github/CODEOWNERS` routes `/schemas/` to `@bartytime4life`. That is a GitHub review-routing fact only. It is not a StewardshipAssignment, completed ReviewRecord, branch-protection rule, independent approval, schema acceptance, release approval, or KFM publication.

### Separation of duties

Where maturity and consequence justify it, the same actor should not silently:

1. redefine semantic meaning;
2. change machine shape;
3. update fixtures and expected errors;
4. alter the validator;
5. approve the policy consequence;
6. approve release.

Any temporary consolidation of duties must be explicit, reviewed, bounded, and reversible.

[Back to top](#top)

---

## Related folders

| Path | Relationship |
|---|---|
| [`schemas/contracts/v1/`](./contracts/v1/) | Current configured v1 machine-schema surface and proposed default canonical family. |
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
| [`tools/validators/`](../tools/validators/) | Validator implementation and shared runners. |
| [`data/receipts/generated/`](../data/receipts/generated/) | Generated provenance records for AI-authored changes. |
| [`release/`](../release/) | Promotion, release, correction, withdrawal, and rollback authority. |
| [Schema validation workflow](../.github/workflows/schema-validation.yml) | Canonical v1 identity, fixture, aggregate, and schema/contract test checks. |
| [Validator suite workflow](../.github/workflows/validator-suite.yml) | Aggregate inventory and fail-closed canary checks. |
| [Directory Rules](../docs/doctrine/directory-rules.md) | Responsibility-root, compatibility, migration, and README-order doctrine. |
| [ADR index](../docs/adr/INDEX.md) | Current decision inventory and ADR status. |
| [Drift register](../docs/registers/DRIFT_REGISTER.md) | Repository drift disclosures; schema migration coverage remains incomplete. |

[Back to top](#top)

---

## ADRs

### Current schema decisions

| Decision | Current status | Consequence for this README |
|---|---:|---|
| [ADR-0001 — `schemas/contracts/v1` is canonical](../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md) | `proposed` | Use as proposed direction and current configured path, not as accepted decision authority. |
| [ADR-0002 — contracts versus schemas split](../docs/adr/ADR-0002-contracts-vs-schemas-split.md) | `proposed` | Preserve semantic meaning under `contracts/` and machine shape under `schemas/`; do not claim acceptance. |
| Directory Rules schema-home convention | doctrine | `schemas/contracts/v1/...` is the default logical home; conflicts require drift/ADR handling. |

### Decisions still needed

- Accept, revise, supersede, or reject ADR-0001.
- Accept, revise, supersede, or reject ADR-0002.
- Decide the authoritative schema registry and its generated/manual ownership.
- Classify every root-level compatibility lane and define migration, freeze, or retirement.
- Define version-bump and compatibility policy by change class.
- Define cross-schema reference and cycle rules.
- Define externally consumed schema support and deprecation windows.
- Define generated schema-inventory and release binding.
- Define schema steward and independent-review requirements.

No ADR is accepted, superseded, or implemented by this README change.

[Back to top](#top)

---

<a id="last-reviewed"></a>

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-23 |
| Evidence base | `main@0ca82aaaf6aac8e7fe5e1a91892c2ffb2132d050` |
| Prior README blob | `43c989a3bead8289bdbaba1a645980f95b0baf3a` |
| Review mode | Complete-baseline, repository-grounded, same-path documentation modernization |
| Implementation effect | None — documentation and generated provenance only |
| Runtime/release effect | None |
| Human review | Pending |
| Rollback | Close the draft PR before merge, or revert the README and generated-receipt commits after merge |

Re-review this README when:

- the aggregate validator inventory changes;
- canonical v1 `$id` policy changes;
- ADR-0001 or ADR-0002 changes status;
- a compatibility schema lane is added, migrated, frozen, or removed;
- schema registry implementation appears;
- fixture or expected-error conventions change;
- the local reference resolver changes;
- `schema-validation` or `validator-suite` changes scope;
- a schema becomes externally published or version-supported;
- a policy-sensitive object family changes;
- CODEOWNERS, branch rules, or stewardship changes;
- Directory Rules changes schema placement or README requirements.

[Back to top](#top)

---

<a id="current-child-lanes"></a>

## Repository topology and compatibility lanes

### Bounded inspected topology

```text
schemas/
├── README.md
├── contracts/
│   └── v1/                      # current configured v1 machine-schema tree
├── policy/                      # compatibility/documentation lane
├── tests/                       # compatibility/documentation lane
├── evidence/                    # transitional compatibility lane
├── governance/                  # transitional compatibility lane
├── maplibre/                    # transitional compatibility + permissive placeholders
└── people-dna-land/             # sensitive-domain transitional compatibility
```

This tree is a **bounded inspected view**, not an assertion that these are the only direct children.

### Lane classification

| Lane | Classification | Write posture |
|---|---|---|
| `contracts/v1/` | Current configured versioned schema tree; proposed default canonical home | New reviewed canonical schema work lands here unless an accepted ADR says otherwise. |
| `policy/` | Compatibility/documentation | Do not add executable policy or independently evolve duplicate schema authority. |
| `tests/` | Compatibility/documentation | Do not move executable tests here without an accepted ownership/migration decision. |
| `evidence/` | Transitional compatibility | Migrate or freeze against canonical evidence families; do not add divergent fields. |
| `governance/` | Transitional compatibility | Treat permissive shapes as incomplete; do not infer governance maturity. |
| `maplibre/` | Transitional compatibility | Treat eight accept-any-object schema files as readiness-held placeholders. |
| `people-dna-land/` | Transitional compatibility / sensitive | Require domain, policy, privacy, and migration review before change. |

### Known documentation discrepancy

[`tests/schemas/README.md`](../tests/schemas/) still describes an older five-validator aggregate in its current text, while current `run_all.py` and `schema-validation.yml` configure six different core object validators. This root README records the current code/workflow evidence and leaves the child README correction as a separate same-path documentation task.

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

The exact fields come from the paired contract and object family, not from this example.

### Authoring rules

| Rule | Requirement |
|---|---|
| Dialect | Canonical v1 schemas declare JSON Schema Draft 2020-12. |
| Identity | Every canonical v1 schema declares a unique stable `$id`; namespace policy remains subject to the proposed ADR and enforcement status below. |
| Meaning | Pair consequential schemas with a semantic contract or label the missing contract. |
| Strictness | Prefer explicit object closure where appropriate; do not accidentally reject composed inherited properties. |
| References | Resolve local references through the reviewed canonical schema registry helper. |
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

A stable `$id` is object identity for schema resolution. It is not proof that:

- the URL is deployed;
- an external registry serves it;
- all references resolve outside the repository;
- the schema is accepted or released;
- the underlying object is semantically valid.

Changing `$id` may be an identity-breaking change even when the file path remains unchanged.

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

The aggregate runner currently invokes these six validators in order and stops on the first nonzero result:

| Order | Validator | Schema | Fixture root |
|---:|---|---|---|
| 1 | `validate_source_descriptor.py` | `schemas/contracts/v1/source/source_descriptor.schema.json` | `fixtures/contracts/v1/source/source_descriptor/` |
| 2 | `validate_evidence_ref.py` | `schemas/contracts/v1/evidence/evidence_ref.schema.json` | `fixtures/contracts/v1/evidence/evidence_ref/` |
| 3 | `validate_evidence_bundle.py` | `schemas/contracts/v1/evidence/evidence_bundle.schema.json` | `fixtures/contracts/v1/evidence/evidence_bundle/` |
| 4 | `validate_runtime_response_envelope.py` | `schemas/contracts/v1/runtime/runtime_response_envelope.schema.json` | `fixtures/contracts/v1/runtime/runtime_response_envelope/` |
| 5 | `validate_decision_envelope.py` | `schemas/contracts/v1/runtime/decision_envelope.schema.json` | `fixtures/contracts/v1/runtime/decision_envelope/` |
| 6 | `validate_run_receipt.py` | `schemas/contracts/v1/runtime/run_receipt.schema.json` | `fixtures/contracts/v1/runtime/run_receipt/` |

For each configured family, current CI requires:

```text
schema exists
valid/*.json is nonempty
invalid/*.json is nonempty
every invalid JSON has an adjacent .expected_error.txt
validator exists
aggregate inventory matches workflow configuration
```

This is a deliberately bounded surface. It does not imply every schema under `schemas/` has a configured top-level validator, fixtures, policy checks, consumer tests, or release integration.

[Back to top](#top)

---

## Schema maturity and admission

### Maturity classes

| Class | Meaning | Release implication |
|---|---|---|
| `PLACEHOLDER` | Accept-any or minimally constrained shape used to reserve an object name. | Cannot support readiness or release claims. |
| `PROPOSED` | Meaningful draft shape with incomplete review or adoption. | May support design/testing only. |
| `FIXTURE_BACKED` | Valid and invalid fixtures exist with expected failures. | Stronger shape evidence; still not semantic/policy/release proof. |
| `VALIDATOR_WIRED` | Repository validator invokes the schema and fixtures. | Bounded executable evidence. |
| `CONSUMER_TESTED` | Known consumers have compatibility tests. | Supports migration decisions. |
| `RELEASE_BOUND` | Accepted release objects identify schema version and rollback. | Requires separate release authority. |
| `DEPRECATED` | Superseded with compatibility and sunset guidance. | New writes should stop. |

A file can have more than one qualifier, but no maturity label should be inferred from filename, age, or permissive success.

### Admission checklist

Before calling a schema implementation-bearing:

- [ ] paired contract exists;
- [ ] nontrivial required fields and constraints exist;
- [ ] `additionalProperties` / `unevaluatedProperties` posture is intentional;
- [ ] valid fixtures are nonempty;
- [ ] invalid fixtures are nonempty;
- [ ] expected errors are reviewed;
- [ ] validator wiring exists;
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
| Move compatibility schema | Placement change | Directory Rules/ADR review, redirect or alias strategy, inbound-link update. |
| Change sensitivity-bearing fields | Elevated | Domain, policy, privacy, security, and release review. |

### Consumer-impact questions

- Which validators import the schema?
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

The current canonical tree is named `v1`, but the complete per-object versioning and release policy remains `NEEDS VERIFICATION`.

Until accepted policy exists:

1. treat `$id` and required-field changes as potentially breaking;
2. preserve old schemas needed to validate retained historical records;
3. do not rewrite released schemas in place without compatibility and correction analysis;
4. use explicit deprecation notes and forward links;
5. maintain fixtures for old/new parity where consumers span versions;
6. preserve migration receipts or manifests where governed records are transformed;
7. keep compatibility aliases frozen except for canonical reference updates;
8. define a mechanical rollback to the prior schema and consumer state.

A version directory does not by itself prove semantic versioning, external support, deployment, or release.

[Back to top](#top)

---

## Correction and rollback

### Documentation rollback

Before merge, close the draft PR and delete or abandon its branch. After merge, revert the README and generated-receipt commits or restore prior README blob `43c989a3bead8289bdbaba1a645980f95b0baf3a`.

### Schema correction triggers

Correct, hold, or withdraw a schema change when:

- documented meaning and machine shape diverge;
- a `$ref` resolves to the wrong object family;
- a schema accepts known-invalid sensitive or release objects;
- a schema rejects previously supported released records without migration;
- an alias diverges from its canonical base;
- valid/invalid fixture polarity is wrong;
- expected errors no longer represent the intended failure;
- a workflow or validator silently skips the family;
- `$id` collides or changes unintentionally;
- permissive placeholders are cited as readiness;
- consumers or published artifacts cannot roll back.

### Operational rollback sequence

For a consequential schema regression:

1. stop promotion and public rollout;
2. identify affected schema IDs, instances, consumers, releases, and caches;
3. preserve failure evidence;
4. restore the prior schema/validator/consumer set or activate an accepted compatibility path;
5. re-run fixtures, validators, consumer tests, policy checks, and release checks;
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
| KFM-SCH-14 | Full validator coverage | Registry of all implementation-bearing schemas, fixture/test matrix, gaps |
| KFM-SCH-15 | Policy-significant field coverage | Policy fixtures and tests for rights, sensitivity, access, release fields |
| KFM-SCH-16 | Generated code compatibility | Generator identity, locked versions, reproducibility, diff and rollback tests |
| KFM-SCH-17 | Stale `tests/schemas/README.md` aggregate count | Same-path child README update grounded in current runner/workflow |
| KFM-SCH-18 | Branch protection and required checks | Repository ruleset evidence |
| KFM-SCH-19 | Schema release binding | ReleaseManifest/receipt/proof references and rollback drill |
| KFM-SCH-20 | Historical-record validation | Retained schema versions and fixtures for released/corrected records |

[Back to top](#top)

---

## No-loss ledger

| v0.3 surface | v0.4 disposition |
|---|---|
| Stable path, H1, and `kfm://doc/schemas-readme` identity | Preserved |
| Machine-shape purpose | Preserved and tightened |
| Contracts/schemas/policy/data/release split | Preserved |
| Schema-valid-is-not-truth warning | Preserved and elevated |
| `contracts/v1`, `policy`, and `tests` lanes | Preserved |
| What belongs / does not belong | Preserved in required Directory Rules order |
| JSON Schema 2020-12 posture | Preserved and grounded in current CI |
| Contract pairing | Preserved |
| Domain alias strictness with `unevaluatedProperties` | Preserved |
| Valid/invalid fixture polarity and `FAIL` log caveat | Preserved and expanded |
| `$id` uniqueness guidance | Preserved and grounded in current workflow; prefix remains explicitly proposed |
| Versioning and change planning | Preserved and expanded |
| Open questions | Preserved and converted to an actionable register |
| Last-reviewed information | Added as required section |
| Root-level compatibility lanes | Newly surfaced from current evidence |
| Current six-validator aggregate | Reconciled to current runner/workflow |
| Stale child README discrepancy | Newly disclosed without expanding file scope |
| Ownership | Replaced placeholder role list with verified routing limits |
| Legacy fragments | Preserved through explicit anchors |

[Back to top](#top)

---

## Evidence ledger

| Evidence | Observation supported | Status |
|---|---|---:|
| `schemas/README.md@0ca82aa…` / blob `43c989a…` | Complete v0.3 baseline and stable identity | `CONFIRMED` |
| `docs/doctrine/directory-rules.md` / blob `2affb08…` | Canonical machine-shape responsibility and required README order | `CONFIRMED doctrine` |
| ADR-0001 / blob `ab0010a…` | Proposed `schemas/contracts/v1` canonical-home decision | `CONFIRMED file; PROPOSED decision` |
| ADR-0002 | Proposed contract-meaning/schema-shape split | `CONFIRMED file; PROPOSED decision` |
| `schemas/contracts/v1/README.md` / blob `bbe931c…` | Current versioned schema-family guidance | `CONFIRMED` |
| `schema-validation.yml` / blob `e6b2633…` | Canonical IDs, fixture non-vacuity, aggregate and pytest workflow definition | `CONFIRMED definition` |
| `validator-suite.yml` / blob `1694afd…` | Aggregate inventory and fail-closed canary definition | `CONFIRMED definition` |
| `tools/validators/_common/run_all.py` / blob `f734a3e…` | Current six-validator order and stop-on-nonzero behavior | `CONFIRMED source` |
| Root compatibility READMEs | Evidence, governance, MapLibre, and people/DNA/land migration debt | `CONFIRMED bounded inspection` |
| `.github/CODEOWNERS` / blob `dd2a84a…` | `/schemas/` review routing and its authority limits | `CONFIRMED` |
| Generated-receipt schema | Provenance record shape for this AI-authored documentation change | `CONFIRMED schema file` |

[Back to top](#top)

---

## Changelog

| Version | Date | Change | Rollback |
|---|---|---|---|
| v0.2 | Before 2026-07-19 | Expanded the short schema-root stub into a boundary guide | Retained in Git history |
| v0.3 | 2026-07-19 | Added child-lane, CI, strictness, alias, `$id`, and change-planning guidance | Restore v0.2 through Git history |
| v0.4 | 2026-07-23 | Reordered to Directory Rules, refreshed current workflows and validator inventory, surfaced compatibility lanes and ADR status, replaced placeholder ownership, preserved strong guidance and anchors, added no-loss/evidence/rollback registers | Restore blob `43c989a3bead8289bdbaba1a645980f95b0baf3a` |

<p align="right"><a href="#top">Back to top</a></p>
