<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/data/cartographic-omission-disclosure
title: CartographicOmissionDisclosureCandidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Data contract steward · Cartography steward · Evidence steward · Validation steward
created: 2026-08-10
updated: 2026-08-10
owning_root: contracts/
policy_label: internal; data; layer-manifest; cartography; disclosure; auditability
responsibility: Define fixture-only disclosure semantics for purposeful cartographic omission, simplification, and emphasis without changing a layer or creating evidence, policy, review, release, or publication authority.
truth_posture: "CONFIRMED supplied-card traceability and repository placement; PROPOSED inactive contract; UNKNOWN consumer adoption; NEEDS VERIFICATION human review and hosted CI"
related:
  - ./layer_manifest.md
  - ../evidence/representation_fitness_assessment.md
  - ../../schemas/contracts/v1/data/cartographic_omission_disclosure.schema.json
  - ../../fixtures/contracts/v1/data/cartographic_omission_disclosure/cases.json
  - ../../tools/validators/data/validate_cartographic_omission_disclosure.py
  - ../../tests/validators/test_validate_cartographic_omission_disclosure.py
  - ../../docs/intake/exploratory/pass-18-cartographic-omission-disclosure-source-map.md
[/KFM_META_BLOCK_V2] -->

# CartographicOmissionDisclosureCandidate

`CartographicOmissionDisclosureCandidate` is an additive, fixture-only profile for recording purposeful omission, simplification, and emphasis choices associated with one candidate `LayerManifest`.

It implements the smallest reviewable portion of supplied Pass 18 card `KFM-P18-INV-401`: cartographic selectivity should be inspectable because what a map leaves out can affect interpretation as materially as what it includes.

## Boundary

The profile is `PROPOSED_INACTIVE`, no-network, and non-authoritative. A validator `PASS` means only that:

- the candidate is closed under this schema;
- its deterministic profile hash replays;
- its entries are canonically ordered and internally coherent;
- material choices name a user-visible disclosure surface;
- sensitivity and rights choices retain policy references; and
- simplification choices retain a transform-receipt reference.

It does **not** resolve a `LayerManifest`, map-purpose statement, `EvidenceBundle`, policy decision, review record, or transform receipt. It does not determine which omissions are materially significant, alter a layer, render a map, approve review, promote lifecycle state, create a release manifest, release, deploy, publish, or authorize public use.

## Profile fields

| Field | Meaning |
|---|---|
| `profile_spec_hash` | Canonical JSON plus SHA-256 binding of the complete candidate except this field. |
| `layer_manifest_ref` / `layer_manifest_digest` | Pinned candidate-layer identity; no reference resolution occurs. |
| `map_purpose` | Pinned map-purpose reference and resolution state. |
| `evidence_scope` | Pinned evidence-scope reference and resolution state. |
| `assessment` | Declared review scope, completeness state, and known undisclosed-material count. |
| `entries` | Canonically ordered omission, simplification, or emphasis records. |
| `authority_claims` | Fixed-false declaration preventing evidence, policy, review, promotion, release, publication, or public-use authority. |

Each entry records a bounded subject, representation action, reason, materiality assessment, public-disclosure surface, evidence references, policy and review references, and any transform-receipt reference. The profile never stores omitted feature values, restricted coordinates, or source payloads.

## Finite validation outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Shape, identity, canonical ordering, and local disclosure invariants are coherent for the declared scope. |
| `ABSTAIN` | Purpose or evidence scope is unresolved, the assessment is incomplete/unknown, or an entry's materiality remains unknown. |
| `DENY` | A deterministic identity, disclosure, policy-reference, transform-receipt, completeness, or canonicalization invariant fails. |
| `ERROR` | The candidate cannot be evaluated safely under the closed machine schema. |

These are validator outcomes only. They are not map trust states, policy decisions, review decisions, release states, or runtime answers.

## Directory Rules basis

The accepted responsibility-root model places semantic meaning under `contracts/`, machine shape under `schemas/`, synthetic cases under `fixtures/`, repository validation under `tools/`, executable checks under `tests/`, CI orchestration under `.github/`, human source reconciliation under `docs/`, and authoring accountability under `data/receipts/generated/`.

The object is adjacent to `contracts/data/layer_manifest.md` because it describes one layer-manifest candidate and composes that existing authority by reference. It does not add a parallel map, layer, evidence, policy, release, or publication home and does not modify the existing `LayerManifest` schema or Evidence Drawer payload.

## Validation

```bash
python -m unittest tests.validators.test_validate_cartographic_omission_disclosure -v
python tools/validators/data/validate_cartographic_omission_disclosure.py --fixtures
```

## Rollback

Revert the additive profile packet. It has no consumer and mutates no map, source, evidence, policy, review, lifecycle, catalog, release, cache, route, deployment, or public artifact.
