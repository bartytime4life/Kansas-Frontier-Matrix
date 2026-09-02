<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contracts/focus/readme
title: contracts/focus — Focus Contract Routing Hold
type: README; child-lane contract; compatibility-boundary; path-status record
version: v1.0.0
status: repository-grounded; routing-hold; no local semantic payload; non-canonical pending path decision
owners: NEEDS VERIFICATION — contract, governed-AI, runtime, evidence, policy, UI, and release stewards
updated: 2026-08-29
supersedes: two-line semantic-family stub at the same path; no contract, schema, policy, runtime, release, or publication state
policy_label: internal-navigation; no-parallel-authority; fail-closed; non-publisher
current_path: contracts/focus/README.md
owning_root: contracts/
truth_posture: >
  CONFIRMED path, prior blob, README-only local tree, sibling Focus contract
  families, proposed Focus ADRs, and no literal repository reference to this
  path at the reviewed base / UNKNOWN intended alias, owner, consumers, and
  migration / DENY canonical, implemented, released, or public interpretation
  from the path name
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_commit: 2b0ea9bbbc9d9a120ea94d92fb4617d96fe7d2a0
  prior_blob: b93ff1f4d5f374b5770ab24a59a38a44ef67355a
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  method: complete target read; parent, sibling contracts, schemas, policy, workflow, Explorer, ADR, tree, and literal-reference inspection
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `contracts/focus/` — Focus Contract Routing Hold

This directory is an unresolved Focus contract path. It contains no semantic
contract other than this README and must not be treated as the canonical Focus
Mode family, a compatibility alias, or a writable aggregation point until a
reviewed path decision establishes that role.

> [!IMPORTANT]
> Current Focus semantics are distributed across object-specific contract
> families. Do not copy them into this directory or infer that the shortest path
> outranks those documents.

## Current repository status

At `main@2b0ea9bbbc9d9a120ea94d92fb4617d96fe7d2a0`:

| Observation | Bounded conclusion |
|---|---|
| Local tree | `contracts/focus/` contains only this README. |
| Prior content | The prior 59-byte file said only that this path held semantic meaning for the Focus family. |
| Parent classification | [`contracts/README.md`](../README.md) lists both `focus/` and `focus_mode/` and leaves alias status to local evidence. |
| Literal references | Repository code search returned no reference to `contracts/focus`. |
| Path decision | No accepted ADR selecting this path as canonical, alias, or retired was identified. |
| Focus ADR posture | ADR-0027, ADR-0028, and the Focus model-adapter boundary remain proposed. |
| Local writer or consumer | **UNKNOWN.** No binding was established by the inspected evidence. |

These observations are exact-repository evidence, not proof that dynamically
constructed paths or external systems do not exist.

## Authority and path boundary

Accepted [Directory Rules](../../docs/doctrine/directory-rules.md) place human
semantic meaning under `contracts/`, machine shape under `schemas/`, and
admissibility under `policy/`. That responsibility split does not choose
between competing child names inside the contract root.

Until path authority is resolved, this directory is a **routing hold**:

- it may explain the conflict and route maintainers to current object-specific
  documents;
- it does not define Focus request, response, payload, runtime, evidence,
  policy, UI, or release semantics;
- it must not mirror sibling contracts, schemas, fixtures, policy modules, or
  application code;
- it must not become a second writable Focus semantic authority by convention;
- it grants no source, model, runtime, review, release, deployment, promotion,
  or publication authority.

## Current semantic routing map

Use the narrowest existing document for the object being changed. Presence in
this table records repository location and stated scope; it does not resolve
which family should become canonical.

| Concern | Current semantic document | Repository-grounded posture |
|---|---|---|
| Focus payload projection | [`contracts/focus_mode/`](../focus_mode/README.md) and its [payload contract](../focus_mode/focus_mode_payload.md) | Draft payload-side semantics for a downstream governed carrier. |
| Governed-AI request | [`contracts/ai/focus_mode_request/`](../ai/focus_mode_request/README.md) | Draft, proposed path; its README explicitly leaves the canonical home unresolved. |
| Governed-AI response | [`contracts/ai/focus_mode_response/`](../ai/focus_mode_response/README.md) | Draft, proposed path; its README explicitly leaves the canonical home unresolved. |
| UI request projection | [`contracts/ui/focus_request.md`](../ui/focus_request.md) | Draft UI-specific request meaning; paired schema remains a scaffold. |
| UI response projection | [`contracts/ui/focus_response.md`](../ui/focus_response.md) | Draft UI-specific response meaning; runtime envelope authority remains separate. |
| Runtime envelope semantics | [`contracts/runtime/`](../runtime/README.md) | Owns runtime result meaning; not a Focus-path alias. |
| Evidence semantics | [`contracts/evidence/`](../evidence/README.md) | Owns evidence references and bundles that support consequential claims. |
| Machine shape | [`schemas/contracts/v1/focus/`](../../schemas/contracts/v1/focus/README.md) and object-specific schema families | Mixed proposed scaffolds and compatibility paths with documented overlap. |
| Admissibility | [`policy/focus/`](../../policy/focus/README.md) | Repository-grounded but inactive policy boundary; evaluator remains unbound. |
| Explorer projection | [Focus Panel feature](../../apps/explorer-web/src/features/focus_panel/README.md) | Bounded fixture-first consumer implementation; not contract-path authority. |

