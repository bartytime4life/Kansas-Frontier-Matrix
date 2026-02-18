# Runbook Templates

![Scope](https://img.shields.io/badge/scope-runbooks-6b7280)
![Governance](https://img.shields.io/badge/governed-evidence--first-2563eb)
![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-required-16a34a)
![Trust Membrane](https://img.shields.io/badge/trust%20membrane-enforced-7c3aed)

> [!IMPORTANT]
> **Runbooks are governed artifacts.** Treat changes like production changes:
> - PR-reviewed (owners + domain reviewers)
> - link-check clean
> - actionable + deterministic where possible
> - safe to share (redaction/sensitivity rules respected)
>
> If a runbook step cannot be executed safely, the runbook **must** say so explicitly and include an escalation path.

---

## Purpose

This folder contains **copy/paste templates** for creating and maintaining KFM runbooks under `docs/runbooks/**`.

Runbooks are **operationally focused** documents:
- incident response playbooks
- reliability procedures (retries, triggers, rollbacks)
- pipeline “lane” procedures (snapshot → validate → transform → publish → catalog → provenance → promote)

---

## What lives here

### ✅ This directory (`docs/runbooks/_templates/`)
- Stable templates you copy into a new runbook.
- Minimal “policy-aligned” structure so runbooks are consistent across teams.

### ❌ This directory is **not**
- A dumping ground for one-off notes
- A place to store secrets, credentials, or sensitive locations
- A substitute for design docs (architecture decisions belong in `docs/specs/**` or equivalent)

---

## Directory layout

> [!NOTE]
> Paths below are **conventions** used across KFM docs; exact structure may vary by repo state.

| Area | Path | What it contains |
|---|---|---|
| Runbooks root | `docs/runbooks/` | Operational procedures and playbooks |
| Templates | `docs/runbooks/_templates/` | Copy/paste templates (this folder) |
| Reliability | `docs/runbooks/reliability/` | Triggering, retries, failure modes, escalation paths |
| Pipelines | `docs/runbooks/pipelines/` | Lane/pipeline operational runbooks (publish + provenance + promotion) |
| Incidents | `docs/runbooks/incidents/` | P0/P1/P2 playbooks + comms + postmortems |
| Security ops | `docs/runbooks/security/` | Emergency patching, key rotation, incident containment (redaction-safe) |

---

## Templates catalog

> [!TIP]
> Prefer **fewer templates** that are well-maintained over many half-finished ones.

| Template filename | Use when | Primary output |
|---|---|---|
| `TEMPLATE__RUNBOOK.md` | General operational procedure (manual or semi-automated) | Repeatable steps + verification + rollback |
| `TEMPLATE__PIPELINE_LANE_RUNBOOK.md` | Data lane run: snapshot → validate → transform → publish → catalogs/provenance → promotion | Step/Output/Gates table + artifact layout |
| `TEMPLATE__INCIDENT_PLAYBOOK.md` | P0/P1/P2 incident handling | Triage → mitigate → communicate → recover |
| `TEMPLATE__POSTMORTEM.md` | After incident resolved | Timeline + contributing factors + fixes + follow-ups |
| `TEMPLATE__CHANGE_PROMOTION.md` | For “promotion PRs” that publish governed artifacts | Checklist-driven promotion + rollback tag |

> [!WARNING]
> If a template listed above does not exist yet, create it first or remove it from this README.
> A template catalog should not drift from reality.

---

## How to use a template

1. **Copy** a template into the appropriate runbook folder.
2. **Rename** it using a stable, readable slug (kebab-case).
3. **Assign a stable ID** (see “Naming & IDs”).
4. Fill all **Required** fields and remove instructional placeholder text.
5. Add at least one **dry-run verification** section (even if it’s “simulated”).
6. Open a PR with:
   - owner reviewers
   - domain reviewer (data, security, SRE) as needed
   - links to related dashboards / alert rules / pipeline jobs

Example:

```bash
cp docs/runbooks/_templates/TEMPLATE__RUNBOOK.md \
   docs/runbooks/reliability/retry-storm-mitigation.md
```

---

## Naming & IDs

### File naming
- Use **kebab-case**: `retry-storm-mitigation.md`, `postgis-backup-restore.md`
- Keep names action-oriented: “how to mitigate / how to restore / how to rotate”

### Stable runbook IDs
Use a stable ID that never changes even if the filename changes:

- `RUNBOOK-REL-0001`
- `RUNBOOK-PIPE-0021`
- `INCIDENT-P1-PLAYBOOK-0003`

> [!NOTE]
> IDs are used for audit trails, references, and incident comms. Prefer stable IDs over titles.

---

## Minimum required structure (for every runbook)

> [!IMPORTANT]
> Runbooks must be **executable documents**, not essays.
> If a step requires judgment, write down the decision criteria.

### Required sections
- **Overview**
  - Purpose
  - When to use / when not to use
  - Impact / blast radius
- **Preconditions**
  - Access requirements (roles, tools)
  - Safety constraints
- **Procedure**
  - Step-by-step instructions
  - Verification after each major step
- **Rollback / Exit**
  - How to revert safely
  - “Stop conditions” (when to halt and escalate)
- **Evidence to capture**
  - Logs, checksums, reports, screenshots (redaction-safe)
- **References**
  - Related runbooks, dashboards, specs, tickets

### Recommended metadata header (optional but strongly encouraged)

```yaml
---
id: RUNBOOK-REL-0001
title: Retry Storm Mitigation
owners:
  - team-sre
review_cycle_days: 90
last_reviewed: YYYY-MM-DD
severity: P1
systems:
  - api-gateway
  - pipelines
  - queues
tags:
  - reliability
  - retries
sensitivity:
  class: public|internal|restricted
  notes: "Do not include exact locations or sensitive asset identifiers."
---
```

---

## Pipeline lane runbook pattern

> [!NOTE]
> Pipeline runbooks should follow the **Step → Output → Gate(s)** structure so CI and humans can audit the run.

### Step / Output / Gate(s) table (recommended)

| Step | Output | Gate(s) (fail-closed) |
|---:|---|---|
| 1) Snapshot raw sources | `RAW + MANIFEST + checksums` | checksum verification; retention policy |
| 2) Geometry fix + CRS | fixed vector layer | CRS/axis sanity; geometry validity |
| 3) Key normalization | stable, de-duplicated keys | uniqueness; referential integrity |
| 4) Attribute QC | QC report | policy bounds; null/domain constraints |
| 5) Delivery formats | GeoParquet / COG / PMTiles | format validators (gdalinfo, parquet schema, tile smoke test) |
| 6) Catalogs + lineage | STAC / DCAT / PROV (+ signatures) | schema validation; required fields; signatures present |
| 7) Promotion proposal | signed PR + rollback tag | PR checklist complete; rollback path documented |

