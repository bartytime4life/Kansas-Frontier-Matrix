<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/f9897f92-8f95-4e15-a53f-c4aee0cb0fed
title: tools/ — Utility scripts, validators, and DevOps helpers
type: standard
version: v1
status: draft
owners: KFM Platform (TODO)
created: 2026-02-26
updated: 2026-02-28
policy_label: public
related:
  - ../contracts/
  - ../configs/
  - ../policy/
  - ../scripts/
  - ../tests/
  - docs/MASTER_GUIDE_v13.md
  - docs/standards/KFM_DCAT_PROFILE.md
  - docs/standards/KFM_STAC_PROFILE.md
  - docs/standards/KFM_PROV_PROFILE.md
tags: [kfm, tools, ci, validators, promotion-contract, evidence-first, trust-membrane, spec-hash]
notes:
  - tools/ contains maintainers’ tooling used by CI and operators to enforce the Promotion Contract (fail-closed gates).
  - Keep tools deterministic, policy-safe, and fixture-driven. Update the tool registry when adding/renaming/retiring tools.
  - This doc describes a target posture. Mark repo-specific facts as TODO until verified in-repo.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# `tools/` — Utility scripts, validators, and DevOps helpers

**Purpose:** Keep KFM *buildable, reversible, and evidence-backed* by running **fail-closed** checks in CI and locally (catalog validation, link checking, spec-hash drift detection, and other guardrails).

