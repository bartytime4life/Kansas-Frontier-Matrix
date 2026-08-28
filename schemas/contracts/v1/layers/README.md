# `schemas/contracts/v1/layers/` — Layer Schema Family Index

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-layers-readme
title: schemas/contracts/v1/layers/ — Layer Schema Family Index
type: readme; schema-family-index; layer-schema-boundary; map-publication-guardrail
authority_class: schema-family-index
version: v0.1
status: draft; layer-family-present; PROPOSED scaffolds present; domain-layer-profiles-present; release-gated; no-parallel-authority; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Layer steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Map/UI steward
  - OWNER_TBD — Domain stewards for affected domains
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Docs steward
created: NEEDS VERIFICATION — empty README existed before v0.1 expansion
updated: 2026-07-04
policy_label: public; schemas; contracts-v1; layers; map-layers; layer-manifest; layer-descriptor; layer-catalog-item; domain-profiles; evidence-bound; policy-aware; release-gated; rollback-aware; no-parallel-authority
tags: [kfm, schemas, contracts, v1, layers, layer-manifest, layer-descriptor, layer-catalog-item, maplibre, map-ui, evidence-drawer, domain-layer-profiles, release, rollback, no-parallel-authority]
related:
  - ../README.md
  - ../domains/README.md
  - ./layer_manifest.schema.json
  - ./layer_descriptor.schema.json
  - ./layer_catalog_item.schema.json
  - ./layer_descriptor.fauna-profile.example.json
  - ../domains/agriculture/layer_manifest.schema.json
  - ../domains/archaeology/layer_manifest.schema.json
  - ../domains/atmosphere/layer_manifest.schema.json
  - ../domains/fauna/layer_manifest.schema.json
  - ../domains/flora/layer_manifest.schema.json
  - ../domains/geology/layer_manifest.schema.json
  - ../domains/habitat/layer_manifest.schema.json
  - ../domains/hazards/layer_manifest.schema.json
  - ../domains/hydrology/layer_manifest.schema.json
  - ../domains/people-dna-land/layer_manifest.schema.json
  - ../domains/roads-rail-trade/layer_manifest.schema.json
  - ../domains/settlements-infrastructure/layer_manifest.schema.json
  - ../domains/soil/layer_manifest.schema.json
  - ../../../../contracts/
  - ../../../../docs/domains/
  - ../../../../docs/architecture/
  - ../../../../policy/
  - ../../../../fixtures/
  - ../../../../tests/
  - ../../../../release/
notes:
  - "Expanded from an empty file at schemas/contracts/v1/layers/README.md."
  - "Current search surfaced layer_manifest.schema.json, layer_descriptor.schema.json, layer_catalog_item.schema.json, and layer_descriptor.fauna-profile.example.json under this folder."
  - "Opened layer schemas are PROPOSED scaffolds with empty properties and additionalProperties true; schema maturity remains NEEDS VERIFICATION."
  - "Search also surfaced many domain-specific layer_manifest.schema.json files under schemas/contracts/v1/domains/<domain>/, so shared layer shapes and domain profiles must not drift into parallel authority."
  - "This folder defines machine-checkable layer object shapes only; it is not a tile store, map runtime, publication record, policy decision, or public-safe exposure authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![family](https://img.shields.io/badge/family-layers-teal)
