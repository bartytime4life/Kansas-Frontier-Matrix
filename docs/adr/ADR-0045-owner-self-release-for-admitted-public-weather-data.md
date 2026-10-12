<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://adr/0045
title: Owner Self-Release for Admitted Public Weather Data
type: architecture-decision-record
version: v1.0
status: accepted
effective_decision_status: accepted
owners: ["@bartytime4life"]
created: 2026-10-11
updated: 2026-10-11
accepted_on: 2026-10-11
policy_label: public; governance; fail-closed
truth_posture: cite-or-abstain
owning_root: docs/
responsibility_root: docs/
current_path: docs/adr/ADR-0045-owner-self-release-for-admitted-public-weather-data.md
responsibility: "Allow one person to review and release a governed GHCN-Daily weather package only when every evidence bundle is public and carries the admitted NOAA public-domain license; keep two-person review for everything else."
related:
  - ./ADR-0044-owner-self-release-for-admitted-public-water-data.md
  - ../../packages/policy-runtime/src/policy_runtime/core.py
  - ../../packages/release/src/release/core.py
  - ../../data/registry/sources/atmosphere/noaa_ghcnd.yaml
  - ../../pipelines/domains/atmosphere/ghcnd_daily_admission.py
  - ../../pipelines/domains/atmosphere/ghcnd_daily_package.py
tags: [kfm, governance, release, atmosphere, weather, review]
notes:
  - "Accepted by the repository owner on 2026-10-11 when admitting the GHCN-Daily source ('admit GHCN-Daily'), as the second phase of the weather layer."
  - "Applies only to the weather serving gate. It does not widen ADR-0044, change the water gate, or touch sensitive data or any other release path."
[/KFM_META_BLOCK_V2] -->

# ADR-0045 — Owner self-release for admitted public weather data

**Status:** ACCEPTED (2026-10-11, @bartytime4life)  
**Supersedes:** no existing decision  
**Extends:** [ADR-0044](./ADR-0044-owner-self-release-for-admitted-public-water-data.md) to the weather serving gate, under the same conditions

## Context

ADR-0044 lets the owner alone review and release a water package when every
evidence bundle is public and carries the admitted USGS public-domain license.
It explicitly changes no other domain.

The second governed layer is NOAA GHCN-Daily station weather (PRCP, TMAX and
TMIN at four federally operated Kansas first-order stations). Its source was
admitted on 2026-10-11 in
`data/registry/sources/atmosphere/noaa_ghcnd.yaml` as U.S. public domain. With
one maintainer, the two-person rule would make every weather release
impossible, for the same reason ADR-0044 describes.

## Decision

The weather serving gate is the shared `policy_runtime.serving_gate` called
with `decision_profile="kfm.weather-release-decision/v1"` and
`licenses=WEATHER_SELF_RELEASE_LICENSES`. A weather release decision may name
the same reviewer and releaser only when **every** evidence bundle in the
package:

1. has sensitivity level `public`, and
2. carries a license on `WEATHER_SELF_RELEASE_LICENSES`.

That list holds exactly one entry, the license in the admitted descriptor:
`U.S. Public Domain (NOAA federal station data, 17 U.S.C. 105); preliminary data subject to revision`.

The weather list is separate from the water list. A weather decision is never
accepted by the water gate, nor a water decision by the weather gate, because
each gate requires its own decision profile. Adding a weather license never
widens water self-release.

Everything else in the gate is unchanged: the decision must be `APPROVED`, name
all six references, have ordered review, release and expiry times, and pass
rights and sensitivity checks. Packages carry the admitted license only when
prepared from the admitted descriptor; without admission they keep the rights
hold.

## Consequences

- The owner can release the GHCN-Daily weather layer without a second person.
- A weather license reaches the list only by admitting its source and adding
  it here in the same change. A test fails if the list and the admitted
  descriptor disagree.
- Volunteer-network data (CoCoRaHS, co-op observers) is outside the admitted
  scope and would need its own rights review and ADR.

## Rollback

Empty `WEATHER_SELF_RELEASE_LICENSES`. Weather decisions with matching reviewer
and releaser then return `INDEPENDENT_REVIEW_REQUIRED`. Water is unaffected.