## Current executable evidence and limits

The [`focus-mock-test` workflow](../../.github/workflows/focus-mock-test.yml)
preserves deterministic finite-envelope and fixture-selection proof while
reporting the mock Focus runtime as held. It does not validate or consume this
directory.

The current evidence supports only these bounded conclusions:

- finite `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` envelope behavior has
  executable synthetic coverage;
- Focus schema families exist, but the `schemas/contracts/v1/focus/` index
  records permissive scaffolds and request/response overlap with UI schemas;
- Focus policy source exists, but its README records an inactive,
  evaluator-unbound boundary;
- the Explorer Focus Panel has bounded fixture-first implementation and tests;
- none of those facts chooses `contracts/focus/` as a semantic authority or
  proves a live model provider, governed production runtime, release, or public
  operation.

A workflow pass proves only its declared checks. A contract, schema, fixture,
test, application, receipt, pull request, or merge does not independently make
an answer true, admissible, reviewed, released, deployed, promoted, or
published.

## Change rules while the hold is open

Before adding any semantic contract beneath this directory, establish:

1. the exact object family and responsibility that is missing;
2. why no current Focus contract owns that meaning;
3. the accepted canonical path and stable identity;
4. every sibling, schema, policy, fixture, validator, workflow, application,
   documentation, and external consumer affected;
5. compatibility, redirect, deprecation, and link-preservation behavior;
6. migration validation and a reversible rollback target;
7. accountable stewardship and independent review.

If those facts are unresolved, update the existing object-specific document or
leave the proposal on hold. Do not create a broad `focus/` copy as a shortcut.

## Validation and review

For a future path-resolution change, verify at minimum:

- one semantic authority per Focus object family;
- contract-to-schema and policy links resolve without circular or parallel
  authority;
- request, response, payload, runtime envelope, evidence, and UI projection
  meanings remain distinct;
- old links and consumers have an explicit compatibility disposition;
- finite negative outcomes and citation/evidence requirements remain
  fail-closed;
- sensitive, withheld, corrected, withdrawn, and stale information cannot be
  exposed through a new alias;
- rollback restores navigation and consumer behavior without restoring
  contradictory authority.

No path consolidation, migration, or alias behavior is performed by this
README.

## Maintenance guidance

- Re-run the direct-child and literal-reference inventory when this directory
  gains a file or consumer.
- Update the routing table when a listed contract changes status or scope.
- Replace the routing hold only through the reviewed path decision that also
  addresses sibling consumers and rollback.
- Correct factual errors in place; do not duplicate the README under another
  path as a competing status record.

## Open verification register

| Question | Status |
|---|---|
| Intended role of `contracts/focus/` | `UNKNOWN` |
| Canonical Focus request, response, payload, and UI projection homes | `NEEDS VERIFICATION` |
| Relationship between `focus/` and `focus_mode/` | `UNRESOLVED PATH DRIFT` |
| Accountable contract owner and independent reviewer | `NEEDS VERIFICATION` |
| Complete internal and external consumer inventory | `UNKNOWN` |
| Migration, compatibility, deprecation, and rollback plan | `NOT ESTABLISHED` |
| Production model/runtime, release, and public serving | `NOT PROVED` |

## Related documentation

- [Contracts root authority](../README.md)
- [Focus Mode payload contract](../focus_mode/focus_mode_payload.md)
- [Focus schema-family overlap register](../../schemas/contracts/v1/focus/README.md)
- [Focus policy boundary](../../policy/focus/README.md)
- [Governed AI Focus Flow](../../docs/architecture/governed-ai/FOCUS_FLOW.md)
- [Proposed county Focus control-plane ADR](../../docs/adr/ADR-0027-county-focus-mode-control-plane.md)
- [Proposed Focus model-adapter ADR](../../docs/adr/ADR-focus-model-adapter-boundary.md)
- [Directory Rules](../../docs/doctrine/directory-rules.md)

[Back to top](#top)
