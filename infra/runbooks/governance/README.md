---
title: "KFM Governance Runbooks (Infra)"
path: "infra/runbooks/governance/README.md"
version: "v0.1.0-draft"
last_updated: "2026-02-16"
status: "draft"
doc_kind: "Runbook Index"
license: "TBD (inherit repo license)"
markdown_protocol_version: "TBD"
pipeline_contract_version: "TBD"

# Governance anchors (expected repo paths; adjust if the repo differs)
governance_ref: "docs/governance/ROOT_GOVERNANCE.md"
ethics_ref: "docs/governance/ETHICS.md"
sovereignty_ref: "docs/governance/SOVEREIGNTY.md"

fair_category: "FAIR+CARE"
care_label: "Public (this doc); runbook-specific overrides apply"
sensitivity: "public"
classification: "internal"
jurisdiction: "US-KS"

doc_uuid: "urn:kfm:doc:runbook:governance:index:v0.1.0-draft"
commit_sha: "<fill-on-merge>"
doc_integrity_checksum: "sha256:<fill-on-merge>"
---

# Governance Runbooks (Infra)

![status](https://img.shields.io/badge/status-draft-yellow)
![governance](https://img.shields.io/badge/governance-critical-blue)

> [!IMPORTANT]
> This directory is **governance-critical**. Treat changes like production changes:
> - PR required
> - Review required (CODEOWNERS / designated approvers)
> - CI gates must pass (fail-closed posture)
>
> If you need an exception/waiver, you must record it as a **governance ticket** and link it in the PR.

> [!CAUTION]
> **Do not** paste secrets, access tokens, or precise restricted locations into runbooks or examples.
> Keep operational procedures generic and point to secure systems (Vault, ticketing, etc.) instead.

---

## 📘 Overview

### Purpose

This folder contains the operational runbooks for KFM’s **governance layer**—the procedures that keep the platform:

- **Evidence-first** (citable, reproducible, and auditable outputs)
- **Fail-closed** (default-deny gates in CI and at runtime)
- **Sensitive-data safe** (redaction/generalization enforced)
- **FAIR + CARE aligned** (with explicit sovereignty and consent handling)

It is the “how we operate” companion to the governance and ethics policies in `docs/governance/`.

### Scope

| In scope ✅ | Out of scope ❌ |
|---|---|
| Policy-as-code operations (OPA/Rego) | Ad-hoc bypasses around policy |
| CI governance gates (schemas, link checks, attestations) | “Hot fixes” that skip evidence/provenance |
| Dataset promotion approval workflows (raw → work → processed → catalogs) | Direct DB edits from a client/UI |
| Sensitivity handling (restricted fields, sensitive-location generalization) | Unreviewed public release of restricted info |
| CARE / sovereignty gates (authority-to-control, consent facets) | Storing culturally restricted knowledge without review |
| Audit trails and incident response for governance failures | One-off debugging playbooks (put those under `infra/runbooks/reliability/`) |

### Audience

Primary:
- Infra/SRE maintainers
- Data stewards / domain stewards
- Security & governance reviewers
- Release managers

Secondary:
- API maintainers (policy integration + contract tests)
- Data pipeline contributors (dataset onboarding + promotion)

### Definitions

| Term | Meaning (in KFM context) |
|---|---|
| **Gate** | A merge/publish blocker that enforces a rule (schema, policy, attestation, sensitivity, etc.). |
| **Fail-closed** | If the system can’t prove “allowed”, it denies/blocks by default. |
| **Promotion** | Moving an artifact from *raw/work* to *processed* and publishing its catalogs. |
| **Policy label** | Classification for exposure (e.g., `public`, `restricted`, `sensitive-location`). |
| **Redaction / generalization** | A first-class transformation that removes or coarsens restricted information. |
| **Receipt / run_receipt** | Run-scoped, typed record of what happened (inputs, outputs, checks). |
| **Run manifest / run_manifest** | Promotion-oriented rollup (digests, rights, attestation pointers, etc.). |
| **Evidence resolver** | The bounded service that maps a citation → exact dataset/version/record evidence. |
| **Audit ref / audit_ref** | A stable identifier for governance-relevant decisions/events (logs, receipts, UI notice). |
| **CARE** | Collective Benefit, Authority to Control, Responsibility, Ethics. Used for sovereignty gating. |

### Key artifacts

| Artifact | Expected path | Owner | Notes |
|---|---|---|---|
| Governance policies | `docs/governance/*` | Governance | Constitutional rules, ethics, sovereignty. |
| Policy-as-code | `policy/` | Governance + Security | Rego bundles; default deny; tested. |
| Schemas/contracts | `schemas/` | Platform | `run_receipt`, `run_manifest`, promotion manifest, Story Node schema, etc. |
| Catalogs | `data/**/{stac,dcat,prov}/` | Data stewardship | Boundary artifacts for discovery + lineage. |
| CI gatehouse | `.github/workflows/` | Infra | Required status checks; fail-closed enforcement. |
| This runbook index | `infra/runbooks/governance/README.md` | Infra + Governance | Your entry point to operational procedures. |

### Definition of Done

- [ ] YAML front-matter present, valid, and up to date
- [ ] Uses the governed section structure (Overview → Directory Layout → Context → Gates → Runbook Index)
- [ ] Runbook index table matches the directory contents (no dead links)
- [ ] No secrets, tokens, or sensitive coordinates in examples
- [ ] Link-check clean (internal links resolve)
- [ ] Reviewed by governance approver(s)

---

## 🗂️ Directory Layout

### This directory

```text
infra/
  runbooks/
    governance/
      README.md                      # (this file) index + invariants + escalation
      _TEMPLATE__RUNBOOK.md          # runbook authoring template (copy for new runbooks)

      00-TRIAGE__governance-gate-failure.md
      10-POLICY__opa-rego-change-control.md
      20-DATASET__onboard-and-promote-dataset.md
      30-SENSITIVITY__redaction-and-generalization.md
      40-CARE__tribal-consent-facets.md
      50-EVIDENCE__receipt-attestation-verification.md
      60-INCIDENT__sensitive-data-leak.md
      70-AUDIT__audit-ledger-exports.md
      80-RELEASE__governed-release-cut.md
```

> [!NOTE]
> If the repository already has a different runbook home (e.g., `docs/runbooks/...`), keep the same structure and **symlink or cross-link** rather than duplicating.

### Naming conventions

- Prefix runbooks with a sortable number (`00`, `10`, `20`, …) to keep an intentional reading order.
- Include a domain tag: `POLICY`, `DATASET`, `SENSITIVITY`, `CARE`, `EVIDENCE`, `INCIDENT`, `AUDIT`, `RELEASE`.
- Use double-underscore between category and slug for scanning.

---

## 🧭 Context

### Governance invariants

These are **non-negotiable**. If a runbook suggests breaking them, the runbook is wrong.

1. **Trust membrane**
   - Frontend and external clients never talk to storage directly.
   - Core backend logic never bypasses repository interfaces to talk directly to PostGIS/Neo4j/search stores.

2. **Evidence-first**
   - User-visible answers must resolve to evidence bundles; otherwise **abstain** (with a policy-safe “why”).

3. **Fail-closed posture**
   - CI and runtime enforcement default to deny/block.
   - Promotions are blocked unless validation + policy + provenance succeed.

4. **Deterministic identity & reproducibility**
   - Manifests and identifiers are stable under canonicalization.
   - Promotion artifacts are content-addressed and checksummed.

5. **Sensitivity and sovereignty are first-class**
   - Restricted fields/locations are redacted or generalized.
   - CARE/consent signals are required where applicable (especially for boundary intersections).

### High-level flow

```mermaid
flowchart LR
  A[Change proposed<br/>PR / automation] --> B[CI Gatehouse]
  B -->|schema + links| C[Contract validation]
  B -->|policy-as-code| D[OPA/Conftest gates]
  B -->|attestation verify| E[Cosign/SLSA checks]
  C --> F[Human review]
  D --> F
  E --> F
  F -->|merge allowed| G[Promotion lane]
  G --> H[Processed outputs]
  H --> I[Catalogs<br/>STAC + DCAT + PROV]
  I --> J[Serving stores<br/>(graph/search)]
  J --> K[Governed API<br/>(policy checks)]
  K --> L[UI / Stories / Focus Mode<br/>(evidence resolver + audit)]
```

### Governance review triggers

File (or link) a governance ticket when any change impacts:

- **Schemas/contracts** (Story Node schema, STAC/DCAT/PROV profiles, receipts/manifests)
- **Policy bundles** (OPA/Rego rules, sensitivity rules, CARE gates)
- **Promotion logic** (raw/work/processed rules; deterministic IDs; versioning)
- **Evidence resolver** behavior or citation formats
- **Focus Mode** rules for cite-or-abstain, redaction, or narrative generation
- **Access control** roles, dataset classification, export/download behavior
- **Any new dataset** (especially with medium/high sensitivity)

### Roles & responsibilities (starter RACI)

| Area | Responsible | Accountable | Consulted | Informed |
|---|---|---|---|---|
| Policy bundle changes | Security/Governance | Governance lead | Domain steward | Platform |
| New dataset onboarding | Domain steward | Governance council | Infra, API | Community stakeholders (as appropriate) |
| Sensitivity/redaction rules | Governance | Governance lead | Domain steward | Platform |
| CARE consent facets | Governance + Domain steward | Governance council | Community reps (where applicable) | Platform |
| Incident response (leak) | Infra/SRE | Security lead | Governance | Maintainers |

---

## 🧪 Governance gates

### Minimum CI gates (conceptual)

Your CI should block merges/promotions unless:

- Docs pass **front-matter + section structure** validation
- Internal links and references are **link-check clean**
- Structured artifacts validate against schemas:
  - STAC Items/Collections
  - DCAT datasets
  - PROV bundles
  - Receipts/manifests/promotion manifests
- Policy gates pass (deny-by-default):
  - sensitivity rules
  - classification consistency (no downgrade without approved transform)
  - CARE consent rules
- Attestations verify (when applicable):
  - signed provenance/attestation matches artifact digest
  - verification checks identity/issuer constraints
- API contract tests pass for representative queries (especially evidence bundles + redaction)

### Runtime policy enforcement (conceptual)

At runtime, the API layer must query the policy engine for decisions like:

- Is this user authorized to access dataset X?
- If not, should the response be **denied** or **sanitized** (generalized geometry / masked fields)?
- Is the response about to leak restricted data in narrative form?

Audit logs must capture **which policy version** produced the decision.

### Dataset onboarding: minimum gates (portable checklist)

Use this checklist when creating or reviewing the onboarding runbook:

- [ ] Row/schema validation (required fields, type rules documented)
- [ ] Geometry validity + bounds (where applicable)
- [ ] Temporal consistency
- [ ] License + attribution captured in catalogs; restrictions encoded in policy
- [ ] Provenance completeness (PROV chain + deterministic checksums)
- [ ] Contract tests verify API returns evidence bundle + respects redaction

---

## 📚 Runbook index

> [!TIP]
> Keep runbooks small and composable. If a runbook grows beyond ~3–5 pages, split it by trigger.

| Runbook | When to use | Primary outputs | Owner |
|---|---|---|---|
| `00-TRIAGE__governance-gate-failure.md` | CI blocks merge/promotion | Triage notes + linked ticket | Infra |
| `10-POLICY__opa-rego-change-control.md` | Updating policies, adding new rules | Policy PR + tests + version bump | Governance/Security |
| `20-DATASET__onboard-and-promote-dataset.md` | New dataset integration | Onboarding PR + catalogs + manifests | Domain steward |
| `30-SENSITIVITY__redaction-and-generalization.md` | Sensitive fields/locations handling | Redaction transform + policy updates | Governance |
| `40-CARE__tribal-consent-facets.md` | Authority-to-control + consent needed | Consent facet record + expiry tracking | Governance + domain steward |
| `50-EVIDENCE__receipt-attestation-verification.md` | Receipt/attestation checks | Verified receipts + “untrusted” handling | Infra + Security |
| `60-INCIDENT__sensitive-data-leak.md` | Potential leak in outputs | Containment + audit refs + postmortem | Infra/Security |
| `70-AUDIT__audit-ledger-exports.md` | Audit requests, reproducibility checks | Exported audit bundle (sanitized) | Governance |
| `80-RELEASE__governed-release-cut.md` | Cutting a governed release | Release notes + signed artifacts | Release manager |

---

## ✅ Quick procedures (index-level)

### If a PR is blocked by a governance gate

1. Identify the failing gate (schema / policy / attestation / link-check / secrets scan).
2. Re-run the failing check locally (when possible) using the same pinned tool versions.
3. If the denial is legitimate: fix the artifact/policy/data; do **not** bypass.
4. If you believe it’s a false positive:
   - open a governance ticket
   - attach the denial output
   - propose the narrowest policy/schema change
5. Only merge after the gate passes (or an approved waiver is documented and referenced).

### Emergency “freeze” / kill-switch (conceptual)

Use only for suspected sensitive-data exposure or compromised policy integrity:

- Activate the kill-switch mechanism (implementation-defined: repo flag, CI secret, or both).
- Confirm it fails closed (blocks merges/promotions quickly).
- File an incident ticket and begin containment (see incident runbook).

> [!WARNING]
> Kill-switch behavior must be tested periodically so it works when needed.

---

## 🧩 Runbook authoring template

<details>
<summary><strong>Copy/paste: _TEMPLATE__RUNBOOK.md skeleton</strong></summary>

```markdown
---
title: "RUNBOOK — <title>"
path: "infra/runbooks/governance/<file>.md"
version: "v0.1.0"
last_updated: "YYYY-MM-DD"
status: "draft|active|deprecated"
doc_kind: "Runbook"
license: "TBD"
markdown_protocol_version: "TBD"
pipeline_contract_version: "TBD"
fair_category: "FAIR+CARE"
care_label: "TBD"
sensitivity: "public|restricted|sensitive-location"
classification: "internal"
jurisdiction: "US-KS"
doc_uuid: "urn:kfm:doc:runbook:<area>:<name>:v0.1.0"
commit_sha: "<fill-on-merge>"
doc_integrity_checksum: "sha256:<fill-on-merge>"
---

# RUNBOOK — <title>

## 📘 Overview
### Purpose
### Trigger / When to run
### Preconditions / Access
### Risks & safety notes

## 🧭 Procedure
1. Step…
2. Step…

## ✅ Verification
- What must be true at the end
- How to confirm (commands, checks, UI signals)

## 🔁 Rollback / Recovery
- How to revert safely
- What to document

## 🧾 Audit & provenance
- audit_ref generation
- required receipts/manifests
- where to store evidence bundles

## 📎 References
- Policies:
- Schemas:
- Related runbooks:
```

</details>

---

## 🔗 References (internal)

- `docs/governance/ROOT_GOVERNANCE.md`
- `docs/governance/ETHICS.md`
- `docs/governance/SOVEREIGNTY.md`
- `docs/templates/TEMPLATE__KFM_UNIVERSAL_DOC.md`
- `docs/templates/TEMPLATE__STORY_NODE_V3.md`
- `docs/templates/TEMPLATE__API_CONTRACT_EXTENSION.md`

> [!NOTE]
> If any referenced paths don’t exist yet in this repo, create them via the doc templates and add them to the governance backlog.
