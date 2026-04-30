---
kfm_meta:
  version: 2
  status: draft
  domain: flora
  layer: usda_plants_scheduled_observer
  rights: public
  promotion_state: not_promoted
  publication_state: not_published
  network: scheduled_observe_only
  ci_network: disabled_for_pytest
  sensitivity: public
  source_id: usda_plants
  source_uri: https://plants.sc.egov.usda.gov/downloads
---
# USDA PLANTS Scheduled Observer Layer
## Purpose
Observe-only scheduled checks that emit review artifacts only.
## Lifecycle placement
Before RAW promotion and before release candidate generation.
## Observe-only rule
Does not publish, promote, open PRs, merge, or create release candidates.
## Scheduled workflow behavior
Runs observer, alert, queue, artifact bundle.
## Watch-state model
Caches previous observed metadata/checksums.
## Scheduled observation model
Captures discovered resources and change summary.
## Change alert model
Summarizes review-needed changes.
## Reviewer queue model
Creates human queue item; manual watcher remains release-candidate path.
## Artifact bundle model
Lists observation artifacts for upload.
## Policy gates
Deny publication/promotion/auto PR claims and non-USDA source/network misuse.
## CI and pytest no-network guarantee
Pytest uses fixtures; no real USDA calls.
## Human review path
Human review required before guarded manual watcher.
## What is intentionally not implemented
No county geometries, no publish, no promote.
## Future work
Publication path remains future work.
