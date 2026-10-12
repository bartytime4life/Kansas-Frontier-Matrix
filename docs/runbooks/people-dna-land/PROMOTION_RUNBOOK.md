<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook/people-dna-land/promotion
title: People, DNA, and Land Promotion HOLD Boundary
type: runbook
subtype: repository-grounded-hold-boundary
version: v1.0.1
prior_version: v1.0.0
prior_state: repository-grounded promotion HOLD boundary with source refresh still described as proposal-era lineage
status: draft; repository-grounded; fail-closed; operational promotion unavailable; review required
owners:
  - "@bartytime4life — verified GitHub review route"
  - "NEEDS VERIFICATION — accountable People/DNA/Land, privacy, consent, Indigenous/Tribal, legal, policy, evidence, release, operations, security, and independent-review assignments"
created: 2026-05-12
updated: 2026-08-28
policy_label: repository-facing; sensitive-domain; promotion-hold; non-release; non-deployment; non-publication
current_path: docs/runbooks/people-dna-land/PROMOTION_RUNBOOK.md
owning_root: docs/
responsibility: "Prevent proposal-era promotion instructions from being used as operational authority, state the current fail-closed promotion boundary, and route future activation to existing responsibility roots."
truth_posture: cite-or-abstain
authority_class: explanatory promotion hold boundary
authority_rank: subordinate to accepted doctrine and ADRs, contracts, schemas, policy, sources, evidence, review, lifecycle, release, correction, revocation, withdrawal, and rollback authorities
canonical_relationship: same-path supersession of proposal-era text; prior body retained in Git history as design lineage; no sibling authority created
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  reconciliation_base_commit: 813ef14b1dbe5bd236fc902ce8fc3bb2e8ae7e80
  prior_blob: e942483dddef1c036354348c8b0a9ca823da2400
  composition_merge_base_commit: 249974ba480fd68dc749ad0258c84e09477d523a
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  domain_workflow_path: .github/workflows/domain-people-dna-land.yml
  bounded_executable_synthetic_profiles: 2
  operational_promotion_path: unavailable
related:
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../domains/people-dna-land/README.md
  - ./README.md
  - ./ROLLBACK_RUNBOOK.md
  - ./SOURCE_REFRESH_RUNBOOK.md
  - ../../../.github/workflows/domain-people-dna-land.yml
  - ../../../contracts/domains/people-dna-land/README.md
  - ../../../schemas/contracts/v1/domains/people-dna-land/README.md
  - ../../../policy/domains/people-dna-land/README.md
  - ../../../fixtures/domains/people-dna-land/README.md
  - ../../../tests/domains/people-dna-land/README.md
  - ../../../tools/validators/domains/people-dna-land/README.md
  - ../../../data/registry/sources/people-dna-land/README.md
  - ../../../release/candidates/people-dna-land/README.md
notes:
  - "This document does not perform, authorize, simulate, or approve promotion."
  - "The current workflow runs two bounded synthetic consent profiles and explicitly holds broader semantics, policy runtime, proof production, and release dry-run capability."
  - "No real personal, genealogical, DNA/genomic, consent, land, title, parcel, or protected cultural payload was accessed or added."
  - "Operational promotion remains unavailable until every required dependency is established by its owning authority and accountable review."
  - "The source-refresh sibling is a repository-grounded HOLD boundary; it does not supply promotion authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# People, DNA, and Land Promotion `HOLD` Boundary

> **Current disposition: `HOLD`.** KFM does not currently expose a verified operational People/DNA/Land promotion procedure. This document preserves the lifecycle boundary and safe review requirements without granting an operator permission to move, admit, transform, release, deploy, or publish data.

> [!CAUTION]
> Do not place real living-person identifiers, relationship data, family trees, DNA or genomic material, kit or vendor identifiers, consent or revocation payloads, private addresses, exact private locations, person-parcel joins, disputed title material, protected cultural information, or reverse-engineerable sensitive transforms in Git, issues, pull requests, CI logs, fixtures, screenshots, generated artifacts, or public outputs.

> [!IMPORTANT]
> A repository path, schema, policy scaffold, fixture, validator, test, workflow, receipt, green check, draft pull request, merge, or documentation statement is not promotion authority. Promotion remains a separate governed state transition through the owning source, evidence, policy, review, lifecycle, release, correction, revocation, withdrawal, and rollback surfaces.

## Purpose

