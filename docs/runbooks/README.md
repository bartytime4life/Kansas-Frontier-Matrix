<!--
[KFM_META_BLOCK_V2]
doc_id: kfm://doc/<uuid>
title: Runbooks
type: guide
version: v1
status: draft
owners: <team or names>
created: 2026-02-22
updated: 2026-02-22
policy_label: restricted
related:
  - kfm://doc/<uuid-of-kfm-gdg>
tags:
  - kfm
  - runbooks
  - operations
notes:
  - Directory index and standards for operational playbooks.
[/KFM_META_BLOCK_V2]
-->

# Runbooks

Operational playbooks for running Kansas Frontier Matrix as a governed data → catalog → API → UI system.

**Status:** Draft • **Owners:** TBD • **Policy label:** Restricted • **Last updated:** 2026-02-22

![status](https://img.shields.io/badge/status-draft-lightgrey)
![policy](https://img.shields.io/badge/policy-restricted-lightgrey)
![governance](https://img.shields.io/badge/posture-fail--closed-lightgrey)

**Navigate:**  
[Runbook index](#runbook-index) • [How to use](#how-to-use-runbooks) • [Runbook standards](#runbook-standards) • [Runbook template](#runbook-template) • [Promotion gates](#promotion-gate-checklist) • [Escalation](#escalation-and-governance-review) • [Related docs](#related-docs)

---

## What belongs here

Runbooks are **step-by-step operational procedures** that can be executed by a maintainer (or CI automation) with:

- Clear triggers and prerequisites
- Explicit governance and safety checks
- Validation and rollback steps
- Required audit artifacts (run receipts, manifests, links to catalogs)

These runbooks exist to keep KFM **reproducible, auditable, and fail-closed**, not “best effort.”

## What does not belong here

- Secrets, tokens, private keys, credentials, or internal URLs that must not leak
- Exact coordinates or precise location details for sensitive sites
- “Tribal knowledge” that cannot be tested or validated

If a runbook needs sensitive details, reference a secured system of record and describe access controls.

---

## Runbook index

> NOTE  
> This README is an index. Add new runbooks as separate files and link them here.

### Data lifecycle and pipelines

| Runbook | Purpose | Typical trigger |
|---|---|---|
| `data/ingest_dataset.md` | Acquire upstream data into RAW with immutable artifacts and checksums | New dataset or upstream update |
| `data/quarantine_triage.md` | Triage failed validation / unclear licensing / sensitivity concerns | Pipeline fails gates |
| `data/promote_dataset_version.md` | Promote from RAW/WORK to PROCESSED + CATALOG + PUBLISHED | PR-based promotion |
| `data/rebuild_projections.md` | Rebuild PostGIS/search/graph/tiles from canonical artifacts | Index drift / schema upgrade |

### Catalogs, evidence, and policy

| Runbook | Purpose | Typical trigger |
|---|---|---|
| `catalog/validate_triplet.md` | Validate DCAT/STAC/PROV profiles + cross-links | Before promotion |
| `evidence/resolve_and_verify.md` | Verify EvidenceRefs resolve and respect policy | Story publish / Focus Mode changes |
| `policy/update_policy_pack.md` | Modify OPA policies + fixtures + tests | New policy rule / new dataset class |

### Runtime operations

| Runbook | Purpose | Typical trigger |
|---|---|---|
| `api/deploy_governed_api.md` | Deploy API with policy + evidence resolver | Release |
| `ui/release_map_story_focus.md` | Release UI with evidence drawer + version badges | Release |
| `ops/rotate_signing_keys.md` | Rotate signing keys for attestations/artifacts | Scheduled rotation / incident |

### Incidents and reviews

| Runbook | Purpose | Typical trigger |
|---|---|---|
| `incidents/policy_bypass_response.md` | Respond to suspected policy bypass | Security event |
| `incidents/licensing_violation.md` | Contain + remediate licensing issues | Rights complaint / audit finding |
| `incidents/sensitive_location_leak.md` | Contain + remediate location leakage | Reported leak / test failure |
| `governance/story_review.md` | Governance review for narrative framing | New sensitive story |

---

## KFM invariants runbooks must preserve

Runbooks are required to uphold KFM’s non-negotiable system invariants:

- **Truth path lifecycle:** upstream → RAW → WORK/QUARANTINE → PROCESSED → CATALOG/Lineage → projections → governed API → UI  
- **Trust membrane:** clients do not directly access storage/DB; access goes through governed APIs with policy, redaction, and logging  
- **Promotion Contract:** promotion must be blocked unless required gates and artifacts are satisfied  
- **Evidence-first and cite-or-abstain:** public claims must open into inspectable evidence; answers must cite resolvable evidence or abstain

### Truth path diagram

```mermaid
flowchart LR
  U[Upstream sources] --> C[Connectors and fetchers]
  C --> R[RAW zone]
  R --> W[WORK and QUARANTINE]
  W --> P[PROCESSED zone]
  P --> T[CATALOG triplet]
  T --> X[Index builders]
  X --> A[Governed API]
  A --> S[UI surfaces]
```

---

## How to use runbooks

1. **Confirm scope and policy label**
   - Is this operation public-safe or restricted?
   - Are there redaction obligations, CARE flags, or steward approvals required?

2. **Identify the trigger**
   - Scheduled run
   - Upstream change detected
   - CI gate failure
   - Incident response

3. **Execute the runbook steps**
   - Follow the steps exactly
   - Record deviations as notes in the audit trail

4. **Validate results**
   - Run required checks
   - Confirm artifacts are produced and links resolve

5. **Record audit artifacts**
   - Run receipt (and promotion manifest if applicable)
   - References to produced DCAT/STAC/PROV artifacts
   - Checksums/digests and environment info

6. **Rollback if validation fails**
   - Fail closed
   - Quarantine or revert promoted references
   - Open an incident ticket if needed

---

## Runbook standards

### Required elements

Every runbook MUST include:

- Trigger and scope
- Preconditions and required permissions
- Safety and policy checks
- Steps with explicit commands or actions
- Validation and expected outcomes
- Rollback procedure
- Required audit outputs
- Links to relevant standards and contracts

### Naming conventions

Recommended:

- Subfolders by operational area: `data/`, `catalog/`, `policy/`, `api/`, `ui/`, `incidents/`, `governance/`, `ops/`
- Filename: `<area>/<verb>_<object>.md`
- Keep titles imperative and specific: “Promote dataset version”, “Validate catalog triplet”

### Metadata

- Runbooks SHOULD include a **KFM MetaBlock v2** at the top.
- This repository uses **no YAML frontmatter**.
- In this directory, MetaBlocks are stored in an HTML comment to keep rendered docs clean.

---

## Runbook template

Copy this skeleton for new runbooks:

```markdown
<!--
[KFM_META_BLOCK_V2]
doc_id: kfm://doc/<uuid>
title: <Runbook title>
type: guide
version: v1
status: draft|review|published
owners: <team or names>
created: YYYY-MM-DD
updated: YYYY-MM-DD
policy_label: public|restricted|...
related:
  - kfm://dataset/<slug>@<version>
tags:
  - kfm
  - runbook
notes:
  - <short notes>
[/KFM_META_BLOCK_V2]
-->

# <Runbook title>

## Trigger

## Scope

## Preconditions

## Safety and policy checks

## Procedure

## Validation

## Rollback

## Audit outputs

## References
```

---

## Promotion gate checklist

Use this as an operator’s checklist before allowing a dataset version into published surfaces.

- Gate A: Identity and versioning
- Gate B: Licensing and rights metadata
- Gate C: Sensitivity classification and redaction plan
- Gate D: Catalog triplet validation
- Gate E: Run receipt and checksums
- Gate F: Policy tests and contract tests
- Gate G: Optional production posture checks

> TIP  
> If any gate cannot be satisfied, the correct outcome is **block promotion** and move the dataset version to **QUARANTINE**.

---

## Escalation and governance review

Escalate to governance review when any of the following are true:

- Licensing is unclear, incompatible, or cannot be captured
- The dataset includes sensitive locations, vulnerable infrastructure, or private individuals
- A story or layer could plausibly cause harm through misinterpretation or sensational framing
- Policy decisions are ambiguous or require a new obligation type

Recommended escalation path:

- Open a governance review issue
- Attach run receipt and relevant catalogs
- Propose a safe default (deny-by-default, generalized public derivative, or metadata-only reference)

---

## Suggested directory layout

This is a **recommended** (not guaranteed) layout for runbooks:

```
docs/runbooks/
  README.md
  templates/
    runbook_template.md
  data/
  catalog/
  evidence/
  policy/
  api/
  ui/
  ops/
  incidents/
  governance/
```

---

## Related docs

- `docs/guides/` — engineering and system guides
- `docs/standards/` — contracts, naming, QA, cartographic standards
- `docs/adr/` — architecture decision records
- `policy/` — policy-as-code, fixtures, tests
- `contracts/` — OpenAPI, schemas, and validation contracts
- `tools/validators/` — schema and link checkers

---

<details>
<summary>Maintenance notes</summary>

- Keep this index current: every runbook added should be linked above.
- Prefer PR-sized runbooks: short, testable, reversible.
- If the repo includes CODEOWNERS, ensure runbooks that affect policy or promotion have required reviewers.

</details>
