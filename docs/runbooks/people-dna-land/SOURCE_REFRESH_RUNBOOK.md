<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook/people-dna-land/source-refresh
title: People · Genealogy · DNA · Land — Source Refresh Runbook
type: standard
version: v1.1.1
prior_version: v1.1.0
prior_state: repository-grounded source-refresh HOLD boundary whose next-review inventory still counted the rollback drill, validation runbook, and vendor watch as scaffolds
status: draft; repository-grounded hold boundary; source-head review only; live retrieval and source mutation unavailable; non-release; non-publication
owners:
  - "@bartytime4life — verified GitHub review route"
  - "NEEDS VERIFICATION — accountable People/DNA/Land, privacy, consent, Indigenous/Tribal, legal, source, rights, data-custody, policy, security, evidence, operations, release, and independent-review assignments"
created: 2026-05-12
updated: 2026-08-29
policy_label: repository-facing; sensitive-domain; source-refresh-held; fail-closed; no-network; non-release; non-publication
current_path: docs/runbooks/people-dna-land/SOURCE_REFRESH_RUNBOOK.md
owning_root: docs/
responsibility: Explain the current People/DNA/Land source-refresh hold, permit only repository-visible source-head review and minimized handoff, and prevent proposal-era fetch, admission, receipt, lifecycle, and watcher instructions from being executed as current authority.
truth_posture: cite-or-abstain
authority_class: explanatory source-refresh hold and proposal-lineage disposition
authority_rank: subordinate to accepted doctrine and ADRs, source registry and activation authority, contracts, schemas, policy, consent, rights, evidence, accountable review, lifecycle, receipts, release, correction, withdrawal, revocation, and rollback authorities
canonical_relationship: same-path replacement of proposal-era instructions; prior detail remains in Git history and is not current operational authority
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: a3d66df629a3b18f01821761898879d7d4996a2f
  current_reconciliation_commit: 4e714b639861e340b0c35a5360f9ffaecdf1f53c
  prior_blob: 4c8eeaf660dbd416371a1a4f58838d43fddc50e3
  lane_readme_prior_blob: 1ba3f28deaaea1fc9811ee1eb58e59558c2ecd84
  rollback_drill_blob: 9088cbff694297613882bfae86b259f93023ff03
  validation_runbook_blob: c1987d5f3b4a0419fa9aa970a71d7cef9d1c341e
  vendor_watch_prior_blob: 84d77e7e9a9d4afb2ee367ff11841a837bdf1a8c
  source_registry_readme_blob: 98a90286e6b3d7ad49a64158be666e34ba6c1720
  connector_readme_blob: 2ab7b6677b077adba7406a42f56c1efead76dd51
  policy_readme_blob: 7260394c77d79629895da16d8d680e8d80c56b32
  contract_readme_blob: d99e7fc318f34fbeb90a1ee31658f5121b8ffd38
  schema_readme_blob: fbe5557ff4e19d1b70a97d284ab1743dd3d08f29
  fixtures_readme_blob: 8eb10804c587c62edf1eb9750c2c82b5cf237f2a
  tests_readme_blob: 77bb1bfd3d3e576bc975c91bbe46dd3e6d8fee52
  validator_readme_blob: 7a78d278aa03d843107d4d66a954c7a670d2ac19
  domain_workflow_blob: bcf64c3e3b6653b9543489fc5a6031805ae3ef48
  release_candidate_readme_blob: cbbef9394fbdbe94ed742957e1b764c84c9907f3
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
related:
  - docs/runbooks/people-dna-land/README.md
  - docs/runbooks/people-dna-land/PROMOTION_RUNBOOK.md
  - docs/runbooks/people-dna-land/ROLLBACK_RUNBOOK.md
  - docs/runbooks/people-dna-land/ROLLBACK_DRILL.md
  - docs/runbooks/people-dna-land/VALIDATION_RUNBOOK.md
  - docs/runbooks/people-dna-land/VENDOR_WATCH_SOP.md
  - docs/doctrine/directory-rules.md
  - docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - docs/domains/people-dna-land/README.md
  - data/registry/sources/people-dna-land/README.md
  - connectors/people-dna-land/README.md
  - policy/domains/people-dna-land/README.md
  - contracts/domains/people-dna-land/README.md
  - schemas/contracts/v1/domains/people-dna-land/README.md
  - fixtures/domains/people-dna-land/README.md
  - tests/domains/people-dna-land/README.md
  - tools/validators/domains/people-dna-land/README.md
  - release/candidates/people-dna-land/README.md
  - .github/workflows/domain-people-dna-land.yml
