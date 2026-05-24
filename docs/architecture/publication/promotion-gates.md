<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/architecture-publication-promotion-gates
title: Publication — Promotion Gates A–G
type: standard
version: v0.1
status: draft
owners: Release Manager · Docs Steward · NEEDS VERIFICATION
created: 2026-05-24
updated: 2026-05-24
policy_label: public
related:
  - README.md
  - RELEASE_GATES.md
  - release-state-machine.md
  - release-objects.md
  - rollback-and-correction.md
  - ../governed-api/LIFECYCLE_GATES.md
  - ../cross-domain/trust-membrane.md
  - ../../doctrine/lifecycle-law.md
  - kfm_unified_doctrine_synthesis.md#8
tags: [kfm, architecture, publication, promotion, gates, doctrine]
notes:
  - PROPOSED. Concise companion to RELEASE_GATES.md (detailed gate matrix).
  - Doctrine for gates A–G is CONFIRMED per kfm_unified_doctrine_synthesis.md §8.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Publication — Promotion Gates A–G

> *The seven governed transitions an artifact passes before it is `PUBLISHED`. A is admission; G is release. Every gate fails closed; none can be skipped.*

![status](https://img.shields.io/badge/status-draft-yellow)
![doctrine](https://img.shields.io/badge/doctrine-CONFIRMED-blue)
![path-status](https://img.shields.io/badge/path-PROPOSED-orange)
![gates](https://img.shields.io/badge/gates-A--G%20(7)-blue)

**Status:** draft · **Owners:** Release Manager · Docs Steward *(NEEDS VERIFICATION)* · **Last updated:** 2026-05-24

> [!IMPORTANT]
> **Publication is a governed state transition, not a file move** *(`README.md` §6; `lifecycle-law.md`; CONFIRMED)*. Promotion runs through gates A–G. **Skipping a gate is a doctrine violation**; each gate covers a distinct failure mode and exists because that failure has happened.

> [!NOTE]
> **This doc is the concise gate overview.** The detailed gate matrix, signers, evidence packs, and per-gate validators live in [`RELEASE_GATES.md`](RELEASE_GATES.md). The API-side request-time mapping lives in [`../governed-api/LIFECYCLE_GATES.md`](../governed-api/LIFECYCLE_GATES.md).

---

## Table of contents

1. [Scope](#1-scope)
2. [The seven gates — at-a-glance](#2-the-seven-gates--ataglance)
3. [Gate A — Source admission](#3-gate-a--source-admission)
4. [Gate B — Provenance](#4-gate-b--provenance)
5. [Gate C — Sensitivity](#5-gate-c--sensitivity)
6. [Gate D — Validation](#6-gate-d--validation)
7. [Gate E — Evidence closure](#7-gate-e--evidence-closure)
8. [Gate F — Review](#8-gate-f--review)
9. [Gate G — Release](#9-gate-g--release)
10. [Gate ordering and re-evaluation](#10-gate-ordering-and-reevaluation)
11. [Anti-patterns](#11-anti-patterns)
12. [Open questions and ADR triggers](#12-open-questions-and-adr-triggers)
13. [Related docs](#13-related-docs)
14. [Appendix](#14-appendix)

---

## 1. Scope

This doc names the seven promotion gates, what each one checks, what its DENY conditions look like, and where each runs. It is the **navigation surface** for the gate matrix; for the deep matrix with evidence packs and signers, see [`RELEASE_GATES.md`](RELEASE_GATES.md).

> [!TIP]
> **When this doc binds.** Designing or auditing a pipeline step, classifying a failure to a gate, training a new reviewer, or wiring a new validator into a gate.

[↑ Back to top](#top)

---

## 2. The seven gates — at-a-glance

> **Evidence basis:** `kfm_unified_doctrine_synthesis.md` §8 *(promotion gates A–G, CONFIRMED)*; `README.md` §7.

```mermaid
flowchart LR
  classDef g fill:#fff4e0,stroke:#d97706;
  classDef p fill:#c8e6c9,stroke:#1b5e20;
  A["A · Source admission"]:::g --> B["B · Provenance"]:::g --> C["C · Sensitivity"]:::g --> D["D · Validation"]:::g --> E["E · Evidence closure"]:::g --> F["F · Review"]:::g --> G["G · Release"]:::g --> PUB["PUBLISHED"]:::p
```

| Gate | Question | DENY produces | Authority |
|---|---|---|---|
| **A — Source admission** | Did the source admit with role and rights known? | `ABSTAIN` `evidence/unresolved` *(API)* | Connector / Source steward |
| **B — Provenance** | Is acquisition timestamped and traceable? | `ABSTAIN` `evidence/inconsistent-bundle` | Provenance receipt |
| **C — Sensitivity** | Joint posture under the four cross-lane invariants? | `DENY` `policy/sensitivity` | OPA bundle; sensitivity reviewer |
| **D — Validation** | Schema + domain validators satisfied? | `ERROR` `schema/invalid-response` | CI validators |
| **E — Evidence closure** | Every consequential claim resolves to a bundle? | `ABSTAIN` `evidence/unresolved` | Closure validator |
| **F — Review** | Steward review applied where required? | `ABSTAIN` / `DENY` `policy/review-required` | Steward queue |
| **G — Release** | Manifest entry + rollback target + signatures present? | `ABSTAIN` `release/no-manifest` or fail | Release plane |

[↑ Back to top](#top)

---

## 3. Gate A — Source admission

| Aspect | Detail |
|---|---|
| Question | Is the source admitted via `SourceDescriptor` with role and rights known? |
| Inputs | `SourceDescriptor`; connector receipt; rights manifest. |
| DENY conditions | Source role missing; rights unknown; ambiguous identity. |
| Receipt | Connector admission receipt. |
| Where it runs | At ingest, before `RAW` →  `WORK`. |

[↑ Back to top](#top)

---

## 4. Gate B — Provenance

| Aspect | Detail |
|---|---|
| Question | Is acquisition timestamped and traceable to a canonical source? |
| Inputs | Retrieval record; lineage chain. |
| DENY conditions | No retrieval record; lineage gap; provenance receipt missing. |
| Receipt | Provenance receipt referenced by `EvidenceBundle`. |
| Where it runs | After admission, before `WORK` → `PROCESSED`. |

[↑ Back to top](#top)

---

## 5. Gate C — Sensitivity

| Aspect | Detail |
|---|---|
| Question | Is the record's joint sensitivity posture correct under the four cross-lane invariants *(`cross-domain/cross-lane-relations.md`)*? |
| Inputs | `SensitivityPolicy`; cross-lane invariant validator. |
| DENY conditions | Joint posture downgraded; fail-closed lane exposed; aggregation used as sensitivity laundromat. |
| Receipt | `PolicyDecision` recording `sensitivity_posture`. |
| Where it runs | Before `PROCESSED`; re-evaluated at request time *(`governed-api/LIFECYCLE_GATES.md` §4.3)*. |

> [!CAUTION]
> **Aggregation does not lower sensitivity.** A county aggregate that includes a fail-closed class is still subject to the fail-closed posture unless the aggregation rule explicitly publishes the result *(k-anonymity, suppression, rounding)*.

[↑ Back to top](#top)

---

## 6. Gate D — Validation

| Aspect | Detail |
|---|---|
| Question | Does the record satisfy its schema and domain validators? |
| Inputs | JSON Schema; per-domain validators; cross-lane validator. |
| DENY conditions | Schema fail; validator fail; integrity mismatch. |
| Receipt | `ValidationReport` in `data/receipts/`. |
| Where it runs | On `PROCESSED` build; at request time for response shape. |

[↑ Back to top](#top)

---

## 7. Gate E — Evidence closure

| Aspect | Detail |
|---|---|
| Question | Does every consequential claim resolve to an `EvidenceBundle`? |
| Inputs | `EvidenceRef[]`; bundle resolver. |
| DENY conditions | Unresolved refs; bundle inconsistency *(role mismatch, sensitivity mismatch, role-preservation violation)*. |
| Receipt | `CitationValidationReport`. |
| Where it runs | At promotion to `PROCESSED`; re-run at every public surface request. |

> [!IMPORTANT]
> **Closure is a runtime fact, not a build-time fact.** Pointers can fail between releases *(deleted source, schema mismatch, manifest drift)*. The runtime checks closure on every public surface, not only at build.

[↑ Back to top](#top)

---

## 8. Gate F — Review

| Aspect | Detail |
|---|---|
| Question | Has steward review been applied where required? |
| Inputs | `ReviewRecord`; steward queue. |
| DENY conditions | Steward queue not cleared for the posture; review revoked. |
| Receipt | `ReviewRecord`. |
| Where it runs | Before `PROCESSED` → `PUBLISHED` for lanes requiring review *(fauna sensitive occurrences, archaeology exact location, etc.)*. |

[↑ Back to top](#top)

---

## 9. Gate G — Release

| Aspect | Detail |
|---|---|
| Question | Is the manifest entry present with a rollback target and valid signatures? |
| Inputs | `ReleaseManifest`; `RollbackCard`; signature receipts. |
| DENY conditions | No manifest; no rollback; receipt authority unresolvable; signature invalid. |
| Receipt | `ReleaseManifest` itself + `PromotionReceipt`. |
| Where it runs | Release plane; the final transition to `PUBLISHED`. |

> [!IMPORTANT]
> **`RollbackCard` is mandatory.** A release without a pre-staged rollback target is not a public release *(see [`rollback-and-correction.md`](rollback-and-correction.md))*.

[↑ Back to top](#top)

---

## 10. Gate ordering and re-evaluation

| Rule | Detail |
|---|---|
| Gates execute in order A → G | Earlier gate failure prevents later gate execution; A blocking → no B–G work. |
| Build-time vs request-time | Build-time enforcement is necessary but not sufficient; the governed API re-evaluates relevant gates per request *(`governed-api/LIFECYCLE_GATES.md` §3)*. |
| Re-evaluation triggers | Release event; policy bundle update; source rebind; review revocation. |
| Skipping a gate | Doctrine violation; release fails closed. |
| Hot-fix path | Runs through expedited Gates F/G, not around them. |

[↑ Back to top](#top)

---

## 11. Anti-patterns

| Anti-pattern | Mitigation |
|---|---|
| **Gate skipped under deadline pressure** | No skip; gate-skipping becomes precedent that erodes the trust path. |
| **Build-time validation treated as sufficient** | Runtime re-evaluation required; closure check on every public surface. |
| **Sensitivity downgraded post-Gate C via aggregation** | Aggregation does not lower sensitivity *(k-anonymity / suppression / rounding required)*. |
| **Release without `RollbackCard`** | Gate G denies. |
| **Steward review revoked silently** | Revocation is a release event; manifest reflects. |
| **Gate failure papered over with retry** | Failures are first-class; retry without diagnosis is drift. |

[↑ Back to top](#top)

---

## 12. Open questions and ADR triggers

| Open item | Class | Suggested ADR title |
|---|---|---|
| Gate matrix consolidation — the corpus has two forms *(synthesis §8 vs PMTiles publication-gate list)*; the existing [`RELEASE_GATES.md`](RELEASE_GATES.md) flags this CONFLICTED. | Doctrine | "Promotion-gate matrix consolidation". |
| Hot-fix path formal definition — expedited Gate F/G or new "H" gate? | Vocabulary | "Expedited promotion route". |
| Whether Gate B and Gate E should merge *(provenance is a kind of evidence closure)*. | Doctrine | "Gate B / Gate E merger". |
| Per-domain gate variation — should fail-closed lanes have additional gates? | Variation | "Per-lane gate extensions". |

[↑ Back to top](#top)

---

## 13. Related docs

| Reference | Role | Truth label |
|---|---|---|
| `README.md` *(this folder)* §7 | Landing summary of the gates | CONFIRMED doctrine |
| `RELEASE_GATES.md` *(sibling)* | Detailed gate matrix with signers, packs, validators | CONFIRMED doctrine *(CONFLICTED on matrix form)* |
| `release-state-machine.md` *(sibling)* | The states the gates connect | PROPOSED |
| `release-objects.md` *(sibling)* | Objects produced and consumed by each gate | PROPOSED |
| `rollback-and-correction.md` *(sibling)* | Gate-G `RollbackCard` requirement | PROPOSED |
| `../governed-api/LIFECYCLE_GATES.md` | API-side request-time mapping | PROPOSED |
| `../cross-domain/cross-lane-relations.md` | Four invariants enforced at Gates C and E | CONFIRMED doctrine |
| `../cross-domain/trust-membrane.md` §4 | Gates as the membrane crossings | CONFIRMED doctrine |
| `../../doctrine/lifecycle-law.md` | Parent doctrine for the invariant | CONFIRMED doctrine *(referenced)* |
| `kfm_unified_doctrine_synthesis.md` §8 | Promotion gates A–G canonical | CONFIRMED doctrine |

[↑ Back to top](#top)

---

## 14. Appendix

<details>
<summary><strong>14.1 Gate → outcome quick-reference</strong></summary>

```text
A — Source admission    →  ABSTAIN evidence/unresolved
B — Provenance          →  ABSTAIN evidence/inconsistent-bundle
C — Sensitivity         →  DENY    policy/sensitivity | fail-closed-lane
D — Validation          →  ERROR   schema/invalid-{request,response}
E — Evidence closure    →  ABSTAIN evidence/unresolved | ai/citation-unresolved
F — Review              →  ABSTAIN | DENY policy/review-required
G — Release             →  ABSTAIN release/{no-manifest,state-not-published,rollback-in-progress}
```

</details>

<details>
<summary><strong>14.2 Truth-label legend</strong></summary>

- **CONFIRMED** — verified this session from attached docs.
- **PROPOSED** — design / placement / inference not yet verified in implementation.
- **INFERRED** — derivable from confirmed evidence but not directly stated.
- **NEEDS VERIFICATION** — checkable, but not yet checked strongly enough to act as fact.

</details>

---

**Related (mini)** · [`README.md`](README.md) · [`RELEASE_GATES.md`](RELEASE_GATES.md) · [`release-state-machine.md`](release-state-machine.md) · [`release-objects.md`](release-objects.md) · [`rollback-and-correction.md`](rollback-and-correction.md) · [`../governed-api/LIFECYCLE_GATES.md`](../governed-api/LIFECYCLE_GATES.md)

**Last updated:** 2026-05-24 · **Doc version:** v0.1 · **Doc status:** draft · **Path status:** PROPOSED

[↑ Back to top](#top)
