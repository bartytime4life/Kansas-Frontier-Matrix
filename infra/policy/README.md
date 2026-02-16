# 🛡️ infra/policy — KFM Policy-as-Code (OPA/Rego)

![Governed](https://img.shields.io/badge/Governed-Policy%20as%20Code-2b6cb0)
![Fail Closed](https://img.shields.io/badge/Default-Deny%20%2F%20Fail--Closed-8b0000)
![Trust Membrane](https://img.shields.io/badge/Boundary-Trust%20Membrane-5a67d8)
![FAIR+CARE](https://img.shields.io/badge/Principles-FAIR%20%2B%20CARE-0f766e)

KFM treats **governance as executable code**. This folder contains the **policy bundles** that enforce:

- **Evidence-first** behavior: “cite-or-abstain” for user-visible claims
- **Fail-closed** promotion & access control (deny-by-default)
- **License + rights** compliance gates
- **Sensitivity + CARE** constraints (including consent-dependent promotion lanes)
- **Supply-chain + provenance** expectations for promoted artifacts (attestations / receipts / manifests)

> [!IMPORTANT]
> **Trust membrane rule:** Frontends and external clients never access storage directly.
> All access crosses the trust membrane through the **Governed API**, which calls the **Policy Decision Point** (OPA) and applies returned **obligations** (e.g., redaction/generalization).  
> CI uses the *same* core policy semantics and fixtures so “governance is enforced” is a system guarantee, not a best-effort guideline.

---

## 📚 Table of contents

- [What this folder is](#-what-this-folder-is)
- [Non-negotiable invariants](#-non-negotiable-invariants)
- [Directory layout](#-directory-layout)
- [Where policies run](#-where-policies-run)
- [Policy conventions](#-policy-conventions)
- [Inputs and outputs](#-inputs-and-outputs)
- [Local development](#-local-development)
- [CI integration](#-ci-integration)
- [Kill switch](#-kill-switch)
- [Governance workflow](#-governance-workflow)
- [Definition of Done](#-definition-of-done)
- [Glossary](#-glossary)

---

## ✅ What this folder is

This directory is the **single source of truth** for KFM governance rules implemented as **OPA/Rego** policy bundles.

It is used in two places:

1. **CI merge gates** (Conftest + OPA/Rego): block merges if governance requirements are not met.
2. **Runtime request gates** (OPA PDP): authorize/deny requests and return **obligations** (redaction, generalization, partial responses).

---

## 🔒 Non-negotiable invariants

These are treated as *build invariants* across the platform:

| Invariant | Meaning in practice | Typical enforcement point |
|---|---|---|
| **Default deny** | If policy lacks required facts/metadata, it denies. | CI + runtime |
| **Fail closed** | Missing receipts/manifests/provenance → no merge / no publish / no serve. | CI merge gate; promotion gate |
| **Determinism** | Stable IDs/hashes; generated artifacts are reproducible. | CI (artifact generation + validation) |
| **Kill switch** | One flag can halt promotion automation immediately. | CI + runner entrypoint |
| **Network boundaries** | No direct writes to prod stores; changes flow via PRs. | CI orchestration + infra |
| **Explainability** | Deny messages must tell you exactly what failed and how to fix it. | Rego design rule |

---

## 🗂️ Directory layout

Recommended default layout (adjust to match repo conventions):

```text
infra/policy/
├── README.md
├── VERSION                         # SemVer for the policy pack (required)
├── conftest.toml                    # Conftest config (namespaces, data roots)
├── rego/
│   ├── bundles.rego                 # Optional: central bundle wiring / shared exports
│   ├── common/
│   │   ├── helpers.rego
│   │   └── license_allowlist.rego
│   ├── catalogs/
│   │   ├── stac_required.rego
│   │   ├── dcat_required.rego
│   │   └── prov_required.rego
│   ├── promotion/
│   │   ├── receipts_pr_gate.rego    # PR/promotion lane gate: receipts + rights + attestations
│   │   ├── care_tribal_gate.rego    # CARE: consent/authority-to-control checks
│   │   └── sensitivity_redaction.rego
│   ├── runtime/
│   │   ├── access_control.rego      # can user access dataset/version/record?
│   │   └── obligations.rego         # redaction/generalization obligations model
│   ├── ai/
│   │   ├── cite_or_abstain.rego     # Focus Mode / Story outputs must cite or abstain
│   │   └── disallowed_content.rego  # content rules (project-specific)
│   └── domains/
│       ├── station_qc.rego          # example: domain QC gates
│       └── artifact_integrity.rego  # example: artifact immutability checks
└── tests/
    ├── rego/
    │   ├── *_test.rego              # opa test unit tests
    │   └── README.md                # how to run tests & add fixtures
    └── fixtures/
        ├── pass/
        └── fail/
```

> [!NOTE]
> Keep policies **small and composable** (one file per concern), and maintain **golden pass/fail fixtures** to prevent silent policy drift.

---

## 🧭 Where policies run

```mermaid
flowchart LR
  subgraph CI["CI (merge gate)"]
    A[Changed artifacts] --> V[Schema + link validation]
    V --> P[OPA/Rego policy checks (default deny)]
    P --> G{All green?}
    G -->|yes| M[Merge allowed]
    G -->|no| B[Merge blocked with deny reasons]
  end

  subgraph Runtime["Runtime (trust membrane)"]
    UI[UI / external clients] --> API[Governed API]
    API --> PDP[Policy Decision Point (OPA)]
    PDP -->|allow/deny + obligations| API
    API --> STORES[(PostGIS / Object Store / Graph / Search)]
  end
```

### CI responsibilities
- Validate catalogs (STAC/DCAT/PROV) & schemas
- Verify required receipts/manifests exist and are complete
- Enforce licensing/sensitivity/CARE gates
- Block merges unless all checks pass
- Emit machine-readable denial reports as build artifacts

### Runtime responsibilities
- Authorize dataset/version/record access
- Apply obligations:
  - **redact** fields
  - **generalize** location resolution
  - **deny** export/download
  - **return safe abstention** (without leaking restricted metadata)

---

## 🧱 Policy conventions

### 1) Default deny
All gate-style policies should default to deny (fail-closed). Example shape:

```rego
package kfm.gates

default allow := false

allow {
  # explicit required conditions
}

deny[msg] {
  not allow
  msg := "explainable_reason_here"
}
```

### 2) Deny messages must be “fix-forward”
A deny message should include:
- what is missing/invalid
- where to add it (file path / field)
- what value format is expected
- whether an exception path exists (and how to reference the governance ticket)

### 3) Policies are **versioned**
- Every change bumps `infra/policy/VERSION`.
- CI should export the **policy version** and ideally a **bundle hash** (e.g., SHA-256 over policy directory) into:
  - run manifests / receipts
  - audit logs
  - any “why was this denied?” payloads

---

## 📥 Inputs and outputs

### Inputs (typical)
Policies generally evaluate one of these inputs:

| Input name | What it represents | Typical producer |
|---|---|---|
| `run_receipt` | Per-run receipt (what happened, inputs/outputs, checks) | pipeline executor |
| `run_manifest` | “promotion intent” + proofs (rights, attestations, sig refs) | CI lane |
| `promotion_manifest` | Policy input for “publish/promotion” decisions | promotion service |
| `access_request` | Runtime query/access context (user, role, dataset, sensitivity) | API gateway |

### Output pattern
Prefer a structured decision object:

```json
{
  "allow": false,
  "deny_reasons": ["missing_license", "missing_prov_bundle"],
  "obligations": [
    {"type": "redact_fields", "fields": ["owner_name", "precise_location"]},
    {"type": "generalize_geometry", "precision": "geohash5"}
  ],
  "policy_version": "0.1.0"
}
```

---

## 🧪 Local development

### Run policy tests (OPA unit tests)
```bash
opa test ./infra/policy/rego ./infra/policy/tests/rego -v
```

### Run Conftest locally (CI parity)
```bash
conftest test \
  --policy ./infra/policy/rego \
  --all-namespaces \
  ./path/to/artifacts-or-json
```

### Add a new fixture
1. Add a minimal JSON input to `tests/fixtures/pass/` or `tests/fixtures/fail/`
2. Add a `_test.rego` test that asserts allow/deny and the exact deny reasons
3. Ensure deny messages are stable and readable (avoid nondeterministic ordering)

---

## 🤖 CI integration

Minimum expectation:
- A PR workflow runs Conftest/OPA on all changed governed artifacts.
- Branch protection requires the policy gate to pass.
- Exceptions must reference a governance ticket (and should be auditable).

> [!TIP]
> Treat toolchain upgrades (Conftest/OPA/Cosign/STAC validators) as **governed changes**:
> pin versions and update fixtures/tests in the same PR.

---

## 🧯 Kill switch

KFM policy gates support a **kill switch** to stop promotion automation immediately.

Recommended implementation:
- repo file: `.github/KILL_SWITCH` **OR**
- CI secret/env: `DEPLOY_KILL_SWITCH=1`

CI entrypoint must fail closed when active.

```bash
if [ -f .github/KILL_SWITCH ] || [ "${DEPLOY_KILL_SWITCH}" = "1" ]; then
  echo "KILL_SWITCH_ACTIVE"
  exit 1
fi
```

---

## 🏛️ Governance workflow

Policy changes are production changes.

**Required reviewers** (recommendation):
- Platform/Infra reviewer (policy execution + CI wiring)
- Data governance reviewer (license/rights/sensitivity/CARE changes)
- Domain reviewer (domain QC gates)

**Change process**
1. Create PR with:
   - policy changes
   - fixture updates
   - `_test.rego` updates
   - `VERSION` bump
2. CI must produce:
   - policy test reports
   - deny reason diffs (if any)
3. Merge only after required reviewers approve.

---

## ✅ Definition of Done

For any policy change PR:

- [ ] `infra/policy/VERSION` bumped (SemVer)
- [ ] New/changed rules have **unit tests** (`*_test.rego`)
- [ ] Golden fixtures updated or added (`tests/fixtures/pass|fail`)
- [ ] Deny messages are explainable and stable
- [ ] CI gate runs Conftest with pinned versions
- [ ] If change affects CARE/sensitivity/rights: governance reviewer approved
- [ ] If change introduces exception behavior: exception path requires governance ticket reference

---

## 📖 Glossary

- **OPA**: Open Policy Agent — evaluates Rego policies.
- **PDP**: Policy Decision Point — the component that returns allow/deny + obligations.
- **Obligations**: Required transformations applied when allowed (e.g., redaction).
- **Fail-closed**: Missing required evidence → deny (safer than “best effort”).
- **Promotion**: Making a dataset/version visible or usable in downstream systems/UI.
- **Evidence-first**: User-visible claims must resolve to source evidence or abstain.

---
