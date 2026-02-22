# data/published — Published zone (governed runtime)

Release-ready **publication manifests and pointers** for dataset versions that are allowed to be served by KFM’s **governed API + UI**.

**Status:** Draft (vNext-aligned)  
**Owners:** Data Stewardship + Maintainers (TBD)  
**Badges:** `PUBLISHED` `governed-runtime` `fail-closed` `evidence-first`

**Navigate:**  
- [Purpose](#purpose)  
- [What belongs here](#what-belongs-here)  
- [How “published” fits the truth path](#how-published-fits-the-truth-path)  
- [Promotion requirements](#promotion-requirements)  
- [Recommended layout](#recommended-layout)  
- [How to add a published dataset version](#how-to-add-a-published-dataset-version)  
- [Operational safety](#operational-safety)  
- [Glossary](#glossary)

---

## Purpose

This directory exists to provide a **single, reviewable, auditable place** to answer:

- “What dataset versions are currently eligible to be served by runtime surfaces?”
- “Where is the **promotion manifest** proving the version passed governance gates?”
- “How do we reproduce / verify what’s being served?”

This is **not** a general storage area and **not** a replacement for the canonical data + catalogs + provenance stores.

> [!NOTE]
> In KFM, “PUBLISHED” is a **governed runtime concept**: what the API/UI are allowed to serve. This folder is an **optional repository-level ‘pointer/index’ surface** to make that state explicit and auditable.

[Back to top](#datapublished--published-zone-governed-runtime)

---

## What belongs here

Keep contents **small, immutable, and reviewable**. Prefer:

- **Promotion manifests** (per dataset version)
- **Published indexes** (curated lists of “servable” dataset versions)
- **Pointer files** that reference canonical artifacts + catalogs by stable IDs/digests/URIs

Avoid storing large binary artifacts here unless you have an explicit “repo-bundled release” requirement (and then prefer `releases/` if your repo uses that pattern).

> [!WARNING]
> Do **not** use this directory as a shortcut around the **trust membrane**.
>
> - Frontends/clients must not fetch data directly from storage or from this folder.
> - Runtime access must go through governed APIs that enforce policy, redaction/generalization, and audit logging.

[Back to top](#datapublished--published-zone-governed-runtime)

---

## How “published” fits the truth path

Conceptually, data moves through these zones and contract surfaces before it can be served:

~~~mermaid
flowchart LR
  A[Upstream Sources] --> B[RAW]
  B --> C[WORK or QUARANTINE]
  C --> D[PROCESSED]
  D --> E[CATALOG Triplet]
  E --> F[Index Builders]
  F --> G[Governed API]
  G --> H[UI Surfaces]
~~~

- **RAW**: immutable acquisition snapshots + checksums + terms  
- **WORK/QUARANTINE**: normalization, QA, redaction candidates; quarantine blocks promotion  
- **PROCESSED**: publishable artifacts in approved formats + checksums  
- **CATALOG Triplet**: DCAT + STAC + PROV + run receipts (cross-linked)  
- **PUBLISHED**: governed runtime surfaces serve only promoted versions that pass gates

[Back to top](#datapublished--published-zone-governed-runtime)

---

## Promotion requirements

A dataset version is “publishable/servable” only if it meets the **Promotion Contract** gates.

### Minimum gates (must pass; fail-closed)

- **Gate A — Identity & versioning**
  - dataset ID stable
  - dataset version ID immutable and derived from a stable `spec_hash`
- **Gate B — Licensing & rights**
  - explicit license and rights/attribution captured
  - unclear licensing → stay in quarantine (default-deny)
- **Gate C — Sensitivity & redaction plan**
  - policy label assigned (e.g., public/restricted)
  - required redaction/generalization obligations recorded in provenance
- **Gate D — Catalog triplet validation**
  - DCAT / STAC / PROV exist, validate, and cross-link resolves
- **Gate E — Run receipt & checksums**
  - run receipt exists per producing run
  - inputs/outputs enumerated with checksums; environment captured
- **Gate F — Policy tests & contract tests**
  - policy tests pass (fixtures-driven)
  - evidence resolution works (at least one resolvable EvidenceRef in CI)
  - API contracts/schemas validate

### Optional but recommended (production posture)

- SBOM + build provenance for pipelines and runtime artifacts
- performance smoke checks (tiles, evidence latency)
- accessibility smoke checks (evidence drawer keyboard nav)

[Back to top](#datapublished--published-zone-governed-runtime)

---

## Recommended layout

Because repository layouts vary, treat the below as **recommended** (not required) patterns.

### Option 1 — Minimal “pointer-only” (recommended)

Store only manifests and indexes; keep canonical artifacts elsewhere.

~~~text
data/published/
  README.md
  published_index.json              # curated list of servable dataset versions (optional)
  manifests/
    <dataset_slug>/
      <dataset_version_id>.json     # promotion manifest (immutable)
~~~

### Option 2 — Repo-bundled published bundle (use sparingly)

Only use this if you have an explicit need to commit a self-contained bundle.

~~~text
data/published/
  README.md
  <dataset_slug>/
    <dataset_version_id>/
      promotion_manifest.json
      catalogs/                     # copies or thin pointers (DCAT/STAC/PROV)
      pointers/                     # pointer files to canonical URIs by digest
      checksums/                    # optional digest lists
~~~

> [!TIP]
> If you need to ship large distribution artifacts, prefer a dedicated release mechanism (for example a `releases/` directory or external object storage) and keep this folder as the **auditable “servable set” index**.

[Back to top](#datapublished--published-zone-governed-runtime)

---

## How to add a published dataset version

1. **Confirm prerequisites exist**
   - processed artifacts + checksums
   - validated catalogs (DCAT/STAC/PROV) with resolvable cross-links
   - run receipt(s) with inputs/outputs and environment capture
   - policy label assignment + any obligations recorded/applied

2. **Generate an immutable promotion manifest**
   - includes dataset slug, dataset version ID, `spec_hash`
   - references artifacts and catalogs by digest/path
   - includes QA status and required approvals (if your governance requires)

3. **Add the manifest under `data/published/manifests/...`**
   - never edit an existing manifest in place
   - if something changes, publish a new dataset version

4. **(Optional) Update `published_index.json`**
   - include the new dataset version ID + manifest digest
   - keep this list curated: it represents what runtime is allowed to serve

5. **Rely on CI to fail-closed**
   - schema validation (catalog profiles, manifest schema)
   - policy tests
   - evidence resolution check
   - link/digest verification

[Back to top](#datapublished--published-zone-governed-runtime)

---

## Operational safety

### Sensitivity and restricted locations

If a dataset includes sensitive locations, culturally restricted sites, private individuals, or vulnerable infrastructure:

- do **not** publish exact coordinates unless policy explicitly permits
- publish generalized geometry / redacted attributes per obligations
- record the redaction/generalization plan in provenance
- ensure runtime errors do not leak restricted dataset existence

### Immutability and rollback

- Treat published manifests as **append-only**.
- Roll forward by publishing a new dataset version.
- Roll back by changing which dataset version is referenced in the published index (if you use one), not by mutating an existing version’s artifacts.

[Back to top](#datapublished--published-zone-governed-runtime)

---

## Glossary

- **dataset_slug**: stable dataset identifier (human-readable)  
- **dataset_version_id**: immutable version identifier derived from a stable spec hash  
- **spec_hash**: stable hash of the dataset version’s canonical spec/config  
- **policy_label**: primary classification input used for allow/deny + obligations  
- **Promotion manifest**: the release record proving a dataset version is promotable/servable  
- **Run receipt**: per-run audit record enumerating inputs/outputs, digests, environment, and policy decision refs  
- **Triplet catalogs**: DCAT (dataset metadata), STAC (asset metadata), PROV (lineage)

---

## Changelog

- **2026-02-22** — Created this README to define the role of `data/published/` as a governed-runtime publication surface.

[Back to top](#datapublished--published-zone-governed-runtime)