This same-path replacement retires the prior proposal-era body as executable guidance. The prior version mixed valid safety principles with placeholder owners, unverified paths, proposed reason codes, proposed receipts, proposed policy and schema homes, and illustrative release steps. Those claims remain available in Git history as design lineage, not as an operator procedure.

This boundary may be used to:

- determine that People/DNA/Land promotion is currently held;
- identify the existing responsibility roots that must supply future evidence;
- review a synthetic, documentation-only candidate without sensitive payloads;
- prepare a minimized accountable-review handoff; and
- preserve finite `HOLD`, `ABSTAIN`, `DENY`, `ERROR`, or `ESCALATE` outcomes.

It may not be used to activate a source, admit data, authorize a person or relationship assertion, validate consent, determine living status, establish kinship, infer title or ownership, approve a legal boundary, override sovereignty or stewardship, mutate lifecycle state, release, deploy, or publish.

## Authority and responsibility roots

Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts the [Directory Rules](../../doctrine/directory-rules.md). Human procedures belong under `docs/runbooks/`, while the following concerns remain in their own roots:

| Concern | Owning surface | This document's role |
|---|---|---|
| Domain meaning and source-role limits | [People/DNA/Land domain documentation](../../domains/people-dna-land/README.md) and accepted semantic contracts | Cite; do not redefine identity, relationship, consent, DNA, land, title, or boundary meaning |
| Object meaning and shape | [`contracts/`](../../../contracts/domains/people-dna-land/README.md) and [`schemas/`](../../../schemas/contracts/v1/domains/people-dna-land/README.md) | Require exact accepted versions; do not create or accept them |
| Allow, deny, restrict, abstain, revoke, or withdraw | [`policy/`](../../../policy/domains/people-dna-land/README.md) plus accountable review | Require an authenticated decision from an active binding; do not emulate policy in prose |
| Source admission and rights | [source registry](../../../data/registry/sources/people-dna-land/README.md) and governed source objects | Require resolved admission, rights, provenance, sensitivity, consent, sovereignty, and purpose; do not retrieve or activate |
| Synthetic validation | [fixtures](../../../fixtures/domains/people-dna-land/README.md), [tests](../../../tests/domains/people-dna-land/README.md), and [validators](../../../tools/validators/domains/people-dna-land/README.md) | Route bounded checks; do not substitute synthetic results for operational evidence |
| Release decision | [release candidates](../../../release/candidates/people-dna-land/README.md) and their accepted carriers | Require immutable reviewed evidence; do not create a release decision by checklist |
| Correction, revocation, withdrawal, rollback | Their owning objects and procedures | Keep these states separate; do not claim cleanup, invalidation, restoration, or republication |

## Current repository evidence

At `813ef14b1dbe5bd236fc902ce8fc3bb2e8ae7e80`, the repository exposes two deterministic, no-network synthetic consent profiles through [`domain-people-dna-land.yml`](../../../.github/workflows/domain-people-dna-land.yml). Those profiles test bounded consent-overlay safety and consent-revocation propagation assessment behavior.

Their success is evidence only for the named synthetic fixtures and validators at the tested revision. The workflow explicitly holds broader People/DNA/Land semantics, policy-runtime binding, proof production, and release dry-run capability. No current repository evidence observed for this reconciliation establishes:

- an active People/DNA/Land promotion runtime;
- admitted real sources or approved sensitive-data handling;
- real consent, revocation, deletion, derivative invalidation, or cache invalidation;
- EvidenceRef-to-EvidenceBundle closure for a release candidate;
- authenticated specialist review or enforced separation of duties;
- an approved ReleaseManifest or equivalent immutable release decision;
- an operational rollback target and tested restoration mechanism; or
- deployment or publication authority.

Therefore the only truthful operational outcome is `HOLD`.

## Fail-closed decision table

| Condition | Required outcome |
|---|---|
| Living status, identity, relationship, consent, rights, purpose, audience, role, data class, expiry, revocation, sovereignty, stewardship, retention, or harmful precision is unresolved | `HOLD`, `ABSTAIN`, or `ESCALATE` |
| DNA/genomic material or a living-person record is proposed for public output without an explicit current purpose- and audience-bounded authorization | `DENY` |
| A relationship model, match, cluster, household, surname, graph edge, or generated narrative is offered as proven kinship or identity | `DENY` or `ABSTAIN` |
| An assessor or tax observation is offered as title truth, or parcel geometry as proof of legal boundary or ownership | `DENY` or `ABSTAIN` |
| EvidenceRef does not resolve to an admitted EvidenceBundle at the exact candidate revision | `HOLD` or `ERROR` |
| Contract, schema, active policy binding, source admission, review, release decision, correction path, or rollback target is missing or inconsistent | `HOLD` or `ERROR` |
| Only synthetic tests or documentation checks pass | `PASS` for those checks; promotion remains `HOLD` |
| A live retrieval, lifecycle mutation, release, deployment, or publication action is requested from this document | Stop and route to the owning authority |

