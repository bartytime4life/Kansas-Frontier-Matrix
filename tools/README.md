<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/8d2fb4f2-0f5f-4b7f-bb8d-acde0d0be6f7
title: tools — Validators, link checkers, and CLI utilities
type: standard
version: v3
status: draft
owners: TBD
created: 2026-03-03
updated: 2026-03-04
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

<div align="center">

# 🧰 `tools/` — validators, link checkers, and CLI utilities

**Purpose:** Evidence-first tooling that enforces KFM’s **Promotion Contract** by validating catalogs, links, policy inputs, and integrity signals before anything is **publishable**.

<!-- Badges (placeholders — replace TODOs with real workflow names/paths) -->
<img alt="CI" src="https://img.shields.io/badge/CI-TODO-lightgrey" />
<img alt="Policy Gates" src="https://img.shields.io/badge/OPA%2FConftest-Gates-TODO-lightgrey" />
<img alt="Catalog" src="https://img.shields.io/badge/DCAT%2FSTAC%2FPROV-Validated-TODO-lightgrey" />
<img alt="Determinism" src="https://img.shields.io/badge/Deterministic-Tools-TODO-lightgrey" />
<img alt="Fail closed" src="https://img.shields.io/badge/Fail--closed-Default--deny-lightgrey" />

</div>

