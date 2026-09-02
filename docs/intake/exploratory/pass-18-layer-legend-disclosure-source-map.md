<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-18-layer-legend-disclosure-source-map
title: Pass 18 Layer Legend Disclosure Source Map
type: source-map
version: v1.0.0
status: exploratory; implementation-mapped; non-authoritative
owners: OWNER_TBD — Intake steward · Cartography steward · Evidence steward
created: 2026-08-10
updated: 2026-08-10
owning_root: docs/
policy_label: internal; exploratory; source-reconciliation; map; legend; disclosure
responsibility: Reconcile one supplied map-legend idea with current repository evidence while preserving renderer, evidence, policy, review, release, and publication boundaries.
truth_posture: "CONFIRMED supplied-card and bounded repository gap; PROPOSED inactive implementation profile; UNKNOWN consumer adoption; NEEDS VERIFICATION human review and hosted CI"
related:
  - ../../../contracts/data/layer_legend_disclosure.md
  - ../../../contracts/data/layer_manifest.md
  - ../../../contracts/data/cartographic_omission_disclosure.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
[/KFM_META_BLOCK_V2] -->

# Pass 18 Layer Legend Disclosure Source Map

## Source and gap

| Evidence | Observation | Status |
|---|---|---|
| Supplied Pass 18 card `KFM-P18-INV-351` | Map legends should disclose evidence class, release state, sensitivity transform, and uncertainty cues for each visible layer. | `CONFIRMED` source statement |
| Connected Drive MapLibre and trust-visible UI corpus | The renderer is downstream of trust and should expose stale, degraded, denied, generalized, withheld, and uncertainty states rather than hide them. | `CONFIRMED` thematic corroboration |
| Existing `LayerManifest` and cartographic omission profile | Current objects define layer and omission semantics, but no exact legend-disclosure contract, schema, fixtures, validator, workflow, or PR was found at the inspected base. | `CONFIRMED` bounded gap |
| Current repository search | No exact implementation of source card `KFM-P18-INV-351` was found before authoring. | `CONFIRMED` bounded search |

## Adaptation

The implementation is a closed synthetic data-contract profile. It records one candidate layer-manifest reference and a canonically ordered legend projection whose entries disclose evidence class, release state, render state, sensitivity transform, uncertainty cue, details surface, and supporting references.

The profile does not render a legend, mutate a style, decide layer visibility, resolve evidence, evaluate policy, approve review, promote, release, deploy, or publish.

## Directory Rules basis

The accepted responsibility-root model places semantic meaning in `contracts/data/`, machine shape in `schemas/contracts/v1/data/`, synthetic replay in `fixtures/contracts/v1/data/`, executable validation in `tools/validators/data/`, conformance proof in `tests/validators/`, orchestration in `.github/workflows/`, reconciliation in `docs/intake/exploratory/`, and generated authoring provenance in `data/receipts/generated/`.

No map, UI, layer, evidence, policy, release, or public-authority home is created.

## Non-effects and rollback

A local validator result is only declaration coherence. It is not evidence validity, policy approval, map rendering, layer admission, review completion, release, publication, or public-answer authority. Rollback is an additive commit revert with no external cleanup.
