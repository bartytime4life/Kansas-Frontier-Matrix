<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/map/renderer-binding-assessment
title: RendererBindingAssessment Candidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD - Map steward · UI steward · Evidence steward · Policy steward · Release steward · Validation steward
created: 2026-08-11
updated: 2026-08-11
owning_root: contracts/
policy_label: internal; map; renderer-binding; layer; trust-membrane; review-required
responsibility: Define a fixture-only assessment of one renderer-to-layer binding without registering a layer, resolving references, reading an internal store, executing a renderer, or granting evidence, policy, review, release, deployment, publication, or public-use authority.
truth_posture: "CONFIRMED supplied Pass 20 EXP-015 proposal lineage, visually inspected MapLibre operating-manual boundary, current repository map architecture and adjacent contracts, accepted Directory Rules, and bounded implementation gap; PROPOSED inactive assessment; UNKNOWN accepted renderer-binding policy and production registration gate; NEEDS VERIFICATION human review and hosted exact-head CI"
related:
  - ../data/layer_descriptor.md
  - ../data/layer_manifest.md
  - ../ui/renderer_capability_profile.md
  - ./renderer_plugin_admission_assessment.md
  - ../../docs/architecture/map-master.md
  - ../../docs/doctrine/directory-rules.md
  - ../../schemas/contracts/v1/map/renderer_binding_assessment.schema.json
  - ../../fixtures/contracts/v1/map/renderer_binding_assessment/cases.json
  - ../../tools/validators/map/validate_renderer_binding_assessment.py
  - ../../tests/validators/map/test_validate_renderer_binding_assessment.py
  - ../../docs/intake/exploratory/pass-20-renderer-binding-assessment-source-map.md
[/KFM_META_BLOCK_V2] -->

# RendererBindingAssessment Candidate

`RendererBindingAssessmentCandidate` is an additive, fixture-only declaration
for checking whether one synthetic renderer-to-layer relationship keeps the
renderer downstream of the KFM trust membrane. It implements only the bounded
renderer-binding portion of Pass 20 `EXP-015`; it does not create the live layer
registry, reference resolver, artifact verifier, policy, or production MapLibre
registration gate that the expansion item still leaves open.

The assessment composes existing meanings by opaque reference. `LayerDescriptor`,
`LayerManifest`, renderer capability, artifact, evidence, policy, review,
promotion, release, correction, and rollback objects retain their own authority.

## Declared assessment

| Concern | Required declaration | Local check |
|---|---|---|
| Renderer | Family, surface, adapter, capability profile, optional admission ref, and inactive binding state. | Unknown declarations and peer-browser policy abstain; incoherent surface/family pairs and active bindings deny. |
| Layer | Distinct descriptor, manifest, style, and artifact refs plus an explicit layer version. | The assessment does not resolve, validate, or rewrite any referenced object. |
| Delivery | Governed API or released carrier, immutable locator posture, and explicit direct-store/query flags. | RAW, WORK, QUARANTINE, internal-store, direct-store, and query paths deny. |
| Trust closure | Evidence, policy, review, promotion, release, rollback, correction, sensitivity, rights, and release-state declarations. | Unknown support abstains; unsafe or incomplete public closure denies. |
| Interaction | Governed API context and evidence-resolution route with explicit anti-authority flags. | Feature properties, client policy, hidden inference, and internal lookup cannot become authority. |
| Review | Pending, unknown, or complete-for-declared-scope with record refs. | A coherent candidate remains `REVIEW_REQUIRED`; it never becomes registered or approved. |

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `REVIEW_REQUIRED` | The fixture-only relationship is locally coherent and still requires human review plus resolution of every referenced authority object. |
| `ABSTAIN` | Renderer, delivery, trust, interaction, or review support remains unresolved. |
| `DENY` | The declaration crosses the trust membrane, treats renderer state as authority, uses unsafe input, or omits required public closure. |
| `ERROR` | The candidate cannot be safely parsed or evaluated under the closed schema. |

## Invariants

- A renderer consumes governed APIs or released carriers; it never reads RAW,
  WORK, QUARANTINE, or internal stores directly.
- LayerDescriptor, LayerManifest, style, artifact, evidence, policy, release,
  and rollback identities remain distinct.
- Feature properties are display/interaction context, not evidence or policy
  authority.
- Client-side filtering is not a sensitivity transform or policy decision.
- A published declaration requires immutable delivery plus promotion, release,
  rollback, evidence, policy, and review support.
- The candidate binding remains inactive and cannot write a registry or call
  MapLibre registration APIs.
- The proposed ADR-0007 posture is not promoted or accepted by this contract.

## Authority boundary

A validator result does not:

- register, activate, load, import, execute, benchmark, or select a renderer;
- register a source or layer, modify a view registry, or call `addSource` or
  `addLayer`;
- resolve references, inspect artifact bytes, verify signatures, or mint
  identity;
- evaluate evidence, rights, sensitivity, policy, review, or release state;
- approve ADR-0007, plugin admission, promotion, release, deployment,
  publication, or public use.

## Directory Rules basis

The object assesses a map renderer relationship, so semantic meaning belongs
under `contracts/map/`. Machine shape, synthetic fixtures, deterministic
validation, executable tests, read-only CI, source lineage, and authoring
provenance remain in their existing responsibility roots. No new registry,
runtime package, policy bundle, release lane, public route, or authority home is
created.

## Validation and rollback

```bash
python -m unittest tests.validators.map.test_validate_renderer_binding_assessment -v
python tools/validators/map/validate_renderer_binding_assessment.py --fixtures
```

Rollback is one additive commit revert. The inactive packet creates no
renderer, registry, layer, data, policy, release, deployment, publication, or
public state that requires restoration.
