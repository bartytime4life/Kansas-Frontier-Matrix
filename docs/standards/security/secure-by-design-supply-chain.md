---
title: "🧬 KFM v11.2.3 — Secure-by-Design Guide for Supply Chain & Developer Environments (Diamond⁹ Ω / Crown∞Ω Ultimate Certified)"
description: "Secure-by-design guardrails for KFM repositories, dev environments, CI/CD, and production runtime to defend against malicious extensions, package worms, and supply-chain attacks."
path: "docs/standards/security/secure-by-design-supply-chain.md"
version: "v11.2.3"
last_updated: "2025-12-03"

release_stage: "Stable · Governed"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Platform & Security · FAIR+CARE Council"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x security-guidance compatible"

commit_sha: "<latest-commit-hash>"
previous_version_hash: "<previous-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../releases/v11.2.3/sbom.spdx.json"
manifest_ref: "../../releases/v11.2.3/manifest.zip"
telemetry_ref: "../../releases/v11.2.3/security-supply-chain-telemetry.json"
telemetry_schema: "../../schemas/telemetry/security-supply-chain-v1.json"
governance_ref: "../governance/ROOT-GOVERNANCE.md"

license: "MIT"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.3"

doc_kind: "Security Standard"
intent: "secure-by-design-supply-chain"

fair_category: "F1-A1-I1-R1"
care_label: "CARE-Compliant"
sensitivity: "General"
sensitivity_level: "Low"
indigenous_data_flag: false
public_benefit_level: "High"
risk_category: "Moderate"
redaction_required: false

ontology_alignment:
  schema_org: "TechArticle"
  cidoc: "E29 Design or Procedure"
  prov_o: "prov:Plan"
  owl_time: "TemporalEntity"
  geosparql: "geo:FeatureCollection"

json_schema_ref: "../../schemas/json/standards-secure-by-design-supply-chain-v1.json"
shape_schema_ref: "../../schemas/shacl/standards-secure-by-design-supply-chain-v1.shape.ttl"

immutability_status: "version-pinned"
machine_extractable: true
accessibility_compliance: "WCAG 2.1 AA"

ttl_policy: "24 Months"
sunset_policy: "Superseded on next major secure-by-design standard revision"
---

<div align="center">

# 🧬 Secure-by-Design Guide for KFM Supply Chain & Developer Environments  
`docs/standards/security/secure-by-design-supply-chain.md`

**Purpose:**  
Define **practical, enforceable guardrails** for KFM repositories, dev environments, CI/CD, and production runtime to defend against:

- Malicious IDE extensions  
- npm/Maven/PyPI worms and compromised packages  
- Supply-chain attacks targeting CI/CD and build systems  

Design assumption for KFM:  
> Anything from public ecosystems (extensions, packages, images, actions) is **untrusted** until explicitly vetted and locked down.

</div>

---

## 1. Why This Matters (KFM Threat Model)

Recent industry incidents have shown that:

- VS Code / OpenVSX extensions can be weaponized (themes, icons, “utility” extensions) and distributed via trusted marketplaces.  
- npm ecosystems have carried large-scale malware campaigns (worm-style behavior, credential theft, lateral movement).  
- Maven/Java ecosystems are also targets; payloads can be **cross-language** and **multi-ecosystem**.  
- Attackers increasingly:
  - Hide payloads in install scripts (`preinstall`, `postinstall`, `prepare`, etc.).  
  - Abuse developer machines, CI runners, and GitHub Actions to steal tokens and secrets.  
  - Use compromised packages/extensions as **worm vectors** into more repos and environments.

For KFM, this means:

- Dev machines and CI agents are **high-value targets** because they bridge code, secrets, and cloud infra.  
- Supply-chain controls are as important as traditional perimeter/network security.

This standard lays out guardrails to bake the “untrusted by default” assumption into how we **build, run, and maintain** KFM.

---

## 2. Core Security Principles

1. **Minimal & Audited Dependencies**  
   - Fewer packages, fewer extensions, fewer actions → smaller attack surface.

