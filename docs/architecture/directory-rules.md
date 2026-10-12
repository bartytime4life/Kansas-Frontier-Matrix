<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/directory-rules
title: Directory Rules Legacy Architecture-Path Compatibility Tombstone
type: architecture-compatibility
version: v2.0-tombstone.1
status: active; read-only; non-authoritative; compatibility
owners: ["@bartytime4life"]
created: 2026-05-18
updated: 2026-08-18
policy_label: public
owning_root: docs/
responsibility: Preserve the legacy architecture-path identity and fragment links while directing every current Directory Rules read and write to the accepted canonical doctrine path.
truth_posture: CONFIRMED accepted decision, canonical identity, prior body identity, and repository compatibility state / NEEDS VERIFICATION consumer closure and external references
canonical_target: docs/doctrine/directory-rules.md
decision_ref: ADR-0029
superseded_body_blob: 18653c00ba193a4afaa3e07a0924452807fb98ef
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_commit: 790ad870a4cd02adaf205666e413c8e26404c68b
  canonical_blob: fd49a0b83e55cef52c1124281f093e263526898d
  canonical_sha256: 44f7e94344cb42b630008eb0bc03a13fcb97dbdfba6f3e56579693a272571e6e
related:
  - ../doctrine/directory-rules.md
  - ../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../control_plane/path_alias_register.yaml
  - ../../contracts/governance/path_alias_register.md
  - ../../schemas/contracts/v1/governance/path_alias_register.schema.json
  - ../../tools/validators/directory_governance/validate_path_alias_register.py
tags: [kfm, directory-rules, compatibility, tombstone, single-write, migration, rollback]
notes:
  - "ADR-0029 makes docs/doctrine/directory-rules.md the single writable human Directory Rules authority."
  - "This file replaces the restored v1.3.1 compatibility body with a bounded read-only tombstone; it does not amend the adopted doctrine."
  - "Legacy fragment anchors are retained to protect repository and unknown external consumers while reference closure remains open."
  - "Physical deletion remains HOLD until zero-writer, zero-consumer, link-closure, and retirement-receipt evidence exists."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>
<a id="directory-rules"></a>
<a id="-contents"></a>
<a id="contents"></a>

# Directory Rules — Legacy Architecture-Path Compatibility Tombstone

> **Canonical Directory Rules:** [`docs/doctrine/directory-rules.md`](../doctrine/directory-rules.md)  
> **Accepted decision:** [`ADR-0029`](../adr/ADR-0029-adopt-directory-governance-standard-v2.md)

> [!IMPORTANT]
> This path is a **read-only compatibility tombstone**. It is not a second Directory Rules body. All current interpretation, citation, authoring, amendment, and review must use the canonical doctrine path. New content must not be added here except bounded compatibility, correction, or retirement metadata.

## Tombstone status

| Field | Current state |
|---|---|
| Legacy path | `docs/architecture/directory-rules.md` |
| Canonical target | `docs/doctrine/directory-rules.md` |
| Canonical identity | `kfm://doctrine/directory-governance/v2` |
| Canonical SHA-256 | `sha256:44f7e94344cb42b630008eb0bc03a13fcb97dbdfba6f3e56579693a272571e6e` |
| Accepted authority | `ADR-0029` |
| Prior full-body Git blob | `18653c00ba193a4afaa3e07a0924452807fb98ef` |
| Prior full-body snapshot | [`main@790ad870a4cd02adaf205666e413c8e26404c68b`](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/790ad870a4cd02adaf205666e413c8e26404c68b/docs/architecture/directory-rules.md) |
| Alias writers | None |
| Canonical write rule | `canonical_only` |
| Read rule | `canonical_only_with_redirect` |
| Consumer closure | `OPEN` |
| Verification state | `PARTIAL` |
| Physical deletion | `HOLD` |

The accepted doctrine bytes retain an internal `PROPOSED_FOR_ADOPTION` label because ADR-0029 adopted the exact pinned artifact without rewriting it. The accepted ADR, canonical digest, and canonical path determine current authority.

## What this tombstone does

