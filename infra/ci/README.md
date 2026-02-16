# infra/ci — Governed CI & Merge-Blocking Gates 🛡️✅

![Governed](https://img.shields.io/badge/Governed-YES-brightgreen)
![Policy](https://img.shields.io/badge/Policy-Fail--Closed-critical)
![Determinism](https://img.shields.io/badge/Determinism-Required-blue)
![Provenance](https://img.shields.io/badge/Provenance-PROV%20%2B%20OpenLineage-orange)
![Supply%20Chain](https://img.shields.io/badge/Supply%20Chain-SBOM%20%2B%20Cosign-informational)

> **What this folder is:** the CI “control plane” documentation + glue for KFM’s **governed** pipeline gates.  
> **What this folder is not:** application logic, domain ETL code, or deployment manifests.  
>
> **If a referenced path is missing:** treat it as **TODO**. This README is the contract for what must exist (or be created) to make governance enforceable in CI.

---

## Why CI lives under “governance” rules (KFM core principle)

KFM is a governed system: **merge = promotion**.  
If CI gates are not merge-blocking, governance becomes “policy-by-document only.”

This directory exists to ensure we can say, with confidence:

- **Policies are executable** (OPA/Rego via Conftest) and **block merges** when violated.
- **Schemas are validated** (STAC/DCAT/PROV and KFM-run artifacts) and CI fails on invalid examples.
- **Determinism is enforced** (same inputs/config ⇒ same outputs within tolerance).
- **Provenance is emitted** on PASS and FAIL and stays link-check clean.
- **Supply chain evidence exists** (SBOM + signatures/attestations) and verifies before promotion.

---

## Quick links (repo-local)

- CI workflows (GitHub Actions, expected baseline):
  - `.github/workflows/kfm-ci.yml` (entry workflow; cron/manual + lane fanout)
  - `.github/workflows/reusables/kfm-reusable-ci.yml` (golden lane runner)
  - `.github/workflows/kfm-policy-gate.yml` (merge-blocking Conftest PR gate)
  - `.github/actions/setup-conftest` (pinned Conftest installer action)
- Lane source-of-truth:
  - `manifests/ci/ci_manifest.yml` (single source of truth for lanes)
- Policy pack:
  - `policy/rego/**` + `policy/tests/**`
- Policy gate wiring (expected):
  - `tools/validation/policy/**` (Conftest inputs, policy bundle assembly)
- Supply-chain docs (expected):
  - `docs/security/supply-chain/**` (dependency-confusion, indicators, signatures, etc.)

---

## Directory map (how CI fits into repo structure)

> The goal is **traceability**: you should be able to follow one lane from “manifest → workflow → gates → artifacts”.

```text
repo-root/
├─ .github/
│  ├─ workflows/
│  │  ├─ kfm-ci.yml                         # entry workflow (cron/manual) → lanes
│  │  ├─ kfm-policy-gate.yml                # PR gate: Conftest/OPA fail-closed
│  │  └─ reusables/
│  │     └─ kfm-reusable-ci.yml             # shared lane runner (guardrails, artifacts)
│  └─ actions/
│     └─ setup-conftest/                    # composite action: install pinned Conftest
│
├─ manifests/
│  └─ ci/
│     └─ ci_manifest.yml                    # lanes registry (single source of truth)
│
├─ policy/
│  ├─ rego/                                 # OPA/Rego bundles (common + catalog + domain)
│  └─ tests/                                # Rego unit tests + samples (valid/invalid)
│
├─ tools/
│  └─ validation/
│     ├─ policy/                            # Conftest inputs + bundle selection
│     ├─ schemas/                           # schema validators (STAC/DCAT/PROV/run artifacts)
│     └─ common/                            # determinism/idempotency helpers (expected)
│
└─ infra/
   └─ ci/
      └─ README.md                          # you are here (governed CI contract)
```

---

## CI architecture at a glance

```mermaid
flowchart LR
  A[PR / Push / Schedule] --> B[kfm-policy-gate.yml<br/>Conftest/OPA (fail-closed)]
  A --> C[kfm-ci.yml<br/>lane fanout (reusable workflow)]
  C --> D[kfm-reusable-ci.yml<br/>guardrails + gates + artifacts]
  D --> E[Schema validation<br/>(STAC/DCAT/PROV + run artifacts)]
  D --> F[Determinism checks<br/>(spec_hash/env_snapshot + replay)]
  D --> G[Quality thresholds<br/>(counts/coverage/index health)]
  D --> H[Supply chain evidence<br/>(SBOM + cosign attest/verify)]
  D --> I[Provenance emit<br/>(OpenLineage + PROV-O JSON-LD)]
  B --> J{All gates green?}
  E --> J
  F --> J
  G --> J
  H --> J
  I --> J
  J -- "No" --> K[Merge blocked]
  J -- "Yes" --> L[Merge = Promotion]
  L --> M[GitOps apply (optional lane)<br/>or publish artifacts by digest]
```

---

## Gate set (Definition-of-Done = CI jobs)

Every row here should map to:
1) a CI job and  
2) an artifact that proves the check ran.

| Gate | Fail-closed rule | Typical CI job(s) | Primary evidence artifact(s) |
|---|---|---|---|
| Determinism | Same inputs/config ⇒ same outputs (within tolerance) | `determinism-replay` | `artifacts/determinism_report.json` |
| Schema | STAC/DCAT/PROV + run schemas validate | `schema-validate` | `artifacts/schema_report.json` |
| Governance labels | Sensitivity/sovereignty enums consistent | `policy-gate` | `artifacts/policy_report.json` |
| Provenance | PROV emitted on PASS/FAIL + links valid | `prov-check` + `link-check` | `prov/**/bundle.jsonld` |
| Supply chain | SBOM present + signatures/attestations verify | `sbom` + `cosign-verify` | `artifacts/sbom.*` + cosign attestation |
| Quality | Counts/coverage/index health above thresholds | `quality-threshold` | `artifacts/quality_report.json` |
| Telemetry | Run lifecycle + freshness metrics emitted | `telemetry-check` | `artifacts/openlineage.json` |
| Promotion | Promotion blocked unless all above pass | branch protection + env protection | GitHub required checks |
| Rollback | Failed promotion ⇒ atomic restore + PROV revert bundle | `rollback-sim` | `prov/reverts/**/bundle.jsonld` |

> **Note:** The *policy gate* is merge-blocking by design: CI must deny-by-default for required fields (license/providers/provenance refs/sensitivity).  

---

## Baseline CI workflows (expected “golden path”)

### 1) Entry workflow: `.github/workflows/kfm-ci.yml`
Purpose:
- Cron/manual entry that selects lanes and calls the reusable lane runner.
- Keeps lane differences in **inputs**, not structure.

### 2) Reusable lane runner: `.github/workflows/reusables/kfm-reusable-ci.yml`
Purpose:
- Shared lane runner with:
  - guardrails
  - concurrency
  - artifact packaging
  - consistent stages and evidence outputs

### 3) Merge-blocking policy PR gate: `.github/workflows/kfm-policy-gate.yml`
Purpose:
- Run Conftest/OPA on PRs and **block merges** if policy denies.

### 4) Conftest installer action: `.github/actions/setup-conftest`
Purpose:
- Install pinned Conftest version.
- **Pinning is governance**: treat version bumps as governed changes.

---

## CI guardrails

### Concurrency (recommended defaults)
- Use `cancel-in-progress: true` for PR workflows.
- Prefer short artifact retention for PR runs.
- Keep lane fanout bounded (avoid “run everything always”).

### Kill-switch (fail-closed)
A kill-switch must exist (repo file and/or secret) so maintainers can halt promotions quickly.

Recommended semantics:
- If `KFM_CI_KILL_SWITCH=1` (secret or repo flag), **required checks fail fast** with a clear message.
- “Fail fast” means < 1 minute to block merges on protected branches.

> This is a governance safety valve, not an availability feature.

---

## Policy pack layout (OPA/Rego) — recommended structure

```text
policy/
  rego/
    common/helpers.rego
    common/license_allowlist.rego
    catalogs/stac_required.rego
    catalogs/dcat_required.rego
    catalogs/prov_required.rego
    domains/<domain>_*.rego
    bundles.rego
  tests/
    *_test.rego
    samples/
      valid/
      invalid/
```

**Policy design guideline:**
- Make denies explainable (clear missing field / violated constraint / remediation).
- Treat policy bundles as versioned artifacts (review required).

---

## Provenance & evidence outputs

KFM uses *two complementary provenance streams*:

| Stream | Why it exists | Minimum artifact |
|---|---|---|
| OpenLineage | run-level telemetry (job/run IDs, inputs/outputs, state) | `artifacts/openlineage.json` |
| PROV-O JSON-LD | auditable lineage (entities/activities/agents, used/generated) | `prov/<component>/<ts>/bundle.jsonld` |
| Build provenance + attestations | supply-chain evidence attached to builds & PRs | `artifacts/build_provenance.json` + cosign attestation |

### Idempotent gate semantics
Re-running CI is expected. All sinks should be keyed by an **idempotency key** so repeats don’t create duplicate lineage.

---

## Promotion checklist (merge = promotion) ✅

Use this checklist as the merge gate for any promotion PR:

- [ ] Artifacts are written deterministically (stable IDs; content hashes captured).
- [ ] STAC/DCAT/PROV artifacts exist and validate against schemas.
- [ ] Policy gates (Conftest/OPA) are fail-closed for required fields (license, providers, provenance refs, sensitivity).
- [ ] Attestation/SBOM links are present (or a policy-approved exception is recorded).
- [ ] Graph QA checks show no anomalies (missing attestations, duplicate hrefs, digest mismatches).
- [ ] Rollback plan exists (quarantine prefix, invalidation record in PROV).

---

## Sensitive data & CARE/FAIR safety

CI outputs (logs, receipts, artifacts) can accidentally leak:
- restricted locations
- sensitive identifiers
- private URLs/tokens

Minimum required controls:
- **Classify receipts** (public vs internal vs restricted)
- **Redact** PII / restricted fields in CI artifacts by default
- Keep logs “structural” (events, hashes, counts) rather than dumping raw rows/features
- Add explicit “known leak fixtures” as negative tests

---

## Local developer workflow (parity with CI)

> Goal: “engineers can prove the full loop locally in minutes” (offline + deterministic).

Recommended local checks (mirror CI steps):
- `lint` + `typecheck`
- `schema-validate` (STAC/DCAT/PROV + run artifacts)
- `policy-gate` (Conftest on sample artifacts)
- `smoke-compose` (bring up minimal services and run a smoke test)
- `determinism-replay` (run snapshot + replay check with fixed seed)

If/when scripts exist, place them under:
- `infra/ci/scripts/` (wrapper scripts)
- `tools/validation/**` (source-of-truth check implementations)

---

## Adding a new lane (thin-slice, merge-safe)

<details>
<summary><strong>Step-by-step lane onboarding</strong></summary>

1) **Register the lane**
   - Add to `manifests/ci/ci_manifest.yml` (lane ID, triggers, validators, outputs).

2) **Define contracts**
   - Add schemas (run_manifest, run_receipt, watcher registry) + valid/invalid fixtures.
   - Ensure CI fails on invalid fixtures.

3) **Add policies**
   - Add domain policy bundle in `policy/rego/domains/`
   - Add unit tests in `policy/tests/`

