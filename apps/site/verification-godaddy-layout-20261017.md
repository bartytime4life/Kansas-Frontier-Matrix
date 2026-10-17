# Explorer GoDaddy layout port verification

**Scope:** local presentation and control changes; no deployment or data migration.

## Source and repository baseline

The GoDaddy activation record in [PR #5215](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5215) identifies app `q9r9beo47t`, selected branch `a0-hosted-ai-web-20261017`, and published commit `4b3cc837e9c131e5eb214427e0a55646fc76e52a`. A separate exact-source checkout and the live `page-C7Fh0jbw.js` bundle corroborated the observed layout and controls. The bundle SHA-256 was `647ba551de64ed4331ef6724ccf7ffc1daebcaf0329b44465aecb2b97ae53bb9`. This is source attribution, not a reproducible bundle-to-commit proof.

This follow-up starts at main `2b22ed1115ebfdac98d497b1db95129453b4a2a1`, which includes merged #5218 and #5219. Its Site source is byte-identical to the pre-port baseline `9e0e9270ef284076800f50b77081c5abedf40de2`. The 19 verified UI/test files were copied into an isolated branch without changing the original working tree. Merged #5219 changes only `tools/qa/site_mirror.py`; this port does not overlap that file or the receipt binding.

## Result

- Effects and rendering controls are accessible from the header, with the existing real renderer callbacks and saved settings.
- Map reports the active representation; selecting 2D, Terrain or Globe closes incompatible Underground/Compare views. Native menu dismissal retains keyboard and pointer behavior.
- Explore exposes navigation, coordinates and camera controls while retaining Local Atlas, Appearance, Measure and advanced tools.
- Source Status is the fourth Layers tab, with selected/all scope, source recovery and embedded private date-specific downloads.
- Chat with KFM and Evidence labels are consistent while Qwen remains local-only, with no hosted fallback.

Archive authorization, APIs, runtime/configuration, dependencies, audience, D1/R2 bindings and data-source files remain unchanged. Four unrelated document edits in the original checkout were preserved byte-for-byte and excluded from the commit.

## Validation

| Check | Result and scope |
|---|---|
| Targeted Node tests | PASS: 85 tests, including menu dismissal, rendering controls, workspace navigation, downloads, archive authorization and local Qwen contracts. |
| TypeScript | PASS: `tsc --noEmit -p .`, repeated on the follow-up branch. |
| Lint | PASS: whole Site ESLint invocation, zero errors or warnings, on the follow-up branch. |
| Production build | PASS on identical application bytes, including subsurface public-asset containment. |
| Desktop visual comparison | PASS at 1280 × 720 CSS/pixels, standard basemap, 2D, 2026, five layers. Full-view and focused Effects/source-drawer comparisons inspected together. |
| Phone visual comparison | PASS at 390 × 844 CSS/pixels, scale 1. Header, Effects, scrollable source sheet and Map menu remain usable without horizontal overflow. |
| Live preview checks | 105 county records and 181 River Pulse stations loaded. Flow toggle, Terrain/2D, Explore, source scope, downloads disclosure, Evidence/chat switching and two-step phone Escape worked. |
| Browser console | No warnings or errors returned by the tab developer log query. |
| Preservation | 14,793 baseline tracked-file hashes checked; only the intended existing UI/test files changed. Original unrelated changes retained. |
| Hosted CI | Check the draft PR's exact current head; this record does not pre-claim its result. |

Intentional differences from the public site: owner-private workflows and local Qwen remain; the public account/hosted AI flow is not imported. The four Layers tabs share one row. Local mobile Effects uses an opaque surface for readable controls. Below 1100 CSS px, the existing Evidence sheet is used; wider screens retain the full-height right drawer.

Actual local Qwen inference was NOT RUN: the companion was unreachable and the UI reported that limitation. Private released snapshots were not available in the disposable local database. No hosted archive writes, production D1/R2 reads or mutations, location permission request, model installation or deployment was performed.

## Draft PR CI follow-up

PR #5220 was merged externally while CI was being checked. The assertion-only follow-up starts from current main `2786e399a3bd66af01d4239f1db291c2d0e0d283`; its application tree matches the verified port. The original checkout and unrelated document edits remain untouched.

[PR #5220's initial Explorer run](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/39005174265/job/117316050561) passed lint, TypeScript and the production build, then reported 1,370 passing tests and three failures. Two source assertions still required the old inline Globe callback and a header without its new dismissal ref. Those assertions now verify the shared representation selector (including closing Underground/Compare) and the single header regardless of attribute order. Both corrected assertions pass locally. The verified application bytes remain unchanged.

The remaining local-runtime test failed with `STARTUP_FAILED` in the [preceding main run](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/39002317013/job/117307652690) at `012536c15a394a4db5b24584e151a331c94a6764` too: 1,363 passed, one failed. That revision and this PR's main base have byte-identical Site source. Runtime code/configuration and its authorization checks are outside this layout fix and remain intact. The backend smoke step was skipped after the test failure; no smoke pass is claimed.

The separate `water-conformance` check fails with `MIRROR_REVIEW_REQUIRED` on [the initial PR](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/39005174223/job/117316050401) and its [exact main base](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/39004937915/job/117315364743). Both passed 338 Python tests before that gate. This port does not change the mirror review receipt or weaken the gate. The follow-up PR's current checks and description record the final rerun; this dated record identifies the initial failures and their attribution.

## Retained visual evidence

The task retains the following browser captures outside the source/deployment tree. Hashes bind the inspected files; these captures are local evidence, not publicly hosted assets. Full QA, interaction notes and logs remain with the task.

| Capture | SHA-256 |
|---|---|
| `public-desktop-map.jpg` | `ae163a2730673eb3cb5898309ee55d36d2502dd7bd8234cf5398d2246b79758f` |
| `local-desktop-map.jpg` | `da60ada4ddba81f12784a88120a47630eb788cdff997f879ed084afdc8420ae5` |
| `public-desktop-effects.jpg` | `4fe2faceaea29141bce5024834ccde68baf8a5a6f45f15971fa7fb154cb1fbc6` |
| `local-desktop-effects-matched.jpg` | `11c08cf40e0e8b93a9a0e5c4ee2480ea13c55a54acce7b405660acf06e3d90b1` |
| `public-mobile-effects.png` | `a1f34bbad8a4fd3bd75bfb5b7ab0a01f1776a65ba6ee3e8df3e1be9bb557c29e` |
| `local-mobile-effects-matched.png` | `b9de2b882250ee0c579a5d2f72553399b39ecffce0e3857c1681b855e1e75f7f` |

## Placement and rollback

UI and adjacent tests remain under the existing `apps/site/source` composition. This dated record follows the existing `apps/site/verification-*.md` lane. The generated receipt uses `data/receipts/generated`, with human review pending. Directory Rules v2 and accepted ADR-0029 preserve these responsibility boundaries; no authority root or data lifecycle is changed.

Revert the follow-up commit or apply a focused forward fix. No database migration, storage rollback or hosted-site action is needed. Historical v252 deployment evidence and existing mirror receipts remain unchanged.
