# Preserved Site baseline

Owner request, 2026-09-24: keep this Site's data and setup from being superseded
by other Site copies. This record preserves the current standalone application;
it does not promote data or modify the KFM monorepo.

## Verified identity

- Site: Kansas Frontier Matrix Explorer
- Project: `appgprj_6aa0b1c41bc08191bfd86003920f1631`
- Application baseline: saved and deployed version **68**
- Source: `46574295bfcdfc02894606f53d769e532acc2682`
- Saved version: `appgprj_6aa0b1c41bc08191bfd86003920f1631~appgver_95e5f91250b88191bcd6b77a064c9ebd`
- Deployment: `appgdep_6ab5a8e32a708191911d825bae792382`
- Native stored archive digest: `sha256:00bbc82866a4f0e58b038736d0f9be591dd0740391025caf0a9693b77806e134`
- Access readback: owner only; no additional editors, viewers or groups.

The baseline includes the Globe-attached Earth Engine panel, viewpoint and
camera controls, eight curated catalog records, Kansas recipes, provenance
labels and the existing Site workflows. Earth Engine remains disconnected.
The application passed its production build and 143 tests in the baseline
session. Browser visual verification remained blocked by an unavailable
admin-enforced security check.

The preservation follow-up adds only editing instructions and documentation.
It must retain every baseline application, dependency, configuration, test and
data file byte-for-byte. Future deliberate changes may build on this baseline.

## Local recovery copy

The task workspace contains a separate `KFM-preserved-site-v68-20260924/`
directory alongside the Site checkout. It contains a Git history bundle, an
exact source archive, the original deployment archive, SHA-256 manifest and
sanitized Site/database readback. Consult its README for verification/recovery.
The original deployment archive and Sites' normalized stored archive have
separate digests; neither is represented as byte-identical to the other.

The DB readback found zero rows in `data_submissions` and
`data_submission_reviews`. This is a dated observation, not a transactional
database export. R2 objects, runtime secret values, external provider responses
and device-local browser settings/Places are not copied into this recovery
snapshot. Existing DB/R2 bindings remain attached to this same Site.

## Future changes and recovery

Follow the root `AGENTS.md`: use current same-Site source; retain the protected
features; do not substitute older mirrors or other projects. Conflicting imports
need explicit owner direction and a reviewed comparison, with a recovery point
before applying them. Additive fixes do not require fresh blanket approval.

Prefer additive repair from the newest source. If the owner requests rollback,
verify the current Site and saved version, preserve newer work, and deploy the
existing saved version 68 to this same project through Sites. Do not create a
replacement Site or repoint storage. Local source recovery should always use a
new empty directory; never extract an archive over an active checkout.

Sites currently exposes saved versions and owner-only access through the tools,
but no platform-wide edit/publication lock. This record and `AGENTS.md` guide
future editing; they cannot prevent every authorized tool from publishing a new
version. The saved version and separate archives provide recovery.

## Placement

Repository-wide editing instructions belong at root; explanatory records reuse
`docs/`. This follows the checked Directory Rules v2 root-file/documentation
responsibilities and accepted ADR-0029, plus this standalone Site's README.
The sibling recovery directory is a task-local backup outside all source and
deployment trees, not a new canonical KFM registry, policy or data store.

### Compact map chrome reconciliation — 2026-10-06
Private Site v157 briefly grouped representation and secondary actions in a
separate compact HUD. That arrangement is historical and is not the current
release surface. The reconciled Explorer uses a 54 px global header followed by
one 44 px map dock: representation, Time, Layers, and Places remain direct;
Basemap and Controls move into the dock's Map overflow below 1440 px. Zoom,
north reset, Fit Kansas, fullscreen, and location remain in Controls. The
single floating Qwen launcher remains available. Keyboard activation, Escape,
focus return, responsive geometry, and minimum target sizes are covered by the
current rendered-shell and browser-geometry checks. No layer, storage, source
eligibility, or audience change is implied. Rollback is saved private Site
v160 plus unloading the local companion.

