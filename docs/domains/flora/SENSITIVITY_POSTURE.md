<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/flora-sensitivity-posture
title: Flora — Sensitivity Posture
type: standard
version: v1
status: draft
owners: Domain steward (Flora); Docs steward
created: 2026-06-03
updated: 2026-06-03
policy_label: public
related: [docs/domains/flora/SENSITIVITY.md, docs/domains/flora/SENSITIVITY_POLICY.md, docs/domains/flora/RIGHTS_AND_SENSITIVITY.md, docs/domains/flora/PUBLICATION_AND_ROLLBACK.md, docs/doctrine/ai-build-operating-contract.md, policy/sensitivity/flora/]
tags: [kfm]
notes: [Doctrine-adjacent stance statement; pins CONTRACT_VERSION = "3.0.0". ROLE — a short, public-facing statement of the Flora lane's sensitivity stance, suitable to quote. It is NOT the doctrine (see SENSITIVITY.md) and NOT the rules (see policy/sensitivity/flora/). Carries no tier tables, transform vocabulary, or rule index by design. Disposition defers to operating contract §23.2.]
[/KFM_META_BLOCK_V2] -->

# 🌿 Flora — Sensitivity Posture

> A plain-language statement of how the Kansas Frontier Matrix treats sensitive plant information. The short version: **rare plants are protected by default, and the safest accurate representation is the one we publish.**

<a id="top"></a>

![status](https://img.shields.io/badge/status-draft-yellow)
![role](https://img.shields.io/badge/role-stance--statement-0969da)
![default](https://img.shields.io/badge/default-deny--by--default-critical)
![contract](https://img.shields.io/badge/CONTRACT__VERSION-3.0.0-informational)
![lane](https://img.shields.io/badge/domain-flora-2ea44f)

**Status:** `draft` · **Owners:** Domain steward (Flora) · Docs steward · **Last updated:** 2026-06-03 · **Contract:** `CONTRACT_VERSION = "3.0.0"`

> [!NOTE]
> **This is a stance statement, not a rulebook.** It states *what we stand for* on sensitive flora in language anyone can read and quote. The operational doctrine (tiers, transforms, receipts) lives in [`SENSITIVITY.md`](./SENSITIVITY.md); the enforcement rules live in [`policy/sensitivity/flora/`](#where-this-is-enforced). Where this statement and the doctrine ever differ, the doctrine and the rules govern.

---

## The posture, in one paragraph

The Flora lane of the Kansas Frontier Matrix exists to make plant knowledge **useful and trustworthy** without putting rare, protected, or culturally significant plants at risk. Exact locations of sensitive plants are **withheld from public surfaces by default.** When we can share something safely, we share a **generalized version** — a region, a grid cell, a range — and we record exactly how and why we transformed it. When we cannot share something safely, we say so plainly rather than hiding it silently. Good data is never a reason to expose a plant that should be protected.

---

## What we stand for

1. **Protection is the default, not the exception.** A rare, protected, or culturally sensitive plant location starts *closed*. Opening it — even to a generalized form — is a deliberate, reviewed, recorded act, never an accident of publishing.

2. **The safest accurate representation wins.** We publish the most useful view that is still safe — typically a generalized or aggregated one — rather than the most precise view the data happens to contain.

3. **Source quality is not a license to expose.** A perfectly sourced, rights-clean rare-plant record can still be unpublishable at exact precision. Sensitivity is decided on the *risk of the result*, not the quality of the input.

4. **Silence is not an answer.** When we deny or generalize, we show *that* we did and *why* — a visible reason, never an empty result that hides a decision.

5. **Culturally significant plants are governed with their communities, not around them.** Tribally important, ceremonial, or steward-governed taxa are handled under CARE and sovereignty principles, with the relevant rights-holders, not by us alone.

6. **Every protective transform leaves a record.** When we generalize, suppress, or withhold geometry, we emit a receipt that documents the change — so the protection is auditable and reversible.

7. **Restriction is always available, instantly.** If rights change, harm potential emerges, or a record is reclassified, anything we have published can be pulled back to fully protected with a single correction — restriction is never harder than exposure.

---

## What this means in practice

| If you are… | …here is what the posture means for you |
|---|---|
| A member of the public | You will see generalized ranges and safe summaries for sensitive plants, not pinpoint locations — and a clear note when something is withheld. |
| A researcher or steward | Exact locations may be available to you through reviewed, authorized surfaces — never through the public map. |
| A rights-holder or tribal partner | Culturally significant plant information is governed with your involvement, under CARE and sovereignty principles. |
| A contributor or reviewer | "Deny by default" is the starting point for every sensitive Flora record; moving anything toward public requires a transform, a review, and a receipt. |

> [!CAUTION]
> This statement does not grant any exception. No exact rare-plant location is published on a public surface on the strength of this document. Disposition is decided by the operating contract §23.2 matrix and the rules under `policy/sensitivity/flora/`.

---

## Where this is enforced

This posture is **stated** here, **specified** in doctrine, and **enforced** in policy — three distinct layers.

| Layer | Where | Owns |
|---|---|---|
| **Stance** (this doc) | `docs/domains/flora/SENSITIVITY_POSTURE.md` | The plain-language statement you can quote. |
| **Doctrine** | [`docs/domains/flora/SENSITIVITY.md`](./SENSITIVITY.md) | Tiers (T0–T4), geoprivacy transforms, the `RedactionReceipt`, CARE/sovereignty, transitions. |
| **Enforcement** | [`policy/sensitivity/flora/`](#related-docs) (described in [`SENSITIVITY_POLICY.md`](./SENSITIVITY_POLICY.md)) | The allow/deny rules that make the posture real. |
| **Canonical disposition** | Operating contract §23.2 | The decision matrix this lane defers to. |

> [!IMPORTANT]
> If this stance statement, the doctrine, and the rules ever disagree, the order of authority is: **rules → doctrine → this statement.** This document is the friendliest layer and the *least* authoritative; it must never be read as overriding `SENSITIVITY.md` or `policy/`. *(Conforms to operating contract §19: avoid parallel authorities; Directory Rules §6.5: `policy/` decides.)*

---

## Truth & status

- The **deny-by-default stance** for rare, protected, and culturally sensitive flora is CONFIRMED doctrine. *(Atlas, Flora §I; §20.5 deny register; operating contract §23.2.)*
- The **tier values, transform vocabulary, and rule paths** referenced indirectly here are PROPOSED pending ADRs (`ADR-S-05` tiers; transform-vocabulary ADR) and mounted-repo verification. This statement intentionally carries none of them.
- This document is a **stance statement**; it is the least authoritative of the Flora sensitivity documents and is superseded by the doctrine and the rules on any conflict.

---

## Changelog v0 → v1

| Change | Type (per contract §37) | Reason |
|---|---|---|
| Initial Flora sensitivity posture statement | new | Plain-language, quotable stance — the one layer the operational docs did not carry. |
| Deliberately carries no tiers, transforms, or rules | clarification | Stance only; doctrine routes to `SENSITIVITY.md`, rules to `policy/`. |
| States the authority order (rules → doctrine → statement) | clarification | Prevents this friendly layer from being read as overriding doctrine. |
| Pinned `CONTRACT_VERSION = "3.0.0"` | housekeeping | Doctrine-adjacent doc requirement. |

> **Backward compatibility.** New doc; no prior anchors to break. This statement is expected to survive the broader Flora sensitivity-doc reconciliation (`OQ-FLORA-SENS-01`) because it occupies a distinct, non-operational layer — but its "Doctrine" pointer must be re-aimed at whichever doc becomes canonical.

## Definition of done

This document is done enough to enter the repository when:

- it is placed according to Directory Rules (`docs/domains/flora/`);
- the Flora domain steward and docs steward review it;
- it carries **no** tier tables, transform vocabulary, or rule logic (those stay in `SENSITIVITY.md` and `policy/`);
- it states the authority order and defers to §23.2;
- the broader sensitivity-doc overlap is logged in `docs/registers/DRIFT_REGISTER.md`;
- the `GENERATED_RECEIPT.json` planned in the authoring notes is wired into CI.

---

## Related docs

- [`docs/domains/flora/SENSITIVITY.md`](./SENSITIVITY.md) — the **doctrine** behind this stance (tiers, geoprivacy, CARE)
- [`docs/domains/flora/SENSITIVITY_POLICY.md`](./SENSITIVITY_POLICY.md) — the **enforcement** companion (rules, `PolicyDecision`, reason codes)
- [`docs/domains/flora/RIGHTS_AND_SENSITIVITY.md`](./RIGHTS_AND_SENSITIVITY.md) — rights + sensitivity doctrine *(overlap tracked in `OQ-FLORA-SENS-01`)*
- [`docs/domains/flora/PUBLICATION_AND_ROLLBACK.md`](./PUBLICATION_AND_ROLLBACK.md) — how protected content is released, corrected, and rolled back
- [`docs/doctrine/ai-build-operating-contract.md`](../../doctrine/ai-build-operating-contract.md) — operating law; §23.2 sensitive-domain matrix (`CONTRACT_VERSION = "3.0.0"`)
- `policy/sensitivity/flora/` — the Flora sensitivity rules *(PROPOSED / TODO)*

_Last updated: 2026-06-03 · `CONTRACT_VERSION = "3.0.0"`_

[↑ Back to top](#top)
