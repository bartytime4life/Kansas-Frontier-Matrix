<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://docs/intake/exploratory/pass-31-watcher-registry-browser-source-map
title: Pass 31 Watcher Registry Browser Source Map
type: exploratory-source-map
version: v0.1.0
status: proposed; implementation-bounded; non-authoritative
owners: [kfm-maintainers]
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; exploratory; public-safe-projection
owning_root: docs/
responsibility: source-to-repository reconciliation for the bounded Watcher Registry browser adaptation
truth_posture: CONFIRMED source and repository reconciliation; PROPOSED fixture-backed implementation
source_ideas: [KFM-P31-FEAT-0019]
related:
  - ../../../contracts/source/watcher_registry.md
  - ../../../schemas/contracts/v1/source/watcher_registry.schema.json
  - ../../../control_plane/watcher_registry.json
  - ../../../apps/explorer-web/src/adapters/WatcherRegistryBrowserProjection.ts
  - ../../../apps/explorer-web/src/features/watcher_registry_browser/README.md
  - ../../../fixtures/ui/watcher_registry_browser_projection/README.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
[/KFM_META_BLOCK_V2] -->

# Pass 31 Watcher Registry Browser Source Map

## Source candidate

| Candidate | Source statement | Source spec hash |
|---|---|---|
| `KFM-P31-FEAT-0019` | KFM should provide a registry browser for watcher identity, canonical identity, endpoint, poll mode, policy, outputs, schema URL, spec hash, and signature reference. | `sha256:fe9b1d2a9e4f1d20fa68a4c9ec48dfdb62a47bdc4d2d07098e13a8914248f9e07` |

The card was verified in the supplied consolidated Pass 23-32 atlas and in the
connected Google Drive atlas corpus. Both are candidate architecture sources;
neither proves repository implementation or watcher activation.

## Repository reconciliation

Current `main@590d3b77dcfd0792fbd183e0b2e1ca4c2d39a581` contains the Watcher
Registry semantic contract, strict schema, inactive control-plane projection,
deterministic validator, synthetic fixtures, tests, and read-only workflow.
The Explorer application has no watcher-registry adapter, feature, unit test,
or browser fixture, and repository/PR search found no competing implementation
for this card.

The existing source-availability watchlist is not equivalent: it presents
source health and material-change routing. This slice presents declared watcher
identity and non-authority state without probing source availability or
creating candidate work.

## Bounded adaptation

The implementation provides:

- exact-field parsing for one public-safe Watcher Registry projection;
- finite available, abstain, deny, and error outcomes;
- canonical ordering and unique watcher/canonical identities;
- placeholder and inactive-state coherence checks;
- opaque references and fixed-false authority flags;
- a non-interactive table of the fields named by the source card; and
- fixture-backed unit and browser coverage for positive and negative paths.

## Source pressure and response

| Source pressure | Bounded repository response |
|---|---|
| Browse watcher identity and version | Display only entries supplied by a closed projection. |
| Inspect endpoint, policy, schema, outputs, spec hash, and signature | Display opaque references and precomputed values; resolve none. |
| Inspect poll mode | Display a finite declaration; do not schedule or execute. |
| Make state visible | Limit this slice to the existing proposed-inactive registry and non-active entries. |

## Directory Rules basis

The adapter and feature remain under `apps/explorer-web`; synthetic packets
remain under `fixtures/ui`; executable tests remain with the Explorer
application; source reconciliation remains under `docs/intake/exploratory`;
and the generated receipt remains under `data/receipts/generated`. These are
existing responsibility roots under accepted ADR-0029 and Directory Rules v2.
No new or parallel registry, source, schema, policy, lifecycle, receipt,
release, or publication home is created.

## Explicit non-effects

This packet does not read or mutate the control-plane registry, resolve a
source, contact an endpoint, schedule or execute a watcher, activate a source,
admit data, classify change, write lifecycle state or receipts, evaluate
policy, approve review, release, deploy, publish, or authorize public use.
Malformed or contradictory input fails closed without reflecting unknown
fields.

## Rollback

Close the draft or revert the additive adapter, feature, fixtures, tests,
source map, and receipt. No watcher, source, lifecycle, review, release,
deployment, or publication state changes.
