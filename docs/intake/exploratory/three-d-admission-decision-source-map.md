<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/three-d-admission-decision-source-map
title: ThreeDAdmissionDecision source map
type: exploratory-source-map
version: 1.0.0
status: proposed
owning_root: docs/
truth_posture: source-derived proposal; current repository behavior verified separately
related:
  - ../../../contracts/map/three_d_admission_decision.md
  - ../../doctrine/directory-rules.md
[/KFM_META_BLOCK_V2] -->

# `ThreeDAdmissionDecision` source map

## Goal

Translate the strongest conditional-3D recommendations in the supplied KFM atlases and MapLibre architecture material into one deterministic, no-network, fixture-only admission profile.

## Source-derived requirements

The supplied material consistently supports the following boundaries:

1. **2D-first admission law.** 3D is conditional and must carry an explanatory burden that 2D cannot serve as well.
2. **Knowledge-character distinction.** Visual 3D, analytical 3D, digital-twin claims, and 2.5D surfaces carry different epistemic burdens.
3. **Scene and Drawer parity.** A 3D scene remains downstream of the same released assets, evidence, sensitivity, correction, and drawer payload logic as the 2D shell.
4. **Reality boundaries.** Modeled, synthetic, and reconstructed representations require explicit interpretive limitations.
5. **Sensitivity before rendering.** Sensitive geometry is transformed before renderer access, not hidden by styling.
6. **Plugin governance.** External renderer plugins are pinned, integrity-bound, attested, license-reviewed, CVE-watched, and admitted before use.

## Repository evidence and gap

At the implementation base:

- `schemas/contracts/v1/evidence/reality_boundary_note.schema.json` and its validator already provide a Reality Boundary Note family;
- `schemas/contracts/v1/map/representation_fitness_assessment.schema.json` and its validator already provide representation fitness evidence;
- MapLibre architecture documents name a 3D admission decision as a governed object; and
- no fixture-backed `three_d_admission_decision` schema, validator, or workflow was found.

The smallest dependency-closed increment is therefore a held, fixture-only admission evaluator that references existing object families without claiming to resolve or approve them.

## Non-effects

This packet does not boot MapLibre, install or select plugins, amend the runtime wrapper, fetch a source, inspect real sensitive geometry, resolve evidence, execute policy, approve human review, activate a scene, promote, release, deploy, publish, or authorize public use.

## Directory Rules basis

Accepted ADR-0029 makes the adopted Directory Governance Standard the placement authority. The packet uses existing semantic-contract, schema, fixture, validator, test, workflow, exploratory-doc, and generated-receipt roots and creates no parallel authority home.
