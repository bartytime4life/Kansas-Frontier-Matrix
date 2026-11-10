# Reading context and keyboard ownership

This bounded pass starts at PR #5794 head
`e99759bb6cc6936d1ebe0f2b00d6b14892479e14` and retains the standalone Site,
source identities, lifecycle gates and publication holds.

## Confirmed corrections

| Surface | Reproduction | Result |
|---|---|---|
| Status dialog | Slash focuses global search behind the open modal; Escape then leaves the dialog open | The dialog isolates its background and owns keyboard focus; global shortcuts defer until it closes |
| Competing compact panels | Desktop chat plus Status followed by compact resize can isolate both panels | Modal isolation effects use a shared layout phase and explicit input priority, restoring the previous eligible owner on close |
| Bridge and PLSS record inspectors | Deliberately abort-ignoring transport fixtures remain pending after their timer only aborts a signal | Whole fetch/body reads settle by the existing fifteen-second deadline independently of transport cooperation; cancellation cleans up and permits retry |
| River Pulse selected reading | Earlier 100 ft³/s is displayed as 100 m³/s using the latest row's unit | The selected value retains its own frame unit |
| River Pulse comparisons | Mixed measurement units produce a false shared range and chart | Compare only qualified matching station, parameter, statistic and unit bases; otherwise disclose the withheld comparison and retain raw sample inspection |

The transport non-cooperation fixture is synthetic; it does not establish an
observed native-browser indefinite fetch stall. Native ReadableStream cases
separately exercise cancellation, bounded bodies, reader release and cleanup.
Prior record results retain their original search location and limitations.

No measurement conversion, provider response rewriting, fabricated observations
or release action is introduced. Zero remains a reading; null remains missing.
Raw samples and source timestamps remain available.

## Browser evidence and validation

Before capture uses the verified base application build. Actual Status-dialog
keyboard reproduction confirms the focus escape and open dialog after Escape.
A GET-only local proxy supplies an explicitly labelled synthetic River bundle
from the actual adapter fixture: 100 ft³/s and 5 m³/s at two exact times. At the
earlier frame, the water card incorrectly shows 100 m³/s while its raw sample
shows 100 ft³/s, and the range incorrectly combines both values in m³/s.
Screenshots are saved, opened and inspected outside Git.

Final Site build/containment, TypeScript and **1,727 Site tests pass**. Lint has
**zero errors and 77 inherited warnings**. Disposable backend smoke passes
**110 checks across 79 routes**; fourteen provider-only routes are unexercised.
The bounded water-conformance suite passes **374 checks**, including **73 mirror
regressions**. Strict inventory contains **933 files**, with all **262 withheld
carriers absent**. Independent reviews cover all three implementation slices.

Final built-app browser steps and results:

1. **Status keyboard — passes.** Slash, R and L retain focus inside the dialog;
   the background search is inert while Status owns input.
2. **Responsive ownership — passes.** Open desktop chat, open Status, resize to
   720 pixels, and use Tab/Shift-Tab. Status remains focusable; Escape resumes
   retained chat. Closing chat and resetting width restores the ordinary map
   slash shortcut. The local model bridge is unavailable; this checks panel
   ownership, not a model answer or model acceptance.
3. **River units and comparison — passes within the labelled synthetic fixture.**
   The latest row retains 5 m³/s; the earlier card and raw inspector both retain
   100 ft³/s. Mixed-basis charts/ranges are visibly withheld, with raw sample
   navigation available. No conversion or provider observation is implied.

Accepted screenshots stay outside Git. The local proxy blocks application writes;
temporary tabs/servers are closed and the viewport override is reset. No full
WCAG/device, provider, private authentication or production qualification is
claimed. Submitted-head CI remains separate in GitHub.

## Inventory and rollback

The new `site-v268-reading-context-integrity-overlay-20261109.json` receipt
binds exactly thirteen changed Site paths and four additions in this pass. All predecessor receipts, source identity,
review/overlay declarations and withheld carriers remain unchanged. Authority is
CONTENT_PARITY_ONLY, status REVIEW_ONLY, source/overlay review pending; human
acceptance and hosted equivalence remain false.

Revert the successor and selector together or use a reviewed forward correction;
preserve all historical receipts and withheld paths. The owner checkout remains
untouched. No dependencies, schemas, access, operational data, source activation,
admission, release, merge, deployment or publication change.
