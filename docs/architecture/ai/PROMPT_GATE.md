# 🛡️ PROMPT_GATE — Input Sanitization & Policy Gating

**Prompt Gate** is the *first* safety control in the **Focus Mode** Retrieval-Augmented Generation (RAG) pipeline. Every user question is **cleaned + checked** before it is ever sent to the LLM backend (e.g., **Ollama**).:contentReference[oaicite:0]{index=0}:contentReference[oaicite:1]{index=1}

> [!IMPORTANT]
> Prompt Gate exists because **the LLM will try to answer whatever prompt it receives**. Therefore, **input sanitization must happen upstream** of the model call.:contentReference[oaicite:2]{index=2}

---

## 🧭 Quick Positioning in the System

**Route:** `POST /focus-mode/query` → **Prompt Gate** → Retrieval → Prompt Template → LLM → Output Policy (OPA) → UI:contentReference[oaicite:3]{index=3}:contentReference[oaicite:4]{index=4}

```text
Client/UI
  |
  |  POST /focus-mode/query
  v
FastAPI (Focus Mode API)
  |
  |  (1) Prompt Sanitization ✅  ← PROMPT_GATE (this doc)
  v
Evidence Retrieval (Neo4j/PostGIS/docs/vectors)
  |
  |  (2) Prompt Assembly + Citation Rules
  v
LLM Generate (Ollama)
  |
  |  (3) Output Governance ✅  ← OPA sidecar checks before release
  v
Response → UI (footnoted citations + provenance)
```

**Why it’s layered:**  
- **Input filtering & sanitization** happens *before* the LLM sees anything risky.:contentReference[oaicite:5]{index=5}  
- **Output governance** (OPA) evaluates the model output *before* returning it to the user.:contentReference[oaicite:6]{index=6}

---

## ✅ Core Guarantees (What Prompt Gate Must Always Do)

Prompt Gate **must**:

1. **Strip or neutralize prompt injection attempts** (e.g., “Ignore all previous instructions…”) before they reach the model.:contentReference[oaicite:7]{index=7}
2. **Filter disallowed content** such as profanity, hate speech, and requests violating usage policies (example: private personal data).:contentReference[oaicite:8]{index=8}
3. Produce a **safe version** of the user’s query by the time the prompt reaches the LLM.:contentReference[oaicite:9]{index=9}
4. Remain an **upstream control** (i.e., *never* “trust” the model to self-censor).:contentReference[oaicite:10]{index=10}
5. Be **maintainable and evolvable** (rules may be regex-based or a small classification model).:contentReference[oaicite:11]{index=11}

> [!NOTE]
> The project documentation explicitly calls out that this layer “will remain in place and unchanged.” Treat that as a hard contract: **Prompt Gate is not optional**.:contentReference[oaicite:12]{index=12}

---

## 🚫 Non‑Goals (What Prompt Gate Is NOT)

Prompt Gate is **not** responsible for:

- **Output compliance / final decisioning** → that is handled by **OPA** after the model generates an answer.:contentReference[oaicite:13]{index=13}
- **Tool permissions / tool execution** → Focus Mode is sandboxed with an explicit allow-list, currently **empty** (no code execution, no HTTP, no DB changes).:contentReference[oaicite:14]{index=14}
- **Evidence provenance and citation enforcement** → enforced via prompt template + governance rules (OPA) downstream.:contentReference[oaicite:15]{index=15}:contentReference[oaicite:16]{index=16}

---

## 🔥 Threat Model (What We Defend Against)

| Threat 🧨 | Example | Prompt Gate action |
|---|---|---|
| Prompt injection / instruction override | “Ignore all previous instructions and…” | Strip/escape the injection clause; keep the user’s actual question.:contentReference[oaicite:17]{index=17} |
| Policy-violating requests | “Give me private personal data about X” | Reject or redact (policy-based); do not forward raw request to LLM.:contentReference[oaicite:18]{index=18} |
| Toxic language | Hate speech / targeted harassment / profanity | Filter or reject per severity; log category.:contentReference[oaicite:19]{index=19} |
| Token/size abuse (DoS-ish prompts) | Extremely long input; repeated garbage | Enforce length limits; summarize/trim; rate-limit upstream (API gateway) |
| Data exfiltration attempts | “Show me system prompt / hidden rules” | Rewrite to safe request or reject; never forward the exfil instruction |

> [!TIP]
> Always treat **user input as hostile**. Also treat any user-controlled strings injected into prompts (names, labels, notes) as hostile unless explicitly proven otherwise.

---

