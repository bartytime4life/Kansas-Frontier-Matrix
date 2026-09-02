<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-templates-readme
title: configs/templates/ — Configuration Templates
type: readme
version: v0.2
status: draft
owners: OWNER_TBD — Config steward · Docs steward
created: 2026-06-16
updated: 2026-07-13
policy_label: public
related:
  - ../README.md
  - ../examples/README.md
  - ../local/README.md
  - ../dev/README.md
  - ../../docs/doctrine/directory-rules.md
  - ../../schemas/contracts/v1/
  - ../../policy/
  - ../../apps/
  - ../../pipelines/
  - ../../pipeline_specs/
  - ../../runtime/
  - ../../infra/
tags: [kfm, configs, templates, defaults, governance]
notes:
  - "configs/templates/ is for commit-safe configuration templates only."
  - "Templates describe shape and placeholders; they do not prove runtime behavior."
  - "Authoritative schemas, policy rules, implementation code, lifecycle records, release records, and generated outputs belong in their own roots."
  - "Current tracked inventory is CONFIRMED at main commit 55a84f06216effd8e3ae5d51450bbf9f3d160417. Consumers, semantic adequacy, validation coverage, and CI enforcement remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Config Templates

`configs/templates/`

`configs/templates/` is a sublane under the canonical `configs/` root for commit-safe configuration templates.

Templates in this folder may show expected structure, placeholder fields, and intended consumers. They must not become schema authority, policy authority, runtime truth, release truth, lifecycle truth, implementation code, or generated-output authority.

> [!IMPORTANT]
> **Status:** draft / `NEEDS VERIFICATION`  
> **Owning root:** `configs/`  
> **Responsibility:** configuration templates only  
> **Truth posture:** README path and five template files CONFIRMED at `main@55a84f062…`; parent `configs/` root CONFIRMED as config home; consumers, semantic adequacy, validation coverage, and CI enforcement remain UNKNOWN / NEEDS VERIFICATION.

## Purpose

Use this folder for reusable configuration templates that are safe to commit and easy to review.

A template here does not prove that an app, package, pipeline, runtime adapter, policy gate, or release path works. Verify the relevant consumer, schema, contract, tests, and workflow before making behavior claims.

## Canonical fit

```text
configs/
└── templates/
    ├── README.md
    ├── dataset_manifest.template.yaml
    ├── layer_manifest.template.yaml
    ├── release_manifest.template.yaml
    ├── source_descriptor.template.yaml
    └── viewer_style.template.json
```

Related roots:

```text
configs/examples/  # sample config examples
configs/local/     # local setup templates and notes
configs/dev/       # development defaults and templates
schemas/           # machine-checkable shape
policy/            # admissibility rules
apps/              # deployable app code
pipelines/         # executable pipeline logic
pipeline_specs/    # durable pipeline definitions
runtime/           # runtime adapters
infra/             # operation controls
data/              # lifecycle records
release/           # release decisions
artifacts/         # generated outputs
```

## Allowed contents

| Allowed item | Example | Required posture |
|---|---|---|
| Generic config template | `base.template.yaml` | Commit-safe and placeholder-based |
| App template | `app.template.yaml` | Must identify intended app consumer |
| Pipeline template | `pipeline.template.yaml` | Must identify intended pipeline/spec consumer |
| Runtime template | `runtime.template.yaml` | Template only; not adapter code |
| Validation note | `validation.md` | Must point to tests/tools without overclaiming |

## Forbidden contents

| Do not store here | Correct home |
|---|---|
| App source | `apps/` |
| Pipeline logic | `pipelines/` |
| Durable pipeline definitions | `pipeline_specs/` |
| Runtime adapter code | `runtime/` |
| Operation control files | `infra/` |
| Schemas | `schemas/` |
| Policy rules | `policy/` |
| Lifecycle records, receipts, proofs, registry rows, or published artifacts | `data/` |
| Release decisions or rollback/correction records | `release/` |
| Generated outputs | `artifacts/` |
| Worked examples and walkthroughs | `examples/` |

## Current inventory and proposed expansion

The five template payloads shown below are `CONFIRMED` in the tracked tree. No verified runtime consumer or validator was found for them; `SKELETON_MAP.md` is a structural reference, not consumption evidence.

```text
configs/templates/
├── README.md
├── dataset_manifest.template.yaml
├── layer_manifest.template.yaml
├── release_manifest.template.yaml
├── source_descriptor.template.yaml
├── viewer_style.template.json
├── apps/                    # PROPOSED app templates
├── pipelines/               # PROPOSED pipeline templates
├── runtime/                 # PROPOSED runtime config templates
├── domains/                 # PROPOSED domain config templates
└── validation.md            # PROPOSED validation notes
```

> [!WARNING]
> Do not create the proposed subdirectories or `validation.md` without a verified consumer or validation responsibility.

## Validation expectations

Before relying on a template here, verify:

- the file is safe to commit;
- placeholders are used where customization is expected;
- the intended consumer is named;
- the relevant schema, contract, app, pipeline, runtime adapter, and tests are aligned;
- the file is not implementation code, a durable pipeline definition, lifecycle data, release state, or generated output.

## Migration posture

If misplaced material is found here:

1. Do not treat it as authoritative until reviewed.
2. Identify the owning root.
3. Move it through a small, reviewable migration.
4. Preserve necessary owner notes and rollback instructions.
5. Add a drift note if the misplaced template was already consumed.

## Safe change pattern

For changes under `configs/templates/`:

1. Confirm the file is a configuration template or config-facing documentation.
2. Confirm the template does not duplicate schema, policy, contract, release, or lifecycle authority.
3. Confirm implementation code belongs under the correct implementation root instead.
4. Confirm consumers and validators are updated or explicitly marked `NEEDS VERIFICATION`.
5. Update tests or explain why the change is documentation-only.

## Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [x] Actual tracked `configs/templates/` contents are inventoried at the pinned base.
- [ ] Templates identify consumers and validation paths.
- [ ] Misplaced files are migrated to the correct owning root.
- [ ] CI/review behavior is verified or marked `NEEDS VERIFICATION`.

## Status summary

`configs/templates/` contains five commit-safe template payloads plus this README. Their presence is confirmed; consumer binding and validation remain unverified. This lane is not a source of runtime truth, release truth, schema truth, policy truth, lifecycle truth, implementation truth, or generated-output authority.

<p align="right"><a href="#top">Back to top</a></p>
