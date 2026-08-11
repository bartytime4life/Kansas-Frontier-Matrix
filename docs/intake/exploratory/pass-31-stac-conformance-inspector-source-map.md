<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://docs/intake/exploratory/pass-31-stac-conformance-inspector-source-map
title: Pass 31 STAC Conformance Inspector Source Map
type: exploratory-source-map
version: v0.1.0
status: proposed; implementation-bounded; non-authoritative
owners: [kfm-maintainers]
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; exploratory; public-safe-projection
owning_root: docs/
responsibility: source-to-repository reconciliation for the bounded STAC conformance inspector adaptation
truth_posture: CONFIRMED source and repository reconciliation; PROPOSED fixture-backed implementation
source_ideas: [KFM-P31-FEAT-0004]
related:
  - ../../../schemas/contracts/v1/stac/kfm-profile-v1.schema.json
  - ../../../tools/validators/stac/validate_kfm_profile_v1.py
  - ../../../apps/explorer-web/src/adapters/StacConformanceInspectorProjection.ts
  - ../../../apps/explorer-web/src/features/stac_conformance_inspector/README.md
  - ../../../fixtures/ui/stac_conformance_inspector_projection/README.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
[/KFM_META_BLOCK_V2] -->

# Pass 31 STAC Conformance Inspector Source Map

## Source candidate

| Candidate | Source statement | Source spec hash |
|---|---|---|
| `KFM-P31-FEAT-0004` | Catalog maintainers should see STAC conformance classes, extension use, item identity rules, MIME types, and collection-contract completeness. | `sha256:c34f79af5deb0f320ec9eeadda8117b738fa0bc4fdb5ad6796e35539cf43eb74` |

The card was verified in the supplied consolidated Pass 23-32 atlas and in the
connected Google Drive atlas corpus. Both are candidate architecture sources;
neither proves repository implementation or catalog conformance.

## Repository reconciliation

Current `main@590d3b77dcfd0792fbd183e0b2e1ca4c2d39a581` contains the KFM STAC
profile schema, deterministic validator, synthetic positive and negative
fixtures, tests, and read-only workflow. The Explorer application has no STAC
conformance adapter, inspector feature, unit test, or browser fixture, and
repository/PR search found no competing implementation for this card.

The existing metadata compatibility and source inspection surfaces are not
equivalent: they do not present the profile checks named by this card. This
slice displays a precomputed STAC summary and does not invoke the existing
validator or inspect a catalog from the browser.

## Bounded adaptation

The implementation provides:

- exact-field parsing for one public-safe STAC inspection projection;
- finite available, abstain, deny, and error outcomes;
- canonical identity, arrays, timestamps, hashes, and finding codes;
- semantic agreement between findings and the declared inspection state;
- opaque catalog references and fixed-false authority flags;
- non-interactive tables for the fields named by the source card; and
- fixture-backed unit and browser coverage for positive and negative paths.

## Source pressure and response

| Source pressure | Bounded repository response |
|---|---|
| Inspect conformance classes | Display only finite, precomputed class checks. |
| Inspect extension use | Display one KFM profile-extension declaration; resolve nothing. |
| Inspect item identity rules | Display closed rule outcomes and finding codes; validate no source bytes. |
| Inspect MIME types | Display declared media-type checks; fetch no assets. |
| Inspect collection-contract completeness | Display bounded counts and findings for one opaque collection reference. |

## Directory Rules basis

The adapter and feature remain under `apps/explorer-web`; synthetic packets
remain under `fixtures/ui`; executable tests remain with the Explorer
application; source reconciliation remains under `docs/intake/exploratory`;
and the generated receipt remains under `data/receipts/generated`. These are
existing responsibility roots under accepted ADR-0029 and Directory Rules v2.
No new or parallel schema, catalog, validator, evidence, policy, lifecycle,
receipt, release, or publication home is created.

## Explicit non-effects

This packet does not query or mutate a catalog, read or validate source bytes,
resolve item or asset references, admit a source, create evidence authority,
evaluate policy, approve review, release, deploy, publish, or authorize public
use. Malformed or contradictory input fails closed without reflecting unknown
fields.

## Rollback

Close the draft or revert the additive adapter, feature, fixtures, tests,
source map, and receipt. No catalog, source, evidence, lifecycle, review,
release, deployment, or publication state changes.
