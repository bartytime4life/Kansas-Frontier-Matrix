<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/correction/supersession-notice
title: contracts/correction/supersession_notice.md — SupersessionNotice Contract
type: contract
version: v0.3
status: draft
owners: OWNER_TBD — Correction steward · Release steward · Governance steward · Contract steward · Schema steward · Policy steward · Docs steward
created: 2026-06-20
updated: 2026-09-07
policy_label: public; contracts; correction; supersession-notice; semantic-contract; first-class-corrections; lineage; rollback-aware
owning_root: contracts/
evidence_snapshot: ec203a9ba11fb83b52245f9523ce36cc1ec6ac66
prior_blob: 22f1fdb4a82063b7e66d0478fcc83cb03a89d68b
related:
  - ./README.md
  - ./correction_notice.md
  - ./correction_impact_assessment.md
  - ./correction_propagation_plan.md
  - ../../schemas/contracts/v1/correction/supersession_notice.schema.json
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md
  - ../../docs/doctrine/corrections-first-class.md
  - ../../docs/architecture/publication/CORRECTION.md
tags: [kfm, contracts, correction, supersession-notice, supersession, rollback, release, lineage, evidence, governance]
notes:
  - "Same-path semantic-document refresh; no schema, validator, policy, runtime, release, or publication change."
  - "CONFIRMED placeholder shape; only id is required. Semantic clarifications remain draft and are not enforced by that schema."
  - "Schema-declared supersession fixtures, validator, and policy/correction path are absent at the pinned snapshot; other correction validators exist."
  - "Public documentation does not classify a notice instance, its references, or its underlying evidence as public-safe."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# SupersessionNotice Contract

> Semantic contract for the named, append-only record that a published KFM
> object has been replaced by a governed successor. A draft notice records
> intent; it does not make the replacement effective or authorize exposure.

**Status: draft. Schema: placeholder. Supersession execution: not established.**

## Quick jumps

