---
title: "🤖 KFM — Tiny PR Bot (JWT→Install Token · Idempotent Fixer · OpenLineage/PROV Emissions)"
path: ".github/apps/kfm-pr-bot/README.md"
version: "v11.2.6"
last_updated: "2025-12-14"

release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Reliability & FAIR+CARE Council"
content_stability: "stable"

status: "Active / Canonical"
doc_kind: "Runbook"
header_profile: "standard"
footer_profile: "standard"
intent: "kfm-ci-pr-bot-mini"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.6"
ontology_protocol_version: "KFM-OP v11"
pipeline_contract_version: "KFM-PDC v11"
stac_profile: "KFM-STAC v11"
dcat_profile: "KFM-DCAT v11"
prov_profile: "KFM-PROV v11"
openlineage_profile: "OpenLineage v2.5 · CI/CD and AI pipeline events"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

semantic_document_id: "kfm-ci-pr-bot-mini"
doc_uuid: "urn:kfm:ci:pr-bot:mini:v11.2.6"
event_source_id: "ledger:.github/apps/kfm-pr-bot/README.md"
immutability_status: "version-pinned"

governance_ref: "../../../docs/standards/governance/ROOT-GOVERNANCE.md"
ethics_ref: "../../../docs/standards/faircare/FAIRCARE-GUIDE.md"
sovereignty_policy: "../../../docs/standards/sovereignty/INDIGENOUS-DATA-PROTECTION.md"
security_ref: "../../../SECURITY.md"

telemetry_schema: "../../../schemas/telemetry/github-workflows-v4.json"
lineage_schema: "../../../schemas/lineage/prov-o-jsonld-v11.json"
openlineage_schema: "../../../schemas/lineage/openlineage-v1beta.json"
energy_schema: "../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../schemas/telemetry/carbon-v2.json"

reprokit_ref: "../../repro-kit/README.md"

classification: "Public Document"
sensitivity: "General (operational patterns; no secrets)"
sensitivity_level: "None"
public_exposure_risk: "Low"
risk_category: "Low to Medium (automation + credentials)"
indigenous_rights_flag: "Dataset-level"
redaction_required: true

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"
---

<div align="center">

# 🤖 **KFM — Tiny PR Bot**
`.github/apps/kfm-pr-bot/README.md`

**Purpose**  
A tiny, production-safe GitHub App that authenticates via **JWT → installation token**, runs deterministic **validate/fix** routines, performs **idempotent writes**, and emits **OpenLineage + PROV‑O JSON‑LD** for every run.

</div>

---

## 📘 Overview

The Tiny PR Bot is intentionally minimal so it can be adopted quickly inside KFM CI without widening risk surface.

It supports four outcomes, in order of preference:

1. **No-op**: validation passes, nothing to change.
2. **Suggest**: validation fails; bot posts a structured report without writing.
3. **Fix**: validation fails; bot applies deterministic transforms and opens/updates a PR.
4. **Quarantine**: policy prevents safe write (permissions, sensitive paths, governance gate); bot emits evidence and stops.

Primary use cases in KFM:

- Docs hygiene aligned with KFM-MDP (front-matter coherence, fence rules, directory tree formatting).
- Small deterministic normalizations (formatting, ordering, schema-safe rewrites).
- Evidence emission to make automation auditable (OpenLineage + PROV).

Non-goals:

- Publishing datasets, modifying governance status, or bypassing required reviews.
- Performing non-deterministic edits or “creative” refactors.
- Running privileged operations in forked PRs.

---

## 🧭 Context

The bot exists inside the `.github/` subsystem and is governed like any other automation component.

KFM pipeline relationship:

- Bot runs in CI contexts and contributes to the “governance and automation fabric.”
- It must never introduce ungoverned changes into:
  - `data/**` publish surfaces,
  - sovereignty-protected content,
  - or release packets.

Evidence relationship:

- Every run emits:
  - OpenLineage event JSON (execution-level lineage)
  - PROV-O JSON-LD (logical provenance)
- Runs that fail in unexpected ways should follow the repo repro-kit pattern:
  - `.github/repro-kit/README.md`

---

## 🗂️ Directory Layout

Canonical layout for this app folder:

