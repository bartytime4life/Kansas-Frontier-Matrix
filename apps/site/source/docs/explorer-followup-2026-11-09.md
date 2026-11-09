# Explorer follow-up — November 9, 2026

This bounded follow-up starts at `main@a8e6fee3acc05608b57239898a9d1e949dbb9c9c`,
after PR #5788 merged. It addresses two failed CI contexts and two independently
confirmed user-facing data/recovery defects. Repository changes, byte inventory,
human acceptance and hosted deployment remain separate.

## Application changes

- **Geology source points:** each bounded map frame owns a mounted sample with
  fresh loading, source and selection state. Frame replacement, disabling and
  redaction retire requests and markers together. Late responses cannot replace
  the current sample. This removes the synchronous state-reset effect that failed
  the Site lint check, without suppressing the rule.
- **Fire context:** NIFC provider transfer limits remain visible even when fewer
  than 250 incidents are returned. Missing/mismatched Kansas state is withheld.
  Invalid optional dates stay missing and make the result partial while valid
  incidents remain available. Malformed transfer metadata returns a finite error.
  The view remains external provider context, not an alert or admitted KFM data.
- **Daily archive:** failed or pending reads are distinct from a successfully
  verified empty archive. Retry and bounded loading replace indefinite checking.
  Unavailable status does not establish zero dates, no stored records or permission
  to capture. Held or failed captures immediately leave map and feature records;
  county geometry must match the current eligible county capture. An acknowledged
  hold suppresses late reads even if the next catalog refresh fails, and its
  acknowledged note replaces the earlier review note. Existing server-side
  access checks remain authoritative.

## CI evidence and mirror reconciliation

The prior `site` check stopped at one inherited geology loading-effect lint
error; later build/test steps did not run. The prior `water-conformance` check
reported three mirror failures, reproduced locally: a stale selected inventory
and two historical receipt tests comparing old declarations to moving source.

The successor `site-v268-explorer-recovery-overlay-20261109.json` records current
repository overlays and file inventory against its immutable predecessor.
Inherited merged changes and changes proposed in this follow-up are identified
separately. The old receipts are not edited; two historical receipt files also
receive fixed SHA-256 assertions in their tests. Current source still undergoes
strict file-set and per-file byte checks against the selected successor. Restoring
withheld carriers remains an error.

This record has `CONTENT_PARITY_ONLY` authority and `REVIEW_ONLY` status. Source
and overlay review remain pending; human acceptance and hosted equivalence remain
false. Preserved Site v268/source metadata are predecessor declarations, not
fresh verification of hosted source or version state. A matching inventory does
not approve overlays, admit data or authorize publication.

## Validation

The candidate is tested against unchanged lockfiles with deterministic provider
responses and disposable local browser storage:

- Site production build and TypeScript pass. Lint has zero errors and 77 existing
  warnings. All 1,497 Site tests pass, including 12 archive recovery regressions.
- All 368 tests in the water-conformance selection pass, including 67 mirror
  tests. Strict selected inventory checks cover 911 files and 262 withheld paths.
- Synthetic fixture regeneration passes for eight outputs in an isolated
  directory; no reviewed fixture is overwritten. Eight smoke-startup isolation
  tests pass. The disposable local backend smoke passes 110 checks across 79
  routes; 14 provider-only routes are listed and remain outside that offline check.
- Browser review at 1440 by 900 and 390 by 844 verifies actual owner-access
  failure, retry, disabled capture/settings controls, explicit unavailable
  coverage and phone layout without horizontal overflow. Screenshots were saved
  and inspected. No token was entered and no provider capture was requested.
- Verified-empty archives, refresh failure with retained eligible data, held and
  failed status transitions, late replies and acknowledged holds with failed
  refresh use deterministic component fixtures, not an operational archive.

Full field accuracy, every source, complete accessibility, long sessions, the
full monorepo suite and production readiness are not established by this bounded
work. Hosted CI for the submitted commit and human acceptance remain pending;
local browser evidence does not establish hosted behavior.

## Preservation and rollback

The original owner checkout and its six pre-existing edited files are preserved.
No operational store, acquisition, camera, source admission, scheduler activation,
installed service, deployment or hosted publication is changed.

Use a focused inverse commit or equivalent forward fix to undo the application
changes. Revert the new receipt and selector together if undoing inventory
reconciliation; preserve all predecessor receipts and withheld paths. A rollback
to the prior selected inventory exposes its recorded drift rather than hiding it.
