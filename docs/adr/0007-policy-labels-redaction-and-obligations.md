<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/7180066f-de26-4218-aa89-79336d40e3e0
title: "ADR 0007: Policy Labels, Redaction, and Obligations"
type: adr
version: v1
status: draft
owners: KFM Stewards (TBD)
created: 2026-03-01
updated: 2026-03-01
policy_label: internal
related:
  - docs/adr/README.md
  - docs/policy/
  - docs/security/
tags: [kfm, adr, governance, policy, redaction, obligations]
notes:
  - "Defines the controlled policy_label vocabulary and the obligations/redaction model."
  - "Aligns CI policy fixtures with runtime enforcement (evidence resolver + governed API)."
[/KFM_META_BLOCK_V2] -->

# ADR 0007: Policy Labels, Redaction, and Obligations

![ADR](https://img.shields.io/badge/ADR-0007-blue)
![Status](https://img.shields.io/badge/status-draft-lightgrey)
![Updated](https://img.shields.io/badge/updated-2026--03--01-lightgrey)
![Governance](https://img.shields.io/badge/governance-policy--as--code-informational)

**Purpose:** Define how KFM classifies data access/sensitivity (`policy_label`), performs redaction/generalization, and expresses “you may proceed, but…” requirements via structured **obligations** — consistently across **pipelines → catalogs → governed APIs → UI → Focus Mode**.

> NOTE  
> This ADR is about *labels + obligations semantics and enforcement*. It does **not** choose the identity provider, ABAC details, or org-specific role mapping; those belong in separate ADRs.

---

## Quick navigation

- [Decision](#decision)
- [Context and drivers](#context-and-drivers)
- [Controlled vocabulary: policy_label](#controlled-vocabulary-policy_label)
- [Obligations model](#obligations-model)
- [Redaction and generalization](#redaction-and-generalization)
- [Enforcement architecture](#enforcement-architecture)
- [Policy-safe UX requirements](#policy-safe-ux-requirements)
- [Consequences](#consequences)
- [Implementation checklist](#implementation-checklist)
- [Open questions](#open-questions)

---

## Decision

KFM will:

1. **Adopt a controlled vocabulary** `policy_label` (dataset-version level) to represent access + sensitivity in a stable, testable way.
2. **Express required redactions/generalizations and user-facing requirements** as structured **obligations** produced by the policy engine.
3. **Enforce identical policy semantics in CI and runtime**:
   - CI blocks merges when policy fixtures fail (fail-closed).
   - Runtime services (governed API + evidence resolver) apply allow/deny and obligations before returning anything.
4. **Treat redaction/generalization as a first-class, versioned transform** recorded in provenance (PROV/run receipts) and—when public output is permitted—publish a *separate* public-safe dataset version rather than mutating restricted outputs.

**Status:** Draft (pending steward approval + policy pack implementation).

---

## Context and drivers

KFM’s trust model depends on **policy being enforceable** and **user-visible** without leaking sensitive information.

We need one consistent way to answer:

- “Can this user do this action?” (**decision**)
- “If yes, what must we do or show?” (**obligations**)
- “If no, how do we fail without leaking?” (**policy-safe errors**)

This must hold across:

- Promotion gates (policy is a gate, not a guideline)
- Evidence resolution (citations must resolve and be policy-allowed)
- Map/Story UI and Focus Mode (abstain or narrow scope when evidence is not allowed)

---

## Controlled vocabulary: policy_label

### Scope

- `policy_label` is attached at **DatasetVersion** granularity (and may optionally be echoed on derived artifacts and catalog records).
- `policy_label` is **controlled and versioned** (changes must be reviewed like code).

### Starter set (v1)

| policy_label | Meaning | Default posture | Typical handling |
|---|---|---|---|
| `public` | Safe to show publicly | allow for public read | Full geometry/fields as allowed by license and QA |
| `public_generalized` | Public-safe derivative of sensitive data | allow for public read *with obligations* | Generalized geometry/aggregated attributes; show notice |
| `restricted` | Requires authorization | default deny for public | Not discoverable publicly; no metadata leakage via errors |
| `restricted_sensitive_location` | Precise locations protected | strict deny for public | Precise geometry never public; public output only via approved generalization |
| `internal` | Visible to operators/stewards | deny for public | Not listed in public catalogs |
| `embargoed` | Time-limited restriction pending release | deny unless authorized | Optional scheduled release; audit required |
| `quarantine` | Not promotable yet | deny by default | Used when validation/rights/sensitivity unresolved |

> WARNING  
> `public_generalized` is a *separate* published representation. It is not a switch that “hides a couple fields” at render time. Generalization must be a reproducible transform with provenance.

---

## Obligations model

### What an obligation is

An **obligation** is a structured requirement returned alongside a policy decision, e.g.:

- “Show a notice explaining geometry generalization.”
- “Remove these sensitive fields from an export.”
- “Only return aggregated counts above a threshold.”
- “Do not expose asset download links; allow metadata-only.”

Obligations are:

- **Policy outputs** (computed by PDP)
- **Enforced by PEPs** (CI/runtime/evidence resolver/export pipeline)
- **Visible to users** when appropriate (UI notices; evidence drawer showing “redactions applied”)

### Proposed obligation schema (v1)

This ADR proposes a minimal typed object. Treat it as a contract to stabilize:

```yaml
type: <string>           # required; e.g., show_notice, redact_fields, generalize_geometry
scope: <string>          # optional; e.g., ui, api, export, tiles, evidence
params: <object>         # optional; typed by obligation type
message: <string>        # optional; UI-safe human text
```

#### Proposed obligation types (starter)

| type | Enforced where | Purpose |
|---|---|---|
| `show_notice` | UI / evidence drawer | Communicate policy modifications (“generalized due to policy”) |
| `generalize_geometry` | pipeline + tiles + export | Ensure public output is non-precise (method + parameters) |
| `redact_fields` | API + export + evidence | Remove/blank sensitive attributes |
| `min_count_threshold` | API + export | Prevent re-identification; suppress small counts |
| `deny_asset_links` | evidence resolver | Permit citation metadata without exposing downloads |
| `require_attribution` | export + UI | Auto-attach license/attribution text |

> NOTE  
> Only `show_notice` and “obligations exist as a policy output” are directly documented in current vNext materials; other types above are included as a pragmatic starter set because promotion gate language explicitly expects obligations like “generalize geometry” and “remove fields,” and the UI is required to display “redactions applied.” See “Minimum verification steps” below to validate the exact schema choice.

---

## Redaction and generalization

### Principle: redaction is a transform, not a view-layer trick

- Redaction/generalization must be done as an explicit pipeline activity with:
  - reproducible parameters
  - recorded provenance (PROV/run receipt)
  - a distinct DatasetVersion identity for the public-safe product

### Geometry generalization methods (starter vocabulary)

Use a controlled vocabulary for `geometry.generalization_method`, for example:

- `centroid_only`
- `grid_aggregation_<cell_size>`
- `random_offset_<meters>`
- `dissolve_to_admin_unit`
- `bounding_box_only`
- `none`

(Exact parameterization should be standardized in a dedicated schema.)

### Non-reversibility requirement

For sensitive locations (heritage sites, protected species, etc.):

- The public representation must **not** be trivially reversible (e.g., no hidden precise points; no stable offsets that can be averaged out).
- Tile delivery must be policy-enforced (no static hosting that bypasses checks).

---

## Enforcement architecture

### Policy-as-code invariants

- **Same policy semantics in CI and runtime**. CI assurances are meaningless if runtime differs.
- Policy is evaluated by a **PDP** (e.g., OPA), and applied at multiple **PEPs**:
  - CI (policy tests + schema validation) — blocks merges
  - Governed runtime API — checks before serving data
  - Evidence resolver — checks before resolving evidence bundles
  - UI — displays badges/notices, but **never** makes policy decisions

### Where obligations must be applied

- **Promotion gate:** A dataset version cannot be promoted unless policy_label is assigned and required obligations are satisfied.
- **Evidence resolver:** A citation must resolve into a policy-allowed EvidenceBundle; if not, the system must abstain or narrow scope.
- **Exports/downloads:** Must attach attribution and must not leak restricted fields/coordinates.

### Policy-safe errors (required)

Error responses must:

- provide an `audit_ref` for steward investigation
- avoid revealing restricted dataset existence or metadata via 403/404 differences (“ghost metadata”)

---

## Policy-safe UX requirements

UI must:

- show **policy badges** and **policy notices** at the moment of interaction
- show “redactions applied” (obligations) in the evidence drawer
- support abstention without leakage:
  - explain “why” in policy-safe terms
  - suggest safe alternatives (broader scope, public-only)
  - include `audit_ref` for follow-up

---

## Consequences

### Positive

- One consistent, testable meaning of “public vs restricted” across all KFM surfaces.
- Redaction is reproducible and auditable (no ad hoc hand edits).
- “Cite or abstain” becomes enforceable because evidence resolution is policy-gated.

### Negative / tradeoffs

- More upfront work: policy fixtures, obligation schema, generalization pipelines.
- Requires discipline: label drift and ad hoc exceptions must be blocked.
- Some user requests will produce abstentions or generalized results (by design).

---

## Implementation checklist

### Contracts and vocabularies
- [ ] Add/confirm controlled vocabulary registry for `policy_label` and `geometry.generalization_method`
- [ ] Add obligation schema (JSON Schema or equivalent) and sample fixtures (valid/invalid)

### Policy pack
- [ ] Implement policy rules for allow/deny and obligations
- [ ] Add CI fixture-driven tests (must block merges)
- [ ] Add “policy-safe errors” tests (no restricted inference)

### Pipelines
- [ ] Implement generalization transforms producing `public_generalized` dataset versions
- [ ] Record transforms in PROV/run receipts

### Runtime
- [ ] Evidence resolver returns (decision, policy_label, obligations) and applies “deny_asset_links” as needed
- [ ] API filters catalogs by policy_label and enforces obligations on query/export

### UI
- [ ] Add policy badges + notice rendering for obligations
- [ ] Evidence drawer shows “redactions applied”
- [ ] Abstention UX patterns implemented without leakage

---

## Open questions

1. **Obligation schema finalization:**  
   Do we standardize obligations as “to be applied” vs “applied”? (Some docs imply “obligations applied” in the evidence bundle payload.)
2. **Embargoed semantics:**  
   Is release time purely manual steward action, or can policy reference time for automatic flips?
3. **Partner / community-controlled datasets:**  
   Do we extend policy input with `owner_group` / consent constraints (ABAC) now, or defer until first partner integration?

---

## Back to top

[↑ Back to top](#adr-0007-policy-labels-redaction-and-obligations)