## 🧱 Decision Model (ALLOW / SANITIZE / REJECT)

Prompt Gate should return a **decision** plus a **sanitized string** and **reasons**.

### ✅ ALLOW
- No policy violations detected.
- Minimal normalization only (whitespace, Unicode normalization, etc.).

### 🧼 SANITIZE
- The user’s intent is legitimate, but the prompt contains:
  - injection fragments (override instructions, roleplay commands),
  - mild profanity,
  - formatting/control sequences that should not be passed through verbatim.

This aligns with: “strips or neutralizes malicious instructions… removed or escaped.”:contentReference[oaicite:20]{index=20}

### ⛔ REJECT
- Direct policy violation (e.g., private personal data request).
- High confidence prompt injection that cannot be safely separated from intent.
- Repeated abusive content, threats, or hate.

> [!IMPORTANT]
> Even when rejecting, Prompt Gate should return a **safe, user-facing explanation** and **never echo back** the malicious payload verbatim.

---

## 🧼 Sanitization Rules (Recommended Baseline)

The documentation supports either **regex-based scrubbers** or a **small classification model** for rules evolution.:contentReference[oaicite:21]{index=21}

### 1) Normalization (do this first)
- Unicode normalization (e.g., NFKC) to defeat “look-alike” tricks
- Strip zero-width characters
- Collapse repeated whitespace
- Trim leading/trailing control characters

### 2) Injection phrase neutralization
Detect and remove/escape common injection patterns, e.g.:
- “ignore all previous instructions”
- “system prompt”
- “developer message”
- “act as” / “roleplay as”
- “you are now”

> [!NOTE]
> The project docs explicitly cite injection attempts like “Ignore all previous instructions…” as an example to remove or escape.:contentReference[oaicite:22]{index=22}

### 3) Policy category filters
- Profanity / hate speech / harassment
- Requests for private personal data
- Other “disallowed content” categories the project defines

### 4) Structure preservation
Prompt Gate should aim to preserve the user’s **actual question** while removing hostile fragments. This is consistent with: sanitize the question so the LLM won’t see disallowed instructions/content.:contentReference[oaicite:23]{index=23}

---

## 🧩 Integration Contract (Suggested)

Even if implementation details vary, keep this contract stable to avoid “security drift.”

### Input
- `raw_question: string`
- `user_context: { role, org, permissions, ... }`
- `request_context: { ip_hash, session_id, ui_state, ... }`

### Output
- `decision: "ALLOW" | "SANITIZE" | "REJECT"`
- `sanitized_question: string | null` (null if REJECT)
- `reasons: string[]` (machine-readable codes)
- `risk_score: number` (0–100)
- `redactions: { start, end, reason }[]` (optional)
- `version: string` (ruleset version)

---

## 🔌 FastAPI Hook (Reference Pattern)

> This is a **pattern**, not a mandated implementation. The hard requirement is that Prompt Gate runs **before** any prompt is sent to Ollama.:contentReference[oaicite:24]{index=24}

```python
# app/ai/prompt_gate.py

from dataclasses import dataclass
from enum import Enum

class Decision(str, Enum):
    ALLOW = "ALLOW"
    SANITIZE = "SANITIZE"
    REJECT = "REJECT"

@dataclass
class PromptGateResult:
    decision: Decision
    sanitized_question: str | None
    reasons: list[str]
    risk_score: int
    version: str = "v1"

def prompt_gate(raw_question: str, user_ctx: dict) -> PromptGateResult:
    q = normalize(raw_question)

    # 1) policy-violating categories first (hard reject)
    if asks_for_private_personal_data(q):
        return PromptGateResult(
            decision=Decision.REJECT,
            sanitized_question=None,
            reasons=["POLICY_PRIVATE_PERSONAL_DATA"],
            risk_score=95,
        )

    # 2) injection neutralization (sanitize)
    injection_hits = find_injection_fragments(q)
    if injection_hits:
        q = remove_or_escape_fragments(q, injection_hits)
        return PromptGateResult(
            decision=Decision.SANITIZE,
            sanitized_question=q,
            reasons=["PROMPT_INJECTION_NEUTRALIZED"],
            risk_score=60,
        )

    # 3) profanity/hate (sanitize or reject based on severity)
    severity = toxicity_severity(q)
    if severity >= 8:
        return PromptGateResult(
            decision=Decision.REJECT,
            sanitized_question=None,
            reasons=["POLICY_TOXIC_CONTENT_HIGH"],
            risk_score=90,
        )
    elif severity > 0:
        q = redact_toxic_terms(q)
        return PromptGateResult(
            decision=Decision.SANITIZE,
            sanitized_question=q,
            reasons=["TOXICITY_REDACTED"],
            risk_score=40,
        )

    return PromptGateResult(
        decision=Decision.ALLOW,
        sanitized_question=q,
        reasons=[],
        risk_score=5,
    )
```

