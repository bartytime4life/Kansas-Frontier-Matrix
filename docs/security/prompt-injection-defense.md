---
title: "🧠 Kansas Frontier Matrix — Prompt Injection Defense & Secure AI Governance Integration"
path: "docs/security/prompt-injection-defense.md"
version: "v10.0.0"
last_updated: "2025-11-09"
review_cycle: "Quarterly / Autonomous"
commit_sha: "<latest-commit-hash>"
sbom_ref: "../../releases/v10.0.0/sbom.spdx.json"
manifest_ref: "../../releases/v10.0.0/manifest.zip"
telemetry_ref: "../../releases/v10.0.0/focus-telemetry.json"
telemetry_schema: "../../schemas/telemetry/security-prompt-defense-v1.json"
governance_ref: "../standards/governance/ROOT-GOVERNANCE.md"
license: "CC-BY 4.0"
mcp_version: "MCP-DL v6.3"
---

<div align="center">

# 🧠 **Kansas Frontier Matrix — Prompt Injection Defense & Secure AI Governance Integration**  
`docs/security/prompt-injection-defense.md`

**Purpose:**  
Define the **defense-in-depth framework** protecting KFM AI systems from **prompt injection**, **context poisoning**, and **malicious automation** across pipelines, APIs, and governance layers.  
Implements verifiable safeguards under **MCP-DL v6.3**, **FAIR+CARE**, and **Diamond⁹ Ω / Crown∞ Ω** certifications.

