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
