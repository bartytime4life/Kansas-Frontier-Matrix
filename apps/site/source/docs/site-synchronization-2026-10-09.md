# GitHub to private Site synchronization — 2026-10-09

## Exact sources

- Existing owner-private Explorer project: `appgprj_6aa0b1c41bc08191bfd86003920f1631`.
- Starting saved Site: v185, source `ecc8921b715959095bafcd7bc201bc4f14b5b7c6`.
- Requested GitHub main: `d07557107863f60a95b44c6d720147deb16a55b9`.
- Comparison baseline: KFM mirror `37eb3923b500098fce8f263f6ab404ac8fcc31ca`.

The Site and KFM checkouts were clean before edits. The prior Site source and
Git history were archived outside the application tree before reconciliation.
Their SHA-256 values are `fcb884efe96b8004de1fa42c90f0225975c8088001a656b92e40ba0094937e37`
(source tar) and `daf3c457d0597f5f3711acf4962366c25d7fd39ef8dbb9cd23cc02a12d63f828`
(Git bundle). The recovery directory is `/tmp/kfm-github-sync-20261009/recovery`;
saved Site v185 remains the hosted rollback point.

## Reconciliation

The comparison included current Site-only differences, prior mirror updates,
and all later merged changes. GitHub now carries the prior Site's resource
panel, Earth Engine download controls, radar replay auto-start, map-layer
redesign, sample anchors, cutaway detail and opacity, and bounded PC cache.
The retained source now incorporates the refreshed interface and quick start,
Scene panel and presentation effects, offline orientation, background download
center, public map library, synthetic Living Waters proof carrier, NEXRAD storm
context, runtime error isolation, source-time fixes, accessibility and lint fixes.

All files under the pinned GitHub `apps/site/source` match that revision after
reconciliation. Two standalone-only files retain the portable PC cache operator
and its Python tests. The operator is byte-identical to GitHub
`tools/local_data/basemap_cache.py`; the tests differ only in the module path.
The synchronization record is an additional standalone document.

The hosting project, DB and BUCKET bindings, preservation instructions and
record, provider assets, saved-context semantics and owner-only audience remain.
No database migration command was run. The optional additive submission indexes
are included as source; the route also works with the existing database indexes.
No local service was restarted or installed as part of this Site-only update.
No source was admitted or activated. Earth Engine snapshots and NASA thermal
context retain their non-evidence labels and independent source clocks. Scene
effects change presentation only. The 10 GB cache maximum is unchanged.

## Validation before publication

- Production build: passed.
- TypeScript `tsc --noEmit`: passed.
- Complete standalone Node suite: 747 passed, 0 failed, 0 skipped. This includes
  the focused rendering, source-time, radar/fire, Earth Engine, cutaway, cache,
  interaction, download, scene and source-boundary regressions; the portable
  Python cache tests run through this suite.
- ESLint: 0 errors, 46 warnings.
- `git diff --check`: passed.
- Local browser smoke: MapLibre ready; Scene panel opens, Tilted map switches,
  Escape returns focus to the Scene trigger; Real data / Earth Engine switching
  retains 5 selected sources, hides topic filters in Earth Engine, and keeps
  Tune this view visible. Non-evidence/source-year labels were visible.
- Mobile 390 × 844: Scene controls open with no horizontal page overflow.
- New Library & downloads route renders its connection, inventory and map
  catalog sections, with unknown/unavailable state explicit.

Local preview lacks hosted owner context and the full provider environment;
these browser checks do not constitute complete hosted visual/accessibility or
provider acceptance. Tests and deployment do not release the inherited
`MIRROR_REVIEW_REQUIRED` hold. Exact saved source/deployment and audience are
read back separately at delivery. Prior GitHub documentation describes its own
historical checks and remains separate from this synchronization evidence.