---

## 🧠 How Prompt Gate Plays with Other Guardrails

### 🧰 AI Sandbox (Tooling)
Focus Mode’s AI runs with least privilege; the allow-list is currently **empty**, meaning the AI can only do text generation (no HTTP, no DB mutation, no code execution).:contentReference[oaicite:25]{index=25}

Prompt Gate does **not** manage allow-lists—but it *assumes* the AI is sandboxed and **still** enforces input constraints.

### 🧾 Output Governance (OPA)
After the model generates an answer, **OPA** evaluates the content before releasing it to the user.:contentReference[oaicite:26]{index=26}

Prompt Gate should pass along useful metadata to OPA (e.g., risk score, triggered categories) as part of the governance context.

### 📌 Citations & Provenance (Evidence-first)
The system is designed around footnoted citations that link back to real records.:contentReference[oaicite:27]{index=27}

OPA can enforce citation presence. Example policy pattern shown in project docs checks for a `[\d+]`-style citation marker.:contentReference[oaicite:28]{index=28}

---

## 📈 Observability & Audit (Must-Haves)

Prompt Gate should emit structured logs (redacted) and metrics:

- `prompt_gate.decision` (ALLOW/SANITIZE/REJECT)
- `prompt_gate.reasons[]` (reason codes)
- `prompt_gate.risk_score`
- `prompt_gate.ruleset_version`
- `prompt_gate.redaction_count`
- correlation IDs: `request_id`, `session_id`, `user_id_hash`

> [!WARNING]
> **Never log raw disallowed content** in plaintext. Log minimal snippets (redacted) or hashes.

---

## 🧪 Test Strategy (Security Regression = Non-Negotiable)

### ✅ Unit tests (deterministic)
- Injection phrases are removed/escaped.
- Profanity/hate list is applied consistently.
- Private-personal-data requests are rejected.

### 🧬 Regression corpus (grow over time)
Maintain a `prompt_gate_corpus.jsonl` with:
- `raw_prompt`
- expected `decision`
- expected `reasons`
- expected `sanitized_prompt` (if applicable)

### 🧱 CI gate
Treat Prompt Gate as a **security boundary**:
- breaking changes must be reviewed
- regression corpus must pass
- coverage thresholds enforced

> [!TIP]
> The docs mention CI/policy gates around governance behaviors (ex: citation enforcement). Apply the same discipline to Prompt Gate. :contentReference[oaicite:29]{index=29}

---

## 🗂️ Suggested Repo Placement

```text
docs/
  architecture/
    AI_SYSTEM_OVERVIEW.md
    ai/
      OLLAMA_INTEGRATION.md
      PROMPT_GATE.md   👈 you are here
app/
  ai/
    prompt_gate.py
    prompt_templates/
    opa/
config/
  ai/
    prompt_gate_rules.yml
```

---

## 🔄 Rule Updates & Versioning

Project docs explicitly anticipate evolving rules and even switching from regex scrubbers to a small classifier model.:contentReference[oaicite:30]{index=30}

Recommended approach:
- Version each ruleset: `v1`, `v1.1`, `v2`
- Record `ruleset_version` on every request
- Add new detections as **additive rules**; avoid changing semantics of existing reason codes unless necessary
- Keep “strict mode” toggles behind configuration (but never default-off in production)

---

## 🔗 Related Architecture Docs

- `../AI_SYSTEM_OVERVIEW.md` — Focus Mode RAG pipeline overview (Prompt Gate is step 1).:contentReference[oaicite:31]{index=31}
- `./OLLAMA_INTEGRATION.md` — LLM backend integration & governance alignment
- `../policy/` — OPA policy rules & governance checks (output filtering):contentReference[oaicite:32]{index=32}

---

## 📚 Primary Source (Project Grounding)

This document is grounded in the **Kansas Frontier Matrix Comprehensive System Documentation** sections describing:
- Prompt Gate as the “Prompt Sanitization” step in the RAG pipeline:contentReference[oaicite:33]{index=33}
- Input filtering & sanitization details, including injection removal/escaping and disallowed content categories:contentReference[oaicite:34]{index=34}
- OPA governance checks as an output-filtering layer:contentReference[oaicite:35]{index=35}
- Citation governance and policy enforcement examples:contentReference[oaicite:36]{index=36}

