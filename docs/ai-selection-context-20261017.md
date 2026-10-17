# AI questions about selected evidence and Underground samples

Status: locally validated authoring for review. No deployment, source admission,
factual-model qualification, or release decision is conferred.

## Behavior

Public hosted chat uses the existing anonymous guest endpoint. The chat toolbar
says **No login needed**; the main **Administrator** control opens the existing
authenticated account tools. Opening `/?kfm-chat=1` opens chat directly.

Select a map record in the Evidence Drawer and choose **Ask AI about this
record**. The chat shows the selected title, source/time boundary and active map
year. Each submitted question carries the current selection. Each returned turn
shows the server-recognized context so an older reply is not confused with a
new selection.

In Underground, select a record or interval, then choose **Ask AI about this
sample/interval** in its inspector. The individual-log control also offers
**Ask AI about selected sample**. Quick prompts help explain the record,
interval and missing support. Draft questions survive context changes.

Catalog selections send identifiers that resolve on the server. Underground
selections send tile, record and optional interval identifiers; the server reads
only the shipped public manifest/allowlisted tile, checks compressed and decoded
SHA-256, resolves the exact record/interval, and sends a bounded projection to
the hosted model. Coordinates, names, source URLs and unrelated intervals are
not included in that KGS projection. Record date and archive edition stay
separate. A core inventory range does not establish recovery or continuous rock.

External provider selections use a bounded **unverified browser display
snapshot**. That snapshot cannot authenticate a source or become released
evidence. A missing, changed, incompatible, malformed or protected context is
withheld. Private location-derived selections remain in the browser. Context
and source revision bind guest follow-up history; changing sample, interval,
time or resolved source content starts fresh model context.

All model responses remain unverified interpretations. Evidence mode continues
to use the existing governed released-record reader and rechecks release state.
The Node composition's released-knowledge binding and the small model's factual
answer qualification remain open. This change does not replace them.

## Source and placement basis

The target is the separate GoDaddy composition on
`a0-hosted-ai-web-20261017@4b3cc837e9c131e5eb214427e0a55646fc76e52a`,
not monorepo main's older local-Qwen Worker mirror. All 1,077 tracked hosted
blobs were compared successfully with the remote Git tree before authoring.
The local content-identical snapshot commit is
`58d37eb8fa6de58cdf1fbbfd13a01d7a08827939`; the PR parent is the actual
remote hosted commit.

Directory Rules §§10–12 and accepted ADR-0029 preserve the established
composition's `app/`, `server/`, `tests/` and explanatory `docs/` lanes.
No parallel policy, schema, source, release or proof authority is created.
The original Sites source and the separately restricted Public Staging Site
are outside this source change. No account store, model weights, audience or
storage bindings are changed.

## Validation and limits

Production build and TypeScript pass. The changed-area tests exercise anonymous
chat, exact sample/interval binding, missing/tampered/traversal assets, source
revision changes, pending expiry, current outgoing UI context, retained drafts,
job ownership, independent account controls and existing Underground behavior.
The existing slice regression exposed a missing-tiles test-fixture edge; the
inspection callback now safely withholds an unresolved tile.

A local HTTP/browser acceptance attempt was blocked by
`listen EPERM 0.0.0.0:5186`. No hosted source-equivalence or new rendered
acceptance is claimed. No real inference or private store was used in these
tests. Model quality and long-session/device/accessibility checks remain open.

The Codex Security diff review covers its recorded authoring snapshot; the
later source-revision binding and optional-tile guard receive supplemental
review and regression coverage. It is a bounded changed-area review, not a
whole-repository audit or publication approval.

## Rollback

Revert this bounded PR or restore the previously accepted hosted source
`4b3cc837e9c131e5eb214427e0a55646fc76e52a`. No migration or private-data
rollback is required. Retain account/job store configuration and model files.
