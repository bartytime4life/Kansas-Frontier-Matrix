# `schemas/contracts/v1/scene/` — Scene Schema Family Guardrail

<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/schemas-contracts-v1-scene-readme
title: schemas/contracts/v1/scene/ — Scene Schema Family Guardrail
type: readme; schema-family-index; scene-schema-boundary; map-runtime-placement-guardrail
authority_class: schema-family-guardrail
version: v0.1
status: draft; empty-schema-family; exact-scene-schema-not-found; map-layer-runtime-nearest-lanes; no-current-scene-schema-files-found; do-not-promote-without-ADR; NEEDS VERIFICATION before promotion
owners:
  - OWNER_TBD — Scene steward
  - OWNER_TBD — Map/UI steward
  - OWNER_TBD — Layer steward
  - OWNER_TBD — Runtime steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Policy steward
  - OWNER_TBD — Release steward
  - OWNER_TBD — Validation steward
  - OWNER_TBD — Docs steward
created: NEEDS VERIFICATION — empty README existed before v0.1 expansion
updated: 2026-07-04
policy_label: public; schemas; contracts-v1; scene; map-scene; viewer-scene; maplibre-adjacent; layer-adjacent; runtime-adjacent; evidence-bound; policy-aware; release-gated; rollback-aware; no-parallel-authority
tags: [kfm, schemas, contracts, v1, scene, map-scene, viewer-scene, maplibre, map, layers, runtime, evidence-drawer, public-ui, release, rollback, no-parallel-authority]
related:
  - ../README.md
  - ../map/README.md
  - ../layers/README.md
  - ../runtime/README.md
  - ../exposure/README.md
  - ../evidence/README.md
  - ../policy/README.md
  - ../release/README.md
  - ../review/README.md
  - ../../../../docs/architecture/map-master/README.md
  - ../../../../docs/doctrine/map-first.md
  - ../../../../contracts/
  - ../../../../policy/
  - ../../../../fixtures/
  - ../../../../tests/
  - ../../../../data/
  - ../../../../release/
notes:
  - "Expanded from an empty file at schemas/contracts/v1/scene/README.md."
  - "Current GitHub search did not surface schema files directly under schemas/contracts/v1/scene/ beyond this README."
  - "Current GitHub search did not surface exact scene schema evidence in this check."
  - "Map, layers, and runtime schema family READMEs were inspected as nearest verified lanes."
  - "This folder may define scene object shapes in the future, but it must not become a MapLibre runtime, layer store, public UI root, release authority, or emitted scene data root."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

