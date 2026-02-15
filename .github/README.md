# .github/ — KFM GitHub Operations, Governance & CI Gates

![Governed Artifact](https://img.shields.io/badge/governed-artifact-critical)
![Trust Membrane](https://img.shields.io/badge/trust%20membrane-enforced-important)
![Policy](https://img.shields.io/badge/policy-fail--closed-red)
![Promotion Contract](https://img.shields.io/badge/promotion%20contract-required-red)
![Receipts](https://img.shields.io/badge/receipts-run%20manifest%20%7C%20spec__hash-6a5acd)
![Catalogs](https://img.shields.io/badge/catalog-DCAT%20%7C%20STAC%20%7C%20PROV-3c7)
![Supply Chain](https://img.shields.io/badge/supply%20chain-SBOM%20%7C%20SLSA%20%7C%20in--toto-0a7)
![CI](https://img.shields.io/badge/CI-required-success)
![Focus Mode](https://img.shields.io/badge/focus%20mode-cite%20or%20abstain-blue)
![Kill Switch](https://img.shields.io/badge/kill--switch-supported-orange)

> [!IMPORTANT]
> **Why this file exists**
>
> This `.github/README.md` is the **single source of truth for repo governance and CI enforcement**:
> what must exist in `.github/`, which checks are mandatory, and what rules are **non‑negotiable**.
> It is written to be readable by humans *and* actionable for CI, CODEOWNERS, and policy review.
>
> **Change impact:** Treat changes to this file as **production changes** (governance surface).

---

## 📌 Quick Links

> Paths are **KFM‑standard expectations**. If your repo differs, keep the **boundaries** identical even if names differ.

- **Project root README**: `../README.md`
- **GitHub Actions workflows**: `./workflows/`
- **CODEOWNERS**: `./CODEOWNERS` *(required)*
- **Docs**: `../docs/` *(not confirmed in repo — expected for KFM)*
- **Architecture**: `../docs/architecture/` *(not confirmed in repo — expected)*
- **Governance**: `../docs/governance/` *(not confirmed in repo — expected)*
- **Contracts & schemas**: `../contracts/` *(not confirmed in repo — expected: Promotion Contract, Run Manifest schema, catalog minimums, policy input schemas)*
- **Policies (OPA/Rego + Conftest)**: `../policy/` *(path name may differ — verify in repo)*
- **Data zones**: `../data/` *(path name may differ — verify in repo)*
- **Catalogs**: `../data/catalog/` *(preferred per KFM examples; your repo may use `../catalog/` — verify)*
- **Watchers / automations registry**: `../watchers/` *(not confirmed in repo — expected if using watcher→PR automation patterns)*
- **Infra / GitOps**: `../infra/` *(not confirmed in repo — expected for KFM)*
- **Scripts**: `../scripts/` *(not confirmed in repo — expected: validators + acceptance harness wrappers)*

---

## 🧭 Table of Contents

- [Governance Header](#-governance-header-treat-as-production)
- [Change Summary](#-change-summary-what-changed-in-v140)
- [Non‑Negotiables](#-nonnegotiables-kfm-invariants)
- [Trust Membrane](#-trust-membrane--how-requests-flow)
- [Canonical Addressing & Evidence Resolver Contract](#-canonical-addressing--evidence-resolver-contract)
- [Promotion Contract, Receipts, and Digest Pinning](#-promotion-contract-receipts--digest-pinning-failclosed)
- [OCI Evidence Bundles & Provenance Hub](#-oci-evidence-bundles--provenance-hub)
- [Toolchain Pinning & Security Advisory Response](#-toolchain-pinning--security-advisory-response)
- [What MUST Live in `.github/`](#-what-must-live-in-github)
- [Expected Repo Directory Layout](#-expected-repo-directory-layout-kfm-standard)
- [CI Gates](#-ci-gates--the-kfm-no-merge-without-proof-standard)
- [Policy-as-Code](#-policy-as-code-opa--conftest--default-deny)
- [Evidence & Audit Guarantees](#-evidence--audit-guarantees)
- [Data Zones & Promotion Gates](#-data-zones--promotion-gates-raw--work--processed)
- [Sensitivity Handling](#-sensitivity-handling-fair--care-enforced)
- [Watchers & Automation Governance](#-watchers--automation-governance)
- [PR Workflow](#-pr-workflow-mandatory)
- [Supply Chain](#-supply-chain-release--deploy-hard-requirement)
- [When CI Fails](#-when-ci-fails--quick-diagnosis)
- [Reference Docs](#-reference-docs-authority-ladder)
- [Definition of Done](#-definition-of-done-for-githubreadmemd)

---

## 🧾 Governance Header (treat as production)

| Field | Value |
|---|---|
| Document | `.github/README.md` |
| Status | **Governed** (changes require review) |
| Applies to | GitHub Actions, branch protections, CODEOWNERS, templates, supply chain attestations, promotion contract enforcement |
| Version | `v1.4.0` *(tightens spec_hash semantics + address hierarchy + toolchain pinning + watchers governance)* |
| Effective date | **2026-02-15** |
| Review cadence | **Quarterly** + **out‑of‑band for security advisories/toolchain changes** |
| Owners | Defined in `.github/CODEOWNERS` *(required)* |
| Review triggers | Any change touching `policy/`, `.github/workflows/`, `contracts/`, catalogs, receipts, Story Nodes, validators, or watcher automation |

> [!WARNING]
> **Fail‑closed governance rule:** If a required enforcement surface is missing (policy, catalogs, receipts, contract tests), the system **denies** promotion/merge/release by default.

---

## 🧷 Change Summary (what changed in v1.4.0)

- Clarified **spec_hash** as `sha256(JCS(spec))` and required `spec_schema_id` + `spec_recipe_version` for comparability across pipelines.
- Added **canonical addressing hierarchy** (OCI digest → gateway resolver URL → storage URL as implementation detail).
- Added **toolchain pinning** section with explicit security‑advisory response expectations (including Cosign verification-bypass CVE guidance).
- Added **watchers governance** (registry, ownership, compliance constraints, and CI gates).
- Hardened example CI workflow with **least‑privilege permissions** and safer defaults.

---

## 🔒 Non‑Negotiables (KFM invariants)

These are not “guidelines.” They are **contracts** that CI + policy must enforce.

1. **Trust membrane**
   - UI and external clients **never** access databases directly.
   - All access is via **governed API gateway + policy decision point (OPA/Conftest)**.
   - Backend core logic **never bypasses repository interfaces** to talk to storage.

2. **Fail‑closed policy**
   - **Default deny** at policy boundaries (runtime + CI).
   - Missing policy input / missing receipts / missing catalogs / missing citations → **deny**.

3. **Promotion Contract is mandatory**
   - Promotion is **Raw → Work → Processed**.
   - Promotion requires:
     - **run manifest / run receipt** (aka run record) + validation report
     - deterministic **checksums**
     - required catalogs (**DCAT always; STAC/PROV as applicable**)
     - policy labels + redaction provenance (if sensitive)
   - No contract → no publish.

4. **Deterministic identity & digest pinning**
   - Every promoted artifact has a stable identity:
     - `spec_hash` (deterministic spec identity) **and**
     - content digest(s) (e.g., `sha256`) for produced artifacts
   - Wherever possible, refer to immutable digests (e.g., OCI `@sha256:...`) rather than mutable tags.

5. **Focus Mode must cite or abstain**
   - Any factual answer must include citations, or the system must abstain.
   - Every Focus Mode answer produces an **audit_ref** and supports evidence resolution endpoints.

6. **Contract‑first APIs (governed OpenAPI)**
   - Treat OpenAPI as a governed artifact: changes require review + contract tests.
   - `/api/v1` has a **no‑breaking‑change gate**.

7. **Workflow security is part of governance**
   - Branch protection + required status checks are mandatory.
   - Workflows run with **least privilege** and avoid unsafe triggers for untrusted PRs.
   - Third‑party Actions are pinned and controlled by CODEOWNERS.
   - Prefer **GitHub Apps and OIDC** over long‑lived PATs for automation.

---

## 🧱 Trust Membrane — How Requests Flow

```mermaid
flowchart LR
  UI["Web UI / External Client"] -->|"HTTP"| GW["API Gateway / Backend API"]
  GW -->|"authorize"| OPA["OPA Policy PDP"]
  OPA -->|"allow/deny + redaction decisions"| GW

  GW -->|"read/write via repository ports"| STORES["Data Stores"]
  STORES -->|"results"| GW

  GW -->|"evidence refs (PROV, STAC, DCAT, DOC, GRAPH)"| EVID["Evidence Resolver API"]
  EVID -->|"resolved evidence views"| GW

  GW -->|"validate response (citations + sensitivity)"| OPA
  GW -->|"append audit event"| LEDGER["Audit Ledger"]
  GW --> UI
```

**Key enforcement principle:** If a path bypasses the gateway or bypasses policy → it is a **design defect** and a **CI failure**.

---

## 🔗 Canonical Addressing & Evidence Resolver Contract

> [!IMPORTANT]
> If clients (UI, Focus Mode, auditors) can’t deterministically fetch “the thing a citation points to,” the system is not evidence-first.

### Canonical address hierarchy (required)

1) **OCI digest address** *(governance root; immutable)*  
   - Example: `oci://registry.example.org/kfm/bundles/example_dataset@sha256:<digest>`

2) **Gateway resolver URL** *(stable, derived from digest; preferred for UI fetch)*  
   - Example: `https://api.example.org/api/v1/bundles/sha256:<digest>`

3) **Storage URL** *(implementation detail; never used as provenance root)*  
   - Example: `s3://...` / `https://blob...`

### Evidence resolver acceptance criteria

- Every citation reference must be resolvable via an API endpoint using stable schemes:
  - `prov://`, `stac://`, `dcat://`, `doc://`, `graph://`, plus `oci://` for bundles.
- A KFM-quality UX means:
  - Given any `citation.ref` in a Focus Mode answer, the UI can resolve it to a human‑readable evidence view in **≤ 2 API calls**.
- Resolver must be **fail‑closed**:
  - missing target → `404`
  - unauthorized → `403`
  - policy denial → `403` (with a non-leaky denial reason code)

---

## 🧩 Promotion Contract, Receipts & Digest Pinning (fail‑closed)

> **Promotion Contract** is the canonical *merge‑blocking* rule set: what must be present to publish datasets, layers, Story Nodes, docs, and artifacts.

### ✅ Required promotion artifacts (baseline)

| Artifact | Required | Canonical location (preferred) | Notes |
|---|---:|---|---|
| Raw manifest (immutable) | ✅ | `data/raw/<dataset>/manifest.yml` | Must capture license + expected files + checksums + sensitivity label |
| Deterministic checksums | ✅ | `data/**/checksums.*` | Applies to inputs and outputs |
| Run manifest / run receipt *(run record)* | ✅ | `data/work/<dataset>/run_manifest.json` *(or `run_record.json`)* | Must include inputs/outputs digests + `spec_hash` + spec schema/version + code identity |
| Validation report | ✅ | `data/work/<dataset>/validation_report.json` | Includes schema, geometry, temporal, license/policy checks |
| PROV record | ✅ | `data/catalog/prov/<dataset>/run_*.json` | Links raw → processed derivatives |
| DCAT record | ✅ | `data/catalog/dcat/<dataset>.json` | License + attribution + restrictions |
| STAC collection/items | ◻︎ conditional | `data/catalog/stac/<dataset>/**` | Required when spatial assets are published |
| Audit ledger event | ✅ | runtime service | Promotion event must be recorded (tamper‑evident chain) |

### 🔐 Digest pinning (recommended default)

- When publishing bundles (data + catalogs + receipts), prefer referencing the immutable digest:
  - `registry.example.org/kfm/bundles/example_dataset@sha256:<digest>`
- Avoid mutable tags for governance‑critical lookups (tags are allowed as *aliases*, not as provenance roots).

### 🧬 spec_hash (required semantics)

> [!IMPORTANT]
> `spec_hash` MUST be comparable across runs. “Some hash existed” is not enough.

**Definition (required):**
- `spec_hash = sha256(JCS(spec))` where:
  - `spec` is a schema-defined object
  - `JCS` is JSON Canonicalization Scheme (RFC 8785)

**Required companion fields:**
- `spec_schema_id` — stable schema identifier (URI or canonical ID)
- `spec_recipe_version` — semver string for the pipeline recipe that interprets `spec`

### 🧾 Run manifest schema (illustrative excerpt)

```json
{
  "run_id": "run_2026-02-15T12:34:56Z",
  "dataset_id": "example_dataset",

  "spec_schema_id": "kfm.schema.run_spec.v1",
  "spec_recipe_version": "1.2.0",
  "spec_hash": "sha256:...",

  "inputs": [{"uri":"data/raw/example.csv","sha256":"..."}],
  "code": {"git_sha":"...","image":"kfm/pipeline@sha256:..."},
  "outputs": [{"uri":"data/processed/example.parquet","sha256":"..."}],

  "validation_report": "data/work/example/validation_report.json",
  "prov_ref": "data/catalog/prov/example/run_....json",

  "policy": {
    "classification": "public|internal|restricted",
    "sensitivity_flags": ["sensitive_location","culturally_sensitive","pii_risk"],
    "redistribution": "allowed|attribution_required|noncommercial_only|no_redistribution|unknown",
    "tags": ["..."],
    "custodian": {"org":"...", "grant_ref":"..."}
  },

  "attestations": {
    "sbom_ref":"...",
    "slsa_provenance_ref":"...",
    "rekor_proof_ref":"..."
  }
}
```

> Naming note: KFM documents use **run record / run receipt / run manifest** for the same concept. This repo standard treats them as the same governed object: validate against the canonical schema regardless of filename.

---

## 📦 OCI Evidence Bundles & Provenance Hub

KFM supports publishing a dataset + its evidence as a **single typed OCI artifact** (“evidence bundle”), with attached referrers for catalogs/receipts/attestations.

```mermaid
flowchart LR
  PR["PR: data + receipts + catalogs"] --> CI["CI: validate + conftest + cosign verify"]
  CI -->|"publish sha256 digest"| OCI["OCI Registry (subject digest)"]
  OCI -->|"referrers"| SBOM["SBOM (SPDX)"]
  OCI -->|"referrers"| SLSA["SLSA / in-toto provenance"]
  OCI -->|"referrers"| PROV["PROV record"]
  OCI -->|"referrers"| DCAT["DCAT record"]
  OCI -->|"referrers"| STAC["STAC collection/items"]
  OCI --> API["Evidence Resolver: /api/v1/bundles/{digest}"]
  API --> UI["UI: Receipt Viewer + Trust Badges"]
```

**Repo expectation:**
- CI must be able to resolve a bundle digest into its attached artifacts (SBOM, provenance, catalogs, receipts).
- Policy must enforce **digest match** and deny if referrers/attestations are missing when required.

---

## 🧷 Toolchain Pinning & Security Advisory Response

> [!WARNING]
> Tooling is part of the governance surface. Unpinned tooling can silently weaken “fail‑closed.”

### Required pinning rules

- Pin third‑party GitHub Actions by **commit SHA**, not tag.
- Pin **Cosign**, **OPA**, **Conftest**, **ORAS**, and validators to known-good versions.
- Updates require:
  - a PR with tool version bumps,
  - regression tests,
  - and an entry in the repo change log (or ADR if behavior changes).

### Minimum toolchain baseline (recommended)

| Tool | Pinning expectation | Why |
|---|---|---|
| GitHub Actions | `uses: <action>@<commit-sha>` | mutable tags are a supply-chain risk |
| Cosign | **≥ 2.6.2** (v2) or **≥ 3.0.4** (v3) | CVE-2026-22703: verification-bypass class issue (verify via NVD / Sigstore advisory) |
| OPA | pinned | policy correctness + reproducibility |
| Conftest | pinned | policy runner behavior changes can alter allow/deny outcomes |
| ORAS | pinned | OCI artifact push/discovery must be deterministic |
| STAC/DCAT/PROV validators | pinned | metadata validation must not drift |

**Reference links (non-authoritative in this repo; verify before adopting):**
- NVD CVE detail: `https://nvd.nist.gov/vuln/detail/CVE-2026-22703`
- Sigstore advisory example: `https://github.com/sigstore/cosign/security/advisories/`

---

## 🗂️ What MUST Live in `.github/`

This directory is where KFM’s repo‑level governance becomes enforceable.

### Required files and folders

Legend: ✅ required • 🟦 required for release/publish • 🟨 recommended • 🧭 optional (only if you use watchers)

| Path | Required | Purpose | Governed impact |
|---|---:|---|---|
| `.github/README.md` | ✅ | This governance document | High |
| `.github/CODEOWNERS` | ✅ | Enforced review ownership | High |
| `.github/workflows/ci.yml` | ✅ | PR gates: docs/stories/contracts/catalogs/receipts/policy/build | High |
| `.github/workflows/policy-regression.yml` | ✅ | OPA + Conftest regression suite (default deny) | High |
| `.github/workflows/api-contract.yml` | ✅ | OpenAPI “governed artifact” + no breaking change gate | High |
| `.github/workflows/release.yml` | 🟦 | Releases only when gates pass; attestations; signing | High |
| `.github/workflows/supply-chain.yml` | 🟦 | SBOM + SLSA/in‑toto provenance + signature verification | High |
| `.github/workflows/watchers.yml` | 🧭 | Watcher→PR automation checks + registry validation | High |
| `.github/actions/kfm-acceptance-harness/` | ✅ | Reusable CI module: validators + cosign + `spec_hash` checks | High |
| `.github/PULL_REQUEST_TEMPLATE.md` | ✅ | PR checklist for governance compliance | Medium |
| `.github/ISSUE_TEMPLATE/` | ✅ | Structured governance-friendly issues | Medium |
| `.github/SECURITY.md` | ✅ | Responsible disclosure + reporting | Medium |
| `.github/dependabot.yml` | 🟨 | Dependency visibility + updates | Medium |
| `.github/renovate.json` *(optional alt)* | 🟨 | Alternative dependency automation | Medium |

> If any ✅ item is missing, open an issue labeled `governance-gap` and block releases until resolved.

---

## 🧭 Expected Repo Directory Layout (KFM standard)

> Canonical layout matches KFM’s Raw→Work→Processed pipeline and catalog placement.  
> If your repo differs, keep the *boundaries* identical even if names differ.

```text
repo-root/
├─ .github/                        # CI + governance enforcement (this folder)
├─ docs/                           # governed docs, Story Nodes, runbooks, ADRs
├─ contracts/                      # Promotion Contract + schemas (run manifest, catalog minimums, policy input schemas)
├─ policy/                         # OPA/Rego + Conftest tests (default deny)
├─ watchers/                       # watcher registry + automation specs (optional; governed if present)
├─ data/
│  ├─ raw/                         # immutable acquisitions + manifests + checksums
│  ├─ work/                        # normalized/validated intermediates + receipts + validation reports
│  ├─ processed/                   # publishable, policy-labeled outputs (CI-only writes)
│  └─ catalog/
│     ├─ dcat/                     # dataset discovery + licensing metadata
│     ├─ stac/                     # spatial asset collections + items
│     └─ prov/                     # lineage: activities/entities/agents
├─ src/                            # backend API (ports/adapters enforced)
├─ web/                            # React/TS UI (no direct DB calls)
├─ scripts/                        # lint/validate scripts executed by CI + local wrappers
└─ infra/                          # deployment (k8s/helm/gitops)
```

> **Boundary rule:** regardless of layout, **frontend never talks to DB**; **core backend uses repository interfaces**; **all access is policy‑governed**.

---

## ✅ CI Gates (GitHub Actions) — The KFM “No‑Merge Without Proof” Standard

### Minimum CI hardening set (required)

CI must validate:

- **Docs & Story Nodes**
  - Markdown lint + link-check + template/schema validator
  - Story Node v3 validator + citation resolvability checks

- **Contracts**
  - Promotion Contract schema + run manifest schema + policy input schemas + catalog minimums schema validate
  - API contract diff: OpenAPI is a governed artifact (no breaking changes on `/api/v1`)

- **Data**
  - STAC/DCAT/PROV validation
  - checksums & deterministic build outputs
  - run manifest/receipt validation (including `spec_hash`, `spec_schema_id`, `spec_recipe_version`)

- **Policy**
  - `opa test` (unit tests)
  - `conftest test` (policy pack regression; promotion guard rules)

- **Supply chain (release)**
  - SBOM (SPDX recommended)
  - SLSA/in‑toto provenance attestation
  - signature verification (cosign/rekor where used)

### CI Gate Matrix

| Gate | What it protects | Typical checks | Required on PR? |
|---|---|---|---:|
| `docs` | governed documentation integrity | markdown lint, link-check, doc build receipt (if enabled) | ✅ |
| `stories` | Story Node validity + evidence | schema validation, citation resolvability | ✅ |
| `contracts` | global interoperability | schema validate Promotion Contract + run manifest + policy inputs + catalog minimums | ✅ |
| `catalogs` | dataset discovery + provenance | STAC/DCAT/PROV validate; link-check clean | ✅ |
| `receipts` | promotion correctness | run manifest schema + `spec_hash` semantics + checksum verification | ✅ |
| `policy` | governance safety | OPA tests + Conftest promotion guard suite | ✅ |
| `api-contract` | compatibility | OpenAPI diff; no breaking changes on `/api/v1` | ✅ |
| `build` | deployability | container builds + smoke tests | ✅ |
| `watchers` | automation governance | watcher registry schema + policy constraints | 🧭 optional |
| `security` | repo hygiene | secret scan, dependency scan, pinned actions | 🟨 recommended |
| `supply-chain` | artifact integrity | SBOM + provenance + signature verify | 🟦 release required |

---

## 🧪 Example CI Workflow (reference skeleton)

> This is a **reference baseline**. Adjust paths as needed, but **do not weaken gates**.  
> **Security rule:** pin third‑party Actions and set least‑privilege `permissions`.

```yaml
name: ci

on:
  pull_request:
  push:
    branches: [main]

# Default: least privilege.
permissions:
  contents: read

jobs:
  docs:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@<PINNED_SHA>
      - run: ./scripts/lint_docs.sh
      - run: ./scripts/validate_story_nodes.sh
      - run: ./scripts/doc_build_receipt.sh  # optional: deterministic doc digest + receipt

  contracts:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@<PINNED_SHA>
      - run: ./scripts/validate_contracts.sh  # JSON Schema: promotion + run manifest + policy inputs + catalog minimums

  catalogs:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@<PINNED_SHA>
      - run: ./scripts/validate_catalogs.sh   # DCAT/STAC/PROV + link-check

  receipts:
    runs-on: ubuntu-latest
    needs: [contracts]
    steps:
      - uses: actions/checkout@<PINNED_SHA>
      - run: ./scripts/validate_receipts.sh   # run manifest schema + spec_hash semantics + checksums

  policy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@<PINNED_SHA>
      - run: opa test policy -v
      - run: conftest test . -p policy/conftest  # promotion guard regression suite

  api-contract:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@<PINNED_SHA>
      - run: ./scripts/openapi_no_breaking_changes.sh  # /api/v1 gate

  build:
    runs-on: ubuntu-latest
    needs: [docs, contracts, catalogs, receipts, policy, api-contract]
    steps:
      - uses: actions/checkout@<PINNED_SHA>
      - run: docker build -t kfm-api ./src
      - run: docker build -t kfm-web ./web
      - run: ./scripts/smoke_tests.sh
```

---

## ⚖️ Policy-as-Code (OPA + Conftest) — Default Deny

### Focus Mode output validation (baseline)

```rego
package kfm.ai
default allow := false

# Require citations AND sensitivity approval.
allow if {
  input.answer.has_citations == true
  input.answer.sensitivity_ok == true
}
```

### Promotion guard (illustrative)

```rego
package kfm.promotion
default allow := false

# Allow promotion only when required governed artifacts exist and validate.
allow if {
  input.run_manifest.valid == true
  input.run_manifest.spec_hash_valid == true
  input.catalogs.dcat.valid == true
  input.catalogs.prov.valid == true

  # STAC required when spatial assets are present:
  not input.catalogs.stac.required
} else if {
  input.run_manifest.valid == true
  input.run_manifest.spec_hash_valid == true
  input.catalogs.dcat.valid == true
  input.catalogs.prov.valid == true
  input.catalogs.stac.required
  input.catalogs.stac.valid == true
}
```

> **Fail‑closed rule:** if required keys are missing, policies must deny.

---

## 🧾 Evidence & Audit Guarantees

### Evidence resolution acceptance criteria

- Every citation reference must be resolvable via an API endpoint using stable schemes:
  - `prov://`, `stac://`, `dcat://`, `doc://`, `graph://`, `oci://`
- A KFM-quality UX means:
  - Given any `citation.ref` in a Focus Mode answer, the UI can resolve it to a human‑readable evidence view in **≤ 2 API calls**.
- System returns `answer_markdown` with citations and `audit_ref`; auditors can resolve `audit_ref` to an evidence pack.

### Audit record schema (excerpt)

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://kfm.example.org/schema/audit_record.json",
  "type": "object",
  "required": ["audit_ref", "timestamp", "event_type", "subject", "event_hash"],
  "properties": {
    "audit_ref": { "type": "string" },
    "timestamp": { "type": "string", "format": "date-time" },
    "event_type": { "type": "string" },
    "actor": { "type": "object", "additionalProperties": true },
    "subject": { "type": "object", "additionalProperties": true },
    "evidence_refs": { "type": "array", "items": { "type": "string" } },
    "prev_hash": { "type": "string" },
    "event_hash": { "type": "string" }
  }
}
```

---

## 🧬 Data Zones & Promotion Gates (Raw → Work → Processed)

### What each zone means

| Zone | Allowed contents | Who can read | Who can publish |
|---|---|---|---|
| `raw/` | acquired source artifacts + deterministic manifests/checksums | internal + reviewers (by policy) | nobody |
| `work/` | normalized + validated intermediates, redaction transforms, run manifests/receipts | internal + reviewers (by policy) | nobody |
| `processed/` | publishable, policy-labeled datasets and derivatives | public/reviewer/admin depending on policy | CI only |

### Promotion checklist (CI-enforced)

- [ ] Row-level schema validation (required fields; type coercion documented)
- [ ] Geometry validity + bounds checks
- [ ] Temporal consistency checks
- [ ] License + attribution captured in DCAT; restrictions encoded in policy
- [ ] Provenance completeness: every promoted artifact has a PROV chain + deterministic checksum
- [ ] Run manifest/receipt exists + validates; includes `spec_hash` + `spec_schema_id` + `spec_recipe_version` + artifact digests + code identity
- [ ] Policy labels defined; restricted fields/locations redacted per rules
- [ ] Catalogs emitted (DCAT always; STAC/PROV as applicable) and link-check clean
- [ ] API contract tests pass for at least one representative query
- [ ] Backfill strategy documented (if applicable)
- [ ] Human approval recorded if classification != public

---

## 🧯 Sensitivity Handling (FAIR + CARE, enforced)

KFM must treat some data as sensitive (examples include private ownership, precise archaeological site locations, and some health/public-safety indicators). Sensitivity handling requires:

- policy labels at dataset/record/field level
- derivative datasets with explicit redaction provenance
- fail‑closed policy checks

**Repo rule:** do not merge PRs that introduce sensitive material without explicit policy labels + redaction evidence.

---

## 🛰️ Watchers & Automation Governance

> [!IMPORTANT]
> Watchers are **governance-critical automation**. Treat watcher code/specs like production.

### Watcher rules (baseline)

- Watchers MUST:
  - use conditional requests (ETag / Last-Modified) where possible
  - respect provider terms and rate/row limits
  - emit typed receipts (`run_manifest`) on every material run
  - be discoverable via a **watcher registry** (schema-validated + signed if required)

### Watcher registry (recommended structure)

- `watchers/registry.json` (or `.yml`) containing:
  - `watcher_id`, `provider`, `endpoint`, `poll_interval`, `outputs`, `policy`, `spec_hash`, `signature_ref`
- CI validates registry schema and blocks merge if invalid.

### Kill switch (required pattern)

Provide an emergency stop for automation/promotion:

- If repo/org variable `KFM_GOVERNANCE_KILL_SWITCH=true`:
  - CI MUST fail any job that would publish/promote
  - Release workflows MUST not run “publish” steps

---

## 🧾 PR Workflow (mandatory)

### Branch protection (required)

- No direct pushes to protected branches
- No force push
- PR required + review required
- Required checks: `docs`, `stories`, `contracts`, `catalogs`, `receipts`, `policy`, `api-contract`, `build`
- `.github/workflows/**`, `policy/**`, `contracts/**`, `data/**`, `docs/**` must be CODEOWNED and require explicit approval
- Signed commits/tags are strongly recommended for governance integrity

### PR Checklist (copy into `.github/PULL_REQUEST_TEMPLATE.md`)

- [ ] No UI-to-DB direct access introduced (trust membrane preserved)
- [ ] Promotion Contract requirements satisfied (receipts + checksums + catalogs + policy labels)
- [ ] `spec_hash` semantics preserved (`sha256(JCS(spec))` + schema/version fields)
- [ ] Story Nodes validate and citations resolve
- [ ] OPA + Conftest tests pass; default deny preserved
- [ ] Sensitive data reviewed; policy labels + redaction provenance present where needed
- [ ] `/api/v1` has no breaking changes (if API touched)
- [ ] CI gates all green; no bypass

---

## 🧷 Issue Templates (recommended set)

Create structured issue templates so governance becomes easy, not optional:

- `bug_report.yml` — defects with reproduction + expected evidence
- `feature_request.yml` — new capability proposals with acceptance criteria
- `data_source_request.yml` — ingestion profile request with licensing + sensitivity
- `promotion_request.yml` — request to promote dataset/version to `processed/` with receipts
- `policy_change.yml` — policy change proposal with tests + deny-by-default impact
- `story_node_proposal.yml` — new Story Node idea with sources + claims list
- `security_report.yml` — private vulnerability channel instructions

---

## 🧑‍⚖️ CODEOWNERS (required)

Minimum recommended ownership map:

| Area | Suggested owners |
|---|---|
| `.github/workflows/**` | platform + security owners |
| `.github/actions/**` | platform + security owners |
| `contracts/**` | governance + data stewardship owners |
| `policy/**` | governance + security owners |
| `watchers/**` | data stewardship + platform owners |
| `data/**` | data stewardship owners |
| `src/**` | backend owners |
| `web/**` | frontend owners |
| `docs/**` | documentation stewards |

> Owners are governance enforcement. Missing CODEOWNERS = missing trust.

---

## 🔐 Supply Chain (release + deploy hard requirement)

**Rule:** Publish versioned container images and/or OCI evidence bundles **only if all gates pass**.

Minimum release artifacts:
- SBOM (SPDX recommended)
- SLSA/in‑toto provenance attestation
- Versioned container images and/or dataset bundles (digest pinned)
- Signature verification policy (cosign/rekor where used)

---

## 🚨 When CI Fails — Quick Diagnosis

| Failure | Usually means | Fix |
|---|---|---|
| `validate_contracts` | Promotion Contract / schema mismatch | update schema + samples; keep fail-closed |
| `validate_catalogs` | missing/invalid DCAT/STAC/PROV | add/repair catalogs; ensure link-check clean |
| `validate_receipts` | run manifest missing fields / checksum mismatch / spec_hash mismatch | regenerate receipts deterministically; fix JCS canonicalization; ensure schema/version fields |
| `conftest test` | policy regression | update policy/tests; do not weaken default deny |
| `opa test` | policy unit test failure | fix policy inputs, add tests for new cases |
| `openapi_no_breaking_changes` | `/api/v1` breaking change | bump version strategy or refactor to `/api/v2` |
| `doc_build_receipt` | docs are non-deterministic | set `SOURCE_DATE_EPOCH`; pin tooling; remove unstable inputs |
| `build` | Dockerfile/path issues | align contexts; update CI paths; fix smoke tests |

---

## 📚 Reference Docs (authority ladder)

If something conflicts:
1) The **Non‑Negotiables** win  
2) Policy remains **fail‑closed**  
3) Escalate via ADR (Architecture Decision Record) instead of weakening gates

**Primary authority sources (by design):**
- KFM Next‑Gen Blueprint & Primary Guide (internal draft, 2026‑02‑12)
- KFM Comprehensive Data Source Integration Blueprint (2026‑02‑12)
- KFM “New Ideas Feb‑2026” integration patterns (Promotion Contract, Run Manifest schema, Provenance Guard, Acceptance Harness, OCI referrers)
- KFM governance + ethics + sovereignty docs *(expected in `docs/governance/`, not confirmed in repo)*

---

## ✅ Definition of Done (for `.github/README.md`)

This document is “done” when:

- [ ] Every ✅ required `.github` item exists in repo
- [ ] Branch protections require PRs + CODEOWNERS + required checks
- [ ] CI gates run on every PR: docs/stories/contracts/catalogs/receipts/policy/api-contract/build
- [ ] OPA + Conftest enforce default deny + cite-or-abstain + promotion guard rules
- [ ] spec_hash semantics standardized and tested (`sha256(JCS(spec))` + schema/version fields)
- [ ] Supply chain attestations exist for releases (SBOM + SLSA/in‑toto + signature policy)
- [ ] Contributors can run the checks locally via `scripts/` equivalents (including Conftest suite)
- [ ] (If watchers exist) watcher registry is schema-validated + CODEOWNED + governed

---

<details>
<summary><strong>Appendix: GitHub Actions hardening (security hygiene)</strong></summary>

- Pin third-party Actions by commit SHA (avoid mutable tags).
- Use least-privilege `GITHUB_TOKEN` permissions per job (default read-only).
- Avoid risky triggers for untrusted PRs (be cautious with `pull_request_target`).
- Enable secret scanning / push protection and dependency scanning (Dependabot or equivalent).
- Require PR reviews for `.github/workflows/**`, `policy/**`, `contracts/**`, and (if present) `watchers/**`.
- Prefer GitHub App identities and OIDC for automation over long-lived PATs.
</details>
