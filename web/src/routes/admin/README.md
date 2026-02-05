# 🛡️ Admin Routes (`/admin`) — KFM Operator Console

![Route](https://img.shields.io/badge/route-%2Fadmin-blue)
![Audience](https://img.shields.io/badge/audience-maintainers%20%26%20admins-orange)
![Governance](https://img.shields.io/badge/governance-fail--closed-critical)
![Data](https://img.shields.io/badge/data-provenance--first-6f42c1)
![Policy](https://img.shields.io/badge/policy-RBAC%20%2B%20OPA-black)
![UI](https://img.shields.io/badge/ui-consistent%20%7C%20accessible-success)

> [!WARNING]
> This folder powers **privileged** workflows (publishing, policy, ingestion, moderation, user/role management).  
> Treat every feature here as **high-impact**: default-deny, audit everything, and require explicit confirmation for destructive actions.

---

## 🎯 Purpose

The **Admin** route is the **governed control room** for Kansas Frontier Matrix (KFM):  
a place where authorized operators can **curate**, **validate**, **publish**, and **protect** the knowledge platform end-to-end.

It exists to:
- ✅ Keep the system **trustworthy** (provenance, metadata completeness, policy compliance)
- ✅ Keep the system **safe** (least privilege, sensitive data handling, human review)
- ✅ Keep the system **maintainable** (consistent UI patterns, predictable workflows, tests)
- ✅ Keep the system **auditable** (“who did what, when, why, with which evidence?”)

---

## 🧭 Non‑Negotiable Principles (Admin Edition)

### 1) 🔁 The “Truth Path” is sacred
Admin UI **must not** create shortcuts that bypass the canonical flow:

**Raw → Processed → Catalog/Provenance → Database → API → UI**

If a proposed admin feature violates that chain, it’s a red flag.

### 2) 🧱 UI never talks to databases directly
Admin screens are still “just clients.”  
All reads/writes happen via the **backend API**, where validation and governance are enforced.

### 3) 🧷 Provenance-first, always
Any admin action that:
- alters data,
- changes metadata,
- publishes content,
- modifies policy,
- or changes access rules

…must result in:
- an audit trail entry,
- linked evidence/citations (where applicable),
- and provenance metadata updates (where applicable).

### 4) 🧯 Fail closed
If metadata is missing, policy doesn’t match, or the system can’t prove the request is allowed:
- **block the operation**
- show a clear reason
- include a “how to fix” path

### 5) 🤝 Respect community data rights
Admin tools must support (and never undermine):
- tiered access,
- sensitivity tags,
- CARE/FAIR-aligned handling,
- and collaboration modes that honor community control.

---

## 🔐 Access Model & Guardrails

### 🧑‍🤝‍🧑 Roles (typical)
> Actual role names may vary—align to the server’s RBAC/OPA policy pack.

- **Public Viewer**: can only read public, approved material
- **Contributor**: can draft/suggest; cannot publish directly
- **Maintainer**: reviews/approves; manages content lifecycle
- **Admin**: can run ingestion pipelines, configure policies, manage sensitive operations

### 🧾 Policy enforcement expectations
Admin pages must assume:
- **RBAC** checks at the API boundary (and optionally for UI gating)
- **OPA policy** decisions for every privileged request
- **Sensitivity classification** affects both what you can access and what the UI may render

> [!IMPORTANT]
> UI gating is not security. It’s *ergonomics*. Security lives at the API (and below).

---

## 🗺️ What belongs under `/admin`

Use `/admin` for operator workflows like:

### 🧪 Data & Pipelines
- Run ingestion / reprocessing jobs
- View pipeline runs, logs, artifacts
- Approve promotion of datasets (draft → published)

### 🗃️ Catalog & Metadata
- Edit dataset records (title, license, description, lineage links)
- Manage assets (STAC items, vector/raster references, exports)
- Validate metadata completeness

### 🧭 Layers & Publishing
- Enable/disable layers
- Version layers
- Promote “candidate” layers to public tiles

### 🧾 Governance & Policy
- Manage policy packs (OPA rules, sensitivity logic)
- Configure “allowed query surfaces” (approved tables/views/endpoints)
- Review and resolve policy failures

### 👥 Users & Access
- Invite / deactivate users
- Assign roles
- Manage special approvals for sensitive datasets

### 🧾 Audit & Provenance
- Review audit trail entries
- Trace “map/story behind the map/story”
- Export audit reports for governance review

---

## 🧠 UX Expectations (Admin is still UX)

Admin does not mean “developer-only UI.”  
Admin means: **high-stakes tasks with low tolerance for confusion**.

**Rules of thumb:**
- 🧭 **Consistent navigation**: one mental model across all admin screens
- 🟢 **Immediate feedback**: saving, errors, permission denials, background job status
- 🧾 **Explain the system’s decision**: “Denied because dataset is confidential and you lack approval”
- 🧯 **Prevent accidents**: destructive actions require explicit confirmation and context
- ♿ **Accessible by default**: keyboard-first, proper semantics, clear focus states, readable layouts

---

## ♿ Accessibility & Semantics

Admin routes should use:
- semantic layout landmarks (`header`, `nav`, `main`, `aside`, `footer`)
- form controls with labels and clear error messages
- predictable focus order and keyboard interactions
- consistent naming and content structure

> [!NOTE]
> Accessibility is not a “polish step.” It’s part of correctness—especially for operator workflows.

---

## 🧊 Sensitive Data Handling

Admin pages may access more data—but **not all admins should see everything**.

Recommended UI behaviors:
- 🏷️ Prominent **sensitivity badges** on datasets/entities (“Public”, “Restricted”, “Confidential”, “Sacred/Community-Controlled”)
- 🧭 Safe preview modes:
  - aggregate by default
  - require explicit intent to reveal finer-grained details
- 🧽 Redaction rules where required:
  - mask precise coordinates for sensitive points
  - avoid small-count displays in sensitive contexts
- 🧾 Always show: **why** data is restricted + **what to do next** (request approval, use aggregate view, etc.)

---

## ⚡ Performance & Reliability (Admin workflows scale)

Admin can involve huge lists (datasets, features, audit events). Design accordingly:
- 🔎 Debounced search + server-side filtering
- 📄 Pagination or virtualization (never render 20k rows naïvely)
- 🧵 Background jobs for heavy operations (imports, exports, reprocessing)
- 🧾 Streaming logs for pipeline runs
- 🧯 Clear retry semantics for idempotent operations

---

## 🧱 Recommended folder structure

> Adapt names to the framework in use (file-based routes, nested layouts, etc.). Keep the *information architecture* stable.

```text
📁 web/
  📁 src/
    📁 routes/
      📁 admin/
        📄 README.md                👈 you are here
        📄 (layout + nav shell)
        📁 datasets/                🗃️ catalog + metadata workflows
        📁 pipelines/               🧪 runs, logs, approvals
        📁 layers/                  🗺️ publish/visibility/versioning
        📁 policies/                🧾 OPA packs, rules, simulations
        📁 users/                   👥 roles, invites, approvals
        📁 audit/                   🧾 trail + provenance explorer
        📁 components/              🧩 admin-only UI building blocks
        📁 _shared/                 🔁 utilities local to admin
```

**Guideline:** If a component is used outside admin, it should live in a global shared location—not here.

---

## 🧩 Conventions for building admin pages

### ✅ Prefer “safe by default” UI flows
- Default to **read-only** views
- Require explicit “Edit” / “Publish” modes
- Use clear staging:
  - draft → review → approve → publish
- Provide “diff” views for changes when possible (especially metadata/policy)

### ✅ Error handling contract
Every admin page must handle:
- `401` unauthenticated (redirect / login)
- `403` forbidden (show role + policy reason)
- `409` conflicts (versioning/optimistic locking)
- validation errors (field-level + summary)
- background job failures (retry + link to logs)

### ✅ Destructive actions
For delete/unpublish/policy changes:
- require explicit confirmation text (e.g., type the dataset id)
- show the blast radius (“this will remove tiles for X layers”)
- require a reason / ticket reference (stored in audit)

---

## 🧰 Adding a new admin capability (checklist)

### 1) 🧭 Decide where it lives
- Is it data, catalog, policy, users, or audit?
- Does it need a review/approval path?

### 2) 🧪 Add the API surface
- Create/extend the API endpoint
- Ensure it is:
  - authenticated
  - authorized (RBAC + OPA)
  - validated
  - audited

### 3) 🧷 Wire the UI
- Create the route + page shell
- Add navigation entry
- Implement:
  - loading states
  - empty states
  - failure states
  - clear success confirmations

### 4) 🧾 Add provenance + audit hooks
- The “why” and “what changed” must be persistently recorded.

### 5) 🧪 Tests
- Unit tests for UI logic
- Integration tests for API calls + permission handling
- E2E for critical workflows (publish, policy change, role assignment)

### 6) 📚 Document it
- Add a short section under **Route Map** below
- Add any required operator notes

---

## 🧭 Route Map (fill as implemented)

> Keep this table accurate—operators rely on it.

| Route | Purpose | “Done” means… |
|------|---------|---------------|
| `/admin/datasets` | Manage catalog records + metadata | validated metadata + auditable edits |
| `/admin/pipelines` | Run/view ingestion & processing jobs | jobs are observable + recoverable |
| `/admin/layers` | Publish/enable/version map layers | safe rollouts + visibility controls |
| `/admin/policies` | Manage policy packs + simulations | changes are reviewed + reversible |
| `/admin/users` | Role/approval management | least privilege + approvals logged |
| `/admin/audit` | Audit & provenance explorer | traceability is one click away |

---

## 🧯 Troubleshooting quick hits

- **I can’t see the page** → likely role gating or feature flag
- **API returns 403** → policy denial (show reason, request approval)
- **Pipeline stuck** → check job logs + worker health + retry semantics
- **Data looks “missing”** → sensitivity masking or catalog not promoted yet
- **Policy change broke something** → rollback + run policy simulation tests

---

## 📚 Related KFM Docs (good starting points)

- `docs/architecture/system_overview.md` 🧠
- `src/server/api/README.md` 🔌
- `docs/governance/` 🧾
- `pipelines/README.md` 🧪
- `tools/kfm/README.md` 🧰

---

## ✅ Definition of Done (Admin PRs)

- [ ] UI matches the established admin navigation + layout patterns
- [ ] New capability is behind RBAC + OPA policy checks
- [ ] All write actions generate audit entries (and provenance where relevant)
- [ ] Sensitive data is labeled + safely rendered (no accidental disclosure)
- [ ] Errors are actionable (explain why + how to fix)
- [ ] Tests added/updated (unit + integration; E2E for high-risk flows)
- [ ] README + route map updated