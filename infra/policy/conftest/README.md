# Conftest Policy Gate (OPA/Rego) — KFM Governance-as-Code

![Governed](https://img.shields.io/badge/governed-evidence--first-2ea44f)
![Policy](https://img.shields.io/badge/policy-fail--closed-critical)
![Engine](https://img.shields.io/badge/engine-OPA%2FRego-blue)
![Runner](https://img.shields.io/badge/runner-conftest-blueviolet)

> **Purpose:** This folder is the **merge‑blocking governance layer** for Kansas Frontier Matrix (KFM).  
> It runs **OPA/Rego policies** via **Conftest** to deny promotion when required evidence, licensing, provenance, or sensitivity constraints are missing or invalid.

---

## Why this exists

KFM’s core promise is **evidence-first, governed outputs**. In practice, that means:

- **Merges are promotions** (promotion happens through Git workflows).
- Promotion must **fail closed** unless required metadata + provenance + rights are present.
- Policy gates must be **explainable**: failures should tell reviewers exactly what’s missing and how to fix it.

This Conftest policy gate operationalizes those rules in CI and (optionally) in local dev workflows.

---

## What this gate enforces

This folder is intended to hold policies for:

### ✅ “Promotion readiness” invariants (baseline)
- Required catalog fields (STAC / DCAT / PROV)
- SPDX license allow-lists + rights fields
- Evidence pointers (receipts/manifests, digests, attestations)
- Sensitivity labels (public/restricted/sensitive-location/etc.) and redaction expectations
- “Deny-by-default” behavior (`default allow = false`)

### ✅ Ops acceptance gates (when applicable)
- Station telemetry health thresholds (missingness, uptime, gaps)
- Artifact integrity drift detection (etag/last_modified/checksums)

### ✅ Emergency stop
- A **kill-switch** that forces CI checks to fail closed (fast response during incidents)

---

## Trust membrane alignment

This Conftest gate is **CI-time governance**:
- It **does not authorize runtime requests**.
- It **does not grant access** to databases or object stores.
- It only determines whether artifacts **may be promoted** into a governed state.

Runtime authorization is expected to be enforced **separately** (e.g., policy checks in an API boundary).

---

## Directory layout

> This is the **recommended** layout for this folder (adapt as needed, but keep the shape stable for CI and audit reproducibility):

```text
infra/policy/conftest/
├── README.md
├── rego/
│   ├── bundles.rego
│   ├── common/
│   │   ├── helpers.rego
│   │   └── license_allowlist.rego
│   ├── catalogs/
│   │   ├── stac_required.rego
│   │   ├── dcat_required.rego
│   │   └── prov_required.rego
│   ├── gates/
│   │   ├── receipts_pr_gate.rego
│   │   ├── station.rego
│   │   └── artifact.rego
│   └── domains/
│       └── <domain_specific_checks>.rego
└── tests/
    ├── *_test.rego
    └── samples/
        ├── pass/
        └── fail/
```

### What goes where (quick map)

| Path | What it contains | Design rule |
|---|---|---|
| `rego/common/` | shared helpers + allow-lists (licenses, providers, enums) | keep stable + reusable |
| `rego/catalogs/` | STAC/DCAT/PROV required fields | **minimal** + strict |
| `rego/gates/` | merge-blocking “promotion readiness” + ops gates | fail closed |
| `rego/domains/` | domain-specific quality gates | one concern per file |
| `tests/samples/` | golden pass/fail fixtures | **no secrets**, no sensitive coords |
| `tests/*_test.rego` | unit tests for policies | prevent silent drift |

---

## Inputs this gate expects

Policy evaluation depends on **structured inputs** (JSON/YAML). Typical KFM inputs include:

| Input artifact | Typical file(s) | What policy checks |
|---|---|---|
| Run receipt | `run_receipt.json` | `spec_hash`, provider allow-list, timestamps, outputs/digests |
| Run manifest | `run_manifest.json` | attestations/signatures/rights present and non-null |
| Catalog objects | STAC Items/Collections, DCAT datasets, PROV bundles | required keys + cross-links |
| Ops facts | station metrics, artifact recorded/current | thresholds + drift detection |
| Promotion manifest (optional) | `promotion_manifest.json` | intended exposure lane, sensitivity, consent facets |

> **Important:** Policy reliability depends on schema-stable inputs. Treat input schemas as governed contracts.

---

## Run Conftest locally

### 1) Install Conftest
Use your team’s standard toolchain install method (pinned versions strongly recommended).

### 2) Run policy checks against an artifact

From repo root:

```bash
# Run policies in this folder against a receipt
conftest test path/to/run_receipt.json \
  --policy infra/policy/conftest/rego

# Example: validate a run manifest used by PR gates
conftest test path/to/run_manifest.json \
  --policy infra/policy/conftest/rego
```

### 3) Run against a directory of JSON/YAML
Conftest can evaluate multiple files at once:

```bash
# Example: validate a catalog directory (STAC/DCAT/PROV)
conftest test data/ \
  --policy infra/policy/conftest/rego
```

> Tip: Start narrow (only the artifacts you touched) to keep iteration fast.

---

## CI integration expectations

A typical KFM CI flow wires this policy gate as a **required status check**:

```mermaid
flowchart LR
  A[PR opened / updated] --> B[Build / generate artifacts]
  B --> C[Schema validation (JSON Schema + STAC/DCAT/PROV validators)]
  C --> D[Conftest policy gate (fail closed)]
  D -->|allow| E[Branch protection: merge enabled]
  D -->|deny| F[Merge blocked + actionable errors]
```

### Required behaviors
- **Pinned tool versions** for Conftest (and related validators) to reduce toolchain drift.
- **Readable denial output** (deny messages must guide remediation).
- **Branch protection** should block merges if any policy denies.
- Optional but recommended: policy gate runs on **every PR update** and on **main**.

---

## Kill switch (emergency stop)

KFM policy gates should support a fast “stop the line” mechanism.

Recommended patterns:

- A repo file: `.github/KILL_SWITCH`
- An env var: `DEPLOY_KILL_SWITCH=1`

Example CI snippet:

```bash
# Fail closed if kill-switch enabled
if [ -f .github/KILL_SWITCH ] || [ "${DEPLOY_KILL_SWITCH}" = "1" ]; then
  echo "KILL_SWITCH_ACTIVE"
  exit 1
fi
```

> Use during incidents, suspected supply-chain issues, or when policy drift is detected.

---

## Policy authoring guidelines

### Core style rules
- Always start with:

```rego
default allow = false
```

- Prefer `deny[msg] { ... }` rules with **specific**, human-readable messages.
- Keep policies **small and composable**: one file per concern.
- Write policies so audits can reconstruct “why allowed/denied” later.

### Minimal skeleton
```rego
package kfm.example

default allow = false

deny[msg] {
  not input.spec_hash
  msg := "spec_hash is required"
}

allow {
  count(deny) == 0
}
```

### Testing & non-regression
- Add **golden fixtures** under `tests/samples/{pass,fail}`.
- Add `*_test.rego` unit tests to prevent silent drift.
- Maintain a **policy regression suite** for sensitive-field leaks:
  - a query or artifact that previously leaked must **fail forever**
  - include negative tests for sensitive-location precision and small-count aggregates

---

## Governance change control

Policy gates are **system behavior**. Treat changes as production changes:

- ✅ Require review by governance/security owners (CODEOWNERS recommended)
- ✅ Pin tool versions and document updates
- ✅ Include allow/deny fixtures for every new rule
- ✅ Avoid “temporary allow” exceptions; if unavoidable, require:
  - a governance ticket reference
  - a time-bound expiry
  - explicit rationale and risk note

---

## Definition of Done

- [ ] Policies exist for baseline invariants (license, sensitivity, provenance)
- [ ] Deny-by-default is enforced across bundles
- [ ] Every policy includes pass/fail examples (fixtures)
- [ ] CI runs Conftest as a required status check on PRs
- [ ] Kill-switch works and fails closed
- [ ] Policy changes are reviewed + versioned
- [ ] Regression tests exist for at least one known “sensitive leak” case

---

## Troubleshooting

### “Policy passed but shouldn’t have”
- Confirm inputs are schema-valid and include the fields policy expects
- Add a failing fixture + a unit test
- Ensure CI runs policies against the correct artifact paths (not stale outputs)

### “Too many false positives”
- Tighten input normalization (canonicalization, thresholds)
- Move noisy checks into a domain-specific policy pack
- Track deny reasons frequency and tune thresholds with governance review

### “CI errors are unreadable”
- Rewrite deny messages to include:
  - missing field / violated constraint
  - expected value / allow-list
  - minimal fix path

---

## Related (expected in a full KFM scaffold)

- Schemas (run_receipt / run_manifest / watcher registry)
- Catalog validators (STAC, DCAT, PROV)
- Supply-chain verification (signatures, attestations, SBOMs)
- UI evidence viewers (render “why trusted/why denied”)

> If any of these are missing in the repo, keep this policy pack minimal and evolve it slice-by-slice.

---
