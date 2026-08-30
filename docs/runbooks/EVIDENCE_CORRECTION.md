<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/runbook/evidence-correction
title: Evidence Correction Runbook
type: runbook
version: v2.0
prior_state: proposal-heavy May 2026 procedure with stale paths and implementation claims that no longer matched current repository evidence
status: draft; repository-grounded; CORRECTION_INTAKE_AND_CANDIDATE_GUIDANCE; BOUNDED_SHAPE_VALIDATION_ONLY; OPERATIONAL_CORRECTION_WITHDRAWAL_AND_ROLLBACK_HELD; NON_RELEASE; NON_DEPLOYMENT; NON_PUBLICATION
owners:
  - "@bartytime4life — verified GitHub review route"
  - "NEEDS VERIFICATION — accountable correction, evidence, domain, rights, sensitivity, review, release, withdrawal, rollback, and public-interface assignments"
created: 2026-05-12
updated: 2026-08-30
policy_label: public; correction-aware; fail-closed; sensitive-details-private
current_path: docs/runbooks/EVIDENCE_CORRECTION.md
owning_root: docs/
responsibility: human intake, classification, candidate preparation, bounded validation, and accountable-review handoff for suspected defects in released or release-facing KFM material
truth_posture: cite-or-abstain
authority_class: explanatory operational documentation
authority_rank: subordinate to accepted doctrine and ADRs, contracts, schemas, evidence, policy, review, release records, signatures, receipts, proofs, competent authorities, and current runtime evidence
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_ref: main
  base_commit: 8adad6a887fbda0d3ca499aff94d144352d49916
  target_before_update_blob: aa0d1237150f149dd0cc49b8b1c3d86b2fd921c8
  runbook_index_blob: 46d0adb2a23fed7bf844d691770be9596cf6a5f8
  directory_rules_blob: fd49a0b83e55cef52c1124281f093e263526898d
  directory_rules_adoption_adr_blob: a4de0d7a96b78da59cfc499d1025e1508afd8dd9
  codeowners_blob: dd2a84aa514d8ecd9208bc347f90f9a2ed37dd61
  object_family_register_blob: 03bba0769738d29bbc4c9481ba34c6c7b8366941
  correction_notice_contract_blob: 4716f2bc6e714ad2ab873d95144417d7855f5beb
  paired_correction_notice_schema_blob: 8f260eb5a5adba0b4966adfeffebfbcf6960277d
  correction_notice_validator_blob: 00b7335a39efdc6b12d180acb40a27fe682b8ade
  correction_notice_tests_blob: 49934e6a7674d8b94ae4c1f1ac61dd4275dca84b
  review_duties_blob: df9848c324cbb1b7a3d63b32bd5e2fcf929ff4e9
  generated_receipt_schema_blob: fba21ed27ebccf1362fe397fe0c3ebd85e072685
  open_pull_requests_touching_target: 0
related:
  - ./README.md
  - ./INCIDENT_RESPONSE.md
  - ./ROLLBACK_RUNBOOK.md
  - ../doctrine/directory-rules.md
  - ../doctrine/lifecycle-law.md
  - ../doctrine/trust-membrane.md
  - ../doctrine/corrections-first-class.md
  - ../governance/REVIEW_DUTIES.md
  - ../architecture/publication/rollback-and-correction.md
  - ../registers/DRIFT_REGISTER.md
  - ../registers/VERIFICATION_BACKLOG.md
  - ../../.github/ISSUE_TEMPLATE/evidence_correction.md
  - ../../SECURITY.md
  - ../../control_plane/object_family_register.yaml
  - ../../contracts/correction/correction_notice.md
  - ../../schemas/contracts/v1/correction/correction_notice.schema.json
  - ../../fixtures/correction/correction_notice/
  - ../../tools/validators/correction/validate_correction_notice.py
  - ../../tests/validators/test_validate_correction_notice.py
  - ../../release/README.md
  - ../../release/correction_notices/README.md
  - ../../release/withdrawal_notices/README.md
  - ../../release/rollback_cards/README.md
