
# USDA PLANTS Guarded Live Watcher Layer

## Purpose
Manual guarded live-fetch/watcher layer.

## Lifecycle placement
RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → RELEASE_CANDIDATE → PUBLISHED.

## What this layer adds
Guarded live fetch, snapshot lock/diff, watcher receipt, PR handoff.

## What this layer does not do
No publish, no promote, no automatic scheduling.

## Live-fetch guards
Explicit flags + operator ack + env vars required.

## CI no-network guarantee
CI does not fetch real USDA endpoint.

## Snapshot lock model
Locks RAW inputs before processing.

## Snapshot diff model
Review support only, not approval.

## Manual watcher flow
Runs intake through release candidate and handoff.

## PR handoff model
Manifest only; does not open PR.

## Policy gates
OPA policies deny publication/promotion claims and unsafe network.

## GitHub Actions manual workflow
workflow_dispatch only; offline/operator modes.

## Operator instructions
Use offline/mock in CI and local mock-server tests.

## Failure and quarantine behavior
Fail closed and emit receipts.

## Future scheduled watcher path
Future work.

## Future publication path
Future work including public map publication.