tags: [kfm, runbook, people-dna-land, source-refresh, source-head, hold, no-network, sensitive-domain, proposal-lineage, fail-closed]
notes:
  - "The prior 2026-05-12 body is retired from operational use because current evidence does not establish an admitted descriptor, active connector, source-refresh profile, receipt producer, policy-runtime binding, or lifecycle mutation path."
  - "This file authorizes no network request, credential use, source retrieval, descriptor edit, source activation, payload placement, receipt emission, lifecycle mutation, watcher PR, promotion, release, deployment, or publication."
  - "Repository-visible review is limited to synthetic or public-safe metadata already admitted to Git; real source or sensitive payloads remain outside Git and CI."
  - "v1.1.1 corrects only the sibling-document inventory: the rollback drill and validation runbook are repository-grounded documentation, and vendor-signal review is manual and repository-visible; none creates live refresh or monitoring authority."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# People · Genealogy · DNA · Land — Source Refresh Runbook

> [!CAUTION]
> **STOP — live People/DNA/Land source refresh is not established by current repository evidence.** Do not execute the prior `curl`, hashing, policy, attestation, quarantine, RAW-placement, or watcher instructions from this path. Their proposal lineage remains in Git history only.

This document is the current repository-grounded hold boundary for People/DNA/Land source refresh. It permits an authorized reviewer to inspect repository-visible source-head metadata and prepare a minimized handoff. It is not a fetcher, source admission decision, connector, policy evaluator, receipt producer, lifecycle transition, incident procedure, release gate, or publication authority.

## Current outcome

| Question | Current answer | Required posture |
|---|---|---|
| Is a live People/DNA/Land refresh implementation verified? | No. The connector lane contains documentation and a placeholder only. | `HOLD` |
| Is a source admitted and activated for this procedure? | No admitted descriptor instance or activation decision is present in the inspected registry lane. | `HOLD` |
| Can this document contact an upstream publisher or use credentials? | No. Network access and credentials are outside this documentation boundary. | `DENY` implied authority |
| Can it place bytes in RAW or QUARANTINE? | No current connector, custody route, or receipt binding was verified. | `HOLD` |
| Can existing synthetic tests authorize refresh? | No. They cover two consent profiles, not source retrieval or admission. | `DENY` implied authority |
| What may happen now? | Review already repository-visible source-head metadata, record gaps, and prepare a minimized handoff without sensitive values. | `PASS` or `HOLD` for that review only |

## Authority and current evidence

