<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://adr/0044
title: Owner Self-Release for Admitted Public Water Data
type: architecture-decision-record
version: v1.0
status: accepted
effective_decision_status: accepted
owners: ["@bartytime4life"]
created: 2026-10-10
updated: 2026-10-10
accepted_on: 2026-10-10
policy_label: public; governance; fail-closed
truth_posture: cite-or-abstain
owning_root: docs/
responsibility_root: docs/
current_path: docs/adr/ADR-0044-owner-self-release-for-admitted-public-water-data.md
responsibility: "Allow one person to review and release a governed water package only when every evidence bundle is public and carries an admitted public-domain license; keep two-person review for everything else."
related:
  - ../../packages/policy-runtime/src/policy_runtime/core.py
  - ../../apps/site/source/app/governed-water.ts
  - ../../data/registry/sources/hydrology/usgs_nwis.yaml
  - ../../pipelines/domains/hydrology/admission.py
  - ../runbooks/water-pilot.md
tags: [kfm, governance, release, hydrology, water, review]
notes:
  - "Accepted by the repository owner on 2026-10-10 in the session that admitted the USGS water source."
  - "Applies only to the governed water serving gate. It does not change other domains, sensitive data, or any other release path."
[/KFM_META_BLOCK_V2] -->

# ADR-0044 — Owner self-release for admitted public water data

**Status:** ACCEPTED (2026-10-10, @bartytime4life)  
**Supersedes:** no existing decision  
**Amends:** the `INDEPENDENT_REVIEW_REQUIRED` rule of the water serving gate

## Context

The water serving gate (`policy_runtime.serving_gate` and its Site copy
`waterGate`) refuses any release decision whose `reviewer` equals its
`releaser`. That rule protects sensitive, restricted or rights-uncertain data,
where a second person catches mistakes the first one makes.

KFM has one maintainer. For the admitted USGS discharge source, the rule made
every release impossible, even though the data is U.S. public domain, comes
from public gauges, and is already published by USGS. A rule that cannot be
satisfied gives no protection; it only keeps the first released layer from
existing.

## Decision

The reviewer and releaser of a water release decision may be the same person
only when **every** evidence bundle in the package:

1. has sensitivity level `public`, and
2. carries a license on the `SELF_RELEASE_LICENSES` list.

The list holds exactly the licenses of admitted public sources. Today that is
one entry, the license recorded in
`data/registry/sources/hydrology/usgs_nwis.yaml`:
`U.S. Public Domain (USGS-authored data, 17 U.S.C. 105); provisional data subject to revision`.

Any package that fails either condition still returns
`INDEPENDENT_REVIEW_REQUIRED` when reviewer and releaser match.

Everything else in the gate is unchanged: the decision must still be
`APPROVED`, name all six references, have ordered review, release and expiry
times, and pass rights and sensitivity checks. Packages carry the admitted
license only when they are prepared with `--admitted-source`; the default
remains the rights hold.

## Consequences

- The owner can release the USGS discharge layer without a second person.
- A license only reaches the list by admitting its source in the registry and
  adding it to both gate copies in the same change. A test fails if the
  Python list, the Site list and the admitted descriptor disagree.
- Sensitive or rights-uncertain data keeps two-person review. Adding a
  non-public source to the list would need a new ADR.

## Rollback

Empty `SELF_RELEASE_LICENSES` in both gate copies. Existing decisions with
matching reviewer and releaser then stop serving and return
`INDEPENDENT_REVIEW_REQUIRED`, which is the pre-ADR behavior.
