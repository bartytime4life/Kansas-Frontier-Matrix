# Terrain lifecycle audit · 2026-11-25

The audit starts from production merge `2dc0b7faed791feefe3858aad0d9cc640ec174cc`, application-input digest `sha256:98fd4e5ca70c348165d6da84cf1dcfbc87f6e901c78bc50cfe54ddcc0a3ad6d6`. The existing app is `urdng3v1vk`; source edits are additive in the standalone GoDaddy composition. The owner monorepo, original map tabs, data, secrets, hosting binding and DNS are preserved.

## Reproduced defects and corrections

Five focused behavioral failures were reproduced against unchanged production code:

- Look down, tilt and finer-detail camera actions still animated in Lightweight mode. All terrain camera shortcuts now apply the same Lightweight/reduced-motion policy while retaining their destinations.
- Disabling raw points left an orphaned point selection and source-record draft. Removal now clears only that point source reading; an independent cell selection survives.
- Moving outside Kansas retained the previous raw-point buffers and reading. Those are retired with the out-of-area source, with no new acquisition.
- In-flight preparation was not terminated at movement start. It now stops immediately; late completions and queued timers cannot install or start CPU work while moving. Existing completed geometry remains available. Identical completed source/settings are reused after a pan, including their resource budget.
- Resize invoked the move-end handler, falsely declaring a moving view settled. Resize now requests a new plan only when the camera is actually stationary. An explicit move-end revision covers fast interrupted movement.

During movement, source acquisition holds its queued work while allowing at most the existing two requests to finish into the bounded cache. The settled view resumes the latest plan, reusing overlaps and aborting obsolete requests. Hidden/disabled/unmounted views still abort active work. Existing cache, vertex and framebuffer limits are unchanged.

Additional regression cases cover returning to completed settings after canceling an intermediate job, a resource-budget change requiring fresh preparation, and a queued timer firing before React commits movement state. These exercise production hooks and the actual tile store; they do not establish browser frame rates or source accuracy.

## Opportunities to prioritize next

1. A drawn transect across multiple tiles, with distance, source boundaries and NoData gaps, would make comparison more useful than a single source row. It requires explicit datum/resolution handling; no cross-survey interpolation should be implied.
2. A coverage/readiness overlay would let visitors distinguish continuous resampled ground, available native Surface/Canopy, pending work and missing support before selecting a layer.
3. A side-by-side base landscape/cell comparison with synchronized camera and a shared source readout would make the data easier to understand while retaining fine visual context. It must share acquisition/cache work and remain optional on constrained devices.

These are prioritized opportunities, not implemented features. Exact-head CI, public source identity and rendered-browser checks are separate release evidence.
