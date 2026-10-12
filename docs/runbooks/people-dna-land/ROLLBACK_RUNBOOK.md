<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook-people-dna-land-rollback
title: People · DNA · Land — Rollback Runbook
type: standard
version: v1.1.6
prior_version: v1.1.5
prior_state: repository-grounded rollback HOLD boundary whose notes and next-review inventory lagged the merged rollback-drill and validation procedures and still counted vendor watch as a scaffold
status: draft; repository-grounded hold boundary; proposal lineage retained in Git history; operational rollback unavailable; non-release; non-publication
owners:
  - "@bartytime4life — verified GitHub review route"
  - "NEEDS VERIFICATION — accountable People/DNA/Land, privacy, consent, Indigenous/Tribal, legal, policy, evidence, release, operations, security, and independent-review assignments"
created: 2026-05-12
updated: 2026-08-29
policy_label: repository-facing; sensitive-domain; fail-closed; rollback-held; non-release; non-publication
current_path: docs/runbooks/people-dna-land/ROLLBACK_RUNBOOK.md
owning_root: docs/
responsibility: "Explain the current People/DNA/Land rollback hold, identify the evidence required before an operational procedure can exist, and prevent proposal-era prose from being executed as repository authority."
truth_posture: cite-or-abstain
authority_class: explanatory rollback hold and proposal-lineage disposition
authority_rank: subordinate to accepted doctrine and ADRs, contracts, schemas, policy, evidence, accountable review, lifecycle, release, correction, revocation, withdrawal, rollback, deployment, and publication authorities
canonical_relationship: same-path replacement of proposal-era instructions; prior detail remains available in Git history and is not current operational authority
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: cf3c5b76dafa74dee79e5249849e4174c2107638
  current_reconciliation_commit: 4e714b639861e340b0c35a5360f9ffaecdf1f53c
  prior_blob: c370837c701f1e2a92e660e8223702ccee462b94
  lane_readme_prior_blob: 1ba3f28deaaea1fc9811ee1eb58e59558c2ecd84
  promotion_runbook_blob: 6df0ed9fa7bd3800276f72889eeefe07c7706934
  rollback_drill_blob: 9088cbff694297613882bfae86b259f93023ff03
  validation_runbook_blob: c1987d5f3b4a0419fa9aa970a71d7cef9d1c341e
  vendor_watch_prior_blob: 84d77e7e9a9d4afb2ee367ff11841a837bdf1a8c
  domain_workflow_blob: bcf64c3e3b6653b9543489fc5a6031805ae3ef48
  tests_readme_blob: 5f1672f24a2992d83829d280cfd2f05b9b6848f6
  policy_readme_blob: 7260394c77d79629895da16d8d680e8d80c56b32
  release_readme_blob: 60b6a656f8f2b765616bba7223f51c25863c7172
  release_rollback_cards_readme_blob: c1fc4d27bca8144faa16e1b888ca95c5d2f88eb5
  release_schema_readme_blob: e3b06be3eb094885eff6b8b3eb85d3be3120f039
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
related:
  - docs/runbooks/people-dna-land/README.md
  - docs/runbooks/people-dna-land/PROMOTION_RUNBOOK.md
  - docs/runbooks/people-dna-land/SOURCE_REFRESH_RUNBOOK.md
  - docs/runbooks/people-dna-land/ROLLBACK_DRILL.md
  - docs/runbooks/people-dna-land/VALIDATION_RUNBOOK.md
  - docs/runbooks/people-dna-land/VENDOR_WATCH_SOP.md
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - tests/domains/people-dna-land/README.md
  - policy/domains/people-dna-land/README.md
  - schemas/contracts/v1/release/README.md
  - release/README.md
  - release/rollback_cards/README.md
  - .github/workflows/domain-people-dna-land.yml
tags: [kfm, runbook, people-dna-land, rollback, sensitive-domain, hold, proposal-lineage, fail-closed]
notes:
  - "v1.1.3 pins the reconciled lane index and promotion HOLD boundary blobs so the rollback consumer's evidence snapshot matches its current maturity claim."
  - "The prior 2026-05-12 body is retired from operational use because current repository evidence does not establish its kill switch, release target, derivative invalidator, signer route, timing targets, or end-to-end rollback runtime."
  - "This file does not execute rollback, revoke consent, delete data, invalidate derivatives or caches, restore a release, or authorize any public-path change."
  - "The lane remains held for operational rollback maturity; this repository-grounded hold boundary narrows unsafe claims without upgrading operational status."
  - "Promotion and source refresh are separate repository-grounded HOLD boundaries; the rollback drill and validation runbook are repository-grounded documentation; vendor watch is manual repository-visible review; no direct child remains an explicit scaffold."