> **Status:** draft  
> **Owners:** TBD  
> **Policy label:** public  
> **Primary posture:** **fail-closed**, **default-deny**, **deterministic outputs**  
> **Repo invariant reminder:** UI/clients do not talk to storage directly; policy is enforced at the PEP/API boundary.

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
[Policy toolchain compatibility](#policy-toolchain-compatibility) ·
[Adding a tool](#adding-a-tool) ·
[Safety and sensitivity](#safety-and-sensitivity) ·
[Unknowns and verification](#unknowns-and-verification) ·
[FAQ](#faq)

</div>

---

## Status tags used in this README

<details>
<summary>Click to expand</summary>

- **CONFIRMED:** Backed by KFM design/inventory documents; treated as intended contract.
- **PROPOSED:** Recommended pattern or target structure; may not exist yet.
- **UNKNOWN:** Not verified in your current checkout; includes the smallest steps to verify.

</details>

---

## Scope

- **CONFIRMED:** `tools/` is the home for **validators, link checkers, and CLI utilities** that support KFM’s promotion gates and “trust foundation.”
- **CONFIRMED:** Catalog validation is not optional: KFM treats **DCAT + STAC + PROV** as *contract surfaces*; broken catalogs or broken cross-links must block promotion.
- **CONFIRMED:** Tools must be **deterministic** and **fail-closed** (missing required evidence, policy inputs, or integrity signals ⇒ non-zero exit).

[Back to top](#)

---

## Where it fits

- **CONFIRMED:** KFM’s runtime is protected by a **trust membrane** (Policy Enforcement Point + Evidence Resolver). Clients and UI must not access stores directly; policy is evaluated uniformly at the boundary.
- **CONFIRMED:** KFM requires the same policy semantics in **CI** and **runtime** (or at least the same fixtures + outcomes). CI guarantees are meaningless if runtime differs.
- **PROPOSED:** Treat `tools/` as the repo’s **governance runtime**: anything that can be expressed as a deterministic check should live here and be wired into required CI checks.

```mermaid
flowchart LR
  subgraph CI[CI Lane]
    V[validators + linkcheck] --> R[reports & receipts]
    R --> P[policy tests (OPA/Conftest)]
  end

  subgraph Runtime[Runtime Lane]
    UI[UI clients] --> API[Governed API (PEP)]
    API --> PDP[Policy Engine (OPA/Rego)]
    API --> ER[Evidence Resolver]
  end

  CI -->|blocks merge/promotion| Merge[Protected branches / releases]
  Merge --> Runtime
```

[Back to top](#)

---

## Inputs

### Acceptable inputs

- **CONFIRMED:** Catalog artifacts and lineage bundles (DCAT, STAC, PROV) and their cross-links.
- **CONFIRMED:** Receipts/manifests that bind **inputs + transforms + outputs** via deterministic hashes/digests.
- **PROPOSED:** Schema contracts and controlled vocabularies used by validators (JSON Schema, SHACL, OpenAPI, STAC/DCAT profiles).
- **PROPOSED:** Policy bundles and fixtures (allow/deny + obligations) used by Conftest/OPA.
- **PROPOSED:** Test fixtures for validators/linkcheckers (small, synthetic, and safe to publish).

### Outputs

- **CONFIRMED:** Machine-readable validation outputs suitable for CI gating (non-zero exit on failure).
- **PROPOSED:** JSON/JSONL reports for artifact upload + downstream policy evaluation, plus optional human-readable summaries.

[Back to top](#)

---

## Exclusions

- **PROPOSED:** Long-running servers and UI code (belongs in `apps/` or service packages).
- **PROPOSED:** Pipeline “business logic” (belongs in `pipelines/` or domain packages; tools may validate pipeline outputs but should not be pipelines).
- **PROPOSED:** Secrets, API keys, or private data dumps (tools must run with least privilege).
- **PROPOSED:** One-off scripts without tests/fixtures or deterministic outputs.

[Back to top](#)

---

## Directory tree

- **UNKNOWN:** The authoritative `tools/` tree in *your current checkout*.
  - **Minimum verification steps (run and paste into PR/notes):**
    1. `git rev-parse HEAD`
    2. `tree -L 3 tools`
    3. `rg -n "validate_(dcat|stac|prov)|linkcheck|spec_hash|receipt|promote" tools -S`

### Target layout

- **PROPOSED:** Keep tooling grouped by contract surface (catalog validation, hashing, promotion gating, policy hygiene).

```text
tools/
├── README.md
├── validators/                       # catalog validators (DCAT/STAC/PROV)
│   ├── dcat_validator/               # profile rules + fixtures + docs
│   ├── stac_validator/
│   ├── prov_validator/
│   └── validate_*.{js,ts,py}         # thin CLIs wrapping library logic
├── linkcheck/                        # referential integrity across catalogs/evidence
│   └── catalog_linkcheck.{js,ts,py}
├── hash/                             # spec_hash + digest helpers
│   └── spec_hash_cli.{ts,py}
├── promote/                          # promotion gate driver (validate + release index)
│   ├── validate_and_release.sh
│   ├── jcs_hash.py
│   ├── verify_checksums.py
│   ├── build_oci_evidence.py
│   └── write_release_index.py
├── policy/                           # policy hygiene helpers (optional)
│   └── policy_v1_guard.sh
└── setup.sh                          # optional: install pinned toolchain (CI + dev)
```

> **PROPOSED:** If you ever rename `tools/validators/` → `tools/validation/catalog/`, do it with a migration plan:
> - keep a compatibility shim (thin wrapper CLIs),
> - update CI paths first,
> - update docs last,
> - and add a redirect note for one release cycle.

[Back to top](#)

---

## Quickstart

- **UNKNOWN:** Exact CLI names/flags in your current checkout.
  - **Minimum verification steps:** run each tool with `--help` and update this section with exact invocations.

### Typical local runs (pattern)

```bash
# 1) Discover tools
ls -la tools
ls -la tools/validators || true
ls -la tools/linkcheck  || true

# 2) Run validators in help mode (adjust to actual filenames)
node tools/validators/validate_dcat.js --help || true
node tools/validators/validate_stac.js --help || true
node tools/validators/validate_prov.js --help || true

# 3) Validate catalogs (paths are examples)
node tools/validators/validate_dcat.js catalog/dcat/dataset.jsonld
node tools/validators/validate_stac.js catalog/stac/items/item.json
node tools/validators/validate_prov.js catalog/prov/run.prov.jsonld

# 4) Link-check the catalog triplet
node tools/linkcheck/catalog_linkcheck.js catalog/

# 5) Emit a JSON report for CI (recommended contract)
node tools/validators/validate_dcat.js catalog/dcat/dataset.jsonld --report artifacts/dcat.report.json
```

> **PROPOSED:** Prefer deterministic, “read-only” checks. If a tool can mutate files (format, fix, rewrite), put it behind an explicit `--write` flag and keep CI in non-mutating mode.

[Back to top](#)

---

## Tool behavior contract

### CLI contract (required for all tools)

- **PROPOSED:** Every tool **MUST**:
  - support `--help`,
  - return **exit code 0** on success and **non-zero** on failure,
  - avoid nondeterminism (stable sorting; pinned deps; no time-based IDs unless injected),
  - log in a CI-friendly way (single-line summaries + optional verbose mode),
  - support `--report <path>` (JSON/JSONL) when the tool is used as a hard gate.

- **PROPOSED:** Every tool **SHOULD**:
  - support `--version`,
  - support `--format json|text`,
  - run offline by default (see Network policy below),
  - include a `report_schema_version` field in JSON output.

### Report format (recommended)

- **PROPOSED:** Reports SHOULD be small, stable, and machine-checkable.

```json
{
  "report_schema_version": "kfm.tool.report.v1",
  "tool": "kfm.validate_dcat",
  "tool_version": "0.1.0",
  "ok": false,
  "checked": [
    {"path": "catalog/dcat/dataset.jsonld", "kind": "dcat.dataset"}
  ],
  "errors": [
    {"code": "missing_required_field", "path": "$.license", "message": "license is required"}
  ],
  "warnings": [],
  "timing_ms": 1234
}
```

### Network policy

- **PROPOSED:** Tools MUST be safe-by-default:
  - **no network I/O** unless `--network`/`--fetch` is explicitly passed,
  - if network is enabled, tools MUST log the endpoints accessed (without secrets),
  - tools MUST remain reproducible (pin versions; record validators such as ETag/Last-Modified when relevant).

[Back to top](#)

---

## Tool registry

> This registry distinguishes “referenced in design docs” from “verified in your checkout.”

| Status | Path (relative) | Tool | Primary job | CI blocking? | Network default |
|---|---|---|---|---:|---|
| **CONFIRMED** (referenced) | `validators/` | Catalog validators | Validate DCAT/STAC/PROV profiles | ✅ | off |
| **CONFIRMED** (referenced) | `linkcheck/` | Catalog link checker | Verify cross-links so EvidenceRefs resolve without guessing | ✅ | off |
| **CONFIRMED** (referenced) | `hash/` | `spec_hash` helper(s) | Deterministic spec hashing for identity/versioning | ✅ | off |
| **PROPOSED** | `promote/` | Promotion gate driver | Validate + emit release index + fail-closed audit events | ✅ | off |
| **PROPOSED** | `policy/` | Policy hygiene helpers | Rego v1 guardrails + bundle checks | ✅ | off |
| **PROPOSED** | `specgen/` | Spec-driven generators | Emit code/tests/receipts from contracts | ✅ | off |
| **UNKNOWN** | `validators/validate_dcat.js` | DCAT CLI | Validate a DCAT dataset/distribution record | ✅ | off |
| **UNKNOWN** | `validators/validate_stac.js` | STAC CLI | Validate STAC Item/Collection/Catalog | ✅ | off |
| **UNKNOWN** | `validators/dcat_validator/README.md` | Validator contract doc | Required fields + exit code behavior | ✅ | n/a |

**Why “UNKNOWN” rows exist:** KFM explicitly warns against claiming a file exists until verified in the live repo tree; this README keeps the *contract* and lists minimal verification steps.

[Back to top](#)

---

## Promotion Contract mapping

- **CONFIRMED:** Promotion to PUBLISHED is blocked unless minimum gates are met (identity, licensing, sensitivity, triplet validation, QA thresholds, receipts, release manifest).
- **PROPOSED:** This matrix is the default “who covers what” mapping for `tools/`.

| Gate | What must be present | Tool types that cover it | Typical artifacts produced |
|---|---|---|---|
| A | dataset_id + version, deterministic spec_hash, content digests | `hash/`, digest checkers | `spec_hash.txt`, `digests.json` |
| B | license/rights fields + upstream terms snapshot | validators + policy checks | `rights_snapshot.*`, `license.report.json` |
| C | policy_label + redaction obligations where needed | policy tests + redaction verifiers | `redaction_receipt.json`, policy report |
| D | DCAT/STAC/PROV all validate and cross-link | `validators/` + `linkcheck/` | validator reports, link map |
| E | dataset QA checks + thresholds met | domain QA tools | `qa_report.json`, threshold receipts |
| F | run receipt capturing inputs/tools/hashes/policy decisions | receipt generators + schema validators | `run_receipt.json`, `prov.jsonld` |
| G | release manifest references artifacts + digests | `promote/` + release tooling | `release_manifest.json`, SBOM refs |

[Back to top](#)

---

## Work package alignment

- **CONFIRMED:** KFM’s “trust foundation” sequencing expects:
  - **WP‑01:** spec hashing + controlled vocab validation
  - **WP‑02:** catalog validators + link checker
  - **WP‑03:** policy pack + fixture tests
  - **WP‑04:** evidence resolver service (runtime) + integration tests

> **PROPOSED:** `tools/` should fully cover WP‑01/WP‑02 and provide CI harness support for WP‑03.

| Work package | Primary output | Where `tools/` fits |
|---|---|---|
| WP‑01 | `spec_hash` library + CLI + golden tests | `tools/hash/` (and/or `tools/promote/` helpers) |
| WP‑02 | DCAT/STAC/PROV validators + linkcheck | `tools/validators/` + `tools/linkcheck/` |
| WP‑03 | OPA bundle + fixtures + conftest tests | `policy/` owns rules; `tools/policy/` may add guard scripts |
| WP‑04 | Evidence resolver route + bundle schema | Service code elsewhere; tools provide fixtures + contract tests |

[Back to top](#)

---

## Policy toolchain compatibility

- **PROPOSED:** Add a **policy v1 guard lane** so policy upgrades do not silently break CI or runtime.

### Rego v1 / OPA 1.0 upgrade guard (pattern)

```bash
# Run locally before changing policy semantics
opa check --v0-v1 --strict ./policy

# Auto-rewrite where safe; review diffs
opa fmt --write --v0-v1 ./policy
```

### CI guard (pattern)

- **PROPOSED:** Add a CI job that fails-closed on any v1 incompatibility:
  - `opa check --v0-v1 --strict ./policy`
  - and/or `opa check --rego-v1 --strict ./policy` depending on the pinned OPA version.

[Back to top](#)

---

## Adding a tool

### Definition of Done (minimum)

- **PROPOSED:** A new tool is not “real” until it is:
  - documented (README with inputs/outputs + exit codes),
  - tested (fixtures + unit tests; property tests if appropriate),
  - wired into CI as a required check if it enforces Promotion Contract gates,
  - deterministic (stable ordering; pinned deps; reproducible reports).

### Template (recommended)

```text
tools/<tool-name>/
├── README.md
├── src/                      (optional)
├── tests/                    (fixtures + unit tests)
└── package.json / pyproject  (if needed)
```

[Back to top](#)

---

## Safety and sensitivity

- **CONFIRMED:** Sensitive location leakage is treated as a high-impact risk; mitigations include restricted precise datasets + generalized public derivatives, redaction tests, and default-deny controls.
- **CONFIRMED:** Licensing/rights are promotion gates; “online availability” does not imply reuse permission.
- **PROPOSED:** Any tool that reads geometry or location-like fields MUST support:
  - redaction/generalization modes (or verification that upstream redaction is applied),
  - “safe projection” outputs (drop disallowed fields),
  - fixtures proving leakage checks (centroid jittering, clustering, attribute masking, temporal coarsening).

### Safe-by-default checks (recommended)

- **PROPOSED:** Add a `tools/validators/safety/` tool that verifies:
  - policy_label consistency,
  - required redaction receipts exist when policy_label != public,
  - “no precise coordinates” rules for public layers (if applicable),
  - no PII-like columns in public-facing schemas.

[Back to top](#)

---

## Unknowns and verification

- **UNKNOWN:** Which `tools/` checks are required to merge in your CI.
  - **Minimum verification steps:**
    1. `ls .github/workflows`
    2. `rg -n "tools/" .github/workflows -S`
    3. Identify required status checks in branch protection settings (if enabled).

- **UNKNOWN:** The exact validator flags and report shapes.
  - **Minimum verification steps:** run each tool with `--help`, then capture one “pass” and one “fail” report as fixtures under `tools/**/tests/fixtures/`.

### Verification checklist (copy/paste)

- [ ] Captured repo commit hash (`git rev-parse HEAD`)
- [ ] Captured `tools/` tree (`tree -L 3 tools`)
- [ ] Verified which validators/link checks exist and their CLI flags
- [ ] Confirmed CI required checks that block merge
- [ ] Added/updated fixtures for one failing and one passing catalog case
- [ ] Confirmed tools are deterministic (same inputs → same report bytes)

[Back to top](#)

---

## FAQ

### Why do tools “fail closed”?

- **CONFIRMED:** KFM treats promotion/publishing as a governed act; failing validation must block promotion so PUBLISHED surfaces never serve unverifiable or unlicensed artifacts.

### Why so many JSON reports?

- **PROPOSED:** Reports bridge tooling and policy: CI can upload them, OPA can evaluate them, and stewards can review them without rerunning local commands.

### Can tools auto-fix catalogs?

- **PROPOSED:** Yes, but keep “fix” functionality behind `--write`, and keep CI in read-only validation mode so merges are explainable and deterministic.

[Back to top](#)

---

## Source pointers

> **CONFIRMED:** KFM’s tooling requirements are derived from the project’s governance + delivery plan, plus policy/citation invariants and promotion gate patterns.

- **[SRC-ToolingPipeline]** “Tooling the KFM pipeline” (work packages, invariants, promotion gates).
- **[SRC-Prime]** “KFM Prime Document” (repo inventory mentioning `tools/validators/*`).
- **[SRC-Snapshots]** “KFM Source Snapshots (vNext)” (policy parity, catalog triplet minimums, rights + sensitivity rules).
- **[SRC-NewIdeas-PolicyV1]** “New Ideas 2-17-26” (OPA/Rego v1 guard recommendations).
- **[SRC-NewIdeas-Receipts]** “New Ideas 2-26-26” (receipts/spec_hash + CI gating sketches).
