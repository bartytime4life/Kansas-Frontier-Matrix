<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/root-registry/v1
title: Root Registry Contract
type: semantic-contract
version: v1
status: draft
owners: ["@bartytime4life"]
created: 2026-08-07
updated: 2026-08-07
policy_label: public
related:
  - "../../docs/doctrine/directory-rules.md"
  - "../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md"
  - "../../control_plane/root_registry.yaml"
  - "../../schemas/contracts/v1/governance/root_registry.schema.json"
  - "../../tools/validators/directory_governance/validate_root_registry.py"
tags: [kfm, governance, directory-rules, root-registry, machine-projection]
notes:
  - "Projection-only contract. The register cannot amend doctrine, create a root, activate a conditional root, authorize writes, migrate paths, or grant release/publication status."
[/KFM_META_BLOCK_V2] -->

# Root Registry Contract

## Purpose

`RootRegistry` is the machine-readable projection of the adopted KFM Directory Rules root classes and current top-level repository-root classification. It makes root identity, primary responsibility, class, write posture, governing decision, canonical target, activation/exit conditions, and validation profile inspectable without turning the projection into authority.

The human-readable Directory Rules and accepted decisions remain normative. The register must cite their exact identity and digest. A register edit cannot self-authorize a new canonical, conditional, or compatibility root.

## Authority boundary

A valid register proves only that:

- the instance conforms to the root-registry schema;
- root IDs and paths are unique and canonically ordered;
- the adopted Directory Rules digest and `ADR-0029` binding are present;
- canonical roots required by the adopted rules are projected;
- every top-level directory at the pinned repository base is classified;
- class/status/target/activation/exit combinations are internally consistent.

It does **not** prove that a root should exist, that a migration is authorized, that a compatibility root may accept independent writes, that data is admissible, or that any release/publication gate has passed.

## Register fields

The register carries shared `entry_defaults` and `class_defaults` so repeated authority metadata is normalized without changing the resolved root-entry shape. The validator expands those defaults before applying invariants.

The register carries:

- version, status, projection-only authority, update date, and pinned `base_ref`;
- a doctrine reference with canonical path, document ID, SHA-256, and accepted decision;
- verified owner/reviewer routing;
- explicit non-effects;
- one ordered `roots` entry per classified top-level directory.

Each root entry follows Directory Rules §19.2:

- `root_id`, `path`, `class`, and one primary `responsibility`;
- allowed and prohibited artifact kinds;
- permitted writers and dependency-rule references;
- exposure, mutation, retention, owner, and reviewers;
- governing decisions and source digest;
- optional canonical target;
- activation conditions, exit conditions, validation profiles, and finite status.

## Class invariants

- `canonical` and `platform` entries are active and have no canonical target.
- `conditional` entries carry activation and exit conditions. A `PROPOSED` conditional root is tracked but gains no new authority.
- `compatibility` entries have a canonical or external target, no-independent-write profile, and an exit condition.
- `deprecated` entries have a target, frozen-write profile, exit condition, and `DEPRECATED` status.
- `retired` entries are non-writable historical identities and use `RETIRED`.
- Every entry cites the adopted Directory Rules digest and `ADR-0029`.

## Current brownfield posture

The pinned instance classifies the adopted canonical/platform roots plus the observed brownfield roots:

- `artifacts/` as a generated-output compatibility transition;
- `catalog/` as a deprecated containment root targeting `data/catalog/`;
- `src/` as an unresolved conditional facade candidate with no new authority.

These classifications preserve drift visibility. They do not perform migration or permit new authority-bearing content.

## Validation outcomes

The validator emits:

- `PASS` — projection is internally consistent and matches the checked top-level roots;
- `FAIL_NEW_DRIFT` — an unregistered root, missing active root, or new projection mismatch is found;
- `FAIL_INVARIANT` — digest, class/status, target, uniqueness, or authority invariant is violated;
- `HOLD_UNRESOLVED` — required authority or decision evidence is absent;
- `ERROR_VALIDATOR` — the validator cannot evaluate safely.

## Rollback

Rollback is removal of this additive contract/schema/register/validator/fixture/test/workflow packet. No root is created, moved, renamed, retired, or deleted by the packet, so rollback requires no lifecycle migration or public-state reversal.
