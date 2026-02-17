# 🧾 Audit Tests (Governance + Trust Membrane)

![tests/audit](https://img.shields.io/badge/tests-audit-blue)
![policy](https://img.shields.io/badge/policy-fail--closed-critical)
![provenance](https://img.shields.io/badge/provenance-required-brightgreen)

KFM is a **governed evidence system**, not “just an app.” This folder is the **audit test suite** that enforces the project’s non‑negotiables in code and CI: **evidence-first**, **fail-closed policy gates**, **sensitivity/sovereignty controls**, and the **trust membrane** (clients never touch storage directly; access flows through governed APIs with policy + audit logging).  

> [!IMPORTANT]
> **Audit tests are allowed to block merges and promotions.**  
> If a rule is “governance load-bearing,” it belongs here (or is referenced by something here).

---

## What counts as an audit test?

An **audit test** is any automated check that verifies a *governance invariant* or a *promotion requirement*, including (but not limited to):

- **Trust membrane enforcement**
  - UI / external clients **must not** access PostGIS / Neo4j / object store directly.
  - Backend domain/use-case layers **must not** bypass repository interfaces or policy boundary logic.
- **Policy-as-code gates (fail-closed)**
  - Missing required labels/fields/signatures → **deny by default**.
  - CARE/sensitivity rules apply at promotion and/or request time.
- **Evidence + provenance integrity**
  - “Cite or abstain” expectations for user-visible outputs (Focus Mode / Story Nodes).
  - Outputs must reference **DatasetVersion(s)** and/or **source_record_id(s)** as applicable.
- **Redaction & restricted-access regression**
  - “Golden queries” that leaked restricted fields must **fail forever**.
  - Precise sensitive locations must be generalized/suppressed for unauthorized roles.
- **Audit integrity**
  - Responses must include **audit reference** + **evidence bundle hash** (or equivalent receipt linkage).
- **Promotion safety**
  - Raw → Work → Processed promotion requirements, catalog completeness, checksums, and signatures.

---

## Directory layout

> [!NOTE]
> The exact file/folder names below are a **recommended shape**. If your repo differs, update this README to match the real layout.

```text
tests/
└── audit/
    ├── README.md
    ├── registry/                 # (recommended) audit registry + metadata
    ├── checks/                   # audit implementations (code)
    ├── policies/                 # (optional) OPA/Rego bundles + conftest tests
    ├── fixtures/                 # synthetic + redacted test data only
    ├── schemas/                  # JSON Schemas for manifests/reports (if used)
    └── reports/                  # generated outputs (SHOULD be gitignored)
```

| Path | Purpose | Must be safe to publish? |
|---|---|---|
| `checks/` | Test implementations (policy gates, provenance checks, contract checks, etc.) | ✅ Yes |
| `policies/` | Policy-as-code bundles and policy regression tests | ✅ Yes |
| `fixtures/` | **Synthetic** data + redacted examples used by audits | ✅ Yes (no secrets / no precise sensitive coords) |
| `schemas/` | Schemas for manifests, catalogs, audit outputs | ✅ Yes |
| `reports/` | CI artifacts (JUnit/SARIF/JSON summaries) | ✅ Yes (but **do not commit**) |

---

## Audit gates

Audit tests typically map to one (or more) gates:

| Gate | When it runs | What it protects |
|---|---|---|
| **Pre-merge** | Pull request checks | Prevent regressions and policy drift |
| **Pre-promotion** | Before publish/promotion | Fail-closed governance: licensing, CARE/sensitivity, signature/attestation |
| **Runtime** | On request (API boundary) | Policy evaluation, redaction/query shaping, audit logging |
| **Release** | Build/release pipelines | Supply chain integrity + immutability |

```mermaid
flowchart LR
  PR[PR / Change] --> CI[CI: Build + Unit/Integration]
  CI --> AUD[Audit Suite (tests/audit)]
  AUD -->|PASS| MERGE[Merge Allowed]
  AUD -->|FAIL| BLOCK[Block Merge/Promotion]

  MERGE --> PROMO[Promotion Lane]
  PROMO --> POLICY[Policy Gates (fail-closed)]
  POLICY -->|PASS| PUBLISH[Publish / Deploy]
  POLICY -->|FAIL| ROLLBACK[Rollback-first + evidence of failure]
```

---

## Audit registry

This table is a **living index** of “blocking” audits. Keep it short and high-signal.

| Audit ID | Name | Gate | Severity | Primary Artifact(s) | Status |
|---|---|---|---|---|---|
| `AUD-001` | Trust membrane: UI cannot access storage directly | Pre-merge | Blocking | source code / dependency graph | ⏳ implement |
| `AUD-010` | API responses include audit ref + evidence bundle hash | Runtime | Blocking | HTTP responses / receipts | ⏳ implement |
| `AUD-020` | Sensitive-location redaction regression suite | Pre-merge + Runtime | Blocking | policy tests + golden queries | ⏳ implement |
| `AUD-030` | CARE promotion gate for authoritative Tribal boundary intersections | Pre-promotion | Blocking | promotion manifest + policy report | ⏳ implement |
| `AUD-040` | PROV bundle emitted on PASS **and** FAIL | Pre-promotion | Blocking | PROV bundles / signatures | ⏳ implement |

> [!TIP]
> If an audit is **blocking**, give it:
> - a stable `AUD-###` identifier
> - a brief “why it exists”
> - a machine-readable report output (at least JSON)

---

## Running audits locally

> [!NOTE]
> Commands below are examples (**not confirmed in repo**). Prefer the repo’s canonical task runner if present (e.g., `make audit`, `just audit`, `npm run audit`, etc.).

### Quick run (example)
```bash
# Example only: adapt to repo tooling
pytest -q tests/audit
```

### Generate CI-friendly reports (example)
```bash
# Example only
pytest tests/audit \
  --junitxml=tests/audit/reports/junit.xml \
  --maxfail=1
```

### Policy pack tests (example)
```bash
# Example only (if using OPA/Conftest)
conftest test tests/audit/policies -o table
```

---

## Required outputs

Audit runs should emit **machine-readable** artifacts so CI can:

- block merges/promotions on violations
- attach evidence to PRs
- support later forensic review (“why did this fail?”)

Recommended minimum outputs:

1. **Human summary** (Markdown or console output)
2. **Machine report** (JSON)
3. **CI format** (JUnit XML and/or SARIF) if your platform supports it

### Suggested JSON shape (recommended)
```json
{
  "audit_id": "AUD-010",
  "status": "FAIL",
  "severity": "BLOCKING",
  "gate": ["runtime"],
  "summary": "Missing audit reference on /evidence/resolve response",
  "evidence": {
    "request": {"method": "GET", "path": "/evidence/resolve"},
    "expected_fields": ["audit_ref", "evidence_bundle_hash"],
    "observed_fields": ["citations"]
  },
  "artifacts": [
    {"kind": "http_response_sample", "uri": "tests/audit/reports/AUD-010-response.json"}
  ]
}
```

---

## Non-regression requirements (what must never slip)

These are the patterns that justify having a dedicated audit suite:

- **Golden queries** that once leaked restricted fields must fail forever.
- **Negative tests** must prove sensitive-location layers can’t be returned at high precision to unauthorized roles.
- **Field-level redaction tests** must cover known restricted fields (e.g., ownership names; small-count aggregates).
- **Audit integrity tests** must ensure responses include an audit reference + evidence bundle hash (or equivalent receipt).  

> [!WARNING]
> If an audit asserts a governance rule, it should include **at least one negative test** (a deliberate violation) so we know the gate is real.

---

## Sensitivity & safety rules for test data

KFM audits must not accidentally become a distribution channel for sensitive info.

- ✅ Use **synthetic** fixtures by default.
- ✅ If you must mimic sensitive-location behavior, use:
  - generalized geometry
  - jittered coordinates
  - or “representative” bounding boxes
- ❌ Never commit precise locations for protected archaeology / culturally restricted sites.
- ❌ Never commit secrets, tokens, or private credentials (even “test” ones).

---

## Adding a new audit

1. **Write the spec first** (1–2 paragraphs): what invariant are we enforcing and why is it load-bearing?
2. Implement the test in `checks/` (or existing test harness folder).
3. Add at least:
   - one passing case
   - one failing case
4. Emit a report artifact (JSON strongly preferred).
5. Add the audit to the registry table in this README.

<details>
<summary><strong>Audit spec template</strong> (copy/paste)</summary>

**Audit ID:** `AUD-___`  
**Name:** `<short name>`  
**Gate:** `pre-merge | pre-promotion | runtime | release`  
**Severity:** `blocking | warn`  
**Invariant:** `<what must always be true>`  
**Failure mode:** `<what risk happens if it breaks>`  
**Evidence produced:** `<paths or report ids>`  
**Negative test included:** `yes/no`

</details>

---

## Definition of Done (DoD) for audit contributions

- [ ] Test is deterministic (no flaky timing / no uncontrolled external calls).
- [ ] Test is fail-closed for governance invariants.
- [ ] Includes negative test(s) that prove the gate actually blocks violations.
- [ ] Uses fixtures that are safe to publish (synthetic/redacted).
- [ ] Produces machine-readable output (JSON; plus JUnit/SARIF if used).
- [ ] Runtime audits do **not** log secrets or sensitive payloads.
- [ ] README registry updated if the audit is blocking.

---

## Troubleshooting

<details>
<summary><strong>Common failure patterns</strong></summary>

- **Policy tests pass locally but fail in CI**
  - Check policy bundle versions and pinned tool versions (OPA/conftest/etc.).
- **Audit depends on live services**
  - Replace with contract tests + recorded fixtures; use service emulators if needed.
- **Redaction tests are hard to write**
  - Start with explicit “known-leak” golden cases and keep them permanently.

</details>
