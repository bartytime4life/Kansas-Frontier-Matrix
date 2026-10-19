# Anonymous application cleanup review follow-up — 2026-10-19

This follows the owner-requested login and unavailable-navigation removal in PR #5308. The GitHub automated review on commit `46aa8cb` identified a missing capture pause/resume path and historical-map controls calling a permanently denied private API.

## Result

- Public historical-sheet search retains USGS catalog metadata, edition/imprint dates, public viewer links, actual footprints and footprint fitting. Selecting a sheet no longer requests private overlay status, preparation, review or activation. Private raster storage and server boundaries remain closed; no private content is made public.
- Public pages no longer request the local reviewed-imagery catalog or display its unavailable controls/inventory. Dataset discovery, provider provenance and export recipes remain. The existing exact loopback-only reviewed-imagery workflow remains at `http://127.0.0.1:4173`; its server capability and integrity checks are unchanged.
- `POST /api/source-pipeline/control?action=pause|resume` is restored for the existing capture-worker machine capability. It accepts only one fixed action, uses the same bounded bearer capability as `/api/source-pipeline/run`, requires all readiness gates, writes the actor `capture-worker`, and invalidates status after success. Browser cookies and role headers confer no authority.
- Proxy readiness accepts only the canonical domain, optionally with its `www` alias. Wildcards and unrelated hosts still fail closed.

## Configuration and activation

No new account, API key or machine token is required for the public app or its hosted Qwen model. The replacement has its own provider-managed database credentials. Its three custom runtime values are `KFM_HOSTED_AI`, `KFM_HOSTED_AI_ORIGIN` and `VINEXT_TRUSTED_HOSTS`, set separately for preview and publication. Old PC-account encryption, worker and administrator secrets are not migrated.

Capture remains unconfigured and paused. This change does not migrate a database, enable a scheduler, create a worker token, confirm archive capacity or grant release authority. An operator choosing to enable capture must first satisfy `ingestionConfig`: verified DB CA/TLS and hostname, exact public origin/trusted hosts, bounded worker token, explicit ingestion enablement, published runtime role and the existing 80 GB capacity confirmation. After applying the existing migration, the initial paused state is intentional. The configured worker can then explicitly POST the `resume` action with its bearer token; `pause` uses the same capability. Neither request has a login UI or public navigation link.

## Validation and limits

Focused behavior tests exercise successful pause/resume, denied browser/forged/cross-origin requests, invalid actions and an unconfigured hold. A rendered component harness selects a public historical sheet and fits its footprint without a private API request. Hook tests verify zero private inventory requests on hosted origins and retained local inventory reads/reloads. Existing historical catalog, privacy, storage-integrity and download tests are retained. Build, TypeScript, actual HTTP boundary and CI results are recorded in the follow-up PR.

The replacement was published to an available slot on the existing Plus Launch plan. File Manager and the live default hostname matched the cleaned-up source. GoDaddy moved the existing domain after detaching its assignment from the old app; its DNS UI shows the new A record and matching certificate verification CNAME, with existing nameservers, www and policy records retained. At this document's creation the domain dashboard reported connected, while the cloud verification browser still reported a TLS handshake failure. Do not treat the dashboard alone as end-to-end HTTPS recovery; the PR records the later observed result.

Original private Site audience/data bindings, SQL history and retained files remain unchanged. No plan/domain purchase or support message was sent.
