# Evidence integrity and asynchronous review recovery

This bounded change starts from main
`df48fcfbcc8b3000c84c479bf410a40fd400e54b`, the independently merged PR #5790.
It corrects retained-file reads, streamed body limits and private review workflows.
It creates no source, data-admission or publication authority.

## Reproduced problems and resulting behaviour

| Surface | Reproduced problem | Correction |
|---|---|---|
| Submission download | A changed R2 object, including same-length corruption, was returned without checking its recorded hash | Authenticate and authorize first, validate recorded metadata, bound the read to the recorded size and ten seconds, then verify actual size and SHA-256 before returning any attachment bytes |
| Steward review | A delayed acknowledgement for A reopened A after the reviewer had opened B | Capture the reviewed identity, version, decision and note; retain a separate acknowledgement; preserve newer selections and drafts; refresh without downgrading an acknowledged version |
| Land evidence | A failed evidence request left a loading message with no recovery | Keep loading, failure, verified-empty and ready states tied to the bundle and record; apply a fifteen-second whole-read deadline, cancellation and retry; ignore stale completions |
| Soil imagery and lightning | Soil readers retained locks or waited indefinitely for cancellation; transport handling was duplicated | Share bounded binary collection, release reader locks, cancel rejected bodies without awaiting an uncooperative source, and preserve each transport's deadline, MIME and PNG validation |
| Governed administrative requests | The entire request body was read before applying its size limit | Enforce the byte limit during collection before the existing fatal UTF-8 decode; retain all origin, owner and release-family checks |
| Soil export | A selected station's extra row at an unbound depth passed the evidence guard | Require every selected row to use one of the five numeric depths already bound to that station's evidence |

A successful review acknowledgement records only the status and version returned
by the write plus the captured submitted note and identity. It invents no persisted
review ID or timestamp. A failed history refresh retains that acknowledgement and
shows a separate warning. Failed writes preserve the draft and create no success
receipt. Evidence retry retains focus ownership without stealing focus from a
reviewer who moved elsewhere.

Original objects, submission metadata and review history remain immutable on read.
Downloads still use private, no-store and sandbox headers and the existing safe
filename handling. Interruptions return a retryable error; size or digest mismatch
returns an integrity error. The ten-second deadline covers streamed original bytes,
not the preceding object lookup. NASA's twelve-second and lightning's fifteen-second
transport deadlines include body collection. Existing image routes do not acquire
new browser-disconnect propagation.

## Validation

- Production build and containment checks pass. TypeScript passes. Lint reports
  zero errors and the same 77 inherited warnings. All 1,568 Site tests pass,
  including original-byte corruption cases in a disposable Miniflare worker.
- All 370 tests in the water-conformance selection pass, including 69 mirror
  regressions. The strict inventory covers 920 files with no unexpected changes;
  the predecessor hash, dependency inputs and all 262 withheld paths are preserved.
- Disposable backend smoke passes 110 checks across 79 routes. Fourteen provider-only
  routes remain listed and unexercised by this offline check.
- Eight review lifecycle and nine land evidence component tests cover late writes,
  A-to-B-to-A navigation, newer drafts, stale and failed refreshes, failed writes,
  finite header/body deadlines, restart, focus ownership and unmount cleanup.
  Independent code review found two additional races; both were corrected and
  covered before the complete checks above.
- The final-source browser rehearsal confirms a delayed A acknowledgement while
  B and its newer draft remain selected, and an integrity error followed by a
  successful evidence retry. Keyboard focus lands on the result heading after
  retry. Desktop and phone layouts were inspected; at a 390-pixel viewport the
  measured document width is 375 pixels with no page-level horizontal overflow.

The first browser retry exposed a native disabled-control focus loss. The final
pending control remains focusable as “Restart evidence check”; activating it
cancels the previous read. The browser rerun confirms the correction. Restart,
intentional focus changes and uncooperative late adapters have deterministic
component coverage. Full device, screen-reader, zoom, real-provider, long-session
and full monorepo qualification remain outside this pass. Hosted CI and human
review are separate from these local results.

The private component browser rehearsal uses the actual client source with a
loopback, in-memory synthetic API and a prominent fixture label. It performs no
real uploads, review writes, authentication or R2/D1 operations. It can establish
selection, draft, retry and layout behaviour; it cannot establish private account
access, live retained-object integrity or production acceptance. Deterministic
source and disposable-worker tests cover those server changes separately.

## Inventory and rollback

The append-only `site-v268-evidence-review-overlay-20261109.json` successor binds
sixteen Site source/test/note changes to the unchanged previous receipt. Its
authority remains `CONTENT_PARITY_ONLY` and its status remains `REVIEW_ONLY`.
Source and overlay review stay pending; human acceptance and hosted equivalence
remain false. Historical Site identity remains an inherited declaration. All 262
withheld carriers remain absent.

The original owner checkout is preserved. No dependency, persisted store, schema,
access, data-admission, release, deployment or hosted publication setting changes.
Undo with a focused inverse commit or reviewed forward correction. Revert the
successor and selector together while retaining all predecessors and withheld paths.
