<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/8d2fb4f2-0f5f-4b7f-bb8d-acde0d0be6f7
title: tools — Validators, link checkers, and CLI utilities
type: standard
version: v3
status: draft
owners: TBD
created: 2026-03-03
updated: 2026-03-05
policy_label: public
related:
  - tools/validators/
  - tools/linkcheck/
  - policy/
  - contracts/
tags: [kfm, tools, validation, governance, policy, determinism]
notes:
  - Status tags are used on all non-trivial statements: CONFIRMED, PROPOSED, UNKNOWN.
  - Tools are deterministic, testable, and safe-by-default; prefer machine-readable outputs for CI.
  - This doc describes the intended contract; anything labeled UNKNOWN must be verified in the current checkout.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

<div align="center">

# 🧰 `tools/` — Validators, link checkers, and CLI utilities

**Purpose:** Evidence-first tooling that enforces KFM’s **Promotion Contract** by validating catalogs, links, policy inputs, and integrity signals before anything is **publishable**.

<!-- Badges (placeholders — replace TODOs with real workflow names/paths) -->
<img alt="CI" src="https://img.shields.io/badge/CI-TODO-lightgrey" />
<img alt="Promotion Contract" src="https://img.shields.io/badge/Promotion%20Contract-CI%20gated-lightgrey" />
<img alt="Catalog triplet" src="https://img.shields.io/badge/DCAT%2FSTAC%2FPROV-validated-lightgrey" />
<img alt="Fail closed" src="https://img.shields.io/badge/Posture-fail--closed%20%7C%20default--deny-lightgrey" />

</div>

> **Status:** draft • **Owners:** TBD  
> **Policy label:** public  
> **Primary posture:** **fail-closed**, **default-deny**, **machine-checkable outputs**  
> **Reminder (design invariant):** clients/UI never bypass the governed API + policy boundary (trust membrane).

<div align="center">

