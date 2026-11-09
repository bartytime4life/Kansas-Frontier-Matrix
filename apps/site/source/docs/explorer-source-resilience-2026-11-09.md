# Explorer source resilience and keyboard measurement

This bounded correction starts from PR #5789 head
`35b54959327fddc284457ea38bedf99304f600f1`. That tree was independently merged as
`05154c0b5d3fa1b94cc971d1a0f0a9848f7731ab`; a repository-wide comparison found no
byte differences between those two trees. This follow-up changes source handling
and the existing measurement flow. It does not add or activate a data source.

## Confirmed defects and corrections

| Surface | Reproduced problem | Bounded correction |
|---|---|---|
| NWS alert context | A successful zone response with unusable geometry could establish empty coverage; advertised next pages were ignored | Validate selected zone geometry and disclose lookup failures, unresolved coverage and pagination without unbounded follow-up requests |
| Archived river context | Invalid or future time strings could become observations; lexical comparison could select the older instant; provider limits were only requested | Normalize timestamps without losing fractional precision, preserve the original clock, enforce the rolling window and first-1,000-record bound, and disclose withheld/omitted readings |
| Lightning image transport | The 1 MiB budget was checked after the entire response had been buffered | Enforce the actual-byte budget while streaming, retain a finite deadline and cancel rejected work without waiting on an uncooperative cancellation adapter |
| Soil tile selector | Prototype property names passed the server view test and caused provider work before failing | Accept only own registered view keys and reject other names before provider work |
| Observatory distance and bearing | A keyboard user could activate measurement but could not place either endpoint | Share endpoint selection between pointer clicks and explicit map-center controls, with coordinate and focus feedback |

Provider time, retrieval time and capture time retain their existing roles. These
are external provider responses and approximate display tools; the corrections
do not establish evidence admission, scientific accuracy, survey accuracy or
source completeness beyond the returned, explicitly bounded response.

## Validation

The initial built-worker run exposed a cold-start fixture defect: the framework
installs its fetch wrapper on the first request and could replace a previously
installed fixture transport. The four adjacent context suites now deny real
transport before worker import, prime a local unsupported-feed request, and
verify fixture calls. Existing empty, error, cap and provenance assertions remain.
This closes accidental provider access and vacuous first-case success; it does
not weaken a source or application gate.

- Production build and containment checks pass. TypeScript passes. Lint has zero
  errors and 77 inherited warnings. All 1,530 Site tests pass, including 33
  built-worker context fixtures with denied unowned transport.
- All 369 tests in the water-conformance selection pass, including 68 mirror
  regressions. Strict current inventory covers 916 files; all 262 withheld paths
  remain absent. Historical receipt SHA pins and dependency inputs are preserved.
- Disposable local backend smoke passes 110 checks across 79 routes. Fourteen
  provider-only routes are listed and remain outside that offline smoke check.
- Actual local Tab/Enter/arrow navigation places both measurement endpoints;
  the checked example reads 44.86 miles / 72.19 km. Done/Edit/Clear/Escape focus
  behavior and third-point restart pass. Desktop and phone screenshots were
  saved and inspected; phone document width is 390 pixels without page-level
  horizontal overflow. Existing toolbar strips scroll internally.
- Focus guards, unavailable-map and reduced-motion cases use synthetic map/DOM
  fixtures. The browser exercised the unchanged final Observatory source; later
  server-only precision/cap changes use deterministic built-worker evidence.

Full device, assistive-technology, 200-percent zoom, long-session, real-provider
qualification and the full monorepo suite remain outside this bounded pass.
Hosted CI for the submitted commit and human review remain separate evidence.

## Inventory, preservation and rollback

The append-only `site-v268-source-resilience-overlay-20261109.json` successor binds
the twelve Site source/test/note changes to the immutable previous receipt. Its
authority remains `CONTENT_PARITY_ONLY` and its status remains `REVIEW_ONLY`.
Source and overlay review stay pending; human acceptance and hosted equivalence
remain false. Historical Site identity is inherited declaration, not fresh hosted
readback. All 262 withheld carriers remain withheld. A byte match does not admit
data, approve overlays or authorize publication.

The original owner checkout remains untouched. No persistent store, access,
dependency input, source admission, capture schedule, deployment or hosted
publication is changed. Use a focused inverse commit or equivalent forward
correction to undo the changes. Revert successor and selector together while
preserving predecessor receipts and withheld paths.