notes:
  - "v2.0 replaces proposal-era execution language with a repository-grounded intake, candidate, validation, review, and transition-boundary procedure."
  - "The current CorrectionNotice family is CONFLICTED across four schema candidates. The paired validator checks only one permissive proposed schema plus bounded JSON safety."
  - "No dedicated correction workflow or policy binding is registered in the current object-family index."
  - "No operational correction, withdrawal, rollback, cache invalidation, public notice route, release transition, deployment, or publication is established by this runbook."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Evidence Correction Runbook

Use this runbook to report, contain, classify, and prepare a reviewable response to a suspected defect in released or release-facing KFM material. It preserves prior records, keeps sensitive details private, and separates candidate preparation from any later correction, supersession, withdrawal, rollback, or publication transition.

> [!IMPORTANT]
> **This runbook is not correction authority.** It can guide intake, evidence collection, candidate preparation, bounded validation, and reviewer handoff. It cannot approve evidence, decide policy, authenticate reviewers, change a release, invalidate a public cache, withdraw an artifact, execute rollback, deploy, or publish.

> [!CAUTION]
> **Use the private route first for active exposure.** Do not put credentials, exploit details, exact sensitive locations, restricted source payloads, living-person records, DNA or genomic material, private-land detail, or critical-infrastructure vulnerability information in a public issue or pull request. Follow [`SECURITY.md`](../../SECURITY.md) and the [Incident Response Runbook](./INCIDENT_RESPONSE.md).