![status](https://img.shields.io/badge/status-draft-yellow)
![root](https://img.shields.io/badge/root-schemas%2F-blue)
![family](https://img.shields.io/badge/family-scene-indigo)
![posture](https://img.shields.io/badge/posture-guardrail-orange)
![truth](https://img.shields.io/badge/truth-cite--or--abstain-success)

> **Purpose.** `schemas/contracts/v1/scene/` is a README-only guardrail for possible machine-checkable scene object shapes used by map/viewer/runtime surfaces.
>
> **One-line boundary.** Scene schemas define object shape only. They do not render MapLibre scenes, publish layers, authorize public display, replace evidence, decide policy, create runtime behavior, or store emitted scene records.

---

## Quick jumps

[Status](#status) · [Authority and placement](#authority-and-placement) · [Repo fit](#repo-fit) · [Current inventory](#current-inventory) · [Related lanes](#related-lanes) · [Candidate scene shapes](#candidate-scene-shapes) · [What belongs here](#what-belongs-here) · [What does not belong here](#what-does-not-belong-here) · [Scene-family rules](#scene-family-rules) · [Promotion checklist](#promotion-checklist) · [Validation](#validation) · [Rollback](#rollback) · [Open questions](#open-questions)

---

## Status

| Question | Answer | Truth label |
|---|---|---|
| Does this README path exist? | Yes: `schemas/contracts/v1/scene/README.md`. It was empty before this expansion. | **CONFIRMED** |
| Are schema files currently present directly under `schemas/contracts/v1/scene/`? | Not found in the current GitHub search beyond this README. | **NEEDS VERIFICATION / search-limited** |
| Did current search confirm an exact scene schema surface? | No exact scene schema surface was found in this check. | **NEEDS VERIFICATION** |
| What are the nearest verified schema lanes? | Map, Layers, and Runtime schema READMEs were inspected as nearest lanes. | **CONFIRMED path evidence** |
| Is this scene lane canonical? | Not proven. Treat this path as README-only until ADR or steward decision. | **NEEDS VERIFICATION / ADR-sensitive** |
| Can this path store rendered scenes, layer payloads, map tiles, runtime outputs, public artifacts, receipts, proofs, or release records? | No. This is schema documentation only, not lifecycle data, runtime, map rendering, proof storage, release storage, or publication surface. | **CONFIRMED boundary** |

> [!IMPORTANT]
> A scene descriptor is not a scene release. A scene manifest is not a rendered map. Schema validation alone does not make a viewer scene evidence-backed, policy-safe, or public-ready.

---

## Authority and placement

This folder is under the schema responsibility root:

```text
schemas/contracts/v1/scene/
```

It may define scene-support object shapes only after placement is resolved. Adjacent authority remains separate:

- `schemas/contracts/v1/map/` owns map-facing manifest and tile-artifact shapes where accepted.
- `schemas/contracts/v1/layers/` owns shared layer object shapes where accepted.
- `schemas/contracts/v1/runtime/` owns runtime-support object shapes where accepted.
- `schemas/contracts/v1/exposure/` owns public/client exposure shapes where accepted.
- `schemas/contracts/v1/evidence/` owns EvidenceBundle, EvidenceRef, and evidence-support shapes.
- `schemas/contracts/v1/policy/` owns policy-decision and sensitivity machine shapes.
- `schemas/contracts/v1/release/` owns release, correction, withdrawal, and rollback support shapes where accepted.
- `contracts/` owns semantic meaning.
- `data/` owns lifecycle records, registries, proofs, receipts, catalog/triplet records, and published data products according to each data root.
- UI/API/MapLibre code renders released/public-safe payloads; it is not owned by this folder.

This README does not amend ADR-0001, Directory Rules, map doctrine, runtime contracts, policy docs, validators, public API behavior, or release gates.

---

## Repo fit

```text
schemas/
└── contracts/
    └── v1/
        ├── README.md
        ├── scene/
        │   └── README.md                         # this file; README-only guardrail
        ├── map/
        │   └── README.md                         # map-facing shapes; not rendering authority
        ├── layers/
        │   └── README.md                         # layer shapes; not layer publication
        ├── runtime/
        │   └── README.md                         # runtime shapes; not execution authority
        ├── exposure/
        ├── evidence/
        ├── policy/
        ├── review/
        └── release/

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
| `schemas/contracts/v1/scene/README.md` | README | **CONFIRMED present** | Empty file expanded by this README. |
| `schemas/contracts/v1/scene/*.schema.json` | JSON Schema files | **Not found in current search** | Do not create here without ADR, paired contracts, fixtures, validators, and map/layer/runtime placement review. |

---

## Related lanes

| Lane | Role signal | Boundary to preserve |
|---|---|---|
| `schemas/contracts/v1/map/` | Map-facing manifest and tile-artifact schema family. | Map schemas do not render MapLibre, publish tiles, authorize public display, decide sensitivity, or replace release records. |
| `schemas/contracts/v1/layers/` | Layer manifest/descriptor/catalog schema family. | Layer schemas do not publish tiles, authorize public display, prove evidence closure, decide sensitivity, or act as release records. |
| `schemas/contracts/v1/runtime/` | Runtime response, decision, receipt, evidence drawer, consent, and layer-manifest schema family. | Runtime schemas do not execute behavior, approve AI output, replace evidence, publish layers, grant consent, or store emitted runtime records. |
| `schemas/contracts/v1/exposure/` | Public/client exposure shapes where accepted. | Exposure must remain policy-aware and release-gated. |
| `schemas/contracts/v1/release/` | Release-support object shapes. | Release schemas do not publish by themselves. |

---

## Candidate scene shapes

Candidate schemas below are proposals only and should not be created without steward review.

| Candidate schema | Purpose | Default posture |
|---|---|---|
| `scene_manifest.schema.json` | Describes a governed viewer scene made of released or candidate layer/style references. | **PROPOSED / not created** |
| `scene_layer_binding.schema.json` | Describes how a scene references layer descriptors, filters, order, and visibility defaults. | **PROPOSED / layer-overlap-sensitive** |
| `scene_evidence_panel.schema.json` | Describes scene-level evidence drawer grouping and display references. | **PROPOSED / evidence-bound** |
| `scene_runtime_state.schema.json` | Describes runtime viewer state or response context without executing the runtime. | **PROPOSED / runtime-overlap-sensitive** |
| `scene_release_projection.schema.json` | Public-safe projection for an already-governed scene surface. | **PROPOSED / release-gated** |

> [!CAUTION]
> Candidate names are proposals only. Do not treat them as repo files, accepted contracts, implementation proof, public-safe views, or release authority until created, paired, fixture-tested, and reviewed.

---

## What belongs here

- This README.
- Future machine-checkable JSON Schema files for scene object shapes if accepted.
- Schema index notes for scene object families.
- Migration notes for scene/map/layer/runtime/exposure overlap.
- Links to paired contracts, fixtures, validators, schema registry records, policy references, evidence references, release references, correction references, rollback references, and tests.

---

## What does not belong here

- Rendered scenes, MapLibre code, UI code, API implementation, runtime state as emitted records, layer payloads, style files, tile files, map screenshots, dashboards, public artifacts, proof outputs, receipt instances, EvidenceBundles, policy decisions, release records, correction notices, rollback records, catalog records, triplets, source records, or generated summaries.
- Policy rules, release decisions, access-control implementation, or map/public-display behavior.
- Domain payloads or source payloads.
- Claims that a scene is rendered, evidence-backed, policy-safe, released, public-ready, or publication-approved merely because it validates against a scene schema.

---

## Scene-family rules

| Rule | Requirement |
|---|---|
| Shape is not rendering | Schema validation constrains object shape; it does not render a scene. |
| Scene is not release | A scene descriptor may reference release state, but does not publish or approve display. |
| Scene is not evidence | A scene may point to evidence panels or EvidenceRefs, but does not replace EvidenceBundles. |
| Scene is not policy | A scene may carry policy state references, but does not decide exposure or sensitivity. |
| Reference over copy | Scene shapes should reference layer, map, runtime, evidence, policy, and release objects instead of copying their fields. |
| Public display is gated | Any public scene projection must use governed, released, policy-safe surfaces. |
| Contracts explain meaning | Accepted scene schemas need paired semantic contracts or approved profiles. |
| Fixtures prove behavior | Accepted schemas need valid and invalid fixtures plus validator coverage. |
| No parallel authority | Equivalent scene, map, layer, runtime, exposure, evidence, policy, and release shapes must not drift across roots without migration notes. |

---

## Promotion checklist

A scene schema should not advance beyond `PROPOSED` unless:

- [ ] Paired semantic contract exists or an approved profile is documented.
- [ ] `$id` namespace convention is settled.
- [ ] Required fields are defined.
- [ ] Placement is resolved against map, layers, runtime, exposure, evidence, policy, review, and release schema families.
- [ ] Layer/map/style/tile references use governed object references rather than embedded payloads.
- [ ] Evidence reference requirements are defined where scene output depends on claims.
- [ ] Policy/exposure requirements are defined where scene output can be shown to clients.
- [ ] Public-safe projection, if any, is release-gated.
- [ ] Valid fixtures exist.
- [ ] Invalid fixtures exist.
- [ ] Validators exist and paths are correct.
- [ ] CI/schema-test coverage exists.
- [ ] Migration notes exist for duplicate or overlapping schema surfaces.
- [ ] Correction and rollback references are defined where public use depends on the scene.

---

## Validation

Recommended local validation sequence:

```bash
# Confirm this scene lane remains README-only unless authorized.
find schemas/contracts/v1/scene -maxdepth 3 -type f | sort

# Detect scene/map/layer/runtime overlap.
find schemas/contracts/v1 -maxdepth 5 -type f \
  | grep -Ei 'scene|map|layer|style|tile|runtime|evidence_drawer|exposure|release' \
  | sort

# Validate JSON syntax for scene schemas if any are added later.
find schemas/contracts/v1/scene -name '*.json' -print0 \
  | xargs -0 -r -I{} python -m json.tool {} >/dev/null

# Inspect paired contracts and fixtures when present.
find contracts fixtures -maxdepth 5 -type f 2>/dev/null \
  | grep -Ei 'scene|map|layer|runtime|evidence_drawer' \
  | sort

# Run project validators when available.
python tools/validate_all.py || true
pytest tests/schemas tests/contract tests/policy tests/release || true
```

Replace `|| true` with fail-closed CI behavior once validator and test paths are confirmed.

---

## Rollback

Rollback for this README is ordinary Git rollback: revert the commit that changed `schemas/contracts/v1/scene/README.md`.

Rollback for future scene schema changes requires checking every downstream reference:

1. Revert or migrate schema files.
2. Restore canonical `$id` and `$ref` targets.
3. Restore paired contract links.
4. Restore fixtures, validators, schema registry records, and CI paths.
5. Restore map, layer, runtime, exposure, policy, evidence, review, release, correction, and rollback references.
6. Restore API/UI/MapLibre/Evidence Drawer consumers where applicable.
7. Preserve correction and rollback records if any public or semi-public scene surface was affected.

---

## Open questions

| Question | Status | Owner |
|---|---|---|
| Should scene object shapes live under `scene/`, `map/`, `runtime/`, or an exposure/viewer profile lane? | **NEEDS VERIFICATION / ADR-sensitive** | Scene steward + Schema steward |
| Which semantic contract owns scene object meaning? | **NEEDS VERIFICATION** | Contract steward + Scene steward |
| Should scene manifests reference map/layer manifests, runtime envelopes, release projections, or all of them through profiles? | **NEEDS VERIFICATION / placement-sensitive** | Scene steward + Map/UI steward + Runtime steward |
| Which fixtures prove scenes reference governed objects without embedding payloads? | **NEEDS VERIFICATION** | Validation steward |
| Which scene projections are safe for public API/MapLibre/Focus Mode use? | **NEEDS VERIFICATION / release-gated** | Release steward + Policy steward |

---

## Maintainer notes

- Keep this folder README-only until scene schema-home placement is resolved.
- Prefer references to governed map, layer, runtime, evidence, policy, and release objects over copied fields.
- Do not let `scene/` duplicate `map/`, `layers/`, `runtime/`, `exposure/`, or release projection authority.
- Preserve evidence, policy, exposure, release, correction, and rollback boundaries for every scene surface.
