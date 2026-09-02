<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/pipelines-publish-fauna-readme
title: Fauna Publish-Readiness Adapter README
type: readme
version: v0.2
status: draft
owners:
  - <pipeline-owner>
  - <fauna-domain-steward>
  - <sensitivity-reviewer>
  - <release-steward>
  - <evidence-steward>
  - <docs-steward>
created: 2026-06-13
updated: 2026-07-22
policy_label: public
path: pipelines/publish/fauna/README.md
related:
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - docs/architecture/release-discipline.md
  - docs/standards/RELEASE_MANIFEST.md
  - pipelines/README.md
  - pipelines/publish/README.md
  - pipelines/domains/fauna/README.md
  - docs/domains/fauna/ARCHITECTURE.md
  - pipeline_specs/README.md
  - pipeline_specs/fauna/README.md
  - fixtures/domains/fauna/README.md
  - tests/domains/fauna/README.md
  - policy/domains/fauna/README.md
  - policy/sensitivity/fauna/README.md
  - release/candidates/fauna/README.md
  - release/manifests/README.md
  - data/catalog/domain/fauna/README.md
  - data/published/layers/fauna/README.md
  - data/proofs/evidence_bundle/README.md
tags: [kfm, pipelines, publish, fauna, readiness, evidence, sensitivity, release, rollback, correction]
notes:
  - "This document describes a Fauna adapter/profile inside the shared publish-readiness lane; it does not establish release authority."
  - "Executable depth is UNKNOWN. Named prospective implementation files and the previously referenced pipeline_specs/publish/fauna.yaml were not present at the pinned evidence snapshot."
  - "If this lane grows into a full Fauna publish workflow, placement must be reconciled with pipelines/domains/fauna/ through an accepted ADR or migration decision."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Fauna publish-readiness adapter

> Fauna-specific adapter guidance for checking whether a governed release candidate is ready to be handed to release authority. A successful check is not publication, release approval, or permission to expose sensitive wildlife locations.

