<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/contracts-story-readme
title: contracts/story — Story Contract Semantics README
type: readme
version: v0.1
status: draft; PROPOSED; semantic-contract-lane; narrative-boundary; evidence-dependent; no-sovereign-truth
owners: OWNER_TBD — Story steward · Contracts steward · Evidence steward · Policy steward · Release steward · Governed-AI steward · Docs steward · Directory Rules reviewer
created: NEEDS VERIFICATION — stub existed before v0.1 expansion
updated: 2026-06-24
policy_label: public; contracts; story; semantic-contracts; narrative; evidence-dependent; citation-required; release-gated; no-ai-truth; no-publication-authority
tags: [kfm, contracts, story, narrative, README, semantic-contracts, evidence, citation, focus-mode, governed-ai, runtime-response, publication, review, rollback]
related:
  - ../README.md
  - ../evidence/
  - ../runtime/runtime_response_envelope.md
  - ../runtime/ai_receipt.md
  - ../policy/policy_decision.md
  - ../release/release_manifest.md
  - ../../schemas/contracts/v1/story/
  - ../../policy/story/
  - ../../docs/architecture/governed-ai/FOCUS_FLOW.md
  - ../../docs/architecture/contract-schema-policy-split.md
  - ../../fixtures/contracts/v1/story/
  - ../../tests/contracts/story/
notes:
  - "Expanded from the short stub at `contracts/story/README.md`."
  - "Repo search in this session did not find an existing mature story contract family or paired story schema; this README therefore defines a PROPOSED guarded semantic lane."
  - "Contracts root documentation says contracts define semantic meaning and exclude executable validation, JSON Schema, policy code, and source data."
  - "Governed AI focus-flow doctrine requires finite outcomes and evidence/policy/citation/receipt/runtime-envelope artifacts before answer text is rendered."
  - "Story contracts must never turn narrative text, generated summaries, UI copy, map callouts, focus-mode build plans, or AI answers into sovereign truth."
  - "Rollback target for this expansion is previous stub blob SHA `450a06fa317c434fefc503726c48262134850187`."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# contracts/story

> Proposed semantic-contract lane for KFM story and narrative presentation objects. Story objects may organize released, cited, policy-safe evidence into human-readable sequences, but they do not create evidence, validate claims, approve release, make AI output true, or grant public access to restricted material.

<p>
  <img alt="Status: proposed" src="https://img.shields.io/badge/status-PROPOSED-yellow">
  <img alt="Root: contracts/story" src="https://img.shields.io/badge/root-contracts%2Fstory-blue">
  <img alt="Purpose: semantic meaning" src="https://img.shields.io/badge/purpose-semantic__meaning-blueviolet">
  <img alt="Evidence: required" src="https://img.shields.io/badge/evidence-required-0a7ea4">
  <img alt="Boundary: narrative not truth" src="https://img.shields.io/badge/boundary-narrative__not__truth-critical">
</p>

**Status:** draft / PROPOSED  
**Path:** `contracts/story/README.md`  
**Owning root:** `contracts/` — semantic meaning only  
**Schema home:** `schemas/contracts/v1/story/` — PROPOSED / NEEDS VERIFICATION  
**Policy home:** `policy/story/` or relevant policy-family roots — PROPOSED / NEEDS VERIFICATION  
**Evidence dependency:** `EvidenceBundle`, `EvidenceRef`, citation validation, release/review state, and policy decisions must remain upstream  
**Truth posture:** CONFIRMED target was a short stub · CONFIRMED no existing mature story contract family or story schema was found by repo search in this session · CONFIRMED contracts root owns semantic meaning and excludes schemas/policy/source data · CONFIRMED governed AI flow requires evidence, policy, citation validation, AIReceipt, and RuntimeResponseEnvelope for answer text · PROPOSED guarded lane until object names, schemas, policy, fixtures, tests, and release behavior are accepted

## Quick jumps

