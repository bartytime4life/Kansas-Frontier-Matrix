<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-examples-readme
title: configs/examples/ — Configuration Example Templates
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Config steward · Docs steward
created: 2026-06-16
updated: 2026-06-16
policy_label: public
related:
  - ../README.md
  - ../../examples/README.md
  - ../../docs/doctrine/directory-rules.md
tags: [kfm, configs, examples, templates, governance]
notes:
  - "configs/examples/ is for commit-safe configuration examples and templates only."
  - "Worked examples belong under examples/."
  - "Current inventory and consumers remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Config Examples

`configs/examples/`

`configs/examples/` is a sublane under the canonical `configs/` root for commit-safe configuration examples and templates.

It is not the same as the root-level `examples/` folder. Root `examples/` is for walkthroughs and example assemblies. This folder is only for example configuration files and short notes about how to validate them.

> [!IMPORTANT]
> **Status:** draft / `NEEDS VERIFICATION`  
> **Owning root:** `configs/`  
> **Responsibility:** configuration examples and templates only  
> **Truth posture:** README path CONFIRMED; current inventory, consumers, validation coverage, and CI enforcement are UNKNOWN / NEEDS VERIFICATION.

## Purpose

Use this folder for small, reviewable configuration examples that help maintainers understand config shape and expected placeholders.

A file here does not prove runtime behavior. Verify the relevant app, package, pipeline, schema, and tests before making behavior claims.

## Canonical fit

```text
configs/
└── examples/
    └── README.md
```

Related roots:

```text
examples/      # worked examples and walkthroughs
apps/          # deployable app code
pipelines/     # executable pipeline logic
runtime/       # runtime adapters
infra/         # operation controls
schemas/       # machine-checkable shape
policy/        # admissibility rules
data/          # lifecycle records
release/       # release decisions
artifacts/     # generated outputs
```

## Allowed contents

| Allowed item | Example | Required posture |
|---|---|---|
| Config example | `default.example.yaml` | Commit-safe and placeholder-based |
| Template file | `.example`, `.template` | Must identify intended consumer |
| Validation note | `validation.md` | Must point to tests/tools without overclaiming |
| Migration note | `MIGRATION.md` | Temporary and review-linked |

## Forbidden contents

| Do not store here | Correct home |
|---|---|
| Walkthrough projects or larger examples | `examples/` |
| App source | `apps/` |
| Pipeline logic | `pipelines/` |
| Runtime adapter code | `runtime/` |
| Operation control files | `infra/` |
| Schemas | `schemas/` |
| Policy rules | `policy/` |
| Lifecycle records, receipts, proofs, registry rows, or published artifacts | `data/` |
| Release decisions or rollback/correction records | `release/` |
| Generated outputs | `artifacts/` |

## Validation expectations

Before relying on an example here, verify:

- the file is commit-safe;
- placeholders are used where local customization is expected;
- the intended consumer is named;
- the relevant schema, contract, app, pipeline, runtime adapter, and tests are aligned;
- the example is not a runnable walkthrough that belongs under `examples/`.

## Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [ ] Actual `configs/examples/` contents are inventoried.
- [ ] Examples identify consumers and validation paths.
- [ ] Misplaced files are migrated to the correct owning root.
- [ ] CI/review behavior is verified or marked `NEEDS VERIFICATION`.

## Status summary

`configs/examples/` is for commit-safe configuration examples and templates only. It is not a source of runtime truth, release truth, schema truth, policy truth, lifecycle truth, or worked-example authority.

<p align="right"><a href="#top">Back to top</a></p>
