---
kfm_meta:
  version: 2
  status: draft
  domain: flora
  layer: usda_plants_external_cdn_deployment
  rights: public
  deployment_state: external_deploy_guarded
  network: disabled_for_tests
  deploys: guarded_optional
  sensitivity: public_static_site_only
  source_id: usda_plants
  geometry_authority: us_census_cartographic_boundary
  source_uri: https://plants.sc.egov.usda.gov/downloads
---

# USDA PLANTS External CDN Deployment Layer

## 1. Purpose
Define a guarded, optional external CDN deployment path for already-built USDA PLANTS static site artifacts.

## 2. Lifecycle placement
This layer runs after static publication artifacts are built and policy-checked, and before any optional external-host promotion.

## 3. External deployment vs static publication
GitHub Pages remains the default deployment surface. Cloudflare deployment is optional and guarded.

## 4. External host registry
External host targeting is declared through the USDA PLANTS external host registry and associated deployment manifests from Step 1.

## 5. External deployment request
A manual `workflow_dispatch` request includes `snapshot_date`, `requester_id`, `approver_id`, and optional Cloudflare deployment toggle.

## 6. External deployment approval
Cloudflare deployment requires protected environment approval via `usda-plants-external-deployment`.

## 7. CDN deployment execution plan
The dry-run job validates Step 1 tests and produces artifact evidence before any deploy gate is evaluated.

## 8. Cloudflare Pages guarded manifest
`deploy_to_cloudflare` defaults false and must be explicitly set to true. Deployment uses Cloudflare Pages Direct Upload for the prebuilt site path only.

## 9. Custom domain readiness
Custom domain readiness is tracked independently from workflow execution and must be reviewed before any DNS cutover.

## 10. Cache invalidation plan
Cache invalidation follows the external deployment chain records and is executed only after successful guarded deployment approval.

## 11. CDN deployment receipt
A deployment receipt is captured in the evidence chain for traceability and rollback support.

## 12. External verification report
Post-deploy verification artifacts are documented through external verification reports without introducing live source fetches.

## 13. Rollback and audit ledger
Rollback remains artifact-addressable and governed by the external deployment audit ledger.

## 14. Policy gates
Policy gates remain enforceable in dry-run mode, with optional OPA execution under explicit operator control.

## 15. Protected Cloudflare workflow
The Cloudflare workflow is `workflow_dispatch` only, has no schedule, no push trigger, and no pull-request deployment trigger.

## 16. CI and no-network posture
Tests never deploy. This layer does not fetch USDA data. This layer does not fetch Census data. This layer does not fetch external basemaps.

## 17. Credential posture
Environment-scoped secrets must be configured by a repo admin. Secrets must never be printed or serialized. Cloudflare secrets are passed only as action inputs to the deploy action.

## 18. What is intentionally not implemented
This layer does not auto-merge, does not auto-open PRs, and does not initiate live data ingestion or geometry refresh.

## 19. Future provider-OIDC/cloud deployment layer
OIDC is preferred for providers that support it. Future provider-OIDC deployment remains a separate layer.
