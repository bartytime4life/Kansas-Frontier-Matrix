<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/<TODO-uuid>
title: Trust Membrane
type: standard
subtype: doctrine
version: v1 (draft)
status: draft
contract_version: "3.0.0"
owners: <TODO: Docs steward + Architecture steward + Policy steward + AI surface steward (drawn from ai-build-operating-contract.md §0 reviewer pattern)>
created: 2026-05-12
updated: 2026-05-26
policy_label: public
related:
  - docs/doctrine/ai-build-operating-contract.md
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md
  - docs/doctrine/evidence-first.md
  - docs/doctrine/policy-aware.md
  - docs/doctrine/ai-as-assistant.md
  - docs/doctrine/authority-ladder.md
  - docs/doctrine/corrections-are-first-class.md
  - docs/doctrine/derived-stays-derived.md
  - docs/doctrine/trust-posture.md
  - docs/doctrine/truth-labels.md
  - docs/doctrine/evidence-model.md
  - docs/doctrine/map-first.md
  - docs/architecture/release-and-publication.md
  - docs/security/threat-model.md
  - schemas/contracts/v1/release_manifest.schema.json
  - schemas/contracts/v1/proof_pack.schema.json
  - schemas/contracts/v1/evidence_bundle.schema.json
  - control_plane/policy_gate_register.yaml
tags: [kfm, doctrine, trust, membrane, governance, lifecycle, evidence, policy, contract-v3]
notes:
  - Articulates the *trust-warranty* view of the boundary `lifecycle-law.md` calls the lifecycle membrane and that `ai-as-assistant.md` and the build-strategy doctrine call the "governance membrane."
  - Pinned to `CONTRACT_VERSION = "3.0.0"` per `ai-build-operating-contract.md` §0 / §37.
  - Introduces no new mechanism; gives an existing CONFIRMED boundary its canonical trust-vocabulary articulation.
  - Foundational sibling doctrine alongside `lifecycle-law.md`, `evidence-first.md`, `policy-aware.md`, `ai-as-assistant.md`, `trust-posture.md`.
  - All concrete file paths, schema paths, runbook paths, CI job names, and Shields targets are PROPOSED until verified against the live repository.
  - v0 draft (2026-05-12) treated `STALE` as a fifth peer outcome; v1 reconciles to the canonical four-outcome model in `ai-build-operating-contract.md` §21.2. See §16 Changelog.
[/KFM_META_BLOCK_V2] -->

# Trust Membrane

> **The boundary across which material in Kansas Frontier Matrix acquires trust the system is willing to defend — and a precise statement of what that trust does, and does not, warrant.**

