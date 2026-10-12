<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/map/renderer-plugin-admission-assessment/v1
title: RendererPluginAdmissionAssessment candidate profile
type: semantic-contract
version: 1.0.0
status: proposed-inactive
owning_root: contracts/
responsibility: Define a fixture-only assessment behind renderer plugin admission references without admitting or installing a plugin.
truth_posture: cite-or-abstain; PASS means ready for human review, never admitted, installed, released, or executable
related:
  - ../../../schemas/contracts/v1/map/renderer_plugin_admission_assessment.schema.json
  - ../../../fixtures/contracts/v1/map/renderer_plugin_admission_assessment/README.md
  - ../../../tools/validators/map/validate_renderer_plugin_admission_assessment.py
  - ../governance/dependency_origin_policy.md
  - three_d_admission_decision.md
  - ../../../docs/doctrine/directory-rules.md
[/KFM_META_BLOCK_V2] -->

# `RendererPluginAdmissionAssessment` candidate profile

> **Status:** `PROPOSED_INACTIVE` · **Authority:** fixture-only evidence assessment · **Plugin admission/install authority:** none

## Purpose

`ThreeDAdmissionDecision` already requires each plugin-hosted renderer dependency to carry an `admission_ref`. This profile defines the narrower evidence assessment that such a reference may eventually identify. It separates evidence collection from policy, human review, release, installation, and runtime execution.

The candidate checks a synthetic declaration for:

- an exact version and SHA-256 artifact binding;
- lockfile and dependency-origin-policy evidence;
- supply-chain attestation and SBOM references;
- license and vulnerability review state;
- a governed adapter boundary and declared network behavior; and
- removal and rollback evidence.

The profile does **not** inspect a registry, download a package, run lifecycle scripts, install or import a plugin, evaluate live policy, approve a dependency, modify a lockfile, or boot a renderer.

## Deterministic identity

The validator computes RFC 8785 JCS + SHA-256 over the full candidate except `assessment_id` and `spec_hash`:

```text
spec_hash    = sha256(JCS(identity_subject))
assessment_id = "renderer-plugin-assessment:" + first_24_hex(spec_hash)
```

The identity binds fixture bytes only. It is not an attestation or admission decision.

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | The synthetic declaration is locally coherent and may be placed in a human review queue. |
| `ABSTAIN` | Required evidence is unresolved or explicitly unknown. |
| `DENY` | A negative supply-chain, adapter, network, removal, rollback, or authority invariant is present. |
| `ERROR` | Input, schema, hashing, identity, or fixture execution failed. |

`recommendation: READY_FOR_REVIEW` is deliberately weaker than admission. `review_state` remains `HOLD` for every valid candidate.

## Invariants

- Package versions are exact and artifact digests use SHA-256.
- A plugin is bound to a lockfile and the existing `DependencyOriginPolicy` assessment surface.
- Verified evidence states carry non-null references included in `evidence_refs`.
- Unknown evidence yields `ABSTAIN`; invalid, denied, affected, violated, failed, or drifted evidence yields `DENY`.
- Admitted layer classes, evidence references, and limitations are sorted and unique.
- The declared recommendation matches the validator's evidence polarity.
- Review remains held and all install, import, renderer, policy, approval, lockfile, release, deployment, publication, and network-probe effects remain false.

## Directory Rules basis

`contracts/map/` owns renderer-plugin candidate meaning. Machine shape, examples, executable validation, proof, CI orchestration, source mapping, and generated accountability remain in their existing responsibility roots. This packet creates no plugin registry, policy DSL, runtime adapter, package manifest, or parallel authority home.

## Trust boundary and rollback

A passing result proves only deterministic fixture shape and the declared evidence relationships. It does not prove registry identity, package bytes, publisher identity, signature validity, SBOM completeness, vulnerability absence, license compatibility, adapter correctness, safe network behavior, review approval, or runtime safety.

Rollback is a revert of this additive fixture packet. No dependency, lockfile, package, runtime, policy, release, deployment, or publication state is changed.
