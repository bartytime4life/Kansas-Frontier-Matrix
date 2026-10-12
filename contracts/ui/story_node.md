<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-ui-story-node
title: UI StoryNode Contract
type: semantic-contract
version: v0.3
status: draft; PROPOSED; closed-schema; fixture-first; ui-family; story-node; public-safe-projection; evidence-dependent; release-gated
owners: OWNER_TBD — UI steward · Story steward · Evidence steward · Runtime steward · Policy steward · Release steward · Schema steward · Accessibility steward
created: NEEDS VERIFICATION — greenfield scaffold existed before v0.2 expansion
updated: 2026-08-08
policy_label: public; contracts; ui; story-node; projection; evidence-dependent; no-sovereign-truth
owning_root: contracts/
responsibility: Define the semantic meaning and fail-closed trust inheritance of the public-safe UI StoryNode projection.
truth_posture: PROPOSED contract / CONFIRMED fixture-first enforcement / no publication authority
related:
  - ./README.md
  - ./story_manifest.md
  - ./evidence_drawer_payload.md
  - ../story/README.md
  - ../evidence/evidence_bundle.md
  - ../evidence/evidence_ref.md
  - ../runtime/runtime_response_envelope.md
  - ../policy/policy_decision.md
  - ../release/release_manifest.md
  - ../../schemas/contracts/v1/ui/story_node.schema.json
  - ../../fixtures/ui/story_node/
  - ../../tools/validators/ui/validate_story_node.py
  - ../../tests/validators/test_validate_story_node.py
  - ../../docs/intake/exploratory/pass-1-idea-index-coverage-source-map.md
tags: [kfm, contracts, ui, StoryNode, story, evidence, citation, rights, sensitivity, release, correction, supersession, accessibility]
notes:
  - "Implements the bounded P1-IMPORT-09 StoryNode trust-inheritance slice for KFM-P1-FEAT-0068 and related UIX cards."
  - "This contract and its schema define a public-safe UI projection only. They do not resolve evidence, decide policy, approve review or release, or publish."
  - "The paired schema is closed and the validator enforces finite state/outcome, support, rights, sensitivity, release, correction, and supersession relationships over synthetic fixtures."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# UI StoryNode Contract

> A `StoryNode` is one public-safe, renderable unit inside a governed story surface. It inherits evidence, citation, rights, sensitivity, policy, review, release, freshness, correction, and supersession posture from upstream authority-bearing objects. It never creates that authority.

**Profile:** `kfm.ui.story-node.public-safe.v1`  
**Paired schema:** `schemas/contracts/v1/ui/story_node.schema.json`  
**Validator:** `tools/validators/ui/validate_story_node.py`  
**Fixtures:** `fixtures/ui/story_node/`  
**Status:** draft / PROPOSED contract; fixture-first enforcement present  
**Pass 1 coverage:** `KFM-P1-FEAT-0065`, `KFM-P1-FEAT-0066`, `KFM-P1-FEAT-0068`, `KFM-P1-FEAT-0074`

## Purpose

The profile answers a narrow UI question:

> May this story node render public-safe content, render only a bounded status card, abstain, deny, report an error, or show that the node was superseded?

The answer is derived from explicit references and finite trust state. The node does not infer support from rendered pixels, client state, prose, map visibility, a model response, or a merged pull request.

```text
governed upstream objects
  -> evidence / citation / policy / review / release / correction checks
  -> public-safe StoryNode projection
  -> Story Player or equivalent UI surface
```

## Authority split

| Responsibility | Owning family |
|---|---|
| StoryNode public-safe projection meaning | `contracts/ui/story_node.md` |
| Machine shape | `schemas/contracts/v1/ui/story_node.schema.json` |
| Evidence truth and resolution | Evidence contracts and resolver |
| Citation validation | Citation validation object family |
| Rights, sensitivity, and admissibility | Policy objects and policy engine |
| Review state | Review records |
| Release and withdrawal state | Release objects |
| Correction, supersession, and rollback | Correction and release object families |
| Rendering and interaction | Explorer/UI implementation |
| Validation evidence | Fixtures, tests, and validator |

A valid StoryNode is not an `EvidenceBundle`, `PolicyDecision`, `ReviewRecord`, `ReleaseManifest`, proof, receipt, or publication decision.

## Closed profile

The machine profile requires:

- stable profile, node, manifest, type, and order identity;
- one finite node `state`, runtime `outcome`, and `reason_code`;
- bounded public-safe title, summary, accessibility label, caveats, and optional governed `body_ref`;
- governed map-context and support references only;
- explicit rights, sensitivity, policy, review, release, freshness, and correction posture;
- optional supersession metadata for a replaced node;
- `authoritative: false` and `projection_only: true`.