- Preserves the legacy path and prior document identities `kfm://doc/directory-rules` and `kfm://doc/doctrine/directory-rules`.
- Preserves legacy fragments so existing repository and unknown external links resolve safely.
- Directs readers to the accepted canonical doctrine instead of maintaining duplicate rules.
- Keeps the pre-tombstone body recoverable through Git history and the alias register's rollback reference.
- Makes single-write behavior visible: the architecture alias has no writers; the doctrine path is the only human-authoritative write surface.

## What this tombstone does not do

- It does not change the accepted Directory Rules bytes, digest, document ID, or decision.
- It does not accept another ADR or make a proposed ADR effective.
- It does not close repository or external consumers.
- It does not authorize physical deletion, root migration, lifecycle movement, release, deployment, or publication.
- It does not convert the path-alias register, validator success, workflow success, or this pull request into authority.

## Current use

For any current placement question:

1. Read the [accepted canonical Directory Rules](../doctrine/directory-rules.md).
2. Apply accepted ADRs within their stated scope.
3. Verify the current repository, adjacent README contracts, machine projections, validators, and tests before claiming implementation.
4. Use finite placement outcomes such as `PLACE`, `SPLIT`, `MIGRATE`, `MIRROR`, `HOLD`, or `DENY`.
5. Keep corrections and rollback explicit.

When an old link lands here, use the compatibility map below. Do not quote the retired v1.3.1 body as current doctrine.

## Legacy top-level fragment compatibility

