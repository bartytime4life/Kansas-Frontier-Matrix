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
├─ registry/                                     # Machine-readable registries + schemas + fixtures (small)
│  ├─ README.md                                  # Registry contract: what MUST be listed + how CI validates it
│  ├─ configs.v1.json                            # Canonical registry (entries for every governed config area/file)
│  ├─ schemas/                                   # Schemas for registries + config shapes (or pointers to contracts/)
│  │  ├─ kfm.config_registry.v1.schema.json      # Validates configs.v1.json (paths, owners, validators, class)
│  │  ├─ kfm.policy_labels.v1.schema.json        # Validates policy label documents
│  │  ├─ kfm.obligations_catalog.v1.schema.json  # Validates obligations catalog documents
│  │  ├─ kfm.promotion_gates.v1.schema.json      # Validates gate definition documents
│  │  ├─ kfm.linkcheck_rules.v1.schema.json      # Validates linkcheck rule documents
│  │  ├─ kfm.feature_flags.v1.schema.json        # Validates runtime feature flag docs
│  │  ├─ kfm.rate_limits.v1.schema.json          # Validates rate limit configs
│  │  ├─ kfm.ui_layer_registry.v1.schema.json    # Validates UI layer registry configs
│  │  ├─ kfm.view_state_schema.v1.schema.json    # Validates view_state schema + migrations metadata
│  │  └─ kfm.redaction_rules.v1.schema.json      # Validates observability redaction rules
│  ├─ fixtures/                                  # Fixtures for CI validation (valid/invalid; deterministic)
│  │  ├─ valid/
│  │  │  ├─ configs.v1.valid.min.json
│  │  │  ├─ policy.labels.v1.valid.yaml
│  │  │  ├─ policy.obligations.v1.valid.yaml
│  │  │  ├─ promotion.gates.v1.valid.yaml
│  │  │  └─ ui.layers.v1.valid.yaml
│  │  ├─ invalid/
│  │  │  ├─ configs.v1.invalid.missing_owner.json
│  │  │  ├─ configs.v1.invalid.bad_path.json
│  │  │  ├─ policy.labels.v1.invalid.unknown_label.yaml
│  │  │  ├─ promotion.gates.v1.invalid.missing_gate.yaml
│  │  │  └─ ui.layers.v1.invalid.missing_dataset_version.yaml
│  │  └─ README.md                               # How fixtures are used (what each one is asserting)
│  └─ _generated/                                # OPTIONAL: generated indexes used by CI/tools (policy decides commit vs ignore)
│     ├─ configs.index.v1.json                    # Flattened index (resolved paths + digests)
│     └─ checksums.v1.json                        # Digest list for configs artifacts (audit-friendly)
│
├─ policy/                                       # Policy-bearing configuration (NOT secrets; NOT policy engine code)
│  ├─ README.md                                  # Policy inputs contract: labels + obligations + rubrics + fixtures
│  ├─ labels/                                    # Policy labels + semantics + display hints
│  │  ├─ README.md
│  │  ├─ labels.v1.yaml                          # Canonical label definitions (public/restricted/etc)
│  │  ├─ labels.display.v1.yaml                  # UI display hints (policy-safe names, colors as tokens, tooltips)
│  │  ├─ labels.export_rules.v1.yaml             # Export posture per label (allowed/denied + obligations)
│  │  └─ labels.compat.v1.yaml                   # Compatibility/migration notes (v1→v2 mapping when needed)
│  ├─ obligations/                               # Obligation catalog (generalize, suppress export, show notice, etc.)
│  │  ├─ README.md
│  │  ├─ obligations.v1.yaml                     # Obligation definitions (kind, params, default UX messaging)
│  │  ├─ obligations.transforms.v1.yaml          # Transform obligations (generalize, jitter, aggregate, redact fields)
│  │  ├─ obligations.notices.v1.yaml             # Notice obligations (required banners, attribution, disclaimers)
│  │  ├─ obligations.exports.v1.yaml             # Export obligations (watermark, suppress, attribution bundle)
│  │  └─ obligations.compat.v1.yaml              # Version mapping for obligations (if you evolve them)
│  ├─ rubrics/                                   # Licensing + sensitivity rubrics (machine-readable + human-readable)
│  │  ├─ README.md
│  │  ├─ licensing_rubric.v1.md                  # Human rubric (what counts as “clear rights”, “metadata-only”, etc.)
│  │  ├─ licensing_rubric.v1.yaml                # Machine rubric (flags, required fields, block conditions)
│  │  ├─ sensitivity_rubric.v1.md                # Human rubric (sensitive location, PII risk, aggregation thresholds)
│  │  ├─ sensitivity_rubric.v1.yaml              # Machine rubric (labels, default obligations, deny rules)
│  │  ├─ pii_risk_rubric.v1.md                   # Human rubric for reidentification risk + minimum counts
│  │  └─ pii_risk_rubric.v1.yaml                 # Machine thresholds + rules (if applicable)
│  └─ fixtures/                                  # Policy parity fixtures (synthetic allow/deny/obligation expectations)
│     ├─ README.md                               # Fixture rules: deterministic, synthetic, no sensitive coords
│     ├─ inputs/
│     │  ├─ fixture_inputs.v1.json               # Structured inputs: user roles, resource labels, action types
│     │  ├─ resource_samples.v1.json             # Sample resources (datasets/stories/evidence) policy-labeled
│     │  └─ obligations_samples.v1.json          # Sample obligation requests
│     ├─ expected/
│     │  ├─ fixture_expected.v1.json             # Expected allow/deny + obligations results
│     │  ├─ fixture_expected.public.v1.json
│     │  ├─ fixture_expected.restricted.v1.json
│     │  └─ fixture_expected.sensitive_location.v1.json
│     └─ golden/
│        └─ parity_golden.v1.json                # Golden outputs for parity tests (CI vs runtime)
│
├─ contracts/                                    # Contract wiring (version selection + validator knobs)
│  ├─ README.md                                  # “Wiring not definitions”: selects/targets contract versions
│  ├─ profiles/                                  # Which DCAT/STAC/PROV profiles are active per env/class
│  │  ├─ README.md
│  │  ├─ dcat.profile_set.v1.yaml                # Active DCAT profile set + required fields per dataset class
│  │  ├─ stac.profile_set.v1.yaml                # Active STAC profile set + required assets/fields
│  │  ├─ prov.profile_set.v1.yaml                # Active PROV profile set + required lineage/agents
│  │  ├─ profiles.by_class.v1.yaml               # Map: dataset_class → profile set (vector/raster/docs)
│  │  └─ profiles.by_env.v1.yaml                 # Map: env → profile overrides (dev/stage/prod), non-secret
│  ├─ vocab/                                     # Controlled vocab selection and validation toggles
│  │  ├─ README.md
│  │  ├─ vocab.sources.v1.yaml                   # Allowed source domains/authority list (for registry hygiene)
│  │  ├─ vocab.themes.v1.yaml                    # Themes/tags vocabulary (DCAT theme, story tags)
│  │  ├─ vocab.policy_labels.v1.yaml             # Mirror/lock policy labels as vocab (optional)
│  │  ├─ vocab.artifact_types.v1.yaml            # Artifact type vocab (geoparquet, pmtiles, cog, pdf, jsonl…)
│  │  └─ vocab.compat.v1.yaml                    # Vocab migrations when terms change
│  └─ linkcheck/                                 # Cross-link/lint rules (EvidenceRef resolvability expectations)
│     ├─ README.md
│     ├─ evidence_ref_schemes.v1.yaml            # Allowed schemes: dcat:// stac:// prov:// doc:// graph:// url://
│     ├─ evidence_ref_resolution.v1.yaml         # Resolver expectations: required fields per scheme, fail-closed rules
│     ├─ catalog_crosslinks.v1.yaml              # DCAT↔STAC↔PROV link rules + required rels
│     ├─ artifact_digest_rules.v1.yaml           # “Every artifact referenced MUST have digest” rules
│     ├─ url_allowlist.v1.yaml                   # If url:// allowed at all, constrain domains / snapshot rules
│     └─ lint_rules.v1.yaml                      # General lint rules (no quarantine links, no missing license, etc.)
│
├─ promotion/                                    # Promotion Contract wiring
│  ├─ README.md                                  # Gate taxonomy + how CI maps A–F to checks
│  ├─ gates/                                     # Gate definitions + thresholds + required artifacts
│  │  ├─ README.md
│  │  ├─ gates.v1.yaml                           # Canonical gate set (A–F) + required checks + failure codes
│  │  ├─ gate_a_identity.v1.yaml                 # Spec-hash inputs/expectations + drift guardrails
│  │  ├─ gate_b_rights.v1.yaml                   # Rights fields required; metadata-only allowance rules
│  │  ├─ gate_c_sensitivity.v1.yaml              # Label requirements + public_generalized derivative rules
│  │  ├─ gate_d_catalogs.v1.yaml                 # Triplet requirements + profile selection hooks + linkcheck rules
│  │  ├─ gate_e_receipts.v1.yaml                 # Receipt fields required + checksum requirements
│  │  ├─ gate_f_policy_contracts.v1.yaml         # Policy parity + schema/contract validation requirements
│  │  └─ gate_codes.v1.yaml                      # Canonical failure codes + policy-safe messages
│  ├─ templates/                                 # Manifest/receipt templates (if not stored elsewhere)
│  │  ├─ README.md
│  │  ├─ promotion_manifest.v1.json              # Template for Promotion Manifest (fields + structure)
│  │  ├─ run_receipt.v1.json                     # Template for Run Receipt (pipeline/index/story/focus)
│  │  ├─ audit_entry.v1.json                     # Optional template for audit ledger entries
│  │  ├─ qa_report.v1.json                       # Optional template for QA summary objects referenced by receipts
│  │  └─ story_publish_receipt.v1.json           # Optional specialized receipt for story publishing
│  └─ classes/                                   # Dataset class defaults (raster/vector/docs) and required checks
│     ├─ README.md
│     ├─ classes.v1.yaml                         # Master map: class → defaults + artifact expectations
│     ├─ vector.v1.yaml                          # Vector defaults (geoparquet + pmtiles, bbox rules, etc.)
│     ├─ raster.v1.yaml                          # Raster defaults (cog + stac items, tiling strategy, etc.)
│     ├─ documents.v1.yaml                       # Docs defaults (pdf/jsonl; OCR caution; citation policy)
│     ├─ timeseries.v1.yaml                      # Time series defaults (station/county, bitemporal requirements)
│     └─ sensitive_location.v1.yaml              # Special class defaults (deny public; generalized derivative required)
│
├─ runtime/                                      # Runtime wiring (non-secret defaults)
│  ├─ README.md
│  ├─ feature_flags/
│  │  ├─ README.md
│  │  ├─ flags.v1.yaml                           # Canonical feature flags + safe defaults
│  │  ├─ flags.by_env.v1.yaml                    # Allowed env overrides (non-secret)
│  │  └─ flags.compat.v1.yaml                    # Deprecated flags + migrations
│  ├─ caching/
│  │  ├─ README.md
│  │  ├─ cache_policy.v1.yaml                    # TTLs, invalidation, vary-by-auth/policy label
│  │  ├─ tile_cache_keys.v1.yaml                 # Tile cache keying rules (must include policy/auth context)
│  │  ├─ http_cache_headers.v1.yaml              # Response header policy (Cache-Control/Vary)
│  │  └─ cdn_rules.v1.yaml                       # Optional CDN constraints (no cross-role leakage)
│  ├─ indexing/
│  │  ├─ README.md
│  │  ├─ postgis_projection.v1.yaml              # Projection build knobs (table naming, required columns)
│  │  ├─ search_index.v1.yaml                    # Text search index knobs (fields allowed, analyzers)
│  │  ├─ graph_index.v1.yaml                     # Graph projection knobs (edge types, redaction)
│  │  ├─ vector_index.v1.yaml                    # Optional semantic index knobs (policy-filtered ingestion)
│  │  └─ tiles_build.v1.yaml                     # Tile generation knobs (zoom ranges, generalization)
│  └─ rate_limits/
│     ├─ README.md
│     ├─ public_api_limits.v1.yaml               # Public limits (policy-safe; deny does not reveal existence)
│     ├─ authenticated_limits.v1.yaml            # Auth limits by role/tenant
│     └─ burst_controls.v1.yaml                  # DoS protection knobs (non-secret)
│
├─ pipelines/                                    # Pipeline runner wiring (non-secret)
│  ├─ README.md
│  ├─ schedules/
│  │  ├─ README.md
│  │  ├─ schedules.v1.yaml                       # Master schedule config (cron refs by dataset class)
│  │  ├─ tier0_anchors.v1.yaml                   # Tier 0 anchor schedules (safe defaults)
│  │  ├─ tier1_enrichers.v1.yaml                 # Tier 1 schedules
│  │  └─ on_demand_only.v1.yaml                  # Datasets that must not auto-run (rights/sensitivity)
│  ├─ runners/
│  │  ├─ README.md
│  │  ├─ runner_defaults.v1.yaml                 # Default runner settings (timeouts/retries; non-secret)
│  │  ├─ container_images.v1.yaml                # Allowed/pinned images (digests), tool versions
│  │  ├─ resource_classes.v1.yaml                # CPU/mem/storage classes by job type
│  │  └─ network_policies.v1.yaml                # Egress allowlist (no direct exfil; policy-safe)
│  └─ dataset_defaults/
│     ├─ README.md
│     ├─ defaults.v1.yaml                        # Global defaults referenced by dataset specs
│     ├─ vector_defaults.v1.yaml                 # CRS, geometry rules, tiling defaults
│     ├─ raster_defaults.v1.yaml                 # COG/STAC defaults, nodata policies
│     ├─ documents_defaults.v1.yaml              # OCR defaults, citation constraints
│     └─ qa_thresholds.v1.yaml                   # Default QA thresholds by dataset class
│
├─ ui/                                           # UI wiring (non-secret)
│  ├─ README.md
│  ├─ layers/                                    # Layer registry defaults, layer groups, display metadata
│  │  ├─ README.md
│  │  ├─ layer_groups.v1.yaml                    # Groups: basemap, hazards, hydrology, demographics, etc.
│  │  ├─ layers.v1.yaml                          # Layer definitions (id, title, dataset refs, render types)
│  │  ├─ basemaps.v1.yaml                        # Basemap selection (sources are public; no keys)
│  │  ├─ styling_tokens.v1.yaml                  # Style tokens (no secret URLs)
│  │  └─ layer_filters.v1.yaml                   # UI filter definitions (display-only)
│  ├─ view_state/                                # View-state schema versions + compatibility rules
│  │  ├─ README.md
│  │  ├─ view_state.schema.v1.json               # Canonical view_state schema (bbox, time, layers, filters)
│  │  ├─ view_state.migrations.v1.yaml           # Migration rules (v1→v2) deterministic transforms
│  │  ├─ share_links.v1.yaml                     # Share link policies (TTL, max size, redact sensitive params)
│  │  └─ view_state.compat.v1.yaml               # Backward compatibility policy and sunset plan
│  └─ policy_badges/                             # UI rendering rules for policy/validation badges (display-only)
│     ├─ README.md
│     ├─ badges.v1.yaml                          # Badge mapping (label → icon/text tokens)
│     ├─ validation_badges.v1.yaml               # QA pass/degraded/fail display rules
│     └─ notice_text.v1.yaml                     # Canonical policy-safe notice strings
│
├─ observability/                                # Observability wiring (policy-safe)
│  ├─ README.md
│  ├─ logging/
│  │  ├─ README.md
│  │  ├─ field_allowlist.v1.yaml                 # Allowed log fields (policy-safe)
│  │  ├─ field_denylist.v1.yaml                  # Fields that must never be logged (tokens, coords, PII)
│  │  ├─ sampling.v1.yaml                        # Sampling rules per component
│  │  └─ retention_guidance.v1.md                # Human guidance (real retention handled by infra)
│  ├─ metrics/
│  │  ├─ README.md
│  │  ├─ metrics_catalog.v1.yaml                 # Metric names + meaning + label constraints
│  │  ├─ slo_targets.v1.yaml                     # SLOs (availability, latency, citation-resolve rate)
│  │  └─ dashboards_map.v1.yaml                  # Maps metrics → dashboards (no URLs required)
│  └─ redaction/
│     ├─ README.md
│     ├─ redaction_rules.v1.yaml                 # Redact patterns (tokens, emails, coords) defense-in-depth
│     ├─ pii_patterns.v1.yaml                    # PII patterns (emails, phone, SSN-like) for scrubbers
│     └─ coordinate_patterns.v1.yaml             # Coordinate/geometry field scrubbers for public logs
│
└─ env/                                          # Example overlays (NO secrets; keys only)
   ├─ README.md                                  # Explains: examples only; secrets live elsewhere
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