[/KFM_META_BLOCK_V2] -->

# People · DNA · Land — Rollback Runbook

> [!CAUTION]
> **STOP — operational People/DNA/Land rollback is not established by current repository evidence.** Do not execute the prior proposal-era steps, timing targets, object examples, kill-switch instructions, or signer assumptions from this path. Their lineage remains in Git history only.

This document is the current repository-grounded hold boundary for rollback involving People, genealogy, DNA/genomic material, consent, living-person information, land assertions, parcel context, title instruments, or culturally restricted material. It explains what is known, what remains missing, and when to stop. It is not a rollback mechanism, incident-response playbook, approval, release decision, legal determination, or publication authority.

## Current outcome

| Question | Current answer | Required posture |
|---|---|---|
| Is there an executable People/DNA/Land rollback procedure? | No complete procedure is verified. | `HOLD` |
| Is a domain rollback target or release manifest verified? | No domain target is established by this lane. | `HOLD` |
| Is a public-surface kill switch verified? | No route, runtime binding, or receipt producer is established here. | `ESCALATE` |
| Is derivative or cache invalidation operational? | The synthetic consent assessment declares seven surfaces, but it does not invalidate deployed derivatives. | `HOLD` |
| Are accountable rollback signers established? | CODEOWNERS supplies a repository review route only; specialist and independent roles remain unverified. | `ESCALATE` |
| Can a passing domain workflow authorize rollback or release? | No. It proves only two bounded synthetic consent profiles at the tested revision. | `DENY` implied authority |

## Repository evidence

- The [lane boundary](./README.md) classifies operational rollback as held and this file as the current repository-grounded hold boundary; the superseded procedure remains proposal lineage in Git history.
- The [domain test index](../../../tests/domains/people-dna-land/README.md) documents two deterministic, synthetic, no-network consent profiles. Neither performs a deployed rollback.
- The [domain workflow](../../../.github/workflows/domain-people-dna-land.yml) runs those profiles and explicitly holds broader policy runtime, proof, real revocation, cleanup, release, and rollback work.
- The [domain policy boundary](../../../policy/domains/people-dna-land/README.md) records proposed or evaluator-unbound policy surfaces; documentation does not activate them.
- The [release root](../../../release/README.md) owns release, correction, withdrawal, and rollback decisions. A repository record is still not an operational decision.
- The [rollback-card index](../../../release/rollback_cards/README.md) describes review aids and currently lists no People/DNA/Land sublane.
- The [release schema index](../../../schemas/contracts/v1/release/README.md) records a mixed-maturity generic `RollbackCard` family. Schema presence does not authenticate a card, select a target, or execute rollback.
- Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) and the adopted [Directory Rules](../../doctrine/directory-rules.md) keep human procedure, policy, schemas, tests, evidence, and release decisions in separate responsibility roots.

## Fail-closed operating boundary

Unknown living status, unclear consent, disputed identity, unresolved rights, unclear sovereignty or stewardship, harmful precision, missing evidence, uncertain title role, or absent accountable review does not produce rollback approval. It produces `HOLD`, `ABSTAIN`, `DENY`, or `ESCALATE` as applicable.

The following distinctions remain mandatory:

- Consent grant, authorization, revocation, withdrawal, correction, retention, deletion, derivative invalidation, cache invalidation, and rollback are separate states.
- Relationship assertions and DNA-derived links remain hypotheses until evidence-bound.
- Assessor and tax records are administrative observations, not title truth.
- Parcel geometry is contextual geometry, not proof of legal boundary or ownership.
- Deeds, title instruments, encumbrances, tenure, jurisdiction, transaction time, record time, and current ownership remain distinct.
- Indigenous, Tribal, descendant-community, burial, archaeological, sacred-site, cemetery, and culturally restricted material requires sovereignty-aware stewardship. Generalization alone does not authorize exposure.
- Maps, tiles, graphs, indexes, summaries, dashboards, and generated text are derived carriers, not sovereign truth.

