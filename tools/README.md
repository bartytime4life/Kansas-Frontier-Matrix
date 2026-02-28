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
- [Repository alignment](#repository-alignment)
- [Non-negotiable invariants](#non-negotiable-invariants)
- [Directory layout](#directory-layout)
- [How tools fit the promotion flow](#how-tools-fit-the-promotion-flow)
- [Promotion Contract gate mapping](#promotion-contract-gate-mapping)
- [Quick start](#quick-start)
- [Tool registry and inventory](#tool-registry-and-inventory)
- [Conventions](#conventions)
- [Adding a new tool](#adding-a-new-tool)
- [Verification checklist](#verification-checklist)
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

## Repository alignment

> [!IMPORTANT]
> **Do not claim repo-specific implementation details unless verified.** This README is allowed to describe the target posture, but any statement like “this script exists at X” must be marked TODO until confirmed.

### Confirmed (repo root)

- `tools/` exists as a top-level directory intended for **validators, link checkers, and CLI utilities**. *(Deeper tool paths still require in-repo verification.)*  

### TODO to verify in-repo

- Actual subfolders (`validators/`, `linkcheck/`, `hash/`, etc.) and the tool entrypoints actually used by CI.
- The precise CI wiring and which checks are *merge-blocking* vs *promotion-blocking*.

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
├── bin/                                              # OPTIONAL: unified entrypoints/wrappers for CI + devs
│   ├── kfm-tools.{sh,ps1,js,ts,py}                   # "one CLI": dispatch by tool_id from registry
│   ├── kfm-tools.env.example                         # Example env vars (NO real secrets)
│   └── README.md                                     # CLI contract + examples + exit codes
│
├── ci/                                               # CI glue that is NOT specific to a single tool
│   ├── README.md                                     # how CI calls tools; required status checks
│   ├── changed_files.{sh,py,ts,js}                   # compute "what changed" → scoped tool runs
│   ├── annotate_findings.{sh,py,ts,js}               # emit GitHub annotations from --json outputs
│   ├── upload_artifacts.{sh,py,ts,js}                # upload tool reports to CI artifacts
│   ├── gate_runner.{sh,py,ts,js}                     # runs "merge gate" / "promotion gate" sets
│   └── fixtures/
│       ├── valid/
│       │   └── changed_files.sample.json
│       └── invalid/
│           └── changed_files.bad_paths.json
│
├── registry/                                         # Machine-readable registry + schemas + fixtures (small)
│   ├── tools.v1.json                                 # Canonical tool registry: owners, commands, gates, inputs, outputs
│   ├── tools.v1.lock.json                            # OPTIONAL: resolved commands + digests/pins for determinism
│   ├── owners.v1.yml                                 # OPTIONAL: owner aliases → CODEOWNERS mapping inputs
│   ├── schemas/                                      # Schemas for registry + common tool I/O
│   │   ├── tools_registry.v1.schema.json             # Schema for tools.v1.json
│   │   ├── tool_result.v1.schema.json                # Standard machine output envelope (--json)
│   │   ├── finding.v1.schema.json                    # Standard finding (code, severity, location, message)
│   │   ├── exit_codes.v1.schema.json                 # Allowed exit codes and meanings
│   │   ├── io_manifest.v1.schema.json                # OPTIONAL: reads/writes contract (paths + zones)
│   │   ├── policy_safe_log.v1.schema.json            # OPTIONAL: enforce redaction/verbosity policy
│   │   └── README.md                                 # how schemas evolve + versioning rules
│   ├── scripts/                                      # Registry maintenance utilities
│   │   ├── validate_registry.{sh,py,ts,js}           # schema-validate tools.v1.json
│   │   ├── render_inventory.{sh,py,ts,js}            # generate README table from registry (no drift)
│   │   ├── diff_registry.{sh,py,ts,js}               # compare registry changes across branches
│   │   └── check_registry_drift.{sh,py,ts,js}        # blocks merge if table != registry (fail closed)
│   └── fixtures/                                     # Valid/invalid registry examples for CI schema validation
│       ├── valid/
│       │   ├── tools.v1.minimal.json
│       │   ├── tools.v1.full.json
│       │   └── README.md                             # How fixtures are used in CI
│       └── invalid/
│           ├── tools.v1.missing_owner.json
│           ├── tools.v1.bad_gate.json
│           ├── tools.v1.bad_paths.json
│           ├── tools.v1.bad_exit_codes.json
│           └── README.md
│
├── validators/                                       # Metadata + schema validators (fail-closed; read-only)
│   ├── README.md                                     # What validators check + expected inputs
│   ├── validate_dcat.{sh,py,ts,js}                   # Validate DCAT against KFM profile (+ required fields)
│   ├── validate_stac.{sh,py,ts,js}                   # Validate STAC Collections/Items/Assets (+ KFM constraints)
│   ├── validate_prov.{sh,py,ts,js}                   # Validate PROV bundles (+ required links/agents/activities)
│   ├── validate_receipts.{sh,py,ts,js}               # Validate run_receipt + run_manifest/promote_manifest schemas
│   ├── validate_pipeline_yaml.{sh,py,ts,js}          # OPTIONAL: validate pipeline.yaml contract if present
│   ├── validate_watchers_registry.{sh,py,ts,js}      # OPTIONAL: validate watchers registry schema/signature
│   ├── validate_catalog_bundle.{sh,py,ts,js}         # One-shot: validate DCAT+STAC+PROV+receipts as a set
│   ├── validate_contract_versions.{sh,py,ts,js}      # Ensure artifacts declare supported schema/profile versions
│   ├── profiles/                                     # OPTIONAL: local copies of KFM profiles/extensions (read-only)
│   │   ├── dcat/                                     # profile rules (SHACL/JSON schema/etc; repo-specific)
│   │   ├── stac/                                     # extension constraints (e.g., CARE extension)
│   │   └── prov/
│   └── fixtures/                                     # Tiny valid/invalid examples (synthetic/sanitized)
│       ├── dcat/
│       │   ├── valid/
│       │   │   ├── minimal_dcat.jsonld
│       │   │   ├── full_dcat.jsonld
│       │   │   └── FIXTURE_NOTES.md
│       │   └── invalid/
│       │       ├── missing_license.jsonld
│       │       ├── missing_publisher.jsonld
│       │       ├── bad_distribution_href.jsonld
│       │       └── FIXTURE_NOTES.md
│       ├── stac/
│       │   ├── valid/
│       │   │   ├── collection.json
│       │   │   ├── item.json
│       │   │   ├── item-assets.json
│       │   │   └── FIXTURE_NOTES.md
│       │   └── invalid/
│       │       ├── missing_datetime.json
│       │       ├── invalid_bbox.json
│       │       ├── missing_license.json
│       │       └── FIXTURE_NOTES.md
│       ├── prov/
│       │   ├── valid/
│       │   │   ├── prov.jsonld
│       │   │   └── FIXTURE_NOTES.md
│       │   └── invalid/
│       │       ├── missing_activity.jsonld
│       │       ├── missing_agent.jsonld
│       │       ├── orphan_entity.jsonld
│       │       └── FIXTURE_NOTES.md
│       ├── receipts/
│       │   ├── valid/
│       │   │   ├── run_receipt.json
│       │   │   ├── run_manifest.json
│       │   │   ├── promotion_manifest.json
│       │   │   └── FIXTURE_NOTES.md
│       │   └── invalid/
│       │       ├── missing_checksums.json
│       │       ├── missing_policy_fields.json
│       │       ├── nondeterministic_fields.json
│       │       └── FIXTURE_NOTES.md
│       ├── pipeline/
│       │   ├── valid/
│       │   │   ├── pipeline.yaml
│       │   │   └── FIXTURE_NOTES.md
│       │   └── invalid/
│       │       ├── missing_inputs.yaml
│       │       ├── bad_schedule.yaml
│       │       └── FIXTURE_NOTES.md
│       └── watchers/
│           ├── valid/
│           │   ├── registry.yml
│           │   └── FIXTURE_NOTES.md
│           └── invalid/
│               ├── missing_signature.yml
│               ├── bad_owner.yml
│               └── FIXTURE_NOTES.md
│
├── linkcheck/                                        # Cross-link integrity checks (no broken refs)
│   ├── README.md                                     # Cross-link rules + what is considered "required"
│   ├── catalog_triplet_linkcheck.{sh,py,ts,js}       # DCAT ↔ STAC ↔ PROV required cross-links
│   ├── evidence_ref_linkcheck.{sh,py,ts,js}          # EvidenceRef resolvability expectations (format + target exists)
│   ├── receipt_artifact_linkcheck.{sh,py,ts,js}      # Receipts ↔ checksums ↔ artifacts paths resolve
│   ├── citation_linkcheck.{sh,py,ts,js}              # OPTIONAL: story/docs citations resolve via EvidenceRefs
│   ├── docs_linkcheck.{sh,py,ts,js}                  # OPTIONAL: markdown link checker (repo-internal)
│   ├── no_restricted_existence_leaks.{sh,py,ts,js}   # Ensure errors don't distinguish forbidden vs missing
│   └── fixtures/
│       ├── valid/
│       │   ├── triplet_ok/
│       │   │   ├── dcat.jsonld
│       │   │   ├── stac/collection.json
│       │   │   ├── stac/items/item-001.json
│       │   │   ├── prov/prov.jsonld
│       │   │   └── receipts/run_receipt.json
│       │   ├── evidence_refs_ok.json
│       │   └── docs_ok/
│       │       ├── README.md
│       │       └── linked.md
│       └── invalid/
│           ├── triplet_broken_link/
│           │   ├── dcat.jsonld                       # points to missing stac item
│           │   └── stac/collection.json
│           ├── evidence_ref_bad_scheme.json
│           ├── receipt_missing_artifact.json
│           └── docs_broken_link/
│               ├── README.md                         # contains missing relative link
│               └── linked.md
│
├── hash/                                             # Spec-hash helpers + drift checks (determinism guardrails)
│   ├── README.md
│   ├── compute_spec_hash.{sh,py,ts,js}               # Deterministic spec hash computation
│   ├── canonicalize_json.{sh,py,ts,js}               # Canonical JSON serializer (stable ordering/whitespace)
│   ├── check_spec_hash_drift.{sh,py,ts,js}           # Recompute + compare; fail on drift
│   ├── check_hash_inputs.{sh,py,ts,js}               # Fail if spec includes non-deterministic fields
│   ├── compute_artifact_checksums.{sh,py,ts,js}      # OPTIONAL: create checksums.json for artifacts
│   ├── verify_artifact_checksums.{sh,py,ts,js}       # OPTIONAL: verify checksums.json matches artifacts
│   └── fixtures/
│       ├── vectors.v1.json                           # canonical test vector list
│       ├── inputs/
│       │   ├── dataset_spec_minimal.json
│       │   ├── dataset_spec_with_ordering_noise.json
│       │   ├── dataset_spec_invalid_nondeterminism.json
│       │   └── receipts_with_nondeterminism.json
│       └── expected/
│           ├── vectors.v1.expected.json              # expected sha256 outputs
│           ├── checksums.expected.json
│           └── FIXTURE_NOTES.md
│
├── lint/                                             # Static guardrails (trust membrane + hygiene)
│   ├── README.md
│   ├── check_no_secrets.{sh,py,ts,js}                # Secret scanning helpers (if not handled elsewhere)
│   ├── check_no_direct_store_access.{sh,py,ts,js}    # Forbid forbidden deps/egress patterns in forbidden layers
│   ├── check_policy_safe_errors.{sh,py,ts,js}        # Enforce safe error envelope conventions
│   ├── check_license_headers.{sh,py,ts,js}           # Optional: enforce license header posture
│   ├── check_large_files.{sh,py,ts,js}               # Optional: block huge binaries in repo
│   └── fixtures/
│       ├── valid/
│       │   ├── ok_codebase/
│       │   └── ok_errors/
│       └── invalid/
│           ├── contains_secret/
│           ├── direct_s3_access_in_ui/
│           ├── error_leaks_restricted_existence/
│           └── missing_license_headers/
│
├── policycheck/                                      # OPTIONAL: wrappers for policy-as-code gates
│   ├── README.md                                     # how CI runs OPA/Conftest + pinned versions
│   ├── opa_test.{sh,py,ts,js}                        # runs `opa test ...` consistently
│   ├── conftest_gate.{sh,py,ts,js}                   # runs conftest on schemas/receipts/watchers (deny-by-default)
│   ├── bundle_policy.{sh,py,ts,js}                   # optional: build/publish policy bundles
│   └── fixtures/
│       ├── allow/
│       ├── deny/
│       └── obligations/
│
├── packaging/                                        # OPTIONAL: deterministic artifact packaging + validation
│   ├── README.md                                     # formats supported + determinism rules
│   ├── validate_geoparquet.{sh,py,ts,js}
│   ├── validate_pmtiles.{sh,py,ts,js}
│   ├── validate_cog.{sh,py,ts,js}
│   ├── validate_zarr.{sh,py,ts,js}
│   └── fixtures/
│       ├── valid/
│       │   ├── geoparquet/
│       │   ├── pmtiles/
│       │   ├── cog/
│       │   └── zarr/
│       └── invalid/
│           ├── geoparquet/
│           ├── pmtiles/
│           ├── cog/
│           └── zarr/
│
├── oci/                                              # OPTIONAL: OCI distribution helpers (ORAS/Cosign plumbing)
│   ├── README.md                                     # push/pull by digest; referrers; “no tags as identity”
│   ├── publish_artifact.{sh,py,ts,js}                # publish blob/artifact by digest
│   ├── attach_referrers.{sh,py,ts,js}                # attach receipt/prov/sbom as referrers
│   ├── list_referrers.{sh,py,ts,js}                  # list referrers to verify evidence “travels”
│   ├── verify_referrers.{sh,py,ts,js}                # verify signatures/attestations
│   └── fixtures/
│       ├── valid/
│       │   ├── minimal_oci_artifact/
│       │   └── minimal_referrers/
│       └── invalid/
│           ├── unsigned_referrer/
│           └── wrong_digest/
│
├── supply_chain/                                     # OPTIONAL: SBOMs + attestations (release hardening)
│   ├── README.md
│   ├── build_sbom.{sh,py,ts,js}
│   ├── sign_attest.{sh,py,ts,js}                     # wrapper (NEVER stores keys in repo)
│   ├── verify_attest.{sh,py,ts,js}
│   └── fixtures/
│       ├── valid/
│       └── invalid/
│
├── watchers/                                         # OPTIONAL: watcher tooling support (usually lives in src/, but tools validate)
│   ├── README.md                                     # how watchers registry is validated + run in dry-run
│   ├── validate_watchers_registry.{sh,py,ts,js}      # duplicate entrypoint (kept for discoverability)
│   ├── run_watcher_dry_run.{sh,py,ts,js}             # optional: executes a watcher without side effects
│   └── fixtures/
│       ├── valid/
│       └── invalid/
│
├── graph/                                            # OPTIONAL: graph mapping + invariants checks
│   ├── README.md
│   ├── validate_graph_mappings.{sh,py,ts,js}          # validates graph/mappings/<domain>/*.yml shape
│   ├── run_graph_invariants.{sh,py,ts,js}             # runs invariants (Cypher) against a test graph
│   ├── schemas/
│   │   └── graph_mapping.v1.schema.json
│   ├── mappings/                                     # (source lives elsewhere; tools validate it)
│   │   └── _examples/
│   │       └── example_domain.yml
│   ├── invariants/
│   │   ├── invariants.cypher                          # example invariants
│   │   └── README.md
│   └── fixtures/
│       ├── valid/
│       └── invalid/
│
├── eval/                                             # OPTIONAL: “trust membrane” evaluation harness runners
│   ├── README.md
│   ├── focus_eval.{sh,py,ts,js}                       # optional: run Focus Mode golden evals
│   ├── evidence_resolver_contract.{sh,py,ts,js}       # optional: evidence resolver contract checks
│   └── fixtures/
│       ├── golden_queries/
│       └── expected_outputs/
│
├── domains/                                          # OPTIONAL: domain-specific tooling modules (keep isolated)
│   ├── README.md                                     # how to add domain tools; naming + ownership
│   ├── wzdx/                                          # example from the integration kit pattern
│   │   ├── normalize.{sh,py,ts,js}
│   │   ├── validate_wzdx.{sh,py,ts,js}
│   │   └── fixtures/
│   │       ├── valid/
│   │       │   └── wzdx_sample.json
│   │       └── invalid/
│   │           └── missing_required_field.json
│   ├── gtfs/                                          # optional placeholder
│   └── soils/                                         # optional placeholder
│
├── release/                                          # Optional: release tooling (must be deterministic)
│   ├── README.md                                     # How releases are assembled + verified
│   ├── build_sbom.{sh,py,ts,js}                      # SBOM build (if used)
│   ├── build_release_manifest.{sh,py,ts,js}          # Assemble release metadata + digests
│   ├── verify_release_artifacts.{sh,py,ts,js}        # Verify digests/signatures/attestations (if used)
│   ├── sign_release.{sh,py,ts,js}                    # Optional: signing wrapper (NEVER stores keys in repo)
│   └── fixtures/
│       ├── valid/
│       │   ├── release_manifest.json
│       │   └── SBOM.spdx.json
│       └── invalid/
│           ├── missing_digest.json
│           └── tampered_manifest.json
│
├── _shared/                                          # Shared helper libs (small; minimal side effects)
│   ├── README.md                                     # Shared helpers contract (keep pure where possible)
│   ├── fs.{py,ts,js}                                 # Safe file IO helpers (path traversal defense)
│   ├── json.{py,ts,js}                               # Canonical JSON + strict parsing helpers
│   ├── log.{py,ts,js}                                # Structured logging helpers (policy-safe)
│   ├── errors.{py,ts,js}                             # Standardized error/finding helpers (codes, severities)
│   ├── exit_codes.{py,ts,js}                         # Exit code constants + mapping
│   ├── time.{py,ts,js}                               # Time helpers (avoid non-determinism in hashes)
│   ├── cli.{py,ts,js}                                # Optional: shared CLI parsing + --json plumbing
│   └── redact.{py,ts,js}                             # Optional: redaction helpers for logs/errors
│
└── fixtures/                                         # Shared fixtures (synthetic/sanitized; tiny; documented)
    ├── public/
    │   ├── FIXTURE_NOTES.md                          # license + sensitivity + intended use
    │   ├── minimal_catalog_bundle/                   # tiny end-to-end bundle used across validators/linkcheck
    │   │   ├── dcat.jsonld
    │   │   ├── stac/collection.json
    │   │   ├── stac/items/item-001.json
    │   │   ├── prov/prov.jsonld
    │   │   └── receipts/run_receipt.json
    │   ├── minimal_policy_bundle/                    # optional: conftest fixtures
    │   │   ├── input.json
    │   │   └── expected.json
    │   ├── minimal_oci_referrers/                    # optional: stub manifests used by oci tools
    │   │   ├── artifact.json
    │   │   ├── receipt.referrer.json
    │   │   └── prov.referrer.json
    │   └── minimal_openapi/                          # optional: contract tool fixtures
    │       └── openapi.v1.yaml
    └── restricted_sanitized/
        ├── FIXTURE_NOTES.md                          # describes sanitization (no precise coords/identifiers)
        ├── generalized_geometry_bundle/              # coarse geometry used to test “no leakage” behavior
        │   ├── dcat.jsonld
        │   └── stac/items/item-001.json
        ├── policy_safe_error_cases/
        │   ├── forbidden.json                        # safe error envelope example
        │   └── not_found.json                        # indistinguishable or policy-safe variant
        └── restricted_receipts_sanitized/
            ├── run_receipt.redacted.json
            └── README.md
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
  H --> P[policy + contracts + tests]
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

## Promotion Contract gate mapping

Tools are not “nice-to-have QA.” They are how the **Promotion Contract** becomes enforceable behavior in CI and during operator-driven promotion.

### Gates → tool categories (starter mapping)

| Promotion Contract gate | What must be true | Typical tool category | Typical artifacts validated |
|---|---|---|---|
| **Gate A — Identity & versioning** | Stable `dataset_id`/`dataset_version_id`; deterministic `spec_hash`; content digests | `hash/` + registry/schema checks | dataset spec, registry entry, digests |
| **Gate B — Licensing & rights metadata** | License/rights fields present + upstream terms snapshot | validators + policy tests | DCAT, registry entry, license snapshot |
| **Gate C — Sensitivity & redaction plan** | `policy_label` present; obligations defined + honored | policy tests + lint | OPA fixtures, redaction rules |
| **Gate D — Catalog triplet validation** | DCAT/STAC/PROV validate + cross-link; EvidenceRefs resolve | `validators/` + `linkcheck/` | DCAT/STAC/PROV + EvidenceRefs |
| **Gate E — QA & thresholds** | Dataset QA checks exist + pass thresholds | validators + QA runners | QA reports, thresholds in spec |
| **Gate F — Run receipt & audit record** | Run receipt exists; captures inputs/tooling/hashes/policy decisions | receipt validators + policy tests | run_receipt, checksums, attestations |
| **Gate G — Release manifest (recommended)** | Promotion recorded as a manifest referencing digests | `release/` + verification | promotion manifest, release notes |

> [!NOTE]
> Keep the mapping **explicit** in the tool registry (which gates each tool enforces). CI should be able to answer: “Which tool proves Gate D?” without tribal knowledge.

[Back to top](#top)

---

## Quick start

> [!NOTE]
> Commands here are examples. Wire the repo’s real entry points (Makefile/Taskfile/npm scripts) and update this section accordingly.

### Run the core gates locally (example)

```bash
# From repo root (replace with your repo's actual bootstrap)
make bootstrap

# Validate catalogs/provenance/receipts (Gate D + F)
make tools-validate

# Cross-link check (Gate D)
make tools-linkcheck

# Spec-hash drift checks (Gate A)
make tools-hash-check

# Policy + lint guardrails (Gate C + general hygiene)
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
- gate type (merge vs promotion)
- **promotion gates enforced** (A–G)
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
      "enforces_promotion_gates": ["B", "D"],
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

| Tool | Type | What it checks | Gate type | Promotion gates | Owner |
|---|---|---|---|---|---|
| `tools/validators/validate_dcat.*` | validator | DCAT conforms to KFM profile; rights/license fields present | merge/promotion | B, D | TODO |
| `tools/validators/validate_stac.*` | validator | STAC Items/Collections/Assets conform to KFM profile | merge/promotion | D | TODO |
| `tools/validators/validate_prov.*` | validator | PROV bundle shape + required lineage links present | merge/promotion | D | TODO |
| `tools/validators/validate_receipts.*` | validator | run_receipt + checksums + promotion_manifest schema validity | promotion | F, G | TODO |
| `tools/linkcheck/catalog_triplet_linkcheck.*` | linkcheck | DCAT ↔ STAC ↔ PROV cross-links resolve deterministically | merge/promotion | D | TODO |
| `tools/hash/check_spec_hash_drift.*` | drift check | Deterministic spec-hash stability; blocks unintended drift | merge | A | TODO |
| `tools/lint/check_no_direct_store_access.*` | lint | Trust membrane guardrail: forbid forbidden deps/egress patterns | merge | (Trust membrane) | TODO |

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
- [ ] Entry in `tools/registry/tools.v1.json` including **which Promotion Contract gates it enforces**
- [ ] Entry in the [Tool inventory](#tool-registry-and-inventory)
- [ ] CI wiring (if the tool is a gate)
- [ ] Policy-safe logging (no restricted details; no secrets)

> [!TIP]
> If the tool enforces a Promotion Contract gate, treat it like a contract change: update fixtures, schema validators, and documentation together.

[Back to top](#top)

---

## Verification checklist

Use this checklist to turn “target posture” into **confirmed repo facts** (attach outputs to the next README revision):

- [ ] Capture repo commit hash and root directory tree: `git rev-parse HEAD` and `tree -L 3`.
- [ ] Confirm which work packages already exist: search for `spec_hash`, OPA policies, validators, evidence resolver route, and dataset registry schema.
- [ ] Extract CI gate list from `.github/workflows` and document which checks are blocking merges.
- [ ] Choose a single MVP dataset and verify it can be promoted through all gates with receipts and catalogs.
- [ ] Validate that UI cannot bypass the PEP (static analysis + network policies) and that EvidenceRefs resolve end-to-end in Map Explorer and Story publishing.
- [ ] For Focus Mode: run the evaluation harness and store golden query outputs and diffs as artifacts.

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
