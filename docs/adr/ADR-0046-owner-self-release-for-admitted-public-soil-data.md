<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://adr/0046
title: Owner Self-Release for Admitted Public Soil Data
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
current_path: docs/adr/ADR-0046-owner-self-release-for-admitted-public-soil-data.md
responsibility: "Allow one person to review and release a governed USCRN daily soil package only when every evidence bundle is public and carries the admitted NOAA public-domain license; keep two-person review for everything else."
related:
  - ./ADR-0044-owner-self-release-for-admitted-public-water-data.md
  - ./ADR-0045-owner-self-release-for-admitted-public-weather-data.md
  - ../../packages/policy-runtime/src/policy_runtime/core.py
  - ../../packages/release/src/release/core.py
  - ../../data/registry/sources/soil/noaa-uscrn.yaml
  - ../../pipelines/domains/soil/uscrn_daily_admission.py
  - ../../pipelines/domains/soil/uscrn_daily_package.py
tags: [kfm, governance, release, soil, review]
notes:
  - "Accepted by the repository owner on 2026-10-11 when admitting the NOAA USCRN source, as the second phase of the soil layer."
  - "Applies only to the soil serving gate. It does not widen ADR-0044 or ADR-0045, change the water or weather gates, or touch sensitive data or any other release path."
[/KFM_META_BLOCK_V2] -->

# ADR-0046 — Owner self-release for admitted public soil data

**Status:** ACCEPTED (2026-10-11, @bartytime4life)  
**Supersedes:** no existing decision  
**Extends:** [ADR-0044](./ADR-0044-owner-self-release-for-admitted-public-water-data.md) and [ADR-0045](./ADR-0045-owner-self-release-for-admitted-public-weather-data.md) to the soil serving gate, under the same conditions

## Context

ADR-0044 (water) and ADR-0045 (weather) let the owner alone review and release
a package when every evidence bundle is public and carries that gate's admitted
public-domain license. Neither changes any other domain.

The third governed layer is NOAA U.S. Climate Reference Network (USCRN) daily
soil moisture and soil temperature at 5, 10, 20, 50 and 100 cm for the two
federally operated Kansas reference stations (WBAN 53974 Manhattan 6 SSW and
WBAN 03067 Oakley 19 SSW). Its source was admitted on 2026-10-11 in
`data/registry/sources/soil/noaa-uscrn.yaml` as U.S. public domain. With one
maintainer, the two-person rule would make every soil release impossible, for
the same reason ADR-0044 describes.

## Decision

The soil serving gate is the shared `policy_runtime.serving_gate` called with
`decision_profile="kfm.soil-release-decision/v1"` and
`licenses=SOIL_SELF_RELEASE_LICENSES`. A soil release decision may name the
same reviewer and releaser only when **every** evidence bundle in the package:

1. has sensitivity level `public`, and
2. carries a license on `SOIL_SELF_RELEASE_LICENSES`.

That list holds exactly one entry, the license in the admitted descriptor:
`U.S. Public Domain (NOAA federal station data, 17 U.S.C. 105); USCRN data subject to revision`.

The soil list is separate from the water and weather lists. Each gate requires
its own decision profile, so no gate accepts another family's decision, and
the soil snapshot profile (`kfm.soil-snapshot/v1`) is refused by the water and
weather snapshot checks. Adding a soil license never widens water or weather
self-release.

Everything else in the gate is unchanged: the decision must be `APPROVED`, name
all six references, have ordered review, release and expiry times, and pass
rights and sensitivity checks. Packages carry the admitted license only when
prepared from the admitted descriptor; without admission they keep the rights
hold.

## Consequences

- The owner can release the USCRN soil layer without a second person.
- A soil license reaches the list only by admitting its source and adding it
  here in the same change. A test fails if the list and the admitted
  descriptor disagree.
- Other soil sources (Kansas Mesonet, SSURGO-derived products, modeled soil
  moisture) are outside the admitted scope and would need their own rights
  review and ADR.

## Rollback

Empty `SOIL_SELF_RELEASE_LICENSES`. Soil decisions with matching reviewer and
releaser then return `INDEPENDENT_REVIEW_REQUIRED`. Water and weather are
unaffected.