[Scope](#scope) ·
[Where it fits](#where-it-fits) ·
[Inputs](#inputs) ·
[Exclusions](#exclusions) ·
[Directory tree](#directory-tree) ·
[Quickstart](#quickstart) ·
[Tool behavior contract](#tool-behavior-contract) ·
[Tool registry](#tool-registry) ·
[Promotion Contract mapping](#promotion-contract-mapping) ·
[Work package alignment](#work-package-alignment) ·
[Adding a tool](#adding-a-tool) ·
[Safety and sensitivity](#safety-and-sensitivity) ·
[Unknowns and verification](#unknowns-and-verification) ·
[FAQ](#faq) ·
[Sources](#sources)

</div>

---

## Status tags used in this README

<details>
<summary>Click to expand</summary>

- **CONFIRMED:** Documented in KFM vNext design / governance / inventory docs (contract intent).
- **PROPOSED:** Recommended pattern or target structure; safe to discuss, not safe to enforce until ratified.
- **UNKNOWN:** Not verified in your current checkout; includes the smallest steps to verify.

</details>

> [!IMPORTANT]
> **Hallucination guardrail (repo-critical):** Do not claim a tool/path exists or is implemented until verified in the live repo tree for *your* branch/checkout.  
> This README is written to **fail closed**: anything uncertain is labeled **UNKNOWN** and paired with a verification step.

[↑ Back to top](#top)

---

## Scope

- **CONFIRMED:** `tools/` is the home for **validators, link checkers, and CLI utilities** that support CI gates and promotion/publishing controls.
- **CONFIRMED:** Catalog validation is a first-class gate: KFM treats **DCAT + STAC + PROV** (“the triplet”) as contract surfaces. Broken catalogs or broken cross-links must block promotion (or keep data in quarantine).
- **PROPOSED:** Where possible, represent checks as deterministic tools with machine-readable reports so CI can be **auditable** and **merge-blocking**.

[↑ Back to top](#top)

---

## Where it fits

- **CONFIRMED:** KFM’s lifecycle is a set of storage zones + validation gates (truth path), not a metaphor.
- **CONFIRMED:** Tools support the “trust foundation” work: deterministic identity (`spec_hash`), triplet validators, and link-checking.
- **PROPOSED:** Treat `tools/` as **the check layer**: anything that can be expressed as a deterministic check should live here and be wired into CI.

### Conceptual lanes: CI ↔ runtime

```mermaid
flowchart LR
  subgraph CI_LANE["CI lane"]
    V["validators and linkcheck"] --> R["reports and receipts"]
    R --> P["policy tests (OPA or equivalent)"]
  end

  subgraph RUNTIME_LANE["Runtime lane"]
    UI["UI clients"] --> API["Governed API (PEP)"]
    API --> PDP["Policy engine"]
    API --> ER["Evidence resolver"]
  end

  P -->|blocks merge or promotion| Merge["Protected branches or releases"]
  Merge -->|deploy| API
```

[↑ Back to top](#top)

---

## Inputs

### Acceptable inputs

- **CONFIRMED:** Catalog artifacts and lineage bundles (DCAT, STAC, PROV) and their cross-links.
- **CONFIRMED:** Receipts/manifests that bind **inputs + transforms + outputs** via checksums/digests.
- **PROPOSED:** Schema contracts and controlled vocabularies used by validators (JSON Schema, OpenAPI, DCAT/STAC/PROV profiles).
- **PROPOSED:** Policy bundles and fixtures used by CI policy tests (default-deny posture).
- **PROPOSED:** Test fixtures for validators/linkcheckers (small, synthetic, safe-to-share).

### Outputs

- **CONFIRMED:** Machine-readable validation outputs suitable for CI gating (non-zero exit on failure).
- **PROPOSED:** JSON/JSONL reports for artifact upload + downstream review, plus optional human-readable summaries.

[↑ Back to top](#top)

---

## Exclusions

Do **not** put these in `tools/`:

- **PROPOSED:** Long-running servers, UI code, or production services (belongs in `apps/` / service packages).
- **PROPOSED:** Pipeline business logic (belongs in pipeline/orchestration packages; tools validate outputs, they do not *become* pipelines).
- **PROPOSED:** Secrets, API keys, or private datasets (tools must run with least privilege; use fixtures).
- **PROPOSED:** One-off scripts without tests/fixtures or deterministic outputs.

[↑ Back to top](#top)

---

## Directory tree

- **UNKNOWN:** The authoritative `tools/` tree in *your current checkout*.
  - **Minimum verification steps (paste into PR/notes when changing gates):**
    1. `git rev-parse HEAD`
    2. `tree -L 3 tools`
    3. `rg -n "spec_hash|dcat|stac|prov|linkcheck|catalog_linkcheck" tools -S`

### Target layout (contract-aligned)

- **CONFIRMED (design intent):** WP-01/WP-02 explicitly call for `tools/hash/spec_hash_cli`, catalog validators under `tools/validators/*`, and `tools/linkcheck/catalog_linkcheck` (names may vary by implementation).
- **PROPOSED:** Keep tooling grouped by contract surface (hashing/identity, catalog validation, link integrity).

```text
tools/
├── README.md
├── hash/
│   └── spec_hash_cli/              # WP-01 deliverable (name may differ)
├── validators/
│   ├── dcat_validator/             # WP-02 deliverable
│   ├── stac_validator/             # WP-02 deliverable
│   ├── prov_validator/             # WP-02 deliverable
│   └── (thin CLI entrypoints)      # node/python wrappers calling library logic
└── linkcheck/
    └── catalog_linkcheck/          # WP-02 deliverable
```

> [!NOTE]
> **UNKNOWN (this checkout):** exact folder names, CLIs, and languages (Node/Python/etc).  
> Verify with `tree -L 3 tools` before wiring CI paths.

[↑ Back to top](#top)

---

## Quickstart

- **UNKNOWN:** Exact CLI names/flags in your current checkout.

### 1) Discover what exists (always safe)

```bash
git rev-parse HEAD
tree -L 3 tools
rg -n "spec_hash|validate_(dcat|stac|prov)|catalog_linkcheck|linkcheck" tools -S
```

### 2) Run tools in “help” mode (pattern)

```bash
# Replace <tool> with actual CLI entrypoints found by rg/tree
<tool> --help || true
<tool> --version || true
```

### 3) Typical local runs (pattern)

> [!IMPORTANT]
> These are *patterns* (PROPOSED) until you confirm exact entrypoints.

```bash
# Validate catalogs (example paths — adapt to your repo)
<validate_dcat>  data/catalog/dcat/<dataset>.jsonld
<validate_stac>  data/catalog/stac/<dataset>/
<validate_prov>  data/prov/<dataset>/bundle.json

# Link-check cross-links across the triplet
<catalog_linkcheck> data/catalog/
```

### 4) Notes on known historical entrypoints (inventory-only)

- **CONFIRMED (inventory doc):** Some repo snapshots referenced Node.js validators under `tools/validators/` (e.g., `validate_dcat.js`, `validate_stac.js`) and a DCAT validator README describing required fields + fail-closed exit codes.
- **UNKNOWN (this checkout):** Whether those exact filenames still exist.

[↑ Back to top](#top)

---

## Tool behavior contract

### CLI contract (recommended)

- **PROPOSED:** Every tool **MUST**:
  - support `--help`,
  - return **exit code 0** on success and **non-zero** on failure,
  - fail closed on missing required inputs (schemas, catalogs, receipts) when used as a promotion gate,
  - avoid nondeterminism (stable sorting; pinned deps; no time-based IDs unless injected),
  - log in a CI-friendly way (single-line summaries + optional verbose mode).

- **PROPOSED:** Every tool **SHOULD**:
  - support `--version`,
  - support `--format json|text`,
  - support `--report <path>` (JSON/JSONL) when used as a hard CI gate,
  - include `report_schema_version` in machine outputs.

### Recommended report shape (example)

```json
{
  "report_schema_version": "kfm.tool.report.v1",
  "tool": "kfm.validate_dcat",
  "tool_version": "0.1.0",
  "ok": false,
  "checked": [
    {"path": "data/catalog/dcat/dataset.jsonld", "kind": "dcat.dataset"}
  ],
  "errors": [
    {"code": "missing_required_field", "path": "$.license", "message": "license is required"}
  ],
  "warnings": [],
  "timing_ms": 1234
}
```

### Network policy (safe-by-default)

- **PROPOSED:** Tools should default to **no network I/O** unless explicitly enabled (e.g., `--network` / `--fetch`).
- **PROPOSED:** If network is enabled, tools should log endpoints accessed (never secrets) and record validators (ETag/Last-Modified) in receipts when relevant.

[↑ Back to top](#top)

---

## Tool registry

> This registry separates **design intent** from **what is verified in your checkout**.

| Surface | Expected tool family | Status | Why it exists | Verify in checkout |
|---|---|---:|---|---|
| Deterministic identity | `spec_hash` helper/CLI | **CONFIRMED** | Stable dataset versioning + drift detection | `rg -n "spec_hash" tools -S` |
| Catalog validation | DCAT validator | **CONFIRMED** | Triplet is contract surface | `tree -L 3 tools/validators` |
| Catalog validation | STAC validator | **CONFIRMED** | Asset metadata + time/space indexing | `tree -L 3 tools/validators` |
| Catalog validation | PROV validator | **CONFIRMED** | Lineage bundles are required | `tree -L 3 tools/validators` |
| Link integrity | Triplet link checker | **CONFIRMED** | Cross-links must resolve without guessing | `tree -L 3 tools/linkcheck` |
| Promotion gate driver | Gate runner (or CI harness) | **PROPOSED** | Make A–D (+ additional gates) merge-blocking | `rg -n "promote|gate" tools .github/workflows -S` |
| Policy hygiene helpers | Policy bundle checks | **PROPOSED** | Keep CI and runtime aligned | `tree -L 3 tools` + `tree -L 3 ../policy` |

> [!NOTE]
> A row marked **CONFIRMED** means “documented as required in design/work-package intent,” not “guaranteed present in this checkout.”

[↑ Back to top](#top)

---

## Promotion Contract mapping

- **CONFIRMED:** Promotion to PUBLISHED is blocked unless minimum gates are met.
- **CONFIRMED:** Gate naming beyond A–D varies across the current design inputs; do **not** treat the letter mapping as canonical until the repo pins a single `promotion_contract` doc as source of truth.
- **PROPOSED:** Keep the canonical mapping in `docs/governance/promotion_contract.md` (or equivalent) and have `tools/` implement the checks.

### Stable core gates (consistent across design inputs)

| Gate | Intent (what must be true) | Tool coverage (typical) |
|---|---|---|
| A | Identity & versioning (`dataset_id`, `dataset_version_id`, stable `spec_hash`, digests) | `tools/hash/` + checksum/digest verifiers |
| B | Licensing & rights metadata + upstream terms snapshot | catalog validators + policy tests |
| C | Sensitivity classification + redaction/generalization plan (when needed) | policy tests + redaction verifiers |
| D | Catalog triplet validation (DCAT/STAC/PROV validate + cross-link) | `tools/validators/` + `tools/linkcheck/` |

### Additional gates (two documented variants)

> These are both **CONFIRMED as “documented variants”**, but **PROPOSED** as *the* canonical letter mapping until the repo chooses one.

**Variant 1 (Delivery-plan framing):** QA thresholds → receipts/audit → release manifest  
- E: QA & thresholds  
- F: Run receipt & audit record  
- G: Release manifest (artifacts + digests)

**Variant 2 (Definitive-guide framing):** receipts/checksums → policy/contract tests → optional production posture  
- E: Run receipt & checksums  
- F: Policy tests & contract tests  
- G: Optional but recommended (SBOM, perf smoke, accessibility smoke)

### Practical “tools ↔ gates” matrix (recommended)

| Check | Gate(s) it supports | Expected artifact(s) |
|---|---|---|
| `spec_hash` stability | A | `spec_hash`, golden test vectors |
| Catalog profile validation | D (and B/C where encoded) | validator report(s) |
| Link integrity validation | D | linkcheck report |
| License/rights completeness check | B | rights report + terms snapshot ref |
| Sensitivity/redaction verification | C | redaction receipt + policy decision refs |
| Run receipt schema validation | (E/F depending on contract) | `run_receipt.json` (or equivalent) |
| Policy fixture tests | (F in some variants) | conftest/OPA report |

[↑ Back to top](#top)

---

## Work package alignment

- **CONFIRMED:** vNext build order includes work packages for spec hashing and for catalog validators/link checking; those are first-class deliverables.
- **PROPOSED:** `tools/` should fully cover WP‑01/WP‑02 and provide CI harness support for policy parity work.

| Work package | What it builds | What belongs in `tools/` |
|---|---|---|
| WP‑01 | Deterministic `spec_hash` + controlled vocab validation | `tools/hash/…` + golden tests |
| WP‑02 | DCAT/STAC/PROV validators + link checker | `tools/validators/…` + `tools/linkcheck/…` |
| WP‑03 | Policy pack + fixtures (default-deny) | Policy lives in `../policy/`; tools may add guard scripts |
| WP‑04 | Evidence resolver service (runtime) | Tools provide fixtures + contract tests (if applicable) |

[↑ Back to top](#top)

---

## Adding a tool

### Definition of Done (minimum)

- **PROPOSED:** A new tool is not “real” until it is:
  - documented (README with inputs/outputs + exit codes),
  - tested (fixtures + unit tests; property tests where helpful),
  - deterministic (same inputs → same output bytes, stable ordering),
  - wired into CI as a required check if it enforces Promotion Contract gates.

### Template (recommended)

```text
tools/<tool-name>/
├── README.md
├── src/                      # optional
├── tests/                    # fixtures + unit tests
└── package.json / pyproject  # if needed
```

[↑ Back to top](#top)

---

## Safety and sensitivity

- **CONFIRMED:** Sensitive-location leakage is a high-impact risk; mitigations include restricted precise datasets + public generalized derivatives, redaction tests, and default-deny controls.
- **CONFIRMED:** Licensing/rights are promotion gates; “online availability” does not imply reuse permission.
- **PROPOSED:** Any tool that reads geometry or location-like fields should support a safe-mode verification path:
  - confirms required redaction receipts exist for non-public releases,
  - checks “no precise coordinates” rules for public layers where applicable,
  - detects PII-like columns in public-facing schemas.

### Safe-by-default checks (recommended)

- **PROPOSED:** Add a `tools/validators/safety/` suite that verifies:
  - `policy_label` consistency,
  - required redaction receipts exist when `policy_label != public`,
  - public-safe schema rules,
  - no prohibited fields leak into PUBLISHED artifacts.

[↑ Back to top](#top)

---

## Unknowns and verification

- **UNKNOWN:** Which `tools/` checks are required to merge in CI.
  - **Minimum verification steps:**
    1. `ls .github/workflows`
    2. `rg -n "tools/" .github/workflows -S`
    3. Confirm required checks in branch protection settings (if enabled).

- **UNKNOWN:** The exact validator flags and report shapes.
  - **Minimum verification steps:**
    1. Run each tool with `--help`
    2. Capture one “pass” and one “fail” report as fixtures under `tools/**/tests/fixtures/`

### Verification checklist (copy/paste)

- [ ] Captured repo commit hash (`git rev-parse HEAD`)
- [ ] Captured `tools/` tree (`tree -L 3 tools`)
- [ ] Verified which validators/link checks exist and their CLI flags
- [ ] Confirmed which CI checks block merge
- [ ] Added/updated fixtures for one failing and one passing catalog case
- [ ] Confirmed determinism (same inputs → same report bytes)

[↑ Back to top](#top)

---

## FAQ

### Why do tools “fail closed”?
- **CONFIRMED:** KFM treats promotion/publishing as a governed act; failing validation must block promotion so PUBLISHED surfaces never serve unverifiable or unlicensed artifacts.

### Why so many JSON reports?
- **PROPOSED:** Reports bridge tooling and policy: CI can upload them, policy checks can evaluate them, and stewards can review them without rerunning local commands.

### Can tools auto-fix catalogs?
- **PROPOSED:** Yes—but put mutations behind `--write` and keep CI in read-only validation mode so merges remain explainable and deterministic.

[↑ Back to top](#top)

---

## Sources

These are the **design inputs** used to label claims in this README (treat as contract intent until superseded by in-repo canonical docs):

- **KFM “Architecture, Governance, and Delivery Plan”** (includes Promotion Contract framing, verification checklist, work packages overview)
- **KFM “Definitive Design & Governance Guide (vNext)” / Source Snapshots bundle** (triplet definition, zone definitions, Promotion Contract gates, WP-01/WP-02 deliverables)
- **KFM Prime Document** (repo inventory notes; historical mentions of `tools/validators/*` entrypoints and fail-closed behavior)
- **KFM “New Ideas” packs** (optional patterns/snippets; treat as PROPOSED unless adopted and wired in CI)

[↑ Back to top](#top)
