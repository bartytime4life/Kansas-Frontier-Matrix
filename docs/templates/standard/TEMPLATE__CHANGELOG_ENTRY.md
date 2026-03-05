<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/f9ab1fad-199e-4982-8654-9998fd111ae3
title: TEMPLATE — Changelog Entry
type: standard
version: v1
status: published
owners: ["@team/kfm-core"]
created: 2026-03-05
updated: 2026-03-05
policy_label: public
related: ["docs/CHANGELOG.md", "docs/templates/standard/"]
tags: ["kfm", "template", "changelog"]
notes: ["Use for release notes + CHANGELOG entries. Keep entries auditable and governance-safe."]
[/KFM_META_BLOCK_V2] -->

# TEMPLATE — Changelog Entry
Standard, audit-ready changelog entry for Kansas Frontier Matrix (KFM) changes across code, data, policy, and docs.

## Where it fits
- **Primary use:** copy/paste into `CHANGELOG.md` (or your release notes system)
- **Secondary use:** paste into PR description when a change needs extra audit detail

## Acceptable inputs
- One cohesive change (or tightly-related set of changes) with:
  - links to the PR/issue/run
  - evidence references (tests, logs, provenance, digests) when applicable

## Exclusions
- No secrets, tokens, credentials, or internal URLs.
- No restricted/sensitive raw content (include only approved summaries + references).
- No “we think/maybe” without marking it explicitly as **UNKNOWN** and listing verification steps.

---

## Minimal entry
> Use this for small, low-risk changes. Prefer one entry per PR.

### [YYYY-MM-DD] <Short title>
- **Type:** Added | Changed | Fixed | Security | Docs | Policy | Data | Infra | Deprecation
- **Scope:** `<component-or-path>` (e.g., `api/`, `policy/`, `pipeline/`, `ui/`, `data/catalog/`, `docs/`)
- **Status:** CONFIRMED | PROPOSED | UNKNOWN
- **Refs:** PR `<#>` · Issue `<#>` · Run `<run_id>` · ADR `<id>` (as applicable)
- **Owners:** `@owner1` `@owner2`
- **Audit keys (if applicable):** `spec_hash=<sha256-...>` · `outputs_digest=<sha256:...>` · `policy_bundle_hash=<sha256:...>`

**Summary**
- <1–3 bullets; user-facing first>

**User impact**
- <Who is impacted? What changes for them?>

**Rollback**
- <One sentence: what’s the fastest safe rollback?>

---

<details>
<summary><strong>Full entry (use for major / risky / breaking changes)</strong></summary>

> Use this when any of the following are true:
> - Breaking change, migration required, or schema changes
> - Policy/governance changes
> - New dataset promotion, changes to catalogs/provenance, or redaction/sensitivity changes
> - Material performance / cost / reliability impact

### [YYYY-MM-DD] <Short title>

**Header**
- **Type:** Added | Changed | Fixed | Security | Docs | Policy | Data | Infra | Deprecation
- **Severity:** patch | minor | major
- **Scope:** `<component-or-path>`
- **Status:** CONFIRMED | PROPOSED | UNKNOWN
- **Owners:** `@owner1` `@owner2`
- **Reviewers / Approvers:** `@reviewer1` `@reviewer2`
- **Refs:** PR `<#>` · Issue `<#>` · Run `<run_id>` · ADR `<id>` · RFC `<id>` (as applicable)
- **Audit keys (if applicable):**
  - `spec_hash`: `<sha256-...>`
  - `outputs_digest`: `<sha256:...>`
  - `policy_bundle_hash`: `<sha256:...>`
  - `attestation_ref`: `<sigstore/cosign ref or artifact path>`

---

## Summary
- <What changed?> (1–3 bullets)
- <Why now?> (1 bullet)
- <What is the user-visible effect?> (1 bullet)

## Motivation and rationale
- <Problem statement>
- <Why this approach (vs alternatives)?>
- <Links to design discussion / ADR>

## Scope and components
- **In scope:**
  - <component(s), module(s), datasets>
- **Out of scope / explicitly not changed:**
  - <important non-changes>

## User impact and operational impact
- **User-facing changes**
  - <UI/API behavior changes, new capabilities, removed behavior>