![Type: Doctrine](https://img.shields.io/badge/type-doctrine-1F3A66?style=flat-square)
![Status: Draft](https://img.shields.io/badge/status-draft-orange?style=flat-square)
![Contract](https://img.shields.io/badge/CONTRACT__VERSION-3.0.0-1f6feb?style=flat-square)
![Conformance: RFC 2119](https://img.shields.io/badge/conformance-RFC%202119-555?style=flat-square)
![Posture: Fail-closed](https://img.shields.io/badge/posture-fail--closed-critical?style=flat-square)
![Boundary: Governance membrane](https://img.shields.io/badge/boundary-governance--membrane-4A6FA5?style=flat-square)
![Policy: Public](https://img.shields.io/badge/policy-public-2E7D32?style=flat-square)
![Updated](https://img.shields.io/badge/updated-2026--05--26-lightgrey?style=flat-square)
<!-- TODO — wire repo-level Shields endpoints (CI status, doctrine-coverage) once the doctrine-doc workflow is verified. -->

**Status:** Draft · **Owners:** *TODO — Docs steward + Architecture steward + Policy steward + AI surface steward* `[NEEDS VERIFICATION]` · **Last updated:** 2026-05-26 · **Pinned to:** `CONTRACT_VERSION = "3.0.0"`

> [!IMPORTANT]
> **Trust Membrane is the *trust-vocabulary* articulation of an existing CONFIRMED KFM boundary.** The boundary itself is referenced across project doctrine under multiple names — most often **"governance membrane"** (the enforcement view, e.g., [`ai-as-assistant.md`](./ai-as-assistant.md) and the build-strategy doctrine) and **"lifecycle membrane"** (the data-movement view, e.g., [`lifecycle-law.md`](./lifecycle-law.md)). This document adds a third, complementary view: what crossing the membrane *warrants in trust terms* and what it does not. It introduces **no new mechanism**.
>
> `[CONFIRMED — the underlying boundary is doctrine.]`
> `[PROPOSED — the doctrine-doc name `docs/doctrine/trust-membrane.md` as a sibling of `lifecycle-law.md` / `trust-posture.md`. See §13 OQ-TM-01 for the consolidation-vs-triangulation question.]`

---

## Contents

1. [Why this is doctrine](#1-why-this-is-doctrine)
2. [Definitions and naming](#2-definitions-and-naming)
3. [Conformance language](#3-conformance-language)
4. [The trust contract](#4-the-trust-contract)
5. [The membrane in the KFM lifecycle](#5-the-membrane-in-the-kfm-lifecycle)
6. [The gates, from a trust angle](#6-the-gates-from-a-trust-angle)
7. [Trust outcomes the membrane emits](#7-trust-outcomes-the-membrane-emits)
8. [Failure dispositions: refusal, quarantine, revocation](#8-failure-dispositions-refusal-quarantine-revocation)
9. [Relationship to other doctrines](#9-relationship-to-other-doctrines)
10. [Validation and tests](#10-validation-and-tests)
11. [Acceptance checklist](#11-acceptance-checklist)
12. [Anti-patterns](#12-anti-patterns)
13. [Open questions register](#13-open-questions-register)
14. [Open verification backlog](#14-open-verification-backlog)
15. [Changelog v0 → v1](#15-changelog-v0--v1)
16. [Definition of done](#16-definition-of-done)
17. [FAQ](#17-faq)
18. [Related docs](#18-related-docs)
19. [Appendix](#19-appendix)

---

## 1. Why this is doctrine

KFM exists to govern how evidence becomes intelligible, inspectable, publishable, reviewable, correctable, reversible, and operationally useful. That work depends on a boundary inside the system across which:

- raw and candidate material on one side is **not warranted** for downstream use, and
- material on the other side is **warranted** by recorded evidence, recorded policy, and recorded review.

Two CONFIRMED doctrine docs already describe this boundary from useful angles:

- [`lifecycle-law.md`](./lifecycle-law.md) describes its **shape** — the `RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED` invariant and the publication-as-state-transition rule.
- The "governance membrane" framing used in [`ai-as-assistant.md`](./ai-as-assistant.md) and the build-strategy doctrine describes its **enforcement** — what runs inside it, what runs outside it, and what may never cross it directly.

What is still missing is a canonical articulation of the membrane in **trust terms**: what the system *promises* by warranting a unit of material, and — equally important — what it *refuses to promise*. Without that articulation, "trusted" decays into a hopeful adjective rather than a recorded contract. This document fixes that.

> [!NOTE]
> **Authority.** This document is doctrine. Under [`ai-build-operating-contract.md`](./ai-build-operating-contract.md) §1.17 (Authority stack), doctrine sits above per-root READMEs, dossiers, and prior architecture reports. A lower rung never overrides a higher one; conflicting repo conventions are *drift to record*, not new authority. `[CONFIRMED — Authority Ladder.]`

Three commitments follow from making the trust view doctrinal:

1. **Trust is a contract, not a status.** Material does not become trusted by being moved between folders. It becomes trusted by acquiring a specific set of recorded warranties at the membrane.
2. **Trust is reversible.** The membrane is a *current* warranty, not a permanent one. New evidence, a failed re-check, a withdrawn rights grant, or a `CorrectionNotice` can revoke a prior crossing — and the doctrine names that path.
3. **Trust is finite.** The membrane emits a fixed vocabulary of outcomes — `ANSWER`, `ABSTAIN`, `DENY`, `ERROR` (with optional `NARROWED` / `BOUNDED` extensions per [`ai-build-operating-contract.md`](./ai-build-operating-contract.md) §21.2) — and no others. Informal trust language is forbidden in trust-significant contexts.

[⬆ Back to top](#trust-membrane)

---

## 2. Definitions and naming

### 2.1 The boundary, and its three names

The Trust Membrane, the governance membrane, and the lifecycle membrane refer to **the same boundary** in KFM, viewed from three angles.

| Name | View | Where it appears |
|---|---|---|
| **Governance membrane** | What **enforces** the boundary — validators, schemas, policy gates, release authority, runtime placement. | [`ai-as-assistant.md`](./ai-as-assistant.md); build-strategy doctrine. `[CONFIRMED]` |
| **Lifecycle membrane** | The **shape of data movement** across the boundary — the `RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED` invariant. | [`lifecycle-law.md`](./lifecycle-law.md). `[CONFIRMED]` |
| **Trust Membrane** | What **crossing warrants in trust terms** — what is promised, what is refused, how outcomes are expressed. | This document. `[CONFIRMED doctrine intent; doc name PROPOSED.]` |

> [!NOTE]
> These three names **MUST NOT drift into three different mechanisms**. If implementation begins treating them as distinct surfaces, that is a doctrine defect, not a refinement. The membrane is one boundary with three doctrinal articulations.

### 2.2 Working definitions

| Term | Meaning in this doctrine |
|---|---|
| **Membrane** | The doctrinal boundary inside KFM that separates not-yet-warranted material (`RAW`, `WORK`, `QUARANTINE`, candidates, secrets, direct-model outputs) from warranted material (released `EvidenceBundle`s, materialized `ReleaseManifest`s, indexed and tiled artifacts tied to a release). |
| **Crossing** | A recorded transition of a unit of material from the un-warranted side to the warranted side, accompanied by the receipts and decisions that justify it. |
| **Warrant** | The system's *recorded* willingness to defend a unit of material for a stated downstream use. A warrant is bounded by source role, policy label, freshness window, and (when published) `ReleaseManifest`. |
| **Revocation** | The withdrawal of a prior warrant. Produces a `CorrectionNotice`, a `RollbackCard` (where required), and an `ABSTAIN` or `DENY` outcome — paired with the UI negative state `RELEASE_WITHDRAWN` — for affected calls. |
| **Trust-significant context** | Any context whose outputs reach a public surface, an export, a release, an `AIReceipt`, an answer that cites an `AIReceipt`, a published map layer, a `ReleaseManifest`, or a `GENERATED_RECEIPT.json`. The doctrine's finite-outcome vocabulary is mandatory here. |
| **Trust badge** | The user-facing rendering of a warranty (e.g., on the map UI, in the Evidence Drawer). See [`map-first.md`](./map-first.md). |

The terms `RAW`, `WORK`, `QUARANTINE`, `PROCESSED`, `CATALOG`, `TRIPLET`, and `PUBLISHED` carry the lifecycle meaning defined in [`lifecycle-law.md`](./lifecycle-law.md). The terms `EvidenceBundle`, `EvidenceRef`, `SourceDescriptor`, `ReleaseManifest`, `ProofPack`, `ReviewRecord`, `CorrectionNotice`, `RollbackCard`, `AIReceipt`, `RunReceipt`, `GENERATED_RECEIPT`, `PolicyDecision`, `ValidationReport`, `CitationValidationReport`, `RuntimeResponseEnvelope`, `LayerManifest`, `MapReleaseManifest`, and `RedactionReceipt` carry the meanings defined in their respective contract schemas (paths PROPOSED in §18). Object names are **stable vocabulary**; renaming an object family without an ADR breaks crosswalks across the entire corpus. `[CONFIRMED — operating contract §29 / Atlas §10.]`

[⬆ Back to top](#trust-membrane)

---

## 3. Conformance language

This document uses RFC 2119 / RFC 8174 conformance keywords, aligned with [`directory-rules.md`](./directory-rules.md) §2.2 and [`ai-build-operating-contract.md`](./ai-build-operating-contract.md) §5.1.1.

| Keyword | Meaning here |
|---|---|
| **MUST / MUST NOT** | Non-negotiable. Implementation that violates a MUST does not conform to this doctrine absent an accepted ADR. |
| **SHOULD / SHOULD NOT** | Strong default. Deviation requires a brief justification logged in `docs/registers/DRIFT_REGISTER.md`. |
| **MAY** | Permitted; no justification required; remain consistent within the lane. |

> [!TIP]
> Where conformance language is omitted from a clause, the clause is **descriptive**, not normative. Normative weight enters only via the keywords above.

[⬆ Back to top](#trust-membrane)

---

## 4. The trust contract

Crossing the membrane warrants a **specific, bounded, recorded** set of claims about a unit of material. Equally important, it warrants *only* those claims — nothing else.

### 4.1 What a successful crossing warrants

`[CONFIRMED at doctrine level; field-level schema is PROPOSED.]`

| The membrane warrants… | …because the crossing recorded |
|---|---|
| **Source identity and role** | A `SourceDescriptor` resolved, with a recorded source role that supports the claim type. |
| **Provenance closure** | Every `EvidenceRef` in the unit's `EvidenceBundle` resolves at crossing time. |
| **Validation** | A passing `ValidationReport` for the relevant schemas, checks, and policies. |
| **Rights and sensitivity** | A `PolicyDecision` against rights, sensitivity, and access labels — `ALLOW`, or a labeled, bounded exception. |
| **Freshness window** | An explicit freshness range; outside that range the runtime returns `ABSTAIN` with reason `freshness.window_lapsed` and the UI renders the `SOURCE_STALE` negative state (see §7.3). |
| **Review (where required)** | A `ReviewRecord` naming a human role for activation, release approval, escalation, correction, or rollback. |
| **Release binding (when published)** | A `ReleaseManifest` reference, a `ProofPack` reference, and a `RollbackCard` reference. |

### 4.2 What a successful crossing does *not* warrant

The membrane's promises are bounded. Crossing it MUST NOT be taken to warrant:

- **Permanent truth.** A warranted unit MAY be revoked. New evidence, a withdrawn rights grant, or a failed re-check produces a revocation; the prior warrant becomes historical.
- **Universal applicability.** The policy label constrains where and to whom a unit MAY be exposed. A unit MAY be warranted for one public surface and `DENY`-ed on another.
- **Downstream AI claims.** When AI summarizes or drafts from warranted evidence, the AI output is **a new claim** that MUST carry its own `RuntimeResponseEnvelope` and `AIReceipt`. The membrane warrants the evidence, not the AI's prose. See [`ai-as-assistant.md`](./ai-as-assistant.md).
- **Reality itself.** The membrane warrants that KFM's evidence pipeline was followed. It does not warrant that the underlying world is as the evidence describes. *Carrier-vs-sovereign-truth* applies — maps, tiles, graphs, dashboards, and AI answers are **carriers** of evidence, never sovereign truth.

> [!CAUTION]
> Conflating these four exclusions with the seven inclusions in §4.1 is the most common path to a quietly broken trust system. The doctrine is fail-closed: anything not in §4.1 is **not** warranted by the membrane, regardless of how it reads on a page.

[⬆ Back to top](#trust-membrane)

---

## 5. The membrane in the KFM lifecycle

The membrane lives **inside** the KFM lifecycle invariant, not at one end of it. From a trust angle, the lifecycle has an un-warranted side and a warranted interior, with the publication gate as the final crossing to public surfaces.

```mermaid
flowchart LR
    classDef unwarranted fill:#FFE9E0,stroke:#B85C38,color:#3B1B0A;
    classDef interior fill:#F4F4F4,stroke:#444,color:#1F1F1F;
    classDef warranted fill:#D9EAD3,stroke:#3B7A57,color:#1B3A24;
    classDef denied fill:#F2D7D7,stroke:#A33,color:#5A0A0A;

    subgraph LEFT["Un-warranted side"]
        RAW["RAW<br/>immutable capture"]:::unwarranted
        WORK["WORK<br/>derivation in progress"]:::unwarranted
        QUAR["QUARANTINE<br/>failed gates · contained"]:::denied
    end

    subgraph MID["Warranted interior (inside the membrane)"]
        PROC["PROCESSED<br/>schemas · validation"]:::interior
        CAT["CATALOG / TRIPLET<br/>indexed · linked"]:::interior
    end

    subgraph RIGHT["Publicly warranted"]
        PUB["PUBLISHED<br/>ReleaseManifest-bound"]:::warranted
    end

    RAW -- "intake gate<br/>IntakeReceipt" --> WORK
    WORK -- "verification gate<br/>EvidenceBundle + ValidationReport + PolicyDecision" --> PROC
    WORK -. "fail-closed" .-> QUAR
    PROC -- "catalog gate<br/>linked-data + index integrity" --> CAT
    CAT -- "publication gate<br/>ReleaseManifest + ProofPack + ReviewRecord + RollbackCard" --> PUB
    QUAR -. "remediation only<br/>(no shortcut to PROC)" .-> WORK
    PUB -. "revocation<br/>CorrectionNotice + RollbackCard" .-> QUAR
```

> [!NOTE]
> The **primary trust crossing** is the verification gate (`WORK → PROCESSED`). After that crossing, material is warranted for internal downstream use under its policy label. The **publication gate** (`CATALOG / TRIPLET → PUBLISHED`) extends that warrant to public surfaces under an explicit `ReleaseManifest`. Material in `QUARANTINE` MUST NOT cut the line; it returns to `WORK` only after remediation, and re-presents at the verification gate from scratch. `[CONFIRMED at doctrine level; gate names PROPOSED — see §13 OQ-TM-02.]`

> [!WARNING]
> **DENY — Public internal-stage access.** Public UI, public APIs, exports, AI / Focus Mode, tile serving, and search MUST NOT read directly from `/data/raw`, `/data/work`, `/data/quarantine`, unpublished candidates, canonical internal stores, direct model runtime outputs, or source-system side effects. Any route that does so is a **build-stop defect**, not a configuration issue. `[CONFIRMED doctrine; consistent with `lifecycle-law.md` and `ai-build-operating-contract.md` §22.]`

[⬆ Back to top](#trust-membrane)

---

## 6. The gates, from a trust angle

A *gate* is the operational checkpoint at which a crossing is decided. The gates are owned by [`lifecycle-law.md`](./lifecycle-law.md); this section restates them from a trust-warranty angle. The gate-letter labels (`A`–`G`) used in some KFM documents (e.g., `kfm_unified_doctrine_synthesis.md` §8) compose with the gate names below; the trust angle is presented here for readability, and the letter-form is preserved for cross-doc traceability.

### 6.1 Gate registry (trust view)

`[CONFIRMED at doctrine level; gate names and receipt schemas PROPOSED.]`

| Gate (trust view) | Letter-form ref | Transition | Primary trust question | Recorded receipts | Refusal disposition |
|---|---|---|---|---|---|
| **Intake gate** | `A` Source identity · `B` Rights and terms | external → `RAW` | "Did we receive what we think we received, from whom, when, and under what terms?" | `IntakeReceipt` paired with a resolved `SourceDescriptor`. | `ERROR` (capture failed) or `DENY` (terms unclear). |
| **Verification gate** *(primary trust crossing)* | `C` Sensitivity · `D` Schema/contract · `E` Evidence closure | `WORK` → `PROCESSED` | "Does the evidence close, validate, and clear policy for the claim type?" | `EvidenceBundle` + `ValidationReport` + `PolicyDecision` + `TransformReceipt` (+ `RedactionReceipt` where applicable). | `DENY` (policy), `ERROR` (validation), or move-to-`QUARANTINE` (containment). |
| **Catalog gate** | `F` Catalog / provenance | `PROCESSED` → `CATALOG / TRIPLET` | "Is this discoverable and linked-data consistent without leaking what it shouldn't?" | Catalog record + triple-form consistency report + `CatalogMatrixReport`. | `DENY` (consistency) or `ERROR` (index integrity). |
| **Publication gate** | `G` Review / release / rollback | `CATALOG / TRIPLET` → `PUBLISHED` | "MAY this be exposed publicly under its operative policy label, with rollback in place?" | `PromotionDecision` + `ReleaseManifest` + `ProofPack` + `ReviewRecord` + `RollbackCard`. | `DENY release.unreviewed` · `DENY policy.sensitivity` · `ABSTAIN release.stale` · `HOLD release.pending_review`. |

> [!IMPORTANT]
> **Bundles compose forward.** A gate MUST NOT re-prove what an earlier gate already warranted; it references prior receipts via `EvidenceRef`. A gate **MAY**, however, revoke an earlier crossing if the evidence it referenced no longer resolves. See §8.

> [!CAUTION]
> **A gate that did not run is a gate that failed.** "We didn't check" is not a `PASS`. If a gate produced no `PolicyDecision`, no `ValidationReport`, or no review record, promotion MUST `DENY`. `[CONFIRMED — kfm_unified_doctrine_synthesis.md §8.]`

### 6.2 Per-call evaluation envelope

Every call into a warranted unit — public API, steward API, AI runtime, map layer admission — re-evaluates the membrane outcome **at call time**, against the current policy register and freshness window. A prior `ALLOW` at the publication gate does not bypass the call-time check; it bounds it.

```text
caller_context + warranted_unit + policy_register + freshness_clock
        │
        ▼
   RuntimeResponseEnvelope {
       decision ∈ {ANSWER, ABSTAIN, DENY, ERROR}  // optional: NARROWED, BOUNDED
       reason_code,
       citations[EvidenceRef],
       policy_refs[],
       ui_negative_state?  // e.g., SOURCE_STALE, RELEASE_WITHDRAWN
   }
```

`[PROPOSED envelope sketch aligned to `ai-build-operating-contract.md` §21.2 and §22.2; canonical schema lives at `schemas/contracts/v1/runtime_response_envelope.schema.json` (PROPOSED).]`

[⬆ Back to top](#trust-membrane)

---

## 7. Trust outcomes the membrane emits

The membrane communicates outcomes using a **finite vocabulary**. Informal substitutes — "probably," "should be fine," "trusted-ish" — are forbidden in trust-significant contexts.

### 7.1 Canonical runtime outcomes (required four)

Per [`ai-build-operating-contract.md`](./ai-build-operating-contract.md) §21.2, every runtime surface MUST return exactly one of:

| Outcome | Meaning | Public-surface presentation |
|---|---|---|
| **`ANSWER`** | A current, policy-allowed warranty exists and the call may proceed. Resolved `EvidenceBundle`, `PolicyDecision = ALLOW`, `ReleaseManifest` applies. | Result rendered with trust badge + citations. |
| **`ABSTAIN`** | A warranty existed but does not currently support this call — freshness lapsed, source-role insufficient for the claim type, unresolved `EvidenceRef`, citation validation failed, or scope too broad. | Result withheld with an explicit reason; no fabricated alternative. |
| **`DENY`** | Policy refuses this exposure of this unit to this caller — rights, sensitivity, source terms, or release state forbids it. Sensitive lanes default here. | Refusal rendered with reason **shape**, never reason **contents**. |
| **`ERROR`** | A receipt failed to resolve, a schema validation failed, an audit invariant tripped, or infrastructure failed. | Refusal + audit trail; never a silent fallback. |

### 7.2 Optional extensions

[`ai-build-operating-contract.md`](./ai-build-operating-contract.md) §21.2 permits the following optional extensions **only when contract schemas define them**:

| Outcome | Meaning |
|---|---|
| **`NARROWED`** | Answer issued within a scope tighter than requested due to evidence or policy bounds. |
| **`BOUNDED`** | Answer issued with explicit confidence/coverage bounds. |

A surface MUST NOT emit `NARROWED` or `BOUNDED` unless the schema for its `RuntimeResponseEnvelope` admits them.

### 7.3 Adjacent governed-process outcomes

Two further outcomes appear at the **gate** layer (not at the runtime layer) and are documented here so the trust vocabulary is exhaustive:

| Outcome | Where it surfaces | Meaning |
|---|---|---|
| **`HOLD`** | Publication gate; review queues. | Promotion / release / correction paused pending steward, rights-holder, or policy review; the surface remains in its prior state, no silent rollback or replacement. `[CONFIRMED — Atlas §24.3.1.]` |
| **`PASS` / `FAIL`** | Validator-class checks. | A validator or admission check completed (acceptable / unacceptable); internal only, does not directly emit a public answer. `[CONFIRMED — Atlas §24.3.1.]` |

### 7.4 UI negative states (not runtime outcomes)

Freshness lapse, withdrawn release, restricted access, and similar conditions are **rendered** through the UI negative-state vocabulary in [`ai-build-operating-contract.md`](./ai-build-operating-contract.md) §22.2. The runtime returns one of the canonical four outcomes (typically `ABSTAIN` or `DENY`) with a reason code; the UI selects a matching negative state for display. The canonical UI negative states are:

`MISSING_EVIDENCE` · `SOURCE_STALE` · `DENIED_BY_POLICY` · `GENERALIZED_GEOMETRY` · `RESTRICTED_ACCESS` · `CONFLICTED_SUPPORT` · `CITATION_FAILED` · `RELEASE_WITHDRAWN` · `RUNTIME_ERROR`

> [!TIP]
> **`ABSTAIN` beats a confident guess.** The membrane's job is to make the system's silence legible, not to fill silence with plausible prose. This is the rule that anchors [`ai-as-assistant.md`](./ai-as-assistant.md): AI MAY consume warranted evidence, but where evidence does not close, AI MUST return `ABSTAIN`, not a fluent paragraph.

[⬆ Back to top](#trust-membrane)

---

## 8. Failure dispositions: refusal, quarantine, revocation

The membrane is defined as much by how it **refuses** as by how it admits. The three refusal modes below are doctrinally distinct.

| Mode | Trigger | What happens to the material | Audit artifact |
|---|---|---|---|
| **Refusal** | A gate's preconditions are not met at crossing time (missing receipt, unresolved `EvidenceRef`, policy `DENY`). | Material stays in its source stage. The refusal is recorded. | Refusal record citing the gate, the failed precondition, and the source stage. |
| **Quarantine** | A gate's preconditions are met *but a check failed*, or sensitivity / rights / source-role checks fail closed. | Material moves to `QUARANTINE`, isolated from public surfaces and from downstream re-derivation. | `QuarantineReceipt` citing the failed check, the containment scope, and the remediation owner. |
| **Revocation** | New evidence, a `CorrectionNotice`, a re-check, or a rights withdrawal invalidates a prior warrant. | Material is moved to `QUARANTINE`; downstream units that referenced it re-evaluate at next call. | `CorrectionNotice` + (where the warrant was published) `RollbackCard` execution record. |

> [!CAUTION]
> **Containment is not deletion.** Quarantined and revoked material is preserved with its containment record. Doctrine forbids silent disappearance, because that would erase the audit trail the membrane depends on. Retention is governed by the retention policy doc. `[CONFIRMED posture; retention policy path PROPOSED.]`

> [!NOTE]
> **A revocation propagates.** Any warranted unit whose `EvidenceBundle` cited a now-revoked unit re-evaluates at its next call and MAY itself downgrade to `ABSTAIN` (with reason `evidence.revoked_upstream`) and render the `RELEASE_WITHDRAWN` UI negative state. Revocations are not local events. Implementation MAY be call-time, build-time, or both — `[NEEDS VERIFICATION]` against the release-and-publication architecture doc. See §13 OQ-TM-04.

[⬆ Back to top](#trust-membrane)

---

## 9. Relationship to other doctrines

The Trust Membrane is one **view** of the boundary. Other doctrines own complementary views and MUST remain mutually consistent.

| Sibling doctrine | What it owns | How Trust Membrane composes with it |
|---|---|---|
| [`ai-build-operating-contract.md`](./ai-build-operating-contract.md) | The canonical operating contract (`CONTRACT_VERSION = "3.0.0"`); §1 Operating Law; finite outcomes; AI containment; `GENERATED_RECEIPT.json` discipline. `[CONFIRMED sibling.]` | **Operating contract above doctrine view.** Where this document references a runtime outcome or receipt class, the contract's definition wins; this document elaborates the *trust-warranty meaning* of that contract. |
| [`directory-rules.md`](./directory-rules.md) | Responsibility-root governance; placement protocol; the schema-home rule. `[CONFIRMED sibling.]` | **Governs where this document lives.** This document's PROPOSED home is `docs/doctrine/trust-membrane.md`; the placement protocol applies to every receipt schema, policy register, and runbook this document references. |
| [`lifecycle-law.md`](./lifecycle-law.md) | Shape of data movement; the `RAW → WORK / QUARANTINE → PROCESSED → CATALOG / TRIPLET → PUBLISHED` invariant; publication as state transition. `[CONFIRMED sibling.]` | **Same boundary, different angle.** Lifecycle Law names the stages and transitions; Trust Membrane names what crossing warrants and what it does not. |
| [`evidence-first.md`](./evidence-first.md) | Cite-or-abstain rule; `EvidenceRef` / `EvidenceBundle` closure obligations. `[CONFIRMED sibling.]` | **Sources the warrant.** A gate cannot warrant a unit whose evidence does not close. The seven-warranty list in §4.1 is bounded by Evidence First. |
| [`policy-aware.md`](./policy-aware.md) | Policy gate at publication; rights, sensitivity, access labels; finite policy outcomes. `[CONFIRMED sibling.]` | **Decides admission.** The publication gate is a Policy Aware decision; Trust Membrane records what its outcome warrants. |
| [`ai-as-assistant.md`](./ai-as-assistant.md) | AI runtime placement inside the governance membrane; cite-or-abstain for AI; AI never decides truth, rights, sensitivity, release. `[CONFIRMED sibling.]` | **Restricts AI.** AI MAY *consume* warranted material; AI MUST NOT *issue* warranties. AI outputs are new claims that cite the membrane's warranties, never substitute for them. |
| [`authority-ladder.md`](./authority-ladder.md) | Primary / Secondary / Tertiary source hierarchy; documentation authority. `[CONFIRMED sibling.]` | **Orthogonal.** Authority Ladder governs *what counts as authoritative documentation*; Trust Membrane governs *what crossing the boundary warrants*. They collaborate at the publication gate, grounding a `ReleaseManifest` from different angles. |
| [`corrections-are-first-class.md`](./corrections-are-first-class.md) | `CorrectionNotice` as a first-class object; correction workflow. `[CONFIRMED sibling; filename verified against operating-contract pattern.]` | **Drives revocation.** A `CorrectionNotice` is the most common revocation trigger; Trust Membrane defines what revocation does to downstream warrants. |
| [`derived-stays-derived.md`](./derived-stays-derived.md) | Derivation is monotonic; no later stage relabels material as `RAW`. `[CONFIRMED sibling.]` | **Constrains the gates.** The verification and catalog gates MUST NOT reach backward and re-classify warranted material as un-warranted; they MAY only **revoke**. |
| [`trust-posture.md`](./trust-posture.md) | Runtime expression of trust posture; how `ABSTAIN` / `DENY` and the UI negative states surface on public and steward UIs. `[CONFIRMED sibling.]` | **Renders the outcomes.** Trust Membrane emits outcomes; Trust Posture renders them. |
| [`truth-labels.md`](./truth-labels.md) | Truth label vocabulary (`CONFIRMED` / `INFERRED` / `PROPOSED` / `UNKNOWN` / `NEEDS VERIFICATION` / `CONFLICTED` / `LINEAGE` / `EXPLORATORY` / `EXTERNAL`). `[PROPOSED sibling; label set aligned to `ai-build-operating-contract.md` §8.]` | **Documentation vocabulary, distinct from runtime.** Truth labels describe *what we know about a document or claim*; trust outcomes describe *what the runtime is willing to do*. They MUST NOT be conflated. |
| [`map-first.md`](./map-first.md) | Public map surface; trust badges; Evidence Drawer. `[CONFIRMED sibling.]` | **Surfaces the warranty.** The map UI renders trust outcomes visibly per layer and per feature. |

[⬆ Back to top](#trust-membrane)

---

## 10. Validation and tests

All validators and CI jobs below are **PROPOSED to create**. The greenfield baseline makes CI deterministic, no-network by default, and fail-closed. `[CONFIRMED at doctrine level; concrete job names and paths are PROPOSED until verified against `.github/workflows/`.]`

| CI job | Purpose | Acceptance gate |
|---|---|---|
| `trust-contract-tests` | Validate that every fixture's `EvidenceBundle` closes and the recorded crossing matches §4.1. | Missing any required receipt → failure for the expected reason. |
| `trust-outcome-vocabulary-tests` | Validate that no trust-significant fixture or doc emits an outcome outside `{ANSWER, ABSTAIN, DENY, ERROR}` plus `{NARROWED, BOUNDED}` when their schemas admit them. | Informal trust language fails the lint. |
| `revocation-propagation-tests` | Inject a revocation against a fixture and verify downstream citing units re-evaluate. | All citing units downgrade to `ABSTAIN` per §8; UI renders `RELEASE_WITHDRAWN`. |
| `quarantine-isolation-tests` | Verify quarantined fixtures are unreachable from public envelopes. | Any public-facing call that resolves a quarantined `EvidenceRef` fails closed. |
| `publication-gate-receipt-tests` | Verify every "published" fixture has a `ReleaseManifest`, `ProofPack`, `ReviewRecord`, and `RollbackCard`. | Missing any of the four → `DENY release.unreviewed`. |
| `freshness-window-tests` | Drive the clock past the freshness window and verify `ABSTAIN freshness.window_lapsed` + UI `SOURCE_STALE`. | Silent-current behavior fails the test. |
| `forbidden-exposure-tests` | Confirm `RAW` / `WORK` / `QUARANTINE` / candidate / direct-model paths never appear in public envelopes. | Any leak → build-stop failure. |
| `audit-immutability-tests` | Confirm trust-significant audit records are append-only. | Any in-place overwrite fails the test. |
| `reason-shape-not-contents-tests` | Confirm `DENY` reasons describe denial *shape*, never denial *contents*. | A `DENY` payload that leaks the denied value fails the test. |
| `contract-version-pin-tests` | Confirm every emitted `AIReceipt` and `GENERATED_RECEIPT.json` carries `contract_version = "3.0.0"`. | Missing or mismatched pin → failure. `[CONFIRMED requirement — operating contract §37.1.]` |

> [!NOTE]
> Each CI job above MUST ship with both **valid** and **invalid** fixtures, and the invalid fixtures MUST fail *for the expected reason*. A test that fails for the wrong reason is not a passing negative test. `[CONFIRMED posture — operating contract §6.]`

[⬆ Back to top](#trust-membrane)

---

## 11. Acceptance checklist

A repository implementation conforms to this doctrine when **all** of the following hold. `[PROPOSED checklist; reconcile with the doctrine-coverage CI job when that job exists.]`

- [ ] The intake, verification, catalog, and publication gates each have a documented receipt schema.
- [ ] No public envelope references `RAW`, `WORK`, `QUARANTINE`, candidate, or direct-model paths.
- [ ] Every `EvidenceBundle` referenced by a published unit resolves at call time.
- [ ] Every published unit binds to a `ReleaseManifest`, a `ProofPack`, and a `RollbackCard`.
- [ ] Every trust-significant outcome uses the canonical four `{ANSWER, ABSTAIN, DENY, ERROR}` (plus `NARROWED` / `BOUNDED` only where schemas admit them).
- [ ] Freshness lapses produce `ABSTAIN freshness.window_lapsed` + UI `SOURCE_STALE`, never silent currency.
- [ ] Quarantined material is preserved, not deleted, and is unreachable from public envelopes.
- [ ] Revocations propagate: downstream warrants re-evaluate at next call.
- [ ] Audit storage is append-only for trust-significant decisions.
- [ ] `DENY` payloads describe denial *shape*, never denial *contents*.
- [ ] AI outputs cite warranted evidence via `EvidenceRef` and carry an `AIReceipt`; AI outputs never replace the membrane's warranty.
- [ ] Every AI-authored merge that touches doctrine, schemas, or policy emits a `GENERATED_RECEIPT.json` with `contract_version = "3.0.0"`. `[CONFIRMED requirement — operating contract §34.]`

[⬆ Back to top](#trust-membrane)

---

## 12. Anti-patterns

The following are CONFIRMED-rejection patterns. Each represents a real failure mode and MUST fail closed. Most rows align with the trust-membrane anti-patterns in `KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas` §24.9.2.

| Anti-pattern | Why rejected | Corrective rule |
|---|---|---|
| "We moved the file to `data/processed/`, so it's trusted." | Trust is a recorded warrant, not a directory location. | A crossing requires receipts. §4.1. |
| "The evidence closed, so we exposed it." | Evidence closure is necessary but not sufficient. Policy decides exposure. | Verification ≠ publication. §6.1. |
| "We deleted the bad record." | Silent deletion erases the audit trail. | Quarantine, do not delete. §8. |
| "The AI confirmed it." | AI consumes warranted evidence; it cannot issue a warrant. | [`ai-as-assistant.md`](./ai-as-assistant.md) binds. |
| "It was true last month, so it's current." | Freshness MUST be evaluated at call time. | `ABSTAIN freshness.window_lapsed` + UI `SOURCE_STALE`, never silent current. §7. |
| "The hint helps the user understand the denial." | Operator hints MUST describe denial *shape*, not denial *contents*. | Reason shape, not reason contents. §7. |
| "We patched the warranted record in place." | Corrections produce a new bundle and a `CorrectionNotice`; in-place edits break audit. | Append-only audit. §8. |
| "The system is mostly fine." | The membrane has no "mostly fine" outcome. | Finite vocabulary or refuse. §7. |
| "We renamed the lifecycle membrane to the trust membrane in the code." | The three names describe one boundary, not three. | Same mechanism. §2.1. |
| "The map renderer reads canonical directly for speed." | Renderer becomes the public surface and inherits no governance. | DENY renderer-as-truth. `[CONFIRMED — Atlas §24.9.2.]` |
| "We routed the AI generation through an admin shortcut." | Admin bypass becomes a normal-path public route. | Trust-membrane audit denies. `[CONFIRMED — Atlas §24.9.2.]` |
| "We released without a `ReleaseManifest` because rollback wasn't ready." | Public surface cannot be rolled back; release not auditable. | DENY release.unreviewed until rollback target exists. §6.1. |

[⬆ Back to top](#trust-membrane)

---

## 13. Open questions register

| ID | Question | Owner role | Resolution path |
|---|---|---|---|
| **OQ-TM-01** | Should this doc live as `docs/doctrine/trust-membrane.md`, or should the trust view be folded into a unified `docs/doctrine/membrane.md` alongside lifecycle and governance views? | Docs steward | ADR before v1 publication. |
| **OQ-TM-02** | Are `intake` · `verification` · `catalog` · `publication` the canonical trust-view gate names, or should they be renamed to match terminology already established in `lifecycle-law.md`? The letter-form (A–G) is preserved either way. | Architecture steward | Repo inspection of `lifecycle-law.md`; ADR if needed. |
| **OQ-TM-03** | Does §4.1's seven-item warranty list match the field set in the planned `release_manifest.schema.json` and `proof_pack.schema.json`? | Architecture steward | Repo inspection once schemas land. |
| **OQ-TM-04** | Is revocation propagation implemented as call-time re-evaluation, build-time re-derivation, or both? | Architecture steward | Verify against the release-and-publication architecture doc. |
| **OQ-TM-05** | Where does `truth-labels.md` end and this doc begin? §9 states the split (documentation vocabulary vs runtime vocabulary); confirm in the truth-labels doctrine when it lands. | Docs steward | Cross-doc review when `truth-labels.md` is drafted. |
| **OQ-TM-06** | The corpus filename `corrections-are-first-class.md` is adopted here in line with the operating-contract pattern; the v0 draft used `corrections-first-class.md`. Verify the canonical name in the live repo and update the related-docs list if needed. | Docs steward | Repo inspection. |
| **OQ-TM-07** | Should `HOLD` (gate-level review-pause outcome per Atlas §24.3.1) be added to the runtime envelope vocabulary in `ai-build-operating-contract.md` §21.2, or remain gate-only? | Architecture steward + AI surface steward | ADR if promotion to runtime is desired. |
| **OQ-TM-08** | Should `RuntimeResponseEnvelope.ui_negative_state` be a normative field (added to the canonical schema) or remain an advisory hint? | Architecture steward | ADR against §22.2. |

[⬆ Back to top](#trust-membrane)

---

## 14. Open verification backlog

These items remain `NEEDS VERIFICATION` before promotion from `draft` to `published`:

1. Canonical filename `corrections-are-first-class.md` (OQ-TM-06).
2. `lifecycle-law.md` gate naming, against this doc's trust-view labels (OQ-TM-02).
3. `release_manifest.schema.json` field set (OQ-TM-03).
4. `proof_pack.schema.json` field set (OQ-TM-03).
5. `evidence_bundle.schema.json` resolution semantics (used by §4.1, §5, §10).
6. `policy_gate_register.yaml` location and shape under `control_plane/`.
7. The doctrine-coverage CI job — whether it exists and what it asserts.
8. The `RuntimeResponseEnvelope` schema home — `schemas/contracts/v1/runtime_response_envelope.schema.json` (PROPOSED).
9. Revocation propagation mechanism (OQ-TM-04).
10. Whether `HOLD` and the UI negative states are documented in `trust-posture.md`.

[⬆ Back to top](#trust-membrane)

---

## 15. Changelog v0 → v1

| Change | Type (per contract §37) | Reason |
|---|---|---|
| Pinned `CONTRACT_VERSION = "3.0.0"` in meta block, badge row, and validation suite. | new | Required by `ai-build-operating-contract.md` §37.1 for all doctrine-adjacent docs. |
| Added §3 Conformance language (RFC 2119 / RFC 8174). | new | Aligns with `directory-rules.md` §2.2 and operating contract §5.1.1. |
| Reconciled outcome vocabulary: `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` as the canonical four; `NARROWED` / `BOUNDED` as schema-gated optional extensions; `STALE` (v0 fifth peer) reconciled as `ABSTAIN freshness.window_lapsed` + UI `SOURCE_STALE`. | reconciliation | v0 §6 treated `STALE` as a fifth peer, which CONFLICTED with operating contract §21.2 and `KFM_Unified_Implementation_Architecture_Build_Manual.md` §2.2. v1 restores the canonical four-outcome model. |
| Added §7.3 gate-level outcomes `HOLD`, `PASS`, `FAIL`. | gap closure | Atlas §24.3.1 names `HOLD`/`PASS`/`FAIL` as governed-process outcomes adjacent to runtime; v0 omitted them. |
| Added §7.4 UI negative-state vocabulary (§22.2 of operating contract). | gap closure | Connects the runtime outcome to its UI rendering so reviewers see the full chain. |
| Added §10 row `contract-version-pin-tests`. | new | Enforces operating contract §37.1 in CI. |
| Added §11 acceptance row for `GENERATED_RECEIPT.json` discipline. | new | Aligns with operating contract §34. |
| Renamed `RollbackPlan` → `RollbackCard` to match the corpus-wide object family in operating contract §29 and `kfm_unified_doctrine_synthesis.md` §10. | reconciliation | v0 referred to both names; doctrine corpus is consistent on `RollbackCard`. |
| Updated `corrections-first-class.md` → `corrections-are-first-class.md` in related-docs list (pending OQ-TM-06 verification). | reconciliation | Operating-contract reviewer pattern names the latter. |
| Added §1 inline reference to the Authority Ladder. | clarification | Anchors this doc in the v3.0 authority stack. |
| Added §6.1 letter-form (`A`–`G`) cross-reference column. | clarification | Preserves traceability with `kfm_unified_doctrine_synthesis.md` §8 and `KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas` §20.2. |
| Added §12 anti-pattern rows for renderer-as-truth, admin-shortcut AI, and release-without-manifest. | gap closure | Atlas §24.9.2 names these; v0 omitted them. |
| Added §13 Open questions register, §14 Verification backlog, §15 Changelog, §16 Definition of done. | new | Required companion sections for doctrine docs per the AI-builder Markdown-authoring contract. |

> **Version type.** Per `ai-build-operating-contract.md` §37.1, **MINOR**: clarifications, reconciliations, and gap closures; no `AIReceipt` / `GENERATED_RECEIPT` field renames; no Operating Law change.

> **Backward compatibility.** Anchors `#1-why-this-is-doctrine` through `#11-anti-patterns` from the v0 draft are preserved (with section bodies tightened). The v0 FAQ moved from §12 to §17 — readers linking to `#12-faq` should update to `#17-faq`. The v0 Appendix B was promoted into §13 Open questions register; readers linking to `#14-appendix` should rely on the new `#19-appendix` anchor.

[⬆ Back to top](#trust-membrane)

---

## 16. Definition of done

This document is done enough to enter the repository when:

- it is placed according to [`directory-rules.md`](./directory-rules.md);
- a docs steward + architecture steward + policy steward + AI surface steward review it (per the operating-contract reviewer pattern in `ai-build-operating-contract.md` §0);
- it is linked from the docs / doctrine index;
- it does not conflict with accepted ADRs;
- any conflict with current repo conventions is logged in `docs/registers/DRIFT_REGISTER.md`;
- a `GENERATED_RECEIPT.json` (per `ai-build-operating-contract.md` §34) is wired into CI for the merge that lands this file;
- OQ-TM-06 (filename of `corrections-are-first-class.md`) is resolved;
- future changes follow `ai-build-operating-contract.md` §37 lifecycle.

[⬆ Back to top](#trust-membrane)

---

## 17. FAQ

**Is the Trust Membrane a service?**
No. It is a doctrinal articulation. It is realized by gates and receipts that live across schemas, validators, the policy register, catalog tooling, release tooling, and the runtime. The membrane is a *property* of the system, not a *component* of it.

**Why a separate doc instead of folding this into `lifecycle-law.md`?**
Because lifecycle, governance, and trust are three useful views of the same boundary, and conflating any two of them leads to predictable failures. Lifecycle Law owns the shape; this doc owns the warranty contract; the "governance membrane" framing owns the enforcement. Keeping them as distinct doctrine docs lets each be precise. See §13 OQ-TM-01.

**Is a "warranted" unit "true"?**
No. A warrant is a recorded promise that KFM's evidence pipeline was followed for the claim. It is not a metaphysical claim about the world. *Carrier-vs-sovereign-truth* applies.

**Can a unit be warranted for one surface and denied on another?**
Yes. Policy labels constrain exposure. The verification gate MAY warrant a unit for internal downstream use while the publication gate refuses it for a given public surface.

**What is the difference between `ABSTAIN` and `DENY`?**
`ABSTAIN` means *"a warranty does not currently support this call"* — typically a freshness, source-role, or claim-type mismatch, or an unresolved `EvidenceRef`. `DENY` means *"policy refuses this exposure"* — typically rights, sensitivity, or access-label denial. They are **not** interchangeable.

**Where did the `STALE` outcome from v0 go?**
Reconciled. `STALE` was not a peer outcome in the canonical model (`ai-build-operating-contract.md` §21.2). v1 expresses freshness lapse as `ABSTAIN freshness.window_lapsed` at the runtime layer and `SOURCE_STALE` at the UI layer (§22.2). See §15 Changelog.

**Where does human judgment fit?**
In the `ReviewRecord` attached to source activations, release approvals, escalations, corrections, and rollback executions. The membrane records that a human role decided; it does not pretend human judgment is automatable.

**Can material skip a gate?**
No. Doctrinally, there is no path from an un-warranted stage into a warranted stage except through the gate that joins them. Manual placements bypass audit and are forbidden.

**What if a sibling doctrine disagrees with this one?**
Surface the conflict in an ADR and resolve it explicitly. Trust Membrane MUST NOT silently override siblings, and siblings MUST NOT silently override it. The boundary is one boundary; the doctrines MUST remain mutually consistent.

[⬆ Back to top](#trust-membrane)

---

## 18. Related docs

> [!NOTE]
> All paths below are PROPOSED until verified against the live repository. Items marked `[CONFIRMED sibling]` are confirmed by prior KFM doctrine to exist or to be planned as siblings of this document; items marked `[PROPOSED sibling]` are referenced as planned in other doctrine but have not been verified in the live repo this session.

**Operating doctrine**

- [`docs/doctrine/ai-build-operating-contract.md`](./ai-build-operating-contract.md) — canonical operating contract; pins `CONTRACT_VERSION = "3.0.0"`. `[CONFIRMED sibling.]`
- [`docs/doctrine/directory-rules.md`](./directory-rules.md) — responsibility-root governance and placement protocol. `[CONFIRMED sibling.]`

**Trust-boundary siblings**

- [`docs/doctrine/lifecycle-law.md`](./lifecycle-law.md) — shape of the lifecycle and publication-as-state-transition. `[CONFIRMED sibling.]`
- [`docs/doctrine/evidence-first.md`](./evidence-first.md) — cite-or-abstain rule. `[CONFIRMED sibling.]`
- [`docs/doctrine/policy-aware.md`](./policy-aware.md) — policy gate and finite policy outcomes. `[CONFIRMED sibling.]`
- [`docs/doctrine/ai-as-assistant.md`](./ai-as-assistant.md) — AI containment and the `RuntimeResponseEnvelope`. `[CONFIRMED sibling.]`
- [`docs/doctrine/authority-ladder.md`](./authority-ladder.md) — source authority hierarchy. `[CONFIRMED sibling.]`
- [`docs/doctrine/corrections-are-first-class.md`](./corrections-are-first-class.md) — `CorrectionNotice` and the correction workflow. `[CONFIRMED sibling; filename pending OQ-TM-06.]`
- [`docs/doctrine/derived-stays-derived.md`](./derived-stays-derived.md) — derivation is monotonic. `[CONFIRMED sibling.]`
- [`docs/doctrine/trust-posture.md`](./trust-posture.md) — runtime expression of trust posture. `[CONFIRMED sibling.]`
- [`docs/doctrine/truth-labels.md`](./truth-labels.md) — truth label vocabulary, distinct from runtime outcomes. `[PROPOSED sibling.]`
- [`docs/doctrine/evidence-model.md`](./evidence-model.md) — `EvidenceRef` / `EvidenceBundle` semantics. `[PROPOSED sibling.]`
- [`docs/doctrine/map-first.md`](./map-first.md) — public map surface, trust badges, Evidence Drawer. `[CONFIRMED sibling.]`

**Architecture and security**

- [`docs/architecture/release-and-publication.md`](../architecture/release-and-publication.md) — release / publication architecture. `[PROPOSED path.]`
- [`docs/security/threat-model.md`](../security/threat-model.md) — threat model, including direct-model bypass. `[PROPOSED path.]`

**Contracts and registers**

- [`schemas/contracts/v1/release_manifest.schema.json`](../../schemas/contracts/v1/release_manifest.schema.json) — `ReleaseManifest` schema. `[PROPOSED path.]`
- [`schemas/contracts/v1/proof_pack.schema.json`](../../schemas/contracts/v1/proof_pack.schema.json) — `ProofPack` schema. `[PROPOSED path.]`
- [`schemas/contracts/v1/evidence_bundle.schema.json`](../../schemas/contracts/v1/evidence_bundle.schema.json) — `EvidenceBundle` schema. `[PROPOSED path.]`
- [`schemas/contracts/v1/runtime_response_envelope.schema.json`](../../schemas/contracts/v1/runtime_response_envelope.schema.json) — `RuntimeResponseEnvelope` schema. `[PROPOSED path.]`
- [`schemas/contracts/v1/receipts/generated_receipt.schema.json`](../../schemas/contracts/v1/receipts/generated_receipt.schema.json) — `GENERATED_RECEIPT` schema. `[PROPOSED path — operating contract §47.]`
- [`control_plane/policy_gate_register.yaml`](../../control_plane/policy_gate_register.yaml) — policy gate register. `[PROPOSED path.]`
- [`docs/registers/DRIFT_REGISTER.md`](../registers/DRIFT_REGISTER.md) — drift register for membrane-related divergences. `[PROPOSED path.]`

[⬆ Back to top](#trust-membrane)

---

## 19. Appendix

<details>
<summary><strong>A. Glossary used in this doctrine</strong></summary>

| Term | Meaning here |
|---|---|
| **Trust Membrane** | The trust-vocabulary articulation of the boundary `lifecycle-law.md` calls the lifecycle membrane and `ai-as-assistant.md` calls the governance membrane. Same boundary, different angle. |
| **Crossing** | A recorded transition from an un-warranted stage to a warranted stage. |
| **Warrant** | The system's recorded willingness to defend a unit for a stated downstream use. |
| **Refusal** | A gate decision to leave material in its source stage. |
| **Quarantine** | A containment state for material that tripped an active check. |
| **Revocation** | Explicit retraction of a prior warrant in light of new evidence or a `CorrectionNotice`. |
| **Trust-significant context** | A context whose outputs reach a public surface, an export, a release, an `AIReceipt`, a citing answer, a map layer, a `ReleaseManifest`, or a `GENERATED_RECEIPT.json`. Finite-outcome vocabulary is mandatory here. |
| **Warranted interior** | The set of stages inside the membrane (`PROCESSED`, `CATALOG / TRIPLET`) that are warranted for internal downstream use under their policy labels. |
| **Publicly warranted** | The `PUBLISHED` stage; warranted for public surfaces under an explicit `ReleaseManifest`. |
| **Reason shape (vs reason contents)** | A denial communicates *what kind* of refusal occurred (e.g., `policy.sensitivity`), never the *value* the policy was protecting. |
| **Letter-form gate ref** | The `A`–`G` gate labels used in `kfm_unified_doctrine_synthesis.md` §8 and Atlas §20.2; cross-referenced from §6.1 for traceability. |

</details>

<details>
<summary><strong>B. Illustrative trust-outcome shapes (not schemas)</strong></summary>

`ANSWER` (illustrative, public API):

```json
{
  "decision": "ANSWER",
  "reason_code": "ok.warranted",
  "citations": [
    "kfm://evidence/bundle/2026-05-26-hydrology-06892350"
  ],
  "policy_refs": ["kfm://policy/public/hydrology/v1"],
  "freshness": { "as_of": "2026-05-26T00:00:00Z", "window_hours": 24 },
  "release": "kfm://release/2026-05-W22/hydrology",
  "contract_version": "3.0.0"
}
```

`ABSTAIN freshness.window_lapsed` (illustrative — pairs with UI `SOURCE_STALE`):

```json
{
  "decision": "ABSTAIN",
  "reason_code": "freshness.window_lapsed",
  "last_fresh_at": "2026-05-23T00:00:00Z",
  "window_hours": 24,
  "citations": [
    "kfm://evidence/bundle/2026-05-23-hydrology-06892350"
  ],
  "ui_negative_state": "SOURCE_STALE",
  "contract_version": "3.0.0"
}
```

`DENY` (illustrative — reason *shape*, not contents):

```json
{
  "decision": "DENY",
  "reason_code": "policy.sensitivity",
  "exposure": "public",
  "guidance": "Requested through /steward/v1 with appropriate role.",
  "ui_negative_state": "DENIED_BY_POLICY",
  "contract_version": "3.0.0"
}
```

`HOLD` (illustrative — gate-level, publication paused):

```json
{
  "decision": "HOLD",
  "reason_code": "release.pending_review",
  "review_owner": "policy_steward",
  "blocking_record": "kfm://review/pending/2026-05-26-hydrology-014",
  "contract_version": "3.0.0"
}
```

> Illustrative only. Canonical schemas live under `schemas/contracts/v1/` — PROPOSED paths.

</details>

<details>
<summary><strong>C. Crosswalk: v0 outcome vocabulary → v1 reconciled vocabulary</strong></summary>

| v0 outcome (draft, 2026-05-12) | v1 reconciliation (2026-05-26) | Where the v1 form lives |
|---|---|---|
| `ANSWER` | `ANSWER` | `RuntimeResponseEnvelope.decision` |
| `ABSTAIN` | `ABSTAIN` | `RuntimeResponseEnvelope.decision` |
| `DENY` | `DENY` | `RuntimeResponseEnvelope.decision` |
| `ERROR` | `ERROR` | `RuntimeResponseEnvelope.decision` |
| `STALE` *(v0 fifth peer)* | `ABSTAIN freshness.window_lapsed` + UI `SOURCE_STALE` | Runtime + UI rendering layer |
| *(not in v0)* | `NARROWED`, `BOUNDED` (optional, schema-gated) | `RuntimeResponseEnvelope.decision` |
| *(not in v0)* | `HOLD` (gate-level, review-paused) | Publication-gate / review queue surfaces |
| *(not in v0)* | `PASS` / `FAIL` (validator-class, internal-only) | `ValidationReport` |

</details>

---

### Related docs (compact)

[`ai-build-operating-contract.md`](./ai-build-operating-contract.md) · [`lifecycle-law.md`](./lifecycle-law.md) · [`evidence-first.md`](./evidence-first.md) · [`policy-aware.md`](./policy-aware.md) · [`ai-as-assistant.md`](./ai-as-assistant.md) · [`trust-posture.md`](./trust-posture.md) · [`corrections-are-first-class.md`](./corrections-are-first-class.md) · [`map-first.md`](./map-first.md)

**Last updated:** 2026-05-26 · **Version:** v1 (draft) · **Status:** awaiting review · **Pinned to:** `CONTRACT_VERSION = "3.0.0"`

[⬆ Back to top](#trust-membrane)
