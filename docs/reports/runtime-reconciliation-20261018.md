# Runtime reconciliation — 2026-10-18

Status: **REVIEW_ONLY / OBSERVATIONS_ONLY**. Public publication remains **ON HOLD**. This owner-requested implementation reconciles compatible features while preserving runtime-specific code, stores, source holds and history. The agent made no PR merge, governed-data activation, access change, production-store migration or public publication occurred.

## Identity and authority

| Surface | Pinned identity | Outcome |
|---|---|---|
| Monorepo main | `326452d14ed52438cc98fd51966d6c894e16bac8` | 107 successful, three skipped checks; no failed or unfinished checks at readback |
| Installed local Node | `d6b14ec8964eae31d25cc0f099457b9e2248443a`, base `5b6e6dbaf9e6afb659649554dfe593371c715ca9` | Single existing Explorer service on port 4173; clean installation; owner-merged [#5258](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5258) |
| GoDaddy private preview | `c139713f59a8475e6154a4fb293977bbc86283b9`, base `d347a26304a878135255891a90b39659be5f888e` | Healthy, infra/site OK; exact source digest visible in About; owner-merged [#5257](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5257) |
| GoDaddy published | `4b3cc837e9c131e5eb214427e0a55646fc76e52a` | Unchanged; preview and public remain intentionally different |
| Active GPT Public Staging | v8, `084b730ca6e4e3f67af1da0426a275e7889c4603` | Saved and successfully deployed; owner-only; unchanged |

Active staging project is `appgprj_6acd1aafe0d88191a4306ea2ab44ed91`; deployment `appgdep_6ad4e5bd8d388191b3f0b8ba5ddab25c`, environment revision 2. One owner, no editors/groups/external visitors; D1/R2 bindings unchanged. Its metadata custom-domain string is not proof of GoDaddy routing. The original Explorer project was intentionally retired; its historical receipts and local v268 API capsule remain preserved.

Main's selected `site-v268-focus-mode-test-reconciliation-20261018.json` still passes **CONTENT_PARITY_ONLY**. It is not native-v8, Node or hosted equivalence. This new [observation receipt](../../data/receipts/generated/runtime-reconciliation-20261018.json) is not selected by the mirror checker and grants no release or review authority.

## Directory basis and overlap

[ADR-0029](../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts the pinned [Directory Rules](../doctrine/directory-rules.md). This document is a bounded authored synchronization checkpoint in the existing `docs/` responsibility root, following the explicitly recorded authored checkpoints in [reports/README](README.md). It adds no generated-report writer or parallel registry. The JSON is an append-only review observation under the existing receipt responsibility; no historical receipt, selector, schema, source registry or policy is replaced. Lane-wide generated-report admission remains held.

The initial comparison found 957 identical common Node paths, 88 changed common paths, 151 local-only and 66 hosted-only paths. Local/main-mirror comparison found 783 identical common paths, 84 changed common paths, 329 local-only and seven mirror-only paths. Counts describe that pinned comparison, not complete behavioral parity.

Merged #5254–#5256 work and later current branch changes were inspected. The local base includes the pinned larger Qwen model integration; the hosted base includes queue/completion work. Bounded source identity and About-guide work from `f37d4c847fef3ff3d96f321341a6de25b3953a1c` was adapted to each Node runtime. Focus Mode provenance assertions from current main were carried into the corresponding existing implementations. No whole-runtime merge or version-number winner was used.

## Feature and data reconciliation matrix

Implementation inventory is distinguished from browser or provider acceptance. Retained routes/files alone do not prove current source availability.

| Feature / responsibility | Local Node | GoDaddy Node | GPT staging / monorepo | Resolution and limits |
|---|---|---|---|---|
| Login, accounts, sessions, admin | Existing local companion/native authorization retained | Existing administrator and invited PC-research boundaries retained | Owner-only staging and governed Worker routes remain separate | Do not copy credentials, cookie state or bindings. No role/access changes; full account lifecycle not rerun |
| HUD, navigation, Appearance, measurements | Shared pointer-safe dismissal; county search ported; Underground stays in Appearance | Explore panel removed; legacy entry resolves to Appearance; Underground added; compact header retained | Existing staging controls retained | Functions remain on map; source values unchanged. Both candidate navigation checks pass |
| Source identity / guide | `/api/build` local input profile and current guide links | `/api/build` hosted input profile and current guide links | v8 already has its separate identity/guide | Fixed input roots, no runtime secrets/stores; digest is application identity, not data or deployment proof |
| Cores, wells, aquifers, locator, cutaway | 50/28 High Plains; two overlaps; public core 1001251474 renders | Same 50/28 and two overlaps; 2048 and 4096 completed | Staging has zero released sources and 56 disabled source controls | Keep verified public locations and all source-specific holds. No invented continuous geology or filled gaps |
| Water gauges, paths, flow | 3,175 directed reaches; Battery saver pauses | 3,175 directed reaches; Battery saver pauses | Governed release and mirror records remain distinct | Provider-directed display motion is not measured velocity; incomplete areas disclosed |
| Historical maps and archives | Historical topo controls/server, local map/archive and acquisition adapters retained | Shared historical displays and hosted download routes retained | Governed archive authorization and source holds retained | No new captures, archive schedule or release activation; broad provider journey not rerun |
| Earth Engine imagery | Existing context/export/download and year controls retained | Existing hosted imagery context retained | Staging controls held | Native cell values, dates, no-data and admission limits unchanged; no new exports or resolution claims |
| Weather, radar, smoke, lightning, disaster | Existing source clocks, HMS playback, NOAA radar and fire reporting retained | Existing corresponding displays retained | Source release holds retained | File inventory confirmed, not an all-feed health claim. Empty/stale sources must remain visible |
| Soil, subsurface and scientific overlays | Existing soil, almanac, land, storm/quake and research adapters retained | Hosted subset retained separately | Governed Worker validation retained | Do not silently substitute fixtures or expose private processed material; no admission/activation |
| BLM, transport and bridges | PLSS/record inspector, bridge inspector, KDOT road/rail catalog entries retained | Corresponding existing catalog entries retained | Staging availability held | Survey references are not ownership; historical/closed assets retain source-specific limits; provider coverage not rerun |
| Time, opacity, legends, source status | Record-time 2000 gives 17/11, restored all; 65% opacity; Census search leaves 2026 map time | 65% opacity and detailed cutaways retain provider dates | Held sources remain held | Distinguish display time, edition, observation and retrieval. Raster/native values unchanged |
| Reports, stories, search, downloads, exports | County result exposes 2020 edition and external-context limit; draft JSON exported | Existing hosted report/AI/investigation and download functions retained | Governed APIs and release gates remain separate | Local export is `DRAFT_NOT_PUBLISHED`; no evidence package produced. Full export matrix remains open |
| AI queue, cancel, continuation, follow-up | Local pinned Qwen3.6:35b stays loopback; one bounded interpretation completed | Existing finite queue/buffer/continuation guards retained; real running request cancelled at 390px | AI stays interpretive, source holds unchanged | No weight tuning, public PC exposure or model substitution. Full hosted completion qualification remains HOLD |
| Runtime-only assets and adapters | Native v268 capsule, terrain optimization, diagnostic overlays, local stores retained | Hosted SmolLM2, crawler/privacy and sitewide AI retained | Worker bindings and exact-geometry holds retained | Adapter compatibility, not blind file/store copying. No held geometry restored for parity |

## Concurrent owner merge readback

GitHub reports `bartytime4life` merged #5257 at 18:27:18Z as `115c3d246bb861a939a1d1f56f891d04bbb057c3` and #5258 at 18:27:32Z as `1cb2997302813e892fe51edb86bf3a75a6d33ff1`. Fresh fetch and whole-tree comparison show zero changed files between each reviewed head and its composition merge. The installed and private-preview build identities intentionally remain the tested heads, with content aligned to those merge trees. The agent did not merge either PR. Public publication remains held.

## Preservation and installation

Before mutation, private recovery snapshots retained full Git history, tracked/untracked material source/build files, permissions and hashes. The local bundle was verified; 1,920 pre-update source/build paths were recorded. All 18,469 affected external state files (920,409,107 bytes) were copied and byte/mode verified before restart. Existing dependencies (29,982 files recorded), native capsule, model and other services were preserved.

The installed checkout is clean at the local candidate. All 1,207 tracked source paths match the candidate. The prepared build has 421 current paths plus 330 retained immutable client assets, 751 total. Only the existing `kfm-explorer-local.service` was restarted. No second local service was installed. Other worktrees, prior copies and stores were not deleted or reset.

Hosted recovery retains a verified complete Git bundle and parent-source archive. A prepared private ZIP was CRC/member/hash checked but **not uploaded**: GoDaddy disables ZIP update while GitHub is connected. Existing authenticated GitHub preview configuration was changed from `a0-hosted-ai-web-20261017` to new alias `a0-reconciliation-preview-20261018`, pointing at the reviewed candidate; no existing branch was changed. User completed GoDaddy authentication. Preview updated; Published did not.

Private final tracked inventories are summarized in the receipt: local 1,207; hosted 1,118; staging 903; initial main 14,816. Full path/hash manifests, build/state manifests, screenshots and logs remain in the private task workspace, not this public repository. Credentials, private backup payloads and unreleased geometry are excluded.

## Validation and browser evidence

Both Node builds and TypeScript checks pass. Changed-area lint has zero errors, 41 local/40 hosted warnings; these warnings were not globally remediated. Local focused unit files pass (31 assertions across seven file runs), navigation checks pass, five aquifer/water preservation files pass. The initial local bridge fixture failed under sandbox listener restrictions; the authorized deterministic rerun passed all 36 bridge tests. Hosted focused checks pass, real HTTP identity/About/asset tests pass (local one, hosted two), and hosted AI queue/completion regressions pass 27/27. Full mixed-runtime suites were not rerun.

Exact reviewed-head CI: local `d6b14ec` **verify-node-composition succeeds**, run 39153995255/job 117753295125; hosted `c139713` **verify-core-delivery succeeds**, run 39153564164/job 117751999670. The owner concurrently merged both heads; see the readback below.

Chrome verified installed local and private preview source identity, fresh map rendering, tidy Appearance/Underground, independent detail controls, source counts and coverage disclosures. Local High Plains completed 2048x1333 and 4096x2667 surfaces; hosted completed 2048x1329 and 4096x2658. Different viewport aspect ratios explain pixel heights, not changed source detail. Local filtering through 2000 produced 17 records/11 columns while aquifer dates stayed 2022–2024, then all records were restored. Public core 1001251474 produced one recorded inventory-envelope column and one overlap on both local and private preview (hosted 2048x1329). No continuous lithology was inferred.

Both Node maps loaded 3,175 provider-directed major-waterway reaches and disclosed incomplete coverage; Battery saver paused motion. Local county search resolved Sedgwick from the loaded 2020 Census baseline, retained 2026 map display time and exposed no EvidenceBundle. A local report JSON downloaded successfully and parsed as `DRAFT_NOT_PUBLISHED`; the browser download observer timed out, so file verification supplied the final download evidence.

Local Qwen3.6:35b returned a bounded interpretation with ABSTAIN/evidence-limit framing and follow-up questions. Its pinned digest, finite budgets, cache settings and loopback-only operation were unchanged. Hosted cancellation reached CANCELLED and returned Send availability; a 390px viewport had no document overflow. This proves bounded interaction, not general answer completeness or accuracy.

The active GPT staging map rendered after owner sign-in, but all 56 source controls remained disabled with zero released sources. This is retained governance, not connector failure or an instruction to unblock data.

Local baseline versus candidate click-to-readback observations were approximately 16.244s and 6.456s, with uncontrolled cache/tool-roundtrip effects. **No performance improvement, FPS, GPU, cold-network or resource-budget claim is made.** Local OpenFreeMap glyph-range warnings used local fallback; browser-control deadlines were inspected separately. Full devices, assistive technology, multi-hour, cold-rollout, heap/GPU and hosted rollback remain unverified.

## Security and remaining holds

Codex Security bounded diff scans completed with no new reportable changed-area finding: local scan `8cf5b688-298b-4d7a-9c9d-44272a4146c0` covers base5b6 through application commit `dc64daa6c7ea7c4345206bd2c8106cfb294b082e`; subsequent two test-file corrections were inspected separately. Hosted scan `aab92227-b5f2-4cbd-b362-64b0abdf4cc4` covers the exact hosted candidate. This is not a comprehensive current-tree, platform or model audit.

Fresh hosted npm audit reports eight high affected-package entries and zero critical, rooted in unchanged unpatched Braces advisory `GHSA-vfj7-8cjw-p6xm`. No public request path was established; the issue is neither remediated nor accepted. Full hosted AI completion remains on hold; queue/duplicate guards and one local answer do not qualify the hosted model. Publication remains prohibited by the owner's explicit hold.

Review the two composition histories independently. The main documentation PR grants no merge or release authority. Human acceptance, source/rights/sensitivity review, package activation and comprehensive hosted equivalence remain separate. The frozen October 7 NWM capture remains unapproved historical data, not live.

## Rollback

1. Re-pin the affected checkout/service and preserve any newer changes before reversal. Never reset another task's branch.
2. Local: use backup branch `codex/pre-reconciliation-20261018` at5b6 and paired private source/build snapshot; restore prepared assets and retain old immutable assets. Restart only the existing Explorer service. **Do not roll stores back** or replace the preserved model/native capsule.
3. GoDaddy: select the prior branch or pinned parent only for an authorized **private preview** update; the parent archive supports reconstruction but is not a byte attestation of the previous Folder-upload runtime. Do not click Publish to Live or restart Published.
4. Main observation: revert the additive report/receipt/link change only. Historical receipts, selected mirror, data assets and release decisions remain intact.

## Project records

The [Notion alignment register](https://app.notion.com/p/3c5a92021bf681b5982ee75dc4376b4e) and [Google Drive System Chronicle](https://docs.google.com/document/d/1fBOUDqrcsHaPJiEfM5HmtJL7fBMKFr-rgoN2ge_uVrI) were updated with a dated current checkpoint while historical text was retained. They are coordination/provenance records, not runtime or release authority. The complete private proof package includes per-file manifests, test logs, source/asset screenshots and installation instructions.
