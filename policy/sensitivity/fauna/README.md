<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/policy/sensitivity/fauna/README
title: "Fauna sensitivity review boundary"
type: policy-review-guide
version: v1.0-draft
status: draft; review-guidance; evaluator-unbound
owners: ["@bartytime4life via CODEOWNERS; specialist review unassigned"]
created: 2026-10-08
created_note: First substantive guide edition; the path predates this update.
updated: 2026-10-08
policy_label: public; review-guidance
owning_root: policy/
responsibility: "Explain the review packet and evidence boundaries for fauna sensitivity review boundary."
truth_posture: PROPOSED guidance; repository-grounded guidance at main@ebcc4988a08a3b96d10ee65ae9b4b09a37af5ebe; no terms approval, active rule or release decision.
related:
  - docs/domains/fauna/MAP_UI_CONTRACTS.md
  - policy/README.md
[/KFM_META_BLOCK_V2] -->

# Fauna sensitivity review boundary

Draft review guidance, 2026-10-08. Source terms, individual decisions and enforcement must be established for the exact candidate.

## Scope

This lane contains proposed sensitivity rules and configuration for fauna material. Its files include `geoprivacy.rego`, `deny_default.rego`, `sensitive_taxa_deny.rego`, and YAML inputs for transforms, sensitive taxa, site classes and tiers. Their presence does not demonstrate an accepted bundle, evaluator or enforced public interface.

## Reviewer workflow

Identify the taxon/record class, requested operation, audience and all location-bearing fields. Inspect exact occurrences and nest, den, roost, hibernaculum and spawning-site information. Review indirect disclosure through identifiers, names, dates, joins and downloadable assets as well as coordinates.

The domain map/UI guide requires sensitive geometry transformation before rendering; hiding features with a style filter is insufficient because the original geometry can still reach the client. Retain the reviewed transform, reason, source identity and redaction receipt relationship in any permitted derivative.

## Validation cases to require

| Case | Expected review property |
|---|---|
| Restricted exact point in a public tile | Rejected before client delivery |
| Generalized geometry with original coordinates in popup/export | Rejected as an incomplete transform |
| Join that reconstructs a restricted location | Held for explicit review |
| Missing rights or release evidence | No inferred public permission |

Use the domain's sensitive-occurrence runbook for the complete review packet. Examples must be synthetic and avoid real protected locations. Native rule tests, evaluator binding, review decisions and consumer enforcement remain separately required; this README is not their evidence.

## Owning references

- [MAP_UI_CONTRACTS.md](../../../docs/domains/fauna/MAP_UI_CONTRACTS.md)
- [README.md](../../README.md)
- [README.md](../README.md)
- [SENSITIVITY_ESCALATION.md](../../../docs/runbooks/SENSITIVITY_ESCALATION.md)
