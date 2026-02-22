# Issue templates
Map-first, time-aware, governed issue intake for Kansas Frontier Matrix (KFM).

**Status:** Active  
**Owners:** Repo maintainers + governance reviewers (see repository ownership / CODEOWNERS if configured)  
**Principles:** **Map-first** • **Time-aware** • **Governed** • **Evidence-first** • **Cite-or-abstain**

Quick nav: [When to file an issue](#when-to-file-an-issue) • [Choose the right template](#choose-the-right-template) • [What we require in every issue](#what-we-require-in-every-issue) • [Sensitive info rules](#sensitive-info-rules) • [Triage flow](#triage-flow) • [Maintainer notes](#maintainer-notes)

---

## When to file an issue

Use GitHub Issues for **trackable work** that should land as code, data, policy, or documentation changes, including:

- **Bugs / regressions** (UI, map, API, pipeline, indexing, search, Focus Mode)
- **Enhancements / feature requests** (small, testable increments preferred)
- **Data intake / dataset publication** requests (source → pipeline → catalog → publish)
- **Governance / policy decisions** (labels, redaction rules, release gates)
- **Performance / reliability** issues (timeouts, memory, latency, cost spikes)
- **Documentation gaps** that change behavior or governance

If your report is a **security vulnerability**, do **not** open a public issue. Use the repo’s private/security reporting path (e.g., GitHub Security Advisories) if available.

---

## Choose the right template

Pick the template that best matches your intent. If you’re unsure, choose the closest match and we’ll re-route during triage.

| You want to… | Use template | Typical outputs |
|---|---|---|
| Report something broken | **Bug report** | Repro steps, expected vs actual, fix PR |
| Propose a capability | **Feature request / Enhancement** | Scoped spec, acceptance criteria, design notes |
| Add/refresh a data source | **Data source request** | Source metadata, license, sensitivity label, ingestion plan |
| Fix/diagnose pipeline problems | **Pipeline issue** | Run receipt(s), logs, failing step, remediation |
| Publish/promote a dataset | **Dataset promotion / release** | Promotion checklist, validation results, checksums |
| Create/modify a map story | **Story node request** | Story intent, evidence bundle, time bounds, redaction notes |
| Make a policy decision | **Governance / policy decision** | Decision record, reviewers, enforcement plan |
| Improve performance | **Performance** | Baselines, profiling, target SLO/SLA, verification steps |

> NOTE: If your repo disables “blank issues”, you’ll need to pick a template. If “blank issues” are allowed, use them only for truly unusual cases.

---

## What we require in every issue

To keep KFM **buildable, reversible, and governed**, every issue should include:

### 1) Clear intent + scope
- **What is the user/system impact?**
- **What is in scope / out of scope?**
- **What does “done” look like?** (acceptance criteria)

### 2) Evidence (show, don’t tell)
Provide at least one of:
- Screenshots / screen recordings
- Logs / stack traces (redacted if needed)
- Links to code paths or commits
- Dataset identifiers, version IDs, checksums (if applicable)
- “Run receipt” / audit record ID(s) (if your pipelines emit them)

### 3) Time-awareness (when relevant)
If your issue concerns events, data validity, or “latest” results, include as applicable:
- **Event time:** when something happened in the world
- **Valid time:** the period the data is true for
- **Transaction time:** when it entered/changed in the system
- Use **explicit dates** (YYYY-MM-DD) instead of “today/yesterday”

### 4) Governance tags (when relevant)
If the issue touches data/public narratives/sensitive locations:
- Proposed **policy label** (e.g., public / restricted / culturally sensitive / internal)
- Proposed **redaction/generalization** (if locations or people are involved)
- **License/consent** details for any new data or media

---

## Sensitive info rules

Default-safe behavior is required.

**Do not include:**
- Exact coordinates or precise directions to **culturally restricted sites**, sensitive habitats, or vulnerable infrastructure
- Personal data about private individuals (names, addresses, contact info) unless you have explicit permission and a governance-approved reason
- Secrets (API keys, tokens), internal URLs, or private system details

**Do include instead:**
- Generalized locations (county/region) or coarse bounding boxes
- Redacted screenshots/logs (blur/replace)
- A note that details can be provided via an approved private channel

---

## Triage flow

```mermaid
flowchart TD
  A[New Issue] --> B{Template fits?}
  B -->|Yes| C[Auto-labels / metadata]
  B -->|No| D[Re-route to correct template]
  C --> E{Sensitive?}
  D --> E
  E -->|Yes| F[Apply policy label + redact request]
  E -->|No| G[Standard triage]
  F --> H[Assign owner + reviewers]
  G --> H
  H --> I[Define acceptance criteria + tests/gates]
  I --> J[Work: PRs / pipeline runs / ADRs]
  J --> K[Verification: evidence + checks]
  K --> L[Close + link artifacts]
