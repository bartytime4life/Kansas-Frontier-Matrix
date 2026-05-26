<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/PATH_TBD_AFTER_REPO_INSPECTION
title: Sensitivity / Rights Tier Reference (Atlas v1.1 §24.5 register extract)
type: standard
version: v1
status: draft
owners: OWNER_TBD (sensitivity reviewer; release authority; sovereignty reviewer; docs steward)
created: 2026-05-25
updated: 2026-05-25
policy_label: public
related:
  - docs/atlases/KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.md
  - docs/atlases/KFM_Domains_Culmination_Atlas_v1_1.pdf
  - docs/atlases/source-role-anti-collapse.md
  - docs/atlases/stale-state-reference.md
  - docs/atlases/decision-outcome-envelope.md
  - docs/atlases/master-api-surface.md
  - docs/adr/ADR-S-05-sensitivity-tier-scheme.md
  - docs/standards/SENSITIVITY_RUBRIC.md
  - docs/standards/REDACTION_DETERMINISM.md
  - docs/registers/DRIFT_REGISTER.md
  - contracts/correction/redaction_receipt.md
  - contracts/correction/correction_notice.md
  - contracts/correction/representation_receipt.md
  - contracts/data/aggregation_receipt.md
  - contracts/governance/review_record.md
  - contracts/governance/policy_decision.md
  - contracts/release/release_manifest.md
  - contracts/release/rollback_card.md
  - schemas/contracts/v1/
  - policy/sensitivity/
  - policy/release/
  - policy/consent/
  - docs/doctrine/ai-build-operating-contract.md
  - docs/doctrine/directory-rules.md
tags: [kfm, atlas, register, sensitivity, rights, tier, T0-T4, deny-by-default, redaction, geoprivacy, sovereignty]
notes:
  - "Authority basis: faithful extraction of Atlas v1.1 §24.5. Atlas v1.1 explicitly states Chapter 24 tables are NAVIGATIONAL, not authoritative."
  - "EvidenceBundle, source dossiers, and schemas under schemas/contracts/v1/... remain the canonical sources for any specific claim (Atlas v1.1 Ch. 24 preamble)."
  - "Tier scheme T0-T4 is PROPOSED per §24.5.1; ADR-S-05 governs canonical adoption."
  - "Corpus-internal divergence: Pass 10 C6-01 uses a 0-5 rubric (6 levels); Atlas v1.1 §24.5 uses T0-T4 (5 tiers). Reconciliation is ADR-S-05 territory. See §12.1."
  - "Implementation depth (redaction profile libraries, validators, policy packages, schema headers) is PROPOSED throughout and requires mounted-repo verification."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Sensitivity / Rights Tier Reference

> **A navigational extract of Atlas v1.1 §24.5.** KFM publishes only the safest representation that still answers the steward's and the public's reasonable needs. Five tiers (T0 Open → T4 Denied) govern how every sensitive object family is released, with a uniform set of allowed transforms and required gates.