![Status](https://img.shields.io/badge/status-draft-lightgrey)
![Scope](https://img.shields.io/badge/scope-repo%20tooling-lightgrey)
![Governance](https://img.shields.io/badge/governance-fail--closed-critical)
![Promotion](https://img.shields.io/badge/promotion%20contract-enforced-critical)
![Trust membrane](https://img.shields.io/badge/trust%20membrane-preserved-important)

> [!IMPORTANT]
> `tools/` is part of KFM’s **trust membrane**. If a tool can be bypassed, is non-deterministic, or leaks restricted details in logs, it is a governance risk.

---

## Quick navigation

- [What lives here](#what-lives-here)
- [Non-negotiable invariants](#non-negotiable-invariants)
- [Directory layout](#directory-layout)
- [How tools fit the promotion flow](#how-tools-fit-the-promotion-flow)
- [Quick start](#quick-start)
- [Tool registry and inventory](#tool-registry-and-inventory)
- [Conventions](#conventions)
- [Adding a new tool](#adding-a-new-tool)
- [Troubleshooting](#troubleshooting)
- [Appendix: recommended CLI contract](#appendix-recommended-cli-contract)

---

## What lives here

This folder is reserved for **utility scripts, validators, and DevOps tooling** that:

- run in CI as **merge gates** or **promotion gates**, and/or
- are used by maintainers/operators during ingest/publish/release workflows.

### ✅ Acceptable contents

| Category | Examples | Typical outcome |
|---|---|---|
| Catalog validators | DCAT/STAC/PROV schema/profile validation | CI blocks invalid metadata |
| Cross-link checkers | Ensure DCAT ↔ STAC ↔ PROV ↔ receipts ↔ artifacts resolve | CI blocks broken evidence paths |
| Spec-hash & drift checks | Detect contract drift / canonicalization regressions | CI blocks “silent” version drift |
| Policy-safe lint checks | Disallow direct-store access, forbid secrets-in-repo patterns | CI blocks trust-membrane bypass |
| Release helpers (optional) | Build SBOMs, assemble release manifests, verify signatures | Reproducible release outputs |

### ❌ Not allowed in `tools/`

- One-off experiments or notebooks → put them in a dedicated experiments area (e.g., `mcp/`) or a PR sandbox.
- Production runtime code → belongs in `src/` / services, behind contracts/interfaces.
- Data pipelines → belong in pipeline modules/runners; tools can validate pipeline outputs.
- Raw/processed datasets → belong in `data/` truth-path zones.
- Secrets, tokens, credentials, kubeconfigs, or `.env` with real values → never commit.

> [!NOTE]
> Tools **prefer read-only validation**. If a tool *must write outputs*, it must:
> 1) write into the correct truth-path zone (usually `data/work/…`),  
> 2) emit a receipt and checksums, and  
> 3) never mutate canonical artifacts in place.

[Back to top](#top)

---

## Non-negotiable invariants

Tools exist to *enforce* these invariants (not merely document them):

1. **Fail closed**  
   If a tool cannot prove a requirement, it must exit non-zero and block the gate.

2. **Truth path discipline**  
   Tools must never “fix” canonical artifacts in place. Canonical artifacts are versioned and immutable by digest.

3. **Trust membrane preserved**  
   Tools must not introduce or normalize bypass patterns (e.g., direct DB/object-store reads from UI code).

4. **Evidence-first / cite-or-abstain support**  
   Tools must help ensure that:
   - EvidenceRefs resolve to EvidenceBundles (or the system abstains/denies),
   - catalogs and receipts are present and cross-linked.

5. **Canonical vs rebuildable**  
   Tools may rebuild projections, but projections are never treated as canonical truth. Tools must validate canonical sources.

6. **Deterministic identity and hashing**  
   Spec hashing must be canonicalized and stable. Any drift is a blocking failure unless explicitly versioned.

7. **Policy-safe output**  
   Tools must not leak restricted details (including “restricted existence”) via logs, timing hints, or error messages.

[Back to top](#top)

---

## Directory layout

> [!IMPORTANT]
> This layout is a recommended baseline. If your repo differs, update this README and keep the **Tool registry** accurate.

```text
tools/                                                # Tooling entrypoint (validators + checks + CI helpers)
├── README.md                                         # This file (how to run + add new tools)
│
├── registry/                                         # Machine-readable registry + schemas + fixtures (small)
│   ├── tools.v1.json                                 # Canonical tool registry: owners, commands, gates, inputs, outputs
│   ├── schemas/                                      # Schemas for registry + common tool I/O (optional but recommended)
│   │   ├── tools_registry.v1.schema.json             # Schema for tools.v1.json
│   │   ├── tool_result.v1.schema.json                # Standard machine output envelope (--json)
│   │   ├── finding.v1.schema.json                    # Standard finding (code, severity, location, message)
│   │   └── exit_codes.v1.schema.json                 # Allowed exit codes and meanings
│   └── fixtures/                                     # Valid/invalid registry examples for CI schema validation
│       ├── valid/
│       │   ├── tools.v1.minimal.json
│       │   ├── tools.v1.full.json
│       │   └── README.md                             # How fixtures are used in CI
│       └── invalid/
│           ├── tools.v1.missing_owner.json
│           ├── tools.v1.bad_gate.json
│           ├── tools.v1.bad_paths.json
│           └── README.md
│
├── validators/                                       # Metadata + schema validators (fail-closed; read-only)
│   ├── README.md                                     # What validators check + expected inputs
│   ├── validate_dcat.{sh,py,ts,js}                   # Validate DCAT against KFM profile (+ required fields)
│   ├── validate_stac.{sh,py,ts,js}                   # Validate STAC Collections/Items/Assets (+ KFM constraints)
│   ├── validate_prov.{sh,py,ts,js}                   # Validate PROV bundles (+ required links/agents/activities)
│   ├── validate_receipts.{sh,py,ts,js}               # Validate run_receipt + promotion_manifest schemas
│   ├── validate_catalog_bundle.{sh,py,ts,js}         # One-shot: validate DCAT+STAC+PROV+receipts as a set
│   ├── validate_contract_versions.{sh,py,ts,js}      # Ensure artifacts declare supported schema/profile versions
│   └── fixtures/                                     # Tiny valid/invalid examples (synthetic/sanitized)
│       ├── dcat/
│       │   ├── valid/
│       │   │   ├── minimal_dcat.jsonld
│       │   │   └── FIXTURE_NOTES.md
│       │   └── invalid/
│       │       ├── missing_license.jsonld
│       │       ├── bad_distribution_href.jsonld
│       │       └── FIXTURE_NOTES.md
│       ├── stac/
│       │   ├── valid/
│       │   │   ├── collection.json
│       │   │   ├── item.json
│       │   │   └── FIXTURE_NOTES.md
│       │   └── invalid/
│       │       ├── missing_datetime.json
│       │       ├── invalid_bbox.json
│       │       └── FIXTURE_NOTES.md
│       ├── prov/
│       │   ├── valid/
│       │   │   ├── prov.jsonld
│       │   │   └── FIXTURE_NOTES.md
│       │   └── invalid/
│       │       ├── missing_activity.jsonld
│       │       ├── orphan_entity.jsonld
│       │       └── FIXTURE_NOTES.md
│       └── receipts/
│           ├── valid/
│           │   ├── run_receipt.json
│           │   ├── promotion_manifest.json
│           │   └── FIXTURE_NOTES.md
│           └── invalid/
│               ├── missing_checksums.json
│               ├── missing_policy_fields.json
│               └── FIXTURE_NOTES.md
│
├── linkcheck/                                        # Cross-link integrity checks (no broken refs)
│   ├── README.md                                     # Cross-link rules + what is considered "required"
│   ├── catalog_triplet_linkcheck.{sh,py,ts,js}       # DCAT ↔ STAC ↔ PROV required cross-links
│   ├── evidence_ref_linkcheck.{sh,py,ts,js}          # EvidenceRef resolvability expectations (format + target exists)
│   ├── receipt_artifact_linkcheck.{sh,py,ts,js}      # Receipts ↔ checksums ↔ artifacts paths resolve
│   ├── no_restricted_existence_leaks.{sh,py,ts,js}   # Ensure error envelopes do not leak restricted existence (static)
│   └── fixtures/
│       ├── valid/
│       │   ├── triplet_ok/                           # Minimal DCAT+STAC+PROV bundle with consistent links
│       │   │   ├── dcat.jsonld
│       │   │   ├── stac/collection.json
│       │   │   ├── stac/items/item-001.json
│       │   │   ├── prov/prov.jsonld
│       │   │   └── receipts/run_receipt.json
│       │   └── evidence_refs_ok.json
│       └── invalid/
│           ├── triplet_broken_link/
│           │   ├── dcat.jsonld                       # points to missing stac item
│           │   └── stac/collection.json
│           ├── evidence_ref_bad_scheme.json
│           └── receipt_missing_artifact.json
│
├── hash/                                             # Spec-hash helpers + drift checks (determinism guardrails)
│   ├── README.md                                     # Canonicalization rules + hashing invariants
│   ├── compute_spec_hash.{sh,py,ts,js}               # Deterministic hash computation (canonical JSON rules)
│   ├── canonicalize_json.{sh,py,ts,js}               # Canonical JSON serializer (stable ordering/whitespace)
│   ├── check_spec_hash_drift.{sh,py,ts,js}           # Recompute + compare; fail on drift
│   ├── check_hash_inputs.{sh,py,ts,js}               # Fail if spec includes non-deterministic fields (timestamps, etc.)
│   └── fixtures/                                     # Golden vectors (inputs → expected digests)
│       ├── vectors.v1.json                            # canonical test vector list
│       ├── inputs/
│       │   ├── dataset_spec_minimal.json
│       │   ├── dataset_spec_with_ordering_noise.json  # should canonicalize to same digest as minimal
│       │   └── dataset_spec_invalid_nondeterminism.json
│       └── expected/
│           ├── vectors.v1.expected.json               # expected sha256 outputs
│           └── FIXTURE_NOTES.md
│
├── lint/                                             # Static guardrails (trust membrane + hygiene)
│   ├── README.md                                     # What lint checks exist + why
│   ├── check_no_secrets.{sh,py,ts,js}                # Secret scanning helpers (if not handled elsewhere)
│   ├── check_no_direct_store_access.{sh,py,ts,js}    # Block direct DB/object-store/index clients in forbidden layers
│   ├── check_policy_safe_errors.{sh,py,ts,js}        # Enforce safe error envelope conventions
│   ├── check_license_headers.{sh,py,ts,js}           # Optional: enforce license header posture in tooling/code
│   └── fixtures/
│       ├── valid/
│       └── invalid/
│
├── release/                                          # Optional: release tooling (must be deterministic)
│   ├── README.md                                     # How releases are assembled + verified
│   ├── build_sbom.{sh,py,ts,js}                      # SBOM build (if used)
│   ├── build_release_manifest.{sh,py,ts,js}          # Assemble release metadata + digests
│   ├── verify_release_artifacts.{sh,py,ts,js}        # Verify digests/signatures/attestations (if used)
│   ├── sign_release.{sh,py,ts,js}                    # Optional: signing wrapper (NEVER stores keys in repo)
│   └── fixtures/
│       ├── valid/
│       └── invalid/
│
├── _shared/                                          # Shared helper libs (small; minimal side effects)
│   ├── README.md                                     # Shared helpers contract (keep pure where possible)
│   ├── fs.{py,ts,js}                                 # Safe file IO helpers (path traversal defense)
│   ├── json.{py,ts,js}                               # Canonical JSON + strict parsing helpers
│   ├── log.{py,ts,js}                                # Structured logging helpers (policy-safe)
│   ├── errors.{py,ts,js}                             # Standardized error/finding helpers (codes, severities)
│   ├── exit_codes.{py,ts,js}                         # Exit code constants + mapping
│   └── time.{py,ts,js}                               # Time helpers (avoid non-determinism in hashes)
│
└── fixtures/                                         # Shared fixtures (synthetic/sanitized; tiny; documented)
    ├── public/
    │   ├── FIXTURE_NOTES.md                          # license + sensitivity + intended use
    │   ├── minimal_catalog_bundle/                   # a tiny end-to-end bundle used across validators/linkcheck
    │   │   ├── dcat.jsonld
    │   │   ├── stac/collection.json
    │   │   ├── stac/items/item-001.json
    │   │   ├── prov/prov.jsonld
    │   │   └── receipts/run_receipt.json
    │   └── minimal_openapi/                          # optional: contract tool fixtures
    │       └── openapi.v1.yaml
    └── restricted_sanitized/
        ├── FIXTURE_NOTES.md                          # describes sanitization (no precise coords/identifiers)
        ├── generalized_geometry_bundle/              # coarse geometry used to test “no leakage” behavior
        │   ├── dcat.jsonld
        │   └── stac/items/item-001.json
        └── policy_safe_error_cases/
            ├── forbidden.json                        # safe error envelope example
            └── not_found.json                        # indistinguishable or policy-safe variant
```

[Back to top](#top)

---

## How tools fit the promotion flow

```mermaid
flowchart LR
  PR[Pull request] --> CI[CI gates]
  CI --> V[tools/validators]
  V --> L[tools/linkcheck]
  L --> H[tools/hash]
  H --> P[policy tests + contracts/tests]
  P --> OK[Merge allowed]

  V --> BLOCK[Fail closed]
  L --> BLOCK
  H --> BLOCK
  P --> BLOCK
```

> [!WARNING]
> Tools should not “paper over” missing artifacts. If a catalog or receipt is missing, the correct output is a **blocking failure** (deny-by-default posture).

[Back to top](#top)

---

## Quick start

> [!NOTE]
> Commands here are examples. Wire the repo’s real entry points (Makefile/Taskfile/npm scripts) and update this section accordingly.

### Run the core gates locally (example)

```bash
# From repo root (replace with your repo's actual bootstrap)
make bootstrap

# Validate catalogs/provenance/receipts
make tools-validate

# Cross-link check (DCAT ↔ STAC ↔ PROV ↔ receipts ↔ artifacts)
make tools-linkcheck

# Spec-hash drift checks
make tools-hash-check

# Optional: lint guardrails (trust membrane / secrets)
make tools-lint
```

### Minimal “direct invocation” pattern (example)

```bash
# Validators
./tools/validators/validate_dcat.sh
./tools/validators/validate_stac.sh
./tools/validators/validate_prov.sh

# Linkcheck
./tools/linkcheck/catalog_triplet_linkcheck.sh

# Hash/drift
./tools/hash/check_spec_hash_drift.sh
```

[Back to top](#top)

---

## Tool registry and inventory

KFM prefers a **machine-readable registry** so CI can run tools consistently and owners can be routed via CODEOWNERS.

### `tools/registry/tools.v1.json` (recommended fields)

At minimum:
- tool id + path
- owner
- gate type (merge gate vs promotion gate)
- inputs/outputs (read-only vs writes)
- required fixtures/tests
- timeout expectations
- policy-safe logging flag

Example shape (illustrative):

```json
{
  "version": "v1",
  "tools": [
    {
      "tool_id": "kfm.tools.validate_dcat",
      "path": "tools/validators/validate_dcat.sh",
      "owner": "KFM Platform",
      "gate": "merge",
      "reads": ["data/catalog/**"],
      "writes": [],
      "requires_fixtures": true,
      "timeout_seconds": 120,
      "policy_safe_logs": true
    }
  ]
}
```

### Tool inventory (human-readable)

Keep this table up-to-date (it should match the registry):

| Tool | Type | What it checks | Gate | Owner |
|---|---|---|---|---|
| `tools/validators/validate_dcat.*` | validator | DCAT conforms to KFM profile; required rights/license fields present | merge/promotion | TODO |
| `tools/validators/validate_stac.*` | validator | STAC Items/Collections/Assets conform to KFM profile | merge/promotion | TODO |
| `tools/validators/validate_prov.*` | validator | PROV bundle shape + required lineage links present | merge/promotion | TODO |
| `tools/linkcheck/catalog_triplet_linkcheck.*` | linkcheck | DCAT ↔ STAC ↔ PROV cross-links resolve deterministically | merge/promotion | TODO |
| `tools/hash/check_spec_hash_drift.*` | drift check | Deterministic spec-hash stability; blocks unintended drift | merge | TODO |
| `tools/lint/check_no_direct_store_access.*` | lint | Trust membrane guardrail: forbid forbidden deps/egress patterns | merge | TODO |

[Back to top](#top)

---

## Conventions

### Deterministic and auditable

- **Deterministic**: same inputs ⇒ same pass/fail decision.
- **Fixture-driven**: every rule has fixtures (valid + invalid).
- **Offline-first**: avoid network calls. If unavoidable, pin versions and record what was accessed.

### Safe by default

- Treat files as untrusted input (strict parsing, safe path handling).
- Never print secrets or restricted data.
- Prefer **policy-safe error outputs**:
  - do not distinguish “not found” vs “forbidden” in ways that leak restricted existence
  - keep error messages actionable for maintainers but safe for CI logs

### Read-only posture (preferred)

- Validators/linkcheck/hash tools should not mutate artifacts.
- If a tool must write outputs:
  - write into the correct truth-path zone (usually `data/work/…`)
  - emit `checksums.json` and a run receipt
  - never overwrite canonical artifacts in place

[Back to top](#top)

---

## Adding a new tool

Every new tool must ship with:

- [ ] A clear location: `tools/<area>/<tool_name>.(sh|py|js|ts|go)`
- [ ] A help/usage entry point (`--help` or header comment)
- [ ] Deterministic behavior (same inputs ⇒ same decision)
- [ ] Fixtures: **known-good** + **known-bad**
- [ ] Tests (unit tests minimum; integration tests if it is a gate)
- [ ] Entry in `tools/registry/tools.v1.json`
- [ ] Entry in the [Tool inventory](#tool-registry-and-inventory)
- [ ] CI wiring (if the tool is a gate)
- [ ] Policy-safe logging (no restricted details; no secrets)

> [!TIP]
> If the tool enforces a Promotion Contract gate, treat it like a contract change: update fixtures, schema validators, and documentation together.

[Back to top](#top)

---

## Troubleshooting

### “Validator passes locally but fails in CI”
- Confirm CI and local are using the same tool version/runtime.
- Confirm fixtures are checked in and paths match CI working directory.
- Confirm the tool is deterministic (no timestamps or environment-dependent ordering).

### “Linkcheck failures”
Common causes:
- DCAT distribution points to missing STAC Item
- STAC asset href changed but catalogs not updated
- PROV references missing run receipt or entity id

Fix the *metadata* and receipts—do not weaken linkcheck rules “to get CI green”.

### “Spec-hash drift failures”
- If drift is expected (intentional contract change): bump the relevant contract/version and update golden vectors.
- If drift is not expected: verify canonicalization rules and field normalization.

### “Tool logs might leak restricted details”
- Treat as a P0 governance bug.
- Redact/aggregate outputs, and enforce policy-safe error shaping.

[Back to top](#top)

---

## Appendix: recommended CLI contract

Tools should follow a consistent CLI contract so CI can interpret results reliably.

### Flags (recommended)
- `--help` prints usage and exits `0`
- `--json` prints machine-readable output (for CI annotations)
- `--input <path>` optional explicit input root
- `--strict` fails on warnings (default for CI)

### Exit codes (recommended)
- `0` = pass
- `1` = validation failed (expected gate failure)
- `2` = tool error (misconfiguration, missing dependency, unexpected exception)

### Output contract (recommended)
- Progress logs → stderr
- Machine output → stdout (when `--json`)
- Never print secrets or restricted details

---

<a href="#top">Back to top</a>
