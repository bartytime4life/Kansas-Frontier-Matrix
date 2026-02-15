<!--
GOVERNED ARTIFACT NOTICE
FILE: README.md

This README is part of the KFM trust boundary: it communicates non-negotiable invariants,
repo boundaries, and the “truth path.”

If you change meaning (not just phrasing), route through the governance review path:
CODEOWNERS + required CI gates + promotion contract checks.
-->

<div align="center">

# Kansas Frontier Matrix — KFM‑NG Governed Geospatial and Historical Knowledge System 🧭🗺️

**KFM turns heterogeneous Kansas history + geospatial data into a governed, evidence-first system:**  
**data → watchers/connectors + pipelines → receipts + catalogs → governed APIs → map UI + Story Nodes + Focus Mode**

<br/>

![Status](https://img.shields.io/badge/status-governed%20draft-2563eb)
![Evidence-first](https://img.shields.io/badge/evidence--first-required-0f766e)
![Trust membrane](https://img.shields.io/badge/trust%20membrane-enforced-16a34a)
![Fail-closed](https://img.shields.io/badge/policy-default%20deny-111827)
![Promotion Contract](https://img.shields.io/badge/promotion-contract%20required-critical)
![Receipts](https://img.shields.io/badge/receipts-run__manifest%20%7C%20run__record-6a5acd)
![spec_hash](https://img.shields.io/badge/spec__hash-RFC8785%20JCS%20%2B%20sha256-6a5acd)
![Catalogs](https://img.shields.io/badge/catalogs-DCAT%20%7C%20STAC%20%7C%20PROV-2563eb)
![Evidence resolver](https://img.shields.io/badge/evidence-resolver%20required-2563eb)
![Audit](https://img.shields.io/badge/audit-audit__ref%20always-6a5acd)
![Digest pinning](https://img.shields.io/badge/digest%20pinning-prefer%20sha256-4b0082)
![Kill switch](https://img.shields.io/badge/kill--switch-required-orange)
![CI](https://img.shields.io/badge/CI-no%20merge%20without%20proof-success)
![Releases](https://img.shields.io/badge/releases-immutable%20records-4b0082)
![Supply chain](https://img.shields.io/badge/supply%20chain-SBOM%20%2B%20attestations%20optional-6b7280)

<!-- OPTIONAL: replace ORG/REPO with real values once workflows exist -->
<!--
[![CI](https://github.com/ORG/REPO/actions/workflows/ci.yml/badge.svg)](https://github.com/ORG/REPO/actions/workflows/ci.yml)
[![Policy](https://github.com/ORG/REPO/actions/workflows/policy-regression.yml/badge.svg)](https://github.com/ORG/REPO/actions/workflows/policy-regression.yml/badge.svg)
[![API Contract](https://github.com/ORG/REPO/actions/workflows/api-contract.yml/badge.svg)](https://github.com/ORG/REPO/actions/workflows/api-contract.yml)
[![Supply Chain](https://github.com/ORG/REPO/actions/workflows/supply-chain.yml/badge.svg)](https://github.com/ORG/REPO/actions/workflows/supply-chain.yml)
-->
</div>

> [!IMPORTANT]
> **Trust membrane:** a governed API plus policy boundary mediates **all access**.  
> **UI and external clients never talk to databases or object storage directly.**  
> **Fail closed:** missing policy inputs, receipts, catalogs, or citations → **deny or abstain**.  
> **Focus Mode must cite or abstain** and always returns an **audit reference**.

---

## Governance header

| Field | Value |
|---|---|
| Document | `README.md` |
| Status | **Governed draft** |
| Applies to | invariants, trust membrane, promotion requirements, evidence UX requirements |
| Version | `v1.8.0-draft` |
| Effective date | **2026-02-15** |
| Review cadence | quarterly + out-of-band for security or toolchain changes |
| Owners | `.github/CODEOWNERS` *(required; if missing, treat as governance gap)* |
| Change impact | invariant changes are **release-blocking** until governance review completes |

> [!WARNING]
> **Fail-closed governance rule:** if required enforcement surfaces are missing (policy, receipts, catalogs, contract tests), promotion, merge, and release must **deny** by default.

---

## Repository status signal

This repo can contain both implemented and design-intent surfaces.

**KFM rule:** if a guarantee is not machine-enforced (schemas + validators + CI wiring), treat it as **not yet proven**.

> [!TIP]
> Add a small, runnable “verification harness” early (`make verify` or equivalent). If it is missing, that is a P0 governance gap.

---

## Quick links

### Governance single source of truth

- **Repo governance and CI gates:** `.github/README.md`
- **Security reporting:** `.github/SECURITY.md`
- **Contributing:** `CONTRIBUTING.md` and `.github/PULL_REQUEST_TEMPLATE.md`
- **CODEOWNERS:** `.github/CODEOWNERS`

### System planes

Each plane is a governed surface. If a plane README is missing, treat it as a governance gap.

- **Docs governance:** `docs/README.md`
- **Data governance:** `data/README.md`
- **Backend governance:** `src/README.md`
- **Web UI governance:** `web/README.md`
- **Tools and validators:** `tools/README.md`
- **Tests and trust gates:** `tests/README.md`
- **Releases:** `releases/README.md`

---

## Table of contents

- [If you are new here start here](#if-you-are-new-here-start-here)
- [Authority ladder](#authority-ladder)
- [KFM constitutional contracts](#kfm-constitutional-contracts)
- [Core features](#core-features)
- [Standards compatibility matrix](#standards-compatibility-matrix)
- [Repo directory layout](#repo-directory-layout)
- [Truth path](#truth-path)
- [Promotion Contract and proof artifacts](#promotion-contract-and-proof-artifacts)
- [Evidence resolution and citation schemes](#evidence-resolution-and-citation-schemes)
- [Focus Mode contract](#focus-mode-contract)
- [Audit ledger and tamper evidence](#audit-ledger-and-tamper-evidence)
- [Sensitivity redaction and FAIR CARE](#sensitivity-redaction-and-fair-care)
- [CI gates](#ci-gates)
- [Quickstart local](#quickstart-local)
- [How to verify with no merge without proof](#how-to-verify-with-no-merge-without-proof)
- [Release model immutable shipping records](#release-model-immutable-shipping-records)
- [Operations runbook minimum](#operations-runbook-minimum)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [Security](#security)
- [License and citation](#license-and-citation)
- [Glossary](#glossary)
- [Provenance notes](#provenance-notes)

---

## If you are new here start here

1) Read **[KFM constitutional contracts](#kfm-constitutional-contracts)**.  
2) Run **[Quickstart local](#quickstart-local)** (or confirm the stack is runnable).  
3) Run the verification harness: **[How to verify with no merge without proof](#how-to-verify-with-no-merge-without-proof)**.  
4) Internalize **processed serves truth** via **[Truth path](#truth-path)**.  
5) Learn why KFM cannot bluff via **[Evidence resolution](#evidence-resolution-and-citation-schemes)** and **[Focus Mode contract](#focus-mode-contract)**.

---

## Authority ladder

If something conflicts, resolve in this order:

1) **KFM constitutional contracts** (this README + `.github/README.md`)  
2) **Policy remains default deny** (fail closed)  
3) **Contracts and schemas** (`contracts/` or `schemas/`)  
4) **Receipts and catalogs** (`data/work/**`, `data/catalog/**`)  
5) **Docs and runbooks** (`docs/**`)  

> [!NOTE]
> If a change requires relaxing an invariant, write an ADR and update contracts + tests first. Do not weaken gates as a shortcut.

---

## KFM constitutional contracts

These invariants must remain true regardless of implementation. Each contract has an ID so it can be referenced in:
- CI gate names
- policy tests
- incident reports
- ADRs

| Contract ID | Invariant | Meaning | Minimum enforcement surface |
|---|---|---|---|
| **KFM‑C0** | **Trust membrane** | UI and external clients never access DBs or object storage directly | network isolation + API-only access + no direct credentials in frontend |
| **KFM‑C1** | **Fail-closed policy** | missing inputs or proofs → deny | default deny policies + regression tests |
| **KFM‑C2** | **Processed serves truth** | only processed + cataloged artifacts are served | API reads from processed catalogs only |
| **KFM‑C3** | **Promotion Contract required** | promotion denies without receipts, checksums, catalogs | CI gates + schema validation |
| **KFM‑C4** | **Deterministic spec hashing** | `spec_hash = sha256(JCS(spec))` (RFC 8785) | receipt gate + reproducibility tests |
| **KFM‑C5** | **Evidence refs resolvable** | citations resolve to evidence views | resolver contract tests |
| **KFM‑C6** | **Cite or abstain with audit reference** | Story Nodes and Focus Mode must cite or abstain; `audit_ref` always | output validator + policy |
| **KFM‑C7** | **Audit ledger integrity** | append-only audit events; integrity verifiable | ledger + checkpoints |
| **KFM‑C8** | **No silent redaction** | redaction and generalization are provenance-tracked transforms | derived datasets + PROV |
| **KFM‑C9** | **Immutable releases** | releases are append-only shipping records | release folder immutability + checksums |

> [!IMPORTANT]
> **No source, no answer** is an enforced contract in KFM.

### Repository health checklist

These are **repository-level** requirements. If any are missing, treat as governance gaps.

- [ ] `.github/CODEOWNERS` exists and covers all governed surfaces  
- [ ] branch protections require PR review + required checks for protected branches  
- [ ] CI is wired to fail closed (no green builds without proof artifacts)  
- [ ] secrets are never committed; secret scanning and pre-commit checks are enabled  
- [ ] GitHub Actions are pinned or constrained to reduce supply-chain risk  
- [ ] “verify” target exists (`make verify` or equivalent) and matches CI behavior  
- [ ] promotion gates validate receipts, catalogs, and cross-links before publish  

> [!NOTE]
> GitHub settings like branch protection and org-level 2FA are not stored in the repo. Track them as governance requirements in `.github/README.md` and enforce via “configuration drift” checks where feasible.

---

## Core features

These are the “boss-level” product capabilities KFM is designed to provide.

### Map and time product surface

- Layer browsing, toggles, filters, feature inspection
- Time-range control and time-aware layer rendering
- Provenance drawer per layer: attribution, license, coverage, freshness
- Evidence drawer: resolves citations into human-readable evidence views

### Story Nodes

- Narrative steps synchronized to map and time state
- Inline citations with resolvable evidence references
- Draft and published lifecycle with template validation and CI gates

### Focus Mode

- Grounded Q&A using **ViewState** (time range, bbox, active layers, story context)
- Builds an evidence pack; answer is allowed only when citations are present and sensitivity is allowed
- Returns `{ answer_markdown, citations[], audit_ref }` or abstains with `audit_ref`

### Proof layer with receipts catalogs and provenance

- Run receipts: `run_record.json`, `run_manifest.json`, `validation_report.json`
- Catalogs: **DCAT required**, **STAC conditional**, **PROV required**
- Determinism: checksums for artifacts + `spec_hash` for specs (RFC 8785 JCS + sha256)

### Policy as code governance

- Default deny across sensitive surfaces
- Field-level redaction, precision constraints, aggregate-only thresholds
- Promotion guard policies that block publish without proofs
- Kill switch to deny publish and risky endpoints without redeploy

---

## Standards compatibility matrix

KFM is standards-first. Pin exact versions in `docs/standards/standards-matrix.md` (or equivalent) and validate in CI.

| Standard or spec | Used for | Required in KFM | Where enforced |
|---|---|---:|---|
| RFC 8785 JSON Canonicalization Scheme | deterministic JSON hashing | ✅ | receipt validators + reproducibility checks |
| SHA-256 checksums | artifact integrity | ✅ | promotion gates + release manifests |
| DCAT | dataset catalog interoperability | ✅ | catalog validators |
| STAC | spatiotemporal asset metadata | ⚠️ conditional | stac-validate + contract tests |
| W3C PROV | lineage and transformations | ✅ | provenance validators + evidence resolver |
| OpenAPI | API contracts | ✅ | contract tests + CI |
| JSON Schema | receipts and contract validation | ✅ | tools + CI |
| GeoJSON | work/debug vectors and STAC Items | ✅ | validators |
| GeoParquet | publish-ready vectors | ✅ recommended | validators + downstream compatibility tests |
| COG or equivalent | publish-ready rasters | ✅ recommended | validators + STAC asset metadata |

> [!TIP]
> Keep this matrix small and enforceable. Standards exist to reduce ambiguity, not to create compliance theater.

---

## Repo directory layout

> [!IMPORTANT]
> **One canonical home per subsystem.** If your repo differs, document the mapping and keep boundaries identical.

```text
repo-root/
├─ .github/                     # governance SSoT: CI gates, templates, branch protection expectations
├─ policy/                      # OPA/Rego policies + tests (default deny; promotion guard; cite-or-abstain)
├─ contracts/                   # Promotion Contract + receipt schemas + catalog minimums + API contracts
│
├─ data/                        # governed data boundary: raw/work/processed + catalogs + bundles
│  ├─ registry/                 # dataset registry + controlled vocab (classification and flags)
│  ├─ raw/                      # immutable manifests + checksums (never served)
│  ├─ work/                     # receipts + validation reports (never served)
│  ├─ processed/                # publishable artifacts + checksums (servable truth)
│  ├─ catalog/
│  │  ├─ dcat/                  # DCAT required
│  │  ├─ stac/                  # STAC conditional
│  │  └─ prov/                  # PROV required
│  ├─ bundles/                  # optional: evidence bundles + fixtures
│  └─ audit/                    # optional: local audit checkpoints (prod often external)
│
├─ docs/                        # governed docs + standards + templates + Story Nodes + runbooks
├─ src/                         # backend: API gateway + pipelines + graph + shared utilities
├─ web/                         # UI: React or equivalent (never direct DB)
├─ tools/                       # validators + CI gates (verification tooling)
├─ tests/                       # trust gates (policy/receipts/catalogs/evidence/ai/ui)
├─ scripts/                     # thin runners (parity with CI; fail closed)
├─ watchers/                    # automation specs (optional; governed if present)
├─ infra/                       # GitOps and deploy (optional; governed if present)
└─ releases/                    # immutable shipping records + manifests + checksums
```

### Deep layout highlights

<details>
<summary><strong>Data plane</strong></summary>

```text
data/
├─ registry/                    # dataset profiles + policy taxonomy (build driver)
├─ raw/<dataset_id>/            # manifest.yml + checksums.sha256
├─ work/<dataset_id>/runs/<run_id>/
│  ├─ run_record.json
│  ├─ validation_report.json
│  └─ run_manifest.json         # Promotion Contract receipt
├─ processed/<dataset_id>/<version_id>/
│  └─ checksums.sha256
└─ catalog/
   ├─ dcat/<dataset_id>.json
   ├─ stac/<dataset_id>/**       # conditional
   └─ prov/<dataset_id>/run_<run_id>.json
```
</details>

<details>
<summary><strong>Docs plane</strong></summary>

```text
docs/
├─ templates/                   # universal doc + story node + api contract extensions
├─ standards/                   # STAC/DCAT/PROV profiles + governance standards
├─ governance/                  # ethics, sovereignty, review gates
├─ runbooks/                    # ops playbooks + incident response
└─ reports/story_nodes/
   ├─ draft/<story_slug>/story.md
   └─ published/<story_slug>/story.md
```
</details>

<details>
<summary><strong>Backend plane</strong></summary>

```text
src/
├─ server/                      # governed API + evidence resolver + audit
├─ pipelines/                   # ingestion, promotion, catalogs, receipts
├─ graph/                       # ontology + migrations + sync jobs
└─ shared/                      # IDs, time, provenance helpers
```
</details>

---

## Truth path

This is the only allowed route to “servable truth.”

```mermaid
flowchart LR
  S[Sources] --> W[Watchers and Connectors<br/>conditional fetch • spec_hash]
  W --> RAW[data/raw<br/>manifests • checksums]
  RAW --> RUN[Pipeline runs<br/>normalize • validate • enrich]
  RUN --> WORK[data/work<br/>run_record • validation_report • run_manifest]
  WORK -->|Promotion Contract gate| PROC[data/processed<br/>servable artifacts + checksums]
  PROC --> CAT[Catalogs<br/>DCAT • STAC • PROV]
  CAT --> API[Governed API<br/>policy • redaction • evidence resolver]
  API --> UI[UI<br/>Map • Timeline • Story Nodes]
  API --> FM[Focus Mode<br/>cite or abstain]
  API --> AUD[Audit ledger<br/>append-only]
```

### Promotion gates are explicit and fail closed

Promotion is denied unless each gate passes:

1) **Raw capture gate:** immutable manifest + checksums  
2) **Run receipt gate:** `run_record.json` + `validation_report.json` + `run_manifest.json`  
3) **Determinism gate:** spec hashing + artifact digests are stable  
4) **Catalog gate:** DCAT + PROV and optional STAC exist and validate  
5) **Cross-link gate:** citations resolve; catalogs reference digests; PROV references outputs  
6) **Policy gate:** classification exists; redaction transforms are tracked  
7) **Audit gate:** promotion event emitted; `audit_ref` recorded  

> [!WARNING]
> If any gate cannot be executed reproducibly in CI, treat it as a P0 gap and fix the gate before scaling data onboarding.

---

## Promotion Contract and proof artifacts

Promotion requires at minimum:

- receipts: `run_record.json` + `run_manifest.json`
- validation: `validation_report.json`
- deterministic checksums (raw + processed)
- catalogs: DCAT always; STAC conditional; PROV required
- sensitivity classification and redaction provenance when needed
- audit event recorded and referenced

> [!NOTE]
> Keep the Promotion Contract schema minimal but strict. Add fields only when a validator and a consumer exist.

---

## Evidence resolution and citation schemes

KFM treats citations as resolvable references, not URLs.

Supported schemes:

- `prov://`, `stac://`, `dcat://`, `doc://`, `graph://` and optional `oci://`

Acceptance criteria:

- citations resolve to human-readable evidence views
- missing target → 404; unauthorized or policy deny → 403 with non-leaky error semantics
- UI goal: resolve any citation in ≤ 2 API calls

---

## Focus Mode contract

Focus Mode must cite resolvable evidence or abstain. Every response returns `audit_ref`.

```json
{
  "answer_markdown": "…",
  "citations": [{"ref":"prov://…","label":"…"}],
  "audit_ref": "audit://event/…"
}
```

### Cite-or-abstain is enforced

- If the evidence pack is empty → abstain
- If policy denies any required evidence → abstain
- If citations cannot resolve → abstain
- If sensitivity requires generalization and it is not available → abstain

---

## Audit ledger and tamper evidence

Audit is governed:

- append-only writes
- `audit_ref` returned on governed responses
- checkpoints or integrity chaining where supported

**No audit, no answer.**

---

## Sensitivity redaction and FAIR CARE

Common sensitivity classes:

- `public`
- `restricted`
- `sensitive-location`
- `aggregate-only`

Rules:

- redaction and generalization are first-class transforms tracked in PROV
- deny on missing classification
- never leak precise sensitive coordinates to unauthorized roles
- when in doubt: reduce precision, aggregate, or abstain

> [!IMPORTANT]
> If you introduce a new sensitivity class, you must update: vocabulary, policy, validators, and tests.

---

## CI gates

Authoritative list: `.github/README.md`

Expected minimum gates:

- docs and Story Nodes validation
- contracts and schemas validation
- receipts validation
- catalogs validation
- policy tests and regressions
- evidence resolver contract tests
- build and smoke tests
- optional supply-chain verification when enabled

---

## Quickstart local

### Prerequisites

- Docker + Docker Compose v2
- Recommended: `make`, `jq`, `opa`, `conftest`

### Start the stack

```bash
cp .env.example .env
docker compose up --build
```

Optional profiles if defined:

```bash
docker compose --profile policy --profile storage --profile vector --profile search up --build
```

### Default URLs

- UI: `http://localhost:3000`
- API docs: `http://localhost:8000/docs`
- Neo4j: `http://localhost:7474`
- OPA: `http://localhost:8181`

> [!NOTE]
> If the repo cannot start a local stack, treat that as a P0 delivery gap. KFM governance depends on runnable verification.

---

## How to verify with no merge without proof

Preferred: run the same checks CI runs.

```bash
# umbrella target if present
make verify
```

Useful drills:

```bash
# policy
opa test policy -v
conftest test . -p policy/conftest

# receipts and catalogs (examples; adjust to your tools)
./scripts/validate_receipts.sh
./scripts/validate_catalogs.sh
./scripts/validate_contracts.sh
```

> [!IMPORTANT]
> If any validator cannot run due to missing tooling, treat it as a governance gap. Fix the tooling or adjust the repo until checks are reproducible.

---

## Release model immutable shipping records

Releases are immutable proof of what shipped:

- `releases/` is append-only
- never edit an existing release folder
- release manifests + checksums are required

See `releases/README.md`.

---

## Operations runbook minimum

Minimum operational signals:

- ingest success and failure with durations
- dataset freshness versus cadence
- drift metrics: missingness, distributions, geometry errors
- policy denials and evidence resolution failures
- audit ledger health and checkpoint integrity

Emergency controls:

- policy-controlled kill switch to disable publish and risky endpoints without redeploy

---

## Roadmap

- governance and CI hardening: validators, policy regressions, contract tests
- Promotion Contract and receipts standardization
- evidence bundles and resolver UX
- dataset integrations at scale: registry-driven and repeatable
- Story Nodes and Focus Mode evaluation harness

---

## Contributing

See `CONTRIBUTING.md` and `.github/PULL_REQUEST_TEMPLATE.md`.

Contribution rules:

- keep changes small and evidence-backed
- do not weaken gates to “make CI green”
- if you change meaning of a contract: update schemas, validators, and tests first

---

## Security

See `.github/SECURITY.md` for private vulnerability reporting.

Security is a system property. These must hold together:

- trust membrane
- default-deny policy
- receipts and catalogs
- auditability

---

## License and citation

- License: `LICENSE`
- Citation metadata: `CITATION.cff`

---

## Glossary

| Term | Meaning in KFM |
|---|---|
| **Watcher or connector** | a governed fetch and normalization boundary for upstream sources |
| **Dataset ID** | stable identifier for a dataset family |
| **Version ID** | stable identifier for a promoted processed version |
| **Run ID** | immutable identifier for a pipeline run producing receipts and outputs |
| **Receipt** | machine-validated proof artifacts of how an output was produced |
| **Catalog** | discoverability and interoperability metadata: DCAT and STAC |
| **Provenance** | lineage graph that records entities, activities, and agents |
| **Evidence ref** | resolvable reference like `prov://...` used for citations |
| **Audit ref** | resolvable reference like `audit://event/...` proving governed outputs were logged |
| **Fail closed** | deny or abstain if proofs are missing or policy cannot prove allow |
| **Processed serves truth** | only processed outputs with catalogs and receipts are served |

---

## Provenance notes

Aligned to Feb 2026 governance patterns:

- fail-closed promotion using receipts, catalogs, and checksums
- deterministic spec hashing using RFC 8785 JCS plus sha256
- cite-or-abstain Focus Mode with resolvable evidence refs
- audit references on governed responses
- immutable releases as shipping proof

<div align="center">

**KFM Principle:** *If it can’t be traced, it can’t be trusted.* 🔎

</div>
