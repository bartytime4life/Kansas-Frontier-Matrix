<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/object-family-domain-reference-profile-source-map
title: Object Family Domain Reference Profile Source Map
type: exploratory-source-map
version: v1.0.0
status: proposed; review-pending
owners: OWNER_TBD — Atlas steward · Governance steward · Domain stewards · Contract steward
created: 2026-08-09
updated: 2026-08-09
policy_label: internal; exploratory; source-grounded; non-authoritative
owning_root: docs/
responsibility: source-grounded adaptation of the object-family/domain matrix proposal into a bounded candidate profile without assigning authority or replacing current registers
truth_posture: CONFIRMED source transcription and repository comparison / PROPOSED bounded adaptation pending review / NEEDS VERIFICATION hosted exact-head execution
related:
  - ../../../contracts/governance/object_family_domain_reference_profile.md
  - ../../registers/OBJECT_FAMILY.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../control_plane/domain_lane_register.yaml
tags: [kfm, atlas, governance, object-family, domain, source-map]
[/KFM_META_BLOCK_V2] -->

# Object Family Domain Reference Profile Source Map

## Source lineage

| Source | Confirmed contribution | Boundary |
|---|---|---|
| Google Drive `KFM_Full_Atlas_seed_cards`, document `1whGonKzHVBe5FOU5ovDBakNU4Nf-30tQr09R_UNeBho` | The "Object Family x Domain Reference Matrix" pattern proposes one owner/citing-domain/sensitivity-default view and warns that repository maturity is unknown until checked. | Proposal register, not implementation or adoption evidence. |
| Attached `KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.pdf`, SHA-256 `020a1207c2a6d193dc23defca40d24d429acd1273da17c2494582116ec8e9639`, pages 179-180 | Section 24.14 supplies the matrix columns and distinguishes source-reported ownership/citation from proposed sensitivity defaults. | The PDF calls the matrix proposed; tier defaults are not policy decisions. |
| `docs/registers/OBJECT_FAMILY.md` | Existing human-facing navigational register names object families, owners, citing domains, identity posture, and sensitivity defaults. | It explicitly is not truth, schema, policy, evidence, or release authority. |
| `control_plane/domain_lane_register.yaml` | Existing machine projection supplies the registered domain-lane IDs used for bounded reference validation. | Projection-only; it does not create domains or verify stewards. |
| Live `control_plane/object_family_register.yaml` on GitHub `main` | Existing partial runtime-core machine register proves a separate navigational index already exists. | This packet does not edit, replace, or compete with it. |

## Repository reconciliation

GitHub was inspected on 2026-08-09 with no open pull requests. Live `main`
contained the partial object-family register but did not contain
`ObjectFamilyDomainReferenceProfileCandidate`, its schema, validator, fixtures,
tests, or workflow. The checked repository also already contained:

- the accepted Directory Rules decision and domain-lane projection;
- the human Object Family Register;
- semantic contracts for the five synthetic reference rows used here; and
- separate evidence, source, policy, release, and sensitivity object families.

The implementation therefore adds a candidate profile only. It does not add a
second register or claim that the five fixtures form a complete repository
matrix.

## Bounded adaptation

| Source pressure | Retained behavior | Deferred authority |
|---|---|---|
| One owner per family | Each row has one domain lane or one cross-cutting steward role. | Owner adoption, reassignment, or conflict resolution. |
| Explicit citing domains | Citing lanes are registered, unique, sorted, and `CITE_ONLY`. | Join permission, mutation, inference, or publication. |
| Sensitivity default visible | Tier is retained with `PROPOSED_SOURCE_DEFAULT` and `policy_effect: false`. | Tier-scheme adoption and instance policy. |
| Review ripple visible | Canonical rows and deterministic identity make changes diffable. | Current complete inventory and downstream invalidation execution. |

## Path decision

~~~yaml
path_decision:
  artifact: ObjectFamilyDomainReferenceProfileCandidate
  proposed_path: contracts/governance/object_family_domain_reference_profile.md
  artifact_kind: semantic contract
  authority_owner: object-family/domain reference candidate meaning
  lifecycle_stage: not_applicable
  execution_role: none
  scope_kind: object_family
  scope_id: object-family-domain-reference-profile
  exposure: internal
  mutability: versioned
  evidence:
    - docs/doctrine/directory-rules.md
    - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
    - docs/registers/OBJECT_FAMILY.md
    - control_plane/domain_lane_register.yaml
  rules:
    - DIR-SIGNATURE-001
    - DIR-SIGNATURE-002
    - DIR-PLACE-001
    - DIR-DEP-001
  outcome: PLACE
~~~

The `contracts/governance/` lane owns candidate governance meaning; the schema,
fixtures, validator, tests, workflow, source map, and receipt remain in their
separate responsibility roots. A canonical machine register would remain under
`control_plane/` and requires its own reviewed change.

## Non-effects

This packet does not write a register, assign or change an owner, add a domain,
adopt a sensitivity default, authorize a cross-domain join, mutate another
domain, resolve evidence, evaluate policy, approve review, release, deploy,
publish, or authorize public use.

