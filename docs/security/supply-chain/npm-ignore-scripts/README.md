---
title: "🛡️ KFM v11.2 — npm Supply-Chain Hardening: ignore-scripts Safeguard (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
path: "docs/security/supply-chain/npm-ignore-scripts/README.md"

version: "v11.2.2"
last_updated: "2025-11-27"
release_stage: "Stable / Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Security Engineering · FAIR+CARE Council Oversight"
content_stability: "stable"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256-of-this-file>"
doc_uuid: "urn:kfm:docs:security:npm-ignore-scripts:v11.2.2"
semantic_document_id: "kfm-security-npm-ignore-scripts"
event_source_id: "ledger:docs/security/supply-chain/npm-ignore-scripts/README.md"
immutability_status: "version-pinned"

sbom_ref: "../../../../releases/v11.2.2/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.2/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.2/security-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/security-npm-ignore-scripts-v11.2.json"
energy_schema: "../../../../schemas/telemetry/energy-v2.json"
carbon_schema: "../../../../schemas/telemetry/carbon-gco2e-v1.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"
license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.2"

status: "Active / Enforced"
doc_kind: "Standard"
intent: "security-npm-ignore-scripts-safeguard"
fair_category: "F1-A2-I1-R1"
care_label: "CARE · Protecting Community Infrastructure"

machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA+"
classification: "Public"
jurisdiction: "Kansas / United States"
lifecycle_stage: "stable"
ttl_policy: "Annual review"
sunset_policy: "Superseded by next supply-chain hardening revision"

layout_profiles:
  - "immediate-one-branch-with-descriptions-and-emojis"
badge_profiles:
  - "root-centered-badge-row"
requires_purpose_block: true
requires_directory_layout_section: true
requires_version_history: true
requires_governance_links_in_footer: true
---

<div align="center">

# 🛡️ **npm Supply-Chain Hardening — ignore-scripts Safeguard**  
`docs/security/supply-chain/npm-ignore-scripts/README.md`

**Purpose**  
Define the **mandatory KFM v11.2.2 standard** for disabling npm lifecycle scripts (`preinstall`, `install`, `postinstall`, `prepare`, etc.) in **CI, release, and autonomous update pipelines**, removing an entire class of supply-chain attacks from KFM’s build surface.

</div>

---

## 📘 Overview

### Why This Exists

npm packages can execute arbitrary code via lifecycle hooks at install time. Compromised packages often hide:

- Credential exfiltration  
- Process spawning and backdoors  
- Environment scraping  
- Persistence mechanisms  

KFM’s CI environments can hold:

- Ephemeral credentials  
- lakeFS branch tokens  
- STAC signing keys  
- Access to data planes and internal APIs  

Therefore, **no npm lifecycle scripts are allowed to execute in CI or automated headless environments**.

The enforcement mechanism is the global use of **`ignore-scripts`**, at both environment and command levels.

---

## 🗂️ Directory Layout

This directory contains the policy, examples, and validation hooks for this safeguard:

```text
📁 docs/
└── 📁 security/
    └── 📁 supply-chain/
        └── 📁 npm-ignore-scripts/
            ├── 📄 README.md             — This file
            ├── 📄 policy.md             — Formal v11.2 policy definition
            ├── 📁 examples/             — CI snippets for major CI platforms
            │   ├── 📄 github-actions.yml
            │   ├── 📄 gitlab-ci.yml
            │   └── 📄 gitea-actions.yml
            ├── 📁 validation/           — Automated checks and audits
            │   ├── 📄 policy-check.json
            │   └── 📄 ci-audit.gx       — Great Expectations / custom rule for compliance
            └── 📁 metadata/
                ├── 📄 dcat.jsonld       — DCAT metadata describing this control
                └── 📄 provenance.json   — PROV-O lineage for policy + enforcement
```

---

## 🧭 Security Model

### Threat Surface

Attack vector:

- Malicious or hijacked npm package with code in:
  - `preinstall`, `install`, `postinstall`, `prepare`, `prepublishOnly`, etc.

Impact:

- Running arbitrary code within CI:
  - Accessing secrets/env  
  - Escaping containers (depending on runtime)  
  - Tampering with build artifacts  
  - Backdooring dependencies  

### Mitigation Strategy

KFM’s mitigation is **surgical and total** in CI:

- For npm, we treat `node_modules` installation as **pure file materialization**:
  - No scripts  
  - No user-defined hooks  
  - No code execution, only package extraction  

This is implemented via:

- Environment variables (`NPM_CONFIG_IGNORE_SCRIPTS`, `npm_config_ignore_scripts`)  
- CLI flags (`--ignore-scripts`)  
- Continuous validation that these settings are present and unchanged.

---

## 🧪 CI Integration

### GitHub Actions (Canonical Example)

```yaml
env:
  NPM_CONFIG_IGNORE_SCRIPTS: "true"

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Use Node
        uses: actions/setup-node@v4
        with:
          node-version: "20.x"

      - name: Install dependencies (scripts disabled)
        run: npm ci --ignore-scripts

      - name: Run tests
        run: npm test
```

### GitLab CI

```yaml
variables:
  NPM_CONFIG_IGNORE_SCRIPTS: "true"

stages:
  - build

build_app:
  stage: build
  image: node:20
  script:
    - npm ci --ignore-scripts
    - npm test
```

