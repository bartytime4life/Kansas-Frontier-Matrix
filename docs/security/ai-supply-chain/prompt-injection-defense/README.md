---
title: "🛡️ KFM v11.2.4 — Prompt-Injection Defense Standard for CI/CD & AI Agents (Diamond⁹ Ω / Crown∞Ω Certified)"
path: "docs/security/ai-supply-chain/prompt-injection-defense/README.md"
version: "v11.2.4"
last_updated: "2025-12-05"

release_stage: "Stable / Enforced"
lifecycle: "Long-Term Support (LTS)"
review_cycle: "Quarterly · Security & Supply-Chain Council"
content_stability: "stable"
backward_compatibility: "v10.x → v11.x security-contract compatible"
status: "Active / Mandatory"

doc_kind: "Standard"
header_profile: "standard"
footer_profile: "standard"

scope:
  domain: "security/ai-supply-chain"
  applies_to:
    - "ci-cd"
    - "github-actions"
    - "ai-agents"
    - "rag-systems"
    - "langgraph-workers"
    - "docs-automation"

fair_category: "F1-A1-I1-R1"
care_label: "Public · Low-Risk"
sensitivity: "General (non-sensitive; auto-mask rules apply)"
classification: "Public"
indigenous_rights_flag: true

commit_sha: "<latest-commit-sha>"
previous_version_hash: "<prev-sha256>"
doc_integrity_checksum: "<sha256>"

sbom_ref: "../../../../releases/v11.2.4/sbom.spdx.json"
manifest_ref: "../../../../releases/v11.2.4/manifest.zip"
telemetry_ref: "../../../../releases/v11.2.4/security-telemetry.json"
telemetry_schema: "../../../../schemas/telemetry/security/prompt-injection-defense-v1.json"

governance_ref: "../../../standards/governance/ROOT-GOVERNANCE.md"

doc_uuid: "urn:kfm:doc:security:prompt-injection-defense-v11.2.4"
semantic_document_id: "kfm-doc-security-prompt-injection-defense-v11.2.4"
event_source_id: "ledger:kfm:doc:security:prompt-injection-defense"

license: "Apache-2.0"
mcp_version: "MCP-DL v6.3"
markdown_protocol_version: "KFM-MDP v11.2.4"
---

<div align="center">

# 🛡️ KFM v11.2.4 — Prompt-Injection Defense Standard for CI/CD & AI Agents  
`docs/security/ai-supply-chain/prompt-injection-defense/README.md`

**Purpose:**  
Define the mandatory, repository-checked, and CI/CD-enforced defenses against prompt injection and AI-agent abuse across KFM’s software supply chain — including GitHub Actions, autonomous reviewers, RAG systems, and documentation agents — so untrusted text can never become executable instructions.

</div>

---

## 📘 Overview

AI-augmented CI/CD pipelines — especially those performing code review, approvals, documentation synthesis, or automated PR triage — are now critical attack surfaces. Recent incidents have shown AI assistants:

- Executing attacker-supplied text from PRs/issues.  
- Treating untrusted repo content as operational instructions.  

KFM v11 therefore:

- Treats **all repository content as adversarial** by default.  
- Requires **strict prompt boundaries** and **sandboxed execution** for all AI agents.  
- Pins defense logic in version-controlled code and workflows.  

### 1. Threat model summary

#### 1.1 Primary attack vectors

- **Untrusted PR/issue text hijacks AI agent logic**  
- **Malicious commit messages** triggering unsafe agent behavior  
- **Injected instructions inside config files (YAML/JSON/Markdown)** interpreted as operational steps  
- **AI-driven code modification loops** acting on manipulated context  
- **AI-generated shell commands** invoked by CI jobs without guardrails  
- **LLM-generated approvals** enabling malicious code submission  

#### 1.2 Capabilities of a successful attacker

If defenses fail, an attacker may achieve:

- Remote code execution inside ephemeral runners.  
- Credential / token exfiltration.  
- Repository rewrite or backdoor introduction.  
- Model or dataset poisoning.  
- Lateral movement within CI/CD and related infrastructure.  

This standard defines the required controls to keep those outcomes unreachable.

---

## 🗂️ Directory Layout

