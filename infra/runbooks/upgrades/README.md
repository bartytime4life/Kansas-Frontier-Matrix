<!--
File: infra/runbooks/upgrades/README.md
Scope: Infrastructure upgrade runbooks (governed operational artifacts)
-->

# 🛠️ Infra Upgrade Runbooks

![Governed](https://img.shields.io/badge/Governed-yes-2ea44f)
![Fail%20closed](https://img.shields.io/badge/Policy-fail--closed-blue)
![PR%20first](https://img.shields.io/badge/Workflow-PR--first-orange)
![Rollback%20first](https://img.shields.io/badge/Safety-rollback--first-critical)

KFM infrastructure upgrades must be **repeatable, auditable, and rollbackable**.  
This folder contains the **operator-facing runbooks** used to upgrade platform components (cluster, GitOps, data stores, gateways, observability, and runtime dependencies) **without violating KFM governance invariants**.

> [!IMPORTANT]
> **Trust membrane stays intact during upgrades.**  
> No “quick fixes” that bypass governed APIs, policy checks, or provenance requirements—ever.

---

## What belongs here

### ✅ In scope
- Cluster / platform upgrades (Kubernetes / OpenShift, node pools, CNI, CSI, ingress)
- GitOps tooling upgrades (Argo CD / OpenShift GitOps, policy bundles, admission)
- Data plane upgrades (PostgreSQL/PostGIS, Neo4j, search/index services, object storage)
- Observability & security plane upgrades (logging, metrics, tracing, cert-manager, secrets tooling)
- “Platform contracts” upgrades that affect:
  - promotion gates
  - provenance emission
  - authentication/authorization
  - rate limiting / API gateway behavior

### ❌ Out of scope
- Feature releases for product services (those go in app/service release runbooks)
- One-off incident mitigations **unless** documented as a “break-glass” upgrade with a retroactive change record

---

## Non‑negotiable invariants

These are **system rules**, not preferences:

- **Evidence-first:** upgrade decisions and outcomes must be traceable (change record + artifacts + verification).
- **Fail-closed promotion:** if required gates fail, **promotion stops** (no manual overrides without break-glass).
- **Rollback-first:** every upgrade runbook must include a tested rollback path.
- **No bypassing boundaries:** external clients and UIs never access storage directly; upgrades must not introduce shortcuts.
- **Governance is part of “done”:** the upgrade is not complete until audit/evidence is captured and validated.

---

## Standard upgrade workflow

### 1) Plan (before you touch anything)
- Identify **component**, **current version**, **target version**, and **compatibility constraints**.
- Confirm **blast radius**: which environments (dev/stage/prod), which dependencies, which data domains.
- Decide the lane:
  - **Routine** (normal change window)
  - **Security patch**
  - **Emergency break-glass** (rare; must be justified and retro-documented)

### 2) Open a PR (PR-first)
- All upgrade changes must be performed as a **pull request**:
  - manifests / Helm / Kustomize
  - policies (OPA/Rego / Conftest)
  - pipeline configs
  - upgrade scripts (if any)
  - documentation updates (this folder)

### 3) Run CI gates (fail closed)
Run (and *record results for*) the required gates in CI before staging promotion.

> [!TIP]
> Treat “upgrade PR CI” as the *first* verification step, not the last.

### 4) Promote through environments
- **Dev → Stage → Prod**, in order.
- Each promotion requires:
  - passing gates
  - human review approvals (as defined by governance policy)
  - verified rollback plan

### 5) Verify and monitor
- Run smoke checks and contract tests immediately after apply.
- Watch SLOs / alerts for a defined observation window.
- If SLOs regress or critical alerts fire: **rollback** (don’t “patch forward” blindly).

### 6) Close the change
- Update the change record with:
  - what happened
  - evidence (logs, dashboards, diffs, digests)
  - final outcome
  - follow-ups / debt created

---

## Default CI / promotion gate set

Use this as the baseline gates for *every* infra upgrade. Add more gates when the component demands it.

| Gate | What must be true (fail closed) | Minimum verification artifact |
|---|---|---|
| Determinism | Same inputs/config yield same outputs (within tolerance) | replay/snapshot test results |
| Schema | Schemas validate (API, catalog, manifests) | schema lint report |
| Governance labels | Sensitivity/sovereignty labels remain consistent | policy/conftest report |
| Provenance | Provenance emitted on pass/fail; links resolve | prov-check + link-check |
| Supply chain | Images signed; SBOM/attestations verified | cosign/sbom verification output |
| Quality | Health checks meet thresholds | quality report w/ thresholds |
| Telemetry | Metrics/logging still emitted as expected | telemetry schema check |
| Promotion | Promotion blocked unless all above gates pass | CI required checks + env protection |
| Rollback | Rollback is defined and rehearsed | rollback simulation evidence |

---

## Rollback-first expectations

Every upgrade runbook must include:

- **Rollback trigger conditions**
  - SLO violation (latency/error rate)
  - data corruption signal
  - auth/policy regressions
  - broken promotion gates / provenance emission failures
- **Rollback mechanics**
  - restore last-known-good **digest** / chart revision / manifest commit
  - validate rollback success with the same verification checklist
- **Rollback evidence**
  - record rollback decision, timestamps, and artifacts in the change record

---

## Directory layout

> [!NOTE]
> Some files/folders below may be “planned” until created. Keep naming consistent.

```text
infra/
└─ runbooks/
   └─ upgrades/
      ├─ README.md                  # you are here
      ├─ _template.md               # standard upgrade runbook template (recommended)
      ├─ records/                   # change records (append-only)
      │  └─ YYYY/
      │     └─ YYYY-MM-DD__component__from-to.md
      ├─ cluster/                   # Kubernetes/OpenShift upgrades
      ├─ gitops/                    # Argo CD / policy / promotion tooling upgrades
      ├─ data/                      # PostGIS/Neo4j/search/object store upgrades
      ├─ gateway/                   # API gateway / auth / rate limit upgrades
      └─ observability/             # metrics/logs/traces/certs upgrades
```

---

## Runbook authoring rules

### A runbook is “mergeable” only if it includes
- **Scope** (what it changes / what it doesn’t)
- **Prereqs** (permissions, backups, tools, access)
- **Risk level** + blast radius
- **Step-by-step procedure**
- **Rollback plan** (with explicit triggers)
- **Verification checklist**
- **Evidence capture instructions**
- **Definition of Done** aligned to promotion gates

### Use the standard template
If `_template.md` exists, copy it for all new upgrade runbooks. If it does not exist yet, create it first.

<details>
<summary><strong>Suggested runbook template (copy/paste)</strong></summary>

```markdown
# Upgrade Runbook: <component>

## Summary
- Component:
- From:
- To:
- Why:
- Risk level:
- Environments:
- Owners:

## Preconditions
- Backups/snapshots:
- Access/permissions:
- Maintenance window:
- Dependencies checked:

## Rollback plan
- Rollback triggers:
- Rollback procedure:
- Rollback verification:

## Steps
1.
2.
3.

## Verification
- Smoke tests:
- Contract tests:
- Dashboards/alerts:
- Data validation:

## Evidence & provenance
- PR link:
- Artifact digests:
- CI run IDs:
- Logs / dashboards:
- Change record path:

## Post-upgrade actions
- Cleanup:
- Follow-ups / tech debt:
```
</details>

---

## Change records

Every upgrade must have a **change record** stored under `records/`:

- **Append-only** (no rewriting history; corrections are addenda)
- Includes PR link(s), artifact digests, verification results, and rollback evidence (if triggered)

<details>
<summary><strong>Minimum change record fields</strong></summary>

- Change ID (date + component + from/to)
- Environments executed (dev/stage/prod)
- Approvals (who/when)
- Preconditions completed (backup IDs, snapshots)
- Promotion sequence (timestamps)
- Verification results (tests + dashboards)
- Outcome (success / rollback / partial)
- Follow-ups (issues created)
</details>

---

## Break-glass upgrades

Break-glass is allowed **only** when delay creates unacceptable risk (e.g., active security incident).

Break-glass still requires:
- a recorded decision (timestamp, reason, approver)
- a retroactive PR within the shortest reasonable window
- a completed change record with evidence

> [!WARNING]
> “Break-glass” is not a shortcut for skipping gates—it is a controlled deviation with stronger documentation.

---

## Related documentation

- Platform reliability runbooks (retries, triggers, incident patterns)
- Governance/policy packs (OPA/Rego, Conftest suites)
- Provenance/citation standards (STAC/DCAT/PROV alignment)
- CI/CD promotion lane docs (required checks, environment protections)
