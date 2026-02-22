<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/7a6b7c3e-5b8a-4a2a-9a8d-2f8f7fb9183a
title: Pull Request Template
type: standard
version: v1
status: draft
owners: [TBD]
created: 2026-02-22
updated: 2026-02-22
policy_label: public
related:
  - kfm://doc/kfm-gdg-vnext
tags: [kfm, github, pr-template]
notes:
  - Evidence-first, fail-closed posture: if rights/policy/citations are unclear, do not promote/publish.
[/KFM_META_BLOCK_V2] -->

# Pull Request

> **Evidence-first + governed:** Every user-facing claim (Map / Story / Focus) should be backed by resolvable evidence, with policy applied consistently.
>  
> **Fail-closed:** If licensing, sensitivity, or citations are unclear → block promotion/publish until resolved.

---

## Summary

**What changed (1–3 bullets):**
- 
- 
- 

**Why (user / ops / governance value):**
- 

**Scope / surfaces impacted (check all that apply):**
- [ ] Data pipelines / ingestion
- [ ] Catalogs / provenance (DCAT / STAC / PROV / receipts)
- [ ] Indexing / storage / tiles
- [ ] Governed API
- [ ] UI (Map / Story / Focus)
- [ ] Policy-as-code / enforcement / redaction
- [ ] Infra / deployment / CI
- [ ] Docs only

---

## PR Type

- [ ] Feature
- [ ] Bug fix
- [ ] Refactor / maintenance
- [ ] Security fix
- [ ] Data update (new or refreshed dataset version)
- [ ] Breaking change

---

## Changeset Details

### Architecture invariants (trust membrane)

- [ ] **No direct client → DB/object store access** (clients use governed APIs only)
- [ ] **Backend core logic uses repository interfaces** (no bypass to storage/index)
- [ ] **Policy is enforced consistently** (CI + runtime semantics aligned)

**Notes / exceptions (must justify):**
- 

---

## Data lifecycle + promotion intent (only if data-related)

### Zones touched (check all that apply)
- [ ] RAW (immutable acquisition)
- [ ] WORK / QUARANTINE (normalize, QA, redaction candidates)
- [ ] PROCESSED (publishable artifacts)
- [ ] CATALOG/TRIPLET (DCAT + STAC + PROV + run receipts)
- [ ] PUBLISHED (served via governed runtime)

### Dataset/version inventory
Fill for each dataset version affected:

| dataset_id | dataset_version_id | spec_hash (if used) | policy_label | publish_candidate? | Notes |
|---|---|---|---|---|---|
|  |  |  | public / restricted / … | true / false |  |

### Promotion gates (self-attest)
- [ ] Identity/versioning is deterministic (stable dataset_id; immutable dataset_version_id)
- [ ] License + rights holder are explicit (or stays in QUARANTINE)
- [ ] policy_label assigned; redaction/generalization plan exists if needed
- [ ] Catalog triplet validates (DCAT / STAC / PROV + cross-links)
- [ ] run_receipt(s) exist; inputs/outputs enumerated with checksums/digests
- [ ] Policy tests + contract tests pass (fixtures-driven, deny-by-default)

**Artifacts / evidence links (paths, checksums, or CI outputs):**
- Run receipt(s):
- DCAT record(s):
- STAC collection/item(s):
- PROV bundle(s):
- QA report(s):

---

## Policy, sensitivity, and redaction

**Policy label(s):** `public` / `restricted` / `…`

- [ ] No sensitive-location / culturally restricted / vulnerable-site details are exposed
- [ ] Redaction/generalization transforms are recorded as first-class provenance (PROV)
- [ ] Error responses do not leak existence via 403/404 differences (policy-safe errors)

**If redaction/generalization applied, describe obligations satisfied:**
- 

**Governance review needed?**
- [ ] Legal/rights
- [ ] Community/Indigenous constraints
- [ ] Security
- [ ] Privacy/PII
- [ ] Other: 

---

## Focus Mode / Evidence UX (only if Map/Story/Focus changes)

- [ ] Every new/changed **Map layer** has an evidence view (dataset version, license, policy label, provenance, checksums)
- [ ] Every new/changed **Story claim** links to resolvable evidence
- [ ] Focus Mode changes respect **cite-or-abstain** (hard gate: if citations can’t verify → abstain/reduce scope)
- [ ] Evidence rendering fails closed (invalid/unsigned/unresolvable evidence shown as **untrusted**)

**Screenshots / screen recordings (UI changes):**
- 

---

## API contract + compatibility (only if API changes)

- [ ] Backwards compatible (only additive changes)
- [ ] Breaking change (explain + migration plan below)
- [ ] Response includes needed governance fields when applicable (e.g., dataset_version_id, policy label, audit_ref)
- [ ] Stable error model (policy-safe message + audit_ref)

**API endpoints / schemas affected:**
- 

**Migration / deprecation plan (if breaking):**
- 

---

## Testing & verification

### Automated tests
- [ ] Unit tests added/updated
- [ ] Integration tests added/updated
- [ ] E2E/UI smoke tests (if UI)
- [ ] Schema validation (catalogs/receipts/contracts)
- [ ] Policy tests (fixtures: allow/deny + obligations)

### Manual verification (what you actually did)
- 

### Performance / safety (if relevant)
- [ ] Tile / query performance sanity-checked
- [ ] Evidence resolution latency sanity-checked
- [ ] No PII in logs; logs are redacted appropriately

---

## Security & supply chain (if relevant)

- [ ] Secrets not committed; no sensitive tokens in diffs/logs
- [ ] Dependencies reviewed (or pinned); vulnerabilities addressed where applicable
- [ ] SBOM / build provenance updated (if your build system supports it)
- [ ] Principle of least privilege maintained for services

---

## Rollout, monitoring, and rollback

**Rollout plan (how this reaches users):**
- 

**Monitoring signals (what will tell us it’s healthy):**
- 

**Rollback plan (reversible steps):**
- 

---

## Reviewer notes (help reviewers help you)

**High-risk areas / tricky parts:**
- 

**Suggested reviewers (domains):**
- [ ] Data
- [ ] Policy/Governance
- [ ] API
- [ ] UI/UX + a11y
- [ ] Security
- [ ] Infra/CI

---

## Final checklist (must be true to merge)

- [ ] PR title is clear and references the driving issue/story (if any)
- [ ] Tests pass (or explain why not and why that’s acceptable)
- [ ] Documentation updated where behavior changed
- [ ] Governance gates satisfied for anything promoted/published
- [ ] No “hand-wavy” claims: if evidence can’t be cited, the change fails closed
