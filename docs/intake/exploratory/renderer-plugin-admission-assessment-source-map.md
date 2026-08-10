<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/renderer-plugin-admission-assessment-source-map
title: RendererPluginAdmissionAssessment source map
type: exploratory-source-map
version: 1.0.0
status: proposed
owning_root: docs/
truth_posture: source-derived proposal; current repository behavior verified separately
related:
  - ../../../contracts/map/renderer_plugin_admission_assessment.md
  - ../../doctrine/directory-rules.md
[/KFM_META_BLOCK_V2] -->

# `RendererPluginAdmissionAssessment` source map

## Goal

Translate the supplied KFM renderer-plugin guidance into the smallest dependency-closed repository increment: a deterministic, no-network, fixture-only evidence assessment behind existing plugin `admission_ref` fields.

## Source-derived requirements

The supplied `maplibre3d.md` states that external renderer plugins remain inside KFM's governance surface, requires pinned versions, supply-chain checks, checksums, attestations, per-plugin admission decisions, and lockfile drift checks, and leaves exact policy realization open as `OQ-3D-12`. Its adapter plan also places plugin-hosted renderers behind a governed runtime boundary.

The Google Drive document `KFM_Full_Atlas_seed_cards` separately describes a “Renderer as Pluggable Component Framework Pattern”: interchangeable implementations sit behind an abstract interface and remain downstream of evidence, policy, and review dependencies. This supports an adapter-boundary check while providing no authority to select or install an implementation.

## Repository evidence and gap

At the implementation base:

- `contracts/map/three_d_admission_decision.md` and its schema require pinned plugin dependencies with integrity, attestation, admission, license, and CVE-watch references;
- `contracts/governance/dependency_origin_policy.md` covers static dependency-origin and lockfile ambiguity but explicitly does not prove attestation, SBOM, license, or vulnerability closure; and
- no fixture-backed renderer plugin admission assessment was found.

The gap is therefore not a runtime plugin registry or policy DSL. It is the evidence object that can sit behind the existing `admission_ref` without overclaiming admission.

## Translation choices

- The fixture uses a synthetic package name and synthetic references; no current real-world version, license, or vulnerability claim is imported.
- `PASS` maps only to `READY_FOR_REVIEW`; `review_state` remains `HOLD`.
- Unknown evidence produces `ABSTAIN`; negative or drifted evidence produces `DENY`.
- The validator performs no registry, package-manager, network, install, import, policy, or renderer operation.

## Non-effects

This packet does not add a dependency, edit a package manifest or lockfile, name an admitted real plugin, query a registry, download bytes, run lifecycle scripts, install or import code, choose a renderer, amend policy, approve review, authorize release, deploy, publish, or change public-use state.

## Directory Rules basis

Accepted ADR-0029 makes the adopted Directory Governance Standard the placement authority. The packet uses existing contract, schema, fixture, validator, test, workflow, exploratory-doc, and generated-receipt roots and creates no parallel authority home.