### Gitea Actions

```yaml
env:
  npm_config_ignore_scripts: "true"

jobs:
  build:
    runs-on: docker
    steps:
      - uses: actions/checkout@v4
      - run: npm ci --ignore-scripts
      - run: npm test
```

### Enforcement Rules

- Any CI workflow that uses `npm install` **MUST** include the `--ignore-scripts` flag.  
- Any environment running CI jobs **MUST** define `NPM_CONFIG_IGNORE_SCRIPTS=true` (or equivalent).  
- Policy defaults:
  - **Disallow** `npm install` without `--ignore-scripts` in CI.  
  - **Prefer** `npm ci` for reproducibility.

Deviation is treated as a **policy violation** and triggers:

- Pipeline failure  
- Security telemetry emission  
- Governance alert (Security Engineering + FAIR+CARE Council)  

---

## 🧱 Policy.md (Normative Summary)

The `policy.md` file in this directory encodes the normative statements, including:

- **MUST NOT** run npm lifecycle scripts in:
  - CI  
  - release pipelines  
  - automated update tasks  
- **MUST** use environment-level ignore-scripts + CLI flags.  
- **MAY** allow lifecycle scripts locally on developer machines, **never** in CI.

Local dev is allowed to differ from CI because:

- Threat surface differs (personal environment vs shared CI).  
- CI is where signed artifacts and releases are produced.  

---

## 🧪 Validation & Auditing

The `validation/` directory includes:

- `policy-check.json` — declarative rule set describing required env vars and flags.  
- `ci-audit.gx` — a test definition (e.g., Great Expectations or custom rule) that:

  - Parses CI workflow YAML (`.github/workflows/*.yml`, etc.).  
  - Verifies presence of:
    - `NPM_CONFIG_IGNORE_SCRIPTS` or `npm_config_ignore_scripts`.  
    - `npm ci --ignore-scripts` or equivalent.  
  - Emits pass/fail status.

These validations are integrated into KFM CI:

- `security-npm-ignore-scripts-check` job runs on any PR that changes:
  - `package.json`  
  - `package-lock.json` / `pnpm-lock.yaml` / `yarn.lock`  
  - CI configs under `.github/workflows/`, `.gitea/workflows/`, `.gitlab-ci.yml`  
- On failure:
  - The PR is blocked.  
  - A security audit entry is written to security telemetry.

---

## 🛠️ Local Development Guidance

Local developers:

- **Can** temporarily run installs with scripts to satisfy build requirements (e.g., native modules).  
- **Must not** modify CI configs to enable scripts.  
- **Should** prefer to test with `--ignore-scripts` where possible to mimic CI behavior.

Local enabling example (for debugging only):

```bash
npm_config_ignore_scripts=false npm install
```

This MUST NOT appear in committed CI scripts.

---

## 📊 Telemetry & Reporting

All enforcement data is written into security telemetry:

- Success/failure of policy checks.  
- Instances where a CI job attempted to run npm lifecycle scripts.  
- Frequency of violations per repo/branch.  
- Trends over releases.

Telemetry target:

```text
releases/v11.2.2/security-telemetry.json
```

Example JSON entry:

```json
{
  "event": "npm_ignore_scripts_enforcement",
  "timestamp": "2025-11-27T18:32:00Z",
  "workflow": "ci-build.yml",
  "status": "pass",
  "violations_detected": 0
}
```

When a violation occurs:

```json
{
  "event": "npm_ignore_scripts_enforcement",
  "timestamp": "2025-11-27T19:04:00Z",
  "workflow": "ci-build.yml",
  "status": "fail",
  "violations_detected": 1,
  "details": "npm install without --ignore-scripts in job build_app"
}
```

---

## 🧠 Story Nodes & Focus Mode Integration

This safeguard feeds into security Story Nodes and Focus Mode views:

- **“Shielded Builds”** — Story Node detailing CI hardening steps, including ignore-scripts.  
- **“Supply-Chain Risk Timeline”** — Focus Mode timeline of security improvements over releases.  
- **“Lifecycle Script Audit”** — Node highlighting attempted script executions and how they were blocked.

This gives governance and contributors **clear visibility** into the evolution and impact of supply-chain controls.

---

## 🕰️ Version History

| Version | Date       | Summary                                                                                             |
|--------:|------------|-----------------------------------------------------------------------------------------------------|
| v11.2.2 | 2025-11-27 | Upgraded to KFM-MDP v11.2.2; fully normalized layout; clarified CI examples; added telemetry schema hook. |
| v11.2.0 | 2025-11-27 | Initial KFM super-standard release for npm ignore-scripts safeguard; integrated into core CI.       |
| v11.1.x | 2025-11-20 | Experimental policy in isolated security runs; not enforced globally.                               |
| v10.x   | 2025-11-10 | Partial lifecycle-script hardening in selected pipelines.                                           |

---

<div align="center">

🛡️ **KFM v11.2 — npm Supply-Chain Hardening: ignore-scripts Safeguard**  
Secure builds · No hidden scripts · Reproducible dependency installs.

© 2025 Kansas Frontier Matrix — MIT  
MCP-DL v6.3 · KFM-MDP v11.2.2 · FAIR+CARE Council  

[⬅ Back to Security Index](../../README.md) ·  
[⚖ Root Governance Charter](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>
