<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-domains-geology-aem-survey-campaign
title: GMD 3 AEM Announcement-Bound Campaign Candidate Fixture Contract
type: semantic-contract; fixture-profile; non-authoritative
version: v0.4
status: draft; PROPOSED; DISABLED; NOT_RELEASED; NEEDS VERIFICATION before promotion
updated: 2026-08-03
owners:
  - OWNER_TBD — Geology domain steward
  - OWNER_TBD — Hydrology domain steward
  - OWNER_TBD — Geophysics steward
  - OWNER_TBD — Contract steward
  - OWNER_TBD — Source steward
  - OWNER_TBD — Schema steward
  - OWNER_TBD — Validation steward
linked_schema: schemas/contracts/v1/domains/geology/aem_survey_campaign.schema.json
linked_source_descriptor_fixture: fixtures/contracts/v1/source/source_descriptor/valid/valid_ku_news_gmd3_aem_announcement_2026_05_11.json
linked_validator: tools/validators/domains/geology/validate_aem_campaign.py
fixtures_root: fixtures/domains/geology/aem_survey_campaign/
governance_issue: https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/1944
[/KFM_META_BLOCK_V2] -->

# GMD 3 AEM announcement-bound campaign candidate fixture contract

> **Status:** PROPOSED, connector-disabled, review-pending, and not released.
> This contract describes one frozen repository fixture profile for one source
> document. It does not prove current campaign state, acquisition, or product
> existence.

## Purpose

The profile represents historical announcement context from a University of
Kansas news document published 2026-05-11 about a proposed Southwest Kansas
GMD 3 airborne-electromagnetic campaign. Its machine object type remains
`AemSurveyCampaign` for compatibility with the draft seed packet, but its claim
scope is only `campaign_announcement`.

The prior seed packet required a campaign object to carry raw acquisition,
processing, inversion, resistivity, datum, county-coverage, target-depth, and
product-uncertainty facts. Those values were not established as current or
observed product metadata. Version v0.4 removes that stage and time collapse:
the document's reported posture is historical, current campaign state is
unknown, and no acquisition or downstream product evidence is bound.

## Frozen fixture profile

Profile ID:

    kfm-geology-gmd3-aem-campaign-candidate-fixture-v1

| Field | Required posture |
|---|---|
| `id` | Exact document-bound campaign-candidate fixture identity. |
| `object_type` | `AemSurveyCampaign`. |
| `source_descriptor_ref` | Document-specific `src:ku-news-gmd3-aem-announcement-2026-05-11`; not the broader campaign/product source ID. |
| `announcement_reported_state` | `planned`; historical posture reported by the document. |
| `announcement_published_on` | `2026-05-11`. |
| `current_campaign_state` | `unknown`. |
| `acquisition_evidence_state` | `not_bound_to_profile`; not a claim that acquisition did or did not occur. |
| `survey_method` | `airborne_electromagnetic`, as announcement context only. |
| `claim_scope` | `campaign_announcement`. |
| `supporting_reference_candidates` | One exact typed `fixture://reference-candidate/...` string awaiting governed evidence resolution. |
| `review_state` | `needs_review`. |
| `release_state` | `not_released`. |
| `limitations` | Exact fixture-only, historical-context, current-state-unknown, no-evidence-bound, non-legal, and non-release disclaimers. |

The reference candidate is syntactic fixture identity only. The validator does
not resolve it to an `EvidenceRef` or `EvidenceBundle`, so its presence is not
evidence binding or closure.

## Denied fields and future stages

The candidate denies unscoped `campaign_state`, `acquisition_state`,
`survey_counties`, and `planned_target_depth` fields. The source document may
contain contextual language about a district or equipment design, but this
profile does not turn it into surveyed coverage, achieved depth, current plan,
or product truth.

The following concepts remain future, separately observed and governed stages:

- flight or acquisition segment;
- raw instrument and navigation observation;
- processing run and configuration;
- inversion/model run;
- resistivity section, grid, or voxel;
- hydrostratigraphic interpretation;
- uncertainty/QC result;
- recommendation or management decision;
- released carrier and release decision.

The campaign candidate must not carry product identity, raw-source,
processing/inversion version, CRS/datum/depth-axis, resistivity-unit, no-data,
uncertainty, frequency-system, or footprint-geometry fields.

## Source posture

The linked `SourceDescriptor` is document-specific and fixture-only. It must
remain citation-only, candidate-only, rights-unresolved, restricted,
documentation/manual-review only, connector-disabled, review-required,
proposed, and not released. Its exact bytes are pinned by the validator so
consumer-visible prose, endpoint, connector, credential, source-head, release
condition, or claim-role drift fails closed.

The existing domain-first compatibility YAML uses the broader
`src:kgs-gmd3-aem-2026` identity. This profile does not read, endorse, change,
or bind that record. Reconciliation of that compatibility view is a separate
reviewed change.

## Fail-closed rules

The fixture profile fails when:

1. profile, campaign-candidate, source-document, or reference-candidate identity changes;
2. the source-reported state or publication date changes;
3. current campaign state is represented as known;
4. acquisition evidence is represented as bound or observed;
5. an unscoped planning field or downstream-stage field appears;
6. a required limitation is absent or reordered;
7. correction lineage is missing, outside the typed campaign-candidate namespace, malformed, or self-referential;
8. review or release posture is strengthened;
9. the document descriptor's exact content changes;
10. the descriptor gains stronger role, authority, rights, access, endpoint, connector, source-head, activation, review, or release posture.

Validator findings contain stable codes and JSON paths only. They do not echo
candidate values.

## Not established

- No current campaign status, completed flight, actual footprint, raw record,
  or product bytes.
- No surveyed county coverage, achieved depth of investigation, processing or
  inversion software, CRS, vertical datum, depth axis, resistivity units,
  uncertainty method, or scientific fitness.
- No canonical source admission, data endpoint, connector, schedule,
  credential, or live fetch.
- No resolved evidence, rights clearance, policy decision, proof, cultural or
  steward approval, lifecycle promotion, release, deployment, or publication.
- No groundwater-level observation, water-right/title/legal finding,
  recommendation, operational decision, or life-safety use.

## Run and rollback

    PYTHONDONTWRITEBYTECODE=1 KFM_NO_NETWORK=1 \
      python tests/domains/geology/test_aem_campaign.py --verbose

Rollback is a normal revert of the bounded fixture-profile change. It creates
no live source, lifecycle, proof, release, or published state.
