<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/flora-sensitivity
title: Flora — Sensitivity
type: standard
version: v1
status: draft
owners: Domain steward (Flora); Sensitivity reviewer; Docs steward
created: 2026-06-03
updated: 2026-06-03
policy_label: public
related: [docs/doctrine/ai-build-operating-contract.md, docs/doctrine/directory-rules.md, docs/domains/flora/README.md, docs/domains/flora/RIGHTS_AND_SENSITIVITY.md, docs/domains/flora/PUBLICATION_AND_ROLLBACK.md, policy/sensitivity/flora/, policy/geoprivacy/, schemas/contracts/v1/receipts/]
tags: [kfm]
notes: [Doctrine-adjacent; pins CONTRACT_VERSION = "3.0.0". OVERLAP NOTICE — this doc covers the same Flora sensitivity surface as docs/domains/flora/RIGHTS_AND_SENSITIVITY.md; the two are CONFLICTED candidates for ADR/DRIFT_REGISTER resolution (single canonical sensitivity home). Built at user request; reconciliation deferred. Disposition defers to operating contract §23.2; tiers defer to ADR-S-05. All repo paths PROPOSED until mounted-repo verification.]
[/KFM_META_BLOCK_V2] -->

# 🌿 Flora — Sensitivity

> What the Flora lane may show, at what precision, and to whom — and the transforms, receipts, and reviews a release must carry. Rare and culturally sensitive plants fail closed by default; public surfaces see only the safest representation that still answers a reasonable question.

<a id="top"></a>

