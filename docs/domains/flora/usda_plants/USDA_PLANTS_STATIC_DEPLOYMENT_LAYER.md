# USDA PLANTS Static Deployment Layer

This layer is artifact-first: static packaging is built and validated without requiring publication to a live endpoint.

## Operating model
- Artifact-only static packaging is the default deployment posture.
- Publication to GitHub Pages is guarded and explicit.
- Deployment and publication are separated: build artifacts can pass policy and tests without being published.

## GitHub Pages guarded deployment
- A GitHub Pages deployment manifest is generated with required permissions (`contents: read`, `pages: write`, `id-token: write`).
- The manifest declares `uses_long_lived_secrets: false` and `requires_environment_protection: true`.
- Local/test mode keeps `deploys: false`.
- The Pages workflow is `workflow_dispatch` only and `deploy_to_pages` defaults to `false`.

## No-network/no-secrets posture in tests
- Tests run with no live USDA fetch, no Census fetch, and no external basemap fetch.
- Tests do not perform a real deployment.
- No long-lived secrets are used.

## Protection and policy
- Protected environment `github-pages` is required for deployment.
- Repository environment reviewers must be configured in GitHub settings; workflow YAML alone cannot enforce reviewer assignment.
- OPA policy denies unsafe deployment packets, including missing Pages permissions, missing environment protection, long-lived secret use, auto-merge claims, and raw/work/quarantine refs.

## Rollback and audit
- Rollback remains artifact-addressable and policy-governed.
- Audit trails continue through deployment manifests and deployment-chain artifacts.
