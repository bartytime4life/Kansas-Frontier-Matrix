# Explorer experience and source reliability review — 2026-10-28

## Scope and source identity

This review follows the public welcome, map entry, county search, selected-record
drawer, report handoff, export review, curated workspace, hosted-source status,
About, topics and source observatory journeys. It does not certify every tool,
provider, browser, physical device or publication control.

- Hosted composition base: `d126c81b80a8c8c1e939aebd29c972fc0ed825d8` on
  `a0-hosted-ai-web-20261017`.
- The public About page identified build
  `bd562032da270cab2ffc7dfc70ec30a730b7214e` and input digest
  `sha256:ab019850d5928e30a5181abfba7d420a6de271ef8022a8a6ed0ecd0baae28eb4`
  when inspected. A repository head is not evidence of public publication.
- GoDaddy hosting preview identification was blocked by a sign-in screen in
  this session. No hosting configuration or publication was changed.
- The separate Barta AI Solutions homepage-card review remains a separate
  repository change; it is not evidence for this Explorer's deployment.

The hosted branch advanced during review. The final reconciliation preserves
the merged welcome readiness/background-work, terrain fallback, and Storm Desk
changes from PRs #5530, #5531 and #5532. Their behavior is inherited rather than
claimed as newly implemented here.

## Demonstrated problems and bounded changes

1. **Selected county lost at report entry.** Selecting the 2020 Census Ellsworth
   County record and choosing Create report opened a governed report with no
   selection or source references. External provider records now enter the
   existing custom map report in selection scope. Preview, JSON and escaped HTML
   share one bounded projection with attribution, provider/source/retrieval
   clocks and an explicit `EXTERNAL_CONTEXT_ONLY` label. This is transient
   context, not an EvidenceRef, EvidenceBundle, registry admission or release.
   Restricted, local, unknown and incompatible selections withhold details.
   Privacy checks also cover an automatically generated title after a selection
   is cleared or replaced. Download substitution treats user text literally.
2. **Source-status responses were trusted too broadly.** Initial reads and manual
   refresh now own cancellation and reject superseded completions. Runtime
   validation bounds rows, fields, counts, dates, states and the declared byte
   limit. Malformed successful responses produce a retryable unavailable state;
   unknown counts remain unknown. Retained data after a failed refresh is
   identified as the last verified response.
3. **A withheld curated workspace looked empty.** The source-record region now
   distinguishes checking, unavailable, withheld, no approved release, partial
   zero and compatible empty responses. Original reasons and navigation remain.
4. **Current hosting and historical identity were conflated.** Status identifies
   the configured public application separately from the preserved Sites and
   repository lineage. Historical identity constants remain intact. Recovery
   copy says Explorer rather than implying the current app is a private Site.

No checkout, paid reports, audience changes, source capture allowlist changes,
new active layers or map layout replacement are introduced.

## Evidence enrichment without activation

Two Konza source candidates were added to the existing source-intelligence
catalog as **held**. They do not fetch biological records, sequences or geometry.

- USDA dataset DOI [10.15482/USDA.ADC/1528782](https://doi.org/10.15482/USDA.ADC/1528782):
  seasonal 2020 soil microbial study metadata, with a bounded study scope and
  BioProject accession attributed to USDA metadata. The NCBI helper could not
  verify the accession independently in this environment.
- Riparian study DOI [10.1371/journal.pone.0106922](https://doi.org/10.1371/journal.pone.0106922)
  is bound to its [published correction](https://doi.org/10.1371/journal.pone.0129409).
  The corrected scope is 20 of 54 watersheds; the design does not support a
  cattle-versus-native-grazer comparison. Discovery summaries that repeated the
  uncorrected scope were not accepted as authority.

Both retain explicit immutable-byte, hash, schema, rights, sensitivity,
EvidenceBundle, admission and release gates. Catalog review date is separate
from observation time. The dated historical corpus snapshot is not rewritten
to imply a new census of admitted sources.

## Validation and limits

The public Chrome journey demonstrated welcome entry, a ready MapLibre map,
county selection, source-time disclosure, the report-selection defect, return
to map, export review and explanatory routes. At the measured mobile CSS
viewport **355 × 767**, welcome entry completed and document horizontal overflow
was zero. This is emulation, not a physical-device performance measurement.

The public curated response was withheld (`PIPELINE_NOT_CONFIGURED`); hosted
archive status reported setup pending and unverified captures/counts. Those
states are not successful data ingestion. A public export download event was
not confirmed, so download acceptance is not claimed from that attempt.

The isolated candidate could build and type-check, but this environment denied
the local HTTP listener (`listen EPERM`). Therefore candidate native browser
acceptance must come from the existing CI browser journey or an independently
identified preview. The county browser journey now exercises the real report
handoff and JSON/HTML download bytes at desktop and mobile fixture sizes; its
fixture data is not a live-provider or publication test.

The reconciled candidate passed the production build and 317 tests across 32
suites: 115 focused tests plus 202 welcome, terrain and Storm Desk integration
tests, with no failures or skips. The page retained the same 42 baseline lint
warnings and zero errors; warning signatures matched. Other changed source,
test and browser-journey files had zero lint warnings or errors. The pull request
records the type check and exact-head CI results separately. No new
paid security scan was run, and historical partial scans do not attest to this
patch or the live host. No actual FPS, heap trend, physical-device or live-host
resource-budget certification is claimed.

## Placement, compatibility and rollback

The project Directory Rules and the hosted composition's `AGENTS.md` were
consulted. Changes stay in existing responsibility roots: `app` for behavior and
the existing catalog, `tests` for behavior-linked verification, and `docs` for
this record. No parallel schema, registry, policy, source or release home is
created. Synced project `sources/` reference material is untouched.

Rollback is a revert of this scoped commit on the hosted branch. There are no
database migrations, persisted-contract changes, hosting edits or activated
sources to undo. Re-run the report privacy/handoff, source-status and curated
tests after reconciliation with future work. Publication requires its own
identified candidate, validation and release decision.