4) **Wire into reusable CI**
   - Ensure the lane uses the shared reusable workflow.
   - Lane-specific behavior should be via inputs, not bespoke job logic.

5) **Evidence artifacts**
   - Emit:
     - `artifacts/*_report.json`
     - `prov/**/bundle.jsonld`
     - (when applicable) SBOM + cosign attestations

6) **Make it merge-blocking**
   - Add required status checks in branch protection for:
     - policy gate
     - schema validation
     - (when enabled) attestation verify

</details>

---

## Updating CI tooling (governed change)

Toolchain drift is a top CI risk (Conftest/Cosign/schema tooling). Minimum mitigation:
- Pin versions
- Add regression suites (policy unit tests + schema fixtures + determinism tests)
- Treat version bumps like production changes (review + changelog + rollback plan)

---

## Troubleshooting (fast triage)

| Symptom | Likely cause | First check |
|---|---|---|
| Policy gate fails unexpectedly | new required field or stricter rule | `artifacts/policy_report.json` deny message |
| Schema validate fails | fixture invalid / schema changed | `artifacts/schema_report.json` + fixture diff |
| Determinism fails | unpinned deps / unordered JSON / network calls | compare `spec_hash` + `env_snapshot` + inputs |
| Cosign verify fails | missing OIDC perms / wrong digest | workflow permissions + digest logs |
| “Green but untrustworthy” | verification UX confusion | ensure UI surfaces “why” + evidence links |

---

## References (repo-local)

- CI baseline: `.github/workflows/*` (reusable lanes + Conftest PR gate + OIDC)
- Policy pack: `policy/rego/**`, `policy/tests/**`
- CI lane registry: `manifests/ci/ci_manifest.yml`
- Supply chain / dependency confusion defenses:
  - `docs/security/supply-chain/dependency-confusion/checks/*`
  - `docs/security/supply-chain/shai-hulud-2.0/**`

---

## Definition of Done for infra/ci (this folder)

- [ ] CI policy gate is merge-blocking on PRs (fail-closed).
- [ ] Schema fixture validation runs in CI (valid + invalid).
- [ ] Tool versions are pinned (Conftest/Cosign/etc.).
- [ ] Kill-switch exists and is tested (fast block semantics).
- [ ] CI outputs include evidence artifacts (reports + provenance).
- [ ] Sensitive-data leakage tests exist (“known leak fixtures”).
