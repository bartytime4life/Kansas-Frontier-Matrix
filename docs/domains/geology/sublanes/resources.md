<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-domains-geology-sublanes-resources
title: Geology Sublane — Resources (pointer / alias)
type: domain-sublane-pointer
version: v0.1
status: draft
owners: <Geology domain steward — TODO confirm>; <docs steward — TODO confirm>
created: 2026-06-03
updated: 2026-06-03
policy_label: restricted
related:
  - docs/domains/geology/sublanes/natural_resources.md   # CANONICAL home for this scope
  - docs/domains/geology/README.md                       # PROPOSED — verify exists
  - directory-rules.md                                    # §2.4 (parallel-home ADR), §12, §13 (drift)
  - ai-build-operating-contract.md                        # canonical operating contract
  - docs/registers/DRIFT_REGISTER.md                      # duplicate-authority routing
tags: [kfm, domain, geology, resources, natural-resources, pointer, alias]
notes:
  - "CONTRACT_VERSION = 3.0.0 pinned per ai-build-operating-contract.md."
  - "INTENTIONALLY A POINTER, NOT A PARALLEL AUTHORITY DOC. The Atlas Ch. 10 is 'Geology and Natural Resources'; the resource object families (Mineral Occurrence, Resource Deposit, ResourceEstimate, Extraction Site, Reclamation Record) are governed by natural_resources.md. A second full doc for the same scope would create a duplicate-authority / parallel-home condition that Directory Rules §2.4 and §13 prohibit without an ADR."
  - "Prior geology sublane docs (bedrock_geology.md, boreholes-wells.md, geochemistry.md, geophysics.md) referenced a sibling 'resources.md'. That reference and the existing 'natural_resources.md' are the SAME scope under two filenames. Reconcile to ONE canonical filename via ADR — see OQ-GEOL-RES-01."
  - "The docs/domains/<domain>/sublanes/<sublane>.md path is PROPOSED; Directory Rules §12 does not enumerate a sublanes/ subfolder. Resolve via ADR."
[/KFM_META_BLOCK_V2] -->

# ♻️ Geology Sublane — Resources

> **This is a pointer, not a second authority doc.** The resource-focused half of the Geology lane — minerals, oil and gas, extraction, reclamation, and resource estimates — is governed by a single canonical sublane doc: **[`natural_resources.md`](./natural_resources.md)**. This file exists to (a) catch the `resources.md` filename that the sibling sublanes reference, and (b) surface the duplicate-authority question for ADR resolution. It deliberately does **not** restate the scope, object families, sources, tiers, or pipeline.