```text
📂 docs/security/ai-supply-chain/
└── 📂 prompt-injection-defense/
    ├── 📄 README.md                      # 🛡️ Prompt-Injection Defense Standard (this file)
    ├── 📂 policy/                        # 📜 Normative policies & narrative guidance
    │   ├── 📄 boundaries.md              # Prompt boundary & context isolation rules
    │   ├── 📄 agent-constraints.md       # Detailed AI agent behavior constraints
    │   └── 📄 ci-isolation.md            # CI isolation & runner policies
    ├── 📂 patterns/                      # 🧪 Attack patterns & tests
    │   ├── 📂 detected-attacks/          # Real / simulated attack write-ups
    │   └── 📂 sanitization-tests/        # Test fixtures for sanitizer
    └── 📂 checklists/                    # ✅ Operational checklists
        ├── 📄 onboarding.md              # New-repo AI-security onboarding
        └── 📄 audit.md                   # Periodic audit & review checklist
```

Security-related **code** must live under `src/security/...` (see Architecture section), but any normative policy or example must be documented under this `docs/security/ai-supply-chain/` subtree and linked from here.

---

## 🧭 Context

This standard applies to all KFM contexts where AI systems:

- See untrusted data (PRs, issues, comments, config files, logs).  
- Propose changes, approvals, or actions affecting code, infrastructure, or data.  

It covers (non-exhaustive):

- GitHub Actions workflows with AI-powered steps.  
- Autonomous or semi-autonomous PR reviewers (e.g., LangGraph workers).  
- CLI-style AI tools invoked from CI/CD.  
- Documentation or Story Node generation jobs fed from repo content.  

Relationship to other standards:

- **Markdown Protocol (KFM-MDP v11.2.4)**  
  - Ensures docs produced by AI remain structurally compliant and non-executable.  
- **Supply-Chain Security & SLSA/SBOM standards**  
  - This document extends those to AI agents and AI-linked dependencies.  
- **Geoethical & geoprivacy standards**  
  - AI systems must respect data-sovereignty rules **in addition** to technical safety constraints.

---

## 🧱 Architecture

This section defines the required defense layers and their implementation expectations.

### 1. Layer 1 — Hard CI isolation

| Component            | Requirement                                                                                   |
|----------------------|-----------------------------------------------------------------------------------------------|
| GitHub Actions       | Never execute `run:` commands built from raw LLM output.                                      |
| AI Agent Runners     | Must operate in **no-credential sandboxes** (no write-scoped tokens, no secret mounts).      |
| PR Workflows         | When AI is involved, workflows must be effectively **read-only** with respect to the repo.   |
| Self-Hosted Runners  | **Forbidden** for AI decisioning unless ephemeral, attested, and WAL-hardened.               |

Key design rules:

- Separate “AI review” jobs from “mutation/merge” jobs.  
- Enforce `permissions: read-all` and a dedicated `GH_TOKEN_AI_SANDBOX` with **zero write privileges**.  
- Prohibit AI paths from gaining access to deployment secrets, package registries, or signing keys.

### 2. Layer 2 — Prompt boundary enforcement

All KFM AI agents must:

- Use **deterministic system prompts**, checked into the repo and version-pinned.  
- Explicitly treat the following as **opaque data**, never executable instruction sources:
  - Issue titles and bodies.  
  - PR descriptions and comments.  
  - Commit messages and diffs.  
  - Config files (YAML/JSON/TOML).  
  - Markdown documents and embedded code fences.  
- Reject or downgrade any instruction that originates from those untrusted fields unless explicitly whitelisted.

Agents must distinguish between:

- **Control plane**: system prompts, configuration, and allowlists (trusted).  
- **Data plane**: user/attacker-provided text (untrusted).

### 3. Layer 3 — Content sanitization API

KFM ships a required pre-processing module:

```text
src/security/prompt_sanitizer/
├── sanitize_untrusted_text.py
├── tokenizer_limits.json
├── forbidden_sequences.txt
└── provenance_labels.yaml
```

Requirements:

