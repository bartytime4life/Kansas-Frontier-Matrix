<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/ba465bfc-f789-4d75-b2e1-26a2c669fa97
title: Sovereignty
type: standard
version: v1
status: draft
owners: KFM Governance Council (TBD)
created: 2026-03-02
updated: 2026-03-02
policy_label: public
related:
  - docs/governance/ROOT_GOVERNANCE.md
  - docs/governance/ETHICS.md
  - docs/governance/REVIEW_GATES.md
  - docs/architecture/KFM_VISION_FULL_ARCHITECTURE.md
tags: [kfm, governance, sovereignty, care, safety]
notes:
  - This document defines sovereignty requirements as enforceable gates (CI + runtime), not aspirational guidance.
[/KFM_META_BLOCK_V2] -->

# Sovereignty
> One-line purpose: Operationalize **CARE + trust membrane** so KFM can be open *without* violating community authority, cultural rights, privacy, or partner constraints.

![Status](https://img.shields.io/badge/status-draft-yellow)
![Governance](https://img.shields.io/badge/policy-governance-blue)
![Safety](https://img.shields.io/badge/default--deny-sensitive%20locations-critical)
![CARE](https://img.shields.io/badge/CARE-Collective%20Benefit%20%7C%20Authority%20to%20Control%20%7C%20Responsibility%20%7C%20Ethics-blueviolet)

## Quick navigation
- [Purpose](#purpose)
- [Non-negotiables](#non-negotiables)
- [Definitions](#definitions)
- [Sovereignty commitments](#sovereignty-commitments)
- [Roles and authority](#roles-and-authority)
- [Sovereignty labeling model](#sovereignty-labeling-model)
- [Enforcement points](#enforcement-points)
- [Workflow](#workflow)
- [Redaction and generalization](#redaction-and-generalization)
- [Audit and accountability](#audit-and-accountability)
- [Governance review triggers](#governance-review-triggers)
- [Implementation checklist](#implementation-checklist)
- [Appendix](#appendix)

---

## Purpose
This document defines **sovereignty requirements** for the Kansas Frontier Matrix (KFM) and how those requirements MUST be implemented as:
- dataset onboarding and promotion gates,
- policy labels + obligations,
- runtime enforcement (governed API, evidence resolver, UI),
- and auditable outcomes.

### Scope
This policy applies to:
- data sources and derived datasets across the truth path,
- catalogs (DCAT/STAC/PROV) and evidence bundles,
- Story Nodes and any narrative publishing workflow,
- Focus Mode (AI-assisted retrieval/synthesis),
- exports/downloads/tiles and any public-facing representations.

### Non-goals
This document does **not**:
- define jurisdiction-specific law (seek counsel for legal interpretation),
- replace licensing policy (see governance/rights docs),
- define technical deployment details (those belong in architecture/runbooks),
- override community decisions (it encodes them).

---

## Non-negotiables
Sovereignty in KFM is only credible if it is enforced by architecture and tests.

KFM MUST preserve the following invariants:
1. **Truth path lifecycle**: Upstream → RAW → WORK/QUARANTINE → PROCESSED → CATALOG → PUBLISHED.
2. **Trust membrane**: clients and UIs MUST NOT access storage/DB directly; all access flows through governed APIs and policy enforcement.
3. **Policy-as-code parity**: CI and runtime MUST share policy semantics (fixtures and expected outcomes), otherwise CI guarantees are meaningless.
4. **Cite-or-abstain**: narratives and Focus Mode outputs MUST be traceable to resolvable evidence (or abstain).

> **Default-deny rule:** If sovereignty status is unclear, KFM MUST fail closed (deny access/publishing) until resolved.

---

## Definitions
### Sovereignty (KFM definition)
A set of **authority, consent, and control obligations** over:
- what may be collected,
- how it may be stored and transformed,
- who may access it (and at what granularity),
- and what may be publicly represented.

### Indigenous data sovereignty (CARE-aligned)
Sovereignty obligations that reflect Indigenous community rights and governance over culturally sensitive knowledge, sites, and narratives.

### Sensitive location
Any location where public precision increases risk of harm, targeting, looting, harassment, or ecological damage (e.g., sacred sites, restricted heritage inventories, endangered species habitat).

### Redaction and generalization
Transformations that remove or degrade sensitive attributes (including location precision) to satisfy sovereignty obligations. These are **first-class transforms** and MUST be recorded in provenance.

---

## Sovereignty commitments
KFM SHALL operationalize CARE principles as enforceable behavior:

- **Authority to Control:** communities and partners define what is publishable; KFM enforces via policy labels, obligations, and steward review.
- **Responsibility:** default deny for sensitive materials; prevent indirect leakage (tiles, exports, story text, error messages).
- **Ethics:** governance review triggers and consultation pathways; harm minimization is mandatory.
- **Collective Benefit:** when possible, publish safe derivatives (generalized layers, educational narratives, metadata-only records) that benefit the public without compromising authority.

---

## Roles and authority
> If a sovereignty decision conflicts with convenience or speed, **sovereignty wins**.

Minimum governance roles (expandable):
- **Contributor**: proposes datasets/stories; drafts specs; cannot publish restricted content.
- **Reviewer/Steward**: owns policy labels, redaction rules, and approves promotions/publishing.
- **Governance Council / Community Stewards**: holds authority to control culturally sensitive materials; defines acceptable public representations.
- **Operator**: runs pipelines and manages deployments; cannot override policy gates.

---

## Sovereignty labeling model
KFM MUST represent sovereignty as **policy labels + obligations**.

### Recommended labels (minimal)
| Label | Meaning | Default access | Notes |
|---|---|---:|---|
| `public` | publishable and safe | allow | still requires citation + provenance |
| `public_generalized` | explicitly generalized for safety | allow | must be non-reversible |
| `restricted` | sovereignty/partner constraints | deny by default | allow only by explicit policy/roles |
| `metadata_only` | discovery allowed, assets not mirrored | allow metadata; deny assets | use when rights/sovereignty unclear |

> NOTE: Actual label names are implementation-specific; what matters is the **deny-by-default** semantics and obligation enforcement.

### Obligations (examples)
Obligations are machine-enforceable requirements attached to a label, such as:
- remove coordinate fields,
- snap to coarse grid / aggregate to safe geographies,
- minimum-count thresholds for tables,
- blur/offset geometry for public tiles,
- disallow download/export even if visualization is allowed,
- require attribution/rights text on export.

---

## Enforcement points
Sovereignty MUST be enforced at every layer (not “just the UI”).

### 1) CI gates (pre-merge)
CI MUST block merges when:
- a dataset or story is missing sovereignty metadata,
- policy fixtures indicate deny/obligation failures,
- catalog triplets are missing `policy_label` or cross-links,
- Story Nodes contain restricted coordinates or unreviewed sensitive claims.

### 2) Promotion Contract gates (data lifecycle)
Promotion between zones MUST fail closed unless:
- license/rights snapshot exists,
- sensitivity classification exists,
- sovereignty label + obligations exist,
- redaction/generalization plan is documented (and tested),
- provenance shows *how* redaction/generalization was applied.

### 3) Runtime policy enforcement
- **Governed API (PEP)** MUST enforce allow/deny + obligations for all queries, tiles, downloads, and exports.
- **Evidence resolver** MUST enforce policy before resolving evidence bundles (no leakage via “citations”).
- **UI** MUST display policy badges/notices but MUST NOT make policy decisions.

---

## Workflow

### A. Onboard a new dataset (sovereignty-first)
1. **Source assessment**
   - Identify authority/rights holders and consent requirements.
   - Identify sensitive location or PII risks.
2. **Registry entry + terms snapshot**
   - Record license/terms and sovereignty constraints as versioned artifacts.
3. **Define policy label + obligations**
   - Default to `restricted` if uncertain.
4. **Implement redaction/generalization transform**
   - In WORK/QUARANTINE; record in PROV.
5. **Create publish-safe derivative (if allowed)**
   - `public_generalized` dataset_version created from restricted canonical.
6. **Add tests**
   - “No restricted bbox leakage” for public tiles.
   - “No coordinate fields” for public exports.
7. **Steward review + sign-off**
   - Required for culturally sensitive data and any classification changes.

### B. Publish Story Nodes / narratives
Story publishing MUST be blocked unless:
- every factual claim has resolvable evidence,
- included media has rights cleared or is metadata-only,
- sensitive locations are generalized (or omitted),
- review state is approved when sovereignty triggers are present.

### C. Focus Mode usage
Focus Mode MUST:
- pre-check policy before retrieval,
- never emit restricted coordinates unless explicitly permitted,
- emit a redaction notice when content is withheld/generalized,
- store a run receipt/audit record for sovereignty-relevant events.

---

## Redaction and generalization
KFM uses **two-track publication** for sensitive layers:

1. **Restricted canonical dataset**
   - precise geometries and attributes (restricted access only)
2. **Public derivative dataset (`public_generalized`)**
   - safe geometry and safe attributes
   - designed to be **non-reversible**
   - explicit provenance links back to the restricted canonical (without leaking secrets)

### Common patterns
- **Geometry generalization**
  - snap to grid, aggregate to safe units, blur, or replace with centroids of coarse geographies.
- **Attribute suppression**
  - remove identifiers, names, or free text that can reidentify individuals or sites.
- **Export controls**
  - allow map visualization but block file download for certain audiences.
- **Metadata-first publication**
  - publish catalog metadata without mirroring assets when rights/consent are unresolved.

> WARNING: Redaction MUST be applied across data, metadata, API responses, and UI surfaces. A “safe” dataset that leaks sensitive coords via metadata is still unsafe.

---

## Audit and accountability
Sovereignty obligations are enforced *and provable* only with auditing.

KFM SHOULD:
- store append-only audit logs for access and transformations,
- restrict audit log access to stewards/operators,
- redact audit logs for sensitive info,
- emit explicit telemetry events when sovereignty redaction is applied (e.g., “redaction_notice_shown”).

---

## Governance review triggers
A manual governance review is REQUIRED when any of the following occurs:
- introduction of culturally sensitive data or Indigenous data sovereignty (CARE) layers,
- addition of detailed archaeology sites, sacred sites, or tribal lands,
- new public-facing outputs (APIs, downloads, exports) that could expose sensitive info,
- changes to classification/sensitivity labels,
- new AI-driven narrative features that could be perceived as factual.

---

## Implementation checklist

### Repo artifacts that MUST exist
- [ ] Policy bundle (OPA/Rego or equivalent) with allow/deny + obligation fixtures.
- [ ] Sensitivity + sovereignty rubric (this doc + supporting checklists).
- [ ] Review workflow definition (promotion queue + story review queue).
- [ ] Audit ledger retention and access policy.
- [ ] Dataset registry schema supports sovereignty metadata (consent/constraints).
- [ ] Catalog profiles require `policy_label` and cross-links.

### Minimum automated tests (fail closed)
- [ ] Schema validation for sovereignty metadata fields.
- [ ] Policy tests for default-deny and obligation enforcement.
- [ ] “No restricted bbox leakage” checks on public tiles.
- [ ] “No coordinate fields” checks on public exports and Story Nodes.
- [ ] Evidence resolver tests ensuring restricted evidence cannot be resolved publicly.

---

## Appendix

<details>
<summary><strong>A. Sovereignty decision matrix (starter)</strong></summary>

| Data category | Example | Default label | Public representation allowed? | Required transform |
|---|---|---|---:|---|
| Culturally restricted locations | sacred sites, restricted heritage inventories | `restricted` | Usually no (or coarse only) | generalize geometry; suppress details; policy deny exports |
| Archaeology site coordinates | site points/polygons | `restricted` | Yes, but generalized | public derivative; no reverse engineering |
| Partner datasets under MOU | infrastructure, land ownership | `restricted` | depends on agreement | obligations per agreement; ABAC if required |
| PII-bearing records | letters, property ownership w/ names | `restricted` | aggregated only | remove identifiers; thresholds; safe geographies |
| Public open data | NOAA, USGS, etc. | `public` | yes | standard QA + provenance |

</details>

<details>
<summary><strong>B. “Sovereignty metadata” fields (PROPOSED)</strong></summary>

These are suggested fields for dataset registry entries and/or DCAT/STAC extensions:
- `kfm:policy_label`
- `kfm:sovereignty_authority` (who has authority to control)
- `kfm:consent_basis` (public domain, agreement, community permission, etc.)
- `kfm:restriction_rationale` (safety/culture/privacy/partner terms)
- `kfm:public_representation` (allowed/denied; if allowed, rules)
- `kfm:redaction_transform_ref` (PROV link to transform activity)
- `kfm:review_required` (boolean + reason codes)

</details>

---

_Back to top: [Sovereignty](#sovereignty)_