2. **Immutable & Reproducible Builds**  
   - Pin versions; hash-lock; use artifact registries and SBOMs.

3. **Strong Identity & Least Privilege**  
   - Short-lived, scoped tokens; avoid long-lived, wide-open secrets.

4. **Deny by Default for Tools & Extensions**  
   - Use **allowlists**, not denylists.

5. **Detect & Recover Fast**  
   - Logs, alerts, incident playbooks, and rollback paths ready **before** you need them.

These principles must be reflected in:

- Repo policies  
- CI/CD configuration  
- Infrastructure documentation  
- Developer onboarding and reviews

---

## 3. Development Environment Guardrails

### 3.1 VS Code / IDE Extensions

**Goal:** Prevent a malicious extension (or update) from exfiltrating KFM secrets or compromising dev machines.

**Controls:**

- **Extension Allowlist**
  - Maintain an internal list:
    - ✅ **Allowed**: pre-reviewed, pinned extensions.  
    - 🚫 **Forbidden**: high-risk types (obfuscated themes, “productivity boosters” from unknown publishers).
  - Enforce via:
    - Organization policies (VS Code Enterprise / Settings Sync) where possible.  
    - Written policy + periodic audits where central enforcement is not available.

- **Pinned Versions & Internal Mirrors**
  - For critical extensions:
    - Pin to a known safe version.  
    - Mirror VS Code extensions internally (OpenVSX proxy or internal artifact system).  
    - Install only from internal mirrors, not from the public marketplace when touching sensitive repos.

- **Review Before Install**
  - Check:
    - Publisher reputation & history.  
    - Changelog for sudden large updates.  
    - Presence of obfuscated JS or embedded native binaries.
  - Do **not** install if:
    - Extension requests broad system access without clear justification.  
    - The project/repo is new with minimal history.  

- **No Secrets in Workspace**
  - Assume the IDE can read everything in the workspace.  
  - Organize KFM secrets so **most secrets never sit on dev machines**:
    - Use central secret stores.  
    - Restrict local dev to low-scope tokens (see §6).

---

### 3.2 Local Package Management (npm, Maven, Python, etc.)

**Target ecosystems:** npm/pnpm/yarn, Maven/Gradle, Python, etc.

**Controls:**

- **Private Registry / Proxy**
  - Route all dependency downloads through:
    - An internal registry (e.g., Artifactory, Nexus, Verdaccio), or  
    - A strict proxy with:
      - Allowlisted upstreams.  
      - Download logging and anomaly alerts.
  - Developers should **not** install directly from public registries for production KFM codebases.

- **Lockfiles Are Required**
  - Enforce presence of:
    - `package-lock.json`, `pnpm-lock.yaml`, `yarn.lock`.  
    - `pom.xml` with explicit versions (no `LATEST`, no `+`).  
  - CI should **fail** if:
    - Lockfile is missing or out of sync with `package.json`.  
    - Versions are floating (e.g., `^` or `~`) in production services.

- **Disable Dangerous Lifecycle Scripts in CI**
  - By default, disallow or heavily constrain:
    - `preinstall`, `postinstall`, `prepare`, `prepublish`, etc.
  - Patterns:
    - Use `npm install --ignore-scripts` (or equivalent) in CI.  
    - Maintain a small allowlist of packages that genuinely require install scripts (e.g., native addons) and run them in **isolated build containers**.

- **Static & Behavioral Scanning**
  - Integrate into CI:
    - Dependency scanning (SCA).  
    - Secret scanning.  
    - Binary/obfuscation detection.
  - Block merges when:
    - New dependency appears with red flags:
      - Tiny / empty repo.  
      - Recently created.  
      - Obfuscated code payloads.  
      - Suspicious install scripts making network calls.

---

## 4. CI/CD Pipeline Hardening

CI/CD is a prime target: it holds tokens and can modify many repos and environments.

### 4.1 CI Design Rules

- **Ephemeral Runners**
  - Use short-lived runners/agents.  
  - After every job:
    - No persistent workspace.  
    - No cached credentials in home directories.

