# `infra/ci/scripts/` 🧰

![Scope](https://img.shields.io/badge/scope-infra%2Fci%2Fscripts-blue)
![Contract](https://img.shields.io/badge/contract-stable%20CLI%20interface-brightgreen)
![Governance](https://img.shields.io/badge/governance-policy%20gates%20%2B%20provenance-orange)

Scripts in this directory are **CI building blocks**: small, composable utilities that implement *governed* checks and repeatable automation steps (validation, scanning, provenance emission, promotion helpers, etc.).

They are intended to be called from:
- GitHub Actions / Jenkins / Tekton / GitLab CI (runner-agnostic)
- local developer workflows **only when explicitly safe** (e.g., validation-only scripts)

---

## ✅ What belongs here

**Put a script here if it is:**
- used by CI (or will be soon),
- deterministic and non-interactive,
- safe to re-run (idempotent where practical),
- capable of producing auditable artifacts (logs, reports, provenance bundles),
- compatible with KFM governance + trust membrane rules.

**Do _not_ put here:**
- one-off personal utilities,
- scripts that assume direct DB access from CI,
- scripts that embed secrets or bypass policy gates.

> [!IMPORTANT]
> **Trust membrane rule:** no frontend / external clients talk directly to storage. CI scripts should also avoid “backdoor” access paths: prefer governed APIs/ports and least-privilege service identities.  
> If a script needs privileged access (e.g., signing keys, deployment tokens), it must be gated, auditable, and reviewed.

---

## 📦 Script contract (required)

All scripts in this directory **must** follow this contract:

### CLI interface
- `--help` prints usage and exits `0`
- `--version` prints a version string and exits `0` (can be `git describe`-based)
- **No interactive prompts** (CI-safe)
- **Exit codes:**
  - `0` success
  - `1` validation failure / policy gate failed
  - `2` misconfiguration / missing dependency
  - `>=3` unexpected runtime errors

### Logging & outputs
- Log to **stderr** for human-readable logs.
- Emit **machine-readable** artifacts to `${KFM_ARTIFACTS_DIR}` (default: `./artifacts/ci`).
- Never print secrets (token redaction required).

### Determinism & idempotency
- Prefer content-addressed outputs (digests) where relevant.
- Re-running a script with identical inputs should produce identical outputs.

---

## 🔧 Quickstart

From repo root:

```bash
# List scripts
ls -la infra/ci/scripts

# Example: run help
bash infra/ci/scripts/<script>.sh --help

# Example: run a gate (paths and names are repo-specific)
KFM_ARTIFACTS_DIR=./artifacts/ci \
bash infra/ci/scripts/<gate-script>.sh --input ./catalog --policy ./policy
```

> [!TIP]
> If you’re running locally, set `CI=false` (or omit it). Some scripts may tighten behavior when `CI=true` (e.g., fail on warnings).

---

## 🗺️ Recommended layout inside `infra/ci/scripts/` (pattern)

> [!NOTE]
> The exact filenames in your repo may differ. Treat this as the **recommended organization** and update as needed.

```text
infra/ci/scripts/
├─ README.md
├─ lib/                    # shared shell helpers (logging, json, env)
├─ gates/                  # policy, provenance, signature verification, QA gates
├─ build/                  # build + package helpers (containers, artifacts, SBOM)
├─ promote/                # promotion helpers (update manifests, open PRs, tag images)
└─ dev/                    # safe local-only helpers (validation, formatting, etc.)
```

---

## 🔐 Governance gates implemented here

KFM CI should include (at minimum):

1) **Policy gates**  
   - Run Conftest/OPA (Rego) against governed metadata outputs (e.g., STAC/DCAT/PROV JSON) to enforce required keys/allowed values.
   - Block merge if policy fails; exceptions require a governance ticket reference.

2) **Supply-chain gates**  
   - Verify Cosign/Sigstore signatures and (where used) SLSA provenance attestations **before** promotion.
   - Prefer digest-pinned artifacts (avoid mutable tags for trust decisions).

3) **Provenance emission**  
   - Emit a PROV bundle (JSON-LD or other approved serialization) describing:
     - inputs (entities),
     - steps (activities),
     - responsible actors (agents),
     - outputs (entities),
     - and links to SBOM / checksums / artifacts.

> [!IMPORTANT]
> If a script changes what gets promoted or published, it is a **governed change**. Treat updates to these scripts like production changes: code review, tests, auditability, and rollback plan.

---

## 🔁 How these scripts fit into CI/CD (GitOps-friendly)

