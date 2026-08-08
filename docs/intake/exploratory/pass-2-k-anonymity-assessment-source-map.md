<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/pass-2-k-anonymity-assessment-source-map
title: Pass 2 K-Anonymity Assessment Source Map
type: exploratory-intake-source-map
version: v0.1.0
status: implemented-as-proposed-synthetic-slice; non-authoritative; review-pending
owners: ["@bartytime4life"]
created: 2026-08-08
updated: 2026-08-08
policy_label: public; intake; exploratory; cite-or-abstain
owning_root: docs/
responsibility: Map Pass 2 card KFM-P2-IDEA-0015 to a bounded fixture-first assessment while preserving the atlas as a downstream carrier and keeping policy selection outside the implementation.
truth_posture: "CONFIRMED source identity and repository placement; PROPOSED inactive implementation; NEEDS VERIFICATION human review"
related:
  - ./pass-2-idea-atlas-import-crosswalk.md
  - ../../../contracts/governance/k_anonymity_assessment.md
  - ../../../schemas/contracts/v1/governance/k_anonymity_assessment.schema.json
  - ../../../tools/validators/governance/k_anonymity_assessment_core.py
  - ../../../tools/validators/governance/validate_k_anonymity_assessment.py
  - ../../../tests/validators/governance/test_validate_k_anonymity_assessment.py
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, pass-2, intake, k-anonymity, privacy, fixture-first]
notes:
  - "The Pass 2 PDF remains a cite-or-abstain downstream carrier and does not become policy through this source map."
  - "No k value is adopted. The fixture uses a synthetic policy-selected k solely to exercise deterministic validation."
[/KFM_META_BLOCK_V2] -->

# Pass 2 K-Anonymity Assessment Source Map

## Source identity

| Field | Value |
|---|---|
| Source artifact | `KFM_Pass_2_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf` |
| Artifact SHA-256 | `60451562c8be005ed77afa8c7eada978a7cec05f406cdff137d38ff60123d408` |
| Atlas authority | `downstream-carrier` |
| Truth posture | `cite-or-abstain` |
| Stable card | `KFM-P2-IDEA-0015` |
| Carry state | `NEW` |
| Repository crosswalk | `docs/intake/exploratory/pass-2-idea-atlas-import-crosswalk.md` |
| Authoring repository snapshot | `main@99f367c2dde6f14a2ee698a2cdbe6e4aca0fefda` |

## Adaptation decision

The card proposes documented k-anonymity for sensitive aggregates, with explicit quasi-identifiers and reproducible generalization or suppression. This slice implements the **measurement and validation boundary only**.

| Atlas pressure | Repository adaptation |
|---|---|
| Select a minimum group size | Require `selected_k` to come from a separate `policy_profile_ref`; no default is supplied. |
| Declare quasi-identifiers | Closed `quasi_identifiers` array; an empty set returns `DENY`. |
| Reproducible generalization | Each step identifies the field, before/after granularity, reason, and transform receipt reference. |
| Reproducible suppression | Nonzero suppression requires reasons and transform receipt references. |
| Detect small classes | Any equivalence class below `selected_k` returns `DENY`. |
| Insufficient support | Missing evidence or policy-decision references returns `ABSTAIN`. |
| Contradictory assessment | Broken arithmetic or unexplained transforms returns `ERROR`. |

## Authority and non-effects

This adaptation does not adopt an atlas example threshold. It does not claim that k-anonymity is sufficient for privacy, legal compliance, ethical release, or any particular dataset. It creates no source activation, real-data transform, policy decision, EvidenceBundle, review record, lifecycle write, release, deployment, or publication.

## Dependency-closed packet

- semantic contract;
- closed Draft 2020-12 schema;
- synthetic 14-case fixture matrix;
- pure semantic validator core plus deterministic CLI/fixture runner using the repository hashing package;
- focused no-network unit tests;
- path-filtered hosted workflow;
- generated authoring receipt.

## Follow-up boundary

A later policy PR may define one or more approved threshold profiles only after qualified privacy and domain review. Separate work is also required for cumulative disclosure, differencing, linkage attacks, geography/time composition, release review, and correction propagation. None of those decisions is implied by this fixture slice.

## Rollback

Revert the implementation commit or its eventual merge commit. Intake lineage remains in the merged Pass 2 crosswalk and Git history.
