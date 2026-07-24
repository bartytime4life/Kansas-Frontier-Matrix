<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/examples/focus-flows/readme
title: `examples/focus_flows/` — Governed Focus Flow Examples
type: readme; nested-example-lane; non-authoritative-demonstration-boundary
version: v0.2.0
status: repository-grounded draft; STATIC_WALKTHROUGH; non-authoritative; validation-bounded; do-not-publish
owners: NEEDS VERIFICATION — examples steward and listed specialist reviewers
updated: 2026-07-24
supersedes: v0.1.x content at the same path; no operational object, runtime behavior, release, or publication state
prepared_under_prompt: KFM Markdown Engineering, Modernization & GitHub Documentation Implementation Agent v5.0.0
policy_label: public-review; synthetic-first; fail-closed; cite-or-abstain; correction-aware
current_path: examples/focus_flows/README.md
review_packet_id: kfm-md-examples-wave-20260724
truth_posture: >
  CONFIRMED exact path, prior blob, current parent examples contract, complete prior file,
  and referenced repository boundaries / PROPOSED normalized lane contract and future
  example-validator profile / UNKNOWN executable child payloads, runtime parity, deployed
  consumers, and production effects / NEEDS VERIFICATION owners, accepted schemas,
  validators, fixtures, CI, host rendering, correction propagation, and retirement drills
evidence_snapshot:
  repository: bartytime4life/Kansas-Frontier-Matrix
  base_commit: fe9442ef01ed676e11ccea2796c6fe4090dd1e7e
  prior_blob: 3f3ab032b323f2a850e5b131a847f9a32e10b2fb
  parent_examples_blob: d3fbce80c82106935288d59a708bbb1a0118591e
  inventory_method: complete target read plus bounded linked-file evidence; no example execution or runtime inspection
notes:
  - "The first twelve H2 sections follow Directory Rules section 15 exactly."
  - "This change is Markdown only and does not create a fixture, test, schema, policy, proof, receipt, route, release, or publication state."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `examples/focus_flows/` — Governed Focus Flow Examples

> **One-line purpose.** Teach the request → policy → evidence → adapter → citation → policy → finite-envelope flow, including safe negative states and Evidence Drawer handoffs.

