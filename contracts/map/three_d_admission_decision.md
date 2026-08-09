<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/map/three-d-admission-decision/v1
title: ThreeDAdmissionDecision candidate profile
type: semantic-contract
version: 1.0.0
status: proposed-inactive
owning_root: contracts/
responsibility: Define a fixture-only candidate that tests whether a 3D representation request preserves explanatory burden, 2D trust parity, sensitivity controls, reality labeling, plugin admission references, and authority holds.
truth_posture: cite-or-abstain; an ALLOW_RENDER_CANDIDATE result is not policy approval, release authority, or permission to boot a renderer
related:
  - ../../../schemas/contracts/v1/map/three_d_admission_decision.schema.json
  - ../../../schemas/contracts/v1/evidence/reality_boundary_note.schema.json
  - ../../../schemas/contracts/v1/map/representation_fitness_assessment.schema.json
  - ../../../fixtures/contracts/v1/map/three_d_admission_decision/README.md
  - ../../../tools/validators/map/validate_three_d_admission_decision.py
  - ../../../docs/doctrine/directory-rules.md
[/KFM_META_BLOCK_V2] -->

# `ThreeDAdmissionDecision` candidate profile

> **Status:** `PROPOSED_INACTIVE` · **Authority:** fixture-only admission candidate · **Renderer boot authority:** none · **Public-use authority:** none

## Purpose

`ThreeDAdmissionDecision` evaluates a bounded, synthetic request to represent one released-asset-shaped map layer in a 3D or 2.5D mode. It operationalizes the KFM source recommendations that:

- 2D remains the calm evidence baseline;
- 3D is admitted only when an explanatory burden cannot be served as well by 2D;
- 2.5D surfaces must not masquerade as true vertical geometry;
- the Evidence Drawer, evidence, correction, and release references must remain in parity with 2D;
- modeled, synthetic, and reconstructed scenes require a `RealityBoundaryNote` reference;
- sensitive geometry must be transformed before rendering; and
- plugin-hosted 3D modes require pinned, integrity-bound, attested, explicitly admitted dependencies.

The profile does **not** install a plugin, import or boot MapLibre, resolve an EvidenceBundle, evaluate live policy, approve a scene, or publish a layer.

## Directory Rules basis

The adopted Directory Governance Standard assigns semantic meaning to `contracts/`, machine shape to `schemas/contracts/v1/`, examples to `fixtures/`, executable validation to `tools/validators/`, proof tests to `tests/`, orchestration to `.github/workflows/`, source mapping to `docs/intake/exploratory/`, and generated accountability to `data/receipts/generated/`. This packet stays within those existing responsibility roots.

## Candidate fields

| Field family | Meaning |
|---|---|
| Identity | `decision_id`, `spec_hash`, `profile`, `version`, and inactive status. |
| Governed inputs | Scene, layer, view-state, representation-fitness, EvidenceBundle, SourceDescriptor, domain-context, and optional Reality Boundary Note references. |
| Representation request | Requested mode, representation kind, geometry label, use case, source roles, and explicit limitations. |
| Sensitivity | Living-person, rare-species precision, archaeology precision/generalization, critical-infrastructure precision, and transform receipt references. |
| Plugin dependencies | Exact version, SHA-256 integrity, attestation, admission, CVE-watch, and verified-license references. |
| 2D parity | Evidence, drawer fields, correction references, release references, and sensitivity labels for both the 2D baseline and 3D candidate. |
| Authority holds | `review_state: HOLD`, `public_use_allowed: false`, and every effect flag `false`. |

## Deterministic identity

The validator computes RFC 8785 JCS + SHA-256 over the complete candidate except `decision_id` and `spec_hash`:

```text
spec_hash  = sha256(JCS(identity_subject))
decision_id = "three-d-admission:" + first_24_hex(spec_hash)
```

This identity proves deterministic fixture binding only.

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `ALLOW_RENDER_CANDIDATE` | The inactive synthetic candidate is locally coherent and retains all holds. |
| `ABSTAIN` | A required interpretive boundary cannot be supported, such as a missing Reality Boundary Note. |
| `DENY` | Explanatory burden, geometry truthfulness, parity, sensitivity, plugin, or authority invariants fail. |
| `ERROR` | Input, schema, hashing, identity, or fixture execution fails. |

## Core invariants

- Terrain and fill-extrusion are labeled `TWO_POINT_FIVE_D`; they cannot support `VERTICAL_EVIDENCE`.
- `OGC_3D_TILES`, `GLTF`, and `POINT_CLOUD` are labeled `TRUE_3D`; `GLOBE` remains a distinct representation label.
- `SPECTACLE_ONLY` never meets the explanatory-burden test.
- Living-person geometry, precise rare-species geometry, under-generalized archaeology, and precise critical-infrastructure geometry fail closed.
- Modeled, synthetic, or reconstructed candidates require a Reality Boundary Note reference.
- Evidence, drawer, correction, release, and sensitivity parity must match the 2D baseline exactly.
- Plugin-hosted modes require the exact expected plugin set; native modes require no plugins.
- Plugin versions are exact, integrity hashes are SHA-256, licenses are verified, and attestation/admission/CVE-watch references are present.
- The review remains held, public use remains false, and no renderer, plugin, policy, review, release, deployment, or publication effect is asserted.

## Trust boundary

A passing result proves only fixture shape, deterministic identity, exact finite polarity, representation labeling, declared 2D parity, sensitivity guards, plugin-reference completeness, and authority holds. It does not prove source authority, EvidenceBundle closure, policy approval, human review, real-device behavior, renderer compatibility, plugin security, release readiness, deployment, publication, or public suitability.
