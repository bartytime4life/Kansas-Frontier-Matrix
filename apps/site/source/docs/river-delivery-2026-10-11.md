# River Pulse delivery and date validation — 2026-10-11

## Source and scope

Baseline browser test: same standalone Site v239, source `9b647f78b05c77cc497ec74407c5611aa47b0f5f`. Final edits are reconciled onto v241 source `04a6d0cdfac36eef4d03e99c59701108162fb342`, preserving concurrent focus/workspace-navigation changes. Project remains `appgprj_6aa0b1c41bc08191bfd86003920f1631`; owner-private access revision 1, existing DB/BUCKET, schedules, API-key handling, upstream allowlists and data-governance boundaries are retained.

The current 24-hour network request opts into `encoding=columns-v1`. It transports all ten existing observation fields through fixed dictionaries and index rows, then restores the original complete bundle before the canonical parser and frame builder. No observations are sampled out, values rounded, source timestamps replaced, qualifiers dropped or uncertainty promoted. Station/archive/observatory callers retain the default legacy response. Both cache variants derive from one capture, without another provider fan-out. Unknown future observation fields fall back to the full legacy packet instead of silently disappearing. Decoder dimensions are limited to the existing 100,000-observation bound; indices are checked before reconstruction and every restored value still undergoes canonical validation.

## Reproducible measurements

Native Chrome 154, Linux, same workstation and preserved unrelated user tabs. Production preview, default five selected map layers, 1258×1323 CSS viewport. Local QA proxy adds 3,000 ms after upstream headers, then streams display/streamflow API responses at 16,384 bytes/sec in 4 KiB chunks. External tiles, scripts and other APIs are unchanged. This is API response throttling, not a full-browser cellular profile. Server caches were warm for transfer measurements; upstream acquisition latency is not claimed as improved. Both browser runs use actual provider responses, not a fixture replay.

| Measurement | Baseline | Compact response |
|---|---:|---:|
| Same captured provider packet, wire bytes | 4,399,021 | 736,491 |
| Actual updated route/cache capture, wire bytes | 4,404,029 | 737,242 |
| Bytes saved on first capture | — | 83.26% |
| Browser under response throttle | 60,012.2 ms timeout | 48,099.2 ms complete |
| Subsequent scheduled compact refresh | — | 48,400.3 ms complete |
| Accepted observations after slow transfer | 0 new readings | 17,249 |
| Time controls after successful compact transfer | unavailable | 96 frames |
| New network read canceled on station-day switch | — | 128.9 ms, 0 delivered bytes |
| Historical station request after switch | — | 5,252.8 ms; 25,644 bytes |

Original and reconstructed JSON SHA-256 match exactly for each real capture. First capture: `a6bdb98f78ec3f4aaf48f1823616cb77ae36c8a048ea630966b26f540f5c7b2a`, 181 stations / 17,229 observations. Actual updated-route capture: `b7efbef117ded9868c180ac12437da83be9f66ea329799d4c19dcb1c1b004957`, 181 stations / 17,249 observations. Capture-time differences explain the small row-count difference between runs; packet equality is checked within each pair. Node single-shot encode/decode on the first real capture measured 21.5/16.6 ms; this is not a browser or Workers capacity certification.

Browser loading sample: five seconds, rAF interval p50/p95 33.4/66.7 ms; zero main-thread long tasks in that window; EventTiming entry p95 88 ms. After load, exact-frame Home/ArrowRight/End and opacity changes passed; sample p50/p95 49.9/66.7 ms, zero main-thread long tasks, EventTiming p95 80 ms. rAF is callback cadence, not GPU/map FPS. EventTiming entries are not deduplicated INP. No rendering-speed improvement is claimed.

## Additional defect found and repaired

A future River Pulse day could pass the prior loader because `Math.min(now, day-end)` clamped the request to the present. The UI could then label an empty filtered result with the future day. Added a valid UTC calendar-day guard (adapter floor 1800, no future day), retained same-day partial-window behavior, disabled invalid checks, and connected `aria-invalid` to visible guidance. Invalid requests return before aborting an active read, changing the archive owner/generation or issuing any fetch. The browser verified a future draft remains invalid while current observations stay displayed. A valid 2024-09-02 station day still loads through the unchanged legacy route. When it supersedes a compact network read, the old request cancels and cannot replace the historical result.

## Validation and limits

The focused transport, route, budget, archive callback and streamflow tests pass. Tests cover zero/null/precision, provisional/approved qualifiers and revisions, empty/partial/truncated captures, exact frame equality, hostile dimensions and indices, duplicate/unsupported encoding, shared-cache timestamps and no extra provider fetch, future-field preservation, impossible/future/pre-adapter days, and unchanged in-flight owner on rejection. Full build/TypeScript/test results for the final reconciled source and deployment/hosted smoke are recorded in the task delivery receipt.

Codex Security assessed the frozen codec patch `6ee25151d79382c6d6641a8e76bd1ed63949015d40df00e34577ffadb34f546e`: advisory merge / human_review_required, with auto-merge excluded for the serialized API contract. Its validated JSON and Markdown are retained in managed artifact storage; the later date guard and reconciliation are identified separately. No full repository security scan, GitHub merge, mirror approval, source admission or owner acceptance is claimed.

Slow transfer still takes about 48 seconds at this deliberately severe rate. Provider fan-out and maximum-size Workers memory/CPU remain unoptimized/unprofiled. Physical-device, screen-reader speech, OS reduced motion and GPU acceptance remain separate from this concrete browser evidence. Raw packets, metric exports, proxy/harness, hashes and reproducible commands are retained outside application source in the task's `.layer-system-work/river-delivery-evidence/`. The QA harness is excluded from deployment assets.
