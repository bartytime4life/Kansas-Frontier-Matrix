<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-governance-escalation
title: Escalation — docs/governance/ESCALATION.md
type: standard
version: v1
status: draft
owners: ["@kfm-docs-stewards"]
created: 2026-05-12
updated: 2026-05-12
policy_label: public
related:
  - docs/governance/README.md
  - docs/governance/SEPARATION_OF_DUTIES.md
  - docs/governance/STEWARD_CHARTERS.md
  - docs/governance/REVIEW_DUTIES.md
  - docs/governance/CONTRADICTION_HANDLING.md
  - docs/doctrine/directory-rules.md
  - docs/doctrine/authority-ladder.md
  - docs/doctrine/trust-membrane.md
  - docs/doctrine/lifecycle-law.md
  - docs/registers/DRIFT_REGISTER.md
  - docs/registers/VERIFICATION_BACKLOG.md
  - docs/runbooks/SENSITIVITY_ESCALATION.md
  - docs/runbooks/INCIDENT_RESPONSE.md
  - docs/security/INCIDENT_RESPONSE.md
  - control_plane/policy_gate_register.yaml
  - control_plane/contradiction_register.yaml
tags: ["kfm", "governance", "escalation", "review", "separation-of-duties", "sensitivity", "rollback"]
notes: "Names the triggers, the owning role, and the secondary reviewer required when a decision exceeds an actor's authority. Explains; does not enforce. Enforcement lives in policy/, tests/, .github/workflows/, and control_plane/."
[/KFM_META_BLOCK_V2] -->

# Escalation · `docs/governance/ESCALATION.md`

> **When a decision exceeds an actor's authority, KFM escalates it through a named, reviewable path. This document catalogs the triggers, the owning role, the required secondary reviewer, and the receipts the handoff must produce.**

