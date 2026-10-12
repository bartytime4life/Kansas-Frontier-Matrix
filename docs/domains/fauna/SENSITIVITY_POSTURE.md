<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/docs-domains-fauna-sensitivity-posture
title: Fauna Domain — Sensitivity Posture (Summary)
type: standard
version: v1
status: draft
owners: [NEEDS VERIFICATION — fauna domain steward; sensitivity reviewer; docs steward]
created: 2026-06-02
updated: 2026-06-02
policy_label: public
related:
  - docs/domains/fauna/SENSITIVITY.md
  - docs/domains/fauna/README.md
  - docs/doctrine/ai-build-operating-contract.md
  - policy/sensitivity/fauna/
tags: [kfm, domain, fauna, sensitivity, posture, summary, deny-by-default]
notes:
  # SUMMARY doc. The full posture (tier tables, transforms, transition matrix, separation of duties) lives in SENSITIVITY.md.
  # This file is a fast orientation surface; it is NOT the authority and MUST NOT diverge from SENSITIVITY.md or policy/sensitivity/fauna/.
  # If this summary and SENSITIVITY.md disagree, SENSITIVITY.md wins; if SENSITIVITY.md and policy disagree, policy wins.
  # Contains NO exact coordinates, identifiers, or geoprivacy parameters by design.
  # Doctrine-adjacent doc; CONTRACT_VERSION = "3.0.0" pinned per AI Build Operating Contract v3.0.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# Fauna Domain — Sensitivity Posture (Summary)

> The one-page statement of how the Fauna lane treats sensitive records. This is a **summary and pointer**; the full rules, tier tables, and transition matrix live in [SENSITIVITY.md](./SENSITIVITY.md), and the binding decisions live in `policy/sensitivity/fauna/`.

---

![Status](https://img.shields.io/badge/status-draft-orange)
![Lane](https://img.shields.io/badge/lane-fauna-2ea44f)
![Posture](https://img.shields.io/badge/posture-deny--by--default-critical)
![Authority](https://img.shields.io/badge/authority-summary%20only-lightgrey)
![Full doc](https://img.shields.io/badge/full%20posture-SENSITIVITY.md-blue)
![Contract](https://img.shields.io/badge/CONTRACT__VERSION-3.0.0-blueviolet)

**Status:** draft · **Authority:** summary (defers to [SENSITIVITY.md](./SENSITIVITY.md)) · **Last updated:** 2026-06-02 · **`CONTRACT_VERSION = "3.0.0"`**

> [!IMPORTANT]
> **This is a summary, not the authority.** It exists so a reader can grasp the Fauna sensitivity stance in under a minute. The full posture — tier scheme, deny register, geoprivacy transforms, transition matrix, and separation of duties — is in **[SENSITIVITY.md](./SENSITIVITY.md)**. Binding admissibility rules are in `policy/sensitivity/fauna/`. This file MUST NOT diverge from either; on conflict, **SENSITIVITY.md wins over this summary, and policy wins over SENSITIVITY.md**.

---

## The posture in five lines

1. **Deny-by-default.** Sensitive taxa, nests, dens, roosts, hibernacula, spawning sites, and steward-controlled records **fail closed**. The default answer for exact sensitive geometry is **DENY** or **ABSTAIN**. [DOM-FAUNA] [OPCON §23.2]
2. **Sensitive occurrence = T4.** Exact sensitive-occurrence and sensitive-site geometry default to the **Denied** tier and move to a public tier only via a documented transform plus a recorded review. [ENCY Atlas §24.5.2]
3. **Release is earned, not assumed.** A record can be well-sourced and still unsafe. Public exposure is a governed state — never a reward for data quality. [DOM-FAUNA]
4. **Every release leaves receipts.** A T4 → public motion requires a **RedactionReceipt + ReviewRecord + PolicyDecision**, and the transition is **reversible**. [ENCY Atlas §24.5.3]
5. **No solo approvals on sensitive lanes.** Author ≠ release authority; a sensitivity reviewer (and rights-holder representative where applicable) must sign off. [ENCY Atlas §24.7]

---

## What is denied by default (quick reference)

| Fauna record | Default | Released only via |
|---|---|---|
| Exact sensitive occurrence | **DENY (T4)** | Geoprivacy generalization + RedactionReceipt → T1 |
| Nest / den / roost / hibernacula / spawning site | **DENY (T4)** | Generalization or suppression + RedactionReceipt; steward review |
| Steward-controlled record (tribal / landowner / agency-restricted) | **DENY (T4)** | Rights-holder representative co-sign; rights recorded |
| Re-identifying join of public sources | **DENY (T4)** | Sensitivity-reviewer-approved join rule |
| Range polygon | **T1** | Aggregated / generalized public-safe layer |
| General (non-sensitive) public occurrence | **T0** | Standard release path |

*Full tables, the T0–T4 tier definitions, the transform library, and the transition matrix: see [SENSITIVITY.md](./SENSITIVITY.md) §4–§7.*

---

## When the disposition is unclear

Apply the **most restrictive applicable** row of the Operating Contract §23.2 sensitive-domain matrix, surface the uncertainty, and route to the sensitivity reviewer. Quarantine uncertain source material; do not guess toward release. [OPCON §23.2]

> [!CAUTION]
> This summary deliberately contains **no exact coordinates, identifiers, generalization radii, or fuzzing parameters** — naming those would itself be an exposure aid. Those values live only in `policy/sensitivity/fauna/`. [OPCON §23]

---

## Where to go next

- **Full posture:** [SENSITIVITY.md](./SENSITIVITY.md) — tier scheme, deny register, transforms, transition matrix, separation of duties, failure modes.
- **Binding rules:** `policy/sensitivity/fauna/` *(PROPOSED — authoritative)*.
- **Lane landing page:** [README.md](./README.md).
- **Schema-side reinforcement:** [SCHEMAS.md](./SCHEMAS.md).
- **Sensitive-domain matrix:** [ai-build-operating-contract.md](../../doctrine/ai-build-operating-contract.md) §23.

---

### Footer

**Authoritative companion:** [SENSITIVITY.md](./SENSITIVITY.md) · **Related:** [README.md](./README.md) · [SCHEMAS.md](./SCHEMAS.md) · [policy/sensitivity/fauna/](../../../policy/sensitivity/fauna/)

**Last updated:** 2026-06-02 · **Owners:** _NEEDS VERIFICATION_ · **Status:** draft · **`CONTRACT_VERSION = "3.0.0"`**

[Back to top ↑](#top)
