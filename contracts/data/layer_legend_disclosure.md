<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/data/layer-legend-disclosure
title: LayerLegendDisclosureCandidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
owners: OWNER_TBD — Data contract steward · Cartography steward · Evidence steward · Validation steward
created: 2026-08-10
updated: 2026-08-10
owning_root: contracts/
policy_label: internal; data; layer-manifest; legend; evidence-disclosure; trust-visible-ui
responsibility: Define fixture-only legend disclosure semantics for evidence class, release state, sensitivity transform, uncertainty cues, and negative states without altering a layer or creating evidence, policy, review, release, or publication authority.
truth_posture: "CONFIRMED source-card traceability and repository placement; PROPOSED inactive contract; UNKNOWN consumer adoption; NEEDS VERIFICATION human review and hosted CI"
related:
  - ./layer_manifest.md
  - ./cartographic_omission_disclosure.md
  - ../evidence/representation_fitness_assessment.md
  - ../../schemas/contracts/v1/data/layer_legend_disclosure.schema.json
  - ../../fixtures/contracts/v1/data/layer_legend_disclosure/cases.json
  - ../../tools/validators/data/validate_layer_legend_disclosure.py
  - ../../tests/validators/test_validate_layer_legend_disclosure.py
  - ../../docs/intake/exploratory/pass-18-layer-legend-disclosure-source-map.md
[/KFM_META_BLOCK_V2] -->

# LayerLegendDisclosureCandidate

`LayerLegendDisclosureCandidate` is an additive, fixture-only profile for declaring the trust-bearing information shown by a map legend for one candidate `LayerManifest`.

It implements the smallest reviewable portion of supplied Pass 18 card `KFM-P18-INV-351`: legends should disclose layer evidence class, release state, sensitivity transform, and uncertainty cues rather than symbols and colors alone.

## Boundary

The profile is `PROPOSED_INACTIVE`, deterministic, no-network, and non-authoritative. A validator `PASS` means only that the legend declaration is closed under this schema, its profile hash replays, entries are canonically ordered, negative states are not represented as visible released data, sensitivity transforms retain policy references, and modeled/derived material carries uncertainty cues.

It does **not** resolve a `LayerManifest`, `EvidenceBundle`, `PolicyDecision`, review record, correction record, or status record. It does not render a legend, alter a style, hide or reveal a feature, determine uncertainty, approve review, promote lifecycle state, release, deploy, publish, or authorize public use.

## Profile fields

| Field | Meaning |
|---|---|
| `profile_spec_hash` | Canonical JSON plus SHA-256 binding of the candidate except this field. |
| `layer_manifest_ref` / `layer_manifest_digest` | Pinned candidate-layer identity; no reference resolution occurs. |
| `evidence_scope` | Evidence-scope reference and resolution state. |
| `legend` | Title, declared scope, completeness state, and known undisclosed-entry count. |
| `entries` | Canonically ordered legend declarations for one visible or disabled class. |
| `authority_claims` | Fixed-false declaration preventing evidence, policy, review, promotion, release, publication, or public-use authority. |

Each entry records the display label and symbol reference plus evidence class, release state, render state, sensitivity transform, uncertainty cue, details surface, evidence references, policy references, status references, and correction references. The profile never stores raw source payloads or restricted geometry.

## Finite validation outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Shape, identity, ordering, disclosure, negative-state, sensitivity, and uncertainty invariants are coherent. |
| `ABSTAIN` | Evidence scope, legend completeness, evidence class, release state, or uncertainty cue remains unresolved. |
| `DENY` | A visibility, policy-reference, status-reference, transform, uncertainty, completeness, or canonicalization invariant fails. |
| `ERROR` | The candidate cannot be evaluated safely under the closed machine schema. |

These are validator outcomes only. They are not map trust states, policy decisions, review decisions, release states, or runtime answers.

## Directory Rules basis

Accepted Directory Rules place semantic meaning under `contracts/`, machine shape under `schemas/`, synthetic cases under `fixtures/`, executable validation under `tools/`, conformance checks under `tests/`, CI orchestration under `.github/`, source reconciliation under `docs/`, and authoring accountability under `data/receipts/generated/`.

The object is adjacent to `contracts/data/layer_manifest.md` and `cartographic_omission_disclosure.md` because it describes one candidate layer's downstream legend projection by reference. It creates no parallel map, UI, evidence, policy, release, or publication home.

## Validation

```bash
python -m unittest tests.validators.test_validate_layer_legend_disclosure -v
python tools/validators/data/validate_layer_legend_disclosure.py --fixtures
```

## Rollback

Revert the additive packet. It has no consumer and mutates no map, style, source, evidence, policy, review, lifecycle, catalog, release, cache, route, deployment, or public artifact.
