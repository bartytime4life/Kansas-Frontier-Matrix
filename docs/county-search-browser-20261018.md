# County search browser acceptance — 2026-10-18

## Scope and identity

Hosted application baseline: `a0-hosted-ai-web-20261017` at
`b7392994224f22720fbc5b6fafa99350ce6785ab`, tree
`aad1e1f45653300169e03b39df0f7fb05c9d1350`. This includes merged county-readiness
PR #5264 (`68be2d95f3f8ef47720087cfc5dd106510396b45`) and development/navigation
follow-up #5265. These are repository identities, not deployed identities.

The browser regression runs the complete built, hydrated Explorer against its
existing loopback Node server. It uses installed Chrome over a debugging pipe,
ordinary browser input/keyboard events and DOM observations. It does not
extract JSX, invoke private React callbacks, or use the helper test as a
substitute for interaction. Browser/version identity and mutation observations
are emitted in the CI log. A missing browser or failed scenario fails the job.

## Controlled asynchronous cases

`tests/county-search.browser.mjs` is an explicit integration entrypoint outside
the ordinary `*.test.mjs` glob. The existing `public-core-repair.yml` Node HTTP
step invokes it against the same candidate server, at 1366×768, 390×844 and
375×667. No npm dependency or production configuration is added.

- Hold the actual county request while changing queries; layer and source
  results must remain usable, with loading feedback and accessible status.
- Deliver the county response after rapid edits; only the latest query may
  receive county rows. Observe actual DOM commits during a subsequent debounce
  to detect obsolete results displayed under the replacement query.
- Return a county HTTP 503, partial coverage, or an empty inventory; none can
  claim a complete no-match, and other available matches remain usable.
- Check a completed miss, cleared/whitespace queries and escaped query text.
- Reach a county result with Tab/Enter, open the existing Evidence Drawer,
  retain Census/source-context restrictions and display time, then use Escape
  to return focus. Check result bounds and horizontal overflow at each size.

Fixtures exist only in the test process. Invented county rectangles and the
minimal background style never enter application assets, a source registry,
evidence, releases or production. The test accepts loopback HTTP origins only.
Browser-intercepted API calls other than the county fixture and read-only build
identity return an explicit synthetic 503; external sources are blocked, with
a synthetic background for style requests. Hosted AI, private stores and
administrator operations are not called. This tests UI response handling,
not the correctness or availability of the real Census adapter or a basemap.

Run after a normal production build with a running candidate server:

```sh
KFM_NODE_TEST_ORIGIN=http://127.0.0.1:5182 node --test tests/county-search.browser.mjs
```

`KFM_TEST_CHROME` may select an installed Chrome executable. Each viewport uses
a disposable browser profile that is closed and removed. Never point the test
at a public or private hosted application; it rejects that origin.

## Session evidence and limits

**CONFIRMED:** direct source tests pass (four county cases, eight readiness
cases); browser-entrypoint syntax passes. Local listener creation failed with
`EPERM`; independent test Chrome startup also failed at Crashpad `setsockopt`
with `Operation not permitted`. No local candidate browser pass is claimed.
Exact-head CI is recorded separately in the PR after execution.

The initial CI attempt at `3a65ba5` reached Chrome 155 and the hydrated app,
then exposed harness errors: a wait returned a DOM element through CDP value
serialization, and typing raced the first-visit guide's autofocus. The follow-up
converts wait predicates to booleans, dismisses the normal guide with native
mouse input, and gives the completed-search scenario its own loaded inventory.
Those failures do not establish application regressions. The original
generation receipt is retained; the follow-up receipt binds the revised bytes.
The second run passed actual rapid-query/pending-feed and outage cases before
timing out at keyboard county activation. The subsequent harness uses the
complete native Enter key/character sequence already used by the existing
geometry verifier, and emits focused search/selection diagnostics instead of
dumping unrelated page text. Its outcome must be established by its own run.