Generalization, aggregation, redaction, pseudonymization, client-side filtering, or masking does not itself authorize exposure. A restricted or denied record remains restricted or denied unless the owning policy and accountable review establish a narrower current authorization.

## Evidence required before any future activation

A future operational procedure remains blocked until current implementation authority establishes all of the following without creating a parallel home:

1. accepted domain contracts and schemas for the exact candidate object families and finite outcomes;
2. an active policy-runtime binding covering purpose, audience, access role, data class, time, consent, rights, sovereignty, stewardship, and harmful precision;
3. admitted source descriptors with provenance, rights, retrieval, sensitivity, retention, and correction obligations;
4. EvidenceRef-to-EvidenceBundle closure and deterministic identity for every claim-bearing carrier;
5. synthetic negative tests for living-person exposure, DNA/genomic exposure, consent-scope mismatch, expiry, revocation, relationship-hypothesis collapse, title-role collapse, parcel-boundary collapse, precision leakage, and publication without evidence;
6. auditable correction, revocation, withdrawal, deletion, derivative invalidation, cache invalidation, and rollback mechanisms that remain separate states;
7. an immutable release candidate and authenticated release decision bound to the exact candidate digest;
8. accountable privacy, consent, Indigenous/Tribal, legal, domain, policy, evidence, release, operations, security, and independent review as applicable;
9. enforced separation of duties between author, reviewer, and release authority where required; and
10. exact-head no-network rehearsal and hosted validation whose limits are recorded without being mistaken for approval.

Missing any item keeps promotion at `HOLD`.

## Validation and interpretation

For a documentation-only change to this file:

- run the current repository-native metadata, link, topology, and changed-area documentation checks;
- run the two current synthetic People/DNA/Land profiles when the workflow selects this lane;
- classify outcomes as `PASS`, `FAIL`, `SKIPPED`, `NOT_RUN`, `PENDING`, `INHERITED`, `EXTERNAL`, or `UNKNOWN`; and
- bind every result to the exact tested head.

A green check does not establish human approval, source admission, policy activation, real-person correctness, consent validity, legal sufficiency, title, sovereignty, EvidenceBundle closure, operational promotion, release, deployment, publication, correction, revocation, withdrawal, or rollback.

## Proposal-lineage disposition

The prior v0.1 body is superseded at this path and retained in Git history. It is not copied to another runbook, contract, schema, policy, registry, proof, or release directory. Its proposed object inventory, reason codes, sensitivity tiers, reviewer roles, receipt names, paths, CI commands, worked examples, and promotion steps must not be reconstructed as current authority without fresh evidence from the owning surfaces.

The sibling [source-refresh boundary](./SOURCE_REFRESH_RUNBOOK.md) is a repository-grounded `HOLD` boundary whose prior procedure remains proposal lineage in Git history. The sibling [rollback boundary](./ROLLBACK_RUNBOOK.md) is also a `HOLD` boundary. Neither supplies missing promotion authority.

## Documentation rollback

Before merge, close the draft pull request and delete only its task branch. After a separately authorized merge, revert the focused documentation commit or apply a reviewed forward correction.

Reverting this file restores proposal-era text only. It does not reverse a consent decision, source admission, lifecycle mutation, release, deployment, publication, correction, revocation, withdrawal, deletion, cache invalidation, derivative invalidation, or operational rollback.

## Next dependency-aware review points

1. Preserve the repository-grounded [source-refresh `HOLD` boundary](./SOURCE_REFRESH_RUNBOOK.md); establish any future live implementation only in its owning source, connector, policy, evidence, custody, and review surfaces.
2. Inventory each explicit lane scaffold before filling, superseding, retaining, or retiring it.
3. Establish accepted contracts, schemas, and policy-runtime binding before designing any executable promotion mechanism.
4. Preserve source, evidence, human-review, release, deployment, publication, correction, revocation, withdrawal, and rollback states as separate evidence gates.
5. Keep real or restricted material outside repository-visible surfaces.

[Back to top](#top)
