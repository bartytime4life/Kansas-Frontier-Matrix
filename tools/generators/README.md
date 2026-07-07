<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-generators-readme
title: tools/generators README
type: README
version: v0.1
status: draft
owner: TODO-tooling-qa-owner
created: 2026-07-07
updated: 2026-07-07
policy_label: public
owning_root: tools/
responsibility: deterministic repo-wide generators and scaffolders for governed KFM artifacts
truth_posture: cite-or-abstain; implementation claims require current repo evidence
related:
  - ../README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/registers/VERIFICATION_BACKLOG.md
  - ../../schemas/contracts/v1/README.md
  - ../../contracts/README.md
  - ../../tests/generators/README.md
notes:
  - "This README defines the governed boundary for generator helpers under tools/generators/."
  - "Generators may scaffold candidate files or derived artifacts, but they do not decide truth, policy, review state, release state, or publication."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# tools/generators

![status](https://img.shields.io/badge/status-draft-orange)
![root](https://img.shields.io/badge/root-tools%2F-blue)
![scope](https://img.shields.io/badge/scope-deterministic--generators-informational)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)
![side--effects](https://img.shields.io/badge/write--mode-explicit--only-lightgrey)

> **One-line purpose.** `tools/generators/` owns deterministic, reviewable helper programs that scaffold or derive KFM files from governed inputs. A generator may create a candidate artifact, but it never makes that artifact authoritative, reviewed, released, published, or true.

---

## Quick jump

- [Purpose](#purpose)
- [Status](#status)
- [Governance boundary](#governance-boundary)
- [What belongs here](#what-belongs-here)
- [What does not belong here](#what-does-not-belong-here)
- [Generator contract](#generator-contract)
- [Inputs and outputs](#inputs-and-outputs)
- [Suggested generator families](#suggested-generator-families)
- [Validation](#validation)
- [Review checklist](#review-checklist)
- [Roadmap](#roadmap)

---

## Purpose

`tools/generators/` is the repo-wide home for durable generator and scaffolding helpers used by maintainers, CI, or governed workflows.

A generator is appropriate here when it creates deterministic files or reports from explicit inputs, such as schemas, contracts, manifests, source descriptors, domain templates, catalog stubs, fixture packs, release dry-run inputs, or documentation inventories.

The lane exists to reduce manual drift while preserving KFM governance:

1. Generate repeatable outputs.
2. Make assumptions explicit.
3. Keep generated files reviewable.
4. Avoid hidden network access.
5. Emit reports that explain what changed.
6. Leave authority decisions to the owning roots and reviewers.

[Back to top](#top)

---

## Status

| Surface | Status | Notes |
|---|---|---|
| `tools/generators/README.md` | **CONFIRMED** | This README defines the generator lane boundary. |
| Generator helper scripts | **NEEDS VERIFICATION** | Confirm current branch contents before naming specific executables as implemented. |
| ID generation | **PROPOSED** | Useful first-slice family for deterministic IDs, but must be tied to a documented namespace rule. |
| Source descriptor scaffolding | **PROPOSED** | Should create candidates only; source acceptance remains a governed review decision. |
| Schema-driven scaffolding | **PROPOSED** | Must not redefine schemas or contracts. |
| Docs index generation | **PROPOSED** | May support docs review but does not become documentation authority. |
| Publication authority | **DENY here** | Generators do not publish or promote artifacts. |

> [!IMPORTANT]
> A generated file is a candidate or derived artifact until it passes its owning validation, review, policy, release, and rollback controls. Generated output is not sovereign truth.

[Back to top](#top)

---

## Governance boundary

KFM's lifecycle invariant remains unchanged:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Generators may help create files that participate in that lifecycle, but they must not silently move information across lifecycle states. Promotion remains a governed state transition, not a file creation event.

### Allowed questions

`tools/generators/` may help answer:

- Can this source descriptor scaffold be created with required placeholder fields?
- Can this domain README template be generated with KFM metadata and warning blocks?
- Can this catalog stub be emitted from validated processed metadata?
- Can this fixture pack be created for a validator test?
- Can a deterministic ID candidate be derived from a documented namespace and stable inputs?
- Can a docs or schema index be regenerated for review?

### Disallowed questions

`tools/generators/` must not decide:

- Is this source admissible?
- Is this evidence sufficient?
- Is this claim true?
- Is this schema accepted?
- Is this policy correct?
- Is this file ready to publish?
- Should this release be promoted?
- Is this generated public payload safe to expose?

Those decisions belong to source stewards, contracts, schemas, policy, validators, review state, release state, receipts, proofs, and rollback targets.

[Back to top](#top)

---

## What belongs here

Good fits for `tools/generators/` include:

- deterministic ID candidate generators;
- source descriptor scaffolders;
- README scaffolders that produce draft files with KFM metadata blocks;
- domain-lane template generators;
- fixture pack generators for tests;
- schema-aware example payload generators;
- catalog stub generators from validated local inputs;
- documentation index builders when they produce derived inventories;
- release dry-run input scaffolds;
- manifest skeleton builders that leave final release authority to `release/` workflows;
- code or config scaffolds derived from accepted contracts and schemas.

A generator belongs here only when it is:

- repo-wide rather than a one-off script;
- deterministic under the same inputs;
- explicit about read paths and write paths;
- safe to run without network access by default;
- conservative about overwriting existing files;
- documented with a dry-run mode;
- tested with public-safe fixtures;
- clear about whether it emits candidates, derived artifacts, reports, or templates.

[Back to top](#top)

---

## What does not belong here

| Do not put in `tools/generators/` | Correct home | Reason |
|---|---|---|
| One-off cleanup scripts | `scripts/one_off/` or `scripts/maintenance/` | Only durable repo-wide generation belongs here. |
| Pipeline orchestration | `pipelines/` | Pipelines decide how steps run; generators are callable steps. |
| Pipeline configuration | `pipeline_specs/` | Declarative run specs are not executable generator code. |
| Reusable libraries imported by apps | `packages/` | Shared runtime libraries should not live in tooling. |
| Source-specific harvesters | `connectors/<source>/` | Source acquisition is connector responsibility. |
| Policy rules | `policy/` | Generators must not embed policy authority. |
| Contract definitions | `contracts/` | Object-family meaning belongs in contracts. |
| JSON Schemas | `schemas/contracts/v1/...` | Field-level shape belongs in schema home. |
| Generated receipts or proofs | `data/receipts/`, `data/proofs/` | Trust artifacts belong in lifecycle roots. |
| Release manifests or rollback cards | `release/` | Release records and rollback targets are not generator code. |
| Tests | `tests/generators/` or existing test convention | Tests prove generators; they are not generators. |
| Fixtures | `fixtures/` or `tests/generators/fixtures/` | Fixture data should be separate from tool code. |
| Public client runtime output | governed API / release artifact homes | Public outputs must pass release and policy gates. |

[Back to top](#top)

---

## Generator contract

Every durable generator should document the following before it becomes part of CI or steward workflows.

| Field | Requirement |
|---|---|
| Inputs | Explicit local files, directories, schemas, contracts, or manifests. |
| Outputs | Explicit output path, report path, or stdout behavior. |
| Dry run | Required for generators that would write files. |
| Overwrite behavior | Deny overwrite by default unless `--force` or an equivalent explicit flag is used. |
| Network | Off by default. Network use requires explicit opt-in and source rationale. |
| Determinism | Same inputs should produce byte-stable or semantically stable output. |
| Report | Emit a machine-readable summary when practical. |
| Validation | State which validator or test should be run after generation. |
| Authority label | Mark outputs as `PROPOSED`, `DRAFT`, `CANDIDATE`, or equivalent unless a separate process promotes them. |
| Sensitive data | Do not generate public examples using real sensitive, private, living-person, DNA, archaeology, rare-species, or infrastructure-risk details. |

Recommended finite statuses for generator reports:

| Status | Meaning |
|---|---|
| `generated` | Candidate output was created. |
| `unchanged` | Existing output already matched expected content. |
| `would_change` | Dry run found changes but did not write. |
| `skipped` | Generator intentionally skipped a target with a documented reason. |
| `blocked` | Generator refused to overwrite or write unsafe output. |
| `error` | Generator could not safely complete. |

[Back to top](#top)

---

## Inputs and outputs

### Suitable inputs

- accepted schemas;
- accepted contracts;
- documented namespace rules;
- source registry metadata;
- validated processed metadata;
- public-safe fixture seeds;
- docs inventories;
- template files;
- release dry-run inputs;
- local manifest files.

### Unsuitable inputs

- credentials or secrets;
- raw source dumps not cleared for processing;
- living-person records;
- DNA or genomic data;
- exact sensitive archaeology locations;
- exact rare-species locations;
- unrestricted infrastructure-risk details;
- unpublished public-client payloads outside their review workflow.

### Suitable outputs

- draft README files;
- source descriptor candidates;
- domain-lane scaffolds;
- fixture packs;
- schema examples;
- catalog stubs;
- manifest skeletons;
- deterministic docs indexes;
- generator run reports.

Generated outputs should include placeholders where owner, reviewer, source-rights, sensitivity, policy, or release status is unknown. Do not invent these fields.

[Back to top](#top)

---

## Suggested generator families

| Helper family | Proposed path | Purpose | Status |
|---|---|---|---|
| ID candidate generator | `tools/generators/generate_id.py` | Derive deterministic ID candidates from documented namespace inputs. | **PROPOSED** |
| Source descriptor scaffolder | `tools/generators/scaffold_source_descriptor.py` | Create draft source descriptor records with required placeholders. | **PROPOSED** |
| README scaffolder | `tools/generators/scaffold_readme.py` | Emit KFM README skeletons with metadata, truth posture, and review checklist. | **PROPOSED** |
| Fixture pack generator | `tools/generators/generate_fixture_pack.py` | Create public-safe valid/invalid fixtures for validator tests. | **PROPOSED** |
| Schema example generator | `tools/generators/generate_schema_examples.py` | Produce example JSON from accepted schema surfaces. | **PROPOSED** |
| Catalog stub generator | `tools/generators/generate_catalog_stub.py` | Create candidate catalog records from validated local metadata. | **PROPOSED** |
| Docs index generator | `tools/generators/generate_docs_index.py` | Create a deterministic documentation inventory for review. | **PROPOSED** |

> [!NOTE]
> These names are recommended first-slice targets, not proof of current implementation. Confirm file presence on the active branch before invoking them.

[Back to top](#top)

---

## Validation

The first useful proof surface should be fixture-backed and side-effect safe.

Recommended structure:

```text
tests/generators/
├── README.md
├── test_scaffold_readme.py
├── test_generate_id.py
└── fixtures/
    ├── readme_expected.md
    ├── source_descriptor_seed.json
    ├── namespace_inputs.json
    └── unsafe_sensitive_seed.json
```

Recommended assertions:

- dry run reports `would_change` without writing output;
- existing matching output reports `unchanged`;
- overwrite is denied without explicit force;
- deterministic inputs produce stable output;
- unknown owner/reviewer/source-rights fields remain placeholders;
- unsafe sensitive fixture seeds are blocked or redacted according to the helper contract;
- generated files include `PROPOSED`, `DRAFT`, or `NEEDS VERIFICATION` labels where implementation evidence is absent;
- generated outputs are validated by the appropriate downstream checker.

Suggested future command pattern:

```bash
pytest -q tests/generators
```

```bash
python tools/generators/scaffold_readme.py \
  --path tools/example/README.md \
  --title "tools/example" \
  --dry-run
```

[Back to top](#top)

---

## Review checklist

Before adding or changing a generator, reviewers should confirm:

- [ ] The generator has a narrow, documented purpose.
- [ ] It has dry-run mode for write operations.
- [ ] It denies overwrite by default.
- [ ] It is deterministic under the same inputs.
- [ ] It does not use network access by default.
- [ ] It does not invent owners, reviewers, rights, evidence, or release state.
- [ ] It labels candidate outputs honestly.
- [ ] It does not redefine contracts, schemas, policy, doctrine, or release authority.
- [ ] Public-safe fixtures cover normal, unchanged, overwrite-blocked, malformed, and unsafe-sensitive cases.
- [ ] Generated output has an identified downstream validation path.
- [ ] Any generated trust-adjacent output is reviewed before being used in promotion or publication.

[Back to top](#top)

---

## Roadmap

| Step | Status | Outcome |
|---|---|---|
| Replace greenfield stub with lane contract | **DONE in this README** | Establishes generator boundaries and first-slice expectations. |
| Add README scaffolder | **PROPOSED** | Produces KFM-style README candidates with honest labels. |
| Add deterministic ID candidate generator | **PROPOSED** | Supports stable namespace workflows after namespace rules are confirmed. |
| Add source descriptor scaffolder | **PROPOSED** | Creates candidates for source steward review. |
| Add generator fixture tests | **PROPOSED** | Proves dry-run, overwrite, determinism, and unsafe-seed behavior. |
| Wire selected generators into CI as non-blocking reports | **PROPOSED / later** | Generates reviewer-visible candidate reports without automatic publication. |

[Back to top](#top)

---

## Last reviewed

| Field | Value |
|---|---|
| Last reviewed | 2026-07-07 |
| Review state | Draft README replacement for existing greenfield stub. |
| Next smallest safe change | Add `tools/generators/scaffold_readme.py` plus public-safe `tests/generators/` fixtures. |