**CONFIRMED, unpinned preview only:** a refreshed existing preview first showed
the older no-match wording while the Census response was pending. After the
real response arrived, Ellsworth was discoverable. Changing to `water` briefly
retained the Ellsworth row. Tab/Enter opened Ellsworth in the Evidence Drawer,
which identified the Census edition, external context, and missing KFM
EvidenceBundle. A fresh 390×844 preview also showed the old premature no-match
wording with no `aria-busy` attribute. This is baseline observation, not
acceptance of the merged implementation.

**UNKNOWN:** exact preview/public deployment revision. The preview `/api/build`
navigation was blocked by the browser (`ERR_BLOCKED_BY_CLIENT`); shell GitHub
network access failed DNS resolution. The connected GitHub API supplied the
pinned repository evidence. UI resemblance, a merge, build or CI pass does
not establish production publication.

**NEEDS VERIFICATION:** exact-head browser outcome until CI finishes; physical
phone/virtual keyboard and screen-reader behavior; real slow/failing Census
service recovery against a revision-identified deployment. The synthetic
matrix does not qualify AI answers or admission/publication controls.

## Placement, review and rollback

Accepted ADR-0029 pins Directory Rules v2 at `docs/doctrine/directory-rules.md`,
blob `fd49a0b83e55cef52c1124281f093e263526898d`. Sections 10.1 and 12.4 keep
county UI with its owning application; the existing standalone `tests/`,
`docs/` and `.github/workflows/` families own executable acceptance, explanation
and invocation. The append-only generated-work receipt uses the established
`data/receipts/generated/` lane. No parallel data, schema, policy, evidence or
release authority is created. Production application behavior is unchanged
unless a separately documented confirmed defect is fixed by this follow-up.

Review route: repository owner; no independent approval or publication is
implied. Rollback reverts the bounded test, invocation, note and generation
receipt through review. It requires no store/model/configuration migration.

## Source search relevance — October 31, 2026 Central

The public `water` query returned seven aquifer-reference sources because
`water` occurs inside their `groundwater` category and catalogue order filled
the seven-row cap before River Pulse. This reproduced against the reviewed
source metadata. Availability of a match did not make it reachable within
that bounded result list.

The candidate keeps the existing eligibility filter: every query term must
match the same source's six discovery fields. It changes only source display
order, before the existing cap:

1. Exact dataset identifier, full title or short title.
2. Every query term matches the start of a word in those dataset names.
3. Every query term matches the start of a word in the existing discovery fields.
4. Remaining substring matches, which remain eligible.

Word tokens retain Unicode letters and numbers; no query becomes a regular
expression. Equal-rank sources retain catalogue order. Counties still come
first, map-index order is unchanged, and no input catalogue is mutated.
Limitations/fallback wording stays outside the index. These are text relevance
tiers, not scientific confidence, evidence quality, source admission or release
decisions. Some previously visible broad matches can move below the cap;
narrower dataset/provider queries remain available.

Two new regressions fail before the application change and pass afterward,
including actual aquifer/snapshot metadata and the actual River Pulse discovery
fields. A separate no-provider-I/O probe of the full source catalogue places
River Pulse in the first seven `water` results. The existing three-viewport
browser journey now also requires River Pulse in those current water matches,
while retaining its keyboard, draft, explicit-selection and visibility checks.
New-head browser acceptance remains a separate execution result recorded in
the PR; authored coverage is not a passing claim.

Four existing files own the change: `app/atlas-discovery.ts` for interaction
support, its existing ordinary and browser tests under `tests/`, and this
guidance under `docs/`. This follows the standalone AGENTS profile and accepted
ADR-0029/adopted Directory Rules consulted for the preceding changes; no new
responsibility root or parallel authority is created. There is no new data,
schema, dependency, provider request or persistence contract.

Rollback reverts this four-file change and restores catalogue-order results;
stored settings and datasets need no migration. Independent review and any
subsequent publication remain separate from authoring and self-review.
