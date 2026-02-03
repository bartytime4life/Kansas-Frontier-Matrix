<!-- 📍 File: tools/my-tool/bin/READMD.md -->

# 🧰 my-tool (bin)

![Status](https://img.shields.io/badge/status-active-success)
![CLI](https://img.shields.io/badge/type-CLI-blue)
![Evidence First](https://img.shields.io/badge/principle-evidence--first-purple)
![No Source, No Answer](https://img.shields.io/badge/rule-no%20source%2C%20no%20answer-black)

**my-tool** is the **command-line toolbelt** for the Kansas-Matrix-System / **Kansas Frontier Matrix** workflow — designed to keep every action traceable, reproducible, and aligned with the platform’s “truth path” (Raw ➜ Processed ➜ Catalog ➜ DB ➜ API ➜ UI/AI). 🧭

> ✅ **Goal:** One consistent CLI entrypoint for **development**, **data pipelines**, and **AI guardrails** — without bypassing governance.

---

## ✨ What lives in `bin/`?

This directory contains **runnable entrypoints** (scripts/shims). Keep them:
- **Thin** (arg parsing + dispatch)
- **Deterministic** (same inputs → same outputs)
- **Auditable** (log what happened, and why)

> 🧠 Rationale: tools that execute “mystery logic” become untrustworthy quickly — especially in high-stakes AI/data contexts.  [oai_citation:0‡Artificial Intelligence & Machine Learning in Health Care & Medical Sciences.pdf](sediment://file_0000000036fc71fda445161776f735db)

---

## ⚡ Quick Start

### 1) Make it executable
```bash
chmod +x tools/my-tool/bin/my-tool
```

### 2) Add `bin/` to your PATH (recommended)
```bash
export PATH="$PWD/tools/my-tool/bin:$PATH"
```

Optional (persist in shell profile):
```bash
echo 'export PATH="$PWD/tools/my-tool/bin:$PATH"' >> ~/.bashrc
```

### 3) Verify
```bash
my-tool --version
my-tool --help
```

---

## 🧭 Core Principles (Non‑Negotiables)

### ✅ 1) Don’t bypass the “truth path”
All operations should respect the system layering and provenance gates:
- UI never queries DB directly
- AI never “makes up” facts
- Outputs must map back to sources

This matches the KFM architecture and governance goals (evidence-first + provenance).  [oai_citation:1‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

### ✅ 2) “No Source, No Answer”
If a command generates summaries, narratives, or AI outputs, it must:
- attach citations/source IDs
- fail closed if evidence is missing

This mirrors Focus Mode’s approach: retrieve → generate → policy check → log provenance.  [oai_citation:2‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

### ✅ 3) Guardrails at input + output
- **Input sanitization** (prompt gate / injection defense)
- **Output filtering** (OPA policy checks)
- **Immutable logs** (who/what/when/sources)

These are core KFM AI security constraints.  [oai_citation:3‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## 🛠️ Command Contract

**Command format**
```bash
my-tool <command> [subcommand] [options]
```

**Exit codes**
- `0` success ✅
- `1` general error ❌
- `2` usage / bad args 🧯
- `3` missing config / dependency 🧩
- `4` policy violation / blocked by guardrails 🛡️

**Output expectations**
- human-readable logs to stderr
- machine-readable outputs as JSON when `--json` is used

---

## 🚀 Typical Workflows (Examples)

### 🧪 Developer workflow
```bash
my-tool doctor
my-tool up
my-tool logs api
my-tool down
```

### 📥 Data pipeline workflow (truth path)
```bash
my-tool ingest <source> --raw-dir data/raw
my-tool process --input data/raw --output data/processed
my-tool catalog build --input data/processed
my-tool load postgis --input data/processed
my-tool index build --input data/processed
```

### 🤖 Focus Mode / RAG test harness
```bash
my-tool focus query "What happened here in the 1930s?" --place "Finney County" --year 1935
my-tool focus lint --answer ./out/answer.md --require-citations
my-tool focus replay --run-id <id>
```

> 💡 Why this matters: AI outputs must be testable and policy-checked, not “trust me bro.”  [oai_citation:4‡Artificial Intelligence & Machine Learning in Health Care & Medical Sciences.pdf](sediment://file_0000000036fc71fda445161776f735db)  [oai_citation:5‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## ⚙️ Configuration

my-tool should read configuration in this order (highest wins):
1. CLI flags
2. Environment variables
3. `.env` / project config file

### 🌱 Suggested environment variables
```bash
# Core services
KFM_API_URL=http://localhost:8000
POSTGIS_URL=postgresql://postgres:postgres@localhost:5432/kfm
NEO4J_URL=bolt://localhost:7687

# AI
OLLAMA_API_URL=http://localhost:11434

# Observability
LOG_LEVEL=info
```

> 🧩 The Ollama integration is designed to be swappable via config (UI stays decoupled).  [oai_citation:6‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## 🔒 Security & Safety Notes

### 🧼 Prompt / input safety
If `my-tool` offers AI commands (e.g., `focus query`), it must:
- sanitize inputs before any LLM call
- reject prompt injection patterns
- block disallowed requests

This is aligned with KFM’s Prompt Gate guidance.  [oai_citation:7‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

### 🛡️ Output policy enforcement
If content is generated, it should be validated by policy rules (OPA-style) before returning results.  [oai_citation:8‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

### 🧾 Provenance logging
At minimum, log:
- command invoked
- inputs (paths/IDs, not secrets)
- artifacts created
- source IDs used for derived outputs
- versions (tool, model, datasets)

> “If you can’t trace it, you can’t trust it.” 🧭  [oai_citation:9‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## 🧠 Implementation Guidance (Why CLI ergonomics matter)

- Prefer **event-driven / async I/O** for network-heavy workflows (API calls, DB queries, indexing), avoiding long blocking steps where possible.  
- Keep CPU-heavy tasks off the “interactive path” (run as jobs/workers).

This matches Node-style scalability concepts (event loop + I/O efficiency).  [oai_citation:10‡Node.js-React-CSS-HTML.pdf](sediment://file_00000000b09c71f8b277cb19b9f597b2)

---

## 🧩 Troubleshooting

### `command not found: my-tool`
```bash
export PATH="$PWD/tools/my-tool/bin:$PATH"
hash -r
which my-tool
```

### Permission denied
```bash
chmod +x tools/my-tool/bin/my-tool
```

### “No Source, No Answer” failures
- Confirm retrieval/index services are running
- Confirm catalog metadata exists
- Confirm policy allows the requested content

> This is expected behavior — fail closed to protect trust. 🛡️  [oai_citation:11‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)

---

## 📚 Reference Docs (Project Grounding)

- Kansas Frontier Matrix — Architecture, strict layering, provenance, Focus Mode + Ollama integration  [oai_citation:12‡Kansas Frontier Matrix Comprehensive System Documentation.pdf](sediment://file_00000000ef40722faf17987b69730695)  
- AI/ML Best Practices & Pitfalls — why black-box systems are risky; emphasizes rigor, safety, and trust  [oai_citation:13‡Artificial Intelligence & Machine Learning in Health Care & Medical Sciences.pdf](sediment://file_0000000036fc71fda445161776f735db)  
- Node.js foundations — event loop + I/O scaling concepts helpful for CLI/service ergonomics  [oai_citation:14‡Node.js-React-CSS-HTML.pdf](sediment://file_00000000b09c71f8b277cb19b9f597b2)  

---

## 🗺️ Suggested Repo Layout (for this tool)

```text
tools/my-tool/
├─ bin/                # ✅ entrypoints (this folder)
│  ├─ my-tool          # CLI shim/launcher
│  └─ READMD.md        # this file
├─ src/                # implementation (python/node/go/etc.)
├─ configs/            # default configs + templates
├─ policies/           # OPA/Rego policies (if applicable)
└─ tests/              # CLI contract + guardrail tests
```

---

## ✅ Checklist (Definition of “Done”)

- [ ] `my-tool --help` works and documents commands
- [ ] `my-tool doctor` validates dependencies + env
- [ ] No command bypasses KFM truth path
- [ ] AI outputs require citations (or fail)
- [ ] Policy checks run before returning risky outputs
- [ ] Provenance logs exist for derived artifacts
- [ ] CI runs CLI smoke tests + guardrail tests

🧰🔍 Build tools people can trust.
