# Focus Mode tests

![Governed](https://img.shields.io/badge/governed-evidence--first-blue)
![Policy](https://img.shields.io/badge/policy-deny--by--default-critical)
![Citations](https://img.shields.io/badge/citations-required-success)
![Audit](https://img.shields.io/badge/audit-provenance--ready-informational)

> [!IMPORTANT]
> **Focus Mode is governed.**
> This test suite exists to prevent regressions that would break:
> - **Evidence-first answers** (no “black box” claims)
> - **Cite-or-abstain** behavior (missing citations must fail)
> - **Deny-by-default policy enforcement**
> - **Trust membrane** (clients use the governed API boundary, never direct DB/LLM access)
> - **Auditability + privacy-aware telemetry**

---

## What this folder is

`tests/focus/` holds the regression and compliance tests for **KFM Focus Mode** (the in-platform, cited AI assistant).

The goal is not “does the UI look nice” or “does the model sound smart.”
The goal is: **does Focus Mode behave like a governed, evidence-backed system** under real-world and adversarial conditions.

---

## Non-negotiable invariants

These are the **hard guarantees** Focus Mode must maintain. Tests in this folder should map to at least one item below.

### Evidence-first

- If a claim cannot be traced to an approved source or governed model run, Focus Mode must label it clearly (e.g., **not confirmed**).
- The system should prefer abstaining over guessing.

### Cite or abstain

- Answers must include citations sufficient to re-open the underlying evidence.
- Missing required citation objects is treated as a **policy deny** (fail closed).

### Deny-by-default policies

- If the policy engine rejects, is uncertain, or cannot be reached, the result must default to **blocked**.
- The safest behavior is “no data leaves unless explicitly allowed.”

### Trust membrane

- UI and external clients **must not** bypass the API boundary to reach databases or the LLM.
- Tests should validate that Focus Mode requests/answers flow through governed endpoints and return policy + provenance metadata.

### Auditability

- Focus Mode interactions should be loggable and traceable (question → retrieved context → model/version → answer → citations).
- Correlation IDs should allow cross-service tracing.

### Privacy-aware telemetry

- Analytics and logs must avoid leaking sensitive scope content.
- Prefer hashed/redacted identifiers unless explicitly required and consented.

---

## Suggested directory layout

> [!NOTE]
> If your repo already has a different convention, keep the invariant intent and adapt paths accordingly.

```text
tests/focus/
├─ README.md
├─ fixtures/
│  ├─ contexts/                 # minimal “map/timeline/dataset selection” contexts
│  ├─ retrieval/                # frozen retrieval results (documents/snippets) for deterministic tests
│  ├─ policies/                 # policy inputs + expected decisions
│  └─ prompts/                  # prompt templates or system instructions (if versioned)
├─ golden/
│  ├─ conversations/            # input → expected structured output snapshots
│  └─ citations/                # expected citation blocks + required identifiers
├─ unit/
│  ├─ state_machine/            # Focus Mode overlay state transitions
│  ├─ citation_schema/          # schema validation: cite-or-abstain
│  └─ redaction/                # sensitive field redaction/generalization checks
├─ contract/
│  ├─ api/                      # OpenAPI/GraphQL contract tests for Focus endpoints
│  └─ etag_conflict/            # conditional write conflict handling (412, retries, merges)
├─ integration/
│  ├─ rag_pipeline/             # retrieval → policy precheck → generation → policy postcheck
│  └─ audit_trail/              # logs emitted with required fields, redactions applied
├─ ui/
│  ├─ focus_mode_panel/         # component tests for hide/show, keyboard behavior
│  └─ a11y/                     # WCAG/ARIA checks + keyboard nav tests
├─ offline/
│  ├─ persistence/              # IndexedDB/local persistence
│  └─ sync_queue/               # offline → online transitions
├─ realtime/
│  ├─ websocket/                # reconnect, ordering, presence fanout
│  └─ rate_limits/              # server and client bounded backoff behavior
└─ load/
   ├─ throughput/               # event ingestion throughput
   └─ latency/                  # p95 latency budgets + client “jank” guardrails
```

---

## Test matrix

This matrix is the baseline coverage expectation for Focus Mode.

| Layer | What we test | Pass/fail signal | Typical location |
|---|---|---|---|
| Unit | State machine transitions, policy evaluation hooks, event schema validation | deterministic transition graph, schema pass | `unit/` |
| Component UI | Panel hide/show, keyboard shortcuts, focus outline stability | no visual/layout regressions, stable a11y tree | `ui/` |
| Integration | API contracts, conditional writes, JSON Patch/Merge Patch behavior | conflicts resolved correctly, correct status codes | `integration/`, `contract/` |
| Offline | Persistence, service worker cache, background sync queue | no data loss offline/online | `offline/` |
| Realtime | WebSocket reconnect, presence fanout, ordering guarantees | bounded reconnect backoff, no dup presence | `realtime/` |
| Accessibility | keyboard nav, ARIA semantics, WCAG checks | WCAG 2.2 AA targets met | `ui/a11y/` |
| Security | auth flows, token storage, CSRF protections, log redaction | no token leakage, least privilege validated | `contract/`, `integration/` |
| Load/perf | throughput, WebSocket fanout, client CPU | p95 budgets met, no UI jank | `load/` |

---

## Core contracts to enforce

### Citation handshake contract

Focus Mode output must include a **citation block** that can be used to resolve evidence.

Minimum expectation for a “citation object”:

- Dataset identifiers (e.g., dataset key and/or DOI if available)
- Links to dataset landing metadata (e.g., DCAT) and spatiotemporal assets (e.g., STAC)
- CARE/sensitivity flags surfaced if generalization/redaction occurred

> [!TIP]
> Keep tests focused on **structure + identifiers + resolvability**, not “the exact prose.”
> LLM text is inherently variable; governance metadata must be stable.

Example of a **proposed** response shape for tests (adjust to your actual API):

```json
{
  "answer_markdown": "…",
  "citations": [
    {
      "dataset_key": "kfm.dataset.example",
      "doi": "10.xxxx/xxxxx",
      "dcat_url": "https://…",
      "stac_url": "https://…",
      "snippet": "…",
      "prov": {
        "activity_id": "prov:…",
        "ingestion_id": "ing:…"
      },
      "care": {
        "privacy_level": "generalized"
      }
    }
  ],
  "policy": {
    "decision": "allow",
    "rules": ["…"]
  }
}
```

### Deny-by-default policy behavior

- If policy returns `deny`, response must not include restricted fields.
- If policy cannot be evaluated, response must be treated as `deny`.

### Trust membrane contract

- UI tests should verify that Focus Mode requests go through governed endpoints.
- Integration tests should detect any “direct DB/LLM” bypassing (e.g., missing audit metadata, missing policy decision envelope).

---

## Running the tests

> [!NOTE]
> Tooling varies across KFM subsystems. Use the commands wired into your repo (e.g., `make test`, `pnpm test`, `pytest`).
> Below are **conventional** entry points and environment variables.

### Environment variables

```bash
# Example only — rename to match repo conventions
export KFM_API_BASE_URL="http://localhost:8000"
export KFM_TEST_AUTH_TOKEN="..."
export KFM_TEST_MODE="1"
```

### Common command patterns

```bash
# unit tests
make test-focus-unit

# API/contract tests
make test-focus-contract

# full integration suite
make test-focus

# UI/a11y tests
make test-focus-ui
```

---

## Adding a new test

1. **Name the invariant** you’re protecting (cite-or-abstain, deny-by-default, auditability, a11y, etc.).
2. Choose the smallest test layer that can catch the regression:
   - logic → unit
   - response shape → contract
   - end-to-end flow → integration
   - keyboard/ARIA → UI/a11y
3. Add minimal fixture inputs in `fixtures/` (synthetic, non-sensitive).
4. If using snapshot/golden outputs, store them in `golden/` and include:
   - expected citation objects
   - expected policy envelope
   - any redaction/generalization markers
5. Ensure the test fails closed:
   - missing citations must fail
   - missing policy decision must fail
   - sensitive fields must never appear unless explicitly allowed

---

## CI gating

Recommended CI requirements for any PR touching Focus Mode:

- [ ] Unit tests pass (`unit/`)
- [ ] API/contract tests pass (`contract/`)
- [ ] Citation schema validation gate passes
- [ ] Policy tests pass (OPA/Rego evaluation, deny-by-default behavior)
- [ ] Audit metadata checks pass (log fields present + redactions applied)
- [ ] Accessibility checks pass (`ui/a11y/`)
- [ ] Security smoke suite passes (token leakage checks, least privilege expectations)
- [ ] Golden snapshot diffs reviewed (if snapshots changed)

> [!WARNING]
> If a PR changes “how citations are generated” or “what fields are returned,” treat it as a **governance-impacting change**.
> It should require the same care as changing policy code.

---

## Troubleshooting patterns

### Failing citation tests

- Missing citation object
- Citation object present but missing identifiers/links
- Citations present but do not correspond to retrieved evidence

### Failing policy tests

- Output includes restricted fields
- Policy engine uncertainty not treated as deny
- Sanitization or post-filter step bypassed

### Flaky LLM tests

- Prefer deterministic stubs in unit tests.
- In integration tests, assert on **structure + identifiers + provenance**, not exact wording.
- If you must assert on content, use anchored snippets derived from fixtures.

---

## References

- KFM Masterpiece Vision: evidence-first, policy-governed, explainable system principles.
- KFM Blueprint and Ideas: Focus Mode guarantees, auditability expectations, trust membrane constraints.
- Deep Research Report on Craft KFM Focus Mode: test matrix coverage categories and quality gates.