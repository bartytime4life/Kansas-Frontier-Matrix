<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/configs-maplibre-readme
title: configs/maplibre/ — MapLibre Configuration Defaults and Templates
type: readme
version: v0.1
status: draft
owners: OWNER_TBD — Map steward · Config steward · UI steward · Ops steward · Docs steward
created: 2026-06-16
updated: 2026-06-16
policy_label: public
related:
  - ../README.md
  - ../../docs/architecture/maplibre.md
  - ../../docs/doctrine/directory-rules.md
  - ../../apps/explorer-web/
  - ../../packages/maplibre-runtime/
  - ../../schemas/contracts/v1/maplibre/
  - ../../schemas/contracts/v1/3d/
  - ../../policy/maplibre/
  - ../../data/published/
  - ../../release/
tags: [kfm, configs, maplibre, map, style, tiles, renderer, defaults, templates, governance]
notes:
  - "configs/maplibre/ is for commit-safe MapLibre configuration defaults and templates only."
  - "MapLibre renders governed/released artifacts; it is not the truth, policy, release, source, citation, or AI authority."
  - "Styles, layer lists, tile endpoints, and display defaults in this folder do not authorize publication or exposure."
  - "Specific current inventory, consumers, validation coverage, runtime wiring, and CI enforcement remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# MapLibre Configs

`configs/maplibre/`

`configs/maplibre/` is a sublane under the canonical `configs/` root for commit-safe MapLibre configuration defaults and templates.

It may describe local/default style configuration, layer toggles, viewport defaults, safe display options, and template placeholders for map clients. It must not become a source of truth, a publication decision point, a policy engine, a schema home, a released artifact home, or a runtime package.

> [!IMPORTANT]
> **Status:** draft / `NEEDS VERIFICATION`  
> **Owning root:** `configs/`  
> **Responsibility:** MapLibre configuration defaults and templates only  
> **Truth posture:** README path CONFIRMED; parent `configs/` root CONFIRMED as config home; MapLibre architecture lane CONFIRMED; current config inventory, consumers, runtime wiring, validation coverage, and CI enforcement remain UNKNOWN / NEEDS VERIFICATION.

> [!CAUTION]
> Map configuration does not decide what is true or what may be shown. Public map behavior must still use governed APIs, released artifacts, policy checks, evidence support, review state, and release state.

## Purpose

Use this folder for small, reviewable MapLibre configuration examples and templates that help maintainers understand map display defaults without placing implementation code, source data, released artifacts, or release decisions under `configs/`.

A file here does not prove that a viewer, API route, tile service, PMTiles path, style JSON, sprite, glyph set, or layer registry is working. Verify the relevant app, package, schema, policy, release record, tests, and generated artifacts before making behavior claims.

## Canonical fit

```text
configs/
└── maplibre/
    └── README.md
```

Related roots:

```text
apps/explorer-web/              # browser app surface, if present and verified
packages/maplibre-runtime/      # shared runtime helpers, if present and verified
schemas/contracts/v1/maplibre/  # machine-checkable MapLibre shapes, if present and verified
schemas/contracts/v1/3d/        # machine-checkable 3D shapes, if present and verified
policy/maplibre/                # admissibility/display rules, if present and verified
data/published/                 # released map artifacts
release/                        # release decisions and rollback/correction state
```

## Authority boundary

```text
configs/maplibre/
├── safe display defaults
├── placeholder-based map templates
├── local viewer config examples
└── validation notes for map config

NOT HERE:
  MapLibre app source
  runtime package code
  style/schema authority
  policy rules
  source data
  lifecycle data
  receipts/proofs
  release decisions
  released artifacts
  generated outputs
```

## MapLibre doctrine reminder

KFM MapLibre is a renderer and interaction runtime. It draws governed/released artifacts and may support receipts or representation checks, but it does not own truth, source authority, citation authority, policy authority, review authority, publication authority, or AI authority.

Configuration in this folder must preserve that boundary.

## Allowed contents

| Allowed item | Example | Required posture |
|---|---|---|
| Safe display defaults | viewport defaults, debug toggles | Must be safe to commit |
| Template files | `.example`, `.template` | Must use placeholders for local customization |
| Style references | pointer to a style file or artifact name | Must not claim release state unless verified |
| Layer toggle examples | local layer switch template | Must defer to governed APIs and release state |
| Validation notes | `validation.md` | Must point to tests/tools without overclaiming |

## Forbidden contents

| Do not store here | Correct home |
|---|---|
| Explorer web source code | `apps/explorer-web/` |
| Shared MapLibre runtime code | `packages/maplibre-runtime/` or accepted package home |
| Machine schemas | `schemas/contracts/v1/maplibre/` or `schemas/contracts/v1/3d/` |
| Policy rules and display decisions | `policy/maplibre/` or governed policy homes |
| Source data or lifecycle records | `data/` lifecycle subtrees |
| Receipts, proofs, registry rows, or published artifacts | `data/` owning subtrees |
| Release decisions or rollback/correction records | `release/` |
| Generated build/QA outputs | `artifacts/` |
| Runnable walkthroughs or larger examples | `examples/` |

## Suggested directory shape

Current inventory remains `NEEDS VERIFICATION`.

```text
configs/maplibre/
├── README.md
├── viewer.example.yaml       # PROPOSED local viewer template
├── style.example.json        # PROPOSED style-config example, not schema authority
├── layers.example.yaml       # PROPOSED layer toggle example
└── validation.md             # PROPOSED validation notes
```

> [!WARNING]
> Do not treat this suggested shape as repo fact. Verify actual files before making inventory or migration claims.

## Validation expectations

Before relying on a MapLibre config here, verify:

- the file is safe to commit;
- placeholders are used where local customization is expected;
- the intended consumer is named;
- the relevant app, package, schema, policy, release record, artifact, and tests are aligned;
- the file does not replace generated/released map artifacts;
- the file does not bypass governed API, evidence, policy, review, or release controls.

## Migration posture

If misplaced material is found here:

1. Do not treat it as authoritative until reviewed.
2. Identify the owning root.
3. Move it through a small, reviewable migration.
4. Preserve necessary owner notes and rollback instructions.
5. Add a drift note if the misplaced config was already consumed.

## Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [ ] Actual `configs/maplibre/` contents are inventoried.
- [ ] MapLibre config templates identify consumers and validation paths.
- [ ] No source data, lifecycle records, released artifacts, release records, policy rules, schemas, package code, app code, or generated outputs live here.
- [ ] Runtime, app, schema, policy, artifact, and test alignment is verified or marked `NEEDS VERIFICATION`.
- [ ] CI/review behavior is verified or marked `NEEDS VERIFICATION`.

## Status summary

`configs/maplibre/` is for commit-safe MapLibre configuration defaults and templates only. It is not a source of truth, release authority, schema authority, policy authority, app implementation, runtime package, lifecycle store, or generated-output home.

<p align="right"><a href="#top">Back to top</a></p>
