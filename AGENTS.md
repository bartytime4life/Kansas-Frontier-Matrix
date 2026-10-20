# GoDaddy Node migration composition

The owner requested this separate GoDaddy Node hosting composition on
2026-10-13 and explicitly excluded Airo. Its destination is GoDaddy app
`urdng3v1vk`, selected by the owner as the replacement preview on 2026-10-19.
The prior GoDaddy app `q9r9beo47t` was deleted; references to it are historical,
not an active recovery or deployment destination. For current operations use
`urdng3v1vk` and `docs/godaddy-node-preview.md`; reverify the app and deployed
source before any later publication. Source starts at Explorer v259 commit
`441c3e29581ffb0293d8e643e5c37eed50319032`.
On 2026-10-13 the owner canceled report pricing, checkout and payment setup
and requested free reports/downloads. Keep report exports free and public;
preserve draft labels, source limitations, privacy redaction and governed
publication controls. Do not add checkout or payment setup to this scope.
See `docs/godaddy-node-preview.md` for runtime and verification boundaries.
Keep this composition separate from the original Sites source. Do not modify
the original Site's audience or data bindings.

# Original Sites preservation instructions

The owner requested on 2026-09-24: save this Site so other Site data and setups
do not override it. This instruction applies to this standalone Site checkout.

- Use only Sites project `appgprj_6aa0b1c41bc08191bfd86003920f1631` for this checkout.
- The preserved application baseline is Site version 68, source commit
  `46574295bfcdfc02894606f53d769e532acc2682`. Read
  [the preservation record](docs/SITE_PRESERVATION.md) before source replacement,
  synchronization, data import, or publication.
- Start subsequent work from the latest verified source for this same Site.
  Retain this baseline's Globe/Earth Engine integration, metadata, recipes,
  provider provenance and existing workflows unless the owner asks to change them.
- Another Site, local mirror, fixture workbench, monorepo branch, folder name,
  or newer file timestamp does not supersede this Site. Do not bulk-replace its
  source, configuration or dataset records with those copies without explicit
  owner direction. Compare and preserve both versions first.
- Preserve unpublished edits. Do not reset, force-push or silently roll back an
  advanced remote. Reconcile against the current same-Site source before saving.
- Ordinary requested additions and fixes may proceed. Keep provider observation
  times and existing refresh behavior truthful; preservation does not freeze
  live observations or authorize Earth Engine activation/data admission.
- Preserve the existing audience and DB/R2 bindings. Do not migrate, reset,
  truncate or reseed persisted data as part of ordinary source synchronization.
- Keep recovery archives outside this application's Git tree and deployment
  assets. They are backups, not canonical datasets or release evidence.

This file is a repository editing instruction, not a server-enforced lock.