![authority](https://img.shields.io/badge/authority-machine--shape-informational)
![maturity](https://img.shields.io/badge/maturity-PROPOSED-orange)
![release](https://img.shields.io/badge/release-gated-critical)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **Purpose.** `schemas/contracts/v1/layers/` is the shared schema family for machine-checkable layer objects: layer manifests, layer descriptors, and layer catalog items used to describe governed map/display surfaces.
>
> **One-line boundary.** Layer schemas define object shape only. They do not publish tiles, authorize public display, prove evidence closure, decide sensitivity, replace domain schemas, or act as release records.

---

## Quick jumps

[Status](#status) · [Authority and placement](#authority-and-placement) · [Repo fit](#repo-fit) · [Current inventory](#current-inventory) · [Domain layer profile surfaces](#domain-layer-profile-surfaces) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Layer-family rules](#layer-family-rules) · [Promotion checklist](#promotion-checklist) · [Validation](#validation) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

| Question | Answer | Truth label |
|---|---|---|
| Does this README path exist? | Yes: `schemas/contracts/v1/layers/README.md`. It was empty before this expansion. | **CONFIRMED** |
| Does this folder contain layer schema files? | Yes. Search surfaced `layer_manifest.schema.json`, `layer_descriptor.schema.json`, and `layer_catalog_item.schema.json`. | **CONFIRMED path evidence** |
| Are these schemas mature? | Not proven. Opened files are PROPOSED scaffolds with empty `properties` and `additionalProperties: true`. | **CONFIRMED scaffold / NEEDS VERIFICATION** |
| Does this folder contain an example? | Yes. `layer_descriptor.fauna-profile.example.json` was opened as a PROPOSED placeholder example. | **CONFIRMED** |
| Are domain layer profiles present elsewhere? | Yes. Search surfaced many `layer_manifest.schema.json` files under domain schema lanes. | **CONFIRMED path evidence / search-limited** |
| Can this folder store map tiles, released layer payloads, catalog records, or public artifacts? | No. This is a schema family folder, not a data, release, publication, tile, or UI runtime root. | **CONFIRMED boundary** |

> [!IMPORTANT]
> A layer manifest or descriptor is not the layer itself. It can describe how a governed layer should be identified, cited, styled, filtered, exposed, and related to evidence/release records, but it does not publish the layer or make it public-safe by itself.

---

## Authority and placement

This folder belongs under the schema responsibility root:

```text
schemas/contracts/v1/layers/
```

It may define shared layer-family shapes when the following are clear:

- which semantic contract explains the layer object meaning;
- whether the object is a shared layer shape or a domain-specific profile;
- whether domain `layer_manifest` schemas are `$ref` profiles, copies, or unresolved scaffolds;
- which evidence, policy, sensitivity, release, correction, and rollback references are required;
- which fixtures and validators prove expected behavior;
- which API/UI/MapLibre consumers are allowed to rely on the shape.

Adjacent authority remains separate:

- `schemas/contracts/v1/domains/<domain>/` owns domain-specific layer profiles and domain object shapes.
- `contracts/` owns semantic meaning.
- `policy/` owns allow/deny/restrict/abstain posture and exposure rules.
- `fixtures/` and `tests/` prove valid/invalid examples and validator behavior.
- `data/` owns lifecycle records, registries, receipts, proofs, catalog/triplet records, and published data products where applicable.
- `release/` owns promotion, release, correction, withdrawal, and rollback records.
- UI/API/MapLibre code renders released/public-safe payloads; it is not owned by this folder.

---

## Repo fit

```text
schemas/
└── contracts/
    └── v1/
        ├── README.md
        ├── layers/
        │   ├── README.md                                  # this file
        │   ├── layer_manifest.schema.json                 # PROPOSED scaffold
        │   ├── layer_descriptor.schema.json               # PROPOSED scaffold
        │   ├── layer_catalog_item.schema.json             # PROPOSED scaffold
        │   └── layer_descriptor.fauna-profile.example.json
        └── domains/
            ├── agriculture/layer_manifest.schema.json
            ├── archaeology/layer_manifest.schema.json
            ├── atmosphere/layer_manifest.schema.json
            ├── fauna/layer_manifest.schema.json
            ├── flora/layer_manifest.schema.json
            ├── geology/layer_manifest.schema.json
            ├── habitat/layer_manifest.schema.json
            ├── hazards/layer_manifest.schema.json
            ├── hydrology/layer_manifest.schema.json
            ├── people-dna-land/layer_manifest.schema.json
            ├── roads-rail-trade/layer_manifest.schema.json
            ├── settlements-infrastructure/layer_manifest.schema.json
            └── soil/layer_manifest.schema.json

contracts/
policy/
fixtures/
tests/
data/
release/
```

---

## Current inventory

| Path | Kind | Current posture | Notes |
|---|---|---|---|
| `README.md` | README | **CONFIRMED present** | Parent layer schema family index. |
| `layer_manifest.schema.json` | JSON Schema | **PROPOSED scaffold** | Draft 2020-12 object; `$id` is `kfm://schemas/contracts/v1/layers/layer_manifest.schema.json`; empty `properties`; `additionalProperties: true`; source docs include Agriculture, Archaeology, Fauna, and Hydrology map/UI docs. |
| `layer_descriptor.schema.json` | JSON Schema | **PROPOSED scaffold** | Draft 2020-12 object; `$id` is `kfm://schemas/contracts/v1/layers/layer_descriptor.schema.json`; empty `properties`; `additionalProperties: true`; source docs include Archaeology and Fauna map/UI docs. |
| `layer_catalog_item.schema.json` | JSON Schema | **PROPOSED scaffold** | Draft 2020-12 object; `$id` is `kfm://schemas/contracts/v1/layers/layer_catalog_item.schema.json`; empty `properties`; `additionalProperties: true`; source docs include Archaeology map/UI docs. |
| `layer_descriptor.fauna-profile.example.json` | Example JSON | **PROPOSED placeholder** | Placeholder profile example sourced from Fauna map/UI contract docs; not a validating schema and not release authority. |

---

## Domain layer profile surfaces

Current search surfaced the following domain-level layer manifest schema paths. This is a search-derived inventory, not proof that these schemas are field-complete or intentionally profiled against the shared layer family.

| Domain path | Posture |
|---|---|
| `schemas/contracts/v1/domains/agriculture/layer_manifest.schema.json` | **NEEDS VERIFICATION** |
| `schemas/contracts/v1/domains/archaeology/layer_manifest.schema.json` | **NEEDS VERIFICATION** |
| `schemas/contracts/v1/domains/atmosphere/layer_manifest.schema.json` | **NEEDS VERIFICATION** |
| `schemas/contracts/v1/domains/fauna/layer_manifest.schema.json` | **NEEDS VERIFICATION** |
| `schemas/contracts/v1/domains/flora/layer_manifest.schema.json` | **NEEDS VERIFICATION** |
| `schemas/contracts/v1/domains/geology/layer_manifest.schema.json` | **NEEDS VERIFICATION** |
| `schemas/contracts/v1/domains/geology/geology_layer_manifest.schema.json` | **NEEDS VERIFICATION / possible duplicate or domain-specific profile** |
| `schemas/contracts/v1/domains/habitat/layer_manifest.schema.json` | **NEEDS VERIFICATION** |
| `schemas/contracts/v1/domains/hazards/layer_manifest.schema.json` | **NEEDS VERIFICATION** |
| `schemas/contracts/v1/domains/hydrology/layer_manifest.schema.json` | **NEEDS VERIFICATION** |
| `schemas/contracts/v1/domains/people-dna-land/layer_manifest.schema.json` | **NEEDS VERIFICATION / sensitivity-sensitive** |
| `schemas/contracts/v1/domains/roads-rail-trade/layer_manifest.schema.json` | **NEEDS VERIFICATION** |
| `schemas/contracts/v1/domains/settlements-infrastructure/layer_manifest.schema.json` | **NEEDS VERIFICATION** |
| `schemas/contracts/v1/domains/soil/layer_manifest.schema.json` | **NEEDS VERIFICATION** |

> [!CAUTION]
> Shared `layers/` schemas and domain `layer_manifest` schemas need a profile or `$ref` strategy before promotion. Do not let the same layer manifest meaning drift across shared and domain-specific schema homes.

---

## What belongs here

- This README.
- Shared layer-family JSON Schema files such as `layer_manifest`, `layer_descriptor`, and `layer_catalog_item`.
- Shared examples that are clearly marked as examples and not release records.
- Profile notes explaining how domain `layer_manifest` schemas relate to shared layer shapes.
- Links to paired contracts, fixtures, validators, policy references, evidence references, release references, correction references, and rollback references.
- Migration notes if shared and domain layer schemas are consolidated, profiled, or renamed.

---

## What does not belong here

- Domain-owned canonical schemas except shared layer-family shapes.
- Semantic contract prose beyond README boundary notes.
- Policy rules, sensitivity decisions, exposure decisions, or release decisions.
- Source data, lifecycle data, emitted layer records, map tiles, vector tiles, raster tiles, catalog records, triplets, receipt instances, proof outputs, release records, correction notices, rollback cards, public map artifacts, dashboards, screenshots, or generated summaries.
- Validator code, packages, pipelines, runtime code, or UI/API/MapLibre implementation.
- Claims that a layer is valid, complete, evidence-backed, policy-safe, release-approved, or public-ready merely because it validates against a schema.

---

## Layer-family rules

| Rule | Requirement |
|---|---|
| Shape is not publication | A layer schema constrains an object shape; it does not publish a layer. |
| Domain truth stays separate | Layer records should reference domain-owned objects, evidence, and release records rather than becoming domain truth. |
| Evidence must be explicit | Layer objects that carry claims should resolve EvidenceRef to EvidenceBundle or equivalent support. |
| Policy must be explicit | Layer objects intended for public or semi-public use need policy and sensitivity posture. |
| Release must be explicit | Public layer payloads need release state, correction path, and rollback target support. |
| Style is not evidence | A style, paint rule, or MapLibre source definition is not evidence for the underlying claim. |
| Tiles are not canonical truth | Vector/raster tiles are derived/publication surfaces, not canonical source records. |
| Profiles must not drift | Domain `layer_manifest` schemas should either `$ref` shared layer shapes or document why they intentionally differ. |
| Examples are not fixtures unless declared | Example JSON files are illustrative until promoted into validated fixtures. |

---

## Promotion checklist

A layer schema or profile should not advance beyond `PROPOSED` unless:

- [ ] Paired semantic contract exists.
- [ ] Shared-vs-domain profile strategy is documented.
- [ ] `$id` is stable and follows the accepted namespace convention.
- [ ] Required fields are defined.
- [ ] Evidence references are defined where claims depend on evidence.
- [ ] Policy and sensitivity fields are defined where exposure matters.
- [ ] Release/correction/rollback references are defined for public use.
- [ ] Valid fixtures exist.
- [ ] Invalid fixtures exist.
- [ ] Public-safe and restricted examples exist where needed.
- [ ] Validators exist.
- [ ] CI/schema-test coverage exists.
- [ ] API/UI/MapLibre consumers are documented without bypassing governed release paths.
- [ ] Migration notes exist for any duplicate shared/domain layer schemas.

---

## Validation

Recommended local validation sequence:

```bash
# Inspect the shared layer schema family.
find schemas/contracts/v1/layers -maxdepth 3 -type f | sort

# Inspect domain layer manifest profiles.
find schemas/contracts/v1/domains -maxdepth 3 -type f \
  | grep -Ei '/layer_manifest\.schema\.json$|/.*layer.*manifest.*\.schema\.json$' \
  | sort

# Detect potential shared/domain layer drift.
find schemas/contracts/v1 -maxdepth 6 -type f \
  | grep -Ei 'layer_manifest|layer_descriptor|layer_catalog|map_ui|maplibre|evidence_drawer' \
  | sort

# Validate JSON syntax for layer schemas and examples.
find schemas/contracts/v1/layers -name '*.json' -print0 \
  | xargs -0 -r -I{} python -m json.tool {} >/dev/null

# Validate JSON syntax for domain layer manifests.
find schemas/contracts/v1/domains -name '*layer*manifest*.schema.json' -print0 \
  | xargs -0 -r -I{} python -m json.tool {} >/dev/null

# Run project validators when available.
python tools/validate_all.py || true
pytest tests/schemas tests/contract tests/policy tests/release || true
```

Replace `|| true` with fail-closed CI behavior once validator and test paths are confirmed.

---

## Rollback

Rollback for this README is ordinary Git rollback: revert the commit that changed `schemas/contracts/v1/layers/README.md`.

Rollback for future layer schema changes requires checking every downstream reference:

1. Revert or migrate schema files.
2. Restore canonical `$id` and `$ref` targets.
3. Restore paired contract links.
4. Restore fixtures, validators, schema registry records, and CI paths.
5. Restore domain, policy, evidence, release, correction, and receipt references.
6. Restore API/UI/MapLibre/Evidence Drawer consumers.
7. Preserve correction and rollback records if any public layer surface was affected.

---

## Open questions

| Question | Status | Owner |
|---|---|---|
| Should domain `layer_manifest` schemas `$ref` the shared `layers/layer_manifest.schema.json`, or remain independent profiles? | **NEEDS VERIFICATION / ADR-sensitive** | Layer steward + Schema steward + domain stewards |
| Which semantic contract owns `LayerManifest`, `LayerDescriptor`, and `LayerCatalogItem` meaning? | **NEEDS VERIFICATION** | Contract steward + Map/UI steward |
| Should examples under `schemas/contracts/v1/layers/` move to `fixtures/` once validation is wired? | **NEEDS VERIFICATION** | Validation steward |
| Which fields are mandatory for public-safe layer exposure? | **NEEDS VERIFICATION / policy-sensitive** | Policy steward + Release steward |
| Which MapLibre/API/Evidence Drawer consumers rely on these shapes? | **NEEDS VERIFICATION** | Map/UI steward + API steward |
| How should layer schema versions align with release manifests, catalog records, and rollback cards? | **NEEDS VERIFICATION / release-sensitive** | Release steward + Schema steward |

---

## Maintainer notes

- Keep this folder focused on shared layer object shapes, not actual map layer artifacts.
- Treat current schemas as PROPOSED scaffolds until fields, contracts, fixtures, validators, and release gates are verified.
- Prevent drift between shared `layers/` schemas and domain `layer_manifest` profiles.
- Preserve evidence, sensitivity, domain ownership, policy, release, correction, and rollback boundaries for every layer surface.