**Quick navigation:** [purpose](#purpose-and-authority-boundary) · [current capability](#current-repository-capability) · [when to use](#when-to-use-this-runbook) · [classification](#classification) · [roles](#roles-and-separation-of-duties) · [procedure](#procedure) · [`CorrectionNotice`](#correctionnotice-candidate) · [withdrawal and rollback](#withdrawal-and-rollback) · [derivatives](#derivative-propagation-and-invalidation) · [validation](#validation) · [closure](#closure-and-record-retention) · [open verification](#open-verification-backlog)

## Purpose and authority boundary

Accepted [ADR-0029](../adr/ADR-0029-adopt-directory-governance-standard-v2.md) adopts the [Directory Rules](../doctrine/directory-rules.md). Those rules place human operational procedures under `docs/runbooks/`, so this same-path update remains in the `docs/` responsibility root.

| Concern | Owning surface | This runbook's limit |
|---|---|---|
| Human intake, classification, and handoff | `docs/runbooks/` and the [evidence-correction issue template](../../.github/ISSUE_TEMPLATE/evidence_correction.md) | Explain the procedure and preserve a review boundary |
| Correction meaning | [`contracts/correction/correction_notice.md`](../../contracts/correction/correction_notice.md) | Cite the draft semantic contract; do not redefine it |
| Machine shape | CorrectionNotice schemas under `schemas/contracts/v1/` | Report the current conflict; do not select authority by prose |
| Admissibility and public exposure | `policy/`, rights and sensitivity records, and accountable review | Missing or unresolved support fails closed |
| Release-plane decisions and notices | [`release/`](../../release/README.md) | Require governed records; do not manufacture a decision from documentation |
| Public-safe carriers | `data/published/` and governed APIs | Never read or mutate internal lifecycle stores from this runbook |
| Receipts and proofs | `data/receipts/` and `data/proofs/` | Reference them; do not treat a receipt as proof or approval |
| Execution | Verified operators, workflows, and runtime services | No operational correction executor was established in this inspection |

The lifecycle remains:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

A correction does not bypass that path. Public clients continue to use governed interfaces and released public-safe carriers; they do not gain access to RAW, WORK, QUARANTINE, canonical or internal stores, unreleased candidates, or direct model output.

## Current repository capability

The conclusions below are bound to the evidence snapshot in the metadata block. Re-inspect them before relying on this runbook at another revision.

| Surface | Current evidence | Safe conclusion |
|---|---|---|
| Public intake | [`.github/ISSUE_TEMPLATE/evidence_correction.md`](../../.github/ISSUE_TEMPLATE/evidence_correction.md) collects identity, stale-versus-wrong posture, materiality, outcome, evidence, overlap, and rollback boundaries | Public-safe intake exists; submitting an issue does not confirm a defect or authorize a transition |
| Semantic contract | The [`CorrectionNotice` contract](../../contracts/correction/correction_notice.md) is a draft v0.2 meaning document | The family has useful semantics, but no accepted operational profile is established |
| Object-family registry | [`control_plane/object_family_register.yaml`](../../control_plane/object_family_register.yaml) marks `correction_notice` `CONFLICTED` and lists four schema candidates | Do not call one CorrectionNotice schema canonical without a governing decision |
| Paired schema | [`schemas/contracts/v1/correction/correction_notice.schema.json`](../../schemas/contracts/v1/correction/correction_notice.schema.json) is a permissive proposed placeholder that requires only `id` | Schema-valid does not mean operationally complete |
| Alternate schemas | Additional proposed candidates exist under `corrections/`, `release/`, and `review/` | The vocabulary and authority split remain unresolved |
| Fixtures and validator | Positive and negative fixtures plus [`validate_correction_notice.py`](../../tools/validators/correction/validate_correction_notice.py) provide bounded no-network JSON/schema checks | The validator does not resolve evidence, policy, review, release, withdrawal, rollback, or public state |
| Tests | [`test_validate_correction_notice.py`](../../tests/validators/test_validate_correction_notice.py) covers schema validity, minimal valid and invalid documents, duplicate keys, non-object roots, non-finite values, alias parity, and CLI behavior | Bounded executable support exists for the paired schema and input safety only |
| Workflow and policy | The object-family register lists both as absent | No dedicated correction workflow or evaluator-bound policy path is established |
| Release notices | Correction, withdrawal, and rollback-card indexes exist under `release/` | They are guidance and communication surfaces, not transition authority |
| Public runtime | No correction route, emitter, consumer, cache invalidator, or deployed public read-back was verified | Operational correction, withdrawal, rollback, and propagation remain `UNKNOWN` or held |

> [!WARNING]
> `CORRECTION_NOTICE_VALID` means only that the input passed the current paired schema and bounded JSON checks. It is not a `PolicyDecision`, `ReviewRecord`, `ReleaseManifest`, proof, withdrawal, rollback, publication event, or confirmation that the notice is true.

## When to use this runbook

Use it when material believed to be released or release-facing may be wrong, unsupported, misleading, unlawfully exposed, overspecific, stale in a way that changes meaning, or inconsistent across public carriers. Typical triggers include:

- an `EvidenceRef` no longer resolves or its `EvidenceBundle` no longer supports the claim;
- an observation, model, forecast, classification, aggregate, regulation, context source, or synthetic fixture was assigned the wrong source role;
- rights, consent, sovereignty, privacy, or sensitivity posture changed;
- geometry, time, attribution, identity, units, uncertainty, or provenance are materially wrong;
- a validation, policy, review, manifest, signature, proof, or release reference no longer closes;
- an API, map, tile, search result, export, report, graph, or AI response conveys a different meaning from the released record; or
- a public artifact must be superseded, withdrawn, or considered for rollback.

Do not use this runbook to make routine pre-release edits in `RAW`, `WORK`, `QUARANTINE`, or candidate material. Use the normal owning workflow unless the defect also reached a released or release-facing surface.

### Immediate containment boundary

When exposure is active or harmful, do not wait for a polished notice. Use the private incident route and seek an authorized fail-closed containment action. Preserve identifiers, timestamps, digests, and audit records without copying the sensitive payload into public coordination. Containment does not itself approve a correction or authorize republication.

## Classification

Classify two independent things: the observed state and the proposed next outcome.

### Observed state

| State | Meaning | Initial posture |
|---|---|---|
| `STALE` | Support aged beyond a declared tolerance, but the prior claim may still describe what was known at release time | Show stale state and trigger review; do not silently refresh |
| `WRONG` | Meaning, support, rights, sensitivity, identity, geometry, time, or release posture is materially incorrect | Contain when necessary and prepare correction, narrowing, denial, supersession, withdrawal, or rollback review |
| `DISPUTED` | Credible evidence or authority conflicts and no resolution is yet accepted | Preserve the dispute; narrow or abstain when consequence requires it |
| `UNCLEAR` | Evidence is insufficient to decide stale, wrong, or disputed | `HOLD`, `ABSTAIN`, or `DENY` rather than guessing |

A rights or policy change that makes formerly public material no longer releasable is not merely a freshness issue. Treat the public posture as wrong and route it through rights, sensitivity, policy, and release review.

### Candidate outcomes

The issue template currently uses the following human-routing vocabulary. It is not a canonical machine enum:

| Candidate outcome | Intended use |
|---|---|
| `NO_ACTION` | Current material remains supportable; close with evidence |
| `CLARIFY` | Improve wording or context without changing the underlying released meaning |
| `MARK_STALE` | Preserve prior release while making stale state visible |
| `CORRECT` | Prepare a superseding evidence or release candidate |
| `NARROW` / `ABSTAIN` | Remove unsupported scope or decline to restate the claim |
| `DENY` / `REDACT` / `GENERALIZE` | Prevent unsafe or unauthorized exposure before delivery |
| `SUPERSEDE` | Replace the current public identity with a reviewed successor while preserving lineage |
| `WITHDRAW` | Remove the affected public item under a governed decision while retaining the allowed audit trail |
| `ROLLBACK_REVIEW` | Evaluate re-pointing public state to a verified prior safe release |
| `HOLD` | Stop because an evidence, rights, sensitivity, review, policy, identity, overlap, or rollback prerequisite is unresolved |
| `ERROR` | The procedure or supporting system could not produce a trustworthy result |

### Defect families

Record the primary defect and any material secondary defects: evidence closure, source role, rights or consent, sensitivity or harmful precision, identity or lineage, spatial representation, temporal representation, policy, validation, API/runtime, renderer/carrier, AI/citation, catalog/index, release integrity, or operational integrity. Do not invent a stable reason code when the governing profile does not define one.

## Roles and separation of duties

| Role | Responsibility | Current status |
|---|---|---|
| Detector or reporter | Preserve the observation, affected identity, time, and public-safe reproduction | Any contributor may report; sensitive material stays private |
| Triage coordinator | Classify immediate risk, coordinate containment, and keep the record current | Assignment `NEEDS VERIFICATION` |
| Domain or evidence steward | Assess source role, evidentiary support, spatial/temporal meaning, and corrected candidate | Assignment `NEEDS VERIFICATION` |
| Rights, sensitivity, privacy, or sovereignty reviewer | Review restricted-use and public-safe transformation decisions | Required when applicable; assignments `NEEDS VERIFICATION` |
| Correction reviewer | Evaluate classification, lineage, evidence, propagation, and notice candidate | Operational roster `NEEDS VERIFICATION` |
| Policy reviewer | Supply or verify applicable policy results | Dedicated correction binding is not established |
| Release or rollback authority | Decide a later governed transition and verify rollback support | Operational authority not established here |
| Documentation steward | Keep public-safe explanation, runbooks, registers, and navigation accurate | Concrete assignment `NEEDS VERIFICATION` |

[`CODEOWNERS`](../../.github/CODEOWNERS) routes review to `@bartytime4life`. That is a verified GitHub route, not proof of domain expertise, independence, approval, a `StewardshipAssignment`, a `ReviewRecord`, or release authority. Follow [Review Duties](../governance/REVIEW_DUTIES.md) and keep authoring, review, policy decision, release, and publication separate when materiality requires it.

## Procedure

### 1. Choose public or private intake

Use the [evidence-correction issue template](../../.github/ISSUE_TEMPLATE/evidence_correction.md) only when the report can be safely public. Use `SECURITY.md` and incident coordination for vulnerabilities, active exposure, restricted material, harmful precision, or details that would make the problem easier to exploit.

### 2. Pin the affected state

Record exact identifiers where available: repository commit, release or manifest ID, artifact digest, claim or evidence reference, layer/export/report identity, public URL, place/time scope, first and latest observation times, and the public-safe reproduction. Distinguish the source record from every derivative carrier.

### 3. Search for overlap

Check current correction records, issues, branches, pull requests, incident references, changelog entries, and release notices. Reuse or reconcile the same work when safe; do not create competing correction histories or overwrite another contributor's branch.

### 4. Contain active harm

For an active rights, sensitivity, privacy, security, or integrity exposure, seek authorized containment before broad diagnosis. The safe posture may be denial, redaction, generalization, route/layer hold, cache isolation, or full withdrawal review. Record what was requested and what was actually confirmed; do not claim unverified invalidation.

### 5. Classify state, defects, and materiality

Choose `STALE`, `WRONG`, `DISPUTED`, or `UNCLEAR`; identify primary and secondary defect families; and record the consequence of leaving the surface unchanged. When several correction paths are possible, use the least expansive path that closes the defect without erasing audit history.

### 6. Resolve evidence and source role

Trace the affected claim to current admissible evidence and source records. Record whether evidence resolves, the role each source can support, relevant rights and sensitivity posture, spatial and temporal limits, uncertainty, and conflicts. Maps, indexes, summaries, AI output, and repeated prose do not replace an `EvidenceBundle`.

### 7. Bound consumers and derivatives

Inventory direct and plausible consumers: canonical object, catalog/triplet projection, governed API, map/tile/raster/3D carrier, Evidence Drawer, search index, graph/vector index, report/export/story, AI receipt or cached answer, CDN/object-store alias, and offline bundle. Classify each as affected, not affected with evidence, `UNKNOWN`, or held.

### 8. Select the candidate outcome

Choose one primary candidate outcome from the table above and record alternatives considered. A candidate is not an approved decision. If replacement evidence is absent, prefer narrowing, abstention, denial, withdrawal review, or hold over unsupported restatement.

### 9. Build through owning roots

Prepare changes through the normal lifecycle and responsibility roots. Keep semantic contract, machine schema, policy, fixtures/tests, receipts/proofs, release records, notices, and public artifacts separate. Preserve prior immutable releases and records; a correction is not an in-place overwrite.

### 10. Prepare the `CorrectionNotice` candidate

Name the semantic contract, selected schema profile, prior and proposed identities, affected releases or assets, public-safe reason and summary, evidence references, review and policy prerequisites, derivative disposition, supersession or withdrawal relationships, and rollback or forward-fix boundary. See the current conflict below.

### 11. Validate and hand off

Run proportionate no-network checks, record exact commands and outputs, and separate performed, failed, skipped, unavailable, inherited, and hosted checks. Route the candidate to accountable reviewers. A schema-valid candidate remains a candidate until evidence, policy, review, and release gates close.

### 12. Execute only under separate authority

Correction, public notice publication, derivative invalidation, withdrawal, rollback, release, deployment, promotion, publication, and external writes are later governed transitions. This runbook does not authorize them. After an authorized transition, verify public read-back and retain correction, review, decision, receipt, proof, manifest, notice, and rollback lineage.

## `CorrectionNotice` candidate

### Current conflict

The object-family register lists four proposed schema candidates:

1. `schemas/contracts/v1/correction/correction_notice.schema.json` — paired with the current validator and fixtures; permissive placeholder requiring only `id`.
2. `schemas/contracts/v1/corrections/correction_notice_candidate.schema.json` — permissive candidate scaffold.
3. `schemas/contracts/v1/release/correction_notice.schema.json` — permissive release-lane scaffold.
4. `schemas/contracts/v1/review/correction_notice.schema.json` — permissive review-lane scaffold.

The draft semantic contract is richer than all four. Until a governing decision and migration establish one profile, name the exact schema used and do not imply cross-profile compatibility.

### Candidate review packet

At minimum, provide:

| Field | Requirement |
|---|---|
| Identity | Stable candidate ID and affected object/release identifiers |
| State and reason | Observed state, defect family, materiality, public-safe explanation |
| Evidence | Resolvable references, source roles, scope, limitations, conflicts |
| Prior and successor state | Prior identity/digest, proposed identity/digest, supersession or withdrawal relation |
| Rights and sensitivity | Review status, obligations, transforms, withheld-detail note |
| Review and policy | Required roles, records, outcomes, unresolved prerequisites |
| Derivatives | Consumer inventory and invalidate/rebuild/retain/hold disposition |
| Release boundary | Candidate release or withdrawal relationship; no prose-only transition |
| Recovery | Verified rollback target or forward-fix boundary, or explicit hold |
| Audit | Receipts, proofs, validation reports, timestamps, and public read-back plan |

Do not copy a hypothetical JSON example into production as though it were canonical. Use the selected schema, current fixtures, and semantic contract, and identify any field not represented by the selected machine shape.

## Withdrawal and rollback

Correction, withdrawal, and rollback solve different problems:

| Path | Use when | Result | Required caution |
|---|---|---|---|
| Forward correction / supersession | A reviewed successor can replace the affected meaning | New governed state points forward; prior state remains inspectable | Complete evidence, policy, review, release, lineage, and derivatives |
| Withdrawal | Material must no longer be publicly served and no immediate replacement is approved | Public access is removed or held; public-safe notice and audit lineage remain as allowed | Rights, privacy, sovereignty, security, or lawful erasure duties can limit public explanation |
| Rollback review | Current public state has an operational/integrity defect and a verified prior safe release may be restored | Candidate re-pointing to an immutable prior release | Do not assume the prior release is safe, compatible, authorized, or available |
| Hold / deny / abstain | Prerequisites are unresolved | No higher transition | Preserve the reason and the evidence needed to continue |

The [Rollback Runbook](./ROLLBACK_RUNBOOK.md), [correction-notice index](../../release/correction_notices/README.md), [withdrawal-notice index](../../release/withdrawal_notices/README.md), and [rollback-card index](../../release/rollback_cards/README.md) are guidance surfaces. Their presence does not prove an operational executor or authorized transition.

## Derivative propagation and invalidation

A correction is incomplete when an affected downstream carrier still presents the old meaning as current. For each derivative, record identity, prior digest/version, owner or resolver, action, verification method, and final state.

| Derivative family | Typical action | Evidence needed before closure |
|---|---|---|
| Catalog/triplet/graph projections | Rebuild or mark superseded | New identity/digest and lineage to corrected canonical support |
| Governed API and Evidence Drawer | Refresh released projection and correction state | Exact response/read-back from the governed public path |
| MVT, PMTiles, COG, raster, scene, or 3D asset | Rebuild, withdraw, or re-point immutable artifact | Manifest/digest parity and public-safe spatial checks |
| Search/vector indexes | Rebuild or remove stale entries | Query-based read-back showing no unsupported current result |
| AI answers and caches | Invalidate affected receipt/answer and generate a new bounded result or abstention | New receipt/citation validation; old receipt retained for audit where allowed |
| Reports, exports, stories, and offline bundles | Reissue, supersede, withdraw, or visibly mark stale | Inventory closure and public-safe notice/linkage |
| CDN, object-store aliases, browser/service-worker caches | Purge or re-point under authorized operations | Provider/operator receipt plus external read-back |

When the inventory cannot be bounded, stop at `HOLD` or narrow the correction. Client-side hiding is not sufficient redaction or invalidation.

## Validation

### Current bounded validator

From a repository checkout with the declared dependencies installed:

```bash
python tools/validators/correction/validate_correction_notice.py --fixtures
python -m pytest -q tests/validators/test_validate_correction_notice.py
```

Validate a candidate file explicitly:

```bash
python tools/validators/correction/validate_correction_notice.py path/to/candidate.json
```

The compatibility entry point is `tools/validators/validate_correction_notice.py`. The current validator emits these stable input/schema findings: `INPUT_NOT_FILE`, `INPUT_TOO_LARGE`, `JSON_DUPLICATE_KEY`, `JSON_INVALID`, `INPUT_UNREADABLE`, `JSON_ROOT_INVALID`, and `SCHEMA_INVALID`.

### Required checks by affected surface

- Confirm the selected schema and semantic contract are named.
- Run schema/input tests and relevant positive and negative fixtures.
- Resolve evidence references independently of shape validation.
- Re-evaluate rights, sensitivity, consent, sovereignty, and policy where applicable.
- Verify review records and actor authority rather than relying on names in prose.
- Rebuild and verify every affected derivative.
- Verify immutable digests, manifests, supersession/withdrawal links, and rollback target.
- Test governed public read-back, including stale, abstain, deny, withdrawn, superseded, and error behavior where material.
- Record network access and external side effects; default repository validation should remain no-network.

For Markdown-only changes to this runbook:

```bash
git diff --check -- docs/runbooks/EVIDENCE_CORRECTION.md
```

Also verify one H1, heading order, anchors, tables, code fences, relative links, final newline, and absence of sensitive material. No canonical repository-wide Markdown link checker was verified at the evidence snapshot.

### Interpretation limits

A schema or validator pass proves only its implemented checks. A workflow pass proves only the exact head, trigger, inputs, and steps run. A notice proves communication, not the underlying correction. A receipt records process memory; it is not evidence closure or proof. A pull request or merge proves repository history, not a correction, withdrawal, rollback, release, deployment, promotion, or publication event.

## Public interface behavior

No dedicated correction API route was verified. Treat route names, response fields, and UI component names as `UNKNOWN` unless current implementation evidence establishes them.

Where a governed public surface represents correction state, it should provide only the public-safe subset needed to understand whether the item is current, stale, disputed, corrected, superseded, withdrawn, denied, or unavailable; which released identity replaces it when public; when the state changed; a safe summary and limitation; resolvable public evidence or notice references; and how to report another discrepancy.

It must not expose internal evidence, restricted reasons, private review notes, exact sensitive geometry, unreleased candidates, credentials, or model-runtime internals.

## Closure and record retention

A correction is closed only when all applicable items are supported:

- [ ] The affected identity, release, place, time, and public surface are pinned.
- [ ] Classification and materiality are supported.
- [ ] Evidence resolves or the outcome explicitly narrows, abstains, denies, or withdraws.
- [ ] Rights, consent, sovereignty, and sensitivity review is complete where applicable.
- [ ] The exact contract and schema profile are named; validation limits are recorded.
- [ ] Accountable review, policy, and release decisions are present where required.
- [ ] Prior records and immutable artifacts remain inspectable where legally and ethically allowed.
- [ ] Supersession, correction, withdrawal, or rollback lineage resolves in both directions where supported.
- [ ] Direct derivatives are invalidated, rebuilt and verified, or explicitly held.
- [ ] Governed public read-back matches the approved state.
- [ ] Public notice is visible when required and does not disclose restricted detail.
- [ ] Remaining unknowns name the evidence needed and first blocked transition.

Preserve the issue or private incident reference, candidate changes, review and policy records, release decisions, notices, receipts, proofs, manifests, changelog entries, and validation results under their owning roots. Do not copy restricted incident material into public correction records.

## Stop conditions

Stop and return `HOLD`, `DENY`, `ABSTAIN`, or `ERROR` as appropriate when the affected release or identity cannot be resolved; required evidence does not resolve; source role, rights, consent, sovereignty, or sensitivity is unclear; the response would expose restricted detail; overlapping work cannot be reconciled safely; the selected schema profile is ambiguous for the intended transition; accountable review, policy, or release authority is absent; derivative impact cannot be bounded; no safe recovery boundary exists; public read-back contradicts the intended correction; or the action requires an unauthorized release, deployment, promotion, publication, external write, or administrative bypass.

## Worked scenarios

These examples are illustrative; they do not assert deployed KFM behavior.

### Unsupported public claim

A report cites an `EvidenceRef` that no longer resolves to a released `EvidenceBundle`. Pin the report, claim, release, and unresolved reference; classify the meaning as unsupported rather than merely stale; narrow or abstain while replacement evidence is reviewed; prepare a candidate through the normal lifecycle; inventory API, map, search, export, report, and AI consumers; and stop before republication unless evidence, policy, review, release, and derivative closure are complete.

### Sensitive location in a derivative

A map export contains harmful precision that should have been generalized. Use the private incident route; seek authorized containment of the export and its derivative copies; preserve digest and audit identity without preserving public access; route sensitivity, rights, and domain review; rebuild the public-safe carrier before rendering rather than hiding it in the client; and publish only a safe notice.

## Anti-patterns

- Silently editing or replacing an already released artifact.
- Calling a CorrectionNotice schema canonical because one validator imports it.
- Treating `CORRECTION_NOTICE_VALID` as evidence, approval, or release readiness.
- Inventing owners, routes, fields, reason codes, deadlines, or completed invalidation.
- Reporting sensitive details in a public correction issue.
- Letting notice prose substitute for evidence or a release decision.
- Correcting the map while leaving the API, search index, export, or AI cache stale.
- Reusing an immutable ID for materially different bytes or meaning.
- Deleting the prior record to make the current state look clean.
- Allowing AI-generated language to approve its own correction.
- Using a pull request merge as a release, withdrawal, rollback, or publication event.
- Closing while a known affected derivative remains unclassified.

## Open verification backlog

| Item | Current status | First blocked transition |
|---|---|---|
| CorrectionNotice schema authority across four candidates | `CONFLICTED` | Canonical machine profile and interoperable instance production |
| Correction policy binding | `ABSENT` in the object-family registry | Policy-backed correction or release decision |
| Dedicated correction workflow | `ABSENT` in the object-family registry | Repeatable repository-orchestrated candidate validation |
| Operational emitter and consumer inventory | `NOT INSPECTED` / `UNKNOWN` | End-to-end correction production and public parity |
| WithdrawalNotice machine contract, schema, validator, and execution path | `NEEDS VERIFICATION` | Governed withdrawal |
| Authenticated reviewers and independent release authority | `NEEDS VERIFICATION` | Steward-significant correction, withdrawal, or rollback |
| Stable public notice and correction-state API surface | `UNKNOWN` | Public visibility and read-back |
| External cache, alias, search, export, and AI invalidation | `UNKNOWN` | Verified operational propagation |
| Correction and rollback rehearsal against a real governed release | `UNKNOWN` | Operational readiness |
| Lawful deletion or erasure boundary distinct from audit-preserving withdrawal | `NEEDS VERIFICATION` | Any retention exception that cannot preserve the normal audit record |

Track cross-cutting items in the [Verification Backlog](../registers/VERIFICATION_BACKLOG.md) or [Drift Register](../registers/DRIFT_REGISTER.md) under their governing rules. This runbook does not create or close those records.

## Related documentation

| Resource | Role |
|---|---|
| [Runbook index](./README.md) | Parent navigation and runbook authority boundary |
| [Evidence-correction issue template](../../.github/ISSUE_TEMPLATE/evidence_correction.md) | Public-safe intake and triage worksheet |
| [`SECURITY.md`](../../SECURITY.md) | Private-first security and sensitive-disclosure route |
| [Incident Response Runbook](./INCIDENT_RESPONSE.md) | Active containment and incident coordination |
| [Rollback Runbook](./ROLLBACK_RUNBOOK.md) | Rollback readiness and review procedure |
| [Corrections Are First-Class](../doctrine/corrections-first-class.md) | Draft correction doctrine and lineage |
| [Publication rollback and correction](../architecture/publication/rollback-and-correction.md) | Architecture comparison of forward correction and rollback |
| [Review Duties](../governance/REVIEW_DUTIES.md) | Repository-grounded review and separation guidance |
| [`CorrectionNotice` contract](../../contracts/correction/correction_notice.md) | Draft semantic meaning |
| [Object-family register](../../control_plane/object_family_register.yaml) | Current navigational maturity and conflict index |
| [Correction-notice index](../../release/correction_notices/README.md) | Release-plane notice guidance |
| [Withdrawal-notice index](../../release/withdrawal_notices/README.md) | Release-plane withdrawal notice guidance |
| [Release root](../../release/README.md) | Canonical append-only release-decision responsibility |

## Documentation rollback

This update changes documentation and its generated provenance receipt only. Roll back by reverting the focused commit or applying a forward documentation fix that restores the prior blob. Reverting this runbook does not roll back a KFM release, correction, withdrawal, public artifact, deployment, or publication.

[Back to top](#top)
