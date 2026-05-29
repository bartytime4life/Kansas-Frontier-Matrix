<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/PLACEHOLDER-uuid
title: Archaeology — Verification Backlog and Open Questions
type: standard
version: v1
status: draft
owners: <archaeology-domain-steward> (PLACEHOLDER — confirm)
created: 2026-05-28
updated: 2026-05-28
policy_label: public
related: [docs/domains/archaeology/README.md, docs/domains/archaeology/sensitivity-and-publication-posture.md, docs/domains/archaeology/pipeline-shape.md, docs/domains/archaeology/source-families.md, docs/registers/VERIFICATION_BACKLOG.md, docs/registers/DRIFT_REGISTER.md, ai-build-operating-contract.md]
tags: [kfm, archaeology, verification, backlog, open-questions, ADR, sensitive-domain]
notes: [CONTRACT_VERSION = "3.0.0" pinned; every item NEEDS VERIFICATION by design, repo not mounted this session]
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# 🏺 Archaeology — Verification Backlog and Open Questions

> What must be checked against a mounted repository before any Archaeology claim, control, or layer can be promoted from PROPOSED to CONFIRMED.

![status](https://img.shields.io/badge/status-draft-orange)
![policy](https://img.shields.io/badge/policy-public_doc-blue)
![sensitivity](https://img.shields.io/badge/sensitive_domain-DENY_by_default-critical)
![backlog](https://img.shields.io/badge/all_items-NEEDS_VERIFICATION-yellow)
![contract](https://img.shields.io/badge/CONTRACT__VERSION-3.0.0-informational)
![repo--state](https://img.shields.io/badge/repo-not_mounted-lightgrey)

**Status:** `draft` · **Owners:** `<archaeology-domain-steward>` (PLACEHOLDER) · **Updated:** 2026-05-28

> [!IMPORTANT]
> **Everything in this document is `NEEDS VERIFICATION` by design.** No repository is mounted in this session. This backlog exists precisely so that no Archaeology control is asserted as implemented without evidence. The main project risk is not lack of ideas — it is overclaiming maturity before repo, runtime, rights, and proof-object evidence exists.

---

## Quick jump

- [1. Scope](#1-scope)
- [2. Repo fit](#2-repo-fit)
- [3. Doctrine verification backlog (§15.N)](#3-doctrine-verification-backlog-15n)
- [4. Validator and test backlog (§15.K)](#4-validator-and-test-backlog-15k)
- [5. Open questions register](#5-open-questions-register)
- [6. Related ADR backlog items](#6-related-adr-backlog-items)
- [7. What "settled" means](#7-what-settled-means)
- [8. Promotion readiness checklist](#8-promotion-readiness-checklist)
- [9. Open verification backlog](#open-verification-backlog)
- [10. Changelog](#changelog-v0--v1)
- [11. Definition of done](#definition-of-done)
- [Related docs](#related-docs)

---

## 1. Scope

This document consolidates the **verification backlog and open questions** for the Archaeology / Cultural Heritage domain: the doctrine items that must be checked against a mounted repository, the validators that must be proven to exist and pass, the open questions awaiting steward or ADR resolution, and what evidence would settle each.

> [!NOTE]
> **Truth labels in this doc.** The backlog items themselves are `CONFIRMED` doctrine (Atlas §15.N, §15.K) — it is `CONFIRMED` that these are the open items. Each item's *resolution* is `NEEDS VERIFICATION` until checked against repository evidence. All repo paths are `PROPOSED`.

[↑ Back to top](#top)

---

## 2. Repo fit

| Aspect | Value | Status |
|---|---|---|
| Proposed path | `docs/domains/archaeology/verification-backlog.md` | `PROPOSED` |
| Owning responsibility root | `docs/` (explains something to humans) | `CONFIRMED` rule |
| Repo-wide register counterpart | `docs/registers/VERIFICATION_BACKLOG.md` | `PROPOSED` |
| Drift register | `docs/registers/DRIFT_REGISTER.md` | `PROPOSED` |
| Upstream | `ai-build-operating-contract.md`; `directory-rules.md` §2.5; `[ENCY]` | `CONFIRMED` rule / `PROPOSED` presence |

**Directory Rules basis.** A doc that *explains to humans* lives under `docs/`. This is the **domain-scoped** backlog; the repo-wide register is `docs/registers/VERIFICATION_BACKLOG.md`, and conflicts between doctrine and a mounted repo are logged in `docs/registers/DRIFT_REGISTER.md` per Directory Rules §2.5.

[↑ Back to top](#top)

---

## 3. Doctrine verification backlog (§15.N)

`CONFIRMED` doctrine (Atlas §15.N). Each item is `NEEDS VERIFICATION`; the evidence that would settle it is the same class for all: *mounted repo files, schemas, registry entries, tests, logs, emitted artifacts, review records, or release manifests.*

| ID | Item to verify | Why it matters | Status |
|---|---|---|---|
| **VB-ARCH-01** | Verify steward authority and confidentiality. | Determines who can authorize sensitive release and under what confidentiality. | `NEEDS VERIFICATION` |
| **VB-ARCH-02** | Define public geometry thresholds and transform profiles. | Without thresholds, "generalize to county/region" is undefined; redaction can't be validated. | `NEEDS VERIFICATION` |
| **VB-ARCH-03** | Verify oral history / cultural knowledge protocol. | Steward-controlled knowledge needs an explicit handling protocol before any use. | `NEEDS VERIFICATION` |
| **VB-ARCH-04** | Verify emergency public-layer disablement and rollback drill. | A sensitive lane must be able to pull a public layer fast and prove the rollback works. | `NEEDS VERIFICATION` |

> [!CAUTION]
> VB-ARCH-02 and VB-ARCH-04 are the highest-risk gaps: undefined generalization thresholds and an unproven disablement drill both expose the lane to exact-site leakage. These should block any public Archaeology layer until resolved.

[↑ Back to top](#top)

---

## 4. Validator and test backlog (§15.K)

`PROPOSED` (Atlas §15.K). These validators/tests are named in doctrine but unverified as implemented. Each must be proven to exist and to exercise its `DENY`/`ABSTAIN` paths, not just happy paths.

| ID | Validator / test | Negative state it must exercise | Status |
|---|---|---|---|
| **VT-ARCH-01** | EvidenceBundle-required tests | Claim without resolvable evidence → `ABSTAIN` | `PROPOSED` |
| **VT-ARCH-02** | Candidate-not-site tests | `CandidateFeature` queried as confirmed site → `DENY` | `PROPOSED` |
| **VT-ARCH-03** | Public no-leak tests | Exact geometry reaching a public surface → `DENY` | `PROPOSED` |
| **VT-ARCH-04** | Rights and cultural-review tests | Unresolved rights / missing cultural review → `HOLD`/`DENY` | `PROPOSED` |
| **VT-ARCH-05** | Exact sensitive geometry denial | Precise coordinates in any public output → `DENY` | `PROPOSED` |
| **VT-ARCH-06** | Catalog closure tests | Unresolved `EvidenceRef` / digest mismatch → `HOLD` | `PROPOSED` |
| **VT-ARCH-07** | AI exact-location denial | AI asked for exact location → `DENY` | `PROPOSED` |

> [!TIP]
> Negative-state coverage is the point. A validator that only proves the happy path does not satisfy the lane's fail-closed posture; each test above must demonstrate the `DENY`/`ABSTAIN`/`HOLD` branch.

[↑ Back to top](#top)

---

## 5. Open questions register

| ID | Question | Owner role | Resolution path |
|---|---|---|---|
| OQ-ARCH-VB-01 | Who holds final release authority for Archaeology, distinct from the author? | release authority | repo inspection / §15.N item 1 |
| OQ-ARCH-VB-02 | What are the numeric public geometry thresholds (buffer radius, generalization unit)? | archaeology steward | ADR / §15.N item 2 |
| OQ-ARCH-VB-03 | What is the oral-history / cultural-knowledge handling protocol and who ratifies it? | tribal/cultural reviewer | steward ratification / §15.N item 3 |
| OQ-ARCH-VB-04 | Is there an emergency disablement + rollback drill, and has it been exercised? | release authority | repo inspection / §15.N item 4 |
| OQ-ARCH-VB-05 | Are the §23.2 Archaeology defaults ratified or still PROPOSED? | archaeology steward | steward ratification |

[↑ Back to top](#top)

---

## 6. Related ADR backlog items

`PROPOSED` ADR backlog (corpus §24.12 / ADR-S series). These repo-wide ADRs directly affect Archaeology resolution:

| ADR (PROPOSED) | Decision needed | Archaeology impact |
|---|---|---|
| **ADR-S-05** | Sensitivity tier scheme (T0–T4) — adopt or revise | Sets the tier for sites, human remains, sacred sites (T4). |
| **ADR-S-11** | Cross-lane join policy + `most-restrictive-applicable` default | Governs Archaeology joins to Spatial Foundation, Roads/Rail, Settlements, Hazards. |
| **ADR-S-12** | Two-person-rule scope for T3/T4 promotion | Determines whether sensitive Archaeology release needs two-person sign-off. |
| **ADR-S-04** | Source-role enum + evolution rule | Fixes the roles Archaeology sources may carry. |
| **ADR-S-01** | Confirm `schemas/contracts/v1/...` schema home | Where Archaeology schemas + SourceDescriptor live. |

> [!NOTE]
> `CONFIRMED` doctrine (corpus §24.5): for Archaeology human remains / sacred sites, **no transform releases them to T0**; T3 only under explicit named authorization, with sovereignty review. That tier rule is settled even while ADR-S-05 (the scheme's ratification) is open.

[↑ Back to top](#top)

---

## 7. What "settled" means

A backlog item moves from `NEEDS VERIFICATION` to `CONFIRMED` only when checked against **admissible evidence in a session where the repository is mounted**:

```text
mounted repo files · schemas · registry entries · tests ·
logs · emitted artifacts · review records · release manifests
```

> [!IMPORTANT]
> Cross-session memory is not evidence. "I verified this before" does not settle an item. Each item must be re-checked against current repository evidence; an attached PDF, a prior plan, or a workspace-only scan does not satisfy the rule.

[↑ Back to top](#top)

---

## 8. Promotion readiness checklist

Before any Archaeology public layer or claim is promoted from `PROPOSED`/`draft` to `published`:

- [ ] VB-ARCH-01 — steward authority and confidentiality confirmed
- [ ] VB-ARCH-02 — public geometry thresholds and transform profiles defined
- [ ] VB-ARCH-03 — oral-history / cultural-knowledge protocol verified
- [ ] VB-ARCH-04 — emergency disablement + rollback drill exercised
- [ ] VT-ARCH-01…07 — validators exist and exercise their `DENY`/`ABSTAIN`/`HOLD` paths
- [ ] §23.2 Archaeology defaults ratified (or most-restrictive-row applied)
- [ ] ADR-S-05, ADR-S-11, ADR-S-12 resolved or their absence logged in `DRIFT_REGISTER.md`
- [ ] `ReleaseManifest`, correction path, and rollback target present

[↑ Back to top](#top)

---

## Open verification backlog

These items remain `NEEDS VERIFICATION` before this *document* is promoted from `draft` to `published`:

1. Confirm `docs/registers/VERIFICATION_BACKLOG.md` exists and whether per-domain backlogs roll up into it.
2. Confirm the VB-/VT- ID scheme used here matches any repo-wide convention (or log the mismatch in `DRIFT_REGISTER.md`).
3. Confirm the ADR-S item numbers against the live ADR index.
4. Confirm the §24.5 tier assignments for Archaeology objects.

## Changelog v0 → v1

| Change | Type (per contract §37) | Reason |
|---|---|---|
| Initial draft of Archaeology verification backlog | new | Consolidates Atlas §15.N + §15.K + related ADR-S items |
| Introduced VB-/VT- local ID scheme | clarification | Make backlog items individually trackable |
| Pinned `CONTRACT_VERSION = "3.0.0"` | clarification | Doctrine-adjacent doc requirement |

> **Backward compatibility.** New document; no prior anchors to preserve. The VB-/VT- IDs are local to this doc and `NEEDS VERIFICATION` against any repo-wide scheme.

## Definition of done

This document is done enough to enter the repository when:

- it is placed according to Directory Rules (`docs/domains/archaeology/`);
- a docs steward and the archaeology domain steward review it;
- it is linked from the archaeology lane README and `docs/registers/VERIFICATION_BACKLOG.md`;
- it does not conflict with accepted ADRs;
- the VB-/VT- ID scheme is reconciled with any repo-wide convention or logged in `docs/registers/DRIFT_REGISTER.md`;
- the `GENERATED_RECEIPT.json` planned in Section 2 is wired into CI;
- future changes follow the operating contract's §37 lifecycle.

---

## Related docs

- `docs/domains/archaeology/README.md` — archaeology lane landing page (`PROPOSED`)
- `docs/domains/archaeology/sensitivity-and-publication-posture.md` — sibling sensitivity doc (`PROPOSED`)
- `docs/domains/archaeology/pipeline-shape.md` — sibling lifecycle doc (`PROPOSED`)
- `docs/domains/archaeology/source-families.md` — sibling source doc (`PROPOSED`)
- `docs/registers/VERIFICATION_BACKLOG.md` — repo-wide backlog register (`PROPOSED`)
- `ai-build-operating-contract.md` — verification threshold, §23.2 matrix (canonical)

**Last updated:** 2026-05-28 · `CONTRACT_VERSION = "3.0.0"`

[↑ Back to top](#top)