![status](https://img.shields.io/badge/status-draft-blue)
![maturity](https://img.shields.io/badge/implementation-UNKNOWN-orange)
![root](https://img.shields.io/badge/root-pipelines%2F-0a7ea4)
![authority](https://img.shields.io/badge/release%20authority-separate-d62728)
![sensitivity](https://img.shields.io/badge/fauna-fail%20closed-d62728)

**Path:** `pipelines/publish/fauna/README.md`  
**Responsibility root:** `pipelines/` — executable pipeline logic  
**Lane role:** Fauna adapter/profile under shared publish-readiness support  
**Document lifecycle:** DRAFT  
**Component maturity:** UNKNOWN  
**Public posture:** readiness support only; no direct public-serving or release mutation

> [!IMPORTANT]
> This lane may check and report readiness. It must not approve a release, create evidence, decide policy, author a final `ReleaseManifest`, move a candidate to `PUBLISHED`, or alter a governed API, map, export, search index, or other public surface as a side effect.

## Quick navigation

- [Purpose](#purpose)
- [Authority level](#authority-level)
- [Status and evidence boundary](#status-and-evidence-boundary)
- [What belongs here](#what-belongs-here)
- [What does not belong here](#what-does-not-belong-here)
- [Inputs](#inputs)
- [Outputs](#outputs)
- [Validation](#validation)
- [Review burden](#review-burden)
- [Related folders](#related-folders)
- [ADRs and placement decisions](#adrs-and-placement-decisions)
- [Last reviewed](#last-reviewed)

---

<a id="purpose"></a>

## Purpose

This directory is reserved for Fauna-specific adaptation of shared publish-readiness behavior. Its job is to help an authorized caller determine whether a Fauna release candidate has the evidence, policy, review, integrity, public-representation, correction, and rollback support needed for a release-steward handoff.

The adapter may:

- resolve candidate, artifact, catalog, triplet, and receipt references supplied by an authorized caller;
- verify that release-facing claims resolve from `EvidenceRef` to `EvidenceBundle`;
- verify source-role, rights, freshness, identity, temporal, sensitivity, and public-representation closure;
- check `ReviewRecord`, validation, manifest-input, digest, correction, and rollback references;
- return a finite readiness outcome, structured blockers, and an auditable receipt fragment;
- return control to the Fauna domain lane and release authority without changing release state.

It is not the primary Fauna pipeline. Domain-owned normalization, identity, evidence construction, sensitivity transformation, and publication preparation remain the responsibility of the accepted Fauna domain lanes and their governing contracts, schemas, policies, fixtures, and tests.

[Back to top](#top)

---

<a id="authority-level"></a>

## Authority level

**Implementation-lane documentation; readiness support only.**

| Question | Answer | Evidence status |
|---|---|---|
| Why is this under `pipelines/`? | The lane describes executable publish-readiness logic: the **how**, not declarative configuration or release decisions. | CONFIRMED by Directory Rules |
| Why is it under shared `publish/`? | It is scoped as a Fauna adapter to shared checks, not as the full domain publish workflow. | PROPOSED / NEEDS VERIFICATION |
| Does it replace `pipelines/domains/fauna/`? | No. That is the confirmed primary Fauna domain pipeline lane. | CONFIRMED boundary |
| Does it own declarative configuration? | No. `pipeline_specs/` owns the **what**; the exact future Fauna publish profile path remains unresolved. | CONFIRMED root split / NEEDS VERIFICATION path |
| Does it own policy, schemas, contracts, evidence, or release decisions? | No. Those remain in their responsibility roots. | CONFIRMED boundary |
| Can an adapter pass publish data? | No. Only release authority may perform the governed transition to `PUBLISHED`. | CONFIRMED invariant |
| Can public clients read this lane or canonical stores directly? | No. Public clients use governed interfaces and released artifacts. | CONFIRMED trust-membrane rule |

The placement is acceptable only while this directory remains a thin adapter/profile inside the shared publish-readiness lane. If it begins to own full Fauna publish behavior, the work must pause for placement review against [`pipelines/domains/fauna/`](../../domains/fauna/README.md) and any applicable accepted ADR or migration record.

### Authority boundaries

| Object or decision | This lane may | This lane must not |
|---|---|---|
| `EvidenceRef` / `EvidenceBundle` | Resolve and verify required references. | Create, rewrite, or treat a reference as the bundle itself. |
| `PolicyDecision` | Require and inspect an applicable decision. | Invent, approve, or weaken policy. |
| `ValidationReport` | Require and evaluate declared status. | Convert a validation pass into release approval. |
| `ReviewRecord` | Require a review state appropriate to materiality. | Self-approve or collapse author and approver duties. |
| `RedactionReceipt` or representation receipt | Require and verify linkage for public-safe derivatives. | Reveal restricted input or declare a transform safe without proof. |
| `ReleaseManifest` | Validate a proposed input package and hand it off. | Author or approve the final release record. |
| `CorrectionNotice` / `RollbackCard` | Verify a resolvable correction path and rollback target. | Execute release rollback or close a correction decision. |
| Published artifact | Verify digest and public-safe representation references. | Write, deploy, publish, or serve it. |

[Back to top](#top)

---

<a id="status-and-evidence-boundary"></a>

## Status and evidence boundary

This README separates verified repository state from proposed future behavior.

### Confirmed at the pinned evidence snapshot

- This README, the parent publish README, the pipelines root README, and the primary Fauna pipeline README exist.
- Directory Rules place executable pipeline logic in `pipelines/`, declarative profiles in `pipeline_specs/`, domain pipeline lanes in `pipelines/domains/<domain>/`, and release decisions in `release/`.
- Fauna architecture and policy documentation require fail-closed handling for sensitive occurrence material and public-safe derived representations.
- Repository documentation exists for Fauna fixtures, tests, sensitivity policy, release candidates, catalog material, published layers, and EvidenceBundles.

### Not confirmed as implemented

- No complete subtree inventory was available in this authoring pass; executable depth therefore remains **UNKNOWN**.
- The previously referenced `pipeline_specs/publish/fauna.yaml` was not present at the pinned snapshot.
- Named prospective files such as `FAUNA_PUBLISH_ADAPTER_CONTRACT.md`, `run_dry_fixture.py`, and `validate_release_candidate.py` were checked and were not present.
- No target-specific accepted ADR confirming this adapter's long-term placement was established in the bounded ADR search.
- No schema-backed adapter receipt vocabulary, blocker reason-code registry, or exact CI ownership was confirmed.

> [!NOTE]
> The contracts below define the lane's required posture for future implementation. They do not claim that executables, schemas, tests, fixtures, receipts, or release integrations already exist.

### Lifecycle boundary

The adapter must preserve:

```text
RAW -> WORK / QUARANTINE -> PROCESSED -> CATALOG / TRIPLET -> PUBLISHED
```

Promotion is a governed state transition, not a file move, successful pipeline run, commit, pull request, artifact upload, deployment, or adapter outcome.

[Back to top](#top)

---

<a id="what-belongs-here"></a>

## What belongs here

Only thin Fauna adaptations of shared publish-readiness behavior belong here, including:

- Fauna release-candidate reference and digest checks;
- object-family, identity, and temporal-scope preservation checks;
- source-role, rights, license, attribution, and freshness closure checks;
- EvidenceBundle and ReviewRecord resolution checks;
- public-representation, geoprivacy, redaction, generalization, aggregation, delay, and withholding receipt checks;
- manifest-input, correction-path, rollback-target, and trust-membrane checks;
- deterministic blocker construction and readiness-receipt fragments;
- fixture-only dry-run entrypoints after their placement and contract are accepted;
- caller adapters that return control to `pipelines/domains/fauna/` or release authority.

### Admission test for future files

A future file belongs here only when every answer below is **yes**:

1. Is its primary responsibility executable publish-readiness adaptation?
2. Is it Fauna-specific glue around shared publish checks rather than primary domain logic?
3. Does it avoid owning policy, semantic contracts, machine schemas, evidence, release decisions, or public serving?
4. Does it fail closed on unresolved rights, sensitivity, evidence, review, correction, or rollback state?
5. Does it emit only a readiness result, blockers, receipt fragment, or controlled handoff?
6. Is its exact placement supported by Directory Rules, adjacent repository evidence, and applicable ADRs?

If any answer is **no**, place the work in the responsibility root that owns it or resolve the conflict before implementation.

### Invariants to preserve

```text
adapter READY      != release approval
candidate          != PUBLISHED
EvidenceRef        != EvidenceBundle
ValidationReport   != PolicyDecision
manifest input     != final ReleaseManifest
redacted candidate != proven public-safe derivative
generated summary  != evidence
commit or PR       != KFM publication
```

[Back to top](#top)

---

<a id="what-does-not-belong-here"></a>

## What does not belong here

| Do not place or perform here | Owning responsibility |
|---|---|
| Primary Fauna ingestion, normalization, identity, evidence construction, or domain orchestration | [`pipelines/domains/fauna/`](../../domains/fauna/README.md) |
| Declarative pipeline profile | [`pipeline_specs/`](../../../pipeline_specs/README.md); exact Fauna publish path NEEDS VERIFICATION |
| Object meaning or semantic contract | `contracts/` |
| Machine-readable schema | `schemas/` |
| Admissibility, sensitivity, geoprivacy, rights, or release policy | [`policy/domains/fauna/`](../../../policy/domains/fauna/README.md) and [`policy/sensitivity/fauna/`](../../../policy/sensitivity/fauna/README.md) |
| Fixtures or test data | [`fixtures/domains/fauna/`](../../../fixtures/domains/fauna/README.md) or another accepted fixture lane |
| Tests | [`tests/domains/fauna/`](../../../tests/domains/fauna/README.md) or another accepted test lane |
| EvidenceBundles | [`data/proofs/evidence_bundle/`](../../../data/proofs/evidence_bundle/README.md) |
| Catalog truth or triplet projection authority | [`data/catalog/domain/fauna/`](../../../data/catalog/domain/fauna/README.md) and accepted triplet homes |
| Release decision, final manifest, approval, correction decision, or rollback decision | [`release/`](../../../release/manifests/README.md) responsibility lanes |
| Published layers or public artifacts | [`data/published/layers/fauna/`](../../../data/published/layers/fauna/README.md) through an approved release workflow |
| Public API, map, UI, search, export, or governed AI behavior | Governed application and runtime roots |
| Exact sensitive occurrence, nest, den, roost, hibernaculum, spawning, telemetry, or steward-controlled location data | Restricted stores and policy-controlled workflows; never this public README or logs |

Generated outputs, receipts, proofs, manifests, candidates, and lifecycle data must not be written beside adapter code.

[Back to top](#top)

---

<a id="inputs"></a>

## Inputs

The adapter accepts references and declared states, not ungoverned direct access to canonical stores.

| Input class | Minimum required information | Failure posture |
|---|---|---|
| Caller context | Authorized owner, purpose, requested release class, and approved candidate scope. | `HELD` when ownerless or out of scope. |
| Release candidate | Stable candidate reference, lifecycle state, artifact references, content digests, and parent lineage. | `HELD` on missing or stale closure. |
| Fauna object scope | Object-family labels, deterministic identities, spatial and temporal scope, and representation class. | `HELD` on ambiguity or collapse. |
| Source support | `SourceDescriptor` references, source roles, rights, attribution, freshness, and authority limits. | `HELD` or `DENIED` according to the governing decision. |
| Evidence support | Required `EvidenceRef` values and resolvable `EvidenceBundle` references for release-facing claims. | `HELD`; claims must not pass unsupported. |
| Validation support | Applicable validation reports and receipt lineage for transforms and artifacts. | `HELD` on missing, failing, or unverifiable status. |
| Policy support | Applicable rights, sensitivity, geoprivacy, public-representation, and release decision references. | `DENIED` or `HELD`; never infer permission. |
| Review support | Required `ReviewRecord` references and separation-of-duties posture. | `HELD` when review is required but unresolved. |
| Public-safe derivative | Digest-linked generalized, redacted, aggregated, delayed, restricted, or withheld representation plus required receipts. | `DENIED` for unsafe public exposure. |
| Manifest inputs | Hashable artifact set, release metadata, dependency refs, and declared public representation. | `HELD` until complete. |
| Correction and rollback | Correction route, invalidation scope, rollback target, and downstream dependency posture. | `HELD` until resolvable. |

### Source-role and evidence rules

- Aggregator or discovery sources must not be silently elevated to legal-status or regulatory authority.
- Conflicting source roles remain visible and block unsupported authority claims.
- Every release-facing factual claim must resolve to admissible evidence or be removed from the candidate.
- A catalog record, triplet projection, model output, summary, tile, or derived layer is not sovereign truth.
- Stale, superseded, or withdrawn support must remain visible to the readiness decision.

### Identity and time rules

- Preserve deterministic identifiers and parent-child digest linkage where repository contracts support them.
- Keep observed time, source-valid time, processing time, review time, and release time distinct where material.
- Do not treat a historical occurrence as current presence or a candidate identification as a confirmed taxon.
- Reject or hold candidates whose identity, temporal scope, or representation lineage cannot be resolved sufficiently for release.

[Back to top](#top)

---

<a id="outputs"></a>

## Outputs

The adapter may emit only non-authoritative readiness support:

- one finite readiness outcome;
- deterministic blocker or reason codes once a canonical vocabulary exists;
- a readiness report referencing the exact candidate and evidence snapshot;
- a manifest-input package for release-authority review;
- an auditable receipt fragment with input, check, decision-reference, and output digests;
- a controlled handoff to the Fauna domain lane or release steward.

### Proposed finite readiness outcomes

This is a documentation-level vocabulary and is **PROPOSED**, not a confirmed schema enum.

| Outcome | Meaning | Permitted next step |
|---|---|---|
| `READY` | All required checks for the adapter's bounded scope completed with resolvable support. | Hand off to release authority; do not publish. |
| `HELD` | Required evidence, review, identity, time, rights, validation, receipt, manifest input, correction, or rollback support is incomplete or unresolved. | Correct or supply the missing support, then rerun. |
| `DENIED` | Governing policy or rights prohibit the requested public representation or operation. | Stop; use only an authorized alternative representation or decision path. |
| `ERROR` | The adapter could not determine readiness because of a system, parsing, dependency, or integrity failure. | Preserve diagnostics without sensitive data and rerun after repair. |

`READY` must never be translated automatically into `ALLOW`, release approval, a final `ReleaseManifest`, or `PUBLISHED`.

### Illustrative receipt fragment

> [!CAUTION]
> The example is non-authoritative and schema-free at the current evidence boundary. Field names and enums require an accepted contract and schema before implementation.

```yaml
schema_version: PROPOSED-kfm.publish.fauna-readiness.v0
adapter_run_id: fauna_publish_readiness_<deterministic-or-run-id>
outcome: HELD
candidate:
  release_candidate_ref: <stable-reference>
  candidate_digest: <sha256>
  parent_lineage_refs: []
scope:
  object_families: []
  spatial_scope_ref: null
  temporal_scope_ref: null
support:
  source_descriptor_refs: []
  evidence_bundle_refs: []
  validation_report_refs: []
  policy_decision_refs: []
  review_record_refs: []
  representation_receipt_refs: []
checks:
  identity_closed: false
  time_scope_closed: false
  source_role_closed: false
  rights_closed: false
  sensitivity_closed: false
  evidence_closed: false
  review_closed: false
  public_representation_closed: false
  manifest_inputs_closed: false
  correction_path_closed: false
  rollback_target_closed: false
  trust_membrane_preserved: false
blockers: []
handoff:
  release_authority_ref: null
  manifest_input_ref: null
  readiness_report_ref: null
```

### Prohibited outputs and side effects

The adapter must not emit or mutate:

- final release approvals or final `ReleaseManifest` records;
- `PUBLISHED` lifecycle state;
- EvidenceBundles, policy decisions, or review approvals;
- exact sensitive-location content in logs, blockers, receipts, summaries, or diagnostics;
- public tiles, APIs, maps, exports, indexes, AI answers, or deployment state;
- correction closure or rollback execution.

[Back to top](#top)

---

<a id="validation"></a>

## Validation

Implementation is not ready until repository-owned contracts, schemas, fixtures, validators, and tests prove both positive and negative behavior. Documentation alone is not validation evidence.

### Gate sequence

Every adapter run must check or fail closed on:

1. **Caller authority** — the release steward, accepted Fauna publish lane, or approved drill scope is explicit.
2. **Candidate lifecycle** — the candidate is at an allowed readiness stage and has not skipped lifecycle phases.
3. **Object-family and identity closure** — Fauna types, stable identifiers, and crosswalks are unambiguous enough for release.
4. **Temporal closure** — observation, validity, processing, review, and release times are not collapsed.
5. **Source-role and rights closure** — authority limits, license, attribution, redistribution, and freshness are resolved.
6. **Sensitivity closure** — exact sensitive occurrences and sites fail closed; restricted fields cannot leak.
7. **Evidence closure** — required `EvidenceRef` values resolve to admissible `EvidenceBundle` support.
8. **Validation and receipt closure** — required transform, redaction, representation, and artifact checks resolve.
9. **Review closure** — materiality-appropriate review and separation of duties are present.
10. **Public-representation closure** — only the approved digest-linked public-safe derivative can proceed.
11. **Manifest-input integrity** — candidate inputs are complete, content-addressed, and internally consistent.
12. **Correction and rollback closure** — correction route, invalidation scope, and rollback target resolve.
13. **Trust-membrane closure** — public clients remain downstream of governed interfaces and released artifacts.
14. **No-side-effect closure** — readiness evaluation cannot release, publish, deploy, or change public serving.

### Fauna sensitivity and public-representation rules

Fauna publication is fail closed where exposure could harm wildlife, protected sites, stewards, landowners, or controlled monitoring programs.

- Exact sensitive occurrence, nest, den, roost, hibernaculum, spawning, lek, telemetry, and steward-controlled location data is denied from ordinary public outputs.
- A public derivative requires the applicable approved generalization, redaction, aggregation, delay, restriction, or withholding decision and digest-linked receipt chain.
- The adapter must validate the derivative's lineage without copying restricted input into public logs or reports.
- Missing or ambiguous rights, sensitivity, transformation, review, or release state produces `HELD` or `DENIED`, never implied permission.
- Generated prose must not reconstruct, infer, or reintroduce redacted geometry.

### Required test matrix for future implementation

| Test family | Minimum proof burden |
|---|---|
| Fixture-only dry run | Runs without live network access, credentials, or restricted data. |
| Valid public-safe candidate | Returns `READY` and performs no release mutation. |
| Missing evidence | Returns `HELD`; no claim or artifact is promoted. |
| Rights unresolved | Returns `HELD` or `DENIED` according to the supplied governing decision. |
| Sensitive exact location | Returns `DENIED`; logs and receipts contain no restricted coordinates. |
| Missing representation receipt | Blocks a derived public artifact. |
| Aggregator-as-authority attempt | Blocks unsupported legal or conservation-status authority. |
| Ambiguous taxon identity | Returns `HELD`; no identity is guessed. |
| Stale or superseded support | Blocks or reports stale state according to policy. |
| Missing review | Returns `HELD` when materiality requires independent review. |
| Digest or lineage mismatch | Returns `ERROR` or `HELD` according to the accepted contract; never proceeds. |
| Missing correction or rollback support | Returns `HELD`. |
| Trust-membrane bypass attempt | Fails closed. |
| Release/public-serving side-effect attempt | Fails and proves no final manifest, release state, deployment, or public artifact changed. |
| Deterministic replay | Identical governed inputs produce stable decisions and receipt content except explicitly permitted run metadata. |

### Fixture posture

- Default to synthetic, public-safe, no-network fixtures.
- Do not copy exact sensitive wildlife locations, private land context, credentials, or rights-restricted payloads into fixtures.
- Keep valid, invalid, held, denied, and error cases distinct.
- Preserve source-role, temporal, sensitivity, and digest relationships needed to exercise real boundaries.
- The confirmed [`fixtures/domains/fauna/README.md`](../../../fixtures/domains/fauna/README.md) and [`tests/domains/fauna/README.md`](../../../tests/domains/fauna/README.md) provide the current domain-level context. Exact future publish-adapter test and fixture leaf placement remains **NEEDS VERIFICATION**.

### Documentation checks for this README

- one H1 and coherent heading hierarchy;
- unique explicit anchors and working quick-navigation links;
- repository-relative links resolve at the reviewed commit;
- prospective files and behavior remain labeled `PROPOSED`, `UNKNOWN`, or `NEEDS VERIFICATION`;
- no exact sensitive locations, credentials, private data, or rights-restricted content is introduced;
- the diff is limited to this README;
- broad pull-request workflows are reported separately from document-specific validation.

> [!NOTE]
> The repository's broad pull-request workflows may run for a documentation-only change. At the reviewed snapshot, `link-check.yml`, `docs-build.yml`, and `domain-fauna.yml` describe explicit holds or incomplete validation surfaces. A green job name must not be treated as proof that links, Fauna publish behavior, or release readiness were validated.

[Back to top](#top)

---

<a id="review-burden"></a>

## Review burden

Changes to this lane should be reviewed proportionally to what they claim or implement.

| Change | Minimum review roles |
|---|---|
| README clarification only | Pipeline owner or docs steward; Fauna steward for domain meaning. |
| Adapter behavior or receipt fields | Pipeline owner, Fauna domain steward, evidence steward, and contract/schema owner. |
| Rights, sensitivity, geoprivacy, or public-representation logic | Fauna domain steward, sensitivity reviewer, policy steward, and rights owner where applicable. |
| Manifest-input or release handoff behavior | Release steward plus the owners above that match the affected trust surfaces. |
| Sensitive or material release candidate | Independent release approval according to governing separation-of-duties rules. |

Repository `CODEOWNERS` currently routes `pipelines/` review to `@bartytime4life`. That routing is not a `StewardshipAssignment`, `ReviewRecord`, policy decision, release approval, or proof of independent review.

### Required handoff record

A reviewable adapter change should identify:

- exact changed paths and pinned base/head commits;
- contracts, schemas, policies, fixtures, tests, and workflows affected;
- finite outcomes and blocker behavior;
- evidence, rights, sensitivity, public-representation, and no-leak implications;
- correction and rollback impact;
- validation performed, not run, pending, or unknown;
- the release authority that remains outside this lane.

[Back to top](#top)

---

<a id="related-folders"></a>

## Related folders

The links below were confirmed at the reviewed repository snapshot.

| Relationship | Repository documentation |
|---|---|
| Pipelines root authority | [`pipelines/README.md`](../../README.md) |
| Shared publish-readiness lane | [`pipelines/publish/README.md`](../README.md) |
| Primary Fauna pipeline lane | [`pipelines/domains/fauna/README.md`](../../domains/fauna/README.md) |
| Declarative pipeline-spec root | [`pipeline_specs/README.md`](../../../pipeline_specs/README.md) |
| Fauna pipeline-spec context | [`pipeline_specs/fauna/README.md`](../../../pipeline_specs/fauna/README.md) |
| Fauna domain architecture | [`docs/domains/fauna/ARCHITECTURE.md`](../../../docs/domains/fauna/ARCHITECTURE.md) |
| Fauna domain policy | [`policy/domains/fauna/README.md`](../../../policy/domains/fauna/README.md) |
| Fauna sensitivity policy | [`policy/sensitivity/fauna/README.md`](../../../policy/sensitivity/fauna/README.md) |
| Fauna fixtures | [`fixtures/domains/fauna/README.md`](../../../fixtures/domains/fauna/README.md) |
| Fauna tests | [`tests/domains/fauna/README.md`](../../../tests/domains/fauna/README.md) |
| Fauna release candidates | [`release/candidates/fauna/README.md`](../../../release/candidates/fauna/README.md) |
| Release manifests | [`release/manifests/README.md`](../../../release/manifests/README.md) |
| Fauna catalog records | [`data/catalog/domain/fauna/README.md`](../../../data/catalog/domain/fauna/README.md) |
| Fauna published layers | [`data/published/layers/fauna/README.md`](../../../data/published/layers/fauna/README.md) |
| EvidenceBundle proofs | [`data/proofs/evidence_bundle/README.md`](../../../data/proofs/evidence_bundle/README.md) |

### Doctrine and standards

- [`Directory Rules`](../../../docs/doctrine/directory-rules.md) — placement, responsibility roots, README contract, and domain placement law.
- [`Lifecycle Law`](../../../docs/doctrine/lifecycle-law.md) — lifecycle and governed-promotion boundary.
- [`Release Discipline`](../../../docs/architecture/release-discipline.md) — release authority and review posture.
- [`ReleaseManifest standard`](../../../docs/standards/RELEASE_MANIFEST.md) — manifest semantics and release boundary.

[Back to top](#top)

---

<a id="adrs-and-placement-decisions"></a>

## ADRs and placement decisions

The bounded repository inspection did not establish a target-specific accepted ADR that makes `pipelines/publish/fauna/` the permanent home for full Fauna publish behavior.

Current decision posture:

- `pipelines/` is the confirmed responsibility root for executable pipeline logic.
- `pipelines/domains/fauna/` is the confirmed domain pipeline lane.
- `pipelines/publish/fauna/` remains a thin shared-readiness adapter/profile lane.
- the exact declarative configuration path and schema-backed receipt contract remain **NEEDS VERIFICATION**;
- expansion into primary domain behavior, release authority, or a parallel contract/schema/policy/receipt home requires a placement decision and may require an ADR or migration record.

Use the [`docs/adr/` index](../../../docs/adr/README.md) and re-run a repository-wide accepted-ADR inspection before adding executable files or authority-bearing contracts.

### Open decisions

| ID | Question | Status | Resolution evidence needed |
|---|---|---|---|
| `PIPE-PUBLISH-FAUNA-001` | Should this remain a shared adapter or move under the primary Fauna domain lane when executable behavior begins? | NEEDS VERIFICATION / ADR review | Accepted placement decision plus migration plan if moved. |
| `PIPE-PUBLISH-FAUNA-002` | What exact declarative profile path owns Fauna publish-readiness configuration? | NEEDS VERIFICATION | Directory Rules, adjacent `pipeline_specs/fauna/` convention, and accepted ADR. |
| `PIPE-PUBLISH-FAUNA-003` | Which contract and schema own readiness outcomes, blockers, and receipt fragments? | UNKNOWN | Accepted semantic contract, schema, validator, fixtures, and compatibility plan. |
| `PIPE-PUBLISH-FAUNA-004` | Which test and fixture leaves own adapter-specific cases? | NEEDS VERIFICATION | Current tree inspection plus owning README/ADR evidence. |
| `PIPE-PUBLISH-FAUNA-005` | Which CI job owns adapter invariant tests? | UNKNOWN | Command-bearing workflow and stable required-check decision. |
| `PIPE-PUBLISH-FAUNA-006` | Which source-role, rights, sensitivity, and representation receipt vocabularies are canonical? | NEEDS VERIFICATION | Accepted policy/contract/schema references and negative tests. |
| `PIPE-PUBLISH-FAUNA-007` | What deterministic identifier and canonicalization rules govern adapter receipts? | UNKNOWN | Accepted receipt contract, hash profile, and replay tests. |

[Back to top](#top)

---

## Correction and rollback

### Documentation correction

If this README overstates implementation or misstates a trust boundary:

1. open a focused correction PR;
2. identify the unsupported claim and the pinned evidence that corrects it;
3. update version, date, related links, and open decisions as needed;
4. preserve any required supersession or correction lineage;
5. re-run link, structure, sensitivity, and no-loss checks.

### Adapter rollback posture

Future adapter behavior must not be considered complete until it can:

- identify the last known-good implementation and configuration digests;
- invalidate affected readiness receipts without rewriting history;
- prevent stale `READY` results from being reused after an upstream correction;
- hand a resolvable rollback target to release authority;
- prove that rollback does not expose restricted Fauna content or bypass review.

Before merge, repository rollback is a transparent revert of the scoped commit or closure of the unmerged PR. After merge, use a revert commit or revert PR; do not rewrite shared history.

[Back to top](#top)

---

## Definition of done

This README revision is complete when it:

- preserves the adapter's narrow publish-readiness purpose and separate release authority;
- states the current evidence boundary and avoids claiming executable depth;
- follows the Directory Rules folder-README contract;
- separates primary Fauna domain logic, declarative specs, contracts, schemas, policy, fixtures, tests, evidence, release decisions, and public serving into their owning roots;
- defines fail-closed evidence, rights, sensitivity, review, public-representation, correction, rollback, and trust-membrane gates;
- distinguishes proposed finite readiness outcomes from canonical schema claims;
- links only to repository paths confirmed at the reviewed snapshot;
- records unresolved placement, receipt, test, fixture, and CI questions;
- introduces no sensitive locations, restricted payloads, credentials, release mutation, or public behavior change.

Future implementation is done only when accepted contracts and schemas, public-safe no-network fixtures, positive and negative tests, deterministic receipts, CI ownership, review separation, release handoff, correction, rollback, and remote verification all exist and pass.

[Back to top](#top)

---

<a id="last-reviewed"></a>

## Last reviewed

| Field | Value |
|---|---|
| Date | 2026-07-22 |
| Document version | v0.2 |
| Status | DRAFT |
| Repository evidence base | `main` at `8db841822c111cb5b6477003dc72f0455f6c41ad` |
| Placement basis | Directory Rules §§4, 7.4, 12, 15, and 16 |
| Implementation depth | UNKNOWN |
| Release/publication impact | None; documentation-only readiness contract |
| Next review trigger | Accepted placement ADR, first executable adapter file, receipt contract/schema adoption, test-lane decision, or material Fauna publication-policy change |

### Maintenance checklist

- [ ] Confirm owner and steward placeholders.
- [ ] Re-check accepted ADRs and drift entries before adding files.
- [ ] Confirm the exact declarative profile, test, fixture, and receipt paths.
- [ ] Replace proposed outcomes and fields only after contract/schema adoption.
- [ ] Keep sensitive-location handling fail closed and test negative paths.
- [ ] Verify every related link and implementation claim at the new pinned commit.
- [ ] Update this README when behavior, validation, review, correction, or rollback responsibilities change.

[Back to top](#top)