~~~text
📁 .github/
└── 📁 apps/
    └── 📁 kfm-pr-bot/
        ├── 📄 README.md                         # This runbook
        ├── 🧾 app.yml                           # GitHub App descriptor (scopes, webhooks)
        ├── 📁 src/
        │   ├── 🧠 app.ts                        # Single webhook handler (pull_request, push, check_suite)
        │   ├── 🔐 auth.ts                       # JWT → installation token
        │   ├── 🧰 gh.ts                         # Thin GitHub API client (retry + jitter + rate handling)
        │   ├── 📁 ruleset/
        │   │   ├── ✅ validator.ts              # Deterministic validation → stable decision + diff plan
        │   │   └── 🛠️ fixer.ts                  # Deterministic transforms (pure, replayable)
        │   ├── ♻️ idempotency.ts                # Branch/PR keys derived from inputs + hashes
        │   ├── 📁 lineage/
        │   │   ├── 🧬 prov.ts                   # PROV-O JSON-LD emitter
        │   │   └── 🧾 openlineage.ts            # OpenLineage event emitter
        │   └── 🧾 logging.ts                    # Structured logs (no secrets)
        ├── 📁 var/
        │   └── 📁 dlq/
        │       └── 🧾 run-<timestamp>-<uuid>.json  # Failed-run envelopes (privacy-safe)
        └── 📁 configs/
            └── ⚙️ ruleset.yaml                  # Rules toggles (KFM-MDP checks, allowlist/denylist)
~~~

Directory layout rules:

- All writes by the bot MUST be attributable and bounded by:
  - `configs/ruleset.yaml`,
  - and the repo’s governance constraints.
- The DLQ MUST contain sanitized envelopes only (no secrets, no raw PII).

---

## 🧱 Architecture

### Single-handler pattern

The bot is implemented as a single webhook handler that routes to a deterministic ruleset:

1. **Receive event** (`pull_request`, `push`, `check_suite`)
2. **Resolve repo context**
   - repository, branch/ref, SHA(s), changed files list
3. **Select ruleset**
   - based on changed file paths and intent routing
4. **Validate**
   - compute stable decision + diff plan
5. **Fix (optional)**
   - apply deterministic transforms to a controlled branch
6. **Report**
   - PR comment and/or check run summary
7. **Emit lineage**
   - OpenLineage + PROV outputs for every run
8. **DLQ on failure**
   - persist a sanitized envelope for replay

### Authentication pattern

- GitHub App private key signs a **JWT**
- JWT exchanged for an **installation token**
- Installation token used for GitHub API calls

Hard constraints:

- Tokens MUST be short-lived.
- Private key MUST never be written to logs, DLQ, or PR comments.
- If authentication fails, bot must fail closed and emit evidence.

### Idempotency contract

Idempotency prevents spam, avoids infinite fix loops, and enables stable replay.

Deterministic keys:

- **Branch name**
  - `kfm/bot/{intent}/{content-hash-8}`
- **PR title**
  - `[KFM Bot] {intent}: {content-hash-8}`
- **PR body**
  - includes a provenance block with:
    - run UUID
    - commit SHA
    - evidence paths/hrefs (no secrets)

Stable hashing inputs (recommended minimum):

- target SHA
- list of changed file paths (sorted)
- ruleset version string
- bot version string

---

## 🧪 Validation & CI/CD

### What the bot is allowed to modify

Allowed (typical safe set):

- Markdown structure and formatting consistent with KFM-MDP:
  - fence normalization
  - directory-tree formatting and emoji alignment
  - front-matter key normalization (order/required keys, when schema-safe)
- Non-executable metadata files when explicitly allowlisted in `ruleset.yaml`

Not allowed:

- Anything that changes dataset meaning, governance status, or policy.
- Any changes that introduce new data sources or assets into `data/raw/**`.
- Anything under protected paths unless explicitly approved and code-owned.

### Retry and backoff behavior

All GitHub API calls MUST use:

- exponential backoff
- full jitter
- rate-limit awareness (respect `Retry-After` and secondary rate limits)

### DLQ behavior

On unexpected failures:

- write one DLQ envelope to `var/dlq/`
- envelope MUST include:
  - event type
  - repo/ref/SHA
  - ruleset id/version
  - error class + message (sanitized)
  - correlation ids (run_id, installation_id if safe)
- envelope MUST NOT include:
  - private key
  - installation token
  - raw request bodies containing secrets

---

## 📦 Data & Metadata

### Run envelope (internal model)

A run is fully described by a stable envelope:

