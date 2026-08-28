<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/tools-validators-habitat-flora-underscore-readme
title: tools/validators/habitat_flora README
type: compatibility-readme
version: v0.1.1
status: repository-grounded draft; documentation-only HOLD
owner: OWNER_TBD — Habitat steward · Flora steward · Validator steward
created: 2026-08-28
updated: 2026-08-28
policy_label: repository-facing; habitat; flora; validator-routing; non-authoritative; fail-closed
owning_root: tools/
responsibility: classify the empty habitat_flora validator path without creating a parallel validator implementation or authority home
truth_posture: cite-or-abstain
related:
  - ../README.md
  - ../domains/habitat/README.md
  - ../domains/flora/README.md
  - ../../../docs/doctrine/directory-rules.md
notes:
  - "This directory contains only README.md and .gitkeep; no executable validator is claimed."
  - "No hyphenated habitat-flora peer was verified at the reviewed baseline."
[/KFM_META_BLOCK_V2] -->

# `tools/validators/habitat_flora/` — compatibility hold

Status: documentation-only compatibility scaffold; executable ownership is unresolved.

This directory previously contained an empty README and `.gitkeep`. File presence did not establish a Habitat × Flora validator, registry entry, command, test, fixture, workflow, policy decision, or release gate.

## Current routing

- Domain-specific Habitat validation is indexed by [`../domains/habitat/README.md`](../domains/habitat/README.md).
- Domain-specific Flora validation is indexed by [`../domains/flora/README.md`](../domains/flora/README.md).
- Shared validator mechanics remain under the established `tools/validators/` responsibility root.

No paired `tools/validators/habitat-flora/` implementation was verified at the reviewed baseline. Until a reviewed path decision establishes a distinct cross-domain responsibility, new validator code is held here. Do not infer a canonical paired lane from this underscore path or create a hyphenated peer merely for naming symmetry.

## Authority and sensitivity boundary

This path does not define Habitat or Flora meaning, source roles, botanical occurrence truth, habitat suitability truth, sensitivity or geoprivacy policy, EvidenceBundles, receipts, proofs, lifecycle data, release decisions, public map products, APIs, or AI answers. Any future cross-domain validator must preserve source-role separation and fail closed for sensitive, rare, private-land, culturally restricted, or reconstructable location material.

## Validation and rollback

For this documentation-only repair, verify the two relative routing links, confirm the directory still has no executable files, validate the metadata block and Markdown structure, and check for trailing whitespace and a final newline.

Rollback by reverting this README. No validator behavior, policy, fixture, workflow, release, deployment, promotion, or publication state changes.