[![status: draft](https://img.shields.io/badge/status-draft-orange)](#)
[![type: pointer](https://img.shields.io/badge/type-pointer%20%2F%20alias-lightgrey)](#)
[![authority: defers to natural_resources.md](https://img.shields.io/badge/authority-defers%20to%20natural__resources.md-blue)](#)
[![CONTRACT_VERSION: 3.0.0](https://img.shields.io/badge/CONTRACT__VERSION-3.0.0-blueviolet)](#)
[![collision: duplicate-authority — ADR pending](https://img.shields.io/badge/collision-duplicate--authority%20%C2%B7%20ADR%20pending-red)](#)
[![last updated: 2026-06-03](https://img.shields.io/badge/last%20updated-2026--06--03-lightgrey)](#)

**Status:** draft · **Canonical doc:** [`natural_resources.md`](./natural_resources.md) · **Contract:** `CONTRACT_VERSION = "3.0.0"` · **Last updated:** 2026-06-03

> [!CAUTION]
> **Duplicate-authority condition — do not split governance.** The Atlas chapter is **"Geology and Natural Resources"** (Ch. 10). Its resource object families — `Mineral Occurrence`, `Resource Deposit`, `ResourceEstimate`, `Extraction Site`, `Reclamation Record` — are already governed by [`natural_resources.md`](./natural_resources.md). Authoring a second full doc here would create a **parallel home** for one scope, which Directory Rules **§2.4** (parallel homes require an ADR) and **§13** (drift prevention) prohibit, and which the operating contract's anti-pattern rules flag as a governance failure. This file therefore stays a pointer until an ADR picks the canonical filename. See [§3 — Open Questions](#3--open-questions).

---

## 1 · Why this file is a pointer

Across the geology sublane suite, prior docs (`bedrock_geology.md`, `boreholes-wells.md`, `geochemistry.md`, `geophysics.md`) listed a sibling **`resources.md`** in their exclusions and related-docs sections. Separately, a full sublane doc already exists at **`natural_resources.md`** covering exactly that scope.

These are **one responsibility under two filenames**, not two responsibilities:

| Concern | Where it actually lives |
|---|---|
| Scope, one-line purpose, exclusions | [`natural_resources.md`](./natural_resources.md) §1, §3, §4 |
| Object families (`Mineral Occurrence`, `Resource Deposit`, `ResourceEstimate`, `Extraction Site`, `Reclamation Record`) | [`natural_resources.md`](./natural_resources.md) §6, §8 |
| Source families & source roles (KGS oil&gas, KCC, MRDS, reclamation programs) | [`natural_resources.md`](./natural_resources.md) §7 |
| Source-role anti-collapse discipline | [`natural_resources.md`](./natural_resources.md) §13 |
| Sensitivity, rights, T0–T4 tiers, deny-by-default classes | [`natural_resources.md`](./natural_resources.md) §12 |
| Pipeline (RAW → PUBLISHED), validators, governed AI | [`natural_resources.md`](./natural_resources.md) §11, §14, §15 |

> [!IMPORTANT]
> **Do not copy that content here.** Per the operating contract's change discipline and Directory Rules §13, duplicating governance text creates two sources that will drift. If `resources.md` is chosen as the canonical filename, the resolution is to **rename / move** `natural_resources.md` to this path (one governed move with a migration note), **not** to maintain two docs.

[Back to top ↑](#-geology-sublane--resources)

---

## 2 · Resolution options (for the ADR)

PROPOSED — to be decided by an ADR, not by this file. Each option keeps exactly **one** canonical doc.

| Option | Action | Trade-off |
|---|---|---|
| **A — keep `natural_resources.md`** | This `resources.md` stays a permanent pointer (or is deleted); sibling docs update their `resources.md` references to `natural_resources.md`. | Matches the Atlas chapter name ("…and Natural Resources"); requires editing sibling references. |
| **B — adopt `resources.md`** | Rename `natural_resources.md` → `resources.md` via a governed move + migration note; delete this pointer. | Matches the shorter sibling-doc references; loses the explicit "natural resources" framing; requires anchor/link fix-ups. |
| **C — both as distinct sublanes** | Split into a narrow `resources.md` (commercial/economic resource layer) and `natural_resources.md` (broad). | **Not supported by current doctrine** — the Atlas treats these as one chapter; would need an ADR establishing two bounded sub-scopes and is the most drift-prone. |

> [!NOTE]
> Options A and B are housekeeping renames. Option C is a doctrine change and should be treated as such (new bounded contexts, new object-ownership split). Absent evidence that the project wants two distinct resource sub-scopes, **A is the lowest-risk default**.

[Back to top ↑](#-geology-sublane--resources)

---

## 3 · Open Questions

| # | Question | Evidence that would settle it | Status |
|---|---|---|---|
| 1 | Which filename is canonical for the resource sublane — `resources.md` or `natural_resources.md`? | An ADR selecting one; mounted-repo precedent. | NEEDS VERIFICATION |
| 2 | Do the sibling docs' `resources.md` references need updating to the canonical name? | Resolution of #1; sibling-doc sweep. | NEEDS VERIFICATION |
| 3 | Is there any project intent to split a narrow "resources" scope from "natural resources" (Option C)? | An ADR establishing two bounded sub-scopes; otherwise treat as one. | UNKNOWN |
| 4 | Is `docs/domains/<domain>/sublanes/<sublane>.md` an accepted layout at all? | ADR amending Directory Rules §12; mounted-repo precedent. | NEEDS VERIFICATION |

[Back to top ↑](#-geology-sublane--resources)

---

## Open questions register

| ID | Question | Owner role | Resolution path |
|---|---|---|---|
| OQ-GEOL-RES-01 | Canonical filename for the resource sublane (`resources.md` vs `natural_resources.md`). | docs steward + geology domain steward | ADR + DRIFT_REGISTER entry; one governed rename, not two docs. |
| OQ-GEOL-RES-02 | Update sibling-doc references after the rename. | docs steward | Sibling-doc sweep once OQ-GEOL-RES-01 resolves. |
| OQ-GEOL-RES-03 | Whether to split a narrow "resources" sub-scope (Option C). | geology domain steward | Doctrine ADR establishing bounded sub-scopes, or close as "one chapter". |
| OQ-GEOL-RES-04 | Accept `sublanes/` subfolder vs flat-prefix scheme. | docs steward + directory-rules owner | ADR amending Directory Rules §12. |

## Open verification backlog

These items remain `NEEDS VERIFICATION` before this pointer (or its replacement) is finalized:

1. Canonical filename decision (`resources.md` vs `natural_resources.md`).
2. Sibling-doc reference updates after the rename.
3. Whether a distinct narrow "resources" scope exists in project intent.
4. `sublanes/` folder layout vs flat-prefix scheme (Directory Rules §12 silent).

## Changelog v0 → v0.1

| Change | Type (per contract §37) | Reason |
|---|---|---|
| Created `resources.md` as a pointer to `natural_resources.md` | new | Catch the `resources.md` filename referenced by sibling docs without creating a parallel authority doc. |
| Surfaced duplicate-authority collision and routed to DRIFT_REGISTER | new | Directory Rules §2.4/§13 prohibit parallel homes without an ADR. |
| Listed A/B/C resolution options for an ADR | new | Give the steward a decision frame; default to A (keep `natural_resources.md`). |

> **Backward compatibility.** This file adds no governance of its own; if the ADR renames `natural_resources.md` to `resources.md`, this pointer is deleted and inbound `resources.md` references resolve to the canonical doc directly.

## Definition of done

This pointer is resolved when:

- an ADR selects the canonical filename (OQ-GEOL-RES-01);
- the non-canonical filename is either deleted or kept as a permanent, clearly labeled pointer;
- sibling geology sublane docs reference the canonical filename (OQ-GEOL-RES-02);
- the `sublanes/` folder question (OQ-GEOL-RES-04) is resolved;
- the collision and rename are logged in `docs/registers/DRIFT_REGISTER.md`;
- no two docs claim governance over the same resource object families.

[Back to top ↑](#-geology-sublane--resources)

---

## Related Docs

- **[`natural_resources.md`](./natural_resources.md)** — **canonical** resource sublane doc (scope, objects, sources, tiers, pipeline, AI).
- `./bedrock_geology.md` — sibling sublane (bedrock / stratigraphy / structures).
- `./boreholes-wells.md` — sibling sublane (shared subsurface objects).
- `./geochemistry.md` — sibling sublane (assay ≠ deposit).
- `./geophysics.md` — sibling sublane (anomaly ≠ deposit).
- `../README.md` — Geology domain landing *(PROPOSED — verify exists)*.
- `directory-rules.md` — §2.4 (parallel-home ADR), §12 (Domain Placement Law), §13 (drift prevention).
- `ai-build-operating-contract.md` — canonical operating contract (`CONTRACT_VERSION = "3.0.0"`).
- `docs/registers/DRIFT_REGISTER.md` — duplicate-authority + filename routing.

---

**Last updated:** 2026-06-03 · **Doc status:** draft (pointer) · **Canonical doc:** `natural_resources.md` · **Contract:** `CONTRACT_VERSION = "3.0.0"` · [Back to top ↑](#-geology-sublane--resources)
