<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://fixtures/ui/watcher-registry-browser-projection
title: Watcher Registry Browser Projection Fixtures
type: fixture-readme
version: v0.1.0
status: proposed; synthetic; non-authoritative
owner: OWNER_TBD - Explorer, watcher, and source stewards
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; fixture-only; no-network
owning_root: fixtures/
responsibility: synthetic positive and negative packets for the Watcher Registry browser adapter
truth_posture: CONFIRMED synthetic fixture shapes only; production data and public use need verification
related:
  - ../../../apps/explorer-web/src/adapters/WatcherRegistryBrowserProjection.ts
  - ../../../apps/explorer-web/src/features/watcher_registry_browser/README.md
  - ../../../contracts/source/watcher_registry.md
[/KFM_META_BLOCK_V2] -->

# Watcher Registry browser projection fixtures

Synthetic, no-network envelopes for an unmounted Explorer browser. They are
display-contract examples only. They do not read or alter the control-plane
registry, run a watcher, activate a source, write lifecycle data, evaluate
policy, approve review, release, deploy, publish, or authorize public use.