References are opaque governed identifiers. Raw URLs, file paths, source payloads, prompts, credentials, precise restricted geometry, and internal denial details do not belong in this projection.

## Finite states

| State | Required outcome | Purpose |
|---|---|---|
| `READY` | `ANSWER` | Render released, reviewed, current, policy-allowed, citation-backed content. |
| `PARTIAL` | `ABSTAIN` | Show a bounded status card because support is incomplete, stale, or citation-limited. |
| `ABSTAINED` | `ABSTAIN` | Show that no authoritative node content is available. |
| `BLOCKED` | `DENY` | Show a public-safe denial without leaking evidence or restricted details. |
| `ERROR` | `ERROR` | Show a bounded upstream/system failure without support leakage. |
| `SUPERSEDED` | `ABSTAIN` | Show correction/supersession posture and the governed replacement reference. |

`READY` may carry `correction=CORRECTED` only when correction references are present. `SUPERSEDED` must carry a replacement reference, withdrawn release posture, and correction references.

## Trust inheritance rules

### Ready content

A `READY` node requires:

- `reason_code=SUPPORTED`;
- evidence, citation-validation, policy-decision, review, and release references;
- a governed `body_ref`;
- `policy=ALLOW`, `review=REVIEWED`, `release=RELEASED`, and `freshness=CURRENT`;
- rights `CLEARED` or `GENERALIZED`;
- sensitivity `PUBLIC` or `GENERALIZED`;
- no supersession record.

A passing node still does not prove the referenced objects are genuine or authoritative. Downstream adapters must resolve them through governed interfaces.

### Partial and abstained content

`PARTIAL` and `ABSTAINED` never render a governed body. They show bounded status text and caveats only. A partial node may retain safe support references for reviewable context; an abstained node exposes no current evidence or citations.

### Blocked and error content

A `BLOCKED` node may carry a public-safe policy-decision reference, but it cannot expose evidence, citations, release, review, correction, rollback, or body references. An `ERROR` node cannot expose any support references.

### Supersession

A `SUPERSEDED` node:

- cannot answer;
- uses `reason_code=SUPERSEDED`;
- has `release=WITHDRAWN` and `correction=SUPERSEDED`;
- carries at least one correction reference;
- names a different governed replacement node;
- exposes no prior evidence, citation, body, review, release, or rollback reference.

The replacement node is validated independently. This profile does not silently copy trust from the prior node to the replacement.

## Public-safe fields

| Field group | Meaning |
|---|---|
| Identity | `profile`, `id`, `version`, optional `spec_hash`, `manifest_ref`, `node_type`, `order_index` |
| Finite posture | `state`, `outcome`, `reason_code` |
| Display | `title`, `summary`, `accessibility_label`, `caveats`, optional `body_ref` |
| Context | `map_context_refs` |
| Support | Evidence, citation, policy, release, review, correction, and optional rollback references |
| Trust | Rights, sensitivity, policy, review, release, freshness, and correction |
| Lineage | Optional `supersession` replacement record |
| Authority guard | `authoritative=false`, `projection_only=true` |

## Validation boundary

The validator proves only bounded local conformance:

- Draft 2020-12 schema validity;
- closed-field shape;
- bounded and duplicate-safe JSON parsing;
- finite state/outcome/reason combinations;
- ready-support closure;
- non-ready body suppression;
- blocked/error support non-leakage;
- rights/sensitivity/release/review fail-closed behavior;
- corrected and superseded lineage requirements;
- deterministic fixture replay without network.

It does not verify source authority, EvidenceBundle resolution, citation content, policy execution, reviewer identity, release authenticity, correction authenticity, API/UI wiring, deployment, or publication.

## Directory Rules basis

This slice reuses established responsibility roots:

- semantic meaning under `contracts/ui/`;
- machine shape under `schemas/contracts/v1/ui/`;
- synthetic cases under `fixtures/ui/`;
- reusable validation under `tools/validators/ui/`;
- enforceability under `tests/validators/`;
- hosted orchestration under `.github/workflows/`;
- authoring provenance under `data/receipts/generated/`.

No new root or parallel evidence, policy, review, release, correction, proof, or publication authority is created.

## Rollback

Before merge, close the feature pull request and delete only its branch. After an authorized merge, revert the bounded packet and restore the prior contract and schema blobs:

- contract: `ecacd7d0e23926a5ee1c058ed06b9b22a6e46e8e`;
- schema: `2a95ad3efada4f151e45358b3aeaa1df59563e12`.

No live source, lifecycle record, API route, UI component, release, cache, deployment, or public artifact requires rollback.

<p align="right"><a href="#top">Back to top</a></p>
