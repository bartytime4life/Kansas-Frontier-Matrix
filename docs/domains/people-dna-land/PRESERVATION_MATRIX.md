<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-domains-people-dna-land-preservation-matrix
title: People · DNA · Land — Preservation Matrix
type: standard
subtype: domain-preservation-matrix
version: v0.2
status: draft
owners: People/DNA/Land domain steward + Docs steward  # PLACEHOLDER — confirm in ADR-S-people-stewards
created: 2026-05-19
updated: 2026-06-07
policy_label: public-doctrine
contract_version: "3.0.0"
related:
  - docs/domains/people-dna-land/README.md                     # PROPOSED; NEEDS VERIFICATION
  - docs/domains/people-dna-land/PEOPLE_DOMAIN_MODEL.md        # authored prior session (v0.1)
  - docs/domains/people-dna-land/MISSING_OR_PLANNED_FILES.md   # authored prior session (v0.2)
  - docs/domains/people-dna-land/VERIFICATION_BACKLOG.md       # PROPOSED; NEEDS VERIFICATION
  - docs/doctrine/directory-rules.md
  - docs/doctrine/lifecycle-law.md                             # PROPOSED placement; NEEDS VERIFICATION
  - docs/doctrine/trust-membrane.md                            # PROPOSED placement; NEEDS VERIFICATION
  - docs/standards/SENSITIVITY_RUBRIC.md                       # PROPOSED; Pass-10 C6-01
  - docs/runbooks/revocation.md                                # PROPOSED; Pass-10 C5-09 expansion
  - docs/registers/DRIFT_REGISTER.md
extends:
  - KFM Domains Culmination Atlas v1.1 — Ch. 16 (People/Genealogy/DNA/Land) §B/§C/§D/§E/§I/§L/§M/§N, Ch. 24.5 (Sensitivity tiers), Appendix C
  - Pass-10 Idea Index — C1-06 (append-only ledger, PROPOSED), C5-09 (tombstones, CONFIRMED), C6-01/05/06/07/08 (sensitivity/consent, CONFIRMED), C9-01/02/03/04/07 (genealogy/genomics, CONFIRMED)
  - Directory Rules v1.3 — §5, §7 (trust membrane / schema home), §12 (Domain Placement Law), §13 (anti-patterns)
authority_posture: doctrine surface (reading aid) — subordinate to ai-build-operating-contract.md, Directory Rules, the Atlas, and any mounted-repo evidence; not a policy, schema, runbook, or release surface; supersedes no source doctrine
truth_labels: [CONFIRMED, PROPOSED, INFERRED, NEEDS VERIFICATION, UNKNOWN, CONFLICTED]
tags: [kfm, domain, people, dna, land, preservation, retention, consent, tombstone, erasure, CARE]
notes:
  - "CONTRACT_VERSION pinned to 3.0.0 per ai-build-operating-contract.md."
  - "PROPOSED synthesis assembling corpus doctrine into matrix form. No mounted repo inspected — all repo paths are PROPOSED / NEEDS VERIFICATION."
  - "v0.2 correction: the append-only audit ledger (Pass-10 C1-06) is PROPOSED in the corpus, not CONFIRMED; only the tombstone-not-deletion rule (C5-09) and revocation discipline (C6-08) are CONFIRMED. §7 truth label corrected."
  - "v0.2 correction: stable-ID citations KFM-P9-PROG-0010/-0018, KFM-P17-PROG-0018, KFM-P19-IDEA-0003 could not be confirmed in the indexed corpus; softened to anchored doctrine (C1-06 / C5-09 / storage-maintenance card) with a NEEDS VERIFICATION note. See §10 appendix."
  - "OPEN CONFLICT carried from MISSING_OR_PLANNED_FILES v0.2: segment 'people' (Atlas Ch. 24.13) vs 'people-dna-land' (Directory Rules §12). Tracked as OQ-PDL-SEG-01."
  - "Open question OPEN-PRES-01: tombstone vs. erasure boundary not yet codified upstream (Pass-10 C5-09 open question)."
[/KFM_META_BLOCK_V2] -->

# People · DNA · Land — Preservation Matrix

> A reviewable, per-object map of what must be preserved, what must be transformed, what must be tombstoned, and what (rarely, narrowly) must be erased — for the most ethically loaded domain in KFM.