### Single toolbar — 2026-10-06
The owner's toolbar request consolidates the global header and map dock into
one 54 px row, including on mobile. Wide screens retain direct map modes,
Time, Layers, and Places; the named Map menu provides those controls when
space is limited. More contains Map/Reports/Stories, Compose, Status, Share,
and About. Search and Data remain available. Terrain provider and DEM state
remain in the representation controls. The map and Underground locator no
longer reserve space for a second toolbar. This layout change preserves data,
storage, audience, and source admission state. Revert the single-toolbar
change to restore the previous two-row layout.

### Immersive Underground cutaway — 2026-10-06
This authoring change starts from the current owner-private Site v166, source
`a4d6b3dc69721fbfb270906a9ff3e44dd941d5c0`, on the same project. It preserves the
single 54 px toolbar, owner-only audience, DB and BUCKET bindings, saved-context
keys, source assets and hashes, record-time eligibility, privacy/export rules,
and existing local data stores. The existing aquifer display becomes an
immersive source-bounded cutaway with a live inset locator, independent log
columns, uncertainty envelopes and explicit unobserved space. No continuous
geological or cave model is implied. Rollback is the saved v166 application;
there is no database or source-data migration. Version, deployment and browser
acceptance are separate delivery evidence and are not asserted by this record.

### Larger Underground selector and fluid camera — 2026-10-07
Starting from owner-private Site v168, source
`c74ca07a33f742eecef5461f13769167df3e1d9d`, the cutaway gains a larger measured
selector region and smooth, interruptible camera controls. The same MapLibre
instance supplies the map and captured surface at matching bounds. Camera
pose survives appearance changes, renderer resizing and same-extent record
refreshes; changing the locator extent can fit a new view. Reduced motion and
keyboard/button alternatives remain supported. Plotted-column counts are
separated from eligible loaded-record counts. The single toolbar, owner-only
audience, DB/BUCKET bindings, source bytes and hashes, saved schema, worker
budgets, depth/uncertainty semantics, export privacy and local stores remain
unchanged. No acquisition, geological interpolation or data admission is
introduced. Rollback is the saved v168 application without a storage migration;
deployment and browser acceptance are recorded separately by delivery.

### Direct recorded-column slice — 2026-10-07
Starting from owner-private Site v169, source
`82c73327119909f9b034976bbf7cfb5f727b6caf`, this presentation change exposes a
named-source 3D slice continuation and co-located depth controls. It retains the
saved `3d` enum and schema, existing cutaway/selector behavior, source intervals,
depth units and references, inventory limitations, and record-time filtering.
The clipping outline is a display guide only. The owner-only audience, DB/BUCKET
bindings, source assets, exports/privacy and local stores remain unchanged.
Rollback uses the saved v169 application without a storage migration. Deployment,
source validation and browser acceptance remain distinct delivery evidence.


### Area-first underlay and record time — 2026-10-07
Starting from owner-private Site v170, source
`54e3f661d3dcede372ef8ae90dee99cd0798e3b9`, this change makes explicit geographic
frame selection and compact 3D/record-time navigation the primary Underground
flow. The live selector previews a new area until **Show this area** applies
it; source records and geometry share accepted bounds. Area source filtering
precedes the 50-record cap and retains source/year eligibility, hash checks,
eight requested tiles, twelve cached tiles and partial-coverage labels. The
source assets and depth/uncertainty semantics do not change. Individual-log
slicing remains secondary and saved `aquifer`/`3d` values remain compatible.
The selected rectangle and camera/image are temporary display state; restoring
an area view requires applying a frame again. The single toolbar, owner-only
audience, DB/BUCKET bindings, saved context schema/keys, exports/redaction and
local stores are preserved. No new acquisition or data admission is introduced.
Rollback uses saved v170 without a storage migration. Source checks, delivery
and browser acceptance are distinct; no new visual acceptance is claimed.
