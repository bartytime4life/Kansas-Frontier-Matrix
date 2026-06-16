<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://policy/domains/archaeology/sensitivity
title: Archaeology Sensitivity Policy README
type: policy-readme
version: v0.1
status: draft
owners: OWNER_TBD — Archaeology steward · Sensitivity reviewer · Rights-holder representative · Release authority · Policy steward · Docs steward
created: 2026-06-15
updated: 2026-06-15
policy_label: restricted
related:
  - ../README.md
  - ../../../../docs/domains/archaeology/SENSITIVITY.md
  - ../../../../docs/domains/archaeology/PUBLICATION_AND_POLICY.md
  - ../../../../docs/domains/archaeology/PRESERVATION_MATRIX.md
  - ../../../../docs/domains/archaeology/CULTURAL_REVIEW.md
  - ../../../../docs/runbooks/archaeology/PROMOTION_RUNBOOK.md
  - ../../../../policy/sensitivity/archaeology/
  - ../../../../policy/consent/archaeology/
  - ../../../../policy/release/archaeology/
  - ../../../../schemas/contracts/v1/receipts/redaction_receipt.schema.json
  - ../../../../schemas/contracts/v1/governance/review_record.schema.json
  - ../../../../contracts/governance/review_record.md
  - ../../../../tests/domains/archaeology/
  - ../../../../fixtures/domains/archaeology/
tags: [kfm, policy, domains, archaeology, sensitivity, deny-by-default, redaction, generalization, sovereignty, CARE, fail-closed]
notes:
  - "Initial README for the Archaeology sensitivity policy sublane."
  - "This lane is for policy checks that decide sensitivity tier/rank, redaction/generalization obligations, review requirements, and public-surface admissibility."
  - "This lane is not the sensitivity doctrine document, redaction-profile store, schema home, release authority, lifecycle data store, or receipt/proof store."
  - "Concrete policy files, bundle syntax, fixtures, tests, redaction profile manifests, CI binding, and runtime enforcement remain NEEDS VERIFICATION."
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

<div align="center">

# Archaeology Sensitivity Policy

`policy/domains/archaeology/sensitivity/`

**Policy sublane for Archaeology sensitivity gates: deny-by-default tier/rank handling, redaction and generalization obligations, sovereignty-aware review requirements, and public-surface safety checks.**

