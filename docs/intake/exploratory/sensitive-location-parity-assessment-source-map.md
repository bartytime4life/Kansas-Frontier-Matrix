<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/sensitive-location-parity-assessment-source-map
title: Sensitive Location Parity Assessment Source Map
type: source-adaptation-map
version: v0.1.0
status: proposed; exploratory; fixture-only; review-pending
owners: OWNER_TBD — Governance steward · Domain stewards · Policy steward · Validation steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; intake; sensitivity; exact-location; generalization; no-authority
owning_root: docs/
responsibility: Map Pass 20 exact-location fixture pressure to a bounded repository assessment without creating coordinates, policy, evidence, access, transform, release, or publication authority.
truth_posture: CONFIRMED source text and repository paths at main@202976d687e76dfb928f714b61d4a4eaea925bdc / PROPOSED inactive assessment profile / UNKNOWN live policy, registry, access-control, runtime, release, and public behavior
related:
  - ./pass20-expansion-conformance-baseline.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../contracts/governance/sensitive_location_parity_assessment.md
  - ../../../contracts/evidence/spatial_transform_receipt.md
  - ../../../contracts/domains/fauna/sensitive_site.md
  - ../../../contracts/domains/archaeology/sensitivity_transform.md
  - ../../../apps/explorer-web/src/features/redaction_preview/README.md
notes:
  - "Source proposal: Pass 20 EXP-011."
  - "All fixture subjects and references are synthetic; no coordinates or source payloads are admitted."
[/KFM_META_BLOCK_V2] -->

# Sensitive location parity assessment source map

## Goal

Implement the smallest dependency-closed form of Pass 20 `EXP-011`: a
synthetic fixture matrix in which exact public requests are declared denied and
generalized public candidates require a separate transform receipt reference.

This is a declaration-consistency assessment. It does not execute the domain
policies whose coverage it compares.

## Source basis

| Source | Requirement adapted | Boundary retained |
|---|---|---|
| Attached `KFM_Pass_20_Part_2_Idea_Index_Category_Atlas_and_Expansion_Dossier.md`, `EXP-011` (`sha256:57e4b74255b52863f2a489595077741d7f45c2968a9740fe4837bac73778f780`) | Exercise deny-by-default for nests, dens, roosts, archaeological sites, and infrastructure at exact precision; pair generalized posture with a transform receipt. | The atlas is proposal lineage, not live policy, sensitivity-registry, or release authority. |
| Google Drive `New Ideas 5-15-26` (`gdrive://1boJrrqtqk9DcnzU8zymxFBv83r2-jvbep2kecj7WRCQ`) | Preserve fail-closed geoprivacy where benign taxonomy/distribution sources become sensitive through occurrence joins. | No GBIF, iNaturalist, heritage, PLANTS, or other source is fetched, activated, or represented by fixture data. |
| [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md) through accepted [`ADR-0029`](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Separate semantic meaning, machine shape, policy, fixtures, validation, tests, workflows, receipts, and release state. | No new root, cross-domain seam, policy home, registry, or public carrier is created. |

## Repository assay

At the pinned snapshot, repository evidence includes:

- archaeology exact-location deny tests;
- fauna and flora redaction-receipt families;
- habitat occurrence-geoprivacy tests;
- [`SpatialTransformReceipt`](../../../contracts/evidence/spatial_transform_receipt.md);
- [`SensitiveSite`](../../../contracts/domains/fauna/sensitive_site.md);
- archaeology sensitivity-transform semantics; and
- sensitive-overlay governance preflight and reveal-expiry profiles; and
- the Explorer redaction preview, which renders a public-safe release-candidate
  summary but does not define subject-family policy or declaration parity.

These are distinct domain and object-family owners. The assay found no single
cross-family fixture assessment that covers all five `EXP-011` subject families
with exact-deny and generalized-with-receipt polarity. The new assessment
references those owners without copying their policies or receipt schemas. It
also remains upstream of, and independent from, the Explorer preview: this
assessment checks synthetic declarations, while the preview renders an already
governed public-safe projection.

## Adaptation decision

The bounded profile records only:

- an opaque synthetic subject reference;
- a protected subject-family enum;
- the domain that owns the atomic fact;
- a public precision request declaration;
- references to domain, sensitivity, policy, source-snapshot, and evidence
  candidates;
- exact-deny or generalized-with-receipt-candidate disposition;
- transform receipt and method references without transform execution;
- deterministic identity; and
- fixed-false authority effects.

It deliberately stores no geometry, coordinates, bounding box, address,
source payload, occurrence value, asset location, or real-world identifier.

## Placement decision

The object assesses governance declaration parity across existing domain
owners, so semantic meaning belongs under `contracts/governance/`. It is not a
new domain fact, cross-domain join, sensitivity policy, transform receipt, or
release decision. The paired shape, public-safe synthetic fixtures,
deterministic validator, tests, workflow, source map, and authoring receipt stay
in their established responsibility roots.

## Truth posture and non-effects

- **CONFIRMED:** source requirement, current repository owners, target-path
  absence, and Directory Rules responsibilities were inspected.
- **PROPOSED:** the inactive field vocabulary and parity assessment semantics.
- **NEEDS VERIFICATION:** accepted domain adapters, sensitivity-registry
  coverage, policy binding, transform verification, steward roles, and
  correction/appeal procedures.
- **UNKNOWN:** runtime, access-control, hosted check, required-check, release,
  deployment, and public behavior.

Validation does not evaluate policy, resolve evidence, authenticate review,
execute a transform, grant access, mutate lifecycle state, promote, release,
deploy, or publish.

## Rollback

Revert the additive fixture-only packet. Existing domain policies, tests,
receipt families, registries, sources, releases, and public surfaces remain
unchanged.
