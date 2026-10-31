<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/reports/repository-shape-assessment-20261031
title: Repository shape, data optimization and placeholder census assessment
type: report
version: v1.0-draft
status: draft; review-only; observations-only; one redundant .gitignore rule removed; no file moved, deleted or re-encoded
owners: ["@bartytime4life via CODEOWNERS"]
created: 2026-10-31
updated: 2026-10-31
policy_label: repository-facing
owning_root: docs/
responsibility: Record measured repository shape, duplicate and precision findings, a hold-by-hold audit of the gap census, and the owner decisions each candidate optimization requires.
truth_posture: CONFIRMED measurements were taken on the pinned main commit with the commands listed below; every recommendation is PROPOSED and changes nothing until an owner decision and its governed migration or supersession record exist.
related:
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/registers/DRIFT_REGISTER.md
  - docs/atlases/README.md
  - tools/qa/gap_scan.py
  - tools/qa/scaffold_inventory.py
  - tools/validators/directory_governance/repository_topology_baseline.json
  - data/registry/datasets/water_planning/kwo_rac_regions_2026-06-24.json
  - data/receipts/generated/genrec-repository-shape-assessment-20261031.json
[/KFM_META_BLOCK_V2] -->

# Repository shape assessment — 2026-10-31

Status: **REVIEW_ONLY / OBSERVATIONS_ONLY**. This authored checkpoint answers an
owner request to reorganize the repository, optimize its data and create what is
missing. It measures the repository at one commit, audits every placeholder the
repository's own census reports, and lists the optimizations that remain
available. It moves, deletes and re-encodes nothing: each candidate below is
blocked by a hold, a pinned digest or a registered migration that only an owner
decision can release. A measurement here is not a readiness, release or
publication claim. The one repository change made in this pass is a single
`.gitignore` line, described under "Ignore rules that shadow canonical lanes".

## Identity and method