[Purpose](#purpose) · [Story object meaning](#story-object-meaning) · [Authority split](#authority-split) · [Candidate object families](#candidate-object-families) · [Accepted contents](#accepted-contents) · [Exclusions](#exclusions) · [Invariants](#invariants) · [Validation expectations](#validation-expectations) · [Open questions](#open-questions) · [Rollback](#rollback)

---

## Purpose

`contracts/story/` is a proposed home for semantic contracts that describe narrative or story-oriented presentation objects.

A story object may help KFM answer questions such as:

- which released/cited evidence items appear in a narrative sequence;
- what map layers, time windows, claims, citations, and caveats are attached to a story section;
- how a public-safe explanatory sequence is assembled from governed records;
- which policy, review, redaction, and release gates constrain narrative display;
- how narrative text must expose uncertainty, source limitations, correction state, and rollback posture.

A story object must not answer:

- whether a claim is true without evidence;
- whether unpublished data can be shown;
- whether a sensitive location, living-person record, DNA/genomic inference, archaeological site, infrastructure-sensitive item, or culturally sensitive record can be exposed;
- whether a model-generated summary may stand as authority;
- whether release is approved.

---

## Story object meaning

A KFM story is not free-form persuasion. It is a governed presentation envelope over evidence, claims, citations, policy decisions, release state, correction state, and map/time context.

A mature flow should look like:

```text
EvidenceBundle / released artifact / catalog or triplet record
  -> policy + sensitivity + rights + review + release checks
  -> citation validation
  -> optional AI or editorial drafting with AIReceipt / ReviewRecord
  -> Story object / StorySection / StoryClaimRef
  -> RuntimeResponseEnvelope or published story artifact
  -> correction / withdrawal / rollback path
```

If evidence is missing, conflicted, stale, restricted, uncited, or not release-safe, the story surface must abstain, deny, generalize, or show a caveat rather than inventing narrative certainty.

---

## Authority split

| Responsibility | Correct home | Rule |
|---|---|---|
| Story object meaning | `contracts/story/` | Proposed Markdown semantic-contract lane only. |
| Evidence support | `contracts/evidence/`, EvidenceBundle/EvidenceRef roots | Evidence supports claims; stories consume evidence. |
| Machine shape | `schemas/contracts/v1/story/` or ADR-selected schema home | JSON Schema owns fields and validation. |
| Policy/admissibility | `policy/story/` plus rights/sensitivity/release policy roots | Policy decides what can be displayed or withheld. |
| AI drafting receipts | `contracts/runtime/ai_receipt.md`, runtime/receipt roots | AI is process memory, not root truth. |
| Runtime response | `contracts/runtime/runtime_response_envelope.md` | Runtime surfaces emit finite outcomes. |
| Release approval | `contracts/release/`, `release/` roots | Publication is a governed state transition. |
| Fixtures/tests | `fixtures/`, `tests/` | Enforceability stays outside contracts. |
| Public UI/map | governed UI/map/API roots | Public clients consume released/governed envelopes only. |

---

## Candidate object families

These candidate contract names are PROPOSED until schemas, policy, fixtures, tests, and owners are accepted.

| Candidate | Purpose | Status |
|---|---|---|
| `story.md` | Top-level story object: title, scope, audience, evidence/citation/release posture. | PROPOSED |
| `story_section.md` | Ordered narrative section with map/time/evidence refs. | PROPOSED |
| `story_claim_ref.md` | Reference to a claim supported by EvidenceBundle and citation validation. | PROPOSED |
| `story_map_callout.md` | Public-safe map annotation or callout tied to released layer/evidence refs. | PROPOSED |
| `story_timeline_event.md` | Time-aware event item with evidence, uncertainty, and correction state. | PROPOSED |
| `story_caveat.md` | Required caveat/uncertainty/sensitivity/release note for narrative surfaces. | PROPOSED |
| `story_revision.md` | Editorial/review/correction metadata for story updates. | PROPOSED |

Do not create these files as canonical facts without checking schema homes, policy homes, fixtures, tests, release behavior, and Directory Rules.

---

## Accepted contents

| Accepted content | Purpose | Guardrail |
|---|---|---|
| `README.md` | Defines story contract-lane boundary. | Must preserve no-sovereign-truth posture. |
| Story semantic contract Markdown | Defines meaning for a proposed story object. | Must cite schema/policy/release/evidence posture or mark NEEDS VERIFICATION. |
| `INDEX.md` | Optional inventory after accepted story contracts exist. | Must not list proposed files as implemented facts. |
| `MIGRATION.md` | Optional migration/backlink plan for story/narrative contracts. | Must identify rollback and source compatibility. |
| `BACKLINKS.md` | Optional stale-reference audit. | Must remain factual. |

---

## Exclusions

| Do not put this here | Correct home | Reason |
|---|---|---|
| Generated story text as authoritative content | released artifacts / governed editorial roots, with evidence and review | Contracts define meaning; they are not story payloads. |
| Evidence bundles or claim truth | evidence/catalog/triplet roots | Evidence supports story claims. |
| JSON Schema | `schemas/contracts/v1/story/` or accepted schema roots | Schemas own shape. |
| Policy rules | `policy/` roots | Policy owns display/admissibility decisions. |
| AI prompts, model outputs, chain-of-thought, model runtime traces | governed AI/runtime/receipt roots | AI output is downstream and receipt-bound. |
| Public UI components | UI/web/map roots | UI renders released/governed story surfaces. |
| Release manifests, correction notices, rollback cards | `release/` and release contracts | Release state is separate. |
| Fixtures/tests/validators | `fixtures/`, `tests/`, `tools/validators/` | Proof and validation stay outside contracts. |
| RAW/WORK/QUARANTINE data | data lifecycle roots | Stories must not read internal lifecycle stores directly. |

---

## Invariants

PROPOSED semantic invariants:

- Story text is never sovereign truth.
- Every substantive story claim must resolve to evidence, citation, policy, review, and release posture appropriate to its significance.
- If evidence is missing or citation validation fails, story surfaces must abstain or caveat instead of inventing claims.
- If policy denies display, story surfaces must deny, withhold, generalize, or redact without leaking restricted details.
- If a story is AI-drafted, an AIReceipt or equivalent process receipt must remain auditable.
- Public story surfaces must not read RAW, WORK, QUARANTINE, canonical/internal stores, or direct model runtime output.
- Correction, withdrawal, and rollback paths must be visible for published story artifacts.
- Story objects must preserve map/time context and not collapse time-validity into timeless narrative.

---

## Validation expectations

NEEDS VERIFICATION in implementation:

- accepted story object names and schema home;
- story schema required fields and closed-enum outcomes/caveats;
- policy/story package or integration with existing rights/sensitivity/release policy;
- fixtures for cited, uncited, denied, abstained, sensitive, corrected, withdrawn, and AI-drafted story cases;
- validators that require evidence/citation/policy/release refs for substantive claims;
- runtime/API/UI behavior for story display;
- release manifest integration for published story artifacts;
- correction and rollback behavior;
- editorial review and AIReceipt linkage.

---

## Open questions

- Should story contracts live under `contracts/story/`, `contracts/narrative/`, `contracts/focus_mode/`, or another accepted family?
- Should story objects be released artifacts, runtime response projections, or both?
- What is the minimal required evidence/citation surface for a `StoryClaimRef`?
- Which story content can be AI-drafted, and what review/receipt is required?
- How should story revisions bind to CorrectionNotice, WithdrawalNotice, and RollbackCard?

---

## Rollback

Rollback is required if this lane is used as evidence truth, source truth, release approval, policy authority, schema authority, public UI implementation, AI output storage, chain-of-thought storage, raw data storage, or a way to publish narrative claims without evidence, citation, review, policy, release, correction, and rollback posture.

Rollback target for this expansion: previous stub blob SHA `450a06fa317c434fefc503726c48262134850187`.

<p align="right"><a href="#top">Back to top</a></p>