- Accepted [ADR-0029](../../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts the [Directory Rules](../../doctrine/directory-rules.md). They place human procedure under `docs/runbooks/`; this path cannot create source, contract, schema, policy, receipt, evidence, lifecycle, or release authority.
- The [source-registry lane](../../../data/registry/sources/people-dna-land/README.md) is experimental, has `OWNER_TBD`, records unresolved topology, and currently contains README files plus placeholders rather than an admitted descriptor instance.
- The [connector lane](../../../connectors/people-dna-land/README.md) is draft and explicitly says its implementation, descriptors, consent sidecars, policy, fixtures, tests, CI, and release behavior need verification. Its current tree contains no source adapter implementation.
- The [policy lane](../../../policy/domains/people-dna-land/README.md) is a mixed-maturity documentation and rule surface. This runbook does not prove an active evaluator binding for source refresh.
- The [contracts](../../../contracts/domains/people-dna-land/README.md), [schemas](../../../schemas/contracts/v1/domains/people-dna-land/README.md), [fixtures](../../../fixtures/domains/people-dna-land/README.md), and [validator index](../../../tools/validators/domains/people-dna-land/README.md) preserve domain boundaries but do not establish an executable source-refresh profile or receipt producer.
- The [domain tests](../../../tests/domains/people-dna-land/README.md) and [workflow](../../../.github/workflows/domain-people-dna-land.yml) execute two deterministic synthetic consent profiles. Neither performs network access, source admission, payload placement, refresh receipt production, or lifecycle promotion.
- The [release-candidate lane](../../../release/candidates/people-dna-land/README.md), [promotion boundary](./PROMOTION_RUNBOOK.md), and [rollback boundary](./ROLLBACK_RUNBOOK.md) do not supply missing refresh authority.

Documentation and repository checks may confirm this boundary at a revision. They cannot close any missing operational dependency.

## Permitted repository-only review

An authorized reviewer may perform this bounded review only on metadata already present in the repository and safe for repository visibility:

1. pin the exact repository revision and the source-registry, connector, policy, contract, schema, fixture, validator, test, workflow, evidence, receipt, release, correction, withdrawal, revocation, and rollback surfaces consulted;
2. confirm whether one authoritative descriptor, activation decision, source-head record, connector implementation, immutable comparison profile, rights posture, sensitivity posture, consent posture, custody route, and receipt binding exist;
3. inventory named consumers without opening a live endpoint, resolving a credential, or copying payload values;
4. preserve source role and time distinctions, including source time, observation time, retrieval time, record time, transaction time, and publication time;
5. assign a finite review outcome and reason from the table below; and
6. hand off a minimized gap list to the owning responsibility roots.

| Review result | Meaning |
|---|---|
| `PASS` | The repository-only inventory completed at the pinned revision. It says nothing about source freshness or operational readiness. |
| `HOLD` | One or more required authorities, implementations, reviews, or safe handling conditions are missing or unresolved. |
| `ABSTAIN` | Available repository evidence cannot support a conclusion without live, restricted, disputed, or authority-controlled material. |
| `DENY` | The requested action would expose prohibited material, exceed consent or rights, collapse a source role, or treat this document as operational authority. |
| `ERROR` | A named repository dependency is missing, inconsistent, malformed, or cannot be inspected safely. |
| `ESCALATE` | Accountable privacy, consent, sovereignty, legal, source, security, custody, policy, evidence, operations, release, or independent review is required. |

A `PASS` for this review does not activate a source or authorize a refresh. The current live-refresh outcome remains `HOLD`.

## Mandatory stop conditions

Stop without network access or mutation when any of the following applies:

- no accepted, uniquely owned descriptor and activation decision identify the exact source product;
- rights, terms, consent, revocation, purpose, audience, access role, sensitivity, sovereignty, stewardship, retention, deletion, custody, cadence, or source head is unknown or disputed;
- a real living person, family relationship, DNA/genomic value, kit or vendor identifier, private address, exact private location, parcel-owner join, title dispute, burial location, or culturally restricted fact would enter Git, CI, logs, screenshots, fixtures, artifacts, or a public handoff;
- no verified connector, immutable comparison profile, deterministic negative fixtures, validator, receipt producer, or accountable operator exists;
- a proposed path, command, role, schema sketch, receipt-shaped JSON, status badge, test, workflow, or generated summary is the only support for the action;
- the proposed refresh would collapse a relationship hypothesis into kinship, an assessor/tax observation into title, parcel geometry into a legal boundary, or a source record into current truth;
- source admission, retrieval, validation, evidence closure, promotion, release, deployment, publication, correction, withdrawal, revocation, deletion, invalidation, and rollback are being treated as one state.

Unknown or unresolved conditions produce `HOLD`, `ABSTAIN`, `DENY`, or `ESCALATE`, never implied approval.

## Sensitive-domain operating law

- Living-person and DNA/genomic material is restricted or denied by default unless current evidence establishes explicit purpose-, audience-, role-, data-class-, and time-bounded authorization and applicable policy support.
- Relationship assertions and DNA-derived links remain evidence-bound hypotheses. A model, match, cluster, household, surname, graph edge, or narrative does not prove identity or kinship.
- Assessor and tax records are administrative observations, not title truth. Parcel geometry is context, not proof of legal boundary or ownership.
- Indigenous, Tribal, descendant-community, burial, archaeological, sacred-site, cemetery, and culturally restricted material requires sovereignty-aware stewardship. Generalization alone does not authorize exposure.
- Client-side filtering, masking, redaction, pseudonymization, aggregation, or generalized geometry is not access control and does not itself create authorization.
- EvidenceRef must resolve to EvidenceBundle when a claim depends on evidence. Maps, tiles, graphs, indexes, summaries, dashboards, and generated text remain derived carriers.

## Evidence required before future live refresh

A future operational procedure remains blocked until current implementation authority establishes all of the following in existing responsibility roots:

1. one accepted descriptor topology, a unique admitted descriptor for the exact source product, and an authenticated activation decision;
2. current rights, terms, consent, revocation, sensitivity, sovereignty, stewardship, cadence, retention, deletion, custody, and correction posture;
3. a verified source-first connector with credential isolation, allowlisted egress, bounded retrieval, immutable source-head capture, digest verification, retry and error behavior, and quarantine-first handling;
4. accepted contracts and schemas for the source head, material-change decision, finite outcomes, and every receipt or handoff object used;
5. active policy-runtime binding for purpose, audience, role, data class, time, living status, consent, rights, source role, harmful precision, sovereignty, and public-path denial;
6. deterministic, minimized, synthetic, no-network fixtures and negative tests covering changed, unchanged, missing-rights, consent-mismatch, revoked, living-person, DNA, title-role, parcel-boundary, precision, receipt, and publication-denial cases;
7. a verified receipt producer and evidence resolver whose output identities bind the exact inputs, decision, runner, code, policy, and candidate revision;
8. accountable source, privacy, consent, Indigenous/Tribal, legal, security, custody, policy, evidence, operations, release, and independent review as applicable;
9. correction, withdrawal, revocation, deletion, derivative invalidation, cache invalidation, and rollback mechanisms that remain separate and are tested without production or restricted data; and
10. exact-head no-network rehearsal plus hosted validation whose limits are recorded without being mistaken for source freshness, human approval, release, or publication.

Missing any item keeps live refresh at `HOLD`.

## Proposal-lineage disposition

The prior v0.1 body is superseded at this path and retained in Git history. It is not copied to another runbook, connector, contract, schema, policy, registry, receipt, proof, or release directory.

In particular, the prior `curl`, `jq`, `sha256sum`, `conftest`, `kfm-source`, `kfm-attest`, and `kfm-refresh` examples; suggested RAW, QUARANTINE, rights, receipt, and fixture paths; HTTP validator behavior; source-family activation assumptions; watcher PR behavior; receipt fields; reason codes; operator checklist; and rollback claims were not verified as a complete current implementation. Do not reconstruct or execute them from this document.

The sibling promotion and rollback documents are repository-grounded `HOLD` boundaries. They do not fill source-refresh dependencies.

## Validation and interpretation

For a documentation-only change to this file:

- run current repository-native metadata, link, topology, and changed-area documentation checks;
- run the two current synthetic People/DNA/Land consent profiles when the workflow selects this lane;
- classify every result as `PASS`, `FAIL`, `SKIPPED`, `NOT_RUN`, `PENDING`, `INHERITED`, `EXTERNAL`, or `UNKNOWN`; and
- bind every result to the exact tested head.

A green check proves only the named document or synthetic profile at that revision. It does not prove source freshness, source admission, rights, consent validity, policy activation, safe custody, evidence closure, receipt authenticity, operational refresh, lifecycle promotion, release, deployment, publication, correction, withdrawal, revocation, deletion, invalidation, or rollback.

## Documentation rollback

Before merge, close the draft pull request and delete only its task branch. After a separately authorized merge, revert the focused documentation commit or apply a reviewed forward correction.

Reverting this file restores proposal-era prose only. It does not undo or execute source retrieval, source admission, consent, policy, evidence, lifecycle, release, deployment, publication, correction, withdrawal, revocation, deletion, invalidation, or rollback.

## Next dependency-aware review points

1. Resolve source-descriptor topology and ownership before creating a source instance or connector profile.
2. Preserve the rollback drill and validation runbook as repository-grounded documentation, and keep vendor-signal review manual and repository-visible; no direct child remains a scaffold, but none of these documents creates live refresh, monitoring, or response authority.
3. Establish active policy-runtime, receipt, evidence, custody, and accountable-review bindings before designing live source refresh.
4. Keep real, restricted, disputed, or proprietary material outside repository-visible surfaces.
5. Preserve source admission, retrieval, validation, lifecycle promotion, release, deployment, publication, correction, withdrawal, revocation, deletion, invalidation, and rollback as separate states.

[Back to top](#top)