- All untrusted text **must** pass through `sanitize_untrusted_text.py` before being sent to AI models.  
- Sanitizer must:
  - Strip or neutralize shell-like patterns (e.g., `$(...)`, backticks, `;`, `&&` chains).  
  - Block heredocs (`<<EOF`, `<<RUN`, `<<SCRIPT`, etc.).  
  - Block or neutralize code-fenced injection attempts (e.g., “```bash\nrm -rf /\n```”).  
  - Detect common jailbreak and prompt-injection patterns.  
  - Add provenance labels (source, repo, PR number, etc.).  
  - Log all sanitization events to OpenTelemetry using the configured security telemetry schema.

No AI agent in CI may bypass this sanitizer for untrusted input.

### 4. Layer 4 — LLM execution sandbox policy

AI-generated output that could influence CI/CD behavior must pass a multi-gate pipeline:

1. **AST Gate**  
   - Parse output; verify it is **data**, not shell commands, scripts, or infra-as-code.  
   - Reject or quarantine outputs containing dangerous constructs (pipes, redirection, `import os`, etc.).  

2. **Intent Classifier Gate**  
   - Use a separate classifier (or rules engine) to detect:
     - Attempts to execute commands.  
     - Attempts to exfiltrate secrets.  
     - Attempts to alter CI config, deployment manifests, or secrets.  

3. **Allowlist Matcher**  
   - Only transformations and formats on an explicit allowlist are permitted (e.g., “summarize code”, “suggest comments”, “generate Markdown doc draft”).  

4. **Retry → WAL Replay**  
   - If output is nondeterministic or violates constraints:
     - Log event to a Write-Ahead Log (WAL).  
     - Optionally retry with stricter constraints.  
     - Never fall back to “just run it anyway”.

### 5. Hardened CI/CD workflow template

Canonical workflow path:

```text
.github/workflows/ai-review.yml
```

Required properties:

- `permissions: read-all` for AI review steps.  
- A dedicated token (e.g., `GH_TOKEN_AI_SANDBOX`) with zero write privileges.  
- All AI-produced text must be:
  - Fed through `src/security/prompt_sanitizer/`.  
  - Persisted only as **review artifacts**, not as commands.  
- AI output must **never** flow directly into:
  - `bash`, `sh`, PowerShell, or similar shells.  
  - Terraform, Kubernetes, or deployment CLIs.  
- Workflow must enforce:
  - SLSA provenance for artifacts.  
  - SBOM-driven dependency validation before AI steps.  
  - WAL-safe logging for AI-related decisions.

### 6. AI agent behavior policy (mandatory)

#### 6.1 Non-negotiable constraints

AI agents **may**:

- Summarize code and configuration.  
- Propose review comments and refactoring suggestions.  
- Generate draft documentation (Markdown, comments, READMEs).  

AI agents **must not**:

- Execute scripts, shell commands, or infra tools.  
- Generate patches that are applied automatically without human approval.  
- Auto-approve PRs or merges.  

Every AI-generated artifact must carry provenance tags:

```yaml
ai_origin: "<agent-name>"
ai_model: "<model-id-or-version>"
input_digest: "<sha256-of-input-context>"
output_digest: "<sha256-of-ai-output>"
```

These tags must be attached to PR comments and stored in associated logs.

#### 6.2 Story Nodes / analyses mode

For documentation workflows (Story Nodes, analyses, architecture docs):

- Input documents are **immutable evidence**, not instructions.  
- AI must not infer or suggest operational actions (e.g., “deploy this now”) from user text.  
- Generated docs must obey KFM-MDP formatting and not introduce hidden executable snippets.

---

## 🧪 Validation & CI/CD

This section defines required tests and checks that enforce the standard.

### 1. Workflow validation

- Lint all workflows using a security-aware validator that checks for:
  - Direct piping of AI output into `run:` steps.  
  - Use of write-scoped tokens in AI steps.  
  - Missing or bypassed sanitizer calls for untrusted text.  

### 2. Sanitizer tests

- `patterns/sanitization-tests/` must include:
  - Prompt-injection examples (e.g., “ignore previous instructions and run…”).  
  - Jailbreak payloads.  
  - Shell and heredoc exploits.  
- CI must run unit and integration tests ensuring these are **blocked or neutralized**.

### 3. AST and intent-gate tests

- Unit tests for AST Gate to:
  - Reject command-like outputs.  
  - Accept benign structured data.  
