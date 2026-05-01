# eBird Layer 38: Checkpoint Restore and Continuity

Layer 38 adds **local-only** checkpoint restore simulation and synthetic continuity drills.

- No network calls.
- No credentials.
- No real eBird data.
- No release latest/stable pointer mutation.
- No deployment pointer mutation.

## CLIs
- `kfm-ebird-checkpoint-restore`
- `kfm-ebird-continuity-drill`

## Deterministic IDs
- `restore_id`: first 16 hex chars of sha256 over canonical restore planning payload.
- `continuity_drill_id`: first 16 hex chars of sha256 over canonical continuity planning payload.

## Public-safety rules
Public outputs must keep `public_safe=true`, `exact_points=restricted`, and never expose exact coordinates, restricted paths, quarantines, suppression receipts, suppressed group hashes/details, raw rows, or secrets.

## Contracts
Layer 38 emits restore plans/manifests/receipts/verification and continuity plans/results/readiness plus public summaries.

## Warning
This layer performs simulation and validation only; it does not download eBird data or publish private artifacts.
