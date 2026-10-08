<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/domains/soil/release-index
title: Soil release and candidate navigation
type: domain-guide
version: v1.0
status: draft; repository-grounded; review-required
owners:
  - OWNER_TBD - Soil domain steward
  - OWNER_TBD - Documentation steward
created: 2026-10-08
updated: 2026-10-08
policy_label: public
owning_root: docs/
responsibility: Soil release and candidate navigation; human guidance subordinate to owning contracts, schemas, policy, evidence, and release decisions
truth_posture: CONFIRMED inspected repository paths and bounded implementation; PROPOSED review procedure; UNKNOWN external source and operational acceptance
related:
  - release/candidates/soil/README.md
  - data/proofs/soil/README.md
  - .github/workflows/domain-soil.yml
evidence_snapshot: ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe
[/KFM_META_BLOCK_V2] -->

# soil — RELEASE_INDEX.md

This is the human navigation index for Soil release review. It is not a release
registry or an approval. At `ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe`, the
Soil-specific candidate and proof lanes contain README files only. No completed
Soil-domain release is registered by this document.

## Current surfaces

| Surface | What is present | What remains separate |
|---|---|---|
| [Candidate lane](../../../release/candidates/soil/README.md) | Candidate boundary documentation | Candidate manifest, review and release decision |
| [Proof lane](../../../data/proofs/soil/README.md) | Domain proof navigation | Emitted proof, authenticated evidence and closure |
| [Domain workflow](../../../.github/workflows/domain-soil.yml) | Bounded fixture tests and explicit proof/release holds | Executable production release path |
| [Catalog review](CATALOG_CLOSURE.md) | Fixture-only declaration assessment | Actual resolution and catalog transition |
| [Site visual context](MAP_UI_CONTRACTS.md) | Soil-related application source and tests | Governed Soil release and hosted acceptance |

A related Agriculture manifest exists at
[`agri-soil-crop-suitability-v1-001.json`](../../../release/manifests/agri-soil-crop-suitability-v1-001.json).
It is a separate lane's artifact. Its filename or presence is not evidence that
the Soil lane has completed its own admission, proof or release requirements.
Review that manifest and its owning controls before relying on its meaning.

## Information required for a future entry

Add an index row only after inspecting the actual owning artifacts. The row
should link to, rather than duplicate, these records:

- product/candidate identity, support type, source edition and content digest;
- intended audience, geography, time coverage, units and depth support;
- source admission, rights and sensitivity results;
- EvidenceBundle and validation report bound to the exact bytes;
- policy and independent review results;
- release decision and manifest, if they actually exist;
- public carrier or governed route and readback status;
- correction/withdrawal reference and rollback target;
- exact repository revision and separately observed deployment identity.

Use distinct values for proposed candidate, pending review, approved decision,
released artifact, deployed version and browser acceptance. Do not collapse
these states into a single green status.

## Review and failure workflow

1. Start with the [definition of done](DEFINITION_OF_DONE.md) and compare the
   proposed claim to available evidence.
2. Confirm artifact digests and references through their owning surfaces.
3. Evaluate the actual release process only if it exists and is authorized.
   Current workflow hold checks must remain visible.
4. If a candidate appears in a previously empty lane, wire its validator and
   tests deliberately; do not remove a hold merely to make CI green.
5. Record a pending entry or evidence gap when verification stops short. A
   successful fixture test alone never creates a release entry.

## Correction and rollback

Keep past entries and mark supersession, withdrawal or correction with links.
A previous Site deployment, a Git revert and a governed data rollback are
separate operations. Restore only an exact previously verified target under its
own authority, then verify affected consumers. If no safe prior state exists,
record the explicit unavailable/empty state instead of silently serving a stale
candidate.
