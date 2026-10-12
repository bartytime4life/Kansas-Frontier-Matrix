<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/exploratory/pass-18-choropleth-classification-disclosure-source-map
title: Pass 18 Choropleth Classification Disclosure Source Map
type: source-map
version: v1.0.0
status: exploratory; implementation-mapped; non-authoritative
owners: OWNER_TBD — Intake steward · Evidence steward · Cartography steward · Analytics steward
created: 2026-08-10
updated: 2026-08-10
owning_root: docs/
policy_label: internal; exploratory; source-reconciliation; choropleth; classification
responsibility: Reconcile one supplied choropleth-classification disclosure idea with current repository evidence while withholding private discovery-source identifiers from public provenance.
truth_posture: "CONFIRMED supplied-card and repository gap; PROPOSED inactive implementation profile; UNKNOWN consumer adoption and domain-specific fitness; NEEDS VERIFICATION human review and hosted CI"
related:
  - ../../../contracts/evidence/choropleth_classification_disclosure.md
  - ../../../contracts/evidence/measurement_scale_operation_assessment.md
  - ../../../contracts/common/aggregate_statistic.md
  - ../../../contracts/common/geography_version.md
  - ../../../contracts/data/cartographic_omission_disclosure.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, intake, pass-18, choropleth, classification, cartography]
[/KFM_META_BLOCK_V2] -->

# Pass 18 Choropleth Classification Disclosure Source Map

## Source and gap

| Evidence | Observation | Status |
|---|---|---|
| Supplied Pass 18 card `KFM-P18-INV-477` | Choropleth and thematic aggregate layers should disclose classification method, class count, geography unit, and value-range assumptions because those choices can materially change public interpretation. | `CONFIRMED` source statement |
| `contracts/evidence/measurement_scale_operation_assessment.md` | The existing profile checks whether a declared measurement scale is compatible with broad operation families, including quantile classification, but it does not describe one actual class-break declaration. | `CONFIRMED` adjacent contract |
| `contracts/common/aggregate_statistic.md` and `contracts/common/geography_version.md` | Existing shared profiles preserve aggregation and geography-version semantics without owning choropleth classification metadata. | `CONFIRMED` adjacent contracts |
| `contracts/data/cartographic_omission_disclosure.md` | The existing layer-adjacent profile records omission, simplification, and emphasis choices but not class method, breaks, range, nulls, or outliers. | `CONFIRMED` adjacent contract |
| Starting `main@463381703bcd6eada8eea05e95c4a88912ed4b02` search | No exact card ID, choropleth classification disclosure contract, schema, fixture family, validator, workflow, branch, or matching pull request was found before implementation. | `CONFIRMED` bounded gap |
| Connected private research corpus | Used only for candidate discovery and corroboration. Private file identifiers, URLs, and copied prose are intentionally excluded. | `CONFIRMED` provenance boundary |

## Adaptation

The implementation is a closed, synthetic disclosure candidate under the existing evidence family. It composes candidate layer, aggregate-statistic, indicator-definition, and geography-version identities by digest-bound reference; records one classification method, ordered break series, class count, boundary rule, geography unit, value-range assumption, null treatment, and outlier treatment; and requires review-facing legend, Evidence Drawer, review-record, and caveat references for public candidates.

The profile does not define a preferred classification method, class count, break algorithm, scientific threshold, or color ramp. It checks authored declaration coherence only.

## Directory Rules basis

The packet uses existing responsibility roots: semantic meaning in `contracts/evidence/`, shape in `schemas/contracts/v1/evidence/`, synthetic replay in `fixtures/contracts/v1/evidence/`, repository validation in `tools/validators/evidence/`, conformance evidence in `tests/validators/evidence/`, orchestration in `.github/workflows/`, this reconciliation in `docs/intake/exploratory/`, and authoring accountability in `data/receipts/generated/`.

No statistics store, geography authority, layer registry, legend authority, evidence store, policy rule, runtime adapter, lifecycle state, release record, or public surface is created.

## Non-effects and rollback

A local `PASS` authenticates no layer, statistic, indicator, geography version, method, break, legend, evidence, policy, review, release, publication, or public-use state. Rollback is a single additive revert with no external cleanup.
