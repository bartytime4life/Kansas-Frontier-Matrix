<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-local-readme
title: configs/local/ — Local Configuration Templates
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Config steward · Developer-experience steward · Ops steward · Docs steward
created: 2026-06-16
updated: 2026-06-16
policy_label: public
related:
  - ../README.md
  - ../dev/README.md
  - ../examples/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../apps/README.md
  - ../../pipelines/README.md
  - ../../pipeline_specs/README.md
  - ../../runtime/README.md
  - ../../infra/README.md
  - ../../tests/README.md
  - ../../tools/README.md
tags: [kfm, configs, local, templates, development, validation, governance]
notes:
  - "configs/local/ is for commit-safe local configuration templates and notes only."
  - "Personal or machine-specific overrides should remain outside the committed repo."
  - "This folder does not prove local runtime behavior, deployment behavior, or CI enforcement."
  - "Specific current inventory, consumers, validation coverage, and owner assignments remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Local Configs

`configs/local/`

`configs/local/` is a sublane under the canonical `configs/` root for commit-safe local configuration templates and notes.

It exists to help contributors understand how local configuration may be shaped without turning local override material into repo authority.

> [!IMPORTANT]
> **Status:** draft / `NEEDS VERIFICATION`  
> **Owning root:** `configs/`  
> **Responsibility:** local configuration templates and notes only  
> **Truth posture:** README path CONFIRMED; current local config inventory, consumers, validation coverage, and CI enforcement are UNKNOWN / NEEDS VERIFICATION.

> [!CAUTION]
> A local config template is not operational proof. Do not cite a file in `configs/local/` as evidence that an app, pipeline, runtime adapter, policy gate, or release path works. Verify consumers, schemas, tests, and workflows before making behavior claims.

## Purpose

Use this folder for small, reviewable local configuration templates that explain expected config shape, placeholders, and local setup boundaries.

This folder should not store authoritative records, lifecycle data, release decisions, policy rules, schemas, source code, runtime adapters, or generated output.

## Canonical fit

```text
configs/
└── local/
    └── README.md
```

Related roots:

```text
configs/dev/       # development defaults and templates
configs/examples/  # example configuration files
apps/              # deployable app code
pipelines/         # executable pipeline logic
pipeline_specs/    # durable pipeline definitions
runtime/           # runtime adapters
infra/             # operation controls
schemas/           # machine-checkable shape
policy/            # admissibility rules
data/              # lifecycle records
release/           # release decisions
artifacts/         # generated outputs
```

## Allowed contents

| Allowed item | Example | Required posture |
|---|---|---|
| Local template | `local.example.yaml` | Commit-safe and placeholder-based |
| Setup note | `README.md`, `validation.md` | Must avoid behavior claims unless verified |
| Consumer note | app/pipeline/runtime reference | Must name the intended consumer |
| Migration note | renamed local config fields | Temporary and review-linked |

## Forbidden contents

| Do not store here | Correct home |
|---|---|
| App source | `apps/` |
| Pipeline logic | `pipelines/` |
| Runtime adapter code | `runtime/` |
| Operation control files | `infra/` |
| Schemas | `schemas/` |
| Policy rules | `policy/` |
| Lifecycle records, receipts, proofs, registry rows, or published artifacts | `data/` |
| Release decisions or rollback/correction records | `release/` |
| Generated outputs | `artifacts/` |
| Worked examples and walkthroughs | `examples/` |

## Validation expectations

Before relying on a local config template, verify:

- the file is safe to commit;
- placeholders are used where local customization is expected;
- the intended consumer is named;
- the relevant schema, contract, app, pipeline, runtime adapter, and tests are aligned;
- the file is not a worked example, lifecycle record, or generated output.

## Migration posture

If misplaced material is found here:

1. Do not treat it as authoritative until reviewed.
2. Identify the owning root.
3. Move it through a small, reviewable migration.
4. Preserve necessary owner notes and rollback instructions.
5. Add a drift note if the misplaced local config was already consumed.

## Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [ ] Actual `configs/local/` contents are inventoried.
- [ ] Local templates identify consumers and validation paths.
- [ ] Misplaced files are migrated to the correct owning root.
- [ ] CI/review behavior is verified or marked `NEEDS VERIFICATION`.

## Status summary

`configs/local/` is for commit-safe local configuration templates and notes only. It is not a source of runtime truth, release truth, schema truth, policy truth, lifecycle truth, implementation truth, or generated-output authority.

<p align="right"><a href="#top">Back to top</a></p>
