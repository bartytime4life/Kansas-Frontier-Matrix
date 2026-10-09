<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/reports/kansas-history-library-20261009
title: Kansas history library delivery
type: report
version: v1.0-draft
status: feature merged; privately deployed; locally installed; reader correction review pending
owners: ["@bartytime4life via CODEOWNERS"]
created: 2026-10-09
updated: 2026-10-09
policy_label: repository-facing
owning_root: docs/
responsibility: Record the bounded history integration, source identities, local capture and validation.
truth_posture: Observed delivery is scoped below; mirror review, data admission, redistribution, merge and release remain separate.
related:
  - apps/site/source/docs/kansas-history-library.md
  - apps/site/source/public/history/sources.json
[/KFM_META_BLOCK_V2] -->

# Kansas history library delivery — 2026-10-09

**History & archives** is available at
[/downloads#history](https://kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site/downloads#history)
on the existing owner-private Explorer and at `http://127.0.0.1:4173/downloads#history`
on the owner's PC. All 17 supplied source URLs are represented; the two malformed
combined links were split into their four constituent URLs.

Searchable source cards retain access findings, coverage, reuse limitations and
publisher links. The [downloadable source inventory](../../apps/site/source/public/history/sources.json)
records individual evidence and checked times. Fifteen collection, guide or
reference pages remain discovery links: their unknown total holdings are not
silently crawled or mirrored. This integration does not claim access to every
linked institution's restricted or licensed material.

## Material delivered

| Material | Size | Treatment |
|---|---:|---|
| Prentis, *A history of Kansas* (1909), original OCR | 757,514 bytes | Bundled unchanged in Git and Site; checksum-verified reader with full-text search |
| Prentis original PDF | 26,261,072 bytes | Captured privately through the local download operator |
| Anna Estelle Arnold, *A History of Kansas*, original PDF | 24,602,998 bytes | Captured privately; exact edition/year and redistribution remain unverified |

The PDFs total **50,864,070 bytes (48.51 MiB)** and are absent from repository
and hosted deployment assets. Each optional subsequent download displays size,
destination and a selected maximum. Only the two exact researched file URLs
were added to the server's allowlist; existing redirect, length, type, path,
Origin/Host, authentication and capacity guards remain in force.

The [reader](https://kansas-frontier-matrix-explorer.blackbart-55.chatgpt.site/history/prentis-1909)
searches 4,338 OCR paragraphs, rendering 16 per page. It identifies historical
bias, omissions and transcription errors. Passage numbers are not printed page
numbers. Neither narrative nor private captures become governed map facts.

## Source and deployment identity

| Surface | Recorded identity |
|---|---|
| Repository baseline | `cee21f885c60f55b3d6ec4582d8c0a650a407981` |
| Authoritative starting Site | v197, source `a35bad43ca68f1eaee6f33176b8d992d05eab326` |
| Delivered standalone source | `d40828815b8af85e60a798b3af83083b9dd5b5ed` |
| Existing Site project | `appgprj_6aa0b1c41bc08191bfd86003920f1631` |
| Published owner-private version | **v199**, `appgprj_6aa0b1c41bc08191bfd86003920f1631~appgver_c227789ba398819185d1a99de527a231` |
| Successful deployment | `appgdep_6ac9374e4f8881919a802f292229aa40` |
| Stored whole-application archive | `sha256:bbac12c17ab6b8b9ea9d764bdae441950a2ce81c59b64efd5c95bfd86f61518f`, 50,708,480 bytes, 409 files |
| Local Site installation | `/home/bartytime/Projects/KFM-Explorer-Site-history-final-20261009` |
| Local companion source | `/home/bartytime/Projects/KFM-History-Downloads-20261009/source` |

All **16 changed Site paths** match the standalone source byte for byte. This
scoped comparison is not a new claim of complete repository/Site parity or an
independent approval of the governed mirror. Owner-only audience and existing
DB/BUCKET bindings are preserved.

The stable local alias selects the new installation. Both relevant user services
were idle before restart. The existing dependency installation is reused through
a symlink after confirming identical package locks. The previous Site and
companion source remain available for rollback; no data migration occurred.

## Local captures and preservation

| Capture job | File SHA-256 |
|---|---|
| Prentis `71e7f6cace964bc8842ad611365d4d01` | `5efb9aa7c70f91f5fc402c057edfb527a033f6da70ac7fc5e22e9eeef857decd` |
| Arnold `216b85cf63fc455ba1fc8d22513b1a50` | `81de98a1a4e1f469081431c266386b668c21f670496477d369d8f1873901c766` |

Both downloads completed through the browser's existing local operator and show
**Downloaded**. Files reside under
`/home/bartytime/Projects/KFM-data/data/raw/public-maps/history-prentis-1909/`
and `history-arnold-history/`, within their corresponding job directories.
Receipts reside under `data/receipts/ingest/public-maps/` in the same data root.
Both stored files passed independent SHA-256 readback. The Prentis PDF also
matches Internet Archive's published SHA1,
`e216f4d62bde70ac3da18fca90383affb6ac13c2`.

The immutable receipts retain `providerChecksumVerified: false`; the separate
Prentis verification above does not rewrite them. Both remain `UNREVIEWED`,
`NOT_ADMITTED`, and `NOT_RELEASED`. Arnold has no publisher checksum in its
receipt. Its 2014 scan timestamp is not asserted as its publication year.

Installation checks preserved all 82 prior job JSON hashes, 164 original-file
and sidecar size/mtime records, 17 SQLite application-table digests, and 18,392
blob size/mtime records. Size/mtime preservation is not a full byte rehash. The
two new book captures were added after these comparisons. The final reader
correction was installed into a fresh folder and preserved all 84 job hashes,
168 original/sidecar size/mtime records, 17 application-table digests and 18,392
blob size/mtime records. Existing stores and unfinished worktrees were retained.

## Validation and review boundaries

- Production build and TypeScript pass. Lint has zero errors and 45 inherited warnings.
- All **809 Site tests** pass.
- **285 local-data tests plus 153 subtests** pass; three optional-reader tests
  are skipped. The isolated test environment supplied the existing RFC3339
  format-checker dependency; repository dependencies were not changed.
- Local browser checks cover category/filter cards, actual PDF transfers and
  Downloaded indicators, OCR loading, search, keyboard pagination and no results.
  Hosted checks cover all 17 source cards and the reader; `Topeka` returns 131
  passages. These checks are not exhaustive accessibility/device acceptance.
- Codex Security scan `11f151ea-26da-4a43-b73b-c5dc5e198cc8` is sealed with
  **zero reportable findings**, complete coverage of the 19 feature files,
  and an independent architecture review. Frozen snapshot digest:
  `codex-security-snapshot/v1:sha256:cd42a76f15d6ece044737e7a79c65866ec371e3306aff52877aa9d1f22132ff4`.
  This delivery narrative was added after sealing. A subsequent two-file
  supplement reviews the reader retry/lint correction and its callback test
  with zero findings; final native snapshot digest:
  `62b0c0292b7dd3f0e4d6236e28cb2ab5dae92f49a45762859817c72e66de36f3`.
  A report citation should end at `public-map-catalog.json:2851`, not 2854;
  the reviewed content and conclusion are unaffected.

GitHub review/checks and merge are separate from the installed and privately
published result. The existing `MIRROR_REVIEW_REQUIRED` selector and receipts
are unchanged. No source activation, independent mirror approval, data admission,
public release or new redistribution permission is asserted by this report.

The first GitHub run identified two reader lint errors, corrected in the final
source above: retry clears errors in its event handler, and memoized values use
separate declarations. A regression exercises the real retry callback after
a failed response. Hosted `local-data-check` and `validate-docs-meta-block` pass.
The initial `run-validators` failure has exactly the same uppercase-path
fingerprint at baseline `cee21f885c`, main `1900750516`, and feature `bbfdd8c087`.
It concerns pre-existing `docs/wiki/Builder-Profile.md`,
`docs/wiki/Engineering-Case-Studies.md`, and `docs/wiki/Visual-Tour.md`; no waiver
or rename is made here. The water check reports `MIRROR_REVIEW_REQUIRED`.
The owner merged feature PR
[#4982](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/4982)
as `13848164fdb4a6a989ca0ee3ce4f841ace45f938` while the correction was being
verified. This task performed no merge. The reader correction is submitted
separately from that merged feature; current GitHub checks remain authoritative.