![status](https://img.shields.io/badge/status-draft-yellow)
![policy](https://img.shields.io/badge/policy-deny--by--default--T4-critical)
![contract](https://img.shields.io/badge/CONTRACT__VERSION-3.0.0-informational)
![lane](https://img.shields.io/badge/domain-flora-2ea44f)
![tiers](https://img.shields.io/badge/tiers-T0–T4-blueviolet)
![CARE](https://img.shields.io/badge/CARE-sovereignty--aware-8a3ffc)

| Field | Value |
|---|---|
| **Status** | `draft` |
| **Owners** | Domain steward (Flora) · Sensitivity reviewer · Docs steward |
| **Last updated** | 2026-06-03 |
| **Contract** | `CONTRACT_VERSION = "3.0.0"` |
| **Disposition authority** | Operating contract §23.2 sensitive-domain matrix (not re-derived here) |
| **Tier scheme authority** | Atlas §24.5 / `ADR-S-05` (PROPOSED until ratified) |
| **Repo home (PROPOSED)** | `docs/domains/flora/SENSITIVITY.md` |

> [!WARNING]
> **Overlapping-authority notice (CONFLICTED).** This document and [`docs/domains/flora/RIGHTS_AND_SENSITIVITY.md`](./RIGHTS_AND_SENSITIVITY.md) both describe the Flora sensitivity surface. Two parallel homes for the same authority is the drift pattern Directory Rules §13.5 names. Until an ADR designates a **single canonical sensitivity home** for the Flora lane, treat both as `PROPOSED / CONFLICTED` and log the conflict in `docs/registers/DRIFT_REGISTER.md`. This doc does not silently supersede the other. See [Open questions](#open-questions-register).

> [!CAUTION]
> **Exact rare, protected, or culturally sensitive plant locations are denied on public surfaces by default (T4).** Public release requires steward review, generalized or withheld geometry, **and** a `RedactionReceipt`. This doc explains the rules; it grants no exceptions and re-derives no disposition — that routes through operating contract §23.2 and `policy/sensitivity/flora/`.

---

## Quick jump

- [1. Scope](#1-scope)
- [2. Repo fit](#2-repo-fit)
- [3. The sensitivity gate](#3-the-sensitivity-gate)
- [4. Sensitivity tiers (T0–T4)](#4-sensitivity-tiers-t0t4)
- [5. Flora tier assignments](#5-flora-tier-assignments)
- [6. Tier transitions](#6-tier-transitions)
- [7. Geoprivacy transforms](#7-geoprivacy-transforms)
- [8. The RedactionReceipt](#8-the-redactionreceipt)
- [9. CARE, sovereignty & culturally sensitive plants](#9-care-sovereignty--culturally-sensitive-plants)
- [10. Join-induced sensitivity](#10-join-induced-sensitivity)
- [11. Negative states surfaced to users](#11-negative-states-surfaced-to-users)
- [12. Validation & fixtures](#12-validation--fixtures)
- [Open questions register](#open-questions-register)
- [Open verification backlog](#open-verification-backlog)
- [Changelog v0 → v1](#changelog-v0--v1)
- [Definition of done](#definition-of-done)
- [Related docs](#related-docs)

---

## 1. Scope

This document is the **sensitivity contract** for the Flora domain lane: which Flora content may reach a public surface, at what precision, to whom, and under what transforms and receipts. It answers the question *"at what precision, and to whom?"* for every Flora claim before the release gate.

**In scope:** the T0–T4 tier scheme as applied to Flora; default tiers for Flora object families; allowed tier transitions and their reversibility; the geoprivacy transform vocabulary; the `RedactionReceipt`; CARE / tribal-sovereignty handling of culturally significant plants; join-induced sensitivity; and the negative states users see when a request is denied or generalized.

**Out of scope** (owned elsewhere; cite, do not restate):
- **Rights** (license, attribution, redistribution, steward obligation) — the *"may we show this at all?"* question. See `RIGHTS_AND_SENSITIVITY.md` §4, or a future `RIGHTS.md` if the reconciliation ADR splits them.
- The release gate mechanics and rollback → `PUBLICATION_AND_ROLLBACK.md`.
- Source families and identity → `README.md`.
- The canonical disposition matrix → operating contract §23.2 (this doc applies it, never overrides it).
- The tier scheme's ratification → `ADR-S-05`.

> [!IMPORTANT]
> **Source quality never overrides sensitivity.** A rare-plant record can be perfectly sourced, rights-clean, and validated — and still be unpublishable at exact precision. Public exposure is a governed state, not a reward for data quality. *(CONFIRMED posture — `KFM-P25-IDEA-0006`; Atlas, Flora §I.)*

[↑ Back to top](#top)

---

## 2. Repo fit

This is a `docs/` lane segment, not a root-level folder (Directory Rules §12). The **decisions** it explains live in `policy/`; the **receipts** it requires live under `data/` and `schemas/contracts/v1/receipts/`.

| Concern | Owning root | Flora-lane segment (PROPOSED) |
|---|---|---|
| Human explanation (this doc) | `docs/` | `docs/domains/flora/SENSITIVITY.md` |
| Sensitivity decisions | `policy/` | `policy/sensitivity/flora/` |
| Geoprivacy decisions | `policy/` | `policy/geoprivacy/` |
| Sensitive-taxa gate list | `policy/` | `policy/sensitivity/flora/sensitive_taxa.txt` |
| `RedactionReceipt` schema | `schemas/` | `schemas/contracts/v1/receipts/redaction_receipt.schema.json` |
| Sensitivity fixtures | `fixtures/` | `fixtures/domains/flora/` |
| Sensitivity-denial tests | `tests/` | `tests/domains/flora/` |

> [!WARNING]
> Every path above is **PROPOSED** until verified against a mounted repository. The **rules** (which root owns which concern) are CONFIRMED doctrine; the **presence** of any specific path is not. *(Directory Rules §0.)* The `policy/sensitivity/` and `policy/geoprivacy/` segments are CONFIRMED as canonical policy lanes in the repository structure guiding document; their `flora/` sub-segments are PROPOSED.

[↑ Back to top](#top)

---

## 3. The sensitivity gate

Sensitivity is a **fail-closed gate** at the release boundary. A Flora claim must clear it before publication; clearing rights, validation, or evidence closure does not relax it. *(CONFIRMED — Atlas, Flora §I: "Unresolved sensitivity … blocks public promotion.")*

```mermaid
flowchart TD
    C["Flora release candidate<br/>(rights already cleared)"] --> S{"Sensitivity gate<br/>tier · transform · audience"}
    S -->|"T0 / non-sensitive"| OK0["Public-safe as-is"]
    S -->|"T4 exact, no transform"| D["DENY<br/>SENSITIVITY_UNRESOLVED"]
    S -->|"T4 → T1 via transform + review"| G["Generalized public-safe<br/>(RedactionReceipt + ReviewRecord)"]
    S -->|"T2 / T3"| R["Restricted surface only<br/>not public"]
    G --> OK1["Eligible for release<br/>(still needs ReleaseManifest)"]

    classDef deny fill:#ffd7d7,stroke:#9b1d1d,color:#000;
    classDef ok fill:#e8f5e9,stroke:#2e7d32,color:#1b5e20;
    class D deny;
    class OK0,OK1 ok;
```

> [!NOTE]
> The sensitivity gate runs **after** the rights gate (the two are independent fail-closed checks). This doc assumes rights are already resolved; if they are not, the candidate is denied at the rights gate first. *(CONFIRMED — `KFM-P1-PROG-0032` treats rights as a distinct, fail-closed check.)*

[↑ Back to top](#top)

---

## 4. Sensitivity tiers (T0–T4)

KFM publishes only the **safest representation that still answers the steward's and the public's reasonable needs.** The tier scheme makes "publish at tier N" a reviewable, repeatable action. *(CONFIRMED doctrine — Atlas §24.5; tier definitions PROPOSED pending `ADR-S-05`.)*

| Tier | Name | Definition | Default audience |
|---|---|---|---|
| `T0` | Open | Public-safe with no transform; no rights/sensitivity/steward gating beyond standard release. | Any public client via governed API. |
| `T1` | Generalized | Public-safe only after generalization, fuzzing, aggregation, or redaction; transform reviewed and recorded. | Any public client via governed API. |
| `T2` | Reviewer | Released only to authenticated reviewers or domain stewards; policy-bounded; correction path active. | Stewards, reviewers, named research collaborators. |
| `T3` | Restricted | Released only under named agreement (rights, sovereignty, or consent) and recorded. | Named authorized parties only. |
| `T4` | Denied | Not released to any audience; the *existence* of a record may be released only as steward review permits. | — |

[↑ Back to top](#top)

---

## 5. Flora tier assignments

Default tiers for Flora object classes, extending the Atlas §20.5 deny register with explicit tiers. PROPOSED pending `ADR-S-05`. *(Atlas §24.5.2; object-family defaults §24.14.)*

| Flora object class | Default tier | Allowed transform → target | Required gates |
|---|---|---|---|
| Rare / protected / culturally sensitive plant location | **T4** | Generalized geometry + steward review → **T2 or T1** | `RedactionReceipt` + `ReviewRecord` |
| `RarePlantRecord` (object family) | **T4** | Public-safe derivative only, via generalization → **T1** | `RedactionReceipt` + `ReviewRecord` |
| `RangePolygon` | **T1** | Aggregate / generalized public-safe layer | `AggregationReceipt` or `RedactionReceipt` |
| Common-species occurrence (non-sensitive) | `T0`/`T1` | None, or generalization where uncertainty warrants | Standard Gates A–G |
| `VegetationCommunity` polygon | `T0`/`T1` | Generalization where rights/source require | Standard Gates A–G |
| `DistributionSurface` (modeled) | `T1` | Model-card + uncertainty surface; `modeled` role preserved | `ModelRunReceipt` |

> [!CAUTION]
> **A rare-plant location starts at T4 — denied to all audiences — and only a documented transform plus a steward review moves it toward public.** The default is *not* "show generalized"; the default is *deny*, and generalization is the exception that must be earned with a receipt and a review. *(CONFIRMED — Atlas §24.5.2 Flora row; §20.5 Flora deny register.)*

[↑ Back to top](#top)

---

## 6. Tier transitions

Tier motion is governed and **reversible**. The asymmetry is the key rule: **moving toward more-public always needs both a transform receipt and a review record; moving toward less-public needs only a `CorrectionNotice`.** *(CONFIRMED doctrine — Atlas §24.5.3.)*

| From → To | Required artifact | Required reviewer | Reversibility |
|---|---|---|---|
| `T4 → T3` | `PolicyDecision` + `ReviewRecord` + agreement | Steward + rights-holder where applicable | Agreement revocation returns object to T4 with `CorrectionNotice`. |
| `T4 → T2` | `PolicyDecision` + `ReviewRecord` | Steward | Review revocation returns object to T4. |
| `T4 → T1` | `RedactionReceipt` + `ReviewRecord` | Steward | Redaction can be re-evaluated; correction may demote a published T1 to T4. |
| `T3 → T2` | `PolicyDecision` + `ReviewRecord` | Steward | Reversible. |
| `T2 → T1` | `RedactionReceipt` + `ReviewRecord` | Steward | Reversible. |
| `T1 → T0` | `ReleaseManifest` + `ReviewRecord` | Steward + release authority | Reversible via `RollbackCard`. |
| **Any tier → T4** (downgrade) | `CorrectionNotice` + `ReviewRecord` | Steward + rights-holder where applicable | Always permitted; precedes derivative invalidation. |

> [!TIP]
> The downgrade path is the safety valve: if a source is reclassified, rights change, or harm potential is discovered, **any** Flora object can be pulled back to T4 with a `CorrectionNotice` alone — no transform receipt required. Restriction is always cheaper than exposure.

[↑ Back to top](#top)

---

## 7. Geoprivacy transforms

When a steward authorizes moving a rare-plant object toward public, the geometry is transformed and the transform is recorded; each transform emits a receipt. *(CONFIRMED posture — `KFM-P1-PROG-0035` rare-species geoprivacy and transform receipts; `KFM-P26-PROG-0022` sensitive-taxa gate requires `public_safe_geometry` + recorded reason.)*

| Transform (PROPOSED vocabulary) | Effect | Typical target tier |
|---|---|---|
| `suppress` | No public geometry; metadata only with regional envelope. | T1 (metadata) / T4 (full) |
| `generalize_to_grid` | Coarsen to a documented grid cell. | T1 |
| `generalize_to_watershed` | Snap to HUC / watershed unit. | T1 |
| `generalize_to_county` | Coarsen to county. | T1 |
| `buffer` / `jitter` (constrained) | Offset within a documented radius — only when scientific value justifies it. | T1 |
| `delayed_publication` | Stage release tied to review state and freshness window. | T1/T2 |
| `steward_only` | Exact geometry available only to authorized stewards; never on a public route. | T2/T3 |

> [!NOTE]
> The transform vocabulary is **PROPOSED** and should be frozen by an ADR (see Open Questions). The generalization radius / grid size per sensitivity class is a policy value that `policy/sensitivity/flora/` must carry — it is not hard-coded here. *(NEEDS VERIFICATION — thresholds per taxon class.)*

[↑ Back to top](#top)

---

## 8. The RedactionReceipt

Every public-safe transform of sensitive Flora content emits a **`RedactionReceipt`** — without it, the transform did not happen in the governed sense. *(CONFIRMED doctrine — Atlas §24.2: "if no receipt exists, the operation did not happen in the governed sense.")*

**Purpose:** records a public-safe transformation that removed, masked, fuzzed, or withheld content for sensitivity, rights, or policy. **Triggered by:** rare-species occurrences, among other sensitive-domain publications. *(CONFIRMED — Atlas §24.2.1 RedactionReceipt row, cites `[DOM-FLORA]`.)*

| Field (PROPOSED shape) | Meaning |
|---|---|
| `policy_ref` | The `policy/sensitivity/flora/` rule that authorized the transform. |
| `redaction_method` | The transform applied (from §7 vocabulary). |
| `kept_fields` | Fields retained in the public-safe output. |
| `removed_fields` | Fields withheld or masked. |
| `geometry_transform` | The geometry operation and parameters (e.g. grid cell, buffer radius). |
| `reviewer` | The steward / sensitivity reviewer who approved it. |

> [!IMPORTANT]
> The `RedactionReceipt` is part of the `EvidenceBundle` lineage and is referenced by the `ReleaseManifest`. A public Flora layer derived from sensitive input that **lacks** a resolvable `RedactionReceipt` fails the release gate closed (`MISSING_RECEIPT`). *(CONFIRMED — Atlas §24.6.1 validation row "RedactionReceipt if sensitivity applies"; §24.6.3 reason code.)*

[↑ Back to top](#top)

---

## 9. CARE, sovereignty & culturally sensitive plants

Culturally significant plants — tribally important, ceremonial-use, or otherwise steward-governed taxa — are governed under CARE principles and tribal-sovereignty rules, **not** treated as ordinary rare-species records. *(CONFIRMED posture — `KFM-P1-IDEA-0034` cultural/tribal/sacred/steward review controls; `KFM-P11-PROG-0024` CARE promotion-gate fail-closed bundle.)*

- **Steward + rights-holder review is required**, not just a domain steward. Cultural, tribal, sacred, and steward-governed material requires review and public-safe transformation before release.
- **Sovereignty-label inheritance.** Flora artifacts whose areas of interest intersect tribal / AIANNH / BIA overlays SHOULD inherit `sovereignty:tribal` and sensitivity labels — or require a signed, time-boxed waiver — before promotion. *(PROPOSED — `KFM-P11-PROG-0025`.)*
- **CARE-aligned promotion gate.** Promotion manifests are blocked when exposure intersects sensitive or sovereign contexts unless CARE-aligned labels, consent, and current waiver evidence are present. Deny-by-default holds where evidence is missing. *(PROPOSED — `KFM-P11-PROG-0024`.)*
- **Map / narrative discipline.** Map assets carrying culturally sensitive plant content require CARE status blocks (public / generalized / restricted) with reviewers and review dates; story narratives use context-only spatial footprints, never precise site disclosure. *(CONFIRMED — `ML-059-029`, `ML-059-015`.)*

> [!CAUTION]
> Where rights, sovereignty, or cultural sensitivity are **unclear**, the default is quarantine, redaction, generalization, staged access, delayed publication, or denial — not publication. Record the transform and the reason. *(CONFIRMED — operating contract §23.2 default disposition.)*

[↑ Back to top](#top)

---

## 10. Join-induced sensitivity

A benign Flora source can become sensitive **when joined** with another source. Sensitivity is a property of the **resulting product**, not only of the inputs. *(Aligns with `ADR-S-14` cross-lane join policy, OPEN.)*

```mermaid
flowchart LR
    A["USDA PLANTS<br/>(county checklist, T0)"] --> J(("join"))
    B["Rare-plant locality dataset<br/>(T4)"] --> J
    J --> R["Joined product<br/>inherits the most restrictive input → T4"]
    classDef deny fill:#ffd7d7,stroke:#9b1d1d,color:#000;
    class R deny;
```

A join that creates new sensitivity must clear the same gates as the **most sensitive input**, and route through a sensitivity reviewer. Examples for Flora: joining a public checklist to a rare-plant locality; joining an iNaturalist coordinate to a small-population polygon; joining a herbarium record to an unprotected micro-habitat. *(CONFIRMED posture — Atlas source-role anti-collapse; operating contract §23.2.)*

[↑ Back to top](#top)

---

## 11. Negative states surfaced to users

When a request is denied or generalized, the user sees a **visible** negative state — never a silent empty result. This lets users tell "we don't know" from "we know but cannot show." *(CONFIRMED — Unified Doctrine Synthesis §19; operating contract §22.2.)*

| Negative state | Meaning for Flora |
|---|---|
| `DENIED_BY_POLICY` | Rights / sensitivity / release blocks display (e.g. exact rare-plant location). |
| `GENERALIZED_GEOMETRY` | Geometry transformed for public safety; links to the `RedactionReceipt`. |
| `RESTRICTED_ACCESS` | Material exists but is T2/T3/T4; not available to this audience. |
| `MISSING_EVIDENCE` | No `EvidenceBundle` resolves for the Flora claim. |
| `SOURCE_STALE` | Source freshness exceeded; sensitivity may need re-review. |

[↑ Back to top](#top)

---

## 12. Validation & fixtures

These Flora-lane checks are **PROPOSED** until proven against fixtures and a mounted repo. *(Atlas, Flora §K; geoprivacy cards `KFM-P1-PROG-0035`, `KFM-P26-PROG-0022`.)*

- [ ] Sensitive-taxa gate: a taxon on `sensitive_taxa.txt` forces `public_safe_geometry` and a recorded reason (PROPOSED).
- [ ] Exact sensitive public-geometry **denial** test (PROPOSED).
- [ ] `RedactionReceipt` validation: `policy_ref`, `redaction_method`, `kept_fields`, `removed_fields`, `geometry_transform`, `reviewer` present (PROPOSED).
- [ ] Tier-transition test: `T4 → T1` requires `RedactionReceipt` **and** `ReviewRecord` (PROPOSED).
- [ ] Downgrade test: `Any → T4` succeeds with `CorrectionNotice` alone (PROPOSED).
- [ ] Join-induced sensitivity test: joined product inherits the most restrictive input tier (PROPOSED).
- [ ] CARE / sovereignty test: AOI intersecting a tribal overlay inherits `sovereignty:tribal` or requires a waiver (PROPOSED).

[↑ Back to top](#top)

---

## Open questions register

| ID | Question | Owner role | Resolution path |
|---|---|---|---|
| OQ-FLORA-SENS-01 | **Which is the single canonical Flora sensitivity home — `SENSITIVITY.md` or `RIGHTS_AND_SENSITIVITY.md`?** | Docs steward + Flora domain steward | ADR designating one; supersede the other; `DRIFT_REGISTER.md` entry |
| OQ-FLORA-SENS-02 | What generalization radius / grid size applies per rare-plant sensitivity class? | Sensitivity reviewer | `policy/sensitivity/flora/` + `ADR-S-05` |
| OQ-FLORA-SENS-03 | Is the geoprivacy transform vocabulary (§7) frozen, and where does it live? | Domain steward (Flora) | ADR enumerating transform types |
| OQ-FLORA-SENS-04 | Where does culturally sensitive plant knowledge sit in the tier matrix, and what review path applies? | Domain steward + rights-holder rep | §23.2 matrix + `KFM-P11-PROG-0025` ratification |
| OQ-FLORA-SENS-05 | What is the `RedactionReceipt` schema home — `schemas/contracts/v1/receipts/` or domain-scoped? | Docs steward | `ADR-S-03` (receipt-class home) |
| OQ-FLORA-SENS-06 | Which sensitivity tier do unprotected-but-rare taxa receive when no listing status exists? | Sensitivity reviewer | `ADR-S-05` + steward policy |

## Open verification backlog

These items remain `NEEDS VERIFICATION` before promotion from `draft` to `published`:

1. **Resolution of the `SENSITIVITY.md` ↔ `RIGHTS_AND_SENSITIVITY.md` overlap** (OQ-FLORA-SENS-01) — a promotion blocker; one must be canonical.
2. Presence and contents of `policy/sensitivity/flora/` and `policy/geoprivacy/`.
3. Existence of `sensitive_taxa.txt` (or its canonical equivalent).
4. `RedactionReceipt` schema home and field names against the mounted repo.
5. Tier scheme (T0–T4) ratification status (`ADR-S-05`).
6. Generalization thresholds per Flora sensitivity class.
7. CARE / sovereignty-label inheritance implementation (`KFM-P11-PROG-0025`).

## Changelog v0 → v1

| Change | Type (per contract §37) | Reason |
|---|---|---|
| Initial Flora sensitivity contract | new | Sensitivity-only doc per request. |
| Surfaced overlap with `RIGHTS_AND_SENSITIVITY.md` as CONFLICTED, routed to ADR/DRIFT_REGISTER | reconciliation | Two parallel sensitivity homes is Directory Rules §13.5 drift; surfaced, not resolved silently. |
| Restated §23.2 disposition and §24.5 tiers without re-deriving them | clarification | Defer disposition to operating contract; tiers to `ADR-S-05`. |
| Pinned `CONTRACT_VERSION = "3.0.0"` | housekeeping | Doctrine-adjacent doc requirement. |

> **Backward compatibility.** New doc; no prior anchors to break. Section anchors intended to be stable. **Pending the OQ-FLORA-SENS-01 ADR, this doc may itself be superseded or merged** — do not deep-link to it as canonical until that ADR lands.

## Definition of done

This document is done enough to enter the repository when:

- the canonical-home conflict with `RIGHTS_AND_SENSITIVITY.md` is resolved by ADR (OQ-FLORA-SENS-01);
- it is placed according to Directory Rules (`docs/domains/flora/`);
- a docs steward, the Flora domain steward, and a sensitivity reviewer review it;
- it is linked from the Flora README and a doctrine/sensitivity index;
- it does not conflict with accepted ADRs (`ADR-S-03`, `ADR-S-04`, `ADR-S-05`, `ADR-S-14`);
- the overlap is logged in `docs/registers/DRIFT_REGISTER.md`;
- the `GENERATED_RECEIPT.json` planned in the authoring notes is wired into CI;
- future changes follow operating contract §37 lifecycle.

---

## Related docs

- [`docs/domains/flora/RIGHTS_AND_SENSITIVITY.md`](./RIGHTS_AND_SENSITIVITY.md) — **overlapping** rights + sensitivity contract (CONFLICTED canonical-home candidate — see OQ-FLORA-SENS-01)
- [`docs/doctrine/ai-build-operating-contract.md`](../../doctrine/ai-build-operating-contract.md) — operating law; §23.2 sensitive-domain matrix (`CONTRACT_VERSION = "3.0.0"`)
- [`docs/doctrine/directory-rules.md`](../../doctrine/directory-rules.md) — placement authority; §13.5 parallel-home drift
- [`docs/domains/flora/README.md`](./README.md) — Flora domain landing page
- [`docs/domains/flora/PUBLICATION_AND_ROLLBACK.md`](./PUBLICATION_AND_ROLLBACK.md) — Flora release / correction / rollback contract
- `policy/sensitivity/flora/` — Flora sensitivity rules *(PROPOSED / TODO)*
- `policy/geoprivacy/` — geoprivacy transform policy *(PROPOSED / TODO)*
- `schemas/contracts/v1/receipts/redaction_receipt.schema.json` — `RedactionReceipt` schema *(PROPOSED — `ADR-S-03`)*

_Last updated: 2026-06-03 · `CONTRACT_VERSION = "3.0.0"`_

[↑ Back to top](#top)