[![Status](https://img.shields.io/badge/status-draft-yellow?style=flat-square)](#status--ownership)
[![Doctrine](https://img.shields.io/badge/doctrine-People%20·%20DNA%20·%20Land-blueviolet?style=flat-square)](#1-scope)
[![Default Tier](https://img.shields.io/badge/default--tier-T4%20deny-red?style=flat-square)](#3-sensitivity-tier-recap)
[![Truth Posture](https://img.shields.io/badge/truth-cite--or--abstain-informational?style=flat-square)](#status--ownership)
[![Lifecycle](https://img.shields.io/badge/lifecycle-RAW→PUBLISHED-success?style=flat-square)](#4-preservation-flow)
[![CONTRACT_VERSION](https://img.shields.io/badge/CONTRACT__VERSION-3.0.0-informational?style=flat-square)](#status--ownership)
[![Segment](https://img.shields.io/badge/segment%20naming-CONFLICTED-orange?style=flat-square)](#status--ownership)
[![Last Updated](https://img.shields.io/badge/last%20updated-2026--06--07-lightgrey?style=flat-square)](#status--ownership)

---

### Status & ownership

| Field | Value |
|---|---|
| **Doc class** | Standard doc · domain dossier member · **reading aid, not authority** |
| **Edition** | v0.2 (truth-label + citation correction pass) |
| **Authority of the matrix shape** | PROPOSED — synthesis aligned with Atlas v1.1 §24.5, Directory Rules §12, Pass-10 C5-09/C6-08 |
| **Authority of doctrinal rules cited** | Mixed — see per-row truth labels; CONFIRMED where the corpus confirms, PROPOSED where it proposes |
| **Authority of any specific path / route / schema URI** | PROPOSED / NEEDS VERIFICATION until repo inspection |
| **Owners (PLACEHOLDER)** | People/DNA/Land domain steward; Docs steward; release authority (separation of duties at maturity) |
| **Conflict rule** | When this matrix disagrees with the domain model, doctrine, ADRs, or Atlas v1.1, **doctrine wins** and the disagreement files to `docs/registers/DRIFT_REGISTER.md` per Directory Rules §13 |
| **Last reviewed** | 2026-06-07 |

> [!IMPORTANT]
> **Deny-default posture.** Every row in this matrix begins from T4 (denied) unless an explicit, evidenced, policy-approved transform path is named. Living-person fields, raw DNA, and private person-parcel joins are denied by default; quiet promotion is a failure mode, not a feature. [DOM-PEOPLE §I] [Atlas v1.1 §24.5.2]

> [!WARNING]
> **Two open conflicts carried into this edition.** (1) **Segment naming** — Atlas Ch. 24.13 assigns `policy/sensitivity/people/`; Directory Rules §12 examples use `people-dna-land`. Paths below use `<segment>` for the contested roots; tracked as **OQ-PDL-SEG-01**. (2) **Append-ledger status** — the append-only audit ledger (Pass-10 C1-06) is **PROPOSED** in the corpus, not CONFIRMED; only the *tombstone-not-deletion* rule (C5-09) and revocation discipline (C6-08) are CONFIRMED. See [§7](#7-tombstone-vs-erasure-decision-matrix).

---

## 📑 Contents

1. [Scope](#1-scope)
2. [How to read this matrix](#2-how-to-read-this-matrix)
3. [Sensitivity tier recap](#3-sensitivity-tier-recap)
4. [Preservation flow](#4-preservation-flow)
5. [Object-class preservation matrix](#5-object-class-preservation-matrix)
6. [Trigger → action matrix](#6-trigger--action-matrix)
7. [Tombstone vs. erasure decision matrix](#7-tombstone-vs-erasure-decision-matrix)
8. [Source-family preservation profile](#8-source-family-preservation-profile)
9. [Anti-patterns this matrix exists to prevent](#9-anti-patterns-this-matrix-exists-to-prevent)
10. [Open questions & verification backlog](#10-open-questions--verification-backlog)
11. [Related docs](#11-related-docs)

---

## 1. Scope

**This matrix governs preservation duties for objects owned by the People, Genealogy, DNA, and Land Ownership domain** — the object families enumerated in Atlas Ch. 16 §B/§C/§E and Appendix C: *Person Assertion, PersonCanonical, NameAssertion, LifeEvent, Residence Event, Migration Event, Genealogy Relationship, FamilyGroup, DNA Match Evidence, DNASegment, DNAKitToken, ConsentGrant, RevocationReceipt, Relationship Hypothesis, LandParcel, LegalDescription, LandInstrument, Deed Instrument, Title Instrument, Assessor Record, TaxRecord, Parcel Version, Ownership Interval.* [DOM-PEOPLE §B] [ENCY App. C]

**What this matrix is.** A 2-D reference layer crossing domain object classes with the preservation duties imposed by the KFM lifecycle invariant, the tier scheme, the consent regime, the tombstone/revocation discipline, and the rollback contract. It is a reading aid for stewards and reviewers — **not a separate authority**.

**What this matrix is not.**

- It is **not** the policy. Policy lives in `policy/sensitivity/<segment>/`, `policy/consent/<segment>/`, and `policy/domains/people-dna-land/` (PROPOSED paths; segment CONFLICTED per OQ-PDL-SEG-01).
- It is **not** the schema. Schema lives in `schemas/contracts/v1/<segment>/` (PROPOSED per ADR-0001; segment CONFLICTED).
- It is **not** the runbook. Revocation drills, vendor-loss playbooks, and erasure procedures live in `docs/runbooks/` (PROPOSED).
- It is **not** a release surface. No object listed here is published merely because the matrix names it.

> [!NOTE]
> **Segment-name conflict (OQ-PDL-SEG-01).** Where Directory Rules §12 gives an explicit example (`policy/domains/people-dna-land/`), this matrix uses `people-dna-land`. Where only the Atlas Ch. 24.13 crosswalk gives a path (`schemas/contracts/v1/people/`, `policy/sensitivity/people/`, `policy/consent/people/`), the segment is written `<segment>` pending ADR. Directory Rules wins on placement.

**Bounded non-ownership.** This matrix does **not** govern: Frontier-Matrix demographic panels (they aggregate from this domain but their preservation duties live with the Frontier Matrix lane); Archaeology cultural-heritage records ([DOM-ARCH]); Settlements infrastructure ([DOM-SETTLE]). When a record straddles a boundary, preservation duties **stack — not collapse**. [DOM-PEOPLE §B]

[↑ back to top](#people--dna--land--preservation-matrix)

---

## 2. How to read this matrix

Every preservation rule in this domain is a function of **four** independent variables. A row is a preservation rule **only if all four are answered**:

1. **What kind of object is it?** (Person Assertion · LandInstrument · DNASegment · …)
2. **What lifecycle phase is it in?** (RAW · WORK/QUARANTINE · PROCESSED · CATALOG/TRIPLET · PUBLISHED)
3. **What is its sensitivity tier today?** (T0 · T1 · T2 · T3 · T4 per Atlas v1.1 §24.5)
4. **What event is firing?** (steady state · consent revocation · vendor-loss · correction · sovereignty change · subject death · re-tier downgrade · rollback drill)

Read the matrix as: *"Given object X in phase Y at tier Z, when event E fires, do A."* Where any of X/Y/Z/E is unresolved, the answer **defaults to deny / quarantine / abstain** — never to publish. [DOM-PEOPLE §I] [DIRRULES]

> [!NOTE]
> **Truth-label key.** **CONFIRMED** = grounded in attached doctrine. **PROPOSED** = doctrine implies but does not codify; awaiting verification. **NEEDS VERIFICATION** = checkable against a mounted repo, not yet checked. **UNKNOWN** = not resolvable from current evidence. **CONFLICTED** = two confirmed sources disagree. Every retention number in this matrix is **PROPOSED** until a Retention SLA ADR lands ([OPEN-PRES-02](#10-open-questions--verification-backlog)).

[↑ back to top](#people--dna--land--preservation-matrix)

---

## 3. Sensitivity tier recap

Reproduced compactly from Atlas v1.1 §24.5 for in-page reference; the master tier table governs. [Atlas v1.1 §24.5.1]

| Tier | Name | Default audience | People · DNA · Land application |
|---|---|---|---|
| **T0** | Open | Any public client via governed API | Aggregate / pre-1900 / fully-published vital records where rights are clean. |
| **T1** | Generalized | Any public client, after recorded transform | County-aggregated population panels; generalized parcel polygons. |
| **T2** | Reviewer | Stewards · reviewers · named collaborators | Working person-assertion graphs prior to release; relationship hypotheses. |
| **T3** | Restricted | Named authorized parties under recorded agreement | DNA segments under explicit research-agreement; living-person review datasets. |
| **T4** | Denied | — | Raw DNA segments · living-person fields · private person-parcel joins · raw DTC kits. |

> [!WARNING]
> **Tier upgrades (toward more public) require both a transform receipt AND a review record** (T4 → T1 = `RedactionReceipt` + `ReviewRecord` + `PolicyDecision`, plus Promotion Gates A–G). **Tier downgrades (toward less public) need a `CorrectionNotice`** — correction is always sufficient to restrict, and is reversible. [Atlas v1.1 §24.5.3]

[↑ back to top](#people--dna--land--preservation-matrix)

---

## 4. Preservation flow

The CONFIRMED lifecycle invariant is `RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED`. For this domain, preservation branches off that spine at four event hinges: consent revocation, vendor-loss, correction, and rollback. [DIRRULES] [DOM-PEOPLE §M] [Atlas v1.1 §24.5]

```mermaid
flowchart TD
  RAW["RAW<br/>source-faithful capture"]
  WORK["WORK / QUARANTINE<br/>normalize, validate, hold"]
  PROC["PROCESSED<br/>public-safe candidates"]
  CAT["CATALOG / TRIPLET<br/>EvidenceBundle closure"]
  PUB["PUBLISHED<br/>governed API surface"]

  REV{{"event: consent revocation"}}
  VEN{{"event: vendor loss / TOS change"}}
  COR{{"event: correction / new evidence"}}
  RBK{{"event: rollback drill"}}

  TOMB["Tombstone receipt<br/>(append-only audit)"]
  ERASE["Erasure procedure<br/>(narrow, logged, ADR-gated)"]
  EMB["Embargo /<br/>re-quarantine"]
  REPUB["Republish at lower tier<br/>or with new transform"]

  RAW --> WORK --> PROC --> CAT --> PUB

  REV -.-> EMB
  REV -.-> TOMB
  REV -.-> ERASE
  VEN -.-> EMB
  VEN -.-> TOMB
  COR -.-> TOMB
  COR -.-> REPUB
  RBK -.-> TOMB

  classDef phase fill:#1e293b,stroke:#94a3b8,color:#f1f5f9;
  classDef event fill:#7c2d12,stroke:#fdba74,color:#fff;
  classDef pres fill:#064e3b,stroke:#6ee7b7,color:#ecfdf5;
  class RAW,WORK,PROC,CAT,PUB phase;
  class REV,VEN,COR,RBK event;
  class TOMB,ERASE,EMB,REPUB pres;
```

> [!NOTE]
> **PROPOSED diagram.** The five lifecycle phases are CONFIRMED [DIRRULES]; the four event hinges are CONFIRMED [DOM-PEOPLE §M; Atlas §24.5; Pass-10 C5-09 / C6-08 / C9-07]. The dashed paths show which preservation actions are valid responses — the *choice* between tombstone, erasure, embargo, or republication is governed by §§6–7 below, not by the diagram alone.

[↑ back to top](#people--dna--land--preservation-matrix)

---

## 5. Object-class preservation matrix

Rows are the object families this domain owns ([DOM-PEOPLE §B]). Columns are the preservation duties that follow from KFM doctrine. Default-tier values reproduce Atlas v1.1 §24.5; retention values are **PROPOSED** placeholders awaiting the Retention SLA ADR ([OPEN-PRES-02](#10-open-questions--verification-backlog)).

| Object class | Default tier | RAW retention | Derived retention | Audit / tombstone retention | Erasure-eligible? | Citation |
|---|---|---|---|---|---|---|
| Person Assertion (deceased subject) | T0–T1 | indefinite (historical record) | indefinite | indefinite | NO — historical claim | [DOM-PEOPLE §I] |
| Person Assertion (living subject) | T4 | encrypted RAW only; PROPOSED ≤ TTL of consent | only via aggregation/k-anon → T1 | indefinite tombstone, no claim retained | NEEDS VERIFICATION | [DOM-PEOPLE §I]; [Pass-10 C6-06, C5-09] |
| PersonCanonical | mirrors strongest input | mirrors strongest input | mirrors strongest input | indefinite | NEEDS VERIFICATION | [DOM-PEOPLE §E] |
| NameAssertion | T0–T1 | source-vintage | indefinite (graph projection) | indefinite | NO | [DOM-PEOPLE §C] |
| LifeEvent · Residence · Migration | T0–T2 by living-flag | source-vintage | indefinite for deceased; consent-bound for living | indefinite | per subject status | [DOM-PEOPLE §C] |
| Genealogy Relationship | T1–T2 | source-vintage | indefinite (graph projection) | indefinite | NO unless living-leak | [DOM-PEOPLE §B] |
| FamilyGroup | T1–T2 | source-vintage | indefinite | indefinite | NO | [DOM-PEOPLE §B] |
| Relationship Hypothesis | T2 default | working set only | NEVER published as truth | indefinite (audit) | NO | [DOM-PEOPLE §I] |
| **DNA Match Evidence** | **T4** | encrypted RAW, scoped access, PROPOSED TTL bound by consent | aggregate / k-anonymized only, with `AggregationReceipt` | indefinite tombstone | NEEDS VERIFICATION — see §7 | [DOM-PEOPLE §I]; [Pass-10 C9-03, C9-04] |
| **DNASegment** | **T4** forever-T4 unless named research agreement → T3 | encrypted RAW only | NEVER public; T3 only under named consent | indefinite tombstone | NEEDS VERIFICATION | [Atlas v1.1 §24.5.2]; [Pass-10 C9-03] |
| **DNAKitToken** | **T4** | pointer-only; raw kit/vendor ID NEVER logged | never derived | indefinite tombstone | NEEDS VERIFICATION | [DOM-PEOPLE §C]; [Pass-10 C9-03] |
| **ConsentGrant** | T2 | signed manifest, indefinite | indefinite (governs other rows) | indefinite | NO (would destroy audit) | [Pass-10 C6-07] |
| **RevocationReceipt** | T2 | signed manifest, indefinite, append-only | indefinite | indefinite (this *is* the audit) | NO | [Pass-10 C5-09, C6-08] |
| LandParcel (current) | T0–T1 | source-vintage | indefinite | indefinite | NO | [DOM-PEOPLE §C] |
| LegalDescription | T0 | indefinite | indefinite | indefinite | NO | [DOM-PEOPLE §C] |
| LandInstrument · Deed · Title (historical) | T0 | indefinite (public record) | indefinite | indefinite | NO | [DOM-PEOPLE §B] |
| Assessor Record · TaxRecord | T1–T2 | source-vintage | indefinite as *evidence*; **never as title truth** | indefinite | NO | [DOM-PEOPLE §I] — "assessor/tax records are not title truth" |
| Parcel Version | T0–T1 | source-vintage | indefinite | indefinite | NO | [DOM-PEOPLE §B] |
| Ownership Interval | T0–T1 | source-vintage | indefinite | indefinite | NO | [DOM-PEOPLE §B] |
| **Private person-parcel join** | **T4** | working set only; never persisted publicly | T2 only via generalized parcel + de-identified person | indefinite tombstone | NEEDS VERIFICATION | [Atlas v1.1 §24.5.2] |

> [!CAUTION]
> **Quiet defaults are failure modes.** Any row without an explicit tier, transform, and gate falls to T4 / DENY at runtime. The matrix does not "discover" a public-safe path for an unlabeled record. If a steward cannot place a record into a row above, the record stays in WORK/QUARANTINE. [DOM-PEOPLE §I] [DIRRULES]

[↑ back to top](#people--dna--land--preservation-matrix)

---

## 6. Trigger → action matrix

Preservation is event-driven. Steady-state retention is the easy column; the hard columns are what fires when consent is withdrawn, when a DTC vendor files Chapter 11, when a subject dies, or when new evidence corrects a claim. [Pass-10 C5-09, C6-08, C9-07]

| Trigger | RAW action | WORK / PROCESSED action | CATALOG / PUBLISHED action | Audit ledger action | Cache / tile action |
|---|---|---|---|---|---|
| **Consent revocation** (subject withdraws) | Hold in encrypted RAW pending erasure decision; **never delete silently** | Re-quarantine working derivatives | Append `RevocationReceipt`; remove from layer manifest at next release | Append signed tombstone with revocation reference and supersession ref | Invalidate PMTiles / tile cache via revocation endpoint (`embargo_until = now`) |
| **DTC vendor loss / TOS change** (e.g., 23andMe Ch. 11) | Embargo all affected raw exports; freeze ingestion | Halt promotion of dependent derivatives | Demote affected layers to T4; emit `CorrectionNotice` | Append vendor-watch event + per-record tombstones for ambiguous-consent records | Cache purge for affected vendor-derived layers |
| **Correction** (new evidence supersedes a published claim) | RAW preserved | Working derivative re-validated | Republish under new digest; old release tombstoned, not deleted | Append correction lineage with supersession ref | Cache invalidation; downstream derivatives recompiled |
| **Subject death** (living → deceased status change) | RAW preserved | Re-classify living-flag; rerun policy gate | Promote previously denied fields only if rights and evidence support | Append status-change receipt | No invalidation unless tier moved |
| **Sovereignty / CARE-authority change** | RAW preserved | Re-evaluate authority-to-control | Default-deny until renewed consent grant | Append CARE-event entry | Embargo applies until renewed |
| **Rollback drill / replay** | RAW used as replay input | Replay validates from RAW to current release | Compare replayed release to current; record any drift | Append `RollbackCard` exercise receipt | None (drill is non-public) |
| **Right-to-erasure request** | See §7 — **escalates to ADR-gated procedure** | — | — | Tombstone always; erasure only after ADR + named authority | — |

> [!IMPORTANT]
> **Tombstone before delete.** Across every event row above, the **first** action is to append an immutable record (tombstone, correction, receipt). Physical removal of any object is a **second, separate, ADR-gated action** — never an alternative to recording. [Pass-10 C5-09]

[↑ back to top](#people--dna--land--preservation-matrix)

---

## 7. Tombstone vs. erasure decision matrix

The corpus is explicit that **tombstones satisfy explainability but not erasure** (Pass-10 C5-09 tensions). For this domain, the boundary between "tombstone is sufficient" and "physical erasure is required" is currently **NEEDS VERIFICATION** — it depends on the right-to-erasure framework that applies to the subject (jurisdiction, vendor TOS, CARE/sovereignty obligations) and on whether audit-ledger immutability is preserved by external archival proof. [Pass-10 C5-09 open question; C1-06]

> [!CAUTION]
> **Append-ledger status correction (v0.2).** The append-only audit ledger concept is carried by Pass-10 **C1-06**, whose status in the corpus is **PROPOSED** (and whose Pass-23 variant is also PROPOSED; the corpus is silent on which backend KFM picks first). The *tombstone-not-deletion* rule (C5-09) and the *revocation discipline* (C6-08) are **CONFIRMED**. The append-only *invariant* is therefore best stated as: **CONFIRMED that revocation appends rather than deletes; PROPOSED that the ledger backend providing write-once semantics exists.** v0.1 labeled the ledger itself CONFIRMED — corrected here.

| Scenario | Tombstone alone? | Physical erasure required? | Gate | Status |
|---|---|---|---|---|
| Public deceased-subject claim corrected | YES | NO | `CorrectionNotice` + `ReviewRecord` | CONFIRMED doctrine [C5-09] |
| Living-subject record where consent was never valid (ingested in error) | NO | YES — quarantine + delete RAW + tombstone the fact | ADR-gated; steward + rights-holder sign-off | PROPOSED |
| Living-subject record under valid revoked consent | YES (default) | Only if the revocation grant requires deletion | `RevocationReceipt` + DUO-code check | NEEDS VERIFICATION [C6-08, C9-04] |
| Raw DNA segment under revoked DTC consent (e.g., vendor Ch. 11) | YES (default) | If vendor TOS or jurisdiction mandates erasure | ADR-gated; vendor-watch trigger | NEEDS VERIFICATION [C9-03, C9-07] |
| CARE-controlled record where the controlling authority revokes | YES (default) | If the authority's revocation explicitly requires erasure | Steward + named authority sign-off | NEEDS VERIFICATION |
| Audit ledger itself | NEVER erased | NEVER | append-only invariant | CONFIRMED that revocation appends not deletes [C5-09]; PROPOSED that the write-once backend exists [C1-06] |

> [!WARNING]
> **Erasure is the narrowest exception to the append-only posture, not the rule.** When erasure occurs, the *fact of erasure* is itself logged: an erasure receipt records who decided, on what evidence, under what authority, and which objects were removed — **without restating the removed content**. The erasure-receipt schema is **PROPOSED** ([OPEN-PRES-13](#10-open-questions--verification-backlog)). [Pass-10 C5-09; storage-maintenance card, NEEDS VERIFICATION — see §10 appendix]

[↑ back to top](#people--dna--land--preservation-matrix)

---

## 8. Source-family preservation profile

Per-source preservation diverges from per-object preservation: a single source can spawn many object instances, each with its own tier and retention. This table captures the **upstream** preservation duties at the source level. Source families reproduced from [DOM-PEOPLE §D].

| Source family | Default tier of capture | RAW preservation | Vendor-watch applies? | Notes |
|---|---|---|---|---|
| Vital · cemetery · burial · obituary · church · school · military · census · directory · court · probate records | T0–T2 by living-flag | indefinite; source-faithful | NO | Living-flag determined at ingest; reverify at promotion. |
| GEDCOM 5.5 / GEDCOM-X / GEDZip tree overlays | T2 working | **preserve original file as asset** + custom-tag provenance sidecar *(sidecar is PROPOSED)* | NO | Original-as-asset CONFIRMED [Pass-10 C9-01]; provenance sidecar PROPOSED [KFM-P22-PROG-0046]. |
| FamilySearch API responses | T2 | RAW response + `access_token` fingerprint (not the token) + GA4GH Passport claim used at fetch + response checksum | YES (OAuth2 scope revocation propagates) | Retention-after-revocation is an explicit open question [Pass-10 C9-02 → OPEN-PRES-03]. |
| DNA vendor match CSV · segment · triangulation data | T4 | encrypted RAW only; access-scoped; **raw genotype never republished** | YES — vendor-watch is mandatory | [Pass-10 C9-03, C9-07]. |
| DTC raw genomic exports (23andMe, AncestryDNA, MyHeritage) | T4 | encrypted RAW only; PROPOSED TTL bound by consent | YES — 23andMe Ch. 11 (Mar 2025) is the canonical scenario | [Pass-10 C9-03, C9-07]. |
| Patent · deed · mortgage · lien · easement · lease · mineral · water · access · probate instruments | T0 | indefinite (public record) | NO | [DOM-PEOPLE §D]. |
| Assessor and tax-roll records | T1–T2 | source-vintage; **never treated as title truth** | NO | [DOM-PEOPLE §I] — assessor-as-title denial validator. |
| Plat · survey · metes · bounds · PLSS · subdivision · derived geometry | T0–T1 | indefinite | NO | Geometry never carries title-boundary authority without source-role evidence [DOM-PEOPLE §I]. |
| Oral-history and cultural knowledge (cross-domain with [DOM-ARCH]) | T3–T4 default | sovereignty review required before any preservation transform | CARE-authority watch applies | CARE fields required in KFM Meta Block v2; cross-references [DOM-ARCH] sovereignty path. |

[↑ back to top](#people--dna--land--preservation-matrix)

---

## 9. Anti-patterns this matrix exists to prevent

Drawn from [DOM-PEOPLE §I], Atlas §24.5, Pass-10 C5-09 / C6-08 / C9-03 / C9-07, and Directory Rules §13. Each is a documented failure mode; the matrix exists so reviewers can name and refuse it.

- **Silent deletion of RAW after consent revocation.** Revocation appends; it does not delete by default. Deletion requires the §7 erasure path with its own receipt. [C5-09]
- **Treating tombstone as erasure.** Tombstone hides; erasure removes. Conflating them either leaks (treating erasure-required records as tombstoned-and-retained) or loses audit (treating tombstone-sufficient records as deleted). [C5-09]
- **Labeling the append-ledger CONFIRMED when its backend is unchosen.** C1-06 is PROPOSED; do not let a reading aid promote it. *(New in v0.2.)*
- **Promoting Relationship Hypothesis as truth.** Hypotheses are working-set objects [DOM-PEOPLE §B]; they do not cross the publication boundary as claims.
- **Treating assessor or tax records as title truth.** Assessor-as-title denial is a doctrinal validator [DOM-PEOPLE §I, §K].
- **Treating parcel geometry as title-boundary proof.** Geometry without source-role evidence is context, not title [DOM-PEOPLE §I].
- **Persisting a private person-parcel join publicly.** T4 default; only generalized-parcel + de-identified-person → T2 paths exist [Atlas §24.5.2].
- **Logging raw kit / vendor DNA IDs.** Pointer-only [Pass-10 C9-03]; raw IDs never enter logs, receipts, or evidence bundles.
- **Storage maintenance (vacuum / partition-prune) destroying audit value without a retention/archival decision.** Storage maintenance is a governance decision, not a janitorial one. [Storage-maintenance card; NEEDS VERIFICATION — see §10 appendix]
- **Falling back to T0 because a record's tier is unresolved.** Unlabeled records default to **T4 / DENY**, never to publish.
- **AI summarization standing in for evidence.** AI may summarize *released* EvidenceBundles only; it must ABSTAIN where evidence is insufficient and DENY where policy blocks [DOM-PEOPLE §L; GAI].

[↑ back to top](#people--dna--land--preservation-matrix)

---

## 10. Open questions & verification backlog

These items must resolve before any retention number, route, schema URI, or test name in this matrix becomes operational. Mirrors the per-domain Verification Backlog discipline in [DOM-PEOPLE §N].

| ID | Item to verify | Evidence that would settle it | Status | Cross-ref |
|---|---|---|---|---|
| OPEN-PRES-01 | Tombstone vs. erasure boundary for personal data | ADR + documented jurisdictional / vendor-TOS / CARE-authority criteria | NEEDS VERIFICATION | [Pass-10 C5-09] |
| OPEN-PRES-02 | Retention SLAs for each lifecycle tier (RAW … TOMBSTONED) | Retention SLA ADR with per-tier numbers | NEEDS VERIFICATION | [Pass-10 C1-06 open question] |
| OPEN-PRES-03 | FamilySearch response retention after consent revocation | FamilySearch Retention Policy aligned with GA4GH revocation semantics | NEEDS VERIFICATION | [Pass-10 C9-02] |
| OPEN-PRES-04 | DTC raw retention — solvent vendor vs. distressed vendor | Vendor-watch SOP + retention triggers | NEEDS VERIFICATION | [Pass-10 C9-03, C9-07] |
| OPEN-PRES-05 | Consent vocabulary normalization (JWT · GA4GH Passport · Meta Block v2) | Canonical normalization spec | NEEDS VERIFICATION | [Pass-10 C6-07 expansion] |
| OPEN-PRES-06 | DUO version handling in long-running consent grants | DUO compatibility profile pinned to policy bundle | NEEDS VERIFICATION | [Pass-10 C9-04] |
| OPEN-PRES-07 | Living-person policy enforcement (schema · validator · UI · API · CI) | Mounted repo: files, schemas, registry, tests, logs, manifests | NEEDS VERIFICATION | [DOM-PEOPLE §N] |
| OPEN-PRES-08 | DNA consent / revocation enforcement | Mounted repo: files, schemas, registry, tests, logs, manifests | NEEDS VERIFICATION | [DOM-PEOPLE §N] |
| OPEN-PRES-09 | Land instrument chain-of-title logic | Mounted repo: files, schemas, registry, tests, logs, manifests | NEEDS VERIFICATION | [DOM-PEOPLE §N] |
| OPEN-PRES-10 | Geometry-role boundary logic (geometry is not title) | Mounted repo: files, schemas, registry, tests, logs, manifests | NEEDS VERIFICATION | [DOM-PEOPLE §N] |
| OPEN-PRES-11 | UI / API restricted-field no-leak behavior | Mounted repo: files, schemas, registry, tests, logs, manifests | NEEDS VERIFICATION | [DOM-PEOPLE §N] |
| OPEN-PRES-12 | Object families that must never be vacuumed without external archival proof | Archive Manifest + retention/vacuuming policy ADR | NEEDS VERIFICATION | [Storage-maintenance card; see appendix] |
| OPEN-PRES-13 | Erasure-receipt schema (what to log when log-without-content is required) | Schema + fixtures + policy test | PROPOSED | derived from §7 |
| OPEN-PRES-14 | Owner names for this matrix (steward, release authority, separation of duties) | ADR-S-people-stewards (PROPOSED) | UNKNOWN | placeholder in front-matter |
| OQ-PDL-SEG-01 | Segment name: `people` (Atlas Ch. 24.13) vs `people-dna-land` (DIRRULES §12) | ADR | CONFLICTED | carried from MISSING_OR_PLANNED_FILES v0.2 |

<details>
<summary><strong>Citation-integrity appendix (new in v0.2)</strong></summary>

v0.1 cited several stable-ID idea cards that **could not be confirmed** against the indexed corpus in this session. They have been softened to anchored doctrine and flagged rather than removed, per the operating contract's no-fabrication rule. Reinstatement is welcome once a card-ID is confirmed in a mounted-repo or corpus check.

| v0.1 citation | Disposition in v0.2 | Anchored to (confirmed) |
|---|---|---|
| `KFM-P17-PROG-0018` (ConsentGrant) | Removed; replaced with `[Pass-10 C6-07]` | C6-07 Compact Consent Tokens — CONFIRMED |
| `KFM-P19-IDEA-0003` (RevocationReceipt) | Removed; replaced with `[Pass-10 C5-09, C6-08]` | C5-09 / C6-08 — CONFIRMED |
| `KFM-P9-PROG-0018` (erasure logging) | Softened to "storage-maintenance card; NEEDS VERIFICATION" | Pass-23 storage-maintenance card citing KFM-P1-PROG-0048 / KFM-P4-PROG-0005 — PROPOSED, exact ID NEEDS VERIFICATION |
| `KFM-P9-PROG-0010 / -0011` (archive manifest) | Softened to "Archive Manifest; NEEDS VERIFICATION" | same storage-maintenance card — PROPOSED |
| `KFM-P22-PROG-0046` (GEDCOM sidecar) | **Retained**; confirmed present but card status is PROPOSED | KFM-P22-PROG-0046 — card exists, status PROPOSED |
| `[KFM-encyclopedia §6.2]`, `§13.1` | Retained as `[ENCY]` references; exact section numbers NEEDS VERIFICATION | ENCY domain-dossier convention — CONFIRMED concept |

**Why this matters.** Every entry in this backlog is a place where a quiet drift could turn the preservation matrix from a trust artifact into theater. The corpus is explicit that retention discipline without codified numbers gets "answered ad hoc per domain" (C1-06 open question); that the tombstone-erasure boundary is the most consequential unresolved question in the consent regime (C5-09 open question); and that vendor-loss scenarios like 23andMe's March-2025 Chapter 11 filing moved consent posture from a steady-state concern to a live operational drill (C9-07). This matrix is honest about what it does not yet decide — and about which of its own citations are not yet confirmed.

</details>

[↑ back to top](#people--dna--land--preservation-matrix)

---

## 11. Related docs

- `docs/domains/people-dna-land/README.md` — domain dossier landing page *(PROPOSED authoring)*. [ENCY]
- `docs/domains/people-dna-land/PEOPLE_DOMAIN_MODEL.md` — bounded-context model; identity rules, aggregates, invariants *(authored v0.1)*.
- `docs/domains/people-dna-land/MISSING_OR_PLANNED_FILES.md` — file inventory; source of OQ-PDL-SEG-01 *(v0.2)*.
- `docs/domains/people-dna-land/VERIFICATION_BACKLOG.md` — open verification items including those mirrored in §10 *(PROPOSED)*. [DOM-PEOPLE §N]
- `docs/doctrine/directory-rules.md` — canonical placement and lifecycle invariant; §13 anti-patterns. [DIRRULES]
- `docs/doctrine/lifecycle-law.md` — promotion as governed transition, not file move *(PROPOSED placement)*. [DIRRULES]
- `docs/doctrine/trust-membrane.md` — public surface never reads canonical store directly *(PROPOSED placement)*. [DIRRULES §7]
- `docs/standards/SENSITIVITY_RUBRIC.md` — sensitivity-rank canonical rubric *(PROPOSED; Pass-10 C6-01)*.
- `docs/runbooks/revocation.md` — operational revocation playbook *(PROPOSED; Pass-10 C5-09 expansion)*.
- `docs/registers/DRIFT_REGISTER.md` — where conflicts with doctrine are filed. [DIRRULES §13]
- Atlas v1.1 §24.5 — Master Sensitivity / Rights Tier Reference. [ENCY]
- Pass-10 Idea Index — C1-06 (append ledger), C5-09 (tombstones), C6-01/05/06/07/08, C9-01/02/03/04/07.

---

<sub><i>Edit discipline: this matrix is a doctrine surface, not a release surface. Edits MUST preserve the lifecycle invariant, sensitivity defaults, and reversibility. Promotion of any <strong>PROPOSED</strong> retention number, path, card-ID, or test name to <strong>CONFIRMED</strong> requires mounted-repo or corpus evidence; otherwise file a drift entry and leave the label.</i></sub>

**Last updated:** 2026-06-07 · **Edition:** v0.2 · **Status:** draft · **CONTRACT_VERSION:** 3.0.0 · [↑ back to top](#people--dna--land--preservation-matrix)
