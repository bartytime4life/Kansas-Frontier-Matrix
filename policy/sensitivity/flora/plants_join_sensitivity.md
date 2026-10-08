<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/policy/sensitivity/flora/plants_join_sensitivity
title: "Plant join sensitivity review"
type: policy-review-guide
version: v1.0-draft
status: draft; review-guidance; evaluator-unbound
owners: ["@bartytime4life via CODEOWNERS; specialist review unassigned"]
created: 2026-10-08
created_note: First substantive guide edition; the path predates this update.
updated: 2026-10-08
policy_label: public; review-guidance
owning_root: policy/
responsibility: "Explain the review packet and evidence boundaries for plant join sensitivity review."
truth_posture: PROPOSED guidance; repository-grounded guidance at main@ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe; no terms approval, active rule or release decision.
related:
  - docs/domains/flora/CANONICAL_PATHS.md
  - policy/README.md
[/KFM_META_BLOCK_V2] -->

# Plant join sensitivity review

Draft review guidance, 2026-10-08. Source terms, individual decisions and enforcement must be established for the exact candidate.

## Risk model

Joining individually coarse records can reveal a precise plant location, observer or restricted site. Examples include combining a generalized occurrence with a small habitat patch, collection date, narrative locality or media metadata. Review the result of the join, not only each input's label.

## Review procedure

1. Identify each input, native identifiers, source role, precision and privacy conditions.
2. State the join purpose, keys/spatial operation, tolerance and intended audience.
3. Inspect unmatched records, one-to-many expansion and combinations that narrow the inference region.
4. Assess every resulting map, table, export and explanation.
5. Record the allowed representation or unresolved hold, with source and transformation lineage.

## Synthetic acceptance cases

| Case | What it should expose |
|---|---|
| Coarse occurrence plus uniquely matching small patch | Reidentification risk despite coarse input |
| Multiple indistinguishable patches | Uncertainty must remain; no invented exact match |
| Restricted source joined to public context | Public input does not remove the restriction |
| Export retains hidden native coordinates | Display-only generalization is incomplete |

The adjacent `join_induced_sensitivity.rego` is a default-only proposed rule at the pinned snapshot. Required join tests and runtime enforcement must be established separately. This guide proposes a review checklist and does not approve a join or define a universal generalization threshold.

## Owning references

- [CANONICAL_PATHS.md](../../../docs/domains/flora/CANONICAL_PATHS.md)
- [README.md](../../README.md)
- [README.md](../README.md)
- [SENSITIVITY_ESCALATION.md](../../../docs/runbooks/SENSITIVITY_ESCALATION.md)