[![Status: static walkthrough](https://img.shields.io/badge/status-STATIC__WALKTHROUGH-f59e0b?style=flat-square)](#status)
[![Authority: example only](https://img.shields.io/badge/authority-example%20only-b42318?style=flat-square)](#authority-level)
[![Publication: denied](https://img.shields.io/badge/publication-denied-b42318?style=flat-square)](#what-does-not-belong-here)
[![Truth: cite or abstain](https://img.shields.io/badge/truth-cite%20or%20abstain-1a7f37?style=flat-square)](#validation)

> [!IMPORTANT]
> `examples/` is canonical for demonstrations, not for the objects or behavior demonstrated. A polished file, merged pull request, parser pass, or screenshot does not prove source authority, runtime parity, evidence closure, policy permission, release approval, or KFM publication.

**Quick navigation:** [Purpose](#purpose) · [Authority](#authority-level) · [Status](#status) · [Belongs](#what-belongs-here) · [Exclusions](#what-does-not-belong-here) · [Inputs](#inputs) · [Outputs](#outputs) · [Validation](#validation) · [Review](#review-burden) · [Related](#related-folders) · [ADRs](#adrs) · [Last reviewed](#last-reviewed) · [Contract](#example-contract) · [Guardrails](#guardrails) · [Inventory](#current-bounded-inventory) · [Verification](#open-verification-register) · [No-loss](#no-loss-ledger)

## Purpose

Teach the request → policy → evidence → adapter → citation → policy → finite-envelope flow, including safe negative states and Evidence Drawer handoffs.

This lane exists to make review and learning faster. It must not become a parallel contract, schema, policy, fixture, test, proof, receipt, source registry, runtime, release, or publication authority.

## Authority level

**Non-authoritative example lane; runtime behavior belongs to the governed API, explorer UI, policy, evidence resolver, and AI adapter.**

Operational meaning remains owned by the relevant `docs/`, `contracts/`, `schemas/`, `policy/`, implementation, `tests/`, `fixtures/`, `data/`, and `release/` surfaces.

## Status

| Field | Bounded result |
|---|---|
| Path | `examples/focus_flows/README.md` |
| Version | `v0.2.0` |
| Maturity | `STATIC_WALKTHROUGH` |
| Prior blob | `3f3ab032b323f2a850e5b131a847f9a32e10b2fb` |
| Recursive payload inventory | `UNKNOWN` beyond the bounded inventory below |
| Executable entrypoint / observed run | `NOT ESTABLISHED` |
| Public/release readiness | `DENY BY PLACEMENT` |

## What belongs here

- synthetic FocusModeRequest-like sketches
- `ANSWER`, `ABSTAIN`, `DENY`, and `ERROR` walkthroughs
- Evidence Drawer handoff examples
- policy-denial, stale-evidence, citation-failure, and adapter-error demonstrations
- accessibility and non-color trust-state notes

Every new file must be visibly synthetic or safely transformed, name its learning objective, identify the operational home it does not replace, and declare its expected finite outcome.

## What does NOT belong here

| Do not place here | Correct home or action |
|---|---|
| route handlers, DTOs, middleware, model adapters, or production responses | `apps/governed-api/`, `apps/explorer-web/`, packages, tests, and fixtures |
| model prompts, hidden reasoning, provider transcripts, or raw model output | governed runtime/receipt lanes where policy permits |
| operational EvidenceBundles, AIReceipts, policy decisions, or release records | `data/proofs/`, `data/receipts/`, `policy/`, and `release/` |
| direct reads from RAW, WORK, QUARANTINE, internal stores, or model runtimes | forbidden; use governed interfaces |
| restricted detail or reconstructive redaction clues | synthetic/generalized example or `DENY` |

## Inputs

Synthetic map/time/layer context, example evidence references, finite policy states, and current architecture documents.

Input provenance, real-versus-synthetic status, rights, sensitivity, and the operational object being illustrated must be explicit.

## Outputs

Static flow walkthroughs and synthetic finite response sketches; never runtime responses.

Outputs may be reviewed, corrected, or proposed for separate fixture/test graduation. They do not become operational merely by being copied.

## Validation

- Confirm the browser path goes through the governed API and never directly to a model or internal store.
- Confirm missing/stale/conflicting/citation-invalid evidence yields `ABSTAIN`.
- Confirm rights/sensitivity/role prohibition yields `DENY` or a safe generalized alternative.
- Confirm schema/adapter/resolver/runtime failure yields `ERROR` without claim leakage.
- Validate links, Mermaid, example markers, and accessibility labels.

No examples-specific runner or complete validator was verified. A Markdown/source check proves only the declared static scope.

## Review burden

Examples/docs plus governed API, governed AI, policy, evidence, UI, and affected domain reviewers.

CODEOWNERS routing is not stewardship, approval evidence, policy permission, or release authorization.

## Related folders

- [Parent examples contract](../README.md)
- [Hydrology walkthrough](hydrology_huc12_question.md)
- [Focus Flow doctrine](../../docs/architecture/governed-ai/FOCUS_FLOW.md)
- [Governed API doctrine](../../docs/architecture/governed-api.md)
- [Evidence Drawer](../../docs/architecture/ui/EVIDENCE_DRAWER.md)

## ADRs

Relevant proposed decisions include ADR-0004, ADR-0019, ADR-0020, ADR-0025, ADR-0027, and ADR-0028. None is promoted by this example lane.

## Last reviewed

- **Date:** 2026-07-24
- **Evidence boundary:** `main@fe9442ef01ed676e11ccea2796c6fe4090dd1e7e`
- **Method:** complete target read plus bounded linked-file verification
- **Execution/runtime inspection:** not performed
- **Human review:** pending

Re-review when an example is added, made runnable, mirrored into fixtures/tests, invalidated by an operational contract, or affected by rights/sensitivity/release changes.

## Example contract

Every consequential example must declare:

```yaml
example: true
authority: non_authoritative_example
do_not_publish: true
maturity: STATIC_WALKTHROUGH
real_vs_synthetic: explicit
expected_outcome: ANSWER | ABSTAIN | DENY | ERROR | HOLD | QUARANTINE | NOT_APPLICABLE
operational_home: "<verified owning root or NEEDS VERIFICATION>"
validation_boundary: "<exact checks performed>"
correction_trigger: "<contract, policy, source, runtime, or release change>"
```

`ANSWER` requires support appropriate to the scenario. Missing, stale, conflicting, or citation-invalid evidence yields `ABSTAIN`; prohibited rights/sensitivity/role exposure yields `DENY` or `HOLD`; tool/schema/runtime failure yields `ERROR`.

## Guardrails

| Risk | Guardrail |
|---|---|
| Browser-to-model shortcut | Every flow uses the governed API. |
| Example becomes runtime response | Use visible non-authority markers and synthetic IDs. |
| Policy is skipped | Represent precheck and postcheck for claim-bearing or sensitive scenarios. |
| Prompt or reasoning leaks | Exclude chain-of-thought, raw prompts, provider transcripts, and private evidence. |

## Current bounded inventory

`hydrology_huc12_question.md` is the only verified child walkthrough in this lane.

Omission is not evidence of absence, retirement, or permission to create speculative children.

## Open verification register

| Item | Status | Required evidence |
|---|---:|---|
| Recursive subtree and non-Markdown inventory | `UNKNOWN` | Pinned tree and file classification |
| Runnable entrypoints and dependency closure | `UNKNOWN` | Manifests, locks, commands, no-network inputs, observed runs |
| Schema/contract conformance | `NEEDS VERIFICATION` | Accepted versions and validation results |
| Examples-specific validation and CI | `NEEDS VERIFICATION` | Repository-owned validator, tests, fixtures, workflow |
| Host rendering and accessibility | `NEEDS VERIFICATION` | Render/browser inspection and accepted checks |
| Correction and retirement consumers | `NEEDS VERIFICATION` | Inbound references, owner, replacement, rollback |

## No-loss ledger

| Prior material | Disposition |
|---|---|
| Stable path and `doc_id` | Preserved |
| Non-authority and trust-membrane warnings | Preserved and strengthened |
| Accepted material and exclusions | Preserved and normalized |
| Finite outcomes and fail-closed behavior | Preserved |
| Domain/source-role/sensitivity guardrails | Preserved |
| Lifecycle and operational-home separation | Preserved |
| Prior evidence ledger and limitations | Consolidated into current evidence/verification sections |
| Speculative child trees | Removed as proposals; no child is retired by omission |
| Operational payload, code, fixture, test, or release change | None |

### Change history

#### v0.2.0 — 2026-07-24

- normalized the first twelve H2 sections to the current folder contract;
- classified the lane as `STATIC_WALKTHROUGH`;
- preserved substantive boundaries, negative states, safety controls, and prior rollback identity;
- removed speculative tree pressure without treating unlisted files as absent;
- changed Markdown only.

<p align="right"><a href="#top">Back to top</a></p>
