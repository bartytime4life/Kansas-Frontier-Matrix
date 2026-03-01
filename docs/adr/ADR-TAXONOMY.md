<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/7ec8f4ba-9bb0-4d51-9bbc-50e765bc1eb3
title: ADR-TAXONOMY — KFM Taxonomy & Controlled Vocabularies
type: adr
version: v1
status: draft
owners: kfm-governance, kfm-platform
created: 2026-03-01
updated: 2026-03-01
policy_label: public
related: []
tags: [kfm, adr, taxonomy, controlled-vocabulary]
notes:
  - Establishes v1 controlled vocabularies + token rules used across catalogs, policy, UI, and evidence resolution.
  - TODO: add related kfm:// doc IDs for the Governance Guide / Pipeline Plan once minted.
[/KFM_META_BLOCK_V2] -->

# ADR-TAXONOMY: KFM Taxonomy & Controlled Vocabularies

**Purpose:** Define a governed, versioned taxonomy (controlled vocabularies + rules) so that **pipelines, catalogs, policy, UI, and Focus Mode** speak the same language — and can **fail closed** when they don’t.

![Status](https://img.shields.io/badge/status-draft-lightgrey)
![ADR](https://img.shields.io/badge/type-ADR-blue)
![Scope](https://img.shields.io/badge/scope-taxonomy%20%26%20vocabularies-purple)
![Governance](https://img.shields.io/badge/posture-fail--closed-critical)

---

## Navigation

- [Status](#status)
- [Context](#context)
- [Decision](#decision)
- [Definitions](#definitions)
- [Taxonomy surfaces](#taxonomy-surfaces)
- [Controlled vocabularies](#controlled-vocabularies)
- [Token and ID rules](#token-and-id-rules)
- [Validation and enforcement](#validation-and-enforcement)
- [Consequences](#consequences)
- [Alternatives considered](#alternatives-considered)
- [Rollout plan](#rollout-plan)
- [Minimum verification steps](#minimum-verification-steps)
- [Appendix A: Example vocab files](#appendix-a-example-vocab-files)

---

## Status

- **Status:** Draft (proposed)
- **Effective when:** Approved + merged
- **Owner:** Steward / Governance + Platform maintainers
- **Decision type:** Contract surface (affects CI gates + runtime policy + UI facets)

---

## Context

KFM is designed around a **trust membrane**: policy enforcement, evidence resolution, and traceability must behave the same in CI and runtime. That requires consistent, machine-checkable labels and categories.

Where taxonomy matters immediately:

- **Catalogs:** DCAT/STAC/PROV require controlled fields (e.g., `dcat:theme`, `kfm:policy_label`) and must validate predictably.
- **Evidence:** citations are **EvidenceRefs** and must resolve through the evidence resolver; a “citation” is not a pasted URL.
- **Policy:** access control and redaction obligations depend on stable classifications.
- **UI / Focus Mode:** facets, badges, and filters must be driven by the same tokens as the pipelines and policy engine.

Without controlled vocabulary + validation:
- Search facets drift (“hazard” vs “hazards” vs “storm”)
- Policy is brittle (“public-generalized” vs “public_generalized”)
- Evidence resolution can’t reliably interpret references
- CI can’t fail closed (because “unknown token” becomes “silent accept”)

---

## Decision

### 1) Adopt controlled vocabularies as contract surfaces

A **controlled vocabulary** is:
- versioned
- machine-readable
- validated in CI
- the **only** allowed source for enumerations used in:
  - catalogs (DCAT/STAC/PROV profiles)
  - policy inputs (`policy_label`)
  - evidence references (`citation.kind`)
  - artifact lifecycle (`artifact.zone`)
  - operational registries (source registry, layer registry)
  - UI facets and badges

### 2) Separate governed taxonomy from freeform tags

- **Taxonomy / vocab tokens** are used for:
  - policy decisions
  - CI gates
  - UI facets (filters)
  - analytics / reporting
- **Freeform tags** may exist, but:
  - MUST NOT drive policy decisions
  - MUST NOT be required for promotion gates
  - SHOULD be treated as “search hints” only

### 3) Start with KFM’s v1 starter lists and expand where required

**Confirmed starter lists (v1):**
- `policy_label`
- `artifact.zone`
- `citation.kind`

**Add v1 vocabularies needed to operationalize registries and UI facets:**
- `source.domain` (hierarchical)
- `source.access_method`
- `source.cadence`

**Optional (defer unless needed):**
- `layer.delivery.type`
- `license.class`
- `time.semantic` (event vs valid vs observation windows)
- `graph.entity_type` (place/person/event/document/etc.)

### 4) Deprecate, don’t delete

- Tokens are stable identifiers.
- **No removal in minor versions.**
- Use:
  - `status: active|deprecated`
  - `deprecated_since`
  - `replaced_by` (optional)
- Runtime and CI must remain compatible with historical tokens to preserve auditability.

---

## Definitions

- **Controlled vocabulary (vocab):** A finite set of allowed tokens, published as a versioned artifact.
- **Taxonomy:** A vocabulary that is hierarchical (e.g., `admin/basemap`), enabling rollups.
- **Token:** The machine identifier (stable; used in JSON, catalogs, policy, receipts).
- **Label:** Human-facing display string (can change without breaking compatibility).
- **EvidenceRef:** A typed reference (e.g., `dcat://…`, `prov://…`) that resolves into an EvidenceBundle.
- **Policy label:** A classification used by policy enforcement points to allow/deny + obligations.

---

## Taxonomy surfaces

This ADR governs tokens used in these surfaces:

### A) Catalogs (DCAT/STAC/PROV)

- `kfm:policy_label`
- `dcat:theme` (controlled vocabulary)
- artifact classifications (zone, media types, etc.)
- identifiers for datasets and versions

### B) Source registry (data onboarding contract)

Minimum fields include (not exhaustive):
- `source_id` (stable)
- `authority`
- `domain`
- `access_method`
- `cadence`
- `license/rights`
- `sensitivity` (maps to `policy_label` intent)
- `notes`

### C) Layer configuration (UI integration contract)

A layer config binds catalogs to rendering + evidence behavior and includes:
- `layer_id`
- `dataset_slug`
- `dataset_version_id`
- `policy_label`
- delivery configuration (type/href/digest)
- style references

### D) Story Nodes and Focus Mode (citation contract)

Story Node sidecars and narrative citation markup use:
- `citations[].kind` (must be from `citation.kind`)
- `citations[].ref` (must match the scheme implied by `.kind`)
- publishing gate requires citations resolve through evidence resolver

---

## Controlled vocabularies

### v1 vocabulary registry

> **NOTE:** Proposed file locations are intentionally marked “proposed” until verified in the live repo.

| Vocab ID | Token format | Used by | Examples | Owner | Change rule |
|---|---|---|---|---|---|
| `policy_label` | `lower_snake` | policy, catalogs, UI badges | `public`, `restricted_sensitive_location` | Steward | add-only + deprecate |
| `artifact.zone` | `lower_snake` | pipelines, promotion, receipts | `raw`, `work`, `processed` | Platform | add-only + deprecate |
| `citation.kind` | `lower_snake` | Story Nodes, evidence resolver | `dcat`, `prov`, `doc` | Platform | add-only + deprecate |
| `source.domain` | `path_token` | source registry, discovery facets | `hazards`, `admin/basemap` | Steward | add-only + deprecate |
| `source.access_method` | `lower_snake` | source registry, pipeline plans | `api`, `bulk`, `portal` | Platform | add-only + deprecate |
| `source.cadence` | `lower_snake` | source registry, freshness reporting | `daily`, `monthly`, `annual` | Steward | add-only + deprecate |

### policy_label

**Goal:** Encode access + sensitivity posture with a small controlled set.

**v1 tokens (starter):**
- `public`
- `public_generalized`
- `restricted`
- `restricted_sensitive_location`
- `internal`
- `embargoed`
- `quarantine`

**Meaning (normative):**
- `public`: may be served to public users.
- `public_generalized`: served publicly, but **geometry/fields are generalized** (must also emit UI notice obligation).
- `restricted`: require privileged role(s); deny by default for public.
- `restricted_sensitive_location`: restricted + additional safeguards; do not surface precise geometry.
- `internal`: authenticated internal use; not public.
- `embargoed`: not public until embargo conditions satisfied.
- `quarantine`: blocked from promotion and publication pending QA/policy review.

### artifact.zone

**Goal:** Normalize lifecycle zone naming so receipts, catalogs, and promotion manifests can be validated.

**v1 tokens (starter):**
- `raw`
- `work`
- `processed`
- `catalog`
- `published`

### citation.kind

**Goal:** Ensure citations are typed references the evidence resolver can interpret (URLs are discouraged).

**v1 tokens (starter):**
- `dcat`
- `stac`
- `prov`
- `doc`
- `graph`
- `url` (discouraged)

**Normative mapping (recommended):**
- `dcat` → `dcat://…`
- `stac` → `stac://…`
- `prov` → `prov://…`
- `doc` → `doc://…`
- `graph` → `graph://…`
- `url` → allowed only when explicitly whitelisted and cataloged

### source.domain (hierarchical taxonomy)

**Goal:** Enable consistent, roll-up friendly discovery facets.

**Rules:**
- allow either:
  - single token: `hazards`
  - hierarchical path: `admin/basemap`
- hierarchy implies rollups:
  - `admin/basemap` is also in `admin`

**Starter examples observed in registry drafts (non-exhaustive):**
- `hazards`
- `hydrology`
- `demographics`
- `boundaries`
- `basemap`
- `land/history`
- `history/archive`
- `heritage`
- `climate`
- `admin/basemap`

### source.access_method

**Goal:** Normalize acquisition strategy and support automated connector selection.

**v1 tokens:**
- `api`
- `bulk`
- `portal`
- `manual`
- `partner`

### source.cadence

**Goal:** Normalize update cadence reporting for “freshness” and watcher design.

**v1 tokens:**
- `daily`
- `weekly`
- `monthly`
- `annual`
- `occasional`
- `varies`

---

## Token and ID rules

### Token character set

**Default token regex (recommended):**
- `lower_snake`: `^[a-z][a-z0-9_]*$`
- `path_token` (hierarchical): `^[a-z][a-z0-9_]*(/[a-z][a-z0-9_]*)*$`

### Naming conventions

- Prefer **lower_snake_case** for tokens.
- Use `/` only where hierarchy is meaningful and intended (e.g., `admin/basemap`).
- No spaces, no capitalization, no punctuation beyond `_` and optional `/`.
- Tokens MUST be globally unique **within** their vocabulary.

### IDs vs labels

- **Token**: stable machine ID used in:
  - JSON schemas
  - policy inputs
  - receipts
  - catalogs
- **Label**: display string for UI; can change without breaking compatibility.

### Compatibility

- Once a token is in use in:
  - a published dataset version
  - a Story Node
  - a run receipt
  - a catalog record
  it MUST remain resolvable forever (deprecate but keep).

---

## Validation and enforcement

### CI gates (fail closed)

CI MUST fail when:
- a token is not present in the vocab version pinned by the build
- a deprecated token is introduced without an explicit migration note
- a Story Node includes a citation kind that is not recognized
- catalogs reference unknown `policy_label` or `artifact.zone`

### Runtime enforcement

Runtime MUST:
- deny by default when `policy_label` is missing/unknown
- apply redaction/generalization obligations when `policy_label` requires it
- validate that evidence refs align with `citation.kind` (scheme correctness)

### Proposed artifacts (not confirmed in repo)

- `contracts/vocab/*.yaml` or `*.json`
- `contracts/schemas/vocab_v1.schema.json`
- `tools/validators/vocab_validator`
- CI job: `vocab-validate` (required status check)

---

## Consequences

### Positive

- Consistent search facets across UI and API
- Deterministic policy behavior (no “stringly-typed” drift)
- Evidence resolution becomes predictable (typed citations)
- CI can block unsafe drift early (fail closed)
- Audit receipts remain interpretable over time

### Negative / costs

- Governance overhead: someone must own vocab updates
- Migration work when “close-enough” tags must be mapped into tokens
- Initial friction for contributors (must pick from controlled lists)

---

## Alternatives considered

1) **Freeform tags everywhere**
- Rejected: breaks policy, validation, and auditability.

2) **Hardcode enums in multiple schemas**
- Rejected: causes drift; vocab must be single source of truth.

3) **Adopt a large external taxonomy immediately**
- Deferred: adds complexity and governance cost early. Start with KFM-minimum lists and expand when there is demonstrated need.

---

## Rollout plan

### Phase 0 — Baseline vocab (v1)
- publish `policy_label`, `artifact.zone`, `citation.kind`
- update validators to enforce them

### Phase 1 — Registry vocab
- add `source.domain`, `source.access_method`, `source.cadence`
- validate source registry entries

### Phase 2 — UI alignment
- Map Explorer facet filters use `source.domain` and `policy_label`
- Evidence drawer uses `citation.kind` to determine resolver path and UX

### Phase 3 — Deprecation workflow
- establish:
  - deprecation policy
  - migration mapping file
  - CI warnings (and later errors) for deprecated token introduction

---

## Minimum verification steps

> Purpose: convert assumptions in this ADR from “Proposed” to “Confirmed” in the live repo.

- [ ] Confirm where controlled vocab files live in the repo (directory + naming).
- [ ] Confirm schemas exist for:
  - catalogs (DCAT/STAC/PROV profiles)
  - layer config
  - story node sidecar
  - vocab format itself
- [ ] Confirm CI has a required check that blocks merges on unknown tokens.
- [ ] Confirm the policy engine (OPA/Rego or equivalent) consumes `policy_label` and emits obligations.
- [ ] Confirm the evidence resolver enforces `citation.kind` and rejects unresolved refs.

---

## Appendix A: Example vocab files

> These examples illustrate shape and governance metadata. Adjust to match the repo’s actual schema.

```yaml
# vocab/policy_label.v1.yaml
vocab_id: policy_label
version: 1.0.0
owned_by: kfm-governance
tokens:
  - token: public
    label: Public
    status: active
    description: Allowed for public users.
  - token: public_generalized
    label: Public (Generalized)
    status: active
    description: Public derivative with redaction/generalization obligations.
  - token: restricted
    label: Restricted
    status: active
    description: Privileged access only.
  - token: restricted_sensitive_location
    label: Restricted (Sensitive Location)
    status: active
    description: Strong restrictions; never expose precise geometry.
  - token: internal
    label: Internal
    status: active
    description: Internal use only.
  - token: embargoed
    label: Embargoed
    status: active
    description: Not public until embargo conditions satisfied.
  - token: quarantine
    label: Quarantine
    status: active
    description: Blocked from promotion pending QA/policy review.
```

```yaml
# vocab/citation_kind.v1.yaml
vocab_id: citation.kind
version: 1.0.0
owned_by: kfm-platform
tokens:
  - token: dcat
    label: DCAT
    status: active
    scheme: dcat://
  - token: stac
    label: STAC
    status: active
    scheme: stac://
  - token: prov
    label: PROV
    status: active
    scheme: prov://
  - token: doc
    label: Document
    status: active
    scheme: doc://
  - token: graph
    label: Graph entity
    status: active
    scheme: graph://
  - token: url
    label: URL
    status: active
    discouraged: true
    description: Only allowed when explicitly whitelisted and cataloged.
```

---

## Appendix B: Deprecation policy (normative)

- Deprecation is recorded in the vocab itself.
- Deprecated tokens remain valid for:
  - resolving historical receipts and Story Nodes
  - reproducing old runs
- New usage of deprecated tokens should:
  - fail in CI (or warn during a transition window)
  - include `replaced_by` guidance

---

## References (inputs to this ADR)

- KFM Definitive Design & Governance Guide (vNext): controlled vocab starter lists; DCAT/STAC/PROV contract posture; source registry and layer config examples.
- Tooling / Pipeline Plan: evidence resolution contract; spec hashing + vocab validation as first work package.
- MARKDOWN_GUIDE (internal): Story Nodes require stable identifiers and clear fact-vs-interpretation separation.
