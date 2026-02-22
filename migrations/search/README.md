<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/4c359225-a143-4dd9-b85c-be5bd34c8b1b
title: Search migrations
type: standard
version: v1
status: draft
owners: TBD
created: 2026-02-22
updated: 2026-02-22
policy_label: restricted
related:
  - kfm://doc/UNKNOWN
tags: [kfm, migrations, search, governance, projections]
notes:
  - This README defines conventions for evolving the Search projection safely (schema, analyzers, ranking, and rebuild patterns).
  - Repo-specific runner commands are intentionally not assumed; adapt the “Runner contract” section to your implementation.
[/KFM_META_BLOCK_V2] -->

# Search migrations
Versioned, reversible changes to KFM’s **Search projection** (dataset/story/document discovery).  
**Status:** draft • **Owners:** TBD • **Location:** `migrations/search/`

![status](https://img.shields.io/badge/status-draft-yellow)
![component](https://img.shields.io/badge/component-search-blue)
![store](https://img.shields.io/badge/store-rebuildable%20projection-lightgrey)
![governance](https://img.shields.io/badge/governance-fail--closed-critical)

---

## Quick navigation
- [Why this exists](#why-this-exists)
- [Scope](#scope)
- [Non-negotiable invariants](#non-negotiable-invariants)
- [Directory layout](#directory-layout)
- [Migration format](#migration-format)
- [Runner contract](#runner-contract)
- [Adding a migration](#adding-a-migration)
- [Running migrations](#running-migrations)
- [CI gates and Definition of Done](#ci-gates-and-definition-of-done)
- [Rollback and rebuild](#rollback-and-rebuild)
- [Appendix: templates](#appendix-templates)

---

## Why this exists

KFM treats Search as a **rebuildable projection**, not a source of truth.

- **Canonical truth** lives in: object storage artifacts (Raw/Work/Processed), catalogs (DCAT/STAC/PROV), and the audit ledger.
- **Projections** (including Search) are derived from canonical artifacts and can be rebuilt to recover, reindex, or change schemas without “losing truth.”

This folder exists so Search changes are:
- **reviewable** (PRs),
- **reversible** (down/rollback paths),
- **auditable** (every apply/rebuild emits a receipt),
- **safe** (policy- and evidence-aware).

> NOTE  
> Search results are only trustworthy in KFM if they can be traced back to **EvidenceRefs** that resolve to inspectable evidence.

[Back to top](#search-migrations)

---

## Scope

### ✅ In-scope (this folder)
Search *projection* evolution, e.g.:
- Index/mapping/schema changes (fields, types, stored metadata)
- Analyzer/tokenizer changes (OCR text vs metadata text)
- Ranking/scoring configuration changes
- Ingest pipeline changes that affect indexed document shape
- Alias / index-version switchovers (zero-downtime patterns)
- “Rebuild-required” migrations (when schema change is not in-place)

### ❌ Out-of-scope (belongs elsewhere)
- Transforming source datasets (pipelines in `src/pipelines/...`)
- Changing promotion gates / catalog profiles (catalog validators & contracts)
- Changing governed API behavior (API module + contract tests)
- Any “fix data in place” of canonical artifacts (requires new dataset versions)

[Back to top](#search-migrations)

---

## Non-negotiable invariants

These are **stop-the-line** rules. If a change would violate any of them, the migration must be redesigned.

### Evidence + identity invariants
Every indexed document **MUST** carry enough metadata to map results to inspectable evidence:

- `dataset_version_id`
- `artifact_digest` (or equivalent immutable artifact identifier)
- `evidence_ref`
- `policy_label` (public-safe)
- spatial + temporal extents (for filtering)
- text fields (OCR, metadata, narrative), **only if allowed by policy**

> WARNING  
> If a migration makes it possible for Search to return “raw text hits” that do not map to EvidenceRefs, Search becomes an unverifiable shadow source.

### Policy invariants
- Search must **not** become a side channel that leaks restricted existence or content.
- Search queries from runtime surfaces must be mediated through the **Governed API** (policy enforcement boundary).
- Treat “403 vs 404” and error messages as sensitive: do not reveal restricted existence through error differences.

### Rebuild invariants
- A **rebuild pipeline** must exist and remain functional:
  1) read catalogs for a `dataset_version_id`  
  2) locate processed artifacts by digest/path  
  3) load into projections (Search included)  
  4) validate counts/extents vs catalog metadata  
  5) record a rebuild receipt in the audit ledger

[Back to top](#search-migrations)

---

## Directory layout

This repo may vary, but migrations should be structured so they are:
- ordered,
- self-describing,
- runnable in CI,
- reversible.

### Proposed on-disk layout
```text
migrations/
└─ search/
   ├─ README.md                         # this file
   ├─ 20260222_0001__init_search_v1/     # example (timestamp + sequence + slug)
   │  ├─ meta.json                      # required
   │  ├─ up.(sql|ts|json)               # required (choose one format)
   │  ├─ down.(sql|ts|json)             # required (choose one format)
   │  └─ notes.md                       # optional: rationale, rollout plan, screenshots
   ├─ 20260222_0002__add_policy_label/
   │  ├─ meta.json
   │  ├─ up.(sql|ts|json)
   │  └─ down.(sql|ts|json)
   └─ _shared/                          # optional: helpers used by multiple migrations
      └─ README.md
```

> TIP  
> Prefer timestamp + sequence IDs so ordering is deterministic in CI and across forks.

[Back to top](#search-migrations)

---

## Migration format

Each migration directory should contain:

### `meta.json` (required)
Minimal metadata contract (extend as needed, but don’t remove fields):

```json
{
  "migration_id": "20260222_0002__add_policy_label",
  "title": "Add policy_label to indexed documents",
  "kind": "schema",
  "applies_to": "search_projection",
  "backwards_compatible": true,
  "requires_rebuild": false,
  "data_touching": false,
  "policy_impact": "low",
  "created_at": "2026-02-22",
  "created_by": "TBD",
  "review_required": ["search", "governance"],
  "notes": [
    "Must preserve evidence_ref mapping",
    "Do not index restricted text fields"
  ]
}
```

### `up.*` (required)
- Applies the change.
- Must be **idempotent** or guarded (safe to re-run).
- Must fail closed when the preconditions are not met.

### `down.*` (required)
- Reverts the change **or** performs a safe rollback pattern (e.g., alias switch back).
- If true reversal is unsafe, set `"requires_rebuild": true` and implement rollback as:
  - “switch alias back” + “rebuild old schema from canonical artifacts.”

[Back to top](#search-migrations)

---

## Runner contract

This README does **not** assume which search backend or migration tool you use.  
But whatever runner exists in this repo should implement a minimum contract:

### Required runner behaviors
- **List** migrations in deterministic order
- **Dry-run** a migration (no writes)
- **Apply** migrations with a lock (prevent concurrent applies)
- **Rollback** (apply down or alias switch-back)
- Emit a **run receipt** containing:
  - who/what/when/why
  - migration_id(s)
  - target environment
  - before/after index version or alias targets
  - digests/hashes of applied scripts
  - policy decision summary (if applicable)
  - outcome + duration

### Recommended runner flags
```text
--env <dev|ci|staging|prod>
--dry-run
--to <migration_id>           # migrate up to
--only <migration_id>         # apply just one
--rollback <migration_id>     # down / switch-back
--lock-timeout <seconds>
--require-clean-git           # for CI reproducibility
```

> NOTE  
> If your runner cannot produce an auditable receipt, it is not a governed operation and must not run in production.

[Back to top](#search-migrations)

---

## Adding a migration

### Step-by-step
1) **Create a new directory** using the naming convention.
2) Add `meta.json`, `up.*`, `down.*`.
3) If the migration changes the *document shape*, update the “Indexed document shape” reference (see Appendix).
4) Add/extend tests:
   - schema/mapping validation
   - smoke query tests (known terms return known EvidenceRefs)
   - policy tests (restricted content is not discoverable)
5) Ensure the migration is either:
   - **in-place & reversible**, or
   - **alias-switch + rebuild** (preferred for large breaking changes)

### When to require governance review
Require steward/governance review when the migration:
- adds new indexed fields containing coordinates or sensitive descriptors
- changes analyzers that could surface restricted OCR text
- changes ranking in a way that prioritizes sensitive results
- adds “suggest/autocomplete” features that could leak restricted existence

[Back to top](#search-migrations)

---

## Running migrations

Because runner commands are repo-specific, the examples below are **pseudocode**.

### Local development
```bash
# 1) start your search backend (local container or dev service)
# 2) run a dry-run
<repo-runner> search:migrate --env dev --dry-run

# 3) apply migrations
<repo-runner> search:migrate --env dev

# 4) run smoke tests (must include EvidenceRef resolvability checks)
<repo-runner> test search
```

### CI
CI should:
- spin up an ephemeral search backend
- apply migrations from scratch
- run smoke tests + contract tests
- fail closed if any EvidenceRef cannot resolve

### Staging / production (recommended pattern)
Prefer **zero-downtime** patterns:

1) Create a new index version (e.g., `search_vN+1`)
2) Build it from canonical artifacts (rebuild pipeline)
3) Validate counts/extents + EvidenceRef mapping
4) Atomically switch an alias (e.g., `search_current -> search_vN+1`)
5) Keep old index for quick rollback until confidence threshold is met

[Back to top](#search-migrations)

---

## CI gates and Definition of Done

### CI gates (minimum)
- [ ] Migration scripts lint/validate (syntax + format)
- [ ] Apply-from-zero passes in CI (fresh backend)
- [ ] Rollback test passes (down or alias switch-back)
- [ ] Smoke queries return **EvidenceRefs** (not raw unverifiable hits)
- [ ] EvidenceRefs resolve via evidence resolver for allowed roles
- [ ] Policy tests pass (no restricted leakage through search)
- [ ] Receipt emitted (or CI equivalent artifact) for the migration run

### Definition of Done (PR checklist)
- [ ] `meta.json` complete and accurate
- [ ] `up.*` + `down.*` present
- [ ] Migration is small + focused (one behavioral change)
- [ ] Rebuild path documented (if `requires_rebuild: true`)
- [ ] Any policy-impacting change has governance approval recorded in PR

[Back to top](#search-migrations)

---

## Rollback and rebuild

### Fast rollback
Use one of:
- Apply `down.*` (true reversal), or
- Switch alias back to the previous index version

### Hard rollback (rebuild)
If state is inconsistent or migration was breaking:
1) Restore canonical artifacts + catalogs (if needed)
2) Re-run the rebuild pipeline to regenerate Search projection
3) Validate:
   - counts/extents vs catalogs
   - EvidenceRef resolvability
4) Record a rebuild receipt

> WARNING  
> Do not “patch” canonical artifacts to make Search happy. If canonical data needs changes, produce a new dataset version + receipts.

[Back to top](#search-migrations)

---

## Appendix: templates

<details>
<summary><strong>Template: Indexed document shape (reference)</strong></summary>

This is a *recommended* minimum shape for documents written into the Search projection.

```json
{
  "id": "stable-doc-id",
  "dataset_version_id": "2026-02.abcd1234",
  "artifact_digest": "sha256:...",
  "evidence_ref": "kfm://evidence/...",
  "policy_label": "public",

  "spatial": { "bbox": [-101.1, 38.5, -100.9, 38.7] },
  "temporal": { "from": "1861-01-01", "to": "1861-12-31" },

  "text": {
    "title": "…",
    "body": "…",
    "tags": ["…"]
  }
}
```

Notes:
- If policy forbids text exposure, store only policy-safe metadata and keep text out of the projection.
- Always preserve the mapping to EvidenceRefs.

</details>

<details>
<summary><strong>Template: notes.md (optional)</strong></summary>

```markdown
# Migration rationale

## What changed
- …

## Why
- …

## Risk & rollback
- …

## Validation plan
- Smoke query:
  - query: "…"
  - expected: evidence_ref resolves, dataset_version_id present

## Governance notes
- Any CARE flags / redactions:
  - …
```

</details>

---
_Last updated: 2026-02-22_