![status](https://img.shields.io/badge/status-draft-blue)
![owner](https://img.shields.io/badge/owner-OWNER__TBD-lightgrey)
![domain](https://img.shields.io/badge/domain-archaeology-6E4C1E)
![truth](https://img.shields.io/badge/truth-NEEDS__VERIFICATION-yellow)
![default](https://img.shields.io/badge/default-DENY__sensitive__exact-d62728)

[Scope](#1-scope) · [Repo fit](#2-repo-fit) · [Boundary](#3-authority-boundary) · [Inputs](#5-inputs) · [Exclusions](#6-exclusions) · [Sensitivity gates](#7-sensitivity-gates) · [Definition of done](#14-definition-of-done)

</div>

---

> [!IMPORTANT]
> **Status:** draft / `NEEDS VERIFICATION`  
> **Owners:** `OWNER_TBD` — Archaeology steward · Sensitivity reviewer · Rights-holder representative · Release authority · Policy steward · Docs steward  
> **Path:** `policy/domains/archaeology/sensitivity/README.md`  
> **Responsibility root:** `policy/` — policy-as-code and policy documentation  
> **Truth posture:** CONFIRMED file path / PROPOSED Archaeology sensitivity-policy sublane / UNKNOWN runtime enforcement

> [!CAUTION]
> Archaeology sensitivity policy must fail closed for exact site geometry, human remains, sacred sites, collection-security detail, looting-risk exposure, restricted cultural knowledge, and unresolved sovereignty or consent state. A transformation is not public-safe unless it is named, reviewed, receipt-backed, and release-authorized.

---

## Quick jump

- [1. Scope](#1-scope)
- [2. Repo fit](#2-repo-fit)
- [3. Authority boundary](#3-authority-boundary)
- [4. Default posture](#4-default-posture)
- [5. Inputs](#5-inputs)
- [6. Exclusions](#6-exclusions)
- [7. Sensitivity gates](#7-sensitivity-gates)
- [8. Diagram](#8-diagram)
- [9. Decision vocabulary](#9-decision-vocabulary)
- [10. Sensitivity obligations](#10-sensitivity-obligations)
- [11. Sensitivity-record expectations](#11-sensitivity-record-expectations)
- [12. Inspection path](#12-inspection-path)
- [13. Validation expectations](#13-validation-expectations)
- [14. Definition of done](#14-definition-of-done)
- [15. Open verification items](#15-open-verification-items)

---

## 1. Scope

`policy/domains/archaeology/sensitivity/` is a proposed policy sublane for Archaeology sensitivity decisions.

It should describe and eventually bind policy checks that decide whether an Archaeology object, artifact, candidate feature, site-related record, oral-history record, 3D or remote-sensing derivative, map layer, Evidence Drawer payload, or Focus Mode response is too sensitive for the requested audience or must be denied, held, redacted, generalized, delayed, or restricted.

In scope:

- audience-tier and per-record sensitivity-rank checks
- deny-by-default handling for exact sensitive archaeology detail
- redaction and generalization obligations
- sovereignty, CARE, rights-holder, consent, revocation, and embargo sensitivity inputs
- public-surface admissibility gates
- receipt and review prerequisites for bounded outputs
- finite policy outcomes and safe reason codes

Out of scope:

- sensitivity doctrine prose
- redaction-profile values not accepted by policy owner and tests
- raw site/source data or precise protected locations
- release approval itself
- schema definitions and semantic contracts
- public UI or API implementation
- receipt/proof storage
- cultural-knowledge interpretation

[Back to top](#top)

---

## 2. Repo fit

| Concern | Owning root | Expected relationship |
|---|---|---|
| Archaeology sensitivity policy | `policy/domains/archaeology/sensitivity/` | This README and future sensitivity policy files, if accepted |
| Archaeology policy parent | `policy/domains/archaeology/` | Domain policy boundary and shared Archaeology obligations |
| Sensitivity doctrine | `docs/domains/archaeology/SENSITIVITY.md` | Human-facing sensitivity catalogue; not executable policy bundle |
| Publication doctrine | `docs/domains/archaeology/PUBLICATION_AND_POLICY.md` | Trust-membrane and release governance reference |
| Cultural review doctrine | `docs/domains/archaeology/CULTURAL_REVIEW.md` | Human-facing review and sovereignty protocol |
| Cross-cutting sensitivity lane | `policy/sensitivity/archaeology/` | Proposed deny lane; relationship remains `NEEDS VERIFICATION` |
| Redaction receipts | `schemas/contracts/v1/receipts/`, `data/receipts/`, or verified homes | Schema and storage remain separate |
| Release authority | `release/` | Publication, correction, supersession, and rollback authority |
| Tests and fixtures | `tests/domains/archaeology/`, `fixtures/domains/archaeology/` | Enforceability proof; presence remains `NEEDS VERIFICATION` |

## 3. Authority boundary

This lane may decide sensitivity policy outcomes and obligations. It must not become the doctrine source, redaction-profile registry unless accepted, schema home, receipt store, lifecycle store, release authority, or public serving code.

```text
policy/domains/archaeology/sensitivity/ = sensitivity policy gates
policy/domains/archaeology/             = parent Archaeology policy lane
policy/sensitivity/archaeology/         = proposed cross-cutting sensitivity deny lane
docs/domains/archaeology/SENSITIVITY.md = sensitivity doctrine and catalogue
schemas/contracts/v1/receipts/          = receipt machine shapes, if accepted
data/                                   = lifecycle artifacts, receipts, proofs, restricted records
release/                                = publication, correction, rollback control
```

## 4. Default posture

Sensitivity policy should deny or hold when support is missing.

A sensitivity gate should not pass when any of these are unresolved:

- requested audience tier
- per-record sensitivity rank
- exact geometry or location exposure risk
- human-remains, sacred-site, collection-security, looting-risk, or cultural-knowledge flags
- sovereignty label, CARE obligations, rights-holder review, consent, revocation, or embargo state
- redaction/generalization profile name and version
- RedactionReceipt or equivalent transform receipt
- EvidenceBundle support
- release state, rollback target, and correction path
- public-surface route and trust membrane status

## 5. Inputs

| Input family | Examples | Required posture |
|---|---|---|
| Sensitivity classification | audience tier, per-record rank, object class, sensitive flags | Explicit or default to deny/hold |
| Geometry / precision context | exact, generalized, redacted, withheld, aggregated, public-safe candidate | Exact protected detail must fail closed |
| Transform context | redaction profile, generalization profile, transform receipt, profile version | Named, versioned, and receipt-backed |
| Sovereignty / CARE context | steward org, authority_to_control, obligations, benefit commitments, labels | Required where cultural authority applies |
| Consent / revocation context | consent receipt, revocation manifest, embargo, retention condition | Checked as live input |
| Evidence context | EvidenceRef, EvidenceBundle status, citation validation | Required for claim-bearing output |
| Release context | candidate, released, superseded, withdrawn, rollback requested | Explicit; never inferred from path alone |
| Audit context | PolicyDecision, reason code, obligation set, reviewer refs, receipt refs | Required for consequential decisions |

## 6. Exclusions

| Does not belong here | Correct home |
|---|---|
| Sensitivity doctrine prose | `docs/domains/archaeology/SENSITIVITY.md` |
| Cultural review protocol prose | `docs/domains/archaeology/CULTURAL_REVIEW.md` |
| RedactionReceipt schemas | `schemas/contracts/v1/receipts/` or accepted schema home |
| Stored RedactionReceipts, proofs, and lifecycle artifacts | `data/` lifecycle roots or verified receipt/proof homes |
| Release manifests and rollback cards | `release/` |
| Raw precise locations or restricted source material | governed restricted lifecycle stores only |
| Public UI or API implementation | `apps/` and governed UI/API packages |
| Cultural-knowledge interpretation | Named authority / review process, not KFM policy docs |

## 7. Sensitivity gates

| Gate | Policy question | Default posture |
|---|---|---|
| `classify_sensitivity` | Is the audience tier and per-record rank known? | Hold or deny when unknown |
| `exact_detail_check` | Does the payload contain exact sensitive archaeology detail? | Deny public exposure |
| `redaction_profile_check` | Is a named, versioned transform profile present? | Hold when missing |
| `receipt_check` | Is the redaction/generalization receipt present and linked? | Hold when missing |
| `sovereignty_care_check` | Are sovereignty and CARE obligations preserved? | Hold or restrict when unresolved |
| `consent_revocation_check` | Is consent valid and not revoked or embargoed? | Deny or hold when invalid |
| `public_surface_check` | Is output public-safe and release-authorized? | Hold or deny without release/rollback support |

## 8. Diagram

```mermaid
flowchart TD
    req["Archaeology sensitivity-gated action"] --> class{"Tier/rank known?"}
    class -->|no| hold0["HOLD / DENY"]
    class -->|yes| exact{"Exact protected detail?"}
    exact -->|yes| transform{"Named transform + receipt?"}
    exact -->|no| care{"CARE / consent / sovereignty clear?"}
    transform -->|no| deny["DENY exact public exposure"]
    transform -->|yes| care
    care -->|no| hold1["HOLD / RESTRICT / DENY"]
    care -->|yes| release{"Release + rollback support?"}
    release -->|no| hold2["HOLD"]
    release -->|yes| allow["ALLOW / RESTRICT bounded output"]

    allow --> audit["PolicyDecision + receipt refs"]
    deny --> audit
    hold0 --> audit
    hold1 --> audit
    hold2 --> audit
```

## 9. Decision vocabulary

| Decision | Meaning | Required behavior |
|---|---|---|
| `ALLOW` | Sensitivity checks pass for the scoped action | Scope to audience, object, transform, release, and version |
| `DENY` | Sensitive detail cannot be exposed or transformed safely for the request | Do not reveal protected detail or exact locations |
| `RESTRICT` | Output may proceed only with redaction, generalization, audience restriction, embargo, or review limits | Preserve obligations downstream |
| `HOLD` | Required classification, transform, receipt, review, consent, or release support is missing | Do not promote or render publicly |
| `ABSTAIN` | Policy cannot decide because evidence, source, rights, or sensitivity support is unresolved | Preserve unresolved handles where safe |
| `ERROR` | Policy machinery, schema, runtime, or repository support failed | Fail closed and record failure |

## 10. Sensitivity obligations

| Obligation | Example effect |
|---|---|
| `deny_exact_detail` | Block exact protected detail from public or broad-audience surfaces |
| `redaction_required` | Withhold protected fields, geometry, relations, or cultural detail |
| `generalization_required` | Reduce spatial, temporal, or attribute precision using an accepted profile |
| `redaction_receipt_required` | Record profile, reason, version, and digest without leaking protected detail |
| `sensitivity_review_required` | Route to sensitivity reviewer before bounded output |
| `sovereignty_review_required` | Route sovereignty-bearing material to the named authority process |
| `consent_check_required` | Check consent, revocation, embargo, and retention state |
| `restricted_audience_required` | Limit material to steward, reviewer, rights-holder, or authenticated surface |
| `rollback_required` | Require rollback target before public-impacting release |

## 11. Sensitivity-record expectations

A future sensitivity policy record or policy input should identify:

- object family and request audience;
- sensitivity tier and per-record rank;
- sensitive flags and precision class;
- transform profile name and version;
- receipt references and digest closure;
- CARE and sovereignty labels;
- consent, revocation, embargo, and retention state;
- evidence and source-role support;
- review status and reviewer roles;
- policy outcome, reason code, and obligations;
- release, rollback, correction, or supersession implications.

## 12. Inspection path

Concrete sensitivity policy files, profiles, manifests, fixtures, tests, validators, and CI remain `NEEDS VERIFICATION`.

```bash
find policy/domains/archaeology/sensitivity -maxdepth 4 -type f | sort
find docs/domains/archaeology policy/sensitivity schemas/contracts/v1 data release -maxdepth 5 -type f 2>/dev/null | grep -Ei 'sensitivity|redaction|generalization|receipt|care|sovereignty|release' | sort
find tests/domains/archaeology fixtures/domains/archaeology -maxdepth 5 -type f 2>/dev/null | grep -Ei 'sensitivity|redaction|deny|generalization|care|sovereignty' | sort
```

## 13. Validation expectations

Useful validation for this lane should cover:

- unknown sensitivity tier or rank returns `HOLD` or `DENY`;
- exact sensitive archaeology detail returns `DENY` for public or broad-audience use;
- missing redaction/generalization profile returns `HOLD`;
- missing RedactionReceipt returns `HOLD`;
- revoked or out-of-scope consent returns `DENY` or `HOLD`;
- sovereignty or CARE obligations survive downstream transforms;
- public surfaces cannot show protected detail just because a transform exists;
- policy decisions emit safe reason codes and receipt-ready metadata.

## 14. Definition of done

- [ ] Owners are confirmed and `OWNER_TBD` is replaced.
- [ ] Sensitivity policy files and bundle structure are inventoried.
- [ ] Runtime policy language and bundle location are confirmed.
- [ ] Sensitivity tier/rank input shape is linked to accepted schemas or contracts.
- [ ] Redaction/generalization profile home is accepted.
- [ ] RedactionReceipt and review-record schemas/contracts are linked.
- [ ] Fixtures cover allow, deny, restrict, hold, abstain, and error outcomes.
- [ ] CARE, sovereignty, consent, revocation, and release obligations are tested.
- [ ] Public API bypass checks are covered by tests or policy fixtures.

## 15. Open verification items

| Item | Why it matters |
|---|---|
| Confirm actual child files under `policy/domains/archaeology/sensitivity/` | Prevents stale empty-lane claims |
| Confirm relationship with `policy/sensitivity/archaeology/` | Prevents duplicate deny-lane authority |
| Confirm Rego/OPA or equivalent policy language | Prevents non-runnable guidance |
| Confirm redaction/generalization profile home | Required for deterministic transforms |
| Confirm RedactionReceipt schema and storage homes | Required for auditability |
| Confirm tests and fixtures | Required before enforcement claims |
| Confirm CARE and sovereignty propagation | Required for cultural authority obligations |
| Confirm release-gate integration | Required before publication claims |

<details>
<summary>Appendix A — no-loss preservation note</summary>

The target file was an empty placeholder. This README adds a bounded Archaeology sensitivity-policy sublane without claiming runtime enforcement, policy modules, redaction profile manifests, tests, fixtures, schema coverage, receipt storage, CI coverage, or release-gate integration.

It preserves the Archaeology sensitivity doctrine that exact sensitive details fail closed unless an accepted, reviewed, receipt-backed transform and release path explicitly permits a bounded output.

</details>

## Status summary

`policy/domains/archaeology/sensitivity/` should define Archaeology sensitivity policy only when backed by accepted sensitivity inputs, transform profiles, receipts, fixtures, tests, review records, consent/revocation checks, and release integration.

It should keep sensitivity decisions fail-closed, sovereignty-aware, obligation-preserving, and auditable without becoming the sensitivity doctrine document, schema home, receipt store, lifecycle store, release authority, public API, or cultural-knowledge authority.

<p align="right"><a href="#top">Back to top</a></p>