- **Scoped & Short-Lived Tokens**
  - GitHub/GitLab tokens:
    - Minimize scopes (read-only where possible).  
    - Use environment-specific service principals/roles.
  - Cloud keys:
    - Prefer OIDC-based access from CI to cloud IAM instead of static long-lived keys.

- **No Direct Push from CI to Public Repos**
  - If CI must push:
    - Use low-privilege bot accounts.  
    - Restrict which branches and repos they can modify.

- **Network Egress Controls**
  - CI jobs should **not** freely call the entire internet.
  - Allowlist:
    - Internal artifact registries.  
    - Explicit third-party endpoints required for the job.
  - Alert on:
    - Unexpected outbound connections.  
    - Data exfiltration patterns (large uploads to unknown domains).

---

### 4.2 Build Integrity & Attestation

- **Reproducible Builds**
  - Same commit + same inputs → same artifacts.  
  - Avoid “build from HEAD of dependency”.

- **SBOM (Software Bill of Materials)**
  - Generate SBOM per build (CycloneDX, SPDX).  
  - Store SBOM alongside artifacts (container images, JARs, ZIPs).  
  - Use SBOM to:
    - Quickly assess impact of new CVEs.  
    - Identify which services pulled a compromised package.

- **Sign & Verify Artifacts**
  - Sign builds and images (cosign, Sigstore, or cloud-native signing).  
  - Enforce verification at deploy time:
    - Only signed, attested artifacts deployable to staging/prod.

- **SLSA-Inspired Levels**
  - Aim for:
    - Versioned, immutable build definitions.  
    - Non-human, policy-driven releases.  
    - Provenance metadata describing:
      - Source commit.  
      - Build system.  
      - Dependencies.

---

## 5. Production Runtime Protections

Goal: even if supply-chain malware slips through, production should **constrain blast radius**.

Controls:

- **Read-Only File Systems Where Possible**
  - Containers with read-only root filesystems.  
  - Mount only necessary volumes.

- **Least-Privilege Service Accounts**
  - Each service gets:
    - Its own identity (service principal / IAM role).  
    - Minimal roles (no shared “god-mode” account).

- **Outbound Network Controls**
  - Restrict outbound connections per service:
    - Allow only:
      - Known internal services.  
      - Specific external APIs.  
    - Default: block unknown domains/IPs.

- **Runtime Monitoring**
  - Collect:
    - Process executions (unexpected shells, `curl`/`wget`).  
    - Network connections.  
    - Unusual file access patterns.
  - Alert (not just log) on:
    - New or rare outbound IPs.  
    - Processes not in your baseline.

---

## 6. Secrets Management

Supply-chain malware often hunts for **secrets first**.

- **Central Secrets Store Only**
  - Use a managed vault (Vault, cloud KMS/secrets manager).  
  - No secrets hard-coded in:
    - Source code.  
    - Container images.  
    - CI configs (except references to vault).

- **Short-Lived Credentials**
  - Prefer:
    - OIDC, STS, or workload identity over long-lived keys.  
  - If static secrets are unavoidable:
    - Rotate frequently.  
    - Monitor usage.

- **Local Dev: Reduced Blast Radius**
  - Dev machines receive:
    - Low-scope development credentials only.  
  - Maintain clear separation between:
    - Dev vs staging vs production secrets.

---

## 7. Governance for New Dependencies & Extensions

Treat **“add a package”** or **“add an extension”** as a change request, not a casual action.

### 7.1 New Package Checklist (npm / Maven / etc.)

Before merging a PR that adds a new dependency:

1. **Identity & Reputation**
   - Maintainers have visible history?  
   - Repo older than a few weeks?

2. **Source Review**
   - Any obfuscated code?  
   - Any suspicious install/postinstall scripts?

3. **Usage Justification**
   - Why is this package needed?  
   - Could you avoid it or use a standard library instead?

4. **Lock & Mirror**
   - Version pinned.  
   - Added to internal registry/proxy.

5. **Scan & Approve**
   - Security tooling shows no critical issues.  
   - Human reviewer signs off on the risk.