- **Operational changes**
  - <SLO, scaling, latency, cost, on-call, monitoring, runbooks>

## Compatibility and breaking changes
- **Breaking?** yes/no
- **If yes:** describe exactly what breaks and how to migrate.
- **Versioning:** `<api_version>` / `<schema_version>` / `<data_contract_version>` (if applicable)

## Migration plan
- **Required?** yes/no
- **Steps**
  1. <step 1>
  2. <step 2>
- **Backfill / reindex needed?** yes/no  
  - If yes: `<what>`, `<expected duration>`, `<throttle/limits>`, `<verification>`

## Rollback plan
- **Fast rollback**
  - <revert PR / disable flag / restore snapshot>
- **Data rollback**
  - <restore prior catalog/assets, or mark as deprecated; include snapshot IDs>
- **Known rollback risks**
  - <e.g., irreversible migrations>

## Validation and tests
> This must be enough for another engineer to reproduce confidence.

- **Local**
  - [ ] unit tests: `<command>`
  - [ ] lint / typecheck: `<command>`
- **CI (fail-closed)**
  - [ ] unit tests pass
  - [ ] integration / contract tests pass
  - [ ] policy checks pass
  - [ ] attestation / signature checks pass (if enabled)
- **Repro / determinism (if pipeline/data/AI touched)**
  - [ ] deterministic rerun matches previous outputs (or change is explained and approved)
  - [ ] inputs are pinned (versions, hashes) and recorded in provenance

## Evidence and audit references
> Prefer references over prose. Store *summaries*, not restricted raw content.

### Primary references
- PR: `<link-or-id>`
- CI run: `<link-or-run-id>`
- Release: `<tag-or-version>` (if already shipped)

### Run record (if applicable)
- run manifest (canonical): `<path-or-artifact>` (e.g., `run_manifest.canonical.json`)
- inputs snapshot: `<path-or-artifact>` (e.g., `inputs.json`)
- outputs manifest: `<path-or-artifact>` (e.g., `outputs.json`)
- validation log: `<path-or-artifact>` (e.g., `validate.log`)

### Artifacts and digests (if applicable)

| Artifact | Location (path/URI) | Digest (sha256) | Notes |
|---|---|---|---|
| `<name>` | `<path>` | `sha256:<...>` | `<what it is>` |

### Provenance and catalogs (if applicable)
- PROV bundle: `<path-or-URI>`
- STAC item/collection: `<path-or-URI>`
- DCAT dataset/distribution: `<path-or-URI>`
- Evidence manifest / bundle: `<path-or-URI>`

## Governance and policy
- **Classification:** public | internal | restricted
- **Sensitivity / redaction impact:** none | changed  
  - If changed: `<what changed>`, `<redaction profile>`, `<redaction receipt ref>`
- **License impact:** none | changed  
  - If changed: `<license(s)>`, `<where recorded>`
- **Policy impact:** none | changed  
  - If changed: `<policy bundle/version/hash>`, `<what rule changed>`, `<policy regression evidence>`

## Architecture invariants check
- [ ] UI/clients do **not** access DB/storage directly (governed API boundary preserved)
- [ ] Core logic does **not** bypass repository/adapter layer
- [ ] AuthN/AuthZ tests exist for any externally exposed endpoint changes
- [ ] Threat model updated if a new external endpoint is introduced

## Docs and comms
- **Docs updated?** yes/no  
  - If yes: `<paths>`
- **Runbook updated?** yes/no  
  - If yes: `<paths>`
- **User announcement needed?** yes/no  
  - If yes: `<channel + summary>`

## Follow-ups
- **TODOs (must be ticketed)**
  - [ ] `<ticket/link>` — <task>
- **Deprecations**
  - `<what>`, `<timeline>`, `<replacement>`

---

### Claims (optional; use for complex entries)
> Use this if you need “cite-or-abstain” within the entry itself.

| Claim ID | Claim | Status (CONFIRMED/PROPOSED/UNKNOWN) | Evidence ref |
|---|---|---|---|
| C1 | `<claim>` | `<status>` | `<evidence ref>` |

</details>

---

## Footnotes
- If any field is **UNKNOWN**, list the smallest verification steps required to make it **CONFIRMED**.

[Back to top](#template--changelog-entry)
