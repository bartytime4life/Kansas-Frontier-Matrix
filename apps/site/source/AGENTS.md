# Preserve this standalone Site

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
