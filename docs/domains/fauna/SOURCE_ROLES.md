<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/TODO-register-fauna-source-roles
title: Fauna Source Roles
type: standard
version: v1
status: draft
owners: TODO(fauna-domain-stewards)
created: 2026-04-27
updated: 2026-04-27
policy_label: TODO(verify-public-or-restricted)
related: [docs/domains/fauna/README.md, docs/domains/fauna/CONTROL_PLANE.md]
tags: [kfm, fauna, source-role, governance]
notes: [Companion role taxonomy for source admission and claim safety checks.]
[/KFM_META_BLOCK_V2] -->

# Fauna Source Roles

Source roles are mandatory semantics, not optional labels. Claims that cross role boundaries without explicit policy approval should fail closed.

## Canonical role table

| Role | Allows | Never implies |
|---|---|---|
| `legal_status_authority` | Jurisdiction-specific listing/status context | Occurrence truth |
| `taxonomic_authority` | Accepted names, synonymy, rank, authority lineage | Legal status or location permission |
| `occurrence_source` | Observation/specimen/survey support with context | Legal authority |
| `occurrence_aggregator` | Discovery and supporting occurrence context | Sovereign truth or exact public release |
| `monitoring_source` | Detection/non-detection and protocol evidence | Public precision entitlement |
| `habitat_context` | Environmental support for interpretation | Presence proof |
| `derived_model` | Suitability/richness/corridor interpretation | Canonical fauna truth |
| `documentary_source` | Historical or narrative support with citation | Unreviewed precise geometry |

## Admission checklist

- [ ] Source has stable identity and version/cadence notes.
- [ ] Rights and redistribution posture documented.
- [ ] Source role selected from canonical table.
- [ ] Sensitivity expectations captured.
- [ ] Citation/attribution requirements captured.

## Claim-role compatibility

| Claim type | Minimum role | Additional required support |
|---|---|---|
| Legal listing/status statement | `legal_status_authority` | jurisdiction + effective date |
| Taxon canonical name | `taxonomic_authority` | synonym handling note |
| Presence/occurrence statement | `occurrence_source` or `monitoring_source` | uncertainty + time window |
| Habitat-only statement | `habitat_context` | explicit non-occurrence disclaimer |
| Modeled suitability statement | `derived_model` | method/version + uncertainty note |

## Guardrails

- Unknown role => `HOLD`.
- Conflicting role evidence => `ABSTAIN` until steward review.
- Missing rights for public use => `DENY` or `QUARANTINE`.