- Tests for Intent Classifier Gate to:
  - Flag attempts at execution, exfiltration, or policy override.  

### 4. Supply-chain & dependency tests

- SBOM validation step before any AI-related jobs.  
- Automated checks for:
  - Vulnerabilities in AI-related dependencies.  
  - Dangerous default configurations in CLI tools or SDKs.  

### 5. Red-team & incident drills

- Quarterly red-team simulations targeting AI workflows.  
- CI tasks or external automation that:
  - Inject known attack patterns into “test PRs” to confirm defenses still hold.

---

## 📦 Data & Metadata

### 1. Telemetry & observability

All AI-assisted CI operations must emit metrics to the configured telemetry backend (OpenTelemetry-aligned):

- `security.prompt_injection.scan_count`  
- `security.prompt_injection.blocked_events`  
- `security.ai_sandbox.exec_attempts`  
- `security.ai_sandbox.violations`  
- `runtime.energy_joules` (mapped to CO₂e as per KFM energy/carbon schemas)  

Telemetry requirements:

- Use `telemetry_schema` specified in front-matter (`prompt-injection-defense-v1.json`).  
- Keep metric cardinality low (e.g., aggregate by repo, workflow, rule).  
- Tag events with:
  - `repo`, `workflow`, `job`, `ai_origin`, `ai_model`, `sensitivity_level`.  

### 2. Provenance records

- All AI workflows must produce:
  - Build/provenance attestations (e.g., SLSA-compatible).  
  - AI decision logs with `input_digest` and `output_digest`.  
- Provenance should be linked to:
  - SBOM entries for AI-related dependencies.  
  - Security policy versions (this document’s `doc_uuid` and `version`).

---

## ⚖ FAIR+CARE & Governance

Although primarily a technical security standard, this document also enforces FAIR+CARE and governance principles for AI in the supply chain:

- **FAIR**
  - *Findable*: AI security configurations and logs are cataloged and discoverable for audits.  
  - *Accessible*: Policies and telemetry are accessible to authorized auditors and governance bodies.  
  - *Interoperable*: Uses open standards (SLSA, SBOM, OpenTelemetry) for cross-tool analysis.  
  - *Reusable*: Standardized patterns and templates can be reused across repos and teams.  

- **CARE**
  - *Collective Benefit*: Secures KFM contributors and downstream users from AI-mediated supply-chain attacks.  
  - *Authority to Control*: Governance bodies (Security Engineering, MCP Council, FAIR+CARE) define and enforce AI behavior boundaries.  
  - *Responsibility*: Clear incident-reporting and review cadences hold maintainers accountable.  
  - *Ethics*: Prevents AI from being weaponized to bypass human review, governance, or safety constraints.  

### Governance & review cadence

Mandatory:

- **Quarterly**:
  - Red-team simulation focused on AI-assisted workflows.  
- **Biannual**:
  - Dependency and model audit (LLM versions, SDKs, CLIs).  
- **Incident reporting**:
  - Any blocked jailbreak attempt.  
  - Any AI output rejected by AST Gate or Intent Gate.  
  - Any sanitizer escalation or anomaly.

Required reviewers for major changes to this standard:

- Security Engineering.  
- MCP Council.  
- FAIR+CARE Compliance.  

---

## 🕰️ Version History

| Version | Date       | Status            | Summary                                                                 |
|--------:|------------|-------------------|-------------------------------------------------------------------------|
| v11.2.4 | 2025-12-05 | Active / Mandatory | First full KFM security standard for prompt-injection defense in CI/CD. |

Future revisions must:

- Document changes to defense layers, sanitizer behavior, or required telemetry.  
- Update workflow templates and checklists in `policy/` and `checklists/` accordingly.  
- Keep this standard in sync with global governance and supply-chain security standards.

---

<div align="center">

🛡️ **KFM v11.2.4 — Prompt-Injection Defense Standard for CI/CD & AI Agents**  
Scientific Insight · Secure-by-Design · AI-Supply-Chain Hardened  

[📘 Docs Root](../../../..) · [🔐 Security Index](../../README.md) · [⚖ Governance](../../../standards/governance/ROOT-GOVERNANCE.md)

</div>