- `run_id` (uuid/ulid)
- `event_name`
- `repo_full_name`
- `ref`
- `head_sha`
- `base_sha` (if PR)
- `changed_files[]` (sorted)
- `intent`
- `ruleset_version`
- `content_hash`
- `decision` ∈ {`noop`,`suggest`,`fix`,`quarantine`,`error`}
- `outputs` (paths or artifact hrefs)
- `metrics` (timings, counts, API calls, backoff stats)

### Ruleset configuration (`configs/ruleset.yaml`)

A ruleset file SHOULD include:

- allowlist paths
- denylist paths
- intents (routing)
- fix toggles (enable/disable by intent)
- maximum write set size (files, bytes)
- comment templates (no secrets)

Example skeleton:

~~~yaml
version: "1"
intents:
  - name: "mdp-fix"
    allow_globs:
      - "docs/**/*.md"
      - ".github/**/*.md"
    deny_globs:
      - "data/**"
    autofix: true
    max_files: 50
    max_bytes: 2000000
~~~

---

## 🌐 STAC, DCAT & PROV Alignment

This bot does not publish STAC/DCAT datasets directly. Its primary metadata integration is lineage:

### OpenLineage (execution-level)

Job naming (recommended):

- namespace: `kfm.ci`
- name: `kfm-pr-bot.mini`

Nominal time:

- for PR events: PR updated window (event time is authoritative)
- for push events: commit time window (event time is authoritative)

Example event skeleton:

~~~json
{
  "eventType": "COMPLETE",
  "eventTime": "2025-12-14T00:00:00Z",
  "job": { "namespace": "kfm.ci", "name": "kfm-pr-bot.mini" },
  "run": {
    "runId": "00000000-0000-0000-0000-000000000000",
    "facets": {
      "nominalTime": { "startTime": "2025-12-14T00:00:00Z", "endTime": "2025-12-14T00:00:05Z" },
      "kfmBot": {
        "intent": "mdp-fix",
        "decision": "fix",
        "content_hash_8": "deadbeef"
      }
    }
  },
  "inputs": [],
  "outputs": []
}
~~~

### PROV-O (logical provenance)

- The run is a `prov:Activity`.
- The bot is a `prov:SoftwareAgent`.
- Inputs include:
  - the repository commit(s) and changed files list
  - the ruleset configuration version
- Outputs include:
  - the created/updated branch and PR metadata
  - the diff artifact hash (if captured)
  - evidence JSON locations

Example skeleton:

~~~json
{
  "@context": "https://www.w3.org/ns/prov.jsonld",
  "@id": "urn:kfm:activity:ci:pr-bot-mini:run:<run_id>",
  "@type": "prov:Activity",
  "prov:startedAtTime": "2025-12-14T00:00:00Z",
  "prov:endedAtTime": "2025-12-14T00:00:05Z",
  "prov:wasAssociatedWith": {
    "@id": "urn:kfm:agent:software:kfm-pr-bot-mini",
    "@type": "prov:SoftwareAgent"
  }
}
~~~

---

## ⚖ FAIR+CARE & Governance

Governance is enforced through three mechanisms:

1. **Path gating**
   - denylist high-risk areas by default (e.g., `data/**`)
2. **Review gating**
   - bot PRs are still subject to CODEOWNERS and required checks
3. **Evidence emission**
   - every run produces auditable lineage

Fail-closed rules:

- If policy cannot determine safety, bot must quarantine and emit evidence.
- If a change would affect sovereignty-protected content, bot must stop and request steward review.

---

## 🕰️ Version History

| Version | Date       | Summary |
|--------:|------------|---------|
| v11.2.6 | 2025-12-14 | Standardized Tiny PR Bot runbook for KFM-MDP v11.2.6; emoji-aligned directory layout; clarified single-handler architecture, idempotency contract, retry/jitter, DLQ safety, and OpenLineage/PROV emission expectations. |

---

<div align="center">

🤖 **KFM — Tiny PR Bot (v11.2.6)**  
Deterministic Fixes · Idempotent Writes · Evidence-First Automation

[⬅ Back to `.github/` Overview](../../README.md) ·
[🧳 Repro-Kit Pattern](../../repro-kit/README.md) ·
[⚖ Governance Charter](../../../docs/standards/governance/ROOT-GOVERNANCE.md) ·
[🤝 FAIR+CARE Guide](../../../docs/standards/faircare/FAIRCARE-GUIDE.md) ·
[🛡 Security Policy](../../../SECURITY.md)

</div>