| Surface | Pinned identity | Readback |
|---|---|---|
| `main` | `511cf4373060c1492abf73133fa393bb42bca36c` (merged [#5639](https://github.com/bartytime4life/Kansas-Frontier-Matrix/pull/5639)) | The 40 most recent workflow runs recorded for this commit completed with `success` or `skipped`; none failed |
| Open Dependabot alerts | 0 | `GET /dependabot/alerts?state=open` |
| Open code-scanning alerts | 0 | `GET /code-scanning/alerts?state=open` |
| Open issues | 52 | 36 carry `status: proposed`; 7 carry `priority: p0`; 8 hourly-builder design issues carry no status label |

Measurements used `git ls-files` with `stat`, `sha256sum` over every tracked
file, `tools/qa/gap_scan.py --check --list`, `tools/qa/scaffold_inventory.py
--check`, `tools/validators/maplibre/validate_v6_readiness.py --scan-root .` and
a Python read of the planning-region GeoJSON. Validators were run with CPython
3.12.3 and the `project-test` profile from `tools/ci/install_python_ci.py`;
`pyproject.toml` requires Python 3.11 or newer, and the QA tools use
`enum.StrEnum`, so a 3.10 interpreter fails at import.

## What the tracked tree is made of

| Measure | Value |
|---|---|
| Tracked files | 15,012 (232.0 MB) |
| Markdown files | 5,049 (118.9 MB, 51% of tracked bytes) |
| `README.md` files | 2,577 |
| `.gitkeep` files | 182 |
| Generated receipts under `data/receipts/generated/` | 1,578 files (35.1 MB) |
| Workflow files under `.github/workflows/` | 499 |
| Scaffold inventory (`tools/qa/scaffold_inventory.py`) | 866 findings in 710 files: 709 placeholder markers, 145 stub modules, 12 unresolved descriptors; by surface: schemas 386, tests 170, policy 112, pipelines 74, connectors 68, packages 28, tools 24, contracts 3, scripts 1 |
| Gap census (`tools/qa/gap_scan.py`) | 7 Markdown placeholders, 8 unratcheted placeholders, 0 broken local links; identical to `tools/qa/gap_scan_baseline.json`, so nothing can be ratcheted |
| Topology baseline entries | 89 |
| Machine document registry entries (`control_plane/document_registry.yaml`) | 7, against 5,049 Markdown files; the `present` profile of `check_meta_blocks.py` reports 1 `REGISTRY_ENTRY_INCOMPLETE` and 4 `REGISTRY_ENTRY_MALFORMED` findings on the current register |

Half of the repository by bytes is prose, and 866 tracked artifacts are declared
scaffolds. That is the shape the directory doctrine chose; it is recorded here
so that later passes can measure whether it is shrinking.

### Largest tracked files

| Size | Path | Pinned by |
|---|---|---|
| 9.5 MiB | `data/processed/water_planning/rac_regions/kwo_rac_regions_2026-06-24.geojson` | Registry record `sha256` and `byte_count` |
| 3.5 MiB | `docs/brand/readme/kfm-tour-water.webp` | `docs/brand/readme/showcase-media.json` and `genrec-docs-recorded-showcase-20261027.json` |
| 3.0 MiB | `docs/brand/readme/kfm-tour-groundwater.webp` | Same showcase records |
| 2.6 MiB | `docs/brand/logo/The-Kansas-Frontier-Matrix-Seal-transparent-cropped.png` | `genrec-github-readme-seal-9b727d4f45baf935.json` |
| 2.2 MiB | `docs/brand/readme/kfm-tour-history.webp` | Showcase records |
| 1.8 MiB | `apps/site/source/public/og-guided.png` | Site source receipts (`site-v268-*`) |
| 1.4 MiB | `apps/site/source/vendor/vinext-0.0.50-kfm.1.tgz` | Site source receipts |
| 1.2 MiB | `control_plane/verification_backlog.yaml` | Validated projection (`validate_verification_backlog_item.py`) |
| 1.0 MiB | `docs/Kansas Frontier Matrix - Domains v1.1 + Pass 23_32 Consolidated Atlas.md` | Named in `docs/atlases/README.md` as the full-text carrier still at the `docs/` root |
| 0.8 MiB | `apps/site/source/app/page.tsx` (10,717 lines) | Site source receipts |

Every large payload is bound to a digest record. Re-encoding any of them is a
supersession, not an edit.

## Duplicate content

Fifty-six groups of byte-identical tracked files exist; removing every second
copy would recover 230 KB. The only groups above 4 KB are deliberate twins:
five governed-water fixtures and three NEXRAD Level 3 captures kept once under
`fixtures/` or `connectors/noaa/tests/fixtures/` and once under
`apps/site/source/tests/fixtures/`, because the Site is built and
digest-pinned as a standalone source tree. The three consolidated-atlas
Markdown carriers under `docs/` and `docs/atlases/` share almost no lines and
are different documents, not copies; `docs/atlases/README.md` already records
their naming conflict. No duplicate removal is proposed.

## Data precision: the planning-region GeoJSON

`kwo_rac_regions_2026-06-24.geojson` holds 14 polygons made of 543,352
coordinate values written with up to 13 decimal places. At Kansas latitudes a
13th decimal is about 10 nanometres; the seventh is about 11 millimetres. The
file is already minified.

| Encoding | Size | Change |
|---|---|---|
| Current (13 decimals) | 10.00 MB | — |
| Rounded to 7 decimals | 6.75 MB | 33% smaller |
| Rounded to 6 decimals | 6.20 MB | 38% smaller |

The registry record
[`kwo_rac_regions_2026-06-24.json`](../../data/registry/datasets/water_planning/kwo_rac_regions_2026-06-24.json)
pins `payload.sha256`, `payload.byte_count` and the upstream
`source_geojson_sha256`, and its schema carries `dataset_version_id`,
`supersedes_ref` and `correction_status`. Rounding is therefore a **new dataset
version** with its own registry record, crosswalk check and receipt, and a
decision on whether a lossy derivative may sit in PROCESSED beside the exact
capture. This pass changed no bytes.

## Placeholder census audit

Each of the 15 gap-census findings was opened and traced to the control that
depends on it. None is an oversight.

| Finding | Why it stays |
|---|---|
| `docs/domains/soil/RELEASE_INDEX.md` (3 lines) | `domain-soil.yml` `publish-dry-run-soil` pins its SHA-256 (`3cc12c9c…`) as the no-release marker restored by #4941; substantive guidance lives in `CATALOG_CLOSURE.md` |
| `policy/domains/roads-rail-trade/README.md`, `policy/domains/settlements-infrastructure/README.md` | Each README states that its domain workflow checks the literal `PROPOSED (greenfield scaffold)` posture |
| `policy/sensitivity/README.md`, `policy/sources/rights/README.md` | Describe corpora that are scaffolds (empty `properties`, `default allow := false` with no rules); the label is accurate |
| `packages/domains/geology/src/geology/README.md`, `packages/domains/soil/src/soil/README.md` | Namespaces contain only `__init__.py`; the status describes the package, not the document |
| `fixtures/domains/fauna/valid/range_polygon.geojson`, `seasonal_range.geojson` | Their schemas (`range_polygon.schema.json`, `seasonal_range.schema.json`) have empty `properties`; no valid fixture can be written until a steward defines fields |
| `infra/compose/docker-compose.yml` | Operative (the `infra-compose-smoke` workflow renders and builds it) and named "the bounded Compose placeholder" by `tests/infra/test_compose_static.py` |
| `release/*.rego` (three files) | `default allow := false` with no rules; adding rules is a policy decision |
| `artifacts/qa/lint/mypy.txt`, `artifacts/build/env/tool-versions.yaml` | No mypy configuration exists; two tool versions are `NEEDS_VERIFICATION` |

Because the census equals its baseline, `gap_scan.py --write-baseline` and
`scaffold_inventory.py --write-baseline` would write identical files.

## Structural drift: all already registered

| Pair | Where it is governed |
|---|---|
| `data/catalog/domain/` and `data/catalog/domains/` | Topology baseline rule `KFM-TOPO-008`; both READMEs name the plural a compatibility alias while `docs/domains/soil/CANONICAL_PATHS.md` v1.2 names the plural the target; recorded as `OPEN-SOIL-10` |
| `release/manifest/` → `release/manifests/`, `release/correction/` → `release/correction_notices/`, `release/rollback/`, `release/corrections/` | Topology baseline migration subjects |
| `schemas/contracts/v1/source/` and `sources/` | `DRIFT_REGISTER.md`, 2026-09-26 |
| Atlas carriers at the `docs/` root and under `docs/atlases/` | `docs/atlases/README.md`, "Naming, compatibility and path drift" |

A file move for any of these is a `MIGRATE` outcome under the adopted Directory
Rules and needs an accepted decision plus a baseline update. No unregistered
placement drift was found in this pass.

## Ignore rules that shadow canonical lanes

`git ls-files | git check-ignore --stdin` shows 2,142 tracked files whose paths
the current `.gitignore` would hide if they were new. Most are by design: the
"Data lifecycle" rules (lines 18 to 24) ignore `data/raw/**` through
`data/published/**` except READMEs and `.gitkeep`, and lines 27 to 30 ignore
`data/receipts/**/*.json` and `data/proofs/**/*.json` as "governed — write only
via tooling". Admitted payloads and receipts are therefore added deliberately
and stay tracked.

One rule was not by design. Line 42, an unanchored `receipts/` filed under the
"OS" heading, was introduced by an automated commit on 2026-05-12 and matched
1,690 tracked files. For `data/receipts/` it duplicated the governed rules
above; outside `data/` it silently ignored any new file under
`contracts/receipts/`, `schemas/contracts/v1/receipts/`, the per-domain
`schemas/…/receipts/` folders, `fixtures/contracts/v1/receipts/`,
`tests/validators/receipts/` and `tools/validators/receipts/`, where 58 tracked
contracts, schemas, fixtures, tests and validators had to be force-added. This
pass removes that one line. The governed data rules are unchanged, every
tracked file keeps its status, and a new receipt JSON under `data/receipts/` is
still ignored until it is added on purpose.

## Dependency note

`pnpm-workspace.yaml` overrides `vite` to 8.3.3 for the pnpm workspace
(`packages/maplibre`'s vitest), while `apps/site/source/package.json` and its
own `package-lock.json` declare 8.3.4. The Site is not a pnpm workspace member
(its manifest sits one level below `apps/site`), so the two graphs do not
conflict and no open alert names either version. Whether the override is
meant to lag the Site is **NEEDS VERIFICATION**.

## MapLibre readiness readback

At this commit `packages/maplibre/package.json`, its lock importer,
`apps/site/source/package.json` and `validate_v6_readiness.py` all select
`maplibre-gl` 6.9.0, and Dependabot ignores that package. The native scan
returns `HOLD` with the single reason `RUNTIME_PROBES_PENDING`; all 12 probes
are `NOT_RUN` because `configs/maplibre/v6-probe-results.json` does not exist
and the repository has no probe runner. This was recorded on
[#2906](https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/2906)
on 2026-10-31.

## Candidate optimizations and the decision each needs

| Candidate | Effect | Blocked on |
|---|---|---|
| Round `kwo_rac_regions` to 7 decimals as a successor dataset version | −3.25 MB in PROCESSED; smaller downstream carriers | Owner decision that a rounded derivative may be a registered version; new registry record with `supersedes_ref`; crosswalk re-check; receipt |
| Re-encode the three README tour images (8.7 MB) at a lower quality or width | Faster README render on GitHub | Showcase record supersession; visual review of the replacements |
| Retire or supersede the eight hourly domain-builder design issues (#3663–#3679) | Removes eight BLOCKED holds from the open queue | The owner retirement decision those issues themselves ask for |
| Build the 12-probe MapLibre runner and commit `v6-probe-results.json` | Turns #2906 from HOLD into reviewable evidence | Engineering work plus the package-owned acceptance contract the issue names |
| Repair the five register findings in `control_plane/document_registry.yaml` | Makes the review-only registry delta usable | Document-registry steward; the validator never writes the register |
| Split `apps/site/source/app/page.tsx` (10,717 lines) | Maintainability of the Site | Site versioning and its source-digest receipts |

## Non-effects

Apart from deleting one redundant `.gitignore` line, this report moves,
deletes, re-encodes or re-baselines no file. It grants no
source admission, policy decision, review approval, release, deployment,
promotion or publication, and it does not change any hold recorded above. Its
receipt is
[`genrec-repository-shape-assessment-20261031.json`](../../data/receipts/generated/genrec-repository-shape-assessment-20261031.json).

[Reports README](README.md) · [Drift register](../registers/DRIFT_REGISTER.md) · [Directory Rules](../doctrine/directory-rules.md)