### Promotion-ready output layout (example)
```text
data/<domain>/raw/<provider>/<yyyymmdd>/
data/<domain>/processed/<region>/<job_id>/            # GeoParquet / COG / PMTiles
data/stac/<domain>/<region>/<job_id>/
data/catalog/dcat/<domain>/<region>/<job_id>/
data/prov/runs/<job_id>/
```

> [!WARNING]
> Pipeline runbooks must include a **rollback/quarantine strategy**:
> - how to invalidate a run
> - how to prevent downstream use
> - how to communicate the rollback

---

## Governance & sensitivity rules

> [!IMPORTANT]
> Do not publish details that increase risk:
> - precise sensitive locations (especially cultural/archaeological)
> - credentials, tokens, private endpoints
> - non-public partner constraints

### Required
- State the runbook’s **sensitivity class** and any redaction rules.
- If the procedure produces artifacts, specify:
  - licenses (if applicable)
  - provenance pointers (where the evidence lives)
  - retention expectations (where logs/manifests are kept)

### If you’re unsure
- Default to **generalizing** details (e.g., “restricted site”, “partner feed”)
- Add a note: **“Requires governance review before public sharing.”**

---

## Definition of Done (DoD) for a new runbook

- [ ] Title + stable ID assigned
- [ ] Owners listed + review cadence set
- [ ] “When to use / not use” is explicit
- [ ] Preconditions + access requirements listed
- [ ] Procedure includes verification checkpoints
- [ ] Rollback / stop conditions documented
- [ ] Evidence-to-capture section included
- [ ] Links to dashboards/logs are redaction-safe
- [ ] No secrets, no sensitive locations, no private keys
- [ ] PR includes reviewers for affected domains (SRE/security/data)

---

## Maintaining templates

> [!TIP]
> Templates are living contracts. Updating a template should prompt updating existing runbooks (or at least filing an issue).

When you change a template:
1. Keep changes minimal and backwards-compatible.
2. Add a short changelog entry (in the template footer or repo-level changelog).
3. Create follow-up tasks to update high-risk runbooks first (P0/P1).

---

## Quick FAQ

<details>
<summary><strong>When do I write a runbook vs a design doc?</strong></summary>

Write a **runbook** when someone might need to execute it during an incident or operational task.

Write a **design doc/spec** when you’re making a system decision (architecture, schema, interfaces, governance model).

</details>

<details>
<summary><strong>When should a runbook be deprecated?</strong></summary>

Deprecate when:
- the system changed and the procedure is no longer safe
- a newer runbook supersedes it
- the runbook depends on tools that no longer exist

Mark it clearly:
- Status: Deprecated
- Link to replacement
- Date + owner

</details>

---

## References

- See: `docs/runbooks/` for operational procedures and playbooks.
- See: `docs/specs/` (or equivalent) for system-level design decisions.

> [!NOTE]
> Add any repo-specific references here once the relevant documents exist (dashboards, CI policies, incident comms SOP, etc.).