## Stop conditions

Stop and escalate without attempting repository-directed rollback when any of these is true:

- a real living person, DNA/genomic record, consent record, family relationship, private address, exact private location, parcel-owner join, disputed title, or protected cultural payload would need to be accessed or copied;
- no authenticated release authority, privacy or consent reviewer, applicable rights-holder or sovereignty-aware reviewer, domain steward, operations owner, and independent review route is established;
- the affected release, safe target, evidence chain, policy decision, correction or withdrawal state, or downstream consumer inventory cannot be resolved;
- a proposed command, route, schema example, receipt, role, timing target, or directory is the only support for the action;
- rollback would be used as a substitute for revocation, deletion, erasure, correction, withdrawal, or incident containment;
- a test, workflow, document, dashboard, or generated narrative is being treated as approval.

Repository-visible discussion, fixtures, logs, and pull requests must remain synthetic, minimized, deterministic, public-safe, and no-network. Do not place sensitive payloads or reverse-engineerable transforms in them.

## Evidence required before operational activation

An operational procedure remains blocked until current implementation authority establishes all of the following in their existing responsibility roots:

1. an accepted domain contract for rollback semantics and finite outcomes;
2. a current machine-checkable schema and authenticated release-decision carrier;
3. active policy-runtime binding with explicit purpose, audience, role, data-class, time, consent, rights, and sovereignty handling;
4. a resolved affected release and independently verified safe target;
5. EvidenceRef-to-EvidenceBundle closure for every claim that depends on evidence;
6. deterministic synthetic negative tests for living-person, DNA/genomic, consent-revocation, source-role collapse, title-role collapse, harmful precision, and publication without evidence;
7. real derivative, graph, tile, index, export, cache, and generated-text invalidation mechanisms with auditable receipts;
8. correction, withdrawal, revocation, retention, deletion, and rollback paths that remain distinct;
9. authenticated accountable reviewers and enforced separation of duties;
10. a no-production, no-network rehearsal whose result is reviewed without being mistaken for operational completion.

Missing any item keeps the procedure at `HOLD`.

## Proposal-lineage disposition

The prior body is superseded at this path and retained in Git history as design lineage. It is not copied into a second authority home. In particular, prior references to immediate disablement, fixed response times, a governed-API kill switch, `SurfaceDisableReceipt`, domain-specific `RollbackCard` fields, republication, cache invalidation, and required signers were not verified as executable current behavior and must not be reconstructed from this document.

The sibling [promotion](./PROMOTION_RUNBOOK.md) and [source-refresh](./SOURCE_REFRESH_RUNBOOK.md) documents are separate repository-grounded `HOLD` boundaries. Their prior operational detail remains proposal lineage in Git history. Neither supplies missing rollback authority.

## Validation and interpretation

For a documentation-only change to this file:

- validate metadata and local links using the repository's current documentation checks;
- run the current People/DNA/Land synthetic profiles when the repository workflow selects the lane;
- classify hosted and local outcomes as `PASS`, `FAIL`, `SKIPPED`, `NOT_RUN`, `PENDING`, `INHERITED`, or `EXTERNAL`; and
- keep specialist and independent human review pending.

A green workflow proves document and fixture conformance at one revision. It does not prove operational rollback, real revocation or cleanup, policy activation, evidence closure, legal sufficiency, title, sovereignty, release readiness, deployment, or publication safety.

## Documentation rollback

Before merge, close the draft and delete only its task branch. After a separately authorized merge, revert the focused documentation commit or apply a separately reviewed forward correction. Reverting this file restores proposal-era text only; it does not reverse consent, source, evidence, lifecycle, release, deployment, or publication state.

## Next dependency-aware review points

1. Preserve promotion and source refresh as separate repository-grounded `HOLD` boundaries; establish any future operational implementation only in its owning authority surfaces.
2. Preserve the rollback drill and validation runbook as repository-grounded documentation and vendor-signal review as a manual repository-visible procedure; no direct child remains a scaffold, but none of these documents creates rollback, monitoring, or response authority.
3. Review any future generic release or rollback work for a real People/DNA/Land consumer before claiming domain readiness.
4. Preserve the current sensitive-domain holds until accountable privacy, consent, Indigenous/Tribal, legal, policy, evidence, release, operations, security, and independent review exist.
