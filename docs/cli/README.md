<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/4d7b4a23-7e5a-4d7d-bc0b-76f1a1f4f09f
title: KFM CLI
type: standard
version: v1
status: draft
owners: TBD
created: 2026-02-22
updated: 2026-02-22
policy_label: public
related:
  - kfm://doc/kfm-definitive-design-governance-guide-vnext
tags:
  - kfm
  - cli
  - governance
  - data-pipelines
notes:
  - Contract-first CLI spec; align with implementation (kfm --help).
[/KFM_META_BLOCK_V2] -->

# KFM CLI
Governed command-line interface for Kansas Frontier Matrix (KFM) operations: ingest, validate, promote, rebuild projections, and inspect evidence.

**Status:** Draft • **Owners:** TBD • **Policy:** fail-closed • **Outputs:** `table|json`

[![CI](https://github.com/<org>/<repo>/actions/workflows/ci.yml/badge.svg)](https://github.com/<org>/<repo>/actions/workflows/ci.yml)
[![Release](https://img.shields.io/github/v/release/<org>/<repo>?include_prereleases)](https://github.com/<org>/<repo>/releases)
[![License](https://img.shields.io/github/license/<org>/<repo>)](./LICENSE)
[![Last Commit](https://img.shields.io/github/last-commit/<org>/<repo>)](https://github.com/<org>/<repo>/commits/main)
![Policy](https://img.shields.io/badge/policy-fail--closed-critical)
![Audit](https://img.shields.io/badge/audit-run%20receipts-informational)
![Truth%20Path](https://img.shields.io/badge/zones-RAW%E2%86%92WORK%E2%86%92PROCESSED%E2%86%92CATALOG%E2%86%92PUBLISHED-blueviolet)

> **Repo wiring note:** Replace all `<org>/<repo>` placeholders above with your actual GitHub org/repo.  
> If you use a different default branch or workflow file name, update the badge links accordingly.

---

## Navigation
- [Quick start](#quick-start)
- [Install and update](#install-and-update)
- [What the CLI is for](#what-the-cli-is-for)
- [Key concepts](#key-concepts)
- [Architecture at a glance](#architecture-at-a-glance)
- [Command surface](#command-surface)
- [Workflows](#workflows)
- [Configuration and auth](#configuration-and-auth)
- [Output and exit-code conventions](#output-and-exit-code-conventions)
- [Governance and safety rules](#governance-and-safety-rules)
- [Development notes](#development-notes)
- [Troubleshooting](#troubleshooting)
- [Contributing and support](#contributing-and-support)

---

## Quick start

> This README is intentionally **contract-first**: the authoritative command list is whatever `kfm --help` prints in your build.  
> If a section here conflicts with reality, fix one of them—either update the docs or align the code.

~~~bash
# 1) Verify the CLI is reachable
kfm --help

# 2) Confirm it can talk to your environment (API, policy bundle, etc.)
kfm doctor

# 3) List datasets (example subcommand; see Command surface)
kfm datasets list

# 4) Run a promotion preflight for a dataset spec (example)
kfm promote preflight data/specs/<dataset>.json --format table
~~~

---

## Install and update

KFM CLI can be distributed in multiple ways. Choose **one** and standardize on it across environments.

### Option A — Prebuilt binary
- Recommended for operator laptops and CI runners.
- Publish per platform: `linux/amd64`, `linux/arm64`, `darwin/arm64`, `windows/amd64`.

~~~bash
# TEMPLATE: replace placeholders with your release asset names
curl -L -o kfm.tgz "https://github.com/<org>/<repo>/releases/download/<tag>/kfm_<os>_<arch>.tar.gz"
tar -xzf kfm.tgz
./kfm --help
~~~

### Option B — Containerized CLI
- Recommended when your environment is container-first.

~~~bash
# TEMPLATE: replace image name/tag
podman run --rm -it ghcr.io/<org>/kfm-cli:<tag> --help
~~~

### Option C — Build from source
- Recommended for contributors.
- Keep builds reproducible and version-stamped.

~~~bash
# TEMPLATE: align to your build system (go/cargo/node/etc.)
make build
./dist/kfm --help
~~~

**Versioning guidance**
- Print version via `kfm version` (recommended).
- Include build metadata (commit SHA, build time, policy bundle version).

---

## What the CLI is for

The CLI is the operator/developer interface for KFM’s governed workflow:

- **Data lifecycle operations**: move artifacts through the truth path zones (RAW → WORK/QUARANTINE → PROCESSED → CATALOG/TRIPLET → PUBLISHED).
- **Promotion gates**: run the Promotion Contract checks (identity, license, sensitivity, catalogs, receipts, policy tests) before anything reaches runtime surfaces.
- **Rebuildable projections**: rebuild search/graph/tiles/DB projections from canonical truth (object store + catalogs + audit).
- **Evidence inspection**: resolve EvidenceRefs to policy-filtered EvidenceBundles used by UI and Focus Mode.
- **Governed runs**: emit receipts/audit references for pipeline and Focus Mode runs.

---

## Key concepts

### Truth path zones
KFM organizes data into zones with strict promotion rules:

- **RAW**: immutable acquisition artifacts + checksums + terms snapshot.
- **WORK / QUARANTINE**: normalized intermediates + QA reports + redaction candidates; quarantine blocks promotion.
- **PROCESSED**: publishable artifacts in approved formats + checksums + derived runtime metadata.
- **CATALOG/TRIPLET**: DCAT + STAC + PROV (and run receipts) as the canonical contract surface.
- **PUBLISHED**: governed runtime (API + UI) may serve **only promoted** dataset versions.

### Promotion Contract
Promotion to runtime **MUST** fail-closed unless all gates pass:

- Gate A: Identity + deterministic versioning
- Gate B: Licensing/rights explicitness
- Gate C: Sensitivity classification + redaction/generalization plan
- Gate D: DCAT/STAC/PROV validation + cross-link integrity
- Gate E: Run receipts + checksums + environment capture
- Gate F: Policy tests + evidence resolver + API/schema contract tests
- Gate G: Optional production posture checks (SBOM, perf smoke, a11y smoke)

### Trust membrane
Clients—including this CLI when acting as a client—**do not** bypass the governed boundary. The policy/provenance boundary must be enforceable in CI and at runtime.

---

## Architecture at a glance

~~~mermaid
flowchart LR
  subgraph TruthPath[Truth path zones]
    U[Upstream sources] --> R[RAW]
    R --> W[WORK / QUARANTINE]
    W --> P[PROCESSED]
    P --> C[CATALOG TRIPLET<br/>DCAT + STAC + PROV + run receipts]
  end

  C --> X[Indexes / projections<br/>DB + search + graph + tiles]
  X --> A[Governed API<br/>Policy + Evidence resolver]
  A --> UI[UI surfaces<br/>Map + Story + Focus]

  CLI[KFM CLI] --> R
  CLI --> W
  CLI --> P
  CLI --> C
  CLI --> X
  CLI --> A
~~~

---

## Command surface

> **Naming is a contract suggestion.** If your implementation uses different names, keep the intent and governance semantics, and update this section.

### Global flags
All commands SHOULD support:

- `--format table|json` (default: `table`)
- `--output <path>` (write machine output to a file)
- `--quiet` / `--verbose`
- `--no-color`
- `--audit` (print `audit_ref` / `run_id` prominently)

Recommended ergonomics:
- `--timezone <iana>` for rendering times in logs (default to operator locale).
- `--page-size <n>` for list commands (if backed by API pagination).

### High-level commands

| Area | Command | Purpose |
|---|---|---|
| Environment | `kfm doctor` | Connectivity + policy + storage sanity checks; prints remediation hints |
| Datasets | `kfm datasets list` | Discover dataset families/versions (from catalogs or API) |
|  | `kfm datasets show <dataset_version_id>` | Show metadata, policy label, artifacts, and catalog links |
| Specs | `kfm spec init <dataset_slug>` | Create a dataset onboarding spec template |
|  | `kfm spec hash <spec.json>` | Compute deterministic `spec_hash` (input to DatasetVersion ID) |
| Ingest | `kfm ingest run --spec <spec.json>` | Execute a deterministic ingest run (or trigger worker) |
|  | `kfm ingest status <run_id>` | Check status and summarize outputs by digest |
| Validate | `kfm validate --spec <spec.json>` | Run all promotion gates in preflight mode (no promotion) |
| Promote | `kfm promote preflight <spec.json>` | Explicit promotion pre-check (Gate A–F) |
|  | `kfm promote apply <spec.json>` | Promote: write processed artifacts + catalogs + receipts; fail closed |
| Catalogs | `kfm catalog validate <path>` | Validate DCAT/STAC/PROV profiles + cross-links |
| Policy | `kfm policy test` | Run fixtures-driven policy tests (OPA/Rego or equivalent) |
| Evidence | `kfm evidence resolve <evidence_ref>` | Resolve an EvidenceRef into a policy-filtered EvidenceBundle |
| Indexes | `kfm index rebuild [--dataset-version <id>]` | Rebuild projections from canonical sources (safe + repeatable) |
| Stories | `kfm story lint <path>` | Lint Story Node citations + policy label + sidecar integrity |
|  | `kfm story publish <path>` | Publish a Story Node (governed run; emits `audit_ref`) |
| Focus | `kfm focus run "<query>" [--view-state <json>]` | Run a governed Focus Mode request; returns citations + `audit_ref` |
| Audit | `kfm audit show <audit_ref>` | Show (policy-safe) audit record / run receipt summary |

---

## Workflows

### Workflow 1 — Dataset onboarding
This is the expected safe-default flow: PR-first and promotion-gated.

1. Create or update a **dataset onboarding spec** (canonical input to `spec_hash`).
2. Open a PR including:
   - source registry entry (if applicable)
   - the spec + pipeline configuration
   - small fixtures and expected outputs (for CI)
3. CI runs:
   - schema + catalog validation
   - policy tests
   - spec_hash stability checks
   - catalog cross-link checks
4. Steward review:
   - licensing/rights
   - sensitivity classification + redaction obligations
   - approve policy label
5. Merge and run in controlled environment.
6. Outputs written to PROCESSED + CATALOG/TRIPLET, with receipts.
7. Release manifest/tag created.

CLI mapping:
~~~bash
kfm spec init noaa_ncei_storm_events
kfm validate --spec data/specs/noaa_ncei_storm_events.json --format table
kfm promote preflight data/specs/noaa_ncei_storm_events.json

# Promotion itself may be restricted to operators/stewards:
kfm promote apply data/specs/noaa_ncei_storm_events.json --format json --output out/run.json
~~~

### Workflow 2 — Rebuild projections
Because projections are rebuildable, you should be able to reindex without mutating canonical truth.

~~~bash
# Rebuild everything
kfm index rebuild

# Or rebuild for a specific promoted dataset version
kfm index rebuild --dataset-version <dataset_version_id>
~~~

### Workflow 3 — Resolve evidence for a claim or UI bug report
~~~bash
kfm evidence resolve "doc://sha256:<digest>#page=12&span=10:200" --format json
~~~

### Workflow 4 — Run a Focus Mode query with map context
~~~bash
kfm focus run "What tornado events occurred in this county in May 2019?" \
  --view-state ops/view_state.json \
  --format json
~~~

---

## Configuration and auth

> If configuration or permissions are unclear, **default deny** and provide a policy-safe error with an `audit_ref`.

### Configuration sources
Recommended precedence:

1. Explicit flags
2. Environment variables
3. Config file (e.g., `~/.config/kfm/config.json`)
4. Built-in defaults (safe defaults only)

### Environment variables
Names below are **recommended conventions**; align to your implementation:

| Variable | Purpose | Example |
|---|---|---|
| `KFM_API_BASE_URL` | Governed API base URL | `https://kfm.example.gov/api` |
| `KFM_AUTH_TOKEN` | Auth bearer token (short-lived) | `eyJ...` |
| `KFM_POLICY_BUNDLE_PATH` | Local policy bundle path (if used) | `./policy/bundle.tar.gz` |
| `KFM_AUDIT_MODE` | Audit verbosity | `summary` |
| `KFM_DEFAULT_FORMAT` | Default output format | `table` |

### Auth expectations
- If using OIDC: prefer device code / SSO flows and short-lived access tokens.
- Never persist long-lived secrets unencrypted.
- When calling the API, the CLI MUST present:
  - operator identity
  - requested action and resource scope
  - a client version string for audit correlation

---

## Output and exit-code conventions

### JSON output
When `--format json` is used, output SHOULD be a single JSON object with stable top-level fields:

- `status`: `ok|error`
- `audit_ref` or `run_id` (when applicable)
- `policy_label` (policy-safe)
- `dataset_version_id` (when applicable)
- `digests[]` (when applicable)
- `errors[]` (stable error model with `error_code` + policy-safe `message` + optional `audit_ref`)

Example:
~~~json
{
  "status": "error",
  "audit_ref": "audit://sha256:...",
  "errors": [
    {
      "error_code": "PROMOTION_GATE_FAILED",
      "message": "Gate D: catalog cross-link integrity failed",
      "details": {
        "gate": "D",
        "failed_checks": ["stac_asset_href_missing"]
      }
    }
  ]
}
~~~

### Exit codes
| Code | Meaning |
|---:|---|
| `0` | Success |
| `2` | Validation failed (promotion gates did not pass) |
| `3` | Policy denied (default deny / restricted by role) |
| `4` | Dependency unavailable (API/evidence resolver/storage) |
| `1` | Other error |

---

## Governance and safety rules

### Fail closed
- If licensing/rights are unclear, quarantine the dataset; do not promote.
- If sensitivity is unclear, quarantine; require steward review.
- If the CLI cannot validate catalogs/receipts, promotion MUST fail.

### Do not leak restricted existence
When policy denies a resource, CLI output must be policy-safe:
- Avoid revealing “this exists but you can’t see it.”
- Align behavior for deny/not-found pathways as appropriate to prevent inference.

### Treat audit artifacts as sensitive
Run receipts and audit logs can contain sensitive metadata and must follow retention/redaction policy.

### Sensitive locations
If a dataset is labeled restricted or has a sensitive-location risk, the CLI MUST:
- avoid printing precise coordinates by default
- prefer generalized geometry summaries (bbox, region, admin area) unless explicitly allowed by policy

---

## Development notes

### Layering rule of thumb
New commands should:
1. parse CLI args (thin)
2. call a **use case** (workflow)
3. use **interfaces/repositories** for storage/API/policy
4. return structured results (for JSON output + audit refs)

Avoid writing commands that talk directly to databases or object storage without going through policy-aware interfaces.

### Tests required for new commands
- unit tests for argument parsing and use case behavior
- policy fixture tests for allow/deny behavior
- contract tests for JSON output stability
- smoke test that emits (or references) a run receipt for governed runs

### Suggested repository layout
~~~text
repo/
  cmd/                 # CLI entrypoints (thin)
  internal/
    domain/            # pure types + invariants
    usecases/          # workflows
    adapters/
      api/             # governed API client
      policy/          # policy evaluation client
      storage/         # object store and catalog IO
  policy/              # policy bundles + fixtures
  fixtures/            # test fixtures for CLI contracts
  docs/
    cli/README.md      # this file (or project root README.md)
~~~

---

## Troubleshooting

### Promotion failed but the reason is unclear
1. Re-run with JSON output and verbose logging:
   ~~~bash
   kfm promote preflight data/specs/<dataset>.json --format json --verbose
   ~~~
2. Look for:
   - Gate failures (A–F)
   - missing checksums or receipts
   - policy deny and obligations
3. Use `audit_ref` / `run_id`:
   ~~~bash
   kfm audit show <audit_ref>
   ~~~

### EvidenceRef does not resolve
- Confirm the dataset version is promoted and catalogs are validated.
- Run catalog link checks:
  ~~~bash
  kfm catalog validate data/catalog/<dataset_version_id>/
  ~~~
- Rebuild indexes only after canonical artifacts + catalogs validate:
  ~~~bash
  kfm index rebuild --dataset-version <dataset_version_id>
  ~~~

### Doctor fails with dependency unavailable
- Verify network connectivity to the governed API.
- Verify your auth token is valid and not expired.
- Verify your policy bundle path is readable (if applicable).

---

## Contributing and support

### Contributing
- Keep changes **additive and reversible**.
- Update `kfm --help` output and this doc together (contract-first).
- Add/extend tests for every command surface change.

### Security
- Do not file sensitive vulnerabilities in public issues.
- Use your project’s private security reporting channel (TBD).

### Support
- For operator support: open an issue tagged `ops`.
- For doc issues: open an issue tagged `docs`.
- For policy issues: open an issue tagged `governance`.

---

*Back to top:* [KFM CLI](#kfm-cli)