![status: draft](https://img.shields.io/badge/status-draft-yellow)
![authority: atlas-register · navigational](https://img.shields.io/badge/authority-atlas--register%20%C2%B7%20navigational-blue)
![doctrine basis: Atlas v1.1 §24.5](https://img.shields.io/badge/doctrine%20basis-Atlas%20v1.1%20%C2%A724.5-success)
![tier scheme: PROPOSED](https://img.shields.io/badge/tier%20scheme-T0%E2%80%93T4%20%C2%B7%20PROPOSED-yellow)
![open ADR: ADR-S-05](https://img.shields.io/badge/open%20ADR-ADR--S--05-orange)
![extends: v1.0 §20.5](https://img.shields.io/badge/extends-v1.0%20%C2%A720.5%20Deny--by--Default-lightgrey)
![corpus divergence: Pass 10 C6-01 0-5 rubric](https://img.shields.io/badge/divergence-Pass%2010%20C6--01-orange)

> [!IMPORTANT]
> **Status:** `draft`.
> **Authority:** Navigational extract. `CONFIRMED` doctrine for the §24.5 register body (extracted faithfully). The tier scheme itself is explicitly labeled `PROPOSED` in §24.5.1 of the source; ADR-S-05 governs canonical adoption.
> **Truth posture:** `CONFIRMED` doctrine framing (safest-representation principle, five tier classes, governed transitions) / `PROPOSED` tier names, transform vocabulary, per-domain defaults, schema paths, policy packages / `NEEDS VERIFICATION` mounted-repo presence of every contract, schema, policy, validator, receipt family / `UNKNOWN` repo implementation depth.
> **Open ADR:** [`ADR-S-05`](../adr/ADR-S-05-sensitivity-tier-scheme.md) — Sensitivity tier scheme (T0–T4) — adopt as canonical or revise (reconcile with Pass 10 C6-01 0–5 rubric).
> **Owner:** `OWNER_TBD`.

**Quick jumps:** [Purpose](#1-purpose-and-doctrine-framing) · [Tier scheme](#2-tier-scheme-§2451) · [Allowed transforms](#3-allowed-transforms-vocabulary) · [Per-domain tier matrix](#4-per-domain-tier-matrix-§2452) · [Tier transitions](#5-tier-transitions-§2453) · [Deny-by-Default Register cross-reference](#6-deny-by-default-register-cross-reference-§205) · [Enforcement surfaces](#7-enforcement-surfaces) · [Validators required](#8-validators-required) · [Implementation surface](#9-implementation-surface-proposed) · [Cross-references](#10-cross-references) · [Verification checklist](#11-verification-checklist) · [Open questions](#12-open-questions-and-verification-backlog)

---

## 1. Purpose and doctrine framing

`CONFIRMED doctrine — KFM publishes only the safest representation that still answers the steward's and the public's reasonable needs.` *(Atlas v1.1 §24.5 preamble.)*

`CONFIRMED doctrine — v1.0 §20.5 introduces a Deny-by-Default Register that names per-domain restrictions. This section extends it with a tier scheme, a uniform set of allowed transforms, and a uniform set of gates — so that 'publish at tier N' becomes a reviewable, repeatable action across domains.` *(Atlas v1.1 §24.5 preamble.)*

`CONFIRMED non-collapse rule — Chapter 24 master tables are navigational, not authoritative. EvidenceBundle, the source dossiers, and the schemas/contracts under schemas/contracts/v1/... (per Directory Rules §7.4 / ADR-0001) remain the canonical sources for any specific claim.` *(Atlas v1.1 Ch. 24 preamble.)* This standalone extract inherits the same non-collapse rule.

### 1.1 The safest-representation principle

| Principle | What it means | Operational consequence |
|---|---|---|
| **Publish only the safest representation that still answers the question.** | If a generalized layer answers the user's question, publish that — not the precise layer. | T0 is preferred only when no transform is needed; otherwise the lowest-tier *transform* that still serves the question is preferred over a higher-tier *unrestricted* publication. |
| **Sensitive content defaults to T4.** | Archaeology coords, sensitive fauna/flora, living-person fields, DNA, critical infrastructure, KFM-as-alert-authority all default to `T4 Denied`. | Lowering the tier requires explicit governed transition (§5). |
| **Transforms are reviewable.** | Generalization, fuzzing, aggregation, and redaction are not improvised — each transform produces a receipt that is auditable. | `RedactionReceipt`, `AggregationReceipt`, `RepresentationReceipt` are first-class artifacts (§3, §9.1). |
| **Tier transitions are governed.** | Moving content between tiers requires named artifacts and reviewers per §5. | No silent re-tiering; every transition leaves a `PolicyDecision` and a `ReviewRecord`. |

### 1.2 Visualization of the tier ladder

```mermaid
flowchart TD
    T4["<b>T4 — Denied</b><br/>Default for sensitive content<br/><i>Not released to any audience</i>"]
    T3["<b>T3 — Restricted</b><br/>Named agreement only"]
    T2["<b>T2 — Reviewer</b><br/>Stewards / reviewers / named collaborators"]
    T1["<b>T1 — Generalized</b><br/>Public with reviewed transform"]
    T0["<b>T0 — Open</b><br/>Public-safe, no transform"]

    T4 -- "PolicyDecision +<br/>ReviewRecord +<br/>agreement" --> T3
    T4 -- "PolicyDecision +<br/>ReviewRecord" --> T2
    T4 -- "RedactionReceipt +<br/>ReviewRecord" --> T1
    T3 -- "PolicyDecision +<br/>ReviewRecord" --> T2
    T2 -- "RedactionReceipt +<br/>ReviewRecord" --> T1
    T1 -- "ReleaseManifest +<br/>ReviewRecord" --> T0

    T0 -. "CorrectionNotice +<br/>ReviewRecord<br/>(downgrade)" .-> T4
    T1 -. .-> T4
    T2 -. .-> T4
    T3 -. .-> T4

    classDef deny fill:#fde8e8,stroke:#a94442,color:#5a1a1a
    classDef restrict fill:#fff5e6,stroke:#b07020,color:#5a3010
    classDef review fill:#fffce6,stroke:#a89020,color:#5a4a10
    classDef gen fill:#e8f3ff,stroke:#1f5fa8,color:#0b2c5a
    classDef open fill:#e8f5ee,stroke:#1f7a3f,color:#0b3a1c

    class T4 deny
    class T3 restrict
    class T2 review
    class T1 gen
    class T0 open
```

> [!NOTE]
> **Solid arrows = upgrade (toward more public).** Require both a transform receipt and a review record.
> **Dashed arrows = downgrade (toward more restrictive).** Require only a `CorrectionNotice` and review. *(Per §24.5.3 reading note.)*

[↑ back to top](#top)

---

## 2. Tier scheme (§24.5.1)

`PROPOSED — the tier scheme itself is explicitly labeled PROPOSED in Atlas v1.1 §24.5.1. ADR-S-05 governs canonical adoption.`

| Tier | Name | Definition *(PROPOSED, per §24.5.1)* | Default audience | Source citation |
|---|---|---|---|---|
| **T0** | **Open** | Public-safe with no transformations required; no rights, sensitivity, or steward gating beyond standard release. | Any public client via governed API. | `[ENCY]` `[MAP-MASTER]` |
| **T1** | **Generalized** | Public-safe only after generalization, fuzzing, aggregation, or redaction; transform is reviewed and recorded. | Any public client via governed API. | `[ENCY]` `[DOM-FAUNA]` `[DOM-FLORA]` |
| **T2** | **Reviewer** | Released only to authenticated reviewers or domain stewards; policy-bounded; correction path active. | Stewards, reviewers, named research collaborators. | `[ENCY]` `[DIRRULES]` |
| **T3** | **Restricted** | Released only under named agreement (rights, sovereignty, or consent) and recorded. | Named authorized parties only. | `[ENCY]` `[DOM-PEOPLE]` `[DOM-ARCH]` |
| **T4** | **Denied** | Not released to any audience; the existence of a record may be released only as steward review permits. | — | `[ENCY]` `[DOM-ARCH]` `[DOM-PEOPLE]` |

> [!CAUTION]
> **T4 Denied is unique.** Even the *existence* of a T4 record may be withheld; release of existence-only metadata requires explicit steward review. This is the strongest fail-closed posture in the register.

[↑ back to top](#top)

---

## 3. Allowed transforms vocabulary

`CONFIRMED doctrine — §24.5.1 T1 row names the four canonical transform categories: generalization, fuzzing, aggregation, and redaction.` `PROPOSED — concrete transform profiles are defined in Pass 10 C6 (Sensitivity, Redaction, and Geoprivacy). Their canonical-home filename is the responsibility of docs/standards/REDACTION_DETERMINISM.md (per Pass 10 C6-03 expansion direction).`

### 3.1 Transform categories

| Category | Definition | Typical profiles *(PROPOSED, per Pass 10 C6)* | Required receipt |
|---|---|---|---|
| **Generalization** | Reduce precision: snap to grid, aggregate to coarse cell, suppress fields. | Square grid (`ST_SnapToGrid`); hex grid (`H3`); coarse cell (e.g., 10 km block); k-anonymity overlay for living-people maps. | `RedactionReceipt` |
| **Fuzzing** *(display redaction)* | Deterministic jitter: seeded PRNG over `(spec_hash, occurrence_id)` so the same record always receives the same offset. | Uniform-within-radius; Laplace distribution *(display only; not formal DP)*. | `RedactionReceipt` with seed and profile id. |
| **Aggregation** | Replace per-record values with unit-level summaries; irreversible loss of individual-record fidelity. | County totals; tract aggregates; minimum-cell suppression; differential privacy (DP) for aggregates only. | `AggregationReceipt` |
| **Redaction** | Withhold fields entirely; replace with `WITHHELD` tombstone. | Field-level redaction; geometry withholding; centroid-only release; time-bucketing. | `RedactionReceipt` |

> [!IMPORTANT]
> **Determinism is required.** Per Pass 10 C6-03, "display-redaction jitter uses a PRNG seeded by `spec_hash` plus `occurrence_id` so the same record always receives the same offset." Random-each-render jitter would be **triangulable** — multiple snapshots over time would reveal the true location. Deterministic seeded jitter is reviewable and stable across renders.

### 3.2 No-redaction-profile-means-deny rule

`CONFIRMED corpus content — Master MapLibre v2.1 ML-Q-017: "No redaction profile means deny publish."`

If a sensitive object has no documented redaction profile, the default is `DENY` at the release queue. There is no "best-effort generalization" fallback path.

### 3.3 Differential privacy belongs to aggregates only

`CONFIRMED corpus content — Master MapLibre v2.1 ML-Q-015: "Differential privacy belongs to aggregates."`

Differential privacy provides formal privacy guarantees only for aggregate releases. Applying DP-style noise to per-record displays is fuzzing-with-DP-aesthetic, not differential privacy proper. The corpus is explicit *(Pass 10 C6-03)* that "Laplace distributions feel more DP-like but should not be confused with true differential privacy guarantees; jitter is for display obfuscation, not formal privacy proofs."

[↑ back to top](#top)

---

## 4. Per-domain tier matrix (§24.5.2)

`CONFIRMED doctrine — thirteen object-class rows, each with default tier, allowed transforms, and required gates, exactly as enumerated in Atlas v1.1 §24.5.2.` This section *extends* Atlas v1.0 §20.5 (Deny-by-Default Register and Sensitivity Matrix); it does not replace it.

| # | Domain / object class | Default tier | Allowed transforms *(PROPOSED)* | Required gates | Source citation |
|---|---|---|---|---|---|
| 1 | **Archaeology — site location** | **T4** | Steward review + cultural review + generalized geometry (coarse cell) + `RedactionReceipt` → T2 or T1. | `RedactionReceipt` + `ReviewRecord` + `PolicyDecision`. | `[DOM-ARCH]` |
| 2 | **Archaeology — human remains / sacred sites** | **T4** | No transform releases this to T0; T3 only under **explicit named authorization**. | Sovereignty review + `ReviewRecord` + `PolicyDecision`. | `[DOM-ARCH]` |
| 3 | **Fauna — sensitive occurrence** | **T4** | Geoprivacy generalization + `RedactionReceipt` → T1. | `RedactionReceipt` + `ReviewRecord` + `PolicyDecision`. | `[DOM-FAUNA]` |
| 4 | **Fauna — range polygon** | T1 | Aggregate / generalized public-safe layer. | `AggregationReceipt` or `RedactionReceipt`. | `[DOM-FAUNA]` |
| 5 | **Flora — rare or culturally sensitive plant location** | **T4** | Generalized geometry + steward review → T2 or T1. | `RedactionReceipt` + `ReviewRecord`. | `[DOM-FLORA]` |
| 6 | **People/DNA — living-person fields** | **T4** | Aggregation by tract or county + `AggregationReceipt` → T1. | Consent or aggregation gate + `ReviewRecord`. | `[DOM-PEOPLE]` |
| 7 | **People/DNA — raw DNA segment data** | **T4** | No transform releases this to a public tier; T3 only under explicit research agreement. | Named consent + `ReviewRecord` + `PolicyDecision`. | `[DOM-PEOPLE]` |
| 8 | **People/Land — private person-parcel join** | **T4** | Generalized parcel + de-identified person → T2 only. | `RedactionReceipt` + `ReviewRecord`. | `[DOM-PEOPLE]` |
| 9 | **Infrastructure — critical asset detail** | **T4** | Generalized facility footprint + suppressed dependency → T1. | Steward review + `RedactionReceipt`. | `[DOM-SETTLE]` |
| 10 | **Infrastructure — condition / vulnerability** | **T4** | T3 to named authorities only; **never T0 / T1**. | Steward review + named-party agreement. | `[DOM-SETTLE]` |
| 11 | **Hazards — KFM as alert authority** | **T4 forever** | **No transform** permits KFM to act as an emergency-alert authority. The boundary holds. | Policy boundary; `DENY` at runtime. | `[DOM-HAZ]` |
| 12 | **Governed AI — RAW / WORK access via AI surface** | **T4** | AI never reads RAW or WORK content; only released `EvidenceBundle`. | `PolicyDecision` + `AIReceipt`. | `[GAI]` |
| 13 | **Planetary/3D — sensitive 3D scene content** | **T4** | Generalization / clipping / withholding; Reality Boundary Note + Representation Receipt → T1 or T2 where steward review supports. | Steward review + `RedactionReceipt` + `RepresentationReceipt`. | `[MAP-MASTER]` `[UIAI]` |

### 4.1 Hard boundaries — rows that never reach T0

`CONFIRMED doctrine — three rows in §24.5.2 carry absolute boundaries that no transform can cross:`

| # | Object class | Hard boundary |
|---|---|---|
| 2 | Archaeology — human remains / sacred sites | "No transform releases this to T0." T3 only under explicit named authorization. |
| 7 | People/DNA — raw DNA segment data | "No transform releases this to a public tier." T3 only under explicit research agreement. |
| 10 | Infrastructure — condition / vulnerability | "T3 to named authorities only; never T0 / T1." |
| 11 | Hazards — KFM as alert authority | **"T4 forever."** No transform permits KFM to act as an emergency-alert authority. |

> [!WARNING]
> **Row 11 ("Hazards — KFM as alert authority") is the strongest single boundary in the register.** It is the only row labeled "T4 forever" with "the boundary holds." This is a doctrine-level commitment: KFM does not serve as an emergency-alert system, regardless of how operationally useful that would be.

### 4.2 Synthetic content interaction (§24.1 ↔ §24.5)

`CONFIRMED doctrine — row 13 (Planetary/3D — sensitive 3D scene content) requires both a Reality Boundary Note and a Representation Receipt before any tier-downgrade.` This is the §24.5 surface where the Source-Role Anti-Collapse register (§24.1, especially collapse pattern 6 "Synthetic content presented as observed reality") meets the tier scheme: synthetic content in sensitive domains compounds two fail-closed defaults.

See [`docs/atlases/source-role-anti-collapse.md`](./source-role-anti-collapse.md) §4 row 6 for the source-role enforcement and §7 row 7 for the sensitive-domain interlock.

[↑ back to top](#top)

---

## 5. Tier transitions (§24.5.3)

`CONFIRMED doctrine — six upgrade transitions (toward more public) plus one universal downgrade transition, each with required artifacts, required reviewer, and reversibility, exactly as enumerated in Atlas v1.1 §24.5.3.`

| From → To | Required artifact | Required reviewer | Reversibility *(CONFIRMED doctrine)* |
|---|---|---|---|
| **T4 → T3** | `PolicyDecision` + `ReviewRecord` + agreement | Steward + rights-holder where applicable | Reversible: agreement revocation returns object to T4 with `CorrectionNotice`. |
| **T4 → T2** | `PolicyDecision` + `ReviewRecord` | Steward | Reversible: review revocation returns object to T4. |
| **T4 → T1** | `RedactionReceipt` + `ReviewRecord` | Steward | Reversible: redaction can be re-evaluated; correction may demote a published T1 to T4. |
| **T3 → T2** | `PolicyDecision` + `ReviewRecord` | Steward | Reversible. |
| **T2 → T1** | `RedactionReceipt` + `ReviewRecord` | Steward | Reversible. |
| **T1 → T0** | `ReleaseManifest` + `ReviewRecord` | Steward + release authority | Reversible: rollback supported via `RollbackCard`. |
| **Any tier → T4 (downgrade)** | `CorrectionNotice` + `ReviewRecord` | Steward + rights-holder where applicable | **Always permitted**; precedes derivative invalidation. |

### 5.1 The asymmetric-discipline rule

`CONFIRMED doctrine reading note — "a tier upgrade (toward more public) always needs both a transform receipt and a review record; a tier downgrade (toward less public) never needs both — correction alone is sufficient to remove or restrict."` *(Atlas v1.1 §24.5.3 reading note.)*

This asymmetry is the fail-closed property of the register. Restricting access is always faster than expanding it:

- **Upgrading** (less restrictive) is friction-laden by design: review, transform receipt, named reviewer, agreement where applicable.
- **Downgrading** (more restrictive) requires only a `CorrectionNotice` and a `ReviewRecord` — and is "always permitted."

### 5.2 Derivative-invalidation rule

`CONFIRMED doctrine — Atlas v1.1 §24.5.3 row "Any tier → T4" notes downgrade "precedes derivative invalidation."`

When an object downgrades, every downstream derivative that depended on the prior tier must be invalidated:

- Tile sets that included the now-T4 layer.
- Exports and stories that cited the now-T4 record.
- Cached AI answers (`AIReceipt`s) that included the now-T4 content.
- API responses cached at the edge.

Cross-reference [`docs/atlases/stale-state-reference.md`](./stale-state-reference.md) §6 for the `CorrectionNotice` decision rule and §8 for the lineage artifacts inventory.

[↑ back to top](#top)

---

## 6. Deny-by-Default Register cross-reference (§20.5)

`CONFIRMED — Atlas v1.0 §20.5 introduces the Deny-by-Default Register and Sensitivity Matrix. §24.5 extends it without replacing it. Both registers remain canonical.`

The v1.0 §20.5 register names per-domain restrictions in the form *"domain / surface → denied by default → allowed only when → citation"*. The §24.5 extension adds:

- A tier scheme (T0–T4) replacing the implicit binary "denied-by-default vs. allowed."
- Uniform allowed transforms (generalization, fuzzing, aggregation, redaction).
- Uniform required gates per transition (§5).
- Per-object-class defaults (§4).

### 6.1 v1.0 §20.5 row → §24.5 mapping

| v1.0 §20.5 row | §24.5 equivalent rows | Tier mapping |
|---|---|---|
| Archaeology: exact sites, burial, human remains, sacred sites, looting-risk detail | §4 rows 1, 2 | T4 default |
| Fauna: exact sensitive occurrences, nests/dens/roosts/hibernacula/spawning | §4 row 3 | T4 default |
| Flora: exact rare/protected/culturally sensitive plant locations | §4 row 5 | T4 default |
| Infrastructure: critical assets, dependencies, condition detail | §4 rows 9, 10 | T4 default |
| People/DNA/Land: living-person private output, raw DNA ids, DNA segments, private person-parcel joins | §4 rows 6, 7, 8 | T4 default |
| Hazards: emergency instructions or KFM as alert authority | §4 row 11 | T4 forever |
| Governed AI: RAW/WORK access, uncited claims, direct model-public traffic | §4 row 12 | T4 (RAW/WORK access) |

> [!NOTE]
> v1.0 §20.5 remains the canonical "denied by default" enumeration. §24.5 layers the tier scheme on top so a reviewer can answer not just "is this denied?" but "what tier is this and what gates govern motion between tiers?"

[↑ back to top](#top)

---

## 7. Enforcement surfaces

`CONFIRMED corpus content — sensitivity enforcement spans admission, release, render, AI, export, and correction surfaces. Each has its own canonical home.`

| # | Surface | What it enforces *(per Atlas v1.1 §24.5 + §20.5)* | Canonical home for the enforcing artifact *(PROPOSED)* | Outcome on violation |
|---|---|---|---|---|
| 1 | **Admission** | `SourceDescriptor.sensitivity_tier` is set at admission alongside `source_role`; T4 default for sensitive object classes. | `contracts/source/source_descriptor.md` + `schemas/contracts/v1/source/source_descriptor.schema.json` + `policy/admission/sensitivity.rego` | Admission `DENY` if tier cannot be determined. |
| 2 | **Release queue** | T0/T1 release requires the transform receipts in §3.1; T2/T3 require named-party agreement; T4 blocks public release entirely. | `policy/release/sensitivity.rego` + `release/` review gates | Release `DENY` / `HOLD`. |
| 3 | **Render (map / UI / Evidence Drawer)** | Public surfaces consume only T0/T1 released content; T2+ visible only to authenticated audiences per `PolicyDecision`. | `policy/render/sensitivity.rego` + MapLibre layer registry guards | Render `DENY`; UI shows `GENERALIZED_GEOMETRY` or `RESTRICTED_ACCESS` *(per `ai-build-operating-contract.md` §22.2)*. |
| 4 | **AI / Focus Mode** | AI never reads RAW/WORK; only released `EvidenceBundle`. T4 content is invisible to the AI surface. | `policy/render/sensitivity.rego` + `AIReceipt` evaluator + Focus Mode citation evaluator | `ABSTAIN` / `DENY` *(per §4 row 12)*. |
| 5 | **Export / story / screenshot** | Exports inherit the source tier; cross-tier joins require explicit gate. | `policy/export/sensitivity.rego` *(per ADR-S-11 story/export receipt scope)* | Export `DENY` for cross-tier collapse. |
| 6 | **Correction / rollback** | Downgrade (Any → T4) requires `CorrectionNotice` + `ReviewRecord` + derivative invalidation; always permitted. | `policy/correction/sensitivity.rego` + `release/correction_notices/` | `ACCEPTED` (downgrade) / `HOLD` (if invalidation list incomplete). |
| 7 | **Consent (Pass 10 C6.d)** | Consent tokens (JWTs, GA4GH visas) governed at render with revocation endpoints introspected by PDP on every render. | `policy/consent/` *(per `KFM-P5-PROG-0007 ConsentDecision render gate`)* | `DENY` / `ABSTAIN` on revoked or expired consent. |

`NEEDS VERIFICATION — every policy and contract path above. Field names and package layout may differ from current repo state.`

[↑ back to top](#top)

---

## 8. Validators required

`CONFIRMED — Atlas v1.0 §20.5 implies validators for every Deny-by-Default row. PROPOSED — the validator table below decomposes those rows into per-collapse-pattern validators consistent with Atlas v1.0 §20.4 test catalogue conventions.`

| Validator | Negative case *(what it must reject)* | Expected outcome |
|---|---|---|
| **Tier-set-at-admission validator** | A `SourceDescriptor` whose `sensitivity_tier` is missing or ambiguous when source class implies sensitivity. | `DENY` admission |
| **Sensitive-default-T4 validator** | Any of the seven hard-boundary object classes (§4 rows 1, 2, 5, 7, 10, 11) admitted at a tier below T4 without an `EvidenceBundle` justifying the override. | `DENY` admission |
| **Transform-receipt-present validator** | A T1 release without a `RedactionReceipt` or `AggregationReceipt`. | `DENY` release *(per Pass 10 / Master MapLibre ML-Q-017 "No redaction profile means deny publish")*. |
| **Deterministic-jitter validator** | A `RedactionReceipt` whose jitter seed is non-deterministic or omits the `(spec_hash, occurrence_id)` seed concatenation. | `FAIL` *(per Pass 10 C6-03)*. |
| **DP-for-aggregates-only validator** | A per-record release that claims differential-privacy guarantees. | `FAIL` *(per Pass 10 C6-05; Master MapLibre ML-Q-015)*. |
| **Upgrade-discipline validator** | A tier upgrade (T4→T1, T2→T1, T1→T0) without both a transform receipt and a `ReviewRecord`. | `DENY` |
| **Downgrade-permitted validator** | A `CorrectionNotice` downgrade rejected for missing transform receipt. | The validator must **accept** the downgrade with only `CorrectionNotice` + `ReviewRecord` per §5.1 asymmetric-discipline rule. |
| **Derivative-invalidation validator** | A downgrade whose `CorrectionNotice` invalidation list omits known downstream derivatives (tiles, exports, AI receipts, caches). | `FAIL` |
| **Hard-boundary validator** | A release attempt for §4.1 row 2, 7, 10, or 11 at a tier the row forbids. | `DENY` (row 11 specifically: forever). |
| **Living-person T4 validator** | A `PersonAssertion` with living-person fields exposed below T4 without an `AggregationReceipt` and consent. | `DENY` |
| **AI-RAW-access validator** | An AI surface request that resolves to RAW or WORK content rather than `EvidenceBundle`. | `DENY` *(per §4 row 12)*. |
| **Alert-authority validator** | A response from Hazards/Air/Hydrology that frames KFM as an emergency-alert authority. | `DENY` *(per §4 row 11)*. |
| **Consent-revocation-honored validator** | A render that proceeds with a revoked or expired consent token. | `DENY` *(per Pass 10 C6.d; `KFM-P5-PROG-0007`)*. |
| **Embargo-honored validator** | A render that exposes content before its `embargo_until` timestamp. | `DENY` *(per Pass 10 C6.e Embargo and Render-Time Enforcement)*. |

`Validator filenames, exit-code contract, and orchestrator wiring are NEEDS VERIFICATION (see OPEN-DR-07 in directory-rules.md v1.1 §18.b).`

[↑ back to top](#top)

---

## 9. Implementation surface (PROPOSED)

`PROPOSED — every entry below is a design proposal grounded in §24.5 doctrine. Mounted-repo presence is NEEDS VERIFICATION for every row.`

### 9.1 Contracts (`contracts/`)

| Artifact | Path *(PROPOSED)* | Purpose |
|---|---|---|
| `SourceDescriptor` (sensitivity fields) | `contracts/source/source_descriptor.md` | Carries `sensitivity_tier` enum, `rights_status`, `sovereignty_marker`. |
| `RedactionReceipt` | `contracts/correction/redaction_receipt.md` | Records the transform profile, parameters, seed (if deterministic), and reviewer for any T4→T1 / T2→T1 motion. |
| `AggregationReceipt` | `contracts/data/aggregation_receipt.md` | Records the aggregation unit, minimum-cell suppression, and DP-noise parameters (for aggregate-only DP). |
| `RepresentationReceipt` | `contracts/correction/representation_receipt.md` | Required companion to synthetic content release (row 13). |
| `RealityBoundaryNote` | `contracts/source/reality_boundary_note.md` *(or)* `contracts/correction/` | Required for synthetic content (row 13). |
| `ReviewRecord` | `contracts/governance/review_record.md` | Required for every tier transition. |
| `PolicyDecision` | `contracts/governance/policy_decision.md` | Required for upgrades to T2/T3 and all renders. |
| `CorrectionNotice` | `contracts/correction/correction_notice.md` | Required for every downgrade. |
| `ConsentSidecar` / `ConsentDecision` | `contracts/consent/consent_sidecar.md` *(or)* `contracts/governance/consent_decision.md` | Per Pass 10 C6.d and `KFM-P5-PROG-0007`. |

### 9.2 Schemas (`schemas/contracts/v1/…`)

Each contract above has a corresponding schema home per ADR-0001 (`schemas/contracts/v1/<family>/<object>.schema.json`). Required schema features:

- `sensitivity_tier` enum on every claim-bearing DTO, constrained to `T0 | T1 | T2 | T3 | T4`.
- `redaction_profile_id` reference field on every `RedactionReceipt` (linked to the redaction-profile catalog).
- `aggregation_unit` and `minimum_cell_count` fields on every `AggregationReceipt`.
- `jitter_seed_basis` field on `RedactionReceipt` (per Pass 10 C6-03 determinism rule).
- `superseded_by` lineage field on every `PolicyDecision` and `RedactionReceipt` to enable supersession per [`docs/atlases/stale-state-reference.md`](./stale-state-reference.md) §3.

### 9.3 Policy (`policy/`)

`PROPOSED policy packages — exact layout may warrant ADR per Directory Rules §2.4:`

- `policy/admission/sensitivity.rego` — enforces T4-default for sensitive object classes (§7 row 1).
- `policy/release/sensitivity.rego` — enforces transform-receipt-required and upgrade-discipline (§7 row 2; §8 validators).
- `policy/render/sensitivity.rego` — enforces render-time tier check; integrates with PDP introspection per Pass 10 C6.e (§7 rows 3, 4).
- `policy/export/sensitivity.rego` — enforces export-tier inheritance (§7 row 5).
- `policy/correction/sensitivity.rego` — enforces downgrade discipline + derivative invalidation (§7 row 6).
- `policy/consent/render.rego` — per `KFM-P5-PROG-0007 ConsentDecision render gate` (§7 row 7).

### 9.4 Standards documentation (`docs/standards/`)

| Standard doc | Path *(PROPOSED)* | Purpose |
|---|---|---|
| Sensitivity Rubric | `docs/standards/SENSITIVITY_RUBRIC.md` | Per Pass 10 C6-01. Defines the canonical tier scheme and per-class defaults. **`NEEDS VERIFICATION` whether this is T0–T4 or 0–5 — ADR-S-05 reconciles.** |
| Redaction Determinism | `docs/standards/REDACTION_DETERMINISM.md` | Per Pass 10 C6-03. Defines seed concatenation rules for deterministic jitter. |
| Redaction Profile Catalog | `docs/standards/REDACTION_PROFILES.md` *(PROPOSED)* | Per Pass 10 C6-02. Lists all named profiles (radius mask, grid, jitter, DP, centroid, time-bucketing) with versioning. |

### 9.5 Receipts (`data/receipts/`)

`CONFIRMED — receipt families per Atlas v1.1 §24.2 Receipt Catalog. PROPOSED — the following receipt patterns relate directly to sensitivity:`

| Receipt | Role |
|---|---|
| `RedactionReceipt` | Emitted on every T4→T1 / T2→T1 transform. |
| `AggregationReceipt` | Emitted on every aggregation, with `minimum_cell_count`. |
| `RepresentationReceipt` | Emitted alongside synthetic content release (row 13). |
| `ConsentDecisionReceipt` *(PROPOSED)* | Emitted by the consent render gate. |
| `CorrectionReceipt` | Emitted alongside every downgrade. |
| `EmbargoReceipt` *(PROPOSED)* | Emitted when content moves out of embargo (Pass 10 C6.e). |

### 9.6 Fixtures (`fixtures/`)

`PROPOSED per directory-rules.md v1.2 §6.6 fixture substructure (valid/ + invalid/):`

- `fixtures/sensitivity/valid/t4_archaeology_site_denied.json`
- `fixtures/sensitivity/valid/t1_fauna_range_polygon_aggregated.json`
- `fixtures/sensitivity/valid/t1_living_person_aggregated_to_county.json`
- `fixtures/sensitivity/invalid/t4_archaeology_site_published_without_receipt.json`
- `fixtures/sensitivity/invalid/living_person_record_at_t0.json`
- `fixtures/sensitivity/invalid/kfm_emergency_alert_authority_claim.json`
- `fixtures/sensitivity/invalid/synthetic_3d_scene_without_reality_boundary_note.json`
- `fixtures/sensitivity/invalid/ai_surface_reading_raw_evidence.json`
- `fixtures/sensitivity/invalid/jitter_non_deterministic_seed.json`
- `fixtures/sensitivity/invalid/dp_applied_to_per_record_display.json`

[↑ back to top](#top)

---

## 10. Cross-references

### 10.1 Other `docs/atlases/` register extracts

| Register | Relationship to this register |
|---|---|
| [`docs/atlases/source-role-anti-collapse.md`](./source-role-anti-collapse.md) *(extract of §24.1)* | Source role and sensitivity tier are sibling fields on `SourceDescriptor`, both fixed at admission. Synthetic content (collapse pattern 6) and sensitive-domain interlock (§7 row 7 of source-role register) interact directly with §4 row 13 of this register. |
| [`docs/atlases/stale-state-reference.md`](./stale-state-reference.md) *(extract of §24.8)* | Stale-state marker 7 (Rights status changed) interacts directly with §5 tier-transitions: a rights change can demote a published tier. §5.2 derivative-invalidation rule cross-references the §6 correction-vs-stale decision rule in stale-state. |
| [`docs/atlases/decision-outcome-envelope.md`](./decision-outcome-envelope.md) *(extract of §24.3)* | §7 enforcement surfaces use the envelope vocabulary `DENY` / `ABSTAIN` / `HOLD` / `ERROR` for sensitivity outcomes. |
| [`docs/atlases/master-api-surface.md`](./master-api-surface.md) *(extract of §20.3)* | Every governed API family carries `sensitivity_tier` in its DTO; the API-family enforcement is at §7 row 2 (release) and row 3 (render). |

### 10.2 Other Atlas v1.1 Chapter 24 registers

| Register | Relationship to this register |
|---|---|
| Atlas v1.1 §24.2 Master Receipt Catalog | Defines `RedactionReceipt`, `AggregationReceipt`, `RepresentationReceipt`, `CorrectionNotice` receipt types referenced in §3 and §9.1. |
| Atlas v1.1 §24.6 Pipeline Gate Reference (RAW → PUBLISHED) | Sensitivity gates fire at Validation, Release, and Correction transitions in §24.6.1. |
| Atlas v1.1 §24.7 Reviewer Role and Separation-of-Duties Matrix | Sensitive-lane release "No" entries (author ≠ release authority) interact with §5 tier transitions. |
| Atlas v1.1 §24.9.2 Trust-membrane anti-patterns | Row "Sensitive content released without redaction" is the anti-pattern view of §3.2 no-redaction-profile-means-deny rule. |
| Atlas v1.1 §24.10 Master Risk Register | Multiple High-severity sensitivity rows (sensitive coordinates leaked via tile/vector/3D; living-person data exposed via inference; rights status changed without re-evaluation). |
| Atlas v1.1 §24.11.2 Sensitivity health indicators | "Sensitive-content side-channel audit" frequency; "Review-aged-out incidence." |

### 10.3 Atlas v1.0 anchors (retained verbatim in v1.1)

- **Atlas v1.0 §20.5 "Deny-by-Default Register and Sensitivity Matrix"** — the base register that §24.5 extends. See §6 above for the row-by-row mapping.
- **Atlas v1.0 §20.4 row "Sensitivity redaction"** — names domains (Archaeology, Fauna, Flora, Infrastructure, People/DNA, 3D) where exact public geometry is `DENY` by default.

### 10.4 Pass 10 — Sensitivity, Redaction, and Geoprivacy (C6)

| Idea | Subject | Status | Relevance |
|---|---|---|---|
| **C6-01** | Sensitivity Rubric 0–5 | `CONFIRMED` (Pass 10) | **Corpus-internal divergence with §24.5.1 T0–T4 — ADR-S-05 territory.** See §12.1. |
| **C6-02** | Redaction Profiles (named library) | `CONFIRMED` (Pass 10) | Defines the named-profile vocabulary referenced in §3 and §9.4. |
| **C6-03** | Seeded, Reproducible Jitter | `CONFIRMED` (Pass 10) | Determinism rule applied in §3.1 fuzzing row and §8 deterministic-jitter validator. |
| **C6-04** | Grid Generalization (Square or Hex) | `CONFIRMED` (Pass 10) | Generalization mechanism for §3.1. |
| **C6-05** | Differential Privacy (aggregates only) | `CONFIRMED` (Pass 10) | Applied in §3.3 DP-for-aggregates-only rule and §8 validator. |
| **C6-06** | k-anonymity | `CONFIRMED` (Pass 10) | Living-people overlay rendering rule. |
| **C6-07** | Consent Tokens (JWTs, GA4GH visas, revocation) | `CONFIRMED` (Pass 10) | Applied in §7 row 7. |
| **C6-08** | Embargo and Render-Time Enforcement | `CONFIRMED` (Pass 10) | Applied in §8 embargo-honored validator. |

### 10.5 Open ADRs

| ADR | Subject | Relationship |
|---|---|---|
| **ADR-S-05** | Sensitivity tier scheme (T0–T4) — adopt as canonical or revise | The primary open question this register surfaces. See §12.1. |
| **ADR-S-04** | Source-role vocabulary v1 | Source role and sensitivity tier are sibling fields on `SourceDescriptor`; their vocabularies must co-evolve. |
| **ADR-S-11** | Story / export receipt scope and retention | Governs §7 row 5 export-tier inheritance. |
| **ADR-S-12** | Two-person-rule scope for T3/T4 promotion | Per `kfm_unified_doctrine_synthesis.md` §49 ADR backlog row 12. |
| **ADR-S-14** | Cross-lane join policy | Bears on row 8 (private person-parcel join) and row 6 (living-person aggregate). |

### 10.6 Doctrinal anchors

- `ai-build-operating-contract.md` §22.2 UI negative states (`DENIED_BY_POLICY`, `GENERALIZED_GEOMETRY`, `RESTRICTED_ACCESS`) — names the UI states surfaced at §7 row 3.
- `ai-build-operating-contract.md` §23.1 sensitive-domain list — corroborates §4 per-domain matrix.
- `directory-rules.md` v1.2 §7.4 + ADR-0001 — grounds §9.2 schema home.

[↑ back to top](#top)

---

## 11. Verification checklist

- [ ] Confirm Atlas v1.1 §24.5 is faithfully reproduced in §2 (tier scheme, five tiers), §4 (per-domain matrix, thirteen rows), and §5 (tier transitions, seven rows). No row should be substituted or paraphrased to a meaning change.
- [ ] Confirm Atlas v1.0 §20.5 Deny-by-Default Register is preserved as canonical alongside this extension (§6).
- [ ] Confirm `contracts/source/source_descriptor.md` carries `sensitivity_tier`, `rights_status`, and `sovereignty_marker` fields.
- [ ] Confirm `schemas/contracts/v1/source/source_descriptor.schema.json` constrains `sensitivity_tier` to `T0 | T1 | T2 | T3 | T4` per ADR-S-05 acceptance (or the alternative vocabulary if ADR-S-05 adopts a different scheme).
- [ ] Confirm `RedactionReceipt`, `AggregationReceipt`, `RepresentationReceipt` contracts and schemas exist per §9.1 + §9.2.
- [ ] Confirm `policy/sensitivity/`, `policy/release/sensitivity.rego`, `policy/render/sensitivity.rego`, `policy/consent/render.rego` packages exist per §9.3.
- [ ] Confirm `docs/standards/SENSITIVITY_RUBRIC.md`, `docs/standards/REDACTION_DETERMINISM.md`, and `docs/standards/REDACTION_PROFILES.md` exist or are filed as routine PRs.
- [ ] Confirm the validator suite in §8 is wired through the validator orchestrator (per OPEN-DR-07).
- [ ] Confirm `fixtures/sensitivity/{valid,invalid}/` exists with at least the negative fixtures enumerated in §9.6.
- [ ] Confirm `ADR-S-05` is filed under `docs/adr/`; resolution status `NEEDS VERIFICATION`.
- [ ] Confirm the corpus-internal divergence between Pass 10 C6-01 (0–5 rubric) and §24.5.1 (T0–T4 tier scheme) is recorded in `docs/registers/DRIFT_REGISTER.md` pending ADR-S-05 resolution.
- [ ] Confirm row 11 (Hazards — KFM as alert authority, T4 forever) has runtime enforcement in `policy/release/hazards/` and is tested.
- [ ] Confirm row 12 (Governed AI — RAW/WORK access via AI surface, T4) has runtime enforcement consistent with `ai-build-operating-contract.md` §10 invariants.
- [ ] Confirm the consolidated Atlas Markdown carrier at `docs/atlases/KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.md` continues to carry §24.5 verbatim; if this standalone extract diverges, file the divergence to `docs/registers/DRIFT_REGISTER.md`.

[↑ back to top](#top)

---

## 12. Open questions and verification backlog

### 12.1 ADR-class (require an Architecture Decision Record)

- **`OPEN-ADR-S-05`** — Sensitivity tier scheme (T0–T4) — adopt as canonical or revise.
  - **Corpus-internal divergence to reconcile.** Atlas v1.1 §24.5.1 uses **T0–T4 (5 tiers)**: Open, Generalized, Reviewer, Restricted, Denied. Pass 10 C6-01 uses a **0–5 sensitivity rubric (6 ranks)**: 0 public/open, 1 common non-sensitive, 2 watchlist, 3 SINC/locally sensitive, 4 threatened/rare, 5 sacred/critical fail-closed. ADR-S-05 must decide:
    - Whether T0–T4 or 0–5 is canonical.
    - The mapping if both are retained for different purposes (e.g., T0–T4 for release-tier, 0–5 for per-record `sensitivity_rank`).
    - Schema migration path for fixtures and receipts authored under the other scheme.
  - Until ADR-S-05 is accepted, both schemes exist in the corpus and this register surfaces both with `PROPOSED` labels.
- **`OPEN-ADR-S-12`** — Two-person-rule scope for T3/T4 promotion. Per `kfm_unified_doctrine_synthesis.md` §49 row 12: when does separation-of-duties tooling enforcement become mandatory for tier upgrades?
- **`OPEN-ADR-S-11`** — Story / export receipt scope and retention. Governs §7 row 5.
- **`OPEN-ADR-PROPOSED`** — Whether `policy/sensitivity/` is one cross-cutting package or distributed across `policy/{admission,release,render,export,correction,consent}/`. §9.3 currently splits across surfaces; alternative single-package layout may warrant an ADR.
- **`OPEN-ADR-PROPOSED`** — Whether `docs/standards/SENSITIVITY_RUBRIC.md` is the canonical home for the tier scheme (per Pass 10 C6-01 expansion direction "Author the rubric document") or whether the canonical home is the per-root `policy/sensitivity/README.md`.

### 12.2 Repo-presence (require mounted-repo inspection)

- Every contract, schema, policy, validator, fixture, receipt path named in §9.
- The exact filenames of ADR-S-05, ADR-S-11, ADR-S-12 once filed.
- The exact validator orchestrator entry point (per OPEN-DR-07).
- Whether the redaction-profile catalog (Pass 10 C6-02) has been authored.
- Whether row 11 (KFM as alert authority) has runtime `DENY` enforcement and where it is tested.
- Whether row 12 (AI surface RAW/WORK denial) has runtime tests verifying no AI request resolves to RAW/WORK.

### 12.3 Doctrine-stability (route through `docs/registers/DRIFT_REGISTER.md` if divergence is observed)

- Drift between Atlas v1.1 §24.5 and this extract — Atlas v1.1's own conflict rule applies.
- Drift between Pass 10 C6-01 and §24.5.1 — pending ADR-S-05; should be filed as a known drift.
- Drift between Atlas v1.0 §20.5 row text and §24.5.2 row text — v1.0 retains authority over its original content per Atlas v1.1 Appendix G G.3.

### 12.4 Cross-register coherence

- §24.5 (this register) and §24.1 (source-role) share `SourceDescriptor` as the carrying object. Verify their schema fields do not conflict in the canonical `source_descriptor.schema.json`.
- §24.5 §5 tier transitions and §24.8 §3 supersession lineage (`SourceDescriptor` row): a `superseded_by` link MAY co-exist with a `sensitivity_tier` downgrade — verify the schema permits both lineage paths on the same descriptor.
- §24.5 §3.3 DP-for-aggregates-only rule and §24.5 §4 row 6 (living-person aggregation) must be tested together for consistency.

[↑ back to top](#top)

---

<details>
<summary><strong>Appendix A — Evidence basis (source ledger)</strong></summary>

| Source | Status | Supports | Limits |
|---|---|---|---|
| Atlas v1.1 §24.5 "Master Sensitivity / Rights Tier Reference (extends v1.0 §20.5)" | `CONFIRMED corpus content` | The doctrine framing (§1), the five-tier scheme (§2), the thirteen per-domain rows (§4), and the seven tier-transition rows (§5). | Atlas-level register; per its own Ch. 24 preamble, navigational not authoritative. The tier scheme itself is explicitly `PROPOSED` in §24.5.1. |
| Atlas v1.0 §20.5 "Deny-by-Default Register and Sensitivity Matrix" | `CONFIRMED corpus content` | The base register that §24.5 extends. §6 above maps each v1.0 row to §24.5 equivalents. | v1.0 register; unchanged per Atlas v1.1 Appendix G G.3. |
| Atlas v1.0 §20.4 row "Sensitivity redaction" | `CONFIRMED corpus content` | Names the six domains where exact public geometry is `DENY` by default. | Validator-catalogue row; not enforcement authority. |
| Atlas v1.1 §24.10 Master Risk Register sensitivity rows | `CONFIRMED corpus content` | High-severity sensitivity risks (sensitive coordinates leakage; living-person data inference; rights status changed). | Planning view; not implementation. |
| Atlas v1.1 §24.11.2 Sensitivity health indicators | `CONFIRMED corpus content` | "Sensitive-content side-channel audit" and "Review-aged-out incidence" indicators. | Health indicators; doctrine, not implementation. |
| Atlas v1.1 §24.12 OPEN-ADR Backlog row 5 (ADR-S-05) | `CONFIRMED open question` | The §12.1 ADR-S-05 reconciliation question. | Names the question; does not resolve. |
| `KFM_Components_Pass_10_Idea_Index_Category_Atlas_and_Expansion_Dossier.pdf` §6.6 Category C6 (Sensitivity, Redaction, and Geoprivacy) | `CONFIRMED corpus content` | The 0–5 rubric divergence (§12.1); transform-profile vocabulary (§3); determinism rule (§3.1); DP-for-aggregates-only (§3.3); consent tokens (§7 row 7); embargo (§8 embargo-honored validator). | Idea-index entries; not implementation proof. |
| `kfm_unified_doctrine_synthesis.md` §15 + §16 | `CONFIRMED doctrine reference` | Corroborates the tier scheme T0–T4 and the per-domain sensitivity matrix; adds explicit "tier transitions are governed" framing. | Cross-document doctrine synthesis. |
| `Master_MapLibre_Components-Functions-Features_v2.1_FULL.md` ML-Q-013 through ML-Q-021 | `CONFIRMED corpus content` | "No redaction profile means deny publish" (ML-Q-017); "DP belongs to aggregates" (ML-Q-015); "Sensitivity policy maps to radius grid" (ML-Q-016); "Revocation issues tombstone new" (ML-Q-018). | MapLibre-master idea anchors; not implementation. |
| `ai-build-operating-contract.md` §22.2 UI negative states + §23.1 sensitive-domain list | `CONFIRMED doctrine` | Names the UI states surfaced at §7 row 3 and corroborates the §4 per-domain matrix. | Doctrine, not implementation. |
| `KFM-P5-PROG-0007 ConsentDecision render gate` | `PROPOSED implementation` / `CONFIRMED card content` | Grounds §7 row 7 consent enforcement and §9.3 `policy/consent/render.rego` path. | Idea card; not implementation proof. |
| `directory-rules.md` v1.2 §6.6 fixture substructure + §7.4 + ADR-0001 | `CONFIRMED doctrine` | Grounds §9.2 schema paths and §9.6 fixture layout. | Doctrine, not implementation. |
| `docs/atlas/README.md` and `docs/atlas/source-role-anti-collapse.md` (prior turns, this session) | `CONFIRMED pointer-page status` | Establishes the deprecated-lane pattern; this canonical-lane register supersedes the prior pointers in scope. | Pointer; not authority. |

**Memory is not evidence.** No mounted repo, CI run, workflow, dashboard, or branch state was inspected. Every implementation claim is `PROPOSED` and bounded to doctrine.

</details>

<details>
<summary><strong>Appendix B — Faithful-extraction note</strong></summary>

This file is a **faithful extraction** of Atlas v1.1 §24.5 into a standalone register form. The §24.5.1 five-tier table (§2 here), the §24.5.2 thirteen-row per-domain matrix (§4 here), and the §24.5.3 seven-row tier-transitions table (§5 here) reproduce the §24.5 content without semantic change. Inline column headers, doctrine language, and the asymmetric-discipline reading note are preserved.

**Net additions in this extract beyond §24.5 itself:**

- §1.1 safest-representation principle table (operationalizes the §24.5 preamble).
- §1.2 Mermaid tier-ladder diagram (visualizes §24.5.3 transitions).
- §3 allowed-transforms vocabulary (synthesizes §24.5.1 T1 row's four-transform list with Pass 10 C6 redaction-profile library).
- §4.1 hard-boundaries subsection (consolidates the four rows where transforms cannot cross to T0/T1).
- §4.2 synthetic-content interaction subsection (cross-references to source-role register §24.1 collapse pattern 6).
- §5.1 asymmetric-discipline rule (extracts the §24.5.3 reading note as its own subsection).
- §5.2 derivative-invalidation rule (extracts the §24.5.3 Any→T4 row note).
- §6 Deny-by-Default Register cross-reference (explicit mapping from v1.0 §20.5 rows to §24.5 rows).
- §7 enforcement surfaces (consolidates §24.5.2 "Required gates" column across seven surfaces).
- §8 validators (decomposes implied §24.5 validators into per-rule validators).
- §9 implementation surface (`PROPOSED` throughout, grounded in `directory-rules.md` v1.2 and Pass 10 C6).
- §10 cross-references.
- §11 verification checklist.
- §12 open questions (especially §12.1 ADR-S-05 + Pass 10 C6-01 divergence).

None of the §24.5 content is overwritten or paraphrased to a meaning change. If divergence is observed, §24.5 inside the consolidated atlas wins, and the divergence is filed to `docs/registers/DRIFT_REGISTER.md` per Directory Rules §2.5.

**Reversibility.** Removing this standalone extract leaves §24.5 inside the consolidated atlas unchanged and authoritative. Full reversibility is consistent with the Atlas v1.1 Appendix G "supersession by extension, not by overwrite" pattern.

**Surfaced divergences (do not silently resolve).**

1. **T0–T4 (§24.5) vs. 0–5 (Pass 10 C6-01).** Both schemes exist in the corpus. This extract surfaces both with `PROPOSED` labels and routes the reconciliation to ADR-S-05. Until ADR-S-05 is accepted, do not assume one supersedes the other.
2. **Per-domain row pass-through.** §4 reproduces thirteen rows from §24.5.2 exactly. If the consolidated atlas later edits a row, the divergence is a drift entry per Directory Rules §2.5, not a unilateral edit on this extract.

</details>

[↑ back to top](#top)
