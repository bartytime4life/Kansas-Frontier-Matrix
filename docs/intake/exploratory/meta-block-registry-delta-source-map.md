<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/meta-block-registry-delta-source-map
title: Documentation Metadata and Registry-Delta Source Adaptation
type: source-map
version: v0.1
status: exploratory; implementation-source-map
owner: TODO-docs-steward-plus-tooling-qa-owner
created: 2026-08-06
updated: 2026-08-06
policy_label: public; repository-facing; non-authoritative
owning_root: docs/
responsibility: record the evidence-led adaptation of KFM metadata and document-registry guidance into bounded no-network documentation QA without creating metadata doctrine or mutating register authority
truth_posture: CONFIRMED current repository gap and accepted placement authority / PROPOSED bounded implementation / NEEDS VERIFICATION hosted exact-head results and steward adoption of stricter profiles
related:
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/registers/DOCUMENT_REGISTRY.md
  - control_plane/document_registry.yaml
  - tools/validators/docs/README.md
  - tools/validators/docs/meta-block/README.md
  - tests/validators/docs/meta-block/README.md
notes:
  - "The source documents describe metadata and registry closure as documentation-control concerns, not truth or release authority."
  - "The implementation leaves evidence-based status-overclaim detection and registry mutation outside this slice."
[/KFM_META_BLOCK_V2] -->

# Documentation metadata and registry-delta source adaptation

## Evidence-led selection

At the inspected base, `tools/validators/docs/meta-block/README.md` described a
metadata validator but explicitly confirmed that no executable existed. The
newly landed documentation graph supplied bounded identity, reachability, and
registry-parity concepts, while `docs/registers/DOCUMENT_REGISTRY.md` required
human/machine registry synchronization but warned against silent amendment.
Accepted ADR-0029 makes the current Directory Rules bytes the operative placement
authority.

The selected increment is therefore structural documentation QA, not a broad
documentation rewrite and not a registry migration:

- validate existing `KFM_META_BLOCK_V2` envelopes when present;
- offer a separate `required` profile for future bounded adoption;
- compare valid identities with the current machine register;
- emit deterministic `ADD_REVIEW` or `HOLD_CONFLICT` candidates;
- leave authority fields unresolved rather than inventing them; and
- never mutate Markdown or the registry.

## Directory Rules basis

| Responsibility | Placement |
|---|---|
| deterministic repository QA | `tools/validators/docs/meta-block/` |
| executable synthetic evidence | `tests/validators/docs/meta-block/` |
| read-only pull-request orchestration | `.github/workflows/docs-meta-block.yml` |
| source adaptation and limitations | this file under `docs/intake/exploratory/` |
| AI authoring accountability | `data/receipts/generated/` |
| separately governed machine input | existing `control_plane/document_registry.yaml` |

No root or parallel documentation, schema, policy, registry, receipt, proof,
release, or publication authority is created.

## Bounded implementation decisions

1. **Top-level subset, not YAML doctrine.** The parser accepts the metadata forms
   already required by the lane: scalars and simple sequences. Unsupported
   nesting is visible rather than guessed.
2. **`present` before `required`.** The initial workflow validates blocks that
   exist but does not require metadata on every historical document.
3. **Structural truth posture only.** A recognized truth marker is required, but
   the tool does not decide that the document's substantive claims justify its
   status.
4. **Responsibility-root consistency.** `owning_root` must agree with the
   document's top-level path, enforcing placement evidence without creating a
   new path rule.
5. **Review-only registry delta.** Missing entries become `ADD_REVIEW` candidates
   with unresolved authority; identity/path disagreement becomes
   `HOLD_CONFLICT`.
6. **Current-change ratchet.** Changed-path failures remain blocking; inherited
   failures remain visible as historical warnings until separately classified.

## Deferred candidates

- a steward-adopted field-value and document-type vocabulary;
- evidence-based status-overclaim detection;
- explicit ignore records with owner and expiry;
- registry schema and authorized write workflow;
- automatic coordination with stale-scan and terminology-parity;
- whole-repository metadata baseline and graduation to `required`; and
- release of generated QA reports beyond ephemeral CI summaries.

## Rollback

Before merge, close the draft pull request and delete its feature branch. After
an authorized merge, revert the bounded implementation commit. The slice creates
no source activation, lifecycle data, registry mutation, release, deployment, or
public artifact.
