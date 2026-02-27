<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/9f8d0a2c-6d1e-4b22-a51d-0d7ac820e4e1
title: configs — Governed configuration registry
type: standard
version: v2
status: draft
owners: TBD (set via CODEOWNERS)
created: 2026-02-22
updated: 2026-02-27
policy_label: restricted
related:
  - ../README.md
  - ../.github/README.md
tags:
  - kfm
  - configs
  - governance
  - policy-as-code
  - contracts
  - promotion-contract
notes:
  - Policy-bearing configuration MUST be reviewed, tested, and promotion-gated.
  - This README is fail-closed: repo-specific wiring is UNKNOWN until validated in CI and confirmed via tree/paths.
  - Prefer machine-readable registries + schema validation over tribal knowledge.
[/KFM_META_BLOCK_V2] -->

<a id="top"></a>

# configs/ — Governed configuration registry

**Purpose:** Governed, version-controlled configuration that drives **policy enforcement**, **contract validation**, **promotion gates**, and **runtime wiring** across Kansas Frontier Matrix (KFM) — without shipping secrets.

**Status:** draft • **Owners:** TBD via `CODEOWNERS` • **Policy label:** restricted  
**Core posture:** default-deny • fail-closed • deterministic resolution • audit-ready • reversible changes

![status](https://img.shields.io/badge/status-draft-lightgrey)
![policy](https://img.shields.io/badge/policy-restricted-red)
![governance](https://img.shields.io/badge/governance-fail--closed-blue)
![contracts](https://img.shields.io/badge/contracts-contract--first-blue)
![promotion](https://img.shields.io/badge/promotion%20contract-gates%20A--F-critical)
![audit](https://img.shields.io/badge/audit-reproducible%20by%20digest-blue)
![anti-skip](https://img.shields.io/badge/CI-anti--skip%20required-important)

> [!WARNING]
> `configs/` is **behavioral surface area**.
> If a config change can alter **allow/deny**, **obligations**, **rights**, **sensitivity**, **promotion gates**, or **contract validation**, it is governance-critical and MUST be validated + reviewed as production configuration.

---

## Navigation

- [Directory contract](#directory-contract)
- [Truth status legend](#truth-status-legend)
- [Quick start](#quick-start)
- [Repo reality check](#repo-reality-check)
- [Scope](#scope)
- [KFM invariants this directory must support](#kfm-invariants-this-directory-must-support)
- [Recommended layout](#recommended-layout)
- [Config registry](#config-registry)
- [Conventions](#conventions)
- [Config precedence and resolution](#config-precedence-and-resolution)
- [Validation and CI gates](#validation-and-ci-gates)
- [Secrets and sensitive values](#secrets-and-sensitive-values)
- [Ownership and review routing](#ownership-and-review-routing)
- [Change management](#change-management)
- [Definition of Done](#definition-of-done)
- [Appendix](#appendix)

---

## Directory contract

| Contract item | Requirement |
|---|---|
| Purpose | Governed configuration that can change system behavior without changing core code |
| Acceptable inputs | Small, reviewable, machine-validated config files (YAML/JSON/TOML/etc.) that drive policy, contracts, promotion gates, pipeline wiring, UI wiring, observability |
| Exclusions | **Secrets**, private keys, raw restricted coordinates, PII, large datasets, opaque binaries, ad-hoc scripts without tests |
| Review posture | **Fail closed** for governance-critical changes; steward/owner review required |
| Promotion posture | Config changes that affect publishability, access, or identity MUST be promotion-gated and auditable |
| Audit posture | Resolved config set SHOULD be captured (by digest) in run receipts and/or deployment receipts |

> [!NOTE]
> If the real repo structure differs from this README, update the **Config registry** first. Don’t “fix” drift by weakening gates.

---

## Truth status legend

- **CONFIRMED (design):** required KFM posture (must hold regardless of stack)
- **UNKNOWN (repo):** not verified in this repository yet (treat as TODO)
- **PROPOSED:** recommended pattern/template (adopt only after verification)

This README intentionally includes **PROPOSED** structure to support bootstrapping, while keeping repo-specific facts **UNKNOWN** until verified.

---

## Quick start

1. Identify which **contract surface** your change touches:
   - policy decisions / obligations
   - schemas / profiles / cross-link rules
   - promotion gates / thresholds
   - runtime wiring (flags, caching, indexing)
   - UI wiring (layer registries, view-state schema versions)
2. Make the smallest change that is **testable** and **reversible**.
3. Add or update **fixtures/tests** that prove the new behavior.
4. Ensure validation passes locally and in CI.
5. If the change alters **allow/deny**, **obligations**, **rights enforcement**, **sensitivity behavior**, or **promotion gates**, route for **steward review** and fail closed until approved.

> [!TIP]
> Treat every config change as a behavior change. If you can’t explain how decisions change, you likely can’t validate it.

---

## Repo reality check

This README describes a **target posture**. Before treating any statement here as CONFIRMED (repo), verify the repo actually contains:

- [ ] `CODEOWNERS` routes reviews for governance-critical config paths
- [ ] CI checks validate configs (schemas + policy parity + linkcheck + secret scanning)
- [ ] a deterministic config resolver that **fails on conflicts** (no silent precedence)
- [ ] runtime components apply the **same policy semantics** as CI (parity)

Minimum verification steps (copy/paste):

```bash
# 1) Inspect actual layout
find configs -maxdepth 3 -type d -print

# 2) Find ownership rules
ls -la .github/CODEOWNERS 2>/dev/null || ls -la CODEOWNERS 2>/dev/null

# 3) Locate CI workflows that validate configs
ls -la .github/workflows 2>/dev/null || true

# 4) Search for config resolver / loader
rg -n "config resolver|loadConfig|resolveConfig|CONFIG_" -S . || true
```

> [!IMPORTANT]
> If validation, ownership routing, or deterministic resolution is missing, treat `configs/` as **unsafe** until those controls exist.

---

## Scope

### What lives here

`configs/` holds configuration that changes **system behavior** without changing core code. Treat these files as **governed artifacts**: reviewable, testable, and promotion-gated.

Common categories:

- **Policy-bearing inputs** (configuration *about* policy)
  - policy label definitions (meaning, display text, export posture)
  - obligation catalogs (generalize geometry, suppress export, watermark, require notice)
  - sensitivity/risk rubrics (machine + human readable)
  - policy parity fixtures (synthetic allow/deny expectations)

- **Contract wiring**
  - which schema/profile versions are active in an environment
  - validator knobs and cross-link/lint rules
  - controlled vocabulary selection and enforcement switches

- **Promotion Contract wiring**
  - gate definitions, thresholds, required artifacts, failure modes
  - “what must be true to promote” per dataset class and per policy label

- **Runtime wiring** (non-secret defaults)
  - feature flags
  - caching rules (including auth/policy-aware cache keying)
  - indexing configuration (search/vector/graph projections)
  - rate limits / safety knobs for public endpoints (as references; enforcement is in runtime)

- **Pipeline wiring** (non-secret)
  - schedules, dataset class defaults, allowed transforms
  - resource classes and safe defaults (timeouts, retries)

- **UI wiring** (non-secret)
  - layer registry defaults, UI policy badge rules, view-state schema versions
  - *NOTE:* UI must never become the enforcement point; it renders what the governed API returns.

- **Observability wiring**
  - telemetry redaction rules (client + server)
  - log field allowlists/denylists (policy-safe)
  - metric naming conventions and SLO thresholds

### What does not live here

- **Secrets** (tokens, passwords, private keys, credentialed connection strings)
- **Raw restricted coordinates** or sensitive-location datasets
- **PII** or private individual details
- **Large datasets** or derived artifacts (those belong in truth path zones with run receipts)
- **Ad-hoc scripts** without tests (put tooling under `tools/`)

> [!WARNING]
> If it would be unsafe to paste into a public issue, it does not belong in `configs/`.

---

## KFM invariants this directory must support

Configuration exists to make KFM’s posture enforceable:

### Trust membrane (CONFIRMED design)
- Apps/clients MUST NOT access DB/object storage directly.
- Enforcement MUST happen behind governed APIs (policy + evidence + audit).
- Config MUST NOT enable bypass routes.

### Policy-as-code parity (CONFIRMED design)
- Policy semantics MUST match between CI and runtime (fixture outcomes match).
- If CI and runtime disagree, CI guarantees are meaningless → release blocker.

### Promotion Contract gates A–F (CONFIRMED design)
Config must support deterministic, fail-closed gates:
- **A Identity/versioning:** spec-hash stability inputs and drift detection
- **B Rights/licensing:** license/attribution requirements and enforcement switches
- **C Sensitivity:** policy labels and obligation defaults (generalization, suppression)
- **D Catalog triplet:** profile selection + cross-link rules (DCAT/STAC/PROV)
- **E Receipts/checksums:** required receipt fields + digest requirements
- **F Policy/contracts:** fixture expectations + contract validation knobs

### Evidence-first + cite-or-abstain (CONFIRMED design)
- Any surfaced layer/story/answer MUST map back to resolvable evidence bundles and policy decisions.
- If citations cannot be verified, the system MUST abstain or reduce scope.

### Deterministic identity/hashing (CONFIRMED design)
- Inputs to identity/hashing MUST be stable and versioned.
- Any change that affects identity inputs MUST have tests proving intended behavior.

---

## Recommended layout

> [!NOTE]
> This is a **PROPOSED** buildable layout. Align it to repo reality and keep the Config registry current.

```text
configs/
├─ README.md
│
├─ registry/                                    # Machine-readable registries + schemas + fixtures (small)
│  ├─ configs.v1.json                            # Canonical registry of governed configs (paths, owners, validators)
│  ├─ schemas/                                   # JSON Schemas for registries and config shapes (if stored here)
│  └─ fixtures/                                  # Valid/invalid examples for CI validation
│
├─ policy/                                       # Policy-bearing configuration (NOT secrets; NOT policy engine code)
│  ├─ labels/                                    # Policy labels + semantics + display hints
│  ├─ obligations/                               # Obligation catalog (generalize, suppress export, show notice, etc.)
│  ├─ rubrics/                                   # Licensing + sensitivity rubrics (machine-readable + human-readable)
│  └─ fixtures/                                  # Policy parity fixtures (synthetic allow/deny/obligation expectations)
│
├─ contracts/                                    # Contract wiring (version selection + validator knobs)
│  ├─ profiles/                                  # Which DCAT/STAC/PROV profiles are active per environment/class
│  ├─ vocab/                                     # Controlled vocab selection and validation toggles
│  └─ linkcheck/                                 # Cross-link/lint rules (EvidenceRef resolvability expectations)
│
├─ promotion/                                    # Promotion Contract wiring
│  ├─ gates/                                     # Gate definitions + thresholds + required artifacts
│  ├─ templates/                                 # Manifest/receipt templates (if not stored elsewhere)
│  └─ classes/                                   # Dataset class defaults (raster/vector/docs) and required checks
│
├─ runtime/                                      # Runtime wiring (non-secret defaults)
│  ├─ feature_flags/
│  ├─ caching/
│  ├─ indexing/
│  └─ rate_limits/
│
├─ pipelines/                                    # Pipeline runner wiring (non-secret)
│  ├─ schedules/
│  ├─ runners/
│  └─ dataset_defaults/
│
├─ ui/                                           # UI wiring (non-secret)
│  ├─ layers/                                    # Layer registry defaults, layer groups, display metadata
│  ├─ view_state/                                # View-state schema versions + compatibility rules
│  └─ policy_badges/                             # UI rendering rules for policy/validation badges (display-only)
│
├─ observability/                                # Observability wiring (policy-safe)
│  ├─ logging/
│  ├─ metrics/
│  └─ redaction/
│
└─ env/                                          # Example overlays (NO secrets; keys only)
   ├─ dev.example.env
   ├─ staging.example.env
   └─ prod.example.env
```

> [!IMPORTANT]
> If your repo already has top-level `policy/` and `contracts/` as sources of truth, avoid duplication:
> - keep policy *rules* and schema *definitions* where they live,
> - keep only **wiring + selection + registries + parity fixtures** under `configs/`.

---

## Config registry

The registry is how we prevent config sprawl and “unknown behavior.”

### Machine-readable registry (PROPOSED)

Store a canonical registry that CI can validate:

- `configs/registry/configs.v1.json`

Template:

```json
{
  "kfm_config_registry_version": "v1",
  "updated": "2026-02-27",
  "entries": [
    {
      "id": "policy.labels",
      "path": "configs/policy/labels/",
      "format": "yaml",
      "behavior_class": "governance-critical",
      "validators": ["configs-lint", "policy-parity"],
      "owners": ["@kfm-governance"],
      "notes": "Defines policy labels and semantics used by API + UI badges."
    }
  ]
}
```

### Registry table (human)

Keep this table consistent with the machine registry if you adopt it.

| Area | Path (relative) | Format | Used by | CI validation | Change class |
|---|---|---|---|---|---|
| Policy labels | `policy/labels/` | YAML/JSON | API + evidence resolver + UI badges | **Required** | Governance-critical |
| Obligations | `policy/obligations/` | YAML/JSON | API + pipelines + exports | **Required** | Governance-critical |
| Policy fixtures | `policy/fixtures/` | JSON | CI + runtime parity | **Required** | Governance-critical |
| Profiles wiring | `contracts/profiles/` | YAML/JSON | catalog validators | **Required** | Contract-breaking (sometimes) |
| Linkcheck rules | `contracts/linkcheck/` | YAML/JSON | CI linkcheck | **Required** | Contract-breaking (sometimes) |
| Gate definitions | `promotion/gates/` | YAML/JSON | promotion step | **Required** | Governance-critical |
| Feature flags | `runtime/feature_flags/` | YAML/JSON | API + UI | **Required (lint)** | Runtime behavior |
| UI layers | `ui/layers/` | YAML/JSON | UI + API (display metadata) | **Required (lint)** | UX behavior |
| Env examples | `env/*.example.env` | dotenv | local dev | **Required (secret scan)** | Docs-only |

### Registry Definition of Done

- [ ] Every config area has an owner via `CODEOWNERS`.
- [ ] Every config area has at least one validator running in CI.
- [ ] Governance-critical entries have fixtures proving allow/deny/obligation outcomes.
- [ ] Any config that affects publishability maps to Promotion Contract gates A–F.
- [ ] The registry is updated in the same PR that adds/moves/deprecates config.

---

## Conventions

### Formats

- Prefer YAML for human-authored config; JSON for fixtures and machine-to-machine artifacts.
- Keep files small and composable.
- Avoid YAML anchors/aliases unless the repo explicitly standardizes them.
- Every config SHOULD have a stable schema or lint rules.

> [!TIP]
> If a config has no validator, it is code without tests.

### Identifiers and versioning

- Contract-bearing config SHOULD be versioned (e.g., `v1`, `2026-02`, semver).
- Policy labels are controlled vocabulary; changing meaning is breaking behavior.
- Any identifier that flows into dataset identity/spec hashing MUST be stable and tested.

### Secret references

If a config must reference a secret, store only a **secret identifier**, never the secret value:

- `secret_ref: KFM_API_KEY`
- `secret_ref: kfm/<env>/<service>/token`

---

## Config precedence and resolution

Config resolution MUST be deterministic and reproducible for audits.

### Recommended precedence (PROPOSED)

1. Repository defaults in `configs/**`
2. Environment overlay (dev/stage/prod) **if used** (examples unless explicitly promoted)
3. Runtime environment variables (non-secret)
4. Secret manager injection (outside git)
5. Per-run parameters (pipeline/focus) captured in run receipts

If two sources conflict, resolution MUST be explicit and documented. If required config is missing, **fail closed**.

### Resolution and enforcement flow

```mermaid
flowchart LR
  subgraph Sources["Config sources (ordered precedence)"]
    A["1) repo defaults<br/>configs/**"]
    B["2) env overlay<br/>configs/env/* (if used)"]
    C["3) runtime env vars<br/>(non-secret)"]
    D["4) secret manager<br/>(outside git)"]
    E["5) per-run params<br/>captured in run receipts"]
  end

  R["Config resolver<br/>(deterministic merge + explicit conflicts)"]

  A --> R
  B --> R
  C --> R
  D --> R
  E --> R

  R --> V["Validators<br/>(schemas, parity tests, linkcheck)"]
  V --> CI["CI gates<br/>(merge blocked if fail)"]
  V --> RT["Runtime wiring<br/>(API / pipelines / indexers)"]

  RT --> REC["Run receipts / deploy receipts<br/>(capture resolved config digest)"]
```

> [!WARNING]
> A resolver that “picks one silently” breaks auditability. Conflicts MUST surface as errors unless explicitly overridden with tests and documentation.

---

## Validation and CI gates

This directory is only safe if it is continuously validated.

### Required validations (minimum)

- **Schema/lint:** configs validate against schemas or strict lint rules
- **Policy parity:** fixtures prove expected allow/deny/obligations
- **Linkcheck:** cross-link rules ensure EvidenceRef and catalog links are resolvable deterministically
- **Secret scanning:** blocks committed credentials
- **Anti-skip summary:** a final always-runs job fails if any required config gate did not run

> [!IMPORTANT]
> Required checks MUST NOT be skippable via `paths:` filters or `if:` conditions.
> Prefer a single “gate-summary” status check as the merge requirement (see `.github/README.md` if present).

### Promotion Contract mapping (A–F)

| Gate | What configs influence | What CI should verify (examples) |
|---|---|---|
| A Identity/versioning | spec-hash inputs, version naming rules | hash drift tests; naming lint |
| B Rights/licensing | license rules, attribution requirements | rights rubrics validated; export rules consistent |
| C Sensitivity | policy labels, obligations defaults | deny-by-default preserved; generalization obligations tested |
| D Catalog triplet | profile selection, link rules | profiles validate; linkcheck passes |
| E Receipts/checksums | required receipt fields | receipt schema validation; required digests present |
| F Policy/contracts | parity fixtures + contract knobs | parity tests pass; contract checks pass |

### Suggested local commands (PROPOSED)

Replace these placeholders with real repo commands once wiring exists:

```bash
make lint-configs
make validate-config-schemas
make test-policy-parity
make linkcheck-catalogs
make scan-secrets
```

---

## Secrets and sensitive values

**Never commit secrets.** Use environment injection and secret managers.

Also prohibited in `configs/`:
- raw restricted geometry / sensitive site coordinates
- PII or reidentifiable personal attributes

If sensitivity handling is unclear, default to deny and route for governance review.

---

## Ownership and review routing

`CODEOWNERS` SHOULD require review for governance-critical config changes. Example (placeholders):

```text
# Governance-critical policy inputs
configs/policy/**        @kfm-governance

# Promotion gates
configs/promotion/**     @kfm-governance @kfm-platform

# Contract wiring
configs/contracts/**     @kfm-standards @kfm-platform

# Runtime knobs
configs/runtime/**       @kfm-platform

# UI wiring
configs/ui/**            @kfm-frontend @kfm-governance

# Observability
configs/observability/** @kfm-platform
```

> [!NOTE]
> Replace the placeholder teams with real owners. Ownership is only real once CODEOWNERS is enforced via branch protection/rulesets.

---

## Change management

### Change classes

Use PR labels or title prefixes for `configs/` changes:

| Class | Meaning | Extra requirements |
|---|---|---|
| Docs-only | README/examples; no behavior change | lint + secret scan |
| Runtime behavior | flags/caches/index knobs | smoke checks for affected components |
| Contract-breaking | profile/schema selection rules | version bump + migration notes |
| Governance-critical | allow/deny, obligations, sensitivity defaults, gate thresholds | steward review + parity fixtures |

### Rollback expectations

Every governance-critical config change MUST include a rollback plan:
- revert commit/PR
- restore prior config version
- confirm parity tests and linkcheck pass on rollback

### Deprecation and migrations

- Deprecations MUST be explicit (document in-file and/or ADR/changelog).
- Keep old versions readable long enough for reproducibility/audits.
- Remove deprecated configs only when receipts prove successful migration.

---

## Definition of Done

Use this checklist in PRs touching `configs/`.

- [ ] Change is scoped and reversible (rollback described)
- [ ] Config registry updated (table + machine registry if adopted)
- [ ] Validators updated/added (schemas/lint/parity/linkcheck as applicable)
- [ ] Governance-critical changes include parity fixtures proving new behavior
- [ ] CI validations pass (and anti-skip summary passes)
- [ ] No secrets committed (scan passes)
- [ ] Required owners reviewed (CODEOWNERS)
- [ ] Any contract-breaking change includes migration notes

---

## Appendix

<details>
<summary><strong>PROPOSED: Minimal policy label file shape</strong></summary>

Example: `configs/policy/labels/labels.v1.yaml`

```yaml
version: v1
labels:
  public:
    description: "Publicly viewable and exportable under license terms."
    export: allowed
  public_generalized:
    description: "Public viewable; geometry generalized by obligation."
    export: allowed
    obligations: ["generalize_geometry", "show_generalization_notice"]
  restricted:
    description: "Access restricted by role; deny by default."
    export: denied
  restricted_sensitive_location:
    description: "Sensitive location; deny public access; generalized derivative required for public surfaces."
    export: denied
```

</details>

<details>
<summary><strong>PROPOSED: Obligation catalog shape</strong></summary>

Example: `configs/policy/obligations/obligations.v1.yaml`

```yaml
version: v1
obligations:
  generalize_geometry:
    kind: transform
    parameters:
      method: "grid_snap"
      cell_meters: 1000
  suppress_export:
    kind: enforcement
    parameters:
      export: false
  show_generalization_notice:
    kind: ui_notice
    parameters:
      message: "Geometry generalized due to policy."
```

</details>

<p align="right"><a href="#top">Back to top ↑</a></p>
