<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://adr/0049
title: Owner Self-Release for Admitted Public Earthquake Data
type: architecture-decision-record
version: v1.0
status: accepted
effective_decision_status: accepted
owners: ["@bartytime4life"]
created: 2026-10-12
updated: 2026-10-12
accepted_on: 2026-10-12
policy_label: public; governance; fail-closed; not-life-safety
truth_posture: cite-or-abstain
owning_root: docs/
responsibility_root: docs/
current_path: docs/adr/ADR-0049-owner-self-release-for-admitted-public-earthquake-data.md
responsibility: "Allow one person to review and release a governed USGS ComCat earthquake package only when every evidence bundle is public and carries the admitted USGS public-domain license; keep two-person review for everything else."
related:
  - ./ADR-0044-owner-self-release-for-admitted-public-water-data.md
  - ./ADR-0045-owner-self-release-for-admitted-public-weather-data.md
  - ./ADR-0046-owner-self-release-for-admitted-public-soil-data.md
  - ./ADR-0047-owner-self-release-for-admitted-public-storm-events-data.md
  - ../../packages/policy-runtime/src/policy_runtime/core.py
  - ../../packages/release/src/release/core.py
  - ../../data/registry/sources/hazards/usgs.earthquakes.yaml
  - ../../pipelines/domains/hazards/earthquake_admission.py
  - ../../pipelines/domains/hazards/earthquake_package.py
tags: [kfm, governance, release, hazards, earthquakes, review]
notes:
  - "Accepted by the repository owner on 2026-10-12 when admitting the USGS ComCat earthquake source, as the second phase of the earthquake layer."
  - "Applies only to the earthquake serving gate. It does not widen ADR-0044 to ADR-0047, change the water, weather, soil or storm events gates, or touch sensitive data or any other release path."
[/KFM_META_BLOCK_V2] -->

# ADR-0049 — Owner self-release for admitted public earthquake data

**Status:** ACCEPTED (2026-10-12, @bartytime4life)  
**Supersedes:** no existing decision  
**Extends:** [ADR-0044](./ADR-0044-owner-self-release-for-admitted-public-water-data.md), [ADR-0045](./ADR-0045-owner-self-release-for-admitted-public-weather-data.md), [ADR-0046](./ADR-0046-owner-self-release-for-admitted-public-soil-data.md) and [ADR-0047](./ADR-0047-owner-self-release-for-admitted-public-storm-events-data.md) to the earthquake serving gate, under the same conditions

## Context

ADR-0044 (water), ADR-0045 (weather), ADR-0046 (soil) and ADR-0047 (storm
events) let the owner alone review and release a package when every evidence
bundle is public and carries that gate's admitted public-domain license. None
changes any other domain.

The fifth governed layer is USGS ANSS Comprehensive Catalog (ComCat)
earthquakes whose epicenter lies in the Kansas context envelope, for one data
year: catalog solutions (origin time, epicenter, depth, magnitude) as ComCat
published them at retrieval. Felt reports, ShakeMap and PAGER products are
never carried. The source was admitted on 2026-10-12 in
`data/registry/sources/hazards/usgs.earthquakes.yaml` as U.S. public domain.
With one maintainer, the two-person rule would make every earthquake release
impossible, for the same reason ADR-0044 describes.

## Decision

The earthquake serving gate is the shared `policy_runtime.serving_gate` called
with `decision_profile="kfm.earthquake-release-decision/v1"` and
`licenses=EARTHQUAKE_SELF_RELEASE_LICENSES`. An earthquake release decision may
name the same reviewer and releaser only when **every** evidence bundle in the
package:

1. has sensitivity level `public`, and
2. carries a license on `EARTHQUAKE_SELF_RELEASE_LICENSES`.

That list holds exactly one entry, the license in the admitted descriptor:
`U.S. Public Domain (USGS works, 17 U.S.C. 105); ComCat solutions subject to revision`.

The earthquake list is separate from the water, weather, soil and storm events
lists. Each gate requires its own decision profile, so no gate accepts another
family's decision, and the earthquake snapshot profile
(`kfm.earthquake-snapshot/v1`) is refused by the other snapshot checks. Adding
this license never widens any other family's self-release.

Everything else in the gate is unchanged: the decision must be `APPROVED`, name
all six references, have ordered review, release and expiry times, and pass
rights and sensitivity checks. Packages carry the admitted license only when
prepared from the admitted descriptor; without admission they keep the rights
hold.

A released record remains a catalog solution. Release does not make KFM an
earthquake alerting, shaking-estimate or life-safety service, and the
`not_for_life_safety` limit in the descriptor still applies.

## Consequences

- The owner can release the earthquake layer without a second person.
- An earthquake license reaches the list only by admitting its source and
  adding it here in the same change. A test fails if the list and the admitted
  descriptor disagree.
- Felt reports (DYFI), ShakeMap, PAGER, other catalogs and areas outside the
  Kansas context envelope are outside the admitted scope and would need their
  own rights and sensitivity review and ADR.

## Rollback

Empty `EARTHQUAKE_SELF_RELEASE_LICENSES`. Earthquake decisions with matching
reviewer and releaser then return `INDEPENDENT_REVIEW_REQUIRED`. The other
families are unaffected.
