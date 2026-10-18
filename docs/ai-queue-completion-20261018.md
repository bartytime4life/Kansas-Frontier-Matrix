# AI queue and continuation repair — 2026-10-18

Authoring base: hosted Node branch `a0-hosted-ai-web-20261017`,
`bc85f8df875fae64d0eaca46d25a9e14d0201d39`. Publication stays on the
owner's explicit hold. Preview verification and publication are separate.

The existing two-read/eight-waiter source buffer and its cancellation,
withdrawal and quota tests pass. A separate inference-queue regression reproduced
the deadline problem: waiting discussions consumed their 270-second answer
budget before generation started. Three admitted jobs now have at most 810
seconds total lifetime; preparation and each actual run still have at most 270 seconds, under
the unchanged 255-second model watchdog. Evidence's 90-second deadline, hourly
limits, one job per guest, three active/waiting jobs, one worker, 512-token
input bound and 2 GiB sampled RSS guard are preserved. Accepted responses expose
the server's deadline. The interface distinguishes waiting, preparing and running
without automatically resubmitting a question.

Continuation reuses the original question and escaped unfinished assistant
prefix, rather than asking the small model to begin another answer. This
reconciles the preserved, unmerged `ac575d929ad9cb34d8d70588942b328af3bae66e`
candidate with current `#5248` prompt framing and `#5250` source-read admission.
That historical candidate remains intact. Earlier turns may be dropped with
disclosure; the original question and unfinished prefix are never silently
shortened. Oversized input is withheld. Only this guest's latest limited reply
in the same source context can be resumed.

Each suffix and the combined answer pass existing precision, URL, repetition
and UTF-8 byte checks before history changes. Multiple suffixes retain one
original question with a cumulative reply capped at 4,096 bytes. Copied text,
changed context, cross-fragment unsafe output and oversized continuations are
withheld without poisoning history. Inference records the actual stop reason;
re-tokenizing decoded output can no longer mislabel a token-limited reply as
complete. The UI explicitly labels resource-limited replies incomplete.

Placement uses the existing standalone Node application's `server/`, `app/`,
`tests/` and `docs/` responsibilities, retaining Directory Rules/ADR-0029
separation from the monorepo's governed release and receipt roots.

Initial regressions failed before repair. Changed-area queue, read-buffer,
privacy and continuation tests pass locally; build, TypeScript and lint results
are recorded on the repair PR. Real hosted-preview outcomes must be recorded
against its displayed commit, separately from synthetic tests and local builds.
The tiny hosted model still has finite capacity: these changes do not guarantee
semantic completeness, factual accuracy or qualification of released evidence.
The larger local Qwen is a separate runtime.

No provider capture, accounts, credentials, storage, data admission, geometry,
native values, runtime model identity or dependency lock changes are introduced.
Rollback reverts this change as a unit and returns Preview to its prior exact
source without migrating stores. Published remains unchanged.
