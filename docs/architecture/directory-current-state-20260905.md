<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/architecture/directory-current-state-20260905
title: Directory Current-State and Cleanup Review
type: inventory-review
version: v0.1.0
status: proposed; non-normative; commit-pinned
owners: ["@bartytime4life"]
created: 2026-09-05
updated: 2026-09-05
policy_label: public
owning_root: docs/
responsibility: Bounded source, build, capability, test and cleanup inventory; no adoption or publication authority.
repository: bartytime4life/Kansas-Frontier-Matrix
base_commit: 8b9c52d88687986879c8f87d7e3835f6a58bbacd
base_tree: c49c300a7102600c22ce5486f2d44c36ecf84d56
related:
  - ../adr/ADR-0039-directory-build-and-verification-profiles.md
  - ./directory-implementation-profiles.md
  - ../doctrine/directory-rules.md
[/KFM_META_BLOCK_V2] -->

# Directory current-state and cleanup review

**Layer C / NON-NORMATIVE.** Source observations are `CONFIRMED` within their stated scope; recommendations and acceptance criteria are `PROPOSED`. Missing evidence is `UNKNOWN` or `NEEDS VERIFICATION`. Updating this inventory cannot adopt architecture, activate a source, approve a migration, or promote data.

## 1. Source and inventory boundary

