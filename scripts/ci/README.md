<!--
File: scripts/ci/README.md
Purpose: Governed, fail-closed CI scripts for Kansas Frontier Matrix (KFM)
-->

# KFM CI Scripts (`scripts/ci/`) 🧪🛡️

![Governed](https://img.shields.io/badge/Governed-yes-2b6cb0)
![Fail Closed](https://img.shields.io/badge/CI-fail--closed-critical)
![Policy](https://img.shields.io/badge/Policy-OPA%2FConftest-informational)
![Supply Chain](https://img.shields.io/badge/Supply%20Chain-SBOM%20%2B%20Attestations-blueviolet)
![Provenance](https://img.shields.io/badge/Provenance-PROV%20%2B%20Receipts-brightgreen)

> [!IMPORTANT]
> KFM’s CI is not “just tests.” It is a **governance enforcement mechanism**.
> These scripts are expected to block merges when:
> - evidence/provenance is missing,
> - sensitivity/sovereignty handling is inconsistent,
> - contracts drift,
> - supply-chain integrity is unverifiable,
> - or “trust membrane” boundaries are violated.

---

## What this folder is

This folder contains **portable CI gate scripts** that must run:

- **locally** (developer laptops / dev containers), and
- in **CI** (GitHub Actions / Jenkins / Tekton / etc.)

The design goal is a **single command interface** that makes CI behavior reproducible and catchable *before* a PR is opened.

---

## Non-negotiable invariants

### ✅ Fail closed (default deny)
If a gate cannot decide safely (missing metadata, missing signature, unknown policy bundle, ambiguous classification), it **fails**.

### ✅ Evidence-first
CI must enforce:
- provenance creation (PASS and FAIL),
- catalog linkage (STAC/DCAT → PROV/receipt),
- and “cite or abstain” rules for narrative artifacts (Story Nodes / Focus Mode outputs).

### ✅ Trust membrane preservation
CI should actively prevent patterns that bypass governance boundaries (e.g., UI code reaching into data stores directly, or services bypassing repository interfaces).

### ✅ Determinism where possible
Same inputs + same config should produce the same outputs (within tolerance for stochastic steps). Where determinism is not possible, CI must enforce explicit “seed/config capture” and controlled variance.

---

## Directory layout

> [!NOTE]
> This README defines the **recommended contract** for this directory. If your repo’s scripts differ, update this tree to match reality.

```text
scripts/ci/
├── README.md                  # you are here
├── run.sh                      # runs the full CI gate set (fail-closed)
├── env.example                 # optional: example env vars for local runs
├── lib/
│   ├── common.sh               # logging, temp dirs, artifact helpers
│   └── tools.sh                # tool detection + version checks
├── checks/
│   ├── 00_format.sh            # fmt/lint (fast)
│   ├── 10_unit.sh              # unit tests
│   ├── 20_contracts.sh         # OpenAPI/GraphQL schema lint + contract tests
│   ├── 30_schema_stac_dcat.sh   # STAC/DCAT schema validation
│   ├── 35_prov_linkcheck.sh     # PROV existence + link integrity
│   ├── 40_policy_opa.sh         # OPA/Conftest policy gates
│   ├── 50_sensitive_scans.sh    # secrets/PII/sensitive-locations/classification checks
│   ├── 60_supply_chain.sh       # SBOM + attest/verify + policy gate
│   ├── 70_quality.sh            # row counts / tile coverage / index health thresholds
│   ├── 80_telemetry.sh          # telemetry schema + freshness checks
│   └── 90_rollback_test.sh      # simulate failed promotion → atomic restore + PROV revert bundle
└── policies/
    ├── rego/                    # OPA policies
    └── data/                    # policy data bundles (enums, sovereignty mappings, etc.)
```

---

## Quick start (local)

```bash
# Run the full gate set
./scripts/ci/run.sh

# Run one gate directly
./scripts/ci/checks/40_policy_opa.sh

# Typical “fast” loop (format + unit)
./scripts/ci/checks/00_format.sh
./scripts/ci/checks/10_unit.sh
```

> [!TIP]
> Make sure `run.sh` is what your CI invokes so “local == CI” remains true.

---

## CI gate set (Definition of Done)

Each row should correspond to **a CI job** or a **contract test**. The gates are intentionally “fail closed.”

| Gate | What must be true | Typical artifacts (examples) |
|---|---|---|
| Determinism | Re-runs are stable within tolerance; configs captured | `run-receipt.json`, `config.snapshot.json` |
| Schema | Canonical schemas validate (code + catalogs) | schema reports, validator logs |
| Governance labels | Sensitivity / sovereignty enums consistent across STAC/DCAT/PROV | conftest output, enum diff |
| Provenance | PROV emitted on PASS and FAIL; linked from catalogs | `prov.jsonld`, linkcheck report |
| Supply chain | SBOM present; signatures/attestations verified | `sbom.spdx.json` or `sbom.cdx.json`, `slsa.att.json` |
| Quality | Coverage/health thresholds met | quality report + threshold summary |
| Telemetry | Run lifecycle/freshness metrics emitted + schema-valid | telemetry JSON, schema report |
| Promotion | Promotion blocked unless all above pass; prod requires review | promotion decision log |
| Rollback | Failed promotion triggers atomic restore + PROV revert bundle | rollback test report, revert PROV |

---

## Security & governance scans

CI should include **automated scanning** (and block merges) for:

- secrets (keys/tokens/passwords),
- PII and unintended sensitive content,
- sensitive location exposures (e.g., protected coordinates),
- classification downgrades without approved de-identification.

> [!IMPORTANT]
> These scans are part of KFM governance: if a dataset includes names or precise coordinates, CI should flag it unless the proper permissioning / generalization / redaction workflow is present.

---

## Supply-chain evidence (SBOM + attestations)

CI should support a “fail-closed” flow like:

1. build artifact (container / bundle / dataset output)
2. generate SBOM
3. attach/attest provenance
4. verify signatures
5. policy-gate the results

```yaml
# Example (illustrative): SBOM + provenance + fail-closed verification
- name: SBOM + provenance + attach/attest
  run: |
    syft $IMAGE -o cyclonedx-json > sbom.cdx.json
    cosign attach sbom --sbom sbom.cdx.json $IMAGE
    cosign attest --predicate slsa-provenance.json --type https://slsa.dev/provenance $IMAGE

- name: Verify signatures
  run: cosign verify $IMAGE

- name: Policy gate (fail-closed)
  run: |
    conftest test slsa.att.json
    conftest test sbom.cdx.json
```

> [!NOTE]
> For PRs: it’s acceptable to generate/verify attestations without publishing “official” release artifacts.
> For releases: expect stronger signing + publishing requirements.

---

## CI/CD and GitOps alignment

KFM treats **CI** as the synchronous “build/test/verify” step and **CD** as a separate concern that can be managed via **GitOps reconciliation** (controller-driven desired state).

```mermaid
flowchart LR
  A[PR opened / commit pushed] --> B[CI scripts run (synchronous)]
  B -->|all gates pass| C[Merge allowed]
  C --> D[Desired state updated in Git]
  D --> E[GitOps controller reconciles (asynchronous)]
  E --> F[Environment matches desired state]
```

Key mindset shifts:

- Promote **manifests/desired state** (and digest-pinned artifacts), not “whatever was last built.”
- Keep CI reproducible and local-friendly: consistent commands for build/test/push-like operations.

---

## Governance review triggers (manual)

Some changes should *automatically* require a human governance review in addition to CI:

- introducing sensitive/culturally restricted layers,
- new AI-driven narrative features that could be perceived as factual,
- onboarding new external data sources (license + provenance review).

> [!IMPORTANT]
> A “green CI” is necessary, not sufficient, when these triggers apply.

---

## Adding a new CI gate

1. Create a new script in `scripts/ci/checks/` with a numeric prefix for ordering.
2. Ensure it:
   - uses strict mode (`set -euo pipefail`)
   - emits machine-readable artifacts (JSON) where possible
   - writes artifacts under a common artifacts directory
   - returns non-zero on failure
3. Wire it into `scripts/ci/run.sh` (and keep the gate table updated).

### Gate script skeleton

```bash
#!/usr/bin/env bash
set -euo pipefail

GATE_ID="40_policy_opa"
ARTIFACT_DIR="${KFM_CI_ARTIFACTS_DIR:-./artifacts/ci}/${GATE_ID}"
mkdir -p "$ARTIFACT_DIR"

echo "[${GATE_ID}] running..."

# ... do work ...
# write reports to "$ARTIFACT_DIR"

echo "[${GATE_ID}] PASS"
```

---

## Troubleshooting

<details>
  <summary><strong>Common failure patterns</strong></summary>

- **Schema validation fails**: a catalog file changed but wasn’t updated to match the canonical schema; run the schema gate locally and inspect the artifact report.
- **Policy gate fails**: sovereignty/sensitivity enums mismatch across STAC/DCAT/PROV; inspect the conftest output and enum mapping file.
- **Provenance missing**: pipeline produced outputs but didn’t emit PROV/receipt; treat as a hard failure—wire provenance generation into the pipeline step.
- **Supply chain fails**: artifact not signed, attestation missing, or verification policy too strict; fix the build pipeline rather than relaxing the policy by default.

</details>

---

## Maintainer checklist

- [ ] `scripts/ci/run.sh` runs successfully on a clean machine (or dev container).
- [ ] Every gate produces artifacts that help debug failures.
- [ ] Policy exceptions require a governance ticket reference.
- [ ] README gate table matches actual scripts and CI configuration.
- [ ] CI changes are treated as production-impacting (review accordingly).

---