[Status](#status) · [Meaning](#meaning) · [Repo fit](#repo-fit) · [Schema pairing](#schema-pairing) · [Accepted uses](#accepted-uses) · [Exclusions](#exclusions) · [Fields](#fields) · [Recommended semantic fields](#recommended-semantic-fields) · [Invariants](#invariants) · [Supersession scenarios](#supersession-scenarios) · [Lifecycle](#lifecycle) · [Validation](#validation) · [No-loss preservation](#no-loss-preservation) · [Evidence basis](#evidence-basis) · [Rollback](#rollback) · [Definition of done](#definition-of-done)

## Status

This revision is grounded in `main@ec203a9ba11fb83b52245f9523ce36cc1ec6ac66`,
inspected on 2026-09-07. The prior document blob is
`22f1fdb4a82063b7e66d0478fcc83cb03a89d68b`.

| Surface | Confirmed evidence at that snapshot | Limit |
| --- | --- | --- |
| This contract | Existing draft semantic document; stable identity and path retained. | Wording is not implementation or approval. |
| Paired schema | Existing greenfield placeholder; only `id` is required. | Does not enforce a replacement relationship or release gates. |
| Declared validator | `tools/validators/correction/validate_supersession_notice.py` is absent from the correction-validator directory. | Absence is scoped to that path, not all correction validation. |
| Declared fixtures | `fixtures/correction/supersession_notice/` returns not found. | No supersession-specific fixture coverage is established here. |
| Declared policy path | `policy/correction/` returns not found. | Does not establish that all correction-related policy is absent. |
| Adjacent contracts | CorrectionNotice, CorrectionImpactAssessment, and CorrectionPropagationPlan documents exist. | Their presence does not prove SupersessionNotice execution or downstream consumption. |

**PROPOSED:** the semantic refinements below, including reference binding,
partial-scope handling, and acceptance cases. **UNKNOWN / NEEDS VERIFICATION:**
complete producer/consumer inventory, operational reference resolution,
supersession-specific enforcement, public API/UI behavior, hosted validation,
and accountable steward review. `OWNER_TBD` is retained rather than inventing
an assignment or treating review routing as completed review.

This document's `public` label describes documentation. It grants no public
access to notice instances, previous releases, successor objects, evidence,
private review records, or sensitive locations.

## Meaning

`SupersessionNotice` records a replacement relationship, its bounded scope,
reason, effective time, and supporting evidence and decisions while retaining
prior history. It answers: what was replaced, what replaces it, why, when,
under whose recorded review and release decision, and what consumers should
see or stop using.

The distinction between intention and fact is essential. A candidate successor,
a higher version number, a newer timestamp, an approved-looking field, or a
successful validation report does not make supersession effective. The
relevant governed release transition must exist and be verified separately.

| Related concept | Distinction |
| --- | --- |
| Correction | Names the broader trust-significant change; a correction can lead to supersession, withdrawal, redaction, or another bounded outcome. |
| Supersession | Replaces a prior published object with an identifiable governed successor for a stated scope. It need not imply that the prior version was erroneous. |
| Withdrawal | Removes or restricts public use; a replacement need not exist. Do not invent a successor to represent withdrawal. |
| Stale or disputed state | Warns or limits reliance pending evidence or review; does not establish a replacement. |
| Rollback | Separately authorized restoration of a suitable earlier target or another safe posture, with auditable lineage. A supersession notice does not execute it. |

Earlier doctrine uses `SupersessionRecord`, `old_release`, `new_release`,
`effective_time`, and `superseded_by`. These are retained as source vocabulary,
not silently adopted aliases or evidence of a second implemented object family.

## Repo fit

**Placement outcome: PLACE, same path.** Accepted
[ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md)
adopts the [Directory Rules](../../docs/doctrine/directory-rules.md).
Section 7.2 assigns semantic meaning to `contracts/`, machine shape to
`schemas/`, admissibility rules to `policy/`, accountability instances to
`data/`, and correction/release decisions to `release/`.

This file remains under the existing `contracts/correction/` responsibility.
It creates no new root, schema home, policy directory, notice-instance store,
release lane, or migration. The generated authoring receipt belongs in the
existing `data/receipts/generated/` lane, not in this contract.

[ADR-0001](../../docs/adr/ADR-0001-schema-home--schemas-contracts-v1-is-canonical.md)
remains **proposed**. Its title is not adoption evidence; the accepted
Directory Rules already establish the default machine-schema route.

The [family README](./README.md) and [CorrectionNotice](./correction_notice.md)
carry older placement and maturity questions about correction/release
contracts. This refresh neither resolves those questions nor treats their
historical inventories as current implementation evidence.

## Schema pairing

The existing pairing is
[supersession_notice.schema.json](../../schemas/contracts/v1/correction/supersession_notice.schema.json),
blob `5ea3ef0895ff8527a3c2a466c654bf53b1431632` at the evidence snapshot.

| Schema entry | Current value or effect |
| --- | --- |
| `$schema` | JSON Schema Draft 2020-12. |
| `$id` | `https://schemas.kfm.local/contracts/v1/correction/supersession_notice.schema.json`. An identifier, not a verified public endpoint. |
| `x-kfm.contract_doc` | `contracts/correction/supersession_notice.md`. |
| `x-kfm.fixtures_root` | `fixtures/correction/supersession_notice/`; declared but absent. |
| `x-kfm.validator` | `tools/validators/correction/validate_supersession_notice.py`; declared but absent. |
| `x-kfm.policy` | `policy/correction/`; declared but absent. |
| `x-kfm.status` | `PROPOSED`. |
| `required` | Exactly `id`. |
| `additionalProperties` | `true`. |

**The schema is unchanged by this revision.** A document containing only
`{"id":""}` satisfies its current shape, as does an arbitrary extra field.
Neither is a semantically complete or admissible supersession notice.
Shape acceptance must never be represented as evidence, review, release,
public-safety, or propagation closure.

## Accepted uses

These are intended semantic uses, not permissions granted to a caller.

| Use | Required boundary |
| --- | --- |
| Draft replacement proposal | Identify unresolved dependencies and remain non-effective until the external gates close. |
| Effective replacement record | Bind the prior object, successor, scope, reason, evidence, review, policy, and release transition. |
| Public-safe lineage summary | Expose only the approved projection and permitted forward references. |
| Map, report, or answer supersession context | Use governed evidence/release resolution; a rendered badge or generated summary is not authority. |

Neither publication of this Markdown file nor acceptance of a schema-valid
instance performs any of these governed transitions.

## Exclusions

The notice references, but does not own, artifact payloads, EvidenceBundles,
ReviewRecords, PolicyDecisions, ReleaseManifests, RollbackCards, or redaction
receipts. It contains no executable policy, arbitrary endpoint instructions,
cache-purge commands, alias writes, rebuild jobs, or UI implementation.

Internal evidence and restricted reasons are not copied into a public summary.
Even a reference, digest, identifier, title, or forward link can disclose
protected information and must be screened for the intended audience.

## Fields

These are the **only declared machine properties** in the current schema:

| Field | Required | What the schema actually checks |
| --- | --- | --- |
| `id` | Yes | String; no non-empty, canonical-identity, or uniqueness constraint. |
| `version` | No | String; no version grammar or ordering constraint. |
| `spec_hash` | No | String; no digest grammar, canonicalization, or recomputation check. |

This revision introduces no wire-format change and no new accepted enum.
A canonicalization method, identity algorithm, or alias set must not be inferred
from this table or from the mere presence of `spec_hash`.

## Recommended semantic fields

**PROPOSED, not implemented by the paired schema.** The following preserve
prior semantic intentions while making the future implementation boundary
explicit. Field spellings and object-reference shapes require a reviewed,
versioned schema/fixture/validator slice before interoperable use.

| Existing source vocabulary or semantic group | Required meaning for a future profile |
| --- | --- |
| `id`, `version`, `spec_hash` | Stable notice identity, revision identity, and a declared digest method. Do not overwrite an effective notice under the same identity. |
| `supersedes`, `old_release`, affected-object references | Unambiguous typed, version-bound predecessor and the affected spatial, temporal, claim, or artifact scope. A mutable `latest` alias alone is insufficient. |
| `superseded_by`, `new_release`, successor references | Resolvable successor and its applicable release/decision binding; predecessor and successor are distinct. These spellings are not interchangeable by default. |
| `reason`, `defect_class` | Evidence-supported reason, distinguishing routine version improvement from error, rights, sensitivity, or policy repair. |
| `effective_time` and recording context | Effective transition time distinct from when the notice was authored, recorded, or observed, and from the underlying data's valid time. |
| `source_refs`, `evidence_refs` | Supporting evidence resolves through EvidenceRef to EvidenceBundle under the caller's policy context. A non-empty string does not prove resolution. |
| `review_state`, policy and release references | Review, policy, release, and notice state stay separate. A claimed state in the notice cannot approve itself. |
| `public_summary` | Audience-safe explanation with permitted history/forward links and explicit limits. |
| `rollback_target` | A separately reviewable recovery target; current policy must still permit restoration. |
| Generated-receipt and propagation references | AI-authorship provenance where applicable, and links to separately owned impact, propagation, and completion records. |

Pending notices must not manufacture an effective time, approved reviewer,
policy result, resolvable successor, or completion receipt to fill a field.
Unknown dependencies remain visible and block the affected later transition,
not safe authoring of the candidate.

## Invariants

The retained doctrinal requirements are named operations, append-only history,
public visibility where safe, a correction/rollback path, cite-or-abstain, and
the governed public boundary. The following are proposed acceptance-level
clarifications of those requirements, not claims of current enforcement.

1. **Preserve history without preserving unsafe access.** Retain predecessor,
   manifest, notice, and decision lineage for authorized audit. Do not silently
   rewrite or delete it. Rights or sensitivity controls may restrict public
   access; auditability is not an exemption from those controls.
2. **Bind scope and identity.** Prevent self-supersession, cycles, unresolved
   references, and competing successors for the same effective scope. Partial
   replacement must not mark an entire dataset or release replaced. Splits and
   merges require an explicit mapping, not a guessed one-to-one relationship.
3. **Separate time and authority.** Effective time is supported by the recorded
   release transition, not inferred from version order or file modification
   time. A future-dated proposal is not already effective. Historical queries
   retain their as-of/version context rather than being silently rewritten.
4. **Keep the trust membrane.** Public clients use governed APIs or released
   artifacts, never RAW, WORK, QUARANTINE, internal stores, or direct models.
   Each proposed successor must pass its own evidence, rights, sensitivity,
   validation, integrity, review, release, and rollback gates.
5. **Treat propagation as separately evidenced work.** A valid notice or plan
   does not prove caches, maps, exports, citations, or other consumers changed.
   Failed or unobserved propagation remains explicit; do not claim global
   completion from one successful consumer.
6. **Keep AI subordinate.** Generated wording cannot decide source authority,
   policy, review, or release state. Preserve authorship receipts and validate
   citations against admissible evidence before a consequential answer.

## Supersession scenarios

| Scenario | Notice and consumer posture |
| --- | --- |
| Source update | Link exact source-derived versions and comparison evidence; make replacement effective only through the release process. |
| Error correction or validation repair | Link the correction and validated successor. A repaired validator alone does not validate all historical artifacts. |
| Rights or sensitivity change | Restrict unsafe exposure through the appropriate authorized process. Record withdrawal when there is no admissible replacement; record supersession only when a permitted successor exists. |
| Redacted or generalized successor | Bind the transform/review evidence without leaking original geometry or restricted reasons in notices, links, or logs. |
| Versioned improvement | Explain what changed without falsely declaring the predecessor defective. |
| Partial replacement | State exactly which features, claims, regions, or time interval changed; preserve unaffected scope. |
| AI-answer correction | Bind the old answer and corrected or explicitly abstaining successor, with evidence/citation revalidation. Do not regenerate prose and call it proof. |
| Missing, conflicting, or failing successor | Hold the replacement claim. Use the separately governed stale, withdrawal, or rollback path as appropriate; never automatically restore an unsafe predecessor. |

## Lifecycle

The data lifecycle remains unchanged:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A proposed supersession sequence is:

```text
Detect a replacement condition -> draft a notice
  -> resolve predecessor, successor, evidence, and affected scope
  -> assess impact and plan propagation
  -> validate; check rights, sensitivity, policy, and accountable review
  -> separately authorize and record the release transition
  -> expose the permitted notice and successor through governed surfaces
  -> verify consumer actions; retain history and recovery evidence
```

This is explanatory sequencing, not an executable state machine or automatic
promotion. A notice file does not repoint an alias. Failed gates preserve a
non-effective proposal; containment of an already unsafe publication is a
separate authorized action and must not wait for a replacement to be invented.

### Relationship to impact assessment and propagation

[CorrectionImpactAssessment](./correction_impact_assessment.md) documents the
fixture-only assessment of `CATALOG`, `API`, `MAP`, `TILE`, `SEARCH`, `GRAPH`,
`EXPORT`, `AI`, `CACHE`, and `DOCUMENTATION`. Its `COMPLETE` result is not
execution authority. The sibling validator exists, but this documentation
refresh does not rerun or certify that implementation.

[CorrectionPropagationPlan](./correction_propagation_plan.md) documents the
non-executing dependency/action inventory. Its `PASS` result is not proof
that downstream systems consumed the plan. The plan and assessment retain
their own profiles and outcome vocabularies; neither becomes the notice schema.

For a future operational supersession slice, identify affected carriers,
required rebuild/invalidation/revalidation actions, dependencies, and actual
completion evidence. Map layers, tiles, graphs, indexes, reports, and AI
answers remain carriers, not truth. Preserve stale/unavailable states until
applicable checks complete. An offline export already held by a user cannot
be assumed recalled merely because a server pointer changed.

## Validation

### Checks for this documentation revision

Check the single H1, preserved anchors, balanced fences, table structure,
repository-relative link targets, final newline, whitespace, source pins,
and exact generated-receipt artifact hash. Report the validation environment
and commands actually used. A bounded connector-sourced workspace is not a
full checkout, and schema characterization is not runtime conformance.

The existing schema can be characterized without a supersession validator:

```python
import json
from pathlib import Path
from jsonschema import Draft202012Validator

schema = json.loads(Path(
    "schemas/contracts/v1/correction/supersession_notice.schema.json"
).read_text(encoding="utf-8"))
Draft202012Validator.check_schema(schema)
validator = Draft202012Validator(schema)
assert validator.is_valid({"id": ""})  # Documents the placeholder gap.
assert validator.is_valid({"id": "example", "superseded_by": 123})
assert not validator.is_valid({})
assert not validator.is_valid({"id": 123})
```

Run from the repository root using its existing JSON Schema dependency.
These expectations describe the pinned placeholder only. Passing them does
not make either accepted example an admissible notice; revise this
characterization when the schema is deliberately strengthened.

### Future semantic and integration acceptance cases

**PROPOSED and not executed by this revision:**

| Case | Expected safety property |
| --- | --- |
| Valid governed replacement | Exact predecessor/successor/scope and decision/evidence bindings resolve; safe history and forward navigation remain available. |
| Shape-valid but incomplete notice | No effective replacement or publication claim. |
| Self-link, cycle, ambiguous successor, digest or version mismatch | Reject the claimed lineage or hold for reconciliation; no silent selection. |
| Partial replacement | Only the mapped scope changes; unrelated regions, periods, and claims remain unaffected. |
| Future effective time or delayed recording | Do not confuse planned, effective, recorded, and as-of state. |
| Missing evidence/review/release dependency | Preserve the appropriate non-effective, abstain, deny, or error posture; do not invent approval. |
| Restricted predecessor or successor | No sensitive body, identifier, reference, digest, or location leaks through the notice projection. |
| Incomplete propagation or stale offline consumer | No global completion claim; stale state and unverified consumers remain visible. |
| Failed successor and now-prohibited old release | Do not restore the old release automatically; use an independently permitted recovery posture. |
| Attempted overwrite or history deletion | Fail closed and preserve auditable correction lineage. |

No new reason-code enum, route, validator command, or production protocol is
adopted by this table.

## No-loss preservation

| Previous element | Disposition in v0.3 |
| --- | --- |
| Document ID, path, draft status, owner uncertainty, principal anchors | Retained. |
| Append-only replacement, evidence, rights, review, release, AI, and rollback boundaries | Retained and clarified; no operational authority added. |
| Placeholder schema and three declared fields | Retained and rechecked, including permissive empty-ID behavior. |
| Proposed semantic field vocabulary | Retained as proposal lineage; no implied aliases, enum, or schema adoption. |
| Unverified path references and old family inventory | Replaced with scoped current observations and explicit historical limits. |
| Supersession/withdrawal and draft/effective ambiguity | Separated without changing an executable profile. |
| Decorative badges and incomplete example tree | Replaced with a text status and evidence table; not implementation evidence. |
| Ancient scaffold rollback target | Replaced with the immediate prior document blob; earlier history remains in Git. |

## Evidence basis

Repository claims above use the pinned snapshot, not moving `main`. The
same-path documents linked here were inspected as sources; descriptions of
runtime behavior inside older documents were not promoted to implementation
facts.

| Source | What it supports | Limit |
| --- | --- | --- |
| [Pinned prior contract](https://github.com/bartytime4life/Kansas-Frontier-Matrix/blob/ec203a9ba11fb83b52245f9523ce36cc1ec6ac66/contracts/correction/supersession_notice.md) | Preserved identity, meanings, anchors, and rollback baseline. | Historical document, not execution evidence. |
| [Paired schema](../../schemas/contracts/v1/correction/supersession_notice.schema.json) | Exact required fields, types, metadata, and permissiveness. | Shape only; declared paths are not proof of implementations. |
| [Directory Rules](../../docs/doctrine/directory-rules.md) and [ADR-0029](../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md) | Adopted responsibility-root boundary and same-path placement. | No new schema, policy, migration, or release authority. |
| [Corrections Are First-Class](../../docs/doctrine/corrections-first-class.md) | Named operations, append-only audit, safe public visibility, recovery, and source vocabulary. | Draft doctrine document with historical/proposed implementation references. |
| [Publication correction architecture](../../docs/architecture/publication/CORRECTION.md) | Trust membrane, supersession lineage, review, and derivative-invalidation design. | Its proposed routes and sequencing are not verified operational behavior. |
| [Impact assessment](./correction_impact_assessment.md) and [propagation plan](./correction_propagation_plan.md) | Separate documented responsibilities and bounded outcome semantics. | No live ref resolution, downstream consumption, or SupersessionNotice enforcement proof. |
| [Drive Directory Rules](https://docs.google.com/document/d/1uTqdIEFZE2cq3gyISetoRYM6LIlnKqTc3FobtEx7Cbs/edit) | Read-only responsibility-root and lifecycle design lineage. | Does not override adopted repository authority. |
| [Notion Repository Workbench](https://app.notion.com/p/3c9a92021bf68195b8b1f3a8d694b447?pvs=204) | Read-only coordination and review/delivery-boundary context. | Neither implementation authority nor approval of this contract. |

Not-found observations are scoped to the exact pinned paths in the Status
and Schema pairing sections. Other implementations, unmerged work, external
consumers, and runtime deployment are not exhaustively inventoried here.

## Rollback

For this documentation change, preserve the immediate prior blob
`22f1fdb4a82063b7e66d0478fcc83cb03a89d68b` at the evidence snapshot. Before
integration, retain or abandon the isolated branch without altering main.
After any separately authorized integration, use an ordinary reviewed forward
revert or corrective commit. Preserve the generated receipt as historical
provenance; any correction to its assertions must be separately traceable.

Reverting this document does not roll back a published object, restore an
alias, purge a cache, revoke an export, or change release decisions. Actual
rollback requires its own evidence, policy, review, release, and execution
records. Never restore previously restricted material merely because it is
an older version.

## Definition of done

**Documentation delivery** means the same-path revision and authoring receipt
are reviewable, source-pinned, structurally checked, and accompanied by exact
validation limitations. It does not mean this draft contract is adopted or
that its semantic rules are implemented.

Before a future operational SupersessionNotice profile can be relied upon:

- [ ] Confirm accountable owners and review duties.
- [ ] Reconcile object/reference vocabulary and any correction/release compatibility questions without creating parallel authority.
- [ ] Replace the placeholder through a reviewed versioned schema, fixtures, validator, and tests covering the semantic acceptance cases.
- [ ] Verify evidence, policy, review, release, integrity, rights, sensitivity, and rollback bindings at the actual transition.
- [ ] Verify public-safe notices, as-of lineage, affected-scope behavior, and negative API/UI states.
- [ ] Demonstrate propagation completion, failure handling, and a policy-safe rollback without silently deleting history.

Safe candidate authoring may proceed while these later gates remain open.
A placeholder's acceptance is never a substitute for their closure.

## Status summary

`SupersessionNotice` remains a **draft semantic contract with a placeholder
schema**. It records auditable replacement lineage; it is not the replacement
release, policy approval, proof closure, a propagation executor, a rollback
command, or permission to publish or silently mutate history.

[Back to top](#top)
