# configs — Governed configuration registry

Governed, version-controlled configuration that drives **policy enforcement**, **contract validation**, **promotion gates**, and **runtime wiring** across Kansas Frontier Matrix (KFM).

**Status:** draft  
**Owners:** TBD (set via `CODEOWNERS`)  
**Principles:** map-first • time-aware • governed • evidence-first • cite-or-abstain

![status](https://img.shields.io/badge/status-draft-lightgrey)
![governance](https://img.shields.io/badge/governance-fail--closed-blue)
![contracts](https://img.shields.io/badge/contracts-contract--first-blue)

---

## Navigation

- [Quick start](#quick-start)
- [What lives here](#what-lives-here)
- [What does not live here](#what-does-not-live-here)
- [KFM invariants this directory must support](#kfm-invariants-this-directory-must-support)
- [Recommended layout](#recommended-layout)
- [Config precedence](#config-precedence)
- [Validation and CI gates](#validation-and-ci-gates)
- [Secrets and sensitive values](#secrets-and-sensitive-values)
- [Change management](#change-management)
- [Definition of Done](#definition-of-done)
- [Appendix](#appendix)

---

## Quick start

1. Identify which **contract surface** your change touches:
   - policy decision or obligation
   - schema/contract
   - promotion gate
   - environment/runtime wiring
2. Make the smallest change that is **testable and reversible**.
3. Add or update **fixtures/tests** that prove the new behavior.
4. Ensure validation passes locally and in CI.
5. If the change alters **allow/deny**, **obligations**, **rights enforcement**, or **sensitivity behavior**, route for **steward review** (fail closed until approved).

---

## What lives here

This directory is for configuration that changes **system behavior** without changing core code. Treat these files as **governed artifacts**: reviewable, testable, and promotion-gated.

Typical contents include:

- **Policy-as-code artifacts**
  - policy labels
  - obligations (redaction/generalization requirements)
  - allow/deny fixtures and test cases
- **Contract artifacts**
  - schema profiles for catalogs and provenance
  - API request/response schemas
  - lint rules for cross-links and resolvability
- **Promotion Contract wiring**
  - gate definitions and thresholds
  - promotion manifest templates
  - policy/rights/sensitivity checks configuration
- **Runtime wiring**
  - feature flags
  - indexing options
  - cache controls
  - environment overlays (dev/stage/prod) as *examples only*

> NOTE  
> This README is a registry and a contract. Keep it accurate. If the repo’s real structure differs, **update the “Config registry” table** and the layout section.

---

## What does not live here

- **Secrets** (tokens, passwords, private keys, connection strings with credentials)
- **Restricted coordinates** or raw sensitive-location data
- **PII** or private individual details
- **Large datasets** or derived artifacts (those belong in data lifecycle zones, governed by run receipts and promotion)
- **Ad-hoc scripts** without tests (put tooling under `tools/` or equivalent)

---

## KFM invariants this directory must support

Configuration in this directory exists to make KFM’s posture enforceable. At minimum:

- **Trust membrane**
  - Frontend and external clients must not access databases/object storage directly.
  - Backend core logic must not bypass repository interfaces to reach storage.
  - Access must flow through governed APIs that apply policy, redaction, and logging consistently.

- **Policy-as-code parity**
  - Policy semantics must match between CI and runtime (or fixtures/outcomes must match). If CI and runtime disagree, CI guarantees are meaningless.

- **Promotion Contract gates**
  - Dataset outputs move through governed zones; promotion must be blocked unless required gates pass.
  - Config must support deterministic, fail-closed gating.

- **Catalog triplet as contract surface**
  - Catalogs/provenance are not “nice metadata”; they are the canonical interface between pipeline outputs and runtime.
  - Profiles and cross-link rules must be strict and validated.

- **Evidence-first and cite-or-abstain**
  - Any surfaced layer/story/answer must map back to resolvable evidence bundles and policy decisions.
  - If citations cannot be verified, the system must abstain or reduce scope.

- **Rights and sensitivity enforcement**
  - Rights metadata and attribution must be enforced in exports and publishing.
  - Sensitive-location handling defaults to deny or to publish-safe generalized derivatives when allowed.

- **Deterministic identity and hashing**
  - Dataset version identity must be stable, based on canonical specifications; prevent “hash drift.”

---

## Recommended layout

This is a **buildable target** layout for `configs/`. Adjust to match the repo, but keep the separation between policy, contracts, promotion gates, and runtime wiring.

```text
configs/
  README.md

  policy/                       # policy-as-code inputs (governed)
    labels/                     # policy labels + meanings
    obligations/                # obligation definitions (generalize geometry, suppress export, etc.)
    fixtures/                   # allow/deny + obligations test cases
    tests/                      # policy unit tests (engine-specific)
    rubrics/                    # licensing + sensitivity rubrics (human-readable + machine-usable)

  contracts/                    # machine-validated contract artifacts
    schemas/                    # JSON Schema (or equivalent) for DCAT/STAC/PROV + API DTOs
    profiles/                   # profile constraints (required fields, controlled vocab, etc.)
    linkcheck/                  # cross-link rules for DCAT/STAC/PROV + EvidenceRefs

  promotion/                    # promotion contract wiring
    gates/                      # gate definitions, thresholds, required artifacts
    templates/                  # promotion manifests, run receipt templates (if stored here)
    ci/                         # CI config for promotion gating (optional)

  runtime/                      # runtime wiring (non-secret)
    feature_flags/
    indexing/
    caching/

  env/                          # example overlays (no secrets)
    dev.example.env
    staging.example.env
    prod.example.env
```

### Config registry

Update this table whenever you add, move, or deprecate config files.

| Area | Path (relative) | Format | Used by | Validation in CI | Owner |
|---|---|---:|---|---:|---|
| Policy labels | `policy/labels/` | YAML/JSON | API + evidence resolver | Required | Steward |
| Obligations | `policy/obligations/` | YAML/JSON | API + pipelines | Required | Steward |
| Policy fixtures | `policy/fixtures/` | JSON | CI + runtime parity tests | Required | Steward + Eng |
| Schemas | `contracts/schemas/` | JSON Schema | CI + runtime validators | Required | API/Standards |
| Profiles | `contracts/profiles/` | MD + machine file | Catalog validators | Required | Standards |
| Linkcheck rules | `contracts/linkcheck/` | Config | CI link-checker | Required | Platform |
| Gate definitions | `promotion/gates/` | YAML/JSON | pipeline promotion step | Required | Steward + Eng |
| Feature flags | `runtime/feature_flags/` | YAML/JSON | API + UI | Required (lint) | Platform |
| Env examples | `env/*.example.env` | dotenv | local dev | Required (secret scan) | Platform |

---

## Config precedence

Config should resolve deterministically and be reproducible for audits.

**Recommended precedence:**

1. Repository defaults in `configs/…`
2. Environment overlay (dev/stage/prod) if present
3. Runtime environment variables (non-secret)
4. Secret manager injection (outside git)
5. Per-run parameters (pipeline/focus) captured in **run receipts**

If two sources conflict, resolution must be explicit and documented. If required config is missing, **fail closed**.

---

## Validation and CI gates

This directory is only safe if it is continuously validated. At minimum CI should enforce:

### Policy checks
- Policy fixtures execute under the same semantics as runtime.
- Default-deny behavior is preserved unless explicitly changed.
- Obligations are testable (a change must have a fixture proving it).

### Contract checks
- Schema validation for:
  - catalog records
  - provenance bundles
  - API request/response DTOs
- Controlled vocabulary validation where applicable
- Cross-link checking:
  - DCAT ↔ STAC ↔ PROV links resolve deterministically
  - EvidenceRef schemes resolve without guessing

### Promotion gating checks
- Promotion manifests reference required artifacts and digests
- Rights and sensitivity metadata required by gates are present
- Gate failures block merge and block promotion

### Suggested local commands

> Replace these placeholders with real repo commands when available.

```bash
# Schema validation
make validate-schemas

# Policy tests
make test-policy

# Link checking
make linkcheck-catalogs

# Secret scanning (should already run in CI)
make scan-secrets
```

---

## Secrets and sensitive values

**Never commit secrets**. Use:
- environment variables injected at runtime
- secret managers
- platform-native secrets (Kubernetes/OpenShift secrets, etc.)

If a config file needs a reference to a secret, store only a **secret key name** (identifier), not the secret value.

Also: do not store exact coordinates or restricted site details in config. Use policy labels + obligations to enforce generalization and access control.

---

## Change management

### Review rules

Some changes are governance-critical and require steward review:

- changes to allow/deny logic
- changes to obligations
- changes to sensitivity defaults or generalization behavior
- changes to licensing/risk rubrics
- changes to promotion gate criteria
- changes to schema profiles that affect what is publishable

### Versioning guidance

- Schemas and profiles must be versioned.
- Breaking changes require explicit version bumps and migration strategy.
- Keep old versions readable long enough to support reproducibility and audit.

---

## Definition of Done

Use this checklist in PRs that touch `configs/`.

- [ ] Change is scoped and reversible (rollback path described)
- [ ] Config registry table updated (paths/owners/validation)
- [ ] Fixtures/tests updated or added to prove new behavior
- [ ] CI validations pass (schemas, policy tests, linkcheck, secret scan)
- [ ] No secrets committed (confirmed by scan)
- [ ] If change affects governance outcomes, steward review completed
- [ ] Any behavior change is documented in the relevant standard or ADR

---

## Appendix

<details>
<summary>Optional metadata block for governed config docs</summary>

If you store additional governed documentation inside `configs/` (rubrics, standards, etc.), prefer a structured metadata block rather than YAML frontmatter.

```text
[KFM_META_BLOCK_V2]
doc_id: kfm://doc/<uuid>
title: <Title>
type: <guide|standard|dataset_spec|adr|run_receipt>
version: v1
status: draft|review|published
owners: <team or names>
created: YYYY-MM-DD
updated: YYYY-MM-DD
policy_label: public|restricted|...
related:
  - kfm://dataset/<slug>@<version>
tags:
  - kfm
  - configs
notes:
  - <short notes>
[/KFM_META_BLOCK_V2]
```

</details>

---

[Back to top](#configs--governed-configuration-registry)
