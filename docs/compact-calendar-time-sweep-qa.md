# Time sweep design acceptance

final result: blocked

## Findings

- Browser-rendered acceptance is blocked. Chrome returned `net::ERR_BLOCKED_BY_CLIENT` for `http://localhost:4173/`; the supported `http://terminal.local:4173/` preview returned `net::ERR_NAME_NOT_RESOLVED`. No implementation screenshot was captured. This is an unavailable comparison, not a visual pass or an observed layout defect.
- A subsequent local dev launch found port 4173 occupied. The existing process was preserved. Production build results do not establish that this candidate was rendered there.

## Comparison evidence

Source visual truth: owner-approved compact transport mock `generated_images/exec-32223dc7-662f-44f9-b975-41817f911b2e.png`, followed by the owner's explicit hover-to-open/animated-emblem clarification. The mock predates that clarification and is not an exact collapsed-state target. Decorative atlas: `generated_images/exec-82168963-b53d-4767-8ce4-1fee0de009ab.png`, 948 × 1659 pixels, four 237-pixel cells across seven era rows. The delivered WebP retains those dimensions; CSS targets a 56 × 56 pixel emblem.

Implementation screenshot path: unavailable. CSS viewport and device scale factor: unverified. Intended acceptance viewports: desktop 1440 × 900 and phones 390 × 844 and 320 × 720. Source/implementation density normalization: not performed; no matched pair exists.

States to capture: idle emblem, all seven era poses, hover reveal, leave-delay collapse, keyboard focus and Escape, touch-pinned menu, source loading/empty/error, range and A/B comparison, reduced motion. Full-view comparison: blocked. Focused comparison: blocked; emblem crop/sharpness and menu typography/overflow require focused captures.

## Required fidelity surfaces

| Surface | Result | Remaining evidence |
| --- | --- | --- |
| Fonts and typography | Unverified | Rendered family, size, wrapping, focus and native date/select controls |
| Spacing and layout rhythm | Unverified | Map grid alignment, panel bounds, hover gap and phone overflow |
| Colors and tokens | Unverified | Rendered contrast, loading/empty/error states and focus visibility |
| Image quality | Unverified in implementation | Sprite crop, transparency, high-density sharpness and transitions |
| Copy and content | Code reviewed; rendered acceptance unverified | Date labels, source limits and announcements at actual widths |

## Comparison history

No successful rendered-comparison iteration. Code, type, lint, build and regression checks are separate engineering evidence and cannot count as design-QA iterations. No visual mismatch has been classified as fixed or acceptable without a post-fix capture.

## Implementation checklist

1. Restore an allowed Chrome preview route to this exact candidate.
2. Capture matched full-view and focused states at the target viewports.
3. Exercise hover, focus, touch, close, date/range, playback and A/B; check browser console and network failures.
4. Check all five fidelity surfaces, fix actionable issues and recapture.
5. Record actual screenshots and comparison evidence before changing the result to passed.

Hover, animation smoothness, mobile acceptance and live-provider end-to-end behavior remain unverified. This candidate must remain a draft; no merge, release or deployment is included.


## Executed validation (2026-10-21)

- `npx tsc --noEmit --incremental false`: passed.
- Changed TypeScript lint: zero errors; 41 pre-existing warnings in app/page.tsx, matching the base. The three new TypeScript files have zero warnings.
- `npm run build`: passed, including postbuild client-asset staging.
- `node --test --test-concurrency=4 tests/*.test.mjs`, after the completed build: 1,619 total, 1,602 passed, 17 skipped, zero failed/cancelled. Skips are not claimed as passing checks.
- Focused date/lifecycle tests: 20 passed, zero failed.
- `git diff --check`: passed.

An earlier full-suite attempt ran concurrently with the build and the existing build-identity HTTP test found dist unavailable while it was being rebuilt. The complete post-build rerun above passed. Two earlier production-loader harness failures were corrected by providing the newly introduced shared-request ref and asserting that duplicate dates share the same completion promise. No production assertion was removed.

The QA result remains blocked. These executed checks do not verify rendered hover, animation, touch, phone layouts, browser console or live-provider end-to-end behavior.
