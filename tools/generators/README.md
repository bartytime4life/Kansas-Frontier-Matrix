<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/bd63e4ac-ca4a-463b-9fce-ba5bc602c5c0
title: tools/generators — governed artifact generators
type: standard
version: v1
status: draft
owners: TBD
created: 2026-02-26
updated: 2026-02-26
policy_label: public
related:
  - kfm://doc/TBD
tags: [kfm, generators, governance, provenance, catalogs]
notes:
  - Directory contract for deterministic, fail-closed generators that emit promotion-grade artifacts.
[/KFM_META_BLOCK_V2] -->

# tools/generators

Deterministic, **fail-closed** generators for Kansas Frontier Matrix (KFM) *promotion-grade* artifacts:  
**catalog triplet (DCAT + STAC + PROV)**, **run receipts + checksums**, **promotion manifests**, and **evidence bundles**.

![KFM](https://img.shields.io/badge/KFM-governed-blue)
![Status](https://img.shields.io/badge/status-draft-yellow)
![CI](https://img.shields.io/badge/ci-TODO-lightgrey)
![License](https://img.shields.io/badge/license-TODO-lightgrey)

> **NOTE**
> This README defines *directory-level requirements* (what generators **must** do).  
> It does **not** assert which generators already exist in the repo.

## Navigation

- [What this directory is](#what-this-directory-is)
- [What belongs here](#what-belongs-here)
- [What must not go here](#what-must-not-go-here)
- [Generator contract](#generator-contract)
- [How this maps to KFM promotion gates](#how-this-maps-to-kfm-promotion-gates)
- [Proposed structure](#proposed-structure)
- [Generator registry](#generator-registry)
- [How to run](#how-to-run)
- [Add a new generator](#add-a-new-generator)
- [Testing and CI gates](#testing-and-ci-gates)
- [Troubleshooting](#troubleshooting)

---

## What this directory is

Generators are **build tools** that turn *canonical inputs* (dataset specs, pipeline params, policy decisions, and produced artifacts) into **governed, evidence-bearing outputs** that KFM can safely publish through API/UI surfaces.

In KFM terms, generators are responsible for creating/validating the artifacts that make the **catalog + provenance surfaces** and the **promotion contract** enforceable.

### Typical inputs

- Dataset spec (identity, semantics, licensing, sensitivity)
- Pipeline parameters (canonicalized for hashing)
- Produced artifacts (raw/work/processed)
- Policy decisions (labels + obligations like redaction/generalization)
- Environment identity (container digest, git commit)

### Typical outputs

- **Catalog triplet**: DCAT (dataset-level), STAC (asset-level), PROV (lineage)
- **Run receipt** for each producing run (inputs/outputs/environment/validation/policy)
- **Checksums** for every artifact (raw + processed)
- **Promotion manifest** (the “receipt bundle” used to promote + publish)
- **Evidence bundle** payloads (human card + machine metadata + digests + audit refs)

[Back to top](#tools-generators)

---

## What belongs here

✅ **Accepted inputs/artifacts in this directory**

- Generator code (CLI + libraries)
- JSON Schemas / profiles for generator outputs (DCAT/STAC/PROV, receipts, manifests)
- Small fixtures for tests (tiny datasets, mock catalogs, policy fixtures)
- Determinism tooling (canonical JSON/YAML, stable sorting, hashing utilities)
- Link-checkers + validators for cross-link rules (DCAT↔STAC↔PROV)

## What must not go here

🚫 **Explicit exclusions**

- Runtime services (APIs, UI apps, workers) — keep those in their own runtime modules
- One-off notebooks or ad-hoc scripts that are not reproducible/tested
- Secrets, credentials, tokens, or private keys (even for local dev)
- Bulk data dumps / large binaries (use the truth-path zones, not git)
- Direct “publish” actions that bypass policy or promotion gates

> **WARNING**
> Generators are part of the trust membrane: they must never create an output that would let
> downstream runtime surfaces serve ungoverned or untraceable data.

[Back to top](#tools-generators)

---

## Generator contract

These requirements are written to be testable. If a generator cannot meet them, it should **fail closed**.

### Determinism and identity

- A generator **MUST** be deterministic: same inputs → same outputs → same digests.
- A generator **MUST** derive/record a stable `spec_hash` (or equivalent) for DatasetVersion identity.
- Outputs **SHOULD** be digest-addressed (e.g., `sha256:`) so they can be referenced immutably.

### Fail-closed posture

- If **licensing is unclear**, the generator **MUST** refuse to produce promotion-grade outputs.
- If **sensitivity is unclear** or redaction requirements are missing, the generator **MUST** refuse.
- If **catalog validation** or **cross-link checks** fail, the generator **MUST** refuse.

### Receipts, checksums, and provenance

- Every producing run **MUST** emit a **run receipt** enumerating:
  - inputs + output URIs
  - digests for each
  - environment identity (container digest, git commit, params digest)
  - validation status/report digest
  - policy decision reference
- Every artifact referenced in catalogs **MUST** have a checksum recorded and resolvable.
- PROV **MUST** link activities, entities, and agents so lineage navigation is deterministic.

### Policy awareness

- Generators **MUST** carry through `policy_label` and any obligations (redaction/generalization), and
  record them in provenance outputs (and/or linked policy decision objects).

### Usability

- A generator **MUST** expose a CLI with:
  - `--help`
  - `--dry-run` or `--plan`
  - `--validate` (schema + links)
- A generator **SHOULD** support `--json` output for machine consumption.

[Back to top](#tools-generators)

---

## How this maps to KFM promotion gates

KFM promotion is **blocked** unless minimum gates pass. Generators are expected to produce the
artifacts that make these gates testable.

| Gate | Fail-closed check (summary) | Artifacts generators must produce/validate |
|---|---|---|
| A. Identity & versioning | Stable dataset ID + immutable DatasetVersion ID derived from stable hash | spec hash + version id; promotion manifest stub |
| B. Licensing & rights | Explicit license + attribution; unclear → quarantine | DCAT license/rights, attribution text |
| C. Sensitivity + redaction | policy label assigned; redaction/generalization plan recorded | policy decision ref; PROV links to obligations |
| D. Catalog triplet | DCAT + STAC + PROV exist, validate, cross-link | profiles + link-checks + resolvable references |
| E. Run receipt + checksums | receipts exist; inputs/outputs have digests; env recorded | run receipts; digests for all artifacts |
| F. Policy + contract tests | OPA tests pass; EvidenceRef resolves in CI; API schemas valid | policy fixtures; resolver smoke; schema validation |
| G. Recommended | SBOM/provenance, perf + accessibility smokes | (optional) attestations; smoke-test harness |

> **TIP**
> Treat each gate as a **unit-testable contract**: if we can’t test it automatically, we can’t trust it.

[Back to top](#tools-generators)

---

## Proposed structure

This directory’s exact contents are repo-dependent. The structure below is a **proposed** baseline
that keeps generators discoverable and testable.

```text
tools/generators/                                      # Artifact generators (deterministic, policy-aware, registry-driven)
├── README.md                                          # (this file)
├── registry.yaml                                      # Generator registry (recommended: name, inputs, outputs, policy_label, version)
├── _lib/                                              # Shared helpers (canonicalization, hashing, IO, fs safety)
├── catalog_triplet/                                   # DCAT/STAC/PROV generation + validation (profile-aware)
│   ├── README.md                                       # Usage, inputs/outputs, examples, and validation gates
│   ├── cli                                             # Entrypoint (recommended)
│   ├── src/                                            # Implementation
│   └── tests/                                          # Unit/schema tests for generator determinism + correctness
├── run_receipt/                                       # Run receipts + audit ledger helpers (run_record/run_manifest/validation_report)
│   └── ...                                             # Add cli/src/tests as needed (keep structure consistent)
├── promotion_manifest/                                # Promotion bundle / release manifest generation (promotion contract emitter)
│   └── ...                                             # Add cli/src/tests as needed (versioned, backward compatible)
└── evidence_bundle/                                   # EvidenceBundle materialization helpers (digest-addressed bundles)
    └── ...                                             # Add cli/src/tests as needed (strict IO + integrity checks)
```

[Back to top](#tools-generators)

---

## Generator registry

Maintain a single registry so CI and humans can discover what exists and what it emits.

**Recommended** fields (expand as needed):

```yaml
# tools/generators/registry.yaml
generators:
  - id: catalog_triplet
    description: Generate + validate DCAT/STAC/PROV for a dataset version
    entrypoint: tools/generators/catalog_triplet/cli
    inputs:
      - dataset_spec
      - processed_artifacts
      - policy_decision
    outputs:
      - dcat
      - stac
      - prov
    gates_supported: [D, C, B]
    owners: [TBD]
```

[Back to top](#tools-generators)

---

## How to run

Because repo entrypoints vary, we standardize the **behavior**, not the language runtime.

### Expected CLI behavior (required)

```bash
# from repo root
tools/generators/<generator_id>/cli --help
tools/generators/<generator_id>/cli --dry-run --dataset-version <id> --out <dir>
tools/generators/<generator_id>/cli --validate --dataset-version <id> --out <dir>
```

### Minimal exit codes (recommended)

- `0` success (artifacts generated and validated)
- `2` validation failure (schema/links/policy)
- `3` missing/unclear rights or sensitivity (quarantine)
- `4` unexpected error (bug)

[Back to top](#tools-generators)

---

## Add a new generator

1. Create `tools/generators/<generator_id>/` with:
   - `README.md` (what it generates, inputs/outputs, examples)
   - `cli` entrypoint
   - `tests/` (determinism + validation)
2. Register it in `tools/generators/registry.yaml`.
3. Add **fixtures** that cover:
   - at least one policy-allowed case
   - at least one policy-denied/quarantine case
4. Ensure outputs include:
   - digests/checksums
   - policy label + obligations
   - cross-links (if producing catalogs)
5. Add CI job(s) to run:
   - determinism test
   - schema/profile validation
   - link-checks

[Back to top](#tools-generators)

---

## Testing and CI gates

Minimum recommended test suite per generator:

- **Determinism test**: run twice → identical digests
- **Schema validation**: DCAT/STAC/PROV/receipt manifests validate against profiles
- **Cross-link validation**: every link between DCAT ↔ STAC ↔ PROV resolves
- **Policy tests**: fixtures-driven allow/deny + obligations
- **Evidence resolution smoke** (where applicable): at least one EvidenceRef resolves in CI

> **NOTE**
> KFM treats catalogs and provenance as contract surfaces — tests are not optional “nice to have”.

[Back to top](#tools-generators)

---

## Troubleshooting

### “Spec hash changed but nothing else did”

- Canonicalize your config before hashing:
  - stable key ordering
  - normalized whitespace
  - explicit defaults

### “Catalog validation passes, but links fail”

- Enforce a single link builder and a single base URI strategy.
- Validate relative vs absolute paths consistently.

### “Run receipt exists, but downstream can’t reproduce”

- Ensure the receipt includes:
  - container image digest
  - git commit SHA
  - params digest
  - validation report digest

### “Policy says allow, but data still leaks sensitive geometry”

- Treat redaction/generalization obligations as *part of generation*, not an afterthought.
- Ensure STAC geometry/bbox is policy-consistent (generalize if required).

[Back to top](#tools-generators)