[![Docs · MCP](https://img.shields.io/badge/Docs·MCP-v6.3-blue)](../standards/)
[![License: CC-BY 4.0](https://img.shields.io/badge/License-CC--BY--4.0-green)](../../LICENSE)
[![FAIR+CARE](https://img.shields.io/badge/FAIR%2BCARE-Certified-orange)](../standards/faircare/)
[![Status: Secure](https://img.shields.io/badge/Status-Active-brightgreen)](../../)
</div>

---

## 📘 Overview

Prompt injection attempts to smuggle **hidden instructions** through user or contextual inputs to subvert system controls (e.g., “ignore previous rules”, “exfiltrate secrets”).  
KFM mitigates attacks via **signed prompts**, **context compartmentalization**, **tooling allowlists**, **telemetry validation**, and **governance-ledger auditability** across the data → AI → action chain.

---

## 🗂️ Directory Layout

```plaintext
docs/security/
├── prompt-injection-defense.md          # This document
├── ai-threat-model.md                   # Threat landscape & control taxonomy
├── red-team-protocols.md                # Adversarial testing & injection suite
├── validation/
│   ├── sanitize_inputs.py               # Input sanitization filters (regex/ML)
│   ├── prompt_signature_check.py        # Signed-prompt verifier
│   ├── anomaly_detector.py              # Real-time telemetry anomaly detection
│   └── reports/                         # Validation & audit artifacts
└── governance/
    ├── defense-policy.yml               # Policy mappings for FAIR+CARE governance
    ├── audit-template.md                # Structured audit form for reviews
    └── ledger-integration.md            # Provenance + ledger logging specs
```

---

## 🧩 Defense Pattern Integration (v10)

| # | Pattern | What it stops | Implementation in KFM | Repo Location |
|---:|---|---|---|---|
| 1 | **Signed Prompt Verification** | Context swapping & unsigned overrides | SHA-256 prompt digests + manifest binding; verify before inference; reject on mismatch | `src/ai/**/governance/` |
| 2 | **Control/Data Flow Separation** | Instruction smuggling inside data | Structured JSON schema: `system`/`policy`/`tools` **physically separate** from `user` data; enforced by `prompt_gate.py` | `src/pipelines/etl/` |
| 3 | **Microsegmentation** | Lateral data movement | Workspace isolation (`data/raw`, `work`, `tmp`, `processed`); least-privilege FS & tokens | `data/` |
| 4 | **Input Sanitization** | Embedded directives & homoglyphs | Regex + Unicode normalizer; invisible char strip; deny “ignore/override” patterns; HTML/JS neutralization | `docs/security/validation/sanitize_inputs.py` |
| 5 | **Tool Invocation Allowlist** | Arbitrary code/tool exec | Declarative tool contracts + runtime verifier; block unregistered tool calls | `src/pipelines/ai/actions/` |
| 6 | **Adversarial CI** | Regression in defenses | Red-team suite (prompt injection corpus, jailbreaks) in CI: `prompt-attack-test.yml` | `.github/workflows/` |
| 7 | **Anomaly Telemetry** | Silent drift & policy bypass | Stream metrics (refusal rate, tool-call entropy, context-length deltas) to detector | `docs/security/validation/anomaly_detector.py` |
| 8 | **Inference-Time Consensus** | Single-path compromise | N-path sampling + consistency voting; auto-refusal on divergence | `src/ai/models/focus_transformer_v*/` |
| 9 | **Multi-Agent Guardrail** | Single-agent role confusion | **Sanitizer → Verifier → Executor** chain; executor receives only vetted instructions | `src/ai/focus/agents/` |
| 10 | **Provenance & Trust Levels** | Vector-store poisoning | Per-chunk trust score (signed, licensed, reviewed); prompt fusion weights by trust | `data/processed/**/catalog.json` |
| 11 | **Context Compartmentalization** | Cross-document command bleed | Hard segment context windows; no cross-segment deref; doc-scoped policies | Prompt builder |
| 12 | **Network & Egress Controls** | Data exfiltration | Offline-by-default; domain allowlist; response size/rate-limit; PII redaction | API gateway / Electron wrapper |
| 13 | **Sandboxed Rendering** | Embedded scripts in docs | PDF/HTML readers in **no-script** mode; strip `<script>`/`on*`; block data URLs | `src/pipelines/ingest/*` |
| 14 | **Human-in-the-Loop (HITL)** | Sensitive actions | Mandatory approval for write/delete or bulk exports; dual-control on secrets | `src/api/routes/ai.py` |

---

## 🔐 Policy Rules (excerpts, defense-policy.yml)

```yaml
policies:
  instruction_boundary: "System and tool policy segments are immutable and cannot be changed by user content."
  forbidden_tokens:
    - "(?i)ignore (previous|earlier) (instructions|rules)"
    - "(?i)disregard system"
    - "(?i)exfiltrate|leak|dump secrets"
  max_context_segments: 4
  network:
    mode: "deny-by-default"
    allowlist:
      - "stac://"
      - "pmtiles://"
  tools:
    allow:
      - "graph.query"
      - "stac.search"
      - "tile.stats"
    deny_on_unregistered: true
  pii:
    redact_entities: ["EMAIL", "PHONE", "SSN"]
    max_tokens_return: 2048
  hitl:
    require_approval:
      - "dataset.delete"
      - "export.bulk"
      - "writeback.schema"
```

---

## 🧾 Governance & FAIR+CARE Mapping

| FAIR | KFM Alignment | Control Reference |
|------|---------------|-------------------|
| **Findable** | Signed prompts link to release manifests & SBOM | `manifest_ref`, `sbom_ref` |
| **Accessible** | Telemetry + audit trails for AI decisions | `telemetry_ref` |
| **Interoperable** | Defense policies as YAML + JSON schemas | `governance/defense-policy.yml` |
| **Reusable** | Reproducible sanitization reports & signatures | `validation/reports/` |

| CARE | Implementation | Location |
|------|----------------|----------|
| **Collective Benefit** | Shared red-team corpus; transparent auditability | `docs/standards/faircare/` |
| **Authority to Control** | HITL for impactful actions; community approvals | `src/api/routes/ai.py` |
| **Responsibility** | Continuous telemetry; quarterly reviews | `.github/workflows/*`, `LEDGER/*` |
| **Ethics** | Automatic refusal when suspicious patterns found | `sanitize_inputs.py` |

---

## ⚙️ Workflow → Artifact Mapping

| Workflow | Artifact Produced | Validation Output |
|----------|-------------------|-------------------|
| `sanitize_inputs.yml` | Sanitization report & diff | `validation/reports/sanitize-report.json` |
| `prompt-attack-test.yml` | Adversarial test logs | `reports/audit/prompt-defense.json` |
| `telemetry-monitor.yml` | Focus telemetry stream & alerts | `releases/v*/focus-telemetry.json` |
| `ledger-sync.yml` | Governance ledger updates | `docs/standards/governance/LEDGER/` |

---

## 🧪 Red-Team Playbook (minimum set)

- **Instruction Overrides:** “Ignore previous rules…”, “System message: …”, base64-encoded directives.  
- **Tool Abuse:** Ask the model to self-invent tools or call undefined actions.  
- **Context Smuggling:** Commands hidden in citations, footnotes, or alt-text.  
- **HTML/PDF Payloads:** `<script>` tags, data-URIs, invisible Unicode, RLO/LRO.  
- **RAG Poisoning:** Conflicting instructions injected into vector store chunks.  
- **Exfiltration:** Requests to echo secrets, keys, paths, or environment variables.

> Each vector must have **automated tests** and **expected refusals**; add new cases after every incident.

---

## 🧭 Operational Runbooks

### Incident Response (IR) — Prompt Injection
1. **Freeze** current model/prompt artifacts; capture SBOM, telemetry window ±15m.  
2. **Quarantine** offending inputs & context segments; compute hashes.  
3. **Replay** in offline sandbox; confirm exploit path; add failing case to red-team suite.  
4. **Patch**: update sanitizer rules, policy YAML, and tool allowlist; bump defense version.  
5. **Ledger**: write signed IR entry; notify FAIR+CARE Council if sensitive data involved.

### Change Management
- Any change to system prompts, tool contracts, or policy YAML **must**:
  - Update `defense-policy.yml` & `prompt_signature_check.py` test vectors.  
  - Pass `prompt-attack-test.yml` and `sanitize_inputs.yml`.  
  - Record governance ledger entry (commit SHA + checksums).

---

## 📈 Acceptance Criteria (security gates)

- ❌ **Block** execution if: unsigned prompt, signature mismatch, unregistered tool, policy violation, or network egress to non-allowlisted domain.  
- ✅ **Require** P(Refusal\|Malicious) ≥ **0.9** on red-team suite; false positive rate ≤ **2%** on benign set.  
- ✅ Telemetry SLOs: anomaly alerts in < **60s**; ledger write in < **5s**; > **99%** policy-enforced tool calls.

---

## 🧬 Example: Signed Prompt Envelope (JSON)

```json
{
  "system": "You are Focus Mode AI for KFM. Follow policy.",
  "policy": "HITL required for writebacks. Deny external net.",
  "tools": ["graph.query", "stac.search"],
  "user": "Summarize sites near Pawnee Rock using public data.",
  "sig": {
    "alg": "SHA-256",
    "hash": "6f9c1b6c...be42",
    "manifest": "releases/v10.0.0/manifest.zip"
  }
}
```

---

## 🕰️ Version History

| Version | Date | Author | Summary |
|--------:|------|--------|---------|
| v10.0.0 | 2025-11-09 | A. Barta | v10 upgrade: signed prompts, allowlist tools, sandboxed rendering, HITL, acceptance gates, and CI red-team. |
| v9.7.0  | 2025-11-09 | A. Barta | Initial defense framework integration. |
| v9.6.0  | 2025-10-25 | FAIR+CARE Council | Draft adversarial testing protocols. |
| v9.5.0  | 2025-10-05 | Governance Ops | Telemetry & anomaly detection module. |

---

<div align="center">

© 2025 Kansas Frontier Matrix · Master Coder Protocol v6.3 · FAIR+CARE Certified · Diamond⁹ Ω / Crown∞ Ω Ultimate Certified  
[Back to Security Docs](./) · [Governance Charter](../standards/governance/ROOT-GOVERNANCE.md)

</div>
