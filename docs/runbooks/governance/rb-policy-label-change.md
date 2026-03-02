<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/3d73c0d6-0f6f-4a23-8f2d-2e8a7bbf3a6c
title: "Runbook: Policy Label Change"
type: standard
version: v1
status: draft
owners: ["KFM Stewardship", "Policy Engineering", "Platform Ops"]
created: 2026-03-02
updated: 2026-03-02
policy_label: public
related:
  - docs/runbooks/governance/README.md
  - docs/runbooks/governance/rb-promotion.md
  - docs/runbooks/governance/rb-story-publish.md
  - docs/policy/README.md
tags: [kfm, runbook, governance, policy_label, opa, evidence, promotion]
notes:
  - "This runbook is evidence-first: every step produces an auditable artifact and is CI-testable."
[/KFM_META_BLOCK_V2] -->

# Runbook: Policy Label Change
**Purpose:** safely change `policy_label` for a DatasetVersion and/or Story Node without breaking the trust membrane, leaking restricted metadata, or leaving catalogs/evidence/indexes out of sync.

![Status](https://img.shields.io/badge/status-draft-yellow)
![Runbook](https://img.shields.io/badge/type-runbook-blue)
![Governance](https://img.shields.io/badge/area-governance-purple)
![Policy](https://img.shields.io/badge/focus-policy__label-black)

---

## Quick navigation
- [When to use](#when-to-use)
- [Scope](#scope)
- [Definitions](#definitions)
- [Roles and approvals](#roles-and-approvals)
- [Safety invariants](#safety-invariants)
- [Decision guide](#decision-guide)
- [Procedure](#procedure)
- [Verification checklist](#verification-checklist)
- [Rollback](#rollback)
- [Audit artifacts](#audit-artifacts)
- [Appendix: Templates](#appendix-templates)

---

## When to use
Use this runbook whenever you need to change `policy_label` on any governed surface, including:

1. **DatasetVersion** (catalog + API + tiles + evidence bundle behavior)
2. **Story Node** (publish visibility, map-state safety, evidence gates)
3. **Derived public representation** (e.g., `public_generalized` clone of a restricted dataset)

Common triggers:
- New sensitivity determination (e.g., “this layer reveals sensitive locations”)
- Rights/licensing clarification that changes allowed distribution
- A dataset that was generalized can now be shared publicly as `public_generalized`
- An embargo has lifted

---

## Scope

### In scope ✅
- Updating `policy_label` for an existing DatasetVersion **to become more restrictive**
- Creating a **new** DatasetVersion (or derivative) to support a **less restrictive** public representation
- Updating Story Node `policy_label` and ensuring publishing rules remain valid
- Ensuring DCAT/STAC/PROV + Evidence Resolver + indexes are consistent after change

### Out of scope ❌
- Creating a **new** `policy_label` value (requires controlled vocabulary change + new policy fixtures/tests)
- Changing the underlying sensitivity rubric (that is a governance policy doc change)
- Emergency incident response beyond immediate containment (see incident runbook, if present)

---

## Definitions

### `policy_label`
A controlled vocabulary value used as the **primary classification input** to policy enforcement, and a key driver for redaction/generalization obligations.:contentReference[oaicite:2]{index=2}:contentReference[oaicite:3]{index=3}

Starter labels (minimum set):
- `public`
- `public_generalized`
- `restricted`
- `restricted_sensitive_location`
- `internal`
- `embargoed`
- `quarantine`:contentReference[oaicite:4]{index=4}

### Obligations
Policy outputs may include “obligations” (e.g., “show a notice”, “generalize geometry”, “remove fields”) that must be honored by the resolver and UI.:contentReference[oaicite:5]{index=5}

### Trust membrane
Clients MUST NOT access storage/DB directly; all access goes through governed APIs applying policy, redaction, and logging.:contentReference[oaicite:6]{index=6}

### Catalog triplet
DCAT + STAC + PROV are contract surfaces; they must carry policy label fields and cross-links so EvidenceRefs resolve deterministically.:contentReference[oaicite:7]{index=7}

---

## Roles and approvals

Minimum roles (baseline):
- **Reviewer/Steward (Accountable):** approves policy label and redaction rules.
- **Policy engineer (Responsible):** updates policy pack + tests/fixtures.
- **Operator (Responsible):** runs pipelines/rebuilds; cannot override policy gates.:contentReference[oaicite:8]{index=8}

Consult as needed:
- Governance council / community stewards (culturally sensitive materials)
- Legal/compliance (rights unclear)
- Security (restricted infrastructure impacts):contentReference[oaicite:9]{index=9}

---

## Safety invariants

These are **non-negotiable** during a policy label change:

- **Default deny** for sensitive-location and restricted datasets (fail closed).:contentReference[oaicite:10]{index=10}
- If any public representation is allowed for sensitive data, create **a separate** `public_generalized` DatasetVersion (do not “just relabel” precise data as public).:contentReference[oaicite:11]{index=11}
- **Never leak restricted metadata** in error responses (e.g., avoid “helpful” 403/404 details).:contentReference[oaicite:12]{index=12}
- Redaction/generalization is a **first-class transform recorded in PROV** (it must appear in lineage).:contentReference[oaicite:13]{index=13}
- Policy semantics must be consistent in CI and runtime: CI fixtures/tests must match runtime outcomes.:contentReference[oaicite:14]{index=14}

---

## Decision guide

### The two safe patterns

#### Pattern A — Tighten access (lower risk)
Example: `public` → `restricted` or `restricted_sensitive_location`

✅ Allowed to re-label an existing DatasetVersion **more restrictive**, as an urgent containment move  
⚠️ Still requires catalog + index + cache consistency work

#### Pattern B — Loosen access (higher risk)
Example: `restricted_sensitive_location` → `public_generalized`, or `restricted` → `public`

✅ Create a **new** DatasetVersion with:
- explicit transformation steps (redaction/generalization)
- updated catalogs reflecting new label
- PROV lineage linking to the source DatasetVersion  
🚫 Do **not** simply flip a label on precise artifacts and call them public

---

## Procedure

> **Operating stance:** small, reviewable, reversible increments. PR-based change, CI enforced, fail closed.

### 0) Preflight: identify impact surface (required)
Capture and include in the change request (issue/PR):
- Target entity: DatasetVersion ID and/or Story ID
- Current label → proposed label
- Reason and evidence (sensitivity/rubric note, legal note, steward decision)
- Affected surfaces:
  - Dataset discovery (`/datasets` / catalog)
  - STAC browse/query
  - Tiles
  - Evidence resolver and Story publishing gates
  - Any public stories or saved views referencing it

**If the change is tightening access:** treat as a potential incident; prioritize containment.

---

### 1) Choose the correct label + obligations (required)
1. Pick the appropriate `policy_label` from the controlled vocabulary.
2. Determine if obligations apply:
   - geometry generalization
   - field suppression
   - UI notices
   - embargo date handling

> If you are changing from sensitive precise → public representation, the default path is **`public_generalized`** plus a recorded generalization transform.:contentReference[oaicite:15]{index=15}

---

### 2) Implement as a PR (required)
Create a PR that includes **only what is necessary**.

**2.1 Update catalog/registry policy fields**
- Ensure dataset registry has `policy_label` (it is a required governance input).:contentReference[oaicite:16]{index=16}
- Ensure DCAT carries `kfm:policy_label` and STAC carries policy label (and that item geometry is consistent with the label; generalized if needed).:contentReference[oaicite:17]{index=17}

**2.2 Update policy pack (OPA/Rego) and fixtures/tests (if needed)**
- Policies should be **default deny** and tested with fixtures; tests MUST run in CI and block merges.:contentReference[oaicite:18]{index=18}:contentReference[oaicite:19]{index=19}

**2.3 Story Nodes: confirm map-state + publish safety**
- Story sidecar includes `policy_label` and review state; publishing is gated by resolvable citations.:contentReference[oaicite:20]{index=20}
- Map state rules: references must point to promoted dataset versions; filters must be policy-safe (no hidden restricted fields).:contentReference[oaicite:21]{index=21}

---

### 3) CI validation gates (required)
Your PR must pass (or you must add) the following checks:

- Schema validation for registry/catalog artifacts
- Link checking across DCAT/STAC/PROV (EvidenceRefs resolve without guessing)
- Policy tests (allow/deny + obligations)
- Evidence resolution contract tests (deny if unauthorized; apply obligations; do not leak):contentReference[oaicite:22]{index=22}

> **Note:** exact command names are repo/tooling-specific. If you don’t have a single “check-all” command, wire these as discrete CI jobs.

---

### 4) Approval + merge (required)
- Steward approval required for label changes and any redaction rules.
- If culturally sensitive: governance council approval required (per your governance model).:contentReference[oaicite:23]{index=23}

---

### 5) Rebuild / re-publish required surfaces (required)
After merge, run the minimal rebuild needed for consistency:

- Rebuild catalogs (DCAT/STAC/PROV) so `policy_label` is correct and cross-links remain valid.
- Rebuild indexes/tiles/search (if they embed or cache results affected by policy).
- Invalidate caches that may have stored “public” material now restricted.

> Published runtime surfaces may only serve promoted dataset versions that have processed artifacts, validated catalogs, run receipts, and a policy label assignment — so re-syncing catalogs is not optional.:contentReference[oaicite:24]{index=24}

---

### 6) Verify runtime behavior (required)
Validate with two roles:
- `public` user (or equivalent)
- `steward` / authorized user

Key checks:
- Dataset discovery is policy-filtered by `policy_label`.
- Evidence resolver returns **deny** for unauthorized, and returns obligations when applicable.
- No restricted metadata leakage in error cases.
- Stories referencing newly restricted layers are blocked from public publishing until corrected.

Evidence behavior should be inspectable via EvidenceBundles (policy decision + label + obligations).:contentReference[oaicite:25]{index=25}

---

## Verification checklist

### Pre-merge checklist
- [ ] Label chosen from controlled vocabulary
- [ ] Obligations defined (or explicitly “none”)
- [ ] PR includes catalogs/registry updates
- [ ] Policy tests updated/added (default deny preserved)
- [ ] Evidence resolver contract tests pass
- [ ] Story impacts assessed (public stories/saved views)

### Post-merge checklist
- [ ] Catalogs rebuilt and validate
- [ ] Indexes/tiles/search rebuilt as needed
- [ ] Caches invalidated as needed
- [ ] Public role cannot discover/access restricted content
- [ ] Authorized role can access as intended
- [ ] No restricted metadata leakage on errors
- [ ] Audit artifacts recorded (see below)

---

## Rollback

### Rollback is allowed when
- The label change breaks critical functionality (false deny)
- The label was applied incorrectly (misclassification)
- The generalization transform produces unusable data (quality failure)

### Rollback steps (fail closed)
1. Revert PR (or apply a follow-up PR restoring previous label + catalogs).
2. Rebuild catalogs and affected indexes.
3. Verify public/authorized behavior again.

> **If data was accidentally exposed publicly**, rollback cannot “un-leak” it. Treat as an incident: tighten access immediately, purge caches, rotate access tokens if applicable, and document the event in the audit ledger.

---

## Audit artifacts

A policy label change MUST be traceable. Store (at minimum):
- PR link + commit SHA(s)
- Steward approval record
- Updated catalogs (DCAT/STAC/PROV) for the affected DatasetVersion(s)
- Run receipt(s) / promotion manifest(s) showing the policy label assignment and policy decision reference

Promotion manifests and receipts should carry policy references and approvals (template examples exist in KFM docs).:contentReference[oaicite:26]{index=26}

---

## Appendix: Templates

### A. PR description skeleton
- **What changed:** `policy_label` from X → Y for DatasetVersion/Story
- **Why:** sensitivity/licensing rationale + steward decision
- **Obligations:** list + where enforced
- **CI evidence:** links to policy tests + catalog validation + linkcheck
- **Runtime verification:** evidence resolver checks for public vs steward
- **Rollback plan:** revert + rebuild

### B. “Loosen access” safe pattern checklist
- [ ] Create a **new** DatasetVersion for `public_generalized`
- [ ] Record generalization transform in PROV
- [ ] STAC item geometry matches label (generalized if needed)
- [ ] Add UI notice obligation (if required)
- [ ] Steward approval + (if relevant) governance council approval

---
<a id="back-to-top"></a>
**Back to top:** [Quick navigation](#quick-navigation)
