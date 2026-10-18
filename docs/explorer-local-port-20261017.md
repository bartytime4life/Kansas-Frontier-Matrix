# Explorer local-port reconciliation

## Source and delivery boundary

The verified local candidate compared Public Staging version 6 source
`3149017bf3711c219f947a8e874d37c9d8a49987` with saved private Explorer version
252 source `190d16acb2f866cb9c2eb108dbd204ca30465269`, retaining local private
workflows on repository base `46d0f0ca73843bc6e9490595ec19a10693b0f1b5`.

Before delivery, PR [#5088](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5088)
was found merged at `2026-10-17T04:06:43Z`. The owner authorized a follow-up
**draft** from current main. This reconciliation starts at its merge commit
`2578192eccc3de36c0f92aee0e1f1e6d66ca93bd`, preserving PR head
`acb2266bc8fe9ae05ff1d6eb51caae929d22a6b3` and all other merged work.

## Remaining changes

Main already contains the subject navigation, map starters, Appearance/Measure
controls, River Pulse restoration and zoom-dependent flow rendering, and Qwen
question-gating, ranking and diagnostic improvements. Thirty-three of the 42
selected local files already match main byte-for-byte. Eight differ, and the
local port record is new. Comparing those differences leaves only:

- The mobile Data sheet releases its header's backdrop-filter containing block,
  so its fixed positioning anchors to the viewport.
- The topic-index regression verifies every rendered internal link has a page.
  Existing almanac resources and private land-record links remain covered.
- This reconciliation record and a dated attribution note in [water flow](water-flow.md).

Newer main content remains intact, including reviewed earthquakes, almanacs,
land records, API connections, Frame Check, Local Atlas private-view redaction,
and subsurface static-delivery validation. The original local working copy and
its unrelated archive edits remain untouched. Identity, access control, Worker
configuration, credentials, dependencies, migrations and data assets are unchanged.
No Site save, deployment, live capture or production D1/R2 operation occurs.

## Verification boundaries

The earlier local candidate passed TypeScript, production build, 1,230 Node
tests (three platform/operator skips), and desktop/mobile navigation checks on
2026-10-17 UTC. Those observations belong to that candidate, not this newer main.
The current reconciliation passed TypeScript, production build including the
subsurface containment checks, and eight focused mobile/topic tests. Additional
current-head results and inherited CI findings are recorded in the follow-up PR
and its generated-work receipt. Real providers and a real Qwen model were not
invoked for this source-only delivery.

Version 252's earlier deployment and approved capture evidence remain in
[the historical archive receipt](../../../../data/receipts/generated/archive-authorization-v252-20261011.json)
and PR #5088. They document the original owner-private deployment and preservation
of its previous archive records; they do not establish deployment of this follow-up,
current hosted equivalence, or closure of the security finding.

## Placement and rollback

Application changes remain in `apps/site/source`; generated-work provenance stays
in `data/receipts/generated`, following CONTRIBUTING and accepted ADR-0029.
Human review remains pending. Revert only the follow-up commit if needed, keeping
all newer or unrelated changes. No data rollback or migration is required.