[![Status](https://img.shields.io/badge/status-draft-lightgrey)](#status)
[![Authority](https://img.shields.io/badge/authority-governance%20prose-blue)](#repo-fit)
[![Owners](https://img.shields.io/badge/owners-%40kfm--docs--stewards-informational)](#review-burden)
[![Lifecycle](https://img.shields.io/badge/lifecycle-RAW%E2%86%92WORK%E2%86%92PROC%E2%86%92CAT%E2%86%92PUB-success)](../doctrine/lifecycle-law.md)
[![Truth posture](https://img.shields.io/badge/truth-cite--or--abstain-purple)](../doctrine/truth-posture.md)
[![Fail-safe](https://img.shields.io/badge/sensitive%20lanes-fail--closed-critical)](#3-sensitivity-tier-escalation)
[![Last reviewed](https://img.shields.io/badge/last%20reviewed-TODO-yellow)](#last-reviewed)

**Status:** `draft` · **Owners:** `@kfm-docs-stewards` *(PROPOSED placeholder)* · **Updated:** `TODO` *(set at merge time)*

> [!IMPORTANT]
> `docs/governance/ESCALATION.md` **explains** how escalation works.
> It does **not** enforce escalation. Enforcement lives in `policy/`, `tests/`, `.github/workflows/`, and `control_plane/`.
> If this document and the executable layer disagree, the executable layer wins and a `docs/registers/DRIFT_REGISTER.md` entry is opened.

---

## Quick links

- [1. Purpose & scope](#1-purpose--scope)
- [2. Roles roster](#2-roles-roster)
- [3. Escalation flow](#3-escalation-flow)
- [4. Trigger catalog](#4-trigger-catalog)
- [5. Routing matrix](#5-routing-matrix)
- [6. Sensitivity tier escalation](#6-sensitivity-tier-escalation)
- [7. AI surface escalation](#7-ai-surface-escalation)
- [8. Source / vendor distress escalation](#8-source--vendor-distress-escalation)
- [9. Process & tracking](#9-process--tracking-proposed)
- [10. Anti-patterns](#10-anti-patterns)
- [11. Open questions](#11-open-questions--verification-backlog)
- [12. Related docs](#12-related-docs)
- [Appendix A — Reason-code crosswalk](#appendix-a--reason-code-crosswalk)

---

## 1. Purpose & scope

Escalation is the deliberate, governed handoff that happens when an actor encounters a decision they cannot, may not, or should not make alone. KFM treats every such handoff as a **first-class event**: it has a named trigger, a named owning role, a named secondary reviewer where separation is required, and one or more receipts that record what was decided and why.

This document catalogs those handoffs. It is the **routing layer** between three other documents:

- `docs/governance/REVIEW_DUTIES.md` *(PROPOSED)* — what each reviewer is responsible for in steady state.
- `docs/governance/SEPARATION_OF_DUTIES.md` *(PROPOSED)* — which duty pairs may not collapse onto a single actor.
- `docs/runbooks/SENSITIVITY_ESCALATION.md` and `docs/runbooks/INCIDENT_RESPONSE.md` *(PROPOSED)* — step-by-step procedures.

**In scope** — the table of *when* to escalate, *to whom*, with *what receipts*, and *what outcome is acceptable*.

**Out of scope**:

- Object-family meaning. (`contracts/`)
- Field-level shape. (`schemas/`)
- Allow / deny / restrict / abstain machine decisions. (`policy/`)
- The mechanical CI gates. (`.github/workflows/`, `tests/`)
- Threat-modeling and exposure posture. (`docs/security/`)

> [!NOTE]
> KFM's operating-law invariant 9 — *separate policy-significant release duties when maturity justifies it* — is doctrine. The matrices below are the **PROPOSED** operational form of that doctrine for ADR review. Until the relevant ADRs are accepted, treat the routing rows as guidance, not enforced procedure.

[Back to top](#escalation--docsgovernanceescalationmd)

---

## 2. Roles roster

The roster below is reproduced from the *KFM Domains Culmination Atlas v1.1* §24.7.1 (PROPOSED) and matches the role names used throughout the Encyclopedia and the per-domain dossiers. Each row carries a **scope** (the artifacts and surfaces the role governs) and a **primary escalation partner** (the role most often paired with it when separation is required).

| Role | Scope | Primary escalation partner |
|---|---|---|
| **Source steward** | `SourceDescriptor` lifecycle; rights confirmation; sensitivity tag; admission gate. | Rights-holder representative (when rights are unclear) |
| **Domain steward** | Meaning of a domain's object families; contracts, schemas, validators; review of domain-internal promotions. | Sensitivity reviewer (sensitive lanes); Release authority (PUBLISHED transitions) |
| **Sensitivity reviewer** | Redaction, generalization, withholding, and tier transitions for sensitive content. `RedactionReceipt`. | Rights-holder representative; Release authority |
| **Rights-holder representative** | Sovereignty, cultural-heritage, and consent-based release decisions. Archaeology, sovereign data, living-person data, DNA data. | Release authority |
| **Release authority** | Issues `ReleaseManifest`; authorizes PUBLISHED transitions; authorizes rollback. Distinct from authorship when materiality applies. | Author (separation); Correction reviewer (post-publication) |
| **Correction reviewer** | Reviews `CorrectionNotice` / `RollbackCard` before they amend a PUBLISHED claim. | Release authority; Domain steward |
| **AI surface steward** | Focus Mode templates, `AIReceipt` sampling, cite-or-abstain audits, policy bindings on the AI surface. | Docs steward (policy binding); Domain steward |
| **Docs steward** | Governance documentation, ADR index, drift register, Atlas / supplement integrity. | At least one subsystem owner (per Directory Rules §15) |

> Status of the roster: **CONFIRMED doctrine** that these are the roles KFM intends to operate with; **PROPOSED** as the operational naming until ratified by ADR. Owner names and contact channels are placeholders pending a mounted repo with `CODEOWNERS` evidence.

[Back to top](#escalation--docsgovernanceescalationmd)

---

## 3. Escalation flow

The high-level flow below captures the most common shape of an escalation. A trigger fires inside the lifecycle; an owning role takes it; a secondary reviewer is added when separation is required or sensitivity is in play; the outcome is recorded as one or more receipts; and the original lifecycle transition either completes or fails closed.

```mermaid
flowchart TD
    T["Trigger fires<br/>(quarantine reason, sensitive event,<br/>AI incident, vendor distress, drift)"] --> O["Owning role takes the case<br/>(see §5 routing matrix)"]
    O --> S{"Separation<br/>required?"}
    S -->|"No"| D["Owning role decides<br/>(routine path)"]
    S -->|"Yes"| P["Pair with secondary reviewer<br/>(see §2 roster)"]
    P --> D
    D --> R["Receipts emitted:<br/>ReviewRecord · PolicyDecision ·<br/>RedactionReceipt · CorrectionNotice ·<br/>RollbackCard · AIReceipt"]
    R --> X{"Outcome"}
    X -->|"ALLOW / ANSWER"| C["Lifecycle transition completes;<br/>artifacts updated"]
    X -->|"RESTRICT / ABSTAIN"| H["Held at prior state;<br/>conditions recorded"]
    X -->|"DENY"| F["Fails closed;<br/>prior state preserved;<br/>reason recorded"]
    X -->|"ERROR"| E["Structured error;<br/>no silent fall-through"]
    C --> AU["Audit log + register update"]
    H --> AU
    F --> AU
    E --> AU
```

> [!TIP]
> Every leaf of this flow ends in **an audit-bearing receipt**, not in a verbal hand-wave. If an escalation cannot produce a receipt, the lifecycle stays at the prior state. This is the same fail-closed posture the trust membrane enforces at the public surface.

[Back to top](#escalation--docsgovernanceescalationmd)

---

## 4. Trigger catalog

Triggers are grouped by **the layer they originate in**. The reason codes are drawn from the *Domains Culmination Atlas v1.1* §24.6.3 (PROPOSED catalog) and the Master Decision Outcome Envelope reference (§24.3). They are the canonical machine-readable signals that an escalation has begun.

### 4.1 Lifecycle gate triggers

A lifecycle gate (Admission, Normalization, Validation, Catalog closure, Release, Correction, Rollback) emits a finite outcome — `PASS`, `FAIL`, `ALLOW`, `HOLD`, `DENY`, or `ERROR`. The non-routine outcomes below escalate.

| Trigger reason code | Where it fires | Default owning role | Receipt required to close |
|---|---|---|---|
| `MISSING_RECEIPT` / `MISSING_EVIDENCE` / `MISSING_REVIEW` | Normalization → Catalog → Release | Domain steward | Re-emitted receipt; `ValidationReport` pass |
| `SCHEMA_MISMATCH` / `CONTRACT_DRIFT` | Normalization / Validation | Domain steward + Contract/schema steward | Schema fix and/or ADR; `ValidationReport` pass |
| `RIGHTS_UNKNOWN` / `SENSITIVITY_UNRESOLVED` | Admission → Release | Source steward → Sensitivity reviewer | `PolicyDecision` + `ReviewRecord` (+ Rights-holder where applicable) |
| `ROLE_COLLAPSE` / `ROLE_DOWNCAST_FORBIDDEN` | Validation → Catalog → Release | Source steward + Domain steward | Restored source role; corrected `EvidenceBundle` |
| `REVIEW_NEEDED` / `REVIEW_INSUFFICIENT` / `REVIEW_REJECTED` | Catalog / Release | The reviewer named by the lane | `ReviewRecord` with outcome |
| `RELEASE_MANIFEST_INVALID` / `ROLLBACK_TARGET_MISSING` | Release | Release authority | Fixed `ReleaseManifest`; rollback target supplied |
| `CORRECTION_DERIVATIVES_UNRESOLVED` / `CORRECTION_PRIOR_RELEASE_MISSING` | Correction | Correction reviewer | Resolved derivatives; supersession entry |

### 4.2 Sensitivity / rights triggers

These escalate the moment the originating signal is observed, regardless of which gate would have fired next. They follow KFM's sensitivity-tier scheme (T0–T4) described in §6.

| Trigger | Default owning role | Required partners |
|---|---|---|
| Archaeology site coordinate at full precision | Sensitivity reviewer | Rights-holder representative (cultural / sovereignty) |
| Sensitive fauna or flora exact occurrence | Sensitivity reviewer | Domain steward |
| Living-person field exposure attempt | Sensitivity reviewer | Rights-holder representative (consent) |
| DNA segment / match-evidence handling | Sensitivity reviewer | Rights-holder representative + Release authority |
| Critical infrastructure detail at facility precision | Sensitivity reviewer | Release authority |
| Hazards surface used as alert / instruction authority | Release authority | Sensitivity reviewer (boundary holds) |
| Synthetic / reconstructed surface presented without Reality Boundary Note | AI surface steward | Domain steward |

> [!WARNING]
> The sensitive-lane defaults are **fail-closed**. An actor who is uncertain about rights, sovereignty, or sensitivity must escalate rather than proceed. There is no "publish and correct later" path for these triggers; the cost of failing safe is much smaller than the cost of failing open.

### 4.3 AI surface triggers

These follow the *Governed AI* doctrine: AI is interpretive, not the root truth source; `EvidenceBundle` outranks generated language.

| Trigger | Default owning role |
|---|---|
| Synthetic-claim incidence detected during `AIReceipt` audit | AI surface steward |
| ABSTAIN rate spike on a Focus Mode template | AI surface steward |
| Large new-reason spike in DENY reason distribution | AI surface steward + Policy steward |
| Uncited language returned as ANSWER | AI surface steward (severity → Release authority) |
| Direct model-runtime access attempt from a public client | AI surface steward + Security |
| Focus Mode template change | AI surface steward + Docs steward |

### 4.4 Source / vendor triggers

These follow the vendor-watchlist doctrine (Components Pass 10 §C9-07). The exemplar event is the 23andMe Chapter 11 filing of March 2025, used in the corpus as the reference case for vendor distress as a consent-relevant variable.

| Trigger | Default owning role |
|---|---|
| Upstream vendor enters distress (bankruptcy, sale, terms-of-service rewrite) | Source steward |
| Source rights change detected by watcher | Source steward + Rights-holder representative |
| Source freshness expired past declared cadence | Source steward (correction routed via Correction reviewer) |
| Source-role collapse risk (e.g., modeled → observed) | Domain steward |

### 4.5 Documentation / structural triggers

| Trigger | Default owning role |
|---|---|
| Path / schema / policy / source home conflict between docs and repo | Docs steward (`docs/registers/DRIFT_REGISTER.md` entry) |
| Atlas / supplement / dossier supersession | Docs steward + at least one subsystem owner |
| ADR-class change (Directory Rules §2.4) without an open ADR | Docs steward (block merge; open ADR) |
| Contradiction register entry that grows stale | Docs steward |

[Back to top](#escalation--docsgovernanceescalationmd)

---

## 5. Routing matrix

The matrix below collapses §4 into a single "trigger → owning role → required partner → outcome envelope" view. The outcome envelope refers to the finite outcomes defined in the *Domains Culmination Atlas v1.1* §24.3: `ALLOW`, `RESTRICT`, `DENY`, `HOLD`, `ERROR` for governance queues, and `ANSWER` / `ABSTAIN` / `DENY` / `ERROR` for runtime surfaces.

| Trigger family | Owning role | Required partner (separation) | Acceptable outcomes |
|---|---|---|---|
| Routine source admission | Source steward | — | `ALLOW` / `HOLD` / `DENY` / `ERROR` |
| Admission with unresolved rights / sovereignty | Source steward | Rights-holder representative | `ALLOW` (only with `PolicyDecision`+`ReviewRecord`) / `HOLD` / `DENY` |
| Normalization receipt (routine) | Domain steward | — | `ALLOW` / `HOLD` / `ERROR` |
| Normalization with sensitivity-relevant transform | Domain steward | Sensitivity reviewer | `ALLOW` / `RESTRICT` / `HOLD` / `DENY` |
| Validator authorship & run | Domain steward | Periodic audit by Docs steward | `PASS` / `FAIL` / `ERROR` |
| Promotion PROCESSED → CATALOG (non-sensitive) | Domain steward | — | `ALLOW` / `HOLD` / `DENY` |
| Promotion PROCESSED → CATALOG (sensitive lane) | Domain steward | Sensitivity reviewer | `ALLOW` / `RESTRICT` / `HOLD` / `DENY` |
| Release CATALOG → PUBLISHED (material change) | Release authority | Author ≠ Release authority; Rights-holder where applicable | `ALLOW` / `HOLD` / `DENY` |
| Sensitive-lane release | Release authority | Author + Sensitivity reviewer + Rights-holder | `ALLOW` (with full receipt stack) / `HOLD` / `DENY` |
| Correction / rollback (steward-significant) | Correction reviewer | Author / detector + Release authority | `ACCEPTED` / `HOLD` / `DENY` / `ERROR` |
| AI surface change (template or policy binding) | AI surface steward | Docs steward | `ALLOW` / `HOLD` / `DENY` |
| Atlas / supplement publication | Docs steward | At least one subsystem owner | `ALLOW` / `HOLD` / `DENY` |
| ADR-class structural change | Docs steward | At least one subsystem owner | `ALLOW` (only with accepted ADR) / `HOLD` |

> Status: **PROPOSED** routing per Atlas v1.1 §24.7.2. Author-and-approver overlap is permitted in low-materiality routine cases; as maturity rises, separation must be enforced through tooling, not custom.

[Back to top](#escalation--docsgovernanceescalationmd)

---

## 6. Sensitivity tier escalation

The tier scheme (T0 Open → T4 Denied) is the canonical KFM language for "how safely is this representation publishable?" An escalation that moves an object **toward T0** (more public) always requires both a transform receipt and a review record. An escalation that moves an object **toward T4** (less public) requires only a `CorrectionNotice`: correction alone is sufficient to remove or restrict.

| Tier transition | Direction | Required artifacts | Required reviewer | Reversibility |
|---|---|---|---|---|
| T4 → T3 | toward public | `PolicyDecision` + `ReviewRecord` + agreement | Steward + Rights-holder where applicable | Reversible via agreement revocation |
| T4 → T2 | toward public | `PolicyDecision` + `ReviewRecord` | Steward | Reversible via review revocation |
| T4 → T1 | toward public | `RedactionReceipt` + `ReviewRecord` | Steward | Reversible; redaction can be re-evaluated |
| T3 → T2 | toward public | `PolicyDecision` + `ReviewRecord` | Steward | Reversible |
| T2 → T1 | toward public | `RedactionReceipt` + `ReviewRecord` | Steward | Reversible |
| T1 → T0 | toward public | `ReleaseManifest` + `ReviewRecord` | Steward + Release authority | Reversible via `RollbackCard` |
| Any → T4 | toward restricted | `CorrectionNotice` + `ReviewRecord` | Steward + Rights-holder where applicable | Always permitted; precedes derivative invalidation |

> [!CAUTION]
> Two transitions **cannot be reached by any transform**:
> - **Archaeology — human remains / sacred sites** never relaxes below T3, and only under explicit named authorization.
> - **People/DNA — raw DNA segment data** never reaches a public tier; T3 only under explicit research agreement.
> - **Hazards — KFM as alert authority** holds at T4 forever. No transform permits KFM to act as an emergency-alert authority. *(Source: Atlas v1.1 §24.5.2.)*

[Back to top](#escalation--docsgovernanceescalationmd)

---

## 7. AI surface escalation

The AI surface (`Focus Mode` and any downstream story / explanation surfaces) has its own escalation envelope because generated language can fluently substitute for evidence if left unchecked.

**Required abstention.** ABSTAIN when `EvidenceBundle` is missing, citations cannot be validated, source roles conflict, temporal scope is insufficient, or the user asks for unsupported inference. *(Encyclopedia, AI behavior table.)*

**Required denial.** DENY direct `RAW` / `WORK` / `QUARANTINE` access, sensitive-location exposure, restricted personal/DNA inference, emergency-alerting replacement, or uncited authoritative claims.

**Escalation triggers (this surface only).**

| Indicator | Healthy posture (PROPOSED) | Escalates to |
|---|---|---|
| `AIReceipt` presence rate | 100% of Focus Mode answers | AI surface steward (any miss is an incident) |
| ABSTAIN rate by template | Visibly tracked; very low ABSTAIN suggests over-fitting, very high suggests evidence gaps | AI surface steward |
| DENY reason distribution | Stable; large new-reason spikes investigated | AI surface steward + Policy steward |
| Synthetic-claim incidence | Approaches zero; never silently | AI surface steward + Release authority |
| Focus Mode template change | n/a (always a change-managed event) | AI surface steward + Docs steward |

> [!IMPORTANT]
> AI suggestions are **never** approvals. A Focus Mode answer that suggests promoting, releasing, or correcting an artifact is interpreted as **a candidate that still owes the same receipts as any other candidate**. The trust-membrane anti-pattern of "AI generation routed through admin shortcut" is denied at the trust-membrane audit. *(Atlas v1.1 §24.9.2.)*

[Back to top](#escalation--docsgovernanceescalationmd)

---

## 8. Source / vendor distress escalation

A source-side incident — vendor distress, terms-of-service rewrite, sudden licensing change, ownership transfer, freshness collapse — is escalated through the source steward, with mandatory consent revalidation when consent-relevant.

**Canonical reference incident.** The corpus uses the 23andMe Chapter 11 filing (March 2025) as the named exemplar that vendor solvency is itself a consent-relevant variable, because a sale of customer data in bankruptcy can void prior consent assumptions. *(Components Pass 10 §C9-07.)*

**Routing.**

1. Watcher detects watchlist event → emits to source steward queue.
2. Source steward classifies severity:
   - **Routine** (e.g., minor licensing-page update with no scope change) → `ReviewRecord` only.
   - **Material** (ownership change, scope change, bankruptcy filing, ToS rewrite affecting downstream rights) → escalate to rights-holder representative + release authority.
3. **Consent-revalidation drill** runs against every active KFM consent grant under that vendor; ambiguous postures embargo until cleared.
4. Affected records are tier-reassigned per §6; downstream derivatives are invalidated per the correction discipline.
5. `CorrectionNotice` + `RollbackCard` emitted where PUBLISHED claims are affected.

> [!NOTE]
> Cadence, threshold definitions, and notification format for watchlist events are **NEEDS VERIFICATION** in the corpus. The vendor-watch SOP is on the proposed expansion list and will live at `docs/runbooks/VENDOR_WATCH.md` *(PROPOSED)* once authored.

[Back to top](#escalation--docsgovernanceescalationmd)

---

## 9. Process & tracking (PROPOSED)

The process below is the smallest useful flow that preserves auditability without prematurely committing to tooling.

1. **Detect.** A trigger fires from §4, either by a validator, a policy gate, a CI check, a steward review, a watcher, an AI surface audit, or a manual catch.
2. **File.** The detector opens an entry in the appropriate register:
   - Policy-gate or release-gate triggers → `control_plane/policy_gate_register.yaml` *(PROPOSED)* with a cross-reference to the originating receipt.
   - Drift between docs and repo → `docs/registers/DRIFT_REGISTER.md` *(PROPOSED)*.
   - Doctrine-or-source contradiction → `control_plane/contradiction_register.yaml` *(PROPOSED)*.
   - Verifiable but unverified claims → `docs/registers/VERIFICATION_BACKLOG.md` *(PROPOSED)*.
3. **Route.** The owning role from §5 picks up the case. If separation is required, the secondary reviewer is named at the time of pickup, not at the time of decision.
4. **Decide.** The owning role and (where required) the secondary reviewer produce the receipts named in §4 / §5.
5. **Close.** The lifecycle transition that triggered the escalation either completes (with the new receipts attached to the `EvidenceBundle`) or fails closed (with the reason recorded). Either way, the register entry moves to a closed state with links to the receipts.
6. **Audit.** Periodic Docs-steward audit reviews aged-out register entries, synthetic-claim incidence on the AI surface, separation-of-duties violations, and ADR completeness for §2.4 cases.

**SLA / cadence.** All time-bound numbers are **UNKNOWN** in the corpus and intentionally left placeholder here:

| Stage | Target (PROPOSED — NEEDS VERIFICATION) |
|---|---|
| Acknowledgement of a triggered escalation | `TODO` |
| Initial routing decision | `TODO` |
| Closure of routine (non-sensitive) escalations | `TODO` |
| Closure of sensitive-lane escalations | `TODO` |
| Periodic Docs-steward audit cadence | `TODO` |

> [!NOTE]
> SLAs encode operational maturity. They are written down only when the team has the capacity to honor them; writing a number that won't be met would weaken the rest of the document. Open an ADR (suggested title: *ADR-S-09 — Reviewer separation-of-duties threshold and tooling*) before pinning numbers.

[Back to top](#escalation--docsgovernanceescalationmd)

---

## 10. Anti-patterns

The list below names the failure modes most likely to corrode the escalation discipline. Each is reproduced from KFM's anti-pattern doctrine in the Atlas, the MapLibre dossier, and the trust-membrane discussion.

> [!WARNING]
> **Approving one's own release on a sensitive lane.** Separation-of-duties matrix §5; release authority must be distinct from the author when materiality applies. *(Atlas v1.1 §24.9.3.)*

> [!WARNING]
> **Documenting a change instead of validating it.** Docs are part of the working system but never substitute for validators, fixtures, or schema. An escalation note is not a receipt. *(Directory Rules / Atlas §24.9.3.)*

> [!WARNING]
> **Treating an AI summary or Story Node as an approval.** AI surface output is interpretive only; cite-or-abstain applies; promotion still requires the full receipt stack. *(Atlas §24.9.2.)*

> [!WARNING]
> **Promotion that "upgrades" a source role** (e.g., modeled → observed). Source role is fixed at admission; never upgraded by promotion. Escalate to the source steward instead. *(Atlas §24.9.3.)*

> [!WARNING]
> **Re-publishing a corrected claim without invalidating derivatives.** `CorrectionNotice` must list invalidated derivatives; `RollbackCard` is required where downstream is affected. *(Atlas §24.9.3.)*

> [!WARNING]
> **Silent migration between schema, policy, or source homes.** ADR is required per Directory Rules §2.4; migration plan and supersession entry are mandatory.

> [!WARNING]
> **Admin shortcut becomes the normal public path.** Admin / steward bypasses are explicitly constrained, documented, and kept out of the normal public route. An escalation triggered through an admin shortcut still owes the full receipt stack. *(Directory Rules; Governed AI doctrine.)*

[Back to top](#escalation--docsgovernanceescalationmd)

---

## 11. Open questions & verification backlog

These items are **NEEDS VERIFICATION** in the current corpus. Each should be retired by ADR, register entry, or mounted-repo evidence before any number in this document is treated as fact.

- **SLA numbers** for acknowledgement, routing, and closure (§9). UNKNOWN; needs ADR or runbook decision.
- **Channel and queue identifiers** (e.g., which queue source-steward queues live in, which channel rights-holder representatives are reachable through). UNKNOWN; needs CODEOWNERS + ops decision.
- **Vendor-watch cadence and threshold definitions** (§8). NEEDS VERIFICATION per Components Pass 10 §C9-07 open question.
- **Right-to-be-forgotten boundary** between tombstoning and erasure (referenced by Components Pass 10 §C5-09 / §C6-08; affects DNA / consent triggers).
- **ADR for reviewer separation-of-duties threshold and tooling** (suggested ID: `ADR-S-09`); pending.
- **ADR for sensitivity-tier scheme adoption** (suggested ID: `ADR-S-05`); pending.
- **Vendor-watch SOP** (suggested path: `docs/runbooks/VENDOR_WATCH.md`); not yet authored.
- **Drift register triage cadence** (suggested ID: `ADR-S-13`); pending.

Track these against `docs/registers/VERIFICATION_BACKLOG.md` *(PROPOSED)*.

[Back to top](#escalation--docsgovernanceescalationmd)

---

## 12. Related docs

The links below assume the `docs/` tree laid out in `docs/doctrine/directory-rules.md` §6.1. Until a mounted repo confirms the paths, treat them as **PROPOSED**.

- [`docs/governance/README.md`](./README.md) *(PROPOSED)* — governance landing page.
- [`docs/governance/REVIEW_DUTIES.md`](./REVIEW_DUTIES.md) *(PROPOSED)* — what each reviewer is responsible for.
- [`docs/governance/SEPARATION_OF_DUTIES.md`](./SEPARATION_OF_DUTIES.md) *(PROPOSED)* — which duty pairs may not collapse.
- [`docs/governance/STEWARD_CHARTERS.md`](./STEWARD_CHARTERS.md) *(PROPOSED)* — per-steward charter and scope.
- [`docs/governance/CONTRADICTION_HANDLING.md`](./CONTRADICTION_HANDLING.md) *(PROPOSED)* — how contradictions are recorded and resolved.
- [`docs/doctrine/directory-rules.md`](../doctrine/directory-rules.md) *(PROPOSED home)* — placement rules and ADR-required changes.
- [`docs/doctrine/authority-ladder.md`](../doctrine/authority-ladder.md) *(PROPOSED)* — canonical authority order.
- [`docs/doctrine/trust-membrane.md`](../doctrine/trust-membrane.md) *(PROPOSED)* — public-vs-internal boundary.
- [`docs/doctrine/lifecycle-law.md`](../doctrine/lifecycle-law.md) *(PROPOSED)* — RAW → PUBLISHED invariant.
- [`docs/runbooks/SENSITIVITY_ESCALATION.md`](../runbooks/SENSITIVITY_ESCALATION.md) *(PROPOSED)* — step-by-step sensitivity escalation procedure.
- [`docs/runbooks/INCIDENT_RESPONSE.md`](../runbooks/INCIDENT_RESPONSE.md) *(PROPOSED)* — operational incident response.
- [`docs/security/INCIDENT_RESPONSE.md`](../security/INCIDENT_RESPONSE.md) *(PROPOSED)* — security-side incident response.
- [`docs/registers/DRIFT_REGISTER.md`](../registers/DRIFT_REGISTER.md) *(PROPOSED)* — doctrine/code/path drift entries.
- [`docs/registers/VERIFICATION_BACKLOG.md`](../registers/VERIFICATION_BACKLOG.md) *(PROPOSED)* — open verification items.
- `control_plane/policy_gate_register.yaml` *(PROPOSED)* — machine-readable policy gate register.
- `control_plane/contradiction_register.yaml` *(PROPOSED)* — machine-readable contradiction register.

[Back to top](#escalation--docsgovernanceescalationmd)

---

## Appendix A — Reason-code crosswalk

<details>
<summary><strong>Click to expand:</strong> reason codes used in this document and their canonical source</summary>

The reason codes below are reproduced from the *Domains Culmination Atlas v1.1* §24.6.3 (PROPOSED catalog) and §24.3 (Master Decision Outcome Envelope). They are the canonical machine-readable signals that a gate has failed closed or that a runtime surface has refused to emit `ANSWER`.

| Code | Layer | Meaning | Recovery |
|---|---|---|---|
| `MISSING_RECEIPT` | Normalization → Release | A required receipt (`TransformReceipt`, `RedactionReceipt`, `RunReceipt`, `AIReceipt`, etc.) is absent. | Re-emit the receipt; re-run validator. |
| `MISSING_EVIDENCE` | Validation → Catalog | An `EvidenceRef` does not resolve to an `EvidenceBundle`. | Resolve the bundle; re-link the reference. |
| `MISSING_REVIEW` | Catalog / Release | A required `ReviewRecord` is missing. | Run the required review; supply the record. |
| `SCHEMA_MISMATCH` | Normalization / Validation | The object does not conform to its schema version. | Schema fix and/or ADR; re-run validator. |
| `CONTRACT_DRIFT` | Normalization / Validation | The object does not conform to its contract / vocabulary. | Contract correction; re-run validator. |
| `RIGHTS_UNKNOWN` | Admission → Release | Source rights are unconfirmed. | Steward review; rights resolution; tier reassignment. |
| `SENSITIVITY_UNRESOLVED` | Admission → Release | Sensitivity tag is unconfirmed. | Sensitivity reviewer; tier assignment. |
| `ROLE_COLLAPSE` | Validation → Release | Source role has been collapsed (e.g., aggregate cited as per-place observation). | Restore source role. |
| `ROLE_DOWNCAST_FORBIDDEN` | Validation → Release | Attempted to upgrade a source role (e.g., modeled → observed). | Refuse upcast; preserve original role. |
| `REVIEW_NEEDED` | Catalog / Release | A review is required but has not been performed. | Run the review. |
| `REVIEW_INSUFFICIENT` | Catalog / Release | A review was performed but is inadequate for the lane. | Re-run with the correct reviewer roster. |
| `REVIEW_REJECTED` | Catalog / Release | The review explicitly rejected the candidate. | Honor the rejection; hold or correct. |
| `RELEASE_MANIFEST_INVALID` | Release | The `ReleaseManifest` is malformed or incomplete. | Fix the manifest. |
| `ROLLBACK_TARGET_MISSING` | Release | No `RollbackCard` / rollback target is supplied. | Supply the rollback target. |
| `CORRECTION_DERIVATIVES_UNRESOLVED` | Correction | Downstream derivatives have not been identified or invalidated. | Resolve derivatives; supersession entry. |
| `CORRECTION_PRIOR_RELEASE_MISSING` | Correction | The `CorrectionNotice` does not reference its predecessor release. | Add the reference. |

</details>

<details>
<summary><strong>Click to expand:</strong> finite outcome envelopes used in routing decisions</summary>

| Outcome | When | Required artifacts | Public-surface effect |
|---|---|---|---|
| `ANSWER` | Evidence sufficient; policy permits; release allows; review (if required) recorded. | `EvidenceBundle` resolved; `PolicyDecision = allow`; `ReleaseManifest` applies. | Substantive answer with citation. |
| `ABSTAIN` | Evidence insufficient or AI cannot cite. | `AIReceipt` with reason; no claim emitted. | Non-substantive note with reason; never invents. |
| `DENY` | Policy / rights / sensitivity / release state forbids. | `PolicyDecision = deny` + reason_code; `AIReceipt` records denial. | Denial reason; offers alternative non-restricted surface where possible. |
| `ERROR` | Governed API cannot evaluate. | Error envelope with diagnostic code; no claim leakage. | Finite, actionable error; no silent fall-through. |
| `HOLD` | Promotion / release / correction paused pending a reviewer. | `ReviewRecord` pending; `PolicyDecision = hold`. | Surface remains in prior state; no silent rollback. |
| `PASS` / `FAIL` | Validator-class outcome. | `ValidationReport`. | Internal; promotion blocked on `FAIL`. |
| `ALLOW` / `RESTRICT` | Governance queue outcomes. | `ReviewRecord`. | Drives downstream lifecycle transition. |
| `ACCEPTED` | Correction-queue outcome. | `CorrectionNotice`. | Triggers supersession or rollback. |

</details>

[Back to top](#escalation--docsgovernanceescalationmd)

---

### Last reviewed

`TODO — set at merge time`

### Review burden

| Aspect | Value |
|---|---|
| Doc owner | `@kfm-docs-stewards` *(placeholder)* |
| Reviewers required for change | Docs steward + at least one subsystem owner; ADR required for changes that bend an invariant from Directory Rules §2.4 |
| Material-change protocol | Open a PR; reference the relevant ADR or register entry; surface the change in the next Docs-steward audit |

---

**Related** · [`README.md`](./README.md) · [`SEPARATION_OF_DUTIES.md`](./SEPARATION_OF_DUTIES.md) · [`STEWARD_CHARTERS.md`](./STEWARD_CHARTERS.md) · [`../doctrine/directory-rules.md`](../doctrine/directory-rules.md) · [`../runbooks/SENSITIVITY_ESCALATION.md`](../runbooks/SENSITIVITY_ESCALATION.md)

**Last updated:** `TODO` · [Back to top](#escalation--docsgovernanceescalationmd)
