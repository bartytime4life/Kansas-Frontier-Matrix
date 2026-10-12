<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://adr/0047
title: Owner Self-Release for Admitted Public Storm Events Data
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
current_path: docs/adr/ADR-0047-owner-self-release-for-admitted-public-storm-events-data.md
responsibility: "Allow one person to review and release a governed NOAA Storm Events package only when every evidence bundle is public and carries the admitted NOAA public-domain license; keep two-person review for everything else."
related:
  - ./ADR-0044-owner-self-release-for-admitted-public-water-data.md
  - ./ADR-0045-owner-self-release-for-admitted-public-weather-data.md
  - ./ADR-0046-owner-self-release-for-admitted-public-soil-data.md
  - ../../packages/policy-runtime/src/policy_runtime/core.py
  - ../../packages/release/src/release/core.py
  - ../../data/registry/sources/hazards/noaa.storm_events.yaml
  - ../../pipelines/domains/hazards/storm_events_admission.py
  - ../../pipelines/domains/hazards/storm_events_package.py
tags: [kfm, governance, release, hazards, storm-events, review]
notes:
  - "Accepted by the repository owner on 2026-10-12 when admitting the NOAA Storm Events source, as the second phase of the storm events layer."
  - "Applies only to the storm events serving gate. It does not widen ADR-0044, ADR-0045 or ADR-0046, change the water, weather or soil gates, or touch sensitive data or any other release path."
[/KFM_META_BLOCK_V2] -->

# ADR-0047 — Owner self-release for admitted public Storm Events data

**Status:** ACCEPTED (2026-10-12, @bartytime4life)  
**Supersedes:** no existing decision  
**Extends:** [ADR-0044](./ADR-0044-owner-self-release-for-admitted-public-water-data.md), [ADR-0045](./ADR-0045-owner-self-release-for-admitted-public-weather-data.md) and [ADR-0046](./ADR-0046-owner-self-release-for-admitted-public-soil-data.md) to the storm events serving gate, under the same conditions

## Context

ADR-0044 (water), ADR-0045 (weather) and ADR-0046 (soil) let the owner alone
review and release a package when every evidence bundle is public and carries
that gate's admitted public-domain license. None changes any other domain.

The fourth governed layer is the Kansas (`STATE_FIPS` 20) rows of one data
year's NOAA NCEI Storm Events details file: National Weather Service reports
of hail, wind, tornado, flood, winter and other events by county or forecast
zone. Episode and event narratives are never carried, and the fatalities and
locations files are out of scope. The source was admitted on 2026-10-12 in
`data/registry/sources/hazards/noaa.storm_events.yaml` as U.S. public domain.
With one maintainer, the two-person rule would make every storm events release
impossible, for the same reason ADR-0044 describes.

## Decision

The storm events serving gate is the shared `policy_runtime.serving_gate`
called with `decision_profile="kfm.storm-events-release-decision/v1"` and
`licenses=STORM_EVENTS_SELF_RELEASE_LICENSES`. A storm events release decision
may name the same reviewer and releaser only when **every** evidence bundle in
the package:

1. has sensitivity level `public`, and
2. carries a license on `STORM_EVENTS_SELF_RELEASE_LICENSES`.

That list holds exactly one entry, the license in the admitted descriptor:
`U.S. Public Domain (NOAA federal records, 17 U.S.C. 105); Storm Events data subject to revision`.

The storm events list is separate from the water, weather and soil lists. Each
gate requires its own decision profile, so no gate accepts another family's
decision, and the storm events snapshot profile
(`kfm.storm-events-snapshot/v1`) is refused by the other snapshot checks.
Adding this license never widens water, weather or soil self-release.

Everything else in the gate is unchanged: the decision must be `APPROVED`, name
all six references, have ordered review, release and expiry times, and pass
rights and sensitivity checks. Packages carry the admitted license only when
prepared from the admitted descriptor; without admission they keep the rights
hold.

A released record remains a historical event report. Release does not make KFM
a warning, alerting or life-safety service, and the `not_for_life_safety`
limit in the descriptor still applies.

## Consequences

- The owner can release the Storm Events layer without a second person.
- A storm events license reaches the list only by admitting its source and
  adding it here in the same change. A test fails if the list and the admitted
  descriptor disagree.
- Narratives, the fatalities file, other NOAA hazard products (NWS alerts, SPC
  reports) and other states are outside the admitted scope and would need
  their own rights and sensitivity review and ADR.

## Rollback

Empty `STORM_EVENTS_SELF_RELEASE_LICENSES`. Storm events decisions with
matching reviewer and releaser then return `INDEPENDENT_REVIEW_REQUIRED`.
Water, weather and soil are unaffected.