<a id="0-status--authority"></a>
- Legacy fragment `#0-status--authority` → [Status, scope, non-effects, and authority boundary](../doctrine/directory-rules.md#1-status-scope-and-non-effects).
<a id="1-purpose"></a>
- Legacy fragment `#1-purpose` → [Purpose and governed scope](../doctrine/directory-rules.md#1-status-scope-and-non-effects).
<a id="2-authority-conformance-and-conflict-resolution"></a>
- Legacy fragment `#2-authority-conformance-and-conflict-resolution` → [Authority order, conflicts, and amendment classes](../doctrine/directory-rules.md#2-authority-model).
<a id="3-the-deeper-rule"></a>
- Legacy fragment `#3-the-deeper-rule` → [Responsibility signature and authority ownership](../doctrine/directory-rules.md#4-the-responsibility-signature).
<a id="4-where-does-this-file-go--placement-protocol"></a>
- Legacy fragment `#4-where-does-this-file-go--placement-protocol` → [Deterministic placement protocol](../doctrine/directory-rules.md#5-deterministic-placement-protocol).
<a id="5-canonical-root-tree"></a>
- Legacy fragment `#5-canonical-root-tree` → [Canonical root registry](../doctrine/directory-rules.md#7-canonical-root-registry).
<a id="6-governance-and-authority-roots"></a>
- Legacy fragment `#6-governance-and-authority-roots` → [Governance and authority roots](../doctrine/directory-rules.md#9-governance-and-authority-roots).
<a id="7-implementation-roots"></a>
- Legacy fragment `#7-implementation-roots` → [Implementation and operations roots](../doctrine/directory-rules.md#10-implementation-and-operations-roots).
<a id="8-compatibility-roots"></a>
- Legacy fragment `#8-compatibility-roots` → [Compatibility, aliases, and deprecation](../doctrine/directory-rules.md#17-compatibility-aliases-and-deprecation).
<a id="9-data-and-release-roots"></a>
- Legacy fragment `#9-data-and-release-roots` → [Data, evidence, and release placement](../doctrine/directory-rules.md#11-data-evidence-and-release-placement).
<a id="10-runtime-infrastructure-and-configuration-roots"></a>
- Legacy fragment `#10-runtime-infrastructure-and-configuration-roots` → [Runtime, infrastructure, and configuration](../doctrine/directory-rules.md#10-implementation-and-operations-roots).
<a id="11-ui-and-map-roots"></a>
- Legacy fragment `#11-ui-and-map-roots` → [Application and reusable implementation placement](../doctrine/directory-rules.md#10-implementation-and-operations-roots).
<a id="12-domain-placement-law"></a>
- Legacy fragment `#12-domain-placement-law` → [Domain, source, geography, and cross-domain scope](../doctrine/directory-rules.md#12-domain-source-geography-and-cross-domain-scope).
<a id="13-anti-patterns-and-drift-prevention"></a>
- Legacy fragment `#13-anti-patterns-and-drift-prevention` → [Naming, identity, drift, and collection grammar](../doctrine/directory-rules.md#13-names-identity-and-collection-grammar).
<a id="14-migration-discipline"></a>
- Legacy fragment `#14-migration-discipline` → [Migration, correction, and rollback](../doctrine/directory-rules.md#18-migration-correction-and-rollback).
<a id="15-required-readme-contract"></a>
- Legacy fragment `#15-required-readme-contract` → [README contracts and documentation inheritance](../doctrine/directory-rules.md#16-readme-contracts-and-documentation-inheritance).
<a id="16-path-validation-checklist-for-reviewers"></a>
- Legacy fragment `#16-path-validation-checklist-for-reviewers` → [Reviewer checklist](../doctrine/directory-rules.md#22-reviewer-checklist).
<a id="17-document-change-discipline"></a>
- Legacy fragment `#17-document-change-discipline` → [Authority freeze and amendment classes](../doctrine/directory-rules.md#2-authority-model).
<a id="18-open-questions-and-needs-verification"></a>
- Legacy fragment `#18-open-questions-and-needs-verification` → [Current convergence and open implementation work](../doctrine/directory-rules.md#20-current-repository-convergence-map).
<a id="19-glossary"></a>
- Legacy fragment `#19-glossary` → [Glossary](../doctrine/directory-rules.md#23-glossary).
<a id="20-practical-final-recommendation"></a>
- Legacy fragment `#20-practical-final-recommendation` → [Deterministic placement protocol](../doctrine/directory-rules.md#5-deterministic-placement-protocol).
<a id="21-changelog"></a>
- Legacy fragment `#21-changelog` → Historical edition lineage is preserved in ADR-0029 and Git history.

## Legacy subsection fragment compatibility

<a id="31-responsibility-roots--visual-overview"></a>
- Legacy fragment `#31-responsibility-roots--visual-overview` → [Responsibility signature](../doctrine/directory-rules.md#4-the-responsibility-signature).
<a id="41-placement-protocol--flow"></a>
- Legacy fragment `#41-placement-protocol--flow` → [Placement protocol](../doctrine/directory-rules.md#5-deterministic-placement-protocol).
<a id="61-docs--the-human-facing-control-plane"></a>
- Legacy fragment `#61-docs--the-human-facing-control-plane` → [Documentation and governance roots](../doctrine/directory-rules.md#9-governance-and-authority-roots).
<a id="61a-docsstandards-placement-contract-v11"></a>
- Legacy fragment `#61a-docsstandards-placement-contract-v11` → [Documentation responsibility](../doctrine/directory-rules.md#9-governance-and-authority-roots).
<a id="61b-docsrunbooks-placement-contract-v11-needs-verification"></a>
- Legacy fragment `#61b-docsrunbooks-placement-contract-v11-needs-verification` → [Runbook placement responsibility](../doctrine/directory-rules.md#9-governance-and-authority-roots).
<a id="62-control_plane--machine-readable-governance-maps"></a>
- Legacy fragment `#62-control_plane--machine-readable-governance-maps` → [Machine governance projections](../doctrine/directory-rules.md#9-governance-and-authority-roots).
<a id="63-contracts--object-meaning"></a>
- Legacy fragment `#63-contracts--object-meaning` → [Semantic contract authority](../doctrine/directory-rules.md#9-governance-and-authority-roots).
<a id="64-schemas--machine-checkable-shape"></a>
- Legacy fragment `#64-schemas--machine-checkable-shape` → [Machine-shape authority](../doctrine/directory-rules.md#9-governance-and-authority-roots).
<a id="65-policy--admissibility-and-release"></a>
- Legacy fragment `#65-policy--admissibility-and-release` → [Policy authority](../doctrine/directory-rules.md#9-governance-and-authority-roots).
<a id="66-tests-and-fixtures"></a>
- Legacy fragment `#66-tests-and-fixtures` → [Tests and fixture placement](../doctrine/directory-rules.md#10-implementation-and-operations-roots).
<a id="67-focus-modes--proof-slice-placement-contract-v12"></a>
- Legacy fragment `#67-focus-modes--proof-slice-placement-contract-v12` → [Focus-scope placement](../doctrine/directory-rules.md#12-domain-source-geography-and-cross-domain-scope).
<a id="71-apps--deployable-applications"></a>
- Legacy fragment `#71-apps--deployable-applications` → [Deployable applications](../doctrine/directory-rules.md#10-implementation-and-operations-roots).
<a id="72-packages--shared-libraries"></a>
- Legacy fragment `#72-packages--shared-libraries` → [Reusable libraries](../doctrine/directory-rules.md#10-implementation-and-operations-roots).
<a id="73-connectors--source-specific-fetch-and-admission"></a>
- Legacy fragment `#73-connectors--source-specific-fetch-and-admission` → [Source connectors](../doctrine/directory-rules.md#10-implementation-and-operations-roots).
<a id="74-pipelines-and-pipeline_specs"></a>
- Legacy fragment `#74-pipelines-and-pipeline_specs` → [Pipelines and declarative specifications](../doctrine/directory-rules.md#10-implementation-and-operations-roots).
<a id="75-tools-and-scripts"></a>
- Legacy fragment `#75-tools-and-scripts` → [Repository tools and thin scripts](../doctrine/directory-rules.md#10-implementation-and-operations-roots).
<a id="75a-toolsvalidatorsvalidate_allpy--canonical-orchestrator-pattern-v11-reconciled-v12"></a>
- Legacy fragment `#75a-toolsvalidatorsvalidate_allpy--canonical-orchestrator-pattern-v11-reconciled-v12` → [Machine enforcement](../doctrine/directory-rules.md#19-machine-enforcement).
<a id="81-common-compatibility-roots-and-their-canonical-homes"></a>
- Legacy fragment `#81-common-compatibility-roots-and-their-canonical-homes` → [Compatibility classes](../doctrine/directory-rules.md#17-compatibility-aliases-and-deprecation).
<a id="82-the-artifacts-rule"></a>
- Legacy fragment `#82-the-artifacts-rule` → [Generated output and caches](../doctrine/directory-rules.md#15-generated-output-external-storage-and-caches).
<a id="83-compatibility-roots-are-not-parallel-authority"></a>
- Legacy fragment `#83-compatibility-roots-are-not-parallel-authority` → [Single-write compatibility](../doctrine/directory-rules.md#17-compatibility-aliases-and-deprecation).
<a id="91-data--the-lifecycle-invariant"></a>
- Legacy fragment `#91-data--the-lifecycle-invariant` → [Lifecycle data placement](../doctrine/directory-rules.md#11-data-evidence-and-release-placement).
<a id="92-release--release-decisions"></a>
- Legacy fragment `#92-release--release-decisions` → [Release-decision placement](../doctrine/directory-rules.md#11-data-evidence-and-release-placement).
<a id="101-runtime"></a>
- Legacy fragment `#101-runtime` → [Runtime implementation](../doctrine/directory-rules.md#10-implementation-and-operations-roots).
<a id="102-infra"></a>
- Legacy fragment `#102-infra` → [Infrastructure](../doctrine/directory-rules.md#10-implementation-and-operations-roots).
<a id="103-configs"></a>
- Legacy fragment `#103-configs` → [Configuration](../doctrine/directory-rules.md#10-implementation-and-operations-roots).
<a id="104-migrations"></a>
- Legacy fragment `#104-migrations` → [Migration records](../doctrine/directory-rules.md#18-migration-correction-and-rollback).
<a id="131-contracts-and-schemas-both-claiming-the-same-authority"></a>
- Legacy fragment `#131-contracts-and-schemas-both-claiming-the-same-authority` → [Authority-root separation](../doctrine/directory-rules.md#9-governance-and-authority-roots).
<a id="132-artifacts-dataproofs-datareceipts-and-release-mixing-proof-process-memory-build-output-and-release-decisions"></a>
- Legacy fragment `#132-artifacts-dataproofs-datareceipts-and-release-mixing-proof-process-memory-build-output-and-release-decisions` → [Data, proof, receipt, and release separation](../doctrine/directory-rules.md#11-data-evidence-and-release-placement).
<a id="133-ui-web-appsexplorer-web-and-packagesui-becoming-competing-shell-homes"></a>
- Legacy fragment `#133-ui-web-appsexplorer-web-and-packagesui-becoming-competing-shell-homes` → [Application/library separation](../doctrine/directory-rules.md#10-implementation-and-operations-roots).
<a id="134-domain-folders-becoming-root-folders-and-fragmenting-the-lifecycle"></a>
- Legacy fragment `#134-domain-folders-becoming-root-folders-and-fragmenting-the-lifecycle` → [Domain-as-lane placement](../doctrine/directory-rules.md#12-domain-source-geography-and-cross-domain-scope).
<a id="135-additional-anti-patterns"></a>
- Legacy fragment `#135-additional-anti-patterns` → [Drift prevention](../doctrine/directory-rules.md#13-names-identity-and-collection-grammar).
<a id="141-for-routine-moves-one-or-a-few-files-within-a-lane"></a>
- Legacy fragment `#141-for-routine-moves-one-or-a-few-files-within-a-lane` → [Routine correction and migration](../doctrine/directory-rules.md#18-migration-correction-and-rollback).
<a id="142-for-structural-moves-changing-a-root-splitting-a-phase-schema-home-migration"></a>
- Legacy fragment `#142-for-structural-moves-changing-a-root-splitting-a-phase-schema-home-migration` → [Structural migration](../doctrine/directory-rules.md#18-migration-correction-and-rollback).
<a id="143-for-renames-that-change-object-identity"></a>
- Legacy fragment `#143-for-renames-that-change-object-identity` → [Identity-changing migration](../doctrine/directory-rules.md#18-migration-correction-and-rollback).
<a id="18a-carried-forward-from-v10"></a>
- Legacy fragment `#18a-carried-forward-from-v10` → [Current convergence map](../doctrine/directory-rules.md#20-current-repository-convergence-map).
<a id="18b-new-in-v11"></a>
- Legacy fragment `#18b-new-in-v11` → [Current convergence map](../doctrine/directory-rules.md#20-current-repository-convergence-map).
<a id="18c-adr-backlog-cross-reference"></a>
- Legacy fragment `#18c-adr-backlog-cross-reference` → [Adoption and implementation sequence](../doctrine/directory-rules.md#21-adoption-and-implementation-sequence).
<a id="18d-new-in-v12"></a>
- Legacy fragment `#18d-new-in-v12` → [Current convergence map](../doctrine/directory-rules.md#20-current-repository-convergence-map).
<a id="18e-new-in-v13"></a>
- Legacy fragment `#18e-new-in-v13` → [Current convergence map](../doctrine/directory-rules.md#20-current-repository-convergence-map).
<a id="18f-new-in-v131"></a>
- Legacy fragment `#18f-new-in-v131` → [Compatibility migration](../doctrine/directory-rules.md#17-compatibility-aliases-and-deprecation).
<a id="v131--2026-05-25-placement-refresh-no-doctrinal-content-change"></a>
- Legacy fragment `#v131--2026-05-25-placement-refresh-no-doctrinal-content-change` → Historical edition lineage is preserved in ADR-0029 and Git history.

## Correction, rollback, and retirement

A correction may update this tombstone only to repair a redirect, preserve a verified legacy fragment, clarify non-authority, or record reviewed migration evidence. Any edit that adds placement law, changes the canonical identity, creates an alias writer, weakens `canonical_only`, or implies consumer closure is denied.

Rollback is to restore the prior full body only through a reviewed revert or forward fix that cannot recreate two writable authorities. The prior body is pinned as Git blob `18653c00ba193a4afaa3e07a0924452807fb98ef`. After rollback or correction, rerun path-alias schema, repository parity, metadata, link, document-graph, topology, and workflow-security checks.

Physical deletion remains held until the accepted exit conditions are proved: zero writers, zero consumers, link and identity parity, and a retirement receipt. Unknown external consumers remain `NEEDS VERIFICATION`.

## Related evidence

- [Accepted Directory Rules](../doctrine/directory-rules.md)
- [ADR-0029 adoption and migration plan](../adr/ADR-0029-adopt-directory-governance-standard-v2.md)
- [Path Alias Register projection](../../control_plane/path_alias_register.yaml)
- [Path Alias Register semantic contract](../../contracts/governance/path_alias_register.md)
- [Path Alias Register schema](../../schemas/contracts/v1/governance/path_alias_register.schema.json)
- [Path Alias Register validator](../../tools/validators/directory_governance/validate_path_alias_register.py)

---

**Compatibility rule:** read canonically, write canonically, preserve the alias until verified retirement, and never let a redirect become parallel authority.

[Back to top](#top)
