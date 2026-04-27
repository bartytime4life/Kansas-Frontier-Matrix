<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/TODO-register-fauna-control-plane
title: Fauna Control Plane
type: standard
version: v1
status: draft
owners: TODO(fauna-domain-stewards)
created: 2026-04-27
updated: 2026-04-27
policy_label: TODO(verify-public-or-restricted)
related: [docs/domains/fauna/README.md, docs/domains/fauna/SOURCE_ROLES.md, docs/domains/fauna/GEOPRIVACY.md, docs/domains/fauna/VALIDATION.md, docs/domains/fauna/MIGRATION_AND_CONTINUITY.md]
tags: [kfm, fauna, control-plane, governance]
notes: [Initialize fauna control-plane registry for repo-native stewardship and review workflows.]
[/KFM_META_BLOCK_V2] -->

# Fauna Control Plane

Purpose: keep fauna-lane governance legible in one place (owners, review cadence, admission state, release posture, and active risks).

## Operating posture

- **Truth posture:** evidence-first; fail closed on unresolved rights/sensitivity/source-role.
- **Publication posture:** public-safe derivatives only.
- **Activation posture:** fixture-first; live-source enablement only after descriptor + rights + steward approval.

## Stewardship matrix

| Area | Default owner | Backup owner | Cadence | Current status |
|---|---|---|---|---|
| Domain documentation | TODO(fauna-doc-steward) | TODO | Weekly | ACTIVE |
| Source descriptors | TODO(fauna-source-steward) | TODO | Weekly | NEEDS VERIFICATION |
| Geoprivacy policy | TODO(fauna-policy-steward) | TODO | Per release | NEEDS VERIFICATION |
| Validation fixtures | TODO(fauna-validation-steward) | TODO | Per PR | ACTIVE |
| Release + rollback runbooks | TODO(fauna-ops-steward) | TODO | Per release | ACTIVE |

## Change-control gates

A fauna change is merge-ready when all apply:

- [ ] Source role is explicit and appropriate for claim type.
- [ ] Rights and redistribution posture is documented.
- [ ] Public geometry class is assigned and validated.
- [ ] Evidence references resolve to inspectable evidence bundles.
- [ ] Validation results are attached (or linked) for touched surfaces.
- [ ] Rollback path is documented for publish-affecting changes.

## Active risk register

| Risk | Severity | Trigger | Mitigation | Owner |
|---|---:|---|---|---|
| Sensitive location exposure | High | Exact protected coordinates in public payload | Fail-closed validation + redaction receipts | TODO |
| Source-role collapse | High | Aggregator used as legal authority | Enforce role-specific validators | TODO |
| Rights ambiguity | High | Unknown license/terms at promotion time | HOLD/QUARANTINE until rights resolved | TODO |
| Taxonomy drift | Medium | Synonym changes or rank conflict | Deterministic taxon key + migration map | TODO |
| Untracked public release | Medium | Manual artifact publish | Release manifest + rollback runbook required | TODO |

## Review ritual (recommended)

1. Weekly 30-minute fauna governance triage.
2. Review new/changed source descriptors and unresolved risks.
3. Confirm geoprivacy exceptions and steward decisions.
4. Verify pending release items have rollback-ready evidence.

