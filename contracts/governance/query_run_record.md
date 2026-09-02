<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/query-run-record
title: QueryRunRecord Contract
type: contract
version: v1.0.0
status: proposed-inactive
owners: OWNER_TBD — Governance steward · Evidence steward · AI surface steward · Contract steward · Schema steward · Validation steward
created: 2026-08-06
updated: 2026-08-06
policy_label: internal; fixture-only; non-authoritative
related:
  - ../../schemas/contracts/v1/governance/query_run_record.schema.json
  - ../../fixtures/contracts/v1/governance/query_run_record/
  - ../../tools/validators/governance/validate_query_run_record.py
  - ../../tests/validators/governance/test_query_run_record.py
  - ./ai_change_proposal.md
  - ../../packages/hashing/src/hashing/core.py
  - ../../docs/doctrine/ai-build-operating-contract.md
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, governance, query-run, evidence-resolution, finite-outcomes, deterministic-identity, control-loop, fixture-only]
notes:
  - "This profile records a public-safe query summary, evidence-resolution projection, candidate AIChangeProposal references, finite outcome, and deterministic hashes."
  - "It stores no raw prompt, private chain-of-thought, model output, secret, source payload, policy decision, human approval, or repository mutation."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# QueryRunRecord Contract

> **Purpose.** Define a deterministic, reviewable, non-authoritative record for one scoped KFM query iteration without turning query history, generated language, or candidate proposals into evidence or mutation authority.

## Status and boundary

| Field | Value |
|---|---|
| Contract status | `PROPOSED_INACTIVE` |
| Execution mode | `FIXTURE_ONLY` |
| Authority created | `NONE` |
| Target lifecycle stage | `WORK` only |
| Public use | denied |
| Machine shape | `schemas/contracts/v1/governance/query_run_record.schema.json` |
| Validator | `tools/validators/governance/validate_query_run_record.py` |
| Current live integration | none |

A passing record proves only that its declared query summary, evidence-resolution projection, candidate proposal references, finite outcome, hashes, and no-effect boundary agree with this profile. It does not prove that evidence was actually resolved, policy ran, a reviewer approved work, a proposal should be applied, or any lifecycle/release/publication transition is authorized.

## Source adaptation and repository fit

The Pipeline Living Implementation Manual proposes a governed `query -> save -> validate -> compile -> review -> promote -> recompile` loop and names `QueryRunRecord`, `CandidateDelta`, and `RecompileManifest` as control-loop records. Current repository evidence already supplies a fixture-only `AIChangeProposal` object that safely represents a candidate deterministic change. This slice therefore adds only the missing query-run record and references `AIChangeProposal` identifiers instead of creating a parallel `CandidateDelta` authority.

The later recompile-manifest/compiler slice remains separate because it introduces output-path, rollback-target, and derived-artifact behavior that deserves its own review boundary.

## Directory Rules basis

Accepted ADR-0029 makes Directory Rules v2 the placement authority. `QueryRunRecord` is a governance/audit object, so semantic meaning belongs under `contracts/governance/`; machine shape under `schemas/contracts/v1/governance/`; synthetic examples under `fixtures/contracts/v1/governance/`; executable validation under `tools/validators/governance/`; focused proof under `tests/validators/governance/`; CI under `.github/workflows/`; and AI authoring provenance under `data/receipts/generated/`.

No new root, lifecycle phase, candidate-delta family, policy authority, evidence store, receipt store, release home, or publication path is introduced.

## Object meaning

A `QueryRunRecord` binds the following concerns without collapsing their authority:

1. **Public-safe query summary** — bounded purpose text, not the raw prompt or private reasoning.
2. **Scope** — domain, geography, time reference, and risk class.
3. **Allowed evidence classes** — a finite allowlist for the query context.
4. **Evidence-resolution projection** — requested `EvidenceRef` values and declared `RESOLVED`, `UNRESOLVED`, `DENIED`, `CONFLICTED`, or `ERROR` states.
5. **Candidate proposal references** — zero or more existing `kfm:ai-change-proposal:<digest>` identifiers; the record does not embed or apply their patches.
6. **Finite result** — `ANSWER`, `ABSTAIN`, `DENY`, or `ERROR` derived from the evidence-resolution summary.
7. **Deterministic identity** — RFC 8785 JCS + SHA-256 hashes over query, context, output, specification, and concrete run projections.
8. **No-effect boundary** — target stage `WORK`, all permissions false, and an exact non-effects declaration.