The current review base is [main at 8b9c52d8](https://github.com/bartytime4life/Kansas-Frontier-Matrix/commit/8b9c52d88687986879c8f87d7e3835f6a58bbacd), tree `c49c300a7102600c22ce5486f2d44c36ecf84d56`. The earlier discovery anchor `cbd6d82b...` is not the authoring base.

A complete tracked path/mode/blob inventory was captured from `d1b430ca51887777766050e5582659ab34322286` by [run 33986784702](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/33986784702), attempt 1, at `2026-09-05T19:20:06.148402Z`. The bounded source archive contains 8,188 exact UTF-8 payloads whose Git blob identities and SHA-256 digests were independently checked locally. It excludes 6,285 payloads at that source revision, including large/nonselected documentation, trust instances, binaries and environment inputs. It is not a full local checkout.

Current-main reconstruction applies only the verified #4304 delta: Workers README blob `cec6fc51bfef930039d006fac78cb9fd2e51f93b` and new receipt blob `b2d206a26020b18a25d5452770e3e6a36c8c0732`. Re-encoding all Git tree entries reproduces current root tree `c49c300a...`. Inventory JSON SHA-256 is `5dc4c172dfeb5c041140f3159d28e75cc5ad2f11629c8f0441e37489c0609461`; reconstruction time was `2026-09-05T20:44:10.715275Z`. The new receipt's size is unmeasured in that inventory; its blob identity is verified. Tracked paths are complete; payload inspection and external-consumer closure are not exhaustive.

| Measured surface | Result | Limitation |
| --- | --- | --- |
| Tracked files / responsibility roots present | 14,474 / 24 | Presence is not canonicality or functionality. |
| READMEs / `.gitkeep` files | 2,593 / 1,205 | Not a deletion license. |
| Filename-classified placeholder-only leaves | 1,271 at d1; #4304 does not change leaf membership | README/`.gitkeep` classification only, not exhaustive dead-code analysis. |
| READMEs larger than 32 KiB | 663 | Size is a review signal, not proof of useless repetition. |
| Markdown larger than 1 MiB | One consolidated atlas, 1,065,803 bytes | Research/lineage retention must be checked before restructuring. |
| Tracked payload larger than 4 MiB | `data/processed/water_planning/rac_regions/kwo_rac_regions_2026-06-24.geojson`, 9,995,739 bytes | Payload not copied or semantically reviewed; reviewed-exception and retention status unknown. |
| NFC/case-fold path collisions | Four pairs | Naming collisions alone cannot choose the semantic winner. |

The four pairs are `contracts/source/SOURCE_DESCRIPTOR.md` / `source_descriptor.md`, and `docs/standards/CANONICALIZATION.md`, `OAI-PMH.md`, `STAC.md` versus their lowercase names. Root `catalog/` and `artifacts/` are present. Historical `ui/`, `web/`, `jsonschema/`, `policies/`, `styles/` and `viewer_templates/` roots are absent in this tracked tree; do not recreate them from PDFs.

## 2. Authority and adoption ledger

| Source / exact identity | Supported claim | Limitation |
| --- | --- | --- |
| `docs/doctrine/directory-rules.md`, blob `fd49a0b83e55cef52c1124281f093e263526898d`, SHA-256 `44f7e94344cb42b630008eb0bc03a13fcb97dbdfba6f3e56579693a272571e6e` | Effective exact-byte standard when read with ADR-0029; 94 distinct rule IDs | Its internal draft label is preserved historical content, not a reason to change the digest. |
| ADR-0029, blob `a4de0d7a96b78da59cfc499d1025e1508afd8dd9` | Accepted exact bytes and single writable doctrine home | Historical checkpoints in the record do not become current merely by fetching today. |
| `docs/architecture/directory-rules.md`, v2.0-tombstone.1 | Actual read-only compatibility tombstone; legacy fragments retained | Physical deletion remains held; external consumers unknown. |
| ADR index at this base | 38 numbered records; 0006, 0007, 0029, 0038 accepted; 34 proposed | ADR-0005 is still proposed; comments calling an app canonical do not accept it. |
| Root/alias projections and directory validators at this base | Adopted digest binding, existing alias mechanism and 20-rule topology engine | Proposed successor text is not active enforcement. |
| Issue #4228, body and latest comment `5553628883` at `2026-09-05T17:43:56Z` | Stage 1A accepted, Stage 1B HOLD, Stage 2 unauthorized; prior provenance mismatch retained | Neither this amendment nor a new test result grants the held transition. |
| Issue #4024, closed metadata with retained open-incident body; latest comment `5549171639` | Branch-first authoring and separated draft delivery remain the inspected containment posture | Closed metadata is not proof of control exit or safe draft creation. |

GitHub sources were fetched during this September 5 session; the connector does not provide exact per-read observation timestamps. The run timestamps above describe original executions, not fresh runs. CODEOWNERS routes to `@bartytime4life`; independent approval and stewardship assignment remain unproved.

## 3. Actual application and package roles

| Surface | Inspected implementation and inputs | Classification / limits |
| --- | --- | --- |
| `apps/explorer-web/` (354 files) | Vite/TypeScript DOM composition: `index.html` -> `src/main.ts` -> `src/site/mount-explorer-site.ts`; root pnpm workspace; strict typecheck/Vite build; Vitest and Playwright selectors | Active bounded fixture implementation, with local scaffolds. The composition imports `createNullMapRuntime`; concrete adapter browser fixtures are not proof of default production rendering. |
| `apps/kansas-frontier-matrix-explorer/` (61 files) | Next/React app-router conventions built with Vinext/Vite/Cloudflare; `app/page.tsx`, `layout.tsx`, `worker/index.ts`, `build/sites-vite-plugin.ts`, `.openai/hosting.json` and local authentication helper | Different composition/hosting adapter, with demonstration data and bounded local interactions. Repository build does not prove the deployed Site version. |
| `packages/maplibre/` (13 files) | `@kfm/maplibre`; manifest pins `maplibre-gl` 6.6.0. Root export supplies neutral port/terrain/null runtime; separate `./adapter` and `./vite-adapter` exports; package-local tests | Reusable implementation with explicit acquisition boundary. Vite adapter configures the package-owned worker URL. Importing the neutral root is not actual renderer acquisition. |
| `packages/temporal/` (6 files) | Python package with `src/temporal/core.py`, normalization, identity, frame/request/commit/failure interfaces | Reusable temporal kernel; not a JavaScript animation package. Explorer's TypeScript temporal implementation is a distinct consumer-side implementation. |
| `apps/packages/` (2 files) | README and `.gitkeep`; no package manifest or implementation | Dormant workspace anomaly, not root `packages/` and not a verified duplicate. Retain until writers/consumers and retirement authority close. |
| `apps/governed-api/` | Python WSGI `app`/`serve`, registry of GET `/bootstrap`, `/layers`, `/evidence`; handlers produce ABSTAIN envelopes; 404/405 guards and tests | Executable bounded stub, not full live evidence/source/policy service. |
| `apps/workers/` (18 files) | Eight comment-only `main.py` placeholders and ten READMEs | Background-worker scaffold; not the Sites worker or MapLibre browser worker. |

Root `package.json` declares pnpm 11.17.0 and workspace membership `apps/*`, `packages/*`. Root `build`, `test`, and `lint` deliberately report unimplemented orchestration and fail; they are not successful validation entrypoints. Preserve `pnpm-workspace.yaml` build-script decisions and the separately consumed app npm lockfile.

### Two-Explorer decision recommendation

**PROPOSED: retain the two current compositions, without renaming either, while sharing genuinely common capabilities through existing package interfaces.** The first is a Vite DOM/fixture verification surface; the second carries app-router/worker/hosting composition. Similar product names do not prove duplicate behavior. Choosing one canonical application now would add framework, feature-parity, installer and hosting migration requirements without proving those dependencies.

This interim choice costs two build/test compositions and leaves some duplicate presentation logic. Canonical convergence may later reduce that cost, but requires an accepted decision, consumer and feature-parity inventory, assembled-builder proof, compatibility plan and rollback. It does not follow from the public URL, ADR-0005's proposal, or this inventory.

Both apps alias `@kfm/maplibre` to `../../packages/maplibre/src/index.ts`; Explorer Web also aliases the Vite-adapter subpath. The Sites app's npm installer cannot manufacture that sibling source. The existing cleanup adds an early missing-source diagnostic, not a portable source assembler. Full app-only dependency closure remains a separate gap.

The inspected hosting configuration retains project `appgprj_6a870a079c1c8191abb7401ef092a181`, with D1/R2 null. Layout source retains the existing Explorer URL. These are repository inputs, not proof of saved/deployed Sites state. Linux development and proposed self-hosting are separate; no hosting migration or Site mutation occurs here.

## 4. Bounded capability-to-test view

Reuse the existing IDs in `apps/explorer-web/src/site/catalog.ts` and the Sites app's `feature-catalog.ts` / `function-registry.ts`; do not create a competing registry. Their maturity labels are source declarations, not accepted requirements or executed evidence. The criteria below are PROPOSED review criteria. Only adopted invariants and separately accepted decisions have their own authority.

Notation: **EW-U** = `pnpm --filter explorer-web test:unit` (Vitest `tests/*.test.ts`); **EW-B** = its Playwright configuration; both are reached by `ui-build.yml`. **SITE** = app `npm test` (build first, then `tests/*.test.mjs`); native app build also consumes the root workspace when invoked through pnpm. **TEMP** = `temporal-view-state-validation.yml` and registered Python/schema checks. A listed test is not marked passed merely because it exists.

| Existing ID / user outcome | Surface and stable boundary | Contract / fixture / test / CI | Acceptance and status; correction dependency |
| --- | --- | --- | --- |
| `map-navigation` / retain place | Both compositions; `MapRuntimePort.setCamera`, `getSnapshot`, `dispose` | Package port/adapter tests; EW-B `maplibre-vite-adapter.spec.ts`; accepted ADR-0006/0007 | Camera retained when panels/layers change. Port/fixture behavior present; actual default renderer and deployed persistence not proved. Roll back composition and camera serialization together. |
| `layer-search`, `layer-toggle` / discover and select | EW `filterFeatures`; Sites `LAYER_REGISTRY` and page-owned requested state | Feature projections; EW layer-manifest-admission tests; SITE source/rendered-HTML tests have narrower scope | Disclose coverage/time/availability; deny before loading. EW `features/layer_catalog` itself remains a placeholder. End-to-end requested/read-back layer admission needs actual-app proof. Preserve layer/evidence IDs. |
| `attribution-view`, `source-watchlist` / disclose sources | Sites source intelligence/metadata and EW source-availability projection | Existing source contracts and layer metadata; source-availability unit/browser cases under EW-U/B | Missing rights/source support must not become admission. Fixture disclosure present; live source clearance absent. Retain source/rights lineage. |
| `timeline-scrub` / select time | TS `normalizeTemporalQuery`, `validateTemporalViewState`; Python `normalize_temporal_query` | Tracked `contracts/common/temporal_view_state.md`, schema and common fixtures; `temporal-kernel.test.ts`; TEMP/EW-U | Preserve valid/observed/retrieval/release semantics. Main build has seven temporal compiler errors; separate M18 branch owns repair. No migration claim. Preserve serialized IDs and schema version. |
| `time-banner` / animate safely | Temporal frame interfaces `request_frame`, `commit_frame`, `fail_frame`; app time presentation | Temporal fixtures/TEMP and EW time-banner browser spec | Interrupted/stale frames cannot win. Kernel/fixture code exists; complete animated application/replay coverage unproved. Retain cancellation and frame/evidence coupling. |
| `evidence-drawer` / inspect evidence | `parseEvidenceDrawerProjection`, drawer mount; Sites evidence presentation | UI/evidence contract families, ADR-0037 proposed reconciliation; EW drawer/map-evidence unit/browser tests | Selected identity resolves correct bundle, denied/stale states disclose safely. Bounded fixtures, not live resolution. Keep correction links and redaction coherent. |
| `focus-mode-answer`, `focus-panel` / evidence-bound explanation | `resolveFocusComposedClaim`, `mountFocusComposedClaimPanel`; Sites `focusResultForState` | Existing focus request/response and projection interfaces; EW focus-composed-claim and workspace-boundary tests | Finite ANSWER/ABSTAIN/DENY/ERROR, citations and no direct provider. Fixture/local interpretive path present; live Qwen integration unproved. Roll back transport, parsers and privacy boundary together. |
| `story-node`, `story-player` / replay a story | `resolveStoryPlayer`, Sites page story state | Story public-safe projection; `story-player.test.ts`, EW-U | Preserve model/synthetic/observation and time/evidence disclosure. Resolver exists; complete camera-driven story replay not proved. Keep story/evidence versions. |
| AOI/measurement (no verified dedicated stable ID) | Sites `screenRectToBounds`, `MeasureUnit`, page-local utility surface | App helpers present; no dedicated AOI/measurement acceptance selector established | Finite geometry/units, restricted precision and reproducible area. Complete analytical measurement and tests remain NEEDS VERIFICATION, not missing by name alone. Preserve geometry/units and redaction. |
| `compare-releases`, `compare` / compare explicit contexts | `buildTemporalComparison`; EW workspace compare context; compare feature placeholder | Workspace/temporal fixtures and EW workspace-context tests | Record comparable layers/time/AOI; do not imply equivalence. Context/local projection present; complete comparison integration unproved. Keep context snapshot and evidence identity. |
| Local import (no verified dedicated stable ID) | Sites `buildLocalImportPreview`, `importPreviewAudit` | App-local GeoJSON/KML preview implementation; no dedicated browser privacy acceptance selector established | Malformed/nonfinite input rejected safely; no upload; stale preview cleared. Source exists, native privacy/negative behavior NOT RUN here. Preserve local-only state and parser contracts. |
| Workspace state (use existing `kfm.explorer.public-workspace-context.v1` profile) | `parsePublicWorkspaceContext`, `serializePublicWorkspaceContext`, URL helpers | EW workspace-context/navigation/registry tests and browser navigation spec | Reproduce supported context without protected URL data. Bounded URL-context code exists; durable saved-workspace storage and migration acceptance unproved. Retain schema/version decoding. |
| `download-export`, `export` / reproducible report | Sites `buildPublicSafeExport`; EW export feature placeholder | Export types/local checks; no full report reproducibility suite verified | Preserve input/evidence/time identities and redaction. Local export implementation does not prove a released report pipeline. Roll back recipe, serialized data and redaction coherently. |
| `settings` / safe preferences | Sites display state; EW settings feature placeholder | No dedicated preference-persistence acceptance suite verified | Preference cannot weaken policy; unknown values bounded. Missing integration/test evidence remains explicit. Preserve defaults and settings compatibility. |
| `accessibility-navigation` / keyboard/mobile use | Actual shell/panel controls; drawer/focus/time interactions | `accessibility.yml` selects eight EW-B specs | Narrow keyboard/focus tests exist; not complete WCAG, mobile/device, reflow or assistive-technology proof. Preserve focus/escape semantics. |
| `debug-proof-view`, `diagnostics` / diagnose safely | Runtime trust status and diagnostics projections; EW diagnostics placeholder | EW runtime-trust browser cases; no full long-session/diagnostic acceptance | Distinguish missing/denied/stale/unsupported without secret leakage. Bounded fixture states only. Preserve reason-code/redaction contracts. |

The complete tracked inventory verifies the referenced contract/schema paths where stated. The bounded text export does not include every semantic contract; this review does not declare those unread contracts accepted or fully analyzed. No capability row is commissioned by this amendment. Browser/GPU, visual/performance, mobile, long-session and released-operation gaps remain separate from unit test results.

## 5. Separate first cleanup and matched execution evidence

The existing [cleanup commit](https://github.com/bartytime4life/Kansas-Frontier-Matrix/commit/3d75f67e8ca48c74e1fab43b1fdebefc383e1d23), on `agent/directory-rules-build-context-20260905`, has parent `8b9c52d8...` and tree `9d51722fbe3ef8fbdc4296d0782b2e9d749d4796`. It changes exactly the build wrapper, its local test, an app-local source-context guide, and a new pending-review GeneratedReceipt. These are not part of this rules-proposal diff.

The guard returns exit **66**, `BUILD_CONTEXT_INCOMPLETE`, before invoking Vinext when the sibling MapLibre facade is absent or a directory. It preserves source ownership, app/workspace builder selection, timeout and builder exit propagation. It does not assemble a portable export, admit a dependency, prove GPU rendering or change the hosted Site. Current Directory Rules `DIR-EXEC-001` / `DIR-DEP-003` and existing app-local test placement already permit this protective slice.

| Execution / exact checked-out source | Commands and actual outcomes | Attribution and limitation |
| --- | --- | --- |
| Run `33987716411`, attempt 1, workflow head `80eef5104703268be0e9c741c240a0a0273e856a`; base job `101364246116` at 8b9c52d8 / candidate job `101364246259` at 3d75f67e | Wrapper tests 4/10 PASS; Bash syntax PASS; frozen pnpm install PASS; filtered Sites build PASS; Explorer unit tests 447 in 54 files PASS on both; Explorer production build FAIL on both | Ubuntu runner, Node 22.23.2, Python 3.11.16, Git 2.55.0. Seven identical temporal TypeScript errors remain actual failures. Workflow head is not the checked-out product SHA. |
| Same run, Python installer invocation | `--profile project-runtime` exited 2 on both | Author-side harness invocation error, not a repository regression. Preserved, then corrected in the next run. |
| Run `33988103629`, attempt 1, workflow head `1ad9f7bdf653223079e267c622c6444885119ca2`; base job `101365286188` / candidate job `101365286065`, same exact product SHAs/trees | Positional `install_python_ci.py test-dependencies` PASS; topology fixtures 23 PASS, 2 FAIL on each; independent topology command exit 1 on each; candidate native GeneratedReceipt PASS | Both runs remain failed in aggregate. Source/installer/protected-input immutability was checked; no baseline or validator weakening. |

The two topology failures are `test_cli_json_is_deterministic` and `test_live_index_matches_baseline_after_reviewed_authority_resolution`. Both independent topology reports contain the same five `FAIL_NEW_DRIFT` findings: uppercase path grammar, frozen `catalog/`, scaffold-only leaves, `data/maps/`, and the duplicated placeholder document ID. Counts are 20 rules, 127 findings, 122 baselined warnings, five new drift findings, zero invariant findings; the report's overall `FAIL_INVARIANT` label is preserved, not reinterpreted as success.

This is matched evidence for this cleanup on these exact revisions. It does not resolve the earlier #4228 run/log provenance mismatch, reproduce its 22-STAC-child-target signature, or authorize frozen-root correction. These are different observations. Native app-only npm build, real browser/GPU, full repository aggregate, live providers, deployment and release were not established by this cleanup's runs.

## 6. Cleanup dispositions and authority closure

No moves, merges, deletions or aliases are executed by the proposal. For the candidates below, current artifact identities are the path/blob pairs in the tree-verified inventory; proposed targets are explicitly conditional, not new canonical homes.

| Current surface -> disposition / target | Owner and rule basis | Writers / consumers / exposure / retention | Tests, required decision and rollback |
| --- | --- | --- | --- |
| Sites build wrapper -> same-path early source-context guard (already on separate branch) | `apps/`; DIR-EXEC-001, DIR-DEP-003 | Build maintainer; npm and pnpm builder consumers; engineering source; versioned | Ten wrapper cases plus matched native build. Root-owner/independent review; reverse wrapper/test/guide together, retain receipt history. |
| `apps/packages/` -> retain pending retirement review; no target selected | `apps/` anomaly; §§6, 17–18 | No implementation writer found in its two files; workspace glob remains relevant; external consumers UNKNOWN; retained documentation | No deletion now. Establish consumer closure and applicable retirement decision, then preserve any required pointer and reversible diff. |
| Both Explorers -> retain composition adapters; share only justified interfaces in existing packages | `apps/`, `packages/`; DIR-DEP-003 and accepted ADR-0006/0007 | Separate entrypoint/build writers and test consumers; public-facing candidate code; versioned | Canonical app migration needs ADR, parity, builder, compatibility and rollback evidence. No move here. |
| Four case-fold pairs -> compare semantics/writers before choosing target | `contracts/` and `docs/`; §§13, 17–18 | Semantic and documentation writers may differ; imports, links/fragments and external consumers not closed; durable | Identity/alias/retention decision required before retirement. Preserve old paths/fragments and reversible mapping; no name-only deletion. |
| 663 oversized READMEs / consolidated atlas -> responsibility-specific reductions only after content/lineage review | `docs/` and owning roots; §16 | Many distinct owners/consumers; public engineering docs; historical retention varies | Avoid mass rewrite. Preserve anchors, claims and evidence. Validate each selected link/claim change, not a filename-based purge. |
| Root pnpm lock + Sites npm lock -> retain | Root/app installer owners; existing build inputs | Both have demonstrated installer consumers; supply-chain and reproducibility inputs | esbuild branch owns overlapping dependency changes. No upgrade/deletion/policy edit here; revert paired inputs coherently. |
| Large RAC-region GeoJSON -> investigate reviewed exception/external locator, not move now | `data/processed/`; §§11, 15 | Data producers/consumers, sensitivity and retention not audited | Data migration requires identity/integrity/retention/rollback closure; no production-data change or source admission. |
| Frozen `catalog/`, aliases and correction register -> HOLD, no new target | ADR-0029/0038 and #4228 | Compatibility readers and audit consumers remain; immutable/frozen responsibility | Stage 1B/2 and strict-shrink rules unchanged. Never restore conflict markers, refresh fingerprints or delete redirects to get green. |
| ADR summary drift in `docs/adr/README.md` and `docs/registers/ADR_INDEX.md` -> bounded future pointer/current-state repair | `docs/`; existing canonical INDEX ownership | Human readers; historical snapshots must remain labeled | Current index is updated for this proposal; old count summaries remain an explicit follow-up, not a second rewritten index. |

For any later actual relocation, record the exact old/new identity, all known writers and consumers, exposure, retention, affected selectors, authority and rollback before execution. Unknown external consumers remain a limitation, not deletion authority.

## 7. Overlap and cross-platform lineage

The open-PR collection returned zero during this review; branch-only work exists. The M18 temporal branch is a five-path repair based on the same main and is excluded. The esbuild branch changes paired dependency inputs and related tests/workflow/receipts and is excluded. The Layer Library branch advanced during this review to `02589b67f4117393856a8e7a74871f8f439243bd`; a fresh comparison includes page/layout composition changes, unlike the older dormant `34a9348c...` checkpoint. Its runtime validation is not assessed here. No selected proposal path overlaps those bounded comparisons. This is not an exhaustive stale-branch audit.

Drive Directory Rules document `1uTqdIEFZE2cq3gyISetoRYM6LIlnKqTc3FobtEx7Cbs`, revision `ANLCKQmmHi1UtK_YrEhgUD_Ngx0M-cdaNP6Q1Ru_dvMTESaB2wdO3EYyJ9dG9QxsP0kxgkVbKF8Mbv0FAHLdGEDOkIvaMydxqwpoXVobVtk`, supplies unversioned responsibility-root lineage. Its equivalence to any historical PDF bytes is not asserted. The April 26 revised MapLibre manual and April 30 Pipeline Manual v0.3 explicitly distinguish design from then-unknown repository implementation; their no-repository statements are historical, not current absence claims.

Notion Workbench `3c9a9202-1bf6-8195-b8b1-f3a8d694b447`, returned as of `2026-09-05T20:10:23.412Z`, is coordination. Its M18, esbuild and Layer Library receipts remain historical within their scopes. GitHub controls implementation; no Drive or Notion mirror is updated or presented as adoption.

## 8. Correction, validation and remaining transitions

The earlier standalone `kfm_directory_rules_unbound_candidate.zip` and final handoff incorrectly said that no repository reads, branches or validation existed. The recovered branch, exact source archive and matched hosted logs contradict that statement. Preserve the earlier artifact as a superseded erroneous handoff; this inventory corrects the factual record without rewriting any original receipt.

The rules proposal is documentation plus an inert replacement patch, not active enforcement. Validate its full candidate reconstruction, predecessor digest, stable IDs/anchors, ADR/index coherence, changed-path links, receipt hashes and protected-input preservation. Report full native candidate validation separately; the cleanup's prior passes do not certify the proposal.

Required later transitions: independent proposal review; explicit exact-byte acceptance; authorized coherent authority/projection/enforcement cutover; independently scoped application convergence or path retirement; separately approved source/data/hosting/release work. Branch delivery is none of these. Proposal rollback removes the unadopted packet/index row without changing the active standard. Cleanup rollback is the separate four-path behavior/documentation unit with its historical receipt retained. Data and deployment rollback are neither required nor performed by this task.
