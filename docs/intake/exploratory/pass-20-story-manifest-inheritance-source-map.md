<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake-pass20-story-manifest-inheritance-source-map
title: Pass 20 StoryManifest Composite Trust Inheritance Source Map
type: exploratory-source-map
version: v1.0.0
status: proposed; source-grounded; non-authoritative
owners: OWNER_TBD — Intake steward · UI steward · Story steward · Evidence steward
created: 2026-08-10
updated: 2026-08-10
policy_label: public; docs; intake; exploratory; StoryManifest; trust-inheritance
tags: [kfm, pass-20, source-map, StoryManifest, composite, trust-inheritance]
related:
  - ../../../contracts/ui/story_manifest.md
  - ../../../schemas/contracts/v1/ui/story_manifest.schema.json
  - ../../../contracts/ui/story_node.md
notes:
  - "This map records source-to-repository interpretation; it grants no truth, policy, review, release, or publication authority."
[/KFM_META_BLOCK_V2] -->

# Pass 20 StoryManifest composite trust inheritance source map

## Evidence ledger

| Source | Truth label | Relevant idea | Repository interpretation |
|---|---|---|---|
| `KFM_Pass_20_Part_2_Idea_Index_Category_Atlas_and_Expansion_Dossier.md`, Story UIX card and explicit gap section | `CONFIRMED` | Story nodes, story arcs, and time tours inherit the worst release/rights posture of constituents; inheritance remains visible; a constituent rollback updates the composite; a `composite_manifest.schema.json` is recommended. | Close the existing `StoryManifest` stub at its accepted UI paths with deterministic fixture-only reduction, limiting-node disclosure, and correction/supersession linkage. |
| Existing `contracts/ui/story_manifest.md` and `schemas/contracts/v1/ui/story_manifest.schema.json` on `main` | `CONFIRMED` | The responsibility root and public-safe display boundary already exist, but the schema requires only `id` and permits arbitrary properties. | Replace the permissive stub; do not create a new root or a second manifest family. |
| Existing StoryNode contract/schema/validator profile | `CONFIRMED` | Adjacent finite states and trust dimensions are already executable. | Reuse the vocabulary in a bounded snapshot; do not duplicate or dereference StoryNode authority. |
| Composite precedence and reduction tables in this PR | `PROPOSED` | One deterministic implementation of “worst-state wins.” | Keep fixture-only and human-reviewable; do not claim repository-wide policy finality. |

## Included

- a closed public-safe schema;
- ordered, unique bounded constituent snapshots;
- finite state/outcome inheritance;
- dimensionwise least-permissive trust reduction;
- visible limiting-node refs and reason codes;
- correction and supersession linkage;
- deterministic no-network validator, exact fixture polarity, tests, CI, and current-state receipt.

## Excluded

- narrative text, claims, coordinates, geometry, and source payloads;
- StoryNode dereferencing or body retrieval;
- evidence or citation resolution;
- policy execution, editorial approval, release, rollback execution, deployment, public use, or publication;
- any migration of existing story content or activation of a story player.

## Placement rationale

Directory governance requires responsibility-rooted paths. The semantic contract remains under `contracts/ui/`; its machine shape, fixtures, validator, tests, workflow, intake evidence, and receipt use their existing responsibility roots. This proposal creates no repository root and no domain ownership claim.
