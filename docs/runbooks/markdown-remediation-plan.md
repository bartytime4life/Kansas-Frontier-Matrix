# Markdown Remediation Plan (2026-04-25)

This plan focuses specifically on markdown quality debt and documentation trust hardening.

## Snapshot from repository scan

A marker scan across `*.md` files (`TODO`, `UNKNOWN`, `NEEDS VERIFICATION`) shows:

- Markdown files with markers: **163**
- Highest concentration appears in top-level orientation and architecture/docs surfaces.

### Top markdown files by marker volume

| Rank | File | Total | TODO | UNKNOWN | NEEDS VERIFICATION |
|---:|---|---:|---:|---:|---:|
| 1 | `packages/indexers/README.md` | 59 | 36 | 1 | 22 |
| 2 | `docs/architecture/README.md` | 55 | 16 | 10 | 29 |
| 3 | `docs/README.md` | 52 | 26 | 5 | 21 |
| 4 | `apps/ui/README.md` | 49 | 30 | 4 | 15 |
| 5 | `docs/domains/fauna/README.md` | 47 | 10 | 7 | 30 |
| 6 | `packages/genealogy_ingest/README.md` | 44 | 35 | 1 | 8 |
| 7 | `pipelines/kansas_biodiversity_etl/dedupe/README.md` | 39 | 23 | 8 | 8 |
| 8 | `data/catalog/prov/README.md` | 39 | 19 | 3 | 17 |
| 9 | `apps/README.md` | 36 | 12 | 7 | 17 |
| 10 | `pipelines/kansas_biodiversity_etl/catalog/README.md` | 35 | 0 | 3 | 32 |

---

## Next best markdown steps (impact-first)

## 1) Fix "authority" docs first

Priority files:

- `docs/README.md`
- `docs/architecture/README.md`
- `apps/README.md`
- `apps/ui/README.md`

Why:
These pages are navigation and policy-shaping entry points; drift here propagates wrong assumptions quickly.

## 2) Convert marker debt to explicit state taxonomy

For each marker occurrence in the top 10 files, convert to one of:

- `Verified` (now true in repo)
- `Planned` (future work, non-claim)
- `Deprecated` (legacy text to remove)

This avoids ambiguous "TODO-like" prose in authoritative docs.

## 3) Enforce incremental markdown thresholds

Use threshold mode in `tools/ci/report_placeholder_markers.py` as follows:

- Week 1: monitor mode (non-blocking)
- Week 2: enforce one threshold on top-level docs only
- Week 3+: expand threshold enforcement to next docs tier

---

## Suggested 10-day execution packet

### Days 1–3

- Remediate top 4 authority docs.
- Remove/convert at least 40 markers across these files.

### Days 4–6

- Remediate domain + pipeline markdown files ranked 5–10.
- Remove/convert another 40+ markers.

### Days 7–10

- Enable first required markdown threshold for top-level docs.
- Publish post-remediation marker trend in `docs/runbooks/repository-next-steps.md`.

---

## Success criteria

- Top-10 markdown marker total reduced by **>=30%**.
- `docs/README.md` and `docs/architecture/README.md` no longer contain unresolved authority-level TODO statements.
- At least one markdown threshold is active as a required CI check.
