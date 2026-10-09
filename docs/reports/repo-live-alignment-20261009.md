<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/reports/repo-live-alignment-20261009
title: Repository and live Explorer alignment audit
type: report
version: v1.0-draft
status: checked; privately deployed; repository review pending
owners: ["@bartytime4life via CODEOWNERS"]
created: 2026-10-09
updated: 2026-10-09
policy_label: repository-facing
owning_root: docs/
responsibility: Record bounded repository repairs, exact application parity, validation and recovery.
truth_posture: CONFIRMED observations are scoped below; mirror review, source admission, merge and release are separate.
related:
  - apps/site/README.md
  - docs/reports/kfm-synchronization-20261009.md
[/KFM_META_BLOCK_V2] -->

# Repository and live Explorer alignment — 2026-10-09

The audit started at repository `6609110827e5a4f9e3fcbaeb760471714543628d`
and privately deployed Site v191, source
`9c364d107c1f560455a56e561c31dbbe51fb46e4`. The isolated audit branch advanced
to GitHub main `899dc274ffe37d2900f49eabd66ea3c7b0b2a484`, including the
river-gauge fix merged as PR #4969 during the audit. Other worktrees were
preserved. MEGALODON is outside this audit.

## Corrected errors

- **Soil release index:** commit `797de41dbe` reduced the substantive guide to
  a placeholder, breaking the existing workflow's pinned no-release index
  check. Restored the exact guide from `5c5f6238df`; its existing digest check
  passes. The Soil release hold remains explicit.
- **People/DNA/Land fixture guides:** the same change removed the explanatory
  text required by the workflow from the golden, invalid and valid marker
  files. Restored those three guides from `5c5f6238df`. The executable fixture
  inventory and documentation-only lane checks now pass without weakening
  the consent or release boundaries.
- **SourceEvent receipt replay:** newer schema-read failure handling changed
  two implementation/test files bound by the historical authoring receipt.
  CI now fetches full history and replays that unchanged 21-artifact receipt
  against `045ef1e4f82d28f9a315f8022892441911b131e8`. Current source tests and
  fixture polarity still run separately. Receipt review remains pending.
- **Application drift and navigation:** reconciled 14 explicit Site paths
  with merged repository changes: daylight shader and layer order, lightning
  playback, stable map state, Observatory frame reuse and river-gauge feature
  state. Updated the Site README's obsolete v173/current and source-only labels.

The failed main runs inspected were
[Soil](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/37953425608),
[People/DNA/Land](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/37953425129),
[SourceEvent](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/37953424984)
and [water](https://github.com/bartytime4life/Kansas-Frontier-Matrix/actions/runs/37953425199).
The water failure is the inherited `MIRROR_REVIEW_REQUIRED` hold; its reviewed
receipt and approval state are unchanged.

## Aligned application identities

| Surface | Verified state |
|---|---|
| Repository application | `apps/site/source` at main `899dc274ffe37d2900f49eabd66ea3c7b0b2a484` |
| Standalone source | `424e62cd429ba3ea13a109e6e37953eea857857f` in the existing same-Site history |
| Private hosted Site | **v192**, deployment `appgdep_6ac9102d8b1081918a2454f93eab18ae`, succeeded at 2026-10-09 16:03:06 UTC |
| Saved version | `appgprj_6aa0b1c41bc08191bfd86003920f1631~appgver_056f2824f95c819182bd04d885776532` |
| Stored deployment archive | `sha256:1050e4d8b3593d0258c4cf42c4aba9b509be51fea464e8f5b3e45ec17ba546a0`, 49,807,360 bytes, 398 files |
| Local installation | `/home/bartytime/Projects/KFM-Explorer-Site-alignment-20261009`; stable alias selects it; service active; loopback `/` returns 200 |
| Access and storage | Existing project, owner-only access revision 1, environment revision 5, `DB` and `BUCKET` unchanged |

All **817 mirrored source files** equal the standalone source byte for byte.
The standalone `scripts/basemap-cache.py` remains mapped to canonical
`tools/local_data/basemap_cache.py`; its test maps to
`tests/local_data/test_basemap_cache.py` with the established import-path
difference. These two files are preserved, not duplicated into the mirrored app.
Application byte parity does not approve the historical governed mirror receipt.

The [hosted Explorer](https://kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site)
and the local service on `http://127.0.0.1:4173` use the same 398-file build.
No database migration was necessary: migration source is identical to the
previous installation. Stopped-store backup verification covered **18,416 files**;
all application rows in **eight SQLite databases** and all **18,392 blob files**
were unchanged after installation. Runtime bookkeeping is excluded from the
application-row comparison. This is Site-store preservation, not a checksum
audit of the separate download library.

## Validation and remaining limits

| Check | Result |
|---|---|
| Site production build and TypeScript | Pass on reconciled source |
| Site Node suite | 795 pass, zero failures/skips |
| Site lint | Zero errors; 45 existing warnings |
| Repository schemas, contracts, CI, local-data and QA tests | 1,033 pass, four skips, 372 passing subtests |
| SourceEvent tests and fixtures | 21 unit tests; 21 envelope cases and 13 admission cases pass |
| Historical SourceEvent receipt | All 21 artifacts bound; review pending |
| Repository guardrails | Workflow security, critical-document structure, registry and topology pass; 113 inherited topology warnings, zero new drift |
| Aggregate validators | All 28 selected validators pass after historical blobs are available; the conformance report correctly retains its BLOCKED closure state |
| Local Worker smoke | 57 assertions across 47 routes pass; nine provider-only routes remain outside this offline smoke |
| Browser | Hosted map loads and Observatory advances through committed replay frames; local download service connects and My library opens; local daylight shading renders and toggles off again; no captured JavaScript console errors in these bounded checks |

Use the repository's hash-locked Python test profile with its interpreter first
on `PATH`. The first exploratory Python environment lacked the declared date-time
checker and used a different subprocess interpreter; all three resulting test
failures disappeared with the declared environment. Historical conformance and
topology reads initially lacked Git blobs in the partial checkout; supplying
those blobs restored replay without changing any validator or historical report.

Recent Worker error logs contain Earth Engine catalog **403 access denials**,
not Worker crashes. Configured owner identifiers match the Site owner. The
requesting identity behind the redacted log headers was not independently
established; these entries are not reclassified as successful reads. Authorization
was preserved. Full live-provider, WebGL/device, touch and accessibility acceptance
is not established by this audit, nor is the whole repository proven error-free.
The root JavaScript workspace's explicit `WORKFLOW_HOLD` scripts remain deliberate.

## Recovery

Recovery material is outside the repository at
`/home/bartytime/KFM-site-recovery/repo-live-alignment-20261009`: previous source
bundle, service configuration, verified stopped-store snapshot in `state-verified`
and the installation result. The old installation remains at
`/home/bartytime/Projects/KFM-Explorer-Site-connection-repair-20261009`.
An initial snapshot comparison detected SQLite shared-memory initialization and
returned to the old service before source switching; the verified retry records
store hashes after the read-only SQLite inspection.

Application rollback can select the retained v191 directory or saved private
Site v191. Do not restore an old database over subsequent writes. The source
update restarted only `kfm-explorer-local.service`; companion services and
ongoing downloads were left running.