### 7.2 New IDE Extension Checklist

Before installing a new extension on machines that touch **KFM-sensitive repos**:

1. **Confirm:**
   - Publisher is known and credible.  
   - Repo has real code and history.

2. **Review:**
   - Permissions requested.  
   - Changelog for recent large changes.

3. **Pin:**
   - Lock to a specific version if widely used.

4. **Document:**
   - Why it’s needed.  
   - Which teams are allowed to use it.

---

## 8. Detection & Incident Response (Supply-Chain Focus)

When a campaign like a **malicious npm worm** or extension is announced:

### 8.1 Triage

- Check:
  - SBOMs for affected packages.  
  - Extension inventories (which machines installed what).

### 8.2 Containment

- Disable/uninstall suspicious extensions.  
- Revoke and rotate:
  - GitHub / GitLab tokens.  
  - Cloud keys.  
- Temporarily block affected packages in the registry proxy.

### 8.3 Forensics

- Audit logs:
  - CI logs.  
  - Git history (unexpected commits or pushes).  
  - Cloud IAM logs.
- Look for:
  - Unusual outbound connections.  
  - PRs or commits from unexpected accounts.

### 8.4 Recovery

- Rebuild artifacts from known-good commits.  
- Restore credentials using new keys.

### 8.5 Hardening Follow-up

- Turn lessons into:
  - New CI checks.  
  - Updated allowlists/denylists.  
  - Training for developers and SREs.

---

## 9. “Day-Zero Supply-Chain Alert” Quick Playbook

When you hear “new npm/extension malware campaign”:

1. **Freeze**
   - Pause non-critical deploys touching the affected ecosystem.

2. **Identify**
   - Search SBOMs and dependency manifests for affected packages.  
   - Check IDE extension lists.

3. **Isolate**
   - Block known-bad packages/extensions at:
     - Registry proxy.  
     - Extension mirror.

4. **Rotate**
   - Revoke and re-issue any tokens/secrets that may have been exposed.

5. **Scan & Hunt**
   - Check CI and production logs for indicators of compromise (IoCs).

6. **Document**
   - Capture what happened, what was done, and next steps.  
   - Feed findings into this standard and related runbooks.

---

## 10. Operationalizing This Standard in KFM

To make this document **real** in KFM, teams should:

- **Turn sections into ORG policies:**
  - Dependencies (package governance).  
  - IDE extensions (allowlist policy).  
  - CI/CD design rules.  

- **Wire into CI/CD:**
  - Enforce lockfiles and pinned versions.  
  - Enforce `--ignore-scripts` plus allowlist logic.  
  - Require SBOMs and artifact signing for production builds.  
  - Integrate SCA/secret scanning as **blocking** checks.

- **Embed in repo workflow:**
  - Add PR templates:
    - “Did you add a new package? Link to risk assessment (package checklist §7.1).”  
  - Add `SECURITY.md` links back to this standard.

- **Include in onboarding and reviews:**
  - New developer onboarding must cover:
    - IDE extension policy.  
    - Package governance.  
    - CI/CD and secrets handling basics.
  - Security reviews and incident postmortems should reference and update this doc.

---

## 11. Version History

| Version  | Date       | Author                                       | Summary                                                                 |
|----------|------------|----------------------------------------------|-------------------------------------------------------------------------|
| v11.2.3  | 2025-12-03 | Platform & Security WG · FAIR+CARE Council   | Initial secure-by-design supply chain & dev environment standard for KFM; covers IDEs, dependency management, CI/CD, runtime protections, secrets, governance, and incident response. |

---

<div align="center">

**© 2025 Kansas Frontier Matrix — MIT**  
FAIR+CARE Certified · MCP-DL v6.3 · KFM-MDP v11.2.3 · Diamond⁹ Ω / Crown∞Ω Ultimate Certified  

[⬅ Back to Security Standards](../README.md) · [⬅ Back to Infrastructure Index](../../infrastructure/README.md) · [📜 Governance Charter](../governance/ROOT-GOVERNANCE.md)

</div>