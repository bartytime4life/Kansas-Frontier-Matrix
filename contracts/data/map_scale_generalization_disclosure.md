<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/data/map-scale-generalization-disclosure
title: MapScaleGeneralizationDisclosureCandidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Data contract steward · Cartography steward · Evidence steward · Validation steward
created: 2026-08-11
updated: 2026-08-11
owning_root: contracts/
policy_label: internal; data; layer-manifest; map-scale; generalization; disclosure
responsibility: Define fixture-only disclosure semantics for the scale or zoom context, method, precision posture, and caveat attached to one generalized layer candidate without changing the layer or creating evidence, policy, review, release, or publication authority.
truth_posture: "CONFIRMED supplied-card traceability and repository placement; PROPOSED inactive contract; UNKNOWN consumer adoption; NEEDS VERIFICATION human review and hosted CI"
related:
  - ./layer_manifest.md
  - ./cartographic_omission_disclosure.md
  - ../evidence/representation_fitness_assessment.md
  - ../../schemas/contracts/v1/data/map_scale_generalization_disclosure.schema.json
  - ../../fixtures/contracts/v1/data/map_scale_generalization_disclosure/cases.json
  - ../../tools/validators/data/validate_map_scale_generalization_disclosure.py
  - ../../tests/validators/test_validate_map_scale_generalization_disclosure.py
  - ../../docs/intake/exploratory/pass-18-map-scale-generalization-disclosure-source-map.md
[/KFM_META_BLOCK_V2] -->

# MapScaleGeneralizationDisclosureCandidate

`MapScaleGeneralizationDisclosureCandidate` is an additive, fixture-only profile for declaring the map scale or zoom context in which one candidate `LayerManifest` generalization is intended to be interpreted.

It implements the smallest reviewable portion of supplied Pass 18 card `KFM-P18-INV-476`: simplified geometry must not be presented as equally precise at every scale or zoom.

## Boundary

The profile is `PROPOSED_INACTIVE`, deterministic, no-network, and non-authoritative. A validator `PASS` means only that:

- the candidate is closed under this schema and its deterministic profile hash replays;
- the declared zoom and/or scale-denominator range is locally well formed;
- a generalization method retains a transform-receipt reference;
- generalized output declares omitted detail, a bounded precision posture, a visible caveat surface, and review references; and
- every authority-bearing declaration remains fixed to `false`.

It does **not** resolve a `LayerManifest`, `EvidenceBundle`, map-purpose record, transform receipt, policy decision, or review record. It does not inspect geometry, infer an appropriate scale, verify positional accuracy, select or execute a generalization method, alter a layer, render a map, approve review, promote lifecycle state, release, deploy, publish, or authorize public use.

## Profile fields

| Field | Meaning |
|---|---|
| `profile_spec_hash` | Canonical JSON plus SHA-256 binding of the candidate except this field. |
| `layer_manifest_ref` / `layer_manifest_digest` | Pinned candidate-layer identity; no reference resolution occurs. |
| `map_purpose` / `evidence_scope` | Pinned supporting references with explicit local resolution posture. |
| `intended_use` | Internal review, public-map candidate, or export candidate; never an authorization. |
| `validity_context` | `ZOOM_RANGE`, `SCALE_DENOMINATOR_RANGE`, `BOTH`, or unresolved posture with bounded numeric fields. |
| `generalization` | Declared method, receipt reference, precision posture, retained properties, and omitted detail classes. |
| `disclosure` | Completeness state, public caveat, details surface, and review-record references. |
| `authority_claims` | Fixed-false evidence, policy, review, promotion, release, publication, and public-use declarations. |

Scale denominators are stored only as a numeric range. This profile does not claim that a denominator corresponds to a particular device, renderer, display size, or zoom level, and it deliberately defines no crosswalk between the two systems.

## Finite validation outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Shape, identity, range, transform, caveat, and local review-reference invariants are coherent. |
| `ABSTAIN` | Purpose, evidence scope, validity context, method, precision posture, or disclosure remains unresolved or incomplete. |
| `DENY` | A range, basis, transform-receipt, omitted-detail, caveat, review, canonicalization, or deterministic-identity invariant fails. |
| `ERROR` | The candidate cannot be evaluated safely under the closed schema. |

These are validator outcomes only. They are not scientific accuracy findings, policy decisions, review decisions, map trust states, release states, or runtime answers.

## Directory Rules basis

Accepted Directory Rules place semantic meaning under `contracts/`, machine shape under `schemas/`, synthetic cases under `fixtures/`, repository validation under `tools/`, executable conformance under `tests/`, CI orchestration under `.github/`, human source reconciliation under `docs/`, and authoring accountability under `data/receipts/generated/`.

The object is adjacent to `contracts/data/layer_manifest.md` and `cartographic_omission_disclosure.md` because it describes one layer-manifest candidate by reference. It does not modify `LayerManifest` or create a parallel map, layer, evidence, policy, release, or publication home.

## Validation

```bash
python -m unittest tests.validators.test_validate_map_scale_generalization_disclosure -v
python tools/validators/data/validate_map_scale_generalization_disclosure.py --fixtures
```

## Rollback

Revert the additive packet. It has no runtime consumer and mutates no map, geometry, source, evidence, policy, review, lifecycle, catalog, release, cache, route, deployment, or public artifact.