## Raw-content exclusion

The closed schema deliberately has no member for `raw_query`, `prompt`, `system_prompt`, `model_output`, `chain_of_thought`, credentials, source bytes, or unrestricted metadata. Unknown members fail schema validation. The `query_summary` is single-line, bounded, and intended to contain only the auditable purpose of the iteration.

Schema closure prevents these fields from being added to the object. It does not inspect human meaning inside an allowed string, so reviewer and source-handling obligations still apply.

## Evidence-resolution semantics

Each item binds one `EvidenceRef` to one declared status. Only `RESOLVED` items may carry an `EvidenceBundle` reference.

| Item states | Required summary | Finite outcome |
|---|---|---|
| every item `RESOLVED` | `COMPLETE` | `ANSWER` |
| at least one `UNRESOLVED`, and none denied/conflicted/errored | `PARTIAL` | `ABSTAIN` |
| at least one `CONFLICTED`, and none denied/errored | `CONFLICTED` | `ABSTAIN` |
| at least one `DENIED`, and none errored | `DENIED` | `DENY` |
| at least one `ERROR` | `ERROR` | `ERROR` |

Precedence is `ERROR > DENIED > CONFLICTED > PARTIAL > COMPLETE`. Evidence items and references are canonical, unique, and sorted. The validator checks declaration consistency only; it does not dereference any identifier.

## Reason-code derivation

A valid record carries exactly four sorted codes:

- `FIXTURE_ONLY`;
- `QUERY_VALIDATED`;
- one evidence result code; and
- `CANDIDATE_PROPOSED` or `NO_CANDIDATE_DELTA`.

A candidate reference does not strengthen the evidence outcome or grant permission to apply the candidate.

## Deterministic identity

The repository hashing package supplies RFC 8785 canonicalization and SHA-256.

```text
query_hash   = SHA-256(JCS(actor_class + query_summary + scope))
context_hash = SHA-256(JCS(allowed_evidence_classes + evidence_resolution))
output_hash  = SHA-256(JCS(candidate_proposal_refs + outcome + reason_codes))
spec_hash    = SHA-256(JCS(profile boundary + query/context/output hashes + permissions + non_effects))
run_hash     = SHA-256(JCS(created_at + query/context/output/spec hashes))
query_run_id = "kfm:query-run:" + hex(run_hash)
```

`created_at` distinguishes concrete executions; `query_hash` groups repeated scopes; `context_hash` exposes evidence-context drift; `output_hash` binds the finite result and candidate links. These hashes support integrity and replay. They do not prove truth.

## Validator outcomes

| Outcome | Meaning |
|---|---|
| `PASS` | Shape, ordering, evidence summary, finite outcome, reason codes, hashes, identity, and no-effects agree. |
| `DENY` | The record is contradictory, non-canonical, hash-invalid, over-authoritative, or otherwise nonconforming. |
| `ERROR` | The input could not be read or parsed safely. |

A `PASS` creates no evidence, approval, mutation, or release authority.

## Validation

```bash
python -m unittest discover \
  --start-directory tests/validators/governance \
  --pattern 'test_query_run_record.py' \
  --verbose

python tools/validators/governance/validate_query_run_record.py --fixtures
```

## Trust boundary

This profile does not:

- call an AI model or save private reasoning;
- retrieve, resolve, admit, or authenticate evidence or sources;
- evaluate policy or create a review record;
- apply `AIChangeProposal` operations;
- write Git, GitHub, a database, object store, or KFM lifecycle stage;
- promote, release, deploy, publish, or authorize public use;
- replace `EvidenceBundle`, `PolicyDecision`, `ReviewRecord`, `RunReceipt`, `RecompileManifest`, `PromotionDecision`, `ReleaseManifest`, correction, or rollback objects.

## Rollback

The implementation is additive and fixture-only. Before merge, close the draft pull request and remove its branch. After an authorized merge, revert the implementation commit or merge commit. No source deactivation, data migration, lifecycle reprocessing, cache purge, release withdrawal, or public correction is required.