```mermaid
flowchart LR
  A[Commit / PR] --> B[CI: build + test]
  B --> C[Generate artifacts\n(COG/PMTiles/GeoParquet/Images)]
  C --> D[Generate SBOM + checksums]
  D --> E[Emit provenance\n(PROV/OpenLineage)]
  E --> F[Policy gates\n(Conftest/OPA)]
  F --> G[Signature/attestation verify\n(Cosign/SLSA)]
  G --> H[Update desired state\n(manifest/catalog PR)]
  H --> I[GitOps controller reconciles\n(asynchronous deploy)]
```

**Design principle:** CI produces *artifacts + attestations + governed metadata updates*; CD is triggered by changes to desired state (manifests/catalogs), not ad-hoc imperative deploy steps.

---

## 🌱 Environment variables

| Variable | Default | Purpose |
|---|---:|---|
| `KFM_ARTIFACTS_DIR` | `./artifacts/ci` | Where scripts write outputs (reports, JSON, logs, provenance). |
| `CI` | *(unset)* | If `true`, scripts may run stricter checks / fail on warnings. |
| `KFM_ENV` | `dev` | Target environment label (`dev`, `test`, `stage`, `prod`). |
| `KFM_REDACT_SECRETS` | `1` | If `1`, redact known secret patterns from logs. |
| `KFM_GOV_TICKET` | *(unset)* | Governance ticket ID (required for exception paths). |

> [!WARNING]
> Never store secrets in Git. CI should source secrets from the CI secret store / vault mechanisms, and scripts must avoid echoing them.

---

## 🧪 Adding a new script (Definition of Done)

### Required
- [ ] Script name is descriptive and scoped (e.g., `gates/verify_cosign.sh`)
- [ ] `--help` and `--version` implemented
- [ ] Non-interactive behavior confirmed (no prompts, no `read`)
- [ ] Uses strict shell mode (recommended): `set -euo pipefail`
- [ ] Emits artifacts to `${KFM_ARTIFACTS_DIR}`
- [ ] Returns correct exit codes (`0/1/2/3+`)
- [ ] Redacts secrets from logs (or avoids printing them)
- [ ] Documented in this README’s **Inventory** section

### Strongly recommended
- [ ] ShellCheck clean (or justified suppressions)
- [ ] Unit tests for parsing/logic (where practical)
- [ ] Golden-file tests for produced JSON/PROV/SBOM artifacts
- [ ] “Dry run” support (`--dry-run`) for any potentially destructive behavior
- [ ] Clear rollback step documented if the script affects promotion/deployment

---

## 🧾 Inventory

> [!NOTE]
> **TODO (repo-specific):** Populate this table with the actual scripts present in `infra/ci/scripts/`.

| Script | Category | Purpose | Safe to run locally? |
|---|---|---|---|
| `gates/<name>.sh` | Gate | Policy/provenance/signature verification | ✅ usually |
| `build/<name>.sh` | Build | Build artifacts/containers, generate SBOM | ⚠️ depends |
| `promote/<name>.sh` | Promote | Update manifests/catalogs for promotion | ⚠️ gated |

---

## 🩹 Troubleshooting

<details>
<summary><strong>Common failures</strong></summary>

- **Exit 2 (misconfiguration):** missing tool (e.g., `conftest`, `cosign`, `jq`), missing env var, wrong path.
- **Exit 1 (gate failure):** policy violation, signature verification failed, provenance missing required fields.
- **CI-only differences:** Some scripts run with stricter defaults when `CI=true`.

</details>

<details>
<summary><strong>Suggested debug pattern</strong></summary>

```bash
# Show environment and tool versions
env | sort | sed -E 's/(TOKEN|SECRET|PASSWORD)=.*/\1=[REDACTED]/'
conftest --version || true
cosign version || true
jq --version || true

# Re-run with verbose logging (if supported)
KFM_LOG_LEVEL=debug bash infra/ci/scripts/<script>.sh ...
```

</details>

---

## 📚 Glossary (quick)

- **OPA/Rego / Conftest:** policy-as-code gates for JSON/YAML outputs.
- **SBOM:** Software Bill of Materials (SPDX/CycloneDX).
- **Cosign/Sigstore:** signing + verification for artifacts/images/attestations.
- **SLSA:** provenance model/levels for software supply-chain integrity.
- **PROV:** W3C provenance model (entities, activities, agents).
- **GitOps:** desired state stored in Git, reconciled continuously by controllers.
